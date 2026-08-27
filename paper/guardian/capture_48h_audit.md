# Auditoria de Captura 48h — Proveniência e Consolidação (2026-08-24 22:00 → 2026-08-27 01:13 UTC)

**Motivo:** suspeita (confirmada) de docs/dados misturados entre `/root` e `/workspace` durante as iterações paralelas do paper. Varredura completa: 521 arquivos em 9 grupos.

## Veredito

Não há **divergência de dados** — há **cópias paradas (stale checkouts)** de um único repositório + material de evidência fora do repo. Todos os artefatos numéricos críticos são **hash-idênticos** entre cópias. A fonte única permanece o repo canônico.

## Grupos e destino

| # | Local | N≈ | Diagnóstico | Ação |
|---|---|---|---|---|
| A | `/root/DeepScientist/quests/003` (branch `paper-v5`) | 156 | **REPO CANÔNICO** — fonte única, git, auditável | MANTER (source of truth) |
| B | `/workspace/quests/003` | 101 | Checkout antigo @85373a7 (linha canônica, commit antigo) | DELETAR (pendente confirmação) |
| C | `/workspace/003` | 77 | Checkout antigo @5d6e698 ("preprint v4.2" paralelo, superseded) — continha **authorship formal** (recuperado ✓) | DELETAR após extração (feita) |
| D | `/workspace/colab_ws8/` | 8 | Artefatos de execução Colab: **ws_9_v4_human.json ORIGINAL** (hash `31f02e13…` = idêntico ao canônico — cadeia Colab→repo íntegra), scripts ws_8/ws_9, notebook LaTeX | MANTER como proveniência bruta de execução |
| E | `/workspace/igel2024/` | 4 | **Fulltext do kernel (E009/Fornara-Igel 2024) + página Zenodo** — material de estudo/verificação | MANTER **privado** (copyright: NÃO entra no repo público; manifest registra "full text inspected") |
| F | `/workspace/projects/quest003-graph/` | 9 | Snapshot graphify v3 (36 nós, 25/08) — histórico; grafo atual = `artifacts/dashboard/data.json` (43 nós, hash `f55fa6f5…` idêntico em A/B/C) | MANTER como snapshot histórico |
| G | `/workspace/quests/{001,002}` | 125 | Outras quests (fora do escopo 003) | FORA DE ESCOPO |
| H | `/workspace/{ws10,salad,live-monitor}` | ~5 | Workstreams paralelos (SaladCloud WS-10, monitor) | MANTER |
| I | `/root/{tools,.config,session-state.md,…}` | ~10 | Infra (tectonic 0.15.0 ✓, colab-cli, estado de sessão) | MANTER |

## Verificação de integridade (evidências centrais)

| Artefato | Hash (sha256, 12) | Cópias | Status |
|---|---|---|---|
| `ws_9_v4_human.json` (θ*=0.333) | `31f02e13485a` | colab_ws8 (origem Colab 23:02) = canônico (23:48) | ✅ cadeia íntegra |
| `bayes_success.json` (36.6%/5.0%) | `7769cc652ba2` | A = B = C | ✅ idêntico |
| `data.json` dashboard (43 nós) | `f55fa6f5ea9f` | A = B = C | ✅ fonte única confirmada |

## Recuperações desta auditoria

1. **Authorship formal** (do commit 5d6e698, pipeline arquivado): Camilla N., correspondente; CRediT: conceptualization, methodology, software, investigation (simulations), writing (original draft); verificação humana das 5 refs críticas registrada; funding none/Colab-free-tier; sem COI; sem patentes → portado para `evidence_workspace/authorship.json` com nota de proveniência.
2. **Licenças** registradas no mesmo commit: MIT (código) / CC-BY (dados) → reutilizar nas declarações do v5.
3. **Cadeia de custódia WS-9**: JSON original gerado no Colab pela autora (23:02) → commit no repo (23:48) — sem mutação.

## Regras decorrentes

- R1: nenhuma nova cópia de trabalho da quest em `/workspace` — todo trabalho de paper em `/root/DeepScientist/quests/003` (branch).
- R2: fulltexts de publishers (`igel2024/`) ficam FORA do repo público — o manifest registra a inspeção, não republica o PDF.
- R3: outputs de execução vêm SEMPRE com o JSON de origem (regra já vigente: "nunca digitar valores").

*Gerado por captura find(1) com -prune de venv/git/pycache; lista bruta: `/workspace/capture_48h.txt`.*
