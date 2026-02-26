# Concurrency — Engineering Reference

## The Big Picture

Concurrency correctness is hard because the interleaving of operations from multiple threads creates an exponential space of possible executions. This guide covers the formal foundations (Herlihy-Shavit territory), hardware memory models, practical synchronization primitives, and the modern concurrency abstractions used in production — from lock-free data structures to async/await.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  CONCURRENCY LANDSCAPE                                                       │
│                                                                              │
│  Correctness Properties          Progress Properties                         │
│  ───────────────────────────     ─────────────────────────────               │
│  Safety: nothing bad happens     Deadlock-freedom: some thread progresses    │
│  Linearizability: atomic ops     Starvation-freedom: every thread progresses │
│  Sequential consistency          Lock-freedom: some op completes in O(steps) │
│  Serializability (transactions)  Wait-freedom: every op completes in O(steps)│
│                                                                              │
│  Synchronization Models         Hardware Concerns                            │
│  ───────────────────────────     ──────────────────────────────              │
│  Mutex / monitors                Memory ordering (TSO, PSO, SC)              │
│  Reader-writer locks             Cache coherence (MESI protocol)             │
│  Lock-free (CAS, LL/SC)          False sharing, cache line contention        │
│  Wait-free (universal construction) Memory barriers / fences                 │
│  STM (transactional memory)      ABA problem                                 │
│  Message passing (CSP, Actors)                                               │
│  Async/await (cooperative)                                                   │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 1. Correctness Properties

### Safety and Liveness

**Safety** ("nothing bad ever happens"): The concurrent history is equivalent to some valid sequential history. Examples: mutual exclusion (at most one thread in CS), deadlock-freedom.

**Liveness** ("something good eventually happens"): Progress properties. Examples: some thread makes progress (deadlock-freedom), every thread eventually makes progress (starvation-freedom).

Formal models use **histories**: sequences of invocations and responses of operations on shared objects.

### Linearizability

**Definition** (Herlihy-Wing 1990): A history H is linearizable if:
1. It can be extended to a legal sequential history S by completing (or removing) pending operations.
2. The real-time order of operations in H is preserved in S (if op A completes before op B invokes, then A is before B in S).

```
Intuition: Each operation appears to take effect instantaneously at some point
           between its invocation and response (the linearization point).

Non-linearizable example:
  Thread 1: enqueue(1)  ─────────────────────────────
  Thread 2: enqueue(2)       ────────────────────────
  Thread 3: dequeue() returns 2, then dequeue() returns 1

  If the queue is FIFO, and enqueue(1) starts before enqueue(2),
  a linearizable queue cannot return 2 before 1.
  This execution is NOT linearizable for a FIFO queue.
```

**Compositionality** (Herlihy-Wing): If each object in a system is linearizable, the combined system is linearizable. This does NOT hold for sequential consistency — cannot compose sequentially consistent objects.

### Sequential Consistency

Weaker than linearizability: operations within each thread must be ordered, but no real-time constraint between threads. Different threads may observe different operation orderings.

**Java volatile** provides sequential consistency for accesses to volatile variables.

### Serializability (transaction model)

A set of concurrent transactions is serializable if the result is equivalent to some serial execution. Does NOT require real-time order (unlike strict serializability = linearizability + serializability).

**Conflict serializability**: Check via conflict dependency graph. Schedule is conflict-serializable iff dependency graph is acyclic.

---

## 2. Hardware Memory Models

### The Cache Coherence Problem

```
Multi-core CPU:

  Core 0              Core 1              Core 2
  ┌──────────┐        ┌──────────┐        ┌──────────┐
  │ L1 cache │        │ L1 cache │        │ L1 cache │
  └────┬─────┘        └────┬─────┘        └────┬─────┘
       │                   │                   │
  ┌────┴───────────────────┴───────────────────┴────┐
  │                  L3 cache (shared)               │
  └─────────────────────────┬───────────────────────┘
                             │
                           DRAM

Problem: Core 0 writes to x. Core 1 has x in L1 cache.
  Without coherence: Core 1 reads stale value.
  With coherence: Core 1's copy is invalidated or updated.
```

**MESI protocol** (Modified-Exclusive-Shared-Invalid):
```
States per cache line:
  M (Modified):  Only this cache has it; memory is stale; must write back.
  E (Exclusive): Only this cache has it; clean (matches memory).
  S (Shared):    Multiple caches have clean copies.
  I (Invalid):   Cache line not valid.

Transitions:
  Core 0 reads x (not in cache) → fetches from memory → state E
  Core 1 reads x (not in cache) → both Core 0 and Core 1 → state S for both
  Core 0 writes x → broadcasts RFO (Request For Ownership) → Core 1 line → I
                  → Core 0 line → M
```

MESI ensures coherence (each cache line has consistent value). But MESI does NOT guarantee that operations on different cache lines are seen in the same order.

### Memory Ordering — Why Compilers and CPUs Reorder

Modern CPUs and compilers aggressively reorder instructions for performance:
- **Out-of-order execution**: CPUs issue instructions in dependency order, not program order
- **Write buffers**: CPU writes go into a buffer before reaching cache; other cores don't see them immediately
- **Compiler reordering**: Compilers move independent operations freely

```
Example (Dekker's algorithm, broken on x86):

Thread 1:              Thread 2:
  x = 1                  y = 1
  r1 = y                 r2 = x
  assert r1 == 1         assert r2 == 1

On x86 (TSO model): Both assertions can fail!
  Thread 1's write to x may still be in the write buffer
  when Thread 2 reads x, even though x=1 comes first in program order.
```

### Memory Models by Architecture

| Architecture | Model | Store-Store reorder | Load-Load reorder | Store-Load reorder | Load-Store reorder |
|--------------|-------|---------------------|-------------------|--------------------|-------------------|
| x86/x86-64 | TSO (Total Store Order) | No | No | Yes | No |
| ARM64 | Relaxed | Yes | Yes | Yes | Yes |
| POWER | Relaxed | Yes | Yes | Yes | Yes |
| RISC-V | RVWMO (relaxed) | Yes | Yes | Yes | Yes |
| Intel Itanium | IA-64 | Yes | Yes | Yes | Yes |

**TSO (Total Store Order)**: x86 stores go into a FIFO write buffer. A store is visible to other cores only after leaving the buffer. A load that occurs after a store may read the old value if the store is still buffered.

### Memory Barriers (Fences)

```
Types:
  StoreStore barrier:  All stores before the barrier visible before any store after.
  LoadLoad barrier:    All loads before the barrier complete before any load after.
  LoadStore barrier:   All loads before the barrier complete before any store after.
  StoreLoad barrier:   All stores before barrier visible before any load after.
                       MFENCE on x86. Full barrier. Most expensive.

x86 MFENCE use: between a store and a subsequent load to prevent reordering.
ARM DMB ISH: data memory barrier for inner shareable domain.
```

**C++ memory_order** (C++11 atomics):
```cpp
memory_order_relaxed:  No ordering guarantees; just atomicity.
memory_order_acquire:  No loads/stores in this thread can be reordered before this load.
memory_order_release:  No loads/stores in this thread can be reordered after this store.
memory_order_acq_rel:  Acquire + Release (for read-modify-write ops).
memory_order_seq_cst:  Sequential consistency. Full fence on x86.

// Release-acquire pattern (most common for synchronization):
// Producer:
flag.store(true, std::memory_order_release);  // All prior writes visible before flag

// Consumer:
while (!flag.load(std::memory_order_acquire));  // Sees all writes that preceded store
// Now safe to read data written by producer.
```

**Java Memory Model (JMM)**: Happens-before relation. `volatile` writes happen-before subsequent `volatile` reads. Synchronized block exit happens-before entry of anyone synchronizing on same monitor. `volatile` = seq_cst on all architectures.

**.NET Memory Model**: Weaker than Java in documentation; in practice CLR on x86 matches JMM. `Volatile.Read()` = acquire; `Volatile.Write()` = release. `Thread.MemoryBarrier()` = full fence. `Interlocked.*` operations = sequentially consistent.

---

## 3. Lock-Based Concurrency

<!-- @editor[audience/P2]: The mutex properties (mutual exclusion, progress, bounded waiting), Dekker's algorithm, Peterson's algorithm, TAS/TTAS definitions, Coffman conditions, and Banker's algorithm are CS curriculum material this learner wrote multi-threaded .NET code with professionally for years. They know Monitor.Enter/Exit, ReaderWriterLockSlim, and Interlocked from production use. What's valuable in this section: CLH/MCS queue locks (AQS internals — probably new), the priority inversion explanation, and the deadlock detection/recovery discussion. Consider trimming Dekker/Peterson/TAS definitions to one-liners and leading with CLH/MCS since that's what actually runs in JVM's AbstractQueuedSynchronizer. -->

### Mutex (Mutual Exclusion)

```
Properties:
  Mutual exclusion: at most one thread in critical section
  Progress: if no thread in CS and some want in, one enters eventually
  Bounded waiting: each thread enters within bounded time (starvation-freedom)

Spinlock: active poll (busy wait). Good for short CS, bad for long.
  pro: no context switch overhead, good with many cores
  con: wastes CPU, causes priority inversion

Blocking mutex: OS-assisted sleep/wake. Good for long CS.
  con: context switch overhead (~1-5 μs)
```

**Dekker's algorithm** (first mutex without hardware support): Complex, requires memory barriers. Never used in practice — hardware atomics are available.

**Peterson's algorithm** (two-thread only): Works with acquire/release semantics. Clean, proof-friendly. Two variables: `flag[2]` and `turn`.

**Test-and-Set (TAS)**: `atomic { old = x; x = 1; return old; }` — simplest spinlock. High contention → cache line invalidation storm.

**Test-and-Test-and-Set (TTAS)**: Spin on regular read (shared state S in MESI); only attempt TAS when it looks free. Reduces coherence traffic dramatically.

**CLH / MCS Queue Lock** (Craig-Landin-Hagersten, Mellor-Crummey-Scott):
```
Queue lock: each thread spins on its own cache line (not shared).
  Eliminates thundering herd on lock release.
  MCS: intrusive linked list of waiters.
  CLH: implicit linked list via predecessor's node.
Both: O(1) lock/unlock, each waiter spins on private cache line.
Used in Linux kernel rwlock, Java AbstractQueuedSynchronizer (AQS).
```

### Monitors and Condition Variables

```
Monitor = mutex + set of condition variables.

Python threading.Condition, Java Object.wait/notify, C++ std::condition_variable:

  Lock mutex
  while (!condition): cv.wait(mutex)   // atomically release mutex and sleep
  // condition is now true
  // ... critical section ...
  Unlock mutex

  // Other thread:
  Lock mutex
  // change state to make condition true
  cv.notify_all()
  Unlock mutex
```

**Spurious wakeups**: Threads can wake from `wait()` without `notify()`. Always check condition in a loop (`while`, not `if`).

**Mesa semantics** (Java, POSIX): `notify()` moves thread to ready queue; condition may change before it runs. Must re-check. **Hoare semantics** (original): Notified thread runs immediately; signaler suspends. Not used in practice (expensive).

### Reader-Writer Locks

```
Multiple readers can hold lock simultaneously.
Writer needs exclusive access.

Implementations:
  - Simple: counter for readers; writer waits for counter = 0.
  - Writer-priority: waiting writer blocks new readers.
  - Reader-priority: writer starves if steady stream of readers.
  - Fair (FIFO): mix based on arrival order.

std::shared_mutex (C++17), java.util.concurrent.locks.ReentrantReadWriteLock,
.NET ReaderWriterLockSlim.

Downgrade: hold write → acquire read → release write. Supported by some implementations.
Upgrade: hold read → acquire write. Risks deadlock if two threads try simultaneously.
```

### Deadlock

<!-- @editor[audience/P2]: The four Coffman conditions and Banker's algorithm are OS curriculum material (Dijkstra 1965). This learner has reviewed deadlock post-mortems in production .NET codebases. The conditions are useful as a quick reference checklist, but the Banker's algorithm explanation ("O(n²) check per request; too slow") is textbook content that adds no value beyond "it's too slow, nobody uses it." The valuable content here is lock ordering and the practical note about hard enforcement in large codebases. Consider collapsing Coffman conditions to a reference table and cutting Banker's to one sentence. -->

**Four Coffman conditions** (all must hold for deadlock):
1. Mutual exclusion
2. Hold and wait
3. No preemption
4. Circular wait

**Prevention**: Break one condition. Circular-wait prevention: acquire locks in global order.

**Avoidance**: Banker's algorithm — only grant if system stays in safe state. O(n²) check per request; too slow for most systems.

**Detection and recovery**: Allow deadlock; detect via wait-for graph cycle; recover by killing a thread.

**Lock ordering**: Most practical deadlock prevention. Define global lock hierarchy; always acquire in order. Hard to enforce across large codebases → use single high-level lock or STM.

---

## 4. Lock-Free and Wait-Free Algorithms

### Compare-And-Swap (CAS)

```
CAS(address, expected, new_value):
  Atomically: if *address == expected then *address = new_value; return true
              else return false

This is the fundamental hardware primitive for lock-free programming.

x86: CMPXCHG instruction (with LOCK prefix for multi-core).
ARM: LDXR/STXR (Load-linked/Store-conditional — LL/SC). No ABA problem.
Java: Unsafe.compareAndSwap*, Atomic*.compareAndSet.
C++: std::atomic<T>::compare_exchange_weak / compare_exchange_strong.
.NET: Interlocked.CompareExchange.
```

### Lock-Free Stack (Treiber Stack 1986)

```
struct Node { T value; Node* next; };
atomic<Node*> top;

push(x):
  Node* node = new Node(x);
  do {
    node->next = top.load(relaxed);
  } while (!top.compare_exchange_weak(node->next, node));

pop():
  Node* old;
  do {
    old = top.load(relaxed);
    if (old == null) return EMPTY;
  } while (!top.compare_exchange_weak(old, old->next));
  return old->value;  // NOTE: memory reclamation problem here (see below)
```

**Lock-free**: If CAS fails, some other thread succeeded → system makes progress.
**Not wait-free**: Under contention, a thread can retry indefinitely.

### ABA Problem

```
Thread 1 reads top → node A. Preempted.
Thread 2: pops A, pops B, pushes A again (different memory? same pointer!).
Thread 1: CAS succeeds (top == A) but list structure is wrong.

Solutions:
  Tagged pointers: pack version counter in pointer (low bits or separate word).
    CAS on (pointer, version); version increments on each swap.
    x86-64: 128-bit CMPXCHG16B or hide version in high pointer bits.

  LL/SC (ARM, POWER, RISC-V): load-linked invalidated by any write to address,
    not just CAS from another thread. ABA cannot occur.

  Hazard pointers: before reading a pointer, announce it as "in use."
    Other threads cannot free memory pointed to by hazard pointer.

  RCU (Read-Copy-Update): readers don't block writers; writers make new copy,
    then atomically swap; old version freed only after all readers done.
    Used extensively in Linux kernel.
```

### Lock-Free Queue (Michael-Scott Queue 1996)

```
Two pointers: head (dummy node), tail.
  push: CAS tail->next = new node; CAS tail = new node.
  pop:  CAS head = head->next (which is actual first data node).

  Handles concurrent pushes via tail chasing.
  Handles concurrent pops via head movement.

Memory reclamation: problematic — use hazard pointers or EBR (epoch-based reclamation).
```

**Java's ConcurrentLinkedQueue** implements Michael-Scott queue.

### Wait-Free Algorithms

**Wait-free**: Every operation completes in bounded number of steps, regardless of other threads' speed.

**Herlihy's Universal Construction** (1991): Given any sequential object with a `apply(state, op) → (state', result)` function, construct a wait-free linearizable implementation using:
- Consensus objects (CAS is consensus number ∞)
- Announce array: each thread announces its operation
- Build result via helping mechanism: threads help each other complete operations

Wait-free is theoretically satisfying but practically expensive (constant factors). Most "lock-free" production code is technically obstruction-free or lock-free (not wait-free).

**Consensus hierarchy** (Herlihy 1991):

| Object | Consensus number | What it can implement |
|--------|-----------------|----------------------|
| Read/Write registers | 1 | Single-thread coordination only |
| Test-and-Set | 2 | 2-thread wait-free |
| Fetch-and-Add | 2 | 2-thread wait-free |
| Compare-and-Swap | ∞ | n-thread wait-free |
| LL/SC | ∞ | n-thread wait-free |

CAS has infinite consensus number → single CAS can implement any wait-free n-thread data structure (via universal construction). This is why CAS is the primitive in all modern CPUs.

### Memory Reclamation in Lock-Free Code

Safe memory reclamation is the hardest problem in lock-free programming:

**Hazard Pointers** (Michael 2004):
- Before accessing pointer p, announce p in a per-thread hazard pointer slot.
- Retiring (freeing) only safe when no hazard pointer points to p.
- Scan all hazard pointers before freeing retired nodes.
- O(p·r) overhead (p = threads, r = retired nodes per round).

**Epoch-Based Reclamation (EBR)** (Fraser 2004):
- Three epochs: 0, 1, 2. Global epoch counter.
- Thread "enters" current epoch; "exits" when done.
- Advance global epoch only when all threads have exited old epochs.
- Retired nodes safe to free after epoch advances twice.
- Used in: Java garbage collector, Folly, crossbeam (Rust).

**RCU (Read-Copy-Update)**:
- Readers: no locks; just read. Periodic "quiescent state" = safe reclamation point.
- Writers: copy old structure, modify copy, atomically swap pointer.
- Free old copy after all readers have passed through quiescent state.
- Linux kernel uses RCU pervasively. User-space: liburcu.

---

## 5. Software Transactional Memory (STM)

### The Concept

```
Transactional memory: treat memory accesses like database transactions.

atomic {
  x = x + 1;   // reads x, increments, writes x
  y = y - 1;   // reads y, decrements, writes y
}

Runtime tracks reads (read set) and writes (write set).
At commit: validate read set (still current?) → if yes, publish writes atomically.
On conflict: abort and retry.
```

**Optimistic concurrency**: Assume no conflicts; handle conflicts at commit. Works well when conflicts are rare.

**Pessimistic (lock-based) transactions**: Lock every location on first access. Deadlock possible. Harder to compose.

### STM Flavors

**TL2 (Transactional Locking II)**: Global version clock. Each memory location has per-location version + lock. Read-set validated against version at commit time. Industry benchmark STM.

**DSTM (Dynamic STM)**: Object-based STM with contention management policies.

**Clojure STM**: refs + `dosync`. MVCC-based (multi-version concurrency control). Retries on conflict. `ensure` for read-only reads inside transactions.

**Haskell STM** (`Control.Concurrent.STM`): Type-safe composable transactions using `TVar`, `TMVar`, `TChan`. Retry and alternative composition (`retry`, `orElse`).

```haskell
-- Haskell STM: composable
transfer :: TVar Int -> TVar Int -> Int -> STM ()
transfer from to amount = do
  fromBalance <- readTVar from
  when (fromBalance < amount) retry   -- block until condition holds
  modifyTVar from (subtract amount)
  modifyTVar to (+ amount)

-- atomically :: STM a -> IO a
-- orElse :: STM a -> STM a -> STM a
```

**Hardware Transactional Memory (HTM)**: Intel TSX (Transactional Synchronization Extensions). Hardware support for transactional regions. Falls back to software path on conflict/overflow. Disabled on many CPUs due to speculative execution vulnerabilities.

**STM in practice**: Composability is the main advantage. Performance is 2-10x worse than fine-grained locking for common cases. Suitable when: complex invariants span multiple objects, lock ordering is difficult, composability is needed.

---

## 6. Message Passing Models

<!-- @editor[content/P2]: The CSP vs Actors section correctly identifies Go channels (CSP) and Erlang/Akka (Actors) but is missing the third major model this learner will encounter: the .NET Channel<T> API (System.Threading.Channels, introduced in .NET Core 3.0). This is the modern C# replacement for BlockingCollection<T> and the TPL Dataflow pipeline. The learner knows TPL Dataflow from Azure Data Factory internals — there is a direct bridge from Dataflow pipelines → Channel<T> + async pipelines that's missing. Also absent: the comparison between Channel<T> (bounded/unbounded, single producer/multi producer) and Go's buffered channels — they're solving the same problem with different ergonomics. -->

### CSP (Communicating Sequential Processes — Hoare 1978)

```
Processes communicate via synchronous channels (rendezvous).
No shared state. Communication IS synchronization.

Process algebra with operators:
  P ∥ Q:  parallel composition
  P ; Q:  sequential composition
  a → P:  prefix action (perform a, then P)
  P ⊓ Q:  internal choice (process chooses)
  P □ Q:  external choice (environment chooses)

Channel c!v: send v on c.
Channel c?x: receive from c into x.

CSP models: Go channels, Erlang processes (actor variant), Unix pipes.
```

**Go channels**: CSP-inspired. Buffered or unbuffered. `select` = CSP external choice.
```go
ch := make(chan int, 1)  // buffered channel, capacity 1

// Goroutine (lightweight thread, ~4KB stack, multiplexed on OS threads)
go func() { ch <- 42 }()

select {
case v := <-ch:
    fmt.Println(v)
case <-time.After(1 * time.Second):
    fmt.Println("timeout")
}
```

**Go runtime scheduler**: M:N threading. M goroutines on N OS threads. Work-stealing scheduler. Goroutines multiplex onto OS threads via GOMAXPROCS-many P (processor) structures.

### Actor Model (Hewitt-Bishop-Steiger 1973)

```
Actors: fundamental unit of computation.
  Each actor has: mailbox, behavior, local state.
  Actors communicate only by sending messages.
  On receiving message: can create new actors, send messages, change behavior.

Properties:
  - Location transparent: actor address doesn't reveal physical location
  - No shared state: actors never access each other's state directly
  - Asynchronous: send returns immediately; recipient processes later
  - Serialized per actor: each actor processes one message at a time (no per-actor races)
```

**Erlang/Elixir** (original actor language):
```erlang
% Actor = process
Pid = spawn(fun() -> loop(State) end),

% Message passing
Pid ! {request, self(), Data},

% Receive (pattern matching on mailbox)
receive
  {response, Result} -> handle(Result);
  {'EXIT', Pid, Reason} -> recover(Reason)
  after 5000 -> timeout
end

% Supervision trees: supervisors restart failed children.
% OTP: standardized patterns (gen_server, gen_statem, supervisor).
```

**Akka** (Scala/Java actor framework):
- ActorRef as opaque handle (location transparent)
- Ask pattern returns Future
- Typed Actors (Akka Typed): type-safe protocol specification

**Akka vs Go channels**:
- Go: explicit channel types, structured concurrency with goroutines
- Akka: object-oriented actors with behavior encapsulation, supervision, cluster distribution
- Both avoid shared state; actors are higher-level than channels

---

## 7. Async/Await — Cooperative Concurrency

### The Model

```
Traditional threads: OS-scheduled, preemptive, full stack per thread.
Async/await: cooperative, user-space scheduling, shared stack via continuations.

async function fetches():
  const a = await fetchA()  // returns to caller while I/O pending
  const b = await fetchB()  // again
  return a + b              // resumes after both complete

Under the hood: each await creates a continuation (rest of function after await).
The runtime runs continuations when I/O completes.
Single-threaded event loop (JS) or thread pool (C#/.NET, Python asyncio).
```

**Single-threaded event loop (JavaScript/Node.js)**:
```
Call stack + microtask queue + macrotask queue

setTimeout → macrotask queue
Promise.then → microtask queue
Process order: call stack → all microtasks → one macrotask → all microtasks → ...

async/await desugars to promise chains.
No data races (single-threaded) but cooperative: long sync operations block event loop.
```

**C# Task/async/await (.NET)**:
```csharp
// async method returns Task<T>
async Task<string> FetchDataAsync(string url) {
    // ConfigureAwait(false): don't capture synchronization context (important for libraries)
    var response = await httpClient.GetAsync(url).ConfigureAwait(false);
    return await response.Content.ReadAsStringAsync().ConfigureAwait(false);
}

// ValueTask<T>: avoid heap allocation for hot paths that often complete synchronously.
// Task.WhenAll: parallel composition of async operations.
// CancellationToken: cooperative cancellation throughout async chains.
```

<!-- @editor[bridge/P2]: The C# async/await section is correct but misses the SynchronizationContext trap that bites .NET developers most frequently: library code that calls .GetAwaiter().GetResult() or .Wait() on a Task from a context that has a SynchronizationContext (ASP.NET classic, WPF, WinForms) deadlocks because the continuation tries to resume on the captured context which is blocked waiting for the task. This is not mentioned. The ConfigureAwait(false) note is present but the *why it deadlocks without it* explanation is absent. For someone who built async pipelines in Azure Data Factory, this is a known failure mode worth documenting explicitly. -->

**Rust async/await** (zero-cost abstraction):
```rust
// Futures are lazy: nothing runs until polled by an executor.
// async fn returns impl Future<Output = T>.
// await polls the future and suspends if not ready.
// Executors: tokio (multi-threaded), async-std, smol.

async fn fetch(url: &str) -> Result<String, Error> {
    let resp = reqwest::get(url).await?;
    resp.text().await
}

// Pin<&mut Self>: futures must be pinned in memory (no moves after first poll).
// The async state machine is a generated struct containing all local variables
// across await points — zero-cost, no hidden allocation.
```

**Python asyncio**:
- Single-threaded event loop. `async def` / `await`.
- `asyncio.gather()` for concurrent tasks.
- GIL means threads don't help CPU-bound code; async helps I/O-bound.

<!-- @editor[bridge/P2]: Missing an explicit bridge from C# Task-based Parallel Library (which this learner knows deeply: Task.Run, Task.WhenAll, CancellationToken, async/await with ConfigureAwait) to structured concurrency in Swift and Kotlin. The learner knows the C# model; what's new is how Swift's `async let` / TaskGroup and Kotlin's coroutines + CoroutineScope enforce the parent-child lifetime contract at the type level (cancellation propagates, exceptions can't escape the scope). A "C# TPL vs Swift structured concurrency vs Kotlin coroutines" comparison table showing what each enforces and what it doesn't would make this section genuinely useful rather than just listing syntax. -->

### Structured Concurrency

**Problem with raw async**: fire-and-forget tasks leak; cancellation doesn't propagate; errors are lost.

**Structured concurrency**: tasks have bounded lifetime of their parent scope.

```python
# Python 3.11+ TaskGroup (PEP 654)
async with asyncio.TaskGroup() as tg:
    task1 = tg.create_task(fetch_a())
    task2 = tg.create_task(fetch_b())
# Both tasks complete (or one fails → all cancelled) before exiting block.
```

```swift
// Swift structured concurrency (Swift 5.5+)
async let imageA = downloadImage("a.jpg")
async let imageB = downloadImage("b.jpg")
let images = await [imageA, imageB]  // both start concurrently, await both
```

---

## 8. Rust Ownership and Concurrency

Rust's ownership system eliminates data races at compile time:

```
Rules:
  1. Each value has one owner at a time.
  2. Owner can lend immutable references (&T) — many simultaneous.
  3. Owner can lend one mutable reference (&mut T) — exclusive.
  4. No reference outlives its data.

Data races require: shared access + mutability + no synchronization.
Rule 3 forbids simultaneous shared mutable access → no data races.

Send:  Types safe to transfer to another thread.
Sync:  Types safe to share references across threads (&T: Send).

Arc<T>:  Atomic reference count. T: Send + Sync.
Mutex<T>: Wraps T. lock() returns MutexGuard<T> (RAII unlock).
RwLock<T>: Reader-writer lock. read() returns RwLockReadGuard.
Atomic*:  Atomic primitives (fetch_add, compare_exchange, etc.).
```

```rust
// Mutex in Rust — compiler enforces lock discipline
let data = Arc::new(Mutex::new(vec![1, 2, 3]));
let clone = Arc::clone(&data);

thread::spawn(move || {
    let mut guard = clone.lock().unwrap();  // MutexGuard
    guard.push(4);
    // guard auto-released when it drops (end of scope)
});
```

**Rayon** (data parallelism library): `par_iter()` turns sequential iterators into parallel. Work-stealing thread pool. Compile-time guarantee: `par_iter()` requires `Send`.

---

## 9. Concurrency Patterns and Pitfalls

### Common Patterns

**Producer-consumer** (bounded buffer):
```
mutex + two condition variables (not-full, not-empty).
Or: use a channel (Go, Rust mpsc, Java BlockingQueue).
```

**Work stealing** (Cilk, Go runtime, Rayon, .NET ThreadPool):
```
Each worker has a double-ended queue (deque).
Push/pop from own queue (local end).
Steal from random other worker's queue (remote end).
Local operations: mostly lock-free (CAS on index).
Stealing: acquires remote lock (rare).
Achieves near-optimal load balancing with low overhead.
```

**Readers-writer cache** (RCU pattern):
```
Read path: lock-free, just read pointer.
Write path: copy, modify, atomically swap pointer.
Reclaim old copy after all readers finish.
```

**Double-checked locking** (classic Java bug, now fixed):
```java
// WRONG (Java pre-1.5):
if (instance == null) {
    synchronized(this) {
        if (instance == null) instance = new Singleton();
    }
}

// WRONG because: new Singleton() has 3 steps:
//   1. allocate memory
//   2. initialize object
//   3. assign to instance
// Steps 2 and 3 can be reordered. Other thread sees non-null, uninitialized instance.

// CORRECT: volatile instance (Java 1.5+) prevents reordering.
private volatile Singleton instance;
```

### Common Pitfalls

**False sharing**: Two independent variables in the same 64-byte cache line. Modifications by different threads cause constant cache invalidations. Fix: pad to 64 bytes, use `__attribute__((aligned(64)))` or `@Contended` annotation (Java 8+).

**Lock granularity**: Too coarse → serialization bottleneck. Too fine → excessive overhead, deadlock risk. Profiling required.

**Priority inversion**: Low-priority thread holds lock needed by high-priority thread. Medium-priority thread preempts low-priority thread → high-priority thread stuck. Fix: priority inheritance (OS-level), lock-free algorithms, or careful priority design.

**Thread pool exhaustion**: Task submits subtask and waits for it. All pool threads doing this → deadlock (circular waiting for threads). Fix: structured concurrency, async/await, or never block pool threads.

---

## 10. Concurrency in Production Systems

| System | Concurrency model | Key detail |
|--------|-------------------|-----------|
| Linux kernel | Locks + RCU + lock-free | RCU dominant for read-heavy shared data |
| Java concurrent collections | Lock-free (CAS) | ConcurrentHashMap: lock-striped then tree per bucket |
| .NET concurrent collections | Lock-free + lock-based | ConcurrentDictionary: lock striping by key hash |
| Node.js | Single-thread event loop | No data races; long sync blocks event loop |
| Go runtime | CSP channels + goroutines | M:N scheduler, work-stealing |
| Erlang/Elixir | Actor model | Lightweight processes, OTP supervision |
| Rust async (tokio) | Green threads + async/await | Zero-cost futures, work-stealing thread pool |
| C# async/await | Task-based (TPL) | Thread pool + SynchronizationContext |
| Python asyncio | Single-thread event loop | GIL prevents true parallelism for CPU-bound |
| Kafka consumer groups | Partition-based parallelism | One partition → one consumer; no shared state |

---

## Decision Cheat Sheet

```
Problem:                                     Solution:
────────────────────────────────────────     ──────────────────────────────────────────
Short critical section, low contention       Spinlock (TTAS) or std::mutex
Long critical section, many waiters          Blocking mutex + condition variable
Readers >> writers                           RwLock (shared_mutex)
Need composable atomic multi-object ops      STM (Clojure refs, Haskell STM)
Avoid locks entirely, high read throughput   Lock-free data structure (skip list, LCRQ)
I/O-bound concurrent work                   Async/await (tokio, asyncio, .NET Tasks)
CPU-bound parallel work                      Thread pool (rayon, .NET ThreadPool, Java FJ)
Independent concurrent tasks                 Goroutines (Go) or async tasks
Message-based component isolation            Actor model (Akka, Erlang)
Distributed shared state                     CRDTs or consensus-based log
Fine-grained parallel list/tree traversal    RCU (Linux), hazard pointers, EBR
Guarantee no data races at compile time      Rust ownership + Arc<Mutex<T>>

Consistency model needed?
  One operation atomic on one object         CAS / fetch_add (hardware atomic)
  Multiple objects atomic                    STM or fine-grained locking with order
  One thread safe to share data to another   std::atomic + release/acquire
  Any order, just no corruption              Relaxed atomics (counters, flags)
```

---

## Common Confusion Points

**Atomicity ≠ memory ordering**: An atomic operation ensures no torn reads/writes. But without ordering constraints, the CPU may reorder it relative to other operations. Use `memory_order_acquire/release` or `volatile` as appropriate.

**Volatile is not enough for synchronization** (Java, C#): `volatile` ensures visibility and prevents reordering with other volatile accesses. Does NOT make compound operations (check-then-act, read-modify-write) atomic. Use `synchronized` / `lock` or atomic classes.

**`volatile` in C/C++ ≠ `volatile` in Java**: C/C++ `volatile` prevents compiler reordering but does NOT provide memory ordering between threads (no CPU fence). Java/C# `volatile` provides sequential consistency for that variable. In C++, use `std::atomic` with appropriate `memory_order`.

**Lock-free ≠ wait-free**: Lock-free guarantees system-wide progress (some thread completes in finite steps). Wait-free guarantees individual progress (every thread completes in bounded steps). All wait-free algorithms are lock-free; not vice versa.

**CAS loops can livelock** under high contention: all threads fail CAS, all retry. In practice, exponential backoff or CLH/MCS queue locks solve this. Java's `LongAdder` stripes across cells to reduce CAS contention.

**Thread.sleep() ≠ fair waiting**: `sleep` relinquishes CPU but does not guarantee another thread runs. Real scheduling depends on OS. Use condition variables, semaphores, or channels for coordination.

**async/await does not automatically parallelize**: `await` suspends the current task and resumes later; it does not start a parallel task. For parallelism, explicitly create tasks: `Task.WhenAll()`, `asyncio.gather()`, `join!()`.

**Go channels are not always the right tool**: For simple mutual exclusion, `sync.Mutex` is faster than a channel with 1 capacity. Channels shine for sequential communication and coordination. Don't use channels as a lock.
