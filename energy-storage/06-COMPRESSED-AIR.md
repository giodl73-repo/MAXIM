# Compressed Air and Gravity Storage: CAES, Adiabatic, LAES, and Gravity

## The Big Picture

Compressed air and gravity storage are the "mechanical alternatives" to pumped hydro --
using the same gravitational potential or pressure potential but without the geographical
constraints of a water reservoir. Each variant has a distinct thermodynamic design point
and economic niche.

```
MECHANICAL STORAGE TAXONOMY (non-pumped hydro)
=================================================

COMPRESSED AIR (CAES):
  Compress air into underground cavern or pressure vessel
  Use air to drive turbine for electricity generation

  DIABATIC CAES:              ADIABATIC CAES (A-CAES):     ISOTHERMAL:
  (heat from compression      (store compression heat,       (compress slowly,
  vented to atmosphere;       re-use it for expansion)       stay at ambient T)
  burn gas to reheat          No gas burning needed          Theoretical limit
  during expansion)           70%+ RTE possible              Very hard to achieve
  42-55% RTE                  Only test plants built         Only research
  Huntorf, McIntosh           Adele project (Germany)

LIQUID AIR (LAES):
  Liquefy air at -196 C
  Store in insulated tanks (no geological requirement)
  Regasify, expand through turbine
  50-60% RTE

GRAVITY (WEIGHTS):
  Raise heavy masses using electricity
  Lower them through generator when needed
  Simple physics, geography-independent

  GRAVITRICITY:                ENERGY VAULT:
  Deep mine shaft              Above-ground crane system
  Heavy cylindrical mass       Concrete blocks (~35 ton)
  Winch motor/generator        Stacked and unstacked
  Very high power density      Demonstrated at MW scale
  Short duration (1-8 hr)      Long duration possible
  30 MW UK prototype           9 MW / 36 MWh deployed
```

---

## Compressed Air Energy Storage (CAES): Thermodynamics

### The Compression Heat Problem

The thermodynamic challenge of CAES is fundamental: compressing air heats it. If that
heat is lost, efficiency is lost. Different CAES designs handle compression heat differently.

```
THERMODYNAMICS OF AIR COMPRESSION
====================================

ISOTHERMAL COMPRESSION (theoretical ideal):
  Keep temperature constant during compression (T = constant)
  Work = n * R * T * ln(P2/P1)  (minimum work to compress gas)
  All work goes to increasing pressure only; no temperature rise
  Problem: requires infinitely slow compression or perfect heat exchange
  Not practical at large scale

ADIABATIC COMPRESSION (actual, no heat exchange):
  T rises during compression: T2 = T1 * (P2/P1)^((gamma-1)/gamma)
  gamma for air = 1.4
  From 1 bar to 70 bar:
    T2 = 293 K * (70)^(0.4/1.4) = 293 K * 70^0.286 = 293 * 3.57 = 1046 K = 773 C
  Air exits compressor at hundreds of degrees C
  If that heat is WASTED: efficiency lost (you paid to heat the air, then cooled it)
  If that heat is STORED: efficiency recovered (use it to reheat during expansion)

EXPANSION (generation):
  Cold high-pressure air expands adiabatically:
    T drops: T2 = T1 * (P1/P2)^((gamma-1)/gamma)
  Expanding cold compressed air (after stored heat was lost) -> very cold air out
  Cold air has LOW enthalpy -> can't drive turbine efficiently
  For diabatic CAES: burn natural gas to heat air before expansion (restores enthalpy)
  For A-CAES: use stored thermal energy from compression instead of burning gas
```

### Diabatic CAES: Huntorf and McIntosh

```
DIABATIC CAES (first generation)
==================================

OPERATING PLANTS:
  Huntorf (Germany, 1978): 321 MW, 8 hours
    First CAES plant in the world; still operating
    Compresses air into two salt caverns at 70 bar
    Burns natural gas to reheat air before turbine expansion
    Heat rate: ~4,400 kJ/kWh of natural gas (adds fuel input)
    RTE: ~42% (electricity in) if you count the gas input
    If you count only electricity-in/electricity-out: ~42%
    Use case: overnight off-peak power -> daytime peak power

  McIntosh (Alabama, USA, 1991): 110 MW, 26 hours
    Improved Huntorf with recuperator (uses exhaust heat to pre-heat inlet air)
    RTE: ~54% (better than Huntorf)
    Salt cavern: ~500,000 m^3 at 45-76 bar
    Only two commercial diabatic CAES plants in world as of 2025

DIABATIC EFFICIENCY ANALYSIS:
  Input:  1 kWh electricity (to compress) + 0.69 kWh of gas (to reheat)
  Output: 1 kWh electricity
  Pure electrical RTE: 42-55%
  Not a pure storage technology -- also a gas peaker (burns fuel)
  Economics: depends on electricity price + gas price arbitrage
  Environmental: CO2 emissions from gas combustion (problematic for clean grid)
```

### Adiabatic CAES (A-CAES)

```
ADIABATIC CAES (second generation)
=====================================

KEY DISTINCTION: store compression heat in a Thermal Energy Storage (TES) unit
Then: use stored heat to re-heat air during expansion
Result: no gas burning required; higher RTE

A-CAES CYCLE:
  Charge phase:
    1. Motor drives compressor (electricity -> mechanical -> pressure + heat)
    2. Compressed air exits at 600-800 C (depending on pressure ratio)
    3. Air passes through TES (solid rock, molten salt, oil -- stores heat)
    4. Cooled compressed air enters underground cavern at ambient-ish temperature

  Discharge phase:
    1. Cold compressed air exits cavern
    2. Air passes through TES (picks up stored heat back)
    3. Hot (600-800 C) compressed air drives turbine
    4. Turbine drives generator -> electricity out

TES MATERIALS FOR A-CAES:
  Solid rock beds: cheap, simple; limited temperature (< 600 C)
  Ceramic tiles: up to 900 C; specific heat ~1 kJ/kg/K
  Molten salt (like CSP plants): 565 C limit (NaNO3/KNO3)
  Oil (Therminol VP-1): up to 400 C; lower temperature stores less energy
  Concrete: cheap, slow response

THEORETICAL RTE:
  A-CAES with ideal TES and turbomachinery: ~70-72% round-trip
  Real systems with losses: ~60-70%
  Significantly better than diabatic (42-55%)

STATUS:
  ADELE project (Germany, RWE + Zublin + DLR): pilot-scale A-CAES
    Target: 200 MW, 1 GWh; Huntorf salt cavern as storage
    Project stalled ~2016 due to economics (natural gas cheap in Germany then)
  Hydrostor (Canada): A-CAES in aquifers (water-compensated: water column maintains
    constant pressure regardless of fill level -- allows constant turbine operation)
    Projects in development: 500 MW (Rosamond, CA), 400 MW (Adelaide, AUS)
  General Compression: isothermal CAES concept using ocean water heat sink (Texas)
```

---

## Liquid Air Energy Storage (LAES)

```
LIQUID AIR ENERGY STORAGE
===========================

PROCESS:
  Charge:
    1. Air liquefaction: compress + cool + expand through Joule-Thomson valve
       Linde-Hampson cycle: T drops from ~300K to 77K (-196 C, boiling point of N2)
       Specific work for liquefaction: ~0.45 kWh/kg-liquid-air (energy cost!)
    2. Store liquid air in well-insulated cryogenic tank (-196 C, near atmospheric pressure)
       Tank: double-walled vacuum-insulated (like a giant Dewar flask)
       Boiloff rate: 0.1-0.2%/day (acceptable for weekly cycling)

  Discharge:
    1. Pump liquid air to high pressure (150-200 bar) using cryogenic pump
       (liquid is easy to pump vs. compressing gas)
    2. Heat liquid air using ambient heat or waste industrial heat
    3. Air expands through turbine (like CAES discharge, but from liquid start)
    4. Generate electricity

EFFICIENCY:
  Liquefaction: ~45-60% of electricity goes to making liquid air
  Regasification + generation: ~60% of stored energy recovered
  Net RTE: ~45-60% (better with industrial waste heat input)

  With co-location at industrial waste heat source:
    Warm-up air from steel plant exhaust, power station cooling water
    -> Adds ~20% to RTE (waste heat is "free")
    Net: up to 70% RTE with waste heat

ADVANTAGES vs. CAES:
  NO geological requirement: any flat industrial site works
  Modular: tanks can be shipped and installed anywhere
  Geographic independence: major advantage vs. CAES caverns or pumped hydro
  Long duration possible: add more liquid air tanks (cheap)

DISADVANTAGES:
  High liquefaction energy cost (45-60% of energy input lost to liquefy)
  Expensive equipment: cryogenic compressors, turbines, tanks
  Insulation requirement (boiloff if stored too long)

COMMERCIAL STATUS:
  Highview Power: 50 MW / 250 MWh plant in operation (Greater Manchester, UK, 2023)
    First commercial LAES facility
    Uses landfill gas peaker plant waste heat for warm-up
  Highview + Sumitomo: 50 MW / 250 MWh projects in multiple countries
  Technology Risk Level (TRL): ~7-8 (commercial demonstration achieved)
```

---

## Gravity Storage

### Gravitricity: Mine Shaft and Heavy Mass

```
GRAVITRICITY (UK)
==================

CONCEPT:
  Steel shaft (vertical, 150-1500 m deep)
  Heavy cylindrical mass: 500-5,000 tonnes
  Winch connected to generator
  Lower mass: generates electricity
  Raise mass: stores energy

PHYSICS:
  E = m * g * h
  10,000 tonne mass (10^7 kg) at h=1000m:
  E = 10^7 * 9.81 * 1000 = 9.81 * 10^10 J = 27.3 MWh

  Multiple masses in same shaft: parallel cylinders
  Power: P = m * g * h * (1/t) = E / t (discharge time determines power)

DEMO:
  250 kW demonstrator in Edinburgh (2022)
  50 MW / multiple hours shaft system target

ADVANTAGES:
  Abandoned mine shafts exist globally -- no new drilling needed
  Fast response: <1 second (like flywheel)
  Long cycle life (no electrochemical degradation)
  Geography independent (any deep mine)
  RTE: ~80-90% (mechanical losses only)

DISADVANTAGES:
  Limited energy per shaft: a 1 km shaft is ~30 MWh max
  Scaling: add more shafts (cost), not deepen one shaft
  Not competitive on $/kWh with pumped hydro or Li-ion at large scale
  Best for: fast response + short duration (1-8 hours) in mine locations
```

### Energy Vault: Above-Ground Concrete Blocks

```
ENERGY VAULT
=============

CONCEPT:
  Multi-story crane structure
  ~35-tonne concrete blocks raised/lowered by cable + generator
  No underground: fully above-ground installation
  Software orchestrates block placement (Tetris-like optimization)

SPECIFICATIONS (EVx system, 2022):
  Power: 4-80 MW (modular)
  Duration: 2-12 hours
  Energy: 4-160 MWh
  RTE: ~80-82% (claimed)
  First deployment: 80 MWh, Saudi Arabia (NEOM project, 2023)

ADVANTAGES:
  No geological requirement
  Fully modular and scalable
  Blocks can be made from local material (soil, concrete, demolition waste)
  Long cycle life (no chemical degradation)
  Fast response

DISADVANTAGES:
  Capital intensive (crane infrastructure)
  Physical scale: large visual footprint
  Power density: limited by crane speed
  $/kWh vs. alternatives: needs more field validation
  Limited commercial deployments (scale-up risk)

COMPARISON:
  Technology    Geo required   RTE    Duration   Status
  CAES diabatic  Yes (cavern)  42-55%  4-26 hr  Commercial (2 plants)
  A-CAES         Yes (cavern)  60-70%  8-24 hr  Pilot (Hydrostor)
  LAES           No            45-60%  4-12 hr  Commercial (1 plant)
  Gravitricity   Yes (mine)    80-90%  1-8 hr   Demonstration
  Energy Vault   No            80-82%  2-12 hr  Early commercial
```

---

## Economics and Use Cases

```
ECONOMICS COMPARISON (mechanical storage alternatives)
=======================================================

Technology     CAPEX $/kW   CAPEX $/kWh   RTE   Duration   Status
-------------  -----------  ------------  ----  ---------  ----------
Diabatic CAES  $400-800     $25-100       42-55%  4-26 hr   2 plants (old)
A-CAES         $800-1500    $80-150       60-70%  8-24 hr   Pilot
LAES           $600-1200    $100-200      45-60%  4-12 hr   1 commercial plant
Gravity mine   $400-800     $100-300      80-90%  1-8 hr    Demonstration
Energy Vault   $300-600     $100-200      80-82%  2-12 hr   Early commercial
Pumped hydro   $500-3000    $50-200       70-85%  8-100+ hr  Very commercial
Li-ion         $500-1200    $200-400      90-95%  1-4 hr     Very commercial
VRFB           $400-800     $150-400      65-80%  4-12 hr   Commercial
```

---

## Decision Cheat Sheet

| Context | Best Mechanical Storage Option |
|---------|-------------------------------|
| Near abandoned salt cavern, short duration | Diabatic CAES (if gas acceptable) |
| Near cavern, want no gas combustion | A-CAES (Hydrostor) |
| No geology available, medium duration | LAES (Highview) |
| Near abandoned mine, fast response needed | Gravitricity |
| Geography-free, modular deployment | Energy Vault |
| Long duration (>10 hr), geography available | Pumped hydro (still best economics) |
| All options vs. Li-ion for 4-hour storage | Li-ion wins (cheaper, faster to deploy) |

---

## Common Confusion Points

**"CAES is a pure storage technology."** Diabatic CAES is not -- it burns natural gas.
It is a hybrid compressed-air + gas peaker plant. This is why only two commercial diabatic
CAES plants exist; economics depend on gas prices. Adiabatic CAES (A-CAES) eliminates
gas and is pure storage, but no commercial A-CAES plant was operational as of 2025.

**"LAES is inefficient at 50-60% RTE."** Compared to Li-ion (90-95%), yes. But for
long-duration grid storage, $/kWh amortized over decades matters more than efficiency.
LAES with co-located industrial waste heat can reach 70%+ effective RTE and competes
on cost with VRFB for 8-24 hour applications.

**"Gravity storage (Energy Vault, Gravitricity) is too small scale."** Individual units:
yes (4-160 MWh). But so is a single Li-ion container (~2-10 MWh). The question is
whether the technology scales to GWh with competitive economics. Gravity storage lacks
the empirical data to assess this yet; it has limited commercial deployments.

**"Compressed air and gravity storage are not nanoscale -- wrong directory."** Correct:
they are macroscale engineering. They belong in the energy-storage/ directory alongside
batteries and hydrogen, not in nanotechnology/. The guide you're reading is energy-storage/.
