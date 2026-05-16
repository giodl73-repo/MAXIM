# R2 Reference Editor Review - Gold Reset Wave 27 Sample 4

## Scope

| Guide | Invariant |
|---|---|
| `computing/15-OBSERVABILITY.md` | `monitoring-vs-observability` |
| `computing/16-MONOREPO.md` | `polyrepo-vs-monorepo` |
| `computing/18-TESTING.md` | `testing-landscape` |
| `computing/20-AZURE.md` | `azure-service-categories` |

## Rubric Findings

| Guide | Score | Note |
|---|---:|---|
| `computing/15-OBSERVABILITY.md` | 4.6 | Observability guidance now separates telemetry type, backend choice, propagation, alert semantics, query model, histogram precision, SLO alignment, and vendor boundary caveats. |
| `computing/16-MONOREPO.md` | 4.6 | Monorepo guidance now separates workspace sharing, affected graph accuracy, cache hermeticity, Turbo/Nx tradeoffs, pnpm behavior, boundaries, versioning, and filtered-test safety. |
| `computing/18-TESTING.md` | 4.6 | Testing guidance now separates test layer, mock boundary, real-stack value, browser scope, visual stability, accessibility limits, snapshot risk, coverage meaning, and contract testing. |
| `computing/20-AZURE.md` | 4.6 | Azure guidance now separates hosting, storage, data, messaging, identity, routing, AI, cost, hybrid, and IaC categories with operational caveats. |

## Adversarial Closure

| Concern | Closure |
|---|---|
| Cheat sheets were lookup tables. | Rebuilt all four as diagnostic tables with explicit caveats. |
| Observability/testing choices could be used as recipes. | Added semantic limits around telemetry, SLOs, mocks, E2E, snapshots, coverage, and contracts. |
| Monorepo/Azure choices could hide ownership cost. | Added graph, cache, boundary, platform, identity, lifecycle, and operations caveats. |

No BLOCK or WARN findings remain for the scoped Gold claims.

