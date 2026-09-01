# M3.1 — PLANO DA NOVA SESSÃO (handoff) · ordem-de-skills da autora
## Sessão 2 de M3.1 (a "primeira dose calculada") · preparado 01/09 · ler ANTES de agir

## §0 · MEMÓRIA-DE-RETORNO (ler nesta ordem na nova sessão)
1. `guardian.md` (topo: decálogo + últimos /RECAPs) — regras vivas
2. `PENDENCIAS.md` — ledger garantista (P-029/P-030)
3. `experiments/m31/m31_protocolo_garantista.md` — o RELATE pré-registrado (critérios de aceitação U1-U7)
4. `experiments/m31/m31_u1u2.json` — o que JÁ foi computado (U1+U2: MW=22,83 kDa; cadeia κ→µM→µg/depósito por banda-Kt)
5. Branches: `m31-dose` (ciência nova; @67e06ae) · `writing-v2-test` (PaperSpine braço-B; stages 1-6 done; @67298b2) · `main` (canônico, CI verde)
6. Skill-alvo da sessão: **/skill:scientific-writing** (contém o AST que aplicamos: claims-hash, binding, validadores, gates) — e SÓ DEPOIS retomar **paper-spine** (Stage 6-writing→7→8→12)

## §1 · POR QUE ESTA ORDEM (decisão da autora — registrar o racional)
O M3.1 nasceu sob scientific-critical-thinking (avaliação/método garantista pré-registrado). A **continuidade metodológica** agora exige o pipeline probatório da casa — que VIVE na skill scientific-writing (norm→sha256 das claims, evidence-binding, validate_manifest/check_consistency/check_references, guardian R0-R3, AST A2-A9) — **antes** de qualquer texto entrar na tese unificada (paper-spine). Fluxo: **dado-JSON → registro-claims → gates → só então escrita** (paper-spine consome material já-gated).

## §2 · EXECUÇÃO DA NOVA SESSÃO (U5→U7 pela ordem)
1. **U5 — Figura 5** (escada de dose: banda µg/depósito × banda-Kt, pior-caso κ=8 destacado; matplotlib no CI como a Fig.4 — script `experiments/m31/make_fig5_doseladder.py` lendo `m31_u1u2.json`).
2. **U6 — pipeline scientific-writing**: claims C058-C060 (dose-banda A6; escada κ↔Kt→µg; largura-da-banda=achado) com **norm→sha256** em claims.csv + claim_texts.md; N-fatos N060+ (µg/depósito por banda, MW 22,83, largura 2-ordens); validadores 0/0; **guardian gates + AST 8/8** (A9 ledger).
3. **U7 — integração**: PR `m31-dose`→`writing-v2-test` alimentando o **B4** (blueprint "aplicação: o desenho emerge") + Fig.5 + tabela de validação M3→M2; depois **retomar paper-spine**: Stage 6-writing (draft da tese unificada com M3.1 no miolo) → Stage 7 integridade → Stage 8 LaTeX/PDF/Word (coluna única justificada) → Stage 12 final-audit (contribution/results-validation/reviewer-audit checks).
4. **Fechamento**: /RECAP + ledger (P-030→FECHADA quando U7 integrar) + avaliação A-vs-B do braço de escrita (WRITING_V2_PROTOCOLO) — **decisão de adoção = autora**.

## §3 · INVARIANTES (não renegociáveis na sessão 2)
Predições v1.0 comparadas-jamais-retreinadas · número só de JSON/registro · banda≠ponto (a largura da banda É o achado até G0-A6) · tier [SIM]-planejamento em toda saída (nunca prescrição) · gates sem isenção · anti-hindsight (cronologia M2-antes-de-M3 declarada) · merge só via PR com CI.

## §4 · ESTADO ATUAL RESUMIDO (para conferência rápida)
U1 ✓ (mapa dimensional banda-GUM) · U2 ✓ (MW 22,83 kDa das sequências próprias) · cadeia A6 computada por banda-Kt (0,03-2,6 µg/depósito na banda humana; pior-caso 0,2-10,3) · redose ≤7d · FALTA: U5 figura, U6 registro probatório, U7 integração-escrita. PaperSpine: stages 1-6 ✓ (motivação M4-da-autora; blueprints B0-B9; matrix R0-R9); próximos 6-writing→8→12.
