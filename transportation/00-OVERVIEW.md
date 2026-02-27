# Transportation Systems — Landscape Overview

## The Big Picture

Five modes move all people and freight on Earth. Each has distinct physics, economics, and geography. They compete on some corridors and complement on others.

```
+------------------------------------------------------------------+
|                    TRANSPORTATION LANDSCAPE                       |
|                                                                  |
|  INFRASTRUCTURE LAYER (fixed, capital-intensive, long-lived)     |
|  +----------+ +---------+ +---------+ +---------+ +---------+   |
|  |   RAIL   | |  ROAD   | |   AIR   | |MARITIME | |PIPELINE |   |
|  | Track    | | Highway | | Airport | | Port    | | Pipe    |   |
|  | $2-50M/km| | $1-10M  | | $500M+  | | $500M+  | | $1-5M/km|   |
|  | 50-100yr | | 30-50yr | | 40yr    | | 50+yr   | | 40-50yr |   |
|  +----------+ +---------+ +---------+ +---------+ +---------+   |
|                                                                  |
|  VEHICLE LAYER (mobile, replaceable, shorter-lived)              |
|  +----------+ +---------+ +---------+ +---------+ +---------+   |
|  | Loco/    | | Truck/  | | Aircraft| | Ship    | | Pump/   |   |
|  | Railcar  | | Car/Bus | |         | |         | | Compress|   |
|  | 25-40yr  | | 5-20yr  | | 20-25yr | | 20-30yr | | station |   |
|  +----------+ +---------+ +---------+ +---------+ +---------+   |
|                                                                  |
|  OPERATIONS LAYER (schedules, routing, control)                  |
|  +----------+ +---------+ +---------+ +---------+ +---------+   |
|  | Train    | | Traffic | | ATC /   | | Voyage  | | SCADA   |   |
|  | Control  | | Mgmt    | | dispatch| | routing | | control |   |
|  +----------+ +---------+ +---------+ +---------+ +---------+   |
|                                                                  |
|  DEMAND LAYER (people and freight needing to move)               |
|  Commuters, tourists, freight shippers, energy consumers         |
+------------------------------------------------------------------+
```

Any transportation system = Infrastructure + Vehicles + Operations + Demand. All four must align. A railway without trains is useless; trains without demand are uneconomic.

---

## Modal Share — Where the Traffic Actually Goes

### Global Freight (tonne-kilometres, ~2022)

| Mode | Global Share | Strength | Weakness |
|------|-------------|----------|----------|
| **Maritime** | ~80% | Intercontinental bulk, lowest cost/tkm | Port-to-port only |
| **Road** | ~8% | Door-to-door, flexible, final mile | Energy-intensive, congested |
| **Rail** | ~7% | High-volume corridors, energy-efficient | Inflexible routes, interop challenges |
| **Pipeline** | ~5% | Lowest cost for liquids/gas, continuous | Fixed routes, single commodity |
| **Air freight** | <0.5% | High value, time-sensitive, >4,000 km | 10-100x road cost, emissions |

*Aviation's <0.5% of tonne-km but ~35% of global trade value — it carries the expensive stuff.*

### Global Passenger (passenger-kilometres, ~2022)

| Mode | Approx Share | Key Context |
|------|-------------|-------------|
| **Road (private car)** | ~50% | Dominant in developed economies |
| **Road (bus/coach)** | ~20% | Dominant in developing economies |
| **Rail** | ~10% | Higher in Asia, Europe; negligible in US |
| **Air** | ~12% | Long-distance, growing fast in Asia-Pacific |
| **Maritime (ferry)** | ~1% | Islands, archipelagos |
| **Urban transit** | ~7% | Metro, LRT, BRT |

---

## Network Economics — Why Transportation is Different

Transportation is a **network industry**. Three cost properties distinguish it from ordinary manufacturing:

```
+---------------------------------------------+
|         NETWORK INDUSTRY ECONOMICS          |
|                                             |
|  1. ECONOMIES OF SCALE                      |
|     Fixed costs >> Variable costs           |
|     Build the track once; run trains cheap  |
|     Average cost falls as output rises      |
|                                             |
|  2. ECONOMIES OF DENSITY                    |
|     More traffic on same route = lower cost |
|     A 70%-full train is far less efficient  |
|     per passenger than the same at 95%      |
|                                             |
|  3. ECONOMIES OF SCOPE                      |
|     Networks of routes share terminals,     |
|     equipment, management                   |
|     Airlines: hub-and-spoke exploits this   |
|                                             |
|  IMPLICATION: Natural monopoly on thin      |
|  routes. Regulation or public ownership     |
|  required. Competition works only where     |
|  demand density is high enough.             |
+---------------------------------------------+
```

These economics explain why:
- Railroads became oligopolies (US Class I railroads — 7 carriers cover 90% of freight)
- Aviation needed deregulation to unlock competition (US 1978, EU 1997)
- Ports are often concessioned to private operators but regulated on rates
- Highways are mostly public (positive externality + natural monopoly)

---

## The Four Components of Any Transport System

Every transport system has these four layers. Failure in any one kills the system.

```
  INFRASTRUCTURE          VEHICLES              OPERATIONS           DEMAND
  ──────────────          ────────              ──────────           ──────
  Fixed, sunk cost        Mobile assets         Real-time mgmt       Derived demand
  Political process       Asset management      Scheduling           Inelastic short-term
  to build/change         Fleet planning        Dispatch             Elastic long-term
                          Maintenance           Control systems

  Examples:               Examples:             Examples:            Examples:
  Track, runway,          Locomotives,          ATC, signaling,      Commuters,
  highway pavement,       aircraft,             GPS tracking,        freight shippers,
  port berths,            trucks, ships         SCADA pipelines      tourists
  pipeline right-of-way
```

**Derived demand** is key: no one travels for the pleasure of traveling. They travel to reach destinations. Freight moves because production and consumption are geographically separated. This is why transport investment without land-use planning fails — you need the destinations to generate demand.

---

## Transportation Geography — Why Mode Depends on Location

Geography is the first-order determinant of modal choice. No optimization model overrides it.

```
  DISTANCE x GEOGRAPHY => MODAL CHOICE

  Short distance, dense city
  +------+     +------+     +-----------+
  | <5km |     | Urban|     | Walk/Bike |
  |      | --> |      | --> | Bus/Metro |
  +------+     +------+     +-----------+

  Medium distance, 50-500km corridor
  +-------+    +----------+    +-------------------+
  | 50-   |    | Corridor |    | Rail (if dense)   |
  | 500km | -> | density? | -> | Road (default)    |
  +-------+    +----------+    | Air (if >300km?)  |
                               +-------------------+
               High density: rail competitive
               Low density: road wins

  Long distance, 500-5,000km
  +--------+    +---------+    +--------------------+
  | 500-   |    | Water   |    | Air (passengers)   |
  | 5000km | -> | cross?  | -> | Maritime (freight) |
  +--------+    +---------+    | HSR (<1,500km pax) |
                               +--------------------+

  Very long distance, >8,000km
  +--------+    +---------------------------+
  | 8000+  | -> | Air (passengers)          |
  | km     |    | Maritime (freight, ~97%)  |
  +--------+    +---------------------------+
```

**Geography rules of thumb:**
- Rail competitive at 200-1,500 km for passengers when population density supports it
- Maritime cheapest for freight over any water crossing
- Pipeline cheapest for bulk liquids/gas over any land distance at high volume
- Air wins >1,000 km for passengers where speed premium justifies cost
- Dense urban corridors: transit outperforms road on throughput per lane-metre

---

## Braess's Paradox — The Distributed Systems Analogy

In 1968, Dietrich Braess proved that **adding a road to a network can increase everyone's travel time**. This is counterintuitive and important.

```
  ORIGINAL NETWORK (two parallel routes, equilibrium = 65 min each):

      t=45+x          t=45+x
  S ----[A]------- T
  |                |
  +------[B]-------+
      t=45+x

  Where x = fraction of drivers on that route (0 to 1).
  At equilibrium: all routes have equal travel time.

  ADD A ZERO-COST SHORTCUT from A to B:

  S ----[A]------- T
  |      |         |
  |    [0 min]     |
  |      |         |
  +------[B]-------+

  NOW: Every rational driver takes S->A->shortcut->B->T
  Everyone's time: 45+1 + 0 + 45+1 = 92 minutes.
  Worse than the original 65 minutes for everyone.

  WHY: Nash equilibrium != social optimum.
       Each driver optimizes individually.
       No global coordinator exists.
```

**The software systems analogy is exact**: adding a fast cache path everyone uses creates a bottleneck worse than the original. Adding a microservice shortcut that every other service calls creates a single point of failure. The lesson: **selfish routing without global coordination produces suboptimal outcomes**. Congestion pricing, traffic management centers, and centralized dispatching exist to approximate the social optimum that decentralized actors cannot find.

**Induced demand** is the flip side: adding road capacity reduces travel time, attracting new trips, eventually restoring congestion. Adding lane-miles to a congested highway produces only short-term relief if induced demand is strong. (This is why some cities stop adding highway capacity and invest in alternatives instead.)

---

## The Decarbonization Imperative

Transport is **16% of global GHG emissions** (~7.5 GtCO2e/year). Harder to decarbonize than electricity because of vehicle energy density requirements.

```
  TRANSPORT GHG BY MODE (approximate)
  +-----------------------------------------+
  |  Road (cars + trucks)  ████████████  72% |
  |  Aviation              ████          12% |
  |  Maritime              ████          11% |
  |  Pipeline (fugitive)   ██             4% |
  |  Rail                  █              1% |
  +-----------------------------------------+

  DECARBONIZATION PATHWAYS BY MODE:

  MODE        PATHWAY                     STATUS          TIMELINE
  ----        -------                     ------          --------
  Road        Battery electric (BEV)      Scaling now     2030-2040
              Hydrogen fuel cell (heavy)  Commercial      2030-2035
  Rail        Electrification (overhead)  ~50% done       2030-2040
              Battery/hydrogen hybrids    Early deploy    2025-2035
  Aviation    Sustainable Aviation Fuel   <5% supply      2030-2050
              Hydrogen aircraft           Pre-commercial  2040-2050
              Battery-electric (<500 km)  Early           2030-2035
  Maritime    Methanol (Maersk pathway)   First ships     2025-2035
              Ammonia (zero-carbon)       Pilot stage     2030-2045
              Wind assist (Flettner)      Deploying       2025-2030
              LNG (bridge fuel)           Mainstream      Now-2035
  Pipeline    Hydrogen repurposing        Planning        2030-2040
```

Rail is the easiest (already partly electric, low rolling resistance). Road passenger is next (BEV). Maritime and aviation are the hard ones — energy density requirements and long asset lives make fast transitions expensive.

---

## Historical Arc — The Five Waves of Transportation

```
  1760s-1840s: CANALS
  +---------+
  | Canal   | Enabled industrial revolution bulk freight
  | Network | Horse towpaths, 3-4 mph, 30 tonnes/boat
  +---------+ Obsoleted by railways within 30 years

  1830s-1900s: RAILWAYS
  +-----------+
  | Rail      | First mass intercity mobility for people
  | Network   | Steam then electric; 20-100 mph
  +-----------+ Created first national markets; vertical monopolies

  1900s-1960s: ROADS
  +----------+
  | Highway  | Automobiles + interstate highway systems
  | Network  | Flexible door-to-door; federally subsidized
  +----------+ Hollowed out rail passenger in US/Canada

  1950s-1970s: AVIATION
  +-----------+
  | Air       | Jet age: Boeing 707 (1958), 747 (1969)
  | Network   | Replaced ocean liners for passenger travel
  +-----------+ Hub-and-spoke restructuring after deregulation (1978 US)

  1956: CONTAINERIZATION — The McLean Revolution
  +---------------+
  | Intermodal    | Malcolm McLean's first container ship (Ideal-X)
  | Containers    | ISO standard container adopted 1961
  +---------------+ Slashed port labor costs ~90%
                   Enabled global supply chains at scale
                   The internet of physical goods movement

  Modern: INTERMODAL INTEGRATION
  All five modes linked by standardized containers,
  EDI/APIs, real-time tracking, global logistics platforms
```

**The McLean Revolution deserves emphasis.** Before containerization, break-bulk cargo required armies of dock workers loading/unloading individual items. A container ship now loads in hours what took weeks. The fully-loaded cost per tonne of shipping dropped by an order of magnitude. This single 1956 innovation made the modern global supply chain possible. Every server rack shipped to a Microsoft data center arrived via container ship.

---

## Key Metrics — What Transportation Measures

| Metric | Definition | Typical Range |
|--------|-----------|---------------|
| **pkm** | Passenger-kilometre: 1 person x 1 km | Airline: 10B pkm/yr (medium carrier) |
| **tkm** | Tonne-kilometre: 1 tonne x 1 km | Container ship: 50B+ tkm/voyage |
| **Load factor** | Actual / available capacity | Aviation target: 85%+; rail varies |
| **On-time performance** | % arrivals within threshold | Shinkansen: 99.9%, <18s avg delay |
| **Deaths/Bpkm** | Fatalities per billion passenger-km | Air: 0.07, Rail: 0.06, Road: 7.3 |
| **Fuel intensity** | pkm or tkm per litre (or kWh) | Maritime: 500 tkm/litre fuel oil |
| **CASM** | Cost per available seat-mile (aviation) | LCC: 6-8c, legacy carrier: 12-15c |
| **TEU** | Twenty-foot equivalent unit (containers) | ULCS: 24,000 TEU capacity |
| **pphpd** | Persons per hour per direction (transit) | Metro: 60,000+; BRT: 15,000 |

**Safety note:** Rail and aviation are roughly 100x safer than road per pkm. The perception is inverted because large aviation accidents dominate news; 1.35M annual road deaths are invisible, distributed across millions of incidents.

---

## The Microsoft Data Center Supply Chain Bridge

Microsoft's infrastructure operations depend on all five modes simultaneously:

```
  SERVERS FOR AZURE DATA CENTERS — FULL SUPPLY CHAIN

  Taiwan/South Korea              Singapore/Malaysia
  (chip fab: TSMC, Samsung)       (assembly: Foxconn, Flextronics)
        |                                |
        | MARITIME (container)           | MARITIME
        | Taiwan->Seattle: ~14 days      | Singapore->Rotterdam: ~20 days
        v                                v
  US West Coast Ports            Rotterdam/Hamburg ports
  (Long Beach, Seattle)                  |
        |                                | ROAD (truck)
        | RAIL (intermodal)              | Last mile to DC
        | Double-stack to Midwest        v
        v                          Azure DC Frankfurt/Dublin
  Distribution Centers
  (Chicago, Dallas hub)
        |
        | ROAD (truck)
        | Last mile to DC location
        v
  Azure US Central/West DC

  AIR: used for urgent replacement parts under SLA
       and for time-critical equipment where sea transit
       would blow delivery commitments
```

When supply chain disruption occurs (COVID-2020, Suez 2021, geopolitical risk on Taiwan Strait), every mode and route above becomes critical path analysis. The same tools — network flow, shortest path, inventory optimization — apply at infrastructure scale as in software systems.

---

## Decision Cheat Sheet — Modal Selection

| If you need to move... | Primary mode | Why |
|------------------------|-------------|-----|
| Bulk commodity, intercontinental | Maritime | Cheapest/tkm |
| Bulk commodity, continental land | Rail (unit train) | Scale economies |
| Container freight, intercontinental | Maritime + intermodal | Standard |
| Time-sensitive high-value freight | Air | Speed premium |
| Liquids/gas, fixed route, high volume | Pipeline | Lowest operating cost |
| People, >1,500 km, speed matters | Aviation | Time value |
| People, 200-1,500 km, dense corridor | High-speed rail | Speed + capacity |
| People, urban commute, high density | Metro / BRT | Throughput |
| People, urban, flexible OD | Car / ride-hail | Flexibility |
| Freight, last mile, urban | Light commercial truck | Door-to-door |

---

## Common Confusion Points

**"Rail is the future" vs "Rail is dead"**
Both are geography-specific. Rail thrives where population density amortizes fixed costs (Europe, Japan, East China). Rail is commercially marginal where it doesn't (US passenger rail). Freight rail is different: US Class I railroads are highly profitable because they haul unit trains of coal, grain, and intermodal over long corridors at high density.

**Pipeline vs other modes for energy**
Pipeline carries ~5% of global tkm and is often omitted from comparisons. For natural gas and crude oil it is 3-10x cheaper per tkm than any alternative. The fossil energy "grid" is the pipeline network — and the hydrogen scenario repurposes it.

**Containerization already happened**
The logistics revolution is 70 years old. The modern challenge is not how to containerize (solved) but how to make container flows visible (supply chain platforms), resilient (multi-sourcing post-COVID), and low-carbon (zero-emission shipping by 2050).

**Decarbonization timelines vary by ~20 years across modes**
Road EVs are near-term (2030s phase-out of ICE sales). Aviation net-zero is 2050 at best. Maritime net-zero requires fuels (ammonia, methanol) that barely exist at commercial scale. Conflating "transport decarbonization" as a single horizon misses this spread entirely.

**Induced demand vs capacity**
Adding road capacity in a congested corridor typically generates enough new traffic within 5-10 years to restore the original congestion level. The empirical elasticity of VMT with respect to lane-miles is approximately 1.0 over the long run (Duranton-Turner 2011). This is why adding capacity is not always the answer — demand management (pricing) is the alternative.

<!-- @editor[content/P2]: EV charging infrastructure absent from directory — explicitly called out in learner calibration as a "DOES need" topic. Covers: charging levels (L1/L2/DC fast/HPC), network topology (home vs public vs fleet depot), range anxiety vs actual behavior, grid impact (V2G, demand response), charging standard wars (CCS vs CHAdeMO vs NACS/Tesla → convergence), battery swapping (NIO), infrastructure planning models. Natural fit in a standalone file or as a major section of 07-AUTONOMOUS-VEHICLES.md (since EV+AV fleet charging is an integrated planning problem). -->
