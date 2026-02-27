# Numerical Optimization

## The Big Picture

Optimization finds the minimum (or maximum) of an objective function, possibly subject to constraints. The landscape ranges from convex problems with global convergence guarantees to non-convex problems where local methods are all we have.

```
+------------------------------------------------------------------+
|                    OPTIMIZATION TAXONOMY                         |
+------------------------------------------------------------------+
|                                                                  |
|  UNCONSTRAINED                    CONSTRAINED                   |
|  +---------------------+          +----------------------+      |
|  | CONVEX              |          | LINEAR PROGRAMMING   |      |
|  | Gradient descent    |          | (Simplex, Interior   |      |
|  | Conjugate gradient  |          |  Point)              |      |
|  | Newton's method     |          +----------------------+      |
|  | BFGS / L-BFGS       |          | CONVEX QP / SDP      |      |
|  +---------------------+          | (Interior point)     |      |
|  | NON-CONVEX          |          +----------------------+      |
|  | Local minima only   |          | NONLINEAR CONSTRAINED|      |
|  | Same methods but    |          | (SQP, IPM, ADMM)     |      |
|  | no global guarantee |          +----------------------+      |
|  +---------------------+                                        |
|                                                                  |
|  STOCHASTIC / GLOBAL                                            |
|  +---------------------------------------------+               |
|  | SGD, Adam, RMSprop (ML training)             |               |
|  | Simulated annealing, genetic algorithms      |               |
|  | Bayesian optimization (expensive objectives) |               |
|  +---------------------------------------------+               |
+------------------------------------------------------------------+
```

---

## Gradient Descent and Variants

**Gradient descent** (steepest descent):

```
  x_{k+1} = x_k - alpha_k * nabla f(x_k)

  alpha_k: step size (learning rate).

  CONVERGENCE (convex f with L-Lipschitz gradient):
  Fixed step: alpha = 1/L
  f(x_k) - f(x*) <= L ||x_0 - x*||^2 / (2k)  = O(1/k)

  STRONG CONVEXITY (sigma-strongly convex, L-smooth):
  Linear convergence: ||x_k - x*||^2 <= (1 - sigma/L)^k ||x_0 - x*||^2
  Contraction factor: (1 - sigma/L) = (kappa - 1)/(kappa + 1) where kappa = L/sigma.
  High condition number kappa: very slow convergence.
```

**Gradient descent with line search**:

```
  BACKTRACKING (Armijo condition):
  Start with alpha = alpha_0.
  While f(x - alpha nabla f(x)) > f(x) - c1 alpha ||nabla f||^2:
    alpha <- alpha * rho   (reduce step)

  WOLFE CONDITIONS (for quasi-Newton methods):
  Armijo: f(x + alpha d) <= f(x) + c1 alpha nabla f^T d        (sufficient decrease)
  Curvature: |nabla f(x + alpha d)^T d| <= c2 |nabla f(x)^T d|  (strong curvature)
  c1 in (0,1), c2 in (c1, 1). Guarantees positive-definite updates for BFGS.
```

**Accelerated gradient methods (Nesterov momentum)**:

```
  Nesterov Accelerated Gradient (NAG):
  y_k = x_k + (k-1)/(k+2) (x_k - x_{k-1})    (momentum step)
  x_{k+1} = y_k - alpha nabla f(y_k)           (gradient step)

  CONVERGENCE: O(1/k^2) instead of O(1/k) for convex smooth f.
  Optimal for gradient methods (no first-order method does better for smooth convex).
  The (k-1)/(k+2) factor is the "momentum coefficient" -- increases toward 1 over time.
```

---

## Newton and Quasi-Newton Methods

**Newton's method** uses second-order information:

```
  x_{k+1} = x_k - (nabla^2 f(x_k))^{-1} nabla f(x_k)

  = x_k - H_k^{-1} g_k   where H = Hessian, g = gradient

  CONVERGENCE: Quadratic near a minimizer x* (where H(x*) is positive definite):
  ||x_{k+1} - x*|| <= C ||x_k - x*||^2

  Double the precision at each step near the solution.

  COST: O(n^3) per iteration (compute and factor H).
  For large n: impractical.

  ISSUES:
  Far from x*: Hessian may not be positive definite -> Newton step may increase f.
  Fix: modify Hessian (add positive multiple of I to ensure PD).
```

**Quasi-Newton methods (BFGS)**:

```
  Approximate H by a positive-definite matrix B_k, updated cheaply:

  BFGS UPDATE:
  s_k = x_{k+1} - x_k     (step)
  y_k = g_{k+1} - g_k     (gradient change)
  B_{k+1} = B_k - (B_k s_k s_k^T B_k) / (s_k^T B_k s_k) + (y_k y_k^T) / (y_k^T s_k)

  SECANT CONDITION: B_{k+1} s_k = y_k (approximate Hessian-vector product)
  B_{k+1} remains positive definite if y_k^T s_k > 0 (guaranteed by Wolfe line search).

  CONVERGENCE: Superlinear near x* (between linear and quadratic).
  COST: O(n^2) per iteration (matrix-vector product).

  L-BFGS (Limited-memory BFGS):
  Don't store B_k explicitly (n x n matrix).
  Store last m (s_k, y_k) pairs (m = 5-20 typically).
  Compute H^{-1} g using two-loop recursion in O(mn) time.
  Memory: O(mn) instead of O(n^2).
  THE STANDARD for large-scale unconstrained optimization (n > 10^4).
  scipy.optimize.minimize(method='L-BFGS-B').
```

---

## Stochastic Gradient Descent and ML Optimizers

For ML training where f(x) = (1/N) Sum_{i=1}^N f_i(x) (sum over training examples):

```
  FULL GRADIENT: nabla f = (1/N) Sum nabla f_i  -- O(N) per step, exact.
  STOCHASTIC GRADIENT: use one sample or mini-batch:
  g_k = (1/|B|) Sum_{i in B_k} nabla f_i(x_k)   (mini-batch B_k)

  SGD: x_{k+1} = x_k - alpha_k g_k

  WHY SGD WORKS: E[g_k] = nabla f(x_k)  (unbiased gradient estimate).
  By LLN + CLT (03-LIMIT-THEOREMS): mini-batch gradient is noisy but correct on average.

  CONVERGENCE FOR CONVEX f (diminishing step sizes alpha_k = a/(k+b)):
  E[f(x_k)] - f(x*) = O(1/sqrt(k)) for non-smooth convex.
  E[f(x_k)] - f(x*) = O(log(k)/k) for smooth convex.
  MUCH SLOWER than GD's O(1/k) -- but each step costs O(N/k) less work.

  For N >> 1: SGD reaches epsilon accuracy in O(1/epsilon) gradient evaluations;
  full GD needs O(1/epsilon) steps but each costs O(N).
  For epsilon >> 1/sqrt(N): SGD wins. For epsilon << 1/sqrt(N): GD can win.
```

**Adaptive methods**:

```
  ADAGRAD: per-parameter adaptive learning rate.
  G_k += g_k^2  (accumulate squared gradients, element-wise)
  x_{k+1} = x_k - alpha / sqrt(G_k + eps) * g_k

  Problem: G_k grows without bound -> learning rate shrinks to 0.

  RMSPROP (Hinton): exponential moving average of squared gradients.
  v_k = beta v_{k-1} + (1-beta) g_k^2
  x_{k+1} = x_k - alpha / sqrt(v_k + eps) * g_k

  ADAM (Adaptive Moment Estimation):
  m_k = beta1 m_{k-1} + (1-beta1) g_k          (1st moment estimate)
  v_k = beta2 v_{k-1} + (1-beta2) g_k^2         (2nd moment estimate)
  m_hat = m_k / (1 - beta1^k)                   (bias correction)
  v_hat = v_k / (1 - beta2^k)                   (bias correction)
  x_{k+1} = x_k - alpha m_hat / (sqrt(v_hat) + eps)

  Default: beta1=0.9, beta2=0.999, alpha=0.001, eps=1e-8.
  CURRENT STANDARD for deep learning. Robust across architectures.
  Connection to natural gradient: Adam approximates diagonal Fisher preconditioning.
```

---

## Convex Optimization

**Convex problems** have no local minima — every local minimum is global. Interior point methods solve them to arbitrary precision.

**Linear Programming (LP)**:

```
  min c^T x  s.t.  Ax <= b, x >= 0

  Feasible set: convex polytope (intersection of half-spaces).
  Optimal solution: at a vertex of the polytope (or on an edge/face for degenerate cases).

  SIMPLEX METHOD (Dantzig 1947):
  Move from vertex to adjacent vertex along edges, improving objective.
  Worst case: exponential in n (Klee-Minty), but practically very fast.

  INTERIOR POINT (Karmarkar 1984):
  Follow the "central path" through the interior of the polytope.
  Polynomial time: O(n^{3.5} L) for bit-complexity L.
  For large-scale LP: usually faster than simplex in practice.

  SIMPLEX vs. IP in practice:
  Simplex: warm-starting efficient, good for re-optimization.
  IP: better for very large problems, no warm-start advantage.
```

**Semidefinite Programming (SDP)**:

```
  min tr(C X)  s.t.  tr(A_i X) = b_i, X >= 0  (X positive semidefinite)

  Generalizes LP and quadratic programming.
  Applications: MAX-CUT relaxation, SOS relaxation, optimal control, robust optimization.
  Solvers: SeDuMi, MOSEK, SDPT3.
  Interior point method: O(n^6) worst case (n x n matrix variable).
```

**Proximal methods and ADMM**:

```
  For composite problems: min f(x) + g(x)
  where f is smooth (has gradient) and g is non-smooth but has a "prox operator."

  Proximal gradient method:
  x_{k+1} = prox_{alpha g}(x_k - alpha nabla f(x_k))

  prox_{alpha g}(v) = argmin_x {g(x) + (1/2alpha)||x-v||^2}

  EXAMPLE: Lasso (g = lambda||x||_1):
  prox_{alpha lambda||.||_1}(v) = soft-threshold(v, alpha lambda)
  (component-wise: sign(v) * max(0, |v| - alpha lambda))

  ADMM (Alternating Direction Method of Multipliers):
  Splits composite problems across computational nodes.
  min f(x) + g(z) s.t. Ax + Bz = c
  Distributed optimization across many machines.
  Used in large-scale ML, distributed signal processing.
```

---

## Derivative-Free and Global Methods

**Nelder-Mead simplex** (derivative-free):

```
  Maintains a simplex of n+1 points. Reflects, expands, contracts the simplex.
  No gradients needed.
  Convergence: slow (O(1/k) at best for convex). Often sub-linear.
  Use when: gradients unavailable, n < 50, moderate accuracy.
```

**Simulated annealing** (global, stochastic):

```
  At "temperature" T: accept worse solution with probability exp(-delta/T).
  Slowly reduce T (cooling schedule).

  INSPIRED BY: physical annealing (metal cooling slowly forms crystal).
  CONVERGENCE: Theoretically converges to global minimum if cooling is slow enough
  (T_k ~ 1/log(k)). In practice: finite budget, approximate solution.
  USEFUL FOR: Discrete optimization, combinatorial problems.
```

**Bayesian optimization** (for expensive black-box functions):

```
  Model f with a Gaussian process surrogate.
  Choose next evaluation point by maximizing an acquisition function:
  Expected Improvement: EI(x) = E[max(f(x) - f_best, 0)]
  Upper Confidence Bound: UCB(x) = mu(x) + beta * sigma(x)

  WORKFLOW:
  1. Evaluate f at a few initial points.
  2. Fit GP model to observed (x_i, f_i).
  3. Maximize acquisition function to choose x_new.
  4. Evaluate f(x_new).
  5. Update GP, repeat.

  CONVERGENCE: O(n^{-1/(d+4)}) for d-dimensional smooth f (slow, but each
  evaluation is "expensive" -- f could be a 10-hour simulation).
  USED FOR: Hyperparameter tuning (Azure ML AutoML, Optuna, Hyperopt).
  Can take the gradient of the acquisition function (it is analytic) -> use L-BFGS inside.
```

---

<!-- @editor[content/P2]: Manifold / Riemannian optimization is absent. The 00-OVERVIEW module map explicitly lists "Manifold optimization (Riemannian SGD)" under 08-OPTIMIZATION. This is a significant gap: optimization on manifolds (Stiefel manifold for orthogonal constraints, positive-definite cone for covariance matrices, hyperbolic space for embeddings) is increasingly important in ML and physics. The section is not stubbed — it simply does not exist. -->

## Connection to ML Training

The gradient descent machinery above is exactly what trains neural networks:

```
  ML TRAINING LOOP (abstract):
  Initialize weights theta_0.
  For k = 1, 2, ... until convergence:
    Sample mini-batch B.
    Compute gradient g_k = (1/|B|) Sum_{i in B} nabla L(f(x_i; theta_k), y_i)
    Update: theta_{k+1} = optimizer_step(theta_k, g_k)

  The optimizer step is gradient descent, momentum, or Adam.
  g_k is computed by BACKPROPAGATION (reverse-mode automatic differentiation).
  Loss surface is non-convex; we find local (hopefully good) minima.
<!-- @editor[bridge/P1]: Backpropagation is mentioned but there is no AD → backpropagation bridge. The learner explicitly needs automatic differentiation. The statement "g_k is computed by BACKPROPAGATION (reverse-mode automatic differentiation)" is a one-liner where a bridge belongs: forward mode vs. reverse mode, why reverse mode is O(cost of f) regardless of parameter count, and how this means the cost of computing the full gradient of a billion-parameter model is just ~3x a single forward pass. This is the key insight that makes deep learning computationally tractable — it deserves a paragraph, not a parenthetical. -->

  LEARNING RATE SCHEDULES:
  Constant: works if tuned. Sensitive.
  Cosine annealing: decreases from alpha_max to alpha_min following cosine curve.
  Warmup + cosine: start from very small lr, ramp up, then cosine decay.
  One-cycle policy: Super-Convergence (Smith 2017) -- peak once in training.

  BATCH SIZE EFFECTS (linear scaling rule):
  Double batch size -> double learning rate (same number of effective steps).
  Breaks down for very large batches (optimization vs. generalization tradeoff).
  Large batch training (distributed): gradient synchronization is the bottleneck.
```

---

## Decision Cheat Sheet

| Problem | Method | Notes |
|---|---|---|
| Small-scale unconstrained, smooth | BFGS | Full Hessian approximation |
| Large-scale unconstrained, smooth | L-BFGS | 5-20 vector pairs stored |
| Very large scale (ML), noisy | Adam / AdamW | Default for deep learning |
| Convex, unconstrained | Nesterov accelerated GD | Optimal first-order method |
| LP | Simplex or Interior Point | Both in scipy, GLPK, Gurobi |
| QP | Active set or IPM | Quadprog, OSQP, Gurobi |
| SDP | Interior Point | MOSEK, SeDuMi |
| L1 regularized | Proximal gradient or ADMM | ISTA, FISTA, ADMM |
| Expensive black-box (hyperparams) | Bayesian optimization | Optuna, GPyOpt |
| Combinatorial, non-convex | Simulated annealing or GA | No guarantees |

---

## Common Confusion Points

**"Non-convex problems are unsolvable."**
Non-convex optimization doesn't guarantee finding the global minimum, but good local minima are often sufficient. For deep learning: overparameterized networks have many equivalent global minima and gradient descent reliably finds good solutions. The non-convexity of the loss landscape doesn't prevent excellent generalization in practice.

**"More training data = harder optimization."**
More data improves generalization but also makes each gradient computation more expensive. SGD solves this by using mini-batches. For convex problems, more data (smoother loss landscape) can actually make optimization easier.

**"Adam always outperforms SGD."**
For deep learning: Adam converges faster (fewer iterations to same loss) but SGD with careful tuning often achieves lower final test loss ("Adam adapts fast; SGD generalizes better"). Vision tasks often use SGD with momentum; NLP/transformers strongly favor Adam/AdamW.

**"Second-order methods are overkill for deep learning."**
This is currently true for practical reasons: Hessian is n x n for n parameters (billions for modern networks). But K-FAC (Kronecker-Factored Approximate Curvature) and Shampoo (matrix-valued momentum) approximate the natural gradient and can converge in significantly fewer steps than Adam. As hardware scales, second-order methods are becoming more competitive.
