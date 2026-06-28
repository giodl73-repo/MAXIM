---
maxim_schema: maxim.frontmatter.v1
id: maxim:embedded-systems:power-management
kind: guide
module: embedded-systems
section: embedded-systems
title: Power Management - Sleep Modes, Clock Gating, Energy Budgets, Battery
status: source-custody
source_custody: partial
current_path: embedded-systems/08-POWER-MANAGEMENT.md
canonical_path: embedded-systems/08-POWER-MANAGEMENT.md
backsource_ids: [proof-backfill:embedded-systems:08-power-management, git-history:embedded-systems:08-power-management]
concepts: [power management, sleep modes, clock gating, energy budget, battery, watchdog]
root_concepts: [power management]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# Power Management — Sleep Modes, Clock Gating, Energy Budgets, Battery

## The Big Picture

For a battery or energy-harvested device, power is the dominant design
constraint — above clock speed, above RAM. A coin-cell sensor must run for
years on 225 mAh, which means the MCU spends >99% of its life asleep and wakes
for milliseconds. The entire discipline is: do the work fast, then *stop the
clock and shut off everything you can*, and account for every microamp. Energy,
not speed, is the budget.

```
+-----------------------------------------------------------------------+
|                 THE DUTY-CYCLE OF A LOW-POWER NODE                    |
|                                                                       |
|  current                                                              |
|    |                                                                  |
|  ACTIVE  |####|                    |####|                |####|       |
|  (mA)    |    |                    |    |                |    |       |
|          |    |                    |    |                |    |       |
|  SLEEP   .    .--------------------.    .----------------.    .---    |
|  (uA)    measure  <----- sleep ---->  measure  <-sleep->              |
|          + send                                                       |
|                                                                       |
|  Average current ~= (I_active * t_active + I_sleep * t_sleep)         |
|                     / (t_active + t_sleep)                            |
|  -> dominated by how LITTLE time you spend awake, and how LOW         |
|     the sleep floor is.                                               |
+-----------------------------------------------------------------------+
```

**Read it as a duty cycle.** Battery life is set by the *average* current,
which is dominated by the sleep floor (because you sleep ~99.9% of the time) and
by how briefly you wake. Cutting active time and lowering the sleep floor are
the two levers — and the second usually matters more.

---

## Sleep Modes — The Power/Wake-Time Trade

MCUs offer a ladder of low-power modes. Deeper sleep = lower current but more
state lost and *longer* to wake. The art is matching the mode to how long you'll
be idle and what you must remember.

```
              SLEEP DEPTH LADDER (deeper = less power, slower wake)
  +-----------------------------------------------------------------+
  | RUN       | full speed         | mA       | everything on       |
  +-----------------------------------------------------------------+
  | SLEEP     | CPU clock stopped, | mA -> sub | wake on any IRQ     |
  | (WFI)     | peripherals run    | mA       | fast (~cycles)      |
  +-----------------------------------------------------------------+
  | STOP/     | clocks off, RAM    | uA       | wake on RTC/EXTI;   |
  | low-power | retained, regulator| (single  | wake ~us-ms; RAM    |
  |           | in low-power mode  |  digits) | + registers KEPT    |
  +-----------------------------------------------------------------+
  | STANDBY/  | most of chip off,  | sub-uA   | wake = ~RESET;      |
  | deep      | RAM mostly LOST,   | to nA    | only RTC/wake pin/  |
  |           | RTC + wake logic on|          | small backup RAM    |
  +-----------------------------------------------------------------+
  | SHUTDOWN/ | everything off but | nA       | wake = full reset,  |
  | off       | a wake pin         |          | all state lost      |
  +-----------------------------------------------------------------+
```

| Mode | CPU | Peripherals | RAM | Wake source | Wake time | Current |
|------|-----|-------------|-----|-------------|-----------|---------|
| Run | On | On | — | — | — | mA |
| Sleep (WFI) | Clock off | On | Kept | Any interrupt | ~cycles | sub-mA |
| Stop / LP | Off | Off (clocks gated) | **Retained** | RTC, EXTI pin | µs–ms | single µA |
| Standby / deep | Off | Off | **Mostly lost** | RTC, wake pin | ~reset | sub-µA |
| Shutdown | Off | Off | Lost | Wake pin | full reset | nA |

The key engineering decision is **what you can afford to forget**. Stop mode
keeps RAM and registers — you resume mid-program, fast. Standby loses RAM (a
tiny backup domain may survive) and wakes like a reset — you re-init, slow.
Choose the deepest mode whose wake-time and state-retention you can tolerate for
the expected idle length. A device idle for 10 seconds between samples should be
in Standby with an RTC alarm; one idle for 2 ms between bytes should be in Sleep.

### The wake-source discipline

Every sleep entry must pair with a guaranteed wake source, or the device sleeps
forever. The two staples:

- **RTC alarm** — a real-time clock running off a low-power 32.768 kHz crystal
  (a power domain that stays alive in deep sleep) wakes the chip after a set
  interval. This is the heartbeat of a periodic sensor node.
- **Wake pin / EXTI** — an external event (button, sensor interrupt line) pulls
  the chip out of sleep on demand. This is the event-driven path.

The canonical low-power loop: configure RTC alarm → enter Stop/Standby → wake →
take a measurement → transmit → repeat. The CPU is awake for milliseconds per
cycle.

---

## Clock Gating and Dynamic Frequency — Power Below Sleep

Even while running, you control power by controlling *clocks*. Dynamic power in
CMOS scales with frequency and the *square* of voltage — so slowing the clock
and dropping the voltage are both powerful levers.

```
  CMOS DYNAMIC POWER (the governing relation)
  +------------------------------------------------------------+
  |   P_dynamic  ~  C * V^2 * f                                |
  |                                                            |
  |   C = switched capacitance (the silicon, fixed)            |
  |   V = supply voltage   <- SQUARED: huge lever              |
  |   f = clock frequency  <- linear                           |
  |                                                            |
  | Halve f    -> ~half the dynamic power (but work is slower) |
  | Drop V 20% -> ~0.64x power -- voltage dominates            |
  | Plus P_static (leakage) which sleep modes attack instead.  |
  +------------------------------------------------------------+
```

| Lever | Mechanism | Effect |
|-------|-----------|--------|
| **Clock gating** | Turn off the clock to *unused* peripherals (RCC) | Removes their dynamic power; off = free |
| **Dynamic frequency** | Run the core only as fast as the work needs | Linear power saving |
| **Voltage scaling (DVFS)** | Lower core voltage at lower frequency | Quadratic saving (the big one) |
| **Peripheral power domains** | Power off whole blocks (radio, ADC) | Removes their static + dynamic draw |

**Clock gating is the everyday lever.** Recall from `02` that an unclocked
peripheral is dead — that same gate is your power tool: only enable the clock to
a peripheral while you're using it. A UART you use for a 1 ms burst every 10
seconds should have its clock gated the other 99.99% of the time. Many MCUs
gate automatically in sleep; in run mode you do it explicitly.

There's a subtlety the racing-to-sleep framing captures: it is usually better to
**run fast, finish, and sleep deep** ("race to idle") than to run slow to save
dynamic power, *because* the deep-sleep floor is so much lower than any active
mode. The dominant energy term is the sleep floor times the (long) sleep time,
so getting to sleep sooner wins. The exception is when active power scales
strongly with frequency and the sleep floor is relatively high — then a slower,
steadier pace can win. Measure both.

---

## Energy Budgeting — Making the Battery Math Real

Battery life is arithmetic once you know the duty cycle. The unit is the
milliamp-hour (mAh): a 225 mAh CR2032 coin cell delivers 225 mA for one hour, or
proportionally longer at lower current.

```
  WORKED ENERGY BUDGET (periodic sensor node)
  +------------------------------------------------------------+
  | Wake every 10 s, awake 5 ms (sense + BLE send), else sleep.|
  |                                                            |
  |   I_active = 8 mA    for t_active = 5 ms                   |
  |   I_sleep  = 2 uA    for t_sleep  = 9995 ms                |
  |                                                            |
  |   charge per cycle = 8mA*5ms + 0.002mA*9995ms              |
  |                    = 40 uA*s ... let's use mA*h directly:  |
  |   avg current = (8mA * 0.005s + 0.002mA * 9.995s) / 10s    |
  |              = (0.040 + 0.01999) mA*s / 10 s               |
  |              = 0.0600 mA*s / 10 s ... per-second avg:      |
  |   avg I ~= 8mA*(0.005/10) + 2uA*(9.995/10)                 |
  |         ~= 0.004 mA + 0.002 mA = 0.006 mA = 6 uA           |
  |                                                            |
  |   life = 225 mAh / 0.006 mA = 37,500 h ~= 4.3 YEARS        |
  |   (before derating for self-discharge, temperature, etc.)  |
  +------------------------------------------------------------+
```

The lesson the arithmetic teaches: with a 5 ms / 10 s duty cycle, the **sleep
floor (2 µA) and the active draw contribute about equally** here — so *both*
the sleep floor and the wake duration matter. Halve the sleep current and you'd
push past 5 years; double the awake time and you lose nearly a year. This is why
data sheets are read for the *sleep-mode microamps* as carefully as for the MHz.

| Budget factor | Typical concern |
|---------------|-----------------|
| Sleep floor (µA) | Dominates for low duty cycles — read it carefully |
| Active current (mA) | Radio TX is often the biggest spike |
| Wake/settle time | Crystal startup, regulator settle waste energy |
| Self-discharge | Battery loses charge even unused (% per year) |
| Temperature | Cold raises battery internal resistance, cuts usable mAh |
| Peak current | Radio TX bursts may exceed coin-cell rating → need a cap |

> Battery *chemistry* — Li-ion vs LiFePO4 vs coin cell, energy density,
> discharge curves, charging — is `energy-storage/`. Here we budget the load the
> firmware imposes. The two meet at the system level: firmware duty cycle ×
> battery capacity = lifetime.

---

## The Watchdog — Reliability, and a Power Footnote

A watchdog timer is a hardware counter that resets the MCU unless firmware
periodically "kicks" it. If the code hangs (deadlock, infinite loop, wild
pointer), the kick stops, the watchdog expires, and the chip resets into a known
state. It is the last line of defense for an unattended embedded system — there
is no operator to power-cycle a device on a Mars rover or in a wall sensor.

```
+-----------------------------------------------------------------------+
|                       THE WATCHDOG PATTERN                            |
|                                                                       |
|  watchdog counts down from T...                                       |
|     firmware healthy:  kick! kick! kick!  (reload before it hits 0)   |
|         |     |     |     |                                           |
|     ----.-----.-----.-----.----  counter never reaches 0              |
|                                                                       |
|  firmware HANGS:                                                      |
|     kick! kick! ......(hung, no more kicks)......                     |
|         |     |                          |                            |
|     ----.-----.--------------------------X--> RESET                   |
|                                          counter hit 0 -> reboot      |
+-----------------------------------------------------------------------+
```

| Watchdog rule | Why |
|---------------|-----|
| Kick from one well-understood place | Kicking everywhere defeats the purpose |
| Don't kick inside a hung loop | Then the loop survives — kick from the main flow |
| Set the timeout to your loop's worst case + margin | Too short → false resets |
| Use a **windowed** watchdog where available | Detects *too-fast* kicks too (runaway code) |
| Independent clock (IWDG) for the critical one | Survives a main-clock failure |

**The Mars Pathfinder tie-in (from `04`).** It was precisely a watchdog that
*detected* the priority-inversion hang on Mars: the high-priority bus task
failed to complete in time, the watchdog noticed the system wasn't healthy, and
it triggered the protective reset — repeatedly, until the priority-inheritance
patch fixed the root cause. The watchdog did its job perfectly; it was the
symptom alarm, not the disease.

**The power footnote.** The watchdog interacts with sleep: a watchdog that keeps
running in deep sleep will reset you mid-sleep unless you either feed it from a
wake event or use a watchdog that pauses in low-power modes. Many designs use an
independent low-power watchdog (IWDG) clocked from the always-on low-speed
oscillator so it survives sleep and clock failures alike.

---

## Common Confusion Points

### "Lower clock speed always saves power, right?"

Not for *energy* (the thing that drains your battery). Dynamic *power* drops
with frequency, but a slower clock means you stay *awake longer* to finish the
work — and active mode is far above the sleep floor. Often "race to idle" (run
fast, finish, sleep deep) uses less total energy. Measure the actual duty cycle;
the answer depends on how low your sleep floor is.

### "I picked the deepest sleep mode and now my device won't keep time / forgot its state"

Deep modes (Standby/Shutdown) lose RAM and most registers and wake like a reset.
If you need to retain state or keep a running clock, use Stop mode (RAM
retained) or store the value in the small always-on backup RAM / RTC backup
registers that survive deep sleep. Match the mode to what you must remember.

### "My MCU sleeps but the board still draws milliamps"

The MCU is one consumer; the *board* has others — pull-up resistors, an LDO
regulator's quiescent current, an always-on sensor, a leaking I/O pin driving a
floating input. The MCU's µA datasheet figure is meaningless if a status LED or
a poorly-chosen regulator dominates. Power budgeting is a *board* exercise, not
just an MCU one. (See `electronics/`.)

### "The watchdog keeps resetting my device in sleep"

A free-running watchdog expires during a long sleep. Either feed it on each
wake, configure it to halt in low-power modes, or size its timeout beyond your
sleep interval. The independent low-power watchdog is designed to coexist with
sleep — but you must plan the interaction.

---

## Decision Cheat Sheet

| I need to... | Reach for |
|---|---|
| Idle a few microseconds between bytes | Sleep mode (WFI) — wake on any IRQ |
| Idle seconds between samples, keep state | Stop / low-power mode + RTC alarm |
| Idle long, can re-init on wake | Standby / deep sleep + RTC or wake pin |
| Lowest possible off current | Shutdown (wakes via full reset) |
| Wake on a schedule | RTC alarm (32.768 kHz low-power domain) |
| Wake on an external event | Wake pin / EXTI interrupt |
| Cut a peripheral's power while unused | Clock gate it (RCC) / power off its domain |
| Big run-mode power win | Voltage scaling (DVFS) — quadratic in V |
| Decide run-slow vs race-to-idle | Compare against the sleep floor; measure energy |
| Estimate battery life | avg current = duty-weighted; life = mAh / avg I |
| Recover an unattended hang | Watchdog timer (independent, low-power clock) |
| Keep a watchdog from resetting in sleep | IWDG that halts in LP mode, or feed on wake |
