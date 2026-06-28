---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "01-LINEAR-PROGRAMMING.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:operations-research:linear-programming
kind: guide
module: operations-research
section: operations-research
title: Linear Programming - Geometry and the Simplex Method
status: source-custody
source_custody: partial
current_path: operations-research/01-LINEAR-PROGRAMMING.md
canonical_path: operations-research/01-LINEAR-PROGRAMMING.md
backsource_ids: [proof-backfill:operations-research:01-linear-programming, git-history:operations-research:01-linear-programming]
concepts: [linear programming, simplex method, feasible polytope, standard form, basic feasible solution]
root_concepts: [linear programming]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Linear Programming — Geometry and the Simplex Method

## The Big Picture

A linear program optimizes a **linear objective** over a **polyhedron** defined by linear inequalities. The entire theory rests on one geometric fact: the optimum, if it exists, is achieved at a **vertex** of the feasible polyhedron. The simplex method is a disciplined walk from vertex to vertex along edges, each step improving the objective, until no improving edge remains.

```
+----------------------------------------------------------------------+
|             LINEAR PROGRAMMING: THE WHOLE PICTURE                     |
|                                                                      |
|   ALGEBRA                       GEOMETRY                              |
|   -------                       --------                             |
|   max c'x                       objective = direction c              |
|   s.t. Ax <= b                  each row of A = a halfspace          |
|        x >= 0                   intersection = POLYHEDRON P          |
|                                                                      |
|                          x2                                          |
|                          |    c (objective direction)               |
|                          |   /                                       |
|        feasible          | V3 ._____                                  |
|        polytope P    V4 _|/        \  V2  <-- OPTIMUM here            |
|                       /  |          \ /     (a vertex)               |
|                      /   |  P        X                                |
|                     /    |          / \                              |
|              V5 ___/_____|_________/   \__ V1                         |
|                          |________________________ x1               |
|                                                                      |
|   FUNDAMENTAL THEOREM OF LP:                                          |
|   if an optimum exists, one occurs at a VERTEX (extreme point).      |
|   SIMPLEX walks vertices V_i along edges, uphill in c, to optimum.   |
+----------------------------------------------------------------------+
```

**Read this as a correspondence**: algebra on the left, geometry on the right. Vertices of the polytope ⟷ basic feasible solutions of the linear system. Edges ⟷ pivots. This algebra-geometry dictionary *is* linear programming.

---

## Layer 1: Standard Form

Every LP can be converted to a canonical **standard form**. Two common conventions exist; we use the inequality form for geometry and the equality form for the simplex tableau.

```
   INEQUALITY (geometric) FORM           EQUALITY (computational) FORM
   ----------------------------          ------------------------------
   max  c'x                              max  c'x
   s.t. Ax <= b                          s.t. Ax = b      (add slacks)
        x >= 0                                x >= 0
                                          where x now includes slack vars
```

**Conversions** (all LPs reduce to standard form):

| Original | Transformation |
|----------|----------------|
| min c'x | max (−c)'x |
| a'x ≥ b (constraint) | −a'x ≤ −b, or subtract surplus s ≥ 0 |
| a'x = b | keep as equality, or split into ≤ and ≥ |
| a'x ≤ b | add slack s ≥ 0: a'x + s = b |
| x free (unbounded sign) | x = x⁺ − x⁻ with x⁺, x⁻ ≥ 0 |

After adding slacks, the constraints become **Ax = b, x ≥ 0** where $A \in \mathbb{R}^{m \times n}$ has full row rank $m$ (drop redundant rows), and $n > m$.

```
   Original:   max 3x1 + 2x2
               s.t.  x1 +  x2 <= 4
                     x1 + 3x2 <= 6
                     x1, x2 >= 0

   Standard:   max 3x1 + 2x2 + 0s1 + 0s2
               s.t.  x1 +  x2 + s1      = 4
                     x1 + 3x2      + s2 = 6
                     x1, x2, s1, s2 >= 0
                          m = 2 equations, n = 4 variables
```

---

## Layer 2: The Geometry — Polyhedra, Vertices, and the Fundamental Theorem

A **polyhedron** is $P = \{x : Ax \le b\}$, an intersection of finitely many halfspaces. A bounded polyhedron is a **polytope**. The key objects:

```
+--------------------------------------------------------------+
|  TERM            DEFINITION                  WHY IT MATTERS   |
|  ----            ----------                  -------------    |
|  Halfspace       {x : a'x <= b}              one constraint   |
|  Polyhedron      intersection of halfspaces  feasible region  |
|  Vertex /        point not on any segment    candidate optima |
|   extreme point  between two other pts of P                   |
|  Edge            1-dim face joining vertices  simplex walks it |
|  Face            P intersect a supporting     where optima     |
|                  hyperplane                   live             |
+--------------------------------------------------------------+
```

**Theorem (Fundamental Theorem of Linear Programming).** Consider max $c'x$ over a nonempty polyhedron $P = \{x : Ax \le b\}$. Then exactly one of:
1. the objective is **unbounded above** on $P$; or
2. an **optimal solution exists**, and if $P$ has at least one vertex, an optimal solution is attained at a vertex.

*Hypotheses worth stating*: the "attained at a vertex" guarantee requires $P$ to have a vertex (equivalently, $P$ contains no line; standard form with $x \ge 0$ always satisfies this). If the optimum is attained on a higher-dimensional face, that face still contains a vertex which is also optimal.

```
   WHY THE OPTIMUM IS AT A VERTEX (intuition):

   The objective c'x is linear. Its level sets {x : c'x = k} are parallel
   hyperplanes. Push the hyperplane in direction c as far as P allows.
   The LAST point(s) of contact form a face of P. A bounded face always
   contains a vertex. So a vertex is always among the optima.

        level sets of c'x
        \    \    \    \
         \    \    \    \   <-- push this way (increasing c'x)
          \    \    \    \
   +-------\----\----\----+
   |  P     \    \    \   |* last contact = optimal vertex
   +---------\----\----\--+
```

### Vertices ⟷ Basic Feasible Solutions (the bridge to algebra)

In equality form $Ax = b$, $x \ge 0$ with $A$ being $m \times n$ of rank $m$:

- Choose $m$ **basic** columns forming an invertible $B$ (the **basis**); the other $n-m$ are **nonbasic**.
- Set nonbasic variables to 0; solve $B x_B = b$ for the basic variables: $x_B = B^{-1}b$.
- This is a **basic solution**. If additionally $x_B \ge 0$, it is a **basic feasible solution (BFS)**.

**Theorem.** $x$ is a vertex of $\{x : Ax = b, x \ge 0\}$ **if and only if** $x$ is a basic feasible solution.

```
   GEOMETRY            ALGEBRA
   --------            -------
   vertex          =   basic feasible solution
   edge            =   one-variable swap (pivot)
   moving along    =   increasing a nonbasic var from 0
    an edge            until a basic var hits 0
```

A vertex is **degenerate** if a basic variable equals 0 there (more than the minimal number of constraints are tight). Degeneracy is the source of simplex cycling.

The number of vertices is at most $\binom{n}{m}$ — exponential. This is why we cannot just enumerate; we need simplex.

---

## Layer 3: The Simplex Method

Dantzig's simplex (1947) is the algebraic realization of "walk vertices uphill."

```
+----------------------------------------------------------------------+
|                        SIMPLEX ALGORITHM                             |
|                                                                      |
|  0. Start at a basic feasible solution (a vertex).                   |
|                                                                      |
|  1. PRICE OUT: compute reduced costs for nonbasic vars:             |
|        c_bar_j = c_j - c_B' B^-1 A_j                                 |
|     (how much the objective improves per unit of x_j entering)      |
|                                                                      |
|  2. OPTIMALITY TEST: if all reduced costs c_bar_j <= 0 (for a max),  |
|        STOP -- current vertex is OPTIMAL.                            |
|                                                                      |
|  3. ENTERING VAR: pick nonbasic j with c_bar_j > 0 (improving edge).|
|                                                                      |
|  4. RATIO TEST: as x_j increases, find which basic var hits 0 first:|
|        theta = min over i with (B^-1 A_j)_i > 0 of                   |
|                    (B^-1 b)_i / (B^-1 A_j)_i                         |
|     If no such i (column has no positive entry): UNBOUNDED.          |
|                                                                      |
|  5. PIVOT: x_j enters basis, the arg-min basic var leaves.          |
|     New vertex. Go to 1.                                             |
+----------------------------------------------------------------------+
```

The **reduced cost** $\bar c_j = c_j - c_B^\top B^{-1} A_j$ is the marginal change in the objective per unit increase of nonbasic $x_j$. The quantity $y^\top = c_B^\top B^{-1}$ is exactly the vector of **dual variables / simplex multipliers** — duality is hiding in plain sight inside the simplex tableau (see file 02).

### A Worked Pivot

```
   max 3x1 + 2x2,  x1 + x2 + s1 = 4,  x1 + 3x2 + s2 = 6

   START basis {s1, s2}: x1=x2=0, s1=4, s2=6, objective = 0.
   Reduced costs: c_bar_x1 = 3, c_bar_x2 = 2  (both > 0).

   ENTER x1 (largest reduced cost = Dantzig rule).
   RATIO TEST: 4/1 = 4  (s1 row),  6/1 = 6 (s2 row). Min = 4 -> s1 leaves.
   PIVOT: x1 = 4, basis {x1, s2}, objective = 12.

   Reduced cost of x2 now: 2 - 3*(1) = -1 < 0 ... recompute properly:
   after pivot c_bar_x2 = -1 (<=0) and c_bar_s1 = -3 (<=0) -> OPTIMAL.
   Optimal: x1=4, x2=0, objective = 12.
```

### Finding a Starting Vertex: Phase I

If the origin is infeasible (e.g., with ≥ or = constraints), simplex needs a starting BFS. Two standard approaches:

| Method | Idea |
|--------|------|
| **Two-phase simplex** | Phase I: add artificial vars, minimize their sum; if min = 0, drop them and a feasible vertex is found. Phase II: optimize the real objective. |
| **Big-M method** | Penalize artificial vars with a huge cost $M$ in a single combined objective. |

If Phase I terminates with positive artificial-variable sum, the original LP is **infeasible** — simplex doubles as a feasibility certificate engine.

---

## Layer 4: Complexity — Precisely

This is where careless guides go wrong. State it exactly.

```
+----------------------------------------------------------------------+
|  CLAIM                                              STATUS            |
|  -----                                              ------            |
|  LP (the decision/optimization problem) is in P     TRUE (Khachiyan   |
|                                                     1979, ellipsoid)  |
|  Simplex has exponential worst-case running time    TRUE (Klee-Minty  |
|    (for common pivot rules)                         cube, 1972)       |
|  Simplex is fast in practice (~ linear in m pivots) TRUE empirically; |
|                                                     explained by      |
|                                                     smoothed analysis |
|                                                     (Spielman-Teng    |
|                                                     2001/2004)        |
|  Interior-point methods are polynomial AND practical TRUE (Karmarkar  |
|                                                     1984)             |
+----------------------------------------------------------------------+
```

**Klee–Minty cube**: a deformed hypercube in $n$ dimensions whose vertices, under Dantzig's largest-coefficient rule, are all visited — $2^n - 1$ pivots. So simplex with that rule is exponential worst-case. Variants of Klee–Minty exist for most deterministic pivot rules; whether *any* pivot rule makes simplex polynomial is **open** (related to the polynomial Hirsch conjecture).

**Why simplex still dominates**: on real instances it takes roughly $O(m)$ to $O(m \log n)$ pivots. Smoothed analysis proved that tiny random perturbations of any instance make the expected number of pivots polynomial — the worst cases are knife-edge and measure-zero-ish.

**Cycling and anti-cycling**: degeneracy can make simplex revisit a vertex forever. **Bland's rule** (choose the lowest-index eligible entering and leaving variable) guarantees finite termination. The **lexicographic / perturbation method** also prevents cycling.

---

## Layer 5: Simplex vs. Interior-Point

```
       SIMPLEX                          INTERIOR-POINT
       -------                          --------------
   walks the BOUNDARY,              cuts THROUGH the interior,
   vertex to vertex                 following the "central path"

        ._____.                          .________.
       /|     |\                        /          \
      / |  P  | \                      /     o      \
     .  |     |  .                    |    .  \      |
      \ *--->*--*  <- path on edges   |   /    o ->  *  <- path inside
       \|     |/                       \ o        * /
        *_____*                         o________*/
                                         endpoint snaps to a vertex
```

| Dimension | Simplex | Interior-point (e.g., primal-dual) |
|-----------|---------|-------------------------------------|
| Path | Vertices (boundary) | Interior, central path |
| Worst case | Exponential | Polynomial, $O(\sqrt{n})$ iterations to ε |
| Per-iteration cost | Cheap (one pivot, rank-1 update) | Expensive (solve a Newton system) |
| Warm starts | Excellent (great for branch & bound, file 03) | Poor |
| Solution type | Exact vertex (basic) | ε-optimal interior point |
| Large sparse LPs | Competitive | Often wins |

**Bridge to numerical methods**: interior-point methods solve a sequence of Newton steps on a barrier-augmented system — see `numerical-methods/` (linear systems, Newton's method) and file 05 here for the convex-optimization treatment. The barrier function $-\sum \log x_i$ keeps iterates strictly inside the feasible region.

---

## Old World → LP World Bridges

| You already know | LP analogue |
|------------------|-------------|
| Constraint solver / SAT feasibility | Phase I simplex decides LP feasibility |
| Gradient descent (ML) | Simplex is a combinatorial cousin: discrete steepest-ascent over vertices |
| Resource quotas / capacity planning | Constraints $Ax \le b$ are resource limits |
| Greedy "improve until stuck" heuristic | Simplex IS greedy, but provably reaches the global optimum (convexity guarantees it) |
| Spreadsheet "Solver" add-in | That Solver runs simplex or interior-point under the hood |
| Profiling: hotspot is in matrix solves | Same here: each pivot/Newton step is a linear-algebra kernel |

The deep point: simplex looks like a greedy local-search heuristic, and in software a greedy heuristic gives no guarantee. Here it gives a *global* guarantee, purely because the feasible region is convex and the objective is linear — local optimality implies global optimality.

---

## Decision Cheat Sheet

| Situation | Choice |
|-----------|--------|
| Small/medium LP, need exact vertex | Simplex |
| Huge sparse LP | Interior-point (often) |
| Inside branch & bound (many re-solves) | Simplex (warm starts) — see file 03 |
| Need to detect infeasibility | Phase I simplex (artificial vars) |
| Worried about cycling at degenerate vertices | Bland's rule or lexicographic pivoting |
| Need shadow prices / sensitivity | Read off $y = c_B^\top B^{-1}$ — see file 02 |
| Objective seems unbounded | Ratio test column all ≤ 0 → certify unbounded |
| Variables must be integer | This is no longer LP — go to file 03 (IP) |

---

## Common Confusion Points

### "Why a vertex? Couldn't the optimum be in the middle of a face?"

It can be — but a face that is optimal always *contains* a vertex that is equally optimal (a bounded face has extreme points, and a linear function is constant on the optimal face). So restricting the search to vertices loses nothing. When the optimal face is higher-dimensional, the LP has **multiple optima** (the objective level set is parallel to that face).

### "Is simplex polynomial or exponential? I've heard both."

Simplex with standard pivot rules is **exponential worst-case** (Klee–Minty) but **polynomial in practice** (and provably so under smoothed analysis). LP **as a problem** is polynomial (ellipsoid, interior-point). The confusion comes from conflating *the algorithm* (simplex) with *the problem* (LP). Keep them separate.

### "Reduced cost, shadow price, dual variable — same thing?"

Related but distinct. The **dual variables** $y = c_B^\top B^{-1}$ are the shadow prices of the *constraints* (value of relaxing $b_i$). The **reduced cost** $\bar c_j = c_j - y^\top A_j$ is the per-unit objective change of bringing nonbasic *variable* $j$ into the solution. Optimality ⟺ all reduced costs ≤ 0 (max) ⟺ dual feasibility. File 02 makes this precise.

### "What if the LP is degenerate?"

A degenerate vertex has a basic variable equal to 0; multiple bases describe the same point. Pivots can then produce no objective improvement (a "stalling" pivot), and naive rules can **cycle**. Use Bland's rule or lexicographic perturbation to guarantee termination. Degeneracy also makes shadow prices non-unique (a one-sided derivative).

### "Slack variables — are they real?"

They are bookkeeping variables that turn inequalities into equalities, but they carry meaning: a positive slack $s_i$ means constraint $i$ is *not* binding (you have unused resource $i$), and by complementary slackness its dual price is 0. A zero slack means the constraint is tight and may have positive shadow price. So slacks are how the geometry (which faces are active) shows up in the algebra.
