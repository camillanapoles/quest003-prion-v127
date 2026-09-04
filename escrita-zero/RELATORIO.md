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
