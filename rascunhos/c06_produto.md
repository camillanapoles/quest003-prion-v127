# CAPÍTULO 6 — O PRODUTO: O DESENHO TERAPÊUTICO EMERGE

O produto da tese é um desenho: regras de posicionamento e entrega, uma dose legitimada pela banda do alicerce, um ensaio capaz de matar a hipótese e um custo cotável. Nada aqui é prescrição — é prognóstico rotulado, derivado dos dados publicados, pronto para o confronto.

## 6.1 Três regras de transporte, falseáveis

A física do transporte entrega três regras de desenho, cada uma derivada e cada uma refutável. Regra 1 — posicionamento: o anel de contenção tem nós espaçados de 8 a 12 mm, com raio de proteção de 4 a 6 mm por depósito [claim:C033] [evidence:E030]. Regra 2 — suporte: a malha do hidrogel deve exceder cinco vezes o raio da proteína; ácido hialurônico a 1–2% passa, acima de 5% sequestra o secretoma [claim:C034] [evidence:E030]. Regra 3 — redose: intervalo de sete dias ou menos mantém o vale entre pulsos em 56% do pico; dez a quatorze dias deixam vales [claim:C035] [evidence:E030]. As três regras dizem onde depositar, em que suporte e com que ritmo — o que faltava aos seis candidatos que fracassaram sem modelo de entrega [claim:C050] [evidence:E021,E022,E034,E035,E036,E037,E038].

## 6.2 O limiar travado e a dose legitimada pela banda

O desenho se ancora no limiar travado do experimento 1: θ* igual a 0,333, com a frente contida em κ=2 — de 2,83 para 0,82 mm [claim:C038] [evidence:E032]. A sondagem multi-espécie legitimou esse valor: a banda central de 0,333 a 0,400 atravessa camundongo, humano, hamster e rato-de-campo [claim:C055] [evidence:E032], e a titulação pela cinética do hospedeiro (Kt 1→κ 1,5; Kt 2→κ 2; Kt 3→κ 3; Kt 4→κ 8) define quando a dose de desenho vale e quando deve subir [claim:C057] [evidence:E032]. A dose κ=2 é, portanto, legítima na banda herdada do humano — e a regra de titulação, não a intuição, manda fora dela.

## 6.3 A primeira dose calculada (cadeia κ→µM→µg) [SIM-planejamento]

O salto do adimensional ao mensurável é a cadeia de tradução: o κ exigido no degrau humano (κ 2) corresponde a uma banda de concentração de pico de 0,14 a 2,0 µM, que se converte em 0,0 a 2,6 µg da forma V127ΔGPI — a variante sem âncora glicosilfosfatidilinositol (ΔGPI) — por depósito, com a massa molecular de 22,83 kDa calculada a partir da própria sequência madura (resíduos 23–231) [SIM] [claim:C058] [evidence:E057,E058,E032,E010,E030,E019]. A escada completa sobe monotonicamente com a cinética: 0,0–1,9 µg em κ 1,5; 0,0–2,6 µg em κ 2; 0,1–3,9 µg em κ 3; 0,2–10,3 µg no pior caso declarado κ 8 [SIM] [claim:C059] [evidence:E058,E032]. A largura de cerca de 53 vezes, constante em todos os degraus, é ela mesma informativa: o κ exigido cancela na razão topo/piso, restando 14 vezes do intervalo do proxy de afinidade [SIM] [claim:C060] [evidence:E057,E058,E010,E030]. A escada de dose, com o pior caso hachurado, compõe a Figura 5; a tabela a seguir a resume.

| Degrau (Kt) | κ exigido | Banda por depósito [SIM] |
|---|---|---|
| Kt 1 | 1,5 | 0,0–1,9 µg [claim:C059] [evidence:E058,E032] |
| Kt 2 (humano) | 2 | 0,0–2,6 µg [claim:C058] [evidence:E057,E058,E032,E010,E030,E019] |
| Kt 3 | 3 | 0,1–3,9 µg [claim:C059] [evidence:E058,E032] |
| Kt 4 (pior caso) | 8 | 0,2–10,3 µg [claim:C059] [evidence:E058,E032] |

É uma dose de planejamento, não uma prescrição: o rótulo [SIM] viaja com o número, e o braço A6 do ensaio é o que fecha a tradução κ↔concentração com dose conhecida.

## 6.4 G0-wet: o ensaio especificado para matar a hipótese

O gate de organoide (G0-wet) está especificado na escada declarada de portões — computacional executado, organoide especificado, camundongo humanizado e primeiro-uso-em-humano condicionais, com toda predição futura rotulada pelo seu nível [claim:C047] [evidence:E033]. O ensaio tem oito braços; a análise é braço-a-braço, Welch contra o braço-controle com correção de Holm nas cinco comparações, com n de 8 por braço extensível a 12 e poder declarado; o avaliador do PrP-res é cego ao braço; e cada braço carrega kill-switch — se nenhum gradiente apresentar θ_obs acima de 0,33, o programa encerra e publica o negativo. O instrumento de leitura é o estimador θ_obs, calibrado em simulação com critérios pré-declarados — adequado na fronteira de decisão, conservador em κ alto, com a variante interpolada testada e rejeitada [claim:C052] [evidence:E032,E033]. Um controle de mesma massa (MV1 semeado com o inóculo de massa MV2) está na fila para separar efeito de massa de cinética de subtipo [claim:C045] [evidence:E033].

A especificação é deliberadamente letal por desenho: um ensaio que não pode matar a hipótese não valida nada.

## 6.5 Custo-cotação: a tabela S1

O envelope de planejamento do G0-wet é de 100 a 150 mil dólares em dez meses [claim:C040] [evidence:E033]. A tabela S1 decompõe esse envelope em dez direcionadores estruturais — quantidades derivadas do protocolo, preços unitários deliberadamente ausentes: preço só entra como cotação assinada e datada de parceiro (regra do preço-como-identificador). As quantidades da tabela são especificação protocolar (declarações de desenho, não medições) e carregam essa natureza; a especificação completa do ensaio, com o plano de análise, é aberta no Cap. 7 e reproduzida no anexo (Cap. 15).

| # | Direcionador | Unidade | Quantidade (n=8) |
|---|---|---|---|
| 1 | Organoides (diferenciação de iPSC) | organoide | 64 (+≈10% reserva) |
| 2 | Meio e fatores de crescimento | kit-mês | ≈70 × 4–5 meses |
| 3 | Inóculo sCJD (isolados MV1/MV2) + manuseio BSL-príon | lote/mês | 1 lote duplo × ≈6 meses |
| 4 | Construto A6 (V127ΔGPI recombinante, grau GMP-like) | mg | escalada de dose (3 × braço) |
| 5 | Vetor A7 (LNP-mRNA, análogo intratecal *in vitro*) | lote | 2–3 lotes |
| 6 | Braço celular A5 (linhagem secretora ou controle) | lote celular | 1–2 |
| 7 | Controle positivo A8 (pentosan polissulfato) | frasco | 1 |
| 8 | Leituras (WB/IHC/RT-QuIC, avaliação cega) | ensaio × organoide | ≈70 × 2–3 tempos |
| 9 | Pessoal (1 técnico + pós-doutorando parcial) | pessoa-mês | ≈15 |
| 10 | Sobrecarga institucional (BSL-3, taxas) | % | 15–30% |

O desenho emerge, portanto, completo e honesto: regras de transporte falseáveis, dose legitimada pela banda e titulada pela cinética, ensaio letal por desenho e custo pronto para cotação. O que o Cap. 7 fará é abrir a caixa do método que produziu tudo isto.
