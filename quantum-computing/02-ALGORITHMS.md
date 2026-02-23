# Quantum Algorithms — From Deutsch to Shor to QAOA

## The Big Picture

```
+------------------------------------------------------------------+
|                   QUANTUM ALGORITHM LANDSCAPE                     |
+------------------------------------------------------------------+
|                                                                    |
|  PROVEN SPEEDUP                    VARIATIONAL (NISQ-era)         |
|  ─────────────────────────         ─────────────────────────      |
|  Shor: factoring ──► exponential   VQE: quantum chemistry         |
|  Grover: search ──► quadratic      QAOA: combinatorial opt        |
|  QFT: Fourier ──► exponential      QSVM: kernel methods           |
|  HHL: linear sys ──► conditional   Quantum ML: embeddings         |
|  QPE: phase est. ──► exponential   (advantages unproven)          |
|  Hamiltonian sim ──► exponential                                   |
|                                                                    |
|  PARADIGMS                                                         |
|  ────────────────────────────────────────────────────────────     |
|  Query complexity → oracle model, count queries                    |
|  Phase estimation → QFT + eigenvalue extraction                   |
|  Amplitude amplification → Grover iterate                         |
|  Hidden subgroup problem (HSP) → unifies Shor, Simon              |
|  Variational → hybrid classical-quantum optimization              |
+------------------------------------------------------------------+
```

---

## Speedup Taxonomy

Before any algorithm, understand what kind of speedup is claimed:

```
TYPE              EXAMPLE              CONDITION
──────────────    ─────────────────    ──────────────────────────────
Exponential       Shor's algorithm     Problem has exploitable structure
  (2^n → poly)   Quantum simulation   (periodicity, group structure)

Quadratic         Grover's search      Unstructured; provably optimal
  (N → √N)       Amplitude estim.     for black-box models

Polynomial        HHL linear systems   Conditional on quantum RAM,
  (conditional)  (potentially exp.)   state prep, readout caveats

No speedup        Most ML, databases   Classical structure already
  (none)         Graph coloring(most) polynomial; no structure to exploit
```

---

## Oracle / Query Model

Many quantum algorithms are analyzed in the **black-box query model**:

```
Algorithm has access to a function f via an oracle O_f:
  O_f |x⟩|y⟩ = |x⟩|y ⊕ f(x)⟩    (y = ancilla bit, ⊕ = XOR)

Phase oracle (equivalent, often more useful):
  O_f^phase |x⟩ = (-1)^f(x) |x⟩  (mark x if f(x)=1 via phase kickback)

Query complexity counts how many times we call O_f.
Quantum queries use superposition: one call evaluates f on all inputs
simultaneously, but output is still probabilistic measurement.
```

---

## Deutsch-Jozsa (1992)

The toy problem that first showed quantum advantage in the query model.

```
Problem: f: {0,1}^n → {0,1} is promised to be either:
  - Constant: f(x) = 0 for all x, OR f(x) = 1 for all x
  - Balanced: f(x) = 0 for exactly half the inputs

Classical: requires 2^(n-1)+1 queries worst case.
Quantum:   requires 1 query.

Circuit:
  |0⟩^⊗n ─ H^⊗n ─ O_f ─ H^⊗n ─ M ─ (all zeros iff constant)
  |1⟩     ─ H    ─

After H^⊗n on |0⟩^⊗n: uniform superposition (1/√2^n)Σ|x⟩
Oracle query: (1/√2^n)Σ(-1)^f(x)|x⟩  (phase kickback)
Second H^⊗n: interference — if f constant, amplitude all in |0⟩^⊗n
                           if f balanced, amplitude 0 in |0⟩^⊗n

Practical value: zero. Exponential query advantage on artificial problem.
Conceptual value: first proof that quantum can do things classically impossible.
```

---

## Simon's Algorithm (1994)

Set the stage for Shor by solving a structured period problem.

```
Problem: f: {0,1}^n → {0,1}^n, promised ∃ nonzero s such that
  f(x) = f(y) iff y = x or y = x ⊕ s
  (f is 2-to-1 with period s under XOR)

Classical: O(2^n/2) queries (birthday paradox)
Quantum:   O(n) queries

Key step: QFT over ℤ₂ⁿ gives uniform superposition over {y : y·s = 0 mod 2}
Repeat n times, solve system of linear equations over ℤ₂ → recover s.

Significance: First exponential speedup over randomized classical algorithms.
Inspired Shor to find the same structure (period finding) over ℤₙ.
```

---

## Quantum Fourier Transform (QFT)

The core building block of most exponential-speedup algorithms.

```
Classical DFT of vector x ∈ ℂ^N:
  X_k = (1/√N) Σⱼ xⱼ e^(2πijk/N)   O(N log N) via FFT

QFT maps computational basis:
  |j⟩  ─QFT─►  (1/√N) Σₖ e^(2πijk/N) |k⟩

On n qubits (N = 2^n):
  QFT|j⟩ = (1/√2^n) Σₖ e^(2πijk/2^n) |k⟩

Circuit: uses n Hadamards + n(n-1)/2 controlled-phase gates
  O(n²) gates vs O(n 2^n) for classical FFT on 2^n elements

BUT: you can't read out all 2^n transformed coefficients — measurement
gives one. QFT is useful only when the transformed state encodes
something extractable, like a period.
```

The QFT circuit for 3 qubits:
```
q₀: ─ H ─ R₂ ─ R₃ ─────── SWAP ─
          │     │               │
q₁: ─────●─── H ─ R₂ ─ SWAP ──│─
               │         │     │
q₂: ───────── ●───────── ────── ─

where R_k = diag(1, e^{2πi/2^k})  (controlled phase gate)
```

---

## Phase Estimation (QPE)

Extract the eigenvalue of a unitary — the workhorse for Shor and HHL.

```
Given: Unitary U and eigenstate |u⟩ with U|u⟩ = e^(2πiφ)|u⟩
Find: φ ∈ [0,1) to t bits of precision

Circuit:
  |0⟩^⊗t ─ H^⊗t ─┐                  ┌─ QFT† ─ M
                   │ controlled-U^j   │
  |u⟩     ─────────┴──────────────────┘ (eigenstate unchanged)

After QFT†: |φ̃⟩ ≈ |⌊2^t φ⌉⟩   (closest t-bit approximation to φ)

Precision: t bits, probability > 1 - ε with t = n + ⌈log(2 + 1/2ε)⌉ qubits
Gate count: O(t²) + cost of implementing controlled-U^(2^j)

Used in:
  Shor: φ is r/N (period/modulus) — extract r
  HHL: φ encodes eigenvalue of matrix A
  Quantum chemistry: φ encodes molecular ground state energy
```

---

## Shor's Algorithm (1994)

Factors N in O((log N)³) quantum gates. Largest cryptographic threat from QC.

```
REDUCTION: Factoring → Period Finding (classical number theory)
────────────────────────────────────────────────────────────────

Step 1 (classical): Choose random a, compute gcd(a, N)
  If gcd(a,N) > 1: found factor, done.

Step 2 (quantum): Find period r of f(x) = aˣ mod N
  r is smallest positive integer such that aʳ ≡ 1 (mod N)

Step 3 (classical): With high probability:
  - r is even (restart if not)
  - a^(r/2) ≢ -1 (mod N) (restart if not)
  - gcd(a^(r/2) ± 1, N) gives nontrivial factor

WHY r IS THE KEY: aʳ ≡ 1 (mod N) means:
  (a^(r/2) − 1)(a^(r/2) + 1) = aʳ − 1 ≡ 0 (mod N)
  But neither factor is divisible by N → they share factors with N.

QUANTUM PERIOD FINDING:
  1. Create superposition |ψ⟩ = (1/√M)Σₓ|x⟩|aˣ mod N⟩
  2. Measure second register: collapses to uniform superposition
     over {x : aˣ mod N = c} for some c
  3. QFT on first register: peaks at multiples of M/r
  4. Measure → get M/r approximately → recover r by continued fractions

COMPLEXITY:
  Circuit depth: O((log N)²) with fast multiplication
  Total gates: O((log N)³)
  Qubits: ~2n + O(1) where N < 2^n

  For RSA-2048: need ~4000 logical qubits → ~8M physical at current error rates
```

---

## Grover's Search (1996)

Quadratic speedup for unstructured search — provably optimal.

```
Problem: Find x* such that f(x*) = 1, where f: {0,1}^n → {0,1}
  N = 2^n items, 1 marked item.

Classical: O(N) queries expected (linear search).
Quantum:   O(√N) queries.

GROVER ITERATION (amplitude amplification):
  1. Initialize: |s⟩ = H^⊗n|0⟩^⊗n = (1/√N)Σ|x⟩  (uniform superposition)

  2. Oracle Uf: phase-flip the marked item:
     |x⟩ → (-1)^f(x)|x⟩
     Geometrically: reflect around subspace perpendicular to |x*⟩

  3. Diffusion (inversion about mean):
     D = 2|s⟩⟨s| − I
     Geometrically: reflect around |s⟩

  Composed: Grover iterate G = D · Uf

  Amplitude of |x*⟩ after k iterations: sin²((2k+1)θ)
  where sin(θ) = 1/√N

  Optimal k ≈ (π/4)√N → amplitude ≈ 1

GEOMETRIC PICTURE:
  State lives in 2D subspace spanned by |x*⟩ and |s⟩.
  Each iteration rotates by 2θ toward |x*⟩.
  After ~π/(4θ) ≈ π√N/4 steps, state ≈ |x*⟩.

MULTIPLE SOLUTIONS (M marked items):
  Optimal: O(√(N/M)) iterations

LOWER BOUND: Bennett-Bernstein-Brassard-Vazirani (BBBV 1996)
  Any quantum search algorithm requires Ω(√N) queries.
  Grover is optimal for unstructured search.

APPLICATIONS:
  Exhaustive key search: AES-128 → 2^64 queries (was 2^128)
  → NIST response: double key lengths (AES-256 stays secure)
  Collision finding: O(N^(1/3)) with Grover + BHT
  Preimage attacks: O(2^(n/2)) instead of O(2^n)
```

---

## HHL Algorithm (Harrow-Hassidim-Lloyd, 2009)

Solve Ax = b exponentially faster — with massive fine print.

```
Problem: Given sparse N×N matrix A and vector b, find x = A⁻¹b.
Classical: O(N^3) (direct) or O(N·κ·poly(log 1/ε)) iterative
Quantum: O(log(N) · κ² · poly(log 1/ε)) with caveats

Circuit:
  1. Prepare quantum state |b⟩ (input state prep — big caveat)
  2. QPE on e^(iAt): extract eigenvalues λⱼ of A
  3. Ancilla rotation: |λⱼ⟩ → (C/λⱼ)|0⟩ + √(1-C²/λⱼ²)|1⟩
  4. Uncompute QPE
  5. Post-select on ancilla = |1⟩ → amplitude encodes 1/λⱼ
  6. Output: |x⟩ = A⁻¹|b⟩/‖A⁻¹b‖

CAVEATS (each can kill the speedup):
  State prep: Preparing |b⟩ from classical b takes O(N) — wipes out speedup
  Readout: Reading out x takes O(N) measurements — wipes out speedup
  Quantum RAM: Requires QRAM for efficient state prep (massive hardware assumption)
  Condition number κ: Algorithm is O(κ²); classical iterative is O(κ) or O(κ√N)
  Sparse access: A must be sparse AND efficiently oracle-accessible

  Practical advantage only when: reading a scalar property of x (not full x),
  input already quantum, A sparse with efficient oracle, κ manageable.
```

---

## Variational Quantum Algorithms (NISQ Era)

Hybrid classical-quantum loop — designed for noisy hardware today.

### VQE (Variational Quantum Eigensolver)

```
Goal: Find ground state energy E₀ = min_ψ ⟨ψ|H|ψ⟩

Algorithm:
  1. Choose parametrized circuit U(θ): |ψ(θ)⟩ = U(θ)|0⟩
  2. Measure ⟨ψ(θ)|H|ψ(θ)⟩ on quantum hardware
     (decompose H into Pauli strings, measure each)
  3. Classical optimizer updates θ (COBYLA, SPSA, gradient descent)
  4. Repeat until convergence

Used for: molecular ground state energies (quantum chemistry)
Hardware: 10–100 qubits, shallow depth (NISQ-friendly)
Status: Demonstrated for small molecules (H₂, LiH, BeH₂)
        Classical methods (CCSD(T)) still win for current qubit counts
```

### QAOA (Quantum Approximate Optimization Algorithm)

```
Goal: Approximate solution to combinatorial optimization (MaxCut, 3SAT)

Problem Hamiltonian H_P: encodes cost function (diagonal in Z basis)
Mixer Hamiltonian H_M: = Σⱼ Xⱼ (drives exploration)

Circuit (depth p):
  |s⟩ = H^⊗n|0⟩  (uniform superposition)
  Apply: [e^{-iγ₁H_P} e^{-iβ₁H_M}] ... [e^{-iγₚH_P} e^{-iβₚH_M}]

  (p layers of alternating problem + mixer unitaries)

  Optimize γ, β to maximize ⟨H_P⟩.

Guarantees: At p→∞ approaches exact solution (adiabatic limit)
            At p=1 gives 0.6924 approximation for MaxCut (Farhi 2014)
Classical best: 0.878 (Goemans-Williamson SDP, 1995)
Status: No proven quantum advantage over classical at any p.
        For small p, classical simulation is easy.
```

---

## Quantum Simulation

The original motivation for quantum computing (Feynman 1982):

```
"Nature isn't classical... and if you want to make a simulation
of nature, you'd better make it quantum mechanical."
            — Richard Feynman

Quantum simulation:
  Simulate quantum system H on quantum hardware
  Trotter decomposition: e^{-iHt} ≈ (e^{-iH₁t/n}e^{-iH₂t/n}...e^{-iHₖt/n})^n

  Applications:
    Quantum chemistry: molecular energies, reaction pathways
    Drug discovery: protein folding, binding affinity
    Materials: high-Tc superconductors, topological phases
    Nuclear physics: QCD on a lattice

  Why exponential speedup is real here:
    Hilbert space of n-body quantum system: 2^n (exponential)
    Classical simulation requires tracking 2^n amplitudes
    QC with n qubits IS the 2^n Hilbert space — exact simulation

  Where speedup is confirmed: simulating quantum systems.
  This is the most likely near-term practical quantum advantage.
```

---

## Algorithm Reference Table

| Algorithm | Problem | Speedup | Key resource | Status |
|-----------|---------|---------|-------------|--------|
| Deutsch-Jozsa | Constant vs balanced | Exp (query) | 1 query | Toy example |
| Simon's | Period mod XOR | Exp | n queries | Historical; led to Shor |
| Grover | Unstructured search | Quadratic (√N) | O(√N) oracle calls | Proven optimal |
| Shor (factoring) | Integer factoring | Exponential | O((log N)³) gates | FTQC required |
| Shor (DLog) | Discrete logarithm | Exponential | Same | FTQC required |
| QFT | Fourier transform | Exponential | O(n²) gates | Subroutine |
| QPE | Eigenvalue estimation | Exponential | O(n²) + controlled-U | Subroutine |
| HHL | Linear systems | Conditional exp | QRAM, sparse access | Fine print kills it |
| Ham. sim. | Simulate quantum H | Exponential | Trotter depth | Best near-term advantage |
| VQE | Chemistry ground state | Unknown | Shallow parametric circuit | NISQ; beats classical? unclear |
| QAOA | Combinatorial opt | Unknown | p-depth circuit | No proven advantage yet |
| Quantum walk | Graph problems | Quadratic (some) | Coherent walk | Specific applications |

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| What problem should I use Grover for? | Unstructured search in a database, key exhaustion |
| Will Grover break AES-128? | Reduces to 2^64 queries — NIST says AES-256 for post-quantum |
| Why does Shor break RSA but not AES? | RSA relies on factoring hardness; AES is symmetric (Grover only) |
| Can QC solve NP-complete problems? | Not known; Grover gives √N — not polynomial for NP-complete |
| What's the most realistic near-term QC advantage? | Quantum chemistry simulation (VQE for small molecules) |
| Is HHL useful? | Only with QRAM, sparse A, logarithmic readout — rarely holds |
| What are variational algorithms good for? | Heuristic approximations; no proven advantage established |

---

## Common Confusion Points

**"Grover solves NP-complete in √N"** — N is the search space size, not
the input length. For 3-SAT with n variables, N = 2^n, and √N = 2^(n/2).
Still exponential in n. Grover reduces exponent by 2, not to polynomial.

**"QFT is the same as FFT and gives exponential speedup"** — QFT runs in
O(n²) gates vs O(n·2^n) gates for FFT on 2^n inputs. But you can't read
out all outputs. The speedup only helps when the QFT's output encodes
something extractable via interference — like Shor's period.

**"Shor requires only 4000 qubits"** — 4000 *logical* qubits. With current
surface code overhead (~1000–2000 physical per logical), that's 4–8 million
physical qubits. Current hardware: ~100–1000 physical, no error correction.

**"VQE has proven quantum advantage"** — no. All published VQE results can
be classically simulated. For useful molecular sizes, classical methods
(CCSD(T)) still win. Advantage may emerge for larger molecules with
fault-tolerant hardware.
