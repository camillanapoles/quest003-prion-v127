#!/usr/bin/env python3
"""WS-9 — Porto Python (mean-field determinístico) do modelo Igel/Fornara 2024
(Zenodo 11093945) + TERMO DE CAPPING V127ΔGPI (inédito) = ensaio in silico do G0.

Fidelidade ao original:
- PART[m, i]: assemblies de tamanho i (i=1..s-1: polímeros; i=s: condensed) por voxel
- Reações: difusão (K1), TEMPLATING (K2 — só com neurônio local NÃO-UPR),
  conversão conformacional/despolimerização catalítica (K3·C), descondensação (K4), condensação (K5)
- UPR: neurônio ativa quando soma local > uprd por uprt tempo → desliga templating na zona
Parâmetros: Params.csv do Zenodo (Kt=[5 10], Kc=[10 50], Kr=[50 10], D0=1000, s=10).
Acréscimo nosso: campo V127ΔGPI c(m) (perfil estacionário WS-7: exp(-r/ℓ));
capping: templating rate × 1/(1 + κ·c) — inibição dominante-negativa da conversão.

Self-tests: (T1) sem V127 → colônia cresce (ΣB_i↑ ao longo do tempo);
           (T2) com κ alto → frente para dentro da casca r* não avança.

Uso: /workspace/.venv-numpy/bin/python ws_9_port.py
"""
import os, json, math
import numpy as np

HERE=os.path.dirname(os.path.abspath(__file__))
OUT=os.path.join(HERE,'ws_9_results'); os.makedirs(OUT,exist_ok=True)

# ---- params (Params.csv 'Neuron Bed') ----
s=10; div=60; L=1.0; D0=1000.0
Kt=np.array([10.0,5.0])     # [templating em tamanho máximo, outros]
Kc=np.array([10.0,50.0])    # [condensation, decondensing]
Kr=np.array([50.0,10.0])    # [conf-change/depol catalítica, ...]
t_lim=5.0; uprd=5.0; uprt=10.0; uprr=6.0; tpr=10.0; N_neur=9

K1=4*D0/((np.arange(1,s+1))*L**2)          # difusão por tamanho
K2=np.array([Kt[1]]*(s-1)+[0.0,Kt[0]])     # templating por tamanho (último=monômero? mantém ordem do original)
K3=np.array([Kr[0]]+[Kr[1]]*(s-1)+[0.0])   # depol catalítica (age com C)
K4=np.array([0.0]+[Kc[0]]*(s-1)+[0.0])     # descondensação
K5=np.array([Kc[1]]*(s-1)+[0.0,0.0])       # condensação

# malha e neurônios (grid 3x3 central como no original)
X,Y=np.meshgrid(np.arange(1,div+1),np.arange(1,div+1))
m_lin=round(uprr+ (div-2*uprr)/2); step=max(1,round((div-2*uprr-1)/2))
neur_pos=[(m_lin+step*i, m_lin+step*j) for i in (-1,0,1) for j in (-1,0,1)]
def disk_mask(cx,cy,r):
    return ((X-cx)**2+(Y-cy)**2)<r**2
tpl_masks=[disk_mask(cx,cy,tpr) for cx,cy in neur_pos]
upr_masks=[disk_mask(cx,cy,uprr) for cx,cy in neur_pos]

def run(kcap=0.0, ell_mm=3.6, R_dep_mm=1.0, px_per_mm=None, dt=5e-4, nrec=60, seed=0):
    rng=np.random.default_rng(seed)
    # escala: div voxels = 1 "L" — interpretamos L=4mm ⇒ px_per_mm=div/4 (declaração nossa)
    px_per_mm=px_per_mm or div/4.0
    P=np.zeros((div,div,s))                 # B_1..B_{s-1}, C(condensed) na última
    c0=(div//2, div//2)
    seed_mask=disk_mask(c0[0],c0[1],2.0)
    n0=np.array([math.ceil(10*s/(i+2)) for i in range(s)])  # aproxima part_n0
    P[seed_mask]=n0/seed_mask.sum()
    upr_t=np.zeros(len(neur_pos))           # tempo acumulado de stress
    upr_on=np.zeros(len(neur_pos),bool)
    # campo V127 (perfil do WS-7: c/c0=exp(-r/ℓ))
    rr=np.hypot(X-c0[0],Y-c0[1])/px_per_mm
    cV=np.exp(-rr/ell_mm) if kcap>0 else np.zeros((div,div))
    rec_t=[]; rec_tot=[]; rec_r=[]; rec_upr=[]
    steps=int(t_lim/dt)
    rec_every=max(1,steps//nrec)
    tp_on=np.ones((div,div),float)
    # pesos por tamanho como arrays (vetorização total)
    Ki_idx=np.arange(s)
    for st in range(steps):
        # UPR (barato: 9 neurônios)
        if st%20==0:
            for n,(um,tm) in enumerate(zip(upr_masks,tpl_masks)):
                if P[um].sum()>uprd:
                    upr_t[n]+=dt*20
                    if upr_t[n]>=uprt and not upr_on[n]: upr_on[n]=True
        if st%20==0:
            tp_on.fill(1.0)
            for n,(um,tm) in enumerate(zip(upr_masks,tpl_masks)):
                if upr_on[n]: tp_on[tm]=0.0
        inhib=(1.0/(1.0+kcap*cV)) if kcap>0 else np.ones((div,div))
        C=P[:,:,s-1]
        dP=np.zeros_like(P)
        # condensação B_i→C (i=0..s-2)
        cond=dt*K5[:s-1][None,None,:]*P[:,:,:s-1]
        dP[:,:,:s-1]-=cond; dP[:,:,s-1]+=cond.sum(axis=2)
        # descondensação C→B1
        dP[:,:,0]+=dt*K4[1]*C; dP[:,:,s-1]-=dt*K4[1]*C
        # templating B_i→B_{i+1} (inibido por V127 e UPR)
        src=dt*K2[None,None,:s-1]*tp_on[:,:,None]*inhib[:,:,None]*P[:,:,:s-1]
        dP[:,:,:s-1]-=src
        dP[:,:,1:s]+=src
        # depol catalítica (C mata B_i, devolve monômero)
        kill=dt*K3[None,None,:s-1]*C[:,:,None]*P[:,:,:s-1]/s
        dP[:,:,:s-1]-=kill
        dP[:,:,0]+=kill.sum(axis=2)
        # difusão (vetorizada nos tamanhos)
        lap=(np.roll(P,1,0)+np.roll(P,-1,0)+np.roll(P,1,1)+np.roll(P,-1,1)-4*P)
        dP+=dt*K1[None,None,:]/(div**2)*lap
        P=np.clip(P+dP,0,None)
        if st%rec_every==0:
            rec_t.append(st*dt); rec_tot.append(float(P.sum()))
            nz=P.sum(axis=2)
            ys,xs=np.nonzero(nz>1e-9)
            rmax=float(np.max(np.hypot(xs-c0[0],ys-c0[1]))/px_per_mm) if len(xs) else 0.0
            rec_r.append(rmax); rec_upr.append(float(upr_on.mean()))
    return {'t':rec_t,'total':rec_tot,'r_mm':rec_r,'upr_frac':rec_upr,
            'final_R_mm':rec_r[-1] if rec_r else 0.0,'upr_final':rec_upr[-1] if rec_upr else 0}

# ---- SELF-TESTS ----
base=run(kcap=0.0)
t1_pass=base['total'][-1]>base['total'][0]*1.5
treated=run(kcap=8.0)   # κ·c0=8 → θ≈1/8 (capping forte)
t2_pass=treated['final_R_mm']<base['final_R_mm']
# varredura θ (κ = 1/θ na normalização do WS-7)
sweep=[]
for kcap in (0,0.5,1,2,4,8,16):
    r=run(kcap=kcap)
    sweep.append({'kcap':kcap,'theta_ref':round(1.0/(1.0+kcap),3),'final_R_mm':round(r['final_R_mm'],2),'total':round(r['total'][-1],1)})
res={'self_tests':{'T1_cresce_sem_V127':bool(t1_pass),'T2_contem_com_V127':bool(t2_pass)},
     'baseline':{'final_R_mm':round(base['final_R_mm'],2),'total_final':round(base['total'][-1],1)},
     'theta_sweep':sweep,
     'nota':'Port mean-field do Igel 2024 (params Zenodo) + capping V127ΔGPI (κ·c inibe templating); r* emerge da varredura; validação fina exige port estocástico completo (próx. passo).'}
json.dump(res,open(os.path.join(OUT,'ws_9_insilico.json'),'w'),indent=1,ensure_ascii=False)
print(json.dumps(res,indent=1,ensure_ascii=False))
