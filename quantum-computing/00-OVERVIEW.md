# Quantum Computing — Field Map & Orientation

<!-- @editor[bridge/P2]: No bridge from classical noise/channel models to quantum decoherence — learner has deep background in distributed systems reliability and classical error models; connecting T1/T2 to classical SNR and channel capacity concepts would anchor the hardware section. -->

## The Big Picture

Quantum computing exploits superposition, entanglement, and interference to solve structured
problems in ways classical computers cannot. It does not replace classical computing — it
extends computation into a fundamentally different physical regime, enabling algorithms
with no known classical equivalent for specific structured problems.

```
+---------------------------------------------------------------------+
|               QUANTUM COMPUTING LANDSCAPE                           |
+---------------------------------------------------------------------+
|                                                                     |
|  FOUNDATIONS       HARDWARE           ALGORITHMS     APPLICATIONS  |
|  ┌──────────┐     ┌─────────────┐    ┌──────────┐  ┌───────────┐ |
|  │ Circuit  │     │ Supercond.  │    │ Shor's   │  │ Crypto    │ |
|  │ model    │     │ IBM Heron   │    │ Grover's │  │ breaking  │ |
|  │ (gate)   │     │ Google      │    │ QFT/QPE  │  │ RSA/ECC   │ |
|  │          │     │ Willow      │    │ HHL      │  │           │ |
|  │ Adiabatic│     │             │    │ VQE/QAOA │  │ Quantum   │ |
|  │ (anneal) │     │ Trapped ion │    │          │  │ chemistry │ |
|  │          │     │ IonQ,       │    │ Quantum  │  │ (sim)     │ |
|  │Topologic.│     │ Quantinuum  │    │ walks,   │  │           │ |
|  │ Majorana │     │             │    │ QML      │  │ Optimiz.  │ |
|  │ anyons   │     │ Neutral atom│    │ (QSVM)   │  │ heuristic │ |
|  └──────────┘     │ Photonic    │    └──────────┘  └───────────┘ |
|                   │ Spin qubit  │                                  |
|                   └─────────────┘                                  |
|                                                                     |
|  ERROR CORRECTION     COMPLEXITY          NISQ → FTQC ROADMAP     |
|  ┌──────────────┐    ┌────────────────┐  ┌────────────────────┐  |
|  │ Stabilizer   │    │ BQP ⊆ QMA ⊆ PP │  │ 2024: ~1000 phys.  │ |
|  │ codes        │    │ ⊆ PSPACE       │  │ qubits, no QEC     │ |
|  │ Surface code │    │                │  │ 2030+: logical QEC  │ |
|  │ Threshold thm│    │ NP ⊄ BQP      │  │ 2035+: CRQC?       │ |
|  │ T gate cost  │    │ (likely)       │  │                    │  |
|  └──────────────┘    └────────────────┘  └────────────────────┘  |
+---------------------------------------------------------------------+
```

---

## Three Quantum Phenomena That Enable QC

```
SUPERPOSITION                ENTANGLEMENT               INTERFERENCE
─────────────────────────    ─────────────────────────  ────────────────────────
A qubit is a unit vector     Two+ qubits share state    Probability amplitudes
in ℂ²:                       that cannot be factored:   are complex numbers —
                                                        they add and cancel.
  |ψ⟩ = α|0⟩ + β|1⟩         |Φ⁺⟩ = (|00⟩+|11⟩)/√2
                                                        Algorithms are designed
  |α|² + |β|² = 1            Measuring one qubit        to constructively
                              instantly collapses both,  interfere at correct
n qubits span ℂ^(2^n):        regardless of distance.   answers and destructively
2^n amplitudes encoded                                  interfere at wrong ones.
in n physical qubits.         No FTL communication
                              (no-comm theorem holds).  This is why Grover and
Classical: coin mid-flip     Classical: no analog       Shor work.
```

Quantum speedup comes from **interference-based amplitude amplification**, not from
"trying all possibilities simultaneously" (a common but misleading framing).

---

## Computation Models

```
CIRCUIT (GATE) MODEL         ADIABATIC MODEL              TOPOLOGICAL MODEL
────────────────────         ─────────────────────────    ─────────────────────────
Standard model. Initialize   Evolve Hamiltonian slowly    Encode logical qubits in
|0⟩^⊗n, apply unitary gates, from easy H_initial to hard  non-Abelian anyon braids.
measure in computational     H_problem ground state.      Inherently fault-tolerant:
basis.                       Adiabatic theorem: stay in   topology protects against
                             ground state if slow enough. local errors.
Universal gate sets:
  H + T + CNOT               Equivalent to circuit model  Microsoft's Majorana
  R(θ) + CNOT               (Aharonov et al. 2004) but   fermion bet. No commercial
                             finite-T hardware may do     hardware available (2025).
All major hardware:          classical thermal annealing.
IBM, Google, IonQ            D-Wave uses this model.      If realized: threshold
                                                          error rate approaches 1%,
                             Not proven quantum speedup   orders of magnitude better
                             for any practical problem.   than surface codes.
```

---

## Complexity Hierarchy

```
┌───────────────────────────────────────────────────────────────────┐
│  PSPACE  (QIP = PSPACE = IP — quantum interactive proofs)         │
│ ┌───────────────────────────────────────────────────────────┐    │
│ │  PP  (PostBQP = PP — Aaronson 2005)                       │    │
│ │ ┌─────────────────────────────────────────────────────┐   │    │
│ │ │  QMA  (quantum Merlin-Arthur, quantum NP analog)     │   │    │
│ │ │  QMA-complete: k-local Hamiltonian (k≥2)             │   │    │
│ │ │ ┌───────────────────────────────────────────────┐   │   │    │
│ │ │ │  BQP  (efficient quantum computation)          │   │   │    │
│ │ │ │  Contains: factoring, discrete log, HSP       │   │   │    │
│ │ │ │  BQP ⊆ QMA ∩ PP                               │   │   │    │
│ │ │ │ ┌─────────────────────────────────────────┐   │   │   │    │
│ │ │ │ │  BPP  (randomized polynomial time)       │   │   │   │    │
│ │ │ │ │   ┌──────────────────────────────────┐   │   │   │   │    │
│ │ │ │ │   │  P                               │   │   │   │   │    │
│ │ │ │ │   └──────────────────────────────────┘   │   │   │   │    │
│ │ │ │ └─────────────────────────────────────────┘   │   │   │    │
│ │ │ └───────────────────────────────────────────────┘   │   │    │
│ │ └─────────────────────────────────────────────────────┘   │    │
│ └───────────────────────────────────────────────────────────┘    │
└───────────────────────────────────────────────────────────────────┘

NP: unknown relation to BQP — BQP ⊆ NP is FALSE (QC can solve problems
outside NP like sampling problems), NP ⊆ BQP is unproven/unlikely.

Key facts:
  - Factoring ∈ BQP ∩ NP, NOT known NP-complete (hence no speedup for NP-complete)
  - Grover gives O(√N) for unstructured search — NP stays hard under QC
  - If NP ⊆ BQP then PH collapses (extremely unlikely)
```

---

## Hardware Platforms Comparison

| Platform | Leaders | Qubit Type | 2Q Gate Fidelity | Coherence | Connectivity | Ops Temp |
|----------|---------|-----------|-----------------|-----------|--------------|----------|
| Superconducting | IBM (Heron 133q), Google (Willow 105q) | Transmon | 99.5–99.9% | 100μs–1ms | Nearest-neighbor | 10–20 mK |
| Trapped ion | IonQ (Forte 36q), Quantinuum (H2 56q) | Yb⁺, Ba⁺ | 99.9%+ | >10 s | All-to-all | Room temp |
| Neutral atom | QuEra (256q), Atom Computing | Rb, Cs | 99.5% | ~1 s | Reconfigurable | Room temp |
| Photonic | PsiQuantum, Xanadu (GBS) | Photon modes | High (loss issue) | — | Graph states | Room temp |
| Spin qubit | Intel (Tunnel Falls) | Electron spin | 99.5% 1Q | ~ms | 2D arrays | <1 K |
| Topological | Microsoft (Majorana) | Non-Abelian anyon | Target 99.99%+ | Very long | TBD | mK |

**Qubit count is a misleading headline metric.** Key quality metrics:

```
METRIC                DEFINITION                           TARGET FOR CRQC
──────────────────    ──────────────────────────────────   ──────────────────
Gate fidelity (2Q)    P(correct) per 2-qubit gate          >99.9%
T1 (relaxation)       Energy decay timescale               Long vs gate time
T2 (dephasing)        Phase coherence, T2 ≤ 2T1            Long vs gate time
Circuit depth         Gates before decoherence kills it    >10^6 gates
Quantum volume (QV)   IBM: max square circuit with >2/3    ≫1000 today
EPLG                  Error per layered gate               <0.1%
Logical error rate    After QEC                            <10^-15 for Shor
```

---

## Roadmap: NISQ → Fault-Tolerant QC

```
NOW (NISQ era)               EARLY FTQC (~2030–2035)       CRQC (~2035–2040+)
─────────────────────────    ─────────────────────────     ──────────────────────
100–1000 physical qubits     1M+ physical qubits           Full error-corrected
No error correction          10s–1000s logical qubits      Logical qubits at scale

Coherence-limited depth      Surface code: ~1000 phys.     RSA-2048 factorable
Noise kills long circuits    per logical qubit             in hours

VQE (quantum chemistry)      Early Shor demos on small N   Grover useful for
QAOA (optimization)          Quantum simulation niche      crypto key search
Quantum advantage unclear    advantages (chemistry)        Full ab initio sim

Key challenge: error         Key challenge: T gate cost    Key bottleneck:
per gate ~0.1–0.5%           (magic state distillation)    magic state factories
exceeds threshold for        overhead still enormous       at scale
useful QEC overhead
```

**Post-quantum cryptography migration timeline:**
- Harvest-now-decrypt-later (HNDL) attacks happening today — adversaries store
  encrypted data now to decrypt when CRQC arrives
- NIST PQC standards published 2024: ML-KEM (FIPS 203), ML-DSA (FIPS 204), SLH-DSA (FIPS 205)
- Migration priority: long-lived secrets (state secrets, medical records, financial data)

---

## What QC Is NOT

```
MYTH                                    REALITY
──────────────────────────────────────  ────────────────────────────────────────────
Solves all NP-hard problems             Grover gives √N — NP stays hard for QC
Faster at everything than classical     Classical dominates for most real workloads
More qubits = more power                Gate fidelity + coherence time matter more
D-Wave is a general quantum computer    It is a specialized annealer, no proven
                                        quantum speedup demonstrated for anything
Quantum teleportation moves objects     It teleports quantum STATE, needs classical
                                        channel, no FTL information transfer
Current NISQ machines are useful        For a few chemistry problems, maybe;
                                        broad practical advantage is not yet shown
```

---

## Session Arc for This Directory

<!-- @editor[content/P2]: Session Arc lists only 5 files but directory contains 10 — files 05-09 (Variational Algorithms, Quantum Communication, NISQ Applications, Quantum Software, Quantum ML) are absent from this navigation block. Update to reflect actual directory contents. -->

```
00-OVERVIEW.md        ← You are here (field map, complexity, hardware, roadmap)
01-QUBITS-CIRCUITS    ← Mathematical foundations: Dirac notation, gates, circuits
02-ALGORITHMS         ← Shor, Grover, QFT, QPE, HHL, QAOA, VQE
03-ERROR-CORRECTION   ← Decoherence, stabilizer codes, surface codes, thresholds
04-HARDWARE-COMPLEXITY← Physical platforms, DiVincenzo criteria, BQP/QMA depth
```

---

## Decision Cheat Sheet

| Goal | Relevant QC concept |
|------|---------------------|
| Break RSA-2048 / ECC | Shor's algorithm — requires CRQC (~millions of logical qubits) |
| Speed up unstructured search | Grover's — √N speedup, useful for key search |
| Simulate quantum chemistry | VQE, QPE — likely first practical advantage |
| Solve combinatorial optimization | QAOA — heuristic, advantage not proven at scale |
| Solve linear systems | HHL — exponential speedup with major input/output caveats |
| Understand QC limits | BQP ⊈ NP, QMA-hardness of k-local Hamiltonians |
| Assess encryption migration urgency | HNDL threat model, NIST PQC FIPS 203/204/205 |
| Evaluate hardware claims | Gate fidelity, EPLG, circuit depth, not qubit count |
| Understand error correction cost | Surface code ~1000 physical per logical qubit |

## Common Confusion Points

**Quantum parallelism is not free parallel execution.** Measuring a superposition collapses
it to a single outcome. You never "read out" all 2^n amplitudes. The entire algorithm must
structure interference so the final measurement is useful.

**Bell inequality violation ≠ FTL communication.** Entanglement correlations are real and
nonlocal, but the no-communication theorem is ironclad. You cannot use entanglement alone
to transmit information.

**NISQ ≠ quantum advantage.** Google's 2019 "quantum supremacy" claim was on a contrived
sampling problem; later classical algorithms improved significantly. No clear practical
quantum advantage for real-world problems has been demonstrated as of 2025.

**QC is not the right tool for:** sorting, most database queries, general ML inference,
most graph algorithms, anything where classical hardware is already polynomial and the
constant matters.
