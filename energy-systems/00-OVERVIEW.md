# Global Energy Landscape — Overview

## The Big Picture

Global primary energy consumption: ~600 EJ/year (~167,000 TWh). Most of it is wasted as heat
before it reaches the end user. The conversion chain is the central fact of energy systems.

<!-- @editor[bridge/P2]: The energy conversion chain (primary → secondary → final → useful, with ~65% lost as waste) is structurally identical to a distributed system's request processing chain: each tier introduces latency and loss. The Carnot-limited thermal plants are the synchronous I/O bottleneck; electrification + heat pumps are the async optimization. The "35% of primary energy becomes useful work" number maps directly to the "useful throughput vs total I/O ops" metric. The transition from centralized thermal generation to distributed VRE is the energy equivalent of moving from mainframe to cloud: both shift from "one big box" to "many commodity units + orchestration layer." The overview already hints at this but doesn't name it directly. -->
```
PRIMARY ENERGY (~600 EJ/yr)
        |
        |  Extraction, mining, drilling, harvesting
        v
+---------------------------------------------------------------+
|  FOSSIL FUELS       |  LOW CARBON          |  RENEWABLES      |
|  Coal  ~25%         |  Nuclear ~5%         |  Solar   ~4%     |
|  Oil   ~31%         |  Hydro  ~7%          |  Wind    ~3%     |
|  Gas   ~23%         |                      |  Bio/Other ~2%   |
+---------------------------------------------------------------+
        |
        |  Conversion (power plants, refineries, boilers)
        |  LOSSES: ~65-70% of primary energy lost as waste heat
        v
SECONDARY ENERGY / ENERGY CARRIERS
  Electricity, refined fuels, district heat
        |
        |  Transmission & distribution losses: ~5-8%
        v
FINAL ENERGY (~400 EJ/yr — what industry/buildings/transport consume)
        |
        +-- Electricity  ~20% of final energy
        +-- Heat          ~50% of final energy (industry + buildings)
        +-- Transport     ~28% of final energy (mostly liquid fuels)
        +-- Non-energy     ~2% (feedstocks, lubricants)
        |
        |  End-use conversion losses
        v
USEFUL ENERGY / ENERGY SERVICES
  Motion, warmth, light, computation
```

The brutal efficiency number: **~35% of primary energy** becomes useful energy services.
The rest is waste heat — mostly from thermal power plants (Carnot limit applies) and
combustion engines. This is why electrification + heat pumps is not just green politics:
it's straightforward thermodynamics.

---

## Energy Units — The Conversion Table

Energy is reported in incompatible units across disciplines. IEA uses EJ. Power sector
uses TWh. US policy uses quads. Your electricity bill uses kWh. Build this table once.

```
+------------------------------------------------------------------+
|                    UNIT CONVERSION MAP                           |
+------------------------------------------------------------------+
|                                                                  |
|  1 EJ (exajoule)         = 10^18 J                              |
|                           = 277.8 TWh                           |
|                           = 23.88 Mtoe                          |
|                           = 948 TBtu                            |
|                           = 0.948 quad (US)                     |
|                                                                  |
|  1 TWh (terawatt-hour)   = 3.6 PJ = 3.6 × 10^15 J             |
|                           = 0.0860 Mtoe                         |
|                           = 3.41 TBtu                           |
|                           = 1,000 GWh = 1,000,000 MWh          |
|                                                                  |
|  1 Mtoe (million tonnes  = 41.87 PJ                             |
|    oil equivalent)        = 11.63 TWh                           |
|                                                                  |
|  1 GJ (gigajoule)        = 0.278 MWh = 0.948 MMBtu             |
|  1 kWh                   = 3.6 MJ = 3,412 BTU                  |
|  1 quad                  = 1.055 EJ                             |
|                                                                  |
+------------------------------------------------------------------+

  Who uses what:
  IEA reports:           EJ and Mtoe
  Power sector:          TWh and GW (capacity) / GWh (storage)
  US EIA, policy:        quads and BTU
  Utility bills:         kWh
  Industrial heat:       GJ or MMBtu
  IPCC scenarios:        EJ
```

**Anchor numbers (2024):**

| Scale | Value |
|-------|-------|
| Global primary energy | ~600 EJ/yr (~167,000 TWh) |
| Global electricity generation | ~30,000 TWh/yr (~108 EJ) |
| Global electricity = % of final energy | ~20% |
| USA primary energy | ~100 EJ/yr (~95 quads) |
| USA electricity generation | ~4,300 TWh/yr |
| 1 GW coal plant @ 80% CF | ~7 TWh/yr |
| 1 GW solar @ 20% CF | ~1.75 TWh/yr |
| Microsoft electricity consumption | ~35-40 TWh/yr (and growing) |

---

## LCOE — Levelized Cost of Energy

LCOE is the most-used (and most-misused) metric for comparing generation technologies.

### The Formula

```
                    NPV(Capex + Opex + Fuel + Decommissioning)
  LCOE ($/MWh)  =  ─────────────────────────────────────────────
                          NPV(Energy Output over lifetime)

  Expanded:

        N   (Capex_t + Opex_t + Fuel_t) / (1+r)^t
        ∑   ──────────────────────────────────────
       t=1         MWh_t / (1+r)^t

  where:
    t = year (1 to project lifetime N, typically 20-35 years)
    r = discount rate (project WACC — 5-8% for utility, 10%+ for merchant)
    Capex_t  = capital expenditure (front-loaded; most in year 0)
    Opex_t   = fixed O&M ($/kW-yr) + variable O&M ($/MWh)
    Fuel_t   = fuel cost (zero for solar/wind)
    MWh_t    = Capacity_MW × 8,760 hr/yr × Capacity_Factor × Degradation_t
```

### What's Inside Each Component

```
+------------------------------------------------------------------+
|  LCOE COMPONENTS — Utility Solar PV Example (2024)              |
+------------------------------------------------------------------+
|  Capital cost (Capex):          ~$900-1,100/kW installed        |
|    Modules (30-35%)                                              |
|    Inverters (8-10%)                                             |
|    Racking/tracking (10-12%)                                     |
|    EPC (labor, civil, electrical) (25-30%)                       |
|    Grid interconnection (8-15%)  ← growing bottleneck           |
|    Development, permitting (10-12%)                              |
|                                                                  |
|  Annual O&M:                     ~$10-15/kW-yr                  |
|    Vegetation management, inverter replacement, monitoring       |
|                                                                  |
|  Capacity factor:                20-30% (US average ~24%)        |
|  Degradation rate:               ~0.5%/yr (linear model)        |
|  Discount rate:                  5-8% (regulated utility)       |
|  Project life:                   25-35 years                     |
|                                                                  |
|  Resulting LCOE:                 ~$30-55/MWh                    |
+------------------------------------------------------------------+
```

### Why LCOE Is Incomplete for Variable Renewables

LCOE was designed for dispatchable baseload plants (coal, gas, nuclear) that produce
reliably on demand. For variable renewables (solar, wind), LCOE systematically
understates what the grid actually pays:

```
  WHAT LCOE CAPTURES:
  +----------------------------------------------+
  | Cost to produce 1 MWh at the generator fence |
  +----------------------------------------------+

  WHAT LCOE MISSES:
  +----------------------------------------------+
  | Grid integration costs:                       |
  |  • Transmission buildout to load centers      |
  |  • Storage (for when sun/wind not available)  |
  |  • Backup/firm capacity (resource adequacy)   |
  |  • Frequency regulation services              |
  |  • Curtailment losses (wasted output)         |
  |  • Grid reinforcement at interconnection point|
  +----------------------------------------------+
  | Value deflation (the cannibalization effect): |
  |  • High solar penetration → midday prices → $0|
  |  • Each additional solar MWh is worth less    |
  |  • Solar LCOE falls, but solar value falls too|
  +----------------------------------------------+

  Better whole-system metrics:
  • System LCOE  = generator LCOE + integration cost
  • VALCOE       = LCOE - (system value of the generator)
                   IEA metric; negative = value exceeds cost
  • LCOS         = Levelized Cost of Storage (separate formula)
```

### 2024 LCOE Benchmarks (Global Average, Utility Scale)

| Technology | LCOE ($/MWh) | Trend |
|------------|-------------|-------|
| Onshore wind | $25-50 | Declining |
| Utility solar PV | $30-55 | Declining (steepest in history) |
| Large hydro | $25-90 | Site-specific; stable |
| CCGT (combined cycle gas) | $45-75 | Fuel-cost sensitive |
| Offshore wind (fixed) | $70-120 | Declining |
| Coal (existing, low marginal cost) | $20-40 | Stranded asset risk |
| Coal (new build) | $65-150 | Economically uncompetitive |
| Nuclear (new build, OECD) | $100-200 | Vogtle ~$180/MWh all-in |
| Nuclear (existing fleet) | $25-40 | Very low marginal cost |

---

## Energy Density — Orders of Magnitude

This single chart explains why storage and transport fuel substitution are hard problems.

```
  GRAVIMETRIC ENERGY DENSITY (MJ/kg — specific energy)
  =====================================================

  Uranium-235 (fission)        ~80,000,000 MJ/kg  ← off the chart
  -----------------------------------------------
  Hydrogen (LHV)                        ~120 MJ/kg
  Natural gas (methane, LHV)             ~55 MJ/kg
  Gasoline / Jet fuel (LHV)              ~44 MJ/kg
  Diesel (LHV)                           ~43 MJ/kg
  Ethanol                                ~27 MJ/kg
  Coal (bituminous)                      ~25 MJ/kg
  Wood (dry)                             ~18 MJ/kg
  -----------------------------------------------
  Li-ion battery (NMC, cell level)    ~0.7 MJ/kg  (195 Wh/kg)
  Li-ion battery (LFP, cell level)    ~0.5 MJ/kg  (140 Wh/kg)
  Li-ion battery (system level)       ~0.3 MJ/kg  (85 Wh/kg)
  Lead-acid battery                   ~0.14 MJ/kg
  -----------------------------------------------
  Compressed air (200 bar)           ~0.15 MJ/kg
  Pumped hydro (100m head)          ~0.001 MJ/kg

  VOLUMETRIC ENERGY DENSITY (MJ/liter)
  =====================================

  Gasoline                  ~34 MJ/L
  Diesel                    ~37 MJ/L
  LNG (liquid natural gas)  ~23 MJ/L
  Liquid hydrogen (-253°C)  ~10 MJ/L  ← poor volumetric density
  H₂ at 700 bar             ~5 MJ/L
  Li-ion (NMC, cell)        ~2.5 MJ/L
  Li-ion (LFP, cell)        ~1.5 MJ/L
  Lead-acid                 ~0.36 MJ/L
  Pumped hydro (100m head) ~0.001 MJ/L
```

**The storage gap in one number:** Gasoline holds ~60× more energy per kg than the best
production Li-ion battery cell, and ~140× more than the full system (pack + BMS + thermal).
This is a physics constraint, not a manufacturing problem. It explains why:
- Long-haul aviation: battery electric is not viable for decades
- Long-haul trucking: marginal (BEV works for some routes, H₂ for others)
- Passenger cars: BEV works fine (range anxiety is psychological, not physical)
- Grid storage: 4-hour Li-ion is fine; seasonal storage requires chemistry or geography

---

## Installed Capacity vs. Generation — The Capacity Factor

A headline "GW" figure without a capacity factor is nearly meaningless for comparing
technologies. This trips up energy journalism constantly.

```
  Technology         Typical CF    Annual GWh per 1 GW installed
  -------            ----------    -----------------------------
  Nuclear            90-95%         7,884 - 8,322 GWh/yr
  Coal (baseload)    70-85%         6,132 - 7,446 GWh/yr
  CCGT               40-60%         3,504 - 5,256 GWh/yr
  Offshore wind      40-55%         3,504 - 4,818 GWh/yr
  Onshore wind       25-40%         2,190 - 3,504 GWh/yr
  Utility solar      15-30%         1,314 - 2,628 GWh/yr
  Rooftop solar      10-18%           876 - 1,577 GWh/yr
  Hydro (run-of-river)30-50%        2,628 - 4,380 GWh/yr
  Pumped hydro       10-15%*          876 - 1,314 GWh/yr*
  (* discharge hours limited by reservoir; 4-12 hours/day peak)
```

**Example:** "China added 200 GW of solar in 2023" sounds enormous.
At 15% CF that's ~263 TWh/yr of generation — roughly equivalent to 30 GW of nuclear
at 90% CF (30 × 7.9 TWh = 237 TWh). Context always requires capacity factor.

---

## Decarbonization Pathways

### IPCC AR6 Scenario Families

```
  Shared Socioeconomic Pathway (SSP) + warming level

  +----------------------------------------------------------------+
  |  SSP1-1.9   Very low emissions. Aggressive mitigation.        |
  |             1.5°C (50% probability) if net zero ~2050         |
  |                                                                |
  |  SSP1-2.6   Low emissions. Strong mitigation. 2°C likely     |
  |                                                                |
  |  SSP2-4.5   Intermediate. Roughly matches current NDC         |
  |             pledges. ~2.5-2.7°C likely.                       |
  |                                                                |
  |  SSP3-7.0   High emissions. Fragmented, regional policies.   |
  |             ~3.6°C likely.                                     |
  |                                                                |
  |  SSP5-8.5   Very high. Fossil-fuel-led development.           |
  |             ~4.4°C likely. "Business as usual" overestimate.  |
  +----------------------------------------------------------------+

  Current trajectory (2024 policies only):  ~2.5-3.0°C
  Current pledges (NDCs, stated policies):   ~2.0-2.4°C
  IEA NZE 2050:                              ~1.5°C (50%)
```

### Carbon Budget Math

```
  Remaining carbon budget (IPCC AR6, Jan 2024 reference):
  ┌─────────────────────────────────────────────────────────┐
  │  1.5°C (50% prob):  ~250 GtCO₂                         │
  │  2.0°C (50% prob): ~1,150 GtCO₂                        │
  │  Current emissions: ~37 GtCO₂/yr                        │
  │                                                          │
  │  1.5°C budget exhausted: ~2031 at current pace          │
  │  2.0°C budget exhausted: ~2055 at current pace          │
  └─────────────────────────────────────────────────────────┘

  Note: budget "exhausted" ≠ automatic failure — the carbon cycle
  has some reversibility. But overshoot requires negative emissions
  (CCS, DAC, BECCS) to come back down. These don't yet exist at scale.
```

### IEA Net Zero Emissions (NZE) 2050 — Key Milestones

```
  2025  No new coal mines or unabated coal power approved
        No new upstream oil/gas beyond replacement of decline
        All new car sales in leading markets must be EV

  2030  Global electricity: 60% clean (vs ~39% in 2023)
        Solar + wind annual additions: 2,400 GW/yr (vs ~500 GW in 2023)
        Coal power: phased out in advanced economies by 2030
        EV share of new car sales: ~60% globally
        Energy intensity improvement: 4%/yr (vs 2% current)

  2035  All new power plants worldwide: zero emissions
        Aviation: 50% SAF (sustainable aviation fuel)

  2040  Global electricity: 80%+ clean
        All new ICE car sales essentially zero

  2050  Global net zero CO₂ emissions
        Electricity: ~90% renewables + nuclear + CCS
        Electricity volume: ~90,000 TWh (tripled from today)
        Why tripled: electrification of heat, transport, hydrogen
        Remaining residual emissions: offset by CCS and BECCS
```

### Why Electricity Must Triple

```
  TODAY                         NZE 2050
  -----                         --------
  ~30,000 TWh electricity       ~90,000 TWh electricity

  Electrification additions:
  +20,000 TWh: transport (EVs, rail)
  +20,000 TWh: buildings (heat pumps replace gas/oil)
  +10,000 TWh: industry (electric arc furnaces, electrolytic processes)
  +10,000 TWh: hydrogen production (green H₂ via electrolysis)
```

---

## The Efficiency Argument for Electrification

This is the core physics argument that makes "electrify everything" more than ideology.

```
  SPACE HEATING COMPARISON

  ┌─────────────────────────────┐   ┌─────────────────────────────┐
  │ GAS FURNACE PATH            │   │ HEAT PUMP PATH              │
  │                             │   │                             │
  │ Natural gas extracted,      │   │ Electricity from grid       │
  │ compressed, transported     │   │ (can be renewables)         │
  │         │                   │   │         │                   │
  │         v                   │   │         v                   │
  │  Combustion in furnace      │   │  Compressor (electric motor)│
  │  Chemical → thermal         │   │  moves heat from outdoors   │
  │         │                   │   │  (even at -10°C)            │
  │         v                   │   │         │                   │
  │  Heat delivered to space    │   │         v                   │
  │                             │   │  Heat delivered to space    │
  │  Efficiency: 85-95%         │   │  COP: 2.5-4.5               │
  │  (combustion efficiency)    │   │  (= 250-450% "efficiency")  │
  └─────────────────────────────┘   └─────────────────────────────┘

  Even if electricity comes from a gas plant at 50% efficiency:
  0.50 (gas plant) × 3.0 (heat pump COP) = 1.5 = 150%
  vs gas furnace at 90%
  → Heat pump path is 67% better even with gas electricity.

  Same argument applies to:
  • EVs vs ICE cars: ICE ~20% thermal efficiency; EV drivetrain ~85%
  • Induction cooking vs gas burner: ~85% vs ~40% usable heat
```

---

## Sector Breakdown — Where Final Energy Goes

```
  GLOBAL FINAL ENERGY CONSUMPTION (~400 EJ, 2022)
  =================================================

  Industry:              ~37%  (~148 EJ)
    High-temp process heat: ~25% of industry = hardest to electrify
    Steel (blast furnace), cement kiln, chemical cracking
    Electrifiable: electric arc furnaces, heat pumps (low-temp heat)

  Transport:             ~28%  (~112 EJ)
    Road:       75% of transport energy
    Aviation:   12%  — jet fuel; hard to replace
    Shipping:   10%  — bunker fuel; ammonia/LNG/methanol pilots
    Rail:        3%  — largely electrifiable

  Buildings:             ~30%  (~120 EJ)
    Space + water heating: ~75% of building energy
    Largely electrifiable via heat pumps + insulation
    Biggest near-term decarbonization opportunity

  Power sector own use:   ~5%   (~20 EJ)
    Auxiliary loads at plants

  ELECTRICITY'S GROWING SHARE:
    2000: electricity ~15% of final energy
    2022: electricity ~20% of final energy
    IEA NZE 2050: electricity ~50% of final energy
```

---

## Microsoft / Hyperscaler Context

### Data Center Energy Footprint

```
  GLOBAL DATA CENTER ELECTRICITY CONSUMPTION (2024)
  ==================================================
  Total:           ~400-500 TWh/yr (~1.5-2% of global electricity)
  Growth rate:     ~15-20%/yr (AI workloads accelerating this)

  Leading hyperscalers:
    Microsoft:    ~35-40 TWh/yr
    Amazon AWS:   ~50-60 TWh/yr
    Google:       ~25-30 TWh/yr
    Meta:         ~15-20 TWh/yr

  AI training energy:
    Large model training run: ~50-200 GWh (one training run)
    GPT-4 training estimate: ~50-100 GWh
    Equivalent to: ~5,000-10,000 US homes for one year

  Power density evolution:
    Traditional IT racks:      5-10 kW/rack
    Current AI racks (H100):   30-60 kW/rack
    Next-gen AI racks (H200+): 60-120 kW/rack
    Above ~30 kW: liquid cooling required
    Above ~100 kW: immersion cooling territory
```

### Scope 1/2/3 Emissions Framework

```
  SCOPE 1: Direct emissions (source owned/controlled by company)
    • Diesel backup generators (significant for data centers)
    • On-site gas boilers (campus heating)
    • Company vehicle fleet
    • Natural gas for campus kitchens, labs

  SCOPE 2: Indirect — purchased electricity
    • Largest carbon category for data centers
    • Two accounting methods (GHG Protocol):
      Market-based: uses contracted energy attributes (RECs, PPAs)
                    "100% renewable" claims use this method
      Location-based: uses actual grid average emissions factor
    • Gap between the two = "accounting renewable energy"

  SCOPE 3: Value chain (everything else — often 70-90% of total)
    • Hardware manufacturing (embodied carbon — servers, chips)
    • Employee commuting and business travel
    • Customers using products (Azure compute emissions)
    • Supply chain goods and services
    • Hardest to measure, hardest to reduce
```

### PPA Mechanics — How Hyperscalers Buy Renewable Energy

```
  PHYSICAL PPA:
  ┌──────────────────┐          ┌──────────────────┐
  │  Microsoft       │          │  Solar/Wind Farm  │
  │  (off-taker)     │◄────────►│  (developer)      │
  │                  │ 10-20yr  │                   │
  │  Fixed $/MWh     │ contract │  Builds, operates │
  │  Price certainty │          │  Gets revenue     │
  └──────────────────┘          │  certainty →      │
           │                    │  enables financing│
           │ Physical power      └──────────────────┘
           │ flows via grid              │
           │                            │ Connects to grid
           └────────────────────────────┘

  VIRTUAL PPA (most common for hyperscalers):
  • No physical delivery of electrons — purely financial
  • Plant sells to grid at spot price
  • Microsoft pays fixed strike price
  • Difference (positive or negative) settled financially
  • Microsoft receives RECs regardless of location
  • Advantage: Microsoft data center and plant can be in different grid regions
  • 1 REC = 1 MWh renewable energy generated

  MICROSOFT EXAMPLE (2023):
  • >50 PPAs globally, >35 GW contracted
  • Mix of solar, wind, some storage + solar
  • Mostly virtual PPAs
  • Renewable energy matching: currently annual; target 24/7 CFE by 2030
```

### 24/7 Carbon-Free Energy — The Harder Target

```
  ANNUAL MATCHING (current standard for most "100% renewable" claims):
  ┌────────────────────────────────────────────────────────────────┐
  │  Jan-Dec: buy RECs = total MWh consumed                        │
  │  Result: on paper "100% renewable"                             │
  │  Reality: at 2am you're pulling grid power (may be coal/gas)   │
  └────────────────────────────────────────────────────────────────┘

  24/7 CARBON-FREE ENERGY (Google's standard since 2020, Microsoft target):
  ┌────────────────────────────────────────────────────────────────┐
  │  Every hour: clean generation >= consumption, same grid region  │
  │  Requires: storage, diverse clean sources (solar+wind+nuclear) │
  │  Much harder operationally and contractually                   │
  │                                                                │
  │  Google 2023: ~64% 24/7 CFE                                    │
  │  Microsoft 2030 target: 100% 24/7 CFE                         │
  └────────────────────────────────────────────────────────────────┘

  The gap between annual matching and 24/7 CFE is where nuclear and
  geothermal become critical — they generate 24/7 without weather dependence.
```

---

## The Energy Transition as a Systems Engineering Problem

A framing that maps cleanly to distributed systems experience:

```
  OLD GRID (centralized thermal):     NEW GRID (distributed VRE):
  ================================     ================================
  Few hundred large generators         Millions of generators
  Dispatchable on demand               Weather-dependent output
  One-way power flow (generation→load) Bidirectional (EVs, rooftop solar)
  Mechanical inertia (spinning mass)   Software-defined synthetic inertia
  Frequency response: physics          Frequency response: control algorithms
  Vertical integration (utility owns   Competitive markets + independent
   generation, transmission, retail)    system operators (ISOs)
  30-60 year asset lifetimes           10-25 year assets (solar panels)
  Planning horizon: deterministic      Planning horizon: probabilistic

  Infrastructure analogy:
  Mainframe → Cloud computing
  • Mainframe: one big box, predictable, controlled, vendor-locked
  • Cloud: commodity servers, statistically reliable, distributed
  • Grid transition: large thermal plants → many VRE + storage

  Both require:
  • Orchestration layer (grid operator / Kubernetes)
  • Reliability under component failure (N-1 criterion / pod restarts)
  • Real-time matching of supply to demand (frequency regulation / autoscaling)
  • Forecasting and capacity planning (load forecasting / capacity planning)
```

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| Convert EJ → TWh | × 277.8 |
| Convert Mtoe → TWh | × 11.63 |
| Convert kWh → MJ | × 3.6 |
| Global primary energy? | ~600 EJ/yr |
| Global electricity generation? | ~30,000 TWh/yr |
| Electricity as % of final energy? | ~20% (heading to 50% by 2050 in NZE) |
| Cheapest new electricity (2024)? | Onshore wind / utility solar: $25-55/MWh |
| Why electrify everything? | Heat pumps: COP 2.5-4.5 vs gas furnace 85-95% |
| LCOE's key weakness? | Misses grid integration costs and value deflation |
| Carbon budget left for 1.5°C? | ~250 GtCO₂ (~6-7 years at current pace) |
| Data centers: % of global electricity? | ~1.5-2%, growing ~15-20%/yr |
| Annual matching vs 24/7 CFE? | Annual = RECs cover on paper; 24/7 = every hour clean |
| NZE 2050 electricity volume? | ~90,000 TWh (3× today) |

---

## Common Confusion Points

**"GW of capacity vs TWh of generation"**
1 GW of solar (20% CF) generates 1.75 TWh/yr. 1 GW of nuclear (90% CF) generates 7.9 TWh/yr.
Always ask: what's the capacity factor? "China added 200 GW of solar" ≠ "China added 200 GW of generation."

**"Primary energy vs final energy vs useful energy"**
Primary (~600 EJ): what you extract. Final (~400 EJ): what arrives at the door.
Useful (~200 EJ): actual energy services. ~65% of primary is waste heat.

**"Net zero vs carbon neutral vs carbon negative"**
Net zero: emissions + removals = zero (allows residual emissions with CDR offsets).
Carbon neutral: often means offset purchases without reduction (high greenwashing risk).
Carbon negative: removals exceed emissions. Microsoft's 2030 target.

**"Renewable electricity vs renewable energy"**
Electricity is ~20% of final energy. "100% renewable electricity" is not "100% renewable energy."
Decarbonizing heat, transport, and industry is the hard 80%.

**"LCOE of solar < LCOE of gas but gas still gets built"**
LCOE ignores dispatchability value. A gas plant that runs on demand is worth more to the grid
than solar at the same LCOE, because the grid needs firm power for reliability.
The relevant comparison is solar + storage vs gas, which changes the math.

**"EJ vs EWh (exawatt-hour)"**
1 EWh = 3.6 EJ. IEA typically uses EJ for primary energy, TWh for electricity.
Don't mix an IEA chart in EJ with a power sector chart in TWh without converting.
