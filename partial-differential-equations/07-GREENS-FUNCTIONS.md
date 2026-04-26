# Green's Functions and Distributions

## The Big Picture

Green's functions encode the complete response of a linear PDE to any source, expressed
as the response to a point source. They are the PDE generalization of matrix inversion,
and are exactly the **impulse response** / **convolution kernel** from signal processing.

```
+-----------------------------------------------------------------------+
|              GREEN'S FUNCTION CONCEPT                                 |
|                                                                       |
|  SIGNAL PROCESSING:          PDE ANALOG:                              |
|  Linear system with          Linear PDE with                          |
|  impulse response h(t):      Green's function G(x,y):                 |
|                                                                       |
|  INPUT: δ(t)                 SOURCE: δ(x−y)                           |
|  OUTPUT: h(t)                RESPONSE: G(x,y)                         |
|                                                                       |
|  GENERAL INPUT f(t):         GENERAL SOURCE f(y):                     |
|  OUTPUT = h * f              u(x) = ∫ G(x,y) f(y) dy                  |
|         = ∫h(t−s)f(s)ds     (same: convolution)                       |
|                                                                       |
|  INVERSION:                  INVERSION:                               |
|  Y(ω) = H(ω)·F(ω)           û(k) = Ĝ(k)·f̂(k)                          |
|  H(ω) = 1 / (transfer fn)   Ĝ(k) = 1 / (symbol)                       |
|                                                                       |
|  KEY: once you have G, you can solve for ANY source f                 |
|  by quadrature. G encodes the operator inverse.                       |
+-----------------------------------------------------------------------+
```

---

## Distributions: Mathematical Foundation

To work rigorously with Green's functions requires the theory of distributions
(generalized functions), developed by Laurent Schwartz in the 1940s.

```
  MOTIVATION: The Dirac delta δ(x) is not a function in any classical sense.
  We need a framework where δ(x) = 0 for x ≠ 0, but ∫ δ(x) dx = 1.

  TEST FUNCTIONS: φ ∈ D(R^n) = C_c^∞(R^n) (smooth, compactly supported)

  DISTRIBUTION: A continuous linear functional T: D → R.
  Written T[φ] or ⟨T, φ⟩.

  REGULAR DISTRIBUTION: T_f[φ] = ∫ f(x)φ(x) dx  for some locally integrable f.
  Identifies "ordinary functions" with distributions.

  DIRAC DELTA: δ_y[φ] = φ(y)
  Not a regular distribution — there is no function f with ∫ f(x)φ(x)dx = φ(0).

  DERIVATIVE OF A DISTRIBUTION: T'[φ] = −T[φ']
  This is integration by parts pushed to all functions, including singular ones.
  Even discontinuous functions and delta functions have distributional derivatives.
```

### Key Distributions

```
  ┌────────────────────────────────────────────────────────────────┐
  │ δ(x):      ⟨δ, φ⟩ = φ(0)           (point mass at 0)           │
  │ δ(x−y):    ⟨δ_y, φ⟩ = φ(y)         (point mass at y)           │
  │ H(x):      ⟨H, φ⟩ = ∫₀^∞ φ(x) dx  (Heaviside step function)    │
  │ H'(x) = δ(x) in distribution sense                             │
  │                                                                │
  │ P.V.(1/x): ⟨P.V.(1/x), φ⟩ = lim_{ε→0} ∫_{|x|>ε} φ(x)/x dx │
  │ (principal value, arises in Hilbert transform)                 │
  │                                                                │
  │ ∂δ/∂x_i: ⟨∂δ/∂x_i, φ⟩ = −∂φ/∂x_i(0)  (dipole source)      │
  └────────────────────────────────────────────────────────────────┘

  FUNDAMENTAL IDENTITY:
  f(x)·δ(x−y) = f(y)·δ(x−y)
  ∫ f(x)·δ(x−y) dx = f(y)
```

---

## Green's Function: Formal Definition

```
  For a linear PDE operator L acting on functions u(x) in domain Ω:

  Lu = f  in Ω,  with homogeneous BCs

  GREEN'S FUNCTION G(x,y) satisfies:
  ┌──────────────────────────────────────────────────────────────┐
  │  L_x G(x,y) = δ(x−y)   in Ω  (for each fixed y)              │
  │  G(x,y) satisfies the homogeneous BCs in x                   │
  └──────────────────────────────────────────────────────────────┘

  SOLUTION:  u(x) = ∫_Ω G(x,y) f(y) dy

  PHYSICAL MEANING:
  G(x,y) = response at x to a unit point source at y.
  The solution is a superposition (integral) of responses to
  each infinitesimal bit of source.

  SYMMETRY:  G(x,y) = G(y,x)
  (consequence of self-adjointness of L — true for L = −∇²)
```

---

## Green's Function for Laplace Operator

### Free Space

```
  L = −∇²,  Ω = R^n

  LG = δ(x−y):  −∇²_x G(x,y) = δ(x−y)

  SOLUTION (fundamental solution):
  G(x,y) = Φ(x−y)

  n=1:  G(x,y) = −½|x−y|
  n=2:  G(x,y) = −1/(2π) log|x−y|
  n=3:  G(x,y) = 1/(4π|x−y|)

  Note: in 3D, G = 1/(4π|x−y|) is the Coulomb potential.
  This is the electric potential at x due to a unit charge at y.
```

### Half-Space (Method of Images)

```
  L = −∇²,  Ω = {x : x_n > 0},  G=0 on ∂Ω

  IDEA: place a negative "image" source at the reflection y* of y
  across the boundary. This cancels the boundary value.

  y = (y', y_n) → y* = (y', −y_n)  (reflection across x_n=0)

  G(x,y) = Φ(x−y) − Φ(x−y*)

  3D:  G(x,y) = 1/(4π) [1/|x−y| − 1/|x−y*|]

  POISSON KERNEL (response on boundary → interior):
  ∂G/∂n_y(x,y)|_{y_n=0} = −x_n / [2π(|x'−y'|² + x_n²)^{3/2}]

  Dirichlet solution:
  u(x) = −∫_{y_n=0} ∂G/∂n_y (x,y) g(y') dA(y')
        = x_n/(2π) ∫_{R^2} g(y')/(|x'−y'|²+x_n²)^{3/2} dA(y')
```

### Ball (Kelvin Inversion)

```
  L = −∇²,  Ω = B_R = {|x| < R},  G=0 on ∂Ω

  For source at y ∈ B_R:
  Reflected point: y* = (R/|y|)² y  (Kelvin inversion through sphere)

  3D:  G(x,y) = 1/(4π) [1/|x−y| − R/(|y||x−y*|)]

  POISSON INTEGRAL FORMULA:
  For u harmonic in B_R with u=g on ∂B_R:

  u(x) = (R² − |x|²)/(nω_n R) ∫_{|y|=R} g(y)/|x−y|^n dσ(y)

  At center x=0:
  u(0) = 1/(nω_n R^{n-1}) ∫_{|y|=R} g(y) dσ(y) = average of g on sphere

  This is the MEAN VALUE THEOREM.
```

---

## Green's Function for the Heat Equation

```
  L = ∂_t − α∇²,  Ω = R^n × (0,∞)

  G(x,t; y,s) = response at (x,t) to point source at (y,s), s < t:

  G(x,t; y,s) = K(x−y, t−s)
              = (4πα(t−s))^{−n/2} exp(−|x−y|²/4α(t−s))  for t > s
              = 0  for t < s  (causality)

  SOLUTION:
  u(x,t) = ∫_{R^n} G(x,t;y,0) u₀(y) dy
           + ∫₀ᵗ ∫_{R^n} G(x,t;y,s) f(y,s) dy ds

  = (heat kernel * IC) + (spacetime convolution with source)
```

---

## Green's Function for the Wave Equation

```
  L = ∂_t² − c²∇²,  3D case

  RETARDED GREEN'S FUNCTION (causal):
  G(x,t; y,s) = δ(t−s − |x−y|/c) / (4πc|x−y|)

  SUPPORT: only on the light cone |x−y| = c(t−s).
  Zero inside and outside the cone (Huygens' principle in 3D).

  SOLUTION:
  u(x,t) = ∫₀ᵗ ∫_{R³} G(x,t;y,s) f(y,s) dy ds

  For point source at origin:
  u(x,t) = f(t − |x|/c) / (4πc|x|)

  This is the RETARDED POTENTIAL — the source's effect arrives
  at x at time |x|/c after the source fires (at the speed of light).
```

---

## Duhamel's Principle

A general method for converting inhomogeneous problems to homogeneous ones:

```
  PROBLEM: u_tt − c²∇²u = f(x,t),  u(x,0) = u_t(x,0) = 0

  DUHAMEL'S PRINCIPLE:
  Let v(x,t;s) = solution to:
      v_tt − c²∇²v = 0,  v(x,s;s) = 0,  v_t(x,s;s) = f(x,s)
  (homogeneous wave equation, "fired" at time s with "velocity" f(x,s))

  Then:  u(x,t) = ∫₀ᵗ v(x,t;s) ds

  PHYSICAL MEANING:
  Break the source into impulsive contributions δ(t−s)·f(x,s).
  Each impulse fires at time s, generating response v(x,t;s).
  Sum (integrate) all the responses.

  ALSO WORKS for:
  • Heat equation: u_t − α∇²u = f  →  v satisfies homogeneous heat
  • Schrödinger: iℏψ_t − Ĥψ = f
  • Any linear evolution PDE
```

---

## Spectral Representation of Green's Functions

For self-adjoint operators on bounded domains:

```
  L = −∇²  with Dirichlet BCs on Ω.
  Spectral decomposition: L = Σ_n λ_n |φ_n⟩⟨φ_n|

  where λ_n, φ_n are eigenvalues and eigenfunctions:
  −∇²φ_n = λ_n φ_n,  φ_n = 0 on ∂Ω,  ∫ φ_n φ_m = δ_{nm}

  GREEN'S FUNCTION:
  G(x,y) = Σ_n φ_n(x)φ_n(y) / λ_n

  HEAT KERNEL:
  K(x,y,t) = Σ_n φ_n(x)φ_n(y) · e^{−λ_n t}

  WAVE KERNEL:
  W(x,y,t) = Σ_n φ_n(x)φ_n(y) · cos(√λ_n · t)

  RESOLVENTS:
  (L − z)⁻¹(x,y) = G_z(x,y) = Σ_n φ_n(x)φ_n(y) / (λ_n − z)

  This is the bridge between Green's functions and spectral theory.
  The poles of the resolvent are the eigenvalues.
```

---

## Connections to Signal Processing and Machine Learning

```
  SIGNAL PROCESSING PARALLELS:

  Convolution with Green's function     = Convolution with impulse response
  Fourier transform of G                = Transfer function H(ω)
  Poles of G(z) = eigenvalues of L      = Poles of H(ω) = resonant frequencies

  KERNEL METHODS IN ML:

  A "kernel" k(x,y) in ML (Gaussian process, SVM, kernel regression)
  is exactly a Green's function. The reproducing kernel Hilbert space
  (RKHS) associated with a kernel k is the Sobolev space H^s where
  k = Green's function of (I + (−∇²))^s or similar operator.

  Gaussian kernel k(x,y) = e^{−|x−y|²/2σ²}
  = (up to scaling) Green's function of a heat operator.

  NEURAL NETWORK ANALOGY:
  A neural ODE dx/dt = f(x,t) with continuous depth → Lagrangian
  formulation where the optimal path satisfies a variational principle.
  The backward pass (adjoint method) computes the "time-reversed Green's
  function" of the linearized dynamics.
```

---

## Numerical Computation of Green's Functions

```
  DIRECT METHODS (small problems):
  • Invert the discretized operator matrix: G ≈ A⁻¹
    where A = stiffness matrix from FEM/FD.
  • Expensive: O(n³) for n degrees of freedom.
  • Only feasible for n up to ~10⁴-10⁵.

  BOUNDARY ELEMENT METHOD (BEM):
  • Use the free-space Green's function analytically.
  • Reduce volume problem to surface integral equation.
  • Discretize only the boundary, not the volume.
  • n_boundary << n_volume → much cheaper.
  • But produces a DENSE matrix (not sparse like FEM).
  • Accelerated by FMM (Fast Multipole Method): O(n log n).

  FAST ALGORITHMS:
  • Fast Multipole Method (FMM): O(n) Green's function evaluations.
  • H-matrices / HSS matrices: hierarchical low-rank compression.
  • Panel clustering: adaptive accuracy for far-field interactions.
```

---

## Decision Cheat Sheet

| Problem | Green's Function | Notes |
|---------|-----------------|-------|
| Poisson in R³ | G = 1/(4π|x−y|) | Coulomb potential |
| Poisson in half-space | Images + Φ | Reflection across boundary |
| Poisson in ball | Kelvin inversion | G = Φ(x−y) − (R/|y|)Φ(x−y*) |
| Heat equation on R^n | G = Gaussian heat kernel | Causal (t > s) |
| Wave equation on R³ | G = δ(t−s−|x−y|/c)/(4πc|x−y|) | Retarded, Huygens |
| General bounded domain | Spectral expansion G = Σ φ_nφ_n/λ_n | Eigenfunction expansion |
| Inhomogeneous PDE → homogeneous | Duhamel's principle | Works for all linear evolution |

---

## Common Confusion Points

**"Green's function vs. fundamental solution — same thing?"**
In free space, yes. In a bounded domain with BCs, no: the fundamental solution Φ satisfies
∇²Φ = δ without any BCs, while the Green's function G satisfies ∇²G = δ AND the BCs.
G = Φ + (correction to enforce BCs). The correction is harmonic (solves the homogeneous
equation) and cancels Φ on the boundary.

**"The Green's function is symmetric G(x,y) = G(y,x). Isn't this obvious for a self-adjoint
operator?"**
Exactly right — and this is the content. Self-adjointness of L means ⟨Lu,v⟩ = ⟨u,Lv⟩.
Applying with u = G(·,x) and v = G(·,y): G(y,x) = G(x,y). The symmetry is a consequence
of self-adjointness, which in physics terms means reciprocity: the response at x to a source
at y equals the response at y to a source at x. (Reciprocity theorem in acoustics, EM, etc.)

**"What's the difference between the retarded and advanced Green's functions?"**
Retarded: G(x,t;y,s) = 0 for t < s (causal — effect follows cause).
Advanced: G(x,t;y,s) = 0 for t > s (anti-causal).
Both solve LG = δ. Physics selects the retarded one (causality principle).
The difference G_retarded − G_advanced is the causal propagator, which solves the
homogeneous wave equation and is related to the free-field commutator in quantum field theory.
