---
maxim_schema: maxim.frontmatter.v1
id: maxim:dynamical-systems:bifurcations
kind: guide
module: dynamical-systems
section: dynamical-systems
title: Bifurcations
status: source-custody
source_custody: partial
current_path: dynamical-systems/03-BIFURCATIONS.md
canonical_path: dynamical-systems/03-BIFURCATIONS.md
backsource_ids: [proof-backfill:dynamical-systems:03-bifurcations, git-history:dynamical-systems:03-bifurcations]
concepts: [bifurcations]
root_concepts: [bifurcations]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Bifurcations

A bifurcation is a **qualitative change in the phase portrait** as a parameter crosses a critical
value: fixed points appear or annihilate, swap stability, or spawn limit cycles. These are exactly
the events linearization cannot resolve — they happen precisely where an eigenvalue's real part hits
zero (Ch. 02). The astonishing fact, the reason the subject is teachable, is that near such an event
the dynamics collapse onto a **normal form**: one of a handful of universal low-order equations.

```
                THE FOUR LOCAL BIFURCATIONS (1-PARAMETER)
                =========================================

   parameter mu sweeps left -> right; x* = fixed-point location (vertical)

   SADDLE-NODE             TRANSCRITICAL          PITCHFORK (super)
   x* ^   stable           x* ^  \   /            x* ^      stable
      |  ___                  |   \ /                 |  ___/  branches
      | /                     |    X  exchange        | /
   ---+------> mu          ---+---/-\----> mu      ---+----*----> mu
      | \___ unstable         |   /   \                | \___
      |     (two collide      |  /     \               |     \  (symmetric;
      |      & vanish)        stable unstable          unstable middle)

   HOPF (super): a fixed point spits out a LIMIT CYCLE
        amplitude ^        _____ stable cycle (radius ~ sqrt(mu))
                  |     ___/
                  |  __/        fixed point: stable for mu<0,
               ---+--*--------> mu   unstable for mu>0, ringed by
                  |               a growing periodic orbit
```

The first three are **bifurcations of fixed points** on a line (`Re(λ)` of a *real* eigenvalue
crosses 0). Hopf is the **2D-essential** one: a *complex* pair crosses the imaginary axis and a
limit cycle is born (the bridge to Ch. 04).

---

## Why Normal Forms Exist (the deep license)

> **Center Manifold Theorem.** At a bifurcation, split the eigenvalues into those with `Re(λ) = 0`
> (the *center* directions, where the action is) and those with `Re(λ) ≠ 0` (stable/unstable, which
> just decay/grow trivially). The essential dynamics live on a low-dimensional invariant **center
> manifold** tangent to the center eigenspace.

So an `n`-dimensional system at a saddle-node reduces to a *1D* equation on its center manifold.
Then **normal form theory** uses near-identity coordinate changes to kill every nonlinear term that
can be killed, leaving the irreducible skeleton. The result: every saddle-node, anywhere, in any
dimension, looks locally like `ẋ = μ − x²`. This is the dynamical-systems analogue of classifying
quadratic forms — a universality theorem.

### Old world → new world bridges

| You already know | Bifurcation framing |
|---|---|
| A control gain that destabilizes a closed loop | A pole crosses into the RHP → bifurcation; if complex, a **Hopf** (limit-cycle oscillation) — `control-theory/01` |
| Buckling of a loaded column (Euler) | **Pitchfork**: straight state loses stability, two bent states appear |
| Phase transition / spontaneous symmetry breaking | Pitchfork of an order-parameter ODE; `μ` ↔ (T_c − T) — `statistical-mechanics/` |
| Onset of oscillation in an op-amp / laser | **Hopf** bifurcation creating a stable limit cycle |
| Hysteresis / Schmitt-trigger latching | **Saddle-node** pair bounding a bistable region |

---

## Saddle-Node (Fold / Blue-Sky)

Two fixed points — one stable, one unstable — collide and **annihilate**. The generic way fixed
points are created or destroyed.

```
   NORMAL FORM:   x' = mu - x^2

   Fixed points: x* = +- sqrt(mu).

     mu < 0:  NO real fixed points.  x' = mu - x^2 < 0 always -> x runs off.
     mu = 0:  ONE half-stable point at x*=0 (the bifurcation).
     mu > 0:  TWO fixed points.  x*=+sqrt(mu) stable (f'=-2x<0),
                                 x*=-sqrt(mu) unstable (f'=-2x>0).

   BIFURCATION DIAGRAM:
        x*  ^
            |       ___ stable (+sqrt mu)
            |    __/
        ----+---*------------> mu          "out of the blue sky" two fixed
            |    \__           points appear as mu increases through 0.
            |       \___ unstable (-sqrt mu)
```

**Signature:** a single real eigenvalue passes through 0 *transversally*, no symmetry required. This
is what ends a stable equilibrium when a parameter is pushed too far — a "tipping point." In
`control-theory/`, a saddle-node of equilibria limits the operating range of a regulated plant.

---

## Transcritical

Two fixed points **exchange stability** as they pass through each other. Neither is destroyed —
they trade roles. Typical when `x = 0` is forced to remain a fixed point for all `μ`.

```
   NORMAL FORM:   x' = mu*x - x^2 = x(mu - x)

   Fixed points: x* = 0  (always)  and  x* = mu.

     mu < 0:  x*=0 STABLE  (f'(0)=mu<0),   x*=mu unstable.
     mu = 0:  the two merge.
     mu > 0:  x*=0 UNSTABLE (f'(0)=mu>0),   x*=mu STABLE.

   BIFURCATION DIAGRAM:
        x*  ^        x*=mu (stable for mu>0)
            |       /
            |      /                  The two lines CROSS and swap
        ----+-----X---------> mu      stability. x=0 persists but
            |    / (exchange)          loses stability to x=mu.
            |   /  x=0 (stable mu<0)
```

**Canonical instance:** logistic growth `N' = rN(1 − N/K)`. The extinction state `N=0` is stable
when `r < 0` and unstable when `r > 0`, exchanging stability with the carrying-capacity state — a
transcritical bifurcation in `r`. The threshold `r = 0` is exactly the epidemic/percolation
threshold `R₀ = 1` in disease models.

---

## Pitchfork (the symmetry breaker)

A symmetric (`x → −x`) system: one fixed point loses stability and **two symmetric** ones appear
(supercritical) or **two symmetric unstable** ones collide into it (subcritical). The mechanism of
**spontaneous symmetry breaking**.

```
   SUPERCRITICAL:  x' = mu*x - x^3            SUBCRITICAL:  x' = mu*x + x^3
   (soft, safe)                               (hard, dangerous)

   Fixed pts: x*=0 and x*=+-sqrt(mu)          Fixed pts: x*=0 and x*=+-sqrt(-mu)
              (exist for mu>0)                           (exist for mu<0, UNSTABLE)

     x* ^                                       x* ^   unstable branches
        |    __/ stable +sqrt mu                   |  \  (mu<0)
        |   /                                      |   \
     ---+--*-------> mu                         ---+----*-------> mu
        |   \___                                   |   /  |
        |       \_ stable -sqrt mu                 |  /   x=0 stable for mu<0,
        x=0 stable mu<0, unstable mu>0             unstable for mu>0 -> JUMPS
```

```
   SUPERCRITICAL                        SUBCRITICAL
   - new branches are STABLE            - new branches are UNSTABLE, exist BEFORE
   - continuous, reversible             - x=0 destabilizes with NO nearby stable
   - "second-order" transition            state -> system JUMPS far away
   - column buckling, magnetization     - HYSTERESIS, "first-order" transition,
     above Curie temperature              subcritical Hopf in fluid turbulence
```

The supercritical pitchfork is the bead-on-a-hoop bifurcation (Ch. 01) and the Ising/mean-field
magnet (`statistical-mechanics/`): below `T_c` magnetization picks `+m` or `−m`. The subcritical
version is the dangerous one — the safe state vanishes with no nearby replacement, so the system
leaps to a distant attractor. Engineers fear subcritical bifurcations for exactly this reason.

---

## Hopf (birth of oscillation)

The only one of the four that needs **two dimensions** and produces a **limit cycle**. A complex
conjugate eigenvalue pair `λ = α(μ) ± iω` crosses the imaginary axis: `α(μ)` changes sign while
`ω ≠ 0`. The fixed point's spiral flips stability and sheds (or absorbs) a periodic orbit.

```
   EIGENVALUE CROSSING:                NORMAL FORM (polar, r = amplitude):
        Im                                 r' = mu*r - r^3   (supercritical)
         ^   lambda(mu)                    theta' = omega + ...
         |  o-->|-->o   as mu increases
   ------+------|------> Re             Fixed pt r=0 ringed by a limit cycle
         |  o-->|-->o                   at r* = sqrt(mu) when mu > 0.
         |     mu=0 (cross axis)
                                        Compare: this is the PITCHFORK normal
   pair moves from LHP (stable spiral)  form in the RADIUS r -- a "rotating
   to RHP (unstable spiral)             pitchfork." Amplitude ~ sqrt(mu).

   SUPERCRITICAL HOPF:                  SUBCRITICAL HOPF:
        amplitude                            amplitude
          | ___ stable cycle (~sqrt mu)        |\  unstable cycle (mu<0)
          |/                                   | \   then JUMP to far cycle
       ---*------> mu  (soft onset)         ---*----> mu  (hard onset, hysteresis)
        stable->unstable fixed pt            dangerous: oscillation appears
                                             with finite amplitude abruptly
```

> **Hopf bifurcation theorem (Andronov–Hopf).** If a complex pair crosses the imaginary axis
> transversally (`dα/dμ ≠ 0` at `μ=0`) with `ω ≠ 0` and the first **Lyapunov coefficient** is
> nonzero, a one-parameter family of periodic orbits emerges. Its sign decides super- vs
> subcritical: negative ⇒ supercritical (stable cycle, amplitude `∝ √μ`); positive ⇒ subcritical.

Hopf is everywhere oscillation is born from rest: heartbeats, lasers turning on, the van der Pol
oscillator (Ch. 04), the onset of self-sustained vibration in a flutter-prone wing, and the
instability that opens the **route to chaos** in the Lorenz system (Ch. 06). In `control-theory/`,
a too-aggressive gain that makes the closed loop ring is a Hopf bifurcation of the feedback system.

---

## Codimension and the Bifurcation Hierarchy

```
   CODIMENSION = how many parameters you must tune to MEET the bifurcation
                 = number of independent conditions (e.g. Re(lambda)=0).

   Codim 1 (one knob):   saddle-node, transcritical, pitchfork, Hopf
                         -- generic; you hit these by sweeping a single parameter.

   Codim 2 (two knobs):  cusp (two saddle-nodes meeting),
                         Bogdanov-Takens (saddle-node + Hopf collide),
                         Bautin/generalized Hopf (super/subcritical switch).
                         -- organizing centers; unfold into codim-1 curves nearby.
```

```
   THE CUSP (codim 2): x' = mu1 + mu2*x - x^3   -- the hysteresis machine

        x*                         Two saddle-node curves bound a wedge in
         |   ___  upper branch     (mu1, mu2) space. Inside the wedge: THREE
         |  /   \                  fixed points (bistability). Crossing a
         | /     \___ folds        fold edge -> a CATASTROPHIC jump.
         |/          lower branch  This is the canonical model of hysteresis,
        -+------------> mu1        switches, and perception bistability.
```

The cusp catastrophe is the bistable/hysteresis backbone: two saddle-node folds meeting at a point.
It is the same object as a Schmitt trigger's latch and as first-order phase transitions with a
spinodal region. Codim-2 points are "organizing centers" — locate one and the nearby codim-1 curves
are forced to exist.

---

## Worked Example: Classifying a Bifurcation

```
   x' = mu - x - e^{-x}                 (a 1D system, parameter mu)

   1. Fixed points: mu = x + e^{-x}.  Let g(x) = x + e^{-x}; g'(x) = 1 - e^{-x}.
      g has a MINIMUM at x=0 where g(0)=1, g'(0)=0.  So:
        mu < 1:  no solution (line mu below the min) -> NO fixed points.
        mu = 1:  tangency at x=0 -> ONE fixed point.
        mu > 1:  TWO fixed points (one on each side of x=0).

   2. Two fixed points born from nothing as mu increases through 1
      => SADDLE-NODE bifurcation at (mu, x) = (1, 0).

   3. Confirm with the normal form: near x=0, e^{-x} ~ 1 - x + x^2/2, so
        x' ~ mu - x - (1 - x + x^2/2) = (mu - 1) - x^2/2.
      Let nu = mu - 1:  x' = nu - x^2/2  -- the saddle-node normal form. QED.
```

---

## Decision Cheat Sheet

| Observed change as `μ` varies | Bifurcation | Normal form |
|---|---|---|
| Two fixed points appear/vanish from nothing | Saddle-node (fold) | `ẋ = μ − x²` |
| Two fixed points cross and swap stability | Transcritical | `ẋ = μx − x²` |
| One symmetric point → two symmetric stable ones | Supercritical pitchfork | `ẋ = μx − x³` |
| Symmetric point destabilizes, no nearby stable state | Subcritical pitchfork | `ẋ = μx + x³` |
| Spiral flips stability, smooth oscillation grows | Supercritical Hopf | `ṙ = μr − r³` |
| Oscillation appears abruptly at finite amplitude | Subcritical Hopf | `ṙ = μr + r³` |
| Bistability + jumps + hysteresis | Cusp (codim 2) | `ẋ = μ₁ + μ₂x − x³` |
| A *real* eigenvalue crosses 0 | One of the first three (symmetry decides which) | — |
| A *complex pair* crosses imaginary axis | Hopf | — |

---

## Common Confusion Points

### "Saddle-node vs pitchfork — both create fixed points"

Count and symmetry. Saddle-node: **two** points (no symmetry needed), born together off-axis.
Pitchfork: requires `x → −x` symmetry, a central point **persists** while **two symmetric** ones
appear. If your system has no symmetry, a "pitchfork" you think you see is really a saddle-node plus
a transcritical nearby — pitchforks are *non-generic* and break into those under perturbation.

### "Supercritical vs subcritical — which is the safe one?"

**Supercritical = soft/safe**: the new attractor emerges continuously from the old one, amplitude
grows like `√(μ−μc)`, fully reversible. **Subcritical = hard/dangerous**: the current state vanishes
with no nearby replacement, so the system **jumps** to a distant attractor and exhibits
**hysteresis** (you can't reverse by backing the parameter off slightly). The sign of the cubic term
(or Lyapunov coefficient) distinguishes them; getting it wrong inverts your stability prediction.

### "Hopf gave me a limit cycle — is it stable?"

Only if **supercritical** (negative first Lyapunov coefficient). A subcritical Hopf produces an
**unstable** cycle that acts as a basin boundary, and the real (stable) oscillation lives far away.
The linearization alone (a pair crossing `iω`) cannot tell you which — you must compute the Lyapunov
coefficient. This is the rotating analogue of the super/subcritical pitchfork confusion above.

### "The eigenvalue is exactly zero — which bifurcation is it?"

A zero real eigenvalue is *necessary* but not *sufficient* to name the bifurcation; the **nonlinear
terms** (and any symmetry) pick saddle-node vs transcritical vs pitchfork. A pure imaginary pair
signals Hopf. The recipe: reduce to the center manifold, compute the normal-form coefficients, and
read off the type. Eigenvalues tell you a bifurcation *happens*; normal forms tell you *which*.

### "Local bifurcations are the whole story"

No — these four are *local* (born at a fixed point). There are **global** bifurcations where invariant
manifolds collide far from any fixed point: **homoclinic** (a cycle collides with a saddle),
**heteroclinic**, and **period-doubling/saddle-node of cycles**. The period-doubling cascade that
launches chaos (Ch. 05) is a global phenomenon of *cycles*, not of fixed points — a different and
essential class.
