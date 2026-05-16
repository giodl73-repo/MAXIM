---
wave: gold-reset-wave24-sample-4-remediation
date_open: 2026-05-15
date_close: 2026-05-15
status: complete
source_wave: gold-certification-reset
---

# Gold Reset Wave 24 Sample 4 Remediation

## Mission

Repair and re-panel the archaeology middle Wave 24 sample before restoring
Current Certified Gold.

## Claim Boundary

| Guide | Invariant |
|---|---|
| `archaeology/03-MATERIAL-ANALYSIS.md` | `archaeological-material-analysis-methods` |
| `archaeology/04-PREHISTORY.md` | `prehistoric-timeline-transitions` |
| `archaeology/05-ANCIENT-CIVILIZATIONS.md` | `first-cities-states-framework` |
| `archaeology/06-CLASSICAL-ARCHAEOLOGY.md` | `classical-world-material-culture` |

## Pulse Status

| Pulse | Status | Governing Roles | Evidence |
|---|---|---|---|
| 01 - Repair and R2 panel | DONE | reference-editor, expert-skeptic, bridge-builder, index-weaver | `panels/r2-wave24-sample-4/R2-consolidated.md` |

## Validation Gates

| Gate | Result |
|---|---|
| Mechanical prerequisite | PASS: `proof.exe check --daVinci -e --no-fail proof.toml <4 guides>` returned OK and output contained no `FAIL` |
| Editorial repair | PASS: material analysis, prehistory, ancient civilizations, and classical archaeology cheat sheets rebuilt as diagnostic tables |
| R2 panel | PASS: guide-specific scoring, reader tasks, and adversarial closure recorded |
| Registry update | PASS: only these four repaired guides restored to Current Certified Gold |

## Closeout

Wave 24 sample 4 restores four archaeology guides with reset-era R2 evidence.

