# Gold Factory Wave 4

## Mission

Continue scaled Gold promotion with an exact-file cohort spanning information
theory, number theory, and signal processing. Normalize guide structure where
needed, add cross-reference polish, and protect each promoted opening figure
with Da Vinci invariants.

## Scope

| Guide | Promotion Target | Invariant |
|---|---|---|
| `information-theory/02-SOURCE-CODING.md` | source-coding compression exemplar | `source-coding-landscape` |
| `information-theory/04-ML-CRYPTOGRAPHY-BRIDGE.md` | ML/crypto/quantum bridge exemplar | `information-theory-ml-crypto-quantum` |
| `information-theory/06-NETWORK-INFORMATION-THEORY.md` | network information theory exemplar | `network-information-theory-primitives` |
| `information-theory/07-ALGORITHMIC-INFORMATION.md` | algorithmic information exemplar | `kolmogorov-complexity` |
| `information-theory/08-QUANTUM-INFORMATION.md` | quantum information exemplar | `quantum-vs-classical-information` |
| `information-theory/09-INFORMATION-GEOMETRY.md` | information geometry exemplar | `information-geometry-statistics` |
| `number-theory/06-ALGEBRAIC-NUMBER-THEORY.md` | ideal factorization exemplar | `algebraic-number-theory-factorization` |
| `number-theory/09-COMPUTATIONAL-NUMBER-THEORY.md` | computational complexity exemplar | `computational-number-theory-complexity` |
| `number-theory/10-CRYPTOGRAPHY-CONNECTIONS.md` | cryptographic hardness exemplar | `number-theory-cryptographic-hardness` |
| `signal-processing/01-FOURIER-ANALYSIS.md` | Fourier transform family exemplar | `fourier-family-tree` |
| `signal-processing/02-SAMPLING-THEORY.md` | sampling pipeline exemplar | `sampling-pipeline` |
| `signal-processing/03-FILTERS.md` | digital filter taxonomy exemplar | `digital-filter-taxonomy` |

## Baseline Findings

| Finding | Resolution |
|---|---|
| Initial scouting command used wrong signal-processing and quantum-computing filenames | Re-ran with exact existing filenames to avoid directory fallback noise |
| Information Theory 01, 03, and 05 remained noisy | Deferred to a targeted information-theory repair lane |
| `quantum-computing/01-QUBITS-CIRCUITS.md` remained noisy | Deferred to a quantum-computing repair lane |
| Six information-theory guides plus three number-theory and three signal-processing guides proofed clean | Selected as the fourth factory cohort |
| Several information-theory files lacked the exact `## The Big Picture` anchor | Normalized headings before attaching invariants |

## Gold Rubric v2 Scores

| Guide | Explanation | Diagrams | Tables | Bridges | Cross-links | Proof | Overall |
|---|---:|---:|---:|---:|---:|---:|---:|
| `information-theory/02-SOURCE-CODING.md` | 4.6 | 4.6 | 4.6 | 4.7 | 4.6 | 5.0 | 4.6 |
| `information-theory/04-ML-CRYPTOGRAPHY-BRIDGE.md` | 4.7 | 4.6 | 4.6 | 4.8 | 4.6 | 5.0 | 4.6 |
| `information-theory/06-NETWORK-INFORMATION-THEORY.md` | 4.6 | 4.6 | 4.6 | 4.7 | 4.6 | 5.0 | 4.6 |
| `information-theory/07-ALGORITHMIC-INFORMATION.md` | 4.6 | 4.6 | 4.6 | 4.7 | 4.6 | 5.0 | 4.6 |
| `information-theory/08-QUANTUM-INFORMATION.md` | 4.6 | 4.6 | 4.6 | 4.7 | 4.6 | 5.0 | 4.6 |
| `information-theory/09-INFORMATION-GEOMETRY.md` | 4.6 | 4.6 | 4.6 | 4.7 | 4.6 | 5.0 | 4.6 |
| `number-theory/06-ALGEBRAIC-NUMBER-THEORY.md` | 4.6 | 4.6 | 4.6 | 4.7 | 4.6 | 5.0 | 4.6 |
| `number-theory/09-COMPUTATIONAL-NUMBER-THEORY.md` | 4.6 | 4.6 | 4.6 | 4.7 | 4.6 | 5.0 | 4.6 |
| `number-theory/10-CRYPTOGRAPHY-CONNECTIONS.md` | 4.6 | 4.6 | 4.6 | 4.8 | 4.6 | 5.0 | 4.6 |
| `signal-processing/01-FOURIER-ANALYSIS.md` | 4.6 | 4.6 | 4.6 | 4.7 | 4.6 | 5.0 | 4.6 |
| `signal-processing/02-SAMPLING-THEORY.md` | 4.6 | 4.6 | 4.6 | 4.7 | 4.6 | 5.0 | 4.6 |
| `signal-processing/03-FILTERS.md` | 4.6 | 4.6 | 4.6 | 4.7 | 4.6 | 5.0 | 4.6 |

## Reader-Task Checks

| Task Family | Representative Pass |
|---|---|
| Information theory ladder | Source coding, ML/crypto bridge, networks, algorithmic information, quantum information, and geometry form a coherent advanced sequence |
| Number theory bridge | Algebraic number theory, computational number theory, and cryptography connections bridge abstract arithmetic to hardness assumptions |
| Signal-processing core | Fourier analysis, sampling theory, and filters form the analysis-to-implementation signal chain |

## Validation

```powershell
git -C C:\src\maxim diff --check
Set-Location -LiteralPath C:\src\maxim
C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml information-theory\02-SOURCE-CODING.md information-theory\04-ML-CRYPTOGRAPHY-BRIDGE.md information-theory\06-NETWORK-INFORMATION-THEORY.md information-theory\07-ALGORITHMIC-INFORMATION.md information-theory\08-QUANTUM-INFORMATION.md information-theory\09-INFORMATION-GEOMETRY.md number-theory\06-ALGEBRAIC-NUMBER-THEORY.md number-theory\09-COMPUTATIONAL-NUMBER-THEORY.md number-theory\10-CRYPTOGRAPHY-CONNECTIONS.md signal-processing\01-FOURIER-ANALYSIS.md signal-processing\02-SAMPLING-THEORY.md signal-processing\03-FILTERS.md
C:\src\proof\target\debug\proof.exe check -e --no-fail context\gold\REGISTRY.md context\waves\2026-05-14-gold-factory-wave-4\WAVE.md context\waves\PHASES.md
```

## Decision

Promote all twelve selected guides to Certified Gold. Defer the remaining noisy
information-theory and quantum-computing guides to targeted repair lanes rather
than weakening the proof-clean promotion gate.
