---
maxim_schema: maxim.frontmatter.v1
id: maxim:compilers:intermediate-representation
kind: guide
module: compilers
section: compilers
title: Intermediate Representation - Three-Address Code, CFG, SSA Form
status: source-custody
source_custody: partial
current_path: compilers/04-INTERMEDIATE-REPRESENTATION.md
canonical_path: compilers/04-INTERMEDIATE-REPRESENTATION.md
backsource_ids: [proof-backfill:compilers:04-intermediate-representation, git-history:compilers:04-intermediate-representation]
concepts: [intermediate representation, three-address code, basic block, control flow graph, SSA, phi function, dominance frontier]
root_concepts: [intermediate representation]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Intermediate Representation — TAC, the CFG, and SSA

## The Big Picture

The IR is where the optimizer lives, and the choice of IR is the single most
consequential design decision in a compiler backend. The modern answer is nearly
universal: linearize the AST into three-address code, group it into basic blocks
connected by a control-flow graph, and convert to **Static Single Assignment** form.
SSA is in LLVM, GCC (GIMPLE), V8 Turbofan, the JVM C2, and rustc's MIR. This guide
builds the IR ladder and the SSA construction algorithm — dominance frontiers and
all.

```
                            THE IR LADDER

    typed AST (tree, control flow implicit)

         |  flatten: introduce temporaries, sequence operations
         v

    THREE-ADDRESS CODE   (each op: x = y <op> z;
                          at most one operator, ~3 operands)
    +-------------------------+
    |  t1 = a + b             |
    |  t2 = t1 * c            |
    +-------------------------+

         |  split at branch targets / branches
         v

    BASIC BLOCKS   (one entry, one exit, no internal jumps;
                    edges = control flow)
    +-------------------------+
    |  straight-line runs;    |
    |  edges = control flow   |
    +-------------------------+

         |  connect blocks by branch edges
         v

    CONTROL-FLOW GRAPH (CFG)   (nodes = blocks,
                                edges = possible jumps)
    +-------------------------+
    |   B0 -> B1 -> B3        |
    |    \-> B2 ->/           |
    +-------------------------+

         |  rename each def uniquely; phi at merges
         v

    SSA FORM   (every variable assigned EXACTLY ONCE;
                phi selects by predecessor at merges)
    +-------------------------+
    |  x1 = ...   x2 = ...    |
    |  x3 = phi(x1, x2)       |
    +-------------------------+

         |
         v   to dataflow (05) + optimization (06)
```

Read top-down: the tree flattens to a linear instruction sequence, the sequence
partitions into basic blocks, the blocks form a CFG, and the CFG is renamed into SSA.
Every later optimization assumes this shape.

---

## Three-Address Code

TAC flattens nested expressions into a sequence where each instruction has at most
one operator. The "three addresses" are the destination and (up to) two sources.

```
  source:  d = a * b + a * b * c

  TAC (introduce temporaries left-to-right):
     t1 = a * b
     t2 = a * b
     t3 = t2 * c
     t4 = t1 + t3
     d  = t4

  The redundancy (t1 and t2) is now SYNTACTICALLY visible -- exactly what
  makes common-subexpression elimination a local pattern match instead of
  a tree traversal. That is the whole point of flattening.
```

```
  TAC instruction shapes:
     x = y op z        binary
     x = op y          unary
     x = y             copy
     x = &y / x = *y   address / load (low-level TAC)
     goto L            unconditional jump
     if x relop y goto L   conditional jump
     x = call f, n     call
     param x / return x    calling-convention glue
```

TAC sits below the AST (control flow is now explicit jumps) and above machine code
(unbounded temporaries, no registers yet). LLVM IR is essentially typed TAC in SSA
form; MSIL/CIL is a *stack*-based cousin that the JIT lowers into register-based TAC.

---

## Basic Blocks and the CFG

A **basic block** is a maximal straight-line sequence: control enters only at the
top and leaves only at the bottom. You find them by marking *leaders*.

```
  Leaders are:
    1. the first instruction,
    2. any target of a jump,
    3. any instruction immediately AFTER a jump.
  A basic block runs from a leader up to (not including) the next leader.
```

```
  TAC with labels:                 CFG:
   B0: t = n                         +-----+
       if t <= 1 goto B2             | B0  |  if t<=1
                                     +--+--+
   B1: r = n * fact(n-1)          F  /     \  T
       goto B3                      v       v

                                 +-----+ +-----+
   B2: r = 1                     | B1  | | B2  |
                                 +--+--+ +--+--+
   B3: return r                     \       /
                                     v     v

                                     +-----+
                                     | B3  |
                                     +-----+
```

```
  CFG vocabulary you'll use constantly:
    predecessors / successors of a block
    entry block (no predecessors except itself)
    back edge (target dominates source) -> marks a LOOP
    critical edge (from a block with >1 successor to a block with >1
       predecessor) -> often SPLIT before SSA destruction / phi lowering
    reducible CFG (loops have single entry headers) -> the well-behaved
       case structured languages produce; irreducible CFGs (from goto
       spaghetti) need extra care
```

The CFG is the substrate for everything in guides 05–07: dataflow runs over it,
dominance is defined on it, and register allocation colors values whose live ranges
span its edges.

---

## SSA — Static Single Assignment

In SSA, **every variable is assigned exactly once**. Reassignments become fresh
versioned names, and where control-flow paths merge, a **φ (phi) function** selects
the right version based on which predecessor executed.

```
  NON-SSA                         SSA
  =======                         ===
  x = 1                           x1 = 1
  if cond:                        if cond:
      x = 2                           x2 = 2
  y = x + 1                       x3 = phi(x1, x2)     <- merge point
                                  y1 = x3 + 1

  phi(x1, x2) means: "take x1 if we arrived from the then-less path,
  x2 if from the `if` body." It is a COMPILE-TIME selector, not a runtime
  branch -- the register allocator turns it into a move on each incoming edge.
```

### Why SSA — the payoff

```
  USE-DEF CHAINS BECOME TRIVIAL
    Every use of x2 has EXACTLY ONE definition. Finding "all defs of x"
    in non-SSA needs global analysis; in SSA it's a single pointer.

  CONSTANT PROPAGATION BECOMES LOCAL
    x1 = 5 ; y = x1 + 3  ->  follow the one def  ->  y = 8.

  DEAD CODE ELIMINATION IS REACHABILITY
    A value with no uses and no side effects is dead -> delete -> repeat.

  GVN / CSE BECOMES HASHING
    Two instructions with identical operator + operand VERSIONS compute
    the same value. Hash on (op, operand-versions) -> dedup across blocks.

  SPARSE ANALYSES
    SSA lets you propagate facts along def-use edges directly, instead of
    re-deriving them at every program point (sparse vs dense dataflow).
```

This is why SSA is the universal modern IR. The single-assignment property turns
several global analyses into local pointer-following.

---

## Constructing SSA — Dominance and Phi Placement

The classic Cytron et al. algorithm: compute dominators, compute **dominance
frontiers**, insert φ at the frontiers, then rename. This is the precision core.

### Dominance

```
  Block A DOMINATES block B if EVERY path from entry to B passes through A.
  (Every block dominates itself. The entry dominates everything.)

  A STRICTLY dominates B if A dominates B and A != B.
  The IMMEDIATE dominator idom(B) is the unique strict dominator of B that
  is dominated by every other strict dominator of B -- B's parent in the
  DOMINATOR TREE.
```

```
  CFG:                  Dominator tree:
     entry                 entry
       |                     |
       B0                    B0
      /  \                  /|\
    B1    B2              B1 B2 B3
      \  /                       (B3's idom is B0, NOT B1 or B2 --
       B3                         neither B1 nor B2 is on EVERY path
       |                          to B3, but B0 is)
       B4                   B4 hangs under B3
```

The dominator tree is computed with Lengauer-Tarjan in near-linear O(E·α(E)) time,
or the simpler Cooper-Harvey-Kennedy iterative algorithm that is fast in practice.

### Dominance Frontier — exactly where phis go

```
  The DOMINANCE FRONTIER of block A, DF(A), is the set of blocks B such that:
     A dominates a PREDECESSOR of B,  but  A does NOT strictly dominate B.

  Intuition: DF(A) is the set of merge points "just beyond" A's region of
  control -- the first places where a value defined in A's dominated region
  could meet a value from elsewhere. THAT is precisely where a phi is needed.
```

```
  PHI PLACEMENT (iterated dominance frontier):
    For each variable v:
      Workset = { blocks that DEFINE v }
      For each block A in the worklist:
        for each B in DF(A):
          if B has no phi for v yet:
            insert  v = phi(...)  at the top of B
            if B did not already define v, add B to the worklist
              (a phi is itself a definition -> may trigger more phis)
    => the ITERATED dominance frontier of the definition set.
```

```
  Worked example -- variable x defined in B1 and B2:

     B0: (entry, branches to B1 or B2)
     B1: x = 1   ;  goto B3
     B2: x = 2   ;  goto B3
     B3: use x

     DF(B1) = {B3}   (B1 dominates its own only-pred-of-B3? B1 is a pred of
                      B3, and B1 does not strictly dominate B3 -> B3 in DF(B1))
     DF(B2) = {B3}   (same reasoning)
     => insert  x3 = phi(x1, x2)  at the top of B3.  Correct: B3 is the merge.
```

### Renaming

After φ insertion, walk the dominator tree, keeping a per-variable version stack:
each definition pushes a new version; each use takes the current top; φ operands are
filled from the version live on each incoming edge.

```
  Before rename:                After rename (versions):
   B1: x = 1                     B1: x1 = 1
   B2: x = 2                     B2: x2 = 2
   B3: x = phi(x, x)            B3: x3 = phi(x1 [from B1], x2 [from B2])
       use x                        use x3
```

This minimal-φ construction places exactly the φ-functions that are needed — the
iterated dominance frontier guarantees neither too few (every reaching def is
covered) nor redundantly many.

---

## Leaving SSA — Phi Elimination

SSA is great for analysis but machines have no φ instruction. Before register
allocation you *destruct* SSA, replacing each φ with copies on the incoming edges.

```
  SSA:                          After phi elimination:
   B1: ... ; goto B3            B1: ... ; x3 = x1 ; goto B3
   B2: ... ; goto B3            B2: ... ; x3 = x2 ; goto B3
   B3: x3 = phi(x1, x2)         B3: (phi gone) use x3
       use x3
```

```
  The lost-copy and swap problems:
    Naive copy insertion can clobber a value still needed by a PARALLEL phi
    (e.g. x3=phi(...) and y3=phi(...) that swap x and y). The fix:
       - SPLIT CRITICAL EDGES so copies have a place to live, and
       - treat all phis in a block as PARALLEL (sequentialize with a temp,
         like a register swap), so  x,y = y,x  doesn't lose a value.
```

This phase hands the (now φ-free) CFG to register allocation (guide 07); the inserted
copies are exactly what coalescing later tries to remove.

---

## Old World → New World Bridges

| You know | Maps to |
|----------|---------|
| MSIL / CIL bytecode | A *stack-based* IR; RyuJIT imports it, builds a CFG, and converts to its own SSA-ish IR for optimization |
| `Expression` trees (LINQ) | An AST-level IR — tree-shaped, not yet linearized to TAC |
| Reading disassembly with basic blocks (windbg) | The CFG made concrete — leaders are the jump targets you see |
| .NET `RyuJIT` phases | Importer → morph → SSA-based optimizations → LSRA → codegen; SSA sits in the middle exactly as here |
| GIMPLE (if you've seen GCC dumps) | GCC's three-address SSA IR — same ladder, different syntax |
| Profiler "hot path" overlays | Edges/blocks of the CFG annotated with execution counts |

The headline bridge: **CIL is a stack machine; the JIT does not optimize the stack
form.** It rebuilds a CFG and a register-based SSA IR first, because dataflow and SSA
optimizations are intractable on a stack representation. The "two IRs" pattern (a
portable stack bytecode plus an internal SSA IR) is shared by .NET, the JVM, and
WASM engines.

---

## Decision Cheat Sheet

| I want to... | Use |
|---|---|
| Make redundant computations visible | Three-address code (flatten the AST) |
| Make control flow explicit | Basic blocks + the CFG |
| Find basic blocks | Mark leaders (targets, post-jumps, first instr) |
| Detect loops | Back edges (target dominates source) in the CFG |
| Make use-def chains trivial | SSA form |
| Decide where φ-functions go | Iterated dominance frontier of the defs |
| Compute dominance fast | Lengauer-Tarjan or Cooper-Harvey-Kennedy |
| Get out of SSA before codegen | φ elimination with critical-edge splitting + parallel copies |
| Optimize CIL/JVM bytecode | Import → CFG → SSA, then optimize (don't optimize the stack form) |

---

## Common Confusion Points

**A φ-function is not a runtime branch.** It is a compile-time selector that says
"use the value from whichever predecessor we came from." It vanishes during SSA
destruction, becoming a register copy on each incoming edge — never a conditional
instruction.

**SSA versions are not new variables at runtime.** `x1, x2, x3` are the *same*
storage at runtime; the subscripts are a compile-time renaming that gives each
definition a unique name so analyses can follow def-use edges by pointer.

**Dominance frontier is not "successors of A."** DF(A) is where A's dominance *stops* —
merge points just outside A's dominated region. Confusing it with successors places
φs in the wrong blocks. The defining condition: A dominates a *predecessor* of B but
not B itself.

**Phi placement uses the *iterated* dominance frontier.** A φ is itself a definition,
so inserting one can require further φs downstream. Stopping after one pass under-
places φs. The worklist iterates until fixed.

**Leaving SSA is not free.** φ elimination inserts copies, and naive insertion hits
the lost-copy/swap bugs. Critical-edge splitting plus parallel-copy sequencing is
mandatory for correctness, and the inserted copies are what coalescing later removes.

**Irreducible CFGs exist.** `goto`-heavy or computed-jump code can produce loops with
multiple entries (no single header). SSA construction still works, but some loop
optimizations assume reducibility; compilers either node-split to reducible form or
fall back to conservative handling.
