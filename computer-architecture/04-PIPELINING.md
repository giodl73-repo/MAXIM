# Pipelining: Stages, Hazards, and Forwarding

## The Core Idea

A non-pipelined processor executes one instruction completely before starting the next. A pipelined processor overlaps execution of multiple instructions — like an assembly line. If each instruction takes 5 stages and each stage takes 1 cycle, a non-pipelined CPU takes 5 cycles per instruction; a pipelined CPU approaches 1 CPI (clock cycles per instruction) at steady state.

```
  NON-PIPELINED (5-cycle instructions):
  Instr 1: [IF ID EX MEM WB]
  Instr 2:                   [IF ID EX MEM WB]
  Instr 3:                               [IF ID EX MEM WB]
  Time:     1  2  3   4   5   6   7   8   9  10  11  12  13  14  15
  = 15 cycles for 3 instructions = 5 CPI

  PIPELINED (5-stage):
  Instr 1: IF  ID  EX  MEM WB
  Instr 2:     IF  ID  EX  MEM WB
  Instr 3:         IF  ID  EX  MEM WB
  Time:     1   2   3   4   5   6   7
  = 7 cycles for 3 instructions → approaches 1 CPI at steady state
  = 5 + (N-1) cycles for N instructions
```

The performance gain is (approximately) equal to the number of pipeline stages — a 5-stage pipeline approaches 5x throughput over non-pipelined. Real CPUs have 14–20+ stages.

---

## The Classic 5-Stage Pipeline

```
  +------+   +------+   +------+   +------+   +------+
  |  IF  | → |  ID  | → |  EX  | → | MEM  | → |  WB  |
  +------+   +------+   +------+   +------+   +------+
  Instruction Instruction  Execute  Memory   Write
  Fetch      Decode      (ALU op)   Access   Back
  (PC → Mem) (Read regs)            (Load/   (Result
              (decode    (compute    Store)    to reg)
              opcode)    address)

  IF: Use Program Counter to fetch instruction from instruction cache.
  ID: Decode the instruction; read source register values from register file.
  EX: Execute ALU operation. Compute effective address for memory ops.
  MEM: Access data cache (for loads/stores). Non-memory ops pass through.
  WB: Write the result back to the destination register.

  PIPELINE REGISTERS: Between each stage, a register holds the
  intermediate results. This is what enables overlap.
  IF/ID register, ID/EX register, EX/MEM register, MEM/WB register.
```

---

## Pipeline Hazards

The three types of hazard that break ideal 1-CPI throughput.

### Structural Hazards

```
  DEFINITION: Two instructions need the same hardware resource
  in the same cycle.

  CLASSIC EXAMPLE: Single unified memory (instruction + data)
  Instruction fetch (IF stage) and memory access (MEM stage)
  both need to access memory simultaneously.

  SOLUTION: SEPARATE instruction cache and data cache.
  Modern CPUs: distinct L1-I (instruction) and L1-D (data) caches.
  This is why Harvard architecture (separate instruction/data paths)
  influences practical pipeline design even in von Neumann machines.

  ANOTHER EXAMPLE: Only one multiply unit (MUL is multi-cycle)
  First MUL needs the unit for 3 cycles.
  Second MUL cannot start until cycle 4.
  SOLUTION: Stall, or add more execution units.
```

### Data Hazards

```
  DEFINITION: An instruction depends on the result of a
  prior instruction that hasn't completed yet.

  EXAMPLE: RAW (Read After Write) — true dependency
  ADD R1, R2, R3    ; R1 = R2 + R3     (computed in EX)
  SUB R4, R1, R5    ; R4 = R1 - R5     (needs R1 in ID)

  Timeline:
  ADD:  IF  ID  EX  MEM WB
  SUB:      IF  ID  EX  MEM WB
               ↑
               SUB needs R1 here (ID stage reads registers)
               But ADD hasn't written R1 yet (WB is 2 cycles later)
               → RAW HAZARD

  THREE APPROACHES:
  1. STALL ("bubble"): insert NOP cycles until value is ready
  2. FORWARDING (bypassing): route result from EX output directly
     to EX input of next instruction
  3. REORDER: compiler reorders code to interleave independent instr.
```

### Data Hazard Types

```
  RAW (Read After Write) — true dependency
  SUB R1, R2, R3       ; R1 = R2 - R3
  ADD R4, R1, R5       ; Needs R1 ← hazard!

  WAR (Write After Read) — anti-dependency
  SUB R4, R1, R5       ; Reads R1
  ADD R1, R2, R3       ; Writes R1 ← "hazard" only in
                         out-of-order; in-order: no problem
                         (SUB reads R1 before ADD writes it)

  WAW (Write After Write) — output dependency
  ADD R1, R2, R3       ; Writes R1
  SUB R1, R4, R5       ; Also writes R1 ← only a problem
                         if SUB finishes before ADD
                         (OOO execution issue)

  IN-ORDER PIPELINES: Only RAW hazards are dangerous.
  OOO PIPELINES: WAR and WAW become dangerous too.
  SOLUTION FOR WAR/WAW: REGISTER RENAMING (see 07-SUPERSCALAR-OOO.md)
```

---

## Forwarding (Data Bypassing)

The key optimization that eliminates most pipeline stalls for data hazards.

```
  WITHOUT FORWARDING (3 stalls for ADD→SUB):

  ADD R1, R2, R3:  IF  ID  EX  MEM  WB
  SUB R4, R1, R5:      IF  ID  **   **   **  EX  MEM  WB
                                ↑wait 3 cycles for WB

  WITH FORWARDING:
  The result of ADD is available at the END of EX stage.
  SUB needs R1 at the START of EX stage.
  We can ADD a bypass path from EX output → EX input:

  ADD R1, R2, R3:  IF  ID  EX──────┐  MEM  WB
  SUB R4, R1, R5:      IF  ID   EX─┘  MEM  WB
                                ↑
                           Forwarded from previous EX stage
                           No stall needed!

  FORWARDING PATHS NEEDED:
  EX/MEM register → EX input  (1-cycle old result)
  MEM/WB register → EX input  (2-cycle old result)

  LOAD-USE HAZARD (cannot be fully forwarded):
  LDR R1, [R2]     ; R1 loaded from memory — result at END of MEM
  ADD R3, R1, R5   ; Needs R1 at START of EX — 1 cycle too early!

  LDR:             IF  ID  EX  MEM──┐  WB
  ADD:                 IF  ID  *** EX─┘  MEM  WB
                                ↑
                           1-cycle stall required (load-use stall)
                           Compiler can hide this with reordering
```

---

## Control Hazards (Branch Hazards)

```
  DEFINITION: The pipeline fetches instructions after a branch
  before knowing whether the branch is taken.

  EXAMPLE:
  BEQZ R1, label    ; branch if R1 == 0
  ADD R2, ...       ; fetched speculatively
  SUB R3, ...       ; fetched speculatively
  ...
  label: XOR R4...  ; the real next instruction if branch taken

  IF the branch is resolved in the EX stage:
  3 instructions were fetched wrongly (IF, ID, possibly EX stages)
  = 3-cycle BRANCH PENALTY if taken and wrong instructions fetched.

  APPROACHES:

  1. PREDICT NOT TAKEN: Always fetch fall-through instructions.
     Flush the pipeline if branch is taken.
     50% accuracy on random branches.

  2. PREDICT TAKEN: Always fetch target instructions.
     Flush if not taken.

  3. DELAYED BRANCH (RISC original): Always execute 1 instruction
     after the branch (the "delay slot"). Compiler fills the slot
     with useful work from before the branch. Awkward for programmers.

  4. BRANCH PREDICTION: Modern approach — see below.
```

---

## Branch Prediction

Modern CPUs invest heavily in prediction to avoid pipeline flushes.

```
  STATIC PREDICTION:
  Compiler sets a "branch hint" bit in the instruction.
  Predict backward branches as taken (loops: usually loop back).
  Predict forward branches as not taken.
  x86: segment override prefix 0x2E = branch not-taken hint
                                0x3E = branch taken hint (rarely used)

  DYNAMIC PREDICTION (hardware):

  1-BIT PREDICTOR:
  Per-branch: store 1 bit — "last outcome."
  Predict same as last time.
  Problem: loops mispredict on last iteration AND first of next loop.

  2-BIT SATURATING COUNTER (Smith predictor):
  States: Strongly Not Taken | Weakly Not Taken | Weakly Taken | Strongly Taken
  Must mispredict TWICE before changing prediction direction.
  Handles nested loops much better.

        NT ──→ WNT ──→ WT ──→ T
        ←─────────────────────
        (transition on each outcome)

  GLOBAL HISTORY PREDICTOR:
  Use last N branch outcomes to index a pattern table.
  A conditional branch inside a loop often correlates with the
  loop counter — global history can capture this.

  PERCEPTRON PREDICTOR:
  Use a dot product of weights × history bits.
  Positive result → predict taken. Train on outcomes.
  Modern Intel and AMD use neural-network-inspired predictors.

  TOURNAMENT PREDICTOR:
  Combine multiple predictors and a meta-predictor that
  learns which predictor is better for each branch.

  MISPREDICTION PENALTY:
  Modern CPUs: 14–20 pipeline stages deep.
  Branch target unknown until resolve at stage 8–10.
  Misprediction = flush ~10–15 instructions of speculative work.
  = 10–15 cycles wasted.
  A branch that mispredicts every 10 times = 1–1.5 cycles/branch overhead.
  This is why branchless code can be faster for unpredictable conditions.
```

---

## Branch Target Buffer (BTB) and Return Stack Buffer

```
  BRANCH TARGET BUFFER (BTB):
  A cache mapping branch PC → predicted target address.
  Enables the fetch stage to predict WHERE to fetch next
  even before decoding reveals it is a branch.
  Without BTB: must wait until decode to know it's a branch.
  With BTB: fetch redirects speculatively at cycle 1.

  Structure: essentially a small cache.
  Tagged with branch PC.
  Capacity: 4K–64K entries in modern CPUs.
  Also includes branch type prediction (conditional/unconditional/call/return).

  RETURN STACK BUFFER (RSB):
  A small stack tracking return addresses for function calls.
  CALL pushes RIP+4 onto RSB.
  RET pops RSB → predicted return address.
  Much more accurate than BTB for RET instructions.
  Depth: 16–32 entries.
  Overflow: RET predictions fall back to BTB (inaccurate).
  (Deep recursion stresses the RSB.)

  INDIRECT BRANCH:
  JMP [RAX] — target depends on runtime value.
  Harder to predict than direct branches.
  Modern CPUs: ITTAGE predictor (Indirect Target History Table).
  Spectre v2 exploits indirect branch prediction.
```

---

## Branch Prediction in the Performance Context

```
  LOOP PREDICTION:
  for (int i = 0; i < 1000; i++) { ... }

  Branch at loop end: taken 999 times, not-taken once.
  Good predictor: mispredict 1/1000. → negligible overhead.

  UNPREDICTABLE BRANCH:
  if (data[i] < threshold) sum += data[i];  // random data

  Without CMOV: branch mispredicts ~50%.
  With CMOV:    no branch at all → no misprediction.

  CMOV (x86):
  CMOVL rax, rbx    "move rbx to rax if less-than flag set"
  No branch, no prediction, no misprediction penalty.
  ARM equivalent: CSEL X0, X1, X2, LT

  WHEN BRANCHLESS IS NOT BETTER:
  If the branch IS highly predictable (>95%), a branch
  is faster because the CPU can skip the computation entirely.
  Branchless computes both sides and selects.
  A well-predicted branch skips the false side entirely.
```

---

## Deeper Pipelines: Tradeoffs

```
  MORE STAGES → HIGHER CLOCK RATE
  Shorter work per stage → shorter cycle time → higher GHz.

  MORE STAGES → HIGHER MISPREDICTION PENALTY
  The branch is resolved later → more speculatively fetched
  instructions must be flushed on a miss.

  Intel Pentium 4 (Prescott, 2004): 31-stage pipeline
  Could reach 3.8 GHz (for its era, very fast clock).
  But: 31-stage pipeline = 31-cycle misprediction penalty.
  Real-world IPC was poor. The design was abandoned.

  Intel Core 2 (2006): Back to ~14 stages.
  Lower clock, much better IPC → better real-world performance.

  MODERN BALANCE:
  Intel Golden Cove (Alder Lake P-core): ~14–16 stages
  AMD Zen 4: similar depth
  Apple M2 Everest core: ~14 stages (estimated)

  THE POWER WALL:
  Deeper pipelines → higher frequency → O(f^n) dynamic power.
  Modern CPUs are frequency-limited by power, not by transistor count.
  Intel's "megahertz myth" era (Pentium 4) was the lesson learned.
```

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| How many pipeline stages in a classic RISC CPU? | 5: IF, ID, EX, MEM, WB |
| What is a RAW hazard? | Read After Write — instruction reads a value being written by a prior instruction |
| How does forwarding fix RAW hazards? | Routes result from EX output directly to EX input of next instruction |
| What is a load-use stall? | 1-cycle stall when an instruction uses a value loaded by the immediately preceding load |
| What is the branch misprediction penalty? | 10–20 cycles depending on pipeline depth and stage at which branch resolves |
| What is a BTB? | Branch Target Buffer — caches branch PC → predicted target address for fast fetch redirection |
| When should you use CMOV instead of JE? | When the branch is data-dependent and unpredictable — branchless code avoids misprediction |
| Why did the Pentium 4 fail? | 31-stage pipeline → high GHz but huge misprediction penalty → poor IPC |

---

## Common Confusion Points

**Forwarding ≠ eliminating stalls**: Forwarding (bypassing) eliminates stalls for ALU-to-ALU dependencies. The load-use case (LDR followed immediately by a using instruction) still requires 1 stall cycle even with forwarding — the memory result arrives too late.

**Stall ≠ NOP in the code**: A pipeline stall (bubble) is inserted by HARDWARE — it is not an instruction. The compiler can sometimes reorder instructions to avoid stalls, but the hardware also inserts bubbles when necessary.

**"Branch prediction" ≠ "speculative execution"**: Branch prediction says "predict which path." Speculative execution is executing instructions along the predicted path before knowing if the branch is correct. They are related but distinct. Speculative execution is what Spectre exploits.

**Pipeline stages ≠ execution units**: The pipeline stages are the phases of a single instruction's journey. Execution units (integer ALU, FP unit, load/store unit) are where work actually happens in the EX/MEM stage. A superscalar CPU has multiple execution units to handle multiple instructions in the same stage simultaneously.

**The 5-stage pipeline is a teaching model**: Real x86 CPUs have 14–20 stages. The stages include: branch prediction, fetch, decode, micro-op decode, allocation, rename, issue, execute (integer/FP/load/store), write-back, retire. The 5-stage model is the conceptual foundation, not the implementation reality.
