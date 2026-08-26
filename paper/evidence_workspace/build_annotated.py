#!/usr/bin/env python3
"""Gera manuscript_annotated.md: o manuscrito EN v4 com marcadores inline [claim:CXXX]/[evidence:EXXX]
nos pontos corretos — a versão de auditoria conforme o workflow da skill (passo 5: 'preserve all IDs')."""
import re, os, csv
HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.join(HERE, "..", "manuscript_EN_v4.md")
src = open(BASE).read()

# âncoras: (trecho único do texto, marcador a inserir logo APÓS o ponto final do trecho)
ANCHORS = [
 ("complete resistance when homozygous in transgenic mice — \"as protective as gene deletion\" — while acting as a potent dose-dependent dominant-negative inhibitor of wild-type propagation", "[claim:C001][claim:C002][claim:C003]"),
 ("protected heterozygous carriers", "[claim:C004]"),
 ("recombinant, GPI-anchorless V127 retains potent dominant-negative activity in trans in vitro", "[claim:C005][claim:C006]"),
 ("systemic AAV delivery of anchorless V127 extends survival ~50 days in a rodent prion model", "[claim:C007]"),
 ("structural basis (β2–α2 loop restriction, intermolecular H-bond dimer stabilization)", "[claim:C008]"),
 ("inoculum clearance 25–28 dpi, de-novo production from 35 dpi, endpoint titers (169 dpi) MV2 = 2.13(±1.63)×10⁵ vs MV1 = 1.69(±0.70)×10³ SD50/mg; protease-resistant PrP only in MV2", "[claim:C010][claim:C011][evidence:E007]"),
 ("pentosan polysulfate as published positive control", "[claim:C012]"),
 ("α = 0.20 and tortuosity λ = 1.8 from in-vivo integrative optical imaging", "[claim:C014][evidence:E010]"),
 ("first-order consumption k_eff swept 10⁻⁶–10⁻⁵ s⁻¹ anchored to nucleated polymerization", "[claim:C015]"),
 ("NPC seeding restores electrophysiological parameters toward uninfected levels", "[claim:C016]"),
 ("quiescent prion-replicating SVZ", "[claim:C017][claim:C019]"),
 ("NSC-to-microglia lineage impossibility", "[claim:C018]"),
 ("iPSC-microglia co-graft", "[claim:C020]"),
 ("chronic intrathecal redosing (nusinersen)", "[claim:C030]"),
 ("accelerated approval via biomarker in lethal genetic neurodegeneration (tofersen; NfL endpoint)", "[claim:C029]"),
 ("human brain cell grafts (2026 Parkinson trial)", "[claim:C031]"),
 ("mass conservation 100.0%; numeric vs analytic Thiele length error 0.5%", "[claim:C032]"),
 ("containment-ring spacing 8–12 mm", "[claim:C033]"),
 ("hydrogel mesh ξ≥5× protein radius", "[claim:C034]"),
 ("mRNA redosing ≤7 days", "[claim:C035]"),
 ("P(G0 informative-go)", "[claim:C036]"),
 ("1 simulation unit = 144 days", "[claim:C037]"),
 ("containment threshold θ* = 0.333", "[claim:C038]"),
 ("reproduces, without fitting, the MV2>MV1 subtype hierarchy", "[claim:C039]"),
 ("All predictions were committed to the public repository with timestamps before any wet-lab experiment exists", "[claim:C040]"),
 ("19 audited in one batch: 11 correct, 3 duplicates, 1 non-scientific, 1 wrong link", "[claim:C041]"),
 ("steady-state ~4 days", "[claim:C042]"),
 ("humanization is a global time rescaling; relative rates remain murine", "[claim:C043]"),
 ("Brazilian E200K kindreds have been reported since 2007", "[claim:C027]"),
 ("prion-like spreading", "[claim:C028]"),
 ("retracted Neurotherapeutics trial (minocycline/FK506; retraction 2020) was found still circulating as supportive evidence and is excluded by rule", "[claim:C024][evidence:E021]"),
 ("minocycline is additionally documented to confound the NfL biomarker endpoint", "[claim:C026]"),
 ("a retracted trial excluded", "[claim:C025]"),
]

n=0
for frag, marker in ANCHORS:
    # tolerância a travessão/aspas variando entre versões
    pat = re.escape(frag)
    m = re.search(pat, src)
    if not m:
        # fallback: primeiros 40 chars do fragmento
        m = re.search(re.escape(frag[:40]), src)
    if m:
        pos = m.end()
        src = src[:pos] + " " + marker + src[pos:]
        n+=1
    else:
        print("ÂNCORA NÃO ENCONTRADA:", frag[:50])

open(os.path.join(HERE,"manuscript_annotated.md"),"w").write(src)
print(f"manuscript_annotated.md: {n}/{len(ANCHORS)} âncoras inseridas")
