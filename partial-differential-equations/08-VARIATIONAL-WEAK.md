# Variational Formulation and Weak Solutions

## The Big Picture

Weak formulations restate a PDE problem as a variational equality that makes sense for
functions with fewer derivatives than the classical formulation requires. This is the
theoretical foundation of the Finite Element Method (FEM).

```
+-----------------------------------------------------------------------+
|              WEAK FORMULATION CONCEPT                                 |
|                                                                       |
|  CLASSICAL (STRONG) FORMULATION:                                      |
|  −∇²u = f in Ω,  u = 0 on ∂Ω                                          |
|  Requires: u ∈ C²(Ω) — twice differentiable                           |
|  What about rough f? Irregular Ω? Discontinuous coefficients?         |
|                                                                       |
|  WEAK FORMULATION:                                                    |
|  ∫_Ω ∇u·∇v dx = ∫_Ω fv dx   for all v ∈ H₀¹(Ω)                        |
|  Requires: u,v ∈ H₀¹(Ω) — just ONE derivative in L²                   |
|                                                                       |
|  KEY STEP: integration by parts ONCE, moving one derivative to v.     |
|  Classical solution ⊂ weak solutions.                                 |
|  Weak solutions may be less smooth — but they exist under             |
|  much weaker hypotheses.                                              |
|                                                                       |
|  FEM CONNECTION:                                                      |
|  Replace: v ∈ H₀¹(Ω) by v ∈ V_h ⊂ H₀¹ (finite-dimensional subspace)   |
|  → Galerkin approximation (linear system Au = b)                      |
|  → This IS the finite element method.                                 |
|                                                                       |
+-----------------------------------------------------------------------+
```

---

## Sobolev Spaces

To make weak formulations rigorous, we need function spaces that track both function
values and derivatives in L².

```
  L²(Ω):  {u : Ω → R : ∫_Ω |u|² dx < ∞}
  Inner product: (u,v) = ∫_Ω uv dx
  Norm: ‖u‖_L² = (∫|u|²)^{1/2}

  H¹(Ω):  {u ∈ L²(Ω) : ∂u/∂x_i ∈ L²(Ω) for all i}
  Norm: ‖u‖_H¹ = (∫|u|² + ∫|∇u|²)^{1/2}

  H^k(Ω) = W^{k,2}(Ω):  all partial derivatives up to order k in L²
  Norm: ‖u‖_{H^k} = (Σ_{|α|≤k} ∫|D^α u|²)^{1/2}

  H₀¹(Ω):  closure of C_c^∞(Ω) in H¹ = {u ∈ H¹ : u|_{∂Ω} = 0}
  (H¹ functions with zero boundary trace)

  POINCARÉ INEQUALITY:
  For bounded Ω: ∃C > 0 such that ‖u‖_L² ≤ C‖∇u‖_L²  for u ∈ H₀¹(Ω)
  → ‖∇u‖_L² is an equivalent norm on H₀¹(Ω)
  → Coercivity for the Dirichlet Laplacian follows automatically.

  SOBOLEV EMBEDDING THEOREM:
  H^k ↪ C^j (bounded embedding) if k − n/2 > j  (n = space dimension)
  In 3D: H² ↪ C⁰ (H² functions are continuous)
         H¹ ↪ L⁶ (H¹ functions are in L⁶, Sobolev exponent p*=2n/(n−2))
```

---

## Deriving the Weak Formulation

### Poisson Equation

```
  STRONG: −∇²u = f in Ω,  u = 0 on ∂Ω

  STEP 1: Multiply both sides by a test function v ∈ H₀¹(Ω):
  −∫_Ω (∇²u) v dx = ∫_Ω f v dx

  STEP 2: Integration by parts (Green's first identity):
  ∫_Ω ∇u · ∇v dx − ∮_{∂Ω} v ∂u/∂n dS = ∫_Ω fv dx

  STEP 3: Since v ∈ H₀¹: v = 0 on ∂Ω, so the boundary term vanishes:
  ∫_Ω ∇u · ∇v dx = ∫_Ω fv dx

  WEAK FORM: Find u ∈ H₀¹(Ω) such that
  ┌──────────────────────────────────────────────────────────────┐
  │  a(u,v) = F(v)   for all v ∈ H₀¹(Ω)                          │
  │  where a(u,v) = ∫_Ω ∇u·∇v dx   (bilinear form)               │
  │  and   F(v)   = ∫_Ω fv dx       (linear functional)          │
  └──────────────────────────────────────────────────────────────┘

  OBSERVATIONS:
  • u appears only with FIRST derivatives (one less than strong form)
  • v also only needs first derivatives
  • No BCs appear explicitly — they're "built in" to H₀¹
  • If u solves the strong form and is smooth, it solves the weak form
  • Weak solution may exist even when strong solution doesn't
```

### General Variable-Coefficient Elliptic

```
  STRONG: −∇·(A(x)∇u) + c(x)u = f in Ω,  u=0 on ∂Ω

  A(x) = diffusion tensor (symmetric, uniformly positive definite)
  c(x) ≥ 0 (reaction coefficient)

  WEAK FORM: Find u ∈ H₀¹(Ω) s.t.
  ∫_Ω [∇v · A∇u + c·uv] dx = ∫_Ω fv dx   for all v ∈ H₀¹

  Bilinear form: a(u,v) = ∫_Ω [∇v · A∇u + c·uv] dx

  UNIFORM ELLIPTICITY: ξ·A(x)ξ ≥ α|ξ|²  for all ξ, x (some α > 0)
  This ensures coercivity: a(u,u) ≥ α‖u‖²_{H₀¹}
  → Lax-Milgram applies → unique weak solution.
```

---

## Finite Element Method: The Full Derivation

FEM is the numerical method that directly discretizes the weak formulation.

```
  STEP 1: TRIANGULATE the domain Ω.
  ┌────────────────────────────────────────────────────────────┐
  │ Mesh T_h: partition Ω into elements (triangles in 2D,      │
  │ tetrahedra in 3D). Mesh size h = max element diameter.     │
  │                                                            │
  │  [*]─[*]─[*]─[*]─[*]                                       │
  │   |\ |\ |\ |\ |\                                           │
  │  [*]─[*]─[*]─[*]─[*]                                       │
  │   |\ |\ |\ |\ |\                                           │
  │  [*]─[*]─[*]─[*]─[*]                                       │
  └────────────────────────────────────────────────────────────┘

  STEP 2: DEFINE FINITE ELEMENT SPACE V_h ⊂ H₀¹(Ω).
  Lagrange P1 elements: piecewise linear, continuous, zero on ∂Ω.
  BASIS FUNCTIONS φ_j: hat functions — φ_j(x_i) = δ_{ij}
  (piecewise linear, = 1 at node j, = 0 at all other nodes)

  STEP 3: GALERKIN APPROXIMATION.
  Replace H₀¹ by V_h in the weak form:
  Find u_h = Σ_j U_j φ_j ∈ V_h such that:
  a(u_h, φ_i) = F(φ_i)   for all basis functions φ_i

  STEP 4: ASSEMBLE LINEAR SYSTEM.
  This becomes AU = b where:
  A_{ij} = a(φ_j, φ_i) = ∫_Ω ∇φ_i · ∇φ_j dx    (STIFFNESS MATRIX)
  b_i    = F(φ_i)       = ∫_Ω f φ_i dx           (LOAD VECTOR)

  STEP 5: SOLVE Au = b.
  A is symmetric positive definite (from coercivity of a).
  A is SPARSE (φ_i, φ_j have overlapping support only when nodes i,j
  are in the same element) → sparse linear solvers.

  STEP 6: RECOVER SOLUTION.
  u_h(x) = Σ_j U_j φ_j(x)
```

---

## Error Analysis: Céa's Lemma

```
  CÉA'S LEMMA:

  ‖u − u_h‖_{H¹} ≤ (M/α) · min_{v_h ∈ V_h} ‖u − v_h‖_{H¹}

  where M = continuity constant of a, α = coercivity constant.

  INTERPRETATION:
  The FEM error is (M/α) times the BEST APPROXIMATION error
  from V_h to the exact solution u.

  FEM quasi-optimally approximates u from within V_h.

  For piecewise linear elements (P1) and u ∈ H²(Ω):
  ‖u − u_h‖_{H¹} ≤ C·h·‖u‖_{H²}    (first-order convergence in H¹)
  ‖u − u_h‖_{L²} ≤ C·h²·‖u‖_{H²}   (second-order in L²)

  For P_k elements: O(h^k) in H¹, O(h^{k+1}) in L².

  AUBIN-NITSCHE TRICK:
  The improved L² estimate comes from a duality argument:
  ‖e‖_{L²} = sup_{g} (e,g)/‖g‖ = ... ≤ C·h·‖e‖_{H¹} ≤ C·h²·‖u‖_{H²}
```

---

## Weak Solutions for Parabolic Equations

```
  HEAT EQUATION WEAK FORMULATION:

  Strong: u_t − α∇²u = f in Q_T = Ω×(0,T), u(x,0) = u₀, u=0 on ∂Ω

  SPACE: V = H₀¹(Ω),  H = L²(Ω)
  Gelfand triple: V ⊂ H ≅ H* ⊂ V*

  WEAK FORM: Find u ∈ L²(0,T;H₀¹) with u_t ∈ L²(0,T;H⁻¹) such that

  d/dt (u,v)_H + α·a(u,v) = ⟨f,v⟩   for a.e. t ∈ (0,T)
  u(0) = u₀

  where (u,v)_H = ∫_Ω uv dx  and  a(u,v) = ∫_Ω ∇u·∇v dx.

  EXISTENCE (Galerkin method):
  1. Discretize in x: Galerkin in space → ODE system u_h'(t) + A·u_h(t) = f_h(t)
  2. Solve ODE → solutions u_h_n
  3. Take limit h→0, n→∞ (compactness arguments)
  → Weak solution u ∈ L²(0,T;H₀¹) with u_t ∈ L²(0,T;H⁻¹) exists.

  REGULARITY: if u₀ ∈ H₀¹ and f ∈ L²(Q_T), then u ∈ H¹(0,T;L²) ∩ L²(0,T;H²).
```

---

## Hyperbolic Weak Solutions: Shocks

```
  For conservation laws u_t + f(u)_x = 0:

  CLASSICAL SOLUTION: smooth, satisfies PDE everywhere.
  Can break down at time t_break when characteristics cross.

  WEAK SOLUTION: Find u ∈ L^∞ such that
  ∫∫ [u·φ_t + f(u)·φ_x] dx dt + ∫ u₀(x)φ(x,0) dx = 0
  for all φ ∈ C_c^∞(R × [0,∞))

  Allows DISCONTINUITIES. Permits shock solutions.
  But weak solutions are NOT unique in general.

  ENTROPY CONDITION (additional selection criterion):
  ∂_t η(u) + ∂_x q(u) ≤ 0  (in distributional sense)
  for all convex entropy η with entropy flux q' = η'f'.

  This selects the unique "physical" (entropy) weak solution.

  RANKINE-HUGONIOT at a shock (speed s):
  s[u] = [f(u)]  (brackets = jump across shock)
  s(u_R − u_L) = f(u_R) − f(u_L)
```

---

## From Weak Formulation to Finite Element: Summary

```
  +-------------------+
  | STRONG PDE        |  −∇·(A∇u) + cu = f in Ω
  +-------------------+
          |
          | Multiply by test fn v, integrate by parts
          v
  +-------------------+
  | WEAK FORMULATION  |  a(u,v) = F(v)  ∀v ∈ H₀¹
  +-------------------+
          |
          | Abstract: Lax-Milgram → existence/uniqueness
          v
  +-------------------+
  | GAP: V_h ⊂ H₀¹   |  Finite-dimensional subspace
  | Galerkin method   |  a(u_h,v_h) = F(v_h)  ∀v_h ∈ V_h
  +-------------------+
          |
          | Basis expansion: u_h = Σ U_j φ_j
          v
  +-------------------+
  | LINEAR SYSTEM     |  A U = b  (A sparse, SPD)
  | Stiffness + load  |
  +-------------------+
          |
          | Céa's lemma → quasi-optimality
          v
  +-------------------+
  | ERROR ESTIMATE    |  ‖u−u_h‖_{H¹} = O(h^k)  for P_k elements
  +-------------------+
```

---

## Neural Methods as Variational Approaches

PINNs and neural operators are direct descendants of the variational framework. Understanding their connection to weak formulations explains both their power and their failure modes.

```
VARIATIONAL / WEAK FORM → NEURAL METHODS
═════════════════════════════════════════════════════════════════════

FEM (classical):
  V_h = span{φ₁,...,φ_N}   (piecewise polynomial basis)
  Find u_h ∈ V_h:  a(u_h, v_h) = F(v_h)  ∀v_h ∈ V_h
  → Stiffness matrix A·c = b;  solve linear system.
  Céa's lemma: ‖u−u_h‖ ≤ (M/α) inf_{v∈V_h} ‖u−v‖

PINN (strong-form residual):
  V_θ = {u_θ(x) : θ ∈ ℝᵖ}  (neural network parameterization)
  Loss: L(θ) = Σ_i |−∇²u_θ(x_i) − f(x_i)|²  + λ · BC penalty
  Gradients: ∂L/∂θ via automatic differentiation through PDE operator.
  No mesh. No linear system. Just gradient descent on the residual.

DEEP RITZ METHOD (variational/energy form):
  Minimize the energy functional directly:
  J[u_θ] = ½ a(u_θ, u_θ) − F(u_θ)
         = ½ ∫|∇u_θ|² dx − ∫ f·u_θ dx
  This IS the Ritz method with a neural network as the trial function.
  Same energy minimization as FEM, different function class.

DEEP GALERKIN METHOD (weak form):
  Test against random test functions v_k:
  Loss = E_v[ |a(u_θ, v) − F(v)|² ]
  Stochastic: sample test functions randomly at each iteration.

WHY PINNs CAN FAIL — VARIATIONAL PERSPECTIVE:
  Céa's lemma requires coercivity: a(u,u) ≥ α‖u‖²
  PINN loss landscape is NON-CONVEX (nonlinear parameterization).
  No analogue of Céa's lemma → no guaranteed approximation quality.
  Spectral bias: networks learn low-frequency modes first (related
  to the eigenvalue spectrum of the NTK — neural tangent kernel).
  Stiff PDEs (large condition number of A) → optimization difficulty.
```

The key insight: FEM trades expressiveness for guarantees (piecewise polynomials are limited but analyzable). Neural methods trade guarantees for expressiveness (universal approximation but non-convex optimization). Understanding the variational framework — coercivity, Céa's lemma, energy minimization — is what explains when each approach is appropriate. See `09-NUMERICAL-PDES.md` for the full comparison table.

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| Why use weak formulations? | Less regularity required; foundation of FEM; handles non-smooth data |
| What is H₀¹(Ω)? | H¹ functions with zero trace on ∂Ω; the natural space for Dirichlet problems |
| What is the stiffness matrix A? | A_{ij} = ∫_Ω ∇φ_i·∇φ_j dx (also: A_{ij} = a(φ_j,φ_i)) |
| Is A symmetric? | Yes, if a(u,v) = a(v,u) (always for Laplace/Poisson) |
| Is A positive definite? | Yes, from coercivity of a(u,u) ≥ α‖u‖² |
| FEM error order for P1? | O(h) in H¹, O(h²) in L² |
| Weak solution for conservation law? | Integral form; non-unique without entropy condition |
| What is the Poincaré inequality? | ‖u‖_L² ≤ C‖∇u‖_L² for u ∈ H₀¹ on bounded Ω |
| What is Lax-Milgram used for? | Proving existence/uniqueness of weak solutions |

---

## Common Confusion Points

**"The weak formulation loses the BCs — they don't appear in the equation anymore."**
Dirichlet BCs are "essential" — they're encoded in the function space H₀¹(Ω) (the zero
boundary condition is part of the definition of the space). Neumann BCs are "natural" —
they appear naturally as boundary terms when you integrate by parts, and are automatically
satisfied by the weak formulation without imposing them explicitly. This is the essential vs.
natural BC distinction fundamental to variational methods.

**"Sobolev spaces have non-integer order H^s — what does that mean?"**
H^s for non-integer s is defined by interpolation or by the Fourier transform:
‖u‖²_{H^s} = ∫ (1 + |k|²)^s |û(k)|² dk.
For s = 1/2: this is the trace space on the boundary (what functions on ∂Ω look like when
restricted from H¹). The trace theorem says the restriction map H¹(Ω) → H^{1/2}(∂Ω) is
bounded and surjective. Relevant for non-homogeneous Dirichlet BCs.

**"FEM gives a sparse matrix A. Is that the only reason to use it over finite differences?"**
FEM has several advantages beyond sparsity: it handles irregular geometries naturally
(the mesh conforms to ∂Ω), it provides a rigorous error theory via Céa's lemma, it handles
variable and anisotropic coefficients A(x) seamlessly, and h/p adaptivity (refine the mesh
or increase polynomial degree where needed) is natural. Finite differences are simpler but
struggle with complex domains and variable coefficients.
