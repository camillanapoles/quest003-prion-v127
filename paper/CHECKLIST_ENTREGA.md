# ✅ CHECKLIST DE ENTREGA — Solicitação vs. Entregue vs. Falta
**Para: coorientador de pesquisa / banca doutoral** (correção: não é parente — interlocutor acadêmico formal)

---

## A. TABELA MESTRE — tudo que o attach solicitou

| # | Item solicitado | Status | Arquivo | Observação |
|---|---|---|---|---|
| 1 | **Conteúdo do paper** (nível pesquisa + criticismo esperado) | ✅ ENTREGUE | `manuscript_EN_v4.md` (28 seções-âncora, claim-tagged) | Passou revisão hostil (8 major endereçados) |
| 2 | **Versão em português** (mesmo modelo EN+PT) | ✅ ENTREGUE | `manuscript_PT_v4.md` | Paridade de conteúdo ✓ (marcadores claim só no EN — declarado) |
| 3 | **PDFs prontos** EN+PT | ✅ ENTREGUE | `preprint_v4_EN.pdf` · `preprint_v4_PT.pdf` | + v3 na release GitHub |
| 4 | **Metodologia, RSF, lógica, explicação** | ✅ ENTREGUE | §2 Methods completo | 4 métodos com equações + proveniência |
| 5 | **Modelo matemático: como feito, dados, parametrização, fonte** | ✅ ENTREGUE | §2.2-2.4 + `consistency_manifest.json` | α/λ→Thorne; D₀→Stokes-Einstein; k→Masel; relógio→Groveman; kernel→Zenodo 11093945 |
| 6 | **Insights e impactos mapeados** | ✅ ENTREGUE | §4 Discussion + `analysis/analogy_map.md` | transferibilidade AD/PD como hipótese declarada |
| 7 | **Possibilidade outras doenças** (AD/Parkinson) | ✅ ENTREGUE | §4.2 + refs Stopschinski/Jucker | qualificada: design framework, não terapia automática |
| 8 | **Lacunas do trabalho** | ✅ ENTREGUE | §5 Limitations (10 itens) + hostile review M1-M8 | gap RoB/GRADE formal declarado honesto |
| 9 | **Honra científica dos achados** (integridade) | ✅ ENTREGUE | `evidence_workspace/` completo | 33 fontes+43 claims+23 fatos: 4 validadores ZERO erros; v1 falhado documentado, não apagado |
| 10 | **Refs completas end-to-end** | ✅ ENTREGUE | 42 refs verificadas + `source_manifest.json` | DOI/PMID/URL em cada uma |
| 11 | **Best practices skill scientific-agent-skills** | ✅ ENTREGUE | harness 4 validadores + PRISMA 5/5 | skill scientific-writing 2.0 passo-a-passo |
| 12 | **Scientific map / diagrama de conexões** (como o projeto foi executado) | ✅ **ENTREGUE AGORA** | `snapshots/scientific_map.png` + grafo vivo 8137 | novo: pipeline metodológico Fase1→4 + garantias |
| 13 | **Layout Cambridge/Harvard 2-col (LaTeX)** | ⚠️ 95% | `paper/latex/manuscript_v41.tex` | .tex pronto+validado; PDF exige 1 célula Colab (fix lmodern no notebook) |
| 14 | **Ajuste de audiência** (tio→coorientador/banca) | ✅ ENTREGUE AGORA | este doc + `audiências` reenquadradas abaixo | tom formal acadêmico |

## B. O MAPA CIENTÍFICO (item 12 — o que ele mostra)

`scientific_map.png` (1650×1200) — 4 fases do pipeline com fluxo horizontal:
```
[FASE 1 AUDITORIA]──▶[FASE 2 FÍSICA WS-7]──▶[FASE 3 BAYES WS-8]──▶[FASE 4 IN-SILICO WS-9]
   42 refs, erros        3 regras, self-test     duas lentes 5%/30-45%    θ*=0.333 humanizado
   corrigidos            massa 100% Thiele 0.5%  6/6 falhas no prior      MV2>MV1 emergente
        │                       │                        │                       │
        └───────────────▶ GARANTIAS: 33 fontes E-ID · 43 claims · 4 validadores ZERO erros
                                │
                                ▼
        PREDIÇÃO PRÉ-REGISTRADA: θ<0.33 ⇒ contenção | anel 8-12mm | leitura 90-120d
                                ▼
        PRÓXIMO GATE: organoide G0 (8 braços, 10 meses, ~US$150k)
```
Complementos: grafo de conhecimento interativo (`127.0.0.1:8137`, 43 nós/60 arestas/vistas) + graphify comunidades + snapshots históricos.

## C. REENQUADRAMENTO PARA BANCA/COORIENTADOR (correção da audiência)

- **Documento de audiência 1**: substituir "conversa com tio" por **apresentação acadêmica formal de 20 min** — mesmo conteúdo científico, abertura neutra ("Este trabalho submete-se à apreciação de V.Sas."), sem linguagem familiar
- **Argumentos que a banca valoriza e JÁ estão no pacote**: predições com timestamp ANTES do experimento; revisão hostil documentada com resposta ponto-a-ponto; validação falha v1 conservada; harness auditável por terceiros (repo público)
- **Perguntas prováveis e respostas** já mapeadas: M1 (κ→µM, ordem de grandeza no §2.2), M3 (n=1 por subtipo, claim suavizado), M4 (taxas murinas vs relógio humano, frase exata no §2.4), "por que não RoB formal?" (declarado como gap, §coverage)

## D. O QUE FALTA PARA CONCLUIR (3 itens, nenhum científico)

| Falta | Esforço | Bloqueio |
|---|---|---|
| 1. Compilar LaTeX v4.1 → PDF Cambridge | 1 célula Colab (~4 min) | notebook pronto com fix; executar quando quiser |
| 2. Paridade de marcadores [claim:] no PT | ~1h de script | mecânico; declarado como limitação de paridade |
| 3. Depósito bioRxiv (DOI) | 15 min | **conta do autor** (só o usuário pode criar) |

## E. AUTOAVALIAÇÃO COMO PAPER-WRITER (conforme skill)

- **No-fabrication** ✓ (duas lentes bayesianas rotuladas; números herdados de JSONs)
- **Evidence-binding** ✓ (claim→sha256→fonte→método verificação→data)
- **Confidentiality** ✓ (nada não-publicado usado; repo público)
- **AI-disclosure** ✓ (SW-S01/03 no título do manuscrito e declarações)
- **Reproducibility** ✓ (notebook + JSON + PNG da execução original do usuário no repo)
- **Honest limitations** ✓ (10 nomeadas + 1 gap declarado + histórico de falha preservado)
