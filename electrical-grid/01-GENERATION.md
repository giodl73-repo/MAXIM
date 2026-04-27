# Electrical Grid — Generation
## Thermal Power, Nuclear, Hydro: Converting Energy Into Electrons

---

## The Big Picture: Generation Technologies

```
HEAT SOURCE              MECHANICAL CONVERSION         ELECTRICAL CONVERSION
──────────────────────────────────────────────────────────────────────────────
Coal/Gas/Nuclear  ──▶  Steam turbine (Rankine cycle) ──▶  Synchronous generator
                        or Gas turbine (Brayton cycle)
                        or Combined cycle (both)

Hydro             ──▶  Water turbine (Pelton/Francis/Kaplan) ──▶  Generator

Wind              ──▶  Wind turbine rotor  ──▶  DFIG or fully-rated converter
(not thermal)           (Betz-limited)

Solar PV          ──▶  No moving parts — photovoltaic effect → DC → inverter
(not thermal)

Every thermal plant is a heat engine: Q_in → W_out + Q_rejected
The Carnot limit applies: η_max = 1 - T_cold/T_hot (absolute temperatures)
Modern plants fight hard to raise T_hot and lower T_cold to approach this limit.
```

---

## Thermal Cycle Fundamentals

### The Rankine Cycle (Steam Plants: Coal, Nuclear, Some Gas)

```
         HIGH PRESSURE/TEMP STEAM
              │
              ▼
    ┌────────────────────┐
    │   Steam Turbine    │
    │  (expands steam,   │
    │   extracts work)   │
    └──────────┬─────────┘
               │  ──▶ Generator (rotor at 3600 or 1800 RPM)
               │ Low-pressure exhaust steam
               ▼
    ┌────────────────────┐
    │    Condenser       │
    │  (condenses steam  │
    │   to liquid water) │
    └──────────┬─────────┘
               │  ◀── Cooling water (river, lake, cooling tower)
               │ Liquid water
               ▼
    ┌────────────────────┐
    │  Feedwater Pump    │
    │  (small work input │
    │   to raise pres.)  │
    └──────────┬─────────┘
               │ High-pressure liquid
               ▼
    ┌────────────────────┐
    │  Boiler/Steam      │
    │  Generator         │
    └──────────┬─────────┘
               │  ◀── Heat input Q_in (coal, nuclear, gas, solar)
               │
               (cycle repeats — back to top)

η_Rankine = W_net / Q_in = (W_turbine - W_pump) / Q_in
```

**The Carnot upper bound:**
- η_Carnot = 1 - T_cold/T_hot (temperatures in Kelvin)
- For 600°C steam (873K) with 30°C condensing (303K):
  η_Carnot = 1 - 303/873 = 65.3%
- Real plants achieve ~42-46% (inefficiencies: turbine isentropic losses, pump work, heat losses, auxiliary loads)

### Coal Plant Efficiency Progression

| Technology | Steam Conditions | Efficiency | Status |
|-----------|-----------------|-----------|--------|
| Subcritical | 540°C / 170 bar | 33–37% | Legacy fleet; being retired |
| Supercritical | 580°C / 250 bar | 38–42% | Most 1990s-2010s builds |
| Ultra-supercritical (USC) | 600°C / 300 bar | 42–46% | Modern new builds (China) |
| Advanced USC (A-USC) | 700°C / 350 bar | 46–50% | Nickel alloy requirements; limited commercial deployment |

**Why efficiency matters:** A 10% improvement in thermal efficiency means 10% less fuel burned for the same electricity. For a 1,000 MW coal plant running at 80% CF, that's 6.5 million fewer tons of coal over a 40-year life — and corresponding reductions in CO₂, SO₂, NOₓ, and particulates.

---

## Natural Gas Generation: Three Technologies

### 1. Combined-Cycle Gas Turbine (CCGT)

The dominant new natural gas technology since the 1990s. Combines Brayton cycle (gas turbine) + Rankine cycle (steam turbine) in series, using waste heat from the gas turbine to generate steam.

```
CCGT CONFIGURATION:

  Compressed air + natural gas ──▶ Combustion chamber
                                          │
                                          ▼
                                  ┌─────────────┐
                                  │ Gas Turbine │
                                  │ (Brayton)   │
                                  └──────┬──────┘
                                         │  ──▶ Generator 1 (≈35-40% of output)
                                         │ Exhaust gas ~600°C
                                         ▼
                                  ┌─────────────┐
                                  │    HRSG     │
                                  │ (boiler in  │
                                  │  exhaust    │
                                  │  duct)      │
                                  └──────┬──────┘
                                         │ High-pressure steam
                                         ▼
                                  ┌─────────────┐
                                  │   Steam     │
                                  │  Turbine    │
                                  │  (Rankine)  │
                                  └──────┬──────┘
                                         │  ──▶ Generator 2 (≈20-25% of output)
                                         │ Condensed water → back to HRSG

  HRSG: Heat Recovery Steam Generator — extracts heat from exhaust to make steam

Total efficiency ≈ 58–62%  (sum of both cycles, minus losses)
Best-in-class (GE 9HA, Siemens SGT5-9000HL): 63-64% LHV efficiency
```

**Why CCGT dominates new gas builds:** The incremental cost of the steam bottoming cycle (HRSG + steam turbine + condenser) adds ~20-25% to capital cost but recovers ~40-50% of the fuel cost wasted as heat in a simple-cycle unit. The economics are compelling at any scale > ~300 MW. Smaller units (<100 MW) often remain simple-cycle because the steam section payback period is too long.

**CCGT startup times:**
- Cold start (>72h shutdown): 4-6 hours (must heat up steam cycle slowly to avoid thermal stress)
- Warm start (8-72h shutdown): 2-3 hours
- Hot start (<8h shutdown): 60-90 minutes
- This limits CCGT ability to serve very short-duration peaks — you need to start it before you need it.

### 2. Simple-Cycle Gas Turbine (Combustion Turbine / Peaker)

Pure Brayton cycle — no steam recovery. Lower efficiency but fast start.

```
  Air intake ──▶ Compressor ──▶ Combustion Chamber ──▶ Turbine ──▶ Generator
                  (raises air pressure         (burns gas,      (expands
                   to ~15-30 atm)               heats air)       hot gas)

Efficiency: 35-42% (exhaust at 550-600°C goes straight to atmosphere — wasted)
Output range: 50 MW to 400+ MW (GE LM6000: 50 MW; GE 7F: 200 MW)
Start time: 10-15 minutes (cold) — this is the key advantage
Fuel cost per MWh: 40-60% higher than CCGT for same gas price
```

**When peakers are used:** 200-400 hours/year (capacity factor ~5-10%). They lose money on energy margins most of the year. Their revenue comes primarily from capacity payments (being available) and ancillary services markets. The economics are: capital cost (~$450/kW vs ~$1,100/kW for CCGT) × very low CF = low total annual fuel cost even at poor efficiency.

### 3. CCGT Heat Rate Comparison

Heat rate = BTU input per kWh electrical output (lower = more efficient):

| Technology | Heat Rate (BTU/kWh) | Efficiency (%) | Note |
|-----------|-------------------|---------------|------|
| Best CCGT (new) | 5,700–6,000 | 57–60% | GE H-class, Siemens HL-class |
| Typical CCGT | 6,100–6,800 | 50–56% | Existing fleet, F-class turbines |
| Simple-cycle CT | 8,500–10,000 | 34–40% | Peakers |
| Subcritical coal | 10,000–11,000 | 31–34% | Old fleet |
| Supercritical coal | 8,900–9,500 | 36–38% | Newer coal |
| Nuclear (PWR) | 10,400–11,000 | 31–33% | Limited by steam conditions |
| Combined heat & power | 4,000–6,000 | 57–85% | Counts recovered heat |

**Heat rate × fuel price = fuel cost per MWh:**
At $4/MMBtu natural gas price: CCGT (6,300 BTU/kWh) → $25.2/MWh fuel cost
At $4/MMBtu: Simple-cycle (9,500 BTU/kWh) → $38/MWh fuel cost
At $2/MMBtu gas: CCGT fuel cost drops to $12.6/MWh → pushes coal off merit order

---

## Nuclear Power: Controlled Fission

### Pressurized Water Reactor (PWR) — ~70% of World Nuclear Fleet

```
PRIMARY LOOP (radioactive):                    SECONDARY LOOP (steam, non-radioactive):

Reactor Pressure Vessel (RPV):
  ┌───────────────────────┐
  │ UO₂ fuel rods         │
  │ Fission: U-235 +      │
  │   neutron →           │
  │   2 fission products  │
  │   + 2-3 neutrons      │
  │   + heat              │
  │ Hot water out / cold  │
  │ coolant return        │
  │ Control rods inserted │
  └───────────┬───────────┘
              │ hot primary water
              ▼
Steam Generator (heat exchanger):
  ┌───────────────────────┐
  │ Primary loop:         │
  │   325°C / 155 bar     │
  │   subcooled water     │
  │ Secondary loop:       │
  │   steam generated     │
  │   (not in contact     │
  │   with primary)       │
  └───────────┬───────────┘
              │ secondary steam
              ▼
Turbine + Generator:
  ┌───────────────────────┐
  │  Steam Turbine        │
  │  → Condenser          │
  │  → Feedwater pump     │
  │  → back to steam gen  │
  └───────────────────────┘
  Steam Turbine ──▶ Generator

Primary loop conditions: 325°C, 155 bar (subcooled — doesn't boil despite temperature
                         because high pressure keeps it liquid)
Secondary steam conditions: ~280°C, ~55 bar
Turbine inlet temperature limited by secondary steam conditions → ~33% thermal efficiency
```

**Why nuclear efficiency is limited to ~33%:** PWR steam conditions are constrained by materials — the zircaloy cladding on fuel rods and the stainless steel reactor vessel can't tolerate the temperatures that coal supercritical plants use. Primary loop must stay below ~350°C to protect fuel integrity. This means secondary steam is cooler than modern coal or gas plants, limiting Rankine cycle efficiency.

**Fuel cycle:**
- Fresh fuel: 3-5% enriched uranium-235 (natural U is 0.7% U-235)
- Zircaloy-clad (zirconium alloy) UO₂ ceramic pellets in 12-14 foot fuel assemblies
- Typical PWR: 193 fuel assemblies, ~80 tonnes UO₂
- Refueling cycle: 18-24 months (most US plants: 18 months)
- Outage duration: 25-40 days (refuel + maintenance)
- Capacity factor contribution: ~92% annual average — the gold standard for reliability

### Boiling Water Reactor (BWR) — ~30% of World Nuclear Fleet

```
BWR (GE/Hitachi design):
Simpler: no separate secondary loop — water boils directly in the reactor vessel
Steam goes directly to turbine (slightly radioactive — requires turbine area shielding)
Lower pressure: ~75 bar (vs 155 bar PWR)
Operating temperature: ~285°C
Efficiency similar to PWR: ~32-34%
Examples: Fukushima Daiichi, many US plants (Dresden, Quad Cities)
```

### Nuclear Capacity Factor — Why 92% Matters

Nuclear's capacity factor advantage over gas (55%) or coal (38%) means:
- 1,000 MW nuclear: 8,059 GWh/yr
- 1,000 MW coal: 3,328 GWh/yr
- 1,000 MW CCGT: 4,818 GWh/yr

Nuclear generates ~2.4× more energy than coal from the same nameplate capacity. This is why nuclear closures are so hard to replace with intermittent renewables on a megawatt-for-megawatt basis.

**Nuclear dispatchability:** Traditional wisdom was "nuclear is inflexible baseload." This is partly policy, partly physics:
- Physically: can load-follow at ~5%/min ramp rate (slower than gas, faster than coal can startup)
- France runs their entire nuclear fleet in load-following mode to manage daily demand variation
- US: typically run nuclear flat for economic reasons (high fixed cost, near-zero marginal cost — most economical to run at 100% always)
- Future: small modular reactors (SMRs) designed with more flexible operations in mind

---

## Hydroelectric Power

### Three Turbine Types (matched to head and flow)

```
HEAD (m)       TYPE            BEST FOR               EXAMPLE
──────────────────────────────────────────────────────────────────────
>200 m         Pelton wheel    High head, low flow     Mountain dams
               (impulse)       (Alps, Rockies)         Hoover Dam (penstock)
                               Jet of water hits       Efficiency: 85-90%
                               buckets on wheel

30–200 m       Francis turbine Medium head/flow       Most large hydro
               (reaction)      Dominant turbine type   Grand Coulee, Three Gorges
                               in the world            Efficiency: 90-95%

<30 m          Kaplan turbine  Low head, high flow    Run-of-river plants
               (propeller)     River dams, tidal       Rhine, Columbia River
                               Adjustable pitch blades Efficiency: 85-92%
```

**Hydroelectric efficiency ~90%:** The highest mechanical-to-electrical conversion efficiency of any generation type. Water's hydraulic energy converts directly to shaft rotation with minimal losses.

P = ρ × g × Q × H × η
Where: ρ = 1,000 kg/m³, g = 9.81 m/s², Q = flow (m³/s), H = head (m), η = efficiency

Grand Coulee Dam: 6,809 MW total installed capacity, head = 98 m, Francis turbines

### Run-of-River vs Reservoir Hydro

```
RUN-OF-RIVER:                          RESERVOIR (STORAGE) HYDRO:
  No significant storage                 Large upstream reservoir
  Must pass whatever flow arrives        Can store water for weeks/months
  Output varies with season              Highly dispatchable
  Can't store for later                  Schedule output to match peak demand
  High CF in wet season                  Capacity factor: 30-60%
  Low CF in dry season                   Grand Coulee: 3-8 GW range dispatch
  Baseload-ish but weather-dependent     Pumped hydro possible (separate facility)
```

**Pumped hydro:** Two reservoirs at different elevations. Pump water up (store energy) using off-peak electricity. Release through turbine-generator during peak (recover energy). This is covered in detail in 06-ENERGY-STORAGE.md — it's the grid's dominant storage technology by installed capacity (93% of world grid storage).

---

## Cogeneration (Combined Heat and Power — CHP)

Instead of rejecting waste heat to a condenser (Rankine cycle inefficiency), cogenerate: extract useful heat from the turbine exhaust for district heating, industrial processes, or building HVAC.

```
CONVENTIONAL POWER PLANT:          COGENERATION:
  Q_in (fuel)                         Q_in (fuel)
    │                                   │
    ▼                                   ▼
  Turbine → W_electrical (~35%)      Turbine → W_electrical (~25-35%)
    │                                   │
    ▼                                   ▼
  Condenser → Q_rejected (~65%)      Heat exchanger → Q_useful (~40-55%)
  (thrown away to cooling water)     (district heating, industrial steam)

Overall electrical efficiency: 33-42%    Overall energy utilization: 75-90%
```

**CHP is everywhere you don't see it:** Hospitals, universities, paper mills, chemical plants, data centers (increasingly). Helsinki heats 90% of the city with district heat from CHP. A natural gas CHP plant in a hospital might generate electricity at 38% efficiency but achieve 85% total energy utilization when the waste heat heats the building.

---

## Generator: Converting Shaft Rotation to AC Power

All thermal (and most hydro) plants use a synchronous generator. This is the device that physically couples to the grid and defines the frequency relationship.

```
SYNCHRONOUS GENERATOR (simplified):

Rotor (rotating):                    Stator (stationary):
  DC electromagnet                     Three-phase AC windings
  fed by excitation                    wound in slots around
  system (from the                     the stator bore
  generator's own AC                   (armature windings)
  output, rectified)

Rotor field rotates at                As rotor field rotates,
mechanical speed (3600 RPM             it induces AC voltage
for 60 Hz, 2-pole machine)            in stator windings
                                       at exactly the rotor
                                       rotation frequency

Frequency = (RPM × poles) / 120
  2-pole at 3600 RPM → 60 Hz
  4-pole at 1800 RPM → 60 Hz  (nuclear plants, some large coal)
  Hydraulic turbines: 10-50 poles, 120-720 RPM
```

**Excitation system:** Controls the rotor field strength → controls reactive power output. An overexcited generator supplies reactive power to the grid (like a capacitor). An underexcited generator absorbs reactive power (like an inductor). Grid voltage control is managed largely by adjusting excitation on large generators.

**Inertia:** The rotor + turbine shaft assembly has enormous angular momentum. A 1,000 MW steam turbine-generator set has ~300 tonnes of rotating mass. This kinetic energy is the "shock absorber" for the grid — it resists instantaneous frequency changes. When generation drops, this spinning mass slows down (giving up kinetic energy → frequency drops), buying time for governor response. This inertia is what inverter-based resources (solar, wind) cannot replicate without special control strategies.

---

## Capacity Factor Deep Dive

```
ANNUAL GENERATION PROFILE BY RESOURCE TYPE:

Nuclear:
  ████████████████████████████████████████ (92% — flat, just planned outages)

CCGT (baseload):
  ████████████████████████████████████████░░░░░░░ (55% — dispatched most of year)

Coal (US 2024):
  ████████████████████████░░░░░░░░░░░░░░░░░░░░░░░ (38% — pushed off by cheap gas/RE)

Wind (good site):
  ████████████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░ (35% — but NOT flat; varies hourly)

Offshore wind:
  █████████████████████████░░░░░░░░░░░░░░░░░░░░░░ (45% — more consistent)

Utility Solar:
  █████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ (25% — ONLY during daylight)

Peaker (gas CT):
  ████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ (8% — only ~700 hours/year)
```

**The dispatchability matrix:**

```
                     CF ACHIEVABLE    RAMP RATE      STARTS IN
Nuclear              90-93%           ~3%/min         Days (not designed for frequent restart)
Geothermal           85%              Limited          Weeks
CCGT                 50-70% (base)    5-10%/min        1-4 hours (hot/warm/cold)
Supercritical coal   40-50%           2-3%/min         4-8 hours
Simple-cycle CT      5-15%            10-15%/min       10-15 minutes
Hydro (reservoir)    30-60%           Very fast         Seconds to minutes (GW in <60s)
Pumped hydro         10-30%           Very fast          30-60 seconds
Battery storage      ~20%             Essentially instant  Milliseconds
```

---

## Levelized Cost of Energy (LCOE)

LCOE = Total lifetime cost (capital + O&M + fuel + decommissioning) / Total lifetime energy (MWh)

**Units:** $/MWh (or cents/kWh). Comparable across technologies.

| Technology | LCOE $/MWh (2024, US) | Key Driver |
|-----------|---------------------|-----------|
| Utility solar PV (new) | $24–45 | Declining capex; site-dependent |
| Onshore wind (new) | $26–50 | Site-dependent; excellent sites $26 |
| Offshore wind (new) | $72–120 | Higher capex; better CF; foundation cost |
| CCGT (new, $3/MMBtu gas) | $40–65 | Fuel cost dominant; capex modest |
| CCGT (new, $6/MMBtu gas) | $65–95 | Gas price sensitivity: large |
| Nuclear (new AP1000) | $80–140 | Massive capex; long construction; high CF |
| Advanced nuclear (SMR) | $80–120 (projected) | Unproven at scale |
| Coal (new, US) | $100–180 | Stranded asset risk + carbon cost |
| Geothermal (existing) | $20–60 | If resource available |
| Pumped hydro (new) | $150–300 | Site-constrained; long life reduces annual |

**LCOE limitations:** Doesn't capture value of dispatchability. A $35/MWh wind plant that generates when it's windy is not equivalent to a $65/MWh CCGT that generates on command. The "system LCOE" or "value-adjusted LCOE" adds integration costs (storage, backup capacity, transmission) to properly compare.

---

## Generator Fleet Economics: Revenue Streams

```
REVENUE STREAMS FOR DIFFERENT GENERATORS:

Nuclear/Baseload:
  Energy payments ($/MWh × high CF) = primary revenue
  Capacity payments (being available) = secondary
  Zero fuel cost volatility
  Fixed O&M ~$15-25/MWh

CCGT (baseload):
  Energy payments: primary, but CF varies with gas price
  When gas prices high → dispatched less → CF drops → less energy revenue
  Ancillary services: some revenue (regulation, spinning reserve)

Peaker (gas CT):
  Energy payments: minimal (very low CF)
  Capacity payments: critical revenue (in markets with capacity markets)
  Ancillary services: fast response → valuable for frequency regulation
  Without capacity market: peakers often uneconomic → reliability risk

Wind/Solar:
  Energy payments: depends on when they generate vs when prices are high
  Production tax credits (PTC): $27/MWh for wind (US, 2024) — critical
  RECs (Renewable Energy Certificates): compliance market
  PPAs (long-term contracts): increasingly primary revenue path
  Cannibalization: more wind/solar → lower prices when wind/solar is generating
```

---

## Decision Cheat Sheet

| Question | Short Answer |
|----------|-------------|
| Why CCGT instead of simple-cycle? | Recovers 40-50% of wasted heat as additional electricity; payback in 5-7 years |
| Why is nuclear thermal efficiency only 33%? | PWR steam conditions constrained by fuel rod materials; can't run 600°C like USC coal |
| What is heat rate? | BTU input per kWh output; lower = better; CCGT ~6,100, nuclear ~10,500, coal ~9,500-11,000 |
| Why are peakers economically viable at 8% CF? | Low capital cost ($450/kW) + capacity payments + ancillary services; not just energy revenue |
| Which turbine for high-head hydro? | Pelton (impulse, >200m head, water jet); Francis (30-200m, most common); Kaplan (low head, propeller) |
| What is the best thermal efficiency available? | CCGT ~63-64% (GE H-class); USC coal ~46%; nuclear ~33% |
| Why does nuclear run at high capacity factor? | Near-zero marginal cost → always cheapest to dispatch; high fixed costs reward max utilization |
| What gives the grid its "inertia"? | Rotating mass (300+ tonnes per 1000 MW unit) of synchronous generator-turbine shafts |
| What is LCOE missing? | Dispatchability value; integration costs; capacity value; system-level costs of variability |

---

## Common Confusion Points

**Heat rate direction:** Lower heat rate = more efficient. This trips up non-engineers who expect "higher is better." 6,000 BTU/kWh (CCGT) beats 10,500 BTU/kWh (nuclear in thermal efficiency) even though the number is smaller.

**Nuclear thermal efficiency vs nuclear energy density:** Nuclear fuel contains ~2 million× more energy per kg than coal. Despite only 33% thermal efficiency, nuclear fuel costs are tiny (~0.5¢/kWh fuel cost vs ~2-3¢/kWh for CCGT). The 33% efficiency is irrelevant to economics — what matters is that the fuel cost is negligible.

**CCGT startup time:** Hot start (< 8h down): 60 minutes. Cold start: 4-6 hours. This matters for dispatch planning. The day-ahead market commits CCGTs in advance precisely because you can't wait until you need them.

**Capacity factor ≠ reliability:** A nuclear plant with 92% CF is very reliable. A wind farm with 35% CF is not unreliable — it generates exactly when the wind blows, predictably. "Reliability" in the grid context means can-you-guarantee-power-when-needed, which is dispatchability + availability.

**Cogeneration efficiency claims:** A CHP system that says "90% efficient" means it uses 90% of the fuel's energy as useful output (electricity + heat). This is not comparable to a power plant's "42% efficiency" which counts only electricity. To compare properly, you'd need to ask: what's the electrical efficiency alone? (Typically 25-35% for CHP, lower than dedicated power plant because the steam cycle is compromised to extract more heat.)

---

*Next: 02-RENEWABLES.md — solar PV physics, wind power curves, grid-forming inverters, integration challenges*
*See also: 05-GRID-STABILITY.md for inertia and frequency dynamics; 06-ENERGY-STORAGE.md for pumped hydro detail*
