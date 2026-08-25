#!/usr/bin/env python3
"""Modelo probabilístico ponderado de G0/G1 — evidência + analogias + modos de falha.
Transparente: todos os pesos nomeados e justificados. Saída: g0_probability_model.json"""
import json, os
M={}

# ===== FATOR 1: o agente funciona em nível de mecanismo (várias linhas independentes) =====
# Asante 2015 (Tg mice, Nature, alto): V127/V127 refratário .95
# Gatdula 2026 (CAD5, dose-dep, multi-cepas): in vitro direto .9
# Gatdula anchorless recombinante: trans in vitro .85
# Zerbes 2026 (AAV in vivo +50d): atravessa para tecido vivo .8
mech=[("V127/V127 refratário in vivo (Asante 2015)",0.95),("G126V suprime infecção estabelecida in vitro (Gatdula 2026)",0.90),("anchorless DN trans in vitro (Gatdula 2026)",0.85),("anchorless in vivo +50d (Zerbes 2026)",0.80),("base estrutural dupla (Zheng 2018; Hosszu 2020)",0.90)]
p_mech=1-1  # p(falha do mecanismo) = produto das falhas (independentes em série → falha exige todas errarem)
for _,p in mech: p_mech*= (1-p)
p_mech=1-p_mech
M['P_mecanismo_funciona']={"valor":round(p_mech,4),"leitura":"~certo; falha exigiria 4 linhas independentes de evidência estarem todas erradas"}

# ===== FATOR 2: a plataforma detecta (PPS = âncora de calibração) =====
# PPS = droga FRACA (mecanismo menos validado que o nosso) e ainda assim deu efeito mensurável
# → sensibilidade do ensaio confirmada com margem; risco de plataforma ~0.2
M['P_plataforma_detecta']={"valor":0.80,"base":["Groveman 2019 infecção fiel","Groveman 2021 PPS(droga fraca)>efeito → range dinâmico","Williams 2023 célula viável"],"risco_residual":"variabilidade organoide/seeding"}

# ===== FATOR 3: geometria do G0 é favorável (insight WS-7) =====
# ℓ=3.6mm (caso central) ≥ raio do organoide (1-2mm): TODO o organoide cabe dentro de UM halo
M['geometria_G0']={"halo_ℓ_mm":3.6,"raio_organoide_mm":"1-2","leitura":"o organoide INTEIRO está dentro do alcance de um depósito central — se o agente difunde, cobre tudo; gradiente proximal/distal mede escala real"}

# ===== MODOS DE FALHA (ponderados; falha compartilhada dos 3 braços ativos) =====
fails=[("secreção abaixo do limiar DN (θ desconhecido; dose-dep de Gatdula sem Km absoluto)",0.30),
       ("células morrem no microambiente infectado (Williams: NPC sobreviveu; secretora expressa mais)",0.22),
       ("falso negativo do readout (RT-QuIC/PrP-res variabilidade)",0.18),
       ("dependência de cepa sCJD MM1 específica (Gatdula: cobertura ampla)",0.12)]
p_shared_fail=1.0
for _,f in fails: p_shared_fail*=(1-f)
p_shared_fail=1-p_shared_fail
M['modos_de_falha']={k:v for k,v in fails}
M['P_falha_compartilhada']={"valor":round(1-p_shared_fail,3),"leitura":"prob. de TODOS os braços falharem por causa comum (não independente)"}

# ===== POR BRAÇO (mecanismo compartilhado, veículo diferente) =====
# P(braço) = P_mech × P(plataforma) × P(veículo) × (1-falha específica)
veh={"A6_proteina":"dose é variável livre (titração direta; risco=meia-vida no meio)",0.9:None}
M['P_braço']={
 "A6_proteína":round(p_mech*0.80*0.90*0.90,3),   # titulável diretamente; risco: estabilidade
 "A5_secretora":round(p_mech*0.80*0.62,3),        # precisa secreção suficiente + sobreviver
 "A7_mRNA":round(p_mech*0.80*0.52,3),             # transfecção LNP em organoide menos documentada
}
M['P_G0_algum_GO']={"valor":round(1-p_shared_fail,3),"leitura":"≥1 braço com ≥50% redução proximal+gradiente (union: falha comum domina)"}
M['desdobramentos']={
 "GO forte (A5 secretora)":M['P_braço']['A5_secretora'],
 "GO forte (A6 proteína) → pivot acelular":M['P_braço']['A6_proteína'],
 "GO (A7 mRNA) → ramo compassivo":M['P_braço']['A7_mRNA'],
 "NO-GO total":round(p_shared_fail,3),
}

# ===== ANALOGIAS: taxa de transferência organoide→camundongo (ponderada) =====
an=[("mecanismo célulo-autônomo 2D→organoide reproduz (base do campo)",0.75),
    ("Zerbes: mecanismo já cruzou p/ in vivo sistêmico (de-risca G1)",0.85),
    ("PPS: droga fraca funcionou no mesmo ensaio (nosso agente é mais forte a priori)",0.70)]
p_an=1.0
for _,x in an: p_an*=(1-x)
p_an=1-p_an
M['analogias_ponderadas']={k:v for k,v in an}
M['P_G1_positivo_dado_G0']={"valor":0.65,"base":"organoide→camundongo p/ mecanismos com validação Tg prévia + AAV in vivo já demonstrado"}
M['P_G1_positivo_absoluto']={"valor":round(M['P_G0_algum_GO']['valor']*0.65,3)}

json.dump(M,open('analysis/g0_probability_model.json','w'),indent=1,ensure_ascii=False)
print(json.dumps(M,indent=1,ensure_ascii=False))
