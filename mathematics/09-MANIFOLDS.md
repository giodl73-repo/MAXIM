# 09 — Manifolds, Differential Forms, and the General Stokes' Theorem

```
THE LANDSCAPE
═══════════════════════════════════════════════════════════════════════════════

  MANIFOLDS                  DIFFERENTIAL FORMS           STOKES' THEOREM
  ┌──────────────────────┐   ┌─────────────────────────┐  ┌──────────────────┐
  │ locally ≅ ℝⁿ         │   │ k-forms: antisymmetric  │  │ ∫_M dω = ∫_∂M ω  │
  │ charts + atlas       │ → │ wedge product ∧         │→ │                  │
  │ smooth transitions   │   │ exterior derivative d   │  │ unifies ALL the  │
  │ Sⁿ, tori, Lie groups │   │ d²= 0                   │  │ integral theorems│
  └──────────────────────┘   └─────────────────────────┘  └──────────────────┘

  THE CHAIN:  Ω⁰ →^d Ω¹ →^d Ω² →^d ··· →^d Ωⁿ →^d 0

  k-FORMS IN ℝ³:
  ┌──────────┬─────────────────────────────────────────────────────────────┐
  │ 0-form   │ scalar field f(x,y,z)                                      │
  │ 1-form   │ covector field: α = P dx + Q dy + R dz                     │
  │ 2-form   │ "flux form": ω = A dy∧dz + B dz∧dx + C dx∧dy             │
  │ 3-form   │ "volume form": f dx∧dy∧dz                                  │
  └──────────┴─────────────────────────────────────────────────────────────┘

  PAYOFF: Maxwell's equations compress to:  dF = 0   and   d★F = J
          Four equations → two lines.
═══════════════════════════════════════════════════════════════════════════════
```

---

## 1. Manifolds

### 1.1 The Definition

An **n-dimensional manifold** M is a topological space that looks locally like ℝⁿ:

```
  Formal definition:
  For every point p ∈ M, there exists:
  ├── An open set U ⊆ M containing p (a "neighborhood")
  └── A homeomorphism φ: U → V ⊆ ℝⁿ (a "coordinate chart")

  The pair (U, φ) is called a chart.
  An atlas is a collection of charts covering all of M.

  SMOOTH MANIFOLD: all transition maps φⱼ ∘ φᵢ⁻¹: ℝⁿ → ℝⁿ are C∞
  (smooth compatibility between overlapping charts)

  EXAMPLES:
  ┌──────────────────────────────────────────────────────────────────────┐
  │  ℝⁿ          dim n  trivial (one chart covers everything)           │
  │  S¹ (circle) dim 1  need ≥2 charts (no single chart covers all)    │
  │  S² (sphere) dim 2  north/south hemisphere charts                   │
  │  Torus T²    dim 2  product of two circles                          │
  │  SO(3)       dim 3  rotation matrices (Lie group)                   │
  │  SU(2)       dim 3  unitary 2×2 matrices, det=1 (≅ S³)             │
  │  Spacetime   dim 4  Lorentzian manifold (pseudo-Riemannian)         │
  │  Calabi-Yau  dim 6  compact complex 3-manifolds (string theory)     │
  └──────────────────────────────────────────────────────────────────────┘
```

### 1.2 Why Manifolds? The Ant on a Surface

```
  An ant living on a surface has no concept of the ambient 3D space.
  It only knows: "near me, things look flat (like ℝ²)."

  The manifold formalism captures exactly this intrinsic geometry.
  No embedding required. No ambient space needed.
  The chart φ: U → ℝⁿ gives the ant local coordinates.

  Different charts give different coordinate systems for the same manifold.
  Physics cannot depend on the choice of coordinates → tensors/forms.
```

---

## 2. Tangent Spaces

### 2.1 Tangent Vectors

```
  At each point p ∈ M, there is a tangent space TₚM — the space of
  "directions you can move" at p.

  DEFINITION VIA CURVES:
  A tangent vector at p = equivalence class of curves γ: (-ε,ε) → M
  with γ(0) = p, where two curves are equivalent if they have the
  same velocity in every coordinate chart.

  In local coordinates (x¹,...,xⁿ): tangent vectors are
  v = vⁱ ∂/∂xⁱ    (Einstein summation: sum over repeated indices)

  Basis for TₚM: {∂/∂x¹, ∂/∂x², ..., ∂/∂xⁿ}    (partial derivatives!)

  Why partial derivatives? A tangent vector acts on functions:
  v[f] = vⁱ ∂f/∂xⁱ   (directional derivative)
  This is the "derivation" definition: tangent vector = derivation on C∞(M)
```

### 2.2 Tangent Bundle and Pushforward

```
  TANGENT BUNDLE: TM = ∪_{p∈M} TₚM   (all tangent spaces together)
  TM is itself a 2n-dimensional manifold.

  PUSHFORWARD (differential) of a smooth map f: M → N:
  f*: TₚM → T_{f(p)}N
  If γ is a curve through p, f*(v) = (f∘γ)'(0) (velocity of image curve)

  In coordinates: (f*)ᵢʲ = ∂fʲ/∂xⁱ   (the Jacobian matrix!)

  The pushforward is the rigorous version of "the Jacobian."
```

---

## 3. Cotangent Space and 1-Forms

### 3.1 Covectors

```
  COTANGENT SPACE T*ₚM = dual of TₚM = {linear maps TₚM → ℝ}

  Basis for T*ₚM: {dx¹, dx², ..., dxⁿ}  dual to {∂/∂x¹,...,∂/∂xⁿ}
  meaning: dxⁱ(∂/∂xʲ) = δⁱⱼ   (Kronecker delta)

  A covector at p: α = αᵢ dxⁱ  (acts on tangent vectors by α(v) = αᵢvⁱ)

  DIFFERENTIAL OF A FUNCTION:
  df = (∂f/∂xⁱ) dxⁱ
  (df)(v) = v[f] = vⁱ ∂f/∂xⁱ   (df eats a tangent vector, spits out a number)

  Connection to gradient:
  In ℝⁿ with Euclidean metric, df corresponds to ∇f.
  But df is more fundamental — it's defined without a metric.
```

### 3.2 1-Forms and Pullback

```
  A 1-FORM (or covector field) α assigns a covector αₚ ∈ T*ₚM to each p.
  α = αᵢ(x) dxⁱ  (components are functions)

  PULLBACK of f: M → N along a 1-form β on N:
  f*β is a 1-form on M defined by (f*β)ₚ(v) = β_{f(p)}(f*v)

  In coordinates: f*β = (βⱼ ∘ f)(∂fʲ/∂xⁱ) dxⁱ  (chain rule!)

  Pullback is contravariant: goes the opposite direction from f.
  Pushforward (f*): M → N (same direction)
  Pullback (f*): forms on N → forms on M (opposite direction)
```

---

## 4. Differential Forms

### 4.1 k-Forms

```
  A k-FORM ω at p is a multilinear, totally antisymmetric map:
  ωₚ: TₚM × TₚM × ... × TₚM (k copies) → ℝ

  "Antisymmetric" means swapping any two arguments flips the sign:
  ω(v₁,...,vᵢ,...,vⱼ,...,vₖ) = -ω(v₁,...,vⱼ,...,vᵢ,...,vₖ)

  BASIS k-FORMS: dxⁱ¹ ∧ dxⁱ² ∧ ... ∧ dxⁱᵏ   (i₁ < i₂ < ... < iₖ)

  Space of k-forms on ℝⁿ has dimension C(n,k) = n!/(k!(n-k)!)

  ON ℝ³:
  0-forms: f                                       (1 basis element)
  1-forms: P dx + Q dy + R dz                      (3 basis elements)
  2-forms: A dy∧dz + B dz∧dx + C dx∧dy            (3 basis elements)
  3-forms: f dx∧dy∧dz                              (1 basis element)

  Note the symmetry: C(3,0)=1, C(3,1)=3, C(3,2)=3, C(3,3)=1
```

### 4.2 Wedge Product

```
  WEDGE PRODUCT ∧: Ωᵏ(M) × Ωˡ(M) → Ωᵏ⁺ˡ(M)

  Properties:
  ├── Bilinear
  ├── GRADED ANTICOMMUTATIVE: α∧β = (-1)^(kl) β∧α
  │   So for 1-forms: α∧β = -β∧α
  │   And: α∧α = 0 for any odd-degree form
  └── Associative: (α∧β)∧γ = α∧(β∧γ)

  EXAMPLES:
  dx∧dy = -dy∧dx        (anticommutative)
  dx∧dx = 0             (any form wedged with itself)
  (dx∧dy)∧dz = dx∧(dy∧dz) = dx∧dy∧dz   (associative)

  2-FORM AS SIGNED AREA:
  (dx∧dy)(u,v) = det[u₁ u₂; v₁ v₂] = u₁v₂ - u₂v₁
  = signed area of parallelogram spanned by u and v in xy-plane
```

---

## 5. Exterior Derivative

### 5.1 The Definition

```
  EXTERIOR DERIVATIVE d: Ωᵏ(M) → Ωᵏ⁺¹(M)

  For a 0-form (function) f:
  df = (∂f/∂xⁱ) dxⁱ   (the differential — same as before)

  For a k-form ω = ωᵢ₁...ᵢₖ dxⁱ¹∧...∧dxⁱᵏ:
  dω = (∂ωᵢ₁...ᵢₖ/∂xʲ) dxʲ∧dxⁱ¹∧...∧dxⁱᵏ
  (differentiate each component, wedge with dxʲ, sum over j)

  THE FUNDAMENTAL PROPERTIES:
  1. d(α+β) = dα + dβ            (linearity)
  2. d(α∧β) = dα∧β + (-1)^k α∧dβ (Leibniz/graded product rule)
  3. d² = 0                       (d∘d = 0 — the key identity!)
  4. d commutes with pullback: d(f*ω) = f*(dω)
```

### 5.2 d in ℝ³ — Recovering Gradient, Curl, Divergence

```
  0-FORM → 1-FORM: d applied to function f
  df = (∂f/∂x)dx + (∂f/∂y)dy + (∂f/∂z)dz
  ↔ gradient  ∇f = (∂f/∂x, ∂f/∂y, ∂f/∂z)

  1-FORM → 2-FORM: d applied to α = P dx + Q dy + R dz
  dα = (∂R/∂y - ∂Q/∂z)dy∧dz + (∂P/∂z - ∂R/∂x)dz∧dx + (∂Q/∂x - ∂P/∂y)dx∧dy
  ↔ curl  ∇×(P,Q,R)

  2-FORM → 3-FORM: d applied to ω = A dy∧dz + B dz∧dx + C dx∧dy
  dω = (∂A/∂x + ∂B/∂y + ∂C/∂z) dx∧dy∧dz
  ↔ divergence  ∇·(A,B,C)

  THE CHAIN:
  Ω⁰ →^(grad) Ω¹ →^(curl) Ω² →^(div) Ω³ →^d 0

  d² = 0 ENCODES:
  ├── curl(grad f) = 0       (d(df) = 0: gradient has no curl)
  └── div(curl F) = 0        (d(dα) = 0: curl has no divergence)
  These are identities from 01-VECTOR-CALC.md — they follow from d²=0!
```

---

## 6. Integration on Manifolds

### 6.1 Oriented Manifolds

```
  ORIENTATION: a consistent choice of "handedness" at every point.
  An n-form everywhere nonzero = volume form = determines orientation.

  Orientable manifolds: sphere S², torus T², all Lie groups.
  Non-orientable: Möbius band, Klein bottle, RP².

  For oriented manifold with boundary ∂M:
  ∂M inherits the induced orientation from M.
  Convention: boundary orientation = outward normal first.
  In ℝ³: ∂(solid ball) = sphere S² with outward-pointing normal. ✓
```

### 6.2 Integrating k-Forms

```
  A k-form integrates naturally over a k-dimensional submanifold.

  1-FORM over a curve γ: [a,b] → M:
  ∫_γ α = ∫ₐᵇ α_{γ(t)}(γ'(t)) dt
  = line integral (work done by a vector field along γ)

  2-FORM over a surface S parameterized by φ: D → M:
  ∫_S ω = ∫_D ω_{φ(u,v)}(∂φ/∂u, ∂φ/∂v) du dv
  = surface integral (flux through surface)

  n-FORM over n-manifold:
  ∫_M f dx¹∧...∧dxⁿ = ∫ f(x) dx¹...dxⁿ  (ordinary multiple integral)

  KEY PROPERTY: the integral is coordinate-independent.
  (Changing coordinates changes the form components AND the Jacobian in exactly
  compensating ways — built into the wedge product structure.)
```

---

## 7. The Generalized Stokes' Theorem

```
  ┌─────────────────────────────────────────────────────────────────────┐
  │                                                                     │
  │   ∫_M  dω  =  ∫_∂M  ω                                             │
  │                                                                     │
  │   M = compact oriented manifold with boundary ∂M                   │
  │   ω = smooth (k-1)-form on M                                       │
  └─────────────────────────────────────────────────────────────────────┘

  This single equation IS all the integral theorems:

  k=1, M = interval [a,b] in ℝ:
  ∫_{[a,b]} df = ∫_∂[a,b] f = f(b) - f(a)
  ↓
  FUNDAMENTAL THEOREM OF CALCULUS

  k=2, M = region D in ℝ²:
  ∫_D d(P dx + Q dy) = ∫_∂D P dx + Q dy
  ↓
  GREEN'S THEOREM

  k=2, M = surface S in ℝ³, ∂M = bounding curve C:
  ∫_S d(P dx+Q dy+R dz) = ∫_C P dx+Q dy+R dz
  (d of a 1-form = curl 2-form)
  ↓
  CLASSICAL STOKES' THEOREM  ∫_S (∇×F)·dA = ∮_C F·dr

  k=3, M = volume V, ∂M = closed surface S:
  ∫_V d(A dy∧dz + B dz∧dx + C dx∧dy) = ∫_S A dy∧dz + B dz∧dx + C dx∧dy
  (d of a 2-form = divergence 3-form)
  ↓
  DIVERGENCE THEOREM  ∫_V (∇·F) dV = ∯_S F·dA
```

---

## 8. Maxwell's Equations in Differential Form Language

### 8.1 The Faraday 2-Form

```
  In 4D spacetime with coordinates (t, x, y, z):

  ELECTROMAGNETIC 2-FORM F (the Faraday tensor as a 2-form):
  F = E_x dx∧dt + E_y dy∧dt + E_z dz∧dt
    + B_x dy∧dz + B_y dz∧dx + B_z dx∧dy

  In index notation: F = ½ Fμν dxμ∧dxν
  where Fμν is the antisymmetric field tensor:
  ┌               ┐
  │  0  -Ex -Ey -Ez │
  │  Ex   0  -Bz  By │
  │  Ey   Bz   0  -Bx│
  │  Ez  -By   Bx   0 │
  └               ┘
```

### 8.2 Maxwell's Equations as Two Lines

```
  dF = 0        ←→  { ∇·B = 0            (Gauss's law for magnetism)
                       ∇×E + ∂B/∂t = 0  (Faraday's law)

  d★F = J       ←→  { ∇·E = ρ/ε₀         (Gauss's law for electricity)
                       ∇×B - μ₀ε₀∂E/∂t = μ₀J (Ampere-Maxwell)

  where:
  ★ = Hodge star operator (maps k-forms to (n-k)-forms using the metric)
  J = 4-current 3-form  J = J_μ εμνρσ dxν∧dxρ∧dxσ

  WHY dF=0 IS AUTOMATIC:
  If we write F = dA for some 1-form A (the 4-potential):
  A = φ dt - A_x dx - A_y dy - A_z dz
  Then dF = d(dA) = d²A = 0 automatically (d²=0!)

  GAUGE INVARIANCE:
  A → A + dχ for any function χ leaves F = dA unchanged:
  F → d(A+dχ) = dA + d²χ = dA = F ✓
  Gauge invariance = the freedom in choosing A is d(anything).
  This is the U(1) fiber bundle connection freedom from 08-TOPOLOGY.md!
```

---

## 9. de Rham Cohomology

### 9.1 Closed and Exact Forms

```
  CLOSED k-form:  dω = 0   (ω is in the kernel of d: Ωᵏ → Ωᵏ⁺¹)
  EXACT k-form:   ω = dα for some (k-1)-form α  (ω is in the image of d)

  Since d²=0: every exact form is closed.
  Exact ⊆ Closed.
  The question: is every closed form exact?

  Locally YES (Poincaré Lemma):
  On any contractible open set, every closed form is exact.
  Explicitly: if dω=0 on a ball, then ω=dα for some α on that ball.

  Globally NO (in general):
  On a circle S¹: dθ is closed but NOT exact.
  (If dθ = df, then ∮_{S¹} dθ = ∮ df = f(2π)-f(0) = 0,
   but ∮_{S¹} dθ = 2π ≠ 0.)
  The failure to be exact detects the hole in S¹.
```

### 9.2 de Rham Cohomology Groups

```
  H^k_dR(M) = (closed k-forms) / (exact k-forms)
             = ker(d: Ωᵏ→Ωᵏ⁺¹) / im(d: Ωᵏ⁻¹→Ωᵏ)

  Elements of H^k_dR(M) are cohomology classes [ω] = {ω + dα | α ∈ Ωᵏ⁻¹}

  EXAMPLES:
  ┌──────────────────────────────────────────────────────────────────────┐
  │  Space         │  H⁰      H¹      H²      H³    │  Betti numbers   │
  ├──────────────────────────────────────────────────────────────────────┤
  │  ℝⁿ            │  ℝ       0       0       0     │  1,0,0,0         │
  │  S¹ (circle)   │  ℝ       ℝ       0       0     │  1,1,0,0         │
  │  S² (sphere)   │  ℝ       0       ℝ       0     │  1,0,1,0         │
  │  Torus T²      │  ℝ       ℝ²      ℝ       0     │  1,2,1,0         │
  │  S³            │  ℝ       0       0       ℝ     │  1,0,0,1         │
  └──────────────────────────────────────────────────────────────────────┘

  DE RHAM'S THEOREM: H^k_dR(M) ≅ H^k_sing(M; ℝ)
  de Rham cohomology (defined by smooth forms) =
  singular cohomology (defined by topological cycles)

  PROFOUND: smooth differential calculus knows about topology.
  The Chern classes from 08-TOPOLOGY.md live in H^even_dR(M).
```

## 10. Manifold Hypothesis and ML

```
  THE MANIFOLD HYPOTHESIS:
  High-dimensional data (images ∈ ℝ^(64×64×3) ≈ ℝ^12288, text ∈ ℝ^768, etc.)
  concentrates near a low-dimensional manifold M ⊂ ℝᵈ.

  Evidence:
  ├── Intrinsic dimensionality of ImageNet: ~40 (not 12288)
  ├── Smooth interpolation in latent space of VAEs/GANs — geodesics work
  └── Random perturbations off the manifold degrade representations sharply

  GEODESIC VS EUCLIDEAN DISTANCE:
  Euclidean distance in ℝᵈ: ‖x - y‖₂  (straight line through ambient space)
  Geodesic distance on M:    inf_γ ∫ ‖γ'(t)‖ dt  (shortest path along manifold)

  These diverge when M is highly curved or has bottlenecks.
  Example: two points on a ring — Euclidean distance cuts through interior,
  geodesic distance goes around the ring.

  Isomap (Tenenbaum 2000): build k-nearest-neighbor graph, approximate
  geodesic distances with graph shortest paths, then apply MDS in geodesic
  distance. Recovers manifold structure invisible to PCA.

  RIEMANNIAN OPTIMIZATION ON MATRIX MANIFOLDS:
  Many ML constraints define manifolds; optimization must stay on them.

  ┌─────────────────────────────────────────────────────────────────────┐
  │  STIEFEL MANIFOLD St(n,k):                                         │
  │  St(n,k) = {X ∈ M_{n×k} | XᵀX = Iₖ}  (matrices with orth. cols) │
  │  Appears in: orthogonal weight matrices (orthogonal RNNs),          │
  │  constrained PCA, CCA (canonical correlation analysis).             │
  │                                                                     │
  │  GRASSMANN MANIFOLD Gr(n,k):                                        │
  │  Gr(n,k) = St(n,k) / O(k)  (k-dimensional subspaces of ℝⁿ)       │
  │  Appears in: subspace tracking, dimensionality reduction,           │
  │  multi-view learning (find common subspace between views).          │
  │                                                                     │
  │  SPD MANIFOLD Sym⁺(n):                                             │
  │  {A ∈ M_{n×n} | A = Aᵀ, A ≻ 0}  (symmetric positive definite)   │
  │  Appears in: covariance matrices, diffusion tensors (DTI in MRI),   │
  │  metric learning, Gaussian processes.                               │
  └─────────────────────────────────────────────────────────────────────┘

  RIEMANNIAN GRADIENT DESCENT:
  Euclidean gradient step:     x_{t+1} = x_t - α ∇f(x_t)
  Riemannian gradient step:    x_{t+1} = Retract(x_t, -α grad_M f(x_t))

  grad_M f(x) = Proj_{T_x M}(∇f(x))  (project Euclidean gradient onto tangent space)
  Retract: map tangent vector back to manifold (e.g., QR retraction on Stiefel)

  For Stiefel: use matrix exponential (exact) or QR retraction (approximate).
  For SPD: exponential map has a closed form: Exp_A(V) = A^{1/2} exp(A^{-1/2}VA^{-1/2}) A^{1/2}

  Libraries: Geoopt (PyTorch), McTorch, Manopt (MATLAB/Python).

  DIFFUSION MAPS — Laplace-Beltrami from data (see §4.5 of 07-DIFFEQ):
  The graph Laplacian eigenvectors converge to eigenfunctions of ∆_M as
  sample size n → ∞ and bandwidth ε → 0 (jointly). This is the
  mathematical justification for spectral clustering and diffusion maps.

  FISHER INFORMATION METRIC (natural gradient):
  For a statistical model p(x; θ) parameterized by θ ∈ ℝᵈ:
  Fisher information: I(θ)_{ij} = E[∂_i log p · ∂_j log p]
  This is a Riemannian metric on the manifold of probability distributions.
  Natural gradient descent: θ_{t+1} = θ_t - α I(θ)⁻¹ ∇L(θ)
  Preconditions by Fisher inverse → K-FAC and second-order optimization methods.
  The manifold of distributions is the statistical manifold (information geometry).
```

### 1.3 Lorentzian Manifolds and Spacetime

```
  PSEUDO-RIEMANNIAN MANIFOLD: metric gᵢⱼ is non-degenerate but NOT positive definite.
  (Some nonzero vectors v have g(v,v) = 0 or g(v,v) < 0.)

  LORENTZIAN MANIFOLD: signature (1,3) or (−,+,+,+).
  At each point p, the tangent space Tₚ M has inner product:
  g(v,v) = -v₀² + v₁² + v₂² + v₃²   (with c=1 units)

  MINKOWSKI SPACE (flat Lorentzian):
  M = ℝ⁴ with metric ds² = -c²dt² + dx² + dy² + dz²

  CAUSAL STRUCTURE — the key new feature vs Riemannian geometry:
  For a vector v ∈ Tₚ M:
  ┌────────────────────────────────────────────────────────────────────┐
  │  g(v,v) < 0:  TIMELIKE  — within the light cone, causal influence │
  │  g(v,v) = 0:  NULL / LIGHTLIKE — on the light cone              │
  │  g(v,v) > 0:  SPACELIKE — outside light cone, spacelike separated │
  │                                                                    │
  │         future                                                     │
  │           │                                                        │
  │    null   │   null                                                 │
  │     ╲     │     ╱      light cone at p                            │
  │  ────────────────── spacelike directions                           │
  │     ╱     │     ╲                                                  │
  │           │                                                        │
  │         past                                                       │
  └────────────────────────────────────────────────────────────────────┘

  CURVES in spacetime:
  Timelike curve: γ with g(γ',γ') < 0 everywhere — worldline of massive particle
  Null curve: g(γ',γ') = 0 — worldline of a photon (light ray)
  Proper time: τ = ∫ √(-g(γ',γ')) dt  (measured by clock on worldline)

  GEODESICS in Lorentzian geometry:
  Timelike geodesics MAXIMIZE proper time (twin paradox — the straight worldline
  in spacetime = maximum aging; curved path = less proper time).
  This is opposite to Riemannian: geodesics minimize length, but in Lorentzian
  signature, the causal structure flips the variational problem.
  Null geodesics: paths of light rays. Zero arc length.

  SCHWARZSCHILD METRIC (exterior of spherical mass M):
  ds² = -(1 - r_s/r)c²dt² + (1 - r_s/r)⁻¹dr² + r²(dθ² + sin²θ dφ²)
  r_s = 2GM/c² = Schwarzschild radius
  At r = r_s: metric coefficient g_tt → 0, g_rr → ∞ (coordinate singularity only)
  Null geodesics at r = r_s: cannot escape → event horizon.

  ISOMETRIES AND KILLING VECTORS:
  A Killing vector field K satisfies: ∇_(μ K_ν) = 0 (Killing equation)
  Each Killing vector → conserved quantity along geodesics (Noether's theorem).
  Schwarzschild: ∂_t and ∂_φ are Killing → energy and angular momentum conserved.

  → 10-DIFFERENTIAL-GEOMETRY.md develops the Riemann tensor Rᵢⱼₖˡ and
    Einstein's equations Gμν = (8πG/c⁴) Tμν for the full GR story.
```

## 11. Lie Groups and Lie Algebras

```
  A LIE GROUP G is both a smooth manifold and a group,
  where multiplication G×G → G and inversion G → G are smooth maps.

  KEY EXAMPLES:
  ┌────────────────────────────────────────────────────────────────────┐
  │  GL(n,ℝ): n×n invertible real matrices (open subset of M_{n×n})  │
  │  SL(n,ℝ): det = 1 (n²-1 dimensional)                             │
  │  O(n): AᵀA = I, det = ±1  (orthogonal group, dim = n(n-1)/2)     │
  │  SO(n): det = +1 (special orthogonal = rotations)                 │
  │  U(n): A†A = I  (unitary group, dim = n² real)                    │
  │  SU(n): det = 1 (special unitary, dim = n²-1)                     │
  │  SU(2) ≅ S³: 3-sphere, double-covers SO(3)                        │
  │  SU(3): gauge group of QCD (strong force, dim=8)                  │
  │  U(1) ≅ S¹: gauge group of EM                                     │
  └────────────────────────────────────────────────────────────────────┘

  THE LIE ALGEBRA g = TeG (tangent space at the identity):
  Captures the infinitesimal structure of G.
  g is a vector space with a bilinear antisymmetric bracket:
  [·,·]: g × g → g   satisfying the Jacobi identity [[X,Y],Z]+[[Y,Z],X]+[[Z,X],Y]=0

  For matrix Lie groups: g = {tangent vectors at I} = {d/dt γ(t)|_{t=0}}
  Lie bracket = matrix commutator: [X,Y] = XY - YX

  EXAMPLES:
  gl(n,ℝ) = M_{n×n}(ℝ) with [X,Y] = XY - YX    (all n×n matrices)
  so(n) = {skew-symmetric matrices: X + Xᵀ = 0}  dim = n(n-1)/2
  su(n) = {skew-Hermitian + traceless: X + X† = 0, tr X = 0}
  su(2): basis {iσ₁/2, iσ₂/2, iσ₃/2} where σᵢ are Pauli matrices
         [Jᵢ, Jⱼ] = εᵢⱼₖ Jₖ  ← angular momentum algebra from QM!

  THE EXPONENTIAL MAP exp: g → G:
  exp(X) = eˣ = I + X + X²/2! + X³/3! + ...  (matrix exponential)
  ├── exp maps g (Lie algebra) → G (Lie group)
  ├── For connected G: exp(g) generates G (may not surject for non-compact G)
  ├── One-parameter subgroup: t ↦ exp(tX) is a group homomorphism ℝ → G
  └── Geodesic from identity through G (bi-invariant metric)

  CONNECTION TO PHYSICS:
  Rotation by angle θ about axis n̂:
  R = exp(θ n̂ · J)  where Jᵢ are the so(3) generators (3×3 skew-sym matrices)
  Quantum: U = exp(-iθ n̂ · σ/2) ∈ SU(2)  (spinor rotation)

  Baker-Campbell-Hausdorff (BCH):
  exp(X)exp(Y) = exp(X + Y + ½[X,Y] + 1/12[X,[X,Y]] - 1/12[Y,[X,Y]] + ...)
  The group commutator to first order = the Lie bracket:
  exp(X)exp(Y)exp(-X)exp(-Y) = exp([X,Y] + O(X²,Y²,...))

  LIE GROUP ACTIONS AND EQUIVARIANCE (geometric deep learning):
  A Lie group G acts on a manifold M via φ: G × M → M (smooth action).
  Examples:
  ├── SO(3) acts on ℝ³ (3D rotations on Euclidean space)
  ├── SE(3) = SO(3) ⋉ ℝ³ acts on ℝ³ (rotations + translations)
  └── Diffeos Diff(M) act on all geometric objects on M (general covariance)

  EQUIVARIANT NETWORK: f(φ_g(x)) = ρ_g(f(x)) for all g ∈ G
  (output transforms predictably under group action on input)
  This is the mathematical heart of:
  ├── CNNs: translation equivariance (G = translation group)
  ├── E(3)-equivariant networks (SchNet, SE(3)-Transformers): molecule geometry
  ├── Spherical CNNs: SO(3) equivariance for omnidirectional vision
  └── Gauge equivariant networks: equivariance under local gauge transformations

  REPRESENTATION THEORY:
  A representation ρ: G → GL(V) is a group homomorphism to linear maps.
  Irreducible representations (irreps) of SU(2) = spin-j representations for j=0,½,1,3/2,...
  These are exactly the angular momentum quantum numbers of QM.
  Character theory: χ(g) = tr(ρ(g)) — key tool for decomposing representations.
```

### 12. Discrete Differential Geometry and Computation

```
  DISCRETE EXTERIOR CALCULUS (DEC):
  Translates the smooth theory of §4–7 into computable matrix operations.

  MESH REPRESENTATION:
  A triangulated surface is a simplicial complex K = (V, E, F):
  V = vertices (0-simplices), E = edges (1-simplices), F = triangles (2-simplices)

  HALF-EDGE DATA STRUCTURE:
  Each undirected edge e splits into two directed half-edges (he, he.twin).
  Provides O(1) access to: neighboring vertex, face, next/prev half-edge.
  Used in: libigl, CGAL, OpenMesh.

  BOUNDARY OPERATORS AS SPARSE MATRICES:
  ∂₁: C₁ → C₀  (edge → its two vertices, with orientation)
  ∂₂: C₂ → C₁  (triangle → its three edges, with orientation)
  ∂₃: 0 for surfaces (no 3-cells)

  In matrix form (|V|×|E| and |E|×|F| sparse matrices):
  ∂₁[v,e] = +1 if e ends at v, -1 if e starts at v, 0 otherwise
  ∂₂[e,f] = ±1 if e is a boundary edge of f (sign = orientation)

  ∂₁ · ∂₂ = 0  (boundary of boundary is zero — verified in matrix arithmetic!)

  DISCRETE HODGE STAR:
  Continuous: ★: Ωᵏ → Ωⁿ⁻ᵏ (requires metric)
  Discrete: diagonal matrix Hₖ encoding primal/dual volume ratios
  H₀[v,v] = 1/6 × Σ(areas of triangles around v)  (Voronoi area)
  H₁[e,e] = (cotan(αₑ) + cotan(βₑ))/2            (cotangent weights!)
  H₂[f,f] = 1/area(f)

  DISCRETE LAPLACE-BELTRAMI (cotangent Laplacian):
  L = ∂₁ᵀ H₁ ∂₁ = H₀⁻¹ ∂₁ᵀ H₁ ∂₁ (acting on vertex functions)
  L[i,i] = Σⱼ (cot αᵢⱼ + cot βᵢⱼ)/2
  L[i,j] = -(cot αᵢⱼ + cot βᵢⱼ)/2  (for adjacent vertices i,j)

  This is the standard mesh Laplacian used in geometry processing.
  It converges to ∆_M as meshes are refined (Wardetzky et al.).

  APPLICATIONS:
  ├── Mesh smoothing: ∂x/∂t = λ L x  (heat equation on mesh)
  ├── Spectral mesh analysis: eigenvectors of L = "shape DNA"
  ├── Harmonic maps: minimize ∫|∇f|² ↔ solve Lf = 0 on interior
  ├── Geodesic distance: heat method (solve heat eq, extract gradient)
  └── FEM on curved domains: stiffness matrix is discrete Laplace-Beltrami

  PYTHON ECOSYSTEM:
  libigl (Python bindings): igl.cotmatrix(V,F) = cotangent Laplacian L
  PyMesh: mesh processing and Boolean operations
  trimesh: lightweight mesh loading + vertex/face adjacency
  potpourri3d: geodesics, heat method on meshes

  import igl
  V, F = igl.read_triangle_mesh("bunny.obj")  # vertices (n×3), faces (m×3)
  L = igl.cotmatrix(V, F)          # sparse cotangent Laplacian (n×n)
  M = igl.massmatrix(V, F, igl.MASSMATRIX_TYPE_VORONOI)  # vertex areas
  eigvals, eigvecs = scipy.sparse.linalg.eigsh(-L, M, k=50)  # Laplace-Beltrami spectrum
```


### 9.3 Computing de Rham Cohomology

```
  KEY TOOLS FOR COMPUTING H^k_dR(M):

  MAYER-VIETORIS SEQUENCE (for M = U ∪ V, U,V open):
  ... → H^k_dR(M) → H^k_dR(U) ⊕ H^k_dR(V) → H^k_dR(U∩V) → H^(k+1)_dR(M) → ...
  This long exact sequence relates the cohomology of M to simpler pieces.

  EXAMPLE: S² = U ∪ V (upper and lower hemispheres, each contractible)
  U ≅ ℝ², V ≅ ℝ², U∩V ≅ S¹ × (-ε,ε) ≃ S¹
  H^k(ℝ²) = ℝ if k=0, else 0.  H^0(S¹)=ℝ, H^1(S¹)=ℝ, H^k(S¹)=0 for k≥2.
  Mayer-Vietoris gives: H^0(S²)=ℝ, H^1(S²)=0, H^2(S²)=ℝ ✓

  KÜNNETH FORMULA (for products M × N):
  H^k_dR(M × N) = ⊕_{i+j=k} H^i_dR(M) ⊗ H^j_dR(N)

  EXAMPLE: Torus T² = S¹ × S¹
  H^0(T²) = H^0⊗H^0 = ℝ
  H^1(T²) = (H^1⊗H^0) ⊕ (H^0⊗H^1) = ℝ ⊕ ℝ = ℝ²
  H^2(T²) = H^1⊗H^1 = ℝ ✓  (matches the Betti table in §9.2)

  POINCARÉ DUALITY (for compact oriented n-manifold M):
  H^k_dR(M) ≅ H^(n-k)_dR(M)
  This isomorphism is implemented by wedging with the volume form and integrating.
  Consequence: bₖ = bₙ₋ₖ (Betti numbers are symmetric around n/2).
  For a 4-manifold: b₀=b₄, b₁=b₃ (but b₂ is unconstrained).

  GAUGE THEORY INTERPRETATION:
  Poincaré lemma: dω=0 locally ⟹ ω=dα locally (on contractible sets).
  H^1_dR(M) measures GLOBAL obstructions to exact 1-forms.

  In gauge theory: A is a connection 1-form (the gauge potential).
  F = dA is the field strength (closed 2-form: dF = d²A = 0).
  Is F exact globally? If H^2_dR(M) ≠ 0, possibly not.
  Non-exact F ↔ topologically non-trivial gauge field (magnetic flux through holes).

  EXAMPLE: EM on ℝ³ \ {point} (monopole geometry):
  H^2_dR(ℝ³\{0}) = ℝ  (non-trivial 2nd cohomology)
  The field strength F of a Dirac monopole represents a non-trivial cohomology class.
  The Dirac quantization condition (§7.3 of 08-TOPOLOGY.md) is the
  requirement that this class be an INTEGER (integrality of characteristic class).

  CHARACTERISTIC CLASSES:
  Chern classes cₖ ∈ H^(2k)_dR(M): obstructions to having globally defined
  sections of complex vector bundles. Computed from curvature:
  c₁ = [tr F / 2πi] ∈ H²(M)  (first Chern class — the monopole number)
  ∫_M c₁ = (integer) = Chern number (the topological invariant of §7.1 in 08-TOPOLOGY.md)
```

---

## Decision Cheat Sheet

| Need to... | Tool |
|-----------|------|
| Integrate a vector field over a curve | 1-form, line integral |
| Integrate flux through a surface | 2-form, surface integral |
| Apply Stokes'/Gauss's/Green's theorem | Generalized Stokes: ∫_M dω = ∫_∂M ω |
| Check if a vector field is conservative | Is the corresponding 1-form exact? (dα=0, then α=df) |
| Write Maxwell's equations compactly | dF=0 and d★F=J |
| Detect "holes" in a manifold | de Rham cohomology groups Hᵏ_dR |
| Change coordinates on an integral | Pullback automatically handles Jacobian |
| Show curl(grad)=0, div(curl)=0 | These follow from d²=0 |

---

## Common Confusion Points

**"Why does d²=0?"**
For a function f: d²f = d(df) = d(∂f/∂xⁱ dxⁱ) = (∂²f/∂xʲ∂xⁱ) dxʲ∧dxⁱ. The factor ∂²f/∂xʲ∂xⁱ is symmetric in i,j (equality of mixed partials), but dxʲ∧dxⁱ is antisymmetric. Symmetric × antisymmetric = 0 when summed. This is the same reason curl(grad)=0 and div(curl)=0 — d²=0 is the single algebraic fact encoding both.

**"What does the Hodge star ★ do?"**
The Hodge star maps k-forms to (n-k)-forms using the metric and orientation. In ℝ³: ★dx = dy∧dz, ★dy = dz∧dx, ★dz = dx∧dy (maps 1-forms to 2-forms). It's what converts the "flux 2-form" to the "vector field" language. Maxwell's d★F = J uses ★ to relate the 2-form F to the 3-form source J. Without a metric, you can't define ★ — this is why the d★F=J equation requires the spacetime metric while dF=0 is purely topological.

**"How does this relate to the integral theorems I already know?"**
It IS those theorems. The Divergence theorem, classical Stokes', Green's theorem — they are all the single equation ∫_M dω = ∫_∂M ω for different choices of M (dimension) and ω (degree). The unified proof of all of them is one proof of the generalized Stokes' theorem.

**"Is every closed form exact?"**
Locally yes (Poincaré lemma). Globally only if the manifold has no "holes" (trivial cohomology in the relevant degree). The failure is measured by de Rham cohomology. In physics: a magnetic monopole would make ∇·B=4πgδ(r)≠0 globally, even though dF=0 locally everywhere except the source — the monopole lives in the cohomology.

**"What's the difference between a form and a tensor?"**
All k-forms are antisymmetric (0,k)-tensors. Tensors are more general (can be symmetric or mixed symmetry). Forms are the antisymmetric part of tensor calculus — but they're the part that integrates naturally and has the exterior derivative d. General tensors need a connection (Christoffel symbols) to differentiate covariantly; forms only need d.

---

*Next: `mathematics/10-DIFFERENTIAL-GEOMETRY.md` — curvature, geodesics, the Riemann tensor, and Einstein's field equations decoded.*
