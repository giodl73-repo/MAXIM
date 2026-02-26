# Integral Theorems — The Bridge Between Maxwell's Two Forms

## The Big Picture

Maxwell's equations exist in two equivalent forms. The integral theorems are
exactly what converts between them.

```
+------------------------------------------------------------------------+
|              THE TWO FORMS OF MAXWELL'S EQUATIONS                      |
|                                                                        |
|   DIFFERENTIAL FORM              INTEGRAL FORM                        |
|   (local — at a point)           (global — over regions)              |
|   ─────────────────────          ──────────────────────               |
|                                                                        |
|   ∇·E  = ρ/ε₀        ←────────→  ∮∮ E·dA = Q_enc/ε₀                 |
|   ∇·B  = 0           ←────────→  ∮∮ B·dA = 0                         |
|   ∇×E  = -∂B/∂t      ←────────→  ∮ E·dl  = -dΦ_B/dt                 |
|   ∇×B  = μ₀J+...     ←────────→  ∮ B·dl  = μ₀I_enc + ...            |
|                                                                        |
|        ↑                                  ↑                           |
|   (module 01)              DIVERGENCE THEOREM + STOKES' THEOREM       |
|                                  (this module)                        |
+------------------------------------------------------------------------+
```

Two theorems do all the conversion:

```
  DIVERGENCE THEOREM:   ∫∫∫_V (∇·F) dV  =  ∮∮_S F·dA
                        volume integral      surface integral
                        of divergence        of flux (boundary)

  STOKES' THEOREM:      ∫∫_S (∇×F)·dA   =  ∮_C F·dl
                        surface integral     line integral
                        of curl              of circulation (boundary)
```

There is a single deeper pattern here — the generalized Stokes' theorem of
differential geometry — developed in the next section.

---

## The Three Integration Domains

Before the theorems, the integrals they connect.

```
  1D: LINE INTEGRAL          2D: SURFACE INTEGRAL       3D: VOLUME INTEGRAL
  ─────────────────          ────────────────────       ───────────────────
  Integrate along            Integrate over a           Integrate over a
  a curve C                  surface S                  volume V

      C                           S                          V
   ·─────·                   ___________                 ___________
   a     b                  /           \               /           \
                            \___________/               \___________/

  ∫_C F·dl                  ∫∫_S F·dA                  ∫∫∫_V f dV
```

---

## Line Integrals: ∫_C F·dl

Integrate a vector field F along a curve C from point a to point b.

**What dl is**: a tiny vector tangent to the curve, pointing in the direction
of travel, with magnitude = arc length element ds.

```
  curve C:    a ──────────────────────── b
                      →   →   →
              dl  dl  dl  dl  dl         (tiny tangent vectors)
```

**F·dl at each point**: dot product = |F||dl|cos θ where θ is angle between
F and the curve direction. Measures how much of F is aligned with the path.

**Physical meaning**: Work done by force F moving along path C.

```
  W = ∫_C F·dl
```

If F is perpendicular to the path everywhere, F·dl = 0 — no work done.
If F is parallel to the path everywhere, F·dl = |F|ds — maximum work.

**In E&M**: Voltage (potential difference) between two points:

```
  V_ab = -∫_a^b E·dl

  The work done per unit charge moving against E from a to b.
  This is why voltage = energy per charge.
```

**Closed line integral** ∮_C F·dl : integrate all the way around a closed loop.
Notation: the circle on the integral sign means the path is closed.

---

## Surface Integrals: ∫∫_S F·dA

Integrate a vector field F over a surface S.

**What dA is**: a tiny vector perpendicular (normal) to the surface at each
point, with magnitude = area element dS. For a closed surface, dA points
outward by convention.

```
  surface S:

         ↑ dA (normal vector, perpendicular to surface)
         |
    ─────┼─────
   /     ·     \      ← tiny area element, dA = n̂ dS
  /             \
```

**F·dA at each point**: measures how much of F passes through the surface.

```
  F parallel to surface  →  F·dA = 0  (skims along, doesn't pass through)
  F perpendicular to surface →  F·dA = |F|dS  (maximum throughput)
```

**Physical meaning**: FLUX — how much of the field passes through the surface.

```
  Φ = ∫∫_S F·dA    (flux of F through S)
```

Think of F as water velocity. Flux = volume of water crossing the surface
per unit time. If F is parallel to the surface, no water crosses it.
If F is perpendicular, maximum water crosses it.

**Closed surface integral** ∮∮_S F·dA : integrate over a closed surface
(like a sphere or a box). Measures net outward flux — how much more leaves
than enters.

**In E&M**:
- Electric flux: Φ_E = ∫∫_S E·dA
- Magnetic flux: Φ_B = ∫∫_S B·dA
- Faraday's law involves dΦ_B/dt — rate of change of magnetic flux through a loop

---

## Volume Integrals: ∫∫∫_V f dV

Integrate a scalar field f over a 3D volume V. This is just a triple integral —
nothing new conceptually. The volume element dV = dx dy dz in Cartesian.

**In E&M**: Total charge in a volume:

```
  Q_enc = ∫∫∫_V ρ(x,y,z) dV

  where ρ is charge density (charge per unit volume)
```

---

## The Fundamental Theorem Chain and the Generalized Stokes' Theorem

The pattern across all of calculus:

```
  FUNDAMENTAL THEOREM OF CALCULUS (1D):

    ∫_a^b f'(x) dx  =  f(b) - f(a)
    ─────────────────────────────────
    integral of        values at the
    derivative         boundary points
    over interval


  GRADIENT THEOREM (generalization to paths):

    ∫_C (∇f)·dl  =  f(b) - f(a)
    ────────────────────────────────
    integral of        values at the
    gradient           endpoints
    over path          (boundary of path)


  STOKES' THEOREM (generalization to surfaces):

    ∫∫_S (∇×F)·dA  =  ∮_C F·dl
    ──────────────────────────────────
    integral of        integral over
    curl               the boundary
    over surface       curve of surface


  DIVERGENCE THEOREM (generalization to volumes):

    ∫∫∫_V (∇·F) dV  =  ∮∮_S F·dA
    ──────────────────────────────────
    integral of        integral over
    divergence         the boundary
    over volume        surface of volume
```

**The single unifying theorem** — the generalized Stokes' theorem:

```
  ∫_M dω  =  ∫_{∂M} ω

  Cast of characters:
    M        — oriented k-manifold with boundary (curve, surface, volume, ...)
    ∂M       — the (k-1)-dimensional boundary of M
    ω        — a differential (k-1)-form (the object being integrated)
    dω       — the exterior derivative of ω (a k-form)
    d        — the exterior derivative operator: d: Ω^k → Ω^(k+1), d²=0

  The four classical theorems are special cases in R³:

  k=1: M = curve C, ∂M = {endpoints a,b}, ω = f (0-form), dω = df = ∇f·dl
       → ∫_C df = f(b)−f(a)         ← Gradient theorem (FTC)

  k=2: M = surface S, ∂M = boundary curve C, ω = F·dl (1-form), dω = (∇×F)·dA
       → ∫∫_S (∇×F)·dA = ∮_C F·dl  ← Stokes' theorem

  k=3: M = volume V, ∂M = bounding surface S, ω = F·dA (2-form), dω = (∇·F)dV
       → ∫∫∫_V (∇·F) dV = ∮∮_S F·dA ← Divergence theorem

  The identity d²=0 is why ∇×(∇f)=0 and ∇·(∇×F)=0 hold automatically —
  they are both instances of d(dω)=0 applied to a 0-form and 1-form.
```

**Differential forms dictionary for R³**:

```
  0-form: scalar field f(x,y,z)
  1-form: F₁dx + F₂dy + F₃dz  ↔  vector field F = (F₁,F₂,F₃)
  2-form: F₁dy∧dz + F₂dz∧dx + F₃dx∧dy  ↔  vector field F (via Hodge ★)
  3-form: f dx∧dy∧dz  ↔  scalar field f

  d on 0-forms: d(f) = ∂f/∂x dx + ∂f/∂y dy + ∂f/∂z dz  ↔  gradient ∇f
  d on 1-forms: d(F·dl) = (∇×F)·dA                        ↔  curl
  d on 2-forms: d(F·dA) = (∇·F) dV                        ↔  divergence
```

The metric on R³ (the standard Euclidean inner product) is what the Hodge star ★
uses to convert between k-forms and (3-k)-forms, allowing curl and divergence
to be expressed as d in different degrees. On a general Riemannian manifold,
the same exterior derivative d works, but the metric changes — this is why
Maxwell's equations take the same coordinate-free form in curved spacetime.

---

## Divergence Theorem

```
  ∫∫∫_V (∇·F) dV  =  ∮∮_S F·dA

  where S is the closed surface bounding volume V
```

**Intuition**: Every bit of divergence (source/sink) inside a volume must
show up as net flux through the boundary surface.

If you have a region full of water sources (∇·F > 0 everywhere inside),
all that water must eventually cross the bounding surface — you can count
it locally (integrate divergence) or at the boundary (count outward flux).
Same answer.

```
  INSIDE V:              AT BOUNDARY S:

  · · ·                  ↑   ↑   ↑
  · ⊕ ·   sources  ───>  →   ·   →    outward flux
  · · ·                  ↓   ↓   ↓

  ∫∫∫ ∇·F dV      =      ∮∮ F·dA
  (count sources inside)  (measure outflow at surface)
```

**Applied to Maxwell — Gauss's Law (electric)**:

Start with: ∇·E = ρ/ε₀

Integrate both sides over volume V:

```
  ∫∫∫_V (∇·E) dV = ∫∫∫_V ρ/ε₀ dV

  Apply divergence theorem to left side:
  ∮∮_S E·dA = (1/ε₀) ∫∫∫_V ρ dV

  Right side is just Q_enc/ε₀:

  ∮∮_S E·dA = Q_enc/ε₀
```

This is **Gauss's Law in integral form**. Draw any closed surface (called a
Gaussian surface). The net electric flux through it equals total enclosed
charge divided by ε₀. Electric field lines start on positive charges and
end on negative charges — they don't appear or disappear in empty space.

**Applied to Maxwell — Gauss's Law (magnetic)**:

∇·B = 0  →  ∮∮_S B·dA = 0

Every B field line that enters any closed surface must also exit it.
No magnetic monopoles. If you found one, this equation would need a source
term on the right, like the electric case.

---

## Stokes' Theorem

```
  ∫∫_S (∇×F)·dA  =  ∮_C F·dl

  where C is the closed boundary curve of surface S
```

**Orientation**: right-hand rule links the surface normal direction to the
direction of travel around the boundary. Curl your right-hand fingers in the
direction you traverse C — thumb points in the direction of dA.

**Intuition**: Total rotation over a surface = net circulation around the edge.

Think of a grid of tiny paddle wheels covering the surface. Interior paddle
wheels cancel each other (adjacent wheels spin in opposite directions at
shared edges). Only the boundary contributes net circulation.

```
  INTERIOR CANCELS:        BOUNDARY REMAINS:

  ↻ | ↻ | ↻               →  →  →
  ──+───+──                         ↓
  ↻ | ↻ | ↻    ─────>     ↑        ↓
  ──+───+──                         ↓
  ↻ | ↻ | ↻               ←  ←  ←

  shared edges cancel      net boundary circulation
```

**Applied to Maxwell — Faraday's Law**:

Start with: ∇×E = -∂B/∂t

Integrate both sides over surface S bounded by loop C:

```
  ∫∫_S (∇×E)·dA = ∫∫_S (-∂B/∂t)·dA

  Apply Stokes' theorem to left side:
  ∮_C E·dl = -d/dt ∫∫_S B·dA

  Right side is -dΦ_B/dt (rate of change of magnetic flux):

  ∮_C E·dl = -dΦ_B/dt
```

This is **Faraday's Law in integral form**.

The left side: ∮ E·dl is the EMF — voltage around the closed loop C.
The right side: -dΦ_B/dt is the rate at which magnetic flux through the
loop is changing.

**This is how every generator ever built works.** Spin a coil in a magnetic
field → Φ_B changes → EMF appears around the coil → drives current.

**Applied to Maxwell — Ampere-Maxwell Law**:

∇×B = μ₀J + μ₀ε₀∂E/∂t  →  ∮_C B·dl = μ₀I_enc + μ₀ε₀ dΦ_E/dt

Left side: circulation of B around loop C.
Right side: current through any surface bounded by C, plus displacement current
(Maxwell's addition — the ε₀∂E/∂t term).

---

## Maxwell: Complete Translation Table

```
+──────────────────────────────────────────────────────────────────────+
|         DIFFERENTIAL              INTEGRAL          VIA              |
+──────────────────────────────────────────────────────────────────────+
|                                                                      |
|  ∇·E = ρ/ε₀          ∮∮ E·dA = Q_enc/ε₀         Divergence thm    |
|                                                                      |
|  "E diverges from      "Net E flux through         ∇· integrated    |
|   charges"             closed surface =             over volume      |
|                         charge inside"                               |
+──────────────────────────────────────────────────────────────────────+
|                                                                      |
|  ∇·B = 0              ∮∮ B·dA = 0                Divergence thm    |
|                                                                      |
|  "B has no             "Net B flux through                           |
|   monopoles"           any closed surface = 0"                      |
+──────────────────────────────────────────────────────────────────────+
|                                                                      |
|  ∇×E = -∂B/∂t         ∮ E·dl = -dΦ_B/dt         Stokes' thm       |
|                                                                      |
|  "Changing B           "EMF around a loop =                         |
|   curls E"              rate of flux change"                         |
|                        ← generator equation →                       |
+──────────────────────────────────────────────────────────────────────+
|                                                                      |
|  ∇×B = μ₀J            ∮ B·dl = μ₀I_enc           Stokes' thm       |
|       +μ₀ε₀∂E/∂t            + μ₀ε₀dΦ_E/dt                         |
|                                                                      |
|  "Current and          "B circulation around                        |
|   changing E curl B"    loop = enclosed current                      |
|                         + displacement current"                      |
+──────────────────────────────────────────────────────────────────────+
```

---

## Gradient Theorem (Bonus — Path Independence)

```
  ∫_C (∇f)·dl = f(b) - f(a)
```

If a vector field F = ∇f (F is the gradient of some scalar f), then the
line integral depends only on the endpoints, not the path.

**In E&M**: E = -∇V in electrostatics. Therefore:

```
  ∫_C E·dl = V(a) - V(b)     path independent
  ∮_C E·dl = 0               for any closed loop (static case)
```

This is why voltage is well-defined — it doesn't matter which path you take
between two points, the voltage difference is the same.

**Breaks down** when ∇×E ≠ 0 (time-varying B fields) — then E is not a
pure gradient, and ∮ E·dl ≠ 0. This is Faraday's law.

---

## Green's Theorem and Green's Identities

Green's theorem is the 2D version of Stokes' theorem, and Green's identities
are direct consequences of the divergence theorem that are foundational for
PDE theory.

**Green's theorem** (2D Stokes'):

```
  ∮_C (P dx + Q dy) = ∫∫_D (∂Q/∂x − ∂P/∂y) dA

  where C is the boundary of region D in R²
```

**Green's first identity** (divergence theorem applied to u ∇v):

```
  ∫∫∫_V u ∇²v dV = ∮∮_S u (∇v)·dA − ∫∫∫_V ∇u·∇v dV
```

This is integration by parts for the Laplacian. It says: the Laplacian of v
integrated against u equals the boundary flux term minus the "gradient
interaction" term. Used to prove that harmonic functions satisfy the mean
value property, and to derive weak formulations of Poisson's equation.

**Green's second identity** (subtract the first with u and v exchanged):

```
  ∫∫∫_V (u ∇²v − v ∇²u) dV = ∮∮_S (u ∇v − v ∇u)·dA
```

This is the backbone of:
- **Potential theory**: if ∇²u = 0 and ∇²v = 0 (both harmonic), then the
  volume integral vanishes and the surface integrals are equal.
- **Green's functions**: the fundamental solution G(r, r') to ∇²G = δ³(r−r')
  is derived using Green's second identity. Once you have G, the solution to
  ∇²u = f is u(r) = ∫ G(r,r') f(r') dV'.
- **Boundary element method (BEM)**: Green's second identity lets you convert
  a PDE over a volume into an integral equation on its boundary — reducing
  3D problems to 2D surface calculations.
- **Reciprocity theorems** in acoustics, EM, and elasticity: Green's second
  identity applied to two solutions of the same PDE gives a relationship
  between source and receiver that is symmetric in the two.

**The Green's function connection**: the Dirac delta satisfies
∇²G(r,r') = δ³(r−r'), whose fundamental solution in free space is:

```
  G(r,r') = −1/(4π |r−r'|)      (3D)
  G(r,r') = (1/2π) ln|r−r'|    (2D)
```

Physically: G is the electric potential of a unit point charge. The superposition
principle for electrostatics (∇²V = −ρ/ε₀) gives V(r) = (1/ε₀) ∫ G(r,r') ρ(r') dV'.

---

## De Rham Cohomology — Topology from Analysis

The integral theorems have a topological shadow: the failure of a closed form
to be exact detects holes in the domain.

**Closed vs exact forms**:

```
  Closed form:  dω = 0     (zero exterior derivative)
  Exact form:   ω = dη     (is itself an exterior derivative)

  d²=0 means: every exact form is closed.
  The converse — is every closed form exact? — depends on topology.
```

**De Rham cohomology** measures the failure:

```
  H^k_dR(M) = {closed k-forms} / {exact k-forms}
             = ker(d: Ω^k → Ω^(k+1)) / im(d: Ω^(k-1) → Ω^k)

  If H^k_dR(M) = 0: every closed k-form is exact
  If H^k_dR(M) ≠ 0: there exist closed forms that are NOT exact
                      → the domain has a topological obstruction
```

**What this means for line integrals and Stokes' theorem**:

A vector field F with ∇×F = 0 (curl-free = closed 1-form) has path-independent
line integrals iff F = ∇f (exact 1-form). The obstruction is H¹_dR of the domain:

```
  Simply connected domain (no holes): H¹_dR = 0 → every curl-free F = ∇f

  Domain with a hole (e.g., R²\{0}):  H¹_dR ≅ R
    The 1-form ω = (−y dx + x dy)/(x²+y²) has dω = 0 everywhere
    but ∮_C ω = 2π for any loop C encircling the origin
    → ω is closed but NOT exact; the hole makes F ≠ ∇f globally.
```

In E&M: the magnetic field around a long straight wire has ∇×B = 0 outside
the wire but ∮ B·dl = μ₀I ≠ 0. The wire creates a topological hole in R³\{wire},
and H¹ of that space is non-trivial. The integral form is globally defined even
though no potential exists globally.

**Higher cohomology**:

```
  H²_dR(M) ≠ 0: closed 2-forms (div-free vector fields) that aren't
                  curls of 1-forms → detects enclosed 2D surfaces (voids)

  Example: R³\{0} has H²_dR ≅ R, generated by the solid angle form
           ω = r̂·dA / r². This is ∇·(r̂/r²) = 4πδ³(0) — the Coulomb field
           has non-trivial second cohomology because of the point singularity.
```

**De Rham's theorem** (the payoff): H^k_dR(M) ≅ H^k(M; R) (singular cohomology
with real coefficients). Analysis (differential forms, exterior derivative)
gives the same topological invariants as algebraic topology. The integral
theorems compute the pairing between homology classes (cycles) and cohomology
classes (closed forms) — this is exactly the content of Stokes' theorem at
the highest level.

---

## Connections

**Complex analysis — Cauchy's theorem as 2D Stokes'.**
In the complex plane, a holomorphic function f = u + iv satisfies the
Cauchy-Riemann equations (which are simultaneously curl-free + divergence-free
for the 2D vector field (u,v)). Stokes' theorem in 2D (Green's theorem) applied
to holomorphic f gives:

```
  ∮_C f(z) dz = 0     for any simple closed curve C in a simply-connected
                       domain where f is holomorphic (Cauchy's theorem)
```

If f has a singularity (pole) inside C, the cohomological obstruction is
non-trivial and the integral equals 2πi × (residue at the pole) — the residue
theorem. Every result in complex analysis that involves contour integrals is
Stokes' theorem applied to the complex plane, with the Cauchy-Riemann equations
encoding the holomorphic condition as a 1-form being closed.

**Numerical methods — discrete divergence theorem.**
Finite-volume methods for CFD discretize the divergence theorem directly:
for each mesh cell, ∫∫∫ ∇·F dV = ∮∮ F·dA is enforced exactly by computing
fluxes through cell faces. This conserves the diverged quantity (mass, momentum,
energy) to machine precision regardless of cell size — the discrete analog of
the theorem holds identically. The integral form is the natural home for
conservation laws on irregular grids.

**PDE theory — Green's functions.**
The fundamental solution to ∇²G = δ is derived via the divergence theorem
applied to a ball of radius ε centered at the source point, taking ε→0.
Green's functions for elliptic, parabolic, and hyperbolic PDEs all use these
integral identities as their derivation scaffolding. The heat kernel, wave
kernel, and Coulomb kernel are all in this family.

**Differential geometry — Stokes' theorem on manifolds.**
The generalized Stokes' theorem ∫_M dω = ∫_{∂M} ω holds on any oriented
compact smooth manifold with boundary. This is the foundation for characteristic
classes (Chern-Weil theory), the Atiyah-Singer index theorem (which relates
analytical data — dimension of solution spaces — to topological data — characteristic
classes), and the Gauss-Bonnet theorem (∫_M K dA = 2πχ(M) for a surface).

---

## Decision Cheat Sheet

| You want to convert | Direction | Use | When valid |
|---------------------|-----------|-----|------------|
| Volume integral of ∇·F | → surface integral | Divergence theorem | F smooth on V∪S |
| Surface integral of ∇×F | → line integral | Stokes' theorem | F smooth on S∪C |
| Line integral of ∇f | → endpoint values | Gradient theorem | F = ∇f (conservative) |
| Differential Maxwell → integral | any | Both theorems | — |
| Is ∮F·dl = 0? | check | Is ∇×F = 0? | Only if domain simply connected |
| Is ∮∮F·dA = 0? | check | Is ∇·F = 0? | Only if domain has no voids |
| Solve ∇²u = f | → integral formula | Green's function | Fundamental solution known |
| Is curl-free F a gradient? | check topology | H¹_dR(domain) = 0? | Yes iff no holes |

---

## Common Confusion Points

**dA points outward for closed surfaces, by convention.**
For open surfaces (Stokes' theorem), the orientation of dA is tied to the
direction you traverse the boundary C by the right-hand rule. Get this wrong
and you get a sign error everywhere.

**Stokes' theorem works for any surface bounded by C.**
Given a closed loop C, you can choose any surface S that has C as its
boundary — a flat disk, a curved bowl, a bag shape. The answer is the same.
Maxwell exploits this: in Ampere's law, the surface can be a flat disk through
a wire, or a bulging surface that avoids the wire — they must give the same B
circulation. This is how Maxwell discovered the displacement current term
(without it, the two surfaces give different answers — a contradiction).

**Flux is signed.**
∮∮ E·dA counts outward flux as positive, inward as negative. Net flux = 0
means equal amounts enter and exit, not that E = 0 everywhere.

**The gradient theorem requires F = ∇f (conservative field).**
Not every vector field is a gradient. F must be curl-free (∇×F = 0) in a
simply-connected domain for a potential f to exist. In E&M, the electrostatic
field is conservative (∇×E = 0 when ∂B/∂t = 0); the full dynamic E field
is not.

**These theorems assume smooth fields.**
Singularities (like the E field of a point charge at r = 0) require care.
Gaussian surfaces are often chosen specifically to avoid singularities while
still enclosing the charge that causes them.

**"Closed" means two things — be careful.**
A closed curve (∮) is one that loops back to its start. A closed form is one
with dω = 0. A closed surface (∮∮) is one with no boundary. These are all
distinct uses of "closed."
