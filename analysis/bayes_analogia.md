# Probabilidade de Sucesso por Analogia — Modelo Bayesiano Estruturado (v1)

**Data:** 2026-08-26 · **Código:** `experiments/bayes_success_model.py` (Beta/Jeffreys + Monte Carlo 200k, seed 42, auditável) · **Dados:** `bayes_results/bayes_success.json`

## Método
Cada gate do programa recebe como prior os **sucessos/insucessos históricos reais dos análogos**, ponderados por similaridade estrutural (peso = sim²), com prior Jeffreys. Análogo negativo incluído (6 falhas anti-príon em clínica). Base dura da indústria entra só no cenário de aprovação: **neurologia fase-1→aprovação = 5,9%** (Citeline/BIO 2011-20), organoide-PDO preditividade ~80% (proxy oncológico, melhor disponível).

## Resultados (média · IC90 via MC)

| Cenário | Prob. | IC90 | vs estimativa estruturada anterior |
|---|---|---|---|
| **B · G0 dá GO** (halo no organoide) | **36,6%** | 14,6–60,5 | coerente c/ 50-65% do trans (o modelo é mais pessimista: inclui o histórico de 0/6) |
| **A · Desaceleração clínica significativa** | **5,0%** | 0,4–13,6 | abaixo dos 30-45% estruturados |
| **C · Aprovação regulatória plena** | **0,3%** | 0,0–1,1 | — |

**Gates individuais:** mecanismo funciona 50% [28-73] · organoide prevê 73% [37-97] · vetor entrega 36% [17-56] · clínica em genético 38% [5-81] · base neurologia 6,8% [2-13].

## Leitura honesta — por que os números caíram e o que isso SIGNIFICA

1. **O IC90 do gate A (0,4–13,6%) captura quase toda a margem da incerteza do programa** — e a mediana (3,9%) próxima da média indica cauda longa de fracasso, não otimismo central. A probabilidade composta pune: 4 gates multiplicados com incertezas somadas.
2. **Onde o modelo discorda de nós:** nossa "desaceleração 30-45%" era estimativa estruturada **condicional** (dado mecanismo+vetor funcionarem); o modelo marginaliza sobre TODAS as formas de falhar, incluindo o 0/6 do campo príon e o 5,9% da neurologia. **Ambos estão certos em suas perguntas**: 30-45% é P(slow | tudo anterior OK); 5% é P(slow | hoje, do zero).
3. **O único número acionável imediato é o B: 36,6% de GO no G0** — e é EXATAMENTE por isso que o G0 é o próximo passo: um experimento de 10 meses que compra o update bayesiano mais barato do programa. Se A5/A7 mostrarem gradiente, o gate mecanismo salta de 50% [28-73] para ~90%+ e o cenário A mais que dobra.
4. **Comparação de realidade:** 0,3% de aprovação plena está na ordem do campo (neurologia média 5,9% × nosso prêmio de raridade/risco adicional) — não é sinal de projeto ruim, é o preço honesto de inovação first-in-class em príon.
5. **Value of Information (implícito):** EVPI do G0 ≈ P(GO)×[P(A|GO)−P(A)] ≈ 0,37×(0,12−0,05) ≈ **+2,6 pontos percentuais por R$300-800k** — provavelmente o melhor retorno informacional por real do programa inteiro.

## Limitações (declaradas)
- Similaridades (0,55–0,90) são rubrica declarada, não medida — sensibilidade deve ser testada (próxima iteração: sweep sim±0,15)
- Análogos escassos (n=1-6); Beta/Jeffreys honesto mas largos por construção
- PDO ~80% é proxy oncológico; validade preditiva de organoide neural-infectado é desconhecida (o que é, ele mesmo, parte do que G0 testa)
- Correlação entre gates assumida zero (conservador: na prática mecanismo→vetor são positivamente correlacionados via G0, o que SUBESTIMA o cenário A pós-GO)

**Nota de governança:** este modelo substitui a coluna "probabilidade" das versões anteriores onde as duas perguntas coincidem; as estruturadas permanecem como P(condicional). A tabela-mãe agora tem as duas leituras, rotuladas.

---

## Apêndice v2 — Sensibilidade e correlação (`sensitivity_sweep.py` → `bayes_results/sensitivity_sweep.json`)

| Cenário rubrica | A (indep) | A (corr ρ=0,4) | B (G0-GO) |
|---|---|---|---|
| Pessimista (sim−0,15) | 5,4% [0,4-15,4] | 5,4% [0,4-15,2] | 36,3% [12,6-62,4] |
| **Central** | **5,1% [0,4-13,7]** | 5,1% | **36,5% [14,5-60,3]** |
| Otimista (sim+0,15) | 4,9% [0,5-12,7] | 4,9% | 37,6% [16,6-59,6] |

**Conclusão de robustez:** as estimativas do modelo v1 NÃO dependem criticamente da rubrica de similaridade (Δ<0,5pp em A; <1,3pp em B através do sweep inteiro) nem da suposição de independência (ρ=0,4 muda <0,2pp). O número que importa — **G0-GO ≈ 36% e desaceleração-marginal ≈ 5% — é estável**. A principal fonte de variância verdadeira permanece a largura dos ICs (incerteza epistêmica dos análogos escassos), que só o próprio G0 reduz.
*(Nota técnica: contra-intuitivamente, sim+0,15 BAIXA levemente A — porque peso maior no análogo negativo 0/6 e no 3/20 do AAV puxa os gates para baixo; coerente com o desenho honesto.)*
