# Evidence Bank — tese unificada (braço-B, branch writing-v2-test)

Fonte-da-verdade: registro probatório do programa (`paper/evidence_workspace/`), sincronizado com o braço-B no merge do PR #6 (m31-dose → writing-v2-test, 01/09).

## Estado do registro (pós-M3.1/U6)

| Registro | Contagem | Arquivo |
|---|---|---|
| Claims (norm→sha256) | 60 (C001–C060) | `paper/evidence_workspace/claims.csv` + `claim_texts.md` |
| Fontes verificadas | 58 (E001–E058) | `paper/evidence_workspace/source_manifest.json` |
| N-fatos | 65 (N001–N065) | `paper/evidence_workspace/consistency_manifest.json` |
| Métodos / resultados | 4 / 5 | idem |

## Blocos de evidência por capítulo (blueprints B0–B9)

| Bloco | E-IDs âncora | Claims-chave | N-fatos-chave |
|---|---|---|---|
| B0–B1 (nota-à-banca → fundamento) | E001–E008 (V127/minociclina/estruturas), E009–E011 (kernel Fornara/transporte) | C001–C015 | N001–N020 |
| B2–B3 (modelagem: solver → G0-sim) | E030 (WS-7), E032 (WS-9), E010 (Thorne), E011 | C013–C015, C032–C040 | N021–N040 |
| B4 (aplicação: desenho emerge) | E030, E032, E019 + **E057 (Chen 2010 Kd 71 nM — verificado NCBI+PMC2924066)** + **E058 (cômputo M3.1)** | C033/C038/C040/C051 + **C058–C060 (M3.1 dose-band)** | N041–N050 + **N060–N065 (MW 22,83 kDa; µg/depósito; largura ≈53×)** |
| B5 (etrização formalizada) | E030–E033 (gates/AST), E031 (Bayes) | C046, C052–C054 | N051–N055 |
| B6 (resultados-como-validação) | E032, E007, E033 (p024/θ_obs) | C038–C040, C055–C057 | N056–N059 |
| B7 (camada clínica) | E019 (LNP), E039 (turnover PrP), E034–E038 (ensaios) | C035, C036 | N-fatos clínicos |
| B8–B9 (limitações/anexos) | todos acima + citation bank (138 genuínos, stage 3) | C024 (retratado), C028 | — |

## Incremento M3.1 (U1–U6, esta sessão)

- **Cadeia A6**: κ_req → µM (banda Kd 0,071–1,0 µM; E057 + âncora ilustrativa §2.2 P1) → nmol (V-halo E030/E010) → µg/depósito (MW 22,83 kDa, E058, sequências próprias P04156 res. 23–231).
- **Banda humana (Kt 2)**: 0,0–2,6 µg/depósito · **pior caso κ=8**: 0,2–10,3 µg/depósito · redose ≤7 d.
- **A largura ≈53× é o achado** (κ cancela: 14× Kd-proxy × 3,7× V-halo) — fecha em G0-A6.
- Tier: **[SIM]-planejamento (prognóstico calculado; NÃO prescrição)** — em toda saída.
- JSON canônico: `experiments/m31/m31_u1u2.json` (+ `fig5_dose_ladder_data.json`).
