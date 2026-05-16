---
wave: gold-reset-wave13-sample-5-remediation
date_open: 2026-05-15
date_close: 2026-05-15
status: complete
source_wave: gold-certification-reset
---

# Gold Reset Wave 13 Sample 5 Remediation

## Mission

Repair and re-panel the fifth Wave 13 natural-sciences chemistry sample before
restoring Current Certified Gold.

## Claim Boundary

| Guide | Invariant |
|---|---|
| `natural-sciences/02-BONDING.md` | `chemical-bonding-landscape` |
| `natural-sciences/03-THERMOCHEM.md` | `thermochemistry-landscape` |
| `natural-sciences/04-KINETICS.md` | `chemical-kinetics-landscape` |
| `natural-sciences/05-ELECTROCHEMISTRY.md` | `electrochemistry-landscape` |

## Pulse Status

| Pulse | Status | Governing Roles | Evidence |
|---|---|---|---|
| 01 - Repair and R2 panel | DONE | reference-editor, expert-skeptic, bridge-builder, index-weaver | `panels/r2-wave13-sample-5/R2-consolidated.md` |

## Validation Gates

| Gate | Result |
|---|---|
| Mechanical prerequisite | PASS: `proof.exe check --daVinci -e --no-fail proof.toml <4 guides>` returned OK and output contained no `FAIL` |
| Editorial repair | PASS: bonding, thermochemistry, kinetics, and electrochemistry cheat sheets rebuilt as diagnostic tables |
| R2 panel | PASS: guide-specific scoring, reader tasks, and adversarial closure recorded |
| Registry update | PASS: only these four repaired guides restored to Current Certified Gold |

## Closeout

Wave 13 sample 5 restores four natural-sciences chemistry guides with reset-era
R2 evidence.

