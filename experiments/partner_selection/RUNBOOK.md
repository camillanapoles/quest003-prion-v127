# RUNBOOK DE EXECUÇÃO — Seleção de Parceiro (instrumento replicável, análogo PRISMA)
## Quest 003 · Parte 2 · artefato 2.5-b · v1 · 2026-08-27
**Tese-claim que este runbook materializa:** a seleção de laboratório é um ATO METODOLÓGICO documentado — assertividade **por método**, replicável por qualquer pesquisador posterior (como o fluxo PRISMA torna a seleção de artigos reproduzível). Cada passo abaixo gera registro; o registro É a tese.

## 0. Fluxo (PRISMA-análogo, 5 estágios)
```
IDENTIFICADOS (fontes §1 do protocolo)          n=?
   └─ TRIAGEM I1–I5 (binária, evidência pública)  → excluídos: motivo X# registrado
        └─ ELEGÍVEIS PONTUADOS (8 eixos, pesos congelados §4) → candidates.csv
             └─ CONTATADOS (sequencial maior→menor; kit B1 v2.1) → contacts_log
                  └─ SELECIONADO (GATE-F: F1–F10 + assinatura PI) → decision_log
```

## 1. Procedimento por etapa (o que o executor faz, passo a passo)

**ETAPA A — Identificação (20 min):** varrer as 5 fontes do protocolo §1; para cada lab novo, registrar linha em `candidates.csv` com coluna `source` (E-ID/página/evento). Nenhuma exclusão ocorre aqui.

**ETAPA B — Triagem binária (15 min/lab):** para cada critério I1–I5, registrar `evidence` = evidência pública verificável:
| Critério | Evidência aceita (padrão de prova) |
|---|---|
| I1 plataforma organoide-príon | artigo peer-reviewed do PRÓPRIO lab infectando/tratando organoide (ex.: E007/E008 para RML) |
| I2 príon infeccioso/BSL3 | publicação com isolates sCJD OU declaração institucional oficial |
| I3 capacidade ≥64 organoides | declaração do PI por e-mail OU evidência de estudo próprio ≥48 organoides |
| I4 aceita pré-registro+kill | **só por resposta escrita do PI** (não inferir) |
| I5 formalização ≤6 meses | resposta escrita / histórico de acordos |
Regra de honestidade: sem evidência → `?` (não pontua, não exclui; vai para "verificar no contato").

**ETAPA C — Pontuação (10 min/lab elegível):** aplicar âncoras 0–5 do protocolo §4 por eixo; score = Σ(eixo×peso)/5. Registrar a LINHA DE RACIOCÍNIO em uma célula `rationale` (frase por eixo). Single-rater declarado; segunda ratificação = TODO quando houver pessoa.

**ETAPA D — Contato sequencial:** 1º colocado → kit B1 v2.1 personalizado; janela 15 dias; follow-up único +15; sem resposta → próximo. Registro em `contacts_log.csv` (data, canal, resposta, próximo passo).

**ETAPA E — Decisão:** selecionado entra no GATE-F (freeze checklist F10); decisão + rationale em `decision_log.md` (público). Nenhum elegível → Plano B documentado (protocolo §4).

## 2. Instrumentos máquina-verificáveis (no repositório)

| Arquivo | Esquema |
|---|---|
| `candidates.csv` | `lab_id, nome, pais, source, I1…I5 (✓/✗/?+evidence), A…H (0–5 ou vazio), score, rationale, excluido_por, data` |
| `contacts_log.csv` | `lab_id, data, canal, kit_versao, resposta, pendencia, proxima_acao` |
| `decision_log.md` | entrada datada por decisão, com réplica (este runbook é contestável: réplica methodológica = rodada R3) |

## 3. Critérios de replicabilidade (o que torna isto PRISMA-grade)
1. Critérios/pesos/vetos congelados por commit ANTES do primeiro contato (já feito — protocolo v1 @4853c58).
2. Toda pontuação cita evidência pública (E-ID/URL/declaração escrita) — zero impressão não registrada.
3. `?` é estado legítimo e visível (não pontua, não exclui) — anti-invenção.
4. Sequência de contato determinística (maior→menor; desempate eixo A).
5. Log completo público; recusa/mudança de critério pós-início = emenda auditada (commit + justificativa).

## 4. Estado atual do instrumento
- `candidates_v1.csv` seeded com os 4 públicos (RML, Calgary, USP-hub, LNP-rede) — só campos com evidência E-registry preenchidos; `?` marcado onde exige contato.
- Executor(a) do fluxo: autora (contatos) + agente (registro/triagem documental) — papéis declarados.
