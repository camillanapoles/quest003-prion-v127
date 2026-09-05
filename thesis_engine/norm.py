"""Normalização e hash — cópia EXATA de paper/evidence_workspace/build_evidence_record.py.

Não alterar: o sha256 das claims (norm→sha256) é o elo de imutabilidade do registro.
"""
import hashlib
import re


def norm(t: str) -> str:
    t = t.lower().strip()
    t = re.sub(r"[^a-z0-9.%×±\-\s]", "", t)
    return re.sub(r"\s+", " ", t)


def sha(t: str) -> str:
    return hashlib.sha256(norm(t).encode()).hexdigest()
