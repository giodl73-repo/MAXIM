---
wave: gold-reset-wave28-sample-2-remediation
date_open: 2026-05-15
date_close: 2026-05-15
status: complete
source_wave: gold-certification-reset
---

# Gold Reset Wave 28 Sample 2 Remediation

## Mission

Repair and re-panel the second Wave 28 acoustics/agriculture sample before
restoring Current Certified Gold.

## Claim Boundary

| Guide | Invariant |
|---|---|
| `acoustics/00-OVERVIEW.md` | `acoustic-frequency-spectrum-overview` |
| `agriculture/02-CROP-SYSTEMS.md` | `crop-system-diversity-spectrum` |
| `agriculture/05-FERTILIZERS-PESTICIDES.md` | `chemical-inputs-agriculture` |
| `agriculture/07-LIVESTOCK-SYSTEMS.md` | `livestock-systems-overview` |

## Pulse Status

| Pulse | Status | Governing Roles | Evidence |
|---|---|---|---|
| 01 - Repair and R2 panel | DONE | reference-editor, expert-skeptic, bridge-builder, index-weaver | `panels/r2-wave28-sample-2/R2-consolidated.md` |

## Validation Gates

| Gate | Result |
|---|---|
| Mechanical prerequisite | PASS: `proof.exe check --daVinci -e --no-fail proof.toml <4 guides>` returned OK and output contained no `FAIL` |
| Editorial repair | PASS: acoustics overview, crop systems, fertilizers/pesticides, and livestock systems cheat sheets rebuilt as diagnostic tables |
| R2 panel | PASS: guide-specific scoring, reader tasks, and adversarial closure recorded |
| Registry update | PASS: only these four repaired guides restored to Current Certified Gold |

## Closeout

Wave 28 sample 2 restores four guides with reset-era R2 evidence.

