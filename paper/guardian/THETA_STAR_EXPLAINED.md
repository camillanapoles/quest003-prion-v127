# θ\* (THETA-STAR) — O que é, por que existe, e por que é O parâmetro do programa
## PLAN_DOC · 01/09 · documento pedagógico-formal · linhagem: F-25/F-26/F-39/F-43/F-44 · claims C038/C044/C046/C051/C052 · predição travada v1.0

---

## 1 · A intuição em uma frase

**θ\* é a fração residual de atividade de conversão que ainda escapa da contenção quando a "dose" de agente dominante-negativo está exatamente no limiar entre conter e não conter o príon** — é o número que diz *"quanto de conversão sobra no pior dia possível do anel de contenção"*.

## 2 · De onde ele vem (a cadeia física → matemática)

1. **O mecanismo biológico:** o agente V127-âncora compete com PrP^C pela conversão templada por PrP^Sc (dominante-negativo *em trans* — F-05/F-08). No motor, essa competição é o **termo de capping**:
   `freeS = (1 + κ·c)⁻²` — a fração de sítios de conversão ainda livres onde há agente na concentração c com potência κ.
2. **κ** (kappa) é a "dose efetiva": potência de capping do agente (κ↔µM via Kd — Chen 2010, validado V2). κ=2 ⇒ freeS=(1+2)⁻²=1/9: a conversão cai ~9× onde o agente está presente — mesma ordem da barreira de nucleação ~5× medida para G126V (Sabareesan 2017).
3. **θ** é definido como a fração de conversão residual no regime de capping: **θ = 1/(1+κ)** (a raiz quadrada de freeS na âncora central — a medida linear da atividade que sobrevive à dose κ).
4. **θ\*** (theta-star) é o valor de θ **no limiar de contenção**: κ\_min = a menor dose que ancora o anel; θ\* = 1/(1+κ\_min). Por isso θ\* é **adimensional** — é razão de atividades, não tem unidades de tempo, massa ou espaço. Essa adimensionalidade é a hipótese central da PARTE 3 (F-44).

**No mouse (calibração travada v1.0):** κ\_min=2 ⇒ **θ\*=0,333** — "um terço da conversão residual ainda escapa no limiar". Esse é o número pré-registrado, timestampado no release v1.0, **que o G0-wet compara e nunca retreina** (claim C052: estimador θ\_obs consagrado na Parte 2 mede exatamente isto no organoide; predição travada: **θ\_obs < 0,33 ⇒ contenção confirmada in situ**).

## 3 · Por que USAMOS este parâmetro (as 5 funções dele no projeto)

| # | Função | Por que θ\* e não outro |
|---|---|---|
| 1 | **Quantidade falsificável central** | "Contenção" binária não é ciência quantitativa; θ\* transforma o design numa **predição numérica pré-registrada** (θ\_obs<0,33) que o gate organoide pode MATAR — o critério de morte programática da tese |
| 2 | **Ponte dose↔biologia** | κ é a alavanca operacional (dose do agente); θ\* é o que a dose compra em termos de contenção — a **curva de resposta** (F-25/F-39: forma funcional testada e travada) |
| 3 | **Quantidade transferível entre espécies** | Por ser adimensional, é o candidato natural a **invariante estrutural** — a PARTE 3 inteira (F-44: Cenário B, razão 1,20) testa se ele sobrevive à troca da parametrização murina |
| 4 | **Interface com o cálculo de transporte** | O anel 8-12mm (Regra 1) e a casca r\* (F-22) são geometria; θ\* é a condição de contorno dinâmica que aquela geometria precisa manter — sem θ\*, o design de entrega não tem alvo quantitativo |
| 5 | **Regra de dose clínica futura** | F-44: κ\_requerido escala com Kt (cinética do hospedeiro) — θ\*(Kt) é a futura **curva de titulação por paciente/espécie**: "quanta dose para qual cinética" |

## 4 · O que θ\* NÃO é (guarda contra inflação)

- **Não é afinidade** (isso é κ/Kd); **não é taxa** (isso é Kt/K\_auto); **não é probabilidade** de nada clínico.
- **Não é absoluto**: é dependente da definição de horizonte de avaliação (F-44): livre-próprio (~2,5 u-sim) contém com κ=1,5→θ\*=0,4 · calendário t=5 idem · gerações-casadas-ao-base-tratado (~9,5) exige κ≥2→0,333 — **toda citação de θ\* deve declarar a def** (a predição v1.0 usa a def S3).
- **Não é dado medido** até o G0-wet: até lá é ⊕ [SIM] — usado como resultado no seu tier, nunca como dado (regra C047).

## 5 · Linhagem do número (auditoria completa)

v1.0 (release, 26/08): θ\*=0,333 travado com κ\_min=2 no modelo humanizado · S1 (F-39): forma funcional (expoente 2) confirmada como discriminadora · S3 (F-43): κ=2 rompe sob escala 2× nas taxas quando pareado por gerações — **θ\* é sensível ao Damköhler (razão reação/difusão), não só à dose** · PARTE 3 (F-44): Cenário B — θ\* central 0,333-0,400 entre espécies; extremo de cinética 4× (hamster-hi) degrada para 0,111 (κ\_min=8) — nasceu a **regra de titulação κ↔Kt** · G0-wet (pendente): θ\_obs mede o análogo organoide; comparação à âncora v1.0 sem retreinar.

## 6 · Glossário de uma linha (para a banca/leitor)
**κ** dose efetiva de capping · **freeS** fração de conversão livre (1+κc)⁻² · **θ=1/(1+κ)** conversão residual linear · **θ\*** θ no limiar de contenção (adimensional, pré-registrado) · **θ\_obs** estimador organoide da Parte 2 (C052) · **Kt** classe de taxas de autocatálise/templating (a única que move θ\* — F-43) · **Damköhler** razão reação/difusão que acopla θ\* ao transporte.

---
*Documento de referência pedagógica; nada aqui é claim novo — tudo deriva de F-25/F-43/F-44 + claims citados; migração a manuscrito só via gate.*
