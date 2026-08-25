# Graph Report - quest003-graph  (2026-08-25)

## Corpus Check
- cluster-only mode — file stats not available

## Summary
- 33 nodes · 35 edges · 8 communities (6 shown, 2 thin omitted)
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [🌕 POSSÍVEL] Anel de contenção ('bombeiros') nas bordas sadias
- ASO anti-PRNP: +61-98% de sobrevida (camundongo)
- [🌕 POSSÍVEL] Programa em gates G0→G4 com kill-switches pré-registrados
- [🌕 POSSÍVEL] Rota pelo 'caminho danificado' (DTI + neuronavegação)
- [VÁLIDO] Janela da DCJ esporádica incompatível com produção celular
- [🌕 POSSÍVEL] NSC SECRETORA de V127ΔGPI — biofábrica local via CED
- [VÁLIDO] Seleção positiva G127V na epidemia de kuru (PNG)
- [🌕 POSSÍVEL] Rota regulatória: CEP → CONEP → Anvisa (ATMP)

## God Nodes (most connected - your core abstractions)

## Surprising Connections (you probably didn't know these)
- `[VÁLIDO] DN 'em trans' por PrP-V127 SEM âncora GPI (anchorless)` --supports--> `[🌕 POSSÍVEL] NSC SECRETORA de V127ΔGPI — biofábrica local via CED`  [EXTRACTED]
  quests/003 → quests/003  _Bridges community 0 → community 5_
- `[🌕 POSSÍVEL] ION717 (ASO) em first-in-human desde 2023` --constrains--> `[🌕 POSSÍVEL] Programa em gates G0→G4 com kill-switches pré-registrados`  [EXTRACTED]
  quests/003 → quests/003  _Bridges community 1 → community 2_
- `[🌕 POSSÍVEL] NSC SECRETORA de V127ΔGPI — biofábrica local via CED` --supports--> `[🌕 POSSÍVEL] Programa em gates G0→G4 com kill-switches pré-registrados`  [EXTRACTED]
  quests/003 → quests/003  _Bridges community 5 → community 2_
- `[🌕 POSSÍVEL] NSC SECRETORA de V127ΔGPI — biofábrica local via CED` --constrains--> `[🌑 BAIXA] Sobrevida do enxerto ≥ necessário em cérebro DCJ ativo`  [EXTRACTED]
  quests/003 → quests/003  _Bridges community 5 → community 4_
- `[🌕 POSSÍVEL] Rota pelo 'caminho danificado' (DTI + neuronavegação)` --enables--> `[🌕 POSSÍVEL] Anel de contenção ('bombeiros') nas bordas sadias`  [EXTRACTED]
  quests/003 → quests/003  _Bridges community 3 → community 0_

## Communities (8 total, 2 thin omitted)

### Community 0 - "[🌕 POSSÍVEL] Anel de contenção ('bombeiros') nas bordas sadias"
Cohesion: 0.33
Nodes (6): [VÁLIDO] CED: cânula step-design anti-refluxo validada, [🌑 BAIXA] Contenção COMPLETA em doença já estabelecida, [VÁLIDO] Dominante-negativo dose-dependente (cis, mesma célula), [🌕 POSSÍVEL] Anel de contenção ('bombeiros') nas bordas sadias, [VÁLIDO] Base estrutural V127: restrição conformacional + dímeros estáveis, [VÁLIDO] DN 'em trans' por PrP-V127 SEM âncora GPI (anchorless)

### Community 1 - "ASO anti-PRNP: +61-98% de sobrevida (camundongo)"
Cohesion: 0.67
Nodes (3): [VÁLIDO] ASO anti-PRNP: +61-98% de sobrevida (camundongo), [VÁLIDO] Depleção de PrP reverte espongiose e cognição precoces, [🌕 POSSÍVEL] ION717 (ASO) em first-in-human desde 2023

### Community 2 - "[🌕 POSSÍVEL] Programa em gates G0→G4 com kill-switches pré-registrados"
Cohesion: 0.22
Nodes (10): [VÁLIDO] E200K no Brasil (Smid 2007) — população-alvo pré-sintomática, [VÁLIDO] NPCs restauram eletrofisiologia mesmo com príon ativo, [VÁLIDO] Reparo neurogênico endógeno ativa-se e protege (camundongo), [🌕 POSSÍVEL] Programa em gates G0→G4 com kill-switches pré-registrados, [🌕 POSSÍVEL] Co-enxerto iMG: micróglia de iPSC como coadjuvante fagocítico, [INVÁLIDO] NSC gera micróglia de vigilância, [VÁLIDO] PRN100 anti-PrP: seguro, sem eficácia clínica clara, [VÁLIDO] RT-QuIC: diagnóstico antemortem precoce validado (+2 more)

### Community 3 - "[🌕 POSSÍVEL] Rota pelo 'caminho danificado' (DTI + neuronavegação)"
Cohesion: 0.67
Nodes (3): [🌕 POSSÍVEL] Cânula coaxial de uso único (anti-semeadura priônica), [🌕 POSSÍVEL] Rota pelo 'caminho danificado' (DTI + neuronavegação), [🌑 BAIXA] Regeneração funcional de território espongiforme morto

### Community 4 - "[VÁLIDO] Janela da DCJ esporádica incompatível com produção celular"
Cohesion: 0.40
Nodes (5): [🌕 POSSÍVEL] CRISPR: knock-in V127 bialélico + silêncio do alelo selvagem, [🌑 BAIXA] Sobrevida do enxerto ≥ necessário em cérebro DCJ ativo, [VÁLIDO] Heterozigoto G/V127: infectável por vCJD, [VÁLIDO] V127/V127 bialélico: resistência completa a todas as cepas, [VÁLIDO] Janela da DCJ esporádica incompatível com produção celular

### Community 5 - "[🌕 POSSÍVEL] NSC SECRETORA de V127ΔGPI — biofábrica local via CED"
Cohesion: 0.50
Nodes (4): [VÁLIDO] PoC in vivo: AAV-sc V127ΔGPI sistêmico → +~50 dias (roedor), [VÁLIDO] Organoide sCJD humano = plataforma de teste (90 d), [VÁLIDO] Resistência persiste após cessar a expressão do transgene, [🌕 POSSÍVEL] NSC SECRETORA de V127ΔGPI — biofábrica local via CED

## Knowledge Gaps
- **2 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Not enough signal to generate questions. This usually means the corpus has no AMBIGUOUS edges, no bridge nodes, no INFERRED relationships, and all communities are tightly cohesive. Add more files or run with --mode deep to extract richer edges._