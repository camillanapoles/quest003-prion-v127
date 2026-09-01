# P-025 ANÁLISE — θ\* multi-espécie [SIM] (PARTE 3 Fases 2-3)
## Fontes: experiments/xspecies/p024_{mouse,human,hamster,vole}.json (GHA matrix run 33470363167, 4/4 success, C0 exato por job)

## §1 · RESULTADOS (defs pré-registradas do driver)

| Espécie | C0 | Banda Kt | κ\_min por ponto | θ\*=1/(1+κ\_min) | escapes |
|---|---|---|---|---|---|
| mouse | ✓ | {1,0} | 1,5 | **0,400** | 0 |
| human | ✓ | {0,5·1·2} | 1,5/1,5/2,0 | 0,400/0,400/**0,333** | 1 |
| hamster | ✓ | {1,5·2·4} | 1,5/2,0/**8,0** | 0,400/0,333/**0,111** | 3 |
| vole | ✓ | {1·1,5·3} | 1,5/1,5/3,0 | 0,400/0,400/**0,250** | 2 |

**Cenário: B (aproximadamente conservado)** — θ\* central por espécie ∈ {0,333; 0,400}, razão 1,20 ≤ 2×. A degradação monótona com Kt é o padrão dominante: **κ\_requerido ≈ acompanha Kt\_scale** (1→1,5 · 2→2 · 3→3 · 4→8 — superlinear no extremo).

**Confirmação estrutural:** valores de R idênticos entre espécies no mesmo Kt\_scale (por construção: parametrização = só Kt) — a pergunta "θ\* varia entre espécies?" reduz-se exatamente a "a banda Kt da espécie espalha θ\*?" — e a resposta é: bandas centrais NÃO (todas 0,4); extremos de hamster/vole SIM (0,111/0,250).

## §2 · PREDIÇÃO PRÉ-REGISTRADA — veredito honesto
**"Kt\_hamster ≥2× murino ⇒ contenção κ=2 falha" → REFUTADA sob a definição P-024** (pareamento ao crescimento livre próprio; horizonte curto ~2,5 sim-u): em Kt=2, κ=2 contém (R=0,659mm; o escape ocorre só em κ=1,5). **Nuance definicional crítica (3 defs, 3 vereditos):**

| Definição de horizonte | Kt=2, κ=2 | Onde |
|---|---|---|
| P-024: gerações do crescimento LIVRE próprio (t≈2,5) | **CONTÉM** (0,659) | p024 JSONs |
| Calendário fixo t=5 | **CONTÉM** (0,859≤0,90) | S3 pass1 (C\_Kt\_x2) |
| S3: gerações casadas ao BASE tratado murino (t≈9,45) | **ESCAPA** (2,828 censurado) | S3 pass2 |

⇒ **θ\* é dependente do horizonte de avaliação** — afirmação quantitativa nova [SIM], que qualifica toda comparação com a predição travada v1.0 (0,333 foi derivada no horizonte S3). A refutação é REPORTADA COMO ESTÁ (anti-hindsight); a predição só "confirmaria" sob a def S3 — trocar de definição após ver o resultado para salvar a predição seria hindsight.

## §3 · CONSEQUÊNCIAS PARA A TESE (achados)
1. **Cenário B**: θ\* aproximadamente conservado nas bandas centrais — transfer murino→humano é computacionalmente robusto NA MEDIDA EM QUE as taxas humanas não excedam ~2× murinas (banda herdada: contém).
2. **Regra de dose emergente**: κ\_requerido escala com Kt (superlinear >2×) — para espécies/pacientes com cinética ≥4× (hamster-hi), κ=8 → θ\*=0,111 — a "dose" de contenção deve ser titulada pela cinética do hospedeiro, não fixada universal.
3. **Vole**: θ\*=0,4 na banda central (aceitador universal ⇒ cinética de conversão alta, mas CONTENÍVEL na banda 1-1,5×); extremo 3× → 0,25.
4. Horizonte-dependência (§2) = limitação formal a declarar: predições devem citar SEMPRE a def de horizonte.

## §4 · N-FATOS (registrados): N055 θ\*\_mouse=0,400 (P-024-def) · N056 θ\*\_hamster-hi=0,111 (κ\_min=8) · N057 θ\*\_vole-hi=0,250 · N058 razão θ\*centrais=1,20 (Cenário B) · N059 predição hamster REFUTADA sob def P-024 (R=0,659 em κ=2/Kt=2).

## §5 · FILA
P-026 (síntese + gates + PR gap-mapper→main + /RECAP final da PARTE 3).
