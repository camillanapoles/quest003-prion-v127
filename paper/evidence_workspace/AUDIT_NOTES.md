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

## Re-execução independente dos sweeps v5 [SIM] (2026-08-27)
A autora re-executou a fase S1 em ambiente próprio (wall 500,5 s vs 813,9 s do run local — máquinas distintas). Comparação semântica campo a campo: **todos os valores idênticos** (exp1 k2/k4/k8 = 2.828/0.85/0.819; exp2 = 0.819/0.778/0.76; baseline 2.828 mm / 144,02 d-unid; T1 pass). Solver determinístico, port paritário entre ambientes. Arquivo arquivado como `ws_9_v5_sweeps_S1_authors_rerun.json`. Cadeia de reprodutibilidade do programa: v4 reproduzido hash-idêntico (executante humana) + v5-S1 reproduzido valor-a-valor em segundo ambiente.

## Parte 2 · 2.1 — Calibração do estimador θ_obs v1 [SIM] (2026-08-27)
Simulation-based calibration (grade κ 1.5–8; ruído organoide CV 30/40%; 1000 boots/unidade): **veredito ADEQUADO** pelos critérios pré-declarados (cobertura do θ verdadeiro 3/3; bias mediano ≤0,032). Leitura honesta: os modos de κ̂ espalham-se (ex.: κ_true=8 → 483 acertos, 252 em 1,5) — o IC unitário cobre quase toda a grade; a precisão declarada para o G0-wet é a da MEDIANA POR BRAÇO com n=8 (§2.7), e a validação do regime pooled fica como TODO pré-GATE-F (THETA-OBS-POOLED). A grade revelou ainda que a biomassa carrega a informação que o raio perde por saturação (R 0,843→0,760 vs ratio 48→1,25).

## Parte 2 · THETA-OBS-POOLED (2026-08-27)
Regime §2.7 (mediana por braço, n=8, 1000 boots): **PASS integral em κ=2** — a fronteira de decisão (θ≈0,333) é a região de melhor precisão (bias 0,008; modal 69%). κ=4 falha modal por 1 p.p.; κ=8 tem bias +0,060 **em direção conservadora** (superestima θ ⇒ subestima contenção — erro no lado seguro da predição travada). Cobertura 3/3 com IC largo (limitado à grade de 6 pontos; κ̂ por vizinho-mais-próximo quantiza). Próximo refinamento pré-GATE-F: estimador v1.1 com interpolação contínua em κ.
