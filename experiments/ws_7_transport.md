# WS-7 — Engenharia de Transporte da V127ΔGPI: demanda, soluções paralelas e solver

**Data:** 2026-08-25/26 · **Artefatos:** `ws_7_solver.py` (auto-testado: massa 100%, ℓ analítico×numérico err 0,5%) + `ws_7_results/{ws_7_results.json, ws7_steady_field.png, ws7_thiele_chart.png}` · **venv numpy:** `/workspace/.venv-numpy`

---

## 1. A DEMANDA — por que este é um gargalo real

O programa inteiro depende de uma pergunta fisicamente quantificável que nenhum paper da cadeia responde: **qual o tamanho do halo protetor de um depósito secretor, e qual espaçamento de injeção o anel precisa?**

- A tese (célula secretora ◆) produz um agente difusível — mas "difusível" sem escala é frase, não desenho. O protocolo cirúrgico (nós do anel, volume por nó) exige número.
- R3 (v2.2): contenção virou problema de **gradiente** (dose/frequência), não de geometria — gradiente exige saber onde a concentração cai abaixo do limiar dominante-negativo.
- R5a (v2.2): o hidrogel HA protege a célula, mas se a malha retiver a proteína, o gel vira armário que prende a arma — precisa critério de porosidade.
- O contexto clínico de falha é documentado: refluxo e distribuição heterogênea são os modos de falha clássicos da CED (Krauze 2005; revisão Elder/Lonser 2025).

## 2. O PROBLEMA FÍSICO

Escala do ECS (âncoras verificadas): fração volumétrica **α ≈ 0,20** e tortuosidade efetiva **λ ≈ 1,6-2,0** para macromoléculas (Thorne & Nicholson, PNAS 2006, 828 cites). PrP ΔGPI ~30 kDa, R_h ≈ 2,5 nm → D_livre ≈ 1,25×10⁻¹⁰ m²/s (Stokes-Einstein) → **D_eff ≈ 3,9×10⁻¹¹ m²/s**. Consumo do escudo: capping de pontas de fibrila (reação do modelo nucleação-polimerização de Masel, Jansen & Nowak 1999 — 332 cites), linearizado como k_eff de 1ª ordem + clearance (k_cl, t½ 19h-8d).

Equação resolvida (ADR em meio poroso):
∂(αc)/∂t = ∇·(D_eff∇c) − ∇·(vc) + S(x) − k_eff·c

## 3. SOLUÇÕES PARALELAS/CORRELATAS — o que outros campos já resolveram (potencial de replicação)

| # | Campo de origem | O que transfere | Potencial |
|---|---|---|---|
| S1 | **Águas subterrâneas (contaminantes)** | A equação ADR inteira + solvers FV maduros | ★★★ direta |
| S2 | **Petróleo (injeção de traçadores/EOR)** | Canalização por heterogeneidade de κ = nossos cistos espongiformes | ★★★ conceito+solver |
| S3 | **Liberação controlada (stents, implantes)** | Cinética de saída de matriz polimérica (Higuchi/Korsmeyer) → o caso hidrogel | ★★★ método |
| S4 | **Engenharia química (reatores catalíticos)** | **Módulo de Thiele / fator de efetividade** — o raio de proteção É um problema de penetração clássico com solução analítica | ★★★★ reenquadramento exato |
| S5 | **Baterias Li-ion (modelo de Newman)** | Fontes/sumidouros acoplados em meio poroso, numérica robusta | ★★ numérica |
| S6 | **Neurociência de fluidos (glinfático/perivascular)** | O termo sumidouro k_cl (clearance real do SNC) | ★★★ parâmetro |
| S7 | **Cinetica priônica (Masel 1999)** | A reação de capping R(c) com parâmetros estimados | ★★★ termo-fonte |
| S8 | **Repositórios nucleares (calor decaimento)** | Difusão+decaimento em escalas de anos | ★★ analogia |
| S9 | **Radioterapia (dose-painting)** | Planejamento clínico por campo de dose ≈ campo de concentração | ★★ deploy clínico |
| S10 | **CED oncológica (já no plano)** | Falha por refluxo/vazamento (Krauze 2005; Elder 2025) | ★★★ validada |

**O achado conceitual (S4):** o halo do escudo é um problema de Thiele — comprimento de penetração **ℓ = √(D_eff/k_eff)**, com solução analítica que serve de verificação para o numérico (feita: 0,5% de erro).

## 4. RESULTADOS (execução real — ver ws_7_results.json)

**A. Raio de proteção do depósito secretor (r = ponto onde c = 10% do pico):**

| k_eff (s⁻¹) | t½ implícito | ℓ = √(D/k) | r₁₀% (1D) | r₁₀% (FV 2D) |
|---|---|---|---|---|
| 1×10⁻⁶ | ~8 dias | 6,2 mm | 5,1 mm | — |
| 3×10⁻⁶ | ~2,7 dias | **3,6 mm** | **4,2 mm** | **5,8 mm** |
| 1×10⁻⁵ | ~19 h | 2,0 mm | 3,2 mm | — |

**REGRA DE DESENHO 1 (anel):** cobertura útil por nó ≈ **4-6 mm de raio** no caso central → **espaçamento entre nós de injeção do anel ≈ 8-12 mm** para cobertura contínua da penumbra. Um único depósito central NÃO cobre um lobo (confirma quantitativamente o redesenho em nós do anel — v1.1 — e dimensiona a cirurgia do G4).

**B. Tempo de regime:** t_ss ≈ ℓ²/D ≈ **~4 dias** (caso central) → os readouts de 90d do G0/G1 operam em regime estacionário — a cinética de estabelecimento NÃO é gargalo.

**C. Hidrogel (carreador HA, modelo de obstrução exponencial):** ξ/r_p = 2 → D_gel/D₀ ≈ 0,41 (retenção preocupante); **ξ/r_p ≥ 5 → D_gel/D₀ ≥ 0,70 (liberação OK)**. Com r_p(PrPΔGPI) ≈ 2,5 nm → **ξ ≥ 12-15 nm** → HA a 1-2% (malha típica 20-100 nm) **APROVADO como carreador secretor**; HA > 5% (ξ ~5-10 nm) **rejeitado** para este uso. REGRA DE DESENHO 2 fecha a tensão WS-7×R5a com critério numérico.

**D. Canalização por cistos (κ×50):** na escala simulada (Q = 0,1 µL/min, ~1,6 h) a captura precoce ≈ 0 — o regime é difusão-limitado longe da cânula; advecção intersticial de infusões discretas é local. **Limitação honesta:** o teste de canalização exige Q maiores/dias de infusão contínua (cenário in-dwelling) — fica como extensão, não como resultado.

## 4-B. RESULTADOS v2 — onda×escudo e pulso mRNA (`ws_7_v2_wave.py` → `ws_7_results/ws_7_v2.json`)

**A. Condição de contenção (r*):** a onda priônica morre onde o capping excede a replicação. Com o campo do v1, a casca de contenção em torno de um depósito de 1 mm vale:

| θ (replicação/capping no pico) | 0.5 | 0.2 | 0.1 | 0.05 | 0.02 | 0.01 |
|---|---|---|---|---|---|---|
| **r* (mm)** | 1,7 | 2,9 | **4,2** | 5,6 | 7,7 | 9,5 |

*Leitura:* se o pico do depósito tiver capacidade de capping 10-50× a taxa de replicação (θ 0,1-0,02 — plausível para secreção contínua vs conversão que depende de PrPSc disponível), a casca protetora tem 4-9 mm — **consistente com o espaçamento 8-12 mm do anel (v1)**: cascas vizinhas se sobrepõem com margem. θ é o parâmetro que o **G0-A5/A7 mede na prática** (gradiente proximal/distal), fechando o loop desenho⇄experimento.

**B. Trem de pulsos mRNA (R2c / G0-A7):** vale entre pulsos (c_final/c_pico) por intervalo — 3d: 1,00 · 5d: 0,81 · **7d: 0,56** · 10d: 0,29 · 14d: 0,11.
**REGRA DE DESENHO 3 (redose):** intervalo **≤7 dias** mantém cobertura contínua (≥50% do pico; alvo f≥0,3); a 10-14 dias aparecem vales de exposição. Alternativa: LNP de t½ de produção ≥4 dias (segunda geração) permitiria quinzenal.
*Self-tests v2:* θ→1 retorna borda do depósito (1,0 mm) ✓; T→0 → razão 1,00 ✓.

## 5. Limitações (declaradas)
1. k_eff é paramétrico (varredura 1e-6..1e-5) — o capping real depende da densidade de pontas de fibrila (acoplamento completo ao modelo de Masel fica para a versão 2 do solver).
2. κ do espongiforme é sintética (50×) — substituir por mapa DTI/poroelástico quando houver imagem de paciente.
3. 2D, malha 192², Euler explícito — suficiente para regras de desenho; refinar em FEM se for para planejamento cirúrgico individual.
4. Reação linearizada; sem competição explícita PrPC/PrPSc na interface do halo (próxima iteração: acoplar ADR×NPM).

## 6. O que WS-7 muda no programa (encaminhado)
- `ring` ganha espaçamento quantificado (8-12 mm) — entra no desenho cirúrgico do G1/G4
- `hagel` (R5a) ganha critério de aprovação/rejeição por wt% — valida Liang/Nih com margem
- `mrna` (R2c): mesmo ℓ se aplica ao pulso transiente — a dose de reforço deve espaçar < t_clearance+k para não deixar vale entre pulsos (próxima iteração numérica)
- G0-A5/A7: endpoints de gradiente proximal/distal agora têm escala esperada (~4-6mm) para calibrar microdissecção

## WS-9 — Hierarquia de dados/simulação para calibrar θ ANTES do G0 (definida 2026-08-26)
**Pergunta-guia:** existe simulação computacional suficiente da PRÓPRIA organela? (obs do usuário)

**Varredura executada — veredito:**
- ❌ Simulação de organoide-príon NÃO existe (lacuna confirmada → é NOSSA — methods paper)
- ✅ METADE 1 existe COM CÓDIGO: **Igel et al. bioRxiv 2024.05.01.592001 (INRAE/Lyon — grupo Béringue/Rezaei): modelo estocástico reação-difusão da propagação priônica (algoritmo de Gillespie), com diversidade estrutural de PrPSc + resposta tecidual; aba "Data/Code" no bioRxiv**
- ✅ METADE 2 existe: frameworks computacionais de organoide (Montes-Olivas 2019; Neagu 2026 — modelos cell-based com solvers reação-difusão)
- ✅ VALIDAÇÃO: time-courses publicados de Groveman 2019/2021 (crescimento PrP-res por subtipo; decaimento com PPS)

**Plano WS-9 (mesclagem):** kernel cinético do Igel (Gillespie) + geometria esferoide organoide + TERMO DE CAPPING V127ΔGPI (nosso, inédito — ninguém simulou tratamento nesta família) → **"ensaio in silico do G0"**: varrer θ antes do laboratório, com IC via WS-8.
**Escada de dados (se um degrau faltar, sobe o próximo):** [1] código+parâmetros Igel → [2] frameworks organoide → [3] digitalização Groveman (curvas publicadas) → [4] priors WS-7/8.

## WS-9 — RESULTADO DO ENSAIO IN SILICO DO G0 (Colab VM, 2026-08-26)
**Executado:** port Python do kernel Igel 2024 (params Zenodo) + capping V127ΔGPI, malha 96², varredura κ∈{0.5..32} — na VM Colab via google-colab-cli-android (fork do usuário), API com timeout 900s.
**Pipeline destravado:** agent → colab CLI → VM Colab (CPU/GPU/TPU) → resultados locais. Token OAuth persistido; aprendizados: fork Android conecta onde oficial falha; baixar TODOS os outputs no mesmo ciclo (idle-prune); CLI oficial 0.6.0 incompatível com jupyter-kernel-client atual (shim aplicado).
**Entregas:** ws_9_insilico.png (frentes vs tempo por θ + curva de resposta R_final(θ)) em snapshots/; JSON perdido com a VM efêmera (re-rodável em 1 ciclo).
