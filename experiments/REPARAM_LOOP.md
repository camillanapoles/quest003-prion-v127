# PARTE 2 — Artefato 2.4: Loop de Re-parametrização ([ORGANOID] → modelo → G1)
## Como o dado medido realimenta os modelos parametrizados (o coração da tese de continuidade)
**v1 · 2026-08-27 · princípio: cada dado novo muda EXATAMENTE o que ele informa — nada mais**

## O loop (4 passos, versão travada)

1. **INGESTÃO [ORGANOID]:** dados do esquema F7 (freeze checklist) entram SEM tocar nos [SIM] arquivados; guardados como tier novo em `experiments/g0_wet_results/`.
2. **RECALIBRAÇÃO ALVO (o que o dado pode mudar):**
   - κ→concentração real do A6 (fecha a limitação 1 e a âncora ilustrativa §2.2 — dose conhecida × gradiente medido → κ efetivo por µM);
   - forma funcional do freeS (exp 1 vs 2): a dose-resposta do A6 É o teste discriminador (predição [SIM] travada nos sweeps);
   - θ* observado vs 0.333 (a predição central travada no release v1.0 — SEM retreinar para "acertar": comparação, não ajuste).
3. **O que NÃO muda com dado de organoide:** taxas murinas relativas do kernel (só dado [MOUSE]/humano publicado muda); parâmetros de transporte humano (só poroelastografia/validação independente); predições já travadas (comparam-se, nunca re-escrevem).
4. **PROPAGAÇÃO:** recalibrações atualizam o motor → versão v6 do modelo com changelog numerado → re-execução dos sweeps de sensibilidade sobre a nova parametrização → novas predições para G1 [MOUSE] com o mesmo rigor (pré-registro antes do próximo gate).

## Regra anti-hindsight (o guardião da Parte 2)
- Toda comparação dado-vs-predição cita o commit/release onde a predição foi travada (v1.0 para θ<0.33; v3.0 para exp1-vs-exp2).
- Toda recalibração gera PRE-DIÇÃO nova antes do próximo dado (o loop nunca "explica depois" sem antes ter previsto antes).

## Condições de sucesso da Parte 2 enquanto programa
- A6 fecha κ↔µM ⇒ o design calculus fica absoluto (não só relativo) para G1.
- A5/A7 testam a tese ⇒ contenção confirmada/refutada com θ_obs e IC.
- Negativo qualificado ⇒ publicação programática (kill-switch) + recalibração honesta.
