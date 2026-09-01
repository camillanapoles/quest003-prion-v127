# GUARDIAN REPORT — paper v5 (hostile recursive reviewer)

**Rodadas executadas:** 3 · **Achados:** 6 (BLOCKED=0, AMEND=0, NOTE=6)

## Gate

**PASS — zero BLOCKED.** O manuscrito resiste à rodada recursiva; recomendação ao editor: aceitável como preprint com auditoria pública.

---

### [NOTE] R0-UNUSED — /data/data/com.termux/files/home/q3ci3/paper_rewriting_output/final_paper/tese_unificada.md
- **Problema:** Claims registradas mas não citadas no manuscrito: C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011, C012, C016, C017, C018, C019, C020, C021, C022, C023, C025, C026, C027, C028, C029, C030, C031, C039, C040, C041, C042, C043, C044, C045, C048, C049, C050.
- **Exigência:** Confirmar que são intencional (claims de outline/suplemento).

### [NOTE] R1-BATTERY-factual — claims
- **Problema:** Bateria hostil aplicada a 3 claims factual: Status de revisão por pares da fonte? (preprint ≠ revisado — rotular) | Fonte única ou corroboração independente? | Transferência de espécie/modelo → humano declarada? (IDs: C013, C014, C024)
- **Exigência:** Cada pergunta deve ter resposta no texto/manifesto; sem resposta → limitação.

### [NOTE] R1-BATTERY-method — claims
- **Problema:** Bateria hostil aplicada a 6 claims method: Self-test executado e arquivado? | Critérios de aceitação especificados ANTES do resultado? | Código+params arquivados no repo? (IDs: C015, C046, C047, C052, C053, C054)
- **Exigência:** Cada pergunta deve ter resposta no texto/manifesto; sem resposta → limitação.

### [NOTE] R1-BATTERY-result — claims
- **Problema:** Bateria hostil aplicada a 14 claims result: Pre-registrado ou post-hoc? (rotular explicitamente) | Baseline e critério de comparação definidos? | Incerteza/IC reportado? (IDs: C032, C033, C034, C035, C036, C037, C038, C051, C055, C056, C057, C058, C059, C060)
- **Exigência:** Cada pergunta deve ter resposta no texto/manifesto; sem resposta → limitação.

### [NOTE] R1-PREPRINT — manifest
- **Problema:** 3 fonte(s) preprint no manifest — o texto deve rotular status de revisão onde forem centrais.
- **Exigência:** Rotular no texto (ex.: bioRxiv preprint).

### [NOTE] R3-TODO-TESE-FICHA — todo-registry
- **Problema:** TODO aberto registrado: TESE-FICHA.
- **Exigência:** Resolver e remover o marcador (o relatório lista todos a cada gate).
