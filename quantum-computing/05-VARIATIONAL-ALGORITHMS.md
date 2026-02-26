# Variational Quantum Algorithms

## Big Picture: The Hybrid Classical-Quantum Loop

```
┌─────────────────────────────────────────────────────────────────────┐
│                  VARIATIONAL HYBRID ARCHITECTURE                    │
│                                                                     │
│  ┌──────────────────────────────────────────────────────────────┐   │
│  │                     QUANTUM DEVICE                           │   │
│  │                                                              │   │
│  │   |0⟩⊗ⁿ ──► [Ansatz U(θ)] ──► |ψ(θ)⟩ ──► Measure H        │   │
│  │                                         ──► ⟨H⟩(θ)         │   │
│  └───────────────────────────┬──────────────────────────────────┘   │
│                              │ cost value C(θ)                     │
│                              ▼                                      │
│  ┌──────────────────────────────────────────────────────────────┐   │
│  │                    CLASSICAL OPTIMIZER                       │   │
│  │                                                              │   │
│  │   θ_new = θ - η ∇C(θ)    (gradient-based)                   │   │
│  │   θ_new = COBYLA/SPSA    (gradient-free)                     │   │
│  │                                                              │   │
│  │   ∂C/∂θⱼ = [C(θ + π/2 eⱼ) - C(θ - π/2 eⱼ)] / 2           │   │
│  │            └──────────── parameter-shift rule ──────────┘   │   │
│  └───────────────────────────┬──────────────────────────────────┘   │
│                              │ new parameters θ                    │
│                              └──────────── (loop until converge) ──►│
└─────────────────────────────────────────────────────────────────────┘

  Foundation: Variational Principle
  ⟨ψ(θ)|H|ψ(θ)⟩ ≥ E₀  for all θ, all normalized |ψ(θ)⟩
  → minimize expectation value to approximate ground state energy
```

The variational principle is ancient (Rayleigh-Ritz, 1870s). VQE and QAOA are its NISQ-era instantiations: let a quantum circuit parameterize the trial state, use classical optimization to minimize the energy.

---

## Variational Principle — Mathematical Foundation

**Theorem (Variational Principle):** For any normalized state |ψ⟩:
```
⟨ψ|H|ψ⟩ ≥ E₀
```
where E₀ is the ground-state energy of H.

**Proof sketch:** Expand |ψ⟩ = Σᵢ cᵢ|φᵢ⟩ in the eigenbasis of H where H|φᵢ⟩ = Eᵢ|φᵢ⟩ with E₀ ≤ E₁ ≤ E₂ ≤ ···

```
⟨ψ|H|ψ⟩ = Σᵢ |cᵢ|² Eᵢ ≥ E₀ Σᵢ |cᵢ|² = E₀
```

since Σᵢ |cᵢ|² = 1 (normalization). Equality holds iff |ψ⟩ = |φ₀⟩ (true ground state). □

This gives the algorithm: parameterize |ψ(θ)⟩ richly enough that the true ground state is reachable (or close), then minimize ⟨H⟩(θ).

---

## VQE — Variational Quantum Eigensolver

### Problem Structure
```
TARGET: find ground state energy E₀ of molecular Hamiltonian H

H = Σᵢⱼ hᵢⱼ aᵢ†aⱼ + Σᵢⱼₖₗ hᵢⱼₖₗ aᵢ†aⱼ†aₖaₗ  (second quantization)
                                                  ↓ Jordan-Wigner / Bravyi-Kitaev
H = Σₖ αₖ Pₖ    where Pₖ ∈ {I,X,Y,Z}⊗ⁿ (Pauli strings)

Evaluate ⟨H⟩ = Σₖ αₖ ⟨Pₖ⟩  by measuring each Pauli term separately
```

### Ansatz Design

Two competing philosophies:

```
┌──────────────────────────────┬───────────────────────────────────────┐
│   HARDWARE-EFFICIENT ANSATZ  │    CHEMICALLY-INSPIRED ANSATZ         │
├──────────────────────────────┼───────────────────────────────────────┤
│ Designed around hardware     │ Designed around physics               │
│ topology and native gates    │ (UCC — Unitary Coupled Cluster)       │
│                              │                                       │
│ Ry(θ₁)─┐                    │ UCCSD: singles + doubles              │
│ Ry(θ₂)─┼─CNOT─Ry(θ₃)       │ |ψ⟩ = e^{T-T†}|HF⟩                  │
│ Ry(θ₄)─┘                    │ T = T₁ + T₂ (cluster operators)       │
│                              │                                       │
│ + Shallow circuit depth      │ + Chemical meaning, variational       │
│ + Fits device connectivity   │   completeness for small molecules    │
│ - No physical interpretation │ - Deep circuits (CNOT-heavy)         │
│ - May miss ground state      │ - Doesn't scale to large systems      │
│   (not chemically motivated) │                                       │
└──────────────────────────────┴───────────────────────────────────────┘
```

### Parameter Optimization

**Parameter-Shift Rule** (exact gradient on quantum hardware):
```
∂C/∂θⱼ = ½[C(θ + π/2 eⱼ) - C(θ - π/2 eⱼ)]

Derivation: For parameterized gate U(θⱼ) = e^{-iθⱼG/2} where G² = I (Pauli):
  eigenvalues of G are ±1, so spectrum of U is {e^{±iθⱼ/2}}
  → gradient is exactly the finite difference at ±π/2 shifts
  → no approximation — this IS the exact derivative
```

**Gradient-free methods** (used when circuit noise makes gradients unreliable):
- COBYLA: Powell's constrained optimization — linear approximation to objective
- SPSA (Simultaneous Perturbation Stochastic Approximation): perturb all parameters simultaneously with random ±1 vector; O(1) circuit evaluations per gradient estimate regardless of parameter count

---

## QAOA — Quantum Approximate Optimization Algorithm

### MaxCut Formulation
```
MAXCUT PROBLEM:
  Given graph G = (V, E), partition V into S, S̄ to maximize |{(u,v) ∈ E : u ∈ S, v ∈ S̄}|

CLASSICAL-TO-QUANTUM ENCODING:
  Variable xᵢ ∈ {0,1} → qubit i: |0⟩ or |1⟩
  Cut objective: C = Σ_{(i,j)∈E} (1 - ZᵢZⱼ)/2
     ZᵢZⱼ = +1 when same partition, -1 when different
     → want ZᵢZⱼ = -1 for each edge in cut

COST HAMILTONIAN:  Hc = Σ_{(i,j)∈E} (1 - ZᵢZⱼ)/2
MIXER HAMILTONIAN: Hb = Σᵢ Xᵢ   (drives transitions between cuts)
```

### Circuit Structure
```
QAOA at depth p:

|+⟩⊗ⁿ ──► [e^{-iγ₁Hc}] ──► [e^{-iβ₁Hb}] ──► ... ──► [e^{-iγₚHc}] ──► [e^{-iβₚHb}] ──► measure

Parameters: γ = (γ₁,...,γₚ), β = (β₁,...,βₚ) — 2p total

p = 1:  Farhi et al. proved approximation ratio ≥ 0.6924 for MaxCut on 3-regular graphs
p → ∞: QAOA converges to exact solution (adiabatic theorem limit)
p finite: approximation ratio improves but circuit depth grows; diminishing returns past p ~ n
```

### Approximation Ratio Guarantees

```
KNOWN RESULTS:
  p = 1, MaxCut on 3-regular:  AR ≥ 0.6924  (Farhi-Goldstone-Gutmann 2014)
  Goemans-Williamson (classical SDP): AR ≥ 0.878

  For p = 1: QAOA does NOT beat classical GW on MaxCut
  For large p: QAOA should asymptotically match exact solution
  Gap in between: not well understood theoretically

WARNING: QAOA approximation ratio for general instances
  at polynomial depth is an OPEN PROBLEM
```

---

## Barren Plateaus — The Fundamental Obstacle

### The Problem
```
RANDOM n-QUBIT ANSATZ:
  U(θ) = random parameterized circuit with depth d

  E[∂C/∂θⱼ] = 0                           (zero mean by symmetry)
  Var[∂C/∂θⱼ] ≤ f(n) → 0 exponentially fast in n

  For a global cost function C = ⟨ψ(θ)|O|ψ(θ)⟩, O acting on all qubits:
  Var[∂C/∂θⱼ] ∈ O(2^{-n})

→ GRADIENTS VANISH EXPONENTIALLY WITH SYSTEM SIZE
→ Need exponentially many shots to estimate gradient to noise-floor precision
```

**Why it happens:** Deep random circuits form approximate unitary 2-designs. The state |ψ(θ)⟩ is essentially uniformly distributed on the Hilbert space. The cost function is nearly constant on this sphere, so all gradients are exponentially small.

**Formal statement (McClean et al. 2018):** For a unitary 2-design U(θ) and global observable O:
```
Var_θ[⟨∂C/∂θⱼ⟩] = C₁/2^n · Tr(O²) - C₁/4^n · [Tr(O)]²
where C₁ is a circuit-architecture constant
→ vanishes as 2^{-n}
```

### Mitigation Strategies

```
┌──────────────────────────────────────────────────────────────────────┐
│ MITIGATION STRATEGY          │ MECHANISM               │ LIMITATION  │
├──────────────────────────────┼─────────────────────────┼─────────────┤
│ Local cost functions         │ Measure subsystems, not  │ May not     │
│ C = Σᵢ ⟨Oᵢ⟩ (k-local O)    │ global — Var ~ O(1/poly) │ approximate │
│                              │ for constant k           │ global obj  │
├──────────────────────────────┼─────────────────────────┼─────────────┤
│ Layerwise training           │ Train one layer at a     │ Local optima│
│ (greedy initialization)      │ time, fix previous       │ not avoided │
├──────────────────────────────┼─────────────────────────┼─────────────┤
│ Structured ansatz            │ Problem-specific U(θ):   │ Requires    │
│ (UCC, QAOA, MERA)            │ not 2-design-like        │ domain know │
├──────────────────────────────┼─────────────────────────┼─────────────┤
│ Warm starting                │ Initialize near known    │ Need good   │
│ (classical pre-solve)        │ solution; small θ range  │ initial pt  │
├──────────────────────────────┼─────────────────────────┼─────────────┤
│ Correlation-based pruning    │ Remove parameters with   │ Overhead;   │
│ (parameter freezing)         │ small gradients early    │ heuristic   │
└──────────────────────────────┴─────────────────────────┴─────────────┘
```

---

## Expressibility vs Trainability Tradeoff

```
            HIGH EXPRESSIBILITY
           (can represent any state)
                    ▲
                    │
         Random    ●  ← BARREN PLATEAU TERRITORY
         circuits   │    (unitary 2-design, gradients vanish)
                    │
     TRADEOFF       │
      CURVE         ●  ← Hardware-efficient ansatz
                    │    (moderate expressibility, trainable)
                    │
        Structured  ●  ← UCCSD, QAOA
        ansätze     │    (low expressibility, good gradients)
                    │
                    ●  ← Fixed circuit (product state)
                    │    (not expressive, trivially trainable)
                    ▼
            LOW EXPRESSIBILITY
            (restricted function class)

HORIZONTAL: Trainability (gradient magnitude) ──────────────►
```

You can't have both. A circuit expressive enough to represent arbitrary quantum states is essentially a random unitary and has barren plateaus. The art of VQA design is finding structured circuits that contain the target state (high effective expressibility) without becoming 2-design-like.

---

## Classical Simulation Limits: When Is VQE Actually Useful?

```
CLASSICAL METHODS VS VQE:

┌──────────────────────────────────────────────────────────────────────┐
│ PROBLEM SIZE    │ BEST CLASSICAL           │ VQE ADVANTAGE?          │
├──────────────────┼──────────────────────────┼─────────────────────────┤
│ n ≤ 20 electrons │ Full Configuration        │ No — FCI is exact       │
│                  │ Interaction (FCI): exact  │ and fast                │
├──────────────────┼──────────────────────────┼─────────────────────────┤
│ n ~ 30-50        │ DMRG: near-exact for 1D  │ Maybe — strongly        │
│                  │ CCSD(T): chemical accuracy│ correlated 2D systems   │
│                  │ for weakly correlated     │                         │
├──────────────────┼──────────────────────────┼─────────────────────────┤
│ n ~ 100+         │ DFT: scales as O(n³),    │ In principle — but need │
│                  │ approximate              │ error-corrected qubits  │
│                  │ Tensor network methods   │ (not NISQ)              │
├──────────────────┼──────────────────────────┼─────────────────────────┤
│ Strongly corr.   │ No reliable classical    │ Target use case —       │
│ 2D systems       │ method (sign problem in  │ FeMoco, high-Tc         │
│ (FeMoco, Cu-O)   │ QMC)                     │ superconductors         │
└──────────────────┴──────────────────────────┴─────────────────────────┘

HONEST ASSESSMENT:
  - For NISQ-scale VQE: classical methods still competitive or better
  - For fault-tolerant quantum: genuine advantage expected for n ~ 50-100
    strongly correlated electrons
  - QAOA on combinatorial: no proven advantage over classical heuristics
    (simulated annealing, GW SDP) at polynomial depth
```

---

## Decision Cheat Sheet

```
┌──────────────────────────────────────────────────────────────────────┐
│ SCENARIO                     │ RECOMMENDATION                       │
├──────────────────────────────┼───────────────────────────────────────┤
│ Ground state energy,         │ UCCSD-VQE or hardware-efficient VQE  │
│ small molecule (< 20 qubits) │ Compare with CCSD(T) classically     │
├──────────────────────────────┼───────────────────────────────────────┤
│ Ground state energy,         │ Wait for fault-tolerant hardware;    │
│ large/strongly correlated    │ current VQE won't beat DMRG/QMC      │
├──────────────────────────────┼───────────────────────────────────────┤
│ Combinatorial optimization   │ QAOA for benchmarking/research;      │
│ (MaxCut, portfolio opt.)     │ for production: use GW/SA classically │
├──────────────────────────────┼───────────────────────────────────────┤
│ Barren plateau suspected     │ Switch to local cost, structured      │
│ (gradient ≈ 0 for all θ)    │ ansatz, or warm start                 │
├──────────────────────────────┼───────────────────────────────────────┤
│ Gradient evaluation          │ Parameter-shift rule on hardware;    │
│ on noisy hardware            │ SPSA when noise dominates            │
├──────────────────────────────┼───────────────────────────────────────┤
│ p-depth for QAOA             │ p = 1 for benchmarking; p ≥ 5 for   │
│                              │ meaningful approximation ratio        │
└──────────────────────────────┴───────────────────────────────────────┘
```

---

## Common Confusion Points

**VQE is not just "quantum gradient descent."** The quantum device evaluates the cost function (energy expectation). The classical computer runs the optimizer. The gradient is computed by two quantum circuit evaluations (parameter-shift), not backpropagation through the quantum gate.

**Parameter-shift rule requires gates of the form e^{-iθG/2} with G² = I.** Not all parameterized gates satisfy this. For generators with more than two eigenvalues, generalized shift rules exist but are more complex.

**QAOA depth p is not the same as circuit layers in VQE.** QAOA has a specific structure from the cost/mixer Hamiltonians. p = 1 has provable guarantees; higher p is better but circuits get deeper.

**Barren plateaus affect global cost functions regardless of optimizer.** Switching from gradient-based to gradient-free (COBYLA, SPSA) doesn't solve the barren plateau problem — gradient-free methods also need to evaluate cost at many points, and if the landscape is flat, they're equally blind.

**Expressibility is not the same as trainability.** A circuit family can be highly expressive (can represent any state) yet completely untrainable (gradients vanish). The useful regime is structured expressibility: rich enough to contain the target state, constrained enough to have gradient signal.

**VQE on NISQ hardware does not yet demonstrate quantum advantage** for any practically relevant molecule. The comparison point is CCSD(T)/DMRG, not exact diagonalization. Current NISQ VQE results on H₂, LiH, BeH₂ are proofs of concept, not computationally superior to classical methods.
