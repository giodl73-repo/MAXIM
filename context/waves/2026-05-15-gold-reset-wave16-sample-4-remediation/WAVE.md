---
wave: gold-reset-wave16-sample-4-remediation
date_open: 2026-05-15
date_close: 2026-05-15
status: complete
source_wave: gold-certification-reset
---

# Gold Reset Wave 16 Sample 4 Remediation

## Mission

Repair and re-panel the fourth freshwater-biology Wave 16 sample before
restoring Current Certified Gold.

## Claim Boundary

| Guide | Invariant |
|---|---|
| `freshwater-biology/04-FRESHWATER-ORGANISMS.md` | `freshwater-food-web-structure` |
| `freshwater-biology/05-NUTRIENT-CYCLES.md` | `freshwater-nutrient-system` |
| `freshwater-biology/06-EUTROPHICATION.md` | `eutrophication-cascade` |
| `freshwater-biology/07-AQUATIC-FOOD-WEBS.md` | `aquatic-food-web-lake-system` |

## Pulse Status

| Pulse | Status | Governing Roles | Evidence |
|---|---|---|---|
| 01 - Repair and R2 panel | DONE | reference-editor, expert-skeptic, bridge-builder, index-weaver | `panels/r2-wave16-sample-4/R2-consolidated.md` |

## Validation Gates

| Gate | Result |
|---|---|
| Mechanical prerequisite | PASS: `proof.exe check --daVinci -e --no-fail proof.toml <4 guides>` returned OK and output contained no `FAIL` |
| Editorial repair | PASS: freshwater-organisms, nutrient-cycles, eutrophication, and aquatic-food-webs cheat sheets rebuilt as diagnostic tables |
| R2 panel | PASS: guide-specific scoring, reader tasks, and adversarial closure recorded |
| Registry update | PASS: only these four repaired guides restored to Current Certified Gold |

## Closeout

Wave 16 sample 4 restores four freshwater-biology guides with reset-era R2
evidence.

