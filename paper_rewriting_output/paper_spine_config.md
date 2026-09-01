# PaperSpine Config (human-readable mirror of paper_spine_config.json)

## O que vamos construir
**Tese doutoral unificada e autocontida (Parte 1 + Parte 2)** em um único PDF de padrão publicação — referência de qualidade: *Johns Hopkins Bloomberg School of Public Health — Center for Clinical Trials and Evidence Synthesis* (URL oficial no config) e padrões de dissertação Harvard-class. PaperSpine opera como **incremento** (braço B isolado no branch `writing-v2-test`); adoção só após avaliação A-vs-B (WRITING_V2_PROTOCOLO.md).

## Decisões principais (com justificativa)
| Decisão | Escolha | Base |
|---|---|---|
| Fluxo | `build_from_materials` | A tese unificada nasce dos materiais do repo (manuscritos, canon, registros, JSONs) — não é reescrita de um draft único |
| Cena | `journal` (pro) | Padrão publicação: contribuição-confirmada, validação-por-resultados, auditoria-de-revisor (V4 rules) |
| Idioma | **PT-BR primário** (tooling `en`) | Tese brasileira; ABNT co-edição preservada; framework suporta en/zh nos artefatos de máquina |
| **Coluna** | **ÚNICA** | Dissertações JHU/Harvard são coluna-única; ABNT NBR 14724 (A4, margens 3/2cm) é single por norma; equações/figuras/tabelas largas do programa (ex. tabela-decisão κ↔θ↔R) exigem largura integral; coluna dupla é otimização de espaço de periódico impresso (classe Nature/NEJM), não padrão de tese |
| Citações | 56 (registro real) | citation_target_count = tamanho do E-registry verificado (validate_manifest 0/0) |
| Humanize | none | Texto acadêmico; a camada clínica (NOTA/openers) já existe na alfa e é preservada |

## Invariantes do projeto (acima da skill)
Predições v1.0 comparadas jamais retreinadas · claims com hash sha256 + binding · tiers em toda saída · nunca fabricar (alinhado ao core rule PaperSpine) · guardian gates permanecem para superfícies gated · decisão final de adoção = autora.

## Rota
Resume-first OK (output vazio → início limpo) · Stage 1 intake ✓ · Stage 2 research (6 artefatos) → Stage 3 citation bank (≥168 candidatos do registro+pool) → **Stage 4 STOP obrigatório: confirmação de motivação pela autora** → Stage 5-12 com gates.
