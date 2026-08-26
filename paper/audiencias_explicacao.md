# Os Achados da Quest 003 — 4 Audiências
**Para:** explicar a pesquisa da terapia V127 para DCJ a médicos, familiares e instituições
**Núcleo em comum (30 segundos):** Descobrimos por que uma mutação que protegeu canibais da Nova Guiné contra o kuru pode virar terapia contra a Doença de Creutzfeldt-Jakob. Simulamos o mecanismo em computador com dados de órgãos cerebrares humanos infectados: existe um limiar (θ*=0,33) abaixo do qual o escudo proteico contém a doença. Falta testar em mini-cérebros de laboratório (10 meses, ~R$500k) antes de qualquer paciente.

---

## AUDIÊNCIA 1 — Dr. George Trigueiro (tio; médico, PE, interface com gestão em saúde e divulgação)

**Como abrir:** "Tio, o senhor acompanhou a cobertura do caso do Lito (piloto com DCJ, agosto/2026). Trabalhei nisso. Preciso do seu olhar clínico."

**Os achados em linguagem médica:**

A doença: PrP^C (proteína príon celular, GPI-ancorada) converte-se em PrP^Sc que se auto-propaga por templating e fragmentação — cinética de nucleação-polimerização (Masel 1999). Letalidade 100%, sobrevida mediana 6-8 meses na esporádica.

O achado central: o polimorfismo **G127V** no PRNP, surgido na epidemia de kuru e sob seleção positiva (Mead, NEJM 2009), confere **resistência completa quando bialélico** em camundongos humanizados — "tão protetor quanto a deleção do gene" (Asante, Nature 2015) — e atua como **inibidor dominante-negativo dose-dependente**: a variante selvagem na mesma vizinhança tem a conversão bloqueada. Crucial para o senhor como clínico: **heterozigotos permanecem suscetíveis à cepa vCJD** — por isso o desenho terapêutico usa a forma **bialélica/sem âncora GPI (ΔGPI, secretada)**, que em 2026 mostrou atividade dominante-negativa *em trans* in vitro (Gatdula) e +50 dias de sobrevida via AAV em roedor (Zerbes).

O que fizemos de novo (e o senhor pode checar):
1. **Revisão sistemática** com 42 referências verificadas — corrigimos 5 erros que se repetem na literatura de propostas dessa terapia (ex.: NSC não gera micróglia — linhagem saco vitelínico; o nicho subventricular adulto humano é quiescente E replica príon)
2. **Engenharia de transporte** (modelo ADR, meio poroso com parâmetros de cérebro humano): o halo do escudo secretor mede 4-6mm → múltiplos depósitos espaçados 8-12mm cobrem a penumbra
3. **Simulação da dinâmica** (kernel de reação-difusão publicado no iScience 2024, calibrado com os organoides humanos do NIH/Groveman 2019): existe **limiar de contenção θ*=0,33** — abaixo dele a frente priônica morre; a hierarquia de subtipos MV2>MV1 **emergiu do modelo sem ser ajustada** (validação comportamental)
4. **Racionais de segurança**: excluímos citação retratada (minociclina/FK506, Neurotherapeutics 2017→2020), documento que minociclina confunde NfL (nosso endpoint)

Honestidade bayesiana: probabilidade de desaceleração clínica hoje = **5%** se usar a história do campo (6/6 falhas terapêuticas), **30-45%** se os gates confirmarem. Não é promessa de cura — é contenção + resgate de penumbra.

**O que peço ao senhor:** leitura clínica do protocolo G0 (8 braços, GO/NO-GO pré-registrado) com seu olhar de quem entende ensaio clínico e gestão; e sua rede no Nordeste para quando precisarmos de discussão em comitê.

**Bloqueios que ele vai levantar (prever):**
- "Cuidado com prometer cura a família" → concordar de saída: endpoint honesto é desaceleração; documento escrito nesses termos
- "Isso é teoria demais" → mostrar: predições PRÉ-registradas em repositório público antes do experimento; organoides humanos já validados para drogas (PPS, Sci Rep 2021)
- "Quem financia?" → FAPESP regular cobre G0; sem indústria no início (patente aberta, code/science aberto)

---

## AUDIÊNCIA 2 — Neurocirurgião

**Como abrir:** "Preciso do seu ferramental, não da sua fé. A pergunta é se minha dosagem cirúrgica fecha."

O que muda para ele: a cirurgia é **acessória ao mecanismo** — o que se opera é o MEIO DE ENTREGA, e todo o ferramental existe:
- **CED (convecção realçada)** com cânula step-design anti-refluxo (Krauze, J Neurosurg 2005; revisão Elder/Lonser 2025 cobre terapias gênicas E celulares) — delivery já padrão em tumores
- **Trajetória pelo "caminho danificado"**: DTI mapeia trato espongiforme necrosado como corredor de menor dano — parênquima sadio intocado
- **Números que ele valida:** depósitos de 1mm, anel de injeções espaçadas 8-12mm na penumbra, cânula coaxial de uso único (biossegurança príons — arrasto mecânico de PrP^Sc em instrumentais é risco documentado; protocolo WHO 134°C/NaOH)
- Margens calibradas por **RT-QuIC intraoperatório** em biópsias de borda (Green 2018) + IHC rápida ex-temporânea

O detalhe da tese: o implanto (NSC secretora de V127ΔGPI em hidrogel HA 1-2%, Liang 2013 — melhora sobrevida do enxerto; malha ≥5× o raio da proteína para não reter o secretoma) é **biofábrica local**, não reposição celular. Sem promessa de reconexão do parênquima morto — contenção de fronteira + resgate eletrofisiológico de penumbra (Williams 2023).

**Bloqueios que ele vai levantar:**
- "Iatrogenia e litígio" → resposta: população-alvo inicial é PRÉ-sintomática eletiva (E200K), não paciente terminal; cortex decaído já é zona de tolerância; robótica + neuronavegação reduzem risco a padrão de biópsia estereotáxica
- "Instrumental contaminado" → coaxial descartável + destruição por protocolo; e a via mRNA (A7) NEMprecisa de cirurgia — intratecal
- "Quem já fez CED de células?" → o pipeline exists (Lund 2026 transplantou em Parkinson; CED celular em revisão 2025) — nosso G0/G1 precede qualquer craniotomia

---

## AUDIÊNCIA 3 — Familiar portador (E200K/D178N)

**Como abrir:** "Vou te dizer tudo — inclusive o que ainda NÃO sabemos. Você merece os dois lados."

O que dizer:
- Sua família tem uma mutação no gene da proteína príon. Significa risco alto de adoecer — geralmente na meia-idade. Hoje a medicina oferece **acompanhamento, não tratamento**. Isso é a verdade atual e não vamos maquiá-la.
- Cientistas descobriram que **outra** mutação, surgida num povo que sofreu uma epidemia de príons (kuru), **protege quem a carrega** — a evolução fez o teste, em pessoas, por gerações
- Nosso time projetou como usar essa proteção: células do próprio paciente, editadas para produzir a proteína protetora "solta" (que alcança os vizinhos), implantadas num hidrogel protetor por cirurgia guiada, OU uma versão em mRNA (injeção no líquor, sem cirurgia)
- Testamos tudo em computador com dados de mini-cérebros humanos infectados: **existe uma dose em que a proteína protetora segura a doença** — calculamos qual
- **Antes de qualquer pessoa:** mini-cérebros reais (10 meses). Depois camundongos. Só depois, primeira dose em humano — em quem AINDA NÃO tem sintomas (quanto mais cedo, maior o benefício: é onde a janela existe)
- Prazo honesto: 5-8 anos até primeiro paciente; sem garantia — desaceleração da doença é o objetivo, não cura do que já morreu

O que pedimos (e o que NÃO): precisamos de vocês para **mapear quem são as famílias brasileiras** (estudo Smid 2007 mostrou E200K no Brasil; anonimato garantido, LGPD) e talvez, no futuro, doação de amostra para fabricar as células. **Não** vendemos esperança: se um gate falhar, paramos e contamos por quê.

**Bloqueios (prever):**
- Desespero querendo acelerar/burlar gates → argumento: as 6 terapias que "aceleraram" sem gates falharam e queimaram a confiança do campo; a via compassiva errada fecha a porta da certa
- Culpa genética/médica → aconselhamento genético formal (Goldman 2022) é parte do protocolo, não opcional
- "Por que não tentar em meu parente doente AGORA?" → a via mRNA compassiva existe no plano (braço A7 → uso compassivo esporádico), mas só DEPOIS do organoide — fabricação em dias quando pronta

---

## AUDIÊNCIA 4 — Ministério da Saúde / órgãos de pesquisa (Butantan, USP, Einstein) — quem executa no Brasil

**Como abrir:** "Apresento um programa com IP aberto, predições pré-registradas e um único pedido: 10 meses de organoide."

O pitch institucional:
- **O problema nacional:** DCJ tem vigilância compulsória; famílias E200K brasileiras identificadas desde 2007 e **zero** pipeline terapêutico nacional. O caso Lito (2026) expôs o vazio
- **O que já existe pronto** (custo já pago, aberto): revisão 42 refs · solver de transporte · simulação humanizada com predição θ*=0,33 pré-registrada · protocolo G0 8 braços com kill-switches · dossiê ético CEP→CONEP→Anvisa (ATMP, RDC 522/489/555) · whitepaper de posicionamento · preprint
- **O gap:** execução úmida do G0 (BSL-3 + organoides + RT-QuIC, 10 meses, R$300-800k)

**Ranking honesto de onde a realização tem mais chance no Brasil:**

| Instituição | Fit | Por quê | Risco |
|---|---|---|---|
| **1º HUG-CELL/USP + HC-FMUSP (conjunto)** | ★★★★★ | HUG-CELL: iPSC/organoides GMP de referência nacional; HC: grupo de príons (Smid — primeiro relato E200K-BR, RT-QuIC operacional); parceria natural com o modelo Groveman (NIH Rocky Mountain, código aberto) | Burocracia USP lenta; competição interna |
| **2º Instituto Butantan** | ★★★☆ | Cultura de agentes biológicos complexos + capacidade GMP + tradição de missão pública; perfil perfeito para a via **mRNA-LNP** (braço A7 e produção futura) | Sem linha de neurodegeneração/príon ativa — teria que montar; foco em vacinas |
| **3º Albert Einstein (IPq/Unifesp)** | ★★★ | IPq tem história em príons (casos iatrogênicos, vigilância) e o Einstein tem cell-therapy clínica rodando (onco/CTA-I) — bom para G4 fase 1 | Lucratividade conflita com população rara; IP em cenário privado |
| **4º INCT/Instituto D'Or, Brain Institute UFRN** | ★★ | Excelência em neuro, mas sem plataforma prion/organoides BSL-3 | começa do zero |

**Estratégia recomendada:** USP executa G0 (ciência), Butantan puxa a manufatura mRNA (escala), Einstein/HC a fase 1 clínica (leito). O programa foi desenhado em camadas exatamente para dividir assim.

**Bloqueios institucionais (prever):**
- "Raro demais para priorizar" → resposta: raro por subnotificado; protocolo inclui triagem RT-QuIC que barateia vigilância; e a plataforma (célula-fábrica de proteína dominante-negativa) é transferível para Parkinson/Alzheimer priônico-like
- "Sem indústria, não vai a lugar nenhum" → preprint + predições pré-registradas são o ativo que atrai biotech depois do G0; tofersen mostrou que aceleração por biomarcador é a rota para doenças raras
- "Célula genoma-editada no Brasil? Jamais" → o desenho segue RDC 522 (ATMP) e começa autólogo em pré-sintomático — o caso de uso mais controlável possível
- "Por que confiar em vocês?" → tudo auditável: repositório público com hash de commits, refs verificadas, errata de citações alheias documentada

---

### Apêndice — os 4 números para levar no bolso (qualquer audiência)
| Número | Significado | Fonte |
|---|---|---|
| **θ* = 0,33** | abaixo disso, o escudo contém a frente priônica | simulação humanizada (pré-registrada) |
| **4-6 mm** | raio de proteção por depósito; anel a cada 8-12mm | solver de transporte |
| **5% → 40-55%** | desaceleração clínica: hoje vs. pós-gates | bayes por analogia |
| **10 meses / R$300-800k** | organoide G0: o único experimento que decide tudo | protocolo público |
