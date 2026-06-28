---
maxim_schema: maxim.frontmatter.v1
id: maxim:embedded-systems:memory-and-dma
kind: guide
module: embedded-systems
section: embedded-systems
title: Memory and DMA - Flash, RAM, Stack/Heap, DMA, Cache Coherence
status: source-custody
source_custody: partial
current_path: embedded-systems/05-MEMORY-AND-DMA.md
canonical_path: embedded-systems/05-MEMORY-AND-DMA.md
backsource_ids: [proof-backfill:embedded-systems:05-memory-and-dma, git-history:embedded-systems:05-memory-and-dma]
concepts: [memory, flash, sram, stack, heap, dma, cache coherence]
root_concepts: [memory]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# Memory and DMA — Flash, RAM, Stack/Heap, DMA, Cache Coherence

## The Big Picture

On an MCU, memory is scarce, heterogeneous, and *physically* visible. There is
no virtual memory papering over the differences — flash is slow and durable,
SRAM is fast and volatile, and you place every byte deliberately. DMA is the
escape hatch that moves data between peripherals and SRAM *without the CPU*,
buying back the cycles a polled copy would burn. The map below is the memory
budget you manage by hand.

```
+-----------------------------------------------------------------------+
|                   THE MCU MEMORY LANDSCAPE                            |
|                                                                       |
|  FLASH (non-volatile)            SRAM (volatile)                      |
|  .-------------------------.     .-------------------------.          |
|  | vector table            |     | .data (init globals)    | <-copied |
|  | .text  (code, XIP)      |     | .bss  (zeroed globals)  | from     |
|  | .rodata (constants)     | --> | HEAP   (grows up)       | flash    |
|  | .data INITIALIZERS      |     |   ...free...            | at boot  |
|  | config / NVM region     |     | STACK  (grows DOWN)     |          |
|  '-------------------------'     '-------------------------'          |
|   slow writes, byte reads,        fast R/W, lost on power-off         |
|   erase-by-sector, wear-limited   tiny (KBs)                          |
|                                                                       |
|         ^                                  ^                          |
|         |  CPU fetches code                |  CPU + DMA both access   |
|         |                                  |                          |
|  .------.----------------------------------.-------------------.      |
|  |              BUS MATRIX                   .---------.       |      |
|  |                                           |  DMA    |       |      |
|  |  CPU <-> bus <-> SRAM/flash/peripherals   | engine  |-------+      |
|  |                                           '---------' moves data   |
|  '-------------------------------------------------------------'      |
+-----------------------------------------------------------------------+
```

**Read it as a budget.** Flash holds the program and constants; SRAM holds the
mutable world. DMA shares the bus with the CPU to shuttle bytes between
peripherals and SRAM autonomously. Every region has a fixed size you cannot
exceed — overrun is not a page fault, it's corruption.

---

## Flash vs RAM — Two Very Different Memories

| Property | Flash (NOR, on-chip) | SRAM |
|----------|----------------------|------|
| Volatility | Non-volatile (keeps state off-power) | Volatile (lost at power-off) |
| Holds | Code, constants, config | Variables, stack, heap, buffers |
| Read | Fast, random, byte-addressable | Fast, random |
| Write | **Slow, special sequence** | Fast, normal store |
| Erase | **Whole sector at a time**, then write | N/A (just overwrite) |
| Endurance | ~10k–100k erase cycles per sector | Effectively unlimited |
| Wait states | Yes at high clock (needs prefetch/cache) | Usually zero-wait |
| Size | Larger (KBs–MBs) | Smaller (KBs–hundreds of KB) |

Two facts that trip up newcomers from the desktop world:

- **You cannot just write to flash like RAM.** Flash bits erase to 1 and
  program to 0; you must *erase a whole sector* (set all bits to 1) before you
  can program new data into it. Writing parameters at runtime means a
  read-modify-erase-write dance, and it's slow (milliseconds). That's why
  config storage uses wear-leveling and journaling, not naive overwrites.
- **Flash wears out.** Each sector tolerates a finite number of erase cycles.
  A naive "save settings every second" loop will brick a sector in days.
  Emulated-EEPROM libraries rotate writes across a region to spread the wear.

```
  WRITING A PARAMETER TO FLASH AT RUNTIME
  1. unlock flash controller
  2. ERASE the target sector (all -> 0xFF)   <- slow, blocks, ms
  3. PROGRAM the new bytes (1 -> 0 only)
  4. lock flash controller
  -> during erase/program, code can't usually execute from that bank
     (read-while-write limits) -- a real-time hazard. Plan around it.
```

> The physics of floating-gate cells, NOR vs NAND, and 3D flash structure live
> in `computer-architecture/05-MEMORY-HIERARCHY.md` and the storage discussion
> there. Here we care about the *programming constraints*.

---

## Stack and Heap — The Constrained Pair

With KBs of SRAM and no MMU guard pages, stack and heap discipline is a
correctness issue, not a style preference. They typically grow toward each
other in one SRAM region.

```
  high addr  +-------------------+ <- _estack (top of SRAM)
             |  STACK            |
             |  grows DOWN  |    |
             |              v    |
             |                   |
             |   ...free RAM...  | <- collision = silent corruption
             |                   |
             |              ^    |
             |  grows UP    |    |
             |  HEAP             |
             +-------------------+ <- end of .bss
             |  .bss / .data     |
  low addr   +-------------------+ <- 0x20000000
```

```
  STACK OVERFLOW (no guard page!)
  +------------------------------------------------------------+
  | On a desktop, overflowing the stack hits an unmapped guard |
  | page -> clean SIGSEGV. On an MCU there is NO guard page.   |
  | The stack just keeps growing DOWN into .bss/.data/heap and |
  | SILENTLY corrupts whatever is there. The bug appears far   |
  | from its cause. This is the #1 hardest MCU bug class.      |
  +------------------------------------------------------------+
```

**Why embedded engineers distrust the heap.** Dynamic allocation introduces
*nondeterminism* (allocation time varies) and *fragmentation* (free memory
exists but not contiguously, so a malloc fails despite "enough" RAM). Both are
poison to a real-time system. The common doctrine: **static allocation** —
fixed-size buffers and pools decided at compile time, so memory use is provable
and bounded. Many safety standards (MISRA-C, automotive, aerospace) ban or
heavily restrict `malloc` after init for exactly this reason.

| Allocation strategy | Determinism | Fragmentation | When |
|---------------------|-------------|---------------|------|
| Static / global | Total | None | Default for real-time |
| Stack (automatic) | Total (bounded depth) | None | Locals; watch depth |
| Memory pool (fixed-block) | High | None (fixed blocks) | When dynamic-ish behavior needed |
| General heap (malloc) | **Low** | **Yes** | Avoid in real-time paths |

Detecting overflow without a guard page: paint the stack with a known pattern
at init and check the high-water mark (RTOS does this per task, `04`), or use
the MPU to mark a region just past each stack as no-access so an overflow
faults cleanly instead of corrupting.

### The MPU (Memory Protection Unit) — not an MMU

A Cortex-M may include an MPU: a small unit that enforces **access permissions
on a handful of address regions** (read/write/execute, privileged/unprivileged)
— but it does **no address translation**. It cannot give each task a private
virtual space; it can mark a stack-guard region no-access, make flash
execute-only, or sandbox an untrusted task's reach. Think "region permissions,"
not "virtual memory." (Bridge: it's to an MMU as a firewall ACL is to NAT.)

---

## DMA — Moving Data Without the CPU

Direct Memory Access is a dedicated engine that copies between memory and
peripherals (or memory and memory) while the CPU does other work — or sleeps.
It is the difference between a UART that interrupts the CPU for every byte and
one that fills a buffer silently and interrupts once when done.

```
+-----------------------------------------------------------------------+
|             POLLED/IRQ COPY vs DMA TRANSFER                           |
|                                                                       |
|  WITHOUT DMA (CPU copies each byte)                                   |
|    ADC -> IRQ -> CPU reads reg -> CPU writes SRAM -> repeat x1000     |
|    CPU is busy the entire time. 1000 interrupts. Cycles burned.       |
|                                                                       |
|  WITH DMA                                                             |
|    ADC -> DMA -> SRAM buffer (engine moves each sample)               |
|    CPU sleeps or works. ONE interrupt when the buffer is full.        |
|    .-------.   trigger   .-------.   bus    .----------.              |
|    |  ADC  |------------>|  DMA  |--------->|  SRAM buf |             |
|    '-------'             '-------'          '----------'              |
|                              | done                                   |
|                              v                                        |
|                          IRQ (half / full)                            |
+-----------------------------------------------------------------------+
```

| DMA concept | Meaning |
|-------------|---------|
| Channel / stream | One independent transfer path (peripheral ↔ memory) |
| Source / destination | Addresses; either can auto-increment |
| Transfer count | How many items to move before stopping/wrapping |
| Trigger | What starts a transfer (peripheral event, software) |
| Circular mode | Wrap to start automatically — continuous streaming |
| Half/full IRQ | Fire at 50% and 100% — enables **double-buffering** |
| Burst | Move several items per bus arbitration grant |

**The double-buffer (ping-pong) pattern** is the workhorse: DMA fills the back
half of a buffer while the CPU processes the front half, then they swap at the
half/full interrupt. The CPU always works on stable data while new data streams
in — no copy, no race, continuous throughput. This is how you sustain a fast
ADC or audio stream on a small core.

```
  CIRCULAR DMA + HALF/FULL IRQ (ping-pong)
  buffer: [ ---- half A ---- | ---- half B ---- ]
  DMA fills A  ---> half IRQ ---> CPU processes A while DMA fills B
  DMA fills B  ---> full IRQ ---> CPU processes B while DMA fills A
  ...forever. CPU never copies, never blocks on I/O.
```

DMA does cost something: it and the CPU **share the bus matrix**, so heavy DMA
adds bus contention that can stall CPU memory accesses — a factor in your WCET
budget (`07`). Good MCUs have multiple bus masters and SRAM banks so CPU and
DMA touch different banks and don't fight.

### Old world → DMA bridge

```
  You know...                          DMA...
  ----------                           ----
  Async I/O / IOCP completion          DMA-done interrupt
  Zero-copy networking                 DMA straight into the app buffer
  Overlapped I/O                       CPU works while DMA transfers
  Bulk memcpy                          Memory-to-memory DMA (offload the copy)
```

---

## Cache Coherence on MCUs — The DMA Trap

Most small Cortex-M (M0–M4) have **no data cache**, so this section doesn't
apply to them — SRAM accesses are direct. But the Cortex-M7 (and A-class)
*does* have caches, and this creates a subtle, vicious bug class when DMA is
involved. You know cache coherence from multi-core CPUs (`computer-architecture/
06-CACHE-COHERENCE.md`); on an MCU the "other agent" isn't another core — it's
the DMA engine, and there is **no hardware coherence between the CPU cache and
DMA**.

```
+-----------------------------------------------------------------------+
|              THE CACHE/DMA COHERENCE HAZARD (Cortex-M7)               |
|                                                                       |
|  CASE 1: CPU writes a TX buffer, then starts DMA                      |
|    CPU writes land in the D-CACHE, not yet in SRAM (write-back).      |
|    DMA reads SRAM -> gets STALE old data. Garbage transmitted.        |
|    FIX: SCB_CleanDCache_by_Addr(buf) BEFORE starting DMA              |
|         (flush cache -> SRAM so DMA sees fresh data)                  |
|                                                                       |
|  CASE 2: DMA fills an RX buffer in SRAM, then CPU reads it            |
|    CPU reads from D-CACHE -> gets STALE pre-DMA data.                 |
|    FIX: SCB_InvalidateDCache_by_Addr(buf) AFTER DMA completes         |
|         (drop cached copy -> CPU re-reads fresh SRAM)                 |
+-----------------------------------------------------------------------+
```

Rules for cached MCUs with DMA:

- **Before DMA reads memory the CPU wrote**: *clean* (flush) the cache so SRAM
  has the real data.
- **After DMA writes memory the CPU will read**: *invalidate* the cache so the
  CPU re-fetches from SRAM.
- **Align and pad DMA buffers to the cache-line size** (32 bytes on M7) so a
  clean/invalidate doesn't accidentally touch a neighboring variable sharing
  the line.
- Or simplest: place DMA buffers in a **non-cacheable** MPU region and skip the
  maintenance entirely (at the cost of cache benefit on that region).

This bug is brutal because it works fine on M4 (no cache), then *intermittently*
fails when ported to M7. If you remember one thing from this file: **DMA and a
data cache are not automatically coherent on an MCU — you maintain it by hand.**

---

## Common Confusion Points

### "My code worked on the M4 but corrupts data on the M7"

Almost certainly the cache/DMA coherence trap. The M4 has no data cache so DMA
buffers were coherent by accident. The M7 caches, and now you must clean before
DMA-out and invalidate after DMA-in, with cache-line-aligned buffers. Or mark
the buffer region non-cacheable in the MPU.

### "malloc returned NULL but I have plenty of free RAM"

Fragmentation. The free memory exists but not as one contiguous block large
enough for the request. This is why real-time embedded avoids the general heap
and prefers static buffers or fixed-block pools, where this can't happen.

### "Where's my segfault? The stack overflowed but nothing crashed"

There's no MMU guard page on most MCUs. The stack silently grew into other
data and corrupted it; the symptom shows up later, elsewhere. Detect it with a
stack-painting high-water check, an RTOS stack monitor, or an MPU no-access
guard region just past the stack.

### "Can I write to flash like I write to a variable?"

No. Flash must be *erased a whole sector at a time* (to all-ones) before
programming, the write sequence is special and slow (milliseconds), code often
can't execute from a bank while it's being written, and sectors wear out after
~10k–100k erases. Runtime parameter storage needs a wear-leveling/journaling
layer, not naive stores.

---

## Decision Cheat Sheet

| I need to... | Reach for |
|---|---|
| Store code and constants | Flash (.text/.rodata, XIP) |
| Store variables, stacks, buffers | SRAM |
| Keep memory use deterministic | Static allocation / fixed-block pools |
| Avoid fragmentation and malloc nondeterminism | No general heap in real-time paths |
| Detect a stack overflow without an MMU | Stack painting + high-water, or MPU guard |
| Sandbox a task / mark a guard region | MPU (permissions, not translation) |
| Move a data stream without the CPU | DMA (circular + half/full IRQ ping-pong) |
| Offload a big memory copy | Memory-to-memory DMA |
| Use DMA on a cached core (M7) | Clean before TX, invalidate after RX, align buffers |
| Skip cache maintenance on DMA buffers | Non-cacheable MPU region |
| Save settings to flash at runtime | Wear-leveled / emulated-EEPROM library |
