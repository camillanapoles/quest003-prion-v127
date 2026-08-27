# Partner Selection Log — execução do protocolo 2.5 (PRISMA-análogo)
## v0.1 · 2026-08-27 · executor: agente (guardian-gated) · registro por commit (PROSPERO-análogo)

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

## 4. Decisões desta rodada
1. **Contato 1º: RML-NIH** (kit #1 pronto — outreach_email_1_groveman.txt).
2. **Contato 2º: Calgary** — kit a personalizar com JCI 2026 (novo no mapa; atualizar E-registry? JCI 2026 = candidato a E039 **se** usado como evidência; por ora, registro no log apenas).
3. UTHealth → lista técnica (assay readout); Nihat → watchlist; USP → verificação I1 documental no primeiro contato.
4. {{TODO:Q3-Q5-EXEC:executar queries restantes + PubMed direto}}; {{TODO:PUBMED-DIRECT:conformidade plena das contagens}}.

## 5. Diagrama (regenerado do log — v0.1)
```
identificados(5) → dedup(5) → triagem: passam(2)+condicional(1)+excluídos(2, motivo I1)
→ pontuação parcial → contato sequencial: próximo = RML-NIH (1º)
```
