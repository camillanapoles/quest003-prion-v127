#!/usr/bin/env python3
"""PARTE 2 — Artefato 2.1: Estimador θ_obs v1 + validação por simulação [SIM]
=============================================================================
Primeira peça da tese de continuidade (C049 Parte 2): pesquisa que USA os dados
parametrizados como substrato. O estimador consumirá, no G0-wet, perfis medidos
em organoides; ANTES do wet-lab, validamos o próprio estimador em dados
sintéticos gerados pelo mesmo motor (simulation-based calibration):

  (a) grade-κ de referência: κ∈{1.5, 2, 3, 4, 6, 8} → features (R_mm, biomass_ratio)
      [o gap κ<2 é onde a curva tem informação: exp=1 mostrou contenção só em κ≥4]
  (b) estimador: observação ruidosa (R̂, log-ratiô) → κ̂ por interpolação na grade
      → θ_obs = 1/(1+κ̂)
  (c) validação: em cada κ verdadeiro, 1000 bootstrap com ruído de medição
      (CV organoide publicado: R ~30%, ratio ~40%) → bias, IC90%, cobertura

Saída: out/part2_theta_obs_v1.json — nunca digitar valores.
"""
import json, math, os, time, sys
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))
from ws_9_v5_sweeps_gha import simulate, ANCH, t_double_h

SEED_MV2 = 130.0
KAPPAS = [1.5, 2.0, 3.0, 4.0, 6.0, 8.0]
OUT = 'out/part2_theta_obs_v1.json'

def build_grid(verbose=True):
    """Grade de referência: features por κ (frente + razão de biomassa)."""
    rows = {}
    for k in KAPPAS + [0.0]:
        tag = f'g{k:g}'
        r = simulate(kcap=k, seed_mass=SEED_MV2, tag=tag, progress=False)
        rows['base' if k == 0 else f'{k:g}'] = {
            'kappa': k,
            'R_mm': round(r['final_R_mm'], 3),
            'biomass_ratio': round(r['totalf'] / r['total0'], 3),
        }
        if verbose:
            print(f"  κ={k:g}: R={rows['base' if k==0 else f'{k:g}']['R_mm']}mm ratio={rows['base' if k==0 else f'{k:g}']['biomass_ratio']}", flush=True)
    return rows

def theta_obs_estimator(obs_R, obs_logratio, grid):
    """κ̂ = argmin distância padronizada na grade (features centrados/escala)."""
    ks = np.array([v['kappa'] for key, v in grid.items() if v['kappa'] > 0])
    R = np.array([v['R_mm'] for key, v in grid.items() if v['kappa'] > 0])
    lr = np.array([math.log(v['biomass_ratio']) for key, v in grid.items() if v['kappa'] > 0])
    zR = (R - R.mean()) / R.std(); zlr = (lr - lr.mean()) / lr.std()
    d = (obs_R - R.mean())/R.std()*np.ones_like(zR)*0 + 0  # placeholder p/ clareza
    dz = np.hypot((obs_R - R.mean())/R.std(), 0)  # não usado
    dist = np.hypot(( (obs_R - R.mean())/R.std() ) - zR, ( (obs_logratio - lr.mean())/lr.std() ) - zlr)
    i = int(np.argmin(dist))
    return float(ks[i])

def main():
    os.makedirs('out', exist_ok=True)
    t0 = time.time()
    res = {'artefato': 'Parte 2 · 2.1 estimador θ_obs v1 (sim-based calibration)',
           'motor': 'v5 sobre v4 humano', 'noise_cv': {'R': 0.30, 'ratio': 0.40},
           'n_boot': 1000}
    print('[grade] construindo grade-κ (6+baseline runs)...', flush=True)
    grid = build_grid()
    res['grid'] = grid
    base = grid['base']
    # validação: para cada κ com contenção, gerar observações sintéticas ruidosas e recuperar
    rng = np.random.default_rng(42)
    val = {}
    for k in (2.0, 4.0, 8.0):
        g = grid[f'{k:g}']
        R_true, r_true = g['R_mm'], g['biomass_ratio']
        hats = []
        for _ in range(res['n_boot']):
            oR = R_true * (1 + rng.normal(0, res['noise_cv']['R']))
            olr = math.log(r_true) + rng.normal(0, res['noise_cv']['ratio'])
            hats.append(theta_obs_estimator(oR, olr, grid))
        hats = np.array(hats)
        theta_hats = 1.0 / (1.0 + hats)
        lo, hi = np.percentile(theta_hats, [5, 95])
        theta_true = 1.0 / (1.0 + k)
        val[f'{k:g}'] = {
            'kappa_true': k, 'theta_true': round(theta_true, 3),
            'theta_hat_median': round(float(np.median(theta_hats)), 3),
            'bias_theta': round(float(np.median(theta_hats) - theta_true), 3),
            'ic90': [round(float(lo), 3), round(float(hi), 3)],
            'coverage_of_true': bool(lo <= theta_true <= hi),
            'kappa_hat_modes': {str(kk): int((hats == kk).sum()) for kk in np.unique(hats)},
        }
        print(f"  κ={k:g}: θ̂ mediana={val[f'{k:g}']['theta_hat_median']} (v={theta_true:.3f}) IC90=[{lo:.3f},{hi:.3f}] cobre={val[f'{k:g}']['coverage_of_true']}", flush=True)
    res['validacao'] = val
    res['wall_s'] = round(time.time() - t0, 1)
    # decisão pré-declarada (anti-circularidade §2.7): estimador é ADEQUADO se
    # cobertura ≥ 2/3 nos pontos e bias |θ| ≤ 0.05 no κ central (4)
    ok = sum(v['coverage_of_true'] for v in val.values()) >= 2 and abs(val['4']['bias_theta']) <= 0.05
    res['estimator_verdict_SIM'] = 'ADEQUADO para freeze (critérios pré-declarados)' if ok \
        else 'INSUFICIENTE — melhorar features/grade antes do freeze'
    json.dump(res, open(OUT, 'w'), indent=1)
    print('OK →', OUT, '| veredito:', res['estimator_verdict_SIM'], flush=True)

if __name__ == '__main__':
    main()
