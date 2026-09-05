# PADRAO_F6_ESTILO — 3 variantes determinísticas de tese (mesmo grafo, saídas distintas)

> Base comum: **ABNT NBR 14724 não é removida em nenhuma variante que a exige** (a institucional
> é a `abnt`). As três são GERADAS do mesmo grafo (blocos status=canonico, ordem seq) —
> determinismo por construção: mesma entrada → .tex byte-idêntico (gate).
> Camada Top-5 metodológica (JHU-estrutura-decisória · reporting-coverage · cronologia-honesta ·
> limitations-as-fruto · evidence-binding-auditável) aplicada onde cada formato hospeda.

## Os 3 contratos de render

| id | Classe/formato | Estrutura | Uso |
|---|---|---|---|
| **abnt** | `abntex2` 12pt A4 — NBR 14724 completa | pré-textuais (capa/folha/RESUMO/ABSTRACT/siglas) → 17 `\chapter` → pós-textuais (Apêndices A–F) · sumário ABNT · notas-auditoria por claim | **entrega institucional** (banca/depósito) |
| **prova** | `memoir` 11pt single-col — publicação-grade (JHU/Harvard) | contribution-first: abstract reforçado → capítulos como `\section` compactos · headers vivos · audit-notas superscript | leitura de banca/avaliadores, preprint-derivado |
| **kappa** | `article` + núcleo-kappa (Karolinska) | núcleo metodológico (c01–c13) + **apêndices elevados a "papers"** (A–F como anexos-paper com folhas próprias) · concordância como audit-trail | defesa-hostil (opponent) · coletânea |

## Mapeamento comum (bloco→LaTeX)

heading h1/h2/h3 → escalas por variante · parágrafo→texto escapado · `$$…$$`→`\[…\]` ·
tabela-pipe→`tabular` determinístico (header/sep/body; `\small`) · `![alt](path)`→`figure+includegraphics+caption` ·
listas→itemize/enumerate · quote→`quote` · hr→rule · `[claim:Cxxx]`→`\audit{Cxxx}` (abnt/kappa) ou
superscript (prova) · `[evidence:Exxx]`→nota · tiers preservados literalmente.

## Regras de ouro (herdadas, agora para .tex)

1. .tex é **descartável**: nunca editado à mão; bug LaTeX = bug do GERADOR.
2. Determinismo é gate: `render_latex(db,fmt)` duas vezes → arquivos idênticos.
3. Compilação (xelatex) é job CI opcional — PDF nunca é fonte da verdade (MD canônico é).
4. Os 3 .tex derivam do MESMO grafo: divergência de conteúdo entre eles = impossível por construção.
