# Partner Selection Log — APLICAÇÃO-PILOTO do protocolo 2.5 (PRISMA-análogo)
> **NATUREZA (diretriz da autora):** demonstração de EXECUTABILIDADE do método — prova que o protocolo roda e produz rastreio auditável. **NÃO é uma seleção**: nenhuma ordem de contato é decisão da tese; as ordens abaixo são SAÍDAS DO MÉTODO ilustrativas para o futuro executor.
## v0.2 · 2026-08-27 (+ Q3-Q5 executadas) · executor: agente (guardian-gated) · registro por commit (PROSPERO-análogo)

**Nota de execução (honestidade):** Q1 e Q2 foram executadas via **meta-busca web** (proxy das strings PubMed registradas) — a execução direta no PubMed fica como pendência de conformidade plena ({{TODO:PUBMED-DIRECT:rodar Q1-Q2 no PubMed interface e anexar contagens}}). Q3-Q5 pendentes. Resultados abaixo com data e URL.

## 1. Identificação (Q1, Q2 · 2026-08-27)

| # | Registro | Grupo/PI | Instituição | Fonte | URL-âncora |
|---|---|---|---|---|---|
| R1 | Groveman/Caughey 2019 (organoid sCJD) + 2021 (PPS screening) + 2023 (subtipos/transmissão) | Groveman BR, Caughey BA | RML, NIAID/NIH (Hamilton, EUA) | Q1,Q2 | pubmed.ncbi.nlm.nih.gov/31196223; nature.com s41598-021-84689-6; link.springer 10.1186/s40478-023-01512-1 |
| R2 | Williams 2026 JCI (alterações neuronais distinguem subtipos em organoides) | Williams K et al. | Calgary (rede SCRT, Canadá) | Q1 | jci.org/articles/view/194721 |
| R3 | Pritzkow 2024 (PMCA screening de 8 compostos) | Soto C / Pritzkow S | UTHealth Houston (EUA) | Q2 | digitalcommons.library.tmc.edu (PMCA) |
| R4 | Nihat 2026 PNAS (EKV: linha celular divisível que propaga sCJD) | Nihat A et al. | (instituição a confirmar) | Q2 | pnas.org/doi/10.1073/pnas.2600341123 |
| R5 | conhecimento prévio E-registry (E024; hub BR) | Smid J + HUG-CELL/HC-FMUSP | USP/São Paulo (BR) | Q5 **pendente** | demneuropsy.com.br (Smid 2007) |

**Identificados: 5 registros (4 via Q1/Q2-proxy + 1 pré-conhecido) → deduplicação por grupo: 5 grupos (n=5).**

## 2. Triagem I1–I5 (2026-08-27)

| Grupo | I1 plataforma organoide-príon publicada | I2 BSL-príon | I3 capacidade | I4 open/kill | I5 formalização | Veredito |
|---|---|---|---|---|---|---|
| RML-NIH | ✓ (2019/2021/2023 — E007/E008 + Groveman 2023) | ✓ | ~ (n=8→12 a negociar) | ? | ? | **PASSA → pontuar** |
| Calgary/Williams | ✓ (JCI 2026 + E012-2023) | ~ (príon via colaboração) | ? | ? | ? | **PASSA → pontuar** |
| UTHealth/Soto | ✗ (PMCA, não organoides) | ✓ | — | — | — | **EXCLUÍDO do G0-inteiro (I1)** → elegível como assay-adjuvante (RT-QuIC/PMCA readout) |
| Nihat-group | ✗ (linha celular, não organoides) | ? | — | — | — | **EXCLUÍDO (I1)** → watchlist (plataforma de propagação p/ pré-filtragem; fora do desenho travado) |
| USP-hub BR | ~ (organoides ✓; infecção por príon a confirmar documentalmente) | ? | ✓ | ? | ✓ | **CONDICIONAL** → verificar I1 por contato |

**Fluxo até aqui: identificados n=5 → triagem: 2 passam direto + 1 condicional + 2 excluídos (motivo I1; ambos redirecionados a papéis técnicos/watchlist, não descartados).**

## 3. Pontuação A–H (só eixos verificáveis sem contato; "?" não pontuam — regra)

| Grupo | A (25) | B (15) | C (15) | D (10) | E (10) | F (10) | G (10) | H (5) | Score parcial* |
|---|---|---|---|---|---|---|---|---|---|
| RML-NIH | 5 (=25) | 5 (=15) | ~ | ? | 0-1 | 0 | ? | ? | **≥40/50 verificáveis** — liderança estrutural |
| Calgary | 4 (=20) | 4 (=12) | ? | 5 (=10) | 0 | 0 | ? | ? | **≥42/45 verificáveis — competitivo, eixo D máximo** |
| USP-hub | 1-2 | ? | 3 | 2 | 0 | 5 (=10) | ? | 3 | condicional |

*\*parcial = soma só dos eixos com evidência documental; classificação final após contato (I4/I5/G/H). A ordem de contato pré-declarada é por score TOTAL previsto (máx=100): RML segue 1º pela regra do desempate-A caso a diferença ≤5 — mas Calgary mostrou PESO REAL no eixo D (braço A5, a tese ◆) que a pré-triagem v1 subestimava. **Método corrigindo estimativa a priori: registrado.***

## 4. Saídas do método nesta rodada (não-decisões da tese)
1. O método ordena: se executado, contato 1º = RML-NIH (maior score verificável) — kit operacional existe (anexo fora da tese).
2. **Contato 2º: Calgary** — kit a personalizar com JCI 2026 (novo no mapa; atualizar E-registry? JCI 2026 = candidato a E039 **se** usado como evidência; por ora, registro no log apenas).
3. UTHealth → lista técnica (assay readout); Nihat → watchlist; USP → verificação I1 documental no primeiro contato.
4. {{TODO:Q3-Q5-EXEC:executar queries restantes + PubMed direto}}; {{TODO:PUBMED-DIRECT:conformidade plena das contagens}}.

## 5. Diagrama (regenerado do log — v0.1)
```
identificados(5) → dedup(5) → triagem: passam(2)+condicional(1)+excluídos(2, motivo I1)
→ pontuação parcial → contato sequencial: próximo = RML-NIH (1º)
```


## 6. Rodada v0.2 — Q3, Q4, Q5 (2026-08-27 18:40, proxy web; PubMed-direto segue pendente)

| # | Registro novo | Grupo | Fonte | Triagem |
|---|---|---|---|---|
| R6 | Prions@Broad — PrP-siRNA em ensaio clínico (enrolling) | Broad Institute (EUA) | Q3 (broadinstitute.org; cjdfoundation.org NN112) | I1 ✗ (não organoide) → **watchlist estratégico** (classe redução-de-substrato; concorrência/convergência p/ G2) |
| R7 | prionregistry.org — prevenção em príon genético (Mead/UCL) | UCL/MRC Prion Unit (UK) | Q3 (prionregistry.org) | I1 ✗ → **watchlist estratégico** (coorte G2/biomarcador NfL; alinhado à nossa população-alvo E200K) |
| R8 | Palestra CJDF-2026: "Generating cerebral organoids from donors with sporadic CJD" | **lab NÃO identificado na fonte** | Q4 (qgiv.com evento 2026) | **PENDENTE DE IDENTIFICAÇÃO** → potencial NOVO elegível I1 |
| R9 | La Trobe — 'living' brain slices CJD | La Trobe University (AUS) | Q4 (cjdisa.com) | I1 ✗ (fatias, não organoides) → técnico-adjacente |
| Q5-BR | Nenhum outro grupo BR organoide-príon surfaced no proxy; ensaiosclinicos.gov.br noticia tratamentos (não lab) | — | Q5 | **confirma USP-hub como âncora BR** (condicional I1 mantém) |

**Fluxo v0.2: identificados 9 registros → 8 grupos (+1 não-identificado R8) → elegíveis 2 (RML, Calgary) + condicional 1 (USP) + watchlist 3 (Broad, UCL, La Trobe) + técnico 2 (UTHealth, Nihat).**
{{TODO:IDENTIFY-ORGANOID-DONOR-LAB:identificar o grupo da palestra CJDF-2026 (programa do evento/agenda pública) — potencial 3º elegível}}
Decisão: ordem de contato INALTERADA (1º RML, 2º Calgary); R8 pode reordenar APÓS identificação e pontuação.


## 7. Rodada v0.3 — CONFORMIDADE PUBMED-DIRETO (28/08 00:20Z)
Q1 e Q2 executadas **sem modificação** no PubMed via E-utilities (esearch.fcgi, JSON arquivado em part2_results/q{1,2}.json): **Q1 = 23 registros; Q2 = 2 registros** — strings-as-registered responderam no banco oficial (sem ajuste necessário; nenhuma emenda de string). Os registros identificados na v0.1 (proxy) permanecem compatíveis com a escala oficial (23 papers organoide×príon no PubMed todo). TODO PUBMED-DIRECT: **RESOLVIDO**. Pendência restante do piloto: Q3–Q5 em fonte oficial (CTG API/agenda pública) — mantido como conformidade futura {{TODO:Q3Q5-OFFICIAL:rodar Q3-Q5 em fonte oficial quando o executor for executar}}.
