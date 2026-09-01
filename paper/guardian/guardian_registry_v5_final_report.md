# GUARDIAN REPORT — paper v5 (hostile recursive reviewer)

**Rodadas executadas:** 3 · **Achados:** 12 (BLOCKED=0, AMEND=3, NOTE=9)

## Gate

**PASS — zero BLOCKED.** O manuscrito resiste à rodada recursiva; recomendação ao editor: aceitável como preprint com auditoria pública.

---

### [AMEND] R0-NBIND-N050 — ../manuscript_EN_v5.md
- **Problema:** N-fato N050 (s3_max_dev_pct_all_arms_Rnorm_vs_base (extremo N_x2 saturado)=245.3 percent) aparece no texto sem marker de rastreabilidade próximo.
- **Exigência:** Colocar [claim:Cxxx][evidence:Exxx] junto ao número ou remover o número.

### [AMEND] R0-NBIND-N060 — ../manuscript_EN_v5.md
- **Problema:** N-fato N060 (m31_mw_prp_mature_kda=22.83 kDa) aparece no texto sem marker de rastreabilidade próximo.
- **Exigência:** Colocar [claim:Cxxx][evidence:Exxx] junto ao número ou remover o número.

### [AMEND] R0-NBIND-N063 — ../manuscript_EN_v5.md
- **Problema:** N-fato N063 (m31_band_ratio_mean_x=52.6 ratio) aparece no texto sem marker de rastreabilidade próximo.
- **Exigência:** Colocar [claim:Cxxx][evidence:Exxx] junto ao número ou remover o número.

### [NOTE] R0-UNUSED — ../manuscript_EN_v5.md
- **Problema:** Claims registradas mas não citadas no manuscrito: C052, C053, C054, C058, C059, C060.
- **Exigência:** Confirmar que são intencional (claims de outline/suplemento).

### [NOTE] R1-BATTERY-factual — claims
- **Problema:** Bateria hostil aplicada a 33 claims factual: Status de revisão por pares da fonte? (preprint ≠ revisado — rotular) | Fonte única ou corroboração independente? | Transferência de espécie/modelo → humano declarada? (IDs: C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011, C012, C013, C014, C016, C017, C018, C019, C020, C021, C022, C023, C024, C025, C026, C027, C028, C029, C030, C031, C040, C041, C050)
- **Exigência:** Cada pergunta deve ter resposta no texto/manifesto; sem resposta → limitação.

### [NOTE] R1-BATTERY-method — claims
- **Problema:** Bateria hostil aplicada a 8 claims method: Self-test executado e arquivado? | Critérios de aceitação especificados ANTES do resultado? | Código+params arquivados no repo? (IDs: C015, C043, C044, C045, C046, C047, C048, C049)
- **Exigência:** Cada pergunta deve ter resposta no texto/manifesto; sem resposta → limitação.

### [NOTE] R1-BATTERY-result — claims
- **Problema:** Bateria hostil aplicada a 13 claims result: Pre-registrado ou post-hoc? (rotular explicitamente) | Baseline e critério de comparação definidos? | Incerteza/IC reportado? (IDs: C032, C033, C034, C035, C036, C037, C038, C039, C042, C051, C055, C056, C057)
- **Exigência:** Cada pergunta deve ter resposta no texto/manifesto; sem resposta → limitação.

### [NOTE] R1-PREPRINT — manifest
- **Problema:** 3 fonte(s) preprint no manifest — o texto deve rotular status de revisão onde forem centrais.
- **Exigência:** Rotular no texto (ex.: bioRxiv preprint).

### [NOTE] R3-TODO-BIORXIV-ADDENDUM — todo-registry
- **Problema:** TODO aberto registrado: BIORXIV-ADDENDUM.
- **Exigência:** Resolver e remover o marcador (o relatório lista todos a cada gate).

### [NOTE] R3-TODO-EMAIL-GROVEMAN — todo-registry
- **Problema:** TODO aberto registrado: EMAIL-GROVEMAN.
- **Exigência:** Resolver e remover o marcador (o relatório lista todos a cada gate).

### [NOTE] R3-TODO-GATEF-SIGNATURE — todo-registry
- **Problema:** TODO aberto registrado: GATEF-SIGNATURE.
- **Exigência:** Resolver e remover o marcador (o relatório lista todos a cada gate).

### [NOTE] R3-TODO-PARTNER-RUN — todo-registry
- **Problema:** TODO aberto registrado: PARTNER-RUN.
- **Exigência:** Resolver e remover o marcador (o relatório lista todos a cada gate).
