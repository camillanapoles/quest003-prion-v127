#!/usr/bin/env bash
# Auditoria CI: roda validadores + checks estruturais + gera relatório
set -u
cd "$(git rev-parse --show-toplevel)"
TS="${TS:-$(date -u +%Y%m%d-%H%M%S)}"
SH=$(git rev-parse --short HEAD)
R="paper/pdf/audit_${SH}.md"
M="paper/manuscript_Parte2_v1.md"
mkdir -p paper/pdf

echo "# AUDITORIA AUTOMÁTICA — ${TS} @ ${SH}" > "$R"
echo "" >> "$R"
echo "## Bateria scientific-writing" >> "$R"

VM=$(python3 scripts/validators/validate_manifest.py paper/evidence_workspace/source_manifest.json --kind source --require-verified 2>&1 | grep -o '"errors": *[0-9]*' | head -1 || echo "?")
echo "- validate_manifest: $VM" >> "$R"

CR=$(python3 scripts/validators/check_references.py paper/evidence_workspace/source_manifest.json 2>&1 | grep -o '"errors": *[0-9]*' | head -1 || echo "?")
echo "- check_references: $CR" >> "$R"

CC=$(python3 scripts/validators/check_consistency.py paper/evidence_workspace/consistency_manifest.json 2>&1 | grep -o '"errors": *[0-9]*' | head -1 || echo "?")
echo "- check_consistency: $CC" >> "$R"

echo "" >> "$R"
echo "## Estrutura" >> "$R"
for chk in "ETRIZAÇÃO COMPUTACIONAL EM:Título" "NOTA À LEITURA:Nota" "CAPÍTULO 1:Cap1" "CAPÍTULO 7:Cap7" "Base de Validade:BaseVal" "APÊNDICE A:ApxA" "APÊNDICE B:ApxB" "REFERÊNCIAS:Refs" "restauram parâmetros:Restauração"; do
  PAT="${chk%%:*}"; NAME="${chk#*:}"
  grep -q "$PAT" "$M" && echo "- [x] $NAME" >> "$R" || echo "- [ ] $NAME ❌" >> "$R"
done
ACP=$(tail -n +2 "$M" | grep -c "ACP" 2>/dev/null || echo 0)
echo "- ACP restantes: $ACP" >> "$R"

echo "" >> "$R"
echo "## PDF" >> "$R"
echo "- Versão: v${TS}_${SH}" >> "$R"
echo "- Fonte: $(wc -w < "$M") palavras" >> "$R"

echo "=== RELATÓRIO: $R ==="
cat "$R"

# A9 — ledger garantista (mesma bateria do pre-commit/CI)
echo "" >> "$R"
echo "## A9 pendências" >> "$R"
python3 scripts/pendencias_check.py >> "$R" 2>&1 || { echo "✗ A9 FALHOU — auditar"; exit 1; }
tail -2 "$R"
