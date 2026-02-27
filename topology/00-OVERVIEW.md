# Topology — Landscape Overview

## The Big Picture

```
<!-- @editor[diagram/P2]: Diagram lists branches and their items but doesn't show how they feed into each other or into modern developments — rework to show the dependency flow: point-set → algebraic → differential → TDA/physics, and add a modern layer (∞-categories, HoTT, derived algebraic geometry) that the learner explicitly needs per calibration -->
+====================================================================+
|              TOPOLOGY — THREE BRANCHES                             |
+====================================================================+
|                                                                    |
|  POINT-SET TOPOLOGY       ALGEBRAIC TOPOLOGY    DIFFERENTIAL TOP.  |
|  (General topology)                                               |
|  +-----------------+     +------------------+  +---------------+  |
|  |Topological      |     |Fundamental group |  |Smooth manifolds| |
|  |spaces           |     |π₁(X)             |  |Tangent bundles | |
|  |Continuous maps  |     |Homology H_n(X)   |  |De Rham cohom. | |
|  |Compactness      |     |Cohomology H^n(X) |  |Differential   | |
|  |Connectedness    |     |Exact sequences   |  |forms, Stokes  | |
|  |Separation axioms|     |Van Kampen, Mayer-|  |Morse theory   | |
|  |Metrization      |     |Vietoris, ATIYAH  |  |h-cobordism    | |
|  +-----------------+     +------------------+  +---------------+  |
|         |                       |                      |          |
|         +----------+------------+----------+-----------+          |
|                    |                       |                      |
|            TOPOLOGICAL          GEOMETRIC/LOW-DIMENSIONAL          |
|            DATA ANALYSIS        TOPOLOGY                          |
|            Persistent homology  Knot theory                       |
|            Mapper algorithm     3-manifolds, Thurston             |
|            Shape analysis       Poincaré conjecture (proved!)     |
+====================================================================+
```

The central question: **when are two spaces "the same"?**
Topology makes "same" mean "homeomorphic" (continuous bijection with continuous inverse).
Two spaces are topologically equivalent if one can be continuously deformed into the other
without tearing or gluing.

---

## The Abstraction Hierarchy

```
METRIC SPACE → TOPOLOGICAL SPACE → (just a set of points)

A metric d(x,y) gives concrete distances.
A topology specifies which sets are "open" — the abstract structure.

WHY GENERALIZE FROM METRIC?
  Products of infinitely many metric spaces need not be metrizable.
  Weak topology on Banach space (functional analysis) is not metric.
  Algebraic geometry's Zariski topology is not even Hausdorff!
  The "correct" notion of continuity is open-set preservation.

OPEN SET AXIOMS:
  1. ∅ and X are open.
  2. Arbitrary unions of open sets are open.
  3. Finite intersections of open sets are open.

From these three axioms: continuous maps, homeomorphisms, and ALL of topology.
```

---

## Why Topology Matters

```
ANALYSIS CONNECTION:
  Completeness, convergence, compactness — all topological.
  Uniform continuity needs metric; continuity needs only topology.
  The Baire Category Theorem (complete metric spaces) ← used everywhere in analysis.
  Banach's fixed point theorem ← contractive maps on complete metric spaces.

ALGEBRA CONNECTION:
  The Galois group Gal(Q̄/Q) carries a profinite topology.
  Algebraic K-theory uses topology of classifying spaces BGL(R).
  Lie groups: groups that are also smooth manifolds.

PHYSICS CONNECTION:
  Configuration space of a mechanical system = a manifold.
  Phase space = cotangent bundle (canonical symplectic structure).
  Topological phases of matter (TKNN invariant, Chern numbers) — see 10-APPLICATIONS.md.
  Fiber bundles: gauge theories (electromagnetism = U(1) bundle, Yang-Mills = non-abelian).

DATA SCIENCE CONNECTION:
  Topological Data Analysis: shape of data modeled by persistent homology.
  Mapper algorithm: "coarse topology" of data clouds.
  Neural networks: topology of loss landscapes.
```

---

## Key Topological Invariants

```
An invariant is a property preserved by homeomorphisms.
If X and Y differ on an invariant: X ≇ Y (not homeomorphic).

BASIC INVARIANTS:
  Connected: is the space in one piece?
  Path-connected: can any two points be joined by a path?
  Simply connected: is every loop contractible?
  Compact: does every open cover have a finite subcover?
  Hausdorff: can distinct points be separated by open sets?

ALGEBRAIC INVARIANTS:
  π₁(X) — fundamental group (loops up to homotopy).
  πₙ(X) — higher homotopy groups.
  H_n(X; R) — homology groups (holes of dimension n).
  H^n(X; R) — cohomology groups (dual to homology, with ring structure).
  χ(X) = Σ(-1)^n rank H_n(X) — Euler characteristic.

INVARIANTS THAT DISTINGUISH SURFACES:
  Sphere S²: π₁={e}, H₀=Z, H₁=0, H₂=Z, χ=2.
  Torus T²: π₁=Z×Z, H₀=Z, H₁=Z², H₂=Z, χ=0.
  Klein bottle: π₁ complicated, not orientable.
  RP²: π₁=Z/2, H₁=Z/2 (torsion!), χ=1, not orientable.
```

---

## The Classification Results

```
SURFACES (2-manifolds):
  Compact, connected, orientable surfaces classified by genus:
  S² (genus 0), T² (genus 1), genus-2 surface, ...
  Connected sum: Σ_g = T² # T² # ... # T² (g times).

  Compact, connected, non-orientable surfaces:
  RP² (1 crosscap), Klein bottle (2 crosscaps), ...

  Classification complete: every closed surface is a genus-g surface or
  connected sum of projective planes. ← COMPLETE THEOREM

3-MANIFOLDS (Thurston's geometrization, Perelman 2003):
  Every closed orientable 3-manifold decomposes into pieces, each
  admitting one of 8 geometric structures.
  Special case: Poincaré conjecture (Millenium Prize): S³ is the only
  simply-connected closed 3-manifold. Proved by Perelman using Ricci flow.

4-MANIFOLDS: Wild — smooth and topological classifications differ.
  Donaldson's theorem (1983), Freedman's classification (1982).
  Exotic R⁴: homeomorphic to R⁴ but not diffeomorphic. Unique to dimension 4.

n-MANIFOLDS (n ≥ 5): Surgery theory, h-cobordism theorem.
  Smale proved Poincaré conjecture in dimensions ≥ 5 (1961).
  Freedman proved it in dimension 4 (1982).
  Perelman proved it in dimension 3 (2003).
```

---

<!-- @editor[content/P1]: No mention of modern developments the learner explicitly needs: ∞-categories (∞-topoi, (∞,1)-categories in homotopy theory), homotopy type theory (HoTT / Univalent Foundations — topology as a foundation for math), and derived algebraic geometry. These are flagged as "DOES need" in the learner calibration. A single section here orienting the learner to where classical topology meets these modern frameworks would unblock 10-APPLICATIONS.md and set context for all files. -->

<!-- @editor[content/P2]: Knot theory connections to biology/physics (DNA topology, protein knotting, topological quantum computing via anyons) are listed in "DOES need" but get only a one-liner in the overview diagram. The overview should orient the learner to the depth available and point to 10-APPLICATIONS.md explicitly. -->

## File-by-File Guide

| File | Content |
|------|---------|
| 01-METRIC-SPACES.md | Metrics, completeness, Baire category, Banach fixed point |
| 02-TOPOLOGICAL-SPACES.md | Open set axioms, bases, product, quotient topologies |
| 03-CONTINUITY-HOMEOMORPHISM.md | Continuous maps, homeomorphisms, topological invariants |
| 04-COMPACTNESS.md | Covers, Heine-Borel, sequential, function spaces |
| 05-CONNECTEDNESS.md | Connected, path-connected, simply connected, Jordan theorem |
| 06-FUNDAMENTAL-GROUP.md | π₁, van Kampen, covering spaces, deck transformations |
| 07-HOMOLOGY.md | Chain complexes, homology, Euler char., exact sequences |
| 08-COHOMOLOGY.md | De Rham, cup product, Poincaré duality, characteristic classes |
| 09-MANIFOLDS.md | Charts, tangent bundles, classification of surfaces |
| 10-APPLICATIONS.md | TDA (persistent homology), topological phases, robotics |

---

## Decision Cheat Sheet

| Question | Topological Tool |
|----------|-----------------|
| Are these spaces homeomorphic? | Compare invariants: π₁, homology, Euler char. |
| Is a sequence convergent? | Topology of the space (open sets / metric) |
| Is every bounded sequence in X subsequentially convergent? | Compactness (sequential) |
| Can f: X→Y be extended or lifted? | Covering space theory, exact sequences |
| What shape is a point cloud? | Persistent homology (TDA) |
| Is this material a topological insulator? | Chern number / TKNN invariant |
| What's the configuration space of a robot? | Manifold theory (joint space) |
| Does this differential equation have a solution? | Topological fixed point theory |

---

## Common Confusion Points

**"Topology = rubber sheet geometry."**
Topology is about which properties are preserved by continuous bijections.
It is NOT about stretching rubber — you cannot tear or glue.
In practice: much of topology uses algebraic tools (homology, homotopy groups),
not geometric intuition at all.

**"All metric spaces are topological spaces."**
Correct direction: every metric space gives a topological space (open sets = unions
of open balls). But not every topological space is metrizable (can be given a metric
inducing the topology). The Zariski topology (algebraic geometry) is not metrizable.

**"Homeomorphic = same shape visually."**
A coffee cup is homeomorphic to a donut (both have genus 1). A sphere is NOT
homeomorphic to a torus (different genus). The visual appearance is misleading;
only the topological invariants matter.

**"Algebraic topology computes things exactly."**
For nice spaces (CW complexes, manifolds), yes. For pathological spaces (Cantor set,
long line), the computations can be subtle. Homotopy groups of spheres πₙ(S^k) are
notoriously complicated and not fully computed.
