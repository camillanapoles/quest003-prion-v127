# THESIS ROADMAP — Contenção V127 até os Resultados Finais (PLANO, não claim) · **TESE [START YEAR - Y0]**
## Documento de planejamento de continuidade da tese — Quest 003 (v2 · Y0-08-27)

**TESE [START YEAR - Y0] — o objetivo é o RESULTADO.** A tese não tem ano: é definida por resultados. Primeiro, colher os RESULTADOS FINAIS que a simulação traz [SIM] (dados reais parametrizados, até o fim do arco em ambiente simulado — detalhado na §3.5 do manuscrito); depois, validar gate a gate [ORGANOID]→[MOUSE]→[HUMAN]. As janelas abaixo são ESTIMATIVAS de fase para planejamento de recursos — jamais promessas de calendário. O horizonte que atrai mais pesquisa é o resultado quantitativo, não a data.

**Natureza epistêmica:** este é um PLANO DE VOO, não um manuscrito. Pertença à faixa de planejamento (exenta dos gates de manuscrito do guardião por desenho — ver guardian.py PLAN_DOCS). O guardião não bloqueia ambição aqui; ele bloquearia apenas o VAZAMENTO de claims de descoberta para o manuscrito antes dos gates. As probabilidades citadas são as do frame bayesiano auditado: P(desaceleração clínica)=5% empírica / 30–45% condicional aos gates.

---

## ARQUITETURA DA TESE — duas partes unidas na junção G0 (claim C049)

| | **PARTE 1 — pré-G0** (este manuscrito) | **PARTE 2 — pós-G0** (tese de continuidade) |
|---|---|---|
| Conteúdo | pesquisa, achados, simulação parametrizada, regras de design, quadros de probabilidade, benefícios | pesquisa E validação usando os dados parametrizados da simulação como substrato de trabalho |
| Gatilho | G0-sim executado & passado [SIM] | G0-wet produz [ORGANOID] → realimenta os modelos |
| Método | colheita final [SIM] + especificação completa do G0 (braços, SAP, estimador, kill) | estimador θ_obs consome a grade-κ da simulação; braços/doses/posições escolhidos pelas regras; loop realimenta parâmetros |
| Por que insustentável sozinha | design não-exercido: simulação sem validação consome a própria autoridade | experimentação sem prior quantitativo desperdiça os recursos que diz respeitar |

**A junção é o G0 — por isso sua declaração (§3.5), estimador (§2.7), plano estatístico (§2.5) e critérios de morte estão especificados ANTES de qualquer wet-lab existir.** A escolha de ONDE medir segue a mesma disciplina: protocolo SLR-análogo de seleção de parceiro (critérios de inclusão/exclusão binários, pesos congelados 25/15/15/10/10/10/10/5, vetos absolutos, fluxo PRISMA-like com log público) — `experiments/PARTNER_SELECTION_PROTOCOL.md`. A Parte 2 operacionaliza a inovação metodológica: previsibilidade e antecipação de informação para design terapêutico — decidir o que medir, onde, em que dose, antes de gastar qualquer recurso wet-lab.

## A LADDER ATÉ OS RESULTADOS (condicional, gate a gate — estimativas de fase)

**Nomenclatura por meio (claim C047):** G0-sim [SIM] (executado) → G0-wet [ORGANOID] (especificado) → G1 [MOUSE] (condicional) → G2 [HUMAN] (condicional). Todo dado do programa é rotulado pelo tier do gate que o produziu; até G0-wet existir, todo output novo é [SIM] — simulação parametrizada auditada, usada como resultado no seu tier, nunca como dado medido.

| Janela | Gate/Entrega | Critério objetivo | Se GO | Se NO-GO |
|---|---|---|---|---|
| **Y0 Q3–Q4** | v5 público (bioRxiv) + harness fechado (E034-38, sweeps expoente/C₅₀/same-mass, θ_obs estimator v1, search_log) | gate PASS mantido; zero BLOCKED | credibilidade metodológica estabelecida | — (já assegurado pela arquitetura) |
| **Y0 Q4** | Lab outreach B1 (USP > Butantan > Einstein; pacote pronto + **G0_UNLOCK_DOSSIER.md** — argumentário de liberação ao comitê baseado no G0-sim validado) | 1 lab parceiro assinado para G0-wet | G0-wet em produção | ampliar para labs internacionais (Caughey/NIH circle) |
| **Y1 H1** | **G0-wet executado** (8 braços, n=8–12; readouts 90–120 d) | θ_obs medido; gradiente proximal/distal por braço | θ_obs<0.33 ⇒ contenção confirmada in situ; manuscrito v7 c/ dado organoide → submissão A1 candidata | critério de morte programática dispara; negative-result publicado (contribuição metodológica permanece) |
| **Y1 H2** | G1 camundongo humanizado (se G0 GO) | sobrevida/gradiente in vivo | pacote pre-IND aberto (Anvisa/FDA) | pivot acelular (A6≈A5 rule) |
| **Y2** | **Contensão de classe-descoberta**: programa first-in-human compassivo E200K (se G1 GO) + paper A1 (organoide+camundongo+quadro probabilístico completo) | sinal modificador de doença (NfL/clínico) | **ARC-Y2: descoberta candidata** — primeira terapia modificadora em doença priônica, com cálculo de entrega quantitativo | arco metodológico já publicado independente do desfecho |

## POR QUE ESTE ARCO É DE CLASSE-DESCOBERTA (argumento de planejamento)

1. **Nenhum dos 6 candidatos falidos tinha**: modelo quantitativo de entrega, thresholds pré-registrados, revisão sistemática corrigindo o registro de citações, kill-switch programático. O nosso tem — travado e público.
2. **O arco evolutivo→terapia** (kuru → DN → cálculo → gate → clínica) é a estrutura de descoberta translacional clássica (Hla/Vane-style); prions têm 2 Nobéis e o terceiro slot aberto é terapia.
3. **Se confirmado**, o resultado é o PRIMEIRO disease-modifying em qualquer doença priônica + framework de contenção transferível a AD/PD (>50M) — envergadura de campo, não de paper.
4. **Honestidade estrutural**: P=5% empírica hoje; a ambição aqui é de PLANEJAMENTO (para onde apontar recursos), não de EXPECTATIVA (o que prometer). O guardião mantém essa separação à força nos manuscritos.

## ASSEGURANDO QUE O GUARDIÃO NÃO BLOQUEIA ESTE PLANO

- `guardian.py` opera sobre superfícies de manuscrito (md/tex). Este roadmap é **PLAN_DOC** — fora do escopo dos gates por desenho; a ambição STARTA-YEAR +2 é legítima AQUI.
- A única regra da faixa: claims de descoberta só entram no manuscrito APÓS o gate correspondente passar. O roadmap os marca como condicionais (tabela acima faz isso linha a linha).
- Continuidade: este arquivo é citado no KNOWLEDGE_CANON (continuidade) e atualizado a cada gate.

## MÉTRICAS DE PROGRESSO Y0→Y2

- harness: E034–E038 elevadas · sweeps rodados · θ_obs v1 congelado
- wet-lab: nº braços executados / 8 · labs parceiros: 0→1
- publicações: v5 (Parte 1, release v3.0 ✓) → v6 (Parte 2/ACP ✓ PR#2 aberto) → v7 (dado organoide, condicional ao G0-wet) → A1 (organoide+mus)
- reputação metodológica: citações do harness; adoção por terceiros


## ESTADO ATUAL DO PLANO (Y0-08-28)
- **Parte 1**: FECHADA — release v3.0 (PR#1 merged); manuscritos v5 EN+PT 51=51; gates 0/0.
- **Parte 2**: v6 — manuscrito próprio (md+PDF; PR #2, branch paper-v6): **ACP nomeada (C054; P0–P6)**; Base de Validade §1-bis (linhagem, check BLOCKED); **M2 (freeze/GATE-F) DORMANT por recorte da autora** (metodologia-somente: a tese não seleciona nem executa — portas abertas, não pendências); M4 = método SLR-análogo (piloto não-decisório, PubMed-direto conforme Q1=23/Q2=2); estimador θ_obs calibrado (v1.1 rejeitada honestamente).
- Registro: 54 claims · 38 fontes · 48 N-fatos · gates part1+part2 0/0 · canon 42 achados.
- Pendências: autora (PARTE2-V2-VALIDACAO; BIORXIV-ADDENDUM); agente (COST-DECOMP opcional); lab (GATEF, dormant).
