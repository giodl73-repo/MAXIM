# Electrical Grid — Renewable Generation
## Solar PV, Wind, and the Grid Integration Challenge

---

## The Big Picture: Renewable Generation Stack

```
SOLAR PV CHAIN:
  Photon in ──▶ p-n junction ──▶ DC current ──▶ Inverter ──▶ AC power ──▶ Grid
  (sunlight)    (semiconductor)   (module output)  (DC→AC)     (synchronized)

WIND CHAIN:
  Wind kinetic energy ──▶ Rotor ──▶ Gearbox ──▶ Generator ──▶ Power electronics ──▶ Grid
  ½ρAv³                  (blades)   (optional)   (DFIG or    (converters,          (transformer)
                                                  PMG)         inverter)

VERSUS THERMAL:
  Fuel → Heat → Steam/Gas → Turbine → Synchronous Generator → Grid
                                       (directly sets frequency and voltage)

KEY DIFFERENCE:
  Thermal: synchronous generator is the grid. It defines voltage magnitude,
           frequency, phase — it IS the grid.
  Renewables (most): inverter interfaces the generation to the grid.
           The inverter follows the grid (usually). Fundamentally different.
```

---

## Solar PV: From Photon to Grid

### The Photovoltaic Effect

A p-n semiconductor junction (typically silicon) absorbs photons. A photon with energy > bandgap (1.1 eV for silicon) promotes an electron from valence to conduction band, leaving a hole. The p-n junction's built-in electric field separates these charge carriers before they recombine — electron flows through external circuit to n-side, hole flows to p-side. This is the photocurrent.

```
SOLAR CELL (simplified cross-section):

Sunlight (photons)
↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
┌───────────────────────────────────┐
│  Anti-reflection coating          │ (silicon nitride, reduces reflection)
│  Metal grid contact (top)         │ (collects electrons)
├───────────────────────────────────┤
│  n-type silicon layer             │ (phosphorus doped, electron-rich)
│  (~0.5 μm)                        │
├ ─ ─ ─ ─ p-n junction ─ ─ ─ ─ ─ ─┤
│  p-type silicon layer             │ (boron doped, hole-rich)
│  (~200 μm)                        │
├───────────────────────────────────┤
│  Metal contact (back)             │
└───────────────────────────────────┘
          │
          ▼ DC current flows in external circuit

Voltage: single silicon cell ≈ 0.5–0.6V at maximum power point
Current: proportional to cell area and irradiance
```

**Cell → Module → Array hierarchy:**
- Cell: ~6 inch × 6 inch silicon wafer, ~4-6W
- Module (panel): 60-96 cells in series/parallel, ~350-700W per panel (2024 standards)
- String: ~20-30 modules in series → ~500-700V DC
- Array: multiple strings, combined at combiner box
- DC output: hundreds of volts to ~1,500V DC (US residential NEC limit; utility: up to 1,500V)
- Inverter: DC → AC at grid frequency and voltage

### Cell Technology Comparison

| Technology | Lab Record | Commercial | Notes |
|-----------|-----------|-----------|-------|
| Monocrystalline Si | 29.4% | 21–23% | Single crystal; most efficient commercial |
| Polycrystalline Si | 23.5% | 17–20% | Cast silicon; lower cost; declining market share |
| CdTe thin-film | 22.1% | 17–19% | First Solar dominates; cadmium telluride; lower temp coefficient |
| CIGS thin-film | 23.4% | 14–17% | Copper indium gallium selenide |
| Perovskite (lab) | 33.9% | Not commercial | Tandem with silicon; stability challenge; rapid research progress |
| Multi-junction (CPV) | 47.1% | 38–42% | Concentrated PV; too expensive except space |
| HJT (heterojunction) | 26.7% | 22–24% | Passivated contacts; low temp coefficient |

**Temperature coefficient matters:** Crystalline silicon efficiency drops ~0.35-0.45%/°C above STC (25°C standard test condition). A rooftop panel on a hot summer day at 60°C operates at 15°C above STC loss = ~6-7% below rated output. CdTe has lower temperature coefficient (~-0.25%/°C) — one reason First Solar panels outperform silicon panels in hot desert climates despite nominally lower efficiency.

### Inverter Topology: String vs Microinverter vs Central

```
UTILITY-SCALE ARRAY TOPOLOGY:

  String architecture (residential/commercial):
  ┌────┐  ┌────┐  ┌────┐
  │ M1 │──│ M2 │──│ M3 │── ... ──┐  String ~600V DC
  └────┘  └────┘  └────┘         │
                                  ├──▶ String Inverter ──▶ AC (120/240V or 208/480V)
  ┌────┐  ┌────┐  ┌────┐         │    (4-10 kW typical)
  │ M4 │──│ M5 │──│ M6 │── ... ──┘
  └────┘  └────┘  └────┘
  Problem: one shaded/failed panel degrades entire string

  Microinverter (residential):
  ┌────┐    ┌────┐    ┌────┐
  │ M1 ├─∿─▶│ M2 ├─∿─▶│ M3 ├─∿─▶ Combined AC output
  └────┘    └────┘    └────┘
  Each panel has own inverter underneath
  Independence: one panel's failure/shading doesn't affect others
  Higher cost, easier monitoring, better harvest in partial shade

  Power Optimizer (Enphase IQ / SolarEdge):
  Each panel has DC optimizer → all strings optimized individually
  → one central inverter
  Middle ground: panel independence + single central inverter cost

  Central inverter (utility-scale):
  Combiner box (arrays combined to ~1000-1500V DC bus)
  → 1-5 MW central inverter → step-up transformer → grid
  Most cost-effective at utility scale
  Single point of failure, but N+1 redundancy easy at large sites
```

### Grid-Following vs Grid-Forming Inverters

This is the most important technical concept in modern grid integration — the difference between a grid that works with high renewables and one that doesn't.

```
GRID-FOLLOWING INVERTER (current standard):

  Measures grid voltage and frequency → locks its output phase to grid phase
  (Phase-Locked Loop — PLL)
  Acts like a current source: outputs sinusoidal current synchronized to grid

  REQUIREMENT: There must be an existing AC voltage reference to lock to.
               If the grid voltage collapses (blackout), inverter trips offline.
               Cannot "black start" — cannot re-energize a dead grid.
               Contributes ZERO synchronous inertia.

  Implication for high-RE grids: If most generation is grid-following inverters
  and a major disturbance occurs, ALL inverters may trip simultaneously (no
  voltage to lock to) → reinforces the collapse rather than stabilizing it.

GRID-FORMING INVERTER (emerging standard):

  Synthesizes its own voltage reference internally (virtual oscillator control,
  droop control, or virtual synchronous machine algorithm)
  Acts like a voltage source: establishes voltage and frequency, others lock to it

  CAN: black start (re-energize a dead grid)
  CAN: provide synthetic/virtual inertia (software-controlled energy reserve)
  CAN: contribute to fault current (needed for protection relays to detect faults)
  CAN: operate in an island (microgrid without any synchronous generators)

  NERC/FERC are beginning to require grid-forming capability for new inverter
  resources above a threshold. Australia (South Australia) forced this issue in
  2016 after the statewide blackout when all wind farms tripped.
```

The South Australia 2016 blackout illustrates a **correlated failure / thundering herd**: all grid-following inverters depended on the same shared state (grid voltage reference), so when voltage collapsed, every inverter tripped simultaneously — reinforcing the collapse. Grid-forming inverters eliminate this single dependency by holding state independently (no external voltage reference required), analogous to moving from shared-state to self-contained nodes in a distributed system.

**Virtual inertia:** A grid-forming inverter with a battery can simulate inertial response by measuring the rate of change of frequency (ROCOF) and immediately injecting or absorbing power — like a flywheel, but controlled by software. The response can be faster than real synchronous inertia (milliseconds vs seconds). The limit is stored energy in the battery.

---

## Solar Capacity Factor: What the Real Numbers Look Like

```
SOLAR IRRADIANCE MAP (approximate US utility CF):

                    WA: 14-18%
                    OR: 16-20%
                    CA (NV/AZ border): 28-32%
    MT: 18-22%
    ID: 18-22%
    WY: 20-24%
    CO: 22-26%       Southwest:
    UT: 22-26%       NV: 26-30%
    NM: 24-30%       AZ: 27-31%
    TX (west): 24-28%  CA (south): 26-30%

    Midwest: 18-22%
    Southeast: 18-22%
    Northeast: 14-18%

Best US utility solar site: ~30% CF (Sonoran Desert, AZ/NV)
Average new utility installation: ~25%
Germany (worst major solar market): ~10-12% CF
```

**Curtailment:** When solar generation exceeds what the grid can absorb, output must be curtailed (panels deliberately misaligned or inverter limited). California curtailed approximately 3 TWh of solar in 2023 — wasted clean energy. This happens during spring days (mild temperatures, low load, high solar output) and midday year-round. Curtailment is the economic loss driver that makes storage investments compelling.

---

## Wind Power: From Wind Speed to Grid Power

### The Betz Limit

A wind turbine cannot extract all kinetic energy from the wind — if it did, the wind would stop completely and no more air could flow through the rotor disk. Betz (1919) derived the theoretical maximum fraction of kinetic energy extractable: **16/27 ≈ 59.3%**.

**Derivation sketch:** Actuator disk theory. Upstream wind velocity v₀, downstream velocity v_d. For maximum power extraction, v_d = v₀/3. P_max = (16/27) × ½ρAv₀³.

Modern large wind turbines achieve 45-50% aerodynamic efficiency (Betz coefficient 0.45-0.50), close to the theoretical maximum.

### Power Curve and Cube Law

```
P = ½ × ρ × A × v³ × C_p

Where: ρ = air density (~1.225 kg/m³ at sea level, 15°C)
       A = rotor swept area = π r² (r = blade length)
       v = wind speed (m/s)
       C_p = power coefficient (Betz-limited, ~0.45-0.50 for modern turbines)

THE CUBE LAW IS CRITICAL:
  Doubling wind speed → 8× power output
  v = 6 m/s: some power
  v = 12 m/s: 8× more power (if below rated speed)

WIND TURBINE POWER CURVE:

Power
(MW)
  6 │                    ╭──────────────────────── (rated power — pitch control)
    │                   ╭╯
  4 │               ╭───╯
    │           ╭───╯
  2 │       ╭───╯   (cube relationship — output grows steeply with wind speed)
    │   ╭───╯
  0 │───╯
    └──────────────────────────────────────────────────────────▶ wind speed (m/s)
     0   3   6   9  12  15  18  21  24  27  (cut-out)

  Cut-in speed:  ~3.5 m/s (below this: not enough torque to turn)
  Rated speed:  ~12-15 m/s (above this: pitch blades to limit power)
  Cut-out speed: ~25 m/s (above this: shut down to protect turbine)

  The rated output range (12-25 m/s) covers ~40-45% of operating hours at
  good wind sites — this is why good sites reach 40%+ capacity factor.
```

**Rotor size progression (onshore):**
- 2005: 1.5 MW, 77m rotor diameter, 80m hub height
- 2015: 2-3 MW, 100-130m rotor, 80-100m hub height
- 2024: 4-6 MW, 150-175m rotor, 100-160m hub height

**Offshore rotor size progression:**
- 2010: 3-5 MW, 90-126m rotor
- 2020: 8-10 MW, 154-164m rotor
- 2023: 14-15 MW, 220-240m rotor (GE Haliade-X 14 MW: 220m diameter)
- 2024-2025: Vestas V236-15MW, Siemens Gamesa SG 14-236 DD: ~236m diameter

The economic logic: larger rotor sweeps more area (A = π r²), captures more of the resource. Offshore turbines get enormous because you only pay for one foundation, one grid connection, one set of installation vessels — might as well maximize the power per turbine.

### Generator Technologies

**Type 1 (SCIG — Squirrel Cage Induction Generator):**
Directly connected to grid. Simple. Rotor speed varies only ±1-2% (nearly fixed speed). Absorbs reactive power — needs capacitor banks. Poor power quality. Mostly legacy; not built new.

**Type 3 (DFIG — Doubly-Fed Induction Generator):**
The dominant onshore technology until ~2015.

```
DFIG ARCHITECTURE:

  Wind rotor → Gearbox → DFIG generator
                            │           │
                         Stator        Rotor
                            │           │
                        direct to    Back-to-back
                          grid        converter
                         (600V AC)    (typically 30% of
                                       rated power)
                                           │
                                          Grid

Key feature: Rotor is connected to grid through a partial-scale converter
Variable speed operation: rotor can spin ±30% of synchronous speed
Only 30% of power goes through converter → lower cost vs full conversion
Stator connected directly → provides some synchronous inertia (reduced)
Good reactive power control capability
Limitation: fault ride-through requires crowbar circuit (protects converter
            during voltage dip); complex control during grid faults
```

**Type 4 (Full-Rated Converter — PMG or EESG):**
Increasingly dominant for both onshore (large turbines) and offshore.

```
TYPE 4 ARCHITECTURE:

  Wind rotor → [optional gearbox] → Generator → Full converter → Grid transformer
               (direct drive:                    (AC-DC-AC)
                no gearbox)
                                    100% of power through converter
                                    Complete electrical decoupling
                                    Can use permanent magnet generator (PMG)
                                    or electrically excited synchronous generator

Advantages:
  Complete mechanical/electrical decoupling — rotor speed unrelated to grid frequency
  Superior low-voltage ride-through (LVRT) capability
  Excellent reactive power control (4-quadrant: export or absorb Q independently)
  Cleaner power quality
  Can implement grid-forming control (virtual inertia)
  No gearbox option (direct drive PMG) → lower maintenance

Disadvantages:
  100% power through converter → more expensive
  Converter losses ~1-2% of rated power

Main manufacturers: Vestas (V162/V172, direct drive), Siemens Gamesa (offshore),
  GE (Haliade-X offshore), Goldwind (China, PMSG)
```

---

## Offshore Wind: Higher CF, Bigger Turbines, Different Challenges

Offshore wind capacity factors 40-55% vs onshore 25-45% — higher and more consistent wind at sea, no terrain disruption, larger rotors feasible.

```
OFFSHORE FOUNDATION OPTIONS (by water depth):

  0-30m: Monopile
         ┌──────────┐
         │  Turbine │
     ┌───┴───┐
     │       │ tower
   ┌─┴─────┐
   │Transition piece│
   │                │
   │=================│  sea surface
   │                │
   │ Steel pipe      │  ~2-8m diameter
   │ driven/drilled  │
   │ into seabed     │
   └─────────────────┘
   Cheapest; 70% of installed offshore

  30-60m: Jacket / Tripod
         ┌──────────┐
         │  Turbine │
         │   tower  │
         │     ╱    │
         │    ╱     │  3-4 leg jacket structure
         │   ╱      │  welded steel lattice
        ═╧═══════╧══╧═  seabed anchors
   More expensive; used in deeper water

  60-300m: Semi-submersible floating
         ┌──────────┐
         │  Turbine │
         │          │
   ─────────────────────  sea surface
    ╔════╗     ╔════╗
    ║    ║     ║    ║   floating pontoons
    ╚════╝     ╚════╝
    │           │
    mooring lines to seabed anchors
   Enables deepwater sites (US west coast, Scotland, Japan)
   Hywind Scotland: world's first floating wind farm (30 MW, 2017)
   Capital cost ~2-3× fixed-bottom
```

**Offshore power export:** Offshore cables (HVAC or HVDC) bring power to shore. Beyond ~80-100 km from shore, VSC-HVDC becomes the standard because the capacitive charging current of long AC submarine cables consumes the thermal capacity of the cable for reactive power rather than real power.

---

## Capacity Factor Realities and Integration Challenges

### The Variability Problem

Wind and solar don't just vary in annual average — they vary at every timescale:

```
TIMESCALE OF VARIABILITY:

Seconds:       Turbulence, cloud shadow → output fluctuations (smoothed by geographic spread)
Minutes:       Wind gusts, cloud systems → handled by regulation reserves
Hours:         Diurnal cycle (solar: zero at night), weather fronts (wind)
Days:          Weather patterns → multi-day low wind events ("wind droughts")
Seasons:       Solar peaks summer (insolation), winter (demand also high but less sun)
               Wind stronger winter in most US markets (higher demand, more wind — lucky)
Years:         Long-term climate variability (5-10% year-to-year difference in CF)
```

**The "Dunkelflaute" (dark doldrums):** German for "dark lull." Multi-day periods of low wind AND low solar — overcast skies, calm air. Europe has experienced 2-week Dunkelflaute events where solar + wind combined produce <10% of nameplate capacity. This defines the "firm capacity" problem — what do you do for 2 weeks when renewables are nearly absent? This is where nuclear, hydro, gas backup, and long-duration storage matter.

### Transmission Constraints

Best renewable resources are not where the loads are:

```
RESOURCE LOCATION vs LOAD CENTER:

Best US Wind:           Texas Panhandle, Wyoming, Great Plains
Main TX load:           Dallas, Houston (east of wind resources)
Main Midwest load:      Chicago (some transmission constraints)

Best US Solar:          Arizona, Nevada, New Mexico, California desert
Main load:              Phoenix, Las Vegas, LA, but also the entire East Coast

THE TRANSMISSION PROBLEM:
  To use Montana/Wyoming wind for California or Illinois loads,
  you need 1,000-2,000 mile HVDC transmission.
  Cost: ~$1-3M per mile for overhead HVDC (+ converter stations)
  A 2,000 MW, 1,500 mile HVDC line: $4-8B total
  Who pays? Who has right-of-way? Regulatory approvals: 10-15 years

  This is WHY high renewable penetration requires massive transmission investment.
  The resources and the loads are fundamentally geographically separated.
```

### Curtailment Economics

When renewable generation exceeds demand + export capacity:
- Solar and wind must be curtailed (output limited)
- Zero-revenue event for the plant
- Wasted clean energy

California solar curtailment trajectory:
- 2018: 460 GWh curtailed
- 2020: 1,640 GWh
- 2022: 2,050 GWh
- 2023: ~3,000 GWh (accelerating as solar build outpaces storage)

LCOE calculations for solar in high-curtailment scenarios must include curtailment risk — effectively, some fraction of annual generation revenue is lost. A project with 20% curtailment rate needs to price its power 25% higher to compensate.

---

## The Merit Order Effect: Renewables Suppress Their Own Price

```
MERIT ORDER WITH HIGH SOLAR PENETRATION:

Low solar hour (6am):             High solar hour (1pm):
  Marginal unit: CCGT @ $45/MWh    Marginal unit: hydro/nuclear @ $8/MWh
  Wholesale price: $45/MWh         Wholesale price: $8/MWh
                                   (solar pushed everything else off stack)

Effect on solar economics:
  More solar → more midday supply → lower midday prices → lower revenue per MWh
  The more solar you build, the less valuable each additional solar MWh becomes

  This is "value deflation" or "cannibalization premium"
  First 10% solar penetration: minimal price impact
  30% solar penetration: midday prices collapse
  50%+: frequent negative prices during solar hours

  Texas: negative prices occurred 1,500+ hours in 2023
  California: negative price hours growing annually

SOLUTION: time-shift the solar output with storage
  Charge battery at $0-5/MWh (midday)
  Discharge at $60-80/MWh (6-9pm)
  Arbitrage spread = revenue basis for BESS economics
```

---

## LCOE Trends: The Renewable Revolution in Numbers

```
UTILITY-SCALE SOLAR PV LCOE DECLINE (US, $/MWh nominal):

2010:  $300/MWh  ████████████████████████████████████████
2012:  $200/MWh  ██████████████████████████████
2015:  $100/MWh  ███████████████
2018:  $60/MWh   █████████
2020:  $45/MWh   ███████
2022:  $35/MWh   █████
2024:  $28/MWh   ████
(-90% in 14 years — Wright's Law / learning curve)

ONSHORE WIND LCOE:
2010:  $95/MWh   ███████████████
2015:  $65/MWh   ██████████
2020:  $40/MWh   ██████
2024:  $30/MWh   █████
(-68% in 14 years)

Both now below new coal (~$120/MWh) and new nuclear (~$100-150/MWh) for US builds.
Both below new CCGT in high-gas-price scenarios ($65-80/MWh at $5/MMBtu gas).
```

**Learning rates:** Solar PV: ~23% cost reduction for every doubling of cumulative installed capacity. Wind: ~12%. These are among the fastest learning rates of any energy technology ever deployed at scale. They appear to be driven primarily by manufacturing scale (polysilicon, module manufacturing) and incremental engineering improvements.

---

## Decision Cheat Sheet

| Question | Short Answer |
|----------|-------------|
| What limits solar PV efficiency? | Bandgap mismatch (only photons above bandgap absorbed), recombination losses; silicon theoretical max ~29% (Shockley-Queisser); current commercial: 21-23% |
| Grid-following vs grid-forming? | Grid-following needs existing voltage/frequency to lock to, can't black start, contributes no inertia; grid-forming creates its own voltage reference, can black start, can provide virtual inertia |
| What is the Betz limit? | 59.3% — maximum fraction of wind kinetic energy extractable; fundamental physics, not engineering limitation |
| Why does wind power scale as v³? | P ∝ kinetic energy flow rate = ½ρAv² × v = ½ρAv³; doubling wind speed = 8× power |
| DFIG vs Type 4 wind? | DFIG: 30% partial converter, lower cost, some coupling to grid; Type 4: full converter, complete decoupling, better fault ride-through, supports grid-forming control |
| What are cut-in/rated/cut-out speeds? | Cut-in ~3.5 m/s (starts generating); rated ~12-15 m/s (max power); cut-out ~25 m/s (shut down for protection) |
| Why are offshore CFs higher? | More consistent, stronger wind at sea; no terrain disruption; larger rotors viable |
| What is curtailment? | Deliberately limiting renewable output when generation exceeds grid absorption capacity; increasing problem as RE penetration grows |
| What is the duck curve? | Net load shape (load minus solar) creates midday surplus + steep evening ramp; defines need for fast-ramping resources or storage |
| What drives value deflation? | More solar → lower midday prices → lower revenue per solar MWh; makes each incremental solar plant less valuable than the previous one |

---

## Common Confusion Points

**Module efficiency vs system efficiency:** A 22% efficient solar module means 22% of incident sunlight becomes DC electricity at the module level. The actual AC system efficiency to the grid point is lower (~18-20%) due to inverter losses, wiring losses, temperature derating, soiling, shading. Project owners care about "performance ratio" (PR) = actual vs expected energy.

**Capacity factor for solar is NOT just location:** Same location, different designs can vary CF by 20% depending on: panel tilt (fixed vs single-axis tracking), row spacing (inter-row shading), inverter loading ratio (DC/AC ratio of 1.3 means some clipping at high irradiance), and operational factors (soiling, vegetation management). Single-axis tracking adds ~15-20% energy over fixed-tilt at same location.

**DFIG "provides inertia":** Partially true and often misquoted. A DFIG's stator is directly coupled to the grid and provides some synchronous inertia. BUT the converter control decouples the rotor's kinetic energy — most of the turbine's rotational kinetic energy is NOT delivered to the grid during a frequency event unless specifically programmed to do so ("hidden inertia" control). Type 4 turbines contribute no synchronous inertia at all.

**Negative electricity prices:** These are real and increasing. When must-run generation (nuclear, some contracted wind) exceeds demand in off-peak hours, prices go negative — generators pay to deliver electricity. This is not a market failure; it means curtailment would be more expensive than paying someone to take the energy. Storage and demand response are economic responses to negative prices.

**Offshore wind = always better than onshore:** Not for all costs. Capital cost is 2-3× higher per MW. Installation requires specialized vessels ($100k+/day). O&M costs are higher (access, marine logistics). The higher CF partially compensates but doesn't always win on LCOE. Offshore wins on grid value (less curtailment, closer to coastal load centers, no land competition), not always on pure LCOE.

---

*Next: 03-TRANSMISSION.md — why high voltage, transformers, HVDC, reactive power, line ratings*
*See also: 05-GRID-STABILITY.md for the inertia/grid-forming inverter stability discussion*
*See also: 06-ENERGY-STORAGE.md for storage as the solution to duck curve and curtailment*
