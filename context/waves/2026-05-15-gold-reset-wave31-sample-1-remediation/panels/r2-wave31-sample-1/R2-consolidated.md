# R2 Consolidated Panel - Gold Reset Wave 31 Sample 1

## Verdict

PASS. The Wave 31 control-theory/coral-reefs sample satisfies Gold Rubric v2
after targeted repair, proof/Da Vinci validation, and guide-specific R2 review.

## Certified Scope

| Guide | Score | Invariant | Decision |
|---|---:|---|---|
| `control-theory/00-OVERVIEW.md` | 4.6 | `control-theory-overview-landscape` | Certified Gold |
| `coral-reefs/00-OVERVIEW.md` | 4.6 | `coral-reefs-overview-biodiversity` | Certified Gold |
| `coral-reefs/07-REEF-CHEMISTRY.md` | 4.6 | `reef-chemistry-carbonate-cascade` | Certified Gold |
| `coral-reefs/08-HUMAN-IMPACTS.md` | 4.6 | `reef-human-impacts-stressor-map` | Certified Gold |

## Evidence Categories

| Required Evidence | Result |
|---|---|
| Proof output parsed for literal `FAIL` | PASS: focused command exited cleanly and contained no `FAIL` |
| Da Vinci invariants | PASS: all four scoped invariants present |
| Guide-specific rubric notes | PASS: see `R2-reference-editor.md` |
| Adversarial findings | PASS: controller-selection, reef-fact, carbonate-threshold, and human-impact answer table issues repaired |
| Reader-task check | PASS: all four guides support diagnostic reader decisions |
| BLOCK/WARN status | PASS: no remaining BLOCK or WARN findings |

## Reader-Task Checks

| Guide | Reader Task | Result |
|---|---|---|
| `control-theory/00-OVERVIEW.md` | Diagnose a control approach by separating loop scope, dynamics, margins, state modeling, estimation, constraints, robustness, and learning-control risk. | PASS |
| `coral-reefs/00-OVERVIEW.md` | Diagnose a reef claim by separating geomorphology, distribution limits, biodiversity, carbonate construction, energy budget, bleaching, and intervention scale. | PASS |
| `coral-reefs/07-REEF-CHEMISTRY.md` | Diagnose a chemistry claim by separating pH, carbonate ions, saturation state, net accretion, mineral vulnerability, diel swings, local treatment, and heat stress. | PASS |
| `coral-reefs/08-HUMAN-IMPACTS.md` | Diagnose a reef-impact claim by separating herbivory, outbreak dynamics, destructive fishing, toxicity exposure, protected areas, trophic cascades, and climate limits. | PASS |

## Certification Rule Applied

Factory hardening made these guides Candidate-Hardened. Current Certified Gold
is restored only because reset-era repair and this R2 panel supply guide-specific
evidence.

