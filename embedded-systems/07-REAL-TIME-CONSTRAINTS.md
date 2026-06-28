---
maxim_schema: maxim.frontmatter.v1
id: maxim:embedded-systems:real-time-constraints
kind: guide
module: embedded-systems
section: embedded-systems
title: Real-Time Constraints - Hard vs Soft, WCET, Schedulability, Jitter
status: source-custody
source_custody: partial
current_path: embedded-systems/07-REAL-TIME-CONSTRAINTS.md
canonical_path: embedded-systems/07-REAL-TIME-CONSTRAINTS.md
backsource_ids: [proof-backfill:embedded-systems:07-real-time-constraints, git-history:embedded-systems:07-real-time-constraints]
concepts: [real-time, hard real-time, wcet, schedulability, jitter, deadline]
root_concepts: [real-time]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# Real-Time Constraints — Hard vs Soft, WCET, Schedulability, Jitter

## The Big Picture

This is the theory that makes "real-time" a provable property instead of a
hope. A real-time system is correct only if it produces the right answer *and*
produces it by a deadline. Lateness is a failure mode equal to a wrong answer.
The discipline has three pillars: classifying *how bad* a missed deadline is
(hard/firm/soft), bounding *how long the work can take* (WCET), and *proving the
whole task set fits* in time (schedulability). Jitter — variation in timing — is
the enemy threading through all of it.

```
+-----------------------------------------------------------------------+
|                THE REAL-TIME CORRECTNESS STACK                        |
|                                                                       |
|  CLASSIFY: how costly is a miss?                                      |
|     hard  -> catastrophe (airbag, motor)                              |
|     firm  -> result useless if late, but no disaster                  |
|     soft  -> degraded quality (dropped video frame)                   |
|           |                                                           |
|           v                                                           |
|  BOUND: WCET -- worst-case execution time of each task                |
|     C_i = the longest the code can EVER take                          |
|           |                                                           |
|           v                                                           |
|  PROVE: schedulability -- does the whole task set meet deadlines?     |
|     utilization bound (quick) OR response-time analysis (exact)       |
|           |                                                           |
|           v                                                           |
|  MINIMIZE: jitter -- keep the actual timing tight around the ideal    |
+-----------------------------------------------------------------------+
```

**Read top-down: it's a pipeline of guarantees.** You classify the deadline,
bound each task's time, prove they collectively fit, then squeeze the variance.
A system that skips any step is "real-time" by assertion only.

---

## Hard vs Firm vs Soft Real-Time

The first question for any timed activity: *what happens when the deadline is
missed?* This classification drives the entire engineering budget.

```
  UTILITY of a result vs TIME (the deadline at D)
  ----------------------------------------------------
  HARD:   utility +-----------+        a miss = system failure.
                  |           |        Value drops to negative
                  |           +---___  (catastrophic) after D.
                  +-----------|------- D
  FIRM:   utility +-----------+        a miss = result worthless,
                  |           |        but no harm. Value = 0 after D.
                  +-----------+======  (drop it, move on)
                              D
  SOFT:   utility +-----------+        a miss = degraded value that
                  |           +\___    decays gracefully after D.
                  +-----------+----\-- D  (late is still somewhat useful)
```

| Class | A missed deadline means... | Example | Design budget |
|-------|---------------------------|---------|---------------|
| **Hard** | System failure, possible harm | Airbag fire, motor commutation, brake-by-wire | Provable worst case; certification |
| **Firm** | This result is useless; discard it | Sensor frame in a control loop you can skip | Bound, but tolerate rare misses |
| **Soft** | Quality degrades, value decays | Video/audio frame, UI responsiveness | Best-effort, statistical targets |

The crucial distinction from your server world: a soft real-time target ("p99
< 50 ms") is a *statistical* goal you optimize on average. A **hard** real-time
deadline is a *correctness* constraint you must *prove* is never violated — not
on average, not at p99, but in the absolute worst case. That shifts the whole
method from measurement to analysis.

### Old world → real-time bridge

```
  You know (server)...                 Real-time embedded...
  -------------------                  ---------------------
  SLA / SLO (p99 latency)              Soft deadline (statistical)
  Tail latency you tolerate            Hard deadline you must PROVE
  Average throughput                   Worst-case execution time (WCET)
  Capacity planning (avg load)         Schedulability (worst-case load)
  "usually meets target"               "provably never misses"
```

---

## WCET — Worst-Case Execution Time

WCET is the longest time a piece of code can *ever* take to run, over all
inputs and all hardware states. It is the C_i that fed the rate-monotonic math
in `04`. Crucially, WCET is **not** the measured maximum — measurement can miss
the true worst case — and it is **not** the average. It is an upper bound you
can defend.

```
  THE WCET DISTRIBUTION
  frequency
     |        .-.
     |       /   \      <- typical (what you usually measure)
     |      /     \
     |     /       \________
     |    /                 \____  rare slow paths
     +---|-------------------|----|--------> execution time
        BCET              measured  WCET (true bound -- you may
        (best case)        max       never have OBSERVED it)
                                      ^ this is what must fit the deadline
```

What makes WCET hard on real hardware:

| Source of variability | Effect | Mitigation for analyzability |
|-----------------------|--------|------------------------------|
| Input-dependent paths | Different branches → different time | Analyze the longest path |
| Loops with data-dependent bounds | Variable iteration count | Cap iterations; bound them |
| **Caches** | Hit vs miss = 1 vs ~100 cycles | Lock cache, or run from SRAM, or count all-miss |
| Branch prediction | Misprediction stalls | Pessimistic assumption |
| Flash wait states | Fetch stalls at high clock | Account in the bound |
| Pipeline state | Depends on prior instructions | Conservative modeling |
| **Interrupts preempting** | Add ISR time to the path | Count interference (see schedulability) |
| **DMA bus contention** | Stalls CPU memory access | Budget bus interference |
| Dynamic allocation | malloc time varies / fragments | Forbid it (static, `05`) |

This is *why* the embedded culture distrusts caches, branch predictors, and
dynamic memory: each one widens the gap between average and worst case, and the
worst case is what you must guarantee. The simplest Cortex-M0 with no cache and
deterministic flash is *easier to certify* than a fast M7 precisely because its
timing is predictable. There's a real tension: performance features improve the
average but complicate (or wreck) the worst-case bound.

**Methods to obtain WCET.** *Static analysis* tools (aiT, etc.) model the
processor and prove an upper bound — sound but pessimistic and expensive.
*Measurement-based* runs the code on hardware over many inputs and takes the max
plus a safety margin — practical but *unsound* (you might never hit the true
worst case). Safety-critical work uses static analysis or a hybrid; most
commercial embedded uses measurement plus margin and discipline.

---

## Schedulability — Proving the Task Set Fits

Given each task's WCET (C_i) and period (T_i), schedulability analysis proves
the whole set meets every deadline. Two levels of rigor.

### Level 1: the utilization bound (quick, sufficient)

From `04`: under rate-monotonic priorities, n periodic tasks are guaranteed
schedulable if

```
  n
  SUM (C_i / T_i)  <=  n * (2^(1/n) - 1)     -> 0.693 as n grows
  i=1
```

This is *sufficient but not necessary*: pass it and you're safe; fail it and
you might still be fine — you just need the exact test. Cheap to compute, good
for a first-cut sanity check.

### Level 2: response-time analysis (exact, necessary-and-sufficient)

The precise test. For each task i, compute its worst-case **response time** R_i
— the longest time from release to completion, *including all interference from
higher-priority tasks preempting it* — and check R_i ≤ deadline D_i.

```
  RESPONSE-TIME RECURRENCE (fixed-priority)
  R_i = C_i  +  SUM over higher-priority tasks j of  ceil(R_i / T_j) * C_j
                \_________________ interference ________________/

  Iterate: start R_i = C_i, plug in, recompute, until R_i stops growing
  (a fixed point). If it converges with R_i <= D_i, task i is schedulable.
```

**Worked example.** Tasks from `04`: A (C=0.5, T=2), B (C=1, T=5), C (C=2,
T=10), deadlines = periods, RM priorities (A > B > C). Check C, the
lowest-priority, hardest case:

```
  R_C^(0) = C_C = 2
  R_C^(1) = 2 + ceil(2/2)*0.5 + ceil(2/5)*1
          = 2 + 1*0.5 + 1*1 = 3.5
  R_C^(2) = 2 + ceil(3.5/2)*0.5 + ceil(3.5/5)*1
          = 2 + 2*0.5 + 1*1 = 4.0
  R_C^(3) = 2 + ceil(4.0/2)*0.5 + ceil(4.0/5)*1
          = 2 + 2*0.5 + 1*1 = 4.0   <- converged
  R_C = 4.0 ms <= D_C = 10 ms.  Task C meets its deadline. Schedulable.
```

Note this set's utilization was 0.65 < 0.78, so the quick bound already passed
— but response-time analysis is what you reach for when utilization sits above
the bound and you must *prove* it still works. It also extends to blocking
terms: add the worst-case blocking B_i (from a held mutex, `04`'s priority
inversion bounded by inheritance) into R_i to account for lower-priority tasks
holding shared resources.

| Test | Type | Cost | Use |
|------|------|------|-----|
| Utilization bound | Sufficient | Trivial | Quick sanity check |
| Response-time analysis | Exact | Iterative per task | Prove a tight system |
| + blocking term | Exact + resources | Adds B_i | When tasks share mutexes |

---

## Jitter — The Variance Enemy

Jitter is the variation in *when* a periodic event actually happens versus when
it should. A 1 kHz control loop ideally fires every 1.000 ms; jitter is the
spread around that. For control systems, jitter degrades stability and injects
noise; for sampling, it corrupts the signal (timing noise looks like amplitude
noise).

```
  IDEAL (no jitter)        JITTERY
  every 1.000 ms           1.02, 0.97, 1.05, 0.94 ms ...
  |   |   |   |   |         |    |  |     |   |
  +---+---+---+---+         +----+--+-----+---+
  metronome-steady         varies -> control noise, sampling error
```

| Jitter source | Cause | Reduce by |
|---------------|-------|-----------|
| Release jitter | Scheduler granularity, tick alignment | Hardware-timer-triggered tasks, not software delays |
| Interrupt latency variance | Critical sections of varying length | Keep critical sections short and uniform |
| Preemption by higher priority | Higher task runs at varying times | Give the jitter-sensitive task high priority |
| Bus/DMA contention | Variable memory access time | Separate SRAM banks, bound DMA |
| Cache/branch effects | Hit/miss variation | Run-from-SRAM, lock cache |

The strongest jitter-reduction move is to take the human (software) out of the
timing loop: trigger the time-critical action **directly from a hardware
timer** (e.g. start an ADC conversion on a timer compare event, `03`) rather
than from a software handler that itself competes for the CPU. Hardware fires at
the same phase every period regardless of what the CPU is doing — near-zero
jitter. (Bridge: this is the embedded version of the lesson that the most
reliable scheduled job is the one the kernel/hardware fires, not the one your
application polls a clock for.)

---

## Putting It Together — A Real-Time Design Checklist

```
  +------------------------------------------------------------+
  | 1. List every periodic/aperiodic timed activity.           |
  | 2. Classify each: hard / firm / soft.                      |
  | 3. Bound each one's WCET (C_i) -- defensibly.              |
  | 4. Assign priorities: rate-monotonic for periodic (04).    |
  | 5. Quick check: utilization <= n(2^(1/n)-1)?               |
  | 6. If above the bound, run response-time analysis.         |
  | 7. Add blocking terms for shared mutexes (priority         |
  |    inheritance to bound them, 04).                         |
  | 8. Drive jitter-sensitive actions from hardware timers.    |
  | 9. Leave headroom -- never design to 100% on hard RT.      |
  +------------------------------------------------------------+
```

---

## Common Confusion Points

### "Real-time means low latency, right?"

No — it means *bounded, predictable* latency, met *every* time. A 10 Hz control
loop with a 100 ms deadline is hard real-time if it must *never* exceed 100 ms,
even though 100 ms is slow. A 2 ms-average web service with occasional 500 ms
spikes is fast but *not* real-time. Determinism, not speed, is the property.

### "I measured the max execution time — that's my WCET, right?"

Not safely. Measurement can miss the true worst case (the rare input + cache
state + interrupt alignment that produces the longest run). Measured-max plus a
margin is common practice but *unsound* — for hard real-time you want static
WCET analysis or a strong hybrid. The whole point of WCET is the case you
*haven't* observed.

### "My utilization is 60% — am I definitely fine?"

If it's under the RM bound (~0.69 for many tasks) and your assumptions hold
(independent periodic tasks, deadlines = periods, no blocking), yes — that's
the *guarantee*. But add shared mutexes, jittery releases, or aperiodic bursts
and you need the exact response-time test with blocking terms to be sure.
Utilization is a screen, not a proof.

### "Why is a faster CPU sometimes worse for real-time?"

Because speed often comes from caches, branch prediction, and out-of-order
execution — all of which *widen* the gap between average and worst case. The
average improves; the worst-case bound gets harder to prove and may even
worsen relative to the deadline margin. A slower, simpler, deterministic core
can be the *more* certifiable choice. (See `computer-architecture/` for the
microarchitecture features in question.)

---

## Decision Cheat Sheet

| I need to... | Reach for |
|---|---|
| Decide how strict a deadline is | Classify hard / firm / soft |
| Justify the engineering budget | Hard → prove; soft → optimize statistically |
| Get each task's C_i for scheduling | WCET — static analysis (safety) or measure+margin |
| Quick check if a task set fits | Utilization ≤ n(2^(1/n)-1) (RM bound) |
| Prove a set above the util bound | Response-time analysis (iterate to fixed point) |
| Account for shared-mutex blocking | Add blocking term B_i to R_i (bound via inheritance) |
| Reduce timing variance | Drive critical actions from hardware timers |
| Protect a jitter-sensitive task | High priority + short, uniform critical sections |
| Choose a CPU for certifiability | Prefer deterministic timing over peak speed |
| Stay safe on hard real-time | Leave headroom; never design to the bound |
