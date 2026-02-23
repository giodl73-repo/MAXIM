# HVAC Systems — Overview

## The Big Picture

HVAC is one integrated control problem: move heat where you want it, dilute contaminants
to acceptable concentration, and maintain moisture in the human comfort band — all while
spending as little energy as possible. Three subsystems, tightly coupled.

```
+------------------------------------------------------------------+
|                    THE HVAC PROBLEM SPACE                         |
|                                                                  |
|  OUTDOOR CONDITIONS          BUILDING ENVELOPE          INDOORS  |
|  ----------------            -----------------          -------- |
|  Temperature (hot/cold)  --> Conduction, Convection --> 68–76°F  |
|  Humidity (humid/dry)    --> Air infiltration     --> 30–60% RH  |
|  Air quality (pollutants)--> Openings, cracks     --> <1000ppm   |
|  Solar radiation         --> Windows, mass        --> CO₂        |
|  Wind                    --> Stack effect         --> No mold     |
|                                                                  |
|                    HVAC RESPONDS TO ALL OF THIS                  |
+------------------------------------------------------------------+
         |                    |                    |
         v                    v                    v
+----------------+  +------------------+  +------------------+
|   HEATING &    |  |   VENTILATION    |  |   AIR QUALITY    |
|   COOLING      |  |                  |  |   CONTROL        |
|                |  |                  |  |                  |
| Move heat in   |  | Bring in fresh   |  | Filter particles |
| or out of the  |  | air, exhaust     |  | dilute CO₂, VOCs |
| conditioned    |  | stale air,       |  | control humidity |
| space          |  | recover energy   |  | (mold prevention)|
+----------------+  +------------------+  +------------------+
```

---

## Load vs. Capacity — The Fundamental Sizing Relationship

```
  LOAD                          CAPACITY
  ----                          --------
  How much heat (BTU/hr)        How much heat (BTU/hr)
  flows through the building    the equipment can move
  envelope from outside          in or out
  to inside (or vice versa)

  Summer: outdoor heat flows IN  → cooling load (remove it)
  Winter: indoor heat flows OUT  → heating load (replace it)

  OVERSIZED equipment:          UNDERSIZED equipment:
  - Short-cycles                - Runs constantly
  - Poor dehumidification       - Can't reach setpoint on
  - High humidity in summer       design day
  - Premature wear              - Fine for mild days only
  - Wasted energy

  Rule: size to load, not to "bigger is safer"
  Tool: Manual J (residential load calculation)
```

### Load Components

```
+----------------------------------------------------------+
|              TOTAL BUILDING LOAD                          |
|                                                          |
|  ENVELOPE LOADS (heat flows through structure)           |
|  ├── Walls (U-value × area × ΔT)                        |
|  ├── Roof/ceiling (usually largest surface area)         |
|  ├── Windows (high U-value + solar gain)                 |
|  ├── Floor (slab or crawlspace)                          |
|  └── Infiltration (air leakage × ΔT)                    |
|                                                          |
|  INTERNAL GAINS (heat generated inside)                  |
|  ├── People (~250 BTU/hr sensible + 200 BTU/hr latent)  |
|  ├── Lighting (3.41 BTU/hr per watt)                     |
|  └── Appliances (refrigerator, oven, electronics)        |
|                                                          |
|  VENTILATION LOADS (conditioning outdoor air)            |
|  └── Code-required fresh air (ASHRAE 62.2 / 62.1)       |
|                                                          |
|  SENSIBLE vs LATENT SPLIT                                |
|  ├── Sensible: changes temperature (dry bulb)            |
|  └── Latent: changes moisture content (humidity)         |
|      → Latent load = dehumidification requirement        |
+----------------------------------------------------------+
```

---

## Residential vs. Commercial

```
+-------------------------------+-------------------------------+
|        RESIDENTIAL            |         COMMERCIAL            |
+-------------------------------+-------------------------------+
| Manual J load calc            | HAP / eQUEST energy model     |
| Single zone or 2-3 zones      | Dozens to hundreds of zones   |
| 1–5 ton equipment             | 5 ton to 1,000+ ton chillers  |
| Split system or heat pump     | Chiller + AHU + VAV boxes     |
| Forced air or mini-split      | Chilled water, fan-coil units |
| 24V thermostat control        | BAS (BACnet/Modbus)           |
| Homeowner-accessible          | Facilities engineer + BMS     |
| SEER2/HSPF2 ratings           | IPLV/NPLV for chillers        |
| $3,000–$20,000 install        | $50/sqft commercial build-out |
+-------------------------------+-------------------------------+
```

---

## System Taxonomy

```
                    HVAC SYSTEM TYPES
                    =================

HEATING ONLY
├── Gas furnace (forced air)
├── Boiler (hydronic — hot water or steam)
├── Electric resistance (baseboard, radiant floor)
└── Wood/pellet stove

COOLING ONLY
└── Central air conditioner (split system)
    ├── Condensing unit (outdoor)
    └── Evaporator coil (indoor, on furnace)

HEATING + COOLING
├── Heat pump (air-source or ground-source)
│   ├── Ducted (central)
│   └── Ductless mini-split
└── Packaged unit (all-in-one, rooftop — common commercial)

VENTILATION
├── Exhaust-only (bath fans, range hood)
├── Supply-only (less common)
└── Balanced
    ├── ERV (Energy Recovery Ventilator — heat + moisture)
    └── HRV (Heat Recovery Ventilator — heat only)

AIR DISTRIBUTION
├── Forced air (ductwork)
│   ├── Trunk-and-branch
│   └── Extended plenum
├── Hydronic (water pipes → radiators, radiant floor)
└── Ductless (refrigerant lines to air handlers)
```

---

## Energy Flow Through a Cooling System

```
  OUTDOORS (115°F)                              INDOORS (75°F)

  Condenser coil                                Evaporator coil
  (rejects heat to outdoor air)                 (absorbs heat from room air)
       |                                                  |
       |  Refrigerant at high pressure/temp              |
       |<-------------------------------------------------|
       |  Compressor raises pressure → work input        |
       |                                                  |
       |  Refrigerant at low pressure/temp               |
       |------------------------------------------------->|
       |  Expansion valve drops pressure → cold refrigerant

  Heat flows:  Building heat → refrigerant → outdoor air
  Work input:  Compressor electricity
  COP:         3.0 = 3 BTU moved per 1 BTU of electricity
```

---

## Module Map

| Module | Topic | Key Concepts |
|--------|-------|-------------|
| `01-THERMODYNAMICS` | Heat transfer physics | R-value, Manual J, psychrometrics, sensible/latent |
| `02-REFRIGERATION-CYCLE` | Vapor compression | P-H diagram, COP, SEER, superheat, subcooling |
| `03-REFRIGERANTS` | Working fluids | ODP, GWP, R-22→R-410A→R-32/R-454B, A2L safety |
| `04-HEATING-SYSTEMS` | Furnaces & boilers | AFUE, condensing, mod-con boiler, combustion |
| `05-HEAT-PUMPS` | COP >1 systems | ASHP, GSHP, mini-split, cold-climate, HSPF2 |
| `06-VENTILATION` | Fresh air & IAQ | ERV/HRV, ASHRAE 62.2, MERV, CO₂, PM2.5 |
| `07-DUCTWORK` | Air distribution | Manual D, static pressure, flex duct, Aeroseal |
| `08-CONTROLS` | Thermostats & BAS | 24V wiring, PID, BACnet, demand control, economizer |
| `09-EFFICIENCY-CODES` | Ratings & regulation | SEER2, AFUE, IRA tax credits, IECC climate zones |

---

## Decision Cheat Sheet

| Situation | Right System |
|-----------|-------------|
| New construction, cold climate (zones 4–6) | Cold-climate ASHP + ERV |
| New construction, hot-humid (zones 1–2) | Heat pump + whole-house dehumidifier + ERV |
| Existing home, gas heating, adding AC | Add AC evaporator coil to existing furnace |
| No ducts, room additions, garages | Mini-split (ductless heat pump) |
| Whole-house replacement, mild climate | Central heat pump, ducted |
| Very cold climate (zone 6+) | Cold-climate ASHP (Mitsubishi/Bosch) or GSHP |
| Large commercial building | Chiller + AHU + VAV distribution |
| Tight building needing fresh air | ERV (hot/humid or mixed climate) |
| Cold climate, tight building | HRV (dry winters — dump moisture) |
| Retrofit over existing gas furnace | Add-on heat pump (dual-fuel) |

---

## Common Confusion Points

**"HVAC" vs "AC"**: HVAC is the whole system. "AC" strictly means cooling only, but colloquially means the whole forced-air system. When someone says "my AC isn't working in winter," they usually mean the furnace.

**Tons of cooling**: 1 ton = 12,000 BTU/hr. Origin: latent heat of melting 1 ton of ice per day (legacy unit). Typical house: 2–4 tons. 1 ton ≈ 1.2 kW of electrical input at SEER2 of 14.

**BTU vs BTU/hr**: BTU is energy; BTU/hr is power (rate). Equipment is rated in BTU/hr but people drop the "/hr." Furnaces: 40,000–120,000 BTU/hr. Residential AC: 24,000–60,000 BTU/hr.

**Efficiency rating confusion**: SEER (cooling) ≠ EER ≠ SEER2. HSPF (heat pump heating) ≠ AFUE (furnace). SEER2 replaced SEER in 2023 — same equipment, harder test, ~15% lower number. Never compare old SEER to new SEER2 directly; the equipment didn't get less efficient.

**Heat pump in winter**: Heat pumps move heat from outdoor air even when it's cold. Air at -10°F still contains substantial thermal energy — absolute zero is -459°F. Modern cold-climate models are rated to -22°F. The physics is counterintuitive but solid.

**Sensible vs. latent**: "It's not the heat, it's the humidity" is about latent load. An AC unit that's too large cools the air (sensible) before it has time to dehumidify (latent) — the space feels cool but clammy. Right-sizing prevents this.
