---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "07-HYDROGEN.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:energy-storage:hydrogen
kind: guide
module: energy-storage
section: energy-storage
title: Hydrogen: Electrolysis, Storage, Fuel Cells, and the Hydrogen Economy
status: source-custody
source_custody: partial
current_path: energy-storage/07-HYDROGEN.md
canonical_path: energy-storage/07-HYDROGEN.md
backsource_ids: [proof-backfill:energy-storage:07-hydrogen, git-history:energy-storage:07-hydrogen]
concepts: [hydrogen]
root_concepts: [hydrogen]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Hydrogen: Electrolysis, Storage, Fuel Cells, and the Hydrogen Economy

## The Big Picture

Hydrogen is both a storage medium and an energy carrier. As electricity storage,
electricity -> H2 -> electricity has poor round-trip efficiency relative to batteries
or pumped hydro. As a molecule for fertilizer, refining, steel, shipping fuels, or
seasonal storage, its value can be independent of electricity round-trip efficiency.
The hydrogen-economy debate is therefore a role-selection problem, not a yes/no
verdict on hydrogen.

```
HYDROGEN VALUE CHAIN
======================

PRODUCTION          STORAGE            USE
===========         ===========        ===========
                    Compressed         Fuel cell
Electrolysis        gas (350/700 bar)  electricity
(green H2)     ->                  ->
                    Liquid H2          Combustion
Steam methane       (-253 C)           (turbine,
reforming                              boiler)
(grey H2)      ->   Metal hydride  ->
                                       Industrial
Coal gasification   Chemical carrier   feedstock
+ CCS              (ammonia NH3,       (fertilizer,
(blue H2)     ->    LOHC)         ->   steel, refinery)

H2 COLOR TAXONOMY:
  Grey: steam methane reforming (no CCS), 95% of current production
  Blue: steam methane reforming + carbon capture and storage (CCS)
  Green: electrolysis with renewable electricity (target for decarbonization)
  Pink: electrolysis with nuclear electricity
  Turquoise: methane pyrolysis (CH4 -> H2 + solid C, no CO2 gas)
  Teal: natural gas with CCS (variant of blue)
```

---

## Electrolysis

### Alkaline Electrolysis (AEL)

```
ALKALINE ELECTROLYSIS
=======================

REACTIONS:
  Cathode (HER): 2H2O + 2e- -> H2 + 2OH-  (hydrogen evolution)
  Anode (OER): 2OH- -> 1/2 O2 + H2O + 2e-  (oxygen evolution)
  Overall: H2O -> H2 + 1/2 O2  (delta_G = +237 kJ/mol = 1.23 V minimum)

ALKALINE ELECTROLYTE: 20-30% KOH or NaOH solution
  High pH: reduces OER overpotential (easier O2 evolution in alkaline)
  Low-cost materials: Ni electrodes (no platinum needed)
  Diaphragm: porous separator (Zirfon membrane or asbestos)
    Keeps H2 and O2 separate; OH- can pass through

SPECIFICATIONS:
  Operating temperature: 60-90 C
  Operating pressure: 1-30 bar
  Stack efficiency: ~70-75% (LHV basis)
  Capital cost: $500-800/kW (electrolysis stack) (2025)
  Stack lifetime: 80,000-150,000 hours
  Part-load range: 20-100% (cannot go below ~20% without issues)

ADVANTAGES:
  Mature technology (100+ years industrial use)
  No platinum group metals
  Lowest CAPEX of all electrolysis types
  Proven at MW and >100 MW scale
  Long stack lifetime

DISADVANTAGES:
  Slow response to load changes (minutes to follow wind/solar)
  Minimum load ~20% (can't shut down and restart quickly)
  Produces at low pressure (requires compression for storage)
  KOH corrosive; liquid electrolyte management
```

### PEM Electrolysis (PEMEL)

```
PEM ELECTROLYSIS (Proton Exchange Membrane)
=============================================

MEMBRANE: Nafion (perfluorosulfonic acid polymer)
  Proton-conducting membrane: H+ passes, not H2 or O2
  Operates in acid environment (low pH)

REACTIONS:
  Anode (OER): H2O -> 1/2 O2 + 2H+ + 2e-
  Cathode (HER): 2H+ + 2e- -> H2
  H+ transports through Nafion membrane from anode to cathode

CATALYST REQUIREMENTS:
  Anode: IrO2 (iridium oxide) for OER -- expensive (Ir: ~$5000/kg)
    Iridium is very rare (Earth's crust: 0.001 ppm vs. platinum 0.005 ppm)
    Ir supply constraint: major concern for PEM scale-up
  Cathode: Pt (platinum) for HER -- also expensive but less than Ir
  Loading: 0.1-0.5 mg/cm^2 (research trending toward <0.05 mg/cm^2)

SPECIFICATIONS:
  Operating temperature: 50-80 C
  Operating pressure: 30-80 bar (can directly produce at high pressure)
  Stack efficiency: ~75-80% (LHV basis) -- slightly better than AEL
  Capital cost: $800-1500/kW (2025, decreasing with scale)
  Stack lifetime: 50,000-100,000 hours
  Part-load range: 5-100% (much better than AEL)
  Response time: seconds (can follow solar/wind directly)

ADVANTAGES:
  Fast response: ideal for variable renewable energy coupling
  High current density: 2-3 A/cm^2 vs. 0.5 A/cm^2 for AEL -> compact stack
  Direct high-pressure H2 production
  No liquid electrolyte

DISADVANTAGES:
  Iridium constraint: limited Ir mining globally (~7 tonnes/yr)
    At 0.5 mg Ir/cm^2 and 2 A/cm^2: 1 GW electrolyzer needs ~100 kg Ir
    -> 1 TW of green H2 would need 100 tonnes Ir/yr (14x current mining)
  Higher CAPEX than AEL
  Nafion membrane cost and fluoropolymer sustainability
  Needs ultra-pure water (deionized: <1 uS/cm)
```

### Solid Oxide Electrolysis (SOEC)

```
SOLID OXIDE ELECTROLYSIS CELL (SOEC)
======================================

PRINCIPLE: High-temperature (700-900 C) electrolysis of steam
  Same materials as solid oxide fuel cells (SOFC) -- reverse operation

REACTIONS:
  Cathode: H2O + 2e- -> H2 + O2-  (steam reduced to H2 at cathode)
  Anode: 2O2- -> O2 + 4e-         (oxygen ions oxidized to O2 at anode)
  O2- ions transport through dense ceramic oxide electrolyte (YSZ: yttria-stabilized zirconia)

THERMODYNAMIC ADVANTAGE:
  At 800 C: electrical energy requirement DROPS
  delta_G of water splitting decreases with temperature (delta_H approximately constant,
    T*delta_S increases -> delta_G = delta_H - T*delta_S decreases)
  At 800 C: ~20% of energy requirement comes from heat, not electricity
  If heat source available (nuclear, industrial waste heat):
    System efficiency: ~90% (electrical) because 20% is heat-input

SPECIFICATIONS:
  Operating temperature: 700-900 C
  Electrical efficiency: ~85-90% (LHV, if heat is free or cheap)
  Capital cost: $1000-2000/kW (2025, immature)
  Stack lifetime: 20,000-50,000 hours (thermal cycling is the lifetime killer)
  Can also co-electrolyze H2O + CO2 -> H2 + CO (syngas) for e-fuels

ADVANTAGES:
  Highest electrical efficiency of any electrolysis method
  Co-electrolysis of H2O + CO2 for Power-to-X applications
  Reversible: SOEC (electrolysis) can run as SOFC (fuel cell) in same unit

DISADVANTAGES:
  High operating temperature: startup time (hours to reach 800 C)
  Thermal cycling degradation (ceramic cracks from thermal stress)
  Cannot follow variable renewables (temperature too sluggish)
  Best suited for: baseload operation (nuclear + SOEC, industrial waste heat + SOEC)
  Status: limited commercial (Haldor Topsoe, Bloom Energy have MW systems)
```

---

## Hydrogen Storage

### Compressed Gas

```
COMPRESSED H2 STORAGE
=======================

700 bar TYPE IV TANK (automotive):
  Carbon fiber reinforced polymer (CFRP) over plastic liner
  Operating pressure: 700 bar (70 MPa = ~10,000 psi) -- very high pressure
  Design pressure: 875 bar (1.25x operating with safety factor)
  Burst pressure: >1,750 bar (2.5x operating)
  Gravimetric density: ~5.7 wt% H2 (of tank system) -- system level
  Volumetric density: ~39 g/L (at 700 bar)
  H2 mass: 5-6 kg in automotive tank (FCV: Toyota Mirai: 5.6 kg, 3 tanks)

  ENERGY TO COMPRESS:
    From 1 bar to 700 bar: ~15% of energy content of H2 is consumed by compressor
    High-pressure fueling stations require careful cascade filling protocol

350 bar TANK:
  Used for: heavy vehicles (buses, trucks), forklift trucks, bulk storage
  Lower mass/cost than 700 bar; lower volumetric density
  Toyota Mirai (passenger car): 700 bar; Hyundai XCIENT truck: 350 bar

UNDERGROUND COMPRESSED H2:
  Salt caverns (same as CAES): possible, demonstrated
  Lined rock caverns: viable
  Depleted gas fields: natural porous rock, H2 bacteria issue (microbes consume H2)
  Salt caverns best: impermeable, non-reactive with H2, multiple operating projects
    Moss Bluff (TX, USA): H2 storage in salt cavern (400 million scf)
```

### Liquid Hydrogen

```
LIQUID HYDROGEN
================

Boiling point: -252.8 C = 20.3 K (just above absolute zero)
  Nitrogen boils at -196 C; liquid H2 is 57 C colder than liquid N2

Liquefaction process (Linde-Hampson + expansion turbines):
  Precooling in N2 liquid (liquid N2 at 77 K cools H2 to 80 K first)
  Then: H2 compression + expansion (Joule-Thomson) -> liquid
  Energy cost of liquefaction: 30-35% of H2 energy content (enormous penalty)

Density:
  Liquid H2: 70.8 kg/m^3 (vs. liquid N2 at 808 kg/m^3 -- very light)
  Gravimetric: ~100% H2 in pure liquid (no containment weight at point of count)
  Volumetric: 70.8 g/L (better than 700 bar compressed at 39 g/L)

BOILOFF:
  Insulated cryogenic tank leaks heat -> H2 evaporates (boiloff)
  Rate: 0.1-1%/day for stationary tanks; 1-5%/day for vehicle tanks (smaller)
  Requires venting (safety) or recapture
  Long-term storage: cumulative boiloff loss is significant
  Best for: large-scale (ship, terminal) where insulation surface/volume ratio good

APPLICATIONS:
  Rocket fuel: NASA, SpaceX (Falcon 9 uses LOX/kerosene; Starship: LOX/LCH4)
    SLS (Space Launch System): liquid H2/LOX -- highest specific impulse chemical rocket
  Aviation: Airbus zero-emission aircraft concept (H2SPEED)
  Long-distance shipping: liquid H2 tanker (Suiso Frontier, Japan-Australia 2021)
```

### Chemical Carriers

```
HYDROGEN CHEMICAL CARRIERS
============================

AMMONIA (NH3):
  Reaction: N2 + 3H2 -> 2NH3 (Haber-Bosch, 450 C, 200 bar, Fe catalyst)
  H2 content: 17.8 wt% (high gravimetric density)
  Liquid at: -33 C (easily liquefied vs. H2 at -253 C)
  Well-established global infrastructure: 200 Mt/yr production, pipelines, ships
  NH3 -> H2 release: crack ammonia at 500-700 C, Ru or Ni catalyst
    Efficiency: ~25-30% energy lost in Haber-Bosch + cracking
  Advantages: liquid at -33 C; infrastructure exists; no CO2
  Disadvantages: toxic (TLV 25 ppm), NOx on combustion, cracking energy loss
  Status: green ammonia projects (Australia, Chile) for export to Japan/Germany

LOHC (Liquid Organic Hydrogen Carriers):
  Hydrogenate an aromatic compound to store H2 chemically at room temperature
  Dehydrogenate (thermally) to release H2

  Common LOHC: Dibenzyltoluene (DBT) + H2 -> perhydro-DBT (H18-DBT)
    H2 content: 6.2 wt% of carrier (19 g H2/L)
    Loading temp: 150-200 C (exothermic, useful heat generated)
    Unloading temp: 310-350 C (endothermic, requires heat input)
    Key advantage: carrier (DBT) is stable at ambient temperature and pressure
    Transport: existing liquid fuel tankers and infrastructure
    No special vessels needed (unlike LH2 cryogenic or NH3 toxic)

  LOHC companies: Hydrogenious (Germany), ChiyodA Corporation (Japan)
  Challenge: energy cost of dehydrogenation (heat at 310 C needed at point of use)

METAL HYDRIDES (solid-state H2):
  H2 absorbed into metal lattice (interstitial sites)
  Low operating pressure (1-10 bar vs. 700 bar for gas)
  Materials: LaNi5 (1.4 wt% H2), TiFe (1.9 wt%), MgH2 (7.6 wt% but 300+ C)
  Gravimetric density: lower than liquid H2 or LOHC (heavy metal lattice)
  Volumetric density: excellent (better than 700 bar gas for some hydrides)
  Use case: very safe (no high pressure, no fire risk if ruptured)
    Submarine auxiliary power, stationary backup power
  Status: niche; Toyota Mirai uses 700 bar compressed, not hydride
```

---

## Fuel Cells

### PEM Fuel Cell

```
PEM FUEL CELL
==============

Reverse of PEM electrolysis:
  Anode: H2 -> 2H+ + 2e-  (H2 oxidized, electrons to circuit)
  Cathode: O2 + 4H+ + 4e- -> 2H2O (O2 reduced, protons from membrane)
  Net: H2 + 1/2 O2 -> H2O  (delta_G = -237 kJ/mol = 1.23 V theoretical)

ACTUAL VOLTAGE: ~0.6-0.75 V per cell under load (vs. 1.23 V theoretical)
  Activation losses (Butler-Volmer): 0.3-0.4 V loss
  Ohmic losses (membrane resistance): 0.05-0.1 V
  Mass transport (O2 depletion at cathode): small at moderate current

EFFICIENCY:
  Thermodynamic efficiency limit: 83% (delta_G / delta_H = 237/286)
  Practical efficiency (cell voltage / 1.23 V): 0.65/1.23 = 53%
  System efficiency (including BOP): ~45-55%
  Compare: gasoline ICE: 25-35%; natural gas turbine: 35-45%
  Fuel cell wins on efficiency vs. combustion (but loses on round-trip vs. battery)

PLATINUM LOADING:
  Cathode: 0.2-0.4 mg Pt/cm^2 (more for ORR, less active than HOR)
  Anode: 0.05-0.1 mg Pt/cm^2 (HOR is fast, low loading needed)
  Target: <0.1 mg Pt/cm^2 total (current research frontier)
  Pt supply: ~190 tonnes/yr mined; 1 GW/yr FC production needs ~10 tonnes
    -> At current loading, 100 GW/yr would need significant Pt supply scaling

APPLICATIONS:
  Toyota Mirai: 128 kW FC + 1.24 kWh Li-ion buffer, 5.6 kg H2 -> 650 km
  Hyundai NEXO, Honda Clarity, GM/Honda hydrogen truck programs
  Forklift trucks: established market (Plug Power)
  Stationary backup power: telecom towers, data centers
  Marine: Alstom H2-powered commuter train (Coradia iLint), German operations
```

---

## The Round-Trip Math: Why H2 Storage is Inefficient

```
HYDROGEN ROUND-TRIP EFFICIENCY
================================

Pathway 1: Renewable electricity -> H2 (PEM) -> compressed storage -> PEM fuel cell -> electricity

Step                    Efficiency   Cumulative
----------------------  -----------  ----------
PEM electrolysis        78%          78%
Compression to 700 bar  85%          66%
Fuel cell (PEM)         55%          36%

RESULT: ~35-40% round-trip efficiency

Compare to Li-ion: 90-95% round-trip efficiency
-> For every 100 kWh of wind electricity put in:
   H2 storage returns: ~35-40 kWh
   Li-ion returns: ~90-95 kWh

Hydrogen "costs" 2.5x more electricity than batteries for same useful output

WHEN HYDROGEN MAKES SENSE DESPITE LOW EFFICIENCY:
  1. Seasonal storage: no battery technology can store summer solar for winter at GWh scale
     Pumped hydro can, but limited geography. H2 cavern storage: possible.
  2. Industrial feedstock: H2 is needed for NH3 (fertilizer), steel (DRI), refineries
     Grid storage is secondary to primary value as feedstock
  3. Long-distance transport: ship green ammonia from Australia to Japan
     No wire can carry electricity across the Pacific Ocean
  4. High energy density transport (aviation, shipping):
     Liquid H2: 33 kWh/kg vs. Li-ion: ~0.3 kWh/kg (100x energy density)
     Despite round-trip losses, liquid H2 as aviation fuel is seriously considered
  5. Grid service at long duration:
     H2 stored in salt cavern at $1-10/kWh (cheapest possible storage)
     Even at 35% RTE, seasonal economics may work for 3-month duration
```

---

## Hydrogen Economy: Green vs. Grey vs. Blue

```
HYDROGEN COLOR ECONOMICS (2025)
=================================

GREY H2 (SMR, no CCS):
  CH4 + H2O -> CO + 3H2 (steam methane reforming)
  CO + H2O -> CO2 + H2 (water-gas shift)
  Cost: $1-2/kg H2
  CO2 emissions: ~10 kg CO2 per kg H2
  Current: 95% of all H2 production

GREEN H2 (electrolysis + renewable electricity):
  Cost: $3-8/kg H2 (2025)
  Target: $1/kg H2 ("H2 1 1 1": $1/kg by 2031, DOE goal)
  CO2 emissions: ~0 (if electricity is zero-carbon)
  Gap vs. grey: $2-6/kg H2 premium for decarbonization
  Requires: cheap renewable electricity (<$20/MWh) + cheap electrolyzer (<$300/kW)
  Learning rate: electrolyzer CAPEX declining ~15-20%/yr (similar to solar)

BLUE H2 (SMR + CCS):
  Cost: $1.5-3/kg H2
  CO2 capture rate: 85-95% (not 100% -- residual methane leakage is issue)
  Gap vs. grey: modest premium
  Controversy: methane leakage upstream (well to pipeline) reduces climate benefit
    If upstream leakage >2.5% methane: blue H2 worse than coal (100-year GWP)
    Most EU regulatory sentiment: blue H2 is a transition fuel, not long-term solution

COST DRIVERS FOR GREEN H2 COST REDUCTION:
  Electricity cost: dominates (~70-80% of LCOH)
    At $20/MWh electricity + PEM at 75% efficiency:
    H2 production electricity = (33.3 kWh/kg H2) / 0.75 = 44 kWh/kg H2
    Electricity cost: 44 * $0.02 = $0.88/kg H2 (achievable in 2030s?)
  Electrolyzer CAPEX: at $300/kW and 90% capacity factor: $0.10/kg H2
  OPEX, balance of plant: $0.20/kg H2
  Total: ~$1.2/kg H2 (target scenario, requires very cheap electricity)
```

---

## Decision Cheat Sheet

| If you need to diagnose... | Start With | Key Caveat |
|---|---|---|
| Whether hydrogen is the right energy carrier | Identify end use: chemical feedstock, industrial heat, transport fuel, seasonal storage, backup power, or daily electricity arbitrage. | Hydrogen is usually weak as a daily battery substitute but can be strong where a molecule is required. |
| Which electrolyzer fits | Compare alkaline, PEM, and SOEC by load-following, efficiency, stack cost, critical materials, water purity, pressure, and heat integration. | Fast response is not the only criterion; utilization and capex dominate hydrogen cost. |
| Whether "green" hydrogen is actually low carbon | Check electricity source, temporal matching, grid emissions, electrolyzer utilization, water source, compression/liquefaction energy, and leakage. | A color label is not an LCA; emissions depend on boundaries and operating pattern. |
| Which storage mode fits | Compare 350/700 bar tanks, salt caverns, liquid hydrogen, ammonia/LOHC, and metal hydrides by scale, duration, safety, and losses. | The cheapest storage is geological and location-specific; tanks are flexible but expensive per kWh. |
| Whether transport by ship is plausible | Compare liquefaction, ammonia synthesis/cracking, LOHC cycling, port infrastructure, toxicity, boil-off, and end-use purity. | Shipping H2 is often really shipping a carrier molecule, with conversion losses and safety regimes. |
| Whether fuel cells or turbines fit | Check scale, duty cycle, efficiency, start time, fuel purity, emissions, maintenance, and heat recovery. | Fuel cells fit vehicles and distributed power better; turbines fit bulk power but may need NOx controls and blending limits. |
| Whether hydrogen can decarbonize a sector | Start with the incumbent molecule or heat process, electrification alternative, cost premium, infrastructure, and policy support. | Use hydrogen where direct electrification is technically or economically weak, not because it is fashionable. |

---

## Cross-References

- `01-ELECTROCHEMICAL.md` contrasts batteries with hydrogen's power-to-gas pathway.
- `08-GRID-ECONOMICS.md` explains when long-duration storage can justify low round-trip efficiency.
- `../energy-systems/04-HYDROGEN.md` connects storage hydrogen to broader energy-system uses.

## Common Confusion Points

**"Hydrogen is a clean energy source."** Hydrogen is an energy CARRIER (like electricity),
not a primary energy source. Its carbon footprint depends entirely on how it was produced.
Grey H2 (95% of current production) emits ~10 kg CO2/kg H2. Green H2 is zero carbon.

**"H2 fuel cells are more efficient than batteries."** Fuel cells are more efficient than
combustion engines (~50-55% vs. 25-35%), but less efficient than batteries (~90-95%).
The comparison depends on what you're comparing to.

**"The hydrogen economy will replace electricity."** Unlikely for most applications.
For road transport, industrial heat, chemical feedstocks, and long-duration storage:
hydrogen has unique value. For short-duration storage, daily transportation, and
heating: direct electricity is more efficient and likely cheaper. The debate is about
which applications are genuinely hydrogen-native vs. forced.

**"Hydrogen is too dangerous to handle."** Hydrogen has different hazards from gasoline
or methane: very low ignition energy, wide flammability range (4-75% vs. 5-15% for
methane), but also much lighter than air (disperses rapidly outdoors), no toxic
combustion products, 500x less radiant heat than gasoline fires. Safety engineering
handles it -- industrial H2 has been handled safely for 100+ years.
