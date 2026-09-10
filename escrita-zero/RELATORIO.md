# RELATÓRIO — escrita do zero · RODADA 3 (FINAL) — branch tese-escrita-zero

**STATUS: 17/17 capítulos escritos do zero, aprovados, renderizados e commitados.**
DB: tese_v2.db · render: 17 arquivos em escrita-zero/render/ · produção cumulativa: 17/17 gates verdes, HARD=0, fila hostil zerada.

## Rodada 3 (esta sessão): c14 → c15 → c16 → c00

| Cap | Conteúdo | Rodada hostil |
|---|---|---|
| c14 | REFERÊNCIAS — 58/58 fontes em ABNT geradas do registro por `escrita-zero/gen_c14_refs.py` (zero digitação; et al. preservado; ordenação alfabética; [s.d.] sem data; URLs/PMID como localizador) | 3 itens: et al. descartado (EMENDADO) · intro prometia forma ABNT completa + "verificadas uma a uma" (EMENDADO) · URL truncada E029 (respondida → ação A0007) |
| c15 | APÊNDICE A — inventário com datas+commits impressos (`gen_c15_anexo.py`): A.1 pré-registros · A.2 motor/solver · A.3 folha de versão do exp1 (promessa c04 §4.2 cumprida) · A.4 F1–F10 · A.5 validação da base · A.6 concordância 60×fontes com TEXTO INTEGRAL · A.7 pendências | 2 itens: concordância truncada (EMENDADO — texto integral) · datas sem hash (EMENDADO — coluna Commit) · ações A0001/A0005/A0006/A0007 fechadas com evidência |
| c16 | APÊNDICE B — mapa da lógica: B.1 fluxo literatura→conclusão (diagrama + instrução de auditoria) · B.2 dez decisões-chave · B.3 quatro rejeições · B.4 glossário · B.5 seis objeções da banca respondidas | 3 itens: âncora C060/E032 errada (EMENDADO — 32/32 pares conferidos) · sinônimo novo "capa" (EMENDADO) · instrução de auditoria implícita (EMENDADO) |
| c00 | Front matter: RESUMO + ABSTRACT (âncoras verbais) · SUMÁRIO · LISTA DE SIGLAS (27 entradas, colhidas do corpo) | 3 itens: nota do sumário entre parênteses (EMENDADO) · falta ficha/rosto (POR REGRA — exclusiva da autora) · "etrization" sem sinalização (EMENDADO) · A0002 fechada (LISTA executada; FICHA da autora) |

## Regressões pegas na checagem cumulativa final (e corrigidas)
- CD47 e FK506 cruzaram o limiar de recorrência com os textos integrais do c15/c16 → adicionados à LISTA DE SIGLAS do c00 (coesão 17/17).
- C051 planejada p/ c06 realizada em c08 → registrado H0130 e respondido (esperado por desenho: desenho no 6, resultado no 8).
- Teste `test_aprova_bloqueada_por_acao_pendente_no_local` atualizado para fase-consciente (c15 aprovado ⇒ nenhuma ação pendente nele).

## PENDÊNCIAS EXCLUSIVAS DA AUTORA (fora do alcance do escritor)
1. **FICHA** (folha de rosto, ficha catalográfica, agradecimentos) — c00 está com resumo/sumário/siglas; a ficha é da autora.
2. **E029**: URL truncada no registro canônico (New Scientist) — completar o registro OU manter a nota do Apêndice A.7.
3. **GATE-F**: assinatura da PI do laboratório parceiro + execução do fluxo de seleção (F10) — dormentes por design até haver parceiro.
4. **Compilação final**: paginar (sumário diz "a numeração acompanha a versão compilada") e gerar PDF/Word para depósito.

## Estado técnico
- Geradores determinísticos commitados: `escrita-zero/gen_c14_refs.py`, `escrita-zero/gen_c15_anexo.py`.
- Testes: 73/73 passando (gate-guardian verde).
- API: `python -m thesis_engine.cli serve --db tese_v2.db` (mantida no ar nesta sessão).
- Ações devedoras: 7/7 fechadas (A0001–A0007 executadas ou por regra).
- Wiki: observações de progresso gravadas em cada rodada.

---

## RODADA 4 — recomeço do zero (2026-09-10): c01 reescrito e aprovado

- **Bootstrap V2 fresh** (rodada-3 arquivada em `arquivo/rodada-20260909-2241` e `-2244`): DB zero, 60 claims, 37 regras de estilo, 7 perguntas do hostil, 4 ações semeadas.
- **c01 NOTA INTRODUTÓRIA À BANCA**: prosa nova do zero (`rascunhos/c01_nota_banca.md`, 21 blocos D0001–D0021) — vazio terminológico · 3 camadas semânticas do radical (consonância intencional, honestidade filológica) · definição operacional C054 · base real C004/C005/C006/C007/C027 · tabela 3 colunas de contraste · analogia do átomo re-enquadrada como interpretativa.
- **Round hostil: 6 itens (H0009–H0014), 5 emendados + 1 respondido** — glosses PrP/GPI/AAV/E200K na 1ª ocorrência; analogia declarada interpretativa; quark como apropriação deliberada; promessas forward mapeadas (P1/P3/P4→c07/anexo; ponta-a-ponta→c08); contraste de definição não de mérito; "nenhum dado inventado" verificável pelas tags.
- **Aprovação: gates 3/3 (objetivo·coesão·gaps) · hostil_falou=True · 0 abertos · 0 ações pendentes → approved → render 21 blocos.**
- **Débitos de engine observados nesta sessão (pré-existentes, não causados pela rodada):** (1) `cli status|check` sem `--db` aponta para `thesis.db` (V1) e crasha após `bootstrap_v2` (quick-start do AGENTS.md quebra em clone fresco); usar `--db tese_v2.db` ou corrigir default. (2) pytest 4 falhas de fixture isolation (test_plano_grafo c17 só-no-plano) — documentadas no AGENTS.md.
- **Próximo capítulo: c02 introdução.**

## RODADA 4 (cont.) — c02 introdução aprovado

- **c02 INTRODUÇÃO** (`rascunhos/c02_introducao.md`, 20 blocos D0022–D0041): contrato formal completo — Q1–Q3 · OE1–OE4 · H1–H3 · tabela-mãe M1–M5/R1 (validada pela autora) · 23 claims com lineage (C001–C015, C022–C023, C032, C037, C040, C043–C044, C046, C049–C052).
- **Round hostil: 6 itens (H0015–H0020), 3 emendados + 3 respondidos** — C050 movida ao ponto da negativa universal (§2.1); validação-da-autora respondida (voz da tese + cronologia em anexo); artefatos da tabela respondidos (conteúdo/ligeagem no Apêndice A); ligação OE4↔H3 justificada pela cláusula de continuidade; gloss GATE-F/F1–F10; «commitado»→«registrado».
- **Aprovação: gates 3/3 · hostil_falou ✓ · 0 abertos → approved → render (41 blocos acumulados).**
- **Próximo: c03 fundamentação (plausibilidade, C001–C023, H3/berth).**

## RODADA 4 (cont.) — c03 fundamentação aprovado

- **c03 FUNDAMENTAÇÃO** (`rascunhos/c03_fundamentacao.md`, 14 blocos): gargalo em 6 camadas (genética→estrutura→cultura→entrega→organoide→clínica-BR) · família antecipatória + regras de desenho C033-C035/C042 · posicionamento H3 com enquadramento bayesiano C036 · fundamento epistemológico C038/C039/C045/C051 · síntese C046-C049 · **Figura 1** (mapa em camadas, especificada em legenda; render via pipeline CI).
- **Round hostil: 5 itens (H0021–H0025), 2 emendados + 3 respondidos** — glosses HLA/CD47/NK; taxonomia da família respondida (conceitual, nunca fabricar citação); figura respondida (especificação + pipeline); C038 2,1×-semente respondido (reporta, não interpreta — c05 formaliza); estilo numérico uniformizado (%).
- **Ação devedora A0003 executada**: C027 citada na camada clínica brasileira §3.1 + mapa em camadas (Figura 1).
- **Aprovação: gates 3/3 · 0 abertos · 0 ações no local → approved → render 55 blocos acumulados.**
- **Correção de rodada**: c02 «promissor» (banido) → «mais forte», re-aprovado (9799db5) — o gate de estilo fica pulado no modo campanha; auditoria manual de termos agora faz parte do ciclo por capítulo.
- **Próximo: c04 linha-experimental (a ponte: base comum + M3→M2 + cronologia honesta).**
