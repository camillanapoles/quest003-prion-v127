# MAPA DA AST — Arquitetura de Execução (gerada do DB)

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
| POST /cycle/{cap}/start | →brief | middleware + DB |
| POST /cycle/{cap}/submit | →hostile | write-guard + claims⊆registro |
| GET /cycle/{cap}/status | consulta | 3 gates + hostil_falou + ações |
| POST /cycle/{cap}/approve | →approved ou 409 | TODAS verdes |
| POST /cycle/{cap}/render | →rendered | only_approved=True |
| POST /cycle/{cap}/report | consulta | relatório do DB |

## DB — Auto-descritivo (TableRegistry)

### SETUP (15 tabelas — imutáveis no ciclo)
- `acaoedeedora`: Ações devedoras (semeadas + executadas)
- `chapter`: 17 capítulos (estrutura, read-only)
- `claim`: Claims C001-C060 (sha256 imutável)
- `environmentrule`: Guard de ambiente (repo/branch/forbidden)
- `graphedge`: Grafo arestas (1145, read-only)
- `graphnode`: Grafo 3-trees (884 nós, read-only)
- `methodfact`: Métodos M001-M004
- `nfact`: N-fatos N001-N065 (imutável)
- `numbervalue`: 308 números com lineage (read-only)
- `planchapter`: Plano global por capítulo (read-only)
- `resultfact`: Resultados R001-R005
- `reviewquestion`: 7 perguntas do revisor hostil (a-g)
- `source`: Fontes E001-E058 (imutável)
- `stylerule`: 37 regras de estilo (LLM-bans + PT-bans)
- `tableregistry`: Esta meta-tabela (auto-descrição do banco)

### EXECUTION (4 tabelas — zeradas no bootstrap)
- `block`: Blocos de texto (escritos pelo ciclo)
- `revisaohostil`: Fila do revisor hostil (perguntas/respostas)
- `section`: Seções (criadas pelo escritor)
- `writingcycle`: FSM do ciclo por capítulo

## Regras Ativas no DB

- **StyleRule**: 37 regras (35 LLM-bans + 2 PT-bans)
- **ReviewQuestion**: 7 perguntas (a, b, c, d, e, f, g)
- **EnvironmentRule**: 4 regras (expected_repo, expected_branch, forbidden_cwd, guard_message)

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
