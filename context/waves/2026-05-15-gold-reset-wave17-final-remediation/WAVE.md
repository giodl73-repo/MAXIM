---
wave: gold-reset-wave17-final-remediation
date_open: 2026-05-15
date_close: 2026-05-15
status: complete
source_wave: gold-certification-reset
---

# Gold Reset Wave 17 Final Remediation

## Mission

Repair and re-panel the remaining masonry Wave 17 guides before closing the wave
reset and restoring Current Certified Gold.

## Claim Boundary

| Guide | Invariant |
|---|---|
| `masonry/03-BRICKLAYING.md` | `bricklaying-workflow` |
| `masonry/04-STONEWORK.md` | `stone-masonry-classification` |
| `masonry/05-STRUCTURAL-MASONRY.md` | `structural-masonry-decision-tree` |
| `masonry/06-ARCHES-VAULTS.md` | `arch-logic` |

## Pulse Status

| Pulse | Status | Governing Roles | Evidence |
|---|---|---|---|
| 01 - Repair and R2 panel | DONE | reference-editor, expert-skeptic, bridge-builder, index-weaver | `panels/r2-wave17-final/R2-consolidated.md` |

## Validation Gates

| Gate | Result |
|---|---|
| Mechanical prerequisite | PASS: `proof.exe check --daVinci -e --no-fail proof.toml <4 guides>` returned OK and output contained no `FAIL` |
| Editorial repair | PASS: bricklaying, stonework, structural-masonry, and arches/vaults cheat sheets rebuilt as diagnostic tables |
| R2 panel | PASS: guide-specific scoring, reader tasks, and adversarial closure recorded |
| Registry update | PASS: only these four repaired guides restored to Current Certified Gold |

## Closeout

Wave 17 final remediation restores four masonry guides with reset-era R2 evidence
and completes the Wave 17 reset repair scope.

