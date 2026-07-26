---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "04-LIMIT-CYCLES.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:dynamical-systems:limit-cycles
kind: guide
module: dynamical-systems
section: dynamical-systems
title: Limit Cycles
status: source-custody
source_custody: partial
current_path: dynamical-systems/04-LIMIT-CYCLES.md
canonical_path: dynamical-systems/04-LIMIT-CYCLES.md
backsource_ids: [mdloom-backfill:dynamical-systems:04-limit-cycles, git-history:dynamical-systems:04-limit-cycles]
concepts: [limit, cycles]
root_concepts: [limit, cycles]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Limit Cycles

A **limit cycle** is an isolated closed orbit: a periodic trajectory that nearby trajectories
spiral toward (stable) or away from (unstable). Unlike the centers of conservative systems (a
*continuum* of nested closed orbits), a limit cycle is *structurally robust* — it survives small
perturbations and self-corrects in amplitude. This is the mathematics of every self-sustained
oscillation: heartbeats, neurons firing, lasers, clocks, predator–prey cycles. In 2D continuous
flows, limit cycles are the *only* recurrent behavior besides fixed points — and the
**Poincaré–Bendixson theorem** is what proves that, ruling out chaos in the plane.

```
              CENTER (conservative)         LIMIT CYCLE (dissipative)
              =====================         =========================
                   ___                          ___
                  /   \  nested closed         /   \   ONE isolated orbit;
                 / ___ \  orbits, a            |  ->-|  outside spirals IN,
                | / * \ |  CONTINUUM           |  *  |  inside spirals OUT.
                 \ \_/ /  (fragile)            |->---|  Amplitude is
                  \___/                         \___/   SELF-SELECTED.
              amplitude set by initial         amplitude set by the
              condition; no attraction          system; attracting.

       A limit cycle is to a center what a stable spiral is to a stable node:
       the structurally stable, dissipative, "real engineering" version.
```

---

## What Makes a Cycle a *Limit* Cycle

```
   ISOLATED:    in a neighborhood of the cycle Gamma, there is NO other
                closed orbit. (Centers fail this -- they come in families.)

   ATTRACTING (stable) limit cycle:
        trajectories from both inside and outside spiral ONTO Gamma.
        => omega-limit set of a whole annulus is Gamma itself.

   STABILITY via the FLOQUET / characteristic multiplier:
        Linearize the Poincare return map about the cycle.
        multiplier |m| < 1  -> stable cycle   (analogue of |lambda|<1 for maps)
        multiplier |m| > 1  -> unstable cycle
        One multiplier is always 1 (motion ALONG the cycle is neutral).
```

The stability of a cycle is the stability of its **Poincaré map** fixed point (Ch. 06/08): lay a
small surface across the cycle, record where successive crossings land, and the cycle is stable iff
that 1D return map contracts. This converts a continuous-time question into the discrete-map
machinery — the unifying trick of the whole directory.

### Old world → new world bridges

| You already know | Limit-cycle framing |
|---|---|
| LC oscillator / op-amp that "rings" steadily | A stable limit cycle (born at a Hopf — Ch. 03) |
| PLL or relaxation timer | Relaxation oscillation; van der Pol at large `μ` |
| A control loop that hunts at fixed amplitude | Limit cycle from a Hopf in the closed loop (`control-theory/01`) |
| Predator–prey population swings | Lotka–Volterra (a *center*) → realistic models give a limit cycle |
| Clock recovery / injection locking | Forced/coupled oscillators → synchronization (Ch. 09) |

---

## Poincaré–Bendixson: Why the Plane Can't Be Chaotic

The theorem that grades the whole subject by dimension. It says a *bounded, non-fixed-point*
trajectory in 2D has nowhere to go *but* a closed orbit.

> **Poincaré–Bendixson theorem.** Let `R` be a closed, bounded region of the plane containing no
> fixed points, and suppose a trajectory enters `R` and never leaves. Then `R` contains a periodic
> orbit, and the trajectory either *is* that orbit or spirals onto it.

```
   THE TRAPPING-REGION ARGUMENT (the standard recipe):

   1. Build an annulus R (a ring) such that the flow points INWARD on
      BOTH boundaries -> trajectories enter and cannot escape.

           outer boundary: flow points IN
              ___________
             /  _______  \           No fixed point inside the ring.
            /  / inflow \  \          => by Poincare-Bendixson, R must
           |  | --> O <-- |  |        contain a LIMIT CYCLE.  The
            \  \ inflow  /  /          trajectory has nowhere else to go:
             \  \______ /  /           can't hit a fixed point, can't
              \__________ /            leave, can't cross itself.
           inner boundary: flow points OUT (e.g. an unstable fixed point)

   2. Verify no fixed points in R.
   3. Conclude a periodic orbit exists.
```

**The dimensional punchline:** the proof rests on the **Jordan curve theorem** — in the plane, a
closed orbit *separates* inside from outside, and trajectories cannot cross (uniqueness, Ch. 00), so
they get *trapped* and forced into periodicity. In 3D there is no such separation; trajectories can
stretch and fold around a closed loop without crossing it — leaving room for the strange attractors
of Chapter 06. **No chaos in 2D continuous autonomous flows. Period.**

(Escape hatches: a *non-autonomous* 2D flow is secretly 3D, and a 2D *map* — Hénon — is not covered;
both can be chaotic. The theorem is specifically about autonomous *flows* in the plane.)

---

## Ruling Cycles *Out*: Negative Criteria

Two tools prove a region has *no* limit cycle — the complement of Poincaré–Bendixson.

```
   BENDIXSON'S CRITERION:
     If div f = df1/dx + df2/dy has ONE SIGN (never zero) on a simply
     connected region D, then NO closed orbit lies entirely in D.
     (A cycle would enclose zero net area-change; impossible if div f != 0.)

   DULAC'S REFINEMENT:
     Same, but for div(g*f) for some chosen weight g(x,y) > 0.
     Choosing a clever g rules out cycles when plain div f changes sign.

   INDEX THEORY (topological count):
     index of a simple closed curve = how many times the vector field
     winds as you traverse it.
       node/spiral/center: index +1     saddle: index -1
     A closed orbit has index +1 and must ENCLOSE fixed points whose
     indices SUM to +1.  => a cycle must surround at least one fixed point,
     and cannot surround only saddles.
```

Index theory gives instant negative results: a limit cycle must enclose a fixed-point set of total
index `+1`, so it cannot encircle nothing, cannot encircle a lone saddle, and must wrap (typically)
a single spiral/node. This is the cheapest sanity check on any proposed cycle.

---

## The van der Pol Oscillator (the canonical limit cycle)

The model that launched nonlinear oscillation theory (vacuum-tube circuits, 1920s). A linear
oscillator with **amplitude-dependent damping**: it pumps energy in when small, bleeds it out when
large — forcing convergence to one amplitude.

```
   x'' - mu(1 - x^2) x' + x = 0      mu > 0 controls nonlinearity

   Damping term: -mu(1 - x^2) x'
     |x| < 1:  (1 - x^2) > 0  -> NEGATIVE damping  -> amplitude GROWS
     |x| > 1:  (1 - x^2) < 0  -> POSITIVE damping  -> amplitude SHRINKS
   => a unique stable limit cycle where the two effects balance.

   As a first-order system (Lienard form, y = x' /mu + ... ):
        x' = mu (y - x^3/3 + x)
        y' = -x/mu

   PHASE PORTRAIT (small mu ~ near-circular | large mu ~ relaxation):

      small mu:  __          large mu:   ___________
                /  \  nearly             |          |  fast jumps
               | -> |  harmonic          |    ___   |  (horizontal),
                \__/   limit cycle       |   |   |--+  slow crawls
                                         +--|   |      (vertical)
                                            |___|      = RELAXATION
```

> **Liénard's theorem.** For `x'' + f(x)x' + g(x) = 0` with `g` odd, `f` even, `F(x) = ∫₀ˣ f`
> having a single positive zero and being monotone increasing past it (plus growth at infinity),
> there exists a **unique, stable limit cycle**. Van der Pol satisfies the hypotheses for every
> `μ > 0` — hence exactly one self-sustained oscillation.

---

## Relaxation Oscillations (the large-`μ` regime)

When `μ` is large, the van der Pol cycle stops being sinusoidal and becomes a sequence of **fast
jumps and slow crawls** — a relaxation oscillation. This is a **two-timescale (singular
perturbation)** phenomenon, the basis of every "charge slowly, dump quickly" oscillator.

```
   The trajectory hugs the slow CUBIC NULLCLINE y = x^3/3 - x,
   crawling along its stable branches, then JUMPS at the folds:

        y |    fold .                    SLOW (crawl down the
          |       \  .                   left branch)         |
          |  jump  \  \___ slow             |  FAST jump      v
          |  <----  \      \  branch     ---+--->  (across)
          |          \___   \                ^
          |    slow       \   fold          |  SLOW (crawl up
          |    branch      \  / jump         |  the right branch)
          +-------------------------> x

   Period scales as  T ~ mu * (3 - 2 ln 2)  for large mu  (set by the SLOW
   crawls, not the jumps). Two timescales: O(1/mu) jumps, O(mu) crawls.
```

Relaxation oscillators model neuron spiking (FitzHugh–Nagumo is a van der Pol cousin), cardiac
pacemakers, and the classic 555-timer/RC sawtooth. The **separation of timescales** is the same
*stiffness* structure that `numerical-methods/06` warns about — naive explicit integrators choke on
the fast jumps and need implicit/stiff solvers. The slow manifold here is a **center manifold**
(Ch. 03) made dynamical.

---

## Where Limit Cycles Come From, Where They Go

```
   BIRTH of a limit cycle:                 DEATH of a limit cycle:
   - HOPF bifurcation (Ch. 03): a fixed     - HOMOCLINIC bifurcation: cycle grows
     point sheds a small cycle, r~sqrt(mu)    until it collides with a saddle and
   - SADDLE-NODE of cycles: a stable +        is destroyed (infinite period).
     unstable cycle appear together         - INVERSE Hopf: shrinks back into a
   - GLOBAL/SNIC: cycle born on a saddle-     fixed point.
     node on an invariant circle            - PERIOD-DOUBLING: cycle -> 2x period
     (excitable -> oscillatory, neurons)      cycle -> ... -> CHAOS (Ch. 05).
```

The period-doubling exit is the crucial link forward: a limit cycle whose Poincaré-map fixed point
crosses multiplier `m = −1` doubles its period, and a *cascade* of such doublings is one of the
standard **routes to chaos** (Ch. 05). Limit cycles are thus both the ceiling of 2D dynamics and
the launching pad into 3D chaos.

---

## Worked Example: A Guaranteed Limit Cycle

```
   In polar coordinates:   r' = r(1 - r^2),   theta' = 1.

   theta' = 1 > 0: pure rotation, the angle always advances.
   r' = r(1 - r^2):  fixed radii at r=0 and r=1.
        r < 1:  r' > 0  -> r grows toward 1.
        r > 1:  r' < 0  -> r shrinks toward 1.
   => r = 1 is an attracting closed orbit:  a STABLE LIMIT CYCLE
      (a unit circle traversed at unit angular speed).

   Cross-check by Poincare-Bendixson: the annulus 1/2 <= r <= 2 is a
   trapping region (flow inward on both edges) with no fixed point inside.
   Theorem guarantees the cycle that we found explicitly. Consistent.

   Origin r=0 is an unstable spiral (linearize: lambda = 1 +- i) feeding
   the cycle from inside; this whole picture is a supercritical Hopf in
   disguise if we replace 1 by a parameter mu.
```

---

## Decision Cheat Sheet

| Goal | Tool |
|---|---|
| Prove a limit cycle *exists* (2D) | Poincaré–Bendixson: build a trapping region with no fixed point |
| Prove a unique stable cycle (Liénard class) | Liénard's theorem |
| Prove *no* cycle in a region | Bendixson (`div f` one sign) or Dulac (weighted) |
| Quick topological screen | Index theory: a cycle encloses fixed points of total index `+1` |
| Determine cycle stability | Floquet multiplier `|m| < 1` (Poincaré-map contraction) |
| Explain birth of oscillation from rest | Hopf bifurcation (Ch. 03) |
| Model fast-spike / slow-recover oscillation | Relaxation oscillation, large-`μ` van der Pol |
| Anticipate numerical stiffness | Two-timescale relaxation ⇒ use stiff solvers (`numerical-methods/06`) |
| See the road to chaos from a cycle | Period-doubling of the Poincaré map (Ch. 05) |

---

## Common Confusion Points

### "Limit cycle vs center — both are closed orbits"

A **center** has a *continuum* of nested closed orbits (conservative; amplitude set by initial
condition; fragile — any damping destroys it). A **limit cycle** is a *single isolated* closed orbit
that *attracts* (dissipative; amplitude set by the system; robust). The undamped pendulum and
Lotka–Volterra have centers; van der Pol has a limit cycle. If perturbing the system slightly
destroys the orbit, it was a center, not a limit cycle.

### "Poincaré–Bendixson means no oscillations in 2D"

Backwards — it *guarantees* oscillations (limit cycles) in 2D under trapping. What it forbids is
**chaos**: the *only* bounded recurrent behaviors in a 2D autonomous flow are fixed points and
periodic orbits. Quasi-periodicity and chaos require ≥ 3 dimensions (or a map, or time-dependence).

### "My 2D model is chaotic"

Then it is not an autonomous 2D flow. Check for: (a) **explicit time dependence** `f(x, t)` — a
forced 2D system is really 3D (`t' = 1`), e.g. the forced Duffing/pendulum; (b) it's a **discrete
map**, not a flow (Hénon, Ch. 08); or (c) a hidden third state variable. Genuine autonomous planar
flows cannot be chaotic — Poincaré–Bendixson is a theorem.

### "Is the cycle's amplitude set by where I start?"

For a **limit cycle**, no — the amplitude is intrinsic; all nearby starts converge to the same
orbit (that's what makes oscillators useful as clocks). For a **center**, yes — each initial
condition rides its own orbit forever. This is the operational test distinguishing the two.

### "Relaxation oscillation period = jump time?"

No — the period is dominated by the **slow crawls** along the stable branches, not the fast jumps.
For large-`μ` van der Pol, `T ∝ μ` from the slow segments while the jumps take `O(1/μ)`. The
counterintuitive scaling (bigger nonlinearity → longer period) is a hallmark of relaxation dynamics.
