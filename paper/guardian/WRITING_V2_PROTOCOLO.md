# WRITING-SYSTEM-V2 — Protocolo de Teste Isolado (PLAN_DOC do branch)
## Branch: `writing-v2-test` (nascido de main@bb6f23c) · Clone-dedicado = worktree-efetivo · 01/09

**Regra de isolamento (mandato da autora):** o novo sistema de escrita científica NÃO se mistura com a linha principal até PROVAR qualidade. Nada deste branch entra em main sem avaliação comparativa + sua aprovação + PR com CI.

## Protocolo de avaliação (espelha o que funcionou na alfa)
1. **Documento-âncora:** um trecho canônico fixo para comparação justa — **§4.7 + NOTA DE LEITURA** (mesmo conteúdo, dois sistemas).
2. **Braço A (baseline):** texto atual (main) — congelado.
3. **Braço B (novo sistema):** reescrita do MESMO trecho no novo sistema, neste branch.
4. **Métricas de avaliação (pré-declaradas antes de escrever o braço B):**
   - scholar-evaluation (developmental, 7 critérios da rúbrica alfa + critério novo "fidelidade-evidencial: zero claims/evidências perdidas ou inventadas")
   - guardian gates (o texto B precisa passar R0-R3 como qualquer superfície gated — sem isenção)
   - leitura cega pela autora (A vs B, qual prefere e por quê)
5. **Decisão:** se B ≥ A em qualidade E fidelidade-evidencial → PR para main + tag `writing-v2-adopted`; senão → branch arquivado com o aprendizado documentado (nada se perde, nada se mistura).

## Fronteiras inegociáveis (mesmas da casa)
Predições v1.0 comparadas · número só de JSON/registro · claims com hash + binding · tiers [SIM] · nenhum texto B substitui A sem gate.

## Pendência-bloqueadora (P-029 no ledger)
**Definir QUAL é o novo sistema** (fonte/metodologia/nome) — autora a especificar.
