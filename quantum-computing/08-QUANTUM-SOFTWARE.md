# Quantum Software Stack

## Big Picture: The Full Stack

```
┌─────────────────────────────────────────────────────────────────────┐
│                    QUANTUM SOFTWARE STACK                           │
│                                                                     │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │ APPLICATION LAYER                                            │  │
│  │  VQE / QAOA / QKD / Grover search                           │  │
│  │  Domain libraries: Qiskit Nature, PennyLane QML, Q# Chemistry│  │
│  └───────────────────────┬──────────────────────────────────────┘  │
│                          │                                          │
│  ┌───────────────────────▼──────────────────────────────────────┐  │
│  │ SDK / FRAMEWORK LAYER                                        │  │
│  │  Qiskit (IBM) · Cirq (Google) · PennyLane (Xanadu) · Q#(MS) │  │
│  │  High-level circuit construction, algorithm primitives       │  │
│  └───────────────────────┬──────────────────────────────────────┘  │
│                          │                                          │
│  ┌───────────────────────▼──────────────────────────────────────┐  │
│  │ INTERMEDIATE REPRESENTATION                                  │  │
│  │  OpenQASM 3.0 (text IR) · QIR (LLVM-based binary IR)        │  │
│  │  Interchange format between tools and hardware vendors       │  │
│  └───────────────────────┬──────────────────────────────────────┘  │
│                          │                                          │
│  ┌───────────────────────▼──────────────────────────────────────┐  │
│  │ TRANSPILATION / COMPILATION                                  │  │
│  │  Gate decomposition → routing → optimization → scheduling    │  │
│  └───────────────────────┬──────────────────────────────────────┘  │
│                          │                                          │
│  ┌───────────────────────▼──────────────────────────────────────┐  │
│  │ HARDWARE ABSTRACTION                                         │  │
│  │  Pulse-level control (Qiskit Pulse, Cirq cirq-google)        │  │
│  │  Native gate sets per backend                                │  │
│  └───────────────────────┬──────────────────────────────────────┘  │
│                          │                                          │
│  ┌───────────────────────▼──────────────────────────────────────┐  │
│  │ PHYSICAL LAYER                                               │  │
│  │  Superconducting (IBM, Google) · Ion trap (IonQ, Quantinuum) │  │
│  │  Photonic (Xanadu, PsiQuantum) · Neutral atom (QuEra)       │  │
│  └──────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────┘

  Azure Quantum: Microsoft abstraction over multiple hardware vendors
  (IonQ, Quantinuum, Rigetti, + Azure simulators)
```

---

## Qiskit (IBM) — Deepest Integration with Real Hardware

### Architecture

```
QISKIT MODULES (post-0.45 / Qiskit 1.x structure):

  qiskit.circuit     – QuantumCircuit, QuantumRegister, ClassicalRegister
  qiskit.primitives  – Sampler (bitstring distributions) + Estimator (⟨O⟩)
  qiskit.transpiler  – PassManager, transpile(), routing, optimization
  qiskit.pulse       – Schedule, pulse-level Drag/Gaussian pulses, control
  qiskit_aer         – Simulators (statevector, density matrix, noise model)
  qiskit_ibm_runtime – IBM Runtime: Sessions, Batch, primitive execution
```

### Circuit Construction

```python
from qiskit import QuantumCircuit
from qiskit.circuit.library import TwoLocal

# Manual circuit
qc = QuantumCircuit(3)
qc.h(0)                    # Hadamard on qubit 0
qc.cx(0, 1)                # CNOT: control=0, target=1
qc.rz(theta, 2)            # Parameterized rotation
qc.measure_all()

# Hardware-efficient ansatz (library)
ansatz = TwoLocal(n_qubits=4, rotation_blocks='ry',
                  entanglement_blocks='cx', reps=2)
# → Ry rotations + CNOT entanglement, 2 repetitions
```

### Primitives API (Qiskit 1.x — the right abstraction)

```
SAMPLER primitive:
  Input:  circuit + parameter values
  Output: quasi-probability distribution over bitstrings
  Use for: sampling-based algorithms, QAOA, VQA measurement

ESTIMATOR primitive:
  Input:  circuit + observable (PauliSumOp or SparsePauliOp) + parameters
  Output: ⟨ψ(θ)|O|ψ(θ)⟩  (expectation value)
  Use for: VQE energy, QAOA cost evaluation

WHY PRIMITIVES MATTER:
  Old API: transpile circuit → submit → get counts → manually compute ⟨O⟩
  Primitives API: declare what you want (expectation), runtime handles the rest
  Same code runs on simulator (Statevector) and real hardware (IBM backends)
  Runtime optimizes batching, error mitigation, shot distribution internally
```

### Transpiler Pipeline

```
INPUT CIRCUIT (arbitrary gates, logical qubits)
         │
         ▼ STAGE 1: INIT (layout selection)
         │   Qubit routing: map logical → physical qubits
         │   TrivialLayout / DenseLayout / SabreLayout (default)
         │
         ▼ STAGE 2: ROUTING (SWAP insertion)
         │   Insert SWAP gates to route non-adjacent 2-qubit gates
         │   SabreSwap algorithm: O(n log n) approximation
         │
         ▼ STAGE 3: TRANSLATION (gate set decomposition)
         │   Arbitrary U → {CX, Rz, SX, X}  (IBM basis)
         │   KAK decomposition for 2-qubit gates
         │
         ▼ STAGE 4: OPTIMIZATION (gate cancellation)
         │   Commutation analysis, redundant gate removal
         │   CX cancellation, 1Q gate fusion
         │
         ▼ STAGE 5: SCHEDULING (timing)
             Assign timing for all gates, handle alignment constraints

OPTIMIZATION LEVELS (transpile optimization_level=0..3):
  0: trivial layout, no optimization — for debugging
  1: TrivialLayout + basic optimization
  2: NoiseAdaptiveLayout + commutativity analysis
  3: SabreLayout + SabreSwap + full optimization — production default
```

### Qiskit Pulse (Pulse-Level Control)

```
For researchers who need sub-gate-level control:

  from qiskit.pulse import Schedule, DriveChannel, Gaussian

  with pulse.build(backend) as my_program:
      pulse.play(Gaussian(duration=160, amp=0.4, sigma=40),
                 pulse.drive_channel(0))
      pulse.play(Drag(duration=160, amp=0.1, sigma=40, beta=-5.0),
                 pulse.drive_channel(0))

USE CASES: custom native gates, optimal control pulses,
           pulse-level noise characterization
```

---

## Cirq (Google) — Moment-Based, Topology-Aware

### Moment Representation

```
CIRQ DESIGN PHILOSOPHY:
  Every circuit is a sequence of Moments (parallel gate layers)
  Each Moment: a set of gates with non-overlapping qubits
  Native to Google hardware topology (Sycamore grid)

from cirq import LineQubit, Circuit, H, CNOT, measure
q0, q1 = LineQubit.range(2)
circuit = Circuit(
    H(q0),
    CNOT(q0, q1),
    measure(q0, q1, key='result')
)
print(circuit)
# 0: ───H───@───M('result')───
# 1: ───────X───M('result')───

GRID QUBITS (for Sycamore topology):
  q = GridQubit(row, col)
  Only adjacent qubits can interact (2-qubit gates)
  cirq.google.Sycamore has specific connectivity graph
```

### Low-Level Circuit Manipulation

```
CIRQ STRENGTHS:
  1. Explicit moment structure (you see exactly what runs in parallel)
  2. Native gate set: CZ, sqrt-ISWAP (Sycamore native)
  3. Insertions/deletions at specific moments
  4. Transformer API for circuit optimization

  circuit.insert(0, H(q0), strategy=InsertStrategy.NEW_THEN_INLINE)

CIRQ-GOOGLE INTEGRATION:
  from cirq_google import optimized_for_sycamore
  optimized_circuit = optimized_for_sycamore(circuit, new_device=Sycamore)
  # → decomposes to CZ/sqrt-ISWAP, applies Google-specific optimizations
```

---

## PennyLane (Xanadu) — Differentiable Quantum Computing

### JAX/PyTorch Integration

```
PENNYLANE DESIGN PHILOSOPHY:
  Quantum nodes (qnodes) as differentiable functions
  Automatic differentiation: parameter-shift rule wired into AD framework
  Hardware-agnostic: runs on any backend (IBM, Google, Rigetti, simulators)

import pennylane as qml
import jax.numpy as jnp

dev = qml.device("lightning.qubit", wires=2)

@qml.qnode(dev, diff_method="parameter-shift")
def circuit(theta):
    qml.RY(theta[0], wires=0)
    qml.CNOT(wires=[0, 1])
    qml.RZ(theta[1], wires=1)
    return qml.expval(qml.PauliZ(0))

# JAX gradient — parameter-shift under the hood
from jax import grad
gradient = grad(circuit)(jnp.array([0.5, 0.3]))
# Works identically with PyTorch, TF, autograd
```

### Quantum Differentiable Programming Features

```
TRANSFORMS (qml.transforms):
  qml.transforms.batch_params     – vectorize over parameter batches
  qml.transforms.mitigate_with_zne – ZNE built in as transform
  qml.transforms.decompose        – custom gate decomposition
  qml.compile                     – gate optimization pass

ADJOINT DIFFERENTIATION (diff_method="adjoint"):
  Exact gradient in O(n) overhead (classical simulation only)
  vs parameter-shift: O(2×n_params) circuit evaluations
  → Only works on simulator, but very fast for hybrid ML training

SHOT VECTORS:
  dev = qml.device("default.qubit", wires=2, shots=[100, 1000, 10000])
  → Single execution returns results for all shot counts (ZNE-ready)
```

---

## Q# + Azure Quantum (Microsoft Stack)

### Q# Language Features

```
Q# TYPE SYSTEM:
  Qubit: opaque reference (allocated/released, never cloned)
  Result: Zero | One (measurement outcome)
  Pauli: PauliI | PauliX | PauliY | PauliZ
  operation vs function distinction:
    operation: can have quantum side effects (qubit ops, measurements)
    function: purely classical (no qubits), deterministic

QUBIT MANAGEMENT:
  use q = Qubit();        // allocate
  // guaranteed |0⟩ on allocation
  H(q);
  CNOT(q, q2);
  let r = M(q);          // measure
  Reset(q);              // reset before release
  // q automatically released at end of scope

ADJOINT AND CONTROLLED GENERATION:
  Every operation can have auto-generated Adjoint + Controlled functors:
  operation MyGate(theta: Double, q: Qubit) : Unit is Adj + Ctl {
      Ry(theta, q);
  }
  // Adjoint MyGate(theta, q) → Ry(-theta, q) auto-generated
  // Controlled MyGate([control], theta, q) → auto-generated
```

### Azure Quantum Resource Estimator

```
UNIQUE MICROSOFT DIFFERENTIATOR:
  Before running on real hardware, estimate:
  - Physical qubit count
  - Runtime duration
  - T-gate count (dominant fault-tolerant cost)
  - Magic state factory requirements

WORKFLOW:
  1. Write Q# algorithm
  2. Run ResourceEstimator (no hardware needed)
  3. Get: {n_physical_qubits, runtime_seconds, qubit_layout}
  4. Optimize algorithm until feasible on target hardware generation

EXAMPLE (Shor's on RSA-2048):
  with target = TargetParams.from_name("qubit_gate_ns_e3"):
      # 10^-3 physical gate error rate, nanosecond gate times
      estimate = resource_estimator.estimate(factoring_algorithm)
      # → ~4M physical qubits, ~8 hours

HARDWARE PARAMETER PROFILES:
  "qubit_gate_ns_e3":  10^-3 error, ns gates (current NISQ)
  "qubit_gate_ns_e4":  10^-4 error, ns gates (near-term target)
  "qubit_gate_us_e3":  10^-3 error, μs gates (ion traps)
→ Compare algorithm feasibility across hardware roadmaps
```

### Azure Quantum Integration with Azure

```
AZURE QUANTUM WORKSPACE:
  azure quantum workspace create --location eastus --resource-group myRG

  JOB SUBMISSION (Q# targeting IonQ):
  qsharp.azure.target("ionq.simulator")
  result = qsharp.azure.execute(MyQuantumProgram, n_shots=1000)

  JOB SUBMISSION (Python targeting Quantinuum via SDK):
  from azure.quantum import Workspace
  workspace = Workspace(subscription_id=..., resource_group=..., name=...)
  backend = workspace.get_backend("quantinuum.hqs-lt-s1")
  job = backend.run(qiskit_circuit, shots=100)

<!-- @editor[audience/P3]: The "VP perspective" sentence is the only place in the entire directory where the guide directly addresses the learner's role. This framing is fine as flavor but should not be the only connection to operational concerns. A Google or AWS engineer reading this file gets equal value from the Azure integration section (it's factual), but calling out "VP perspective" breaks the peer-level tone the style contract requires. Drop the explicit persona call-out; the content stands on its own. -->
INTEGRATION STORY (bridges to existing Azure):
  Azure Quantum Jobs → Azure Monitor (same metrics pipeline as App Insights)
  Quantum storage: results go to Azure Blob Storage / Azure Cosmos DB
  IAM: same RBAC as all Azure services
  Quantum Network Simulator: simulates quantum repeater networks on Azure
  → From a VP perspective: same operational posture as any other Azure service
```

---

## Intermediate Representations

### OpenQASM 3.0

```
OpenQASM 3 CAPABILITIES vs OpenQASM 2:
  Dynamic circuits: if/while/for loops based on measurement outcomes
  Classical registers with full type system (int, float, bool)
  Real-time classical computation in circuit
  Subroutines (gate definitions with classical args)
  Extern functions (call classical code from circuit)
  Hardware calibration instructions (pulse-level annotations)

EXAMPLE:
  OPENQASM 3.0;
  include "stdgates.inc";
  qubit[2] q;
  bit[2] c;

  h q[0];
  cx q[0], q[1];
  c = measure q;

  // Conditional on measurement:
  if (c[0]) {
      x q[1];  // Pauli-X correction
  }
```

### QIR (Quantum Intermediate Representation)

```
QIR = LLVM IR for quantum programs

DESIGN:
  Classical computation: standard LLVM types and instructions
  Quantum operations: LLVM intrinsics (__quantum__qis__h__body, etc.)
  Qubit/result: opaque LLVM pointer types

ADVANTAGE:
  Leverage 50 years of LLVM optimization infrastructure
  Classical control flow through LLVM JIT
  Heterogeneous compilation: same IR can target different hardware backends
  Microsoft-driven but designed for ecosystem adoption

  define void @GroverIteration(%Qubit* %q0, %Qubit* %q1) {
    call void @__quantum__qis__h__body(%Qubit* %q0)
    call void @__quantum__qis__cnot__body(%Qubit* %q0, %Qubit* %q1)
    %r = call %Result* @__quantum__qis__m__body(%Qubit* %q0)
    ret void
  }
```

---

## Classical Simulation Backends

```
┌──────────────────────────────────────────────────────────────────────┐
│ BACKEND          │ METHOD              │ MEMORY    │ QUBITS │ NOISE  │
├──────────────────┼─────────────────────┼───────────┼────────┼────────┤
│ Statevector      │ Store 2^n amplitudes│ 2^n       │ ≤ 30   │ No     │
│ (Aer, Cirq)      │ Matrix-vector mult  │ complex   │ (32GB) │        │
├──────────────────┼─────────────────────┼───────────┼────────┼────────┤
│ Density Matrix   │ Store 2^n × 2^n ρ  │ 4^n real  │ ≤ 20   │ Yes    │
│                  │ Superoperator app   │           │        │ (mixed │
│                  │                     │           │        │ states)│
├──────────────────┼─────────────────────┼───────────┼────────┼────────┤
│ MPS / Tensor     │ Represent state as  │ χ²·n      │ 100+   │ No     │
│ Network          │ matrix product state│ (bond dim │ (low   │        │
│ (ITensor, quimb) │ Contract networks   │ χ)        │ entgl) │        │
├──────────────────┼─────────────────────┼───────────┼────────┼────────┤
│ Stabilizer       │ Gottesman-Knill:    │ O(n²)     │ 1000+  │ No     │
│ (Clifford sim)   │ track Pauli frame   │           │ (Cliff.│        │
│ (Stim, Aer)      │ n² updates per gate │           │ only!) │        │
├──────────────────┼─────────────────────┼───────────┼────────┼────────┤
│ Noise model sim  │ Statevector + noise │ 2^n       │ ≤ 30   │ Yes    │
│ (Aer noisemodel) │ channel application │ complex   │        │ (model)│
└──────────────────┴─────────────────────┴───────────┴────────┴────────┘

STIM (Google, Gidney 2021):
  Specialized stabilizer simulator for quantum error correction research
  Handles circuits with 10^6+ Clifford operations efficiently
  Essential for QEC circuit development (surface codes, etc.)
```

---

## Framework Decision Matrix

```
┌──────────────────────────────────────────────────────────────────────┐
│ USE CASE                      │ RECOMMENDED FRAMEWORK               │
├───────────────────────────────┼─────────────────────────────────────┤
│ IBM hardware access           │ Qiskit (native API, Runtime)        │
│ VQE/QAOA on IBM backends      │ Qiskit + Qiskit Nature               │
├───────────────────────────────┼─────────────────────────────────────┤
│ Google hardware access        │ Cirq (native) + cirq-google         │
│ Low-level circuit manip       │ Cirq (moment-level control)         │
├───────────────────────────────┼─────────────────────────────────────┤
│ Quantum ML / hybrid gradient  │ PennyLane (JAX/PyTorch integration) │
│ Hardware-agnostic research    │ PennyLane                           │
├───────────────────────────────┼─────────────────────────────────────┤
│ Resource estimation           │ Q# + Azure Quantum RE               │
│ Azure integration             │ Q# + Azure Quantum                  │
│ Algorithm development (typed) │ Q# (adjoint/controlled auto-gen)    │
├───────────────────────────────┼─────────────────────────────────────┤
│ QEC circuit simulation        │ Stim (stabilizer circuits)          │
│ Large stabilizer circuits     │ Stim                                │
├───────────────────────────────┼─────────────────────────────────────┤
│ Multi-backend research        │ PennyLane or Qiskit (both support  │
│                               │ multiple backends via providers)    │
└──────────────────────────────┴──────────────────────────────────────┘
```

---

## Common Confusion Points

**OpenQASM 2 vs OpenQASM 3 are almost different languages.** QASM 2 is a simple gate listing format (barely a language). QASM 3 adds a full classical type system, real-time feedback, loops, and subroutines. They look similar but have very different expressiveness. Most tutorials still use QASM 2; production code should target QASM 3.

<!-- @editor[content/P2]: Qiskit versioning note is accurate for the 1.0 transition but may already be outdated — Qiskit 1.x has continued evolving (check current stable version), and IBM's deprecation/migration schedule for ibm_runtime vs qiskit_ibm_runtime has shifted. Verify the version boundary specifics and add current stable version number so the reader has a reference point. -->

**Qiskit versioning is a nightmare.** Qiskit Terra/Aer/IBMQ merged and reorganized: pre-0.39 (old Terra/Aer split), 0.39-0.45 (transition), 1.0+ (new unified structure). The primitives API (Sampler/Estimator) replaced the old QuantumInstance API. Be aware which tutorial era code comes from.

**QIR vs OpenQASM 3 are complementary, not competing.** QIR is a binary LLVM IR (compiler target). OpenQASM 3 is a text format (developer-facing). A compiler might: read Q# → emit QIR → optimize → emit OpenQASM 3 → submit to hardware.

**Transpilation output is NOT hardware-independent.** Transpiling for ibmq_manila (Falcon, heavy-hex) vs ibm_sherbrooke (Eagle) gives completely different circuits. When benchmarking circuit depth, always specify the target backend. A 2-qubit circuit might compile to 3 CX gates on one backend and 7 on another due to connectivity.

**Azure Quantum is not a quantum computer.** It's a cloud service that brokers access to third-party quantum hardware (IonQ, Quantinuum, Rigetti) plus Microsoft's own simulators and resource estimator. The quantum processors are operated by the respective companies; Azure provides a unified API, job queue, and billing surface.

**PennyLane "hardware-agnostic" has caveats.** The abstract circuit runs anywhere, but gradient methods differ: parameter-shift on hardware, adjoint differentiation only on simulator, finite differences everywhere (but inaccurate with shot noise). Code must be aware of which diff_method is being used and what device supports it.
