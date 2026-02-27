# Qubits, Quantum Gates & Circuits

## The Landscape

```
┌─────────────────────────────────────────────────────────────────────┐
│             CIRCUIT MODEL — BUILDING BLOCKS                         │
│                                                                     │
│  QUBIT MATH          GATES                MULTI-QUBIT              │
│  ┌────────────┐      ┌──────────────┐     ┌──────────────────┐    │
│  │ ℂ² state   │      │ Single-qubit │     │ Tensor products  │    │
│  │ Bloch sphere│─────►│ X,Y,Z,H,S,T │────►│ Entanglement     │    │
│  │ Born rule   │      │ Rotations    │     │ Bell states      │    │
│  └────────────┘      ├──────────────┤     └────────┬─────────┘    │
│                      │ Two-qubit    │              │               │
│                      │ CNOT,CZ,SWAP │              │               │
│                      ├──────────────┤              │               │
│                      │ Three-qubit  │              │               │
│                      │ Toffoli,     │              ▼               │
│                      │ Fredkin      │     ┌──────────────────┐    │
│                      └──────────────┘     │ CIRCUITS         │    │
│                                           │ Width, depth,    │    │
│  UNIVERSALITY          MEASUREMENT        │ T-count metrics  │    │
│  ┌──────────────┐     ┌──────────────┐    └────────┬─────────┘    │
│  │ {H,T,CNOT}   │     │ Projective   │             │               │
│  │ Solovay-      │     │ Born rule    │             ▼               │
│  │ Kitaev       │     │ Syndrome     │    ┌──────────────────┐    │
│  │              │     │ (for QEC)    │    │ DENSITY MATRICES │    │
│  │ Clifford+T   │     └──────────────┘    │ Mixed states     │    │
│  │ Gottesman-   │                         │ Lindblad eqn     │    │
│  │ Knill thm    │     NO-CLONING          │ Decoherence      │    │
│  └──────────────┘     ┌──────────────┐    └──────────────────┘    │
│                       │ Can't copy   │                             │
│  PAULI/CLIFFORD       │ unknown |ψ⟩  │                             │
│  ┌──────────────┐     │ → QEC must   │                             │
│  │ Pauli group  │     │   spread info│                             │
│  │ Clifford grp │     │ → QKD secure │                             │
│  │ Normalizer   │     └──────────────┘                             │
│  └──────────────┘                                                   │
└─────────────────────────────────────────────────────────────────────┘
```

---

## The Qubit — Mathematical Foundation

A qubit is a unit vector in ℂ²:

```
|ψ⟩ = α|0⟩ + β|1⟩,   α,β ∈ ℂ,   |α|² + |β|² = 1

Computational basis:
  |0⟩ = [1, 0]ᵀ   (ground state)
  |1⟩ = [0, 1]ᵀ   (excited state)

Bra-ket (Dirac) notation:
  |ψ⟩ = ket (column vector in ℂ²)
  ⟨ψ| = bra (conjugate-transpose row vector)
  ⟨φ|ψ⟩ = inner product (overlap / probability amplitude)
  |ψ⟩⟨φ| = outer product (operator / matrix)
```

### Bloch Sphere

Every single-qubit pure state maps to a point on the unit sphere in ℝ³:

```
          |0⟩ (north pole, z=+1)
            ↑
            |  ← |ψ⟩ at (θ, φ)
          ──┼──
           /|
          / |   θ ∈ [0,π]   polar (colatitude)
         /  |   φ ∈ [0,2π)  azimuthal
|−⟩←────   ↑   ────→|+⟩
        \   |
         \  |   |ψ⟩ = cos(θ/2)|0⟩ + e^(iφ)sin(θ/2)|1⟩
          \ |
            ↓
          |1⟩ (south pole, z=−1)

Key points:
  |0⟩:  z=+1  (north)
  |1⟩:  z=−1  (south)
  |+⟩ = (|0⟩+|1⟩)/√2:  +x axis (θ=π/2, φ=0)
  |−⟩ = (|0⟩−|1⟩)/√2:  −x axis (θ=π/2, φ=π)
  |i⟩ = (|0⟩+i|1⟩)/√2: +y axis (θ=π/2, φ=π/2)
```

Measurement collapses |ψ⟩ to |0⟩ with probability |α|² or |1⟩ with probability |β|².
After measurement the state is destroyed — quantum parallelism is not free parallel
computation.

---

## Multi-Qubit States

n qubits = unit vector in ℂ^(2^n) via tensor product:

```
2 qubits: |ψ⟩ = α₀₀|00⟩ + α₀₁|01⟩ + α₁₀|10⟩ + α₁₁|11⟩,  Σ|αᵢⱼ|² = 1
3 qubits: 8 complex amplitudes
n qubits: 2^n complex amplitudes — exponential classical description

PRODUCT STATE (separable):
  |ψ_A⟩ ⊗ |ψ_B⟩ = (α|0⟩+β|1⟩) ⊗ (γ|0⟩+δ|1⟩)
                 = αγ|00⟩ + αδ|01⟩ + βγ|10⟩ + βδ|11⟩

ENTANGLED STATE (not factorable as product):
  Bell states (maximally entangled):
    |Φ⁺⟩ = (|00⟩+|11⟩)/√2   ← same outcomes (correlated)
    |Φ⁻⟩ = (|00⟩−|11⟩)/√2
    |Ψ⁺⟩ = (|01⟩+|10⟩)/√2   ← opposite outcomes (anti-correlated)
    |Ψ⁻⟩ = (|01⟩−|10⟩)/√2   ← singlet
  Cannot be written as |ψ_A⟩⊗|ψ_B⟩ for any single-qubit states.
```

---

## Single-Qubit Gates

Quantum gates are **unitary matrices** (U†U = I, probability-preserving, reversible):

```
GATE   MATRIX                   BLOCH SPHERE         ACTION
─────  ───────────────────────  ───────────────────  ──────────────────────────
X      [0 1]                    π rotation around X  Bit flip: |0⟩↔|1⟩ (NOT)
       [1 0]

Y      [ 0 -i]                  π rotation around Y  Bit + phase flip
       [ i  0]

Z      [1  0]                   π rotation around Z  Phase flip: |1⟩→−|1⟩
       [0 -1]

H      [1  1]/√2                π/2 Y then π X       |0⟩→|+⟩, |1⟩→|−⟩
       [1 -1]                                        Creates superposition

S      [1 0]                    π/2 rotation Z       Phase gate: |1⟩→i|1⟩
       [0 i]

T      [1      0    ]           π/4 rotation Z       Non-Clifford; expensive
       [0  e^(iπ/4) ]                                in fault-tolerant QC

Rz(φ)  [e^(-iφ/2)  0  ]        Rotation Z by φ      General phase
       [0   e^(iφ/2)   ]
```

Key identities:
- H² = I  (Hadamard is self-inverse)
- X² = Y² = Z² = I  (Paulis are self-inverse)
- S² = Z, T² = S, T⁸ = I
- HXH = Z, HZH = X  (Hadamard conjugates X and Z)
- XY = iZ, YZ = iX, ZX = iY  (cyclic; Paulis anti-commute pairwise)

---

## Two-Qubit Gates

```
GATE          OPERATION                                CIRCUIT SYMBOL
────────────  ───────────────────────────────────────  ──────────────
CNOT (CX)     If control=|1⟩, flip target             q₀:─●─
              |00⟩→|00⟩, |01⟩→|01⟩                  q₁:─⊕─
              |10⟩→|11⟩, |11⟩→|10⟩

CZ            If control=|1⟩, phase-flip target        q₀:─●─
              |11⟩→−|11⟩                               q₁:─Z─
              Symmetric: either qubit can be control

SWAP          Exchange qubit states                    q₀:─╳─
              |01⟩→|10⟩, |10⟩→|01⟩                  q₁:─╳─
              = 3 CNOTs

iSWAP         SWAP + phase i on swapped component      Native in superconducting
              Common on superconducting processors

CPhase(θ)     Phase-kick target by e^(iθ) if ctrl=|1⟩ Used in QFT
```

**Creating a Bell state** (H + CNOT):
```
q₀: |0⟩ ─H─●─  →  (|0⟩+|1⟩)/√2 acts as control
q₁: |0⟩ ───⊕─  →  (|00⟩+|11⟩)/√2 = |Φ⁺⟩  ← entangled!

Why: H creates |+⟩ = (|0⟩+|1⟩)/√2 on q₀.
     CNOT conditional on q₀ maps |0⟩→|00⟩ and |1⟩→|11⟩ by linearity.
```

---

## Three-Qubit Gates

```
GATE         OPERATION                                   USE
──────────── ────────────────────────────────────────    ────────────────────────
Toffoli (CCX) Doubly controlled NOT: flip target iff     Classical reversible AND
              both controls are |1⟩                      Error correction primitives
              Universal for classical reversible logic

Fredkin (CSWAP) Controlled SWAP: if control=|1⟩, swap   Classical reversible SWAP
                the two target qubits
```

---

## Universality

```
UNIVERSAL GATE SETS (approximate any unitary to ε precision):
  {H, T, CNOT}      ← standard; Solovay-Kitaev gives O(log^c(1/ε)) gates
  {Rx(θ), Rz(φ), CNOT} for irrational θ/π  ← also universal

CLIFFORD GATES = {H, S, CNOT, X, Y, Z}:
  ─ Map Pauli operators to Pauli operators under conjugation
  ─ Efficiently classically simulable (Gottesman-Knill theorem, O(n²) time)
  ─ NOT universal alone

T GATE BREAKS CLASSICAL SIMULABILITY:
  T ∉ Clifford group → adding T to Clifford makes set universal
  Cost in fault-tolerant QC: each logical T gate requires ~100–1000 physical
  T gates via magic state distillation (see 03-ERROR-CORRECTION.md)
  T-count and T-depth are the primary resource metrics for FTQC algorithms
```

---

## Quantum Circuits

```
NOTATION:
  ─────── = qubit wire (time flows left to right)
  [gate]  = gate applied to qubit
    ●     = control (filled dot)
    ⊕     = CNOT target
    M     = measurement (→ classical bit output)

Example: Quantum teleportation (three qubit lines)
  (Alice has q₀=|ψ⟩ and q₁; Bob has q₂)

  q₀(|ψ⟩): ────────●──H──M─────────────── (→ classical bit b₀)
  q₁(|0⟩): ──H──●──⊕──────M──────────────  (→ classical bit b₁)
  q₂(|0⟩): ──────⊕─────────────X^b₁──Z^b₀─→ |ψ⟩ at Bob's end

  Step by step:
  1. Bell pair preparation: H on q₁, CNOT (q₁,q₂) → |Φ⁺⟩₁₂
  2. Alice's Bell measurement: CNOT (q₀,q₁), H on q₀, measure both
  3. Classical communication: Alice sends (b₀,b₁) to Bob
  4. Bob's correction: X^b₁ then Z^b₀ on q₂
  Result: q₂ in state |ψ⟩ — state teleported without physical qubit moving
```

### Circuit Complexity Metrics

```
WIDTH   = number of qubits                          (space resource)
DEPTH   = longest path through circuit gates         (time; bounded by T2)
T-COUNT = number of T gates                          (FTQC cost)
T-DEPTH = longest T-gate path (some T's parallelizable)
CNOT-COUNT = two-qubit gate count                   (fidelity cost on NISQ)
```

---

## Measurement and Born Rule

```
PROJECTIVE MEASUREMENT in {|0⟩, |1⟩}:
  P(outcome 0) = |α|² = ⟨ψ|P₀|ψ⟩    P₀ = |0⟩⟨0| (projector)
  P(outcome 1) = |β|² = ⟨ψ|P₁|ψ⟩    P₁ = |1⟩⟨1|
  Post-measurement state collapses to |0⟩ or |1⟩

MEASURING IN X BASIS (Hadamard basis):
  Apply H, then measure in Z basis
  P(+) = |⟨+|ψ⟩|² = |(α+β)/√2|²

GENERAL OBSERVABLE A (Hermitian):
  ⟨A⟩ = ⟨ψ|A|ψ⟩  (expectation value)
  Outcomes = eigenvalues of A; collapse to corresponding eigenstate

SYNDROME MEASUREMENT (for error correction):
  Measure Pauli operators on ancilla qubits, not data qubits
  → extracts error information without disturbing logical qubit
  (uses POVM / indirect measurement)
```

---

## Density Matrices (Mixed States)

The Lindblad master equation below is the quantum analog of a classical Markov master equation (dP/dt = WP, where W is the transition rate matrix). The unitary term -i[H,ρ] is deterministic evolution (no classical analog in a Markov chain), while the jump operators Lⱼ correspond directly to classical transition rates — each Lⱼ represents one way the system can stochastically jump between states (bit-flip, phase-flip, amplitude damping). If you zero out the Hamiltonian, Lindblad reduces to a classical master equation on the diagonal of ρ.

When the qubit is in a probabilistic mixture or entangled with an environment:

```
PURE STATE ρ = |ψ⟩⟨ψ|:
  ρ² = ρ, Tr(ρ) = 1, Tr(ρ²) = 1, rank 1

MIXED STATE ρ = Σᵢ pᵢ|ψᵢ⟩⟨ψᵢ|:
  Tr(ρ) = 1, Tr(ρ²) < 1

MAXIMALLY MIXED ρ = I/2:
  No information about qubit state
  Bloch vector = origin
  Result of tracing over entangled partner or fully decohered qubit

PARTIAL TRACE (tracing out subsystem B):
  ρ_A = Tr_B(ρ_AB)
  Bell state |Φ⁺⟩⟨Φ⁺|: ρ_A = I/2 (maximally mixed)

TIME EVOLUTION:
  Unitary: ρ(t) = U(t)ρ(0)U†(t)
  With decoherence: Lindblad master equation
    dρ/dt = -i[H,ρ] + Σⱼ Lⱼ ρ Lⱼ† - ½(Lⱼ†Lⱼ ρ + ρ Lⱼ†Lⱼ)
    Lⱼ = jump operators (bit-flip, phase-flip, amplitude damping...)
```

---

## No-Cloning and No-Deletion

### No-Cloning Theorem

**You cannot copy an unknown quantum state.** Proof by contradiction:

```
Assume ∃ unitary U: U|ψ⟩|0⟩ = |ψ⟩|ψ⟩  for all |ψ⟩.

Apply to |0⟩: U|00⟩ = |00⟩
Apply to |1⟩: U|10⟩ = |11⟩
Apply to |+⟩ = (|0⟩+|1⟩)/√2:
  By linearity: U|+⟩|0⟩ = (U|00⟩ + U|10⟩)/√2 = (|00⟩+|11⟩)/√2

But desired clone output = |+⟩|+⟩ = (|00⟩+|01⟩+|10⟩+|11⟩)/2

(|00⟩+|11⟩)/√2 ≠ (|00⟩+|01⟩+|10⟩+|11⟩)/2   ✗ Contradiction.
```

**Consequences:**
- Cannot amplify/fanout quantum signals (as you would a classical bit)
- Error correction must spread info without cloning (stabilizer approach)
- Quantum cryptography security (BB84, E91) relies on no-cloning
- Quantum teleportation consumes the original (no duplication)

### No-Deletion Theorem (time-reversal of no-cloning)

You cannot delete a copy of unknown |ψ⟩: no U such that U|ψ⟩|ψ⟩ = |ψ⟩|0⟩ for all |ψ⟩.

---

## Pauli and Clifford Groups

Critical for quantum error correction:

```
PAULI GROUP P₁ = {±I, ±iI, ±X, ±iX, ±Y, ±iY, ±Z, ±iZ}  (16 elements)

Commutation relations:
  XY = iZ = −YX   (anti-commute)
  YZ = iX = −ZY   (anti-commute)
  ZX = iY = −XZ   (anti-commute)
  Each Pauli anti-commutes with the other two

n-qubit Pauli Pₙ: tensor products like X⊗Z⊗I, with phases ±1, ±i

CLIFFORD GROUP Cₙ: N(Pₙ)/U(1)  (normalizer of Pauli group)
  Generated by {H, S, CNOT}
  Key property: CPC† ∈ Pₙ for all C ∈ Cₙ, P ∈ Pₙ
  Example: HXH† = Z, HZH† = X  (H conjugates X↔Z)
           CNOT (X⊗I) CNOT† = X⊗X   (CNOT maps X on control to X⊗X)
           CNOT (Z⊗I) CNOT† = Z⊗I
           CNOT (I⊗Z) CNOT† = Z⊗Z

GOTTESMAN-KNILL THEOREM:
  Any circuit consisting of {H, S, CNOT, X, Y, Z, measurements in Z basis,
  Pauli preparations and postselection} can be simulated in O(n²) classical time.
  Implication: Clifford-only circuits provide no quantum speedup.
```

---

## Decision Cheat Sheet

| Task | Tool |
|------|------|
| Create superposition from |0⟩ | Hadamard H gate |
| Entangle two qubits | H on qubit 0, then CNOT(0→1) |
| Bit flip | X gate |
| Phase flip (relative sign) | Z gate |
| Phase +90° | S gate |
| Phase +45° | T gate (expensive in FTQC) |
| Arbitrary rotation around Z | Rz(φ) gate |
| Rotate around X axis | Rx(θ) = e^{-iθX/2} |
| Measure qubit in Z basis | Born rule → collapses to |0⟩/|1⟩ |
| Measure qubit in X basis | Apply H, then Z-measure |
| Show a gate set is universal | Must include non-Clifford gate (T or Toffoli) |
| Simulate on classical computer efficiently | Use Clifford gates only |
| Describe decoherence / noise | Density matrix ρ + Lindblad equation |
| Teleport unknown state | Bell pair + Bell measurement + 2 classical bits |

## Common Confusion Points

**Global phase is unobservable; relative phase is critical.** e^(iφ)|ψ⟩ ≡ |ψ⟩ physically.
But Z flips the *relative* phase between α|0⟩ and β|1⟩ components — observable via
interference. Hadamard turns relative phases into amplitude differences.

**Quantum gates are unitary, NOT just linear.** Unitarity ensures ||U|ψ⟩|| = ||ψ⟩||.
Non-unitary quantum operations (measurement, decoherence) require ancillas or
environment in the mathematical description (Kraus operators, Lindblad).

**CNOT does not always create entanglement.** CNOT on |1⟩|0⟩ gives |1⟩|1⟩ (product).
CNOT on |+⟩|0⟩ gives (|00⟩+|11⟩)/√2 (Bell state). The input matters.

**T-count is the FTQC bottleneck, not qubit count.** Each logical T gate requires
preparing a "magic state" |T⟩ = T|+⟩ via magic state distillation — expensive.
Circuit optimization focuses heavily on reducing T-count.

**The Bloch sphere is only for single qubits.** Two-qubit states live in ℂ⁴; you cannot
draw them on a Bloch sphere. Mixed two-qubit states require density matrices.
