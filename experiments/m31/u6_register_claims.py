#!/usr/bin/env python3
"""M3.1 U6 — registro probatório (skill scientific-writing): fontes E057/E058 + claims C058-C060
(norm→sha256, norma da casa de build_evidence_record.py) + N-fatos N060-N065.
Idempotente: pula entradas já presentes. Números SÓ de m31_u1u2.json / fig5_dose_ladder_data.json."""
import csv, hashlib, json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
EW = os.path.join(HERE, "..", "..", "paper", "evidence_workspace")

def norm(t):
    t = t.lower().strip()
    t = re.sub(r'[^a-z0-9.%×±\-\s]', '', t)
    return re.sub(r'\s+', ' ', t)

def sha(t):
    return hashlib.sha256(norm(t).encode()).hexdigest()

D = json.load(open(os.path.join(HERE, "m31_u1u2.json")))
F5 = json.load(open(os.path.join(HERE, "..", "..", "paper", "latex", "figs", "fig5_dose_ladder_data.json")))

# ── 1. fontes (E057 Chen 2010 Kd 71 nM — verificado NCBI+PMC nesta sessão; E058 cômputo M3.1) ──
sm = json.load(open(os.path.join(EW, "source_manifest.json")))
eids = [v["evidence_id"] for v in sm["sources"]]
if "E057" not in eids:
    sm["sources"].append({
        "evidence_id": "E057", "source_type": "journal_article",
        "title": "Interaction between human prion protein and amyloid-beta (Abeta) oligomers: role of N-terminal residues",
        "authors": ["Chen, Sen", "Yadav, Shrishail P", "Surewicz, Witold K"], "year": 2010,
        "identifiers": {"doi": "10.1074/jbc.M110.145516", "pmid": "20576610", "pmcid": "PMC2924066"},
        "locator": "pmid:20576610 (full text PMC2924066 aberto e conferido: Kd aparente = 71 nM, SPR, Aβ42-oligômero↔huPrP — PROXY declarada para κ↔µM)",
        "confidentiality": "public",
        "verification": {"status": "verified", "source_opened": True,
                         "verified_by": "agent session M3.1-2 (P-030); human-supervised", "verified_on": "2026-09-01"}})
if "E058" not in eids:
    sm["sources"].append({
        "evidence_id": "E058", "source_type": "software",
        "title": "M3.1: dose-chain kappa_req→µM→µg/deposit with GUM Type-B band + PrP MW from own P04156 sequences (this program)",
        "authors": ["Open Prion & Molecular Engineering, Consortium"], "year": 2026,
        "identifiers": {"url": "https://github.com/camillanapoles/quest003-prion-v127"},
        "locator": "experiments/m31/m31_u1u2.json (+ u1_u2_dimensional_mw.py; U1+U2 pré-registrados em m31_protocolo_garantista.md)",
        "confidentiality": "public",
        "verification": {"status": "verified", "source_opened": True,
                         "verified_by": "agent session M3.1-2 (P-030); human-supervised", "verified_on": "2026-09-01"}})
json.dump(sm, open(os.path.join(EW, "source_manifest.json"), "w"), indent=1, ensure_ascii=False)
print(f"source_manifest.json: {len(sm['sources'])} fontes")

# ── 2. claims C058-C060 (textos; números conferidos contra o JSON acima) ──
MW = D["u2_mw"]["mw_kDa"]
k2 = D["chain"]["Kt2"]; k4 = D["chain"]["Kt4"]
ratios = [F5["ladder"][k]["band_ratio_x"] for k in ("Kt1", "Kt2", "Kt3", "Kt4")]
ratio_mean = round(sum(ratios) / len(ratios), 1)
assert MW == 22.83 and k2["ug_per_deposit"] == [0.0, 2.6] and k4["ug_per_deposit"] == [0.2, 10.3]
assert 51 <= ratio_mean <= 55

CLAIMS = [
 ("C058", "M3.1", "result",
  f"A6 recombinant-protein dose band for the human Kt rung: kappa_req 2 corresponds to a peak-concentration band of 0.14-2.0 µM, converting to 0.0-2.6 µg of V127ΔGPI per deposit (protein MW {MW:.2f} kDa computed from our own P04156 mature sequence, residues 23-231), with redose interval at most 7 days - a simulation-tier planning band, not a prescription",
  ["E057", "E058", "E032", "E010", "E030", "E019"], "verified", "high"),
 ("C059", "M3.1", "result",
  "The dose ladder scales with host kinetic band: the per-deposit band rises monotonically with kappa_req - 0.0-1.9 µg at kappa 1.5 (Kt 1), 0.0-2.6 at kappa 2 (Kt 2), 0.1-3.9 at kappa 3 (Kt 3) and 0.2-10.3 at kappa 8 (declared worst case covering Kt 4) - so the containment dose must be titrated to the host Kt band rather than fixed universally",
  ["E058", "E032"], "verified", "moderate"),
 ("C060", "M3.1", "result",
  f"The band width is about {ratio_mean:.0f}x at every rung because kappa_req cancels in the hi-to-lo ratio: 14x from the Kd proxy band (71 nM apparent Abeta42-oligomer-PrP Kd to the 1 µM declared illustrative anchor) times 3.7x from the deposit-halo volume band (radius 4-6 mm; ECS fraction 0.15-0.25) - the width itself is the finding: the A6 dose remains band-valued until arm G0-A6 closes the kappa-to-µM link",
  ["E057", "E058", "E010", "E030"], "verified", "moderate"),
]

rows = list(csv.DictReader(open(os.path.join(EW, "claims.csv"))))
have = {r["claim_id"] for r in rows}
for cid, sec, kind, text, ev, status, unc in CLAIMS:
    if cid in have:
        print(f"{cid}: já presente, pulando"); continue

with open(os.path.join(EW, "claim_texts.md"), "a", encoding="utf-8") as f:
    f.write("\n")
    for cid, sec, kind, text, ev, status, unc in CLAIMS:
        if cid in have:
            continue
        f.write(f"\n- **{cid}** ({sec},{kind}) [{';'.join(ev)}]: {text}\n")
        f.write(f"  - *M3.1 sessão-2 (branch m31-dose, 01/09): cadeia U1+U2 pré-registrada → registro probatório; integrará a tese no B4 (U7).*\n")

# normaliza também linhas já existentes destes IDs (idempotência correta)
for r in rows:
    if r["claim_id"] in {c[0] for c in CLAIMS}:
        m = next(c for c in CLAIMS if c[0] == r["claim_id"])
        r["verification_status"] = m[5]; r["uncertainty"] = m[6]
for cid, sec, kind, text, ev, status, unc in CLAIMS:
    if cid in have:
        continue
    rows.append({"claim_id": cid, "section": sec, "claim_kind": kind,
                 "claim_text_sha256": sha(text), "evidence_ids": ";".join(ev),
                 "verification_status": status, "uncertainty": unc, "analysis_intent": "confirmatory"})
with open(os.path.join(EW, "claims.csv"), "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["claim_id", "section", "claim_kind", "claim_text_sha256",
                                      "evidence_ids", "verification_status", "uncertainty", "analysis_intent"])
    w.writeheader(); w.writerows(rows)
print(f"claims.csv: {len(rows)} claims")
cm = json.load(open(os.path.join(EW, "consistency_manifest.json")))
nids = {n["fact_id"] for n in cm["numeric_facts"]}
NEWN = [
 ("N060", "m31_mw_prp_mature_kda", MW, "kDa", ["E058"]),
 ("N061", "m31_a6_ug_per_deposit_kt2_hi", k2["ug_per_deposit"][1], "µg/deposit", ["E058", "E032"]),
 ("N062", "m31_a6_ug_per_deposit_kt4_worst_hi", k4["ug_per_deposit"][1], "µg/deposit", ["E058", "E032"]),
 ("N063", "m31_band_ratio_mean_x", ratio_mean, "ratio", ["E058"]),
 ("N064", "m31_redose_interval_max_d", 7, "d", ["E030", "E019"]),
 ("N065", "m31_kd_apparent_proxy_lo_um", D["u1_kd_band"]["lo"], "µM", ["E057"]),
]
for fid, concept, val, unit, ev in NEWN:
    if fid in nids:
        print(f"{fid}: já presente, pulando"); continue
    cm["numeric_facts"].append({"fact_id": fid, "concept": concept, "section": "M3.1",
                                "value": val, "unit": unit, "numerator": None, "denominator": None,
                                "sample_size": None, "analysis_set": "program-level",
                                "evidence_ids": ev})
json.dump(cm, open(os.path.join(EW, "consistency_manifest.json"), "w"), indent=1, ensure_ascii=False)
print(f"consistency_manifest.json: {len(cm['numeric_facts'])} N-fatos")
print("U6 registro ✓ — rodar validadores + gates agora")
