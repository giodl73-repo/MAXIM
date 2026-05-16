# R2 Consolidated Panel - Gold Reset Wave 36 Sample 2

## Verdict

PASS. The second Wave 36 reset sample satisfies Gold Rubric v2 after targeted
editorial repair, proof/Da Vinci validation, and guide-specific R2 review.

## Certified Scope

| Guide | Score | Invariant | Decision |
|---|---:|---|---|
| `formal-methods/03-THEOREM-PROVING.md` | 4.6 | `proof-assistant-landscape` | Certified Gold |
| `formal-methods/04-TYPE-THEORY.md` | 4.6 | `type-theory-hierarchy` | Certified Gold |
| `freshwater-biology/00-OVERVIEW.md` | 4.6 | `freshwater-biology-landscape` | Certified Gold |

## Evidence Categories

| Required Evidence | Result |
|---|---|
| Proof output parsed for literal `FAIL` | PASS: focused command exited cleanly and contained no `FAIL` |
| Da Vinci invariants | PASS: all three scoped invariants present |
| Guide-specific rubric notes | PASS: see `R2-reference-editor.md` |
| Adversarial findings | PASS: lookup tables and false univalence overclaim repaired |
| Reader-task check | PASS: all three guides now support diagnostic reader decisions |
| BLOCK/WARN status | PASS: no remaining BLOCK or WARN findings |

## Reader-Task Checks

| Guide | Reader Task | Result |
|---|---|---|
| `formal-methods/03-THEOREM-PROVING.md` | Choose a proof assistant or verification workflow while naming trust-boundary assumptions. | PASS |
| `formal-methods/04-TYPE-THEORY.md` | Select the relevant type-system feature and identify its inference, soundness, or expressiveness tradeoff. | PASS |
| `freshwater-biology/00-OVERVIEW.md` | Route a freshwater problem through stratification, river continuum, wetland, nutrient, food-web, conservation, or water-quality frames. | PASS |

## Certification Rule Applied

Factory hardening made these guides Candidate-Hardened. Current Certified Gold
is restored only because reset-era repair and this R2 panel supply guide-specific
evidence.

