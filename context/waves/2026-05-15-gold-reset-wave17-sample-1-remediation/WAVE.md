---
wave: gold-reset-wave17-sample-1-remediation
date_open: 2026-05-15
date_close: 2026-05-15
status: complete
source_wave: gold-certification-reset
---

# Gold Reset Wave 17 Sample 1 Remediation

## Mission

Repair and re-panel the first woodworking Wave 17 sample before restoring
Current Certified Gold.

## Claim Boundary

| Guide | Invariant |
|---|---|
| `woodworking/01-WOOD-SELECTION.md` | `wood-selection-decision-tree` |
| `woodworking/02-HAND-TOOLS.md` | `hand-tool-categories` |
| `woodworking/03-POWER-TOOLS.md` | `power-tool-workflow` |
| `woodworking/04-JOINERY.md` | `joinery-selection-function` |

## Pulse Status

| Pulse | Status | Governing Roles | Evidence |
|---|---|---|---|
| 01 - Repair and R2 panel | DONE | reference-editor, expert-skeptic, bridge-builder, index-weaver | `panels/r2-wave17-sample-1/R2-consolidated.md` |

## Validation Gates

| Gate | Result |
|---|---|
| Mechanical prerequisite | PASS: `proof.exe check --daVinci -e --no-fail proof.toml <4 guides>` returned OK and output contained no `FAIL` |
| Editorial repair | PASS: wood-selection, hand-tools, power-tools, and joinery cheat sheets rebuilt as diagnostic tables |
| R2 panel | PASS: guide-specific scoring, reader tasks, and adversarial closure recorded |
| Registry update | PASS: only these four repaired guides restored to Current Certified Gold |

## Closeout

Wave 17 sample 1 restores four woodworking guides with reset-era R2 evidence.

