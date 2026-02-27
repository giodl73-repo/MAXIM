# HVAC Controls

## The Big Picture

Controls sit between the occupant's comfort preference and the mechanical equipment.
The interface has evolved from a bimetal spring to machine-learning algorithms. But the
underlying control architecture — 24VAC signaling in residential, BAS/DDC in commercial —
is fundamentally unchanged for 50+ years.

```
+----------------------------------------------------------------------+
|                    HVAC CONTROLS HIERARCHY                            |
|                                                                      |
|  RESIDENTIAL                         COMMERCIAL                      |
|  -----------                         ----------                      |
|  Occupant comfort preference         Building management requirement  |
|         |                                      |                     |
|  ┌──────┴──────┐                     ┌─────────┴──────────┐         |
|  │ Thermostat  │                     │ BAS (Building       │         |
|  │ (smart/prog)│                     │ Automation System)  │         |
|  └──────┬──────┘                     └─────────┬──────────┘         |
|         |                                      |                     |
|  24V control wiring                  DDC controllers (BACnet/Modbus) |
|         |                                      |                     |
|  ┌──────┴──────┐                     ┌─────────┴──────────┐         |
|  │ Air handler │                     │ AHU, VAV boxes,    │         |
|  │ + Outdoor   │                     │ Chiller, Boiler    │         |
|  │ unit        │                     │ Pumps, Fans (VFD)  │         |
|  └─────────────┘                     └────────────────────┘         |
+----------------------------------------------------------------------+
```

---

## Section 1: Thermostat Evolution

```
  GENERATION 1 — Bimetal strip (1880s–1960s):
  Two metals bonded (different thermal expansion → bends with temperature)
  Contact makes → sends power to furnace; breaks → shuts off
  Very simple; no settings; maintains average temperature in one room

  GENERATION 2 — Mercury tilt switch (1950s–1990s):
  Bimetal strip + glass tube containing mercury
  Tilts with temperature → mercury slides → makes/breaks contact
  Quieter than snap contacts; very accurate; mercury disposal issue
  Now banned in many states; still found in older homes

  GENERATION 3 — Electronic programmable (1980s–2000s):
  Digital temperature sensor; LCD display; 7-day scheduling
  Setback setpoints: lower at night/when away → significant energy savings
  Studies show: rarely programmed by homeowners (same as gen 1 in practice)
  Honeywell T87, T6360 → Honeywell RTH series → millions installed

  GENERATION 4 — Smart/learning (2011+):
  Nest (2011): learned occupancy patterns from adjustments
  Ecobee (2012): remote occupancy sensors, room averaging
  Features: geofencing (phone GPS → away mode); remote app; energy reports;
            demand response (utility pricing); integration with home automation
  Better adoption of setback schedules (app vs. menu-button)
  Energy savings studies: 10–15% average vs generation 3

  GENERATION 5 — Cloud-connected + room sensors:
  Ecobee SmartSensor; remote room sensors average temperatures
  Corrects for thermostat location issue (thermostat in hallway ≠ bedroom comfort)
  Integration: Google Home, Amazon Alexa, Apple HomeKit
```

---

## Section 2: 24V Control Wiring

The universal interface between thermostat and HVAC equipment in residential and light
commercial. A transformer steps 120V down to 24VAC; the thermostat makes/breaks
connections between terminals.

```
  TERMINAL REFERENCE:
  ┌────┬────────────────────────────────────────────────────────────┐
  │ R  │ 24VAC power (hot from transformer)                         │
  │ Rh │ Heating transformer power (separate transformer systems)   │
  │ Rc │ Cooling transformer power (separate transformer systems)   │
  │ C  │ Common — 24VAC return; needed by smart thermostats        │
  │    │ for continuous power; many old systems lack C wire         │
  ├────┼────────────────────────────────────────────────────────────┤
  │ G  │ Fan (air handler blower — runs fan without heating/cooling)│
  │ Y  │ Cooling (energizes compressor contactor on outdoor unit)   │
  │ W  │ Heating (energizes gas valve OR heat strips)               │
  ├────┼────────────────────────────────────────────────────────────┤
  │ O  │ Heat pump reversing valve — energize for COOLING mode      │
  │    │ (most manufacturers: Carrier, Trane, Lennox, York)         │
  │ B  │ Heat pump reversing valve — energize for HEATING mode      │
  │    │ (Carrier/Bryant convention — opposite of O)                │
  ├────┼────────────────────────────────────────────────────────────┤
  │ E  │ Emergency heat — bypasses heat pump, resistance strips only│
  │ Aux│ Auxiliary heat — resistance strips ON with heat pump       │
  ├────┼────────────────────────────────────────────────────────────┤
  │ Y2 │ Second-stage cooling (two-stage compressor)                │
  │ W2 │ Second-stage heating                                       │
  │ G2 │ Second-speed fan                                           │
  └────┴────────────────────────────────────────────────────────────┘

  BASIC COOLING CALL:
  Thermostat closes: R → Y (compressor) + R → G (fan)
  → Outdoor unit starts; blower runs

  BASIC HEATING CALL (gas furnace):
  Thermostat closes: R → W (gas valve) + R → G (fan after ignition)

  HEAT PUMP COOLING CALL:
  Thermostat closes: R → Y + R → G + R → O (or not-B)
  → Reversing valve energized for cooling mode

  HEAT PUMP HEATING CALL:
  Thermostat closes: R → Y + R → G (O or B not energized/energized)
  → Reversing valve in heating position
```

### The C-Wire Problem

```
  Smart thermostats (Nest, Ecobee) need continuous 24V power.
  Old systems often have no C wire at thermostat (4-wire cable only).

  Solutions:
  1. Fish new 5-wire cable to thermostat (best)
  2. "C-wire adapter" kit using existing wires differently
  3. Ecobee Power Extender Kit (steals power from G wire)
  4. Nest "power steal" from R wire (doesn't always work)
  5. Add 24V C-wire transformer at thermostat location
```

---

## Section 3: Staging and Variable-Speed Control

```
  SINGLE-STAGE (conventional):
  Thermostat simple on/off → 100% or nothing
  Short-cycles → poor humidity control → temperature swings

  TWO-STAGE:
  Thermostat sends Y1 → first stage (65% capacity typically)
  If temperature doesn't recover → delay (10 min) → Y1 + Y2 → full capacity
  Longer run times → better dehumidification → more stable temperatures
  Two separate compressor unloaders or two compressor scrolls

  VARIABLE-SPEED (COMMUNICATING SYSTEMS):
  Proprietary digital communication between thermostat and equipment
  ┌────────────────────┬────────────────────────────────────────────┐
  │ Carrier ComfortLink│ iStat series thermostats; Infinity equipment│
  ├────────────────────┼────────────────────────────────────────────┤
  │ Trane ComfortLink  │ Nexia integration                          │
  ├────────────────────┼────────────────────────────────────────────┤
  │ Lennox iComfort    │ iHarmony zoning system                     │
  ├────────────────────┼────────────────────────────────────────────┤
  │ Ecobee/Nest        │ With inverter equipment: uses standard 2-  │
  │ (generic)          │ stage wiring; equipment self-modulates;    │
  │                    │ thermostat just sets demand level          │
  └────────────────────┴────────────────────────────────────────────┘

  Variable-speed advantages:
  - Compressor runs at precisely the load required
  - 25% speed on mild days → quiet, highly efficient, excellent humidity control
  - 100-120% speed on design day → full capacity
  - SEER2 and HSPF2 rating assumes variable-speed operation profile
```

---

## Section 4: Heat Pump Thermostat Logic

Heat pump thermostats are not interchangeable with gas furnace thermostats. The logic
is fundamentally different and getting it wrong causes major efficiency losses.

```
  GAS FURNACE THERMOSTAT:
  Heat call → turn on furnace (W) → heat up fast → shut off
  Efficiency is insensitive to how long it runs

  HEAT PUMP THERMOSTAT (correct):
  Heat call → turn on heat pump (Y + G + O/B)
  Monitor outdoor temp and heat pump performance
  If ΔT (setpoint minus actual) growing slowly → supplemental strip heat (Aux)
  Strips should run ONLY when heat pump genuinely insufficient

  HEAT PUMP THERMOSTAT (wrong):
  Treats heat pump like furnace — ramps up strips quickly
  → Strips run frequently → COP drops to 1.0 → high utility bills
  → Homeowner thinks "heat pump doesn't work" → replaces with gas

  "INTELLIGENT" RECOVERY:
  Smart heat pump thermostats calculate when to start heating in advance
  → Gradual ramp → heat pump runs longer at COP 3.0 vs strips at COP 1.0
  → "Pre-conditioning" timer accounts for outdoor temp

  OUTDOOR TEMP LOCKOUT:
  Some thermostats lock out heat pump below a certain outdoor temp (e.g., 25°F)
  and switch to resistance-only (emergency heat mode)
  → WRONG for cold-climate heat pumps rated to -13°F to -22°F
  → Must configure lockout correctly or disable (use heat pump down to rated temp)
```

---

## Section 5: Commercial Controls — PID, DDC, BAS

### PID Control

```
  PID (Proportional-Integral-Derivative) control:
  The standard algorithm for continuous modulation in commercial HVAC.
  Not on/off — continuously adjusts output to maintain setpoint.

  ERROR = Setpoint - Measured value

  P (Proportional):  output ∝ error
                     Large error → large correction; small error → small correction
                     Alone: causes offset (never exactly reaches setpoint)

  I (Integral):      output += integral of error over time
                     Eliminates steady-state offset; eliminates persistent error
                     Too much I → windup → overshoot

  D (Derivative):    output += rate of change of error
                     Anticipates overshoot; applies braking force
                     Helps on fast-responding systems; risky with noisy sensors

  HVAC PID applications:
  - VAV box damper position (maintains room temperature)
  - AHU supply air temperature (maintains discharge setpoint)
  - Chilled water valve position (maintains zone temperature)
  - Building static pressure (supply fan VFD speed control)
```

### Building Automation System (BAS)

The BAS three-layer hierarchy maps to network control plane architecture: supervisory layer = management plane (analytics, scheduling, alarming); automation layer = control plane (DDC controllers running local PID logic, continue operating if network fails — partition tolerance); field layer = data plane (sensors and actuators). The automation layer's "continue operating if network fails" property is the same partition-tolerance guarantee in distributed systems design. Azure datacenter BMS uses this same hierarchy for chilled water, CRAC units, and power distribution.

```
  BAS HIERARCHY:
  ┌──────────────────────────────────────────────────────────────────┐
  │ SUPERVISORY LAYER (Server/cloud)                                 │
  │ Honeywell Niagara Framework; Siemens Desigo; JCI Metasys         │
  │ Scheduling, reporting, alarming, energy analytics, maintenance    │
  └──────────────────────────────────┬───────────────────────────────┘
                                     |
  ┌──────────────────────────────────┴───────────────────────────────┐
  │ AUTOMATION LAYER (DDC Controllers)                               │
  │ Field panels with PLC-like processors; run PID loops locally     │
  │ Continue operating if network fails (local intelligence)         │
  └──────────────────────────────────┬───────────────────────────────┘
                                     |
  ┌──────────────────────────────────┴───────────────────────────────┐
  │ FIELD LAYER (Sensors and Actuators)                              │
  │ Temperature sensors, pressure sensors, CO₂ sensors               │
  │ Damper actuators, valve actuators, VFD speed references          │
  └──────────────────────────────────────────────────────────────────┘

  PROTOCOLS:
  BACnet (ASHRAE 135): open standard; IP-based (BACnet/IP) or MS/TP serial
                       vendor-neutral; most commercial BAS supports it
  Modbus RTU/TCP:      simple serial protocol from industrial automation
                       most devices support it; read/write registers
  LonWorks:            older proprietary protocol; still in field
  Proprietary:         each major vendor (Siemens, Honeywell, JCI) has native
                       protocol; gateways needed for cross-vendor integration
```

---

## Section 6: Economizers

### Datacenter Free Cooling — The Dominant Application

Hyperscale datacenters (Azure, AWS, Google) are designed around maximizing **economizer hours**: annual hours when outdoor conditions allow free cooling without running chillers. PUE (Power Usage Effectiveness) = total facility power / IT equipment power. Best hyperscale facilities achieve PUE 1.1-1.2 vs inefficient facilities at PUE 2.0+.

```
DATACENTER ECONOMIZER LOGIC:
  Same principle as building economizers — use cold outdoor air
  instead of running chillers when conditions allow.

  Why site selection matters:
  Dublin (Microsoft): ~85% economizer hours/year (cool, humid)
  Des Moines (Facebook): ~70% economizer hours/year
  Phoenix: ~20% economizer hours/year (hot climate)

  ASHRAE TC 9.9 temperature guidelines for IT equipment:
  Class A1: 15-32°C (59-90°F) — standard IT equipment
  Class A4: 5-45°C (41-113°F) — hardened equipment, max economizer hours

  Raising the allowable inlet temperature from A1 to A3/A4 adds
  hundreds of additional economizer hours per year — each degree
  of expanded envelope directly reduces chiller energy.

  Liquid cooling (direct-to-chip, immersion) is the frontier:
  removes the air-side bottleneck entirely, enables higher rack
  density (>30 kW/rack), and allows heat rejection at higher
  temperatures (warm water cooling at 45°C — always above ambient
  in most climates → 100% economizer operation year-round).
```

```
  CONCEPT: When outdoor air is cool/dry enough, use it directly for cooling
  instead of running refrigeration. "Free cooling."

  WHEN IT WORKS:
  Summer night: outdoor 65°F, setpoint 72°F → use outdoor air (no compressor)
  Spring/fall: outdoor 55°F during occupied hours → economizer hours possible

  TYPES:
  ┌──────────────────┬────────────────────────────────────────────────┐
  │ Dry-bulb         │ Open outdoor air damper when outdoor temp      │
  │ economizer       │ below setpoint (e.g., 65°F)                    │
  │                  │ Simple; problem: may bring in humid air at low  │
  │                  │ dry-bulb (enthalpy might be too high)          │
  ├──────────────────┼────────────────────────────────────────────────┤
  │ Enthalpy         │ Measures outdoor + indoor enthalpy (BTU/lb)    │
  │ economizer       │ Open only when outdoor enthalpy < indoor        │
  │                  │ Avoids humid days; more accurate; higher cost   │
  └──────────────────┴────────────────────────────────────────────────┘

  DOE REQUIREMENT: Economizers required in most commercial climate zones
  RESIDENTIAL: Rarely cost-justified (complex controls, modest savings in home)

  FAILURE MODE: Stuck open economizer damper in summer
  → Massive humidity load from outdoor air → comfort problems
  → One of most common BAS diagnostic findings
```

---

## Section 7: Defrost Control (Revisit)

```
  DEFROST TRIGGERS:
  Timer only: runs defrost every 30–90 min regardless
  → Unnecessary defrost cycles in mild conditions = inefficiency

  Demand defrost (preferred): combined logic
  → Timer provides maximum interval
  → Temperature differential across coil indicates frost buildup
  → OR pressure drop sensor (differential pressure across coil)
  → Defrost only when needed → more efficient

  DEFROST SEQUENCE:
  1. Reversing valve → cooling mode (outdoor coil = condenser = hot)
  2. Outdoor fan OFF (retain heat at outdoor coil)
  3. Aux heat strips ON (prevent cold air to house)
  4. Run ~2–5 minutes; coil temp sensor confirms thaw
  5. Return to heating mode; outdoor fan back on

  Homeowner visible: water/steam from outdoor unit, outdoor fan stops
  Duration: 2–5 minutes every 30–90 minutes in icing conditions (normal)
```

---

## Decision Cheat Sheet

| Situation | Solution |
|---|---|
| Upgrade thermostat, no C wire | Ecobee with PEK kit, or fish new 5-wire |
| Heat pump high utility bills | Check thermostat aux heat logic; check lockout settings |
| Multiple zones, single system | Motorized dampers + bypass + variable-speed handler |
| Commercial multi-zone control | VAV boxes with DDC controllers on BACnet |
| Reduce commercial ventilation energy | DCV with CO₂ sensors + economizer |
| Stuck-open economizer (summer humidity problem) | BAS FDD or manual inspection + economizer actuator check |
| New commercial installation | Niagara Framework or Metasys for supervisory |
| Residential smart integration | Ecobee or Nest; configure heat pump logic properly |

---

## Common Confusion Points

**O vs B reversing valve wiring**: Carrier and Bryant energize the reversing valve
for HEATING (B terminal). Every other major manufacturer energizes for COOLING (O terminal).
Wrong configuration → heat pump heats in cooling call and cools in heating call. Symptom:
"my heat pump runs but the house gets colder when I call for heat."

**The missing C wire problem**: generic programmable thermostats (old Honeywells) use
"power stealing" — they grab tiny amounts of current through the load during off cycles.
Smart thermostats need more power continuously. If no C wire, options are limited. The
power stealing approach the Nest uses doesn't work with all equipment (especially high-
efficiency furnaces that don't tolerate tiny current draws through their gas valve).

**Emergency heat is not for cold weather**: Emergency heat bypasses the heat pump entirely
and runs resistance strips only. It exists for when the heat pump has failed mechanically.
Running in emergency heat mode during a cold spell costs 2–4× as much to operate.

**BAS and proprietary lock-in**: Niagara Framework by Tridium (owned by Honeywell)
became the dominant open-integration platform, but the "open" BACnet layer still runs
on top of each vendor's proprietary controller ecosystem. Full cross-vendor interop
requires careful architecture at design time.
