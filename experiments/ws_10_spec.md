# WS-10 — Especificação de Requisitos: Simulador de Alta Fidelidade + Gêmeo Digital do Protocolo
**Quest 003 · v1.0 · 2026-08-26 · Alvo: GPU SaladCloud (RTX 3090/4090, container Docker)**

---

## PRODUTO 1 — SIMULADOR DE AMBIENTE REAL (física doentes→tecido, tempo real, renderizável)

### 1.1 O que deve ser computado (modelo matemático)

**Meio (parênquima 3D):**
- Malha Euleriana 3D: 256³ (mín) → 512³ (alvo) voxels, voxel = 50-100 µm (escala de um glomerulo neurológico)
- Meio poroso heterogêneo por campo: fração ECS α(x) ∈ [0.12, 0.25], tortuosidade λ(x) ∈ [1.4, 2.2], permeabilidade κ(x) (cistos espongiformes = κ×50, até 5% do volume)
- Difusão anisotrópica opcional (tensor D alinhado a tratos — ativa módulo DTI sintético)

**Príon (kernel estocástico completo — evolução do mean-field v4):**
- Variáveis por voxel: B_i(x,t) i=1..s (polímeros por tamanho), C(x,t) (pool conformacional), PrPC(x,t) (substrato nativo, com mapa de expressão)
- Reações (tau-leaping GPU, não mais determinístico):
  - auto-catálise C→2C · K_auto (com saturação C/(C+C₅₀) — calibrada: t_dupl = 12,1 d)
  - templating B_a→B_{a+1} · K_templ·tp(x)
  - fragmentação B_a→B_{a-1}+C · K_frag·C
  - nucleação C→B_1 · K_nucl
  - condensação/descondensação · K_cond/K_decond
  - clearância intersticial k_cl (glymphatic-like)
- **Neurônios como agentes lagrangianos**: grade de ~10³-10⁴ células com estado {saudável, UPR, morto} — UPR desliga templating na vizinhança (raio tpr) após threshold uprd por uprt; morte quando carga local > limiar (para morfologia espongiforme emergente)
- **PDE de transporte** (acoplada às reações, explícita em GPU):
  ∂(αc)/∂t = ∇·(D_eff/λ² ∇c) − ∇·(vc) + R_reac(x, c, estado) − k_cl·c
  com v(x) de infusões CED (Darcy: v = −κ/µ ∇P, fonte de pressão na cânula)

**Terapia (mesma física, agentes extras):**
- Depósitos celulares secretores: esferas de raio ~0,5-1 mm com taxa de secreção S(t) de V127ΔGPI (decaimento opcional a longo prazo — meia-vida do enxerto)
- V127ΔGPI difunde (D já calibrado 3,86×10⁻¹¹ m²/s), compete por substrato: freeS = (1+κ·c_V127)^-2 — mesmo termo validado no WS-9
- LNP-mRNA: partículas com cinética de expressão (t½ 2 d — Xue 2025) injetadas intratecal (campo de fluxo CSF simplificado)
- ASO-ponte: redução percentual de PrPC global (perfil farmacocinético ION717-like)

### 1.2 Escalas e fidelidade numérica (protocolo à la skill fluidsim)
- Unidades SI reais (s, m) — relógio já humanizado (WS-9 v4: 1 d real; t_dupl 12,1 d âncora Groveman)
- Δt interno: adaptativo por CFL de difusão (τ ≈ Δx²/2D/λ² ≈ 0,5-2 s real por passo); 10⁵-10⁶ passos por "mês de doença"
- **Validação obrigatória por gate (não "rodeu = vale"):** (V1) conservação de massa sem reação <0,1%; (V2) θ*∈[0,30-0,36] reproduzido no limite 2D (regressão ao v4 já validado); (V3) halo estacionário = √(D/k) analítico ±5%; (V4) hierarquia MV2>MV1 preservada; (V5) eclipses 25-35 d e duplicação 12,1 d
- Estocasticidade: tau-leaping com seed por réplica; ≥3 réplicas por condição para intervalos

### 1.3 Runtime & render (tempo real)
- **Stack**: PyTorch (ou JAX) — reações como ops tensoriais em GPU; PDE por stencil; agentes em tensor de estados. Kernel único compilado (torch.compile) — alvo ≥ 20× tempo real (1 mês de doença < 90 s em 3090)
- **Render em tempo real**: volume raymarching (vispy/ModernGL, formato 3D-tex) — carga priônica em mapa inferno, campo V127 em azul, neurônios mortos em pontos escuros, corte de plano arrastável
- Telemetria: curvas R(t), carga(t), θ local — dashboard on-line durante o run
- **SaladCloud**: container Docker (base pytorch:2.x-cuda12) ~6 GB, job via API (SCE), checkpoint HDF5 por hora de simulação, custo-alvo < US$ 0,40/h (3090)

### 1.4 Critérios de aceite do Produto 1
A1. Roda 512³ + 10⁴ neurônios ≥ 10× tempo real na 3090
A2. Passa V1-V5
A3. Vídeo 360° e screenshots de 4 ângulos exportáveis
A4. Um mês de doença humana (30 d) + terapia completa renderizados em < 10 min de parede

---

## PRODUTO 2 — EMULAÇÃO DO PROGRAMA CLÍNICO (gêmeo digital do protocolo, fase a fase)

### 2.1 Escopo simulado (sucesso conforme desenho — pop. E200K pré-sintomática)
Reproduce o fluxo clínico INTEIRO sobre o motor do Produto 1 (cérebro = região cortical + SVZ simplificada em 3D):

**Fase 0 — Estado do paciente (t=-6 meses):**
- Cérebro saudável; sementes prônicas iniciais discretas (2-5 focos de carga mínima, locais plausíveis — córtex/putâmen; parâmetros do subtipo)
- Marcadores simulados: RT-QuIC(-) ou fraco(+), NfL basal, PrPC mapa normal

**Fase 1 — Diagnóstico/eligibilidade:**
- Exame simulado: RT-QuIC de LCR (função da carga total acima de threshold de detecção ~10² SD50-eq), NfL sérico (função da taxa de morte neuronal), MRI (carga > limiar de detecção por voxel agregado)
- **Critério de inclusão G4 avaliado pelo próprio modelo** (CDR, banda de conversão)

**Fase 2 — Produção do produto celular (t=0 a -2 meses, paralelo):**
- Autóloga: iPSC→NSC editada V127ΔGPI (QA gates: pureza, karyo, secreção ng/mL/d — **simulamos o atraso de fabricação no calendário**)
- Enquanto isso a doença progride no fundo (o modelo NÃO pausa — janela real!)

**Fase 3 — Cirurgia (t=0): planejamento + execução**
- Entrada: MRI sintética do estado ATUAL (focos visíveis + margem)
- Planejamento: trajeto "caminho danificado" (evitar tratos sadios), NÓS do anel a 8-12 mm de espaçamento (regra WS-7) ao redor dos focos, depósito central 1-2 mm
- Execução simulada: cânula insere (dano mecânico local ~0,5 mm³ por trajeto), deposita células no hidrogel HA (ξ≥5×r_p — controla taxa de liberação), CED no recuo
- Imperfeições REAIS modeladas: refluxo parcial (10-20% de perda), distribuição irregular, 1 nó "falho" aleatório por caso

**Fase 4 — Pós-op imediato (t=0 a +30 d):**
- Inflamação cirúrgica transitória (κ local reduzido por 7-14 d — reduz a competição)
- Estabelecimento do halo (t_ss ~4 d — WS-7)
- Exame simulado +14d: MRI (edema), PrP-LCR (spike transitório), NfL (pico operatório)

**Fase 5 — Monitoramento contínuo (t=+30 d → +24 meses):**
- A cada 60-90 d (calendário do G4): exame simulado — RT-QuIC (titulação), NfL (tendência), MRI (volume de foco), cognição-proxy (fração de neurônios vivos ponderada)
- **O modelo DECIDE e RESPONDE:** se frente ultrapassar a casca em algum eixo (falha local) → simula redose de resgate (mRNA-LNP intratecal, braço R2c: redose ≤7 d — WS-7 Rule 3) e a doença reage
- Loop terapêutico adaptativo: o gêmeo digital roda "o que o médico faria" vs "o que o protocolo manda"

**Fase 6 — Desfecho (t=+24 meses):**
- Primário simulado: tempo até conversão clínica (proxy: perda de 20% de neurônios regionais) vs braço-controle natural-history do mesmo paciente virtual
- Secundários: carga total, tempo com halo íntegro, nº de redoses, eventos adversos
- **Cohorte virtual**: N=50-200 pacientes virtuais (variando semente/época/foco/κ de resposta) → poder estatístico e curvas Kaplan-Meier simuladas

### 2.2 Diferença crucial vs Produto 1
P1 = microfísica validada; **P2 = microfísica + processo clínico em cima** (tempo de fabricação, imperfeição cirúrgica, calendário de exames com limites de detecção, decisões adaptativas). P2 responde a pergunta de investimento: *"se tudo der certo como desenhado, quantos meses de sobrevida funcional ganha o paciente-tipo e com qual variância?"*

### 2.3 Requisitos de dados do P2 (âncoras já existentes na quest)
- Limites de detecção: RT-QuIC (Green 2018), NfL conversão (Gentile 2024 — sem minociclina!), MRI espongiforme
- PK: secreção NSC (dossiê G0-A5), LNP t½ (Xue 2025), hidrogel (Liang 2013 + WS-7 Rule 2)
- História natural E200K: incubação/idade-onset da lit. (Appleby 2026) para o braço-controle

### 2.4 Arquitetura de software (comum)
```
ws10/
  core/       # motor estocástico 3D (torch GPU) + validação V1-V5 (CI)
  tissue/     # geradores de parênquima sintético + DTI sintético
  therapy/    # agentes: depósito secretor, LNP, ASO, cânula/CED, hidrogel
  clinic/     # módulo de exames simulados + protocolo G4 + scheduler adaptativo
  render/     # raymarching tempo real + export MP4/360
  salad/      # Dockerfile + job-submission SaladCloud (API SCE) + checkpoints
  tests/      # V1-V5 + clínica determinística (seed fixa)
```
- Linguagem: Python 3.12 + PyTorch; render vispy; CI de validade numérica obrigatório a cada merge (padrão da skill fluidsim: "rodou ≠ convergeu")

### 2.5 Requisitos de infraestrutura
| Item | Especificação |
|---|---|
| GPU | RTX 3090 24 GB (SaladCloud ~US$0,35/h) — 512³×(s+3) campos float32 ≈ 8 GB ok |
| Container | Docker pytorch:2.4-cuda12.1, FFMPEG, vispy headless (EGL) |
| Persistência | Checkpoints HDF5 + dataset de runs no salad (obj storage) |
| Interface | Job assíncrono (API) + dashboard local para monitorar; estimativa P1: 1 mês-doença = 15-30 GPU-min ≈ US$0,10-0,20; cohorte P2 (200 casos×24 meses) ≈ 3-6 GPU-h ≈ US$2-4 |

### 2.6 Entregáveis e critérios de aceite do P2
B1. Cohorte virtual de ≥100 pacientes: curva de conversão com IC vs controle
B2. Trade-offs quantitativos: espaçamento do anel (8 vs 12 mm) × nº redoses × desfecho — mapa de decisão cirúrgica
B3. O que quebra primeiro: ranking de modos de falha (refluxo > node falho > inflamação > clearance) com frequência
B4. Vídeo "jornada do paciente" (P2 completo, fase 0→6, legendado) — o material de apresentação para comitê/investidor

### 2.7 Limitações declaradas
- Parênquima sintético (não, imagem de paciente real — integração DICOM é extensão futura)
- Kernel calibrado em organoidide MV1/MV2 (Groveman) — E200K terá params próprios quando medidos
- Imunologia grosseira (UPR + inflamação cirúrgica como moduladores locais, sem sistema adaptativo completo)
- P2 é EMULAÇÃO de cenário de sucesso (conforme pedido) — para estatística clínica real, G0-G4 reais

### 2.8 Roadmap de execução (proposto)
S1. Core 3D + V1-V3 (porta P1 mínima em GPU) — 1 semana de trabalho
S2. Neurônios-agente + espongiforme + render tempo real — +1 semana
S3. Módulo terapia (depósitos/CED/hidrogel) + vídeo A/B 3D — +1 semana
S4. Módulo clínico P2 (fases 0-6, exames, adaptativo) + cohorte — +2 semanas
S5. SaladCloud production + relatório final — +1 semana
