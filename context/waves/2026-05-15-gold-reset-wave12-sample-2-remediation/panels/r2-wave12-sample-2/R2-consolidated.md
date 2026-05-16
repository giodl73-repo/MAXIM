# R2 Consolidated Panel - Gold Reset Wave 12 Sample 2

## Verdict

PASS. The Wave 12 chemotherapy, drug development, gastrulation, and
developmental signaling sample satisfies Gold Rubric v2 after targeted repair,
proof/Da Vinci validation, and guide-specific R2 review.

## Certified Scope

| Guide | Score | Invariant | Decision |
|---|---:|---|---|
| `pharmacology/07-CHEMOTHERAPY.md` | 4.6 | `cancer-pharmacology-landscape` | Certified Gold |
| `pharmacology/08-DRUG-DEVELOPMENT.md` | 4.6 | `drug-development-pipeline` | Certified Gold |
| `developmental-biology/02-GASTRULATION.md` | 4.6 | `gastrulation-overview` | Certified Gold |
| `developmental-biology/03-SIGNALING-PATHWAYS.md` | 4.6 | `developmental-signaling-pathways` | Certified Gold |

## Evidence Categories

| Required Evidence | Result |
|---|---|
| Proof output parsed for literal `FAIL` | PASS: focused command exited cleanly and contained no `FAIL` |
| Da Vinci invariants | PASS: all four scoped invariants present |
| Guide-specific rubric notes | PASS: see `R2-reference-editor.md` |
| Adversarial findings | PASS: selector table issues repaired |
| Reader-task check | PASS: all four guides support diagnostic reader decisions |
| BLOCK/WARN status | PASS: no remaining BLOCK or WARN findings |

## Reader-Task Checks

| Guide | Reader Task | Result |
|---|---|---|
| `pharmacology/07-CHEMOTHERAPY.md` | Diagnose cancer-drug choice by separating tumor type, biomarker, resistance, immunotherapy, and supportive-care context. | PASS |
| `pharmacology/08-DRUG-DEVELOPMENT.md` | Diagnose drug-development stage by separating validation, binding, ADME, NOAEL, MTD, efficacy signal, pivotal endpoint, review, and surveillance. | PASS |
| `developmental-biology/02-GASTRULATION.md` | Diagnose gastrulation events by separating timing, signals, tissue movement, dorsal organizer logic, segmentation, folding, and cardiac induction. | PASS |
| `developmental-biology/03-SIGNALING-PATHWAYS.md` | Diagnose developmental pathway activation by separating Wnt, Notch, and Hedgehog receptor-effector logic and context caveats. | PASS |

## Certification Rule Applied

Factory hardening made these guides Candidate-Hardened. Current Certified Gold
is restored only because reset-era repair and this R2 panel supply guide-specific
evidence.

