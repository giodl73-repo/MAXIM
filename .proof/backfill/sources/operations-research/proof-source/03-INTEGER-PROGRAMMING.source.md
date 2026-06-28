---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "03-INTEGER-PROGRAMMING.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:operations-research:integer-programming
kind: guide
module: operations-research
section: operations-research
title: Integer Programming - Branch-and-Bound, Cutting Planes, NP-Hardness
status: source-custody
source_custody: partial
current_path: operations-research/03-INTEGER-PROGRAMMING.md
canonical_path: operations-research/03-INTEGER-PROGRAMMING.md
backsource_ids: [proof-backfill:operations-research:03-integer-programming, git-history:operations-research:03-integer-programming]
concepts: [integer programming, branch and bound, cutting planes, LP relaxation, NP-hardness]
root_concepts: [integer programming]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Integer Programming — Branch-and-Bound, Cutting Planes, and the Cost of Discreteness

## The Big Picture

An integer program (IP) is a linear program with the extra demand that some variables take **integer** values. That single requirement destroys convexity, makes the problem **NP-hard**, and forces a search strategy: solve the easy **LP relaxation** to get a bound, then systematically rule out fractional possibilities by **branching** and **cutting**.

```
+----------------------------------------------------------------------+
|             INTEGER PROGRAMMING: THE WHOLE PICTURE                    |
|                                                                      |
|   The LP relaxation gives a CONTINUOUS polytope (easy).             |
|   The integer points are a LATTICE inside it (hard).               |
|                                                                      |
|        x2                                                            |
|        3 +  . . . . . . . .   . = integer feasible point            |
|          |  . ___________ .       o = LP optimum (fractional!)      |
|        2 +  ./           \. o     * = IP optimum                    |
|          |  /  LP poly-   \                                         |
|        1 +  . *  tope P    .                                        |
|          |  \             /                                         |
|        0 +  . \_________ /. .                                       |
|          +--+--+--+--+--+--+---- x1                                  |
|             0  1  2  3  4  5                                         |
|                                                                      |
|   STRATEGY:                                                          |
|     1. Solve LP relaxation -> bound z_LP >= z_IP (for a max).        |
|     2. If LP optimum is integer -> done.                            |
|     3. Else BRANCH (split on a fractional var) or                   |
|        CUT (add a valid inequality slicing off o, keeping the dots).|
+----------------------------------------------------------------------+
```

**The core insight**: the LP relaxation is both your *bound* and your *guide*. Its optimal value bounds the IP optimum (relaxation is a superset, so a max over it is $\ge$). Its fractional variables tell you where to branch.

---

## Layer 1: The Model Zoo

```
+----------------------------------------------------------------------+
|  TYPE                  VARIABLES              EXAMPLE                 |
|  ----                  ---------              -------                 |
|  Pure IP (ILP)         all integer            counting / lot sizing  |
|  Mixed IP (MIP)        some integer,          facility location      |
|                        some continuous         (open? + how much?)   |
|  0-1 / Binary IP       x_j in {0,1}           assignment, knapsack,  |
|                                                set cover, scheduling |
|  Combinatorial         structure-encoded      TSP, matching, cuts    |
+----------------------------------------------------------------------+
```

Binary variables are the modeling power tool. They encode logic:

| Logical condition | Linear encoding (binary $x, y$) |
|-------------------|----------------------------------|
| "at most one of A, B" | $x_A + x_B \le 1$ |
| "if A then B" ($x_A \Rightarrow x_B$) | $x_A \le x_B$ |
| "exactly $k$ of $n$" | $\sum_j x_j = k$ |
| "fixed cost if used" (big-M) | $q \le M\,x$, $q \ge 0$, $x \in \{0,1\}$ |
| "either constraint 1 or 2" (disjunction) | big-M with an indicator $x$ |

**Bridge — old world → constraint solving**: binary IP is the LP-flavored cousin of SAT. "if A then B" is a Horn clause; the big-M disjunction is a clause selector. A MIP solver is, in effect, a numerical constraint solver with an objective. The reason MIP and SAT are both NP-hard is the same: they can encode each other.

---

## Layer 2: NP-Hardness — Stated Precisely

**Theorem.** Integer Linear Programming (feasibility: does $\{x \in \mathbb{Z}^n : Ax \le b\}$ contain a point?) is **NP-complete**. The optimization version is **NP-hard**.

```
   WHY: a Karp reduction from a known NP-complete problem.

   3-SAT  ----encodes as---->  0-1 IP feasibility
   each clause (a v ~b v c) becomes  x_a + (1 - x_b) + x_c >= 1
   x_i in {0,1}.  A satisfying assignment <=> a feasible 0-1 point.
```

So IP is at least as hard as 3-SAT (Cook–Levin). Contrast with LP, which is in **P** (file 01). The watershed is integrality, not linearity.

```
   COMPLEXITY LANDSCAPE:

   LP (continuous)          in P        ellipsoid / interior-point
        |
        | add integrality
        v
   ILP (integer)            NP-hard     no poly algorithm known (P=NP open)
        |
        | special structure (TU matrix)
        v
   Network flow / matching  in P        relaxation is automatically integral
```

**The crucial escape hatch — total unimodularity (TU):** if the constraint matrix $A$ is **totally unimodular** (every square submatrix has determinant in $\{-1, 0, +1\}$) and $b$ is integer, then *every vertex of the LP relaxation is already integer*. The IP and its LP relaxation coincide — you get integrality for free, in polynomial time. This is exactly why network-flow problems (file 04) are easy: their node-arc incidence matrices are TU.

| Matrix property | Consequence |
|-----------------|-------------|
| Totally unimodular, integer $b$ | LP relaxation optimum is integer → IP is polynomial |
| General integer matrix | IP is NP-hard |

---

## Layer 3: LP Relaxation — Bound and Guide

The **LP relaxation** drops integrality ($x \in \mathbb{Z}^n \to x \in \mathbb{R}^n$). It is the single most important tool in IP.

```
   FOR A MAXIMIZATION IP:
       z_IP  <=  z_LP        (relaxation has MORE feasible points)
       ^                ^
   true optimum    relaxation bound (UPPER bound for max)

   INTEGRALITY GAP = z_LP / z_IP  (worst-case ratio over instances) --
   measures how good a bound the relaxation gives. Small gap = strong
   formulation. Tightening the formulation shrinks this gap.
```

Three uses of the relaxation:
1. **Bound** — prune the search tree (a node whose LP bound is worse than the incumbent can be discarded).
2. **Guide** — fractional variables in the LP solution tell you where to branch.
3. **Rounding / approximation** — for many problems, rounding the LP solution gives a provably near-optimal integer solution.

**Bridge to ML / approximation algorithms**: LP-relaxation-and-round is the dominant technique for designing approximation algorithms (e.g., set cover via LP rounding achieves an $H_n \approx \ln n$ approximation; vertex cover via LP gives factor 2). The relaxation is solved, then a deterministic or randomized rounding maps the fractional solution to an integer one with a bounded loss. This is the same "relax the hard discrete problem to a tractable convex one" move that pervades `machine-learning-theory/`.

---

## Layer 4: Branch and Bound

The exact algorithm. Divide the feasible region by branching on fractional variables; bound each subregion with its LP relaxation; prune aggressively.

```
+----------------------------------------------------------------------+
|                       BRANCH AND BOUND (maximize)                    |
|                                                                      |
|  incumbent z_best := -inf.  Queue := { root LP relaxation }.        |
|  while queue not empty:                                              |
|    pop a node; solve its LP relaxation -> value z_LP, point x_LP.   |
|                                                                      |
|    PRUNE BY INFEASIBILITY: LP infeasible -> discard node.           |
|    PRUNE BY BOUND:        z_LP <= z_best -> discard (can't beat it).|
|    PRUNE BY INTEGRALITY:  x_LP integer -> candidate; update z_best. |
|                                                                      |
|    else BRANCH: pick fractional x_j = f.                            |
|       child A: add constraint x_j <= floor(f)                       |
|       child B: add constraint x_j >= ceil(f)                        |
|       push both children.                                           |
|  return z_best.                                                     |
+----------------------------------------------------------------------+
```

```
   BRANCHING TREE (branch on x_j = 2.4):

                    [ root LP: z=18.5, x_j=2.4 ]
                     /                        \
            x_j <= 2                         x_j >= 3
           /                                        \
   [ LP: z=17.1, x_k=1.6 ]                   [ LP: z=16.0, integer! ]
      /          \                            -> incumbent z_best = 16
  x_k<=1       x_k>=2                          (prunes siblings with z_LP<=16)
   ...           ...
```

| Prune rule | Trigger | Why valid |
|------------|---------|-----------|
| **Infeasibility** | LP relaxation has no solution | Subregion empty |
| **Bound** | $z_{LP} \le z_{best}$ (max) | Subregion can't beat incumbent |
| **Integrality** | LP solution already integer | Optimal *for this subregion*; record it |

**Design choices that determine performance**:

| Choice | Options | Effect |
|--------|---------|--------|
| Branching variable | most-fractional, pseudocost, strong branching | Tree size |
| Node selection | depth-first (memory-light), best-first (fewest nodes), best-bound | Memory vs. node count |
| Incumbent | heuristics (rounding, feasibility pump) | Earlier pruning |
| LP warm starts | dual simplex reuse | Per-node speed (file 01) |

**Why dual simplex matters here**: branching *adds a constraint* to the parent's LP. The parent's optimal basis is still dual-feasible for the child, so **dual simplex** re-optimizes in a handful of pivots from the warm start. This is the operational reason simplex (not interior-point) dominates inside branch and bound — see file 01.

---

## Layer 5: Cutting Planes

Instead of (or alongside) branching, **tighten the relaxation** by adding valid inequalities (**cuts**) that remove the fractional LP optimum but no integer-feasible point.

```
   A CUT slices off the fractional LP optimum o, keeps all dots (.):

        before cut                       after adding cut
        ___________                      __________
       /          \  o                  /         /
      /  . . . .   \                    /  . . . ./   <- cut hugs the
     /   . . . .    \                  /   . . . /        integer hull
    /____. . . .____ \                /____. . ./
            (o is fractional)           (o now infeasible; re-solve LP)
```

**Gomory fractional cuts** (Gomory 1958): derived purely from the simplex tableau, they guarantee finite convergence to the integer optimum for pure ILP. Take a tableau row where basic $x_i = \bar b_i$ is fractional; the cut $\sum_j \text{frac}(\bar a_{ij})\, x_j \ge \text{frac}(\bar b_i)$ is valid for all integer points but violated by the current LP solution.

| Cut family | Source | Where used |
|------------|--------|------------|
| **Gomory fractional** | Simplex tableau, any ILP | General-purpose; finite termination |
| **Cover inequalities** | Knapsack constraints | 0-1 IP |
| **Clique / odd-hole** | Graph structure | Stable set, coloring |
| **MIR (mixed-integer rounding)** | General MIP | The backbone of modern solvers |

The ultimate object is the **integer hull**: $\text{conv}(\{x \in \mathbb{Z}^n : Ax \le b\})$, the convex hull of integer-feasible points. It is a polytope (for rational data), and optimizing the LP over it would solve the IP exactly — but it can have exponentially many facets, so we generate cuts on demand.

```
   LP polytope  ⊇  INTEGER HULL  ⊇  integer points
   cutting planes shrink the LP polytope toward the integer hull.
```

### Branch and Cut — the modern synthesis

Production solvers (CPLEX, Gurobi, SCIP, the COIN-OR stack) combine both:

```
   BRANCH AND CUT = branch & bound
                  + cutting planes added at nodes
                  + primal heuristics for incumbents
                  + presolve / preprocessing
                  + conflict learning (SAT-style clause learning)
```

This is why MIP solvers, despite NP-hardness, routinely solve instances with millions of variables: the worst case is exponential, but engineering (cuts + heuristics + presolve + warm starts) tames the typical case — directly analogous to how simplex is exponential worst-case but excellent in practice (file 01).

---

## Layer 6: Lagrangian Relaxation (an alternative bound)

When the constraints split into "easy" and "complicating," **Lagrangian relaxation** dualizes the complicating constraints into the objective with multipliers, leaving an easy subproblem.

```
   IP:  max c'x  s.t.  Ax <= b  (complicating),  x in X (easy set)

   Lagrangian:  L(lambda) = max_{x in X}  c'x + lambda'(b - Ax),  lambda >= 0
                (an easy problem for fixed lambda)

   L(lambda) >= z_IP for all lambda >= 0   (a valid bound)
   best bound = min_{lambda >= 0} L(lambda)  -- the Lagrangian dual
```

The Lagrangian dual bound is always at least as strong as the LP-relaxation bound (and strictly stronger when $X$ is not the integer hull of an LP). It is solved by **subgradient methods** — bridge to convex optimization, file 05, and to the subgradient machinery in `numerical-methods/`.

---

## Old World → IP Bridges

| You already know | IP analogue |
|------------------|-------------|
| SAT / constraint solver | 0-1 IP feasibility; both NP-complete, inter-reducible |
| Backtracking search with pruning | Branch and bound *is* backtracking with LP bounds |
| Branch prediction / pruning a search tree | Bounding rules prune the B&B tree |
| Build dependency resolution (version solving) | A feasibility IP over package selection |
| Resource scheduling / bin packing | Classic 0-1 IP (file 07 for scheduling specifics) |
| Caching a subproblem result | Warm-starting child LPs from parent basis |
| "Within 2% of optimal" SLA | The B&B optimality gap $(z_{best} - z_{LP})/z_{LP}$ is reported live |

The mental upgrade for a systems leader: a MIP solver gives you a **provable optimality gap** during the run. You can stop at "1% gap" and *know* you are within 1% of the best possible — a guarantee a hand-rolled heuristic cannot offer.

---

## Decision Cheat Sheet

| Situation | Choice |
|-----------|--------|
| Yes/no, assignment, selection decisions | 0-1 / binary IP |
| Open-a-facility + how-much-to-ship | Mixed IP with big-M linking |
| Constraint matrix is network-structured (TU) | Solve the LP relaxation — it's already integer (file 04) |
| Need an exact optimum | Branch and cut (modern MIP solver) |
| Need a quick provable bound | LP relaxation value |
| Need a near-optimal answer fast | LP relaxation + rounding (approximation) |
| Constraints split into easy + complicating | Lagrangian relaxation + subgradient |
| Solver too slow | Tighten formulation (cuts), add valid inequalities, presolve |
| Want "within X% of optimal" | Run B&B; stop at desired optimality gap |

---

## Common Confusion Points

### "Why not just solve the LP and round to the nearest integer?"

Rounding the LP optimum can be **infeasible** or **arbitrarily far from optimal**. Rounding $x_j = 2.4$ down might violate a constraint; rounding up another variable might too. For *structured* problems (TU, or with rounding theorems) it works with a guarantee; in general it does not. Branch and bound exists precisely because naive rounding fails.

### "Is the LP relaxation an upper or lower bound?"

For a **maximization** IP the relaxation is an **upper** bound ($z_{LP} \ge z_{IP}$) because relaxing constraints can only increase a max. For a **minimization** IP it is a **lower** bound. The rule: relaxation = optimistic bound. Always orient yourself by "more feasible points → better optimal value for that direction."

### "If IP is NP-hard, how do solvers handle million-variable models?"

NP-hardness is a *worst-case* statement. Real instances have structure (sparsity, near-TU blocks, symmetry the solver exploits). The combination of cuts, heuristics, presolve, and warm-started LP re-solves makes typical instances tractable. This is exactly parallel to simplex being exponential worst-case yet fast in practice (file 01) — the worst cases are adversarial, not typical.

### "Branch and bound vs. cutting planes — pick one?"

Modern solvers use **both** (branch and cut). Pure cutting planes (Gomory alone) can converge slowly with numerical issues; pure branching can explode. Cuts tighten each node's relaxation so branching has less work; branching resolves what cuts can't. They are complementary, not alternatives.

### "Total unimodularity — when do I get integrality for free?"

When the constraint matrix is **totally unimodular** (all square submatrices have determinant $\in \{-1,0,1\}$) **and** the RHS $b$ is integer. Then every LP vertex is integer, so the LP relaxation *is* the IP. Network-flow incidence matrices, interval matrices, and bipartite-matching matrices are TU — which is why those problems (file 04) are polynomial. Check TU before reaching for branch and bound.

### "Lagrangian bound vs. LP bound — which is tighter?"

The Lagrangian dual bound is **always at least as tight** as the LP-relaxation bound, and strictly tighter when the retained easy set $X$ has a non-integral LP description (the "integrality property" fails). If $X$'s LP relaxation is automatically integral, Lagrangian and LP bounds coincide. Use Lagrangian relaxation when the complicating constraints, once dualized, leave a genuinely combinatorial-but-easy subproblem.
