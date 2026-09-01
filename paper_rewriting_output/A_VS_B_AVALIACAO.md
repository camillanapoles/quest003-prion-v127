# AVALIAÇÃO A-VS-B — material para a decisão da autora (P-030, sessão 01/09)

**O que é o A (baseline):** `paper/manuscript_Parte2_v1.md` (tese v2 Parte-3-integrada; edição ABNT `tese_v2_ABNT.pdf`) — congelado.
**O que é o B (novo sistema):** branch `writing-v2-test` — tese unificada via PaperSpine V4 (este braço) + M3.1 integrado.

## 1. O que o B entrega que o A não tem

| # | Entrega do B | Onde |
|---|---|---|
| 1 | **Arquitetura da autora** (M1-nota→M3-fundamento→M2-aplicação) executada como capítulos 1-4 com cronologia honesta na abertura | tese_unificada.md Caps. 1-4 |
| 2 | **M3.1 integrado à tese**: §4.3 "primeira dose calculada" + Fig.5 + escada por banda-Kt + claims C058-C060 | Cap. 4.3 |
| 3 | **Base comum como capítulo-âncora** (validação M3→M2 tabela íntegra) | Cap. 2 |
| 4 | Resultados-como-validação explícitos (8 promessas→evidência) | Cap. 6 |
| 5 | Limitações reorganizadas por classe com o gate que fecha cada (11) | Cap. 8 |
| 6 | Edição de publicação: main.tex (latex_guard 0 erros), PDF xelatex coluna-única justificada, docx TNR | final_paper/ + CI |
| 7 | V4 hard-gates: contribution + results-validation + reviewer-audit (15 objeções com severity) | paper_rewriting_output/ |
| 8 | Registro probatório ampliado: 60 claims/58 fontes/65 N-fatos; E057 Chen 2010 verificada full-text | evidence_workspace/ |

## 2. O que o A tem que o B não replicou (1:1)

- O texto mestre ABNT completo (Cap. 2-fundamentação bibliográfica integral, Apêndice B.1-B.5 na íntegra, tabela-M completa) — o B referencia-os por apêndice/registro em vez de duplicar (decisão anti-duplicação; a banca pode preferir tudo inline).
- Camada clínica: o B carrega a versão condensada; a alfa tinha mindmap/caixa extras.
- EN companion: fora do escopo do B (manuscript_Parte2_v1_EN.md intocado).

## 3. Tensões/desvios que a decisão deve pesar

1. **Citation-bank × E-registro**: PaperSpine exige 3× candidatos (174) e ≥80% desde 2023; a casa tem 138 genuínos e política "citação só do E-registro verificado" — a cota foi RECUSADA por violar anti-fabricação (documentado em artifact_check.md). Se adotar B: aceitar a política da casa como override permanente do PaperSpine.
2. **Quality-audit offline** heurístico (FAIL por truncamento de display) — desvio documentado; manifest autoritativo.
3. **TODO TESE-FICHA** permanece (ficha acadêmica = autora; P-009).
4. **Fidelidade-evidencial**: zero claims perdidas ou inventadas no B (toda claim do B é tag do registro; claims novas C058-C060 passaram gates antes de entrar no texto).

## 4. Como decidir (protocolo WRITING_V2 §4)
scholar-evaluation (rúbrica alfa + critério fidelidade-evidencial) sobre §-âncora comum (Cap. 4 aplicação B vs Cap. 4 resultados A) · guardian gates (B passa R0-R3? — superfícies gated do B: registro ✓; tese_unificada.md ainda NÃO roda no perfil part2 do guardião — pendência se adotar) · **leitura cega pela autora** (prefere A ou B e por quê).

## 5. Estado dos gates (evidência)
AST 9/9 local + CI AST Quality Gate SUCCESS (writing-v2-test) · validadores registro 0/0 · V4 3× PASS · latex_guard 0 erros · word_guard PASS (exceto TODO legítimo) · integrity_audit ALL CLEAN · CI build unificado: PDF+docx versionados.

---

## ATUALIZAÇÃO (pós-rodada, 01/09 ~21:40): métrica-2 EXECUTADA pelo agente — B passou

O gate guardian R0-R3 perfil-part2 foi rodado NA tese unificada (metric §4 do protocolo, "sem isenção"):
- **1ª rodada: FAIL 21 BLOCKED / 30 AMEND** — todas de classe contrato-de-tag (B over-taggeava assumptions κ↔µM como se fossem medida; canon não referenciado)
- **Correção em 1 iteração** (dialeto-da-casa) → **PASS 0 BLOCKED / 0 AMEND** — mesmo patamar contratual do A (relatório: paper/guardian/guardian_report_unified_test.md)
- B agora detém: gate 0/0 ✓ · AST 9/9 @ ratchet 60/58/65 ✓ · validadores 0/0 ✓ · V4 3×PASS ✓ · CI superconjunto ✓
- **O veredito do agente passa a ser: ADOTAR B** (ver matriz e justificativa na conversa com a autora; métrica-3 leitura-cega permanece dela)
