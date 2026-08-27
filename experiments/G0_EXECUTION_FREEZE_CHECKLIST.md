# PARTE 2 — Artefato 2.2: Checklist de Freeze de Execução do G0-wet
## O que deve estar travado (commit + assinatura) ANTES do primeiro organoide infectado
**Deriva de:** §2.5 (SAP/blinding/kill) · §2.7 (θ_obs) · G0_UNLOCK_DOSSIER · epistemic E-01/E-09/E-23 · v1 · 2026-08-27

| # | Item a congelar | Artefato | Status |
|---|---|---|---|
| F1 | Estimador θ_obs (grade, features, função-objetivo, margem de decisão vs 0.333) | `part2_theta_obs_v1.py` + JSON de calibração | ✅ CALIBRADO (part2_theta_obs_v1.json): veredito ADEQUADO por critérios pré-declarados (cobertura 3/3, bias≤0.032) · NOTA HONESTA: resolução por-órganoide é baixa (IC unitário ~grade inteira) — o pooling n=8/mediana por braço (§2.7) é a fonte de precisão; POOLED EXECUTADO (part2_theta_obs_pooled.json): veredito PARCIAL por critérios pré-declarados — PASS integral NA FRONTEIRA DE DECISÃO (κ=2: bias −0,008, modal 69%, cobertura ✓; é a região θ≈0,33 da predição travada); κ=8 com bias +0,060 CONSERVADOR (lê contenção menos otimista); limitador estrutural = grade 6 pontos com κ̂ por vizinho-mais-próximo → V1.1-IDW TESTADA E REJEITADA (part2_theta_obs_v11.json): interpolação suaviza entre κs e PIORA a fronteira de decisão (bias +0,008→−0,037 em κ=2; cobertura quebra em κ=8) — v1.0-NN MANTIDA como estimadora de freeze (PASS na fronteira; conservadora em κ alto). Caminho de refinamento futuro (opcional, se o painel pedir IC mais estreito): grade-κ mais fina com novas simulações — NÃO exigido pelos critérios pré-declarados. **F1 = FECHADO (v1.0-NN).** |
| F2 | Análise estatística braço-a-braço (Welch vs A2; Holm α=0.05 nas 5 comparações; n=8→12; poder declarado) | §2.5 manuscrito v5 + g0_protocol.md | ✅ escrito |
| F3 | Cegamento: scorer do PrP-res (WB/IHC) cego ao braço; código de aleatorização por lote/linha de iPSC | este checklist + SOP do lab | ✅ especificado |
| F4 | Estratificação por lote e aleatorização (dado DP MV2 ≈77% da média) | §2.5 + checklist | ✅ especificado |
| F5 | Controle positivo A8 (PPS, protocolo Groveman 2021) e critério de validade do ensaio (A8 deve mostrar efeito; se não, ensaio NÃO-validado → re-run) | g0_protocol.md | ✅ |
| F6 | Kill-switches por braço + critério de morte programática (nenhum gradiente EM θ_obs>0.33 em todos ⇒ programa encerra, negativo publicado) | §2.5 | ✅ |
| F7 | Formato de dado [ORGANOID] cru (tabela: orgão_id, lote, braço, dpi, R_medido_mm, biomass_ratio, scorer_id) — esquema que o estimador consumirá | spec abaixo | ✅ novo |
| F8 | Loop de re-parametrização (o que recalibra, com que prior, quando) | `REPARAM_LOOP.md` | ✅ novo |
| F10 | Parceiro selecionado pelo PROTOCOLO SLR-análogo (critérios/pesos congelados pré-contato; log público) | `PARTNER_SELECTION_PROTOCOL.md` + selection_log | {{TODO:PARTNER-RUN:executar o fluxo identificados→triagem→pontuação→contato; log em part2_results}} |
| F9 | Timelines de readout (90–120 d pós-seeding; regime estacionário desde ~4 d) | g0_protocol | ✅ |

## Esquema de dado [ORGANOID] (F7) — o contrato entre bancada e estimador
```json
{"organoid_id": "str", "batch": "str", "arm": "A1..A8", "dpi": int,
 "front_R_mm": float, "biomass_ratio": float, "assay": "WB|IHC|RT-QuIC",
 "scorer_id": "str (blindado)", "anomalias": "str|null"}
```
Regra: nada além deste esquema entra no estimador; qualquer campo faltante → organoid excluído ANTES da análise (lista de exclusões publicada, não editada pós-hoc).

## Gates formais do freeze
- **GATE-F** (liberação para infectar): F1–F9 todos ✅ + estimador com veredito ADEQUADO na calibração [SIM] + {{TODO:GATEF-SIGNATURE:assinatura da PI do lab parceiro — último item do gate}}.
- Qualquer mudança pós-GATE-F = emenda auditada (commit + justificativa + re-análise com e sem a mudança).
