# Heating Systems

## The Big Picture

Before heat pumps dominated new construction, heating was entirely about combustion
or electrical resistance. These systems remain in hundreds of millions of existing
homes and will continue operating for decades. The key distinctions are fuel type,
AFUE efficiency, and distribution method.

```
+----------------------------------------------------------------------+
|                    HEATING SYSTEM TAXONOMY                            |
|                                                                      |
|  COMBUSTION SYSTEMS              ELECTRIC SYSTEMS                    |
|  ------------------              -----------------                   |
|  Gas furnace (forced air)        Electric resistance (baseboard)     |
|  Gas boiler (hydronic)           Electric furnace / heat strips      |
|  Oil furnace (Northeast US)      Heat pump (covered in 05)           |
|  Propane furnace (rural)         Heat pump water heater              |
|  Wood/pellet                     Radiant electric floor              |
|                                                                      |
|  ALL COMBUSTION SYSTEMS:         ALL ELECTRIC RESISTANCE:            |
|  AFUE < 100% (flue losses)       "100% efficient" at point of use    |
|  Ventilation required            No flue needed                      |
|  Carbon monoxide risk            High operating cost ($/BTU)         |
+----------------------------------------------------------------------+
         |                                    |
         v                                    v
  Distribution: Forced air (ducts)   OR  Hydronic (water)
                Mini-split refrigerant     Baseboard / radiant floor
```

---

## Section 1: Gas Furnaces

The dominant US residential heating system. Gas furnace + AC coil in a single air handler
is the most common configuration installed over the past 40 years.

### Internal Anatomy

```
  GAS FURNACE INTERNALS (airflow path):

  Return air in
       |
       v
  ┌─────────────┐
  │   Filter    │  (owner-maintained; often neglected)
  └──────┬──────┘
         |
  ┌──────┴──────┐
  │  Evaporator │  (AC coil — not part of furnace, downstream of HX)
  │  Coil (AC)  │  (see 05-HEAT-PUMPS for heat pump coil)
  └──────┬──────┘
         |
  ┌──────┴──────┐
  │  Heat       │  Primary heat exchanger
  │  Exchanger  │  Combustion gases INSIDE (stainless or steel)
  │  (primary)  │  Supply air over OUTSIDE (never mix)
  └──────┬──────┘
         |         (Condensing furnace only:)
  ┌──────┴──────┐
  │  Secondary  │  Extracts remaining heat; flue gases cool below dew point
  │  Heat       │  → water condenses → condensate drain
  │  Exchanger  │  Enables 90–98% AFUE
  └──────┬──────┘
         |
  ┌──────┴──────┐
  │   Blower    │  ECM (electronically commutated motor) = variable speed
  └─────────────┘  PSC = permanent split capacitor = single speed (older)

  Combustion path:
  Gas valve → burners → heat exchanger → (secondary HX) → draft inducer → flue
  Ignition: hot surface igniter (HSI) — replaced standing pilot ~1990
  Safety: limit switch (high temp), pressure switch (proves draft), rollout switch
```

### AFUE — Annual Fuel Utilization Efficiency

```
  AFUE = (heat delivered to home) / (fuel energy consumed) × 100%

  Includes:
  - Cycling losses (startup and shutdown inefficiency)
  - Pilot light losses (if applicable)
  - Standby losses

  80% AFUE → 20% of gas energy goes up the flue as hot exhaust
  96% AFUE → 4% lost (mostly latent heat in condensate)

  FEDERAL MINIMUMS:
  - Non-condensing gas furnace: 80% AFUE
  - 2023 DOE attempt at 92% AFUE national minimum → blocked by courts
  - Some regional programs (utility rebates): may require 95%+

  RULE: In cold climates (heating season with frequent days below 20°F),
  condensing furnace payback is 3–7 years. In mild climates, 10+ years.
```

### Non-Condensing vs. Condensing — The Critical Distinction

```
  NON-CONDENSING (80% AFUE):
  ┌─────────────────────────────────────────────────────────────────┐
  │ Flue gas exits at 300–400°F (too hot to condense water vapor)   │
  │ Requires Category I or B-vent flue (metal, negative pressure)   │
  │ Can use existing chimney/B-vent (retrofit-friendly)             │
  │ No condensate — no drain required                               │
  │ Simpler, less expensive                                         │
  │ Cannot use PVC flue                                             │
  └─────────────────────────────────────────────────────────────────┘

  CONDENSING (90–98% AFUE):
  ┌─────────────────────────────────────────────────────────────────┐
  │ Secondary heat exchanger extracts latent heat from water vapor  │
  │ Flue gas exits at 100–120°F → water vapor condenses            │
  │ Condensate: slightly acidic (pH 3–5) → floor drain required     │
  │ Condensate neutralizer (limestone chips) → some municipalities  │
  │ PVC or CPVC flue (2" or 3") — two pipes: intake + exhaust       │
  │ Direct-vent or power-vent configurations                        │
  │ Can terminate through side wall (no chimney needed)             │
  │ More complex; secondary HX susceptible to corrosion if not      │
  │   maintained; high static pressure in return can cause issues   │
  └─────────────────────────────────────────────────────────────────┘

  EFFICIENCY COMPARISON:
  Annual gas cost saving (condensing vs non-condensing):
  $1,000/yr gas bill × (1 - 80/96) = ~$167/yr savings
  → roughly 4–6 year payback on $600–900 upcharge
  (more savings in colder climates where furnace runs harder)
```

---

## Section 2: Boilers — Hydronic Heating

Boilers heat water and distribute it through pipes to radiators, baseboard convectors,
or radiant floor. No ductwork — heat distribution is hydraulic.

```
  HYDRONIC SYSTEM OVERVIEW:
  ┌──────────┐     hot water    ┌─────────────────────────────┐
  │  Boiler  │─────────────────>│ Radiators / Baseboard / Floor│
  │          │                  └──────────────┬──────────────┘
  │          │<─────────────────────────────────┘
  └──────────┘     return water (cooled)

  STEAM vs HOT WATER:
  Steam: water boils → steam rises through pipes → condenses in radiators
         → releases latent heat (970 BTU/lb) → condensate returns
         Older urban housing (pre-1940s); one-pipe or two-pipe systems
         No thermostats at individual radiators (one-pipe steam)
         Temperature cannot be modulated at boiler without system redesign

  Hot water: simpler, safer, controllable; no steam → no phase change
             Temperature 120–180°F supply; return 100–160°F
             Circulator pump moves water
             Zone valves or zone circulators per zone
             Allows outdoor reset control (lower supply temp on mild days)
```

### Boiler Types

```
  ┌───────────────────┬────────────────────────────────────────────────┐
  │ Cast iron sectional│ High mass; slow response; very durable;       │
  │                   │ atmospheric vent common; assembled in sections │
  │                   │ (fits through door); AFUE ~80–85%             │
  ├───────────────────┼────────────────────────────────────────────────┤
  │ Steel fire tube   │ Lighter; faster response; AFUE 80–85%         │
  ├───────────────────┼────────────────────────────────────────────────┤
  │ Mod-con           │ Modulating-Condensing; stainless steel HX;    │
  │ (condensing)      │ modulates 10–100% burner output;              │
  │                   │ AFUE 95–98%; PVC flue; outdoor reset control; │
  │                   │ eliminates short cycling; best efficiency;     │
  │                   │ Brands: Navien, Triangle Tube, Viessmann,     │
  │                   │ Weil-McLain Ultra                             │
  │                   │ REQUIRES: low return water temp (<130°F)      │
  │                   │ for condensing operation                       │
  └───────────────────┴────────────────────────────────────────────────┘
```

### Outdoor Reset Control (Critical for Mod-Con)

```
  Concept: boiler supply temperature tracks outdoor temperature
  Cold outside → high supply temp (140°F); Mild outside → lower temp (90°F)

  Benefits:
  - Always in condensing mode when mild → highest efficiency
  - Reduces system cycling
  - More comfortable (radiators always warm vs. hot/cold cycling)

  Incompatible with: steam systems, some old cast iron at low temps (sludge)
  Required for: getting full benefit from condensing boilers
```

---

## Section 3: Electric Resistance Heating

100% efficient at the point of use — all input electrical energy becomes heat. The catch:
electricity is ~3–4× more expensive per BTU than natural gas in most US markets.

```
  ELECTRIC HEATING TYPES:
  ┌──────────────────┬─────────────────────────────────────────────────┐
  │ Baseboard        │ 240V resistance element + natural convection;   │
  │ convectors       │ silent; no maintenance; zone control per room   │
  │                  │ by individual thermostat; high operating cost   │
  ├──────────────────┼─────────────────────────────────────────────────┤
  │ Electric furnace │ Air handler with resistance strips; same ducts  │
  │                  │ as AC; used where gas not available             │
  ├──────────────────┼─────────────────────────────────────────────────┤
  │ Heat strips in   │ Backup/supplemental in heat pump air handlers;  │
  │ air handler      │ runs only when heat pump insufficient or fails  │
  ├──────────────────┼─────────────────────────────────────────────────┤
  │ Radiant floor    │ Low-watt-density elements in or under floor;    │
  │ (electric)       │ excellent comfort; expensive to operate;        │
  │                  │ good for bathrooms, small areas                │
  ├──────────────────┼─────────────────────────────────────────────────┤
  │ Infrared panels  │ High-temperature radiant; warms occupants       │
  │                  │ directly via radiation; efficient if people     │
  │                  │ in line of sight (garages, outdoor patios)     │
  └──────────────────┴─────────────────────────────────────────────────┘

  WHEN ELECTRIC RESISTANCE MAKES SENSE:
  - Very mild climate (low heating load)
  - No gas service available
  - Very cheap electricity (Pacific Northwest hydro)
  - Small supplemental loads (bathroom floor, garage)
  - Backup in heat pump systems (unavoidable)
```

---

## Section 4: Oil Furnaces

```
  GEOGRAPHY: Northeast US (Maine, Vermont, New Hampshire, Connecticut, New York
             — legacy oil heating due to historical lack of natural gas pipelines)
             ~5.5 million US households use heating oil (declining)

  HOW THEY WORK:
  #2 Fuel oil (similar to diesel) → high-pressure spray gun (burner)
  → ignited by high-voltage transformer spark → combustion in retention head
  → heat exchanger → flue → oil storage tank (above or below ground)

  AFUE: 80–90% (condensing oil furnaces exist, less common)

  CHALLENGES:
  - Oil price volatility ($2–6+/gallon historically)
  - Annual tank inspection/maintenance
  - Underground storage tank (UST) liability (leaks, contamination)
  - Conversion to natural gas or heat pump increasingly common as gas reaches area

  OIL vs GAS COMPARISON:
  Oil furnace at 85% AFUE, $5/gallon, 140,000 BTU/gallon:
  → $5 / (0.85 × 140,000) = $0.000042/BTU

  Gas furnace at 96% AFUE, $1.30/therm, 100,000 BTU/therm:
  → $1.30 / (0.96 × 100,000) = $0.0000135/BTU

  Gas ~3× cheaper per BTU where available
```

---

## Section 5: Wood and Pellet Systems

```
  WOOD STOVES:
  - Not connected to house HVAC system (standalone supplemental heat)
  - EPA Phase 2 rules (2020): ≤2.0 g/hr PM2.5 (certified stoves)
  - Pre-2020 uncertified stoves: 15–30 g/hr (major air quality impact)
  - Requires: UL-listed installation, clearances, chimney liner

  PELLET STOVES:
  - Automated auger feed from hopper (bags of compressed sawdust pellets)
  - Thermostatic control — turn on/off like furnace
  - Much cleaner combustion than wood (≤0.5 g/hr PM2.5)
  - Electric-dependent (auger, controls, igniter)

  WOOD GASIFICATION BOILERS:
  - High-temperature gasification chamber → burns wood gas, not logs directly
  - Very high efficiency (80–90%)
  - Requires large thermal storage tank (batch-fired, not continuous)
  - Underground storage: insulated tank 1,000–4,000 gallons
  - Complex, expensive, rural appropriate

  OUTDOOR WOOD BOILERS (OWB):
  - Boiler outside house (fire risk isolated) → hot water pipes to house
  - Older designs: notorious for smoke/creosote, neighbors complain
  - Phase 2 OWB rules: cleaner combustion required
```

---

## Decision Cheat Sheet

| Situation | Right System |
|---|---|
| New construction, gas available, cold climate | 96%+ condensing gas furnace + AC |
| New construction, any climate, electrification goal | Air-source heat pump (see module 05) |
| No gas service, moderate climate | Heat pump as primary; electric strips as backup |
| Existing oil heat, gas not available | Heat pump as primary with oil backup (dual-fuel) |
| Adding heat to room without ducts | Mini-split heat pump or electric baseboard |
| Best efficiency for hydronic system | Mod-con boiler with outdoor reset control |
| Supplemental heat for garage/workshop | Infrared propane heater or electric radiant panel |
| Retrofit efficiency upgrade, existing boiler | Add outdoor reset control; update zone valves |

---

## Common Confusion Points

**Heat exchanger integrity is a life-safety issue**: combustion gases (CO, CO₂, NOx)
must stay inside the heat exchanger. Cracked heat exchangers leak combustion gases into
supply airflow. CO detectors are mandatory for gas-heated homes. Annual furnace inspection
includes heat exchanger visual check.

**Condensing furnace can't vent into existing B-vent**: the cool, low-velocity flue
gas from a condensing furnace will condense in an oversized B-vent, causing corrosion and
draft problems. Condensing furnaces use 2" PVC pipe. Can't share a chimney.

**Mod-con boiler condensing requires low return water temp**: cast iron baseboard
is designed for 180°F supply water. At 180°F supply, the return is ~160°F — too hot
for condensing. To get 95%+ AFUE, you need radiant floor or oversized baseboard (lower
water temp). Retrofitting mod-con to old high-temp baseboard may not achieve the rated efficiency.

**Steam radiators don't use thermostats per room (one-pipe)**: in one-pipe steam systems,
steam rises and condensate falls through the same pipe. Thermostatic radiator valves don't
work on one-pipe steam (restrict condensate return). Zone control requires separate approaches.
