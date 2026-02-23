# Vector Calculus — The Language of Maxwell's Equations

## The Big Picture

Vector calculus gives you four operators that act on fields in space. Everything in
Maxwell's equations is built from exactly these four tools.

```
+------------------------------------------------------------------------+
|                     VECTOR CALCULUS LANDSCAPE                          |
|                                                                        |
|   INPUT              OPERATOR          OUTPUT       MEASURES           |
|   -----              --------          ------       --------           |
|                                                                        |
|   f(x,y,z)   ──── ∇  (gradient) ───>  vector field  which way uphill  |
|   scalar field                                                         |
|                                                                        |
|   F(x,y,z)   ──── ∇· (divergence) ─>  scalar field  source or sink    |
|   vector field                                                         |
|                                                                        |
|   F(x,y,z)   ──── ∇× (curl) ───────>  vector field  local rotation    |
|   vector field                                                         |
|                                                                        |
|   f(x,y,z)   ──── ∇² (Laplacian) ──>  scalar field  vs. neighbors     |
|   scalar field                                                         |
+------------------------------------------------------------------------+
```

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
|        │ ∇ (gradient)          ∇· (divergence) │                 |
|        ▼                                        ▼                |
|   VECTOR FIELD ∇f              SCALAR FIELD ∇·F                  |
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

## Decision Cheat Sheet

| You have | You want to know | Operator | Output |
|----------|-----------------|----------|--------|
| Scalar field f | Which direction changes fastest | ∇f | Vector field |
| Scalar field f | Is this point above/below neighbors | ∇²f | Scalar field |
| Vector field F | Is there a source or sink here | ∇·F | Scalar field |
| Vector field F | Is there local rotation here | ∇×F | Vector field |
| Vector field F | Can I write F = ∇f (no rotation) | Check ∇×F = 0 | Yes/No |
| Vector field F | Can I write F = ∇×A (no sources) | Check ∇·F = 0 | Yes/No |

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
look different. The operators are the same conceptually; only the coordinate
expression changes. We will use spherical form when needed in the physics modules.

**∂B/∂t is a partial time derivative.**
Maxwell's equations also involve time. ∂B/∂t means: at a fixed point in space,
how fast is B changing in time? The full machinery of electrodynamics treats
fields as functions of both space and time: E(x,y,z,t), B(x,y,z,t).
