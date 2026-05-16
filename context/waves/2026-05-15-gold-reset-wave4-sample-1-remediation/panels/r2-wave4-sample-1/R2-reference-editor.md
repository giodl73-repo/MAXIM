# R2 Reference Editor Panel - Gold Reset Wave 4 Sample 1

## Scope

| Guide | Invariant | Score |
|---|---|---:|
| `information-theory/02-SOURCE-CODING.md` | `source-coding-landscape` | 4.6 |
| `information-theory/04-ML-CRYPTOGRAPHY-BRIDGE.md` | `information-theory-ml-crypto-quantum` | 4.6 |
| `information-theory/06-NETWORK-INFORMATION-THEORY.md` | `network-information-theory-primitives` | 4.6 |
| `information-theory/07-ALGORITHMIC-INFORMATION.md` | `kolmogorov-complexity` | 4.6 |

## Findings

| Role | Finding | Disposition |
|---|---|---|
| reference-editor | All four guides retained selector tables without explicit diagnostic caveats. | Rebuilt each as a diagnostic `If you need to diagnose...` table. |
| expert-skeptic | Information-theory claims need caveats about source models, perceptual quality, asymptotics, uncomputability, bound looseness, security assumptions, channel models, CSI, side information, and effective randomness tests. | Added caveats for each diagnostic claim. |
| bridge-builder | The guide bodies already bridge compression, ML/crypto, network coding, and algorithmic information. | Preserved bridges; cheat sheets now route diagnostic use. |
| index-weaver | Cross-reference sections were present and proof-clean. | No link rewiring required. |

## Guide Notes

| Guide | Reader-Task Evidence |
|---|---|
| `information-theory/02-SOURCE-CODING.md` | Reader can diagnose source-coding choices by separating source type, loss tolerance, model cost, entropy coding, universality, and rate-distortion limits. |
| `information-theory/04-ML-CRYPTOGRAPHY-BRIDGE.md` | Reader can diagnose ML/crypto bridges by separating KL direction, variational bounds, MI bounds, MDL, IB, GAN/divergence theory, secrecy models, and QKD assumptions. |
| `information-theory/06-NETWORK-INFORMATION-THEORY.md` | Reader can diagnose network-information claims by separating MAC, broadcast, interference, relay, MIMO, network coding, and side-information compression settings. |
| `information-theory/07-ALGORITHMIC-INFORMATION.md` | Reader can diagnose algorithmic-information claims by separating entropy, Kolmogorov complexity, MDL proxies, incompressibility, logical depth, physical erasure, universal prediction, and effective randomness. |

## Verdict

PASS. All four guides satisfy Current Certified Gold after reset-era repair,
proof/Da Vinci validation, and guide-specific reader-task review.

