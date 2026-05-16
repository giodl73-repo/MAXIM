---
wave: gold-reset-wave25-sample-5-remediation
date_open: 2026-05-15
date_close: 2026-05-15
status: complete
source_wave: gold-certification-reset
---

# Gold Reset Wave 25 Sample 5 Remediation

## Mission

Repair and re-panel the fifth Wave 25 ceramics sample before restoring Current
Certified Gold.

## Claim Boundary

| Guide | Invariant |
|---|---|
| `ceramics/02-FORMING.md` | `ceramic-forming-method-spectrum` |
| `ceramics/03-DRYING-FIRING.md` | `ceramic-firing-sequence` |
| `ceramics/04-GLAZES.md` | `glaze-structure-cross-section` |
| `ceramics/05-DECORATION.md` | `ceramic-decoration-temperature-ladder` |

## Pulse Status

| Pulse | Status | Governing Roles | Evidence |
|---|---|---|---|
| 01 - Repair and R2 panel | DONE | reference-editor, expert-skeptic, bridge-builder, index-weaver | `panels/r2-wave25-sample-5/R2-consolidated.md` |

## Validation Gates

| Gate | Result |
|---|---|
| Mechanical prerequisite | PASS: `proof.exe check --daVinci -e --no-fail proof.toml <4 guides>` returned OK and output contained no `FAIL` |
| Editorial repair | PASS: forming, drying/firing, glazes, and decoration cheat sheets rebuilt as diagnostic tables |
| R2 panel | PASS: guide-specific scoring, reader tasks, and adversarial closure recorded |
| Registry update | PASS: only these four repaired guides restored to Current Certified Gold |

## Closeout

Wave 25 sample 5 restores four ceramics guides with reset-era R2 evidence.

