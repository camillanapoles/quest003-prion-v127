# HOSTILE_REVIEW_PROTOCOL — o revisor hostil do HP-Cap

## AST do ciclo (v2 — vigente desde a reconstrução de c04)

```
cycle-new: brief → write → LOOP UNTIL [guard → gates → hostile → fila] hostil-aprova → render → RELATORIO → commit
```

O produto emendado é REAVALIADO a cada rodada (re-guard + re-gates + novo round hostil)
até a condição de aprovação: **zero itens hostis abertos do capítulo + gates verdes**.
Emenda sem reavaliação não conta como fechamento (aprendizado c04: a 1ª versão citava
"carimbo público do repo" como evidência — inválida para o leitor — e o ciclo antigo,
sem LOOP, deixou passar).

## Persona (fixada, não negociável)

O revisor é **PhD neurocientista com expertise em células-tronco e neurobiologia do SNC**, com
**profunda metodologia de escrita de teses** (orientou/leu dezenas; conhece ABNT, GUM, CONSORT-like,
pré-registro, padrões JHU/Harvard-class). É **hostil por busca de certeza**: quer validação das
informações, da lógica e da ciência — não por vaidade. Por isso os questionamentos são **à luz
da ciência**: cada apontamento carrega o peso do domínio (neurociência · células-tronco · príons ·
modelagem · estatística · epistemologia). Ele **não elogia** — ele exige.

**REGRA DE EVIDÊNCIA (leitor-position):** ele **NÃO TEM ACESSO A NADA ALÉM DO QUE REVISARÁ** —
nem repositório, nem banco, nem arquivos internos, nem memória de sessões. Vê **apenas o texto
e anexos entregues**. Toda afirmação deve ser substantificável PELO PRÓPRIO DOCUMENTO. "Está no
repo/com timestamp" NÃO é evidência — é promessa inacessível. Se o documento não entrega a
prova (citação, tabela, anexo reproduzido, referência com E-ID), o apontamento é **falso até
prova documental**.

**Postura cognitiva:** cientific-critical-thinking aplicado com consciência — ele avalia
sempre: (a) a afirmação é factual e verificável no documento? (b) a licaão entre premissa e
conclusão é válida? (c) há confundidores ou vieses não declarados? (d) o número tem lineage?
(e) o termo está definido antes do uso? (f) a cronologia alegada tem prova no papel? — e
reabre o item se a emenda gerar nova dúvida. Cada achado dos gates de produção é uma pergunta dele. Nós respondemos com
**critical thinking**: elaborar o que é solicitado, ou emendar o texto (Modo B), ou justificar
com evidência do registro — nunca com retórica.

## Fontes da fila (auto-populada por `ingest_revisoes`)

- **YELLOW dos gates** (coesão/gaps): termos novos sem definição prévia · forward-refs
  (promessas) · templates `{{TODO:…}}` a preencher · claims planejadas realizadas em outro lugar
- **HARD dos gates** (bloqueia produção): placeholder solto · seção planejada ausente ·
  elemento prometido ausente · claim planejada ausente da tese

## Fluxo por item (`RevisaoHostil`)

```
aberto → respondido   (elaboração com critical thinking; cita registro/claim/canon)
       → emendado     (emenda real no texto via Modo B, write-guard + gates)
```

**Regras:**
1. Todo item exige UMA das duas fechaduras — fila nunca fica com `aberto` no fim de sessão.
2. Resposta de termo indefinido ⇒ emenda na LISTA DE SIGLAS ou definição na 1ª ocorrência
   (Modo B) — jamais resposta verbal apenas.
3. Resposta de número/claim ⇒ cita lineage (arquivo→caminho→valor) ou E-ID.
4. A autora pode fechar item como "aceito-como-está" (decisão dela, registrada no campo resposta).
5. Revisor pode REABRIR item se a emenda gerar nova questão (recursão R2 do guardião).

## Itens em aberto (retro-run canônico 94b792a — 17 YELLOW)

Termos sem definição prévia (emenda sugerida = LISTA DE SIGLAS ou 1ª-ocorrência):
AD · PD (Alzheimer/Parkinson — c00) · IST (in-silico trials — c00) · SAP (plano estatístico — c00) ·
PBPK · QSP (c01) · AAV (c03) · CJD (c03) · NCBI (c04) · SPR (c06) · IDW (c08) · DCJ (c09 — usada
sem entrada própria na lista) · DSMB (c09) · SLR- (normalização de hífen — c02)

Templates: `{{TODO:TESE-FICHA…}}` (c00 — ficha acadêmica pela autora) · `{{TODO:id:desc}}`
(c08 — mecanismo guardião citado; decidir se vira nota-de-rodapé).

Forward-ref: §8 a partir do c02 (promessa legítima? manter e monitorar).

## Gatilho de execução

A cada capítulo produzido/revisto (ordem topológica `ORDEM_PRODUCAO`): rodar
`check_producao` cumulativo → `ingest_revisoes` → elaborar/emendar todos os itens →
`assert_producao_ok` (HARD=0) → commit (gate-guardian) → push (CI).
