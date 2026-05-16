# R2 Reference Editor Panel - Gold Reset Wave 20 Sample 2

## Scope

| Guide | Invariant | Score |
|---|---|---:|
| `signal-processing/08-WAVELETS.md` | `wavelets-fourier-time-frequency` | 4.6 |
| `signal-processing/09-APPLICATIONS.md` | `dsp-application-map` | 4.6 |
| `quantum-computing/02-ALGORITHMS.md` | `quantum-algorithm-landscape` | 4.6 |
| `quantum-computing/03-ERROR-CORRECTION.md` | `quantum-error-correction-landscape` | 4.6 |

## Findings

| Role | Finding | Disposition |
|---|---|---|
| reference-editor | Factory-era application and answer tables were too selector-like for Gold closeout. | Repaired into diagnostic `If you need to diagnose...` tables. |
| expert-skeptic | DSP and quantum choices require caveats about assumptions, overhead, and practical advantage. | Added caveats for wavelet tradeoffs, DSP implementation, Grover/Shor limits, VQE/HHL assumptions, and QEC overhead. |
| bridge-builder | Existing guide bodies already bridge applications, algorithms, and engineering constraints. | Preserved bridges; cheat sheets now support diagnostic routing. |
| index-weaver | Cross-reference sections were present and proof-clean. | No link rewiring required. |

## Guide Notes

| Guide | Reader-Task Evidence |
|---|---|
| `signal-processing/08-WAVELETS.md` | Reader can diagnose wavelet choices by separating compression, edges, audio, biomedical, geophysical, denoising, and CWT interpretation cases. |
| `signal-processing/09-APPLICATIONS.md` | Reader can diagnose DSP applications by separating audio, reverb, radar, ECG, speech, classification, and image-processing operations. |
| `quantum-computing/02-ALGORITHMS.md` | Reader can diagnose quantum algorithm claims by separating Grover, Shor, symmetric crypto, NP limits, VQE, HHL, and variational heuristics. |
| `quantum-computing/03-ERROR-CORRECTION.md` | Reader can diagnose QEC claims by separating no-cloning, syndromes, thresholds, T gates, overhead, decoders, CRQC, and Eastin-Knill. |

## Verdict

PASS. All four guides satisfy Current Certified Gold after reset-era repair,
proof/Da Vinci validation, and guide-specific reader-task review.

