# 08 — Digital Logic

This is the physical substrate beneath the entire computing stack: NAND gates compose into ALUs, ALUs into pipeline stages, pipelines into CPUs that execute the ISA, and the OS scheduler manages threads atop that ISA. Every abstraction from Boolean algebra through FSMs to RTL synthesis has a direct counterpart in the software world — truth tables are lookup tables, FSMs are state machines in protocol handlers, and the synthesis flow is a compiler toolchain targeting silicon instead of machine code.

```
DIGITAL LOGIC LANDSCAPE
═══════════════════════════════════════════════════════════════════════════════

  COMBINATIONAL LOGIC           SEQUENTIAL LOGIC            SYSTEM LEVEL
  ─────────────────────────     ───────────────────────     ───────────────────
  Boolean algebra               Flip-flops (D, JK, SR, T)  FSMs (Moore/Mealy)
  Truth tables, K-maps          Registers, counters         ASM charts
  Gates: AND/OR/NOT/XOR/NAND    Latches vs edge-triggered   Datapaths
  Two-level minimization        Clocking, setup/hold        RTL description
  Hazards (glitches)            Metastability               FPGA architecture
  Multiplexers, decoders        Synchronous design          HDL synthesis

  CMOS IMPLEMENTATION:
    nMOS: ON when gate=1
    pMOS: ON when gate=0
    CMOS gate: pMOS pull-up network + nMOS pull-down network (complementary)
    No static current draw at logic levels → low power

  6.111 bridge: This IS 6.111. Precision refresher from first principles
  through FSMs, timing analysis, and FPGA/HDL.
```

---

## 1. Boolean Algebra

### Axioms (Huntington's Postulates)

```
  Variables: B ∈ {0, 1}

  OR  (+ or ∨):            AND (· or ∧):
  0 + 0 = 0                0 · 0 = 0
  0 + 1 = 1                0 · 1 = 0
  1 + 0 = 1                1 · 0 = 0
  1 + 1 = 1                1 · 1 = 1

  NOT (complement):
  0̄ = 1,  1̄ = 0

  Completeness: {AND, OR, NOT} is functionally complete.
  Also complete: {NAND} alone, {NOR} alone.
```

### Identities

| Law | OR form | AND form |
|---|---|---|
| Identity | A + 0 = A | A · 1 = A |
| Null | A + 1 = 1 | A · 0 = 0 |
| Idempotent | A + A = A | A · A = A |
| Complement | A + Ā = 1 | A · Ā = 0 |
| Double negation | — | Ā̄ = A |
| Commutative | A+B = B+A | AB = BA |
| Associative | A+(B+C) = (A+B)+C | A(BC) = (AB)C |
| Distributive | A(B+C) = AB+AC | A+BC = (A+B)(A+C) |
| Absorption | A + AB = A | A(A+B) = A |
| **De Morgan** | **(A+B)̄ = Ā·B̄** | **(AB)̄ = Ā+B̄** |
| Consensus | AB + ĀC + BC = AB + ĀC | (A+B)(Ā+C)(B+C) = (A+B)(Ā+C) |

**De Morgan**: negate a product → sum of negations; negate a sum → product of negations.
Mechanically: flip AND↔OR, complement all literals.

### Duality

Every valid equation in Boolean algebra remains valid when AND ↔ OR and 0 ↔ 1 are swapped simultaneously. The dual of any theorem is also a theorem.

---

## 2. Logic Gate Implementations

### Gate Symbol Summary

```
  AND:  A──┐                OR:  A──┐                NOT:  A──▷○── Ā
       B──┤ >─── AB              B──┤ ≥1─── A+B
            └──                       └──

  NAND: A──┐                NOR:  A──┐                XOR: A──┐
       B──┤ >○─── (AB)̄           B──┤ ≥1○─── (A+B)̄          B──┤ =1─── A⊕B
            └──                       └──                      └──

  XNOR: A──┐
        B──┤ =1○─── A⊙B = A⊕B⊕1
             └──
```

### CMOS Implementation

```
  CMOS inverter:
       VDD
        |
       pMOS (A=0 → ON, A=1 → OFF)
        |
        +─── output = Ā
        |
       nMOS (A=0 → OFF, A=1 → ON)
        |
       GND

  CMOS NAND (2-input):
       VDD
        |
     pA─┤ pMOS A
        |
     pB─┤ pMOS B (two pMOS in parallel)
        |
        +─── Y = (AB)̄
        |
     nA─┤ nMOS A
        |
     nB─┤ nMOS B (two nMOS in series)
        |
       GND

  Rule: pMOS in pull-up = DUAL of nMOS in pull-down.
  nMOS: series = AND, parallel = OR.
  pMOS: series = OR (De Morgan), parallel = AND (De Morgan).
  Complex gate: implement F directly → saves transistors vs multi-gate approach.
```

### Gate Count and Complexity

| Gate | Transistors | Notes |
|---|---|---|
| CMOS inverter | 2 | Most efficient gate |
| NAND-2 | 4 | Preferred building block (speed + count) |
| NOR-2 | 4 | Also 4T, slower due to series pMOS |
| AND-2 | 6 | NAND + inverter |
| OR-2 | 6 | NOR + inverter |
| XOR-2 | 8–12 | Several implementations |

**NAND is preferred** in standard cells: series nMOS is fast, parallel pMOS is acceptable.
NOR: series pMOS is slow (pMOS already slower than nMOS).

---

## 3. Canonical Forms and K-Maps

### Canonical Sum of Products (SOP) and Product of Sums (POS)

```
  Truth table → canonical forms:

  Minterm: product term with all variables (complemented or not) = 1 at exactly one row.
  m₃ = A̅BC (for ABC = 011)

  Maxterm: sum term with all variables = 0 at exactly one row.
  M₃ = (A+B̄+C̄) (for ABC = 011)

  SOP (sum of minterms):  F = Σm(where F=1)
  POS (product of maxterms): F = ΠM(where F=0)
  F_SOP and F_POS are equivalent; which is simpler depends on function.
```

### Karnaugh Maps (K-maps)

```
  Systematic minimization for 2–4 variables (5–6 manageable).
  Visual grouping of adjacent minterms → simplify.

  3-variable K-map (2×4):
       BC
  A  00  01  11  10
  0 | 0 | 1 | 1 | 0 |
  1 | 1 | 1 | 0 | 0 |

  Rules:
  1. Group 1s into rectangles of sizes 1, 2, 4, 8 (powers of 2)
  2. Rectangles must wrap around edges (map is toroidal)
  3. Each rectangle = one product term (essential prime implicant if unique)
  4. Use fewest, largest rectangles covering all 1s
  5. Find all prime implicants, then minimum cover

  Example groups above:
  Column 01-11 rows 0,1: BC (B and C both 1, regardless of A)
  Row 1, columns 00-01: AB̄ (A=1, B=0, C varies)
  Minimal: F = BC + AB̄C  → or after checking: F = BC + AB̄ (need to verify)
```

### 4-Variable K-map

```
       CD
  AB  00  01  11  10
  00 |   |   |   |   |
  01 |   |   |   |   |
  11 |   |   |   |   |
  10 |   |   |   |   |

  Corner cells are all adjacent (map wraps horizontally AND vertically).
  A group of all four corners = one term.
  "Don't care" (X): can be included in group or not — use to make larger groups.
```

### Hazards

```
  Static hazard: output momentarily transitions to wrong value during input change.
  Dynamic hazard: output changes 3+ times when it should change once.

  Static-1 hazard: output should stay 1 but glitches to 0.
  Cause: SOP realization where adjacent minterms in different product terms
         have race condition during variable transition.
  Fix: add consensus term (cover the transition with a redundant term).
       The extra term is the prime implicant covering both minterms.

  In synchronous circuits: hazards don't matter if flip-flop captures
  value only after glitches have settled. Hazards matter in:
    - Asynchronous logic
    - Glitch-sensitive outputs (chip select, memory enable)
    - High-speed analog-adjacent circuits (ADC clock)
```

---

## 4. Combinational Building Blocks

### Multiplexer (MUX)

```
  2-to-1 MUX:      n-to-1 MUX (log₂n select lines):
  S=0: Y = A       Universal logic element.
  S=1: Y = B       MUX(A,B;S) = ĀS̄ + BS = SOP
                   Any function of n variables implementable with
  Y = ĀS + BS      2^(n-1)-to-1 MUX (one variable used as data).

  Example 4-to-1 MUX:        MUX for F(A,B,C):
  S[1:0] selects one of      Use A,B as selects (4 combinations).
  4 inputs D3..D0.           Each input = F(0,0,C), F(0,1,C), F(1,0,C), F(1,1,C)
                             = 0, C, 1, C̄ (constants or C/C̄).
```

### Decoder

```
  n-to-2^n decoder: activates exactly one output line for each input code.
  3-to-8 decoder: inputs A,B,C → 8 output lines O0..O7
  Oₖ = 1 only when ABC = binary(k)

  Use: memory address decode, microprocessor instruction decode.
  Two-level AND-OR = decoder + OR gates → any combinational function.
```

### Encoder and Priority Encoder

```
  2^n-to-n encoder: inverse of decoder.
    Multiple active inputs → ambiguous. Use priority encoder instead.

  Priority encoder: if multiple inputs active, output code for highest priority input.
    V (valid) output: 0 if no input active, 1 if any active.
```

### Adders

```
  Half adder: S = A⊕B,  C = AB
  Full adder: S = A⊕B⊕Cin,  Cout = AB + ACin + BCin = AB + (A⊕B)Cin

  Ripple carry adder:
    Chain n full adders. Each Cout → Cin of next stage.
    Delay: O(n) — carry must propagate through all stages.
    n=32: too slow for modern CPUs.

  Carry lookahead adder (CLA):
    Generate G = AB,  Propagate P = A⊕B
    Carry: Cₖ₊₁ = Gₖ + PₖCₖ
    Compute all carries simultaneously from G and P:
    C₄ = G₃ + P₃G₂ + P₃P₂G₁ + P₃P₂P₁G₀ + P₃P₂P₁P₀C₀
    Delay: O(log n) with multi-level CLA — standard in ALUs.

  Carry select adder:
    Compute two 4-bit sums in parallel (assuming Cin=0 and Cin=1).
    Select correct sum via MUX once actual Cin arrives.
    Balance area vs speed.
```

### Comparator and ALU

```
  1-bit equality: A⊙B = 1 iff A=B  (XNOR)
  n-bit equality: AND of n XNORs

  n-bit magnitude comparator (iterative):
    Compare MSB first. If equal, proceed to next bit.

  ALU: combines arithmetic (add/sub) and logic (AND/OR/XOR) in one unit.
    Operation select via control lines.
    Most ALUs: adder for arithmetic, bitwise units for logic, MUX for output.
```

---

## 5. Sequential Logic: Flip-Flops

### Latches vs Edge-Triggered Flip-Flops

```
  Latch: level-sensitive. Output follows input while enable is active.
    SR latch: S=R=0: hold; S=1: set Q=1; R=1: clear Q=0; S=R=1: forbidden.
    D latch: Q follows D when E=1; latches when E=0.
    Problem: transparent during enable → output glitches during pulse.

  Edge-triggered flip-flop: samples input on clock edge only.
    D flip-flop: Q captures D at rising edge of CLK.
    Most common: positive-edge-triggered D-FF.
    JK FF: J=1,K=0: set; J=0,K=1: clear; J=K=1: toggle; J=K=0: hold.
    T FF: toggle on clock when T=1. Built from D-FF + XOR.

  Always use edge-triggered FFs in synchronous design.
  Latches are used intentionally only in specific timing-critical cases.
```

### D Flip-Flop Timing Parameters

```
  ┌──────────────────────────────────────────────────────────────────┐
  │                    D-FF TIMING                                    │
  │                                                                   │
  │    D ───XXXXXXX╔════════════════╗XXXXXXXX───                      │
  │                 ← t_setup →    ← t_hold →                        │
  │   CLK ──────────────╔════╗─────────────────                       │
  │                     ↑ rising edge                                 │
  │                     capture point                                 │
  │    Q ────────────────────────────╔══════════── (after t_cq)       │
  │                                  Q captures D at edge             │
  └──────────────────────────────────────────────────────────────────┘

  t_setup: D must be stable before clock edge by this much
  t_hold:  D must stay stable after clock edge by this much
  t_cq:    clock-to-Q propagation delay (time until Q is valid)

  Setup violation: D changes too close before clock → metastability
  Hold violation: D changes too close after clock → potentially captures wrong value
  Metastability: FF output can remain at indeterminate voltage for unbounded time
                 MTBF = e^(τ·f_sync) / (f_data · f_clock) — synchronizer design
```

### Registers and Shift Registers

```
  Register: n D-FFs sharing a clock. Holds n-bit value.
  Load enable: CLK only loads when EN=1; otherwise holds.

  Shift register (serial input, parallel output):
    D₀ ─FF─ D₁ ─FF─ D₂ ─FF─ ... (all share clock)
    Serial in: bit enters D₀ each cycle, shifts through.
    After n cycles: full n-bit word loaded serially.
    Uses: serial-to-parallel conversion, LFSR, delay lines.

  Linear Feedback Shift Register (LFSR):
    XOR taps at specific positions feed back to input.
    Maximal length LFSR of n bits: cycles through 2ⁿ-1 states.
    Uses: pseudo-random number generation, CRC, spread-spectrum.
    Polynomial: x^n + ... + 1 (primitive polynomial mod 2).
```

---

## 6. Synchronous Finite State Machines

### Moore vs Mealy Machines

```
  Moore Machine:                    Mealy Machine:
  Output = f(state only)            Output = f(state, input)

  State register                    State register
     |                                 |
  next-state logic ← input         next-state logic ← input
     |                                 |
  output logic (no input)          output logic ← input

  Moore: output changes only on clock → glitch-free, one cycle latency.
  Mealy: output can change with input within a clock cycle → faster, can glitch.
  Any Mealy machine ↔ Moore machine (Moore may need extra state).
```

### FSM Design Procedure

```
  1. Understand the specification (natural language or timing diagram)
  2. Draw state diagram:
     - Circle = state
     - Arc = transition (label: input/output for Mealy, input for Moore)
     - Arrow = initial state
  3. Encode states (binary, one-hot, or Gray code)
  4. Derive next-state logic (K-map or Boolean equations)
  5. Derive output logic
  6. Implement in flip-flops + combinational logic (or HDL)
```

### State Encoding Choices

```
  Binary:   n states → ⌈log₂n⌉ bits. Fewest FFs. Complex next-state logic.
  One-hot:  n states → n bits (one hot at a time). More FFs. Simpler logic.
            Preferred for FPGAs (abundant FFs, routing is the cost).
  Gray code: adjacent states differ by 1 bit. Reduces glitches on FSM outputs.
             Used for async safe counters crossing clock domains.

  One-hot example (3-state FSM):
    S0=001, S1=010, S2=100
    Transition from S1 to S2: just check if S1 bit is 1
    No decoder needed, each state's register directly enables transitions.
```

### Example: Traffic Light Controller

```
  States: GREEN (30 cycles), YELLOW (5 cycles), RED (30 cycles)
  Simple timer-based:

  State     | Timer | Next state | Outputs
  ──────────┼───────┼────────────┼─────────────
  GREEN     | > 0   | GREEN      | G=1, Y=0, R=0
  GREEN     | = 0   | YELLOW     | G=1, Y=0, R=0
  YELLOW    | > 0   | YELLOW     | G=0, Y=1, R=0
  YELLOW    | = 0   | RED        | G=0, Y=1, R=0
  RED       | > 0   | RED        | G=0, Y=0, R=1
  RED       | = 0   | GREEN      | G=0, Y=0, R=1

  Datapath: down-counter, TC (terminal count) drives FSM transitions.
  Control: FSM outputs drive light signals + counter load/enable.
  This separation (datapath + control FSM) is the standard RTL structure.
```

---

## 7. Timing Analysis

### Setup and Hold Time Analysis

```
  For a pipeline register:
    Source FF (reg_A) → combinational logic → Destination FF (reg_B)

  Setup constraint (max frequency):
    t_clk ≥ t_cq_A + t_logic + t_setup_B
    f_max = 1 / (t_cq + t_logic_max + t_setup)

  Hold constraint (min delay — must hold long enough):
    t_cq_A + t_logic_min ≥ t_hold_B
    If violated: FF captures wrong data regardless of clock speed.
    Cannot fix by slowing clock. Fix: add buffer (delay element) in path.

  Clock skew: arrival time difference between clock at two FFs.
    Positive skew (dest clock arrives later):
      Setup: t_clk + δ_skew ≥ t_cq + t_logic + t_setup  (helps setup)
      Hold:  t_cq + t_logic ≥ t_hold - δ_skew             (hurts hold)
    Negative skew: opposite.
    Target: minimize skew across chip via clock distribution network (H-tree).
```

### Critical Path

```
  Critical path: the combinational path with the largest delay.
  Determines maximum clock frequency.

  Methods to improve:
    1. Retiming: move registers through logic to balance pipeline stages
    2. Pipelining: add registers in the middle of long paths
    3. Restructure logic: reorder operations (e.g., CLA instead of ripple carry)
    4. Technology mapping: use faster cells for critical gates
    5. Gate sizing: larger gates drive faster (at cost of power)

  Static timing analysis (STA): enumerate all paths, compute slack.
    Slack = t_clk - (t_cq + t_path + t_setup)
    Positive slack: path meets timing.
    Negative slack: timing violation — path is too slow.
```

---

## 8. FPGA Architecture

### Basic FPGA Resources

```
  ┌─────────────────────────────────────────────────────────────────────┐
  │                   FPGA ARCHITECTURE                                  │
  │                                                                      │
  │  IOB ──── Routing ──── CLB ──── Routing ──── CLB ──── Routing ─ IOB │
  │            matrix       │        matrix       │        matrix        │
  │                         │                     │                      │
  │                        DSP                   BRAM                   │
  │                    (multiply-                (block                  │
  │                    accumulate)                RAM,                   │
  │                                             18/36Kb)                 │
  └─────────────────────────────────────────────────────────────────────┘

  CLB (Configurable Logic Block):
    LUT (Look-Up Table): n-input truth table stored in SRAM.
      4-input LUT = 16-bit SRAM → implements any 4-variable function.
      6-input LUT (modern Xilinx): 64-bit SRAM.
    FF: D flip-flop for registered outputs.
    MUX: select combinational or registered output.

  Routing:
    Programmable switches between CLBs and signal wires.
    Configured at startup from bitstream.
    Routing delay often dominates over logic delay in FPGAs.

  BRAM (Block RAM): 18 or 36 Kbit dual-port RAM.
  DSP slice: 18×18 or 27×18 multiplier + adder + accumulator.
    Implements multiply-accumulate in one CLK. Used for filters, FFTs.
```

### LUT-Based Logic

```
  4-input LUT as truth table:
    Inputs: A,B,C,D (4 bits → 16 combinations)
    SRAM: 16 bits, one per row of truth table
    Operation: use ABCD as address into 16-bit memory → output

  Any 4-variable Boolean function implementable in one LUT.
  5-variable: two 4-LUTs + MUX (available in one CLB).
  6-variable: one 6-LUT (modern FPGAs).

  Advantages vs ASIC:
    Reconfigurable: change bitstream = change logic
    Short time-to-market, no NRE cost
    Lower peak performance than ASIC (routing overhead)
    Lower density, higher power per logic function
```

### FPGA vs ASIC

| Property | FPGA | ASIC |
|---|---|---|
| Speed | Lower (routing delay) | 5–10× faster |
| Power | Higher per function | Lower |
| Density | Lower | Higher |
| NRE cost | $0 | $1M–$100M |
| Unit cost | Higher | Lower (high volume) |
| Time to market | Days–weeks | 6–18 months |
| Reconfigurability | Yes (bitstream) | No |
| Prototyping | Standard method | Not used |

---

## 9. HDL Synthesis Concepts

**Compiler toolchain analogy:** The RTL-to-silicon flow maps directly onto the compiler pipeline:

```
SOFTWARE COMPILATION                  HARDWARE SYNTHESIS
──────────────────────────────────────────────────────────────────────────────
C/C++/Rust source code                Verilog / SystemVerilog / VHDL
  ↓ parsing, AST                        ↓ elaboration, design hierarchy
Intermediate representation (IR)      Generic gate-level netlist
  ↓ optimization passes                 ↓ boolean optimization, retiming
Target-specific code generation       Technology mapping (library cells / LUTs)
  ↓ register allocation                  ↓ placement (cells → physical locations)
Linker (resolves addresses)           Routing (connects wires, resolves geometry)
  ↓ static analysis / verification       ↓ STA (static timing analysis)
Executable binary                     GDSII (ASIC) or bitstream (FPGA)
──────────────────────────────────────────────────────────────────────────────
```

The synthesis constraint file (.sdc) is analogous to compiler flags and link-time optimization targets — it tells the tool what clock frequency to target, which paths are critical, and where to trade area for speed.

### RTL (Register Transfer Level) Design Flow

```
  Specification (behavior)
       ↓
  RTL description (Verilog / VHDL)
    - Registers (always @posedge clk)
    - Combinational logic (assign / always @*)
    - Structural hierarchy (module instantiation)
       ↓
  Synthesis (Synopsys DC, Vivado, Quartus)
    - Maps RTL to library cells / LUTs
    - Performs optimization (boolean, timing)
    - Outputs gate-level netlist
       ↓
  Place & Route
    - Physical placement on chip / FPGA
    - Route wires
    - Static timing analysis (STA)
       ↓
  Bitstream (FPGA) or GDSII (ASIC tape-out)
```

### Verilog RTL Coding Style

```verilog
  // D flip-flop with synchronous reset
  always @(posedge clk) begin
    if (reset)
      q <= 1'b0;        // Non-blocking assignment — use in clocked logic
    else
      q <= d;
  end

  // Combinational logic
  always @(*) begin     // Sensitive to all inputs
    case (sel)
      2'b00: y = a;
      2'b01: y = b;
      2'b10: y = c;
      default: y = d;
    endcase
  end

  assign y = (sel == 2'b00) ? a :   // Continuous assignment
             (sel == 2'b01) ? b : c;
```

### Critical Coding Rules for Synthesis

```
  1. Always use non-blocking (<=) for clocked logic,
     blocking (=) for combinational.
     Mixing them causes simulation/synthesis mismatch.

  2. List all inputs in sensitivity list of combinational always @(*).
     Missing signals: simulation works, synthesis may differ.

  3. Avoid latches: every combinational output must be assigned
     in every branch of every if/case.
     Incomplete case → synthesis infers latch (usually wrong).

  4. Avoid asynchronous resets in modern design (setup/hold analysis harder).
     Synchronous reset: flip-flop samples reset on clock edge.
     Exception: global reset (power-on) often asynchronous.

  5. One clock domain per always block. Multiple clocks = multiple always blocks.
     Cross-domain signals: synchronizer (two FFs in series).
```

---

## 10. Clock Domain Crossing (CDC)

```
  Data crossing from clock domain A to clock domain B:
    Setup/hold cannot be guaranteed — metastability risk.

  Synchronizer (for single-bit signals):
    Two-FF synchronizer: 1st FF may go metastable, 2nd FF samples resolved output.
    MTBF = e^(τ·T_clk2) / (f_data · f_clk2)
    τ depends on FF technology, T_clk2 = clock period.
    Rule: two FFs standard; three FFs for high-speed, mission-critical.

  Multi-bit signals: must not use multiple synchronizers independently.
    Gray-coded counter: adjacent values differ by 1 bit → only 1 bit can be wrong.
    FIFO with Gray-coded read/write pointers: standard solution.
    Handshake: req/ack protocol with each bit synchronized.

  Never sample unsynchronized multi-bit bus: bits may capture from different cycles.
```

---

## 11. Decision Cheat Sheet

| Design need | Method |
|---|---|
| Minimize combinational logic | K-map (≤4 vars), Quine-McCluskey (≥5 vars), EDA tool |
| Implement any function with one logic block | MUX (2^(n-1)-to-1 for n-variable function) |
| Fast adder (32-bit) | Carry lookahead or Kogge-Stone adder |
| Store state / pipeline data | D flip-flop (positive edge triggered) |
| Design a controller | FSM (Moore for glitch-free outputs) |
| One-hot vs binary encoding | One-hot for FPGAs, binary for ASICs (fewer FFs) |
| Maximize clock frequency | Pipeline, retiming, optimize critical path |
| Prevent hold violations | Add buffer (delay cell) in short paths |
| Cross clock domain (1-bit) | Two-FF synchronizer |
| Cross clock domain (N-bit counter) | Gray code + synchronizer |
| Cross clock domain (data bus) | Async FIFO with Gray-coded pointers |
| FPGA vs ASIC | FPGA: prototype/low volume; ASIC: high volume/performance |
| Generate pseudo-random sequence | LFSR (maximal length polynomial) |

---

## 12. Common Confusion Points

**1. Latch vs flip-flop — level vs edge sensitive**
A latch is transparent while enable is high: Q follows D whenever E=1. A D flip-flop captures D only at the clock edge. In synchronous design, always use edge-triggered FFs. Synthesis tools infer latches from incomplete if/case in combinational blocks — this is almost always a bug. If you see "inferred latch" in synthesis messages, check your sensitivity lists and case completeness.

**2. Non-blocking vs blocking in always blocks**
Non-blocking (<=): all right-hand sides evaluated, then all left-hand sides assigned simultaneously. Models register behavior correctly. Blocking (=): immediate sequential execution, like a software assignment. Use non-blocking exclusively in clocked (sequential) always blocks; use blocking in combinational always blocks. Mixing them in the same always block produces simulation/synthesis mismatch and is the source of many subtle RTL bugs.

**3. Clock period constraint = setup analysis only**
The clock period constraint (t_clk ≥ t_cq + t_logic + t_setup) prevents setup violations. Hold violations are independent of clock period — they're about minimum path delay, and slowing the clock does nothing. Hold violations must be fixed by increasing minimum path delay (adding buffers). FPGA tools handle hold automatically; ASIC designers must verify minimum paths.

**4. One-hot encoding doesn't reduce to one state on reset**
With one-hot encoding, reset must load exactly one 1 bit (e.g., 00001 for the initial state). If reset is not designed carefully or if the FSM somehow loses its one-hot property (corruption), it may enter an illegal state (0 ones or 2+ ones). Add a default case in HDL that goes to a known reset state to handle illegal state recovery.

**5. Metastability is probabilistic, never eliminated**
A synchronizer reduces the probability of metastability to acceptably low levels, but never to zero. Adding more FFs reduces the MTBF exponentially. For most designs, two FFs give MTBF of millions of years. In safety-critical systems (aviation, medical), three FFs or formal verification may be required. You cannot detect metastability from outside — the FF output eventually settles to 0 or 1, but you cannot know if it was metastable during the transition.

**6. FPGA LUT inference: every function costs the same**
In an ASIC standard cell library, an XOR costs more than a NOR. In an FPGA, every 4-input function costs exactly one LUT — XOR, XNOR, complex Boolean expression — all the same. This changes optimization strategy: for FPGAs, minimize LUT count (packing multiple inputs), not gate-level complexity. A 4-input AND and a 4-input XOR both use one LUT with the same delay.
