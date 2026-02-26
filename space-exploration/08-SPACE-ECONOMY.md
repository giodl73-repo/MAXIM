# Space Economy: Commercial Space and New Space

## The Big Picture

The space economy has undergone a structural transition since ~2010. Prior paradigm: government agencies as primary operators, contractors building cost-plus hardware at government direction. New paradigm: commercial operators as primary customers and operators, government as anchor tenant and regulator. The driver is cost reduction through competition and reusability — launch costs dropped roughly 10× in 15 years.

```
+------------------------------------------------------------------+
|                    SPACE ECONOMY STRUCTURE (2025)                |
+------------------------------------------------------------------+
|                                                                  |
|  UPSTREAM                                                        |
|  Launch services: SpaceX, ULA, Rocket Lab, Arianespace, ISRO    |
|  Satellites: Airbus DS, Ball Aerospace, Maxar, Lockheed, Surrey  |
|  Ground systems: Harris, Kratos, Amazon AWS Ground Station       |
|                                                                  |
|  MIDSTREAM (infrastructure)                                      |
|  Satellite constellations: Starlink, OneWeb, Amazon Kuiper       |
|  GPS/GNSS: US DoD (GPS), EU (Galileo), Russia (GLONASS), CN (BDS)|
|  Relay/TDRSS, lunar comm (upcoming)                              |
|                                                                  |
|  DOWNSTREAM (applications)                                       |
|  Earth observation: Planet, Maxar, Airbus, Satellogic            |
|  Communications: direct-to-device, maritime, aviation            |
|  Navigation/PNT: every GPS chip, precision agriculture           |
|  Weather: NOAA, ESA, private (Spire, Tomorrow.io)               |
|                                                                  |
|  EMERGING                                                        |
|  Space tourism: Blue Origin, Virgin Galactic, SpaceX             |
|  In-space manufacturing: Varda, Space Forge, Redwire             |
|  Cislunar economy: Gateway, commercial lunar payload services     |
|  Asteroid mining: AstroForge, early development                  |
+------------------------------------------------------------------+

  Total space economy (2024 estimate): ~$630B/yr
  Launch services: ~$10B (small fraction of total)
  Satellite services: ~$140B
  Ground equipment: ~$170B
  Navigation/GPS downstream: ~$300B (GPS contributes ~$300B to US GDP alone)
```

---

## Launch Market Structure

```
COMMERCIAL LAUNCH MARKET
==========================

  MARKET SEGMENTS:
    Government/Civil: NASA, ESA, JAXA, national agencies; typically cost-plus contracts
    Commercial GEO: telecom satellites; stable demand; $200-400M satellites
    Commercial LEO: constellation deployment (biggest growth); rideshare/batch
    Defense: DoD, NRO, Space Force; national security; strict vendor qualification
    Smallsat/NewSpace: CubeSats, tech demos; rideshare or dedicated small launch

  PRICE BENCHMARKS (2024):
    Falcon 9 list:     ~$67M    (22.8 t to LEO)       = ~$2,900/kg
    Falcon Heavy:      ~$97M    (63 t to LEO)         = ~$1,500/kg
    Rocket Lab Electron: ~$7.5M (0.3 t to LEO)        = ~$25,000/kg
    Ariane 6:          ~$100M   (10.3-21 t to LEO)    = ~$5-10K/kg
    SpaceX Transporter rideshare: ~$5,500/kg (SSO)
    ISRO PSLV:         ~$15-25M (varies)
    SLS:               ~$4B     (95 t; NASA internal) = ~$42,000/kg

  MARKET CONCENTRATION:
    SpaceX: ~80%+ of commercial orbital launches by 2024
    Most launches worldwide are SpaceX Falcon 9
    Remaining market: ULA, Rocket Lab, Arianespace, ISRO, JAXA, CASC

  LAUNCH FREQUENCY (2024 approximate):
    SpaceX: ~90 launches/year (dominant by far)
    Global total: ~210-250 launches (most in history; growing)
    Chinese launches: ~65-70/yr (CASC + commercial)
    Other Western: ~25-30 launches combined

  COMPETITIVE DYNAMICS:
    New entrants struggling: Ariane 6 delayed; ULA Vulcan late; Virgin Orbit bankrupt (2023)
    SpaceX competitive moat: integrated manufacturing, reuse, vertical integration
    China growing fast: government-backed; not competing directly for Western commercial
    Small launch: SpaceX rideshare at $5,500/kg undercuts dedicated small launchers
    Consolidation expected: many small launchers will not survive
```

---

## Satellite Constellations

```
MEGA-CONSTELLATION ECONOMICS
==============================

  STARLINK (SpaceX):
    Goal: global broadband internet from LEO
    Constellation: 5,000+ operational (2024); licensed for 40,000+
    Altitude: ~550 km (Shell 1) + ~340 km (Gen2)
    Coverage: global (with polar orbit inclinations)
    Latency: ~20-40 ms (vs GEO: 600 ms); competitive with terrestrial fiber
    User terminal: $499 + $120/month (residential, 2024)
    Revenue model: subscriptions; maritime; aviation; enterprise; military (Starshield)

    ECONOMICS:
      Satellite cost: ~$500K-1M each (estimated; SpaceX won't say)
      5,000 sats: ~$5B capital cost (plus $10B+ R&D for Starlink + Falcon)
      Per-satellite launch cost: effectively ~free (SpaceX self-launches in batches of 20-60)
      Operating expenses: ground stations, spectrum, customer support
      Revenue: ~$3-4B/yr (2024 estimated); growing rapidly

  AMAZON KUIPER:
    Goal: Compete with Starlink
    Constellation: 3,236 satellites licensed
    Status: prototype launches 2023; commercial deployment 2025+
    Launch: mixed (Atlas V, Vulcan, Ariane 6, Blue Origin New Glenn)
    Amazon's advantage: AWS integration, enterprise cloud market
    Investment: ~$10B committed

  ONEWEB (now Eutelsat OneWeb):
    Constellation: ~648 satellites operational (full LEO complement)
    Focus: enterprise, government, maritime/aviation
    History: bankrupt 2020 → rescued by UK government + Bharti Airtel
    Merged with Eutelsat (GEO operator) 2023; troubled combination

  TELESAT LIGHTSPEED (Canada):
    298 satellites; enterprise focus; Canada government backed
    Delayed; financing challenges

  CHINESE CONSTELLATIONS:
    Guowang (CASCO/SatNet): 13,000 satellites licensed (rival to Starlink)
    Honghu-3: 10,000+ planned
    SpaceSail: Qianfan constellation
    Significant national investment; not available to Western markets

  SPECTRUM AND REGULATORY:
    ITU (International Telecommunication Union): coordinates radio spectrum + orbits
    Coordination: operators must coordinate to avoid interference
    Orbital debris: growing concern; SpaceX files for frequent deorbit capability
    Kessler syndrome risk: cascading debris if major constellation collision
    Astronomy impact: Starlink trails visible in long-exposure telescope images
```

---

## Earth Observation

```
COMMERCIAL EARTH OBSERVATION (EO) MARKET
==========================================

  MARKET VALUE: ~$4-5B/yr and growing

  OPTICAL IMAGERY:
    Resolution tiers:
      Sub-meter (0.3-1m): DigitalGlobe/Maxar (WorldView-3: 0.31m); government contracts
      Medium (1-5m): commercial standard; Planet (Dove: 3m)
      Coarse (10-500m): free (Sentinel-2: 10m; Landsat: 30m)
    Planet Labs: 200+ Dove CubeSats; daily global revisit at 3-5m
    Maxar: highest-res commercial; dominates US government (NRO) contracts
    Airbus Defence: Pleiades Neo (0.3m); European focus

  SAR (Synthetic Aperture Radar):
    Penetrates clouds; day/night capable; different information than optical
    ICEYE: SAR CubeSats; near-real-time; Finland-based
    Capella Space: X-band SAR; 0.5m resolution; US
    Synspective: L-band SAR; ground deformation monitoring

  HYPERSPECTRAL:
    Many wavelength bands (hundreds vs 3-4 RGB)
    Material identification: agriculture, mining, environmental monitoring
    HyperScout: ESA startup; Planet + Satellogic developing

  ANALYTICS LAYER:
    Raw imagery is commoditizing → value moves to analytics
    Change detection: AI/ML to flag what changed since last image
    Customers: agriculture (crop monitoring), insurance, defense intelligence,
               real estate, shipping, emergency response
    Platforms: Google Earth Engine, AWS Geospatial, Planet Analytics

  BUSINESS MODEL SHIFT:
    Old: sell large imagery archives; long procurement cycles (government)
    New: subscription (daily revisit); tasking-as-a-service; API access
    Planet: "time series > individual images"; agriculture subscriptions
    Maxar/NRO: long-term government contracts ($0.5B+/yr total)
```

---

## Space Tourism

```
COMMERCIAL HUMAN SPACEFLIGHT
==============================

  SUBORBITAL TOURISM:
    BLUE ORIGIN NEW SHEPARD:
      110 km altitude (Kármán line); ~11 min flight; 3 min weightlessness
      Capsule: 6 passengers; automated (no pilot needed in capsule)
      Price: $450K-$500K per seat (estimated; not publicly disclosed)
      First crewed flight: July 20, 2021 (Jeff Bezos + crew)
      Status: multiple tourist flights; grounded 2022-2023 for engine anomaly; resumed

    VIRGIN GALACTIC SPACESHIPTWO:
      VSS Unity: air-launched from WhiteKnightTwo mothership
      Spaceplane design (not capsule); glides back; horizontal landing
      Altitude: ~86-90 km (below Kármán line per FAI; above US Air Force 80 km line)
      6 passengers + 2 pilots
      Price: $450K-$600K (Delta class tickets)
      Status: first commercial flights 2023; multiple flights; production gaps
      Next: SpaceShipIII (Delta class); higher flight rate goal

  ORBITAL TOURISM:
    SPACEX INSPIRATION4 (2021):
      First all-civilian orbital mission (SpaceX Crew Dragon)
      4 passengers; 3-day orbit at 585 km altitude
      Chartered by Jared Isaacman (Shift4 Payments CEO) for ~$200M estimate

    SPACEX POLARIS PROGRAM:
      Series of missions funded by Jared Isaacman
      Polaris Dawn (2024): first commercial spacewalk; crew EVA in Dragon suits
      Polaris 2-3: planned follow-ons

    AXIOM SPACE:
      Private ISS missions: Ax-1 (2022), Ax-2, Ax-3, Ax-4
      ~$55M/seat to NASA for Crew Dragon + ISS stay
      Long-term goal: private space station (Axiom Station, attaching to ISS, then standalone)
      Business model: luxury stations, microgravity R&D, film/media in space

    SPACEX DEARYMOON (YUSAKU MAEZAWA):
      Lunar flyby mission aboard Starship
      Japanese entrepreneur chartered entire flight
      Status: delayed with Starship development timeline

  MARKET ASSESSMENT:
    True mass market: decades away (price must drop 100× from $450K)
    Near-term: ultra-high-net-worth individuals; government astronauts on commercial vehicles
    Growing: in-flight entertainment, media rights, brand sponsorship of missions
    Risk: high-profile accident would severely set back market
```

---

## In-Space Economy

```
IN-SPACE MANUFACTURING AND RESOURCES
======================================

  IN-SPACE MANUFACTURING:
    VARDA SPACE INDUSTRIES:
      Satellite with processing capsule; manufacture in microgravity; return to Earth
      Focus: pharmaceuticals (crystal growth), fiber optic cables, semiconductors
      First capsule: returned 2024 (Utah desert landing)
      Advantage: protein crystal growth produces better drug formulations in microgravity
      Challenge: regulatory (FAA capsule reentry; FDA pharmaceutical approval in orbit)

    SPACE FORGE (UK):
      Semiconductor manufacturing in space
      Reusable reentry vehicle concept
      Status: early stage; 2022 launch failure

    REDWIRE SPACE:
      3D printing in space; plant growth; bioprinting
      MADE IN SPACE heritage (acquired)
      Operates facilities aboard ISS

    ECONOMICS OF IN-SPACE MANUFACTURING:
      Only viable if: (1) product has unique microgravity properties AND
                      (2) value/kg is extremely high (pharmaceuticals: $1M+/kg vs $10K/kg launch cost)
      Most manufacturing: NOT viable in space for Earth consumption
      Exception: space infrastructure built in space (solar panels, structures)
                 → no need to pay Earth-to-LEO launch cost to lift finished product

  ASTEROID MINING:
    RESOURCE POTENTIAL:
      M-type (metallic) asteroids: iron-nickel + PGMs (platinum group metals)
      C-type (carbonaceous): water (H₂O) → in-space propellant feedstock
      16 Psyche (metallic): estimated $10^19 value (but this is nonsensical — markets would collapse)

    WATER AS PROPELLANT:
      Electrolysis → H₂ + O₂ → rocket propellant
      Extracted at asteroid or lunar poles → propellant depot → refuel deep space missions
      Economics: launch cost from Earth for propellant: ~$20,000/kg to GEO
      Space-sourced propellant: potentially $500-2000/kg (break-even point for mining)

    COMPANIES:
      AstroForge: asteroid mining focus; launched refinery demo 2024
      TransAstra: optical mining concept
      Previous ventures: Planetary Resources, Deep Space Industries — both failed / acquired
      Challenge: decades-away technology; capital-intensive; no revenue path

    LEGAL FRAMEWORK:
      Outer Space Treaty (1967): prohibits national appropriation of celestial bodies
      US Commercial Space Launch Competitiveness Act (2015): US citizens can own
        resources extracted from celestial bodies (controversial interpretation)
      Luxembourg Space Law (2017): similar rights framework
      No international consensus on property rights

  LUNAR ECONOMY:
    ARTEMIS COMMERCIAL LUNAR PAYLOAD SERVICES (CLPS):
      NASA contracts commercial vendors to deliver payloads to Moon surface
      Vendors: Astrobotic, Intuitive Machines, Firefly, others
      CLPS delivery cost: $1-2B per delivery vs NASA direct cost
      Goal: build commercial lunar transportation market

    IN-SITU RESOURCE UTILIZATION (ISRU):
      Lunar water ice (south pole permanently shadowed craters): high confidence
      Mining water → oxygen for breathing + propellant production on Moon
      Lunar regolith: can produce oxygen via molten electrolysis; structural material
      NASA Artemis goal: demonstrate ISRU before 2030

    CISLUNAR ECONOMY MODEL:
      Earth → LEO: Starship / New Glenn (cheap access)
      LEO depot → lunar surface: small upper stages + landers
      Surface: mining, construction, fuel production, science
      Timeline: commercial cislunar economy 2030s+ (optimistic scenario)
```

---

## Government Policy and Investment

```
NATIONAL SPACE POLICIES AND PROGRAMS
======================================

  US SPACE POLICY:
    NASA AUTHORIZATION:
      Annual budget: ~$24-25B (2024)
      Science: ~$8B; Human exploration: ~$7B; Space operations (ISS): ~$4B
      Aeronautics: ~$1B; STEM/other: ~$1B
      Significant: NASA budget is ~0.3% of federal budget (peak Apollo: ~4%)

    SPACE FORCE:
      Established 2019; 6th military branch
      Budget: ~$30B/yr (2024)
      Focus: satellite communications, GPS, missile warning, space domain awareness
      National Security Space: launch (NSSL contracts), on-orbit operations, cyber

    COMMERCIAL CREW / CARGO MODEL:
      Shift from cost-plus to fixed-price competitive contracts → cost reduction demonstrated
      Commercial Crew: Dragon ($55M/seat) vs Starliner (>$90M/seat)
      Lesson: competition + fixed-price + milestone payments → lower costs
      Applied to: HLS lunar lander (SpaceX Starship HLS won), Gateway, CLPS

  CHINA SPACE PROGRAM (CNSA):
    Budget: ~$10-15B/yr (official; actual higher with military integration)
    Crewed: Tianhe space station; Shenzhou; Long March 5B
    Moon program: Chang'e series (Chang'e-6: far side sample return 2024)
    Mars: Tianwen-1 (2021) — orbiter + lander + rover (Zhurong)
    Vision: crewed Moon landing before 2030; Mars 2030s
    Commercial: CASC (state) + growing commercial sector (Landspace, etc.)

  ESA:
    Budget: ~€7.8B/yr (2024)
    Member states: 22 countries
    Key programs: Ariane 6, Galileo (GNSS), Copernicus (EO), ExoMars, JUICE
    Challenge: Ariane 6 late; reliance on Soyuz ended 2022; now using SpaceX
    Science: JWST partner; Euclid (dark energy/matter); Hera (asteroid deflection)

  JAPAN (JAXA):
    Budget: ~$2B/yr
    H3 rocket: finally achieved orbit 2024 (after initial failure)
    Hayabusa2: Ryugu asteroid sample return (2020) ← landmark mission
    SLIM: precision Moon lander (2024) — pinpoint landing demo
    Lunar Gateway partner

  INDIA (ISRO):
    Budget: ~$1.5B/yr
    Chandrayaan-3: lunar south pole landing (2023) — first successful soft landing near pole
    Aditya-L1: solar observatory (Lagrange L1, 2023)
    Gaganyaan: crewed spacecraft (uncrewed demo 2023; crewed planned 2025)
    PSLV: commercial launch success; low-cost reliable medium launcher

  REGULATORY ENVIRONMENT:
    FAA Office of Commercial Space: US launch licensing, reentry, safety
    ITU: spectrum and orbit coordination
    NOAA: Earth observation licensing in US
    FCC: satellite communication spectrum
    Outer Space Treaty (1967): no sovereignty; peaceful purposes; liability
    Key gaps: asteroid mining rights, debris mitigation, lunar resource rights
```

---

## Decision Cheat Sheet

| Question | Answer |
|---|---|
| What is the actual size of the space economy? | ~$630B/yr globally (2024); dominated by satellite services (~$140B) and GPS downstream ($300B); launch itself is only ~$10B — the small upstream fraction |
| Why does GPS contribute ~$300B to US GDP? | GPS underlies precision agriculture, fleet logistics, financial transaction timing (millisecond synchronization), rideshare, emergency services; users pay nothing but the economic value is enormous |
| Who dominates commercial launch? | SpaceX: ~80%+ of commercial launches globally by 2024; Falcon 9 reliability + pricing + cadence created near-monopoly; major challengers (Ariane 6, New Glenn, Vulcan) finally operational in 2024-2025 |
| What is Starlink's revenue model? | Subscriptions: residential ($120/mo), maritime (~$5K/mo), aviation, enterprise, military (Starshield); ~$3-4B/yr 2024; SpaceX finances launch operations partly through Starlink cash flow |
| Why is in-space manufacturing only viable for high-value products? | Launch cost is ~$3,000-10,000/kg; in-space manufacture only beats Earth manufacture if (1) microgravity uniquely improves product AND (2) value/kg >> launch cost; pharmaceuticals qualify; steel does not |
| What legal framework governs asteroid mining? | No settled international law; US (2015) and Luxembourg (2017) laws allow citizens to own extracted resources; Outer Space Treaty prohibits national sovereignty; no international consensus; significant legal risk for capital investment |
| What is the CLPS model? | Commercial Lunar Payload Services: NASA pays commercial vendors fixed price to deliver payloads to Moon; vendors retain design ownership; goal is to build lunar commercial market rather than NASA owning logistics |

---

<!-- @editor[bridge/P2]: No explicit old-world bridge section — the content implicitly bridges (cost-plus vs fixed-price, platform economics) but deserves a dedicated bridge callout: the shift from cost-plus to fixed-price competitive contracts is the same shift the learner saw from waterfall government IT procurement to cloud marketplace models; Starlink's platform economics mirror Azure's infrastructure-as-a-service model -->
## Common Confusion Points

**Launch cost is not the dominant cost in space**: Launch is $3,000-10,000/kg but is just a fraction of the value. GPS downstream is worth 30× the entire launch market. Satellite services are 14× the launch market. Launch cost matters for mission feasibility but "space economy" is mostly about applications, not getting there.

**Starlink is not just internet**: It's also serving maritime (ships), aviation (aircraft), enterprise, and military markets (Starshield is a classified variant). The consumer internet is the headline; military and enterprise contracts may eventually be larger revenue sources. Ukraine's use of Starlink in 2022-present demonstrated strategic value.

**Commercial and government space are not separate sectors**: NASA's Commercial Crew contracts fund SpaceX's capabilities. SpaceX's government revenue (NASA, DoD) is substantial. "NewSpace" companies are often sustained by government contracts while building commercial markets. The distinction is contract type (fixed-price competitive vs cost-plus directed) more than funding source.

**Debris is an externality problem, not solved by the market**: Individual operators benefit from launching satellites; the debris risk is shared by all operators and is not internalized by the deployer. This is a classic tragedy-of-the-commons. Starlink's sheer scale (~5,000+ satellites) creates collision risk that threatens other orbits. Market forces alone won't fix this; international coordination is required.

**Space tourism price will not drop 10× in 10 years**: Current suborbital tourism at $450K is analogous to early commercial aviation. Mass market aviation took 50 years of incremental technology improvement. Orbital tourism at $450K/seat reflects actual marginal cost of a Crew Dragon seat (Axiom charges NASA ~$55M for 4 people = ~$14M/seat; tourist markup). True mass market requires order-of-magnitude cost reduction in spacecraft + life support amortization.
