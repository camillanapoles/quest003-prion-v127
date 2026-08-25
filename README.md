# Quest 003 — PrP-V127 Antiprion Platform (CJD)

> **Preprint:** [`paper/preprint_v2_quest003.pdf`](paper/preprint_v2_quest003.pdf) — *PrP-V127 as a Modular Antiprion Platform: Therapeutic Vectors, Tissue-Scale Transport Design, and Regulatory Precedents for Creutzfeldt-Jakob Disease*

Open-science research program (DeepScientist quest) converting the kuru-protective PrP variant **G127V** into a deployable antiprion therapy for Creutzfeldt-Jakob disease — three vectors, quantitative transport design, pre-registered organoid gate, and a regulatory analogy map.

## What's here

| Path | Content |
|---|---|
| `paper/` | **Preprint (PDF + builder)** · audited review v1.2 (41 refs) · E200K-Brazil clinical dossier (CEP→CONEP→Anvisa) · competitive positioning whitepaper |
| `experiments/` | **G0 organoid protocol** (8 arms, pre-registered GO/NO-GO with kill-switches) · **WS-7 transport solver** (self-tested ADR; 3 design rules) · results |
| `analysis/` | Verdict audit (valid/invalid/pending taxonomy) · solution branches for every refutation (R1-R8) · probability calibration · regulatory analogy map (SMA/ALS/Parkinson/TTR precedents) |
| `literature/` | Evidence table (all claims → verified sources) · reference audits |
| `artifacts/dashboard/` | **Live knowledge graph** (data.json = single source) · graphify communities · session snapshots |

## Headline results

- **Mechanism:** anchorless (ΔGPI) PrP-V127 is a dominant-negative antiprion agent *in trans* — documented in vitro (Gatdula 2026) and in vivo via AAV (+~50 d survival; Zerbes 2026). Biallelic/editorial requirement derives from Asante 2015 (heterozygotes infectable by vCJD).
- **Design rules (transport engineering, self-tested solver):**
  1. Containment-ring node spacing **8-12 mm** (protection radius ≈4-6 mm/node);
  2. Hydrogel carrier mesh **ξ ≥ 5× protein radius** (HA 1-2% releases the secreted agent; >5% retains it);
  3. LNP-mRNA redosing **≤7 days** (trough ≥30-56% of peak).
  Containment shell 4.2-9.5 mm per deposit — and the capping/replication ratio that sets it is exactly what G0 measures.
- **Nothing unprecedented is being asked:** chronic intrathecal redosing (nusinersen), biomarker-based accelerated approval in lethal genetic neurodegeneration (tofersen/NfL), brain cell grafts (Parkinson 2026), dominant native-state stabilization (tafamidis) — the program requests their *conjunction*.
- **Realistic endpoint:** significant slowing (structured estimate 30-45%), not cure.

## The gate

**G0** (8 arms in sCJD-infected human cerebral organoids; platform validated by Groveman 2019/2021, Williams 2023 — V127 in any form has never been tested in organoids) decides which vector scales: secretory graft vs recombinant protein vs LNP-mRNA, with pentosan polysulfate as the published benchmark.

## Provenance

Every session is committed (34+ commits); every external document was reference-audited before adoption (one collaborator document passed 6/6 checks; earlier ones did not — documented in `literature/refs_audit.md`). Retracted evidence is banned by rule.

---
*Open-source research produced with the DeepScientist agentic workflow (MODO DIRETO) · 2026-08.*
