# Launch Vehicles: Evolution and Architecture

## The Big Picture

A launch vehicle is a rocket system that delivers a payload from Earth's surface to orbit. The architecture choices — staging, propellants, staging ratios, engine count — determine payload capacity, cost, and reliability. The economics have been transformed by reusability.

```
+------------------------------------------------------------------+
|            LAUNCH VEHICLE LANDSCAPE (2025)                        |
|   Physics constraints → Architecture choices → Capability tiers  |
+------------------------------------------------------------------+
|                                                                  |
|  PHYSICS CONSTRAINTS                                             |
|  Δv to LEO ~9.4 km/s  →  exponential mass ratio  →  staging     |
|  Isp ceiling (chem)   →  propellant choice shapes upper stages   |
|  TWR > 1 required     →  engine count/thrust scales with GLOW    |
|       |                                                          |
|       v                                                          |
|  ARCHITECTURE CHOICES                                            |
|  Propellant   Engine cycle    Stages    Reusability              |
|  LOX/RP-1     Gas generator   2-stage   Expendable → low cost/kg |
|  LOX/LH₂      Expander        3-stage   Reusable → economics     |
|  LOX/CH₄      Full-flow SC    +boosters ISRU-compatible          |
|       |                                                          |
|       v                                                          |
|  CAPABILITY TIERS                                                |
|  SMALL (<2 t LEO)   MEDIUM (2-45 t LEO)   HEAVY (45-150+ t LEO) |
|  Electron, Alpha    Falcon 9, New Glenn    Falcon Hvy, SLS       |
|  ~$25K/kg           ~$2-5K/kg              ~$1.5-42K/kg          |
+------------------------------------------------------------------+
```

---

## Architecture Fundamentals

### Multi-Stage Rocket

```
WHY STAGING?
============

  PROBLEM: Tsiolkovsky tyranny
    To reach LEO (Δv ~9.4 km/s), you need a large mass ratio
    Single stage: must carry empty first-stage tanks all the way to orbit
    Those empty tanks are dead mass reducing efficiency

  SOLUTION: STAGING
    Drop the empty first stage; lighter second stage achieves remaining Δv
    Each stage has its own engines + tanks; discarded when empty
    Δv_total = Δv₁ + Δv₂ + Δv₃  (additive from each stage)

  EXAMPLE: FALCON 9 (2 stages + payload)
    +------------------------+
    |        Payload         | ~22.8 t to LEO capacity
    | (fairing or Dragon)    |
    +------------------------+
    |    STAGE 2 (upper)     | Single Merlin Vacuum (MVac)
    |    LOX/RP-1            | Δv ~ 5-6 km/s (varies)
    |    ~113 kN thrust      |
    +------------------------+
    |    STAGE 1 (booster)   | 9 × Merlin (890 kN each)
    |    LOX/RP-1            | Total ~8 MN sea level
    |    Landing legs + fins |
    +------------------------+

  STAGING MASS FRACTIONS (approximate for two-stage):
    Propellant mass: 85-90% of total stage mass
    Structure + engines: 5-10%
    Payload (final stage only): 1-5%
    → For Falcon 9: ~500 t GLOW; 22.8 t to LEO = ~4.5% to LEO

  MASS FRACTION RULE:
    Good rocket: propellant mass / total mass > 0.85-0.90
    This leaves 10-15% for structure + engines — engineering challenge
    Lightweight tanks (Al-Li alloys, carbon fiber composites) are critical
```

---

## Key Launch Vehicles: History

```
HISTORICAL MILESTONES
======================

  EARLY MISSILES (1940s-1950s):
    V-2 (Germany, 1944): first liquid rocket to reach space (80+ km altitude)
    R-7 (USSR, 1957): Sputnik launch vehicle; first ICBM; basis for Soyuz
    Atlas (USA, 1957): first American ICBM; still evolved in Atlas V

  HUMAN SPACEFLIGHT ERA (1960s-1970s):
    SATURN V (1967-1973):
      3 stages; LOX/RP-1 (S-IC) + LOX/LH₂ (S-II) + LOX/LH₂ (S-IVB)
      LEO capacity: 140 t; TLI: 48.6 t
      GLOW: 2970 t; Height: 110 m
      5 × F-1 engines (first stage): each 6.7 MN; total 33.5 MN
      13 missions (1967-1973); no failures (no Saturn V launch ever failed)

    SOYUZ (1966-present):
      Continuous operation; 1900+ launches
      Most reliable launch vehicle ever; based on R-7 ICBM
      Still operational in 2025 for crewed missions (Soyuz MS)

  SHUTTLE ERA (1981-2011):
    SPACE SHUTTLE SYSTEM:
      Partially reusable: Orbiter + SRBs reused; External Tank discarded
      3 × RS-25 main engines (LOX/LH₂): 2279 kN each
      2 × SRBs: 12.5 MN each (solid propellant)
      LEO payload: ~24 t (to ISS inclination)
      Costly: ~$1.5B/flight; 135 missions; 2 losses (Challenger, Columbia)
```

---

## Current Major Launch Vehicles

```
ACTIVE HEAVY LAUNCH VEHICLES (2025)
======================================

  FALCON 9 (SpaceX):
    Type: 2-stage; reusable (1st stage)
    Propellants: LOX/RP-1 (both stages)
    Engines: 9 × Merlin (S1) + 1 × Merlin Vac (S2)
    LEO: 22.8 t (expendable); ~17 t (reuse)
    GTO: 8.3 t; GEO direct: ~4.3 t
    GLOW: ~549 t; Height: 70 m
    Launch cost: ~$67M (list); actual ~$50-60M with reuse
    Reliability: 99.3% success rate (as of 2024)
    Launch frequency: ~90/year (2024); most in history

  FALCON HEAVY (SpaceX):
    Type: 3 × Falcon 9 cores; all reusable
    LEO: 63.8 t; GTO: 26.7 t; Mars: ~16.8 t
    3 × 9 Merlin engines = 27 engines total
    Cross-feed center core to side boosters (can)
    Notable: Tesla Roadster launch (2018); Arabsat-6A, AFSPC-44

  SLS BLOCK 1 (NASA):
    Type: Expendable; 2 stages + SRBs
    Core stage: LOX/LH₂; 4 × RS-25 (SSME heritage)
    SRBs: 2 × Northrop Grumman solid boosters (evolved shuttle SRBs)
    Upper stage: Interim Cryogenic Propulsion Stage (Centaur-based) → in Block 2: Exploration Upper Stage
    LEO: 95 t; TLI: 27 t
    Cost per launch: ~$4B (FY2022); extremely expensive
    Artemis 1 (2022): unmanned; Artemis 2 (2025): crewed lunar flyby

  STARSHIP (SpaceX):
    Type: 2 stages; both fully reusable
    Super Heavy (S1): ~33 × Raptor; LOX/CH₄
    Starship (S2/upper): 6 × Raptor (3 vac + 3 SL); LOX/CH₄
    LEO: 150+ t (expendable); potentially 100 t reusable
    GLOW: ~5000 t (fully fueled); Height: 121 m
    Key: refueling in LEO for deep space; full reusability goal
    Status (2025): extensive test program underway; integrated flights in 2023-2024

  NEW GLENN (Blue Origin):
    Type: 2-stage; reusable (1st stage)
    Propellants: Stage 1: LOX/LNG (methane-like, BE-4 engines)
                 Stage 2: LOX/LH₂ (BE-3U engine)
    Engines: 7 × BE-4 (S1, LOX/LNG, 2.4 MN each); 2 × BE-3U (S2, LOX/LH₂)
    LEO: 45 t; GTO: 13 t
    First launch: January 2025 (commercial payload)
```

---

## Small Launch Vehicles

```
SMALL AND MICRO LAUNCH VEHICLES
=================================

  DRIVER: CubeSat revolution + smallsat constellations
  Challenge: rideshare (cheap) vs dedicated (flexibility)

  ROCKET LAB ELECTRON:
    Two stages; LOX/RP-1; Rutherford engines (electric pump-fed!)
    LEO: 300 kg; GTO: 200 kg
    Launch cost: ~$7.5M per launch
    Battery-powered turbopump: unique; no gas generator
    Recovering fairing and first stage (helicopter catch) → partial reuse
    30+ flights; high reliability for class

  RELATIVITY SPACE TERRAN:
    3D-printed rocket (85% by mass); Aeon R engine
    Terran 1: flew once (2023), reached space but failed to orbit
    Terran R: reusable; 23.5 t to LEO; under development

  FIREFLY ALPHA:
    2-stage; LOX/RP-1; 4 × Lightning engines (aerospike-like)
    LEO: 1 t; GTO: 630 kg; ~$15M
    First successful launch Oct 2022 (after anomaly in first attempt)

  VEGA-C (ESA/Arianespace):
    4-stage (3 solid + liquid fourth stage)
    SSO: 2.2 t; good for small science + Earth obs
    P120C solid first stage: also used on Ariane 6 strap-ons

  RIDE-SHARE REVOLUTION:
    SpaceX Transporter missions: hundreds of payloads per launch
    ~$5,500/kg to SSO (2024) — commoditizing small launch
    Drove small dedicated launchers to cost-competitiveness challenge
```

---

## Fairing and Payload Accommodation

```
PAYLOAD INTEGRATION
====================

  LAUNCH VEHICLE INTERFACE:
    Payload sits atop upper stage; separated after orbit insertion
    Separation systems: marmon clamp, split nuts, hot gas systems
    Loads: axial/lateral acceleration during launch (up to 6G)
    Vibro-acoustic environment: 140+ dB during ascent (structural/acoustic)

  PAYLOAD FAIRING:
    Aerodynamic nose cone protecting payload during ascent
    Jettisoned at ~110 km altitude (atmosphere negligible)
    Falcon 9 fairing: 5.2 m diameter; 13.9 m length
    SpaceX recovers fairings by boat catch (Shenna/Doug) → save ~$6M each
    Clean room maintained inside fairing during integration

  INTERFACE DIMENSIONS (standard sizes):
    Small: 937 mm ISD (Electron); 1.0 m diameter
    Medium: 3.75 m fairing ID (Atlas V 4m)
    Large: 4.6 m ID (Falcon 9); 5 m ID (Falcon Heavy, SLS)
    Super heavy: 8+ m planned (Starship payload bay)

  PAYLOAD SEPARATION:
    Marmon clamp: ring held by explosive bolts; releases
    Lightband: spring-loaded deployer for CubeSats
    Star-48: kick stage for high-energy destinations (GEO, planetary)
```

---

## Launch Site Infrastructure

```
LAUNCH SITE CONSIDERATIONS
============================

  LATITUDE ADVANTAGE:
    Lower latitude → more Earth rotational velocity contribution
    Equatorial: 465 m/s eastward free ΔV (vs polar: 0)
    Kennedy Space Center (28.5°N): 408 m/s
    Vandenberg SFB (34.7°N): 397 m/s; SSO polar preferred
    JAXA Tanegashima (30.4°N): 430 m/s

  LAUNCH DIRECTION CONSTRAINTS:
    Cannot overfly populated areas (range safety)
    Kennedy: can't go north (US mainland); east/northeast open
    Vandenberg: south or northwest (Pacific); polar/retrograde

  LAUNCH FACILITIES:
    LC-39A (Kennedy): Apollo, Shuttle, Falcon 9/Heavy, Starship (planned)
    LC-40 (CCSFS): Falcon 9 primary
    SLC-4E (Vandenberg): Falcon 9 West Coast polar/SSO
    SLC-40 / SLC-41: Atlas V; Vulcan (ULA)
    Boca Chica (Starbase): SpaceX Starship launch/landing facility

  LAUNCH SCRUB CRITERIA:
    Weather: clouds, lightning, high altitude winds, anvil clouds
    Range safety: aircraft/ship exclusion zones
    Vehicle health: telemetry, countdown go/no-go criteria
    Weather hold: aircraft abort + lighting hold → common delays
```

---

## Decision Cheat Sheet

| Question | Answer |
|---|---|
| Why can't we just use a single-stage rocket to orbit? | Mass fraction requirements make single-stage-to-orbit (SSTO) extremely difficult; you'd need 90%+ propellant fraction leaving almost nothing for structure and payload; staging improves this by discarding dead mass |
| What payload class does Falcon 9 cover? | Medium lift: 22.8 t to LEO (expendable); ~16-17 t reusable; covers most commercial GEO, government LEO, ISS cargo, small constellations |
| What is SLS for? | NASA's Space Launch System; designed for Artemis lunar program; very high payload capacity (95 t to LEO); extremely expensive ($4B/launch); not designed to be competitive commercially |
| How does Starship differ architecturally? | Both stages fully reusable; methane propellant (ISRU on Mars); enormous payload capacity (150 t); in-space refueling for deep space; stainless steel (heat management) |
| What drove small launch vehicle development? | CubeSat + smallsat revolution; dedicated launch (vs rideshare) for schedule flexibility; but SpaceX Transporter rideshare at $5,500/kg has undercut many small launchers |
| Why does launch latitude matter? | Earth's rotational velocity contributes free ΔV for equatorial orbits; lower latitude = more eastward velocity; Kourou (French Guiana, 5°N) is better than Kennedy (28.5°N) for GEO |

---

## Engineering Parallels

**Staging as pipeline decomposition.** A multi-stage rocket is a decomposed pipeline where each stage is optimized for its flight regime and then discarded. Stage 1 runs at high thrust, low altitude, high aerodynamic stress — optimized for that regime. Stage 2 runs in near-vacuum at lower thrust, different nozzle expansion ratio, and lighter structure. You cannot merge them into one stage without compromising both regimes, exactly as you cannot merge a batch ingestion layer with a real-time serving layer without degrading both.

**Expendable vs. reusable as capex/opex model transition.** The shift from expendable launch vehicles (buy hardware, use once, expense entirely to one launch) to reusable vehicles (amortize hardware cost over N flights) is structurally identical to the on-premises-to-cloud transition. An expendable rocket is a dedicated server: full hardware cost allocated to a single use, written off immediately. A reusable rocket with 20+ flights is infrastructure amortized over a fleet. The marginal cost of the 20th flight is close to propellant + labor — equivalent to the marginal cost of an additional cloud tenant. SpaceX's vertical integration creates the same structural advantage as owning the datacenter: no external margin, faster iteration, full-stack optimization.

**Launch vehicle selection as a build-vs-buy trade.** Rideshare (Transporter missions, $5,500/kg) vs. dedicated launch is the same build-vs-buy analysis as shared vs. dedicated infrastructure. Rideshare is cheaper per kg but constrained in orbit, schedule, and interface. Dedicated is more expensive but provides full control. The economics invert when your schedule, orbit, or interface requirements cannot be satisfied by the shared pool — the same threshold at which a tenant moves from shared hosting to a dedicated instance.

## Common Confusion Points

**Expendable vs reusable costs**: Expendable Falcon 9 costs ~$67M list. But SpaceX barely uses expendable; the reusability is what drives their economics (production costs + refurbishment << new rocket). The "savings" from reuse aren't passed to customers dollar-for-dollar — SpaceX captures the margin for R&D and profit.

**Atlas V uses a Russian engine (RD-180)**: The Atlas V main engine (RD-180) was a Russian-American collaboration since the 1990s. This became politically complicated after 2022 (Russia-Ukraine war). ULA's replacement is Vulcan Centaur with Blue Origin BE-4 engines. The transition represents a major shift in US launch infrastructure.

**Thrust ≠ capability**: Saturn V had 33.5 MN thrust and 140 t to LEO. Starship has ~70-80 MN thrust (full stack) and aims for 150+ t. But thrust alone doesn't determine payload — the entire mass ratio, Isp, and staging strategy determine payload fraction.

**Rideshare is not always cheaper for the customer**: Rideshare (sharing a launch with many others) is cheap per kg but you must wait for a launch that goes to your desired orbit at the right time. Dedicated launch costs more per kg but guarantees the orbit and schedule you need. For constellations, rideshare works; for time-sensitive or unique orbit requirements, dedicated is necessary.
