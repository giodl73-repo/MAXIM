# Memory Hierarchy: Caches to DRAM

## Why the Hierarchy Exists

The memory wall: DRAM access latency has improved ~1.3x per decade. CPU compute performance improved ~1000x per decade. The gap is enormous. Caches exist to paper over it by exploiting two principles:

- **Temporal locality**: if you accessed address X, you will likely access X again soon
- **Spatial locality**: if you accessed address X, you will likely access X±Δ soon

These principles hold for most real programs (loops, arrays, structs). They are the foundation of the entire memory hierarchy.

```
+-----------------------------------------------------------------------+
|                     MEMORY HIERARCHY                                  |
|                                                                       |
|   LEVEL    SIZE         LATENCY    BANDWIDTH    TECHNOLOGY            |
|   -------  -----------  ---------  -----------  -----------           |
|   Register  <1 KB       0 cycles   ∞            flip-flops            |
|   L1 I$    32–64 KB     ~4 cycles  ~1 TB/s      6T SRAM               |
|   L1 D$    32–64 KB     ~4 cycles  ~1 TB/s      6T SRAM               |
|   L2       256KB–1MB    ~12 cycles ~500 GB/s    6T SRAM               |
|   L3       8–64 MB      ~40 cycles ~200 GB/s    6T SRAM               |
|   DRAM     8–256 GB     ~70ns      ~50–100 GB/s DRAM cells            |
|            (100 cycles)                                               |
|   NVMe     256GB–8TB    ~100μs     ~5–12 GB/s   NAND flash            |
|            (~50K cycles)                                              |
|   HDD      1–20 TB      ~5–10ms    ~100–200 MB/s magnetic             |
|                                                                       |
|  DRAM latency numbers: DDR5-6400, typical desktop system              |
|  Apple M2: L2 per-cluster 12 MB; "System cache" 8–24 MB before DRAM   |
+-----------------------------------------------------------------------+
```

---

## SRAM: The Cache Cell

All caches use Static RAM (SRAM), which holds a bit stably as long as power is applied — no refresh needed.

```
  6-TRANSISTOR SRAM CELL:

  VDD
   |
  T1   T2        (Pull-up transistors)
   |     |
  Q ──── Q̄       (Cross-coupled inverters — stable bistable state)
   |     |
  T3   T4        (Pull-down transistors)
   |
  GND

  T5  T6 ─── BL, BL̄   (Access transistors — controlled by Word Line)

  Word Line (WL): selects which row to read/write
  Bit Line (BL) / Bit Line Bar (BL̄): carry data in/out

  READ: WL high → T5/T6 connect cell to BL/BL̄ → sense amplifier
  WRITE: Drive BL/BL̄ strongly → overpower the cell → flip state

  AREA: ~120 nm² per bit in modern process (vs ~4 nm² for DRAM)
  SRAM is 30× larger than DRAM per bit.
  This is why L3 caches max out at ~64 MB on chip — 64 MB SRAM
  = significant die area.
```

---

## Cache Organization

### Cache Line

```
  CACHE LINE (BLOCK): The fundamental unit of transfer.
  ALL caches transfer data in blocks, not individual bytes.

  x86: 64-byte cache lines (standard)
  ARM64: 64-byte cache lines (most implementations)

  CONSEQUENCE:
  If you read one int32 (4 bytes) from cold DRAM,
  the cache fetches 64 bytes (the whole line) anyway.
  Reading the next 15 ints in that line = free (cache hits).
  Reading scattered data = one cache miss per element.

  This is why struct layout matters:
  +---------------------+          +---------------------+
  | AoS (Array of       |          | SoA (Structure of   |
  | Structures):        |          | Arrays):            |
  | {x, y, z, w} × N   |          | {x×N, y×N, z×N, w×N}|
  |                     |          |                     |
  | If you only use x:  |          | If you only use x:  |
  | Load all 4 fields   |          | Load only x array   |
  | → 75% bandwidth     |          | → 100% efficient    |
  | wasted              |          |                     |
  +---------------------+          +---------------------+
```

### Set-Associative Cache

```
  THREE CACHE ORGANIZATIONS:

  DIRECT MAPPED (1-way associative):
  Each address maps to exactly ONE cache line slot.
  Address → cache index via (address >> 6) % num_lines

  +───+───+───+───+───+───+───+───+   Slot 0
  |tag|v|d| data (64 bytes)         |  (maps to addr 0, 64, 128...)
  +───+───+───+───+───+───+───+───+
  |tag|v|d| data (64 bytes)         |  Slot 1
  ...

  Problem: Two "hot" addresses that map to the same slot thrash each other.

  FULLY ASSOCIATIVE:
  Data can go in ANY slot. Full tag comparison.
  Best hit rate. Hardware cost: N comparators for N lines.
  Only feasible for small structures (TLBs, victim caches).

  N-WAY SET ASSOCIATIVE (standard):
  Cache is divided into sets, each set has N ways (slots).
  Address → set via index bits.
  Within the set, data can be in any of the N ways.

  Example: 32 KB L1, 8-way, 64-byte lines:
  32768 / 64 / 8 = 64 sets
  Address bits: [tag][index:6 bits][offset:6 bits]

  +────────+──────────────────────────────────────────────────+
  |  SET 0 |  Way 0  |  Way 1  | ... |  Way 7  |              |
  |  SET 1 |  Way 0  |  Way 1  | ... |  Way 7  |              |
  |  ...   |                                                  |
  |  SET 63|  Way 0  |  Way 1  | ... |  Way 7  |              |
  +────────+──────────────────────────────────────────────────+

  On access:
  1. Compute set index from address
  2. Compare tag against all 8 ways in parallel
  3. If match (hit): return data
  4. If no match (miss): fetch from next level, evict one way

  EVICTION POLICY:
  LRU: replace least recently used way (optimal for temporal locality)
  Pseudo-LRU: approximation of LRU (tree-based or PLRU bits)
  Random: simpler; surprisingly good in practice
  RRIP (Re-reference Interval Prediction): state-of-the-art
```

---

## DRAM: The Main Memory Cell

Dynamic RAM uses a capacitor and single transistor per bit — much denser than SRAM but requires constant refresh.

```
  1-TRANSISTOR DRAM CELL:

  Word Line (WL) ─┤ T (NMOS)├──── Bit Line (BL)
                         |
                         C (capacitor)
                         |
                        GND

  READ: WL high → T connects capacitor to BL → sense amplifier.
        READ IS DESTRUCTIVE — must rewrite after read.
  WRITE: WL high + drive BL strongly → charge/discharge capacitor.
  REFRESH: Capacitor leaks charge → must be read and rewritten
           every 64–128 ms. Typical: refresh 8192 rows every 64 ms.

  DRAM ARRAYS:
  Organized in banks, rows, columns.
  Access must ACTIVATE a row (copy into row buffer) before read.
  OPEN PAGE POLICY: row buffer stays open for subsequent accesses.
  Row hit: ~CAS latency (~14 ns)
  Row miss (different row): row activate + row read + CAS latency
  Bank conflict: ~50–100 ns total
```

### DRAM Timing

```
  DDR5-6400 (2023 typical):
  CAS Latency (CL):    32  = cycles to read after column activation
  RAS to CAS (tRCD):   32  = cycles for row activate to column access
  Row Precharge (tRP): 32  = cycles to close and precharge a row
  Active to Active (tRAS): 76  = total row activation time

  At 3200 MHz effective (DDR5-6400):
  CL32 = 10 ns CAS latency
  Total first-access: ~40-50 ns = ~100 CPU cycles at 3 GHz

  DDR vs LPDDR:
  DDR5 (desktop/server): higher bandwidth, higher power
  LPDDR5x (mobile, Apple Silicon): lower power, integrated package
  Apple M2: 100+ GB/s memory bandwidth (LPDDR5)
  vs typical PC: 50 GB/s (DDR5-6400 dual channel)
```

---

## Cache Performance Analysis

### Hit Rate and AMAT

```
  AVERAGE MEMORY ACCESS TIME (AMAT):
  AMAT = HitTime + MissRate × MissPenalty

  Multi-level:
  AMAT = HitL1 + MissRateL1 × (HitL2 + MissRateL2 × (HitL3 + MissRateL3 × DRAM))

  EXAMPLE:
  L1: 4 cycles, 95% hit rate
  L2: 12 cycles, 80% hit rate (conditional on L1 miss)
  L3: 40 cycles, 90% hit rate (conditional on L2 miss)
  DRAM: 200 cycles

  Global miss rate: 0.05 × 0.20 × 0.10 = 0.001 = 0.1%
  AMAT ≈ 4 + 0.05×(12 + 0.20×(40 + 0.10×200))
        ≈ 4 + 0.05×(12 + 0.20×60)
        ≈ 4 + 0.05×24 = 4 + 1.2 = 5.2 cycles effective

  A 0.1% DRAM miss rate only has ~1.2 cycle overhead because
  L2 and L3 absorb most misses. The 1% case (bad cache behavior)
  dramatically degrades performance.
```

### Prefetching

```
  HARDWARE PREFETCHER:
  Detects access patterns and prefetches data before it's needed.

  SEQUENTIAL PREFETCHER: If you accessed line N, prefetch N+1, N+2...
    Works for: array traversal, sequential scans
    Blind to: struct offsets, strides ≠ 1

  STRIDE PREFETCHER: Detect access stride, prefetch ahead.
    e.g., accessing every 4th cache line → prefetch next in stride
    Works for: for loops with fixed stride

  NON-TEMPORAL STORES (x86):
  MOVNT (Move Non-Temporal) instructions bypass the cache:
  MOVNTDQ [mem], xmm0   "write to memory without polluting cache"
  Use for: large sequential writes you won't re-read
  (video frame writes, memset on large buffers)
  Avoids evicting useful data from the cache.

  SOFTWARE PREFETCH:
  PREFETCHT0 [addr]     "prefetch into all cache levels"
  PREFETCHNTA [addr]    "prefetch minimally (don't pollute)"
  ARM: PRFM PLDL1KEEP, [x0]
  C intrinsic: __builtin_prefetch(addr, 0, 3)
  Distance: should be 100–200 cycles ahead (latency hiding)
```

---

## TLB: Translation Lookaside Buffer

```
  VIRTUAL ADDRESS → PHYSICAL ADDRESS requires page table walks.
  A 4-level page table walk = 4 memory accesses = 4 L3/DRAM hits.
  The TLB caches these translations.

  TLB STRUCTURE:
  iTLB: Instruction TLB (12 entries for 4K pages, 8 for 2M)
  dTLB: Data TLB (L1: 64 entries, L2: 1536 entries — Intel Golden Cove)

  TLB HIT: address translation = 0 additional cycles (parallel lookup)
  TLB MISS: hardware page table walker traverses 4 levels
    Each level: cache hit (4–40 cycles) or DRAM hit (100 cycles)
    Total TLB miss cost: ~50–300 cycles

  HUGE PAGES:
  Standard page: 4 KB → TLB entry covers 4 KB
  Huge page (Linux: transparent huge page): 2 MB → 512× coverage
  Gigantic page: 1 GB → 262,144× coverage

  Using huge pages for large working sets dramatically reduces TLB misses.
  Linux: /proc/meminfo shows AnonHugePages.
  madvise(addr, size, MADV_HUGEPAGE) hints huge pages.
  C#: windows uses large page support via VirtualAlloc + MEM_LARGE_PAGES.

  CONTEXT SWITCH TLB FLUSH:
  Process A and B have different virtual→physical mappings.
  On context switch, TLB must be flushed (or process tags added).
  PCID (Process-Context Identifiers, x86): tag each TLB entry with ASID.
  Avoids full TLB flush on context switch.
  INVLPG: invalidate a single TLB entry.
  ASID (ARM): Address Space Identifier — same concept.
```

---

## Non-Uniform Memory Access (NUMA)

```
  MULTI-SOCKET SERVERS:
  Modern servers have 2–8 CPU sockets.
  Each socket has its own local DRAM.
  A core on Socket 0 accesses Socket 1 DRAM via:
  QPI/UPI (Intel) or Infinity Fabric (AMD) inter-socket interconnect.

  Socket 0 DRAM access: ~70 ns (local)
  Socket 1 DRAM access: ~120–200 ns (remote, via UPI/IF)

  NUMA EFFECTS:
  Process migrated from core 0 to core 16 (different socket)
  but its memory stays on socket 0.
  Result: remote NUMA accesses = 2–3× latency penalty.

  NUMA-AWARE ALLOCATION:
  Linux: numactl, mbind(), set_mempolicy()
  C#/.NET: not directly exposed; use affinity + Runtime.GetCurrentProcessorId()
  Azure VM: most VMs are single socket; NUMA matters for bare-metal D-series

  AZURE CONTEXT: Azure HBv3 VMs (HPC) expose NUMA topology.
  Application code using large in-memory data (ML training,
  in-memory databases) benefits from NUMA awareness.
```

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| Why is the cache line 64 bytes? | Balances spatial locality benefit vs bandwidth wasted on partial use |
| What is the cost of an L3 miss? | ~100 CPU cycles to DRAM; 4× more if NUMA remote socket |
| What is a TLB miss? | Page table walk: 4 memory accesses → 50–300 cycles |
| When should you use huge pages? | Large working sets (>1 GB) to reduce TLB pressure |
| What is a non-temporal store for? | Large sequential writes that you won't re-read — avoid cache pollution |
| What is cache associativity? | 8-way: each cache set has 8 slots; higher associativity = fewer conflict misses |
| Why does AoS often lose to SoA? | AoS loads unused fields into cache lines; SoA packs accessed fields together |

---

## Common Confusion Points

**Cache line ≠ cache block ≠ cache entry**: These terms are often used interchangeably. All refer to the same unit: the 64-byte (on x86) chunk that is transferred between cache levels. "Cache block" is the older term; "cache line" is most common in hardware literature.

**L3 is "last level cache" (LLC) on most chips but not all**: Apple Silicon has a "System Cache" between L2 and DRAM that is on-chip but shared differently. The "LLC" concept is relative to the chip's cache hierarchy.

**DRAM refresh does not affect latency noticeably for individual accesses**: Refresh occurs row by row; individual accesses happen between refreshes. What does affect latency is row activation and the difference between row-hit and row-miss scenarios.

**Prefetching cannot fix pointer-chasing patterns**: Sequential prefetchers work well for arrays. Linked list traversal (pointer chasing) has each access dependent on the previous — no hardware prefetcher can predict the next address before the current one returns. Pointer-heavy data structures (linked lists, tree nodes) have inherently poor cache performance.

**NUMA in virtualization**: Cloud VMs hide NUMA topology. Unless you are on bare metal or an HPC VM, you are typically within one NUMA domain. But for latency-sensitive .NET services with large in-memory state, enabling NUMA awareness in the GC (System.GC.Server=true, LatencyMode) can matter.
