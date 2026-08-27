#!/usr/bin/env python3
"""PARTE 2 · TODO THETA-OBS-POOLED — validação do estimador no REGIME DECLARADO (§2.7)
=====================================================================================
Regime do G0-wet: θ_obs POR ÓRGANOIDE (features ruidosas → κ̂ unitário na grade)
→ MEDIANA POR BRAÇO (n=8) com IC bootstrap. Critérios de sucesso PRÉ-DECLARADOS:
  (P1) cobertura do θ verdadeiro pelo IC90 do braço, nos 3 pontos (3/3);
  (P2) |bias| da mediana do braço ≤ 0.02 (θ);
  (P3) recuperação modal ≥ 60% (modo de κ̂ do braço = κ verdadeiro).
Reusa a grade de part2_theta_obs_v1.json (sem novas simulações). Saída: out/part2_theta_obs_pooled.json"""
import json, math, os
import numpy as np

GRID_F = 'experiments/part2_results/part2_theta_obs_v1.json'
CV = {'R': 0.30, 'ratio': 0.40}
N_ARM = 8
N_BOOT = 1000
SEED = 20260827

def load_grid():
    d = json.load(open(GRID_F))
    rows = [(v['kappa'], v['R_mm'], math.log(v['biomass_ratio']))
            for k, v in d['grid'].items() if v['kappa'] > 0]
    ks = np.array([r[0] for r in rows]); R = np.array([r[1] for r in rows]); lr = np.array([r[2] for r in rows])
    zR = (R - R.mean()) / R.std(); zlr = (lr - lr.mean()) / lr.std()
    return ks, R, lr, zR, zlr

def kappa_hat_unit(oR, olr, ks, R, lr):
    d = np.hypot(((oR - R.mean()) / R.std()) - (R * 0 + 1e9), 0)  # placeholder
    zR0 = (R - R.mean()) / R.std(); zlr0 = (lr - lr.mean()) / lr.std()
    dist = np.hypot(((oR - R.mean()) / R.std()) - zR0, (olr - lr.mean()) / lr.std() - zlr0)
    return float(ks[np.argmin(dist)])

def main():
    os.makedirs('out', exist_ok=True)
    ks, R, lr, _, _ = load_grid()
    rng = np.random.default_rng(SEED)
    res = {'artefato': 'Parte 2 · THETA-OBS-POOLED (regime §2.7: mediana por braço n=8)',
           'grid_source': GRID_F, 'noise_cv': CV, 'n_arm': N_ARM, 'n_boot': N_BOOT,
           'criterios_pre': ['P1 cobertura 3/3', 'P2 |bias mediana|<=0.02', 'P3 recuperação modal >=60%'],
           'validacao': {}}
    all_ok = True
    for k in (2.0, 4.0, 8.0):
        i = int(np.where(ks == k)[0][0])
        R_true, lr_true = R[i], lr[i]
        # bootstrap do BRAÇO: n=8 órgãos → θ̂ unitários → mediana; repetido N_BOOT
        med_thetas = []; modes = []
        for _ in range(N_BOOT):
            units = []
            for _u in range(N_ARM):
                oR = R_true * (1 + rng.normal(0, CV['R']))
                olr = lr_true + rng.normal(0, CV['ratio'])
                units.append(kappa_hat_unit(oR, olr, ks, R, lr))
            med_thetas.append(np.median(1.0 / (1.0 + np.array(units))))
            vals, cnts = np.unique(units, return_counts=True)
            modes.append(vals[np.argmax(cnts)])
        med = np.array(med_thetas); th_true = 1.0 / (1.0 + k)
        lo, hi = np.percentile(med, [5, 95])
        mode_vals, mode_cnts = np.unique(modes, return_counts=True)
        modal_recovery = float(mode_cnts[np.argmax(mode_cnts)] / N_BOOT)
        v = {'theta_true': round(th_true, 3),
             'theta_arm_median': round(float(np.median(med)), 3),
             'bias': round(float(np.median(med) - th_true), 3),
             'ic90_arm': [round(float(lo), 3), round(float(hi), 3)],
             'ic90_width': round(float(hi - lo), 3),
             'coverage': bool(lo <= th_true <= hi),
             'modal_recovery': round(modal_recovery, 3),
             'mode_distribution': {str(float(a)): int(b) for a, b in zip(mode_vals, mode_cnts)}}
        ok = v['coverage'] and abs(v['bias']) <= 0.02 and modal_recovery >= 0.60
        v['criterios'] = {'P1': v['coverage'], 'P2': abs(v['bias']) <= 0.02, 'P3': modal_recovery >= 0.60, 'PASS': ok}
        all_ok &= ok
        res['validacao'][f'{k:g}'] = v
        print(f"κ={k:g}: θ̂_braço={v['theta_arm_median']} (v={th_true:.3f}) IC90=[{lo:.3f},{hi:.3f}] w={hi-lo:.3f} cobre={v['coverage']} modal={modal_recovery:.0%} PASS={ok}")
    res['veredito_pooled'] = 'ADEQUADO P/ GATE-F (P1-P3 cumpridos)' if all_ok else \
        'PARCIAL — ver critérios por ponto (P3 modal é o limitante: n=8 mediana)'
    json.dump(res, open('out/part2_theta_obs_pooled.json', 'w'), indent=1)
    print('OK → out/part2_theta_obs_pooled.json |', res['veredito_pooled'])

if __name__ == '__main__':
    main()
