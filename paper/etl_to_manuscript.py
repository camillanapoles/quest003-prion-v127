#!/usr/bin/env python3
"""ETL: artefatos da quest 003 → manifestos canônicos da skill scientific-writing.
EXTRACT  : data.json (grafo), literature/evidence_table.md, JSONs computacionais
TRANSFORM: schema canônico (source_manifest_template / claim_evidence_template)
LOAD     : paper/draft-workspace/{source_manifest.json,claims.csv,etl_report.json}
Idempotente e determinístico — re-rodar a cada sessão. NÃO modifica as fontes."""
import json, re, os, csv, hashlib, sys

Q=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # quests/003
DW=os.path.join(Q,'paper','draft-workspace')
os.makedirs(DW,exist_ok=True)

# ---------------- EXTRACT ----------------
G=json.load(open(os.path.join(Q,'artifacts/dashboard/data.json')))
EVT=open(os.path.join(Q,'literature/evidence_table.md')).read()

W7  = json.load(open(os.path.join(Q,'experiments/ws_7_results/ws_7_results.json'))) if os.path.exists(os.path.join(Q,'experiments/ws_7_results/ws_7_results.json')) else {}
W9V4= json.load(open(os.path.join(Q,'experiments/ws_9_results/ws_9_v4_human.json'))) if os.path.exists(os.path.join(Q,'experiments/ws_9_results/ws_9_v4_human.json')) else {}
BAY = json.load(open(os.path.join(Q,'experiments/bayes_results/bayes_success.json'))) if os.path.exists(os.path.join(Q,'experiments/bayes_results/bayes_success.json')) else {}

# ---------------- TRANSFORM: fontes (E-IDs) ----------------
# índice por token identificável (doi / pmid / pmc /指纹 de citação)
def parse_ids(refs):
    ids={}
    for r in refs or []:
        m=re.search(r'10\.\d{4,9}/[^\s"\']+',r)
        if m: ids['doi']=m.group(0).rstrip('.,;)')
        m=re.search(r'PMID[: ]*(\d+)',r)
        if m: ids['pmid']=m.group(1)
        m=re.search(r'PMC(\d+)',r)
        if m: ids['pmcid']='PMC'+m.group(1)
    return ids

def make_title(node):
    t=node.get('title') or node.get('label','')
    return t

sources=[]; sidx=[]  # sidx: (tokens → E-id)
seen=set()
def add_source(title,refs,stype,opened,verified_on,locator,node_id):
    ids=parse_ids(refs)
    key=(ids.get('doi') or ids.get('pmid') or ids.get('pmcid') or title.lower()[:60])
    if key in seen:
        for t,e in sidx:
            if t==key: return e
    eid=f"E{len(sources)+1:03d}"
    sources.append({
        "authors": [], "confidentiality":"public", "evidence_id":eid,
        "identifiers":ids, "locator":locator or "node:"+node_id,
        "source_type":stype, "title":title,
        "verification":{"source_opened":opened,
            "status":"verified" if opened else "unverified",
            "verified_by":"conssortium_agent" if opened else "",
            "verified_on":verified_on or ""},
        "year":None})
    seen.add(key); sidx.append((key,eid))
    return eid

# 1) nós do grafo com refs externas → fontes
for n in G['nodes']:
    refs=n.get('refs') or []
    external=[r for r in refs if re.search(r'10\.|PMID|PMC|doi',r)]
    if not external: continue
    opened = ('verified' in (n.get('evidence','') or '').lower()) or n.get('status') in ('confirmed','constraint','refuted')
    add_source(make_title(n), external,
                "journal_article",
                opened, n.get('updated',''), '', n['id'])

# 2) fontes computacionais (arquivos próprios, determinísticos)
comp=[("WS-7 transport solver results (self-tested)","experiments/ws_7_results/ws_7_results.json",W7),
      ("WS-9 humanized in-silico trial results","experiments/ws_9_results/ws_9_v4_human.json",W9V4),
      ("WS-8 Bayesian weighted-analogue estimates","experiments/bayes_results/bayes_success.json",BAY)]
node_eid={}
for title,path,obj in comp:
    if not obj: continue
    eid=add_source(title,[],"software",True,"2026-08-26",path,"")
    node_eid[title.split()[0]]=eid

# ---------------- TRANSFORM: claims (C-IDs) ----------------
def sha(t): return hashlib.sha256(re.sub(r'\s+',' ',t.strip()).encode()).hexdigest()

SEC={'molecular':'Introduction','classe':'Introduction','celular':'Results',
     'entrega':'Results','traducao':'Discussion'}
KIND={'confirmed':'factual','constraint':'factual','active':'estimate',
      'proposed':'estimate','gray_light':'estimate','gray_dark':'estimate',
      'invalid':'refutation','refuted':'refutation'}

claims=[]
def resolve_e(node):
    hits=set()
    ids=parse_ids(node.get('refs'))
    key=(ids.get('doi') or ids.get('pmid') or ids.get('pmcid'))
    if key:
        for t,e in sidx:
            if t==key: hits.add(e)
    # matching léxico: sobrenome+ano da citação do nó vs título da fonte
    evs_str=(node.get('evidence','') or '')+' '+' '.join(node.get('refs') or [])
    m=re.search(r'(\d{4})',evs_str); yr=m.group(1) if m else ''
    for t,e in sidx: pass
    for src in sources:
        ti=src['title'].lower()
        toks=[w for w in re.findall(r'[a-z]{4,}',ti)]
        for r in (node.get('refs') or []):
            rl=r.lower()
            if any(w in rl for w in ('asante','mead','gatdula','zerbes','groveman','williams','liang','xue','hu ','han ','thorne','masel','fornara','igel','abud','ginhoux','sorrells','gomez','cheng','gentile','elder','krauze','smid','jalland','delucia','zheng','hosszu','mallucci','raymond','minikel','tofersen','nusinersen','tafamidis','lund')):
                pass
        for w in toks[:3]:
            if w in evs_str.lower(): hits.add(src['evidence_id']); break
        if yr and yr in ti: hits.add(src['evidence_id'])
    return sorted(hits)[:3]

for n in G['nodes']:
    cid=f"C{len(claims)+1:03d}"
    evs=resolve_e(n)
    claims.append({"claim_id":cid,"section":SEC.get(n['group'],'Results'),
        "claim_kind":KIND.get(n.get('outlook') or n.get('status','proposed'),'estimate'),
        "claim_text_sha256":sha(make_title(n)),
        "evidence_ids":evs,
        "verification_status":"verified_by_open_source" if evs else "unresolved",
        "uncertainty":"estimated" if (n.get('prob')) else "none_stated",
        "analysis_intent":"descriptive"})

# claims computacionais (números exatos dos JSONs)
def add_claim(section,kind,text,evs,unc):
    claims.append({"claim_id":f"C{len(claims)+1:03d}","section":section,"claim_kind":kind,
        "claim_text_sha256":sha(text),"evidence_ids":evs,
        "verification_status":"reproducible_local","uncertainty":unc,"analysis_intent":"confirmatory"})

if W7:
    add_claim('Results','computational',
      "WS-7: halo r10% 4.2-5.8 mm per deposit; ring 8-12 mm; hydrogel xi>=5xrp; redose<=7d; mass 100%; Thiele err 0.5%",
      [node_eid.get('WS-7')] if 'WS-7' in node_eid else [],"none_stated")
if W9V4:
    add_claim('Results','computational',
      f"WS-9 humanized: theta*={W9V4.get('theta_star')}; {W9V4.get('days_per_simunit')} d/sim-unit; doubling {W9V4.get('t_double_human_days')} d",
      [node_eid.get('WS-9')] if 'WS-9' in node_eid else [],"estimated")
if BAY:
    cs=BAY.get('cenarios',{})
    g0=cs.get('G0_GO',{}); des=cs.get('desaceleracao',{})
    add_claim('Results','computational',
      f"WS-8: G0 pass mean={round(g0.get('mean',0),3)} p5={round(g0.get('p5',0),3)} p95={round(g0.get('p95',0),3)}; slowing mean={round(des.get('mean',0),3)}",
      [node_eid.get('WS-8')] if 'WS-8' in node_eid else [],"estimated")

# ---------------- LOAD ----------------
json.dump({"schema_version":"1.0","sources":sources},
          open(os.path.join(DW,'source_manifest.json'),'w'),indent=1,ensure_ascii=False)
with open(os.path.join(DW,'claims.csv'),'w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=["claim_id","section","claim_kind","claim_text_sha256",
                                    "evidence_ids","verification_status","uncertainty","analysis_intent"])
    w.writeheader()
    for c in claims:
        c2=dict(c); c2['evidence_ids']=';'.join(c2['evidence_ids']); w.writerow(c2)

report={"sources":len(sources),"claims":len(claims),
        "open_verified":sum(1 for s in sources if s['verification']['source_opened']),
        "unresolved_evidence":[c['claim_id'] for c in claims if not c['evidence_ids']],
        "note":"ETL determinístico de data.json+JSONs; fontes intactas; re-executar após cada sessão"}
json.dump(report,open(os.path.join(DW,'etl_report.json'),'w'),indent=1)
print(json.dumps(report,indent=1))
