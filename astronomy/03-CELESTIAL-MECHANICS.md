# Celestial Mechanics
## Two-Body Problem, Orbital Elements, Perturbations, Resonances, Tidal Effects

---

## 1. The Full Map

```
  CELESTIAL MECHANICS HIERARCHY

  ┌──────────────────────────────────────────────────────────────────────────┐
  │  TWO-BODY PROBLEM (exact analytic solution)                             │
  │    Reduction to 1D via conservation laws                                │
  │    Conic sections: ellipse / parabola / hyperbola                       │
  │    Kepler's laws as corollaries; vis-viva equation                      │
  └───────────────────────┬──────────────────────────────────────────────────┘
                          │ add a third body
                          ▼
  ┌──────────────────────────────────────────────────────────────────────────┐
  │  THREE-BODY PROBLEM (no general analytic solution — Poincaré 1887)      │
  │    Restricted case → Jacobi integral (1 conserved quantity)             │
  │    Hill sphere, Lagrange points L1–L5                                   │
  └───────────────────────┬──────────────────────────────────────────────────┘
                          │ add n bodies, small perturbations
                          ▼
  ┌──────────────────────────────────────────────────────────────────────────┐
  │  PERTURBATION THEORY                                                    │
  │    Lagrange planetary equations (elements evolve under perturbations)   │
  │    Secular vs periodic effects; J₂ nodal regression; lunisolar forcing  │
  └───────────────────────┬──────────────────────────────────────────────────┘
                          │ special frequency relationships
                          ▼
  ┌──────────────────────────────────────────────────────────────────────────┐
  │  RESONANCES                                                             │
  │    Mean motion resonances (MMR) — Laplace, Kirkwood, Trojans, Plutinos  │
  │    Secular resonances — precession rate matching                        │
  └───────────────────────┬──────────────────────────────────────────────────┘
                          │ add deformable bodies, dissipation
                          ▼
  ┌──────────────────────────────────────────────────────────────────────────┐
  │  TIDAL MECHANICS                                                        │
  │    Tidal forces, tidal locking, Roche limit, tidal heating              │
  └───────────────────────┬──────────────────────────────────────────────────┘
                          │ long time integration
                          ▼
  ┌──────────────────────────────────────────────────────────────────────────┐
  │  CHAOS AND STABILITY                                                    │
  │    Lyapunov exponents; solar system long-term fate; Mercury chaos       │
  └──────────────────────────────────────────────────────────────────────────┘
```

---

## 2. The Two-Body Problem — Exact Solution

### 2.1 Reduction to One-Body

Two masses m₁ and m₂ under mutual gravity:

```
  m₁ r̈₁ = +G m₁ m₂ / |r₁−r₂|² × r̂₁₂
  m₂ r̈₂ = −G m₁ m₂ / |r₁−r₂|² × r̂₁₂

  Center of mass:  R = (m₁r₁ + m₂r₂) / (m₁+m₂)   → R̈ = 0 (free particle, inertial)

  Relative vector: r = r₁ − r₂
  Reduced mass:    μ = m₁m₂/(m₁+m₂)

  Equation of motion reduces to:
  ┌─────────────────────────────────────────────┐
  │  μ r̈ = −G m₁ m₂ r / r³  =  −μ GM r / r³  │   M = m₁ + m₂
  └─────────────────────────────────────────────┘

  One particle, mass μ, in a central force field with GM = G(m₁+m₂).
  For M >> m (planet orbiting star): μ ≈ m, the star barely moves.
```

### 2.2 Two Conservation Laws → Planar Motion + Conic Sections

**Angular momentum** (central force → torque = 0):

```
  L = μ r × ṙ = constant (vector)
  → r and ṙ always in the same plane → motion is 2D

  |L| = μ r² θ̇ = μ √(GM p)    where p = a(1−e²) = semi-latus rectum
```

**Energy:**

```
  E = ½μv² − G m₁ m₂ / r = constant

  E < 0: bound orbit (ellipse)
  E = 0: escape with zero velocity at ∞ (parabola)
  E > 0: unbound (hyperbola)
  E = −Gm₁m₂/(2a)    ← only depends on semi-major axis a
```

**Orbit equation** (from L, E conservation → integrate):

```
  r(ν) = p / (1 + e cos ν)         p = L²/(μ² GM) = a(1−e²)

  ν = true anomaly (angle from periapsis)
  e = eccentricity = √(1 + 2EL²/(μ³ G²m₁²m₂²))

  ┌─────────────────────────────────────────────────────────┐
  │  e = 0: circle      e < 1: ellipse     r_min = a(1−e)  │
  │  e = 1: parabola    e > 1: hyperbola   r_max = a(1+e)  │
  └─────────────────────────────────────────────────────────┘
```

### 2.3 Kepler's Three Laws as Corollaries

```
  1st Law:  r = a(1−e²)/(1+e cos ν) — ellipse with focus at center of mass
            [from E, L conservation — conic section is the general solution]

  2nd Law:  dA/dt = |L|/(2μ) = constant — equal areas in equal times
            [from L = constant → angular momentum conservation]

  3rd Law:  T² = 4π² a³ / (GM)      T = period
            [from integrating dA/dt = |L|/(2μ) over full ellipse area πab]

  ALL THREE follow from Newton's inverse-square law + calculus.
  Kepler derived them empirically from Brahe's data.
```

### 2.4 Vis-Viva Equation

The single most useful formula in orbital mechanics:

```
  ┌──────────────────────────────────────────────────────┐
  │  v² = GM ( 2/r − 1/a )                              │
  └──────────────────────────────────────────────────────┘

  From E = ½μv² − GMμ/r = −GMμ/(2a), rearranged.

  Special cases:
  ─────────────────────────────────────────────────────────────
  Circular orbit (r = a):    v_c = √(GM/a)
  At periapsis (r = a(1−e)): v_peri = √(GM(1+e)/(a(1−e)))
  At apoapsis (r = a(1+e)):  v_apo  = √(GM(1−e)/(a(1+e)))
  Escape (a → ∞):            v_esc  = √(2GM/r) = v_c√2
  ─────────────────────────────────────────────────────────────
  Earth surface: v_c ≈ 7.91 km/s,  v_esc ≈ 11.19 km/s
  LEO (400 km):  v_c ≈ 7.67 km/s,  ISS orbital speed ≈ 7.66 km/s
```

---

## 3. Orbital Elements — Describing Any Orbit in 3D

Six numbers completely specify an orbit + position on it:

```
  THE CLASSICAL ORBITAL ELEMENTS

  ┌──────────────────────────────────────────────────────────────────────────┐
  │ SHAPE & SIZE                                                             │
  │   a  — semi-major axis        [distance]  Sets T via T²=4π²a³/(GM)     │
  │   e  — eccentricity           [0 to 1+]   Shape: 0=circle, 1=parabola  │
  ├──────────────────────────────────────────────────────────────────────────┤
  │ ORIENTATION OF ORBITAL PLANE                                             │
  │   i  — inclination            [0°–180°]   Tilt wrt reference plane      │
  │   Ω  — longitude of ascending node [0°–360°]  Where orbit crosses      │
  │         (RAAN)                              reference plane going north  │
  ├──────────────────────────────────────────────────────────────────────────┤
  │ ORIENTATION OF ELLIPSE IN PLANE                                          │
  │   ω  — argument of periapsis  [0°–360°]   Angle from node to periapsis  │
  ├──────────────────────────────────────────────────────────────────────────┤
  │ POSITION ON ORBIT                                                        │
  │   ν  — true anomaly           [0°–360°]   Current angle from periapsis  │
  │   (or M — mean anomaly, or E — eccentric anomaly, or t₀ — epoch)       │
  └──────────────────────────────────────────────────────────────────────────┘

  GEOMETRY:

        reference direction (vernal equinox ♈ for heliocentric)
              ↑
     ─────────┼──────────  reference plane (ecliptic or equatorial)
              │   ↗ ascending node (Ω measured here, along reference plane)
              │  /
              │ /  ← orbital plane tilted at i
              ●
              └── periapsis direction (ω measured from ascending node
                  within orbital plane, to the direction of periapsis)
```

### 3.1 Kepler's Equation — Time on the Orbit

Getting from time t to position ν requires solving transcendentally:

```
  Mean anomaly:      M = n(t − t₀)        n = 2π/T  (mean motion, rad/s)
  Kepler's equation: M = E − e sin E       E = eccentric anomaly
  True anomaly:      tan(ν/2) = √((1+e)/(1−e)) · tan(E/2)

  Kepler's equation has no closed-form inverse → Newton-Raphson in practice.

  Physical meaning of E:
  If you circumscribe the ellipse with a circle of radius a,
  E is the angle of the corresponding point on that circle.

         a
    ─────●─────── (circumscribed circle, radius a)
        / |
       /  |     ← E = eccentric anomaly
      ●───┼──── (point on ellipse at distance r from focus)
    focus │
          ν = true anomaly (from focus)
```

---

## 4. Three-Body Problem and Lagrange Points

### 4.1 Why Three Bodies Are Hard

```
  TWO-BODY:  10 conserved quantities (E, L×3, P×3, CM×3, t)
             → 12 degrees of freedom reduced to 2 (r and ν in orbital plane)
             → FULLY INTEGRABLE, analytic solution

  THREE-BODY: 10 conserved quantities vs 18 degrees of freedom
              → 8 degrees of freedom remain
              → NOT integrable in general
              Poincaré (1887): proved no algebraic first integrals beyond the 10 classical
              → demonstrated chaos; won the King Oscar II prize (with correction)
```

### 4.2 Restricted Three-Body Problem

Two massive bodies M₁ ≫ M₂ orbit their CM in circles; massless test particle m₃:

```
  ROTATING FRAME (co-rotating with M₁, M₂ at angular velocity n):

  Effective potential (centrifugal + gravitational):
  U*(x,y) = −GM₁/r₁ − GM₂/r₂ − ½n²(x² + y²)

  Jacobi integral (the one conserved quantity):
  C_J = 2U*(x,y) − v²    (conserved along any trajectory)

  C_J determines "Hill surfaces" — zero-velocity surfaces in rotating frame.
  A particle cannot cross a zero-velocity surface with given C_J.
  → limits where the particle can go (Hill's regions)
```

### 4.3 The Five Lagrange Points

```
  ∇U* = 0  →  five equilibrium points

  ──────────────────────────────────────────────────────────────────────────
         L4 (stable)
          ●
         / \
        /60°\
       /     \
      M₁──────M₂──────L3──────────L1────L2
      (larger) (smaller) (behind) (between) (beyond M₂)

      L5 (stable, below the M₁-M₂ line, symmetric to L4)
  ──────────────────────────────────────────────────────────────────────────

  L1: between M₁ and M₂ — unstable saddle, Hill sphere boundary
      Practical use: SOHO (Sun-Earth L1), DSCOVR, continuous Sun observation
      Distance from M₂: r_L1 ≈ d × (M₂/(3M₁))^(1/3)  (Hill radius)

  L2: beyond M₂ (opposite M₁) — unstable saddle
      Practical use: JWST, Herschel, Planck, Gaia — thermal stability + sky access
      Distance from M₂: r_L2 ≈ d × (M₂/(3M₁))^(1/3)  (same as L1 to first order)

  L3: opposite M₂, behind M₁ — unstable, inaccessible, no practical use
      Sun-Earth L3: always behind the Sun — no spacecraft sent there

  L4, L5: equilateral triangle vertices with M₁, M₂
          Stable iff:  M₂/(M₁+M₂) < 0.03852  (Routh's criterion)

  STABILITY CHECK:
  ┌─────────────────────────────────────────────────────────────────────┐
  │ System         M₂/(M₁+M₂)    L4/L5 stable?   Trojans?             │
  │ Sun–Jupiter    9.5 × 10⁻⁴    YES              ~12,000 Trojans      │
  │ Sun–Earth      3.0 × 10⁻⁶    YES              ~few Earth Trojans   │
  │ Sun–Mars       3.2 × 10⁻⁷    YES              ~Trojan asteroids    │
  │ Sun–Neptune    5.2 × 10⁻⁵    YES              abundant Trojans     │
  │ Earth–Moon     1.2 × 10⁻²    YES (< 0.0385)   no significant obj.  │
  └─────────────────────────────────────────────────────────────────────┘
```

### 4.4 Halo Orbits (Practical Use)

L1 and L2 are unstable — a spacecraft placed exactly there will drift. But **periodic halo orbits** around these points exist and require only small station-keeping ΔV.

```
  HALO ORBIT around L2 (JWST):
  ─────────────────────────────────────────────────────────────────────
  Amplitude: ~500,000 km in y/z, ~100,000 km in x (around L2)
  Period: ~6 months
  Station-keeping: ~2.5 m/s per year
  Advantage: continuous view of >50% of sky, thermal stability
  (one side always faces Sun, one always in shadow)
  ─────────────────────────────────────────────────────────────────────
```

---

## 5. Perturbation Theory — How Real Orbits Evolve

### 5.1 Lagrange Planetary Equations

Under a perturbing force R (disturbing function), the orbital elements evolve:

```
  da/dt = (2/na) · ∂R/∂M                             [n = mean motion]
  de/dt = ((1−e²)/na²e)·∂R/∂M − √(1−e²)/(na²e)·∂R/∂ω
  di/dt = −1/(na²√(1−e²) sin i)·(∂R/∂Ω − cos i·∂R/∂ω)
  dΩ/dt = +1/(na²√(1−e²) sin i)·∂R/∂i
  dω/dt = +√(1−e²)/(na²e)·∂R/∂e − cos i/(na²√(1−e²) sin i)·∂R/∂i
  dM/dt = n − (2/na)·∂R/∂a − (1−e²)/(na²e)·∂R/∂e

  These are exact — the full osculating element dynamics.
  Perturbation theory: expand R in small parameter, average over fast angle (M).
  → Secular terms: systematic drift (orbit-averaged)
  → Periodic terms: oscillate with orbital frequencies
```

### 5.2 J₂ Perturbations — The Most Important Real-World Case

Earth's equatorial bulge (J₂) acts as a perturbation R on satellite orbits:

```
  J₂ SECULAR EFFECTS (orbit-averaged):

  Nodal regression:
  ┌─────────────────────────────────────────────────────────┐
  │  dΩ/dt = −(3/2) · n · J₂ · (R_E/a)² · cos i          │
  │                              (1−e²)²                   │
  └─────────────────────────────────────────────────────────┘
  Prograde orbits (i < 90°): Ω decreases (nodes regress westward)
  Retrograde orbits (i > 90°): Ω increases (nodes precess eastward)

  Apsidal precession:
  ┌─────────────────────────────────────────────────────────┐
  │  dω/dt = +(3/4) · n · J₂ · (R_E/a)² · (5cos²i − 1)   │
  │                               (1−e²)²                  │
  └─────────────────────────────────────────────────────────┘
  5cos²i − 1 = 0 at i = 63.43° → ω frozen (Molniya condition)

  ENGINEERING APPLICATIONS:

  Sun-synchronous orbit:  choose i so dΩ/dt = +360°/yr (matches Earth's orbit)
    → satellite always crosses equator at same local solar time
    → i ≈ 97–98° (slightly retrograde)
    → used by: Landsat, Sentinel, weather sats, spy sats

  Molniya orbit:  i = 63.43°, e ≈ 0.74, T = 12 hr
    → ω = 270° frozen → apoapsis always over Northern Hemisphere
    → ~8 hr per orbit with high elevation over Russia/Arctic
    → used by Russian Molniya comms satellites, SIRIUS Radio

  Frozen orbit:  choose (e, i, ω) to minimize secular element changes
    → long-lived satellite without frequent maneuvers
```

---

## 6. Orbital Resonances

### 6.1 Mean Motion Resonances (MMR)

Two bodies are in p:q MMR when their mean motions satisfy:

```
  p · n₁ = q · n₂     (p, q positive integers)

  Equivalent: T₁/T₂ = p/q   (period ratio is rational)

  The order of the resonance = |p − q|
  Lower order → stronger resonance (larger perturbation amplitude)
```

### 6.2 Stable vs Destabilizing Resonances

Resonances are *not* all alike:

```
  DESTABILIZING: Kirkwood Gaps in asteroid belt (Jupiter MMRs)
  ─────────────────────────────────────────────────────────────────────
  Resonance with Jupiter    Location (AU)    Effect
  ─────────────────────────────────────────────────────────────────────
  4:1                        2.06             gap (asteroids cleared out)
  3:1                        2.50             gap (Hestia family border)
  5:2                        2.82             gap
  7:3                        2.95             gap
  2:1                        3.27             Hecuba gap
  ─────────────────────────────────────────────────────────────────────
  Mechanism: repeated Jupiter kicks pump eccentricity → Mars/Earth
  crossing orbits → eventual close encounter → ejection from belt

  STABILIZING: Orbital resonances that protect
  ─────────────────────────────────────────────────────────────────────
  Resonance               Bodies               Status
  ─────────────────────────────────────────────────────────────────────
  3:2 with Neptune        Plutinos (Pluto...)  ~200 known — STABLE
  1:1 with Jupiter        Trojans (L4, L5)     ~12,000 — STABLE
  1:1 with Neptune        Neptune Trojans       STABLE
  2:1 (Lindblad MMR)      Saturn ring gaps      gap = destabilizing
  ─────────────────────────────────────────────────────────────────────
  Why 3:2 Neptune is stable while 2:1 Jupiter is not:
  In the Pluto case, the resonance is "protected" — Pluto's aphelion
  is near Neptune's orbit, but the resonance ensures they are NEVER
  near each other at the same time. The critical angle librates rather
  than circulating.
```

### 6.3 The Laplace Resonance — Jupiter's Galilean Moons

```
  n_Io : n_Europa : n_Ganymede  ≈  4 : 2 : 1

  More precisely, the three-body Laplace resonance:
  φ_L = λ_Io − 3λ_Europa + 2λ_Ganymede = 180° (librates around 180°)
  where λ = mean longitude

  CONSEQUENCES:
  1. Orbital eccentricities maintained non-zero (Io: e≈0.004, forced by Europa)
  2. Io's non-zero eccentricity → varying tidal deformation → TIDAL HEATING
  3. Io is the most volcanically active body in the solar system
  4. Europa's eccentricity → possible subsurface liquid ocean (tidal heating)

  The resonance is self-correcting: if Io speeds up slightly,
  it pushes Europa back in phase; Europa does same to Ganymede.
  Very stable over solar system age.
```

### 6.4 Secular Resonances

MMR is about orbital *periods*. Secular resonances are about orbital *precession frequencies*:

```
  When the apsidal precession rate (dω/dt) or nodal regression rate (dΩ/dt)
  of one body matches a fundamental frequency of the planetary system.

  Key secular resonances in solar system:
  ─────────────────────────────────────────────────────────────────────────
  ν₆ resonance: dω/dt of asteroid = g₆ (Saturn's apsidal frequency)
    Located at ~2.1 AU inner asteroid belt boundary
    Pumps eccentricity → Mars-crossing → removed from belt
    Acts as the "inner edge" of the asteroid belt

  ν₁₆ resonance: nodal regression rate matches s₆ (Saturn nodal rate)
    Located at ~2.1 AU (overlaps ν₆)
    Pumps inclination

  These secular resonances, combined with Kirkwood gaps, largely explain
  the structure of the asteroid belt.
```

---

## 7. Tidal Mechanics

### 7.1 Tidal Force

Gravity varies across an extended body — the *differential* is the tidal force:

```
  TIDAL ACCELERATION on mass at displacement δ from body center,
  in the direction toward perturber M at distance d:

             2GM δ
  a_tidal = ───────   (radial component, toward perturber)
               d³

  Scales as M/d³ — same dependence as precession forcing.
  Falls off faster than gravity itself (1/d²).

  TIDAL DEFORMATION OF EARTH by Moon:
  ─────────────────────────────────────────────────────────────────────
  Solid Earth tide:  ~0.3 m  (measurable with GPS, strainmeters)
  Ocean equilibrium: ~0.27 m  (theoretical — actual ocean tides larger)
  Bay of Fundy:      ~15 m   (resonance of ocean basin, 12.5-hr period ≈ tidal period)
  Open ocean:        0.5–1 m  (typical)
  ─────────────────────────────────────────────────────────────────────
  The tidal bulge is AHEAD of the Moon (Earth rotates faster than Moon orbits)
  → Moon pulls backward on bulge → Earth rotation slows
  → Moon gains energy → Moon's orbit expands
  → Moon recedes: +3.8 cm/yr (measured by laser ranging to Apollo retroreflectors)
```

### 7.2 Tidal Locking

The same tidal torque that slows Earth's rotation eventually brings a body to **synchronous rotation** — one face permanently toward the perturber.

```
  SYNCHRONOUS ROTATION (spin = orbital period):
  ─────────────────────────────────────────────────────────────────────
  Body              Spin:Orbit ratio   Notes
  ─────────────────────────────────────────────────────────────────────
  Moon              1:1 (locked)       We always see the same face
  Pluto/Charon      1:1 (mutually)     Both tidally locked to each other
  Io, Europa, etc.  1:1                All Galilean moons locked
  Mercury           3:2 (NOT 1:1!)     Spin-orbit resonance, not lock
  Venus             retrograde, slow   Thermal atmospheric tides complicate
  ─────────────────────────────────────────────────────────────────────

  Mercury 3:2 resonance:
  Rotates 3 times per 2 orbits. The 3:2 is a stable resonance because
  Mercury's high eccentricity (e=0.206) makes 1:1 unstable — the torque
  averages to non-zero at 3:2 but averages away at other resonances.

  Tidal locking timescale:
       a⁶ Q m_planet
  τ ∝ ──────────────      Q = tidal dissipation factor (rock: ~100, ice: ~10⁴)
       M_star² R⁵_planet

  Small a (close orbit), large m_star, large R_planet → faster locking.
  Moon locked to Earth in ~100 Myr; Mercury locked in ~1 Gyr.
```

### 7.3 Roche Limit — When Tides Destroy

If a body orbits too close, tidal forces overcome its self-gravity and it is torn apart:

```
  ROCHE LIMIT (fluid body approximation):

  d_Roche ≈ 2.44 R_primary × ( ρ_primary / ρ_secondary )^(1/3)

  ┌─────────────────────────────────────────────────────────────────────┐
  │  System              d_Roche    Comparison                         │
  │  Earth (fluid Moon)  ~9,500 km  ~1.5 R_Earth (Moon at 384,400 km) │
  │  Saturn (ice)        ~87,000 km Saturn's rings are INSIDE this!    │
  │  Sun (Earth)         ~557,000 km ~0.8 R_Sun (well inside Sun)      │
  └─────────────────────────────────────────────────────────────────────┘

  Saturn's rings exist because:
  (a) they are inside Saturn's Roche limit → ring material cannot coalesce
  (b) the rings are continuously supplied (impacts, Enceladus plumes)
  (c) the rings are relatively young (~100 Myr, not primordial)

  For RIGID bodies: stronger (tensile strength matters), different formula.
  Comet Shoemaker-Levy 9: fragmented inside Jupiter's Roche limit (1992),
  then the chain of fragments impacted Jupiter (1994).
```

### 7.4 Tidal Heating

Forced orbital eccentricity → varying tidal deformation → viscous dissipation → heat:

```
  IO (Jupiter):
  ─────────────────────────────────────────────────────────────────────
  Europa's resonance forces Io's eccentricity to e≈0.004
  → Io's shape oscillates by ~100 m per orbit (1.77 days)
  → Dissipated power ≈ 6×10¹³ W (Io's interior heat flux ~2 W/m²)
  → Exceeds Earth's total geothermal output by factor ~35
  → 400+ active volcanoes; sulfur dioxide plains
  ─────────────────────────────────────────────────────────────────────
  Power formula:
                21  k₂  G M_perturber² R⁵ e²
  P_tidal = ────────────────────────────────────
                  2 Q a⁶

  k₂ = Love number (deformability), Q = dissipation quality factor
  P ∝ e² / a⁶ — very steep distance dependence
```

---

## 8. Orbital Maneuvers

### 8.1 Hohmann Transfer

Minimum-energy path between two coplanar circular orbits:

```
  HOHMANN TRANSFER  r₁ → r₂  (assume r₂ > r₁)

  Transfer ellipse:  a_t = (r₁ + r₂) / 2

     r₁  ──●────────────────────────────────────────●──  r₂
            ↑ Δv₁ (burn 1)                          ↑ Δv₂ (burn 2)
            └─── transfer ellipse ──────────────────┘

  Δv₁ = v_c1 · ( √(2r₂/(r₁+r₂)) − 1 )   [accelerate at periapsis]
  Δv₂ = v_c2 · ( 1 − √(2r₁/(r₁+r₂)) )   [accelerate at apoapsis]

  Transfer time: t = π √(a_t³/GM)        [half the period of transfer ellipse]

  LEO → GEO example (r₁ = 6778 km, r₂ = 42164 km):
    Δv₁ ≈ 2.42 km/s
    Δv₂ ≈ 1.47 km/s
    Total: ≈ 3.89 km/s,   Transit: ~5.25 hours
```

### 8.2 Gravity Assist (Slingshot)

```
  IN PLANET'S REST FRAME:
  Speed is unchanged (elastic scattering), direction rotated by deflection angle.

  IN HELIOCENTRIC FRAME:
  The planet is moving — the spacecraft gains or loses heliocentric energy.

  Maximum speed gain:  Δv_max = 2 V_planet  (fly by behind planet, prograde)
  Maximum speed loss:  Δv_max = 2 V_planet  (fly by ahead of planet)

  ┌─────────────────────────────────────────────────────────────────────┐
  │  Voyager 2 gravity assists (launched 1977):                         │
  │  Jupiter (1979): +10 km/s → Saturn achievable                      │
  │  Saturn  (1981): +5 km/s  → Uranus achievable                      │
  │  Uranus  (1986): +3 km/s  → Neptune achievable                     │
  │  Neptune (1989): final flyby; now coasting at ~15 km/s             │
  │  Without assists: Uranus/Neptune missions would require ~5× more Δv │
  └─────────────────────────────────────────────────────────────────────┘

  CONSTRAINT: The Voyager 2 sequence required a planetary alignment
  that occurs once every ~176 years (next: ~2153).
```

### 8.3 Tsiolkovsky Rocket Equation

```
  Δv = v_e · ln(m₀/m_f)        v_e = exhaust velocity (Isp × g₀)

  m₀ = initial mass (fueled)
  m_f = final mass (dry)

  Consequence: exponential relationship between Δv and mass ratio
  ─────────────────────────────────────────────────────────────────────
  Δv = 10 km/s, Isp = 450 s (H₂/O₂):   v_e ≈ 4.41 km/s
  m₀/m_f = e^(10/4.41) ≈ 9.7   →  ~90% of initial mass must be propellant

  This is why multi-stage rockets exist, and why gravity assists are so valuable —
  each km/s of gravity assist is worth exponentially more in propellant mass.
```

---

## 9. Chaos and Long-Term Stability

### 9.1 Lyapunov Exponents and the Solar System

```
  Lyapunov exponent λ: two nearby trajectories diverge as e^(λt)
  Lyapunov time T_L = 1/λ: timescale for initial uncertainty to amplify by e

  Solar system Lyapunov time: ~5 Myr (Laskar 1989, using secular equations)
  → Two initial conditions differing by 1 mm in Mercury's position
    lead to completely different planetary positions after ~100 Myr

  BUT: Lyapunov chaos ≠ immediate instability
  The chaos is "bounded chaos" — planets stay in roughly their current orbits
  even while individual trajectories diverge exponentially.

  ANALOGY: weather is chaotic (2-week limit), but Earth's orbit isn't
  changing season to season. Different timescale, different character.
```

### 9.2 Mercury's Orbital Instability

```
  Mercury is the solar system's problem child:

  Laskar & Gastineau (2009) — 2500 integrations for 5 Gyr:
  ─────────────────────────────────────────────────────────────────────
  ~99% of runs: planetary system survives to present day ✓
  ~1% of runs: Mercury's eccentricity excited to e > 0.9 by secular resonance
               → Mercury collides with Venus or Sun
               → In one run: Mercury destabilizes Mars → collision with Earth!
  ─────────────────────────────────────────────────────────────────────
  The culprit: a secular resonance between Mercury's apsidal precession
  rate and Jupiter's (the g₁ ≈ g₅ near-resonance)
  Currently g₁ = 5.59"/yr, g₅ = 4.25"/yr — close but not resonant.
  If g₁ crosses g₅ (possible under the chaotic evolution): rapid eccentricity growth.

  Connection to Milankovitch: this is why La2004/La2010 are unreliable
  beyond ±50 Myr — Mercury's chaotic orbit propagates uncertainty into
  Earth's orbital solution.
```

### 9.3 The Moon's Role in Earth's Stability

Covered in 02-MILANKOVITCH.md but worth connecting here:

```
  WITHOUT MOON:
  Earth's precession rate → 0 → secular resonances with planetary system
  → obliquity could wander 0°–85° on ~10–100 Myr timescales
  → catastrophic climate swings

  WITH MOON:
  Fast precession (~26 kyr) sweeps through resonances quickly
  → perturbations average away rather than accumulate
  → obliquity confined to 22°–24.5°

  The Moon is therefore not only a tidal engine (Section 7) but also
  a gyroscopic stabilizer of Earth's climate. Moons of similar size
  relative to their planet are rare — Earth-Moon is exceptional.
```

---

## Decision Cheat Sheet

```
  ┌────────────────────────────────────────────────────────────────────────────┐
  │ Problem                             │ Tool / Formula                       │
  ├────────────────────────────────────────┼────────────────────────────────────┤
  │ Speed at any point in orbit         │ Vis-viva: v² = GM(2/r − 1/a)       │
  ├────────────────────────────────────────┼────────────────────────────────────┤
  │ Orbit period                        │ T = 2π √(a³/GM)                     │
  ├────────────────────────────────────────┼────────────────────────────────────┤
  │ Position at time t                  │ Kepler's equation: M = E − e sin E  │
  ├────────────────────────────────────────┼────────────────────────────────────┤
  │ Will satellite orbit precess?        │ J₂ nodal regression: dΩ/dt ∝ cos i │
  │ Need sun-synchronous?                │ i ≈ 97–98° (retrograde, dΩ/dt =    │
  │                                      │ +360°/yr)                           │
  ├────────────────────────────────────────┼────────────────────────────────────┤
  │ Want apogee frozen over latitude?    │ Molniya: i = 63.43°, ω = 270°      │
  ├────────────────────────────────────────┼────────────────────────────────────┤
  │ Is a resonance stable or clearing?   │ Check critical angle libration vs   │
  │                                      │ circulation; check forced e growth  │
  ├────────────────────────────────────────┼────────────────────────────────────┤
  │ Lagrange point choice for mission    │ L1: Sun-monitoring, continuous view │
  │                                      │ L2: deep-space observation, thermal │
  │                                      │ L4/L5: debris/Trojans, station-keep │
  ├────────────────────────────────────────┼────────────────────────────────────┤
  │ Does object get tidally disrupted?   │ Check if r < d_Roche               │
  │                                      │ d_Roche ≈ 2.44 R (ρ₁/ρ₂)^(1/3)   │
  ├────────────────────────────────────────┼────────────────────────────────────┤
  │ Is tidal locking expected?           │ τ ∝ a⁶ Q m / (M² R⁵)             │
  │                                      │ Small a → locked fast               │
  ├────────────────────────────────────────┼────────────────────────────────────┤
  │ Minimum-ΔV transfer between orbits   │ Hohmann (two burns); bi-elliptic   │
  │                                      │ if r₂/r₁ > ~12 (three burns)       │
  ├────────────────────────────────────────┼────────────────────────────────────┤
  │ Getting to outer solar system fast   │ Gravity assist; plan alignment     │
  │                                      │ windows years in advance            │
  └────────────────────────────────────────┴────────────────────────────────────┘
```

---

## Common Confusion Points

**"Kepler's third law: T² ∝ a³" — what's the proportionality constant?**
T² = 4π²a³/(GM). The M here is the *total* mass m₁+m₂. For planets orbiting the Sun, M ≈ M_☉ since M_☉ ≫ m_planet. For binary stars, both masses matter. The original Kepler relation (planets in the same solar system) hides the GM because it cancels in the ratio T₁²/T₂² = a₁³/a₂³.

**"Geostationary vs geosynchronous"**
Both have T = 24 hr (actually sidereal day = 23h 56m). Geosynchronous: any inclination — ground track is a figure-8 (analemma). Geostationary: i = 0° — fixed point above equator. All geostationary orbits are geosynchronous; not vice versa. GEO altitude ≈ 35,786 km from Earth's surface.

**"Lagrange points are where gravity cancels"**
No — L4 and L5 are stable points where the object is *not* gravitationally balanced, it's in the centrifugal-plus-gravitational effective potential minimum. The object at L4 is actually being pulled toward *both* masses. The stability comes from Coriolis forces in the rotating frame.

**"Tidal locking means the Moon doesn't rotate"**
The Moon rotates once per revolution — that IS tidal locking. In the inertial frame, the Moon rotates (you can observe it from the stars). In the Earth-Moon rotating frame, it appears not to. Tidal locking = spin period = orbital period, not zero spin.

**"Mercury's 3:2 resonance is a step toward full tidal locking"**
Possibly. It depends on Mercury's Q factor and whether the 3:2 resonance has its own stable basin of attraction vs being a transient. Current models suggest the 3:2 is a stable capture state for Mercury's current eccentricity — not necessarily an intermediate.

**"Chaos means the solar system is unstable"**
No. Chaos (positive Lyapunov exponent) means long-term predictability is limited, not that the system is headed toward catastrophic change. The solar system has been chaotic in this sense for its entire 4.6 Gyr history and will likely survive another 5 Gyr. The ~1% instability probability for Mercury is real but rare.

**"The Kirkwood gaps are empty because asteroids were never there"**
Wrong direction. Resonances actively remove material over geological time. The asteroid belt initially had a more uniform population; Jupiter's resonances swept out the gap locations over ~100 Myr timescales by pumping eccentricities to Mars/Earth-crossing orbits, leading to eventual ejection or collision.
