---
maxim_schema: maxim.frontmatter.v1
id: maxim:operations-research:queuing-theory
kind: guide
module: operations-research
section: operations-research
title: Queuing Theory - Little's Law, M/M/1, M/M/c, Jackson Networks
status: source-custody
source_custody: partial
current_path: operations-research/06-QUEUING-THEORY.md
canonical_path: operations-research/06-QUEUING-THEORY.md
backsource_ids: [proof-backfill:operations-research:06-queuing-theory, git-history:operations-research:06-queuing-theory]
concepts: [queuing theory, Little's law, M/M/1, M/M/c, Kendall notation, Jackson networks]
root_concepts: [queuing theory]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Queuing Theory — Little's Law, M/M/1, M/M/c, and Jackson Networks

## The Big Picture

Queuing theory predicts **waiting** in systems where work arrives randomly and is served at finite rate. Its power is that a few parameters — arrival rate $\lambda$, service rate $\mu$, number of servers $c$ — determine the entire steady-state behavior, and one law (**Little's Law**) holds with *almost no assumptions*. The defining lesson: as utilization $\rho \to 1$, delay does not grow linearly — it **explodes hyperbolically**.

```
+----------------------------------------------------------------------+
|                 QUEUING THEORY: THE WHOLE PICTURE                     |
|                                                                      |
|   arrivals          QUEUE              SERVER(S)         departures   |
|   rate lambda  -->  o o o o o  -->   [ S ][ S ]...   -->             |
|                     (waiting)        c servers, rate mu each         |
|                                                                      |
|   KENDALL NOTATION:  A / S / c / K / N / D                          |
|                      |   |   |   |   |   |                          |
|              arrival_|   |   |   |   |   |_discipline (FCFS/LCFS/PS) |
|              service____ |   |   |   |__population size              |
|              servers________ |   |__system capacity (buffer)        |
|                                                                      |
|   LITTLE'S LAW (the universal invariant):   L = lambda * W          |
|     L = avg # in system,  W = avg time in system,  lambda = arrival  |
|                                                                      |
|   THE CONGESTION CLIFF (M/M/1):   W = 1 / (mu - lambda)             |
|     delay                                                            |
|       |                          /|  <- blows up as rho -> 1         |
|       |                        _/                                    |
|       |__________----------''''                                     |
|       +-------------------------------- utilization rho = lambda/mu  |
|       0                              1                               |
+----------------------------------------------------------------------+
```

**The systems-leader takeaway up front**: a server at 90% utilization has roughly *10x* the average queue of one at 50% — and 99% has ~100x. Capacity planning is governed by this nonlinearity, not by the mean load.

---

## Layer 1: Kendall Notation and the Vocabulary

A queue is specified by **A/S/c/K/N/D** (last three often omitted, defaulting to $\infty/\infty/$FCFS):

```
+----------------------------------------------------------------------+
|  SYMBOL   MEANING                  COMMON VALUES                     |
|  ------   -------                  -------------                     |
|  A        arrival process         M (Markov/Poisson, memoryless)    |
|                                    D (deterministic), G (general)    |
|  S        service distribution    M (exponential), D, G             |
|  c        number of servers       1, c, infinity                    |
|  K        system capacity (buffer)default infinity (unbounded)      |
|  N        calling population       default infinity                 |
|  D        queue discipline         FCFS, LCFS, PS (processor share), |
|                                    priority                          |
+----------------------------------------------------------------------+
```

"M" stands for **Markovian/memoryless** — the exponential interarrival or service distribution, whose memoryless property ($P(T > s+t \mid T > s) = P(T>t)$) makes the system a continuous-time Markov chain (CTMC) and yields closed forms.

| Notation | Means |
|----------|-------|
| **M/M/1** | Poisson arrivals, exponential service, one server, infinite buffer |
| **M/M/c** | same, $c$ parallel servers (a call center / thread pool) |
| **M/M/c/K** | $c$ servers, finite buffer $K$ (blocking when full) |
| **M/M/c/c** | $c$ servers, no waiting room — **Erlang B** (loss system, trunk lines) |
| **M/G/1** | general service distribution — **Pollaczek–Khinchine** formula |
| **G/G/1** | general arrivals and service — approximations only |

**Key parameters and symbols (memorize):**

| Symbol | Meaning |
|--------|---------|
| $\lambda$ | mean arrival rate |
| $\mu$ | mean service rate per server |
| $\rho$ | utilization (traffic intensity) $= \lambda / (c\mu)$ |
| $L$ / $L_q$ | mean number in system / in queue |
| $W$ / $W_q$ | mean time in system / in queue (waiting) |

---

## Layer 2: Little's Law — The Universal Invariant

**Theorem (Little's Law).** For any stable queuing system in steady state,
$$L = \lambda\, W,$$
where $L$ is the long-run average number of items in the system, $\lambda$ the long-run average arrival rate, and $W$ the long-run average time an item spends in the system.

```
   L = lambda * W

   (items in system) = (arrival rate) * (time per item)

   HYPOTHESES (remarkably weak):
   - the system is stable (a long-run steady state exists)
   - arrivals are conserved (every arrival eventually departs)
   NO assumption about arrival distribution, service distribution,
   number of servers, or queue discipline. It is essentially a
   conservation/accounting identity.
```

Applies to **any subsystem** by choosing the boundary:

| Apply Little's Law to... | Get |
|--------------------------|-----|
| Whole system | $L = \lambda W$ |
| Queue only (exclude service) | $L_q = \lambda W_q$ |
| Servers only | (busy servers) $= \lambda / \mu = c\rho$ |

**Bridge — old world → systems**: this is the same identity behind **throughput × latency = concurrency** in performance engineering. If your service handles $\lambda$ = 1000 req/s and each takes $W$ = 50 ms in the system, then $L = 1000 \times 0.05 = 50$ requests are in flight on average. Little's Law is why you size connection pools and in-flight limits this way. It needs *no* model of the internals — pure conservation.

---

## Layer 3: The M/M/1 Queue Solved Exactly

M/M/1 is a birth–death CTMC: state $n$ = number in system; birth rate $\lambda$ (arrival), death rate $\mu$ (service completion).

```
   BIRTH-DEATH CHAIN (M/M/1):

         lambda    lambda    lambda    lambda
      (0) ---> (1) ---> (2) ---> (3) ---> ...
          <---     <---     <---     <---
          mu       mu       mu       mu

   Balance equations give p_n = (1 - rho) rho^n,  rho = lambda/mu < 1.
   (a geometric distribution of the number in system)
```

**Steady-state results (M/M/1), valid only when $\rho = \lambda/\mu < 1$:**

```
+----------------------------------------------------------------------+
|  Utilization:           rho = lambda / mu          (must be < 1)     |
|  P(n in system):        p_n = (1 - rho) rho^n                        |
|  P(system empty):       p_0 = 1 - rho                               |
|                                                                      |
|  L  (mean in system):   L  = rho / (1 - rho)                        |
|  Lq (mean in queue):    Lq = rho^2 / (1 - rho)                      |
|  W  (mean time in sys): W  = 1 / (mu - lambda)                      |
|  Wq (mean wait):        Wq = rho / (mu - lambda) = lambda/(mu(mu-lam))|
|                                                                      |
|  CHECK via Little:  L = lambda W,  Lq = lambda Wq    (consistent)   |
+----------------------------------------------------------------------+
```

**The congestion cliff, made quantitative:**

| $\rho$ | $L = \rho/(1-\rho)$ | Mean # in system |
|--------|---------------------|------------------|
| 0.50 | 1.0 | 1 |
| 0.80 | 4.0 | 4 |
| 0.90 | 9.0 | 9 |
| 0.95 | 19.0 | 19 |
| 0.99 | 99.0 | 99 |

The $1/(1-\rho)$ factor is the entire story of capacity planning: **the last 10% of utilization costs more than the first 80%.** This is why high-reliability systems run at moderate utilization — headroom is delay insurance.

---

## Layer 4: M/M/c — Multiple Servers (the real model)

A call center, thread pool, or server farm with $c$ identical parallel servers, one shared queue. Now $\rho = \lambda/(c\mu)$ must be $< 1$ for stability.

The key quantity is the **Erlang C** probability — the chance an arriving job must **wait** (all servers busy):

```
   ERLANG C:  P(wait) = C(c, a) where a = lambda/mu (offered load, Erlangs)

                  ( a^c / c! ) * ( 1 / (1 - rho) )
   P(wait) = ------------------------------------------------
              sum_{n=0}^{c-1} a^n/n!  +  (a^c/c!)(1/(1-rho))

   with rho = a/c = lambda/(c mu).
```

```
   Then:
   Wq (mean wait in queue) = P(wait) / (c mu - lambda)
   W  = Wq + 1/mu
   Lq = lambda * Wq          (Little)
   L  = Lq + a               (a = lambda/mu = avg busy servers)
```

**Economy of scale (the pooling effect)** — a crucial, counterintuitive result:

```
   Two separate M/M/1 queues (split traffic)
        vs.
   One M/M/2 queue (pooled traffic, same total capacity)

   THE POOLED M/M/2 HAS LOWER MEAN WAIT.

   Reason: in split queues a server can sit idle while the OTHER
   queue has a backlog. Pooling lets any free server take any job.
   This is why shared thread pools / shared queues beat per-shard
   queues, and why consolidating call-center lines reduces wait.
```

**Erlang B vs. Erlang C** (don't confuse them):

| Formula | System | Question answered |
|---------|--------|-------------------|
| **Erlang B** | M/M/c/c (no waiting room) | Probability a call is **blocked** (lost) — trunk sizing |
| **Erlang C** | M/M/c (infinite queue) | Probability a call must **wait** — staffing with a queue |

---

## Layer 5: Beyond Markovian — M/G/1 and Pollaczek–Khinchine

When service times are **not** exponential, M/G/1 still has a closed form for the mean wait via the **Pollaczek–Khinchine (P–K) formula**:

```
   POLLACZEK-KHINCHINE (M/G/1 mean wait in queue):

           lambda * E[S^2]              rho^2 (1 + C_s^2)
   Wq  =  -----------------    =    --------------------------
           2 (1 - rho)                  2 lambda (1 - rho)

   where E[S^2] = second moment of service time,
         rho = lambda * E[S],  C_s^2 = Var(S)/E[S]^2 (coeff. of variation^2).
```

**The decisive insight**: $W_q$ depends on the **variance** of service time, not just its mean. With the mean fixed:
- **Deterministic service** (M/D/1, $C_s^2 = 0$): wait is *halved* versus exponential.
- **Exponential service** (M/M/1, $C_s^2 = 1$): the baseline.
- **High-variance service** (heavy tails, $C_s^2 \gg 1$): wait blows up.

```
   SAME mean service time, different VARIANCE:

   M/D/1  (C_s^2 = 0):   Wq = rho^2 / (2 lambda (1-rho))      [smallest]
   M/M/1  (C_s^2 = 1):   Wq = rho   / (mu (1-rho)) = baseline
   M/G/1, heavy tail :   Wq grows with C_s^2                  [largest]
```

This is why **reducing variability** (consistent request sizes, capping tail latency, smoothing batch sizes) cuts queueing delay even without adding capacity — a direct, actionable consequence for tail-latency engineering.

---

## Layer 6: Jackson Networks — Queues in Series and Parallel

Real systems are **networks** of queues (microservices, assembly lines, packet routers). A **Jackson network** is the tractable case.

```
   AN OPEN JACKSON NETWORK:

   ext arrivals --> [Q1] --p12--> [Q2] --> exit
        |             |               ^
        |             p13             |
        v             v               |
       [Q3] ---------+---------------+
   Each node i: Poisson external arrivals, exponential service, FCFS,
   routing probability p_ij from i to j.
```

**Theorem (Jackson 1957 — product form).** In an open Jackson network where each node $i$ is an M/M/$c_i$ queue, with total arrival rate $\lambda_i$ solving the **traffic equations**
$$\lambda_i = r_i + \sum_j \lambda_j p_{ji}$$
(external rate $r_i$ plus internal routing), the steady-state distribution **factorizes**:
$$P(n_1, \dots, n_K) = \prod_{i=1}^K p_i(n_i),$$
i.e., each node behaves *as if* it were an independent M/M/$c_i$ queue with arrival rate $\lambda_i$.

```
   PRODUCT FORM: joint distribution = product of per-node marginals.

   P(n1, n2, ..., nK) = p1(n1) * p2(n2) * ... * pK(nK)

   Each node analyzed in ISOLATION with its computed lambda_i.
   (Remarkable, because the internal arrival streams are NOT actually
    Poisson — yet the steady-state marginals behave as if they were.)
```

This product-form result lets you analyze a large network node-by-node. **Closed** Jackson networks (fixed population, no external arrivals — e.g., a fixed thread pool cycling through stages) have an analogous product form computed via the **convolution / mean-value analysis (MVA)** algorithm.

**Caveats (state them):** product form requires exponential service (or specific quasi-reversible disciplines like processor-sharing), probabilistic (Markovian) routing, and unbounded buffers. Add blocking, deterministic service, or finite buffers and the product form generally breaks — you fall back to simulation (file 08) or approximations (QNA, diffusion).

---

## Old World → Queuing Bridges

| You already know | Queuing analogue |
|------------------|------------------|
| throughput × latency = concurrency | Little's Law $L = \lambda W$ |
| Connection pool / thread pool sizing | M/M/c server count $c$; Erlang C wait probability |
| Sharded queues vs. one shared queue | M/M/1 split vs. M/M/c pooling (pooling wins) |
| Tail latency from request-size variance | Pollaczek–Khinchine: $W_q \propto C_s^2$ |
| Autoscaling target utilization (~70%) | Avoiding the $1/(1-\rho)$ congestion cliff |
| Microservice call graph capacity | Jackson network, traffic equations |
| Load-shedding / admission control | M/M/c/K finite buffer, Erlang B blocking |
| Backpressure | Stability condition $\rho < 1$ |

The mental upgrade: don't size systems to the *mean* load. Size to keep $\rho$ off the cliff and to **reduce variance**, because both the $1/(1-\rho)$ utilization term and the $C_s^2$ variability term multiply your delay.

---

## Decision Cheat Sheet

| Question | Tool |
|----------|------|
| Average concurrency from rate and latency | Little's Law $L = \lambda W$ |
| Wait time, single server | M/M/1: $W = 1/(\mu - \lambda)$ |
| How many servers for an SLA | M/M/c + Erlang C ($P(\text{wait})$) |
| Trunk/line sizing with no queue (blocking) | M/M/c/c + Erlang B |
| Effect of service-time variance | Pollaczek–Khinchine ($M/G/1$) |
| Pool vs. shard a queue | Compare M/M/c (pooled) to split M/M/1 — pool wins |
| Multi-stage / microservice network | Jackson network, traffic equations, product form |
| Non-Markovian, finite buffers, blocking | Drop to simulation (file 08) |
| Target utilization for headroom | Keep $\rho$ well below 1 (the cliff) |

---

## Common Confusion Points

### "Does Little's Law need Poisson arrivals?"

**No.** Little's Law ($L = \lambda W$) holds for essentially *any* stable system — any arrival process, any service distribution, any number of servers, any discipline. It's a conservation identity, not a stochastic result. The Poisson/exponential assumptions are only needed for the *closed-form* M/M/1, M/M/c results, not for Little's Law itself.

### "Why does delay explode near $\rho = 1$ instead of growing smoothly?"

Because of the $1/(1-\rho)$ factor in $L$ and $W$. At $\rho = 0.9$, the system is empty 10% of the time, so any backlog takes a long time to clear; randomness creates bursts the server can barely keep up with. As $\rho \to 1$ the "drain rate" of excess work $\to 0$, so transient backlogs persist longer and longer. It's a pole at $\rho = 1$, not a linear ramp.

### "$\rho$ is utilization — so $\rho < 1$ just means under 100%?"

For stability you need $\rho = \lambda/(c\mu) < 1$ **strictly**. At exactly $\rho = 1$ the queue is unstable (grows without bound in expectation) even though the server isn't "overloaded" on average — randomness guarantees backlog accumulates faster than it clears. You cannot run a stochastic queue at 100% utilization and expect bounded delay.

### "Erlang B or Erlang C?"

**Erlang B** = no waiting room; excess arrivals are *blocked/lost* (loss system, M/M/c/c) — answers "what fraction of calls get a busy signal?" **Erlang C** = infinite queue; excess arrivals *wait* (M/M/c) — answers "what fraction of calls must wait, and how long?" Using the wrong one over- or under-provisions. Call centers with hold queues use Erlang C; circuit/trunk sizing uses Erlang B.

### "Why does pooling beat splitting if total capacity is the same?"

Statistical multiplexing. In split queues, one server can idle while the other's queue is backed up — that idle capacity is wasted. A pooled queue lets any free server grab any waiting job, eliminating the "idle-while-others-wait" loss. The math: M/M/2 has strictly lower $W_q$ than two M/M/1 queues each at half the load. This is the queuing-theory justification for shared resource pools.

### "Jackson networks have Poisson internal flows, right?"

A subtle trap. The internal arrival streams (departures from one queue feeding another) are generally **not** Poisson. Yet Jackson's theorem proves the **steady-state marginal** at each node behaves *exactly as if* it were an independent M/M/c queue with the solved arrival rate $\lambda_i$ — the product form holds even though the streams aren't truly Poisson. This is what makes the theorem surprising and useful: analyze each node in isolation despite the dependence.
