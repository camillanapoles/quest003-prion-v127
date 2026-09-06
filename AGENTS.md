# AGENTS.md — Thesis Engine (Etrização / PrP-V127)

## O que é este projeto

Tese de doutorado em neurociência (doenças priônicas, plataforma terapêutica PrP-V127) com um **engine de escrita garantidor por princípio**: toda garantia é estrutural (código consulta DB e bloqueia), nunca documental.

**Autora:** Camilla N. — única que aprova (`author_approved` só dela).

## O engine em 60 segundos

| Peça | O quê |
|---|---|
| **DB** (SQLite) | 19 tabelas OO: 15 SETUP (imutáveis no ciclo) + 4 EXECUTION (zeradas no bootstrap) |
| **FastAPI** | 35+ endpoints incluindo `/cycle/{cap}/*` (API dirige o fluxo) |
| **FSM** | `WritingCycle`: brief→drafting→guard→gates→hostile→emenda→LOOP→approved→rendered→committed |
| **Guard** | Middleware verifica worktree do banco a cada request `/cycle/*` |
| **Pre-commit** | 3 camadas: pytest(69+) + cli.check(6 gates) + WritingCycle(blocos não-aprovados→BLOQUEIA) |
| **CI/CD** | GitHub Actions: gates + figuras + pipeline_diagram.html |

## Separação de poderes (NUNCA violar)

| Papel | Faz | NUNCA faz |
|---|---|---|
| **WRITER** (você) | escreve texto do zero | auto-aprova |
| **AUDITOR** (hostil) | questiona continuamente | escreve/emenda texto |
| **AUTORA** (Camilla) | aprova ou rejeita | — |

## Como escrever um capítulo

```bash
# 1. Bootstrap (DB novo)
.venv/bin/python -c "from thesis_engine.escritor import bootstrap_v2; print(bootstrap_v2())"

# 2. Iniciar ciclo (brief + skills injetados juntos)
.venv/bin/python -c "
from fastapi.testclient import TestClient
from thesis_engine.api import create_app
from thesis_engine.escritor import V2_DB
c = TestClient(create_app(V2_DB))
r = c.post('/cycle/c01/start')
print(r.json()['brief']['objetivo'])
print(r.json()['writer_skills'])
"

# 3. Escrever (rascunhos/cNN_*.md)
#    → toda afirmação factual termina com [claim:Cxxx] [evidence:Exxx]
#    → números SEMPRE dentro de claim (lineage)
#    → cronologia SEMPRE no documento (nunca "está no repo")

# 4. Submeter
c.post('/cycle/c01/submit', json={'markdown': Path('rascunhos/c01_xxx.md').read_text()})

# 5. LOOP até aprovação
r = c.get('/cycle/c01/status')
# se aprova=False: leia o que falta, EMENDE o rascunho, re-submeta

# 6. Aprovar (só se TUDO verde)
c.post('/cycle/c01/approve')

# 7. Render + commit
c.post('/cycle/c01/render')
git add -A && git commit
```

## Regras absolutas (NUNCA violar)

1. **NUNCA** copie texto do canônico (`tese_unificada.md`) — escreva do zero
2. **NUNCA** use termos LLM: verbatim, delve, comprehensive, robust, moreover, etc. (37 banidos)
3. **NUNCA** diga "está no repo com timestamp" — o leitor da tese NÃO TEM repo
4. **NUNCA** digite números sem `[claim:]` — lineage é obrigatória
5. **NUNCA** preencha a ficha acadêmica `{{TODO:TESE-FICHA}}` — EXCLUSIVA da autora
6. **NUNCA** pule o LOOP — sem `hostil_aprova=True`, sem render
7. **NUNCA** o auditor escreva emendas — auditor QUESTIONA; escritor REESCREVE
8. **NUNCA** opere em `~/etrizacao` (só symlinks) — repo é `~/q3ci3`

## Skills do escritor (injetadas no POST /start)

1. `article-writing` — prosa com voz de doutoranda, sem AI-slop
2. `paper-spine` — contribution-first, validação-por-resultados
3. `scientific-writing` — evidence-outline → draft-sem-acrescentar → gates
4. `scientific-critical-thinking` — valida metodologia ANTES de escrever
5. `consciousness-council` — deliber multi-perspectiva (metodólogo/clínico/epistemólogo/banca)

## Skills do auditor (ReviewQuestion no DB)

(a) factual verificável? (b) lógica válida? (c) confundidores? (d) lineage? (e) termo definido? (f) cronologia no papel? (g) **SOA HUMANO?**

## Estrutura (18 capítulos, c00-c17)

| Cap | Função | Claims âncora |
|---|---|---|
| c00 | front-matter + LISTA DE SIGLAS | — |
| c01 | nomear+diferenciar | C054 (definição P0-P6) |
| c02 | contrato formal (Q/OE/H) | C052 · C040 |
| c03 | plausibilidade (literatura) | C001-C023 |
| c04 | linha experimental (exp1→exp2=base) | C055-C057 · C013 |
| c05 | alicerce: θ* invariante | C055-C057 |
| c06 | produto: dose banda GUM | C058-C060 · E057/E058 |
| c07 | métodos formalizados P0-P6 | C046 · C052-C054 |
| c08 | resultados-validação M1-M5 | C038-C040 |
| c09-c13 | novidade·discussão·clínica·limites·conclusões | — |
| c14 | referências ABNT | todas |
| c15 | anexo: folhas de pré-registro | **A0001** (ação devedora) |
| c16-c17 | mapa da lógica + apêndices C-F | — |

## Comandos úteis

```bash
.venv/bin/python -m thesis_engine.cli status      # painel geral
.venv/bin/python -m thesis_engine.cli check       # 6 gates
.venv/bin/python -m thesis_engine.cli serve       # API + dashboard
.venv/bin/python -m thesis_engine.cli producao    # gates por capítulo
.venv/bin/python -m pytest tests/ -q              # testes
```

## Fontes de dados (IMUTÁVEIS — nunca editar)

- `paper/evidence_workspace/claims.csv` — 60 claims (sha256)
- `paper/evidence_workspace/source_manifest.json` — 58 fontes
- `paper/evidence_workspace/consistency_manifest.json` — 65 N-fatos
- `experiments/*/` — JSONs experimentais (ws_7, ws_9, xspecies, m31)

## Débitos conhecidos (corrigir quando encontrados)

1. 4 testes com falha (fixture isolation) — ver STATE_HANDOFF.md §5
2. 5 FKs implícitas (JSON lists + valores especiais "plano"/"SEED")
3. Dashboard não extrai secção específica do capítulo no sidebar

## Linha experimental (NUNCA esquecer)

**A tese emerge do EXPERIMENTO 2** (multi-espécie: camundongo/hamster/humano/vole). O experimento 1 (murino/humanização) é fase de SEGURANÇA, narrada e justificada. Dados do exp1 só onde inalterados. Anti-hindsight sempre IN-DOCUMENT.
