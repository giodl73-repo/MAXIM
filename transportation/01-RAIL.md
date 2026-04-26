# Rail Systems

## The Big Picture

Rail is the oldest large-scale transportation technology still dominant in its niches. It wins on energy efficiency (steel wheel on steel rail rolling resistance is ~10x lower than rubber on asphalt), capacity (one track lane moves far more people or freight than one road lane), and safety. It loses on flexibility, capital cost, and the chicken-and-egg demand problem.

```
+------------------------------------------------------------------+
|                       RAIL SYSTEM LAYERS                         |
|                                                                  |
|  INFRASTRUCTURE                                                  |
|  +---------+  +---------+  +---------+  +---------+              |
|  | Track   |  | Signals |  | Stations|  | Power   |             |
|  | Geometry|  | & Safety|  | & Yards |  | Supply  |             |
|  +---------+  +---------+  +---------+  +---------+             |
|                                                                 |
|  VEHICLE (rolling stock)                                        |
|  +---------+  +---------+  +---------+  +---------+             |
|  | Traction|  | Bogies  |  | Braking |  | Cab /   |             |
|  | (motor) |  | (trucks)|  | system  |  | ETCS OBU|             |
|  +---------+  +---------+  +---------+  +---------+             |
|                                                                 |
|  OPERATIONS                                                     |
|  +---------+  +---------+  +---------+  +---------+             |
|  | Timetable  | Train   |  | Control |  | Incident|             |
|  | planning|  | dispatch|  | Centre  |  | mgmt    |             |
|  +---------+  +---------+  +---------+  +---------+             |
|                                                                  |
|  APPLICATION SEGMENTS                                            |
|  +----------+  +--------+  +---------+  +----------+            |
|  | High-    |  | Inter- |  | Urban   |  | Heavy    |            |
|  | Speed    |  | city   |  | Metro/  |  | Freight  |            |
|  | Rail     |  | Rail   |  | LRT/BRT |  | Rail     |            |
|  +----------+  +--------+  +---------+  +----------+            |
+------------------------------------------------------------------+
```

---

## Track Engineering

### Gauge

The distance between inner faces of the running rails. Standardization is incomplete globally — a historical accident with large economic consequences.

```
  +------------------------------------------+
  |              RAIL GAUGES                 |
  |                                          |
  |  Standard    1,435mm (4ft 8.5in)         |
  |  --------    UK, US, Canada, China,      |
  |              Western Europe, most HSR    |
  |                                          |
  |  Broad       1,520mm (Russia/FSU)        |
  |  -----       1,676mm (India, Pakistan)   |
  |              Chose broad for more        |
  |              stability; now a barrier    |
  |                                          |
  |  Narrow      1,000mm (metric) — Africa,  |
  |  ------      parts of Asia, South Am.    |
  |               610mm (mining/plantation)  |
  |                                          |
  |  Consequence: gauge break at Spain-France|
  |  border (Spain uses 1668mm Iberian gauge)|
  |  Trains must change bogies or use        |
  |  variable-gauge axles (SUW/RD system)    |
  +------------------------------------------+
```

### Track Structure

```
  BALLASTED TRACK (conventional)       SLAB TRACK (HSR)

  Rail ──────────────────              Rail ──────────────────
  Clip/fastener                        Clip/fastener
  Sleeper/tie (wood or concrete)       Concrete slab
  Ballast (crushed stone, ~300mm)      Hydraulically bound layer
  Formation (subgrade)                 Formation (subgrade)

  Advantages: cheap, drains well,      Advantages: stable geometry,
  absorbs shock, maintainable          low maintenance at high speed
  Disadvantages: geometry degrades,    Disadvantages: expensive to
  requires tamping, not ideal >250 kph build, no margin for movement
```

**CWR (Continuous Welded Rail):** Conventional rail is bolted in 10-25m sections with expansion joints (the clickety-clack). CWR welds the rail into continuous lengths of several km, eliminating joints, reducing noise, reducing maintenance. Thermal stress managed by stress-free temperature: the rail is laid at a specific temperature and locked. Above/below that temperature the rail is in compression/tension. Buckling (sun kink) risk in hot weather; pull-apart risk in cold. Track geometry monitoring cars (geometry recording vehicles) measure six key parameters: gauge, cross-level, twist, alignment, longitudinal level, curvature.

### Horizontal Alignment

```
  TRACK ALIGNMENT ELEMENTS

  Tangent (straight) -> Transition spiral (clothoid) -> Circular curve

  Circular curve: radius R determines speed limit
  Transition spiral: eases entry/exit, reduces lateral jerk

  CANT (SUPERELEVATION):
  Outer rail raised above inner rail in curves.
  Provides centripetal force component from gravity.

  Balance cant = v^2 / (R * g) * gauge     (in mm for standard speeds)

  Cant deficiency (CD): for speeds above balance speed
  Cant excess: for speeds below (freight vs passenger problem)

  SPEED vs RADIUS (approximate limits):

  Application        Min Radius    Max Speed
  -----------        ----------    ---------
  Heavy freight      300m          80 km/h
  Conventional rail  800m          160 km/h
  High speed (cant)  4,000m        250 km/h
  HSR (TGV/Shinkansen) 6,000m+    320 km/h
```

### Vertical Alignment

Gradients (grades) matter enormously for traction and braking:

| Application | Max Gradient | Why |
|-------------|-------------|-----|
| Heavy freight (loaded) | 0.5-1.0% | Adhesion limit for long trains |
| Conventional mainline | 1-2% | Balance traction and cost |
| High-speed rail | 2.0-3.5% | Shorter trains, more power |
| Mountain rack railway | 25-48% | Special rack-and-pinion |

---

## Wheel-Rail Contact Mechanics

This is the fundamental physics of rail. Everything else is built on it.

```
  WHEEL PROFILE                RAIL HEAD PROFILE

     /===\                        /===\
    /     \  <- tread           /     \
   |  flange|                  |       |
    \      /                    \     /
     ======                      =====

  Contact patch: approximately elliptical (Hertz contact theory)
  Typical dimensions: 10-15mm x 10-15mm
  Contact pressure: 800-1,200 MPa (extremely high)
  Entire weight of train transmitted through this tiny patch
```

**Adhesion coefficient (mu):** The ratio of maximum tangential force to normal load that can be transmitted without wheelslip.

```
  Conditions             mu (adhesion coefficient)
  ----------             -------------------------
  Dry steel on steel     0.20 - 0.30
  Wet rail               0.10 - 0.18
  Leaf contamination     0.02 - 0.05 (autumn problem)
  Sand applied           0.25 - 0.35 (sanders restore adhesion)

  Traction force limit = mu * axle load * g

  For a 20-tonne axle:
  Dry: 20,000 * 9.81 * 0.25 = ~49 kN per axle
  Wet: 20,000 * 9.81 * 0.12 = ~24 kN per axle
```

**Creep and Kalker theory:** At any non-trivial speed, the wheel does not roll purely — there is always some microslip (creep) at the contact patch. Kalker (1966) developed the linear theory: creep forces are proportional to creep ratios up to the adhesion limit. Creep forces are what steer wheelsets in curves (gravitational steering from coned wheel profiles). Hunting oscillation: above a critical speed, a wheelset oscillates laterally in a sinusoidal motion that grows in amplitude — instability. Dampers and careful profile geometry management control this.

---

## Traction Systems

```
  ELECTRIC TRACTION SYSTEMS

  +------------------------------------------------------+
  |  System        | Voltage | Freq  | Collection | Use  |
  |----------------|---------|-------|------------|------|
  | DC 600/750V    | 750V DC | -     | Third rail | Urban metro |
  | DC 1500V       | 1500V DC| -     | Overhead   | Commuter, some mainline |
  | DC 3000V       | 3000V DC| -     | Overhead   | Italy, Czech, Poland |
  | AC 25kV 50Hz   | 25kV AC | 50Hz  | Overhead   | Mainline, HSR — dominant |
  | AC 15kV 16.7Hz | 15kV AC | 16.7Hz| Overhead   | Germany, Austria, Switzerland |
  | AC 25kV 60Hz   | 25kV AC | 60Hz  | Overhead   | Japan HSR (Shinkansen) |
  +------------------------------------------------------+

  Higher voltage = lower current = thinner wire = cheaper infrastructure
  But more complex on-board transformers and converters

  DIESEL TRACTION (non-electrified routes):

  Old: Diesel-mechanical (direct drive via gearbox) — maintenance nightmare
  Modern: Diesel-electric (diesel engine drives generator -> electric motor)
          Same as a hybrid locomotive
  Current: Hydrogen fuel cell (HFC) locomotives entering service
           Battery-electric for shorter non-electrified segments
```

**Regenerative braking:** Electric traction motors can act as generators during braking, returning energy to the overhead wire (or to onboard storage if no other train is drawing power). Urban metros typically recover 15-30% of traction energy through regeneration. HSR lines with frequent braking can recover 20-40%.

---

## Signaling and Train Protection

This is where the critical safety architecture lives.

### Fixed Block vs Moving Block

```
  FIXED BLOCK SIGNALING (traditional):

  Track divided into physical blocks (track circuits)
  Signal aspect at block entry = occupancy status of next block(s)

  [Block 1  ][Block 2  ][Block 3  ][Block 4  ]
  [  Train  ][  CLEAR  ][  CLEAR  ][  CLEAR  ]
  [         ][ GREEN   ][ GREEN   ][ GREEN   ]

  Headway limited by: block length + braking distance + buffer
  Typical minimum headway: 2-3 minutes (mainline)
  Urban metro with short blocks: can reach ~90 seconds

  MOVING BLOCK (CBTC / ETCS L3):

  No physical blocks. System knows exact train position.
  Safety envelope calculated dynamically per train.

  Train A position known to ±1m
  Train B position known to ±1m
  Safe separation = braking distance + safety margin

  Headway limited by: braking distance only
  Typical minimum headway: 60-90 seconds (metro)
  Theoretical: 50 seconds on some systems
```

### ETCS/ERTMS — The European Standard

The EU mandated a single interoperable train control system to replace 20+ national systems that prevented through-running of trains across borders. (Imagine if every country's internet had a different protocol stack — that was European rail in 1990.)

```
  ETCS LEVELS:

  Level 0    Train has no ETCS; runs on lineside signals
             Fallback mode only

  Level 1    Lineside signals still primary
             ETCS Eurobalises (transponders in track) transmit
             Movement Authorities to train
             ATP overlay on top of existing signals

  Level 2    Radio Block Centre (RBC) tracks trains via GSM-R radio
             Lineside signals can be removed
             ETCS on-board unit enforces Movement Authority
             Tracks ~1-2 km accuracy with radio heartbeat

  Level 3    Full moving block
             Train determines its own position (GPS + odometry)
             Reports to RBC; RBC grants Movement Authority
             No track circuits needed
             Not yet widely deployed (liability/redundancy issues)

  ERTMS = ETCS + GSM-R (radio) + EuroRadio (protocol)
  All new European mainline and HSR uses Level 2
```

### CBTC — Urban Metro Standard

Communications-Based Train Control: the urban moving-block system. Uses 2.4 GHz Wi-Fi or TETRA radio for continuous bidirectional communication between train and wayside. Trains self-report position from odometry + transponder correction. Central controller (ATC) calculates Movement Authorities for every train continuously. Enables 60-90 second headways on metros like Singapore MRT, Beijing Line 1, NYC L train.

### PTC — North American Mandate

Positive Train Control: mandated in the US after the Chatsworth collision (2008, 25 deaths, engineer was texting). Three functions: stop a train exceeding speed limit, stop a train running a stop signal (SPAD), prevent unauthorized train-on-train collision. Implementation: GPS for position, digital radio for data link, back-office server maintaining movement authority. All Class I railroads met the 2020 compliance deadline. PTC does not provide moving block — it is a safety overlay on fixed-block operation.

---

## High-Speed Rail

### Infrastructure Requirements

HSR is not just a faster train — it requires fundamentally different infrastructure:

```
  CONVENTIONAL RAIL              HIGH-SPEED RAIL

  Max speed: 100-200 km/h        Max speed: 250-350 km/h
  Curve radius: 800-1,500m       Curve radius: 4,000-7,000m
  Max gradient: 1.5%             Max gradient: 2.0-3.5%
  Track: ballasted               Track: slab track (>250 km/h)
  Overhead: 25kV AC              Overhead: 25kV AC (same)
  Shared: freight + passenger    Dedicated ROW: passengers only
  Level crossings: allowed       Level crossings: NONE
  Cost: $5-20M/km                Cost: $15-100M/km

  WHY DEDICATED ROW:
  - Freight trains have different speed profiles (slower)
  - Mixed operations complicate scheduling (slow train blocks fast)
  - Level crossings are fatal at 300 km/h
  - Track geometry must be maintained to tighter tolerances
```

### The Major Systems

| System | Country | Network | Speed | Introduced | Key Achievement |
|--------|---------|---------|-------|-----------|----------------|
| **Shinkansen** | Japan | 3,000+ km | 320 km/h | 1964 | Zero passenger fatalities ever; 18-second avg delay |
| **TGV/LGV** | France | 2,700+ km | 320 km/h | 1981 | First modern HSR; land speed record 574.8 km/h |
| **ICE** | Germany | 3,600+ km | 300 km/h | 1991 | Tilt technology (ICE-T); shared some conventional track |
| **Eurostar** | UK-France | Channel Tunnel | 300 km/h | 1994 | Under-sea operation; cross-national |
| **CR (CRH)** | China | 40,000+ km | 350 km/h | 2007 | Largest HSR network in world by factor of 5 |
| **AVE** | Spain | 3,800+ km | 300 km/h | 1992 | Standard gauge break with legacy Iberian network |

**China's HSR story:** China built more HSR in 15 years than the rest of the world combined in 50 years. The CR400AF/BF operates at 350 km/h commercial speed. Controversially subsidized but demonstrated that HSR at large scale is achievable at lower cost than Western projects when planning, procurement, and construction are streamlined. Unit cost: ~$20-50M/km vs $100M/km+ in California.

### Why the US Has Almost No HSR

```
  US GEOGRAPHY + POLICY FACTORS:

  1. Low density: 94% of land area has <100 people/km^2
     (HSR needs >150-300 people/km^2 in corridor to break even)

  2. Long distances between cities: LA-SF = 559km (viable for HSR)
                                    NY-LA = 4,500km (no)

  3. Freight rail dominates corridors: Class I RRs own most ROW
     HSR cannot share with slow heavy freight (gauge + speed)
     New ROW acquisition: politically impossible + extremely expensive

  4. Automobile culture + aviation competition: very price-elastic
     Low-cost carriers make air affordable on most corridors

  5. No federal commitment at scale:
     California HSR: approved 2008, $100B+ cost overruns, partial only
     Amtrak Acela (NE Corridor): maximum 240 km/h on curves, 150 km/h avg
     Not truly high-speed; constrained by shared track

  VIABLE US CORRIDORS (if political will existed):
  NY-Boston-Washington (NE Corridor, 220km, 740km)
  Chicago-Detroit-Cleveland-Pittsburgh
  Dallas-Houston (240km, under development)
  Las Vegas-Los Angeles (Brightline West, 2028 target)
```

---

## Urban Rail

### Mode Comparison

```
  URBAN RAIL MODES — CAPACITY vs COST

  Capacity     (pphpd)
  ^
  80,000 |  +---------+
         |  |  METRO  |  Grade-separated, 60,000-80,000 pphpd
  60,000 |  | (Heavy) |  $200-700M/km construction cost
         |  |  Rail   |  90-120 second headways achievable
  40,000 |  +---------+
         |       |
  30,000 |  +---------+
         |  |  LRT    |  Mix of at-grade and elevated
  20,000 |  | (Light  |  20,000-40,000 pphpd
         |  |  Rail)  |  $50-150M/km
  15,000 |  +---------+
         |       |
  10,000 |  +---------+
         |  |  BRT    |  Bus Rapid Transit — IF done properly
   5,000 |  |(Bus     |  10,000-20,000 pphpd
         |  | Rapid)  |  $2-20M/km (or much less)
         |  +---------+
         +--------------------------------> Cost
                Low                   High
```

**pphpd = persons per hour per direction.** This is the fundamental capacity metric for a transit corridor.

### Metro (Heavy Rail)

Requirements for true metro operation:
- Complete grade separation (no level crossings with road traffic)
- Platform screen doors or equivalent gap management
- Automatic train operation (ATO) on most systems
- Dedicated ROW, no freight sharing
- Third-rail or overhead power, no diesel

Maximum theoretical capacity depends on train length x cars x passengers + headway. A 6-car train at 200 pass/car = 1,200 pax. At 90-second headway: 40 trains/hr x 1,200 = 48,000 pphpd. Best systems (Tokyo, Beijing) approach 80,000 pphpd with longer trains and denser loading.

### Light Rail Transit (LRT)

LRT spans a wide spectrum from glorified streetcar to near-metro:

```
  LRT SPECTRUM:

  Low end                                        High end
  (streetcar)                                  (near-metro)
  +------------+                             +------------+
  | At-grade   |                             | Elevated   |
  | In traffic |                             | or tunnel  |
  | 10-15 km/h |                             | 40-60 km/h |
  | No signal  |                             | Signal     |
  | priority   |                             | priority   |
  | 5,000 pphpd|                             | 30,000+    |
  +------------+                             +------------+

  What makes LRT work:
  - Dedicated lanes (not mixed with traffic)
  - Off-board fare payment (no boarding delays)
  - Level boarding (no steps)
  - Signal priority (extends green when tram approaching)
```

### Commuter Rail

Heavy rail operated on mainline tracks, shared with or separated from freight. Lower frequency than metro (30-60 min headways typical), larger stations, higher speed between stations. Examples: LIRR, Metra Chicago, Paris RER, London Overground. Challenge: sharing mainline track constrains headways. Cannot achieve metro-level frequency without dedicated tracks.

---

## Freight Rail

### Class I Railroad Structure (US)

The US freight rail network is the largest and most efficient in the world. Seven Class I railroads (revenue >$490M/yr) carry >70% of rail freight tonnage.

```
  US CLASS I RAILROADS (7 carriers):

  BNSF Railway          (Burlington Northern + Santa Fe merged 1995)
  Union Pacific (UP)    (largest by route-km: ~52,000 km)
  CSX Transportation
  Norfolk Southern
  Canadian National (CN)
  Canadian Pacific Kansas City (CPKC) (merged 2023)
  Kansas City Southern (now part of CPKC)

  STRUCTURE:
  High fixed costs (track, signals, terminals)
  Variable costs: fuel, crew, car repair
  Revenue: primarily contract rates (not regulated for freight)

  PROFITABILITY:
  US Class I RRs are highly profitable — 60%+ operating ratios
  (operating ratio = operating expense / revenue; lower is better)
  European freight railways often lose money or break even
  Why? US freight is long haul (avg ~1,600 km), high density, unit trains
       European freight is shorter haul, mixed with passenger, higher cost
```

### Train Types

| Type | Description | Economics |
|------|-------------|-----------|
| **Unit train** | Single commodity, dedicated train, direct origin-destination | Highest efficiency; minimal switching |
| **Intermodal** | Containers on flatcars; double-stack (2 containers high) | High value, time-sensitive; connects to ocean shipping |
| **Mixed manifest** | Multiple commodities, cars sorted at classification yards | Lower efficiency; intermediate stops |
| **Auto rack** | Multi-level flatcars for automobiles | Specialized; 3 levels = 15-20 vehicles/car |
| **Coil / steel** | Flatcars with cradles for steel coils | Steel industry supply chain |

**Double-stack intermodal:** The most efficient land freight movement available. Two ISO containers stacked on a flatcar. A double-stack train of 300 cars carries 600 containers. The clearance requirement (over 7 metres) means double-stack is impossible in most of Europe and restricted in the US where tunnels were built in the 19th century.

---

## Interoperability Challenges

Rail interoperability is the network compatibility problem taken to national scale.

```
  INTEROPERABILITY BARRIERS:

  1. GAUGE BREAK
     Spain (1,668mm) -> France (1,435mm) at border
     Russia (1,520mm) -> Europe (1,435mm) at Belarus/Poland border
     Solutions: bogie exchange (slow), variable-gauge axles (expensive),
                gauge-adjusting stations (Talgo trains)

  2. SIGNALING INCOMPATIBILITY
     Europe had 20+ national ATP systems before ETCS
     Pre-ETCS: trains needed 4-5 different cab-signal systems
               to run Amsterdam -> Paris -> Frankfurt -> Vienna
     Solution: ETCS mandate (still not fully deployed, 2024)

  3. ELECTRIFICATION INCOMPATIBILITY
     Multiple voltages and frequencies (see traction table above)
     Solution: multi-system electric locos (4-system Eurostar e320)

  4. LOADING GAUGE
     British loading gauge (kinematic) is smaller than continental
     Prevents standard continental wagons running on UK routes
     HS2 designed to continental loading gauge for future through-running

  5. COUPLING SYSTEMS
     Screw coupling (European conventional) vs automatic couplers (US/freight)
     Scharfenberg couplers (European metro/commuter) not compatible

  THE RESULT:
  An interoperable EU freight corridor requires:
  - Multi-system loco
  - ETCS-equipped cab
  - Correct loading gauge
  - Correct bogie profile for each network
  - Route-specific operational knowledge
  Cost of interoperability >> cost of single-system operation
```

The EU's TSI (Technical Specifications for Interoperability) are the regulatory framework mandating compatibility standards — a decades-long project analogous to standardizing internet protocols across 27 national "internets."

---

## Decision Cheat Sheet — Rail Segment Selection

| Requirement | Solution |
|-------------|----------|
| High-volume urban corridor, 60,000+ pphpd | Heavy metro, grade-separated |
| Urban corridor, 15,000-40,000 pphpd, lower cost | LRT with dedicated lanes |
| Urban corridor, flexible, lower capital | Full BRT (not BRT-lite) |
| Intercity, 200-1,200 km, dense corridor | High-speed rail if density supports |
| Intercity, lower density | Conventional rail or air |
| Heavy freight, bulk commodity | Unit train, Class I freight railroad |
| Container freight, intermodal | Double-stack intermodal train |
| Non-electrified branch, no freight | Diesel multiple unit (DMU) |
| Cross-border European operation | ETCS Level 2 + multi-system loco |

---

## Common Confusion Points

**HSR and conventional rail cannot easily share track**
Mixing freight (heavy, slow) and HSR (light, fast) on the same track creates scheduling conflicts and track wear incompatibility. Real HSR is dedicated ROW. The Acela in the US is not HSR by European/Asian standards — it shares track with freight and Amtrak regional trains, limiting max speed.

**CBTC is different from ETCS**
CBTC is a proprietary-era moving block system designed for urban metros (high frequency, short distances). ETCS is the standardized European system for mainline/HSR. They serve different markets and are not interoperable.

**Gauge is not the only interoperability barrier**
Even if two systems share gauge (like the UK and France via Channel Tunnel), voltage, loading gauge, signaling, and operational rules all need compatibility. The Eurostar required a custom locomotive to handle all variations.

**Leaf fall is a real operational crisis**
Autumn leaf contamination on rails creates a compressed film that reduces adhesion to mu=0.02-0.05 — near frictionless. UK railways have high-pressure Sandite (sand+gel) trains that run at night before the service day. The timetable is padded in autumn to accommodate worse performance. This is a solved engineering problem but never entirely eliminated.

**Unit train economics vs intermodal**
Unit trains (coal, grain) are more efficient because there is no switching. But they require that both origin and destination are large single-commodity facilities. Intermodal is more flexible (any port to any inland facility) at slightly higher per-unit cost.
