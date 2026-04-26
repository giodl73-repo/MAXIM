# Maxwell's Equations — The Unification of Electricity and Magnetism

## The Big Picture

James Clerk Maxwell, 1865. He took the experimental laws of electricity and
magnetism, found an internal inconsistency, fixed it with one term, and
discovered that light is an electromagnetic wave — from pure mathematics,
no optics required. One of the great moments in the history of science.

```
+------------------------------------------------------------------------+
|                    MAXWELL'S FOUR EQUATIONS                            |
|                    (differential form, in vacuum)                      |
|                                                                        |
|   ∇·E  = ρ/ε₀           Gauss — charges create E field divergence      |
|   ∇·B  = 0               No monopoles — B has no sources               |
|   ∇×E  = -∂B/∂t          Faraday — changing B creates curling E        |
|   ∇×B  = μ₀J + μ₀ε₀∂E/∂t  Ampere-Maxwell — current + changing E        |
|                                               creates curling B        |
|                                                                        |
|   Four equations. Two fields (E, B). All of classical electrodynamics. |
+------------------------------------------------------------------------+
```

The payoff — in vacuum, no charges, no currents (ρ = 0, J = 0):

```
  ∇²E = μ₀ε₀ ∂²E/∂t²        ← wave equation for E
  ∇²B = μ₀ε₀ ∂²B/∂t²        ← wave equation for B

  Wave speed:  c = 1/√(μ₀ε₀) = 2.998 × 10⁸ m/s

  That is the speed of light. Light is an electromagnetic wave.
```

Maxwell computed c from two constants measured in electrical experiments —
ε₀ from Coulomb's law, μ₀ from Ampere's law — with no reference to optics,
and got the speed of light exactly.

---

## The Problem Maxwell Solved

Before Maxwell, there were four experimental laws:

```
  ∇·E  = ρ/ε₀      Gauss (1835)
  ∇·B  = 0          Faraday (implicit)
  ∇×E  = -∂B/∂t     Faraday (1831)
  ∇×B  = μ₀J        Ampere (1826)  ← PROBLEM HERE
```

**The inconsistency in Ampere's law**: Take the divergence of ∇×B = μ₀J:

```
  ∇·(∇×B) = μ₀ ∇·J

  But ∇·(∇×anything) = 0 always  (from module 01)

  Therefore: ∇·J = 0 always?
```

But the continuity equation (charge conservation) says:

```
  ∂ρ/∂t + ∇·J = 0
```

So ∇·J = 0 only if ∂ρ/∂t = 0 — only for steady currents. The moment
charge density changes anywhere (a capacitor charging, for instance),
Ampere's law as written violates charge conservation. It cannot be right.

**Maxwell's fix**: Use Gauss's law ∇·E = ρ/ε₀ to rewrite the continuity equation:

```
  ∂ρ/∂t + ∇·J = 0

  ∂(ε₀ ∇·E)/∂t + ∇·J = 0

  ∇·(J + ε₀ ∂E/∂t) = 0
```

The quantity J + ε₀∂E/∂t is always divergence-free. Replace J with this
in Ampere's law:

```
  ∇×B = μ₀J + μ₀ε₀ ∂E/∂t
                   ─────────
                   displacement current
```

Now ∇·(∇×B) = μ₀∇·(J + ε₀∂E/∂t) = 0 ✓ — consistent with charge conservation.

**The displacement current** μ₀ε₀∂E/∂t: not a real current (no charges moving),
but a changing electric field that acts as a source of B exactly as current does.

```
  CAPACITOR CHARGING (the canonical example):

    I ──→  [  +  |  -  ]  ──→  I
            plate gap
           no charges cross
           but E builds up
           between plates

  Real current I flows into plates.
  No current crosses the gap.
  But ∂E/∂t in the gap acts exactly like a current — B circles the gap
  exactly as if current were flowing through it.

  Without displacement current: B is different on two sides of the gap. ✗
  With displacement current: B is consistent everywhere.            ✓
```

---

## The Four Equations — Each One

### Equation 1: ∇·E = ρ/ε₀ (Gauss's Law for E)

```
  Differential: ∇·E = ρ/ε₀
  Integral:     ∮∮ E·dA = Q_enc/ε₀
```

Electric field lines start on positive charges, end on negative charges.
In empty space (ρ = 0): ∇·E = 0 — no sources or sinks, field lines
pass through without starting or stopping.

**Reads as**: The divergence of E at a point equals the charge density there.
Charge is the source of E.

### Equation 2: ∇·B = 0 (Gauss's Law for B)

```
  Differential: ∇·B = 0
  Integral:     ∮∮ B·dA = 0
```

Magnetic field lines have no sources or sinks, ever. They always form
closed loops. No magnetic monopoles.

**Reads as**: B has zero divergence everywhere. Whatever B you have, its
field lines close on themselves.

**The asymmetry** with Equation 1 is not fundamental — it reflects the absence
(observed, not required) of magnetic monopoles. If monopoles existed:
∇·B = μ₀ρ_m. The search continues; none found.

### Equation 3: ∇×E = -∂B/∂t (Faraday's Law)

```
  Differential: ∇×E = -∂B/∂t
  Integral:     ∮ E·dl = -dΦ_B/dt
```

A changing magnetic field creates a curling electric field. The negative
sign (Lenz's law) means the induced E opposes the change in B.

**Reads as**: If B changes at some point, E curls around that point.
The faster B changes, the stronger the induced E.

**In electrostatics**: ∂B/∂t = 0, so ∇×E = 0. E is conservative —
path-independent, derivable from potential V. In dynamics, ∇×E ≠ 0,
and E is no longer purely conservative. Voltage around a loop can be nonzero.

**Faraday's law is the generator equation.** Move a magnet (change Φ_B
through a loop), EMF appears, current flows. Every power plant on Earth.

### Equation 4: ∇×B = μ₀J + μ₀ε₀∂E/∂t (Ampere-Maxwell Law)

```
  Differential: ∇×B = μ₀J + μ₀ε₀∂E/∂t
  Integral:     ∮ B·dl = μ₀I_enc + μ₀ε₀ dΦ_E/dt
```

Two things create curling B:
- Real current J (Ampere's original law)
- Changing electric field ∂E/∂t (Maxwell's addition)

**Reads as**: Wherever current flows or E changes, B curls around it.

**The second term is the key to EM waves.** In vacuum, no current (J = 0).
Faraday says changing B creates E. Ampere-Maxwell says changing E creates B.
The fields sustain each other — propagating wave.

---

## Deriving the Wave Equation

In vacuum: ρ = 0, J = 0. The four equations become:

```
  ∇·E = 0         ∇·B = 0
  ∇×E = -∂B/∂t    ∇×B = μ₀ε₀ ∂E/∂t
```

Take the curl of Faraday's law:

```
  ∇×(∇×E) = -∂/∂t (∇×B)
```

Left side — use the vector identity ∇×(∇×F) = ∇(∇·F) - ∇²F:

```
  ∇(∇·E) - ∇²E = -∂/∂t (∇×B)
```

In vacuum ∇·E = 0, so first term vanishes:

```
  -∇²E = -∂/∂t (∇×B)
```

Substitute Ampere-Maxwell for ∇×B:

```
  -∇²E = -∂/∂t (μ₀ε₀ ∂E/∂t) = -μ₀ε₀ ∂²E/∂t²
```

Therefore:

```
  ┌────────────────────────────────────┐
  │                                    │
  │   ∇²E  =  μ₀ε₀ ∂²E/∂t²           │
  │                                    │
  │   ∇²B  =  μ₀ε₀ ∂²B/∂t²           │
  │                                    │
  └────────────────────────────────────┘

  This is the wave equation: ∇²f = (1/v²) ∂²f/∂t²
  with wave speed v = 1/√(μ₀ε₀)
```

Computing c from measured constants:

```
  μ₀ = 4π × 10⁻⁷   T·m/A
  ε₀ = 8.854 × 10⁻¹²  C²/(N·m²)

  c = 1/√(μ₀ε₀)
    = 1/√(4π × 10⁻⁷ × 8.854 × 10⁻¹²)
    = 2.998 × 10⁸  m/s

  Known speed of light (1849, Fizeau):  3.1 × 10⁸  m/s
```

Maxwell 1865: *"We can scarcely avoid the conclusion that light consists
in the transverse undulations of the same medium which is the cause of
electric and magnetic phenomena."*

---

## Structure of the EM Wave

The wave equation allows plane wave solutions. For a wave traveling in the +x direction:

```
  E(x,t) = E₀ ŷ cos(kx - ωt)     (E field oscillates in y-direction)
  B(x,t) = B₀ ẑ cos(kx - ωt)     (B field oscillates in z-direction)

  where:  k = 2π/λ  (wave number)
          ω = 2π f  (angular frequency)
          ω/k = c   (wave speed)
          E₀ = cB₀  (magnitudes related by c)
```

```
  ELECTROMAGNETIC WAVE (propagating in +x direction):

  direction of travel ──────────────────────────────→  x

       ↑E                    ↑E
       │     ╭───╮           │     ╭───╮
  ─────┼────╯     ╰──────────┼────╯     ╰───    E oscillates ±y
       │         ╰───╯       │         ╰───╯
                 ↓E                     ↓E

       ·B  ·B  ·B            ·B  ·B  ·B
  ─────────────────────────────────────────       B oscillates ±z (into/out of page)
       ×B  ×B  ×B            ×B  ×B  ×B

  E ⊥ B ⊥ direction of travel — transverse wave
```

Key properties:
- E and B are perpendicular to each other and to the direction of travel
- They are in phase (peaks and zeros coincide)
- E₀/B₀ = c always
- The wave carries energy and momentum

---

## Energy and the Poynting Vector

The energy density stored in the EM field:

```
        ε₀         B²
  u  = ─── E²  +  ────     (electric + magnetic energy density, J/m³)
         2          2μ₀
```

For a plane wave: electric and magnetic energy densities are equal.

**Poynting vector** — energy flux (power per unit area, W/m²):

```
         1
  S  =  ─── (E × B)
         μ₀

  Direction of S = direction of energy flow
  |S| = intensity (power per unit area crossing a surface)
```

S points in the direction the wave travels — same direction as k.

**Poynting's theorem** — energy conservation for EM fields:

```
  ∂u/∂t  +  ∇·S  =  -J·E

  Rate of change     Energy flux    Work done on
  of field energy  + out of region = charges (power
  density            (divergence)    delivered to matter)
```

Energy flows out of the field (∇·S > 0) when work is done on charges.
Energy flows into the field (∇·S < 0) when charges do work on the field
(charging a capacitor, for instance).

---

## Maxwell's Equations in Matter

In free space: E and B are the fields. In matter, charges and currents
inside materials respond to fields and modify them.

**Polarization** P: bound charge dipoles in a dielectric align with E.
**Magnetization** M: magnetic dipoles in a material align with B.

Define new fields that absorb the material response:

```
  D = ε₀E + P = εE         (electric displacement field, C/m²)
  H = B/μ₀ - M = B/μ       (H field, A/m)

  ε = ε₀εᵣ  (permittivity — εᵣ is relative permittivity / dielectric constant)
  μ = μ₀μᵣ  (permeability — μᵣ is relative permeability)
```

Maxwell's equations in matter (only free charges and currents on right side):

```
  ∇·D  = ρ_free              ∇·B  = 0
  ∇×E  = -∂B/∂t              ∇×H  = J_free + ∂D/∂t
```

Wave speed in matter: v = 1/√(εμ) = c/√(εᵣμᵣ) = c/n

Where n = √(εᵣμᵣ) is the **index of refraction**. Light slows down in
glass (n ≈ 1.5) because of the interaction between the EM wave and the
bound electrons in the material.

---

## The Symmetry Maxwell Almost Completed

The four equations have a structural asymmetry — Equation 1 has ρ on the
right, Equation 2 has 0. If magnetic monopoles existed:

```
  ACTUAL MAXWELL:           IF MONOPOLES EXISTED:
  ∇·E  = ρ_e/ε₀             ∇·E  = ρ_e/ε₀
  ∇·B  = 0                   ∇·B  = μ₀ρ_m        ← symmetric
  ∇×E  = -∂B/∂t              ∇×E  = -μ₀J_m - ∂B/∂t  ← symmetric
  ∇×B  = μ₀J_e + μ₀ε₀∂E/∂t  ∇×B  = μ₀J_e + μ₀ε₀∂E/∂t
```

The equations would be fully symmetric under exchange of E and B
(with appropriate sign and constant changes) — electromagnetic duality.
Dirac showed in 1931 that if a single magnetic monopole exists anywhere
in the universe, all electric charges must be quantized (integer multiples
of e). This is why the quantization of charge is considered strong indirect
evidence that monopoles either exist or that charge quantization has a
different origin.

---

## Engineering Bridge: Maxwell as U(1) Gauge Theory

```
MAXWELL'S EQUATIONS                 GAUGE THEORY LANGUAGE
──────────────────────────────────────────────────────────────────────────────
4-potential Aμ = (V/c, A)          Connection on U(1) principal bundle
  Gauge: Aμ → Aμ + ∂μΛ              Gauge transformation (change of section)

Field strength Fμν = ∂μAν - ∂νAμ   Curvature 2-form F = dA
  F₀ᵢ = Eᵢ/c, Fᵢⱼ = εᵢⱼₖBₖ        Encodes both E and B in one object

∂νFμν = μ₀Jμ                       Equations of motion (Yang-Mills for U(1))
  Source equation: charges/currents    Extremize the action S = ∫(-1/4)FμνFμν

∂[λFμν] = 0                        Bianchi identity (automatic from F = dA)
  Homogeneous equations               No magnetic monopoles = dF = d²A = 0
  (∇·B=0 and Faraday's law)           A topological identity, not dynamics

U(1) → SU(2): weak force           Yang-Mills: Fμν = ∂μAν - ∂νAμ + g[Aμ,Aν]
U(1) → SU(3): strong force         Non-abelian: gauge fields self-interact
U(1) × SU(2) × SU(3)              The Standard Model of particle physics
```

Maxwell's equations are the simplest Yang-Mills theory: the gauge group U(1) is abelian, so the commutator [A,A] vanishes and the equations are linear. All the complexity of the Standard Model (asymptotic freedom, confinement, spontaneous symmetry breaking) comes from replacing U(1) with non-abelian groups where [A,A] is nonzero.

## Special Relativity Lives Here

Maxwell's equations are already relativistically correct. They do not need
modification for special relativity — they were the clue that led Einstein to it.

The problem: in 1905 the equations predicted EM waves travel at c, with no
dependence on the observer's motion. Newtonian mechanics said speeds add
(if you run at speed v toward a wave moving at c, you'd see it at c+v).
Contradiction.

Einstein's resolution: the equations are right. Mechanics needed fixing.
Special relativity preserves Maxwell's equations exactly.

In the relativistic formulation:
- E and B are not separate fields — they are components of a single
  antisymmetric **field strength tensor** Fᵘᵛ
- V and A combine into a 4-vector Aᵘ = (V/c, A)
- All four Maxwell equations become two tensor equations:
  ∂_ν Fᵘᵛ = μ₀ Jᵘ  and  ∂_[λ Fᵘᵛ] = 0
- Lorentz transformations mix E and B: a pure E field in one frame
  has a B component in a moving frame, and vice versa

---

**Beyond Maxwell**: Classical E&M breaks down at quantum scales and extreme field strengths. QED (quantum electrodynamics) replaces Maxwell at short distances — key phenomena include vacuum polarization (virtual e+e- pairs screen charges), photon-photon scattering (light-by-light, first observed at LHC 2017), and the Lamb shift (radiative correction to hydrogen energy levels, confirmed to 12 decimal places). See `08-QUANTUM-BRIDGE.md` and `09-ZERO-POINT-ENERGY.md`. Separately, EM waves carry information: Shannon channel capacity C = B log2(1 + S/N) is set by bandwidth B and signal-to-noise ratio S/N, both grounded in the wave physics of this module.

## Decision Cheat Sheet

| Situation | Equation to use |
|-----------|----------------|
| Source of E field lines | ∇·E = ρ/ε₀ (Gauss) |
| Do B field lines close? | Always — ∇·B = 0 |
| Changing B → what field? | Curling E — Faraday |
| Current or changing E → what? | Curling B — Ampere-Maxwell |
| Wave in vacuum | ∇²E = μ₀ε₀∂²E/∂t², c = 1/√(μ₀ε₀) |
| Energy flow direction | S = E×B/μ₀ (Poynting vector) |
| Wave speed in material | v = c/n, n = √(εᵣμᵣ) |
| Are Maxwell's equations relativistic? | Yes — already exact |

---

## Common Confusion Points

**The displacement current is not a current.**
μ₀ε₀∂E/∂t has units of current density (A/m²) and acts as a source of B,
but no charges move. It is a changing E field. Maxwell called it "displacement
current" by analogy; the name stuck. Don't picture charges oscillating in vacuum.

**E and B in a wave are in phase, not 90° out of phase.**
A common error from the analogy with LC circuits (where V and I are 90° out
of phase). In a propagating EM wave, E and B peaks coincide in space and time.

**The wave equation requires BOTH Faraday AND Ampere-Maxwell.**
The derivation uses curl of Faraday, then substitutes Ampere-Maxwell.
Remove either term, no wave. The displacement current term is what completes
the loop: changing B → E → changing E → B → changing B → ...

**In matter, use D and H on the left side of Gauss/Ampere.**
∇·D = ρ_free (not ρ_total). The bound charge inside dielectrics is absorbed
into D. ∇·E = ρ_total includes bound charge. They're both correct — different
ways of accounting for the same physics.

**Maxwell's equations are linear — superposition holds exactly.**
If (E₁, B₁) and (E₂, B₂) are both solutions, so is any linear combination.
This is why you can have two radio waves pass through each other without
interaction. Nonlinearity appears only in quantum electrodynamics (photon-photon
scattering) — negligibly small at everyday field strengths.
