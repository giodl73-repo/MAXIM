# Stability and Linearization

The central engine of the whole subject: to decide whether a fixed point is stable, **linearize**
the flow around it and read the **eigenvalues of the Jacobian**. The signs of their real parts
settle the question for hyperbolic fixed points (Hartman–Grobman). When eigenvalues sit on the
imaginary axis, linearization fails and you reach for a **Lyapunov function**. This chapter is the
linear-algebra core; Chapter 03 studies what happens *at* the failure boundary.

```
                LINEARIZE -> EIGENVALUES -> STABILITY
                =====================================

   Nonlinear flow            Linearize at x*           Eigenvalues of J
   x' = f(x)        ----->    let u = x - x*    ----->  decide stability
                              u' ≈ J u                  via signs of Re(lambda)
                              J = Df(x*) (Jacobian)

        Im(lambda)
            ^
            |     UNSTABLE half-plane
            |   (any Re(lambda) > 0  =>  unstable)
            |
   ---------+---------> Re(lambda)
            |
            |     STABLE half-plane
            |  (ALL Re(lambda) < 0  =>  asymptotically stable)
            |
   The imaginary axis Re(lambda)=0 is the MARGINAL boundary:
   linearization is INCONCLUSIVE there (centers, bifurcations -> Ch. 03).
```

The rule in one line:

> **Asymptotic stability ⇔ every eigenvalue of the Jacobian has strictly negative real part.**

---

## The Jacobian and the Linearization Theorem

Near a fixed point `x*`, write `u = x − x*`. Taylor-expanding `f`:

```
   u' = f(x* + u) = f(x*) + Df(x*) u + O(|u|^2)
                  =   0    +   J u    + (higher order)

   J = Df(x*) = [ df_i / dx_j ]   evaluated at x*   (the JACOBIAN matrix)

   Linearized system:   u' = J u      Solution:  u(t) = e^{Jt} u(0)
```

The matrix exponential `e^{Jt}` decomposes along eigenvectors: a mode with eigenvalue
`λ = a + ib` evolves as `e^{at}(cos bt + i sin bt)` — `a` sets growth/decay, `b` sets rotation.
Hence:

```
   Re(lambda) < 0  ->  that mode DECAYS    (contributes to stability)
   Re(lambda) > 0  ->  that mode GROWS      (one is enough for instability)
   Re(lambda) = 0  ->  that mode is MARGINAL (neither; nonlinear terms decide)
   Im(lambda) != 0 ->  that mode ROTATES   (oscillatory approach/departure)
```

> **Hartman–Grobman theorem.** If `x*` is **hyperbolic** (no eigenvalue has `Re(λ) = 0`), then the
> nonlinear flow near `x*` is topologically conjugate to its linearization `u' = J u`. The phase
> portraits are deformable into each other — linearization tells the *complete* local story.

The hypothesis is sharp. At `Re(λ) = 0` the nonlinear terms you discarded become decisive: that is
exactly a **bifurcation point** (Ch. 03) or a **center** (which can be a true center or a slow
spiral). Linearization is necessary but, on the imaginary axis, not sufficient.

### Old world → new world bridges

| You already know | Stability framing |
|---|---|
| Char. polynomial roots of `x'' + cx' + kx = 0` | Eigenvalues of the companion Jacobian; `Re < 0` ⇔ damping `c > 0` |
| Routh–Hurwitz / pole locations (`control-theory/01`) | Identical criterion: closed-loop poles = eigenvalues; LHP ⇔ stable |
| `e^{At}` matrix exponential | The linearized flow *is* `e^{Jt}`; eigenvalues are its decay rates |
| Spectral radius `ρ(A) < 1` for a stable map | The **discrete** analogue: `|λ| < 1` (inside unit circle) — Ch. 08 |
| Gershgorin disks bounding eigenvalues | A quick stability screen without solving the characteristic polynomial |

Note the flow-vs-map difference, which trips everyone up:

```
   FLOWS (continuous):   stable  <=>  Re(lambda) < 0      (LEFT half-plane)
   MAPS  (discrete):     stable  <=>  |lambda|   < 1      (INSIDE unit circle)

   The map of a flow's time-T sampling sends lambda -> e^{lambda T},
   which maps the left half-plane exactly onto the unit disk. Consistent.
```

---

## The 2D Classification: Trace–Determinant Plane

For a 2×2 Jacobian `J`, the two eigenvalues are determined entirely by `τ = tr J` and `Δ = det J`:

```
   lambda^2 - tau*lambda + Delta = 0     =>   lambda = (tau +- sqrt(tau^2 - 4*Delta)) / 2

   Discriminant  D = tau^2 - 4*Delta  decides real vs complex.
```

This compresses every 2D fixed point into a single picture — the most useful diagram in the field:

```
                    THE TRACE-DETERMINANT PLANE
                    ===========================

      Delta = det J
         ^
         |        \  STABLE      |  UNSTABLE  /
         |  STABLE \  SPIRALS    |  SPIRALS  / UNSTABLE
         |  NODES   \  (Re<0,    | (Re>0,   /  NODES
         |  (lam<0   \ Im!=0)    | Im!=0)  /  (lam>0
         |  both)     \          |        /   both)
         |             \  parabola D=0:   /        parabola
         |              \  tau^2=4*Delta /         tau^2 = 4*Delta
         |   - - - - - - +CENTERS+ - - - +        (real, repeated)
         |              /  (tau=0,        \
         |             /    Delta>0)       \
         |            /                     \
   ------+-----------+----------------------+--------> tau = tr J
         |          /      SADDLE POINTS     \
         |         /     (Delta < 0 always)   \
         |        /   one lam>0, one lam<0     \
         |       /     -> ALWAYS UNSTABLE       \

   READING IT:
     Delta < 0           -> SADDLE        (unstable; has stable + unstable dirs)
     Delta > 0, tau < 0  -> STABLE   node (D>0) or spiral (D<0)
     Delta > 0, tau > 0  -> UNSTABLE node (D>0) or spiral (D<0)
     Delta > 0, tau = 0  -> CENTER        (marginal; Re=0; pure imaginary lambda)
     parabola tau^2=4Delta -> degenerate / star nodes (repeated eigenvalue)
```

The full zoo, with portraits:

```
   STABLE NODE (lam2 < lam1 < 0)        SADDLE (lam1 < 0 < lam2)
      \  |  /                              \         /
       \ | /                                \   ^   /   unstable
   ------*------  all in                  ---*-->---  manifold W^u
       / | \      arrows IN                /   v   \   stable
      /  |  \                             /         \  manifold W^s

   STABLE SPIRAL (Re<0, Im!=0)          CENTER (Re=0, Im!=0)
       ___                                  ___
      /   \  spiraling                     /   \   closed
     | -> -*  inward                      |     *  orbits,
      \___/  (decaying                     \___/   no decay
             oscillation)                          (marginal)
```

### Worked classification

```
   x' = -x + y
   y' = -y - x^3          (note: nonlinear)

   Fixed point at origin (0,0). Jacobian:
        J = [ df1/dx  df1/dy ]   [ -1    1 ]
            [ df2/dx  df2/dy ] = [ -3x^2 -1 ]   at (0,0) -> [ -1  1; 0 -1 ]

   tau = tr J = -2,   Delta = det J = (-1)(-1) - (1)(0) = 1.
   D = tau^2 - 4*Delta = 4 - 4 = 0  -> repeated eigenvalue lambda = -1 (twice).
   tau < 0, Delta > 0  ->  STABLE (degenerate stable node).

   Hyperbolic (Re = -1 != 0) -> Hartman-Grobman applies: the nonlinear -x^3
   term does not change the local picture. Origin is asymptotically stable.
```

---

## Stable and Unstable Manifolds

A saddle is not "just unstable" — it has *structure*. Its eigenvectors seed two invariant curves:

```
   +-------------------------------------------------------------------+
   |  STABLE MANIFOLD   W^s(x*): trajectories -> x* as t -> +infinity  |
   |                    tangent to eigenvectors with Re(lambda) < 0    |
   |                                                                   |
   |  UNSTABLE MANIFOLD W^u(x*): trajectories -> x* as t -> -infinity  |
   |                    tangent to eigenvectors with Re(lambda) > 0    |
   +-------------------------------------------------------------------+

         W^s (incoming)
              \         /  W^u (outgoing)
               \       /
                \     /
        ---------*---------     The stable manifold is the separatrix:
                /     \         it divides basins of attraction. A
               /       \        trajectory landing exactly on W^s reaches
              /         \       the saddle; one epsilon off shoots away
            W^u         W^s     along W^u.
```

> **Stable Manifold Theorem.** Near a hyperbolic fixed point, `W^s` and `W^u` exist, are as smooth
> as `f`, and are tangent at `x*` to the stable/unstable eigenspaces of `J`. Their dimensions equal
> the number of eigenvalues with `Re(λ) < 0` and `Re(λ) > 0`.

Manifolds are the global skeleton: they form **basin boundaries**, and when a stable and unstable
manifold cross transversally (a **homoclinic tangle**) you get the geometry behind chaos — the
Smale horseshoe (Ch. 08) lives in such tangles. In `control-theory/`, `W^s` of a saddle is the
manifold a controller must steer the state onto.

---

## Lyapunov Functions: Stability Without Eigenvalues

When `x*` is non-hyperbolic (`Re(λ) = 0`), or when you want a **global** or **nonlinear** guarantee
that linearization cannot give, use an energy-like function.

> **Lyapunov's direct method.** Let `V(x)` be continuously differentiable on a neighborhood of `x*`
> with `V(x*) = 0` and `V(x) > 0` for `x ≠ x*` (positive definite). Compute the rate of change along
> trajectories, `V̇ = ∇V · f`. Then:
>
> - `V̇ ≤ 0` ⇒ `x*` is **stable** (Lyapunov).
> - `V̇ < 0` for `x ≠ x*` ⇒ `x*` is **asymptotically stable**.
> - If additionally `V → ∞` as `|x| → ∞` (radially unbounded) ⇒ stability is **global**.

```
   THE PICTURE: V's level sets are nested "bowls" around x*.
   V-dot <= 0 means trajectories cross INWARD (or stay) -> trapped, can't escape.

        V level sets (contours of constant energy):
            ____________
           /  _______    \        trajectory --.
          /  /  ___   \    \                     \  always moving
         |  |  / * \   |    |  <-- x* at bottom    v  to lower V
         |  |  \___/   |    |       of the bowl    (V-dot < 0)
          \  \_______ /    /
           \____________ /
         The energy can only decrease => state slides to the bottom x*.
```

The genius and the pain: **no algorithm produces `V`**. You guess it (often physical energy, or a
quadratic `V = xᵀP x` with `P > 0`), then verify `V̇ ≤ 0`. For linear systems `x' = Ax`, solving the
**Lyapunov equation** `AᵀP + PA = −Q` (with `Q > 0`) yields a valid `V = xᵀP x` whenever `A` is
stable — this is the rigorous bridge to `control-theory/`'s LQR and to the discrete Lyapunov
equation used in Kalman filtering.

### LaSalle's invariance principle (when `V̇ = 0` on a whole set)

A frequent snag: `V̇ ≤ 0` but `V̇ = 0` on more than just `x*` (e.g. a damped pendulum where
`V̇ = −c v²` vanishes whenever `v = 0`, not only at the bottom). Plain Lyapunov gives only stability,
not convergence.

> **LaSalle.** Trajectories converge to the largest **invariant set** contained in `{V̇ = 0}`. If
> that set is just `{x*}`, you recover asymptotic stability.

For the damped pendulum: on `{v = 0}` the only way to *stay* (`v` remains `0`) is to sit at a fixed
point, so the largest invariant set in `{v=0}` is the equilibria — and the bottom attracts. LaSalle
is the standard closer for mechanical and control systems where damping acts on velocities only.

### Worked Lyapunov example

```
   x' = -x + 2 y^2
   y' = -y - x y           Fixed point: origin. Try V = x^2 + 2 y^2 (pos. def.)

   V-dot = 2x x' + 4y y'
         = 2x(-x + 2y^2) + 4y(-y - xy)
         = -2x^2 + 4x y^2 - 4y^2 - 4x y^2
         = -2x^2 - 4y^2  <  0   for all (x,y) != (0,0).

   => origin is asymptotically stable, and since V is radially unbounded,
      GLOBALLY asymptotically stable. (The cross terms 4x y^2 canceled exactly
      -- that cancellation is the art of choosing V.)
```

---

## Decision Cheat Sheet

| Situation | Tool / verdict |
|---|---|
| `n`-D fixed point, want local stability | Eigenvalues of Jacobian `J`; stable ⇔ all `Re(λ) < 0` |
| Any single `Re(λ) > 0` | Unstable — stop, no need to check the rest |
| 2D fixed point, classify type | Trace–determinant plane (`τ = tr J`, `Δ = det J`) |
| `Δ < 0` (2D) | Saddle — always unstable |
| `Re(λ) = 0` for some eigenvalue | Linearization fails — use Lyapunov or go to Ch. 03 (bifurcation) |
| Want global / nonlinear guarantee | Lyapunov function `V`, check `V̇ ≤ 0` |
| `V̇ = 0` on a set, not just `x*` | LaSalle invariance principle |
| Linear `x' = Ax`, need `V` | Solve Lyapunov equation `AᵀP + PA = −Q`, `Q > 0` |
| Discrete map fixed point | `|λ| < 1` (inside unit circle), not `Re(λ) < 0` |
| Find basin boundaries | Stable manifolds `W^s` of saddles |

---

## Common Confusion Points

### "All eigenvalues negative" vs "all `Re(λ)` negative"

For complex eigenvalues you care about the **real part**, not the eigenvalue itself. `λ = −1 ± 3i`
is stable (`Re = −1 < 0`): a *decaying oscillation*, a stable spiral. Only the real part governs
growth; the imaginary part only sets the rotation frequency.

### "Linearization said marginal — so the fixed point is marginal?"

No. At `Re(λ) = 0` linearization is **silent**, not affirmative. A center in the linearization can
be a true center, a slow stable spiral, or a slow unstable spiral once nonlinear terms are
included. You must use Lyapunov, a conserved quantity, or normal-form analysis (Ch. 03). This is the
single most common error — treating "marginal" as a verdict rather than as "go look harder."

### "Lyapunov failed, so the system is unstable"

Failure to *find* a Lyapunov function proves nothing — `V` might exist and you just didn't guess it.
Lyapunov's method gives **sufficient** conditions only. To prove *instability*, use Chetaev's
theorem (a Lyapunov-like function that increases) or simply exhibit one eigenvalue with `Re(λ) > 0`.

### "Stable vs asymptotically stable vs exponentially stable"

```
   Stable (Lyapunov)        stay near if you start near. (Re(lambda) <= 0; center qualifies)
   Asymptotically stable    stay near AND converge. (Re(lambda) < 0)
   Exponentially stable     converge at rate >= c e^{-at}. (Re(lambda) <= -a < 0)
```

Linear asymptotic stability is automatically exponential; for nonlinear systems it need not be
(convergence can be algebraically slow near a non-hyperbolic point). Engineering specs usually want
*exponential* — a guaranteed decay rate — which the most-negative `Re(λ)` provides.

### "Hartman–Grobman lets me ignore the nonlinear terms"

Only at **hyperbolic** points and only **locally** (a small neighborhood). It says nothing about
global behavior, basins, limit cycles, or what happens at `Re(λ) = 0`. The nonlinear terms govern
the large-scale phase portrait and every bifurcation — Hartman–Grobman just licenses the *local
linear sketch* away from the imaginary axis.
