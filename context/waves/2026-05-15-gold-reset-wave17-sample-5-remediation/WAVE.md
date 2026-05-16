---
wave: gold-reset-wave17-sample-5-remediation
date_open: 2026-05-15
date_close: 2026-05-15
status: complete
source_wave: gold-certification-reset
---

# Gold Reset Wave 17 Sample 5 Remediation

## Mission

Repair and re-panel the leather hardware/care and first masonry Wave 17 sample
before restoring Current Certified Gold.

## Claim Boundary

| Guide | Invariant |
|---|---|
| `leatherworking/08-HARDWARE-ASSEMBLY.md` | `leather-hardware-selection` |
| `leatherworking/09-CARE-MAINTENANCE.md` | `leather-aging-paths` |
| `masonry/01-MASONRY-UNITS.md` | `masonry-unit-families` |
| `masonry/02-MORTAR-GROUT.md` | `mortar-function-diagram` |

## Pulse Status

| Pulse | Status | Governing Roles | Evidence |
|---|---|---|---|
| 01 - Repair and R2 panel | DONE | reference-editor, expert-skeptic, bridge-builder, index-weaver | `panels/r2-wave17-sample-5/R2-consolidated.md` |

## Validation Gates

| Gate | Result |
|---|---|
| Mechanical prerequisite | PASS: `proof.exe check --daVinci -e --no-fail proof.toml <4 guides>` returned OK and output contained no `FAIL` |
| Editorial repair | PASS: hardware-assembly, care-maintenance, masonry-units, and mortar-grout cheat sheets rebuilt as diagnostic tables |
| R2 panel | PASS: guide-specific scoring, reader tasks, and adversarial closure recorded |
| Registry update | PASS: only these four repaired guides restored to Current Certified Gold |

## Closeout

Wave 17 sample 5 restores two leatherworking guides and two masonry guides with
reset-era R2 evidence.

