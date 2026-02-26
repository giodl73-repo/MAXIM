# Space Exploration — Landscape and Taxonomy

## The Big Picture

Space exploration is the application of physics, engineering, and systems design to put objects and humans beyond Earth's atmosphere. The physics is orbital mechanics and propulsion; the engineering is reliability under extreme conditions; the systems challenge is the hardest integration problem humans routinely tackle.

<!-- @editor[diagram/P2]: Diagram lists items in columns but doesn't show how physics feeds engineering feeds operations — rework as layered system view with flow arrows -->
```
+------------------------------------------------------------------+
|                    SPACE EXPLORATION LANDSCAPE                    |
+------------------------------------------------------------------+
|                                                                  |
|  PHYSICS               ENGINEERING             OPERATIONS        |
|  -------               -----------             ----------        |
|  Orbital mechanics     Launch vehicles         Mission design    |
|  Propulsion theory     Spacecraft design       Ground control    |
|  Radiation physics     Thermal control         Navigation        |
|  Celestial mechanics   Power systems           Communications    |
|  Atmospheric entry     Life support            Data handling     |
|                                                                  |
|  ERA / ACTOR           CAPABILITY              MARKET            |
|  ----------            ----------              ------            |
|  Government (NASA,ESA) Science missions        Government        |
|  Legacy launch (ULA)   Human spaceflight       Commercial        |
|  New Space (SpaceX)    Reusable rockets        Civil             |
|  Commercial smallsats  Megaconstellations      Defense           |
+------------------------------------------------------------------+
```

---

## Historical Eras

```
SPACE AGE TIMELINE
==================

  ERA 1: RACE TO SPACE (1957-1969)
    1957: Sputnik 1 (USSR) — first satellite
    1961: Gagarin — first human in space; Freedom 7 (Shepard) — first American
    1965: Mariner 4 — first Mars flyby images
    1969: Apollo 11 — first lunar landing

  ERA 2: COLD WAR PROGRAMS (1969-1991)
    Apollo 12-17; Skylab; Mir; Salyut; Viking; Voyager; Pioneer
    Space Shuttle (1981-2011); 135 flights; Challenger (1986), Columbia (2003)

  ERA 3: INTERNATIONAL STATION (1993-2020s)
    ISS assembly (1998-2011); permanent crew since 2000
    Hubble Space Telescope; Cassini; Mars Odyssey; MER; MSL
    Commercial Crew (2020): SpaceX Crew Dragon first operational commercial crew

  ERA 4: NEW SPACE (2010s-present)
    SpaceX Falcon 9 reusability (2015 first booster landing)
    SpaceX Crew Dragon (2020 first crewed commercial flight)
    SpaceX Starship (first orbital attempt 2023; first full mission 2024)
    Artemis program: return to Moon; first crewed Artemis planned 2025+
    Commercial launch market: competitive; prices fallen dramatically

  ERA 5: EMERGING (2025+)
    Lunar Gateway (planned)
    Moon base concepts (Artemis sustained presence)
    Mars: SpaceX Starship; NASA concept missions
    Commercial stations (Axiom, Starlab, etc.)
```

---

## The Fundamental Numbers

```
KEY CONSTANTS FOR SPACE EXPLORATION
=====================================

  Earth surface escape velocity:   11.2 km/s
  LEO orbital velocity:             7.8 km/s  (altitude ~200-2000 km)
  GEO orbital velocity:             3.1 km/s  (altitude 35,786 km)
  Moon:  escape velocity:           2.4 km/s
  Mars:  escape velocity:           5.0 km/s

  DELTA-V BUDGET (km/s to reach):
    LEO from Earth surface:         ~9.4 km/s  (includes gravity + drag losses)
    GEO from LEO:                   ~3.9 km/s  (Hohmann)
    Lunar orbit from LEO:           ~3.1 km/s
    Lunar surface from LEO:         ~5.7 km/s  (descent)
    Mars orbit from Earth:          ~3.6-6.3 km/s  (depends on launch window)
    Mars surface from Earth:        ~13-15 km/s cumulative

  GRAVITY WELL ANALOGY:
    Getting to LEO costs as much ΔV as going halfway to anywhere in solar system
    The first ~9 km/s is the hardest part

  ROCKET EQUATION:
    Δv = Isp × g₀ × ln(m₀/mf)
    where Isp = specific impulse (seconds)
    m₀ = initial mass (full propellant)
    mf = final mass (empty)
    ln(m₀/mf) = mass ratio
```

---

## Sector Map

```
SPACE SECTOR TAXONOMY
======================

  GOVERNMENT SPACE                COMMERCIAL SPACE
  ----------------                ----------------
  Science (NASA, ESA, JAXA)       Launch services (SpaceX, RocketLab, ULA)
  Human exploration (NASA)        Satellite operators (Starlink, OneWeb)
  National security (NRO, DoD)    Earth observation (Planet, Maxar)
  Weather/Earth obs (NOAA)        Communications (SES, Intelsat, Viasat)
  Navigation (GPS, Galileo)       In-space services (Astroscale, Northrop)
  Space traffic mgmt              Space tourism (Virgin, Blue Origin, Axiom)
                                  Lunar/planetary (ispace, Astrobotic, Intuitive)

  MISSION TYPES:
  LEO:         ISS, Earth obs, Starlink (200-2000 km)
  MEO:         GPS, Galileo navigation satellites (20,000 km)
  GEO:         Communications, weather (35,786 km, geostationary)
  HEO:         Molniya, Tundra orbits (polar coverage)
  Lunar:       Orbiters, landers, rovers; L1/L2 halo orbits (Gateway)
  Interplanetary: Solar system exploration missions
  Deep space:  Voyager, New Horizons (heliospheric boundary)
```

---

## Module Map

```
00-OVERVIEW (this file)
    |
    +-- 01-ORBITAL-MECHANICS   Kepler, Hohmann, gravity assists, Δv budget
    |                          Tsiolkovsky equation, Lagrange points
    |
    +-- 02-PROPULSION          Chemical (liquid/solid), electric, nuclear
    |                          Isp, thrust, efficiency tradeoffs
    |
    +-- 03-LAUNCH-VEHICLES     Architecture, staging, historical + current
    |                          Expendable vs reusable; payload classes
    |
    +-- 04-REUSABILITY         SpaceX Falcon 9/Heavy, Starship
    |                          Economics of reusability; landing technology
    |
    +-- 05-SPACECRAFT-DESIGN   Subsystems (power, thermal, comms, ADCS)
    |                          Mass budget; radiation environment
    |
    +-- 06-MISSION-DESIGN      Interplanetary trajectory design
    |                          Launch windows, gravity assists, TCMs
    |
    +-- 07-HUMAN-SPACEFLIGHT   Physiology, life support, EVA, radiation
    |                          ISS; Artemis; Mars long-duration challenges
    |
    +-- 08-SPACE-ECONOMY       Commercial space structure; markets
    |                          Costs, launch economics, new space business models
    |
    +-- 09-FUTURE-EXPLORATION  Moon, Mars, beyond; propulsion roadmap
                               Cislunar economy; settlement concepts
```

---

## Decision Cheat Sheet

| Question | Answer |
|---|---|
| Why is getting to LEO so expensive? | ~9.4 km/s of ΔV required (gravity losses + drag + need for orbital velocity); the rocket equation means most of the rocket is propellant |
| What is LEO vs GEO vs HEO? | Low Earth Orbit (200-2000 km); Geostationary Earth Orbit (35,786 km, synchronous); High Earth Orbit (>35,786 km) |
| What was the first milestone of the "new space" era? | SpaceX Falcon 9 first-stage booster landing, December 2015 — proving orbital-class booster reuse was practical |
| What is specific impulse (Isp)? | Effective exhaust velocity ÷ g₀ = efficiency metric for rockets; higher Isp = more efficient use of propellant; chemical ~300-450 s; electric ~1500-10,000 s |
| What made commercial crew important? | Ended US dependence on Soyuz for ISS crew transport; first crewed orbital commercial flight (SpaceX Dragon) in 2020; established model for NASA as customer |

---

<!-- @editor[bridge/P2]: No old-world-to-new-world bridge anywhere in overview — natural parallel: cost-plus government contracting (VSTS-era Microsoft procurement) vs fixed-price commercial (SpaceX model) maps directly onto waterfall-vs-agile or on-prem-vs-cloud transitions the learner lived through -->
## Common Confusion Points

**Orbital velocity ≠ escape velocity**: To stay in LEO you need ~7.8 km/s (just enough centripetal balance). To leave Earth entirely you need 11.2 km/s (another ~3.4 km/s more). The rocket equation means that extra 3.4 km/s is enormously expensive in propellant.

**The space station is not "above" Earth's gravity**: ISS altitude is 408 km; Earth's gravity there is ~89% of surface gravity. The ISS and crew are in free fall (constant falling in a curve that matches Earth's curvature). Microgravity = free fall, not absence of gravity.

**"New Space" is not purely commercial**: Government agencies are major customers (NASA commercial crew, commercial cargo, SBIR grants). "New Space" means private companies own and operate the hardware, contrasted with traditional cost-plus contracts where government owned everything.
