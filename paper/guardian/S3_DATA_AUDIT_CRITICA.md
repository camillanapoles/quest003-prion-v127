# S3 DATA AUDIT CRÍTICA — Forense do dataset + inventário por espécie + adequação metodológica
## PLAN_DOC · 01/09 · Skill: scientific-critical-thinking · Papel: analista de dados adversarial
**Objeto:** `ws_9_v5_sweeps_S3.json` (22 runs), uso histórico S1/S2, e o inventário de cenários por espécie do ACTION_PLAN (pré-P-023). Nenhum número abaixo é digitado de memória — todos extraídos dos JSONs arquivados (regra §3.4).

---

## 1 · SUMMARY

Dataset S3 internamente coerente e cross-run consistente (5 execuções independentes da config κ=2/base = 0,819mm idênticas). O veredito C2 **se mantém** após auditoria. Porém a auditoria expõe: (a) os escapes são **dados censurados à direita** no canto do grid (2,828mm), não raios físicos — inclusive o 2,828 histórico do S1-exp1 é o MESMO valor censurado; (b) a decomposição de sensibilidade é mais extrema que o veredito agregado sugere: **só a classe Kt importa** para contenção e para o relógio — descoberta que REDUZ a carga de identificação do P-023; (c) três não-padrões dignos de nota (assimetria Kc no relógio, cap de matching em N_x2, MV2 censurado na hierarquia); (d) o inventário por espécie contém **afirmações de disponibilidade de dados ainda sem proveniência** e um problema de identificabilidade estrutural (5 parâmetros de observáveis agregados).

## 2 · STRENGTHS (o que o dataset faz bem)

| # | Ponto forte | Evidência |
|---|---|---|
| S-1 | **Determinismo cross-run**: κ=2/base = 0,819 idêntico em S1-exp2-k2, S2 (×3 C50) e S3-BASE — 5 runs independentes | S1/S2/S3 JSONs |
| S-2 | **C0 paridade cross-ambiente**: baseline 2,828/144,02 local = ref v4; cloud completou os braços sem desvio detectável | baseline S3 |
| S-3 | **Lei de escala limpa do relógio**: t2/t2_base = 0,492/2,103 para N±2× (esperado 0,5/2,0 — desvio ≤5%) | tabela S3 |
| S-4 | **Proveniência mecânica**: wall_s distingue local (~225-245s) de cloud (72s) — auditoria de execução embutida no próprio dado | wall_s coluna |
| S-5 | Critérios pré-registrados aplicados sem renegociação; escapes tratados como limite inferior | SKILL_SCOUT_S3 §4 + harvest |

## 3 · CONCERNS (por severidade)

### CRÍTICAS (ameaçam interpretação se não tratadas)

**E-S3-01 · Censura à direita disfarçada de valor.** Os três escapes (N_x2, C_Kt_x2, J_KtKr_x2 = 2,828) e o MV2 da hierarquia (2,828) são o **canto do grid**: hypot(48,48)px ÷ 24px/mm = 2,828mm. Não é raio físico — é fronteira do domínio. O S1-exp1-k2 histórico (2,828, "não contém") é o mesmo artefato. Tratamento correto: R ∈ [2,828, ∞). O veredito C2 não muda (critério ≥2× satisfeito por censura), mas **qualquer magnitude quantitativa além do flag "escape" é indefensável** com estes dados. *Ação: P-024 deve registrar escape-como-flag (ou grid maior / parada na fronteira).*

**E-S3-02 · Identificabilidade do P-023.** O ACTION_PLAN propõe extrair 5 parâmetros (K_autocat, K_frag, K_nucl, k_clear, [PrP^C]₀) por espécie a partir de observáveis agregados (incubação, PMCA, transgênicos). 5 incógnitas de 1-2 observáveis = **subdeterminado**; estimativas pontuais seriam ilusórias. *Mitigação que o próprio S3 licencia:* a decomposição (abaixo) mostra que só a **escala de Kt** controla contenção e relógio — logo P-023 precisa apenas de **Kt-scale + âncora de relógio por espécie**, com o resto herdado como razões murinas (declrado). Enunciado como banda, não ponto.

### IMPORTANTES (afetam leitura, não o veredito)

**E-S3-03 · Decomposição extrema (o padrão central que o veredito esconde):**
| Classe | efeito no relógio (t2 ratio) | efeito na contenção (R_norm) |
|---|---|---|
| Kt ±2× | 0,53/1,99 (≈proporcional) | **escape / −21%** |
| Kr ±2× | 0,99/1,02 (nulo) | +1,3%/−1,2% |
| Kc ±2× | 0,96/1,06 (quase nulo) | +2,9%/−2,2% |
Kt sozinho explica o C2. Confirmações independentes no dado: J_KtKr_x2 (tl=9,70, R_sim5=0,859) ≡ C_Kt_x2 (9,45, 0,859) — adicionar Kr×2 não muda nada; N_x0.5 ≡ J_KtKr_x0.5 (0,637 ambos — diferença é só Kc, ~nula). **Consequência científica:** a pergunta multi-espécie reduz-se a "qual a escala relativa de Kt (e de D_eff/clearance que fixam o Damköhler) na espécie" — e a consequência operacional: hamster (agregado ~10× mais rápido) deve exigir κ maior — **predição testável do P-024 antes de rodar** (travá-la).

**E-S3-04 · Matching imperfeito exatamente onde importa.** Clock-matching usa t2 do crescimento NÃO-tratado; nos braços que escapam, a dinâmica sob κ=2 diverge do crescimento livre → o pareamento por gerações é menos exato nos escapes. Além disso N_x2 foi **capado** (ideal 10,16 → usado 10,0; −1,6% das gerações). *Ação P-024: parear sobre a fase tratada OU reportar ambos os pareamentos; remover o cap (tl≤12).*

**E-S3-05 · Observáveis perdidos.** O driver registrou só final_R/t2/wall; simulate() retorna total0/totalf (e o motor grava T/TOT/U que o retorno descarta). Sem trajetória de massa não se distingue **transiente vs estado estacionário** — o 0,819 do BASE é convergido? A eficácia "contém" pode ser ainda-lento-crescendo. *Ação P-024: registrar totalf/total0 + slope final do raio (critério de convergência declarável).*

### MENORES

**E-S3-06 · Assimetria/curvatura não resolvida:** Kc_x0.5 desacelera 5,5% mas Kc_x2 acelera só 3,8% — não-linearidade que um DOE de 2 pontos não caracteriza; para espécies com diferenças >2× (hamster), braços log-espaçados {0,25, 0,5, 1, 2, 4} são necessários.
**E-S3-07 · C50 absorvido pelo regime:** 0,819 idêntico para C50 ∈ {20,100,200} — a frente opera em saturação (C≫C50); coerente com F-39, mas significa que este parâmetro é **não-identificável nestas condições** (informativo para o desenho do A6-wet: a dose-resposta deve varrer κ, não C50).
**E-S3-08 · Paridade cross-ambiente não-bitwise:** J-cloud (72s) vs braços locais — coincidências exatas (0,859=0,859) suportam equivalência, mas o teste C0 formal rodou local; declarar como limitação menor.

## 4 · AUDITORIA DO INVENTÁRIO POR ESPÉCIE (pré-P-023 — qualidade do dado afirmado)

| Espécie | Dado afirmado (ACTION_PLAN) | GRADE pós-auditoria | Não-padrões/lacunas |
|---|---|---|---|
| Camundongo | Kernel Igel completo; half-life Corridon; D_eff Thorne | **ALTA** (mas estirme-RML; relógio humanizado é renormalização, não dado humano) | é a origem do risco Damköhler que o S3 expôs |
| Humano | Relógio Groveman; half-life 4,8-6,4d "Corridon humano" | **MÉDIA** — Corridon testou **PrP humano em fundo MURINO** (V2 já declara); taxas relativas NÃO publicadas | braço humano não pode testar Damköhler como ponto: rodar como **banda ×{0,5,1,2}** (herda o envelope S3) |
| Hamster | "dados disponíveis p/ extrair" (Telling 1995; Castilla 2008) | **MÉDIA-BAIXA até prova** — fontes ainda não provenance-bound; observáveis agregados | identificabilidade (E-S3-02): extrair Kt-scale por banda; **pré-registrar predição: κ>2 necessário** |
| Bank vole | "ponte; suscetível" | **BAIXA** — transmissão/agregado; polimorfismo 129 interage com estirpe | confunde barreira de entrada com escala de taxa |
| Rato | "resistente = negativo" | **BAIXA** — resistência pode ser barreira de conversão/entrada, não taxa lenta | modelar como taxa≈0 misrepresenta mecanismo; usar como outlier declarado |
| Levedura | "taxas completamente publicadas" | **ALTA p/ forma funcional, IRRELEVANTE p/ contenção** — sem GPI/difusão extracelular/Hsp104≠mammaliano | escopar: valida o termo freeS apenas (DN trans), não o Damköhler |

**Conclusão de inventário:** apenas camundongo está pronto-como-ponto; humano pronto-como-banda; hamster/vole/rato exigem extração com proveniência E declaração de banda; levedura é teste ortogonal de forma funcional. Nenhuma afirmação "dados disponíveis" sem identificador é aceitável para entrar no P-024 (regra: identifier de fonte aberta).

## 5 · RECOMMENDATIONS (específicas, acionáveis)

1. **P-024 spec (travar antes de rodar):** flag escape (não raio) para censura E-S3-01 · pareamento duplo (livre E tratado) + tl≤12 · registrar total0/totalf + slope final · braços log-espaçados quando span>2× · braço humano como banda ×{0,5,1,2}.
2. **P-023 spec:** extrair por espécie apenas Kt-scale + âncora de relógio (com IC/banda e fonte por parâmetro); demais classes herdadas como razões murinas DECLARADAS; elevar Corridon 2026 → E039 ANTES de usá-lo como âncora universal.
3. **Pré-registrar hoje (anti-hindsight):** "se Kt-scale_hamster ≥ 2× murino ⇒ contenção κ=2 falha no braço hamster" — derivada do S3, testável no P-024, comparável ao release.
4. Canon F-43: anexar nota de censura (R_norm dos escapes = limite inferior; idem S1-exp1 histórico).
5. Distinguir em toda saída: raio **físico** (não-censurado) vs **flag de escape**.

## 6 · OVERALL ASSESSMENT

Dataset **adequado ao veredito C2 e inadequado a qualquer quantificação de magnitude de escape** (censura). A força maior é a decomposição mecanicista limpa (Kt-dominância) — que simultaneamente simplifica o programa multi-espécie e concentra todo o risco epistêmico num único parâmetro por espécie. O inventário por espécie está 1/6 pronto como ponto, 1/6 como banda, 4/6 exigem proveniência. **O veredito C2 sobrevive à auditoria; as recomendações 1-3 são pré-condições de validade do P-024.**
