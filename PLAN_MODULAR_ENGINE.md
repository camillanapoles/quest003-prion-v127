# PLANO — Motor Modular da Tese (tese-modular-md)

**Ancoragem:** branch `tese-modular-md` @ `94b792a` (ponto da validação-adversarial da autora — o plano de escrita completo que DEVE ser seguido rigorosamente).
**Norteador:** `paper_rewriting_output/final_paper/tese_unificada.md` (822 linhas, 13 caps, 72 tags `[claim:]`, Fig.4/Fig.5, registro probatório íntegro).

---

## 1 · Decisão de arquitetura (avaliação solicitada)

### 1.1 Remover LaTeX do fluxo crítico — ✓ CORRETO e fundamentado
Os **26 commits pós-94b792a** em `main` são todos da campanha latex-rescue (3 ondas para chegar a 0 erros). Prova empírica: LaTeX mantido à mão é o ponto de fragilidade. **Regra nova:**
- **MD é canônico.** Fonte da verdade dos textos = blocos MD no DB.
- **LaTeX/DOCX/PDF são SAÍDAS DERIVADAS**, geradas deterministicamente pelo render, nunca editadas à mão. Se quebra, corrige-se o *render*, não o artefato.

### 1.2 Backend + DB OO com FastAPI — ✓ ADEQUADO, com ajustes
- **SQLite + SQLModel** (Pydantic v2 + SQLAlchemy): o domínio é rico e relacional — 60 claims (sha256), 58 fontes (E001–E058), 65 N-fatos, blocos de seção, figuras, cross-refs, JSONs experimentais. CRUD + queries de integridade são exatamente o que os gates exigem.
- SQLite basta (local, single-writer, zero-config). Sem Postgres (YAGNI).
- **FastAPI** expõe CRUD + queries + endpoints de render + docs OpenAPI automáticas.

### 1.3 BAML vs Pydantic+instructor — △ AVALIAÇÃO: nenhum dos dois AGORA
- BAML/instructor são camadas de **saída estruturada de LLM**. O pipeline central aqui é **determinístico** (parse MD → DB → render). Nenhum LLM é necessário para integridade — e o protocolo garantista (m31 §2: "entradas só de registro") **proíbe** LLM no caminho probatório.
- **Decisão:** Pydantic puro (via SQLModel) agora. `instructor` fica como camada **opcional futura** (ex.: triagem semântica de blocos, sugestão de cross-refs — sempre atrás de gate humano). BAML: desnecessário (runtime próprio, ganho zero aqui).

### 1.4 Blocos modulares compatíveis MD↔LaTeX — ✓ É O PRODUTO
Todo bloco carrega: id estável, tipo tipado, texto canônico, refs (claims/fontes/N-fatos/figuras), lineage de números. Render MD e LaTeX consomem **o mesmo grafo** — compatibilidade por construção, não por conversão.

---

## 2 · Arquitetura

```
REGISTRO PROBATÓRIO (canônico, intocável)          TESE (texto canônico)
  claims.csv · claim_texts.md                         tese_unificada.md @94b792a
  source_manifest.json · consistency_manifest.json          │
  experiments/**/*.json (ws_7/ws_9/xspecies/m31/…)          │
        │                                                    │
        └───────────────► ingest ◄───────────────────────────┘
                               │
                        SQLite (modelos OO)
     Source · Claim · NFact · NumberValue · Chapter · Section
     Block(tipado) · Figure · CrossRef · RenderLog
                               │
                    ┌──────────┴──────────┐
                integrity.py           render/
          gates (falham o build)     md.py (canônico)
                                    latex.py (derivado)
                                    docx.py (pandoc, opcional)
                               │
                          api.py (FastAPI) + cli.py (typer)
```

**Pacote:** `thesis_engine/` (models, db, ingest/, crud, integrity, render/, api, cli).

**Blocos tipados:** heading, paragraph, math_block, math_inline, table, figure, list, quote, claim_ref `[claim:Cxxx]`, cross_ref `§x.y`, code. Parser: `markdown-it-py` (AST fiel, preserva byte-a-byte o texto canônico).

**Regras de ouro (herdadas da autora, agora mecânicas):**
1. Claim sem evidência → build FALHA (régua: "claim sem referência é inaceitável").
2. Número sem lineage (N-fato/JSON) → build FALHA ("número nunca digitado").
3. Ref `§` sem header correspondente → build FALHA (o fix do fractal, automatizado).
4. Figura sem JSON/script gerador → build FALHA (figuras auditáveis).
5. sha256 das claims preservado (imutabilidade do registro).

---

## 3.5 · Camada de TEXTO — produção escrita sob o skill `scientific-writing`

**Sim: o skill `scientific-writing` é o GOVERNANTE da produção de texto** (docs+dados → prosa da tese). E a integração é nativa: o registro probatório do repo JÁ segue a convenção exata do skill (E-IDs em `source_manifest.json`, C-IDs com sha256 em `claims.csv`, N/M/R em `consistency_manifest.json`, tags `[claim:Cxxx] [evidence:Exxx]`).

**Duas modalidades de texto no engine:**
- **Modo A — Conservação:** texto canônico existente (`tese_unificada.md`, já validado adversarialmente) → blocos **byte-preserving**, zero LLM.
- **Modo B — Produção:** texto NOVO/revisto (seções novas, reescrita, EN companion) via workflow do skill: *evidence-outline → draft sem acrescentar fatos → gates determinísticos → aprovação humana*. O agente-escritor transforma outline-de-evidência em prosa; **nunca** inventa citação/valor/método (regra no-fabrication do skill).

**Categorização OBRIGATÓRIA de todo bloco de texto (campos mandatórios do modelo `Block`):**

| Campo | Valores / Fonte da categoria |
|---|---|
| `block_type` | paragraph · math · table · figure · list · quote · heading |
| `function` | motivation · method · result · interpretation · limitation · transition · clinical-opener · nota-banca (alinhado à matriz R0–R9) |
| `claim_ids` | `[Cxxx]` — obrigatório em bloco factual |
| `evidence_ids` | `[Exxx]` — obrigatório onde há claim |
| `nfact_ids`/`number_lineage` | `[Nxxx]` + arquivo JSON→chave — obrigatório em bloco numérico |
| `tier` | `[SIM]` · `[SIM]-planejamento` · `[ORGANOID]` · `—` |
| `uncertainty` | not_applicable · low · moderate · high |
| `status` | draft → revised → validated → **author_approved** (só humana) |
| `blueprint` | B0–B9 (section_blueprints) |

Os specs de estilo que hoje são prosa (`style_profile.md`, `writing_rationale_matrix.md`) viram **metadados aplicados por gate**: decimais PT-BR vs EN, openers clínicos, proibições ativas ("promissor", promessa clínica), negação-de-segurança tripla, banda como par lo–hi.

**Gates do skill wired no CI do engine** (scripts locais, determinísticos, sem rede): `audit_claims.py` · `check_consistency.py` · `lint_manuscript.py` · `validate_manifest.py` · `check_references.py`.

**Divisão de papéis:** skill = governança do processo · agente-LLM = redator supervisionado (outline→prosa) · engine = armazém+render · **autora = único aprovador** (`author_approved` nunca é setado por máquina).

---

## 4 · TODOLIST (fases com gates)

- [x] **F0 — Setup** ✓ (commit ecd05ab)
  - [x] Deps: venv `.venv/` — pydantic-core 2.48 compilado (rust + `ANDROID_API_LEVEL=36`,Termux) · fastapi 0.141 · sqlmodel 0.0.42 · pydantic 2.13 · markdown-it-py · typer · pytest · requirements.txt
  - [x] CI: `unified-thesis-build.yml` → `thesis-build.yml` (MD-only: gates pytest + figs; LaTeX/DOCX = job `workflow_dispatch` p/ F6; histórico preservado em `main`)
  - [x] Scaffold `thesis_engine/` + `tests/`
- [x] **F1 — Modelos OO + ingest do registro** ✓ (commit ecd05ab)
  - [x] `models.py`: Source · Claim · NFact · MethodFact · ResultFact (listas em Column(JSON))
  - [x] Ingest: claims.csv + claim_texts.md · source_manifest.json · consistency_manifest.json (`ingest/registro.py`); `norm.py` = cópia exata da normalização sha256
  - [x] Gate: 60 claims / 58 fontes / 65 N-fatos / 4 métodos / 5 resultados · sha256 de TODAS conferido · integridade evidence→source · rebuild idempotente — **5/5 testes VERDE**
- [ ] **F2 — Parser da tese → blocos** (1–1,5 dia)
  - [ ] Parser MD → blocos tipados com ids estáveis (`cap07/sec7.2/blk0014`)
  - [ ] Vinculação: tags `[claim:]` → Claim; `§` → Section; figuras → Figure
  - [ ] Gate: round-trip MD → DB → MD == original (byte diff só em whitespace tolerado)
- [ ] **F2.5 — Camada de escrita (Modo B)** (1 dia)
  - [ ] Estender `Block` com os campos mandatórios de categorização (§3.5) + validador de schema
  - [ ] Backfill: blocos do Modo A recebem categorias inferidas das tags/posição (function/blueprint/tier)
  - [ ] Roteiro de produção Modo B: evidence-outline por seção → draft → `lint_manuscript` + `audit_claims` → fila de aprovação (`status=author_approved`)
  - [ ] Gate de estilo: decimais, openers clínicos, proibições ativas, tier em toda saída de dose
- [ ] **F3 — Ingest dos JSONs experimentais** (0,5–1 dia)
  - [ ] ws_7/ws_9/xspecies/m31/bayes/part2 → NumberValue com lineage (arquivo→chave)
  - [ ] Gate: todos os números citados nas tabelas da tese (§4.3) batem com o registro
- [ ] **F4 — CRUD + queries + API** (1 dia)
  - [ ] CRUD completo por entidade + queries de integridade
  - [ ] FastAPI: `/chapters /sections /blocks /claims /sources /nfacts /figures /integrity /render/{md|latex}`
  - [ ] CLI: `ingest · check · build · serve`
- [ ] **F5 — Render MD modular** (0,5–1 dia)
  - [ ] Saída canônica: `build/tese/` (1 arquivo por capítulo + índice) E `tese_unificada.md` single-file
  - [ ] Blocos 100% integrados: toda ref resolvida no grafo
- [ ] **F6 — Render LaTeX derivado** (1 dia)
  - [ ] Gerador determinístico blocos→`.tex` (ABNT/unified-thesis class existente como alvo)
  - [ ] Zero edição manual; se erro → corrige gerador. DOCX via pandoc (opcional)
- [ ] **F7 — Gates de integridade no CI** (0,5 dia)
  - [ ] `check`: 5 regras de ouro; build falha se qualquer gate quebra
  - [ ] Badge/log `integrity_report.json`
- [ ] **F8 — Docs + entrega** (0,5 dia)
  - [ ] README do engine · exemplo de uso da API · rollback/backup do DB

**Total estimado: ~6–7 dias de trabalho agentado.**

---

## 4 · Guardrails

- `main` preservada intacta (histórico latex-rescue nunca apagado; reversível).
- Registro probatório é **read-only** para o engine (nunca reescreve claims/fontes).
- DB é artefato derivado e versionável (`thesis.db` no .gitignore; rebuild = `cli ingest`).
- Qualquer edição de texto da tese passa pelos blocos (API/CLI), nunca em arquivo solto.
