# Final Artifact Manifest — braço-B (writing-v2-test)

| Artefato | Caminho | Estado |
|---|---|---|
| Tese unificada (md mestre) | paper_rewriting_output/final_paper/tese_unificada.md | 411 linhas; PT-BR; claims taggeadas C001–C060 |
| LaTeX | final_paper/main.tex (+ preamble_unified.tex) | latex_guard 0 erros |
| PDF | final_paper/paper.pdf (+ versionado paper/pdf/) | CI unified-thesis-build.yml (xelatex×2) |
| Word | final_paper/paper.docx | word_guard PASS (fontes TNR/headings pretos via fix_docx_fonts.py); TODO TESE-FICHA legítimo (P-009) |
| Figuras | fig4_theta_species.png · fig5_dose_ladder.png (+_data.json) | geradas no CI por scripts auditáveis |
| Registro probatório | paper/evidence_workspace/ (60/58/65) | validadores 0/0 · AST 9/9 · ratchet A5 |
| V4 gates | confirmed_contribution · results_validation · reviewer_audit | 3× PASS |
| CI | unified-thesis-build.yml (novo) · tese-abnt.yml (Fig.5 adicionada) | push-dispatched |
| Co-edição ABNT | paper/latex/tese_v2_ABNT.pdf | intocada |
| Pendências vivas | TESE-FICHA (autora) · recorte-artigo p/ periódico · co-rating P-parceiro | ledger |

## Categorias (pro-tier)
**required:** tese_unificada.md · main.tex/preamble · paper.pdf · paper.docx · figs 4-5 · registro 60/58/65 · V4 gates (contribution/results-validation/reviewer-audit) · evidence_bank/figure_asset_map/claim_register/source_inventory · section_blueprints/rationale-matrix · confirmed_motivation/confirmed_contribution · latex_report/word_report
**pro-extra:** m3_to_m2_validation (§§1-2+§5) · tabela resultados-como-validação (Cap.6) · registro de objeções 15-linhas com severity · fix_docx_fonts.py (ferramenta in-repo) · CI unified-thesis-build.yml · nota-de-desvio do citation_quality_audit · AST 9/9 + ratchet A5 60/58/65
**optional-word:** paper.docx (política TNR/headings-pretos aplicada)
**optional-translation:** EN companion existente (manuscript_Parte2_v1_EN.md) — fora do escopo do braço-B
**optional-submission:** ficha-acadêmica + recorte-artigo — pendências da autora (ledger)
**optional-review-response:** n/a (tese; sem carta de resposta no escopo)

## Desvio registrado (citation-bank × invariantes da casa)
O `artifact_check` exige banco com ≥3× citation_target (174 candidatos p/ 56-alvo) e ~80% recentes. O banco da casa tem **138 candidatos genuínos** e o alvo real do programa é o **E-registro verificado (58 fontes, validate_manifest --require-verified 0 erros)** — política "nenhuma citação vive fora do E-registro" (invariante acima do PaperSpine, declarada no config). Encher o banco a 174 com entradas não-verificadas para satisfazer a cota VIOLARIA a disciplina anti-fabricação da casa. Desvio documentado para a avaliação A-vs-B da autora (este é exatamente o tipo de tensão que a avaliação deve decidir).
