# Plano de Continuidade Metodológica — Parte 2 da Tese
## Do dado parametrizado à validação gate-a-gate: G0-sim [SIM] → G0-wet [ORGANOID] → G1 [MOUSE] → G2 [HUMAN]

**Manuscrito Parte 2 · v1 · 2026-08-27 · PT-BR (mestre)**
Open Prion & Molecular Engineering Consortium — correspondente: Camilla N. (CRediT in-repo)
Companion da Parte 1 (manuscript_EN_v5/PT_v5, release v3.0) — **não a modifica**: cita-a, estende-a. Gated pelo guardião R0–R3 [claim:C046] [evidence:E032, E033].

---

## Resumo

A Parte 1 demonstrou a tese de design: plataforma de contenção V127 quantitativamente dimensionada, com gate computacional G0-sim **executado, aprovado e reproduzido em dois ambientes** [claim:C046] [evidence:E032, E009, E007, E033], colheita de sensibilidade com predição discriminadora [claim:C051] [evidence:E032, E033] e estimador θ_obs com calibração por simulação com **veredito ADEQUADO por critérios pré-declarados na fronteira de decisão** [claim:C052] [evidence:E032, E033]. A Parte 2 **deste manuscrito** é o plano metodológico de continuidade: como o dado parametrizado [SIM] opera como substrato da validação — o que medir, como estimar, o que congelar, como o dado medido realimenta os modelos, e COMO (não quem) escolher o laboratório. O modo epistêmico é o da física teórica — previsibilidade e antecipação de informação (estimativas precedem, dirigem e valem até a medição — Parte 1 §4.1): o programa computacional não para à espera do wet-lab; tudo que tem publicação é usado como evidência direta; tudo que não tem entra como metodologia pré-declarada. A tese tem **[SEM ANO]**: definida por resultados, com durações de fase como estimativas de planejamento [claim:C047] [evidence:E032, E033]. Esta Parte 2 documenta **método somente** — nenhuma seleção de laboratório é feita aqui; a seleção é ato de execução, do executor futuro, guiado pelo método §5 [claim:C053] [evidence:E033].

## 1. Natureza e escopo

A Parte 2 é a **tese de continuidade** na arquitetura declarada (C049): duas partes unidas na junção G0, insustentáveis separadas — Parte 1 sozinha seria design não-exercido; Parte 2 sozinha seria experimentação sem prior quantitativo [claim:C049] [evidence:E032, E033]. Componentes deste plano (M1–M5), cada um com artefato executável ou executado no repositório:

| # | Componente | Estado | Artefato |
|---|---|---|---|
| M1 | Estimador θ_obs (consome a grade-κ parametrizada) | **calibrado e rejeitado-melhorado** (ver §2) | part2_theta_obs_{v1,pooled,v11}.json |
| M2 | Freeze de execução do G0-wet (F1–F10 + GATE-F) | especificado | G0_EXECUTION_FREEZE_CHECKLIST.md |
| M3 | Loop de re-parametrização (anti-hindsight) | especificado | REPARAM_LOOP.md |
| M4 | Método de seleção de parceiro (SLR-análogo) | método + aplicação-piloto | PARTNER_SELECTION_PROTOCOL v2.1 + log v0.2 |
| M5 | Infraestrutura de continuidade (guardião + runbook) | operante | guardian.py + guardian.md (decálogo) |

## 2. M1 — Estimador θ_obs: o dado parametrizado como instrumento

O objetivo operacional: converter gradiente proximal/distal medido em θ_obs comparável ao limiar travado θ\*=0,333 [claim:C038] [evidence:E032] **sem circularidade** (grade e função-objetivo congeladas antes do dado; Parte 1 §2.7). A validação do próprio instrumento é computacional — simulation-based calibration sobre a grade κ∈{1,5–8} do motor v4 exato:

- **Calibração unitária** (1000 boots; ruído organoide publicado CV 30/40%): veredito **ADEQUADO** por critérios pré-declarados (cobertura do θ verdadeiro 3/3; bias ≤ 0,032) [claim:C052] [evidence:E032, E033] — com nota honesta: resolução por-órganoide é baixa; a precisão vem do **regime declarado** (mediana por braço, n=8).
- **Regime pooled n=8**: PASS integral **na fronteira de decisão** (κ=2: bias 0,008; recuperação modal 69%; cobertura ✓) — a região exata onde a predição travada decide (θ<0,33) [claim:C052] [evidence:E032, E033]; em κ alto o bias é **conservador** (+0,060: superestima θ, subestima contenção — erro no lado seguro).
- **v1.1-IDW (interpolação) testada e rejeitada**: piorou a fronteira (bias −0,037, direção anti-conservadora) e quebrou cobertura em κ=8 — registrado como evidência de que a disciplina anti-hindsight está viva: o upgrade que falha é descartado, não embranquecido [claim:C052] [evidence:E032, E033].
- Achado de design que o método produziu: a razão de biomassa carrega a informação que o raio perde por saturação (R 0,843→0,760 mm contra razão 48→1,25 na grade) — o estimador opera no par de features por necessidade [claim:C052] [evidence:E032, E033].

## 3. M2 — Freeze de execução: o que trava antes do primeiro organoide

Dez itens F1–F10, com GATE-F de liberação: estimador (F1, fechado — §2), plano estatístico (Welch/Holm α=0,05, 5 comparações; n=8→12; poder ~80% para Δ≥50%), cegamento do scorer, randomização/estratificação por lote (DP MV2 ≈77% da média publicada), controle positivo A8-PPS como critério de validade do ensaio, kill-switches por braço + **critério de morte programática**, esquema de dado [ORGANOID] (contrato bancada→estimador; exclusões publicadas nunca editadas), loop M3, timelines (readouts 90–120 d; regime estacionário desde ~4 d) e M4 (parceiro por método). Regra: pós-GATE-F, qualquer mudança é emenda auditada com re-análise com-e-sem.

## 4. M3 — Loop de re-parametrização (o coração anti-hindsight)

O dado medido recalibra **exatamente o que informa**: o braço A6 (dose conhecida) fecha κ↔µM — âncora ilustrativa da Parte 1 §2.2 tornado absoluto pelo dado — convertendo o cálculo de contenção de relativo a absoluto — e executa o teste discriminador da forma funcional (primeira potência vs quadrática; travado na colheita [SIM] da Parte 1) [claim:C051] [evidence:E032, E033]; θ\* **compara-se, nunca se retreina**; taxas murinas relativas e parâmetros de transporte humano só mudam por dado do seu próprio escopo. Toda comparação cita a âncora do release onde a predição foi travada (v1.0 / v3.0); toda recalibração gera pre-dição nova **antes** do próximo dado — o loop nunca "explica depois" sem ter previsto antes.

## 5. M4 — Método de seleção de parceiro: assertividade por método (SLR-análogo)

**A tese documenta o COMO; não seleciona o QUEM** [claim:C053] [evidence:E033]. O protocolo (v2.1) é o análogo de revisão sistemática aplicado à decisão "onde medir":

1. **Query bank Q1–Q5** — strings exatas por plataforma (PubMed `[tiab]`, ClinicalTrials.gov, cinza-conferências, rede BR), registradas antes da execução, ancoradas em commit (PROSPERO-análogo);
2. **Inclusão I1–I5 / exclusão X1–X4 binárias** — plataforma organoide-príon publicada · BSL-príon certificada · capacidade ≥64 organoides com controle de lote · aceitação de pré-registro/kill-switch · formalização ≤6 meses; vetos: sem biossegurança, sem cegamento, IP exclusiva, indisponibilidade >12m;
3. **Pesos congelados A–H** (25/15/15/10/10/10/10/5 — plataforma, track príon, capacidade, braço A5, braço A7, co-localização BR/E200K, open-science, prontidão), âncoras 0–5, "?" não pontua por regra;
4. **Fluxo PRISMA-regenerável** (identificados→dedup→triagem→pontuação→contato sequencial por score; desempate = plataforma) com log datado e público;
5. **Aplicação-piloto** (log v0.2): demonstra executabilidade — 9 registros → 8 grupos → 2 elegíveis + 1 condicional + 3 watchlist + 2 técnicos; o método corrigiu o prior (peso do eixo D em Calgary à luz do JCI 2026); o piloto **não decide** — as ordens que emite são saídas do método para o executor futuro [claim:C053] [evidence:E033].

Replicabilidade posterior: qualquer pesquisador re-executa as strings, re-tria, re-pontua; divergências >10 pts viram auditoria, não erro. Viés declarado: single-rater v1 (co-rating pré-declarado como pendência).

## 6. M5 — Infraestrutura de continuidade (guardião + runbook)

Toda superfície de manuscrito é gated por revisão hostil recursiva (R0 drift estrutural · R1 checklist+baterias · R2 recursão de emendas · R3 interrogação epistêmica + registro {{TODO:id:desc}}); o decálogo vivo (tiers de dado · locked-stays-locked · ilustrativo≠evidência · paridade · anti-hindsight · fim-de-sessão=/RECAP) está no guardian.md com comandos copy-paste — a continuidade não depende de memória de quem continua, e sim de método documentado — índice-mestre no KNOWLEDGE_CANON.md.

## 7. Promessas e limites desta Parte 2

Promete: método completo, replicável e em parte já demonstrado (M1 executado; M4 piloto) para dar continuidade à tese por estimativa computacional — como a física, sem parar à espera de cada confirmação. **Não promete**: seleção de parceiro (execução externa), dado [ORGANOID]+ (não existe ainda — e é rotulado como tal), nem qualquer claim clínica (escada de tiers: nenhum degrau empresta a autoridade do seguinte). Limites declarados: pesos e scores são julgamento estruturado single-rater; a calibração do estimador é na grade atual (refinamento futuro = grade mais fina, pré-declarado); PubMed-direto e identificação R8 pendem como conformidade do piloto.

## Referências (herdam da Parte 1 + artefatos próprios)

Parte 1: release v3.0 (manuscritos EN/PT + harness 38 fontes · 51 claims · 43 N-fatos). Próprias: `experiments/part2_results/part2_theta_obs_{v1,pooled,v11}.json` (calibração/pooled/rejeição) · `experiments/G0_EXECUTION_FREEZE_CHECKLIST.md` · `experiments/REPARAM_LOOP.md` · `experiments/PARTNER_SELECTION_PROTOCOL.md` v2.1 + `partner_selection_log.md` v0.2 · `guardian.md` (runbook/decálogo). Claims novas desta Parte: C052 (estimador calibrado/regime pooled/v1.1 rejeitada) · C053 (método de seleção como metodologia de tese; piloto não-decide) — registro em claims.csv/claim_texts.md.

---
*Parte 2 [SEM ANO] — o resultado define; as fases são estimativas. Toda cifra deste manuscrito vem de JSON arquivado ou do registro E (regra: nunca digitar valor). Gated: guardian R0–R3, 0 BLOCKED exigido.*
