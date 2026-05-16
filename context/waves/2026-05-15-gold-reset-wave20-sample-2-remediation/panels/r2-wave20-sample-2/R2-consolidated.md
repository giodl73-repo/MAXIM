# R2 Consolidated Panel - Gold Reset Wave 20 Sample 2

## Verdict

PASS. The Wave 20 mixed DSP/quantum sample satisfies Gold Rubric v2 after
targeted repair, proof/Da Vinci validation, and guide-specific R2 review.

## Certified Scope

| Guide | Score | Invariant | Decision |
|---|---:|---|---|
| `signal-processing/08-WAVELETS.md` | 4.6 | `wavelets-fourier-time-frequency` | Certified Gold |
| `signal-processing/09-APPLICATIONS.md` | 4.6 | `dsp-application-map` | Certified Gold |
| `quantum-computing/02-ALGORITHMS.md` | 4.6 | `quantum-algorithm-landscape` | Certified Gold |
| `quantum-computing/03-ERROR-CORRECTION.md` | 4.6 | `quantum-error-correction-landscape` | Certified Gold |

## Evidence Categories

| Required Evidence | Result |
|---|---|
| Proof output parsed for literal `FAIL` | PASS: focused command exited cleanly and contained no `FAIL` |
| Da Vinci invariants | PASS: all four scoped invariants present |
| Guide-specific rubric notes | PASS: see `R2-reference-editor.md` |
| Adversarial findings | PASS: application-selector and direct-answer table issues repaired |
| Reader-task check | PASS: all four guides support diagnostic reader decisions |
| BLOCK/WARN status | PASS: no remaining BLOCK or WARN findings |

## Reader-Task Checks

| Guide | Reader Task | Result |
|---|---|---|
| `signal-processing/08-WAVELETS.md` | Diagnose wavelet choice by separating image, edge, audio, biomedical, geophysical, denoising, and interpretability requirements. | PASS |
| `signal-processing/09-APPLICATIONS.md` | Diagnose DSP application choices by separating filter, transform, convolution, radar, ECG, speech, classification, and image kernels. | PASS |
| `quantum-computing/02-ALGORITHMS.md` | Diagnose quantum algorithm claims by separating Grover, AES, Shor, NP-complete limits, near-term simulation, HHL, and variational methods. | PASS |
| `quantum-computing/03-ERROR-CORRECTION.md` | Diagnose QEC by separating no-cloning, syndrome measurement, thresholds, T-gate overhead, physical/logical scale, decoders, CRQC, and Eastin-Knill. | PASS |

## Certification Rule Applied

Factory hardening made these guides Candidate-Hardened. Current Certified Gold
is restored only because reset-era repair and this R2 panel supply guide-specific
evidence.

