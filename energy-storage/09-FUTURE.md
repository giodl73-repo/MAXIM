# Future Energy Storage: Long-Duration, Thermal, and 2040+ Roadmap

## The Big Picture

The critical gap in the current energy storage landscape is long-duration storage (LDES):
more than 10 hours, ideally 100+ hours, at costs that make renewable grids economically
viable without backup fossil generation. Li-ion solves 1-4 hour storage. The 10-100+
hour gap is the central unsolved problem in clean energy.

```
STORAGE DURATION GAP
=====================

DURATION (hours)   TECHNOLOGY                    STATUS (2025)
-----------------  ----------------------------  ---------------
< 1 hour           Supercapacitor, flywheel       Commercial
1-4 hours          Li-ion (LFP, NMC)              Commercial, mature
4-12 hours         Li-ion (possible), VRFB        Commercial, growing
12-24 hours        VRFB, pumped hydro (new)       Limited, expensive
                   CAES A-CAES, LAES
24-100 hours       Pumped hydro (existing)        Mostly existing assets
                   Iron-air (Form Energy)          Pilot stage
                   Hydrogen cavern                 Very limited
                   Thermal storage                 Industrial, not grid
100+ hours         Pumped hydro (existing)        Existing assets only
("Seasonal")       Hydrogen underground            Concept/pilot
                   Ammonia, LOHC                   Emerging infrastructure
                   Thermal (rock beds, salt)       Conceptual

TARGET: <$0.05/kWh for LDES to enable 100% renewable grids (ARPA-E DAYS)
CURRENT: $0.10-0.30/kWh for 10+ hr storage
GAP: 2-6x cost reduction needed
```

---

## ARPA-E DAYS Program (Duration Addition to Electricity Storage)

```
ARPA-E DAYS PROGRAM
=====================

Launched: 2020
Goal: Develop storage for 10-100+ hours at <$0.05/kWh
Rationale: grid models show that long-duration storage can reduce
  total system cost of 100% renewable grid by >10% vs. only short-duration

KEY METRICS:
  Energy capital cost: <$0.05/kWh (vs. Li-ion ~$0.10-0.15/kWh)
  Round-trip efficiency: >50% (some pathways)
  Cycle life: >5,000 cycles or >10 years calendar
  No critical mineral constraints (no Li, Co, Ni, Ir)

FUNDED TECHNOLOGY CATEGORIES:
  Thermal: electric thermal storage (resistance heating + industrial heat)
  Electrochemical: iron-air, new flow chemistries, liquid metal batteries
  Mechanical: gravity (Gravitricity, Energy Vault), pumped hydro variants
  Chemical: metal-hydrogen (nickel-iron), CO2 capture/release cycles
  Hybrid: multiple approaches combined

NOTABLE DAYS RECIPIENTS:
  Malta Inc. (Alphabet X project): molten salt + antifreeze thermal storage
  Form Energy: iron-air battery
  CMBlu Energy: organic flow battery
  Energy Dome: CO2 battery (liquefied CO2)
  Noon Energy: CO/CO2 electrochemical cycle
  AltairNano: grid-scale iron-vanadium flow
  Ambri: liquid metal battery (calcium/antimony, ~700 C operating temperature)
```

---

## Thermal Energy Storage: The Underrated Technology

### Molten Salt (Existing CSP Technology)

```
MOLTEN SALT THERMAL STORAGE (CSP)
===================================

Standard for Concentrated Solar Power plants (not grid battery):
  Salt mixture: NaNO3/KNO3 "solar salt" (60/40 by weight)
  Liquid range: 220-565 C (solidifies below 220 C -- freeze risk)
  Heat capacity: ~1.5 kJ/kg/K
  Density: ~1,900 kg/m^3
  Energy density: ~100 kWh/m^3 (temperature swing 220-565 C = 345 K)

  Cost: ~$25-40/kWh thermal (much cheaper than batteries)
    BUT: thermal-to-electricity conversion: 35-45% (Rankine turbine)
    Effective electrical storage cost: $25/kWh / 0.40 = $62.5/kWh electrical
    Adding electric heater for charging: another ~10-20% loss
    Total RTE: 30-40% (similar to hydrogen economically)

ELECTRIC THERMAL ENERGY STORAGE (ETES / FIREBEE concept):
  Charge: resistance electric heaters -> heat rocks/firebrick to 1500+ C
  Store: insulated hot rock bed (cheap, any geographic location)
  Discharge: pump air through hot rock -> air heats -> drives turbine or industrial use

  RESISTANCE HEATING ADVANTAGE:
    Nearly 100% efficient (all electricity -> heat)
    No moving parts (very cheap)
  DISADVANTAGE:
    Thermodynamic degradation: Carnot efficiency limits heat-to-electricity
    At T_hot = 1200 C = 1473 K, T_cold = 300 K:
    Carnot efficiency = 1 - T_cold/T_hot = 1 - 300/1473 = 80% (theoretical)
    Practical Brayton cycle at 1200 C: ~55-65% efficiency
    Net RTE: ~50-65% (charging nearly perfect, discharge limited by Carnot)

FORM ENERGY vs. ETES vs. MOLTEN SALT COMPARISON:
  Technology       Cost $/kWh   RTE    Geography   Duration
  Iron-air         $20 target   45%    Any          100+ hr
  ETES (rock)      $10-30       50-65% Any          10-100 hr
  Molten salt CSP  $25-40 thermal 30-40% Any        10-14 hr
  VRFB             $150-300     65-80% Any          4-24 hr
  Pumped hydro     $50-200      70-85% Limited      8-100+ hr
```

### Ice Storage and Demand-Side TES

```
ICE STORAGE (COMMERCIAL BUILDINGS)
=====================================

CONCEPT:
  Run chiller overnight (off-peak electricity, ~$0.04-0.08/kWh)
  Make ice (store thermal energy)
  Melt ice to cool building during day (avoid running chiller at peak electricity cost)

ECONOMICS:
  Chiller COP (coefficient of performance): ~3-4 (3-4 kWh cooling per 1 kWh electricity)
  At 5 ton chiller with 8 hr ice storage: ~40 ton-hr of cooling storage
  1 ton = 12,000 BTU/hr = 3.5 kW cooling
  Off-peak: $0.05/kWh; On-peak: $0.20/kWh
  Savings: avoid on-peak chiller operation for 4-6 hours/day
  Payback: 3-7 years depending on rate structure

  CALMAC, FAFCO: commercial ice storage systems
  1,000s of installations in commercial buildings (hospitals, offices, schools)
  This is one of the most cost-effective TES technologies -- proven, mature

DISTRICT COOLING:
  Central chilled water plant with large thermal storage tanks
  Singapore: district cooling stores cold water (7 C) in large tanks
  Chicago DES: large chilled water tanks in downtown district cooling
  Cost: $10-30/kWh thermal -- very competitive
```

---

## Iron-Air at Scale (Form Energy)

```
FORM ENERGY DEPLOYMENT STATUS (2026)
======================================

Company history:
  Founded 2017, Cambridge MA
  Founders: from lithium-ion community + deep tech
  Board: Bill Gates, others via Breakthrough Energy Ventures
  Total funding: ~$600M+ (as of 2024)

Technology basis:
  Iron-air chemistry (see 04-FLOW-BATTERIES.md for chemistry detail)
  Multi-day duration: 100+ hours
  System: array of cells, each with Fe anode + air cathode
  Scale-up: parallel cells -> MW systems

Commercial progress:
  2023: First pilot customer announced (Georgia Power, 3 MW / 150 MWh pilot)
  2024: Weirton, WV factory begins production
  2025-2026: First commercial installations scaling
  2030 target: <$20/kWh at scale, GWh-scale production

ECONOMIC THESIS:
  100-hr storage at $20/kWh: enables storage of 4-day renewable supply
  "Peaker replacement": replace gas peaker plants that run <500 hr/year
  Gas peaker LCOS: $200-400/MWh
  Iron-air at $20/kWh + 45% RTE: LCOS ~$80-120/MWh
  -> Iron-air cheaper than gas peakers if claims hold

RISKS:
  RTE: 45% is low -- sensitivity to electricity prices
  Manufacturing scale-up: factory still proving out yield, throughput
  Performance durability: need 20-year life demonstration (not yet available)
  Grid integration: multi-day operation requires sophisticated dispatch
```

---

## Compressed CO2 Energy Storage

```
CO2 BATTERY (Energy Dome)
===========================

CONCEPT (Energy Dome, Italy):
  Store CO2 at atmospheric pressure (gas, not supercritical)
  Compress CO2 and liquefy (heat removed to atmosphere or TES)
  Store liquid CO2 in tank (not pressure vessel -- at ambient pressure near critical point)
  To discharge: evaporate CO2, expand through turbine

  KEY: CO2 critical point: 31 C, 73.8 bar
    Just above critical point: CO2 can be stored as dense supercritical fluid
    At 40 C, 80 bar: very dense CO2 (like liquid), stores 2x energy vs. compressed gas
    Or: just below critical point at 15-20 C: liquid CO2 at 50-60 bar in sealed tank

ADVANTAGES:
  CO2 is abundant, non-toxic, cheap
  Closed loop: same CO2 recycled (not consumed)
  Geographic independence (no geology needed)
  Scalable: add more CO2 storage tanks

EFFICIENCY:
  Charge (compression + liquefaction): 70-75% efficient
  Discharge (expansion through turbine): 75-80% efficient
  Net RTE: ~75% (claimed in design) -- significantly better than iron-air
  First plant (Sardinia, Italy, 2022): 4 MW / 24 MWh demonstration
  Multiple projects under development

COST TARGET:
  $50-100/kWh (claimed) for 10+ hour storage
  More expensive than iron-air but better RTE
  Comparison: LAES also 50-60% RTE, similar cost range
```

---

## Grid Storage Technology Roadmap 2025-2040+

```
GRID STORAGE ROADMAP
=====================

PHASE 1 (2025-2030):
  DOMINANT: Li-ion LFP for 1-4 hour grid storage
    Cost declining: $80-100/kWh (2025) -> $60-70/kWh (2030)
    Massive scale-up: 100s GWh new deployment/year globally
  EMERGING: VRFB, LAES for 8-24 hour storage
    Cost declining as scale increases
  PILOT: Iron-air (Form Energy), A-CAES (Hydrostor)
  RESEARCH: ETES (electric rock), advanced organic flow, liquid metal

PHASE 2 (2030-2035):
  SOLID-STATE BATTERIES: premium EV cells starting to appear
    Grid storage: solid-state too expensive unless radical cost reduction
  SODIUM-ION: commercial-scale for grid; cost advantage over LFP emerging
  LONG-DURATION (10-24 hr): VRFB + flow batteries mainstream at this duration
  IRON-AIR: if Form Energy scaling successful, $20-30/kWh possible
  ETES: electric thermal storage validated at GW scale
  HYDROGEN: green H2 seasonal storage pilots -> commercial

PHASE 3 (2035-2040):
  LDES MAINSTREAM: cost target $0.05/kWh for 100-hr storage approached
  100% RENEWABLE FEASIBILITY: with LDES + solar + wind + some pumped hydro
  SOLID-STATE: becoming mainstream EV and commercial BESS if manufacturing scales
  SEASONAL STORAGE: hydrogen caverns and large ETES proven at scale

PHASE 4 (2040+):
  LI-S: possible if shuttle/cycle life solved (aviation mainstream)
  ADVANCED FLOW: quinone or other organic flow at grid scale
  INTEGRATED: heat, power, hydrogen all co-optimized in industrial parks
  NUCLEAR + STORAGE: SMR + H2 or molten salt thermal at industrial scale

CRITICAL UNCERTAINTIES:
  Iron-air scale-up (Form Energy's manufacturing execution)
  ETES heat-to-electricity efficiency in practice (Carnot limits are real)
  Hydrogen underground storage economics (H2 bacteria, leakage)
  Solid-state battery manufacturing (interface problem still open as of 2026)
```

---

## Solid-State Battery Timeline (Conservative Assessment)

```
SOLID-STATE BATTERY REALISM CHECK
====================================

WHY IT MATTERS: solid-state could unlock Li metal anode -> 500+ Wh/kg cells
  This would increase EV range from ~500 km to ~800-1000 km per charge
  Or: same range, much lighter/smaller battery -> lower vehicle cost

TIMELINE HISTORY:
  2013: "Solid-state batteries in 5 years" -- Toyota
  2016: "Solid-state batteries in 5 years" -- multiple OEMs
  2018: "Solid-state batteries by 2025" -- Toyota, VW/QuantumScape
  2020: "Solid-state in production by 2025-2027" -- Samsung, Solid Power, QuantumScape
  2022: QuantumScape shows 1000+ cycle single-layer cell (no anode, LLZO)
  2023: Multiple parties delay targets 2-4 years
  2025: Toyota targeting 2027-2028 production start (limited volume)
  2026: QuantumScape targeting automotive qualification ~2027-2028

REALISTIC ASSESSMENT:
  "Limited volume premium EV": 2028-2030 (probably)
  "Volume production EV": 2030-2033 (more uncertain)
  "Grid storage cost-competitive": 2035+ (needs massive manufacturing scale + cost reduction)

KEY REMAINING CHALLENGES:
  Dendrite suppression under pressure: requires 5-10 MPa stack pressure -- engineering hard
  Interface stability after 1000+ automotive cycles: not yet proven at full cell level
  Manufacturing thin electrolyte sheets at scale: no production line exists
  Sulfide moisture: manufacturing requires ultra-dry (Ar glovebox) environments at scale

GRID STORAGE SPECIFIC:
  Grid storage requires: $80-100/kWh (current LFP target)
  Solid-state initial cells: $300-500/kWh (premium EV pricing)
  Grid storage adoption: needs 5-10 yr after EV production starts + cost learning
  Realistic grid solid-state: 2038-2045 if EV timeline holds
```

---

## Decision Cheat Sheet

| Future storage goal | Technology path |
|--------------------|----------------|
| 1-4 hour grid (2025-2030) | Li-ion LFP (current) |
| 8-24 hour grid (2025-2030) | VRFB or LAES (emerging commercial) |
| 100+ hour grid (2025-2030) | Iron-air if Form Energy delivers; pumped hydro (new) |
| Seasonal storage | Hydrogen cavern or ETES at scale |
| Ultra-high energy density EV (2030+) | Solid-state Li metal (if timeline holds) |
| Grid with very cheap electricity | ETES (electric rock thermal) -- resistance heating cheap |
| Island grid (100% renewable) | Mix: Li-ion + pumped hydro + H2 seasonal |
| Steel/industry heat + storage | SOEC + H2 or ETES with industrial heat integration |

---

## Common Confusion Points

**"Long-duration storage is just bigger batteries."** No. Li-ion cost scales linearly
with duration (more cells = more cost). LDES technologies (iron-air, ETES, hydrogen)
have low incremental cost per additional hour (more tank, not more stack). This is why
completely different technologies are needed for 10+ hours, not just more Li-ion.

**"Iron-air will be proven by 2026."** Form Energy has pilots deploying, but "proven"
requires demonstrated multi-year performance under real grid cycling conditions.
Commercial-scale production learning curve validation. The technology is real;
the scale-up execution is the unknown.

**"Thermal storage is not real electricity storage."** For electric grids, thermal
storage can function as effective electricity storage: store excess electricity as heat,
discharge as heat (industrial use) or re-convert to electricity (lower efficiency).
Ice storage in buildings is already widely deployed and economically competitive. ETES
for grid electricity is newer but uses the same principle.

**"The ARPA-E DAYS $0.05/kWh target is impossible."** Iron-air claims <$20/kWh.
ETES (rock + resistance heating) could plausibly reach $10-20/kWh. These are not
impossible; they require manufacturing scale-up and performance validation. The targets
are aspirational but grounded in thermodynamic and material cost analysis.
