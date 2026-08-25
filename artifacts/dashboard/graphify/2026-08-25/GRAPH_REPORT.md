# Graph Report - quest003-graph  (2026-08-25)

## Corpus Check
- cluster-only mode — file stats not available

## Summary
- 29 nodes · 26 edges · 8 communities (5 shown, 3 thin omitted)
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- CRISPR: knock-in V127 bialélico + silêncio do alelo selvagem
- ASO anti-PRNP: +61-98% de sobrevida (camundongo)
- NSC SECRETORA de V127ΔGPI — biofábrica local via CED
- DN 'em trans' por PrP-V127 SEM âncora GPI (anchorless)
- Programa em gates G0→G4 com kill-switches pré-registrados
- Seleção positiva G127V na epidemia de kuru (PNG)
- NSC gera micróglia de vigilância
- Rota regulatória: CEP → CONEP → Anvisa (ATMP)

## God Nodes (most connected - your core abstractions)

## Surprising Connections (you probably didn't know these)
- `DN 'em trans' por PrP-V127 SEM âncora GPI (anchorless)` --supports--> `NSC SECRETORA de V127ΔGPI — biofábrica local via CED`  [EXTRACTED]
  quests/003 → quests/003  _Bridges community 3 → community 2_
- `ION717 (ASO) em first-in-human desde 2023` --constrains--> `Programa em gates G0→G4 com kill-switches pré-registrados`  [EXTRACTED]
  quests/003 → quests/003  _Bridges community 1 → community 4_
- `NSC SECRETORA de V127ΔGPI — biofábrica local via CED` --supports--> `Programa em gates G0→G4 com kill-switches pré-registrados`  [EXTRACTED]
  quests/003 → quests/003  _Bridges community 2 → community 4_
- `Janela da DCJ esporádica incompatível com produção celular` --enables--> `E200K no Brasil (Smid 2007) — população-alvo pré-sintomática`  [EXTRACTED]
  quests/003 → quests/003  _Bridges community 0 → community 4_

## Communities (8 total, 3 thin omitted)

### Community 0 - "CRISPR: knock-in V127 bialélico + silêncio do alelo selvagem"
Cohesion: 0.50
Nodes (4): CRISPR: knock-in V127 bialélico + silêncio do alelo selvagem, Heterozigoto G/V127: infectável por vCJD, V127/V127 bialélico: resistência completa a todas as cepas, Janela da DCJ esporádica incompatível com produção celular

### Community 1 - "ASO anti-PRNP: +61-98% de sobrevida (camundongo)"
Cohesion: 0.67
Nodes (3): ASO anti-PRNP: +61-98% de sobrevida (camundongo), Depleção de PrP reverte espongiose e cognição precoces, ION717 (ASO) em first-in-human desde 2023

### Community 2 - "NSC SECRETORA de V127ΔGPI — biofábrica local via CED"
Cohesion: 0.29
Nodes (7): PoC in vivo: AAV-sc V127ΔGPI sistêmico → +~50 dias (roedor), NPCs restauram eletrofisiologia mesmo com príon ativo, Reparo neurogênico endógeno ativa-se e protege (camundongo), Organoide sCJD humano = plataforma de teste (90 d), Resistência persiste após cessar a expressão do transgene, NSC SECRETORA de V127ΔGPI — biofábrica local via CED, Nicho SVZ como fábrica autossustentável humana

### Community 3 - "DN 'em trans' por PrP-V127 SEM âncora GPI (anchorless)"
Cohesion: 0.29
Nodes (7): CED: cânula step-design anti-refluxo validada, Cânula coaxial de uso único (anti-semeadura priônica), Dominante-negativo dose-dependente (cis, mesma célula), Rota pelo 'caminho danificado' (DTI + neuronavegação), Anel de contenção ('bombeiros') nas bordas sadias, Base estrutural V127: restrição conformacional + dímeros estáveis, DN 'em trans' por PrP-V127 SEM âncora GPI (anchorless)

### Community 4 - "Programa em gates G0→G4 com kill-switches pré-registrados"
Cohesion: 0.40
Nodes (5): E200K no Brasil (Smid 2007) — população-alvo pré-sintomática, Programa em gates G0→G4 com kill-switches pré-registrados, PRN100 anti-PrP: seguro, sem eficácia clínica clara, RT-QuIC: diagnóstico antemortem precoce validado, RT-QuIC intraoperatório para calibrar margens

## Knowledge Gaps
- **3 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Not enough signal to generate questions. This usually means the corpus has no AMBIGUOUS edges, no bridge nodes, no INFERRED relationships, and all communities are tightly cohesive. Add more files or run with --mode deep to extract richer edges._