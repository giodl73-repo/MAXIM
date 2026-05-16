# R2 Reference Editor Review - Gold Reset Wave 31 Sample 1

## Scope

| Guide | Invariant |
|---|---|
| `control-theory/00-OVERVIEW.md` | `control-theory-overview-landscape` |
| `coral-reefs/00-OVERVIEW.md` | `coral-reefs-overview-biodiversity` |
| `coral-reefs/07-REEF-CHEMISTRY.md` | `reef-chemistry-carbonate-cascade` |
| `coral-reefs/08-HUMAN-IMPACTS.md` | `reef-human-impacts-stressor-map` |

## Rubric Findings

| Guide | Score | Note |
|---|---:|---|
| `control-theory/00-OVERVIEW.md` | 4.6 | Control guidance now diagnoses loop scope, oscillation, margins, MIMO coupling, observer assumptions, LQR tradeoffs, MPC constraints, and learning-control risk. |
| `coral-reefs/00-OVERVIEW.md` | 4.6 | Reef overview guidance now diagnoses geomorphology, distribution constraints, biodiversity dependence, carbonate budgets, coral energetics, bleaching reversibility, and intervention limits. |
| `coral-reefs/07-REEF-CHEMISTRY.md` | 4.6 | Reef chemistry guidance now separates pH, carbonate ions, Omega-arag, net accretion, mineral vulnerability, diel swings, local alkalinity, and bleaching/acidification mechanisms. |
| `coral-reefs/08-HUMAN-IMPACTS.md` | 4.6 | Human-impact guidance now diagnoses herbivory, CoTS amplification, physical framework damage, exposure context, protected-area enforcement, cascades, and climate/local-management limits. |

## Adversarial Closure

| Concern | Closure |
|---|---|
| Cheat sheets were answer or selector tables. | Rebuilt all four as diagnostic tables with caveats. |
| Control guidance risked treating tools as guarantees. | Added model-relative margins, sensing, noise, constraint, solver, and sim-to-real caveats. |
| Coral guidance risked fact lookup without ecological context. | Added net budgets, site specificity, scale, exposure, reversibility, and climate/local-stressor caveats. |

No BLOCK or WARN findings remain for the scoped Gold claims.

