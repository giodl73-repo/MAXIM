---
wave: gold-reset-wave13-sample-3-remediation
date_open: 2026-05-15
date_close: 2026-05-15
status: complete
source_wave: gold-certification-reset
---

# Gold Reset Wave 13 Sample 3 Remediation

## Mission

Repair and re-panel the third Wave 13 ecology sample before restoring Current
Certified Gold.

## Claim Boundary

| Guide | Invariant |
|---|---|
| `ecology/02-COMMUNITY-ECOLOGY.md` | `community-species-interaction-matrix` |
| `ecology/03-ECOSYSTEM-ENERGETICS.md` | `ecosystem-energy-budget` |
| `ecology/04-BIOGEOCHEMICAL-CYCLES.md` | `biogeochemical-cycle-framework` |
| `ecology/05-SUCCESSION-STABILITY.md` | `succession-stability-framework` |

## Pulse Status

| Pulse | Status | Governing Roles | Evidence |
|---|---|---|---|
| 01 - Repair and R2 panel | DONE | reference-editor, expert-skeptic, bridge-builder, index-weaver | `panels/r2-wave13-sample-3/R2-consolidated.md` |

## Validation Gates

| Gate | Result |
|---|---|
| Mechanical prerequisite | PASS: `proof.exe check --daVinci -e --no-fail proof.toml <4 guides>` returned OK and output contained no `FAIL` |
| Editorial repair | PASS: community ecology, ecosystem energetics, biogeochemical cycles, and succession/stability cheat sheets rebuilt as diagnostic tables |
| R2 panel | PASS: guide-specific scoring, reader tasks, and adversarial closure recorded |
| Registry update | PASS: only these four repaired guides restored to Current Certified Gold |

## Closeout

Wave 13 sample 3 restores four ecology guides with reset-era R2 evidence.

