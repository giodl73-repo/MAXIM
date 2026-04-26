# Heat Pumps

## The Big Picture

A heat pump is a refrigeration system with a reversing valve. In cooling mode it's an
air conditioner. In heating mode it runs the refrigerant cycle backwards — extracting
heat from outdoor air and delivering it indoors. The critical insight: you're not
creating heat, you're moving it. Moving heat requires less work than creating it.

```
+----------------------------------------------------------------------+
|                    HEAT PUMP OPERATING MODES                         |
|                                                                      |
|  COOLING MODE (Summer)          HEATING MODE (Winter)                |
|  -----------------------        -----------------------              |
|  Indoor coil = EVAPORATOR       Indoor coil = CONDENSER              |
|  Absorbs heat from room         Releases heat to room                |
|  Cools + dehumidifies           Warms the space                      |
|                                                                      |
|  Outdoor coil = CONDENSER       Outdoor coil = EVAPORATOR            |
|  Rejects heat to outside        Absorbs heat from outdoor air        |
|                                                                      |
|                    REVERSING VALVE switches direction                |
|                    (four-way valve in refrigerant circuit)           |
|                                                                      |
|  COP (cooling): 3–5             COP (heating): 2–4 at 47°F           |
|  = more efficient than AC       = more efficient than gas furnace    |
|    vs. gas furnace (COP < 1)    in most conditions                   |
+----------------------------------------------------------------------+
```

---

## Section 1: The Physics — Why COP > 1

The Carnot bound for heat pump heating: COP_max = T_hot / (T_hot - T_cold) in Kelvin. Heating to 70F (294K) when outdoor is 20F (266K): COP_max = 294 / 28 = 10.5. Real ASHP at those conditions: COP 2-3, or 20-30% of Carnot. The key relationship: COP_max is proportional to 1/delta-T — as outdoor temperature drops, delta-T increases and COP_max falls steeply. This is why the performance-vs-temperature curve below has its characteristic shape, and why supplemental heat (electric resistance or gas) kicks in at extreme cold.

```
  GAS FURNACE:                  HEAT PUMP:
  ┌──────────────────┐          ┌──────────────────────────────────┐
  │ Chemical energy  │          │ Electrical energy (work) in:     │
  │ (gas) burned     │          │ W = 1 BTU                        │
  │ → heat directly  │          └──────────────────────────────────┘
  │ AFUE 80–98%      │                      |
  │ COP ≤ 0.98       │                      v Compressor work
  └──────────────────┘          ┌──────────────────────────────────┐
                                │ Outdoor air at 20°F contains     │
  ENERGY IN = ENERGY OUT        │ heat (absolute zero = -459°F;    │
  (some lost up flue)           │ 20°F = 479°F above absolute zero)│
                                │ → Heat absorbed from outdoor air │
                                │   by evaporating refrigerant     │
                                └──────────────────────────────────┘
                                              |
                                              v
                                ┌──────────────────────────────────┐
                                │ Heat delivered indoors:          │
                                │ Q = W + Q_outdoor                │
                                │   = 1 + 2 = 3 BTU                │
                                │ COP = Q/W = 3.0                  │
                                │ (300% "efficiency")              │
                                └──────────────────────────────────┘

  Not magic — work moves ambient heat uphill against ΔT
  Second law: work required is proportional to temperature lift
  Smaller temperature difference (mild outdoor) → higher COP
  Larger temperature difference (very cold outdoor) → lower COP
```

---

## Section 2: Air-Source Heat Pump (ASHP) — Standard

```
  BASIC ASHP:
  - Same components as AC + reversing valve
  - Outdoor unit handles both condensing (cooling) and evaporating (heating)
  - Balance point: outdoor temp where heat pump output = building heat loss
  - Below balance point: auxiliary electric resistance strips supplement

  TRADITIONAL BALANCE POINT: ~25–30°F
  Below 25°F: COP drops, aux strips kick in (COP = 1.0)
  → Operating cost penalty; efficiency advantage disappears in deep cold
  → Traditional ASHP problematic in climate zones 5+

  R-VALUE BRIDGE:
  Better-insulated building → lower heat loss → lower balance point
  → Heat pump can handle more of the load without aux heat
  → Envelope improvements directly extend heat pump viability
```

### Performance Curve

```
  ASHP COP in Heating Mode vs Outdoor Temperature:

  Outdoor Temp:   50°F    40°F    30°F    20°F    10°F    0°F   -10°F
  Standard ASHP:  3.8     3.2     2.5     2.0     1.5     --     --
  Cold-Climate:   4.0     3.5     3.0     2.7     2.3     2.0    1.5

  Gas furnace: 0.80–0.98 (constant)
  Electric resistance: 1.0 (constant)

  Crossover: cold-climate ASHP remains more efficient than
  electric resistance down to ~-10°F and more efficient than
  a 96% gas furnace at equivalent energy prices down to ~-5°F
```

---

## Section 3: Cold-Climate ASHP

The engineering problem: as outdoor temp drops, air density decreases, evaporator
coil performance degrades, and more compression work is required. Standard ASHPs
hit their performance floor at ~25°F.

```
  COLD-CLIMATE ASHP TECHNOLOGIES:
  ┌─────────────────────────────────────────────────────────────────┐
  │ Variable-speed/inverter compressor                              │
  │ → Runs at higher speed in cold (compensates for less heat       │
  │   in air) → maintains capacity at low temperatures              │
  │                                                                 │
  │ Enhanced Vapor Injection (EVI) / Intermediate Injection         │
  │ → Injects additional refrigerant vapor mid-compression          │
  │ → Increases refrigerant mass flow → more capacity in cold       │
  │ → Reduces discharge temperature → protects compressor           │
  │                                                                 │
  │ Flash tank / Economizer cycle                                   │
  │ → Intermediate pressure stage for additional heat exchange      │
  └─────────────────────────────────────────────────────────────────┘

  MAJOR COLD-CLIMATE BRANDS:
  ┌──────────────────┬────────────────────────────────────────────────┐
  │ Mitsubishi       │ Hyper Heat (H2i) line; rated to -13°F; some    │
  │                  │ models to -22°F; pioneered the market          │
  ├──────────────────┼────────────────────────────────────────────────┤
  │ Daikin           │ Aurora series; rated to -13°F; extensive mini- │
  │                  │ split and ducted options                        │
  ├──────────────────┼────────────────────────────────────────────────┤
  │ Bosch            │ IDS series; rated to -13°F; strong US market   │
  ├──────────────────┼────────────────────────────────────────────────┤
  │ Fujitsu          │ Halcyon series; -15°F rated                   │
  ├──────────────────┼────────────────────────────────────────────────┤
  │ LG, Samsung      │ Various cold-climate options to -13°F          │
  └──────────────────┴────────────────────────────────────────────────┘

  NEEP (Northeast Energy Efficiency Partnerships) cold-climate database:
  Lists tested performance at 5°F and 17°F for enrolled products
  → Use this, not marketing specs alone
```

---

## Section 4: Mini-Split (Ductless) Systems

The dominant form factor for cold-climate heat pumps and zone additions:

```
  MINI-SPLIT ARCHITECTURE:
  ┌───────────────────────────────────────────────────────────────────┐
  │                                                                   │
  │  OUTDOOR UNIT ("condenser")                                       │
  │  ┌──────────────────────┐                                         │
  │  │ Compressor (inverter)│                                         │
  │  │ Outdoor coil         │                                         │
  │  │ Fan                  │                                         │
  │  └──────────┬───────────┘                                         │
  │             │ Refrigerant line set (3/8" liquid + 5/8" suction)   │
  │             │ + control wire + power                              │
  │             │ Max line length: ~100 ft (model-dependent)          │
  │             │                                                     │
  │         ┌───┴────┐                                                │
  │         │ Indoor │  Wall-mounted cassette (most common)           │
  │         │ unit 1 │  OR ceiling cassette, floor console,           │
  │         │ ("air  │     concealed ducted air handler               │
  │         │ handler│  Each indoor unit = independent zone           │
  │         └────────┘  with its own remote/app control               │
  │             │                                                     │
  │         ┌───┴────┐                                                │
  │         │ Indoor │  Multi-zone: one outdoor, multiple indoors     │
  │         │ unit 2 │  (capacity shared — each indoor sized          │
  │         └────────┘   appropriately)                              │
  │                                                                   │
  └───────────────────────────────────────────────────────────────────┘

  EFFICIENCY: SEER2 up to 42 (single-zone, optimal conditions)
              Typical cold-climate mini-split: SEER2 18–30
              HSPF2: 10–14 for quality systems

  LINE SET RULES:
  - Maximum line length varies by model (typically 25–100 ft)
  - Excessive line length → refrigerant charge correction needed
  - Elevation difference (indoor above/below outdoor) → manufacturer limits
  - Never kink the refrigerant lines
```

### Mini-Split Indoor Unit Types

```
  ┌──────────────────┬────────────────────────────────────────────────┐
  │ Wall-mounted     │ Most common; installed high on wall; typical   │
  │ cassette         │ rooms, bedrooms, living areas                  │
  ├──────────────────┼────────────────────────────────────────────────┤
  │ Ceiling cassette │ 4-way airflow; center of room; commercial feel;│
  │                  │ minimal wall space impact; requires ceiling     │
  │                  │ access for installation                        │
  ├──────────────────┼────────────────────────────────────────────────┤
  │ Floor console    │ Low on wall; good for rooms with windows on    │
  │                  │ all walls or where high mount impractical      │
  ├──────────────────┼────────────────────────────────────────────────┤
  │ Concealed ducted │ Air handler in ceiling/closet; short duct runs; │
  │ air handler      │ no visible indoor unit; aesthetically seamless; │
  │                  │ less efficient than ductless; ~50 ft max duct  │
  └──────────────────┴────────────────────────────────────────────────┘
```

---

## Section 5: Ground-Source Heat Pump (GSHP / Geothermal)

Instead of using outdoor air as the heat source/sink, uses the earth or water.
The ground temperature below frost line (~6 feet) is ~50–55°F year-round in the US.

```
  WHY GROUND SOURCE:
  - Ground temp constant ~50–55°F regardless of outdoor air temp
  - In winter (heating): 50°F >> -10°F → much easier to extract heat
  - In summer (cooling): 50°F << 90°F → much easier to reject heat
  - Seasonal COP averages 3.5–5.0 (vs 2.0–3.5 for air-source)
  - Higher upfront cost (ground loop installation); lower operating cost

  LOOP TYPES:
  ┌───────────────────┬──────────────────────────────────────────────┐
  │ Horizontal closed │ 2–6 ft deep trenches; 400–600 ft pipe/ton;   │
  │ loop              │ large lot required; lowest drilling cost     │
  ├───────────────────┼──────────────────────────────────────────────┤
  │ Vertical closed   │ Boreholes 150–300 ft deep; ~200–250 ft/ton; │
  │ loop              │ smaller lot OK; higher drilling cost         │
  ├───────────────────┼──────────────────────────────────────────────┤
  │ Pond/lake closed  │ Coiled pipe sunk in pond; lowest cost if     │
  │ loop              │ water body available and accessible          │
  ├───────────────────┼──────────────────────────────────────────────┤
  │ Open loop         │ Pump groundwater through HX, return to ground│
  │                   │ Highest COP (large thermal reservoir);      │
  │                   │ water rights, reinjection requirements       │
  └───────────────────┴──────────────────────────────────────────────┘

  COSTS:
  - Horizontal bore: $10,000–15,000 for 3-ton system (trenching)
  - Vertical bore: $20,000–35,000+ (drilling is expensive)
  - Equipment + installation total: $25,000–45,000+ installed
  - Federal tax credit (IRA 2022): 30% (no cap for GSHP)
  - Operating savings: 40–70% vs conventional; 5–10 year payback typical
```

---

## Section 6: Heat Pump Water Heaters

```
  PRINCIPLE: Heat pump evaporates refrigerant → absorbs heat from room air →
             compresses → condenses inside water storage tank → heats water
             COP 3.5–4.0 (vs. electric resistance COP 1.0)

  REQUIREMENTS:
  - Unconditioned or semi-conditioned space (basement, garage)
  - Draws heat FROM space → slightly cools/dehumidifies the room
    (benefit in summer, slight penalty in winter if in conditioned space)
  - Min. ~750 sq ft air space around unit (air source)
  - Ambient temp: 40–120°F for efficient operation
  - Fan + compressor noise (60–65 dB) — don't install in bedroom above

  BRANDS: Rheem ProTerra, A.O. Smith Voltex, Stiebel Eltron, Bradford White

  FEDERAL TAX CREDIT (IRA 2022): $300 (§25C, Energy Star certified)

  ECONOMICS:
  Electric resistance WH: ~$600–800/yr operating cost
  HPWH at COP 3.5:        ~$175–225/yr
  Annual savings: ~$400/yr → ~2–3 year payback on $300 upcharge
```

---

## Section 7: Defrost Cycle

An unavoidable consequence of extracting heat from cold outdoor air:

```
  WHEN FROST FORMS:
  - Outdoor coil operating in heating mode: coil surface is below outdoor air temp
  - When outdoor temp < 35°F AND coil surface < 32°F
  - Moisture in air freezes on coil → frost buildup
  - Frost insulates coil → reduces heat transfer → reduced heating capacity

  DEFROST CYCLE:
  1. Triggered by timer + temperature sensor, or differential pressure sensor
     (pressure drop across frosted coil)
  2. System briefly reverses to cooling mode
     → Outdoor coil becomes condenser (hot refrigerant melts frost)
  3. Backup resistance heat runs during defrost
     → Prevents cold air delivery to house
  4. After ~2–5 minutes: defrost complete, returns to heating mode

  VISIBLE TO HOMEOWNER:
  - Steam or water dripping from outdoor unit
  - Cold air from vents briefly (if backup heat slow to respond)
  - Outdoor unit fan stops during defrost (to retain heat)
  → All NORMAL — not a malfunction
  → Common homeowner complaint: "my heat pump doesn't heat on cold days"
     Reality: it's running defrost cycles every 30–90 min in icy conditions
```

---

## Decision Cheat Sheet

| Scenario | System |
|---|---|
| New construction, cold climate (zones 4–6) | Cold-climate ASHP (Mitsubishi/Daikin/Bosch) ducted |
| New construction, mild climate | Standard ASHP, ducted |
| No existing ductwork, room addition | Mini-split, ductless |
| Large lot, budget for upfront cost | GSHP (best operating efficiency) |
| Multiple rooms needing separate control | Multi-zone mini-split |
| Replacing existing gas furnace, keep ducts | Ducted heat pump air handler + existing duct |
| Adding AC to existing furnace, consider future | Add-on heat pump coil (dual-fuel with gas backup) |
| Water heating, have basement or garage | Heat pump water heater |
| Zone 7+ (subarctic, Fairbanks) | GSHP or cold-climate ASHP + well-insulated envelope |

---

## Common Confusion Points

**COP > 1 is not a thermodynamics violation**: you're moving ambient heat against a
temperature gradient. The work (electricity) enables the transfer. First law satisfied:
heat output = electrical work + heat extracted from outdoor air.

**Aux heat vs emergency heat**: aux = heat pump + resistance strips simultaneously
(normal operation in very cold weather). Emergency = resistance strips ONLY, heat pump
off. Never run in emergency heat except during maintenance — massive efficiency penalty.

**Balance point is not a cliff**: as outdoor temp drops below balance point, heat pump
COP decreases gradually. The thermostat system smoothly ramps in aux heat. It's not
a sudden switch. Good thermostat logic minimizes how often aux heat runs.

**Mini-splits in multi-zone systems share capacity**: a 36,000 BTU/hr outdoor unit
powering three indoor units can't deliver 36,000 to each simultaneously — it splits
capacity. Design requires each indoor unit to be sized for its room, and total simultaneous
demand must not exceed outdoor unit capacity.

**R-22 equipment cannot be retrofitted to R-410A**: different operating pressures,
different lubricant (POE vs alkylbenzene), different compressor design. R-22 →
R-410A is an equipment replacement, not a refrigerant swap.
