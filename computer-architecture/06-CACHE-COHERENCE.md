# Cache Coherence and Memory Consistency

## The Problem

In a multi-core processor, each core has its own L1 and L2 caches. If two cores cache the same memory address and one writes to it, the other core's cached value is now stale. Cache coherence protocols solve this. Memory consistency models define when a write by one core becomes visible to others.

These are two distinct problems that are often conflated:

```
+-----------------------------------------------------------------------+
|                    TWO DISTINCT PROBLEMS                              |
|                                                                       |
|  CACHE COHERENCE                    MEMORY CONSISTENCY                |
|  --------------------------------   --------------------------------- |
|  Single cache line problem          Ordering of multiple operations   |
|  across multiple cores              across multiple addresses         |
|                                                                       |
|  "If Core 0 writes X=1,             "If Core 0 writes X=1, Y=1,       |
|   when does Core 1 see X=1?"        does Core 1 see X=1 when it       |
|                                      sees Y=1?"                       |
|                                                                       |
|  Solved by: MESI protocol,          Defined by: memory model          |
|  snooping, directory               (TSO, PSO, WRC, SC, etc.)          |
|                                                                       |
|  Guarantee: reads see the MOST      Does NOT guarantee ordering       |
|  recent write to that address       between different addresses       |
+-----------------------------------------------------------------------+
```

---

## The MESI Protocol

The standard cache coherence protocol. Each cache line is in one of four states.

```
  MESI STATES:

  M — MODIFIED:
  This cache has the only copy, and it has been written.
  Memory is STALE — only this cache has the current value.
  Must write back to memory before sharing.
  Line is "dirty."

  E — EXCLUSIVE:
  This cache has the only copy, and it is CLEAN (matches memory).
  Can be read or written without coordination.
  (A write silently transitions to M.)

  S — SHARED:
  This cache line is shared — multiple caches may hold copies.
  All copies match memory (all clean).
  Reads are allowed without coordination.
  Writes require transitioning: must INVALIDATE all other copies first.

  I — INVALID:
  This line is not present in this cache, or has been invalidated.
  A read causes a cache miss. A write causes a miss + protocol.

  +---------------------------------------------------------------------+
  |                     MESI STATE TRANSITIONS                          |
  |                                                                     |
  |  I  ──(local read miss)──→  E   (no other sharers found)            |
  |  I  ──(local read miss)──→  S   (other sharers exist)               |
  |  I  ──(local write miss)─→  M   (invalidate others first)           |
  |  E  ──(local write)──────→  M   (silent, no bus traffic)            |
  |  E  ──(remote read)──────→  S   (share the line)                    |
  |  S  ──(local write)──────→  M   (broadcast invalidation to others)  |
  |  S  ──(remote invalidate)→  I   (another core wrote)                |
  |  M  ──(remote read)──────→  S   (write back, then share)            |
  |  M  ──(remote write)─────→  I   (write back, then invalidate self)  |
  +---------------------------------------------------------------------+
```

---

## MOESI: Adding the Owned State

```
  MOESI extends MESI with:

  O — OWNED:
  This cache has a dirty copy, but OTHER caches also have
  (shared, stale) copies.
  This cache is responsible for supplying the data on request —
  without writing back to memory first.

  WHY USEFUL:
  In MESI: if M-state core is asked to share,
  it must write back to memory, then both read from memory.
  In MOESI: M-state core can supply data directly to requester,
  both become O and S respectively.
  Avoids memory bandwidth for sharing dirty data.

  AMD processors use MOESI.
  Intel uses a modified MESIF (F = Forward variant).
  ARM uses MOESI or similar.
```

---

## Snooping vs Directory Protocols

```
  SNOOPING (for bus/ring topologies, smaller core counts):
  All caches monitor (snoop) a shared bus for memory transactions.
  When a cache sees a transaction, it checks its own state and responds.

  +─────┐   +─────┐   +─────┐
  |Core0|   |Core1|   |Core2|
  | L1  |   | L1  |   | L1  |
  +──┬──┘   +──┬──┘   +──┬──┘
     │          │          │
  ═══╪══════════╪══════════╪═══  ← Shared bus / ring
     │
  +──┴──┐
  | L3  |
  | LLC |
  +──┬──┘
     │
   DRAM

  All cores see all transactions. Simple but doesn't scale:
  Bus bandwidth = O(N) cores × O(M) cache misses per second.
  Works well for 8–32 cores.

  DIRECTORY PROTOCOL (for multi-socket, large core counts):
  A distributed directory tracks who has each cache line.
  No need for broadcast — only send coherence messages to
  cores that have a copy.

  Directory entry per memory block:
  [Present Bits: core 0...N] [Dirty Bit] [Owner Bits]

  Core 0 wants to write address X:
  1. Send request to directory for X
  2. Directory looks up: cores 1, 3, 5 have S copies of X
  3. Directory sends invalidation to cores 1, 3, 5
  4. Cores acknowledge (send INV-ACK)
  5. Directory sends write permission to Core 0
  6. Core 0 transitions to M state

  Scales to 100s-1000s of cores.
  AMD EPYC: Infinity Fabric directory protocol across chiplets.
  Intel Xeon: scalable mesh with distributed LLC and directory.
```

---

## False Sharing: The Silent Performance Killer

```
  DEFINITION:
  Two or more cores frequently write to DIFFERENT variables
  that happen to reside on the SAME cache line.

  Neither core is sharing the same variable, but the cache
  coherence protocol treats the whole line as shared.

  EXAMPLE:
  struct Counter {
    int64_t count_core0;    // offset 0
    int64_t count_core1;    // offset 8
  } counters;               // Both in SAME 64-byte cache line!

  Core 0: counters.count_core0++  → writes line, invalidates Core 1's copy
  Core 1: counters.count_core1++  → must re-acquire line, invalidates Core 0

  RESULT: Massive coherence traffic. Each write by one core
  requires the other to invalidate and re-fetch.
  Performance: can be 10-100× slower than independent writes.

  DETECTION:
  Linux perf: `perf c2c record` + `perf c2c report`
  Intel VTune: memory analysis, cache-to-cache transfer visualization

  FIX 1: PADDING
  struct Counter {
    int64_t count_core0;
    char padding[56];      // pad to 64 bytes
    int64_t count_core1;
  }; // Each field now in its own cache line

  FIX 2: C#/.NET — use [StructLayout(LayoutKind.Sequential)]
  with explicit padding or the internal PaddingHelpers approach.
  .NET has a concept of "false sharing avoidance" in the GC.

  FIX 3: PER-CORE OR PER-THREAD LOCAL ACCUMULATION
  Each thread accumulates locally, then atomically adds to global
  at the end. Thread-local storage avoids sharing entirely.

  x86: alignas(64) or __declspec(align(64))
  C#: [StructLayout(LayoutKind.Sequential, Pack=64)]
  JAVA: @sun.misc.Contended annotation
```

---

## Memory Consistency Models

Cache coherence ensures that reads see the most recent write to a GIVEN address. Memory consistency defines the ordering of reads and writes across MULTIPLE addresses.

### Sequential Consistency (SC)

```
  LAMPORT'S DEFINITION (1979):
  The result of any execution is the same as if the operations
  of all processors were executed in some sequential order,
  and the operations of each individual processor appear
  in this sequence in the order specified by its program.

  MEANING:
  1. Within each core, operations appear in program order.
  2. Globally, there exists SOME interleaving of all cores'
     operations that explains all observable results.

  ALL WRITES BECOME GLOBALLY VISIBLE SIMULTANEOUSLY.

  STRONGEST MODEL — hardware never needed.
  Even x86 TSO is slightly weaker.
  Programmer intuition matches SC.
```

### x86 TSO (Total Store Order)

```
  x86 RELAXATION: Store Buffers

  Every core has a STORE BUFFER (write buffer).
  Stores go into the buffer first, then eventually drain to cache.
  This means: a core can read its own store (from buffer)
  BEFORE it becomes visible to other cores.

  ALLOWED BY TSO but NOT by SC:

  Core 0:             Core 1:
  X = 1               Y = 1
  read Y              read X
  (sees Y = 0)        (sees X = 0)

  Under SC: impossible — one of the writes must have happened
  before the other's read.
  Under TSO: ALLOWED.
  Core 0 sees Y=0 because its store X=1 is still in its store buffer
  (not yet globally visible) when it reads Y.
  Core 1 similarly.

  IMPLICATION FOR C#/.NET:
  Without memory fences, reads can see stale values.
  C# volatile keyword: inserts the appropriate x86 fences.
  Interlocked operations: full memory fence (LOCK prefix).
  Thread.MemoryBarrier(): full fence (MFENCE instruction).

  x86 FENCE INSTRUCTIONS:
  SFENCE: Store fence — all prior stores visible before this point
  LFENCE: Load fence — all prior loads complete before this point
  MFENCE: Full fence — both loads and stores ordered
  LOCK prefix on RMW: implies full fence
```

### ARM and RISC-V: Weak Memory Models

```
  ARM and RISC-V are WEAKLY ORDERED.
  Significantly more relaxed than TSO.

  ALLOWED (under ARM WMO, not under TSO):
  - Loads can be reordered past prior stores to different addresses
  - Stores can be reordered past prior loads
  - Loads can appear reordered relative to each other

  ARM SYNCHRONIZATION PRIMITIVES:
  DMB ISH    Data Memory Barrier (inner shareable domain)
    Ensures all memory accesses before are visible before
    all accesses after.
  DMB ISHST  Store barrier only
  DMB ISHLD  Load barrier only
  DSB ISH    Data Synchronization Barrier (stronger: stalls pipeline)
  ISB        Instruction Synchronization Barrier (flush pipeline)

  LOAD-ACQUIRE / STORE-RELEASE:
  LDAR X0, [X1]    Load-Acquire: no load/store after this can
                   be reordered before it
  STLR X0, [X1]   Store-Release: no load/store before this can
                   be reordered after it

  These map directly to:
  C++ std::atomic with memory_order_acquire / memory_order_release
  C# volatile reads (LDAR) and volatile writes (STLR)
  .NET's Thread.VolatileRead / Thread.VolatileWrite

  WHY WEAK MEMORY MODELS EXIST:
  Allowing reordering = better compiler optimization
  = better hardware pipelining
  = better speculative execution
  = higher throughput at the cost of programmer complexity.
```

---

## The Memory Model Stack

The full stack from language ordering guarantees down to hardware coherence — shown universally with language instances alongside each other.

```
  +------------------------------------------------------------------------+
  |  LANGUAGE LEVEL — acquire/release semantics                            |
  |                                                                        |
  |  C++: memory_order_acquire/release on std::atomic<T>                   |
  |  Java: volatile fields, synchronized, VarHandle.getAcquire()           |
  |  Go: sync.Mutex, sync/atomic.Load/Store (seq_cst by default)           |
  |  Rust: Ordering::Acquire / Ordering::Release on atomics                |
  |  C#: volatile keyword, Interlocked, Thread.MemoryBarrier()             |
  +------------------------------------------------------------------------+
              ↕ compiler translates to
  +------------------------------------------------------------------------+
  |  RUNTIME / COMPILER LAYER                                              |
  |  C++ / Rust: direct ISA fence emission (no separate runtime layer)     |
  |  JVM: JMM specifies happens-before; HotSpot JIT emits fences           |
  |  .NET CLR: CLR memory model (stronger than C# spec minimum);           |
  |            explicit fences at volatile read/write                      |
  |  Go runtime: inserts barriers at goroutine sync points                 |
  +------------------------------------------------------------------------+
              ↕ emits
  +------------------------------------------------------------------------+
  |  ISA FENCE INSTRUCTIONS                                                |
  |  x86-64: MFENCE (full), SFENCE (stores), LFENCE (loads),               |
  |          LOCK prefix on RMW operations                                 |
  |  ARM64:  LDAR (load-acquire), STLR (store-release),                    |
  |          DMB ISH (full data memory barrier)                            |
  |  RISC-V: FENCE r,rw / FENCE rw,w (per RVWMO)                           |
  |                                                                        |
  |  x86 NOTE: TSO is so strong that acquire/release often maps to         |
  |  plain load/store — no fence emitted. ARM requires LDAR/STLR.          |
  +------------------------------------------------------------------------+
              ↕ hardware enforces
  +------------------------------------------------------------------------+
  |  CACHE COHERENCE PROTOCOL                                              |
  |  MESI / MOESI — snooping (small core count) or directory (large)       |
  |  Ensures: a read sees the most recent write to that address            |
  +------------------------------------------------------------------------+
              ↕ defines what is observable
  +------------------------------------------------------------------------+
  |  MEMORY CONSISTENCY MODEL                                              |
  |  x86: TSO (Total Store Order) — near-sequential, only store-buffer     |
  |  ARM: WMO (Weak Memory Ordering) — aggressive reorder, fences needed   |
  |  RISC-V: RVWMO (weak + composable fence semantics)                     |
  |  Java JMM: SC for DRF (data-race-free programs see SC behavior)        |
  +------------------------------------------------------------------------+
```

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| What does M-state mean in MESI? | Modified: only this cache has it, it's dirty (written), memory is stale |
| What is false sharing? | Two cores writing different variables on the same cache line, causing spurious coherence traffic |
| What is TSO? | Total Store Order — x86's memory model; stores go through a per-core buffer before becoming globally visible |
| What fence eliminates TSO reordering? | MFENCE (full fence), SFENCE (stores), LFENCE (loads) |
| What does ARM use instead of TSO? | Weak Memory Ordering — requires explicit DMB/LDAR/STLR for synchronization |
| What is the cost of a cache-to-cache transfer? | ~30–60 cycles (vs ~4 for L1 hit, ~100 for DRAM) |
| How do you fix false sharing in C#? | Pad structures to 64 bytes, or use thread-local storage |

---

## Common Confusion Points

**Cache coherence ≠ memory consistency**: Coherence guarantees: reads to an address eventually see the most recent write to THAT address. Consistency defines: the ordering of operations to MULTIPLE addresses. You need both — coherence alone is not enough for correct concurrent programs.

**Volatile in C# ≠ volatile in C/C++**: C# `volatile` provides acquire/release semantics (LDAR/STLR on ARM, implicit on x86). C/C++ `volatile` only prevents compiler optimization — it does NOT guarantee any ordering relative to other threads. These are completely different.

**MFENCE is rarely needed on x86**: x86 TSO already orders stores with respect to subsequent loads (same address). MFENCE is needed when you need a store to be globally visible BEFORE a subsequent load to a DIFFERENT address. This comes up in lock-free algorithms. Most x86 code never needs explicit MFENCE.

**MOESI "ownership" is for bandwidth**: When an M-state cache shares its line to respond to a read request, MESI forces a write-back to memory first (expensive). MOESI adds the O (Owned) state to allow direct cache-to-cache transfer without the write-back, saving memory bandwidth. The O-state cache is responsible for supplying the data.

**Software memory models stack on top of hardware**: C# volatile on x86 may not emit any instructions (x86 is already strongly ordered). The same C# volatile on ARM emits LDAR/STLR instructions. The language-level guarantee is preserved; the hardware cost varies by architecture.
