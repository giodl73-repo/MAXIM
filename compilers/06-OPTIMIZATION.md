---
maxim_schema: maxim.frontmatter.v1
id: maxim:compilers:optimization
kind: guide
module: compilers
section: compilers
title: Optimization - Local, Global, Interprocedural Passes, GVN, LICM, Inlining
status: source-custody
source_custody: partial
current_path: compilers/06-OPTIMIZATION.md
canonical_path: compilers/06-OPTIMIZATION.md
backsource_ids: [proof-backfill:compilers:06-optimization, git-history:compilers:06-optimization]
concepts: [optimization, constant propagation, GVN, dead code elimination, LICM, inlining, loop optimization, pass pipeline]
root_concepts: [optimization]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Optimization — From Peephole to Whole-Program

## The Big Picture

Optimization is a sequence of semantics-preserving IR-to-IR rewrites, each justified
by a dataflow fact from guide 05. The passes are organized by *scope* — within a
basic block (local), across the CFG of one function (global), and across function
boundaries (interprocedural) — and they run in a carefully ordered *pipeline* because
one pass exposes opportunities for the next. SSA (guide 04) makes most of them cheap.
This guide is the catalog and the ordering logic, with the classic algorithms stated
precisely.

```
+--------------------------------------------------------------------------+
|                     OPTIMIZATION BY SCOPE                                |
|                                                                          |
|   LOCAL (one basic block)                                                |
|     constant folding, local CSE, local DCE, peephole, algebraic         |
|     simplification, local copy/constant propagation                     |
|        |                                                                 |
|        v                                                                 |
|   GLOBAL / INTRAPROCEDURAL (one function's CFG, needs dataflow)         |
|     global constant propagation (SCCP), GVN, global DCE,                |
|     LICM, loop unrolling/fusion, strength reduction, vectorization,     |
|     jump threading, tail-call elimination                               |
|        |                                                                 |
|        v                                                                 |
|   INTERPROCEDURAL (across functions / whole program)                    |
|     inlining, interprocedural constant propagation,                     |
|     devirtualization, escape analysis, whole-program DCE,               |
|     Link-Time Optimization (LTO)                                         |
|                                                                          |
|   All wired into a PASS PIPELINE: ordered, often run to a fixpoint,     |
|   gated by -O0/-O1/-O2/-O3/-Os.                                          |
+--------------------------------------------------------------------------+
```

Read top-down by widening scope: each tier sees more context and can prove more, at
greater cost. The pipeline interleaves them so cheap local cleanups feed expensive
global analyses and vice versa.

---

## Local Optimizations

Within a single basic block, control flow is trivial (straight line), so these need
no dataflow — just a forward scan.

```
  CONSTANT FOLDING        2 + 3        -> 5          (evaluate at compile time)
  ALGEBRAIC SIMPLIFY      x * 1        -> x
                          x + 0        -> x
                          x & x        -> x
  STRENGTH REDUCTION      x * 4        -> x << 2     (cheap op for expensive)
                          x % 8        -> x & 7      (power-of-two)
  LOCAL CSE               t1 = a+b; t2 = a+b  -> t1 = a+b; t2 = t1
  COPY PROPAGATION        y = x; z = y+1 -> z = x+1
  LOCAL DCE               t = a+b (t never used) -> delete
  PEEPHOLE                mov eax,eax  -> delete; redundant load after store
```

Peephole optimization slides a small window over the instruction stream and replaces
recognized patterns. It runs late (on near-machine code) to clean up what earlier
passes and instruction selection leave behind. LLVM's `InstCombine` is the
industrial-strength version at the IR level.

---

## Global Optimizations (SSA-Powered)

These span the whole function CFG. In SSA they collapse from dense dataflow into
sparse, def-use-edge propagation.

### Sparse Conditional Constant Propagation (SCCP)

The strong form of constant propagation: it propagates constants *and* discovers
unreachable branches simultaneously, so each makes the other more powerful.

```
  SCCP lattice per SSA value:  TOP (unknown) > constant c > BOTTOM (varying)
  Two worklists: SSA edges (value changes) and CFG edges (reachability).

  if (x1 == 0)  where SCCP proved x1 = 0  -> the `else` edge is UNREACHABLE
     -> code in the else block is dead (won't even be analyzed)
     -> a phi merging that dead edge ignores it -> may become constant too

  Why "conditional" beats plain constant propagation:
     plain CP assumes all branches reachable -> a phi at a merge sees both
        a constant and a dead value -> conservatively BOTTOM.
     SCCP knows the dead edge can't contribute -> the phi stays constant.
```

### Global Value Numbering (GVN)

Assign each *value* a number; two computations with the same number are the same
value and one can be eliminated — across basic blocks, unlike local CSE.

```
  Hash each instruction on (operator, value-numbers-of-operands).
  Identical hash = identical value = redundant.

  In SSA this is clean because operand NAMES are their value identities:
     a = x + y      VN(a) = h(+, VN(x), VN(y)) = #7
     b = x + y      VN(b) = h(+, VN(x), VN(y)) = #7   -> b is redundant
     replace uses of b with a.

  GVN vs CSE:
     local CSE: only within a block, syntactic match.
     GVN: across the whole CFG, by computed value -- catches
          a = x+y in B1 and b = x+y in B3 even with blocks between.
```

### Global DCE

```
  A value is dead if it has no uses AND no side effects.
  In SSA: build the use-def graph, mark all roots (returns, stores, calls
  with effects, volatile ops), keep everything reachable backward from roots,
  delete the rest. One graph sweep, repeat to fixpoint.
```

---

## Loop Optimizations

Loops are where programs spend their time, so loop transforms dominate the payoff.
They require loop structure (back edges, headers, preheaders) from the dominator tree.

### Loop-Invariant Code Motion (LICM)

```
  Move a computation OUT of the loop if its operands don't change in the loop.

   before:                          after (hoist to PREHEADER):
   for i in 0..n:                   t = a * b          # invariant -> hoisted
       x = a * b                    for i in 0..n:
       use(x, i)                        use(t, i)

  Safety conditions:
    - operands (a,b) are loop-invariant (defs dominate the loop, not redefined)
    - the instruction is SAFE TO SPECULATE or DOMINATES all loop exits
        (else you'd execute it when the loop runs zero times -- may fault
         or have effects). LICM only hoists when it can't change behavior.
    - a PREHEADER block exists (a single entry edge into the loop header to
       hold the hoisted code) -- compilers insert one if absent.
```

### Other Loop Transforms

```
  STRENGTH REDUCTION OF INDUCTION VARIABLES
     for i: a[i*4]   ->   p = base; for i: *p ; p += 4
     (replace multiply-by-stride with a running add -- the classic)

  LOOP UNROLLING
     replicate the body k times -> fewer branch/counter overheads, more ILP;
     enables vectorization. Cost: code size, i-cache pressure.

  VECTORIZATION (auto-SIMD)
     for i: c[i] = a[i] + b[i]  ->  process 4/8/16 lanes per SIMD instruction
     needs: no loop-carried dependence, known/aligned access, trip count.

  LOOP FUSION / FISSION
     fuse: merge two loops over the same range -> better locality, fewer
       loop overheads. fission: split a loop -> isolate vectorizable part.

  LOOP-INVARIANT + UNSWITCHING
     hoist a loop-invariant branch OUT, duplicating the loop per branch:
       for i: if cond {A} else {B}  ->  if cond { for i:A } else { for i:B }
```

The full LLVM `-O2` loop pipeline runs LICM, induction-variable simplification,
unrolling, and the loop vectorizer in sequence, each re-running cleanup passes.

---

## Interprocedural Optimization

### Inlining — the enabling optimization

```
  Replace a call with the callee's body.
     int sq(int x){ return x*x; }   ...   y = sq(a+1);
     ->  t = a+1;  y = t*t;

  WHY it matters: not the call-overhead saving (small) but what it ENABLES --
     constant propagation across the boundary, CSE, DCE, devirtualization.
     Inlining is the gateway drug of interprocedural optimization.

  THE HEURISTIC (the hard part, heavily tuned):
     inline if  estimated_speedup > code_size_cost,
       weighing: callee size, call-site hotness, whether args are constants,
       whether it enables further opts, recursion depth.
     Over-inlining -> code bloat -> i-cache misses -> SLOWER. The threshold
       is one of the most empirically tuned numbers in any compiler.
```

JITs inline better than AOT compilers because they know *actual* hotness from the
profile (guide 09); AOT compilers estimate it statically or use PGO data.

### Devirtualization

```
  A virtual/interface call has an unknown target -> can't inline.
  If analysis proves the receiver's concrete type (or there's only one
  implementer in the program), replace the indirect call with a direct one
  -> then inline it.

     Guarded devirtualization (JIT): "if type == Foo, call Foo.m() inline;
       else fall back to the virtual call." Speculate on the hot type.
```

### Whole-Program / Link-Time Optimization (LTO)

```
  Classic: each translation unit compiled independently -> no cross-module
     inlining, conservative about external functions.
  LTO: emit IR (not machine code) per unit; at link time, optimize the WHOLE
     program together -> cross-module inlining, whole-program DCE,
     devirtualization with a closed world.

  ThinLTO: per-module summaries + parallel optimization -> nearly LTO quality
     at near-normal build times (the practical default for large C++/Rust).
```

---

## The Pass Pipeline — Ordering Matters

Passes are not independent; order determines what gets caught. The pipeline runs many
passes, often iterating cleanup passes to a fixpoint.

```
  Why order matters (phase-ordering problem):
     INLINE first      -> exposes constants across the call -> then CONST-PROP
     CONST-PROP first  -> simplifies the body -> better INLINE size estimate
     -> there is no globally optimal order; compilers use a tuned schedule
        and re-run cheap passes (instcombine, simplifycfg, DCE) between
        expensive ones.

  A representative -O2 sketch (LLVM-ish):
     mem2reg (build SSA)
     -> SCCP -> instcombine -> GVN -> DCE
     -> inliner (SCC bottom-up over the call graph)
        -> [re-run SCCP, instcombine, GVN, DCE on newly inlined code]
     -> loop pipeline: LICM -> indvars -> unroll -> vectorize
     -> simplifycfg -> DCE
     -> (codegen prep, then backend)
```

| Level | Intent | Typical contents |
|-------|--------|------------------|
| -O0 | no opt, fast build, debuggable | just mem2reg maybe; 1:1 with source |
| -O1 | cheap wins | DCE, const-fold, simple inline, simplifycfg |
| -O2 | the default for release | full scalar + loop opts, inlining, vectorize |
| -O3 | aggressive | higher inline/unroll thresholds, more IPO; often only marginal over -O2 |
| -Os/-Oz | size | disable unroll/vectorize; favor small code |
| PGO | profile-driven | use real branch/hotness data to guide inline + layout |

---

## Old World → New World Bridges

| You know | Maps to |
|----------|---------|
| `/O2`, `/Ox` in MSVC | A pass pipeline preset — a named, ordered list of IR rewrites |
| RyuJIT "minopts" vs "fullopts" | The JIT's -O0-like vs -O2-like pipelines, chosen by tiering |
| .NET tiered compilation (Tier0→Tier1) | Tier0 = fast/minimal opt; Tier1 re-JITs hot methods with the full pipeline |
| `[MethodImpl(AggressiveInlining)]` | A hint nudging the inliner's cost heuristic |
| PGO in Visual Studio / `dotnet` Dynamic PGO | Profile-guided inlining + block layout — JITs do it online now |
| ReadyToRun / crossgen | AOT codegen with a (usually) -O2-ish pipeline baked at publish time |

The headline bridge: **.NET's tiering is the AOT/JIT optimization trade-off made
explicit.** Tier0 compiles fast with almost no optimization to start the app quickly;
Dynamic PGO instruments it; hot methods are re-JITted at Tier1 with inlining, guarded
devirtualization, and the loop pipeline using the *observed* profile — exactly the
"speculate on real data" advantage AOT compilers lack.

---

## Decision Cheat Sheet

| I want to... | Use |
|---|---|
| Evaluate `2+3` at compile time | Constant folding (local) |
| Replace `x*4` with `x<<2` | Strength reduction (local) |
| Remove a value with no uses | Dead code elimination (local + global) |
| Reuse a value computed elsewhere in the function | GVN (global, across blocks) |
| Propagate constants and prune dead branches together | SCCP |
| Hoist invariant work out of a loop | LICM (with a preheader) |
| Turn a scalar loop into SIMD | Auto-vectorization (no loop-carried deps) |
| Cut call overhead and enable cross-call opts | Inlining (tuned by the cost heuristic) |
| Turn a virtual call direct | Devirtualization (proven/guarded type) |
| Optimize across modules | LTO / ThinLTO |
| Use real runtime behavior | PGO / JIT Dynamic PGO |
| Get the most from -O | -O2 (–O3 rarely beats it meaningfully) |

---

## Common Confusion Points

**Inlining's value is enabling, not call-overhead.** The saved `call`/`ret` is minor.
The win is that the callee body now sees the caller's constants and context, unlocking
constant propagation, CSE, DCE, and devirtualization. Over-inline and you bloat code,
thrash the i-cache, and get *slower*.

**-O3 is not "more optimized = faster."** -O3 raises inline/unroll thresholds and adds
IPO, often producing larger binaries with marginal or negative speedups versus -O2.
-O2 is the release default for good reason.

**GVN ⊋ CSE.** Local CSE is syntactic and block-local; GVN works across the whole CFG
by computed value identity. They are not the same pass with different names.

**SCCP is stronger than const-prop + DCE run separately.** Doing reachability and
constant propagation *together* lets each strengthen the other; running them in
sequence loses the interaction (a phi over a dead edge looks non-constant).

**Phase ordering has no optimal solution.** Inlining-before-constprop and the reverse
each win on different code. Compilers use a tuned schedule and re-run cheap cleanup
passes between heavy ones — there is no order that is best for all programs.

**LICM must respect zero-trip loops and faults.** Hoisting a faulting or side-effecting
op above a loop that might run zero times changes behavior. LICM only hoists when the
op is safe to speculate or provably executes — correctness gates the win.

**Optimizations must preserve semantics — and proving that is hard.** Translation
validators (Alive2 for LLVM peepholes) and verified compilers (CompCert) exist because
miscompilations are real; see `formal-methods/06-PROGRAM-ANALYSIS.md`.
