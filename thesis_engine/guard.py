"""GUARD DE AMBIENTE — regras DO BANCO (nunca hardcoded).

O guard consulta EnvironmentRule no DB (semeado pelo bootstrap com paths
derivados de __file__). Sem regras no DB = sem guard (modo permissivo p/ testes).
"""
from pathlib import Path

from sqlmodel import Session, select

from thesis_engine.db import create_db
from thesis_engine.models import EnvironmentRule

# repo root = derivado do código (nunca digitado)
REPO = Path(__file__).resolve().parents[1]


def seed_environment_rules(db_path: str) -> int:
    """Bootstrap semeia as regras de ambiente — paths derivados, não hardcoded."""
    from thesis_engine.escritor import setup_v2  # garante tabelas existirem
    engine = create_db(db_path)
    rules = [
        ("expected_repo", str(REPO), "repo onde o engine opera"),
        ("expected_branch", "tese-escrita-zero", "branch de trabalho"),
        # DEFAULT de fábrica: derivado de __file__ em runtime (não path digitado).
        # Após o seed, a regra vive NO BANCO e é consultada dali (editável sem código).
        ("forbidden_cwd", str(REPO.parent / "etrizacao"), "dir de symlinks — NÃO é o repo"),
        ("guard_message", f"cd {REPO} && git checkout tese-escrita-zero", "como corrigir"),
    ]
    with Session(engine) as s:
        n = 0
        for key, valor, desc in rules:
            existing = s.exec(
                select(EnvironmentRule).where(EnvironmentRule.rule_key == key)
            ).first()
            if not existing:
                s.add(EnvironmentRule(rule_key=key, valor=valor, descricao=desc))
                n += 1
        s.commit()
        return n


def check_environment(db_path: str = None, raise_on_fail: bool = True) -> dict:
    """Verifica ambiente contra regras DO BANCO. Sem regras = modo permissivo."""
    if db_path is None:
        db_path = str(REPO / "tese_v2.db")
    if not Path(db_path).exists():
        return {"ok": True, "modo": "permissivo (DB não existe)", "cwd": str(Path.cwd()), "problems": []}

    engine = create_db(db_path)
    with Session(engine) as s:
        rules = {
            r.rule_key: r.valor
            for r in s.exec(select(EnvironmentRule)).all()
        }
    if not rules:
        return {"ok": True, "modo": "permissivo (sem regras)", "cwd": str(Path.cwd()), "problems": []}

    cwd = Path.cwd()
    problems = []

    # 1 · forbidden_cwd
    forbidden = rules.get("forbidden_cwd")
    if forbidden and str(cwd) == forbidden:
        problems.append(f"VOCÊ ESTÁ EM {cwd} (só symlinks, NÃO é o repo)!")

    # 2 · expected_repo
    expected = rules.get("expected_repo")
    if expected and str(cwd) != forbidden:
        try:
            cwd.relative_to(Path(expected))
        except ValueError:
            if str(cwd) != forbidden:
                problems.append(f"cwd={cwd} fora do repo {expected}")

    # 3 · expected_branch (só se estamos no repo)
    if not problems and expected:
        import subprocess
        r = subprocess.run(
            ["git", "branch", "--show-current"],
            capture_output=True, text=True, cwd=expected
        )
        branch = r.stdout.strip()
        want = rules.get("expected_branch", "")
        if branch and want and branch != want:
            problems.append(f"branch={branch} (esperada: {want})")

    fix = rules.get("guard_message", "cd <repo>")
    if problems and raise_on_fail:
        raise EnvironmentError(
            f"\n🛑 GUARD DE AMBIENTE (regras do DB):\n"
            + "\n".join(f"  ❌ {p}" for p in problems)
            + f"\n\n✅ Corrija:\n  {fix}\n"
        )
    return {"ok": not problems, "cwd": str(cwd), "problems": problems}

def _seed_all_environment_rules(db_path: str) -> int:
    """Bootstrap semeia TODAS as EnvironmentRule (28) — WRITER skills + AUDITOR persona + invariantes + FSM."""
    from thesis_engine.models import EnvironmentRule
    ALL = [
        ("expected_repo", str(REPO), "[SISTEMA] repo onde o engine opera"),
        ("expected_branch", "tese-escrita-zero", "[SISTEMA] branch de trabalho"),
        ("forbidden_cwd", str(REPO.parent / "etrizacao"), "[SISTEMA] dir de symlinks"),
        ("guard_message", f"cd {REPO} && git checkout tese-escrita-zero", "[SISTEMA] como corrigir"),
        ("cycle_fsm", "brief->drafting->guard->gates->hostile->emenda->LOOP->approved->rendered->committed", "[SISTEMA] FSM"),
        ("cycle_loop_rule", "LOOP UNTIL hostil-aprova (zero abertos + gates verdes + ações + hostil_falou)", "[SISTEMA]"),
        ("cycle_separation_flow", "WRITER escreve -> AUDITOR questiona -> WRITER reescreve -> AUDITOR valida", "[SISTEMA]"),
        ("separation_of_powers", "writer escreve / auditor revisa / autora aprova", "[SISTEMA]"),
        ("persona_expertise", "PhD neurocientista com expertise em células-tronco e neurobiologia do SNC", "[AUDITOR]"),
        ("persona_metodologia", "metodologia de escrita de teses: ABNT·GUM·CONSORT·pré-registro·JHU/Harvard", "[AUDITOR]"),
        ("persona_postura", "hostil por busca de certeza: valida informação, lógica e ciência; não elogia — exige", "[AUDITOR]"),
        ("persona_acesso", "SEM acesso a nada além do que revisa — só texto+anexos", "[AUDITOR]"),
        ("persona_pergunta_g", "SOA HUMANO? Doutoranda brasileira não usa vocabulário de máquina", "[AUDITOR]"),
        ("auditor_rule_never_write", "AUDITOR NUNCA escreve: quem revisa não produz texto", "[AUDITOR]"),
        ("auditor_output_rule", "AUDITOR produz APENAS questionamentos — NUNCA emenda", "[AUDITOR]"),
        ("auditor_never_amend", "PROIBIDO: auditor escrever EMENDA na resposta", "[AUDITOR]"),
        ("cycle_invariant_1", "CI verde != tese pronta", "[AUDITOR] kernel"),
        ("cycle_invariant_2", "author_approved SÓ humana", "[AUDITOR]"),
        ("cycle_invariant_3", "números sempre via claims (lineage)", "[AUDITOR]"),
        ("cycle_invariant_4", "cronologia sempre IN-DOCUMENT", "[AUDITOR]"),
        ("cycle_invariant_5", "ficha acadêmica EXCLUSIVA da autora", "[AUDITOR]"),
        ("writer_skill_article", "article-writing: prosa com voz própria, sem AI-slop", "[WRITER] skill"),
        ("writer_skill_paper_spine", "paper-spine V4: contribution-first, STOP humano", "[WRITER] skill"),
        ("writer_skill_sci_writing", "scientific-writing: evidence->draft->gates->aprovação", "[WRITER] skill"),
        ("writer_skill_critical_thinking", "critical-thinking: valida metodologia ANTES de escrever", "[WRITER] skill"),
        ("writer_skill_council", "consciousness-council: deliber multi-perspectiva", "[WRITER] skill"),
        ("writer_rule_never_self_approve", "ESCRITOR NUNCA auto-aprova", "[WRITER]"),
    ]
    engine = create_db(db_path)
    with Session(engine) as s:
        n = 0
        for key, valor, desc in ALL:
            if not s.exec(select(EnvironmentRule).where(EnvironmentRule.rule_key == key)).first():
                s.add(EnvironmentRule(rule_key=key, valor=valor, descricao=desc))
                n += 1
        s.commit()
        return n
