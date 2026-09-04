# RELATÓRIO — escrita do zero · RODADA 2 (branch tese-escrita-zero)

Progresso: **c01–c13 ✓ aprovados (13/17)** · restam: c14 refs → c15 anexos → c16 mapa → c00 front-matter
(NESSA ORDEM). DB: tese_v2.db · render: 13 arquivos em escrita-zero/render/

| Cap | Título | Hostil |
|---|---|---|
| c01 | Nota à banca | 5 Qs (3 emendas, 2 respostas) |
| c02 | Introdução (contrato OE1–4/H1–3/M1–M5) | 5 Qs + 7 stale |
| c03 | Fundamentação (mapa em camadas) | 4 Qs + 5 stale; A0003 executada |
| c04 | Base comum/ponte (linha experimental) | 5 Qs + 12 stale; A0005 criada |
| c05 | Alicerce M3 (invariância θ*, horizonte) | 4 Qs + 9 stale |
| c06 | Produto M2 (dose [SIM], G0-wet, S1) | 4 Qs + 17 stale |
| c07 | Métodos (P0–P6, Base de Validade, análogo) | 3 Qs + 5 stale |
| c08 | Resultados (M1–M5 como resultados) | 3 Qs + 6 stale; A0006 criada |
| c09 | Achados (contenção+restauração, AD/PD) | 2 Qs + 5 stale |
| c10 | Discussão (significa/não-significa) | 2 Qs + 2 stale |
| c11 | Leitura clínica 10-min | 2 Qs + 2 stale; 3 openers G2 ✓ |
| c12 | Limitações (limite↔fecho) | 1 Q + 1 stale |
| c13 | Conclusões (veredito OE1–4+H1–3) | 1 Q + 1 stale (ciclo via /start após submit — lição) |

**AÇÕES DEVEDORAS pendentes (bloqueiam o local):**
- A0001@c15 folhas de pré-registro + versão do motor/solver com datas impressas
- A0002@c00 LISTA DE SIGLAS consolidada (+ FICHA — EXCLUSIVA da autora)
- A0005@c15 folha de versão do exp1 (originada em c04 §4.2)
- A0006@c15 conferir cobertura do anexo: pré-registros, validação tabela-mãe, versão exp1, F1–F10
- (A0004@plano: refinar mapeamento brief — não bloqueia capítulo)

**Continuação (próxima sessão):** subir API (`python -m thesis_engine.cli serve --db tese_v2.db`),
seguir c14→c15→c16→c00 com o ciclo de sempre: /start ANTES do submit → sync fila SEM restore →
fechar stale → registrar Qs hostis tipo='hostil' → emendar/responder → /status → /approve → render → commit.
c15 precisa executar A0001/A0005/A0006 com evidência (fechar_acao) para aprovar; c00 executa a
LISTA de siglas (A0002) mas a FICHA fica para a autora. Bootstrap NÃO rodar de novo (preservaria
DB, mas arquivaria render/briefs).
