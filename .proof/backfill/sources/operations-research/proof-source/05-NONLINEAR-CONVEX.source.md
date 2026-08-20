---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "05-NONLINEAR-CONVEX.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:operations-research:nonlinear-convex
kind: guide
module: operations-research
section: operations-research
title: Nonlinear and Convex Optimization - Convexity, KKT, Interior-Point
status: source-custody
source_custody: partial
current_path: operations-research/05-NONLINEAR-CONVEX.md
canonical_path: operations-research/05-NONLINEAR-CONVEX.md
backsource_ids: [proof-backfill:operations-research:05-nonlinear-convex, git-history:operations-research:05-nonlinear-convex]
concepts: [convex optimization, KKT conditions, gradient descent, interior-point methods, Lagrangian duality]
root_concepts: [convex optimization]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Nonlinear and Convex Optimization — Convexity, KKT, and Interior-Point Methods

## The Big Picture

Once the objective or constraints become nonlinear, the clean vertex story of LP (file 01) is gone — but a deeper structure replaces it: **convexity**. For convex problems, local optimality implies global optimality, the **KKT conditions** certify optima (generalizing LP's complementary slackness), and **interior-point methods** solve them in polynomial time. Nonconvex problems lose all of this and you settle for stationary points.

```
+----------------------------------------------------------------------+
|          NONLINEAR / CONVEX OPTIMIZATION: THE WHOLE PICTURE          |
|                                                                      |
|   min f(x)   s.t.  g_i(x) <= 0,  h_j(x) = 0                          |
|                                                                      |
|   IS IT CONVEX?  (f convex, g_i convex, h_j affine)                  |
|         |                                                            |
|    +----+----------------------------+                              |
|    | YES                             | NO                           |
|    v                                 v                               |
|  every local min = GLOBAL min      many local minima;               |
|  KKT are SUFFICIENT (w/ CQ)        KKT only NECESSARY               |
|  interior-point: poly to eps       NP-hard in general;              |
|  strong duality (Slater)           local search -> a stationary pt  |
|                                                                      |
|   CERTIFICATE OF OPTIMALITY = KKT CONDITIONS:                       |
|     stationarity:  grad f + sum lambda_i grad g_i                    |
|                            + sum mu_j grad h_j = 0                  |
|     primal feas:   g_i(x) <= 0,  h_j(x) = 0                          |
|     dual feas:     lambda_i >= 0                                    |
|     compl. slack:  lambda_i g_i(x) = 0                              |
+----------------------------------------------------------------------+
```

**The watershed (restated from the overview)**: convexity — not linearity — separates tractable from intractable continuous optimization. LP is the linear special case of convex optimization; everything in files 01–02 is a corollary of the convex theory here.

---

## Layer 1: Convex Sets and Convex Functions

**Convex set**: $C$ is convex if $x, y \in C \Rightarrow \lambda x + (1-\lambda)y \in C$ for all $\lambda \in [0,1]$. The line segment between any two points stays inside.

**Convex function**: $f: \mathbb{R}^n \to \mathbb{R}$ is convex if its domain is convex and
$$f(\lambda x + (1-\lambda)y) \le \lambda f(x) + (1-\lambda) f(y).$$

```
   CONVEX FUNCTION                  CONVEX SET
   ---------------                  ----------
       f                            +-----------+
       |  \           /            /             \
       |   \         /            |   any chord   |
       |    \.______./            |   stays       |
       |   chord lies ABOVE       |   inside      |
       |   the graph               \             /
       +---------------- x          +-----------+
```

**First-order characterization** (differentiable $f$): convex iff
$$f(y) \ge f(x) + \nabla f(x)^\top (y - x) \quad \forall x, y$$
— the function lies above every tangent plane (the gradient gives a **global underestimator**).

**Second-order characterization** (twice-differentiable): convex iff the **Hessian** $\nabla^2 f(x) \succeq 0$ (positive semidefinite) everywhere on the domain.

| Convexity-preserving operation | Why it matters |
|--------------------------------|----------------|
| Nonnegative weighted sum | Sum of convex losses is convex |
| Pointwise maximum/supremum | $\max$ of convex (e.g., hinge loss) is convex |
| Composition with affine map | $f(Ax+b)$ convex if $f$ is |
| Partial minimization over a convex jointly-convex fn | Marginalization stays convex |

**Norms are convex** (triangle inequality + homogeneity); so $\ell_1$, $\ell_2$, $\ell_\infty$ regularizers are convex. **Affine functions are both convex and concave**, which is why LP (linear objective, linear constraints) is the simplest convex problem.

---

## Layer 2: The KKT Conditions

The central optimality result. Consider
$$\min f(x) \quad \text{s.t.}\quad g_i(x) \le 0\ (i=1..m),\quad h_j(x)=0\ (j=1..p).$$

Form the **Lagrangian** $L(x, \lambda, \mu) = f(x) + \sum_i \lambda_i g_i(x) + \sum_j \mu_j h_j(x)$.

**KKT conditions** at a point $x^*$ with multipliers $\lambda^*, \mu^*$:

```
+----------------------------------------------------------------------+
|  (1) STATIONARITY:                                                   |
|      grad f(x*) + sum_i lambda*_i grad g_i(x*)                       |
|                 + sum_j mu*_j grad h_j(x*) = 0                       |
|                                                                      |
|  (2) PRIMAL FEASIBILITY:                                             |
|      g_i(x*) <= 0,    h_j(x*) = 0                                    |
|                                                                      |
|  (3) DUAL FEASIBILITY:                                               |
|      lambda*_i >= 0                                                  |
|                                                                      |
|  (4) COMPLEMENTARY SLACKNESS:                                        |
|      lambda*_i g_i(x*) = 0   for all i                               |
|      (inactive constraint => zero multiplier;                       |
|       positive multiplier  => active constraint)                    |
+----------------------------------------------------------------------+
```

**The precise theorems** (state hypotheses — this is where errors creep in):

| Direction | Statement | Hypotheses |
|-----------|-----------|------------|
| **Necessary** | If $x^*$ is a local min, KKT hold | A **constraint qualification** (CQ) holds at $x^*$ (e.g., LICQ, Slater, or linear constraints) |
| **Sufficient** | If KKT hold, $x^*$ is a **global** min | The problem is **convex** ($f, g_i$ convex, $h_j$ affine) |

```
   CONVEX problem  + KKT satisfied  =>  GLOBAL optimum (certificate!)
   NONCONVEX       + KKT satisfied  =>  only a STATIONARY point
                                        (could be a saddle or local max)
   Local min (any) + a CQ           =>  KKT necessarily hold
```

**Why constraint qualifications are needed**: without a CQ, the gradients of active constraints may be degenerate and stationarity can fail at a true minimum. Common CQs:
- **LICQ**: gradients of active constraints are linearly independent.
- **Slater's condition** (convex problems): a strictly feasible point exists ($\exists x: g_i(x) < 0$). Slater also guarantees **strong duality** (zero gap).
- **Linearity CQ**: all constraints affine ⟹ no further CQ needed (this is why LP's KKT — i.e., complementary slackness, file 02 — needs no qualification).

**Bridge — KKT generalizes LP duality**: for an LP, KKT *is* exactly {primal feasibility, dual feasibility, complementary slackness} from file 02. The Lagrange multipliers $\lambda_i$ are the dual variables / shadow prices. KKT is the nonlinear lift of the LP duality machinery.

---

## Layer 3: Lagrangian Duality (the unifying frame)

The Lagrangian gives a **dual function** by minimizing out $x$:
$$g(\lambda, \mu) = \inf_x L(x, \lambda, \mu).$$
This $g$ is **always concave** (an infimum of affine functions of $(\lambda,\mu)$), regardless of whether the primal is convex. The **dual problem** is $\max_{\lambda \ge 0, \mu} g(\lambda, \mu)$.

```
   WEAK DUALITY (always):     g(lambda, mu) <= f(x*)   = p*
   DUAL OPTIMUM:              d* = max g(lambda, mu) <= p*
   DUALITY GAP:              p* - d* >= 0

   STRONG DUALITY (gap = 0):  holds if CONVEX + Slater's condition
                              (or other CQ). NONCONVEX: gap may be > 0.
```

| Problem class | Duality gap |
|---------------|-------------|
| LP (feasible, finite) | Zero (no CQ needed) |
| Convex + Slater | Zero |
| Convex, Slater fails | May be positive |
| Nonconvex | Generally positive |

**This is the precise generalization of file 02.** LP strong duality is the special case where the gap is always zero under mere feasibility; the general convex case needs Slater; the nonconvex case can have a real gap — which is exactly why duality-based bounds (Lagrangian relaxation, file 03) give *bounds* not exact values for hard problems.

**Bridge to ML — the SVM dual**: the support vector machine is a convex QP; its Lagrangian dual is where the data appear only through inner products $x_i^\top x_j$, which you replace with a kernel $K(x_i, x_j)$ — the **kernel trick**. Slater's condition holds, so strong duality gives the same optimum. See `machine-learning-theory/`.

---

## Layer 4: Algorithms — Unconstrained

```
+----------------------------------------------------------------------+
|              ALGORITHM LADDER (unconstrained min f)                  |
|                                                                      |
|  GRADIENT DESCENT      x_{k+1} = x_k - t_k grad f(x_k)               |
|    first-order; cheap step; linear convergence on strongly convex;  |
|    O(1/k) on convex smooth, O(1/k^2) with Nesterov acceleration.    |
|                                                                      |
|  NEWTON'S METHOD       x_{k+1} = x_k - [Hess f]^-1 grad f            |
|    second-order; QUADRATIC local convergence; costly Hessian solve. |
|                                                                      |
|  QUASI-NEWTON (BFGS)   approximate Hessian from gradient history;   |
|    superlinear; the practical sweet spot for smooth medium-scale.  |
|                                                                      |
|  STOCHASTIC GRADIENT   x_{k+1} = x_k - t_k grad f_i(x_k) (sampled)  |
|    the engine of large-scale ML; noisy but cheap per step.          |
+----------------------------------------------------------------------+
```

| Method | Order | Local rate | Per-step cost |
|--------|-------|-----------|---------------|
| Gradient descent | 1st | Linear (strongly convex); $O(1/k)$ (convex smooth) | $\nabla f$ |
| Nesterov accelerated GD | 1st | $O(1/k^2)$ (convex smooth) — optimal first-order | $\nabla f$ |
| Newton | 2nd | Quadratic | $\nabla^2 f$ + solve |
| BFGS / L-BFGS | quasi-2nd | Superlinear | $\nabla f$ + rank-2 update |
| SGD | 1st (stochastic) | $O(1/k)$ (convex), sublinear | one sample gradient |

**Convergence rate facts (state them right):**
- On **$L$-smooth convex** $f$, gradient descent with step $1/L$ achieves $f(x_k) - f^* = O(1/k)$.
- On **$\mu$-strongly convex** $f$, it converges **linearly** (geometric): error $\sim (1 - \mu/L)^k$. The ratio $\kappa = L/\mu$ (condition number) governs speed.
- **Nesterov acceleration** improves the convex-smooth rate to $O(1/k^2)$ — provably optimal for first-order methods (Nemirovski–Yudin lower bound).
- **Newton** converges **quadratically** near the optimum (error squares each step) but each step costs a Hessian solve.

**Bridge to numerical methods**: Newton's method, conjugate gradient, and the linear-algebra cost of Hessian solves are developed in `numerical-methods/` (linear systems, optimization). Gradient descent on a quadratic *is* an iterative linear solver in disguise.

---

## Layer 5: Algorithms — Constrained and Interior-Point

For constrained convex problems, two dominant families:

```
   INTERIOR-POINT (barrier) METHODS
   --------------------------------
   Replace inequality g_i(x) <= 0 with a LOG-BARRIER penalty:
       min f(x) - (1/t) sum_i log(-g_i(x))
   The -log(-g_i) blows up as g_i -> 0, keeping x strictly feasible.
   Solve for increasing t (barrier vanishes); iterates trace the
   CENTRAL PATH to the boundary optimum.

      feasible region
      +---------------+
      | t small  o    |   o = current iterate (deep interior)
      |          |    |
      | t large  o    |   path follows central path
      |          v    |
      | t -> inf  *<--+   * = optimum on the boundary
      +---------------+
```

**Complexity (precise):** for **self-concordant barriers** (Nesterov–Nemirovski theory), a primal-dual interior-point method reaches an $\epsilon$-accurate solution in $O(\sqrt{\nu}\,\log(1/\epsilon))$ Newton iterations, where $\nu$ is the barrier parameter (e.g., $\nu = m$ for $m$ linear inequalities). Each Newton step solves a linear system. This is the **polynomial-time** guarantee for LP (file 01) and convex programming — Karmarkar's 1984 method is an interior-point method.

| Constrained method | Idea | Note |
|--------------------|------|------|
| **Interior-point / barrier** | log-barrier + Newton on central path | Polynomial; standard for LP/QP/SOCP/SDP |
| **Projected gradient** | gradient step then project onto feasible set | Simple when projection is cheap (box, simplex) |
| **Proximal / prox-gradient (ISTA/FISTA)** | gradient on smooth part + prox on nonsmooth | LASSO ($\ell_1$), the ML workhorse |
| **ADMM** | split + augmented Lagrangian + alternating | Distributed/decomposable convex problems |
| **Sequential Quadratic Programming (SQP)** | solve a QP approximation each step | General (nonconvex) NLP |

**Bridge — projected/proximal gradient ↔ ML regularization**: training a LASSO ($\min \|Ax-b\|^2 + \lambda\|x\|_1$) uses proximal gradient (ISTA/FISTA), where the prox of $\ell_1$ is soft-thresholding. This convex-optimization toolkit is the mathematical core of regularized ML — see `machine-learning-theory/`.

---

## Layer 6: The Convex Problem Hierarchy

Convex optimization is not one problem but a tower of increasingly general cones, each solvable by interior-point methods:

```
   LP    subset of   QP    subset of   SOCP   subset of   SDP
   ---              ---               ----                ---
   linear obj +     convex quadratic  second-order        linear obj over
   linear constr    obj + linear      cone constraints    positive-semidef
                    constr            ||Ax+b|| <= c'x+d   matrices X >= 0
                                                          (X symmetric PSD)

   Each is a special case of conic programming over a symmetric cone.
   All solvable in polynomial time by interior-point methods.
```

| Class | Cone | Example application |
|-------|------|---------------------|
| LP | nonnegative orthant | resource allocation (files 01–02) |
| QP | + quadratic objective | portfolio (Markowitz), SVM, least squares |
| SOCP | second-order (Lorentz) cone | robust LP, antenna design |
| SDP | PSD matrix cone | relaxations of combinatorial problems (Max-Cut), control (LMIs) |

**Bridge to control theory**: linear matrix inequalities (LMIs) — the SDP layer — are the modern language of robust control and Lyapunov stability; see `control-theory/`. **Bridge to integer programming**: SDP relaxations (e.g., Goemans–Williamson for Max-Cut, 0.878-approximation) are tighter than LP relaxations for some combinatorial problems (file 03).

---

## Old World → Convex Optimization Bridges

| You already know | Convex-optimization analogue |
|------------------|------------------------------|
| Gradient descent in model training | The canonical first-order convex method |
| Least-squares fitting | An unconstrained convex QP (normal equations) |
| Lagrange multipliers from calculus | The multipliers in KKT / the dual variables |
| "Local minimum trap" worry in deep nets | The nonconvex regime — no global guarantee |
| Regularization (L1/L2) | Convex penalty terms; prox-gradient solves them |
| Hyperparameter sweep (nonconvex, black-box) | When KKT/gradients don't apply → global/heuristic methods |
| Condition number of a matrix | $\kappa = L/\mu$ governs gradient-descent speed |

The conceptual upgrade: in LP you got a vertex and a certificate; in convex optimization you get an interior optimum and the **KKT certificate**. Both are duality-based proofs of optimality. The reason convex problems are "solved" and deep learning is "trained" is exactly the convex/nonconvex line.

---

## Decision Cheat Sheet

| Situation | Method |
|-----------|--------|
| Linear obj + linear constraints | LP — simplex or interior-point (file 01) |
| Convex quadratic objective | QP — interior-point |
| Smooth unconstrained convex, large scale | Gradient descent / L-BFGS |
| Want optimal first-order rate | Nesterov acceleration ($O(1/k^2)$) |
| Constrained convex, need polynomial guarantee | Interior-point (barrier) |
| $\ell_1$ / nonsmooth regularizer | Proximal gradient (ISTA/FISTA) |
| Distributed / decomposable | ADMM |
| Nonconvex smooth NLP | SQP / trust-region → stationary point only |
| Robust / cone constraints | SOCP or SDP |
| Need to certify global optimality | Check KKT **and** confirm convexity |
| Problem is nonconvex | Accept local optimum, or use global/heuristic (multistart, etc.) |

---

## Common Confusion Points

### "Are KKT conditions necessary or sufficient?"

Both, in different regimes — state which:
- **Necessary** for *any* local min, **provided a constraint qualification holds** (e.g., LICQ, Slater, or all-affine constraints).
- **Sufficient for a global optimum** *only when the problem is convex*. For a nonconvex problem, a KKT point may be a saddle or local max — KKT is necessary but not sufficient there. Never claim "KKT ⟹ optimal" without the convexity hypothesis.

### "Does strong duality always hold for convex problems?"

No — it needs a **constraint qualification**, most commonly **Slater's condition** (a strictly feasible point exists). A convex problem where Slater fails can have a positive duality gap. LP is the exception: strong duality holds under mere feasibility, no CQ (because constraints are affine). For nonconvex problems, expect a gap.

### "Convex vs. linear — what's the actual dividing line?"

**Convexity** is the dividing line between tractable and intractable continuous optimization; **linearity** is just the simplest convex case. A nonlinear *convex* problem (e.g., SVM, LASSO, SDP) is polynomially solvable. A nonconvex problem (deep net, general NLP) is NP-hard in general. Don't conflate "nonlinear" with "hard" — conflate "nonconvex" with "hard."

### "Why interior-point and not simplex for these?"

Simplex only applies to LP (it walks polytope vertices). Convex QP/SOCP/SDP have curved feasible regions with no vertex structure, so interior-point (which follows the smooth central path via Newton steps) is the natural and polynomial method. For LP specifically, both work; for general convex programs, interior-point is the unifying engine.

### "Gradient descent convergence — linear or $O(1/k)$?"

Depends on the function class. On **strongly convex smooth** $f$: **linear** (geometric) convergence, rate governed by condition number $\kappa = L/\mu$. On merely **convex smooth** $f$: sublinear $O(1/k)$, improvable to $O(1/k^2)$ with Nesterov acceleration. "Linear convergence" means error shrinks by a constant factor each step (fast); $O(1/k)$ means error $\propto 1/k$ (slow). They are very different — always state the assumed regime.

### "My problem has integer variables AND a convex objective — what is it?"

That is **convex MINLP** (mixed-integer nonlinear programming) — you've combined the integrality of file 03 with the convexity here. It's NP-hard (integrality dominates), solved by branch-and-bound where each node solves a *convex* relaxation (instead of an LP relaxation). The convex relaxations are still polynomial per node, but the tree is exponential.
