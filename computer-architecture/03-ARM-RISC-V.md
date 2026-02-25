# ARM and RISC-V: Modern RISC Designs

## Overview

ARM64 (AArch64) dominates mobile and has taken a large slice of the server and desktop market via Apple Silicon and AWS Graviton. RISC-V is the open-source ISA that has become the standard for embedded systems and is growing toward datacenter use. Both are load-store RISC architectures with fixed 32-bit instruction encoding, but they made different design choices.

```
+-----------------------------------------------------------------------+
|                    ARM64 vs RISC-V COMPARISON                         |
|                                                                       |
|  ARM64 (AArch64)                  RISC-V (RV64GC)                    |
|  ----------------                 ----------------                   |
|  ARM Holdings, licensed           RISC-V International, open         |
|  Fixed 32-bit instructions        Fixed 32-bit (C ext: 16-bit)       |
|  31 GP registers + zero           31 GP registers + zero             |
|  32 FP/SIMD registers (128-bit)   32 FP registers (64-bit)           |
|  Conditional execution flags      No condition codes                 |
|  Hardware divide (UDIV/SDIV)      M extension for multiply/divide    |
|  Pointer auth (PAC)               Pointer masking (CFI via SW)       |
|  SVE/SVE2: scalable vectors       V extension: scalable vectors       |
|  A profile, R profile, M profile  RV32, RV64, RV128 + extensions     |
|  IP royalties required            Free to implement                  |
+-----------------------------------------------------------------------+
```

---

## ARM64 (AArch64) Architecture

AArch64 is the 64-bit ARM ISA introduced with ARMv8 (2013). It is a clean break from 32-bit ARM (AArch32) — not an extension, a separate ISA.

### Register File

```
  GENERAL-PURPOSE REGISTERS (31 + zero):

  Name    Role                        Notes
  ----    ----                        -----
  X0–X7   Arguments / return values   Caller-saved
  X8      Indirect result location    / 8th syscall argument
  X9–X15  Caller-saved temporaries
  X16–X17 Intra-procedure-call scratch (IP0, IP1)
  X18     Platform-specific (Windows TEB pointer / reserved)
  X19–X28 Callee-saved
  X29     Frame pointer (FP)
  X30     Link register (LR) — return address
  SP      Stack pointer (not X31 in most contexts)
  XZR     Zero register (reads = 0, writes = discard)

  W-prefix: 32-bit view of X registers
  W0 = low 32 bits of X0; writing W0 zero-extends to X0

  FLOATING-POINT / SIMD (32 × 128-bit V registers):
  V0–V7:  FP arguments / return values
  V8–V15: Callee-saved (low 64 bits only)
  V16–V31: Caller-saved

  Register aliases by access width:
  B0 = 8-bit view    H0 = 16-bit    S0 = 32-bit
  D0 = 64-bit        Q0 = 128-bit   V0 = full vector
```

### Key Instruction Classes

```
  LOAD / STORE (only instructions that access memory):
  LDR X0, [X1]           X0 = Mem[X1]
  LDR X0, [X1, #8]       X0 = Mem[X1 + 8]       (offset)
  LDR X0, [X1, X2]       X0 = Mem[X1 + X2]      (register offset)
  LDR X0, [X1, X2, LSL #3]  X0 = Mem[X1 + X2*8] (scaled index)
  LDRB W0, [X1]          8-bit load, zero-extend to W0
  LDRSB X0, [X1]         8-bit load, sign-extend to X0
  LDP X0, X1, [X2]       Load pair: X0=Mem[X2], X1=Mem[X2+8]

  STR X0, [X1]           Mem[X1] = X0
  STP X29, X30, [SP, #-16]!  Store pair + pre-decrement SP

  PRE/POST INDEX ADDRESSING (ARM64 exclusive):
  LDR X0, [X1, #8]!      Pre-index:  X1 += 8, then X0 = Mem[X1]
  LDR X0, [X1], #8       Post-index: X0 = Mem[X1], then X1 += 8

  ARITHMETIC (register only):
  ADD X0, X1, X2         X0 = X1 + X2
  ADD X0, X1, X2, LSL #2 X0 = X1 + X2*4   (shifted register)
  ADD X0, X1, #42        X0 = X1 + 42      (immediate, 12-bit)
  MADD X0, X1, X2, X3    X0 = X1*X2 + X3   (multiply-add)
  MSUB X0, X1, X2, X3    X0 = X3 - X1*X2
  UDIV X0, X1, X2        X0 = X1 / X2 (unsigned)
  CLZ  X0, X1            Count leading zeros

  BRANCHES:
  B  label               Unconditional branch
  BL label               Branch with link (call — saves return addr in X30)
  RET                    Return: branch to X30 (link register)
  RET X17                Return to arbitrary register
  BR X0                  Branch to register (indirect call)
  BLR X0                 Branch with link to register

  B.cond label:          B.EQ, B.NE, B.LT, B.GT, B.LE, B.GE
  CBZ X0, label          Compare and branch if zero
  CBNZ X0, label         Compare and branch if non-zero
  TBZ X0, #3, label      Test bit 3 and branch if zero
```

### ARM64 Calling Convention (AAPCS64)

```
  ARGUMENTS:
  Integers/pointers:   X0–X7  (8 registers)
  Floats:              V0–V7  (8 registers)
  Additional args:     Stack (right to left, 8-byte aligned)

  RETURN VALUE:
  Integer:             X0 (+ X1 for 128-bit)
  Float:               V0 (+ V1 for larger)

  FRAME SETUP (typical):
  STP X29, X30, [SP, #-16]!   ; Push frame pointer and link register
  MOV X29, SP                  ; Set frame pointer to current SP

  FRAME TEARDOWN:
  MOV SP, X29                  ; Restore SP
  LDP X29, X30, [SP], #16     ; Restore FP and LR
  RET                          ; Return

  STACK: 16-byte aligned at all public function boundaries
  Red zone: none in AArch64 procedure call standard
            (Apple's ABI also has no red zone)
```

### ARM64 System Features

```
  POINTER AUTHENTICATION (ARMv8.3):
  PACIA X0, X1    Sign pointer in X0 using key A + context X1
  AUTIA X0, X1    Authenticate pointer
  RETAA           Authenticate and return (CFI mitigation)
  Used by: Apple's PAC, Linux kernel, Windows ARM

  MEMORY ORDERING / BARRIERS:
  DMB ISH         Data Memory Barrier (inner shareable domain)
  DSB ISH         Data Synchronization Barrier
  ISB             Instruction Synchronization Barrier (flush pipeline)
  LDAR X0, [X1]  Load-Acquire (ordering: no load/store after)
  STLR X0, [X1]  Store-Release (ordering: no load/store before)
  These replace volatile + lock in C# when writing low-level concurrent code.

  EXCLUSIVE LOADS/STORES (atomic operations):
  LDXR X0, [X1]  Load-exclusive
  STXR W2, X0, [X1]  Store-exclusive; W2=0 on success, 1 on failure
  Used for CAS-like operations, lock-free algorithms.
```

---

## RISC-V Architecture

RISC-V is an open ISA developed at UC Berkeley starting 2010. "Open" means anyone can implement it royalty-free. This is a structural difference from ARM (which you license from Arm Holdings).

### ISA Modularity

```
  RISC-V is MODULAR — a base ISA plus optional extensions.

  BASE ISA:
  RV32I   32-bit integer instructions (47 instructions)
  RV64I   64-bit integer instructions (adds 64-bit ops to RV32I)
  RV128I  128-bit (future)

  STANDARD EXTENSIONS:
  M   Integer multiply and divide  (MULW, DIVW, REMW)
  A   Atomic operations            (LR/SC, AMO* instructions)
  F   Single-precision FP          (fadd.s, fmul.s, etc.)
  D   Double-precision FP          (fadd.d, fmul.d, etc.)
  C   Compressed (16-bit) instructions (code density)
  G = IMAFD: the "general" profile (what Linux targets)

  LATER EXTENSIONS:
  V   Vector instructions          (scalable SIMD)
  B   Bit manipulation             (RISC-V version of BMI)
  H   Hypervisor support
  Zicsr  Control/Status Registers
  Zifencei  Instruction fetch fence (self-modifying code)

  MARKETING: "RV64GC" = 64-bit + IMAFD + Compressed
  = what embedded Linux typically uses.
```

### Register File

```
  ABI NAME    USAGE                           SAVER
  --------    -----                           -----
  x0  zero    Hardwired zero (reads=0)        —
  x1  ra      Return address                  Caller
  x2  sp      Stack pointer                   Callee
  x3  gp      Global pointer                  —
  x4  tp      Thread pointer                  —
  x5  t0      Temporary / alternate link reg  Caller
  x6  t1      Temporary                       Caller
  x7  t2      Temporary                       Caller
  x8  s0/fp   Saved / frame pointer           Callee
  x9  s1      Saved                           Callee
  x10 a0      Arg 0 / return value 0          Caller
  x11 a1      Arg 1 / return value 1          Caller
  x12 a2      Argument 2                      Caller
  x13 a3      Argument 3                      Caller
  x14 a4      Argument 4                      Caller
  x15 a5      Argument 5                      Caller
  x16 a6      Argument 6                      Caller
  x17 a7      Argument 7 / syscall number     Caller
  x18 s2–s11  Saved registers                 Callee
  x28 t3–t6   Temporaries                     Caller

  FP registers: f0–f31 (with D extension, all 64-bit)
  fa0–fa7: float arguments / return values
  fs0–fs11: callee-saved float
  ft0–ft11: caller-saved float temporaries
```

### RISC-V Instruction Formats

```
  RISC-V has 6 instruction formats, all 32-bit:

  R-TYPE: [funct7:7][rs2:5][rs1:5][funct3:3][rd:5][opcode:7]
  I-TYPE: [imm[11:0]:12][rs1:5][funct3:3][rd:5][opcode:7]
  S-TYPE: [imm[11:5]:7][rs2:5][rs1:5][funct3:3][imm[4:0]:5][opcode:7]
  B-TYPE: Branch variant of S (target offset encoding)
  U-TYPE: [imm[31:12]:20][rd:5][opcode:7]
  J-TYPE: [imm:20][rd:5][opcode:7]

  Immediates are SIGN-EXTENDED from their field width.
  Immediate fields are split across non-contiguous bit positions
  (design choice: keep rd/rs1/rs2 at fixed positions for simpler decode)

  KEY INSTRUCTIONS (RV64I):
  LW  rd, imm(rs1)         Load word (32-bit, sign-extend)
  LD  rd, imm(rs1)         Load doubleword (64-bit)
  SD  rs2, imm(rs1)        Store doubleword
  ADD rd, rs1, rs2         rd = rs1 + rs2
  ADDI rd, rs1, imm        rd = rs1 + imm (12-bit sign-extended)
  ADDIW rd, rs1, imm       rd = SignExt32(rs1+imm) (32-bit add + extend)
  MUL rd, rs1, rs2         rd = low 64 bits of rs1*rs2  (M ext)
  DIV rd, rs1, rs2         rd = rs1 / rs2 signed         (M ext)
  AUIPC rd, imm            rd = PC + (imm << 12)  (PC-relative addressing)
  JAL  rd, label           rd = PC+4, PC = PC + offset  (jump + link)
  JALR rd, rs1, imm        rd = PC+4, PC = (rs1+imm) & ~1  (indirect jump)
  LR.D rd, (rs1)           Load-reserved (atomic)
  SC.D rd, rs2, (rs1)      Store-conditional (atomic)
  AMOADD.D rd, rs2, (rs1)  Atomic memory add
```

---

## Performance Comparison: ARM64 vs x86-64 vs RISC-V

```
+----------------------------------------------------------------------+
| ATTRIBUTE          | x86-64          | ARM64           | RISC-V      |
|--------------------|-----------------|-----------------|-------------|
| Code density       | Best (var width)| Good (Thumb2/C) | Good (C ext)|
| Decode complexity  | Very high       | Low             | Very low    |
| Power/perf         | Good (recent)   | Excellent       | Excellent   |
| Register count     | 16              | 31 + zero       | 31 + zero   |
| Memory ordering    | Very strong     | Weak (barriers) | Weak (RVWMO)|
| Atomics            | LOCK prefix     | LDXR/STXR       | LR/SC, AMO  |
| Vector/SIMD        | AVX-512         | NEON/SVE        | V extension |
| Royalties          | x86 IP required | Arm license fee | Free        |
| Major impls        | Intel, AMD      | Apple, Cortex,  | SiFive,     |
|                    |                 | Graviton        | Alibaba, T-Head |
| Dominant use       | Server/desktop  | Mobile, Mac, HPC| IoT, embedded|
+----------------------------------------------------------------------+
```

---

## Apple Silicon: ARM64 Done Right

Apple Silicon (M1/M2/M3/M4 series) is the current benchmark for single-thread performance.

```
  WHAT MAKES IT FAST:

  DECODE WIDTH:
  8-wide decode (M1/M2) — issues up to 8 instructions/cycle
  Compare: Intel Golden Cove: 6-wide
           AMD Zen 4: 4-wide

  OUT-OF-ORDER WINDOW:
  M1: ~630 ROB entries (reorder buffer)
  Compare: Intel Skylake: 224 ROB entries
  Larger window = more parallel execution visible to the OOO engine

  MEMORY SUBSYSTEM:
  Unified Memory Architecture: CPU and GPU share the same physical DRAM
  High-bandwidth (LPDDR5): 200 GB/s (M2 Max: 400 GB/s)
  L1 data cache: 192 KB per performance core (huge)
  L2 per-cluster: 12–16 MB (what Intel calls L3)
  System cache: 32 MB (like LLC but faster)

  PACKAGE:
  CPU + GPU + NPU + I/O on one die, chip-to-chip removed
  = eliminates PCIe latency for GPU communication
  = cache coherence between CPU and GPU memory

  PERFORMANCE CORES + EFFICIENCY CORES:
  M2: 4P + 4E (or more in Pro/Max/Ultra)
  P cores: high frequency, large OOO — for latency-sensitive work
  E cores: small, slow, power-efficient — for background tasks
  Analogous to Intel's P-core/E-core split (Alder Lake+)
```

---

## RISC-V in Practice

```
  CURRENT ECOSYSTEM (2024):

  EMBEDDED / IoT: Dominant new design space
    ESP32-C3, ESP32-C6 (Espressif): Wi-Fi + BT MCU on RV32
    GD32VF103 (GigaDevice): first commercial RV32 MCU
    Western Digital SweRV core: in storage controllers

  LINUX-CAPABLE:
    SiFive HiFive Unmatched: RV64GC developer board
    StarFive VisionFive 2: $70 SBC
    T-Head C908/C920 (Alibaba): server-class RV64

  CHINA STRATEGIC INVESTMENT:
    Alibaba, Huawei, multiple Chinese chip companies
    investing heavily in RISC-V to avoid ARM licensing
    in case of geopolitical restrictions

  GPU / AI ACCELERATORS:
    Esperanto ET-SoC-1: 1092 RV64 cores for ML inference
    Tenstorrent: RISC-V + custom tensor units

  EMULATION:
    QEMU supports RV32/RV64 completely
    Spike: official ISS (Instruction Set Simulator)
    RISC-V formal spec in Sail (executable formal model)
```

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| Why did ARM win mobile over x86? | Load-store simplicity → fewer transistors → better power/area |
| What is AArch64's zero register? | XZR — reads as 0, writes discarded; avoids needing a dedicated XOR-to-zero instruction |
| What is the ARM64 calling convention's argument limit before stack? | 8 integer (X0–X7) and 8 float (V0–V7) registers |
| What does LR/SC implement? | Load-Reserved / Store-Conditional — the basis for lock-free operations in RISC-V |
| What is RISC-V's minimal "Linux" profile? | RV64GC (RV64IMAFDC) |
| Why is RISC-V growing in China? | Geopolitical independence from ARM licensing |
| What is SVE? | Scalable Vector Extension — ARM SIMD with variable-width vectors (not fixed 128/256/512) |

---

## Common Confusion Points

**AArch64 ≠ AArch32**: They are different ISAs. AArch32 is 32-bit ARM (the old ISA). AArch64 is a clean redesign. A processor in AArch64 state cannot execute AArch32 instructions in the same execution state — it switches mode. Most new code targets AArch64 only.

**RISC-V zero register XZR is not a wasted register slot**: Having x0 hardwired to zero simplifies instruction encoding significantly. Many common patterns (clear a register: `ADD rd, x0, x0`, unconditional jump: `JALR x0, ra, 0`) become free. Every serious RISC ISA since MIPS has done this.

**ARM's SVE is not AVX**: AVX has fixed vector widths (128/256/512 bits). SVE has a variable width — the hardware implements some width (128–2048 bits in multiples of 128), and the code uses a predicate register to work on "vl" elements regardless of width. The same binary runs on any SVE implementation.

**RISC-V compressed (C extension) does not mean RISC-V is variable-width**: The C extension adds 16-bit COMPRESSED encodings of common instructions (25% of code in practice). The processor must detect whether it is reading a 16-bit or 32-bit instruction by looking at the low 2 bits (00, 01, 10 = 16-bit; 11 = 32-bit). It breaks the fixed-width property but for a meaningful code size reduction on embedded systems.

**Graviton vs Apple Silicon**: Both are ARM64 but very different designs. AWS Graviton (Neoverse N2/V2) is optimized for throughput and server workloads — many cores, moderate single-thread perf. Apple Silicon is optimized for peak single-thread performance with huge OOO windows and massive caches. Same ISA, wildly different microarchitectures.
