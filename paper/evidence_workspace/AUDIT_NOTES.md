# Notas de auditoria — divergências documentadas (audit_claims)
## 2026-08-27 · suite completa: validate_manifest 0 err · check_references 0 err · check_consistency 0 warn · audit_claims: só UNTAGGED_NUMERIC_CONTENT residual (EN 42 / PT 40)

**Estado:** todas as claims (49/49) usadas nos dois idiomas, pares [claim]+[evidence] completos e consistentes com o registro, enum `verified`, paridade EN=PT exata.

**Divergência residual deliberada — UNTAGGED_NUMERIC_CONTENT (42 EN / 40 PT), decomposta:**
1. **34 identificadores bibliográficos** (DOIs 10.xxxx, PMIDs, anos, volume:página) na seção *References*. Não são fatos numéricos do estudo — são identificadores de fonte, já validados pelo `check_references` (0 erros). Tagging de claim sobre DOI seria ruído semântico.
2. **Contextuais-secundários no corpo** (epidemiologia: "~85% esporádica", "6–8 meses", "10–15%", ">50M"): declarados "contextual secondary" no texto, sem binding de claim por decisão da seção §2.1 (o peso científico não repousa neles).
3. **Linha da âncora ilustrativa κ↔µM (Tabela 1)**: o guardião (R2-ASSUM-TAGGED, nível BLOCKED) **proíbe** tag de evidência em estimativa ilustrativa — os dois validadores divergem aqui por propósito: a skill quer binding em todo número; o guardião quer separação assumção↔evidência. Resolução adotada: **a proibição do guardião prevalece para assumptions; a skill prevalece para fatos** — divergência documentada, não silenciada.

*Qualquer revisão futura deve manter esta decomposição atualizada.*
