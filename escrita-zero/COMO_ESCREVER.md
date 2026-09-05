# COMO ESCREVER UM CAPÍTULO — cartão de bolso (leia antes de escrever)

## O FLUXO (é SEMPRE isto, sem exceção):

```bash
# 1. PEGUE O BRIEF (o banco te diz o que escrever)
.venv/bin/python -c "
from thesis_engine.escritor import brief_capitulo, save_brief, V2_DB
b = brief_capitulo(V2_DB, 'c01')       # troque c01 pelo capítulo
save_brief(V2_DB, 'c01')                # salva em escrita-zero/briefs/
for c in b['claims']: print(f\"  {c['id']}: {c['texto'][:80]}\")
print('OBJETIVO:', b['objetivo'])
print('TÓPICOS :', b['topicos'])
"

# 2. ESCREVA O TEXTO NOVO (num arquivo .md — VOCÊ escreve, do zero)
#    → rascunhos/c01_nota_banca.md
#    → cada afirmação factual TERMINA com [claim:Cxxx] [evidence:Exxx]
#    → números: SEMPRE dentro de claim (nunca digitados soltos)
#    → cronologia/precedência: sempre "no próprio documento" (nunca "está no repo")

# 3. INGESTIONE NO DB
.venv/bin/python -c "
from thesis_engine.escritor import reingest_capitulo, V2_DB
from pathlib import Path
r = reingest_capitulo(V2_DB, 'c01', Path('rascunhos/c01_nota_banca.md').read_text())
print(r)
"

# 4. LOOP (repita até hostil_aprova == True)
.venv/bin/python -c "
from thesis_engine.escritor import hostil_aprova, V2_DB
r = hostil_aprova(V2_DB, 'c01')
print(r)
# se aprova=False: leia o que falta, EMENDE o rascunho, re-ingestione (passo 3), re-teste
# se aprova=True:  siga para render
"

# 5. RENDER (só após aprovação)
.venv/bin/python -c "
from thesis_engine.escritor import render_v2, V2_DB
print(render_v2(V2_DB))
"

# 6. COMMIT
git add -A && git commit -m "feat(escrita-zero): cNN — descrição"
```

## O QUE NÃO FAZER (JAMAIS):
- ❌ NÃO olhe commits antigos para "buscar texto" — o texto vem do BANCO (brief)
- ❌ NÃO copie/rascunhos antigos — escreva prosa NOVA
- ❌ NÃO digite números sem [claim:] — lineage é obrigatória
- ❌ NÃO diga "está no repo com timestamp" — o leitor da tese NÃO TEM repo
- ❌ NÃO pule o LOOP — sem hostil_aprova, sem render
- ❌ NÃO preencha a ficha acadêmica — é EXCLUSIVA da autora

## LINGUAGEM HUMANA (regra da autora):
Escreva como uma **doutoranda brasileira** escreveria — não como um modelo de linguagem.
O gate de estilo agora BANE (lista completa em `integrity.py _TERMONS_LLM`):
```
verbatim · delve · furthermore · moreover · notably · comprehensive · robust ·
multifaceted · nuanced · holistic · leverage · seamlessly · elucidate ·
unprecedented · myriad · plethora · whilst · amongst · notwithstanding
```
**Se o revisor hostil lê um termo que soa "de máquina", ele QUESTIONA:**
*"que doutoranda brasileira escreve assim? Reescreva em linguagem acadêmica natural."*
