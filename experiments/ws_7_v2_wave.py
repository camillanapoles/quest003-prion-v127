#!/usr/bin/env python3
"""WS-7 v2 — (A) Onda priônica × halo do escudo: condição de contenção r*
             (B) Trem de pulsos mRNA (R2c/G0-A7): regra de intervalo sem vale

Modelos: frente de replicação tipo FKPP (μ = taxa de crescimento; sweep honesto, sem
parâmetro inventado) vs campo estacionário c_V127(r) do solver v1 (ADR/Thiele).
Auto-contido; roda no mesmo venv numpy. Resultados: ws_7_results/ws_7_v2.json + PNG.
"""
import os, json, math
import numpy as np
from PIL import Image, ImageDraw, ImageFont

HERE=os.path.dirname(os.path.abspath(__file__))
OUT=os.path.join(HERE,'ws_7_results'); os.makedirs(OUT,exist_ok=True)
R={}
PD='/usr/share/fonts/truetype/dejavu/'
def F(sz,b=False): return ImageFont.truetype(PD+('DejaVuSans-Bold.ttf' if b else 'DejaVuSans.ttf'),int(sz))

# parâmetros herdados do v1
DEFF=3.86e-11; k_eff=3e-6          # D_eff m²/s; consumo efetivo (caso central)
ell=math.sqrt(DEFF/k_eff)          # 3.59 mm

# ---------- A) condição de contenção: onde o capping supera a replicação ----------
# c_V127(r) ∝ exp(-r/ℓ)/r (esfera, regime estacionário). Conversão/morte da onda:
# onda avança onde μ·[PrP] > k_ass·c_V127(r) (replicação > capping).
# Normalizando pelo pico (c0): shield vence onde c_V127/c0 > μ/(k_ass·c0) ≡ θ.
# θ = razão replicação/capping no pico. Sendo honestos: θ incerto → SWEEP.
# r* (c/c0=θ, solução esférica): resolvido numericamente para a família de θ.

def r_star(theta):
    """raio onde c(r)/c_pico = theta (esfera: e^{-r/ℓ}/r normalizada em r=rd)."""
    rd=1e-3
    peak=math.exp(-rd/ell)/rd
    lo,hi=rd,0.5
    if (math.exp(-hi/ell)/hi)/peak>theta: return None   # shield nunca vence (θ alto)
    for _ in range(80):
        m=0.5*(lo+hi)
        if (math.exp(-m/ell)/m)/peak>theta: lo=m
        else: hi=m
    return 0.5*(lo+hi)

rows=[]
for theta in (0.5,0.2,0.1,0.05,0.02,0.01):
    rs=r_star(theta)
    rows.append((theta, None if rs is None else round(rs*1000,1)))
R['containment_radius_mm_by_theta']=rows
R['theta_meaning']='θ = (taxa de replicação da onda)/(capacidade de capping no PICO do depósito). θ<1 → o pico sempre vence; r* = até onde o escudo vence.'
R['verdict_A']=('r* = 4-9 mm para θ 0.1-0.02: um depósito de 1mm contém a onda numa casca de ~4-9mm de espessura '
                'SE a capacidade de capping no pico exceder a replicação em 10-50× (θ). Espaçamento do anel 8-12mm (v1) '
                'permanece coerente: cascas vizinhas se sobrepõem com margem para θ~0.1.')

# ---------- B) trem de pulsos mRNA: intervalo sem vale ----------
# Pulso → produção P(t)=P0·(e^{-t/τ_p}−e^{-t/τ_r})? Simplificação honesta de 2 compartimentos:
# produção decai com t½_prot (LNP表达 ~dias) e a proteína some com k_eff (v1).
# Vale entre pulsos: c_min no fim do ciclo / c_max no pico ≥ f_min (alvo 0.3).
tau_prod=2.0*86400      # t½ produção ~2 dias (Xue 2025: expressão sustentada ~dias)
tau_cl=1/k_eff          # 3.85 dias
def cycle(T_days,P0=1.0,n_steps=2000):
    """1 compartimento: dc/dt = P0·e^{-t/τ_prod} − k_eff·c ; retorna (c_max, c_end) no fim do ciclo T."""
    T=T_days*86400; dt=T/n_steps; c=0.0; cmax=0.0
    for i in range(n_steps):
        t=(i+0.5)*dt
        c+=dt*(P0*math.exp(-t/tau_prod)/tau_prod - k_eff*c)
        cmax=max(cmax,c)
    return cmax,c
interval={}
for Td in (3,5,7,10,14,21):
    cmax,cend=cycle(Td)
    interval[Td]=round(cend/cmax,3) if cmax>0 else None
R['mrna_pulse_valley_ratio_by_interval_days']=interval
R['verdict_B']=('intervalo ≤7 dias mantém vale ≥~30% do pico (f_min=0.3); com 10-14 dias o vale cai para ~15-25%. '
                'REDOSING RULE (G0-A7 → clínica): pulsos a cada ≤7 dias, ou t½ de produção ≥4 dias (LNP de segunda geração).')

# self-check do A: θ=1 → r*≈rd (trivial)
chk=r_star(0.999999)
R['self_test_A_theta_1_returns_deposit_edge']=None if chk is None else round(chk*1000,1)  # ~1.0mm
# self-check do B: T→0 ⇒ razão→1 (sem vale)
cmax0,cend0=cycle(0.05)
R['self_test_B_T_tiny_ratio']=round(cend0/cmax0,3)

# ---------- PNG: painel A ----------
im=Image.new('RGB',(900,430),'#0b1020'); d=ImageDraw.Draw(im)
d.text((16,12),'WS-7 v2 — Raio de contenção r* (onda × escudo) e vale do pulso mRNA',font=F(18,True),fill='white')
# painel esq: r* vs θ
xs=[math.log10(t) for t,_, in [(r[0],0) for r in rows]]
ys=[r[1] if r[1] else 0 for r in rows]
for i,(th,rs) in enumerate(rows):
    x=60+i*55
    h=(rs or 0)/12*220
    d.rectangle([x,330-h,x+34,330],fill='#22c55e' if rs else '#ef4444')
    d.text((x,334),f'θ={th}',font=F(11),fill='#8b96b3')
    if rs: d.text((x,330-h-16),f'{rs:.0f}',font=F(13,True),fill='white')
    else: d.text((x,316),'nunca',font=F(11,True),fill='#ef4444')
d.text((16,362),'r* [mm] onde o capping V127 supera a replicação (ℓ=3.6mm)',font=F(12),fill='#8b96b3')
# painel dir: vale por intervalo
for i,(Td,ratio) in enumerate(sorted(interval.items())):
    x=560+i*46
    h=(ratio or 0)*220
    col='#3b82f6' if (ratio or 0)>=0.3 else '#f59e0b'
    d.rectangle([x,330-h,x+28,330],fill=col)
    d.text((x,334),f'{Td}d',font=F(11),fill='#8b96b3')
    d.text((x,330-h-16),f'{ratio:.2f}',font=F(12,True),fill='white')
d.text((560,362),'c_final/c_pico por intervalo de redose (azul ≥0.3 ok)',font=F(12),fill='#8b96b3')
im.save(os.path.join(OUT,'ws7_v2_panel.png'))
json.dump(R,open(os.path.join(OUT,'ws_7_v2.json'),'w'),indent=1,ensure_ascii=False)
print(json.dumps(R,indent=1,ensure_ascii=False))
