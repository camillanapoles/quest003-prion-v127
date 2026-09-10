# APÊNDICE B — MAPA DA LÓGICA
Este apêndice é o mapa de como a tese pensa: de onde veio cada informação, por onde ela passou, que decisões foram tomadas no caminho, o que foi tentado e descartado, e quais perguntas a banca faria antes mesmo de virarem perguntas. O leitor que quiser uma única página para se orientar antes de mergulhar nos capítulos achou o lugar.
## B.1 O fluxo da informação: da literatura à conclusão
Nada nesta tese é informação de segunda mão. Cada afirmação factual seguiu um caminho único: sai de uma fonte pública verificada ou de uma execução pré-registrada do programa, vira claim do registro probatório — com soma criptográfica que amarra o texto ao congelado —, e só então entra nos capítulos, sempre com a etiqueta que a devolve à origem. O mapa abaixo mostra esse caminho; as contagens vêm do mesmo banco que gerou o apêndice A.
    Literatura pública — fontes verificadas (lista nas REFERÊNCIAS)
           │  variantes V127/G127V · kernel publicado · âncoras de organoide
           ▼
    Registro probatório — claims com soma criptográfica · N-fatos numerados
           ▲
           │  pré-registros e execuções com datas impressas (Apêndice A.1–A.3)
    Programa — WS-7 → WS-8 → WS-9 → M31 (auto-testado, re-executável)
           │  citação com etiqueta [claim:] [evidence:]
           ▼
    Tese — Capítulos 2 a 13 ──► G0-wet desenhado e congelado (Apêndice A.4)
A força do mapa está no que ele impede: não existe seta de "achismo" para capítulo, nem de capítulo para número sem etiqueta. Quando o Capítulo 8 afirma um resultado, a seta atravessa o registro e termina num arquivo executável; quando o Capítulo 3 afirma um fato da literatura, a seta termina numa fonte que qualquer leitor pode abrir. Para auditar uma seta: siga-a até a tabela correspondente do apêndice A, confira a data e o hash do commit, e a etiqueta do parágrafo que a citou devolve o resto.
## B.2 Decisões-chave — e por quê
| Decisão | Por quê | Onde | Âncora |
|---|---|---|---|
| Nomear a etrização computacional | método novo precisa de nome, definição operacional e produto nomeado para ser auditável | Cap. 7 | [claim:C054] [evidence:E009,E033] |
| Objetivo sem ano-calendário | a tese depende de gate úmido com parceiro que não se escolhe sozinha — prometer data seria prometer o que não controla | Cap. 2 | [claim:C048] [evidence:E030,E031,E032,E033] |
| Humanização como reescala global do tempo | mantém as taxas relativas murinas e troca só o relógio — o mínimo de interpretação possível | Cap. 5 | [claim:C043] [evidence:E032] |
| Estimador por vizinho-mais-próximo mantido | a variante interpolada suavizava entre braços e piorava a fronteira de decisão exatamente onde a predição vive | Cap. 8 | [claim:C052] [evidence:E032,E033] |
| Controle de mesma massa | separa efeito de subtipo de efeito de massa de inóculo antes que a banca pergunte | Cap. 6 | [claim:C045] [evidence:E033] |
| Regra de horizonte após a rachadura | a descoberta de que θ* depende do horizonte virou regra de citação, não exceção escondida | Cap. 5 | [claim:C056] [evidence:E032] |
| Parceiro como método, sem seleção e sem contato | escolher parceiro seria decidir o resultado; o método escolhe quando o parceiro aparecer | Cap. 8 | [claim:C053] [evidence:E033] |
| Arquitetura de duas partes | Parte 1 entrega os achados que o simulação pode sustentar; Parte 2 é a tese de continuidade úmida | Cap. 2 | [claim:C049] [evidence:E032,E033] |
| Escada de portões como régua | progresso medido por gate aprovado, não por calendário nem por ânimo | Cap. 8 | [claim:C047] [evidence:E032,E033] |
| Rotulagem explícita do que é simulação | predição travada, simulação rotulada — o rótulo é o contrato com o leitor | Cap. 7 | [claim:C046] [evidence:E032,E033] |
## B.3 Rejeições documentadas — o que não funcionou
Uma tese que só lista acertos está escondendo metade do conhecimento. As rejeições abaixo estão nos capítulos com o mesmo peso dos resultados positivos.
| O que foi rejeitado | O que se esperava | O que aconteceu | Âncora |
|---|---|---|---|
| Variante interpolada do estimador | interpolação suave entre braços daria precisão sem custo | suavizou a fronteira de decisão e quebrou a cobertura no braço alto — rejeitada, a de vizinho-mais-próximo ficou | [claim:C052] [evidence:E032,E033] |
| Predição derivada do hamster sob a definição S3 | a conservação entre espécies se confirmaria em qualquer definição de horizonte | sob gerações casadas à base tratada a frente escapa — a refutação virou a regra de horizonte | [claim:C056] [evidence:E032] |
| Os seis antiprion históricos | quinacrina, doxiciclina, polissulfato de pentosana, flupirtina e anticorpo monoclonal deveriam deter a doença | nenhum mudou o desfecho de sobrevida — o fracasso informou o desenho em camadas da tese | [claim:C050] [evidence:E034,E035,E036,E037,E038] |
| Estudo de minociclina com FK506 em hamsters | a combinação anti-inflamatória havia mostrado ganho de sobrevida | o estudo foi retratado — a tese cita como alerta, não como apoio | [claim:C050] [evidence:E021] |
## B.4 Glossário contextual
Definições curtas, no lugar onde o leitor precisa delas; a lista formal de siglas fica nos elementos pré-textuais.
| Termo | Definição de trabalho | Onde nasce |
|---|---|---|
| etrização | formalização computacional de uma plataforma terapêutica com garantia por passo | Cap. 2 |
| kernel estocástico | modelo de reação-difusão publicado que descreve a propagação priônica | Cap. 4 |
| âncoras de relógio | parâmetros de tempo medidos em organoides que ancoram o relógio humano | Cap. 4 |
| humanização | troca do relógio murino pelo humano mantendo as taxas relativas | Cap. 5 |
| θ* (teta-estrela) | limiar de fração de dose em que a frente de propagação é contida | Cap. 5 |
| banda central | intervalo de θ* entre espécies dentro da sondagem pré-registrada | Cap. 5 |
| κ exigido | dose relativa que o hospedeiro pede para conter a frente | Cap. 5 |
| θ_obs (teta-observado) | estimador que lê contenção a partir do dado de bancada | Cap. 8 |
| G0-sim | gate computacional já executado: a validação da tese neste estágio | Cap. 8 |
| G0-wet | gate úmido desenhado e congelado, à espera de parceiro | Cap. 8 |
| tabela-mãe | tabela de marcos que contrata objetivos, hipóteses e entregas | Cap. 2 |
| Base de Validade | tríade kernel publicado, âncoras de relógio, motor auto-testado | Cap. 7 |
| predição discriminadora | predição que falsifica uma de duas formas funcionais | Cap. 6 |
| controle de mesma massa | braço que isola efeito de subtipo do efeito de massa de inóculo | Cap. 6 |
| regra de horizonte | citação de θ* sempre acompanhada da definição de horizonte | Cap. 5 |
| escada de portões | sequência de gates que mede progresso sem calendário | Cap. 8 |
## B.5 Objeções da banca — respondidas antes da pergunta
*— "No fim das contas, é só simulação?"* Não — e a tese nunca vendeu como. O gate computacional é a validação do estágio, executado, aprovado e reproduzido [claim:C046] [evidence:E032,E033]; o que é simulação está rotulado como tal em cada uso [claim:C047] [evidence:E032,E033], e a arquitetura declara que o úmido é Parte 2 [claim:C049] [evidence:E032,E033]. A pergunta certa não é se é simulação, é se a simulação é auditável — e é.
*— "Onde está o experimento de verdade?"* Desenhado, pré-registrado e congelado: o ensaio de organoides tem protocolo, checklist de congelamento e estimador calibrado à espera [claim:C052] [evidence:E032,E033]; a seleção de parceiro é método sem seleção e sem contato [claim:C053] [evidence:E033]. Fazer o ensaio sem parceiro não era uma opção honesta — era a única alternativa a mentir sobre a autoria.
*— "Por que confiar num modelo?"* Porque a confiança não vem do modelo, vem da cadeia: kernel publicado com código aberto [claim:C013] [evidence:E009], âncoras medidas em organoides [claim:C009] [evidence:E007], motor com auto-testes [claim:C032] [evidence:E030], execuções reproduzidas em ambiente independente [claim:C040] [evidence:E033] e sensibilidade colhida sem mover o limiar [claim:C051] [evidence:E032,E033]. Cada elo tem etiqueta.
*— "O hamster não refutou a conservação?"* Refutou a versão ingênua dela — e a tese imprimiu a refutação. A dependência de horizonte foi descoberta, declarada e convertida em regra de citação [claim:C056] [evidence:E032]; a banda entre espécies segue de pé sob a definição pré-registrada que a anunciou [claim:C055] [evidence:E032]. Uma conservação que sobrevive só com definição declarada é mais forte que uma que nunca foi confrontada.
*— "A dose em microgramas saiu de onde?"* Da cadeia de titulação com pedra de toque na própria sequência: a capa exigida por cinética do hospedeiro [claim:C057] [evidence:E032] é convertida em banda de concentração e massa por deposit com incerteza propagada [claim:C058] [evidence:E058,E032], a escada sobe monotônica com a cinética [claim:C059] [evidence:E058,E032] e a largura da banda tem explicação analítica — o requisito cancela na razão [claim:C060] [evidence:E058,E010,E030,E057].
*— "E se nada disso der certo no úmido?"* A tese já declarou o desfecho negativo como resultado legítimo: os kill-switches por braço encerram o programa e publicam o negativo [claim:C046] [evidence:E032,E033]; a continuidade está na infraestrutura e na documentação, não na promessa de sucesso [claim:C047] [evidence:E032,E033]. Um programa que pode falhar publicamente é o único que merece confiança quando acerta.
