# Computer Architecture — Landscape and Taxonomy

## The Big Picture

Computer architecture describes the interface between hardware and software. Understanding it explains why code has the performance characteristics it does — cache misses, branch misprediction, SIMD speedups, NUMA effects. You know the theory (Turing machines, von Neumann model, computability) — this guide is about what the silicon actually does in 2024.

```
+-----------------------------------------------------------------------+
|                   COMPUTER ARCHITECTURE STACK                         |
|                                                                       |
|  APPLICATION CODE (C#, Rust, Java, C, C++)                           |
|  "What you write"                                                     |
|           |                                                           |
|           v                                                           |
|  COMPILER / JIT / AOT                                                 |
|  (translates to machine code; must know the ISA)                     |
|           |                                                           |
|           v                                                           |
|  +-----------------------+                                            |
|  | ISA                   |  Instruction Set Architecture             |
|  | (Instruction Set      |  The CONTRACT between software and HW:    |
|  | Architecture)         |  "what instructions exist, what they do,  |
|  | x86-64 / ARM64 /      |   what registers exist, memory model"     |
|  | RISC-V                |  Portable: same binary runs on any        |
|  +-----------------------+  x86-64 machine regardless of microarch   |
|           |                                                           |
|           v                                                           |
|  +-----------------------+                                            |
|  | MICROARCHITECTURE     |  The IMPLEMENTATION of that contract.     |
|  | (what Intel/AMD/Apple |  Pipeline depth, cache sizes,             |
|  | actually build)       |  out-of-order width, branch predictor —   |
|  | Intel Golden Cove /   |  all invisible from ISA.                  |
|  | AMD Zen 4 /           |  Governs performance.                     |
|  | Apple Everest core    |                                            |
|  +-----------------------+                                            |
|           |                                                           |
|           v                                                           |
|  PHYSICAL / CIRCUIT LAYER                                             |
|  (transistors, CMOS logic, lithography — below this guide)           |
+-----------------------------------------------------------------------+
```

**The critical split**: ISA vs microarchitecture. Two Intel CPUs from different generations run the same x86-64 binary (same ISA) but have wildly different performance (different microarchitectures). This is why backward compatibility is achievable at all — change the microarch, keep the ISA.

---

## ISA Design Philosophies

```
  CISC                              RISC
  (Complex Instruction Set)         (Reduced Instruction Set)
  -------------------------         -------------------------
  "Do more per instruction"         "Do simple things fast, combine"

  Many instructions, varying        Few instructions, fixed-length,
  length, complex operations        simple operations

  x86 / x86-64 (Intel, AMD)        ARM64 / RISC-V / MIPS / SPARC

  Variable instruction length:      Fixed instruction length:
  1–15 bytes (x86-64)               4 bytes (ARM64, RISC-V)

  Instructions like:                Instructions like:
    IMUL [mem], reg                   LDUR (load from memory)
    REP MOVS (block copy)             STUR (store to memory)
    ENTER/LEAVE (stack frame)         ADD  (add registers)
    CMPS/SCAS (string compare)        BL   (branch with link)
    FMUL on memory operand            MADD (multiply-add)

  Decode is expensive:              Decode is trivial:
  Intel Haswell: 4 decoders,        1 instruction = 1 micro-op
  variable-length decode            Pipeline stages stay uniform
  Internal translation to micro-ops
  (CISC surface, RISC interior)

  Legacy advantage:                 Power advantage:
  Decades of software compatibility Simpler decode = fewer transistors
  Compiler can do more in one       = less power = better perf/watt
  instruction                       → won mobile completely
```

---

## Memory Hierarchy: The Numbers That Drive Everything

```
  STORAGE           LATENCY     BANDWIDTH    SIZE (typical)
  +-------------+   ~0 cycles   ----         ~1 KB total
  | REGISTERS   |
  +-------------+
         |
  +-------------+   ~4 cycles   ~1 TB/s      32–64 KB/core
  | L1 CACHE    |
  +-------------+
         |
  +-------------+   ~12 cycles  ~500 GB/s    256 KB–1 MB/core
  | L2 CACHE    |
  +-------------+
         |
  +-------------+   ~40 cycles  ~200 GB/s    8–64 MB (shared)
  | L3 CACHE    |
  +-------------+
         |
  +-------------+   ~100 cycles ~100 GB/s    8–256 GB
  | DRAM        |
  +-------------+
         |
  +-------------+   ~50K cycles ~5 GB/s      256 GB–8 TB
  | NVMe SSD    |
  +-------------+
         |
  +-------------+   millions    ~1 GB/s      unlimited
  | HDD/Network |
  +-------------+

  RULE: L1 hit = fast. L3 miss → DRAM = 25x slower. Page fault = catastrophic.
  The memory wall: CPUs got faster than DRAM much faster.
  Caches exist to paper over this gap.
  Cache-friendly code is the single biggest performance lever in userspace.
```

---

## Parallelism Taxonomy

```
  +-----------------------------------------------------------+
  |           PARALLELISM IN MODERN PROCESSORS                |
  |                                                           |
  |  INSTRUCTION-LEVEL (ILP)      DATA-LEVEL (DLP)           |
  |  -------------------------    ----------------------     |
  |  Superscalar: issue 4+        SIMD/vector:               |
  |  instructions per cycle       AVX-512 = 16 × float32     |
  |  Out-of-order execution        in one instruction          |
  |  Branch prediction            NEON (ARM): 4 × float32    |
  |  Register renaming (RAT)      GPU: thousands of           |
  |  Speculative execution        SIMT threads                |
  |                                                           |
  |  THREAD-LEVEL (TLP)           TASK / PROCESS             |
  |  ----------------------       ------------------         |
  |  SMT (hyperthreading):        Multi-socket NUMA           |
  |  2 threads share 1 core's     Distributed compute        |
  |  execution units              (outside this guide)        |
  |  CMP: multiple cores                                      |
  +-----------------------------------------------------------+
```

---

## Flynn's Taxonomy (Historical Orientation)

```
  Flynn (1966) classified computers by instruction × data streams:

  SISD   Single Instruction, Single Data   — classic uniprocessor
  SIMD   Single Instruction, Multiple Data — vector units, GPUs
  MISD   Multiple Instruction, Single Data — rare; fault-tolerant systems
  MIMD   Multiple Instruction, Multiple Data — multi-core CPUs, clusters

  Modern reality:
  A single core is roughly SISD (with speculative/OOO blur).
  Vector units add SIMD.
  Multi-core makes the chip MIMD.
  A GPU is SIMT (Single Instruction, Multiple Threads) — like SIMD
  but with independent PCs, thread divergence allowed.
```

---

## Module Map

| File | Topic | Key Concepts |
|------|-------|-------------|
| 01-ISA-FUNDAMENTALS.md | ISA design space | RISC vs CISC, instruction formats, addressing modes |
| 02-X86-ARCHITECTURE.md | x86 and x86-64 | Register file, modes, encoding, extensions (SSE/AVX) |
| 03-ARM-RISC-V.md | ARM64 and RISC-V | Load-store arch, AArch64 registers, RISC-V ISA extensions |
| 04-PIPELINING.md | Pipeline design | 5-stage pipeline, hazards, forwarding, stalling, branch prediction |
| 05-MEMORY-HIERARCHY.md | Cache to DRAM | SRAM cells, DRAM timing, cache organization, TLB |
| 06-CACHE-COHERENCE.md | Coherence protocols | MESI/MOESI, snooping vs directory, memory consistency models |
| 07-SUPERSCALAR-OOO.md | Modern execution | Tomasulo algorithm, reservation stations, ROB, register renaming |
| 08-GPU-ARCHITECTURE.md | GPU / SIMT | SM/warp model, memory hierarchy, CUDA programming model |
| 09-FUTURE-ARCHITECTURE.md | Emerging designs | CXL, chiplets, neuromorphic, near-memory compute |

---

## Decision Cheat Sheet

| Question | Answer | See |
|----------|--------|-----|
| Why is my loop slow? | Cache miss, branch misprediction, or memory bandwidth | 05, 06 |
| What makes Apple Silicon fast for single-thread? | Wide OOO, massive caches, high memory bandwidth, package integration | 03, 07 |
| Why doesn't adding pipeline stages always help? | Deeper pipeline → longer misprediction penalty; more stages to fill | 04 |
| Why does SIMD speed up array processing 8–16x? | One instruction processes 8–16 elements simultaneously | 07 |
| Why do GPUs need thousands of threads? | To hide DRAM latency — while one warp stalls, others run | 08 |
| What is the ISA/microarch split? | ISA = visible contract; microarch = implementation | 01 |
| Why did ARM win mobile? | Load-store RISC simplicity = power efficiency; no complex decode | 03 |
| What causes false sharing? | Two threads writing different variables in the same cache line | 06 |

---

## Common Confusion Points

**"ISA" vs "architecture" are used sloppily**: "x86 architecture" usually refers to the ISA. The microarchitecture is what Intel or AMD actually implements. Intel Haswell and Intel Golden Cove both implement x86-64 ISA — radically different microarchitectures.

**"RISC is always faster"** is outdated: Modern x86 CPUs translate CISC instructions to RISC-like micro-ops internally (the decoders are expensive, but the execution backend is RISC-style). Performance differences between Intel and ARM today are more about process node, design choices, and memory subsystem than RISC vs CISC per se.

**L3 miss cost is not constant**: The 100-cycle figure for DRAM is average. With NUMA (multi-socket), a remote DRAM access can cost 200–300 cycles. With memory-mapped files, a page fault can cost millions.

**Out-of-order ≠ speculative**: OOO reorders instructions within what the program knows is definitively correct. Speculation predicts outcomes (usually branch targets) and executes along a predicted path before confirmation. Spectre/Meltdown exploited speculative execution specifically — OOO alone is not the issue.

**Hyperthreading ≠ 2x performance**: Two hardware threads share execution units. If one stalls on memory, the other uses idle units. Realistic gain: 20–30% on typical workloads, sometimes negative if cache footprint doubles and they thrash each other's L1.

**Cache line granularity matters**: Caches transfer in cache lines (64 bytes on x86). Reading one byte of a cold cache line costs you the full 64-byte transfer. This is why struct layout (AoS vs SoA) profoundly affects performance.
