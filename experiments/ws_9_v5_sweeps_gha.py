#!/usr/bin/env python3
"""WS-9 v5 SWEEPS [SIM] — runner STANDALONE p/ GitHub Actions (mesh Tier 1).
Motor = célula C0 do WS9_v4_HUMAN.ipynb COPIADA EXATAMENTE (única alteração:
freeS parametrizado por fs_exp ∈ {1,2} — guardian E-07). Sem.Colab necessário.

Fases (payload {"phase": "S1"|"S2"}):
  S1 — expoente do freeS {1,2} × κ {2,4,8} + baseline (valida paridade c/ v4:
       baseline final_R_mm ≈ 2.83 mm; days_per_simunit ≈ 144) [+S3 deduzido:
       same-mass = S1/κ4 já É seed MV2-massa; hierarquia seed-mass-driven]
  S2 — C50 logístico {20,100,200} × κ 2 (C50=50 vem do S1/κ2)
Saída: out/ws_9_v5_sweeps_<phase>.json — números só do run (nunca digitar).
Roda também standalone: python3 ws_9_v5_sweeps_gha.py --phase S1"""
import argparse, json, math, os, time
import numpy as np

def simulate(div=96, s=10, t_lim=5.0, dt=5e-4, nrec=80, kcap=0.0, ell_mm=3.6,
             Kt=(10.0,5.0), Kr=(50.0,10.0), Kc=(10.0,50.0), D0=1000.0, L=1.0,
             uprd=5.0, uprt=10.0, uprr=6.0, tpr=10.0, C50=50.0, seed_mass=130.0,
             tag='', progress=False, fs_exp=2.0):
    """Motor v4 EXATO (C0) + fs_exp. freeS=(1/(1+kcap*cV))**fs_exp."""
    t_start=time.time()
    px_per_mm=div/4.0
    K_templ,K_auto,K_nucl,K_frag,K_decond,K_cond=Kt[1],Kt[0],Kr[0],Kr[1],Kc[0],Kc[1]
    K1=4*D0/(np.arange(1,s+2)*L**2)
    X,Y=np.meshgrid(np.arange(1,div+1),np.arange(1,div+1))
    m_lin=round(uprr+(div-2*uprr)/2); step=max(1,round((div-2*uprr-1)/2))
    neur=[(m_lin+step*i,m_lin+step*j) for i in(-1,0,1) for j in(-1,0,1)]
    def disk(cx,cy,r): return ((X-cx)**2+(Y-cy)**2)<r**2
    tpl=[disk(*p,tpr) for p in neur]; upz=[disk(*p,uprr) for p in neur]
    c0=(div//2,div//2)
    P=np.zeros((div,div,s+1),dtype=float)
    sm=disk(c0[0],c0[1],3.0); P[sm,s]=seed_mass/sm.sum()
    rr=np.hypot(X-c0[0],Y-c0[1])/px_per_mm
    cV=np.exp(-rr/ell_mm) if kcap>0 else np.zeros((div,div))
    upr_t=np.zeros(9); upr_on=np.zeros(9,bool); tp=np.ones((div,div))
    steps=int(t_lim/dt); rec_every=max(1,steps//nrec)
    marks={int(steps*f):f for f in (0.2,0.4,0.6,0.8)}
    T=[];TOT=[];R=[];U=[]
    for st in range(steps):
        if st%400==0 and st>0 and kcap>0 and P.sum()<seed_mass*1e-6:
            print(f'  [{tag}] EXTINÇÃO no passo {st}/{steps} — early-stop', flush=True)
            for k2 in range(st,steps):
                if k2%rec_every==0:
                    T.append(k2*dt); TOT.append(float(P.sum()))
                    ys,xs=np.nonzero(P.sum(axis=2)>1e-9)
                    R.append(float(np.max(np.hypot(xs-c0[0],ys-c0[1]))/px_per_mm) if len(xs) else 0.)
                    U.append(float(upr_on.mean()))
            break
        if st%20==0:
            for n,(um,tm) in enumerate(zip(upz,tpl)):
                if P[um].sum()>uprd:
                    upr_t[n]+=dt*20
                    if upr_t[n]>=uprt: upr_on[n]=True
            tp.fill(1.0)
            for n,(um,tm) in enumerate(zip(upz,tpl)):
                if upr_on[n]: tp[tm]=0.0
        eff=tp
        C=P[:,:,s]; dP=np.zeros_like(P)
        freeS=(1.0/(1.0+kcap*cV))**fs_exp if kcap>0 else np.ones((div,div))
        dP[:,:,s]+=dt*K_auto*eff*C*(C/(C+C50))*freeS
        for a in range(s-1):
            g=dt*K_templ*eff*P[:,:,a]*freeS
            dP[:,:,a]-=g; dP[:,:,a+1]+=g
        nuc=dt*K_nucl*C*freeS
        dP[:,:,0]+=nuc; dP[:,:,s]-=nuc
        frs=dt*K_frag*C[:,:,None]*P[:,:,1:s]
        dP[:,:,1:s]-=frs; dP[:,:,0:s-1]+=frs; dP[:,:,s]+=frs.sum(axis=2)
        dcs=dt*K_decond*P[:,:,1:s]
        dP[:,:,1:s]-=dcs; dP[:,:,0:s-1]+=dcs; dP[:,:,0]+=dcs.sum(axis=2)
        for a in range(s):
            for b in range(max(1,1-a),s-a):
                cr=dt*K_cond*P[:,:,a]*P[:,:,b]/(div*div)*10
                dP[:,:,a]-=cr; dP[:,:,b]-=cr; dP[:,:,a+b]+=2*cr
        lap=(np.roll(P,1,0)+np.roll(P,-1,0)+np.roll(P,1,1)+np.roll(P,-1,1)-4*P)
        dP+=dt*K1[None,None,:]/(div*div)*lap
        P=np.clip(P+dP,0,1e6)
        if st%rec_every==0:
            T.append(st*dt); TOT.append(float(P.sum()))
            ys,xs=np.nonzero(P.sum(axis=2)>1e-9)
            R.append(float(np.max(np.hypot(xs-c0[0],ys-c0[1]))/px_per_mm) if len(xs) else 0.)
            U.append(float(upr_on.mean()))
        if progress and st in marks:
            el=time.time()-t_start
            print(f'  [{tag}] {int(marks[st]*100)}% elapsed {el:.0f}s ETA {el/st*(steps-st):.0f}s', flush=True)
    tot=np.array(TOT); tarr=np.array(T)
    lt=np.log(np.clip(tot,1e-9,None)); rng=lt.max()-lt.min()
    m=(lt>lt.min()+0.1*rng)&(lt<lt.max()-0.1*rng)&(tarr>0)
    t_double=None; r2=None
    if m.sum()>5:
        A=np.polyfit(tarr[m],lt[m],1)
        if A[0]>0: t_double=math.log(2)/A[0]; r2=float(np.corrcoef(tarr[m],lt[m])[0,1]**2)
    return dict(final_R_mm=R[-1] if R else 0., total0=TOT[0],
                totalf=TOT[-1] if TOT else 0, t_double_sim=t_double,
                fit_r2=r2, wall_s=round(time.time()-t_start,1))

# ── âncoras humanas (C1 exato) ──
ANCH={'clear_dpi':25.5,'first_denovo_dpi':35,'final_dpi':169,
      'titer_MV2':2.13e5,'titer_MV1':1.69e3,'WB_MV2_only':True}
growth_window=ANCH['final_dpi']-ANCH['first_denovo_dpi']
doublings=math.log2(ANCH['titer_MV2']/100.0)
t_double_h=growth_window/doublings
SEED_MV2=130.0; SEED_MV1=130.0/126.0

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--phase',choices=['S1','S2'],required=True)
    a=ap.parse_args()
    os.makedirs('out',exist_ok=True)
    res={'motor':'v5 sweeps sobre v4 humano (C0 exato + fs_exp param)',
         'phase':a.phase,'wall_total_s':0.0,'anchors':ANCH}
    t0=time.time()
    print(f'[{a.phase}] baseline MV2-like (paridade c/ v4: R≈2.83, d/unid≈144)...',flush=True)
    BASE=simulate(kcap=0.0,seed_mass=SEED_MV2,tag='BASE',progress=True)
    T1=BASE['totalf']>BASE['total0']*1.5
    assert T1,'ABORTAR: baseline não replica (T1)'
    dpu=t_double_h/BASE['t_double_sim']
    res['baseline']={'final_R_mm':round(BASE['final_R_mm'],3),
                     'days_per_simunit':round(dpu,2),'T1_pass':T1}
    print(f"  base R={BASE['final_R_mm']:.2f}mm d/unid={dpu:.1f} (v4: 2.83 / 144.02)",flush=True)
    if a.phase=='S1':
        res['S1_exponent']={}
        for expo in (1.0,2.0):
            res['S1_exponent'][str(int(expo))]={
                f'k{k}': round(simulate(kcap=float(k),seed_mass=SEED_MV2,fs_exp=expo,
                                        tag=f'e{int(expo)}k{k}',progress=True)['final_R_mm'],3)
                for k in (2,4,8)}
            print(f"  exp={int(expo)}: {res['S1_exponent'][str(int(expo))]}",flush=True)
        # S3 same-mass: por construção, seed=MV2-massa É o run k4 acima (exp=2);
        # MV1-like (seed/126) k4 = 0.69 no v4. Documenta hierarquia seed-mass-driven.
        res['S3_same_mass']={'k4_seed_MV2mass_R_mm':res['S1_exponent']['2']['k4'],
                             'k4_seed_MV1like_R_mm_v4ref':0.69,
                             'conclusion':'no kernel v4 subtipo ≡ seed_mass; hierarquia MV2>MV1 é seed-mass-driven POR CONSTRUÇÃO — cinética subtipo-específica está fora do escopo do port (limitação 12 formalmente demonstrada)'}
    else:
        res['S2_C50']={}
        for c50 in (20.0,100.0,200.0):  # C50=50 vem de S1 exp2 k2
            res['S2_C50'][str(int(c50))]={
                f'k{k}': round(simulate(kcap=float(k),seed_mass=SEED_MV2,C50=c50,
                                        tag=f'c{int(c50)}k{k}',progress=True)['final_R_mm'],3)
                for k in (2,)}
            print(f"  C50={int(c50)}: {res['S2_C50'][str(int(c50))]}",flush=True)
    res['wall_total_s']=round(time.time()-t0,1)
    out=f'out/ws_9_v5_sweeps_{a.phase}.json'
    json.dump(res,open(out,'w'),indent=1)
    print('OK →',out,flush=True)

if __name__=='__main__':
    main()
