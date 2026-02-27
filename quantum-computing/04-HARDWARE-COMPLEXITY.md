# Quantum Hardware, Complexity & Path to Fault Tolerance

## The Big Picture

```
+------------------------------------------------------------------+
|         FROM PHYSICS TO COMPUTATION: QC STACK                    |
+------------------------------------------------------------------+
|                                                                    |
|  PHYSICAL LAYER         CONTROL LAYER         LOGICAL LAYER       |
|  ──────────────         ─────────────         ─────────────       |
|  Transmon qubit         Microwave pulses       Logical qubits      |
|  Trapped ion            RF/laser control       Error correction    |
|  Photon                 FPGA classical         Clifford + T gates  |
|  Neutral atom           signal proc.           Algorithms          |
|                                                                    |
|  DiVincenzo criteria    Calibration +          Surface code        |
|  Coherence times        optimal control        MWPM decoder        |
|  Gate fidelity          pulse shaping          Magic state distil. |
|                                                                    |
|  COMPLEXITY LAYER                                                  |
|  ──────────────────────────────────────────────────────────────   |
|  BPP ⊆ BQP ⊆ QMA ⊆ PP ⊆ PSPACE                                  |
|  Factoring ∈ BQP (Shor) — the key result                         |
|  NP vs BQP: open; believed incomparable                           |
+------------------------------------------------------------------+
```

---

## DiVincenzo Criteria (2000)

The checklist for any physical QC implementation:

```
FIVE CRITERIA FOR COMPUTATION:

1. SCALABLE QUBIT REPRESENTATION
   Well-defined, distinct, controllable 2-level quantum systems.
   Must scale to 10³–10⁶+ qubits for useful computation.
   Challenge: fabrication uniformity, crosstalk, classical control scaling.

2. ABILITY TO INITIALIZE
   Reset each qubit to |0⟩ reliably before computation.
   Superconducting: wait for T₁ decay (10–100× T₁) or active reset via measurement.
   Trapped ion: optical pumping to ground state.
   Required fidelity: >99.9% for fault tolerance.

3. COHERENCE TIMES ≫ GATE TIMES
   Ratio T₂ / T_gate determines "useful circuit depth."
   Superconducting: T₂~100μs, T_gate~100ns → ~1000 gates before decoherence.
   Trapped ion: T₂~10s, T_gate~100μs → ~100,000 gates.
   (Trapped ions slower clock, but longer coherence.)

4. UNIVERSAL GATE SET
   Implement {CNOT, H, T} or equivalent with high fidelity.
   1Q gates: > 99.9% fidelity achievable today.
   2Q gates: > 99.5% best labs; > 99.9% required for practical QEC.

5. QUBIT-SPECIFIC MEASUREMENT
   Read out each qubit efficiently (high fidelity, fast).
   Superconducting: dispersive readout ~1μs, ~99% fidelity.
   Trapped ion: fluorescence detection ~1ms, ~99.9% fidelity.

TWO ADDITIONAL FOR QUANTUM NETWORKS:
6. Interconvert stationary ↔ flying qubits (quantum transducer)
7. Faithfully transmit flying qubits between locations
```

---

## Platform Deep Dives

### Superconducting Qubits (IBM, Google)

```
PHYSICS:
  Josephson junction: nonlinear inductor from two superconductors
  separated by thin insulator. Cooper pairs tunnel through.
  Creates nonlinear LC oscillator → anharmonic energy levels.
  |0⟩ and |1⟩ = ground and first excited state of transmon.

  Transmon: Josephson junction + shunting capacitor (reduces charge noise)
  Frequency: 4–8 GHz  (microwave control)
  Operating temperature: 10–20 mK (dilution refrigerator)

OPERATIONS:
  Single-qubit gates: microwave pulses (50–200 ns)
  Two-qubit gate (CZ/CNOT): tunable coupling or cross-resonance (~200-500 ns)
  Measurement: dispersive readout via microwave resonator (~1 μs)

STRENGTHS:
  Fast gates (100s of ns → high clock rate)
  Scalable fabrication (semiconductor fab processes)
  Well-understood physics
  IBM and Google leading this platform

WEAKNESSES:
  T₂ limited (~100 μs, improving but constrained by substrate noise)
  Nearest-neighbor connectivity (grid topology) → SWAP overhead
  Cryogenic infrastructure expensive and bulky
  No two identical chips (fabrication variation)

KEY METRICS (IBM Heron, 2023):
  Qubits: 133
  T₁: ~300 μs, T₂: ~200 μs
  CX gate error: ~0.2% (EPLG: ~0.14%)
  Readout fidelity: ~99%
  Quantum volume: 512 (2022 Falcon)
```

### Trapped Ion Qubits (IonQ, Quantinuum)

```
PHYSICS:
  Single ions (⁴⁰Ca⁺, ¹⁷¹Yb⁺) suspended in Paul (RF) trap.
  Qubit: hyperfine levels of ground state (spin states)
  or optical qubit (ground ↔ long-lived excited state).
  Immense T₁, T₂: minutes to hours (no substrate noise).

OPERATIONS:
  Single-qubit gates: laser pulses (~1 μs)
  Two-qubit gate (Mølmer-Sørensen, Cirac-Zoller): laser-mediated
    via shared motional mode of trapped ion chain (~100 μs–1 ms)
  Measurement: fluorescence photon counting (~1 ms)

STRENGTHS:
  Highest gate fidelities (~99.9% 2Q), record-holder
  All-to-all connectivity (any pair of ions can interact)
  Long coherence times (hours)
  Homogeneous (all ions identical)

WEAKNESSES:
  Slow clock rate (ms gates vs ns for SC)
  Scaling beyond ~100 ions per trap challenging
  Modular architecture required for large systems
  Laser control system complex and expensive

KEY METRICS (Quantinuum H2, 2024):
  Qubits: 56
  T₂: >10 s (spin echo)
  2Q gate fidelity: 99.9%
  JAQCD score: best in industry
  Circuit depth: can run much deeper than SC
```

### Neutral Atom Qubits (QuEra, Pasqal)

```
PHYSICS:
  Neutral Rb or Cs atoms trapped in optical tweezer arrays.
  Qubit: hyperfine ground state.
  Gates use Rydberg state excitation (n~60 principal quantum number):
    Rydberg atoms have huge van der Waals interaction → blockade
    "Rydberg blockade": two atoms within ~10 μm can't both be Rydberg excited
    → natural conditional gate

OPERATIONS:
  Single-qubit gates: microwave or Raman laser (~1 μs)
  Two-qubit (CZ via Rydberg blockade): ~1 μs (fast!)
  Reconfigurable: physically move atom arrays mid-circuit
  Measurement: fluorescence imaging

STRENGTHS:
  Reconfigurable connectivity (move atoms between shots)
  High coherence (~seconds)
  Large arrays (100s–1000s of atoms demonstrated)
  Analog simulation mode (Hamiltonian simulation)

WEAKNESSES:
  ~1% loss per site per shot (vacuum)
  Gate fidelities lagging SC/ion trap (~99.5%)
  Still maturing as gate-based platform

KEY MILESTONE (QuEra 2023, Nature):
  48 logical qubits, fault-tolerant circuits, 99.5% logical gate fidelity
  First demonstration of logical qubit advantage over physical qubits
```

### Photonic (PsiQuantum, Xanadu)

```
PHYSICS:
  Quantum information in photon states (polarization, path, squeezed light).
  Linear optical QC (KLM protocol 2001): CNOT gates with photons, ancilla, detection.
  Measurement-based QC: generate resource state (cluster/graph state), measure.

STRENGTHS:
  Room temperature operation
  Fiber/integrated optic integration
  Photons naturally mobile (quantum networking)

WEAKNESSES:
  Photon loss is primary error
  Deterministic 2-photon gates hard (need ancilla + postselection)
  Large overhead for fault tolerance vs qubit platforms

XANADU (GBS — Gaussian Boson Sampling):
  Special-purpose sampling device, not universal gate-based.
  Claimed quantum advantage for molecular vibronic spectra simulation.
```

### Topological (Microsoft Majorana)

```
GOAL: Use non-Abelian anyons (Majorana zero modes) as inherently
      fault-tolerant qubits.

THEORY:
  Majorana fermions: particle = antiparticle.
  In topological superconductors, zero-energy Majorana modes emerge
  at boundaries. Qubit is encoded in pair of Majorana modes (nonlocal).
  Errors must physically move Majorana modes around each other to
  affect qubit state → topological protection.

STATUS (2025):
  2018: Initial Majorana evidence paper (Delft/Microsoft) — later retracted (2021)
        due to data handling concerns. Significant credibility damage.
  2023: New paper (Nature) reporting Majorana signatures in InAs-Al
        heterostructures using improved measurement protocols.
        Distinct from retracted work — different device, different team leadership.
  2025: Microsoft announced "topological qubit" milestone (February 2025),
        claiming first demonstration of a topological qubit based on
        Majorana zero modes in an InAs-Al nanowire device.
  Key distinction: evidence for topological gap signatures ≠ operational qubit.
  No quantum gate operations or error correction demonstrated on topological qubits.
  The field remains cautious given the 2018 retraction history.

POTENTIAL ADVANTAGE:
  Physical error rate could be ~1% (vs 0.1% for SC) to reach threshold.
  Fewer physical qubits needed per logical qubit.
  T gates may be implementable via anyon braiding (cheaper distillation).
```

---

## Qubit Quality Metrics

```
METRIC            DEFINITION                           WHY IT MATTERS
──────────────    ──────────────────────────────────   ──────────────────────────
T₁ (ms)           Energy relaxation time               |1⟩ → |0⟩ spontaneous decay
T₂ (ms)           Phase coherence time (T₂ ≤ 2T₁)     Random phase kicks
Gate fidelity     Avg P(correct) over unitaries         Directly bounds error rate
SPAM error        State prep + measurement error        Initialization + readout
Quantum Volume    Max n: n×n circuit passes 2/3         IBM's holistic single number
                  heavy output test
EPLG              Error per layered gate                Benchmarks deep circuits
                  (layer = all gates in parallel)
Circuit layer ops Max gates before decoherence kills    Depth × width trade-off
```

---

## Complexity Theory Deep Dive

### Key Classes

| Class | Definition | Complete problem |
|-------|-----------|-----------------|
| **P** | Poly-time deterministic | Sorting, LP, primality testing |
| **BPP** | Poly-time randomized (2/3 success) | Miller-Rabin? (believed = P) |
| **BQP** | Poly-time quantum (2/3 success) | Factoring (Shor) |
| **QMA** | Quantum-verifiable NP analog | k-local Hamiltonian (k≥2) |
| **PP** | Majority vote quantum | Permanent (counting #P-hard) |
| **PSPACE** | Poly-space | QBF, Quantified Boolean Formula |
| **QIP** | Quantum interactive proofs | QIP = PSPACE (Jain et al. 2009) |

### Critical Separations and Open Questions

```
KNOWN:
  P ⊆ BPP ⊆ BQP ⊆ QMA ⊆ PP ⊆ PSPACE
  P ⊂ PSPACE (strict separation, TQSAT ∉ P)
  BQP ⊄ NP  (BQP can solve sampling problems NP can't verify)
  Factoring ∈ BQP ∩ NP (NOT known NP-complete)

OPEN:
  P vs BPP  (believed equal; derandomization)
  P vs BQP  (believed BQP ⊋ P but unproven)
  BQP vs NP  (likely incomparable but unproven)
  BQP vs PSPACE  (BQP ⊂ PSPACE but strict?)
  NP vs QMA  (NP ⊆ QMA trivially; proper subset?)

KEY IMPLICATION:
  If BQP ⊇ NP, polynomial hierarchy collapses.
  This is considered very unlikely.
  Quantum computers probably can't solve NP-complete problems in poly time.
```

### Oracle Separations

```
Relative to oracles:
  ∃ oracle A: P^A ≠ BPP^A (oracles can separate)
  ∃ oracle A: BQP^A ⊄ PH^A (Raz-Tal 2019 — strongest known structural result)
    → Relative to an oracle, BQP contains problems outside the ENTIRE
      polynomial hierarchy. This is an unconditional oracle separation —
      no unproven complexity assumptions needed (unlike P vs NP barriers).
    → Caveat: oracle separations don't directly imply non-relativizing
      separations. BGS (1975) showed oracles can't resolve P vs NP.
      Raz-Tal is evidence for BQP ⊄ PH, not a proof.

  Forrelation problem (Aaronson-Ambainis):
    BQP query complexity: 1
    Randomized query complexity: Ω(√N/log N)
    → concrete separation BQP vs BPP in query model
```

---

## Hardware Roadmaps

### IBM Quantum Roadmap

```
2021: Eagle (127 qubits)
2022: Osprey (433 qubits), Heron architecture announced
2023: Heron (133q, heavy-hex, EPLG 0.14%)
      Condor (1121 qubits, exploratory)
2024: Flamingo + modular systems
2025: 2000 qubit target
2029: 200,000 qubit target
2033: 100,000 qubit + error correction target

Key innovations:
  Heavy-hex lattice: each qubit has ≤3 neighbors (reduced crosstalk)
  Tunable couplers (Heron): faster gates, lower residual ZZ coupling
  Quantum communication links: connect separate processors
```

### Google Quantum AI

```
2019: Sycamore (54q) — "quantum supremacy" claim
2022: surface code below threshold demonstration (Nature)
2023: Willow (105q) — below threshold, improved RCS performance
2024: Willow milestone: logical error suppressed below physical
      as code distance increases (key theoretical requirement met)

Goal: Error-corrected quantum computer within decade
Key metric: Logical qubit lifetime > physical qubit lifetime ✓ (Willow)
```

---

## Post-Quantum Cryptography

The immediate practical consequence of quantum computing for industry:

```
THREAT MODEL:
  Shor's algorithm breaks: RSA, ECC (all elliptic curve), Diffie-Hellman
  Grover's algorithm weakens: AES (halves effective key length)
  No known quantum speedup for: AES (symmetric), SHA-2/3 (hashing)

HARVEST-NOW-DECRYPT-LATER:
  Adversaries capturing encrypted traffic NOW to decrypt LATER
  when CRQC available. Relevant for: state secrets, health records,
  long-term contracts, anything with >10-year confidentiality.

NIST PQC STANDARDS (2024):
  Algorithm          Type            Based on        FIPS
  ────────────────   ──────────────  ─────────────   ──────
  ML-KEM (Kyber)     KEM            Module-LWE      203
  ML-DSA (Dilithium) Signature      Module-LWE      204
  SLH-DSA (SPHINCS+) Signature      Hash functions  205
  FALCON             Signature (alt) NTRU lattice    206

  LWE (Learning With Errors): believed hard for quantum computers.
  Hash-based: security from collision resistance of hash functions.
  Lattice problems: believed in BQP's complement (hard for QC).

MIGRATION STRATEGY:
  Phase 1 (now): Inventory all cryptographic usage
  Phase 2 (2025-2027): Hybrid deployment (classical + PQC)
  Phase 3 (2027-2030): Full PQC deployment
  Priority: TLS certificates, VPN, code signing, long-lived secrets

TLS 1.3 + PQC:
  X25519Kyber768 (hybrid): deployed by Cloudflare, Google, Chrome since 2023
  FIPS 203 implementations shipping in 2025
```

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| Best platform for gate fidelity? | Trapped ion (~99.9% 2Q); superconducting improving |
| Best platform for qubit count? | Superconducting (IBM, Google) — 100s–1000s |
| Which platform will win? | Unknown; likely problem-dependent or hybrid |
| Is D-Wave a fault-tolerant QC? | No — quantum annealer, specialized, no proven quantum speedup |
| When do quantum computers break RSA? | Most experts: 2035–2040+ minimum; 10M+ physical qubits needed |
| Should I implement PQC now? | Yes — harvest-now-decrypt-later attacks are active today |
| What's NIST's post-quantum standard? | ML-KEM (FIPS 203), ML-DSA (FIPS 204), SLH-DSA (FIPS 205) |
| What complexity class is factoring in? | BQP ∩ NP; NOT known NP-complete |
| Can QC solve NP-complete problems? | No known polynomial time algorithm; Grover gives √N |

---

## Common Confusion Points

**"More qubits = better quantum computer"** — false. 1000 low-fidelity
qubits is worse than 100 high-fidelity qubits for most tasks. Quantum
volume, EPLG, and circuit depth matter more than raw qubit count.

**"Quantum computers only need to beat classical once"** — quantum
advantage must be demonstrated for *practically useful* problems, not
contrived benchmarks. Google's RCS demo used a circuit designed to be
hard to simulate classically but useless for computation.

**"Microsoft's topological qubits exist"** — as of 2025, no operational
topological qubit has been demonstrated. The 2023 paper showed evidence
of Majorana-like signatures, not operational qubits. The 2022 paper
was retracted.

**"BQP ⊃ NP would solve P vs NP"** — would imply NP ⊆ BQP ⊆ PP and
the polynomial hierarchy would collapse, but wouldn't directly resolve P vs NP.
The containment P ⊆ BQP is proven; P ⊊ BQP is unproven.

**"Quantum computers operate at room temperature"** — only photonic
and neutral atom platforms. Superconducting qubits (currently leading)
require dilution refrigerators at ~10 mK — colder than outer space.
This is a major engineering and cost barrier for scaling.
