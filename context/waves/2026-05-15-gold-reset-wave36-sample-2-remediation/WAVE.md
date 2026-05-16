---
wave: gold-reset-wave36-sample-2-remediation
date_open: 2026-05-15
date_close: 2026-05-15
status: complete
source_wave: gold-certification-reset
---

# Gold Reset Wave 36 Sample 2 Remediation

## Mission

Continue Wave 36 reset review with formal-methods and freshwater-biology
candidates: repair substantive editorial defects, validate proof/Da Vinci
coverage, and restore Certified Gold only with guide-specific R2 evidence.

## Claim Boundary

This wave certifies only:

| Guide | Invariant |
|---|---|
| `formal-methods/03-THEOREM-PROVING.md` | `proof-assistant-landscape` |
| `formal-methods/04-TYPE-THEORY.md` | `type-theory-hierarchy` |
| `freshwater-biology/00-OVERVIEW.md` | `freshwater-biology-landscape` |

It does not restore Gold to the wider Wave 36 factory backlog.

## Pulse Status

| Pulse | Status | Governing Roles | Evidence |
|---|---|---|---|
| 01 - Repair and R2 panel | DONE | reference-editor, expert-skeptic, bridge-builder, index-weaver | `panels/r2-wave36-sample-2/R2-consolidated.md` |

## Validation Gates

| Gate | Result |
|---|---|
| Mechanical prerequisite | PASS: `proof.exe check --daVinci -e --no-fail proof.toml <3 guides>` returned OK and output contained no `FAIL` |
| Editorial repair | PASS: recall-style cheat sheets replaced; Lean/Mathlib univalence overclaim corrected |
| R2 panel | PASS: guide-specific scores, reader tasks, and adversarial closure recorded |
| Registry update | PASS: only the three repaired guides restored to Current Certified Gold |

## Closeout

This sample continues the reset distinction: factory hardening supplied
candidacy, while certification required repair, skeptical review, and
reader-task evidence.

