---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "01-FLOWS-AND-FIXED-POINTS.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:dynamical-systems:flows-and-fixed-points
kind: guide
module: dynamical-systems
section: dynamical-systems
title: Flows and Fixed Points
status: source-custody
source_custody: partial
current_path: dynamical-systems/01-FLOWS-AND-FIXED-POINTS.md
canonical_path: dynamical-systems/01-FLOWS-AND-FIXED-POINTS.md
backsource_ids: [mdloom-backfill:dynamical-systems:01-flows-and-fixed-points, git-history:dynamical-systems:01-flows-and-fixed-points]
concepts: [flows, and, fixed, points]
root_concepts: [flows, and]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Flows and Fixed Points

Everything starts with a **vector field**: at each point of phase space, an arrow telling the
state where to go next. A flow is what you get by following those arrows. Fixed points are where
the arrows vanish — the skeleton around which all trajectories organize. This chapter builds the
objects; Chapter 02 makes the stability rigorous.

```
            A VECTOR FIELD AND ITS FLOW  (the system x' = f(x))
            ===================================================

   phase space R^n, with an arrow f(x) attached at every point x:

        ^   \   \   |   /   /   ^            Trajectories are curves
        |    \   \  |  /   /    |            tangent to the arrows
     x2 |     \   \ | /   /     |            everywhere.  They thread
        | <----  o  *  o  ---->              between the arrows and
        |     /   / | \   \     |            CANNOT cross each other
        |    /   /  |  \   \    |            (uniqueness, Ch. 00).
        v   /   /   |   \   \   v
        +----------------------------->
                     x1                       * = fixed point  (f = 0)
                                              o = ordinary point (f != 0)

   A FIXED POINT x* satisfies   f(x*) = 0   -- the arrow is zero, motion stops.
   The flow phi_t(x0) slides x0 along the curve through it as t increases.
```

A fixed point is a *constant solution*: if you start exactly on it, you stay forever. The entire
qualitative theory is: locate the fixed points, decide their stability, and connect them with the
trajectories the arrows demand.

---

## The 1D Case: Phase Lines

In one dimension `x' = f(x)`, the phase space is a line and the analysis is complete and exact —
no eigenvalues needed yet. You read everything off the sign of `f`.

```
   x' = f(x)        Draw f(x).  Fixed points = zeros of f.
                    Where f > 0, x increases (arrow right ->).
                    Where f < 0, x decreases (arrow left  <-).

   Example:  x' = x - x^3 = x(1 - x^2)     zeros at x = -1, 0, +1

   f(x)
    |        ___
    |      /     \                         PHASE LINE:
    |     /       \
  --+----*----*----*----------- x        --->  *  <---  *  --->  *  <---
    |  -1 \   0   /+1                          -1       0        1
    |      \___ /                          stable  unstable  stable
    |                                       (sink)   (source)  (sink)

   Read the arrows: just LEFT of x=0, f>0 so arrow ->; just RIGHT, f<0 so arrow <-.
   Arrows point AWAY from 0  => x=0 is UNSTABLE (source/repeller).
   Arrows point TOWARD +-1   => x=+-1 are STABLE (sinks/attractors).
```

**Stability rule in 1D (the seed of everything):**

```
   f'(x*) < 0   ->  STABLE   (graph of f crosses zero going DOWN; arrows converge)
   f'(x*) > 0   ->  UNSTABLE (graph crosses zero going UP;   arrows diverge)
   f'(x*) = 0   ->  marginal; higher-order terms decide (a bifurcation, Ch. 03)
```

`f'(x*)` is the 1×1 Jacobian. In `n` dimensions this becomes "eigenvalues of the Jacobian have
negative real part" (Ch. 02) — same idea, more bookkeeping.

### The crucial 1D theorem (why 1D flows are boring)

> **No oscillation in 1D autonomous flows.** Since `x(t)` is monotone between consecutive fixed
> points (`f` has constant sign there), `x(t)` either approaches a fixed point or diverges to
> `±∞`. It can never overshoot, never turn around, never oscillate.

To oscillate you need at least 2D (room to circle). To be chaotic you need 3D (Ch. 00 dimension
table). This single fact is why the whole subject is *graded by dimension*.

---

## Old World → New World Bridges

| You already know | Flow framing |
|---|---|
| RC circuit `V' = (V_in − V)/RC` | 1D linear flow; single stable fixed point `V = V_in`, rate `1/RC` |
| Newton's law `m x'' = F(x)` | 2nd-order ODE → 2D **first-order system** `(x, v)`, `v = x'` |
| Logistic growth `N' = rN(1 − N/K)` | 1D flow; fixed points `0` (unstable) and `K` (stable carrying capacity) |
| Markov chain `p_{n+1} = P p_n` | Discrete linear *map*; the flow analogue is the master equation `p' = Q p` |
| State-space plant `x' = Ax + Bu` | Vector field with an input; setting `u=0` gives the open-loop flow (`control-theory/02`) |

### Reducing high-order ODEs to first-order systems

This is the universal trick — every `n`-th order scalar ODE becomes a first-order system in `R^n`,
which is the *only* form dynamical systems theory uses.

```
   x'' + c x' + k x = 0          (damped oscillator, 2nd order)

   Let  x1 = x,  x2 = x'.  Then:

        x1' = x2
        x2' = -k x1 - c x2

   In matrix form:   [x1]'   [ 0    1 ] [x1]
                     [x2]  = [-k   -c ] [x2]      <- a 2D LINEAR flow x' = Ax

   The eigenvalues of A are exactly the roots of the characteristic
   polynomial  lambda^2 + c lambda + k = 0  you already know. Same math,
   geometric repackaging.  (Stability + classification: Ch. 02.)
```

---

## 2D Phase Portraits: the Real Geometry

In 2D the phase portrait is a *picture* of all trajectories. The organizing tool is the
**nullcline** — the curve where one component of velocity vanishes.

```
   System:  x' = f(x, y)        x-nullcline:  f(x,y) = 0  (vertical motion only)
            y' = g(x, y)        y-nullcline:  g(x,y) = 0  (horizontal motion only)

   FIXED POINTS = intersections of x-nullcline and y-nullcline (both zero).

        y |        x-nullcline (x'=0): arrows cross it VERTICALLY  ||
          |      .  .  .  .
          |    .              .                  Intersections of the
          |  .     * <- fixed   .                two nullclines are the
          | .       point         .  y-nullcline fixed points. Nullclines
          |.         =====================  (y'=0) carve the plane into
          +-------------------------------> x  regions of fixed flow
                                               direction (sign of x', y').
```

Nullclines are the 2D analogue of "find the zeros of `f`" from the 1D phase line. They partition
the plane into regions where the signs of `x'` and `y'` are constant, letting you sketch the global
flow before computing a single eigenvalue. The predator–prey and van der Pol portraits in
Chapter 04 are built this way.

---

## Invariant Sets: the Vocabulary of "Where Trajectories Live"

```
   +------------------------------------------------------------------+
   |  INVARIANT SET S: if x in S then phi_t(x) in S for all t.        |
   |  (Once you're in it, you never leave. The flow "respects" it.)   |
   +------------------------------------------------------------------+
        |
        +-- FIXED POINT      a single invariant point, f(x*)=0
        |
        +-- PERIODIC ORBIT   a closed loop, phi_T(x)=x  (limit cycle, Ch. 04)
        |
        +-- INVARIANT MANIFOLD  stable W^s / unstable W^u of a saddle (Ch. 02)
        |
        +-- ATTRACTOR        invariant + attracts a neighborhood + minimal
        |                    (point, cycle, torus, or STRANGE — Ch. 06)
        |
        +-- BASIN OF ATTRACTION  the set of initial conditions whose
                                 trajectories end up on a given attractor
```

Two limit-set definitions you will see constantly:

```
   omega-limit set  w(x):  where the trajectory from x goes as t -> +infinity
   alpha-limit set  a(x):  where it came from as t -> -infinity

   For a stable fixed point x*, w(x) = {x*} for every x in its basin.
   For a stable limit cycle Gamma,   w(x) = Gamma for every x in its basin.
```

The grand goal of the subject restated in this vocabulary: **classify the ω-limit sets and their
basins.** In 1D they are fixed points. In 2D, fixed points or cycles (Poincaré–Bendixson). In 3D+,
also tori and strange attractors.

---

## Conservative Flows and First Integrals

A **first integral** (conserved quantity) `H(x)` satisfies `dH/dt = ∇H · f = 0` along
trajectories — so trajectories are confined to **level sets** `H = const`. This is the structure
behind every Hamiltonian system and the bridge to analytical mechanics and `statistical-mechanics/`.

```
   Undamped pendulum:  theta'' + sin(theta) = 0
   As a system:        theta' = v,   v' = -sin(theta)
   Conserved energy:   H(theta,v) = (1/2) v^2 - cos(theta)

   Phase portrait = level curves of H:

        v |     ____           ____
          |   /      \   ___  /      \         CLOSED loops near (0,0):
          |  |  CENTER |/SEP \| CENTER |       oscillation (libration).
        --+--*--------X-------*-------->  theta SEPARATRIX (X): the orbit
          |  |        |\     /|        |       through the SADDLE points
          |   \______/   ---  \______/        (+-pi, 0) -- threshold between
          |                                    swinging and going over the top.
        centers at theta=0,+-2pi (stable, but NOT asymptotically -- no friction)
        saddles at theta=+-pi   (unstable)
```

The closed orbits are **centers** — stable but not asymptotically stable (energy is conserved, so
trajectories circle forever and never settle). Add damping `-c v` and `H` decreases monotonically:
`H` becomes a **Lyapunov function** (Ch. 02), centers turn into spirals, and the system becomes
dissipative. Conservation ↔ marginal stability; dissipation ↔ asymptotic stability. This is the
deepest recurring theme of the directory.

---

## Worked Example: The Two Fixed Points of a Bead on a Rotating Hoop

A bead on a vertical hoop spinning at rate `ω` obeys (over-damped limit, after non-dimensionalizing
with parameter `γ = ω² R / g`):

```
   phi' = sin(phi) (gamma cos(phi) - 1)        phi = angle from bottom

   Fixed points (phi'=0):
     phi = 0       (bottom)  -- always a fixed point
     phi = pi      (top)     -- always a fixed point
     cos(phi) = 1/gamma      -- EXISTS only when gamma > 1  (two symmetric points)

   Stability (1D rule, sign of f'):
     gamma < 1:  bottom phi=0 STABLE, top phi=pi unstable.
     gamma > 1:  bottom phi=0 becomes UNSTABLE; the two side branches
                 cos(phi)=1/gamma are stable. The bead rides UP the hoop.
```

At `γ = 1` the bottom fixed point loses stability and two new stable ones are born — a
**supercritical pitchfork bifurcation** (Ch. 03). This is exactly how spontaneous symmetry breaking
appears in a mechanical toy: below threshold the bead sits at the bottom; above threshold it
*chooses* a side. The same normal form governs phase transitions in `statistical-mechanics/`.

---

## Decision Cheat Sheet

| I want to... | Do this |
|---|---|
| Find fixed points | Solve `f(x) = 0` (intersect nullclines in 2D) |
| Classify 1D fixed point | Sign of `f'(x*)`: `< 0` stable, `> 0` unstable |
| Sketch a 1D system | Plot `f(x)`; arrows right where `f>0`, left where `f<0` |
| Sketch a 2D portrait | Draw both nullclines; mark flow direction in each region |
| Handle a 2nd-order ODE | Introduce `v = x'` → first-order system in `R²` |
| Know where trajectories live long-term | Find ω-limit sets (fixed points / cycles / attractors) |
| Check if a quantity is conserved | Compute `dH/dt = ∇H · f`; if `0`, trajectories lie on `H = const` |
| Tell conservative from dissipative | `div f = 0` → conservative; `div f < 0` → dissipative |
| Prove stability rigorously | Move to Ch. 02 (Jacobian eigenvalues / Lyapunov) |

---

## Common Confusion Points

### "Fixed point vs equilibrium vs critical point"

For a flow they are synonyms: `f(x*) = 0`. Beware: in optimization a "critical point" means
`∇f = 0` of a *scalar*; a flow's fixed point is a zero of a *vector field*. They coincide only for
gradient flows `x' = -∇V`, where fixed points are critical points of `V` (Ch. 09). Keep the two
senses separate.

### "Why can't I just solve the ODE?"

For linear systems you can (Ch. 02 — matrix exponential). For generic nonlinear `f`, no closed form
exists — that's the normal case, not a failure. The whole point of phase-plane analysis is to
extract behavior (stability, oscillation, basins) *without* a formula.

### "Trajectories crossing in my phase portrait"

They never cross for an autonomous `x' = f(x)` with Lipschitz `f` (uniqueness). If your sketch shows
a crossing, either you drew the nullclines wrong, or your system is **non-autonomous**
(`f` depends on `t`) — in which case lift it to `R^{n+1}` with `t' = 1`, and the crossings vanish in
the higher-dimensional space.

### "A center looks stable — isn't that good enough?"

A center (closed orbits, `Re(λ) = 0`) is **Lyapunov stable but not asymptotically stable**, and it
is *structurally fragile*: an arbitrarily small perturbation (a touch of damping) turns it into a
spiral — stable or unstable. Centers only survive in conservative systems with special structure.
Never rely on a center for engineered stability; you want `Re(λ) < 0`. This fragility is precisely
why linearization can *fail* at centers (Hartman–Grobman needs `Re(λ) ≠ 0` — Ch. 02).
