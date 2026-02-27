# Magnetostatics — Currents, Fields, and the Vector Potential

## The Big Picture

Magnetostatics is E&M with currents steady in time — charges moving at
constant rate, no acceleration, no changing fields. The magnetic analog
of electrostatics, but with a structural difference that runs deep:
**there are no magnetic monopoles**.

```
+------------------------------------------------------------------------+
|                     MAGNETOSTATICS LANDSCAPE                           |
|                                                                        |
|   SOURCE          CREATES            FIELD          DESCRIBED BY       |
|   ──────          ───────            ─────          ────────────       |
|                                                                        |
|   current J  ──>  force on           B(x,y,z)       ∇·B  = 0          |
|   (vector)        moving charges     vector field    ∇×B  = μ₀J        |
|                                          │                             |
|                                          │ B = ∇×A                    |
|                                          ▼                             |
|                                     A(x,y,z)       ∇²A = -μ₀J        |
|                                     vector field   (Coulomb gauge)     |
|                                                                        |
|   FORCE ON CHARGE:   F = q(E + v×B)   ← Lorentz force (full)         |
|   FORCE ON WIRE:     F = I L×B                                         |
+------------------------------------------------------------------------+
```

Compare directly with electrostatics:

```
  ELECTROSTATICS              MAGNETOSTATICS
  ──────────────              ──────────────
  Source: charge ρ            Source: current J
  Field: E                    Field: B
  ∇·E = ρ/ε₀  (monopoles)    ∇·B = 0  (no monopoles)
  ∇×E = 0     (static)        ∇×B = μ₀J
  Potential: V (scalar)       Potential: A (vector)
  E = -∇V                     B = ∇×A
  ∇²V = -ρ/ε₀                 ∇²A = -μ₀J
```

Same mathematical structure — Poisson's equation for the potential —
but E has sources (charges), B does not.

---

## The Lorentz Force

The force on a charge q moving with velocity v in fields E and B:

```
  F = q(E + v×B)     ← Lorentz force law

  Electric part:  qE    — acts on charge regardless of motion
  Magnetic part:  qv×B  — acts only on moving charges, perpendicular to v
```

**The cross product v×B**: perpendicular to both v and B, determined by
right-hand rule. Point fingers along v, curl toward B — thumb is v×B.

```
  v = v x̂  (moving right)
  B = B ẑ  (pointing out of page)

  v×B = vB (x̂ × ẑ) = -vB ŷ    ← force is downward
```

**Key consequence**: the magnetic force is always perpendicular to velocity.
Therefore **magnetic fields do no work** on charges. They change direction
of motion, never speed. A magnetic field alone cannot accelerate a charge
from rest — it needs to already be moving.

This is why motors need both: the current in the wire provides moving charges,
the external B field deflects them, and the deflection (torque) does the work
through the mechanical constraint of the wire geometry.

---

## Current and Current Density

**Current** I: charge per unit time crossing a surface (amperes = C/s).

**Current density** J: current per unit area, a vector field (A/m²).
Direction of J = direction of positive charge flow.

```
  Relation:  I = ∫∫_S J·dA

  J is the microscopic field; I is the macroscopic integral over a surface.
  Same relationship as ρ (volume) vs Q (total) for charge.
```

**Ohm's law in field form**: J = σE, where σ is electrical conductivity.
Metals have high σ (free electrons respond strongly to E).
This is the microscopic origin of V = IR from 6.002 — integrating J = σE
over wire geometry gives the circuit-level relation.

**Continuity equation** — charge conservation in field form:

```
  ∂ρ/∂t + ∇·J = 0

  Rate of change of charge density + divergence of current = 0
  (charge flowing out of a volume = decrease in charge inside)
```

In magnetostatics: ∂ρ/∂t = 0 (steady state) → ∇·J = 0.
Steady currents have no sources or sinks — current that flows in must flow out.

---

## Biot-Savart Law

The magnetic field produced by a steady current — the magnetic analog of Coulomb's law:

```
         μ₀   I dl × r̂
  dB  = ────  ──────────
         4π      r²

  μ₀ = 4π × 10⁻⁷ T·m/A    (permeability of free space)
```

Where dl is a directed current element and r̂ points from the element to the
field point. Integrate along the entire current path:

```
         μ₀       dl × r̂
  B(r) = ────  I ∫ ──────
          4π          r²
```

**Direction**: dl×r̂ is perpendicular to both the current direction and
the line from current to field point. For a straight wire, this gives
field lines that circle the wire — right-hand rule: thumb along current,
fingers curl in direction of B.

```
  STRAIGHT WIRE (cross section view):

  Current I  →  into page ⊗

        ↙  ↓  ↘
        ←  ⊗  →     B field circles counterclockwise
        ↖  ↑  ↗     (viewed from behind: current coming toward you, B clockwise)
```

### Biot-Savart: Infinite Straight Wire

Result (derived by integrating along the wire):

```
          μ₀ I
  |B| = ───────    (at distance r from wire)
          2πr
```

Falls as 1/r (not 1/r² like Coulomb) — wire is a 1D source in 3D space.

Direction: circles the wire, right-hand rule.

---

## Ampere's Law — The Magnetostatic Shortcut

Just as Gauss's law is the shortcut for symmetric charge distributions,
Ampere's law is the shortcut for symmetric current distributions.

**Integral form**:

```
  ∮_C B·dl = μ₀ I_enc

  Circulation of B around a closed loop
  = μ₀ × total current threading through the loop
```

**Differential form** (Stokes' theorem applied):

```
  ∇×B = μ₀J
```

**The Amperian loop strategy** (mirrors Gauss's surface strategy):
1. Identify the symmetry
2. Choose a loop where B is constant and parallel (or perpendicular) everywhere
3. Pull |B| out: ∮ B·dl = |B| × (loop perimeter)
4. Set equal to μ₀I_enc and solve

### Example 1: Infinite Straight Wire

Choose a circular loop of radius r centered on the wire.
B is tangential, constant magnitude everywhere on the loop.

```
  ∮ B·dl = |B| × 2πr = μ₀I

          μ₀I
  |B| = ──────    ← same as Biot-Savart result, much faster
          2πr
```

### Example 2: Infinite Solenoid

N turns per unit length, current I. Use a rectangular Amperian loop
with one side inside the solenoid (length L), one side outside.

```
  Outside solenoid:  B = 0  (by symmetry and superposition)
  Inside:   B is uniform, parallel to axis

  ∮ B·dl = B·L = μ₀ (nL) I     (nL turns thread through loop)

  B = μ₀nI    inside solenoid
  B = 0       outside
```

A solenoid concentrates B field inside, shields outside. Transformer cores,
MRI machines, particle accelerators all exploit this.

### Example 3: Toroid

Donut-shaped solenoid, N total turns. Choose a circular Amperian loop
of radius r inside the doroid:

```
         μ₀NI
  B  = ────────    (inside the toroid, varies with r)
          2πr

  B = 0  outside the toroid entirely
```

All flux is confined inside the donut — used in transformer cores to
prevent stray fields.

---

## No Magnetic Monopoles: ∇·B = 0

In electrostatics: ∇·E = ρ/ε₀. Charges are sources and sinks of E field lines.

In magnetostatics: **∇·B = 0 always**. Magnetic field lines have no sources or
sinks. Every B field line that enters any closed surface must also exit.

```
  ∮∮_S B·dA = 0    for any closed surface S
```

This means B field lines always close on themselves — they form closed loops.
They never start or stop anywhere. (Compare E lines: start on + charge, end on -.)

```
  ELECTRIC FIELD LINES:      MAGNETIC FIELD LINES:
  start and end on charges   always closed loops

     +          -              N ↑ S
     ·──────────·              │ │ │
  →→→→→→→→→→→→→→→          ─────────
                              ↑     ↑
                             closed loops through
                             magnet and around outside
```

**Physical consequence**: You cannot isolate a magnetic north pole from a
south pole. Cut a bar magnet in half — you get two smaller bar magnets,
each with both poles. Magnetic monopoles have been searched for extensively
(Dirac showed they would quantize electric charge if they existed) and never found.

---

## The Vector Potential A

Since ∇·B = 0 everywhere, the identity ∇·(∇×A) = 0 (from module 01)
guarantees we can write:

```
  B = ∇×A        A is the magnetic vector potential (units: T·m = Wb/m)
```

Analogous to V for electrostatics, but A is a vector field, not scalar.

**Why A is useful**:
- Simpler in many calculations (A obeys Poisson's equation)
- Essential in quantum mechanics — the Aharonov-Bohm effect shows a particle
  can be affected by A even where B = 0 (no classical analog)
- The full relativistic formulation of E&M unifies V and A into a 4-vector (Aᵘ)

## Engineering Bridge: The Vector Potential as Gauge Connection

```
MAGNETOSTATICS CONCEPT              DIFFERENTIAL GEOMETRY EQUIVALENT
──────────────────────────────────────────────────────────────────────────────
Vector potential A                  Connection 1-form on a U(1) principal bundle
  B = ∇×A                            Curvature F = dA (the field strength 2-form)
  Gauge freedom A → A + ∇Λ           Gauge transformation: change of trivialization
  B unchanged (∇×∇Λ = 0)             Curvature is gauge-invariant

Aharonov-Bohm phase                Holonomy of the connection
  ∮A·dl = Φ (enclosed flux)          Phase = exp(i e/ℏ ∮A·dl)
  Measurable even where B = 0        Observable = holonomy, not connection itself

Magnetic flux quantization          Chern number (first Chern class)
  Φ₀ = h/2e in superconductors       Topological invariant of the bundle
                                      Integer-valued → quantized
```

This is the prototype for all gauge theories in modern physics. Replace U(1) with SU(2) → the weak force; with SU(3) → the strong force. The vector potential A is not a computational convenience — it is the fundamental dynamical variable (the connection), and B is the derived quantity (the curvature). The Aharonov-Bohm effect proves this: electrons detect A even where B = 0, because the phase they accumulate is the holonomy of the connection around a closed loop.

**Gauge freedom**: B = ∇×A is unchanged if you replace A → A + ∇Λ for any
scalar Λ (since ∇×(∇Λ) = 0). This is gauge freedom — physically equivalent
descriptions with different A.

**Coulomb gauge**: Choose ∇·A = 0. Then ∇×B = ∇×(∇×A) = ∇(∇·A) - ∇²A = -∇²A

Combined with ∇×B = μ₀J:

```
  ∇²A = -μ₀J    (vector Poisson equation — one component at a time)
```

Same structure as ∇²V = -ρ/ε₀. Solve component by component.

---

## Force on Current-Carrying Conductors

From F = qv×B for individual charges, the force on a current-carrying wire:

```
  dF = I dl × B       (force on current element I dl in field B)

  For straight wire of length L in uniform B:
  F = I L × B         (L is vector along wire in direction of current)
```

**Parallel wires**: Two parallel wires carrying currents I₁ and I₂ separated
by distance d. Wire 1 creates B at wire 2; wire 2 feels force in that B.

```
  Force per unit length:

       μ₀ I₁I₂
  f = ─────────
         2πd

  Same direction currents:  attractive force
  Opposite direction:       repulsive force
```

This is the original definition of the ampere — 1 A is the current in each
of two parallel wires 1 m apart that produces 2×10⁻⁷ N/m of force between them.

---

**Condensed matter connection**: The classical Hall effect (Lorentz force v x B causes charge separation, producing a transverse voltage V_H = IB/nqt) is the standard method for measuring carrier density n and sign in semiconductors. The quantum Hall effect (integer: von Klitzing 1980, Nobel 1985; fractional: Tsui-Stormer 1982, Nobel 1998) reveals that Hall conductance is quantized in units of e^2/h — a topological invariant (Chern number) of the electron band structure. This connects directly to the gauge theory bridge above: the quantized Hall conductance IS the first Chern number of the Berry connection on the magnetic Brillouin zone.

## Magnetic Dipoles

The simplest magnetic source — a current loop:

```
  Area A, current I, normal n̂:

  Magnetic dipole moment:  m = IA n̂    (units: A·m²)
```

Far from the loop, the field looks like an electric dipole — same angular
structure but for B instead of E. The Earth, bar magnets, and atoms are all
magnetic dipoles.

**Torque on a dipole in a field**:

```
  τ = m × B
```

The dipole tends to align with B (τ = 0 when m ∥ B). This is:
- How a compass needle aligns with Earth's B field
- The operating principle of electric motors (torque on current loop in B field)
- The basis of NMR/MRI (nuclear magnetic moments precessing in B)

**Energy of a dipole in a field**:

```
  U = -m·B

  Minimum energy when m aligns with B (stable equilibrium)
  Maximum energy when m anti-aligns with B (unstable)
```

---

## Electrostatics vs Magnetostatics — Full Comparison

```
+──────────────────────────────────────────────────────────────────────+
|                    SIDE BY SIDE COMPARISON                           |
+──────────────────────────────────────────────────────────────────────+
|                   ELECTROSTATICS    |    MAGNETOSTATICS              |
+──────────────────────────────────────────────────────────────────────+
| Source                ρ (charge)    |    J (current)                 |
| Constant              1/ε₀          |    μ₀                          |
| Field                 E             |    B                           |
| Divergence law     ∇·E = ρ/ε₀      |    ∇·B = 0                    |
| Curl law           ∇×E = 0          |    ∇×B = μ₀J                  |
| Integral (div)   ∮∮E·dA = Q/ε₀     |    ∮∮B·dA = 0                 |
| Integral (curl)  ∮E·dl = 0          |    ∮B·dl = μ₀I_enc            |
| Potential         V scalar           |    A vector                   |
| Field from pot    E = -∇V           |    B = ∇×A                    |
| Poisson eq        ∇²V = -ρ/ε₀      |    ∇²A = -μ₀J                 |
| Point source      Coulomb 1/r²       |    Biot-Savart (messier)      |
| Symmetric tool    Gauss's law        |    Ampere's law               |
| Force on charge   F = qE             |    F = qv×B                   |
| Does work?        Yes                |    No (F⊥v)                   |
| Monopoles?        Yes (charges)      |    No                         |
| Field lines       start/end          |    closed loops               |
+──────────────────────────────────────────────────────────────────────+
```

---

## Decision Cheat Sheet

| Situation | Tool |
|-----------|------|
| B from arbitrary current | Biot-Savart integral |
| B from symmetric current | Ampere's law |
| B from straight infinite wire | B = μ₀I/2πr |
| B inside infinite solenoid | B = μ₀nI |
| Force on charge in B | F = qv×B |
| Force on wire in B | F = IL×B |
| Torque on current loop in B | τ = m×B |
| B field lines start/stop? | Never — ∇·B = 0 always |
| Does B do work? | Never — F always ⊥ v |
| Can write B = ∇×A? | Always — because ∇·B = 0 |

---

## Common Confusion Points

**Magnetic force does no work — but motors do work.**
F = qv×B is always perpendicular to v, so the magnetic force does zero work
on the charge itself. But in a motor, the wire is constrained — the force on
moving charges is transmitted to the wire lattice as mechanical force. The
work comes from the EMF source driving the current, not from B directly.

**Right-hand rule for cross products — keep one version and use it consistently.**
For v×B: point fingers along v, curl toward B, thumb gives direction.
For Ampere's law (current direction → B direction): thumb along current,
fingers curl in direction of B. These are the same rule, applied differently.

**Ampere's law in integral form depends on what surface you use.**
I_enc is the current threading through any surface bounded by the loop.
For a simple wire, a flat disk and a bulging surface give the same I_enc.
This stops being true in dynamic situations (capacitor charging) — that
inconsistency is exactly what forced Maxwell to add the displacement current
term. Details in module 03-MAXWELL.md.

**B = 0 outside a solenoid is approximate.**
For an infinite solenoid, B = 0 outside exactly. For a finite solenoid,
there is fringe field outside the ends. "Infinite solenoid" means length >> radius.

**A is not unique — gauge choice matters for calculation, not for physics.**
B = ∇×A is gauge-invariant. The choice of gauge (Coulomb, Lorenz, etc.)
affects the form of A but not the physical B field. In QM, the gauge choice
can affect the form of the wavefunction — though all observables remain gauge-invariant.

**The 4/π factor in μ₀.**
μ₀ = 4π × 10⁻⁷ T·m/A is by definition in SI (prior to 2019 redefinition).
The 4π appears because Ampere's law is written without a 4π (unlike Coulomb's
law which has 1/4πε₀). Consistent convention: the 4π lives in ε₀/μ₀
or it lives in the law — not both. SI puts it in μ₀, Gaussian units
distribute it differently.
