# Early Computers — Von Neumann, Atanasoff, Eckert+Mauchly, Zuse

## Era Overview

```
FIRST MACHINES: 1937–1952
===========================

  1937 ─── ATANASOFF conceives ABC (electronic, special-purpose, Iowa)
  1941 ─── ZUSE: Z3 — first programmable computer (relay-based, Berlin)
  1943 ─── COLOSSUS (Bletchley Park) — electronic, somewhat programmable, secret
  1944 ─── HARVARD MARK I (Aiken + IBM) — relay-based, programmed by punched tape
  1945 ─── ENIAC completed (Eckert+Mauchly, Penn) — electronic, general-purpose
  1945 ─── VON NEUMANN: "First Draft of a Report on EDVAC"
           — the stored-program architecture document
  1946 ─── ENIAC publicly demonstrated
  1948 ─── MANCHESTER BABY (Small-Scale Experimental Machine)
           — first stored-program computer to run a program
  1949 ─── EDSAC (Cambridge, UK) — first practical stored-program computer
  1951 ─── UNIVAC I — first commercial computer sold (to US Census Bureau)
  1952 ─── IAS machine (Princeton) — Von Neumann's own implementation
```

---

## John von Neumann (1903–1957)

### Bio Snapshot

Hungarian-American mathematician. Child prodigy — memorized phone books for amusement. Budapest, Berlin, Hamburg, then Princeton's Institute for Advanced Study from 1933. Contributions to: set theory (axiomatization), quantum mechanics (Hilbert space formalism), game theory (minimax theorem), economics (general equilibrium), fluid dynamics (shock waves), and computing. Died of cancer (possibly from Los Alamos radiation exposure) at 53.

### The Architecture

The 1945 "First Draft of a Report on the EDVAC" is the founding document of computer architecture. It describes a machine that stores both programs and data in the same memory — and specifies the components that every modern computer still uses.

```
VON NEUMANN ARCHITECTURE (1945)
================================

  ┌─────────────────────────────────────────────────────────────────┐
  │                    VON NEUMANN MACHINE                          │
  │                                                                 │
  │  ┌────────────────────────────────────────────────────────┐     │
  │  │                    CENTRAL PROCESSING UNIT             │     │
  │  │                                                        │     │
  │  │   ┌──────────────────┐     ┌────────────────────────┐ │     │
  │  │   │   CONTROL UNIT   │     │     ARITHMETIC LOGIC   │ │     │
  │  │   │                  │←───→│         UNIT           │ │     │
  │  │   │ Fetches, decodes, │     │                        │ │    │
  │  │   │ sequences instrs │     │ ADD, SUB, MUL, DIV     │ │     │
  │  │   │                  │     │ AND, OR, NOT, XOR      │ │     │
  │  │   │ PC (program ctr) │     │ Comparison, shifts     │ │     │
  │  │   │ IR (instr reg)   │     │ Registers (fast storage)│ │    │
  │  │   └──────────────────┘     └────────────────────────┘ │     │
  │  └────────────────────────────────────────────────────────┘     │
  │                    ↑                                            │
  │                    │ Memory Bus                                  │
  │                    ↓                                            │
  │  ┌────────────────────────────────────────────────────────┐     │
  │  │                      MEMORY                            │     │
  │  │                                                        │     │
  │  │    DATA and INSTRUCTIONS stored together               │     │
  │  │    Addressed linearly: cell 0, cell 1, ...             │     │
  │  │    CPU cannot distinguish data cell from code cell     │     │
  │  │    (this is the key insight AND the key vulnerability) │     │
  │  └────────────────────────────────────────────────────────┘     │
  │                    ↑                   ↓                        │
  │              ┌─────────┐         ┌──────────┐                   │
  │              │  INPUT  │         │  OUTPUT  │                   │
  │              └─────────┘         └──────────┘                   │
  └─────────────────────────────────────────────────────────────────┘

  THE FETCH-DECODE-EXECUTE CYCLE:
    1. FETCH:   Read instruction at address in PC → load into IR
    2. DECODE:  Interpret opcode and operands
    3. EXECUTE: ALU performs operation or memory access
    4. UPDATE:  PC incremented (or set by branch instruction)
    Repeat forever.
```

**What made it genuinely hard to conceive**: Before Von Neumann's document, computers were programmed by rewiring — plugboards, patch cables, switches. The program was in the machine's wiring, not in memory. ENIAC had 6,000 switches and required days to repatch for a new problem. The insight of storing the program in memory alongside data meant:
- Programs could be loaded and swapped like data
- A program could modify its own instructions (self-modifying code)
- One machine could simulate another (the UTM made physical)

**The Von Neumann bottleneck**: Because CPU and memory share a single bus, the CPU constantly waits for memory fetches. Every modern CPU architecture (pipelines, caches, branch predictors, out-of-order execution) is an attempt to paper over this fundamental bottleneck. The bottleneck is not a bug — it is an inescapable consequence of the architecture.

### Von Neumann's Broader Contributions

Von Neumann understood that the computer needed software infrastructure, not just hardware:

- **Sorting networks**: He worked on efficient sorting algorithms for EDVAC
- **Merge sort**: He invented merge sort specifically for use with tape drives (external sorting)
- **Monte Carlo methods**: He and Ulam developed Monte Carlo simulation while at Los Alamos — random sampling to solve problems intractable by direct calculation
- **Self-reproducing automata**: His cellular automaton work (completed posthumously by Burks) proved that machines could in principle reproduce themselves — precursor to von Neumann probes and artificial life research

---

## John Atanasoff (1903–1995) and Clifford Berry (1918–1963)

### The ABC Computer

Atanasoff was an Iowa State physicist frustrated by the tedium of solving systems of linear equations by hand for his dissertation work. In the winter of 1937–38, driving through Illinois, he conceived the key principles of an electronic digital computer. He and his graduate student Berry built the Atanasoff-Berry Computer (ABC) between 1939 and 1942.

```
ABC (ATANASOFF-BERRY COMPUTER) — KEY INNOVATIONS
==================================================

  Electronic:     Vacuum tubes for computation (not mechanical relays)
  Binary:         All arithmetic in base 2 (not decimal)
  Capacitor drum: 60 capacitors on rotating drum = memory
  Regenerative:   Capacitors refreshed every rotation (DRAM ancestor)
  Card reader:    Intermediate results recorded on spark-burned cards

  Limitations:
    - Could only solve systems of linear equations
    - Not programmable in the general sense
    - Could not store its own program
    - Required manual setup for each problem step
```

**The patent dispute**: Mauchly visited Atanasoff in June 1941 and saw the ABC. He later denied being influenced by it. The 1973 court case *Honeywell Inc. v. Sperry Rand Corp.* voided the ENIAC patent on grounds that Atanasoff had priority on the basic electronic computer concept, citing Mauchly's visit. This is still disputed.

**Berry's fate**: Clifford Berry, the graduate student who built the ABC, died in 1963 at 45 — ruled suicide, but circumstances were suspicious. He never received significant credit during his lifetime.

---

## J. Presper Eckert (1919–1995) and John Mauchly (1907–1980)

### ENIAC

ENIAC (Electronic Numerical Integrator and Computer) was built at the University of Pennsylvania's Moore School of Electrical Engineering under Army contract during WWII. Its primary purpose: computing artillery firing tables. It was completed in late 1945, too late for the war.

```
ENIAC — THE NUMBERS
====================

  Weight:         30 tons
  Tubes:          17,468 vacuum tubes
  Diodes:         7,200
  Resistors:      70,000
  Capacitors:     10,000
  Speed:          5,000 additions/second, 357 multiplications/second
  Memory:         20 ten-digit decimal numbers
  Power:          150 kilowatts
  Footprint:      1,800 square feet
  Programming:    Plugboards and switches — days to reprogram
  Cooling:        Constant maintenance — tubes burned out daily
```

```
PROGRAMMING ENIAC
==================

  BEFORE: (plugboard programming)
  ─────────────────────────────────
  Operator physically cables accumulators together.
  Sets decade ring switches to establish constants.
  Routes signals from accumulator to accumulator.
  One problem type = one wiring configuration.
  Reprogramming: days.

  AFTER: (1948 "Read Only Storage" conversion)
  ──────────────────────────────────────────────
  Eckert and others added a function table modification:
  programs could be stored in function tables (read-only).
  Loading a new program: hours instead of days.
  Not quite stored-program, but a step toward it.
```

**Eckert's key technical insight**: He insisted on conservative design margins for vacuum tubes — operating them at 25% of rated voltage and current. This cut the failure rate from tubes-per-hour to roughly one per week, making the machine practical. Most engineers assumed vacuum tubes were too unreliable for large-scale computation. Eckert proved them wrong through engineering discipline.

**Mauchly's role**: Conceptual and specification. Mauchly had the vision of a general-purpose electronic computer and wrote the initial proposal. Eckert led the engineering.

### UNIVAC

After ENIAC, Eckert and Mauchly founded Eckert-Mauchly Computer Corporation. Their UNIVAC I (1951) was:
- The first commercial computer sold
- Delivered to the US Census Bureau (same customer as Hollerith)
- Used magnetic tape for data storage (not punched cards)
- Famous for predicting Eisenhower's 1952 election victory on live TV (CBS)

IBM acquired the company and incorporated UNIVAC's architecture concepts. The "IBM vs. UNIVAC" competition established IBM's dominance for 30 years.

---

## Konrad Zuse (1910–1995)

### Bio Snapshot

German civil engineer, disgusted by the tedious calculations required for structural engineering. Built his computers in his parents' living room in Berlin using salvaged phone relays. Worked in near-total isolation from Allied computing developments due to WWII.

### The Z Series

```
ZUSE Z-SERIES: MILESTONES
==========================

  Z1 (1936–38): Mechanical. Binary floating-point. Programmable via
                punched holes in discarded 35mm film. Never worked
                reliably (mechanical tolerances).

  Z2 (1939):    Hybrid: relay arithmetic unit, mechanical memory.
                Proof-of-concept for relay approach.

  Z3 (1941):    All-relay. Binary. Floating-point. Programmable from
                punched film tape. 2,600 relays.
                ─── FIRST WORKING PROGRAMMABLE COMPUTER ───
                Destroyed in Berlin bombing, 1944.
                Replica at Deutsches Museum, Munich.

  Z4 (1944–45): Relay-based. Survived war in Bavarian Alps.
                Rented to ETH Zurich 1950–1955.
                Only computer in continental Europe for years.
```

**Z3's significance**: It was Turing-complete in principle (though Zuse may not have known this at the time — he was isolated from British theoretical work). It performed floating-point arithmetic in binary — a design choice not taken by ENIAC (which used decimal). Binary floating-point became the basis for all modern FPUs.

### Plankalkül

Zuse conceived **Plankalkül** (Plan Calculus) in 1945 — the first high-level programming language, designed for the Z4. It included:
- Array types with multiple indices
- Nested data structures
- Assignment and conditionals
- Floating-point operations

It was not published until 1972 and not implemented until 1975 — too late to influence language design directly. But it demonstrates that Zuse was thinking in terms of software abstraction, not just hardware, at the very moment the hardware was being built.

---

## Comparison Table

| Figure | Machine | Year | Medium | Programmable? | Stored-Program? |
|--------|---------|------|--------|--------------|-----------------|
| Atanasoff+Berry | ABC | 1942 | Electronic | No (special-purpose) | No |
| Zuse | Z3 | 1941 | Relay | Yes (punched film) | No |
| Aiken | Mark I | 1944 | Relay | Yes (punched tape) | No |
| Eckert+Mauchly | ENIAC | 1945 | Electronic | Yes (plugboard) | No (partially, post-1948) |
| Von Neumann / Manchester | Manchester Baby | 1948 | Electronic | Yes | Yes |

---

## Who to Cite for What

| Concept | Figure |
|---------|--------|
| Stored-program architecture (concept) | Von Neumann (1945 draft) |
| Stored-program architecture (first working) | Kilburn + Williams (Manchester Baby, 1948) |
| First electronic components for computation | Atanasoff (ABC, 1942) |
| First programmable computer | Zuse (Z3, 1941) |
| First general-purpose electronic computer | Eckert+Mauchly (ENIAC, 1945) |
| First commercial computer | Eckert+Mauchly (UNIVAC, 1951) |
| Merge sort | Von Neumann |
| Monte Carlo methods | Von Neumann + Ulam |
| Binary floating-point | Zuse (Z1/Z3 design) |
| The Von Neumann bottleneck | Von Neumann architecture (unintended consequence) |

---

## Common Confusion Points

**"Von Neumann invented the stored-program computer."**
He wrote the definitive architectural specification (1945). The first machine to actually run a stored program was the Manchester Baby (1948), designed by Kilburn and Williams. Von Neumann's IAS machine at Princeton came later (1952). He described the architecture before anyone built it.

**"ENIAC was the first computer."**
Depends on definition. Zuse's Z3 (1941) was programmable but relay-based and destroyed. Atanasoff's ABC (1942) was electronic but special-purpose. Colossus (1943) was electronic and somewhat programmable but secret and special-purpose. ENIAC (1945) was the first general-purpose, electronic, programmable computer — and the first publicly demonstrated.

**"Von Neumann bottleneck is a fundamental limit."**
Yes — and 80 years of CPU design is essentially the history of working around it. Caches (reduce memory latency), pipelines (overlap fetch/decode/execute), out-of-order execution (execute instructions whose operands are ready while waiting for others), branch prediction (speculatively execute the likely branch), SIMD (do many operations in one fetch cycle) — all are responses to the bottleneck Von Neumann's architecture creates.

**"The ENIAC patent dispute matters now."**
Historically important — the 1973 ruling that Honeywell won (voiding Sperry Rand's ENIAC patent) prevented any single company from owning the concept of a programmable electronic digital computer. It kept the field open. Without that ruling, every computer might have required a patent license to IBM/Sperry.
