# Quantum Information Theory

```
QUANTUM VS CLASSICAL INFORMATION

Classical bit:       0 or 1  (definite state)
Qubit:               α|0⟩ + β|1⟩,  |α|² + |β|² = 1  (superposition)

Classical channel:   p(y|x) — probability of output given input
Quantum channel:     ε(ρ) — completely positive trace-preserving (CPTP) map on density matrix

Classical entropy:   H(X) = -Σ p(x) log p(x)
Von Neumann entropy: S(ρ) = -Tr(ρ log ρ)

┌─────────────────────────────────────────────────────────────────────┐
│  Density matrix ρ:                                                  │
│    Pure state:  ρ = |ψ⟩⟨ψ|,   ρ² = ρ,   Tr(ρ²) = 1               │
│    Mixed state: ρ = Σᵢ pᵢ|ψᵢ⟩⟨ψᵢ|,  ρ² ≠ ρ,  Tr(ρ²) < 1          │
│    Maximally mixed: ρ = I/d  (S = log d,  maximum entropy)         │
│                                                                     │
│  Eigendecomposition: ρ = Σᵢ λᵢ|eᵢ⟩⟨eᵢ|,  λᵢ ≥ 0,  Σ λᵢ = 1      │
│  Von Neumann entropy: S(ρ) = -Σᵢ λᵢ log λᵢ   [0 ≤ S ≤ log d]     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 1. Von Neumann Entropy

```
S(ρ) = -Tr(ρ log ρ) = H({λᵢ})   [Shannon entropy of eigenvalues]

Key values:
  Pure state  |ψ⟩⟨ψ|:    eigenvalues {1,0,...,0} → S = 0
  Qubit ρ = I/2:          eigenvalues {½,½}      → S = 1
  d-dimensional I/d:      eigenvalues {1/d,...}  → S = log d
```

**Why S = 0 for pure states**: A pure state has no classical uncertainty — it's a definite
quantum state even if we don't know the measurement outcome in advance. Entropy measures
our ignorance about the state preparation, not the measurement outcome.

**Additivity**: S(ρ_A ⊗ ρ_B) = S(ρ_A) + S(ρ_B) for product states. For entangled states,
S(ρ_AB) < S(ρ_A) + S(ρ_B) in general.

**Quantum relative entropy**: D(ρ‖σ) = Tr(ρ(log ρ - log σ)) ≥ 0, with equality iff ρ = σ.
This is the quantum analog of KL divergence. Klein's inequality provides the proof.

---

## 2. Quantum Mutual Information and Strong Subadditivity

For a tripartite system ABC with density matrix ρ_ABC:

```
Quantum mutual information:
  I(A:B)_ρ = S(ρ_A) + S(ρ_B) - S(ρ_AB) ≥ 0

  I(A:B) = 0  ⟺  ρ_AB = ρ_A ⊗ ρ_B   [no correlations]

Conditional mutual information:
  I(A:B|C)_ρ = S(ρ_AC) + S(ρ_BC) - S(ρ_ABC) - S(ρ_C)

Strong Subadditivity (Lieb-Ruskai 1973):
  S(ρ_ABC) + S(ρ_B) ≤ S(ρ_AB) + S(ρ_BC)

Equivalently:
  I(A:C|B) ≥ 0    [conditional quantum mutual information ≥ 0]
```

**Why SSA is hard**: Classical strong subadditivity is easy (follows from chain rule).
Quantum SSA requires Lieb-Ruskai theorem — a major result in matrix analysis (1973).
It took > 5 years after introduction of quantum entropy to prove.

**Consequences of SSA**:
- Concavity of S(ρ_A) as a function of ρ_AB (with ρ_B fixed) — not obvious
- Fundamental to proving many quantum capacity results
- Used in proving area laws in condensed matter (entanglement entropy of ground states)

**Classical subadditivity** is weaker: H(X,Y) ≤ H(X) + H(Y). Equality iff independent.
Quantum: S(ρ_AB) can be LESS than S(ρ_A) [or S(ρ_B)] for entangled states — no classical analog.

---

## 3. Entanglement Entropy

For a bipartite pure state |ψ⟩_AB in H_A ⊗ H_B:

```
Schmidt decomposition: |ψ⟩ = Σᵢ √λᵢ |aᵢ⟩|bᵢ⟩

Entanglement entropy: E(ψ) = S(ρ_A) = S(ρ_B) = H({λᵢ})

  λᵢ: Schmidt coefficients (eigenvalues of reduced density matrix ρ_A)

  Product state |ψ⟩ = |a⟩⊗|b⟩:     λ = {1,0,...}  → E = 0
  Bell state (|00⟩+|11⟩)/√2:         λ = {½,½}     → E = 1 ebit
  Maximally entangled d×d:            λ = {1/d,...} → E = log d ebits
```

**Operational interpretation** (LOCC interconversion):
- m copies of |ψ⟩ can be converted to n copies of Bell state (and vice versa)
  using local operations and classical communication iff m·E(ψ) ≈ n (asymptotically)
- E(ψ) is the unique measure of bipartite pure state entanglement
- Mixed state entanglement: much more complex (distillable entanglement ≠ entanglement cost)

**Area law** (condensed matter): Ground states of gapped local Hamiltonians typically satisfy
S(ρ_A) = O(|∂A|) — entanglement grows with boundary area, not volume. This justifies DMRG
and tensor network methods for 1D systems.

---

## 4. Quantum Channel Capacities

A quantum channel ε: ρ → ε(ρ) is a CPTP map. Multiple capacity notions:

```
┌─────────────────────────────────────────────────────────────────────┐
│  Classical capacity C:  max bits/channel use                        │
│    Holevo bound (single use): χ = S(Σᵢ pᵢ ε(ρᵢ)) - Σᵢ pᵢ S(ε(ρᵢ)) │
│    HSW theorem: C = lim_{n→∞} χ(ε^{⊗n})/n                         │
│    Superadditivity: χ(ε⊗ε) may exceed 2χ(ε) for some channels     │
│                                                                     │
│  Quantum capacity Q:  max qubits/channel use                        │
│    Coherent information: Ic(ρ,ε) = S(ε(ρ)) - S((id⊗ε)(|φ⟩⟨φ|))   │
│      where |φ⟩ is purification of ρ in reference system            │
│    LSD theorem: Q = lim_{n→∞} max_ρ Ic(ρ,ε^{⊗n})/n               │
│    Superadditivity: Q > single-use coherent info for some channels  │
│                                                                     │
│  Entanglement-assisted capacity C_E:                                │
│    C_E = max_{ρ} I(A:B) = max_{ρ} [S(ρ) + Ic(ρ,ε)]               │
│    No superadditivity: single-letter formula suffices              │
│    C_E ≥ C, Q  (pre-shared entanglement only helps)                 │
└─────────────────────────────────────────────────────────────────────┘
```

**Holevo bound** (C ≤ χ per channel use): Sending classical info by choosing ρ₁,...,ρₘ
(one per message) and measuring output. Bound = S(average output) - average S(individual outputs).
Not always tight for single-channel use, but tight in the limit.

**Why Q uses coherent information**: Q measures how well quantum information (superpositions)
survives the channel. Coherent information = S(output) - S(environment output) = S(output) - S(entanglement with reference). Positive coherent information means quantum info survives.

**No-cloning from linearity**: If cloning |ψ⟩→|ψ⟩|ψ⟩ were possible, it would be a linear map
only if |ψ⟩ is an eigenstate of the cloning operator — contradicts universality. Quantum capacity
of any channel ≤ (classical capacity)/2 for this reason (rough intuition).

**Quantum erasure channel**: With probability p, qubit erased (receiver told which location).
Q = max(0, 1 - 2p), C = 1 - p. Erasure of known location allows error correction up to p = ½.

---

## 5. Quantum Error Correction

**Quantum error correction conditions** (Knill-Laflamme): Code C ⊆ H_n with projector P_C
can correct errors {E_k} iff:

```
P_C E_k† E_l P_C = c_{kl} P_C   for all k, l

  [errors don't rotate code states relative to each other]

[[n,k,d]] code: encodes k logical qubits in n physical qubits,
  corrects errors on any ⌊(d-1)/2⌋ qubits

CSS codes: built from two classical codes C₁, C₂ with C₂⊥ ⊆ C₁
  Correct X errors with C₁, Z errors with C₂⊥ independently

Surface code: [[O(d²), 1, d]] — threshold ~1%,  local operations
  Toric code (Kitaev 1997): Z₂ gauge theory on torus
```

**Hashing bound**: Q ≥ max_ρ Ic(ρ,ε) for any single-letter input.
For Pauli channels (depolarizing, etc.), hashing = coherent information.

**Information in quantum error correction**: QEC trades physical qubits for error protection.
The no-cloning theorem prevents naive redundancy (you can't copy qubits). Instead, entanglement
distributes information non-locally across physical qubits.

---

## 6. Holographic Principle and Ryu-Takayanagi Formula

The deepest application of quantum information to physics: entanglement entropy encodes geometry.

```
Anti-de Sitter / Conformal Field Theory correspondence (Maldacena 1997):

  CFT on boundary  ←→  gravity in bulk AdS space

  ┌─────────────────────────────────────────────────────────┐
  │     Bulk (AdS)                                          │
  │        ·    ·                                           │
  │      ·        ·                                         │
  │     ·  γ_A ·   ·     γ_A = minimal surface             │
  │     ·   ╔══╗   ·            anchored to ∂A             │
  │     ·   ╚══╝   ·                                       │
  │      ·        ·                                         │
  │        ·    ·                                           │
  │  A ═══════════════ Ā   (boundary CFT split)             │
  └─────────────────────────────────────────────────────────┘

  Ryu-Takayanagi formula (2006):
    S(ρ_A) = Area(γ_A) / (4G_N)

  Entanglement entropy of boundary region A =
  Area of minimal bulk surface homologous to A,
  measured in Planck units
```

**Why this is profound**: The Bekenstein-Hawking entropy of a black hole S = A/(4G_N) is a
special case — the black hole horizon IS the minimal surface anchoring to the entire boundary.
Quantum entanglement in the CFT encodes the spatial geometry of the bulk.

**Tensor networks as toy models**: MERA (Multi-scale Entanglement Renormalization Ansatz)
and perfect tensor networks reproduce the Ryu-Takayanagi formula in discrete settings.
Each tensor = bulk lattice site; contraction = geometry; boundary = CFT state.

**Quantum error correction in holography**: The bulk-to-boundary map is a quantum error
correcting code (Almheiri-Dong-Harlow 2015). Different boundary regions can reconstruct
the same bulk operator — topological redundancy of holographic encoding.

---

## 7. Quantum Data Compression

**Schumacher compression** (quantum analog of Shannon's source coding):

For a source emitting pure states {|ψᵢ⟩} with probabilities {pᵢ}, forming ensemble
ρ = Σᵢ pᵢ|ψᵢ⟩⟨ψᵢ|:

```
Quantum typical subspace: span of typical eigenstates of ρ^{⊗n}
  Dimension ≈ 2^{nS(ρ)}

Schumacher's theorem:
  Rate S(ρ) qubits/symbol is achievable and necessary for faithful compression

  Compress: project onto typical subspace (dim 2^{nS(ρ)})
  Decompress: embed back in original Hilbert space

Fidelity: F(ρ^{⊗n}, decompress(compress(ρ^{⊗n}))) → 1
  as n → ∞ for rate > S(ρ)
```

**Contrast with classical**: Shannon compression rate = H(X) bits/symbol. Schumacher = S(ρ) qubits/symbol. Both are tight — the fundamental limits of lossless compression in their respective theories.

---

## Decision Cheat Sheet

| Quantity | Formula | Analogy | Key property |
|----------|---------|---------|--------------|
| Von Neumann entropy | S(ρ) = -Tr(ρ log ρ) | Shannon H | Pure state → S=0 |
| Quantum mutual info | I(A:B) = S_A+S_B-S_AB | Classical I(X;Y) | Always ≥ 0 |
| Entanglement entropy | E(ψ) = S(ρ_A) = S(ρ_B) | No classical analog | Unique for pure states |
| Coherent information | Ic = S_out - S_env | ≈ negative "noise" | Can be negative |
| Holevo quantity | χ = S(avg) - avg(S) | Classical MI bound | Bounds classical capacity |
| Quantum capacity | Q = lim Ic^{(n)}/n | Shannon capacity C | Superadditive |
| EA classical capacity | C_E = S + Ic | Beats classical C | Single-letter formula |

**Ordering**: C_E ≥ C ≥ Q ≥ 0 always. Entanglement assistance only helps.

---

## Common Confusion Points

**S(ρ_A) > S(ρ_AB) is possible**: For entangled states, the subsystem can have MORE entropy
than the whole system. This has no classical analog (classically H(X) ≤ H(X,Y) always).
Example: Bell state S(ρ_AB) = 0, S(ρ_A) = 1. The whole system is pure; subsystems are mixed.

**Classical capacity C requires regularization**: C = lim χ(ε^{⊗n})/n. You can't just compute
χ for a single channel use because superadditivity means using the channel multiple times
simultaneously beats independent uses. This is a major difference from classical theory.

**Coherent information can be negative**: Ic(ρ,ε) < 0 means the channel destroys quantum
information. The quantum capacity Q = 0 if Ic ≤ 0 for all input states (though this isn't
exactly right due to superadditivity). Negative Ic doesn't mean Q = 0 in general.

**Holographic entropy is not just thermodynamics**: The Ryu-Takayanagi formula is about
entanglement entropy in the dual CFT state, not thermal entropy. For pure states in CFT,
the bulk is a smooth spacetime; for mixed states, it may contain a black hole.

**Von Neumann entropy ≠ thermodynamic entropy in general**: Von Neumann entropy equals
thermodynamic entropy only for thermal (Gibbs) states ρ = e^{-βH}/Z. For arbitrary quantum
states, S(ρ) is a measure of quantum uncertainty, not directly a thermodynamic quantity.
