# Auditoria de Referências do Adendo Externo + Mapa de Contradições

**Data:** 2026-08-25 · **Objeto:** 15 links do documento colaborador ("Mecanismos de Defesa e Regeneração") · **Método:** verificação direta (fetch/abstract) de cada fonte

## Parte 1 — Verificação ref a ref

| # | Fonte citada | O que é de verdade | Status | Suporta o alegado? |
|---|---|---|---|---|
| 1 | PMC4486072 | Asante 2015, Nature — resistência V127 | ✅ REAL | Sim — MAS omite a nuance crítica: heterozigoto infectável por vCJD |
| 2 | cureffi.org 2015 | Blog de divulgação científica (E. Minikel) | ⚠️ Secundário | Ok como leitura; não é primária |
| 3 | PMID 26061765 | Asante 2015 — **mesma que [1]** | ✅ REAL | 🔁 DUPLICAÇÃO de [1] |
| 4 | PMC6123418 | Zheng et al. 2018, Sci Rep — base estrutural | ✅ REAL | Sim |
| 5 | s42003-020-01126-6 | Hosszu 2020, Commun Biol — dímeros estáveis + loop β2-α2 | ✅ REAL | Sim, com nuance: mecanismo é conformacional/dinâmico, não "trava mecânica rígida" |
| 6 | S0969996126002512 | Gatdula 2026 (publicação) | ✅ REAL | Sim |
| 7 | bioRxiv 703887 | Gatdula 2026 (preprint) — **mesmo estudo que [6]** | ✅ REAL | 🔁 DUPLICAÇÃO de [6] |
| 8 | PMC4601379 | Relaño-Ginés/Crozet 2014, REVIEW — título real: *"How do prions COUNTERACT the brain's endogenous repair machinery?"* | ✅ REAL | ❌ **USO ENVIESADO**: o review enfatiza que o príon SEQUESTRA o reparo; não menciona NSC→micróglia nem scaffold |
| 9 | S2213671125001377 | Stem Cell Res 2025 (paywall) — não identificada diretamente | ⚠️ NÃO VERIFICÁVEL | Claim (hidrogel carreador p/ NSC) é suportado por literatura equivalente (Chen 2023, PMC10102240) — mas a ref específica fica pendente |
| 10 | PMID 23935493 | Relaño-Ginés 2013, PLoS Pathog e1003485 (confirmado via citação em [8]) | ✅ REAL | Ver abaixo — uso invertido |
| 11 | PLoS Pathog e1003485 | **Mesma que [10]** | ✅ REAL | 🔁 DUPLICAÇÃO de [10] |
| 12 | Brain 137:2312 | Gomez-Nicola 2014 — neurogênese ↑ contrabalça | ✅ REAL | Parcial: é HIPOCAMPO, camundongo — não SVZ humano |
| 13 | PMC10834622 | Kreatsoulas/Lonser 2024 — CED em GLIOMAS | ✅ REAL | Metodologia CED sim; contexto tumoral (não príon) |
| 14 | Aetna CPB 0731 | **Política comercial de plano de saúde** | ❌ NÃO-CIENTÍFICA | Remover — não é literatura |
| 15 | thejns 143(5) | Elder/Lonser 2025, J Neurosurg — CED gene+celular | ✅ REAL | Sim — a melhor ref do conjunto |

**Escore: 11/15 reais e corretas · 1 blog · 1 não-verificável (paywall) · 1 comercial · 3 duplicações ([3]=[1], [11]=[10], [7]≈[6])** — inflação aparente de base bibliográfica: são ~10 fontes únicas, não 15.

## Parte 2 — Mapa: ideia original → o que a literatura diz → veredito

| Ideia (v0/adendo) | Literatura verificada | Veredito |
|---|---|---|
| **A. NSC gera "micróglias imunes"** | NENHUMA das 15 refs mostra isso; a própria ref [8] não contém o claim; Ginhoux 2010 (nossa tabela) proíbe a linhagem | ✕ **CONTRADIZ** — claim sem suporte nem na própria bibliografia do adendo |
| **B. "Miolo SVZ = fábrica; blindar reverte"** | [10/11] demonstram o OPOSTO do uso: príon replica no nicho e altera o destino das NSCs — risco, não cura; Sorrells 2018: SVZ humano adulto mínimo; [12]: neurogênese é no HIPOCAMPO (outra estrutura, camundongo) | ✕ **CONTRADIÇÃO INVERTIDA** — a citação usada como ref de cura demonstra a ameaça + mapeamento anatômico errado |
| **C. "Inundar o interstício com G127V"** (como PrP de membrana) | [1] Asante: PrP ancorado, expresso na célula; o mecanismo de inundação real é o ANCHORLESS de [6/7] Gatdula — que o adendo cita mas NÃO conecta ao claim | ⚠️ **INCONSISTÊNCIA INTERNA** — as duas metades da bibliografia apontam mecanismos diferentes; só ΔGPI sustenta "inundação" |
| **D. Hidrogel: trava células em ms + scaffold de reconexão** | [9] pendente; Chen 2023 suporta hidrogel como carreador que AUMENTA sobrevida de NSC; "gelificação em ms" não aparece em nenhuma fonte | ⚠️ **SUPORTE PARCIAL INDIRETO** + contradição de projeto: gel que retém célula pode reter a V127ΔGPI secretada (→WS-7) |
| **E. PG exponencial (2^n) vs migração linear (mm/dia)** | Assimetria qualitativamente correta; 2^n é upper bound (in vivo há saturação por substrato) | ✅ **VÁLIDO COM NUANCE** |
| **F. CED pela rota do tecido necrosado** | [13][15] validam CED como técnica; nenhuma ref cobre CED em meio espongiforme degradado (κ heterogênea → fluxos preferenciais — risco que o próprio doc #1 do colaborador levantou) | ⚠️ **TÉCNICA SIM, MEIO NÃO TESTADO** |
| **G. Uso compassivo N-of-1 como rota principal** | PRN100 (seguro, sem eficácia) + aritmética de janela da esporádica | ✕ **CONTRADIZ o otimismo** — persiste do v0 |

## Parte 3 — O que sobrevive da ideia original (síntese honesta)

**Sobreviveu à verificação:** escudo V127 (refs 1,3,4,5,6,7 — núcleo sólido) · contenção trans via anchorless (6,7) · CED como vetor (13,15) · eixo regenerativo endógeno (12 + Jalland/De Lucia nossos) · hidrogel-carreador em princípio (9-equivalente).
**Caiu ou exige reforma:** micróglia-de-NSC (A) · fábrica SVZ/blindagem-reverte (B) · inundação por PrP de membrana (C) · gel ms + scaffold literal (D) · N-of-1 como rota principal (G).

## Recomendações ao colaborador
1. Desduplicar a bibliografia (10 fontes únicas, não 15) e remover a Aetna (política comercial).
2. Explicitar V127ΔGPI (sem âncora) em TODO claim de efeito intersticial.
3. Corrigir o uso de Relaño-Ginés (2013 e review 2014): citar como **motivação do risco do nicho**, não como suporte de cura.
4. Reancorar regeneração no hipocampo/neurogênese endógena (Gomez-Nicola/Jalland), não no SVZ.
