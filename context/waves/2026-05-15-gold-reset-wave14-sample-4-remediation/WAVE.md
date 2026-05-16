---
wave: gold-reset-wave14-sample-4-remediation
date_open: 2026-05-15
date_close: 2026-05-15
status: complete
source_wave: gold-certification-reset
---

# Gold Reset Wave 14 Sample 4 Remediation

## Mission

Repair and re-panel the fourth geochemistry Wave 14 sample before restoring
Current Certified Gold.

## Claim Boundary

| Guide | Invariant |
|---|---|
| `geochemistry/05-CARBON-CYCLE.md` | `geochemical-carbon-cycle-architecture` |
| `geochemistry/07-WEATHERING-SOILS.md` | `weathering-system` |
| `geochemistry/08-OCEAN-GEOCHEMISTRY.md` | `ocean-geochemical-system` |
| `geochemistry/09-PLANETARY-GEOCHEMISTRY.md` | `planetary-geochemistry-landscape` |

## Pulse Status

| Pulse | Status | Governing Roles | Evidence |
|---|---|---|---|
| 01 - Repair and R2 panel | DONE | reference-editor, expert-skeptic, bridge-builder, index-weaver | `panels/r2-wave14-sample-4/R2-consolidated.md` |

## Validation Gates

| Gate | Result |
|---|---|
| Mechanical prerequisite | PASS: `proof.exe check --daVinci -e --no-fail proof.toml <4 guides>` returned OK and output contained no `FAIL` |
| Editorial repair | PASS: carbon-cycle, weathering-soils, ocean-geochemistry, and planetary-geochemistry cheat sheets rebuilt as diagnostic tables |
| R2 panel | PASS: guide-specific scoring, reader tasks, and adversarial closure recorded |
| Registry update | PASS: only these four repaired guides restored to Current Certified Gold |

## Closeout

Wave 14 sample 4 restores four geochemistry guides with reset-era R2 evidence.

