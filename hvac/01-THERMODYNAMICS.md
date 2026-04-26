# HVAC Thermodynamics & Load Calculation

## The Big Picture

Before selecting any equipment, you need to know the load — how many BTU/hr must be
moved under design conditions. That requires understanding how heat moves through the
building envelope and what drives that movement.

```
+----------------------------------------------------------------------+
|               HEAT TRANSFER IN THE BUILDING ENVELOPE                 |
|                                                                      |
|  CONDUCTION             CONVECTION              RADIATION            |
|  (through solids)       (via fluid movement)    (EM transmission)    |
|                                                                      |
|  Wall, roof, floor      Air leakage (infil.)    Sun through glass    |
|  Window frame           Forced air at surface   Night sky radiation  |
|  Thermal bridging       Natural convection      Radiant floor        |
|                                                                      |
|  Q = kA∆T/L            Q = h·A·∆T              Q = ε·σ·A·T⁴          |
|  Fourier's law          Newton's law of          Stefan-Boltzmann    |
|                         cooling                                      |
+----------------------------------------------------------------------+
         |                    |                    |
         v                    v                    v
    All three contribute to "load" — the total BTU/hr demand
```

---

## Section 1: Three Modes of Heat Transfer

### Carnot Bounds — The Thermodynamic Ceiling

Before heat transfer modes: the Carnot efficiency sets the theoretical maximum for any heat-moving device. All temperatures in Kelvin.

```
HEAT ENGINE (rare in HVAC — absorption chillers use this):
  η_Carnot = 1 − T_cold/T_hot

REFRIGERATION (AC, chillers):
  COP_max = T_cold / (T_hot − T_cold)

HEAT PUMP (heating mode):
  COP_max = T_hot / (T_hot − T_cold)

WHY COP > 1 IS PHYSICAL:
  You are moving heat, not creating it. The work input moves Q_cold
  from inside to outside. Total heat rejected Q_hot = Q_cold + W.
  COP = Q_cold/W. Since Q_cold > 0 and W < Q_cold + Q_hot, COP > 1.

PRACTICAL EXAMPLE:
  AC cooling to 45°F (280K), outdoor 95°F (308K):
  COP_max = 280/28 = 10.0    Real equipment: COP 3–5 (30–50% of Carnot)

  Heat pump heating to 70°F (294K), outdoor 20°F (266K):
  COP_max = 294/28 = 10.5    Real ASHP: COP 2–3 (20–30% of Carnot)

  WHY PERFORMANCE DEGRADES:
  COP_max ∝ 1/ΔT. As outdoor T rises (cooling) or falls (heating),
  ΔT increases → COP_max drops → equipment works harder per BTU moved.
```

### Conduction

Heat flows through a solid from high-temperature to low-temperature regions. Rate is
proportional to thermal conductivity (k), area, and temperature difference; inversely
proportional to thickness.

```
  Q = k · A · ΔT / L

  k = thermal conductivity (BTU·in / hr·ft²·°F)
  A = area (ft²)
  ΔT = temperature difference (°F)
  L = thickness (inches)

  Material conductivities (approximate):
  +--------------------------+------------------+
  | Material                 | k (BTU·in/hr·ft²·°F) |
  +--------------------------+------------------+
  | Copper                   | 2,900            |
  | Steel                    | 314              |
  | Concrete                 | 5–12             |
  | Brick                    | 5–9              |
  | Wood (fir)               | 0.8              |
  | Fiberglass batt          | 0.26             |
  | Spray foam (closed cell) | 0.14             |
  | Air (still)              | 0.18             |
  +--------------------------+------------------+
```

### Convection

Heat transfer via fluid movement. **Natural convection**: buoyancy-driven (warm air rises).
**Forced convection**: fan or pump-driven. HVAC primarily uses forced convection — the blower
moves air over the heat exchanger coil. ERV/HRV use air-to-air forced convection.

### Radiation

Electromagnetic transmission — no medium required. Solar radiation through windows is the
dominant radiation load in HVAC. Radiant floor heating warms occupants via infrared radiation
(long-wavelength) without heating intervening air. Night sky radiation causes unconditioned
roofs to lose heat to the cold sky even when outdoor air temp is moderate.

---

## Section 2: R-Value and U-Factor

The engineering abstraction that makes envelope calculations manageable:

```
  R-VALUE (thermal resistance)             U-FACTOR (thermal conductance)
  ================================         ================================
  R = L / k  (thickness / conductivity)   U = 1 / R  (inverse of R)

  Units: ft²·°F·hr / BTU                  Units: BTU / hr·ft²·°F

  HIGHER R = better insulator             LOWER U = better insulator
  Used for: insulation, wall assemblies   Used for: windows (industry standard)

  Q = U · A · ΔT  (heat flow through assembly)
  Q = ΔT / R      (same thing, different form)
```

### R-Values in Series (Wall Assembly)

A wall is multiple layers in series — their R-values add:

```
  Typical 2×6 wood-framed wall assembly (cavity R-21 fiberglass):
  +-----------+---------------------------+--------+
  | Layer     | Material                  | R-value|
  +-----------+---------------------------+--------+
  | Exterior  | Vinyl siding              | 0.61   |
  | Sheathing | OSB (7/16")               | 0.62   |
  | Cavity    | Fiberglass batt (R-21)    | 21.0   |
  | Drywall   | 1/2" gypsum               | 0.45   |
  | Air films | Interior + exterior       | 0.85   |
  +-----------+---------------------------+--------+
  | TOTAL     |                           | 23.5   |
  +-----------+---------------------------+--------+

  But studs (wood, R~1.25/inch) short-circuit the cavity:
  Effective whole-wall R ≈ 18 (thermal bridging through framing)
  → Steel studs are far worse (high conductivity → R drops to ~7)
```

### IECC Minimum R-Values by Climate Zone

```
  Zone  Description          Wall (cavity) Ceiling  Window U
  ----  -----------          ------------- -------  --------
  1     Hot/humid (Miami)    13            30       0.50
  2     Hot/humid (Houston)  13            38       0.40
  3     Mixed (Atlanta)      13            38       0.35
  4     Mixed (Seattle, DC)  13+5ci or 20  49       0.32
  5     Cold (Chicago)       13+5ci or 20  49       0.30
  6     Very cold (Minneapolis) 13+10ci or 20+5ci  49  0.30
  7     Subarctic (Fairbanks) 13+10ci or 20+5ci    60  0.27
  ci = continuous insulation (outside stud framing, eliminates thermal bridging)
```

---

## Section 3: BTU — The Currency of HVAC

```
  1 BTU (British Thermal Unit) = heat to raise 1 lb water by 1°F

  UNIT EQUIVALENCES:
  1 ton of cooling     = 12,000 BTU/hr
  1 therm (gas billing)= 100,000 BTU
  1 kWh (electricity)  = 3,412 BTU
  1 watt (power)       = 3.412 BTU/hr

  GAS PRICE COMPARISON EXAMPLE:
  Gas at $1.20/therm:   $1.20 / 100,000 BTU = $0.000012/BTU
  Electric at $0.15/kWh: $0.15 / 3,412 BTU = $0.000044/BTU
  Ratio: electricity ~3.7× more expensive per BTU (offsets for heat pumps by COP)
```

---

## Section 4: Psychrometrics

The thermodynamics of moist air. Critical for understanding cooling loads and
dehumidification — the "latent" half of the load that most people ignore.

```
                    PSYCHROMETRIC PROPERTIES
                    ========================

  DRY-BULB TEMPERATURE (Tdb)
  └── What a regular thermometer reads
  └── "Temperature" in everyday speech

  WET-BULB TEMPERATURE (Twb)
  └── Evaporative cooling effect
  └── Lower than dry-bulb (except at 100% RH where Twb = Tdb)
  └── Encodes both temperature AND moisture content

  DEW POINT (Tdp)
  └── Temperature at which moisture condenses
  └── AC coil must be below dew point to dehumidify
  └── When Tdp < Tdb: condensation occurs on coil surface

  RELATIVE HUMIDITY (RH%)
  └── Ratio of actual moisture to maximum possible at that temp
  └── 100% RH = air can hold no more moisture (saturation)
  └── Human comfort: 30–60% RH

  HUMIDITY RATIO (W)
  └── lbs of water vapor per lb of dry air
  └── Doesn't change with temperature (unlike RH%)
  └── What matters for latent load calculation

  ENTHALPY (h)
  └── Total heat content = sensible + latent (BTU/lb dry air)
  └── h = 0.240 × Tdb + W × (1061 + 0.444 × Tdb)
  └── Enthalpy difference × airflow = total cooling capacity
```

### Sensible Heat Ratio (SHR)

```
  SHR = sensible cooling / total cooling

  SHR = 0.80: typical northern US home
  SHR = 0.70: hot/humid climate (more latent load)

  WHY IT MATTERS:
  AC coils are designed with a specific SHR.
  Oversized equipment → short cycles → coil doesn't stay cold long enough
  → moisture not removed → high RH despite thermostat set low
  → "cool and clammy" feeling

  Right-sizing for latent load = humidity control = comfort
```

---

## Section 5: Manual J Load Calculation

The correct way to size HVAC equipment. Rules of thumb ("400 sq ft per ton") are not
substitutes — they routinely produce 30-50% oversized equipment.

```
  MANUAL J INPUTS:
  ┌─────────────────────────────────────────────────────────┐
  │ Building geometry: floor plan, orientation, ceiling heights
  │ Insulation: R-values per assembly (wall, ceiling, floor)  │
  │ Windows: U-factor, SHGC, area by orientation            │
  │ Infiltration: ACH50 from blower door (or assumed)       │
  │ Outdoor design conditions: ASHRAE 99%/1% by city        │
  │ Indoor setpoints: 70°F heating, 75°F cooling            │
  │ Internal gains: occupants, lighting, equipment          │
  └─────────────────────────────────────────────────────────┘
                           |
                           v
  SOFTWARE: Wrightsoft, Elite CHVAC, CoolCalc
                           |
                           v
  MANUAL J OUTPUTS:
  ┌─────────────────────────────────────────────────────────┐
  │ Room-by-room sensible heating load (BTU/hr)             │
  │ Room-by-room sensible cooling load (BTU/hr)             │
  │ Room-by-room latent cooling load (BTU/hr)               │
  │ Total building peak loads → equipment sizing target     │
  │ Airflow per room (CFM) → input to Manual D duct sizing  │
  └─────────────────────────────────────────────────────────┘
```

### Heating Load Components

```
  HEATING LOAD CALCULATION:
  Design outdoor temp = 99% heating design day (city-specific)
  Example: Chicago = -4°F; Dallas = 21°F; Miami = 44°F

  Component              Formula
  ---------              -------
  Envelope conduction    U × Area × ΔT (each assembly)
  Infiltration           0.018 × CFM_infil × ΔT
  Slab edge loss         F × perimeter (BTU/hr·ft)

  Note: NO credit for solar gains or internal gains in heating
  (conservative — design for worst case, solar not guaranteed)
```

### Cooling Load Components

```
  COOLING LOAD is more complex (time-dependent):

  Solar gain through glass:
    = SHGC × Area × Peak Solar Intensity × CLF
    (CLF = cooling load factor, accounts for thermal lag)
    South windows: peak in December (low sun angle, direct)
    West windows:  peak in afternoon

  Envelope conduction: uses CLTD (Cooling Load Temperature Differential)
    CLTD accounts for thermal mass lag — heavy walls absorb heat,
    re-release it hours later (peak indoor impact ≠ peak outdoor temp)

  Internal gains:
    People: 250 BTU/hr sensible + 200 BTU/hr latent per person
    Lighting: 3.41 BTU/hr per watt
    Appliances: varies; refrigerator ~400 BTU/hr, computers ~300 BTU/hr
```

---

## Section 6: Infiltration and the Tight Building Dilemma

```
  OLD LEAKY HOUSE (>10 ACH50):
  - Sufficient natural infiltration for IAQ
  - BUT: large infiltration load (conditioning all that leakage air)
  - Energy waste is massive

  MODERN TIGHT HOUSE (<3 ACH50):
  - Dramatically reduced infiltration load
  - BUT: insufficient natural air exchange for IAQ
  - MUST add mechanical ventilation (ASHRAE 62.2)

  BLOWER DOOR TEST:
  - Depressurizes house to 50 Pa (0.2 inches water)
  - Measures CFM50 (air leakage at 50 Pa)
  - ACH50 = (CFM50 × 60) / building volume
  - Energy Star: <7 ACH50; DOE Zero Energy Ready: <3 ACH50; Passive House: <0.6

  INFILTRATION LOAD (sensible):
  Q = 0.018 × CFM × ΔT
  (0.018 = volumetric heat capacity of air BTU/ft³·°F)

  At 3 ACH50, natural infiltration ≈ 0.05 ACH at normal conditions
  → way below the 0.15–0.35 ACH needed for IAQ
  → mechanical ventilation required
```

---

## Decision Cheat Sheet

| I need to... | Method/Tool |
|---|---|
| Size equipment for new construction | Full Manual J (software) |
| Size equipment for replacement | Manual J with blower door data |
| Calculate R-value of wall assembly | Sum R-values of all layers in series |
| Understand window energy performance | U-factor (conductance) + SHGC (solar gain) |
| Determine dehumidification need | SHR — sensible heat ratio of building load |
| Size ductwork after load calc | Manual D (input: CFM per room from Manual J) |
| Know design outdoor temperature | ASHRAE fundamentals by city (99%/1% values) |
| Measure building airtightness | Blower door test → ACH50 |

---

## Common Confusion Points

**R-value adds for series, not parallel**: wall studs and cavity insulation are
in parallel (heat chooses the easier path). You can't just use the cavity R-value —
the studs short-circuit it. This is thermal bridging; effective whole-wall R is lower.

**U-factor and R-value are inverses**: R=20 insulation has U=0.05. Windows are always
specified in U-factor (lower = better). Walls are in R-value (higher = better).
Confusion is universal. Just remember: for windows, go low; for insulation, go high.

**SHGC vs. U-factor for windows**: SHGC (Solar Heat Gain Coefficient) = fraction of
solar radiation that passes through. South windows in cold climates want HIGH SHGC
(free solar heating). West windows want LOW SHGC (avoid afternoon overheating). U-factor
controls conductive loss — want low everywhere.

**Latent load is not on the thermostat**: a space can be 75°F (thermostat satisfied)
and 75% RH (miserable, mold risk). The thermostat only tracks dry-bulb temperature.
Oversized equipment makes this worse. Dedicated dehumidifiers or properly-sized
variable-speed equipment are the solutions.
