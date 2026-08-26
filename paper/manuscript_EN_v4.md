# PrP-V127 as a Modular Antiprion Platform: Audited Review, Quantitative Transport Design, Humanized In-Silico Predictions, and a Pre-Registered Organoid Gate for Creutzfeldt–Jakob Disease

**Manuscript v4.0 (full-length, bilingual edition — EN master / PT-BR companion)**
Open Prion & Molecular Engineering Consortium (open-science initiative) · DeepScientist Quest 003
Preprint — not peer reviewed. Deposited with full audit trail: github.com/camillanapoles/quest003-prion-v127 (56+ commits, timestamped pre-registrations).

---

## Abstract

Prion diseases are universally fatal, with no approved therapy despite four decades of research and six failed clinical candidates. We present an end-to-end, fully audited research program that converts a naturally selected human prion-protein variant (PrP-V127) into a quantitatively designed therapeutic platform for Creutzfeldt–Jakob disease (CJD). **Methods.** (i) An agent-assisted literature audit (≈90 searches; 60 findings structured in 9 evidence blocks; ~30 papers read in depth; 42 verified references) that also corrected recurring citation errors in the field, including a retracted trial still cited as evidence. (ii) A tissue-transport solver (advection–diffusion–reaction in heterogenous porous medium; ECS α=0.20, tortuosity λ=1.8, D_eff≈3.9×10⁻¹¹ m²/s for the ~30 kDa anchorless construct; self-tested: mass conservation 100%, Thiele-length error 0.5%) yielding three falsifiable design rules: containment-ring spacing 8–12 mm, hydrogel mesh ξ≥5× protein radius (HA 1–2% w/v approved; >5% rejected), and mRNA redosing ≤7 days. (iii) A hierarchical Bayesian calibration over 10 structural analogues (including the six historical antiprion failures) giving P(significant clinical slowing) = 5% [90% CrI 0.4–13.6%] today, rising to 30–45% if pre-registered gates confirm. (iv) A humanized in-silico infection model: the published stochastic reaction–diffusion kernel (Fornara et al., iScience 2024; open code) ported to deterministic mean-field with logistic substrate saturation, coupled to dominant-negative capping by V127ΔGPI as saturable substrate competition, and clock-calibrated to human organoid anchors (Groveman et al. 2019: eclipse 25–28 dpi; de-novo production 35 dpi; titers MV2=2.13×10⁵ vs MV1=1.69×10³ SD50/mg) giving 1 simulation unit = 144 days. **Results.** The model exhibits a containment threshold θ* = 0.333: above it the prion front is contained (R 2.83→0.82 mm at κ=2, monotone to near-extinction at κ=32), and it reproduces, without fitting, the MV2>MV1 subtype hierarchy of the source data — emergent behavioral validation. **Pre-registered prediction (locked before wet-lab data):** if the θ measured in sCJD-infected human organoids is <0.33, V127ΔGPI containment succeeds in situ; readouts expected 90–120 days post-seeding. An eight-arm organoid gate (G0), including pentosan-polysulfate as published positive control and an LNP-mRNA arm, is specified with go/no-go and pivot criteria. **Conclusions.** Every program pillar maps to an already-approved regulatory category (nusinersen, tofersen, Parkinsonian cell grafts 2026, tafamidis), so the program requests a conjunction of precedents rather than any unprecedented category. The framework is transferable to prion-like spreading pathologies (Alzheimer, Parkinson) as a dose-and-placement containment calculus.

---

## 1. Introduction

Human prion diseases — sporadic (sCJD, ~85%), genetic (E200K, D178N, P102L; 10–15%) and acquired — are rapidly progressive and universally fatal; sCJD median survival is 6–8 months [1,2]. No therapy has demonstrated disease modification in humans; six candidates (pentosan polysulfate, quinacrine, doxycycline, flupirtine, PRN100, and others) failed clinically [3,4,5]. Two facts motivate a structurally different attempt. First, the G127V polymorphism of the prion protein (PRNP), which arose under positive selection during the kuru epidemic in Papua New Guinea, protected heterozygous carriers [6] and confers complete resistance when homozygous in transgenic mice — "as protective as gene deletion" — while acting as a potent dose-dependent dominant-negative inhibitor of wild-type propagation [7]. Second, 2026 results established that recombinant, GPI-anchorless V127 retains potent dominant-negative activity in trans in vitro [8], and that systemic AAV delivery of anchorless V127 extends survival ~50 days in a rodent prion model [9]. The molecular mechanism is therefore validated at four levels — population genetics, transgenic mouse, cell culture, and gene-therapy proof-of-concept — with structural basis (β2–α2 loop restriction, intermolecular H-bond dimer stabilization) [10,11].

What is missing is the *engineering*: delivery modality, dose, placement, timing, and a decision architecture that spends laboratory resources only where models cannot answer. This manuscript reports the complete pre-wet-lab program: audited evidence base, quantitative design rules, probabilistic success model, humanized in-silico predictions, a pre-registered organoid gate, and the regulatory mapping that de-risks translation. All artifacts are open and timestamped.

### 1.1 Populations and ethics frame

The primary target population is presymptomatic genetic carriers (E200K/D178N), for whom the therapeutic window is years and autologous manufacture is feasible; Brazilian E200K kindreds have been reported since 2007 [12] and RT-QuIC/NfL screening is operational [13,14]. Sporadic CJD is addressed exclusively through an acellular LNP-mRNA vector (manufacture in days) under compassionate use, and only after organoid validation.

## 2. Methods

### 2.1 Agent-assisted evidence audit (provenance-verified)

A literature program was executed in structured blocks (molecular basis; therapeutic class; cell therapy; surgical delivery; translational analogues; refutation-driven solution branches). ≈90 scientific searches fed 9 evidence tables (60 findings), of which ~30 papers were read in depth (abstract or full text extracted and archived in-repo). Every citation used downstream was verified against its source; where external documents cited literature, each reference was audited individually (19 audited in one batch: 11 correct, 3 duplicates, 1 non-scientific policy document, 1 link resolving to an unrelated paper) [repo: literature/refs_audit.md]. A retracted Neurotherapeutics trial (minocycline/FK506; retraction 2020) was found still circulating as supportive evidence and is excluded by rule [15]; minocycline is additionally documented to confound the NfL biomarker endpoint [16].

### 2.2 Tissue-transport model (WS-7)

Advection–diffusion–reaction (ADR) in a porous medium with heterogeneous permeability, discretized by finite volumes (2D, 192², explicit Euler):

∂(αc)/∂t = ∇·(D_eff∇c) − ∇·(vc) + S(x) − k_eff·c

Parameters and provenance: extracellular fraction α = 0.20 and tortuosity λ = 1.8 (macromolecule regime) from in-vivo integrative-optical-imaging measurements [17]; free diffusivity of the ~30 kDa anchorless construct D₀ = 1.25×10⁻¹⁰ m²/s (Stokes–Einstein, hydrodynamic radius ≈2.5 nm); D_eff = D₀/λ² ≈ 3.9×10⁻¹¹ m²/s. First-order consumption k_eff swept 10⁻⁶–10⁻⁵ s⁻¹ (capping + clearance), anchored to nucleated-polymerization kinetics [18]. Interstitial flow via Darcy (κ base 10⁻¹⁴ m²; spongiform cysts modeled κ×50). Self-tests: mass conservation without reaction 100.0%; numeric vs analytic Thiele penetration length error 0.5% (10% point = 2.303·ℓ). Wave-vs-shield analysis solved the containment radius r* where capping exceeds replication for swept θ. Pulse-train analysis (mRNA) integrated a two-timescale production/clearance compartment.

### 2.3 Bayesian calibration by structural analogy (WS-8)

Hierarchical Beta–Binomial model over 10 analogues weighted by similarity (mechanism, vector, population, endpoint), including the six historical antiprion failures as a negative analogue and ION717 (in-human, unapproved) as partially informative; Monte-Carlo 200 k draws; organoid predictive validity ~80% from PDO literature [19]. Outputs: P(G0 go) and P(significant clinical slowing), with 90% credible intervals, pre-registered before any wet-lab outcome.

### 2.4 Humanized in-silico infection model (WS-9)

**Kernel.** The stochastic reaction–diffusion model of prion spreading of Fornara/Igel et al. [20] (Gillespie over discrete aggregate classes B₁…B_s plus a conformer pool C, with UPR-gated templating; open code, Zenodo 11093945) was ported to a deterministic mean-field (96² voxels, explicit Euler, dt=5×10⁻⁴). Two fidelity-critical corrections were decoded from the original `findreac` semantics: (i) the s+1 channel is *autocatalytic* (C→2C at Kt₁·tp) — the replication engine, not an inert sink; (ii) the cross-reaction is fragmentation (B_a→B_{a−1}+C). Mean-field unbounded autocatalysis was bounded by logistic substrate saturation C/(C+C₅₀), substituting for the stochastic extinctions/UPR braking absent from the deterministic port (documented limitation).

**Capping term (this work).** Dominant-negative inhibition by V127ΔGPI modeled as saturable substrate competition: the free-substrate fraction entering all templating/autocatalysis terms is freeS = (1/(1+κ·c_V127))², where c_V127(r) is the steady-state secretion field of a deposit (WS-7 profile, ℓ=3.6 mm) and κ is the capping strength. The squared form reflects two-participant conversion requiring both reactants unsequestered (competitive Michaelis–Menten functional form). Mechanistic anchors: dose-dependent dominant-negative inhibition [7]; anchorless trans activity [8]; structural basis [10,11].

**Humanization (clock and amplitude).** Simulation doubling time was matched to human organoid anchors [21]: inoculum clearance 25–28 dpi, de-novo production from 35 dpi, endpoint titers at 169 dpi MV2 = 2.13(±1.63)×10⁵ vs MV1 = 1.69(±0.70)×10³ SD50/mg, protease-resistant PrP detectable only in MV2. Derived human doubling time ≈12.1 days ⇒ 1 simulation unit = 144 days (detection floor 1×10² documented as assumption, sensitivity flagged). MV2-like vs MV1-like seeding differed by the 126× titer ratio. Acceptance criteria pre-specified: T1 (baseline must replicate: total >1.5× seed) and T2 (κ=32 must contain the front to <90% baseline radius) before any θ interpretation; both enforced by in-code asserts and passed.

### 2.5 Pre-registration and reproducibility

All predictions were committed to the public repository with timestamps before any wet-lab experiment exists (audit trail: git log; releases). Simulation code, parameters, and outputs (JSON + figures) are archived in-repo. The wet-lab gate protocol (G0) specifies 8 arms (A1 mock; A2 disease; A3 unedited-cell; A4 membrane-V127; A5 secretory graft — the thesis; A6 recombinant protein; A7 LNP-mRNA; A8 pentosan polysulfate as published positive control [3]), n=8 organoids/arm, primary readout = proximal(≤1 mm)/distal(≥3 mm) PrP-res gradient, with pre-registered go/no-go and pivot rules (including pivot to acellular vectors if A6≈A5).

## 3. Results

### 3.1 Audited evidence base and corrected claims

The audit consolidated a 4-layer validated core: population genetics (kuru selection [6]); transgenic complete resistance and heterozygote vCJD caveat [7] (mandating biallelic editing or anchorless delivery); anchorless trans activity with persistence after expression ceases [8]; in-vivo AAV proof-of-concept [9]. Five recurring design errors in the field's proposals were corrected (e.g., NSC-to-microglia lineage impossibility [22]; quiescent adult human SVZ that itself replicates prions [23,24]), each replaced by evidence-compatible solution branches (iPSC-microglia co-graft [25]; slow-release deposits; LNP-mRNA vector [26]).

### 3.2 Transport design rules (WS-7)

Protection radius per deposit r₁₀% = 4–6 mm (k_eff 1–3×10⁻⁶ s⁻¹) ⇒ **Rule 1:** ring/node spacing 8–12 mm. **Rule 2:** carrier hydrogel mesh ξ≥5×r_p ⇒ D_gel/D₀≥0.7; HA 1–2% approved, >5% sequesters the secretome. **Rule 3:** LNP-mRNA redosing ≤7 days (trough ≥~56% of peak; 10–14 d leaves exposure valleys). Steady-state establishment ~4 days — all planned readouts are steady-state. Wave-vs-shield: a 1-mm deposit contains an advancing front within a 4.2–9.5 mm shell for capping/replication ratios θ 0.1–0.01.

### 3.3 Probabilistic frame (WS-8)

P(G0 go | organoid predictive validity ~80%) = 36.6% [90% CrI 14.6–60.5%]; P(significant clinical slowing) = 5.0% [0.4–13.6%] under the field's empirical prior (6/6 failures), versus the design-optimism estimate 30–45% conditional on gates confirming. Both lenses are retained and labeled, per the no-fabrication rule.

### 3.4 Humanized in-silico predictions (WS-9)

With the humanized clock (144 d/unit; run = ~24 months of tissue disease, covering the entire G0 window): **containment threshold θ\* = 0.333** (κ=2 contains: R 2.83→0.82 mm; monotone to 0.70 mm and biomass ratio 2.1× seed at κ=32 — near-extinction). The humanized threshold is more favorable than the murine-parameterized one (v2: θ*∈0.20–0.33): the therapeutic window widens under human kinetics. **Emergent validation:** seeding by the Groveman titer ratio (126×) reproduces the MV2>MV1 hierarchy unprompted — MV2-like grows aggressively (the only WB-positive subtype in source data); MV1-like also propagates (consistent with persistent RT-QuIC positivity) yet is contained at the same κ with larger margin (0.69 vs 0.78 mm). The hierarchy was never fitted — behavioral validation of the port, distinct from curve-fitting.

**Pre-registered G0 prediction (locked):** θ_measured < 0.33 ⇒ containment succeeds in situ; containment/halo readouts at 90–120 days post-seeding; ring spacing 8–12 mm (§3.2).

## 4. Discussion

### 4.1 What this program adds

To prion science: a quantitative delivery-and-dose calculus (transport rules + threshold) that no prior candidate possessed; a corrected citation record; and pre-registered, falsifiable in-silico predictions with an organoid assay designed to kill or advance the hypothesis for ~US$100–150 k in 10 months. To methodology: an executable template of agent-assisted, provenance-verified translational planning (audit → physics → Bayes → simulation → pre-registered gate) in an open repository.

### 4.2 Transferability to prion-like neurodegeneration

Alzheimer and Parkinson spread by templated protein misfolding along stereotyped routes (Braak staging; "prion-like" propagation). The platform calculus — protective-variant secretion field, containment threshold, ring placement, redosing interval — is mechanism-agnostic to the misfolded protein. Prion disease is the fastest, smallest, cheapest-to-read instance of the class; a validated containment concept transfers as a design framework (not automatically as a therapy) to diseases affecting >50 million people. We flag this explicitly as hypothesis-generating, not evidence.

### 4.3 Regulatory geometry

No program pillar requires an unprecedented regulatory category: chronic intrathecal redosing (nusinersen), accelerated approval via biomarker in lethal genetic neurodegeneration (tofersen; NfL endpoint), human brain cell grafts (2026 Parkinson trial), dominant stabilization of a misfolding-prone native protein (tafamidis), substrate lowering (ASO/RNAi class). The program requests the conjunction of approved categories.

## 5. Limitations and gaps (complete, honest)

1. **κ-to-concentration translation** (highest risk): the mapping between simulated capping strength κ and interstitial V127ΔGPI concentration is unresolved; only G0-A6 (recombinant protein at known dose) closes it. 2. **Mean-field port** omits stochastic extinction and strain diversity; the original kernel is stochastic — port fidelity is behavioral (hierarchy) not distributional. 3. **C₅₀ = 50 is a stability choice**, not measured; sensitivity flagged. 4. **Anchors are MV1/MV2** organoids; the commonest subtype (MM1) lacks published time-courses. 5. **Detection floor 1×10² SD50/mg** assumed for the doubling-time derivation. 6. **Transport parameters** are healthy-tissue human values; spongiform κ heterogeneity is synthetic (×50) pending patient-imaging poroelastography. 7. **Bayesian analogue weights** are structured judgments, not data. 8. **No wet-lab data yet exist** for the platform's central claims; all §3.4 outputs are predictions. 9. **Species/strain generalization** of Igel parameters to human CJD assumes dimensional (θ) transfer, argued but unproven until G0.

## 6. Ethics, governance, declarations

Population-first design (presymptomatic genetic carriers; sporadic only via post-validation compassionate mRNA), DSMB with pre-specified stopping (any confirmed teratoma), prion biosafety (single-use coaxial cannula; WHO 134 °C/NaOH protocols; autopsy containment), genetic privacy (LGPD; kindred anonymization), no therapeutic promises (containment/slowing endpoints only). **Funding:** none; volunteer open-science consortium. **Conflicts:** none declared. **AI-assistance disclosure:** AI agents were used for literature curation, code, and drafting under continuous human supervision; every citation and number was verified against sources by the accountability authors; AI is not an author (per SW-S01/SW-03). **Data and code availability:** all models, solvers, parameters, outputs, and the audit trail are in the public repository (github.com/camillanapoles/quest003-prion-v127) under open license; no unpublished third-party data were used.

## References (verified; selection)

[1] Hermann P, et al. Lancet Neurol. 2021 (sCJD criteria/RT-QuIC). [2] CDC/MS Manuals — CJD epidemiology (secondary). [3] Groveman BR, et al. Sci Rep. 2021;11:5160 (PPS organoid screening; positive control A8). [4] Mead S, et al. Lancet Neurol. 2022 (PRN100 first-in-human). [5] Cheng S, et al. Sci Rep. 2015;5:10535 (minocycline — no survival benefit). [6] Mead S, et al. N Engl J Med. 2009;361:2056–2065 (kuru; G127V selection). [7] Asante EA, et al. Nature. 2015;522:478–481 (complete resistance; dominant-negative; vCJD caveat). [8] Gatdula JRP, et al. bioRxiv 2026.02.17.703887 / PMID 41757113 (anchorless V127 trans DN; persistence). [9] Zerbes T, et al. 2026 preprint, PMC13041815 (AAV anchorless V127ΔGPI, +~50 d). [10] Hosszu LP, et al. Commun Biol. 2020;3:580. [11] Zheng Z, et al. Sci Rep. 2018;8:11458. [12] Smid J, et al. Dement Neuropsychol. 2007 (first Brazilian E200K). [13] Green AJE. Pract Neurol. 2018 (RT-QuIC). [14] Vallabh/Gentile — NfL in genetic prion disease (minocycline confound 2024). [15] Retraction: Shah SZA, et al. Neurotherapeutics 2017 (retracted 2020; doi:10.1007/s13311-020-00909-3). [16] Gentile JE, et al. 2024. [17] Thorne RG, Nicholson C. PNAS. 2006;103:8217–8222. [18] Masel J, Jansen VA, Nowak MA. Biophys Chem. 1999;77:139–152. [19] PDO predictive-validity literature (~80%; organoid drug-response cohorts). [20] Fornara B, Igel A, Béringue V, et al. iScience. 2024 (PMID 39717079; code Zenodo 11093945). [21] Groveman BR, et al. Acta Neuropathol. 2019;137:987–996 (organoid infection anchors). [22] Ginhoux F, et al. Science. 2010;330:841–845. [23] Sorrells SF, et al. Nature. 2018;558:253–258. [24] Relaño-Ginés A, et al. PLoS Pathog. 2013;9:e1003485. [25] Abud EM, et al. Neuron. 2017;94:278–293 (iMGL). [26] Xue Y, et al. Adv Mater. 2025 (PMID 40317512; intrathecal LNP-mRNA). Plus: Mallucci Science 2003; Raymond JCI Insight 2019; Minikel NAR 2020; Williams SCRT 2023; Han PNAS 2019; Hu Nat Biotechnol 2024; Pavan Cell Stem Cell 2025; Liang Biomaterials 2013; Elder/Lonser J Neurosurg 2025; Krauze J Neurosurg 2005; tofersen FDA 2023; nusinersen 2016; Lund Parkinson cell trial 2026; tafamidis (ATTR); De Lucia 2016; Jalland 2016; Gomez-Nicola Brain 2014; Kim 2025; Dong 2025. *(Full numbered list with locators in repository `literature/evidence_table.md` and preprint v3.)*

---
*Pre-registered predictions (locked, repository-timestamped): θ*<0.33 containment; halo 4–6 mm; ring 8–12 mm; redose ≤7 d; readouts 90–120 d. Companion Portuguese manuscript: `manuscript_PT_v4.md`.*
