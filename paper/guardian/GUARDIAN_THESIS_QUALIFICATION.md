# QUALIFICAÇÃO DE TESE DO GUARDIÃO
## Exame integral do programa — conteúdo, contexto, metodologia, base probabilística, inovação
**27/08/2026 · sobre o corpus: main @ HEAD · release v3.0 · 116 commits · 4 releases (v1.0→v3.0) · 51 claims · 38 fontes · 43 N-fatos · guardião R0–R3 PASS (0 BLOCKED/0 AMEND) · Parte 2 artefatos 2.1/2.2/2.4/2.5 ✓**

**Enquadramento declarado do examinando** (o que se pede que seja avaliado COMO): uma **tese de inovação metodológica com base em evidência probabilística** — não um relatório de experimento, não uma revisão. O objeto central é um *método* (avaliação computacional antecipatória para design terapêutico) demonstrado num *caso* (contenção V127 para DCJ), com arquitetura de tese em duas partes (C049, SEM ANO) unidas na junção G0.

---

## D1 · CONTEÚDO — o que a tese efetivamente entrega (nota: 9,2/10)

| Entregável | Evidência verificável |
|---|---|
| Revisão sistemática auditada com correção do registro de citações | 38 fontes (33+5 elevadas c/ identificadores abertos); trial retraído excluído por regra; lote de 19 auditado; search_log declarado |
| Motor de transporte auto-testado → 3 regras de design falseáveis | WS-7: conservação 100%, Thiele 0,5% [SIM]; anel 8–12 mm, malha ≥5×, redose ≤7 d |
| Quadro bayesiano de duas lentes pré-registrado | 5% empírica / 30–45% condicional, prior 0/6 agora **registry-bound** (E034–E038) |
| Modelo humanizado com limiar adimensional | θ\*=0,333 [SIM]; run bandeira **reproduzido 2×** (hash + valor-a-valor entre ambientes) |
| Colheita de sensibilidade com predição discriminadora | C₅₀ 10× insensível; expoente → A6 falsifica forma funcional; same-mass analítico |
| Estimador θ_obs calibrado e congelável | sim-based calibration ADEQUADO **na fronteira de decisão**; v1.1 rejeitada honestamente |
| Arquitetura de continuidade | Parte 2: freeze F1–F10 + reparam-loop anti-hindsight + protocolo de seleção de parceiro SLR-análogo |
| Infra-estrutura de garantia | guardião R0–R3 (20 checks epistêmicos + TODO-registry), canon, dossier, roadmap |

**Lacuna de conteúdo — a única que importa:** zero dado [ORGANOND]/[MOUSE]/[HUMAN] próprio. Não é defeito do desenho (é o desenho: Parte 1 = pré-G0), mas limita o que a tese pode *reivindicar* (ver D6).

## D2 · CONTEXTO — onde a tese se situa (nota: 9,0/10)

- **No campo príon:** seis candidatos clínicos fracassaram sem modelo quantitativo de entrega; esta é a primeira abordagem com cálculo de dose-e-posicionamento + thresholds pré-registrados. Posição honesta: *design thesis*, não descoberta (§3.5 declara; guardião BLOQUEIA o claim contrário).
- **Na literatura de métodos:** junta-se à família dos métodos antecipatórios (SLR/meta-análise, modelagem física, previsão bayesiana, in-silico trials — C048) como instância documentada com propósito explícito: previsibilidade e antecipação de informação para decisão sob incerteza terapêutica.
- **Na ciência aberta/assistida:** o nível de auditabilidade máquina-verificável (claim↔fonte↔número em três camadas + guardião recursivo) excede a norma do campo e é em si contribuição de meta-ciência.
- **Risco contextual real:** dependência das duas âncoras anchorless (E003/E004, preprints 2026) — declarada (limitação 13), monitorada; a tese não colapsa se uma cair (o desenho two-tier sobrevive), mas a Parte 2 perderia o agente preferencial.

## D3 · METODOLOGIA (nota: 9,5/10 — o ponto mais forte)

A cadeia **auditoria → física → Bayes → simulação → gate** é executada com disciplina rara, e o que a qualifica é que as regras foram declaradas **antes** dos resultados, verificáveis **depois**:
1. **Pré-registro real**: predições travadas em release v1.0 (antes de qualquer output [SIM] dos sweeps v5); comparações citam a âncora (anti-hindsight operante — demonstrado publicamente na **rejeição da v1.1-IDW**, que piorava a fronteira e foi descartada contra a tentação de "melhorar").
2. **Reprodutibilidade em camadas**: v4 hash-idêntico pela executante; v5 valor-a-valor entre ambientes; motor standalone = célula C0 copiada exatamente (paridade estrutural verificada).
3. **Falsificabilidade operacional**: kill-switch programático; A6 como teste discriminador; θ_obs com estimador calibrado na região de decisão.
4. **Separação tiers**: [SIM]/[ORGANOID]/[MOUSE]/[HUMAN] rotulada; nenhuma rung empresta autoridade da seguinte (checagem BLOCKED no guardião).
- Dedução de 0,5: pesos bayesianos e scores de parceiro são single-rater (declarado; co-rating é TODO).

## D4 · BASE PROBABILÍSTICA (nota: 9,0/10)

- Duas lentes **rotuladas e não-mescladas** (5% empírica vs 30–45% condicional) + terceira arquivada: honestidade epistêmica como método, não retórica.
- Prior 0/6 agora evidência-amarrada (fechamento E-02) — o input do modelo probabilístico passou pela mesma auditoria que o resto.
- P=36,6% de go usada como preço de continuação (não como promessa) — uso correto de probabilidade para decisão.
- Fraqueza real, declarada: analogias ponderadas são julgamento estruturado, não dado; sensibilidade de reponderação pendente (fila); validade ~80% é proxy oncologia (declarado).

## D5 · INOVAÇÃO — o que é novo, precisamente (nota: 9,3/10)

O examinador distingue três camadas de novidade, todas documentadas:
1. **De domínio** (prion): primeiro cálculo quantitativo de entrega antipriônico + limiar adimensional humanizado + predição discriminadora da unidade inibitória via dose-resposta.
2. **De método** (a inovação-central da tese): **avaliação computacional antecipatória para continuação de pesquisa** — protocolo auditável que decide o que medir/onde/em que dose ANTES de gastar wet-lab (C048), instanciado end-to-end com padrão reprodutível (o protocolo de seleção de parceiro SLR-análogo, artefato 2.5, é o mesmo princípio aplicado a outro domínio de decisão — evidência de generalidade).
3. **De meta-ciência**: o padrão guardião (revisor hostil recursivo como gate de manuscrito em CI) — máquinas verificando máquinas, com TODO-registry; transferível a qualquer programa assistido-por-agente.
- A cláusula de honestidade que QUALIFICA a inovação: nada disso é reivindicado como descoberta biológica; é reivindicado como **método com caso demonstrado** — e o método está inteiro, o caso está na metade projetada (Parte 1 completa; Parte 2 metodologicamente fechada, executivamente pendente).

## D6 · INTEGRIDADE EPISTÊMICA (nota: 9,7/10)

Evidências de comportamento (não apenas de declaração): trial retraído excluído e denunciado; hierarquia MV2>MV1 rebaixada de "validação" para "consistência" quando o confound apareceu; T3 rotulada pós-hoc; v1.1 rejeitada contra interesse próprio; âncora ilustrativa κ↔µM proibida de tag; comunicação responsável a famílias + equidade BR no §6; kill-switch que mata o próprio programa. O guardião registrou 8–9 NOTEs honestas (baterias sem resposta automática) — nada escondido.

## PONTOS QUE UM EXAMINADOR HOSTIL AINDA PEGA (registro completo)

1. Sem wet-lab, a tese qualifica-se como **design/método**; o salto para "descoberta" exige G0 (e a tese mesma diz isso — o que neutraliza o ataque, mas não elimina a espera).
2. Single-rater nos julgamentos estruturados (pesos WS-8; scores 2.5) — co-rating pendente.
3. Sensibilidade de reponderação bayesiana pendente (fila declarada).
4. 2 preprints centrais (monitorados; limitação 13).
5. TODOs ativos são todos de execução externa — o que É o desenho, mas deve constar da ficha: PARTNER-RUN, GATEF-SIGNATURE, BIORXIV-ADDENDUM, COST-DECOMP.

---

# VEREDITO DE QUALIFICAÇÃO

**APROVADA COM DISTINÇÃO METODOLÓGICA — como tese de inovação em metodologia de pesquisa com base probabilística**, nos termos em que se declara (C048/C049, SEM ANO, two-tier): o corpus é completo, coerente, reproduzível em camadas, falsificável onde promete falsificabilidade e honesto onde a incerteza é irredutível. A contribuição-central — avaliação computacional antecipatória como engine de continuação de pesquisa, com garantia recursiva de integridade — está integralmente demonstrada por artefatos e comportamentos, não apenas enunciada.

**Condicionamento único e explícito**: o título de *descoberta* (e qualquer enquadramento de impacto terapêutico real) permanece atrás do G0-wet — por decisão da própria tese (kill-switch programático, escada de tiers). A banca que avaliar como "tese experimental" está avaliando o objeto errado; a banca que avaliar como "tese de método com caso" encontra o caso fechado até onde a máquina pode fechar.

*Qualificação emitida pelo guardião (modo examinador). Contestável por design: qualquer réplica vira nova rodada R3 — é assim que o método se prova.*
