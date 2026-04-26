# 22 — Compilers & Interpreters in Modern Systems

## The Frame

Lexing and parsing are covered in 21-AUTOMATA. This guide picks up after the AST exists and focuses on what modern compilers do with it: IR design, SSA form, optimization passes, code generation, and the JIT/AOT spectrum. Then it maps these concepts to the specific compilers you interact with daily — TypeScript, V8, LLVM, esbuild, the Rust compiler.

```
The Classical Pipeline
=======================

  Source
    ↓  Lexer (DFA)              — characters → tokens
    ↓  Parser (PDA/LL/LR)       — tokens → AST
    ↓  Semantic Analysis        — type checking, name resolution, scoping
    ↓  IR Generation            — AST → intermediate representation
    ↓  Optimization Passes      — on IR (machine-independent)
    ↓  Code Generation          — IR → target (machine code, bytecode, JS)
    ↓  Target Optimization      — machine-dependent (peephole, scheduling)
  Output
```

The frontend (lex → parse → sema) is language-specific. The middle (IR + optimization) is where the real work happens. The backend (codegen) is target-specific. LLVM's great insight: share the middle.

```
THE COMPILER ECOSYSTEM — WHO SHARES WHAT
==========================================

  LLVM-based (shared backend)
  ┌─────────────────────────────────────────────────────────────────┐
  │  clang   → Clang AST → LLVM IR ──────────────────────┐         │
  │  rustc   → HIR → THIR → MIR → LLVM IR ───────────────┤         │
  │  swiftc  → Swift AST → SIL → LLVM IR ─────────────────┤        │
  │  kotlin/native → Kotlin IR → LLVM IR ──────────────────┤       │
  │  zig     → Zig IR → LLVM IR ────────────────────────────┼──→  LLVM
  │  clangd  (language server uses clang frontend)          │    backend
  └─────────────────────────────────────────────────────────┘       │
                                                               x86 / ARM /
                                                               WASM / RISC-V

  Standalone JIT (own backend, no LLVM)
  ┌────────────────────────────────────────────────────────────────┐
  │  V8 (JS):    Ignition (bytecode) → Maglev → Turbofan           │
  │  SpiderMonkey: Warp JIT (replaces IonMonkey)                   │
  │  JavaScriptCore: LLInt → Baseline → DFG → FTL (LLVM-based!)    │
  └────────────────────────────────────────────────────────────────┘

  Transpilers (no native backend — source → source)
  ┌────────────────────────────────────────────────────────────────┐
  │  tsc   (TypeScript → JS)  own AST + type checker, no backend   │
  │  esbuild (TS/JS → JS bundle)  Go-native, no LLVM, no typecheck │
  │  SWC   (TS/JS → JS)  Rust-based, strips types only             │
  └────────────────────────────────────────────────────────────────┘

  Multi-IR pipelines (notable for IR depth)
  ┌────────────────────────────────────────────────────────────────┐
  │  rustc:  .rs → HIR → THIR → MIR → LLVM IR                      │
  │          Each IR serves a distinct purpose:                    │
  │          HIR: desugaring + name resolution                     │
  │          THIR: type-checked, pattern exhaustiveness            │
  │          MIR: borrow checker + const eval (CFG-based)          │
  │          LLVM IR: machine-independent optimization             │
  │                                                                │
  │  clang:  C++ → Clang AST → LLVM IR  (2-stage, simpler)         │
  └────────────────────────────────────────────────────────────────┘

  Incremental compilation (semantic caching)
  ┌────────────────────────────────────────────────────────────────┐
  │  Roslyn: SyntaxTree (immutable) + SemanticModel (lazy)         │
  │          Incremental: syntax + semantic caches per compilation │
  │          Full compiler-as-a-service API                        │
  └────────────────────────────────────────────────────────────────┘
```

---

## Intermediate Representations

The choice of IR is the central design decision of a compiler. It determines what optimizations are easy, what information is preserved, and how fast the compiler itself runs.

### AST as IR

The simplest choice. Tree-walk interpreters (Ruby MRI before YARV, many scripting languages) execute directly on the AST.

```
Pros:  Easy to generate; preserves source structure; good for error messages
Cons:  Poor cache locality (pointer-chasing through tree nodes)
       Hard to do dataflow analysis (control flow is implicit)
       Hard to optimize (e.g., common subexpression elimination across branches)
```

### Three-Address Code / Linearized IR

Flatten the AST into a sequence of simple instructions, each with at most one operator and (usually) three operands.

```
Source:  z = (a + b) * (a + b)

TAC:
  t1 = a + b
  t2 = a + b
  z  = t1 * t2

  Redundancy obvious → common subexpression elimination (CSE):
  t1 = a + b
  z  = t1 * t1
```

The classic scalar optimizations on TAC — CSE (deduplicate redundant computations), DCE (remove unused results), constant folding (evaluate `2+3` at compile time), strength reduction (replace `x*4` with `x<<2`) — are described in every Dragon Book chapter. What matters in practice is where they run and at what cost:

```
LLVM optimization levels (approximate):

  -O1:  Basic DCE, constant folding, mem2reg (SSA promotion),
        simple inlining, basic jump threading
        Goal: fast compile, correctness, minimal overhead

  -O2:  Full scalar optimizations + loop optimizations (LICM, unrolling),
        inlining (size-limited), auto-vectorization, alias analysis
        Default for release builds; most of the wins are here

  -O3:  Aggressive inlining (higher size threshold), loop vectorization
        at higher unroll factors, interprocedural analysis
        Bigger binary, marginally better throughput; rarely worth it over -O2

  -Os / -Oz:  Optimize for size (embedded, WASM); disables unrolling/vectorization

  PGO (-fprofile-generate / -fprofile-use):
    Profile-guided optimization — lets the compiler make decisions
    based on real execution data rather than static estimates
    Most impactful for code with hard-to-predict branching

rustc MIR optimizations (before LLVM):
  MIR sits between the borrow checker and LLVM lowering.
  MIR-level passes run before LLVM sees the code:
    - Inlining of small functions (MIR inliner)
    - Const propagation (leveraging the const evaluator)
    - Copy propagation, basic DCE
    - Promotion of temporaries to static constants
  Key point: borrow-checker-aware optimizations happen here —
  the MIR knows about borrows and moves, so passes can exploit
  the ownership invariants that LLVM IR doesn't see.
```

### SSA — Static Single Assignment

SSA is the IR form used by every serious modern compiler (LLVM, GCC, V8 Turbofan, the Rust MIR pipeline, the JVM JIT). It is the single most important concept in modern compiler backends.

Every variable is assigned exactly once; φ (phi) functions at merge points select among reaching definitions. The important details are in how specific compilers build and use SSA:

**LLVM's approach — `alloca` + `mem2reg`:**

LLVM frontends do not need to construct SSA directly. The standard pattern:
1. Emit local variables as `alloca` (stack allocation) instructions
2. Use `store`/`load` to read and write them (non-SSA)
3. Run the `mem2reg` pass, which promotes stack allocations to SSA virtual registers

This two-phase approach simplifies the frontend considerably — it can emit straightforward imperative code, and `mem2reg` handles the SSA construction including φ-node placement. The LLVM IR after `mem2reg` is proper SSA; before, it's a mix of SSA for intermediate expressions and stack-based for locals.

**rustc's MIR — SSA from the start:**

MIR is designed as SSA from its initial construction. More importantly, borrows and moves are first-class annotations in MIR, not just type-level metadata. This means borrow-checker-aware optimizations (copy propagation through borrows, elision of redundant clones) can happen in the MIR optimizer before LLVM ever sees the code.

**V8 Turbofan — sea of nodes instead of CFG SSA:**

Turbofan avoids explicit φ nodes entirely. Its "sea of nodes" IR treats control flow as just another edge type — value nodes float freely, ordered only by data dependencies. Scheduling (placing nodes into a linear order for code emission) is a separate late pass. This enables more aggressive global value numbering but makes the IR harder to debug.

```
Non-SSA:                           SSA:
═════════                          ════
x = 1                              x₁ = 1
if cond:                           if cond:
  x = 2                              x₂ = 2
y = x + 1                          y = φ(x₁, x₂) + 1
                                   (φ selects x₁ or x₂ based on which
                                    branch was taken)
```

**Why SSA enables optimizations that are hard otherwise:**

```
Use-def chains are trivial:
  Each use of x₂ has exactly one definition (the φ or assignment that created x₂).
  In non-SSA, finding all definitions of "x" requires global analysis.
  In SSA, it's a single pointer.

Constant propagation becomes local:
  x₁ = 5
  y = x₁ + 3    → y = 5 + 3 → y = 8   (follow the single definition)

Dead code elimination is a graph reachability problem:
  Compute the use-def graph. Nodes with no uses (and no side effects) are dead.
  Remove them. Repeat until fixed point.

Global value numbering (GVN):
  Assign a number to each unique computed value.
  Two instructions with the same value number compute the same thing → deduplicate.
  More powerful than local CSE — works across basic blocks.
```

### φ Functions and the Dominance Tree

Standard SSA construction: compute dominance tree, compute dominance frontiers, insert φ at frontiers, rename variables. This is a standard homework problem; the interesting part is why LLVM chose not to do it directly.

LLVM's `mem2reg` is the practical alternative. Instead of building SSA upfront, frontends emit `alloca`/`store`/`load` for locals, and `mem2reg` promotes them to SSA registers in a single pass. The reason: it decouples the frontend from SSA construction entirely. A new language targeting LLVM can emit correct (if slightly inefficient) code without implementing dominance-frontier-based SSA construction — `mem2reg` handles it. The pass is fast enough that this is not a performance concern.

```
Dominance: block A dominates block B if every path from entry to B goes through A.

SSA construction algorithm:
  1. Compute dominance tree
  2. Compute dominance frontiers (where control flows merge)
  3. Insert φ functions at dominance frontiers
  4. Rename variables with subscripts (the single-assignment pass)

The dominance tree is the backbone of most SSA-based analyses.
Algorithms that are O(n²) on CFGs often become O(n log n) or O(n) on the dom tree.
```

### LLVM IR

LLVM's IR is typed SSA in text form. It's the reason LLVM can be a shared backend for C, C++, Rust, Swift, Clang, Zig, and hundreds of research languages.

```llvm
; LLVM IR — factorial
define i64 @factorial(i64 %n) {
entry:
  %cond = icmp sle i64 %n, 1
  br i1 %cond, label %base, label %recurse

base:
  ret i64 1

recurse:
  %n_minus_1 = sub i64 %n, 1
  %sub_result = call i64 @factorial(i64 %n_minus_1)
  %result = mul i64 %n, %sub_result
  ret i64 %result
}
```

```
LLVM IR properties:
  Typed (i8, i32, i64, float, ptr, <4 x i32> vectors)
  SSA with explicit φ functions
  Infinite virtual registers (lowered to physical regs in backend)
  Three forms: in-memory (bitcode), text (.ll), bitcode (.bc)
  Platform-independent — same IR → x86, ARM, WASM, RISC-V
```

---

## Optimization Passes

LLVM has ~100 optimization passes. The important classes:

### Scalar Optimizations

```
Constant folding / propagation
  2 + 3 → 5 at compile time
  Propagate known constants through SSA def-use chains

Dead code elimination (DCE)
  Remove instructions whose results are never used
  Intra-procedural: remove unused temporaries
  Inter-procedural: whole-program DCE (link-time optimization)

Inlining
  Replace call site with callee body
  Enables further optimization (constant propagation through call boundary)
  Trade-off: reduces call overhead, increases code size, may hurt i-cache

Loop optimizations
  Loop-invariant code motion (LICM): move invariant computations out of loop
  Loop unrolling: replicate loop body k times, reduce branch overhead
  Vectorization (auto-vectorization): scalar loop → SIMD instructions
  Loop fusion / fission: combine or split loops for cache locality

Alias analysis
  Can pointers p and q point to the same memory?
  Conservative: assume yes (safe, misses optimization)
  Interprocedural: track provenance (enables more aggressive opt)
  TBAA (type-based alias analysis): in C/C++, objects of different types
    can't alias → enables load/store reordering
```

### Whole-Program Optimizations (LTO)

```
Link-Time Optimization (LTO)
  Classical compiler: optimize each translation unit separately
  LTO: emit LLVM IR bitcode, optimize the whole program at link time
  Enables: cross-module inlining, whole-program DCE, devirtualization

  Rust uses LTO by default for release builds
  Swift uses LTO
  C/C++ with clang: -flto flag

  Thin LTO: parallel LTO with summary-based analysis (faster, nearly as good)
```

---

## The JIT Spectrum

AOT (ahead-of-time) compilers generate native code before execution. JIT (just-in-time) compilers generate native code during execution, using runtime profiling to guide optimization decisions that no static compiler can make.

```
The JIT Insight
================

  Static compiler:  must generate code that works for all possible inputs
  JIT compiler:     has seen actual inputs — can speculate

  Speculation example (V8):
    function add(a, b) { return a + b; }
    Called 10,000 times with integers → speculate it's always integers
    Generate optimized integer add (no type checks)
    If called with a string: deoptimize → fall back to interpreter

  Speculation enables optimizations provably impossible for static compilers:
    Inline virtual dispatch (if the target is always the same concrete type)
    Eliminate type checks (if the type has never varied)
    Specialize for observed shapes (object layouts)
```

### V8's Multi-Tier Pipeline

```
JavaScript source
      ↓
  Parser → AST
      ↓
  Ignition (bytecode interpreter)
  ┌─────────────────────────────────────┐
  │  Generates compact bytecode         │
  │  Collects type feedback:            │
  │    "add() always sees Smi + Smi"    │
  │  Fast to start — no compilation     │
  └─────────────────┬───────────────────┘
                    │ hot function threshold
                    ↓
  Maglev (mid-tier JIT — new in V8 2023)
  ┌─────────────────────────────────────┐
  │  Fast compilation (< 1ms)           │
  │  Basic type specialization          │
  │  Good for: startup-sensitive code   │
  └─────────────────┬───────────────────┘
                    │ very hot + stable types
                    ↓
  Turbofan (optimizing JIT)
  ┌─────────────────────────────────────┐
  │  Sea-of-nodes IR (not CFG-based)    │
  │  Full SSA + aggressive opts         │
  │  Speculative type narrowing         │
  │  Escape analysis + stack allocation │
  │  Produces near-native performance   │
  └─────────────────┬───────────────────┘
                    │ type assumption violated
                    ↓
  Deoptimization → back to Ignition
```

### Sea of Nodes (Turbofan's IR)

Turbofan uses "sea of nodes" rather than a traditional CFG + SSA. Nodes represent both values and control flow; edges represent both data dependencies and ordering constraints.

```
Traditional CFG + SSA:             Sea of Nodes (Turbofan):
══════════════════════             ════════════════════════
Explicit basic blocks              No basic blocks
Explicit φ functions               φ is just a node with value edges
Control flow is structural         Control flow is an edge type
Ordering is block-based            Ordering is data + control edges

Benefits of sea of nodes:
  Global value numbering is natural (hash on node type + input edges)
  Code motion is free (move node anywhere without violating order)
  More optimization opportunities visible simultaneously

Cost:
  Harder to implement correctly
  Scheduling (mapping nodes back to instruction order) is complex
  Debugging is harder
```

### HotSpot (JVM) — Tiered Compilation

```
JVM Tiered Compilation (Java, Kotlin, Scala)
=============================================

Tier 0: Interpreter
Tier 1: C1 (client compiler) — fast compile, minimal opt
Tier 2: C1 with invocation + backedge counters
Tier 3: C1 with full profiling
Tier 4: C2 (server compiler) — slow compile, aggressive opt, SSA + global opts

Method becomes hot (10,000 invocations or 1,500 backedges in hot loop)
→ tiered compilation kicks in
→ profile-guided optimization using real type feedback

GraalVM Native Image:
  AOT compiles JVM bytecode to native binary
  No JIT at runtime — trades startup speed for peak throughput
  Used for: serverless Functions (fast cold start), CLI tools
  Limitation: closed-world assumption — no dynamic class loading at runtime
```

---

## The TypeScript Compiler

tsc is a recursive descent parser + type checker + emitter. It does not optimize — it's a transpiler with a rich type system bolted on.

```
tsc Pipeline
=============

  .ts source
      ↓
  Scanner (lexer) — produces tokens
      ↓
  Parser — recursive descent LL, produces AST (called "nodes" in tsc)
      ↓
  Binder — builds symbol table, assigns symbol IDs, computes flow analysis
           (this is where "narrowing" gets computed — the control flow graph)
      ↓
  Type Checker — structural type checking, inference, error reporting
                 The biggest and most complex phase (~40% of codebase)
      ↓
  Emitter — AST → JavaScript (or declaration files)
            No optimization — output structure mirrors input structure
```

**Roslyn ↔ tsc pipeline comparison** (for the .NET background):

| Roslyn | tsc | Role |
|--------|-----|------|
| Parser → `SyntaxTree` | Parser → AST | Syntax; immutable in Roslyn, mutable in tsc |
| Binder | Binder | Name resolution, scope analysis, control flow |
| `ISymbol` | `Symbol` | Named entities (types, variables, methods) |
| `IOperation` | IOperation API | Semantic operations (added tsc 4.x for tooling) |
| `Compilation` | `Program` | The whole compilation unit |
| Emit (IL / PDB) | Emit (JS / `.d.ts`) | Code generation |
| `SemanticModel` per file | `TypeChecker` (global) | On-demand semantic queries |

Key difference: Roslyn's `SemanticModel` is per-`SyntaxTree` and lazily computed — you ask for semantics of a node and it computes them. tsc's `TypeChecker` is a global object over the whole `Program`. Roslyn's design enables finer-grained incremental invalidation; tsc's is simpler but re-typechecks broader regions on edits.

### TypeScript's Incremental Compilation

```
tsc --build (project references) + --incremental

  Each file has a signature: hash of the public types it exports
  If a file's signature hasn't changed → dependents don't re-typecheck
  Stored in .tsbuildinfo

  This is whole-program incremental compilation via a dependency graph.
  The insight: you don't need to re-check B if A's public API didn't change,
  even if A's implementation changed.

  ts-server (language server):
    Keeps the compiler pipeline in memory
    Re-runs only affected phases on file save
    Produces diagnostics in ~50ms instead of the full tsc cold time
```

### Why tsc Is Slow on Large Projects

```
Type checking is not linear in source size:
  Structural subtyping requires potentially deep comparison
  Conditional types can trigger recursive evaluation
  The type system is Turing complete (see 23-PL-THEORY)
    → some type expressions take exponential time to evaluate
    → tsc adds depth limits to avoid infinite loops

  Large codebases (>500k LOC): tsc can take 30–120 seconds cold
  Mitigations:
    Project references: split into independently type-checked units
    ts-go (2025): Golang port of tsc — ~10× faster (parallelism + GC)
    Isolating type-checking from transpilation (SWC/esbuild do only transpile)
```

---

## esbuild — A Different Design Point

esbuild (written in Go) is 10–100× faster than webpack/rollup for bundling. The speed comes from deliberate constraints, not magic.

```
Why esbuild is fast
====================

  Single pass:
    Traditional bundlers: multiple passes over the module graph
    esbuild: parse + link + codegen in one pass where possible

  Parallel processing:
    Go's goroutines + shared memory
    Each file parsed in parallel; linking serialized only where necessary

  No full type checking:
    esbuild strips TypeScript types syntactically — no semantic analysis
    Valid TS with type errors will still bundle successfully
    Consequence: esbuild can't do TS const enum or decorators that need
    type info to emit correctly

  Minimal IR:
    esbuild's AST is simpler than tsc's
    No SSA, no optimization passes (beyond basic DCE and tree-shaking)
    The goal is fast throughput, not optimal output

  Written in Go (not JS):
    No JIT warmup cost
    Predictable GC pauses
    Direct memory control

Tradeoff:
  esbuild: fast, limited optimization
  Rollup: slower, better tree-shaking (module-aware, ES semantics)
  Webpack: slowest, most configurable, most plugins
```

---

## The Rust Compiler (rustc)

rustc has the most interesting compiler architecture in common use today — MIR (Mid-level Intermediate Representation) is where the borrow checker lives.

```
rustc Pipeline
===============

  .rs source
      ↓
  Lexer + Parser → AST
      ↓
  HIR (High-level IR) — desugaring (match, for loops, closures → primitives)
                         Name resolution, macro expansion
      ↓
  THIR (Typed HIR) — type-checked HIR; used for pattern exhaustiveness checking
      ↓
  MIR (Mid-level IR) — ← THE INTERESTING PART
    Control flow graph with explicit borrows
    Borrow checker runs here (NLL — Non-Lexical Lifetimes)
    Const evaluation runs here
    Monomorphization preparation
      ↓
  LLVM IR — MIR lowered to LLVM IR
      ↓
  LLVM optimization passes → machine code
```

### MIR and the Borrow Checker

```
MIR is explicitly designed to make the borrow checker tractable.

HIR borrows have complex lifetimes tied to syntactic scope.
MIR borrows have explicit start/end points on the CFG.
NLL (Non-Lexical Lifetimes) computes liveness on the MIR CFG.

  fn first_or_default(v: &Vec<i32>, default: i32) -> i32 {
    if v.is_empty() {           // borrow of v starts
      default
    } else {
      v[0]                      // borrow of v ends here (NLL)
    }
  }

  Lexical lifetimes (pre-NLL): borrow of v extends to end of function body
  NLL: borrow of v extends only to last use — allows more programs
  The NLL paper (Matsakis 2018) defines this as a dataflow problem on MIR.

Polonius (next-gen borrow checker):
  Reformulates NLL as a Datalog computation
  More precise — accepts more valid programs
  Currently behind a feature flag (--Zpolonius)
  The Datalog formulation makes correctness proofs tractable
```

---

## WASM — A Compiler Target and a VM

WebAssembly is a binary instruction format designed as a portable compilation target. It's what "compile to the web" actually means for non-JS languages.

```
WASM Design Choices
====================

  Stack machine bytecode (not register-based like LLVM IR)
  Structured control flow (no arbitrary jumps — loop/block/if primitives)
  Linear memory (a big byte array — no GC by default)
  Type-safe (validated before execution)
  Sandboxed (no direct system calls — capability-based imports)

  These constraints enable:
    Fast validation (linear time — structured control flow)
    Easy JIT compilation (stack machine → register allocation is straightforward)
    Security (sandbox + capability model)

WASM compilation pipeline (e.g., Rust → WASM):
  Rust → MIR → LLVM IR → wasm32 backend → .wasm binary
  Then in browser: .wasm → Liftoff (fast baseline JIT) → Turbofan (optimizing JIT)
  V8 has two WASM compilers just like it has two JS compilers.

WASI (WebAssembly System Interface):
  Brings WASM outside the browser (server-side, edge functions)
  Standardizes system call interface (file I/O, networking, clocks)
  Fastly's Compute@Edge, Cloudflare Workers use WASM + WASI
```

### Cranelift — The Fast-Compile Alternative Backend

Cranelift is a code generation backend designed around fast compilation rather than optimal output. Two production uses: rustc's alternative backend and Wasmtime's primary JIT.

**rustc + Cranelift** (`RUSTFLAGS="-Zcodegen-backend=cranelift"`):
- Design goals: fast compilation for debug cycles, simple IR, fast register allocation
- Deliberately skips LLVM's optimization passes — no vectorization, no aggressive inlining, no loop unrolling
- Trade-off: -O2-quality output is 20–30% slower than LLVM, but debug-build compilation is 2–3× faster
- The use case: you don't need optimized output for a debug build; you need it to compile fast so the edit-compile-test cycle stays short

**Wasmtime + Cranelift**:
- Wasmtime (Bytecode Alliance's WASM runtime) uses Cranelift as its tier-1 JIT
- Firefox uses Cranelift as its WASM baseline compiler (tier 1 before the optimizing tier)
- Fast validation + fast code generation is the right trade-off for a runtime that needs to start executing WASM modules quickly

```
Cranelift IR design:
  Register-based (not stack machine)
  Explicit SSA from construction (no alloca/mem2reg)
  Simple instruction set — close to a hardware ISA
  Fast register allocation: linear scan (not graph coloring)
  No LLVM-style pass manager — single-pass lowering

  vs LLVM:
    LLVM: ~100 passes, complex IR, slow to compile, excellent output
    Cranelift: ~5 passes, simple IR, fast to compile, acceptable output
    For debug builds: Cranelift wins (fast cycle)
    For release builds: LLVM wins (optimized output)
```

---

## Compiler Correctness and Testing

```
How compilers are tested
=========================

  Unit tests on passes:
    Feed known IR → apply one pass → check output IR

  End-to-end correctness tests:
    Compile program → run → check output matches expected

  Randomized testing (fuzzing):
    AFL, libFuzzer: generate random inputs → find crashes/hangs
    Compiler fuzzing: generate random (but syntactically valid) programs
    CSmith: random C programs for GCC/Clang correctness testing

  Differential testing:
    Compile same program with GCC and Clang → outputs must match
    (This caught hundreds of GCC/Clang miscompilation bugs)

  Translation validation:
    Formally verify that optimization pass preserves semantics
    Alive2: SMT-based validator for LLVM peephole optimizations
    Checks that output IR is equivalent to input IR for all inputs

  CompCert (Xavier Leroy):
    Formally verified C compiler (in Coq)
    Every compilation step proved correct
    Used in safety-critical systems (aviation, nuclear)
    Slower than GCC/Clang but produces no miscompilations
```

---

## Common Confusion Points

**SSA φ functions are not runtime branches.**
A φ node at the top of a basic block is a compiler abstraction meaning "take the value from whichever predecessor executed." It's resolved by the register allocator — in the output code, it becomes a register assignment along each predecessor edge, not a conditional instruction.

**Inlining is not always a win.**
Inlining eliminates call overhead and enables further optimization. But it increases code size, which hurts instruction cache efficiency. The "inlining heuristic" (based on estimated code size increase and hotness) is one of the most empirically tuned parts of optimizing compilers. JITs handle this better than AOT compilers because they know actual hotness.

**Deoptimization is normal, not a failure.**
V8 deoptimizing a Turbofan-compiled function when a type assumption is violated is designed behavior. The code falls back to Ignition and continues profiling. Pathological deopt loops (repeated optimize → deopt → optimize) are a performance problem but a rare one in practice.

**The TypeScript type checker is not the emitter.**
SWC and esbuild both strip TypeScript types without type checking. They produce valid JavaScript from syntactically valid TypeScript even if `tsc` would report type errors. This is correct behavior for a bundler — type checking is the developer's concern; the bundler's concern is throughput. In CI you run `tsc --noEmit` for type checking, `esbuild` for bundling.

**WASM linear memory ≠ safe memory.**
WASM's sandbox prevents escaping the tab/process, but within the WASM module, linear memory is an untyped byte array. A buffer overflow in a C program compiled to WASM corrupts its own linear memory just as it would in native code. WASM safety guarantees are about isolation from the host, not memory safety within the module. Rust-compiled WASM is memory-safe; C-compiled WASM is not.

---

## Compiler Landscape Map

```
Compiler          Source    Target          IR / Key Tech
════════          ══════    ══════          ════════════════════════
rustc             Rust      native/WASM     HIR → MIR (borrow check) → LLVM IR
clang             C/C++     native/WASM     Clang AST → LLVM IR
GCC               C/C++     native          GIMPLE + RTL (pre-LLVM era IR)
tsc               TS        JS              Own AST + flow graph, no opt
SWC               TS/JS     JS              Rust-based, strips types only
esbuild           TS/JS     JS bundle       Go, single pass, no type check
Turbofan          JS        native          Sea of nodes, speculative JIT
GraalVM           JVM+      native          Partial evaluation, Truffle
Cranelift         Rust cfg  native/WASM     Simple IR, used in Wasmtime/Firefox
Binaryen          WASM      WASM (opt)      Optimizes .wasm binaries (wasm-opt)
MLIR              any       any             Meta-IR framework (Google, multi-level)
```

---

## Decision Cheat Sheet

| I need to understand... | Key concept |
|---|---|
| Why V8 is fast after warmup | Turbofan JIT + speculative type narrowing |
| Why V8 is slow at startup | Ignition interpreter; Turbofan compilation takes time |
| Why esbuild is 100× faster than Webpack | Go + single pass + no type checking |
| Why tsc is slow on large codebases | TC type system + structural subtyping depth |
| Where the Rust borrow checker lives | MIR — the CFG-based mid-level IR |
| Why Rust compiles slowly | LLVM IR generation + full LLVM optimization pipeline |
| How WASM achieves portability | Stack machine bytecode + structured control flow |
| Why SSA is in every serious compiler | Makes def-use chains trivial → enables all scalar opts |
| What LTO does | Cross-module inlining + whole-program DCE at link time |
| How JIT beats AOT on peak throughput | Profile-guided speculative optimization unavailable to AOT |
| Why φ nodes exist | Control flow merges require explicit value selection in SSA |
| How CompCert differs from GCC | Formally verified (Coq proof) — no miscompilations |
| When to use Cranelift vs LLVM backend | Cranelift: fast debug cycles; LLVM: optimized release builds |
| How Roslyn differs from tsc architecturally | Roslyn: per-file SemanticModel, lazy; tsc: global TypeChecker |
