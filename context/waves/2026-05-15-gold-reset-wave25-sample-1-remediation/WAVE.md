---
wave: gold-reset-wave25-sample-1-remediation
date_open: 2026-05-15
date_close: 2026-05-15
status: complete
source_wave: gold-certification-reset
---

# Gold Reset Wave 25 Sample 1 Remediation

## Mission

Repair and re-panel the first Wave 25 astrobiology sample before restoring
Current Certified Gold.

## Claim Boundary

| Guide | Invariant |
|---|---|
| `astrobiology/01-ORIGIN-OF-LIFE.md` | `origin-life-landscape` |
| `astrobiology/02-EXTREMOPHILES.md` | `extremophile-envelope-life` |
| `astrobiology/03-HABITABLE-ENVIRONMENTS.md` | `solar-system-habitability-map` |
| `astrobiology/04-BIOSIGNATURES.md` | `biosignature-space` |

## Pulse Status

| Pulse | Status | Governing Roles | Evidence |
|---|---|---|---|
| 01 - Repair and R2 panel | DONE | reference-editor, expert-skeptic, bridge-builder, index-weaver | `panels/r2-wave25-sample-1/R2-consolidated.md` |

## Validation Gates

| Gate | Result |
|---|---|
| Mechanical prerequisite | PASS: `proof.exe check --daVinci -e --no-fail proof.toml <4 guides>` returned OK and output contained no `FAIL` |
| Editorial repair | PASS: origin of life, extremophiles, habitable environments, and biosignatures cheat sheets rebuilt as diagnostic tables |
| R2 panel | PASS: guide-specific scoring, reader tasks, and adversarial closure recorded |
| Registry update | PASS: only these four repaired guides restored to Current Certified Gold |

## Closeout

Wave 25 sample 1 restores four astrobiology guides with reset-era R2 evidence.

