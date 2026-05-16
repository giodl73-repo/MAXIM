---
wave: gold-reset-wave15-sample-3-remediation
date_open: 2026-05-15
date_close: 2026-05-15
status: complete
source_wave: gold-certification-reset
---

# Gold Reset Wave 15 Sample 3 Remediation

## Mission

Repair and re-panel the third Wave 15 sample across programming-language-theory
and remote-sensing before restoring Current Certified Gold.

## Claim Boundary

| Guide | Invariant |
|---|---|
| `programming-language-theory/09-MODERN-FRONTIERS.md` | `modern-plt-frontiers` |
| `remote-sensing/01-EM-SPECTRUM.md` | `remote-sensing-spectrum` |
| `remote-sensing/02-PASSIVE-SENSORS.md` | `passive-sensor-sampling` |
| `remote-sensing/03-ACTIVE-SENSORS-SAR.md` | `sar-geometry` |

## Pulse Status

| Pulse | Status | Governing Roles | Evidence |
|---|---|---|---|
| 01 - Repair and R2 panel | DONE | reference-editor, expert-skeptic, bridge-builder, index-weaver | `panels/r2-wave15-sample-3/R2-consolidated.md` |

## Validation Gates

| Gate | Result |
|---|---|
| Mechanical prerequisite | PASS: `proof.exe check --daVinci -e --no-fail proof.toml <4 guides>` returned OK and output contained no `FAIL` |
| Editorial repair | PASS: PL frontiers, EM spectrum, passive sensors, and SAR cheat sheets rebuilt as diagnostic tables |
| R2 panel | PASS: guide-specific scoring, reader tasks, and adversarial closure recorded |
| Registry update | PASS: only these four repaired guides restored to Current Certified Gold |

## Closeout

Wave 15 sample 3 restores one programming-language-theory guide and three
remote-sensing guides with reset-era R2 evidence.

