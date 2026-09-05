"""Gera mapa da AST a partir do TableRegistry (auto-descritivo, do DB)."""
from pathlib import Path

from sqlmodel import Session, select

from thesis_engine.db import create_db
from thesis_engine.escritor import V2_DB
from thesis_engine.models import EnvironmentRule, ReviewQuestion, StyleRule, TableRegistry

with Session(create_db(V2_DB)) as s:
    regs = s.exec(select(TableRegistry).order_by(TableRegistry.categoria, TableRegistry.table_name)).all()
    stylerules = s.exec(select(StyleRule)).all()
    questions = s.exec(select(ReviewQuestion)).all()
    envrules = s.exec(select(EnvironmentRule)).all()

setup = [r for r in regs if r.categoria == "setup"]
execution = [r for r in regs if r.categoria == "execution"]
llm_bans = sum(1 for r in stylerules if r.tipo == "llm_ban")
pt_bans = sum(1 for r in stylerules if r.tipo == "pt_ban")

L = f"""# MAPA DA AST — Arquitetura de Execução (gerada do DB)

## FSM (WritingCycle — máquina de estados)

```
brief → drafting → guard → gates → hostile
                                          ↓ (se reprovado)
                                       emenda → LOOP (re-submit)
                                          ↓ (se aprovado)
                                      approved → rendered → committed
```

## Event-Driven Guard (middleware FastAPI)

```
Request → /cycle/* → check_environment(DB) → OK → endpoint
                                        → FAIL → 412 + instruções
```

## API Endpoints (cycle)

| Endpoint | Transição FSM | Guardas |
|---|---|---|
| POST /cycle/{{cap}}/start | →brief | middleware + DB |
| POST /cycle/{{cap}}/submit | →hostile | write-guard + claims⊆registro |
| GET /cycle/{{cap}}/status | consulta | 3 gates + hostil_falou + ações |
| POST /cycle/{{cap}}/approve | →approved ou 409 | TODAS verdes |
| POST /cycle/{{cap}}/render | →rendered | only_approved=True |
| POST /cycle/{{cap}}/report | consulta | relatório do DB |

## DB — Auto-descritivo (TableRegistry)

### SETUP ({len(setup)} tabelas — imutáveis no ciclo)
"""
for r in setup:
    L += f"- `{r.table_name}`: {r.descricao}\n"

L += f"\n### EXECUTION ({len(execution)} tabelas — zeradas no bootstrap)\n"
for r in execution:
    L += f"- `{r.table_name}`: {r.descricao}\n"

L += f"""
## Regras Ativas no DB

- **StyleRule**: {len(stylerules)} regras ({llm_bans} LLM-bans + {pt_bans} PT-bans)
- **ReviewQuestion**: {len(questions)} perguntas ({", ".join(q.letra for q in questions)})
- **EnvironmentRule**: {len(envrules)} regras ({", ".join(r.rule_key for r in envrules)})

## Pre-Commit (3 camadas)

1. pytest (73 testes)
2. cli check (6 gates determinísticos)
3. WritingCycle (blocos não-aprovados → BLOQUEIA)

## Invariantes (acima de qualquer gate)

1. CI verde ≠ tese pronta
2. author_approved SÓ humana
3. Nunca 2ª fonte LaTeX
4. Números sempre via claims (lineage)
5. Cronologia sempre IN-DOCUMENT
6. hostil_falou: sem round hostil = sem aprovação
7. Ficha acadêmica EXCLUSIVA da autora
"""

out = Path("escrita-zero") / "AST_MAPA.md"
out.write_text(L, encoding="utf-8")
print(f"AST_MAPA.md: {len(L.splitlines())} linhas · {len(setup)} setup + {len(execution)} execution")
