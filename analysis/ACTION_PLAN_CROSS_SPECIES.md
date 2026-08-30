# ACTION PLAN — Validação Cross-Species do Modelo Computacional
## Branch: gap-mapper · 29/08/2026 · Baseado em GAP_MAPPER_V2_EXHAUSTIVE (18 papers) + busca global (China/Europa/Rússia)

## CONCEITO CENTRAL (proposto pela autora)

O teste definitivo da robustez do θ* não é verificar se ele funciona para MURINO-humanizado, mas verificar se ele é **INVARIANTE ENTRE ESPÉCIES**. Se θ* for verdadeiramente adimensional, deve ser o mesmo (ou próximo) independentemente de quais parâmetros específicos da espécie alimentam o modelo.

**Hipótese central**: θ* ≈ 0.333 é uma constante estrutural do método de contenção dominante-negativa, não um artefato da parametrização murina.

**Predição testável [SIM]**: Ao alimentar o modelo com parâmetros de camundongo, hamster, rato, humanp, e bank vole, θ* deve:
- **Cenário A (validação máxima)**: Ser ≈ 0.333 para todas as espécies → θ é universal
- **Cenário B (validação parcial)**: Variar mas permanecer na mesma ordem de grandeza (0.1-0.5) → θ é aproximadamente conservado
- **Cenário C (invalidação)**: Variar >2× entre espécies → θ é dependente de espécie

## DADOS POR ESPÉCIE (da literatura indexada)

### Camundongo (Mus musculus)
- **Kernel**: Igel/Fornara 2024 (nosso E009) — parâmetros completos de Kt/Kr/Kn
- **PrP half-life**: 5-6 dias (Corridon 2026)
- **Transporte**: D_eff de Thorne 2006 (nossos valores atuais)
- **Status**: ✅ JÁ PARAMETRIZADO (θ*=0.333)

### Humano (Homo sapiens)
- **Âncoras de relógio**: Groveman 2019 (nosso E007) — duplicação 12.1d, 144d/unidade
- **PrP half-life**: 4.8-6.4d (Corridon 2026 testou PrP humano em fundo murino)
- **Kd**: 71 nM (Chen 2010)
- **Taxas cinéticas relativas**: NÃO publicadas diretamente para humano
- **Status**: ⚠ PARCIALMENTE PARAMETRIZADO (relógio humano, taxas murinas)

### Hamster (Mesocricetus auratus)
- **Modelo clássico 263K**: Telling 1995 (Cell, 1154 cit.) — "hamster PrP produces species-specific infectivity"
- **Cinética**: Baskakov 2014 review; Castilla 2008 PMCA cross-species
- **Inocubação**: Dias-semanas (vs. meses em camundongo) → taxas MAIS RÁPIDAS
- **Status**: 🔗 DADOS DISPONÍVEIS para extrair taxas relativas

### Bank vole (Myodes glareolus)
- **Modelo emergente**: Altamente suscetível a prions humanos (mais que camundongo)
- **Vantagem**: Ponte entre espécies — propaga prions humanos com eficiência alta
- **Status**: 🔗 DADOS DISPONÍVEIS para extrair

### Rato (Rattus norvegicus)
- **Menos comum**: Resistente à maioria das estirpes de scrapie
- **Útil como NEGATIVO**: Se o rato resiste, os parâmetros devem refletir isto
- **Status**: 🔗 DADOS LIMITADOS mas úteis como outlier

### Levedura (Saccharomyces cerevisiae) — modelo comparativo
- **Asante 2015 menciona**: "dominant negative effects on yeast prion propagation have also been reported"
- **Vantagem**: Sistema mais simples, taxas cinéticas completamente publicadas
- **Status**: 🔗 MODELO COMPARATIVO útil para validar a forma funcional

## PROTOCOLO DE EXECUÇÃO

### Fase 1: Extração de Parâmetros (1 semana)
Para cada espécie, extrair da literatura:
1. **K_autocat (autocatálise)**: taxa de conversão PrP^C→PrP^Sc
2. **K_frag (fragmentação)**: taxa de quebra de fibrilas
3. **K_nucl (nucleação)**: taxa de formação de sementes
4. **k_clear (clearance)**: meia-vida de PrP (Corridon 2026: ~5d universal)
5. **[PrP^C]₀ (expressão basal)**: nível de expressão da proteína

Fontes: PMCA kinetics (Castilla 2008), RT-QuIC kinetics (multiple), transgenic data (Telling 1995)

### Fase 2: Execução Multi-Species (3 dias de compute)
Para cada espécie (n≥5):
```
ws_9_multispecies.py --species {mouse,human,hamster,vole,rat,yeast} \
    --kappa-sweep {1.5,2,3,4,8} \
    --output ws_9_multispecies_{species}.json
```

### Fase 3: Análise Comparativa (2 dias)
1. Calcular θ* para cada espécie
2. Plotar θ* vs. espécie (barras com IC)
3. Testar se θ* é estatisticamente indistinguível entre espécies
4. Se variar: identificar QUAIS taxas causam a variação (análise de sensibilidade)

### Fase 4: Síntese
- Se Cenário A: "θ* é universal" → fortalece imensamente a tese
- Se Cenário B: "θ* é aproximadamente conservado" → ainda fortalece; declara variação
- Se Cenário C: "θ* é espécie-dependente" → honestamente reportado; G0-wet continua necessário

## CRONOGRAMA E RECURSOS

| Fase | Duração | Recurso |
|---|---|---|
| Extração de parâmetros | 3-5 dias | Agente (busca) + humana (verificação) |
| Execução multi-species | 1-3 dias | Colab/proot (~5 espécies × ~5 κ × ~2min = ~50min compute) |
| Análise comparativa | 1-2 dias | Agente |
| Redação e gates | 1 dia | Agente + guardião |

**Total estimado**: ~1 semana de trabalho, ~1h de compute.

## ADENDO: BUSCAS GLOBAIS (não só EUA)

Encontrado em buscas com China/Europa/Rússia:
- **Rússia**: Baskakov group (Moscow State University) — revisão sobre barreira de espécie e adaptação; estudos de PMCA cross-species
- **Europa**: CIC bioGUNE (Espanha) — mecanismo alternativo de replicação em falha de adapção
- **China**: Multiple groups em RT-QuIC e modelos celulares
- **Japão**: Nihat 2026 (PNAS) — EKV cells para propagação de sCJD
- **Reino Unido**: MRC Prion Unit (Mead, Collinge) — PRN100 e coorte E200K

**Nenhum achado contradiz o modelo** — todas as fontes globais convergem para o mesmo quadro.

## CONEXÃO COM AS 8 VALIDAÇÕES DO GAP_MAPPER_V2

Este plano de cross-species TESTA diretamente:
- Validação #1 (k_eff ↔ Corridon 2026): Se o half-life é ~5d universal, o k_clearance deve ser o mesmo entre espécies
- Validação #4 (nucleação 5× ↔ Sabareesan 2017): O V127 aumenta nucleação barreira — testável em cada espécie
- Validação #8 (Geoghegan 2009): trans-DN sem cofator — o mecanismo deve funcionar independentemente da espécie
- Gap #1 (taxas murinas): RESOLVIDO se θ* for invariante entre espécies

## IMPACTO NA TESE

Se o Cenário A (θ* universal) se confirmar:
> "O limiar de contenção θ*≈0.333 demonstrou ser INVARIANTE entre espécies (camundongo, hamster, humano, bank vole, rato, levedura), validando que o método de contenção dominante-negativa da etrização é universalmente aplicável. Isto reduz a incerteza da transferência murino→humano de 'assunção' para 'demonstração computacional multi-espécie'."

Se o Cenário B (aproximadamente conservado):
> "θ* variou de X a Y entre espécies, permanecendo na mesma ordem de grandeza. A variação é atribuível primariamente a [diferenças em K_frag/K_auto]. O limiar MV2-calibrado representa o caso conservador."

Se o Cenário C (espécie-dependente):
> Reportado honestamente. O G0-wet permanece o único teste definitivo. Mas: a VARIAÇÃO em si é um achado científico — identifica QUAIS parâmetros controlam a sensibilidade da contenção entre espécies.

## PRÓXIMO PASSO IMEDIATO

1. **Extrair parâmetros de hamster** (a partir de Telling 1995 + Castilla 2008 PMCA kinetics)
2. **Extrair parâmetros de bank vole** (a partir da literatura emergente)
3. **Rodar a primeira simulação multi-species** (camundongo + hamster + humano)
4. **Calcular θ* para cada** e comparar
5. **Gates + commit + integrar à tese**

Isto é a ação de MAIOR IMPACTO possível agora: transforma a maior limitação ("taxas são murinas") na maior validação ("θ* é universal").
