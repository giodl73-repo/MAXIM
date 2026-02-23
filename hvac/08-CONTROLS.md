# 08 — Controls

## Thermostats, 24V Wiring, BAS, Smart Controls, Heat Pump Logic

> **STUB** — outline only, content to be authored

**Planned coverage:**
- **Thermostat evolution**: bimetal strip (two metals bonded, different thermal expansion rates → bends with temperature → makes/breaks contact → simple on/off); mercury tilt switch (bimetal + glass tube of mercury → quiet, but mercury disposal issue); electronic programmable (1980s-90s — setback scheduling → significant energy savings, underutilized in practice); wireless/WiFi smart thermostats (Nest 2011, Ecobee 2012 → learning algorithms, geofencing, remote access, energy reporting); occupancy and room sensors
- **24V low-voltage control wiring** (the standard interface): HVAC equipment uses 24VAC control circuit; transformer steps down 120V to 24V; thermostat simply makes/breaks connections between terminals:
  - R (or Rh/Rc): 24VAC power (hot)
  - C: common (24VAC return) — needed for smart thermostats requiring power
  - G: fan on (activates air handler blower)
  - Y: cooling (activates compressor contactor)
  - W: heating (activates gas valve or heat strips)
  - O or B: reversing valve (heat pump) — O=energize for cooling (most), B=energize for heating (Carrier/Bryant)
  - E: emergency heat (bypasses heat pump, activates backup resistance)
  - Aux: auxiliary/supplemental heat (activates backup heat along with heat pump)
  - Y2, W2, G2: second-stage cooling, heating, fan for two-stage systems
- **Staging and variable-speed control**: single-stage = on/off; two-stage = thermostat sends Y1 for first stage, Y1+Y2 for second (if demand not met after delay); variable-speed (communicating) systems use proprietary protocols (Carrier ComfortLink, Trane ComfortLink, York iComfort) — thermostat communicates digitally with equipment, equipment self-modulates; or Ecobee/Nest uses simple two-stage wiring with variable-speed equipment doing its own modulation
- **Heat pump thermostat logic**: critical difference from gas furnace; must prevent resistance backup (aux heat) from running when not needed (efficiency penalty); smart thermostat knows heat pump capacity at current conditions; "lockout" temperature (if outdoor temp below setpoint, lock out heat pump → only resistance); proper heat pump thermostat enables heat pump down to rated low-temp, uses resistance only when heat pump genuinely insufficient; oversimplified thermostat (treats heat pump like furnace) causes frequent aux heat → high utility bills
- **PID control in commercial HVAC**: commercial systems use PID (proportional-integral-derivative) control for continuous modulation; not on/off; maintains precise temperature and pressure setpoints; variable air volume (VAV) systems modulate airflow per zone; variable frequency drives (VFD) on fans and pumps → energy savings at part load; building pressurization control
- **BAS (Building Automation System)**: commercial HVAC, lighting, access control, elevators integrated into one supervisory control system; Honeywell Niagara, Siemens Desigo, Johnson Controls Metasys; BACnet (ASHRAE standard open protocol) and Modbus (industrial serial) as dominant protocols; IP-based integration; analytics, predictive maintenance; fault detection and diagnostics (FDD) algorithms identify stuck dampers, sensor failures, mechanical issues from data trends; edge computing in modern BAS
- **Economizer (free cooling)**: when outdoor conditions are acceptable, bypass refrigeration and cool with 100% outdoor air; dry-bulb economizer (outdoor temp below setpoint), enthalpy economizer (outdoor enthalpy below indoor — avoids bringing in humid air when dry-bulb would otherwise call for OA); DOE requires economizers in most commercial zones; residential rarely used (cost)
- **Defrost control**: heat pump outdoor coil in heating mode can frost when outdoor temp ≤35°F and coil is below freezing; frost reduces airflow and heat transfer; defrost cycle: reverse to cooling mode briefly (outdoor coil = condenser, melts frost); triggered by timer + temperature sensor, or demand-defrost (pressure drop across coil indicates frost buildup); backup heat runs during defrost to prevent cold air delivery; defrost cycle = expected normal operation, not a malfunction
