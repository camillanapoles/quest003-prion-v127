# ETRIZAÇÃO COMPUTACIONAL EM DOENÇAS PRIÔNICAS: APLICADA À PLATAFORMA TERAPÊUTICA PrP-V127

## RESUMO

Esta tese nomeia, formaliza e valida uma forma de fazer pesquisa quando o laboratório não está ao alcance e a doença mata em meses: a etrização computacional [claim:C054] [evidence:E009,E033], aplicada à plataforma terapêutica da variante protetora PrP-V127. O programa é pré-registrado antes de cada execução [claim:C040] [evidence:E033]; o limiar de contenção é travado — um terço da dose basta para conter a frente em hospedeiro humano sob o relógio humanizado [claim:C038] [evidence:E032]; a conservação entre espécies é declarada com sua banda [claim:C055] [evidence:E032]; a dose titula-se pela cinética do hospedeiro com cadeia completa até microgramas [claim:C057] [evidence:E032] [claim:C059] [evidence:E058,E032]; o estimador que lerá o dado de bancada é calibrado em simulação com critérios pré-declarados [claim:C052] [evidence:E032,E033]; e o ensaio úmido está desenhado, congelado e à espera de parceiro [claim:C053] [evidence:E033]. A validação deste estágio é o gate computacional, executado e reproduzido [claim:C046] [evidence:E032,E033]; a arquitetura declara duas partes — os achados que a simulação sustenta e a continuidade que depende do úmido [claim:C049] [evidence:E032,E033]. Cada afirmação carrega etiqueta que a devolve ao registro probatório: a tese é auditável linha a linha.

Palavras-chave: doenças priônicas; PrP-V127; etrização computacional; simulação pré-registrada; plataforma terapêutica.

## ABSTRACT

This thesis names, formalizes and validates a way of doing research when the laboratory is out of reach and the disease kills within months: computational etrization — the English form of the named method [claim:C054] [evidence:E009,E033], applied to the therapeutic platform of the protective variant PrP-V127. The program pre-registers every run [claim:C040] [evidence:E033]; the containment threshold is locked — one third of the dose contains the front in the human host under the humanized clock [claim:C038] [evidence:E032]; cross-species conservation is declared with its band [claim:C055] [evidence:E032]; the dose is titrated by host kinetics with a complete chain down to micrograms [claim:C057] [evidence:E032] [claim:C059] [evidence:E058,E032]; the estimator that will read the bench data is simulation-calibrated under pre-declared criteria [claim:C052] [evidence:E032,E033]; and the wet assay is designed, frozen and awaiting a partner [claim:C053] [evidence:E033]. The validation of this stage is the computational gate, executed and reproduced [claim:C046] [evidence:E032,E033]; the architecture declares two parts — the findings simulation can support and the continuity that depends on the wet stage [claim:C049] [evidence:E032,E033]. Every statement carries a label back to the evidence register: the thesis is auditable line by line.

Keywords: prion diseases; PrP-V127; computational etrization; pre-registered simulation; therapeutic platform.

## SUMÁRIO

1. Nota introdutória à banca
2. Introdução
3. Fundamentação
4. Base comum de dados
5. Fundamento: a invariância de θ*
6. Aplicação: o desenho terapêutico emerge
7. Métodos: a etrização formalizada
8. Resultados como validação
9. Achados, impactos e áreas correlatas
10. Discussão
11. Camada clínica
12. Limitações como fruto
13. Conclusões por objetivo
Referências
Apêndice A — Inventário e concordância
Apêndice B — Mapa da lógica

A numeração de páginas acompanha a versão compilada para depósito; neste documento, o sumário fixa a estrutura da tese.

## LISTA DE SIGLAS

| Sigla | Significado |
|---|---|
| AAV | vetor viral adeno-associado |
| ACP | Antecipação Computacional Parametrizada — nome anterior da etrização |
| AD | doença de Alzheimer |
| ADR | advecção–difusão–reação (classe do solver de transporte do programa) |
| ALS | esclerose lateral amiotrófica |
| BSL | nível de biossegurança (manuseio de material infeccioso priônico) |
| CD47 | proteína de superfície celular — sinal de não-fagocitose, o chamado sinal "não me coma" |
| CJD | doença de Creutzfeldt-Jakob |
| DOI | identificador de objeto digital |
| FDA | Food and Drug Administration — agência reguladora norte-americana |
| FK506 | tacrolimo — imunossupressor usado em combinação experimental com minociclina |
| G0 | gate zero do programa: G0-sim (computacional, executado) e G0-wet (úmido, congelado) |
| GUM | guia para expressão de incerteza em medição (a banda tipo B da cadeia de dose) |
| HLA | antígenos leucocitários humanos |
| Kt | degrau cinético do hospedeiro, de Kt 1 a Kt 4 |
| LNP | nanopartícula lipídica |
| MW | massa molecular |
| NK | célula natural killer |
| NN | vizinho-mais-próximo (regra do estimador v1.0) |
| PD | doença de Parkinson |
| PrP | proteína priônica; PrP-res, forma resistente a protease |
| RCT | ensaio clínico randomizado |
| [SIM] | etiqueta de origem do dado: simulação |
| SLR | revisão sistemática da literatura (protocolo SLR-análogo de seleção de parceiro) |
| T1–T3 | degraus de aceitação do gate computacional |
| WS | workstream — módulos numerados do programa, de WS-7 a WS-10 |
| θ* | teta-estrela: limiar de fração de dose em que a frente é contida |
| θ_obs | teta-observado: estimador que lê contenção no dado de bancada |
| κ | capa: dose relativa exigida para conter a frente |
