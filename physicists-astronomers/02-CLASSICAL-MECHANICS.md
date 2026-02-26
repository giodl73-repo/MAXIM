# Classical Mechanics — Newton, Hooke, Huygens, Lagrange, Hamilton

## The Framework Being Built

Classical mechanics is the mathematical description of how macroscopic objects
move under forces. It ran physics from 1687 to ~1900, and remains the right
framework for objects larger than atoms moving slower than ~10% the speed of light.

```
CLASSICAL MECHANICS — ARCHITECTURE
=====================================

NEWTON (1687): Forces cause acceleration.
  F = ma. Three laws. Law of gravitation.
  The foundation.

HOOKE, HUYGENS (contemporaries): specific forces and phenomena.
  Springs, pendulums, wave theory, centripetal force.

LAGRANGE (1788): Reframe in terms of energy and generalized coordinates.
  Action principle. Calculus of variations.
  More powerful than F = ma for complex systems.

HAMILTON (1833): Reformulate Lagrangian mechanics in phase space.
  Hamiltonian mechanics. Hamilton-Jacobi equation.
  The bridge to quantum mechanics.

FLOW:
  Newton (forces) → Lagrange (energy/coordinates) → Hamilton (phase space)
     ↓                         ↓                          ↓
  Engineering           Celestial mechanics          Quantum mechanics
  design                Classical field theory       Statistical mechanics
```

---

## Isaac Newton (1643–1727) — The Physics

Newton's mathematics is covered in File 03 of mathematicians-logicians.
Here the focus is his physical contributions and their implications.

### The Three Laws of Motion

```
NEWTON'S LAWS (Principia, 1687)
================================

LAW 1 (INERTIA):
  A body remains at rest, or in uniform motion in a straight line,
  unless acted upon by a force.
  (Galileo's principle, formalized by Newton)

LAW 2 (FORCE):
  F = ma = dp/dt
  The net force equals the rate of change of momentum.
  (More general form: F = dp/dt handles variable-mass systems)

LAW 3 (ACTION-REACTION):
  For every force F₁₂ (body 1 on body 2),
  there is an equal and opposite force F₂₁ = -F₁₂.
  Forces come in pairs.

Key insight: Forces are REAL entities that CAUSE changes in motion.
  This is non-trivial: Aristotle thought "rest is the natural state."
  Newton: "constant velocity is the natural state; force causes deviation."
```

### Universal Gravitation

```
LAW OF UNIVERSAL GRAVITATION
==============================

Between any two masses m₁ and m₂ separated by distance r:

  F = G · m₁m₂ / r²   (attractive, along the line joining them)

  G = 6.674 × 10⁻¹¹ N·m²/kg²  (Newton didn't know G; measured by Cavendish 1798)

WHAT NEWTON PROVED IN THE PRINCIPIA:
  1. This law implies Kepler's three laws (a complete derivation).
  2. The Moon's orbital acceleration = surface gravity × (R_earth/d_moon)²
     (He checked the numbers — they agreed to ~6% with his original attempt,
      later to better precision.)
  3. Tides are caused by the Moon's differential gravitational pull.
  4. The shape of the Earth (oblate spheroid, flattened at poles).
  5. Precession of the equinoxes (gravitational torque on Earth's equatorial bulge).

SHELL THEOREM:
  A uniform spherical shell attracts an external particle as if all its
  mass were concentrated at the center. (Newton invented this proof.)
  This allows treating planets and stars as point masses.
```

### Newton's Insights on Method

The Principia established **mathematical physics** as a methodology:
hypothesize a mathematical law, derive consequences, compare with observation.
Newton famously wrote "Hypotheses non fingo" (I frame no hypotheses) —
meaning he was not speculating about the cause of gravity, just its law.

---

## Robert Hooke (1635–1703)

### Who He Was

English scientist, curator of experiments for the Royal Society. Polymath who
contributed to: elasticity, optics, microscopy, architecture, and more.
Had an acrimonious dispute with Newton over credit (for gravity's inverse-square
law, optics, and more). Newton destroyed Hooke's portrait after Hooke died.

### The Contribution: Elasticity and the Spring Law

**Hooke's Law (1678)**

```
HOOKE'S LAW
============

F = -kx

The restoring force from a spring is proportional to displacement x
from equilibrium, and directed toward equilibrium (negative sign).

k = spring constant (stiffness of spring)
x = displacement from rest

Consequence: SIMPLE HARMONIC MOTION
  ma = -kx
  ẍ = -(k/m)x
  Solution: x(t) = A cos(ωt + φ),  ω = √(k/m)
  Period: T = 2π/ω = 2π√(m/k)

Applications:
  - Pendulum (small angles): same math, ω = √(g/L)
  - Molecular vibrations (atomic bonds are springs to first approximation)
  - Sound waves (pressure oscillations in air)
  - Quantum harmonic oscillator: the exactly-solvable QM model;
    every quantum field is an infinite collection of harmonic oscillators
  - Normal modes of any mechanical system
```

Hooke also proposed (before Newton published) that planets orbit due to
an inverse-square attraction. Newton had the mathematics to prove it;
Hooke had the intuition but not the tools.

---

## Christiaan Huygens (1629–1695)

### Who He Was

Dutch mathematician and physicist. Discovered Saturn's rings and Titan (moon),
invented the pendulum clock (most accurate timepiece until the 20th century),
and developed the wave theory of light (in opposition to Newton's particle theory).

### The Contribution: Pendulum, Centripetal Force, Wave Optics

**Pendulum Clock and SHM**

The pendulum clock (1656) kept time to within 10 seconds per day — a massive
improvement. The key physics: for small angles, the period of a pendulum
depends only on its length, not amplitude.

T = 2π√(L/g)  (for small angles, pendulum length L, gravitational acceleration g)

Huygens measured g precisely using pendulums. He discovered that g varies
with latitude (confirming Earth is not a perfect sphere).

**Centripetal Force**

For circular motion at speed v with radius r:
  a_centripetal = v²/r  (directed inward, toward center)
  F_centripetal = mv²/r

Huygens derived this correctly before Newton published. Newton
incorporated it (giving Huygens credit in the Principia).

**Huygens' Principle (Wave Optics)**

```
HUYGENS' PRINCIPLE
===================

Every point on a wavefront acts as a source of secondary spherical wavelets.
The new wavefront is the envelope of all secondary wavelets.

APPLICATIONS:
  - Reflection: explains why angle of incidence = angle of reflection
  - Refraction: explains Snell's law (n₁ sin θ₁ = n₂ sin θ₂)
    The wavefront bends because the speed of light changes in different media.
  - Diffraction: waves bend around corners because secondary sources exist
    at the edge of an obstacle.

This is still used in modern wave optics and acoustics.
Combined with interference (later: Young's double-slit, Fresnel diffraction),
it explains essentially all wave phenomena.
```

---

## Joseph-Louis Lagrange (1736–1813) — The Physics

Lagrange's mathematics is covered in File 03 of mathematicians-logicians.
The physics reformulation he created is covered here.

### Analytical Mechanics

**The Action Principle**

```
HAMILTON'S PRINCIPLE (stated by Maupertuis, proved by Euler/Lagrange):
  The path taken by a physical system is the one that makes
  the ACTION stationary:

  S = ∫ L(q, q̇, t) dt

  where L = T - V (kinetic minus potential energy).

  The condition δS = 0 gives the Euler-Lagrange equations:
    d/dt (∂L/∂q̇ᵢ) - ∂L/∂qᵢ = 0  for each coordinate i.

WHY THIS IS PROFOUND:
  1. You can choose ANY coordinate system (Cartesian, spherical, etc.)
  2. Constraints handled naturally (Lagrange multipliers)
  3. Conservation laws = symmetries of L (Noether's theorem — File 05)
  4. Generalizes to field theory (L becomes a Lagrangian density)
  5. Quantum mechanics path integral: probability amplitude = sum over
     all paths weighted by exp(iS/ℏ) — Feynman's formulation.
```

**Lagrangian Coordinates and Configuration Space**

The brilliant abstraction: describe a system not by forces acting on each
particle, but by:
- **Generalized coordinates** qᵢ that describe the system's configuration
- **Configuration space**: the space of all possible configurations
- **The Lagrangian** L(q, q̇, t) encodes all the physics

Example: Double pendulum
- 2 angles (θ₁, θ₂) as generalized coordinates
- Configuration space is a torus (T²)
- L = T(θ₁, θ₂, θ̇₁, θ̇₂) - V(θ₁, θ₂)
- Euler-Lagrange equations give coupled ODEs

---

## William Rowan Hamilton (1805–1865)

### Who He Was

Irish mathematician and physicist. Child prodigy (knew ~12 languages at age 12).
Predicted conical refraction (1832) before experiment confirmed it.
Discovered quaternions while walking on a Dublin bridge in 1843 —
famously scratching the formula into the stone.

### The Contribution: Hamiltonian Mechanics and Quaternions

**Hamiltonian Mechanics**

```
FROM LAGRANGIAN TO HAMILTONIAN
================================

Lagrangian mechanics: works in (q, q̇) space (configuration + velocity)
Hamiltonian mechanics: works in (q, p) space (position + momentum)

The LEGENDRE TRANSFORM:
  Define conjugate momenta: pᵢ = ∂L/∂q̇ᵢ
  The Hamiltonian: H(q, p, t) = Σᵢ pᵢ q̇ᵢ - L(q, q̇, t)

  For systems where L = T - V with T quadratic in velocities:
    H = T + V = total energy

Hamilton's equations:
  q̇ᵢ = ∂H/∂pᵢ   (positions evolve by momentum gradient)
  ṗᵢ = -∂H/∂qᵢ  (momenta evolve by negative position gradient)

These are 2n first-order ODEs (instead of n second-order).
They have a beautiful symmetry between q and p.

PHASE SPACE:
  State of a system = point (q, p) in 2n-dimensional phase space.
  Time evolution = flow of points through phase space.
  Liouville's theorem: the phase space "volume" is conserved.
  (This is deep: it's equivalent to conservation of information,
   and underlies the second law of thermodynamics.)
```

**Why Hamiltonian Mechanics Matters**

```
CONNECTIONS TO QUANTUM MECHANICS
==================================

Hamiltonian mechanics         Quantum mechanics
-----------------             -----------------
State: (q, p) in phase space  State: |ψ⟩ in Hilbert space
Observable: function f(q,p)   Observable: operator Â
Poisson bracket: {A,B}        Commutator: [Â,B̂] = ÂB̂ - B̂Â
{q,p} = 1                     [q̂,p̂] = iℏ
Evolution: df/dt = {f,H}      dÂ/dt = i/ℏ [Â,Ĥ]

QUANTIZATION PROCEDURE:
  Take classical Hamiltonian H(q,p)
  Replace q → q̂ (position operator), p → p̂ = -iℏ ∂/∂q (momentum operator)
  Get quantum Hamiltonian Ĥ
  Schrödinger equation: iℏ ∂ψ/∂t = Ĥψ

Hamiltonian mechanics is the direct route to quantum mechanics.
Without Hamilton's reformulation, Schrödinger and Heisenberg's work
would look ad hoc. With it, quantization has a natural structure.
```

**Quaternions**

Quaternions: a 4D number system {a + bi + cj + dk} with:
i² = j² = k² = ijk = -1

Hamilton scratched the formula into Broom Bridge in Dublin in 1843.
Vector calculus (dot product, cross product) was extracted from quaternions
by Gibbs and Heaviside in the 1880s.

In modern use: quaternions represent 3D rotations efficiently and without
gimbal lock. Every 3D graphics engine (Unity, Unreal, DirectX) uses quaternions
for rotation. The SLERP (spherical linear interpolation) for smooth animation
uses quaternion arithmetic.

---

## Comparison Table

| Figure | Dates | Core Contribution | Framework | Legacy |
|--------|-------|-------------------|-----------|--------|
| **Newton** | 1643–1727 | F=ma, universal gravitation, Kepler derivation | Force laws | All of engineering, space travel |
| **Hooke** | 1635–1703 | Spring law, elasticity | F = -kx | All oscillation theory |
| **Huygens** | 1629–1695 | Pendulum, centripetal force, wave optics | Wave theory | Optics, precision timekeeping |
| **Lagrange** | 1736–1813 | Analytical mechanics, action principle | Energy/coordinates | QFT, general relativity |
| **Hamilton** | 1805–1865 | Hamiltonian mechanics, phase space, quaternions | Phase space | Quantum mechanics, 3D graphics |

---

## Who to Cite for What

| Concept | Cite | Notes |
|---------|------|-------|
| Newton's laws (F=ma) | Newton | *Principia* 1687 |
| Universal gravitation | Newton | Same |
| Shell theorem | Newton | |
| Kepler's laws from gravitation | Newton | In the Principia |
| Hooke's law F = -kx | Hooke | 1678 |
| Simple harmonic motion | Hooke (physics) + Huygens (pendulum) | |
| Centripetal acceleration v²/r | Huygens | Before Newton published |
| Huygens' principle (wave optics) | Huygens | 1690 |
| Lagrangian mechanics / L = T - V | Lagrange | *Mécanique Analytique* 1788 |
| Euler-Lagrange equations | Euler + Lagrange | Calculus of variations |
| Hamiltonian mechanics | Hamilton | 1833 |
| Phase space / Liouville theorem | Hamilton + Liouville | |
| Quaternions | Hamilton | 1843 |

---

## Common Confusion Points

**"Newtonian mechanics is exact"** — It is exact in the limit v << c (special
relativity corrections negligible) and objects >> quantum scale. GPS satellites
run at v/c ≈ 10⁻⁵ and require SR corrections of ~7 microseconds/day from their
speed plus GR corrections of ~45 microseconds/day from reduced gravity at altitude.
Without both corrections, GPS would drift ~10 km/day.

**"The Lagrangian is just a reformulation"** — It reveals structure invisible in
Newton. The Noether theorem (symmetry → conservation law) requires the Lagrangian
formulation. The path integral formulation of QM requires it. The Standard Model
of particle physics is written as a Lagrangian. It's not cosmetically different
from Newton — it's the language in which all subsequent physics is written.

**"Hamilton invented vectors"** — Hamilton invented quaternions. Gibbs and Heaviside
extracted 3D vector algebra from quaternions (discarding the scalar part, using the
vector part). The cross product and dot product are quaternion operations in disguise.

**"Hooke and Newton were just rivals"** — Newton erased Hooke's contributions from
the historical record with deliberate effort. Hooke's portrait vanished (possibly
destroyed by Newton). Newton delayed publication of his optics work until after
Hooke's death. The historical record unfairly underrepresents Hooke's contributions
to gravitation theory and optics.
