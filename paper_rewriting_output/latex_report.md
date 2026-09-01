# LaTeX Report — edição unificada (braço-B)

- **Fonte:** `final_paper/tese_unificada.md` (PT-BR; arquitetura nota-à-banca→base-comum→fundamento→aplicação→métodos→validação→clínica→limitações→conclusões)
- **Build:** `pandoc → final_paper/main.tex` (preamble_unified.tex: XeLaTeX, TeX Gyre Termes, a4, margens 3/2cm, **coluna única justificada** — tese JHU/Harvard-class e ABNT A4 single; two-column é otimização de impressão de periódico) → `xelatex ×2` no CI (`unified-thesis-build.yml`), cwd=final_paper (paths ../.. das figuras)
- **Figuras:** Fig.4 + Fig.5 geradas ANTES do build por scripts determinísticos que leem SOMENTE JSONs do registro (auditável; número nunca digitado) — Termux não compila matplotlib (nota da casa); o CI valida
- **latex_guard (local):** **0 erros** · 130 warnings = falsos-positivos PT ("todo/toda/todos") + o TODO legítimo `{{TODO:TESE-FICHA}}` (ledger P-009, ficha da autora) + paths de figuras que só existem pós-geração no CI
- **Título/metadata:** \title + \maketitle via metadados pandoc (guard exigia)
- **Citações:** lista [1]–[58] ABNT no corpo (a casa usa régua própria; \cite{} formal na edição LaTeX fica como refino de venue — fora do escopo do braço-B)
- **Co-edição:** ABNT NBR 14724 institucional preservada (`paper/latex/tese_v2_ABNT.pdf` + workflow tese-abnt.yml intocado)
- **PDF versionado:** o CI comita `paper/pdf/tese_unificada_<stamp>.pdf` (padrão casa)

---

## ATUALIZAÇÃO — EDIÇÃO A+ (padrão-publicação, sessão 01/09 pós-adoção)

- **Gerador:** `scripts/build_aplus_tex.py` (determinístico; md-mestre gated é a única fonte) → `final_paper/main.tex`
- **Classe**: `report` 12pt A4 (capítulos de tese), margens 3/2cm, TeX Gyre Termes + **microtype**
- **Frontmatter**: titlepage (\maketitle) → abstract → nota-à-leitura → **TOC/LOF/LOT** → siglas
- **Citações**: **134 `\cite{e1..e58}` reais** em `thebibliography` (58 bibitems; regra hard paper-spine: zero colchete literal morto) — as tags-da-casa `[claim:Cxxx][evidence:Exx]` viram superscript cinza `\audit{}` (trilha de auditoria preservada sem poluir o texto A+)
- **Equações**: display-math numeradas (ADR; freeS/θ) no mestre via `$$`
- **Figuras**: `width=0.92\textwidth`, captions pandoc; **Apêndices em `\appendix`**
- **Conversão-completa**: 949 linhas-mestre (13 caps + A/B integrais + concordância; lista [1]-[38] duplicada do apA removida — A+ não duplica bibliografia)
- **latex_guard: 0 erros** · guardian unificado 0/0 · validadores SW 0/0
