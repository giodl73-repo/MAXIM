---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "05-DATAFLOW-ANALYSIS.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:compilers:dataflow-analysis
kind: guide
module: compilers
section: compilers
title: Dataflow Analysis - Lattices, Fixpoint, Liveness, Dominators
status: source-custody
source_custody: partial
current_path: compilers/05-DATAFLOW-ANALYSIS.md
canonical_path: compilers/05-DATAFLOW-ANALYSIS.md
backsource_ids: [mdloom-backfill:compilers:05-dataflow-analysis, git-history:compilers:05-dataflow-analysis]
concepts: [dataflow analysis, lattice, fixpoint, meet, reaching definitions, liveness, available expressions, dominators, worklist]
root_concepts: [dataflow analysis]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Dataflow Analysis — Lattices, Fixpoint, and Liveness

## The Big Picture

Optimization needs *facts*: which definitions reach this use, which variables are
live here, which expressions are already computed. Dataflow analysis computes these
facts by iterating transfer functions over the CFG until nothing changes — a
fixpoint. The whole framework is one piece of order theory: facts form a **lattice**,
the **meet** operator combines facts at control-flow joins, the transfer functions
are **monotone**, and the iteration is guaranteed to terminate at the **least (or
greatest) fixpoint**. You know lattices and fixed points; this guide instantiates
them as the optimizer's analysis engine.

```
+--------------------------------------------------------------------------+
|                    THE DATAFLOW FRAMEWORK                                |
|                                                                          |
|   A lattice L of "facts"      +  a CFG  +  transfer functions            |
|        TOP  (most optimistic /                                           |
|             "no info yet")                                               |
|         |                                                                |
|       .....    (lattice of facts, ordered by information)                |
|         |                                                                |
|       BOTTOM (most conservative / "anything possible")                   |
|                                                                          |
|   For each block B:                                                      |
|     IN[B]  = MEET over predecessors of OUT[p]   (forward analysis)       |
|     OUT[B] = transfer_B( IN[B] )  =  GEN[B] U (IN[B] - KILL[B])          |
|                                                                          |
|   Iterate until IN/OUT stop changing  =>  FIXPOINT.                      |
|   Monotone transfer + finite-height lattice  =>  guaranteed to halt.     |
|                                                                          |
|   Direction:  forward (reaching defs) | backward (liveness)              |
|   Meet:       union (may) | intersection (must)                          |
+--------------------------------------------------------------------------+
```

Read it as a fill-in template: pick a lattice, a direction, a meet, and GEN/KILL
sets, and the iteration engine is identical across analyses.

---

## The Lattice — Facts Ordered by Information

A dataflow value is an element of a lattice: a partially ordered set where every pair
has a meet (greatest lower bound) and join (least upper bound). The order encodes
"how much we know."

```
  Constant-propagation lattice for one variable:

                TOP   (no information yet -- "could be anything,
                 |     start optimistic")
        +--------+--------+----- ...
        |        |        |      ...
       ...0      1        2  ...   (each known constant)
        +--------+--------+----- ...
                 |
               BOTTOM  (NOT a constant -- "overdefined", conservative)

    MEET rules:
       meet(TOP, x)   = x          (TOP is identity -- defers to any fact)
       meet(c, c)     = c          (same constant -> still that constant)
       meet(c1, c2)   = BOTTOM     (c1 != c2 -> not constant on all paths)
       meet(BOTTOM,x) = BOTTOM     (already overdefined)
```

```
  Key properties the framework requires:
    FINITE HEIGHT: no infinite descending chains -> iteration must stop.
    MONOTONE transfer functions: if x <= y then f(x) <= f(y)
       -> facts only move DOWN the lattice; never oscillate.
    These two together = the fixpoint exists and is REACHED in finite steps
       (Kleene / Knaster-Tarski).
```

The lattice direction convention varies by textbook (some put "optimistic" at top,
some at bottom). What is invariant: meet moves toward *less* information, transfer
functions are monotone, and the height bounds the iteration count.

---

## The Generic Iterative Algorithm

Every classical analysis is the same loop with different parameters.

```
  initialize IN[B], OUT[B] to TOP (or the boundary condition at entry/exit)
  repeat:
    changed = false
    for each block B (in a good order):
       IN[B]  = MEET over preds p of OUT[p]        # forward
       newOUT = GEN[B] U (IN[B] - KILL[B])         # transfer
       if newOUT != OUT[B]: OUT[B] = newOUT; changed = true
  until not changed     # FIXPOINT
```

```
  Parameters that define a specific analysis:
    DIRECTION   forward (IN from preds) | backward (OUT from succs)
    MEET        union (MAY/exists-a-path) | intersection (MUST/all-paths)
    TRANSFER    GEN/KILL sets per block
    BOUNDARY    value at entry (forward) or exit (backward)
    INITIAL     interior blocks start at the meet identity
```

| Analysis | Direction | Meet | "GEN" | Question answered |
|----------|-----------|------|-------|-------------------|
| Reaching definitions | forward | union (may) | defs in block | which defs might reach here? |
| Live variables | backward | union (may) | uses before defs | is this value needed later? |
| Available expressions | forward | intersection (must) | exprs computed, not killed | is `a+b` already computed on all paths? |
| Very busy / anticipated | backward | intersection (must) | exprs used before redef | will this expr be used on all paths? |
| Constant propagation | forward | constant lattice meet | const evals | is this a known constant here? |

The **may vs must** distinction is exactly the union/intersection choice: "may" =
some path (union, optimistic merges weaken), "must" = all paths (intersection,
pessimistic merges).

---

## Worked: Reaching Definitions

"Which assignments to a variable might be the source of its value at a given point?"
Forward, union.

```
  d1: x = 1          B0
      if p goto B2
  ------------------------
  d2: x = 2          B1
      goto B3
  ------------------------
  (B2): y = x        B2     <- uses x
      goto B3
  ------------------------
  (B3): z = x        B3     <- uses x, a MERGE of B1 and B0->B2

  GEN/KILL for x's defs {d1,d2}:
    B0: GEN={d1}, KILL={d2}     OUT[B0] = {d1}
    B1: GEN={d2}, KILL={d1}     OUT[B1] = {d2}
    B2: GEN={},   KILL={}       IN[B2]=OUT[B0]={d1} -> use of x sees d1
    B3: IN[B3] = OUT[B1] U OUT[B2] = {d2} U {d1} = {d1,d2}
        -> the use of x in B3 may be reached by EITHER def. (union = may)
```

In SSA this analysis is nearly free: each use already names its single defining
version (or a φ that lists the reaching versions). SSA *is* reaching-definitions
pre-solved — which is exactly why the SSA-based optimizer in guide 06 skips much of
this machinery.

---

## Worked: Liveness

"Is the value in this variable used on some path before being overwritten?" Backward,
union. The defining analysis for register allocation (guide 07).

```
  A variable is LIVE at a point if there is a path from that point to a USE
  of it, with no intervening redefinition.

  Backward transfer:
     IN[B]  = use[B] U (OUT[B] - def[B])
     OUT[B] = UNION over successors s of IN[s]

  Example:
     B1: a = 1                 def {a}
         b = 2                 def {b}
         if a goto B3
     B2: c = a + b   ; use a,b
     B3: return b    ; use b

     Liveness (backward):
       IN[B3] = {b}                       (b used)
       IN[B2] = {a,b}                     (a,b used)
       OUT[B1] = IN[B2] U IN[B3] = {a,b}
       IN[B1]  = {} U (OUT[B1] - {a,b}) = {}   (a,b defined in B1)

     Reading the result: across the branch, a and b are both live (needed by
     B2 or B3) -> they must occupy registers there. After B2 uses them, a may
     die. These LIVE RANGES are the input to register allocation.
```

---

## Worked: Available Expressions (a MUST analysis)

"Is `a+b` already computed and still valid on *every* path here?" Forward,
**intersection**. Enables common-subexpression elimination.

```
     B1: t = a + b          GEN {a+b}
         if p goto B3
     B2: u = a + b          GEN {a+b}
         goto B4
     B3: a = 9              KILL anything mentioning a  (a+b no longer valid)
         goto B4
     B4: v = a + b          <- is a+b available?

     IN[B4] = OUT[B2] INTERSECT OUT[B3]
            = {a+b}  INTERSECT  {}   (B3 killed a+b)
            = {}      -> a+b NOT available on all paths -> cannot reuse.

     If B3 did not redefine a, the intersection would keep {a+b} and CSE
     could replace `v = a + b` with `v = t` (or `v = u`). The intersection
     (MUST) is what makes this safe -- a union would wrongly reuse a value
     that one path invalidated.
```

This is the textbook reason meet must be intersection for "must" properties:
optimizing on a fact that holds on only *one* path would be unsound.

---

## Dominators as a Dataflow Problem

Dominance (guide 04) is itself a forward, **intersection** dataflow analysis — the
same engine, applied to the CFG's own structure.

```
  DOM[B] = {B} UNION ( INTERSECT over predecessors p of DOM[p] )
  DOM[entry] = {entry}

  Iterate to fixpoint:
     "A dominates B" means A is in DOM[B].
     A block is dominated by itself and by everything that dominates ALL
     its predecessors (intersection -> every path) .

  CFG:  entry -> B0 -> {B1,B2} -> B3
     DOM[entry] = {entry}
     DOM[B0]    = {entry,B0}
     DOM[B1]    = {entry,B0,B1}
     DOM[B2]    = {entry,B0,B2}
     DOM[B3]    = {B3} U (DOM[B1] INTERSECT DOM[B2])
                = {B3} U ({entry,B0,B1} INTERSECT {entry,B0,B2})
                = {B3,entry,B0}        (B1,B2 drop out -- not on every path)
```

In production, Lengauer-Tarjan or Cooper-Harvey-Kennedy compute the dominator *tree*
directly (faster than the set-based iteration above), but the dataflow formulation
shows dominance is the same kind of object as liveness and reaching defs — and it is
the backbone of SSA construction, LICM, and loop detection.

---

## Worklist Algorithms and Iteration Order

Re-evaluating every block each round is wasteful — only blocks whose inputs changed
need recomputation. The **worklist** algorithm tracks exactly those.

```
  worklist = all blocks
  while worklist not empty:
     B = pop()
     recompute OUT[B] (or IN[B] for backward)
     if it changed:
        push B's successors (forward) / predecessors (backward)

  ITERATION ORDER MATTERS for speed (not correctness):
     forward analysis  -> REVERSE POSTORDER (process a block after its preds)
     backward analysis -> POSTORDER
     Good order: a reducible CFG converges in (loop-nesting-depth + 2) passes.
```

```
  Cost picture:
     iterations bounded by  (lattice height) x (CFG size)
     reverse-postorder makes most analyses converge in a handful of passes
     SSA + sparse analysis: propagate only along def-use edges, skipping
        blocks where nothing relevant happens -> far fewer evaluations.
```

The sparse, SSA-based version (sparse conditional constant propagation, guide 06) is
the modern default: instead of dense IN/OUT per block, facts flow along SSA def-use
edges, touching only the instructions that matter.

---

## Old World → New World Bridges

| You know | Maps to |
|----------|---------|
| "Definite assignment" errors in C# | A forward dataflow analysis — the compiler proves every local is assigned before use |
| Nullable reference analysis (C# 8 `?`) | Dataflow tracking null-state through the CFG; the lattice is {not-null, maybe-null, null} |
| Roslyn `ControlFlowAnalysis` / `DataFlowAnalysis` APIs | These literally expose reaching-defs/liveness results over a method's CFG |
| Reachability warnings ("unreachable code") | CFG reachability — a degenerate dataflow over the control graph |
| Escape analysis (JIT) you've read about | A dataflow/points-to analysis deciding if an object outlives its frame |
| Knaster-Tarski / lattice fixpoints (MIT) | The exact termination guarantee — finite-height lattice + monotone transfer |

The headline bridge: **C#'s "use of unassigned local variable" and nullable analysis
are textbook dataflow.** The compiler runs a forward analysis over the method CFG; the
lattice elements are assignment/null states; the meet at merges is what makes
`if (x != null) {...}` narrow on one branch and not the other. You have been reading
dataflow diagnostics for years.

---

## Decision Cheat Sheet

| I want to... | Use |
|---|---|
| Frame any analysis | Lattice + direction + meet + transfer (GEN/KILL) |
| Guarantee termination | Finite-height lattice + monotone transfer functions |
| Combine facts at a join | Meet: union for "may", intersection for "must" |
| Find which defs reach a use | Reaching definitions (forward, union) |
| Find which values are needed later | Liveness (backward, union) |
| Reuse already-computed expressions | Available expressions (forward, intersection) → CSE |
| Compute dominance | Forward intersection dataflow, or Lengauer-Tarjan for the tree |
| Iterate efficiently | Worklist + reverse-postorder (forward) / postorder (backward) |
| Skip the dense iteration | SSA-based sparse analysis (propagate along def-use edges) |

---

## Common Confusion Points

**Meet direction is about information, not control flow.** "Meet" combines facts at
joins toward *less* certainty. For "may" properties the meet is union; for "must"
properties it is intersection. Picking the wrong one makes the analysis unsound, not
just imprecise.

**May vs must = union vs intersection.** A "may" fact holds if *some* path provides it
(union, optimistic). A "must" fact holds only if *every* path provides it
(intersection). CSE needs "available on all paths" (must/intersection); dead-code
needs "live on some path" (may/union).

**Termination comes from the lattice, not the program.** Even with loops, iteration
halts because the lattice has finite height and transfer functions are monotone —
facts only move one direction and run out of room. An infinite-height lattice (e.g.
exact integer sets) needs *widening* (see `formal-methods/06-PROGRAM-ANALYSIS.md`).

**Iteration order affects speed, never the answer.** Reverse-postorder converges
faster, but any fair order reaches the same least fixpoint. Order is a performance
knob.

**SSA pre-solves reaching definitions.** In SSA every use already names its defining
version (or a φ of them), so the classic reaching-defs pass is largely redundant —
one reason the SSA optimizer is leaner than the classical dense-dataflow optimizer.

**Dominance is dataflow too.** It is the same iterative framework (forward,
intersection) applied to the CFG itself, which is why dominators, liveness, and
reaching defs all share one engine — and why guide 04's SSA construction and this
guide's analyses are the same machine.
