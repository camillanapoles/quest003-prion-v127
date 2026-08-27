# PARTE 2 — Artefato 2.5: Protocolo de Seleção de Parceiro (SLR-análogo, critérios pré-declarados)
## Como será escolhido o laboratório que executa o G0-wet — metodologia ANTES do contato
**v1 · 2026-08-27 · congelado por commit antes de qualquer abordagem (anti-hindsight)**

### 0. Pergunta focal e princípio
*Qual laboratório maximiza a probabilidade de um G0-wet válido e decisivo, dado o desenho travado (8 braços, θ_obs §2.7, SAP §2.5, kill §2.5)?*
A Parte 2 é **previsibilidade**: decidir o que medir, onde e em que dose antes de gastar recurso. A escolha de ONDE medir segue a mesma disciplina — critérios, inclusão/exclusão e pesos **declarados antes da triagem**, como uma revisão sistemática (SLR) de laboratórios em vez de artigos.

### 1. Identificação de candidatos (≈ "busca em bases")
| Fonte | Análogo SLR | Rendimento esperado |
|---|---|---|
| Autores de E007/E008 (Groveman/Caughey) | rastreamento por citação dos estudos primários | 1–2 labs (dono da plataforma) |
| Autores de E012 (Williams) + rede SCRT | rastreamento por intervenção | 1–2 (braço celular) |
| Rede E200K/príons BR (Smid, HUG-CELL/HC-FMUSP) | busca gray-literature nacional | 1–2 (hub BR) |
| Grupos LNP-mRNA CNS (rede E019) | busca por vetor | 1–2 (braço A7) |
| PRION 2026 (conferência) + ClinicalTrials.gov | alerta de novidade | novos pós-v1 |

### 2. Critérios de INCLUSÃO (binários — screening, análogo title/abstract)
- **I1** plataforma organoide-príon **publicada** (infecta + trata; peer-reviewed)
- **I2** manipulação de príons infecciosos com biossegurança certificada (BSL-3-equivalente)
- **I3** capacidade declarável de ≥64 organoides (8 braços × n=8) com controle de lote
- **I4** aceita pré-registro + publicação do negativo (kill-switch programático)
- **I5** colaboração formalizável (acordo de cooperação/termo) em ≤6 meses

### 3. Critérios de EXCLUSÃO (binários — qualquer um remove)
- **X1** sem instalação/prontuário para príon infeccioso (risco desqualificador)
- **X2** recusa de cegamento/randomização do scorer (validade comprometida)
- **X3** exige propriedade intelectual exclusiva sobre resultados/predições (bloqueia open-science)
- **X4** indisponibilidade de início em ≤12 meses

### 4. Pontuação ponderada (elegibilidade — pesos CONGELADOS agora, soma 100)
| # | Eixo | Peso | Escala 0–5 (âncoras) |
|---|---|---|---|
| A | **Posse da plataforma organoide-príon** (E007/E008-grade) | **25** | 5=publicou a plataforma; 3=organoides + príon sem ensaio de droga; 0=nenhum |
| B | Track record príon infeccioso humano (sCJD isolates) | 15 | 5=decadas; 3=recente; 0=nenhum |
| C | Capacidade braços×n (staff, cronograma realista) | 15 | 5=≥64 sem diluição de lote; 0=≤24 |
| D | Braço celular A5 (iPSC/editação/enxerto em organoide) | 10 | 5= publicado enxerto em organoide; 0=não opera |
| E | Braço A7 (LNP-mRNA intratecal/CNS) | 10 | 5=competência demonstrada; 0=terceiriza tudo |
| F | Co-localização com população-âncora (BR/E200K) | 10 | 5=hub BR com coorte; 0=sem vínculo |
| G | Aderência open-science (repo, dados, co-autoria ICMJE) | 10 | 5=prática usual; 0=resistente |
| H | Prontidão (início ≤6 meses) | 5 | 5=start imediato; 0=≥12m |

**Regras de decisão pré-declaradas:** score = Σ(eixo×peso)/5, normalizado 0–100. **Contato sequencial** do maior score para baixo (um por vez, janela de resposta 15 dias, follow-up único +15). **Empate (>5 pts de diferença)**: desempata A (plataforma). Nenhum candidato elegível → ativação do Plano B (Colab-na-bancada própria via parceria indireta de serviço), documentada como decisão.

### 5. Vetos absolutos (independem de score)
Segurança príon insuficiente in loco · recusa ao pré-registro/kill-switch · recusa de publicar negativo · conflito com consortium open-license (MIT/CC-BY).

### 6. Fluxo documentado (análogo PRISMA) + registro de decisão
`identificados (n) → triagem I1–I5 (n) → elegíveis pontuados (n) → contatados (n) → selecionado (1)`
Cada etapa registrada em `experiments/part2_results/partner_selection_log.md` (data, critério aplicado, evidência — publicação, e-mail, site). Score de cada candidato é **publicável**: julgamento estruturado declarado (mesma natureza dos pesos WS-8; TODO co-rating por segunda pessoa quando houver).

### 7. Pré-triagem v1 (estrutura aplicada HOJE aos candidatos conhecidos — julgamento estruturado, single-rater; reconfirmação ao contato)
| Candidato | I1 | I2 | I3 | I4 | I5 | Score (A–H) | Ordem |
|---|---|---|---|---|---|---|---|
| **Caughey/Groveman (RML-NIH)** | ✓ (E007,E008) | ✓ | ~ (n=8→12 a negociar) | ? | ? | ~85 (estim.) | **1º** (A=25 máx) |
| Williams/rede Calgary | ✓ (E012) | ✓ | ~ | ? | ? | ~70 | 2º |
| HUG-CELL/HC-FMUSP + Smid | ~ (organoides sim; príon-infect ?) | ? | ✓ (hub BR) | ? | ✓ | ~60 | 3º (eixo F máx) |
| Grupo LNP-mRNA (rede E019) | ✗ (sem I1 própria) | — | — | — | — | excluído p/ G0-inteiro; elegível como **subcontratado do braço A7** | papel técnico |

*Não há pontuação de laboratório específico além dos públicos das fontes E-registry; pontuações completas só após contato e verificação documental — os "?" permanecem não-pontuados por honestidade.*

### 7-bis. Instrumento executável (runbook + fichas)
A execução é ela mesma metodologia documentada: `partner_selection/RUNBOOK.md` (procedimento por etapa + padrão de prova por critério + regras de replicabilidade) e fichas máquina-verificáveis `candidates_v1.csv` / `contacts_log.csv` / `decision_log.md` — o que torna a seleção replicável por terceiros, como o fluxo PRISMA o é para artigos.

### 8. Ligação com a tese
Este protocolo É a Parte 2 em ação no plano da parceria: a previsibilidade aplicada à escolha de onde medir — com o mesmo padrão de auditabilidade da SLR do §2.1 do manuscrito (critérios antes de resultados, decisão reproduzível, registro público). Referência cruzada: THESIS_ROADMAP (componente 2.3) · G0_EXECUTION_FREEZE_CHECKLIST (novo item F10: parceiro selecionado por este protocolo) · G0_UNLOCK_DOSSIER (§3 o que o comitê recebe).
