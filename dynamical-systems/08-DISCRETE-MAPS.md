---
maxim_schema: maxim.frontmatter.v1
id: maxim:dynamical-systems:discrete-maps
kind: guide
module: dynamical-systems
section: dynamical-systems
title: Discrete Maps
status: source-custody
source_custody: partial
current_path: dynamical-systems/08-DISCRETE-MAPS.md
canonical_path: dynamical-systems/08-DISCRETE-MAPS.md
backsource_ids: [proof-backfill:dynamical-systems:08-discrete-maps, git-history:dynamical-systems:08-discrete-maps]
concepts: [discrete, maps]
root_concepts: [discrete, maps]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Discrete Maps

A discrete map `x_{n+1} = F(x_n)` advances state in integer ticks rather than continuous time. Maps
are not a poor cousin of flows — they are *more powerful*: a 1D map (logistic) is already chaotic,
escaping the dimension hierarchy that tames continuous flows (Ch. 00). They arise as **Poincaré
sections** of flows (Ch. 06), as **numerical integrators** (each step is a map — `numerical-methods/06`),
and natively in seasonal/digital systems. This chapter develops the map toolkit in full: cobweb
analysis, the stability rule `|F'| < 1`, **symbolic dynamics** (the bridge to formal languages), the
**Hénon** attractor, and the **Smale horseshoe** — the geometric heart of chaos.

```
              FLOW vs MAP: STABILITY LIVES ON DIFFERENT CURVES
              ================================================
        FLOWS x' = f(x)              MAPS x_{n+1} = F(x_n)
        eigenvalue lambda            multiplier lambda = F'(x*)

           Im                              Im
            |  UNSTABLE                      | unstable (outside)
            |                          .-----+-----.
   ---------+--------> Re             /  |STABLE|   \
            |  STABLE                |   |  o   |    |  <- unit circle
            | (Re < 0)                \  |unit  |   /   |lambda| < 1 stable
            |                          '--+--disk+--'
   stable <=> LEFT half-plane         stable <=> INSIDE unit circle
   marginal: Re = 0                   marginal: |lambda| = 1
                                      (lambda=+1 fold, lambda=-1 flip/doubling)
```

The change of stability boundary (imaginary axis → unit circle) is the single fact to internalize:
the time-`T` map of a flow sends `λ → e^{λT}`, carrying the left half-plane onto the unit disk.

---

## Fixed Points, Cobwebs, and Stability of Maps

```
   FIXED POINT:  F(x*) = x*  (an intersection of y=F(x) with the diagonal y=x).
   STABILITY (multiplier m = F'(x*)):
        |m| < 1 -> STABLE   (orbits converge)        |m| = 0 superstable
        |m| > 1 -> UNSTABLE (orbits diverge)         |m| = 1 marginal
        m > 0   -> monotone approach                 m < 0 -> ALTERNATING
                                                     (sets up period-doubling)

   COBWEB DIAGRAM (graphical iteration):  bounce between F and the diagonal.

      y |        y=x  /          Read x_{n+1}=F(x_n): go UP to the curve F,
        |          / .--F(x)      then ACROSS to the diagonal y=x to copy
        |        /  /|            x_{n+1} onto the x-axis, repeat.
        |       /  / |            Staircase IN  -> stable fixed point.
        |      /__/  |            Staircase OUT -> unstable.
        |     /| *   |            Square spiral -> oscillatory (m < 0).
        +----/-+-----+----> x
            x0  x*
```

The map rule `|F'(x*)| < 1` is the exact discrete analogue of the flow rule `f'(x*) < 0` (Ch. 01).
The crucial new feature is **`m < 0`**: a negative multiplier makes orbits *alternate* sides of the
fixed point, and when `m` passes through `−1` you get a **period-doubling (flip) bifurcation** — the
engine of the logistic cascade (Ch. 05). Maps have *two* generic codimension-1 local bifurcations:
`m=+1` (fold/tangent, like a saddle-node) and `m=−1` (flip/period-doubling, which has no flow
analogue at a fixed point).

### Old world → new world bridges

| You already know | Map framing |
|---|---|
| Newton's method `x_{n+1} = x_n − f/f'` | A map; its fixed points are roots, superstable (`F'=0`) → quadratic convergence (`numerical-methods/`) |
| Fixed-point iteration `x = g(x)` | Converges iff `|g'(x*)| < 1` — the map stability rule, exactly (`numerical-methods/02`) |
| A digital filter / IIR recurrence | A linear map; stability ⇔ poles inside the unit circle (`signal-processing/`) |
| Power iteration for eigenvalues | A map on projective space converging to the dominant eigenvector |
| Gradient descent `θ_{n+1}=θ_n−η∇L` | A nonlinear map; `|1−ηλ|<1` per Hessian eigenvalue sets the step limit (Ch. 09) |

The fixed-point-iteration bridge is exact and load-bearing: `numerical-methods/`'s convergence
criterion `|g'(x*)| < 1` *is* the discrete-map stability rule. Newton's method is a map engineered to
have `F'(x*) = 0` (superstable) at every root, which is *why* it converges quadratically.

---

## Symbolic Dynamics: Maps as Languages

The most powerful idea in discrete dynamics, and a direct bridge to MIT-TCS formal-language theory:
encode each orbit as an **infinite symbol sequence**, then study the *shift* on those sequences.

```
   PARTITION the state space into labeled regions {A, B, ...}. Record which
   region the orbit visits at each step -> an itinerary, e.g.  A B B A B A ...

   THE SHIFT MAP sigma on sequences:  sigma(s0 s1 s2 ...) = (s1 s2 s3 ...)
   (drop the first symbol). One step of F = one shift of the itinerary.

       F on state space     <--conjugate-->    sigma on {A,B}^N (sequences)
       (geometry, hard)                         (combinatorics, easy)

   FULL SHIFT on 2 symbols = ALL infinite binary strings. Its dynamics:
     - periodic orbits  <-> periodic strings (ABAB..., AABAAB..., ...)
       => COUNTABLY infinitely many, DENSE.
     - a sequence listing every finite block exists -> TRANSITIVITY (mixing).
     - the shift has SDIC: differ in symbol n -> separate after n shifts.
   => the full 2-shift is provably CHAOTIC (Devaney, Ch. 05) -- and it's
      pure combinatorics. This is the cleanest model of chaos that exists.
```

For the MIT-TCS reader this is immediate: the shift on `{A,B}^ℕ` is a full-shift **automaton**;
**subshifts of finite type** (forbidding certain symbol blocks) are exactly the languages accepted by
a finite graph — chaos becomes the theory of a regular language on bi-infinite strings.
**Topological entropy** `h = log(growth rate of admissible n-blocks)` measures the language's
complexity; the metric (Kolmogorov–Sinai) entropy equals the sum of positive Lyapunov exponents
(Pesin's formula), and topological entropy bounds it from above (variational principle). The grammar of the
itineraries *is* the dynamics:

```
   ENTROPY as language growth:
     N(n) = number of admissible length-n symbol blocks.
     h_top = lim (1/n) ln N(n)   = exponential growth rate of distinct orbits.
     Full 2-shift: N(n) = 2^n -> h = ln 2 (= tent/logistic-at-r=4, Ch. 05).
     A forbidden block (subshift of finite type) lowers h via the largest
     eigenvalue of the transition matrix:  h = ln(spectral radius).
```

This is the deepest bridge in the directory: **chaos ↔ formal languages ↔ symbolic computation.**
Smooth dynamics is recoded as combinatorics on strings, where existence of every period, density,
and mixing become elementary statements about sequences.

---

## The Hénon Map: the 2D Strange Attractor

Michel Hénon, 1976, sought the simplest map with a Lorenz-like strange attractor. Two dimensions, a
quadratic stretch plus a linear fold — the minimal *invertible* chaotic map.

```
   x_{n+1} = 1 - a x_n^2 + y_n            a = 1.4, b = 0.3  (standard chaos)
   y_{n+1} = b x_n

   JACOBIAN det = -b (constant) -> uniform area CONTRACTION by |b| = 0.3
   each step (dissipative -> attractor exists). The fold-and-stretch:
        x-update STRETCHES (quadratic) ; y=bx FOLDS the band back.

   THE ATTRACTOR (a boomerang of nested curves):
        y |        ___,,,,---'''       Looks like a few smooth arcs, but
          |    ,-''   ____,,---        ZOOMING IN reveals each "curve" is a
          |  ,'   ,-''                 Cantor set of infinitely many parallel
          | /  ,-'    (self-similar    strands transverse to the fold.
          |/ ,'        Cantor layering) Fractal dimension ~ 1.26.
          +-------------------> x       Locally = (smooth curve) x (Cantor set).
```

Hénon is the 2D map archetype paralleling Rössler's 3D-flow archetype (Ch. 06): minimal, invertible,
explicitly stretch-and-fold, with a self-similar Cantor cross-section (dimension `≈ 1.26`, Ch. 07).
Being invertible (unlike the logistic map), it is the bridge from 1D non-invertible maps to the
genuine **horseshoe** geometry of real chaos.

---

## The Smale Horseshoe: the Geometry of Chaos

Stephen Smale abstracted the *mechanism* common to Lorenz, Hénon, and every homoclinic tangle: take a
square, **stretch** it, **fold** it into a horseshoe, lay it back over itself. Iterating this is
chaos, *provably*, via symbolic dynamics.

```
   ONE STEP OF THE HORSESHOE MAP H:
        [    square    ]   --stretch-->  [=== long thin strip ===]
                                              |  --fold-->
        +-----+   the intersection         +--+ +--+
        | === |   of the square with        |  | |  |   two vertical
        | === |   its image = TWO            |  | |  |   strips survive
        +-----+   horizontal strips          +--+ +--+

   THE INVARIANT SET (points that stay in the square FOREVER, forward AND
   backward) = a CANTOR SET x CANTOR SET.  Label the two strips 0 and 1.
   Each point's full itinerary (...s_{-2} s_{-1} . s_0 s_1 s_2...) is a
   bi-infinite binary string, and H acts as the SHIFT.

   => H restricted to its invariant set is CONJUGATE to the full 2-shift
      => provably chaotic: dense periodic orbits, transitivity, SDIC.
```

> **Smale–Birkhoff homoclinic theorem.** Wherever a stable and unstable manifold of a saddle cross
> *transversally* (a transverse homoclinic point), some iterate of the map contains a horseshoe.
> Hence transverse homoclinic intersections ⇒ chaos.

This is the structural theorem of chaos: it explains *why* chaos appears (the manifolds of Ch. 02
crossing creates a tangle), *makes it rigorous* (conjugacy to the shift, Ch. 05's Devaney criteria),
and *connects geometry to combinatorics* (the invariant set is symbolic). Lorenz, Hénon, the forced
pendulum — all contain horseshoes in their homoclinic tangles.

---

## Sharkovskii and "Period 3 Implies Chaos"

A startling order theorem for *continuous 1D maps* — purely about which periods can coexist.

```
   SHARKOVSKII'S ORDERING of the naturals (for periods of a continuous
   1D map; rightmost forces everything to its right):

     3 > 5 > 7 > ... (odds) > 2.3 > 2.5 > ... > 4.3 > 4.5 > ...
       ... > 2^3 > 2^2 > 2 > 1

   THEOREM: if a continuous map f: R -> R has a periodic point of period p,
   it has periodic points of EVERY period q with p > q in this ordering.

   CONSEQUENCE (Li-Yorke): period 3 is FIRST -> a period-3 orbit forces
   orbits of EVERY period, plus an uncountable "scrambled set".
   "Period three implies chaos."  (The period-3 window of the logistic map,
   Ch. 05, therefore certifies chaos directly.)
```

Sharkovskii reads off an entire periodic skeleton from a single observed period, and the position of
`3` at the top is why the logistic map's period-3 window (Ch. 05) guarantees chaos. The `…> 2³ > 2² >
2 > 1` tail at the right is exactly the period-doubling cascade in reverse order — Sharkovskii and
Feigenbaum describe the same skeleton from order-theoretic and metric viewpoints.

---

## Decision Cheat Sheet

| Goal | Tool |
|---|---|
| Stability of a map fixed point | Multiplier `\|F'(x*)\| < 1` (inside unit circle for matrices: `ρ(J)<1`) |
| Visualize 1D map iteration | Cobweb diagram (bounce between `F` and `y=x`) |
| Predict period-doubling | Multiplier crosses `−1` (flip bifurcation) |
| Predict fold/tangent bifurcation | Multiplier crosses `+1` (two fixed points collide) |
| Prove a map is chaotic | Conjugacy to the shift / find a horseshoe |
| Measure orbit complexity | Topological entropy = `log` growth of admissible blocks |
| Reduce a flow to a map | Poincaré section (Ch. 06) |
| Get a strange attractor from a 2D map | Hénon (dissipative, invertible, stretch-and-fold) |
| Certify chaos from one observed period | Sharkovskii — especially period 3 |
| Connect to numerical iteration | Each integrator step is a map; `\|g'\|<1` ⇔ convergence (`numerical-methods/`) |

---

## Common Confusion Points

### "Maps are just discretized flows — less powerful"

Backwards. Maps are *more* permissive: a 1D map is chaotic (logistic), while a 1D *flow* can only
crawl to a fixed point (Ch. 00). Maps escape the no-crossing constraint of flows because `F` need not
be invertible — a non-invertible map *folds* the line onto itself, which a flow can never do. Every
flow induces a map (Poincaré), but maps are a strictly richer class.

### "`F'(x*) < 1` for stability — same as flows?"

No — it is the **absolute value**: `|F'(x*)| < 1`. The flow rule is `f'(x*) < 0` (sign of the real
part). A map fixed point with `F'(x*) = −0.5` is **stable** (orbits alternate but shrink), whereas a
flow with `f'(x*) = −0.5` is also stable but *monotone*. And `F'(x*) = 2` is unstable just as
`F'(x*) = −2` is. The unit *circle*, not the left half-plane, is the boundary.

### "Symbolic dynamics is just notation"

It is a *conjugacy* — a genuine change of coordinates that makes hard smooth dynamics into elementary
combinatorics. Once you show `F` on its invariant set is conjugate to the shift, *every* dynamical
property (chaos, entropy, period structure, mixing) transfers from trivial statements about strings.
For the TCS reader: it recasts a differential-geometry problem as a regular-language problem on
bi-infinite words — and topological entropy is the language's growth rate.

### "Period 3 implies chaos — for any system?"

Only for **continuous maps of an interval (1D)**, via Sharkovskii. It does **not** apply to
higher-dimensional maps (Hénon can have a 3-cycle without the full Sharkovskii cascade) nor to flows
(a flow's period-3 *orbit* is just one limit cycle). The theorem is specific to 1D continuous maps —
a beautiful but narrow result. Don't over-extend it.

### "The Hénon attractor is a smooth curve"

It looks like a few arcs, but each apparent curve is a **Cantor set of infinitely many strands**
(dimension `≈ 1.26`, Ch. 07) — locally a smooth curve times a Cantor dust, the universal transverse
structure of a stretch-and-fold attractor. The smooth appearance is a resolution artifact, exactly as
with the Lorenz "surface" (Ch. 06). Zoom in to see the layering.
