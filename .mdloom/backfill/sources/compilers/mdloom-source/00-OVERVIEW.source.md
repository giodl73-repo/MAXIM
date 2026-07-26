---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "00-OVERVIEW.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:compilers:overview
kind: guide
module: compilers
section: compilers
title: The Compiler Pipeline, Front to Back - Landscape
status: source-custody
source_custody: partial
current_path: compilers/00-OVERVIEW.md
canonical_path: compilers/00-OVERVIEW.md
backsource_ids: [mdloom-backfill:compilers:00-overview, git-history:compilers:00-overview]
concepts: [compiler pipeline, frontend, middle-end, backend, IR, AOT, JIT]
root_concepts: [compilers]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# The Compiler Pipeline, Front to Back — Landscape

## The Big Picture

A compiler is a function from source text to machine code, but the interesting
structure is the *pipeline* that function factors into. The factoring is not
arbitrary: it isolates language-specific concerns (the frontend), target-specific
concerns (the backend), and the language-and-target-independent optimization
machinery in the middle. The single most consequential idea in modern compiler
engineering — LLVM's organizing principle — is that the middle can be *shared*.

You know the theory: regular languages and DFAs do lexing, context-free grammars
and pushdown automata do parsing, and the static semantics is a type system. This
module is about what a backend team actually builds on top of that theory — the
algorithms, the data structures, and the engineering trade-offs that separate a
toy compiler from clang, RyuJIT, V8, or HotSpot.

```
+----------------------------------------------------------------------------+
|                          THE COMPILER PIPELINE                             |
|                                                                            |
|   FRONTEND            |        MIDDLE-END         |       BACKEND          |
|   (language-specific) |   (language + target      |   (target-specific)    |
|                       |     independent)          |                        |
|                       |                           |                        |
|  source text          |                           |                        |
|     |                 |                           |                        |
|     v                 |                           |                        |
|  +--------+   tokens   |                           |                       |
|  | LEXER  |---------+  |                           |                       |
|  | (DFA)  |   [01]  |  |                           |                       |
|  +--------+         v  |                           |                       |
|                  +--------+    AST                 |                       |
|                  | PARSER |----------+             |                       |
|                  | (LL/LR)|   [02]   |             |                       |
|                  +--------+          v             |                       |
|                              +-------------+ typed |                       |
|                              |  SEMANTIC   | AST   |                       |
|                              |  ANALYSIS   |-----+ |                       |
|                              | (types,scope|[03]| |                        |
|                              +-------------+     v |                       |
|                                         +-----------------+                |
|                                         |  IR / SSA / CFG |  [04]          |
|                                         +--------+--------+                |
|                                                  |                         |
|                                   +--------------+--------------+          |
|                                   |   DATAFLOW ANALYSIS  [05]   |          |
|                                   |   OPTIMIZATION       [06]   |          |
|                                   |   (iterate to fixpoint)     |          |
|                                   +--------------+--------------+          |
|                                                  | optimized IR            |
|                                                  v                         |
|                       |                  +---------------+  [08]           |
|                       |                  | INSTRUCTION   |                 |
|                       |                  | SELECTION +   |                 |
|                       |                  | SCHEDULING    |                 |
|                       |                  +-------+-------+                 |
|                       |                          v                         |
|                       |                  +---------------+  [07]           |
|                       |                  | REGISTER      |                 |
|                       |                  | ALLOCATION    |                 |
|                       |                  +-------+-------+                 |
|                       |                          v                         |
|                       |                  +---------------+                 |
|                       |                  | EMIT: asm /   |                 |
|                       |                  | machine code  |                 |
|                       |                  +-------+-------+                 |
|                       |                          v                         |
|                       |              +-----------------------+  [09]       |
|                       |              | RUNTIME: loader, GC,  |             |
|                       |              | stack maps, JIT, ABI  |             |
|                       |              +-----------------------+             |
+----------------------------------------------------------------------------+
   [NN] = the guide in this directory that covers that stage in depth
```

**Read this top-to-bottom.** Characters become tokens, tokens become a tree, the
tree gets a type and a meaning, the meaning is lowered to an intermediate
representation, the IR is analyzed and rewritten until a fixpoint, and then it is
mapped onto a specific machine. The runtime is the environment the emitted code
executes inside.

---

## The Three-Phase Split — Why It Exists

The frontend/middle/backend partition is the load-bearing architecture of every
production compiler. Each phase has a different *reason to change*.

```
  +-------------+        +-------------+        +-------------+
  |  FRONTEND   |        | MIDDLE-END  |        |   BACKEND   |
  +-------------+        +-------------+        +-------------+
  Changes when the      Changes when you       Changes when you
  SOURCE LANGUAGE       improve OPTIMIZATION    add a new TARGET
  changes               (new pass, better       (x86, ARM, RISC-V,
  (new syntax, new      alias analysis)         WASM)
   type rule)
        |                      |                      |
        v                      v                      v
   N languages            1 optimizer            M targets
        \                      |                      /
         \                     |                     /
          +----- IR is the narrow waist ------------+

  Without a shared IR:  N x M compilers to build and maintain.
  With a shared IR:     N frontends + M backends. The classic
                        "narrow waist" architecture.
```

This is exactly why LLVM exists. clang (C/C++), rustc, swiftc, and Zig all lower to
**LLVM IR**, and LLVM provides one optimizer and many backends. The ecosystem-level
view of who shares which middle-end lives in `computing/22-COMPILERS.md`; here we
build the pieces.

| Phase | Input | Output | Independent of |
|-------|-------|--------|----------------|
| Frontend | source text | typed AST | the target machine |
| Middle-end | IR (SSA/CFG) | optimized IR | both source and target |
| Backend | optimized IR | machine code | the source language |

---

## Old World → New World Bridges

You have prior art. These map the classical mental model onto modern systems.

| You know (classical / .NET / MS) | Maps to (modern compiler engineering) |
|----------------------------------|----------------------------------------|
| The Dragon Book "phases" picture | The pipeline above — but the middle-end is now the center of gravity |
| MSIL / CIL bytecode | A stack-based IR; RyuJIT lowers it to a register-based internal IR with SSA |
| `csc` produces IL, the CLR JITs it | Two-stage: AOT to IL, then JIT to native — the JIT *is* a backend run at load time |
| NGen / ReadyToRun (precompiled IL) | AOT compilation of bytecode — same idea as GraalVM Native Image |
| Roslyn `SyntaxTree` + `SemanticModel` | The frontend: parser produces syntax, binder/checker produces semantics |
| "Optimizer settings" (`/O2`) | A pass *pipeline* — an ordered list of IR-to-IR rewrites |
| Profiler-guided optimization (PGO) | The runtime feeds real type/branch data back into a re-JIT (guide 09) |

The most important shift from the classical picture: in 1986 the optimizer was an
afterthought bolted between parsing and codegen. Today the **IR + optimizer is the
product** (LLVM, the JVM C2 compiler, RyuJIT), and frontends/backends are clients.

---

## AOT vs JIT — The Spectrum, Not a Binary

The same pipeline runs either before execution (ahead-of-time) or during it
(just-in-time). The difference is *when* the backend runs and *what information* it
has.

```
   AHEAD-OF-TIME                            JUST-IN-TIME
   =============                            ============
   Run the whole pipeline once,            Interpret first, compile hot code
   before the program ships.               while the program runs.

   +-------------------+                   +-------------------+
   | full pipeline     |                   | interpreter       |
   | -> native binary  |                   |   (collects type  |
   +-------------------+                   |   + branch        |
                                           |     profile)      |
                                           +---------+---------+

   Sees: static program text                         | hot threshold
   Cannot see: actual inputs                         v

                                           +-------------------+
   Examples:                               | optimizing JIT    |
     gcc, clang, rustc, Go,                | (speculates using |
     GraalVM Native Image,                 |  real profile)    |
     .NET Native / NativeAOT               +---------+---------+

                                                     | assumption broken
   Wins: startup, no warmup,                         v

         predictable, smaller RSS          +-------------------+
                                           |DEOPTIMIZE -> back |
                                           |to interpreter     |
                                           +-------------------+
                                           Examples: V8, HotSpot,
                                             RyuJIT, SpiderMonkey

   Key asymmetry:
     AOT must be correct for ALL inputs.
     JIT has SEEN the inputs -> it can speculate (assume `x` is always
       an int, inline the one observed call target) and fall back if wrong.
```

The full treatment of the JIT, tiering, speculation, and deoptimization is guide
**09**; the ecosystem-level tour (V8 tiers, HotSpot C1/C2, Cranelift) is in
`computing/22-COMPILERS.md`. This module builds the components both kinds of
compiler share.

---

## A Single Statement, Through the Whole Pipeline

To anchor the rest of the module, trace one assignment all the way down. Source:

```
  x = (a + b) * (a + b);
```

```
  LEX [01]        IDENT(x) EQ LPAREN IDENT(a) PLUS IDENT(b) RPAREN
                  STAR LPAREN IDENT(a) PLUS IDENT(b) RPAREN SEMI

  PARSE [02]              =
                        /   \
                       x     *
                            / \
                          +     +
                         / \   / \
                        a   b a   b

  SEMA [03]       resolve a,b,x to symbols; check all are `int`;
                  annotate every node with type `int`. Result type ok.

  IR (TAC) [04]   t1 = a + b
                  t2 = a + b
                  t3 = t1 * t2
                  x  = t3

  SSA [04]        t1 = a + b           (each name assigned once)
                  t2 = a + b
                  t3 = t1 * t2
                  x1 = t3

  OPTIMIZE [06]   GVN sees t1 and t2 compute the same value:
                  t1 = a + b
                  x1 = t1 * t1         (t2, t3 folded away)

  CODEGEN [08]    mov  eax, [a]        ; instruction selection
                  add  eax, [b]
                  imul eax, eax
                  mov  [x], eax

  REGALLOC [07]   t1 lives only across two uses -> EAX, no spill needed

  RUNTIME [09]    `x`, `a`, `b` are slots in this frame's stack map;
                  if `x` were a heap pointer, the GC would find it here.
```

Every later guide zooms into one of those steps. The redundancy elimination
(`t2` gone) is the kind of win SSA makes trivial — that thread runs through guides
04, 05, and 06.

---

## What This Module Is — and Is Not

```
  IS:  the engineering of real compiler backends
       - subset construction, LALR tables, SSA via dominance frontiers,
         dataflow lattices + fixpoint, Chaitin coloring, instruction
         selection, GC algorithms
       - bridges to LLVM / RyuJIT / V8 / HotSpot

  IS NOT:  a re-derivation of automata or type theory
       - DFAs, CFGs, lambda calculus, the typing judgment forms are
         ASSUMED. We use them; we do not teach them.
       - For the meaning of programs (operational/denotational semantics,
         Curry-Howard, dependent types): programming-language-theory/
       - For the ecosystem survey (which compiler is which, the JIT
         tour at product level): computing/22-COMPILERS.md
```

---

## Where Each Stage Lives in This Directory

| Stage | Guide | One-line scope |
|-------|-------|----------------|
| Lexing | `01-LEXING.md` | regex → NFA → DFA → min; maximal munch; lexer generators |
| Parsing | `02-PARSING.md` | LL(k) vs the LR family; LALR conflicts; error recovery |
| Semantics | `03-SEMANTIC-ANALYSIS.md` | symbol tables, scope, type checking vs inference, AST |
| IR | `04-INTERMEDIATE-REPRESENTATION.md` | TAC, basic blocks, CFG, SSA, φ placement |
| Dataflow | `05-DATAFLOW-ANALYSIS.md` | lattices, meet, fixpoint, liveness, dominators |
| Optimization | `06-OPTIMIZATION.md` | GVN, DCE, LICM, inlining, loop opts, the pipeline |
| Reg alloc | `07-REGISTER-ALLOCATION.md` | graph coloring vs linear scan, spilling |
| Codegen | `08-CODE-GENERATION.md` | instruction selection, scheduling, the ABI |
| Runtime | `09-RUNTIME-AND-GC.md` | object layout, GC algorithms, JIT, deopt |

---

## Cross-References

```
  compilers/  (this directory — IMPLEMENTATION depth)
       |
       +-- computing/22-COMPILERS.md   ecosystem survey (LLVM/V8/rustc/tsc),
       |                               the JIT spectrum at product level
       |
       +-- programming-language-theory/  the MEANING layer:
       |     01-LAMBDA-CALCULUS, 02-TYPE-THEORY (inference -> guide 03 here),
       |     03-OPERATIONAL-SEM, 08-COMPILER-SEMANTICS (SSA/CPS semantics)
       |
       +-- computer-architecture/      pipelines, caches, ISAs, hazards
       |                               (what codegen + scheduling target)
       |
       +-- os/                         loaders, virtual memory, the
       |                               runtime/OS boundary (mmap, threads)
       |
       +-- formal-methods/06-PROGRAM-ANALYSIS.md
                                       abstract interpretation, the lattice
                                       framework (the theory under dataflow),
                                       translation validation (Alive2/CompCert)
```

---

## Decision Cheat Sheet

| I want to understand... | Read |
|---|---|
| Why compilers are split into three phases | The narrow-waist argument above |
| Why one IR can serve C, Rust, and Swift | The shared middle-end / LLVM insight |
| Why a JIT can beat an AOT compiler | The AOT/JIT asymmetry — speculation on real inputs |
| How a single statement flows end-to-end | The worked trace above |
| Which guide covers a given pipeline stage | The "Where Each Stage Lives" table |
| The semantics behind SSA/CPS, not the algorithm | `programming-language-theory/08-COMPILER-SEMANTICS.md` |
| Which real compiler uses what | `computing/22-COMPILERS.md` |

---

## Common Confusion Points

**"Frontend / backend" here is not the web sense.** Compiler frontend = the
language-facing half (lex/parse/sema). Backend = the machine-facing half
(codegen/regalloc). Nothing to do with browsers and servers.

**The middle-end is where modern compilers live.** The classical Dragon Book
picture makes optimization look like a small box. In LLVM, the JVM, and RyuJIT the
IR + optimizer is the largest and most valuable component; frontends and backends
are comparatively thin.

**A JIT is not "an interpreter that got faster."** A JIT *is* a compiler backend
that runs at execution time. The interpreter tier exists to collect a profile and
to provide a fallback when speculation fails — not as the thing that eventually
"becomes" the JIT.

**"IR" is not one thing.** rustc has HIR/THIR/MIR/LLVM-IR; a JIT may have bytecode
plus an internal SSA IR. Each level discards information the next level does not
need. The narrow waist is a *level*, not a single data structure.

**Pipeline order is logical, not strictly sequential.** Real compilers interleave,
cache, and run phases lazily (Roslyn's `SemanticModel` is on-demand; incremental
compilers re-run only affected phases). The linear picture is the contract, not the
schedule.
