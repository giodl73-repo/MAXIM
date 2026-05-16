# R2 Reference Editor Panel - Gold Reset Wave 4 Final

## Scope

| Guide | Invariant | Score |
|---|---|---:|
| `number-theory/10-CRYPTOGRAPHY-CONNECTIONS.md` | `number-theory-cryptographic-hardness` | 4.6 |
| `signal-processing/01-FOURIER-ANALYSIS.md` | `fourier-family-tree` | 4.6 |
| `signal-processing/02-SAMPLING-THEORY.md` | `sampling-pipeline` | 4.6 |
| `signal-processing/03-FILTERS.md` | `digital-filter-taxonomy` | 4.6 |

## Findings

| Role | Finding | Disposition |
|---|---|---|
| reference-editor | All four guides retained selector tables without explicit diagnostic caveats. | Rebuilt each as a diagnostic `If you need to diagnose...` table. |
| expert-skeptic | Crypto and signal-processing claims need caveats about padding, subgroup/curve parameters, implementation security, sampling margins, filter rolloff, ADC limits, window tradeoffs, group delay, and hardware tolerances. | Added caveats for each diagnostic claim. |
| bridge-builder | The guide bodies already bridge number-theoretic hardness and Fourier/sampling/filter implementation. | Preserved bridges; cheat sheets now route diagnostic use. |
| index-weaver | Cross-reference sections were present and proof-clean. | No link rewiring required. |

## Guide Notes

| Guide | Reader-Task Evidence |
|---|---|
| `number-theory/10-CRYPTOGRAPHY-CONNECTIONS.md` | Reader can diagnose crypto-number-theory claims by separating RSA arithmetic, padding, DH/ECDH groups, lattice assumptions, finite-field arithmetic, and quantum attacks. |
| `signal-processing/01-FOURIER-ANALYSIS.md` | Reader can diagnose Fourier-analysis choices by separating finite DFT assumptions, continuous transforms, periodic series, window sidelobes/resolution, amplitude accuracy, and FFT algorithms. |
| `signal-processing/02-SAMPLING-THEORY.md` | Reader can diagnose sampling claims by separating sample-rate margin, antialias filtering, oversampling, ADC architecture, aperture limits, and dithering. |
| `signal-processing/03-FILTERS.md` | Reader can diagnose filter choices by separating phase, latency, coefficient count, ripple, pulse integrity, biquad implementation, analog antialiasing, windows, and equiripple design. |

## Verdict

PASS. All four guides satisfy Current Certified Gold after reset-era repair,
proof/Da Vinci validation, and guide-specific reader-task review.

