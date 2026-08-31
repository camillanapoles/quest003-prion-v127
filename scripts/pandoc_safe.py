#!/usr/bin/env python3
"""pandoc_safe — sanitização mínima pré-pandoc (contrato do workflow pdf-version-audit).
Remove apenas caracteres que quebram pdflatex/UTF-8 (zero-width, BOM, controles),
preservando integralmente o conteúdo científico (θ, ×, sobrescritos etc.).
Passa-o-que-existe: se o arquivo já é são, saída == entrada (idempotente)."""
import sys, unicodedata

src, dst = sys.argv[1], sys.argv[2]
BAD = {"\ufeff", "\u200b", "\u200c", "\u200d", "\u2060", "\ufeff"}
text = open(src, encoding="utf-8").read()
clean = "".join(
    ch for ch in text
    if ch not in BAD and (ch == "\n" or ch == "\t" or unicodedata.category(ch)[0] != "C")
)
open(dst, "w", encoding="utf-8").write(clean)
print(f"pandoc_safe: {len(text)} -> {len(clean)} chars ({len(text)-len(clean)} removidos)")
