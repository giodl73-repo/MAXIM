---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "05-PUMPED-HYDRO.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:energy-storage:pumped-hydro
kind: guide
module: energy-storage
section: energy-storage
title: Pumped Hydro: Physics, Sites, Efficiency, and Global Dominance
status: source-custody
source_custody: partial
current_path: energy-storage/05-PUMPED-HYDRO.md
canonical_path: energy-storage/05-PUMPED-HYDRO.md
backsource_ids: [proof-backfill:energy-storage:05-pumped-hydro, git-history:energy-storage:05-pumped-hydro]
concepts: [pumped, hydro]
root_concepts: [pumped, hydro]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Pumped Hydro: Physics, Sites, Efficiency, and Global Dominance

## The Big Picture

Pumped hydroelectric storage is the oldest, most proven, and by far the most deployed
form of grid-scale energy storage. Recent global surveys still place it at the large
majority of installed grid-storage energy capacity, though exact shares vary by source
and by whether power or energy capacity is counted. Its advantage is not novelty; it is
site-specific, long-lived civil infrastructure at GW/GWh scale.

```
PUMPED HYDRO GLOBAL CONTEXT
=============================

GLOBAL STORAGE INSTALLED (approximate, source-dependent):
  Pumped hydro:       dominant by installed energy capacity
  Li-ion BESS:        fastest-growing new-build category
  Flow/CAES/thermal:  smaller installed base, targeted niches

LARGEST PUMPED HYDRO PLANTS:
  Bath County (VA, USA): 3,003 MW / 24,000 MWh (30-year payback, paid off)
  Tianhuangping (China): 1,836 MW
  Goldisthal (Germany):  1,060 MW
  Dinorwig (Wales, UK):  1,728 MW -- zero-to-full power in 12 seconds
  Okutataragi (Japan):   1,932 MW

WHY PUMPED HYDRO DOMINATES:
  50+ year asset life (civil structure outlasts most technology)
  Round-trip efficiency: 70-85% (competitive with many alternatives)
  Proven at GW scale; no technology risk
  Multiple services: energy shifting + frequency regulation + black start capability
  No degradation over time (water doesn't wear out)
```

---

## Physics

### Basic Energy Equation

```
PUMPED HYDRO ENERGY CALCULATION
=================================

  E = m * g * h * eta

where:
  E   = energy stored (Joules)
  m   = mass of water (kg)
  g   = gravitational acceleration (9.81 m/s^2)
  h   = head (effective height difference between upper and lower reservoir) (m)
  eta = round-trip efficiency (fraction)

Converting to kWh:
  1 kWh = 3.6e6 J
  E [kWh] = rho * V * g * h * eta / 3.6e6
           = 1000 kg/m^3 * V [m^3] * 9.81 * h * eta / 3.6e6
           = 2.725 * V[m^3] * h[m] * eta  [Wh]
           = 0.002725 * V[m^3] * h[m] * eta  [kWh]

PRACTICAL EXAMPLES:
  Bath County (3000 MW, 6+ hours):
    Head h = 385 m; Volume pumped ~ 10 million m^3
    E = 0.002725 * 10^7 * 385 * 0.78 ~ 8.2 million kWh = 8.2 GWh

  Small pumped hydro (100 MW, 4 hours = 400 MWh):
    At h = 400 m: V = 400,000 kWh / (0.002725 * 400 * 0.75) = 490,000 m^3
    That's 490,000 metric tons of water -- a significant reservoir

HEAD MATTERS MOST:
  Doubling head doubles energy for same water volume
  High head sites (300-900 m): preferred (less water, smaller reservoirs)
  Low head sites (<100 m): require enormous water volumes (less common)
  Most sites: 150-600 m head

POWER EQUATION:
  P = rho * g * Q * h * eta_turbine
    = 1000 * 9.81 * Q [m^3/s] * h * 0.90 (turbine efficiency)
  At h=400m, Q=250 m^3/s: P = 1000 * 9.81 * 250 * 400 * 0.9 = 882 MW
```

### Efficiency Breakdown

```
ROUND-TRIP EFFICIENCY DECOMPOSITION
=====================================

PUMPING (electricity -> potential energy):
  Electric motor: 96-98% efficient
  Pump/turbine unit: 90-93% (hydraulic efficiency)
  Penstock losses: 1-2% (pipe friction)
  Evaporation losses: 0.1-1% (depends on reservoir area and climate)
  Total pumping efficiency: ~86-90%

GENERATION (potential energy -> electricity):
  Turbine: 90-93% hydraulic efficiency
  Generator: 97-99% electrical efficiency
  Transformer + line losses: 1-2%
  Total generation efficiency: ~88-92%

ROUND-TRIP:
  eta_RTE = eta_pump * eta_generate
  Typical: 0.88 * 0.90 = 0.79 (79%)
  Best modern variable-speed units: 82-85% RTE
  Older fixed-speed units: 70-76% RTE

VARIABLE-SPEED OPERATION:
  Fixed-speed: motor/generator at fixed RPM (synchronized to grid 50/60 Hz)
    Can only operate at or near rated output (poor part-load efficiency)
  Variable-speed: asynchronous machine (doubly-fed induction or full converter)
    Can pump at variable power (partial load) with maintained efficiency
    Key for absorbing variable renewable energy (pump when solar excess, variable amount)
    Cost: +20-30% higher capital for variable-speed units
    ARIES (Arizona), Nant de Drance (Switzerland): recent variable-speed installs
```

---

## Siting Requirements

```
PUMPED HYDRO SITE REQUIREMENTS
================================

TOPOGRAPHIC:
  Two reservoir locations with 150-900 m elevation difference
  Within 1-3 km horizontal distance preferred (shorter tunnels)
  Natural topography: mountain lakes, valleys, gorges preferred
  Minimum reservoir size: determined by energy capacity target

  RULE OF THUMB:
    1 GWh storage at 300m head: ~1.2 million m^3 reservoir (~480 Olympic pools)
    1 GWh storage at 600m head: ~0.6 million m^3 (~240 Olympic pools)

WATER:
  Water rights (legally complicated in western US, many jurisdictions)
  Enough water to fill reservoirs initially (one-time fill + makeup for evaporation)
  No consumptive use -- water cycles between reservoirs continuously
  Evaporation: 0.5-2 m/year from reservoir surface (depends on climate)
  Closed-loop (no river intake): preferred for environmental permitting

GEOLOGICAL:
  Stable rock mass (granite, gneiss preferred; no karstic limestone)
  Underground powerhouse: cavern in competent rock
  Penstock: tunneling required through mountain
  No active faults in zone (seismic stability)

ENVIRONMENTAL / PERMITTING:
  FERC (US): typically 5-15 years permitting for new hydro
  EU: Water Framework Directive, Habitats Directive
  First Nations / Indigenous rights (critical path in many jurisdictions)
  Cumulative impact on existing water bodies
  Fish passage, sediment transport (if on river)
  Visual impact (reservoir in scenic area)

COST:
  $500-3,000/kW (wide range depending on head, site complexity, tunneling)
  $/kWh (for 8+ hour storage): $50-200/kWh (much cheaper than Li-ion for long duration)
  Civil works: 60-70% of cost; electromechanical: 20-25%; other: 10-15%
```

---

## Conventional vs. Underground Pumped Hydro

```
CONVENTIONAL vs. UNDERGROUND PUMPED HYDRO
==========================================

CONVENTIONAL:
  Upper and lower reservoirs on surface
  Requires specific topography (two hills/valleys at different elevations)
  Limited to certain geographies (Alps, Rockies, Appalachians, Norwegian fjords)
  Large surface footprint (visible reservoirs)
  Environmental impact: habitat change, hydrology change

  Estimated global potential:
    World Bank study: 617,000 sites with >100 GWh capacity each
    Most potential: China (Asia-Pacific), Africa, Americas
    Total: >23 million GWh potential (vs. ~9,500 GWh deployed)
    Not resource constrained; constrained by permitting, capital, time

UNDERGROUND PUMPED HYDRO (UPH):
  Upper reservoir: surface (natural lake, abandoned quarry, or surface reservoir)
  Lower reservoir: underground cavern (excavated in rock) or abandoned mine
  No lower surface reservoir -- eliminates major topographic constraint

  Examples:
    Mount Hope (NJ, USA, proposed): iron mine cavern, 2,000 MW
    Kidston (Queensland, AUS, under construction): gold mine, 250 MW
    STENSEA (Germany, concept): offshore underwater sphere on seabed

  Geography independence: can be built where there is elevation to bedrock
    (not just in mountains) -- much wider applicable area
  Cost: higher excavation cost but no surface reservoir land acquisition
  Status: limited examples; Kidston (former gold mine) is best near-term example

OCEAN / SEAWATER PUMPED HYDRO:
  Sea as lower reservoir, upper reservoir onshore
  Okinawa Yanbaru (Japan): 30 MW, seawater, operational since 1999
  Canary Islands (La Palma): proposed 200 MW seawater system
  Challenge: salt corrosion on turbines, membranes; easier to seal vs. freshwater
  Advantage: eliminates water scarcity constraint for island/coastal sites
```

---

## Pumped Hydro vs. Other Technologies: Head-to-Head

```
PUMPED HYDRO vs. ALTERNATIVES (for 8+ hour storage)
======================================================

Metric           Pumped Hydro   VRFB Flow     Li-ion BESS   Hydrogen
---------------  -------------  ------------  -------------  ---------
Round-trip eff.  70-85%         65-80%        90-95%         25-40%
Installed cost   $500-3000/kW   $400-800/kW   $1000-2000/kW  $800-1500/kW
                 $50-200/kWh    $150-400/kWh  $200-400/kWh   $50-150/kWh
                 (8+ hr)        (8+ hr)       (4 hr cap)     (seasonal)
Life (yrs)       50-100         25+           10-20          20-30
Calendar aging   None (water)   Low           Moderate       Low
Geography dep.   HIGH           None          None           None
Time to build    10-20 years    2-3 years     1-2 years      3-5 years
Best for         GW scale       8-24 hr       1-4 hr         Seasonal/H2
                 long term      regional      grid edge      economy
```

---

## Fast Response: Pumped Hydro for Ancillary Services

```
PUMPED HYDRO FAST RESPONSE CAPABILITY
=======================================

Dinorwig (Wales) -- "Electric Mountain":
  1,728 MW, from standby to full power in 12 seconds
  Mechanism: spinning in air (runner spinning in dewatered draft tube)
    -> No acceleration time needed; just open gate and water enters
  Used for: frequency regulation, spinning reserve, black start (grid restoration)

Black start capability:
  Pumped hydro can start WITHOUT grid power (motor drives itself)
  Used to restart grid after major blackout (start at pumped hydro,
    energize transmission lines, bring thermal plants back up synchronously)
  Critical infrastructure; most pumped hydro sites are designated black start units

Response time:
  From standby (spinning in air): 10-30 seconds
  From cold stop: 2-5 minutes (mechanical startup)
  From pump to generate: 3-5 minutes (reverse pump direction)
  Li-ion BESS: <100 ms (much faster)
  Li-ion better for sub-second frequency response; pumped hydro for sustained MW·hr
```

---

## Decision Cheat Sheet

| If you need to diagnose... | Start With | Key Caveat |
|---|---|---|
| Whether pumped hydro fits a storage need | Check required MW, MWh, duration, cycle frequency, ramp rate, black-start need, and transmission location. | Pumped hydro is excellent for large/long assets, but it is not a rapid modular deployment tool. |
| Whether a site is feasible | Examine head height, reservoir volume, geology, water rights, environmental impact, land ownership, and grid interconnection. | The limiting constraint is usually site/permitting, not turbine physics. |
| Whether it beats batteries | Compare duration, lifetime, degradation, round-trip efficiency, construction time, financing risk, and market revenue. | Batteries often win short-duration speed and modularity; pumped hydro can win long life and large energy volume. |
| Whether it can provide black start | Verify auxiliary power, start sequence, cranking path, reactive support, governor behavior, and load-pickup plan. | A plant may be black-start capable only if the restoration path and grid conditions are engineered. |
| Whether it provides frequency regulation | Check fixed-speed vs variable-speed machines, operating point, reserve headroom, governor controls, and market rules. | Li-ion can respond faster; pumped hydro brings rotating mass and large sustained capability. |
| Whether it works for an island or isolated grid | Map terrain, reservoirs, rainfall/evaporation, seismic risk, land constraints, and backup generation. | Mountainous geography helps, but island permitting, water, and environmental constraints can dominate. |
| Whether it solves seasonal storage | Compare reservoir size, inflow, evaporation, environmental limits, multi-week energy need, and competing water uses. | It is proven at GWh scale, but "seasonal" requires enormous reservoirs and favorable geography. |

---

## Cross-References

- `08-GRID-ECONOMICS.md` compares pumped hydro economics with battery and long-duration storage.
- `06-COMPRESSED-AIR.md` gives another geography-dependent bulk-storage technology.
- `../hydrology/00-OVERVIEW.md` supplies the water-system context behind reservoirs and siting.

## Common Confusion Points

**"Pumped hydro is old technology being replaced by batteries."** Li-ion batteries
are replacing pumped hydro for NEW SHORT-DURATION storage projects (1-4 hour).
For long-duration storage (8+ hours), pumped hydro is still the most cost-effective option
and accounts for 96% of global grid storage. The two technologies serve different
duration niches. Li-ion does not economically replace a 24-hour pumped hydro project.

**"Water is consumed (burned) in pumped hydro."** Water is not consumed -- it cycles
between upper and lower reservoirs indefinitely. Net water loss is only from evaporation
(0.5-2 m/year from reservoir surface) and any seepage. Pumped hydro is non-consumptive
unlike thermal power plants.

**"Building more pumped hydro is easy."** The physics is simple; the project delivery is
not. FERC licensing in the US takes 5-15 years. Environmental review, First Nations
consultation, water rights acquisition, and geological risk can each be decade-scale
challenges. The longest lead time in energy infrastructure.

**"Variable-speed pump-turbine units are just a minor improvement."** For renewable
integration, variable speed is transformative -- it allows the pump to absorb variable
amounts of wind/solar power (from 30% to 100% of rated capacity) rather than only
operating at full load. Fixed-speed units are on/off; variable-speed units are a
continuously adjustable load -- exactly what's needed for renewable balancing.
