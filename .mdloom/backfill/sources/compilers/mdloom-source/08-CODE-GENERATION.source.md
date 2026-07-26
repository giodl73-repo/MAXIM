---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "08-CODE-GENERATION.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:compilers:code-generation
kind: guide
module: compilers
section: compilers
title: Code Generation - Instruction Selection, Scheduling, Calling Conventions, ABI
status: source-custody
source_custody: partial
current_path: compilers/08-CODE-GENERATION.md
canonical_path: compilers/08-CODE-GENERATION.md
backsource_ids: [mdloom-backfill:compilers:08-code-generation, git-history:compilers:08-code-generation]
concepts: [code generation, instruction selection, instruction scheduling, calling convention, ABI, peephole, prologue epilogue]
root_concepts: [code generation]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Code Generation — IR to Machine Code

## The Big Picture

The backend turns optimized, target-independent IR into instructions for a specific
machine. Three problems dominate: **instruction selection** (which machine
instructions implement this IR?), **instruction scheduling** (in what order, to keep
the pipeline busy?), and **register allocation** (guide 07). Wrapped around all of it
is the **ABI** — the calling convention, stack layout, and binary contract that lets
your code call, and be called by, code you did not compile. This guide builds the
machine-facing half of the pipeline.

```
+--------------------------------------------------------------------------+
|                          CODE GENERATION                                 |
|                                                                          |
|   optimized IR (target-independent, SSA, virtual regs)                   |
|        |                                                                 |
|        v                                                                 |
|   INSTRUCTION SELECTION                                                  |
|     tile the IR/DAG with machine instructions                            |
|     IR ops -> machine instructions                                       |
|     (maximal munch / BURS / DAG covering)                                |
|        |                                                                 |
|        v                                                                 |
|   INSTRUCTION SCHEDULING                                                 |
|     reorder to hide latencies / hazards                                  |
|     list scheduling over the dependence DAG                              |
|     (respect data deps, fill pipeline slots)                             |
|        |                                                                 |
|        v                                                                 |
|   REGISTER ALLOCATION (guide 07)                                         |
|     virtual -> physical                                                  |
|     coloring / linear scan + spills                                      |
|        |                                                                 |
|        v                                                                 |
|   CALLING CONVENTION                                                     |
|     ABI: prologue/epilogue, arg passing,                                 |
|     stack frame, callee/caller-saved regs                                |
|        |                                                                 |
|        v                                                                 |
|   PEEPHOLE cleanup -> emit assembly / object code -> linker              |
+--------------------------------------------------------------------------+
```

Selection, scheduling, and allocation are mutually entangled (each constrains the
others); compilers run them in a target-tuned order with cleanup passes between.

---

## Instruction Selection

Map IR operations onto target instructions. The catch: real ISAs have complex
instructions that implement *several* IR ops at once (`lea`, fused multiply-add,
addressing modes), so the goal is to **cover the IR with the cheapest set of tiles.**

```
  IR DAG for  t = a[i]   (i.e.  load(base + i*4)) :

            load
              |
             add
            /    \
         base    mul
                /    \
               i      4

  Naive (one instruction per node):        x86 covers it with ONE tile:
     mul  r1, i, 4                            mov  rax, [base + rax*4]
     add  r2, base, r1                        ; the addressing mode does
     load r3, [r2]                            ; base + index*scale for free
  3 instructions                             1 instruction -> pick this tiling
```

```
  TILING APPROACHES:
    MAXIMAL MUNCH      greedily match the largest tile at each node, top-down.
                       Fast, near-optimal in practice.
    TREE / DAG COVERING with dynamic programming (BURS -- Bottom-Up Rewrite
                       Systems, e.g. iburg, lburg): assign a COST to each tile,
                       find the minimum-cost cover of the tree. OPTIMAL for
                       trees; DAGs (shared subexpressions) are NP-hard -> heuristics.
    LLVM: SelectionDAG (DAG covering) and the newer GlobalISel (a more
                       incremental, faster selector).
```

The pattern set is the *machine description* — a declarative table of `IR-pattern →
instruction(+cost)`. Adding a new target is largely writing this table, which is why
LLVM can support many ISAs from one IR.

---

## Instruction Scheduling

Modern CPUs are pipelined and superscalar: an instruction's result is not ready for
several cycles, and the wrong order stalls the pipeline. Scheduling reorders
instructions (respecting data dependencies) to hide these latencies.

```
  Dependence (precedence) DAG -- edges are data dependencies:

     load r1, [a]   (3-cycle latency)
     load r2, [b]   (3-cycle latency)
     add  r3, r1, r2   <- needs r1 AND r2
     mul  r4, r3, r3

  BAD schedule:            GOOD schedule (overlap the loads):
     load r1,[a]              load r1,[a]
     add r3,r1,r2  <- STALL!  load r2,[b]   <- issued while r1 loads
        (r2 not ready)        add r3,r1,r2  <- both ready now
                              mul r4,r3,r3

  LIST SCHEDULING (the standard heuristic):
     topologically order the DAG; maintain a READY set (deps satisfied);
     each cycle pick the ready instruction with the highest PRIORITY
     (critical-path length / latency), respecting functional-unit limits.
```

```
  Hazards scheduling addresses:
    DATA hazard (RAW): consumer must wait for producer -> space them out.
    STRUCTURAL hazard: only N units of a kind -> don't over-issue.
    LOAD-USE latency: cache/memory ops are slow -> hoist loads early.
  Note: out-of-order CPUs reschedule dynamically, so scheduling matters most
  for in-order cores (embedded, some mobile) and for keeping the OOO window
  fed. See computer-architecture/ for pipelines, hazards, and OOO execution.
```

Scheduling and register allocation conflict: aggressive scheduling lengthens live
ranges (more values in flight → more pressure → more spills). Compilers schedule
before *and* after allocation, or balance the two (e.g. LLVM's pre-RA and post-RA
schedulers).

---

## Calling Conventions and the ABI

The **Application Binary Interface** is the contract that makes separate compilation
and linking work: how arguments are passed, who saves which registers, how the stack
is laid out, how values are returned. Get it wrong and code cannot interoperate.

```
  THE STACK FRAME (x86-64, grows DOWN):

     higher addresses
     +------------------------+----------------------------------------+
     |  caller's frame        |                                        |
     +------------------------+----------------------------------------+
     |  argument 7, 8, ...    |  args beyond register count, by caller |
     +------------------------+----------------------------------------+
     |  return address        |  pushed by CALL                        |
     +------------------------+----------------------------------------+
     |  saved RBP             |  frame base = RBP (if used)            |
     +------------------------+----------------------------------------+
     |  callee-saved regs     |  prologue saves the ones it will use   |
     +------------------------+----------------------------------------+
     |  local variables /     |                                        |
     |  spill slots           |  register allocator's overflow here    |
     +------------------------+----------------------------------------+
     lower addresses  <- RSP (stack pointer)
```

```
  ARGUMENT PASSING (registers first, then stack):
    System V AMD64 (Linux/macOS):  int args -> RDI,RSI,RDX,RCX,R8,R9;
                                   float -> XMM0..7; return in RAX (RDX:RAX)
    Windows x64:                   int args -> RCX,RDX,R8,R9; float -> XMM0..3;
                                   32-byte "shadow space" reserved by caller;
                                   return in RAX
    AArch64 (AAPCS):               X0..X7 for args, X0/X1 return

  REGISTER PARTITION (who preserves what):
    CALLER-SAVED (volatile): caller must save if it needs them across a call.
    CALLEE-SAVED (non-volatile): callee must restore before returning.
    -> this partition is exactly what constrained register allocation (07).
```

### Prologue and Epilogue

```
  PROLOGUE (on entry):                  EPILOGUE (on return):
     push rbp                              mov rsp, rbp     ; or add rsp,N
     mov  rbp, rsp                         pop rbp
     sub  rsp, frame_size  ; locals       ret
     push callee-saved regs used          (pop callee-saved first)

  Modern compilers often OMIT the frame pointer (RBP) when not needed
  (-fomit-frame-pointer): one more usable register, but stack unwinding then
  relies on .eh_frame / unwind tables rather than walking saved RBPs.
```

The ABI also fixes struct layout, alignment, name mangling (C++/Rust), exception
unwinding tables, and how the dynamic linker resolves cross-module calls (the PLT/GOT
on ELF, import tables on PE). It is the seam between your generated code and guide 09's
runtime, the OS loader, and every other compiled module.

---

## Peephole and Final Lowering

A last local pass over near-machine code catches patterns the earlier phases left.

```
  redundant move        mov rax, rax        -> delete
  store-then-load same  mov [x], rax        -> drop the load, keep rax
                        mov rax, [x]
  combine               add rax, 1 ; add rax, 1 -> add rax, 2
  use addressing mode   mov r,[b]; add r,i  -> mov r,[b+i]
  branch simplification jmp L; L:           -> fall through
```

These are the machine-level cousins of the IR-level local optimizations in guide 06,
applied after instruction selection and allocation expose target-specific patterns.

---

## Old World → New World Bridges

| You know | Maps to |
|----------|---------|
| Reading x64 disassembly (windbg/VS) | The output of instruction selection + allocation — addressing modes are selected tiles |
| Windows x64 calling convention (RCX/RDX/R8/R9, shadow space) | The ABI the codegen must honor; differs from SysV — same code, different target table |
| P/Invoke / `DllImport` marshaling | The ABI seam — you are manually matching calling conventions across the boundary |
| `[StructLayout]` / `Pack` in C# | ABI struct layout and alignment rules made explicit |
| Stack traces / unwinding | Driven by frame layout + unwind tables the prologue/epilogue and ABI define |
| RyuJIT emitting native code at runtime | A JIT backend doing exactly this pipeline — selection, LSRA, ABI — at load time |

The headline bridge: **the ABI is why P/Invoke and `DllImport` need `CallingConvention`
and marshaling.** When .NET calls a native function it must place arguments in the
exact registers/stack slots the callee's ABI expects and preserve the right registers.
That is the same calling convention the code generator bakes into every emitted call —
made visible because you are crossing a boundary the compiler can't see across.

---

## Decision Cheat Sheet

| I want to... | Use |
|---|---|
| Map IR ops to machine instructions | Instruction selection (tiling) |
| Get optimal tiling of an expression tree | BURS / DP tree covering (iburg-style) |
| Select fast in a JIT | Maximal munch or LLVM GlobalISel |
| Exploit complex addressing (`base+idx*scale`) | Larger tiles that cover multiple IR nodes |
| Hide load/ALU latencies | Instruction scheduling (list scheduling) |
| Order instructions on an in-order core | Pre-RA + post-RA list scheduling |
| Pass arguments correctly | Follow the target ABI (SysV vs Win64 vs AAPCS) |
| Decide which registers to preserve | Caller-saved vs callee-saved per the ABI |
| Lay out a stack frame | Prologue/epilogue + spill slots + saved regs |
| Free up a register | Omit the frame pointer (rely on unwind tables) |
| Clean up final code | Peephole optimization |
| Call native code from managed | Match the calling convention (P/Invoke marshaling) |

---

## Common Confusion Points

**Instruction selection is a covering problem, not a 1:1 map.** One machine
instruction often implements several IR nodes (a `lea` or an addressing mode does
multiply-add-load). The goal is the cheapest *tiling* of the IR, not translating each
node independently.

**Scheduling matters even on out-of-order CPUs.** OOO hardware reorders dynamically,
but the compiler's schedule sets the instruction window the CPU sees and still matters
for in-order cores, code size, and keeping the OOO engine fed. For the hardware model,
see `computer-architecture/`.

**Scheduling and allocation fight each other.** Better scheduling lengthens live ranges
and raises register pressure, causing spills; better allocation constrains scheduling.
There is no clean phase order — compilers run both, before and after each other.

**The ABI is not the ISA.** The instruction set is what the CPU executes; the ABI is a
*convention layered on top* (which registers carry arguments, who saves what). Two OSes
on the same CPU (Windows x64 vs Linux SysV) have different ABIs and incompatible
binaries despite identical instructions.

**Caller-saved vs callee-saved is the ABI talking to the allocator.** A value live
across a call must go in a callee-saved register or be spilled — that constraint
(guide 07) comes straight from the calling convention defined here.

**Omitting the frame pointer is a real trade-off.** It frees a register but makes stack
unwinding depend on unwind metadata (`.eh_frame`, PE unwind info) rather than a chain
of saved RBPs — fine with good tables, painful without them.
