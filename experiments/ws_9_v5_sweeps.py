#!/usr/bin/env python3
"""WS-9 v5 SWEEPS — colheita final [SIM] da Parte 1 (para execução no Colab pela autora).
Sensibilidades estruturais pendentes (guardian E-07/E-13 + controle same-mass E-12/M3):
  S1) expoente do freeS: {1, 2}   (heterodímero V127-WT como unidade inibitória?)
  S2) C50 logístico: {20, 50, 100, 200}
  S3) same-mass: MV1 semeado com a MASSA da semente MV2 (desconfunde hierarquia)
BASE: motor v4 humano (clock Groveman; VER ws_9_v4_human.json — re-executado hash-idêntico).
SAÍDA: ws_9_v5_sweeps.json (mesma disciplina: números só do run; nunca digitar).
Executar célula única no WS9_v4_HUMAN.ipynb após o baseline T1/T2 passar."""
import json, copy, time

# ── adaptar aos nomes reais das funções do motor v4 no notebook ──
# convenção assumida (conferir no notebook): run_sim(kappa, seed_mass, exponent=2, C50=50) -> dict(R_mm=...)
# e BASELINE dict com seed_mass_MV2, seed_mass_MV1, R_baseline.

def harvest(run_sim, seed_mass_MV2, seed_mass_MV1, R_baseline):
    out = {"motor": "v5 sweeps sobre v4 humano (clock Groveman 2019)",
           "baseline_R_mm": R_baseline, "wall_s": 0.0}
    t0 = time.time()
    # S1 expoente
    out["S1_exponent"] = {}
    for expo in (1, 2):
        out["S1_exponent"][str(expo)] = {
            str(k): run_sim(k, seed_mass_MV2, exponent=expo)["R_mm"] for k in (2, 4, 8)
        }
        # theta* por expoente: menor kappa cujo R < 50% baseline (interp. linear simples)
    # S2 C50
    out["S2_C50"] = {}
    for c50 in (20, 50, 100, 200):
        out["S2_C50"][str(c50)] = {
            str(k): run_sim(k, seed_mass_MV2, C50=c50)["R_mm"] for k in (2, 4)
        }
    # S3 same-mass
    r_mv1_samemass = run_sim(4, seed_mass_MV2, seed_mass_override="MV1")["R_mm"]
    out["S3_same_mass"] = {"MV1_seed_with_MV2_mass_kappa4_R_mm": r_mv1_samemass,
                           "MV2_kappa4_R_mm_reference": run_sim(4, seed_mass_MV2)["R_mm"]}
    out["wall_s"] = round(time.time() - t0, 1)
    with open("ws_9_v5_sweeps.json", "w") as f:
        json.dump(out, f, indent=1)
    print("OK → ws_9_v5_sweeps.json:", json.dumps(out, indent=1)[:400])
    return out
