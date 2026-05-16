---
wave: gold-reset-wave13-sample-4-remediation
date_open: 2026-05-15
date_close: 2026-05-15
status: complete
source_wave: gold-certification-reset
---

# Gold Reset Wave 13 Sample 4 Remediation

## Mission

Repair and re-panel the fourth Wave 13 ecology sample before restoring Current
Certified Gold.

## Claim Boundary

| Guide | Invariant |
|---|---|
| `ecology/06-BIOGEOGRAPHY.md` | `biogeography-framework` |
| `ecology/07-AQUATIC-ECOSYSTEMS.md` | `aquatic-ecosystem-types` |
| `ecology/08-DISTURBANCE-ECOLOGY.md` | `disturbance-ecology-framework` |
| `ecology/09-CONSERVATION-BIOLOGY.md` | `conservation-biology-framework` |

## Pulse Status

| Pulse | Status | Governing Roles | Evidence |
|---|---|---|---|
| 01 - Repair and R2 panel | DONE | reference-editor, expert-skeptic, bridge-builder, index-weaver | `panels/r2-wave13-sample-4/R2-consolidated.md` |

## Validation Gates

| Gate | Result |
|---|---|
| Mechanical prerequisite | PASS: `proof.exe check --daVinci -e --no-fail proof.toml <4 guides>` returned OK and output contained no `FAIL` |
| Editorial repair | PASS: biogeography, aquatic ecosystems, disturbance ecology, and conservation biology cheat sheets rebuilt as diagnostic tables |
| R2 panel | PASS: guide-specific scoring, reader tasks, and adversarial closure recorded |
| Registry update | PASS: only these four repaired guides restored to Current Certified Gold |

## Closeout

Wave 13 sample 4 restores four ecology guides with reset-era R2 evidence.

