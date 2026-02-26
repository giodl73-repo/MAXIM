# Future Architectures: Neuromorphic, Quantum, Accelerators

## The Landscape

Post-Moore's law computing explores architectures that do not rely on transistor scaling for performance gains. The major directions: (1) specialization — custom silicon for specific workloads; (2) integration — CXL, chiplets, memory-near-compute; (3) neuromorphic — event-driven spiking neural networks; (4) quantum — superposition and entanglement for specific algorithms.

```
+-----------------------------------------------------------------------+
|               FUTURE ARCHITECTURE LANDSCAPE                           |
|                                                                       |
|  NEAR TERM (2024–2027)          MEDIUM TERM (2028–2035)              |
|  ----------------------         -------------------------             |
|  Chiplet integration            3D stacked DRAM on CPU               |
|  CXL memory expansion           CXL fabric at rack scale             |
|  Domain-specific accelerators   Photonic interconnects               |
|  NPUs on consumer silicon       In-memory compute (PIM)              |
|  Die stacking (3D)              Near-memory processing                |
|                                                                       |
|  LONG TERM / SPECULATIVE        QUANTUM                              |
|  -------------------------      -------                               |
|  Neuromorphic (Loihi, SpiNNaker)NISQ devices: 100–10,000 qubits      |
|  Analog compute                 (2024: IBM Condor 1,121 qubits)      |
|  Optical computing              Fault-tolerant: millions of           |
|  DNA storage/compute            physical qubits for logical qubit    |
|                                 Target: chemistry, optimization,      |
|                                 crypto-breaking (distant)             |
+-----------------------------------------------------------------------+
```

---

## Chiplets and Advanced Packaging

The most immediately impactful trend. Instead of designing one monolithic die, break the chip into separate small chips (chiplets) connected via high-bandwidth, low-latency interconnects in one package.

```
  WHY CHIPLETS?

  YIELD ECONOMICS:
  A 600 mm² monolithic die on TSMC N5:
  If defect density = 0.1/mm², yield ≈ e^(-0.1×600) ≈ 1% — useless.
  A 150 mm² chiplet: yield ≈ e^(-0.1×150) ≈ 22%.
  Build the 600 mm² chip as 4 chiplets: each yields 22%.
  Effective yield of package: ~22%^4 × correction factors ≈ much better.
  SMALLER DIES = HIGHER YIELDS = CHEAPER CHIPS AT SCALE.

  HETEROGENEOUS INTEGRATION:
  Use the best process node for each function:
  CPU cores: TSMC N3 (bleeding edge, expensive)
  I/O: TSMC N6 (mature, cheap — I/O doesn't need tiny transistors)
  Memory: DRAM process (completely different from logic process)
  RF: SiGe BiCMOS
  Combine in one package via advanced packaging.

  EXAMPLES:
  AMD EPYC (Genoa/Turin): 12 CCD (CPU Core Chiplets) + 1 IOD
    CCD: 8 Zen 4 cores, TSMC N5, ~70 mm² each
    IOD: I/O controller, TSMC N6, ~400 mm²
    Total: 12×8 = 96 cores, one package

  Intel Meteor Lake: CPU tile (Intel 4) + GPU tile (TSMC N5)
    + SoC tile (TSMC N6) + I/O tile (Intel 7)
    Four different process nodes in one package.

  Apple M2 Ultra: two M2 Max dies connected via UltraFusion
    700 GB/s die-to-die bandwidth (vs 16 GB/s PCIe 5.0)
    Appears as one chip to software.
```

### Interconnect Standards for Chiplets

```
  UCIe (Universal Chiplet Interconnect Express):
  Industry standard for die-to-die interconnect.
  Standard bump pitch, protocol stack.
  Allows mixing chiplets from different vendors.

  LATENCY vs BANDWIDTH COMPARISON:
  PCIe 5.0 ×16: 128 GB/s, ~500 ns (off-package)
  CXL 2.0:      same physical as PCIe, adds coherency, ~200 ns
  UCIe (short reach): 1–2 TB/s, ~1–5 ns (same package)
  HBM (on-package): 1–3 TB/s, ~30–100 ns
  SRAM L3 to core: ~40 cycles = ~10 ns

  The die-to-die bandwidth within a chiplet package approaches
  what was previously on-chip bandwidth. This changes the
  tradeoffs for cache design and memory architecture.
```

---

## CXL: Compute Express Link

CXL (Compute Express Link) is a PCIe 5.0-based open interconnect standard enabling cache-coherent memory and device expansion.

```
  CXL DEVICE TYPES:

  CXL.io (Type 1 devices):
  Traditional PCIe device semantics.
  No memory or cache coherency.
  Use: accelerators that don't need host-coherent memory.

  CXL.cache + CXL.mem (Type 2 devices):
  Device has its own memory + can cache host memory.
  Cache coherence between host and device.
  Use: FPGAs, smart NICs, GPU-like accelerators.

  CXL.mem (Type 3 devices):
  Memory expansion: add more DRAM to a host.
  The host can access this memory with load/store instructions
  (byte-addressable, cache-coherent).
  Latency: ~170 ns (vs ~70 ns for local DRAM).
  Use case: memory-bandwidth-hungry applications (in-memory DB,
           ML training, analytics).

  MEMORY POOLING (CXL 2.0 / 3.0):
  Multiple hosts share a CXL memory pool.
  Host A uses 256 GB, Host B uses 128 GB from same 512 GB pool.
  Dynamic allocation as workloads change.
  "Memory disaggregation" — decouple memory from compute.

  DATACENTER USE CASE (general):
  Memory-capacity-hungry workloads (in-memory databases, ML training,
  analytics) often need more DRAM than physically fits in a single
  server's DIMM slots. CXL enables:
  - Rack-scale memory pools: add CXL memory shelves, share across hosts
  - Dynamic overcommit: allocate more memory to a VM than host DIMMs hold
  - Cost optimization: right-size compute vs memory independently
  - Memory tiering: fast local DRAM + slower CXL-attached DRAM as tier 2

  All major cloud providers (AWS, GCP, Azure, hyperscalers) are
  building toward CXL-backed memory expansion. This is not
  Azure-specific — it is the direction of the entire industry.

  CLOUD INSTANCE EXAMPLE (Azure):
  CXL-based memory expansion allows VMs to have more DRAM than
  the physical host's DIMMs provide.
  Azure HBv4 and ND H100 v5 families are building toward CXL.
  Pooling allows overcommit and dynamic memory allocation across VMs.
```

---

## Processing in Memory (PIM / Near-Memory Compute)

```
  THE MEMORY WALL FROM ANOTHER ANGLE:
  CPU reads data from DRAM, processes it, writes back.
  75% of energy in many workloads: moving data.
  Solution: put compute NEAR or IN the memory.

  NEAR-MEMORY PROCESSING:
  Logic layer close to DRAM but not inside DRAM cells.
  HBM (High Bandwidth Memory): DRAM dies stacked with
  a base logic die. PIM logic can be added to the base die.
  Samsung HBM-PIM: simple SIMD units in HBM base die.
  SK Hynix GDDR6-AiM: multiply-accumulate units in GDDR.

  IN-MEMORY PROCESSING:
  Compute using the DRAM cell arrays themselves.
  Analog operations: bitwise ops can be done on DRAM rows.
  "Bulk bitwise" operations: AND/OR/XOR on entire memory rows
  without data ever leaving the array.
  Companies: UPMEM (DRAM with embedded RISC cores), Micron UPMEM partner.

  USE CASES:
  Graph processing (irregular memory access)
  Genome sequencing (huge datasets, simple operations)
  Database filtering (scan without cache pollution)
  Neural network inference (matrix-vector multiply in memory)

  STATUS (2024):
  Commercial PIM: UPMEM DIMMs (2020+), Samsung HBM-PIM.
  Still niche — programming models are immature.
  The memory consistency challenges are significant.
```

---

## Domain-Specific Accelerators

The dominant near-term trend: custom silicon for specific computations.

```
  TPU (Google Tensor Processing Unit):
  Custom ASIC for matrix multiply (the dominant ML operation).
  TPU v4: 275 TFLOPS BF16, 32 GB HBM, interconnected in "pods."
  3D torus network: 4,096 chips → "TPU Pod" = 1.1 exaFLOPS.
  vs NVIDIA H100: 989 TFLOPS BF16.
  TPU advantage: TCO, interconnect bandwidth.

  NPU (Neural Processing Unit):
  On-chip accelerator for ML inference on edge devices.
  Apple Neural Engine (ANE): in every Apple Silicon.
  M2: 15.8 TOPS INT8. M4: 38 TOPS.
  Qualcomm Hexagon DSP + AI accelerator.
  Intel NPU (Meteor Lake): ~34 TOPS.
  Used for: face recognition, autocorrect, voice processing, Core ML.
  Power-efficient: dedicated silicon beats general GPU at inference.

  DPU (Data Processing Unit):
  Offloads network processing, security, storage from main CPU.
  NVIDIA BlueField-3: 16 Arm Cortex-A78 + 400 Gbps networking.
  AWS Nitro: custom ASICs for VPC networking, storage IO, security.
  Azure SmartNIC: similar purpose.
  "The third programmable processor in the datacenter" (CPU, GPU, DPU).

  FPGA (Field-Programmable Gate Array):
  Reconfigurable logic — an array of logic blocks + interconnect.
  Can implement any digital logic (including custom accelerators).
  Xilinx (now AMD) UltraScale+, Altera (now Intel) Agilex.
  Latency: closer to ASIC than GPU.
  Power: better than GPU for fixed workloads.
  Flexibility: reprogram for different algorithms.
  Azure: available in some specialized instances (Catapult project).

  COMPARISON:
  ASIC > FPGA > GPU >> CPU  (for a specific workload: PPA = power, perf, area)
  ASIC = best PPA, no flexibility.
  FPGA = good PPA, reprogrammable (software changes).
  GPU = general, programmable, large ecosystem.
  CPU = universal, worst PPA for fixed computation.
```

---

## Neuromorphic Computing

```
  BIOLOGICAL INSPIRATION:
  The brain: ~86 billion neurons, ~100 trillion synapses.
  Power: ~20 watts.
  Tasks: vision, language, reasoning — with 20W vs AI data center MW.

  Brain's computation: SPIKING.
  Neurons don't output continuous values.
  They FIRE a brief spike (~1 ms) when membrane potential exceeds threshold.
  Information is encoded in the TIMING of spikes.
  Computation is EVENT-DRIVEN: no global clock, only when spikes arrive.

  NEUROMORPHIC ARCHITECTURE:
  Intel Loihi 2 (2021):
  128 neurons/core, 1 million+ neurons per chip.
  Event-driven: cores only compute when spikes arrive.
  On-chip learning: STDP (Spike-Timing Dependent Plasticity).
  Power: ~1 mW per 100K operations (vs GPU: ~1 W).

  IBM TrueNorth:
  4096 cores, 1 million neurons, 256 million synapses.
  70 mW total power.

  SpiNNaker2 (University of Manchester):
  Large-scale brain simulation platform.
  10 billion neuron simulation target.

  STATUS AND CHALLENGES:
  Programming: radically different from CUDA.
  No general-purpose compiler or framework.
  Models must be expressed as spiking networks.
  Training: backpropagation doesn't directly apply.
  Surrogate gradient methods, STDP.

  CURRENT USE CASES:
  Sensory processing (edge vision, radar)
  Reinforcement learning with low power budget
  Structural brain simulation (neuroscience research)
  NOT a general GPU replacement — very specialized.
```

---

## Quantum Computing

```
  THE QUANTUM ADVANTAGE PREMISE:
  Certain problems have exponential speedup on quantum hardware.
  Not all problems — quantum is NOT universally faster.

  QUANTUM GATE MODEL:
  Qubits: superposition of |0⟩ and |1⟩.
  |ψ⟩ = α|0⟩ + β|1⟩, where |α|² + |β|² = 1.
  Quantum gates: unitary operations on qubits.
  H (Hadamard): |0⟩ → (|0⟩ + |1⟩)/√2 (superposition)
  CNOT: controlled-NOT (entanglement)
  T, S: phase gates

  CURRENT STATE (2024):
  Physical qubit count:
    IBM Heron (2023): 133 qubits
    IBM Condor (2023): 1,121 qubits (but low quality)
    Google Sycamore (2023): ~70 high-quality qubits
    Atom Computing: 1,180 neutral atom qubits
  Useful qubits: much fewer — error rates limit effectiveness.
  NISQ era (Noisy Intermediate Scale Quantum): 50–1000 physical qubits.

  ERROR CORRECTION:
  Surface code: ~1000 physical qubits → 1 logical qubit.
  A 1000-logical-qubit fault-tolerant quantum computer
  needs ~1 million physical qubits.
  Current: ~100 useful physical qubits = 0 logical qubits with
  surface code error correction.
  This is the fundamental bottleneck.

  ALGORITHMS WITH QUANTUM ADVANTAGE:
  Shor's algorithm: factor N in polynomial time.
    Would break RSA/ECC if fault-tolerant QC existed.
    ~20 million physical qubits needed for RSA-2048.
    NOT imminent.
  Grover's algorithm: search √N instead of N.
    Quadratic speedup; breaks symmetric keys of half their
    classical security (AES-128 → 64-bit security).
  Quantum simulation: simulate quantum systems efficiently.
    Drug discovery, materials science, chemistry.
    THIS is the most likely near-term practical application.
  Quantum optimization: QAOA, VQE for optimization.
    Unclear practical advantage vs classical heuristics.

  AZURE QUANTUM:
  Microsoft: topological qubits (still pre-production as of 2024).
  Partners: Quantinuum, IonQ, Rigetti (on Azure Quantum).
  Q# language and QDK for quantum programming.
  Most practical use: hybrid quantum-classical algorithms.

  TIMELINE REALITY CHECK:
  NISQ era "quantum advantage" on real problems: 2027–2030 (maybe).
  Breaking RSA-2048: 2040+ (very optimistic), more likely 2050+ or never.
  Quantum simulation (chemistry): useful applications 2028–2035.
  Post-quantum cryptography migration: should start NOW regardless.
  (NIST PQC standards finalized 2024: ML-KEM, ML-DSA, SLH-DSA)
```

---

## 3D Integration

```
  CONVENTIONAL (2D):
  All transistors in a plane on the wafer.
  Interconnect limited by 2D area.

  STACKING (3D):
  Stack multiple dies vertically.
  Connect via Through-Silicon Vias (TSVs) or hybrid bonding.
  Increases bandwidth between layers dramatically.

  TYPES:
  DRAM on DRAM (HBM): 8–12 DRAM dies stacked.
  HBM3: 8-high stack, ~3.35 TB/s per stack.
  Logic on Logic: CPU die + cache die stacked.
  Intel Foveros (Meteor Lake): 3D stacked tiles.
  DRAM on Logic: future HBM-PIM, Samsung CXL-PIM.

  CACHE STACKING:
  AMD 3D V-Cache (Zen 3 / Zen 4):
  64 MB L3 SRAM stacked DIRECTLY on top of CPU core chiplet.
  Bonded via hybrid bonding (~9 µm pitch).
  Result: 192 MB total L3, 2× gaming/simulation performance.
  No change in ISA or software.
  Purely architectural improvement from packaging.

  INTEL EMBEDDED MULTI-DIE INTERCONNECT BRIDGE (EMIB):
  2D silicon bridge instead of 3D stacking.
  Dense interconnect tile embedded in package substrate.
  Allows high-bandwidth links between chiplets without TSVs.
  Used in: Intel Alder Lake, Meteor Lake.

  FUTURE: 3D stacking LOGIC on DRAM (not just DRAM on DRAM).
  This would put compute units directly above memory arrays.
  Bandwidth: 100s of TB/s between logic and data.
  Not yet manufacturable at scale.
```

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| Why use chiplets instead of one big die? | Yield: small dies yield much better; enables heterogeneous process nodes |
| What is CXL? | Cache-coherent memory/device interconnect over PCIe 5.0 physical layer — enables memory pooling |
| What is PIM? | Processing In Memory — puts compute near or inside DRAM to avoid data movement energy |
| What is the difference between TPU and GPU? | TPU: custom ASIC for matrix multiply, better TCO for ML; GPU: general compute with tensor cores |
| What makes neuromorphic efficient? | Event-driven (no idle compute), spike encoding, STDP learning — 1 mW vs 1 W at scale |
| When will quantum break RSA? | Not for decades — RSA-2048 requires ~20M physical qubits; today's best: ~1000 low-quality qubits |
| What should you do about post-quantum crypto now? | Begin migration to NIST PQC standards (ML-KEM, ML-DSA) — don't wait for "harvest now, decrypt later" |

---

## Common Confusion Points

**Chiplets ≠ multiple CPUs**: A chiplet package like AMD EPYC looks like one CPU to the OS. The chiplet decomposition is a manufacturing technique, not a programming model change. Some NUMA effects from chiplet topology exist (cross-die latency) but software mostly doesn't need to know.

**CXL ≠ NVMe or PCIe storage**: CXL is for MEMORY (byte-addressable, load/store semantics, cache coherent). NVMe is for storage (block I/O, filesystem, not byte-addressable). CXL 3.0 also enables peer-to-peer coherency between multiple devices.

**NISQ quantum ≠ useful quantum**: A 1000-qubit NISQ device can perform demonstrations and experiments but the error rate (~0.1–1% per gate) accumulates too fast for long algorithms. "Quantum advantage" claims from 2019–2023 (Google, IBM) were for contrived problems with no classical alternatives. Fault-tolerant quantum computing for real applications is still years away.

**Neuromorphic ≠ deep learning acceleration**: Neuromorphic chips run spiking neural networks (SNNs) — a different computational paradigm from the ANNs (artificial neural networks) used in deep learning. You cannot simply run PyTorch models on Loihi. The programming models are completely different.

**3D stacking ≠ just more cache**: 3D V-Cache doubles L3 size and dramatically reduces L3 miss rate for applications with large working sets (games, CFD, scientific computing). But it also increases the die height (thermal challenges) and the L3 latency is slightly higher than non-stacked L3. The win depends strongly on the application's memory access pattern.
