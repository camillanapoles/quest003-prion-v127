# Source Map — quem autoriza o quê (mapeamento de autoridade dos materiais)

| Material | Papel na edição unificada | Autoridade |
|---|---|---|
| paper/manuscript_EN_v5.md + PT | Parte 1 (design terapêutico) | gated; release v3.0; claims C001-C051 |
| paper/manuscript_Parte2_v1.md | Tese mestra (P2 + alfa clínica + PARTE 3 §4.7) | gated (part2); claims C052-C057 |
| paper/evidence_workspace/{claims.csv,source_manifest.json,consistency_manifest.json} | registro probatório único | validadores 0/0; 58/56/59 |
| KNOWLEDGE_CANON.md | índice-mestre de achados F-01..F-44 | PLAN_DOC (não migra sem gate) |
| experiments/{ws_9_results,xspecies,part2_results}/*.json | fonte de todo número [SIM] | número só de JSON |
| paper/guardian/{SKILL_SCOUT_S3,P023,P025,COMPUTE_EVAL,S3_DATA_AUDIT,THETA_STAR_EXPLAINED,CONSELHO,AVALIACAO,WRITING_V2_PROTOCOLO}.md | dossiês de método/avaliação | PLAN_DOCS |
| literature/{evidence_table,refs_audit,search_log}.md | revisão + auditoria de citações | E-registry vinculado |
| paper/{e200k_br_dossier,positioning_whitepaper,lab_outreach_package,G0_UNLOCK_DOSSIER}.md | dossiês translacionais | PLAN_DOCS |
| Repositório git + CI (gates/ABNT/PDF) | replicabilidade | runs públicas |

**Regra de autoridade (régua da casa):** resultado→JSON; número→registro E; claim→hash; manuscrito→gate. Materiais externos (JHU/Harvard/ABNT) ensinam ESTRUTURA apenas.
