# Energy Systems — The Alchemist's Question

*Where does availability die?*

Every energy system is a machine for destroying exergy. Primary energy enters with
thermodynamic potential — the capacity to do work relative to the dead state of the
environment. At every conversion step, irreversibility consumes some of that potential.
What reaches the end user is what survived the gauntlet. The Alchemist's discipline is
knowing exactly where the losses hide, why each one is there, and which are negotiable.

---

## The Big Picture — Exergy Destruction Chain

```
PRIMARY ENERGY SOURCES                            EXERGY CONTENT
┌────────────────────────────────────────────────────────────────────────────┐
│  CHEMICAL (fossil, biomass)   ΔG_rxn of combustion      ~100% of LHV     │
│  NUCLEAR  (fission, fusion)   Q-value × (1 - T₀/T_rad)  ~70% of thermal │
│  SOLAR    (photons, 5778 K)   Petela limit: 93%         ~93% of flux     │
│  GRAVITATIONAL (hydro, tidal) mgh — already work         ~100%             │
│  GEOTHERMAL   (T_reservoir)   1 - T₀/T_res              ~15-30%          │
│  WIND     (kinetic, ½ρAv³)   Betz limit: 59.3%          ~59% of KE      │
└────────────────────────────────────────────────────────────────────────────┘
        │
        │  ① Extraction / harvesting losses
        │     mining energy, drilling, refining parasitic loads
        │     solar: reflection, sub-bandgap photons, thermalization
        │     EXERGY DESTROYED: 2-15%
        ▼
┌────────────────────────────────────────────────────────────────────────────┐
│  CONVERSION — where the Carnot tax is collected                            │
│                                                                            │
│  Heat engines (coal, gas, nuclear)                                         │
│    η_Carnot = 1 - T_cold/T_hot     ← the ceiling nobody escapes          │
│    η_actual = η_Carnot × η_internal (friction, mixing, finite ΔT)        │
│                                                                            │
│  Electrochemical (fuel cell, battery)                                      │
│    η = ΔG/ΔH = 1 - TΔS/ΔH         ← Carnot does NOT apply              │
│    direct chemical→electrical; no thermal bottleneck                       │
│                                                                            │
│  Photovoltaic (solar PV)                                                   │
│    η_SQ = 33.7% (single junction)  ← Shockley-Queisser limit            │
│    thermalization + sub-bandgap = main exergy destruction                  │
│                                                                            │
│  Turbomachinery (wind, hydro)                                              │
│    η_turbine = 85-95% of available KE/PE                                   │
│    Betz limit (wind): 16/27 of kinetic energy flux                       │
│  ─────────────────────────────────────────────────────────────────────── │
│  EXERGY DESTROYED: 40-70% (thermal), 5-15% (direct conversion)          │
└────────────────────────────────────────────────────────────────────────────┘
        │
        │  ② Transmission / distribution
        │     electrical: I²R losses in lines + transformers (5-8%)
        │     fuel transport: pipeline compression, tanker fuel
        │     EXERGY DESTROYED: 3-8%
        ▼
┌────────────────────────────────────────────────────────────────────────────┐
│  FINAL ENERGY — what arrives at the meter/nozzle                           │
│  ~400 EJ/yr globally (~67% of primary)                                     │
│                                                                            │
│  Electricity  ~20%    Heat  ~50%    Transport fuel  ~28%    Other  ~2%   │
└────────────────────────────────────────────────────────────────────────────┘
        │
        │  ③ End-use conversion
        │     ICE drivetrain: 20% of fuel → motion (80% waste heat)
        │     Electric motor: 90-95% of electricity → shaft work
        │     Heat pump: COP 3 → 300% of electricity → useful heat
        │     Gas furnace: 90% of fuel → heat (but fuel exergy >> heat exergy)
        │     EXERGY DESTROYED: 20-80% depending on end use
        ▼
┌────────────────────────────────────────────────────────────────────────────┐
│  USEFUL ENERGY SERVICES — motion, warmth, light, computation               │
│  ~200 EJ/yr globally (~35% of primary energy)                              │
│                                                                            │
│  THE REST IS WASTE HEAT → radiated to the 2.7 K cosmic background        │
│  Entropy has increased. The universe has aged. The Alchemist's tax is paid.│
└────────────────────────────────────────────────────────────────────────────┘
```

**The single most important number in energy:** ~65% of primary energy is destroyed as waste
heat before it does anything useful. That destruction is not engineering failure — most of it
is thermodynamic *inevitability*. The Alchemist's craft is distinguishing the inevitable
from the merely conventional.

---

## Three Directories, One Exergy Story

This volume contains three directories. They are not peers — they are layers of a single
transformation chain.

```
┌──────────────────────────────────────────────────────────────────────┐
│  chemical-eng/         THE FEEDSTOCK TRANSFORMER                     │
│                                                                      │
│  Transforms raw materials into products at scale.                    │
│  Exergy lens: Gibbs free energy of mixing and reaction.              │
│  Destroys exergy via: finite-rate heat/mass transfer, mixing,        │
│    reaction irreversibility, separation work (distillation,          │
│    membranes — always costs more than the reversible minimum).       │
│  Key ratio: actual separation work / minimum reversible work         │
│    (thermodynamic efficiency of separation ≈ 5-20% for distillation) │
├──────────────────────────────────────────────────────────────────────┤
│  nuclear/              THE FISSION TRANSFORMER                       │
│                                                                      │
│  Transforms nuclear binding energy into thermal energy.              │
│  Exergy lens: 200 MeV per fission event → radiation → coolant heat  │
│    → Carnot-limited steam cycle. The exergy of fission products      │
│    (high-energy gamma, neutrons) degrades to ~550°C steam — a        │
│    massive voluntary exergy destruction in the name of containment.  │
│  PWR thermal efficiency: ~33%. Not because nuclear is inefficient —  │
│    because T_hot is deliberately kept low for materials/safety.      │
│  Key ratio: 200 MeV fission → 66 MeV electricity → 134 MeV waste   │
├──────────────────────────────────────────────────────────────────────┤
│  energy-systems/       THE INTEGRATION LAYER (this directory)        │
│                                                                      │
│  Connects primary sources to final energy services.                  │
│  Exergy lens: the orchestration of conversion, storage, transport,   │
│    and dispatch. Every storage cycle destroys exergy (round-trip     │
│    efficiency < 100%). Every transmission line dissipates I²R heat.  │
│    Grid dispatch is a real-time optimization: minimize total exergy  │
│    destruction subject to demand, reliability, and cost constraints. │
│  Key ratio: primary energy in / useful energy services out           │
│    (global average: ~35%)                                            │
└──────────────────────────────────────────────────────────────────────┘
```

---

## Module Map — This Directory

| Module | Topic | Exergy Angle |
|--------|-------|-------------|
| `01-SOLAR-PV` | Photovoltaic systems | Shockley-Queisser: where photon exergy dies |
| `02-WIND-POWER` | Wind energy | Betz limit: the kinetic energy ceiling |
| `03-ENERGY-STORAGE` | Batteries, pumped hydro, CAES, hydrogen | Round-trip losses: exergy cost of time-shifting |
| `04-HYDROGEN` | H₂ production, transport, end use | Electrolyzer + fuel cell: two conversions, two taxes |
| `05-GRID-INTEGRATION` | Dispatch, frequency, VRE integration | The orchestration problem: reliability vs. waste |
| `06-NUCLEAR-SYSTEMS` | Reactor designs in energy context | Carnot at 550K: the safety-efficiency trade |
| `07-FOSSIL-TRANSITION` | Coal, gas, CCS, phase-out pathways | Stranded assets: exergy of sunk capital |
| `08-THERMAL-CYCLES` | Rankine, Brayton, combined cycle, sCO₂, ORC | Where the Carnot tax is collected: cycle-by-cycle |
| `09-HYDROPOWER` | Turbines, reservoir ops, ROR, pumped storage | Gravity's gift: PE → work with no Carnot limit |
| `10-GRID-DISPATCH` | Merit order, unit commitment, BESS dispatch | Scheduling exergy destruction in real time |

---

## Primary / Secondary / Final — The Energy Cascade

A precise vocabulary. Most energy journalism mangles these distinctions.

```
PRIMARY ENERGY                  SECONDARY ENERGY               FINAL ENERGY
(as extracted from nature)      (after first conversion)       (as delivered to user)
───────────────────────────     ────────────────────────       ──────────────────────
Crude oil                  →    Gasoline, diesel, jet fuel →   Fuel in your tank
Coal                       →    Electricity (power plant)  →   kWh at your meter
Uranium ore                →    Enriched UO₂ → heat → elec →  kWh at your meter
Sunlight on panel          →    DC electricity → AC (inv.)  →  kWh at your meter
Natural gas at wellhead    →    Pipeline gas / LNG          →  Gas at your burner
Biomass (wood, crop)       →    Bioethanol / biogas         →  Fuel or heat

Global totals (2024):
  Primary:     ~600 EJ/yr     (what we extract)
  Secondary:   ~450 EJ/yr     (after refining/conversion)
  Final:       ~400 EJ/yr     (what reaches the door)
  Useful:      ~200 EJ/yr     (actual energy services)

  Missing ~400 EJ = waste heat. That is two-thirds of everything we extract.
```

**Why this matters:** When someone says "nuclear is 5% of primary energy," that
understates nuclear's contribution to useful energy services because nuclear converts
at ~33% while the primary energy of wind/solar is counted at electrical output
(by the IEA's "direct equivalent" method). Accounting methodology changes the narrative.

---

## The Carnot Limit — Why It Matters and Where It Doesn't

The second law sets an absolute ceiling on heat-to-work conversion. Every thermal power
plant lives under this ceiling.

```
η_Carnot = 1 - T_cold / T_hot      (temperatures in Kelvin)

TECHNOLOGY          T_HOT      T_COLD    η_CARNOT    η_ACTUAL    GAP
────────────────────────────────────────────────────────────────────────
Coal subcritical    810 K      310 K      61.7%       33-36%     ~28%
Coal supercritical  870 K      310 K      64.4%       40-42%     ~23%
CCGT (gas turbine)  1600 K     310 K      80.6%       58-63%     ~19%
Nuclear PWR         590 K      310 K      47.5%       32-34%     ~14%
Nuclear HTGR        1200 K     310 K      74.2%       45-48%     ~27%
Geothermal          420 K      310 K      26.2%       10-15%     ~13%
Ocean thermal       298 K      278 K       6.7%        3-4%      ~3%
────────────────────────────────────────────────────────────────────────

Where Carnot does NOT apply:
  Fuel cell:    η = ΔG/ΔH (can exceed Carnot for same temperatures)
  Solar PV:     photon → electron-hole pair (quantum, not thermal)
  Wind turbine: kinetic energy → shaft work (Betz limit, not Carnot)
  Heat pump:    COP = T_hot/(T_hot - T_cold) — the Carnot cycle in reverse

The "gap" column is where the Alchemist earns a living: finite-ΔT heat
transfer, turbine blade friction, generator losses, auxiliaries, condenser
approach temperature. Every percentage point recovered is real money.
```

**The nuclear paradox:** Fission releases energy at ~10⁹ K equivalent (MeV-scale gamma),
but PWR steam exits at ~590 K. That voluntary degradation from 10⁹ → 590 K destroys
enormous exergy — the price paid for zirconium cladding integrity and pressure-vessel
metallurgy. Gen IV reactors (HTGR, molten salt) push T_hot higher, recovering some of
that squandered potential.

---

## Key Numbers — Thermal Efficiencies, LCOE, Capacity Factors

### Conversion Efficiencies

| Technology | Thermal / System Efficiency | Why |
|------------|---------------------------|-----|
| Coal subcritical | 33-36% | T_hot limited by steam pressure (~540°C) |
| Coal supercritical | 40-42% | Higher steam parameters (600°C, 250+ bar) |
| Coal ultra-supercritical | 44-47% | 700°C+ steam; materials at the edge |
| CCGT (combined cycle gas) | 58-63% | Gas turbine (Brayton) + steam bottoming (Rankine) |
| OCGT (open cycle gas) | 35-42% | Peaker duty; no heat recovery |
| Nuclear PWR/BWR | 32-34% | T_hot deliberately low (~320°C steam) |
| Nuclear HTGR (Gen IV) | 45-48% | Helium at 750-950°C → higher Carnot ceiling |
| Solar PV (module) | 20-23% | Shockley-Queisser: thermalization + sub-bandgap |
| Solar PV (system, AC) | 17-20% | Inverter, wiring, soiling, temperature derating |
| Wind turbine (rotor) | 35-48% of KE | Betz limit is 59.3%; best rotors reach ~80% of Betz |
| Fuel cell (PEM, H₂) | 50-60% (LHV) | Electrochemical: no Carnot limit |
| Fuel cell (SOFC) | 55-65% (LHV) | Higher T → better kinetics, CHP potential |
| Electrolysis (PEM) | 60-70% (LHV) | Overpotential losses at electrodes |
| Battery round-trip | 85-92% (Li-ion) | Ohmic, activation, concentration losses |
| Pumped hydro round-trip | 75-82% | Turbine + pump + friction + evaporation |
| Heat pump COP | 2.5-4.5 | Not an "efficiency" — moves heat, doesn't create it |

### Capacity Factors (actual output / nameplate maximum)

```
TECHNOLOGY               TYPICAL CF      ANNUAL OUTPUT PER GW INSTALLED
──────────────────────────────────────────────────────────────────────────
Nuclear                  90-95%          7,900 - 8,300 GWh/yr
Coal (baseload)          70-85%          6,100 - 7,400 GWh/yr
CCGT                     40-60%          3,500 - 5,300 GWh/yr
Offshore wind            40-55%          3,500 - 4,800 GWh/yr
Onshore wind             25-40%          2,200 - 3,500 GWh/yr
Utility solar PV         15-30%          1,300 - 2,600 GWh/yr
Rooftop solar PV         10-18%            880 - 1,600 GWh/yr
Hydro (run-of-river)     30-50%          2,600 - 4,400 GWh/yr

  "China added 200 GW of solar in 2023" → at 15% CF that is ~263 TWh/yr
  ≈ equivalent to ~30 GW nuclear at 90% CF (237 TWh/yr).
  Capacity without capacity factor is a meaningless headline.
```

### LCOE Ranges (2024, global average, utility scale)

| Technology | LCOE ($/MWh) | Dispatchable? | Notes |
|------------|-------------|---------------|-------|
| Onshore wind | 25-50 | No | Best sites < $30 |
| Utility solar PV | 30-55 | No | Steepest cost decline in history |
| Large hydro | 25-90 | Yes (reservoir) | Site-dependent; very long-lived |
| CCGT | 45-75 | Yes | Fuel-price sensitive |
| Offshore wind (fixed) | 70-120 | No | Declining; higher CF partly compensates |
| Nuclear (new build, OECD) | 100-200 | Yes | Vogtle: ~$180/MWh all-in |
| Nuclear (existing fleet) | 25-40 | Yes | Very low marginal cost |
| Coal (new build) | 65-150 | Yes | Economically uncompetitive in most markets |
| Battery storage (4h Li-ion) | LCOS: 100-200 | Enables VRE | Declining ~15%/yr |

**Why LCOE is necessary but insufficient:** LCOE measures cost per MWh at the generator
fence. It ignores when that MWh is produced, whether the grid can absorb it, and what
backup capacity must exist for when it is absent. For variable renewables, system LCOE
(generator + integration + backup + storage) is the honest metric. The gap between
generator LCOE and system LCOE grows with penetration — the cannibalization problem.

---

## Dispatchable vs. Intermittent — The Grid's Central Tension

```
DISPATCHABLE                              VARIABLE / INTERMITTENT
(produces on demand)                      (produces when nature allows)
─────────────────                         ──────────────────────────────
Coal, gas, nuclear, hydro (reservoir),    Solar PV, onshore/offshore wind,
biomass, geothermal                       run-of-river hydro

Operator says: "give me 500 MW at 3pm"    Output depends on: sun, wind, rain
Plant responds: ramp to 500 MW            Grid operator must: forecast, store,
                                            curtail, or find backup

The grid equation (every second):
  Generation = Demand + Losses
  If generation > demand → frequency rises (>50/60 Hz) → curtail or store
  If generation < demand → frequency drops (<50/60 Hz) → shed load or start peakers

Mismatch tolerance: ±0.5 Hz before equipment damage
Response time budget: primary response <10s, secondary <30s, tertiary <15min

At low VRE penetration (<20%):  fossil/nuclear fleet handles variability easily
At medium (20-40%):             need flexible gas + some storage + better forecasting
At high (40-60%):               need significant storage + grid interconnection
At very high (60-80%+):         need seasonal storage + sector coupling + overbuild
```

**The duck curve:** In high-solar grids (California, Australia), net demand (demand minus
solar) dips at midday and ramps steeply at sunset. The curve looks like a duck. The belly
is curtailment risk; the neck is the ramp rate that gas plants or storage must meet.
This is not a California curiosity — it is the structural challenge of any solar-heavy grid.

---

## Energy Storage — The Exergy Cost of Time-Shifting

Storage does not create energy. It borrows energy from one moment and returns less of it
later. The round-trip efficiency is the Alchemist's overhead for the service of dispatchability.

```
STORAGE TECHNOLOGY       ROUND-TRIP η   ENERGY DENSITY   DURATION    SCALE
──────────────────────────────────────────────────────────────────────────────
Li-ion (NMC/LFP)        85-92%         200-700 Wh/L     1-4 hours   MW-GW
Pumped hydro (PHS)       75-82%         0.3 Wh/L (res.)  6-24 hours  GW
Compressed air (CAES)    50-70%         3-6 Wh/L (cav.)  4-24 hours  100MW-GW
Flow batteries (VRFB)    65-75%         20-35 Wh/L       4-12 hours  MW-100MW
Hydrogen (P2G2P)         30-42%         700 Wh/L @700bar seasonal    GW
Thermal (molten salt)    40-50% (→elec) 200-300 kWh/m³   6-12 hours  100MW
Gravity (tower/mine)     80-85%         low               4-8 hours   MW-GW
Flywheel                 85-95%         high, low cap.    seconds-min MW

THE STORAGE HIERARCHY (by response time):
  Flywheels / supercaps        → frequency regulation (seconds)
  Li-ion batteries             → peak shifting (hours)
  Pumped hydro / CAES          → daily load balancing (hours-day)
  Hydrogen / ammonia           → seasonal storage (weeks-months)
  No single technology covers all timescales. The portfolio is the answer.
```

**The hydrogen round-trip problem:** Electrolysis (70%) × compression/liquefaction (85%)
× fuel cell (55%) = ~33% round-trip. You put in 3 MWh of electricity and get back 1 MWh.
That is brutal — but for seasonal storage (storing summer solar for winter heating), the
alternative is curtailment (0% recovery), so 33% beats zero.

---

## Sector Coupling — Where the Boundaries Dissolve

Traditionally, electricity, heat, and transport are separate silos with separate fuels and
separate infrastructure. Decarbonization forces them to merge.

```
                    ELECTRICITY GRID
                   ╱       │        ╲
                  ╱        │         ╲
    ┌────────────┐  ┌──────────┐  ┌──────────────┐
    │  TRANSPORT │  │  HEAT    │  │  INDUSTRY    │
    │            │  │          │  │              │
    │  EVs       │  │  Heat    │  │  Electric    │
    │  ←elec     │  │  pumps   │  │  arc furnace │
    │            │  │  ←elec   │  │  ←elec       │
    │  H₂ trucks │  │          │  │              │
    │  ←elec→H₂  │  │  District│  │  Green H₂    │
    │            │  │  heat    │  │  ←elec→H₂    │
    │  E-fuels   │  │  ←waste  │  │              │
    │  ←elec→H₂  │  │   heat  │  │  E-fuels      │
    │   →synfuel │  │          │  │  ←elec→H₂→NH₃│
    └────────────┘  └──────────┘  └──────────────┘

SECTOR COUPLING MECHANISMS:
  Power-to-Heat (P2H):     Heat pumps, resistive heating, industrial electric boilers
  Power-to-Gas (P2G):      Electrolysis → H₂; optionally + CO₂ → synthetic methane
  Power-to-Liquid (P2L):   H₂ + CO₂ → Fischer-Tropsch → synthetic jet fuel / diesel
  Vehicle-to-Grid (V2G):   EV batteries as distributed storage (discharge to grid)
  Combined Heat & Power:   Gas turbine/fuel cell waste heat → district heating

WHY IT MATTERS:
  Electricity is ~20% of final energy today; must reach ~50% by 2050 (IEA NZE).
  The other 80% — industrial heat, transport fuel, building heat — currently runs
  on direct combustion. Electrification + hydrogen covers most of it. The sectors
  that resist electrification (aviation, cement, steel) need hydrogen or CCS.
```

---

## Decarbonization Pathways — The Wedge Analysis

```
GLOBAL CO₂ EMISSIONS: ~37 Gt/yr (2024)
TARGET (IEA NZE 2050): net zero

THE REDUCTION WEDGES:
┌──────────────────────────────────────────────────────────────────────┐
│  Electricity decarbonization         (~40% of the job)               │
│    Solar + wind build-out: 2,400 GW/yr by 2030 (vs ~500 GW 2023)  │
│    Nuclear fleet: maintain + extend + new SMRs                       │
│    Coal phase-out: advanced economies by 2030, global by 2040      │
│    CCS on remaining fossil: 5-10 GtCO₂/yr capture capacity         │
├──────────────────────────────────────────────────────────────────────┤
│  Transport electrification           (~20% of the job)              │
│    Passenger EVs: 60% of sales by 2030, ~100% by 2040              │
│    Trucking: BEV for short/medium; H₂ fuel cell for long-haul      │
│    Aviation: SAF 50% by 2035; e-fuels for remainder                │
│    Shipping: ammonia, methanol, LNG (bridge fuel)                  │
├──────────────────────────────────────────────────────────────────────┤
│  Building heat electrification       (~15% of the job)               │
│    Heat pumps replace gas/oil boilers (COP 3-4 = 300-400%)         │
│    District heating from waste heat / large heat pumps               │
│    Building envelope: insulation, triple glazing                     │
├──────────────────────────────────────────────────────────────────────┤
│  Industrial decarbonization          (~20% of the job)              │
│    Steel: DRI with green H₂ replaces blast furnace coke            │
│    Cement: CCS on process emissions (CaCO₃ → CaO + CO₂ = chemistry)│
│    Chemicals: green H₂ for ammonia (Haber-Bosch); electrification  │
│    Low-temp heat: industrial heat pumps (<200°C)                    │
├──────────────────────────────────────────────────────────────────────┤
│  Negative emissions                  (~5% of the job, post-2040)     │
│    DAC (direct air capture): 1-5 GtCO₂/yr by 2050                  │
│    BECCS (biomass energy + CCS)                                      │
│    Afforestation / soil carbon                                       │
│    Cost: $100-600/tCO₂ for DAC (declining)                           │
└──────────────────────────────────────────────────────────────────────┘

CARBON BUDGET (IPCC AR6):
  1.5°C (50% prob):  ~250 GtCO₂ remaining → exhausted ~2031 at current pace
  2.0°C (50% prob): ~1,150 GtCO₂ remaining → exhausted ~2055 at current pace
```

---

## The Efficiency Argument for Electrification

This is not ideology. It is the second law applied to end-use conversion.

```
HEATING: Gas Furnace vs Heat Pump
─────────────────────────────────────────────────────────────────
  Gas furnace:   1 GJ gas → 0.90 GJ heat        (η = 90%)
  Heat pump:     1 GJ elec → 3.0 GJ heat         (COP = 3.0)

  Even if electricity comes from a 50%-efficient gas plant:
    0.50 (plant η) × 3.0 (COP) = 1.50 GJ heat per GJ gas
    vs 0.90 GJ heat per GJ gas from direct combustion
    → Heat pump path delivers 67% more useful heat per unit of fuel.

TRANSPORT: ICE vs Electric Drivetrain
─────────────────────────────────────────────────────────────────
  ICE:    1 GJ gasoline → 0.20 GJ motion + 0.80 GJ waste heat
  EV:     1 GJ elec     → 0.85 GJ motion + 0.15 GJ waste heat

  Tank-to-wheel ratio: 4.25× (EV uses 4.25× less energy per km)

COOKING: Gas Burner vs Induction
─────────────────────────────────────────────────────────────────
  Gas burner:    ~40% of fuel energy reaches the pot
  Induction:     ~85% of electricity reaches the pot
  Ratio: 2.1× in favor of induction
```

The thermodynamic case is unambiguous. The implementation case — grid capacity, peak demand,
retrofit cost, cold-climate heat pump performance — is where the engineering happens.

---

## Energy Units — The Rosetta Stone

```
┌──────────────────────────────────────────────────────────────────────┐
│  1 EJ  = 10¹⁸ J = 277.8 TWh = 23.88 Mtoe = 0.948 quad             │
│  1 TWh = 3.6 PJ = 0.0860 Mtoe = 3.41 TBtu                         │
│  1 Mtoe = 41.87 PJ = 11.63 TWh                                       │
│  1 kWh = 3.6 MJ = 3,412 BTU                                          │
│  1 quad = 1.055 EJ (used in US EIA reports)                          │
│                                                                      │
│  Who uses what:                                                      │
│    IEA / IPCC:        EJ, Mtoe                                       │
│    Power sector:      TWh (energy), GW (capacity), GWh (storage)     │
│    US EIA, Congress:  quads, BTU                                     │
│    Utility bills:     kWh                                            │
│    Industrial heat:   GJ, MMBtu                                      │
│    Physics papers:    J, eV                                          │
└──────────────────────────────────────────────────────────────────────┘

ANCHOR NUMBERS (2024):
  Global primary energy:           ~600 EJ/yr (~167,000 TWh)
  Global electricity generation:   ~30,000 TWh/yr (~108 EJ)
  Electricity as % of final:       ~20%
  USA primary energy:              ~100 EJ/yr (~95 quads)
  1 GW nuclear @ 90% CF:          ~7.9 TWh/yr
  1 GW solar @ 20% CF:            ~1.75 TWh/yr
```

---

## Energy Density — Why Storage and Transport Substitution Are Hard

```
GRAVIMETRIC (MJ/kg)                     VOLUMETRIC (MJ/L)
───────────────────────                 ──────────────────────
Uranium-235        80,000,000           Diesel               37
Hydrogen (LHV)           120           Gasoline              34
Natural gas               55           LNG                   23
Gasoline                  44           Liquid H₂ (-253°C)    10
Diesel                    43           H₂ at 700 bar          5
Coal (bituminous)         25           Li-ion NMC (cell)     2.5
Wood (dry)                18           Li-ion LFP (cell)     1.5
Li-ion NMC (cell)        0.7           Lead-acid             0.36
Li-ion LFP (cell)        0.5
Lead-acid                0.14
Pumped hydro (100m)      0.001

THE GAP: Gasoline holds ~60× more energy per kg than the best Li-ion cell.
  → Long-haul aviation: battery-electric not viable for decades
  → Long-haul trucking: marginal (BEV for some routes, H₂ for others)
  → Passenger cars: BEV works (range anxiety is psychological)
  → Grid storage (4h): Li-ion works well at current cost curves
  → Seasonal storage: requires chemistry (H₂) or geography (pumped hydro)
```

---

## Global Energy Mix — Where We Are

```
PRIMARY ENERGY BY SOURCE (2024, ~600 EJ):
  Oil          ~31%     Coal         ~25%     Natural gas  ~23%
  Hydro         ~7%     Nuclear       ~5%     Wind          ~4%
  Solar         ~4%     Biomass/other ~2%

  Fossil total: ~79%. Down from ~85% a decade ago. Declining, but slowly.

ELECTRICITY GENERATION BY SOURCE (2024, ~30,000 TWh):
  Coal         ~34%     Gas          ~22%     Hydro        ~15%
  Nuclear      ~10%     Wind          ~8%     Solar         ~6%
  Other RE      ~5%

  Low-carbon electricity: ~39% (nuclear + hydro + wind + solar + other RE)
  Fossil electricity:     ~56%
  Other:                   ~5%

IEA NZE 2050 ELECTRICITY TARGET:
  ~90,000 TWh (3× today). ~90% low-carbon. Electricity = ~50% of final energy.
  Tripling driven by: EV charging + heat pumps + green H₂ electrolysis + industry.
```

---

## Bridges — Energy Systems to Computing

| Energy Systems Concept | Computing / Distributed Systems Parallel |
|----------------------|------------------------------------------|
| Grid frequency regulation (50/60 Hz ± 0.5 Hz) | Distributed consensus: all nodes must agree on a shared clock within tight tolerance |
| Energy dispatch (merit order, unit commitment) | Job scheduling (priority queue, bin packing, cost minimization) |
| Capacity factor (actual output / nameplate) | System utilization (actual throughput / peak capacity); same ratio, same misleading headlines |
| LCOE (levelized cost of energy) | TCO (total cost of ownership): amortize capital + ops over lifetime output |
| Baseload vs peaker plants | Always-on services vs autoscaled burst instances |
| Duck curve (solar midday surplus → evening ramp) | Diurnal traffic pattern: low overnight, spike at business hours, autoscaler lag |
| Curtailment (wasted renewable output) | Request shedding / load shedding under excess supply/demand mismatch |
| N-1 contingency (grid survives any single failure) | N+1 redundancy (system survives any single node failure) |
| Spinning reserve (generators idling, ready to ramp) | Hot standby (instances warmed up, ready to serve) |
| Storage round-trip efficiency | Cache hit rate: the overhead of the indirection layer |
| Transmission losses (I²R) | Network latency and serialization overhead |
| Sector coupling (electricity ↔ heat ↔ transport) | Platform integration (breaking silos between services) |
| Renewable energy certificate (REC) | Offset accounting: the delta between "we paid for it" and "we actually used it" |

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| Convert EJ → TWh? | × 277.8 |
| Global primary energy? | ~600 EJ/yr (~167,000 TWh) |
| Global electricity? | ~30,000 TWh/yr |
| Electricity as % of final energy? | ~20% (heading to ~50% by 2050 in NZE) |
| Cheapest new generation (2024)? | Onshore wind / utility solar: $25-55/MWh |
| Most efficient thermal plant? | CCGT: 58-63% (Brayton + Rankine combined) |
| Nuclear efficiency and why? | 32-34%; T_hot deliberately limited by materials/safety |
| Why electrify heating? | Heat pump COP 3 beats 90% gas furnace even with 50% gas-plant electricity |
| LCOE's fatal weakness? | Ignores dispatchability, integration cost, value deflation |
| Carbon budget for 1.5°C? | ~250 GtCO₂ remaining (~6-7 years at current pace) |
| Why hydrogen round-trip is awful? | Electrolyze (70%) × compress (85%) × fuel cell (55%) ≈ 33% |
| When is hydrogen justified? | Seasonal storage, aviation/shipping fuel, steel DRI, ammonia |
| NZE 2050 electricity volume? | ~90,000 TWh (3× today) |
| Best storage for 4 hours? | Li-ion (LFP for cost, NMC for density) |
| Best storage for seasonal? | Hydrogen (33% RT loss beats 0% from curtailment) |
| Capacity factor of 1 GW solar? | 15-30% → 1,300-2,600 GWh/yr (vs 7,900 for nuclear) |

---

## Common Confusion Points

**Primary energy accounting inflates fossil and deflates renewables.** The "substitution
method" (BP/EI) counts nuclear and renewables by the fossil fuel they would replace,
inflating their primary energy contribution. The "direct equivalent" method (IEA) counts
electricity at face value. Both are conventions, not physics. Compare final energy or
useful energy for honest technology comparison.

**Capacity is not generation.** A headline "GW of capacity" without a capacity factor is
useless for comparing technologies. 200 GW of solar (15% CF) produces roughly the same
annual energy as 30 GW of nuclear (90% CF). Always multiply by 8,760 hours × CF.

**LCOE of solar < LCOE of gas, but gas still gets built.** LCOE ignores dispatchability.
A gas plant that produces on demand has higher value to the grid than solar at the same
LCOE. The honest comparison is solar + storage vs gas, and at high VRE penetration the
system LCOE includes integration costs that generator LCOE hides.

**"100% renewable electricity" is not "100% renewable energy."** Electricity is ~20% of
final energy. The other 80% — industrial heat, transport, building heating — mostly runs
on direct combustion. Decarbonizing the full energy system requires electrification of
end uses, not just clean generation.

**Efficiency ≠ exergy efficiency.** A gas furnace at 90% thermal efficiency sounds
impressive. But the exergy of natural gas (~1,000°C flame) used to produce 40°C room heat
is a thermodynamic travesty — you are using high-quality work potential to produce low-grade
warmth. A heat pump at COP 3 does the same job with one-third the exergy input. First-law
efficiency deceives; second-law (exergy) efficiency reveals.

**The hydrogen economy hype ignores round-trip losses.** Electrolysis → compression →
fuel cell delivers ~33% of input electricity. That makes green hydrogen a terrible
electricity storage medium. It is justified only where: (a) direct electrification is
impossible (steel, shipping, aviation), or (b) the alternative is curtailing renewable
output that has zero other use.

**Net zero ≠ zero emissions.** Net zero allows residual emissions (cement process CO₂,
long-haul aviation) offset by negative emissions (DAC, BECCS, forestry). Carbon neutral
often means purchasing offsets without reducing emissions — high greenwashing risk.
Microsoft's target is carbon negative by 2030: removals > emissions.

---

## Decision Guide

```
WHAT ENERGY SYSTEMS QUESTION?
        │
        ├── How does solar/wind convert energy and what limits efficiency?
        │   └──► 01-SOLAR-PV / 02-WIND-POWER
        │
        ├── How do we store energy and what does each cycle cost in exergy?
        │   └──► 03-ENERGY-STORAGE
        │
        ├── When does hydrogen make sense vs direct electrification?
        │   └──► 04-HYDROGEN
        │
        ├── How does the grid balance supply/demand in real time?
        │   └──► 05-GRID-INTEGRATION
        │
        ├── How do nuclear reactors fit into the energy system?
        │   └──► 06-NUCLEAR-SYSTEMS (+ nuclear/ directory for reactor physics)
        │
        ├── How do fossil plants transition and what replaces them?
        │   └──► 07-FOSSIL-TRANSITION
        │
        ├── How do thermal power cycles work and where does exergy die?
        │   └──► 08-THERMAL-CYCLES (Rankine, Brayton, CCGT, sCO₂, ORC)
        │
        ├── How does hydropower work and which turbine for which site?
        │   └──► 09-HYDROPOWER (Pelton, Francis, Kaplan, reservoir ops)
        │
        ├── How does the grid dispatch generators and storage in real time?
        │   └──► 10-GRID-DISPATCH (merit order, unit commitment, BESS ops)
        │
        ├── How do chemical processes transform feedstock at scale?
        │   └──► chemical-eng/ directory (reaction, separation, transport)
        │
        └── What is the physics of fission and reactor design?
            └──► nuclear/ directory (neutronics, thermal hydraulics, safety)
```
