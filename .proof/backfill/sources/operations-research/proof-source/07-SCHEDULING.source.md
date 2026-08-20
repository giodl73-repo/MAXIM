---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "07-SCHEDULING.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:operations-research:scheduling
kind: guide
module: operations-research
section: operations-research
title: Scheduling - Job-Shop, Critical Path/PERT, List Scheduling, Approximation
status: source-custody
source_custody: partial
current_path: operations-research/07-SCHEDULING.md
canonical_path: operations-research/07-SCHEDULING.md
backsource_ids: [proof-backfill:operations-research:07-scheduling, git-history:operations-research:07-scheduling]
concepts: [scheduling, job-shop, critical path, PERT, list scheduling, approximation algorithms]
root_concepts: [scheduling]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Scheduling — Job-Shop, Critical Path, List Scheduling, and Approximation Bounds

## The Big Picture

Scheduling assigns **jobs to machines over time** to optimize an objective (finish fast, hit deadlines, balance load). The field splits sharply: a handful of problems have elegant **polynomial optimal rules** (single-machine sequencing, critical path), while most multi-machine problems are **NP-hard** and we settle for **approximation algorithms with provable ratio bounds**. The deliverable is often not the optimal schedule but a *guarantee* — "this greedy list schedule is within a factor 2 of optimal."

```
+----------------------------------------------------------------------+
|                 SCHEDULING: THE WHOLE PICTURE                        |
|                                                                      |
|   alpha | beta | gamma   <-- the 3-field classification             |
|     |      |      |                                                   |
|  machine_| job  |_objective (Cmax makespan, sum C_j, sum w_j C_j,   |
|  environ. |constraints     Lmax lateness, ...)                       |
|  (1, P, F,|(release dates,                                           |
|   J, O,...)| precedence, ...)                                        |
|                                                                      |
|   POLYNOMIAL (exact rules)        NP-HARD (approximate)             |
|   ------------------------        --------------------              |
|   1 || sum C_j   -> SPT           P || Cmax  (load balancing)       |
|   1 || Lmax      -> EDD           J || Cmax  (job-shop)             |
|   critical path  -> longest path  flow shop F>=3                     |
|                    in a DAG                                          |
|                                                                      |
|   GREEDY LIST SCHEDULING (Graham): always within (2 - 1/m) of opt   |
+----------------------------------------------------------------------+
```

**The conceptual spine**: scheduling is where combinatorial optimization meets *guarantees*. When you can't solve optimally, you bound. The bounds (factor 2, factor 4/3, PTAS) are the real intellectual content.

---

## Layer 1: The Three-Field Classification ($\alpha\,|\,\beta\,|\,\gamma$)

Graham's notation classifies every deterministic scheduling problem:

```
+----------------------------------------------------------------------+
|  alpha (machine environment)                                        |
|    1     single machine                                             |
|    P     identical parallel machines                                |
|    Q     uniform (different speeds)                                 |
|    R     unrelated parallel machines                                |
|    F     flow shop (all jobs same machine order)                    |
|    J     job shop (each job its own machine order)                  |
|    O     open shop (order free)                                     |
|                                                                      |
|  beta (job characteristics / constraints)                           |
|    r_j   release dates       prec    precedence constraints         |
|    d_j   due dates           pmtn    preemption allowed             |
|    p_j=1 unit processing                                            |
|                                                                      |
|  gamma (objective to minimize)                                      |
|    Cmax       makespan (max completion time) -- finish everything   |
|    sum C_j    total completion (mean flow time)                    |
|    sum w_j C_j weighted completion                                  |
|    Lmax       max lateness                                          |
|    sum U_j    number of late jobs                                  |
+----------------------------------------------------------------------+
```

Examples read like a formula:
- $1\,||\,\sum C_j$ — one machine, no constraints, minimize total completion time.
- $P\,||\,C_{max}$ — identical parallel machines, minimize makespan (load balancing).
- $J\,||\,C_{max}$ — job shop, minimize makespan (the classic hard problem).

This taxonomy matters because tractability flips dramatically across cells: $1\,||\,\sum C_j$ is trivially polynomial; $1\,|\,\text{prec}\,|\,\sum w_j C_j$ is NP-hard.

---

## Layer 2: Single-Machine — The Polynomial Optimal Rules

On one machine, several objectives have provably optimal **greedy sequencing rules**:

```
+----------------------------------------------------------------------+
|  PROBLEM            OPTIMAL RULE                  WHY                 |
|  -------            ------------                  ---                 |
|  1 || sum C_j       SPT: Shortest Processing      short jobs first    |
|                     Time first                    minimize the wait   |
|                                                   they impose on rest |
|                                                                      |
|  1 || sum w_j C_j   WSPT: largest ratio w_j/p_j   weighted version    |
|                     first (Smith's rule)          (exchange argument) |
|                                                                      |
|  1 || Lmax          EDD: Earliest Due Date first  minimize max        |
|                                                   lateness            |
|                                                                      |
|  1 || sum U_j       Moore-Hodgson algorithm       min # of late jobs  |
+----------------------------------------------------------------------+
```

**SPT optimality (the exchange argument)**: in $\sum C_j$, a short job placed before a long one delays only itself a little; the reverse delays the short job by the long job's full length. Swapping any out-of-SPT-order adjacent pair improves the objective — so SPT is optimal. This *adjacent-pairwise-exchange* proof technique recurs throughout scheduling.

**Smith's WSPT rule** generalizes: sequence by decreasing $w_j / p_j$ for $\sum w_j C_j$. **EDD** (Jackson's rule) minimizes maximum lateness $L_{max}$. These are exact, $O(n \log n)$ (just a sort) — a striking contrast to the NP-hardness one cell over.

```
   SPT in action (1 || sum C_j):
   jobs p = [3, 1, 2]  ->  sort: [1, 2, 3]
   completion times:    1, 1+2=3, 3+3=6   sum = 10  (optimal)
   any other order gives a larger sum.
```

---

## Layer 3: Critical Path Method (CPM) and PERT

For a **project** — tasks with durations and precedence — the schedule is governed by the **longest path** through the dependency DAG.

```
   PROJECT AS A DAG (activity-on-node), durations in [ ]:

        [A:3] ---> [C:2] ---\
       /                      \
   START                       [E:4] ---> END
       \                      /
        [B:5] -------> [D:1]-/

   PATHS:   A->C->E = 3+2+4 = 9
            B->D->E = 5+1+4 = 10  <- CRITICAL PATH (longest = project length)
   Project minimum duration = 10. Critical activities: B, D, E (zero slack).
```

**The Critical Path Method** computes, for each activity, four times via two passes:

| Quantity | Pass | Meaning |
|----------|------|---------|
| ES (earliest start) | forward | earliest it can begin given predecessors |
| EF (earliest finish) | forward | $ES + \text{duration}$ |
| LS (latest start) | backward | latest start not delaying the project |
| LF (latest finish) | backward | latest finish not delaying the project |
| **Slack / float** | $LS - ES$ | how much an activity can slip |

**Critical activities have zero slack** — delaying any of them delays the whole project. The critical path is the chain of zero-slack activities; it *is* the longest path in the DAG, computable in $O(V+E)$ by topological order. This is a polynomial-time optimum — the project length problem is easy.

**Bridge — old world → project tooling**: this is exactly the engine inside MS Project / any Gantt tool. "What's the critical path?" = "longest path in the task DAG." Crashing the schedule = shortening critical-path activities (and watching for a *new* critical path to emerge).

### PERT — Adding Uncertainty

**PERT** treats activity durations as random, typically with a **Beta distribution** estimated from three points: optimistic $a$, most-likely $m$, pessimistic $b$:

```
   PERT activity estimates (Beta approximation):
     mean      te  = (a + 4m + b) / 6
     variance  sigma^2 = ((b - a) / 6)^2

   Project duration ~ Normal (CLT over critical-path activities):
     mean    = sum of te along the critical path
     var     = sum of sigma^2 along the critical path
   => P(finish by deadline) from the normal CDF.
```

**The PERT caveat (state it honestly):** PERT assumes the critical path is fixed and sums variances along it, applying the CLT. But with randomness a *non-critical* path can become critical in some scenarios, so classical PERT **systematically underestimates** expected project duration (Jensen's inequality on the max of paths). For accurate tail estimates, **Monte Carlo simulation** of the network (file 08) is the right tool — and this is one of the canonical "simulate vs. solve" cases.

---

## Layer 4: Parallel Machines and List Scheduling

$P\,||\,C_{max}$ — schedule $n$ jobs on $m$ identical machines to minimize makespan — is **NP-hard** (it generalizes the Partition problem). We use **list scheduling** and bound how bad it can be.

```
   GRAHAM'S LIST SCHEDULING:
   - order the jobs in some list
   - repeatedly assign the next job to the machine that is
     currently LEAST loaded (greedy, no idle time)

   M1: [== J1 ==][= J4 =]
   M2: [= J2 =][=== J3 ===][J5]
   M3: [==== J6 ====]
        makespan = max machine finish time
```

**Theorem (Graham 1966).** Any list schedule for $P\,||\,C_{max}$ has makespan at most
$$\left(2 - \frac{1}{m}\right) \cdot C_{max}^*,$$
where $C_{max}^*$ is the optimal makespan. So list scheduling is a **$(2 - 1/m)$-approximation**, and this bound is **tight** (achieved by adversarial instances).

```
   PROOF IDEA (clean and worth knowing):
   Let M be the last machine to finish, and let job J start last on it
   at time S. Before S, every machine was busy (greedy: J went to the
   least-loaded machine). So S <= (total work - p_J)/m. Then
        Cmax = S + p_J <= (sum p_i)/m + (1 - 1/m) p_J.
   Two lower bounds on the optimum:  Cmax* >= (sum p_i)/m   (avg load)
        and  Cmax* >= p_J  (longest job). Combine:
        Cmax <= Cmax* + (1 - 1/m) Cmax* = (2 - 1/m) Cmax*.
```

**Improving the constant — LPT (Longest Processing Time first):**

**Theorem (Graham 1969).** If the list is sorted in *decreasing* processing time (LPT), the makespan is at most
$$\left(\frac{4}{3} - \frac{1}{3m}\right) \cdot C_{max}^*.$$
Sorting longest-first leaves only small jobs to balance at the end — a $4/3$-approximation, far better than the generic $2$.

| Algorithm | Approximation ratio for $P\,||\,C_{max}$ |
|-----------|------------------------------------------|
| Arbitrary list scheduling | $2 - 1/m$ (tight) |
| LPT (longest first) | $4/3 - 1/(3m)$ |
| PTAS (Hochbaum–Shmoys) | $(1+\epsilon)$ for any fixed $\epsilon$, poly time |

A **PTAS** (polynomial-time approximation scheme) exists for $P\,||\,C_{max}$: for any $\epsilon > 0$ you can get within $(1+\epsilon)$ of optimal in time polynomial in $n$ (exponential in $1/\epsilon$). This is the strongest positive result — you can get arbitrarily close to optimal in polynomial time.

---

## Layer 5: Flow Shop and Job Shop

```
   FLOW SHOP (F): every job visits machines in the SAME order M1->M2->...
   JOB SHOP (J):  each job has its OWN machine route (the general factory)
   OPEN SHOP (O): machine order is free
```

**Johnson's rule** — the one beautiful exact result: $F2\,||\,C_{max}$ (two-machine flow shop) is solved **optimally in $O(n \log n)$**:

```
   JOHNSON'S RULE (2-machine flow shop):
   - jobs with p1 <= p2: schedule EARLY, in increasing p1 order
   - jobs with p1 >  p2: schedule LATE,  in decreasing p2 order
   This minimizes makespan exactly. (A rare exact multi-machine result.)
```

But the moment you add a third machine, $F3\,||\,C_{max}$ becomes **NP-hard**. And **$J\,||\,C_{max}$ (job shop) is strongly NP-hard** — famously, a 10-job × 10-machine instance (Fisher–Thompson, 1963) stood unsolved for over 20 years. Job shop is attacked by:

| Job-shop method | Type |
|-----------------|------|
| Disjunctive graph + branch & bound | Exact (small instances) |
| Shifting bottleneck heuristic | Constructive heuristic |
| MIP formulation (big-M disjunctions) | Exact via solver (file 03) |
| Tabu search / simulated annealing / GA | Metaheuristic |
| Constraint programming | Often the practical winner |

The **disjunctive graph** model represents the job-shop as a DAG with *disjunctive* edges (which job goes first on a shared machine?); choosing an orientation for each disjunction and finding the longest path gives the makespan — connecting directly to the critical-path idea of Layer 3.

---

## Old World → Scheduling Bridges

| You already know | Scheduling analogue |
|------------------|---------------------|
| Critical path in a project plan (MS Project) | CPM: longest path in the task DAG, $O(V+E)$ |
| Build dependency graph / topological order | The precedence DAG; forward/backward passes |
| CPU scheduler (SJF, EDF) | SPT = SJF for $\sum C_j$; EDD ≈ EDF |
| Load balancing across workers | $P\,||\,C_{max}$, list scheduling, the $(2-1/m)$ bound |
| "Greedy heuristic, hope it's good" | List scheduling — but now with a *proven* $2-1/m$ bound |
| Slack/buffer in a release plan | Float = $LS - ES$; zero-float tasks are critical |
| Capacity-constrained sprint planning | Bin-packing / parallel-machine makespan |
| Tail-risk on a delivery date | PERT + Monte Carlo (file 08) |

The systems upgrade: a CPU scheduler ships a heuristic with no guarantee; scheduling theory gives you the *same* greedy rule **plus a proof** that you're within $2\times$ (or $4/3\times$ with LPT) of the best possible. When you can't compute the optimum, the bound is the product.

---

## Decision Cheat Sheet

| Problem | Approach |
|---------|----------|
| Minimize total completion on 1 machine | SPT (sort by $p_j$) — exact |
| Weighted total completion, 1 machine | WSPT / Smith's rule (sort by $w_j/p_j$) — exact |
| Minimize max lateness, 1 machine | EDD (sort by due date) — exact |
| Project duration + critical path | CPM: longest path in DAG — exact, $O(V+E)$ |
| Project duration under uncertainty | PERT, but Monte Carlo for tails (file 08) |
| Balance load on $m$ machines | LPT list scheduling ($4/3$-approx); PTAS for $(1+\epsilon)$ |
| 2-machine flow shop | Johnson's rule — exact, $O(n\log n)$ |
| Job shop (general factory) | MIP / CP / shifting bottleneck / metaheuristics |
| Need a provable guarantee, not just a heuristic | Use an approximation algorithm with a known ratio |

---

## Common Confusion Points

### "Is scheduling polynomial or NP-hard?"

Both, depending on the cell of $\alpha|\beta|\gamma$. Single-machine sum-completion (SPT) and max-lateness (EDD), critical path, and 2-machine flow shop (Johnson) are **polynomial**. Parallel-machine makespan, 3+-machine flow shop, and job shop are **NP-hard**. The tractability boundary is razor-thin — adding one machine or a precedence constraint can flip an easy problem to NP-hard. Always locate your exact problem in the taxonomy before assuming difficulty.

### "What does a $2 - 1/m$ approximation actually guarantee?"

That for *every* instance, the greedy list schedule's makespan is at most $(2 - 1/m)$ times the (unknown) optimal makespan. It is a **worst-case** guarantee — typical performance is much better. The bound is **tight**: there exist adversarial instances where list scheduling really is $(2 - 1/m)$ times optimal, so you cannot prove a smaller constant for arbitrary list order (use LPT for $4/3$).

### "PERT gives the expected project duration, right?"

Not exactly — classical PERT **underestimates** expected duration. It sums means and variances along the *single* deterministic critical path, but under randomness the actual longest path varies, and $E[\max(\text{paths})] \ge \max(E[\text{paths}])$ by Jensen's inequality. The true expected completion is at least the PERT estimate, often more. For honest tail probabilities, simulate the network (file 08). This is a textbook "simulate vs. solve" decision.

### "SPT minimizes everything?"

No. SPT minimizes **total (unweighted) completion time** $\sum C_j$ on one machine. It does *not* minimize makespan (irrelevant on one machine, but on parallel machines LPT is better), nor max lateness (use EDD), nor weighted completion (use WSPT). Match the rule to the objective — each objective in $\gamma$ has its own optimal rule (or is NP-hard).

### "Critical path vs. critical chain — same thing?"

Critical path is the longest precedence chain (CPM, deterministic). Critical *chain* (Goldratt) adds **resource constraints** and buffers — it accounts for the fact that two critical-path tasks might need the same scarce resource and can't actually run in parallel. Resource-constrained project scheduling (RCPSP) is NP-hard, unlike pure CPM. Don't conflate the resource-free longest-path computation with the resource-constrained scheduling problem.

### "Job shop is just parallel scheduling with routes?"

It's much harder. Parallel-machine makespan ($P||C_{max}$) is NP-hard but has good approximations and a PTAS. Job shop ($J||C_{max}$) is **strongly NP-hard** with no constant-factor approximation known for the general case, and small instances resisted solution for decades. The per-job routing and the disjunctive machine-sharing constraints make it qualitatively harder — which is why it's the domain of MIP solvers, constraint programming, and metaheuristics rather than clean approximation bounds.
