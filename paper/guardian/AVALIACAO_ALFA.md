# AVALIAÇÃO ALFA (developmental) — Edição clínica da tese v2
## Skill: scholar-evaluation (qualitativo-primero, evidência-rastreável, SEM julgamento de prontidão/aceitação) · 01/09
**Objeto:** `paper/manuscript_Parte2_v1.md` @ camada-alfa (merge PR#5 + NOTA DE LEITURA + openers + siglas + Figura 4 + ABNT pipeline) · **Avaliador:** agente (developmental; validação humana: autora) · **Limitação declarada:** a validação-máquina da rúbrica (`validate_rubric` schema 2.0) ficou não-conforme nesta rodada (66 erros de conformidade de template — campos obrigatórios do template oficial); os achados abaixo seguem o método da skill (critério-nível + evidência + âncora + incerteza) sem depender do composite.

---

## Achados por critério (qualitativo primeiro; escores = resumo ordinal 0-4 com incerteza, nunca decisão)

### C1 — Compreensibilidade médica — `rated` 3 [2-4] · EV1, EV3
**Evidência:** NOTA DE LEITURA responde as 5 perguntas clínicas antes de qualquer técnica; §3.2/§4.7 abrem com "Em linguagem clínica". **Interpretação (âncora):** um clínico consegue seguir o argumento completo lendo apenas os openers + Figura 4 + conclusões; a matemática é opcional (declarado). **Limitação:** Cap.2 §2.4 (fundamento epistemológico) e Apêndice B permanecem densos sem opener — cobertura parcial. **Opções de melhoria (não-prescritivas):** opener clínico no §2.4; versão "resume para o clínico" de 1 página no início do PDF.

### C2 — Definições — `rated` 4 [3-4] · EV2
**Evidência:** LISTA DE SIGLAS ampliada (θ\*, θ\_obs, κ, Kt, Damköhler, PrP^C/PrP^Sc, RT-QuIC, DN) + mapa de símbolos na NOTA ("θ\* = quanto da conversão sobrevive à dose"). **Interpretação:** todo símbolo usado no texto principal tem definição leiga acessível. **Limitação:** símbolos dentro de equações (C₅₀, ℓ, D\_eff) dependem do §3.2 contextual.

### C3 — Pré-abordagens antes da penetração técnica — `rated` 3 [3-4] · EV1, EV3
**Evidência:** nota-frontal (pré-abordagem do PROGRAMA) + openers nos dois núcleos técnicos. **Interpretação:** o princípio "tema antes da penetração" está institucionalizado; cobertura = núcleos duros (equações + multi-espécie). **Limitação:** §2.4 e Cap.3 §3.3-3.5 sem openers.

### C4 — Estrutura — `rated` 4 [3-4] · EV4, EV6
**Evidência:** sumário único (fix do duplo-índice); ABNT NBR 14724 no CI; tabela-M reordenada/condensada. **Interpretação:** a queixa estrutural original (dois índices, desorganização) foi endereçada na raiz e é regressão-protegida (workflow). **Limitação:** validação VISUAL do PDF ABNT ainda pendente (autorrega da autora); formatação de tabelas no tex merece inspeção.

### C5 — Conexões claims→evidência→figura — `rated` 4 [3-4] · EV5
**Evidência:** C055-C057 pareadas com [evidence:] em 5.1/6.2/OE3/H2/limitação 9; N-fatos N055-059; gates 0/0. **Interpretação:** cadeia evidencial íntegra e rastreável (guardião atesta).

### C6 — Honestidade de enquadramento — `rated` 4 [4-4] · EV8
**Evidência:** pergunta 5 da NOTA ("que promessa NÃO faz"); §6.2 "não significam"; ressalva mandatória §5.1-bis; tiers em toda saída. **Interpretação:** o clínico não pode sair da leitura com expectativa inflada — a não-promessa é explícita e upfront.

### C7 — Suporte de figuras — `rated` 3 [3-4] · EV7
**Evidência:** Figura 4 nova (θ\* por espécie, banda Cenário B sombreada, linha v1.0) gerada dos JSONs p024 por script commitado — no CI (Termux não compila matplotlib). **Limitação:** incorporação visual no PDF ABNT pendente de verificação no run; figuras 1-2 são ponteiros-de-caminho (não embeds) — padrão histórico mantido.

---

## Síntese qualitativa (o composite não substitui o critério)
A edição alfa **resolve a barreira de entrada clínica** (C1/C2/C6) e **protege estruturalmente** (C4/C5); as frentes de desenvolvimento remanescentes são cobertura de openers (C3) e a verificação visual do PDF com a Figura 4 embarcada (C7) — ambas **não-bloqueantes** para a rodada alfa, ambas endereçáveis em uma passada. **Nenhum achado indica inflação de claim ou desconexão evidencial.** Obrigatório pela skill: isto NÃO é julgamento de prontidão-publicação nem aceitação — é feedback de desenvolvimento para a autora decidir a próxima versão.

## Insumos (rastreio)
Rúbrica/avaliação/manifesto das evidências: `tmp/{rubric,eval,evman}_alfa.json` (conformidade plena ao schema-máquina pendente — documentado).
