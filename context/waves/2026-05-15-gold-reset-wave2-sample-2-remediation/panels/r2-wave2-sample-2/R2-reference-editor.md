# R2 Reference Editor Panel - Gold Reset Wave 2 Sample 2

## Scope

| Guide | Invariant | Score |
|---|---|---:|
| `abstract-algebra/08-MODULES-LINEAR-ALGEBRA.md` | `modules-vector-spaces-over-rings` | 4.6 |
| `abstract-algebra/09-CATEGORY-THEORY.md` | `category-theory-structure-language` | 4.6 |
| `abstract-algebra/10-APPLICATIONS.md` | `abstract-algebra-applications` | 4.6 |
| `acoustics/07-UNDERWATER-ACOUSTICS.md` | `underwater-acoustics-applications` | 4.6 |

## Findings

| Role | Finding | Disposition |
|---|---|---|
| reference-editor | All four guides retained structure/concept/application selector tables without explicit diagnostic caveats. | Rebuilt each as a diagnostic `If you need to diagnose...` table. |
| expert-skeptic | Claims need caveats about non-field scalars, PID hypotheses, tensor torsion, categorical laws, universal properties, algebraic-crypto assumptions, code parameters, finite-field implementation, sound-speed profiles, multipath, Doppler, and ocean variability. | Added caveats for each diagnostic claim. |
| bridge-builder | The guide bodies already bridge modules, category theory, algebra applications, and underwater acoustics. | Preserved bridges; cheat sheets now route diagnostic use. |
| index-weaver | Cross-reference sections were present and proof-clean. | No link rewiring required. |

## Guide Notes

| Guide | Reader-Task Evidence |
|---|---|
| `abstract-algebra/08-MODULES-LINEAR-ALGEBRA.md` | Reader can diagnose module claims by separating ring scalars, classification hypotheses, operator modules, projective/injective tests, tensor products, and group representations. |
| `abstract-algebra/09-CATEGORY-THEORY.md` | Reader can diagnose category-theory claims by separating arrows, functor laws, naturality, adjunctions, Yoneda, limits, colimits, monads, and Cartesian closure. |
| `abstract-algebra/10-APPLICATIONS.md` | Reader can diagnose applied-algebra claims by separating coding, crystallography, ECC, Module-LWE, storage, quantum gates, pairings, ZK, IBE, QEC, and AG-code assumptions. |
| `acoustics/07-UNDERWATER-ACOUSTICS.md` | Reader can diagnose underwater-acoustics claims by separating SOFAR, USBL, echo sounding, mapping frequency, modem limits, thermocline placement, and thermometry path effects. |

## Verdict

PASS. All four guides satisfy Current Certified Gold after reset-era repair,
proof/Da Vinci validation, and guide-specific reader-task review.

