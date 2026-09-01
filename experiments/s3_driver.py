#!/usr/bin/env python3
"""S3 DRIVER — orquestrador resiliente da fase S3 (P-001) com checkpoint por unidade.
O MOTOR (simulate) é importado INTACTO de ws_9_v5_sweeps_gha.py (contrato: motor v4 exato).
Cada unidade (baseline/braço/hierarquia) é checkpointada em out/s3_partial.json — se o
processo morrer (Android phantom-killer), o relaunch retoma do último checkpoint.
Saída final: mesmo schema do S1/S2 (+ seções S3_rate_composition/S3_hierarchy).
Uso: python3 s3_driver.py   (roda até completar; idempotente)"""
import json, math, os, sys, time

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))
from ws_9_v5_sweeps_gha import simulate, ANCH, SEED_MV2, SEED_MV1

CKPT = 'out/s3_partial.json'
FINAL = 'out/ws_9_v5_sweeps_S3.json'
t_double_h = (ANCH['final_dpi']-ANCH['first_denovo_dpi'])/math.log2(ANCH['titer_MV2']/100.0)

KT0,KR0,KC0=(10.0,5.0),(50.0,10.0),(10.0,50.0)
def sc(v,f): return (v[0]*f,v[1]*f)
ARMS={'BASE':(KT0,KR0,KC0),
      'N_x0.5':(sc(KT0,.5),sc(KR0,.5),sc(KC0,.5)),
      'N_x2':(sc(KT0,2),sc(KR0,2),sc(KC0,2)),
      'C_Kt_x0.5':(sc(KT0,.5),KR0,KC0),'C_Kt_x2':(sc(KT0,2),KR0,KC0),
      'C_Kr_x0.5':(KT0,sc(KR0,.5),KC0),'C_Kr_x2':(KT0,sc(KR0,2),KC0),
      'C_Kc_x0.5':(KT0,KR0,sc(KC0,.5)),'C_Kc_x2':(KT0,KR0,sc(KC0,2)),
      'J_KtKr_x2':(sc(KT0,2),sc(KR0,2),KC0),
      'J_KtKr_x0.5':(sc(KT0,.5),sc(KR0,.5),KC0)}

def load():
    os.makedirs(os.path.dirname(CKPT),exist_ok=True)
    return json.load(open(CKPT)) if os.path.exists(CKPT) else {}
def save(st):
    with open(CKPT,'w') as f:
        json.dump(st,f,indent=1); f.flush(); os.fsync(f.fileno())

st=load(); t00=time.time()
def run_arm(name,kt,kr,kc,tl,seed,tag):
    r=simulate(kcap=2.0,seed_mass=seed,Kt=kt,Kr=kr,Kc=kc,t_lim=tl,tag=tag,progress=False)
    return r

# 1) baseline de paridade (kcap=0, seed MV2) — C0
if 'baseline' not in st:
    r=simulate(kcap=0.0,seed_mass=SEED_MV2,tag='BASE',progress=False)
    T1=r['totalf']>r['total0']*1.5
    assert T1,'C0 FALHOU: baseline nao replica (T1)'
    dpu=t_double_h/r['t_double_sim']
    st['baseline']={'final_R_mm':round(r['final_R_mm'],3),'days_per_simunit':round(dpu,2),
                    'T1_pass':T1,'t_double_sim':r['t_double_sim']}
    save(st); print('Ckpt: baseline', st['baseline'], flush=True)

# 2) passada 1 (t_lim=5) — todos os braços em κ=2
for name in ARMS:
    if name not in st.get('p1',{}):
        kt,kr,kc=ARMS[name]
        r=run_arm(name,kt,kr,kc,5.0,SEED_MV2,name.replace('.','_'))
        st.setdefault('p1',{})[name]={'R_sim5_mm':round(r['final_R_mm'],3),
                                      't_double_sim':r['t_double_sim'],'wall_s':r['wall_s']}
        save(st); print('Ckpt: p1',name,st['p1'][name], flush=True)

b=st['p1']['BASE']['t_double_sim']
# 3) passada 2 (clock-matched: mesmo nº de duplicações do BASE)
for name in ARMS:
    if name=='BASE': continue
    if name not in st.get('p2',{}):
        t2=st['p1'][name]['t_double_sim']
        tl=5.0 if (not t2) else min(10.0,max(2.5,5.0*b/t2))
        kt,kr,kc=ARMS[name]
        r=run_arm(name,kt,kr,kc,tl,SEED_MV2,name.replace('.','_')+'_m')
        st.setdefault('p2',{})[name]={'R_norm_mm':round(r['final_R_mm'],3),'t_lim_used':round(tl,3)}
        save(st); print('Ckpt: p2',name,st['p2'][name], flush=True)

# 4) H — hierarquia seed-mass no braço extremo (C3)
if 'hierarchy' not in st:
    rbc=st['p1']['BASE']['R_sim5_mm']
    ext=max(st['p2'],key=lambda n: abs(st['p2'][n]['R_norm_mm']-rbc))
    t2=st['p1'][ext]['t_double_sim']
    tl=5.0 if (not t2) else min(10.0,max(2.5,5.0*b/t2))
    kt,kr,kc=ARMS[ext]
    rH2=run_arm(ext,kt,kr,kc,tl,SEED_MV2,'H_MV2')
    rH1=run_arm(ext,kt,kr,kc,tl,SEED_MV1,'H_MV1')
    st['hierarchy']={'extreme_arm':ext,'t_lim_used':round(tl,3),
                     'R_MV2mass_mm':round(rH2['final_R_mm'],3),
                     'R_MV1mass_mm':round(rH1['final_R_mm'],3),
                     'hierarchy_preserved':bool(rH2['final_R_mm']>rH1['final_R_mm'])}
    save(st); print('Ckpt: hierarchy', st['hierarchy'], flush=True)

# 5) finalização — schema S1/S2
res={'motor':'v5 sweeps sobre v4 humano (C0 exato + fs_exp param) — S3 via s3_driver (checkpoint)',
     'phase':'S3','wall_total_s':round(time.time()-t00,1),'anchors':ANCH,
     'baseline':st['baseline'],
     'S3_rate_composition':{n:{**st['p1'][n],
                               ('R_norm_mm' if n=='BASE' else 'R_norm_mm'):
                               (st['p1'][n]['R_sim5_mm'] if n=='BASE' else st['p2'][n]['R_norm_mm']),
                               't_lim_used':(5.0 if n=='BASE' else st['p2'][n]['t_lim_used'])}
                            for n in ARMS},
     'S3_hierarchy':st['hierarchy']}
json.dump(res,open(FINAL,'w'),indent=1)
print('COMPLETO →',FINAL, flush=True)
