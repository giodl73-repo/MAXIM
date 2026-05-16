# R2 Reference Editor Panel - Gold Reset Wave 20 Final

## Scope

| Guide | Invariant | Score |
|---|---|---:|
| `fluid-dynamics/04-BOUNDARY-LAYERS.md` | `boundary-layer-structure` | 4.6 |
| `fluid-dynamics/05-TURBULENCE.md` | `turbulence-conceptual-map` | 4.6 |
| `fluid-dynamics/06-COMPRESSIBLE-FLOW.md` | `compressible-flow-mach-regimes` | 4.6 |
| `fluid-dynamics/08-HYDRODYNAMICS.md` | `free-surface-flow-landscape` | 4.6 |

## Findings

| Role | Finding | Disposition |
|---|---|---|
| reference-editor | Factory-era situation/tool selectors needed diagnostic caveats. | Repaired into diagnostic `If you need to diagnose...` tables. |
| expert-skeptic | Fluid regime selection needs validity limits for transition, turbulence models, compressibility, shocks, waves, and geophysical scaling. | Added caveats for wall units, RANS/LES/DNS scope, shock irreversibility, real-gas limits, Froude regimes, and empirical roughness. |
| bridge-builder | Existing guide bodies already bridge governing equations to engineering regimes. | Preserved bridges; cheat sheets now support diagnostic routing. |
| index-weaver | Cross-reference sections were present and proof-clean. | No link rewiring required. |

## Guide Notes

| Guide | Reader-Task Evidence |
|---|---|
| `fluid-dynamics/04-BOUNDARY-LAYERS.md` | Reader can diagnose boundary layers by separating thickness, friction, separation, drag, wall layers, transition, and shedding. |
| `fluid-dynamics/05-TURBULENCE.md` | Reader can diagnose turbulence by separating RANS, separation models, heat-transfer correlations, dissipation scale, LES/DNS, spectra, and scale separation. |
| `fluid-dynamics/06-COMPRESSIBLE-FLOW.md` | Reader can diagnose compressible flow by separating Mach thresholds, stagnation states, shocks, nozzle choking, oblique shocks, expansions, shock tubes, and heating. |
| `fluid-dynamics/08-HYDRODYNAMICS.md` | Reader can diagnose hydrodynamics by separating Froude regimes, jumps, wave speed limits, channel flow, Coriolis scaling, stratification, instabilities, and capillarity. |

## Verdict

PASS. All four guides satisfy Current Certified Gold after reset-era repair,
proof/Da Vinci validation, and guide-specific reader-task review.

