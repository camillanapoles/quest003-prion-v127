# G0 UNLOCK DOSSIER — Argumentário para Liberação do Gate Organoide
## Documento de submissão a comitê de ética/parecer científico (CEP/parceiro B1) · v1 · 2026-08-27
**Natureza:** PLAN_DOC (faixa de planejamento — fora dos gates de manuscrito por desenho). Este dossier NONA o que o comitê precisa para decidir; a decisão permanece do comitê. Toda cifra aqui vem de artefatos auditados do repositório público (regra: nenhum número sem JSON/claim).

---

## 1. O QUE SE PEDE

Liberação para execução do **G0 — gate organoide humano, 8 braços, n=8–12/braço** (protocolo `experiments/g0_protocol.md`): primeiro experimento wet-lab do programa de contenção V127ΔGPI para DCJ. Sem intervenção em humanos; material: organoides cerebrais humanos derivados de iPSC infectados com isolados sCJD (plataforma publicada — Groveman et al. 2019/2021 [E007/E008]).

## 2. POR QUE G0 ESTÁ PRONTO AGORA (a base que desbloqueia)

O programa chega ao comitê com o **gate computacional G0-sim EXECUTADO E PASSADO** (§3.5 do manuscrito v5; claim C046):
1. **Thresholds pré-registrados ANTES da execução** (release v1.0, timestamped): T1 replicação, T2 contenção mínima, T3 informativa — todos passos; θ*=0.333; consistência emergente MV2>MV1 sem fitting.
2. **Kernel parametrizado publicado** (Fornara/Igel 2024, código aberto, Zenodo 11093945 [E009]) ancorado a **dados organoide humanos** (relógio e amplitude; Groveman [E007]) — revisão sistemática de 9 blocos com citações verificadas uma a uma.
3. **Self-tests numéricos** (conservação de massa 100%; erro Thiele 0,5%) e **solvers reproduzíveis** (JSONs de resultado commitados).
4. **Quadro probabilístico honesto**: P(G0 informative-go)=36,6% [CrI 14,6–60,5]; P(desaceleração clínica)=5% empírica / 30–45% condicional — ambos rotulados; o comitê vê exatamente a mesma incerteza que os autores.
5. **Achados computacionais usados COMO RESULTADO no seu tier**: não substituem validação biológica — **reduzem o risco de o experimento ser desperdiçado** (cada braço testado contra predições quantitativas travadas, não contra expectativa qualitativa).

**Argumento de relevância para liberação:** nenhum dos seis candidatos antipriônicos que chegaram à clínica dispunha de modelo quantitativo de entrega, correção sistemática de literatura ou thresholds pré-registrados. O G0 chega com os três — o que eleva a probabilidade de que recursos, animais-zero (organoide, sem uso animal) e tempo do comitê retornem informação decisiva, seja confirmação (θ_obs<0,33) seja refutação publicável (kill-switch programático pré-declarado).

## 3. O QUE O COMITÊ RECEBE JUNTO (pacote de garantias)

| Garantia | Artefato |
|---|---|
| Pré-registro imutável das predições | release v1.0 + §2.5; auditoria git |
| Definição operacional do estimador (anti-circularidade) | §2.7 (θ_obs: scorer cego, grade κ, função-objetivo, IC bootstrap) — freeze antes do 1º organoide |
| Plano estatístico completo | Welch/Holm 5 comparações; n=8→12; poder ~80% para Δ≥50% (§2.5) |
| Cegamento + randomização por lote | §2.5 + checklist de execução |
| Biossegurança príon | WHO 134°C/NaOH; cânula single-use; necropsia contida (§6) |
| Controle positivo publicado | braço A8 pentosan-polissulfato (Groveman 2021 [E008]) — valida o ensaio por si |
| Kill-switch programática | se nenhum gradiente em nenhum braço E θ_obs>0,33 ⇒ programa encerra e negativo publica (§2.5) |
| Reprodutibilidade integral | código+params+outputs no repo público (MIT/CC-BY) |
| Sem conflito, sem promessa clínica | declarações §6; endpoints contenção/desaceleração apenas |

## 4. LADDER DECLARADA (o que G0 NÃO é)

G0 valida contenção em organoide infectado — **não** autoriza inferência clínica nem uso compassivo. A escada review→simulação→organoide→clínica permanece rotulada degrau a degrau; o dossier pede exatamente o degrau que lhe corresponde.

## 5. CHECKLIST DE SUBMISSÃO (uso prático)

1. Protocolo G0 (8 braços, GO/NO-GO) — anexo `experiments/g0_protocol.md`
2. Este dossier + manuscrito v5 (preprint) + links do repo
3. Termo do lab parceiro (plataforma organoide; B1: USP > Butantan > Einstein — pacote `paper/lab_outreach_package.md`)
4. Plano de comunicação (§6: sem promessas; enquadramento probabilístico aos familiares)
5. Pós-aprovação: freeze do θ_obs estimator + checklist cegamento → primeiro organoide

*Atualizado por guardião/evolução 5. Referência de continuidade: THESIS_ROADMAP_2028.md (janela 2026 Q4: "G0-wet em produção").*
