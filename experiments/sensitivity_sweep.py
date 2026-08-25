#!/usr/bin/env python3
"""Sweep de sensibilidade ±0,15 nas similaridades + correlação positiva entre gates
(Spearman copula) — limitações declaradas do modelo v1 (bayes_analogia.md §Limitações).
Roda em segundos; superior ao Colab p/ esta escala."""
import numpy as np, json
rng=np.random.default_rng(7)
N=100_000
ANALOGOS={
 'tofersen':(1,1,0.85),'tafamidis':(1,1,0.80),'prion_fail':(0,6,0.55),'ion717':(0,1,0.90),
 'pdo':(4,5,0.70),'cell_brain':(1,3,0.75),'aav_cns':(3,20,0.60),'aso_cns':(3,5,0.75),'mrna_cns':(0,2,0.65)}
def post(k,delta):
    s,n,sim=ANALOGOS[k]; sim=np.clip(sim+delta,0.05,0.99)
    w=max(n*sim,0.5); eff=w*s/n
    return rng.beta(0.5+eff,0.5+(w-eff),size=N),sim**2
def mixgate(keys,delta):
    m=np.zeros(N);ws=0
    for k in keys:
        p,w=post(k,delta); m+=w*p; ws+=w
    return m/ws
gates=['mecanismo','organoide','vetor','clinica']
KEYS={'mecanismo':['tofersen','tafamidis','prion_fail','ion717'],'organoide':['pdo'],
      'vetor':['aav_cns','aso_cns','mrna_cns'],'clinica':['cell_brain']}
res={}
for delta,tag in ((-0.15,'pessimista'),(0.0,'central'),(+0.15,'otimista')):
    ps=[mixgate(KEYS[g],delta) for g in gates]
    # incorrelacionado
    pA0=np.ones(N)
    for p in ps: pA0*=p
    # correlacionado (copula gaussiana rho=0.4 entre gates via ranks)
    rho=0.4
    L=np.linalg.cholesky(np.full((4,4),rho)+np.eye(4)*(1-rho))
    Z=rng.standard_normal((4,N)); Z=L@Z
    U=__import__('scipy.special',fromlist=['ndtr']).ndtr(Z) if False else None
    # ndtr via erf puro (evitar dependência scipy)
    from math import erf, sqrt
    vU=np.vectorize(lambda x:0.5*(1+erf(x/sqrt(2))))
    pc=np.ones(N)
    for i,p in enumerate(ps):
        r=np.argsort(np.argsort(Z[i]))          # rank do fator latente
        order=np.argsort(r)                      # permuta: p ordenado atribuído pelo rank
        p_sorted=np.sort(p)
        pc*=p_sorted[order[:(len(p))]] if False else p_sorted[np.argsort(r)]
    res[tag]={'A_indep':[float(pA0.mean()),float(np.percentile(pA0,5)),float(np.percentile(pA0,95))],
              'A_corr0.4':[float(pc.mean()),float(np.percentile(pc,5)),float(np.percentile(pc,95))],
              'B':None}
    # B sob mesmo delta
    pB=mixgate(KEYS['mecanismo'],delta)*mixgate(KEYS['organoide'],delta)
    res[tag]['B']=[float(pB.mean()),float(np.percentile(pB,5)),float(np.percentile(pB,95))]
print(json.dumps(res,indent=1,default=float))
json.dump(res,open('bayes_results/sensitivity_sweep.json','w'),indent=1,default=float)
