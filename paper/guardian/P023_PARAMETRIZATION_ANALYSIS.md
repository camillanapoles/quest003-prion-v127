# P-023 ANÁLISE DE PARAMETRIZAÇÃO — características dos experimentos/animais × dados resultantes, por espécie
## PLAN_DOC · 01/09 · Skills: scientific-critical-thinking (auditoria) + scikit-bio/biopython (cômputo) + analista de dados/ML · Parceiro do S3_DATA_AUDIT_CRITICA.md
**Fontes computacionais (número só de JSON):** `experiments/xspecies/{prnp_sequences, prnp_identity_matrix, prnp_key_positions, prnp_region_analysis}.json` + proveniência PubMed verificada em `papers_batch{1,2,3}.txt`. Datamol avaliado e **fora de escopo** (química de pequenas moléculas; objeto aqui é proteína/sequência → scikit-bio/biopython).

---

## §1 · PROVENIÊNCIA VERIFICADA (identifier de fonte aberta — esearch/esummary E-utilities)

| ID | Ano | Veículo | Título (verificado) | Papel aqui |
|---|---|---|---|---|
| 26061765 | 2015 | Nature | A naturally occurring variant of the human prion protein completely prevents prion disease | G127V/DN (E001-família) |
| 19923577 | 2009 | NEJM | A novel protective prion protein variant that colocalizes with kuru exposure | descoberta G127V |
| 7553876 | 1995 | Cell | Prion propagation in mice expressing human and chimeric PrP transgenes | barreira hamster↔mouse; chimeras |
| 18775309 | 2008 | Cell | Crossing the species barrier by PrP(Sc) replication in vitro… | PMCA cross-species |
| 18769716 | 2008 | PLoS Pathog | Accelerated high fidelity prion amplification within and across species | PMCA taxas |
| 19193264 | 2009 | EID | Characteristics of 263K scrapie agent in multiple hamster species | cinética 263K hamster |
| 2138656 | 1990 | J Infect Dis | Organ-specific modification of the dose-response… | dose-resposta hamster |
| 39255320 | 2024 | PLoS Pathog | The molecular determinants of a universal prion acceptor | vole aceitador universal |
| 41559809 | 2026 | Acta Neuropathol | Overexpression of bank vole PrP(I109) in mice induces spontaneous atypical disease | vole I109; expressão |
| 36511154 | 2023 | J Neurochem | A single protective polymorphism blocks cross-species… | polimorfismo protetor |
| 42189860 | 2026 | PLoS Pathog | PrP turnover in vivo and time to effect of therapeutics | half-life (E039-cand.) |
| 39717079 | 2024 | iScience | The dynamics of prion spreading is governed by the interplay… | kernel (E009-família) |
| 24430187 | 2014 | J Clin Invest | Prion disease tempo determined by host-dependent substrate reduction | [PrP^C]₀ ↔ tempo |
| 22869728 | 2012 | PNAS | Overexpression of Hspa13 reduces incubation | moduladores hospedeiro |
| 39565640 | 2024 | Biochemistry | Rigidifying the β2-α2 loop slows down formation | rigidez loop ↔ cinética |
| 30592012 | 2019 | Mol Neurobiol | Bidirectional properties of the sheep-deer prion transmission | loop/barreira bidirecional |
| 23746351 | 2013 | Mol Cell | Structural definition is important for propagation of yeast [PSI+] | DN trans em levedura |
| 27259989 | 2017 | Mol Neurobiol | PMCA cross-species products of mouse→hamster | produtos cross-species |

## §2 · RESULTADOS COMPUTACIONAIS (destes dados, agora)

**Matriz de identidade global (BLOSUM62, alinhamento global, % colunas idênticas):**

| | human | mouse | hamster | vole | rat |
|---|---|---|---|---|---|
| human | — | 89,0 | 89,4 | 89,0 | 89,4 |
| mouse | | — | 93,7 | 94,1 | **96,5** |
| hamster | | | — | 94,9 | 94,1 |
| vole | | | | — | 94,9 |

**Posições-chave (homólogos ao humano):** G127 = **G em todas as espécies** (conservado); homólogo do 129 = **M em todos os roedores** (vole incluído — consistente com o fenótipo aceitador universal tipo-129M [39255320]).
**Regiões:** 125-132 = **LGGYMLGS 100% conservada em todas** (o bolso estrutural do G127 é portável); **loop β2-α2 (165-175) = 73-82% local vs 89-90% global — hotspot de divergência**.

## §3 · A CORRELAÇÃO POR ESPÉCIE (a resposta direta — forte vs fraca)

**Claim central (evidenciada):** *A correlação entre sequência global e escala cinética é FRACA/AUSENTE; a correlação relevante é LOCAL (loop β2-α2) e CONTEXTUAL (nível de expressão, ensaio, estirme/passage).*

| Evidência | Dado | Interpretação |
|---|---|---|
| **Experimento natural mouse↔rat** | 96,5% de identidade, susceptibilidade OPOSTA (rato resistente à maioria das estirmes de scrapie que matam camundongo) | identidade global NÃO prediz cinética — o preditor não pode ser global |
| **Banda plana humano×roedores** | 89,0-89,4% (espalhamento 0,4 p.p.) vs cinética diferindo por ordens de grandeza (263K-hamster dias-semanas [19193264]; vole aceita humano prontamente [39255320]) | sem variância ⇒ sem poder preditivo |
| **Hotspot local** | loop 165-175: 73-82% local, e rigidez do loop CAUSA lentidão de formação [39565640; 30592012] | a divergência cinética mora no loop — candidato a feature forte |
| **Expressão ↔ tempo** | "tempo determinado por redução de substrato hospedeiro-dependente" [24430187]; Hspa13 modula incubação [22869728]; vole I109 superexpresso → doença espontânea [41559809] | [PrP^C]₀ é correlacionador FORTE (não-sequência) |
| **Bolso G127 portável** | 125-132 100% conservado + G127/M129-homólogo universais | o mecanismo DN-V127 transfere estruturalmente (suporte à tese) |

**Correlação com a decomposição S3 (E-S3-03):** o que governa contenção é Kt-scale; as features FORTEMENTE correlacionadas a Kt-scale por espécie são, nesta análise: classe de rigidez do loop β2-α2 [39565640], nível de expressão [24430187, 41559809], e contexto de ensaio (PMCA vs in vivo vs passagem [18769716, 7553876]). FRACO: identidade global (estes dados). INDETERMINADO com n=5: efeito isolado de cada resíduo — só banda ordinal é defensável.

## §4 · POR ESPÉCIE (paper → achado → ação)

| Espécie | Papers-base | Achado detalhado | Ação P-023 |
|---|---|---|---|
| **Camundongo** | 39717079; 42189860; 24430187 | kernel completo; half-life 5-6d; expressão↔tempo causal | referência (Kt=1,0 por definição); registrar D_eff Thorne no params.json |
| **Humano** | 26061765; 19923577; 42189860; 24430187 | relógio organoide; G127V portátil (bolso 100% conservado); taxas relativas inexistentes | banda ×{0,5,1,2} herdada do envelope S3 (audit E-S3-02); âncora de relógio Groveman |
| **Hamster** | 19193264; 2138656; 18775309; 27259989 | 263K multi-espécime (incubação + dose-resposta + passage); barreira via chimeras [7553876]; produtos PMCA [27259989] | extrair Kt-scale ORDINAL (≈"rápido") com IC por dose-resposta; **predição pré-registrada: Kt≥2× ⇒ κ=2 falha** |
| **Bank vole** | 39255320; 41559809; 36511154 | aceitador universal; M129-homólogo (nosso dado); I109-spontâneo; polimorfismo protetor bloqueia cross-species | Kt-scale banda alta p/ estirmes humanas + flag "expressão-dependente" [41559809] |
| **Rato** | (experimento natural §3) | resistente com 96,5% id. mouse | outlier NEGATIVO declarado: não modelar como taxa≈0 (barreira de entrada ≠ taxa lenta) — usar como controle de não-identificabilidade |
| **Levedura** | 23746351 | DN trans depende de definição estrutural | validação ortogonal do termo freeS apenas; sem Damköhler |

## §5 · METODOLOGIA EXPLICATIVA (analista de dados/ML — a realizar no P-024)

1. **Matriz feature-disponibilidade** por espécie (loop-class, 129-state, expressão, half-life, D_eff, assay-type, passage-history) — células com ref ou vazias; célula sem ref = feature ausente (nunca imputada).
2. **Alvo:** Kt-scale como **banda ordinal** {lenta≈0,5 · ref=1 · rápida≈2 · extrema≥4} — SEM regressão (n=5): análise de consistência de ranks + **LOSO** (deixar-uma-espécie-fora) sobre o rank predito pelas features fortes.
3. **Validação pré-registrada:** predição do hamster (Kt≥2× ⇒ κ=2 falha no braço hamster do P-024) — comparada ao release, nunca retreinada.
4. **Inferência sob censura:** escapes = flag (audit E-S3-01); métrica ordinal "contém/não-contém/indeterminado(censurado)".
5. **Saída ML honesta:** mapa de calor feature×espécie + rank observado vs rank das features + IC por banda; claims condicionais rotulados [SIM].

## §6 · AGRUPAMENTO (parametrização ideal para assertividade)

- **Grupo A (ponto):** camundongo (tudo-verificado).
- **Grupo B (banda-herdada):** humano (envelope S3 + relógio humano).
- **Grupo C (banda-extrativa):** hamster, vole (Kt ordinal + expressão flag; proveniência obrigatória por célula).
- **Grupo D (controle):** rato (não-paramétrico, declarado), levedura (ortogonal).
**Assertividade máxima atingível hoje:** ordinal + banda por espécie com proveniência por parâmetro — nunca ponto — até dado [ORGANOID]/[MOUSE] informar o REPARAM_LOOP.

## §7 · Regras
Número de JSON · claim → [PMID] · banda≠ponto · escopo [SIM] · correlação global explicitada como fraca (não omitida) · este doc é PLAN_DOC (nada migra a manuscrito sem gate).
