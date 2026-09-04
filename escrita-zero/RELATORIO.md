# RELATÓRIO — escrita do zero · RODADA 2 (reinício pós-retificação arquitetural)

Progresso: **c01 ✓ c02 ✓** · próximo: c03 · branch `tese-escrita-zero` · DB: `tese_v2.db` (bootstrap novo,
zero blocos canônicos) · rodada 1 arquivada em `escrita-zero/arquivo/` (referência, não base).

| Cap | Título | Gates (obj·coes·gaps) | Claims | Hostil |
|---|---|---|---|---|
| c01 | Nota à banca | ✓✓✓ | 6 (C004–C007, C027, C054) | 5 Qs: 3 emendas (preprint, deriva, kuru) · 2 respostas (aritmética décadas, promessa-anexo) |
| c02 | Introdução (contrato formal) | ✓✓✓ | 16 (contrato OE1–4/H1–3/M1–M5+R1) | 5 Qs: 4 emendas (bayes, θ* em H2, θ_obs, registro) · 1 resposta (validação-autora→anexo) + 7 stale resolvidos |

**Ordem topológica:** c01 ✓ → c02 → c03 → c04 → c05 → … → c13 → c14 → c15 → c16 → c00 (por último,
com siglas acumuladas e ficha da autora).

**AÇÕES DEVEDORAS (semeadas no bootstrap — cobradas no local):**
A0001@c15 folhas de pré-registro+versão (pend.) · A0002@c00 LISTA DE SIGLAS+FICHA (pend., ficha
EXCLUSIVA da autora) · A0003@c03 citar C027 + mapa visual opcional-autora (pend.) ·
A0004@plano refinar mapeamento section→caps (pend.)

**Fila hostil:** 71 itens (5 de c01 — todos fechados; 66 YELLOW de caps ainda não escritos,
auto-populados pelos gates cumulativos — abrem e fecham no ciclo de cada capítulo).

Saídas neste folder: `briefs/` (banco→escritor) · `render/` (capítulos aprovados) ·
`fila_hostil.json` · `acoes_devedoras.json` · rascunhos-fonte em `../rascunhos/`.

Ciclo por capítulo (cycle-new): brief → write → **LOOP UNTIL [guard → gates → hostile → fila]
hostil-aprova** → render → RELATORIO → commit. API: `python -m thesis_engine.cli serve --db tese_v2.db`.
