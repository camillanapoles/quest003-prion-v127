# STATE_HANDOFF — Motor Modular da Tese · registro persistente de continuidade

> **Função (padrão autonomous-agent-harness):** este arquivo é a MEMÓRIA de posição.
> Qualquer sessão futura (agente ou humana) que abrir este repo deve ler isto PRIMEIRO
> para saber onde estamos, o que cada coisa é, e o que vem depois. Atualizar a CADA fase.

---

## 0 · Cold-start: como retomar em 60 segundos

```
repo:      ~/q3ci3                        (cwd 'etrizacao' só tem symlinks p/ quests)
branch:    tese-modular-md                (âncora canônica: 94b792a "fix fractal")
           main = histórico latex-rescue (NUNCA apagar; reversível)
venv:      .venv/  (pydantic-core compilado c/ rust + ANDROID_API_LEVEL=36 — Termux)
engine:    thesis_engine/  · tests/ (41) · gates: .githooks/pre-commit + CI GitHub
CLI:       .venv/bin/python -m thesis_engine.cli ingest|check|build|serve
API:       create_app(db) · /docs · /integrity · /render/md
grafo 3trees: ~/etrizacao/graphify-out/ (884 nós · query: `graphify query "..."`)
plano:     PLAN_MODULAR_ENGINE.md  ·  este arquivo = posição viva
```

## 1 · Timeline de fases (estado em 2026-09-02)

| Fase | Estado | Commit | Entrega-chave |
|---|---|---|---|
| F0 setup | ✅ | ecd05ab | venv+stack · CI MD-only · scaffold |
| F1 registro→DB | ✅ | ecd05ab | 60 claims·58 fontes·65 N-fatos·sha256 conferido |
| F2 tese→blocos | ✅ | 55f53c3 | 524 blocos · round-trip BYTE-EXATO |
| F2.5 categorização | ✅ | 5fcb542 | ENUMs §3.5 · write-guard · gates estilo G1-G4 |
| F3 números c/ lineage | ✅ | 828a88d | 308 NumberValues · 12 âncoras §4.3 · anti-tamper |
| F4 API+CLI guardados | ✅ | a8c40b6 | CRUD Modo B · registro read-only · author_approved só humana |
| F5 render modular | ✅ | d30324e | 17 caps+SUMARIO · partição exata · check_bindings |
| débitos R1-R3 pinados | ✅ | e2828e0 | regressões permanentes (colisão·tier·G3) |
| **F5.7 grafo+plano global** | ✅ | 46aaddc | graphify→SQL (884/1145) · PLANO_GLOBAL_DA_TESE.md como dado OO · gate G7 |
| **HP-Cap produção+hostil** | ✅ | 3266ba0 | gates objetivo/coesao/gaps cumulativos · fila RevisaoHostil · 17 itens reais |
| **T1 elaboração hostil** | ✅ | d4f59de | 13 termos emendados na LISTA (round-trip ok) + 4 decisões respondidas — YELLOW 17→4, fila 0 abertos |
| **T2/G6 âncoras §6.3** | ✅ | 06644fa | check_sec63: 8 âncoras dose↔m31 (0,0–2,6·0,2/10,3·MW 22,83·halo 4/6·κ=8) · 6 gates no check |
| **F6 LaTeX 3 variantes (núcleo)** | ✅ checkpoint | 5ab5cab | abnt·prova·kappa determinísticas (byte-idêntico) · CI latex ativado · **F6.1 pendente: markdown inline (163 `**` sem textbf) + validar PDFs do artifact** |
| F7 gates no CI | ⏳ | — | scripts scientific-writing wired (audit_claims/lint/check_consistency) |
| F8 docs finais | ⏳ | — | README engine · plano de documentação executado |

## 2 · Topologia: 3 worktrees + repo engine (triangulação)

```
~/etrizacao/ (symlinks) ── graphify-out/  ← grafo dos 3 trees (77% EXTRACTED)
├── 003            ← quest master: KNOWLEDGE_CANON (F-43/F-44) · guardian/ · THETA_STAR_EXPLAINED · evidence_workspace
├── 003-executor   ← braço executor: hostile batteries · TESE-FICHA · manuscript EN
├── 003-gap-mapper ← braço gap: guardian reports · PLAN_2027
└── ~/q3ci3        ← REPO DO ENGINE (este) — q3ci3/paper/evidence_workspace = registro canônico INGERIDO
```
**Relação:** quests = arquivo epistêmico upstream (canon+guardian) · q3ci3 = fonte canônica da TESE (tese_unificada.md @94b792a) + engine. O grafo correlaciona os 3 quests; o engine correlaciona tese↔registro.

## 3 · Correlação validade (audit × grafo) — registro dos achados

**Queries executadas (evidência em ~/etrizacao/graphify-out):**
1. *"Quem governa os gates…" → **Paper integrity kernel** (`003/.codex/prompts/system.md`): "never infer submission readiness from green validators or compile success alone" · cadeia sha256 ws_9_v4_human 31f02e13 Colab≡repo · audit_claims.py (community Claim Audit Validators)
2. *"estrutura M1/M3/M2…" → M3 anti-hindsight core · PARTE3 invariante (predições v1.0 travadas) · SLR-analog I1-I5/X1-X4 declaradas ANTES do contato
3. *"θ* 0,333 + dose A6…" → θ*=1/(1+κ_min) travada v1.0 (THETA_STAR_EXPLAINED) · H-P3 · F-44 Cenário B hamster-refutado-honesto · **R0-DRIFT-TEX** (drift LaTeX↔fonte já ocorreu — F6 mata a classe)

**Validação do audit de escrita (A-F):** ESTRUTURA ✅ · METODOLOGIA ✅ · PÚBLICOS ✅ (3, com artefatos) · COESÃO-mecânica ✅ · gaps confirmados = G5/G6/G7.

## 4 · Harness-audit — ledger de achados (agent-architecture-audit, 12-camadas adaptado)

| ID | Severidade | Achado | Status/Plano |
|---|---|---|---|
| F1 | 🟡 ALTA | **Canon dos quests fora do engine** (F-43/F-44/H-P3 não ingeridos → risco divergência canon↔engine) | fix = F5.5/G6-canon (âncoras nomeadas) |
| F2 | 🟡 MÉDIA | **Kernel green≠ready** não documentado no engine (CI verde ≠ tese pronta) | ✅ documentado aqui + vai ao PLAN (invariante) |
| F3 | 🟢 MÉDIA | R0-DRIFT-TEX histórico prova drift LaTeX↔fonte | F6 resolve permanentemente (grafo único; JAMAIS 2ª fonte) |
| F4 | 🟢 BAIXA | 2 sistemas de gate: guardian.py (epistêmico-adversarial) × engine (mecânico-determinístico) | complementares — camada documentada (este §4) |

## 5 · Skills utilizadas — correlação ação↔skill (registro p/ continuidade)

| Skill | Onde/Quando | Ação que governa |
|---|---|---|
| **scientific-writing** | §3.5 do PLAN; Modo B; F7 | governança de escrita: evidence-outline→draft→gates→aprovação; scripts wired no CI em F7 |
| **incremental-implementation** | F0-F5 inteiras | fatias finas, 1 commit por fatia, compilável sempre |
| **test-driven-development** | todas as fases | RED→GREEN por fatia; 41 testes; tamper-tests provam gates |
| **autonomous-agent-harness** | ESTE arquivo | memória persistente + fila (§7) + consent/checkpoint (F6) |
| **graphify** | §3 correlação | validação por grafo dos 3 worktrees (queries como evidência) |
| **agent-architecture-audit** | §4 achados F1-F4 | harness-audit 12-camadas adaptado ao stack engine+gates+CI |
| **debugging-and-error-recovery** | bugs R1-R3, maturin/pydantic-core | causa-raiz antes de patch (colisão prefixo; tier hífen; assinatura G3) |
| **code-review-and-quality** | cada commit (gate-guardian) | qualidade + escopo disciplinado |
| **git-workflow-and-versioning** | commits atômicos convencionais | branch por fase · push + CI a cada fatia |
| **scientific-critical-thinking / paper-spine / peer-review / scholar-evaluation** | camada de escrita (audit §B/E) | orquestração V4 · avaliador garantista · revisão adversarial (= origem do 94b792a) |
| latex-rescue etc. | **APOSENTADAS por decisão** | LaTeX = render derivado (F6), nunca fonte manual |

## 6 · Metodologia de validação (multi-solução + validação-negativa)

1. **Positiva mecânica:** gates §4.3/estilo/bindings · 41 testes · CI GitHub
2. **Por triangulação:** 3 worktrees ↔ grafo ↔ engine (§2-3)
3. **Por NÃO-encontrar (negativa):** round-trip MD→DB→MD sem divergência (byte-exato — a não-existência de drift é o teste) · partição modular==single · tamper-tests (injetar erro PROVA detecção: §9.9, 0,999, "promissor", tiers zerados)
4. **Por autoridade:** kernel green≠ready → decisão final SEMPRE humana (`author_approved`)

## 7 · Fila imediata (task-queue persistente)

- [x] ~~Elaborar os 17 itens da fila hostil~~ ✓ T1 (d4f59de): 13 emendados + 4 respondidos
- [x] ~~F5.5-resto G6~~ ✓ T2 (06644fa): check_sec63 + 6 gates
- [ ] **F6**: LaTeX derivado do grafo único — **STOP: apresentar à autora DURANTE a fase (checkpoint pedido expressamente)**
- [x] ~~F6 núcleo~~ ✓ (5ab5cab): 3 variantes determinísticas + CI latex-derivado (run 33695547611)
- [ ] **F6.1**: markdown inline → LaTeX (**bold**→textbf · *itálico*→textit · `código`→texttt) · conferir PDFs do artifact CI · ajustar gerador onde quebrar (nunca o .tex)
- [ ] **F7**: scripts scientific-writing no CI (audit_claims·lint_manuscript·check_consistency) + integrity_report.json como artefato
- [ ] **F8**: README do engine · plano de documentação (uso da API, Modo B, rollback)

**Feito na F5.7 (46aaddc):** G7 entregue como `check_plano` (congruência plano↔tese + fontes resolvem: claims/figuras/JSONs/canon-tokens/comunidades) · grafo no SQL (`/graph?community=&q=`) · PLANO_GLOBAL_DA_TESE.md (329 linhas) single-source `plano_data.py`

## 8 · Invariantes (acima de qualquer skill/gate)

1. MD canônico; LaTeX/DOCX/PDF sempre DERIVADOS do grafo (nunca 2ª fonte)
2. Registro probatório read-only; sha256 imutável
3. `author_approved` SOMENTE humana; **CI verde ≠ tese pronta** (kernel)
4. Predições v1.0 jamais retreinadas; tiers em toda saída de dose; nunca fabricar
5. main intocada (histórico); toda fatia = commit verificável + CI
