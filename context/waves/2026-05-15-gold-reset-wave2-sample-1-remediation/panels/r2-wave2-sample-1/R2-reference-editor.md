# R2 Reference Editor Panel - Gold Reset Wave 2 Sample 1

## Scope

| Guide | Invariant | Score |
|---|---|---:|
| `abstract-algebra/02-SUBGROUPS-QUOTIENTS.md` | `quotients-homomorphisms-architecture` | 4.6 |
| `abstract-algebra/04-RINGS-IDEALS.md` | `ring-hierarchy` | 4.6 |
| `abstract-algebra/05-POLYNOMIALS-FIELDS.md` | `field-extensions-tower` | 4.6 |
| `abstract-algebra/06-GALOIS-THEORY.md` | `galois-correspondence` | 4.6 |

## Findings

| Role | Finding | Disposition |
|---|---|---|
| reference-editor | All four guides retained task/tool/method selector tables without explicit diagnostic caveats. | Rebuilt each as a diagnostic `If you need to diagnose...` table. |
| expert-skeptic | Algebra claims need caveats about normality, quotient well-definedness, semidirect action data, UFD/PID implications, irreducibility tests, finite-field construction, separability/normality, and Galois correspondence hypotheses. | Added caveats for each diagnostic claim. |
| bridge-builder | The guide bodies already bridge group quotients, rings, fields, and Galois theory. | Preserved bridges; cheat sheets now route diagnostic use. |
| index-weaver | Cross-reference sections were present and proof-clean. | No link rewiring required. |

## Guide Notes

| Guide | Reader-Task Evidence |
|---|---|
| `abstract-algebra/02-SUBGROUPS-QUOTIENTS.md` | Reader can diagnose quotient/group-structure claims by separating normality, quotient construction, isomorphism theorem, products, semidirect actions, solvability, and composition factors. |
| `abstract-algebra/04-RINGS-IDEALS.md` | Reader can diagnose ring/ideal claims by separating UFD/PID/Euclidean properties, maximal/prime quotients, root adjunction, domain/field quotients, and localization. |
| `abstract-algebra/05-POLYNOMIALS-FIELDS.md` | Reader can diagnose field-extension claims by separating minimal polynomials, algebraicity, irreducibility, finite-field construction, splitting fields, characteristic, and multiplicative order. |
| `abstract-algebra/06-GALOIS-THEORY.md` | Reader can diagnose Galois claims by separating automorphisms, normal/separable extensions, fixed fields, correspondence, solvability, constructibility, and cyclotomic groups. |

## Verdict

PASS. All four guides satisfy Current Certified Gold after reset-era repair,
proof/Da Vinci validation, and guide-specific reader-task review.

