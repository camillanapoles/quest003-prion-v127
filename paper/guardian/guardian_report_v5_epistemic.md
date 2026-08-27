# RELATÓRIO EPISTÊMICO DO GUARDIÃO — v5
## Interrogação hostil de contexto, ideias, metodologia, evidência e lógica

**Papel:** revisor A1 crítico e recursivo. Cada achado responde: **o quê** está frágil, **por quê** importa, **o que falta** de informação, e **qual procedimento inserir**.
**Regra de ouro:** nenhuma frase abaixo é retórica — cada uma aponta para um artefato ou seção específica do repositório.
**Baseline determinístico:** R3 executado → 2 BLOCKED (θ-ops, plano estatístico ausente do manuscrito) + 8 AMEND. Este relatório cobre a camada semântica que padrões não alcançam.

---

## VEREDITO GERAL

O programa é **metodologicamente distinto e honesto** — mas um revisor A1 o derruba hoje em **três pontos de ruptura** (E-01, E-02, E-03): a predição travada não tem estimador operacional; as entradas do prior bayesiano não estão amarradas a evidência verificada; e o argumento regulatório comete (e não declara) um salto lógico. Todos os três são corrigíveis por **inserção de procedimento**, sem novos experimentos.

---

## A. CONTEXTO E ENQUADRAMENTO

### E-01 · A predição travada é tecnicamente infalsificável como escrita — BLOCKED
- **O quê:** "se θ medido em organoides < 0.33, contenção sucede" está travada no release v1.0 — mas θ é quantidade do MODELO, não observável. Não existe em lugar nenhum (verificado: `grep θ experiments/g0_protocol.md` → zero) o procedimento para estimar θ a partir do readout real (gradiente PrP-res proximal/distal).
- **Por quê importa:** sem estimador, o resultado do G0 não pode confirmar nem refutar a predição — o núcleo falsificável do programa vira retórica. Risco de circularidade: ajustar o modelo aos dados e comparar com o limiar do próprio modelo.
- **Falta:** definição operacional de θ_obs: qual grade de κ é ajustada, por que distância (mínimos quadrados sobre o perfil radial? verossimilhança?), com que normalização do campo c_V127, unidade de análise (órganoide vs poça), estatística do limiar (mediana por braço? bootstrap-CI? margem de equivalência?).
- **INSERIR (procedimento):** nova **§2.7 "Operational definition of θ_obs"** no manuscrito + bloco no `g0_protocol.md` congelado ANTES da execução: "(i) pré-registrar a grade de κ e a função-objetivo do ajuste; (ii) scorer cego para quantificação de PrP-res; (iii) θ_obs por órganoide via ajuste do modelo humanizado ao gradiente radial medido; (iv) comparação ao limiar 0.333 com IC bootstrap 90% e margem de decisão declarada; (v) tudo congelado por commit antes do primeiro órganoide infectado."

### E-02 · O prior bayesiano 0/6 está construído sobre fontes fora do registro de evidências — BLOCKED
- **O quê:** o análogo negativo (6/6 falhas clínicas) que puxa P(slowing) para 5% usa PPS, quinacrina, doxiciclina, flupirtina, PRN100 — **nenhuma dessas fontes está no source_manifest** (verificado: grep → vazio). São "contextual secondary".
- **Por quê importa:** o harness de evidência certifica 45 claims e 33 fontes — mas o INPUT do modelo probabilístico que governa a decisão de gastar US$100–150k não passa pela mesma garantia. Um revisor: "vocês auditaram citações alheias, mas as suas próprias entradas de modelo estão não-auditadas."
- **Falta:** DOI/PMID verificado por fonte das 6 falhas (quinacrina: ensaio randomizado; doxiciclina: ensaio publicado; flupirtina: ensaio alemão; PPS: série compassiva; PRN100: Mead 2022; minociclina-comb: já no registro como E022/E021) + pesos de similaridade das 10 âncoras documentados fora do JSON.
- **INSERIR:** (i) elevar as ~5 fontes das falhas a E034–E038 com abertura e verificação por humano (regra da skill: sem DOI de memória — abrir a fonte); (ii) nota em §2.3 declarando o estado atual e a ação; (iii) publicar a tabela de pesos dos análogos como tabela suplementar (hoje só existe dentro do bayes_success.json).

### E-03 · "Conjunção de precedentes" tem salto lógico não declarado — AMEND
- **O quê:** §4.3 argumenta que cada pilar tem categoria regulatória aprovada. Verdade — mas a CONJUNÇÃO (enxerto secretório expressando variante de proteína priônica em cérebro infectado + redose crônica + endpoint biomarcador em doença 100% fatal) nunca foi aprovada como conjunto. Precedente por pilar ≠ precedente para a conjunção.
- **Por quê importa:** é o primeiro questionamento de um revisor regulatório; não declará-lo parece seleção de argumento.
- **INSERIR:** frase em §4.3: "a conjunção em si é o risco regulatório novo; cada precedente degrada uma incerteza, nenhuma elimina a necessidade de diálogo pré-IND" + mapear qual pilar tem o precedente mais frágil (enxerto secretório anti-prion — o grafo de Parkinson 2026 é de progenitores dopaminérgicos, não de biofábrica secretora).

### E-04 · Onde está a frente? O cálculo do anel pressupõe localização que não existe — AMEND
- **O quê:** Regra 1 (anel 8–12 mm) assume que se sabe ONDE posicionar. sCJD é multifocal no diagnóstico; RT-QuIC diagnostica, não localiza; não existe traçador de PET validado para PrP-res. O G0 (organoide) não sofre disso — a tradução clínica sofre.
- **Falta:** procedimento de definição de alvo in vivo (imuno-PET anti-PrP em desenvolvimento? MRI-DTI da rota? biópsia? mapeamento por propagação esperada do subtipo?).
- **INSERIR:** limitação explícita (§5) + procedimento G1: "definição de alvo por imagem como gate pré-clínico adicional antes de qualquer protocolo humano; para portadores genéticos pré-sintomáticos (população primária), o problema se reduz a anatomia estereotípica da conversão — declarar esse relaxamento e sua base".

### E-05 · Por que θ* muda com a humanização? (asserção sem derivação) — AMEND
- **O quê:** §3.4 afirma que o limiar humanizado (0.333) é "mais favorável" que o murino (0.20–0.33). Um modelador pergunta: se θ é adimensional e a humanização é REESCALA GLOBAL DO TEMPO, por que θ* muda? (Resposta provável: a janela de replicação por unidade de difusão muda — mas isso não está escrito.)
- **INSERIR:** uma frase de derivação em §3.4 explicando o mecanismo da mudança (ou, se for artefato da re-escala, declarar como tal) — antes que o revisor descubra por você.

## B. IDEIAS (tese central)

### E-06 · O agente não transfere para AD/PD — só o cálculo — AMEND
- **O quê:** §4.2 diz que o cálculo é "protein-agnostic" — correto para o CÁLCULO, mas a VANTAGEM do programa é o V127: uma variante protetora SELECIONADA PELA EVOLUÇÃO. Para Aβ/α-sinucleína não existe equivalente natural.
- **INSERIR:** parágrafo honesto em §4.2: o que faria o papel do agente (anticorpo intracelular? variante travada por dissulfeto? degradação direcionada?) e por que isso é uma incerteza ADICIONAL não apenas de engenharia, mas de existência de solução.

### E-07 · Expoente do freeS: a forma funcional não foi testada contra alternativa — AMEND
- **O quê:** freeS=(1+κc)² assume dois eventos independentes. Se a unidade inibitória real é o heterodímero V127-WT (um evento), a forma seria (1+κc) — e θ* mudaria. Sensibilidade ao expoente nunca foi varrida.
- **INSERIR:** sweep {1, 2} × κ-grid no ws_9 (execução barata, ~1 run de 17 min no Colab) + tabela em §3.4; se θ* for robusto ao expoente, a alegação ganha; se não, a limitação sobe de prioridade.

### E-08 · Redose LNP sem discussão de imunogenicidade repetida — AMEND
- **O quê:** Regra 3 (≤7 d) é farmacocinética pura. Redose intratecal repetida de LNP tem barreira translacional conhecida (anti-PEG, ativação de complemento, clearance acelerado — caracterizado em via sistêmica, não intratecal).
- **INSERIR:** estender a limitação 10: "imunogenicidade da redose não caracterizada inclusive na via intratecal; G0-A7 deve incluir leitura de marcadores inflamatórios locais (IL-6, complemento) como endpoint secundário de segurança."

## C. METODOLOGIA

### E-09 · Plano estatístico do G0 existe no protocolo, não no manuscrito; blinding/randomização não existem em nenhum — BLOCKED (meta do R3-SAP)
- **O quê:** `g0_protocol.md` linha 70: "t/Welch por braço vs A2, α=0.05, Holm (5 comparações), n=8 detecta Δ≥50% com poder ~80% a CV~30%, escalar para n=12" — bom, mas (i) não subiu ao manuscrito; (ii) cegamento do avaliador de WB/IHC e randomização de organoides por lote não estão escritos em lugar algum.
- **INSERIR:** §2.5 ganha o plano estatístico completo + frase: "scorer blinding e randomização por lote são requisitos a congelar no checklist de execução antes do primeiro experimento (registro de lacunas transparente)". Um manuscrito que declara a lacuna antes do revisor achá-la ganha credibilidade; esconder, perde.

### E-10 · Auditoria não é reproduzível como descrita — AMEND
- **O quê:** "≈90 buscas" — as queries não estão arquivadas (verificado: literature/ tem só evidence_table e refs_audit). Para um paper cuja contribuição inclui "registro de citações corrigido", a própria auditoria deve ser reproduzível.
- **INSERIR:** (i) nota honesta em §2.1: buscas executadas por agente em sessões; queries e datas reconstituíveis do log de sessões, consolidação em `literature/search_log.md` como ação pendente; (ii) criar o search_log.md consolidando o que consta das evidence tables (queries por bloco A–I).

### E-11 · WS-7 verificado mas não VALIDADO contra dados de distribuição publicados — AMEND
- **O quê:** self-tests (conservação, Thiele) são VERIFICAÇÃO numérica, não VALIDAÇÃO contra experimento. Existe literatura de distribuição intratecal/parenquimal de macromoléculas (anticorpos, albumina) com perfis mensurados.
- **INSERIR:** validação de história de caso: reproduzir com o solver um perfil publicado de distribuição (fonte a verificar e elevar ao registry) e reportar erro — ou declarar como trabalho futuro no §2.2 com justificativa do porquê a verificação basta para REGRAS RELATIVAS (espaçamento escala com ℓ; regras são razões, não concentrações absolutas).

### E-12 · Pesos bayesianos: quem pontuou? — AMEND
- **O quê:** análogos pontuados por julgamento estruturado — de um avaliador único (monorater). sensitivity_sweep cobre cenários, não a matriz de pesos.
- **INSERIR:** §2.3: "pesos atribuídos por avaliador único (limitação 7); análise de sensibilidade ao vetor de pesos (reponderação ±50% por eixo) commitada como pendência" + executar no ws_8 (barato, local).

### E-13 · C₅₀ sweep prometido ("flagged") mas nunca reportado — AMEND
- **O quê:** limitação 3 diz "sensitivity flagged" — flag existe, sweep não. Igual ao E-07: mesma execução resolve.
- **INSERIR:** sweep C₅₀ ∈ {20, 50, 100, 200} sobre θ* no mesmo run do Colab que resolver E-07.

### E-14 · Subtipo da predição travada não especificado — AMEND
- **O quê:** a predição θ<0.33 não diz qual subtipo semeia o G0 (MV1? MV2? MM1 — sem âncoras?). θ* pode ser subtipo-dependente (a própria §3.4 mostra margens diferentes por subtipo).
- **INSERIR:** em §2.5/§3.4: "predição travada refere-se a challenged MV2-like (subtipo com âncoras completas); generalização a MM1 é claim futuro condicionado a âncoras."

## D. EVIDÊNCIA

### E-15 · As duas âncoras centrais são preprints não revisados — AMEND
- **O quê:** E003 (Gatdula) e E004 (Zerbes) carregam o elo anchorless-trans — a peça sem a qual o programa não existe. Ambos são preprints de 2026. (E003 tem PMID — é depositado, não revisado.)
- **INSERIR:** limitação nova em §5: "a camada anchorless-trans descansa em duas fontes não revisadas por pares; monitorar versões revisadas e re-verificar claims afetados quando publicarem" — transforma vulnerabilidade em disciplina.

### E-16 · E029 (Lund 2026) tem a proveniência mais fraca do registry — AMEND
- **O quê:** url newscientist → locator clinicaltrials.gov (genérico). Citaçãode imprensa para claim de precedente regulatório é o elo mais fraco das 33 fontes.
- **INSERIR:** substituir por registro NCT direto (a abrir e verificar — sem número de memória) ou rebaixar o claim a "reportado".

### E-17 · Single-source em claims pivotais — AMEND
- **O quê:** seleção do kuru (só Mead 2009); âncoras de organoide (só Groveman 2019). A bateria R1 já pergunta; o texto não responde por que corroboração independente não existe/é esperada.
- **INSERIR:** uma linha por claim pivotal em §3.1: status de corroboração ("nenhuma replicação independente conhecida até [data da auditoria]") — honestidade que blinda.

## E. LÓGICA (validação das cadeias inferenciais)

### E-18 · Auditório do claim emergente: consistência ainda pesa como resultado — NOTE
- **O quê:** o abstract lista MV2>MV1 como Resultado — tecnicamente é resultado do CHECK DE FIDELIDADE do port, não do sistema biológico. A declaração do confound está feita; falta alinhar o peso retórico (resultado-de-método, não resultado-de-biologia).
- **INSERIR:** meia frase no abstract: "emergent qualitative consistency, seed-mass confound declared" — JÁ está lá ✓ (verificado). Mover para NOTE resolvido; manter vigilância para não regredir.

### E-19 · "Custos e prazos" (US$100–150k / 10 meses) sem decomposição — NOTE
- **O quê:** número usado em §4.1 como argumento de eficiência; nenhuma tabela de decomposição existe no repo.
- **INSERIR:** mini-tabela suplementar (organoides × braços × preço-unitário + overhead) ou remover o número (menos é mais seguro).

### E-20 · A tese precisa de um critério de MORTE programática — NOTE
- **O quê:** kill-switches existem por braço (pivot A6≈A5, etc.) mas não há critério que mate o PROGRAMA (não o ramo). Ex.: "se A6 não mostrar gradiente de contenção em nenhuma dose testada E θ_obs>0.33 em todos os braços, o programa encerra e o negative-result é publicado."
- **Por quê importa:** sem isso, o programa é infalsificável no nível de portfólio — a mesma crítica que E-01 faz à predição, agora no nível do programa. Publicar o critério de morte é a demonstração máxima de boa-fé científica e protege contra escalation-of-commitment.
- **INSERIR:** parágrafo em §2.5: "program-level kill criterion" com condições explícitas e compromisso de publicação do resultado negativo.

---

## MATRIZ DE AÇÃO (o que entra no manuscrito AGORA vs. o que vira execução)

| Achado | Ação imediata (texto) | Ação de execução (repo/execução) | Dono/prazo |
|---|---|---|---|
| E-01 θ-ops | §2.7 nova | congelar bloco no g0_protocol.md | texto: hoje; freeze: antes do G0 |
| E-02 falhas-fora-do-registry | nota §2.3 | elevar E034–E038 c/ abertura de fonte | agente, próxima sessão |
| E-03 conjunção | frase §4.3 | — | hoje |
| E-04 localização | limitação §5 | procedimento G1 | hoje / G1 |
| E-05 derivação θ* | frase §3.4 | — | hoje |
| E-06 agente-AD/PD | parágrafo §4.2 | — | hoje |
| E-07 expoente | nota §3.4 | sweep no Colab | nota: hoje; sweep: próximo run |
| E-08 redose-immun | estender limitação 10 | marcadores no A7 | hoje / G0 |
| E-09 SAP+blinding | §2.5 completo | checklist de execução | hoje / freeze antes G0 |
| E-10 search-log | nota §2.1 | consolidar search_log.md | hoje / próxima sessão |
| E-11 validação WS-7 | nota §2.2 | caso publicado | nota hoje; validação futura |
| E-12 pesos monorater | nota §2.3 | reponderação | hoje / barato-local |
| E-13 C₅₀ | nota limitação 3 | sweep junto c/ E-07 | hoje / próximo run |
| E-14 subtipo | frase §2.5 | — | hoje |
| E-15 preprints | limitação nova | monitorar v2 | hoje |
| E-16 E029 | nota registry | abrir NCT | próxima sessão |
| E-17 single-source | linhas §3.1 | — | hoje |
| E-19 custos | tabela supl. ou remover | — | hoje |
| E-20 kill programático | parágrafo §2.5 | — | hoje |

**Conclusão do Guardião:** com E-01/E-02/E-09 inseridos (texto + freeze de protocolo) e a matriz acima executada, o manuscrito resiste à revisão hostil no nível metodológico. O que NENHUM texto resolve: só o G0 resolve a incerteza científica — e o manuscrito deve continuar dizendo exatamente isso.
