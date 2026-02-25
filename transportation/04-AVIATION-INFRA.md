# Aviation Infrastructure

## The Big Picture

Aviation is a system of extraordinary complexity operating to extraordinarily tight tolerances. A 350-tonne aircraft must depart within minutes of schedule, navigate through 12,000 meters of atmosphere shared with thousands of other aircraft, and land within 30 metres of the centreline. The infrastructure — airports, airspace, ATC systems, and airline operations — makes this routine.

```
+------------------------------------------------------------------+
|                    AVIATION SYSTEM LAYERS                        |
|                                                                  |
|  AIRSPACE                                                        |
|  +----------+  +----------+  +----------+  +----------+         |
|  | ICAO     |  | Airways  |  | RVSM     |  | RNAV/RNP |         |
|  | Class A-G|  | Routes   |  | (1000ft  |  | (PBN     |         |
|  |          |  |          |  | sep)     |  | operations)|        |
|  +----------+  +----------+  +----------+  +----------+         |
|                                                                  |
|  ATC SYSTEMS                                                     |
|  +----------+  +----------+  +----------+  +----------+         |
|  | Primary  |  | Secondary|  | ADS-B    |  | TCAS II  |         |
|  | Radar    |  | Radar    |  | Out      |  | (RA/TA)  |         |
|  | (PSR)    |  | (SSR)    |  |          |  |          |         |
|  +----------+  +----------+  +----------+  +----------+         |
|                                                                  |
|  AIRPORT                                                         |
|  +----------+  +----------+  +----------+  +----------+         |
|  | Runway   |  | Taxiway  |  | Terminal |  | Approach |         |
|  | Design   |  | System   |  | & Apron  |  | Aids     |         |
|  +----------+  +----------+  +----------+  +----------+         |
|                                                                  |
|  AIRLINE ECONOMICS                                               |
|  +----------+  +----------+  +----------+  +----------+         |
|  | Yield    |  | Hub vs   |  | CASM /   |  | Slot     |         |
|  | Mgmt     |  | LCC      |  | RASM     |  | Coords   |         |
|  +----------+  +----------+  +----------+  +----------+         |
+------------------------------------------------------------------+
```

---

## Airport Design

### Runway Geometry and Declared Distances

Runway geometry is governed by ICAO Annex 14 and FAA Advisory Circulars. The "declared distances" system accounts for clearways and stopways.

```
  DECLARED DISTANCES (ICAO terminology):

  THRESHOLD                                    THRESHOLD
  |                                                    |
  +----------------------------------------------------+
  |            TORA (Take-Off Run Available)           |
  +----------------------------------------------------+
  |       TODA (Take-Off Distance Available)      -----|-----
                                                 Clearway (not
                                                 hard surface)
  |     ASDA (Accelerate-Stop Distance Avail.)   +------+
                                                 Stopway (paved,
                                                 cannot be used
                                                 for takeoff roll)
  LDA (Landing Distance Available):
  From displaced threshold (if applicable) to end of runway.

  KEY POINTS:
  - TODA >= TORA (clearway extends beyond runway end)
  - ASDA >= TORA (stopway can slow a rejected takeoff)
  - LDA can be less than TORA (displaced threshold)

  RUNWAY LENGTH DETERMINATION:
  Reference field length from aircraft performance manual
  Corrections for: airport elevation (less dense air)
                   temperature (ISA + correction)
                   slope (uphill increases requirement)
                   surface (wet runway factor)

  A Boeing 777-300ER at MTOW (352t):
    Sea level, ISA, dry: ~3,200m
    Denver (1,655m elev), hot day (35°C): ~4,000m+
```

### Runway Configuration and Capacity

```
  RUNWAY CONFIGURATIONS AND THEORETICAL CAPACITY:

  Single runway:
  ==============================
  Capacity: 45-60 operations/hr (mixed arrivals/departures)
  Typical: 25-30 arrivals/hr + 25-30 departures/hr

  Close parallel (< 760m separation):
  ==============================
  ==============================
  Must use dependent operations (staggered)
  Capacity: 60-75 operations/hr (shared instrument approaches)

  Far parallel (> 1,300m separation):
  ==============================
                     (1300m+ separation)
  ==============================
  Independent operations (simultaneous ILS)
  Capacity: 90-120 operations/hr (dual independent runways)

  Open-V (converging):
  =========>
          <=========
  Independent departures; arrivals must alternate
  Atlanta (ATL): 5 runways = world's highest capacity airport

  ORIENTATION:
  Runway oriented to align with prevailing wind (crosswind limit).
  Design criterion: wind rose analysis — achieve 95% coverage
  (aircraft can operate in 95% of observed wind conditions).
  ILS/GLS approaches: headwind preferred; crosswind limit ~30-40 knots.
```

### Pavement Classification

**PCN/ACN system:** Pavement Classification Number (PCN) indicates bearing strength. Aircraft Classification Number (ACN) indicates the load the aircraft imposes. Aircraft with ACN <= PCN can operate unrestricted; ACN > PCN requires special permission.

```
  PCN/ACN REPORT FORMAT:
  PCN 80 / F / B / W / T

  80  = numerical PCN value
  F   = pavement type: F (flexible/asphalt) or R (rigid/concrete)
  B   = subgrade strength category: A (high) B (medium) C (low) D (ultra-low)
  W   = tire pressure category: W (high, no limit) X Y Z (decreasing)
  T   = evaluation method: T (technical) or U (using aircraft experience)

  Example: 747-400 at MTOW has ACN ~60-80 depending on tire pressure.
  Runway PCN must be >= ACN for unrestricted operations.

  NEW SYSTEM (ICAO Annex 14, 2024): ACN/PCN -> ACR/PCR
  ACR = Aircraft Classification Rating (replaces ACN)
  PCR = Pavement Classification Rating (replaces PCN)
  Uses energy approach; more physically accurate.
```

### Instrument Approach Categories

```
  ILS APPROACH CATEGORIES:

  Category | Decision Height | RVR minimum | Notes
  ---------|-----------------|-------------|------
  CAT I    | 200ft (60m)     | 550m RVR    | Standard ILS
  CAT II   | 100ft (30m)     | 300m RVR    | Enhanced equipment req.
  CAT IIIA | <100ft or zero  | 200m RVR    | Autoland capable aircraft
  CAT IIIB | <50ft or zero   | 50-200m RVR | Reduced rollout visibility
  CAT IIIC | zero            | zero        | Rarely authorized (rollout)

  RVR = Runway Visual Range (measured at threshold)
  CAT II/III requires: autoland certified aircraft, trained crew,
                       enhanced ground equipment, low-failure runway lighting

  ALTERNATIVE APPROACH SYSTEMS:
  GLS (Ground-based Landing System): Uses GBAS (ground-based augmentation
       of GPS/GNSS). More flexible than ILS (one station serves all runway ends).
       A-SMGCS: Advanced Surface Movement Guidance and Control System
       Provides taxi guidance and surface traffic control in low visibility.
```

---

## Air Traffic Control Systems

### Surveillance Architecture

```
  ATC SURVEILLANCE LAYERS:

  1. PSR (Primary Surveillance Radar):
  +----------------------------------+
  | Transmits pulses; receives       |
  | reflections from aircraft hull   |
  | No transponder needed on aircraft|
  | Range: 80-100nm (terminal)       |
  |        200-250nm (en-route)      |
  | Shows: position, track, speed    |
  | Does NOT show: altitude, ID      |
  +----------------------------------+
  Useful for: birds, weather, aircraft with failed transponder

  2. SSR (Secondary Surveillance Radar):
  +----------------------------------+
  | Interrogates Mode A/C/S          |
  | transponder on aircraft          |
  | Mode A: 4-digit squawk code      |
  | Mode C: pressure altitude        |
  | Mode S: individual aircraft addr |
  |         + downlinked data        |
  | Range: 250-300nm                 |
  +----------------------------------+
  Key advantage over PSR: altitude, identity, better target definition

  3. ADS-B (Automatic Dependent Surveillance - Broadcast):
  +----------------------------------+
  | Aircraft broadcasts its own      |
  | GPS position, altitude, ID,      |
  | velocity every 0.5 seconds       |
  | on 1090MHz (Mode S Extended      |
  | Squitter)                        |
  | No interrogation needed          |
  | Range: line-of-sight (~250nm)    |
  | Space-based: Aireon satellites   |
  |              (Iridium Next)      |
  +----------------------------------+
  ADS-B Out mandate: US (2020), EU (2020), most regions by 2025
  First time oceanic aircraft position known in real-time (Aireon, 2019)

  COMPARISON:
  PSR: always works; no info; expensive to maintain
  SSR: needs transponder; altitude + ID; existing infrastructure
  ADS-B: needs GPS + transponder; full data; cheap to receive; GPS denied = failure
```

### TCAS II — Traffic Collision Avoidance System

TCAS is the last line of defense against midair collisions. It operates independently of ATC.

```
  TCAS II OPERATION:

  Own aircraft TCAS interrogates nearby transponders.
  Tracks relative position and altitude of other aircraft.

  Two levels of alert:

  TA (Traffic Advisory):
  "Traffic, traffic" - other aircraft within ~25-40 seconds
  Action: search visually, prepare for potential RA
  NO mandatory action; situational awareness only

  RA (Resolution Advisory):
  "Climb, climb" or "Descend, descend" (typically)
  Issued at ~15-35 seconds to collision
  TCAS coordinates with other aircraft's TCAS via Mode S
    -> If both have TCAS, they get complementary RAs
    -> One climbs, one descends; never both same direction

  MANDATE:
  ICAO: All transport aircraft >5,700kg -> TCAS II required
  Resolution Advisory MUST be followed even if contradicts ATC
  This is the ONLY case where a pilot must disobey ATC
  Reason: TCAS has better situational awareness at 15-second horizon
  than a controller managing hundreds of targets

  UBERLINGEN (2002):
  DHL 757 and Bashkirian Tu-154 mid-air collision.
  TCAS said descend (757) and climb (Tu-154).
  ATC said Tu-154 descend (same direction as TCAS).
  Tu-154 crew followed ATC, ignored TCAS RA.
  Result: 71 fatalities.
  LESSON: TCAS RA takes priority over ATC. Always.
```

### NextGen and SESAR

The US (NextGen) and Europe (SESAR) programs to modernize aging ATC infrastructure.

```
  KEY MODERNIZATION ELEMENTS:

  PBN (Performance-Based Navigation):
  Area navigation using GPS/GNSS instead of ground-based navaids.
  Aircraft navigates to a waypoint in 3D space, not a VOR radial.
  Allows: curved approaches, closely-spaced parallel approaches,
          arbitrary routing not constrained by navaid location.

  RNP AR (Required Navigation Performance - Authorization Required):
  Special type of PBN approach allowing very tight path tolerances.
  RNP 0.1 = aircraft stays within ±0.1 nautical mile of path (185m)
  Enables curved approaches into terrain-surrounded airports
  (Innsbruck, Kathmandu, Queenstown) that were previously impossible.

  CDM (Collaborative Decision Making):
  Airlines, airports, and ATC share flight data in real-time.
  ATFM (Air Traffic Flow Management): slot allocation to manage
  flow before aircraft depart rather than holding them in the air.

  SWIM (System Wide Information Management):
  Common data-sharing architecture for aviation community.
  Analogous to API integration in software: common interfaces,
  not point-to-point data feeds.

  DATA COMM (FANS/CPDLC):
  Text messaging between ATC and pilots on VHF/SATCOM.
  Replaces some voice readbacks, reduces frequency congestion.
  Controller-Pilot Data Link Communications (CPDLC).
  Used routinely on oceanic routes since 1990s; expanding to domestic.
```

---

## ICAO Airspace Classification

ICAO defines seven airspace classes (A-G). The key dimension is: IFR only, IFR/VFR, or VFR only.

```
  ICAO AIRSPACE CLASSES:

  Class | IFR | VFR | ATC   | Sep IFR-IFR | Sep IFR-VFR | Sep VFR-VFR
  ------+-----+-----+-------+-------------+-------------+------------
  A     | Yes |  No | Full  | Provided    | N/A         | N/A
  B     | Yes | Yes | Full  | Provided    | Provided    | Provided
  C     | Yes | Yes | Full  | Provided    | Provided    | Info only
  D     | Yes | Yes | Full  | Provided    | Info only   | Info only
  E     | Yes | Yes | Partial| Provided   | No          | No
  F     | Yes | Yes | Advisory| Advisory  | No          | No
  G     | Yes | Yes | None  | None        | None        | None

  TYPICAL US USAGE:
  Class A: FL180-FL600 (above 18,000ft MSL) — IFR only
  Class B: Major airports (LAX, ORD, JFK) — busy terminal
  Class C: Mid-size airports (Sacramento, Tucson)
  Class D: Smaller controlled airports
  Class E: Most controlled airspace not in B/C/D
  Class G: Low-altitude uncontrolled airspace (below ~700-1,200ft AGL)

  RVSM (Reduced Vertical Separation Minima):
  FL290-FL410: 1,000ft vertical separation (vs old 2,000ft above FL290)
  Implemented globally 2000-2005.
  Doubled capacity in upper airspace.
  Requires: approved avionics, altitude-keeping accuracy <65ft rms.
```

---

## Airline Economics

Airlines have notoriously thin margins. Warren Buffett famously said that a far-sighted capitalist would have shot down Orville Wright at Kitty Hawk. Total airline profit 1919-2019 approximately zero net. Yet individual periods and carriers are highly profitable.

### Cost Structure

```
  AIRLINE COST BREAKDOWN (approximate, US major carrier):

  +------------------------------------------+
  | Labor                       28-35%        |
  | Fuel                        20-30%        |
  | Aircraft ownership/leasing  10-15%        |
  | Maintenance                 10-15%        |
  | Distribution/sales           5-10%        |
  | Airport/navigation fees      8-12%        |
  | Other                        5-10%        |
  +------------------------------------------+

  KEY METRICS:

  CASM (Cost per Available Seat-Mile):
  CASM = Total operating cost / (seats * miles flown)
  LCC: 6-9¢/ASM (Southwest, Spirit, Ryanair)
  Legacy: 12-18¢/ASM (American, Delta, United, BA)
  The CASM gap is the structural competitive challenge for legacies.

  RASM (Revenue per Available Seat-Mile):
  RASM = Total revenue / (seats * miles flown)
  Profitable if RASM > CASM.

  LOAD FACTOR:
  = Revenue Passenger Miles / Available Seat Miles
  Industry average: 83-87% (long-run trend upward)
  Break-even load factor: ~75-80% for most carriers
  At 85%+: airline profitable; at 70%-: airlines bleed cash

  AIRCRAFT UTILIZATION:
  Hours per aircraft per day.
  LCC target: 12-14 hours/day
  Legacy long-haul: 14-16 hours/day (overnight long-haul)
  High utilization spreads ownership cost over more ASMs.
```

### Hub-and-Spoke vs Point-to-Point

```
  HUB-AND-SPOKE (legacy carrier model):
                    +-------+
         /--------| CHICAGO|--------\
        /          |  Hub  |         \
  Boston          +-------+         LA
  NY                  |             Seattle
  DC              Denver            Portland
                  Phoenix
                  Dallas

  ECONOMIES:
  N spokes -> N*(N-1)/2 markets served via hub
  15 spokes -> 105 city pairs with 15 routes
  Load consolidation: each spoke feeds multiple connecting banks
  Frequency on thin routes: possible because demand combines

  DISECONOMIES:
  Hub congestion: schedule banks -> peaks -> delays
  Connection time: passengers lose 90-180min at hub
  CASM penalty: hub operations expensive

  POINT-TO-POINT (LCC model):
  Direct city pairs only. No connections.
  Southwest: point-to-point, no interlining, no bags-checked through.
  Ryanair: secondary airports, fast turns (25 min), no connections.

  LCC COST ADVANTAGES:
  - Single aircraft type (no mixed fleet training/maintenance)
  - Higher seat density (30cm pitch vs 33-35cm)
  - No premium cabin (all seats similar cost to operate)
  - Secondary airports (lower fees, faster slot access)
  - Shorter check-in/boarding times
  - Higher utilization (turn around in 25-30 min vs 45-60 min)
```

### Revenue Management (Yield Management)

One of the most sophisticated real-time pricing systems ever built — SABRE (1960) was the first, and it directly descended into modern airline RM systems and from there into modern distributed transaction databases.

```
  FARE CLASS STRUCTURE:

  Booking       Business  Premium  Economy  Economy  Discount
  Class Code:   J/C       W        Y        B/H/M    T/Q/V
                ^                                    ^
                |                                    |
                Highest fare                        Lowest fare
                (full flexibility)                  (restricted)

  NESTED FARE CLASSES:
  Available seats per class set by RM system.
  EMSR-b (Expected Marginal Seat Revenue - bid price):
  Optimal nesting: open class j if E[revenue from future high-class]
                               < current class j revenue

  OVERBOOKING:
  Airline sells more seats than the aircraft has.
  No-show model: historically 5-15% of passengers no-show.
  Overbooking level = f(fare class mix, route, season, day of week)
  Expected oversales = Poisson(show-up rate) - capacity
  Denied boarding cost < oversale revenue → rational to overbook.
  Voluntary denied boarding: compensation + later flight = happy.
  Involuntary denied boarding: involuntary bump rules (EU261, US DOT).

  O&D vs LEG-BASED RM:
  Leg-based: optimize each flight leg independently
  O&D: optimize across entire itinerary (passenger from BOS->CHI->LAX
       competes with BOS->CHI-only passenger for the BOS->CHI seat)
  O&D is harder (4B+ itinerary-fare combinations at a major airline)
  but materially improves revenue (5-10%).
```

---

## Slot Coordination

Airport slots are the right to land or take off at a specific time. At Level 3 (fully coordinated) airports, slots are allocated by an independent coordinator.

```
  IATA WORLDWIDE SLOT GUIDELINES (WSG):

  Level 1:  No coordination needed. Slots allocated on request.
  Level 2:  Schedule facilitated. Some congestion; coordinator helps.
  Level 3:  Fully coordinated. Slot required for each movement.

  ~170 Level 3 airports worldwide (LHR, CDG, NRT, PEK, HKG, etc.)

  GRANDFATHER RIGHTS:
  "Use it or lose it" rule: airline must operate >=80% of allocated slots
  or lose them ("slot forfeiture").
  If operated >= 80%: airlines keeps slot series for next equivalent season.
  This creates strong incentive to fly even unprofitable routes (ghost flights).

  SLOT TRADING:
  EU allows secondary slot trading.
  Heathrow slots: £50-100M per slot pair (2 = 1 landing + 1 takeoff)
  Airlines with valuable slots (LHR) have a strategic asset.

  LHR CAPACITY:
  ~480,000 movements/year (2 runways, 82 stands, ~140 gates)
  Third runway approved in 2016 planning inquiry; still not built in 2024.
  Global airports with slot scarcity: LHR, JFK, NRT, CDG, HND.
```

---

## The SABRE Bridge — Aviation as Distributed Systems Pioneer

SABRE (Semi-Automated Business Research Environment, 1960) was built by IBM and American Airlines. It was the first real-time transaction processing system at commercial scale. Running on an IBM 7090 at Briarcliff Manor, NY, it processed reservations across 2,000 terminals nationwide — the first distributed database application in history.

```
  SABRE (1960) ->          Modern relevance:
  Real-time reservations    Same problem: distributed state
  across 2,000 terminals    across thousands of nodes
  18 million fares          Billions of records
  Conflict resolution       Eventual consistency / MVCC
  Inventory management      Available-seat tracking
  IBM 7090 mainframe        Cloud-native microservices

  Lineage:
  SABRE (1960) -> PARS/BARS -> Amadeus/Sabre GDS (1990s)
  -> Modern PSS (Passenger Service System)
  -> Google Flights (ITA Software, acquired 2011)

  The airline industry invented distributed real-time transaction
  systems in 1960. Every lesson in CAP theorem, eventual consistency,
  and distributed locking was learned first in airline reservations.
```

---

## Decision Cheat Sheet

| Aviation decision | Guidance |
|------------------|----------|
| Determine runway length needed | Aircraft performance AFM + ISA + elevation + temperature corrections |
| Choose runway orientation | Wind rose analysis; achieve 95% coverage with single or dual orientations |
| Size terminal for demand | IATA LOS C: ~1.2m^2/pax in hold room, 40 passengers/check-in desk |
| Classify airspace at new airport | Follow ICAO Annex 11; Class D for controlled, traffic-based |
| Choose surveillance technology | ADS-B for new builds (cheaper); SSR for existing infrastructure upgrade |
| Evaluate airline CASM | LCC benchmark: 6-9¢; legacy benchmark: 12-18¢ |
| Assess slot-constrained route | Check Level 3 status; slot cost often dominates market entry decision |
| Choose approach aid type | ILS CAT I for most; CAT II/III for low-visibility hubs; GLS for flexibility |

---

## Common Confusion Points

**ADS-B does not replace radar**
ADS-B is dependent on the aircraft having a working GPS and transponder. It fails in GPS-denied environments (jamming, spoofing), and aircraft without transponders are invisible. Radar remains the independent backup. ICAO mandates ADS-B Out (aircraft broadcasts position) but ADS-B In (aircraft receives others' positions) is not yet universal.

**IFR vs VFR is not about weather; it's about rules**
IFR = Instrument Flight Rules. You file a flight plan, get clearances, get separated by ATC. You can fly IFR in clear weather. VFR = Visual Flight Rules. You are responsible for your own separation, maintain visual reference to ground, stay clear of clouds and controlled airspace. Most commercial aviation is IFR. Most light aircraft training is VFR. The rule change is about who provides separation, not visibility conditions.

**Hub-and-spoke is not dying**
LCCs forced legacy carriers to match prices on point-to-point routes. But hub-and-spoke has significant advantages for international connections and thin domestic routes. Delta/United/American and the European legacies (BA, Lufthansa, AF-KL) remain hub-dependent. The model is constrained but not replaced.

**Slots vs schedule times vs allocated capacity**
A slot is the right to operate a specific movement at a specific time. Schedule times are what you publish to passengers. Allocated capacity at an airport is the physical maximum movements. These can all differ: you might have a slot for 0800 but publish a 0810 departure to account for preparation time.

**TCAS RA is not optional**
When TCAS issues a Resolution Advisory, FAA/ICAO regulations require the pilot to follow it immediately, even if it contradicts ATC instructions. The Uberlingen accident killed 71 people because a crew followed ATC instead. There is a single exception: the pilot has visual separation and the RA would create conflict with another visually identified aircraft.
