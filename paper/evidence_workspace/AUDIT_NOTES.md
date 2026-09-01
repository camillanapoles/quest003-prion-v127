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
Regime §2.7 (mediana por braço, n=8, 1000 boots): **PASS integral em κ=2** — a fronteira de decisão (θ≈0,333) é a região de melhor precisão (bias −0,008; modal 69%). κ=4 falha modal por 1 p.p.; κ=8 tem bias +0,060 **em direção conservadora** (superestima θ ⇒ subestima contenção — erro no lado seguro da predição travada). Cobertura 3/3 com IC largo (limitado à grade de 6 pontos; κ̂ por vizinho-mais-próximo quantiza). Próximo refinamento pré-GATE-F: estimador v1.1 com interpolação contínua em κ.

## Parte 2 · THETA-OBS-V11 — testado e REJEITADO (2026-08-27)
Estimador interpolado (IDW-2 vizinhos) avaliado contra os mesmos critérios pré-declarados: PIORA a fronteira de decisão (κ=2: bias −0,037 vs +0,008 do NN; direção agora ANTI-conservadora) e quebra cobertura em κ=8. Conclusão epistêmica: o sinal ruidoso com grade esparsa se beneficia do NN (quantização dura) — suavização espalha probabilidade entre κs. Decisão: v1.0-NN permanece a estimadora de freeze; F1 fechado. Refinamento opcional futuro = grade mais fina (novas sims), não interpolação.

## audit_claims no manuscrito Parte 2 (perfil próprio — divergência documentada, 27/08)
Execução da ferramenta oficial sobre `manuscript_Parte2_v1.md`: 54 registradas / 11 usadas / 31 "erros". Decomposição e veredito de perfil:
1. **CLAIM_NOT_USED (43)** — semântica de registro-conjunto: o claims.csv serve às DUAS partes (C001–C051 = Parte 1; C052–C054 = Parte 2). A ferramenta não tem noção de multi-manuscrito; cada parte usa seu subconjunto. Não é lacuna.
2. **UNTAGGED_NUMERIC (30)** — anos bibliográficos na tabela de linhagem (1999–2026, já identificados por [E-ID] na mesma linha), constantes de protocolo (n=8, P0–P6, tamanhos de grade) e decimais já cobertos pelo R0/R1 do guardião com N044–N048 e adjacência de tags. O gate de registro da Parte 2 é o guardião `--profile part2` (PASS 0/0).
3. **MISSING_EVIDENCE_MARKER (1)** — não reproduzível por scan de adjacência (todos os [claim:] da Parte 2 têm [evidence:] imediato); diferença de regra da ferramenta (linha) vs perfil (cláusula).
*Veredito: impecabilidade da Parte 2 é atestada pelo seu gate de registro (guardião perfil part2, 0/0) + linhagem §1-bis; divergências da ferramenta single-manuscript documentadas aqui — mesmo padrão da Parte 1 (AUDIT_NOTES §anterior).*

## audit_claims no documento de tese EXPANDIDO (Cap.1-7; 28/08 ~11:10)

## §S3 — Proveniência e notas da colheita S3 (P-001) · 31/08→01/09
- **Execução híbrida com checkpoint**: 9/11 braços p1 computados local (Termux; phantom-killer interrompeu 3× — driver resumível por design `experiments/s3_driver.py`); restante (2 p1 + 10 p2 clock-matched + 2 H) no cloud GHA **run 33459375823** (workflow `s3-sweep.yml`; seed commitado; artifact s3-checkpoint **9783045928**). JSON final reconstruído local do checkpoint integral (finalize instantâneo, wall=0).
- **Reprodução incidental do S2** no primeiro run local abortado: c20k2 = 0.819 = valor arquivado do S2 (paridade adicional; número de log, fora dos N-fatos).
- **C0 paridade exata cross-ambiente**: baseline 2.828/144.02 (ref v4 2.83/144.02) — mesmo código, hardware diferente ⇒ determinismo atestado.
- **Limitação de domínio declarada**: escapes (N_x2, C_Kt_x2, J_KtKr_x2) saturam no canto do grid (2,83mm = hypot(48,48)/24 px→mm); R_norm nesses braços é **LIMITE INFERIOR** do raio verdadeiro. Veredito C2 não muda (critério ≥2× satisfeito por saturação); magnitude real requer grid maior.
- **Falha do passo de versionamento do workflow**: git push non-fast-forward (corrida com bot-commit do PDF) — fix aplicado: fetch+rebase antes do push.
- **Compute-matrix**: CF Workers REJEITADO p/ motor (port V8/Pyodide quebraria motor-exato/C0; limites CPU) — tokens `~/.cloudflare` reservados p/ orquestração; GPU só p/ motor v6 pós-REPARAM com parity-gate próprio; GHA = via atual (billing OK).
- **Falso-positivo conhecido R0-NBIND-N050**: o guardião flagou "245.3 aparece no texto sem marker" — verificação direta exaustiva (todas as variantes de 245.3 × 6 superfícies: EN/PT md+tex, Parte2 PT/EN) = **zero ocorrências**. Achado classificado como falso-positivo de máquina (edge de formatação float em num_variants); gate PASS mantido (AMEND≠BLOCKED; invariante zero-BLOCKED intacta). Investigação do bug = item menor, não pendência do programa.
157 'erros' da ferramenta decompostos: **UNTAGGED_NUMERIC 154** — 96 na seção REFERÊNCIAS/CONCORDÂNCIA (localizadores [n] + anos ABNT + tabela claims→refs: numéricos ESTRUTURAIS da lista, não fatos) e 58 no corpo, dos quais ≈27 são localizadores de citação [n] colados às claims tags (formato da própria skill); o restante = numerais estruturais (OE/H/Q, P0-P6, refs de figura) — cobertura real por claim/evidence tags mantida pelo gate part2 (0/0). **CLAIM_NOT_USED 37** = registro-conjunto P1+P2 (documentado). **MISSING_MARKER 3** = regra de adjacência por linha da ferramenta; scan por cláusula não reproduz (0 ocorrências). check_consistency: 16 erros UNKNOWN_SCHEMA_FIELD 'note' → campo movido p/ sidecar (nf_notes_sidecar.md), manifest 100% schema-oficial agora.
