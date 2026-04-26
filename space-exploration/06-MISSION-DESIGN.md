# Mission Design: Interplanetary Trajectories

## The Big Picture

Interplanetary mission design is the art of finding trajectories from Earth to a target body that satisfy constraints on launch vehicle capability, mission duration, spacecraft mass, and arrival conditions. The fundamental tool is the patched conic approximation; the gold standard is full numerical integration.

```
+------------------------------------------------------------------+
|              INTERPLANETARY TRAJECTORY FRAMEWORK                 |
+------------------------------------------------------------------+
|                                                                  |
|  DESIGN PHASES:                                                  |
|  1. Porkchop plot → launch window + C3 (departure energy)        |
|  2. Gravity assist architecture (VEGA? DVGA? multi-flyby?)       |
|  3. Arrival conditions (orbit insertion, flyby, direct entry)    |
|  4. Trajectory Correction Maneuvers (TCMs)                       |
|  5. Navigation (optical, radiometric ranging, VLBI)              |
|                                                                  |
|  KEY QUANTITIES:                                                  |
|  C3 = v∞² = excess hyperbolic velocity squared at departure      |
|  v∞ = arrival hyperbolic excess speed                            |
|  ΔV_insertion = how much to slow down to orbit                   |
|  Δt = flight time (months to years for outer planets)            |
+------------------------------------------------------------------+
```

---

## Porkchop Plots and Launch Windows

```
PORKCHOP PLOTS
===============

  DEFINITION: Contour map of C3 (or Δv) vs launch date (X) and arrival date (Y)
              The minimum-energy transfer traces the "pork chop" shape

  C3 = v∞² at departure = (v_spacecraft - v_Earth)² in heliocentric frame
  Units: km²/s²
  Launch vehicle performance scales with C3:
    C3 = 0: minimum energy escape (just barely leaves Earth SOI)
    C3 > 0: hyperbolic departure with v_∞ = √C3
    For Mars: typical C3 = 8-16 km²/s² (good window)

  READING A PORKCHOP PLOT:
    X axis: launch date
    Y axis: arrival date (or flight time)
    Contours: constant C3 (or ΔV)
    Inner contours = lower energy = more favorable
    "Pork chop" shape: minimum-energy region repeats with synodic period

  LAUNCH WINDOWS:
    Earth-Mars synodic period: ~2.135 years
    Opportunity windows: ~26 months apart
    Window width: typically 15-30 days for "good" C3
    Best window (minimum C3) varies by synodic period; 2003 and 2018 were exceptional

  FLIGHT TIME TRADEOFF:
    Hohmann transfer: ~8.5 months (minimum energy); C3 ≈ 8-9 km²/s²
    "Fast" transfer: 4-6 months; much higher C3 (more propellant)
    Conjunction class: long stay on Mars (~500 days); short transit (~180 days each)
    Opposition class: short stay on Mars (~30-60 days); one long transit (~320 days)
    ISRO Mangalyaan (2013): minimum energy; 10 months transit
    NASA Mars missions: typically Hohmann-class minimum energy
```

---

## Gravity Assist Mission Architecture

```
GRAVITY ASSIST TRAJECTORY DESIGN
===================================

  VENUS-EARTH-EARTH GRAVITY ASSIST (VEEGA):
    Used by Galileo (Jupiter) and Cassini (Saturn)
    Why: insufficient launch vehicle capability for direct trajectory

  GALILEO TRAJECTORY:
    Launch: Oct 1989 (Shuttle + IUS upper stage)
    Venus flyby: Feb 1990 (+2.24 km/s from Venus)
    Earth flyby 1: Dec 1990 (+5.2 km/s)
    Asteroid Gaspra flyby: Oct 1991
    Earth flyby 2: Dec 1992 (+3.7 km/s)
    Jupiter arrival: Dec 1995
    Without gravity assists: far more propellant, or far lower payload

  NEW HORIZONS TRAJECTORY:
    Launch: Jan 2006 (Atlas V 551 + Star 48 kick stage)
    C3 = 157 km²/s² (enormous! fastest launch ever)
    Jupiter flyby: Feb 2007 (+4 km/s; also tested instruments)
    Pluto flyby: July 2015 (9.5 years transit)
    Arrokoth flyby: Jan 2019

  PARKER SOLAR PROBE TRAJECTORY:
    Need to slow DOWN to reach low solar orbits
    Venus retrograde flybys (7 total): each removes angular momentum
    Perihelion: 9.86 R_Sun (2024); goal 6.9 R_Sun (2025)
    Without Venus assists: would need enormous ΔV to brake into a solar orbit

  INTERPLANETARY SUPERHIGHWAY (IPS):
    Network of low-energy trajectories using L1/L2 Lagrange points
    Near-zero ΔV transfers between planets if time is unconstrained
    Useful for small spacecraft with limited propellant (not humans!)
    ACE → SOHO → other halo orbits → lunar orbits
    Genesis (solar wind sample return) used IPS-derived trajectory
```

---

## Patched Conic Approximation

```
PATCHED CONIC APPROXIMATION
============================

  PRINCIPLE: Divide trajectory into spheres of influence (SOI)
  Inside SOI: only the local body's gravity matters
  Outside SOI: only the Sun's gravity matters
  At SOI boundary: "patch" (match) the conic sections

  EARTH DEPARTURE:
    Start: parking orbit (LEO, 200 km)
    Burn: Trans-XX Injection (TXI): add Δv to achieve hyperbolic departure
    Within Earth SOI: hyperbolic orbit around Earth
    v_∞(Earth) = √(C3) = departure excess velocity
    At SOI boundary: convert to heliocentric coordinates

  HELIOCENTRIC TRANSFER:
    Spacecraft + Earth velocity → spacecraft heliocentric velocity
    Transfer orbit: Keplerian ellipse (or hyperbola for escape)
    Ignore all planets except Sun during this phase
    Duration: months to years

  TARGET ARRIVAL:
    Enter target's SOI
    Hyperbolic approach: v_∞(arrival) from porkchop plot
    If orbiting: Orbit Insertion Burn (OIB) to slow into elliptical/circular orbit
    If landing/entry: aerobraking, EDL system
    If flyby: trajectory design ensures closest approach at desired distance

  V_INFINITY AT ARRIVAL:
    Cannot be made zero with this approach (infinite ΔV needed to match orbit)
    v_∞ is the hyperbolic excess velocity
    Orbital insertion: v_periapsis = √(v_∞² + v_escape²); then brake to circular
    Lower v_∞ → less insertion ΔV → more mass to science instruments

  SOI RADII (APPROXIMATE):
    Moon:    66,000 km  (0.17 Moon-Earth distance)
    Mars:    578,000 km (0.39% of Earth-Mars distance at conjunction)
    Jupiter: 48.2 million km (large; deep gravity well)
    Earth:   925,000 km from Earth
```

---

## Aerocapture and Aerobraking

```
USING ATMOSPHERE FOR ORBIT INSERTION
======================================

  AEROBRAKING (slow orbit reduction):
    Make multiple passes through upper atmosphere
    Each pass removes a small amount of orbital energy → reduces apoapsis
    Takes weeks to months; requires precise atmospheric modeling
    USED: Magellan (Venus 1993), Mars Global Surveyor, Mars Odyssey,
          Mars Reconnaissance Orbiter

    DANGER: Too deep → heating + excessive drag → crash
            Too shallow → no reduction; misses aerobraking zone
    Navigation challenge: atmospheric density varies with season + solar activity

  AEROCAPTURE (one-pass orbit insertion):
    Single pass through atmosphere: go from hyperbolic approach to captured orbit
    HIGH ΔV savings: replaces propulsive insertion (3-5 km/s at Mars)
    NOT yet demonstrated operationally (as of 2025) in a mission
    Required: precise entry angle (too steep = burn up; too shallow = skip out)

  EDL (ENTRY, DESCENT, LANDING):
    Mars EDL is the "7 minutes of terror"
    Mars atmosphere: 1% Earth density → heat shield needed, parachute possible,
                     but too thin for terminal-velocity parachute landing alone

  CURIOSITY/PERSEVERANCE EDL SEQUENCE:
    +-----------------------------+
    |  10 km altitude: 900 m/s    | ← Parachute deploy (Mach 1.7)
    |  atmospheric entry: 5.8 km/s|
    |  heat shield peak heating   |
    +-----------------------------+
    |  1 km: heat shield jettison |
    |  parachute deployed         |
    +-----------------------------+
    |  6.4 km: powered descent    | ← Backshell + parachute separate
    |  sky crane: 8 rocket engines|
    +-----------------------------+
    |  20 m: sky crane deploys    | ← Lowers rover on tethers
    |  rover lands: 2.7 m/s       |
    |  sky crane flies away       |
    +-----------------------------+

  PROBLEM WITH DIRECT LANDING ON MARS:
    Falcon 9-style retropropulsion: works on Moon (no atmosphere)
    Mars: atmosphere too thin for large vehicles to land propulsively
    Starship on Mars: needs either very large heat shield + parachutes
                      OR massive retropropulsion (methane fuel from Mars surface)
    Key challenge for Mars human missions: land 100+ tonnes on Mars surface
```

---

## Navigation

```
SPACECRAFT NAVIGATION
======================

  ORBIT DETERMINATION (OD):
    Determine spacecraft's actual trajectory from measurements
    Update trajectory model; compute TCMs needed

  TRACKING MEASUREMENTS:
    RANGE: Time-of-flight of signal; range = (light-travel time) × c / 2
           DSN round-trip light time; accuracy ~1-10 m at Mars
    RANGE RATE (Doppler): radial velocity from Doppler shift of carrier
           Accuracy: ~0.1 mm/s; most sensitive measurement type
    VLBI (Very Long Baseline Interferometry): angular position
           Two DSN stations measure arrival time difference → angular position
           Accuracy: ~1 nrad (~0.2 mm at 1 AU)

  OPTICAL NAVIGATION (OPNAV):
    Spacecraft camera images target body against star background
    Position of target in image → bearing constraint (angle)
    Used: Voyager, Galileo, New Horizons
    Especially useful near flyby (rapid angular motion)

  AUTONOMOUS NAVIGATION:
    Deep Space 1: first autonomous navigation demo (AutoNav)
    No continuous DSN contact → spacecraft processes images + updates trajectory
    Required for fast flyby encounters (minutes of critical data)

  TRAJECTORY CORRECTION MANEUVERS (TCMs):
    Small burns (0.1-50 m/s) to correct trajectory errors
    Scheduled at mission-critical points (shortly after launch, mid-course)
    Targeting: aim for entry corridor / flyby distance / orbit insertion conditions
    Uncertainty grows without TCMs; phased approach reduces fuel

  PLANETARY PROTECTION:
    Prevents contamination of target bodies with Earth microbes
    COSPAR guidelines: category I (flyby) to V (sample return)
    Spacecraft cleaned to specific biological burden (bioassay)
    For Mars surface: 300 spores/m² limit (Category IVb)
    Affects trajectory: must avoid unintended planetary impact by 1000+ years
```

---

## Mission Phase Timeline

```
TYPICAL PLANETARY MISSION PHASES
===================================

  PHASE A: Concept Study
    Trade studies; feasibility; mission objectives; cost estimates

  PHASE B: Preliminary Design
    Define requirements; subsystem design; interface control docs (ICDs)
    Mission Design Review (MDR); PDR (Preliminary Design Review)

  PHASE C: Detailed Design
    Critical Design Review (CDR); detailed drawings; test plans
    Build prototypes; qualification units

  PHASE D: Development and Test
    Build flight hardware; environmental testing (vibe, thermal-vac, EMI)
    Integration; launch campaign; launch

  PHASE E: Operations
    Launch + Early Operations (LEOP): first 24-72 hrs critical
    Cruise: en route; limited operations; instrument calibration
    Science operations: at target; data collection
    Extended mission: if funded; additional science

  PHASE F: Closeout
    End of mission; data archiving; lessons learned

  KEY REVIEWS (NASA):
    SRR: System Requirements Review
    SDR: System Definition Review
    PDR: Preliminary Design Review (30-40% design complete)
    CDR: Critical Design Review (60-80% design complete; build starts)
    ATLO: Assembly, Test, and Launch Operations
    FRR: Flight Readiness Review (last review before launch)
```

---

## Decision Cheat Sheet

| Question | Answer |
|---|---|
| What is C3? | Characteristic energy = v∞² = excess kinetic energy at departure; C3 = 0 means just barely escaping Earth; C3 > 0 means you have velocity to spare at infinity; determines how much launch vehicle capability is needed |
| What is a porkchop plot? | Contour map of C3 (or mission ΔV) vs launch date and arrival date; shows which launch dates offer efficient trajectories; "pork chop" shape identifies launch windows |
| Why do missions use gravity assists? | To gain or lose orbital energy without propellant; equivalent to many km/s of free ΔV at the cost of flight time and additional trajectory complexity |
| What is the SOI? | Sphere of Influence: the region where a body's gravity dominates over the Sun's; inside SOI, trajectory is approximately a conic section around that body |
| What is the "7 minutes of terror" for Mars? | Time from atmospheric entry to landing for Curiosity/Perseverance; no real-time control possible (7-20 min radio delay); fully autonomous EDL sequence |
| What is aerobraking? | Multiple shallow passes through a planet's upper atmosphere to reduce orbital energy; saves enormous propellant; used by multiple Mars orbiters |
| What tracking measurement gives the best range accuracy? | Range measurement (time-of-flight); Doppler gives best velocity accuracy; VLBI gives angular position; all three combined for full orbit determination |

---

## Engineering Parallels

**Mission lifecycle gates as stage-gated development.** NASA's Phase A-F structure with SRR/SDR/PDR/CDR/FRR reviews is the aerospace equivalent of a structured SDLC with gate reviews. PDR (~30-40% design complete) corresponds to a design review where the architecture is committed but implementation is not; CDR (~60-80%) corresponds to code-complete review before integration. The review artifacts — interface control documents (ICDs), test plans, mass/power budgets — are the aerospace equivalent of API contracts, integration test suites, and capacity projections. The difference is that aerospace gate reviews are formal contractual commitments with government oversight, not internal process checkpoints.

**Trajectory correction maneuvers as feedback control.** The navigation loop — measure position via DSN ranging/Doppler, compute trajectory error, execute a TCM — is a discrete-time feedback control system operating on a weeks-to-months time constant. The "plant" is the spacecraft's trajectory; the "sensor" is the DSN; the "actuator" is the thruster; the "controller" is the navigation team's orbit determination software. The phase margin is enormous (corrections are tiny), but the stakes are high: a 1 mm/s error at departure translates to thousands of km of positional error at Mars arrival without correction.

**Gravity assist architecture as algorithm design under resource constraints.** Designing a multi-flyby trajectory (VEEGA for Cassini, or Parker Solar Probe's 7 Venus flybys) is a search problem over a sparse graph: which planets are in the right positions at the right times to provide the needed energy change? The "Tisserand criterion" is a conservation law that constrains which flyby sequences are even physically possible — analogous to an invariant that prunes the search space. Trajectory designers work backward from the destination constraints (arrival energy, approach geometry) to find feasible departure windows — the same dynamic programming structure used in optimal subproblem decomposition.

## Common Confusion Points

**Gravity assists are not free forever**: You can't keep adding flybys to gain unlimited energy. Each flyby must take energy from the planet's orbital motion; the planet slows by an undetectable amount. More practically: trajectories with many gravity assists have very long flight times and specific geometry constraints.

**Aerobraking ≠ aerocapture**: Aerobraking uses many passes over weeks-months to gradually reduce the orbit; aerocapture uses a single deep pass to go directly from hyperbolic to captured orbit. Aerocapture saves more time and propellant but is technically much harder and hasn't been demonstrated operationally.

**Mars EDL doesn't scale**: The sky crane worked for ~1 tonne rovers. Delivering 20+ tonne human missions to Mars surface is an unsolved engineering problem. The atmosphere is too thin for parachutes at those masses; retropropulsion is needed but aerodynamic heating and mass are huge challenges. Starship on Mars is a multi-year engineering challenge, not a solved problem.

**Synodic period ≠ how often you can launch**: The Earth-Mars synodic period is ~26 months, meaning windows repeat every ~26 months. But each window has different energy characteristics — some windows have much lower C3 than others. Planning for a specific mission requires evaluating which window offers acceptable performance.
