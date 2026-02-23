# Electromagnetic Waves — Propagation, Spectrum, and Interaction with Matter

## The Big Picture

Module 03 derived the wave equation. This module unpacks what that equation
means — the full structure of EM waves, how they carry energy and momentum,
how they interact with matter, and why different frequencies behave so differently.

```
+------------------------------------------------------------------------+
|                     EM WAVE LANDSCAPE                                  |
|                                                                        |
|  WAVE PARAMETERS          WAVE STRUCTURE          INTERACTIONS         |
|  ───────────────          ──────────────          ────────────         |
|  λ, f, k, ω, c            E ⊥ B ⊥ k              Reflection           |
|  c = λf = ω/k             |E| = c|B|              Refraction           |
|  in matter: v = c/n       Transverse              Absorption           |
|                           Polarization            Diffraction          |
|                                                   Skin depth           |
|                                                                        |
|  ENERGY                   SPECTRUM                                     |
|  ──────                   ────────                                     |
|  u = ε₀E² (avg)           Radio → Microwave → IR → Visible            |
|  S = E×B/μ₀               → UV → X-ray → Gamma                        |
|  I = cε₀E₀²/2             all same wave, different f                  |
+------------------------------------------------------------------------+
```

---

## Wave Parameters

A wave is characterized by how it repeats in space and time:

```
  SPATIAL:                       TEMPORAL:
  ────────                       ─────────
  λ = wavelength (m)             T = period (s)
      distance between peaks         time between peaks

  k = 2π/λ  wave number (rad/m)  f = 1/T  frequency (Hz)
      spatial frequency               temporal frequency

                                 ω = 2πf  angular frequency (rad/s)

  LINK:   c = λf = ω/k

  In vacuum:    ω = ck   (linear dispersion — all frequencies same speed)
  In matter:    ω = (c/n)k   where n = index of refraction
```

**Phase velocity**: speed at which a phase front (constant phase surface) moves:

```
  v_phase = ω/k = c/n
```

**Group velocity**: speed at which a wave packet (envelope of a modulated wave)
moves — the speed of information and energy:

```
  v_group = dω/dk
```

In vacuum: v_group = v_phase = c (non-dispersive).
In matter: v_group ≠ v_phase generally (dispersive medium). This is why a
prism separates colors — different frequencies have different phase velocities,
but the signal (group velocity) moves at a different speed still.

From 6.003: this is exactly the group delay concept in signals and systems —
the same mathematics, different physical domain.

---

## Plane Wave Solution — Full Structure

A **plane wave** has planar wavefronts — constant phase everywhere on a plane
perpendicular to the direction of travel. The general solution:

```
  E(r,t) = E₀ cos(k·r - ωt + φ) n̂_E

  where:
    k = k k̂  (wave vector, pointing in direction of travel)
    k = |k| = ω/c = 2π/λ
    n̂_E = polarization direction (unit vector for E)
    φ = initial phase
```

**Constraints from Maxwell's equations on the plane wave**:

From ∇·E = 0 (in vacuum):  k·E₀ = 0  → **E is perpendicular to k**

From ∇·B = 0: k·B₀ = 0  → **B is perpendicular to k**

From ∇×E = -∂B/∂t:

```
  B = (1/c)(k̂ × E)

  B is perpendicular to both k̂ and E.
  |B| = |E|/c
```

The full geometric constraint:

```
  k̂ (direction of travel)
   │
   │────────────→  E
   │
   └──────────→  B = k̂ × E / c

  E, B, k̂ form a right-handed orthogonal triad.
  Like x̂, ŷ, ẑ but for the wave.
```

This is a **transverse wave** — fields oscillate perpendicular to propagation,
unlike sound (longitudinal). EM waves cannot be longitudinal because ∇·E = 0
in vacuum forbids a field component along the propagation direction.

---

## Polarization

Polarization describes how the E field direction behaves over time.

### Linear Polarization

E oscillates along a fixed direction:

```
  E(z,t) = E₀ cos(kz - ωt) x̂     ← always along x̂

  Time snapshots:
  t=0:    →  →  →  →  →
  t=T/4:  ·  ·  ·  ·  ·    (zero crossing)
  t=T/2:  ←  ←  ←  ←  ←
```

Two orthogonal linear polarizations are independent solutions — any
linearly polarized wave can be decomposed into x̂ and ŷ components.

### Circular Polarization

Two equal-amplitude, 90°-phase-shifted orthogonal components:

```
  E(z,t) = E₀[cos(kz-ωt) x̂ ± sin(kz-ωt) ŷ]

  (+) = left circular polarization (LCP)
  (-) = right circular polarization (RCP)

  The E vector rotates as the wave passes — traces a circle.
```

Looking toward the source: LCP rotates counterclockwise, RCP clockwise.

Circular polarization matters in:
- Optics: chiral molecules rotate the polarization plane (optical activity)
- Antennas: circularly polarized antennas receive from any orientation
- QM: photons carry angular momentum ±ℏ — LCP vs RCP

### Elliptical Polarization

The general case: two components with different amplitudes and arbitrary phase.
E traces an ellipse. Linear and circular are special cases.

```
  POLARIZATION HIERARCHY:

  Elliptical (general)
     ├── Linear (equal phase, any amplitude ratio)
     └── Circular (90° phase, equal amplitude)
```

---

## Energy Transport

### Intensity

Time-averaged Poynting vector magnitude for a plane wave:

```
        cε₀ E₀²      E₀²
  I  = ─────────  =  ──────    (W/m²)
            2        2μ₀c
```

I is the power per unit area crossing a surface perpendicular to propagation.

**Inverse square law**: for a point source radiating total power P:

```
         P
  I  = ──────    at distance r
        4πr²
```

Same 1/r² geometry as Coulomb's law — fixed power spreads over sphere of area 4πr².

### Radiation Pressure

EM waves carry momentum. Pressure on a surface:

```
  P = I/c   (absorbed surface)
  P = 2I/c  (perfectly reflected surface)
```

Tiny but real. Solar sails work on this principle. Radiation pressure from
the Sun prevents molecular clouds from collapsing too quickly.

### Larmor Radiation

**Any accelerating charge radiates EM waves.** Power radiated:

```
        q²a²
  P  = ──────────    (Larmor formula)
        6πε₀c³
```

Consequences:
- Electrons orbiting nuclei should spiral inward (they radiate) — classical
  physics predicts atoms collapse in ~10⁻¹¹ s. Quantum mechanics resolves this.
- Antennas work by accelerating charges in a conductor
- Synchrotron radiation: relativistic electrons in circular paths radiate
  brilliantly (X-ray sources at accelerator facilities)
- Bremsstrahlung: deceleration radiation when electrons are stopped in matter

---

## The Electromagnetic Spectrum

Same physics, enormously different behavior due to frequency:

```
+─────────────────────────────────────────────────────────────────────+
│  REGION       FREQUENCY          WAVELENGTH    APPLICATIONS         │
+─────────────────────────────────────────────────────────────────────+
│  Radio        3 Hz – 300 MHz     1 mm – 100 km AM/FM, TV, cell      │
│  Microwave    300 MHz – 300 GHz  1 mm – 1 m    WiFi, radar, μwave  │
│  Infrared     300 GHz – 430 THz  700 nm – 1 mm heat, night vision  │
│  Visible      430 – 750 THz      400 – 700 nm  human vision         │
│               ├─ violet  750 THz    400 nm                          │
│               ├─ blue    670 THz    450 nm                          │
│               ├─ green   545 THz    550 nm                          │
│               ├─ yellow  510 THz    590 nm                          │
│               └─ red     430 THz    700 nm                          │
│  UV           750 THz – 30 PHz   10 – 400 nm   sunburn, sterilize  │
│  X-ray        30 PHz – 30 EHz    0.01 – 10 nm  medical imaging     │
│  Gamma        > 30 EHz           < 0.01 nm     nuclear, PET scans  │
+─────────────────────────────────────────────────────────────────────+

  All travel at c in vacuum. All described by same Maxwell's equations.
  Difference: frequency determines energy per photon (E = hf — quantum).
```

**Why different behavior?** The interaction of EM radiation with matter depends
on what the radiation frequency matches:
- Radio: matches antenna resonance (metal rods), reflects from ionosphere
- Microwave: matches molecular rotation/water absorption
- IR: matches molecular vibration (heat)
- Visible: matches electron transitions in outer shells
- UV/X-ray: matches inner electron transitions, ionizes atoms
- Gamma: matches nuclear transitions, penetrates deeply

---

## Reflection and Refraction

At the interface between two media with different indices n₁ and n₂:

**Snell's law**:

```
  n₁ sin θ₁ = n₂ sin θ₂

  θ₁ = angle of incidence   (from normal)
  θ₂ = angle of refraction  (from normal)
```

Derived from boundary conditions on Maxwell's equations — the tangential
component of k must be continuous across the interface.

**Total internal reflection**: when going from dense to sparse medium (n₁ > n₂):

```
  Critical angle:  sin θ_c = n₂/n₁

  θ₁ > θ_c  →  no transmitted wave, total reflection
```

This is the operating principle of **optical fibers** — light is trapped by
total internal reflection in a high-index glass core surrounded by lower-index
cladding. The internet runs on this.

**Fresnel equations**: give amplitudes of reflected and transmitted waves as
a function of angle and polarization. At Brewster's angle (tan θ_B = n₂/n₁),
the reflected wave is completely polarized — polarized sunglasses exploit this.

---

## EM Waves in Conductors — Skin Depth

In a conductor with conductivity σ, free charges respond to E by flowing —
current J = σE dissipates energy, attenuating the wave.

The wave equation in a conductor becomes:

```
  ∇²E = μσ ∂E/∂t + με ∂²E/∂t²
         ────────   ─────────
         dissipation  wave term
```

At low frequency: dissipation dominates (quasi-static).
At high frequency: wave term dominates (radiative).

The plane wave solution in a conductor is exponentially damped:

```
  E(z,t) = E₀ e^(-z/δ) cos(z/δ - ωt)

  where:        2
         δ = √──────    ← SKIN DEPTH
               ωμσ

  δ = depth at which amplitude falls to 1/e ≈ 37% of surface value
```

**Physical meaning**: EM waves cannot penetrate deeply into good conductors.
The fields and currents are confined to a thin layer at the surface of
thickness δ. High frequency → thinner skin depth.

```
  SKIN DEPTH FOR COPPER (σ = 5.8 × 10⁷ S/m):

  60 Hz (power line):    δ ≈ 8.5 mm
  10 kHz (audio):        δ ≈ 0.66 mm
  1 MHz (AM radio):      δ ≈ 0.066 mm
  1 GHz (microwave):     δ ≈ 2.1 μm
  10 GHz (radar):        δ ≈ 0.66 μm
```

**Consequences**:
- RF shielding: conductors block EM waves above a certain frequency
- Coaxial cables: signal is at skin depth; center conductor radius must be >> δ
- Transformer core losses: eddy currents confined to skin depth, laminating
  the core (thin sheets) reduces losses
- **Liquid metals** (modules 06-07): skin depth governs how deep EM fields
  penetrate into liquid metal — determines the coupling between EM and fluid

For liquid mercury at 60 Hz: δ ≈ 65 mm. For a large MHD device, the field
penetrates throughout the metal. At higher frequencies, fields are confined
to the surface — completely different MHD dynamics.

---

## Standing Waves and Cavities

Two counterpropagating waves superpose to form a standing wave:

```
  E₁ = E₀ cos(kz - ωt)   (forward)
  E₂ = E₀ cos(kz + ωt)   (backward)

  E₁ + E₂ = 2E₀ cos(kz) cos(ωt)   ← standing wave
             ──────────  ─────────
             space part  time part
             (doesn't move)
```

**Nodes**: positions where E = 0 always (cos(kz) = 0)
**Antinodes**: positions of maximum |E| (cos(kz) = ±1)

**Resonant cavities**: standing waves in a box. Only certain frequencies
(modes) fit — those where the boundary conditions (E tangential = 0 at
conducting walls) are satisfied. Cavity modes are the EM analog of standing
waves on a string.

Applications:
- Microwave ovens: food in a resonant cavity at 2.45 GHz
- Lasers: optical cavity between two mirrors selects one mode
- Accelerator cavities: resonant RF cavities accelerate particles

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| Wave speed in vacuum | c = 1/√(μ₀ε₀) = 3×10⁸ m/s |
| Wave speed in medium | v = c/n, n = √(εᵣμᵣ) |
| E and B relationship | B = k̂×E/c, E⊥B⊥k̂ |
| Energy flow direction | S = E×B/μ₀ (Poynting) |
| Intensity of plane wave | I = cε₀E₀²/2 |
| Penetration into conductor | δ = √(2/ωμσ) (skin depth) |
| Reflection/refraction angles | n₁ sin θ₁ = n₂ sin θ₂ (Snell) |
| Total internal reflection | θ > θ_c = arcsin(n₂/n₁) |
| Power radiated by accelerating charge | P = q²a²/6πε₀c³ |
| Does frequency change at interface? | Never — only λ and v change |

---

## Common Confusion Points

**Frequency never changes at an interface — wavelength does.**
When a wave crosses from one medium to another, f stays constant (boundary
condition), but λ = v/f changes because v = c/n changes. This is why light
bends — same frequency, different wavelength, wavefronts must stay continuous.

**The E and B fields are in phase in a traveling wave.**
In a standing wave, E and B are 90° out of phase in time (when E is maximum,
B is zero and vice versa). In a propagating wave, they're in phase.
These behave very differently.

**Skin depth depends on frequency — RF and DC behave completely differently.**
A thick copper rod carries DC uniformly across its cross section.
At 1 GHz, the same rod carries current only in the outer 2 μm.
The effective resistance at high frequency is much higher than DC resistance.
This is why microwave conductors are made differently from power conductors.

**Light in a medium slows down — but information never exceeds c.**
Phase velocity v = c/n can be < c (normal dispersion) or even apparently
> c (anomalous dispersion near a resonance). Group velocity (signal speed)
never exceeds c. Seemingly superluminal phase velocity doesn't transmit
information faster than c.

**Polarization is defined by E, not B.**
Historically confusing but conventional. The polarization state is the
direction/behavior of E. B is determined by B = k̂×E/c — it's not independent.
When someone says "vertically polarized wave" they mean E is vertical.
