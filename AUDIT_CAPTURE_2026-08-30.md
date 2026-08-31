# AUDIT CAPTURE — Local + Remoto (2026-08-30)

**Método:** captura exaustiva local (AST, gates, TODO-registry, worktrees) + remota (GitHub API: branches/PRs/tags/releases/CI) → agrupamento → validação de divergências → ledger garantista (`PENDENCIAS.md`) + gancho A9. PLAN_DOC (exento de gates por desenho; nenhum claim migra para manuscrito daqui).

---

## §1 — AUDITORIAS LOCAIS

| Superfície | Resultado | Detalhe |
|---|---|---|
| AST `ast_check.py --fast` | **8/8 VERDE** | A2 gate P1 PASS (0 BLOCKED) · A3 gate P2 PASS (0 BLOCKED) · A4 manifest 38 fontes 0 erros · A5 registro 54/38/48 · A6 artefatos 14/14 · A7 consistência 48 N-fatos 0 warnings · A8 referências 0/0 · **A9 pendências PASS (novo)** |
| Gates guardian.py | PASS 0/0 (P1 e P2) | round=3, perfis part1+part2, BLOCKED-gates permanentes íntegros |
| Pre-commit hook | **EXISTE e bloqueante** | `.git/hooks/pre-commit` → `ast_check.py --fast`; falha = commit bloqueado (mandato zero-débito 28/08). Agora inclui A9 automaticamente |
| Portabilidade skills | **CORRIGIDA** | `ast_check.py` resolvia scripts da skill em `/workspace/...` (só existia no ambiente original) → agora: env `SCIENTIFIC_SKILLS_SCRIPTS` > repo-local `scripts/validators/` > `/workspace/...` > `~/.agents/...`. Bateria A4/A7/A8 verde em qualquer ambiente |
| TODO-registry (scan A9) | 9 marcadores vivos | PARTNER-RUN · GATEF-SIGNATURE · Q3Q5-OFFICIAL · IDENTIFY-ORGANOID-DONOR-LAB · TESE-FICHA · BIORXIV-ADDENDUM · EMAIL-GROVEMAN · COST-DECOMP · SEARCHLOG-FULL — todos mapeados no ledger |
| Marcadores obsoletos | 3 REMOVIDOS (higiene) | ETRIZACAO-APLICAR (aplicado+validado 29/08) · PUBMED-DIRECT (resolvido 29/08) · Q3-Q5-EXEC (superseded por Q3Q5-OFFICIAL) — "resolver = remover" |
| Worktree executor | Trabalho íntegro | 6 batches (~88 candidatos), verificação DOI/PMID CrossRef (CONFIRMA_EXATO/fuzzy, DIVERGE_ANO registrados), 49 bindings rascunhados, D-01 FECHADO via opção B (ausência de DALY priônico como dado: 5 provas + PMC12672555), D-02/D-03 FECHADOS, auto-auditoria honesta de D-02 reaberto |
| Worktree gap-mapper | Trabalho íntegro | GAP_MAPPER v1+v2 EXAUSTIVO (18 papers, GRADE): **4 parâmetros do modelo validados por literatura independente** (k_eff↔Corridon 2026; Kd 71nM↔Chen 2010; 2D local↔Hrabe 2004; difusão>fluxo↔Holter 2017); 3 gaps novos (5-7) classificados; ACTION_PLAN_CROSS_SPECIES (θ* invariante entre espécies; cenários A/B/C) |

## §2 — AUDITORIAS REMOTAS (GitHub: `camillanapoles/quest003-prion-v127`)

| Item | Estado |
|---|---|
| main | `9ad4428` (29/08 23:49 — PDF FINAL 170KB "tese etrizada"); projeção local **sincronizada** (etrização ×59, Apêndice B, FINAL.pdf presentes) |
| PRs | #1 paper-v5 MERGED 27/08 · #2 paper-v6/ACP MERGED 28/08 |
| Tags/releases | v1.0 (predições travadas) · v2.6 · v2.7 · v3.0 (5 assets) · v6.0 (3 assets) |
| Branches ativas | `executor` +10 diverged · `gap-mapper` +3 · `otimizacao-pqms-batch1` +4 (FULL.tex 1506L + TESE-FICHA-TEMPLATE + anexos) |
| Branch stale | `fix/fig1-parte1` +2/−70 |
| CI (`pdf-version-audit.yml`) | **0 runs** — consistente com GHA bloqueado por billing-privado (guardian.md §2) |
| Access | credencial store presente (`~/.git-credentials`) — push via API possível se necessário |

## §3 — DIVERGÊNCIAS VALIDADAS (grupo → veredito → desdobramento)

| # | Divergência | Veredito | Desdobramento (ledger) |
|---|---|---|---|
| D1 | main↔executor: 10 commits não-mergeados (candidatos/verificações) | Trabalho válido, estagiado — merge exige verificação claim-a-claim (regra P1.1) | P-003, P-021 |
| D2 | main↔gap-mapper: 3 commits (validações de parâmetros) | Validado por literatura, MAS não elevado a claims/E-registry (ainda ⊕-declarado, não binding) | P-022, P-001, P-002 |
| D3 | main↔otimizacao: FULL.tex + ficha-template não-mergeados | Pronto; merge pendente de OK da autora dos anexos P2.1/P2.2 | P-020, P-009 |
| D4 | fix/fig1-parte1 stale (70 atrás) | Obsoleta provável (fig1 de main já regenerada do grafo v3.2) — decisão de descarte/rebase é da autora | P-019 |
| D5 | /RECAPs ausentes 29–30/08 (regra 10 do decálogo) | Violação de protocolo confirmada — reconstruídos retroativamente do git (marcados como não-contemporâneos) | P-004 |
| D6 | Marcadores obsoletos (ETRIZACAO-APLICAR, PUBMED-DIRECT, Q3-Q5-EXEC) | "Resolver=remover" não aplicado — CORRIGIDO neste ciclo | P-005 |
| D7 | AST A4/A7/A8 falhavam fora do ambiente original (path `/workspace`) | Defeito de portabilidade, não metodológico — CORRIGIDO (resolução em cascata env>repo>2 fallbacks) | P-006 |
| D8 | Meta futura ≥150 fontes (P1.1) vs alvo AST A5 atual (≥38) | Consistente por enquanto (majoração só após elevação claim-a-claim) | P-003, P-018 |
| D9 | Git local inoperante: objetos = placeholders `.l2s.tmp_obj`, `fetch` falha na escrita de pack; loose-objects escrevem OK mas HEAD/index ilegíveis | Projeção de storage — commits locais impossíveis neste ambiente; via de registro = API GitHub (credencial existe) ou ambiente original | limitação de sessão (ver /RECAP) |

## §4 — Pendências → garantia (resumo)

22 itens no ledger: 18 abertos — **nenhuma pendência agente-planejada sem `{{DEFER:...}}` explícito** (5 deferidas com justificativa visível: P-001 P-002 P-015 P-018 P-019); 3 executadas-não-mergeadas (P-020/021/022, condicionadas a P-003/P-009/P-001-2); externas aguardam autora (4), lab (1), executor (3); 1 dormant declarada (SEARCHLOG-FULL); 1 bloqueada-externa (D-08 VizHub). **O A9 bloqueia commit** se qualquer planejada-agente perder a deferação, se evidência de fechada sumir, ou se marcador TODO divergir do ledger.
