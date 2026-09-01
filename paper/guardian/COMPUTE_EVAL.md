# COMPUTE EVAL — Alocação de recursos computacionais (com números medidos, não opinião)
## PLAN_DOC · 01/09 · decide a topologia do P-024 · calibração: wall_s do próprio S3 (local 229s/braço vs GHA 72s/braço = **3,2×**, n=9/n=2, medido)

## §1 · Matriz de recursos (medido/teórico → veredito)

| Recurso | Dado | Papel no P-024 | Veredito |
|---|---|---|---|
| **Termux local** | 229s/braço; phantom-killer mata bg a cada ~8 min (3 mortes no S3) | dev/checkpoint/paridade C0 | **backup** — nunca produção |
| **GHA single-job** | 72s/braço (medido); free 2000 min/mês (repo privado); cap 6h/job | produção atual (S3 provou: run 33459375823) | ✅ **via atual** |
| **GHA matrix (5 espécies paralelas)** | mesmo custo total, wall = max(job) | P-024: ~150 runs ÷ 5 jobs ≈ **36 min/job** | ✅ **RECOMENDADO p/ P-024** |
| **Cloudflare Workers** | tokens existem (`~/.cloudflare/{token,mesh-token}`) | NÃO-compute: port V8/Pyodide quebraria motor-exato/paridade C0 (numpy-Pyodide 2-5× mais lento; CPU 30s-5min) | ⛔ motor · ○ orquestração/webhook de dispatch (opcional, valor marginal) |
| **SaladCloud / Modal / RunPod (GPU)** | motor numpy single-thread → GPU = ganho ZERO sem reescrita | só p/ **motor v6 pós-REPARAM** (port cuPy + parity-gate PRÓPRIO; predições v1.0 jamais rodam em motor portado) | ⏸️ **deferido ao v6** — chave GPU não existe no projeto (CF ≠ GPU); solicitar à autora SE v6 aprovado |
| **Colab** | histórico (era S1/S2) | fallback manual | ○ contingência |

## §2 · Topologia do P-024 (travada por este doc)

1. Workflow `p024-multispecies.yml` com `strategy.matrix: species=[mouse,human,hamster,vole]` (rat=controle declarado sem run; yeast=escopo freeS-only opcional).
2. Cada job: restaura seed `species_params.json` → rota κ-sweep {1,5, 2, 3, 4, 8} × pontos de banda (human 3, hamster 3, vole 3, mouse 1) × **2 pareamentos** (livre+tratado) → checkpoint-artifact por job (padrão S3).
3. **Spec de validade embutida** (audit E-S3-01/04/05): escape como FLAG (não raio) · pareamento duplo · registrar total0/totalf + slope final do raio · braços log-espaçados quando banda>2×.
4. Veredito pelos Cenários A/B/C pré-registrados + **predição do hamster** comparada ao release (species_params.json).
5. Custo: ~150 runs × 72s ≈ 3h-runner total ≈ 36 min de wall em matrix — dentro do free-tier; billing privado não bloqueia jobs leves (provado 5× verde).

## §3 · Regras herdadas
Motor v4 EXATO intocado em toda via atual · números só de JSON · paridade C0 em cada job (baseline antes de braços) · CF=orquestração-only · GPU=só-v6-pós-REPARAM.
