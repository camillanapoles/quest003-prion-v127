# DECLARAÇÃO AST — cobertura, resultado e limites (pós-escrita-zero)

**De:** agente (escritor, Modo B) · **Data:** 2026-09-05 · **Repo:** ~/q3ci3 @ tese-escrita-zero
**Motivo:** na sessão de 04/09, o agente apresentou "AST 10/10 VERDE" como evidência de conformidade da escrita-zero. **Isso estava errado por conflação de superfícies.** Esta declaração corrige o registro.

## 1. O que a AST é

Bateria consolidada `experiments/ast_check.py` (A1–A10) que garante as superfícies **CANÔNICAS VELHAS** do programa: manuscritos `paper/manuscript_EN_v5.md` e `paper/manuscript_Parte2_v1.md` (+ seus PDFs), o registro probatório e o solver WS-7.

## 2. Resultado da rodada de 04/09 (reproduzível)

Comando: `python3 experiments/ast_check.py` — **o python3 do sistema** (numpy 2.4.4; o `.venv` do engine **não** tem numpy e faz A1 falhar com `ModuleNotFoundError`).

| Componente | O que valida | Resultado |
|---|---|---|
| A1 | self-tests do solver WS-7 (massa 100,0% · ℓ-err 0,5%) | PASS |
| A2 | guardian Parte 1 (manuscrito VELHO EN v5): 0 BLOCKED | PASS |
| A3 | guardian Parte 2 (manuscrito VELHO Parte2 v1): 0 BLOCKED | PASS |
| A4 | validate_manifest das 58 fontes: errors=0 | PASS |
| A5 | ratchet do registro: claims≥60 · fontes≥58 · N-fatos≥65 | PASS (60/58/65) |
| A6 | 14 artefatos-chave **de paper/** presentes | PASS |
| A7 | check_consistency (bateria): errors=0 | PASS |
| A8 | check_references (bateria): 0 erros/0 avisos | PASS |
| A9 | pendências garantistas: VERDICT PASS | PASS |
| A10 | **ergonomia: abre o PDF mais recente** | PASS — **mas abre a TESE VELHA** |

**VEREDITO: 10/10 — AST VERDE.**

## 3. O que a AST **NÃO** valida (o limite que foi omitido)

- **A2/A3** guardam os manuscritos v5/Parte2 — **não a prosa nova** c00–c16.
- **A6** confere artefatos de `paper/` — não os renders de `escrita-zero/render/`.
- **A10** abre `paper/pdf/tese_unificada_20260902-030359.pdf` (build de 02/09, **pré-escrita-zero**). A tese escrita-zero **nunca foi compilada em PDF**: existe como 17 arquivos MD (258 blocos, tese_v2.db). Termux não tem LaTeX local; o CI (`tese-abnt.yml`) compila o manuscrito velho via pandoc+xelatex, não o v2 (`thesis_engine/render/latex.py`, fmt='abnt', existe e não rodou até aqui).
- **Conclusão:** "AST 10/10" certifica que a escrita-zero **não corrompeu o canônico** (zero drift; registro íntegro) — **não certifica a prosa nova**.

## 4. A cadeia que de fato governa a escrita-zero (estado real, verificado)

1. **Registro:** ingest com sha256 por claim — 60/60 conferidas; 58 fontes; 65 N-fatos (ratchet A5 é o ponto de contato com a AST).
2. **Write-guard:** toda claim citada ⊆ registro — zero fantasmas (32/32 pares conferidos no c16; validação de pares claim↔evidence executada).
3. **Gates por capítulo:** objetivo/coesão/gaps × 17 caps — **17/17 verdes, HARD=0, YELLOW=1** (C051, planejada no c06, realizada no c08 — registrada H0130 e respondida como esperado-por-desenho).
4. **LOOP hostil:** 17/17 ciclos `approved`; `hostil_falou` em todos; fila com **zero itens abertos**; desta rodada: H0119–H0121 (c14), H0122–H0123 (c15), H0124–H0126 (c16), H0127–H0129 (c00), H0130 (informativo) — todos emendados ou respondidos.
5. **Ações devedoras:** 7/7 fechadas (A0001–A0007: executadas com evidência, ou por regra da autora).
6. **Estilo:** proibições 0; 3 openers clínicos (gate estilo VERDE).
7. **Gate-guardian no commit:** pytest **73/73**.
8. **`cli check`:** 6/6 gates VERDE (sec43 · sec63 · estilo · bindings · plano · produção).

## 5. Pendências declaradas (fora do alcance de AST e v2)

- **Compilação da escrita-zero em PDF** (pré-requisito para qualquer A10 futuro apontar para a tese nova) — exige LaTeX (CI ou máquina da autora); `render_latex(fmt='abnt')` pronto para gerar a fonte.
- FICHA (rosto/catalográfica/agradecimentos) — exclusiva da autora.
- URL E029 no registro canônico — decisão da autora.
- GATE-F (assinatura da PI) + F10 — dormentes por design.

## 6. Proposta (NÃO aplicada — decisão da autora)

A10 poderia etiquetar o PDF que abre ("build canônico de 02/09") ou preferir PDF v2 quando existir. O agente não altera a bateria da autora sem ordem.

---
*Assinado pelo agente que escreveu e que errou a apresentação — o erro original ("AST 10/10" como certificado da prosa nova) está registrado aqui para não se repetir.*

## 7. Efeito colateral declarado
Ao rodar a bateria, o A10 baixou de origin/main quatro builds antigos (`tese_unificada_20260902-02*.pdf`–`03*.pdf`, ~1,6 MB) para `paper/pdf/` — comportamento por design do componente — e o commit desta declaração os versionou junto. Se a autora preferir o diretório limpo, remover os quatro binários é um commit trivial.
