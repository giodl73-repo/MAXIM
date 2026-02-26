# Controlled Environment Agriculture: Greenhouses and Vertical Farms

## The Big Picture

Controlled environment agriculture (CEA) is the application of engineering systems to manage all or most of the variables that affect plant growth. It represents the convergence of horticulture, HVAC, electrical engineering, and information systems.

```
CEA CONTINUUM:

  OPEN FIELD          LOW TUNNEL        GREENHOUSE        VERTICAL FARM
  (no control)        (frost only)      (partial→full)    (full control)
  +------------+    +------------+    +------------+    +------------+
  | Weather as |    | Season     |    | Temperature|    | All climate|
  | received   |    | extended   |    | Humidity   |    | parameters |
  | No capital |    | ~1–5°C     |    | CO₂        |    | LED spectra|
  | overhead   |    | advantage  |    | Irrigation |    | No sunlight|
  +------------+    +------------+    +------------+    +------------+
       |                 |                 |                 |
  Lowest cost/unit → → → → → → → → → → Highest cost/unit
  Lowest control → → → → → → → → → → → Highest control
  Weather risk high → → → → → → → → → Weather risk zero

THE ENGINEERING CHALLENGE:
  As control increases, capital and operating costs increase.
  The economic justification requires: high crop value, year-round
  production, geographic isolation from natural growing season, or
  supply chain reliability premium.
```

---

## Greenhouses

### Structure and Glazing

```
GREENHOUSE GEOMETRY:
  Venlo (Dutch, most common commercial): multi-span, W-shaped gutters,
    vertical sides + pitched roof. Maximum headroom, efficient structure.
    Standard module: 3.2m or 4m span × 8m bay length.
    Height to gutter: 5–7m (modern) for good climate management.

  Gothic arch: single arch shape; shed snow well; popular in cold climates.
  Single span: simplest; good for small operations.
  Saw-tooth: asymmetric spans; north light glazing; good diffuse light.
  Chinese solar: passive solar thermal; common in China; unheated or minimal heat.

GLAZING COMPARISON:
  Material          Light transmit  U-value  Lifespan  Cost index
  ──────────────────────────────────────────────────────────────────
  Single glass       90%           6.0       50+ yr    High
  Double glass       78%           3.0       50+ yr    Very high
  Polycarbonate 2-wall 78%         3.8       15–20 yr  Medium
  Polycarbonate 3-wall 68%         2.7       15–20 yr  Medium
  Polycarbonate 4-wall 60%         2.0       15–20 yr  Medium-high
  Single PE film     88%           6.5       3–5 yr    Very low
  Double PE film     78%           2.5       3–5 yr    Low
  ──────────────────────────────────────────────────────────────────
  U-value: W/m²K (lower = better insulation)

  DUTCH COMMERCIAL: Single or double glass. High light transmission
  valued above insulation (light = production in winter).
  COLD CLIMATES (N. America): Triple-wall polycarbonate for better
  insulation; accepts lower light for heating cost reduction.
  LOW-COST PRODUCTION: Double PE film tunnel houses: very low capital,
  low insulation, but adequate for spring/fall extension.
```

### Heating

```
HEATING SYSTEMS:
  Hot water (hydronic):
    Boiler heats water (80–90°C); circulates through pipes.
    Pipe positions: floor pipes (under benches or in floor),
                    high-pipe (perimeter/overhead heating).
    Advantages: even temperature distribution; adjustable zones;
               thermal mass (slower response but stable).
    Low-pipe (floor) heating: warm root zone; reduced heating demand
                               compared to overhead heating alone.

  Forced air:
    Unit heaters (gas or oil) with fans blow warm air into space.
    Fast response; lower capital than hydronic.
    Less even distribution; can create temperature gradients.

  Infrared (radiant):
    Long-wave radiant heaters above or beside plants.
    Heats surfaces (leaves, soil, paths) rather than air.
    Energy-efficient for heated benches in cold climates.
    Does not heat the air volume (most heat lost through glazing is from hot air).
    Good for frost protection; less suitable for temperature-controlled production.

HEATING CALCULATIONS:
  Heat loss = U-value × area × temperature differential
  For a greenhouse:
    Total U × area × (T_inside - T_outside) = heating requirement (W or BTU/hr)
  Plus: infiltration losses (air leaks) — typically 10–30% additional.
  Output: boiler or heater capacity required.
```

### Ventilation

```
NATURAL VENTILATION:
  Ridge vent + side wall vents (stack effect + wind-driven).
  HOT AIR RISES: opens at ridge → hot air exits.
                  cool air enters at sides.
  Area rule of thumb: ventilation area ≥ 25% of floor area.
  Works well in moderate climates; inadequate in hot humid summers.

MECHANICAL VENTILATION:
  Exhaust fans (negative pressure): pull air through house.
    Fans on one end; louvered inlet at other end.
    Airflow rate: 1 house volume change per minute (rough rule).
  Horizontal Air Flow (HAF) fans: not exhaust — circulate within space.
    Purpose: prevent temperature stratification; reduce disease.
    Run continuously; low energy.

EVAPORATIVE COOLING (pad-and-fan systems):
  Wet cellulose pads on one end; exhaust fans on other end.
  Hot outside air passes through wet pads → evaporation cools air.
  AT: temperatures drop 5–8°C (more in dry climates, less in humid).
  Used in hot dry regions (desert southwest US, Middle East, Spain).
  NOT effective in humid climates (already high humidity → little evaporation).

VPD (VAPOR PRESSURE DEFICIT) MANAGEMENT:
  VPD = water vapor pressure difference between inside leaf and air.
  High VPD (>1.5 kPa): too dry; plant stressed; high transpiration.
  Low VPD (<0.3 kPa): too humid; disease risk (botrytis, downy mildew).
  Target VPD: 0.5–1.0 kPa for most crops (varies by crop and light level).
  Management: heating (raises VPD — warm air holds more water), ventilation
              (removes humid air), fogging (lowers VPD), shade cloth.
```

### Supplemental Lighting

```
HIGH PRESSURE SODIUM (HPS):
  Standard greenhouse supplemental lighting until ~2015.
  Spectrum: broad, yellow-orange dominant. Good for most growth.
  Efficacy: 1.0–1.7 μmol/J (photosynthetically active photons per joule).
  Heat output: high — useful in winter; problem in summer.
  Lifespan: 12,000–20,000 hours.
  Color rendering: poor (sodium-yellow color).

LED (LIGHT-EMITTING DIODE):
  Now dominant for new installations.
  Spectrum: tunable — can specify ratio of red:blue:green:far-red.
  Red (640–680nm): most efficient for photosynthesis.
  Blue (450nm): required for stomatal opening, compact growth.
  Far-red (730nm): shade-avoidance response, extension growth, can
                   satisfy phytochrome requirement for some crops.
  Efficacy: 2.5–3.5 μmol/J (modern 2024 units) — significantly better than HPS.
  Heat output: less heat at canopy (heat goes to heatsinks, not to plants).
  Lifespan: 50,000+ hours.
  Capital cost: higher than HPS; falling rapidly.

DAILY LIGHT INTEGRAL (DLI):
  Total photosynthetically active radiation (PAR) received per day.
  Units: mol/m²/day.
  High-light crops (tomato, pepper): 20–30 mol/m²/day.
  Medium-light crops (lettuce, herbs): 12–17 mol/m²/day.
  Low-light crops (microgreens): 6–12 mol/m²/day.
  Northern Europe winter natural DLI: 1–4 mol/m²/day.
  Supplemental target: achieve at least minimum crop DLI.
```

---

## Hydroponic Systems

Hydroponics = growing plants in nutrient solution rather than soil:

```
HYDROPONIC SYSTEMS TAXONOMY:

  ┌────────────────────────────────────────────────────────────────┐
  │ NFT (Nutrient Film Technique)                                  │
  │ Thin film of nutrient solution flows continuously through      │
  │ shallow channels. Roots sit in channel; top half in air.       │
  │ + Very low water/solution volume; O₂ abundant.                │
  │ + Fast growth for leafy crops (lettuce, herbs, strawberry).    │
  │ - Power failure = immediate root drying and death.             │
  │ - Poor for fruiting crops (roots can't support heavy plant).   │
  └────────────────────────────────────────────────────────────────┘

  ┌────────────────────────────────────────────────────────────────┐
  │ DWC / RAFT / FLOATING RAFT                                     │
  │ Plants suspended in Styrofoam raft floating on deep solution.  │
  │ Roots hang into continuously aerated solution.                 │
  │ + Simplest system; very forgiving.                             │
  │ + Good for leafy greens at large scale.                        │
  │ - Disease (Pythium): spreads rapidly through shared solution.  │
  │ - Large water volume = slow temperature response.              │
  └────────────────────────────────────────────────────────────────┘

  ┌────────────────────────────────────────────────────────────────┐
  │ EBB-AND-FLOW (FLOOD-AND-DRAIN)                                │
  │ Tray flooded periodically; solution drains back to reservoir.  │
  │ + Good O₂ delivery (drains fully between floods).             │
  │ + Flexible (many substrates possible).                         │
  │ - Higher capital; complex plumbing.                            │
  └────────────────────────────────────────────────────────────────┘

  ┌────────────────────────────────────────────────────────────────┐
  │ DRIP (Dutch bucket / substrate)                                │
  │ Nutrient solution dripped to individual plants in substrate    │
  │ (rockwool, coco coir, perlite, clay pebbles).                 │
  │ + Good for tomato, cucumber, pepper (fruiting crops).          │
  │ + Easy to manage large individual plants.                      │
  │ - Waste if run-to-waste; recirculating requires management.    │
  └────────────────────────────────────────────────────────────────┘

  ┌────────────────────────────────────────────────────────────────┐
  │ AEROPONICS                                                      │
  │ Roots hang in air chamber; nutrient mist sprayed at intervals. │
  │ + Maximum O₂; rapid growth; lowest water use.                 │
  │ + Excellent for tissue culture acclimatization, R&D.           │
  │ - Very high capital and maintenance.                           │
  │ - Power/pump failure: roots dry in minutes.                    │
  └────────────────────────────────────────────────────────────────┘
```

---

## Nutrient Solution Management

```
NUTRIENT SOLUTION PARAMETERS:
  EC (Electrical Conductivity): proxy for total dissolved salt concentration.
    Measured in dS/m or mS/cm (same value).
    Low EC: low nutrient concentration (risk of deficiency).
    High EC: high salt; osmotic stress; may improve quality (concentrates flavor).
    Typical ranges:
      Lettuce: 1.2–2.0 dS/m
      Tomato: 2.5–4.0 dS/m (higher EC → smaller but higher Brix fruit)
      Strawberry: 1.5–2.5 dS/m

  pH: controls nutrient availability in solution (same pH principles as soil).
    Target: 5.5–6.5 for most crops (wider range than soil because no mineral
             buffering; solution needs pH control system).
    Adjust: add phosphoric acid (lower pH) or potassium hydroxide (raise pH).
    Drift: pH naturally rises as plants take up nutrients (prefer NO₃⁻,
           which releases OH⁻ into solution). Daily monitoring required.

  TEMPERATURE: root zone temperature matters.
    Optimal root zone: 18–22°C for most crops.
    Below 15°C: P and Fe uptake severely reduced.
    Above 25°C: O₂ dissolved in solution drops; root respiration increases;
                Pythium (root rot pathogen) flourishes.

RECIRCULATING VS. RUN-TO-WASTE:
  Recirculating: drain water collected, EC/pH adjusted, reused.
    + Zero waste.
    + Cost-effective for large systems.
    - Disease spread risk (Pythium, viruses in water).
    - Requires careful EC management (different crops take up nutrients at different ratios).

  Run-to-waste: drain water discarded.
    + Simple; lower disease risk.
    - Water/fertilizer waste (typically 20–30% drain fraction).
    - Regulatory issue in Netherlands (discharge prohibited) → mandatory recirculation.
```

---

## Vertical Farming

Vertical farms stack multiple growing layers in climate-controlled buildings, relying entirely on LED lighting:

```
VERTICAL FARM ARCHITECTURE:
  +------------------+  Layer N (top)   LED above
  |  growing layer   |
  +------------------+
  +------------------+  Layer N-1
  |  growing layer   |
  +------------------+
  +------------------+  Layer N-2
  |  growing layer   |
  +------------------+
  ...
  +------------------+  Layer 1 (bottom)
  |  growing layer   |
  +------------------+

  CROPS: Primarily leafy greens (lettuce, spinach, arugula, kale,
         basil, herbs) and microgreens.
         Not fruiting crops (tomato, cucumber): insufficient light
         intensity from LEDs at current cost to support fruiting yields.

THE ENERGY ECONOMICS (the central problem):
  Natural sunlight is free.
  LEDs must replace sunlight.
  Cost of LED electricity to replace full-sun photosynthesis:
    Full sun (1,000 W/m²) × 8 hours = 8 kWh/m²/day
    LED efficacy ~3 μmol/J; target DLI for lettuce ~17 mol/m²/day
    Electricity needed: ~17,000,000 μmol / 3 μmol/J / 3,600 s/h = ~1.6 kWh/m²/day
    At $0.10/kWh: $0.16/m²/day just for lighting.
    At 40-day crop cycle: $6.40/m² of lighting cost.
    Add: HVAC (significant), labor, depreciation, nutrient.
    Typical total production cost (lettuce): $3–8/head in VF.
    Retail price required: $5–15/head.
    Compare: field lettuce: $0.30–0.80/head production cost.

WHY VERTICAL FARMS EXIST DESPITE HIGH COST:
  Urban location proximity: ultra-fresh (hours from harvest to consumer).
  Year-round reliability: no weather disruption.
  No pesticides required (closed environment).
  Water efficiency: ~95% reduction vs. field production.
  Geographic: Japan, Singapore, Middle East (no viable field land; high import cost).
  Premium segment: willingness to pay for local, pesticide-free, ultra-fresh.

ENERGY TREND:
  LED efficacy improving ~10%/year.
  Renewable electricity costs falling.
  At $0.03/kWh (wind/solar) + 4 μmol/J LEDs:
  Cost drops ~60% from current levels.
  Economic viability for more crops approaches as these improve.
```

---

## Climate Computer Control

Modern commercial greenhouses use climate computer systems that integrate sensing and actuation:

```
CONTROLLED VARIABLES:
  Temperature (air and root zone)
  Humidity / VPD
  CO₂ concentration
  Light (DLI accumulation; supplemental light switching)
  Irrigation (volume, frequency, based on plant stage and transpiration)
  Nutrient solution EC and pH
  Heating setpoint (day vs. night)

SENSORS:
  Temperature/RH: psychrometer or capacitive RH sensor.
    Multiple locations in house (spatial variation matters).
  CO₂: NDIR (non-dispersive infrared) sensors.
    Calibrate regularly — NDIR drifts.
  Radiation: PAR sensor (quantum sensor) or solarimeter.
    Used for DLI calculation; supplemental light control.
  Tensiometers / mat sensors: substrate moisture (irrigation trigger).
  EC/pH probes: in drain water or nutrient solution tank.
  Weight sensors (lysimeters): weigh small group of plants.
    Transpiration = weight loss before next irrigation event.
    Precision irrigation scheduling based on actual plant water use.

DIF (DIFFERENCE BETWEEN DAY AND NIGHT TEMPERATURE):
  Positive DIF: day temp > night temp (normal).
    Results in: taller, more elongated plants.
  Negative DIF: day temp < night temp.
    Results in: shorter, compact plants.
    Used for: floriculture height control (compact bedding plants, poinsettia).
  Mechanism: temperature affects rate of internode elongation, which
             peaks in morning during rapid growth.
  PRACTICAL: many greenhouses run a brief cool period at dawn
             (the "negative DIF period") rather than cooling all day —
             achieves height control without excessive heating cost.
```

---

## Decision Cheat Sheet

| Crop | System | Target EC | DLI | Key Management |
|------|--------|-----------|-----|----------------|
| Lettuce/leafy greens | NFT or DWC raft | 1.2–2.0 dS/m | 12–17 mol/m²/day | Pythium management; temperature |
| Tomato | Dutch bucket drip | 3.0–4.0 dS/m | 20–30 mol/m²/day | Pruning, trellising, pollination |
| Strawberry | NFT or substrate | 1.5–2.5 dS/m | 15–20 mol/m²/day | Runner removal; chilling for dormancy break |
| Basil/herbs | NFT | 1.0–1.8 dS/m | 12–18 mol/m²/day | Bolting management (temperature + photoperiod) |
| Microgreens | Tray on media | Minimal | 6–12 mol/m²/day | Density; humidity management; harvest timing |

| Problem | Likely Cause | Solution |
|---------|-------------|---------|
| Tipburn (lettuce) | Ca delivery failure (low transpiration) | Increase air movement; lower VPD; Ca in nutrient solution |
| Root rot (Pythium) | Warm, low-O₂ solution | Cool solution; improve aeration; H₂O₂ treatment; trichoderma |
| Interveinal chlorosis | Fe or Mn deficiency at high pH | Lower pH to 5.8–6.0; chelated Fe/Mn |
| Leggy plants | Insufficient light or high DIF | Increase DLI; use negative DIF period |
| Blossom drop (tomato) | Low humidity, high VPD, low temp | Manage VPD 0.5–1.0 kPa; gentle vibration for pollination |

---

<!-- @editor[bridge/P2]: Missing explicit control-systems bridge — this file describes a SCADA-like architecture (sensors, actuators, setpoints, PID loops) without naming it. For this learner with engineering background, explicitly framing the climate computer as an industrial control system with VPD/temperature/CO2 as controlled variables would be a high-value bridge -->
## Common Confusion Points

**Hydroponics is not soil-free nutrition magic**: the plant biology is the same. Roots still require O₂, appropriate temperature, and the same mineral nutrients. Hydroponics provides precise delivery of what the plant needs but does not override plant physiology.

**VPD is not the same as relative humidity**: RH 80% at 15°C has very different VPD than RH 80% at 25°C. VPD is the absolute driving force for transpiration; RH is relative. CEA management uses VPD; quoting only RH is insufficient.

**Vertical farming is not economically viable for all crops yet**: the energy and capital cost structure of vertical farming limits economic viability to premium segments and specific geographies. Tomatoes, cucumbers, and peppers are generally not economically viable in vertical farms in 2025 compared to Dutch-style greenhouse production. Leafy greens in urban locations is the proven economic model.

**CO₂ enrichment has diminishing returns**: increasing CO₂ from 400ppm to 1000ppm in a closed greenhouse increases photosynthesis significantly at adequate light. But if light is the limiting factor (winter greenhouse), CO₂ enrichment has minimal effect. Check light first.

**Recirculating systems require active disease management**: unlike run-to-waste, a recirculating system can propagate waterborne pathogens (Pythium, viruses) through the entire crop via the shared solution. Ultraviolet sterilization of the recirculating solution is standard practice in large commercial operations to prevent this.
