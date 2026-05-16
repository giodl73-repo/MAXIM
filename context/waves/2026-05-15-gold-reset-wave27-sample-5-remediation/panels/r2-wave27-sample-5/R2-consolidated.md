# R2 Consolidated Panel - Gold Reset Wave 27 Sample 5

## Verdict

PASS. The Wave 27 mixed computing/construction sample satisfies Gold Rubric v2
after targeted repair, proof/Da Vinci validation, and guide-specific R2 review.

## Certified Scope

| Guide | Score | Invariant | Decision |
|---|---:|---|---|
| `computing/28-CONCURRENCY.md` | 4.6 | `concurrency-landscape` | Certified Gold |
| `construction-materials/01-PREHISTORIC-VERNACULAR.md` | 4.6 | `vernacular-building-strategies` | Certified Gold |
| `construction-materials/02-ANCIENT-MASONRY.md` | 4.6 | `ancient-masonry-systems` | Certified Gold |
| `construction-materials/03-MEDIEVAL-TIMBER.md` | 4.6 | `medieval-structural-evolution` | Certified Gold |

## Evidence Categories

| Required Evidence | Result |
|---|---|
| Proof output parsed for literal `FAIL` | PASS: focused command exited cleanly and contained no `FAIL` |
| Da Vinci invariants | PASS: all four scoped invariants present |
| Guide-specific rubric notes | PASS: see `R2-reference-editor.md` |
| Adversarial findings | PASS: answer-key issues repaired |
| Reader-task check | PASS: all four guides support diagnostic reader decisions |
| BLOCK/WARN status | PASS: no remaining BLOCK or WARN findings |

## Reader-Task Checks

| Guide | Reader Task | Result |
|---|---|---|
| `computing/28-CONCURRENCY.md` | Diagnose a concurrency primitive by separating contention, waiting, fairness, read/write mix, atomic scope, async vs CPU parallelism, actor/channel boundaries, distributed state, reclamation, and memory ordering. | PASS |
| `construction-materials/01-PREHISTORIC-VERNACULAR.md` | Diagnose a vernacular construction choice by separating climate, labor/material availability, breathability, dry-stone stability, mortar compatibility, span limits, thatch pitch, and daub movement. | PASS |
| `construction-materials/02-ANCIENT-MASONRY.md` | Diagnose ancient masonry behavior by separating arch thrust, pointed geometry, concrete chemistry, dome crown stress, stone tradeoffs, lime repair, frost resistance, and vault load paths. | PASS |
| `construction-materials/03-MEDIEVAL-TIMBER.md` | Diagnose medieval timber and lime behavior by separating hydraulic setting, sacrificial mortar, buttress load paths, truss force state, residual wall thrust, vault geometry, green oak, infill movement, and bearing joints. | PASS |

## Certification Rule Applied

Factory hardening made these guides Candidate-Hardened. Current Certified Gold
is restored only because reset-era repair and this R2 panel supply guide-specific
evidence.

