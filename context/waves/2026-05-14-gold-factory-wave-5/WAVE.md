# Gold Factory Wave 5

## Mission

Continue scaled Gold promotion with a proof-clean math cohort across
probability/statistics and differential geometry. Preserve the factory rule:
promote clean exact files, polish cross-references, attach Da Vinci invariants,
and defer noisy files to explicit repair lanes.

## Scope

| Guide | Promotion Target | Invariant |
|---|---|---|
| `probability-statistics/02-RANDOM-VARIABLES.md` | distribution family exemplar | `random-variable-distribution-families` |
| `probability-statistics/03-LIMIT-THEOREMS.md` | LLN/CLT hierarchy exemplar | `limit-theorem-hierarchy` |
| `probability-statistics/04-STOCHASTIC-PROCESSES.md` | stochastic process taxonomy exemplar | `stochastic-process-taxonomy` |
| `probability-statistics/05-STATISTICAL-INFERENCE.md` | inference framework exemplar | `statistical-inference-framework` |
| `probability-statistics/06-BAYESIAN-STATISTICS.md` | Bayesian workflow exemplar | `bayesian-workflow` |
| `probability-statistics/07-REGRESSION-MODELS.md` | regression model taxonomy exemplar | `regression-taxonomy` |
| `probability-statistics/08-TIME-SERIES.md` | time series landscape exemplar | `time-series-landscape` |
| `probability-statistics/09-INFORMATION-GEOMETRY.md` | statistical-manifold exemplar | `probability-information-geometry` |
| `differential-geometry/01-MANIFOLDS.md` | smooth manifold construction exemplar | `smooth-manifold-construction` |
| `differential-geometry/02-TANGENT-BUNDLES.md` | tangent/cotangent bundle exemplar | `tangent-cotangent-bundle-hierarchy` |
| `differential-geometry/03-DIFFERENTIAL-FORMS.md` | differential forms exemplar | `differential-forms-landscape` |
| `differential-geometry/05-CONNECTIONS.md` | connection and parallel transport exemplar | `connections-overview` |

## Baseline Findings

| Finding | Resolution |
|---|---|
| Probability/statistics 02-09 proofed clean as exact files | Selected all eight for a coherent probability-to-statistics ladder |
| Differential geometry 01, 02, 03, 05, 06, and 08 proofed clean | Selected four foundational files to complete a 12-guide cohort |
| Differential geometry 04, 07, and 09 had ASCII/table defects | Deferred to a targeted differential-geometry repair lane |
| Cross-reference sections were missing in the selected files | Added before Decision Cheat Sheet without changing core exposition |

## Gold Rubric v2 Scores

| Guide | Explanation | Diagrams | Tables | Bridges | Cross-links | Proof | Overall |
|---|---:|---:|---:|---:|---:|---:|---:|
| `probability-statistics/02-RANDOM-VARIABLES.md` | 4.6 | 4.6 | 4.6 | 4.7 | 4.6 | 5.0 | 4.6 |
| `probability-statistics/03-LIMIT-THEOREMS.md` | 4.7 | 4.6 | 4.6 | 4.8 | 4.6 | 5.0 | 4.6 |
| `probability-statistics/04-STOCHASTIC-PROCESSES.md` | 4.6 | 4.6 | 4.6 | 4.7 | 4.6 | 5.0 | 4.6 |
| `probability-statistics/05-STATISTICAL-INFERENCE.md` | 4.6 | 4.6 | 4.6 | 4.7 | 4.6 | 5.0 | 4.6 |
| `probability-statistics/06-BAYESIAN-STATISTICS.md` | 4.6 | 4.6 | 4.6 | 4.8 | 4.6 | 5.0 | 4.6 |
| `probability-statistics/07-REGRESSION-MODELS.md` | 4.6 | 4.6 | 4.6 | 4.7 | 4.6 | 5.0 | 4.6 |
| `probability-statistics/08-TIME-SERIES.md` | 4.6 | 4.6 | 4.6 | 4.7 | 4.6 | 5.0 | 4.6 |
| `probability-statistics/09-INFORMATION-GEOMETRY.md` | 4.6 | 4.6 | 4.6 | 4.8 | 4.6 | 5.0 | 4.6 |
| `differential-geometry/01-MANIFOLDS.md` | 4.6 | 4.6 | 4.6 | 4.7 | 4.6 | 5.0 | 4.6 |
| `differential-geometry/02-TANGENT-BUNDLES.md` | 4.6 | 4.6 | 4.6 | 4.7 | 4.6 | 5.0 | 4.6 |
| `differential-geometry/03-DIFFERENTIAL-FORMS.md` | 4.7 | 4.6 | 4.6 | 4.8 | 4.6 | 5.0 | 4.6 |
| `differential-geometry/05-CONNECTIONS.md` | 4.6 | 4.6 | 4.6 | 4.7 | 4.6 | 5.0 | 4.6 |

## Reader-Task Checks

| Task Family | Representative Pass |
|---|---|
| Probability ladder | Random variables, limit theorems, stochastic processes, inference, Bayesian statistics, regression, time series, and information geometry form a coherent statistics sequence |
| Geometry foundation | Manifolds, tangent/cotangent bundles, differential forms, and connections establish coordinate-free calculus |
| Cross-domain bridge | Information geometry now links probability/statistics to differential geometry and information theory |

## Validation

```powershell
git -C C:\src\maxim diff --check
Set-Location -LiteralPath C:\src\maxim
C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml probability-statistics\02-RANDOM-VARIABLES.md probability-statistics\03-LIMIT-THEOREMS.md probability-statistics\04-STOCHASTIC-PROCESSES.md probability-statistics\05-STATISTICAL-INFERENCE.md probability-statistics\06-BAYESIAN-STATISTICS.md probability-statistics\07-REGRESSION-MODELS.md probability-statistics\08-TIME-SERIES.md probability-statistics\09-INFORMATION-GEOMETRY.md differential-geometry\01-MANIFOLDS.md differential-geometry\02-TANGENT-BUNDLES.md differential-geometry\03-DIFFERENTIAL-FORMS.md differential-geometry\05-CONNECTIONS.md
C:\src\proof\target\debug\proof.exe check -e --no-fail context\gold\REGISTRY.md context\waves\2026-05-14-gold-factory-wave-5\WAVE.md context\waves\PHASES.md
```

## Decision

Promote all twelve selected guides to Certified Gold. Defer the noisy
differential-geometry exact files to a repair wave rather than diluting the
proof-clean gate.
