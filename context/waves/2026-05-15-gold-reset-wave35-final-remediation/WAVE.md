---
wave: gold-reset-wave35-final-remediation
date_open: 2026-05-15
date_close: 2026-05-15
status: complete
source_wave: gold-certification-reset
---

# Gold Reset Wave 35 Final Remediation

## Mission

Close the remaining Wave 35 reset backlog by repairing the food-plants cohort,
validating proof/Da Vinci coverage, and restoring Certified Gold only where
reset-era R2 evidence exists.

## Claim Boundary

This wave certifies only:

| Guide | Invariant |
|---|---|
| `food-plants/00-OVERVIEW.md` | `food-plant-vavilov-landscape` |
| `food-plants/02-LEGUMES.md` | `legume-relationship-map` |
| `food-plants/03-ROOT-TUBERS.md` | `root-tuber-crop-comparison` |
| `food-plants/04-FRUITS.md` | `major-fruit-crop-landscape` |
| `food-plants/05-VEGETABLES.md` | `vegetable-botanical-diversity` |
| `food-plants/06-TREE-CROPS.md` | `tree-crops-vs-annuals` |

It does not certify any other historical factory candidates.

## Pulse Status

| Pulse | Status | Governing Roles | Evidence |
|---|---|---|---|
| 01 - Repair and R2 panel | DONE | reference-editor, expert-skeptic, bridge-builder, index-weaver | `panels/r2-wave35-final/R2-consolidated.md` |

## Validation Gates

| Gate | Result |
|---|---|
| Mechanical prerequisite | PASS: `proof.exe check --daVinci -e --no-fail proof.toml <6 guides>` returned OK and output contained no `FAIL` |
| Editorial repair | PASS: food-plant, legume, root/tuber, fruit, vegetable, and tree-crop cheat sheets rebuilt diagnostically; false or overstrong claims corrected |
| R2 panel | PASS: guide-specific scores, reader tasks, and adversarial closure recorded |
| Registry update | PASS: only the six repaired food-plant guides restored to Current Certified Gold |

## Closeout

This final sample completes Wave 35 reset certification with scoped repair,
skeptical review, reader-task evidence, and literal-`FAIL` proof parsing.

