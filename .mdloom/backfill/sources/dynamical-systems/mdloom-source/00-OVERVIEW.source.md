---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "00-OVERVIEW.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:dynamical-systems:overview
kind: guide
module: dynamical-systems
section: dynamical-systems
title: Dynamical Systems - The Landscape
status: source-custody
source_custody: partial
current_path: dynamical-systems/00-OVERVIEW.md
canonical_path: dynamical-systems/00-OVERVIEW.md
backsource_ids: [mdloom-backfill:dynamical-systems:00-overview, git-history:dynamical-systems:00-overview]
concepts: [overview]
root_concepts: [overview]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Dynamical Systems — The Landscape

A dynamical system is a rule for evolving a **state** forward in time. That is all. The state
lives in a space (the **phase space**); the rule is either a vector field (continuous time) or a
map (discrete time). Everything in this directory — fixed points, limit cycles, bifurcations,
chaos, strange attractors — is the study of the *long-term geometry* of trajectories under that
rule, **without** demanding a closed-form solution.

```
                         THE DYNAMICAL SYSTEMS LANDSCAPE
                         ===============================

   CONTINUOUS TIME (FLOWS)                       DISCRETE TIME (MAPS)
   x' = f(x),  x in R^n                          x_{n+1} = F(x_n)
        |                                              |
        |  integrate / iterate                         |
        v                                              v
   +---------------------------------------------------------------------+
   |                          PHASE SPACE  R^n                           |
   |                                                                     |
   |   LINEAR              -->   NONLINEAR          -->   CHAOTIC        |
   |   x' = Ax                   x' = f(x)               sensitive to    |
   |   solvable in closed        no closed form;         initial conds   |
   |   form; eigenvalues         linearize near          (positive       |
   |   of A decide              fixed points             Lyapunov exp.)  |
   |   everything                                                        |
   |     |                          |                        |           |
   |     v                          v                        v           |
   |  fixed points              fixed pts + limit       strange          |
   |  (nodes/spirals/           cycles + bifurca-       attractors,      |
   |  saddles/centers)          tions + manifolds       fractal sets     |
   +---------------------------------------------------------------------+
        |                          |                        |
        v                          v                        v
    EIGENVALUES               JACOBIAN +               LYAPUNOV EXPONENTS
    Re(λ) signs               NORMAL FORMS             + FRACTAL DIM
    (Ch. 02)                  (Ch. 02-03)              (Ch. 05-07)

   DIMENSION GATES WHAT CAN HAPPEN (continuous flows):
     n = 1:  only monotone approach to fixed points (no oscillation)
     n = 2:  fixed points + limit cycles ONLY  (Poincare-Bendixson rules out chaos)
     n >= 3: chaos becomes possible (Lorenz, Rossler)
   Discrete maps escape this: even 1D maps (logistic) are chaotic.
```

Read top-to-bottom: a system is continuous or discrete; its phase space is linear, nonlinear, or
chaotic; the diagnostic tool sharpens as you move right. The **dimension** of phase space is the
master gate — it determines what behaviors are even *possible*.

---

## The Two Kinds of Time

```
   FLOWS (continuous)                     MAPS (discrete)
   ------------------                     ---------------
   x'(t) = f(x(t))                        x_{n+1} = F(x_n)
   t in R (real time)                     n in Z (tick count)

   trajectory = smooth curve              trajectory = sequence of points
   "phase portrait"                       "orbit" / cobweb

   arises from:                           arises from:
     physical laws (F = ma)                 Poincare sections of flows
     reaction kinetics                      every-T sampling
     RC/RL circuits                         iterated numerical schemes
     population ODEs                        population census per season

   a flow induces a map                   a map can be "suspended"
   (time-T map, Poincare map)             into a flow (one dim higher)
```

The two views are not rivals — they convert into each other. The **Poincaré map** turns an
`n`-dimensional flow into an `(n-1)`-dimensional map by recording successive crossings of a
surface. This is why a 3D continuous flow (Lorenz) and a 2D map (Hénon) sit in the same family,
and why a 1D map (logistic) can model a 2D flow's return behavior. Chapter 08 develops maps;
Chapter 06 builds Poincaré sections.

### Old world → new world bridges

| You already know | Dynamical-systems framing |
|---|---|
| Linear ODE `x' = Ax` solved by `e^{At}` | Eigenvalues of `A` *are* the stability classification (Ch. 02) |
| State-space control `x' = Ax + Bu` | Same phase space; feedback `u = -Kx` moves eigenvalues = pole placement (`control-theory/02`) |
| Lyapunov function `V` proving stability | Identical object here; LaSalle extends it (`control-theory/06`, Ch. 02) |
| Gradient descent `θ_{n+1} = θ_n - η∇L` | A discrete map; its continuous limit `θ' = -∇L` is a **gradient flow** (Ch. 09) |
| Eigenvalue stability of a numerical scheme | Same algebra; the integrator *is* a map and inherits its dynamics (`numerical-methods/06`) |
| Phase transitions in stat-mech | Bifurcations of an order-parameter ODE; symmetry breaking = pitchfork (Ch. 03, `statistical-mechanics/`) |

---

## What This Field Actually Asks

The defining move of dynamical systems is **qualitative analysis**: answer the questions below
*without* integrating the equations.

```
   +--------------------------------------------------------------+
   |  THE CENTRAL QUESTIONS                                       |
   |                                                              |
   |  1. WHERE does the system settle?                            |
   |     fixed points, limit cycles, tori, strange attractors     |
   |                                                              |
   |  2. Is that destination STABLE?                              |
   |     linearize -> Jacobian eigenvalues -> Re(lambda) signs    |
   |                                                              |
   |  3. How does the answer CHANGE as a parameter varies?        |
   |    bifurcations: saddle-node, transcritical, pitchfork, Hopf |
   |                                                              |
   |  4. Can the system be CHAOTIC?                               |
   |     positive Lyapunov exponent, SDIC, fractal attractor      |
   |                                                              |
   |  5. What is the GEOMETRY of the attracting set?              |
   |     fractal dimension, stable/unstable manifolds             |
   +--------------------------------------------------------------+
```

Question 1–2 are **local** and largely **linear-algebraic** (Ch. 01–02). Question 3 is the theory
of **bifurcations** (Ch. 03). Questions 4–5 are the **nonlinear/chaotic** regime (Ch. 05–07).
Limit cycles (Ch. 04) are the bridge: genuinely nonlinear yet still well-behaved in 2D.

---

## Existence, Uniqueness, and the Flow

Before any geometry, the foundational guarantee. For `x' = f(x)`, `x(0) = x_0`:

> **Picard–Lindelöf theorem.** If `f` is Lipschitz continuous on a neighborhood of `x_0` (e.g.
> `f ∈ C^1`), then a unique solution exists on some interval `(-τ, τ)` around `t = 0`.

Two consequences shape *all* of the geometry that follows:

```
   CONSEQUENCE 1: trajectories cannot cross.
     Two distinct trajectories never intersect in phase space.
     (If they did, the crossing point would have two futures -> non-unique.)
     => phase portraits are foliations; this is WHY 2D rules out chaos.

   CONSEQUENCE 2: the flow phi_t is a one-parameter group.
     phi_t(x_0) = state at time t starting from x_0
     phi_0 = identity,   phi_{t+s} = phi_t o phi_s,   phi_{-t} = (phi_t)^{-1}
     A smooth, invertible, time-shiftable family of maps.
```

Lipschitz can fail: `x' = x^{2/3}` from `x(0)=0` has infinitely many solutions (not Lipschitz at
0). Finite-time blowup is also allowed: `x' = x^2` reaches `+∞` at finite `t`. Existence is
*local*; global existence needs extra control (boundedness, a Lyapunov function — Ch. 02).

---

## The Dimension Hierarchy (the single most useful fact)

```
   FLOW DIMENSION   WHAT CAN HAPPEN                 WHY
   --------------   ---------------                 ---
   n = 1            monotone -> fixed point         x' = f(x) on a line;
                    NO oscillation, NO overshoot    x can only move one way
                                                    between zeros of f

   n = 2            fixed points + LIMIT CYCLES     trajectories can't cross
                    NO chaos                        (Poincare-Bendixson, Ch. 04)
                                                    -> trapped orbits must be
                                                    periodic

   n >= 3           CHAOS possible                  enough room for trajectories
                    strange attractors             to stretch + fold without
                    (Lorenz needs exactly 3)       self-intersecting

   DISCRETE MAPS    chaos at ANY dimension          F need not be invertible;
                    1D logistic map is chaotic      no "can't cross" constraint
```

This table is the spine of the directory. Continuous 1D and 2D are *tame* for a deep topological
reason (Jordan curve theorem + no-crossing); only 3D+ flows and maps of any dimension can be
chaotic. Memorize it — it tells you instantly whether to even look for chaos.

---

## Conservative vs Dissipative

A second master dichotomy, orthogonal to dimension, governed by **phase-space volume**:

```
   Take a blob of initial conditions. Track its volume V(t) under the flow.
   Divergence theorem:  dV/dt = integral of (div f) over the blob.

   div f = 0   everywhere   ->  CONSERVATIVE (volume-preserving)
                                Hamiltonian systems, frictionless mechanics
                                NO attractors; centers, tori, KAM
                                Liouville's theorem (stat-mech!)

   div f < 0   on average   ->  DISSIPATIVE (volume-contracting)
                                friction, resistance, real engineering
                                attractors EXIST; volume -> 0 onto them
                                strange attractors live here (Lorenz: div f = -(sigma+1+b))
```

This is why the Lorenz attractor has zero volume yet positive dimension — dissipation crushes
volume to nothing while chaos forbids it collapsing to a point. Conservative systems (Hamiltonian)
connect directly to `statistical-mechanics/` (Liouville, ergodicity) and analytical mechanics;
dissipative systems are the home of the strange attractors in Chapter 06.

---

## How the Chapters Fit Together

```
   01 FLOWS & FIXED POINTS  -- the objects: vector fields, fixed pts, 1D lines
        |
        v
   02 STABILITY             -- linearize: Jacobian eigenvalues, 2D zoo, Lyapunov
        |
        +--> 03 BIFURCATIONS -- how stability CHANGES with a parameter (normal forms)
        |
        v
   04 LIMIT CYCLES          -- genuine nonlinear oscillation; Poincare-Bendixson caps 2D
        |
        v   (cross the dimension-3 threshold)
   05 CHAOS                 -- logistic map, Feigenbaum, Lyapunov exponents, SDIC
        |
        +--> 06 STRANGE ATTRACTORS -- Lorenz, Rossler; the geometry of chaos
        |         |
        |         v
        +--> 07 FRACTALS    -- the geometry itself: dimension, Mandelbrot, IFS
        |
        v
   08 DISCRETE MAPS         -- the map theory in full: symbolic dynamics, Henon
        |
        v
   09 APPLICATIONS          -- synchronization, networks, gradient flows (ML), chaos control
```

---

## Decision Cheat Sheet

| I want to... | Tool / chapter |
|---|---|
| Decide if a fixed point is stable | Jacobian eigenvalues, signs of `Re(λ)` — Ch. 02 |
| Classify a 2D fixed point | Trace–determinant plane — Ch. 02 |
| Prove stability when linearization is inconclusive | Lyapunov function — Ch. 02 |
| Understand how behavior flips as a knob turns | Bifurcation normal forms — Ch. 03 |
| Show a system oscillates persistently | Poincaré–Bendixson / van der Pol — Ch. 04 |
| Rule out chaos | Check `n ≤ 2` for flows (Poincaré–Bendixson) — Ch. 04 |
| Detect chaos | Positive largest Lyapunov exponent — Ch. 05 |
| Quantify a chaotic attractor's geometry | Box / correlation dimension — Ch. 06–07 |
| Model seasonal/iterated data | Discrete map, cobweb, symbolic dynamics — Ch. 08 |
| Connect to ML training dynamics | Gradient flow / discretized descent — Ch. 09 |
| Connect to feedback control | Lyapunov, Hopf, pole placement — `control-theory/` |
| Actually integrate the ODE numerically | RK / stiff solvers — `numerical-methods/06` |

---

## Common Confusion Points

### "Dynamical systems vs differential equations — same thing?"

Differential-equations courses teach you to **solve** `x' = f(x)` (separation, integrating
factors, Laplace, series). Dynamical systems asks what trajectories **do** when you *can't* solve —
which is the generic nonlinear case. Closed-form solution is the exception; qualitative geometry
is the rule. The `mathematics/` differential material covers solution techniques; this directory
covers the asymptotic/geometric theory.

### "Is a fixed point the same as an equilibrium / steady state?"

Yes — `f(x*) = 0` (flow) or `F(x*) = x*` (map). "Equilibrium," "steady state," "stationary point,"
"critical point of the flow," and "fixed point" are interchangeable. Do not confuse a fixed point
of the *flow* (where motion stops) with a critical point of a *potential* (`∇V = 0`) — they
coincide only for gradient systems `x' = -∇V` (Ch. 09).

### "Chaos = randomness?"

No. Chaos is **deterministic**. The same initial condition always yields the same trajectory; there
is no noise. Chaos is *sensitive dependence on initial conditions* (SDIC): nearby states diverge
exponentially (positive Lyapunov exponent), so prediction degrades, but the rule is fixed and
exact. Randomness has no rule; chaos has a perfectly definite one (Ch. 05).

### "Can a 2D system be chaotic?"

Not a 2D *continuous flow* — Poincaré–Bendixson forbids it (Ch. 04). A 2D *map* (Hénon) absolutely
can. And a non-autonomous 2D flow `x' = f(x, t)` is secretly 3D (append `t' = 1`), so a periodically
forced pendulum is chaotic. The dimension count is about *autonomous* flows.

### "Stable vs asymptotically stable?"

**Stable (Lyapunov):** stay near `x*` if you start near it. **Asymptotically stable:** stay near
*and* converge to `x*`. A frictionless pendulum's bottom is stable but not asymptotically stable
(it orbits forever — a center). Add friction and it becomes asymptotically stable (a spiral). The
distinction is exactly `Re(λ) < 0` (asymptotic) vs `Re(λ) = 0` (marginal) — Ch. 02.
