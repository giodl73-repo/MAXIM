# The Refrigeration Cycle

## The Big Picture

Refrigeration doesn't create cold — it moves heat from where you don't want it
to where you don't mind it. This distinction is fundamental: you're not removing
cold from a room, you're removing heat from it. The vapor compression cycle is
the mechanism that makes this practical.

```
+----------------------------------------------------------------------+
|                  VAPOR COMPRESSION CYCLE                              |
|                                                                      |
|  INDOOR UNIT                          OUTDOOR UNIT                   |
|  (EVAPORATOR in cooling mode)         (CONDENSER in cooling mode)    |
|                                                                      |
|  ┌─────────────┐                      ┌─────────────┐               |
|  │ Low pressure│                      │High pressure│               |
|  │ Low temp    │                      │ High temp   │               |
|  │ Refrigerant │                      │ Refrigerant │               |
|  │ boils at 40°F                      │ condenses   │               |
|  │ Absorbs heat│                      │ at ~100°F   │               |
|  │ from room air                      │ Rejects heat│               |
|  │ Dehumidifies│                      │ to outdoor  │               |
|  └──────┬──────┘                      └──────┬──────┘               |
|         │                                    │                       |
|         │ Low-pressure vapor                 │ High-pressure liquid  |
|         │                                    │                       |
|     ┌───┴────┐                          ┌────┴────┐                  |
|     │COMPRESS│◄─────── WORK IN ─────────│EXPANSION│                  |
|     │  -OR   │                          │  VALVE  │                  |
|     └────────┘                          └─────────┘                  |
|     Raises pressure                     Drops pressure               |
|     and temperature                     (throttling)                 |
+----------------------------------------------------------------------+

  Heat flows: Room heat → refrigerant → outdoor air
  Work input: Compressor electricity
  COP: 3.0 → 3 BTU of heat moved per 1 BTU of work
```

---

## Section 1: The Four Steps

### Step 1: Evaporation (Indoor Coil — Cooling Mode)

```
  Low-pressure liquid refrigerant enters evaporator coil
                    |
                    v
  Pressure is low → boiling point is low (~40°F for R-410A)
                    |
                    v
  Room air (70°F) blows across coil → air is warmer than boiling refrigerant
                    |
                    v
  Refrigerant ABSORBS heat of vaporization from room air
  (boiling absorbs ~100 BTU/lb for typical refrigerants)
                    |
                    v
  Refrigerant exits as low-pressure vapor
  Room air exits: cooler + drier (moisture condenses on cold coil → condensate drain)

  KEY: The latent heat of vaporization is massive compared to sensible heat
  → That's why refrigerants work: phase change carries enormous energy per lb
```

### Step 2: Compression

```
  Compressor receives low-pressure vapor
               |
               | Work input (electricity)
               v
  Raises pressure AND temperature of refrigerant
  (ideal: isentropic compression; real: slightly less efficient)
               |
               v
  Exits as high-pressure, high-temperature vapor
  (e.g., R-410A: ~400 PSIA, 130–150°F at compressor outlet)

  COMPRESSOR TYPES:
  ┌──────────────┬────────────────────────────────────────────────────┐
  │ Type         │ Notes                                              │
  ├──────────────┼────────────────────────────────────────────────────┤
  │ Reciprocating│ Piston — older, simple, loud; small commercial     │
  │ Scroll       │ Two interlocking spirals; dominant residential;    │
  │              │ quieter, more efficient, fewer moving parts        │
  │ Rotary       │ Mini-splits; quiet, compact                        │
  │ Screw        │ Two helical rotors; medium commercial              │
  │ Centrifugal  │ Large commercial chillers (>100 ton)              │
  ├──────────────┼────────────────────────────────────────────────────┤
  │ Variable-speed (inverter-driven): DC motor, continuously modulates │
  │ 25–120% capacity; dominant in modern heat pumps and mini-splits   │
  └──────────────┴────────────────────────────────────────────────────┘
```

### Step 3: Condensation (Outdoor Coil — Cooling Mode)

```
  High-pressure, high-temperature vapor enters condenser coil
               |
               v
  Outdoor air (~90°F) blows across coil
  Refrigerant at high pressure has high condensing temp (~110°F)
  → refrigerant is hotter than outdoor air → heat flows out
               |
               v
  Refrigerant RELEASES heat to outdoor air (heat of condensation)
  Fan rejects this heat to atmosphere
               |
               v
  Exits as high-pressure liquid

  Heat rejected = heat absorbed in evaporator + compressor work
  Q_condenser = Q_evaporator + W_compressor
  (Energy conservation — must account for the work input)
```

### Step 4: Expansion

```
  High-pressure liquid enters expansion device
               |
  Throttling through small orifice or valve
               |
               v
  Pressure drops sharply (no heat exchange — throttling process)
  Temperature drops (Joule-Thomson effect in real fluids)
  Partial flash to vapor (wet mixture at low pressure)
               |
               v
  Low-pressure, low-temperature liquid/vapor mixture
  Ready to enter evaporator

  EXPANSION DEVICES:
  ┌──────────────────┬──────────────────────────────────────────────────┐
  │ Fixed orifice /  │ Simple; one optimum operating point; used in     │
  │ piston           │ older/cheaper equipment                           │
  ├──────────────────┼──────────────────────────────────────────────────┤
  │ TXV (Thermal     │ Modulates to maintain fixed superheat at evap     │
  │ Expansion Valve) │ outlet; bulb senses evap outlet temp + pressure  │
  │                  │ → adjusts opening; better over range of loads    │
  ├──────────────────┼──────────────────────────────────────────────────┤
  │ EEV (Electronic  │ Stepper motor; electronic control; optimal for   │
  │ Expansion Valve) │ variable-speed systems; adjusts continuously      │
  └──────────────────┴──────────────────────────────────────────────────┘
```

---

## Section 2: The P-H (Pressure-Enthalpy) Diagram

The Mollier diagram for refrigerants — the fundamental tool for refrigeration analysis.

```
  PRESSURE-ENTHALPY (MOLLIER) DIAGRAM
  ====================================

  P (pressure)
  |          Saturation dome
  |        /                 \
  |       /    Two-phase      \
  |      /     (liquid+vapor)  \
  |     /                       \     ← Subcooled
  |    /                         \      liquid
  |---/---------------------------\------- region
  |  3         1 & 2              4
  |
  +-------------------------------------------> h (enthalpy BTU/lb)

  Point 1: Evaporator inlet — low pressure, wet mixture
  Point 2: Evaporator outlet — low pressure, saturated vapor (or slightly superheated)
  Point 3: Compressor outlet — high pressure, superheated vapor
  Point 4: Condenser outlet — high pressure, subcooled liquid

  Process 2→3: Compression (vertical on P-H diagram for ideal isentropic)
  Process 3→4: Condensation (horizontal at high pressure)
  Process 4→1: Throttling (vertical drop — constant enthalpy, isenthalpic)
  Process 1→2: Evaporation (horizontal at low pressure)

  REFRIGERATING EFFECT = h₂ - h₁ (enthalpy absorbed in evaporator)
  COMPRESSOR WORK = h₃ - h₂ (enthalpy rise during compression)
  COP = (h₂ - h₁) / (h₃ - h₂)
```

---

## Section 3: Superheat and Subcooling

These are the diagnostic measurements technicians use to verify proper system operation
and refrigerant charge. If you can measure superheat and subcooling, you can diagnose
most refrigerant charge and airflow problems.

### Superheat

```
  SUPERHEAT = Evaporator outlet temperature MINUS saturation temperature
              at suction pressure

  Example:
  - Suction pressure (low-side gauge): 76 PSIG for R-410A
  - Saturation temperature at 76 PSIG: 40°F (from PT chart)
  - Actual vapor temperature at evaporator outlet: 55°F
  - Superheat = 55 - 40 = 15°F  ← target 8–15°F

  WHY IT MATTERS:
  Too low (0–5°F): liquid refrigerant may reach compressor → liquid slugging
                   → compressor damage (liquids don't compress)
  Too high (>20°F): low capacity, high discharge temp, compressor overheats
  Target 8–15°F: ensures dry vapor entering compressor with some margin

  SUPERHEAT DIAGNOSTIC:
  High superheat + low suction pressure = LOW refrigerant charge (leak)
  High superheat + normal pressure      = restricted metering device
  Low superheat                         = overcharged or low airflow across evaporator
```

### Subcooling

```
  SUBCOOLING = Condensation temperature MINUS actual liquid temperature
               at condenser outlet

  Example:
  - Discharge pressure: 410 PSIG for R-410A
  - Saturation temperature at 410 PSIG: 110°F (from PT chart)
  - Actual liquid temperature at condenser outlet: 95°F
  - Subcooling = 110 - 95 = 15°F  ← target 10–15°F

  WHY IT MATTERS:
  Ensures only liquid (no vapor) enters expansion device.
  Too little subcooling → flash gas before expansion valve → reduced capacity
  Too much subcooling → overcharged system → high head pressure

  SUBCOOLING DIAGNOSTIC:
  Low subcooling + high superheat = UNDERCHARGED
  High subcooling                 = OVERCHARGED
```

---

## Section 4: Efficiency Metrics

The theoretical ceiling for COP is the Carnot bound: COP_max = T_cold / (T_hot - T_cold) for cooling (temperatures in Kelvin). At 45F/95F conditions: COP_max = 280/28 = 10.0. Real equipment achieves COP 3-5, i.e., 30-50% of Carnot efficiency. The gap comes from compressor irreversibilities, heat exchanger temperature differences, and expansion losses. COP drops as delta-T increases: on a 110F day, COP_max falls to 280/(316-280) = 7.8, and real equipment drops proportionally. "COP = 3.0 means 300% efficiency" is physically meaningful — you are moving heat, not creating it — but it has a thermodynamic ceiling.

```
  METRIC     DEFINITION                              UNITS    TYPICAL
  ------     ----------                              -----    -------
  COP        Heat moved / work input                 ratio    2.5–5.0
             Thermodynamic. Used for heat pumps.
             COP = 3.0 → 300% "efficiency"

  EER        BTU/hr cooling / watts input            BTU/W·hr 10–15
             At fixed ARI conditions (95°F outdoor,
             80°F/67°F indoor). Instantaneous.

  SEER       Seasonal integrated EER                 BTU/W·hr 14–26
  (legacy)   Weighted over cooling season.
             Replaced by SEER2 Jan 2023.

  SEER2      SEER under new 2023 DOE test procedure  BTU/W·hr 13–26
             Higher external static pressure test.
             ~4–7% lower number vs same equipment.
             DO NOT compare old SEER to SEER2 directly.

  HSPF       Seasonal heating performance (heat pump) BTU/W·hr ~8–10
  (legacy)   Heating BTU / watt-hours over season.

  HSPF2      HSPF under 2023 test procedure.        BTU/W·hr ~7.5–14
             Lower outdoor test temp; more realistic.

  EER2       EER under 2023 test procedure.          BTU/W·hr similar
```

### Efficiency vs. Temperature (Heat Pumps)

```
  COP of Air-Source Heat Pump vs Outdoor Temperature (Heating Mode):

  Outdoor Temp:  -10°F   0°F   10°F  20°F  30°F  40°F  50°F
  Standard ASHP:   ---   ---   1.5   1.8   2.1   2.5   3.0
  Cold-Climate:    1.5   2.0   2.4   2.7   3.1   3.5   4.0

  Gas furnace equivalent COP: 0.8 (80% AFUE) to 0.98 (98% AFUE)
  → Heat pump is more efficient down to ~-10°F (cold-climate models)
  → Even at 0°F, a cold-climate heat pump at COP 2.0 delivers
    2× the heat per dollar as a 96% gas furnace (at equivalent energy prices)
```

---

## Section 5: Variable-Speed / Inverter-Driven Systems

Single-stage vs two-stage vs variable-speed — the biggest quality-of-life distinction
in modern HVAC:

```
  SINGLE-STAGE:         TWO-STAGE:            VARIABLE-SPEED:
  ┌───────────────┐     ┌───────────────┐     ┌───────────────┐
  │ 100% or OFF   │     │ 65% or 100%   │     │ 25% to 120%   │
  │               │     │ (or OFF)      │     │ continuously  │
  │ Short cycles  │     │ Less cycling  │     │ Very long runs│
  │ Poor dehumid  │     │ Better dehumid│     │ Best dehumid  │
  │ Hot/cold swings     │ More stable   │     │ Stable temps  │
  │ Cheap upfront │     │ Higher cost   │     │ Most expensive│
  │ SEER2 ~14-15  │     │ SEER2 ~16-18  │     │ SEER2 ~20-30  │
  └───────────────┘     └───────────────┘     └───────────────┘
```

Variable-speed (inverter-driven) systems are what make cold-climate heat pumps
viable — the compressor runs at very high speed in extreme cold, low speed in
mild weather, matching load at all conditions.

---

## Decision Cheat Sheet

| Question | Answer |
|---|---|
| Why does refrigeration work thermodynamically? | Latent heat of vaporization moves huge energy; phase change at controllable pressure |
| What does the compressor do? | Creates pressure differential enabling phase change at useful temperatures |
| How do you know if charge is correct? | Measure superheat (TXV systems use subcooling method) |
| Low suction pressure + high superheat means? | Refrigerant undercharge (leak) |
| High suction pressure + low superheat means? | Overcharge or poor airflow across evaporator coil |
| SEER2 vs old SEER — same equipment? | Yes — same efficiency, harder test conditions, lower number |
| Why does COP > 1 not violate thermodynamics? | Heat pumps move heat; they don't create it. Work moves more heat than the work itself |

---

## Common Confusion Points

**Heat pump in heating mode**: the refrigerant cycle reverses. Outdoor unit becomes
the evaporator (extracts heat from cold outdoor air), indoor unit becomes the condenser
(releases heat indoors). The reversing valve (four-way valve) switches refrigerant flow
direction. Same compressor, same coils — just reversed role assignment.

**Liquid slugging**: refrigerant liquid reaching the compressor pistons or scrolls.
Liquids don't compress. This is why superheat must stay positive — ensure all
refrigerant is vapor before reaching the compressor. This is why low superheat is dangerous.

**COP vs SEER**: COP is a thermodynamic ratio at a single operating point. SEER is a
seasonal integrated metric (many operating hours at varying conditions). COP 3.5 at 95°F
translates to roughly SEER 14 (older test). They're measuring the same thing, different scope.

**Compressor as the expensive part**: the compressor is the heart of the system and the
most expensive single component. Liquid slugging, operating without proper refrigerant
charge (too high or too low), running with poor airflow — all lead to compressor failure.
Refrigerant charge must be precise to within a few ounces.
