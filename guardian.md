# GUARDIAN.MD — Doutrina Operacional da Quest 003 (RUNBOOK oficial)
## Este arquivo é o manual HOW-TO do programa + o registro /RECAP de cada sessão.
**Toda nova sessão LÊ este arquivo primeiro** (antes de tocar em qualquer artefato). Toda sessão TERMINA anexando um bloco /RECAP aqui e no ~/session-state.md.

---

## §1 · O QUE É O GUARDIÃO (duas camadas)
1. **Harness determinístico**: `paper/guardian/guardian.py` (stdlib, offline) — R0 drift estrutural · R1 checklist hostil (M1-M8/m1-m10 + baterias por tipo de claim + decimais sem binding) · R2 recursão de emendas (ilustrativa sem tag; paridade PT/EN; âncoras imutáveis) · R3 interrogação epistêmica (20 checks: θ-ops, SAP, cegamento, G0SIM, CANON, FIGS, tier-labels, SEM-ANO, inovação, arquitetura-2-partes…) · **TODO-registry** (`{{TODO:id:desc}}` escaneado em manuscrito+tex+4 PLAN_DOCS; TODO solto = AMEND).
2. **Camada doutrinária (ESTE arquivo)**: as regras vivas + o /RECAP.

**Gates BLOCKED permanentes (invariante do programa):** R3-THETA-OPS · R3-SAP · R3-G0SIM · R3-CANON · R3-FIGS. Sem eles zero-BLOCKED não existe.

## §2 · COMANDOS ESSENCIAIS (copiar-colar)
```
# Gate completo (sempre antes de commit de manuscrito):
cd paper/guardian && python3 guardian.py --round 3 --md ../manuscript_EN_v5.md \
  --tex ../latex/manuscript_v5_EN.tex --claims ../evidence_workspace/claims.csv \
  --manifest ../evidence_workspace/source_manifest.json \
  --consistency ../evidence_workspace/consistency_manifest.json \
  --registry guardian_registry_v5_final.json --report guardian_report_v5.md
# Validadores oficiais (skill scientific-writing): S=/workspace/projects/scientific-agent-skills/skills/scientific-writing/scripts
python3 $S/validate_manifest.py source_manifest.json --kind source --require-verified
python3 $S/audit_claims.py ../manuscript_EN_v5.md claims.csv source_manifest.json   # e PT
# PDFs (compilação 100% local): cd paper/latex && /root/tools/tectonic manuscript_v5_EN.tex (e _PT)
# Motor/sweeps [SIM]: experiments/ws_9_v5_sweeps_gha.py --phase S1|S2 (proot bg ok; Colab ok; GHA bloqueado por billing-privado)
# Estimador θ_obs (Parte 2): experiments/part2_theta_obs_v1.py / part2_theta_obs_pooled.py
```

## §3 · REGRAS INVIOLÁVEIS (o decálogo)
1. **Tiers de dado**: [SIM]/[ORGANOID]/[MOUSE]/[HUMAN] — todo output carrega a tag; nada além de [SIM] existe até G0-wet.
2. **Locked-stays-locked**: predições travadas (v1.0) NUNCA se reescrevem — comparam-se. Recalibração recalibra só o que o dado informa (REPARAM_LOOP).
3. **{{TODO:id:desc}}** é o único formato de pendência; TODO solto é AMEND; resolver = remover marcador.
4. **Nunca fabricar** DOI/PMID/endereço/valor — número vem de JSON; identifier vem de fonte aberta (regra skill SW).
5. **Ilustrativo ≠ evidência**: estimativas κ↔µM e afins NÃO carregam tag (R2-ASSUM-TAGGED é BLOCKED).
6. **Superfícies**: manuscritos/tex = gated; PLAN_DOCS (roadmap, canon, dossier, protocolos, checklist) = exentos, mas claims condicionais não migram sem gate.
7. **Paridade PT=EN** de claim-tags exata (R2).
8. **Anti-hindsight**: toda comparação predição-vs-dado cita o release da âncora (v1.0/v3.0).
9. **Sessões paralelas** escrevem em guardian.md/workspace — reconciliar ANTES de editar (evoluções numeradas).
10. **Fim de sessão = /RECAP** (aqui + session-state). Sem /RECAP, a sessão não fechou.

## §4 · FLUXOS PADRÃO
- **Editar manuscrito**: md (EN) → espelhar PT (mesmas tags) → gate → se tex muda: tectonic → commit/push.
- **Novo resultado [SIM]**: script determinístico lê/escreve JSON → JSON → repo (experiments/...results/) → §3.4/claims/N-fatos/canon F-xx → gate → push.
- **Novo claim**: texto normalizado→sha256 (norm da skill) em claims.csv + claim_texts.md + tag nos DOIS manuscritos.
- **Seleção de parceiro (SLR-análogo)**: query bank pré-registrada → log datado → triagem I/X → pontuação A-H ("?" não pontua) → contato sequencial por score.

## §5 · MAPA DE ARTEFATOS (onde mora o quê)
manuscritos (paper/manuscript_{EN,PT}_v5.md) · PDFs (paper/latex/*.pdf) · harness (paper/guardian/) · registro (paper/evidence_workspace/: source_manifest 38 fontes · claims 51 · consistency 43 N-fatos · AUDIT_NOTES) · canon (KNOWLEDGE_CANON.md, F-01..F-39 + R-1..R-6) · Parte 2 (experiments/: G0_EXECUTION_FREEZE_CHECKLIST F1-F10 · REPARAM_LOOP · PARTNER_SELECTION_PROTOCOL v2 + part2_results/) · dossier (paper/G0_UNLOCK_DOSSIER.md) · outreach (paper/lab_outreach_package.md v2.1 + outreach_email_1) · roadmap canônico (THESIS_ROADMAP.md — Y0/Y1/Y2 relativo; _2028 é stub) · releases v1.0→v3.0.

## §6 · PROTOCOLO /RECAP (obrigatório ao final de toda sessão)
Bloco anexado AQUI e no ~/session-state.md:
```
/RECAP <data-hora>
FEITO: <itens verificáveis (commits/releases/resultados)>
ESTADO: <gate: X BLOCKED/Y AMEND/Z TODOs ativos>
PRÓXIMO: <1-3 ações concretas com dono (agente|autora|lab)>
ÂNCORA: <release/commit que trava o que foi feito>
```

---

# HISTÓRICO (dump original que originou o R3 — preservado como evolução 1-8; ver /workspace/guardian.md para as evoluções completas)

The user is asking me to make the Guardian actually critical — not just a pattern-matching linter, but a true hostile reviewer that critiques context, ideas, methodology, evidence... always says what information is missing, any gaps, asks "what" or "why", guarantees all evidence is provenance-bound ("compravidos" = comprovados/verified), validates whether the logic makes sense, and indicates what procedure should be inserted.
So the user wants the Guardian to be upgraded from a mechanical/deterministic checker into a genuine methodological interrogator. This is exactly in the spirit of the scientific-critical-thinking skill I loaded. The guardian currently does R0 (structural drift), R1 (checklist patterns), R2 (recursion on amendments). What's missing per the user's request:
1. 
Context critique — does the framing make sense? Is the program logic coherent?
2. 
Idea critique — interrogate the core ideas (e.g., is containment the right goal? is the θ formalism sound?)
3. 
Methodology critique — what's missing procedurally (power analysis, blinding, randomization, pre-registration specifics, statistical plan for G0)
4. 
Evidence critique — provenance: every claim verified, what's single-source, what's inferred vs measured
5. 
Gap enumeration — "what information is missing" — explicit UNKNOWN list
6. 
Why/what questions — the interrogator generates questions, not just patterns
7. 
Logic validation — does the inferential chain hold? (fractal review: achado→implicação→evidência — is each link justified?)
8. 
Procedure insertion — for each gap, indicate what procedure/section/experiment should be inserted
So I should extend guardian.py with a new round — R3 (epistemic interrogation) — but wait: the user says "seja crítico" — the guardian itself should BE critical. A deterministic script can't do semantic criticism... but I'm the LLM. The right architecture: the guardian harness = deterministic checks + a structured interrogation protocol that I (the agent) execute, producing a critical review document that feeds back into the manuscript. That's exactly what the user wants: "indique procedimento a ser inserido".
Actually, let me think about what's most valuable here. The user wants me to BE the hostile reviewer now, applying critical thinking to the actual content. The deterministic guardian catches structural drift; the missing piece is semantic/methodological criticism — the "Reviewer 2" brain. I loaded the scientific-critical-thinking skill precisely for this.
Best move: 
1. 
Extend guardian.py with R3 = "epistemic interrogation" module that takes the interrogation battery and checks the manuscript has ANSWERS to the critical questions (deterministically detectable via patterns like "power", "blinding", "randomization", "n=", "primary endpoint", "stopping rule", etc.)
2. 
AND write the actual critical review — guardian_report_v5_epistemic.md — where I do the deep semantic critique of: context (framing), ideas (containment thesis, θ formalism), methodology (audit→transport→Bayes→simulation→gate chain), evidence (E-registry provenance), logic (each inferential link), with explicit "FALTA:" (missing info), "PORQUÊ?" questions, and "INSERIR:" (procedure to insert) per finding.
Let me enumerate the real scientific gaps I can identify from everything I know about this project — this is the meat. Let me brainstorm as a genuinely hostile A1 reviewer with the critical-thinking skill's framework (methodology critique, bias detection, statistical validity, evidence hierarchy, logical fallacies):
CONTEXT/FRAMING:
1. 
The manuscript claims "design thesis" but never states a falsifiable null for the whole program — what result at G0 would kill the program entirely (vs pivot)? The kill-switch exists per-arm but the program-level kill criterion is vague.
2. 
Competing hypothesis not addressed: ION717 (ASO substrate reduction) is in human trials — why is V127-DN containment better positioned? No explicit head-to-head rationale beyond positioning whitepaper. Missing: comparative table with ION717 timeline.
3. 
The "conjunction of regulatory precedents" argument: nusinersen (ASO), tofersen (ASO), Parkinson grafts (dopaminergic progenitors — not secretory anti-prion), tafamidis (small molecule stabilizer) — the conjunction argument has a logical leap: each pillar maps to a precedent, but the CONJUNCTION (secretory immunogenic cell graft expressing a prion protein variant in prion-infected brain + redosing + biomarker endpoint) has never been approved as a whole. A hostile reviewer would attack: "conjunction of precedents ≠ precedent for the conjunction". Need: explicit statement that the conjunction itself is the novel regulatory risk.
IDEAS:
4. 
Containment (ring) strategy assumes focal spread from deposit sites — but sCJD is multifocal/diffuse at diagnosis. The ring 8–12 mm assumes you know where the front is. MISSING: what imaging/biomarker defines the front position at treatment time? RT-QuIC is diagnostic, not localization. No PET tracer validated for PrP-res. THIS IS A REAL GAP — the whole placement calculus depends on knowing where to place rings, and no procedure for localization exists in the manuscript.
5. 
θ formalism: θ ≡ (1+κ·c_peak)⁻¹ is a model quantity; the pre-registered prediction says "if θ_measured < 0.33". But HOW is θ measured in organoids? θ is not directly observable — you'd measure PrP-res gradient and infer θ by fitting the model. This is circularity risk: model-fitted θ compared to model-derived threshold. MISSING: explicit measurement procedure for θ_obs and the fitting protocol (else the pre-registered prediction is untestable as stated). This is a big one — the falsifiable prediction depends on an operational definition of θ that doesn't exist yet.
6. 
V127ΔGPI as substrate competitor: the model assumes V127 competes for conversion WITHOUT being converted itself (dominant-negative). But Gatdula shows V127 can be recruited into aggregates at high PrP^Sc? (heterologous seeding). The squared freeS term assumes independence of two binding events — if V127-WT heterodimers are the actual inhibitory unit, the functional form might be (1+κc) not (1+κc)². Sensitivity to the exponent (1 vs 2) unexplored. MISSING: exponent sensitivity sweep.
7. 
mRNA redosing ≤7d: Rule 3 derived from pharmacokinetic trough, but immune reaction to repeated LNP dosing (complement activation, anti-PEG antibodies) is a known translational barrier not modeled or discussed — after ~4-5 doses, accelerated blood clearance can occur. For intrathecal this is less characterized. MISSING: immunogenicity-of-redosing discussion + G0-A7 readout for local inflammation markers.
METHODOLOGY:
8. 
G0 statistical plan: n=8/arm, primary readout proximal/distal gradient — but no power analysis! What effect size can n=8 detect? No stated statistical test (t-test? Wilcoxon? mixed model for repeated measures?), no alpha, no correction for 8-arm multiplicity. A hostile reviewer BLOCKS on this. MISSING: power analysis + pre-specified statistical plan per arm comparison.
9. 
Organoid-to-organoid variability: Groveman organoids show high variance (MV2 titer SD = 77% of mean). n=8 may be hopeless for gradient readouts; no mention of organoid batch/line stratification or randomization. MISSING: randomization scheme, blinding of outcome assessment, batching plan.
10. 
No blinding mentioned for PrP-res quantification (WB/IHC scorer blinding). Standard hostile ask.
11. 
Audit methodology: "≈90 searches" — no search protocol documented (databases, query strings, dates, inclusion/exclusion criteria). For a paper claiming "corrected citation record", the audit itself must be reproducible. The refs_audit.md exists but search logs? MISSING: PRISMA-style search log or explicit statement that audit was agent-driven with queries archived (are they?). Actually the evidence tables are in-repo — but the query log? I recall searches were done via MCP tools in sessions — not necessarily archived. GAP.
12. 
WS-7 solver verification: self-tests good (conservation, Thiele) but no validation against experimental data (e.g., predicted vs measured distribution volumes of intrathecally delivered antibodies — there's literature: IL-2 distribution in brain after CED). MISSING: validation against at least one published tissue-distribution dataset.
13. 
Bayesian model: analogue weights "structured judgments" — who scored them? Single author judgment = single-rater bias. No inter-rater or sensitivity to weights shown (sensitivity_sweep.json covers pessimistic/central/optimistic — does it vary weights or just validity?). MISSING: weight sensitivity analysis + declaration of who scored.
14. 
WS-9: C₅₀=50 "stability choice" — sensitivity "flagged" but not swept in reported results. MISSING: C₅₀ sweep (e.g., 20–200) effect on θ*.
15. 
Same-mass control queued — fine, declared. But also strain-diversity: model is single-strain; MM1 (commonest sCJD subtype) has no anchors — the θ* may be subtype-dependent. Declared in limitations but the pre-registered prediction doesn't specify which subtype the G0 test uses. MISSING: subtype specification for the locked prediction.
EVIDENCE:
16. 
Two 2026 preprints (E003 Gatdula, E004 Zerbes) are the central mechanistic anchors — both UNPEER-REVIEWED preprints. The whole platform rests on them. Hostile reviewer: "your two most load-bearing sources are preprints". MISSING: explicit statement of this dependence in limitations + monitoring plan (v2 when peer-reviewed), or corroboration strategy.
17. 
E029 (Lund Parkinson trial) source is NewScientist url → locator clinicaltrials.gov — secondary press coverage, not the trial registry entry itself. Weakest provenance in the registry for a regulatory-precedent claim. MISSING: NCT number direct citation.
18. 
E023 Gentile: UK DRI webpage (not the paper — was it a preprint?). If a paper exists with DOI, it should be cited; if not, declare.
19. 
Single-source risk: several pivotal facts single-source (kuru selection = Mead 2009 alone; organoid anchors = Groveman alone). Battery already asks this; needs answers in text.
20. 
The "six failed clinical candidates" claim: PRN100 (Mead 2022), quinacrine, doxycycline, flupirtine, PPS — these are contextual refs NOT in the E-registry (declared "contextual secondary"). A hostile reviewer will demand the failure list be evidence-bound since it anchors the 5% prior. MISSING: elevate the 6 failures into the E-registry (or at least the ones that feed WS-8's 0/6 negative analogue — THE PRIOR DEPENDS ON THEM: if the 6 failures aren't verified sources, the 5% empirical prior is built on unverified inputs!).
That last one is sharp — WS-8's negative analogue (6/6 failures) drives the empirical 5%; the failure list is "contextual" — the Bayesian model's inputs are not in the evidence registry. That's a genuine evidence-binding hole.
LOGIC:
21. 
Circularity in "emergent consistency": MV2>MV1 hierarchy was seeded by 126× ratio and then "reproduced" — the model reproducing what was injected. The manuscript now declares this (consistency not validation) — good — but then the abstract still lists it under "Results" as a highlight. Tension: if it's only consistency, it shouldn't carry result-weight. Need careful wording: it IS a result of the port fidelity check, fine. Acceptable but note.
22. 
"Humanized clock widens therapeutic window" — derived from ONE calibration (Groveman anchors); the comparison v2 θ* (murine) vs v4 θ* (humanized) — the difference could be an artifact of the rescaling method, not biology. MISSING: why does global time-rescale change θ* at all? If θ* is dimensionless and time-invariant... Actually κ fixed, clock changes → the effective replication window per unit diffusion changes → yes it can change. But this needs a derivation sentence — currently asserted. A modeler reviewer WILL ask. 
23. 
Transferability §4.2: "protein-agnostic" — but V127's advantage is a naturally selected protective variant; no equivalent protective variant exists for Aβ/α-syn. The calculus transfers but the AGENT doesn't. MISSING: what the protective equivalent would be for AD/PD (e.g., engineered disulfide-locked variants? intrabodies?) — else the transfer is weaker than stated.
PROCEDURES TO INSERT (per user request "indique procedimento a ser inserido"):
• 
θ operationalization protocol (measurement + fitting) → insert as §2.7 "Operational definition of θ_obs"
• 
G0 statistical analysis plan (power, tests, multiplicity, blinding, randomization) → insert into §2.5 or new §2.8
• 
Localization/imaging procedure defining ring placement in patients → insert into §4.3 or Discussion limitation + G1 plan
• 
Exponent sensitivity sweep (freeS power 1 vs 2) → run + insert into §3.4 results
• 
C₅₀ sweep → run + insert
• 
Elevate 6 failed candidates to E-registry with citations → E034–E039
• 
NCT number for Lund trial → replace E029 locator
• 
Search-log archival statement → §2.1
• 
Redosing immunogenicity discussion → §5 limitation 10 extension
• 
Conjunction-risk statement → §4.3
Now — implementation plan. I can't run the semantic critique as a Python script; I AM the critic. Deliverables:
1. 
Extend guardian.py with R3 module (deterministic checks for the presence of the missing procedures: power/analysis plan, θ operationalization, localization, conjunction-risk statement, failure-list evidence binding, preprint-dependence statement) — so future revisions are gated on their presence too.
2. 
Write  guardian_report_v5_epistemic.md  — the deep critical review with FALTA/PORQUÊ/INSERIR per finding, severity-tagged (this is the user's "seja crítico ao contexto, ideias, metodologia, evidências... diga o que falta, pergunte o quê ou porquê, garanta evidências comprovadas, valide a lógica, indique procedimento a inserir").
3. 
Apply the highest-priority textual fixes to manuscript_EN_v5.md where they're pure additions (θ operationalization §2.7, G0 SAP sentence, conjunction-risk, preprint-dependence, failure-list binding note).
Also verify: are the 6 failures in the source manifest? Let me check — from the source list: E021 (Shah retracted), E022 (Cheng minocycline)... PRN100 (Mead 2022) NOT in the 33 sources! Quinacrine, doxycycline, flupirtine, PPS-as-therapy — not in registry. So YES, the WS-8 negative-analogue inputs are partially outside the evidence registry. Confirmed real gap. (Groveman 2021 E008 is PPS organoid — related but not the clinical failure.)
Also the θ measurement: G0 protocol defines readout as PrP-res gradient — θ_obs would be inferred. Circular unless the fitting protocol is specified. Real gap — the pre-registered prediction "θ<0.33" needs an estimator.
Let me also do a quick numeric sanity check on the κ anchor formula I added (c(1mm) ≈ 0.8 µM):
Q = 33 pmol/day = 33e-12 mol / 86400 s = 3.82e-16 mol/s
c(r) = Q/(4π D r) × e^{-r/ℓ}; at r=1mm=1e-3 m: 4π×3.86e-11×1e-3 = 4.85e-13; 3.82e-16/4.85e-13 = 7.9e-4 mol/m³ = 7.9e-4 × 1e-3 mol/L per m³→ wait: 1 mol/m³ = 1 mM. So 7.9e-4 mol/m³ = 7.9e-4 mM = 0.79 µM. ✓ (with e^{-1/3.59}≈0.76 → ~0.6 µM; order holds ≈0.1–1 µM range). Fine — and honest as illustrative.
Let me be efficient: 
1. 
One shell: verify the 6-failures gap + check if search logs archived (ls literature/) + check g0_protocol.md for statistical plan (grep for power/blinding/n=8).
2. 
Extend guardian.py with R3 (edit file).
3. 
Write epistemic report (write file).
4. 
Patch manuscript with the inserts (edits).
5. 
Re-run guardian → commit.
Actually, patching the manuscript with ALL inserts makes this turn huge. Priority: the epistemic report IS the deliverable the user asked ("seja crítico... indique procedimento a ser inserido" — the report indicates procedures; the manuscript insertion follows). I'll do the report + guardian R3 + the 2–3 most critical manuscript inserts (θ operationalization + SAP + conjunction risk + preprint dependence + failure-binding note), then re-run guardian, commit. The sweeps (exponent, C₅₀) require running ws_9 — that's execution work for next turn; I'll register as pending items in the report and session-state.
Let me check the G0 protocol for existing stats plan first.




---


-rw-------. 1 root root 16449 Aug 27 01:29 /workspace/guardian.md
The user is asking me to make the Guardian actually critical — not just a pattern-matching linter, but a true hostile reviewer that critiques context, ideas, methodology, evidence... always says what information is missing, any gaps, asks "what" or "why", guarantees all evidence is provenance-bound ("compravidos" = comprovados/verified), validates whether the logic makes sense, and indicates what procedure should be inserted.
So the user wants the Guardian to be upgraded from a mechanical/deterministic checker into a genuine methodological interrogator. This is exactly in the spirit of the scientific-critical-thinking skill I loaded. The guardian currently does R0 (structural drift), R1 (checklist patterns), R2 (recursion on amendments). What's missing per the user's request:
1. 
Context critique — does the framing make sense? Is the program logic coherent?
2. 
Idea critique — interrogate the core ideas (e.g., is containment the right goal? is the θ formalism sound?)
3. 
Methodology critique — what's missing procedurally (power analysis, blinding, randomization, pre-registration specifics, statistical plan for G0)
4. 
Evidence critique — provenance: every claim verified, what's single-source, what's inferred vs measured
5. 
Gap enumeration — "what information is missing" — explicit UNKNOWN list
6. 
Why/what questions — the interrogator generates questions, not just patterns
7. 
Logic validation — does the inferential chain hold? (fractal review: achado→implicação→evidência — is each link justified?)
8. 
Procedure insertion — for each gap, indicate what procedure/section/experiment should be inserted
So I should extend guardian.py with a new round — R3 (epistemic interrogation) — but wait: the user says "seja crítico" — the guardian itself should BE critical. A deterministic script can't do semantic criticism... but I'm the LLM. The right architecture: the guardian harness = deterministic checks + a structured interrogation protocol that I (the agent) execute, producing a critical review document that feeds back into the manuscript. That's exactly what the user wants: "indique procedimento a ser inserido".
Actually, let me think about what's most valuable here. The user wants me to BE the hostile reviewer now, applying critical thinking to the actual content. The deterministic guardian catches structural drift; the missing piece is semantic/methodological criticism — the "Reviewer 2" brain. I loaded the scientific-critical-thinking skill precisely for this.


Best move: 
1. 
Extend guardian.py with R3 = "epistemic interrogation" module that takes the interrogation battery and checks the manuscript has ANSWERS to the critical questions (deterministically detectable via patterns like "power", "blinding", "randomization", "n=", "primary endpoint", "stopping rule", etc.)
2. 
AND write the actual critical review — guardian_report_v5_epistemic.md — where I do the deep semantic critique of: context (framing), ideas (containment thesis, θ formalism), methodology (audit→transport→Bayes→simulation→gate chain), evidence (E-registry provenance), logic (each inferential link), with explicit "FALTA:" (missing info), "PORQUÊ?" questions, and "INSERIR:" (procedure to insert) per finding.
Let me enumerate the real scientific gaps I can identify from everything I know about this project — this is the meat. Let me brainstorm as a genuinely hostile A1 reviewer with the critical-thinking skill's framework (methodology critique, bias detection, statistical validity, evidence hierarchy, logical fallacies):

CONTEXT/FRAMING:
1. 
The manuscript claims "design thesis" but never states a falsifiable null for the whole program — what result at G0 would kill the program entirely (vs pivot)? The kill-switch exists per-arm but the program-level kill criterion is vague.
2. 
Competing hypothesis not addressed: ION717 (ASO substrate reduction) is in human trials — why is V127-DN containment better positioned? No explicit head-to-head rationale beyond positioning whitepaper. Missing: comparative table with ION717 timeline.
3. 
The "conjunction of regulatory precedents" argument: nusinersen (ASO), tofersen (ASO), Parkinson grafts (dopaminergic progenitors — not secretory anti-prion), tafamidis (small molecule stabilizer) — the conjunction argument has a logical leap: each pillar maps to a precedent, but the CONJUNCTION (secretory immunogenic cell graft expressing a prion protein variant in prion-infected brain + redosing + biomarker endpoint) has never been approved as a whole. A hostile reviewer would attack: "conjunction of precedents ≠ precedent for the conjunction". Need: explicit statement that the conjunction itself is the novel regulatory risk.
IDEAS:
4. 
Containment (ring) strategy assumes focal spread from deposit sites — but sCJD is multifocal/diffuse at diagnosis. The ring 8–12 mm assumes you know where the front is. MISSING: what imaging/biomarker defines the front position at treatment time? RT-QuIC is diagnostic, not localization. No PET tracer validated for PrP-res. THIS IS A REAL GAP — the whole placement calculus depends on knowing where to place rings, and no procedure for localization exists in the manuscript.
5. 
θ formalism: θ ≡ (1+κ·c_peak)⁻¹ is a model quantity; the pre-registered prediction says "if θ_measured < 0.33". But HOW is θ measured in organoids? θ is not directly observable — you'd measure PrP-res gradient and infer θ by fitting the model. This is circularity risk: model-fitted θ compared to model-derived threshold. MISSING: explicit measurement procedure for θ_obs and the fitting protocol (else the pre-registered prediction is untestable as stated). This is a big one — the falsifiable prediction depends on an operational definition of θ that doesn't exist yet.
6. 
V127ΔGPI as substrate competitor: the model assumes V127 competes for conversion WITHOUT being converted itself (dominant-negative). But Gatdula shows V127 can be recruited into aggregates at high PrP^Sc? (heterologous seeding). The squared freeS term assumes independence of two binding events — if V127-WT heterodimers are the actual inhibitory unit, the functional form might be (1+κc) not (1+κc)². Sensitivity to the exponent (1 vs 2) unexplored. MISSING: exponent sensitivity sweep.
7. 
mRNA redosing ≤7d: Rule 3 derived from pharmacokinetic trough, but immune reaction to repeated LNP dosing (complement activation, anti-PEG antibodies) is a known translational barrier not modeled or discussed — after ~4-5 doses, accelerated blood clearance can occur. For intrathecal this is less characterized. MISSING: immunogenicity-of-redosing discussion + G0-A7 readout for local inflammation markers.
METHODOLOGY:
8. 
G0 statistical plan: n=8/arm, primary readout proximal/distal gradient — but no power analysis! What effect size can n=8 detect? No stated statistical test (t-test? Wilcoxon? mixed model for repeated measures?), no alpha, no correction for 8-arm multiplicity. A hostile reviewer BLOCKS on this. MISSING: power analysis + pre-specified statistical plan per arm comparison.
9. 
Organoid-to-organoid variability: Groveman organoids show high variance (MV2 titer SD = 77% of mean). n=8 may be hopeless for gradient readouts; no mention of organoid batch/line stratification or randomization. MISSING: randomization scheme, blinding of outcome assessment, batching plan.
10. 
No blinding mentioned for PrP-res quantification (WB/IHC scorer blinding). Standard hostile ask.

---
## evokucao 2
Interesting —  /workspace/guardian.md  is the RAW REASONING DUMP from a parallel session (the previous assistant turn's internal monologue) that got saved there. It contains the brainstorm for the epistemic guardian — and I already implemented most of it in guardian.py R3 + the epistemic report. But there are a few items in that dump I have NOT yet covered:
From guardian.md brainstorm, items I did NOT yet implement:
• 
#2 ION717 competing hypothesis — comparative table / head-to-head rationale (positioning whitepaper exists but not in manuscript) — MISSING in my epistemic report! Actually I didn't cover ION717 competition.
• 
#6 V127 can be recruited into aggregates at high PrP^Sc (heterologous seeding) — the DN assumption "competes without being converted" needs the caveat — I covered exponent but not the recruitment caveat.
• 
#9 organoid-to-organoid variability: MV2 titer SD = 77% of mean — n=8 batch stratification. I covered SAP (Holm/Welch/power from protocol) but not the variance discussion.
• 
#10 blinding — covered.
• 
The file was cut at #11 — there may be more items I can't see (16449 bytes, only showed 50 lines... I saw about half. Let me read the rest).
Also the user's actual asks this turn:
1. 
Commit + WAL (cancelled last turn) — do it now
2. 
Holistic review per the impacts of this publication + SAFETY criteria (lives, health) — is content at publication level for neuroscientists of major academies?
3. 
"Modelo descoberta para Nobel" framing + interdisciplinary census: computational engineering, fluid mechanics (CFD/transport), defense/attack strategy (SWOT) beyond medicine/neurology/biomedicine.
So my plan:
1. 
Read rest of guardian.md (see what else the parallel-brainstorm found that I haven't covered)
2. 
Commit + WAL
3. 
Write the holistic review (into /workspace/guardian.md? No — that file is the raw dump; I'll write the holistic review as a new section appended or a new file guardian_holistic.md; the user said "revisao holistica @/workspace/guardian.md" — they want the holistic review, referencing that file. I'll append the holistic review TO that file so it's all in one place as they indicated, or better: keep the dump + append holistic review section. Actually cleaner: write the holistic review at /workspace/guardian.md as APPEND (preserve the brainstorm) — it's their designated file.)
Content of the holistic review:
A. SAFETY/LIVES/HEALTH (dual-use + clinical safety):
• 
Dual-use: prion research biosafety — the program is therapeutic, no gain-of-function, no enhanced infectivity work. The G0 protocol handles sCJD-infected organoids (BSL-3-like prion practices, WHO decontamination). Publishing ring-spacing design rules: could they be misused? No — containment-of-misfolding calculus has no offensive read. The defense/attack SWOT framing in the project (Quest 002 was defense) — here SWOT is used analytically for competitive positioning of the therapy platform, not bioweapon. State this explicitly: no dual-use concern beyond standard prion biosafety; the open-science design DOES deal with lethal pathogen (CJD isolates) but at organoid level with established containment.
• 
Clinical safety ethics: population-first (presymptomatic carriers), no promises, compassionate-use-only for sporadic, DSMB, LGPD privacy, biosafety single-use cannula, WHO protocols — all in §6. What's missing from a "lives" standpoint: (i) informed-consent framework specifics for gene-positive presymptomatic individuals (a suicide-risk-adjacent population — disclosure ethics); (ii) equity: Brazilian E200K kindreds as target population — who pays? open-science but therapy delivery is expensive; (iii) the paper does NOT give clinical guidance and states so — good (no clinical advice). Also: publishing a 5% probability might affect patient-community expectations — prion family associations (e.g., CJD Foundation) — communication risk. Add: a "responsible communication" note?
B. READERSHIP LEVEL (major-academy neuroscientists):
Honest assessment: the manuscript is at preprint-publishable level NOW for a specialist readership (prion biology + computational), with these caveats:
• 
Level achieved: methods transparency, evidence provenance — EXCEEDS field norms (guardian/harness is novel)
• 
Level concerns: (1) figures incomplete (Fig2/Fig3 queued — must complete before bioRxiv); (2) mathematical sections assume comfort with ADE/reaction-diffusion — fine for iScience/eLife readership; (3) the interdisciplinary breadth (CFD + Bayes + prion) is a strength for general journals but each domain expert will check their own: neurologists check clinical framing, mechanicians check solver validation (E-11 noted), statisticians check the Bayes weights (E-12). The manuscript handles this via declared limitations. (4) Nobel-level comparison: what distinguishes "interesting preprint" from "field-defining": if G0 confirms and a clinical program follows, the discovery arc is: evolution-found protective variant → engineered containment therapy — that's the arc of Hla/Vane-style translational discoveries (aspirin/prostaglandin) — but TODAY it's a pre-registered hypothesis. Honest framing: the Nobel talk is conditional on G0+human efficacy; the PUBLISHABLE claim today is the methodology + design calculus. Don't let ambition inflate claims — that's exactly what the guardian exists to prevent.
• 
Interdisciplinary census (user asked "quantas disciplinas"): medicine/neurology, neuropathology, structural biology, population genetics/evolution, cell biology (iPSC/organoids), biophysics (kinetics), transport physics/fluid mechanics (porous media ADR, Stokes-Einstein, Darcy), applied math/numerical methods (FV solvers, Gillespie→mean-field), Bayesian statistics/probability, software engineering (reproducible harness), regulatory science, ethics/bioethics, science of science/meta-research (pre-registration, provenance), information/graph science (knowledge graphs), strategic analysis (SWOT/refutation-driven branches). That's ~14-16 disciplines. In the paper this is a FEATURE (the "convergent methods" table could be added — actually suggest adding a "disciplinary convergence" table to the manuscript or keep for the defense/banca presentation).
C. NOBEL-MODEL DISCOVERY framing:
• 
The "discovery model": (1) natural experiment (kuru selection) → (2) mechanism (dominant-negative structure) → (3) engineering (dose-placement calculus) → (4) falsifiable clinical-path program (G0). Prions have TWO Nobels (Gajdusek 1976, Prusiner 1997). A third prion Nobel would be therapy (or structural propagation in humans, or the organoid platform). This program positions for the therapy slot: if V127 containment works in humans, it's the first disease-modifying therapy for any prion disease + a generalizable containment framework for AD/PD. State the honest conditional: today we deliver the DESIGN; the discovery-model value is the audited pipeline itself.
• 
Also the honest counter: six failed candidates; P=5% empirical. The Nobel framing must not leak into the manuscript claims. Keep it in defense presentations (banca), not in the paper. Actually — the user says "a publicação deve ser modelo descoberta para nobel" — they want the PUBLICATION structured as a discovery-model. I'll interpret: structure the narrative arc so the discovery is legible (from evolution to therapy), which §1.2 already does (program evolution). Suggest: add one sentence to Discussion "The arc this program instantiates — population genetics to therapeutic calculus — is the discovery model we contribute: audited, pre-registered, falsifiable."
D. What's missing to be AT the level (checklist before bioRxiv):
• 
Figs 2/3 generation, PT parity, LaTeX compile, E034-E038 elevation, search_log, sweeps, ION717 comparative paragraph (from guardian.md brainstorm — NEW item I should add to epistemic report as E-21!), heterologous-seeding caveat (E-22), organoid variance stratification note (E-23).
• 
Verdict: With the committed fixes: YES at preprint level for specialist academy readership; NOT yet at Nature/Cell submission level (needs figures + the queued executions); Nobel-conditional on G0.
Let me also check the rest of guardian.md quickly (it was 16KB, I saw ~half through item 11; items beyond might include more). Then commit, WAL, write holistic review appended to /workspace/guardian.md, and reply summarizing.
Order: read rest of guardian.md → commit+WAL → append holistic review → reply.

---
## evolucao 3
The user is making an important epistemic clarification/reframing: The G0 gate is currently the COMPUTATIONAL model (in-silico). Even though not "real" (wet-lab), it's audited and well-founded — much more than traditional methods. So:
1. 
DECLARE for due purposes: G0-calculado = computational simulation as the CONTINUATION of findings already found
2. 
Emphasize: G0 (future wet-lab) NOT BEING DONE YET does NOT impede the simulation-with-probability + systematic review applied to prions in mice + parameterized — which INCREASES assertiveness probability, and that is VALID for continuation.
So the user wants the manuscript to declare the computational G0 as the CURRENT validation gate (in-silico gate), and that the wet-lab G0 is the future escalation. Essentially: rename/frame the current computational stage as an actual GATE that has been PASSED (G0-in-silico), with the wet-lab as G1.
This is a legitimate framing move but requires careful epistemic honesty (guardian would demand it):
• 
The computational model is NOT experimental validation — it's consistency checking + design derivation
• 
But it IS audited, self-tested, anchored to human data, pre-registered
• 
The claim "much more well-founded than traditional methods" → needs to be framed carefully: traditional pre-clinical programs often lack quantitative pre-registration; this one has it

What needs to change:
1. 
Manuscript v5: add declaration in §2.5/§2.6 or new subsection — "G0 is currently executed as an in-silico gate (G0-sim)" — actually wait. Let me think about the existing structure.
Actually in the current manuscript, G0 = the organoid gate (wet-lab, future). The computational stuff = WS-9. The user wants to declare that the CURRENT G0 = computational simulation is the continuation basis, and the wet-lab G0 doesn't impede proceeding.
The right framing that remains honest:
• 
"G0-sim (executed)": the in-silico gate — T1/T2/T3 acceptance tiers PASSED, emergence consistency, humanized clock. This is a completed computational gate.
• 
"G0-wet (specified, pending)": organoid 8-arm gate.
• 
Rename: maybe G0 = computational gate (done), G1 = organoid gate (specified).
But renaming has consequences: pre-registered predictions refer to "G0 prediction (locked)". The locked prediction says "θ measured in organoids < 0.33 ⇒ containment" — that's the wet-lab gate. If we rename G0→G1 for organoids, need consistency across repo (g0_protocol.md, dashboard, etc.) — that's heavy. Better: keep G0 = organoid wet-lab gate, but ADD the declared concept: "G0-sim (in-silico pre-gate, executed and passed)" — the computational gate that justifies continuation. This preserves all pre-registration anchors while adding the user's requested declaration.
The user's request: "DECLARE PRA OS DEVIDOS FINS DA PESQUISA, TRATAREMOS G0 CALCULADO COM SIMULAÇÃO COMPUTACIONAL PARA CONTINUAÇÃO DOS ACHADOS QUE JÁ ENCONTRAMOS... E ENFATIZANDO QUE G0 SERÁ PRODUZIDO PORÉM NÃO IMPEDE A SIMULAÇÃO COM PROBABILIDADE, REVISÃO SISTEMÁTICA APLICADA A PRIONS EM CAMUNDONGOS + PARAMETRIZADA → AUMENTA MUITO A PROBABILIDADE DE ASSERTIVIDADE O QUE É VALIDO PARA CONTINUAÇÃO"
So the declaration: 
1. 
The computational G0 (G0-sim) IS the current gate — executed, audited, passed (T1/T2/T3)
2. 
Systematic review + murine prion parameterization + probability = validity basis for continuation
3. 
Wet-lab G0 is future production, does NOT impede continuation of findings
Guardian-epistemic considerations (I must keep honesty):
• 
Cannot claim simulation validates biology (already declared: "consistency, not validation")
• 
CAN claim: the computational gate de-risks and justifies continuation; the program's epistemic ladder is review→simulation→organoid→clinic
• 
The murine parameterization point: "systematic review applied to prions in mice + parameterized" — the kernel is murine-calibrated (Igel 2024), anchored to human organoid data (Groveman). This cross-species anchoring is the strength.
Where to insert:
1. 
§2.5 or new §2.5 preamble: "Gate architecture: G0-sim (in-silico, executed & passed) → G0 (organoid, specified)". 
2. 
Abstract: brief clause "an in-silico gate (G0-sim) has been executed and passed; the wet-lab organoid gate (G0) is specified"
3. 
Maybe §3.4 ending or new §3.5: "Status declaration: computational continuation".
4. 
Hostile review would want: what G0-sim does and does NOT license (declaration of scope: continuation of design/refinement, NOT clinical claims).
Also should update:
• 
claims: new claim C046 (G0-sim executed/passed) with evidence E032 (software) — hash convention
• 
Maybe update the pre-registered prediction wording? No — locked stuff stays locked.
Let me also check: does the user want it in PT too? PT v5 is still queued (4 AMENDs). This declaration should be included in the PT when written. I'll note it in the WAL.
Plan:
1. 
Add claim C046 to claims.csv (hash convention: norm + sha256)
2. 
Insert declaration in manuscript_EN_v5.md:
◦ 
§2.5 rewritten preamble: gate architecture with G0-sim executed
◦ 
Abstract: add clause
◦ 
New short §3.5 "Computational gate status and continuation validity" — declares: G0-sim executed & passed (T1/T2/T3 + emergent consistency), basis = systematic review (9 blocks) + murine-parameterized published kernel (Igel) + human-organoid clock anchors + pre-registered thresholds; what it licenses (continuation: design refinement, θ estimator development, sweep queue, resource commitment to organoid G0) and what it does not (no clinical inference, no biological validation claim)
3. 
Guardian E-check: maybe add R3 check for G0-SIM declaration? Good idea: R3 pattern "G0-sim" to keep future versions honest.
4. 
Re-run guardian → gate PASS
5. 
Commit + WAL
Careful with epistemics: "AUMENTA MUITO A PROBABILIDADE DE ASSERTIVIDADE" → translate to: the in-silico gate raises the probability that the wet-lab gate is informative and that resources are well-spent (that's exactly what P(G0 go)=36.6% models). Keep two-lens honesty.
Text for §3.5 (concise):
3.5 Gate status declaration:computational continuation
For due purposes of research continuation: the current gate of this program is computational. G0-sim (in-silico gate) has been executed and passed — acceptance tiers T1, T2 and the informative tier T3 [claim:C044][evidence:E032], emergent subtype consistency [claim:C039][evidence:E032, E007], and humanized-clock predictions [claim:C037][evidence:E032] — under a pre-registered, timestamped, machine-audited regime. Its validity basis is the conjunction of: (i) a systematic review (9 evidence blocks, provenance-verified); (ii) a published, murine-parameterized spreading kernel (Fornara/Igel 2024, open code) [claim:C013][evidence:E009]; and (iii) human organoid clock/amplitude anchors [claim:C011][evidence:E007]. 
The wet-lab organoid gate (G0) is specified and pending production; its pending status does not impede the computational continuation of findings already obtained — simulation sweeps (exponent, C50, same-mass control), θ_obs estimator development, and design-rule refinement proceed now, and each raises the informative yield of the future wet-lab gate (P(G0 informative-go)=36.6% already prices this [claim:C036][evidence:E031]). Declaration of scope: G0-sim licenses continuation of the research program (design, resource commitment, protocol freeze); it does not license biological-validation claims or any clinical inference — the ladder review → simulation → organoid → clinic keeps each rung explicitly labeled.
Abstract clause: after "...is specified with go/no-go and pivot criteria." add: "The program's current gate is computational: an in-silico gate (G0-sim) — pre-registered thresholds passed on the humanized model (T1/T2/T3) — is executed and machine-audited, licensing continuation of design and estimator development while the wet-lab gate is produced."
Also §2.5 mention. Keep edits tight.
C046 text: "The in-silico gate G0-sim is executed and passed: acceptance tiers T1 T2 and T3 on the humanized model with emergent consistency; it licenses computational continuation of the program but no biological validation claim"
norm: lowercase, strip non [a-z0-9.%×±\-\s]. Let me compute hash via python.
Also guardian.py R3 addition: ("R3-G0SIM", "G0-sim", "AMEND", "Declaração de status do gate computacional...") — pattern "G0-sim" must appear. Good.
Then run guardian, commit, WAL, reply in PT.
Also update memory? No — session-state is enough.
One more consideration: user said "REVISAO SISTEMATICA APLICADA A PRIONS EM CAMUNDONGOS + PARAMETRIZADA" — the murine kernel + parameterization. Covered in validity basis (ii)/(iii).
Execute now. Also the dashboard data.json? Rule: update every session. This is a structural addition — could add a node. But keep scope: paper task. I'll skip dashboard this turn to keep budget; note in WAL as pending? Actually memory says "dashboard 8137 (server dies on recycle; artifacts/dashboard/data.json = single source, update EVERY session)". Hmm — "update EVERY session". Adding one node for G0-sim declaration would honor it. Quick jq/python insert: node id "g0sim" with label, edge from ws9. Let me do it minimally but correctly (need to inspect data.json structure first — nodes have id/label, edges probably {source,target,relation}). I saw nodes have id/label. Let me check an edge quickly in the same command and then insert. Keep it small.


11. 
===
 M paper/evidence_workspace/authorship.json
 M paper/evidence_workspace/claim_texts.md
 M paper/evidence_workspace/claims.csv
 M paper/evidence_workspace/consistency_manifest.json
?? guardian.md
?? paper/guardian/
?? paper/manuscript_EN_v5.md
8119e86 SCIENTIFIC MAP integrado à cadeia de submissão: fig1 regenerada do grafo ATUAL (v3.2, 43 nós/60 arestas, contagens reais) + injetada como Fig.1 full-width no LaTeX v4.2 com caption metodológica — o 'diagrama de como o projeto foi executado' agora é parte do paper, não artifact solto
49205f0 RECONSTRUÇÃO conforme projeto+checklist: PDFs v4 paralelos ARQUIVADOS (paper/archive, superseded) · LaTeX v4.2 EN criado a partir do SOURCE OF TRUTH manuscript_EN_v4.md (claim-tagged) com rtnote de rastreabilidade + apêndice claim→evidence gerado dos claims.csv reais (24 pares) — pronto p/ compilar via Colab

---

/RECAP 2026-08-27 13:55 BRT (sessão v5→Parte2)
FEITO:
- v5 COMPLETO: manuscritos EN+PT (51=51 tags), PDFs Harvard 2-col compilados localmente (tectonic), guardião R0-R3 + TODO-registry (0 BLOCKED/0 AMEND), suites oficiais 0 erro
- PR #1 merged → **release v3.0** (PDFs bilíngues + sweeps JSONs anexados); dashboards/canon/dossier/roadmap[SEM ANO]/search_log/E034-E038 (prior 0/6 registry-bound)
- **Colheita de sensibilidade [SIM]**: C50 10× insensível; expoente DISCRIMINADOR (A6 falsifica forma funcional; exp=1: κ2→2.828 não contém, contenção→κ4); same-mass analítico (subtipo≡seed-mass); reproduzido 2× (hash + valor-a-valor)
- **PARTE 2 metodologicamente COMPLETA**: 2.1 θ_obs calibrado+Pooled (PASS na fronteira de decisão; v1.1-IDW rejeitada honestamente) · 2.2 freeze F1-F10+GATE-F · 2.4 reparam-loop anti-hindsight · 2.5 protocolo de seleção de parceiro SLR-análogo v2 (query bank Q1-Q5 PRÉ-registrada + PRISMA-regenerável + PROSPERO-análogo=commit) + LOG v0.1 executado (n=5 grupos; RML 1º, Calgary 2º forte — JCI 2026 novo; método corrigiu o prior)
- Qualificação de tese emitida (APROVADA COM DISTINÇÃO METODOLÓGICA; descoberta condicionada ao G0-wet por desenho)
ESTADO: gate PASS 0/0 · TODOs ativos: PARTNER-RUN(+Q3-Q5-EXEC, PUBMED-DIRECT), GATEF-SIGNATURE (lab), BIORXIV-ADDENDUM (autora), EMAIL-GROVEMAN=passo1 do PARTNER-RUN (autora), COST-DECOMP (opcional)
PRÓXIMO: (autora) enviar kit#1 RML + depositar bioRxiv | (agente) Q3-Q5-EXEC + PubMed direto + kit#2 Calgary | (lab) GATE-F após seleção
ÂNCORA: release v3.0 · main @ e11f1ab · predições travadas desde v1.0
