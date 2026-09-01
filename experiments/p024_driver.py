#!/usr/bin/env python3
"""P-024 DRIVER — multi-species θ* (PARTE 3 Fase 2) · motor v4 EXATO importado intacto.
Espécie via --species (matrix injeta). Bandas de Kt_scale de experiments/xspecies/species_params.json
(grupos A-D; banda≠ponto). Unidades checkpointáveis (retomável como o S3).

DEFINIÇÕES OPERACIONAIS PRÉ-REGISTRADAS (antes de qualquer run; espelham COMPUTE_EVAL §2 + audit):
  escape ......... final_R_mm >= 2.80 (canto do grid 2.828 — dado censurado ⇒ FLAG, nunca raio)
  κ_min(espécie) . menor κ ∈ {1.5,2,3,4,8} com escape=False E R_norm <= 0.90 mm
  θ*_espécie ..... 1/(1+κ_min)  · mouse referência: θ*=0.333 (v1.0, COMPARA-SE)
  pareamento ..... pass1 t=5 (calendário-sim) + pass2 t clock-matched às DUPLICAÇÕES do
                   crescimento LIVRE do próprio braço (untreated run por ponto de banda)
  C0 ............. baseline murina (kcap=0) por job: R≈2.83, T1 (motor-paridade por job)
  observáveis .... final_R_mm, total0, totalf (massa), t_double_sim, escape, wall_s
"""
import argparse, json, math, os, sys, time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ws_9_v5_sweeps_gha import simulate, ANCH, SEED_MV2, SEED_MV1

CKPT = 'out/p024_%s_partial.json' % (os.environ.get('SPECIES') or 'local')
FINAL = 'out/p024_%s.json' % (os.environ.get('SPECIES') or 'local')
SPECIES_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'xspecies', 'species_params.json')
KAPPAS = [1.5, 2.0, 3.0, 4.0, 8.0]
KT0, KR0, KC0 = (10.0, 5.0), (50.0, 10.0), (10.0, 50.0)
CONTAIN_R = 0.90      # pré-registrado (≈ murino 0.819 +10%)
ESCAPE_R = 2.80       # canto do grid (2.828) com tolerância

def sc(v, f): return (v[0] * f, v[1] * f)

def load(): return json.load(open(CKPT)) if os.path.exists(CKPT) else {}
def save(st):
    with open(CKPT, 'w') as f:
        json.dump(st, f, indent=1); f.flush(); os.fsync(f.fileno())

def run_treated(kt, kcap, tl):
    r = simulate(kcap=kcap, seed_mass=SEED_MV2, Kt=kt, Kr=KR0, Kc=KC0, t_lim=tl,
                 tag='x%g_k%g_t%.1f' % (kt[0] / 10.0, kcap, tl), progress=False)
    out = {'R_mm': round(r['final_R_mm'], 3), 'total0': round(r['total0'], 2),
           'totalf': round(r['totalf'], 2), 't_double_sim': r['t_double_sim'],
           'wall_s': r['wall_s']}
    out['escape'] = bool(r['final_R_mm'] >= ESCAPE_R)
    out['amplification'] = round(r['totalf'] / max(r['total0'], 1e-9), 2)
    return out

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--species', default=os.environ.get('SPECIES', 'mouse'))
    a = ap.parse_args()
    os.makedirs('out', exist_ok=True)
    sp = json.load(open(SPECIES_FILE))[a.species]
    band = sorted({sp['Kt_scale']['lo'], sp['Kt_scale']['central'], sp['Kt_scale']['hi']})
    st = load(); t0 = time.time()

    # C0 por job — baseline murina (motor-paridade)
    if 'c0' not in st:
        r = simulate(kcap=0.0, seed_mass=SEED_MV2, tag='C0_BASE', progress=False)
        ok = (abs(r['final_R_mm'] - 2.83) <= 0.05) and (r['totalf'] > r['total0'] * 1.5)
        st['c0'] = {'final_R_mm': round(r['final_R_mm'], 3), 'T1': bool(r['totalf'] > r['total0'] * 1.5), 'pass': bool(ok)}
        save(st)
        assert ok, 'C0 FALHOU: motor divergiu (job abortado, nada colhido)'

    # crescimento livre (untreated) por ponto de banda → âncora de pareamento própria
    for kt_s in band:
        key = 'free_%g' % kt_s
        if key not in st:
            r = simulate(kcap=0.0, seed_mass=SEED_MV2, Kt=sc(KT0, kt_s), Kr=KR0, Kc=KC0,
                         t_lim=5.0, tag=key, progress=False)
            st[key] = {'t_double_sim': r['t_double_sim'], 'R_free_mm': round(r['final_R_mm'], 3)}
            save(st); print('Ckpt:', key, st[key], flush=True)

    # varredura κ × banda × 2 passes
    for kt_s in band:
        kt = sc(KT0, kt_s)
        t2free = st['free_%g' % kt_s]['t_double_sim'] or 1.2
        for k in KAPPAS:
            u = 'b%g_k%g' % (kt_s, k)
            if u not in st:
                st[u] = {'pass1': run_treated(kt, k, 5.0)}
                save(st); print('Ckpt:', u, st[u]['pass1'], flush=True)
            if ('pass2' not in st[u]) and not st[u]['pass1']['escape']:
                t2a = st[u]['pass1']['t_double_sim']
                tl = 5.0 if (not t2a) else min(12.0, max(2.5, 5.0 * t2free / t2a))
                st[u]['pass2'] = run_treated(kt, k, tl); st[u]['t_lim_used'] = round(tl, 2)
                save(st); print('Ckpt:', u, 'pass2', st[u]['pass2'], flush=True)

    # finalização: κ_min, θ*, cenário
    rows = []
    for kt_s in band:
        kt = sc(KT0, kt_s)
        kmin = None
        for k in KAPPAS:
            u = st['b%g_k%g' % (kt_s, k)]
            rn = u.get('pass2', u['pass1'])['R_mm']
            if (not u['pass1']['escape']) and (not u.get('pass2', {}).get('escape', False)) and rn <= CONTAIN_R:
                kmin = k; break
        rows.append({'Kt_scale': kt_s, 'kappa_min': kmin,
                     'theta_star': round(1.0 / (1.0 + kmin), 3) if kmin else None,
                     'R_by_kappa': {str(k): st['b%g_k%g' % (kt_s, k)].get('pass2', st['b%g_k%g' % (kt_s, k)]['pass1'])['R_mm'] for k in KAPPAS},
                     'escape_by_kappa': {str(k): st['b%g_k%g' % (kt_s, k)]['pass1']['escape'] for k in KAPPAS}})
    thetas = [r['theta_star'] for r in rows if r['theta_star']]
    res = {'meta': {'tier': '[SIM]', 'species': a.species, 'group': sp['group'],
                    'band': band, 'kappas': KAPPAS,
                    'defs': 'escape>=2.80 flag · kmin=menor k com R_norm<=0.90mm sem escape · theta=1/(1+kmin)',
                    'c0': st['c0'], 'wall_total_s': round(time.time() - t0, 1)},
           'rows': rows,
           'summary': {'theta_star_values': thetas,
                       'theta_range': [min(thetas), max(thetas)] if thetas else None,
                       'theta_mouse_ref': 0.333}}
    with open(FINAL, 'w') as f:
        json.dump(res, f, indent=1); f.flush(); os.fsync(f.fileno())
    print('COMPLETO →', FINAL, '| thetas:', thetas, flush=True)

if __name__ == '__main__':
    main()
