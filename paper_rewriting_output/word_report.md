# Word Report — paper.docx (edição unificada)

- **Fonte:** `tese_unificada.md` (arquitetura B0–B9; PT-BR; coluna única justificada)
- **Geração:** `pandoc tese_unificada.md -o paper.docx` (regenerado no CI com as figuras embutidas — localmente, sem matplotlib, as Fig.4/Fig.5 entram como texto-descritivo; o CI gera os PNGs antes da conversão)
- **Figuras:** Fig.4 (`fig4_theta_species.png`) e Fig.5 (`fig5_dose_ladder.png`) são geradas por scripts determinísticos que leem apenas JSONs do registro (número nunca digitado) — pipelines: `experiments/xspecies/make_fig4_thetaspecies.py` · `experiments/m31/make_fig5_doseladder.py`
- **Claims:** toda afirmação-numérica carrega `[claim:Cxxx] [evidence:Exxx]`; concordância no registro (`paper/evidence_workspace/claims.csv`; 60 claims · 58 fontes · 65 N-fatos)
- **Citações:** lista [1]–[58] ABNT ao final (a checagem formal `\cite{}` fica na edição LaTeX `main.tex`/CI; o .docx usa a lista numerada — sem literais soltos no corpo)
- **Co-edição:** este .docx é a edição de publicação; a edição institucional ABNT NBR 14724 permanece `paper/latex/tese_v2_ABNT.pdf`
- **TODO vivo (formato casa):** `{{TODO:TESE-FICHA:...}}` — ficha acadêmica a preencher pela autora (rastreado no ledger; não é placeholder de conteúdo)
- **Tier:** documento inteiro [SIM]-planejamento; a nota clínica carrega o aviso de não-conselho-médico
