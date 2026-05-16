# Gold Factory Wave 7

## Mission

Continue scaled Gold promotion with a proof-clean signal-processing and
control-theory cohort. Use exact-file scouting, defer the only noisy candidate,
polish cross-references, and protect every promoted opening figure with Da
Vinci invariants.

## Scope

| Guide | Promotion Target | Invariant |
|---|---|---|
| `signal-processing/04-CONVOLUTION-CORRELATION.md` | convolution/correlation exemplar | `convolution-correlation-operations` |
| `signal-processing/05-Z-TRANSFORM.md` | discrete transform exemplar | `z-transform-correspondence` |
| `signal-processing/06-STOCHASTIC-SIGNALS.md` | stochastic signal exemplar | `stochastic-signal-framework` |
| `signal-processing/07-SPECTRAL-ESTIMATION.md` | PSD estimation exemplar | `spectral-estimation-problem` |
| `signal-processing/08-WAVELETS.md` | wavelet time-frequency exemplar | `wavelet-fourier-limitation` |
| `signal-processing/09-APPLICATIONS.md` | DSP application map exemplar | `dsp-application-map` |
| `control-theory/02-STATE-SPACE.md` | state-space exemplar | `state-space-mental-model` |
| `control-theory/03-OPTIMAL-CONTROL.md` | optimal-control exemplar | `optimal-control-paths` |
| `control-theory/04-KALMAN-FILTER.md` | state-estimation exemplar | `state-estimation-landscape` |
| `control-theory/05-ROBUST-CONTROL.md` | robust-control exemplar | `robust-control-framework` |
| `control-theory/06-NONLINEAR-CONTROL.md` | nonlinear-control exemplar | `nonlinear-control-taxonomy` |
| `control-theory/07-MPC.md` | MPC exemplar | `model-predictive-control-core` |

## Baseline Findings

| Finding | Resolution |
|---|---|
| Signal-processing 04-09 proofed clean | Selected all six remaining core signal-processing guides |
| Control-theory 02-07 proofed clean | Selected six modern-control guides for a coherent control lane |
| `machine-learning-theory/05-KERNEL-METHODS.md` had table-column defects | Deferred to a targeted machine-learning-theory repair lane |
| Control-theory 05-07 used topic-specific `## Big Picture:` headings | Normalized to `## The Big Picture` before adding invariants |
| Cross-reference sections were missing in the selected guides | Added before Decision Cheat Sheet |

## Gold Rubric v2 Scores

| Guide | Explanation | Diagrams | Tables | Bridges | Cross-links | Proof | Overall |
|---|---:|---:|---:|---:|---:|---:|---:|
| `signal-processing/04-CONVOLUTION-CORRELATION.md` | 4.6 | 4.6 | 4.6 | 4.8 | 4.6 | 5.0 | 4.6 |
| `signal-processing/05-Z-TRANSFORM.md` | 4.6 | 4.6 | 4.6 | 4.7 | 4.6 | 5.0 | 4.6 |
| `signal-processing/06-STOCHASTIC-SIGNALS.md` | 4.6 | 4.6 | 4.6 | 4.7 | 4.6 | 5.0 | 4.6 |
| `signal-processing/07-SPECTRAL-ESTIMATION.md` | 4.6 | 4.6 | 4.6 | 4.7 | 4.6 | 5.0 | 4.6 |
| `signal-processing/08-WAVELETS.md` | 4.6 | 4.6 | 4.6 | 4.8 | 4.6 | 5.0 | 4.6 |
| `signal-processing/09-APPLICATIONS.md` | 4.6 | 4.6 | 4.6 | 4.7 | 4.6 | 5.0 | 4.6 |
| `control-theory/02-STATE-SPACE.md` | 4.6 | 4.6 | 4.6 | 4.8 | 4.6 | 5.0 | 4.6 |
| `control-theory/03-OPTIMAL-CONTROL.md` | 4.7 | 4.6 | 4.6 | 4.8 | 4.6 | 5.0 | 4.6 |
| `control-theory/04-KALMAN-FILTER.md` | 4.7 | 4.6 | 4.6 | 4.8 | 4.6 | 5.0 | 4.6 |
| `control-theory/05-ROBUST-CONTROL.md` | 4.6 | 4.6 | 4.6 | 4.8 | 4.6 | 5.0 | 4.6 |
| `control-theory/06-NONLINEAR-CONTROL.md` | 4.6 | 4.6 | 4.6 | 4.7 | 4.6 | 5.0 | 4.6 |
| `control-theory/07-MPC.md` | 4.6 | 4.6 | 4.6 | 4.8 | 4.6 | 5.0 | 4.6 |

## Reader-Task Checks

| Task Family | Representative Pass |
|---|---|
| Signal-processing core | Convolution, z-transform, stochastic signals, spectral estimation, wavelets, and applications complete the DSP ladder |
| Modern control ladder | State-space, optimal control, Kalman filtering, robust control, nonlinear control, and MPC form a coherent advanced-control sequence |
| Signal-control bridge | Stochastic signals and Kalman filtering connect measurement noise, estimation, and feedback design |

## Validation

```powershell
git -C C:\src\maxim diff --check
Set-Location -LiteralPath C:\src\maxim
C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml signal-processing\04-CONVOLUTION-CORRELATION.md signal-processing\05-Z-TRANSFORM.md signal-processing\06-STOCHASTIC-SIGNALS.md signal-processing\07-SPECTRAL-ESTIMATION.md signal-processing\08-WAVELETS.md signal-processing\09-APPLICATIONS.md control-theory\02-STATE-SPACE.md control-theory\03-OPTIMAL-CONTROL.md control-theory\04-KALMAN-FILTER.md control-theory\05-ROBUST-CONTROL.md control-theory\06-NONLINEAR-CONTROL.md control-theory\07-MPC.md
C:\src\proof\target\debug\proof.exe check -e --no-fail context\gold\REGISTRY.md context\waves\2026-05-14-gold-factory-wave-7\WAVE.md context\waves\PHASES.md
```

## Decision

Promote all twelve selected guides to Certified Gold. Defer the noisy
kernel-methods file to a focused repair lane rather than mixing repair work into
the proof-clean factory wave.
