# LaTeX Report — edição unificada (braço-B)

- **Fonte:** `final_paper/tese_unificada.md` (PT-BR; arquitetura nota-à-banca→base-comum→fundamento→aplicação→métodos→validação→clínica→limitações→conclusões)
- **Build:** `pandoc → final_paper/main.tex` (preamble_unified.tex: XeLaTeX, TeX Gyre Termes, a4, margens 3/2cm, **coluna única justificada** — tese JHU/Harvard-class e ABNT A4 single; two-column é otimização de impressão de periódico) → `xelatex ×2` no CI (`unified-thesis-build.yml`), cwd=final_paper (paths ../.. das figuras)
- **Figuras:** Fig.4 + Fig.5 geradas ANTES do build por scripts determinísticos que leem SOMENTE JSONs do registro (auditável; número nunca digitado) — Termux não compila matplotlib (nota da casa); o CI valida
- **latex_guard (local):** **0 erros** · 130 warnings = falsos-positivos PT ("todo/toda/todos") + o TODO legítimo `{{TODO:TESE-FICHA}}` (ledger P-009, ficha da autora) + paths de figuras que só existem pós-geração no CI
- **Título/metadata:** \title + \maketitle via metadados pandoc (guard exigia)
- **Citações:** lista [1]–[58] ABNT no corpo (a casa usa régua própria; \cite{} formal na edição LaTeX fica como refino de venue — fora do escopo do braço-B)
- **Co-edição:** ABNT NBR 14724 institucional preservada (`paper/latex/tese_v2_ABNT.pdf` + workflow tese-abnt.yml intocado)
- **PDF versionado:** o CI comita `paper/pdf/tese_unificada_<stamp>.pdf` (padrão casa)
