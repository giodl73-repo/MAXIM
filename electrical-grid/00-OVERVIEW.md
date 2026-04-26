# Electrical Grid — Overview
## The Largest Coordinated Machine Ever Built

---

## The Big Picture

```
GENERATION              STEP-UP TX    HV TRANSMISSION           DISTRIBUTION       END USE
(10 MW–1500 MW units)                 (230 kV – 765 kV)         (4–35 kV)

┌─────────────┐  GSU      ┌──────────────────────────────┐  Substation  ┌─────────┐  Service TX  ┌────────────────┐
│  Coal/Gas   │  13.8kV   │                              │  230→12.4kV  │ Primary │  12.4kV→240V │ 120/240V       │
│  Nuclear    │───────────▶  HV Transmission Backbone    │──────────────▶ Feeder  │──────────────▶ Residential    │
│  Hydro      │  →500 kV  │  (hundreds of miles)         │              │ (miles) │              │                │
│  Wind/Solar │           │                              │              │         │              │ 480V/208V      │
└─────────────┘           └──────────────────────────────┘              └─────────┘              │ Commercial     │
                                                                                                  └────────────────┘

VOLTAGE LADDER:
  Generator terminal:      13.8 kV – 25 kV
  Generator step-up (GSU): 13.8 kV → 230/345/500/765 kV
  HV/EHV Transmission:     230 kV / 345 kV / 500 kV / 765 kV
  Sub-transmission:         69 kV – 138 kV
  Primary distribution:     4.16 kV – 34.5 kV (12.47 kV most common US)
  Secondary service:        120/240V single-phase (residential US)
                            208/480V three-phase (commercial/industrial)
```

---

## The Fundamental Problem: No Buffer

Every other large distributed system has caching and queues. The electrical grid has none at the wire level.

```
Traditional Distributed System:              The Electrical Grid:

┌──────────┐    ┌─────────┐                 ┌──────────┐    ╔══════════════════╗
│ Producer │───▶│  Queue  │───▶ Consumer    │Generator │───▶║ WIRE — no buffer ║───▶ Load
└──────────┘    └─────────┘                 └──────────┘    ╚══════════════════╝
                    ↑
           Buffer absorbs mismatches         Supply MUST equal demand at every instant.
                                             Imbalance → frequency drifts
                                             Uncorrected drift → cascading failure
```

**The governing constraint:** At 60.0 Hz (North America), every synchronous generator in the Eastern Interconnection rotates at exactly 3600 RPM (2-pole) or 1800 RPM (4-pole). All generators are electromagnetically coupled through the transmission network — they must all agree on this single value. This is mandatory distributed consensus without a protocol layer; it emerges from physics.

- Generation > Load: rotor shafts accelerate → frequency rises above 60 Hz
- Generation < Load: rotors decelerate (kinetic energy extracted from spinning mass) → frequency drops
- Operating target: 60.000 Hz ± 0.036 Hz (NERC standard for normal operations)

This real-time balance requirement is what makes the grid fundamentally different from all other infrastructure. There is no packet retransmission. There is no retry. An imbalance that isn't corrected in seconds becomes a cascade failure in minutes.

---

## The Three North American Interconnections

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                     NORTH AMERICAN GRID STRUCTURE                            │
│                                                                              │
│  ┌────────────────────────────────────────────────────────────────────────┐  │
│  │                   EASTERN INTERCONNECTION                              │  │
│  │   ~700 GW installed capacity                                           │  │
│  │   26 states + eastern Canada (Ontario, Quebec, Maritime provinces)     │  │
│  │   ISOs/RTOs: PJM, MISO, SPP, SERC, NYISO, ISO-NE, IESO (Ontario)     │  │
│  │   The largest synchronously connected AC system on Earth by load       │  │
│  └────────────────────────────┬───────────────────────────────────────────┘  │
│                               │  DC ties only (back-to-back converters)      │
│  ┌────────────────────────────▼───────────────────────────────────────────┐  │
│  │                   WESTERN INTERCONNECTION                              │  │
│  │   ~300 GW installed capacity                                           │  │
│  │   11 western US states + 2 Canadian provinces + N. Baja Mexico        │   │
│  │   ISOs/RTOs: CAISO, WECC-coordinated areas, BPA (Bonneville)          │   │
│  └────────────────────────────┬───────────────────────────────────────────┘  │
│                               │  DC ties only                                │
│  ┌────────────────────────────▼───────────────────────────────────────────┐  │
│  │                   ERCOT (Texas)                                        │  │
│  │   ~90 GW installed capacity                                            │  │
│  │   Most of Texas (not El Paso, Panhandle — those are in EI/WI)         │   │
│  │   Single control area — unique in North America                        │  │
│  │   Intentionally isolated: avoids federal FERC jurisdiction             │  │
│  │   Consequence: minimal mutual aid during ERCOT-wide emergency         │   │
│  └────────────────────────────────────────────────────────────────────────┘  │
│                                                                              │
│  KEY: The interconnections are NOT synchronously connected to each other.    │
│  They each run at 60 Hz independently. DC ties (back-to-back converters)    │
│  allow controlled power flow without synchronization. This is identical to  │
│  the architectural choice of isolated failure domains connected by async     │
│  message passing rather than synchronous RPC.                               │
└──────────────────────────────────────────────────────────────────────────────┘
```

**Why separate interconnections?** Synchronous coupling means a fault propagates instantaneously across all electromagnetically connected generators. Isolating ERCOT from the Eastern and Western interconnections limits cascade propagation — the same tradeoff as network partitioning in distributed systems. The cost: no neighbor to call for emergency power imports.

---

## AC vs DC: Why Tesla Won, and Why DC Is Coming Back

### Why AC Won (1880s–1900s)

The core physics: transformers work on Faraday's law (dΦ/dt — time-varying magnetic flux). Transformers require AC. Transformers enable efficient voltage transformation. Edison's DC could not be stepped up economically, so generators had to be near loads. Typical Edison DC distribution radius: ~1 mile from Pearl Street Station, NYC (1882).

```
Edison's DC world (1882):              Tesla/Westinghouse AC world (1888+):
  Generator terminal: 110V DC            Generator terminal: ~2,300V AC
  Copper wire: very large gauge          Step up to 10,000V+ at substation
  I²R losses: severe at any distance    Transmission at high V, low I → low loss
  Service radius: ~1 mile               Niagara Falls → Buffalo: 26 miles (1896)
  Cost: massive copper investment        Then 100 miles, then transcontinental
```

The physics argument quantified: P = IV. For a given power P, doubling V halves I. Since losses = I²R, doubling V cuts losses by 4×. Transmitting at 500 kV vs 13.8 kV means I is 36× smaller → losses 1,296× lower for the same wire resistance.

### Why DC Is Coming Back (HVDC)

For specific use cases, DC is now superior to AC:

| Use Case | Why HVDC Wins |
|----------|--------------|
| Submarine cable (>50 km) | AC cable acts as a capacitor; capacitive charging current dominates at length → almost no real power delivered. DC has no such limit. |
| Asynchronous interconnection | HVDC links two AC systems without requiring frequency synchronization. The Pacific DC Intertie (CA–OR–WA) operates without the two ends being in sync. |
| Very long distance (>800 km) | HVDC losses are lower than AC over very long distances, even including converter station losses (~0.6% per 100 km for DC vs ~1-2% for AC including reactive losses). |
| Underground cable (long) | Same capacitive issue as submarine. London, NYC, urban underground systems increasingly HVDC. |
| Controllability | Power flow in AC networks is governed by impedance ratios (Kirchhoff) — you can't easily direct where power goes. HVDC sets power flow precisely and quickly. |

Major HVDC projects: Pacific DC Intertie (±500 kV, 3,100 MW, 1,362 km Oregon→California), China's Changji–Guquan (±1,100 kV, 12,000 MW, 3,324 km — world's longest), BritNed (450 kV, 1,000 MW, Netherlands→UK).

---

## Capacity Factor vs Nameplate Capacity

This single concept explains more energy policy confusion than anything else.

```
NAMEPLATE CAPACITY = maximum rated output under ideal conditions (MW)
ACTUAL GENERATION  = energy generated in a year (MWh)
CAPACITY FACTOR    = Actual MWh / (Nameplate MW × 8,760 hours/year)
```

**Example:** A 1,000 MW nuclear plant running at 92% CF generates 8,059 GWh/year.
A 1,000 MW solar farm in the US Southwest at 28% CF generates 2,453 GWh/year.
Same nameplate. 3.3× different annual output.

| Source | Typical CF | Range | Key driver |
|--------|-----------|-------|------------|
| Nuclear | 92% | 85–94% | Refueling cycle ~18 months; outages planned |
| Geothermal | 85% | 75–95% | Continuous thermal resource |
| Run-of-river hydro | 40–50% | 25–60% | Seasonal river flow |
| Reservoir hydro | 30–60% | varies | Operator-controlled dispatch |
| Coal (US, 2024) | 38% | 20–60% | Economic dispatch below renewables |
| CCGT (baseload) | 55% | 40–70% | Dispatched when gas is competitive |
| CCGT (peaker) | 10% | 5–20% | Only for peak hours |
| Offshore wind | 45% | 35–55% | Higher, more consistent wind resource |
| Onshore wind | 35% | 25–48% | Site-dependent; Texas Panhandle ~48% |
| Utility solar PV | 25% | 18–32% | US SW hits 30%; Seattle ~15% |
| Simple-cycle gas | 8% | 1–20% | Emergency/peaking only |
| Residential solar | 15% | 10–20% | Roof orientation, shading |

**Dispatchability is the other axis.** A 35% CF wind farm and a 38% CF coal plant have similar annual outputs, but the coal plant can be ramped on command. The wind farm generates when the wind blows. "When you need it" is the dimension capacity factor doesn't capture.

---

## The Load Curve and Dispatch Stack

```
TYPICAL WEEKDAY LOAD CURVE (Eastern US, Summer weekday)

Demand
(GW)
 550 │                         ╭──────────────────╮
     │                    ╭───╯  Afternoon AC     ╰──╮
 500 │             ╭──────╯      peak (~3pm)          ╰─╮
     │      ╭─────╯  Morning                            ╰─╮
 450 │  ╭───╯       ramp                                  ╰───╮
     │╭─╯                                                      ╰─────╮
 400 │╯  Overnight minimum                                           ╰─
     │   (hydro + nuclear + some coal)
 350 │
     └────────────────────────────────────────────────────────────────▶
      12am  3am  6am  9am  12pm  3pm  6pm  9pm  12am

DISPATCH STACK (how generators are called in order of marginal cost):

Marginal  ┌─────────────────────────────────────────────────────────────────┐
Cost      │                                                          ┌──────┐│
$/MWh     │                                                     ┌────┤Peaker││ Oil/gas CT
 $150+    │                                                 ┌───┤    ├──────┘│ ~$120-200/MWh
          │                                             ╔═══╪   │           │
  $80     │                                         ╔═══║ D │ C │           │ D=Demand
          │                                     ╔═══║   ║   │   │           │ Response
  $50     │                            ╔══════╗ ║   ║   ║   │   │           │ C=Coal
          │               ╔════════════║ CCGT ║═╝   ║   ║   │   │           │ B=CCGT gas
  $30     │ ╔═════════════║            ╠══════╝     ║   ║   │   │           │
          │ ║  Nuclear,   ║            ║            ╚═══╝   │   │           │
  $5      │ ║  hydro,     ║  Wind/Solar║                    │   │           │
          │ ║  wind/solar ║  (variable)║                    └───┘           │
   $0     │─╚═════════════╚═══════════╚════════════════════════════════════╝│
          └────────────────────────────────────────────────────────────────▶┘
                                         ← Load →
```

**Merit order effect on prices:** When large amounts of zero-marginal-cost wind and solar enter the market, they push all other generators to the right of the dispatch stack, suppressing wholesale electricity prices. In Germany (Energiewende), high solar penetration caused wholesale prices to drop near zero and occasionally negative during sunny middays — even forcing payments to consumers to take electricity. This is the "cannibalization" problem for renewable economics: more renewables → lower prices → lower revenue for those same renewables.

---

## The Duck Curve: Why High Solar Creates Its Own Problem

California's CAISO grid operators coined this term circa 2013 as solar penetration grew.

```
NET LOAD CURVE (Total load MINUS solar generation) — California, March/April

Net Load
(GW)
  30 │╲                                                              ╭──
     │  ╲  Morning demand                                           ╭╯
  25 │   ╲ before solar              "Duck's back"           ╭─────╯  Evening
     │    ╲ peaks                    (evening demand)       ╭╯        peak &
  20 │     ╰────────────╮──────────────────────────────────╯         steep ramp
     │                  ╰────────────────────────────╯
  15 │                  Midday solar surplus            ▲
     │                  (low/negative net load)    13 GW ramp
  10 │                                              in 3 hours
     └────────────────────────────────────────────────────────────────▶ hour
      6am   9am   12pm  3pm   6pm   9pm

Three problems this creates:
1. Steep RAMP RATE: 13 GW in 3 hours at sunset → needs fast-responding gas or storage
2. Midday MINIMUM may go negative without curtailment or exports (pay someone to take power)
3. OVERGENERATION: must curtail solar or export to neighbors — in 2023, CA curtailed
   ~3 TWh of solar (wasted)
```

The designed-for solution is battery storage (charge at noon when solar is cheap, discharge at 7pm when it's expensive). This is the primary economic driver for the 4-hour battery storage buildout in California.

---

## Carbon Intensity by Generation Source

```
LIFECYCLE CO₂e EMISSIONS (grams CO₂ equivalent per kWh, IPCC median estimates)

Coal (subcritical):      820 g/kWh  ████████████████████████████████████████████
Coal (supercritical):    740 g/kWh  █████████████████████████████████████████
Oil/Distillate:          650 g/kWh  █████████████████████████████████████
Natural gas (CCGT):      490 g/kWh  ████████████████████████████
Natural gas + CCS:        49 g/kWh  ███
Biomass (varies widely): 230 g/kWh  ████████████
Solar PV (utility):       48 g/kWh  ███
Concentrating solar:      27 g/kWh  ██
Hydro (reservoir):        24 g/kWh  ██
Nuclear:                  12 g/kWh  ▌
Wind (onshore):           11 g/kWh  ▌
Wind (offshore):          12 g/kWh  ▌

Includes manufacturing, construction, operations, decommissioning.

2024 context:
  US average grid:       ~380 g/kWh (improving ~2-3% annually as coal retires)
  France (80% nuclear):   ~56 g/kWh
  Germany (coal+RE mix): ~350 g/kWh (high despite large renewable build-out)
  Sweden (hydro+nuclear):  ~13 g/kWh
  Poland (coal-heavy):   ~650 g/kWh
```

**Important: marginal vs average carbon intensity.** The average grid carbon intensity tells you what the average kWh costs in CO₂. The marginal carbon intensity tells you the CO₂ cost of one more kWh of demand (or equivalently, the CO₂ savings from one more kWh of efficiency/storage). In a grid with nuclear baseload + gas peakers, the marginal unit during peak hours is a gas peaker at ~490 g/kWh even if the grid average is 200 g/kWh. EV charging at night on a nuclear-heavy grid is very different from charging at 7pm when gas peakers are on.

---

## Full Grid Taxonomy

```
LAYER                VOLTAGE RANGE       KEY EQUIPMENT               OPERATORS
──────────────────────────────────────────────────────────────────────────────────
Generation           0.4–25 kV           Turbine-generators,         GENCOs, IPPs,
(source)             (terminal)          excitation systems,         vertically
                                         auxiliary power systems      integrated utilities

Generator Step-Up    13.8kV → 230-765kV  GSU transformer,            Generator owner
Transformer                              disconnect switches,
                                         generator breaker

HV Transmission      69 kV – 765 kV AC   Transmission lines          Transmission
(backbone)           ±200–800 kV DC      (ACSR conductors), towers,  Owner (TO)
                                         substations, CB arrays      RTO/ISO

Sub-Transmission     26 kV – 69 kV       Lower-voltage HV lines      Utility or TO

Bulk Transmission    Varies              Bus, transformers,           Utility, DISCO
Substation                               protective relays, breakers

Primary Distribution 4.16 kV – 34.5 kV  Overhead/underground        Distribution
                     (12.47 kV typical)  feeders, reclosers,         utility (DISCO)
                                         sectionalizing switches,
                                         capacitor banks, regulators

Distribution         ~25 kV → 120/240V   Pole-mounted or             Utility
Transformer                              pad-mount transformers

Secondary Service    120V – 600V         Service drop, meter,        Utility + customer
                                         service entrance,
                                         load center / panel

Distributed Energy   1W – 20 MW          Rooftop solar, batteries,   Customer, aggregator,
Resources (DER)                          EV chargers, fuel cells,    DISCO coordination
                                         smart thermostats
```

---

## The Grid as a Distributed Real-Time System

For anyone with large-scale distributed systems background, the grid is the most demanding real-time distributed system in existence. Beyond the real-time control challenge, AC power flow is a continuous constrained optimization problem: the dispatcher solves an optimal power flow (OPF) — minimize generation cost subject to KCL/KVL balance, thermal line limits, and voltage bounds — every few minutes. The DC approximation is a linear program; the full AC OPF is nonlinear/non-convex. The analogies are exact:

| Distributed Systems Concept | Electrical Grid Equivalent |
|-----------------------------|---------------------------|
| **Consensus protocol** (Raft, Paxos) | Grid frequency (60.000 Hz) — all synchronous generators must agree on this single value; it emerges from physics, not software |
| **Byzantine fault tolerance** | N-1 contingency planning — system must remain stable and serve all load despite any single component failure |
| **Message propagation speed** | Electromagnetic propagation at ~0.97c — effectively zero delay vs mechanical response time |
| **Cache / message queue** | Energy storage (pumped hydro, batteries) — the grid has almost no native buffering; storage is expensive and limited |
| **Load balancer** | Economic dispatch + AGC (Automatic Generation Control) — continuously allocates generation to match load |
| **Circuit breaker (Hystrix pattern)** | Protection relay + circuit breaker — detects fault, isolates faulted segment in < 100 ms, redistributes load |
| **CAP theorem** | Grid can't sacrifice Consistency (frequency) or Availability (serving load) — Partition tolerance managed by DC tie isolation |
| **Eventual consistency** | Frequency restoration via AGC — after a disturbance, returns to exactly 60.000 Hz within minutes, not immediately |
| **Cascading failure (thundering herd)** | Grid cascade — one line trip overloads neighbors, exponential cascade; 2003 Northeast Blackout, 55M people |
| **Microservice isolation / bulkheads** | Microgrid islanding — local system survives external failure by disconnecting at controlled boundary |
| **Rate limiting / admission control** | Under-frequency load shedding (UFLS) — automatically drops load to match remaining supply |
| **Health check / heartbeat** | PMU (Phasor Measurement Unit) measurements — GPS-synced, 30-120 samples/sec, real-time situational awareness |
| **Configuration drift** | Transmission topology changes — must track line status in real-time for accurate power flow models |

The critical difference from software distributed systems: in software, a cascade failure means slow responses or errors. In the grid, a cascade failure means no lights, no heat, no water pumping, no hospital power. The consequences are physical and immediately life-safety.

---

## Key Numbers to Internalize

| Metric | Value |
|--------|-------|
| US total installed generation capacity (2024) | ~1,250 GW |
| US annual electricity generation | ~4,200 TWh/yr |
| US average demand | ~480 GW |
| US summer peak demand | ~750 GW (extreme heat event) |
| Eastern Interconnection installed capacity | ~700 GW |
| Western Interconnection | ~300 GW |
| ERCOT | ~90 GW |
| Transmission EHV range | 500–765 kV AC; ±500–800 kV DC |
| North American nominal frequency | 60.000 Hz |
| NERC frequency tolerance (normal) | ±0.036 Hz |
| UFLS begins (automatic load shedding) | ~59.3–59.7 Hz (varies by utility) |
| Frequency at which generators trip offline | ~57–58 Hz (underfrequency protection) |
| Largest single generating unit (US) | Grand Coulee Dam: 6,809 MW |
| World's largest single unit | Three Gorges Dam: 22,500 MW |
| US average retail electricity price | ~13¢/kWh (2024; range: 10–30¢) |
| Wholesale electricity price (normal operations) | $20–80/MWh (varies by region, season) |
| Wholesale price spikes (scarcity events) | Up to $10,000/MWh (ERCOT February 2021) |
| Negative prices (oversupply) | Down to -$50/MWh or below |
| US electricity industry revenue | ~$450B/yr |
| Transmission line losses (typical) | 2–5% (national average ~5%) |
| Distribution losses | 3–7% |
| Total grid losses (US) | ~6% of generation |

---

## Why the Grid Is Hard: The Engineering Constraints

```
CHALLENGE                 WHY IT'S HARD                     MANAGING IT
─────────────────────────────────────────────────────────────────────────────────
Real-time balance         No buffer; supply = demand always  Economic dispatch + AGC
                          (millisecond-to-millisecond)       Governor response
                                                             Demand response
                                                             Storage (limited)

Cascading failure         Power automatically redistributes  N-1 planning
                          (Kirchhoff) when a line trips →    Protection coordination
                          overloads → more trips             Wide-area monitoring

No geographic routing     Power takes paths of least         FACTS devices
                          impedance, not what you want       HVDC for control
                                                             Congestion pricing (LMP)

Reactive power            Q does no work but causes I²      VAr compensation (caps,
                          and voltage drops — must           reactors, STATCOMs)
                          be locally sourced                 Synchronous generators

Inertia erosion           Inverter-based resources (wind,    Grid-forming inverters
(high-RE grids)           solar) contribute zero            Virtual inertia
                          synchronous inertia               Fast frequency response

Equipment age             Average US transmission           Modernization programs
                          transformer: >40 years old        Smart grid investment
                          Many substations predate          Infrastructure bills
                          digital controls
```

---

## Decision Cheat Sheet

| Question | Short Answer |
|----------|-------------|
| Why high voltage transmission? | P=IV; high V → low I → low I²R losses; 500 kV vs 13.8 kV = 1,296× lower losses |
| Why AC for bulk grid? | Transformers require AC; transformers enable economical voltage stepping |
| When does HVDC beat HVAC? | Submarine cable > 50 km; asynchronous interconnection; >800 km distance |
| What is capacity factor? | Actual MWh / (nameplate MW × 8,760h); nuclear 92%, solar 25%, wind 35% |
| What maintains 60.00 Hz? | Spinning inertia of synchronous generators + governor response + AGC |
| What happens if generation suddenly drops? | Frequency drops; if uncorrected → UFLS → cascade risk |
| What is the duck curve? | Net load (load minus solar) creates midday surplus + steep evening ramp |
| What is merit order dispatch? | Generators called in order of marginal cost; cheapest first (nuclear, hydro, wind/solar, then gas, then peakers) |
| What drives wholesale price? | Marginal unit; last unit dispatched sets clearing price for all |
| Hardest part of high-renewable grids? | Variability + zero synchronous inertia from inverters + transmission constraints |
| Most dangerous failure mode? | Cascading failure — automatic power redistribution via Kirchhoff → overloads → exponential cascade |

---

## Common Confusion Points

**Capacity vs energy**: "The US has 200 GW of solar" is nameplate MW. Annual output = 200,000 MW × 8,760h × 0.25 = 438 TWh, which is ~10% of total US electricity. Nameplate makes solar sound bigger than it is for annual energy supply.

**Power vs energy**: Power = MW (instantaneous rate). Energy = MWh (power integrated over time). The grid must balance power at every instant, not just annual energy totals. A windstorm at 3am generates power when you don't need it; a heat wave at 6pm needs power when wind isn't blowing.

**Frequency vs voltage**: Two distinct stability problems. Frequency is system-wide (Eastern Interconnection is one coupled frequency). Voltage is local (can vary by 5-10% from node to node). Both can fail independently.

**"The grid is one machine"**: Each interconnection is one synchronous machine. But there are three separate AC interconnections in North America, connected only via DC ties. The Eastern Interconnection doesn't care what frequency ERCOT is running at, and vice versa.

**Marginal vs average carbon**: The grid average carbon intensity is what you see in reports. The marginal carbon intensity is what actually changes when you add or remove a kWh. Often 2-3× different during peak hours (gas peakers at margin vs nuclear baseload in average).

**Renewable energy percentages**: When you see "X% renewable electricity," this is usually percentage of annual energy generated (MWh), not percentage of installed capacity (MW) and not percentage of hours powered at 100% renewables. These can be dramatically different numbers.

---

*Next: 01-GENERATION.md — thermal plants, nuclear, hydro; heat rate, efficiency, dispatchability*
*See also: 05-GRID-STABILITY.md for frequency dynamics; 08-MARKETS.md for merit order pricing detail*
