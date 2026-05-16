---
wave: gold-reset-wave13-sample-1-remediation
date_open: 2026-05-15
date_close: 2026-05-15
status: complete
source_wave: gold-certification-reset
---

# Gold Reset Wave 13 Sample 1 Remediation

## Mission

Repair and re-panel the first Wave 13 botany sample before restoring Current
Certified Gold.

## Claim Boundary

| Guide | Invariant |
|---|---|
| `botany/02-ROOTS-SOILS.md` | `roots-soils-interactions` |
| `botany/03-STEMS-WOOD.md` | `stems-growth-modes` |
| `botany/04-LEAVES-PHOTOSYNTHESIS.md` | `leaf-photosynthesis-tradeoff` |
| `botany/05-FLOWERS-REPRODUCTION.md` | `angiosperm-reproductive-cycle` |

## Pulse Status

| Pulse | Status | Governing Roles | Evidence |
|---|---|---|---|
| 01 - Repair and R2 panel | DONE | reference-editor, expert-skeptic, bridge-builder, index-weaver | `panels/r2-wave13-sample-1/R2-consolidated.md` |

## Validation Gates

| Gate | Result |
|---|---|
| Mechanical prerequisite | PASS: `proof.exe check --daVinci -e --no-fail proof.toml <4 guides>` returned OK and output contained no `FAIL` |
| Editorial repair | PASS: roots/soils, stems/wood, leaves/photosynthesis, and flowers/reproduction cheat sheets rebuilt as diagnostic tables |
| R2 panel | PASS: guide-specific scoring, reader tasks, and adversarial closure recorded |
| Registry update | PASS: only these four repaired guides restored to Current Certified Gold |

## Closeout

Wave 13 sample 1 restores four botany guides with reset-era R2 evidence.

