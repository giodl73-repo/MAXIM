---
wave: gold-reset-wave6-sample-1-remediation
date_open: 2026-05-15
date_close: 2026-05-15
status: complete
source_wave: gold-certification-reset
---

# Gold Reset Wave 6 Sample 1 Remediation

## Mission

Repair and re-panel the first Wave 6 PDE sample before restoring Current
Certified Gold.

## Claim Boundary

| Guide | Invariant |
|---|---|
| `partial-differential-equations/01-CLASSIFICATION.md` | `pde-classification-determines` |
| `partial-differential-equations/02-FIRST-ORDER.md` | `first-order-pde-taxonomy` |
| `partial-differential-equations/03-WAVE-EQUATION.md` | `wave-equation-landscape` |
| `partial-differential-equations/04-HEAT-EQUATION.md` | `heat-equation-landscape` |

## Pulse Status

| Pulse | Status | Governing Roles | Evidence |
|---|---|---|---|
| 01 - Repair and R2 panel | DONE | reference-editor, expert-skeptic, bridge-builder, index-weaver | `panels/r2-wave6-sample-1/R2-consolidated.md` |

## Validation Gates

| Gate | Result |
|---|---|
| Mechanical prerequisite | PASS: `proof.exe check --daVinci -e --no-fail proof.toml <4 guides>` returned OK and output contained no `FAIL` |
| Editorial repair | PASS: PDE classification, first-order, wave, and heat decision tables rebuilt as diagnostic tables |
| R2 panel | PASS: guide-specific scoring, reader tasks, and adversarial closure recorded |
| Registry update | PASS: only these four repaired guides restored to Current Certified Gold |

## Closeout

Wave 6 sample 1 restores four PDE guides with reset-era R2 evidence.

