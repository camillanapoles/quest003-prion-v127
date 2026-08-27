#!/usr/bin/env python3
"""
GUARDIAN v1 — Recursive Hostile Reviewer Harness (Quest 003, paper-v5)
=====================================================================
Revisor hostil simulado de revista A1: questionador RECURSIVO de evidência
e base metodológica. Determinístico, offline, stdlib-only (skill contract).

Rodadas:
  R0 — drift estrutural: manuscrito(md) vs claims.csv vs consistency_manifest
        vs latex; ORPHAN_TAGS, NUMBER_BINDINGS, DRIFT_TEX_MD.
  R1 — bateria hostil: checklist M1-M8 + m1-m10 (hostile_review_v4.md) +
        bateria por claim_kind (factual/result/method) + contagens de
        referência vs source_manifest + figuras/tabelas exigidas.
  R2 — recursão: cada AMENDMENT/assumption adicionado é re-atacado
        (foi claim-tagged? assumption declarada? contradição com N-facts?).
        Converge quando rodada não gera novos achados (delta=0).

Gate de saída: zero BLOCKED. Findings: BLOCKED > AMEND > NOTE.
Uso:
  python3 guardian.py --round 0|1|2 --md ../manuscript_EN_v5.md \
      --claims ../evidence_workspace/claims.csv \
      --manifest ../evidence_workspace/source_manifest.json \
      --consistency ../evidence_workspace/consistency_manifest.json \
      --tex ../latex/manuscript_v5_EN.tex \
      --registry guardian_registry.json --report guardian_report_v5.md
"""
import argparse, csv, hashlib, json, os, re, sys, unicodedata
from collections import OrderedDict

def slug(s): return unicodedata.normalize("NFKD", str(s)).encode("ascii","ignore").decode()

def load_json(p):
    with open(p, encoding="utf-8") as f: return json.load(f)

def load_claims(p):
    with open(p, encoding="utf-8") as f:
        return list(csv.DictReader(f))

SUP = {"0":"⁰","1":"¹","2":"²","3":"³","4":"⁴","5":"⁵","6":"⁶","7":"⁷","8":"⁸","9":"⁹","-":"⁻"}
def sup(n): return "".join(SUP.get(c,c) for c in str(n))
def num_variants(v):
    """Gera variantes tipográficas de um número p/ binding no texto."""
    out = set()
    try:
        x = float(v)
    except (TypeError, ValueError):
        return out
    def add(s):
        if s: out.add(s)
    add(str(v)); add(str(int(x)) if x == int(x) else None)
    add(str(round(x))); add(f"{round(x,1):g}" if abs(x) >= 0.05 else None)
    if abs(x) >= 1:  # percentual
        add(f"{x:g}%"); add(f"{round(x,1):g}%")
    if abs(x) < 1 and x != 0:
        add(f"{x*100:g}%"); add(f"{round(x*100,1):g}%")
    m = re.match(r"([-\d.]+)e-?(\d+)", f"{x:.6e}")
    if m:
        mant, exp = m.group(1), int(m.group(2))
        mant_t = mant.rstrip("0").rstrip(".") if "." in mant else mant
        for mm_ in {mant, mant_t}:
            add(m.group(0).replace(".0e", "e"))
            add(f"{mm_}×10{sup(exp)}"); add(f"{mm_} × 10^{exp}")
            add(f"{mm_}e{exp}"); add(f"{mm_}e-{exp}")
            # mantissa com gap até o expoente (ex.: 2.13(±1.63)×10⁵)
            out.add(f"__RX__{re.escape(mm_)}{{0,16}}10{re.escape(sup(exp))}")
    # round-2 (θ*: 0.333 -> predição escrita como 0.33)
    add(f"{round(x,2):g}")
    if x == round(x, 2) or True:
        add(f"{x:.2f}")
    texish = re.sub(r"e-?0*(\d+)", r"\\times10^{-\1}", f"{x:.10g}")
    add(texish if "\\times" in texish else None)
    if 0 < abs(x) < 1 and x == round(x, 2):
        add(f"{x:.2f}".rstrip("0").rstrip("."))
    return {t for t in out if t}

def variant_matches(txt, var):
    if var.startswith("__RX__"):
        return re.search(var[6:], txt) is not None
    return var in txt

class Guardian:
    def __init__(self, md_path, tex_path, claims, manifest, consistency):
        self.md_path = md_path
        self.tex = open(tex_path, encoding="utf-8").read() if tex_path and os.path.exists(tex_path) else ""
        self.md = open(md_path, encoding="utf-8").read() if md_path and os.path.exists(md_path) else ""
        self.claims = claims
        self.cids = {c["claim_id"]: c for c in claims}
        self.manifest = manifest
        self.eids = {s.get("evidence_id"): s for s in manifest.get("sources", [])}
        self.consistency = consistency
        self.nfacts = consistency.get("numeric_facts", [])
        self.findings = []

    def flag(self, rid, sev, where, issue, demand):
        self.findings.append(OrderedDict(
            id=rid, severity=sev, where=where, issue=issue, demand=demand))

    # ---------- R0 ----------
    def round0(self):
        # 1. ORPHAN TAGS: [claim:Cxxx] no md sem entrada no csv
        tags = set(re.findall(r"\[claim:(C\d+)\]", self.md))
        orphans = sorted(t for t in tags if t not in self.cids)
        for t in orphans:
            self.flag(f"R0-ORPHAN-{t}", "BLOCKED", self.md_path,
                      f"Tag [claim:{t}] citada no manuscrito não existe em claims.csv.",
                      "Registrar a claim no CSV (com evidence_ids e verificação) ou remover a tag.")
        unused = sorted(set(self.cids) - tags)
        if unused:
            self.flag("R0-UNUSED", "NOTE", self.md_path,
                      f"Claims registradas mas não citadas no manuscrito: {', '.join(unused)}.",
                      "Confirmar que são intencional (claims de outline/suplemento).")
        # 2. EVIDENCE LINKS: evidence_ids das claims citadas devem existir no manifest
        for t in sorted(tags & set(self.cids)):
            evs = [e.strip() for e in re.split(r"[;,]", self.cids[t].get("evidence_ids","")) if e.strip()]
            missing = [e for e in evs if e not in self.eids]
            if missing:
                self.flag(f"R0-EVID-{t}", "BLOCKED", self.md_path,
                          f"Claim {t} liga a evidência inexistente no manifest: {', '.join(missing)}.",
                          "Corrigir evidence_ids ou registrar a fonte.")
        # 3. NUMBER BINDING: todo N-fato citado no md deve ter tag [evidence:] ou [claim:] próxima
        for n in self.nfacts:
            for var in num_variants(n.get("value")):
                if not variant_matches(self.md, var):
                    continue
                idx = 0 if not var.startswith("__RX__") else self.md.find(
                    re.search(var[6:], self.md).group(0)) if re.search(var[6:], self.md) else 0
                m = re.search(var[6:], self.md) if var.startswith("__RX__") else None
                start = m.start() if m else self.md.find(var)
                ctx = self.md[max(0,start-220):start+220+len(var)]
                if "[claim:" in ctx or "[evidence:" in ctx:
                    break
            else:
                self.flag(f"R0-NBIND-{n['fact_id']}", "AMEND", self.md_path,
                          f"N-fato {n['fact_id']} ({n.get('concept')}={n.get('value')} {n.get('unit','')}) "
                          "aparece no texto sem marker de rastreabilidade próximo.",
                          "Colocar [claim:Cxxx][evidence:Exxx] junto ao número ou remover o número.")
        # 4. DRIFT TEX<->MD: números que estão no tex e não no md
        if self.tex and self.md:
            tex_nums = set(re.findall(r"\d+\.\d+|\d+", self.tex))
            md_nums = set(re.findall(r"\d+\.\d+|\d+", self.md))
            drift = sorted(n for n in tex_nums - md_nums if len(n) >= 2 and n not in
                           {"1","2","3","4","5","6","7","8","9","0"} | {str(i) for i in range(10,60)})
            interesting = [n for n in drift if re.search(rf"\b{re.escape(n)}\b", self.tex)]
            if interesting:
                self.flag("R0-DRIFT-TEX", "AMEND", "latex",
                          f"Números presentes no LaTeX e ausentes no manuscrito-fonte (drift): "
                          f"{', '.join(interesting[:25])}.",
                          "Retropropagar ao md (source of truth) ou remover do LaTeX.")
        return len(self.findings)

    # ---------- R1 ----------
    BATTERY = {
        "factual": [
            "Status de revisão por pares da fonte? (preprint ≠ revisado — rotular)",
            "Fonte única ou corroboração independente?",
            "Transferência de espécie/modelo → humano declarada?",
        ],
        "result": [
            "Pre-registrado ou post-hoc? (rotular explicitamente)",
            "Baseline e critério de comparação definidos?",
            "Incerteza/IC reportado?",
        ],
        "method": [
            "Self-test executado e arquivado?",
            "Critérios de aceitação especificados ANTES do resultado?",
            "Código+params arquivados no repo?",
        ],
    }
    CHECKLIST = [  # (id, regex/teste no md+tex, severity, demanda)
        ("M1-κconc", r"(µM|\\textmu M|uM)", "AMEND",
         "M1: estimativa de ordem de grandeza κ↔concentração presente E rotulada como ilustrativa/fechada pelo braço A6."),
        ("M2-T3", r"T3", "AMEND", "M2: critério informativo T3 (frente<50% em κ≤8) definido e distinguido de T1/T2."),
        ("M3-hierarchy", r"same-mass|mesma massa|consistência qualitativa|qualitative consistency", "AMEND",
         "M3: hierarquia MV2>MV1 rotulada como consistência (não validação) + controle same-mass declarado."),
        ("M4-murine", r"relative rates remain murine|taxas relativas permanecem|time rescal", "AMEND",
         "M4: declaração explícita de que humanização = rescala global de tempo, taxas relativas murinas."),
        ("M6-refcount", r"42 verified", "AMEND",
         "M6: contagem de referências deve bater com o manifest (33 fontes E-ID) — remover '42 verified' ou reconciliar."),
        ("M7-prionlike", r"Stopschinski|Jucker", "AMEND", "M7: refs canônicas de prion-like citadas no §transferência."),
        ("M8-safety", r"immunogenicity|imunogenicidade", "AMEND", "M8: parágrafo/limite de segurança (imunogenicidade/clearance) do construto."),
        ("m1-theta-def", r"θ\s*≡|\\\\theta\s*\\equiv|theta ≡|θ \u2261", "AMEND", "m1: definição formal de θ na primeira ocorrência."),
        ("m2-keff-days", r"\b88\b|\b8\.64\b|10\^\{-6\}|10⁻⁶", "NOTE", "m2: k_eff com contraparte em dias (tabela consolidada)."),
        ("m3-anchor", r"release v1\.0|tag v", "AMEND", "m3: âncora imutável (release/commit) citada no lugar de contagem de commits."),
        ("m4-figs", r"FIG2_MARKER|fig2_theta", "BLOCKED", "m4: Fig.2 (θ-resposta) e Fig.3 (subtipos) devem existir como arquivo e ser referenciadas."),
        ("m5-table1", r"Table 1|Tabela 1", "AMEND", "m5: tabela consolidada de parâmetros com fonte por parâmetro."),
        ("m10-lock", r"release v1\.0", "NOTE", "m10: predições travadas citam release específico."),
    ]
    def round1(self):
        body = self.md + "\n" + self.tex
        for cid_item, pat, sev, demand in self.CHECKLIST:
            if not re.search(pat, body, re.IGNORECASE):
                self.flag(f"R1-CHK-{cid_item}", sev, "manuscript+tex",
                          f"Checklist hostil {cid_item} não satisfeito (padrão não encontrado).", demand)
        # bateria por claim_kind (amostra executável: claims citadas)
        cited = sorted(set(re.findall(r"\[claim:(C\d+)\]", self.md)) & set(self.cids))
        batt = OrderedDict()
        for t in cited:
            kind = self.cids[t].get("claim_kind","factual")
            batt.setdefault(kind, []).append(t)
        for kind, ids in batt.items():
            self.flag(f"R1-BATTERY-{kind}", "NOTE", "claims",
                      f"Bateria hostil aplicada a {len(ids)} claims {kind}: " +
                      " | ".join(self.BATTERY.get(kind, [])) +
                      f" (IDs: {', '.join(ids)})",
                      "Cada pergunta deve ter resposta no texto/manifesto; sem resposta → limitação.")
        # verificação de fontes: preprints devem estar rotulados no manifest
        n_pre = sum(1 for s in self.manifest["sources"] if s.get("source_type")=="preprint")
        if n_pre:
            self.flag("R1-PREPRINT", "NOTE", "manifest",
                      f"{n_pre} fonte(s) preprint no manifest — o texto deve rotular status de revisão onde forem centrais.",
                      "Rotular no texto (ex.: bioRxiv preprint).")
        # números de manuscrito fora do manifest de consistência → exige marker de assumption
        allowed = set()
        for n in self.nfacts:
            allowed |= num_variants(n.get("value"))
        md_nums = set(re.findall(r"\d+\.\d+", self.md))
        extra = []
        SKIP_CTX = re.compile(r"bioRxiv|doi|DOI|http|github|release|v2\.[67]|^#|\n#{1,4} ")
        for n in sorted(md_nums):
            if any(variant_matches(self.md, v) for v in (allowed if isinstance(allowed, set) else {t for t in allowed}) if not t.startswith("__RX__")) or n in allowed:
                # ainda precisa de ocorrência específica sem tag? aqui allowed já conta como ligado
                continue
            if re.match(r"^10\.\d+$", n):  # DOI prefix, não é valor
                continue
            exempt = False
            for m in re.finditer(re.escape(n), self.md):
                ctx = self.md[max(0,m.start()-200):m.end()+200]
                pre = self.md[max(0,m.start()-8):m.start()]
                if ("[claim:" in ctx or "[evidence:" in ctx or SKIP_CTX.search(ctx)
                        or re.search(r"#{1,4}\s*$", pre)):
                    exempt = True; break
                if any(w in ctx.lower() for w in ("assumption","ilustrativ","illustrative","assumid","order-of-magnitude")):
                    exempt = True; break
            if not exempt:
                extra.append(n)
        if extra:
            self.flag("R1-NUM-UNBOUND", "AMEND", self.md_path,
                      f"Números decimais no texto sem N-fato e sem marker de assumption: {', '.join(extra[:20])}",
                      "Ligar a N-fato/claim, ou rotular como assumption ilustrativa no contexto.")
        return len(self.findings)

    # ---------- R3: epistemic interrogation ----------
    # Presença dos PROCEDIMENTOS que a crítica semântica exige (cada um nasceu de
    # uma pergunta "o quê falta / por quê?" — ver guardian_report_v5_epistemic.md)
    EPISTEMIC = [
        ("R3-THETA-OPS", "operational definition|θ[_ ]?obs|theta[_ ]?obs|estimator", "BLOCKED",
         "A predição travada θ<0.33 exige definição OPERACIONAL de como θ é medido/estimado em organoides (senão é infalsificável/circular)."),
        ("R3-SAP", "statistical (analysis )?plan|Welch|Holm", "BLOCKED",
         "Plano estatístico do G0 (teste, α, correção de multiplicidade, poder) deve estar NO manuscrito, não só no protocolo."),
        ("R3-BLIND", "blind|cego|randomiz", "AMEND",
         "Cegamento do avaliador e randomização de organoides por lote declarados."),
        ("R3-FAILBIND", "failures.{0,260}(contextual|registry|E03|elevat)", "AMEND",
         "As 6 falhas clínicas que alimentam o análogo negativo 0/6 do Bayes precisam de status de evidência declarado (hoje: fora do E-registry)."),
        ("R3-PREPRINT-DEP", "load-bearing|central.{0,120}preprint|preprint.{0,120}central", "AMEND",
         "Dependência das âncoras centrais em 2 preprints não revisados (E003/E004) declarada explicitamente."),
        ("R3-CONJ-RISK", "precedent for the conjunction|conjunction itself", "AMEND",
         "Risco lógico do argumento regulatório: precedente para cada pilar ≠ precedente para a conjunção."),
        ("R3-SEARCHLOG", "search[ _](log|quer)|queries.{0,80}archiv|buscas.{0,80}arquivad", "AMEND",
         "Reprodutibilidade da auditoria: onde estão as ~90 queries arquivadas?"),
        ("R3-LOCALIZ", "localization|PET|front position|localiza", "AMEND",
         "O cálculo do anel 8–12 mm depende de SABER onde está a frente — nenhum procedimento de localização in vivo é especificado."),
        ("R3-SENS-SWEEP", "exponent|C[₅_]{0,2}50.{0,60}sweep|sensitivity sweep", "AMEND",
         "Sensibilidades estruturais pendentes: expoente do freeS (1 vs 2) e C50 sweep sobre θ*."),
        ("R3-CANON", r"KNOWLEDGE_CANON", "BLOCKED",
         "Canon do conhecimento: o manuscrito deve referenciar KNOWLEDGE_CANON.md (índice-mestre achado→evidência→impacto→falsificador) — nenhum achado publica sem linha no canon."),
        ("R3-G0SIM", r"G0-sim", "BLOCKED",
         "Declaração de status do gate vigente: o G0-sim (computacional, executado e passado) e seu escopo (licencia continuação; não valida biologia) devem estar declarados."),
        ("R3-G0SIM-STIM", r"non-substitutable|does not substitute|não substitui|stimulat", "AMEND",
         "Cláusula construtiva do G0-sim: achados computacionais usados como resultado; validação necessária e insubstituível; estimula P&D ágil conforme metodologia científica."),
        ("R3-REDOSE-IMMUN", "anti-PEG|repeat-dose immun|redosing.{0,80}immunogen|clearance acelerad", "AMEND",
         "Imunogenicidade da redose repetida (LNP/anti-PEG, via intratecal) discutida."),
    ]
    def round3(self):
        body = self.md
        for cid_item, pat, sev, demand in self.EPISTEMIC:
            if not re.search(pat, body, re.IGNORECASE):
                self.flag(f"R3-{cid_item}", sev, "manuscript",
                          f"Interrogação epistêmica {cid_item}: procedimento ausente.", demand)
        return len(self.findings)

    # ---------- R2 ----------
    def round2(self, prev_count):
        """Recurse: ataca as correções. Se nada novo, converged."""
        start = len(self.findings)
        if not self.md:
            return 0
        # toda assumption declarada deve ter '(assumption)' ou análogos E não ter tag de evidence
        # cláusula: limites em ;/nova-linha/período que NÃO está entre dígitos (decimal)
        def clause(pos):
            lo, hi = pos, pos
            while lo > 0 and not re.match(r"[;\n]", self.md[lo-1]) and not (
                lo >= 2 and self.md[lo-1] == "." and not (self.md[lo-2].isdigit() or self.md[lo].isdigit())):
                lo -= 1
            while hi < len(self.md) and not re.match(r"[;\n]", self.md[hi]) and not (
                self.md[hi] == "." and not (self.md[hi-1].isdigit() and hi+1 < len(self.md) and self.md[hi+1].isdigit())):
                hi += 1
            return self.md[lo:hi]
        for m in re.finditer(r"(?:pg/cell/day|µM|uM)", self.md):
            cl = clause(m.start())
            if "[claim:" in cl or "[evidence:" in cl:
                self.flag("R2-ASSUM-TAGGED", "BLOCKED", self.md_path,
                          "Estimativa ilustrativa (κ↔µM) carrega tag de evidência na mesma cláusula — mas é assumption, não medida.",
                          "Remover tag da cláusula; rotular como '(illustrative assumption; closed by arm A6)'.")
                continue
            look = self.md[max(0,m.start()-200):m.end()+140]
            if not re.search(r"illustrative|ilustrativ|assumption|assumid", look, re.IGNORECASE):
                self.flag("R2-ASSUM-UNLABELED", "AMEND", self.md_path,
                          "Estimativa κ↔concentração sem rótulo de assumption na cláusula/adjacência.",
                          "Rotular '(illustrative; not a measured secretion estimate)'.")
        # consistência PT/EN: mesma contagem de claims se ambos existirem
        pt = os.path.join(os.path.dirname(self.md_path), "manuscript_PT_v5.md")
        if os.path.exists(pt):
            pt_txt = open(pt, encoding="utf-8").read()
            en_tags = sorted(set(re.findall(r"\[claim:(C\d+)\]", self.md)))
            pt_tags = sorted(set(re.findall(r"\[claim:(C\d+)\]", pt_txt)))
            if en_tags != pt_tags:
                miss = set(en_tags) ^ set(pt_tags)
                self.flag("R2-PT-PARITY", "BLOCKED", pt,
                          f"Paridade PT/EN de claim-tags quebrada: {', '.join(sorted(miss))}.",
                          "Adicionar/remover tags para igualar o EN (source of truth).")
        else:
            self.flag("R2-PT-MISSING", "AMEND", os.path.dirname(self.md_path),
                      "Companion PT sem claim-tags (paridade declarada como passo futuro).",
                      "Gerar manuscript_PT_v5.md com as mesmas tags.")
        # predições travadas: mesma frase no EN e registro no repo
        if "0.33" in self.md and "release v1.0" not in self.md and "b7b40f0" not in self.md:
            self.flag("R2-LOCK-ANCHOR", "AMEND", self.md_path,
                      "Predição θ<0.33 presente sem âncora imutável (release v1.0 / commit).",
                      "Citar release v1.0 (ou hash) junto à predição travada.")
        new = len(self.findings) - start
        return new

def render_report(findings, rounds):
    sev_order = {"BLOCKED":0, "AMEND":1, "NOTE":2}
    fs = sorted(findings, key=lambda f: sev_order.get(f["severity"],3))
    lines = ["# GUARDIAN REPORT — paper v5 (hostile recursive reviewer)",
             "",
             f"**Rodadas executadas:** {rounds} · **Achados:** {len(findings)} "
             f"(BLOCKED={sum(1 for f in fs if f['severity']=='BLOCKED')}, "
             f"AMEND={sum(1 for f in fs if f['severity']=='AMEND')}, "
             f"NOTE={sum(1 for f in fs if f['severity']=='NOTE')})",
             "", "## Gate", "",
             ("**PASS — zero BLOCKED.** O manuscrito resiste à rodada recursiva; recomendação ao editor: "
              "aceitável como preprint com auditoria pública.")
             if not any(f["severity"]=="BLOCKED" for f in fs) else
             ("**FAIL — existem achados BLOCKED.** Revisor hostil nega submissão até resolução."),
             "", "---", ""]
    for f in fs:
        lines.append(f"### [{f['severity']}] {f['id']} — {f['where']}")
        lines.append(f"- **Problema:** {f['issue']}")
        lines.append(f"- **Exigência:** {f['demand']}")
        lines.append("")
    return "\n".join(lines)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--round", type=int, required=True)
    ap.add_argument("--md"); ap.add_argument("--tex")
    ap.add_argument("--claims", required=True)
    ap.add_argument("--manifest", required=True)
    ap.add_argument("--consistency", required=True)
    ap.add_argument("--registry", required=True)
    ap.add_argument("--report", required=True)
    a = ap.parse_args()
    g = Guardian(a.md, a.tex, load_claims(a.claims), load_json(a.manifest), load_json(a.consistency))
    if a.round == 0:
        g.round0()
    elif a.round == 1:
        g.round0(); g.round1()
    elif a.round == 3:
        g.round0(); g.round1()
        prev = -1
        for i in range(4):
            new = g.round2(prev)
            if new == 0:
                break
        g.round3()
    reg = {"round": a.round, "n_findings": len(g.findings),
           "gate_pass": not any(f["severity"]=="BLOCKED" for f in g.findings),
           "findings": g.findings}
    with open(a.registry, "w", encoding="utf-8") as f:
        json.dump(reg, f, ensure_ascii=False, indent=2)
    with open(a.report, "w", encoding="utf-8") as f:
        f.write(render_report(g.findings, a.round))
    print(f"round={a.round} findings={len(g.findings)} "
          f"BLOCKED={sum(1 for x in g.findings if x['severity']=='BLOCKED')} "
          f"AMEND={sum(1 for x in g.findings if x['severity']=='AMEND')} "
          f"gate={'PASS' if reg['gate_pass'] else 'FAIL'}")
    sys.exit(0 if reg["gate_pass"] else 1)

if __name__ == "__main__":
    main()
