#!/usr/bin/env python3
"""S3 HARVEST — colheita determinística da fase S3 (P-001).
Lê out/ws_9_v5_sweeps_S3.json (fonte única de números) e:
  1. calcula veredito pelos critérios PRÉ-REGISTRADOS (SKILL_SCOUT_S3 §4):
     C0 paridade baseline · C1 robustez (<10% desvio em TODOS os braços, R_norm)
     · C2 rompimento (algum braço ≥2× o BASE ou escape) · C3 hierarquia seed-mass
  2. anexa N-fatos (N049+) ao consistency_manifest.json — números só do JSON
  3. imprime bloco de veredito p/ canon/ledger//RECAP
Uso: python3 experiments/s3_harvest.py   (após COMPLETO no driver)"""
import json, os, sys

R = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
SRC = os.path.join(R, "out", "ws_9_v5_sweeps_S3.json")
MAN = os.path.join(R, "paper", "evidence_workspace", "consistency_manifest.json")

d = json.load(open(SRC))
arms = d["S3_rate_composition"]; hier = d["S3_hierarchy"]; base = d["baseline"]

# C0 — paridade com v4 (valores de referência do S1 arquivado: 2.83 / 144.02)
c0 = (abs(base["final_R_mm"] - 2.83) <= 0.05) and (abs(base["days_per_simunit"] - 144.02) <= 7.2)

# métricas por braço (R_norm = clock-matched)
rb = arms["BASE"]["R_norm_mm"]
devs = {n: (v["R_norm_mm"] - rb) / rb * 100.0 for n, v in arms.items() if n != "BASE"}
max_abs = max(abs(x) for x in devs.values())
extreme = max(devs, key=lambda n: abs(devs[n]))
ext_val = arms[extreme]["R_norm_mm"]
escaped = any(v["R_norm_mm"] >= 2.0 * rb for v in arms.values())
n_spread = max(arms[n]["R_norm_mm"] for n in ("N_x0.5", "N_x2")) - min(arms[n]["R_norm_mm"] for n in ("N_x0.5", "N_x2"))

# C1/C2 (mutuamente exclusivos; C1 exige <10% em TODOS; C2 dispara ao primeiro ≥2×/escape)
c1 = (max_abs < 10.0) and not escaped
c2 = escaped
c3 = bool(hier["hierarchy_preserved"])
verdict = ("C1_GAP1_FECHADO_INSENSIVEL" if c1 else
           ("C2_GAP1_MATERIAL_ESPECIE_DEPENDENTE" if c2 else
            "C2b_PARCIAL_SENSIVEL_SEM_ROMPIMENTO"))

# N-fatos (schema do manifest; evidence E032 = software/sweeps [SIM])
man = json.load(open(MAN))
def nf(fact_id, concept, value, unit, extra=None):
    e = {"fact_id": fact_id, "concept": concept, "section": "2", "value": value,
         "unit": unit, "numerator": None, "denominator": None, "sample_size": None,
         "analysis_set": "program-level", "evidence_ids": ["E032"]}
    if extra: e.update(extra)
    return e

new = [
    nf("N049", "s3_base_k2_containment_R_mm", round(rb, 3), "mm"),
    nf("N050", "s3_max_dev_pct_all_arms", round(max_abs, 2), "percent",
       {"numerator": ext_val, "denominator": rb}),
    nf("N051", "s3_extreme_arm_R_norm_mm", round(ext_val, 3), "mm"),
    nf("N052", "s3_hierarchy_MV2mass_R_mm", round(hier["R_MV2mass_mm"], 3), "mm"),
    nf("N053", "s3_hierarchy_MV1mass_R_mm", round(hier["R_MV1mass_mm"], 3), "mm"),
    nf("N054", "s3_null_arms_spread_mm", round(n_spread, 3), "mm"),
]
ids = {x["fact_id"] for x in man["numeric_facts"]}
man["numeric_facts"] += [x for x in new if x["fact_id"] not in ids]
with open(MAN, "w") as f:
    json.dump(man, f, indent=1, ensure_ascii=False); f.flush(); os.fsync(f.fileno())

print("=" * 64)
print("S3 VEREDITO — critérios pré-registrados (SKILL_SCOUT_S3 §4)")
print("=" * 64)
print(f"C0 paridade v4 .......... {'PASS' if c0 else 'FAIL'}  (base={base['final_R_mm']}/d={base['days_per_simunit']}; ref 2.83/144.02)")
print(f"BASE κ=2 R_norm ......... {rb:.3f} mm  (F-25 canon: 0,82)")
for n in sorted(devs, key=lambda k: -abs(devs[k])):
    print(f"  {n:14s} R_norm={arms[n]['R_norm_mm']:.3f}  desvio={devs[n]:+.1f}%  (tl={arms[n].get('t_lim_used','—')})")
print(f"desvio máximo ........... {max_abs:.1f}%  ({extreme})")
print(f"escape ≥2× .............. {'SIM' if escaped else 'NÃO'}")
print(f"C3 hierarquia ........... {'PRESERVADA' if c3 else 'ROMPIDA'}  (MV2 {hier['R_MV2mass_mm']:.3f} vs MV1 {hier['R_MV1mass_mm']:.3f} mm @ {hier['extreme_arm']})")
print(f"VEREDITO ................ {verdict}")
print(f"N-fatos .................. +{len(new)} (N049–N054) em consistency_manifest (total {len(man['numeric_facts'])})")
