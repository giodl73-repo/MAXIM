# Orbital Mechanics and the Rocket Equation

## The Big Picture

Orbital mechanics is the application of Newtonian gravity and classical mechanics to spacecraft trajectories. The Tsiolkovsky rocket equation is the fundamental constraint; Kepler's laws govern orbits; the Hohmann transfer is the minimum-energy path between orbits.

```
+------------------------------------------------------------------+
|                    ORBITAL MECHANICS FRAMEWORK                   |
+------------------------------------------------------------------+
|                                                                  |
|  GOVERNING PHYSICS  (sets the hard constraints)                  |
|  -----------------------------------------------                |
|  Newton's gravity (F=GMm/r²)                                     |
|  Conservation of energy  +  Conservation of angular momentum     |
|       |                               |                          |
|       v                               v                          |
|  KEY EQUATIONS  (closed-form results from the physics)           |
|  -----------------------------------------------                |
|  Vis-viva: v²=GM(2/r−1/a)    Tsiolkovsky: Δv=Isp·g₀·ln(m₀/mf) |
|  Kepler T²∝a³                Hohmann: min-energy transfer orbit  |
|  Orbital elements (6 params define any conic)                    |
|       |                               |                          |
|       v                               v                          |
|  MISSION APPLICATIONS  (engineering choices within the envelope) |
|  -----------------------------------------------                |
|  Orbit insertion    Δv budget    Gravity assists                  |
|  Station-keeping    Launch windows   GTO / TLI / TMI             |
+------------------------------------------------------------------+
```

---

## Kepler's Laws

```
KEPLER'S THREE LAWS
====================

  LAW 1 (Elliptical Orbits):
    All orbits are conic sections (ellipse, parabola, hyperbola)
    Sun (or attracting body) at one focus
    Circle = special case of ellipse (e = 0)

  LAW 2 (Equal Areas):
    A line from body to focus sweeps equal areas in equal times
    → Faster near periapsis (closest point); slower near apoapsis
    → Conservation of angular momentum: L = m × v × r = constant

  LAW 3 (Harmonic Law):
    T² ∝ a³
    T² = (4π²/GM) × a³
    where T = period, a = semi-major axis, GM = standard gravitational param.
    For Earth orbit: T (years) ≈ a (AU)^(3/2)
    ISS (408 km ≈ 0.0063 AU from Earth center): T ≈ 92 min

ORBITAL ELEMENTS (6 parameters define any orbit):
  a:   semi-major axis (size)
  e:   eccentricity (shape)
  i:   inclination (tilt relative to reference plane)
  Ω:   right ascension of ascending node (orientation of plane)
  ω:   argument of periapsis (orientation of ellipse in plane)
  ν/M: true/mean anomaly (position in orbit at epoch)
```

---

## Vis-Viva Equation

```
VIS-VIVA: THE ORBITAL SPEED EQUATION
======================================

  v² = GM(2/r - 1/a)
  where v = orbital speed, r = current distance, a = semi-major axis

  SPECIAL CASES:
    Circular orbit (a = r):     v = √(GM/r)
    Periapsis of ellipse:       v > circular (maximum speed)
    Apoapsis of ellipse:        v < circular (minimum speed)
    Parabolic escape (e = 1):   v = √(2GM/r) = √2 × v_circular

  NUMERICAL EXAMPLES (Earth):
    LEO (r = 6778 km):  v_circ = 7.73 km/s
    GEO (r = 42,164 km): v_circ = 3.07 km/s
    Moon (r = 384,400 km): v_circ = 1.02 km/s
    Escape from Earth:   v_esc = 11.19 km/s (from surface)

  DELTA-V = CHANGE IN VELOCITY:
    Δv = |v_final - v_initial|  (for orbit changes)
    Not the same as speed change (direction matters)
    Total mission Δv budget = sum of all maneuver Δv values
    Δv determines propellant mass via rocket equation
```

---

## The Tsiolkovsky Rocket Equation

```
TSIOLKOVSKY ROCKET EQUATION
=============================

  Δv = v_e × ln(m₀/mf)
     = Isp × g₀ × ln(m₀/mf)

  where:
    Δv  = total velocity change achievable (km/s)
    v_e = effective exhaust velocity (km/s) = Isp × g₀
    Isp = specific impulse (s) — engine efficiency metric
    g₀  = 9.80665 m/s² (standard gravity; just a units conversion)
    m₀  = initial mass (spacecraft + full propellant)
    mf  = final mass (spacecraft + empty tanks)
    ln(m₀/mf) = natural log of the mass ratio

  TYRANNY OF THE ROCKET EQUATION:
    To achieve higher Δv for the same dry mass:
    → Need exponentially more propellant
    → Example: Δv = 9.4 km/s, Isp = 311 s (kerosene)
      Mass ratio needed = e^(9400/(311×9.8)) = e^(3.09) = 22
      → 21 kg of propellant per 1 kg of payload + structure
    → This is why rockets are mostly propellant (95%+ by mass)
    → Why staging exists: drop empty tanks to reduce dead mass

  STAGING:
    Multi-stage rocket: each stage is discarded when empty
    Effective mass ratio = product of individual stage mass ratios
    2-stage: m_ratio_1 × m_ratio_2 (much more favorable)
    Tsiolkovsky equation applied per stage:
    Δv_total = Δv_stage_1 + Δv_stage_2 + ...

  PHYSICAL INSIGHT:
    High Isp → less propellant for same Δv
    Chemical rockets: Isp ≈ 300-460 s (limited by bond energy of molecules)
    Ion engines: Isp ≈ 1500-10,000 s (much more efficient; but low thrust)
    Nuclear thermal: Isp ≈ 800-1000 s (hydrogen heated by reactor)
```

---

## Orbital Maneuvers

### Hohmann Transfer

```
HOHMANN TRANSFER ORBIT
=======================

  Minimum-energy transfer between two CIRCULAR, COPLANAR orbits

  GEOMETRY:
  +--------------+
  | Initial      |
  | Orbit r₁     |
  +--------------+

    BURN 1: Δv₁ at periapsis.

    Transfer ellipse (semi-major axis a = (r₁ + r₂) / 2)
    touches both orbits.

    BURN 2: Δv₂ at apoapsis.

  +--------------+
  | Final        |
  | Orbit r₂     |
  +--------------+

  MATH:
    Δv₁ = √(GM/r₁) × (√(2r₂/(r₁+r₂)) - 1)
    Δv₂ = √(GM/r₂) × (1 - √(2r₁/(r₁+r₂)))
    Transfer time = T_hohmann/2 = π√((r₁+r₂)³/(8GM))

  EARTH LEO → GEO EXAMPLE:
    r₁ = 6778 km (LEO); r₂ = 42,164 km (GEO)
    Δv₁ ≈ 2.46 km/s (from LEO)
    Δv₂ ≈ 1.47 km/s (to circularize at GEO)
    Total: ~3.93 km/s
    Transfer time: ~5.25 hours (one-way)

  LIMITATIONS:
    Only optimal for coplanar, circular → circular
    Plane changes are very expensive (Δv = 2v × sin(Δi/2))
    Combined inclination change + apoapsis kick → cheaper than separate
    Not applicable to hyperbolic/escape trajectories (need Δv > escape)
```

### Gravity Assists (Flyby Maneuvers)

```
GRAVITY ASSISTS
===============

  FREE Δv by exchanging momentum with a planet

  MECHANISM:
    Spacecraft approaches planet on hyperbolic trajectory
    In the planet's reference frame: speed unchanged (hyperbolic, elastic)
    In the heliocentric frame: SPEED CHANGES

    If spacecraft flies behind a planet (in direction of orbital motion):
    → Planet's gravity pulls spacecraft forward
    → Spacecraft gains energy (stolen from planet's orbital energy)
    → Δv = up to 2 × v_planet (for a retrograde pass; theoretical max)

  REAL EXAMPLES:
    Voyager 1: Jupiter (1979) + Saturn (1980) → escape solar system
    Cassini: Earth flyby (1999) + Jupiter (2000) → Saturn insertion 2004
    Messenger: 2 Earth + 2 Venus + 3 Mercury flybys to slow down to Mercury orbit
    New Horizons: Jupiter (2007) gravity assist → Pluto (2015)
    Parker Solar Probe: 7 Venus flybys to lower perihelion to <10 R_Sun

  TYPES:
    Prograde flyby (pass behind planet): GAIN energy (speed up in heliocentric)
    Retrograde flyby (pass ahead of planet): LOSE energy (slow down)
    Polar flyby: change inclination without much energy change

  VELCRONAUTICS? (deceleration):
    Arriving at Mercury or going deep into solar gravity well:
    Use retrograde gravity assists to LOSE energy
    Messenger needed 6.9 km/s of deceleration; gravity assists provided most of it
```

---

## Orbit Types

```
ORBIT TAXONOMY
===============

  BY ALTITUDE (Earth):
    LEO:  200-2000 km   v~7.8 km/s, T~90-127 min
    MEO: 2000-35786 km  (GPS ~20,200 km; T~12 hr)
    GEO: 35,786 km      v~3.1 km/s, T=24 hr (geostationary)
    HEO: >35,786 km     (Molniya; highly elliptical)

  BY INCLINATION:
    Equatorial: i ≈ 0° (GEO)
    Polar:      i ≈ 90° (Earth observation, SSO)
    Sun-synchronous (SSO): i ≈ 97-99° (ascending node precesses at 1°/day
                           → always same local time; Earth obs standard)
    Retrograde: i > 90°

  SPECIAL ORBITS:
    Molniya: highly elliptical; apoapsis over Russia; 12-hr period
             Used for Soviet communications over high latitudes
    Tundra:  ~63.4° incl.; 24-hr period; single apoapsis over target
    GTO (Geostationary Transfer): Hohmann transfer ellipse from LEO to GEO
    HEO for radiation avoidance: keeps spacecraft in Van Allen belts less
    Graveyard orbit: +300 km above GEO; end-of-life disposal for GEO sats

  EARTH-MOON-SUN:
    LAGRANGE POINTS (5 equilibrium points in 3-body problem):
      L1: between Earth and Moon (~326,000 km from Earth)
      L2: behind Moon (far side); ~450,000 km
      L3: behind Earth (opposite Moon)
      L4/L5: 60° ahead/behind Moon; Trojan points (stable)
      L1/L2/L3: unstable (need stationkeeping)
      L4/L5: stable

    HALO ORBITS:
      L1/L2 halo: orbit around the Lagrange point (not a true equilibrium)
      Require small ΔV station-keeping to maintain
      SOHO, JWST (L2), ACE (L1), DSCOVR (L1)
      Lunar Gateway: NRHO (Near-Rectilinear Halo Orbit) around L2
```

---

## Delta-V Budget

```
CUMULATIVE Δv BUDGET (km/s from Earth surface)
================================================

  To achieve:                           Δv (km/s)
  ---------------                       ---------
  LEO (200 km, i=28.5°)                 9.4
  LEO (200 km, polar, i=90°)            9.7
  GEO (from LEO, Hohmann + plane chg)   4.2
  Lunar flyby (escape + targeting)      3.1 (from LEO)
  Lunar orbit (from LEO)                3.9
  Lunar surface (from LEO, 1-way)       5.7
  Trans-Mars Injection (from LEO)       3.6-6.3  (window-dependent)
  Mars orbit capture (from TMI)         0.5-2.0  (aerobraking or propulsive)
  Mars surface (from LEO)               ~13-15
  Jupiter (flyby from LEO, direct)      ~8-9
  Jupiter (with Earth+Venus gravity)    ~4-6

  GRAVITY AND DRAG LOSSES:
    Getting from surface to LEO requires ~9.4 km/s total, but
    orbital velocity at LEO is only 7.8 km/s
    Difference (~1.6 km/s): gravity drag (thrust wasted fighting gravity
    during vertical ascent) + aerodynamic drag (thinner at altitude,
    so drag loss small ~0.1-0.2 km/s)
    → Launch vehicles must produce ~21% more Δv than orbital velocity alone

  AEROBRAKING:
    Use atmosphere to lose velocity (no propellant cost)
    Used: Mars missions, Magellan (Venus), Cassini (Saturn aerobraking ~ not)
    Saves enormous Δv for Mars orbit insertion
    Requires careful thermal design for entry
```

---

## Decision Cheat Sheet

| Question | Answer |
|---|---|
| What does the Tsiolkovsky equation tell you? | How much velocity change you can achieve given propellant mass and exhaust velocity; exponential relationship — doubling Δv requires squaring the mass ratio |
| What is specific impulse (Isp)? | Thrust per unit propellant mass flow rate; units = seconds; proportional to exhaust velocity; the efficiency metric for rocket engines |
| Why is orbital mechanics so different from normal engineering? | Counterintuitive: firing retrograde (backward) raises your orbit at the opposite side; "speeding up" while going forward puts you in a higher, slower orbit |
| What is the cheapest way to change orbits? | Hohmann transfer (two burns at periapsis and apoapsis); only minimum energy for coplanar circular orbits; plane changes are very expensive |
| How do gravity assists provide free ΔV? | Spacecraft steals orbital energy from the planet; in planet reference frame speed unchanged; in heliocentric frame speed changes |
| What is a halo orbit? | Quasi-periodic orbit around a Lagrange point (not a true equilibrium); requires station-keeping; used by JWST (L2), SOHO (L1) |
| Why is the rocket equation "tyrannical"? | To go from 9 km/s to 10 km/s ΔV requires exponentially more propellant — not linearly. Every extra km/s costs more than the last. |

---

## Engineering Parallels

**Δv budget as a resource-allocation problem.** Total mission Δv is a fixed budget; every maneuver is a withdrawal. The planner allocates burns across mission phases to minimize total cost subject to constraints (launch vehicle capability, arrival conditions, mission duration). This is integer programming on a manifold — the state space is continuous, the decision points are discrete maneuvers, and the objective is the sum of |Δv| terms. Gravity assists add negative-cost arcs to the graph.

**The Hohmann transfer as a shortest path.** Between two circular coplanar orbits, the Hohmann transfer is the minimum total Δv path — two impulsive burns at the endpoints of the transfer ellipse. This is Dijkstra's shortest path applied to orbital energy space, where "distance" is propellant cost. More general trajectories (bi-elliptic transfers, low-thrust spirals) are different cost-metric problems on the same graph.

**Gravity assists as free energy from the graph topology.** Gravity assists exploit existing nodes in the solar system trajectory graph — planets moving through space — to add or remove orbital energy at zero propellant cost, at the expense of flight time and geometric constraints. The same principle appears in algorithm design: if a problem structure provides free transformations (symmetries, invariants), exploit them before spending computation. Voyager's Grand Tour was feasible in 1977 only because of a rare planetary alignment creating a favorable graph topology.

**Lagrange points as saddle points on the effective potential.** L4/L5 are stable equilibria (local minima); L1/L2/L3 are saddle points requiring station-keeping (unstable equilibria). Any engineer who has studied convex vs. non-convex optimization recognizes this landscape immediately. JWST orbits L2 precisely because the saddle point, though unstable, is easy to station-keep with small periodic corrections — the same reason you might deploy a service at a resource-contested boundary node rather than at a stable but distant one.

## Common Confusion Points

**Orbiting is not "escaping" gravity**: ISS is in Earth's gravity field. It's in free fall — falling in a circle. Gravity is providing the centripetal force. "Zero-g" is a misnomer; it's "free fall" or "microgravity" (tidal forces over the spacecraft volume cause tiny differential accelerations).

**Higher orbit = slower orbital speed**: Counterintuitive. At GEO (35,786 km), the spacecraft moves at 3.1 km/s — slower than LEO's 7.8 km/s. Yet GEO has more orbital energy. Energy is distributed between kinetic and potential; at higher altitude, more PE and less KE, but total E is higher.

**Inclination changes are very expensive**: Changing orbit inclination by 30° at LEO costs ~3.2 km/s — as much as going from LEO to the Moon. This is why satellites launch to their operational inclination directly from the launch site (Kennedy Space Center is at 28.5° latitude, so GEO launches to 28.5° and then perform combined perigee + inclination burns).

**The rocket equation applies to each stage separately**: A two-stage rocket's total Δv is not Isp × g₀ × ln(total initial mass / final payload mass). Each stage has its own Isp and mass ratio, and you add the Δv contributions. Staging works precisely because you discard the heavy empty first stage before running the second-stage calculation.
