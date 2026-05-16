# R2 Consolidated Panel - Gold Reset Wave 6 Sample 1

## Verdict

PASS. The Wave 6 PDE classification, first-order PDE, wave equation, and heat
equation sample satisfies Gold Rubric v2 after targeted repair, proof/Da Vinci
validation, and guide-specific R2 review.

## Certified Scope

| Guide | Score | Invariant | Decision |
|---|---:|---|---|
| `partial-differential-equations/01-CLASSIFICATION.md` | 4.6 | `pde-classification-determines` | Certified Gold |
| `partial-differential-equations/02-FIRST-ORDER.md` | 4.6 | `first-order-pde-taxonomy` | Certified Gold |
| `partial-differential-equations/03-WAVE-EQUATION.md` | 4.6 | `wave-equation-landscape` | Certified Gold |
| `partial-differential-equations/04-HEAT-EQUATION.md` | 4.6 | `heat-equation-landscape` | Certified Gold |

## Evidence Categories

| Required Evidence | Result |
|---|---|
| Proof output parsed for literal `FAIL` | PASS: focused command exited cleanly and contained no `FAIL` |
| Da Vinci invariants | PASS: all four scoped invariants present |
| Guide-specific rubric notes | PASS: see `R2-reference-editor.md` |
| Adversarial findings | PASS: question/situation selector table issues repaired |
| Reader-task check | PASS: all four guides support diagnostic reader decisions |
| BLOCK/WARN status | PASS: no remaining BLOCK or WARN findings |

## Reader-Task Checks

| Guide | Reader Task | Result |
|---|---|---|
| `partial-differential-equations/01-CLASSIFICATION.md` | Diagnose PDE classification claims by separating type, data placement, domains of dependence, uniqueness tools, and weak existence. | PASS |
| `partial-differential-equations/02-FIRST-ORDER.md` | Diagnose first-order PDE claims by separating characteristics, shock formation, entropy conditions, rarefactions, viscosity solutions, and jump speeds. | PASS |
| `partial-differential-equations/03-WAVE-EQUATION.md` | Diagnose wave claims by separating d'Alembert/Kirchhoff formulas, Huygens behavior, energy, modes, dispersion, solitons, and impedance reflection. | PASS |
| `partial-differential-equations/04-HEAT-EQUATION.md` | Diagnose heat claims by separating Gaussian diffusion, scaling, eigenmode decay, backward instability, maximum principles, positivity, and reaction-diffusion patterns. | PASS |

## Certification Rule Applied

Factory hardening made these guides Candidate-Hardened. Current Certified Gold
is restored only because reset-era repair and this R2 panel supply guide-specific
evidence.

