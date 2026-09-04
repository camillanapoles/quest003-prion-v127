# CAPÍTULO 2 — INTRODUÇÃO

Este capítulo fixa o contrato da tese: problema, justificativa, questões, objetivos, hipóteses e componentes — nesta ordem, e antes de qualquer evidência. O que se promete aqui é cobrado nos capítulos de resultados e encerrado no Cap. 13, um por um.

## 2.1 Problema

A pesquisa translacional em doenças raras e fatais trava num dilema conhecido: sem dado clínico não há financiamento; sem previsão quantitativa, o dado que existe é desperdiçado. Nas doenças priônicas, o dilema está documentado, caso a caso. Seis candidatos terapêuticos chegaram ao paciente e fracassaram — quinacrina em ensaio de Classe I sem ganho de sobrevida, doxiciclina em fase 2 randomizada sem efeito significativo, pentosan polissulfato intraventricular em série de casos com efeito biológico sem cura, flupirtine com desfecho cognitivo sem sobrevida, o anticorpo PRN100 em primeiro-uso-em-humano sem eficácia clínica clara, e combinações com minociclina com o ensaio retraído excluído por regra — todos sem um modelo quantitativo de entrega que lhes dissesse o que medir, onde medir e em que dose [claim:C050] [evidence:E021,E022,E034,E035,E036,E037,E038].

O paradoxo é que a biologia necessária já está publicada. A variante G127V, selecionada durante a epidemia de kuru, protege: camundongos transgênicos homozigotos V127 são completamente resistentes a todas as cepas priônicas testadas, com proteção equivalente à deleção do gene [claim:C001] [evidence:E001]; heterozigotos G/V127 resistem a kuru e à forma clássica da doença de Creutzfeldt-Jakob, embora permaneçam infectáveis pela forma variante [claim:C002] [evidence:E001]; e o V127 atua como inibidor dominante-negativo potente e dose-dependente da propagação da proteína selvagem [claim:C003] [evidence:E001,E003,E005]. O gargalo, portanto, não é mecanístico — é de método: falta a capacidade de converter, de imediato, o conhecimento publicado no planejamento quantitativo do passo terapêutico seguinte.

O problema que esta tese assume é o da **continuidade**: como uma pesquisa avança hoje, com método auditável, quando a validação experimental é essencial, mas não é pré-requisito para produzir conhecimento novo?

## 2.2 Justificativa

Três razões sustentam a empreitada.

A primeira é epistêmica. Simulação parametrizada com dados reais publicados é prognóstico: opera no tempo futuro e não depende de ano-calendário. Os ingredientes existem e são de acesso público — um modelo estocástico de reação-difusão da propagação priônica, com código aberto [claim:C013] [evidence:E009]; organoides cerebrais humanos suscetíveis à infecção por forma esporádica, com cinética dependente de subtipo [claim:C009] [evidence:E007]; e o registro público das predições, com carimbos de tempo anteriores à existência de qualquer experimento úmido [claim:C040] [evidence:E033]. Interromper essa cadeia à espera de confirmação laboratorial reduziria a produção de conhecimento sem ganho de rigor.

A segunda é ética e econômica. Cada experimento desperdiçado em príon custa meses e recursos escassos — em doença com sobrevida de meses. Decidir o que medir, onde e em que dose *antes* de gastar não é luxo metodológico: é responsabilidade.

A terceira é metodológica. As ferramentas de rigor documental hoje disponíveis — revisão sistemática auditável, código aberto, uma moldura bayesiana que converte expectativa de portão em probabilidade declarada [claim:C036] [evidence:E031] e pré-registro — permitem um padrão de auditoria equivalente ao experimental; o gate computacional G0-sim já foi executado, aprovado e reproduzido [claim:C046] [evidence:E032,E009,E007,E033]. O que faltava era formalizar esse padrão como método com nome, passos e garantias — e é isso que esta tese entrega.

## 2.3 Questões de pesquisa

- **Q1.** É possível formalizar um método de continuidade de pesquisa por simulação computacional com o mesmo rigor documental de uma tese experimental?
- **Q2.** Esse método, aplicado ao caso V127, produz resultados próprios — não meros planos — com validade declarada e linhagem completa?
- **Q3.** Como esse método se posiciona e se diferencia da família existente de métodos antecipatórios, em particular a meta-análise e os ensaios *in silico*?

## 2.4 Objetivos

O objetivo geral, declarado sem ano e definido por resultados: conduzir a pesquisa até o fim de seu arco no ambiente simulado, com dados reais parametrizados, colher os resultados completos da simulação e validar portão por portão; a metodologia de continuação computacional — revisão sistemática, física parametrizada, moldura bayesiana e portões *in silico* pré-registrados — é a inovação em avaliação antecipatória de pesquisa [claim:C048] [evidence:E033].

Os objetivos específicos são quatro:

- **OE1 — nomear e formalizar.** Nomear a etrização e formalizá-la com os passos P0–P6 e garantias por passo, nomeando também o seu produto [claim:C054] [evidence:E009,E010,E031,E032,E033,E007].
- **OE2 — Base de Validade.** Estabelecer a Base de Validade: tríade de dados declarada e linhagem completa, com o gate G0-sim como validação executada [claim:C046] [evidence:E032,E009,E007,E033].
- **OE3 — resultados como achados.** Entregar os resultados da simulação já realizada como os achados próprios da tese: limiar de contenção, regras de desenho, colheita de sensibilidade e estimador [claim:C038] [evidence:E032] [claim:C051] [evidence:E032,E033] [claim:C052] [evidence:E032,E033].
- **OE4 — continuidade documentada.** Documentar a continuidade futura como método replicável — seleção de parceiro análoga à revisão sistemática, sem executá-la [claim:C053] [evidence:E033].

## 2.5 Hipóteses

- **H1 (metodológica).** A etrização é formalizável com rigor documental equivalente ao experimental. Predição discriminadora: um examinador de tese experimental consegue auditá-la trocando apenas os termos do mapeamento análogo (pessoa→fonte, instrumento→código, coleta→execução), sem perder a tese de vista.
- **H2 (de caso).** A etrização aplicada ao caso V127 gera resultados próprios, falsificáveis, independentes de medição. As predições foram travadas antes de qualquer confronto: contenção da frente abaixo do limiar declarado — θ* igual a 0,333, a fração de replicação remanescente no pico secretor abaixo da qual a frente é contida [claim:C038] [evidence:E032] —, insensibilidade do limiar à variação de dez vezes no parâmetro logístico, e dose-resposta que distingue a forma funcional do bloqueio [claim:C051] [evidence:E032,E033].
- **H3 (de posicionamento).** A etrização ocupa espaço estrutural distinto dos ensaios *in silico* e das sínteses de evidência: prognóstico travado antes da medição, simulação rotulada, antecipação pronta na bancada e pesquisa derivada imediata.

## 2.6 Estrutura do documento

A tese se organiza em arco único. A nota à banca (Cap. 1) nomeou o método e o diferenciou. Este capítulo fixa o contrato. A fundamentação (Cap. 3) situa o problema biomédico e a família de métodos antecipatórios. A base comum de dados (Cap. 4) une fundamento e aplicação sob os mesmos dados reais, com cronologia honesta exibida como força. O alicerce (Cap. 5) estabelece a invariância do limiar entre espécies; o produto (Cap. 6) faz o desenho terapêutico emergir desse alicerce, com titulação de dose. Os Cap. 7 e 8 apresentam métodos e resultados [SIM]; o Cap. 9 nomeia os achados; o Cap. 10 discute o que significam e o que não significam; o Cap. 11 projeta a leitura clínica; o Cap. 12 declara os limites; o Cap. 13 devolve veredito por objetivo; as referências (Cap. 14) e os anexos de pré-registro (Cap. 15) fecham o corpo; o mapa lógico (Cap. 16) e o front-matter com a lista consolidada de siglas completam o volume. A arquitetura de duas partes permanece como declaração de escopo: a Parte 1, pré-G0, produz os achados da simulação; a Parte 2, pós-G0, é a tese de continuidade — pesquisa e validação usando os dados parametrizados da simulação [claim:C049] [evidence:E033].

## 2.7 Componentes M1–M5 (tabela-mãe validada pela autora)

A continuidade não se promete em abstrato: ela tem componentes com nome, estado e artefato. A tabela-mãe abaixo reúne os componentes M1–M5 sob a base validada *in silico* — o gate G0-sim executado, aprovado e reproduzido é a validação da tese neste estágio [claim:C046] [evidence:E032,E009,E007,E033] — e liga cada objetivo específico a uma hipótese e aos componentes que o cumprem. A redefinição da tabela foi validada expressamente pela autora, e a folha de validação integra o anexo de pré-registro (Cap. 15).

| Componente | O que é | Estado | Cumpre |
|---|---|---|---|
| M1 — estimador θ_obs | mede, num gradiente espacial, o análogo do limiar θ* — fração de replicação remanescente no pico secretor, adimensional —, comparável ao limiar travado (simulado hoje, medido amanhã); calibrado em simulação com critérios pré-declarados [claim:C052] [evidence:E032,E033] | executado e aprovado | OE3, H2 |
| R1 — resultados como resultados | os achados da simulação realizada são os resultados da tese; nada fica pendente de laboratório para valer | realizado | OE3, H2 |
| M2 — congelamento (freeze) | extensão futura opcional ao gate de organoide; especificada e dormente | especificado (dormente) | OE4 |
| M3 — laço de re-parametrização | realimentação sem retro-alterar predições — o mecanismo anti-retrospectiva entre cenários | especificado | OE4 |
| M4 — seleção de parceiro | método análogo à revisão sistemática, com banco de consultas pré-registrado, critérios binários e pesos congelados — sem seleção, sem contato [claim:C053] [evidence:E033] | método documentado | OE4 |
| M5 — infraestrutura de continuidade | guardião e livro de execução: continuidade por método, não por memória | operante | OE4 |

A escada de portões fecha o contrato: G0-sim executado *in silico*; G0-wet, em organoide, especificado; G1, camundongo humanizado, condicional; G2, primeiro uso em humano, condicional — e toda predição futura carrega o rótulo do seu portão [claim:C047] [evidence:E033]. O cruzamento objetivo × hipótese × componente resume-se assim: OE1 testa H1 com o método formalizado; OE2 sustenta H1 com a Base de Validade; OE3 realiza H2 com M1 e R1; OE4 documenta a continuidade que H3 posiciona. O que a tabela promete, o Cap. 13 julga — objetivo por objetivo, hipótese por hipótese.
