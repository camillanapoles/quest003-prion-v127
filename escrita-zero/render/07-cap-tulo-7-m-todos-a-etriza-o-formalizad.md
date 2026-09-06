# CAPÍTULO 7 — MÉTODOS: A ETRIZAÇÃO FORMALIZADA
Este capítulo formaliza o método: o pipeline P0–P6 com garantia por passo, a formulação matemática com proveniência, a Base de Validade e o mapeamento que permite ler a tese como experimental. Quem auditou teses experimentais sabe o que procura; aqui está tudo em forma equivalente.
## 7.0 O pipeline P0–P6
O método tem sete passos, cada um com garantia própria:
| Passo | Operação | Garantia |
|---|---|---|
| P0 | identificação de dados publicados validados | tudo o que entra é publicado e verificável |
| P1 | parametrização com proveniência declarada | cada parâmetro carrega sua fonte |
| P2 | execução determinística auditável | re-executar reproduz o resultado |
| P3 | colheita sob critérios pré-declarados | nada é colhido que não foi anunciado |
| P4 | prognóstico travado antes de qualquer medição | a predição precede o confronto |
| P5 | pesquisa derivada prossegue de imediato com valores razoáveis simulados | a pesquisa não espera validação |
| P6 | confronto opcional, com passos subsequentes já avançados | antecipação pronta na bancada, nunca pendente |
Esses passos definem a etrização computacional — antes Antecipação Computacional Parametrizada — como o método nomeado de continuar pesquisa por simulação nos dias atuais [claim:C054] [evidence:E009,E010,E031,E032,E033,E007].
## 7.1 O método nomeado
Nomear não foi ornamento: foi condição de operação. Sem nome, o conjunto P0–P6 seria um procedimento ad hoc de um grupo; com nome, definição operacional e garantias, é método auditável por qualquer terceiro [claim:C054] [evidence:E009,E010,E031,E032,E033,E007]. A garantia transversal é a cronologia: as predições do programa foram registradas publicamente, com carimbo de tempo, antes de qualquer experimento úmido existir [claim:C040] [evidence:E033] — o anti-retrospectiva é estrutural, não retórico.
## 7.2 Formulação matemática com proveniência
A quantidade central é adimensional: θ ≡ (1 + κ·c_pico)⁻¹ — a fração de replicação remanescente no pico secretor, com κ a força de bloqueio e c_pico a concentração de pico do agente. O estimador observacional segue a mesma forma: θ̂ = 1/(1+κ̂), com κ̂ — o κ estimado — obtido por vizinho-mais-próximo na grade do motor; a calibração em simulação atende critérios pré-declarados na fronteira de decisão, com a variante interpolada testada e rejeitada [claim:C052] [evidence:E032,E033]. O limiar de contenção é θ* igual a 0,333, com frente contida em κ=2 [claim:C038] [evidence:E032].
A dinâmica vem de componentes publicados: o kernel é o modelo estocástico de reação-difusão com código aberto, de Gillespie sobre classes de agregados com templating [claim:C013] [evidence:E009]; o consumo de primeira ordem foi varrido de 10⁻⁶ a 10⁻⁵ por segundo, ancorado na cinética de polimerização nucleada [claim:C015] [evidence:E011,E030]; o transporte intersticial usa fração de volume de cerca de 0,20 e tortuosidade de cerca de 1,8 medidas *in vivo* [claim:C014] [evidence:E010,E030]. A humanização é reescalamento global do tempo — uma unidade de simulação igual a 144 dias, tempo de duplicação humano derivado de 12,1 dias das âncoras [claim:C037] [evidence:E032,E007] — com taxas relativas murinas até ajuste por séries publicadas [claim:C043] [evidence:E032,E009]. Cada constante da tese remonta a uma dessas âncoras: nenhuma é digitada sem procedência.
## 7.3 A Base de Validade (mandatória)
A Base de Validade tem três pernas — o kernel publicado [claim:C013] [evidence:E009], as âncoras de relógio humanas [claim:C009] [evidence:E007] e o motor com auto-testes declarados (conservação de massa de 100,0%; erro numérico-analítico de 0,5% no comprimento de Thiele) [claim:C032] [evidence:E030] — e um critério de uso: o gate computacional G0-sim, executado, aprovado e reproduzido, é a validação da tese neste estágio, e nada além dele se alega [claim:C046] [evidence:E032,E009,E007,E033]. O rótulo de dado viaja com cada saída: a escada de portões G0-sim, G0-wet, G1 e G2 obriga toda predição a declarar seu nível de evidência [claim:C047] [evidence:E033]. A seleção de parceiros, quando a continuidade exigir, é método documentado análogo à revisão sistemática — banco de consultas pré-registrado, critérios binários, pesos congelados — sem seleção e sem contato [claim:C053] [evidence:E033].
## 7.4 A tese em forma experimental: o mapeamento análogo
A hipótese H1 afirma que um examinador de tese experimental auditaria esta tese trocando apenas os termos. O mapeamento:
| Elemento experimental | Elemento da etrização |
|---|---|
| participantes | fontes publicadas (P0) |
| instrumento de medição | código do motor, com auto-testes [claim:C032] [evidence:E030] |
| coleta de dados | execução determinística (P2) |
| caderno de campo | registro público com carimbo de tempo [claim:C040] [evidence:E033] |
| pré-registro | prognóstico travado antes da medição (P4) [claim:C051] [evidence:E032,E033] |
| análise estatística | colheita sob critérios pré-declarados (P3) |
| revisão por pares | revisor hostil de máquina + validação da autora |
| replicação | re-execução auditável (P2) |
| trabalho futuro | pesquisa derivada imediata (P5–P6) [claim:C049] [evidence:E033] |
Lido pela direita, o mapeamento mostra onde cada garantia experimental tem equivalente documental; lido pela esquerda, mostra que nada do rigor foi trocado por simulação — o que mudou foi a matéria-prima: dado publicado no lugar de participante, motor no lugar de instrumento. A forma da tese permanece a de um experimento.
