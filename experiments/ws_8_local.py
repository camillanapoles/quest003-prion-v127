# ============================================================
# QUEST 003 — WS-8 Bayes (Colab) + WS-9 ранние simulações
# Uso: Colab novo → Runtime GPU → rodar célula única. Baixa ws8_bayes_results.json no fim.
# ============================================================
# !pip -q install "numpy<2.1" "pymc[nutpie]==6.0.1" 2>/dev/null | tail -1

import json, numpy as np, pymc as pm

SEED = 20260826
np.random.seed(SEED)

# ---------- PARTE A: WS-8 (Bayes por analogia — o pendente local) ----------
ANALOGS = [
    ("SMA-nusinersen",  0.80, 0.90, 1),
    ("ALS-tofersen",    0.85, 0.90, 1),
    ("TTR-tafamidis",   0.75, 0.45, 1),
    ("TTR-silenciadores",0.80,0.70, 1),
    ("PD-célula-2026",  0.60, 0.95, 1),
    ("AAV-CNS",         0.55, 0.75, 1),
    ("PPS-organoid",    0.30, 0.20, 0),
    ("PRN100",          0.65, 0.40, 0),
    ("Quinacrina/doxi", 0.25, 0.15, 0),
    ("ION717-pendente", 0.90, 0.95, 0.5),
]
sim = np.array([(a[1]+a[2])/2 for a in ANALOGS])
outcome = np.array([a[3] for a in ANALOGS], float)
w = np.array([10*s/sum(sim) for s in sim])
BASE = 0.059            # neurologia fase1→aprovação (CROMO/BIO)
VP = 0.80               # validade preditiva organoide (PDO ~80%)

with pm.Model() as m:
    p_class = pm.Beta("p_class", alpha=BASE*20, beta=(1-BASE)*20)
    p_analog = pm.Beta("p_analog", alpha=1+2*outcome.sum(), beta=1+2*(len(outcome)-outcome.sum()))
    p_i = pm.Deterministic("p_i", pm.math.exp((1-sim)*pm.math.log(p_class) + sim*pm.math.log(p_analog)))
    pm.Binomial("obs", n=w, p=p_i, observed=outcome*w)
    p_true = pm.Beta("p_true", alpha=1, beta=1)
    pm.Deterministic("p_obs", p_true*VP + (1-p_true)*(1-VP))
    idata = pm.sample(1200, tune=1200, chains=4, cores=2, random_seed=SEED,
                      target_accept=0.9, progressbar=False,
                      compute_convergence_checks=False)

post = idata.posterior
R = {}
for v in ["p_class", "p_analog", "p_true", "p_obs"]:
    x = post[v].values.flatten()
    R[v] = {"media":   round(float(x.mean()), 3),
            "sd":      round(float(x.std()), 3),
            "ic90":    [round(float(np.percentile(x,5)),3), round(float(np.percentile(x,95)),3)]}
pc = post["p_class"].values.flatten()
pt = post["p_true"].values.flatten()
po = post["p_obs"].values.flatten()
EV = {"P(classe>10%)":        round(float((pc>0.10).mean()),3),
      "P(classe>20%)":        round(float((pc>0.20).mean()),3),
      "P(p_true>base 5.9%)":  round(float((pt>BASE).mean()),3),
      "P(G0 passa | vp=80%)": round(float(po.mean()),3)}
print("WS-8 POSTERIOR:\n", json.dumps(R, indent=1))
print("EVENTOS:\n", json.dumps(EV, indent=1))

# ---------- salvar + download ----------
res = {"posterior": R, "eventos": EV,
       "analogos": {a[0]: {"sim": float(s), "outcome": float(o)} for a,s,o in zip(ANALOGS, sim, outcome)}}
json.dump(res, open("ws8_bayes_results.json","w"), indent=1, ensure_ascii=False)
try:
    from google.colab import files
    files.download("ws8_bayes_results.json")
except Exception:
    print("rodando fora do colab — arquivo em ./ws8_bayes_results.json")

# ============================================================
# PARTE B — WS-9 (próxima célula, depois que A rodar):
# Simulação de campo de contenção (versão numpy pura do WS-7, pronta p/ escalar):
# ============================================================
def ws9_field(N=256, L=0.05, ell_mm=3.6, theta=0.1, days=30):
    """Organoide/tecido 2D: deposito central secretor + frente priônica FKPP.
    Retorna snapshots. rodar no colab p/ N grande + 3D."""
    import math
    dx = L/N
    D = 3.86e-11
    k = D/ (ell_mm*1e-3)**2
    c = np.zeros((N,N)); u = np.zeros((N,N))
    cx = cy = L/2
    rr = (np.arange(N)*dx-cx)**2 + (np.arange(N)*dx-cy)**2
    XX,YY = np.meshgrid(np.arange(N)*dx, np.arange(N)*dx)
    dep = ((XX-cx)**2+(YY-cy)**2) < (1e-3)**2
    u[0:N//8, :] = 1.0                     # frente priônica entrando por um lado
    dt = 0.2*dx*dx/max(D, 1e-12)
    snaps = []
    steps = int(days*86400/dt)
    for i in range(min(steps, 4000)):
        lapc = np.zeros_like(c); lapu = np.zeros_like(u)
        lapc[1:-1,1:-1] = c[1:-1,2:]-2*c[1:-1,1:-1]+c[1:-1,:-2]
        lapc[1:-1,1:-1]+= c[2:,1:-1]-2*c[1:-1,1:-1]+c[:-2,1:-1]
        lapu[1:-1,1:-1] = u[1:-1,2:]-2*u[1:-1,1:-1]+u[1:-1,:-2]
        lapu[1:-1,1:-1]+= u[2:,1:-1]-2*u[1:-1,1:-1]+u[:-2,1:-1]
        src = np.where(dep, 1.0, 0.0)
        c += dt*(D*lapc/dx**2 + src*0.02 - k*c)
        # frente priônica: FKPP com inibição pelo capping local proporcional a c
        mu_eff = 0.35*(1/(1+c/theta))
        u += dt*(D*0.5*lapu/dx**2 + mu_eff*u*(1-u))
        np.clip(c,0,None,out=c); np.clip(u,0,1,out=u)
        if i % 800 == 0: snaps.append((c.copy(), u.copy()))
    return snaps, c, u
# snaps,c,u = ws9_field()   # descomentar no colab p/ rodar a simulação
