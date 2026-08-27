# Plano de Continuidade Metodológica — Parte 2 da Tese
## Do dado parametrizado à validação gate-a-gate: G0-sim [SIM] → G0-wet [ORGANOID] → G1 [MOUSE] → G2 [HUMAN]

**Manuscrito Parte 2 · v1 · 2026-08-27 · PT-BR (mestre)**
Open Prion & Molecular Engineering Consortium — correspondente: Camilla N. (CRediT in-repo)
Companion da Parte 1 (manuscript_EN_v5/PT_v5, release v3.0) — **não a modifica**: cita-a, estende-a. Gated pelo guardião R0–R3 [claim:C046] [evidence:E032, E033].

---

## Resumo

**Por que [SEM ANO]:** a tese lida com **prognósticos obtidos de dados simulados**. Simulação opera, por natureza, em tempo futuro — independe do ano em que se esteja: a referência a ano não tem impacto sobre a tese, pois as predições são do tipo "o que acontece se", não "quando acontece". Por isso o horizonte temporal é declarado vazio por construção, e as durações de fase que porventura apareçam são apenas estimativas de planejamento, nunca promessas.

A Parte 1 demonstrou a tese de design: plataforma de contenção V127 quantitativamente dimensionada, com gate computacional G0-sim **executado, aprovado e reproduzido em dois ambientes** [claim:C046] [evidence:E032, E009, E007, E033], colheita de sensibilidade com predição discriminadora [claim:C051] [evidence:E032, E033] e estimador θ_obs com calibração por simulação com **veredito ADEQUADO por critérios pré-declarados na fronteira de decisão** [claim:C052] [evidence:E032, E033]. A Parte 2 **deste manuscrito** reenquadra a continuidade: **a base validada da tese são os próprios dados in-silico já realizados** — não a metodologia de validação por experimento humano. Os **resultados da tese são os resultados da simulação computacional já executada** (§2). O intuito é **gerar novas pesquisas, não fechar portas aguardando cenários futuros**: onde um valor razoável já existe, a pesquisa derivada prossegue imediatamente; onde algo dependeria de medição, entra como metodologia pré-declarada — e segue válido e não-prendente. O modo epistêmico é o da física teórica — previsibilidade e antecipação de informação (estimativas precedem, dirigem e valem até a medição — Parte 1 §4.1): o programa computacional não para à espera do wet-lab; tudo que tem publicação é usado como evidência direta; tudo que não tem entra como metodologia pré-declarada. A tese tem **[SEM ANO]**: definida por resultados, com durações de fase como estimativas de planejamento [claim:C047] [evidence:E032, E033]. Esta Parte 2 documenta **método somente** — nenhuma seleção de laboratório é feita aqui; a seleção é ato de execução, do executor futuro, guiado pelo método §5 [claim:C053] [evidence:E033].

## 1. Natureza e escopo

A Parte 2 é a **tese de continuidade** na arquitetura declarada (C049) — e o seu fundamento é a **base validada in-silico**: conforme aclamado antecipadamente, lidamos com dados simulados; o gate computacional G0-sim **executado, aprovado e reproduzido** [claim:C046] [evidence:E032, E009, E007, E033] É a validação da tese neste estágio. Isto não prende a pesquisa — ao contrário, a liberta para derivar novas pesquisas de cada valor razoável já obtido, sem aguardar cenários de confirmação. A tabela abaixo reenquadra os componentes M1–M5 **sob essa compreensão** (coluna direita) e **aguarda validação expressa da autora**:

| # | Componente (ferramenta) | Reenquadramento sob a base validada in-silico | Estado | Artefato |
|---|---|---|---|---|
| M1 | Estimador θ_obs | **instrumento da continuidade**: converte qualquer gradiente (simulado hoje; medido amanhã, se a autora quiser) em θ_obs comparável ao limiar travado | **executado e aprovado** (§2) | part2_theta_obs_{v1,pooled,v11}.json |
| R1 | Resultados como resultados | **os achados da simulação já realizada SÃO os resultados da tese** (§2-bis) — nada fica "pendente de lab" para valer | realizado | §2-bis + part2_derived_summary.json |
| M3 | Loop de re-parametrização | regra de como pesquisa derivada realimenta os modelos sem retro-alterar predições (anti-hindsight) — vale já entre cenários [SIM] | especificado | REPARAM_LOOP.md |
| M2 | Freeze/GATE-F (F1–F10) | **extensão futura OPCIONAL**: pronta e documentada caso a autora decida, um dia, estender ao [ORGANOID] — não é requisito da tese | especificado (dormant) | G0_EXECUTION_FREEZE_CHECKLIST.md |
| M4 | Seleção de parceiro (SLR-análogo) | **método documentado para replicabilidade** — sem seleção, sem contato; existe para quem, no futuro, escolher executar | método + piloto | PARTNER_SELECTION_PROTOCOL v2.1 + log v0.2 |
| M5 | Infraestrutura (guardião + runbook) | garantia de que a continuidade é por método, não por memória | operante | guardian.py + guardian.md |

> **⏳ VALIDAÇÃO EXPRESSA PENDENTE:** esta tabela (e o reenquadramento M1→R1/M2-dormant) só se torna definitiva do texto da tese com validação expressa da autora. {{TODO:PARTE2-V2-VALIDACAO:autora valida ou ajusta a tabela reenquadrada}}


## 1-bis. Base de Validade (MANDATÓRIA — exigência do guardião)

**Declaração tríade:** (i) esta tese é **baseada em simulação computacional e NÃO SUBSTITUI a validação de laboratório** — o laboratório é **essencial** para que a tese seja absorvida como real; (ii) a continuidade do estudo provém dos **prognósticos**: se os exames iniciais de laboratório (G0-wet [ORGANOID], e no futuro o humano) **equivalerem ao que foi simulado**, nós já possuímos **antecipação de dados e informações aplicáveis imediatamente** — essa é a metodologia da tese; (iii) o rigor exigido de uma tese experimental — como foi feito, por quem, com quais critérios, quais resultados — é aqui **convertido para o ambiente computacional**: cada dado tem linhagem completa declarada (quem produziu, em que espécie/sistema, validação cruzada por qual fonte independente, qual código simulou, como foi parametrizado para humano, qual resultado produziu).

**Linhagem dos dados (data lineage — o "métodos experimental" convertido):**

| Dado | Produzido por (primário) | Espécie/sistema | Validação cruzada (independente) | Simulado por (código) | Parametrização humana | Resultado [SIM] |
|---|---|---|---|---|---|---|
| Cinética de replicação do prião | Fornara/Igel 2024, iScience, código aberto [E009] | camundongo | Masel 1999 (polimerização nucleada) [E011] | kernel reação–difusão (Zenodo 11093945) portado [C013] | relógio calibrado às âncoras humanas | θ\*=0,333 [C038] |
| Relógio e amplitude humanos | Groveman 2019, Acta Neuropathol [E007] | organoide humano sCJD | Groveman 2021 (ensaio de droga na mesma plataforma) [E008]; subtipos 2023 (RML) | regressão de duplicação (12,1 d; 144 d/unid) [C037] | direto (já humano) | predição travada θ<0,33 [C040] |
| Transporte intersticial | Thorne & Nicholson 2006, PNAS (IOI in-vivo) [E010] | humano (in-vivo) | Stokes–Einstein (físico-química, derivação auditável) | solver ADR auto-testado [C032] | direto (já humano) | regras 1–3 [C033][C034][C035] |
| Agente V127 anchorless | Asante 2015 Nature [E001] · Gatdula 2026 [E003] · Zerbes 2026 [E004] | população→camundongo→cultura→AAV in-vivo | quatro níveis independentes de evidência | termo de capping freeS | dose ↔ κ (âncora ilustrativa; A6 fecharia) | contenção em κ=2 [C038] |
| Prior de falhas clínicas | Geschwind 2013 · Haïk 2014 · Newman 2014 · Otto 2004 · Mead 2022 · Cheng 2015 [E034–E038, E022] | humano (ensaios clínicos) | registry-bound, identificadores abertos | Beta–Binomial WS-8 [C036] | direto | P=5%/30–45% duas lentes |
| Sensibilidade estrutural | (este programa) | in-silico | motor reproduzido 2× ambientes (hash+valor) | sweeps S1/S2 + estimador | — | predição discriminadora [C051] |

**Por que isto é ciência com referências sólidas:** toda célula da linhagem amarra a fonte peer-reviewed ou ao run arquivado com hash; nenhum número vive fora do registro (51 claims · 38 fontes · 48 N-fatos · 4 validadores em zero); o código é aberto e o guardião audita máquina-a-máquina — a cadeia **quem→espécie→cruzamento→código→parâmetro→resultado** é verificável de ponta a ponta, exatamente como um "métodos" experimental exige, só que executada em ambiente computacional e declarada com a mesma disciplina.

## 2-bis. Os resultados da tese são os resultados da simulação já realizada

Em vez de laboratório ou teste humano, **o que valida e compõe a tese neste estágio é o conjunto computacional executado** — completo, arquivado e reproduzido: (i) limiar de contenção θ\*=0,333 com relógio humanizado [claim:C038] [evidence:E032]; (ii) três regras de design falseáveis [claim:C033] [evidence:E030] [claim:C034] [evidence:E030, E020] [claim:C035] [evidence:E030, E019]; (iii) colheita de sensibilidade com predição discriminadora (C₅₀ 10× insensível; forma funcional falseável por dose-resposta) [claim:C051] [evidence:E032, E033]; (iv) quadro probabilístico de duas lentes com prior registry-bound [claim:C036] [evidence:E031]; (v) estimador θ_obs calibrado no regime declarado [claim:C052] [evidence:E032, E033]; (vi) reprodução independente em dois ambientes (hash + valor-a-valor); e (vii) a **tabela-decisão derivada** (κ↔θ_obs↔frente↔biomassa↔margem) extraída sem nova simulação — que mostra a margem de raio saturando cedo (70,2% já em κ=1,5) e confirma a **razão de biomassa como coordenada informativa** (48→1,25), com θ\*=0,333 como variável-de-decisão pré-registrada [claim:C052] [evidence:E032, E033]. De cada valor razoável aqui, **pesquisa derivada já pode prosseguir** — portas abertas.

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
