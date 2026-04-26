# Concurrency — Engineering Reference

## The Big Picture

Concurrency correctness is hard because the interleaving of operations from multiple threads creates an exponential space of possible executions. This guide covers the formal foundations (Herlihy-Shavit territory), hardware memory models, practical synchronization primitives, and the modern concurrency abstractions used in production — from lock-free data structures to async/await.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  CONCURRENCY LANDSCAPE                                                      │
│                                                                             │
│  Correctness Properties          Progress Properties                        │
│  ───────────────────────────     ─────────────────────────────              │
│  Safety: nothing bad happens     Deadlock-freedom: some thread progresses   │
│  Linearizability: atomic ops     Starvation-freedom: every thread progresses │
│  Sequential consistency          Lock-freedom: some op completes in O(steps) │
│  Serializability (transactions)  Wait-freedom: every op completes in O(steps)│
│                                                                             │
│  Synchronization Models         Hardware Concerns                           │
│  ───────────────────────────     ──────────────────────────────             │
│  Mutex / monitors                Memory ordering (TSO, PSO, SC)             │
│  Reader-writer locks             Cache coherence (MESI protocol)            │
│  Lock-free (CAS, LL/SC)          False sharing, cache line contention       │
│  Wait-free (universal construction) Memory barriers / fences                │
│  STM (transactional memory)      ABA problem                                │
│  Message passing (CSP, Actors)                                              │
│  Async/await (cooperative)                                                  │
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
  │                  L3 cache (shared)              │
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

### Mutex Reference

| Algorithm / Primitive | What it demonstrates | Production use |
|----------------------|---------------------|----------------|
| Dekker's algorithm | First software mutex without hardware support; uses shared memory + turn variable | Never — requires memory barriers; hardware atomics are available |
| Peterson's algorithm | Two-thread mutex with acquire/release semantics; clean correctness proof | Never — two-thread only; use OS mutex |
| TAS (Test-and-Set) | Simplest spinlock; CAS on a single byte | Rarely — causes cache line invalidation storm under contention |
| TTAS (Test-and-Test-and-Set) | Spin on regular read (MESI S state); attempt TAS only when lock looks free | Low-contention spinlocks; reduces coherence traffic vs TAS |
| CLH / MCS queue lock | Fair queuing; each waiter spins on its own cache line | Linux kernel rwlock, Java AbstractQueuedSynchronizer (AQS) |
| OS blocking mutex | Kernel-assisted sleep/wake; ~1–5 μs context switch | Standard choice for long critical sections |

### CLH / MCS Queue Locks

CLH (Craig-Landin-Hagersten) and MCS (Mellor-Crummey-Scott) are the production-grade fair queuing mutexes. The key insight: each thread spins on its own node's flag, not on a shared variable — so lock release doesn't broadcast a cache invalidation to all waiters simultaneously (the thundering herd problem with TAS/TTAS).

```
MCS queue structure:
  Each thread allocates a QNode: { volatile bool locked; QNode* next; }
  Global tail pointer (atomic).

  Acquire:
    qnode.locked = true; qnode.next = null
    prev = fetch_and_store(tail, qnode)    // atomic swap
    if prev != null:
      prev.next = qnode
      while qnode.locked: spin            // spin on OWN node's field

  Release:
    if qnode.next == null:
      if CAS(tail, qnode, null): return   // no waiters
      while qnode.next == null: spin      // wait for enqueuing thread
    qnode.next.locked = false             // hand lock to successor

Each waiter spins on its own cache line (private to that thread).
Lock release touches exactly ONE other cache line (the successor's).
No broadcast invalidation storm.
```

CLH is the implicit version (predecessor's node, not own). Java's `AbstractQueuedSynchronizer` (the backing class for `ReentrantLock`, `Semaphore`, `CountDownLatch`) implements a CLH-variant. Linux kernel's `rwlock` uses MCS for the write path.

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

**Four Coffman conditions** — all must hold simultaneously for deadlock:

| Condition | Break it by |
|-----------|-------------|
| Mutual exclusion | Use lock-free data structures (atomics, MPSC queues) |
| Hold and wait | Acquire all locks atomically (std::lock, Monitor.TryEnter with timeout) |
| No preemption | Lock timeouts; tryLock patterns |
| Circular wait | Global lock ordering — always acquire in consistent order |

**Lock ordering** (canonical production approach): Define a global total order on locks (by memory address, by assigned ID, by resource hierarchy). Every code path acquires locks in that order. Circular wait becomes impossible.

```csharp
// C# — acquire two locks without deadlock
// std::lock equivalent: acquire both or neither, retry internally
lock (LockOrderer.First(lockA, lockB))   // order by address or ID
{
    lock (LockOrderer.Second(lockA, lockB))
    {
        // safe
    }
}

// Or use Monitor.TryEnter with timeout:
if (Monitor.TryEnter(lockA, TimeSpan.FromMilliseconds(100)))
{
    try {
        if (Monitor.TryEnter(lockB, TimeSpan.FromMilliseconds(100)))
        {
            try { /* critical section */ }
            finally { Monitor.Exit(lockB); }
        }
    }
    finally { Monitor.Exit(lockA); }
}
```

**C++ std::lock**: Acquires multiple mutexes without deadlock using a deadlock-avoidance algorithm (tries, backs off, retries in different order). `std::scoped_lock(m1, m2)` in C++17.

**Lock-free elimination**: The best deadlock prevention is removing the lock. Use `Interlocked.Increment` for counters, MPSC (multi-producer single-consumer) queues for work distribution — no lock, no deadlock.

**Banker's algorithm**: O(n²) per allocation decision; requires knowing maximum resource demands in advance. Textbook concept; unused in production OS or databases.

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

### System.Threading.Channels (.NET)

`System.Threading.Channels` (added in .NET Core 3.0) is the modern C# replacement for `BlockingCollection<T>` and TPL Dataflow pipelines for producer/consumer work. It's the .NET equivalent of Go's buffered channels: typed, async-first, and supports back-pressure.

```csharp
// Bounded channel — back-pressure when full
var channel = Channel.CreateBounded<WorkItem>(new BoundedChannelOptions(capacity: 100)
{
    FullMode = BoundedChannelFullMode.Wait  // or DropOldest, DropNewest, DropWrite
});

ChannelWriter<WorkItem> writer = channel.Writer;
ChannelReader<WorkItem> reader = channel.Reader;

// Producer (async — awaits when channel is full)
await writer.WriteAsync(new WorkItem(...));
writer.Complete();  // signal no more items

// Consumer (async — awaits when channel is empty)
await foreach (var item in reader.ReadAllAsync())
{
    await ProcessAsync(item);
}
```

**Unbounded channel**: `Channel.CreateUnbounded<T>()` — no back-pressure; producer never blocks. Use only when producer rate is bounded by other constraints.

**Bridge to Go channels**:

| Feature | Go channel | .NET Channel<T> |
|---------|-----------|-----------------|
| Buffered | `make(chan T, n)` | `Channel.CreateBounded<T>(n)` |
| Unbuffered | `make(chan T)` | `Channel.CreateUnbounded<T>()` with `SingleProducerSingleConsumer` option |
| Select / multiplex | `select { case v := <-ch: }` | No direct equivalent; use `Task.WhenAny` |
| Close / completion | `close(ch)` | `writer.Complete()` |
| Async consumer | Range over channel in goroutine | `await foreach` + `ReadAllAsync()` |
| Back-pressure | Goroutine blocks on send | `await WriteAsync()` suspends producer |

**Migration path from BlockingCollection**: `BlockingCollection<T>` blocks threads (synchronous); `Channel<T>` suspends tasks (async). For Azure Data Factory-style pipeline stages (transform → validate → persist), `Channel<T>` + async pipeline eliminates the dedicated blocking threads that TPL Dataflow required.

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

### SynchronizationContext and the Deadlock Trap

The most common C# async failure mode, and the reason `ConfigureAwait(false)` exists.

**How `SynchronizationContext` works**: In ASP.NET classic (not Core), WinForms, and WPF, a `SynchronizationContext` is installed on the thread. When you `await` a task, the runtime captures the current context. When the task completes, the continuation is **scheduled back onto that captured context** — meaning it needs the original thread to run.

**The deadlock**:
```csharp
// WinForms button click handler (runs on UI thread, which has a SynchronizationContext)
private void Button_Click(object sender, EventArgs e)
{
    // .Result blocks the UI thread waiting for FetchDataAsync to complete.
    var data = FetchDataAsync().Result;   // DEADLOCK
    label.Text = data;
}

async Task<string> FetchDataAsync()
{
    // await captures the UI thread's SynchronizationContext.
    // When GetAsync completes, the continuation tries to resume on the UI thread.
    // But the UI thread is blocked in .Result above, waiting for this method.
    // Neither can proceed. Deadlock.
    var response = await httpClient.GetAsync("https://api.example.com/data");
    return await response.Content.ReadAsStringAsync();
}
```

**Why `ConfigureAwait(false)` fixes it**:
```csharp
async Task<string> FetchDataAsync()
{
    // ConfigureAwait(false): do NOT capture the current SynchronizationContext.
    // Continuation resumes on a thread pool thread instead of the UI thread.
    // The UI thread (blocked in .Result) is no longer needed for the continuation.
    var response = await httpClient.GetAsync("https://...").ConfigureAwait(false);
    return await response.Content.ReadAsStringAsync().ConfigureAwait(false);
}
```

**Rules**:
1. **Library code**: always use `ConfigureAwait(false)`. Libraries don't own the `SynchronizationContext`; they shouldn't capture it.
2. **Application code** (event handlers, controller actions, top-level tasks): `ConfigureAwait(false)` is optional — you typically want to resume on the original context (UI thread for WinForms, request context for ASP.NET classic).
3. **ASP.NET Core**: there is no `SynchronizationContext`; `ConfigureAwait(false)` has no effect but is harmless. Many teams still use it for library portability.
4. **The real fix**: don't block async code with `.Result` or `.GetAwaiter().GetResult()`. If you're in an async method, await the task. If you're in synchronous code that calls async code, the method should be async all the way up (async all the way).

**`GetAwaiter().GetResult()` vs `.Result`**: Both block. `.Result` wraps exceptions in `AggregateException`; `.GetAwaiter().GetResult()` rethrows the original exception type. Neither is safe from a `SynchronizationContext` that owns the continuation thread.

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

### Structured Concurrency

**Problem with raw async**: fire-and-forget tasks leak; cancellation doesn't propagate; errors are lost.

**Structured concurrency**: tasks have bounded lifetime of their parent scope. The analogy to structured programming is exact: structured programming replaced goto with blocks (code cannot jump out of a block's scope); structured concurrency replaces fire-and-forget with task scopes (a spawned task cannot outlive its enclosing scope).

| Model | Language | What's enforced | C# equivalent |
|-------|----------|-----------------|---------------|
| `Task.Run()` unstructured | C# | Nothing — fire-and-forget is possible; exceptions can be lost | — |
| `async Task` method | C# | Caller must `await` to observe result; exceptions propagate on await | — |
| `coroutineScope { }` | Kotlin | All child coroutines complete before scope exits; cancellation propagates | No direct equivalent (`TaskGroup` is closest) |
| `async let` + `withTaskGroup` | Swift | Child tasks scoped to enclosing async block; cancellation propagates on throw | — |
| `TaskGroup` (Python 3.11+, PEP 654) | Python | All tasks complete before `async with` block exits; first exception cancels rest | — |
| Nursery (Trio) | Python | Child tasks cannot outlive nursery; exception from any child cancels all | — |

```python
# Python 3.11+ TaskGroup (PEP 654) — closest to structured concurrency in Python
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

```csharp
// C# approximation with Task.WhenAll — not truly structured
// (tasks start before WhenAll, exceptions may be lost if not awaited carefully)
var t1 = FetchA();
var t2 = FetchB();
var results = await Task.WhenAll(t1, t2);
// If t1 throws before WhenAll: t2 is still running, exception propagation
// depends on whether you awaited t1 separately. Less safe than TaskGroup.
```

The C# gap: `Task.WhenAll` is not truly structured. A spawned `Task.Run` that throws and is never awaited silently swallows the exception (it goes to `TaskScheduler.UnobservedTaskException`). Kotlin's `coroutineScope` and Python's `TaskGroup` make this impossible by enforcing scope.

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
Or: use a channel (Go, Rust mpsc, Java BlockingQueue, .NET Channel<T>).
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
| .NET Channel<T> | Lock-free MPSC/SPSC queue | Async producer/consumer; replaces BlockingCollection |
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
Fair queuing under high contention           CLH/MCS queue lock (Java ReentrantLock/AQS)
Readers >> writers                           RwLock (shared_mutex)
Need composable atomic multi-object ops      STM (Clojure refs, Haskell STM)
Avoid locks entirely, high read throughput   Lock-free data structure (skip list, LCRQ)
I/O-bound concurrent work                   Async/await (tokio, asyncio, .NET Tasks)
CPU-bound parallel work                      Thread pool (rayon, .NET ThreadPool, Java FJ)
Independent concurrent tasks                 Goroutines (Go) or async tasks
Message-based component isolation            Actor model (Akka, Erlang)
Producer/consumer pipeline in C#            System.Threading.Channels (Channel<T>)
Distributed shared state                     CRDTs or consensus-based log
Fine-grained parallel list/tree traversal    RCU (Linux), hazard pointers, EBR
Guarantee no data races at compile time      Rust ownership + Arc<Mutex<T>>
Child tasks must not outlive parent scope    Structured concurrency (Kotlin coroutineScope,
                                             Swift TaskGroup, Python TaskGroup)

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

**ConfigureAwait(false) is for libraries, not top-level app code**: Library methods should always use it to avoid capturing the caller's SynchronizationContext. Application code (UI event handlers, controller actions) often wants the context captured — that's what brings the continuation back to the UI thread or request context after the await.
