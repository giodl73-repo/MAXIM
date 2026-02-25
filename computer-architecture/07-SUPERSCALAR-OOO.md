# Superscalar and Out-of-Order Execution

## Beyond 1 IPC

A pipelined in-order processor approaches 1 IPC (instruction per cycle). But stalls from hazards reduce it. Superscalar execution attacks throughput by issuing multiple instructions per cycle. Out-of-order execution attacks latency by reordering instructions to hide stalls. Modern high-performance cores combine both.

```
+-----------------------------------------------------------------------+
|                   EXECUTION ENGINE OVERVIEW                           |
|                                                                       |
|  FRONT-END                    EXECUTION ENGINE (OOO)                 |
|  ---------                    --------------------                   |
|  Fetch (4–8 instrs/cycle)     Reservation Stations (Tomasulo)        |
|  Branch prediction            Issue queues per execution unit type    |
|  Decode (CISC→µops on x86)    Reorder Buffer (ROB) — in-order commit |
|  Micro-op cache (µop cache)   Register Alias Table (RAT) — renaming  |
|  Rename/allocate              Multiple execution units in parallel    |
|  Dispatch to reservation      Load/Store queues                       |
|  stations                     Write-back to ROB                       |
|                                                                       |
|  IN ORDER:               OUT OF ORDER:                RETIRE:        |
|  Fetch → Decode          Issue → Execute               In-order       |
|  → Rename → Dispatch     (when operands ready)         commit from   |
|                                                          ROB head     |
+-----------------------------------------------------------------------+
```

---

## Tomasulo's Algorithm

Robert Tomasulo described the out-of-order execution algorithm in 1967 for the IBM 360/91 floating-point unit. It is the basis for all modern OOO engines.

### Core Concepts

```
  RESERVATION STATION (RS):
  A buffer associated with each execution unit.
  Holds instructions waiting for operands.
  When all operands are ready, the instruction is issued.
  Multiple instructions can be waiting simultaneously.

  COMMON DATA BUS (CDB):
  When an execution unit computes a result, it broadcasts
  on the CDB with the value + the tag (RS number).
  All reservation stations simultaneously check: does any of
  my waiting operands match this tag? If so, capture the value.

  REGISTER RENAMING:
  The RAT (Register Alias Table) maps architectural registers
  to physical registers (or RS entries).
  This eliminates WAR (Write After Read) and WAW hazards.
  Instructions can operate on "physical" registers independently
  even if they share the same architectural register name.
```

### Tomasulo Example

```
  PROGRAM (floating point):
  1. FADD F1, F2, F3       ; F1 = F2 + F3
  2. FMUL F4, F1, F5       ; F4 = F1 * F5  (WAR on F1 from instr 1)
  3. FADD F1, F6, F7       ; F1 = F6 + F7  (WAW on F1 from instr 1)
  4. FMUL F8, F1, F9       ; F8 = F1 * F9  (WAR on F1 from instr 3)

  WITHOUT RENAMING: 3 and 4 must wait for 1 to complete.
  True dependency: 2 waits for 1 (F1 is actually needed).
  Name dependencies: 3 and 4 appear to depend on 1 but don't REALLY.

  WITH RENAMING:
  1. FADD P1, F2, F3       ; P1 (physical) = F2+F3  (F1 → P1)
  2. FMUL P4, P1, F5       ; P4 = P1*F5 (waits for P1 — real dep)
  3. FADD P10, F6, F7      ; P10 = F6+F7 (F1 → P10, different physical)
  4. FMUL P8, P10, F9      ; P8 = P10*F9 (waits for P10 — real dep)

  Instructions 1 and 3 can execute SIMULTANEOUSLY (independent physical regs)
  Instructions 2 and 4 each wait only for their real dependency.
  The WAW and WAR hazards are eliminated.
```

---

## The Reorder Buffer (ROB)

```
  PROBLEM: Instructions execute out of order.
  But EXCEPTIONS and INTERRUPTS must be handled precisely —
  the machine state must reflect program order up to the point
  of the exception.
  Also: branch mispredictions require flushing speculative work.

  SOLUTION: The Reorder Buffer.

  ROB is a circular buffer holding all in-flight instructions
  in PROGRAM ORDER.

  +---+---+---+---+---+---+---+---+---+---+---+---+
  | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |   |   |   |   |
  +---+---+---+---+---+---+---+---+---+---+---+---+
    ↑                               ↑
   HEAD (oldest)                  TAIL (newest)
   (next to commit)               (last allocated)

  ENTRIES: instruction, result value, destination register/memory,
           status (issued / executing / completed / ready-to-commit)

  COMMIT (RETIRE): The HEAD instruction commits when:
  1. It has completed execution (result ready)
  2. No earlier instruction has raised an exception
  Commits in-order, one or more per cycle.
  Result written to architectural register file.

  FLUSH: On misprediction or exception:
  All instructions from mispredicted branch onward are FLUSHED.
  ROB tail rewinds to the branch.
  Renamed physical registers are freed.
  Front-end redirected to correct path.
```

---

## Register Renaming: The RAT

```
  ARCHITECTURAL REGISTERS: The ISA's visible registers.
  x86-64: RAX, RBX... R15 (16 regs)
  ARM64: X0-X30 + SP (32 regs)

  PHYSICAL REGISTERS: The actual hardware register file.
  Many more than architectural: 180–200+ physical regs (Intel)
  (Intel Golden Cove: 280+ integer physical regs)

  REGISTER ALIAS TABLE (RAT):
  Maps: architectural register → physical register currently holding its value.

  EXAMPLE (x86-64, 4-wide rename):

  Cycle N: Rename 4 instructions:
  ADD RAX, RBX    RAX → P42 (new physical reg allocated)
  ADD RAX, RCX    RAX → P43 (new physical reg for RAX)
  ADD RDX, P42    RDX → P44 (reads P42 = old RAX value)
  MOV RSI, P43    RSI → P45 (reads P43 = RAX after first ADD)

  At this point:
  The four instructions are INDEPENDENT (different physical regs).
  Instructions 3 and 4 only need to wait for their producers.
  Instructions 1 and 2 can proceed in parallel.

  The RAT is updated every cycle for each renamed instruction.
  On flush (misprediction): the ROB-based architectural state is
  used to restore the RAT to the correct committed state.
```

---

## The Superscalar Front-End

```
  INSTRUCTION FETCH:
  Modern CPUs fetch 16–32 bytes per cycle.
  x86-64: 16 bytes = potentially 1–15 instructions (variable width)
  ARM64: 16 bytes = 4 instructions exactly (fixed 4-byte)

  BRANCH PREDICTION (integrated at fetch):
  The BTB predicts next fetch address before decode reveals branches.
  If BTB says this fetch contains a branch to target T:
  Next cycle fetches from T (not sequential).
  This is the "predict the branch at fetch time" optimization.

  DECODE:
  x86: 4–6 complex decoders (one complex decoder + N simple)
  The complex decoder handles multi-µop instructions.
  Simple decoders handle 1-µop instructions.
  Intel Golden Cove: 6 decoders total → up to 6 µops/cycle

  MICRO-OP CACHE (µop cache / decode cache):
  Intel: "Loop Stream Detector" (Nehalem) → "µop cache" (Sandy Bridge+)
  AMD: "Op cache"
  Stores already-decoded µops. Bypasses decode stage for hot loops.
  Intel Sandy Bridge µop cache: 1536 µops, ~32 KB effective.
  Benefits: hot loops often fit entirely in µop cache;
            decode bandwidth no longer the bottleneck.

  ALLOCATION + RENAME:
  After decode: allocate ROB entries + RS entries + physical regs.
  Update RAT. This is the rename stage.
  Width: same as decode width (4–8 µops/cycle).
```

---

## Execution Units

```
  EXECUTION UNIT TYPES (Intel Golden Cove example):

  INTEGER ALU:           4–6 ports, ~1 cycle latency
  INTEGER SHIFT/ROTATE:  Part of ALU or separate
  INTEGER MULTIPLY:      1 port, 3 cycle latency
  INTEGER DIVIDE:        1 port, 20–90 cycle latency (not pipelined)

  FP/SIMD ADD:           2 ports, 4 cycle latency
  FP/SIMD MULTIPLY:      2 ports, 5 cycle latency
  FP/SIMD FUSED MA-ADD:  2 ports, 5 cycle latency (replaces add+mul)
  FP DIVIDE:             1 port, 10–20 cycle latency

  LOAD:                  2–3 ports, 4–5 cycle L1 latency
  STORE ADDRESS:         2 ports
  STORE DATA:            2 ports
  (Load and store split into address computation + data transfer)

  BRANCH/JUMP:           1 port, ~1 cycle (verify prediction)

  DISPATCH PORTS (Intel):
  Physical ports connecting the scheduler to execution units.
  Intel Golden Cove: 10+ dispatch ports.
  Each cycle: scheduler selects ready µops and dispatches to ports.
  Up to 12 µops dispatched per cycle (across all ports).

  THROUGHPUT vs LATENCY:
  FP ADD: 4 cycle LATENCY (you must wait 4 cycles for the result)
          but 2/cycle THROUGHPUT (can start 2 FP ADDs per cycle)
  Pipeline: a new FP ADD can start every cycle even though
  it takes 4 cycles — as long as there's no dependency chain.
```

---

## Intel vs AMD vs Apple Microarchitecture

```
+------------------------------------------------------------------+
| FEATURE           | Intel Golden | AMD Zen 4  | Apple Everest   |
|                   | Cove (P-core)| (Raphael)  | (M2, ~est)      |
|-------------------|--------------|------------|-----------------|
| Decode width      | 6 µop/cycle  | 4 op/cycle | 8 op/cycle      |
| Rename width      | 6            | 6          | 8               |
| ROB entries       | 512          | 320        | ~630            |
| INT phys regs     | 280+         | 224        | ~400 (est)      |
| Scheduler (issue) | 160 entries  | 128 entries| ~300 (est)      |
| Dispatch ports    | 10           | 6+         | 12+ (est)       |
| Load bandwidth    | 2×256-bit    | 2×256-bit  | 2×128-bit (L1)  |
|                   |              |            | 4×load AGU      |
| Store bandwidth   | 2×256-bit    | 1×256-bit  | 2×store         |
| L1D cache         | 48 KB        | 32 KB      | 192 KB          |
| L1I cache         | 32 KB        | 32 KB      | 192 KB          |
| L2 cache          | 2 MB         | 1 MB       | 12–16 MB        |
| Clock (Boost)     | ~5.8 GHz     | ~5.7 GHz   | ~3.5 GHz        |
+------------------------------------------------------------------+

Apple's lower frequency + wider issue window + massive caches
= comparable or superior single-thread performance at lower power.
The OOO window (ROB, scheduler, physical regs) determines
how far ahead the processor can look for parallelism.
Apple's wide window is a deliberate design choice.
```

---

## Speculation and Spectre

```
  SPECULATIVE EXECUTION:
  The CPU executes instructions along the PREDICTED branch path
  before the branch outcome is confirmed.
  If prediction correct: those instructions commit — zero wasted time.
  If prediction wrong: those instructions flush — wasted cycles but
  no incorrect architectural state.

  THE SPECULATION RULES:
  Speculative instructions:
  - CAN read memory and registers
  - CANNOT modify architectural state
  - CANNOT perform I/O
  - CAN write to physical registers (uncommitted)
  - CANNOT commit until branch is confirmed + all prior instrs commit

  SPECTRE (2018, Kocher et al.):
  The microarchitectural state (cache state, TLB state) IS modified
  by speculative execution.
  After flush, the values are discarded — but the cache remains warm.
  A cache timing side-channel reveals what speculatively loaded data was.

  ATTACK:
  1. Train the branch predictor to mispredict in a specific direction.
  2. Speculatively execute code that reads a secret value.
  3. Use the secret to index into an array (cache-load a specific line).
  4. Flush the speculatively executed state (branch mispredict).
  5. TIME access to array elements — the one that's fast was loaded.
  6. Infer the secret from timing.

  MITIGATIONS:
  Retpoline: replace indirect branches with a construct that
  prevents speculation to arbitrary addresses.
  IBRS/IBPB: indirect branch speculation restrictions.
  eIBRS (Enhanced IBRS): Intel hardware mitigation.
  BTI mitigation on ARM: SB (Speculation Barrier).
  Performance cost: 5–30% on some workloads.
```

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| What is the ROB? | Reorder Buffer — holds in-flight instructions in program order, enables in-order commit |
| What does register renaming eliminate? | WAR (Write After Read) and WAW (Write After Write) name dependencies |
| What is the physical register file? | The actual hardware register file — much larger than the ISA's architectural registers |
| What determines OOO window size? | ROB entries + reservation station depth + physical register count |
| Why does Apple M-series beat Intel at lower frequency? | Wider decode (8 vs 6), massive caches (192 KB L1D), larger ROB/scheduler — more parallelism visible |
| What is Spectre? | A side-channel attack exploiting the microarchitectural effects (cache warming) of speculative execution |
| What is a dispatch port? | Hardware connection from the scheduler to an execution unit; sets maximum throughput |

---

## Common Confusion Points

**Out-of-order ≠ out-of-order from the programmer's perspective**: The programmer sees a sequentially consistent state at each instruction retirement. OOO is entirely invisible to correctly-written code. The observation from software is: instructions seem to execute in order; the hardware is lying about this in a well-defined way.

**Superscalar width ≠ speedup multiplier**: A 4-wide superscalar does not give 4× speedup. Dependency chains limit parallel execution. If instructions 1–4 are all dependent on each other, they must execute sequentially regardless of width. Superscalar helps when independent instruction streams can be co-scheduled.

**Reservation stations ≠ the ROB**: These are different structures. The ROB holds instructions for in-order commit. Reservation stations (the issue queue / scheduler) hold instructions waiting for operands. An instruction can be in the ROB (to maintain program order) while still waiting in a reservation station for its operands.

**µop cache bypass ≠ cache in the data sense**: The µop cache (Decoded Stream Buffer) caches already-decoded micro-operations. It is not a data cache. Its purpose is to avoid re-running the expensive decode stage for hot loops. When the µop cache is active, the complex x86 decoders are idle.

**Division is not pipelined**: Division hardware is iterative (non-restoring or SRT-radix algorithms). An integer divide takes 20–90 cycles and is NOT fully pipelined — you typically cannot start the next divide until the current one completes. This is why division in tight loops is catastrophically slow compared to multiplication.
