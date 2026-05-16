---
wave: gold-reset-wave17-sample-2-remediation
date_open: 2026-05-15
date_close: 2026-05-15
status: complete
source_wave: gold-certification-reset
---

# Gold Reset Wave 17 Sample 2 Remediation

## Mission

Repair and re-panel the second woodworking Wave 17 sample before restoring
Current Certified Gold.

## Claim Boundary

| Guide | Invariant |
|---|---|
| `woodworking/05-SURFACE-PREPARATION.md` | `surface-preparation-sequence` |
| `woodworking/06-FINISHING.md` | `wood-finish-chemistry-map` |
| `woodworking/07-FURNITURE-CONSTRUCTION.md` | `furniture-construction-systems` |
| `woodworking/08-TURNING-CARVING.md` | `turning-carving-comparison` |

## Pulse Status

| Pulse | Status | Governing Roles | Evidence |
|---|---|---|---|
| 01 - Repair and R2 panel | DONE | reference-editor, expert-skeptic, bridge-builder, index-weaver | `panels/r2-wave17-sample-2/R2-consolidated.md` |

## Validation Gates

| Gate | Result |
|---|---|
| Mechanical prerequisite | PASS: `proof.exe check --daVinci -e --no-fail proof.toml <4 guides>` returned OK and output contained no `FAIL` |
| Editorial repair | PASS: surface-preparation, finishing, furniture-construction, and turning/carving cheat sheets rebuilt as diagnostic tables |
| R2 panel | PASS: guide-specific scoring, reader tasks, and adversarial closure recorded |
| Registry update | PASS: only these four repaired guides restored to Current Certified Gold |

## Closeout

Wave 17 sample 2 restores four woodworking guides with reset-era R2 evidence.

