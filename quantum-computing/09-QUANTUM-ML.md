# Quantum Machine Learning — Honest Assessment

## Big Picture: Hype vs Reality

```
┌─────────────────────────────────────────────────────────────────────┐
│                 QML CLAIMS — CREDIBILITY SPECTRUM                   │
│                                                                     │
│   SOLID                PLAUSIBLE            SPECULATIVE  DEBUNKED   │
│   ─────────────────────────────────────────────────────────────────│
│   Quantum              Quantum kernels       Quantum NNs  HHL for   │
│   simulation           (no dequantization)   speedup      classical │
│   for molecular        over classical ML     over CNNs    data      │
│   properties           verified                                     │
│                                                                     │
│   Quantum              QML for quantum       Quantum      Quantum   │
│   sampling             data generated        speedup for  random    │
│   (theoretically       by quantum systems    NLP/vision   forests   │
│   hard classically)                                                 │
│                                                                     │
│   VQE energies         Grover-based          Quantum      "Quantum  │
│   as ML features       speedup for           kernels beat GPU       │
│                        database search       classical   training"  │
│                        (polynomial only)     SVM on real            │
│                                              data                   │
└─────────────────────────────────────────────────────────────────────┘
```

---

## The Promise — Where Quantum Speedups Come From

### HHL Algorithm for Linear Systems

```
PROBLEM: Solve Ax = b (A is n×n Hermitian, b is n-vector)
CLASSICAL: O(n³) (Gaussian elimination) or O(n²) (iterative, well-conditioned)
QUANTUM (HHL, 2009): O(log n · κ² / ε)  where κ = condition number, ε = precision

APPARENT SPEEDUP: exponential in n (log n vs n)

THE CATCH — WHY HHL SPEEDUP IS LARGELY ILLUSORY:
  1. INPUT PROBLEM (state preparation):
     Classical vector b of n entries → quantum state |b⟩ = Σ bᵢ|i⟩/‖b‖
     Creating this quantum state requires O(n) operations (you have to read all n entries)
     → Bottleneck is state prep, not the algorithm
     EXCEPTION: if b is already a quantum state (from quantum sensor, etc.)

  2. OUTPUT PROBLEM (readout):
     x is encoded as quantum state |x⟩
     To read out all n entries: measure repeatedly → O(n/ε²) samples needed
     → Destroys the exponential speedup

  3. CONDITION NUMBER:
     HHL runtime is O(κ²) — for ill-conditioned matrices (κ >> 1), slow even quantumly
     Classical preconditioned iterative methods often achieve O(κ) or better

  4. GATE COUNT IN PRACTICE:
     HHL requires quantum phase estimation (expensive) + oracle for A (expensive)
     Actual circuit depth for problem of interest >> T₁/T₂

NET RESULT: HHL provides exponential speedup ONLY when:
  - Input b is a quantum state (not classical data)
  - You want a quantum state output (not classical numbers)
  - κ is poly(log n)
  → These conditions exclude almost all practical ML applications
```

---

## Quantum Kernel Methods

### The Setup

```
CLASSICAL SVM KERNEL TRICK:
  Map data x → φ(x) ∈ feature space F
  Kernel: k(xᵢ, xⱼ) = ⟨φ(xᵢ), φ(xⱼ)⟩
  SVM only needs kernel matrix K, not explicit φ
  Power: k can be high/infinite-dimensional feature map
         (RBF kernel: F is infinite-dimensional RKHS)

QUANTUM KERNEL:
  Map data x → quantum state via feature circuit: |φ(x)⟩ = U(x)|0⟩
  Quantum kernel: k(xᵢ, xⱼ) = |⟨φ(xᵢ)|φ(xⱼ)⟩|² = |⟨0|U†(xᵢ)U(xⱼ)|0⟩|²
  Evaluate via SWAP test or destructive SWAP:

  SWAP TEST:
    |0⟩ ──H──●──H── measure
    |φ(x)⟩  SWAP
    |φ(x')⟩──────
    P(0) = ½(1 + |⟨φ(x)|φ(x')⟩|²) → kernel value

  INVERSION TEST (destructive, more efficient):
    Apply U†(xᵢ)U(xⱼ)|0⟩ and measure probability of |0⟩ outcome
```

### Havlíček et al. (2019) — The Key Paper

```
SETUP: Second-order Pauli feature map
  x ∈ ℝⁿ → quantum state |φ(x)⟩ via:
  U_φ(x) = exp(i Σ_{j<k} φⱼₖ(x) ZⱼZₖ) · exp(i Σⱼ xⱼ Zⱼ) repeated

  where φⱼₖ(x) = (π - xⱼ)(π - xₖ)  (nonlinear feature encoding)

CLAIM: This feature map is classically hard to simulate efficiently
  (for appropriate parameter choices, evaluating k(x,x') classically
   would require classical simulation of the quantum circuit, which is
   assumed hard for deep enough circuits)

EXPERIMENTAL RESULT:
  Small dataset, few qubits, quantum kernel SVM matches classical SVM
  → Proof of concept, not evidence of advantage

DEQUANTIZATION CONCERN (Tang 2018 style):
  Tang's key insight: the quantum recommendation algorithm's speedup relied on
  efficient sampling from low-rank matrices — but classical algorithms can do
  this too via Monte Carlo row sampling given "sample access" to the input.
  The quantum hardware was performing a logical operation (low-rank sampling)
  that didn't actually require quantum mechanics — like discovering a
  distributed system's claimed advantage depended on a data structure the
  single-node system could also use.

  Classical "quantum-inspired" algorithms often match quantum kernel
  performance using random features / low-rank approximations
  → Classical SVMs with RBF / polynomial kernels often competitive

GENUINE OPEN QUESTION:
  Is there a practical dataset where quantum kernel provably outperforms
  all classical kernels? No example demonstrated as of 2025.
```

---

## Quantum Neural Networks (QNNs)

### Parameterized Quantum Circuits as Function Approximators

```
QNN STRUCTURE:
  Input x → encode as initial state: |ψ_in(x)⟩
  Apply parameterized circuit U(θ): |ψ(x,θ)⟩ = U(θ)|ψ_in(x)⟩
  Measure observable: ŷ = ⟨ψ(x,θ)|O|ψ(x,θ)⟩
  Loss: L(θ) = ΣΣ (yᵢ - ŷᵢ)²
  Gradient: parameter-shift rule

EXPRESSIBILITY:
  n-qubit QNN with depth d: can represent any function in span of
  exponentially many Fourier modes (data-encoding dependent)
  BUT: Universal function approximation doesn't imply efficient learning

TRAINING PROBLEMS:
  Barren plateaus (see 05): gradients vanish exponentially
  Local minima in loss landscape
  No activation functions → hard to build deep representations
  Shot noise: gradient estimates require many circuit evaluations

COMPARISON TO CLASSICAL NN:
  Classical 2-layer MLP: universal approximator, trainable by SGD
  QNN: also universal (in principle), but:
    - Gradients vanish (barren plateaus)
    - No demonstrated advantage over classical NN on any task
    - Much more expensive to evaluate (quantum circuit vs GPU matmul)

HONEST VERDICT: QNNs as classical data classifiers have no demonstrated
  advantage over classical NNs and significant trainability disadvantages.
  Not a promising near-term direction.
```

---

## Quantum Sampling — The Strongest Near-Term Case

### Boson Sampling (Aaronson-Arkhipov 2011)

```
SETUP: n photons through m-mode linear interferometer (beamsplitters, phase shifters)
TASK: Sample from the output photon distribution
CLASSICAL HARDNESS: Computing permanent of an n×n matrix is #P-hard
  P(s₁,...,sₙ) ∝ |Perm(U_S)|²  where U_S is submatrix of unitary U

COMPLEXITY CLAIM:
  If a classical computer could efficiently sample from boson sampling distribution,
  the polynomial hierarchy collapses to the third level (very unlikely)
  → Boson sampling is plausibly classically hard under standard complexity assumptions

LIMITATIONS:
  - Not a useful computation — sampling from permanent distribution
  - Noise makes the output distinguishable from ideal distribution
  - With enough noise, classical simulation becomes easier (noisy circuits lose hardness)
```

### Gaussian Boson Sampling (Xanadu)

```
EXTENSION: Use Gaussian states (squeezed light) instead of single photons
ADVANTAGE: Easier to implement experimentally
ADVANTAGE: Connected to graph theory (computing hafnian of adjacency matrix)

XANADU BOREALIS (2022):
  216 squeezed modes (photonic qumodes)
  Claimed: sampling in 36 μs vs 9,000 years classical simulation
  This is Xanadu's "quantum advantage" claim

COUNTER-ARGUMENTS:
  Liu et al. (2023): improved classical sampling algorithms close the gap
  Seasonal pattern: each "quantum advantage" claim is narrowed over time by
  better classical algorithms (tensor networks, improved permanents computation)

CURRENT STATUS: GBS may retain some computational advantage for specific
  graph problems, but advantage shrinks as classical algorithms improve
```

---

## Legitimate Quantum-Classical Hybrid ML

### VQE Energies as ML Features

```
LEGITIMATE USE CASE:
  VQE computes ground-state energies of molecules (quantum advantage expected
  for fault-tolerant hardware with ~50-100 strongly correlated electrons)

  These energies become FEATURES in classical ML pipeline:
  ┌──────────────────────────────────────────────────────┐
  │  Molecular structures → VQE energy per conformer     │
  │       ↓                                              │
  │  Classical ML: predict binding affinity, reactivity, │
  │  toxicity from VQE-derived quantum features          │
  └──────────────────────────────────────────────────────┘

  No quantum speedup for the ML part — classical SGD, random forests, etc.
  Quantum provides BETTER INPUT FEATURES (more accurate energy surfaces)
  This is a hybrid pipeline, not "quantum ML"
```

### Quantum Annealing for Combinatorial Subproblems (D-Wave)

**Clarification:** D-Wave is not ML and not gate-based quantum computing. It appears here because QML literature often cites QUBO formulations of ML training problems (sparse feature selection, binary neural network weight optimization) as a quantum ML application. The only ML connection is that some ML training objectives can be cast as combinatorial optimization. For D-Wave's role in the broader NISQ landscape, see 07-NISQ-APPLICATIONS.

```
D-WAVE ARCHITECTURE:
  2000+ flux qubits (analog, not gate-based)
  Implements Ising model: H = Σᵢ hᵢσᵢᶻ + Σ_{ij} Jᵢⱼσᵢᶻσⱼᶻ
  Quantum annealing: start in superposition, slowly evolve to ground state

  Physical Hamiltonian: H(t) = -A(t)·Σᵢ σᵢˣ + B(t)·H_Ising
  A(t) → 0, B(t) → 1  (anneal from quantum to classical)

MAPPING TO QUBO (Quadratic Unconstrained Binary Optimization):
  Many combinatorial problems map to QUBO: min xᵀQx, x ∈ {0,1}ⁿ
  Portfolio optimization, vehicle routing, job scheduling, MaxCut

HONEST ASSESSMENT:
  No proven quantum speedup over classical simulated annealing/SA
  For dense connectivity, requires embedding (D-Wave is sparse Chimera/Pegasus)
  Embedding overhead: 1 logical variable → 10-30 physical qubits
  Classical SA or branch-and-bound often wins in practice

  WHERE IT SOMETIMES WORKS: problems with natural sparse Ising structure,
  short anneal times as a warm-start for classical refinement
```

---

## QML Claim Evaluation Table

```
┌────────────────────────────────────────────────────────────────────────┐
│ CLAIM                        │ STATUS    │ WHY                         │
├──────────────────────────────┼───────────┼─────────────────────────────┤
│ HHL gives exponential        │ ILLUSORY  │ State prep + readout kill   │
│ speedup for classical linear │           │ the speedup for classical   │
│ algebra                      │           │ data; QRAM required         │
├──────────────────────────────┼───────────┼─────────────────────────────┤
│ Quantum kernels beat         │ NO        │ Dequantization (Tang-style) │
│ classical SVM on real data   │ EVIDENCE  │ often matches; no benchmark │
│                              │           │ showing real advantage      │
├──────────────────────────────┼───────────┼─────────────────────────────┤
│ QNNs outperform classical    │ NO        │ Barren plateaus; training   │
│ NNs for image/NLP            │ EVIDENCE  │ harder; no GPU equivalent   │
├──────────────────────────────┼───────────┼─────────────────────────────┤
│ Quantum speedup for          │ DEBUNKED  │ Grover: √N iterations —     │
│ database search (practical)  │ AS USEFUL │ need quantum RAM, advantage │
│                              │           │ much smaller than expected  │
├──────────────────────────────┼───────────┼─────────────────────────────┤
│ Boson sampling /             │ PLAUSIBLE │ Theoretically hard to       │
│ GBS advantage                │ BUT       │ simulate classically;       │
│                              │ DISPUTED  │ classical algorithms improve │
├──────────────────────────────┼───────────┼─────────────────────────────┤
│ VQE → better molecular       │ SOLID for │ FeMoco etc. genuinely hard  │
│ energies than classical      │ fault-    │ classically; NISQ VQE not   │
│ quantum chemistry            │ tolerant  │ yet better than CCSD(T)     │
├──────────────────────────────┼───────────┼─────────────────────────────┤
│ Quantum ML for quantum       │ SOLID     │ Learning from quantum       │
│ data (quantum system output) │           │ measurements / quantum      │
│                              │           │ sensors — natural use case  │
└──────────────────────────────┴───────────┴─────────────────────────────┘
```

---

## QRAM — The Elephant in the Room

Many QML speedup claims implicitly require QRAM:

```
QRAM (Quantum Random Access Memory):
  Classical:  RAM[i] → x_i  (read n-bit integer, linear time)
  QRAM:       Σ aᵢ|i⟩ → Σ aᵢ|i⟩|x_i⟩  (superposition read)

REQUIREMENT: Query QRAM in superposition to achieve quantum speedups
  for data loading (state preparation)

PROBLEM:
  Building QRAM requires n qubits and poly(n) coherent operations
  QRAM itself is a complex quantum circuit — error rates accumulate
  Each read touches O(n) quantum gates → decoherence
  No physical QRAM has been built at useful scale

IMPACT:
  Without QRAM: quantum speedups for classical data loading don't exist
  Many complexity-theoretic QML speedup results assume QRAM — implicitly
  stripping QRAM from the assumption invalidates the speedup claim
```

---

## When to Take QML Seriously

```
TAKE SERIOUSLY IF:
  1. The data is quantum in origin
     (quantum sensor output, quantum simulation result, quantum channel learning)
  2. The algorithm doesn't require QRAM (or explicitly addresses state prep)
  3. The paper compares to BEST classical baseline, not strawman
  4. The speedup survives dequantization (Tang-style classical algorithm checks)
  5. The resource estimates include fault tolerance overhead

BE SKEPTICAL IF:
  1. "Exponential speedup for classical ML tasks" — state prep bottleneck
  2. "Quantum speedup for gradient descent" — no demonstrated advantage
  3. "Our quantum circuit is a better neural network" — barren plateaus
  4. Uses HHL as a subroutine for practical ML
  5. Benchmark is against naive classical (not best-in-class classical)
  6. Claims advantage on NISQ hardware (error mitigation overhead ignored)
```

---

## Decision Cheat Sheet

```
┌──────────────────────────────────────────────────────────────────────┐
│ SCENARIO                      │ RECOMMENDATION                       │
├───────────────────────────────┼─────────────────────────────────────┤
│ Classical ML on classical data│ Use classical ML (torch, sklearn,   │
│                               │ XGBoost) — no quantum advantage     │
├───────────────────────────────┼─────────────────────────────────────┤
│ Molecular property prediction │ Classical ML on DFT features NOW;   │
│ (drug discovery, materials)   │ Plan for VQE features when fault-   │
│                               │ tolerant hardware available         │
├───────────────────────────────┼─────────────────────────────────────┤
│ Combinatorial optimization    │ Classical SA / genetic algorithms;  │
│ (logistics, scheduling)       │ try D-Wave for sparse QUBO as       │
│                               │ warm-start heuristic only           │
├───────────────────────────────┼─────────────────────────────────────┤
│ Kernel SVM with quantum       │ Research only; compare rigorously   │
│ feature map                   │ with classical RBF/polynomial kernel │
├───────────────────────────────┼─────────────────────────────────────┤
│ "QML for LLMs / vision"       │ No — no evidence, no mechanism for  │
│                               │ advantage; classical GPUs win       │
├───────────────────────────────┼─────────────────────────────────────┤
│ Learning from quantum data    │ Yes — natural and potentially       │
│ (quantum sensors, quantum     │ advantageous; PennyLane useful here │
│ system characterization)      │                                     │
└──────────────────────────────┴──────────────────────────────────────┘
```

---

## Common Confusion Points

**"Quantum ML" usually means classical ML on a quantum computer, not learning about quantum systems.** The latter (learning from quantum data) is where there might be genuine advantage. The former has no demonstrated advantage and significant theoretical obstacles.

**The exponential speedup in HHL is real — the speedup for practical ML is not.** HHL's O(log n) scaling is a genuine result. The problem is the interface: loading classical data into quantum states costs O(n), and reading quantum states back costs O(n). The algorithm is exponentially fast but the I/O is not.

**Dequantization (Tang 2018) is not a refutation of all quantum ML.** Tang showed that certain quantum-inspired classical algorithms can sample from the same distributions as HHL-based recommendations, removing the exponential speedup. This applies to some specific algorithms. It doesn't apply to quantum kernel methods with hard-to-simulate feature maps, or to quantum simulation.

**Quantum kernels are not equivalent to quantum advantage.** Having a quantum circuit that defines a kernel is easy. Having a kernel that (a) is classically hard to compute, (b) provides a statistical advantage on real data, and (c) survives classical dequantization is extremely difficult. Papers often show the first without the latter two.

**Barren plateaus make QNN training hard at scale — not just slow.** The gradient vanishes exponentially with system size. This means the number of shots needed to estimate the gradient with fixed signal-to-noise grows exponentially. This is a fundamental problem, not a hardware limitation that better devices will fix.

**Quantum annealing is not gate-based quantum computing.** D-Wave uses analog quantum annealing — evolving a physical Hamiltonian. Gate-based quantum computers (IBM, Google, IonQ) implement digital quantum circuits. These are fundamentally different paradigms with different strengths, hardware, and error models.
