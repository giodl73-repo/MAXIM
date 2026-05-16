# R2 Reference Editor Panel - Gold Reset Wave 20 Sample 1

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
| reference-editor | Factory-era selector tables routed readers to methods without diagnostic caveats. | Repaired into diagnostic `If you need to diagnose...` tables. |
| expert-skeptic | DSP method choice depends on assumptions about padding, stationarity, model order, and numerical implementation. | Added caveats for circular aliasing, ROC, ergodicity, PSD resolution, and subspace assumptions. |
| bridge-builder | Existing guide bodies already bridge operations, transforms, and estimation workflows. | Preserved bridges; cheat sheets now support diagnostic routing. |
| index-weaver | Cross-reference sections were present and proof-clean. | No link rewiring required. |

## Guide Notes

| Guide | Reader-Task Evidence |
|---|---|
| `signal-processing/04-CONVOLUTION-CORRELATION.md` | Reader can diagnose convolution/correlation choices by separating finite/streaming convolution, FFT padding, matched filtering, delay, energy, periodicity, and image filtering. |
| `signal-processing/05-Z-TRANSFORM.md` | Reader can diagnose discrete-system questions by separating poles, ROC, unit-circle response, notch/resonator placement, difference equations, and biquad implementation. |
| `signal-processing/06-STOCHASTIC-SIGNALS.md` | Reader can diagnose stochastic signals by separating PSD, autocorrelation, filtering, coherence, delay, thermal noise, stationarity, and Welch estimates. |
| `signal-processing/07-SPECTRAL-ESTIMATION.md` | Reader can diagnose spectral estimation by separating Welch, multitaper, AR modeling, subspace methods, model order, Goertzel, and STFT tradeoffs. |

## Verdict

PASS. All four guides satisfy Current Certified Gold after reset-era repair,
proof/Da Vinci validation, and guide-specific reader-task review.

