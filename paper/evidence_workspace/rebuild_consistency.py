#!/usr/bin/env python3
"""Reescreve consistency_manifest.json no SCHEMA CANÔNICO da skill (fact_id/concept/section/value/unit/numerator/denominator/sample_size/analysis_set/evidence_ids; methods; results com method_id/outcome_id)."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))

F = [
 ("N001","ecs_volume_fraction","2.2","0.20","dimensionless",["E010"]),
 ("N002","tortuosity_macromolecule","2.2","1.8","dimensionless",["E010"]),
 ("N003","free_diffusivity_D0","2.2","1.25e-10","m2/s",["E030"]),
 ("N004","effective_diffusivity","2.2","3.86e-11","m2/s",["E030"]),
 ("N005","k_eff_sweep","2.2","1e-6 to 1e-5","s-1",["E011"]),
 ("N006","ws7_mass_conservation","3.2",100.0,"percent",["E030"]),
 ("N007","ws7_thiele_error","3.2",0.5,"percent",["E030"]),
 ("N008","protection_radius","3.2","4 to 6","mm",["E030"]),
 ("N009","ring_spacing_rule1","3.2","8 to 12","mm",["E030"]),
 ("N010","hydrogel_mesh_rule2","3.2",5,"ratio minimum",["E030"]),
 ("N011","mrna_redose_rule3","3.2",7,"days maximum",["E030"]),
 ("N012","mv2_titer_169dpi","2.4","2.13e5","SD50/mg",["E007"]),
 ("N013","mv1_titer_169dpi","2.4","1.69e3","SD50/mg",["E007"]),
 ("N014","human_doubling_time","2.4",12.1,"days",["E032"]),
 ("N015","sim_unit_days","2.4",144,"days",["E032"]),
 ("N016","containment_threshold","3.4",0.333,"dimensionless",["E032"]),
 ("N017","front_kappa2","3.4",0.82,"mm",["E032"]),
 ("N018","p_g0_go","3.3",36.6,"percent",["E031"]),
 ("N019","p_slowing_empirical","3.3",5.0,"percent",["E031"]),
 ("N020","p_slowing_conditional","3.3","30 to 45","percent",["E031"]),
 ("N021","lnp_transduction_neurons","2.2",29.6,"percent",["E019"]),
 ("N022","aav_survival_extension","1",50,"days approx",["E004"]),
 ("N023","mv2_mv1_titer_ratio","2.4",126,"ratio",["E007"]),
]

cm = {
 "schema_version": "1.0",
 "numeric_facts": [
   {"fact_id": fid, "concept": con, "section": sec, "value": val, "unit": unit,
    "numerator": None, "denominator": None, "sample_size": None,
    "analysis_set": "program-level", "evidence_ids": evs}
   for fid, con, sec, val, unit, evs in F
 ],
 "methods": [
   {"method_id": "M001", "name": "ADR transport solver finite volumes self-tested", "analysis_intent": "exploratory", "protocol_status": "prespecified", "outcome_ids": ["O001"]},
   {"method_id": "M002", "name": "wave-vs-shield radius and mRNA pulse-train", "analysis_intent": "exploratory", "protocol_status": "prespecified", "outcome_ids": ["O001"]},
   {"method_id": "M003", "name": "humanized kernel port with logistic saturation and substrate-competition capping", "analysis_intent": "exploratory", "protocol_status": "prespecified", "outcome_ids": ["O002", "O003"]},
   {"method_id": "M004", "name": "hierarchical Bayesian calibration over ten analogues", "analysis_intent": "exploratory", "protocol_status": "prespecified", "outcome_ids": ["O004"]}
 ],
 "results": [
   {"result_id": "R001", "method_id": "M001", "outcome_id": "O001", "analysis_intent": "exploratory", "sample_size": None, "evidence_ids": ["E030"], "reported_sections": ["3.2"]},
   {"result_id": "R002", "method_id": "M004", "outcome_id": "O004", "analysis_intent": "exploratory", "sample_size": None, "evidence_ids": ["E031"], "reported_sections": ["3.3"]},
   {"result_id": "R003", "method_id": "M003", "outcome_id": "O002", "analysis_intent": "exploratory", "sample_size": None, "evidence_ids": ["E032"], "reported_sections": ["3.4"]},
   {"result_id": "R004", "method_id": "M003", "outcome_id": "O003", "analysis_intent": "exploratory", "sample_size": None, "evidence_ids": ["E032", "E007"], "reported_sections": ["3.4"]}
 ]
}
with open(os.path.join(HERE, "consistency_manifest.json"), "w") as f:
    json.dump(cm, f, indent=1, ensure_ascii=False)
print("consistency canônico:", len(cm["numeric_facts"]), "facts ·", len(cm["methods"]), "methods ·", len(cm["results"]), "results")
