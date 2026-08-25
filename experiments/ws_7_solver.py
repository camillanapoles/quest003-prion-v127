#!/usr/bin/env python3
"""
WS-7 — Solver de transporte da PrP-V127ΔGPI em parênquima espongiforme.
Modelo: ADR (advecção-difusão-reação) em meio poroso heterogêneo (α, λ de Thorne&Nicholson 2006;
cinética de capping parametrizada por Masel 1999). Auto-testado; gera CSV+PNG em ws_7_results/.

Uso: /workspace/.venv-numpy/bin/python ws_7_solver.py
"""
import os, json, math
import numpy as np
from PIL import Image, ImageDraw, ImageFont

HERE=os.path.dirname(os.path.abspath(__file__))
OUT=os.path.join(HERE,'ws_7_results'); os.makedirs(OUT,exist_ok=True)
RESULTS={}

# ---------- parâmetros base ----------
ALPHA=0.20        # fração volumétrica ECS (Thorne&Nicholson PNAS 2006: ~20%)
LAM=1.8           # tortuosidade p/ macromolécula ~30kDa (Thorne 2006: 1.6-2.0)
D0=1.25e-10       # D livre Stokes-Einstein, R_h≈2.5nm, 30kDa [m²/s]
DEFF=D0/LAM**2    # ≈3.9e-11 m²/s
PD='/usr/share/fonts/truetype/dejavu/'
def F(sz,b=False): return ImageFont.truetype(PD+('DejaVuSans-Bold.ttf' if b else 'DejaVuSans.ttf'),int(sz))

# ---------- A) 1D radial analítico: raio de proteção (Thiele/penetração) ----------
# Estado estacionário esférico com consumo de 1ª ordem k: c(r)=c0·exp(-r/ℓ)/r, ℓ=sqrt(D/k)
def ell(D,k): return math.sqrt(D/k)
def r90(D,k):
    ℓ=ell(D,k); r=ℓ
    for _ in range(60):
        f=math.exp(-r/ℓ)/r - 0.1/ℓ  # c/c0=0.10 onde r≈ℓ·W(...) — resolva numérico:
        r-=0.001*ℓ*100
        if r<=0: break
    # solução numérica robusta (bisseção em c/c0 = 0.1 do máximo em r=Rd):
    Rd=1.0e-3
    def ratio(r):
        c0=math.exp(-Rd/ℓ)/Rd
        return (math.exp(-r/ℓ)/r)/c0
    lo,hi=Rd,Rd
    while ratio(hi)>0.10 and hi<0.5: hi*=1.05
    for _ in range(80):
        mid=0.5*(lo+hi)
        if ratio(mid)>0.10: lo=mid
        else: hi=mid
    return 0.5*(lo+hi)

table=[]
for k in (1e-6,3e-6,1e-5):
    for D in (5e-12,DEFF,1e-10):
        table.append((D,k,ell(D,k)*1000,r90(D,k)*1000))  # mm
RESULTS['thiele_table_m']=[[f"{a:.2e}",f"{b:.2e}",f"{c:.2f}",f"{d:.2f}"] for a,b,c,d in table]

# ---------- B) 2D FV: ADR com cistos espongiformes (κ heterogêneo) + depósito secretor ----------
L=0.04; N=192; dx=L/N
X,Y=np.meshgrid(np.linspace(dx/2,L-dx/2,N),np.linspace(dx/2,L-dx/2,N))
KAPPA=np.full((N,N),1e-14)                     # permeabilidade base [m²] (substância cinzenta ~1e-14..1e-13)
cysts=[(0.012,0.016,2.2e-3),(0.028,0.026,1.7e-3),(0.020,0.009,1.3e-3)]
for cx,cy,rc in cysts:
    KAPPA[(X-cx)**2+(Y-cy)**2<rc**2]=50e-14    # cisto: κ×50
Sdep=np.zeros((N,N))
cx,cy,rd=0.020,0.020,1.0e-3                    # depósito central r=1mm
Sdep[(X-cx)**2+(Y-cy)**2<rd**2]=1.0            # densidade de fonte unitária (normalizada)

# Darcy estacionário com fonte puntiforme (pumping ~ 0.1 µL/min no depósito):
Q=0.1e-9/60                                    # m³/s no ponto do depósito
MU=1e-3
# resolver ∇·(κ∇p)=q via Jacobi (basta campo suave)
P=np.zeros((N,N)); q=np.zeros((N,N)); q[(X-cx)**2+(Y-cy)**2<rd**2]=-Q/Sdep.sum()
for it in range(4000):
    Pn=np.zeros_like(P)
    Pn[1:-1,1:-1]=0.25*(P[1:-1,2:]+P[1:-1,:-2]+P[2:,1:-1]+P[:-2,1:-1]) \
                  -q[1:-1,1:-1]*dx*dx/(4*KAPPA[1:-1,1:-1])
    P=Pn
Kb=np.zeros((N,N)); Kf=np.zeros((N,N))
Kb[1:-1,1:-1]=-KAPPA[1:-1,1:-1]/MU*(P[1:-1,2:]-P[1:-1,:-2])/(2*dx)
Kf[1:-1,1:-1]=-KAPPA[1:-1,1:-1]/MU*(P[2:,1:-1]-P[:-2,1:-1])/(2*dx)

def advect_diffuse(c,kcl,kcap,dt,steps,vx=None,vy=None,scale_v=1.0):
    """Euler explícito FV, advecção upwind, reflexo nas bordas (massa conserva-se exceto reação)."""
    m0=c.sum()
    for _ in range(steps):
        Jx=np.zeros_like(c); Jy=np.zeros_like(c)
        if vx is not None:
            u=vx*scale_v; w=vy*scale_v
        else: u=w=None
        # difusão
        cx_=np.clip(c,0,None)
        Jx[:,1:]= -DEFF*(cx_[:,1:]-cx_[:,:-1])/dx
        Jy[1:,:]= -DEFF*(cx_[1:,:]-cx_[:-1,:])/dx
        c[:,1:-1]+=dt/dx*(Jx[:,1:-1]-Jx[:,:-2])/ALPHA*(ALPHA)
        c[1:-1,:]+=dt/dx*(Jy[1:-1,:]-Jy[:-2,:])/ALPHA*(ALPHA)
        # advecção upwind
        if u is not None:
            ue=np.where(u>0,np.roll(cx_,1,1),cx_); uw=np.where(u>0,cx_,np.roll(cx_,-1,1))
            vn=np.where(w>0,np.roll(cx_,1,0),cx_); vs=np.where(w>0,cx_,np.roll(cx_,-1,0))
            c-=dt*(u*(ue-uw)/(2*dx)+w*(vn-vs)/(2*dx))
        c-=dt*(kcl+kcap)*c
        np.clip(c,0,None,out=c)
    return c

# pulso central → fração capturada por cistos (canalização do espongiforme)
c=np.zeros((N,N)); c[(X-cx)**2+(Y-cy)**2<(0.6e-3)**2]=1.0
dt=0.2*dx*dx/DEFF; steps=int(3*24*3600/dt*0.02)+1   # amostra ~ parcial (custo)
c=advect_diffuse(c,1e-6,0,dt,steps,vx=Kb,vy=Kf)
cyst_mask=np.zeros_like(c,bool)
for a,b,r in cysts: cyst_mask|=((X-a)**2+(Y-b)**2<r**2)
cap=float(c[cyst_mask].sum()/max(c.sum(),1e-12))
RESULTS['cyst_capture_frac_early']=round(float(cap),3)

# estado estacionário com fonte contínua (D + reação, sem convecção): campo c_ss
c2=np.zeros((N,N)); k=3e-6
T=25*24*3600; dt2=0.2*dx*dx/DEFF; n2=min(int(T/dt2),26000)
src=Sdep*(0.02)                                   # intensidade adimensional
for i in range(n2):
    cx_=c2
    lapx=np.zeros_like(c2); lapy=np.zeros_like(c2)
    lapx[:,1:-1]=cx_[:,2:]-2*cx_[:,1:-1]+cx_[:,:-2]
    lapy[1:-1,:]=cx_[2:,:]-2*cx_[1:-1,:]+cx_[:-2,:]
    c2+=dt2*(DEFF*(lapx+lapy)/dx**2+src-k*c2)
    np.clip(c2,0,None,out=c2)
RESULTS['ss_reached_steps']=n2
R=np.hypot(X-cx,Y-cy); maxc=c2.max()
for frac in (0.5,0.1):
    mask=(c2>=frac*maxc)
    RESULTS[f'ss_radius_{int(frac*100)}pct_mm']=round(float(np.nanmax(R[mask]))*1000,2) if mask.any() else None

# ---------- C) hidrogel: obstrução de difusão (ξ vs D_gel/D_0, modelo exponencial) ----------
gel_table=[]
for xi_r in np.linspace(1,12,12):                 # ξ/r_p de 1 a 12 (r_p≈2.5nm → ξ 2.5..30nm)
    DgD0=math.exp(-1.8/xi_r)                     # forma exponencial (obstrução, qualitativa)
    gel_table.append((round(float(xi_r),1),round(DgD0,3)))
RESULTS['gel_xi_over_rp_vs_DgD0']=gel_table
RESULTS['gel_rule']=('ξ ≥ 5×r_p → D_gel/D_0 ≥ ~0.7 (liberação ok); ξ ≤ 2×r_p → <0.4 (retém a secretora — rejeitar)')

# ---------- D) self-tests ----------
tests={}
# T1 conservação sem reação
a=np.zeros((64,64)); a[32,32]=1000
dt=0.1*(L/192/4)**2/DEFF
for _ in range(300):
    lapx=np.zeros_like(a); lapy=np.zeros_like(a)
    lapx[:,1:-1]=a[:,2:]-2*a[:,1:-1]+a[:,:-2]
    lapy[1:-1,:]=a[2:,:]-2*a[1:-1,:]+a[:-2,:]
    a+=dt*DEFF*(lapx+lapy)/ (L/192/4)**2
    np.clip(a,0,None,out=a)
tests['mass_conservation_pct']=round(100*a.sum()/1000,1)
# T2 ℓ analítico vs numérico 1D
Nx=400; dx1=1e-4; kk=3e-6; dt=0.15*dx1*dx1/DEFF
c1=np.zeros(Nx); c1[0]=1.0
for _ in range(60000):
    lap=np.zeros(Nx); lap[1:-1]=c1[2:]-2*c1[1:-1]+c1[:-2]
    c1+=dt*DEFF*(lap)/dx1**2-kk*c1*dt
    c1[0]=1.0
idx=np.argmin(abs(c1-0.1*c1.max()))
tests['ell_analytic_mm']=round(2.303*ell(DEFF,kk)*1000,2)  # ponto de 10% = 2.303·ℓ (decaimento exponencial)
tests['ell_reference_note']='ℓ=√(D/k)=%.2fmm; ponto 10%% = 2.303ℓ' % (ell(DEFF,kk)*1000)
tests['ell_numeric_mm']=round(idx*dx1*1000,2)
tests['ell_err_pct']=round(abs(tests['ell_numeric_mm']-tests['ell_analytic_mm'])/tests['ell_analytic_mm']*100,1)
RESULTS['self_tests']=tests

# ---------- E) PNGs ----------
def heatmap(arr,fname,title,scale_um=False):
    a=arr/ (arr.max() or 1)
    im=Image.new('RGB',(N,N))
    px=im.load()
    for j in range(N):
        for i in range(N):
            v=a[j,i]
            px[i,j]=(int(255*min(1,v*1.2)),int(200*v),int(60*v))
    im=im.resize((768,768),Image.NEAREST)
    d=ImageDraw.Draw(im)
    d.text((10,8),title,font=F(15,True),fill='white',stroke_width=2,stroke_fill='black')
    d.text((10,748),'cístico κ×50 em círculos — campo c com consumo k=3e-6/s',font=F(12),fill='white')
    im.save(os.path.join(OUT,fname))
heatmap(c2,'ws7_steady_field.png','WS-7: campo estacionário V127ΔGPI (raio de proteção)')
# gráfico de barras ℓ (PIL)
im=Image.new('RGB',(860,420),'#0b1020'); d=ImageDraw.Draw(im)
d.text((16,12),'Raio de proteção ℓ=√(D/k) — Thiele do escudo secretor',font=F(19,True),fill='white')
ks=[1e-6,3e-6,1e-5]
for i,(D,k,el,_) in enumerate(table[0::3]):
    x0=60+i*260
    h=el/8*300
    d.rectangle([x0,380-h,x0+120,380],fill='#22c55e')
    d.text((x0,382),f'k={k:.0e}',font=F(12),fill='#8b96b3')
    d.text((x0,390-h-16),f'{el:.1f} mm',font=F(14,True),fill='white')
d.text((16,406),'D=3.9e-11 m²/s (Thorne&Nicholson: α=0.2, λ=1.8; D0=1.25e-10)',font=F(12),fill='#8b96b3')
im.save(os.path.join(OUT,'ws7_thiele_chart.png'))

json.dump(RESULTS,open(os.path.join(OUT,'ws_7_results.json'),'w'),indent=1,ensure_ascii=False)
print(json.dumps(RESULTS,indent=1,ensure_ascii=False))
print('\nSELF-TESTS:',tests,'| mass cons' ,tests['mass_conservation_pct'],'% | ℓ err',tests['ell_err_pct'],'%')
