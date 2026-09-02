"""Engine SQLite do thesis_engine. DB é artefato derivado (rebuild = ingest)."""
import os

from sqlalchemy.orm import sessionmaker
from sqlmodel import Session, SQLModel, create_engine

_DEFAULT_DB = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "thesis.db")
_Echo = os.environ.get("THESIS_ENGINE_SQL_ECHO") == "1"


def create_db(db_path: str = _DEFAULT_DB):
    """Cria o engine e registra as tabelas. Retorna o engine."""
    engine = create_engine(f"sqlite:///{db_path}", echo=_Echo)
    # Importa models para registrar nas metadatas antes do create_all
    from thesis_engine import models  # noqa: F401

    SQLModel.metadata.create_all(engine)
    return engine


def get_session(db_path: str = _DEFAULT_DB) -> Session:
    return Session(create_db(db_path))


__sessionmakers: dict[str, sessionmaker] = {}


def session_for(db_path: str = _DEFAULT_DB) -> Session:
    """Session factory cacheada por caminho (uso da API/CLI)."""
    if db_path not in __sessionmakers:
        __sessionmakers[db_path] = sessionmaker(bind=create_db(db_path))
    return __sessionmakers[db_path]()
