# Protocolo G0 — Ensaio Decisório em Organoides Cerebrais Humanos (Gate Killer)

**Quest:** 003 · **Versão:** 1.0 · **Data:** 2026-08-25 · **Status:** pronto para parceiro de lab
**Referência-modelo:** Williams K et al., Stem Cell Res Ther 2023;14:348 (organoide sCJD + NPC) — adaptado com deltas Gatdula 2026 / Zerbes 2026

---

## 1. Objetivo e hipótese

**Pergunta decisória:** células neurais editadas (iPSC-NSC) expressando PrP-V127 conseguem (a) resistir à conversão por sCJD e (b) inibir a propagação de PrP-res em **trans** — ou seja, no parênquima vizinho ao enxerto, sem contato célula-a-célula com o substrato convertido?

**Por que este gate mata ou salva o plano:** toda a "Estratégia dos Bombeiros" depende do efeito trans no parênquima. Gatdula 2026 demonstrou o DN trans com proteína recombinante anchorless in vitro; Zerbes 2026 validou V127ΔGPI sistêmico in vivo (+50 d). **Ninguém testou a entrega celular local.** G0 testa exatamente isso.

## 2. Desenho experimental

### 2.1 Braços (n=8 organoides/braço; total 48)

| Braço | Células/tratamento | Mecanismo testado |
|---|---|---|
| A1 — Mock controle | organoide não infectado, sem células | baseline eletrofisiologia/marcadores |
| A2 — Controle doença | sCJD infectado, sem tratamento | referência de progressão |
| A3 — Controle celular | sCJD + NSC **WT não editada** | isola efeito "célula por si" (trófico) |
| A4 — Membrana | sCJD + NSC **V127/V127 bialélica** (PrP de membrana) | resistência cis + trans apenas por juxtacrine |
| A5 — Secretora ⭐ | sCJD + NSC **V127/V127 + delecção da âncora GPI (ΔGPI), PrP secretado** | **mecanismo trans por agente difusível — o núcleo do anel** |
| A6 — Proteína direta | sCJD + PrP-V127ΔGPI recombinante aplicado ao meio (2 pulpos, d0 e d45 pós-seeding) | replica Gatdula 2026 como comparador acelular; valida o agente sem o veículo celular |

### 2.2 Linhagens celulares (produção independente do ensaio, com QC próprio)

- iPSC de doador saudável (preferir HLA haplotipo comum; documentar consentimento para uso em pesquisa) → NSC via diferenciação dual-SMAD.
- **A4:** knock-in V127 em ambos os alelos de PRNP (prime editing ou HDR + ssODN), selagem CRISPR off-target por NGS (top-50 sites previstos), cariótipo, ausência de SSEA-4/Tra-1-60 (gate de pureza <0.1%).
- **A5:** mesma base + delecção do sinal GPI (C-terminal), confirmar secreção por western blot de meio condicionado (dosar ng/mL/dia/10⁶ células — alvo: níveis comparáveis ao pico sérico estimado no Zerbes 2026, calibrar por ELISA).
- Cryo-preserved aliquots; mesma passagem para todos os braços celulares.

### 2.3 Infecção e seeding (linha do tempo, modelo Williams 2023)

```
D-120..D0    Organogênese (spin) → maturação 120 d
D0           Homogenato sCJD MM1 (10% w/v, 10 µL, biópsia confirmada RT-QuIC+/PrP-res+) vs mock
             [BSL-3, consumíveis de uso único, protocolo de descontaminação WHO]
D+90 p.inf   Seeding celular: 2×10⁵ células/órganoide, 2 sítios (injetor de micropipeta);
             A6 recebe primeiro pulso proteico
D+135        Meio-termo: coorte sacrificial n=3/braço (readouts parciais)
D+180        Endpoint principal: MEA 24h → fixação/proteômica
D+90..D+180  Meio condicionado coletado q15d para RT-QuIC seriado
```
*Ciclo total ≈ 10 meses por rodada (maturação 4 + infecção 3 + leitura 3). O readout decisório chega 90 d após o seeding.*

### 2.4 Endpoints

**Primários (critério de trans):**
1. PrP-res por immunoblot/ELISA em microdissecção: **zona proximal (≤1 mm do enxerto) vs distal (≥3 mm)** — o gradiente espacial É a assinatura do trans.
2. RT-QuIC do meio condicionado (lag phase e altura de sinal) — cinética de propagação global.

**Secundários:**
3. MEA: taxa de spikes/bursts (desfecho funcional de Williams 2023 — espera-se restauração parcial).
4. Sobrevida do enxerto: antígeno nuclear humano + Ki67; apoptose (cleaved caspase-3) — testa a previsão de hostilidade do microambiente.
5. Citocinas do meio (IL-6, TNF-α, IL-1β) — inflamação vs A3.

## 3. Critérios GO/NO-GO (pré-registrados)

| Resultado | Decisão |
|---|---|
| A5 ≥50% redução de PrP-res proximal vs A2 **e** gradiente proximal>distal significativo **e** lag RT-QuIC +≥25% | **GO G1** (camundongo humanizado) com desenho secretor |
| Efeito presente só em A4 (juxtacrine), não em A5 | GO-condicional: redesenhar para contato denso (contenção por " parede celular", não por difusão) |
| Efeito só em A6, não em braços celulares | Pivot: abandona terapia celular, prioriza proteína recombinante/AAV (convergir com Zerbes) |
| A4/A5 morrem (>70% apoptose) ou **aumentam** PrP-res | NO-GO celular; documento a causa e encerra esta linha da quest |

*Marginal estatística: teste t/Welch por braço vs A2, α=0.05 corrigido Holm (5 comparações); com CV~30%, n=8 detecta Δ≥50% com poder ~80%. Se variabilidade organoide >esperada, n=12.*

## 4. Biossegurança e governança

- Príons humanos: instalação BSL-3 (ou equivalente institucional), todo material destruído por incineração/NaOH+autoclave 134°C.
- Células editadas: comitê de biossegurança institucional (CTBio-like) aprova antes do seeding.
- Dados e materiais: registro prospectivo do ensaio (preprint de protocolo em bioRxiv antes do primeiro dado — padrão do campo pós-2020).
- O organoide infectado permanece infeccioso nos readouts — rotina de fixação com formol+fenol antes da saída da BSL-3.

## 5. Insumos e parceiros (Brasil)

- Organoides + sCJD homogenato: parceria com grupo já publicante ( Williams 2023 é Calgary; análogo nacional: laboratórios de organoides HUG-CELL/USP + banco de amostras CJD de referência FMUSP — Smid et al.).
- RT-QuIC: já operacional em centros BR (incluir validação inter-lab no plano).
- Proteína recombinante V127ΔGPI: expressão em HEK293, purificação por cromatografia de afinidade — ensaio de dobramento (CD spectroscopy) como QC.

## 6. Entregáveis do G0
1. Dataset (PrP-res proximal/distal, RT-QuIC séries, MEA) + código de análise
2. Relatório go/no-go com recomendação de desenho para G1
3. Rascunho de methods paper (organoide + NSC editada = citável independentemente do veredito)
