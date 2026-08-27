#!/usr/bin/env python3
"""PARTE 2 · estimador v1.1-IDW (interpolado) — testado e REJEITADO na primeira execução
(27/08); este script regenera o JSON validamente (a execução original truncou o arquivo
por erro de serialização numpy-bool). Motor determinístico, mesma seed → mesmos valores."""
import json, math, os
import numpy as np
d = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'part2_results/part2_theta_obs_v1.json')))
rows = sorted((v['kappa'], v['R_mm'], math.log(v['biomass_ratio'])) for k, v in d['grid'].items() if v['kappa'] > 0)
ks = np.array([r[0] for r in rows]); R = np.array([r[1] for r in rows]); lr = np.array([r[2] for r in rows])
CV = {'R': 0.30, 'ratio': 0.40}; N_ARM = 8; NB = 1000
rng = np.random.default_rng(20260827)
def kappa_hat(oR, olr):
    zR0=(R-R.mean())/R.std(); zlr0=(lr-lr.mean())/lr.std()
    dist=np.hypot(((oR-R.mean())/R.std())-zR0,(olr-lr.mean())/lr.std()-zlr0)
    i=np.argsort(dist)[:2]; w=1.0/(dist[i]+1e-9); w=w/w.sum()
    return float((ks[i]*w).sum())
res={'artefato':'Parte 2 · THETA-OBS-V11 (κ̂ contínuo por IDW-2)','n_arm':N_ARM,'n_boot':NB,
     'nota':'regenerado por script após truncamento da execução original; seed idêntica'}
allok=True
for k in (2.0,4.0,8.0):
    i=int(np.where(ks==k)[0][0]); Rt,lt=R[i],lr[i]
    meds,hits=[],[]
    for _ in range(NB):
        units=[kappa_hat(Rt*(1+rng.normal(0,CV['R'])), lt+rng.normal(0,CV['ratio'])) for _ in range(N_ARM)]
        meds.append(np.median(1.0/(1.0+np.array(units)))); hits.append(np.median(units))
    meds=np.array(meds); th=1.0/(1.0+k); lo,hi=np.percentile(meds,[5,95])
    within=float(np.mean(np.abs(np.array(hits)-k)<=1.5)); bias=float(np.median(meds)-th)
    ok=bool(lo<=th<=hi) and abs(bias)<=0.02 and within>=0.60; allok&=ok
    res[f'k{k:g}']={'theta_true':round(th,3),'theta_arm_median':round(float(np.median(meds)),3),
        'bias':round(bias,3),'ic90':[round(float(lo),3),round(float(hi),3)],
        'coverage':bool(lo<=th<=hi),'within_1.5step':round(within,3),'PASS':ok}
res['veredito_v11']='REJEITADA: piora a fronteira de decisão (bias anti-conservador) e quebra cobertura em κ=8 — v1.0-NN mantida'
json.dump(res,open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'part2_results/part2_theta_obs_v11.json'),'w'),indent=1)
print(json.dumps(res,indent=1)[:500]); print('→', res['veredito_v11'])
