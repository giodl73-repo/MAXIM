---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "03-INTERRUPTS-AND-TIMERS.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:embedded-systems:interrupts-and-timers
kind: guide
module: embedded-systems
section: embedded-systems
title: Interrupts and Timers - NVIC, ISR Discipline, Latency, PWM
status: source-custody
source_custody: partial
current_path: embedded-systems/03-INTERRUPTS-AND-TIMERS.md
canonical_path: embedded-systems/03-INTERRUPTS-AND-TIMERS.md
backsource_ids: [proof-backfill:embedded-systems:03-interrupts-and-timers, git-history:embedded-systems:03-interrupts-and-timers]
concepts: [interrupts, nvic, isr, interrupt latency, timers, pwm]
root_concepts: [interrupts]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# Interrupts and Timers — NVIC, ISR Discipline, Latency, PWM

## The Big Picture

Interrupts are how hardware steals the CPU. The core is running your main loop;
a byte arrives on the UART, a timer expires, a pin changes — and the hardware
*forces* the core to drop everything, jump to a handler, and return. This is
the embedded concurrency primitive: not threads, but asynchronous hardware
events that preempt mainline code. Timers are the most important interrupt
source because they manufacture *time* — periodic ticks, deadlines, PWM edges.

```
+-----------------------------------------------------------------------+
|                  ANATOMY OF AN INTERRUPT                              |
|                                                                       |
|  main loop running...                                                 |
|       |                                                               |
|       |   <==== peripheral asserts IRQ line (e.g. timer overflow)     |
|       v                                                               |
|  .------------------------------------------------------------.       |
|  | NVIC: is this IRQ enabled? higher priority than current?   |       |
|  |   yes -> request the core take the exception               |       |
|  '------------------------------------------------------------'       |
|       |                                                               |
|       v                                                               |
|  .------------------------------------------------------------.       |
|  | CORE (hardware, automatic):                                |       |
|  |   push R0-R3,R12,LR,PC,xPSR onto current stack             |       |
|  |   load handler address from vector table                  |        |
|  |   start executing the ISR  (latency ~12 cycles)           |        |
|  '------------------------------------------------------------'       |
|       |                                                               |
|       v                                                               |
|  .------------------------------------------------------------.       |
|  | YOUR ISR: do the minimum, clear the interrupt flag         |       |
|  '------------------------------------------------------------'       |
|       |                                                               |
|       v                                                               |
|  | EXC_RETURN: hardware pops the stacked registers, resumes  |        |
|  | main loop EXACTLY where it left off                        |       |
+-----------------------------------------------------------------------+
```

**Read top-down: this is one event in time.** The key fact for a Cortex-M: the
register stacking and unstacking is **done by hardware**, which is why an ISR
is just a normal C function with no special prologue — no assembly shim
required.

---

## The NVIC — Nested Vectored Interrupt Controller

The NVIC is a core peripheral (at the fixed 0xE0000000 region, `01`) that sits
between every interrupt source and the CPU. Three words, three jobs:

```
  +-------------+----------------------------------------------------+
  | NESTED      | A higher-priority IRQ can preempt a running ISR.   |
  |             | ISRs stack like function calls -> "nested."        |
  +-------------+----------------------------------------------------+
  | VECTORED    | Each IRQ has its OWN handler address in the vector |
  |             | table. No software dispatch -- hardware jumps      |
  |             | straight to the right ISR. (Fast, deterministic.)  |
  +-------------+----------------------------------------------------+
  | CONTROLLER  | Enables/disables, prioritizes, latches pending     |
  |             | IRQs. One register interface for all interrupts.   |
  +-------------+----------------------------------------------------+
```

### Old world → NVIC bridge

```
  You know...                          NVIC equivalent...
  ----------                           -----------------
  OS interrupt dispatch table          The vector table (but in hardware)
  Signal handler (SIGINT)              ISR -- but preemptive + nestable
  Thread priority                      IRQ priority (lower number = higher!)
  Disabling preemption (lock)          __disable_irq() / BASEPRI mask
  PIC/APIC on x86                      NVIC (tighter, deterministic, on-core)
```

### Priority — counterintuitive numbering

On Cortex-M, **lower priority number = higher urgency.** Priority 0 preempts
priority 1. Each IRQ priority byte splits into *preemption priority* (group)
and *sub-priority*: preemption priority decides who can interrupt whom;
sub-priority only breaks ties among simultaneously-pending IRQs of equal
preemption level (it does *not* enable nesting).

```
  Priority field (e.g. 4 implemented bits):
  +----------------+----------------+
  | preemption     | sub-priority   |
  | (can preempt?) | (tie-break)    |
  +----------------+----------------+
  Split point set by NVIC_SetPriorityGrouping().

  Example:
    SysTick   prio 0   -- highest, the RTOS tick
    motor PWM prio 1   -- preempts comms
    UART RX   prio 2
    button    prio 3   -- lowest, can be preempted by all above
```

A common rule: give the tightest-deadline source the highest priority (lowest
number), and never let a long-running low-priority handler block a critical
high-priority one — which the NVIC's preemption guarantees, *if you assign
priorities correctly*.

---

## Interrupt Latency — The Number That Matters

Latency is the time from the hardware asserting the IRQ to the first useful
instruction of your ISR. For real-time work this is part of your WCET budget
(`07`). On Cortex-M it is famously low and *deterministic*.

```
  TIMELINE of interrupt latency (Cortex-M, no contention)
  ---------------------------------------------------------
  IRQ asserted
     | finish current instruction (worst case: a long one, e.g. LDM)
     | ~ up to ~a dozen cycles for multi-load/store
     v
  begin exception entry: stack 8 registers + fetch vector
     | ~12 cycles (overlapped with vector fetch on M3/M4)
     v
  first instruction of ISR executes
     |
     | (your ISR body)
     v
  exception return: unstack 8 registers
     | ~12 cycles
```

| Factor | Effect on latency | Notes |
|--------|-------------------|-------|
| HW stacking | ~12 cycles fixed | Deterministic on M-profile |
| Longest atomic instruction | Adds its remaining cycles | LDM/STM can be interrupted/restarted on some cores |
| Disabled interrupts (critical section) | Adds the full masked duration | **You** control this — keep critical sections short |
| Higher-priority ISR in flight | You wait for it | Priority design problem |
| Flash wait states / no cache | Adds fetch stalls | Run ISR from SRAM to cut this |
| Tail-chaining | *Removes* an unstack+stack | Back-to-back ISRs skip redundant stacking |

Two Cortex-M tricks worth knowing as a systems peer:

- **Tail-chaining**: if a second interrupt is pending when one ISR finishes,
  the core skips the pop-then-push and jumps straight into the next ISR —
  saving ~6 cycles of churn.
- **Late-arriving preemption**: if a higher-priority IRQ arrives *during* the
  stacking of a lower one, the core redirects to the higher handler without
  re-stacking.

The biggest latency you actually control is **how long you disable interrupts**.
Every critical section in mainline code is a window where even the
highest-priority ISR is blocked. Keep them measured in a few instructions.

---

## ISR Discipline — Rules That Are Not Optional

An ISR runs in a stolen context with a deadline on it: get in, do the
essential, get out. Violations cause missed deadlines, races, and
hard-to-find timing bugs.

```
+-----------------------------------------------------------------------+
|                       ISR COMMANDMENTS                                |
|                                                                       |
|  DO                              DO NOT                               |
|  --                              ------                               |
|  Keep it short (us, not ms)      Call blocking functions              |
|  Clear the interrupt flag        Busy-wait / poll / delay()           |
|  Read/stash data, set a flag     malloc / free (heap, nondeterm.)     |
|  Use ISR-safe RTOS API          Call normal RTOS API (use ...FromISR) |
|  Defer real work to mainline     printf (slow, may block/reenter)     |
|  Mark shared vars volatile       Long loops over data                 |
|  Re-enter? design for it         Assume single-entry without nesting  |
+-----------------------------------------------------------------------+
```

The deferral pattern is the heart of good interrupt design: the ISR captures
the event and hands work to a lower-priority context.

```
  TOP HALF (ISR)            BOTTOM HALF (mainline / task)
  --------------            -----------------------------
  byte = UART->DR;          while(buffer_has_data){
  ringbuf_push(byte);   ->     parse_message();
  clear RXNE flag;             dispatch();
  // <2 us, returns          }
```

This is the same top-half/bottom-half split you know from Linux driver
design (the ISR vs the softirq/tasklet/workqueue). In an RTOS, the "bottom
half" is often a task woken by a semaphore the ISR gives (`04`); on bare metal
it's the super-loop draining a ring buffer the ISR filled.

### Clearing the flag — the silent infinite loop

Most peripheral interrupts latch a flag that *you must clear* in the ISR
(write-1-to-clear, or a read of the data register, depending on the
peripheral). Forget it, and the moment the ISR returns the still-asserted flag
re-triggers it instantly — an infinite interrupt storm that starves mainline
entirely. Always clear the source before returning.

---

## Timers — Manufacturing Time

A hardware timer is a counter clocked from the system clock (via a prescaler).
It is the most-used peripheral because almost everything in embedded is
periodic or deadline-bound.

```
+-----------------------------------------------------------------------+
|                       HOW A TIMER COUNTS                              |
|                                                                       |
|  system clock (e.g. 84 MHz)                                           |
|        |                                                              |
|        v                                                              |
|  .-----------.   divides clock    .------------.                      |
|  | PRESCALER |------------------->| COUNTER    | counts 0..ARR        |
|  | (PSC)     |   tick = clk/(PSC+1)| (CNT)     | then overflows       |
|  '-----------'                    '-----'------'                      |
|                                         |                             |
|                            reaches ARR  v                             |
|                            .------------------------.                 |
|                            | UPDATE EVENT -> IRQ    |                 |
|                            | (and/or reload to 0)   |                 |
|                            '------------------------'                 |
|                                                                       |
|  period = (PSC+1) * (ARR+1) / f_clk                                   |
+-----------------------------------------------------------------------+
```

**Worked example.** System clock 84 MHz, want a 1 kHz tick (1 ms period).
Choose PSC = 83 → timer tick = 84 MHz / 84 = 1 MHz (1 µs per tick). Set
ARR = 999 → overflow every 1000 ticks = 1000 µs = 1 ms. Each overflow fires
the update interrupt: your millisecond tick. The two-stage divide (prescaler
then auto-reload) gives you a wide range of periods from one clock.

| Timer mode | What it does | Used for |
|------------|--------------|----------|
| Periodic / update | IRQ every N ticks | RTOS tick, control-loop rate |
| Output compare | Toggle/pulse a pin at a count | Waveform generation |
| PWM | Duty-cycle a pin | Motor/LED/power control |
| Input capture | Latch CNT on a pin edge | Measure frequency/pulse width |
| Encoder | Count quadrature edges | Read motor shaft position |
| One-shot | Fire once, then stop | Timeouts, debounce |

### SysTick — the system's heartbeat

SysTick is a dedicated 24-bit down-counter built into every Cortex-M core (at
0xE0000000, so portable). It exists specifically to be the OS/RTOS tick — a
periodic interrupt that drives the scheduler (`04`) and `HAL_Delay`-style time
bases. Because it's part of the core, it's the one timer you can rely on across
every vendor's M-series part.

---

## PWM — Driving the Analog World Digitally

Pulse-Width Modulation encodes an analog level as the *duty cycle* of a fast
square wave. The MCU only drives a pin high or low, but switching fast and
varying the on-fraction yields an effective average voltage — the basis of
motor speed control, LED dimming, and switching power supplies.

```
  100% duty   ____________________  full power
              |                  |
   75% duty   ______      ______    3/4 average
              |    |______|    |__
   50% duty   ___    ___    ___     half average
              | |___| |___| |___
   25% duty   _    _    _           1/4 average
              |_|__|_|__|_|__

  duty = CCR / (ARR+1)        period fixed by ARR, level set by CCR
```

A timer in PWM mode compares its counter against a *compare register* (CCR):
pin is high while CNT < CCR, low otherwise. Change CCR and you change the duty
cycle — and thus the average power delivered. The period (PWM frequency) is set
by ARR as before; you pick it high enough that the load (motor inductance,
LED + eye, capacitor) integrates the pulses into a smooth average.

> The *electrical* side — H-bridges, gate drivers, the inductor that smooths
> PWM into current — lives in `electronics/` and the motor-control material in
> `robotics/07-ACTUATORS.md`. Here PWM is a timer configured to wiggle a pin.

---

## Common Confusion Points

### "My interrupt fires once then hangs the whole system"

You didn't clear the interrupt flag. The peripheral's pending bit is still set
on ISR return, so the NVIC immediately re-enters the ISR — forever, starving
mainline. Every ISR must clear its source (write-1-to-clear or read the
relevant register) before returning.

### "Lower priority number is higher priority — why?"

ARM's design: priority is an *order*, and 0 sorts first. It mirrors "priority 1
support ticket" conventions. Internally the NVIC compares numerically and the
smaller value wins the core. Get this backwards and your critical handler ends
up *lowest* urgency.

### "Can I call my RTOS's xSemaphoreGive from an ISR?"

Only the `...FromISR` variants. Normal RTOS API calls may block or assume a
task context and will corrupt state or fault if called from an ISR. FreeRTOS,
Zephyr, etc. provide explicit ISR-safe entry points that defer the actual
scheduling decision to ISR exit. Mixing them up is a classic, intermittent bug.

### "How is an ISR different from a thread/signal handler I know?"

A POSIX signal handler is delivered by the kernel asynchronously but runs in
thread context with software dispatch. A Cortex-M ISR is delivered by *hardware*
with hardware register stacking, runs at a hardware priority, can *preempt
other ISRs* (nesting), and returns via a special EXC_RETURN — no kernel
involved. It is closer to a hardware trap than to a signal.

---

## Decision Cheat Sheet

| I need to... | Reach for |
|---|---|
| Run something every N microseconds | Timer in periodic/update mode → IRQ |
| Drive the RTOS scheduler tick | SysTick (built into every M core) |
| Vary motor speed / LED brightness | Timer in PWM mode (set CCR) |
| Measure an input pulse width/frequency | Timer input-capture mode |
| Read a quadrature encoder | Timer encoder mode |
| React instantly to a pin change | EXTI (external) interrupt + GPIO |
| Make a critical handler never wait | Highest priority = lowest number |
| Keep ISR latency low | Short ISRs, short critical sections, ISR in SRAM |
| Do real work triggered by an interrupt | Defer: ISR sets flag/gives sem, task acts |
| Call RTOS API from an ISR | Use the `...FromISR` variant only |
| Stop an interrupt storm | Clear the peripheral's flag in the ISR |
