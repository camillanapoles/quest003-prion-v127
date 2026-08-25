# Dashboard vivo — Quest 003 (Diagrama Lógico dos Achados)

## O que é
Visualização do estado do conhecimento da quest 003 (DCJ / PrP-G127V): nós = achados (com status de validação), arestas = conexões lógicas (sustenta / limita / habilita / testa), + painéis de gates, evolução de probabilidades por sessão, tabela de validações e changelog.

## Arquivos
- `data.json` — **fonte única de verdade**. Nada de layout aqui; só conteúdo.
- `index.html` — visualizador (vanilla JS/SVG, offline, sem dependências). Não precisa mexer por atualização de conteúdo.

## Como visualizar
Servir a pasta e abrir `index.html`:
```bash
cd /root/DeepScientist/quests/003/artifacts/dashboard && python3 -m http.server 8137 --bind 127.0.0.1
# → http://127.0.0.1:8137
```
(fetch não funciona sobre file://; precisa do servidor mínimo.)

## Protocolo de atualização por sessão (obrigatório ao fechar qualquer sessão da quest 003)
1. Editar `data.json`:
   - `meta.updated` / `meta.version` → data/hora e versão da sessão
   - nós: promover/rebaixar `status` (`confirmed`/`constraint`/`refuted`/`proposed`/`active`), atualizar `prob`, `updated`, `delta` (`up`/`down` marca ▲▼)
   - arestas: adicionar conexões novas
   - `probability_history`: acrescentar ponto datado no componente (não sobrescrever o anterior — a história É o conteúdo)
   - `gates`: mover status/tone (`ready`/`wait`)
   - `changelog`: entrada nova no topo (reverse-chron é feito pelo viewer)
2. `git add -A && git commit` no repo da quest (auditoria do delta)
3. Servir + conferir renderização antes de reportar (verify-before-reporting)

## Convenções de status
| Status | Significado | Cor |
|---|---|---|
| confirmed | validado por literatura/experimento | verde ✓ |
| constraint | verdadeiro, mas com condição estruturante | âmbar ⚠ |
| refuted | refutado — corrigido ou removido do desenho | vermelho ✕ |
| proposed | proposto, aguarda teste (gera gate) | azul ⏳ |
| active | em curso / desenho ativo | roxo ▶ |
