#!/usr/bin/env python3
"""WS-8 — Inferência Bayesiana da probabilidade de sucesso do programa (quest 003).
Modelo hierárquico de analogias: cada doença-análoga contribui evidência sobre a
"conversão pré-clínica→clínica em neuroterapia" ponderada por similaridade estrutural.
Segue o workflow 8-passos da skill pymc (prior predictive → NUTS → diagnósticos → posterior).

Dados (todas as taxas são de fontes públicas citadas no artefato):
  Base-rate neurologia fase1→aprovação: 5.9% (CROMO/BIO 2011-20; n≈grande)
  Validade preditiva de organoide (PDO oncológico, proxy): ~80% acurácia
  Análogos (sucessos da CLASSE de solução, não da droga específica):
    SMA-ASO aprovado; ALS-SOD1 ASO aprovado; TTR-estabilizador aprovado;
    TTR-silenciador aprovado; PD-célula-2026 (fase1 ok, em curso); AAV-CNS (vários aprovados)
Ponderação por similaridade (script review): 4 eixos — mecanismo, vetor, doença, via.

Roda: /workspace/.venv-numpy/bin/python ws_8_bayes.py  (~2-4 min NUTS)
"""
import os, json
import numpy as np
import pymc as pm
import arviz as az

HERE=os.path.dirname(os.path.abspath(__file__))
OUT=os.path.join(HERE,'ws_8_results'); os.makedirs(OUT,exist_ok=True)
SEED=20260826

# ---------- 1) DADOS: base + análogos ----------
# similaridade estrutural ao nosso programa (0-1), justificada no MD
ANALOGS = [
    # nome, similaridade_mecanismo, similaridade_vetor, peso_classe, resultado_histórico (1=sucesso clínico)
    ("SMA-nusinersen",      0.80, 0.90, 1),   # ASO intratecal crônico — MESMA classe vetor do nosso mRNA/ASO
    ("ALS-tofersen",        0.85, 0.90, 1),   # genético-letal + biomarcador — população/endpoint iguais ao G4
    ("TTR-tafamidis",       0.75, 0.45, 1),   # estabilizador dominante — mecanismo espelhado, vetor diferente (small mol)
    ("TTR-silenciadores",   0.80, 0.70, 1),   # negação de substrato, classe ASO/RNAi
    ("PD-célula-2026",      0.60, 0.95, 1),   # célula em cérebro humano — MESMO vetor, mecanismo diferente (reposição)
    ("AAV-CNS (spa)",       0.55, 0.75, 1),   # gene terapia CNS aprovada (spinal atrophy etc.)
    ("PPS-organoid (CJD)",  0.30, 0.20, 0),   # droga anti-prion validada no MESMO modelo — mas sem sucesso clínico subsequente
    ("PRN100 (anti-PrP)",   0.65, 0.40, 0),   # anticorpo anti-PrP seguro porem sem eficácia clínica
    ("Quinacrina/dox ciclo",0.25, 0.15, 0),   #失败的 anti-prion pequenas moléculas (3 décadas)
    ("Ionis ASO príon",     0.90, 0.95, 0.5), # ION717 em clínica — sucesso parcial definido como "ainda pendente" (0.5)
]
sim=np.array([ (a[1]+a[2])/2 for a in ANALOGS ])          # similaridade média mecanismo+vetor
outcome=np.array([a[3] for a in ANALOGS], dtype=float)    # 1 sucesso / 0 falha / 0.5 pendente
w_rel=np.array([len(ANALOGS)*s/sum(sim) for s in sim])    # peso relativo

BASE_RATE=0.059   # neurologia fase1→aprovação (CROMO; BIO 2011-20 média 7.9%)
ORG_VP=0.80       # validade preditiva organoide (PDO oncológico)

# ---------- 2) MODELO ----------
with pm.Model() as model:
    # prior da taxa de sucesso da classe "neuroterapia estruturada" (base da indústria,
    # atualizada pelos análogos): Beta centrado em 5.9% com força moderada (k=20)
    alpha0=BASE_RATE*20; beta0=(1-BASE_RATE)*20
    p_class=pm.Beta("p_class", alpha=alpha0, beta=beta0)
    # similaridade modula QUANTA evidência cada análogo carrega (pesos como precisões)
    # likelihood binomial ponderada: sucesso_histórico ~ Bernoulli(p_class^(1-sim) * … )
    # forma fechada simples e honesta: odds ponderado
    # p_i = p_base^(1-sim_i) * p_analog^sim_i  (shrinkage geométrico para o análogo)
    p_analog=pm.Beta("p_analog", alpha=1+2*outcome.sum(), beta=1+2*(len(outcome)-outcome.sum()))
    # vetor de probabilidade por análogo
    p_i=pm.Deterministic("p_i", pm.math.exp((1-sim)*np.log(p_class) + sim*np.log(p_analog)))
    # observações: successo/fracasso com pesos de similaridade (exposição)
    obs=pm.Binomial("obs", n=w_rel, p=p_i, observed=outcome*w_rel)
    # gate G0 com validade preditiva do organoide
    p_true=pm.Beta("p_true", alpha=1, beta=1)
    p_obs=pm.Deterministic("p_obs", p_true*ORG_VP + (1-p_true)*(1-ORG_VP))  # acurácia 80% (Sens=Espec)
    prior_check=pm.sample_prior_predictive(200, random_seed=SEED)

# ---------- 3) FIT ----------
with model:
    idata=pm.sample(1200, tune=1200, chains=4, cores=1, random_seed=SEED, target_accept=0.9, progressbar=False)

# ---------- 4) DIAGNÓSTICOS + POSTERIOR ----------
summ=az.summary(idata, var_names=["p_class","p_analog","p_true","p_obs"], hdi_prob=0.9)
diag={
 'r_hat_max': float(az.rhat(idata, var_names=["p_class","p_analog","p_true","p_obs"]).to_array().max()),
 'ess_bulk_min': float(az.ess(idata, var_names=["p_class","p_analog","p_true","p_obs"], method="bulk").to_array().min()),
 'divergences': int(idata.sample_stats.diverging.sum()),
}
post=idata.posterior
res={
 'prior_predictive_range':{
    'p_class': [float(post.p_class.min()), float(post.p_class.max())],
 },
 'posterior':{},
 'diagnostics':diag,
 'analogos':{a[0]:{'sim':round(float(s),2),'outcome':float(o),'peso_rel':round(float(w),2)} for a,s,o,w in zip(ANALOGS,sim,outcome,w_rel)},
}
for v in ["p_class","p_analog","p_true","p_obs"]:
    x=post[v].values.flatten()
    res['posterior'][v]={
      'media':round(float(x.mean()),3),
      'sd':round(float(x.std()),3),
      'ic90':[round(float(np.percentile(x,5)),3),round(float(np.percentile(x,95)),3)],
      'ic95':[round(float(np.percentile(x,2.5)),3),round(float(np.percentile(x,97.5)),3)],
    }
json.dump(res,open(os.path.join(OUT,'ws_8_bayes.json'),'w'),indent=1,ensure_ascii=False)
print(json.dumps(res['posterior'],indent=1))
print('DIAG:',diag)
