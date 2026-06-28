---
maxim_schema: maxim.frontmatter.v1
id: maxim:embedded-systems:rtos
kind: guide
module: embedded-systems
section: embedded-systems
title: RTOS - Tasks, Schedulers, Rate-Monotonic, Priority Inversion
status: source-custody
source_custody: partial
current_path: embedded-systems/04-RTOS.md
canonical_path: embedded-systems/04-RTOS.md
backsource_ids: [proof-backfill:embedded-systems:04-rtos, git-history:embedded-systems:04-rtos]
concepts: [rtos, scheduling, rate-monotonic, edf, priority inversion, priority inheritance]
root_concepts: [rtos]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# RTOS — Tasks, Schedulers, Rate-Monotonic, Priority Inversion

## The Big Picture

A real-time operating system is a small scheduler plus synchronization
primitives that lets multiple tasks share one core while *meeting deadlines*.
It is not Linux shrunk down — it is a different design point. Linux optimizes
throughput and fairness; an RTOS optimizes *predictability*. The whole kernel
might be 5–20 KB. You already know processes, threads, mutexes, and scheduling
in the abstract; this guide is about the embedded specialization — fixed
priorities, preemption, and the deadline math that makes "real-time" a
provable property rather than a marketing word.

```
+-----------------------------------------------------------------------+
|                        AN RTOS AT WORK                                |
|                                                                       |
|  TASKS (each = own stack, priority, state)                            |
|  .----------.  .----------.  .----------.  .----------.               |
|  | Control  |  | Comms    |  | Logger   |  | Idle     |               |
|  | prio 5   |  | prio 3   |  | prio 1   |  | prio 0   |               |
|  | RUNNING  |  | READY    |  | BLOCKED  |  | READY    |               |
|  '----------'  '----------'  '----------'  '----------'               |
|       |             |             |             |                     |
|       v             v             v             v                     |
|  .------------------------------------------------------------.       |
|  |               SCHEDULER (fixed-priority preemptive)         |      |
|  |  "run the highest-priority READY task. Always."             |      |
|  |  driven by SysTick + events (sem give, queue post)          |      |
|  '------------------------------------------------------------'       |
|       |                                                               |
|       v                                                               |
|  .------------------------------------------------------------.       |
|  |  PRIMITIVES: semaphores, mutexes, queues, event groups,    |       |
|  |  software timers, notifications                            |       |
|  '------------------------------------------------------------'       |
|       |                                                               |
|       v                                                               |
|  ONE Cortex-M core   +   ISRs preempting EVERYTHING above             |
+-----------------------------------------------------------------------+
```

**Read top-down.** Tasks are at the top; the scheduler in the middle decides
who runs; primitives let tasks coordinate. ISRs (`03`) sit *above* the whole
RTOS — no task can preempt an ISR, but an ISR can wake a task.

---

## Task vs Thread vs Process — Mapping Your Mental Model

| Concept you know | RTOS analogue | Difference |
|------------------|---------------|------------|
| Process | (none) | No address-space isolation — one flat memory |
| Thread | **Task** | Own stack + priority; shares all memory |
| Thread priority (dynamic) | Task priority (**fixed**) | No aging/fairness; you set it, it stays |
| Context switch (µs–ms) | Context switch (**~1 µs**) | Tiny — just save/restore registers + SP |
| OS scheduler (CFS, fair) | Fixed-priority preemptive | Highest-ready-task-wins, no fairness |
| `pthread_mutex` | Mutex (with inheritance) | Adds priority-inheritance for real-time |
| Virtual memory per process | One physical space (MPU at most) | A task can scribble another's memory |

The defining shift: **tasks share one address space with no protection** (an
optional MPU can sandbox stacks, but there's no MMU/virtual memory). A wild
pointer in one task corrupts another. This is the price of the RTOS's tiny
size and speed. Discipline replaces hardware isolation.

### Task states

```
            create
              |
              v
        +-----------+   highest ready    +-----------+
        |  READY    |------------------->|  RUNNING  |
        |           |<-------------------|           |
        +-----+-----+   preempted/yield  +-----+-----+
              ^                                |
   event /    |                                | block on
   timeout    |                                | sem/queue/delay
              |          +-----------+         |
              +----------|  BLOCKED  |<--------+
                         '-----------'
                               ^
                               v
                         .-----------.
                         | SUSPENDED | (explicitly paused)
                         '-----------'
```

A task is RUNNING (one at a time on a single core), READY (wants the CPU),
BLOCKED (waiting on a primitive or delay), or SUSPENDED (parked). The scheduler
only ever runs the highest-priority READY task. A blocked task consumes zero
CPU — the whole point of an RTOS over a polling super-loop.

---

## The Scheduler — Fixed-Priority Preemptive

The dominant RTOS scheduling policy. Two rules: (1) always run the
highest-priority READY task; (2) the instant a higher-priority task becomes
READY (an ISR gives it a semaphore, a delay expires), preempt the current task.

```
  PREEMPTION TIMELINE
  prio 5 (Control)  ........####............####........
  prio 3 (Comms)    ....####....####....####....####....
  prio 1 (Logger)   ##........##........##........##....
                    ^   ^      ^
                    |   |      Comms ready -> preempts Logger
                    |   Control's tick fires -> preempts Comms
                    Logger runs only when nothing higher is ready

  '#' = running    '.' = ready-but-waiting or blocked
```

Higher-priority work always wins the core immediately — that's what makes
latency bounded. The cost is that a runaway high-priority task can *starve*
everything below it (no fairness), and that you, the engineer, must assign
priorities correctly. That assignment is not guesswork — it has theory.

| Policy | Rule | RTOS reality |
|--------|------|--------------|
| Fixed-priority preemptive | Highest-priority ready task runs | The default everywhere |
| Round-robin (within a priority) | Time-slice equal-priority tasks | Optional, for fairness among peers |
| Cooperative | Tasks yield voluntarily | Smallest, but one bad task hangs all |
| EDF (dynamic) | Earliest deadline runs | Rare in commercial RTOS; theoretically optimal |

---

## Rate-Monotonic Scheduling — Priorities From Math

For periodic tasks, you don't have to guess priorities. **Rate-Monotonic (RM)**
assigns priority by *rate*: the task with the shortest period gets the highest
priority. It is the provably optimal *fixed-priority* assignment for periodic
tasks (Liu & Layland, 1973) — if any fixed-priority assignment can meet all
deadlines, RM can.

```
  RATE-MONOTONIC PRIORITY ASSIGNMENT
  +------------------------------------------------------------+
  | Task     Period T   ->   Priority (shorter period = higher)|
  | A         2 ms             HIGHEST                         |
  | B         5 ms             middle                          |
  | C        10 ms             LOWEST                          |
  +------------------------------------------------------------+
  "Fastest cadence wins the CPU."
```

### The utilization bound (~0.693)

RM comes with a schedulability test. Let each task i have worst-case execution
time C_i and period T_i; its utilization is U_i = C_i / T_i. For n periodic
tasks, RM **guarantees** all deadlines are met if total utilization satisfies:

```
  n
  SUM (C_i / T_i)  <=  n * (2^(1/n) - 1)
  i=1

  n=1 -> 1.000      As n -> infinity, the bound -> ln(2) = 0.6931...
  n=2 -> 0.828
  n=3 -> 0.780
  n=4 -> 0.757
  n=5 -> 0.743
  ...
  n=inf-> 0.693     <- the famous ~69% RM utilization bound
```

So RM *guarantees* schedulability up to roughly **69% CPU utilization** for
many tasks. This is a **sufficient, not necessary** condition: above 69% it
*may* still be schedulable, you just need the exact test (response-time
analysis, `07`) to prove it. The lost ~31% is the price of using a simple
fixed-priority scheme instead of a dynamic one.

**Worked example.** Three tasks: A (C=0.5 ms, T=2 ms), B (C=1 ms, T=5 ms),
C (C=2 ms, T=10 ms). Utilizations: 0.25 + 0.20 + 0.20 = **0.65**. The n=3 bound
is 0.780. Since 0.65 ≤ 0.780, RM **guarantees** all three meet their deadlines.
Assign A highest priority (shortest period), then B, then C.

---

## EDF — Earliest Deadline First

EDF is the *dynamic-priority* alternative: at every scheduling instant, run the
task whose absolute deadline is nearest. Priorities aren't fixed — they shift
as deadlines approach.

```
  RM (fixed)                          EDF (dynamic)
  ----------                          -------------
  priority = f(period), set once      priority = f(time-to-deadline), changes
  bound ~0.693 (n large)              bound = 1.00 (full utilization!)
  simple, cheap to implement          must track deadlines, more overhead
  predictable under overload          unpredictable under overload (domino)
  ubiquitous in commercial RTOS       rare; used where 100% util is needed
```

| Property | Rate-Monotonic | EDF |
|----------|----------------|-----|
| Priority type | Static | Dynamic |
| Utilization bound | n(2^(1/n)-1) → 0.693 | **1.000** |
| Overhead | Low | Higher (deadline tracking) |
| Overload behavior | Lower-priority tasks fail predictably | Domino effect, hard to predict |
| Implementation | Trivial | Needs deadline-aware scheduler |
| Commercial use | Dominant | Niche |

EDF is **theoretically optimal** — it can schedule any task set up to 100%
utilization that *any* algorithm could. So why isn't it everywhere? Because RM's
*predictability under overload* is worth more than EDF's extra ~31% headroom.
When an RM system is overloaded, the lowest-priority task misses first —
predictable, you know who suffers. When an EDF system overloads, it can cascade
("domino"): one missed deadline pushes the next, and the failure is hard to
bound. For safety-critical embedded, predictable degradation beats peak
utilization.

---

## Priority Inversion — and the Mars Pathfinder

Here is the famous failure mode that every real-time engineer must understand.
A high-priority task gets *blocked by a low-priority task* holding a shared
resource — inverting the priority order. If a medium-priority task then
preempts the low one, the high-priority task waits indefinitely.

```
+-----------------------------------------------------------------------+
|                   UNBOUNDED PRIORITY INVERSION                        |
|                                                                       |
|  H (high)   ...wants the mutex L holds... B  L  O  C  K  E  D  ...... |
|                                            ^                          |
|  M (medium) ......................########################........... |
|                                   ^ M preempts L (M doesn't need      |
|                                     the mutex) and runs a LONG time   |
|  L (low)    ....####[takes mutex]##..........................[done]## |
|                                                                       |
|  Result: H -- the MOST urgent task -- is blocked for as long as M     |
|  chooses to run. The priorities are INVERTED. Deadline missed.        |
+-----------------------------------------------------------------------+
```

The chain: L takes a mutex → H needs the same mutex, blocks on L → M (which
needs nothing) preempts L because M > L → L can't run to release the mutex → H
stays blocked the entire time M runs. H's blocking time is bounded only by M's
runtime, not L's critical section. That is **unbounded** priority inversion.

### Mars Pathfinder (1997)

This exact bug nearly lost the **Mars Pathfinder** mission in July 1997. The
Sojourner rover's lander used VxWorks. A high-priority `bc_dist` task (bus
management) shared a mutex-protected information bus with a low-priority
`ASI/MET` (meteorological) task. A medium-priority, long-running communications
task sat between them in priority. The classic inversion occurred: the
meteorological task held the mutex, the comms task preempted it, and the
high-priority bus task blocked long enough that a **watchdog timer** (`08`)
detected the bus task hadn't completed and triggered a **system reset** — over
and over, on Mars.

The fix was already available in VxWorks: **priority inheritance** on the mutex,
which had been disabled. JPL diagnosed it by reproducing the fault on an
identical ground unit with tracing enabled, then uploaded a patch that flipped
the mutex's inheritance flag on. The rover recovered. The lesson burned into
the field: *priority inversion is not a corner case — it is the default
behavior of a naive mutex, and it will find you.*

---

## Priority Inheritance and Priority Ceiling — The Fixes

Two protocols bound the inversion so a high-priority task waits only for the
*critical section*, never for unrelated medium tasks.

```
  PRIORITY INHERITANCE
  +------------------------------------------------------------+
  | When H blocks on a mutex held by L,                        |
  | L TEMPORARILY INHERITS H's priority.                       |
  | Now M cannot preempt L (L is effectively high).            |
  | L finishes its critical section fast, releases, drops back.|
  | H proceeds. Blocking is bounded by L's critical section.   |
  +------------------------------------------------------------+

  before:  H blocked while M runs (unbounded)
  after:   L runs at H's priority -> M waits -> L releases -> H runs
```

```
  PRIORITY CEILING
  +------------------------------------------------------------+
  | Each mutex has a CEILING = priority of the highest task    |
  | that can ever take it. A task taking the mutex is raised   |
  | to the ceiling immediately. Prevents deadlock AND          |
  | bounds inversion to ONE critical section. Stronger;        |
  | needs static knowledge of who uses what.                   |
  +------------------------------------------------------------+
```

| Protocol | Mechanism | Bounds inversion? | Prevents deadlock? | Cost |
|----------|-----------|-------------------|--------------------|------|
| Naive mutex | None | **No** (unbounded) | No | — |
| Priority inheritance | Holder inherits blocker's priority | Yes (to crit. section) | No | Low, dynamic |
| Priority ceiling | Holder raised to mutex ceiling | Yes | **Yes** | Needs static analysis |

**Practical rule.** Use a mutex *with priority inheritance* (FreeRTOS
`xSemaphoreCreateMutex` does this; a plain binary semaphore does **not**) for
any resource shared across priority levels. Never use a plain binary semaphore
as a lock between tasks of different priority — that is exactly the Pathfinder
setup.

### Old world → RTOS sync bridge

```
  You know...                          RTOS...
  ----------                           ------
  pthread_mutex (PI optional)          Mutex with priority inheritance
  Semaphore (counting)                 Counting semaphore (signaling)
  Condition variable                   Event group / task notification
  Blocking queue                       Queue (the RTOS message-passing core)
  Lock-free for low latency            Critical section (disable IRQ) for ISRs
```

---

## Choosing and Configuring an RTOS

```
                  DO I NEED AN RTOS?
                        |
        .---------------+----------------.
        | <= 2-3 timed activities, no    |  -> super-loop + timers (02/03)
        | blocking I/O, simple           |
        +--------------------------------'
        | many tasks, blocking waits,    |  -> RTOS
        | independent rates, priorities  |
        '---------------+----------------'
                        |
            +-----------+-----------+-----------+
            v           v           v           v
        FreeRTOS    Zephyr      ThreadX     safety-cert
        ubiquitous  Linux-      Azure RTOS  (SafeRTOS,
        tiny, free  Foundation, (commercial, integrity)
                    driver-rich  small)
```

| RTOS | Footprint | Niche |
|------|-----------|-------|
| FreeRTOS | ~5–10 KB | The default; huge ecosystem, AWS-backed |
| Zephyr | Larger | Rich drivers, networking, Linux Foundation governance |
| ThreadX (Azure RTOS) | Tiny | Deterministic, certified variants |
| embOS / RTX | Small | Commercial, IDE-integrated |
| SafeRTOS / INTEGRITY | Varies | Safety-certified (DO-178, IEC 61508) |

Sizing pitfall unique to RTOS: **each task needs its own stack**, sized to its
worst-case call depth + the ~8-word interrupt frame + any nested-ISR depth.
Under-size a task stack and it silently overflows into the next task's
memory — a top cause of mysterious RTOS crashes. Use the RTOS's stack
high-water-mark API to measure real usage.

---

## Common Confusion Points

### "Is an RTOS just a small Linux?"

No — different goals. Linux maximizes throughput and fairness with a dynamic,
aging scheduler and full memory isolation. An RTOS maximizes *predictability*
with fixed priorities, preemption, and (usually) no memory protection. An RTOS
kernel is kilobytes; it makes timing analyzable, which Linux does not (without
the PREEMPT_RT patches and great care, covered in `os/`).

### "Why give a low-priority task the high task's priority — isn't that backwards?"

Priority inheritance is temporary and surgical: only while the low task *holds a
lock the high task needs*, and only for the critical section. It exists to stop
unrelated medium tasks from indefinitely delaying the high task. The instant the
lock is released, the low task drops back. It's a fix for inversion, not a
priority change in spirit.

### "I'm using a binary semaphore as a lock — fine, right?"

Dangerous across priority levels. A binary semaphore has no notion of an owner,
so it can't implement priority inheritance — it's exactly the Pathfinder setup.
Use a **mutex** (which has an owner and inheritance) for mutual exclusion;
reserve semaphores for *signaling* (ISR-to-task, producer-consumer counts).

### "RM caps me at 69% CPU — that seems wasteful"

The 69% is a *guarantee* (sufficient condition), not a ceiling. Many real task
sets schedule fine well above it; you just need the exact response-time test
(`07`) instead of the simple bound to prove it. If you genuinely need
guaranteed 100% utilization, that's EDF's domain — at the cost of unpredictable
overload behavior.

---

## Decision Cheat Sheet

| I need to... | Reach for |
|---|---|
| Run many independent periodic tasks | RTOS, fixed-priority preemptive |
| Assign priorities to periodic tasks | Rate-Monotonic (shortest period = highest) |
| Prove deadlines are met (quick test) | RM utilization bound ≤ n(2^(1/n)-1) |
| Prove deadlines above the RM bound | Exact response-time analysis (`07`) |
| Squeeze 100% utilization | EDF (accept unpredictable overload) |
| Protect a resource shared across priorities | Mutex **with priority inheritance** |
| Prevent both inversion and deadlock | Priority-ceiling protocol |
| Signal a task from an ISR | Counting semaphore / notification (`...FromISR`) |
| Pass messages between tasks | Queue |
| Avoid a Pathfinder-style hang | Never lock across priorities with a bare binary semaphore |
| Diagnose a mystery RTOS crash | Check per-task stack high-water marks |
| Decide RTOS vs super-loop | Many blocking, multi-rate tasks → RTOS, else loop |
