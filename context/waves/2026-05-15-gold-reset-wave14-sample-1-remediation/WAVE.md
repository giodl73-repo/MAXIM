---
wave: gold-reset-wave14-sample-1-remediation
date_open: 2026-05-15
date_close: 2026-05-15
status: complete
source_wave: gold-certification-reset
---

# Gold Reset Wave 14 Sample 1 Remediation

## Mission

Repair and re-panel the first materials-processing Wave 14 sample before
restoring Current Certified Gold.

## Claim Boundary

| Guide | Invariant |
|---|---|
| `materials-processing/02-HEAT-TREATMENT.md` | `heat-treatment-taxonomy` |
| `materials-processing/03-SOLIDIFICATION.md` | `solidification-fundamentals` |
| `materials-processing/04-DEFORMATION.md` | `deformation-temperature-mechanisms` |
| `materials-processing/05-FRACTURE-MECHANICS.md` | `fracture-mechanics-exists` |

## Pulse Status

| Pulse | Status | Governing Roles | Evidence |
|---|---|---|---|
| 01 - Repair and R2 panel | DONE | reference-editor, expert-skeptic, bridge-builder, index-weaver | `panels/r2-wave14-sample-1/R2-consolidated.md` |

## Validation Gates

| Gate | Result |
|---|---|
| Mechanical prerequisite | PASS: `proof.exe check --daVinci -e --no-fail proof.toml <4 guides>` returned OK and output contained no `FAIL` |
| Editorial repair | PASS: heat-treatment, solidification, deformation, and fracture-mechanics cheat sheets rebuilt as diagnostic tables |
| R2 panel | PASS: guide-specific scoring, reader tasks, and adversarial closure recorded |
| Registry update | PASS: only these four repaired guides restored to Current Certified Gold |

## Closeout

Wave 14 sample 1 restores four materials-processing guides with reset-era R2
evidence.

