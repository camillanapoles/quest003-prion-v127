# DRAFT — NOT FOR SUBMISSION

This scaffold is intentionally incomplete. Remove this banner only after every local
validator passes and accountable human authors approve the final document.

# PrP-V127 as a Modular Antiprion Platform: An Open-Science Program From Population Genetics to Pre-Registered Organoid Predictions, Tissue-Scale Transport Design, and Regulatory Precedents for Creutzfeldt-Jakob Disease

## Abstract

Prion diseases are universally fatal; six clinical candidates have failed in three decades. We present a complete, audited, open-science program converting the kuru-selected variant PrP-V127 — which confers complete, structurally understood resistance and acts as a dose-dependent dominant-negative inhibitor [claim:C004][evidence:E001,E003], including as a secreted anchorless protein [claim:C005][evidence:E003] — into a deployable therapy. The program integrates: an audited review (41 source-verified references, one retraction excluded by rule [claim:C026][evidence:E032,E033,E034]); refutation-driven design (every refuted claim converted to an anchored solution branch); an eight-arm pre-registered organoid gate (G0) with a published positive control [claim:C013][evidence:E013]; tissue-scale transport engineering — a self-tested ADR solver yielding three falsifiable design rules [claim:C029][evidence:E035]; a humanized in-silico trial locating the containment threshold at θ* = 0.333 with the MV2>MV1 subtype hierarchy emerging unfitted [claim:C030][evidence:E036,E012]; and Bayesian estimates under two explicit lenses [claim:C031][evidence:E037]. The single remaining wet-lab gate arrives with all quantitative predictions locked in version control before any wet-lab data.

## Introduction

Human prion diseases are universally fatal; the sporadic form kills within months, and thirty years of candidates have produced six failures and zero approvals [claim:C011][evidence:E010]. We treat the development process itself as the engineering object. The molecular asset is PrP-V127: selected during the kuru epidemic [claim:C001][evidence:E002], proven to confer complete resistance when biallelic — with the heterozygote's vCJD permeability as a binding constraint on design [claim:C002,C003][evidence:E001] — structurally explained twice over [claim:C008][evidence:E005,E006], and validated as a secreted anchorless therapeutic principle in vitro and in rodents in 2026, with protection persisting after transgene cessation [claim:C005,C006,C007][evidence:E003,E004].

## Methods

**Design.** Program-level, multi-workstream, entirely computational and literature-based at this stage; one pre-registered wet-lab gate (G0) specified but not yet executed. No human or animal experimentation was performed by the consortium.

**Evidence discipline.** Every external claim was source-verified (fetch/read of open full texts or structured search) before adoption; three external drafts were audited (verification improvement documented: 11/15 → 6/6) [claim:C032][evidence:E038]. One retracted study is excluded by program rule [claim:C026][evidence:E034]. Industry-sourced statements (drug pipeline status) are flagged as non-peer-reviewed wherever cited [claim:C028][evidence:E040].

**Transport solver (WS-7).** Advection–diffusion–reaction on heterogeneous porous medium; ECS parameters from human in-vivo measurement (α=0.20, λ=1.8) [claim:C022][evidence:E021]; consumption parameterized 10⁻⁶–10⁻⁵ s⁻¹; explicit finite-volume scheme; self-tests: mass conservation 100.0%, Thiele length vs analytic 0.5% [claim:C029][evidence:E035].

**In-silico trial (WS-9).** Mean-field port of the public stochastic reaction–diffusion kernel of Fornara/Igel [claim:C023][evidence:E011] (reaction semantics decoded from the original implementation; stochasticity declared as a limitation), coupled to V127 capping as substrate competition: freeS=(1/(1+κc))². Clock calibrated to human organoid anchors: eclipse 25–28 dpi, de-novo production from 35 dpi, titers at 169 dpi (MV2 2.13×10⁵ vs MV1 1.69×10³ SD50/mg) [claim:C012][evidence:E012], yielding doubling time ≈12.1 d and 1 simulation unit = 144 days [claim:C030][evidence:E036,E012].

**Bayesian model (WS-8).** Weighted-analogue Beta/Jeffreys with Monte Carlo (200k draws); ten analogues including the six historical prion failures as the negative analogue and the sibling program ION717 (status: first-in-human, industry-sourced [claim:C028][evidence:E040]) as pending 0/1 [claim:C031][evidence:E037].

**Organoid gate (G0, specified not executed).** Eight arms on the validated sCJD-infected human organoid platform [claim:C012,C013][evidence:E012,E013], including secretory graft (A5), recombinant protein (A6), LNP-mRNA (A7) and PPS positive control (A8); primary readout: proximal(≤1mm)/distal(≥3mm) PrP-res gradient; n=8/arm; GO/NO-GO and pivot rules pre-registered.

## Results

**Program audit.** Molecular core: 8/8 findings valid [claim:C001–C008]. Two original-protocol claims refuted with literature and converted: NSC→microglia lineage [claim:C015][evidence:E024] → iPSC-microglia co-graft [claim:C018][evidence:E015]; SVZ permanent factory [claim:C016][evidence:E025,E026] → slow-release depot and transient vectors. Microglial function rehabilitated as pro-neurogenic [claim:C017][evidence:E027,E028,E029].

**Transport design rules (WS-7).** Protection halo r₁₀% = 4.2–5.8 mm per deposit (mid case ℓ≈3.6 mm); ring node spacing 8–12 mm; hydrogel mesh ≥5× protein radius (HA 1–2% passes); mRNA redosing ≤7 days; steady state ≈4 days [claim:C029][evidence:E035].

**Humanized in-silico threshold (WS-9).** With humanized clock and seed, the front is contained at θ ≤ 0.333 (κ=2; R 2.83→0.82 mm), monotonically to near-extinction at κ=32 (R 0.70 mm; biomass 2.1× seed). The MV2>MV1 hierarchy emerged unfitted from the ported rates (behavioral validation) [claim:C030][evidence:E036,E012].

**Bayesian estimates (WS-8).** Organoid-gate pass: 36.6% [90% CrI 14.6–60.5]; significant clinical slowing: 5.0% [0.4–13.6] under the historical prior; structured-design band 30–45% reported alongside [claim:C031][evidence:E037].

**Regulatory map.** Every pillar has an approved precedent in a sister proteinopathy (nusinersen; tofersen/NfL [claim:C024][evidence:E023]; tafamidis; PD cell transplant [claim:C033][evidence:E040b, flagged]).

## Discussion

The program's claims are conditional and pre-registered: G0 will measure θ in infected human tissue; the prediction θ<0.33 ⇒ containment was locked in version control before any wet-lab data. Strengths: complete audit trail; two independent quantifications (analytic transport vs simulated kinetics) converging on the same regime; honest dual-lens probability. Limitations are stated in the manuscript and include: mean-field port (stochasticity absent); TSE-calibrated kernel rates (θ adimensional mitigates); κ↔concentration translation unmapped (G0-A6 closes it); only MV1/MV2 anchors available; sparse Bayesian priors; no wet-lab data yet — this preprint exists to pre-register predictions, not to report outcomes.

## Declarations

**Ethics:** no human/animal experimentation performed; the specified future gate (G0) is a protocol document. **Funding:** none declared. **Conflicts:** none declared. **AI use:** AI-assisted literature verification, computation and drafting under the open-science consortium workflow; all citations and numeric claims carry evidence bindings in the accompanying registries; accountable human authors pending consortium attribution.

**Data and code availability:** solvers, ports, parameters, notebooks, knowledge-graph data and audit registers version-controlled in the consortium repository with timestamps preceding any wet-lab data; deterministic analysis scripts; this manuscript is generated by a reproducible build.
