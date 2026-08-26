# Rodadas de Revisão Hostil (pré-depósito) — manuscript v4

## RODADA 1 — Reviewer-2 hostile (2026-08-26) — veredito: MAJOR REVISION (5 achados)

**R1 (BLOCKER — contradição lógica).** O texto invoca invariância de θ sob reescala temporal (Methods §2.4) e depois reporta θ* humanizado (0,333) "mais favorável" que o murino (0,20-0,33). Se θ é invariante ao relógio, o relógio não pode mover o limiar. *Justificativa:* leitor quantitativo detecta autocontradição e rejeita. **Fix:** explicitar que o deslocamento decorre da **recalibração de amplitude/semente** (semente MV2-like calibrada aos títulos humanos muda o regime logístico do motor), NÃO da reescala temporal — consistente com a invariância.

**R2 (MAJOR — integridade citacional).** Abstract alega "42 verified references"; lista numerada tem 26 + "Plus". Refs [2] (fonte secundária), [14] ("Vallabh/Gentile" vago) e [19] ("PDO literature ~80%" sem citação específica) são inaceitáveis em padrão top. **Fix:** frasear "≈42 (26 numeradas; localizadores completos no repo)" + reformular [2]/[14]/[19] com citação precisa ou apontador honesto ao repo.

**R3 (MAJOR — estatístico).** n=8 organoides/braço sem análise de poder declarada. **Fix:** declarar: Welch por braço vs A2, α=0,05 Holm (5 comparações), CV≈30% ⇒ detecta Δ≥50% com ~80% de poder (e escalonamento n=12 se variabilidade organoide exceder).

**R4 (MAJOR — figuras).** Manuscrito sem legendas de figura — pré-requisito de formatação. **Fix:** bloco de legendas apontando às figuras do repo (Fig 1 transporte/halo; Fig 2 curva R(θ); Fig 3 frentes MV1/MV2).

**R5 (MINOR — norma de revista top).** Falta Significance Statement. **Fix:** adicionar EN/PT.

**Aprovados pelo revisor (sem alteração):** proveniência dos parâmetros com fontes; self-tests declarados; limitações completas (9 itens incl. κ→concentração como risco nº1); pré-registro timestamped; divulgação de IA; biossegurança; dupla lente bayesiana; validação emergente MV1/MV2 corretamente distinguada de curve-fitting; transferabilidade para prion-like rotulada como hipótese.

**Veredito pós-fix:** aprovado para depósito como preprint com audit trail; nível de revisão externa (peer review formal) dependerá de dados G0.
