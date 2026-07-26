---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "07-REGISTER-ALLOCATION.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:compilers:register-allocation
kind: guide
module: compilers
section: compilers
title: Register Allocation - Graph Coloring vs Linear Scan, Spilling
status: source-custody
source_custody: partial
current_path: compilers/07-REGISTER-ALLOCATION.md
canonical_path: compilers/07-REGISTER-ALLOCATION.md
backsource_ids: [mdloom-backfill:compilers:07-register-allocation, git-history:compilers:07-register-allocation]
concepts: [register allocation, interference graph, graph coloring, Chaitin, linear scan, spilling, coalescing]
root_concepts: [register allocation]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Register Allocation — Coloring vs Linear Scan

## The Big Picture

The IR has unlimited virtual registers; the machine has, say, 16. Register
allocation maps the infinitely many virtual registers (the SSA values from guide 04)
onto the finite physical register file, spilling the overflow to the stack. Two
values can share a register iff they are never *live at the same time* — so the
problem is graph coloring of an interference graph, which is NP-complete, and the
whole field is the trade-off between near-optimal coloring (Chaitin-Briggs) and the
fast-but-greedy linear scan that JITs use.

```
+--------------------------------------------------------------------------+
|                     REGISTER ALLOCATION                                  |
|                                                                          |
|   IR with unlimited virtual regs (v1, v2, v3, ...)                       |
|        |                                                                 |
|        |  LIVENESS analysis (guide 05) -> live ranges/intervals          |
|        v                                                                 |
|   +----------------------------------------------------------------+     |
|   |  INTERFERENCE: two values interfere if their live ranges       |     |
|   |  OVERLAP -> they cannot share a register.                      |     |
|   +----------------------------------------------------------------+     |
|   |    |                                                           |     |
|        +-----------------------------+----------------------------+      |
|        v                             v                            v      |
|  GRAPH COLORING               LINEAR SCAN                  SSA-BASED     |
|  (Chaitin-Briggs)            (Poletto-Sarkar)            (chordal graph) |
|  build interference graph,    sort live intervals by      color in       |
|  K-color it (K = #regs),     start, sweep, assign        polynomial time |
|  spill if can't color.        reg or spill greedily.      (SSA interf.   |
|  Quality: high. Slow.         Quality: ok. Very fast.      graphs are    |
|  Used: gcc, LLVM -O2+.        Used: JITs, RyuJIT (LSRA).   chordal)      |
|        |                             |                            |      |
|        +--------------- assign physical regs & insert -------------+     |
|        |                 SPILL loads/stores for overflow           |     |
+--------------------------------------------------------------------------+
```

Read it as: liveness produces ranges, overlap produces interference, and coloring (or
a fast sweep) assigns registers, spilling whatever does not fit.

---

## Interference and the Graph

Liveness analysis (guide 05) gives each value a **live range** — the set of program
points where it holds a value still needed. Two values *interfere* if their ranges
overlap; they cannot occupy the same register.

```
  v1 = ...        v1 live ----+
  v2 = ...        v2 live --+ |
  ... = v1        v1 dies   | |          v1 and v2 overlap -> INTERFERE
  v3 = ...        v3 live   +-|--+       v1 and v3 do NOT overlap -> may share
  ... = v2                    + |        v2 and v3 overlap -> INTERFERE
  ... = v3                      +

  INTERFERENCE GRAPH:           Coloring with K=2 registers (R0,R1):
     v1 --- v2                    v1 -> R0
            |                     v2 -> R1
            v3                    v3 -> R0   (doesn't interfere with v1)
                                  -> 2 colors suffice. No spill.
```

The core theorem: **assigning K registers without spilling = K-coloring the
interference graph** (no two adjacent nodes share a color). General graph coloring is
NP-complete, which is why exact allocation is intractable and every allocator is a
heuristic or exploits special graph structure.

---

## Graph Coloring — Chaitin-Briggs

The classic high-quality allocator. Chaitin (1981) plus Briggs's refinements
(optimistic coloring, better spilling) is what gcc and LLVM's older allocators use.

```
  THE SIMPLIFY / SELECT ALGORITHM (Kempe's heuristic):

  1. BUILD     interference graph from liveness.
  2. SIMPLIFY  repeatedly remove any node with DEGREE < K and push it on a
               stack. (Degree<K guarantees a color will be free when we
               put it back -- its <K neighbors can't use up all K colors.)
  3. SPILL     if only nodes of degree >= K remain, pick one as a POTENTIAL
               spill (lowest spill-cost / highest degree), remove it,
               push it -- mark it "may spill". Continue simplifying.
  4. SELECT    pop nodes off the stack; assign each a color not used by its
               (already-colored) neighbors.
               - a degree<K node ALWAYS gets a color.
               - a potential-spill node: BRIGGS'S OPTIMISM -- maybe its
                 neighbors didn't use all K colors after all; try to color it.
                 If a free color exists -> no actual spill. If not -> ACTUAL
                 SPILL: rewrite to load/store, rebuild, restart.
```

```
  Briggs's optimistic coloring vs Chaitin's original:
     Chaitin: a node marked for spill IS spilled.
     Briggs:  defer the decision to SELECT -- often the node colors anyway
              because its high degree included neighbors that share colors.
     Result: fewer actual spills, better code.
```

### Coalescing — removing copies

```
  After SSA destruction (guide 04) you have many copies  v2 = v1.
  If v1 and v2 DON'T interfere, give them the SAME register -> the copy
  becomes  mov R0, R0  -> deleted. This is COALESCING.

  Aggressive coalescing can raise degree and FORCE spills, so use a
  conservative rule:
     BRIGGS: coalesce only if the merged node has < K neighbors of degree >= K.
     GEORGE: coalesce a,b if every neighbor of a already interferes with b
             or has degree < K.
  Both guarantee coalescing never turns a colorable graph uncolorable.
```

Coalescing is why SSA destruction's inserted copies (guide 04) mostly vanish — the
allocator merges the source and destination into one register.

---

## Spilling

When the graph will not K-color, some value must live in memory and be loaded/stored
around each use.

```
  Spill v:  every DEF of v -> store v to a stack slot
            every USE of v -> load v from the stack slot into a temp register

   before spill:                after spilling v (stack slot [v]):
     v = a + b                    t1 = a + b ; store [v], t1
     ...                          ...
     x = v + c                    t2 = load [v] ; x = t2 + c

  The loads/stores create SHORT new live ranges (t1, t2) -> rebuild the
  interference graph and re-run. Spilling reduces register pressure but
  adds memory traffic.

  SPILL COST heuristic -- pick the cheapest value to spill:
     cost(v)  ~  (def_count + use_count, weighted by LOOP DEPTH) / degree
     -> NEVER spill a value used inside a hot loop if avoidable
        (each loop iteration pays the load/store). Spill the long-lived,
        rarely-used value with many interferences instead.
```

Loop-depth weighting is the single most important spill heuristic: a spill inside a
deep loop is paid every iteration, so allocators weight use/def counts by `10^depth`.

---

## Linear Scan — The JIT Allocator

Graph coloring is too slow for a JIT compiling on the program's critical path.
Linear scan (Poletto-Sarkar, 1999) abandons the graph for a single sweep over live
intervals — much faster, slightly worse code.

```
  Approximate each value's live range as ONE INTERVAL [start, end] over a
  linearized instruction numbering (lose the holes -> slight imprecision).

  Sort intervals by START point. Sweep left to right, keeping an ACTIVE set
  of intervals currently holding a register:

    for each interval I in start order:
       EXPIRE from active any interval that ended before I.start
                 -> free its register
       if a free register exists:  assign it to I; add I to active
       else:  SPILL the active interval with the FARTHEST end point
              (it ties up a register longest) -- or spill I itself if I
              ends even later.
```

```
  Picture:
    v1 [==========]
    v2    [====]
    v3       [==========]
    v4              [====]
       time -------------->
    With 2 registers: v1->R0, v2->R1; v2 expires -> R1 free -> v3->R1;
    v1 still live when v4 starts and both regs busy -> spill the one ending
    latest (v3) ... greedy, O(n) after the sort.
```

| | Graph coloring (Chaitin-Briggs) | Linear scan |
|---|---|---|
| Model | interference graph, K-coloring | sorted live intervals, sweep |
| Quality | high (near-optimal) | good, ~10% more spills typically |
| Speed | slow (build graph, iterate) | fast, ~O(n log n) |
| Live-range holes | precise | approximated (one interval) |
| Used by | gcc, LLVM `-O2`+ | early HotSpot client, V8 Crankshaft-era, **RyuJIT (LSRA)** |
| Coalescing | first-class | limited / second pass |

LLVM's default `greedy` allocator is a sophisticated hybrid: live-interval based like
linear scan but with splitting, eviction, and priority that recover much of coloring's
quality at acceptable cost.

---

## SSA-Based Register Allocation

A modern result: the interference graph of a program *in SSA form* is **chordal**, and
chordal graphs are colorable in polynomial time. This decouples the NP-hardness from
allocation.

```
  Insight (Hack/Brisk ~2005):
     SSA interference graphs are chordal -> optimal coloring is POLYNOMIAL.
     The hard part moves into SSA DESTRUCTION (phi -> copies) and spilling,
     not the coloring itself.

  Pipeline:
     spill to satisfy register pressure (MAXLIVE <= K via a tree scan)
     -> color the chordal SSA interference graph in poly time
     -> destruct SSA, coalescing the phi copies
```

This is why guide 04's SSA pays off again here: the same property that made dataflow
sparse makes register allocation tractable.

---

## Calling Conventions Constrain the Allocator

Allocation is not free choice — the ABI (guide 08) reserves registers and dictates
which survive calls.

```
  CALLER-SAVED (volatile): a call may clobber them. If a value is live
     ACROSS a call, the allocator must either put it in a callee-saved reg
     or spill it around the call.
  CALLEE-SAVED (non-volatile): the callee must preserve them -> using one
     costs a save/restore in the prologue/epilogue.
  FIXED registers: stack pointer, frame pointer, the ABI's argument and
     return registers (e.g. RDI/RSI.. then RAX on SysV x86-64; RCX/RDX..
     then RAX on Windows x64) are pre-committed at call sites.

  -> a value live across a call interferes with all caller-saved registers.
     This is encoded by adding interference edges, so the graph naturally
     pushes long-lived values into callee-saved regs or onto the stack.
```

---

## Old World → New World Bridges

| You know | Maps to |
|----------|---------|
| Watching RyuJIT assembly in a debugger | LSRA (Linear Scan Register Allocation) is RyuJIT's allocator — fast, JIT-suitable |
| "register pressure" intuition from reading asm | Exactly MAXLIVE vs K — too many simultaneously-live values force spills |
| Stack frame locals you've seen in disassembly | Spill slots — values the allocator couldn't keep in registers |
| x64 calling convention (RCX/RDX/R8/R9, RAX) | The fixed/caller-saved/callee-saved partition the allocator must respect |
| `[MethodImpl]` / perf of hot loops | Loop-depth spill weighting — spilling in a hot loop is the cardinal sin |
| Why debug builds are slower | -O0/minopts skip coalescing and good allocation; every local goes to a stack slot |

The headline bridge: **RyuJIT uses linear scan, gcc/LLVM use coloring, for the same
reason JIT vs AOT differs everywhere.** A JIT pays allocation cost on the program's
critical path, so it buys speed with a greedy sweep; an AOT compiler can afford the
NP-hard-flavored coloring for ~10% better code. Same trade-off as the rest of the
backend.

---

## Decision Cheat Sheet

| I want to... | Use |
|---|---|
| Decide if two values can share a register | Do their live ranges interfere? |
| Frame allocation formally | K-coloring the interference graph (K = #physical regs) |
| Get near-optimal allocation (AOT) | Chaitin-Briggs coloring (simplify/select + optimistic) |
| Allocate fast in a JIT | Linear scan over sorted live intervals |
| Remove SSA-destruction copies | Coalescing (conservative: Briggs/George) |
| Handle register overflow | Spilling, weighted by loop depth |
| Pick what to spill | Lowest (use/def, loop-weighted) / degree |
| Exploit SSA for poly-time coloring | SSA-based allocation (chordal interference graphs) |
| Handle values live across a call | Callee-saved register or spill (ABI-driven interference) |

---

## Common Confusion Points

**Register allocation is graph coloring, and that is NP-complete.** Exact allocation is
intractable in general; every production allocator is a heuristic (Chaitin-Briggs) or
exploits structure (SSA chordality) or trades quality for speed (linear scan).

**Spilling is normal, not failure.** Real functions have more live values than
registers. The allocator's job is to spill the *cheapest* values (long-lived,
rarely-used, outside loops), not to avoid spilling entirely.

**Linear scan is not "worse coloring" — it is a different model.** It never builds the
interference graph; it sweeps sorted intervals. It is chosen for speed (JITs), losing
~10% to coloring, not because coloring is unavailable.

**Coalescing can backfire.** Merging copy-related values reduces moves but raises
degree and can force a spill. Conservative coalescing (Briggs/George) only merges when
it provably cannot make a colorable graph uncolorable.

**Loop depth dominates spill cost.** A spill inside a triple-nested loop is paid on
every iteration. Allocators weight spill cost by ~10^loop-depth, so they will spill a
function-wide temp rather than a loop-body value.

**SSA makes coloring polynomial but doesn't make allocation free.** The hardness moves
into spilling and SSA destruction (φ-copy coalescing). The win is real — optimal
coloring in poly time — but the allocator still has to spill and destruct carefully.

**The ABI pre-commits registers.** The allocator does not freely use all K registers:
the stack/frame pointer, argument, and return registers are fixed at boundaries, and
values live across calls interfere with all caller-saved registers (guide 08).
