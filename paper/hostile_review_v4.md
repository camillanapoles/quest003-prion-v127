# Revisão Hostil do Manuscrito v4.0 (peer-review simulado, Reviewer 2)
**Método:** skill peer-review 2.1 — claim–evidence check, methods/stats/reproducibility/citation critique. Manuscrito próprio e público (sem confidencialidade). Tom: o revisor mais duro que podemos encontrar.

---

## Major Concerns (M1-M8)

**M1 — Falta o elo κ→concentração em qualquer direção.** O manuscrito varre κ adimensional mas nunca declara a escala molar correspondente (nM? µg/mL?) nem a capacidade secretora por depósito (mol/dia). O revisor exige: ou uma subseção com estimativa de ordem de grandeza (células × taxa de secreção × D_eff → concentração em r=1mm), ou admissão explícita de que θ* é ancorado apenas relativamente. **Ação:** adicionar estimativa de ordem de grandeza + mover M1 já listado como limitação 1 para discussão ativa com número.

**M2 — T1/T2 são critérios fracos disfarçados de fortes.** T1 (total>1.5× semente) passa até com crescimento artefactual de deposição sem espalhamento espacial; T2 (R<90%) com κ=32 quase zera o sistema (freeS~1/1000) — "contém" é trivial nesse regime. O regime informativo é κ∈[2,8] e os guard-rails deveriam ser: gradiente radial monotônico de carga E frente <50% baseline em κ≤8. **Ação:** re-rotular T1/T2 como triagem mínima e adicionar critério informativo T3 (frente <50% em κ≤8 = sucesso mecanístico) — já satisfeito pelos dados apresentados.

**M3 — "Validação emergente" MV1/MV2 é qualitativa e n=1 por subtipo.** Reproduzir ORDEM (n=2 condições) é frágil como validação; e a diferença de amplitude 126× só entrou como condição inicial de semente, não como parâmetro cinético — a hierarquia poderia ser consequência trivial de massa inicial. **Ação:** (i) admitir que a diferença é de semente (e que Groveman sugere diferenças de taxa também); (ii) teste de controle: MV1 com semente igual à MV2 (mesma massa, cinética distinta) — se ainda contém antes, a alegação fortalece; adicionar como experimento futuro ou run rápido. (iii) suavizar claim de "validação" para "consistência qualitativa emergente".

**M4 — O modelo v4 usa Params.csv murinos intocados + relógio humano.** As TAXAS continuam murinas; só o relógio global foi re-escalado. Um revisor de modelagem pega isto imediatamente: as âncoras humanas calibraram 1 grau de liberdade (escala de tempo) de um sistema com ~6 taxas livres. **Ação:** declarar explicitamente na seção de métodos ("humanização = reescala global de tempo; taxas relativas permanecem murinas; fitting completo das taxas é trabalho futuro com séries MV1/MV2 publicadas") + limitação 4 já existe — reforçar com esta frase exata.

**M5 — P(G0 go)=36.6% com validade preditiva 80% parece incompatível.** Se o organoide acerta 80% e o mecanismo tem prior ~50%, P(go) deveria ser ~0.8×0.5+... — o número 36.6% precisa de derivação mostrada ou está mal especificado. **Ação:** mostrar a fórmula/ponderação no suplemento do repo (bayes_success.json gates) ou apresentar como P(go|frame completo) com nota. Transparência: incluir os pesos dos análogos no apêndice.

**M6 — Abstract afirma "42 verified references" mas a lista mostra [1]-[26]+lista "adicionais".** Contagem e numeração precisam fechar exatamente; revisores contam. **Ação:** renumerar todas ou remover a contagem do abstract (manter "42 references verified, full list in repository").

**M7 — Transferibilidade Alzheimer/Parkinson sem nenhuma citação de espalhamento priônico-like.** §4.2 afirma Braak/prion-like sem refs (stopschinski 2017, Jucker/Walker reviews existem e NÃO estão citadas). **Ação:** adicionar 2-3 refs canônicas (Stopschinski & Diamond 2017 Lancet Neurol; Jucker & Walker 2018 Nature; Braak reviews) — são conhecidas e verificáveis.

**M8 — Falta declaração sobre ausência de dados de segurança in vivo do construto V127ΔGPI.** O texto cita Zerbes (AAV roedor) mas não discute imunogenicidade/clearance renal do construto proteico — pergunta padrão de revisor farmacêutico. **Ação:** parágrafo curto em Limitações (imunogenicidade não caracterizada; anchorless PrP tem histórico PK; G0-A6 dá primeiros dados de exposição).

## Minor Concerns (m1-m10)

m1 — θ é usado antes de definido com precisão (definir formalmente na primeira ocorrência: θ ≡ replication-rate/capping-capacity ratio at deposit peak). m2 — unidades de k_eff (s⁻¹) mas tabela do sweep não mostra tempo em dias lado a lado — adicionar coluna. m3 — "56 commits" no abstract muda a cada push; fixar release (v1.0) como âncora. m4 — Figura inexistente: o texto descreve curvas mas o manuscrito não tem UMA figura — revisor exigirá Fig.1 (design do programa), Fig.2 (θ response), Fig.3 (MV1/MV2). m5 — tabela de parâmetros consolidada falta (α, λ, D0, k, Kt..., âncoras) — uma tabela única. m6 — repo URL no rodapé de cada página (footer) para impressão. m7 — palavras "protocolo"/"plataforma" às vezes trocadas — padronizar. m8 — PT/EN divergem em 2-3 frases (check de paridade). m9 — autoridade de CRediT ausente (consórcio sem nomes — comoCit.ar?). m10 — data de " locked predictions" deve citar o commit hash específico, não "repositório".

## Veredicto simulado: MAJOR REVISION
Com M1-M8 endereçados, o manuscrito tem corpo para preprint de credibilidade; sem eles, revisor técnico derruba por elos não declarados.
