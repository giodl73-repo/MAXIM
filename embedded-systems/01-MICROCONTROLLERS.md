---
maxim_schema: maxim.frontmatter.v1
id: maxim:embedded-systems:microcontrollers
kind: guide
module: embedded-systems
section: embedded-systems
title: Microcontrollers - MCU, MPU, SoC and the ARM Cortex-M
status: source-custody
source_custody: partial
current_path: embedded-systems/01-MICROCONTROLLERS.md
canonical_path: embedded-systems/01-MICROCONTROLLERS.md
backsource_ids: [proof-backfill:embedded-systems:01-microcontrollers, git-history:embedded-systems:01-microcontrollers]
concepts: [microcontroller, cortex-m, memory map, mcu, mpu, soc]
root_concepts: [microcontroller]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# Microcontrollers — MCU, MPU, SoC and the ARM Cortex-M

## The Big Picture

A microcontroller is a complete computer on one die: CPU, program memory
(flash), working memory (SRAM), and a pile of peripherals, wired by internal
buses. Unlike the server CPU you know — which is a core surrounded by *external*
DRAM and a chipset — the MCU's defining feature is that it boots and runs
entirely from on-chip resources. The map below is the territory you program.

```
+-----------------------------------------------------------------------+
|                      A TYPICAL Cortex-M MCU                           |
|                                                                       |
|  .----------------.        .-----------------------------------.      |
|  |  CPU CORE      |        |  NVIC (interrupt controller)      |      |
|  |  Cortex-M4F    |<------>|  prioritizes + vectors IRQs       |      |
|  |  + FPU         |        '-----------------------------------'      |
|  |  + SysTick     |                  ^                                |
|  '-------'--------'                  | IRQ lines                      |
|          |  AHB bus                  |                                |
|  .-------.-------------------------------------------------.          |
|  |                  BUS MATRIX (AHB/APB)                   |          |
|  '--'--------'--------'--------'--------'--------'---------'          |
|     |        |        |        |        |        |         |          |
|     v        v        v        v        v        v         v          |
|  .-----. .------. .------. .------. .------. .-----. .---------.      |
|  |FLASH| | SRAM | | GPIO | | UART | | SPI  | | ADC | |  DMA    |      |
|  |512KB| |128KB | |ports | | I2C  | | CAN  | | DAC | |engine   |      |
|  '-----' '------' '------' '------' '------' '-----' '---------'      |
|                                                                       |
|  +-----------------------------------------------------------+        |
|  | CLOCK TREE (PLL, prescalers) | POWER (regulators, modes)  |        |
|  +-----------------------------------------------------------+        |
+-----------------------------------------------------------------------+
```

**Read this as a small city.** The core is downtown; the bus matrix is the
road network; flash and SRAM are the warehouses; peripherals are the factories
on the edge of town. The NVIC is the dispatch center that interrupts the core
when a factory needs attention. Most of the die area is *not* the core.

---

## Restating MCU vs MPU vs SoC Precisely

The overview introduced the tiers; here we make the distinction operational —
what changes for *you* as the programmer.

| Property | MCU | MPU | SoC |
|----------|-----|-----|-----|
| Program memory | On-chip flash | External (NOR/NAND/eMMC) | External |
| Working memory | On-chip SRAM (KBs) | External DRAM (GBs) | External DRAM |
| Address translation | None (physical) | MMU (virtual) | MMU on A-cores |
| Boots | From reset vector in flash | Multi-stage bootloader → kernel | Boot ROM → SPL → U-Boot → kernel |
| Typical core | Cortex-M, RISC-V, AVR | Cortex-A, x86 | Mixed A + M islands |
| Runs an OS? | Bare metal or RTOS | Linux / RTOS | Linux + RTOS islands |
| Power floor | µA in deep sleep | mW class minimum | mW–W |
| You write | The whole firmware image | App on top of an OS | Both, per subsystem |

The programmer-visible consequence: **on an MCU you own physical address
0x00000000 upward.** There is no `mmap`, no demand paging, no copy-on-write.
A pointer is a physical address. This is simultaneously the most liberating and
most dangerous fact about MCU programming.

### Old world → MCU bridge

```
  General-purpose CPU you know        MCU
  ---------------------------         ---
  RAM is the program's world          FLASH holds code, SRAM holds data
  Virtual address space               Physical memory map (fixed addresses)
  "Where is my code?" = wherever      Code executes IN-PLACE from flash (XIP)
  Loader copies exe into RAM          .data copied flash->SRAM at startup
  Stack grows in mapped pages         Stack is a fixed SRAM region; can overflow
  Peripherals via /dev + driver       Peripherals are MEMORY ADDRESSES you write
```

---

## The ARM Cortex-M Family

ARM dominates 32-bit MCUs. The Cortex-M line is the embedded profile (the "M"
profile of the ARM architecture), distinct from the Cortex-A application
profile you'd find in a phone. Knowing the rungs of this ladder lets you read
any datasheet.

```
                 CORTEX-M LADDER (low -> high capability)
  +--------------------------------------------------------------+
  | M0 / M0+ | ARMv6-M | smallest, ~0.9 DMIPS/MHz | sensor nodes |
  |          | no/limited divide, 2-3 stage pipe | nRF51, RP2040 |
  +--------------------------------------------------------------+
  | M3       | ARMv7-M | full Thumb-2, hw divide   | workhorse   |
  |          | 3-stage pipe, bit-banding          | STM32F1      |
  +--------------------------------------------------------------+
  | M4 / M4F | ARMv7-M + DSP (+ FPU on M4F)        | motor/audio |
  |          | SIMD-ish DSP instrs, single FPU    | STM32F4      |
  +--------------------------------------------------------------+
  | M7       | ARMv7-M | superscalar, caches, dual | high-perf   |
  |          | -issue, branch predict, I/D cache  | STM32H7      |
  +--------------------------------------------------------------+
  | M23/M33  | ARMv8-M | TrustZone-M security      | secure IoT  |
  |          | M33 adds DSP/FPU                 | nRF53, STM32L5 |
  +--------------------------------------------------------------+
  | M55/M85  | ARMv8.1-M | Helium (MVE) vector ML  | edge AI     |
  +--------------------------------------------------------------+
```

| Core | Architecture | FPU | DSP | Cache | Notable feature |
|------|--------------|-----|-----|-------|-----------------|
| M0/M0+ | ARMv6-M | No | No | No | Tiny, cheap, low power |
| M3 | ARMv7-M | No | No | No | Bit-banding, hardware divide |
| M4 | ARMv7-M | Optional (M4F) | Yes | No | DSP for audio/control |
| M7 | ARMv7-M | Double | Yes | I+D cache | Superscalar, fastest classic M |
| M23 | ARMv8-M base | No | No | No | TrustZone-M, low power |
| M33 | ARMv8-M main | Optional | Optional | No | TrustZone-M + DSP/FPU |
| M55/M85 | ARMv8.1-M | Yes | Helium MVE | Optional | Vector ML inference |

**Key architectural facts that matter in practice.** Cortex-M executes the
**Thumb-2** instruction set (mixed 16/32-bit, no classic ARM mode — M cores
have no 32-bit ARM state at all). It uses a **memory-mapped** register model:
even the NVIC and SysTick are memory addresses. Exceptions push state
automatically (hardware stacking of R0–R3, R12, LR, PC, xPSR), which is why
ISRs can be plain C functions — covered in `03-INTERRUPTS-AND-TIMERS.md`.

> The deep ISA mechanics (Thumb-2 encoding, pipeline, ARMv7-M vs ARMv8-M) live
> in `computer-architecture/03-ARM-RISC-V.md`. Here we care about the
> *programmer's model* of the chip, not the silicon.

---

## The Memory Map — The MCU's Address Space

This is the single most important diagram for an MCU programmer. The Cortex-M
architecture *fixes* a 4 GB address layout (even though you have KBs of real
memory) so that code, data, peripherals, and the core's own control registers
each live at architecturally defined regions.

```
  0xFFFFFFFF .-----------------------------.
             |  Vendor / system            |
  0xE0000000 '-----------------------------' <- PRIVATE PERIPHERAL BUS
             |  Cortex-M internals:        |    (NVIC, SysTick, SCB,
             |  NVIC, SysTick, SCB, debug  |     debug, MPU registers)
  0xE0100000 |  -- same on every M core -- |
             '-----------------------------'
             |                             |
  0xA0000000 |  External device            |
             '-----------------------------'
  0x60000000 |  External RAM               |
             '-----------------------------'
  0x40000000 .-----------------------------. <- PERIPHERALS
             |  APB/AHB peripheral regs:   |    GPIO, UART, SPI, I2C,
             |  GPIOA @0x40020000 ...      |    timers, ADC, DMA, RCC
             |  every peripheral is HERE   |    -- vendor specific --
             '-----------------------------'
  0x20000000 .-----------------------------. <- SRAM (your data)
             |  .data .bss heap stack      |    e.g. 128 KB here
             |  stack grows DOWN from top  |
             '-----------------------------'
  0x00000000 .-----------------------------. <- CODE / FLASH
             |  vector table @ 0x00000000  |    [0]=initial SP
             |  then your code (.text)     |    [1]=reset handler
             |  .rodata, const data        |    XIP: runs in place
  0x08000000 |  (often aliased here too)   |
             '-----------------------------'
```

| Region | Base (ARM-defined) | Holds | Notes |
|--------|--------------------|-------|-------|
| Code | 0x00000000 | Vector table, .text, .rodata | Often aliased to flash @0x08000000 |
| SRAM | 0x20000000 | .data, .bss, heap, stack | Bit-band region on M3/M4 |
| Peripheral | 0x40000000 | All peripheral registers | Vendor-specific layout |
| External RAM | 0x60000000 | Off-chip SDRAM/SRAM | Via FSMC/FMC if present |
| External device | 0xA0000000 | QSPI flash, memory-mapped devices | |
| Private peripheral | 0xE0000000 | NVIC, SysTick, SCB, MPU, debug | **Identical across all M cores** |

The brilliance of fixing 0xE0000000 across every Cortex-M is portability of
system code: the NVIC enable register is at the *same address* on an M0 from
one vendor and an M7 from another. CMSIS exploits this.

### Bit-banding (M3/M4 only)

A neat Cortex-M3/M4 trick: a 1 MB region of SRAM and of peripheral space is
"aliased" to a 32 MB region where each word maps to one bit of the base
region. Writing 1 to a bit-band alias address sets exactly one bit *atomically*
— a single store, no read-modify-write, no interrupt race. Useful for setting
one GPIO bit without a critical section. Absent on M0/M0+ and M7 (M7 uses
exclusive load/store instead).

---

## What Lives On the Chip — Peripherals at a Glance

```
+-----------------------------------------------------------------------+
|  ON-CHIP PERIPHERAL CATALOG (typical mid-range MCU)                   |
|                                                                       |
|  TIMING            COMMS            ANALOG          SYSTEM            |
|  ------            -----            ------          ------            |
|  SysTick (RTOS)    UART x4          ADC (12-bit)    RCC (clocks)      |
|  General timers    SPI x3           DAC (12-bit)    PWR (power)       |
|  Advanced timer    I2C x3           comparators     WDG (watchdog)    |
|  (PWM, encoder)    CAN x2           temp sensor     RTC (calendar)    |
|  Watchdog timers   USB FS/HS        Vref            CRC unit          |
|                    + DMA channels                  Flash controller   |
+-----------------------------------------------------------------------+
```

Each of these is a block of memory-mapped registers in the 0x40000000 region.
Programming a peripheral means writing the right bit patterns to the right
register at the right address — the subject of `02-BARE-METAL.md`. The buses
themselves (UART/SPI/I2C/CAN) and the analog blocks (ADC/DAC) get full
treatment in `06-PERIPHERALS-AND-BUSES.md`. DMA — the engine that moves data
between peripherals and SRAM without the core — is in `05-MEMORY-AND-DMA.md`.

---

## Choosing an MCU — The Real Selection Axes

```
                      MCU SELECTION TREE
                            |
        .-------------------.-------------------.
        |                                       |
   Need radio?                            Need an MMU/Linux?
    yes |  no                               yes -> that's an MPU/SoC,
        v   v                                      leave this module
  .---------.  .-----------------.           no  -> stay MCU
  | nRF52/53|  | core class?     |
  | ESP32   |  '--------.--------'
  | (BLE/   |           |
  |  Wi-Fi) |   .-------.--------.--------.
  '---------'   v       v        v        v
              M0+     M3/M4    M4F/M7   M33/M55
            (cheap)  (general)(DSP/    (secure/
                              float)    edge AI)
```

The axes that actually decide a part number:

| Axis | Question | Drives |
|------|----------|--------|
| Flash size | Code + constants fit? | Part variant |
| SRAM size | Buffers + stack(s) + heap fit? | Part variant |
| Core/clock | Compute headroom, FPU/DSP needed? | M-class |
| Peripherals | Right count of UART/SPI/I2C/CAN/ADC? | Vendor + part |
| Power | Sleep current budget (`08`)? | Family (e.g. STM32L) |
| Radio | Wi-Fi/BLE/Thread on-die? | nRF, ESP32, etc. |
| Security | Secure boot, TrustZone, crypto? | M23/M33, secure elements |
| Ecosystem | HAL, RTOS ports, debugger support | Vendor maturity |

Rule of thumb on memory: size your SRAM for **peak** simultaneous buffer use
plus the *sum* of every task's worst-case stack plus margin, then pick the next
size up. Running out of SRAM mid-project is the classic MCU regret — flash you
can sometimes trim, but a buffer that must exist must fit.

---

## Common Confusion Points

### "Where does my code actually run from — RAM or flash?"

By default, **execute-in-place (XIP) from flash**. The core fetches
instructions directly out of flash over the bus. Only `.data` (initialized
mutable globals) and your stack/heap live in SRAM. Some performance-critical
routines (and ISRs, to cut latency) are copied to SRAM at startup and run from
there — that's an explicit linker-script decision (`02`). This differs sharply
from a desktop where the loader copies the whole executable into RAM.

### "The chip has 128 KB of RAM but a 4 GB address space?"

The 4 GB is the *architectural* address space the Cortex-M defines — most of it
is unmapped or reserved. Touch an unmapped address and you take a BusFault.
Your actual physical SRAM is a small window (e.g. 0x20000000–0x2001FFFF for
128 KB). The huge map exists so that code, data, peripherals, and core
registers each get a fixed, non-overlapping home.

### "Is the flash address 0x00000000 or 0x08000000?"

Often both — vendors *alias* flash into the Code region. On STM32, flash is
physically at 0x08000000 but the boot configuration can map 0x00000000 to
flash so the vector table lives at address 0. The core fetches the initial
stack pointer from 0x00000000[0] and the reset vector from 0x00000000[4] at
power-on, regardless of where flash physically sits.

### "M4 vs M4F — why does it matter for my control loop?"

The **F** is a hardware single-precision FPU. Without it, every `float`
multiply in your PID loop becomes a software emulation routine — tens of cycles
instead of one. For DSP/control workloads that's the difference between hitting
your control rate and not. If you do float math in the loop, get the F. Note
the M4 FPU is single-precision only; double-precision still goes to software.

---

## Decision Cheat Sheet

| I need to... | Reach for |
|---|---|
| Pick the smallest/cheapest 32-bit core | Cortex-M0+ |
| General-purpose workhorse MCU | Cortex-M3 / M4 |
| Float-heavy control or audio DSP | Cortex-M4F (FPU) |
| Highest classic-M performance + cache | Cortex-M7 |
| Hardware security / secure boot | Cortex-M23 / M33 (TrustZone-M) |
| On-device ML inference | Cortex-M55/M85 (Helium MVE) |
| Find a peripheral's registers | Memory map @ 0x40000000 region |
| Find NVIC / SysTick / MPU registers | 0xE0000000 (same on all M cores) |
| Set one GPIO bit atomically (M3/M4) | Bit-band alias write |
| Decide MCU vs MPU | MMU/Linux needed? → MPU/SoC, else MCU |
| Size SRAM | Peak buffers + sum of task stacks + margin |
