# Maritime Transportation

## The Big Picture

Maritime shipping moves ~80% of global trade by volume and ~70% by value. It is the backbone of globalization — not the internet, not aviation. Every container of electronics, every tonne of iron ore, every barrel of crude oil crossing an ocean moves by ship. The economics are extraordinary: shipping a 40-foot container from Shanghai to Rotterdam costs roughly $1,500-3,000 in normal markets — less than the cost of a domestic courier delivery.

```
+------------------------------------------------------------------+
|                   MARITIME SYSTEM LAYERS                         |
|                                                                  |
|  SHIP TYPES (by cargo)                                           |
|  +----------+ +----------+ +----------+ +----------+ +--------+ |
|  | Container| | Bulk     | | Tanker   | | LNG/LPG  | | RoRo / | |
|  | Ship     | | Carrier  | | (Crude/  | | Carrier  | | Ferry  | |
|  | (TEU)    | | (Dry)    | | Product) | |          | |        | |
|  +----------+ +----------+ +----------+ +----------+ +--------+ |
|                                                                  |
|  NAVAL ARCHITECTURE                                              |
|  +----------+ +----------+ +----------+ +----------+            |
|  | Hull Form| | Stability| | Resistance| | Propulsion|           |
|  | (Cb, Cp) | | (GM, GZ) | | (wave/   | | (diesel/ |           |
|  |          | |          | | friction)| | propeller)|           |
|  +----------+ +----------+ +----------+ +----------+            |
|                                                                  |
|  PORT OPERATIONS                                                 |
|  +----------+ +----------+ +----------+ +----------+            |
|  | Berths   | | Cranes   | | Yard     | | Inland   |            |
|  | (draft   | | (STS     | | (RTG/ASC)| | Connectivity|         |
|  | limits)  | | gantry)  | |          | | (rail/   |            |
|  +----------+ +----------+ +----------+ | truck)   |            |
|                                         +----------+            |
|  ROUTING AND NAVIGATION                                          |
|  +----------+ +----------+ +----------+ +----------+            |
|  | Weather  | | AIS      | | GMDSS    | | Chokepoint|           |
|  | routing  | | tracking | | Safety   | | risk mgmt |           |
|  +----------+ +----------+ +----------+ +----------+            |
+------------------------------------------------------------------+
```

---

## Ship Types and Their Cargo

### Container Ships

The workhorses of globalized manufacturing. They carry everything that fits in a standard ISO container.

```
  CONTAINER SHIP SIZE CLASSES:

  Class            TEU range   LOA (m)   Beam (m)   Draft (m)   Notes
  -----            ---------   -------   --------   --------    -----
  Feeder           100-999     100-150   20-25      5-8         Small ports, islands
  Sub-Panamax      1,000-3,000 180-210   25-30      10-12       Pre-Panama route
  Panamax          3,000-5,000 294       32.3       12          Old Panama locks (max)
  Post-Panamax     5,000-12,000 300-350  35-43      13-15       Major port routes
  New Panamax      10,000-14,500 366     49         15.2        New Panama locks (max)
  ULCS (Ultra-     18,000-24,500 400     61         16          Fewest ports can handle
  Large Container
  Ship)

  TEU = twenty-foot equivalent unit
  1 TEU = standard 20-foot ISO container
  1 FEU = 40-foot (= 2 TEU)
  Modern typical container: 40-foot high-cube = 1 FEU = 2.3 TEU (in industry counting)

  Top 5 carriers (2024, fleet TEU):
  1. MSC (Mediterranean Shipping Co) — ~6.2M TEU
  2. Maersk — ~4.3M TEU
  3. CMA CGM — ~3.9M TEU
  4. COSCO — ~3.0M TEU
  5. Hapag-Lloyd — ~2.0M TEU
  Top 3 = ~50% of global container capacity (oligopoly)
```

### Dry Bulk Carriers

Carry unpackaged bulk commodities: iron ore, coal, grain, bauxite, phosphate. Self-loading/unloading in some designs.

```
  BULK CARRIER SIZE CLASSES:

  Class       DWT range    Key cargo         Key routes
  -----       ---------    ---------         ----------
  Handysize   10-40k DWT   Grain, fertilizer  Short sea, minor ports
  Handymax    40-60k DWT   Coal, grain        Flexible routing
  Supramax    50-65k DWT   Minor bulk         Global
  Panamax     65-80k DWT   Coal, grain        Any with Panama access
  Capesize    100-200k DWT Iron ore, coal     Cannot transit Panama/Suez;
                                              routes via Cape of Good Hope
                                              or Cape Horn
  VLBC        200-400k DWT Iron ore           Brazil-China, Australia-China
  (Vale class 400k DWT)

  DWT = deadweight tonnes (total payload capacity)

  KEY ROUTES:
  Iron ore: Australia -> China; Brazil -> China; South Africa -> China
  Coal:     Australia -> Japan/Korea/India; US -> Europe
  Grain:    US Gulf -> China; Brazil -> China/Middle East
```

### Tankers

Carry liquid bulk: crude oil, refined petroleum products, chemicals.

```
  TANKER CLASSIFICATION:

  Type        Size (DWT)    Product       Example route
  ----        ----------    -------       -------------
  General     5-25k         Clean (petrol, Singapore -> Thailand
  Purpose                   jet fuel)
  MR          25-55k        Clean product US Gulf -> Europe
  LR1         55-80k        Dirty/clean   Middle East -> Europe
  LR2         80-160k       Dirty crude   Middle East -> Asia
  Aframax     80-120k       Crude         Caribbean, Mediterranean
  Suezmax     120-200k      Crude         Max size for Suez Canal
  VLCC        200-320k      Crude         Middle East -> Asia/Europe
  ULCC        320k+         Crude         Few ports can handle

  Double hull: MARPOL 73/78 mandated double-hull construction
  after Exxon Valdez (1989). No single-hull tankers allowed since 2010.
  Double hull = inner hull + outer hull with void space between.
  Accidental grounding: outer hull breached, inner hull intact.
```

### LNG Carriers

Liquefied Natural Gas requires cryogenic storage at -163°C. The engineering is extreme.

```
  LNG CARRIER DESIGN:

  Two main tank types:

  MOSS (Spherical):           MEMBRANE (GTT):
  +--+--+--+--+               +-----------------------+
  |  O  O  O  O|              |  ~~~~~~~~~~~~~~~~~~~  |
  | (4 spheres)|              | Thin stainless steel  |
  +------------+              | 1.2mm thick, corrugated|
  Self-supporting             +-----------------------+
  Visible above deck          Insulation box: 200mm
  Simpler insulation          Supported by ship hull
                              Lower center of gravity
                              More cargo space

  Tank pressure: ~0.025 bar gauge (near atmospheric)
  Temperature: -163°C
  Boil-off: ~0.1-0.15%/day (small amount vaporizes; used as fuel or reliquified)

  FSRU (Floating Storage and Regasification Unit):
  A converted or purpose-built LNG carrier that also regasifies.
  Used to rapidly deploy LNG import terminals without fixed infrastructure.
  Germany deployed 5 FSRUs in 2022-2023 to replace Russian pipeline gas.
```

---

## Naval Architecture

### Hull Form and Resistance

The hull form determines resistance — the force that must be overcome to move the ship.

```
  BLOCK COEFFICIENT (Cb):
  Cb = Displacement volume / (L * B * T)
  Where L = length, B = beam, T = draft

  Cb = 1.0: perfect rectangular block
  Cb = 0.5: fine ship (sailboat)
  Cb = 0.85: typical bulk carrier
  Cb = 0.65-0.70: typical container ship (fine ends for speed)

  HIGH Cb: more cargo per metre of length; harder to push (more resistance)
  LOW Cb: faster for given power; less cargo volume

  RESISTANCE COMPONENTS:
  +--------------------------------------------+
  | Total resistance = Rf + Rw + Ra            |
  |                                            |
  | Rf = Frictional resistance                 |
  |    = Dominated at low speeds              |
  |    = Scales with wetted surface area       |
  |    = Reduced by anti-fouling paint         |
  |      (hull fouling adds 10-15% fuel/yr)    |
  |                                            |
  | Rw = Wave-making resistance                |
  |    = Dominates at high speeds              |
  |    = Scales approximately with Fr^4        |
  |    = Froude number Fr = v / sqrt(g*L)      |
  |    = Hard limit ~Fr 0.3-0.35 for           |
  |      displacement vessels                  |
  |                                            |
  | Ra = Air resistance, appendage drag        |
  |    = Smaller, sometimes significant        |
  +--------------------------------------------+

  FROUDE NUMBER LIMIT:
  At Fr ~0.3-0.35, wave-making resistance rises steeply.
  Container ships: ~22 knots, Fr = 0.24 (well below limit)
  High-speed ferries: 35-45 knots, must use planing or hydrofoil hulls
```

### Stability

A ship that capsizes is obviously a problem. Stability is the ship's ability to return to upright after heeling.

```
  METACENTRIC HEIGHT (GM):

  G = Centre of gravity (where ship's weight acts downward)
  B = Centre of buoyancy (centre of displaced water volume)
  M = Metacentre (pivot point)

  GM = BM - BG

  GM > 0: ship is stable (M above G) -> rights itself when heeled
  GM < 0: ship is unstable -> capsizes if heeled beyond certain angle
  GM too large (>1.5-2m): "stiff" ship, violent rolling, cargo damage

  GZ CURVE (righting lever):
  At any heel angle theta, righting moment = displacement * GZ
  GZ > 0 for theta < angle of vanishing stability -> stable range

  IMO Intact Stability Code requirements:
  - Area under GZ to 30 degrees > 0.055 m-rad
  - Area 30-40 degrees > 0.030 m-rad
  - GZ peak >= 0.2m at >=30 degrees heel
  - GM initial >= 0.15m
```

---

## Propulsion Systems

### Diesel Engine Dominance

The 2-stroke slow-speed diesel engine powers ~90% of the world's large merchant ships.

```
  2-STROKE SLOW-SPEED MARINE DIESEL:

  Cylinder bore:  650-980mm (enormous)
  Stroke:         2,000-3,500mm (2-3.5 metre piston stroke)
  RPM:            80-120 RPM (direct drive to propeller)
  Power:          5-100 MW per engine
  Thermal efficiency: 50-55% (best heat engine in commercial use)
  SFOC (Specific Fuel Oil Consumption): ~160-175 g/kWh

  WHY 2-STROKE:
  2-stroke = one power stroke per revolution (vs 4-stroke: every other)
  At 100 RPM, 100 power strokes per minute
  Very high torque, low RPM = ideal for large propellers
  Direct drive: no gearbox needed (huge advantage for reliability)

  PROPELLER:
  Typically: Fixed Pitch Propeller (FPP) or Controllable Pitch (CPP)
  Diameter: 5-10 metres on large vessels
  Optimal advance ratio: J = Va / (n*D)  where Va = advance speed
  Cavitation limit: if local pressure drops below vapor pressure -> erosion
  Tip speed typically limited to 40 m/s to avoid cavitation
```

**Speed-fuel cube law:** Fuel consumption scales approximately with the cube of speed.

    Fuel consumption (tonnes/day) ~ v^3

Therefore:
- 20% speed reduction (e.g., 25 knots -> 20 knots) -> 51% fuel reduction
- 30% speed reduction -> 66% fuel reduction
- **Slow steaming** became standard practice after 2008 oil price spike and container market depression

This cubic relationship is why slow steaming dominated the post-2008 shipping industry and why higher fuel prices directly incentivize speed reduction.

---

## Port Operations

### Container Terminal Anatomy

```
  CONTAINER TERMINAL LAYOUT:

  SEA SIDE                           LAND SIDE
  +---------+  +---------+           +---------+
  |  Berth  |  |  Berth  |           |  Gate   | <- Truck entry/exit
  |  STS    |  |  STS    |           +---------+
  | Cranes  |  | Cranes  |                |
  +---------+  +---------+           +---------+
       |              |              | Rail    | <- Intermodal rail
       v              v              | Terminal|
  +-----------------------+          +---------+
  |      YARD             |
  | Stack storage:        |
  | RTG (rubber-tyred     |
  |   gantry cranes)      |
  | or ASC (automated     |
  |   stacking cranes)    |
  | 4-6 containers high   |
  |                       |
  | Yard tractors + chassis|
  +-----------------------+

  STS (Ship-to-Shore) gantry crane:
  - Outreach: 60-70m (spans width of ULCS)
  - Height: 50-60m above quay
  - Lift capacity: 65+ tonnes
  - Productivity target: 30-40 moves/crane/hour
  - "Move" = one container lift (on or off ship)

  TERMINAL THROUGHPUT METRICS:
  TEU/hectare/year: yard density
  High-density: 1,000-2,500 TEU/ha/yr (automated terminals)
  Low-density: 300-600 TEU/ha/yr (conventional RTG)
  Ship turn time: critical for berth utilization
  Port State Control (PSC) inspections: flag state/port state authority
```

### Berth Productivity

Port productivity directly determines shipping cost. A ship at anchor earns nothing and costs ~$50,000-100,000/day in capital and operating costs.

| Terminal | Moves/ship-hour | World class? |
|----------|----------------|-------------|
| World record | ~200 moves/hr | (combined multiple cranes) |
| Top Asian ports | 100-150 moves/hr | Yes |
| European average | 80-110 moves/hr | Good |
| US West Coast | 60-80 moves/hr | Below average (labor rules) |
| Developing world | 30-50 moves/hr | Low |

The US West Coast productivity gap is partly structural (ILA/ILWU labor agreements) and partly equipment vintage. This is why some shippers diverted to East Coast ports (more flexible work rules) or Canadian/Mexican alternatives.

---

## Strategic Chokepoints

Chokepoints are where geography concentrates global trade into narrow passages. Any disruption has immediate global supply chain effects.

```
  GLOBAL MARITIME CHOKEPOINTS:

  +---------------------+--------+------------------+------------------+
  | Chokepoint          | Width  | Annual transits  | If blocked...    |
  +---------------------+--------+------------------+------------------+
  | Strait of Malacca   | 2.7km  | 100,000+ ships   | Alt: Sunda/      |
  | (Malaysia-Indonesia)| min    | 40% global trade  | Lombok strait    |
  |                     |        |                  | +1,200km; costly  |
  +---------------------+--------+------------------+------------------+
  | Suez Canal (Egypt)  | 313m   | ~20,000 ships/yr | Alt: Cape of     |
  |                     | (new   | 12% global trade  | Good Hope        |
  |                     | canal) | 30% container    | +10 days; +$300k |
  |                     |        | traffic Europe-  | per voyage       |
  |                     |        | Asia             |                  |
  +---------------------+--------+------------------+------------------+
  | Panama Canal        | N/A    | ~14,000 ships/yr | Alt: Cape Horn   |
  |                     |        | 5% global trade   | +14 days;        |
  |                     |        |                  | or US intermodal |
  +---------------------+--------+------------------+------------------+
  | Strait of Hormuz    | 55km   | ~20 tankers/day  | Alt: IPSA        |
  | (Iran-Oman)         |        | ~20% global oil  | pipeline (Saudi) |
  |                     |        | ~30% global LNG  | most oil has     |
  |                     |        |                  | no viable alt    |
  +---------------------+--------+------------------+------------------+
  | Bab el-Mandeb       | 26km   | ~20,000 ships/yr | Alt: Suez bypass |
  | (Yemen-Djibouti)    |        | Red Sea access   | or Cape Horn     |
  |                     |        | to Suez          |                  |
  +---------------------+--------+------------------+------------------+
```

**Ever Given (2021):** 400m ULCS ran aground in the Suez Canal on March 23, 2021. Blocked for 6 days. Tied up 369 ships. Estimated $9.6B/day in trade delayed. Demonstrated that single chokepoints in global supply chains have no redundancy. The insurance industry now factors in geopolitical risk to Suez much more aggressively.

**Panama Canal: Old Locks vs New Locks**
- Old (Panamax) locks: 32.3m wide, 294m long — built 1914
- New (Neopanamax) locks: 49m wide, 366m long — opened 2016
- New locks handle up to 14,500 TEU vessels vs 5,000 TEU old locks
- New locks use water-saving basins (recycle ~60% of lockage water)
- The new locks dramatically changed US East Coast vs West Coast port competition

---

## Automatic Identification System (AIS)

AIS is the maritime equivalent of ADS-B in aviation — automatic position broadcasting.

```
  AIS OPERATION:

  Ship broadcasts VHF radio message every 2-10 seconds:
  - MMSI (Maritime Mobile Service Identity) — unique vessel ID
  - Position (GPS lat/lon)
  - Speed over ground (SOG)
  - Course over ground (COG)
  - Heading
  - Vessel name, type, dimensions
  - Destination and ETA

  Reception:
  Class A: Ships >300 GRT or passenger ships — mandatory
  Class B: Smaller vessels — voluntary
  Satellite AIS (spAIS): Low-Earth-orbit satellites receive AIS
                         Coverage: 100% of ocean, 5-15min delay
                         Data providers: exactEarth, Orbcomm, Spire

  DARK VESSEL (AIS manipulation):
  Vessels can turn off AIS or spoof position.
  Used by: sanctions-evading tankers (Iran, Russia)
  Detection: satellite radar (SAR) images without AIS broadcast
  Services: Windward, Pole Star, Lloyd's List Intelligence

  APPLICATIONS:
  - Port arrival planning (automated berthing schedules)
  - Weather routing optimization
  - Collision avoidance (ARPA)
  - Port State Control targeting
  - Sanctions monitoring
  - Cargo tracking (shippers)
```

---

## Maritime Decarbonization

Shipping emits ~1 GtCO2e/year (11% of transport emissions). IMO's 2023 GHG Strategy targets net-zero "by or around 2050."

```
  MARITIME FUEL PATHWAYS:

  FUEL          Carbon intensity  Energy density  Technology    Timeline
  ----          ----------------  -------------   ----------    --------
  HFO/MDO       Reference (~90g   ~41 MJ/kg       Available     Phase-out
  (current)     CO2/MJ)                                         by 2040s
  LNG           ~75 g CO2/MJ      ~50 MJ/kg       Commercial    Bridge fuel
                (methane slip     (but cryogenic) now
                risk)
  Methanol      ~45-55 g CO2/MJ   ~22 MJ/kg       First ships   2025-2030
  (green)       (well-to-wake)                    (Maersk)
  Ammonia       ~0 g CO2/MJ       ~18 MJ/kg       Pilot stage   2027-2035
  (green)       (if green H2)     (toxic)         (MAN engines)
  Hydrogen      ~0 g CO2/MJ       ~120 MJ/kg      Pre-          2030-2040
  (green)       (if green)        (storage!)      commercial
  Wind-assist   Reduces 5-30%     N/A             Deploying     Now
  (Flettner)    depending on      (auxiliary)     now
                route

  SLOW STEAMING:
  Already delivers 15-30% emission reduction from speed alone.
  Widely practiced since 2008.

  EU REGULATION:
  FuelEU Maritime: reduces carbon intensity of fuels stepwise
  2025: -2%, 2030: -6%, 2040: -31%, 2050: -80%
  Applies to ships >5,000 GT calling EU ports
  CII (Carbon Intensity Indicator): annual rating A-E per vessel
```

**Maersk methanol bet:** Maersk ordered 25 dual-fuel methanol vessels (2021-2023), committing to methanol pathway before the fuel supply infrastructure was established. Classic first-mover bet: create demand signal to incentivize methanol production buildout. The 16,000 TEU vessels can run on conventional fuel until green methanol supply is available.

---

## Maritime Conventions

| Convention | Purpose |
|-----------|---------|
| **SOLAS** (Safety of Life at Sea) | Minimum safety standards for ships; fire, lifeboats, stability, radio |
| **MARPOL** 73/78 | Prevention of pollution from ships; Annexes I-VI |
| **STCW** | Standards of Training, Certification, Watchkeeping for seafarers |
| **MLC 2006** | Maritime Labour Convention — seafarer working conditions |
| **COLREGS** | International Regulations for Preventing Collisions at Sea |
| **ISPS Code** | International Ship and Port Facility Security Code |

All are administered by IMO (International Maritime Organization), a UN agency headquartered in London. IMO cannot enforce directly — flag states (countries where ships are registered) enforce IMO requirements on their flagged vessels. Port State Control (PSC) allows port states to inspect foreign ships.

---

## Decision Cheat Sheet

| Shipping decision | Guidance |
|------------------|----------|
| Choose ship type for cargo | Containers: manufactured goods; Bulk: commodities; Tanker: liquids; LNG: natural gas |
| Estimate fuel cost for a voyage | P_fuel = SFC * P_shaft * distance / speed; then * fuel price |
| Slow steam or maintain speed? | Break-even: if time saving value < fuel cost saving, slow steam |
| Select port routing via Suez vs Cape | Suez saves ~10 days, costs canal fee (~$1M for VLCS); break-even at ~$500-600k/day vessel cost |
| Evaluate terminal productivity | Target 30+ moves/crane/hour; assess gate truck turnaround |
| Assess geopolitical shipping risk | Check chokepoint exposure; dual-route options; insurance premium |
| Choose decarbonization fuel pathway | Near-term: slow steam + LNG; 2030+: methanol; 2035+: ammonia |

---

## Common Confusion Points

**TEU vs container**
A TEU is a unit of measurement, not a physical container. A 20-foot container = 1 TEU. A 40-foot container (the standard today) = 1 FEU = 2 TEU. Ships are measured in TEU capacity but carry mostly 40-foot containers, so actual container count is about half the TEU number.

**Deadweight tonnes (DWT) vs displacement**
DWT = total payload capacity (cargo + fuel + stores + crew + water). Displacement = total weight of ship (hull + cargo + everything). A Capesize bulk carrier might have 200,000 DWT but 220,000 tonnes displacement (full load). These are not interchangeable.

**"Slow steaming" is a business decision, not a technical limitation**
Ships are designed for a service speed (typically 22-25 knots for container ships). Slow steaming (18-20 knots) is a choice driven by fuel cost economics and overcapacity. When fuel prices spike or capacity is tight (post-COVID), operators return to higher speeds. It is a variable operating decision, not a fixed constraint.

**Flag state vs port state vs coastal state**
Flag state: country where ship is registered (Panama, Liberia, Marshall Islands handle ~40% of world fleet via "open registries" offering low taxes). Port state: country where ship calls; can inspect for SOLAS/MARPOL compliance. Coastal state: country whose EEZ (Exclusive Economic Zone) the ship passes through; limited jurisdiction unless the ship enters territorial waters. These three types of jurisdiction overlap and can conflict.

**The LNG vs methanol vs ammonia debate**
There is no single right answer. LNG has the infrastructure advantage; methanol has better energy density than ammonia and known engine technology; ammonia is the only zero-carbon option at scale. The answer depends on route, cargo, fleet replacement cycle, and which fuel supply chain builds out fastest. Most major operators are dual-fuel (can run on conventional fuel + alternative), hedging the uncertainty.
