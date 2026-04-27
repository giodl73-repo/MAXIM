# Solar Photovoltaics

## The Big Picture

Solar PV went from boutique technology to cheapest electricity source in history in ~15 years.
The learning rate (cost per unit drops ~20% each time cumulative deployment doubles) has been
faster than any prior energy technology. Understanding the full stack — from physics to grid —
is what separates "solar is cheap" from knowing why and what it means.

```
SOLAR PV STACK — From Photon to Grid

  SUN
   |
   |  Photons (AM1.5G spectrum at ground level)
   v
+------------------+
|  PV CELL         |
|  Si monocrystal  |
|  or thin-film    |
+------------------+
  Semiconductor p-n junction; converts photons → electrons
  Cell efficiency: 20-26% (commercial monocrystalline)
  Perovskite/tandem: 26-33%
   |
   |  Series/parallel cell strings
   v
+------------------+
|  PV MODULE       |
|  (panel)         |
+------------------+
  60-72+ cells encapsulated; module efficiency ~19-22%
  Losses vs cell: reflection, cell gaps, series resistance
   |
   |  String wiring (600-1500V DC)
   v
+------------------+
|  DC COMBINER     |
|  (utility scale) |
+------------------+
  Aggregates multiple module strings; string fusing, monitoring
   |
   v
+------------------+
|  INVERTER        |
|  (string/central)|
+------------------+
  DC → AC conversion; MPPT tracking; grid sync; efficiency ~97-99%
   |
   |  AC output (LV or MV)
   v
+------------------+
|  TRANSFORMER     |
+------------------+
  Step up to distribution voltage (typically 34.5 kV or 138 kV)
   |
   v
  GRID
```

---

## The Photovoltaic Effect — Physics

The p-n junction is the core. For an MIT TCS grad: this is carrier physics in a semiconductor,
not exotic. The engineering challenge is maximizing photon absorption and minimizing recombination.

```
  P-N JUNCTION IN A SOLAR CELL

  ┌─────────────────────────────────────────────────────┐
  │                p-type silicon (boron-doped)         │
  │  Majority carriers: holes (+)                       │
  │                                                     │
  ├──────────────── DEPLETION REGION ───────────────────┤
  │  Built-in electric field ←────────────────          │
  │                                                     │
  │                n-type silicon (phosphorus-doped)    │
  │  Majority carriers: electrons (-)                   │
  └─────────────────────────────────────────────────────┘

  WHEN PHOTON HITS:
  1. Photon absorbed → electron-hole pair generated
     (requires photon energy > bandgap: 1.12 eV for Si)
  2. Minority carrier (electron in p-type, hole in n-type)
     diffuses to depletion region
  3. Built-in field sweeps electron → n-side, hole → p-side
  4. Charge separation → voltage across junction
  5. Connect external circuit → current flows

  ENERGY LOSSES (why single-junction efficiency ~33% limit):
  • Photons with E < bandgap: not absorbed (transmitted)
  • Photons with E >> bandgap: excess energy → heat (thermalization)
  • Recombination (radiative + Auger + Shockley-Read-Hall)
  • Series resistance (metal contacts)
  • Reflection from front surface

  Shockley-Queisser limit: theoretical max ~33% for single-junction Si
  Record lab cells (multijunction, concentrators): ~47%
  Commercial production: 20-26% (mono Si), lower for others
```

### I-V Curve and Key Parameters

```
  CURRENT-VOLTAGE (I-V) CURVE

  I (current)
  │
  Isc ─────────────────────────────────────┐
  │                                        │  ← Maximum Power Point (MPP)
  │                                       /│
  │                                      / │
  │                               (Imp, Vmp) ← operate here
  │                                    /   │
  │                                   /    │
  │                                  /     │
  │                                 /      │
  0 ──────────────────────────────/────────── V (voltage)
                                            Voc

  Key parameters:
  Isc:  Short circuit current (max current, V=0)
        ∝ Irradiance (doubles if irradiance doubles)
  Voc:  Open circuit voltage (max voltage, I=0)
        Weakly dependent on irradiance, decreases with temperature
  Imp, Vmp: Current and voltage at maximum power point
  Pmax: Isc × Voc × FF  (not just Isc × Voc!)

  FILL FACTOR (FF):
       Imp × Vmp       Actual max power
  FF = ──────────── = ──────────────────────
       Isc × Voc       Theoretical max rectangle

  Good silicon cells: FF = 0.78-0.83
  Perovskite cells:   FF = 0.80-0.88
  FF < 0.7: poor cell quality (shunts, series resistance)

  Cell efficiency: η = Pmax / (G × Area)
    where G = irradiance (W/m²), standard = 1000 W/m² at 25°C
```

---

## Cell Technology Landscape

```
  TECHNOLOGY FAMILY TREE

  Silicon:
  ├── Monocrystalline (mono-Si)
  │   ├── Standard BSF (back surface field) — legacy, declining
  │   ├── PERC (Passivated Emitter Rear Contact) — market dominant 2020-2024
  │   ├── TOPCon (Tunnel Oxide Passivated Contact) — 2024+ dominant
  │   └── HJT (Heterojunction Technology) — highest efficiency, higher cost
  │
  ├── Polycrystalline (poly-Si / mc-Si) — declining, cheaper historically
  │
  └── Silicon-based tandem
      └── Perovskite/Si tandem — near commercial, 30-33%

  Thin-Film:
  ├── CdTe (cadmium telluride) — First Solar, utility-scale dominant TF
  ├── CIGS (copper indium gallium selenide) — flexible, niche
  └── a-Si (amorphous silicon) — tiny cells, calculators, legacy

  Emerging:
  ├── Perovskite single-junction — ~26% lab, stability challenge
  ├── OPV (organic PV) — flexible, low cost, low efficiency
  └── III-V (GaAs/InGaP) — space cells, concentrator systems
```

### Technology Comparison Table

| Technology | Efficiency (commercial) | Key advantage | Key challenge | Market share |
|------------|------------------------|---------------|---------------|-------------|
| PERC mono-Si | 21-23% | Mature, cost-optimized | Being displaced by TOPCon | ~50% (falling) |
| TOPCon mono-Si | 23-25% | Higher efficiency, bifacial | Higher mfg cost (but falling) | ~40% (growing) |
| HJT | 24-26% | Best temperature coefficient, bifacial | Highest production cost | ~5% |
| CdTe (First Solar) | 19-22% | Low temp coefficient, thin-film | Cd toxicity/disposal; Te scarcity | ~5% |
| CIGS | 17-21% | Flexible substrates | Complexity, cost | <1% |
| Perovskite/Si tandem | 28-33% (lab, ~28% commercial pilot) | Exceeds Si efficiency limit | Stability (UV, moisture), Pb content | <1% (2024) |

### PERC vs TOPCon vs HJT — The Mono-Si Succession

```
  PERC (2015-2024 dominant):
  • Dielectric passivation layer on rear
  • Local contacts through laser-fired openings
  • ~21-23% efficiency ceiling due to recombination at rear contact
  • Fully depreciated fabs can produce at ~$0.12/W (Chinese)

  TOPCon (2024-2030 likely dominant):
  • Thin tunnel oxide + heavily doped poly-Si layer on rear
  • Near-perfect surface passivation
  • 23-25% efficiency, bifacial gain of 10-20%
  • Compatible with existing PERC lines (incremental upgrade)
  • Chinese module prices ~$0.10-0.12/W in 2024

  HJT (Heterojunction):
  • Amorphous silicon (a-Si) layers on both sides of crystalline Si
  • Best temperature coefficient: -0.26%/°C vs -0.35%/°C for PERC
  •  Matters in hot climates — HJT loses less performance at 70°C
  • Can be made symmetrically (bifacial easily)
  • Manufacturing challenge: low-temperature process required
    (a-Si layer deposited at <200°C; no diffusion furnaces)
  • Cost premium ~15-20% over TOPCon
```

---

## Module Architecture

### From Cell to Module: Loss Budget

```
  CELL EFFICIENCY:    ~23% (TOPCon, measured at STC)
          |
          |  Losses in module assembly:
          |  • Interconnect ribbon resistance:     -0.5%
          |  • Cell spacing (inactive area):       -0.8%
          |  • Front glass reflection:             -0.5%
          |  • Encapsulant absorption:             -0.3%
          |  • Cell mismatch (string effects):     -0.3%
          v
  MODULE EFFICIENCY:  ~20-21% (STC)
          |
          |  Real-world losses (vs STC):
          |  • Temperature (operating at 55-70°C): -3 to -5%
          |  • Low-light performance (morning/evening): -1%
          |  • Soiling (dust, bird droppings):     -2 to -5%
          |  • Shading:                            -variable
          |  • DC wiring losses:                   -1 to -2%
          v
  REAL-WORLD DC EFFICIENCY: ~16-18%
```

### Standard Test Conditions (STC) vs Real World

```
  STC (how modules are rated):          REAL WORLD:
    Irradiance: 1000 W/m²                 Variable (0-1100 W/m² at peak)
    Temperature: 25°C cell temp           Cell temp: 50-80°C in summer
    Air mass: AM1.5                       AM changes through day

  Performance Ratio (PR):
    PR = (Actual energy / Theoretical energy at STC irradiance) × 100%
    Good systems: PR = 75-85%
    PR < 70%: investigate losses (soiling, inverter issues, shading)
```

### Bifacial Modules

```
  Standard module: captures front irradiance only
  Bifacial module: transparent rear (glass-glass) captures reflected light from ground

  Bifacial gain (additional energy from rear):
    Light-colored gravel (albedo ~0.4): +8-12% energy
    Green grass (albedo ~0.25):         +5-8%
    Concrete (albedo ~0.3):             +6-10%
    Dark soil (albedo ~0.15):           +3-5%

  Bifacial gain is why TOPCon adoption is accelerating —
  symmetric structure makes bifacial manufacturing straightforward.
```

---

## System Architecture — Inverter Topologies

```
  STRING INVERTER:
  Module1──────┐
  Module2──────┤ (string, typically 8-20 modules)
  Module3──────┘──►[String Inverter DC→AC]──► AC grid

  Module4──────┐
  Module5──────┤ (another string)
  Module6──────┘──►[String Inverter DC→AC]──► AC grid

  Pros:  Lower cost per W; simple; easy to replace
  Cons:  String mismatch (one shaded module degrades whole string)
         No per-module optimization
  Use:   Residential and small commercial; most utility-scale today

  ─────────────────────────────────────────────────────────

  CENTRAL INVERTER (utility-scale traditional):
  Many strings ──► DC combiner ──► [1-5 MW central inverter] ──► MV transformer

  Pros:  Very low cost per W at scale; simple wiring
  Cons:  Single point of failure; lower partial-load efficiency
         Entire combiner string degrades if any module fails
  Use:   Large utility plants (>10 MW); declining vs string at utility

  ─────────────────────────────────────────────────────────

  MICROINVERTER (AC module):
  Module1──►[Micro-inv]──┐
  Module2──►[Micro-inv]──┤──► AC branch circuit ──► AC grid
  Module3──►[Micro-inv]──┘

  Pros:  Per-module MPPT; no string mismatch; module-level monitoring
         No high-voltage DC on rooftop (safety)
  Cons:  Higher cost per W; more units to potentially fail
  Use:   Residential (Enphase dominant); complex shaded roofs

  ─────────────────────────────────────────────────────────

  DC OPTIMIZERS + STRING INVERTER (SolarEdge model):
  Module1──►[DC opt]──┐
  Module2──►[DC opt]──┤──► String ──► String inverter ──► AC grid
  Module3──►[DC opt]──┘

  Pros:  Per-module MPPT; shade tolerance; keeps string inverter cost
         Module-level monitoring; fixed DC bus voltage (easier inverter design)
  Cons:  More components than pure string; SolarEdge lock-in risk
  Use:   Residential and commercial where shading is a concern
```

### Maximum Power Point Tracking (MPPT)

The I-V curve shifts with irradiance and temperature. MPPT continuously finds the
operating point (V, I) that maximizes power. Modern inverters do this in real-time
using perturb-and-observe or incremental conductance algorithms — effectively a
fast gradient descent on the P-V curve. At MIT you'd recognize this as trivial
numerics; the engineering challenge is doing it fast enough given rapid cloud transients.

---

## Capacity Factor and Resource Assessment

```
  CAPACITY FACTOR BY GEOGRAPHY (utility-scale, single-axis tracking):

  Region                         CF range
  ──────────────────────────────────────────
  US Southwest (Mojave, AZ)      28-32%
  US Southeast / Texas           22-26%
  US Midwest / Great Plains      18-22%
  Northeast US / New England     15-18%
  Germany / Central Europe       11-14%
  UK                             10-13%
  Middle East / North Africa     25-30%
  Chile Atacama Desert           30-35%
  India (Rajasthan)              25-30%
  Australia (Northern)           28-33%

  Single-axis tracking adds ~15-25% vs fixed-tilt (same capex premium ~5-8%)
  Almost always worth it for utility-scale in latitude > 25°.
```

### Solar Resource Measurement

```
  GHI (Global Horizontal Irradiance):  Total irradiance on horizontal surface
                                        DNI + DHI × cos(zenith angle)
                                        Standard metric for flat-panel systems

  DNI (Direct Normal Irradiance):       Beam radiation perpendicular to sun
                                        Used for concentrating solar (CSP, III-V)

  DHI (Diffuse Horizontal Irradiance):  Scattered light from sky
                                        Flat panels capture this; concentrators don't

  TMY (Typical Meteorological Year):    Synthetic year combining best-representative
                                        months from multi-year data
                                        Standard input for energy yield models

  Tools:
    NREL PVWatts:  Simple online calculator (system level yield estimate)
    NREL SAM:      System Advisor Model (detailed, free, industry standard)
    PVsyst:        Commercial, most widely used by project developers
    Solargis:      Commercial satellite-derived irradiance data
```

---

## LCOE Trajectory — The Learning Curve

```
  SOLAR PV MODULE PRICE ($/W, global average)
  ============================================

  2010:  $1.80/W  ←── "Solar is expensive"
  2012:  $0.70/W  ←── Chinese manufacturing scale
  2015:  $0.50/W
  2018:  $0.25/W
  2020:  $0.20/W
  2022:  $0.25/W  ←── supply chain disruptions (polysilicon shortage)
  2024:  $0.10-0.13/W (Chinese module spot price, oversupply)

  Learning rate: ~20-25% cost reduction per doubling of cumulative capacity
  Cumulative capacity doubled from 2010 to 2013, 2013 to 2016, 2016 to 2019...

  UTILITY-SCALE SYSTEM LCOE (including BoS, land, grid):
  2010:  ~$300/MWh
  2015:  ~$130/MWh
  2018:  ~$70/MWh
  2020:  ~$45/MWh
  2023:  ~$35-50/MWh (US; $20-35/MWh in best locations globally)
  2024:  ~$30-55/MWh (range reflects interconnection costs, location, financing)

  For context: US average wholesale electricity price ~$30-60/MWh.
  Solar is now at or below the marginal cost of gas in most US markets.
```

---

## Utility-Scale Plant Design

### Single-Axis Tracking

```
  FIXED TILT:                       SINGLE-AXIS TRACKING (SAT):

  Module angle fixed at ~latitude    Row rotates E→W through day
  optimal angle (e.g., 25° in TX)    following sun azimuth

  +===+                              +===+     Morning
                                    /
                               =====           Noon
                                    \
                                     +===+     Afternoon

  SAT energy gain vs fixed tilt:
    Low latitude (<30°): +15-20%
    Mid latitude (30-45°): +18-25%
    High latitude (>45°): +20-28% (worth it even in Germany)

  SAT capital cost premium: ~$50-100/kW (tracker hardware + civil)
  Typical payback: 3-5 years of additional generation value

  Ground coverage ratio (GCR):
    How densely packed rows are
    Low GCR (0.25-0.3): less shading between rows, more land
    High GCR (0.4-0.5): more shading but less land (relevant where land is costly)
```

### Agrivoltaics

Co-location of solar panels and agriculture. Panels provide partial shade → reduced
water stress for crops (particularly in hot/dry climates). Land use efficiency increases.
Active research area; some crops (shade-tolerant vegetables, berries) show yield increases.

### Plant Layout and Interconnection

```
  Large utility solar plant (~200 MW):

  ┌────────────────────────────────────────────────────┐
  │  ~80,000 modules (bifacial TOPCon, ~450 W each)    │
  │  ~200 acres land (at GCR 0.35)                     │
  │  String inverters every 2-4 rows (~100 kW ea)      │
  │  Medium-voltage collection (~34.5 kV)              │
  │  Substation with step-up transformer (138 kV)      │
  │  Point of interconnection (POI) to transmission    │
  └────────────────────────────────────────────────────┘

  Interconnection queue:
  • 2024: ~1,600 GW queued in US ISOs (2-5 year wait typical)
  • Single largest bottleneck to solar deployment
  • Grid upgrade cost allocation is the key policy dispute
  • FERC Order 2023: interconnection reform underway
```

---

## Distributed Generation — Rooftop Solar

```
  ECONOMICS DRIVERS FOR ROOFTOP:

  1. Retail rate arbitrage:
     "Save money by generating your own power"
     Value = retail electricity rate (avoiding $0.12-0.30/kWh)
     vs LCOE of rooftop (~$0.06-0.12/kWh in good markets)

  2. Net metering:
     Export surplus power to grid at (typically) retail rate
     Erodes utilities' revenue → ongoing policy battles
     NEM 3.0 in California: export rate cut ~75% (Jan 2023)
     → kills CA rooftop economics except with battery storage

  3. Self-consumption optimization:
     Battery storage shifts solar output to evening peak
     Increases self-consumption, reduces grid exports
     (IRA Section 48E: 30% investment tax credit for solar + storage)

  4. Demand charge reduction:
     Commercial customers: utility bills include $/kW peak demand charge
     Solar reduces peak → bill reduction beyond kWh savings

  Rooftop economics summary:
  Good (high retail rates, NEM):    CA before NEM 3, HI, NY, MA
  Challenging (NEM cutbacks):       CA after NEM 3.0
  Excellent (no net metering needed): TX deregulated market, commercial self-consumption
```

---

## Grid Challenges — The Duck Curve

```
  CALIFORNIA ISO DUCK CURVE (net load = total load minus solar generation)

  Load (GW) by hour:

  Hour:    0   2   4   6   8  10  12  14  16  18  20  22  24
  Net GW: 20  20  20  20  20  15  10  12  20  28  30  25  20

  Shape: morning baseline ~20 GW
         drops at midday (the "belly of the duck") to ~10 GW (solar fills it)
         climbs steeply 17:00–20:00 to peak ~30 GW (sun setting, demand high)
         drops back overnight

  The problem: steep evening ramp from ~17:00 to 20:00
  Grid must ramp up 10-15 GW in 3 hours as solar drops
  Requires: fast-ramping gas turbines OR storage OR demand flexibility

  CURTAILMENT: when solar generation > load (negative net load territory)
  CA curtailed ~2.7 million MWh in 2022, ~3+ million MWh in 2023
  Batteries absorbing midday excess → reduce curtailment
  This is the key economic driver for 4-hour BESS in California
```

---

## PPA Mechanics — Microsoft Context

```
  HOW A SOLAR PPA WORKS FOR A HYPERSCALER

  Microsoft Data Center                 Solar Farm (200 MW, Texas)
  (electricity consumer)               (independent power producer)
         │                                          │
         │  Virtual PPA                             │
         │  • 15-year contract                      │
         │  • Strike price: $35/MWh                 │
         │◄────────────────────────────────────────►│
         │                                          │
         │  If spot price > $35:                    │
         │    Farm pays Microsoft the difference    │
         │  If spot price < $35:                    │
         │    Microsoft pays farm the difference    │
         │                                          │
         │  Microsoft gets RECs from the farm       │
         │  (~200,000 MWh/yr = 200,000 RECs)        │
         │                                          │
         │  Microsoft reports Scope 2 = zero        │
         │  (market-based accounting)               │

  Why this enables farm financing:
    Bank: "Will this farm have revenue?"
    Developer: "Yes — Microsoft 15-year contract"
    Bank: "We'll lend at 5% instead of 10%"
    → Lower WACC → lower LCOE → project viable

  Microsoft 2023: ~20 GW of PPAs globally (solar-heavy, some wind)
```

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| Most deployed cell technology? | Monocrystalline silicon (PERC, now TOPCon) |
| Highest efficiency commercial? | HJT ~24-26%; TOPCon ~23-25% |
| Best efficiency roadmap? | Perovskite/Si tandem: 28-33%, near commercial |
| Utility-scale CF in US southwest? | 28-32% (single-axis tracking) |
| Why TOPCon replacing PERC? | Higher efficiency, bifacial gain, incremental mfg upgrade |
| String vs microinverter for home? | Microinverter if any shading; string if clean south-facing roof |
| DC optimizer vs microinverter? | Optimizer = cheaper, string-inverter compatible; micro = per-module AC |
| Best irradiance metric for flat panels? | GHI (global horizontal irradiance) |
| Why interconnection queue is the bottleneck? | 1,600 GW queued in US; 2-5 year waits |
| Bifacial gain over monofacial? | +5-15% depending on ground albedo |
| LCOE utility solar 2024? | $30-55/MWh US; $20-35/MWh best global locations |
| What is the duck curve? | Midday solar surplus → steep evening ramp as solar drops |

---

## Common Confusion Points

**"Module efficiency vs system efficiency"**
A 22% efficient module does not mean 22% of sunlight becomes grid power.
Module efficiency (STC) → real-world output → DC losses → inverter losses → transformer losses.
System efficiency (grid output / irradiance on module area) is typically 14-18%.

**"Rated power (Wp) vs actual power"**
Wp (watt-peak) is measured at STC: 1000 W/m², 25°C cell temperature.
On a hot summer day, cell temp is 60-70°C; actual power is 10-15% less than rated.
HJT wins in hot climates specifically because of better temperature coefficient.

**"Installing 1 kW of solar = 1 kWh/hr"**
No. At CF 18%, 1 kW installed produces ~1,577 kWh/yr = average 0.18 kW continuously.
The peak output is 1 kW, but only for a few hours around solar noon on clear days.

**"Perovskite is about to replace silicon"**
Lab efficiency records are impressive (26%+, tandems at 33%+).
Commercial timeline: perovskite alone struggled with stability (UV degradation,
moisture sensitivity, thermal cycling). Perovskite/Si tandems will enter commercial
market ~2025-2027 at premium prices, not immediately displacing silicon.
Lead content is a regulatory hurdle in some markets.

**"Solar is variable so it needs 1:1 storage backup"**
No. A grid is not a single generator. Diversity of solar locations, time zones, and
pairing with wind and hydro reduces the storage requirement substantially.
Studies show 80-90% renewable grids need 4-12 hours of storage per MW of peak demand,
not 24-hour storage per MW of solar capacity.
