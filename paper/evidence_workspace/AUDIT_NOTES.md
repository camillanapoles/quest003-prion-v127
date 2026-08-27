# Notas de auditoria — divergências documentadas (audit_claims)
## 2026-08-27 · suite completa: validate_manifest 0 err · check_references 0 err · check_consistency 0 warn · audit_claims: só UNTAGGED_NUMERIC_CONTENT residual (EN 42 / PT 40)

**Estado:** todas as claims (49/49) usadas nos dois idiomas, pares [claim]+[evidence] completos e consistentes com o registro, enum `verified`, paridade EN=PT exata.

**Divergência residual deliberada — UNTAGGED_NUMERIC_CONTENT (42 EN / 40 PT), decomposta:**
1. **34 identificadores bibliográficos** (DOIs 10.xxxx, PMIDs, anos, volume:página) na seção *References*. Não são fatos numéricos do estudo — são identificadores de fonte, já validados pelo `check_references` (0 erros). Tagging de claim sobre DOI seria ruído semântico.
2. **Contextuais-secundários no corpo** (epidemiologia: "~85% esporádica", "6–8 meses", "10–15%", ">50M"): declarados "contextual secondary" no texto, sem binding de claim por decisão da seção §2.1 (o peso científico não repousa neles).
3. **Linha da âncora ilustrativa κ↔µM (Tabela 1)**: o guardião (R2-ASSUM-TAGGED, nível BLOCKED) **proíbe** tag de evidência em estimativa ilustrativa — os dois validadores divergem aqui por propósito: a skill quer binding em todo número; o guardião quer separação assumção↔evidência. Resolução adotada: **a proibição do guardião prevalece para assumptions; a skill prevalece para fatos** — divergência documentada, não silenciada.

*Qualquer revisão futura deve manter esta decomposição atualizada.*


## Verificação das E034–E038 (2026-08-27)
Abertas via busca web + landing pages PubMed/editor em 27/08/2026; identificadores confirmados das páginas (Geschwind PMID 24122181 · Haïk 24411709 · Newman 24554103 · Otto DOI 10.1212/01.WNL.0000113764.35026.ef · Mead 35305340). Re-confirmação humana pela autora responsável pendente (mesma prática das 5 críticas originais, commit 5d6e698).

## Reprodutibilidade do run bandeira [SIM] (2026-08-27 03:25)
A autora re-executou o WS-9 v4 humanizado no Colab e re-enviou JSON+PNG. Hash sha256 do JSON re-executado = `31f02e13485a…` — **idêntico** ao arquivado (experiments/ws_9_results/ws_9_v4_human.json). θ*=0.333, sweep κ, âncoras MV1/MV2 e relógio (144.02 d/unid) reproduzidos bit a bit pelo executor humano independente da sessão que gerou. Cadeia: Colab autora (26/08 23:02) → commit repo (23:48) → re-execução confirmada (27/08 03:25). O resultado central da Parte 1 é **reprodutível**, não apenas arquivado.
