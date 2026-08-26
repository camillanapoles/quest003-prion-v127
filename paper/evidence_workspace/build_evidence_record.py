#!/usr/bin/env python3
"""Popula claims.csv + consistency_manifest.json do evidence workspace (skill scientific-writing).
Cada claim: texto normalizado → SHA-256; binding às fontes E-IDs verificadas em source_manifest.json."""
import csv, hashlib, json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))

def norm(t):
    t = t.lower().strip()
    t = re.sub(r'[^a-z0-9.%×±\-\s]', '', t)
    return re.sub(r'\s+', ' ', t)

def sha(t):
    return hashlib.sha256(norm(t).encode()).hexdigest()

# (id, seção, tipo, texto, evidências, status, incerteza)
CLAIMS = [
 ("C001","2.1/3.1","factual","V127 homozygous transgenic mice are completely resistant to all tested prion strains, as protective as gene deletion",["E001"],"verified_by_opening","none_reported"),
 ("C002","2.1/3.1","factual","Heterozygous G/V127 mice resist kuru and classical CJD prions but remain infectable by vCJD prions",["E001"],"verified_by_opening","none_reported"),
 ("C003","2.1/3.1","factual","V127 acts as a potent dose-dependent dominant-negative inhibitor of wild-type prion propagation",["E001","E003","E005"],"verified_by_opening","none_reported"),
 ("C004","1","factual","G127V was under positive selection during the kuru epidemic; heterozygote carriers were protected",["E002"],"verified_by_opening","none_reported"),
 ("C005","1/3.1","factual","Recombinant anchorless V127 retains potent dominant-negative activity in trans in cell culture",["E003"],"verified_by_opening","none_reported"),
 ("C006","1/3.1","factual","Prion resistance in cell culture persists after transgene expression ceases",["E003"],"verified_by_opening","none_reported"),
 ("C007","1/3.1","factual","Systemic AAV delivery of anchorless V127GPI extended survival approximately 50 days in a rodent prion model",["E004"],"verified_by_opening","effect_size_single_study"),
 ("C008","2.1","factual","V127 restricts the pre-beta-sheet backbone and stabilizes dimers via intermolecular hydrogen bonds; alters beta2-alpha2 loop dynamics",["E005","E006"],"verified_by_opening","none_reported"),
 ("C009","2.4","factual","Human cerebral organoids are susceptible to sCJD infection with subtype-dependent kinetics",["E007"],"verified_by_opening","none_reported"),
 ("C010","2.4","factual","Organoid infection anchors: inoculum cleared by 25-28 dpi, de-novo seeding activity from 35 dpi",["E007"],"verified_by_opening","single_lab"),
 ("C011","2.4","factual","Endpoint titers at 169 dpi: MV2 = 2.13(+/-1.63)e5 and MV1 = 1.69(+/-0.70)e3 SD50 per mg; protease-resistant PrP detected only in MV2",["E007"],"verified_by_opening","single_lab"),
 ("C012","2.1/3.1","factual","Pentosan polysulfate delays prion propagation in infected organoids in prophylactic-like and therapeutic-like paradigms (published positive control)",["E008"],"verified_by_opening","none_reported"),
 ("C013","2.4","factual","The prion-spreading kernel is a published stochastic reaction-diffusion model with open code (Gillespie over aggregate classes with UPR-gated templating)",["E009"],"verified_by_opening","none_reported"),
 ("C014","2.2","factual","In vivo brain extracellular space: volume fraction approximately 0.20 and tortuosity approximately 1.8 for macromolecules",["E010"],"verified_by_opening","parameter_ranges_reported"),
 ("C015","2.2","methodological","First-order consumption swept 1e-6 to 1e-5 per second anchored to nucleated-polymerization kinetics",["E011"],"verified_by_opening","parametric_sweep"),
 ("C016","3.1","factual","NPC seeding restores electrophysiological parameters of sCJD-infected organoids toward uninfected levels",["E012"],"verified_by_opening","single_study"),
 ("C017","3.1","factual","Endogenous adult neural stem cells accumulate and replicate prions; neuronal fate is altered by infection",["E013"],"verified_by_opening","none_reported"),
 ("C018","3.1","factual","NSCs do not generate microglia; microglia derive from yolk-sac macrophage lineage",["E014"],"verified_by_opening","dogma"),
 ("C019","3.1","factual","Adult human SVZ neurogenesis is minimal; the niche is largely quiescent",["E015"],"verified_by_opening","debated_then_resolved"),
 ("C020","3.1","factual","iPSC-derived microglia-like cells are generated in approximately five weeks by a defined protocol",["E016"],"verified_by_opening","none_reported"),
 ("C021","3.1","factual","HLA-KO hypoimmunogenic pluripotent cells evade rejection; CD47 is necessary and sufficient against NK-mediated rejection with long-term allogeneic survival",["E017","E018"],"verified_by_opening","preclinical"),
 ("C022","2.2/3.1","factual","A single intrathecal dose of brain-targeting LNP mRNA expresses in 29.6 percent of neurons and 38.1 percent of astrocytes in rodents",["E019"],"verified_by_opening","rodent"),
 ("C023","2.2/3.1","factual","Hyaluronic-acid hydrogel scaffolding increases survival of engrafted neural stem cells",["E020"],"verified_by_opening","preclinical"),
 ("C024","methods","factual","A 2017 Neurotherapeutics minocycline/FK506 prion trial was retracted in 2020 and is excluded by rule",["E021"],"verified_by_opening","none_reported"),
 ("C025","methods","factual","Minocycline reduces neuroinflammation without survival benefit in prion-infected mice",["E022"],"verified_by_opening","none_reported"),
 ("C026","methods","factual","Minocycline confounds neurofilament-light chain biomarker interpretation (3.5x plasma, 5.7x CSF increase)",["E023"],"verified_by_opening","n=1_signal"),
 ("C027","1.1","factual","Brazilian E200K kindreds have been documented since 2007",["E024"],"verified_by_opening","none_reported"),
 ("C028","4.2","factual","Alzheimer and Parkinson proteins spread by templated misfolding along stereotyped routes (prion-like propagation)",["E025","E026"],"verified_by_opening","model_based"),
 ("C029","4.3","factual","Tofersen received accelerated approval for SOD1-ALS with a biomarker (NfL) endpoint in 2023",["E027"],"verified_by_opening","none_reported"),
 ("C030","4.3","factual","Nusinersen established chronic intrathecal ASO redosing safety since 2016",["E028"],"verified_by_opening","none_reported"),
 ("C031","4.3","factual","Dopaminergic progenitor cell transplantation in Parkinson patients proved feasible in a 2026 trial",["E029"],"verified_by_opening","phase1"),
 ("C032","2.2","result","WS-7 self-tests pass: mass conservation 100.0 percent; numeric vs analytic Thiele length error 0.5 percent",["E030"],"verified_by_execution","deterministic_checks"),
 ("C033","3.2","result","Design rule 1: containment-ring node spacing 8-12 mm (protection radius 4-6 mm per deposit)",["E030"],"verified_by_execution","parametric_range"),
 ("C034","3.2","result","Design rule 2: hydrogel mesh must exceed 5x protein radius; HA 1-2 percent passes, above 5 percent sequesters the secretome",["E030","E020"],"verified_by_execution","model_based"),
 ("C035","3.2","result","Design rule 3: LNP-mRNA redosing interval of 7 days or less keeps inter-pulse trough at 56 percent of peak; 10-14 days leaves valleys",["E030","E019"],"verified_by_execution","model_based"),
 ("C036","3.3","result","Bayesian frame: P(G0 go) = 36.6 percent with 90 percent credible interval 14.6 to 60.5; P(clinical slowing) = 5.0 percent [0.4-13.6] empirical vs 30-45 percent design-conditional",["E031"],"verified_by_execution","structured_judgment_weights"),
 ("C037","2.4","result","Humanization: 1 simulation unit = 144 days; derived human doubling time 12.1 days from organoid anchors",["E032","E007"],"verified_by_execution","detection_floor_assumed"),
 ("C038","3.4","result","Containment threshold theta-star = 0.333: front contained at kappa=2 (2.83 to 0.82 mm), monotone to near-extinction at kappa=32 (0.70 mm, biomass ratio 2.1x seed)",["E032"],"verified_by_execution","in_silico_prediction"),
 ("C039","3.4","result","Emergent consistency: seeding by the published 126x titer ratio reproduces the MV2-greater-than-MV1 hierarchy without fitting",["E032","E007"],"verified_by_execution","qualitative_n2"),
 ("C040","2.5","factual","All program predictions were committed to the public repository with timestamps before any wet-lab experiment exists",["E033"],"verified_by_opening","auditable"),
 ("C041","methods","factual","External document references were audited individually: of 19 audited, 11 correct, 3 duplicates, 1 non-scientific, 1 wrong link",["E033"],"verified_by_opening","batch"),
 ("C042","3.2","result","Steady-state establishment takes approximately 4 days; planned readouts operate in steady state",["E030"],"verified_by_execution","model_based"),
 ("C043","2.4","methodological","Humanization is a global time rescaling; relative rates remain murine pending fits to published series",["E032","E009"],"verified_by_construction","declared_limitation"),
]

rows=[]
for cid,sec,kind,text,evs,status,unc in CLAIMS:
    rows.append({"claim_id":cid,"section":sec,"claim_kind":kind,
                 "claim_text_sha256":sha(text),
                 "evidence_ids":";".join(evs),
                 "verification_status":status,
                 "uncertainty":unc,
                 "analysis_intent":"confirmatory" if kind=="factual" else "exploratory"})

# reclamar texto claro para auditoria (arquivo irmão não-exigido pela skill mas útil)
with open(os.path.join(HERE,"claim_texts.md"),"w") as f:
    f.write("# Claim texts (normalized hashes in claims.csv)\n\n")
    for cid,sec,kind,text,evs,_,_ in CLAIMS:
        f.write(f"- **{cid}** ({sec},{kind}) [{';'.join(evs)}]: {text}\n")

with open(os.path.join(HERE,"claims.csv"),"w",newline="") as f:
    w=csv.DictWriter(f,fieldnames=["claim_id","section","claim_kind","claim_text_sha256","evidence_ids","verification_status","uncertainty","analysis_intent"])
    w.writeheader(); w.writerows(rows)

# ================= consistency manifest =================
manifest={
 "document_id":"quest003-preprint",
 "provenance_note":"All numeric facts below were extracted from the same sources/runs as the claims; units reconciled; every fact carries its evidence ID. Own-execution numbers (E030-E032) are reproducible from in-repo scripts and archived outputs.",
 "numeric_facts":[
  {"id":"N001","value":"0.20","unit":"dimensionless","what":"ECS volume fraction","evidence":"E010","reconciled_with":["M001"]},
  {"id":"N002","value":"1.8","unit":"dimensionless","what":"tortuosity (macromolecule)","evidence":"E010","reconciled_with":["M001"]},
  {"id":"N003","value":"1.25e-10","unit":"m2/s","what":"free diffusivity D0 (~30kDa, R_h 2.5nm)","evidence":"E030","reconciled_with":["M001"]},
  {"id":"N004","value":"3.86e-11","unit":"m2/s","what":"effective diffusivity D_eff","evidence":"E030","reconciled_with":["M001","M002"]},
  {"id":"N005","value":"1e-6 - 1e-5","unit":"s-1","what":"k_eff sweep","evidence":"E011","reconciled_with":["M001"]},
  {"id":"N006","value":"100.0","unit":"percent","what":"WS-7 mass conservation self-test","evidence":"E030","reconciled_with":["O001"]},
  {"id":"N007","value":"0.5","unit":"percent","what":"Thiele length numeric-vs-analytic error","evidence":"E030","reconciled_with":["O001"]},
  {"id":"N008","value":"4-6","unit":"mm","what":"protection radius r10% per deposit","evidence":"E030","reconciled_with":["R001"]},
  {"id":"N009","value":"8-12","unit":"mm","what":"ring node spacing (Rule 1)","evidence":"E030","reconciled_with":["R001"]},
  {"id":"N010","value":">=5","unit":"ratio xi/r_p","what":"hydrogel mesh rule (Rule 2)","evidence":"E030","reconciled_with":["R001"]},
  {"id":"N011","value":"<=7","unit":"days","what":"mRNA redosing (Rule 3); trough 56% peak","evidence":"E030","reconciled_with":["R001"]},
  {"id":"N012","value":"2.13e5 / 1.69e3","unit":"SD50/mg","what":"MV2/MV1 endpoint titers 169dpi","evidence":"E007","reconciled_with":["M003","R003"]},
  {"id":"N013","value":"126","unit":"ratio","what":"MV2:MV1 titer ratio","evidence":"E007","reconciled_with":["M003"]},
  {"id":"N014","value":"12.1","unit":"days","what":"derived human doubling time","evidence":"E032","reconciled_with":["M003"]},
  {"id":"N015","value":"144","unit":"days per sim unit","what":"humanized clock scale","evidence":"E032","reconciled_with":["M003","R003"]},
  {"id":"N016","value":"0.333","unit":"dimensionless","what":"containment threshold theta*","evidence":"E032","reconciled_with":["R003"]},
  {"id":"N017","value":"2.83 -> 0.82","unit":"mm","what":"front radius baseline -> kappa2","evidence":"E032","reconciled_with":["R003"]},
  {"id":"N018","value":"36.6 [14.6-60.5]","unit":"percent (90% CrI)","what":"P(G0 go)","evidence":"E031","reconciled_with":["R002"]},
  {"id":"N019","value":"5.0 [0.4-13.6]","unit":"percent (90% CrI)","what":"P(clinical slowing) empirical prior","evidence":"E031","reconciled_with":["R002"]},
  {"id":"N020","value":"30-45","unit":"percent","what":"P(slowing) design-conditional (labeled lens)","evidence":"E031","reconciled_with":["R002"]},
  {"id":"N021","value":"29.6 / 38.1","unit":"percent","what":"LNP-mRNA transduction neurons/astrocytes","evidence":"E019","reconciled_with":["M004"]},
  {"id":"N022","value":"~50","unit":"days","what":"AAV anchorless V127 survival extension (rodent)","evidence":"E004","reconciled_with":["M004"]},
  {"id":"N023","value":"0.1-1","unit":"uM (order of magnitude)","what":"estimated deposit peak V127dGPI (kappa 2-4 analog)","evidence":"E030","reconciled_with":["R001"],"uncertainty":"order_of_magnitude_only"}
 ],
 "methods":[
  {"method_id":"M001","name":"ADR transport solver (finite volumes, self-tested)","analysis_intent":"exploratory_design","protocol_status":"prespecified_in_repo","outcome_ids":["O001","R001"],"reproducible":"experiments/ws_7_solver.py"},
  {"method_id":"M002","name":"Wave-vs-shield r*(theta) + mRNA pulse-train","analysis_intent":"exploratory_design","protocol_status":"prespecified_in_repo","outcome_ids":["R001"],"reproducible":"experiments/ws_7_v2_wave.py"},
  {"method_id":"M003","name":"Humanized kernel port (Igel/Fornara) with logistic saturation + substrate-competition capping; clock calibrated to Groveman anchors","analysis_intent":"exploratory_prediction","protocol_status":"prespecified_in_repo","outcome_ids":["R003"],"reproducible":"paper/../experiments (colab runs; JSON archived)"},
  {"method_id":"M004","name":"Hierarchical Bayesian calibration over 10 analogues (Monte-Carlo 200k)","analysis_intent":"exploratory_probability","protocol_status":"prespecified_in_repo","outcome_ids":["R002"],"reproducible":"experiments/bayes_results/"}
 ],
 "outcomes":[
  {"outcome_id":"O001","what":"self-tests mass/Thiele","status":"passed","captured":"experiments/ws_7_results/ws_7_results.json"}
 ],
 "results":[
  {"result_id":"R001","what":"three transport design rules","status":"derived","claims":["C033","C034","C035","C042"]},
  {"result_id":"R002","what":"dual-lens probabilities","status":"computed","claims":["C036"]},
  {"result_id":"R003","what":"theta*=0.333 + emergent hierarchy","status":"in_silico_prediction_pre_registered","claims":["C037","C038","C039"]}
 ]
}
with open(os.path.join(HERE,"consistency_manifest.json"),"w") as f:
    json.dump(manifest,f,indent=1,ensure_ascii=False)

print(f"claims.csv: {len(rows)} claims (C001-C{len(rows):03d}) com SHA-256 normalizado")
print(f"claim_texts.md: textos claros para auditoria humana")
print(f"consistency_manifest.json: {len(manifest['numeric_facts'])} numeric facts · {len(manifest['methods'])} methods · {len(manifest['results'])} results")
# validação de binding bidirecional
src=json.load(open(os.path.join(HERE,"source_manifest.json")))
declared={c for s in src["sources"] for c in s.get("supports",[])}
written={r["claim_id"] for r in rows}
print("binding bidirecional:", "OK — conjuntos idênticos" if declared==written else f"DIVERGÊNCIA: só-no-manifesto={declared-written} só-no-csv={written-declared}")
