# ISA Fundamentals: RISC vs CISC

## What an ISA Is

The Instruction Set Architecture is the contract between software and hardware. It specifies:

1. The set of instructions (opcodes and their semantics)
2. The programmer-visible register file
3. The data types supported (integer widths, float formats)
4. The memory model (byte ordering, alignment requirements, atomicity)
5. Addressing modes (how operands are specified)
6. Exception and interrupt model
7. Privilege levels / protection model

Everything below the ISA is the microarchitecture — invisible to correctly-written software, but governing every cycle of execution.

```
+-----------------------------------------------------------------------+
|                          ISA DESIGN SPACE                             |
|                                                                       |
|  RISC                              CISC                               |
|  (Reduced Instruction Set)         (Complex Instruction Set)          |
|                                                                       |
|  "Simple instructions,             "Complex instructions,             |
|  execute in one cycle"             do more per instruction"           |
|                                                                       |
|  ARM64 / RISC-V / MIPS /           x86-64 / x86 / VAX /              |
|  SPARC / PowerPC                   68000 / PDP-11                     |
|                                                                       |
|  Fixed instruction size            Variable instruction size          |
|  Load/store architecture           Register-memory operations         |
|  Many registers (≥32)              Fewer registers (8–16 general)     |
|  Simple addressing modes           Rich addressing modes              |
|  Compiler does the work            Hardware does the work             |
|                                                                       |
|  History: IBM 801 (Patterson       History: IBM 360, PDP-11,          |
|  & Hennessy, Berkeley, Stanford,   VAX, Intel 8086 → x86 → x86-64   |
|  ~1980)                            (backward compat chain)            |
+-----------------------------------------------------------------------+
```

---

## RISC vs CISC: The Key Differences

```
+--------------------------------------------------------------------+
| ATTRIBUTE         | RISC                  | CISC                  |
|-------------------|-----------------------|-----------------------|
| Instruction size  | Fixed (4 bytes)       | Variable (1–15 bytes) |
| Instructions/ISA  | ~100–200              | 1000+ for x86-64      |
| Memory access     | Only LOAD/STORE       | Any instruction can   |
|                   | instructions          | access memory         |
| Register count    | 32 GP registers       | 8 (x86) – 16 (x86-64)|
|                   | (ARM64: x0–x30 + SP)  | (+ segment, flags)    |
| Addressing modes  | Simple: [base+offset] | Complex: [base+       |
|                   |                       | index*scale+offset]   |
| Decode complexity | Trivial (fixed width  | Complex; variable     |
|                   | → fixed decode time)  | length; multiple      |
|                   |                       | decoders needed       |
| Multi-cycle ops   | Few (FP/divide)       | Many CISC instructions |
|                   |                       | expand to many cycles |
| Code density      | Lower (4 bytes/instr) | Higher (avg ~3 bytes  |
|                   |                       | on x86)               |
+--------------------------------------------------------------------+
```

---

## Instruction Format

### RISC-V Fixed Format (32-bit instructions)

```
  R-TYPE (register-register operations):
  31      25 24   20 19   15 14  12 11    7 6      0
  +--------+-------+-------+------+-------+--------+
  | funct7 |  rs2  |  rs1  |funct3|  rd   | opcode |
  +--------+-------+-------+------+-------+--------+
    7 bits   5 bits  5 bits  3 bits  5 bits  7 bits

  I-TYPE (immediate / loads):
  31              20 19   15 14  12 11    7 6      0
  +----------------+-------+------+-------+--------+
  |   imm[11:0]    |  rs1  |funct3|  rd   | opcode |
  +----------------+-------+------+-------+--------+
       12 bits       5 bits  3 bits  5 bits  7 bits

  Fixed 32-bit width: one fetch cycle, trivial decode.
  Decode = split fixed-width fields. No length disambiguation.
```

### x86-64 Variable Format

```
  x86-64 instruction can be 1 to 15 bytes:

  [Prefixes 0-4 bytes] [REX 0-1 byte] [Opcode 1-3 bytes]
  [ModRM 0-1 byte] [SIB 0-1 byte] [Disp 0,1,2,4 bytes]
  [Immediate 0,1,2,4,8 bytes]

  Example: simple ADD
  48 01 C3   = REX.W + ADD r/m64, r64

  Example: complex memory operation
  42 8B 84 D5 80 00 00 00
  = MOV eax, [rbp + r10*8 + 0x80]
    REX + opcode + ModRM + SIB + 32-bit displacement

  The decoder must figure out length BEFORE decode.
  This requires complex look-ahead logic in hardware.
  Intel allocates significant transistor budget to decoding.
  Average x86-64 instruction ~3 bytes in practice; worst case 15.
```

---

## Addressing Modes

```
  REGISTER DIRECT:
  ADD R1, R2, R3         "R3 = R1 + R2"         (RISC)
  ADD eax, ebx           "eax += ebx"             (x86)

  IMMEDIATE:
  ADD R1, R2, #42        "R1 = R2 + 42"           (ARM)
  ADD eax, 42            "eax += 42"               (x86)

  REGISTER INDIRECT (load/store):
  LDR X0, [X1]           "X0 = Mem[X1]"           (ARM64)
  MOV eax, [rbx]         "eax = Mem[rbx]"          (x86)

  BASE + DISPLACEMENT:
  LDR X0, [X1, #8]       "X0 = Mem[X1+8]"         (ARM64)
  MOV eax, [rbx+8]       "eax = Mem[rbx+8]"        (x86)

  BASE + INDEX * SCALE + DISPLACEMENT (x86 only):
  MOV eax, [rbx + rcx*4 + 16]
  "eax = Mem[rbx + rcx*4 + 16]"
  Useful for: array[base + index * sizeof(element)]
  in one instruction

  LOAD-STORE RESTRICTION (RISC):
  All memory access through LDR/STR only.
  Arithmetic ops only on registers.
  ADD R1, R2, [R3]  ← ILLEGAL in ARM64 / RISC-V
  Must be: LDR R4, [R3]   then  ADD R1, R2, R4
```

---

## Register Files

```
  x86-64 GENERAL PURPOSE:            ARM64 GENERAL PURPOSE:
  RAX RBX RCX RDX                    X0–X7   (arguments/return values)
  RSI RDI RSP RBP                    X8–X18  (caller-saved temporaries)
  R8–R15                             X19–X28 (callee-saved)
  = 16 registers, 64-bit             X29     (frame pointer)
                                     X30     (link register / return addr)
  Legacy sub-registers:              SP      (stack pointer)
  EAX (low 32 of RAX)                XZR/WZR (zero register — hardwired 0)
  AX  (low 16 of RAX)                = 31 registers + zero register
  AL  (low 8 of RAX)
  AH  (bits 8–15 of AX)              W-prefix: 32-bit view of same register
                                     W0 = low 32 bits of X0

  x86 BAGGAGE:                       ARM64 ADVANTAGE:
  AX/BX/CX/DX had SPECIFIC           All registers general-purpose.
  implicit meanings (AX = accumulator No implicit register usage.
  for multiply, CX = count for LOOP). More compiler flexibility.
  These survive in x86-64 calling
  conventions (RAX = return value,
  RCX = 4th arg on Windows).

  RISC-V GENERAL PURPOSE:
  x0  hardwired zero (always 0, writes discarded)
  x1  return address (ra)
  x2  stack pointer (sp)
  x3  global pointer (gp)
  x4  thread pointer (tp)
  x5–x7   temporaries (t0–t2)
  x8–x9   saved registers (s0–s1; x8 also frame pointer)
  x10–x17 function arguments/return values (a0–a7)
  x18–x27 saved registers (s2–s11)
  x28–x31 temporaries (t3–t6)
```

---

## ISA Evolution and Backward Compatibility

```
  The x86 Compatibility Chain:

  8086 (1978): 16-bit, 1 MB addressable, segmented memory
       |
       v
  80286 (1982): Protected mode, 16 MB
       |
       v
  80386 (1985): 32-bit (IA-32), 4 GB, flat memory, paging
       |
       v
  Pentium, P6, Pentium 4...
       |
       v
  AMD64 / x86-64 (AMD Opteron, 2003):
    64-bit long mode, 16 EB addressable
    Extended to 16 GP registers (R8–R15)
    Intel adopted as Intel 64 (2004)
       |
       v
  Today: every x86-64 CPU runs:
    MS-DOS .COM files (16-bit real mode)
    32-bit Windows programs (IA-32)
    64-bit programs (x86-64)
  All on the same hardware.

  COST: The decode logic must handle all these modes.
  Intel's front-end is enormously complex because of this legacy.
  Estimated: 50,000+ opcodes when you count all encodings/prefixes.

  ARM's escape hatch:
  AArch64 (ARMv8+) is a CLEAN BREAK from 32-bit ARM.
  Different instruction encoding, no baggage.
  32-bit ARM apps run in a compatibility layer (AArch32 mode)
  but the 64-bit ISA is clean.
```

---

## Modern Reality: CISC Frontend, RISC Backend

```
  MODERN x86 EXECUTION:

  +------------------+
  | x86-64 CISC ISA  |  "What the programmer / compiler sees"
  +------------------+
           |
           | DECODE (Front-end: complex, power-hungry)
           v
  +------------------+
  | MICRO-OPS (μops) |  Simple, RISC-like internal operations
  +------------------+  Intel calls these "uops" (micro-operations)
  | ADD rax, rbx     |  → 1 uop
  | IMUL [mem], rcx  |  → 2 uops (load + multiply)
  | REP MOVS         |  → microcode (many uops)
           |
           | ISSUE (Out-of-order engine)
           v
  +------------------+
  | EXECUTION UNITS  |  Integer, FP, Load, Store, Branch
  +------------------+

  The conversion to micro-ops is the DECODE step.
  After that, the execution engine is essentially RISC.
  "RISC-ification" at decode time.

  Intel: 4-6 complex decoders per core, can decode 4 uops/cycle typically
  AMD Zen 4: 4 decoders, up to 4 ops/cycle, op cache for hot loops
```

---

## ISA Comparison Table

| Attribute | x86-64 | ARM64 (AArch64) | RISC-V (RV64GC) |
|-----------|--------|-----------------|------------------|
| Origin | Intel 8086 (1978) | ARM Ltd (1985) | UC Berkeley (2010) |
| Instruction width | 1–15 bytes | 4 bytes (Thumb2: 2/4) | 4 bytes (C ext: 2) |
| GP registers | 16 (64-bit) | 31 (64-bit) + zero | 31 (64-bit) + zero |
| Memory model | Strong (TSO) | Weak (with barriers) | Weak (RVWMO) |
| FP registers | xmm0–15 (SSE) / zmm0–31 (AVX-512) | v0–v31 (128-bit) | f0–f31 (float) |
| ISA owner | Intel + AMD (x86-64 ABI) | Arm Holdings (licensed) | RISC-V International (open) |
| Primary use | Server, desktop, laptop | Mobile, embedded, Apple Silicon, servers | IoT, academic, growing |
| Royalties | Implicitly via x86 IP | Yes (Arm licenses) | None — open standard |

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| Why does x86 need so many decoders? | Variable instruction width requires look-ahead; 1–15 bytes per instruction |
| Why does ARM64 have 31 registers vs x86's 16? | Clean RISC design; more registers = fewer spills to stack |
| What is a micro-op? | An internal RISC-like operation that x86 CISC instructions are decoded into |
| Why is RISC-V royalty-free? | Open ISA standard — no company owns it |
| What does "load-store architecture" mean? | Only LOAD and STORE instructions access memory; ALU ops are register-only |
| What is the TSO memory model? | Total Store Order — Intel x86's strong consistency guarantee; stores globally visible in order |
| Why do compilers prefer registers over memory? | Register access: 0 cycles; L1 cache: 4 cycles; DRAM: 100 cycles |

---

## Language Memory Models → ISA Fence Instructions

Every concurrent programmer needs to map: language ordering guarantee → ISA fence instruction → hardware memory model. The chain is universal across language ecosystems.

```
  LANGUAGE LEVEL — acquire/release semantics

  C++:   std::atomic<T> with memory_order_acquire / memory_order_release
         std::atomic_thread_fence(memory_order_seq_cst)
  Java:  volatile fields (JMM happens-before)
         synchronized / VarHandle.setVolatile / VarHandle.getAcquire
  Go:    sync.Mutex, sync/atomic, channel send/receive
  Rust:  std::sync::atomic::Ordering::{Acquire, Release, SeqCst}
  C#:    volatile, Interlocked, Thread.MemoryBarrier()

  All provide acquire/release semantics at the language level.
  The COMPILER maps these to ISA fence instructions.

         ↓  compiles to

  ISA LEVEL — fence instructions

  x86-64:  MFENCE (full), SFENCE (stores), LFENCE (loads)
           LOCK prefix on RMW implies full fence
           (TSO is strong enough that acquire/release
            compiles to NO fence on x86 in many cases)

  ARM64:   LDAR  (load-acquire)    — pairs with release stores
           STLR  (store-release)   — pairs with acquire loads
           DMB ISH  (full barrier) — for seq_cst / full fence

  RISC-V:  FENCE r,rw / FENCE rw,w (RVWMO acquire/release)
           FENCE.TSO (total store order subset)

         ↓  governs

  HARDWARE LEVEL — coherence model

  x86 TSO:    near-sequential; store buffer is the only relaxation
  ARM WMO:    aggressive reordering; fences are load-bearing
  RISC-V RVWMO: weak by default; composable fence types

  KEY INSIGHT:
  A C++ memory_order_acquire on x86 compiles to a plain load
  (TSO does the work). The same code on ARM64 compiles to LDAR
  (explicit hardware instruction). The language guarantee is
  identical; the hardware cost is not.

  A memory_order_seq_cst load on x86 requires MFENCE before
  the load. On ARM64 it is LDAR. Both are more expensive than
  acquire/release — only use seq_cst when you actually need it.
```

---

## Common Confusion Points

**The "RISC is faster" claim is 1980s era**: At the time, RISC chips had 3–5× higher clock rates than CISC. Today, Intel and AMD implement RISC micro-ops internally after decode. The real advantages of ARM64 today are power efficiency (simpler decode logic = fewer transistors = less heat) and clean register file design.

**x86-64 backward compatibility is both asset and liability**: Every new CPU generation must run MSDOS code. This forces the front-end to maintain enormous legacy complexity. But it means all existing software runs without recompilation — for server/desktop use, this is a massive ecosystem moat.

**"RISC = fewer instructions" is misleading**: RISC-V with the G profile includes 100+ instructions (base integer + multiply + atomic + FP + compressed). "Reduced" referred to the original philosophy of one-cycle instructions and simple operations, not a literally small count.

**Thumb/Thumb2 are NOT RISC**: ARM's 16-bit Thumb encoding and mixed 16/32-bit Thumb2 encoding sacrifice the fixed-width property for code density. Most ARM embedded code runs in Thumb2 mode; AArch64 is fixed-width 32-bit only.

**ISA specifies atomicity guarantees**: The memory model part of the ISA matters enormously for concurrent programming. x86 TSO gives you near-sequential consistency for free; ARM's weak model requires explicit fences (`DMB`, `DSB`). C# `Interlocked` operations compile to different instruction sequences on each architecture.
