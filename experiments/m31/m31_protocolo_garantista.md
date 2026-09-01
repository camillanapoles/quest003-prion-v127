# M3.1 — "A PRIMEIRA DOSE CALCULADA" · Protocolo Garantista Pré-Registrado (RELATE)
## Alto-impacto metodológico ➞ método garantista ANTES de computar · skill-scout: uncertainty-and-units + pkpd-modeling + incremental-implementation (avaliador: scientific-critical-thinking)

---

## §1 · AVALIAÇÃO CRÍTICA — o que M3.1 é, e o elo que falta (honesto)

**Definição operacional de M3.1:** o desenho de dose do V127ΔGPI expresso como **prescrição quantitativa com incerteza propagada** — para cada vetor (A5/A6/A7), cada banda-Kt de paciente/espécie: **κ\_req (M3) → concentração-alvo no depósito (µM, banda) → carga/massa por depósito → nº depósitos (anel 8-12 mm) → intervalo de redose (≤7 d) → dose total com banda de incerteza GUM** — mais o **falsificador declarado** (G0-A6 fecha κ↔µM, convertendo banda em ponto).

**O que JÁ temos (todos de JSON/registro):**
- κ\_req↔Kt (M3: 1→1,5·2→2·3→3·4→8) · θ\*=0,333 (v1.0) · banda humana Kt{0,5·1·2}
- Âncora κ↔µM **ILUSTRATIVA** (Chen 2010 Kd=71 nM; §2.2 P1: κ=2-4 ≈ 0,1-1 µM) — limitação nº1
- PK: meia-vida PrP 4,8-6,4 d (E039 Corridon) · redose ≤7 d (regra 3, trough ≥30-56%)
- Sequências PrP próprias (P023) ➞ **massa molecular computável do nosso dado** (~253 aa)
- Transporte: halo r₁₀%=4-6 mm/depósito; volume de distribuição do solver

**O elo que falta (a análise crítica que você pediu — fractal por natureza):**
1. **Cadeia dimensional κ→massa nunca foi fechada COM incerteza**: κ é adimensional-por-normalização; a conversão a µM usa proxy (Kd de Aβ!) — para M3.1 isto não pode permanecer ilustrativo-solto: vira **banda GUM Tipo-B** com fonte por el.
2. **Kt do paciente é desconhecido** ➞ a dose não é um número, é a **escada κ\_req(Kt)** com pior-caso explícito (κ=8 cobre Kt=4).
3. **Por vetor, a unidade de dose difere** (células+Q secretor / mg proteína / µg mRNA) ➞ M3.1-primário = **A6 (proteína recombinante — dose conhecível, o braço discriminador)**; A5/A7 como derivadas.
4. **Nenhum dado [ORGANOID]+** ➞ M3.1 inteiro é **[SIM]-planejamento** com tier honesto — a "dose" é prognóstico-calculado, não prescrição (a não-promessa permanece a regra).

## §2 · MÉTODO GARANTISTA (pré-registrado AGORA, antes de computar)

1. **Mapa dimensional primeiro** (uncertainty-and-units): tabela κ→µM→ng/depósito→mg-total, cada conversão com unidades, fonte e incerteza Tipo-B (GUM). Nada computa antes do mapa passar em auditoria dimensional.
2. **Entradas só de registro**: JSONs próprios + constantes com PMID/E-ID (Kd→Chen E-registro; meia-vida→E039; MW→calculado das sequências P023 via script).
3. **Incerteza propagada por el** (não ponto): dose = banda [limite-otimista, pior-caso] por banda-Kt × vetor; pior-caso = κ=8/Kt=4.
4. **Incremental-implementation**: unidades verificáveis — U1 mapa dimensional · U2 MW-PrP do nosso dado · U3 cadeia A6 (κ→µM→ng→mg×N-depósitos→redose) · U4 escada por banda-Kt · U5 JSON final + Figura 5 (escada de dose) · U6 claims C058+ · U7 seção-tese B4. Cada U: script determinístico → JSON → gate.
5. **Critérios de aceitação pré-declarados**: (a) toda célula da cadeia tem unidade+fonte; (b) banda final ≥2 extremos (otimista/pior-caso) SEMPRE; (c) falha de propagação (incerteza dominada por κ↔µM) é RESULTADO válido e esperado — declara que a dose fica banda-larga até G0-A6; (d) nenhuma unidade prescritiva clínica (mg "para administrar") — unidade de SAÍDA = planejamento [SIM].
6. **Avaliador**: scientific-critical-thinking em cada U (o mesmo loop do S3: critérios antes, colheita depois).

## §3 · SKILL-SCOUT (para esta tarefa)
| Skill | Papel |
|---|---|
| **uncertainty-and-units** | auditoria dimensional da cadeia κ→massa; GUM Tipo-B; sanity de ordem-de-grandeza |
| **pkpd-modeling** | lógica de redose/trough (regra 3 é PK de manutenção); meia-vida→intervalo; NCA-lite do desenho |
| **incremental-implementation** | U1-U7 com verificação por unidade |
| scientific-critical-thinking | avaliador por unidade (pré-registro acima) |
| scientific-writing | claims C058+ com hash/binding quando migrar à tese |

## §4 · LOCAL NA ÁRVORE (decisão)
**Branch novo `m31-dose`** (worktree-efetivo via clone dedicado), **filho de main** — pois: o cómputo pertence ao programa-mãe (não ao experimento de escrita); integra à tese unificada via **PR para writing-v2-test (capítulo B4)** após gates; nunca direto em main sem avaliação A-vs-B da escrita. (Se native-em-writing-v2-test: contaminaria o braço-B com ciência nova — errado.)

## §5 · PLANO DE PRODUÇÃO (como gerar M3.1)
U1-U2 hoje (mapa+MW) → U3-U4 (cadeia A6 + escada JSON) → U5 Figura 5 → U6 claims → U7 seção no B4 do braço de escrita. Estimativa: 1 ciclo de sessão para U1-U5; U6-U7 no fechamento do PaperSpine (Stage 6-writing).
