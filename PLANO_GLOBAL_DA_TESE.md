# PLANO GLOBAL DA TESE — planejamento metodológico antecipado

> Single-source: `thesis_engine/plano_data.py` → SQL (`planchapter`) → este MD + gate `check_plano`.
> Fundamentos: blueprints B0–B9 · rationale R0–R9 · style_profile · canon (grafo 3-trees) · roadmap.

## 1 · Ordem lógica (o que antecede o quê — e por quê)

1. **c01 · nomear+diferenciar** — sem nome aceito, nada é discutível — a 'chave-antes-da-porta'
1. **c02 · contrato formal** — define O QUE se promete (questões/objetivos/hipóteses/M1–M5) antes de qualquer evidência
1. **c03 · plausibilidade** — por que acreditar que é possível (literatura) — antes de gastar simulação
1. **c04 · a ponte** — mesmos dados sob fundamento e aplicação + validação M3→M2 + cronologia honesta (anti-hindsight EXIBIDO como força)
1. **c05 · o alicerce** — invariância θ* multi-espécie: SEM ela, a aplicação não emerge — precede e legitima c06
1. **c06 · o produto** — o desenho terapêutico EMERGE (transporte→limiar→dose banda GUM→G0-wet→custo)
1. **c07 · auditabilidade** — método formalizado P0–P6: examinador audita 'trocando só termos' (H1)
1. **c08 · validação** — cada resultado valida UMA promessa (regra V4) — nada órfão
1. **c09 · novidade** — o que é novo (cura+restauração), replicável AD/PD, próximas abordagens declaradas
1. **c10 · significado** — o que os resultados significam E o que não significam
1. **c11 · tradução clínica** — acessibilidade médica: leitura-10min, o incomum explicado a médicos
1. **c12 · limites-como-fruto** — cada limitação com o gate que a fecha (JHU-iii)
1. **c13 · fechamento** — veredito por objetivo OE1–OE4

## 2 · Ranking de valor (o mais valioso primeiro)

1. **θ*=0,333 invariante multi-espécie (c05)** — alicerce: tudo deriva dela; cenário B 0,333–0,400 ×4 espécies
2. **A primeira dose calculada — banda GUM A6 (c06)** — produto nunca feito; 'a largura ≈53× É o achado' — honestidade quantificada
3. **O método etrização (c01/c07)** — nomeável, auditável, transferível para AD/PD — contribuição metodológica perene
4. **Cura+restauração (achado único, c09)** — conteção E reversão de dano: além de qualquer terapia priônica existente
5. **Infraestrutura M1–M5 (c08)** — θ_obs/freeze/re-param/seleção-parceiro/continuidade — replicabilidade institucional

## 3 · O que garante o quê

| Mecanismo | Garante | Implica |
|---|---|---|
| Cronologia honesta (predições v1.0 travadas ANTES da Parte 3) | garante anti-hindsight | → valida M3→M2 como emergência lógica, não ajuste ad hoc |
| Cadeia sha256 (claims norm→hash; JSONs idênticos Colab≡repo) | garante integridade dos números | → gate F1/F3 do engine a espelham |
| Tiers [SIM]/[ORGANOID] em toda saída de dose | garante honestidade epistêmica (não-promessa) | → gate G3 |
| Base comum (mesmos dados M2=M3) | garante que o desenho EMERGE do fundamento | → tabela §4.3 |
| G0-wet especificado c/ kill-switch + SAP cego | garante falsificabilidade programática | → negative-result é resultado válido |
| Concordância claims↔referências 58/58 | garante rastreabilidade total | → régua: claim sem referência é inaceitável |

## 4 · O incomum — mesmo para médicos (traduzir no Cap.11)

- Dominante-negativo por COMPETIÇÃO, sem silenciar o alelo nativo (vs terapias de silenciamento — o nativo segue funcionando)
- Dose como BANDA com incerteza GUM propagada, não número único — 'a largura da banda é o achado até G0-A6'
- Prognóstico calculado ANTES da medição: decidir o que medir/onde/em que dose antes de gastar wet-lab (etrização)
- Horizonte de observação como parte da dose (dependência de horizonte: o número só compara sob horizonte declarado)
- Titulação por cinética do paciente (Kt em classes 1–4): dose personalizada por subtipo — não há 'a dose', há a escada

## 5 · Definido previamente (invariantes de escrita)

- nomenclatura θ* (limiar travado) vs θ (funcional) · κ adimensional · Kt em classes 1–4 (nunca contínuo)
- tiers [SIM]/[SIM]-planejamento/[ORGANOID] + tríade não-promessa (título de figura + tabela + claim)
- decimais: vírgula PT-BR no corpo; ponto só nas claims EN canônicas (norm→sha256)
- cronologia: predições v1.0 de 26/08 NUNCA retreinadas; Parte 3 declarada como força
- voz: agente é 'o programa/a tese/o desenho'; a autora aparece como validadora expressa

## 6 · Plano por capítulo (objetivo · fontes · tópicos · elementos · simplificação)

### c00 — contrato de leitura

**Objetivo da seção:** Declarar título-promessa e dar os instrumentos de navegação (resumo, sumário, siglas).

**Onde está a informação (e como aplicar):**
- [doc] style_profile.md · paper_spine_config.md

**Tópicos/subtópicos:** RESUMO/ABSTRACT (contribuição em 1 parágrafo) · SUMÁRIO · LISTA DE SIGLAS

**Elementos:** siglas upfront

**O que é complicado:** densidade terminológica (θ*, κ, Kt, G0, tiers)

**Como simplificar visualmente:** LISTA DE SIGLAS antes do Cap.1 + âncoras verbais ('1/3 sobrevive')

### c01 — nomear+diferenciar (M1)

**Objetivo da seção:** Responder 'por que etrização, e o que a diferencia' ANTES de qualquer conteúdo técnico.

**Onde está a informação (e como aplicar):**
- [doc] ERITRIZACAO.md (câmara de fundamentação)
- [claim] C054 (definição operacional)
- [grafo] comunidade 'Etrização Framework (Philosophy)'

**Tópicos/subtópicos:** 3 camadas semânticas do radical · definição operacional C054 · vs in-silico trials (simulam o ENSAIO; etrização simula a CONTINUAÇÃO) · vs revisão sistemática/meta-análise (resumem; etrização DERIVA)

**Elementos:** tabela 3-colunas de contraste

**O que é complicado:** abstração filosófica de um nome novo

**Como simplificar visualmente:** analogia do átomo (palavra que fundou 2.400 anos de pesquisa antes da prova) + tabela de contraste

### c02 — contrato formal

**Objetivo da seção:** Fixar problema→justificativa→questões→objetivos(OE1-4)→hipóteses(H1-3)→componentes M1–M5.

**Onde está a informação (e como aplicar):**
- [doc] m3_to_m2_validation.md §1
- [db] claims seção 2.x

**Tópicos/subtópicos:** 2.1 problema · 2.2 justificativa · 2.3 questões · 2.4 objetivos+OE · 2.5 hipóteses · 2.6 estrutura · 2.7 tabela M1–M5 validada pela autora

**Elementos:** tabela-mãe M1–M5 (validada)

**O que é complicado:** cruzamento OE×H×M1–M5

**Como simplificar visualmente:** uma única tabela-mãe; cada OE liga a 1 hipótese e a componentes nomeados

### c03 — plausibilidade

**Objetivo da seção:** Mostrar que o gargalo priônico é real e que a família antecipatória tem berth (posição H3).

**Onde está a informação (e como aplicar):**
- [doc] literature/evidence_table.md E001–E029
- [grafo] comunidades 'Prion Literature Evidence Table' · 'Neuro-Disease Precedents'
- [figura] Fig.1 mapa científico

**Tópicos/subtópicos:** 3.1 gargalo terapêutico · 3.2 família dos métodos antecipatórios/in-silico · 3.3 posicionamento da etrização (H3) · 3.4 fundamento epistemológico · 3.5 síntese

**Elementos:** Fig.1 — mapa científico em camadas

**O que é complicado:** 28 fontes heterogêneas (genética→estrutural→organoides→regulatório)

**Como simplificar visualmente:** mapa em camadas (Fig.1): cada achado vira um pino no mapa, não uma seção

### c04 — a ponte M3↔M2

**Objetivo da seção:** Provar que fundamento e aplicação assentam nos MESMOS dados; exibir validação e cronologia honesta.

**Onde está a informação (e como aplicar):**
- [doc] m3_to_m2_validation.md §§1-2
- [json] p023 sequences · E007/E009/E032
- [db] check_sec43 (12 âncoras)

**Tópicos/subtópicos:** 4.1 a mesma base sob os dois módulos · 4.2 cronologia honesta (o hostil perguntaria — respondemos antes) · 4.3 tabela de validação (TODOS os números dos JSONs)

**Elementos:** tabela §4.3 com vereditos ✅

**O que é complicado:** números espalhados por N JSONs

**Como simplificar visualmente:** uma tabela única veredito-por-linha; o engine (gate §4.3) garante que nenhum número é digitado

### c05 — o alicerce (M3)

**Objetivo da seção:** Estabelecer a invariância de θ* multi-espécie, a regra de titulação e a dependência de horizonte.

**Onde está a informação (e como aplicar):**
- [json] p024_{mouse,hamster,human,vole}.json
- [claim] C055–C057 · N055–N059
- [canon] F-44 · H-P3 · THETA_STAR_EXPLAINED (grafo Guardian Integrity)
- [figura] Fig.4

**Tópicos/subtópicos:** 5.1 sweep→parametrização por espécie · 5.2 Cenário B [SIM] · 5.3 regra de titulação emergente (Kt 1→1,5·2→2·3→3·4→8) · 5.4 dependência de horizonte (a única assimetria real; hamster refutado honestamente)

**Elementos:** Fig.4 θ* por espécie · tabela bandas A–D

**O que é complicado:** 4 espécies × bandas-Kt × horizonte simultâneos

**Como simplificar visualmente:** Fig.4 escada por espécie com banda sombreada + âncora verbal única ('1/3 sobrevive no pior dia')

### c06 — o produto (M2)

**Objetivo da seção:** Derivar o desenho terapêutico: transporte→limiar travado→primeira dose em banda GUM→G0-wet→custo.

**Onde está a informação (e como aplicar):**
- [json] m31_u1u2.json (u1_kreq·chain·u2_mw 22,83 kDa) · ws_7_results.json
- [claim] C033/C038/C040/C051 · C058–C060 · E057/E058 · N060–N065
- [figura] Fig.5 escada de dose

**Tópicos/subtópicos:** 6.1 três regras de transporte falseáveis · 6.2 limiar travado e dose legitimada pela banda · 6.3 a PRIMEIRA dose calculada (cadeia κ→µM→µg/depósito GUM) [SIM]-planejamento · 6.4 G0-wet especificado (8 braços, SAP Welch/Holm cego, kill-switch) · 6.5 custo-cotação S1

**Elementos:** tabela escada Kt×κ (≤5 col) · Fig.5 com pior-caso hachurado · tabela S1 custo

**O que é complicado:** cadeia dimensional κ_req→µM→µg com incerteza Tipo-B por el

**Como simplificar visualmente:** Fig.5 escada-de-dose (bandas explícitas, hatch no pior-caso) + mantra: 'a largura ≈53× É o achado até G0-A6'

### c07 — auditabilidade (B5)

**Objetivo da seção:** Formalizar a etrização P0–P6 com garantias por passo e Base de Validade de linhagem completa.

**Onde está a informação (e como aplicar):**
- [doc] guardian decálogo · AST 9/9 · C046/C052–C054
- [grafo] comunidades 'guardian.py Rounds Engine' · 'ast_check.py Validation Suite'

**Tópicos/subtópicos:** 7.0 pipeline P0–P6 (diagrama) · 7.1 o método nomeado · 7.2 formulação matemática COM proveniência · 7.3 Base de Validade (mandatória) · 7.4 a tese em forma experimental (mapeamento análogo)

**Elementos:** diagrama pipeline §7.0 · equações cada uma com citação de origem

**O que é complicado:** formalismo matemático denso

**Como simplificar visualmente:** opener 'rastreio farmacocinético' + diagrama do pipeline + equação-com-proveniência (nunca equação nua)

### c08 — resultados-como-validação (V4)

**Objetivo da seção:** Cada resultado valida UMA promessa; apresentar M1–M5 como resultados (não como planos).

**Onde está a informação (e como aplicar):**
- [doc] results_validation.md
- [json] part2_theta_obs_*.json · E032/E033

**Tópicos/subtópicos:** 8.1 resultados da simulação JÁ realizada · 8.2 M1 θ_obs · 8.3 M2 freeze · 8.4 M3 loop anti-hindsight · 8.5 M4 seleção de parceiro (SLR-análogo) · 8.6 M5 continuidade

**Elementos:** tabela promessa↔resultado↔registro

**O que é complicado:** mapeamento 1:1 promessa-resultado

**Como simplificar visualmente:** tabela de mapeamento explícita — nenhuma subseção métrica órfã (gate V4)

### c09 — novidade explícita

**Objetivo da seção:** Nomear o achado único (cura+restauração), a replicabilidade (AD/PD) e as próximas abordagens.

**Onde está a informação (e como aplicar):**
- [doc] 5.1-bis/5.2-bis · F-44
- [grafo] comunidade 'Population Impact & Trials'

**Tópicos/subtópicos:** 9.1 achados e impactos · 5.1-bis cura+restauração · 9.2 áreas correlatas · 5.2-bis replicabilidade AD/PD · 9.3 próximas abordagens (declaração mandatória)

**Elementos:** —

**O que é complicado:** escopo além de priões pode soar promessa

**Como simplificar visualmente:** declaração mandatória de próximas abordagens + tiers em tudo

### c10 — significado com limites

**Objetivo da seção:** Dizer o que os resultados significam E o que não significam.

**Onde está a informação (e como aplicar):**
- [doc] hostile_review_v4 · guardian reports E-01..23

**Tópicos/subtópicos:** 10.1 promessas e limites da Parte 2 · 10.2 significa/não-significa

**Elementos:** estrutura binária significa|não-significa

**O que é complicado:** tom entre promessa e não-promessa

**Como simplificar visualmente:** estrutura binária explícita em duas colunas

### c11 — tradução clínica (B7)

**Objetivo da seção:** Acessibilidade médica total: leitura-10min, linguagem clínica, acompanhamento previsto.

**Onde está a informação (e como aplicar):**
- [doc] AVALIACAO_ALFA convergências · E019 LNP · E039 turnover · E034–38 ensaios

**Tópicos/subtópicos:** NOTA DE LEITURA (5 perguntas + caixa de aviso) · resumo-1página rota-10min · openers 'Em linguagem clínica:' · acompanhamento previsto [SIM] (desenho, NÃO conduta)

**Elementos:** caixa de aviso · tabela acompanhamento [SIM] · Fig.4 no leito clínico

**O que é complicado:** farmacocinética/toxicologia para não-especialista

**Como simplificar visualmente:** openers analógicos ('rastreio farmacocinético') + 5 perguntas de leitura + rota de 10 minutos

### c12 — limitações-como-fruto (JHU-iii)

**Objetivo da seção:** Cada limitação nomeada COM o gate/ensaio que a fecha — limite como agenda.

**Onde está a informação (e como aplicar):**
- [doc] guardian findings E-01..23 · C043
- [grafo] 'Negatives & Appendix Anchors'

**Tópicos/subtópicos:** classes: transferência/horizonte/preprints-monitorados/localização/imunogenicidade · cada limite → o que fecha

**Elementos:** tabela limite↔fecho

**O que é complicado:** 15+ limitações

**Como simplificar visualmente:** agrupar por classe + coluna única 'o que fecha isto'

### c13 — fechamento por objetivo

**Objetivo da seção:** Veredito por OE1–OE4, cada um ancorado nas claims correspondentes.

**Onde está a informação (e como aplicar):**
- [db] claims por OE · tabela §2.7

**Tópicos/subtópicos:** OE1 nomear/formalizar · OE2 Base de Validade · OE3 resultados-como-achados · OE4 continuidade documentada

**Elementos:** um parágrafo-veredito por OE

**O que é complicado:** —

**Como simplificar visualmente:** estrutura fixa por OE: prometido→entregue→onde

### c14 — rastreabilidade ABNT

**Objetivo da seção:** 58 fontes do registro em ABNT, citadas 58/58.

**Onde está a informação (e como aplicar):**
- [db] source_manifest.json (E001–E058)

**Tópicos/subtópicos:** 58 referências · fontes complementares (verificação pendente — snippet)

**Elementos:** gerada do registro (engine)

**O que é complicado:** duplicação/ordem ABNT

**Como simplificar visualmente:** geração determinística do registro; zero digitação

### c15 — inventário verificável

**Objetivo da seção:** Todo artefato da Parte 2 listado em disco + concordância claims↔referências completa.

**Onde está a informação (e como aplicar):**
- [doc] artifact_check.md · claim_register.md

**Tópicos/subtópicos:** inventário A · concordância claims→referências (régua da autora)

**Elementos:** tabela concordância 60 claims × fontes

**O que é complicado:** 60×N cruzamento

**Como simplificar visualmente:** tabela gerada do grafo (engine) — o gate G7 a valida

### c16 — mapa da lógica

**Objetivo da seção:** De onde veio cada informação e como se conecta; decisões, rejeições, glossário, objeções.

**Onde está a informação (e como aplicar):**
- [grafo] todo o grafo dos 3 trees
- [doc] guardian decisions/rejeições

**Tópicos/subtópicos:** B.1 fluxo informação literatura→conclusão · B.2 decisões-chave (por quê) · B.3 rejeições documentadas (o que NÃO funcionou) · B.4 glossário contextual · B.5 prejulgando objeções da banca

**Elementos:** fluxograma B.1 · tabela de rejeições B.3

**O que é complicado:** proveniência total é o maior grafo

**Como simplificar visualmente:** um mapa único: cada afirmação da tese rastreável a arquivo/claim/JSON (o engine já faz isto — expor como figura)
