# Search Log — Quest 003 (consolidação retrospectiva declarada)
**Data de consolidação:** 2026-08-27 · **Executor:** agente (busca web assistida), sessões 24–27/08/2026
**Natureza (declaração de honestidade):** as buscas foram executadas por agente em sessões de trabalho; os transcripts brutos (paginação de resultados) **não foram retidos**. Este log consolida, retrospectivamente, as queries e intenções conforme documentadas em `plan.md` (rede de 12), `evidence_table.md` (blocos A–I), `refs_audit.md` (24 refs auditadas) e registros de sessão. Cada linha indica a fonte do registro. Queries exatas string-por-string não são reconstituíveis — declarado como limitação de reprodutibilidade (guardian E-10 parcialmente fechado: o mapa de busca é auditável; o transcript bruto não existe).

## 1. Rede fundacional (12/12 válidas — registrada em plan.md, 24/08)

| # | Query/intenção | Bloco alimentado |
|---|---|---|
| 1 | Asante 2015 G127V Nature (resistência transgênica) | A |
| 2 | Mead 2009 kuru NEJM (seleção G127V) | A |
| 3 | PRNP ASO sobrevida camundongos | B |
| 4 | PRN100 humano (primeira aplicação) | B |
| 5 | Mallucci 2003/2007 depleção de PrP | B |
| 6 | NSC transplante em príon | C |
| 7 | CED refluxo de cânula | D |
| 8 | diversidade de cepas × V127 | A/E |
| 9 | RT-QuIC diagnóstico precoce | F |
| 10 | NSC humano fase 1 | C |
| 11 | DCJ iatrogênica por instrumentais | D (biossegurança) |
| 12 | ASO first-in-human 2023+ | B |

## 2. Blocos da evidence_table (intenções de busca por bloco)

| Bloco | Tema | Fontes resultantes registradas |
|---|---|---|
| A | fundamento molecular G127V | E001, E002, E005, E006 (+estruturais) |
| B | negação de substrato (classe terapêutica) | E004-contexto, ION717, Mallucci, Raymond |
| C | terapia celular em príons | E012, E016, E020, transplantation refs |
| D | entrega cirúrgica (CED/DTI/biossegurança) | Krauze 2005, Elder/Lonser 2025 |
| E | limites biológicos (SVZ, linhagens) | E013, E014, E015 |
| F | atualizações 25/08 (pendências fechadas) | E019, E024, E029-contexto |
| G | adendo externo (refs adjudicadas) | ver refs_audit (11 corretas/3 dup/1 não-cient/1 errada) |
| H | correção micróglia (HSC→microglia) | Shibuya 2022, Colella 2024 (adjudicadas) |
| I | "este experimento já existe?" (novidade do G0) | conclusão: plataforma existe (Groveman), agente V127 nunca entrou em organoide |

## 3. Auditoria de referências (24 linhas em refs_audit.md, 25/08)
Lote de 19 referências de documento externo auditadas individualmente: 11 corretas, 3 duplicatas, 1 documento de política não-científico, 1 link apontando para paper não-relacionado — registro completo em `refs_audit.md`.

## 4. Elevações posteriores (data + identificador confirmado)

| Data | Busca | Resultado registrado |
|---|---|---|
| 26/08 | kernel reação–difusão príon código aberto | E009 (PMID 39717079; Zenodo 11093945) |
| 26/08 | fulltext Fornara/Igel para port | /workspace/igel2024 (privado; copyright) |
| 27/08 | as 5 falhas clínicas (E-02) | E034–E038 (PMIDs/DOI confirmados) |

## 5. Limitação declarada
Reprodutibilidade estratificada: (i) **reprodutível** — cada fonte do registry é aberta e re-buscável pelos identificadores; (ii) **não-reprodutível exatamente** — a sequência de queries como strings (agent sessions não retêm transcript). Para auditoria de citações futuras, a prática recomendada é log estruturado no momento da busca (adoção declarada como padrão a partir de agora).
