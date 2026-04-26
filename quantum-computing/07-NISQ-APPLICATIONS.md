# NISQ — Near-Term Quantum Devices

## Big Picture: The NISQ Landscape

```
┌─────────────────────────────────────────────────────────────────────┐
│                     NISQ ERA (2019 – ~2030?)                        │
│                                                                     │
│  PHYSICAL REALITY:                                                  │
│  ┌─────────────────────────────────────────────────────────────┐    │
│  │  ~50 – 1,000 physical qubits                                │   │
│  │  No full quantum error correction                           │   │
│  │  2-qubit gate error: 0.1% – 1%                              │   │
│  │  T₁ coherence: 50 – 500 μs (superconducting)               │   │
│  │  T₂ dephasing: 20 – 200 μs                                  │   │
│  │  Gate time (2-qubit): 50 – 500 ns                           │   │
│  │  → Circuit depth limit: ~100-1000 gates before noise wins   │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                                                                     │
│  RESPONSE:                                                          │
│  Error MITIGATION (not correction): post-process to reduce noise   │
│  effect without overhead of full QEC (thousands of physical/logical) │
│                                                                     │
│  HARDWARE                ERROR           BENCHMARKING              │
│  CHARACTERIZATION    MITIGATION          & CLAIMS                  │
│  (know your device)  (ZNE, PEC, CDR)    (honest assessment)        │
└─────────────────────────────────────────────────────────────────────┘
```

---

## NISQ Constraints in Detail

### Qubit Lifetime vs Circuit Depth

```
SUPERCONDUCTING QUBITS (IBM, Google):
  T₁ (amplitude damping):  50 – 500 μs
  T₂ (dephasing):          20 – 300 μs  (always ≤ 2T₁)
  1-qubit gate time:        ~20 ns
  2-qubit gate time (CX):  ~200 – 500 ns
  Readout time:            ~1 μs

  Practical circuit depth:  T₂ / t_gate_2q ~ 200 μs / 300 ns ~ 600 gates
  With connectivity constraints (routing overhead): ~100-300 effective 2-qubit gates

ION TRAPS (IonQ, Quantinuum):
  T₁, T₂:   seconds to minutes (much longer)
  Gate times: ~10 μs – 1 ms (much slower)
  All-to-all connectivity (no routing overhead)
  2-qubit gate fidelity: 99.5% – 99.9% (better than superconducting)
  But: current scale < 50 qubits; slower clock speed

COMPARISON:
  Superconducting: fast gates, short coherence, limited connectivity, many qubits
  Ion trap:        slow gates, long coherence, full connectivity, fewer qubits
  Photonic:        room temp, no coherence limit, hard to do 2-qubit gates
```

### Noise Channels

```
DEPOLARIZING NOISE (most common model):
  ρ → (1-p)ρ + p/3(XρX + YρY + ZρZ)
  Effect: random Pauli error with probability p
  Symmetric: erases quantum info equally in all directions

DEPHASING (Z-noise, T₂ process):
  ρ → (1-p)ρ + p·ZρZ
  Effect: destroys off-diagonal elements (superposition → mixed)
  Caused by: charge noise, magnetic field fluctuations
  Most common in practice

AMPLITUDE DAMPING (T₁ process):
  |1⟩ → |0⟩ with probability γ = 1 - e^{-t/T₁}
  Effect: qubit spontaneously decays to ground state
  Kraus operators: K₀ = [[1,0],[0,√(1-γ)]], K₁ = [[0,√γ],[0,0]]

GATE ERROR MODEL:
  Coherent errors: systematic rotation errors (can be calibrated away)
  Incoherent errors: depolarizing/dephasing during gate (fundamental noise floor)
  Leakage: |2⟩ level population (transmons have finite anharmonicity)
  Crosstalk: neighboring qubits interact during single-qubit operations
```

---

## Noise Characterization Protocols

### Randomized Benchmarking (RB)

```
PROTOCOL:
  1. Apply sequence of m random Clifford gates C₁, C₂, ..., Cₘ
  2. Compute their inverse: Cₘ₊₁ = (Cₘ...C₂C₁)†
  3. Measure return to |0⟩ probability
  4. Repeat for many sequences of length m
  5. Plot mean survival probability vs m:

  p(m) = A · r^m + B

  where r = 1 - 2ε/(1-1/2^n) ≈ 1 - 2ε   (ε = depolarizing error rate)

PROPERTIES:
  + Gate-set-independent (Cliffords form a group → RB is valid)
  + Insensitive to SPAM (state prep and measurement) errors (A, B absorb them)
  + Gives single error-per-Clifford number
  - Clifford gates ≠ native gates (requires decomposition)
  - Average fidelity, not gate-specific fidelity
  - Doesn't diagnose which gates are bad

INTERLEAVED RB: insert target gate between random Cliffords → isolate one gate's error
```

### Cross-Entropy Benchmarking (XEB)

```
PROTOCOL (Google's approach for Sycamore):
  1. Apply random circuit U of depth d
  2. Measure output bitstring s
  3. Compute ideal probability p_U(s) = |⟨s|U|0⟩|²  (classical simulation)
  4. XEB fidelity: F_XEB = 2^n · E[p_U(s)] - 1

  Ideal (noiseless): E[p_U(s)] = 2/2^n  (Porter-Thomas distribution)  → F = 1
  Completely noisy:  outputs uniform → E[p_U(s)] = 1/2^n              → F = 0

USED IN: Google's "quantum supremacy" claim (Sycamore, 2019)
ISSUE: Classical algorithms (tensor networks) have since improved significantly
       — see benchmarking claims section below
```

---

## Error Mitigation (Not Correction)

**Note:** This section is the authoritative treatment of error mitigation techniques. 05-VARIATIONAL-ALGORITHMS covers the optimizer-side interaction (how mitigation affects VQA convergence). 08-QUANTUM-SOFTWARE covers framework-level APIs (PennyLane transforms, Qiskit primitives). The theory and tradeoffs live here.

### Zero-Noise Extrapolation (ZNE)

```
IDEA: Run circuit at multiple noise levels λ₁ < λ₂ < λ₃, extrapolate to λ → 0

NOISE AMPLIFICATION:
  Gate folding: replace gate G with G·G†·G (same unitary, 3× noise)
  Pulse stretching: stretch pulse duration → more decoherence

EXTRAPOLATION:
  Linear:   f(λ) = a + bλ  → f(0) = a
  Richardson (polynomial order k):
    f_mitigated = Σᵢ cᵢ f(λᵢ)
    where cᵢ satisfy Σ cᵢ = 1, Σ cᵢ λᵢ^j = 0 for j = 1,...,k
  Exponential: f(λ) = a + b·e^{cλ}

ERROR:
  Systematic: extrapolation assumes noise model is correct
  Statistical: more noise → more variance per shot → more shots needed
  Diverges: exponentially noisy circuits cannot be mitigated linearly (cost too high)
```

### Probabilistic Error Cancellation (PEC)

```
IDEA: Express noisy gate G as quasi-probability sum of implementable operations

G_ideal = Σᵢ qᵢ Oᵢ    where Σᵢ |qᵢ| = γ ≥ 1, Oᵢ are noisy operations

SAMPLING:
  Sample operation Oᵢ with prob |qᵢ|/γ, record sign sgn(qᵢ)
  Run circuit with this operation, multiply result by γ·sgn(qᵢ)
  Average over many samples → unbiased estimate of ideal expectation

COST:
  Sampling overhead: γ^(2d) shots for depth-d circuit
  γ ≥ 1 + 2ε per gate (ε = error rate)
  Total overhead: e^(4εd) → exponential in circuit depth × error rate

  For 100 gates at 0.1% error: e^(0.4) ≈ 1.5× — manageable
  For 1000 gates at 0.5% error: e^(20) ≈ 5×10⁸ — impossible

→ PEC is only practical for short circuits with low error rates
```

### Clifford Data Regression (CDR)

```
IDEA: Train classical noise model using circuits near target that can be simulated

1. Take target circuit C
2. Replace some non-Clifford gates with Clifford gates → "training circuit" Cₜ
   (Clifford circuits are classically simulable via Gottesman-Knill)
3. Run Cₜ on quantum hardware AND classical simulator
4. Fit regression: y_ideal = f(y_noisy) from training data
5. Apply learned correction to target C's noisy output

ADVANTAGE: Learns empirical noise model from data — works even for complex correlated noise
LIMITATION: Regression assumes noise for Clifford near-circuits ≈ noise for target circuit
```

### Measurement Error Mitigation (Readout Calibration)

```
SIMPLEST MITIGATION: Correct for imperfect readout

CALIBRATION:
  Prepare |0⟩⊗ⁿ, measure → calibration matrix A[i,j] = P(measure i | prepared j)

CORRECTION:
  p_measured = A · p_ideal  →  p_ideal = A⁻¹ · p_measured

ISSUES:
  n qubits → 2^n × 2^n matrix A — exponentially large for full characterization
  Practical fix: assume local measurement errors (diagonal A in the tensor product sense)
  M3 method: matrix-free inversion using iterative methods

ALWAYS DO THIS: readout errors are the easiest to mitigate and often significant (1-5%)
```

---

## Benchmarking Quantum Advantage Claims

### Google Sycamore (2019)

```
CLAIM: Random circuit sampling on 53-qubit Sycamore in 200 seconds
       "would take 10,000 years on Summit" (IBM's best supercomputer)

COUNTER-ARGUMENTS:
  IBM (same week): with more clever simulation + disk storage → 2.5 days, not 10,000 years
  Villalonga et al. (2022): claimed ~300 seconds on classical hardware
  Pan, Chen, Zhang (2022): using tensor network contraction, completed in 300 seconds
                            on classical cluster at comparable cost

CURRENT HONEST ASSESSMENT:
  - Sycamore's specific task: sampling from XEB distribution
  - This is NOT a useful computation — it's a benchmark of the benchmark
  - Classical simulation has steadily improved; advantage has shrunk
  - Task was specifically designed to be hard to simulate classically
  - Not a general quantum speedup demonstration

WHAT SYCAMORE DID DEMONSTRATE:
  - 53 high-quality qubits with low enough noise to produce coherent quantum states
  - XEB fidelity consistent with known 2-qubit gate error rates
  - World-class control system
  - Legitimate engineering achievement
```

### IBM Heavy-Hex Architecture

```
HEAVY-HEX TOPOLOGY:
  Reduces crosstalk by limiting qubit connectivity (max degree 3)
  Enables higher gate fidelities through decreased ZZ coupling
  Trade-off: requires more SWAP gates for non-native connectivity
             → deeper circuits for algorithms needing long-range interactions

  ●─●─●─●─●
  │   │   │
  ●   ●   ●      Heavy-hex unit cell
  │   │   │
  ●─●─●─●─●

IBM Eagle: 127 qubits (2021)
IBM Osprey: 433 qubits (2022)
IBM Condor: 1,127 qubits (2023)
IBM Heron: 133 qubits, improved error rates (2023, focus on fidelity over count)
```

---

## NISQ Application Landscape — Honest Assessment

```
┌───────────────────────────────────────────────────────────────────────┐
│ APPLICATION           │ NISQ STATUS  │ REALISTIC TIMELINE             │
├───────────────────────┼──────────────┼───────────────────────────────┤
│ VQE for small         │ Demonstrated │ NOW — but classical (CCSD(T)) │
│ molecules (H₂, LiH)  │ proof-of-    │ beats NISQ VQE on accuracy   │
│                       │ concept      │ Fault-tolerant needed for     │
│                       │              │ genuine speedup (n~100 e⁻)   │
├───────────────────────┼──────────────┼───────────────────────────────┤
│ QAOA for              │ Demonstrated │ No proven advantage over      │
│ combinatorial opt.    │ at small n   │ simulated annealing / GW SDP  │
│ (MaxCut, TSP)         │              │ Needs much deeper circuits    │
├───────────────────────┼──────────────┼───────────────────────────────┤
│ Quantum ML            │ Active       │ No advantage demonstrated;    │
│ (kernels, QNNs)       │ research     │ highly speculative (see 09)   │
├───────────────────────┼──────────────┼───────────────────────────────┤
│ Quantum simulation    │ Best NISQ    │ Small systems now; 50-100     │
│ (condensed matter,    │ use case     │ qubit simulation might be     │
│ Hubbard model)        │              │ classically intractable       │
├───────────────────────┼──────────────┼───────────────────────────────┤
│ Quantum chemistry     │ Limited      │ RSA-2048 needs ~4,000 logical │
│ / Shor's algorithm    │ (too deep    │ qubits, ~4M physical —        │
│                       │ for NISQ)    │ decades away                  │
├───────────────────────┼──────────────┼───────────────────────────────┤
│ Quantum sensing       │ Deployed     │ Already commercially useful   │
│ (atomic clocks, MRI   │ (not same    │ Does not require quantum      │
│ enhancement, gravity) │ as computing)│ computing hardware            │
└───────────────────────┴──────────────┴───────────────────────────────┘
```

### Resource Estimates for Fault-Tolerant Quantum Advantage

```
RSA-2048 FACTORING (Shor's algorithm):
  Logical qubits: ~4,000
  Error correction: surface code, p_physical ≈ 0.1%
  Physical/logical ratio: ~1,000:1 at distance d=21
  Physical qubits required: ~4,000,000
  Runtime: ~8 hours

AES-256 (Grover): √(2^256) = 2^128 operations → negligible speedup in practice
  (NIST quantum-resistant because key length doubles, not because impossible)

QUANTUM CHEMISTRY (FeMoco active space):
  Logical qubits: ~1,000 – 2,000
  Physical qubits: ~1,000,000 – 4,000,000
  Still requires millions of physical qubits → 10-20 year horizon

CURRENT NISQ DEVICES: 50 – 1,127 noisy physical qubits
  Gap to useful fault-tolerant computation: 1,000 – 100,000× more qubits
                                           + 10-100× better gate fidelity
```

---

## NISQ Timeline

```
2019: Google Sycamore "quantum supremacy" (sampling benchmark)
2021: IBM Eagle (127 qubits), error mitigation papers proliferate
2022: IBM Osprey (433 q), Quantinuum H2 (32 ion-trap qubits, 99.9% 2-qubit fidelity)
2023: IBM Condor (1127 q), Heron (133 q, improved fidelity), error-corrected ops demos
2024: IBM roadmap targets 100k+ qubit systems; Google Willow (105 q, below threshold demo)
2025: Early fault-tolerant experiments — logical qubit demos, not yet useful computation

NEAR-TERM (2025-2028): "Early fault-tolerant" — small logical qubit registers,
  transversal gates, limited QEC — no useful factoring/chemistry yet

MEDIUM-TERM (2028-2035): Fault-tolerant systems for limited quantum chemistry,
  cryptanalysis of small RSA key sizes

LONG-TERM (2035+): Full fault-tolerant systems capable of RSA-2048, useful chemistry
```

---

## Decision Cheat Sheet

```
┌──────────────────────────────────────────────────────────────────────┐
│ SCENARIO                      │ RECOMMENDATION                       │
├───────────────────────────────┼─────────────────────────────────────┤
│ Need error mitigation now     │ Always apply readout calibration;   │
│                               │ ZNE for shallow circuits (< 50 gates│
│                               │ PEC for tiny circuits with known ε  │
├───────────────────────────────┼─────────────────────────────────────┤
│ Benchmarking hardware quality │ Randomized benchmarking (RB);       │
│                               │ Interleaved RB for specific gates   │
├───────────────────────────────┼─────────────────────────────────────┤
│ Claim: "NISQ advantage"       │ Ask: compared to BEST classical?    │
│ evaluation                    │ Simulated annealing, CCSD(T), GW?   │
│                               │ Look for classical simulation paper │
├───────────────────────────────┼─────────────────────────────────────┤
│ Near-term compute investment  │ Focus on quantum simulation         │
│                               │ (strongly correlated systems —      │
│                               │ best bet for genuine NISQ value)    │
├───────────────────────────────┼─────────────────────────────────────┤
│ Fault-tolerant planning       │ Resource estimation tools (e.g.,    │
│                               │ Azure Quantum Resource Estimator,   │
│                               │ Q# estimates, Qualtran) before      │
│                               │ committing; plan for millions of    │
│                               │ physical qubits                     │
└──────────────────────────────┴──────────────────────────────────────┘
```

---

## Common Confusion Points

**"Quantum supremacy" ≠ quantum utility.** Google's Sycamore experiment demonstrated that a specific random sampling task ran faster on a quantum device than the best classical simulation available at the time. The task has no practical application and has since been significantly narrowed as classical algorithms improved.

**More qubits ≠ better quantum computer.** IBM's Condor (1,127 qubits) is less computationally useful per qubit than Quantinuum's H2 (32 qubits) because H2 has 99.9% 2-qubit gate fidelity vs ~99.5% for superconducting systems. For fault tolerance, fidelity determines the encoding overhead (physical qubits per logical qubit).

**ZNE does not work for deep circuits.** As circuit depth d grows, the noise-extrapolation overhead grows exponentially (the mitigated estimator variance). For circuits where the noisy output is essentially random, no amount of mitigation recovers the ideal signal.

**T₁ ≠ T₂.** T₁ is the energy relaxation time (|1⟩ → |0⟩). T₂ is the dephasing time (superposition → mixed). Always T₂ ≤ 2T₁. Dephasing is typically the dominant decoherence source and is often set by environmental noise (magnetic, charge) rather than fundamental physics.

**Error mitigation is not free.** PEC requires exponentially more shots. ZNE increases variance. CDR requires running training circuits. The overhead must be included when comparing NISQ results to classical benchmarks — raw runtime comparisons that ignore shot overhead are misleading.

**Physical qubit count to logical qubit count ratio is not fixed.** Surface code overhead depends on physical gate error rate. At ε = 0.1%, you might need ~1,000 physical qubits per logical qubit. At ε = 0.01%, maybe ~100:1. The goal of hardware improvement is reducing this ratio as much as crossing the threshold.
