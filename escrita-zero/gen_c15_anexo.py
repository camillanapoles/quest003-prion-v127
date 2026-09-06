#!/usr/bin/env python
"""Gera c15 (APÊNDICE A — INVENTÁRIO E CONCORDÂNCIA) do repo + do banco.

Determinístico: datas vêm do git (primeiro/último commit por artefato);
a tabela de concordância vem do banco (claims × evidências × status).
Prosa escrita à mão — tabelas geradas. Saída: rascunhos/c15_apendice_a.md
"""
import json
import sqlite3
import subprocess
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
OUT = REPO / "escrita-zero" / "rascunhos" / "c15_apendice_a.md"
DB = REPO / "tese_v2.db"


def datas_git(f: str) -> tuple[str, str, str]:
    """(primeiro commit, último commit, hash curto do último) — data curta."""
    first = subprocess.run(
        ["git", "log", "--follow", "--diff-filter=A", "--format=%ad", "--date=short", "--", f],
        capture_output=True, text=True, cwd=REPO).stdout.strip().splitlines()
    last = subprocess.run(
        ["git", "log", "-1", "--follow", "--format=%ad %h", "--date=short", "--", f],
        capture_output=True, text=True, cwd=REPO).stdout.strip()
    pri = first[-1] if first else "—"
    partes = last.split()
    ult, hsh = (partes[0], partes[1]) if len(partes) >= 2 else (last or "—", "—")
    return (pri, ult, hsh)


# (arquivo, papel, o que trava)
PREREGISTROS = [
    ("experiments/g0_protocol.md", "Protocolo do gate G0-wet", "desenho do ensaio, controle positivo e kill-switches"),
    ("experiments/G0_EXECUTION_FREEZE_CHECKLIST.md", "Checklist de congelamento F1–F10", "o que deve estar travado antes do primeiro organoide infectado"),
    ("experiments/PARTNER_SELECTION_PROTOCOL.md", "Protocolo de seleção de parceiro", "critérios e pesos congelados antes de qualquer contato"),
    ("experiments/REPARAM_LOOP.md", "Loop de re-parametrização", "o que recalibra, com qual prior e quando"),
    ("experiments/ws_10_spec.md", "Especificação WS-10", "a escada de portões como régua de continuidade"),
    ("experiments/m31/M31_SESSAO2_PLANO.md", "Plano da sessão M31", "a titulação κ-exigido por cinética do hospedeiro"),
    ("experiments/m31/m31_protocolo_garantista.md", "Protocolo garantista M31", "garantias por passo da cadeia de dose"),
]

MOTOR = [
    ("experiments/ws_7_solver.py", "WS-7 — solver de transporte ADR", "auto-testes de conservação de massa e erro numérico-analítico"),
    ("experiments/ws_7_v2_wave.py", "WS-7 — frente de onda v2", "verificação da solução de onda"),
    ("experiments/ws_8_bayes.py", "WS-8 — calibração bayesiana", "calibração hierárquica sobre análogos estruturais"),
    ("experiments/ws_8_local.py", "WS-8 — ajuste local", "ajuste local da calibração"),
    ("experiments/ws_9_port.py", "WS-9 — portabilidade do modelo", "porta do modelo para o programa"),
    ("experiments/ws_9_run.py", "WS-9 — execução do modelo", "execução da infecção in silico com tampão V127"),
    ("experiments/ws_9_v5_sweeps.py", "WS-9 — varreduras v5", "colheita de sensibilidade S1–S3"),
    ("experiments/p024_driver.py", "Driver multi-espécie", "a sondagem multi-espécie do experimento 2"),
    ("experiments/part2_theta_obs_v1.py", "Estimador θ_obs v1.0-NN", "estimadora congelada do congelamento F1"),
    ("experiments/part2_theta_obs_pooled.py", "Estimador θ_obs pooled", "agregação por braço da calibração"),
    ("experiments/part2_theta_obs_v11.py", "Estimador θ_obs v1.1-IDW", "variante interpolada — testada e rejeitada"),
]

EXP1 = [
    ("experiments/ws_9_results/ws_9_v4_human.json", "Execução v4 humanizada", "o run que travou θ* e a contenção em κ=2"),
    ("experiments/ws_9_results/ws_9_v5_sweeps_S1.json", "Varredura S1", "a colheita de sensibilidade sobre a predição travada"),
    ("experiments/ws_9_results/ws_9_v5_sweeps_S1_authors_rerun.json", "Re-execução da autora (S1)", "paridade valor-a-valor em ambiente independente"),
]

F_FREEZE = [
    ("F1", "Estimador θ_obs congelado", "v1.0-NN mantida; variante interpolada testada e rejeitada", "FECHADO"),
    ("F2", "Análise braço-a-braço", "Welch com correção de Holm, poder declarado", "congelado"),
    ("F3", "Cegamento do scorista", "scorista cego ao braço; aleatorização por lote", "congelado"),
    ("F4", "Estratificação por lote", "aleatorização estratificada", "congelado"),
    ("F5", "Controle positivo A8", "critério de validade do ensaio declarado", "congelado"),
    ("F6", "Kill-switches por braço", "critério de morte programática do programa", "congelado"),
    ("F7", "Esquema do dado de organoide", "contrato entre bancada e estimador", "congelado"),
    ("F8", "Loop de re-parametrização", "recalibração com prior e gatilho declarados", "congelado"),
    ("F9", "Janelas de leitura", "regime estacionário e leitura declarados", "congelado"),
    ("F10", "Seleção do parceiro", "protocolo congelado; execução do fluxo aguarda contato", "dormente por design"),
]


def tb(rows: list[list[str]]) -> str:
    head = rows[0]
    out = ["| " + " | ".join(head) + " |", "|" + "---|" * len(head)]
    out += ["| " + " | ".join(r) + " |" for r in rows[1:]]
    return "\n".join(out) + "\n"


def main() -> None:
    linhas: list[str] = []
    linhas += [
        "# APÊNDICE A — INVENTÁRIO E CONCORDÂNCIA",
        "",
        "Este apêndice existe para que o leitor confira a tese sem acesso a nenhum "
        "repositório: as datas de pré-registro e de versão do motor estão impressas "
        "aqui, o congelamento do gate úmido está resumido na íntegra dos seus itens, "
        "e a concordância entre cada claim e suas fontes está numa tabela só, gerada "
        "do registro probatório. O que aparece abaixo é o que o disco e o registro "
        "guardam — nada além disso.",
        "",
        "## A.1 Folhas de pré-registro — datas impressas",
        "",
        "Cada documento de pré-registro entrou no controle de versão antes da "
        "execução que ele disciplina; a primeira coluna de datas é a data de "
        "nascimento do documento, a segunda a última alteração aceita [claim:C040] "
        "[evidence:E033].",
        "",
    ]
    rows = [["Documento", "Trava", "Primeira versão", "Última alteração", "Commit"]]
    for f, papel, trava in sorted(PREREGISTROS, key=lambda r: datas_git(r[0])[0] + r[0]):
        pri, ult, hsh = datas_git(f)
        rows.append([f"`{f}` — {papel}", trava, pri, ult, hsh])
    linhas += [tb(rows), ""]

    linhas += [
        "## A.2 Motor e solver — folha de versão",
        "",
        "O motor da Parte 2 é o solver WS-7 com auto-testes declarados — conservação "
        "de massa e erro numérico-analítico verificados [claim:C032] [evidence:E030] "
        "— calibrado pelo WS-8 sobre análogos estruturais [claim:C036] "
        "[evidence:E031] e executado pelo WS-9 com humanização do tempo e tampão "
        "V127 [claim:C037] [evidence:E032]. As versões abaixo são as folhas com as "
        "datas em que cada peça entrou e foi alterada pela última vez.",
        "",
    ]
    rows = [["Peça", "Papel", "Primeira versão", "Última alteração", "Commit"]]
    for f, papel, _trava in sorted(MOTOR, key=lambda r: datas_git(r[0])[0] + r[0]):
        pri, ult, hsh = datas_git(f)
        rows.append([f"`{f}`", papel, pri, ult, hsh])
    linhas += [tb(rows), ""]

    linhas += [
        "## A.3 Experimento 1 — folha de versão",
        "",
        "A regra da linha experimental (Cap. 4, §4.2) exige que os dados do "
        "experimento 1 — a corrida murina com humanização do tempo — entrem na tese "
        "apenas onde permaneceram inalterados pelo experimento 2, com a folha de "
        "versão anexada. Esta é a folha. O run v4 humanizado travou o limiar: θ* "
        "igual a 0,333, com a frente contida em κ=2 — de 2,83 para 0,82 mm "
        "[claim:C038] [evidence:E032] — sob o relógio humanizado de uma unidade de "
        "simulação igual a 144 dias [claim:C037] [evidence:E032,E007]. A varredura "
        "S1 colheu a sensibilidade sem mover o limiar: em κ=2 a frente permanece no "
        "valor de base e a contenção desloca-se para κ=4 — a predição discriminadora "
        "que separa as duas formas funcionais da unidade inibitória [claim:C051] "
        "[evidence:E032,E033]. A re-execução da autora, em ambiente independente, "
        "reproduziu o S1 valor a valor [claim:C040] [evidence:E033].",
        "",
    ]
    rows = [["Artefato", "Papel", "Primeira versão", "Última alteração", "Commit"]]
    for f, papel, _trava in sorted(EXP1, key=lambda r: datas_git(r[0])[0] + r[0]):
        pri, ult, hsh = datas_git(f)
        rows.append([f"`{f}`", papel, pri, ult, hsh])
    linhas += [tb(rows), ""]

    linhas += [
        "## A.4 Congelamento do gate úmido — F1–F10",
        "",
        "O checklist de congelamento define o que precisa estar travado antes do "
        "primeiro organoide infectado. A tabela resume o estado de cada item; o "
        "estimador fechou com a variante de vizinho-mais-próximo mantida e a "
        "interpolada rejeitada na fronteira de decisão [claim:C052] "
        "[evidence:E032,E033]. A liberação final — o gate F — exige todos os itens "
        "fechados e a assinatura da pesquisadora principal do laboratório parceiro; "
        "a seleção de parceiro é método sem seleção e sem contato [claim:C053] "
        "[evidence:E033], e a infraestrutura de continuidade segue operante com a "
        "escada de portões como régua [claim:C047] [evidence:E033]. As duas "
        "pendências — a execução do fluxo de parceiro e a assinatura — são "
        "dormências por design, declaradas como tais nas conclusões.",
        "",
    ]
    linhas += [tb([["Item", "Conteúdo congelado", "Status"]] + [list(r) for r in F_FREEZE]), ""]

    linhas += [
        "## A.5 Validação da base comum",
        "",
        "A base que fundamento e aplicação compartilham tem cadeia de validação "
        "própria: o kernel estocástico é publicado com código aberto [claim:C013] "
        "[evidence:E009]; o motor passa por auto-testes declarados [claim:C032] "
        "[evidence:E030]; e a cadeia de reprodutibilidade do programa — versão "
        "anterior reproduzida idêntica, varredura reproduzida valor a valor em "
        "segundo ambiente — está registrada [claim:C040] [evidence:E033]. No "
        "ingestão do registro probatório para a escrita, cada texto de claim é "
        "verificado por soma criptográfica contra o índice do registro: nenhuma "
        "claim entra na tese se o texto divergir do congelado.",
        "",
        "## A.6 Concordância claims ↔ fontes",
        "",
        "A tabela abaixo é a régua da autora: cada claim do registro, ao lado das "
        "evidências que a sustentam e do seu estado de verificação. Gerada do "
        "banco, sem digitação; o leitor confere cada texto integral contra a forma como o corpo da tese o usou.",
        "",
    ]
    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row
    rows = [["Claim", "Texto integral", "Evidências", "Verificação"]]
    for r in con.execute("SELECT claim_id, claim_text, evidence_ids, verification_status FROM claim ORDER BY claim_id"):
        evs = ";".join(json.loads(r["evidence_ids"])) if r["evidence_ids"] else "—"
        texto = r["claim_text"].replace("|", "/")
        rows.append([f"[{r['claim_id']}]", texto, evs, r["verification_status"]])
    linhas += [tb(rows), ""]

    linhas += [
        "## A.7 Pendências anotadas",
        "",
        "Duas pendências vivem neste apêndice por honestidade, não por descuido. "
        "Primeira: a fonte do relato jornalístico do transplante dopaminérgico "
        "(referência da lista cujo registro guarda o endereço truncado) precisa de "
        "decisão da autora sobre o registro canônico — completar o endereço lá, ou "
        "manter a nota de pendência aqui; o escritor não edita o registro. Segunda: "
        "a execução do fluxo de seleção de parceiro e a assinatura do gate F "
        "continuam dormentes — sem parceiro não há gate, e a tese declara isso como "
        "arquitetura de duas partes, não como atraso [claim:C049] [evidence:E033].",
        "",
    ]

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(linhas), encoding="utf-8")
    print(f"anexo gerado → {OUT} ({len(linhas)} linhas)")


if __name__ == "__main__":
    main()
