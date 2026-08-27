# GUARDIAN REPORT — paper v5 (hostile recursive reviewer)

**Rodadas executadas:** 3 · **Achados:** 14 (BLOCKED=0, AMEND=9, NOTE=5)

## Gate

**PASS — zero BLOCKED.** O manuscrito resiste à rodada recursiva; recomendação ao editor: aceitável como preprint com auditoria pública.

---

### [AMEND] R0-NBIND-N011 — ../manuscript_EN_v5.md
- **Problema:** N-fato N011 (mrna_redose_rule3=7 days maximum) aparece no texto sem marker de rastreabilidade próximo.
- **Exigência:** Colocar [claim:Cxxx][evidence:Exxx] junto ao número ou remover o número.

### [AMEND] R0-NBIND-N012 — ../manuscript_EN_v5.md
- **Problema:** N-fato N012 (mv2_titer_169dpi=213000.0 SD50/mg) aparece no texto sem marker de rastreabilidade próximo.
- **Exigência:** Colocar [claim:Cxxx][evidence:Exxx] junto ao número ou remover o número.

### [AMEND] R0-NBIND-N013 — ../manuscript_EN_v5.md
- **Problema:** N-fato N013 (mv1_titer_169dpi=1690.0 SD50/mg) aparece no texto sem marker de rastreabilidade próximo.
- **Exigência:** Colocar [claim:Cxxx][evidence:Exxx] junto ao número ou remover o número.

### [AMEND] R0-DRIFT-TEX — latex
- **Problema:** Números presentes no LaTeX e ausentes no manuscrito-fonte (drift): 103, 10441, 10615, 11458, 116, 137, 139, 2003, 2014, 2022, 2056, 2312, 253, 278, 3.9, 302, 330, 348, 361, 37844, 3948, 478, 5160, 522, 558.
- **Exigência:** Retropropagar ao md (source of truth) ou remover do LaTeX.

### [AMEND] R2-PT-MISSING — ..
- **Problema:** Companion PT sem claim-tags (paridade declarada como passo futuro).
- **Exigência:** Gerar manuscript_PT_v5.md com as mesmas tags.

### [AMEND] R2-PT-MISSING — ..
- **Problema:** Companion PT sem claim-tags (paridade declarada como passo futuro).
- **Exigência:** Gerar manuscript_PT_v5.md com as mesmas tags.

### [AMEND] R2-PT-MISSING — ..
- **Problema:** Companion PT sem claim-tags (paridade declarada como passo futuro).
- **Exigência:** Gerar manuscript_PT_v5.md com as mesmas tags.

### [AMEND] R2-PT-MISSING — ..
- **Problema:** Companion PT sem claim-tags (paridade declarada como passo futuro).
- **Exigência:** Gerar manuscript_PT_v5.md com as mesmas tags.

### [AMEND] R3-R3-UNLOCK — manuscript
- **Problema:** Interrogação epistêmica R3-UNLOCK: procedimento ausente.
- **Exigência:** Dossier de liberação do G0 (argumentário ao comitê) deve existir e ser referenciado na superfície de planejamento; claims do dossier não migram ao manuscrito sem gate.

### [NOTE] R0-UNUSED — ../manuscript_EN_v5.md
- **Problema:** Claims registradas mas não citadas no manuscrito: C001, C006, C009, C016, C021, C023.
- **Exigência:** Confirmar que são intencional (claims de outline/suplemento).

### [NOTE] R1-BATTERY-factual — claims
- **Problema:** Bateria hostil aplicada a 26 claims factual: Status de revisão por pares da fonte? (preprint ≠ revisado — rotular) | Fonte única ou corroboração independente? | Transferência de espécie/modelo → humano declarada? (IDs: C002, C003, C004, C005, C007, C008, C010, C011, C012, C013, C014, C017, C018, C019, C020, C022, C024, C025, C026, C027, C028, C029, C030, C031, C040, C041)
- **Exigência:** Cada pergunta deve ter resposta no texto/manifesto; sem resposta → limitação.

### [NOTE] R1-BATTERY-method — claims
- **Problema:** Bateria hostil aplicada a 5 claims method: Self-test executado e arquivado? | Critérios de aceitação especificados ANTES do resultado? | Código+params arquivados no repo? (IDs: C015, C043, C044, C045, C046)
- **Exigência:** Cada pergunta deve ter resposta no texto/manifesto; sem resposta → limitação.

### [NOTE] R1-BATTERY-result — claims
- **Problema:** Bateria hostil aplicada a 9 claims result: Pre-registrado ou post-hoc? (rotular explicitamente) | Baseline e critério de comparação definidos? | Incerteza/IC reportado? (IDs: C032, C033, C034, C035, C036, C037, C038, C039, C042)
- **Exigência:** Cada pergunta deve ter resposta no texto/manifesto; sem resposta → limitação.

### [NOTE] R1-PREPRINT — manifest
- **Problema:** 2 fonte(s) preprint no manifest — o texto deve rotular status de revisão onde forem centrais.
- **Exigência:** Rotular no texto (ex.: bioRxiv preprint).
