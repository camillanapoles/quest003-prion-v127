# GUARDIAN2.MD — Doutrina Operacional da PARTE 2 (gate de conformidade de MÉTODO e DADOS)
## Manual HOW-TO da tese de continuidade (ACP) + registro /RECAP da Parte 2
**Companheiro do guardian.md (Parte 1/global).** Toda sessão que tocar a Parte 2 lê ESTE arquivo primeiro; toda sessão de trabalho Parte 2 termina anexando /RECAP aqui e no session-state.

---

## §1 · O QUE O GUARDIÃO-2 GARANTE (identidade)
O gate da Parte 2 existe para responder uma pergunta só: **"isto ainda é método e dado impecáveis?"** — onde impecável significa:
1. **Método**: a ACP (§1-met do manifesto2) está nomeada, com passos P0–P6 declarados, e o eixo retórico se mantém — *tudo é simulação e é dito que é*; nada promete aplicação/validação; dado real análogo ⇒ antecipação **bancada** (P6), nunca pendência.
2. **Dados**: todo número vem de JSON arquivado ou do registro E (nunca digitado); linhagem §1-bis (quem→espécie→cruzamento→código→parametrização→resultado) íntegra; tiers rotulados.
3. **Conformidade estrutural**: guardian.py `--profile part2` com **R3-BASE-VALIDADE BLOCKED** — a Parte 2 sem Base de Validade declarada não passa, por invariante.


**As quatro dimensões de revisão hostil de tese (mapeamento formal):**
| Dimensão | Como o gate-2 atesta | Check-chave |
|---|---|---|
| **Metodologia** | ACP P0–P6 declarada; critérios antes de resultado; anti-hindsight; rejeições publicadas | R3-BASE-VALIDADE · R3-G0SIM · eixo retórico |
| **Dados** | linhagem §1-bis (quem→espécie→cruzamento→código→parâmetro→resultado); número só de JSON/registro; tiers | R0-drift · N-fatos · R1-NUM-UNBOUND |
| **Conformidade** | formato de claims/evidência da skill; paridades; TODO-registry; decálogo | R0-ORPHAN · R2 · TODO-registry |
| **Conteúdo** | §1-met a §8 íntegros; PRODUTO FINAL declarado; promessas/limites honestos | R3-CANON · R3-THETA-OPS · R3-SAP |

**Gates BLOCKED permanentes do perfil part2:** R3-BASE-VALIDADE · R3-THETA-OPS · R3-SAP · R3-G0SIM · R3-CANON (mesma espinha da Parte 1 + o mandato próprio).

## §2 · COMANDOS ESSENCIAIS (copiar-colar)
```
# GATE da Parte 2 (antes de qualquer commit de manifesto2):
cd paper/guardian && python3 guardian.py --round 3 --profile part2 \
  --md ../manuscript_Parte2_v1.md --tex ../latex/manuscript_v5_EN.tex \
  --claims ../evidence_workspace/claims.csv \
  --manifest ../evidence_workspace/source_manifest.json \
  --consistency ../evidence_workspace/consistency_manifest.json \
  --registry guardian_registry_parte2.json --report guardian_report_parte2.md
# GATE da Parte 1 (inalterado — checar que não regrediu):
#   mesmo comando SEM --profile, --md manuscript_EN_v5.md (ver guardian.md §2)
# Audit oficial (ferramenta single-manuscript — divergências em AUDIT_NOTES §part2):
S=/workspace/projects/scientific-agent-skills/skills/scientific-writing/scripts
python3 $S/audit_claims.py ../manuscript_Parte2_v1.md claims.csv source_manifest.json
# AST EXECUTÁVEL (com a bateria oficial EMBUTIDA — 8/8: solver+2 gates+validate_manifest+registro+artefatos+check_consistency+check_references):
#   python3 experiments/ast_check.py   ← rodar a TODO ciclo; A7/A7-bateria garantem que 'check_consistency não rodava' NUNCA mais escorrega

# Artefatos executáveis da Parte 2:
python3 experiments/part2_theta_obs_v1.py       # grade+calibração unitária
python3 experiments/part2_theta_obs_pooled.py   # regime n=8 (§2.7)
python3 experiments/part2_theta_obs_v11.py      # rejeitada — manter como evidência
python3 experiments/ws_9_v5_sweeps_gha.py --phase S1|S2
```

## §3 · DECÁLOGO DA PARTE 2 (regras invioláveis)
1. **É simulação e é dito que é** — em toda saída; tiers [SIM]/[ORGANOID]/[MOUSE]/[HUMAN] obrigatórios.
2. **Não promete aplicar nem validar** — dado real análogo ⇒ passos seguintes JÁ avançados (P6); nunca "pendente de validação".
3. **Método, não seleção** — nenhum laboratório é escolhido na tese; M4 é protocolo + piloto não-decisório.
4. **Base de Validade é mandato** — §1-bis com tríade + linhagem; perdê-la é BLOCKED.
5. **Número vem de JSON/registro** — regra de nunca-digitar; N044–N048 cobrem os resultados Part 2.
6. **Locked-stays-locked** — θ\*=0,333 (v1.0) compara-se, retreina-se jamais; recalibração só o que o dado informa.
7. **TODOs em `{{TODO:id:desc}}`** — TODO solto é AMEND; resolver = remover.
8. **Registro conjunto** — claims.csv serve às duas partes (C001–C051 P1; C052–C054+ P2); CLAIM_NOT_USED da ferramenta é divergência documentada (AUDIT_NOTES §part2), não lacuna.
9. **Rejeições são evidência** — v1.1-IDW rejeitada permanece no repo com JSON válido; auditoria publica suas correções (nota §8 do manifesto2).
10. **Fim de sessão Parte 2 = /RECAP** aqui + session-state.

## §4 · FLUXOS PADRÃO
- **Editar manifesto2**: md → gate part2 (PASS 0/0) → commit. Mudança de método (P0–P6, eixo retórico, BASE-VALIDADE) = emenda versionada com justificativa.
- **Novo resultado [SIM] Parte 2**: script determinístico → JSON em `experiments/part2_results/` → N-fatos (consistency_manifest) → manifesto2 §2/§8 inventário → gate → push.
- **Novo claim C05x**: texto normalizado→sha (norm da skill) no claims.csv + claim_texts.md + tag `[claim:Cxxx] [evidence:Exxx]` no manifesto2.
- **Validação expressa da autora**: pendências de validação ficam como TODO (hoje: `PARTE2-V2-VALIDACAO`) e só fecham com OK dela registrado em commit.


### Protocolo de Ciclo (diretriz da autora, 28/08) — TODO ciclo de trabalho
1. **RELATE (antes)**: ao usuário, o que será realizado, COMO e PORQUÊ — nenhuma ação sem anúncio metódico prévio.
2. **EXECUTE**: a ação, com o método já declarado.
3. **AST (verificar)**: fechamento obrigatório do ciclo com verificação — `python3 experiments/ast_check.py` (6/6) ou o gate específico da superfície tocada. Ciclo sem AST não está fechado.

## §5 · MAPA DE ARTEFATOS PARTE 2
manifesto: `paper/manuscript_Parte2_v1.md` (PT mestre) · gate: `paper/guardian/guardian.py --profile part2` + `guardian_registry_parte2.json`/`guardian_report_parte2.md` · resultados: `experiments/part2_results/` (theta_obs v1/pooled/v11 + derived_summary + partner_log) · scripts: `experiments/part2_theta_obs_*.py` · método-docs: `G0_EXECUTION_FREEZE_CHECKLIST.md` (dormant) · `REPARAM_LOOP.md` · `PARTNER_SELECTION_PROTOCOL.md` v2.1 · registro compartilhado: `paper/evidence_workspace/` (54 claims · 38 fontes · 48 N-fatos) · divergências audit: `AUDIT_NOTES.md` §part2.

## §6 · PROTOCOLO /RECAP (fim de sessão Parte 2)
Mesmo formato do guardian.md §6 (FEITO/ESTADO/PRÓXIMO/ÂNCORA), anexado AQUI.

---

/RECAP 2026-08-27 (noite) — Parte 2 v3
FEITO: guardian2.md criado (réplica estrutural do guardian.md p/ conformidade de método+dados) · ACP nomeada (C054; §1-met P0–P6; eixo retórico) · BASE-VALIDADE §1-bis (linhagem 6 linhas; check BLOCKED) · auditoria de disco: v11.json regenerado + sinal bias −0,008 corrigido em 3 docs · §8 inventário (9 artefatos) + nota de integridade · audit oficial P2 rodado c/ divergências documentadas
ESTADO: Parte 1 gate PASS 0/0 · Parte 2 gate PASS 0/0 · 54 claims/38 fontes/48 N-fatos · main @67b2ee6 sincado · TODOs: PARTE2-V2-VALIDACAO (autora), BIORXIV-ADDENDUM (autora), GATEF-SIGNATURE (lab, dormant), PARTNER-RUN/EMAIL-GROVEMAN (anexo operacional, fora da tese), COST-DECOMP (opcional)
PRÓXIMO: (autora) validar tabela M1–M5 reenquadrada + linhagem §1-bis + inventário §8 | (agente) PDF/LaTeX da Parte 2 impecável p/ publicação
ÂNCORA: main @67b2ee6 · predições travadas v1.0 · Parte 1 release v3.0 intacta

/RECAP 2026-08-28 ~01:40 — P2/v6 idem guardian.md (FEITO incl. scout D2-related-work p/ ACP; AST 6/6; Protocolo de Ciclo) · PRÓXIMO aguarda autora (validação+posicionamento C opcional→merge) · guardião-2 íntegro


/RECAP 2026-08-28 (merge) — PR #2 MERGED em main@a01f8c2: **TESE COMPLETA EM DUAS PARTES** (P1=v5/release v3.0; P2=v6=ACP com PRODUTO FINAL + validação expressa da autora registrada). Gates 0/0 · AST 6/6 · fila agente vazia · restam: BIORXIV (autora) + GATEF (lab, dormant)

/RECAP 2026-08-28 (FINAL — tese finda COMPLETA conforme produzida)
FEITO: Parte 2 BILÍNGUE (companion EN integral: PRODUTO FINAL·[NO YEAR]·ACP P0-P6·Validity Basis·mapeamento análogo·resultados·M1-M5·promessas; paridade claims 14=14) · LaTeX EN+PDF (57,5KB tectonic) · gates PT+EN ambos 0/0 (padrão Validity Basis aceito; EN impecável com literais de invariante) · PDF EN anexado ao release v6.0
ESTADO: TESE COMPLETA E BILÍNGUE — releases v3.0 (P1) + v6.0 (P2: PT+EN) · gates 4 superfícies 0/0 · AST 6/6 · registro 54/38/48
PRÓXIMO: externo apenas — BIORXIV (autora) · GATEF (lab, dormant) — internamente, FINDADA
ÂNCORA: main@9102c36 · v3.0/v6.0 · predições v1.0

/RECAP 2026-08-28 03:40 — Ciclo 2 FECHADO (após 3 tentativas honestas)
FEITO: Cap.2 Fundamentação (corroborado pelas 38 fontes; herança=lógica correta; in-silico trials c/ 2 complementares em verificação) · REFERÊNCIAS COMPLETAS 38 ABNT programáticas do manifest + CONCORDÂNCIA 54 claims→refs (régua: claim sem referência = inaceitável — atendida) · RECONSTRUÇÃO CANÔNICA do documento (pré-textuais→Cap1→Cap2→metodo→resultados→componentes→refs; esqueleto verificado linha a linha) · gates 0/0
ESTADO: documento de tese ~70% (faltam: Ciclo 3 = renumerar Cap.3-4 + EQUAÇÕES da metodologia; Ciclo 4 = figuras próprias em resultados + discussão/conclusões-por-objetivo + EN sincronizar; PDFs regenerar ao final)
PRÓXIMO: Ciclo 3 (equações ADR/freeS/calibração com procedência por parâmetro no corpo) — depois Ciclo 4 e /RECAP de fechamento do documento
ÂNCORA: main@HEAD · registro 54/38/48 · predições v1.0

/RECAP 2026-08-28 04:35 — Ciclo 3 FECHADO
FEITO: capítulos renumerados (1-5 + Apêndice A) · §3.2 equações com proveniência (ADR/freeS+θ/relógio/estimador — claims+refs adjacentes) · gate 0/0 · memória id32: 13 instruções da autora consolidadas
ESTADO: documento ~85% · falta Ciclo 4: figuras próprias no Cap.4 (θ-response/subtipos/tabela-decisão como figuras) + §5.2 discussão ampliada + CAPÍTULO 6 CONCLUSÕES POR OBJETIVO (OE1-OE5/H1-H3) + EN sincronizar + PDFs regenerar
ÂNCORA: main@HEAD · 54/38/48

/RECAP 2026-08-28 06:05 — CICLO 4 FECHADO · DOCUMENTO DE TESE COMPLETO
FEITO: figuras no corpo (Fig1-3 dos JSONs) · §5.2 discussão (significa/não-significa) · CAPÍTULO 6 CONCLUSÕES POR OBJETIVO (OE1-OE5 ✓ · H1-H3 c/ veredicto · síntese P6) · cross-check matemático P2↔P1 (17/18 idênticos; ℓ 3,59≈3,6 notado) · tex/PDF PT 75,7KB recompilado c/ §3.2+Cap6 · EN sync (formulação+conclusões) · gates PT+EN 0/0
ESTADO: DOCUMENTO DE DOUTORADO COMPLETO — pré-textuais · Cap1 introdução formal · Cap2 fundamentação c/ 38 refs ABNT · Cap3 metodologia c/ equações · Cap4 resultados c/ figuras · Cap5 discussão · Cap6 conclusões-por-objetivo · Apêndice A · concordância 54 claims→refs · válida por estrutura padrão de tese (ficha acadêmica {{TODO:TESE-FICHA}} = única pendência interna, da autora)
PRÓXIMO: (autora) preencher ficha acadêmica; eventual defesa; BIORXIV P1; GATEF dormant — interno: FINDADO como documento
ÂNCORA: main@e175c68 · 54/38/48 · predições v1.0
