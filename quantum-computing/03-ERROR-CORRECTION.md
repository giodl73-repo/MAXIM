# Quantum Error Correction

## The Big Picture

```
+------------------------------------------------------------------+
|               QUANTUM ERROR CORRECTION LANDSCAPE                  |
+------------------------------------------------------------------+
|                                                                    |
|  WHY IT'S HARD               HOW IT WORKS                        |
|  ─────────────────            ─────────────────                   |
|  No-cloning: can't copy       Encode logical qubit in             |
|  Measurement destroys state   entangled multi-qubit state         |
|  Errors are continuous        Syndrome measurements detect        |
|  Quantum info fragile         errors without reading state        |
|                                                                    |
|  CODES (historical order)     PRACTICAL PATH                      |
|  ─────────────────────────    ─────────────────────────           |
|  Shor 9-qubit (1995)          Surface code (2D toric)             |
|  Calderbank-Shor-Steane       ~1000 phys. per logical             |
|  CSS codes (1996)             IBM, Google targeting this          |
|  Kitaev toric code (1997)     Threshold theorem: below p*,        |
|  Surface code variants        logical error → 0 as code size ↑    |
+------------------------------------------------------------------+
```

Without error correction, quantum computers are limited to circuits
shallow enough that decoherence doesn't corrupt the computation.
For most useful algorithms (Shor, QPE, HHL), this requires
fault-tolerant quantum computers — still years away.

---

## Why Quantum Error Correction Is Hard

Three fundamental obstacles vs classical error correction:

```
OBSTACLE 1: NO-CLONING
  Classical: back up bit stream, compare, restore from majority
  Quantum:   |ψ⟩ cannot be cloned (no-cloning theorem)
  Solution:  Spread logical qubit across entangled multi-qubit states.
             Syndrome measurements detect error location/type
             without revealing the encoded information.

OBSTACLE 2: MEASUREMENT DESTROYS STATE
  Classical: read bit → extract value directly
  Quantum:   measuring |ψ⟩ = α|0⟩ + β|1⟩ destroys superposition
  Solution:  Ancilla qubits measure error syndromes — parity checks
             on stabilizer generators — without touching logical state.
             E.g., measure ZZ = parity of two qubits: ⟨ZZ⟩ = ±1
             reveals if they're equal/unequal, not their individual values.

OBSTACLE 3: CONTINUOUS ERRORS
  Classical: bit flip is discrete {0→1, 1→0}
  Quantum:   arbitrary rotation error: |0⟩ → cos(ε)|0⟩ + sin(ε)e^{iφ}|1⟩
  Solution:  Discretization by stabilizer measurement. Measuring syndrome
             projects continuous error onto discrete error space (X, Z, Y, I).
             This is why QEC works despite continuous error model.
```

---

## Quantum Error Model

Any single-qubit error can be decomposed in the Pauli basis:

```
PAULI BASIS {I, X, Y, Z}:
  I = identity (no error)
  X = bit flip:    X|0⟩ = |1⟩, X|1⟩ = |0⟩
  Z = phase flip:  Z|0⟩ = |0⟩, Z|1⟩ = −|1⟩
  Y = both:        Y = iXZ  (bit flip + phase flip)

Any single-qubit error ε:
  ε(|ψ⟩⟨ψ|) = Σᵢⱼ Eᵢ|ψ⟩⟨ψ|Eⱼ†  where Eᵢ ∈ {I, X, Y, Z} × complex coeff.

QEC only needs to correct X, Z, Y errors:
  If code corrects these, it corrects any error (by linearity)
  This is the discretization miracle.

Quantum channel models:
  Bit-flip channel:   with prob p: X error, prob (1-p): I
  Phase-flip channel: with prob p: Z error, prob (1-p): I
  Depolarizing:       with prob p: uniform X, Y, or Z error each with p/3
  Amplitude damping:  |1⟩ → |0⟩ energy loss (T₁ process)
```

---

## 3-Qubit Bit-Flip Code

The simplest quantum error correcting code (analogous to classical repetition):

```
ENCODING:   |0_L⟩ = |000⟩    |1_L⟩ = |111⟩
  |ψ⟩ = α|0⟩ + β|1⟩  →  α|000⟩ + β|111⟩

Error occurs (say X on qubit 1): α|100⟩ + β|011⟩

SYNDROME MEASUREMENT (ancilla qubits):
  Measure stabilizers Z₁Z₂ and Z₂Z₃  (parity checks):

  State         Z₁Z₂  Z₂Z₃   Error
  ─────         ─────  ─────   ─────
  α|000⟩+β|111⟩  +1    +1     none (I)
  α|100⟩+β|011⟩  −1    +1     X on qubit 0
  α|010⟩+β|101⟩  −1    −1     X on qubit 1
  α|001⟩+β|110⟩  +1    −1     X on qubit 2

CORRECTION: Apply X to the indicated qubit. State restored.

WHAT IS NOT MEASURED: The logical state (α, β) — only the syndrome
(which physical qubit has an X error).

LIMITATION: Corrects only single X (bit-flip) errors.
            Cannot correct Z (phase-flip) errors.
```

---

## 3-Qubit Phase-Flip Code

Handles phase errors using Hadamard-rotated basis:

```
ENCODING (in |+⟩/|−⟩ basis):
  |0_L⟩ = |+++⟩    |1_L⟩ = |−−−⟩
  where |+⟩ = (|0⟩+|1⟩)/√2, |−⟩ = (|0⟩−|1⟩)/√2

SYNDROME: Measure X₁X₂ and X₂X₃ (analog of Z₁Z₂ in rotated basis)

Z error on qubit j flips phase of that qubit: |+⟩ ↔ |−⟩
Same syndrome table as bit-flip code but with X↔Z.

CORRECTION: Apply Z to indicated qubit.
```

---

## Shor's 9-Qubit Code (1995)

First quantum error correcting code. Combines the two 3-qubit codes:

```
ENCODING (each logical qubit into 9 physical qubits):
  |0_L⟩ = (|000⟩+|111⟩)^⊗3 / 2√2
  |1_L⟩ = (|000⟩−|111⟩)^⊗3 / 2√2

  Three blocks of 3 qubits — each block encodes for bit flips.
  The three blocks together encode for phase flips.
  Outer code: phase-flip code (over 3 blocks)
  Inner code: bit-flip code (within each block)

CORRECTS: Any single-qubit X, Y, or Z error.
SYNDROME: 8 measurements (2 per block for bit-flip + 2 for phase-flip)
OVERHEAD: 9 physical qubits per 1 logical qubit
[[n,k,d]] notation: [[9,1,3]]
  n = 9 physical qubits
  k = 1 logical qubit
  d = 3 (distance — can correct ⌊(d-1)/2⌋ = 1 error)
```

---

## Stabilizer Formalism

The general framework unifying all major QEC codes.

```
PAULI GROUP on n qubits: Pₙ = {±1, ±i} × {I,X,Y,Z}^⊗n
  Elements are n-qubit Pauli operators (e.g., XZYIZ)

STABILIZER GROUP S:
  Abelian subgroup S ⊂ Pₙ with −I ∉ S
  A state |ψ⟩ is stabilized by S if: s|ψ⟩ = |ψ⟩ for all s ∈ S

STABILIZER CODE [[n,k,d]]:
  n physical qubits, k logical qubits, distance d
  |S| = n − k stabilizer generators (s₁, ..., s_{n-k})
  Code space: simultaneous +1 eigenspace of all stabilizers

  Logical operators: X̄, Z̄ commute with all stabilizers
                    but are not themselves stabilizers

  Error detection:
    Error E anticommutes with some stabilizer: sᵢE ≠ Esᵢ
    → syndrome measurement of sᵢ gives −1 instead of +1
    → reveals error without reading logical state
```

**Example — 3-qubit bit-flip code in stabilizer language:**

```
Generators: s₁ = Z₁Z₂, s₂ = Z₂Z₃
Logical operators: X̄ = X₁X₂X₃, Z̄ = Z₁  (or Z₂ or Z₃)
Code space: +1 eigenspace of Z₁Z₂ and Z₂Z₃
           = span{|000⟩, |111⟩}  ✓

X error on qubit 1: X₁ anticommutes with Z₁Z₂ (syndrome s₁ = -1),
                    commutes with Z₂Z₃ (syndrome s₂ = +1)
Syndrome = (−1, +1) → X₁ error → apply X₁ → corrected
```

---

## CSS Codes (Calderbank-Shor-Steane)

Construct quantum codes from two classical codes H_x, H_z:

```
Requirements:
  H_x, H_z are parity-check matrices of classical codes C_x, C_z
  Rows of H_x ⊥ rows of H_z  (CSS construction condition: C_z⊥ ⊆ C_x)

CSS code [[n, k, d]] with k = dim(C_x) + dim(C_z) − n:
  X-type stabilizers from H_x (detect Z errors)
  Z-type stabilizers from H_z (detect X errors)
  Bit-flip and phase-flip correction are independent!

Examples:
  Steane [[7,1,3]] code: from Hamming [7,4,3] code
  Reed-Solomon based: large k/n ratio
  Topological codes (toric, surface): CSS structure on lattice

Transversal gates:
  CSS codes support transversal CNOT
  Steane code supports transversal H, CNOT, P (Clifford group)
  No code supports transversal T gate (Eastin-Knill theorem)
  → T gate requires magic state distillation
```

---

## Surface Code

The current leading candidate for practical fault-tolerant quantum computers.

```
LAYOUT (distance-d surface code, d × d data qubits):

  ● ─── ● ─── ● ─── ●    ● = data qubit (physical)
  │  X  │  Z  │  X  │    X = X-type stabilizer (face/plaquette check)
  ● ─── ● ─── ● ─── ●    Z = Z-type stabilizer (vertex check)
  │  Z  │  X  │  Z  │
  ● ─── ● ─── ● ─── ●
  │  X  │  Z  │  X  │
  ● ─── ● ─── ● ─── ●

  d×d data qubits + (d²-1)/2 X-stabilizers + (d²-1)/2 Z-stabilizers
  Total qubits: ~2d²

  Each stabilizer check: 4 neighboring data qubits (weight-4 Pauli)
  Only nearest-neighbor interactions — hardware friendly!
  1 logical qubit per surface code patch

LOGICAL OPERATORS:
  Z̄ = product of Z along top-bottom path (d qubits)
  X̄ = product of X along left-right path (d qubits)

  Code distance d = min path length crossing the patch
  Corrects up to ⌊(d-1)/2⌋ arbitrary errors

ERROR CORRECTION CYCLE (~1 μs for superconducting):
  1. Measure all stabilizers using ancilla qubits
  2. Compare syndrome to previous round
  3. Run minimum-weight perfect matching (MWPM) decoder
  4. Apply corrections or track in software (correction tracking)

THRESHOLD: With physical error rate p < p* ≈ 0.1–1%:
  Logical error rate: p_L ≈ (p/p*)^⌈d/2⌉  (exponentially suppressed!)

  At p = 0.1%, d = 31:  p_L ≈ 10^{-15}  (target for Shor on RSA-2048)
  Physical qubits needed: ~2 × 31² ≈ 2000 per logical qubit
```

---

## Toric Code (Kitaev, 1997)

The original topological quantum code — surface code ancestor:

```
Same structure as surface code but on a torus (periodic boundary conditions):
  Encodes 2 logical qubits per torus (vs 1 for surface code)
  Logical operators: nontrivial loops around torus

Why it matters conceptually:
  Error correction ↔ topology: error is a chain of flipped stabilizers
  Logical error = chain wrapping around torus
  Correctable errors = chains that don't wrap

  Physical intuition: quantum information is stored in global topological
  properties, immune to local perturbations — Anyonic excitations.

Excitations are anyons:
  X error: creates pair of "e" anyons (Z-stabilizer violations)
  Z error: creates pair of "m" anyons (X-stabilizer violations)
  MWPM decoder pairs them up and annihilates
```

---

## Fault Tolerance Threshold Theorem

The fundamental theoretical guarantee:

```
THEOREM (Aharonov-Ben-Or 1997, Knill-Laflamme-Zurek 1996, ...):
  If each gate has error probability ≤ p < p* (threshold),
  then using quantum error correction with O(log^c(1/ε)) overhead,
  any quantum circuit of depth L can be simulated with error < ε.

  p* depends on:
    Code choice: surface code p* ≈ 1%
    Error model: depolarizing, correlated, ...
    Decoder efficiency: MWPM is efficient and near-optimal

  Overhead:
    Gate overhead: O(poly(log 1/ε)) per logical gate
    Space overhead: 2d² physical per logical (surface code, distance d)

CURRENT STATE (2024):
  Best physical error rates: ~0.1–0.5% 2Q gate error (superconducting)
  Surface code threshold: ~1%
  Status: at/near threshold, not yet well below it

  IBM Heron: 0.2% CX gate error — approaching threshold
  Google Willow: demonstrated logical error suppression below threshold

CONSEQUENCE: below threshold, more physical qubits = better.
             above threshold, more physical qubits = worse (error propagation).
```

---

## Magic State Distillation

Why T gates are expensive in fault-tolerant QC:

```
EASTIN-KNILL THEOREM: No quantum error correcting code supports
a universal transversal gate set. Specifically, CSS codes are
limited to Clifford group gates transversally.

CLIFFORD GROUP gates (transversal → "cheap" in FTQC):
  H, S, CNOT, CZ, SWAP — efficiently simulable classically (Gottesman-Knill)
  Free to implement in logical space via transversal circuits.

T GATE (non-Clifford → "expensive"):
  Required for universality.
  No transversal implementation in any code.

MAGIC STATE DISTILLATION (Bravyi-Kitaev 2005):
  1. Inject noisy "magic states" |T⟩ = T|+⟩ = (|0⟩ + e^{iπ/4}|1⟩)/√2
     Noisy injection: use teleportation with noisy resource state
  2. Purify many noisy |T⟩ states into few high-fidelity ones
     15 noisy → 1 clean (15-to-1 protocol, distance-3 Reed-Muller code)
     Output error: O(ε^3) from input ε (cubic purification per round)
  3. Use clean |T⟩ + gate teleportation → apply T logically

OVERHEAD:
  15-to-1 distillation, round 1: 15 physical T-count per logical T
  For RSA-2048 Shor: ~10^10 T gates needed
  Magic state factories: ~90% of the total physical qubit overhead

  More efficient protocols: Haah et al. 2017: 20-to-4 protocol, better asymptotic
```

---

## Resource Estimation for Shor's Algorithm

Putting it all together:

```
TARGET: Factor 2048-bit RSA modulus

Logical resources:
  Logical qubits: ~4000
  T gates: ~10^10  (using optimized Shor circuit)
  Clifford gates: ~10^12
  Total circuit depth: ~10^9 logical cycles

Physical resources (surface code, p = 10^{-3}):
  Code distance: d ≈ 31  (to reach logical error 10^{-15} per gate)
  Physical qubits per logical: ~2 × 31² ≈ 2000
  Data qubits total: 4000 × 2000 = 8M physical qubits
  Magic state factories: additional ~1M qubits
  Total: ~9–10 million physical qubits

  Clock cycle: 1 μs per error correction round
  Total time: ~10^9 cycles × 1 μs = ~1000 seconds ≈ 17 minutes (in ideal case)
  Realistic: hours due to various overheads

CURRENT STATE (2024):
  IBM Heron: 133 physical qubits
  Google Willow: 105 physical qubits
  Gap to CRQC: ~4–5 orders of magnitude
  Timeline: Most experts say 2035–2040+ minimum
```

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| Why can't we just repeat qubits like classical bits? | No-cloning theorem forbids copying quantum states |
| How does syndrome measurement avoid disturbing state? | Measures parity of multiple qubits — tells error location, not state value |
| What's the surface code threshold? | ~1% physical error rate; leading platforms approaching this |
| Why is T gate expensive? | Eastin-Knill theorem: no transversal non-Clifford gate; needs distillation |
| How many physical qubits per logical qubit? | ~1000–2000 at d≈30 for surface code |
| What decoder does surface code use? | Minimum-weight perfect matching (MWPM) — polynomial time |
| When will CRQC break RSA? | ~9-10M physical qubits needed; current: 100s — most say 2035–2040+ |
| What's the Eastin-Knill theorem? | No universal transversal gate set exists for any QEC code |

---

## Common Confusion Points

**"QEC corrects errors by measuring the qubit"** — wrong. Syndrome
measurements measure *parity operators* (products of Paulis) on ancilla
qubits entangled with the data, revealing error syndromes without
collapsing the logical qubit state.

**"More error correction levels always help"** — only below the threshold.
Above the threshold, concatenation increases the effective error rate.
This is why the threshold theorem is critical.

**"Logical qubits are stable and error-free"** — no. Logical qubits have
logical error rates. The surface code suppresses them exponentially with
distance, but never to zero. Shor's algorithm requires ~10^{-15} logical
error per gate — achievable but demands large d.

**"Magic state distillation is just a detail"** — it's actually the
dominant overhead. For Shor's algorithm, magic state factories account
for ~90% of physical qubit count. Reducing T-count in circuits is
therefore a major quantum compilation research area.

**Toric code vs surface code** — toric code has periodic boundary
conditions (encodes 2 logical qubits, somewhat more efficient);
surface code has open boundaries (easier to implement, 1 logical qubit
per patch). Surface code is preferred for hardware.
