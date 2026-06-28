---
maxim_schema: maxim.frontmatter.v1
id: maxim:embedded-systems:overview
kind: guide
module: embedded-systems
section: embedded-systems
title: Embedded Systems - The Landscape
status: source-custody
source_custody: partial
current_path: embedded-systems/00-OVERVIEW.md
canonical_path: embedded-systems/00-OVERVIEW.md
backsource_ids: [proof-backfill:embedded-systems:00-overview, git-history:embedded-systems:00-overview]
concepts: [embedded systems, real-time, bare metal, microcontroller, firmware]
root_concepts: [embedded systems]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Embedded Systems — The Landscape

## The Big Picture

An embedded system is a computer that disappears into a product. There is no
user staring at a desktop; there is a thermostat, a motor controller, an
insulin pump, a brake ECU. The defining tension is not "how fast" but "how
predictable, how small, how power-frugal, and how directly does software touch
hardware." You already know operating systems, concurrency, and CPU
microarchitecture. This module is the layer where those abstractions get
stripped away: where you write to a register and a voltage changes 40 ns
later, where a missed deadline is a physical failure, where there may be no OS
at all and no heap you are allowed to touch.

```
+-----------------------------------------------------------------------+
|                     THE EMBEDDED STACK                                |
|                                                                       |
|  APPLICATION FIRMWARE                                                 |
|  control loops, protocol stacks, device logic (C, C++, Rust)          |
|           |                                                           |
|           v                                                           |
|  .-----------------------.    .-----------------------.               |
|  | RTOS  (optional)      | OR | SUPER-LOOP / BARE     |               |
|  | FreeRTOS, Zephyr,     |    | METAL                 |               |
|  | ThreadX, embOS        |    | while(1){ poll; act } |               |
|  | tasks, scheduler,     |    | + interrupts          |               |
|  | priorities, mutexes   |    | no scheduler          |               |
|  '-----------------------'    '-----------------------'               |
|           |                            |                              |
|           v                            v                              |
|  .-------------------------------------------------------.            |
|  | HAL / DRIVERS / CMSIS                                 |            |
|  | register maps, peripheral init, vector table          |            |
|  '-------------------------------------------------------'            |
|           |                                                           |
|           v                                                           |
|  .-------------------------------------------------------.            |
|  | SILICON: CPU core + on-chip peripherals + memory      |            |
|  | Cortex-M core | NVIC | timers | UART/SPI/I2C/CAN      |            |
|  | flash | SRAM  | ADC/DAC | DMA | clock tree | power    |            |
|  '-------------------------------------------------------'            |
|           |                                                           |
|           v                                                           |
|  PHYSICAL WORLD: sensors, actuators, motors, radios, the plant        |
+-----------------------------------------------------------------------+
```

**Read this bottom-up**: the physical world drives sensors, peripherals
digitize signals, firmware decides, actuators move the world. The CPU is a
small part of the picture — most of an MCU's die is peripherals.

---

## What Makes "Embedded" Different

You know general-purpose computing. Here is the delta, stated as contrasts so
nothing familiar gets re-taught.

| Dimension | Server / Desktop (you know this) | Embedded |
|-----------|----------------------------------|----------|
| Goal | Throughput, average latency | **Determinism**, worst-case latency |
| Memory | GBs, virtual memory, paging | KBs–MBs, often **no MMU**, physical addresses |
| Scheduler | Fair, throughput-optimal (CFS) | **Priority/deadline**, preemptive, no fairness |
| Failure | Restart the process | Physical consequence; must not fail |
| I/O | Through syscalls + drivers | **Direct register writes**, memory-mapped |
| Concurrency | Threads + OS primitives | **Interrupts** + (maybe) tasks |
| Power | Wall power | Battery / harvested; microamps matter |
| Update | apt/Windows Update | **OTA** to flash, must be atomic, recoverable |
| Time | "Eventually" is fine | A deadline is a **correctness** constraint |

### Old world → embedded world bridge

```
  You already know...              Embedded analogue...
  -------------------              --------------------
  Process                          Task (RTOS) or just "the program"
  Thread                           Task; or an ISR (no scheduler context)
  OS scheduler (CFS)               RTOS scheduler (fixed-priority preemptive)
  Page fault / MMU                 Usually ABSENT; MPU at most (no translation)
  malloc/free heap                 Static allocation; heap is suspect
  System call                      Direct MMIO register write (no kernel trap)
  Driver in kernel                 Driver IS your code, runs in one address space
  SIGINT signal handler            Interrupt service routine (hardware-vectored)
  Database durability              Wear-leveled flash + journaled config
```

The single biggest mental shift: **there is usually one address space and no
privilege boundary you didn't build yourself.** Your application code, your
"drivers," and your interrupt handlers all run with full access to every
register. The OS is not protecting you. That is freedom and a loaded gun.

---

## MCU vs MPU vs SoC — The Hardware Tiers

The first taxonomy question is what kind of chip you are programming. These
terms are abused constantly; here is the precise distinction.

```
+-----------------------------------------------------------------------+
|                                                                       |
|  MCU (Microcontroller Unit)                                           |
|  .-------------------------------------------.                        |
|  |  CPU core (Cortex-M)  +  FLASH  +  SRAM    |   ALL ON ONE DIE      |
|  |  +  timers + UART/SPI/I2C + ADC + GPIO     |   Runs from internal  |
|  |  No external memory needed. Boots alone.   |   flash. No MMU.      |
|  '-------------------------------------------'                        |
|                                                                       |
|  MPU (Microprocessor Unit)                                            |
|  .-------------------------------------------.                        |
|  |  CPU core (Cortex-A) + MMU + caches        |   Needs EXTERNAL      |
|  |  NO on-chip program memory worth running   |   DRAM + flash.       |
|  |  an OS from. Pairs with DDR + NAND/eMMC.    |   Runs Linux.        |
|  '-------------------------------------------'                        |
|                                                                       |
|  SoC (System on Chip)                                                 |
|  .-------------------------------------------.                        |
|  |  One or more MPU cores + GPU + radios +    |   A whole computer.   |
|  |  NPU + memory controllers + MCU "islands"  |   Phone/Pi class.     |
|  |  Often INCLUDES MCUs as subsystems.        |                       |
|  '-------------------------------------------'                        |
|                                                                       |
+-----------------------------------------------------------------------+
```

| Term | Core family | Memory model | OS | Example | "MMU?" |
|------|-------------|--------------|----|---------|--------|
| **MCU** | Cortex-M, RISC-V, AVR | On-chip flash+SRAM, physical | Bare metal / RTOS | STM32, nRF52, RP2040, ESP32 | No (MPU optional) |
| **MPU** | Cortex-A, x86 | External DRAM, virtual | Linux / RTOS | i.MX, Cortex-A53 SoCs | Yes |
| **SoC** | Mixed | Both | Linux + RTOS islands | Raspberry Pi, phone chips, ESP32-S3 | Yes (on A-cores) |

**Confusing edge cases.** ARM names "MPU" the *Memory Protection Unit*
(register-region permissions, no translation) **and** the industry uses "MPU"
for *Microprocessor Unit*. Different things. The ESP32 is marketed as an MCU
but is really a small SoC (Wi-Fi/BT radios on die). The RP2040 is an MCU with
*no* internal flash — it boots from external QSPI flash via a ROM bootloader.
Taxonomy is a guide, not a law.

> See `computer-architecture/03-ARM-RISC-V.md` for the Cortex-A vs Cortex-M
> ISA split, and `os/00-OVERVIEW.md` for what "runs Linux" actually entails.
> This module stays on the MCU / bare-metal / RTOS side of the line.

---

## The Two Software Worlds: Bare Metal vs RTOS

Every embedded project lands in one of two execution models (Linux-class MPUs
are a third world covered by the `os/` module). The choice is architectural
and you make it early.

```
  BARE METAL (super-loop)              RTOS (multi-task)
  -----------------------              -----------------
  int main(void) {                     void task_sensor(void*) {
    init();                              for(;;){ read(); notify(); }
    for(;;){                           }
      poll_sensor();                   void task_control(void*) {
      run_control();                     for(;;){ wait(); actuate(); }
      service_comms();                 }
    }                                  // scheduler runs them by priority
  }                                    // + ISRs on top of everything

  + tiny, no overhead                  + clean concurrency, deadlines
  + fully predictable                  + preemption, blocking primitives
  - timing tangled in code             - scheduler + RAM overhead
  - hard to add deadlines              - priority bugs (inversion!)
  Good below ~3-4 timed activities     Good when many timed activities
```

A useful rule: if you can count the periodic activities on one hand and they
share a common rate structure, a timer-driven super-loop with a few interrupts
is simpler and more analyzable than an RTOS. Once you have many independent
periodic tasks with different rates and blocking I/O, an RTOS earns its
overhead. Files `02-BARE-METAL.md` and `04-RTOS.md` go deep on each.

---

## Why Determinism Beats Speed

This is the cultural shock for someone arriving from cloud/server thinking. In
embedded, a system that responds in a guaranteed 100 µs every time is superior
to one that responds in 10 µs on average but occasionally 5 ms. The motor
controller that updates at a jittery rate produces audible whine and mechanical
wear; the one that is metronome-steady is silent.

```
  SERVER MINDSET                  EMBEDDED MINDSET
  --------------                  ----------------
  optimize the AVERAGE            optimize the WORST CASE
  p99 latency                     ABSOLUTE max latency (WCET)
  "mostly fast"                   "never late"
  GC pause? acceptable            GC pause? often forbidden
  cache miss? amortized           cache miss? counted in the WCET budget
  add a retry                     a retry means the deadline is already blown
```

This is why embedded engineers distrust dynamic allocation (fragmentation =
nondeterministic latency), caches without analysis (variable hit time), and
anything labeled "usually fast." The entire module is, in a sense, a campaign
against variance. `07-REAL-TIME-CONSTRAINTS.md` formalizes this with WCET and
schedulability.

---

## Module Map — How These Guides Layer

```
                       00-OVERVIEW  (you are here)
                            |
        +-------------------+-------------------+
        v                                       v
  01-MICROCONTROLLERS                     07-REAL-TIME-CONSTRAINTS
  (the chip, memory map)                  (WCET, schedulability, jitter)
        |                                       ^
        v                                       |
  02-BARE-METAL  ----> 03-INTERRUPTS-AND-TIMERS-+
  (registers, GPIO)    (NVIC, ISR, latency)     |
        |                     |                 |
        |                     v                 |
        |               04-RTOS  ---------------+
        |               (tasks, scheduling, priority inversion)
        v                     |
  05-MEMORY-AND-DMA  <--------+
  (flash/RAM, DMA, cache)
        |
        v
  06-PERIPHERALS-AND-BUSES   08-POWER-MANAGEMENT   09-DEBUG-AND-TOOLCHAIN
  (UART/SPI/I2C/CAN/USB)     (sleep, clocks)        (JTAG/SWD, HAL, OTA)
```

Read 01→02→03 for the bare-metal spine. Add 04 for the RTOS world. 05–06 are
the resource and I/O layers. 07 is the theory that makes timing a contract.
08–09 are the production concerns (power and toolchain) that decide whether a
prototype ever ships.

---

## Cross-References to the Rest of the Library

| When you need... | Go to |
|------------------|-------|
| The CPU pipeline / ISA beneath the core | `computer-architecture/` |
| Virtual memory, full OS scheduling, Linux internals | `os/` |
| Motion control, sensors-as-robots, ROS, SLAM | `robotics/` |
| Transistors, op-amps, signal conditioning, PCB | `electronics/` |
| Battery chemistry, energy density, charging | `energy-storage/` |
| Control loops (PID, state-space) the firmware runs | `robotics/06-CONTROL.md`, `control-theory/` |

Embedded sits at the seam of all of these. The MCU runs a control law
(control theory), reads conditioned analog signals (electronics), sips from a
battery (energy storage), and may be the low-level layer of a robot
(robotics). This module owns the *digital firmware/peripheral* layer and
hands off at each boundary.

---

## Common Confusion Points

### "Is an embedded system just a small Linux box?"

No — that conflates two tiers. A Raspberry Pi running Linux is an *embedded
Linux* (MPU/SoC) system, and it lives mostly in the `os/` module. The classic
embedded system in this module is an MCU: no MMU, no Linux, kilobytes of RAM,
firmware that owns the whole chip. Both are "embedded" colloquially; the
engineering is very different.

### "MCU vs microprocessor — aren't they the same chip, just sizes?"

No. The defining line is **integration and memory model**, not size. An MCU
has its program memory and peripherals on-die and runs from internal flash
with no external memory required. An MPU needs external DRAM and storage and
typically has an MMU. You can have a physically large MCU and a tiny MPU.

### "Why not just use an RTOS everywhere — concurrency is nicer?"

Because the RTOS adds RAM cost, scheduler latency, and a whole class of bugs
(priority inversion, deadlock, stack overflow per task) for benefit you may
not need. For a system with two periodic activities, a super-loop plus one
timer interrupt is smaller, faster, and *easier to prove correct*. Reach for
the RTOS when concurrency complexity exceeds the cost it imposes.

### "Real-time means fast, right?"

No. Real-time means **on time** — bounded, predictable latency. A real-time
system can be slow; it just must never miss its deadline. A 1 Hz control loop
that must fire within 1 ms of its tick is real-time. A web service averaging
2 ms with rare 500 ms spikes is fast-but-not-real-time. `07` makes this
rigorous.

---

## Decision Cheat Sheet

| I need to... | Reach for |
|---|---|
| Pick a chip class for a battery sensor node | **MCU** (Cortex-M0+/M4), bare metal or tiny RTOS |
| Run Linux, a display, a network stack | **MPU/SoC** (Cortex-A) — see `os/` |
| Add Wi-Fi/BLE to a small product | MCU-with-radio SoC (ESP32, nRF52/53) |
| Guarantee a control loop never misses | RTOS with rate-monotonic priorities + WCET analysis |
| Keep it dead-simple and provable | Super-loop + timer interrupt, no RTOS |
| Touch hardware directly, no OS overhead | Bare metal (`02`) — MMIO registers |
| Get the lowest possible standby power | MCU with deep sleep + RTC wake (`08`) |
| Move bytes without burning CPU | DMA (`05`) |
| Decide hard vs soft real-time | `07-REAL-TIME-CONSTRAINTS.md` |
