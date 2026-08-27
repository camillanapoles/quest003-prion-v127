# GUARDIAN REPORT — paper v5 (hostile recursive reviewer)

**Rodadas executadas:** 3 · **Achados:** 38 (BLOCKED=2, AMEND=31, NOTE=5)

## Gate

**FAIL — existem achados BLOCKED.** Revisor hostil nega submissão até resolução.

---

### [BLOCKED] R3-R3-THETA-OPS — manuscript
- **Problema:** Interrogação epistêmica R3-THETA-OPS: procedimento ausente.
- **Exigência:** A predição travada θ<0.33 exige definição OPERACIONAL de como θ é medido/estimado em organoides (senão é infalsificável/circular).

### [BLOCKED] R3-R3-SAP — manuscript
- **Problema:** Interrogação epistêmica R3-SAP: procedimento ausente.
- **Exigência:** Plano estatístico do G0 (teste, α, correção de multiplicidade, poder) deve estar NO manuscrito, não só no protocolo.

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

### [AMEND] R1-NUM-UNBOUND — ../manuscript_EN_v5.md
- **Problema:** Números decimais no texto sem N-fato e sem marker de assumption: 0.20, 0.70, 1.0, 1.1, 1.2, 1.25, 1.69, 10.1007, 10.1016, 10.1038, 10.1056, 10.1073, 10.1126, 10.1186, 10.1371, 17.703887, 2.13, 2.303, 2.5, 2.6
- **Exigência:** Ligar a N-fato/claim, ou rotular como assumption ilustrativa no contexto.

### [AMEND] R2-ASSUM-UNLABELED — ../manuscript_EN_v5.md
- **Problema:** Estimativa κ↔concentração sem rótulo de assumption: 8 µM; across the plausible secretion range this spans ≈0....
- **Exigência:** Rotular '(illustrative; not a measured secretion estimate)'.

### [AMEND] R2-ASSUM-UNLABELED — ../manuscript_EN_v5.md
- **Problema:** Estimativa κ↔concentração sem rótulo de assumption: 1–1 µM....
- **Exigência:** Rotular '(illustrative; not a measured secretion estimate)'.

### [AMEND] R2-ASSUM-UNLABELED — ../manuscript_EN_v5.md
- **Problema:** Estimativa κ↔concentração sem rótulo de assumption: 1–1 µM interstitial V127ΔGPI at the deposit peak....
- **Exigência:** Rotular '(illustrative; not a measured secretion estimate)'.

### [AMEND] R2-ASSUM-UNLABELED — ../manuscript_EN_v5.md
- **Problema:** Estimativa κ↔concentração sem rótulo de assumption: 1–1 µM (c(1mm)≈0....
- **Exigência:** Rotular '(illustrative; not a measured secretion estimate)'.

### [AMEND] R2-PT-MISSING — ..
- **Problema:** Companion PT sem claim-tags (paridade declarada como passo futuro).
- **Exigência:** Gerar manuscript_PT_v5.md com as mesmas tags.

### [AMEND] R2-ASSUM-UNLABELED — ../manuscript_EN_v5.md
- **Problema:** Estimativa κ↔concentração sem rótulo de assumption: 8 µM; across the plausible secretion range this spans ≈0....
- **Exigência:** Rotular '(illustrative; not a measured secretion estimate)'.

### [AMEND] R2-ASSUM-UNLABELED — ../manuscript_EN_v5.md
- **Problema:** Estimativa κ↔concentração sem rótulo de assumption: 1–1 µM....
- **Exigência:** Rotular '(illustrative; not a measured secretion estimate)'.

### [AMEND] R2-ASSUM-UNLABELED — ../manuscript_EN_v5.md
- **Problema:** Estimativa κ↔concentração sem rótulo de assumption: 1–1 µM interstitial V127ΔGPI at the deposit peak....
- **Exigência:** Rotular '(illustrative; not a measured secretion estimate)'.

### [AMEND] R2-ASSUM-UNLABELED — ../manuscript_EN_v5.md
- **Problema:** Estimativa κ↔concentração sem rótulo de assumption: 1–1 µM (c(1mm)≈0....
- **Exigência:** Rotular '(illustrative; not a measured secretion estimate)'.

### [AMEND] R2-PT-MISSING — ..
- **Problema:** Companion PT sem claim-tags (paridade declarada como passo futuro).
- **Exigência:** Gerar manuscript_PT_v5.md com as mesmas tags.

### [AMEND] R2-ASSUM-UNLABELED — ../manuscript_EN_v5.md
- **Problema:** Estimativa κ↔concentração sem rótulo de assumption: 8 µM; across the plausible secretion range this spans ≈0....
- **Exigência:** Rotular '(illustrative; not a measured secretion estimate)'.

### [AMEND] R2-ASSUM-UNLABELED — ../manuscript_EN_v5.md
- **Problema:** Estimativa κ↔concentração sem rótulo de assumption: 1–1 µM....
- **Exigência:** Rotular '(illustrative; not a measured secretion estimate)'.

### [AMEND] R2-ASSUM-UNLABELED — ../manuscript_EN_v5.md
- **Problema:** Estimativa κ↔concentração sem rótulo de assumption: 1–1 µM interstitial V127ΔGPI at the deposit peak....
- **Exigência:** Rotular '(illustrative; not a measured secretion estimate)'.

### [AMEND] R2-ASSUM-UNLABELED — ../manuscript_EN_v5.md
- **Problema:** Estimativa κ↔concentração sem rótulo de assumption: 1–1 µM (c(1mm)≈0....
- **Exigência:** Rotular '(illustrative; not a measured secretion estimate)'.

### [AMEND] R2-PT-MISSING — ..
- **Problema:** Companion PT sem claim-tags (paridade declarada como passo futuro).
- **Exigência:** Gerar manuscript_PT_v5.md com as mesmas tags.

### [AMEND] R2-ASSUM-UNLABELED — ../manuscript_EN_v5.md
- **Problema:** Estimativa κ↔concentração sem rótulo de assumption: 8 µM; across the plausible secretion range this spans ≈0....
- **Exigência:** Rotular '(illustrative; not a measured secretion estimate)'.

### [AMEND] R2-ASSUM-UNLABELED — ../manuscript_EN_v5.md
- **Problema:** Estimativa κ↔concentração sem rótulo de assumption: 1–1 µM....
- **Exigência:** Rotular '(illustrative; not a measured secretion estimate)'.

### [AMEND] R2-ASSUM-UNLABELED — ../manuscript_EN_v5.md
- **Problema:** Estimativa κ↔concentração sem rótulo de assumption: 1–1 µM interstitial V127ΔGPI at the deposit peak....
- **Exigência:** Rotular '(illustrative; not a measured secretion estimate)'.

### [AMEND] R2-ASSUM-UNLABELED — ../manuscript_EN_v5.md
- **Problema:** Estimativa κ↔concentração sem rótulo de assumption: 1–1 µM (c(1mm)≈0....
- **Exigência:** Rotular '(illustrative; not a measured secretion estimate)'.

### [AMEND] R2-PT-MISSING — ..
- **Problema:** Companion PT sem claim-tags (paridade declarada como passo futuro).
- **Exigência:** Gerar manuscript_PT_v5.md com as mesmas tags.

### [AMEND] R3-R3-BLIND — manuscript
- **Problema:** Interrogação epistêmica R3-BLIND: procedimento ausente.
- **Exigência:** Cegamento do avaliador e randomização de organoides por lote declarados.

### [AMEND] R3-R3-PREPRINT-DEP — manuscript
- **Problema:** Interrogação epistêmica R3-PREPRINT-DEP: procedimento ausente.
- **Exigência:** Dependência das âncoras centrais em 2 preprints não revisados (E003/E004) declarada explicitamente.

### [AMEND] R3-R3-CONJ-RISK — manuscript
- **Problema:** Interrogação epistêmica R3-CONJ-RISK: procedimento ausente.
- **Exigência:** Risco lógico do argumento regulatório: precedente para cada pilar ≠ precedente para a conjunção.

### [AMEND] R3-R3-SEARCHLOG — manuscript
- **Problema:** Interrogação epistêmica R3-SEARCHLOG: procedimento ausente.
- **Exigência:** Reprodutibilidade da auditoria: onde estão as ~90 queries arquivadas?

### [AMEND] R3-R3-SENS-SWEEP — manuscript
- **Problema:** Interrogação epistêmica R3-SENS-SWEEP: procedimento ausente.
- **Exigência:** Sensibilidades estruturais pendentes: expoente do freeS (1 vs 2) e C50 sweep sobre θ*.

### [AMEND] R3-R3-REDOSE-IMMUN — manuscript
- **Problema:** Interrogação epistêmica R3-REDOSE-IMMUN: procedimento ausente.
- **Exigência:** Imunogenicidade da redose repetida (LNP/anti-PEG, via intratecal) discutida.

### [NOTE] R0-UNUSED — ../manuscript_EN_v5.md
- **Problema:** Claims registradas mas não citadas no manuscrito: C001, C006, C009, C016, C021, C023.
- **Exigência:** Confirmar que são intencional (claims de outline/suplemento).

### [NOTE] R1-BATTERY-factual — claims
- **Problema:** Bateria hostil aplicada a 26 claims factual: Status de revisão por pares da fonte? (preprint ≠ revisado — rotular) | Fonte única ou corroboração independente? | Transferência de espécie/modelo → humano declarada? (IDs: C002, C003, C004, C005, C007, C008, C010, C011, C012, C013, C014, C017, C018, C019, C020, C022, C024, C025, C026, C027, C028, C029, C030, C031, C040, C041)
- **Exigência:** Cada pergunta deve ter resposta no texto/manifesto; sem resposta → limitação.

### [NOTE] R1-BATTERY-method — claims
- **Problema:** Bateria hostil aplicada a 4 claims method: Self-test executado e arquivado? | Critérios de aceitação especificados ANTES do resultado? | Código+params arquivados no repo? (IDs: C015, C043, C044, C045)
- **Exigência:** Cada pergunta deve ter resposta no texto/manifesto; sem resposta → limitação.

### [NOTE] R1-BATTERY-result — claims
- **Problema:** Bateria hostil aplicada a 9 claims result: Pre-registrado ou post-hoc? (rotular explicitamente) | Baseline e critério de comparação definidos? | Incerteza/IC reportado? (IDs: C032, C033, C034, C035, C036, C037, C038, C039, C042)
- **Exigência:** Cada pergunta deve ter resposta no texto/manifesto; sem resposta → limitação.

### [NOTE] R1-PREPRINT — manifest
- **Problema:** 2 fonte(s) preprint no manifest — o texto deve rotular status de revisão onde forem centrais.
- **Exigência:** Rotular no texto (ex.: bioRxiv preprint).
