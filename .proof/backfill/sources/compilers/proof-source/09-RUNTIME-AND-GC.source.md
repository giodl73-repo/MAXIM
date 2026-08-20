---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "09-RUNTIME-AND-GC.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:compilers:runtime-and-gc
kind: guide
module: compilers
section: compilers
title: The Runtime - Memory Model, Garbage Collection, JIT, Deoptimization
status: source-custody
source_custody: partial
current_path: compilers/09-RUNTIME-AND-GC.md
canonical_path: compilers/09-RUNTIME-AND-GC.md
backsource_ids: [proof-backfill:compilers:09-runtime-and-gc, git-history:compilers:09-runtime-and-gc]
concepts: [runtime, memory model, garbage collection, mark-sweep, copying, generational, JIT, deoptimization, safepoints]
root_concepts: [runtime, garbage collection]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# The Runtime — Memory, Garbage Collection, and the JIT

## The Big Picture

Generated code does not run in a vacuum — it runs inside a **runtime**: the layer
that lays out objects in memory, reclaims dead memory (garbage collection), and, for
managed languages, compiles bytecode to native code on the fly (the JIT) using the
profile the running program provides. This is the last stage of the pipeline and the
environment all the earlier stages target. The two big algorithmic stories are the
**GC family** (mark-sweep, copying, generational, concurrent tri-color) and the **JIT
+ deoptimization** mechanism that makes speculation safe.

```
+--------------------------------------------------------------------------+
|                          THE RUNTIME                                     |
|                                                                          |
|   +----------------------------------------------------------------+     |
|   |  EXECUTION ENGINE                                              |     |
|   |    interpreter (bytecode) <--> JIT (tiered, speculative)       |     |
|   |    deoptimization on broken assumptions                       |     |
|   +----------------------------------------------------------------+     |
|   +----------------------------------------------------------------+     |
|   |  MEMORY MANAGER                                               |     |
|   |    stack frames (guide 08)  |  heap + allocator               |     |
|   |    GARBAGE COLLECTOR: find live objects from ROOTS, reclaim   |     |
|   |    the rest (mark-sweep / copying / generational / concurrent)|     |
|   +----------------------------------------------------------------+     |
|   +----------------------------------------------------------------+     |
|   |  METADATA & SUPPORT                                           |     |
|   |    object layout / type info, stack maps + safepoints,        |     |
|   |    exception unwinding, threads, the OS boundary (mmap)       |     |
|   +----------------------------------------------------------------+     |
+--------------------------------------------------------------------------+
```

Read it as three cooperating subsystems: execute code, manage memory, and carry the
metadata (stack maps, type info) that lets the first two work together — the GC needs
the JIT's stack maps to find pointers; the JIT needs safepoints to let the GC run.

---

## The Memory Model and Object Layout

```
  STACK                          HEAP
  =====                          ====
  per-thread, LIFO frames        shared, dynamically allocated
  fast (bump the SP)             allocator-managed, GC-collected (managed langs)
  locals, spill slots, return    objects whose lifetime escapes a frame
  addr (guide 08)
  auto-reclaimed on return       reclaimed by GC or manual free()

  A managed object's layout (typical):
     +----------------+
     | header / mark  |
     +----------------+
     | field 0        |
     | field 1        |
     | ...            |
     +----------------+

  header / mark  = type pointer, GC mark bits, hash, lock word
  field 0..n     = references to other heap objects = the OBJECT GRAPH
                   (the edges the GC traces)
```

Escape analysis (a JIT optimization, guide 06) decides whether an object can be
**stack-allocated** (or scalar-replaced into registers) because it never escapes its
frame — avoiding the heap and the GC entirely. This is one of the biggest JIT wins
and impossible for many AOT languages without whole-program analysis.

---

## Garbage Collection — Finding the Live Set

Every tracing GC answers one question: starting from the **roots** (stack slots,
registers, globals), which heap objects are reachable? Everything else is garbage.

```
  ROOTS  ->  object graph  ->  reachable = LIVE, unreachable = GARBAGE

     root (a stack local) --> A --> B
                              |      \--> C
                              +----> D            E   F      (E,F unreachable
                                                              -> collect them)

  The GC needs to know WHERE the pointers are:
     STACK MAPS (from the JIT, per safepoint) say which stack slots/registers
     hold object references at this exact point. Without them the GC can't
     distinguish a pointer from an integer (precise GC) -- or it must scan
     conservatively (Boehm GC: treat anything that looks like a pointer as one).
```

### The GC Algorithm Family

```
  MARK-SWEEP                          COPYING (semispace, Cheney)
  ==========                          ===========================
  1. MARK: trace from roots, set       Two spaces: FROM and TO.
     a mark bit on each live object.    Trace from roots, COPY each live
  2. SWEEP: walk the heap, free          object to TO-space, leaving a
     unmarked objects (add to freelist). forwarding pointer behind.
  + no object movement (pointers stable) Swap roles. FROM-space (all garbage)
  - FRAGMENTATION; sweep scans all heap   is reclaimed wholesale.
  - freelist allocation slower           + compacts (no fragmentation),
                                          + allocation = bump a pointer (fast),
                                          + cost proportional to LIVE data only
                                          - needs 2x address space, moves objects
                                          - must update all pointers (forwarding)
```

```
  MARK-COMPACT
  ============
  Mark like mark-sweep, then SLIDE live objects to one end -> compaction
  without doubling memory. Slower than copying but no 2x space.
  (The .NET GC compacts gen2 this way.)
```

### Generational GC — the Practical Default

The **generational hypothesis**: most objects die young. So segregate by age and
collect the young generation often (cheap) and the old generation rarely.

```
  +-----------------+     promote survivors     +------------------+
  |  YOUNG GEN      | ------------------------> |  OLD GEN         |
  |  (nursery/gen0) |                           |  (gen2)          |
  | collected OFTEN |                           | collected RARELY |
  |  copying GC,    |                           |  mark-compact    |
  |  cheap (few     |                           |  (big, mostly    |
  |   survivors)    |                           |   long-lived)    |
  +-----------------+                           +------------------+

  THE WRITE BARRIER -- the key mechanism:
     A young-gen collection must treat OLD->YOUNG pointers as roots (an old
     object may be the only thing keeping a young object alive). Scanning all
     of old gen would defeat the purpose. So the compiler emits a WRITE
     BARRIER on every pointer store that records old->young references in a
     REMEMBERED SET (or card table). Young-gen GC scans only the remembered
     set, not all of old gen.
```

The write barrier is **code the compiler generates** — every reference-field store in
managed code includes (or may include) a barrier. This is the runtime reaching back
into code generation (guide 08): GC design dictates what the backend must emit.

### Concurrent and Tri-Color GC

To avoid long stop-the-world pauses, modern collectors run mostly *concurrently* with
the program. The correctness framework is the **tri-color invariant**.

```
  TRI-COLOR ABSTRACTION:
     WHITE  = not yet visited (candidate garbage)
     GREY   = visited, but its children not yet scanned (the wavefront)
     BLACK  = visited, children all scanned (definitely live)

  Invariant to preserve while the MUTATOR (program) runs concurrently:
     NO BLACK object may point to a WHITE object
     (without that white being reachable via some grey) -- else the GC could
     free a live object.

  The mutator can violate this by storing a white pointer into a black object.
  WRITE BARRIERS restore it:
     - Dijkstra (incremental update): shade the stored-to white object grey.
     - Yuasa (snapshot-at-the-beginning): shade the OVERWRITTEN object grey.

  Production concurrent collectors (G1, ZGC, Shenandoah, .NET background GC)
  build on this -> sub-millisecond pauses on multi-GB heaps.
```

| Collector | Strategy | Pause profile |
|-----------|----------|---------------|
| Mark-sweep | trace + freelist | stop-the-world, fragmenting |
| Copying (Cheney) | semispace, compacting | stop-the-world, fast young gen |
| Generational | young copying + old mark-compact | short young pauses, rare full GC |
| .NET GC | generational, background (concurrent) gen2 | workstation/server modes |
| G1 (JVM) | region-based, incremental, mostly concurrent | predictable pause targets |
| ZGC / Shenandoah | concurrent, load/read-barrier, colored ptrs | sub-ms, heap-size-independent |

GC algorithm theory connects to `os/` (virtual memory, `mmap`, page protection that
read-barrier collectors exploit) and `computer-architecture/` (cache behavior, the
cost of pointer-chasing during marking).

---

## The JIT — Speculation and Deoptimization

A managed runtime starts by interpreting bytecode, profiles it, and JIT-compiles hot
methods with the full optimizer (guide 06) — speculating on the observed profile.

```
  TIERED EXECUTION:
     Tier 0  interpreter / quick JIT   -- start fast, COLLECT PROFILE
        | method gets hot (call/loop counters cross a threshold)
        v
     Tier 1  optimizing JIT            -- inline, devirtualize, vectorize using
                                          the PROFILE (which types/branches occurred)

  SPECULATION example:
     virtual call site that has ONLY EVER seen type Foo:
        emit:  if (recv.type == Foo) { <inlined Foo.m()> }   // fast path
               else { DEOPTIMIZE }                            // bail out
     -> a guarded, inlined, devirtualized call -- provably impossible for a
        static AOT compiler, which must handle every possible type.
```

### Deoptimization — making speculation safe

```
  When a guard fails (a never-before-seen type arrives, an assumption breaks),
  the JIT cannot just "be wrong." It DEOPTIMIZES:
     1. stop at a safe point in the optimized code,
     2. RECONSTRUCT the interpreter's state (locals, stack) from the
        optimized frame using a DEOPT MAP recorded at compile time,
     3. resume execution in the interpreter (tier 0) at the equivalent point.

  This is why speculation is sound: the fast path is an OPTIMISTIC BET with a
  guaranteed correct fallback. Deopt is normal operation, not an error.
  (A pathological optimize<->deopt loop is a perf bug, but rare.)
```

### Safepoints and Stack Maps — the GC/JIT contract

```
  The GC must find all roots, which means the program must be at a point where
  the JIT can describe the stack precisely. SAFEPOINTS are those points
  (loop back-edges, call sites, allocation sites) where threads can be paused
  and a STACK MAP describes which registers/slots hold live references.

  GC requests a collection -> all mutator threads roll forward to the next
  safepoint -> GC reads the stack maps -> traces -> resumes threads.

  This ties three guides together:
     guide 07 (allocation) decided WHERE values live (regs vs spill slots),
     guide 08 (codegen) emitted the safepoints + write barriers,
     guide 09 (here) consumes the stack maps to trace precisely.
```

---

## AOT vs JIT, Revisited at the Runtime Level

```
  JIT runtime (HotSpot, V8, RyuJIT/CLR):
     + speculative optimization on real profiles, adaptive
     - warmup cost, memory for the compiler, less predictable latency

  AOT runtime (Go, Rust, .NET NativeAOT, GraalVM Native Image):
     + instant startup, no warmup, smaller/predictable footprint
     - no runtime profile -> can't speculate (PGO closes part of the gap);
       often a "closed world" (no dynamic class/code loading)

  Both still need a RUNTIME for GC (if managed), exception handling, threads,
  and stack maps -- AOT just doesn't include a compiler in it. NativeAOT ships
  the .NET GC and type system without RyuJIT; Go ships its GC and scheduler.
```

The ecosystem-level tour of these runtimes (V8 tiers, HotSpot C1/C2, GraalVM) lives in
`computing/22-COMPILERS.md`; here we built the mechanisms (stack maps, deopt, GC) those
runtimes share.

---

## Old World → New World Bridges

| You know | Maps to |
|----------|---------|
| .NET GC generations (gen0/1/2) | Textbook generational GC — gen0 nursery (copying), gen2 mark-compact |
| GC modes (workstation vs server, background GC) | Stop-the-world vs concurrent/background tri-color collection |
| LOH (Large Object Heap) | A separate, non-compacting region for big allocations — a real-GC engineering detail |
| RyuJIT + tiered compilation / Dynamic PGO | The tiered JIT + profile-guided speculation described here |
| `GCHandle`, pinning, `fixed` | Telling the GC "don't move this" — defeats compaction so native code can hold a raw pointer |
| Crashes from bad P/Invoke pointers | The stack-map / precise-GC contract broken at the managed/native seam |
| `Span<T>` / `stackalloc` | Stack allocation / escape avoidance — keep data off the GC heap |

The headline bridge: **.NET's gen0/gen1/gen2 *is* generational GC, and "server GC" vs
"background GC" is the stop-the-world vs concurrent tri-color choice.** Your intuition
about gen0 being cheap and gen2 collections being the expensive ones is exactly the
generational hypothesis plus the write-barrier/remembered-set machinery making
old→young references cheap to find.

---

## Decision Cheat Sheet

| I want to... | Use |
|---|---|
| Find live objects | Trace from roots (stack maps + globals) |
| Reclaim with stable pointers | Mark-sweep (accepts fragmentation) |
| Compact + fast allocation | Copying (Cheney) or mark-compact |
| Exploit "most objects die young" | Generational GC + write barrier + remembered set |
| Minimize pause times | Concurrent tri-color GC (G1/ZGC/Shenandoah/.NET background) |
| Keep correctness while collecting concurrently | The tri-color invariant + Dijkstra/Yuasa write barriers |
| Keep an object off the GC heap | Escape analysis → stack allocation / scalar replacement |
| Optimize hot code with real data | Tiered JIT + profile-guided speculation |
| Make speculation safe | Guards + deoptimization (deopt maps) |
| Let the GC pause threads safely | Safepoints + stack maps |
| Start instantly, no warmup | AOT (NativeAOT / GraalVM) — give up runtime speculation |
| Pin memory for native interop | `fixed`/`GCHandle` — but it defeats compaction |

---

## Common Confusion Points

**The GC finds garbage by finding the *live* set, not the dead set.** Tracing
collectors mark everything reachable from roots and reclaim the rest. They never
"detect" a dead object directly — death is "not reachable." (Reference counting is the
exception, and it fails on cycles.)

**Copying GC cost is proportional to *live* data, not heap size.** A semispace
collector touches only surviving objects (copying them); all garbage is reclaimed by
swapping spaces. This is why young-gen copying is cheap when most objects die young.

**The write barrier is compiler-emitted code, not a GC-only thing.** Every
reference-field store in managed code may carry a barrier so generational and
concurrent collectors can maintain their invariants. GC design dictates codegen (guide
08) — they are not separable.

**Deoptimization is correctness, not failure.** A JIT speculates on the profile and
guards the assumption; when the guard fails it reconstructs interpreter state and falls
back. The fast path is an optimistic bet with a guaranteed-correct fallback. Frequent
deopt is a perf bug, but a single deopt is normal.

**Safepoints are why a GC can't run "anywhere."** Precise tracing needs the stack
described by a stack map, which only exists at safepoints. Threads roll forward to a
safepoint before the GC reads roots — that handshake (guides 07/08/09) is the whole
precise-GC contract.

**"WASM/native is memory-safe" is false in general.** Sandboxing isolates a module from
the host, but within it, C-compiled code has the same buffer-overflow bugs as native C.
GC and memory safety come from the *language/runtime*, not from the compilation target —
see `computing/22-COMPILERS.md`.

**AOT still has a runtime.** Removing the JIT does not remove the GC, exception
handling, threads, or type metadata. NativeAOT and Go binaries embed a full runtime
minus the compiler — "no runtime" usually means "no JIT," not "no managed services."
