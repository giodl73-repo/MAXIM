# R2 Reference Editor Panel - Gold Reset Wave 7 Sample 2

## Scope

| Guide | Invariant | Score |
|---|---|---:|
| `signal-processing/08-WAVELETS.md` | `wavelet-fourier-limitation` | 4.6 |
| `signal-processing/09-APPLICATIONS.md` | `dsp-application-map` | 4.6 |
| `control-theory/02-STATE-SPACE.md` | `state-space-mental-model` | 4.6 |
| `control-theory/03-OPTIMAL-CONTROL.md` | `optimal-control-paths` | 4.6 |

## Findings

| Role | Finding | Disposition |
|---|---|---|
| reference-editor | Two control guides retained selector tables without caveats; the signal-processing guides already used the target diagnostic form. | Rebuilt the control tables into diagnostic `If you need to diagnose...` tables and confirmed the signal-processing tables. |
| expert-skeptic | Wavelet, DSP-application, state-space, and optimal-control claims need caveats about localization tradeoffs, domain-specific assumptions, coordinate choice, stabilizability/detectability, model mismatch, constraints, and HJB dimensionality. | Added or preserved caveats for each diagnostic claim. |
| bridge-builder | The guide bodies already bridge wavelet/DSP use cases and state-space/optimal-control design. | Preserved bridges; cheat sheets now route diagnostic use. |
| index-weaver | Cross-reference sections were present and proof-clean. | No link rewiring required. |

## Guide Notes

| Guide | Reader-Task Evidence |
|---|---|
| `signal-processing/08-WAVELETS.md` | Reader can diagnose wavelet claims by separating localization, scale, wavelet family, multiresolution, denoising/compression use, and boundary artifacts. |
| `signal-processing/09-APPLICATIONS.md` | Reader can diagnose DSP applications by separating signal type, transform/filter need, domain constraints, latency, noise, and deployment assumptions. |
| `control-theory/02-STATE-SPACE.md` | Reader can diagnose state-space claims by separating MIMO modeling, controllability, observability, pole placement, observers, separation, Lyapunov stability, discretization, and transfer-function views. |
| `control-theory/03-OPTIMAL-CONTROL.md` | Reader can diagnose optimal-control choices by separating LQR, LQG, robustness, `H∞`, MPC, PMP, shooting, HJB, DDP/iLQR, and cost tuning. |

## Verdict

PASS. All four guides satisfy Current Certified Gold after reset-era repair,
proof/Da Vinci validation, and guide-specific reader-task review.

