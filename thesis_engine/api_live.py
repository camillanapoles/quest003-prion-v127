"""App singleton p/ `pi serve` (uvicorn precisa de um import-path)."""
import os

from thesis_engine.api import create_app

app = create_app(os.environ.get("THESIS_DB", "thesis.db"))
