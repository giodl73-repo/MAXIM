# Ising Model and Lattice Systems

## The Big Picture

The Ising model is the hydrogen atom of statistical mechanics. Simple enough to admit exact
solutions in 1D and 2D, rich enough to capture the essential physics of phase transitions,
and general enough that it maps to dozens of other problems. The 1D solution is a warm-up;
the 2D Onsager solution (1944) is one of the most celebrated exact results in all of physics.
Monte Carlo simulation of the Ising model is the prototype for all computational statistical
mechanics. And the Hopfield model (1982) shows that an Ising-like network can store and
retrieve memories — bridging statistical physics and neural networks.

```
ISING MODEL LANDSCAPE
═══════════════════════════════════════════════════════════════════════════════

  HAMILTONIAN:  H = −J Σ_{⟨ij⟩} sᵢ sⱼ − h Σᵢ sᵢ    (sᵢ = ±1)

  ┌──────────────────────────────────────────────────────────────────────┐
  │  1D: exact solution (transfer matrix) — no phase transition T > 0    │
  │  2D: exact solution (Onsager 1944) — T_c = 2.27 J/k_B, β = 1/8     │
  │  3D: no exact solution — Monte Carlo, ε-expansion, conformal field   │
  │  Mean-field: T_c = zJ/k_B, β = 1/2 (always overestimates order)      │
  └──────────────────────────────────────────────────────────────────────┘

  MAPPINGS:
  Ising ↔ Binary alloy (A/B atoms ↔ ±1 spins)
  Ising ↔ Lattice gas (particle/hole ↔ ±1 spins)
  Ising ↔ Hopfield network (stored patterns ↔ couplings Jᵢⱼ)
  Ising ↔ MAX-CUT in graphs (graph partition ↔ spin configuration)
  Ising ↔ Boltzmann machine in ML
```

---

## 1D Ising — Transfer Matrix Solution

**Model**: N spins on a line with periodic boundary conditions (s_{N+1} = s₁).

**Partition function**:

    Z = Σ_{s₁,...,s_N = ±1} exp(K Σᵢ sᵢ sᵢ₊₁ + h Σᵢ sᵢ)

where K = J/k_BT, h here stands for βh_field.

**Transfer matrix** T is a 2×2 matrix:

    T_{s,s'} = exp(K ss' + (h/2)(s + s'))

    T = | e^{K+h}    e^{-K}  |
        | e^{-K}    e^{K-h}  |

The partition function:

    Z = Tr(T^N) = λ₊^N + λ₋^N ≈ λ₊^N    (N → ∞, λ₊ > λ₋)

where λ₊ > λ₋ are the eigenvalues of T:

    λ_± = e^K cosh(h) ± √(e^{2K} sinh²(h) + e^{-2K})

**At h = 0**:

    λ₊ = 2 cosh(K) = e^K + e^{-K}    λ₋ = 2 sinh(K) = e^K − e^{-K}

    f = −k_BT ln λ₊ = −k_BT ln(2 cosh(J/k_BT))

**Free energy is analytic for all T > 0** — no phase transition.

**Correlation function**:

    ⟨s₀ s_r⟩ = (λ₋/λ₊)^r = tanh^r(K) = e^{-r/ξ}

    ξ = −1/ln(tanh K) → ∞ as T → 0 (K → ∞): ordered at T = 0 only.

```
1D ISING — WHY NO PHASE TRANSITION:

  Peierls argument: A single domain wall (two neighboring spins flipped
  relative to each other) costs energy 2J but gains entropy k_B ln N
  (N possible positions for the wall). For N → ∞ and any T > 0,
  entropy wins → domain walls proliferate → long-range order destroyed.

  Only at T = 0 can you have order.
  This is a general argument: in 1D with short-range interactions,
  there is no phase transition at T > 0 (Landau, 1937;
  Mermin-Wagner for continuous symmetry in 2D, 1966).
```

---

## 2D Ising — Onsager's Exact Solution

Lars Onsager (1944) solved the 2D Ising model on a square lattice exactly, in zero field. This was a landmark — the first exact solution of a statistical mechanical model showing a genuine phase transition.

**Exact free energy per spin** (h = 0):

    f = −k_BT [ln(2 cosh 2K) + (1/2π) ∫₀^π dθ ln(1 − κ sin θ)]

where κ = 2 sinh(2K)/cosh²(2K).

**Critical point**: κ = 1, giving:

    sinh(2K_c) = 1    ⟹    K_c = J/k_BT_c = (1/2) ln(1+√2) ≈ 0.4407

    k_B T_c = 2J/ln(1+√2) ≈ 2.269 J

**Specific heat**:

    C_V ~ −A ln|T − T_c| + const    (logarithmic divergence)

This means α = 0 (logarithmic), not the simple power law form.

**Spontaneous magnetization** (zero-field order parameter, Onsager-Yang):

    m = ⟨s⟩ = [1 − sinh^{-4}(2K)]^{1/8}    (T < T_c)

Near T_c:

    m ≈ B(1 − T/T_c)^{1/8}    ⟹    β = 1/8

**Critical exponents for 2D Ising**:

| Exponent | 2D Ising (exact) | Mean-field |
|---------|-----------------|-----------|
| α | 0 (log) | 0 (jump) |
| β | 1/8 | 1/2 |
| γ | 7/4 | 1 |
| ν | 1 | 1/2 |
| η | 1/4 | 0 |

The exact 2D exponents satisfy all scaling relations, providing a non-trivial check.

---

## Transfer Matrix — General Structure

The transfer matrix approach generalizes:

```
TRANSFER MATRIX METHOD:

  For a 1D chain or a quasi-1D system (2D lattice = chain of rows):

  Z = Tr(T^N)    where T is the transfer matrix between adjacent layers

  THERMODYNAMIC PROPERTIES (N → ∞):
  f = −k_BT ln λ_max    (free energy from largest eigenvalue)
  ξ = −1/ln(λ₂/λ₁)     (correlation length from ratio of two largest eigenvalues)

  FOR 2D ISING (M columns, N rows):
  T is a 2^M × 2^M matrix (exponentially large — why 2D is hard).
  Onsager diagonalized this matrix exactly using Clifford algebras.

  QUANTUM ANALOGY:
  Transfer matrix T ↔ Boltzmann operator e^{-βH_quantum}
  2D classical stat mech ↔ 1D quantum mechanics
  More precisely: T = e^{-H_quantum δτ} where δτ = 1/(k_BT per row)
  This maps d-dimensional classical systems to (d-1)-dimensional quantum systems.
```

---

## Monte Carlo Methods

For 3D Ising (and virtually all realistic systems), exact solutions don't exist. Monte Carlo (MC) simulation samples the partition function stochastically.

**Metropolis algorithm** (1953):

```
METROPOLIS ALGORITHM FOR ISING:

  Initialize: random spin configuration {s}
  Repeat:
    1. Pick a spin sᵢ at random
    2. Compute ΔE = energy change if sᵢ → −sᵢ
       ΔE = 2J sᵢ Σ_{j∈nbrs} sⱼ + 2h sᵢ
    3. Accept flip with probability:
       P_accept = min(1, e^{-βΔE})
       If ΔE ≤ 0: always accept (lower energy)
       If ΔE > 0: accept with probability e^{-βΔE}
    4. Measure observables periodically

  This satisfies DETAILED BALANCE:
  P(s→s') W(s') = P(s'→s) W(s)  where W(s) ∝ e^{-βH(s)}
  → ergodic chain converges to Boltzmann distribution.

  CRITICAL SLOWING DOWN near T_c:
  Correlation time τ ~ ξ^z where z ≈ 2 (dynamic exponent).
  ξ → ∞ at T_c → exponentially slow equilibration.
  Fix: Cluster algorithms (Wolff, Swendsen-Wang) update entire clusters
  at once, reducing z to near 0.
```

**Wolff cluster algorithm**:

1. Start with a random seed spin.
2. Probabilistically add neighboring spins of the same orientation to the cluster with probability P_add = 1 − e^{-2βJ}.
3. Flip the entire cluster.

This is much more efficient near T_c because it flips correlated domains.

---

## Mean-Field Ising Model — Curie-Weiss

In the mean-field (Curie-Weiss) model, every spin interacts equally with every other spin:

    H = −(J/N) Σ_{i<j} sᵢ sⱼ − h Σᵢ sᵢ    = −(J/2N)(Σᵢ sᵢ)² + const − h Σᵢ sᵢ

This is exactly solvable by a Hubbard-Stratonovich transformation or direct saddle-point:

    Z = ∫_{-∞}^∞ dm N e^{-N f(m)}    where f(m) = (J/2)m² − k_BT ln(2 cosh(β(Jm+h)))

Saddle-point equation: ∂f/∂m = 0 gives m = tanh(β(Jm+h)) — the mean-field self-consistency equation.

Critical temperature: T_c = J/k_B (one interaction per spin in Curie-Weiss).

---

## Hopfield Network and Neural Connections

The Hopfield model (1982) is an Ising-like recurrent neural network used for associative memory.

**Setup**: N neurons, state sᵢ = ±1. Couplings:

    Jᵢⱼ = (1/N) Σ_{μ=1}^p ξᵢ^μ ξⱼ^μ    (Hebb's rule: store p patterns {ξ^μ})

**Energy function**:

    E = −(1/2) Σ_{i≠j} Jᵢⱼ sᵢ sⱼ    (same as Ising with these couplings)

The energy function is minimized by the stored patterns. Starting from a corrupted pattern, asynchronous updates converge to the nearest stored pattern (energy minimum).

```
HOPFIELD ↔ ISING CORRESPONDENCE:

  Hopfield neuron sᵢ = ±1    ↔    Ising spin sᵢ = ±1
  Synaptic weights Jᵢⱼ       ↔    Exchange couplings Jᵢⱼ
  Stored patterns             ↔    Local energy minima
  Recall                      ↔    Energy minimization (zero T dynamics)
  Noise temperature T         ↔    Temperature of Ising model
  Storage capacity p/N ≤ 0.14 ↔    Phase transition in Ising spin glass

  AT TEMPERATURE T > 0:
  The network makes probabilistic updates: P(sᵢ=1) = σ(β Σⱼ Jᵢⱼ sⱼ)
  where σ(x) = 1/(1+e^{-x}) is the sigmoid = Fermi-Dirac at ε=0.

  This is the BOLTZMANN MACHINE (Hinton, Sejnowski 1985):
  a stochastic Hopfield network trained by maximizing log-likelihood.
  Training = matching model statistics to data statistics.
```

**Storage capacity**: Hopfield proved that for p << 0.14N patterns, retrieval is reliable. Above this threshold, interference between patterns causes catastrophic errors (spin glass phase). The phase transition is analyzed by the replica method — a technique from spin glass theory.

---

## Spin Glasses

Beyond ferromagnets: **spin glasses** have random couplings Jᵢⱼ (positive AND negative), creating frustration.

**Sherrington-Kirkpatrick model** (SK model, infinite-range spin glass):

    H = −Σ_{i<j} Jᵢⱼ sᵢ sⱼ    where Jᵢⱼ ~ N(0, J/√N) i.i.d.

This model has a glass transition at T_g, below which the system freezes into one of many metastable configurations. The **replica trick** (analytical continuation in replica number n) and **replica symmetry breaking** (Parisi 1979) solve this model.

The SK model is formally equivalent to the Hopfield model with random patterns — both undergo a spin glass transition when the system is overloaded.

**Parisi's replica symmetry breaking (RSB)**: The SK model is solved via the replica trick: compute Z^n for integer n, then analytically continue to n → 0. The naive (replica-symmetric) solution is unstable below T_g. Parisi (1979, Nobel Prize 2021) showed that the correct solution breaks replica symmetry in a hierarchical pattern:

```
SPIN GLASS ENERGY LANDSCAPE — ULTRAMETRIC STRUCTURE:

  Energy
    │     ╱╲           ╱╲               ╱╲
    │    ╱  ╲         ╱  ╲             ╱  ╲
    │   ╱ ╱╲ ╲       ╱ ╱╲ ╲           ╱ ╱╲ ╲
    │  ╱ ╱  ╲ ╲     ╱ ╱  ╲ ╲         ╱ ╱  ╲ ╲
    │ ·  ·  ·  ·   ·  ·  ·  ·       ·  ·  ·  ·
    └──────────────────────────────────────────── configuration

  The landscape is a hierarchy of metastable states:
  - Many "pure states" (valleys), each with overlap q between them
  - Overlap q(x) is the Parisi order parameter, 0 ≤ x ≤ 1
  - States within the same valley have q close to 1
  - States in distant valleys have small q
  - The hierarchy is ULTRAMETRIC: d(A,C) ≤ max(d(A,B), d(B,C))
    (like a taxonomy tree — all distances are determined by the
    most recent common ancestor)
```

**Spin glasses as optimization landscapes**: The connection to TCS is direct. The ground state of a spin glass is an NP-hard optimization problem (equivalent to MAX-CUT on a weighted graph). The replica method from spin glass theory predicts phase transitions in random combinatorial problems:

| CSP Problem | Spin Glass Analog | Critical Threshold |
|-------------|-------------------|-------------------|
| Random k-SAT | Diluted spin glass, k-body interactions | α_s(k) clauses/variable |
| Random MAX-CUT | ±J Ising on random graph | ~ 0.763N |
| Number partitioning | 1D random-field Ising | Phase transition at N ~ 2^{c·M} |
| Graph coloring | Potts glass | q colors, c edges/vertex threshold |
| TSP | Continuous spin glass | Parisi-type RSB in random instances |

The satisfiability threshold for random 3-SAT (α_s ≈ 4.267) was predicted by the cavity method (the spin glass "belief propagation" algorithm) before being rigorously proved. Survey propagation — an algorithm derived from 1-RSB spin glass theory — is the best known algorithm for random k-SAT near the threshold.

---

## Lattice Models Beyond Ising

```
GENERALIZATIONS:

  Potts model: sᵢ ∈ {1,...,q}  (q=2 is Ising)
  H = −J Σ_{⟨ij⟩} δ(sᵢ, sⱼ)
  q=1: connected clusters (random bond percolation)
  q → 0: spanning trees
  q=2: Ising  |  q=3,4: exact in 2D; first-order for q>4 in 2D

  XY model: sᵢ ∈ U(1), θᵢ ∈ [0,2π)
  H = −J Σ_{⟨ij⟩} cos(θᵢ − θⱼ)
  2D XY: Berezinskii-Kosterlitz-Thouless transition (topological!)
         No symmetry breaking; but superfluid stiffness jumps.
         Vortex-antivortex unbinding transition.
         KTH Prize 2016.

  Heisenberg model: sᵢ ∈ S² (3D unit vector)
  H = −J Σ_{⟨ij⟩} sᵢ·sⱼ
  2D Heisenberg: NO phase transition at T>0 (Mermin-Wagner)
  3D Heisenberg: transition at T_c, O(3) universality class
```

---

## Decision Cheat Sheet

| Model | Dimension | Phase transition | Method |
|-------|-----------|-----------------|--------|
| 1D Ising | 1D | No (T>0) | Transfer matrix; ξ = −1/ln(tanh K) |
| 2D Ising | 2D | Yes, T_c = 2.269 J/k_B | Onsager exact; β=1/8 |
| 3D Ising | 3D | Yes, T_c ≈ 4.51 J/k_B | Monte Carlo; β≈0.326 |
| Mean-field (Curie-Weiss) | any | Yes, T_c = zJ/k_B | Saddle-point; β=1/2 |
| Hopfield (p < 0.14N) | — | Retrieves patterns | Energy minimization |
| Hopfield (p > 0.14N) | — | Spin glass phase | Replica method |
| 2D XY | 2D | BKT topological | Vortex unbinding |

| Monte Carlo step | Formula / Rule |
|----------------|---------------|
| Metropolis acceptance | min(1, e^{-β ΔE}) |
| Energy change for one flip | ΔE = 2J sᵢ Σ_{j∈nbrs} sⱼ + 2h sᵢ |
| Critical slowing down | τ ~ ξ^z, z≈2 |
| Wolff cluster add probability | P_add = 1 − e^{-2βJ} |

---

## Common Confusion Points

**β = 1/8 for 2D Ising is exact, not approximate**: Onsager's solution is exact for the square lattice 2D Ising model. The exponent β = 1/8 is not a series approximation or mean-field result. This is remarkable — a non-trivial rational number from an exact calculation of the thermodynamic limit of a statistical mechanical model.

**Metropolis satisfies detailed balance, but detailed balance alone does not guarantee correctness**: You also need ergodicity — the chain must be able to reach any configuration from any other. For the Ising model, single-spin flips are ergodic. For some constrained models (conserved magnetization), you need different moves.

**The Hopfield network "memories" are local energy minima, not global**: The energy landscape has many local minima (spurious states: mixtures of stored patterns, reversed patterns). Above ~14% capacity, the network fails to recall stored patterns reliably — too many spurious states compete. This is not a flaw in the model; it reflects the physics of spin glasses.

**Modern Hopfield networks and Transformer attention**: The classical Hopfield network stores ~0.14N patterns using a quadratic energy E = −(1/2)Σ_{ij} J_{ij} s_i s_j. Ramsauer et al. (2020) showed that replacing the quadratic energy with a higher-order interaction energy E = −log Σ_μ exp(ξ^μ · s) — a log-sum-exp of pattern-state overlaps — exponentially increases storage capacity to O(e^{αN}) patterns. The update rule for this modern Hopfield network is:

    s^{new} = softmax(β Ξ^T s^{old}) · Ξ

where Ξ is the matrix of stored patterns. This is exactly the self-attention mechanism in Transformers: queries = current state, keys = stored patterns, values = stored patterns, and softmax(QK^T/√d) · V is the Hopfield update. The classical Hopfield → modern Hopfield → Transformer attention chain closes the loop between Ising-like associative memory and the dominant ML architecture.

**BKT transition — topological phase transitions beyond Landau**: The Berezinskii-Kosterlitz-Thouless transition in the 2D XY model does not fit the Landau symmetry-breaking framework. There is no local order parameter that turns on at T_c — instead, the transition is driven by topological defects (vortices).

```
BKT VORTEX-ANTIVORTEX UNBINDING:

  Below T_BKT: vortex-antivortex pairs bound (dipoles).
               No free vortices. Algebraic (power-law) correlations:
               ⟨cos(θ(0) − θ(r))⟩ ~ r^{−η(T)}  (quasi-long-range order)
               Superfluid stiffness ρ_s > 0.

  At T_BKT:   Pairs unbind → free vortices proliferate.
              Superfluid stiffness jumps DISCONTINUOUSLY to zero:
              ρ_s(T_BKT⁻) = 2k_BT_BKT/π  (universal jump)
              Correlation length diverges EXPONENTIALLY:
              ξ ~ exp(b/√(T − T_BKT))  (essential singularity, not power law)

  Above T_BKT: Free vortices destroy coherence.
               Exponential correlation decay: ⟨cos(θ(0)−θ(r))⟩ ~ e^{−r/ξ}

  KEY DISTINCTION from Ising-type transitions:
  - No symmetry breaking (⟨e^{iθ}⟩ = 0 on both sides in 2D)
  - No power-law divergence of ξ (essential singularity instead)
  - Transition is in the topology of the defect configuration, not
    in the order parameter
  - Nobel Prize 2016 (Kosterlitz, Thouless, Haldane)
```

This is the prototype for all topological phase transitions: the transition is between a phase with bound topological defects and one with free defects, classified by a topological invariant (winding number) rather than a broken symmetry.

**Mean-field theory overestimates T_c because it ignores fluctuations**: Mean-field gives T_c = zJ/k_B (z = coordination number). The actual T_c is lower because fluctuations reduce the effective coupling. In 2D with z = 4: mean-field gives T_c = 4J/k_B, but the exact answer is 2.269 J/k_B — 43% lower. The discrepancy grows as dimension decreases (more fluctuations in lower dimensions).
