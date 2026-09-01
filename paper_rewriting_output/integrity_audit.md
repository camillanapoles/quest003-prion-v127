# Integrity Audit

- Output directory: `paper_rewriting_output`
- Total findings: 4
- LaTeX gate: READY

> This report teaches, not just checks. Each finding includes a root cause, a concrete fix, what happens downstream if unfixed, and why this pattern matters.

## Summary

| Dimension | Status | Findings |
|---|---|---|
| Artifact Chain | CLEAN | 1 |
| Reasoning Depth | CLEAN | 1 |
| Evidence Chain | CLEAN | 1 |
| Integrity Patterns | WARNINGS | 1 |
| Process-Language Leak | CLEAN | 0 |

## Artifact Chain

**ART-000** ✅ All 8 required artifacts present

---

## Reasoning Depth

**RSN-000** ✅ All 10 rationale rows have adequate depth

---

## Evidence Chain

**EVD-000** ✅ Claims are adequately linked to evidence

---

## Integrity Patterns

### ⚠️ INT-001 — WARNING

**What was found:** No manuscript text to scan for integrity patterns

**Root cause:** The manuscript hasn't been written yet or final_paper/ is empty.

**Fix:** Proceed with writing, then re-run this audit.

**Downstream impact:** Cannot verify integrity of unwritten text.

---
