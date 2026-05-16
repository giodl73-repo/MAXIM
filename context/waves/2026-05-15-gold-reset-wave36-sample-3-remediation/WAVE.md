---
wave: gold-reset-wave36-sample-3-remediation
date_open: 2026-05-15
date_close: 2026-05-15
status: complete
source_wave: gold-certification-reset
---

# Gold Reset Wave 36 Sample 3 Remediation

## Mission

Continue Wave 36 reset review with the first furniture candidates: repair
substantive editorial defects, validate proof/Da Vinci coverage, and restore
Certified Gold only with guide-specific R2 evidence.

## Claim Boundary

This wave certifies only:

| Guide | Invariant |
|---|---|
| `furniture/00-OVERVIEW.md` | `furniture-field-map` |
| `furniture/01-WOOD-JOINERY.md` | `joinery-problem-hierarchy` |
| `furniture/02-HISTORY-STYLES.md` | `furniture-history-driver-axis` |

It does not restore Gold to the wider Wave 36 factory backlog.

## Pulse Status

| Pulse | Status | Governing Roles | Evidence |
|---|---|---|---|
| 01 - Repair and R2 panel | DONE | reference-editor, expert-skeptic, bridge-builder, index-weaver | `panels/r2-wave36-sample-3/R2-consolidated.md` |

## Validation Gates

| Gate | Result |
|---|---|
| Mechanical prerequisite | PASS: `proof.exe check --daVinci -e --no-fail proof.toml <3 guides>` returned OK and output contained no `FAIL` |
| Editorial repair | PASS: lookup-style tables and factual/engineering overclaims corrected |
| R2 panel | PASS: guide-specific scores, reader tasks, and adversarial closure recorded |
| Registry update | PASS: only the three repaired furniture guides restored to Current Certified Gold |

## Closeout

This sample keeps Gold scoped to reset-era evidence: factory hardening supplied
candidacy, while certification required repair, skeptical review, and
reader-task evidence.

