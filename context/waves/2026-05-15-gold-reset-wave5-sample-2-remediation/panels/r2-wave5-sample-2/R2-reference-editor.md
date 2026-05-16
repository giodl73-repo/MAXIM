# R2 Reference Editor Panel - Gold Reset Wave 5 Sample 2

## Scope

| Guide | Invariant | Score |
|---|---|---:|
| `probability-statistics/06-BAYESIAN-STATISTICS.md` | `bayesian-workflow` | 4.6 |
| `probability-statistics/07-REGRESSION-MODELS.md` | `regression-taxonomy` | 4.6 |
| `probability-statistics/08-TIME-SERIES.md` | `time-series-landscape` | 4.6 |
| `probability-statistics/09-INFORMATION-GEOMETRY.md` | `probability-information-geometry` | 4.6 |

## Findings

| Role | Finding | Disposition |
|---|---|---|
| reference-editor | All four guides retained selector tables without explicit diagnostic caveats. | Rebuilt each as a diagnostic `If you need to diagnose...` table. |
| expert-skeptic | Bayesian, regression, time-series, and information-geometry claims need caveats about prior convenience, MCMC diagnostics, VI uncertainty, model regularity, residual structure, overdispersion, stationarity, dependence, latent identification, and KL asymmetry. | Added caveats for each diagnostic claim. |
| bridge-builder | The guide bodies already bridge Bayesian workflow, regression families, temporal models, and statistical geometry. | Preserved bridges; cheat sheets now route diagnostic use. |
| index-weaver | Cross-reference sections were present and proof-clean. | No link rewiring required. |

## Guide Notes

| Guide | Reader-Task Evidence |
|---|---|
| `probability-statistics/06-BAYESIAN-STATISTICS.md` | Reader can diagnose Bayesian workflows by separating conjugacy, sampling, approximation, model comparison, hierarchy, and posterior prediction. |
| `probability-statistics/07-REGRESSION-MODELS.md` | Reader can diagnose regression choices by separating outcome type, dispersion, skew, collinearity, sparsity, grouping, and high-dimensional regularization. |
| `probability-statistics/08-TIME-SERIES.md` | Reader can diagnose time-series methods by separating stationarity, trend, seasonality, gaps, multivariate dynamics, volatility, latent structure, and long memory. |
| `probability-statistics/09-INFORMATION-GEOMETRY.md` | Reader can diagnose information-geometry claims by separating Fisher metric, KL direction, natural gradient, dual flatness, EM projection, and robust divergence choice. |

## Verdict

PASS. All four guides satisfy Current Certified Gold after reset-era repair,
proof/Da Vinci validation, and guide-specific reader-task review.

