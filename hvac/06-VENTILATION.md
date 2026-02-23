# Ventilation

## The Big Picture

Modern tight construction created a new problem: buildings no longer breathe enough
to maintain acceptable indoor air quality by accident. Intentional mechanical ventilation
is now required — and the energy cost of ventilating can be recovered through heat exchange.

```
+----------------------------------------------------------------------+
|               THE TIGHT BUILDING DILEMMA                             |
|                                                                      |
|  OLD LEAKY HOUSE           NEW TIGHT HOUSE                           |
|  (>10 ACH50)               (<3 ACH50)                               |
|                                                                      |
|  Natural infiltration      Minimal infiltration                      |
|  keeps air "fresh"         saves energy                              |
|  (accidentally)            BUT indoor air quality                    |
|                            degrades without                          |
|  Large heating/cooling     intentional ventilation                   |
|  energy waste                                                        |
|                            Solution: mechanical                      |
|  No mold risk from         ventilation with                          |
|  tight air pockets         energy recovery                           |
+----------------------------------------------------------------------+
         |                                    |
         v                                    v
  Rule: tighter is better for energy;  tighter requires ventilation
  build tight, ventilate right
```

---

## Section 1: Infiltration vs. Ventilation

```
  INFILTRATION (uncontrolled):
  - Air leakage through cracks, gaps, penetrations, electrical outlets
  - Driven by: wind pressure + stack effect (warm air rises, creates
    positive pressure at ceiling, negative at floor)
  - Unpredictable, variable, unfiltered
  - Can draw radon from soil, moisture from crawlspace,
    exhaust from garage, pollen from outdoors
  - Measured by blower door: ACH50

  VENTILATION (controlled):
  - Intentional introduction of outdoor air
  - Measured, filtered, often conditioned
  - Can be paired with heat recovery

  STACK EFFECT:
  ┌──────────────────────────────────────────────────────┐
  │                    ROOF                              │
  │          +P  warm air exits ↑                        │
  │                                                      │
  │ NEUTRAL  ←─────────────────────────────── neutral   │
  │ PLANE    no pressure differential                    │
  │                                                      │
  │          -P  cold air enters ↓                       │
  │                    SLAB                              │
  └──────────────────────────────────────────────────────┘
  Warm air in house rises → exits through upper gaps →
  replacement air drawn in at bottom
  Effect is larger: taller buildings, larger ΔT inside/outside
```

---

## Section 2: ASHRAE 62.2 — Residential Ventilation Standard

The design target for whole-house mechanical ventilation:

```
  ASHRAE 62.2 FORMULA:
  Q_total = 0.01 × A_floor + 7.5 × (N_br + 1)

  Where:
  A_floor = conditioned floor area (ft²)
  N_br    = number of bedrooms

  EXAMPLES:
  ┌──────────┬────────┬────────┬────────────┐
  │ House    │ Sq Ft  │ Beds   │ Required   │
  ├──────────┼────────┼────────┼────────────┤
  │ Small    │ 1,000  │ 2      │ 10+22=32   │
  │ Typical  │ 1,500  │ 3      │ 15+30=45   │
  │ Large    │ 2,500  │ 4      │ 25+37=62   │
  └──────────┴────────┴────────┴────────────┘

  These are in CFM (cubic feet per minute)

  COMPLIANCE:
  - Any combination of exhaust, supply, or balanced that achieves
    the required CFM over time (intermittent allowed with boost factor)
  - Spot ventilation (bath, kitchen) separate requirement
```

---

## Section 3: Ventilation Strategies

```
  EXHAUST-ONLY:
  ┌──────────────────────────────────────────────────────────────────┐
  │ Bath fan or dedicated exhaust fan runs continuously              │
  │ Slightly negative house pressure                                 │
  │ Fresh air infiltrates through leakage paths                      │
  │                                                                  │
  │ PROS: Cheapest; simplest; uses existing bath fans                │
  │ CONS: Air path uncontrolled (may draw radon, garage fumes)       │
  │       Slightly negative pressure may pull from bad sources       │
  │       Cold climate: infiltrating air unfiltered                  │
  └──────────────────────────────────────────────────────────────────┘

  SUPPLY-ONLY:
  ┌──────────────────────────────────────────────────────────────────┐
  │ Fresh air fan forces outdoor air into return duct or directly    │
  │ Slightly positive house pressure                                 │
  │ Stale air exfiltrates through leakage paths                      │
  │                                                                  │
  │ PROS: Cleaner air source; positive pressure keeps pollutants out │
  │ CONS: Pushing humid air into walls in cold climates (condensation│
  │       risk inside wall assembly); filtration quality varies      │
  └──────────────────────────────────────────────────────────────────┘

  BALANCED (ERV/HRV):
  ┌──────────────────────────────────────────────────────────────────┐
  │ Equal exhaust + supply airflow; no pressure imbalance            │
  │ Dedicated intake + exhaust pathways                              │
  │ Heat exchanger core recovers energy                              │
  │                                                                  │
  │ PROS: Controlled; filtered; energy efficient; no pressure issues │
  │ CONS: Higher equipment cost; installation complexity             │
  └──────────────────────────────────────────────────────────────────┘
```

---

## Section 4: HRV vs. ERV

The most important design decision for balanced ventilation:

```
  HRV (Heat Recovery Ventilator):
  ┌──────────────────────────────────────────────────────────────────┐
  │ Transfers SENSIBLE HEAT only between exhaust and supply streams  │
  │                                                                  │
  │ Exhaust air: 70°F, 50% RH  ──────── HRV core ──────── exits    │
  │ Supply air: -10°F outdoor   ──────── HRV core ──────── 55°F in  │
  │                                                                  │
  │ 70–80% sensible heat recovery                                    │
  │ Moisture: does NOT transfer → exhaust moisture exits building    │
  │                                                                  │
  │ WHEN TO USE:                                                     │
  │ Cold, dry climates (zones 5–8)                                   │
  │ - Don't want to bring in outdoor humidity in humid summers       │
  │ - Winter: some say prefer to expel indoor moisture (tight homes  │
  │   can have excess humidity from cooking, showers, occupants)     │
  │ - HRV expels moisture → prevents condensation on cold surfaces   │
  └──────────────────────────────────────────────────────────────────┘

  ERV (Energy Recovery Ventilator):
  ┌──────────────────────────────────────────────────────────────────┐
  │ Transfers BOTH sensible heat AND moisture (enthalpy exchange)    │
  │ Desiccant wheel or semi-permeable membrane core                  │
  │                                                                  │
  │ Summer mode: incoming hot humid air → ERV core → moisture        │
  │              transferred to cooler exhaust stream → enters       │
  │              house cooler AND drier                              │
  │ Winter mode: outgoing humid exhaust air → ERV core → moisture    │
  │              partially retained → incoming air gains humidity    │
  │                                                                  │
  │ 70–80% of both sensible AND latent energy recovered              │
  │                                                                  │
  │ WHEN TO USE:                                                     │
  │ Hot/humid climates (zones 1–3)                                   │
  │ Mixed humid climates (zone 4)                                    │
  │ - Summer: reduces latent load on AC by pre-dehumidifying         │
  │ - Winter: retains humidity (combats dry air issues)              │
  └──────────────────────────────────────────────────────────────────┘

  CLIMATE DECISION:
  Zone 1–3 (humid): ERV
  Zone 4 (mixed): either; lean ERV for humid summers
  Zone 5–8 (dry/cold): HRV (dump excess winter moisture)
  Exception: very dry cold climates (Denver, Phoenix in winter): ERV
             to retain moisture
```

---

## Section 5: Filtration — MERV Ratings

Filtration efficiency is standardized by ASHRAE 52.2:

```
  MERV RATINGS (Minimum Efficiency Reporting Value):
  ┌──────────┬──────────────────────────────────────────────────────┐
  │ MERV 1–4 │ Fiberglass, washable; pollen (>10 μm); dust mites   │
  │          │ Basic equipment protection only                      │
  ├──────────┼──────────────────────────────────────────────────────┤
  │ MERV 5–8 │ Mold spores, dust, pet dander (3–10 μm)             │
  │          │ Minimum recommended for residential comfort           │
  ├──────────┼──────────────────────────────────────────────────────┤
  │ MERV 9–12│ Legionella, auto emissions, lead dust (1–3 μm)       │
  │          │ Good residential; some commercial; hospital waiting   │
  ├──────────┼──────────────────────────────────────────────────────┤
  │ MERV 13  │ Bacteria, virus-carrying droplets (0.3–1 μm)         │
  │          │ Recommended upgrade post-COVID; residential feasible │
  │          │ with proper system design; some pressure drop penalty │
  ├──────────┼──────────────────────────────────────────────────────┤
  │ MERV 14–16│ Similar to HEPA efficiency; hospital, OR, clean room │
  │          │ High pressure drop — must verify system fan capacity  │
  ├──────────┼──────────────────────────────────────────────────────┤
  │ MERV 17+ │ HEPA: ≥99.97% at 0.3 μm; cleanroom, OR, IC fab     │
  │          │ Standalone HEPA units bypass main HVAC (separate unit)│
  └──────────┴──────────────────────────────────────────────────────┘

  PRESSURE DROP TRADEOFF:
  Higher MERV → higher pressure drop across filter
  → reduced airflow → reduced equipment capacity
  → possible coil freeze-up (low airflow = low suction pressure)
  → check external static pressure spec before upgrading

  MERV 13 in residential: usually fine with proper duct sizing;
  verify TESP (total external static pressure) headroom
```

---

## Section 6: IAQ — Key Pollutants

```
  POLLUTANT    SOURCE              HEALTH EFFECT        STANDARD/ACTION
  ---------    ------              -------------        ---------------
  CO₂          Occupants,          Cognitive impairment 400 ppm outdoor baseline
               combustion          at >1000 ppm;        800–1000 ppm = poor IAQ
                                   drowsiness, focus    1500+ = significant impairment
                                   decline              Proxy for ventilation adequacy

  CO           Combustion          Toxic at 70+ ppm;    UL2034: alarm at 70 ppm
               appliances          lethal at 400+ ppm   CO detector mandatory
               malfunction         No warning signs     (no color, no smell)

  PM2.5        Outdoor pollution,  Lung disease, CV     EPA: 12 μg/m³ annual avg
               cooking, wildfire,  disease, cancer      35 μg/m³ 24-hr average
               candles, smoking    (fine particles       HEPA + ERV/HRV filtration
                                   penetrate deepest)

  VOCs         Off-gassing from    Eye/nose irritation, No single standard
               materials, paint,   headaches, long-term Source control first;
               cleaners, plastics  carcinogen risk      ventilation + activated carbon

  Radon        Soil radioactive    2nd leading cause of EPA action level: 4 pCi/L
               decay (uranium)     lung cancer in US    Mitigation: sub-slab
               → basements                              depressurization fan

  Humidity     Occupants,          Mold >60% RH         30–60% RH optimal
  (RH%)        cooking, showers    Virus survival <30%  Monitor; control with
                                   Dust mites >50%      HVAC + dehumidifier

  Formaldehyde Composite wood,     Carcinogen            Low-emission materials;
               insulation, carpet  (IARC Group 1)        ventilation; activated carbon
```

---

## Section 7: Demand-Controlled Ventilation (DCV)

```
  PRINCIPLE: Vary ventilation rate based on actual CO₂ concentration
  → Ventilate more when occupied (CO₂ rising), less when empty (save energy)

  IMPLEMENTATION:
  CO₂ sensor → BAS or ERV controller → damper or fan speed modulation

  ASHRAE 62.1: explicitly allows DCV for commercial spaces
  Residential: emerging; smart ERV/HRV controllers (Broan, Fantech, Panasonic)

  TARGET CO₂ SETPOINTS:
  700–800 ppm: well-ventilated
  800–1000 ppm: acceptable; slight cognitive impact
  1000–1200 ppm: trigger increased ventilation
  >1200 ppm: fully open ventilation; occupancy load exceeds design

  PM2.5 DCV: AQI sensors from outdoor network → close HRV/ERV fresh
             air intake during wildfire smoke events (recirculate + HEPA)
```

---

## Decision Cheat Sheet

| Situation | Choice |
|---|---|
| Cheap ventilation, existing bath fan | Exhaust-only (ASHRAE 62.2 cfm required) |
| New construction, cold dry climate (zones 5–8) | HRV balanced ventilation |
| New construction, hot/humid climate (zones 1–3) | ERV balanced ventilation |
| New construction, mixed climate (zone 4) | ERV (lean toward humid side) |
| Need MERV 13 in existing system | Check TESP headroom; may need duct upgrade |
| Wildfire/outdoor air quality concern | Close fresh air intake; HEPA recirculation |
| CO₂ monitoring for office ventilation | DCV with CO₂ sensors → BAS control |
| Radon found at >4 pCi/L | Sub-slab depressurization (separate from HVAC) |

---

## Common Confusion Points

**HEPA bypass problem**: a HEPA filter in the main HVAC duct reduces airflow so much
it often damages equipment. Dedicated HEPA air purifiers (standalone units with their
own fan) or MERV 13-16 in-duct filters are the practical approach for residential.

**ERV doesn't fully dehumidify**: ERV transfers moisture between exhaust and supply
(recovery), but it doesn't dehumidify if the incoming air is more humid than indoor.
In very humid climates, you still need AC and possibly a whole-house dehumidifier.

**Kitchen exhaust creates makeup air need**: running a 1,000 CFM commercial range
hood creates serious negative pressure in a tight house. Makeup air must be provided
(dedicated inlet, sometimes conditioned) or the hood stalls and backdraft from the
furnace is possible.

**Bath fan intermittent = ventilation credit**: ASHRAE 62.2 allows intermittent
ventilation with a "boost factor" (e.g., run at 3× required CFM for ⅓ of the time).
This is why Panasonic WhisperGreen with intermittent ventilation mode is a popular
code compliance approach.
