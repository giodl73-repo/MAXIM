# R2 Reference Editor Panel - Gold Reset Wave 20 Sample 5

## Scope

| Guide | Invariant | Score |
|---|---|---:|
| `differential-geometry/05-CONNECTIONS.md` | `connections-overview` | 4.6 |
| `fluid-dynamics/01-CONTINUUM-MECHANICS.md` | `continuum-mechanics-structure` | 4.6 |
| `fluid-dynamics/02-INVISCID-FLOW.md` | `inviscid-flow-conceptual-structure` | 4.6 |
| `fluid-dynamics/03-VISCOUS-FLOW.md` | `navier-stokes-full-structure` | 4.6 |

## Findings

| Role | Finding | Disposition |
|---|---|---|
| reference-editor | Factory-era concept/use and situation/approach tables were selector-like. | Repaired into diagnostic `If you need to diagnose...` tables. |
| expert-skeptic | Geometry and fluid mechanics require validity caveats about global structure, coordinates, Reynolds regimes, and boundary layers. | Added caveats for non-tensor Christoffels, connection dependence, incompressibility, potential flow, Bernoulli, and scaling. |
| bridge-builder | Existing guide bodies already bridge geometric derivatives and governing-equation fluid reasoning. | Preserved bridges; cheat sheets now support diagnostic routing. |
| index-weaver | Cross-reference sections were present and proof-clean. | No link rewiring required. |

## Guide Notes

| Guide | Reader-Task Evidence |
|---|---|
| `differential-geometry/05-CONNECTIONS.md` | Reader can diagnose connections by separating connection structure, symbols, transport, holonomy, torsion, Levi-Civita uniqueness, geodesics, and curve derivatives. |
| `fluid-dynamics/01-CONTINUUM-MECHANICS.md` | Reader can diagnose continuum mechanics by separating parcel derivatives, mass balance, incompressibility, vorticity, irrotationality, Euler, Navier-Stokes, and vorticity evolution. |
| `fluid-dynamics/02-INVISCID-FLOW.md` | Reader can diagnose inviscid flow by separating potential methods, pressure, cylinder flow, lift, drag paradox, vorticity conservation, and validity limits. |
| `fluid-dynamics/03-VISCOUS-FLOW.md` | Reader can diagnose viscous-flow regimes by separating exact laminar solutions, pressure drop, Stokes flow, high-Re layers, transition, viscous times, and scaling. |

## Verdict

PASS. All four guides satisfy Current Certified Gold after reset-era repair,
proof/Da Vinci validation, and guide-specific reader-task review.

