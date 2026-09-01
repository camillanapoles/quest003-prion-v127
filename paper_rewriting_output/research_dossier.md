# Research Dossier — o programa Quest 003 (base local, pro tier)

## Problema central
Doenças priônicas humanas (DCJ): 100% fatais, sem terapia modificadora; 6 candidatos falharam em clínica (quinacrina, doxyciclina, flupirtine, PPS, PRN100, minociclina-retraído). Gargalo: nenhum candidato anterior tinha cálculo quantitativo de entrega-e-dose nem predições pré-registradas.

## A resposta do programa (arco completo, auditado)
Variante PrP-G127V (selecionada pelo kuru; Mead 2009/Asante 2015) → mecanismo dominante-negativo (estrutural: Zheng 2018; trans sem cofator: Geoghegan 2009; anchorless: Gatdula 2026+Zerbes 2026 preprints monitorados) → **etrização computacional** (método nomeado, P0-P6): simulação parametrizada com dados reais publicados → regras de design quantitativas (anel 8-12mm; hidrogel ξ≥5×rp; redose ≤7d) → limiar θ*=0,333 travado v1.0 → estimador θ_obs (Parte 2) → **PARTE 3: invariância multi-espécie sondada** (Cenário B: θ* central 0,333-0,400 entre camundongo/humano/hamster/vole; regra de titulação κ↔Kt; dependência de horizonte documentada; predição hamster honestamente refutada sob def P-024).

## Estado da evidência (o que a tese unificada integra)
- Parte 1 (manuscrito v5 EN+PT, release v3.0): revisão corrigida do registro de citações; transporte; bayes duas-lentes (5% empírica / 30-45% condicional); G0-wet especificado (8 braços, SAP, kill-switch); Tabela Suplementar S1 (10 direcionadores de custo).
- Parte 2 (tese mestra PT, alfa clínica): etrização formalizada; Base de Validade com linhagem; M1-M5; camada pedagógica clínica; Figuras 1-4 auditáveis.
- Registro vivo: 58 claims (hash) · 56 fontes verificadas · 59 N-fatos · canon 44 achados · guardião R0-R3 dois perfis · AST A2-A9 em 3 superfícies (pre-commit/CI/ci_audit).

## Por que agora uma edição unificada publicação-grade
A tese atual é composta (P1 publicável + P2 tese de continuidade); a unificação autocontida exige: narrativa contribuição-primero (PaperSpine V4), validação-por-resultados por seção, auditoria-de-revisor — exatamente os três gates do framework — sobre o material já validado.

## Material M3.1 (dose-band, integrado nesta sessão — PR #6)
Cadeia κ_req→µM→µg/depósito em banda GUM Tipo-B com critérios de aceitação pré-registrados (protocolo garantista U1-U7): banda humana (Kt2/κ=2) = 0,0-2,6 µg V127ΔGPI/depósito; pior caso κ=8 = 0,2-10,3; redose ≤7 d; MW 22,83 kDa das sequências próprias (P04156 res. 23-231); largura ≈53× constante (κ cancela: 14× Kd-proxy [Chen 2010, E057, verificado full-text PMC2924066] × 3,7× V-halo [E030/E010]) — **a largura da banda é o achado até G0-A6**. Registro: claims C058-C060 · N060-N065 · fig5_dose_ladder.

## Fontes locais indexadas (materials_dir=".", curadoria)
Manuscritos: manuscript_EN_v5.md / manuscript_PT_v5.md / manuscript_Parte2_v1.md (tese mestra c/ §4.7 Parte-3) · Registro: evidence_workspace/ (claims.csv, claim_texts.md, source_manifest.json [58], consistency_manifest.json [65]) · JSONs canônicos: ws_9_results/, part2_results/, xspecies/p024_*, m31/m31_u1u2.json · PLAN_DOCS: guardian.md, KNOWLEDGE_CANON.md (F-01..F-44), THESIS_ROADMAP.md, m3_to_m2_validation.md, WRITING_V2_PROTOCOLO.md · Camada clínica: AVALIACAO_ALFA.md, conselho-alfa, G0_UNLOCK_DOSSIER.md, lab_outreach_package.md · Anti-exemplar de citação: ensaio retraído excluído por regra (C024).

## Regras de uso destas fontes (invariantes)
Número só de JSON/registro; claim só com hash+binding; tier em toda saída; predições v1.0 comparadas-jamais-retreinadas; ilustrativo≠evidência; paridade PT=EN de tags; anti-hindsight com release citado; merge só via PR com CI.
