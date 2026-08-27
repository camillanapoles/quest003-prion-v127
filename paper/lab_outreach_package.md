# Pacote de Contato — Laboratórios Parceiros para o Gate G0
## Quest 003 · v2.1 · 2026-08-27 · USO: envio LIBERADO (decisão da autora 27/08: sem DOI — release v3.0 é a fonte citável; bioRxiv DOI será adicionado como adendo quando depositado, sem impacto no conteúdo)

**Novo na v2:** manuscrito v5 bilíngue (EN+PT, claim-audited) · gate computacional G0-sim EXECUTADO e re-produzido em 2 ambientes (hash-idêntico + valor-a-valor) · colheita de sensibilidade com PREDIÇÃO DISCRIMINADORA para o braço A6 (a dose-resposta distingue heterodímero vs dois-eventos: unidade inibitória molecular) · dossier de liberação científica pronto (G0_UNLOCK_DOSSIER.md) · estimador θ_obs operacional pré-especificado (anti-circularidade)

---

## Email técnico (1 página — adaptar nome do grupo em [colchetes])

**Assunto:** Partnership inquiry — anchorless PrP-V127 antiprion vectors in sCJD-infected human organoids (preprint + pre-registered protocol)

Dear Dr. [Caughey / Williams / Okamoto / Martins],

We are an open-science research consortium that has completed a structured preclinical program on the therapeutic use of the kuru-protective PrP-V127 variant for Creutzfeldt-Jakob disease. Our preprint (attached; deposited open-source with full audit trail at github.com/camillanapoles/quest003-prion-v127, release v3.0; bioRxiv DOI to follow as addendum) integrates three components your group is uniquely positioned to test:

**1. The agents.** Based on the 2026 demonstrations that recombinant anchorless V127 retains potent dominant-negative activity in trans (Gatdula et al.) and that AAV-delivered V127ΔGPI extends survival in vivo (Zerbes et al.), we specified three delivery vectors for the anchorless agent: CRISPR-edited secretory neural progenitors, recombinant protein, and intrathecal LNP-mRNA.

**2. The pre-registered organoid assay (G0).** Built directly on your group's platform [Groveman 2019/2021 — infected organoids; PPS screening | Williams 2023 — NPC seeding], it asks one question: does anchorless V127 generate a proximal-to-distal PrP-res containment gradient? Eight arms (n=8), including pentosan polysulfate as published positive control; kill-switches pre-registered, including pivot-to-acellular if protein matches cells. Full protocol attached.

**3. Quantitative predictions to falsify — now including a discriminating one.** Our self-tested transport model (mass-conservation 100%, Thiele-length 0.5% vs analytic) predicts a 4-6 mm protection radius per deposit and a containment threshold θ*=0.333 under a humanized clock. The in-silico gate (G0-sim) is executed, machine-audited and independently re-executed with identical values; sensitivity harvest shows the threshold is robust to C50 over a tenfold range but *discriminates the functional form*: under a first-power inhibition term, containment shifts from kappa 2 to 4 — so the arm-A6 dose-response curve can distinguish the molecular inhibitory unit (heterodimer vs two independent events). The result is informative in every direction, including negative.

A Bayesian success model calibrated on historical analogs (all six clinical failures now registry-bound with verified identifiers) places P(GO) at ~37% — we are asking you to help run an experiment we honestly expect to fail 6 times out of 10, because it is the cheapest decisive measurement in the field. A committee-facing unlock dossier (validity basis, guarantees, declared scope) and the pre-specified θ_obs estimator (blinded scorer, pre-committed grid and objective) are attached — the assay arrives pre-registered against circularity.

We seek: [your organoid+BSL-3 infrastructure | your NPC expertise] for a ~10-month, 8-arm assay (estimated reagents+staffing USD 60-160k; we are preparing FAPESP/CNPq applications and welcome co-application with your institution). All materials, protocols, analysis code and the full audit trail (git-versioned) are available; we propose co-authorship per ICMJE and open publication of results regardless of direction.

We would welcome a 30-minute call at your convenience.

Respectfully,
[Nome do corresponding author] — Consórcio de Investigação em Príons e Engenharia Molecular

---

## Destinatários-alvo (ordem de prioridade)

| # | Grupo | Por quê | O que pedir |
|---|---|---|---|
| 1 | **Byron Caughey / Bradley Groveman** — Rocky Mountain Labs (NIH/NIAID) | Donos do modelo organoide-príon E do screening (Groveman 2019/2021); já trataram organoide infectado com PPS | Executar G0 completo (8 braços) como colaboração |
| 2 | **K. Williams / grupo Calgary** | Donos do braço celular (NPCs em organoide CJD) | Braço A5 (secretora) — expertise única em semeadura celular |
| 3 | **HUG-CELL (USP) + grupo príons HC-FMUSP (Smid)** | Infraestrutura nacional (GMP iPSC, E200K clínico); executa sob colaboração internacional | Hub BR: fabricação celular (A5) + coorte E200K futura |
| 4 | Grupo de organoides com LNP-mRNA publicado (ex.: laboratório Xue-afins) | Braço A7 (mRNA) | Parceria de vetor para A7 |

## Anexos do pacote
1. `manuscript_v5_EN.pdf` + `manuscript_v5_PT.pdf` (v5, claim-audited, bilíngue; após depósito bioRxiv, citar DOI)
2. `experiments/g0_protocol.md` (protocolo completo 8 braços)
3. `paper/G0_UNLOCK_DOSSIER.md` (dossier de liberação: base de validade + garantias ao comitê + escopo declarado)
4. `experiments/ws_7_transport.md` + `experiments/ws_9_results/ws_9_v5_sweeps_*.json` (transporte + colheita de sensibilidade com a predição discriminadora A6)
5. `analysis/bayes_analogia.md` (frame probabilístico pré-registrado; falhas históricas registry-bound E034-E038)
6. Link do repo/git (audit trail: 38 fontes · 51 claims · guardião R0-R3 · release v1.0 trava as predições) — sob acordo de colaboração

## Regras do envio
- [v2.1] Envio liberado SEM DOI (decisão da autora): prioridade intelectual protegida pelo release público timestamped v3.0 (predições travadas desde v1.0); bioRxiv vira adendo
- Um email por vez (personalizar [colchetes]); aguardar 2 semanas antes de follow-up
- Oferecer call de 30 min; nunca anexar dados brutos do repo antes de acordo
- IP: desenho e predições já timestampados em git público do consórcio; formalizar MTA/acordo de colaboração antes de qualquer material biológico
