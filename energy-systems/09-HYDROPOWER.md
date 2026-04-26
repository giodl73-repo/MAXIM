# Hydropower — Gravity's Gift to the Grid

*Hydropower is the oldest large-scale electricity source and the only renewable that is
fully dispatchable. A reservoir stores potential energy — water at height — and converts
it to electricity on demand. No Carnot limit applies: gravitational potential energy
converts directly to shaft work through turbine hydrodynamics. The Alchemist's overhead
here is friction, turbulence, and the ecological cost of interrupting a river.*

---

## The Big Picture — Hydropower in the Energy System

```
HYDROPOWER LANDSCAPE

                          DISPATCHABLE?    CF       SCALE        ROLE IN GRID
  ┌──────────────────────────────────────────────────────────────────────────────┐
  │  RESERVOIR HYDRO        Yes (hours-     30-60%   100 MW-     Baseload + peak
  │  (dam + storage)        months of        (avg    22 GW       + ancillary
  │                         stored energy)   45%)    (Three      services
  │                                                  Gorges)
  ├──────────────────────────────────────────────────────────────────────────────┤
  │  RUN-OF-RIVER (ROR)     No (follows     25-50%   1-500 MW   Baseload only
  │  (weir/diversion,       river flow)                          (limited storage)
  │  no large reservoir)
  ├──────────────────────────────────────────────────────────────────────────────┤
  │  PUMPED HYDRO (PHS)     Yes (daily      N/A      100 MW-    Storage + grid
  │  (upper + lower         cycle; charges   (net     3.6 GW     balancing
  │  reservoir)             off-peak)       consumer) (Bath      (see 03-ENERGY
  │                                                   County)    -STORAGE)
  ├──────────────────────────────────────────────────────────────────────────────┤
  │  MICRO / SMALL HYDRO    Partly          30-60%   <1-10 MW   Rural/remote
  │  (<10 MW)               (limited        (site-              electrification
  │                         storage)         dependent)
  └──────────────────────────────────────────────────────────────────────────────┘

GLOBAL HYDRO CAPACITY AND GENERATION (2024):
  Installed capacity:   ~1,400 GW (conventional) + ~170 GW (pumped storage)
  Annual generation:    ~4,400 TWh (~15% of global electricity)
  Capacity factor:      ~36% average (highly variable by geography/season)
  Largest producers:    China (~1,300 TWh), Brazil (~400 TWh), Canada (~380 TWh),
                        USA (~260 TWh), Russia (~200 TWh), Norway (~140 TWh)

HYDROPOWER'S UNIQUE GRID ROLE:
  1. Dispatchable renewable — ramp in seconds-minutes (unlike solar/wind)
  2. Black start capable — can restart grid after blackout (no external power needed)
  3. Frequency regulation — governor response matches or beats gas turbines
  4. Reactive power — synchronous generators provide essential voltage support
  5. Seasonal storage — multi-month reservoir in Norway, Brazil
  6. Flood control — non-energy benefit that justifies many dams
  7. Irrigation — often the original purpose; electricity is a co-benefit
```

---

## Fundamental Physics — Head, Flow, and Power

```
HYDROPOWER EQUATION:

  P = η × ρ × g × Q × H

  where:
    P = power (W)
    η = overall efficiency (turbine × generator × transformer) ≈ 0.85-0.93
    ρ = water density = 1,000 kg/m³
    g = gravitational acceleration = 9.81 m/s²
    Q = volumetric flow rate (m³/s)
    H = net head (m) = gross head - hydraulic losses (friction, bends, valves)

  EXAMPLE:
  H = 200 m (medium-high head), Q = 50 m³/s, η = 0.90
  P = 0.90 × 1000 × 9.81 × 50 × 200 = 88.3 MW

  ENERGY STORED IN RESERVOIR:
  E = ρ × g × V × H_avg × η

  where V = usable reservoir volume (m³), H_avg = average head over drawdown

  Three Gorges (China):
  V ≈ 22 km³ usable, H_avg ≈ 80 m, η = 0.90
  E = 1000 × 9.81 × 22×10⁹ × 80 × 0.90 = 15.5 × 10¹² J = 4,300 GWh
  For context: ~6 months of the plant's own output stored in the reservoir.

  SPECIFIC SPEED:
  Ns = N × √P / H^(5/4)    (dimensionless form varies by convention)

  This parameter determines which turbine type is optimal for a given
  combination of head (H) and flow (Q). It is the turbine engineer's
  fundamental selection criterion — analogous to Reynolds number for
  fluid flow regime selection.
```

---

## Turbine Types — Pelton, Francis, Kaplan

The three dominant turbine types each occupy a distinct region of the head-flow space.
Selecting the wrong turbine for a site is like using quicksort on nearly-sorted data —
it works, but you leave performance on the table.

### Pelton Turbine — High Head, Low Flow

```
PELTON TURBINE:

  ┌───────────────────────────────────────────────────────┐
  │                                                       │
  │  PENSTOCK (high-pressure pipe from reservoir)         │
  │       │                                               │
  │       ▼                                               │
  │  ┌─────────┐                                          │
  │  │  NOZZLE  │──► High-velocity water jet              │
  │  │ (spear   │    V_jet = Cv × √(2gH)                │
  │  │  valve)  │    Cv ≈ 0.98 (nozzle velocity coeff)   │
  │  └─────────┘                                         │
  │       │                                               │
  │       ▼                                               │
  │  ┌───────────────────────────────────────────────┐   │
  │  │  RUNNER (wheel with double-cupped buckets)    │   │
  │  │                                               │   │
  │  │    ╭──────╮                                    │  │
  │  │   ╱ bucket ╲   Jet strikes bucket center      │   │
  │  │  │  ╭──╮   │   Splits, deflects ~170°         │   │
  │  │  │ ╱    ╲  │   Momentum transfer → torque      │   │
  │  │   ╲      ╱     Water exits at low velocity     │   │
  │  │    ╰────╯                                      │   │
  │  │                                                │   │
  │  │  Runner operates in AIR (not submerged)        │   │
  │  │  Atmospheric discharge (no draft tube)         │   │
  │  └───────────────────────────────────────────────┘   │
  │                                                       │
  │  IMPULSE turbine: all pressure → velocity at nozzle  │
  │  Runner at atmospheric pressure                       │
  └───────────────────────────────────────────────────────┘

  OPERATING RANGE:
  Head:        200-1,800 m (record: ~1,890 m at Bieudron, Switzerland)
  Flow:        0.5-50 m³/s per jet (multiple jets for higher Q)
  Power:       1-400 MW
  Efficiency:  90-93% at design point; excellent part-load (down to 20%)
  Speed:       300-1,000 RPM (varies with head and diameter)

  WHY PELTON FOR HIGH HEAD:
  At very high head, the jet velocity is enormous (V = √(2gH)):
  H = 1000 m → V = √(2 × 9.81 × 1000) = 140 m/s (~500 km/h)
  This energy is kinetic — an impulse turbine captures it directly.
  Reaction turbines (Francis, Kaplan) would need to withstand huge
  pressures in the runner; Pelton avoids this by converting all
  pressure to velocity at the nozzle before the runner.

  REGULATION: Spear valve adjusts nozzle opening → varies Q
  Deflector plate diverts jet away from runner for emergency stop
  (avoids water hammer from sudden nozzle closure)
```

### Francis Turbine — The Versatile Workhorse

```
FRANCIS TURBINE:

  ┌───────────────────────────────────────────────────────┐
  │                                                       │
  │  PENSTOCK                                             │
  │       │                                               │
  │       ▼                                               │
  │  ┌───────────────────────────────────┐                │
  │  │  SPIRAL CASING (scroll)            │               │
  │  │  Distributes flow evenly around    │               │
  │  │  the runner circumference          │               │
  │  │          ╭───────────╮             │               │
  │  │    ──►  ╱ Guide vanes ╲   ──►     │                │
  │  │        │   (wicket     │          │                │
  │  │    ──►   │    gates)    │   ──►    │               │
  │  │         ╲  adjustable ╱           │                │
  │  │          ╰─────┬─────╯            │                │
  │  └────────────────┼──────────────────┘               │
  │                   ▼                                   │
  │  ┌────────────────────────────────────┐              │
  │  │  RUNNER                            │              │
  │  │  Mixed-flow: water enters radially, │             │
  │  │  exits axially                     │              │
  │  │  REACTION turbine: pressure drops  │              │
  │  │  across BOTH guide vanes AND runner │             │
  │  │  Runner is SUBMERGED (not in air)  │              │
  │  └────────────┬───────────────────────┘              │
  │               │                                       │
  │               ▼                                       │
  │  ┌────────────────────────────────────┐              │
  │  │  DRAFT TUBE                        │              │
  │  │  Diffuser: recovers kinetic energy │              │
  │  │  from runner exit, converts back   │              │
  │  │  to pressure → increases effective │              │
  │  │  head (enables setting runner above │             │
  │  │  tailwater without losing head)    │              │
  │  └────────────────────────────────────┘              │
  │                                                       │
  └───────────────────────────────────────────────────────┘

  OPERATING RANGE:
  Head:        30-700 m (most versatile range)
  Flow:        1-800+ m³/s
  Power:       1-800 MW (Three Gorges: 32 × 700 MW Francis turbines)
  Efficiency:  92-95% at design point (the highest of any hydro turbine)
  Speed:       60-600 RPM (synchronous to grid frequency)

  WHY FRANCIS DOMINATES:
  ~60% of all hydropower capacity worldwide uses Francis turbines.
  The mixed-flow design (radial in, axial out) works across a wide
  head range. The reaction principle captures energy from both
  pressure and velocity changes across the runner.

  WICKET GATES (guide vanes):
  Adjustable vanes control flow to the runner.
  Opening/closing changes Q → varies power output.
  Full open = maximum flow = rated power.
  Closed = zero flow = shutdown.
  Servo-hydraulic actuators move gates in seconds → fast regulation.

  PART-LOAD BEHAVIOR:
  Francis turbines are optimized for design flow.
  Below ~60% of design flow: efficiency drops significantly.
  "Rough zone" at 30-50% load: vortex rope in draft tube
  causes vibration and pressure pulsation → operators avoid this range.
  → Unlike Pelton, Francis does NOT have a flat efficiency curve.
```

### Kaplan Turbine — Low Head, High Flow

```
KAPLAN TURBINE:

  ┌───────────────────────────────────────────────────────┐
  │                                                       │
  │  Flow enters scroll casing → guide vanes → runner     │
  │                                                       │
  │  ┌────────────────────────────────────────┐           │
  │  │  RUNNER: axial flow (propeller-type)    │          │
  │  │                                         │          │
  │  │    ───►  ┌──────────┐  ───►            │          │
  │  │          │ Adjustable│                  │         │
  │  │    ───►  │  blades  │  ───►            │          │
  │  │          │ (4-8 per │                  │          │
  │  │    ───►  │  runner) │  ───►            │          │
  │  │          └──────────┘                   │         │
  │  │                                         │          │
  │  │  DOUBLE REGULATION:                     │          │
  │  │  Both guide vanes AND runner blades     │          │
  │  │  adjust → optimal efficiency across     │          │
  │  │  wide flow range                        │          │
  │  └─────────────────────────┬──────────────┘          │
  │                            ▼                          │
  │                   DRAFT TUBE (diffuser)               │
  │                                                       │
  └───────────────────────────────────────────────────────┘

  OPERATING RANGE:
  Head:        2-80 m (low head rivers, tidal)
  Flow:        20-1,000+ m³/s (very large volumes)
  Power:       1-200 MW per unit
  Efficiency:  91-94% at design point; EXCELLENT part-load
               (double regulation keeps η>85% from 20% to 100% load)
  Speed:       60-300 RPM (low-speed, large diameter)

  KAPLAN vs FRANCIS at LOW HEAD:
  Below ~30 m head, Francis runners become very large and inefficient.
  Kaplan's axial-flow design handles huge volumes at low head efficiently.
  Double regulation (adjustable guide vanes + adjustable runner blades)
  gives Kaplan superior part-load performance vs Francis.

  VARIANTS:
  ┌──────────────┬──────────────────────────────────────────────┐
  │ Kaplan       │ Adjustable guide vanes + adjustable blades   │
  │ (full)       │ Best efficiency range; highest cost          │
  ├──────────────┼──────────────────────────────────────────────┤
  │ Semi-Kaplan  │ Adjustable guide vanes, fixed blades         │
  │              │ Simpler, cheaper; narrower efficiency range   │
  ├──────────────┼──────────────────────────────────────────────┤
  │ Propeller    │ Fixed guide vanes + fixed blades             │
  │              │ Cheapest; single design point only           │
  ├──────────────┼──────────────────────────────────────────────┤
  │ Bulb turbine │ Generator inside water passage (horizontal)  │
  │              │ Very low head (2-25 m); tidal applications   │
  │              │ La Rance tidal plant (France, 240 MW, 1966)  │
  └──────────────┴──────────────────────────────────────────────┘
```

### Turbine Selection Guide

```
TURBINE TYPE SELECTION — HEAD vs FLOW:

  Head (m)
  │
  │ 1800 │ ████████████████
  │      │ █  PELTON      █
  │ 1000 │ █  (impulse)   █
  │      │ █              █
  │  500 │ ████████████████
  │      │      ████████████████████████
  │  200 │      █                      █
  │      │      █   FRANCIS            █
  │  100 │      █   (reaction, mixed)  █
  │      │      █                      █
  │   50 │      █                      █
  │      │      ████████████████████████
  │   30 │           █████████████████████████████
  │      │           █                           █
  │   10 │           █   KAPLAN                  █
  │      │           █   (reaction, axial)       █
  │    2 │           █                           █
  │      │           █████████████████████████████
  │
  └──────┼──────┼──────┼──────┼──────┼──────┼─────── Q (m³/s)
         0.5    5     50    200   500  1000+

  OVERLAP ZONES:
  30-80 m head, medium flow:  Francis OR Kaplan — economics decide
  200-500 m head, low flow:   Pelton OR Francis — site geometry decides
  Very low head (<5 m):       Bulb Kaplan or Archimedes screw (micro)

  DECISION RULE OF THUMB:
  Head > 200 m → Pelton (consider Francis if Q is very large)
  Head 30-200 m → Francis (dominant choice for medium installations)
  Head < 30 m → Kaplan (or bulb for run-of-river at very low head)

  BRIDGE: Turbine selection by head/flow is directly analogous to
  data structure selection by access pattern. Hash table (O(1) lookup)
  for random access, B-tree for range queries, bloom filter for
  membership testing. Wrong choice works but at severe performance cost.
  Pelton at low head = hash table for sequential scan — functional but
  wasting the design's strengths.
```

### Efficiency Curves

```
EFFICIENCY vs LOAD — ALL THREE TURBINE TYPES:

  η (%)
  │
  95│                    ╭─────╮ Francis (peak)
  │                   ╱       ╲
  93│    ╭────────────╱         ╲── Francis
  │    │           ╱             ╲
  91│    │ Pelton ─╱               ╲
  │    │  (flat efficiency          ╲
  89│    │   across load range)      ╲ Francis drops at part-load
  │    │                              ╲
  87│  ──╯                             ╲
  │       ╭──────────────────────────╮ ╲
  85│      │  Kaplan (double-regulated)│  ╲
  │       │  stays high across range  │   ╲
  83│       ╰──────────────────────────╯
  │
  80│
  │
  └────┼─────┼──────┼──────┼──────┼──────── % of design flow
       20    40     60     80    100

  KEY OBSERVATIONS:
  Pelton:  Flattest efficiency curve (multi-jet operation)
           Excellent for variable-load applications
           Each jet can be independently controlled

  Francis: Highest peak efficiency (~94-95%) but drops off
           at part load due to draft tube vortex and off-design
           guide vane angles. "Rough zone" at ~35-50% avoided.

  Kaplan:  Double regulation keeps efficiency >85% across 20-100%
           Best part-load performance for low-head sites.
           Single most expensive but justified by flexibility.
```

---

## Plant Configurations

### Reservoir (Storage) Hydro

```
RESERVOIR HYDROPOWER — SYSTEM DIAGRAM:

  ┌─────────────────────────────────────────────────────────────┐
  │                                                             │
  │  RESERVOIR (impounded water behind dam)                     │
  │  Volume: millions to km³ of water                           │
  │  Purpose: store water for seasonal/annual regulation        │
  │                                                             │
  │  ┌─────────────────┐                                        │
  │  │       DAM        │  Concrete gravity, arch, earth-fill, │
  │  │  (retains water) │  or rock-fill — site geology decides  │
  │  └────────┬────────┘                                       │
  │           │  INTAKE (with trash rack + gate)                │
  │           ▼                                                 │
  │  ┌─────────────────┐                                       │
  │  │    PENSTOCK      │  Pressure conduit: steel-lined tunnel │
  │  │  (water tunnel) │  or surface pipe. Length: 100m-10km+  │
  │  └────────┬────────┘                                       │
  │           ▼                                                 │
  │  ┌─────────────────────────────────────┐                   │
  │  │  POWERHOUSE                         │                   │
  │  │  Turbines + generators + transformers│                  │
  │  │  Surface, underground, or cavern    │                   │
  │  └────────┬────────────────────────────┘                   │
  │           ▼                                                 │
  │  ┌─────────────────┐                                       │
  │  │   TAILRACE      │  Returns water to river downstream    │
  │  └─────────────────┘                                       │
  │                                                             │
  │  SPILLWAY: overflow safety valve (uncontrolled release      │
  │  if reservoir is full during flood — protects dam)          │
  └─────────────────────────────────────────────────────────────┘

  OPERATING MODES:
  Baseload:     Run at steady output (e.g., 60% of capacity)
  Peaking:      Ramp up during daily demand peaks (morning/evening)
  Regulation:   Governor responds to grid frequency deviations in <5 seconds
  Flood control: Pre-release water before forecasted flood season

  SEASONAL STORAGE:
  Norway: 87 TWh of reservoir storage = ~50% of annual generation capacity
  → Can store spring snowmelt and release through dry autumn/winter
  → Natural complement to Nordic wind (winter wind → summer hydro balance)
  Brazil: Itaipu + Belo Monte + Tucurui — Amazon basin seasonal cycle
  → Wet season fills reservoirs; dry season dispatches stored water

  BLACK START:
  Hydro plants are the primary black start resource for most grids.
  After a total blackout, hydro generators can self-start (water + gravity
  = no external power needed). They energize the transmission grid,
  then thermal plants can restart. No other large-scale renewable can do this.
```

### Run-of-River (ROR)

```
RUN-OF-RIVER HYDRO:

  River flow → diversion weir → headrace canal or tunnel → penstock
  → turbine (Francis or Kaplan) → tailrace → river

  KEY DIFFERENCES FROM RESERVOIR:
  • No significant storage (or very small pondage for daily regulation)
  • Output follows river flow — variable, seasonal
  • Environmental impact lower (no large reservoir, less habitat loss)
  • Fish passage easier (smaller structures)
  • Capacity factor highly dependent on hydrology

  TYPICAL CF:
  Glacier-fed rivers (Alps, Norway): 50-70% (steady melt, long season)
  Rain-fed tropical rivers (SE Asia): 40-60%
  Snowmelt-dominated (Pacific NW): 30-50% (seasonal, spring-heavy)

  SCALE EXAMPLES:
  Chief Joseph Dam (WA, USA): 2,620 MW (ROR on Columbia River, high flow)
  Beauharnois (Quebec): 1,903 MW (St. Lawrence River, stable flow)
  Many ROR projects in Nepal, Bhutan, Laos: 10-500 MW on steep rivers

  PONDAGE:
  Some ROR plants have small pondage (hours-days of storage)
  Allows daily load-following: store overnight, release for peak
  Not seasonal storage — just daily flexibility
```

### Small and Micro Hydro

```
SMALL HYDRO CLASSIFICATION:

  Category        Capacity       Typical application
  ──────────────  ─────────────  ────────────────────────────────
  Pico hydro      <5 kW          Single household, off-grid
  Micro hydro     5-100 kW       Village, small community
  Mini hydro      100 kW-1 MW    Small town, industrial site
  Small hydro     1-10 MW        Grid-connected, regional

  TECHNOLOGIES FOR VERY LOW HEAD / SMALL SCALE:
  ┌──────────────────┬────────────────────────────────────────┐
  │ Archimedes screw │ 1-10 m head, 0.1-10 m³/s               │
  │                  │ Fish-friendly (very slow rotation)     │
  │                  │ η ≈ 80-90%, simple, low maintenance    │
  │                  │ Historically: grain mills, now: micro  │
  ├──────────────────┼────────────────────────────────────────┤
  │ Crossflow        │ 2-200 m head, 0.02-10 m³/s            │
  │ (Banki-Mitchell) │ Self-cleaning, debris-tolerant         │
  │                  │ η ≈ 80-85%, cheap to manufacture       │
  │                  │ Popular in developing world            │
  ├──────────────────┼────────────────────────────────────────┤
  │ Turgo            │ 15-300 m head (like small Pelton)      │
  │                  │ η ≈ 85-90%, compact, simple            │
  │                  │ Good for micro/mini with moderate head │
  └──────────────────┴────────────────────────────────────────┘

  GLOBAL SMALL HYDRO:
  Installed: ~80 GW globally (2024)
  China: ~50 GW (massive rural electrification program, 1980s-2000s)
  Europe: ~20 GW (many heritage sites, refurbished)
  Potential: IRENA estimates ~230 GW untapped globally
  Environmental tension: small dams fragment rivers cumulatively;
  many conservation groups now oppose small hydro on ecological grounds
```

---

## Environmental Trade-offs

```
HYDROPOWER ENVIRONMENTAL IMPACT MATRIX:

  Impact                    Reservoir hydro       Run-of-river
  ────────────────────────  ──────────────────    ──────────────────
  Land inundation           HIGH (reservoir)      LOW (no reservoir)
  Fish migration blockage   HIGH (dam barrier)    MODERATE (weir)
  Sediment trapping         HIGH (reservoir traps LOW (weir passes
                            bed load → downstream  some sediment)
                            erosion, delta loss)
  Downstream flow change    HIGH (regulated       LOW (flow mostly
                            release ≠ natural     preserved)
                            hydrograph)
  GHG emissions             VARIABLE              LOW
  (reservoir methane        Tropical reservoirs:
  from decomposing          2-20 g CO₂eq/kWh
  organic matter)           Temperate: <5 g
  Water evaporation         HIGH in arid climates LOW
  (reservoir surface)       (Lake Mead: ~6% of
                            Colorado River flow)
  Community displacement    HIGH (Three Gorges:   LOW
                            1.3M people relocated)
  Cultural/archaeological   HIGH (submerged       MODERATE
  loss                      sites)

  THE METHANE PROBLEM IN TROPICAL RESERVOIRS:
  Organic matter flooded by reservoir decomposes anaerobically → CH₄.
  Worst case: Balbina Dam (Brazil) — lifecycle emissions higher than
  coal per kWh (huge reservoir, small generation, warm tropics).
  Best case: Norwegian reservoirs — cold, oligotrophic, minimal organic.
  Rule of thumb: reservoir area / power output ratio determines emissions.
  Low ratio (deep, narrow valleys) = low emissions per kWh.
  High ratio (shallow, wide tropical floodplains) = high emissions per kWh.

  FISH PASSAGE:
  Fish ladder (pool-and-weir): effective for some species (salmon)
  Fish elevator/lift: used at very high dams
  Trap and haul: truck fish upstream (Bonneville, Columbia River)
  Downstream: juvenile fish passage screens, bypass channels
  Reality: no technology fully replaces a free-flowing river for
  anadromous fish (salmon, steelhead, shad). Dam removal is growing:
  Elwha River (WA): 2 dams removed 2011-2014 → salmon returned within years.
  Klamath River (CA/OR): 4 dams removed 2023-2024 → largest dam removal in US history.
```

---

## Hydropower Economics

```
LCOE AND COST STRUCTURE:

  Component          New large hydro     Existing (paid-off)    Pumped hydro (new)
  ─────────────────  ──────────────────  ────────────────────   ──────────────────
  Capital cost       $1,500-5,000/kW    ~$0 (amortized)        $1,500-3,000/kW
  Fixed O&M          $20-40/kW-yr       $15-30/kW-yr           $15-35/kW-yr
  Variable O&M       $2-5/MWh           $2-5/MWh               $3-6/MWh
  LCOE               $25-90/MWh         $10-25/MWh             LCOS: $40-100/MWh
  Lifetime           50-100+ years      (many > 80 years)      50-100 years
  WACC sensitivity   HIGH (long build)  LOW (operating)        HIGH

  WHY NEW HYDRO IS EXPENSIVE:
  1. Construction: massive civil works (dams, tunnels, penstocks)
  2. Duration: 5-10 year construction (capital tied up earning nothing)
  3. Financing: interest during construction adds 30-60% to overnight cost
  4. Geology risk: rock quality, seismic, groundwater — each site unique
  5. Environmental mitigation: fish passage, relocation, compensation

  WHY EXISTING HYDRO IS PRICELESS:
  1. Zero fuel cost (gravity is free)
  2. Capital fully amortized (paid off decades ago)
  3. O&M is low and predictable
  4. Extremely long-lived (Hoover Dam: 1936, still running)
  5. Provides ancillary services that solar/wind cannot

  KEY GLOBAL INVESTMENT:
  China: ~400 GW installed, still building (~10 GW/yr)
  Africa: only ~40 GW of ~250 GW economically viable potential developed
  Grand Ethiopian Renaissance Dam (GERD): 5.2 GW, filling since 2020
  → geopolitical tension with Egypt/Sudan over Nile water allocation
```

---

## Pumped Hydro Storage — The Time-Shifter

Covered in detail in `03-ENERGY-STORAGE.md`. Key additions here focus on the
hydrodynamic integration with the grid.

```
PUMPED HYDRO IN THE VRE GRID:

  DAILY CYCLE (duck curve arbitrage):
  ┌──────────────────────────────────────────────────────────┐
  │  Midday (11am-3pm):   Solar surplus → negative LMP       │
  │    PUMP MODE:  buy cheap electricity, pump water uphill  │
  │                (consuming 1,200-1,500 MWh)               │
  │                                                          │
  │  Evening (5pm-9pm):   Solar gone, demand peak            │
  │    TURBINE MODE: release water, generate 1,000-1,200 MWh│
  │                  (round-trip efficiency: 78-85%)         │
  │                                                          │
  │  Revenue = (peak price × generation) - (off-peak × pump) │
  │  If peak = $60/MWh and off-peak = $10/MWh:               │
  │  Revenue = $60 × 1100 - $10 × 1375 = $66,000 - $13,750 │
  │         = $52,250 per cycle → ~$19M/yr                   │
  └──────────────────────────────────────────────────────────┘

  SEASONAL CYCLE (Norway / Swiss Alps):
  Spring snowmelt → fill reservoirs (water is abundant, demand is low)
  Winter → draw down reservoirs for heating/lighting demand
  → Natural seasonal storage without electrolysis/hydrogen

  VARIABLE-SPEED PUMPED HYDRO:
  Traditional PHS: pump operates at fixed speed (synchronous motor)
  → Cannot adjust pump power; consumes fixed amount of electricity
  Variable-speed PHS: uses doubly-fed induction machine or full converter
  → Pump power adjustable (can follow VRE fluctuations while pumping)
  → Grid regulation service while pumping (new revenue stream)
  → 3-5% round-trip efficiency gain from optimized pump operation
  Examples: Goldisthal (Germany, 1,060 MW), Nant de Drance (Switzerland, 900 MW)

  SEAWATER PUMPED HYDRO:
  Uses ocean as lower reservoir → no need for lower dam.
  Okinawa Yanbaru (Japan, 30 MW): only operational seawater PHS
  Corrosion management (seawater): more expensive materials and coatings
  Advantage: coastal sites abundant where geography has cliffs near ocean
  Proposed: multiple sites in Australia, Chile, Spain, South Africa
```

---

## Hydropower and Climate Change

```
CLIMATE IMPACTS ON HYDROPOWER:

  Region               Projection                    Impact on hydro
  ──────────────────   ──────────────────────────    ──────────────────
  Glacier-fed rivers   Glaciers shrink → initial     Short-term increase,
  (Alps, Andes,        melt increase, then           long-term decline
  Himalayas)           permanent loss by 2050-2100   as glaciers disappear

  Snow-dominated       Snowpack declines →           Earlier spring peak,
  (Pacific NW, Nordic) earlier, lower spring melt    lower summer flow

  Tropical (Amazon,    More intense wet/dry cycles   Higher flood risk,
  Mekong, Congo)       More extreme droughts         lower dry-season output

  Mediterranean        Less total precipitation       Declining annual output
  (Iberia, Turkey)     Shift to more intense but     (~10-20% by 2050)
                       rarer storms

  HYDROPOWER VULNERABILITY SCORE:
  High vulnerability:  Single-river dependence + glacier loss + drought trend
  Low vulnerability:   Diverse basins + stable precipitation + large reservoirs

  EXAMPLE — Western US:
  Lake Mead (Hoover Dam): water level dropped ~50 m since 2000
  Power output reduced from 2,074 MW to ~1,500 MW (head-dependent)
  Colorado River Compact: overallocated relative to actual flow
  → Climate change + overallocation = structural deficit

  ADAPTATION:
  1. Interconnect hydro-rich and hydro-poor regions (transmission)
  2. Pair hydro with VRE (wind/solar fill gaps during low-water years)
  3. Optimize reservoir operations with improved climate forecasting
  4. Accept that some hydro assets will lose capacity — plan replacements
```

---

## Bridges — Hydropower to Computing

| Hydropower Concept | Computing/Distributed Systems Parallel |
|-------------------|---------------------------------------|
| Reservoir (stored PE) | Buffer/queue (stored work units) — smooth variable supply into steady demand |
| Head (driving force) | Voltage / pressure differential in a pipeline — the potential that drives flow |
| Turbine selection by head/flow | Data structure selection by access pattern — wrong choice works but wastes performance |
| Run-of-river (no storage) | Streaming pipeline (process data as it arrives, no buffering) |
| Spillway (safety overflow) | Backpressure / circuit breaker — controlled overflow when input exceeds capacity |
| Francis "rough zone" at 35-50% load | Garbage collector pauses in throughput "dead zone" — certain operating ranges are unstable |
| Double regulation (Kaplan) | Two-level load balancing — coarse (guide vanes = admission control) + fine (blade angle = per-request routing) |
| Fish ladder (passage around dam) | Bypass route around a bottleneck — lets some traffic through at reduced throughput |
| Dam removal (Elwha, Klamath) | Technical debt removal — decommissioning infrastructure that no longer justifies its cost |
| Variable-speed PHS | Auto-scaling consumer — adjusts consumption rate to match available supply (VRE) |

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| What fraction of global electricity is hydro? | ~15% (~4,400 TWh/yr from ~1,400 GW) |
| Most common turbine type? | Francis (~60% of installed capacity) |
| When to use Pelton? | Head > 200 m, moderate flow (impulse, jet-driven) |
| When to use Kaplan? | Head < 30 m, very high flow (propeller, double-regulated) |
| Peak turbine efficiency? | Francis: 94-95%; Pelton: 92-93%; Kaplan: 91-94% |
| Can hydro provide grid frequency regulation? | Yes — governor response in seconds; a primary grid stabilizer |
| Can hydro black-start a grid? | Yes — only large-scale renewable that can |
| Why is existing hydro so cheap? | Capital amortized (zero fuel + paid-off dam = $10-25/MWh) |
| Is new large hydro being built? | Yes, mainly China and Africa; OECD mostly refurbishing |
| Pumped hydro round-trip efficiency? | 78-85% (pump η × turbine η) |
| Climate change impact on hydro? | Varies: glacier-fed rivers decline long-term; tropics face drought/flood extremes |
| Why is reservoir methane a concern? | Tropical reservoirs with high area/power ratio → anaerobic decomposition → CH₄ |
| Largest hydropower plant? | Three Gorges (China): 22.5 GW, ~100 TWh/yr |

---

## Common Confusion Points

**"Hydropower is not truly renewable"**
The water cycle (evaporation → precipitation → runoff → generation → evaporation) is solar-driven
and self-renewing. Hydro is renewable. What is not infinite is the number of suitable sites,
and climate change is altering the water cycle. But the energy source (gravity + solar-driven
water cycle) is fundamentally renewable.

**"Small hydro is always better for the environment than large hydro"**
Per unit of electricity, small hydro often has worse environmental impact than large hydro.
Many small dams fragment more total river kilometers than one large dam. The aggregate
impact of thousands of micro dams can exceed that of a single large reservoir. This is
the "death by a thousand cuts" problem in river ecology.

**"Run-of-river means no environmental impact"**
ROR plants still divert flow, create barriers, alter downstream hydrology, and can dewater
river reaches between the diversion and tailrace. "Run-of-river" is a spectrum, not a binary.
Some ROR plants have significant pondage (daily storage) that alters natural flow patterns.

**"Hydropower capacity factor is low, so hydro is unreliable"**
A reservoir hydro plant with 40% CF is not running 40% of the time randomly.
It is dispatched strategically: running at full power during peaks, off during cheap
hours. Low CF in hydro usually means the plant is providing peaking/regulation services —
its most valuable function. CF for hydro reflects dispatch strategy, not reliability.

**"Pumped hydro is the only mature grid storage"**
True by installed GWh (~93% of global grid storage). But Li-ion BESS is adding
capacity faster and doesn't require specific geography. Pumped hydro's advantage is
duration (8-24+ hours), lifetime (50-100 years), and very low marginal cost per cycle.
Its disadvantage is lead time (7-15 years to build) and geography dependence.

**"Dam safety is solved"**
Most dam failures involve older earthfill/embankment dams, inadequate spillway capacity,
or foundation geology that was poorly characterized at construction. The 1975 Banqiao Dam
failure (China) killed an estimated 85,000-240,000 people. Oroville Dam spillway failure
(2017, California) forced 188,000 evacuations. Dam safety requires ongoing monitoring,
updated hydrological analysis (climate change increases design floods), and political will
to invest in maintenance of aging infrastructure. The US has ~90,000 dams; average age >50 years.
