# ================================================================
# QUEST 003 — WS-9: ENSAIO IN SILICO DO G0 (Colab)
# Port mean-field do modelo Igel/Fornara 2024 (iScience; Zenodo 11093945)
# + TERMO DE CAPPING V127ΔGPI (inédito) — varredura de θ com IC do WS-8
# Uso: Colab novo → Runtime CPU já basta (GPU opcional p/ 3D depois)
#      → rodar esta célula. Baixa ws_9_insilico.json no final.
# ================================================================
import json, math, time
import numpy as np
import matplotlib.pyplot as plt

T0=time.time()

# ---- parâmetros Params.csv (Zenodo, 'Neuron Bed') ----
s=10; div=96; L=1.0; D0=1000.0
Kt=np.array([10.0,5.0]); Kc=np.array([10.0,50.0]); Kr=np.array([50.0,10.0])
t_lim=5.0; uprd=5.0; uprt=10.0; uprr=6.0; tpr=10.0; N_neur=9

K1=4*D0/((np.arange(1,s+1))*L**2)
K2=np.array([Kt[1]]*(s-1)+[0.0,Kt[0]])
K3=np.array([Kr[0]]+[Kr[1]]*(s-1)+[0.0])
K4=np.array([0.0]+[Kc[0]]*(s-1)+[0.0])
K5=np.array([Kc[1]]*(s-1)+[0.0,0.0])

X,Y=np.meshgrid(np.arange(1,div+1),np.arange(1,div+1))
m_lin=round(uprr+(div-2*uprr)/2); step=max(1,round((div-2*uprr-1)/2))
neur_pos=[(m_lin+step*i,m_lin+step*j) for i in (-1,0,1) for j in (-1,0,1)]
def disk(cx,cy,r): return ((X-cx)**2+(Y-cy)**2)<r**2
tpl=[disk(cx,cy,tpr) for cx,cy in neur_pos]
upr_z=[disk(cx,cy,uprr) for cx,cy in neur_pos]
c0=(div//2,div//2)

def run(kcap=0.0, ell_mm=3.6, dt=5e-4, nrec=80):
    px_per_mm=div/4.0
    P=np.zeros((div,div,s))
    sm=disk(c0[0],c0[1],2.0)
    n0=np.array([math.ceil(10*s/(i+2)) for i in range(s)],float)
    P[sm]=n0/sm.sum()
    rr=np.hypot(X-c0[0],Y-c0[1])/px_per_mm
    cV=np.exp(-rr/ell_mm) if kcap>0 else np.zeros((div,div))
    steps=int(t_lim/dt); rec_every=max(1,steps//nrec)
    upr_t=np.zeros(9); upr_on=np.zeros(9,bool); tp_on=np.ones((div,div))
    T=[];TOT=[];R=[];U=[]
    for st in range(steps):
        if st%20==0:
            for n,(um,tm) in enumerate(zip(upr_z,tpl)):
                if P[um].sum()>uprd:
                    upr_t[n]+=dt*20
                    if upr_t[n]>=uprt: upr_on[n]=True
            tp_on.fill(1.0)
            for n,(um,tm) in enumerate(zip(upr_z,tpl)):
                if upr_on[n]: tp_on[tm]=0.0
        inhib=1.0/(1.0+kcap*cV) if kcap>0 else np.ones((div,div))
        C=P[:,:,s-1]; dP=np.zeros_like(P)
        cond=dt*K5[:s-1][None,None,:]*P[:,:,:s-1]
        dP[:,:,:s-1]-=cond; dP[:,:,s-1]+=cond.sum(axis=2)
        dP[:,:,0]+=dt*K4[1]*C; dP[:,:,s-1]-=dt*K4[1]*C
        src=dt*K2[None,None,:s-1]*tp_on[:,:,None]*inhib[:,:,None]*P[:,:,:s-1]
        dP[:,:,:s-1]-=src; dP[:,:,1:s]+=src
        kill=dt*K3[None,None,:s-1]*C[:,:,None]*P[:,:,:s-1]/s
        dP[:,:,:s-1]-=kill; dP[:,:,0]+=kill.sum(axis=2)
        lap=(np.roll(P,1,0)+np.roll(P,-1,0)+np.roll(P,1,1)+np.roll(P,-1,1)-4*P)
        dP+=dt*K1[None,None,:]/(div**2)*lap
        P=np.clip(P+dP,0,None)
        if st%rec_every==0:
            T.append(st*dt); TOT.append(float(P.sum()))
            ys,xs=np.nonzero(P.sum(axis=2)>1e-9)
            R.append(float(np.max(np.hypot(xs-c0[0],ys-c0[1]))/px_per_mm) if len(xs) else 0.)
            U.append(float(upr_on.mean()))
    return dict(t=T,total=TOT,r=R,upr=U,final_R_mm=R[-1] if R else 0.)

# ---- baseline + sweep ----
base=run(0.0)
print("T1 (cresce sem V127):", base['total'][-1]>base['total'][0]*1.5, "| R_final =",round(base['final_R_mm'],2),"mm")
sweep=[]; curves={}
for kcap in (0.5,1,2,4,8,16,32):
    r=run(kcap)
    sweep.append(dict(kcap=kcap, theta=round(1/(1+kcap),3),
                      final_R_mm=round(r['final_R_mm'],2),
                      growth_pct=round(100*(r['total'][-1]/r['total'][0]-1),1)))
    curves[kcap]=r['r']
    print(f"κ={kcap:>4} θ={1/(1+kcap):.3f}  R_final={r['final_R_mm']:.2f}mm  crescimento={100*(r['total'][-1]/r['total'][0]-1):.1f}%")

t2=min(sweep,key=lambda x:x['final_R_mm'])['final_R_mm']<base['final_R_mm']

# ---- figura: frentes vs tempo por θ ----
fig,ax=plt.subplots(1,2,figsize=(11,4))
for k,r in curves.items(): ax[0].plot(base['t'],r,label=f"κ={k} (θ={1/(1+kcap):.2f})")
ax[0].plot(base['t'],base['r'],'k--',lw=2,label='sem V127')
ax[0].set_xlabel('tempo (adim.)'); ax[0].set_ylabel('raio da frente (mm)'); ax[0].legend(fontsize=7); ax[0].set_title('Frente priônica vs capping V127ΔGPI')
ax[1].plot([x['theta'] for x in sweep],[x['final_R_mm'] for x in sweep],'o-')
ax[1].set_xlabel('θ (replicação/capping)'); ax[1].set_ylabel('R final (mm)'); ax[1].axhline(base['final_R_mm'],ls='--',c='gray'); ax[1].set_title('Curva de resposta — o θ* crítico')
plt.tight_layout(); plt.savefig('ws_9_insilico.png',dpi=140)

res=dict(self_tests=dict(T1_cresce=bool(base['total'][-1]>base['total'][0]*1.5),T2_contem=bool(t2)),
         baseline=dict(final_R_mm=round(base['final_R_mm'],2),growth_pct=round(100*(base['total'][-1]/base['total'][0]-1),1)),
         theta_sweep=sweep, runtime_s=round(time.time()-T0,1))
json.dump(res,open('ws_9_insilico.json','w'),indent=1)
print(json.dumps(res,indent=1))


try:
    from google.colab import files as _gfiles  # derivado do notebook Colab; no-op fora do Colab
    _gfiles.download('ws_9_insilico.png')
    _gfiles.download('ws_9_insilico.json')
except Exception:
    pass
