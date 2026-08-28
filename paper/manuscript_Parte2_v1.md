# PARAMETRIZAÇÃO COMPUTACIONAL PARA CONTINUIDADE DE PESQUISA EM DOENÇAS PRIÔNICAS: O MÉTODO ACP APLICADO À PLATAFORMA TERAPÊUTICA PrP-V127
## Parte 2 da Tese — Continuidade Metodológica Realizada

---

**AUTORA:** Camilla N. *(correspondente)* — {{TODO:TESE-FICHA:programa de pós-graduação, área de concentração, orientadora e coorientadora — preencher}}
**DOCUMENTO:** Parte 2 da tese (companion validado da Parte 1, release v3.0) · v1 · 2026-08-28
**NATUREZA:** tese baseada em simulação computacional — G0 validado por simulação; dados reais de pesquisa em ambiente simulado; forma experimental análoga (§ "mapeamento análogo")

---

## RESUMO

**Introdução.** Doenças priônicas são 100% fatais e seis candidatos clínicos fracassaram sem modelo quantitativo de entrega. A Parte 1 desta tese construiu, por auditoria sistemática, física de transporte, calibração bayesiana e simulação humanizada, uma plataforma de contenção terapêutica (PrP-V127) com limiar adimensional θ*=0,333 — executada, aprovada e reproduzida em dois ambientes computacionais. **Objetivo.** Esta Parte 2 formaliza e realiza a continuidade: (i) nomeia e formaliza o método de pesquisa que a sustenta — a ACP (Antecipação Computacional Parametrizada), passos P0–P6; (ii) estabelece a Base de Validade com linhagem completa de cada dado (quem→espécie→validação cruzada→código→parametrização→resultado); (iii) declara a tese em forma experimental análoga, na qual o sujeito da pesquisa é o conjunto papers+fontes+código+simulação; (iv) entrega os resultados da tese como os próprios achados [SIM] já executados; e (v) documenta, como método replicável, a seleção futura de parceiros (SLR-análogo) sem executá-la. **Método.** ACP P0–P6 sobre base E-registrada (38 fontes), motores determinísticos auto-testados (conservação de massa 100%; erro de Thiele 0,5%), colheita sob critérios pré-declarados, prognósticos travados por release antes de qualquer medição, estimador θ_obs calibrado por simulação (veredito pré-declarado; fronteira de decisão com bias −0,008; v1.1 interpolada testada e rejeitada), guardião recursivo R0–R3 em dois perfis de superfície. **Resultados.** Limiar θ*=0,333; três regras de design; colheita de sensibilidade com predição discriminadora (C50 insensível em faixa 10×; forma funcional falseável por dose-resposta); quadro probabilístico de duas lentes com prior registry-bound; tabela-decisão derivada κ↔θ↔frente↔biomassa (margem de raio satura cedo; biomassa é a coordenada informativa); registro de 54 claims, 38 fontes, 48 fatos numéricos com validação por máquina. **Conclusão.** A tese está realizada nos termos da ACP: continuar pesquisa por simulação parametrizada sem substituir o laboratório — se dados reais futuros forem análogos aos simulados, os passos seguintes já estarão avançados (P6, antecipação bancada).

**Palavras-chave:** príons; simulação computacional; Antecipação Computacional Parametrizada; PrP-V127; doença de Creutzfeldt-Jakob; metodologia de pesquisa; in-silico.

## ABSTRACT

*(companion EN — manuscript_Parte2_v1_EN.md; keywords: prions; computational simulation; Parameterized Computational Anticipation; PrP-V127; Creutzfeldt-Jakob disease; research methodology; in-silico)*

## SUMÁRIO

1. **INTRODUÇÃO** (este capítulo)
2. **FUNDAMENTAÇÃO — o campo dos métodos antecipatórios e dos in-silico trials** *(a completar — Ciclo 2: revisão estruturada com as 38 fontes formatadas ABNT)*
3. **METODOLOGIA — o método ACP** *(conteúdo consolidado: método nomeado P0–P6; Base de Validade com linhagem; tese em forma experimental — mapeamento análogo)*
4. **RESULTADOS — os resultados da tese são os resultados da simulação** *(conteúdo consolidado + figuras próprias — Ciclo 4)*
5. **COMPONENTES E CONTINUIDADE** *(M1–M5 reenquadrados; seleção de parceiro como método)*
6. **DISCUSSÃO E CONCLUSÕES POR OBJETIVO** *(Ciclo 4)*
REFERÊNCIAS · APÊNDICES (inventário de artefatos)

## LISTA DE SIGLAS

ACP — Antecipação Computacional Parametrizada · θ — fração de replicação remanescente no pico secretor, θ≡(1+κ·c_pico)⁻¹ · κ — força de capping · G0-sim/G0-wet — gates computacional/organoide · T1/T2/T3 — níveis de aceitação · [SIM]/[ORGANOID]/[MOUSE]/[HUMAN] — tiers de dado · SLR — revisão sistemática de literatura · WB — western blot · PPS — pentosan-polissulfato · CrI — intervalo de credibilidade

---

# CAPÍTULO 1 — INTRODUÇÃO

> ## PRODUTO FINAL — ESTA É A TESE (declaração de abertura)
> **Este manifesto (v6) é a tese realizada.** A Parte 1 produziu os achados (manifesto v5, release v3.0); o **G0 foi validado por simulação computacional** — executado, aprovado e reproduzido em dois ambientes; e a **continuidade está realizada** nos termos da ACP (P0–P6). Os dados são **reais de pesquisa**: cinética murina publicada [E009], dados de organoide humano publicados [E007], parâmetros de transporte humano in-vivo [E010], código aberto — **parametrizados para humanos e executados em ambiente simulado**, o que garante **aproximação e expectativa quantitativas** (prognóstico falseável) sem reivindicar medição. As claims são reais e registry-bound; o ambiente é simulado; a tese é o produto. **Guardião-2 atesta** como revisor hostil nas quatro dimensões: metodologia, dados, conformidade e conteúdo.

**Por que [SEM ANO]:** a tese lida com **prognósticos obtidos de dados simulados**. Simulação opera, por natureza, em tempo futuro — independe do ano em que se esteja: a referência a ano não tem impacto sobre a tese, pois as predições são do tipo "o que acontece se", não "quando acontece". Por isso o horizonte temporal é declarado vazio por construção, e as durações de fase que porventura apareçam são apenas estimativas de planejamento, nunca promessas.

### 1.1 Problema

A pesquisa translacional em doenças raras fatais paralisa-se num dilema: sem dado clínico não há financiamento; sem previsão quantitativa, o dado clínico é desperdiçado. Nos príons, esse dilema produziu seis fracassos clínicos sequenciais sem modelo de entrega que os orientasse. A Parte 1 resolveu a metade quantitativa (cálculo de contenção com limiar travado); resta o problema da **continuidade**: como uma tese avança **hoje**, com método, quando a validação de laboratório é essencial mas não é pré-requisito para produzir conhecimento?

### 1.2 Justificativa

Três razões. (i) **Epistêmica**: simulação parametrizada com dados reais publicados é prognóstico — opera em tempo futuro e não depende de ano; interrompê-la à espera de confirmação reduziria a produção de conhecimento (como a física teórica não esperou testar cada predição). (ii) **Ética/econômica**: cada experimento wet-lab desperdiçado em príon custa meses e recursos escassos; decidir *o que medir, onde e em que dose antes de gastar* é responsabilidade metodológica. (iii) **Metodológica**: as ferramentas (revisão sistemática auditável, código aberto, bayesiana hierárquica, pré-registro) hoje permitem rigor documental equivalente ao experimental — faltava formalizá-lo como método com nome e passos.

### 1.3 Questões de pesquisa

- **Q1.** É possível formalizar um método de continuidade de pesquisa por simulação computacional com o mesmo rigor documental de uma tese experimental?
- **Q2.** Esse método, aplicado ao caso V127, produz resultados próprios (não meros planos) com validade declarada e linhagem completa?
- **Q3.** Como tal método se posiciona e se diferencia da família existente de métodos antecipatórios (meta-análise, in-silico trials)?

### 1.4 Objetivos

**Geral.** Formalizar, demonstrar e documentar a ACP — Antecipação Computacional Parametrizada — como método de continuidade de pesquisa por simulação, realizando a Parte 2 da tese sobre os achados da Parte 1: previsibilidade e antecipação de informação para decisão de pesquisa (o que medir, onde, em que dose, antes de gastar recurso).

**Específicos.**
- **OE1** — Nomear e formalizar a ACP com passos P0–P6 e garantias por passo [claim:C054] [evidence:E009, E010, E031, E032, E033, E007].
- **OE2** — Estabelecer a Base de Validade: tríade declarada + linhagem completa dos dados (Cap. 3) [claim:C046] [evidence:E032, E033].
- **OE3** — Entregar os resultados da tese como os achados [SIM] realizados: limiar, regras, sensibilidade, probabilístico, estimador [claim:C038] [evidence:E032] [claim:C051] [evidence:E032, E033] [claim:C052] [evidence:E032, E033].
- **OE4** — Documentar a continuidade futura como método replicável (loop de re-parametrização; seleção de parceiro SLR-análogo; freeze dormant) sem executá-la [claim:C053] [evidence:E033].
- **OE5** — Submeter o conjunto a revisão hostil de máquina (guardião R0–R3, dois perfis) e validação expressa da autora.

### 1.5 Hipóteses

- **H1 (metodológica).** A ACP é formalizável com rigor documental equivalente ao experimental — *predição discriminadora*: um examinador de tese experimental consegue auditá-la trocando apenas os termos do mapeamento análogo (§ Cap. 3) sem perdê-la.
- **H2 (de caso).** A aplicação ACP ao caso V127 gera resultados próprios falsificáveis independentes de medição — *predições travadas desde o release v1.0*: θ<0,33 ⇒ contenção; C50 insensível 10×; dose-resposta do braço A6 distingue a forma funcional do capping [claim:C051] [evidence:E032, E033].
- **H3 (de posicionamento).** A ACP ocupa espaço estrutural distinto dos in-silico trials (que simulam o ensaio): prognóstico travado antes da medição; simulação rotulada; antecipação bancada; pesquisa derivada imediata.

### 1.6 Estrutura do documento

Cap. 2 fundamentação (Ciclo 2) · Cap. 3 metodologia (ACP; Base de Validade; mapeamento análogo) · Cap. 4 resultados [SIM] · Cap. 5 componentes e continuidade · Cap. 6 discussão e conclusões por objetivo (Ciclo 4) · Referências completas (Ciclo 2) · Apêndices.

---

### 1.7 Componentes M1–M5 (tabela validada pela autora) e natureza do escopo

A Parte 2 é a **tese de continuidade** na arquitetura declarada (C049) — e o seu fundamento é a **base validada in-silico**: conforme aclamado antecipadamente, lidamos com dados simulados; o gate computacional G0-sim **executado, aprovado e reproduzido** [claim:C046] [evidence:E032, E009, E007, E033] É a validação da tese neste estágio. Isto não prende a pesquisa — ao contrário, a liberta para derivar novas pesquisas de cada valor razoável já obtido, sem aguardar cenários de confirmação. A tabela abaixo reenquadra os componentes M1–M5 **sob essa compreensão** (coluna direita) e **aguarda validação expressa da autora**:

| # | Componente (ferramenta) | Reenquadramento sob a base validada in-silico | Estado | Artefato |
|---|---|---|---|---|
| M1 | Estimador θ_obs | **instrumento da continuidade**: converte qualquer gradiente (simulado hoje; medido amanhã, se a autora quiser) em θ_obs comparável ao limiar travado | **executado e aprovado** (§2) | part2_theta_obs_{v1,pooled,v11}.json |
| R1 | Resultados como resultados | **os achados da simulação já realizada SÃO os resultados da tese** (§2-bis) — nada fica "pendente de lab" para valer | realizado | §2-bis + part2_derived_summary.json |
| M3 | Loop de re-parametrização | regra de como pesquisa derivada realimenta os modelos sem retro-alterar predições (anti-hindsight) — vale já entre cenários [SIM] | especificado | REPARAM_LOOP.md |
| M2 | Freeze/GATE-F (F1–F10) | **extensão futura OPCIONAL**: pronta e documentada caso a autora decida, um dia, estender ao [ORGANOID] — não é requisito da tese | especificado (dormant) | G0_EXECUTION_FREEZE_CHECKLIST.md |
| M4 | Seleção de parceiro (SLR-análogo) | **método documentado para replicabilidade** — sem seleção, sem contato; existe para quem, no futuro, escolher executar | método + piloto | PARTNER_SELECTION_PROTOCOL v2.1 + log v0.2 |
| M5 | Infraestrutura (guardião + runbook) | garantia de que a continuidade é por método, não por memória | operante | guardian.py + guardian.md |

> **✓ VALIDAÇÃO EXPRESSA DA AUTORA — REGISTRADA (28/08, no commit do merge do PR #2):** a tabela reenquadrada (M1→R1/M2-dormant/M4-método), a Base de Validade §1-bis, o inventário §8 e a declaração PRODUTO FINAL foram validadas expressamente e são definitivas.

# CAPÍTULO 2 — FUNDAMENTAÇÃO

### 2.1 Doenças priônicas: o gargalo terapêutico que motiva a continuidade

As doenças priônicas humanas são neurodegenerativas, transmissíveis e universalmente fatais; a forma esporádica (sCJD) mata em meses. A base molecular do programa — a variante G127V selecionada pela epidemia de kuru [6], a resistência completa do homozigoto V127 [1], a ressalva do heterozigoto (infectável por vCJD) [1], o efeito dominante-negativo dose-dependente [1][3][5] e sua persistência em trans sem âncora GPI [3] com prova-de-conceito AAV in vivo [4] — constitui o núcleo validado em quatro níveis (população→camundongo→cultura→gene-terapia). O gargalo histórico éterapêutico, não mecanístico: **seis candidatos clínicos fracassaram sem modelo quantitativo de entrega** — quinacrina [35], doxiciclina [36], pentosan-polissulfato intraventricular [37], flupirtina [38], PRN100 [34] e minociclina [33] (com o ensaio retraído [21] excluído por regra) — todos agora **registry-bound** (concordância completa no fim deste documento). A plataforma organoide humana [7][8] fornece as âncoras que humanizam o relógio da simulação; a cinética murina publicada com código aberto [9] e o transporte intersticial humano in vivo [10] completam a base paramétrica.

### 2.2 A família dos métodos antecipatórios e os in-silico trials

A agregação do publicado (meta-análise/revisão sistemática), a derivação física (modelagem de transporte) e a execução de cenários (in-silico trials) formam a família de métodos que decidem sob incerteza antes do dado. Os in-silico trials consolidaram-se como campo — com workflows formais (CORTÉS-RÍOS et al., 2025, PMCID PMC12706418; verificação completa pendente) e ferramentas abertas de validação de coortes virtuais (doi:10.1038/s41598-025-99720-3) — e simulam **o ensaio**: pacientes virtuais, desenho, vias regulatórias.

### 2.3 Posicionamento da ACP (corroborando H3)

A ACP ocupa o espaço complementar: simula **a continuação da pesquisa**, distinta por quatro diferenciais estruturais — (i) prognóstico travado por release **antes** da medição (anti-hindsight como requisito, não virtude); (ii) simulação rotulada em toda saída (tiers); (iii) P6: dado real análogo ⇒ antecipação **bancada**; (iv) P5: pesquisa derivada imediata como produto de primeira classe. A herança metodológica é explícita: a tese emerge da própria pesquisa (Parte 1) e **herda sua lógica e suas claims** — corroborando-as e ampliando com o que somar (fontes complementares em verificação).

### 2.4 Síntese

O campo oferece mecanismo validado em quatro níveis [1][3][4][5], plataforma de âncora humana [7][8], parâmetros de transporte in vivo [10], cinética aberta [9] e um registro de fracassos que calibra honestamente o prior [33–38] — e a família de métodos oferece os instrumentos. O que faltava — e esta tese fornece — é o método nomeado que converte esse acervo em continuidade.

---

# CAPÍTULO 3 — METODOLOGIA

### 3.1 O método nomeado: ACP — Antecipação Computacional Parametrizada (*Parameterized Computational Anticipation*)

O que a Parte 2 formaliza **é um novo método de pesquisa**: nos dias atuais, é possível **continuar pesquisa por simulação** — com dados publicados e validados como insumo, execução determinística auditável e prognósticos travados antes de qualquer medição — sem que isso substitua ou espere o laboratório. **Declaração de eixo retórico (obrigatória em toda a Parte 2):** tudo aqui **é simulação, e é dito que é**; não prometemos aplicar nem validar na Parte 2 — antes: **se dados reais vierem a exibir resultados análogos aos simulados, os passos seguintes já terão sido dados** — a antecipação estará bancada, não pendente [claim:C054] [evidence:E009, E010, E031, E032, E033, E007].

**Passos formais do método (P0–P6):**

| Passo | Nome | Entrada | Procedimento | Saída | Garantia |
|---|---|---|---|---|---|
| P0 | identificação | pergunta focal | SLR auditada de dados publicados validados (espécie, sistema, fontes cruzadas) | base de insumos com E-IDs | linhagem completa (§1-bis) |
| P1 | parametrização | base E-registrada | derivação física/estatística com proveniência por parâmetro | modelos parametrizados | cada número amarra a fonte |
| P2 | execução | modelos | motores determinísticos, código aberto, self-tests | runs arquivados [SIM] | reprodução entre ambientes |
| P3 | colheita | runs | critérios de aceitação pré-declarados | resultados [SIM] + margens | veredito sem meta móvel |
| P4 | prognóstico | resultados | predições travadas por release antes de qualquer medição | limiares/decision-table | âncora anti-hindsight |
| P5 | pesquisa derivada | valores razoáveis | novas perguntas/produtos derivam **imediatamente** (portas abertas) | agenda derivada [SIM] | geração, não espera |
| P6 | confronto (opcional) | dados reais futuros, **se existirem e forem análogos** | comparação à âncora travada (nunca retreino) | passos seguintes **já avançados** | antecipação bancada |

**Posição na família (related-work):** o campo dos *in-silico trials* é estabelecido (simulam **o ensaio**: pacientes virtuais, desenho, via regulatória). A ACP ocupa o espaço adjacente e complementar: simula **a continuação da pesquisa**, distinguindo-se por quatro pontos estruturais — (i) prognóstico travado por release **antes** de qualquer medição; (ii) simulação rotulada em toda saída (tiers); (iii) P6: dado real análogo ⇒ antecipação **bancada**; (iv) P5: pesquisa derivada imediata como produto de primeira classe. Mapeamento de fontes candidatas em `SKILL_SCOUT_PARTE2.md` (elevação a registro E pendente de abertura, conforme regra).

**Posição na família dos métodos antecipatórios:** a ACP é irmã da meta-análise (agrega o publicado), da modelagem física (deriva comportamento) e dos in-silico trials (executa cenários) — e distingue-se por **travar prognósticos antes da medição e declarar a simulação como simulação em cada saída** (tiers [SIM]/[ORGANOID]/[MOUSE]/[HUMAN] [claim:C047] [evidence:E032, E033]). Onde a Parte 1 demonstrou a ACP no caso V127 (Parte 1 §2–§3), a Parte 2 **é** a ACP enquanto método de continuidade [claim:C054] [evidence:E009, E010, E031, E032, E033, E007].

### 3.2 Formulação matemática com proveniência (equações herdadas ESCRITAS nesta tese)

**Transporte (ADR) em meio poroso heterogêneo** (volumes finitos 2D 192², Euler explícito):

∂(αc)/∂t = ∇·(D_eff∇c) − ∇·(vc) + S(x) − k_eff·c

com α=0,20 e λ=1,8 medidos in-vivo por imagem óptica integrativa [10] [claim:C014] [evidence:E010]; D_eff=D₀/λ²=3,86×10⁻¹¹ m²/s com D₀=1,25×10⁻¹⁰ m²/s (Stokes–Einstein, R_h≈2,5 nm, ~30 kDa) [claim:C014] [evidence:E030]; k_eff varrido 10⁻⁶–10⁻⁵ s⁻¹ ancorado à polimerização nucleada [11] [claim:C015] [evidence:E011]; fluxo intersticial por Darcy; cistos espongiformes κ×50. Auto-testes do solver: conservação de massa 100,0% e erro de Thiele 0,5% (ℓ=3,59 mm) [claim:C032] [evidence:E030].

**Capping dominante-negativo e o limiar θ** (termo próprio deste programa):

freeS(r) = (1 + κ·c_V127(r))⁻² ;  c_V127(r) ∝ exp(−r/ℓ), ℓ=3,59 mm ;  **θ ≡ (1 + κ·c_pico)⁻¹ ∈ (0,1]**

θ é a fração de atividade máxima de replicação remanescente no pico do campo secretor; contenção declarada quando a frente assintótica cai abaixo de 50% do baseline (T3) [claim:C033] [evidence:E030]. A forma quadrática reflete conversão de dois participantes (ambos dessequestrados); a alternativa de primeira potência (heterodímero) é falseável pela dose-resposta do braço A6 [claim:C051] [evidence:E032, E033].

**Relógio humanizado** (âncoras de organoide humano [7] [E007]): duplicação ≈12,1 dias e 1 unidade de simulação = 144 dias, derivadas de clareza do inóculo 25–28 dpi, produção de-novo 35 dpi e títulos 169 dpi [claim:C037] [evidence:E032, E007].

**Estimador θ_obs (instrumento da continuidade; calibração sim-a-sim)**: features (raio da frente R, log-razão de biomassa); κ̂ por vizinho-mais-próximo na grade κ∈{1,5–8} do motor v4; θ̂=1/(1+κ̂); regime por braço: mediana com n=8 e IC bootstrap 90%. Veredito pré-declarado: ADEQUADO na fronteira de decisão (cobertura do θ verdadeiro 3/3; bias −0,008 em κ=2; recuperação modal 69%); a variante interpolada v1.1 foi testada e rejeitada [claim:C052] [evidence:E032, E033]. Toda saída carrega o rótulo do tier que a produziu [claim:C047] [evidence:E032, E033].

### 3.3 Base de Validade (MANDATÓRIA — exigência do guardião)

**Declaração tríade:** (i) esta tese é **baseada em simulação computacional e NÃO SUBSTITUI a validação de laboratório** — o laboratório é **essencial** para que a tese seja absorvida como real; (ii) a continuidade do estudo provém dos **prognósticos**: se os exames iniciais de laboratório (G0-wet [ORGANOID], e no futuro o humano) **equivalerem ao que foi simulado**, nós já possuímos **antecipação de dados e informações aplicáveis imediatamente** — essa é a metodologia da tese; (iii) o rigor exigido de uma tese experimental — como foi feito, por quem, com quais critérios, quais resultados — é aqui **convertido para o ambiente computacional**: cada dado tem linhagem completa declarada (quem produziu, em que espécie/sistema, validação cruzada por qual fonte independente, qual código simulou, como foi parametrizado para humano, qual resultado produziu).

**Linhagem dos dados (data lineage — o "métodos experimental" convertido):**

| Dado | Produzido por (primário) | Espécie/sistema | Validação cruzada (independente) | Simulado por (código) | Parametrização humana | Resultado [SIM] |
|---|---|---|---|---|---|---|
| Cinética de replicação do prião | Fornara/Igel 2024, iScience, código aberto [E009] | camundongo | Masel 1999 (polimerização nucleada) [E011] | kernel reação–difusão (Zenodo 11093945) portado [claim:C013] [evidence:E009] | relógio calibrado às âncoras humanas | θ\*=0,333 [C038] |
| Relógio e amplitude humanos | Groveman 2019, Acta Neuropathol [E007] | organoide humano sCJD | Groveman 2021 (ensaio de droga na mesma plataforma) [E008]; subtipos 2023 (RML) | regressão de duplicação (12,1 d; 144 d/unid) [claim:C037] [evidence:E032, E007] | direto (já humano) | predição travada θ<0,33 [C040] |
| Transporte intersticial | Thorne & Nicholson 2006, PNAS (IOI in-vivo) [E010] | humano (in-vivo) | Stokes–Einstein (físico-química, derivação auditável) | solver ADR auto-testado [claim:C032] [evidence:E032] | direto (já humano) | regras 1–3 [C033][C034][C035] |
| Agente V127 anchorless | Asante 2015 Nature [E001] · Gatdula 2026 [E003] · Zerbes 2026 [E004] | população→camundongo→cultura→AAV in-vivo | quatro níveis independentes de evidência | termo de capping freeS | dose ↔ κ (âncora ilustrativa; A6 fecharia) | contenção em κ=2 [C038] |
| Prior de falhas clínicas | Geschwind 2013 · Haïk 2014 · Newman 2014 · Otto 2004 · Mead 2022 · Cheng 2015 [E034–E038, E022] | humano (ensaios clínicos) | registry-bound, identificadores abertos | Beta–Binomial WS-8 [C036] | direto | P=5%/30–45% duas lentes |
| Sensibilidade estrutural | (este programa) | in-silico | motor reproduzido 2× ambientes (hash+valor) | sweeps S1/S2 + estimador | — | predição discriminadora [C051] |

**Por que isto é ciência com referências sólidas:** toda célula da linhagem amarra a fonte peer-reviewed ou ao run arquivado com hash; nenhum número vive fora do registro (51 claims · 38 fontes · 48 N-fatos · 4 validadores em zero); o código é aberto e o guardião audita máquina-a-máquina — a cadeia **quem→espécie→cruzamento→código→parâmetro→resultado** é verificável de ponta a ponta, exatamente como um "métodos" experimental exige, só que executada em ambiente computacional e declarada com a mesma disciplina.


### 3.4 A tese em forma experimental — o mapeamento análogo (diretriz da autora, 28/08)

Esta é **uma tese igual em forma à tese experimental** — com "sujeito", instrumentos, coleta, documentos e implicações documentados como um protocolo com pessoas documenta seus participantes. A diferença é uma só: **em vez de pessoas, o sujeito da pesquisa é o conjunto papers + fontes + código + simulação** — e cada elemento é documentado exatamente como o seria numa tese de laboratório. O dado produzido permanece rotulado [SIM] (a semântica dos tiers não muda; muda quem desempenha cada papel):

| Elemento de tese experimental (com pessoas) | Nesta tese (baseada em simulação computacional) |
|---|---|
| Participantes/pacientes recrutados | **Fontes publicadas** — os "sujeitos de dados" (38 fontes E-registradas; linhas 1–6 da linhagem §1-bis) |
| Critérios de recrutamento/inclusão-exclusão | SLR auditada com query bank pré-registrada (P0; protocolo 2.5 quando o objeto é parceiro) |
| Consentimento/aprovação ética | Verificação de proveniência por fonte aberta (identifier confirmado; método e data no manifest) |
| Instrumentos de medição calibrados | **Código**: kernel publicado + solvers auto-testados (massa 100% · ℓ 0,5%) — calibração documentada |
| Protocolo experimental executado | Parametrização com proveniência por parâmetro (P1) + execução determinística (P2) |
| Eventos/dados coletados e registrados | **Runs arquivados [SIM]** (JSONs: sweeps, grade, calibração do estimador; reprodução em 2 ambientes) |
| Prontuário/documentação clínica | **Registro da tese**: 54 claims · 48 N-fatos · linhagem completa · registro de pendências estruturado · AUDIT_NOTES |
| Análise estatística pré-especificada | Colheita sob critérios pré-declarados (P3) + estimador θ_obs com calibração sim-a-sim |
| Consequências/implicações relatadas | Prognósticos travados por release (P4) + pesquisa derivada imediata (P5) + antecipação bancada se análogo (P6) |
| Auditoria/supervisão | **Guardião-2**: revisor hostil da tese em metodologia · dados · conformidade · conteúdo |

*Um examinador que sabe ler tese experimental sabe ler esta: basta trocar "pessoa" por "fonte", "instrumento" por "código", "coleta" por "run" — a forma documental é idêntica; a base é simulação computacional.*

# CAPÍTULO 4 — RESULTADOS

### 4.1 Os resultados da tese são os resultados da simulação já realizada

Em vez de laboratório ou teste humano, **o que valida e compõe a tese neste estágio é o conjunto computacional executado** — completo, arquivado e reproduzido: (i) limiar de contenção θ\*=0,333 com relógio humanizado [claim:C038] [evidence:E032]; (ii) três regras de design falseáveis [claim:C033] [evidence:E030] [claim:C034] [evidence:E030, E020] [claim:C035] [evidence:E030, E019]; (iii) colheita de sensibilidade com predição discriminadora (C₅₀ 10× insensível; forma funcional falseável por dose-resposta) [claim:C051] [evidence:E032, E033]; (iv) quadro probabilístico de duas lentes com prior registry-bound [claim:C036] [evidence:E031]; (v) estimador θ_obs calibrado no regime declarado [claim:C052] [evidence:E032, E033]; (vi) reprodução independente em dois ambientes (hash + valor-a-valor); e (vii) a **tabela-decisão derivada** (κ↔θ_obs↔frente↔biomassa↔margem) extraída sem nova simulação — que mostra a margem de raio saturando cedo (70,2% já em κ=1,5) e confirma a **razão de biomassa como coordenada informativa** (48→1,25), com θ\*=0,333 como variável-de-decisão pré-registrada [claim:C052] [evidence:E032, E033]. De cada valor razoável aqui, **pesquisa derivada já pode prosseguir** — portas abertas.

### 4.2 M1 — Estimador θ_obs: o dado parametrizado como instrumento

O objetivo operacional: converter gradiente proximal/distal medido em θ_obs comparável ao limiar travado θ\*=0,333 [claim:C038] [evidence:E032] **sem circularidade** (grade e função-objetivo congeladas antes do dado; Parte 1 §2.7). A validação do próprio instrumento é computacional — simulation-based calibration sobre a grade κ∈{1,5–8} do motor v4 exato:

- **Calibração unitária** (1000 boots; ruído organoide publicado CV 30/40%): veredito **ADEQUADO** por critérios pré-declarados (cobertura do θ verdadeiro 3/3; bias ≤ 0,032) [claim:C052] [evidence:E032, E033] — com nota honesta: resolução por-órganoide é baixa; a precisão vem do **regime declarado** (mediana por braço, n=8).
- **Regime pooled n=8**: PASS integral **na fronteira de decisão** (κ=2: bias −0,008; recuperação modal 69%; cobertura ✓) — a região exata onde a predição travada decide (θ<0,33) [claim:C052] [evidence:E032, E033]; em κ alto o bias é **conservador** (+0,060: superestima θ, subestima contenção — erro no lado seguro).
- **v1.1-IDW (interpolação) testada e rejeitada**: piorou a fronteira (bias −0,037, direção anti-conservadora) e quebrou cobertura em κ=8 — registrado como evidência de que a disciplina anti-hindsight está viva: o upgrade que falha é descartado, não embranquecido [claim:C052] [evidence:E032, E033].
- Achado de design que o método produziu: a razão de biomassa carrega a informação que o raio perde por saturação (R 0,843→0,760 mm contra razão 48→1,25 na grade) — o estimador opera no par de features por necessidade [claim:C052] [evidence:E032, E033].

### 4.3 M2 — Freeze de execução: o que trava antes do primeiro organoide

Dez itens F1–F10, com GATE-F de liberação: estimador (F1, fechado — §2), plano estatístico (Welch/Holm α=0,05, 5 comparações; n=8→12; poder ~80% para Δ≥50%), cegamento do scorer, randomização/estratificação por lote (DP MV2 ≈77% da média publicada), controle positivo A8-PPS como critério de validade do ensaio, kill-switches por braço + **critério de morte programática**, esquema de dado [ORGANOID] (contrato bancada→estimador; exclusões publicadas nunca editadas), loop M3, timelines (readouts 90–120 d; regime estacionário desde ~4 d) e M4 (parceiro por método). Regra: pós-GATE-F, qualquer mudança é emenda auditada com re-análise com-e-sem.

### 4.4 M3 — Loop de re-parametrização (o coração anti-hindsight)

O dado medido recalibra **exatamente o que informa**: o braço A6 (dose conhecida) fecha κ↔µM — âncora ilustrativa da Parte 1 §2.2 tornado absoluto pelo dado — convertendo o cálculo de contenção de relativo a absoluto — e executa o teste discriminador da forma funcional (primeira potência vs quadrática; travado na colheita [SIM] da Parte 1) [claim:C051] [evidence:E032, E033]; θ\* **compara-se, nunca se retreina**; taxas murinas relativas e parâmetros de transporte humano só mudam por dado do seu próprio escopo. Toda comparação cita a âncora do release onde a predição foi travada (v1.0 / v3.0); toda recalibração gera pre-dição nova **antes** do próximo dado — o loop nunca "explica depois" sem ter previsto antes.

### 4.5 M4 — Método de seleção de parceiro: assertividade por método (SLR-análogo)

**A tese documenta o COMO; não seleciona o QUEM** [claim:C053] [evidence:E033]. O protocolo (v2.1) é o análogo de revisão sistemática aplicado à decisão "onde medir":

1. **Query bank Q1–Q5** — strings exatas por plataforma (PubMed `[tiab]`, ClinicalTrials.gov, cinza-conferências, rede BR), registradas antes da execução, ancoradas em commit (PROSPERO-análogo);
2. **Inclusão I1–I5 / exclusão X1–X4 binárias** — plataforma organoide-príon publicada · BSL-príon certificada · capacidade ≥64 organoides com controle de lote · aceitação de pré-registro/kill-switch · formalização ≤6 meses; vetos: sem biossegurança, sem cegamento, IP exclusiva, indisponibilidade >12m;
3. **Pesos congelados A–H** (25/15/15/10/10/10/10/5 — plataforma, track príon, capacidade, braço A5, braço A7, co-localização BR/E200K, open-science, prontidão), âncoras 0–5, "?" não pontua por regra;
4. **Fluxo PRISMA-regenerável** (identificados→dedup→triagem→pontuação→contato sequencial por score; desempate = plataforma) com log datado e público;
5. **Aplicação-piloto** (log v0.2): demonstra executabilidade — 9 registros → 8 grupos → 2 elegíveis + 1 condicional + 3 watchlist + 2 técnicos; o método corrigiu o prior (peso do eixo D em Calgary à luz do JCI 2026); o piloto **não decide** — as ordens que emite são saídas do método para o executor futuro [claim:C053] [evidence:E033].

Replicabilidade posterior: qualquer pesquisador re-executa as strings, re-tria, re-pontua; divergências >10 pts viram auditoria, não erro. Viés declarado: single-rater v1 (co-rating pré-declarado como pendência).

### 4.6 M5 — Infraestrutura de continuidade (guardião + runbook)

O guardião opera com **perfis de superfície** (`--profile part1|part2`): a Parte 2 tem contrato próprio de gate (mesmo registro de pendências estruturado, baterias e binding de números citados; sem herdar os padrões literais da Parte 1), e a **Base de Validade (§1-bis) é check BLOCKED permanente** neste perfil. Toda superfície de manuscrito é gated por revisão hostil recursiva (R0 drift estrutural · R1 checklist+baterias · R2 recursão de emendas · R3 interrogação epistêmica + registro {{TODO:id:desc}}); o decálogo vivo (tiers de dado · locked-stays-locked · ilustrativo≠evidência · paridade · anti-hindsight · fim-de-sessão=/RECAP) está no guardian.md com comandos copy-paste — a continuidade não depende de memória de quem continua, e sim de método documentado — índice-mestre no KNOWLEDGE_CANON.md.

# CAPÍTULO 5 — DISCUSSÃO

### 5.1 Promessas e limites desta Parte 2

Promete: a ACP como método completo, replicável e em parte já demonstrado (M1 executado; M4 piloto) — continuar pesquisa por simulação hoje, como a física, sem parar à espera de cada confirmação. E declara: os resultados daqui **são de simulação e assim permanecem rotulados**; a aplicação/validação em ambiente real não é prometida nesta Parte — se dados reais futuros forem análogos aos simulados, **os passos seguintes já estão avançados** (P6) [claim:C054] [evidence:E009, E010, E031, E032, E033, E007]. **Não promete**: seleção de parceiro (execução externa), dado [ORGANOID]+ (não existe ainda — e é rotulado como tal), nem qualquer claim clínica (escada de tiers: nenhum degrau empresta a autoridade do seguinte). Limites declarados: pesos e scores são julgamento estruturado single-rater; a calibração do estimador é na grade atual (refinamento futuro = grade mais fina, pré-declarado); PubMed-direto e identificação R8 pendem como conformidade do piloto.

# APÊNDICE A — Inventário dos artefatos da Parte 2 (verificável em disco)

| Artefato | O que é | Estado |
|---|---|---|
| `experiments/part2_theta_obs_v1.py` + `part2_results/part2_theta_obs_v1.json` | estimador v1-NN: grade κ 1,5–8 + calibração unitária (veredito ADEQUADO pré-declarado) | executado |
| `experiments/part2_theta_obs_pooled.py` + `.json` | regime declarado §2.7: mediana por braço n=8 (bias −0,008 na fronteira; modal 69%) | executado |
| `experiments/part2_theta_obs_v11.py` + `.json` | estimador interpolado IDW-2 — **testado e REJEITADO** (bias anti-conservador na fronteira; cobertura quebra em κ=8); JSON regenerado por script após truncamento da primeira execução (nota de integridade in-file) | executado (rejeitado) |
| `experiments/part2_results/part2_derived_summary.json` | tabela-decisão derivada (κ↔θ↔R↔biomassa↔margem) — zero novas simulações | derivado |
| `experiments/part2_results/partner_selection_log.md` v0.2 | aplicação-piloto do método M4 (9 registros → 8 grupos → 2+1+3+2) — não-decisório | piloto |
| `experiments/G0_EXECUTION_FREEZE_CHECKLIST.md` | F1–F10 + GATE-F (M2 — dormant por reenquadramento) | especificado |
| `experiments/REPARAM_LOOP.md` | regra anti-hindsight de realimentação (M3) | especificado |
| `experiments/PARTNER_SELECTION_PROTOCOL.md` v2.1 | método M4 (query bank + I/X + pesos + fluxo) | método |
| `paper/guardian/guardian.py` (`--profile part2`) | gate da Parte 2 (inclui R3-BASE-VALIDADE BLOCKED) | operante |

*Nota de integridade da auditoria 27/08 (tarde): dois defeitos encontrados e corrigidos no próprio ato — JSON da v11 truncado por erro de serialização (regenerado por script salvo, seed idêntica, veredito idêntico) e sinal do bias pooled invertido na prosa (−0,008 conforme o JSON; corrigido nos três documentos). Ambos registrados aqui porque a auditoria que não publica suas correções não é auditoria.*

## REFERÊNCIAS E CONCORDÂNCIA

### Referências (38 fontes do registro, geradas do manifest)

[1] ASANTE, E.A. et al. A naturally occurring variant of the human prion protein completely prevents prion disease. 2015. doi:10.1038/nature14510.
[2] MEAD, S. et al. A novel protective prion protein variant that colocalizes with kuru exposure. 2009. doi:10.1056/NEJMoa0809716.
[3] GATDULA, J.R. et al. Leveraging the dominant-negative effect of the kuru-protective G127V prion protein variant as a novel therapeu. 2026. PMID 41757113.
[4] ZERBES, T. et al. A self-complementary recombinant adeno-associated virus vector coding for an anchorless prion protein carrying. 2026. .
[5] HOSSZU, L.P. et al. Structural effects of the highly protective V127 polymorphism on human prion protein. 2020. doi:10.1038/s42003-020-01126-6.
[6] ZHENG, Z. et al. Structural basis for the complete resistance of the human prion protein mutant G127V to prion disease. 2018. doi:10.1038/s41598-018-31394-6.
[7] GROVEMAN, B.R. et al. Sporadic Creutzfeldt-Jakob disease prion infection of human cerebral organoids. 2019. doi:10.1186/s40478-019-0742-2.
[8] GROVEMAN, B.R. et al. Human cerebral organoids as a therapeutic drug screening model for Creutzfeldt-Jakob disease. 2021. doi:10.1038/s41598-021-84689-6.
[9] FORNARA, B. et al. The dynamics of prion spreading is governed by the interplay between the non-linearities of tissue response an. 2024. PMID 39717079.
[10] THORNE, R.G. et al. In vivo diffusion analysis with quantum dots and dextrans predicts extracellular space and tortuosity in brain. 2006. doi:10.1073/pnas.0509425103.
[11] MASEL, J. et al. Quantifying the kinetic parameters of prion replication. 1999. doi:10.1016/S0301-4622(99)00004-3.
[12] WILLIAMS, K. et al. Neural cell engraftment therapy for sporadic Creutzfeldt-Jakob disease restores neuroelectrophysiological para. 2023. doi:10.1186/s13287-023-03591-2.
[13] RELANO-GINES, A. et al. Prion replication occurs in endogenous adult neural stem cells and alters their neuronal fate. 2013. doi:10.1371/journal.ppat.1003485.
[14] GINHOUX, F. et al. Fate mapping analysis reveals that hematopoietic cells of yolk-sacil origin give rise to microglia. 2010. doi:10.1126/science.1194637.
[15] SORRELLS, S.F. et al. Human hippocampal neurogenesis drops sharply in children to undetectable levels in adults. 2018. doi:10.1038/s41586-018-0336-4.
[16] ABUD, E.M. et al. iPSC-derived human microglia-like cells to study neurological diseases. 2017. PMID 28426964.
[17] HAN, X. et al. Generation of hypoimmunogenic human pluripotent stem cells. 2019. doi:10.1073/pnas.1902566116.
[18] HU, X. et al. Hypoimmune induced pluripotent stem cells survive long-term in fully immunocompetent allogeneic rhesus macaque. 2024. doi:10.1038/s41587-023-01784-x.
[19] XUE, Y. et al. Lipid nanoparticles enhance mRNA delivery to the central nervous system upon intrathecal injection. 2025. PMID 40317512.
[20] LIANG, Y. et al. The survival of engrafted neural stem cells within hyaluronic acid hydrogels. 2013. PMID 23623429.
[21] SHAH, S.Z. et al. Early minocycline and late FK506 treatment improves survival... in prion-infected hamsters (RETRACTED). 2017. doi:10.1007/s13311-020-00909-3.
[22] CHENG, S. et al. Minocycline reduces neuroinflammation but does not improve survival in prion-infected mice. 2015. doi:10.1038/srep10535.
[23] GENTILE, J.E. et al. Evidence that minocycline treatment confounds neurofilament light chain biomarker interpretation. 2024. https://www.ukdri.ac.uk/publications/evidence-minocycline-treatment-confounds-interpretation-neurofilament-biomarker.
[24] SMID, J. et al. Creutzfeldt-Jakob disease associated with a missense mutation at codon 200 of the prion protein gene in Brazil. 2007. https://www.demneuropsy.com.br/article/creutzfeldt-jakob-disease-associated-with-a-missense-mutation-at-codon-200-of-the-prion-protein-gene-in-brazil/.
[25] STOPSCHINSKI, B.E. et al. Prion-like mechanisms in neurodegenerative disease. 2017. doi:10.1016/S1474-4422(17)30370-6.
[26] JUCKER, M. et al. Propagation and spread of pathogenic protein assemblies in neurodegenerative diseases. 2018. doi:10.1038/s41586-018-0344-4.
[27] FDA, (.F. et al. FDA grants accelerated approval of tofersen for SOD1-ALS (press release/decision summary). 2023. https://www.fda.gov/news-events/press-announcements/fda-grants-accelerated-approval-first-treatment-als-patients-rare-genetic-form-disease.
[28] FDA, (.F. et al. FDA approval of nusinersen (Spinraza) — regulatory record. 2016. https://www.fda.gov/vaccines-blood-biologics/approved-blood-products/spinraza-nusinersen.
[29] BENGTSSON, S. et al. Clinical trial of stem-cell derived dopaminergic progenitor transplantation in Parkinson's disease (feasibilit. 2026. https://www.newscientist.com/article/....
[30] OPEN, P.&. et al. WS-7: ADR transport solver — self-tested design rules (this program). 2026. Disponível em: https://github.com/camillanapoles/quest003-prion-v127.
[31] OPEN, P.&. et al. WS-8: hierarchical Bayesian calibration over structural analogues (this program). 2026. Disponível em: https://github.com/camillanapoles/quest003-prion-v127.
[32] OPEN, P.&. et al. WS-9: humanized in-silico infection model with V127 capping (this program). 2026. Disponível em: https://github.com/camillanapoles/quest003-prion-v127.
[33] OPEN, P.&. et al. Quest 003 repository — timestamped pre-registrations and audit trail (this program). 2026. Disponível em: https://github.com/camillanapoles/quest003-prion-v127.
[34] GESCHWIND, M.D. et al. Quinacrine treatment trial for sporadic Creutzfeldt-Jakob disease (Class I: no survival benefit). 2013. PMID 24122181.
[35] HAIK, S. et al. Doxycycline in Creutzfeldt-Jakob disease: a phase 2, randomised, double-blind, placebo-controlled trial (no si. 2014. PMID 24411709.
[36] NEWMAN, P.K. et al. Postmortem findings in a case of variant CJD treated with intraventricular pentosan polysulfate (iPPS): biolog. 2014. PMID 24554103.
[37] OTTO, M. et al. Efficacy of flupirtine on cognitive function in patients with CJD: a double-blind placebo-controlled study (co. 2004. doi:10.1212/01.WNL.0000113764.35026.ef.
[38] MEAD, S. et al. Prion protein monoclonal antibody (PRN100) therapy for Creutzfeldt-Jakob disease: evaluation of a first-in-hum. 2022. PMID 35305340.

### Fontes complementares (skill-scout; verificação completa pendente — snippet-level)
- CORTÉS-RÍOS, J. et al. A step-by-step workflow for performing in silico clinical trials. 2025. PMCID PMC12706418. *(abertura completa pendente antes de registro E)*
- An open source statistical web application for validation of in-silico trials and virtual cohorts. 2025. doi:10.1038/s41598-025-99720-3. *(idem)*

### Concordância claims → referências (régua da autora: claim sem referência é inaceitável)

| Claim | Evidências | Referências |
|---|---|---|
| C001 | E001 | [1] |
| C002 | E001 | [1] |
| C003 | E001, E003, E005 | [1], [3], [5] |
| C004 | E002 | [2] |
| C005 | E003 | [3] |
| C006 | E003 | [3] |
| C007 | E004 | [4] |
| C008 | E005, E006 | [5], [6] |
| C009 | E007 | [7] |
| C010 | E007 | [7] |
| C011 | E007 | [7] |
| C012 | E008 | [8] |
| C013 | E009 | [9] |
| C014 | E010, E030 | [10], [30] |
| C015 | E011, E030 | [11], [30] |
| C016 | E012 | [12] |
| C017 | E013 | [13] |
| C018 | E014 | [14] |
| C019 | E015 | [15] |
| C020 | E016 | [16] |
| C021 | E017, E018 | [17], [18] |
| C022 | E019 | [19] |
| C023 | E020 | [20] |
| C024 | E021 | [21] |
| C025 | E022 | [22] |
| C026 | E023 | [23] |
| C027 | E024 | [24] |
| C028 | E025, E026 | [25], [26] |
| C029 | E027 | [27] |
| C030 | E028 | [28] |
| C031 | E029 | [29] |
| C032 | E030 | [30] |
| C033 | E030 | [30] |
| C034 | E030, E020 | [30], [20] |
| C035 | E030, E019 | [30], [19] |
| C036 | E031 | [31] |
| C037 | E032, E007 | [32], [7] |
| C038 | E032 | [32] |
| C039 | E032, E007 | [32], [7] |
| C040 | E033 | [33] |
| C041 | E033 | [33] |
| C042 | E030 | [30] |
| C043 | E032, E009 | [32], [9] |
| C044 | E032 | [32] |
| C045 | E033 | [33] |
| C046 | E032, E009, E007, E033 | [32], [9], [7], [33] |
| C047 | E032, E033 | [32], [33] |
| C048 | E009, E010, E030, E031, E032, E033 | [9], [10], [30], [31], [32], [33] |
| C049 | E032, E033 | [32], [33] |
| C050 | E021, E022, E034, E035, E036, E037, E038 | [21], [22], [34], [35], [36], [37], [38] |
| C051 | E032, E033 | [32], [33] |
| C052 | E032, E033 | [32], [33] |
| C053 | E033 | [33] |
| C054 | E009, E010, E031, E032, E033, E007 | [9], [10], [31], [32], [33], [7] |

---
---
*Parte 2 [SEM ANO] — o resultado define; as fases são estimativas. Toda cifra deste manuscrito vem de JSON arquivado ou do registro E (regra: nunca digitar valor). Gated: guardian R0–R3, 0 BLOCKED exigido.*
---
*Parte 2 [SEM ANO] — o resultado define; as fases são estimativas. Toda cifra vem de JSON arquivado ou do registro E (regra: nunca digitar valor). Gated: guardian R0–R3 perfil part2, 0 BLOCKED exigido. PT é o mestre; EN companion: manuscript_Parte2_v1_EN.md.*
