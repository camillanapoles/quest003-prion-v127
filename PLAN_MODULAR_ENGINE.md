# PLANO MODULAR DO ENGINE — documento-canônico (consolidado)

> **Estado:** Este plano foi consolidado. A todolist F0-F8 vive em `STATE_HANDOFF.md §1`.
> O plano global da tese (17 caps, ordem lógica, valor, garantias) vive em
> `PLANO_GLOBAL_DA_TESE.md` e como dado OO em `thesis_engine/plano_data.py → PlanChapter`.
> Este arquivo é o ponto de entrada arquitetural.

## Arquitetura (imutável)

- **OO em DB** (SQLModel/Pydantic): 15 modelos incluindo StyleRule·ReviewQuestion·WritingCycle
- **FastAPI** gerencia CRUD + queries + gates + events (34 endpoints incluindo /cycle/*)
- **MD canônico** (nunca LaTeX manual; LaTeX/DOCX/PDF = derivados do grafo)
- **Registro probatório read-only** (sha256 imutável)
- **Gate-driven**: pre-commit local + CI GitHub + write-guard na API + hostil_falou

## O ciclo (cycle-new)

```
brief → write → LOOP UNTIL [guard → gates → hostile → fila] hostil-aprova → render → RELATORIO → commit
```

## Invariantes (acima de qualquer gate)

1. CI verde ≠ tese pronta (kernel: "never infer readiness from green validators alone")
2. `author_approved` SÓ humana
3. Nunca 2ª fonte LaTeX
4. Números sempre via claims (lineage por tag)
5. Cronologia/precedência sempre IN-DOCUMENT (leitor não tem repo)
6. hostil_falou: capítulo sem round hostil da prosa NUNCA aprova
7. Ficha acadêmica EXCLUSIVA da autora

## Fases (estado vivo em STATE_HANDOFF.md §1)

F0-F6 ✓ · F7 (scripts scientific-writing no CI) ⏳ · F8 (docs finais) ⏳
Resscrita do zero: branch `tese-escrita-zero` (ver §9 do handoff)
