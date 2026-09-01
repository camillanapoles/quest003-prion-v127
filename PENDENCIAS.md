# PENDÊNCIAS — Ledger Mestre Garantista (Quest 003)

**Função:** fonte única de todas as pendências planejadas do programa — capturadas das auditorias local+remota de 30/08 (ver `AUDIT_CAPTURE_2026-08-30.md`), do TODO-registry (`{{TODO:id:desc}}`), dos /RECAPs e dos logs de otimização. **Garantia:** o check **A9** (`scripts/pendencias_check.py`, embutido no `ast_check.py` e no pre-commit hook) BLOQUEIA commit se: item agente planejado sem deferação explícita (`{{DEFER:...}}`), evidência de item fechado inexistente, resumo divergente da contagem, ou marcador TODO descompassado do ledger. **Regra herdada do decálogo:** resolver pendência = remover o marcador e fechar a linha aqui.

**Taxonomia de STATUS:** PLANEJADA · EM_EXECUCAO · EXECUTADA_NAO_MERGADA · FECHADA · DORMANT · BLOQUEADA_EXTERNA · AGUARDANDO_AUTORA · AGUARDANDO_LAB · AGUARDANDO_EXECUTOR
**DONO:** AGENTE · AUTORA · LAB · EXECUTOR (sessão executora externa à de ledger)

<!-- LEDGER-RESUMO total=26 abertas=21 planejadas_agente=8 fechadas=4 dormant=1 -->

| ID | TODOID | PENDÊNCIA | DONO | STATUS | EVIDÊNCIA/ARTEFATO | ORIGEM |
|---|---|---|---|---|---|---|
| P-001 | - | Sweep de composição de taxas ±50% — **EXECUTADO (cloud GHA run 33459375823; veredito C2 GAP-1 MATERIAL; F-43/N049-054)** | AGENTE | FECHADA | experiments/ws_9_results/ws_9_v5_sweeps_S3.json | gap-mapper GAP-1 · SKILL_SCOUT_S3 |
| P-002 | - | Teste de invariância de θ* entre espécies — guarda-chuva da PARTE 3, decomposto em P-023..P-026. **PRIORIDADE-1 (S3/C2: contenção é sensível à escala de taxas — só dado multi-espécie real resolve)** {{DEFER:Fase 0 OK (gap-mapper@edd2361); sequência P-023→26; ver paper/guardian/PLAN_PARTE3_CROSS_SPECIES.md}} | AGENTE | PLANEJADA | paper/guardian/PLAN_PARTE3_CROSS_SPECIES.md | diretriz da autora 30/08 · F-43 |
| P-003 | - | Verificação claim-a-claim dos 88 candidatos (batches 1–6) + 49 bindings → elevação E-registry 38→≥150 fontes + re-target AST A5/A8 | AGENTE | EM_EXECUCAO | ../003-executor/paper/evidence_workspace/candidates/verification_status_consolidado.csv | otimizacao P1.1 / OPTIMIZATION_LOG |
| P-004 | - | /RECAPs das sessões 29–30/08 (ausentes nos runbooks — regra 10) reconstruídos e anexados | AGENTE | FECHADA | guardian.md | AUDIT_CAPTURE §D5 |
| P-005 | - | Marcadores obsoletos removidos (resolver=remover): ETRIZACAO-APLICAR, PUBMED-DIRECT, Q3-Q5-EXEC | AGENTE | FECHADA | paper/ERITRIZACAO.md | AUDIT_CAPTURE §D6 |
| P-006 | - | Gancho garantista de pendências instalado: ledger + A9 + portabilidade skills no AST | AGENTE | FECHADA | scripts/pendencias_check.py | mandato da autora 30/08 |
| P-007 | BIORXIV-ADDENDUM | Depositar Parte 1 no bioRxiv; ao depositar, adicionar DOI como adendo nos PDFs/repo | AUTORA | AGUARDANDO_AUTORA | paper/lab_outreach_package.md | /RECAP 28/08 |
| P-008 | TESE-FICHA | Preencher ficha catalográfica ABNT (template pronto na branch otimizacao-pqms-batch1) e re-hash C054 | AUTORA | AGUARDANDO_AUTORA | paper/manuscript_Parte2_v1.md | /RECAP 28/08 + otimizacao P3.1 |
| P-009 | - | OK da autora: anexos P2.1/P2.2 (população/impacto + roadmap TRL) + entrada do posicionamento ACP×in-silico-trials na tese | AUTORA | AGUARDANDO_AUTORA | ../003-executor/paper/otimizacao/OPTIMIZATION_LOG.md | otimizacao P2.1/P2.2 |
| P-010 | EMAIL-GROVEMAN | Enviar kit #1 (RML) — endereço institucional Groveman + outreach | AUTORA | AGUARDANDO_AUTORA | paper/outreach_email_1_groveman.txt | /RECAP 27/08 |
| P-011 | GATEF-SIGNATURE | Assinatura da PI do lab parceiro — último item do GATE-F (dormant por recorte da autora: tese não seleciona lab) | LAB | AGUARDANDO_LAB | experiments/G0_EXECUTION_FREEZE_CHECKLIST.md | /RECAP 28/08 |
| P-012 | Q3Q5-OFFICIAL | Rodar Q3–Q5 do protocolo de parceiro em fonte oficial (CTG API/agenda pública) | EXECUTOR | AGUARDANDO_EXECUTOR | experiments/part2_results/partner_selection_log.md | partner_log v0.2 |
| P-013 | IDENTIFY-ORGANOID-DONOR-LAB | Identificar grupo da palestra CJDF-2026 (agenda pública) — potencial 3º elegível | EXECUTOR | AGUARDANDO_EXECUTOR | experiments/part2_results/partner_selection_log.md | partner_log §4 |
| P-014 | PARTNER-RUN | Executar fluxo identificados→triagem→pontuação→contato sequencial (kits prontos; envio é ação humana) | EXECUTOR | PLANEJADA | paper/lab_outreach_package.md | F10 checklist |
| P-015 | COST-DECOMP | Decompor US$100–150k em tabela suplementar (limitação 15; manuscritos EN+PT gated) {{DEFER:tabela suplementar exige edição gated + paridade PT/EN + re-gate; opcional por design}} | AGENTE | PLANEJADA | paper/manuscript_EN_v5.md | TODO-registry |
| P-016 | - | D-08: extração VizHub GBD do valor absoluto de DALYs priônicos (ferramenta interativa instável; reforço opcional, não-bloqueante — D-01 já fechado via opção B) | AGENTE | BLOQUEADA_EXTERNA | ../003-executor/paper/otimizacao/OPTIMIZATION_LOG.md | executor D-08 |
| P-017 | SEARCHLOG-FULL | Queries exatas das ~90 buscas não reconstituíveis retroativamente — limitação DECLARADA no manuscrito; logs futuros no momento da busca | AGENTE | DORMANT | paper/manuscript_PT_v5.md | TODO-registry |
| P-018 | - | Batch 6+ do programa de otimização (meta ≥150 refs únicas, ≥60% 2021+; regra de suspensão por D-01 liberada — D-01 fechado) {{DEFER:continuação de P-003 na mesma linha claim-a-claim; depois re-rodar AST A5/A8 majorado}} | AGENTE | PLANEJADA | ../003-executor/paper/evidence_workspace/candidates/batch5_ref_candidates.csv | OPTIMIZATION_LOG |
| P-019 | - | Decisão sobre branch fix/fig1-parte1 (stale, 70 commits atrás; figs archify existem só lá) {{DEFER:rebase-ou-descartar é decisão da autora; fig1 em main já regenerada do grafo v3.2}} | AGENTE | PLANEJADA | ../quest003-fixfig1/paper/latex/figs/archify/fig1.svg | AUDIT_CAPTURE §D4 |
| P-020 | - | Branch otimizacao-pqms-batch1: manuscript_Parte2_FULL.tex (1506 L) + TESE-FICHA-TEMPLATE + anexos P2.1/P2.2 — trabalho pronto, merge pendente de OK da autora (P-009) | AGENTE | EXECUTADA_NAO_MERGADA | branch:otimizacao-pqms-batch1 @bd95dc9 (remoto GitHub) | compare API main...otimizacao |
| P-021 | - | Branch executor (+10 commits): candidatos verificados, D-01/D-02/D-03 fechados, bindings rascunhados — merge condicionado a P-003 (claim-a-claim) | AGENTE | EXECUTADA_NAO_MERGADA | branch:executor @a3e2a37 (remoto GitHub) | compare API main...executor |
| P-022 | - | Branch gap-mapper (+3 commits): GAP_MAPPER v1/v2 + ACTION_PLAN_CROSS_SPECIES — merge condicionado a P-001/P-002 (elevação a claims com binding) | AGENTE | EXECUTADA_NAO_MERGADA | branch:gap-mapper @e7a2976 (remoto GitHub) | compare API main...gap-mapper |
| P-023 | - | Fase 1 P3: extração de parâmetros por espécie (K_autocat/K_frag/K_nucl/k_clear/[PrP^C]₀) com proveniência + elevação Corridon 2026→E039+ {{DEFER:após P-001 e Fase 0 (sync gap-mapper←main); skill paper-lookup+scientific-writing}} | AGENTE | PLANEJADA | ../003-gap-mapper/analysis/ACTION_PLAN_CROSS_SPECIES.md | PLAN_PARTE3 §3 F1 |
| P-024 | - | Fase 2 P3: ws_9_multispecies.py (motor v4 intocado, parity C0 embutido, κ-sweep {1.5,2,3,4,8}, relógio por espécie normalizado) → JSONs por espécie {{DEFER:requer P-023 concluído; skills TDD+code-review+uncertainty}} | AGENTE | PLANEJADA | paper/guardian/SKILL_SCOUT_S3_RATECOMPOSITION.md | PLAN_PARTE3 §3 F2 |
| P-025 | - | Fase 3 P3: θ* por espécie + IC + decomposição de sensibilidade + figuras auditáveis dos JSONs {{DEFER:requer P-024; skills visualization+statistical-analysis}} | AGENTE | PLANEJADA | paper/guardian/PLAN_PARTE3_CROSS_SPECIES.md | PLAN_PARTE3 §3 F3 |
| P-026 | - | Fase 4 P3: síntese pelos Cenários A/B/C travados + N-fatos/canon/claims + gates + PR gap-mapper→main + /RECAP {{DEFER:requer P-025; veredito pelo critério pré-registrado, nunca pelo desejo}} | AGENTE | PLANEJADA | paper/guardian/PLAN_PARTE3_CROSS_SPECIES.md | PLAN_PARTE3 §3 F4 |

## Mapeamento por skill scientific-\* (como cada pendência é garantida)

| Pendência | Skill que rege a execução | Instrumento de garantia |
|---|---|---|
| P-001, P-002 | scientific-critical-thinking (falsificabilidade proporcional) + REPARAM_LOOP (locked-stays-locked) | script determinístico → JSON → N-fatos → gate; A9 impede esquecimento |
| P-003, P-018 | scientific-writing (evidence-binding; identifiers só de fonte aberta) | validate_manifest/check_references no AST A4/A8 + auditoria claim-a-claim |
| P-015 | scientific-writing (limite declarado × suplemento) | edição gated com paridade PT=EN + guardian R2 |
| P-012, P-013, P-014 | scientific-brainstorming (critérios/pesos congelados; "?" não pontua) | PARTNER_SELECTION_PROTOCOL v2.1 + log público |
| P-004, P-005, P-006 | meta-ciência do harness (guardião recursivo) | A9 + TODO-registry do guardian.py |

**Manutenção:** toda sessão que cria/resolve pendência atualiza este ledger ANTES do /RECAP; o A9 roda no pre-commit e no AST — pendência planejada sem `{{DEFER:...}}` bloqueia o commit até ser executada ou deferida com justificativa visível.
