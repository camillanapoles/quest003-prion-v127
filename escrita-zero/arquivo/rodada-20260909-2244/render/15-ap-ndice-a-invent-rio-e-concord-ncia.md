# APÊNDICE A — INVENTÁRIO E CONCORDÂNCIA
Este apêndice existe para que o leitor confira a tese sem acesso a nenhum repositório: as datas de pré-registro e de versão do motor estão impressas aqui, o congelamento do gate úmido está resumido na íntegra dos seus itens, e a concordância entre cada claim e suas fontes está numa tabela só, gerada do registro probatório. O que aparece abaixo é o que o disco e o registro guardam — nada além disso.
## A.1 Folhas de pré-registro — datas impressas
Cada documento de pré-registro entrou no controle de versão antes da execução que ele disciplina; a primeira coluna de datas é a data de nascimento do documento, a segunda a última alteração aceita [claim:C040] [evidence:E033].
| Documento | Trava | Primeira versão | Última alteração | Commit |
|---|---|---|---|---|
| `experiments/g0_protocol.md` — Protocolo do gate G0-wet | desenho do ensaio, controle positivo e kill-switches | 2026-08-25 | 2026-08-31 | f26246f |
| `experiments/ws_10_spec.md` — Especificação WS-10 | a escada de portões como régua de continuidade | 2026-08-26 | 2026-08-31 | f26246f |
| `experiments/G0_EXECUTION_FREEZE_CHECKLIST.md` — Checklist de congelamento F1–F10 | o que deve estar travado antes do primeiro organoide infectado | 2026-08-27 | 2026-08-31 | f26246f |
| `experiments/PARTNER_SELECTION_PROTOCOL.md` — Protocolo de seleção de parceiro | critérios e pesos congelados antes de qualquer contato | 2026-08-27 | 2026-08-31 | f26246f |
| `experiments/REPARAM_LOOP.md` — Loop de re-parametrização | o que recalibra, com qual prior e quando | 2026-08-27 | 2026-08-31 | f26246f |
| `experiments/m31/M31_SESSAO2_PLANO.md` — Plano da sessão M31 | a titulação κ-exigido por cinética do hospedeiro | 2026-09-01 | 2026-09-01 | 33f2e9f |
| `experiments/m31/m31_protocolo_garantista.md` — Protocolo garantista M31 | garantias por passo da cadeia de dose | 2026-09-01 | 2026-09-01 | 0d17f34 |
## A.2 Motor e solver — folha de versão
O motor da Parte 2 é o solver WS-7 com auto-testes declarados — conservação de massa e erro numérico-analítico verificados [claim:C032] [evidence:E030] — calibrado pelo WS-8 sobre análogos estruturais [claim:C036] [evidence:E031] e executado pelo WS-9 com humanização do tempo e tampão V127 [claim:C037] [evidence:E032]. As versões abaixo são as folhas com as datas em que cada peça entrou e foi alterada pela última vez.
| Peça | Papel | Primeira versão | Última alteração | Commit |
|---|---|---|---|---|
| `experiments/ws_7_solver.py` | WS-7 — solver de transporte ADR | 2026-08-25 | 2026-09-01 | 98e7c02 |
| `experiments/ws_7_v2_wave.py` | WS-7 — frente de onda v2 | 2026-08-25 | 2026-08-31 | f26246f |
| `experiments/ws_8_bayes.py` | WS-8 — calibração bayesiana | 2026-08-25 | 2026-08-31 | f26246f |
| `experiments/ws_8_local.py` | WS-8 — ajuste local | 2026-08-25 | 2026-08-31 | f26246f |
| `experiments/ws_9_port.py` | WS-9 — portabilidade do modelo | 2026-08-26 | 2026-08-31 | f26246f |
| `experiments/ws_9_run.py` | WS-9 — execução do modelo | 2026-08-26 | 2026-08-31 | f26246f |
| `experiments/part2_theta_obs_pooled.py` | Estimador θ_obs pooled | 2026-08-27 | 2026-08-31 | f26246f |
| `experiments/part2_theta_obs_v1.py` | Estimador θ_obs v1.0-NN | 2026-08-27 | 2026-08-31 | f26246f |
| `experiments/part2_theta_obs_v11.py` | Estimador θ_obs v1.1-IDW | 2026-08-27 | 2026-08-31 | f26246f |
| `experiments/ws_9_v5_sweeps.py` | WS-9 — varreduras v5 | 2026-08-27 | 2026-08-31 | f26246f |
| `experiments/p024_driver.py` | Driver multi-espécie | 2026-09-01 | 2026-09-01 | 1e1d88d |
## A.3 Experimento 1 — folha de versão
A regra da linha experimental (Cap. 4, §4.2) exige que os dados do experimento 1 — a corrida murina com humanização do tempo — entrem na tese apenas onde permaneceram inalterados pelo experimento 2, com a folha de versão anexada. Esta é a folha. O run v4 humanizado travou o limiar: θ* igual a 0,333, com a frente contida em κ=2 — de 2,83 para 0,82 mm [claim:C038] [evidence:E032] — sob o relógio humanizado de uma unidade de simulação igual a 144 dias [claim:C037] [evidence:E032,E007]. A varredura S1 colheu a sensibilidade sem mover o limiar: em κ=2 a frente permanece no valor de base e a contenção desloca-se para κ=4 — a predição discriminadora que separa as duas formas funcionais da unidade inibitória [claim:C051] [evidence:E032,E033]. A re-execução da autora, em ambiente independente, reproduziu o S1 valor a valor [claim:C040] [evidence:E033].
| Artefato | Papel | Primeira versão | Última alteração | Commit |
|---|---|---|---|---|
| `experiments/ws_9_results/ws_9_v4_human.json` | Execução v4 humanizada | 2026-08-26 | 2026-08-31 | f26246f |
| `experiments/ws_9_results/ws_9_v5_sweeps_S1.json` | Varredura S1 | 2026-08-27 | 2026-08-31 | f26246f |
| `experiments/ws_9_results/ws_9_v5_sweeps_S1_authors_rerun.json` | Re-execução da autora (S1) | 2026-08-27 | 2026-08-31 | f26246f |
## A.4 Congelamento do gate úmido — F1–F10
O checklist de congelamento define o que precisa estar travado antes do primeiro organoide infectado. A tabela resume o estado de cada item; o estimador fechou com a variante de vizinho-mais-próximo mantida e a interpolada rejeitada na fronteira de decisão [claim:C052] [evidence:E032,E033]. A liberação final — o gate F — exige todos os itens fechados e a assinatura da pesquisadora principal do laboratório parceiro; a seleção de parceiro é método sem seleção e sem contato [claim:C053] [evidence:E033], e a infraestrutura de continuidade segue operante com a escada de portões como régua [claim:C047] [evidence:E033]. As duas pendências — a execução do fluxo de parceiro e a assinatura — são dormências por design, declaradas como tais nas conclusões.
| Item | Conteúdo congelado | Status |
|---|---|---|
| F1 | Estimador θ_obs congelado | v1.0-NN mantida; variante interpolada testada e rejeitada | FECHADO |
| F2 | Análise braço-a-braço | Welch com correção de Holm, poder declarado | congelado |
| F3 | Cegamento do scorista | scorista cego ao braço; aleatorização por lote | congelado |
| F4 | Estratificação por lote | aleatorização estratificada | congelado |
| F5 | Controle positivo A8 | critério de validade do ensaio declarado | congelado |
| F6 | Kill-switches por braço | critério de morte programática do programa | congelado |
| F7 | Esquema do dado de organoide | contrato entre bancada e estimador | congelado |
| F8 | Loop de re-parametrização | recalibração com prior e gatilho declarados | congelado |
| F9 | Janelas de leitura | regime estacionário e leitura declarados | congelado |
| F10 | Seleção do parceiro | protocolo congelado; execução do fluxo aguarda contato | dormente por design |
## A.5 Validação da base comum
A base que fundamento e aplicação compartilham tem cadeia de validação própria: o kernel estocástico é publicado com código aberto [claim:C013] [evidence:E009]; o motor passa por auto-testes declarados [claim:C032] [evidence:E030]; e a cadeia de reprodutibilidade do programa — versão anterior reproduzida idêntica, varredura reproduzida valor a valor em segundo ambiente — está registrada [claim:C040] [evidence:E033]. No ingestão do registro probatório para a escrita, cada texto de claim é verificado por soma criptográfica contra o índice do registro: nenhuma claim entra na tese se o texto divergir do congelado.
## A.6 Concordância claims ↔ fontes
A tabela abaixo é a régua da autora: cada claim do registro, ao lado das evidências que a sustentam e do seu estado de verificação. Gerada do banco, sem digitação; o leitor confere cada texto integral contra a forma como o corpo da tese o usou.
| Claim | Texto integral | Evidências | Verificação |
|---|---|---|---|
| [C001] | V127 homozygous transgenic mice are completely resistant to all tested prion strains, as protective as gene deletion | E001 | verified |
| [C002] | Heterozygous G/V127 mice resist kuru and classical CJD prions but remain infectable by vCJD prions | E001 | verified |
| [C003] | V127 acts as a potent dose-dependent dominant-negative inhibitor of wild-type prion propagation | E001;E003;E005 | verified |
| [C004] | G127V was under positive selection during the kuru epidemic; heterozygote carriers were protected | E002 | verified |
| [C005] | Recombinant anchorless V127 retains potent dominant-negative activity in trans in cell culture | E003 | verified |
| [C006] | Prion resistance in cell culture persists after transgene expression ceases | E003 | verified |
| [C007] | Systemic AAV delivery of anchorless V127GPI extended survival approximately 50 days in a rodent prion model | E004 | verified |
| [C008] | V127 restricts the pre-beta-sheet backbone and stabilizes dimers via intermolecular hydrogen bonds; alters beta2-alpha2 loop dynamics | E005;E006 | verified |
| [C009] | Human cerebral organoids are susceptible to sCJD infection with subtype-dependent kinetics | E007 | verified |
| [C010] | Organoid infection anchors: inoculum cleared by 25-28 dpi, de-novo seeding activity from 35 dpi | E007 | verified |
| [C011] | Endpoint titers at 169 dpi: MV2 = 2.13(+/-1.63)e5 and MV1 = 1.69(+/-0.70)e3 SD50 per mg; protease-resistant PrP detected only in MV2 | E007 | verified |
| [C012] | Pentosan polysulfate delays prion propagation in infected organoids in prophylactic-like and therapeutic-like paradigms (published positive control) | E008 | verified |
| [C013] | The prion-spreading kernel is a published stochastic reaction-diffusion model with open code (Gillespie over aggregate classes with UPR-gated templating) | E009 | verified |
| [C014] | In vivo brain extracellular space: volume fraction approximately 0.20 and tortuosity approximately 1.8 for macromolecules | E010;E030 | verified |
| [C015] | First-order consumption swept 1e-6 to 1e-5 per second anchored to nucleated-polymerization kinetics | E011;E030 | verified |
| [C016] | NPC seeding restores electrophysiological parameters of sCJD-infected organoids toward uninfected levels | E012 | verified |
| [C017] | Endogenous adult neural stem cells accumulate and replicate prions; neuronal fate is altered by infection | E013 | verified |
| [C018] | NSCs do not generate microglia; microglia derive from yolk-sac macrophage lineage | E014 | verified |
| [C019] | Adult human SVZ neurogenesis is minimal; the niche is largely quiescent | E015 | verified |
| [C020] | iPSC-derived microglia-like cells are generated in approximately five weeks by a defined protocol | E016 | verified |
| [C021] | HLA-KO hypoimmunogenic pluripotent cells evade rejection; CD47 is necessary and sufficient against NK-mediated rejection with long-term allogeneic survival | E017;E018 | verified |
| [C022] | A single intrathecal dose of brain-targeting LNP mRNA expresses in 29.6 percent of neurons and 38.1 percent of astrocytes in rodents | E019 | verified |
| [C023] | Hyaluronic-acid hydrogel scaffolding increases survival of engrafted neural stem cells | E020 | verified |
| [C024] | A 2017 Neurotherapeutics minocycline/FK506 prion trial was retracted in 2020 and is excluded by rule | E021 | verified |
| [C025] | Minocycline reduces neuroinflammation without survival benefit in prion-infected mice | E022 | verified |
| [C026] | Minocycline confounds neurofilament-light chain biomarker interpretation (3.5x plasma, 5.7x CSF increase) | E023 | verified |
| [C027] | Brazilian E200K kindreds have been documented since 2007 | E024 | verified |
| [C028] | Alzheimer and Parkinson proteins spread by templated misfolding along stereotyped routes (prion-like propagation) | E025;E026 | verified |
| [C029] | Tofersen received accelerated approval for SOD1-ALS with a biomarker (NfL) endpoint in 2023 | E027 | verified |
| [C030] | Nusinersen established chronic intrathecal ASO redosing safety since 2016 | E028 | verified |
| [C031] | Dopaminergic progenitor cell transplantation in Parkinson patients proved feasible in a 2026 trial | E029 | verified |
| [C032] | WS-7 self-tests pass: mass conservation 100.0 percent; numeric vs analytic Thiele length error 0.5 percent | E030 | verified |
| [C033] | Design rule 1: containment-ring node spacing 8-12 mm (protection radius 4-6 mm per deposit) | E030 | verified |
| [C034] | Design rule 2: hydrogel mesh must exceed 5x protein radius; HA 1-2 percent passes, above 5 percent sequesters the secretome | E030;E020 | verified |
| [C035] | Design rule 3: LNP-mRNA redosing interval of 7 days or less keeps inter-pulse trough at 56 percent of peak; 10-14 days leaves valleys | E030;E019 | verified |
| [C036] | Bayesian frame: P(G0 organoid gate informative-go) = 36.6 percent with 90 percent credible interval 14.6 to 60.5; P(clinical slowing) = 5.0 percent [0.4-13.6] empirical vs 30-45 percent design-conditional; the operative computational gate G0-sim is already executed (two-tier gate architecture) | E031 | verified |
| [C037] | Humanization: 1 simulation unit = 144 days; derived human doubling time 12.1 days from organoid anchors | E032;E007 | verified |
| [C038] | Containment threshold theta-star = 0.333: front contained at kappa=2 (2.83 to 0.82 mm), monotone to near-extinction at kappa=32 (0.70 mm, biomass ratio 2.1x seed) | E032 | verified |
| [C039] | Emergent consistency: seeding by the published 126x titer ratio reproduces the MV2-greater-than-MV1 hierarchy without fitting | E032;E007 | verified |
| [C040] | All program predictions were committed to the public repository with timestamps before any wet-lab experiment exists | E033 | verified |
| [C041] | External document references were audited individually: of 19 audited, 11 correct, 3 duplicates, 1 non-scientific, 1 wrong link | E033 | verified |
| [C042] | Steady-state establishment takes approximately 4 days; planned readouts operate in steady state | E030 | verified |
| [C043] | Humanization is a global time rescaling; relative rates remain murine pending fits to published series | E032;E009 | verified |
| [C044] | Acceptance tiers: T1 and T2 are minimal screening criteria; T3 is the informative mechanistic success tier - front radius below 50 percent of baseline at kappa at most 8 with monotone radial gradient - satisfied by the humanized run at kappa 2 (0.82 mm = 29 percent of 2.83 mm baseline) | E032 | verified |
| [C045] | A same-mass MV1-seed control run (MV1 seeded with the MV2-mass inoculum) is queued to disentangle seed mass from subtype-specific kinetics in the hierarchy consistency test | E033 | verified |
| [C046] | The in-silico gate G0-sim is executed and passed: acceptance tiers T1 T2 and T3 on the humanized model plus emergent subtype consistency; computational findings are used as results in their own epistemic tier and stimulate agile assertive research and development; validation remains necessary and non-substitutable; no biological validation or clinical claim is licensed | E032;E009;E007;E033 | verified |
| [C047] | Gate nomenclature and data-tier labeling rule: the gate ladder is G0-sim in silico executed, G0-wet organoid specified, G1 humanized mouse conditional, G2 first-in-human conditional; all forthcoming program outputs carry an explicit data-tier tag SIM ORGANOID MOUSE or HUMAN so that simulation-based data is never mistaken for measured data | E032;E033 | verified |
| [C048] | The thesis objective is stated without a calendar year and is defined by results: to carry the research to the end of its arc in the simulated environment using real parametrized data, harvest the complete simulation results, and then validate gate by gate; the computational-continuation methodology - systematic review plus parametrized physics plus Bayesian frame plus pre-registered in-silico gates - is an innovation in anticipatory research evaluation (predictability and information anticipation) | E009;E010;E030;E031;E032;E033 | verified |
| [C049] | Thesis architecture: the thesis is composed of Part 1 pre-G0 (research findings simulation benefits) and Part 2 post-G0 (continuity thesis: research and validation using the parametrized simulation data) joined at the G0 junction with detailed explanation; neither part is systematically sustainable without the other; Part 2 operationalizes predictability and information anticipation for therapeutic design - deciding what to measure where and at what dose before any wet-lab resource is spent | E032;E033 | verified |
| [C050] | The six historical antiprion clinical failures are evidence-bound: quinacrine (Class I trial, no survival benefit), doxycycline (phase 2 RCT, no significant effect), intraventricular pentosan polysulfate (case series, biological effect without cure), flupirtine (RCT, cognitive endpoint without survival benefit), PRN100 antibody (first-in-human, no clear clinical efficacy), and minocycline-combinations (retracted trial excluded; separate no-benefit trial) | E021;E022;E034;E035;E036;E037;E038 | verified |
| [C051] | Sensitivity harvest SIM: the containment threshold is robust to the logistic C50 over a tenfold range (20 to 200: front at kappa 2 unchanged at 0.819 mm) but sensitive to the free-substrate functional form: with a first-power term (heterodimer unit) kappa 2 no longer contains (front 2.828 mm equals baseline) and containment shifts to kappa 4 (0.85 mm); the archived exp-2 sweep is reproduced exactly (0.819/0.778/0.760 vs 0.82/0.78/0.76); dose-response at arm A6 can therefore discriminate the two forms | E032;E033 | verified |
| [C052] | Part 2 M1: the theta_obs estimator is simulation-calibrated with pre-declared criteria (unit calibration ADEQUADO: coverage 3 of 3, bias <= 0.032); in the declared per-arm regime (median, n=8) it passes INTEGRALLY at the decision boundary (kappa 2: bias 0.008, modal recovery 69 percent) with conservative bias at high kappa; the interpolated v1.1 was tested and REJECTED (degrades the boundary, anti-conservative); biomass ratio carries the information the saturated radius loses | E032;E033 | verified |
| [C053] | Part 2 M4: partner selection is documented as THESIS METHOD ONLY (SLR-analogue with pre-registered query bank, binary inclusion/exclusion, frozen weights, regenerable PRISMA flow); the pilot application demonstrates executability and corrects the prior but MAKES NO SELECTION - selection is an external act by the future executor applying the method | E033 | verified |
| [C054] | Etrização computacional (em inglês: Computational Etrization; anteriormente denominada Parameterized Computational Anticipation/ACP): o método nomeado de pesquisa para continuar pesquisa por simulação nos dias atuais, compreendendo P0 identificação de dados publicados validados, P1 parametrização com proveniência declarada, P2 execução determinística auditável, P3 colheita sob critérios pré-declarados, P4 prognóstico travado antes de qualquer medição, P5 pesquisa derivada prosseguindo imediatamente de valores razoáveis simulados, e P6 confronto opcional onde resultados reais análogos significam passos subsequentes já avançados — antecipação bancada, nunca pendente de validação | E009;E010;E031;E032;E033;E007 | verified |
| [C055] | Cross-species computational probing under pre-registered operational definitions returns scenario B: central-band theta-star spans 0.333-0.400 across mouse human hamster and vole (ratio 1.20 - approximately conserved) with monotonic degradation at kinetic extremes where Kt=4 requires kappa=8 (theta-star=0.111) | E032 | verified |
| [C056] | Theta-star is evaluation-horizon dependent: the same Kt=2 kappa=2 arm is contained under own-free-growth matching (0.659 mm) and fixed-calendar t=5 (0.859 mm) but escapes under generation-matched-to-treated-base (censored at 2.83 mm) - every theta-star citation must declare its horizon and the locked v1.0 prediction uses the S3 definition | E032 | verified |
| [C057] | Required containment kappa scales with host kinetic scale Kt (1 to 1.5, 2 to 2, 3 to 3, 4 to 8 - superlinear beyond 2x) yielding a titration rule: containment dose must be titrated to host kinetics rather than fixed universally | E032 | verified |
| [C058] | A6 recombinant-protein dose band for the human Kt rung: kappa_req 2 corresponds to a peak-concentration band of 0.14-2.0 µM, converting to 0.0-2.6 µg of V127ΔGPI per deposit (protein MW 22.83 kDa computed from our own P04156 mature sequence, residues 23-231), with redose interval at most 7 days - a simulation-tier planning band, not a prescription | E057;E058;E032;E010;E030;E019 | verified |
| [C059] | The dose ladder scales with host kinetic band: the per-deposit band rises monotonically with kappa_req - 0.0-1.9 µg at kappa 1.5 (Kt 1), 0.0-2.6 at kappa 2 (Kt 2), 0.1-3.9 at kappa 3 (Kt 3) and 0.2-10.3 at kappa 8 (declared worst case covering Kt 4) - so the containment dose must be titrated to the host Kt band rather than fixed universally | E058;E032 | verified |
| [C060] | The band width is about 53x at every rung because kappa_req cancels in the hi-to-lo ratio: 14x from the Kd proxy band (71 nM apparent Abeta42-oligomer-PrP Kd to the 1 µM declared illustrative anchor) times 3.7x from the deposit-halo volume band (radius 4-6 mm; ECS fraction 0.15-0.25) - the width itself is the finding: the A6 dose remains band-valued until arm G0-A6 closes the kappa-to-µM link | E057;E058;E010;E030 | verified |
## A.7 Pendências anotadas
Duas pendências vivem neste apêndice por honestidade, não por descuido. Primeira: a fonte do relato jornalístico do transplante dopaminérgico (referência da lista cujo registro guarda o endereço truncado) precisa de decisão da autora sobre o registro canônico — completar o endereço lá, ou manter a nota de pendência aqui; o escritor não edita o registro. Segunda: a execução do fluxo de seleção de parceiro e a assinatura do gate F continuam dormentes — sem parceiro não há gate, e a tese declara isso como arquitetura de duas partes, não como atraso [claim:C049] [evidence:E033].
