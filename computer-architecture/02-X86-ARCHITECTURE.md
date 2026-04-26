# x86 and x86-64 Architecture

## Overview

x86-64 (also called AMD64 or Intel 64) is the dominant ISA for servers, desktops, and laptops as of 2024. It is the target for every major compiler (GCC, Clang, MSVC), every major language runtime (JVM, V8, CPython, CLR), and every major server operating system. Linux, macOS, and Windows all run natively on x86-64 on the same binary-compatible ISA. Understanding its register file, instruction encoding, and calling conventions is essential for understanding performance, interop, and what any JIT or AOT compiler actually emits — whether you are writing C++, Java, Go, Python, or .NET.

```
+-----------------------------------------------------------------------+
|                    x86-64 ARCHITECTURE MAP                            |
|                                                                       |
|  EXECUTION MODES:                                                     |
|  Long Mode (64-bit)     Protected Mode (32-bit)     Real Mode (16-bit)|
|  x86-64 programs        32-bit Windows apps         DOS / BIOS        |
|  (what you care about)  (WoW64 compatibility layer) (legacy only)     |
|                                                                       |
|  REGISTER FILE (Long Mode):                                           |
|  16 × 64-bit GP registers: RAX RBX RCX RDX RSI RDI RSP RBP R8–R15  |
|  16 × 128-bit XMM (SSE): XMM0–XMM15                                 |
|  16 × 256-bit YMM (AVX): YMM0–YMM15 (extend XMM)                   |
|  32 × 512-bit ZMM (AVX-512): ZMM0–ZMM31                             |
|  + RFLAGS (status flags) + RIP (instruction pointer)                  |
|                                                                       |
|  MEMORY MODEL:                                                        |
|  Flat 64-bit virtual address space (up to 128 TB in practice)         |
|  TSO (Total Store Order) — very strong consistency                    |
|  Pages: 4 KB, 2 MB (huge), 1 GB (gigantic)                          |
+-----------------------------------------------------------------------+
```

---

## The Register File

### General-Purpose Registers

```
  64-bit name  32-bit view  16-bit  8-bit high  8-bit low
  -----------  -----------  ------  ----------  ---------
  RAX          EAX          AX      AH          AL
  RBX          EBX          BX      BH          BL
  RCX          ECX          CX      CH          CL
  RDX          EDX          DX      DH          DL
  RSI          ESI          SI                  SIL
  RDI          EDI          DI                  DIL
  RSP          ESP          SP                  SPL
  RBP          EBP          BP                  BPL
  R8           R8D          R8W                 R8B
  R9           R9D          R9W                 R9B
  R10          R10D         R10W                R10B
  R11          R11D         R11W                R11B
  R12          R12D         R12W                R12B
  R13          R13D         R13W                R13B
  R14          R14D         R14W                R14B
  R15          R15D         R15W                R15B

  KEY RULES:
  - Writing a 32-bit register ZEROS the upper 32 bits of the 64-bit reg
    (MOV EAX, 1  →  RAX = 0x0000000000000001)
  - Writing an 8-bit or 16-bit register DOES NOT zero upper bits
    (MOV AL, 1   →  RAX upper bits unchanged)
  - This asymmetry is a common source of bugs in assembly
```

### Register Conventions

```
  TRADITIONAL USES (from 8086 heritage, still matter in encoding):
  RAX: Accumulator — implicit in MUL, DIV, IMUL, LAHF, string ops
  RCX: Counter — implicit in LOOP, REP, shift counts (CL)
  RDX: Data — implicit in MUL/DIV (64-bit product in RDX:RAX)
  RSI: Source Index — string ops (source)
  RDI: Destination Index — string ops (destination)
  RSP: Stack Pointer — always points to top of stack (PUSH/POP/CALL/RET)
  RBP: Base Pointer — conventional frame pointer (not mandatory)
  RIP: Instruction Pointer — cannot be directly modified; PC-relative addressing
```

---

## Calling Conventions

Understanding calling conventions is essential for interop and for reading JIT output.

### System V AMD64 ABI (Linux, macOS)

```
  ARGUMENT PASSING:
  Integer/pointer arguments:   RDI, RSI, RDX, RCX, R8, R9
  Float arguments:             XMM0–XMM7
  Additional args:             pushed on stack (right to left)

  RETURN VALUES:
  Integer/pointer:             RAX (+ RDX for 128-bit)
  Float:                       XMM0

  CALLER-SAVED (scratch — callee may destroy):
  RAX RCX RDX RSI RDI R8 R9 R10 R11
  XMM0–XMM15

  CALLEE-SAVED (preserved — callee must restore if used):
  RBX RBP R12 R13 R14 R15

  STACK:
  - 16-byte aligned at call instruction
  - Red zone: 128 bytes below RSP can be used without adjusting RSP
    (leaf functions can use this as scratch space)
```

### Microsoft x64 ABI (Windows, .NET CLR)

```
  ARGUMENT PASSING:
  Args 1–4: RCX, RDX, R8, R9 (integers/pointers)
            XMM0–XMM3 (floats, in corresponding slot)
  Additional args: on stack

  Shadow space: 32 bytes (4 × 8) MUST be allocated by caller
  on the stack before the CALL, above the arguments.
  Even if the callee doesn't use it — it must be there.
  (This is "home space" / "spill space" for the first 4 args.)

  RETURN VALUE:
  RAX (integer) / XMM0 (float)

  CALLEE-SAVED:
  RBX RBP RDI RSI R12 R13 R14 R15 XMM6–XMM15

  KEY DIFFERENCE FROM SYSV:
  Windows: args in RCX, RDX, R8, R9  (4 regs, shadow space required)
  Linux:   args in RDI, RSI, RDX, RCX, R8, R9  (6 regs, no shadow)
  Mixing them up = crash. This matters for .NET P/Invoke.
```

---

## Instruction Encoding

x86-64 instructions are 1 to 15 bytes. The encoding is a legacy format evolved from 8086 through 486 through x86-64.

### Instruction Format

```
  [Optional Prefixes (0-4 bytes)]
  [REX Prefix (0-1 byte)]
  [Opcode (1-3 bytes)]
  [ModRM (0-1 byte)]
  [SIB (0-1 byte)]
  [Displacement (0,1,2,4 bytes)]
  [Immediate (0,1,2,4,8 bytes)]

  LEGACY PREFIXES (can appear 0-4 times):
  0x66: Operand-size override (16-bit operand in 32/64-bit mode)
  0x67: Address-size override
  0xF2, 0xF3: REP/REPNE (also repurposed for SSE)
  0x2E, 0x3E, etc.: Segment overrides (mostly irrelevant in 64-bit)

  REX PREFIX: 0100WRXB
  W: 1 = 64-bit operand size (REX.W)
  R: Extends ModRM reg field (bit 3)
  X: Extends SIB index field (bit 3)
  B: Extends ModRM r/m or SIB base field (bit 3)

  This is how R8–R15 are encoded: the REX prefix
  adds a 4th bit to the otherwise 3-bit register field.
```

### ModRM Byte

```
  ModRM: [mod:2][reg:3][r/m:3]

  mod = 00: [r/m] = memory, no displacement
  mod = 01: [r/m] + 8-bit displacement
  mod = 10: [r/m] + 32-bit displacement
  mod = 11: r/m = register directly

  reg: source or destination register (or opcode extension)
  r/m: register or memory operand (with SIB for complex addressing)

  SIB (Scale-Index-Base): [scale:2][index:3][base:3]
  scale = 1, 2, 4, or 8
  Effective address = base_reg + index_reg * scale + displacement

  EXAMPLE: MOV EAX, [RBX + RCX*4 + 0x10]
  REX: none needed (32-bit op, regs in 0-7)
  Opcode: 8B (MOV r32, r/m32)
  ModRM: mod=01 (disp8), reg=000 (EAX), r/m=100 (SIB follows)
  SIB: scale=10 (×4), index=001 (RCX), base=011 (RBX)
  Disp: 0x10
```

---

## Key Instruction Classes

### Integer Arithmetic

```
  ADD dst, src          dst += src
  SUB dst, src          dst -= src
  IMUL reg, r/m         reg *= r/m   (signed; result in reg)
  IMUL reg, r/m, imm    reg = r/m * imm
  IDIV r/m              RDX:RAX / r/m → quotient in RAX, remainder in RDX
  INC dst               dst++   (does NOT affect CF; subtle difference from ADD 1)
  DEC dst               dst--
  NEG dst               dst = -dst
  LEA dst, [mem_expr]   Load Effective Address — computes address, no memory access
                        Often used as fast multiply: LEA rax, [rbx + rbx*2]  (= rbx*3)
```

### Logical and Shift

```
  AND dst, src          bitwise AND
  OR  dst, src          bitwise OR
  XOR dst, src          bitwise XOR   (XOR reg, reg = fast zero; sets ZF)
  NOT dst               bitwise NOT
  SHL dst, cl/imm       Shift left (fill with 0)
  SHR dst, cl/imm       Shift right logical (fill with 0)
  SAR dst, cl/imm       Shift right arithmetic (fill with sign bit)
  ROL/ROR               Rotate left/right (bits wrap around)
  BIT MANIPULATION EXTENSIONS (BMI1/BMI2):
  BLSI  dst, src        Extract lowest set bit: src & (-src)
  BLSR  dst, src        Reset lowest set bit: src & (src-1)
  TZCNT dst, src        Count trailing zeros
  POPCNT dst, src       Count set bits
```

### Branches and Control Flow

```
  CMP dst, src          Sets flags; does NOT modify operands (SUB without storing)
  TEST dst, src         Sets flags; does NOT modify (AND without storing)

  FLAGS (in RFLAGS):
  ZF: zero flag    (result = 0)
  SF: sign flag    (result negative)
  CF: carry flag   (unsigned overflow)
  OF: overflow     (signed overflow)
  PF: parity flag  (low byte has even number of 1 bits)

  CONDITIONAL JUMPS:
  JE/JZ   jump if equal / zero (ZF=1)
  JNE/JNZ jump if not equal
  JL/JNGE jump if less (signed: SF≠OF)
  JG/JNLE jump if greater (signed)
  JB/JC   jump if below (unsigned: CF=1)
  JA      jump if above (unsigned)
  JMP     unconditional jump

  CMOVcc: conditional move — no branch, avoids prediction penalty
  CMOVE rax, rbx   "if ZF=1 then RAX = RBX"  (no jump, no misprediction)
```

### SIMD: SSE / AVX

```
  SSE: 128-bit XMM registers
  MOVAPS xmm0, [mem]        Aligned load of 4 × float32
  ADDPS  xmm0, xmm1         Add 4 pairs of float32 in parallel
  MULPS  xmm0, xmm1         Multiply 4 pairs
  SQRTPS xmm0, xmm1         Square root of 4 floats
  CVTDQ2PS xmm0, xmm1       Convert 4 × int32 to float32

  AVX: 256-bit YMM registers (VEX prefix)
  VMOVAPS ymm0, [mem]        Aligned load of 8 × float32
  VADDPS  ymm0, ymm1, ymm2   8 × float32 addition (3-operand, non-destructive)
  VFMADD213PS ymm0,ymm1,ymm2  Fused multiply-add: ymm0 = ymm1*ymm0 + ymm2

  AVX-512: 512-bit ZMM registers + mask registers k0–k7
  VMOVAPS zmm0 {k1}, [mem]   Masked load (only elements where k1 bit set)
  = 16 × float32 in one instruction

  ACCESSING SIMD FROM SOFTWARE:

  AUTO-VECTORIZATION (universal — any language + compiler):
  The compiler detects loops over arrays and emits SIMD instructions
  automatically. No source changes required.
    GCC/Clang: -O2 or higher enables auto-vectorization
    MSVC: /O2 enables; /arch:AVX2 unlocks 256-bit
    JVM (JIT): HotSpot auto-vectorizes counted loops (JDK 9+)
    .NET CLR JIT: auto-vectorizes Span<T> loops in common patterns
    CPython: NumPy/SciPy rely on C/Fortran SIMD under the hood

  EXPLICIT INTRINSICS (portable C/C++):
    GCC/Clang: __m256 / __m256d / __m256i types
               _mm256_add_ps(), _mm256_mul_ps(), etc.
    AVX-512:   __m512 and _mm512_* intrinsics
    std::experimental::simd (C++23): portable SIMD abstraction
               std::experimental::fixed_size_simd<float, 8>

  JAVA VECTOR API (JDK 16+, incubating):
    FloatVector v = FloatVector.fromArray(SPECIES_256, a, i);
    v.add(FloatVector.fromArray(SPECIES_256, b, i)).intoArray(c, i);
    JIT compiles to AVX2 or AVX-512 depending on hardware.

  .NET: System.Runtime.Intrinsics.X86 exposes SSE/AVX directly.
    Avx.Add(), Sse.Multiply(), etc.
    Vector256<float> also available via System.Numerics.
    The JIT can auto-vectorize LINQ-like loops in common patterns.
```

---

## Virtual Memory and Paging

```
  x86-64 VIRTUAL ADDRESS SPACE:
  48-bit canonical addresses (current CPUs)
    User space:   0x0000000000000000 – 0x00007FFFFFFFFFFF (128 TB)
    Kernel space: 0xFFFF800000000000 – 0xFFFFFFFFFFFFFFFF (128 TB)
    (Addresses must be canonical — bits 48–63 = sign extension of bit 47)
  57-bit LA57 extension: 5-level paging → 128 PB user space

  PAGE TABLE HIERARCHY (4-level):
  CR3 → PML4 → PDPT → PD → PT → Physical Frame

  CR3 holds physical address of PML4 (per-process).
  Each level has 512 entries (9 bits from VA).

  VA SPLIT (48-bit, 4-level):
  [bit 63-48: sign ext][bit 47-39: PML4][bit 38-30: PDPT]
  [bit 29-21: PD][bit 20-12: PT][bit 11-0: page offset]

  TLB: Translation Lookaside Buffer
  Cache of VA→PA translations. L1 TLB (iTLB, dTLB), L2 TLB.
  TLB miss: hardware page table walker traverses 4 levels.
  Context switch flushes TLB (unless PCID — process-context ID).
  INVLPG: invalidate single TLB entry.
```

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| What zero-extends automatically? | 32-bit writes zero the upper 32 bits; 8/16-bit writes do not |
| Windows vs Linux calling convention? | Windows: RCX/RDX/R8/R9 + 32-byte shadow; Linux: RDI/RSI/RDX/RCX/R8/R9 |
| What is LEA used for (beyond addresses)? | Fast multiply-add without memory access: `LEA rax,[rbx+rbx*4]` = rbx×5 |
| Why use CMOV instead of JE? | Conditional move avoids branch misprediction penalty |
| What is the REX prefix for? | Enables 64-bit operand size (REX.W) and extends register fields to access R8–R15 |
| How wide are AVX-512 operations? | 512 bits = 16 × float32 or 8 × float64 per instruction |
| What is the red zone? | 128 bytes below RSP that leaf functions can use as scratch (Linux ABI only) |

---

## Common Confusion Points

**32-bit write zero-extends but 8/16-bit doesn't**: This is by design (x86-64 ABI) but trips up people writing assembly. Compilers know this and exploit it (32-bit move to zero-extend for free). Partial register writes (AL, AX) can cause dependency chains (processor must merge into full register).

**Shadow space on Windows is mandatory**: Forgetting the 32-byte shadow (home space) before a call on Windows x64 is a common interop bug. The callee's prolog may use it even if it doesn't read the arguments there. .NET P/Invoke handles this automatically but handwritten asm must not forget it.

**XMM/YMM/ZMM are the same register with different widths**: XMM0 is the low 128 bits of YMM0, which is the low 256 bits of ZMM0. Mixing SSE and AVX instructions on the same registers causes performance penalties (AVX-SSE transition penalty). Use VZEROUPPER to avoid this.

**TSO does not mean sequentially consistent**: x86 TSO (Total Store Order) means stores are visible to all processors in program order, but a processor can read its own store buffer before it becomes globally visible. This is weaker than full sequential consistency. See 06-CACHE-COHERENCE.md for implications.

**Segment registers still exist**: CS, DS, ES, SS, FS, GS. In 64-bit mode, CS/DS/ES/SS are forced to zero base (flat model). FS and GS have non-zero bases — used by the OS: FS (Linux thread-local storage), GS (Windows TEB — Thread Environment Block, where `.` in .NET thread-local data lives).
