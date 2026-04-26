# Vector Calculus — The Language of Maxwell's Equations

## The Big Picture

```
+------------------------------------------------------------------------+
|                     VECTOR CALCULUS LANDSCAPE                          |
|                                                                        |
|   COORDINATE EXPRESSION (R³)          COORDINATE-FREE                  |
|   ─────────────────────────────        (Exterior Calculus)             |
|                                                                        |
|   f: R³→R   ──── ∇  (gradient) ──>  F: R³→R³   ≡  d on 0-forms       |
|   F: R³→R³  ──── ∇· (divergence) → f: R³→R     ≡  ★d★ on 2-forms     |
|   F: R³→R³  ──── ∇× (curl) ──────> F: R³→R³   ≡  ★d on 1-forms       |
|   f: R³→R   ──── ∇² (Laplacian) → f: R³→R     ≡  ★d★d on 0-forms     |
|                                                                        |
|   INPUT TYPE        OPERATOR          OUTPUT TYPE     PHYSICAL MEANING |
|   scalar field      gradient          vector field    steepest ascent  |
|   vector field      divergence        scalar field    source/sink rate |
|   vector field      curl              vector field    local rotation   |
|   scalar field      Laplacian         scalar field    vs. neighbors    |
|                                                                        |
|   COORDINATE-FREE LAYER: exterior calculus (differential forms)        |
|   d²=0 is ONE identity that encodes ∇×(∇f)=0 and ∇·(∇×F)=0          |
+------------------------------------------------------------------------+
```

**The coordinate/coordinate-free split.** Vector calculus is the classical, Cartesian coordinate expression of exterior calculus on R³. The gradient is the exterior derivative d acting on a 0-form. Curl is ★d acting on a 1-form (where ★ is the Hodge star, converting between k-forms and (3-k)-forms via the metric). Divergence is ★d★ acting on a 1-form. The single identity d²=0 is what makes both ∇×(∇f)=0 and ∇·(∇×F)=0 true — they are the same equation in different degrees. In this file, all operators are expressed in Cartesian coordinates; the differential-forms viewpoint makes the structure coordinate-free and generalizes to curved spaces (Riemannian geometry).

**Why this matters immediately** — Maxwell's four equations in differential form:

```
  ∇·E  = ρ/ε₀          Gauss's Law (electric charges create E fields)
  ∇·B  = 0             No magnetic monopoles (B has no sources)
  ∇×E  = -∂B/∂t        Faraday's Law (changing B creates E)
  ∇×B  = μ₀J + μ₀ε₀∂E/∂t   Ampere-Maxwell (current + changing E creates B)
```

Four equations. Two operators (divergence and curl). By the end of this guide
those symbols will read as sentences, not notation.

---

## What Is a Field?

Before the operators, the objects they act on.

A **scalar field** assigns one number to each point in space:

```
  f : R³ → R

  Examples:
    T(x,y,z) — temperature at every point in a room
    V(x,y,z) — electric potential (voltage) at every point
    p(x,y,z) — air pressure at every point in the atmosphere
```

A **vector field** assigns one vector (magnitude + direction) to each point in space:

```
  F : R³ → R³

  Examples:
    E(x,y,z) — electric field vector at every point
    B(x,y,z) — magnetic field vector at every point
    v(x,y,z) — fluid velocity at every point in a flow
    g(x,y,z) — gravitational field at every point near Earth
```

This is the key mental model for E&M: **E and B are vector fields**. At every
point in space, there is an E arrow and a B arrow. Maxwell's equations are
statements about how those arrows behave — where they point, where they spread
out, where they rotate.

---

## Foundation: Partial Derivatives

You know derivatives. The extension to multiple variables is direct.

For f(x, y, z), the **partial derivative with respect to x** treats y and z as
constants and differentiates as normal:

```
  f(x, y) = x²y + 3y

  ∂f/∂x = 2xy          (y is a constant multiplier)
  ∂f/∂y = x² + 3       (x² is a constant, 3y → 3)
```

Notation: ∂ (curly d) signals "partial" — only one variable moves, the rest freeze.

**Second partials** — differentiate twice:

```
  ∂²f/∂x² = 2y
  ∂²f/∂y² = 0
```

**Mixed partials** — differentiate in different variables (order doesn't matter for
smooth functions — this is Clairaut's theorem):

```
  ∂²f/∂x∂y = ∂/∂x (∂f/∂y) = ∂/∂x (x² + 3) = 2x
  ∂²f/∂y∂x = ∂/∂y (∂f/∂x) = ∂/∂y (2xy)   = 2x  ✓ same
```

That's the entire calculus machinery you need to rebuild. Everything below
assembles these partial derivatives into operators.

---

## The Del Operator ∇

The del operator (nabla) is a **vector of partial derivative operations**:

```
         ∂          ∂          ∂
  ∇  =  ─── x̂  +  ─── ŷ  +  ─── ẑ
        ∂x         ∂y         ∂z
```

Where x̂, ŷ, ẑ are unit vectors pointing along the three coordinate axes.

∇ is not a number or a vector. It is an **operator** — it does something to
whatever you put to its right. How you apply it (multiply, dot, cross) determines
which of the four tools you get.

---

## Gradient: ∇f

**Apply ∇ to a scalar field** — ordinary multiplication (each component acts on f):

```
           ∂f         ∂f         ∂f
  ∇f  =   ─── x̂  +  ─── ŷ  +  ─── ẑ
           ∂x         ∂y         ∂z
```

**Output**: a vector field. At each point in space, the gradient is an arrow.

**Physical intuition**: The gradient points in the direction of steepest increase
of f, and its magnitude is the rate of that increase.

```
  TOPOGRAPHIC MAP (top view — contour lines of equal elevation f)

        f=50 ─────────────────────
        f=40 ─────────────────────
        f=30 ─────────────────────       ∇f arrows point
        f=20 ─────────────────────  →→→  perpendicular to
        f=10 ─────────────────────       contour lines,
        f=0  ─────────────────────       uphill
```

Contour lines = equal value of f. The gradient is always perpendicular to
contour lines, pointing toward higher values.

**Example**: T(x,y,z) = 3x² + 2y + z

```
  ∂T/∂x = 6x,   ∂T/∂y = 2,   ∂T/∂z = 1

  ∇T = 6x x̂ + 2 ŷ + ẑ
```

At the point (1, 0, 0): ∇T = 6x̂ + 2ŷ + ẑ
Heat flows opposite to ∇T — from hot toward cold, i.e., in direction -∇T.

**In Maxwell**: Electric field E = -∇V (electric field is the negative gradient of
electric potential). This is why high voltage → strong E field: steep gradient.

---

## Divergence: ∇·F

**Apply ∇ to a vector field via dot product**:

```
  F = Fx x̂ + Fy ŷ + Fz ẑ

         ∂Fx   ∂Fy   ∂Fz
  ∇·F =  ─── + ─── + ───
          ∂x    ∂y    ∂z
```

**Output**: a scalar field. At each point, one number.

**Physical intuition**: Divergence measures how much the field **spreads out**
(sources) or **converges** (sinks) at a point.

```
  ∇·F > 0  at a point:   SOURCE — field arrows radiate outward
  ∇·F < 0  at a point:   SINK   — field arrows converge inward
  ∇·F = 0  at a point:   field passes through without accumulating


  SOURCE (∇·F > 0)       SINK (∇·F < 0)       UNIFORM (∇·F = 0)
      ↑↗ →                  → ↘ ↓                  → → →
     ↑  ·  →               ↑  ·  ↓                 → · →
      ↖↙ ←                  ← ↗ ↑                  → → →
```

**Physical example** — incompressible fluid (water):
- ∇·v = 0 everywhere: no sources, no sinks, water just flows through
- ∇·v > 0 at a point: water is being pumped in there
- ∇·v < 0 at a point: water is draining there

**In Maxwell**:
- ∇·E = ρ/ε₀ : Electric field has divergence where there is charge ρ.
  Positive charge is a source of E field lines. Negative charge is a sink.
  No charge → ∇·E = 0 → E field lines don't start or stop there.
- ∇·B = 0 : Magnetic field has **zero divergence everywhere**.
  There are no magnetic monopoles — no sources or sinks for B field lines.
  Every B field line that enters a region must also exit it.

---

## Curl: ∇×F

**Apply ∇ to a vector field via cross product**:

```
  ∇×F = det | x̂      ŷ      ẑ   |
             | ∂/∂x  ∂/∂y  ∂/∂z |
             | Fx     Fy     Fz   |

       = (∂Fz/∂y - ∂Fy/∂z) x̂
       + (∂Fx/∂z - ∂Fz/∂x) ŷ
       + (∂Fy/∂x - ∂Fx/∂y) ẑ
```

Use the determinant form to remember it — expand along the first row.

**Output**: a vector field. At each point, a vector indicating rotation axis and strength.

**Physical intuition**: Curl measures the **local rotation** of the field at a point.
Imagine dropping a tiny paddle wheel into a fluid flow — if the paddle wheel spins,
the curl is nonzero. The direction of the curl vector is the axis of rotation
(right-hand rule: curl your right-hand fingers in the rotation direction, thumb
points along ∇×F).

```
  CURL = 0                    CURL ≠ 0
  (no local rotation)         (local rotation present)

    → → →                       ↑ ← ←
    → → →                       ↑  ·  ←   ∇×F points out of page
    → → →                       ↑ → →
```

**Careful**: A field can go around in a big circle globally while having zero curl
at every point — curl is a *local* measurement. This subtlety is what Stokes'
theorem (next module) resolves.

**Example**: F = -y x̂ + x ŷ (field that rotates counterclockwise around origin)

```
  ∂Fx/∂y = -1,  ∂Fy/∂x = 1,  all other relevant partials = 0

  ∇×F = (∂Fy/∂x - ∂Fx/∂y) ẑ = (1 - (-1)) ẑ = 2ẑ
```

Curl points in +z direction (out of page), magnitude 2. Uniform rotation.

**In Maxwell**:
- ∇×E = -∂B/∂t : A changing magnetic field creates a curling electric field.
  This is Faraday's law — the operating principle of every generator ever built.
- ∇×B = μ₀J + μ₀ε₀∂E/∂t : Current J and changing electric fields create
  curling magnetic fields. The μ₀ε₀∂E/∂t term is Maxwell's addition —
  without it, the equations are inconsistent, and EM waves don't exist.

---

## Laplacian: ∇²f

**Divergence of the gradient** — apply ∇· to ∇f:

```
  ∇²f = ∇·(∇f) = ∂²f/∂x² + ∂²f/∂y² + ∂²f/∂z²
```

Output: a scalar field.

**Physical intuition**: At each point, ∇²f measures how much f at that point
**differs from the average value** of its immediate neighbors.

```
  ∇²f > 0 at point P:  f(P) is BELOW the local average — a valley
  ∇²f < 0 at point P:  f(P) is ABOVE the local average — a peak
  ∇²f = 0 at point P:  f(P) equals its local average — saddle or flat
```

**Laplace's equation**: ∇²f = 0 everywhere — called a **harmonic function**.
Solutions have no local maxima or minima in the interior. Electric potential V
satisfies ∇²V = 0 in free space (no charges). Solving Laplace's equation is
most of classical electrostatics.

**Poisson's equation**: ∇²V = -ρ/ε₀ — electric potential with charge present.
Generalization of Laplace's equation. Shows up constantly in E&M.

**Example**: f(x,y,z) = x² + y² - 2z²

```
  ∂²f/∂x² = 2,   ∂²f/∂y² = 2,   ∂²f/∂z² = -4

  ∇²f = 2 + 2 + (-4) = 0    ← harmonic function
```

---

## The Operators Together

```
+-------------------------------------------------------------------+
|                                                                   |
|   SCALAR FIELD f                         VECTOR FIELD F           |
|                                                                   |
|        │ ∇ (gradient)          ∇· (divergence) │                  |
|        ▼                                        ▼                 |
|   VECTOR FIELD ∇f              SCALAR FIELD ∇·F                   |
|        │                                                          |
|        │ ∇· (divergence of gradient)                              |
|        ▼                                                          |
|   SCALAR FIELD ∇²f = ∇·(∇f)   ← Laplacian                       |
|                                                                   |
|   VECTOR FIELD F                                                  |
|        │ ∇× (curl)                                                |
|        ▼                                                          |
|   VECTOR FIELD ∇×F                                                |
|                                                                   |
+-------------------------------------------------------------------+
```

**Two identities you will use constantly**:

```
  ∇×(∇f) = 0        curl of any gradient is zero
  ∇·(∇×F) = 0       divergence of any curl is zero
```

These are not coincidences — they follow directly from mixed partial symmetry
(∂²f/∂x∂y = ∂²f/∂y∂x). They have deep consequences in E&M:
- ∇·B = 0 is consistent with writing B = ∇×A (the vector potential)
- ∇×E = 0 in static fields is consistent with writing E = -∇V

**The Helmholtz decomposition precursor**:

```
  ∇²F = ∇(∇·F) − ∇×(∇×F)
```

This vector identity is the key step in deriving the EM wave equations from
Maxwell's equations. Apply it to E in free space (ρ=0, J=0):

```
  Take ∇× of Faraday:  ∇×(∇×E) = -∂/∂t(∇×B) = -μ₀ε₀ ∂²E/∂t²

  Using the identity:  ∇(∇·E) - ∇²E = -μ₀ε₀ ∂²E/∂t²

  Since ∇·E = 0 in free space:  ∇²E = μ₀ε₀ ∂²E/∂t²

  This is the wave equation with speed c = 1/√(μ₀ε₀) ≈ 3×10⁸ m/s.
```

Maxwell's identification of light as an electromagnetic wave follows directly
from this identity and his addition of the displacement current term.

---

## Preview: Maxwell Decoded

With these operators in hand, Maxwell's equations are now readable:

```
  ∇·E = ρ/ε₀
  ─────────────────────────────────────────────────────────────────
  "The divergence of the electric field at a point equals the charge
   density there (divided by ε₀). Electric field lines start on
   positive charges and end on negative charges."


  ∇·B = 0
  ─────────────────────────────────────────────────────────────────
  "The magnetic field has zero divergence everywhere. There are no
   magnetic monopoles. Every B field line that enters a region must
   exit it."


  ∇×E = -∂B/∂t
  ─────────────────────────────────────────────────────────────────
  "The curl of the electric field equals the negative rate of change
   of the magnetic field. A changing B field induces a curling E field.
   This is how generators work."


  ∇×B = μ₀J + μ₀ε₀ ∂E/∂t
  ─────────────────────────────────────────────────────────────────
  "The curl of the magnetic field is caused by electric current J
   and by a changing electric field. The second term (Maxwell's
   addition) is what allows electromagnetic waves to propagate
   through empty space."
```

---

## Curvilinear Coordinates

The Cartesian formulas above are coordinate-specific. In spherical and cylindrical
coordinates — used constantly in E&M, QM, and fluid dynamics — the operators
take different forms because the basis vectors vary from point to point.

**Spherical coordinates** (r, θ, φ) where r = radius, θ = polar angle from z-axis,
φ = azimuthal angle in xy-plane:

```
  ∇f = ∂f/∂r r̂  +  (1/r) ∂f/∂θ θ̂  +  (1/(r sinθ)) ∂f/∂φ φ̂

  ∇·F = (1/r²) ∂(r²Fᵣ)/∂r  +  (1/(r sinθ)) ∂(sinθ Fθ)/∂θ
             +  (1/(r sinθ)) ∂Fφ/∂φ

  ∇²f = (1/r²) ∂/∂r(r² ∂f/∂r)  +  (1/(r² sinθ)) ∂/∂θ(sinθ ∂f/∂θ)
             +  (1/(r² sin²θ)) ∂²f/∂φ²

  (∇×F)ᵣ = (1/(r sinθ))[∂(sinθ Fφ)/∂θ − ∂Fθ/∂φ]
  (∇×F)θ = (1/r)[(1/sinθ) ∂Fᵣ/∂φ − ∂(rFφ)/∂r]
  (∇×F)φ = (1/r)[∂(rFθ)/∂r − ∂Fᵣ/∂θ]
```

**Cylindrical coordinates** (ρ, φ, z) where ρ = radial distance in xy-plane:

```
  ∇f = ∂f/∂ρ ρ̂  +  (1/ρ) ∂f/∂φ φ̂  +  ∂f/∂z ẑ

  ∇·F = (1/ρ) ∂(ρFᵨ)/∂ρ  +  (1/ρ) ∂Fφ/∂φ  +  ∂Fz/∂z

  ∇²f = (1/ρ) ∂/∂ρ(ρ ∂f/∂ρ)  +  (1/ρ²) ∂²f/∂φ²  +  ∂²f/∂z²

  (∇×F)z = (1/ρ) ∂(ρFφ)/∂ρ − (1/ρ) ∂Fᵨ/∂φ    (z-component — most common)
```

The conceptual operators (gradient, divergence, curl, Laplacian) are the same
in all coordinate systems. Only the coordinate expression changes because the
metric tensor (the inner product structure) is different. In spherical coordinates
the metric is ds² = dr² + r²dθ² + r²sin²θ dφ² — the r-dependent scale factors
propagate into every operator formula.

**Key application**: the Laplacian in spherical coordinates separates into radial
and angular parts. The angular part is the Laplace-Beltrami operator on S² whose
eigenfunctions are the spherical harmonics Yₗᵐ(θ,φ). This is why hydrogen orbital
wavefunctions factor as Rₙₗ(r)Yₗᵐ(θ,φ).

---

## Distributional Extensions

The operators above are defined for smooth fields. Physics requires more:

**Point charges** produce E fields with ∇·E = ρ/ε₀ where ρ is a Dirac delta
function, not a smooth function. The delta distribution δ³(r) satisfies:

```
  ∫ δ³(r) dV = 1     (unit charge when integrated)
  ∇·(r̂/r²) = 4π δ³(r)   (the fundamental divergence identity)
```

This identity is the core of Coulomb's law — it is what makes ∮ E·dA = Q/ε₀
work for a point charge, where the integrand has a non-smooth source.

**Weak derivatives** extend differentiation to functions in Sobolev spaces
H^k(Ω). A function u has a weak partial derivative v = ∂u/∂xᵢ if for all
smooth test functions φ with compact support:

```
  ∫ u (∂φ/∂xᵢ) dV = − ∫ v φ dV      (integration by parts, moved to test fn)
```

This lets you apply the divergence theorem and Green's identities to functions
that are only L² (square-integrable), not classically differentiable. The
entire framework of finite-element methods rests on weak derivatives — the PDE
is enforced in the weak (integral against test functions) sense, which allows
piecewise-polynomial approximations that aren't differentiable at element boundaries.

**Shock waves in fluid dynamics**: the compressible Euler equations can develop
discontinuous solutions (shocks). The correct formulation is in weak form —
the conservation laws (mass, momentum, energy) hold in integral form across
the discontinuity, giving the Rankine-Hugoniot jump conditions.

---

## Connections to Adjacent Mathematics

**Differential forms and exterior calculus.** The coordinate-free version of
vector calculus. A 0-form is a scalar field, a 1-form is what line-integrates
naturally (locally F·dl), a 2-form flux-integrates over surfaces, a 3-form
volume-integrates. The exterior derivative d: k-forms → (k+1)-forms satisfies
d²=0 and unifies all four vector calculus operators. The identities ∇×(∇f)=0
and ∇·(∇×F)=0 are both d²=0 in disguise. Stokes' theorem, the divergence
theorem, and the gradient theorem are all ∫_M dω = ∫_{∂M} ω. See module 02
for the integral form; the full exterior calculus machinery is in
differential-geometry/.

**Riemannian geometry.** On a manifold with metric tensor g, the inner product
used to define gradient (raise index) and divergence (contract with metric
determinant) changes. The Laplace-Beltrami operator ∇²f = (1/√g) ∂ᵢ(√g gⁱʲ ∂ⱼf)
reduces to the Cartesian Laplacian when gᵢⱼ = δᵢⱼ and to the spherical form
above when expressed in spherical coordinates. General relativity replaces all
of this with covariant derivatives on a pseudo-Riemannian manifold.

**Complex analysis in 2D.** In R², the Cauchy-Riemann equations for f = u+iv
to be holomorphic are exactly ∂u/∂x = ∂v/∂y and ∂u/∂y = −∂v/∂x. The first
is ∇·F = 0 (divergence-free) and the second is (∇×F)_z = 0 (curl-free), where
F = (u,v). Holomorphic functions are precisely the 2D vector fields that are
simultaneously divergence-free and curl-free — conformal maps of the plane.

**Automatic differentiation.** JAX and PyTorch compute ∇f via reverse-mode AD
(backpropagation), which gives the full gradient in O(forward pass) time
regardless of dimension. The Jacobian ∂Fᵢ/∂xⱼ (the matrix of partial
derivatives) is computed via forward-mode or reverse-mode AD. Divergence
(trace of Jacobian) and curl can be extracted from the Jacobian matrix.
For a neural network f: Rⁿ→R, the gradient ∇f ∈ Rⁿ is exactly what
backprop computes. `jax.grad`, `torch.autograd.grad`.

**Numerical computation.** On a discrete grid with spacing h:
```
  (∂f/∂x)ᵢ ≈ (f(x+h) − f(x−h)) / 2h        (centered finite difference)
  (∇·F)ᵢ   ≈ (Fₓ(x+h) − Fₓ(x−h))/2h + ...  (component sum)
  (∇²f)ᵢ   ≈ (f(i+1) + f(i-1) − 2f(i)) / h²  (1D Laplacian stencil)
```
In NumPy: `np.gradient(f, h)` computes ∇f on a grid.
In SciPy: `scipy.ndimage.laplace(f)` computes ∇²f using the 3×3 stencil.
The finite-volume method (used in CFD) discretizes the divergence theorem
directly — it enforces ∇·F = 0 in integral form over each mesh cell, which
automatically conserves the diverged quantity to machine precision.

---

## Decision Cheat Sheet

| You have | You want to know | Operator | Output | When to use |
|----------|-----------------|----------|--------|-------------|
| Scalar field f | Which direction changes fastest | ∇f | Vector field | Gradient descent, E = -∇V |
| Scalar field f | Is this point above/below neighbors | ∇²f | Scalar field | Laplace/Poisson equations |
| Vector field F | Is there a source or sink here | ∇·F | Scalar field | Gauss's law, continuity eq. |
| Vector field F | Is there local rotation here | ∇×F | Vector field | Faraday/Ampere, vorticity |
| Vector field F | Can I write F = ∇f (conservative) | Check ∇×F = 0 | Yes/No | Path independence, potential |
| Vector field F | Can I write F = ∇×A (solenoidal) | Check ∇·F = 0 | Yes/No | Magnetic vector potential |
| Any | Need coordinate-free version | Exterior calculus | k-forms | Curved spaces, manifolds |
| Any | Need numerical computation | Finite differences | Grid values | CFD, FEM, PDE solvers |

---

## Common Confusion Points

**∇ is not a vector, it is an operator.**
Writing ∇ = ∂/∂x x̂ + ∂/∂y ŷ + ∂/∂z ẑ is notation that lets you use dot/cross
product rules to derive the gradient/divergence/curl formulas. Don't try to
"evaluate" ∇ alone — it only makes sense when applied to something.

**Divergence-free ≠ zero field.**
∇·F = 0 everywhere means no sources or sinks. The field can still be large and
point strongly in a direction. A uniform field → → → has ∇·F = 0 because
∂Fx/∂x = 0 (constant). The B field in a region far from any magnet can be
uniform and nonzero but still ∇·B = 0.

**Curl-free ≠ no circulation.**
A field can go around in a big loop globally while having ∇×F = 0 at every point
inside the loop — if there is a singularity (like a wire carrying current) at the
center. This is Stokes' theorem territory (next module). The classic example is
the magnetic field around a long straight wire.

**The Laplacian of a vector field ∇²F applies component-wise.**
∇²F = (∇²Fx) x̂ + (∇²Fy) ŷ + (∇²Fz) ẑ. Same operator, applied to each
scalar component separately. This appears in the wave equation for E and B.

**These formulas are Cartesian.**
In spherical coordinates (which you will use constantly in E&M — charges are
spherical, atoms are spherical), the gradient, divergence, and curl formulas
look different. The full spherical and cylindrical forms are given above in
the "Curvilinear Coordinates" section.

**∂B/∂t is a partial time derivative.**
Maxwell's equations also involve time. ∂B/∂t means: at a fixed point in space,
how fast is B changing in time? The full machinery of electrodynamics treats
fields as functions of both space and time: E(x,y,z,t), B(x,y,z,t).
