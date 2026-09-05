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
