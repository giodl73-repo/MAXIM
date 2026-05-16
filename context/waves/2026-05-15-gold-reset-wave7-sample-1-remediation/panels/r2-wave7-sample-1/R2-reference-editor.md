# R2 Reference Editor Panel - Gold Reset Wave 7 Sample 1

## Scope

| Guide | Invariant | Score |
|---|---|---:|
| `signal-processing/04-CONVOLUTION-CORRELATION.md` | `convolution-correlation-operations` | 4.6 |
| `signal-processing/05-Z-TRANSFORM.md` | `z-transform-correspondence` | 4.6 |
| `signal-processing/06-STOCHASTIC-SIGNALS.md` | `stochastic-signal-framework` | 4.6 |
| `signal-processing/07-SPECTRAL-ESTIMATION.md` | `spectral-estimation-problem` | 4.6 |

## Findings

| Role | Finding | Disposition |
|---|---|---|
| reference-editor | All four guides already used the reset target diagnostic decision table rather than factory-era selector prose. | Confirmed the `If you need to diagnose...` tables and preserved the current guide text. |
| expert-skeptic | Signal-processing claims need caveats about boundary conditions, ROC selection, stationarity, ergodicity, spectral leakage, estimator variance, and model mismatch. | Existing caveats were sufficient for diagnostic use and were verified during panel review. |
| bridge-builder | The guide bodies already bridge time-domain operations, z-domain reasoning, stochastic modeling, and spectral estimation. | Preserved bridges; cheat sheets route reader diagnosis rather than giving broad recommendations. |
| index-weaver | Cross-reference sections were present and proof-clean. | No link rewiring required. |

## Guide Notes

| Guide | Reader-Task Evidence |
|---|---|
| `signal-processing/04-CONVOLUTION-CORRELATION.md` | Reader can diagnose convolution/correlation claims by separating LTI response, matched filtering, alignment, Fourier duality, boundary handling, and normalization. |
| `signal-processing/05-Z-TRANSFORM.md` | Reader can diagnose discrete-system claims by separating poles, zeros, ROC, causality, stability, inverse transforms, and transfer-function use. |
| `signal-processing/06-STOCHASTIC-SIGNALS.md` | Reader can diagnose stochastic-signal claims by separating process model, stationarity, autocorrelation, PSD, filtering, estimation, and ergodic assumptions. |
| `signal-processing/07-SPECTRAL-ESTIMATION.md` | Reader can diagnose spectral-estimation claims by separating leakage, windowing, averaging, resolution, estimator variance, parametric assumptions, and bias. |

## Verdict

PASS. All four guides satisfy Current Certified Gold after reset-era confirmation,
proof/Da Vinci validation, and guide-specific reader-task review.

