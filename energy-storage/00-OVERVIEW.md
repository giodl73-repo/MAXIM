# Energy Storage — Landscape Overview

## The Big Picture

Energy storage is the enabling technology for renewable energy transition, electric vehicles,
and grid stability. No single technology dominates across all scales and applications.
The choice is determined by energy density, power density, duration, cost, cycle life,
and deployment context.

```
ENERGY STORAGE TECHNOLOGY MAP
==============================

                    HIGH POWER DENSITY
                    (kW/kg or kW/L)
                           ^
                           |
         Supercapacitors   |   Flywheels
                      +----|----+
                      |         |
                      |         |   Li-ion batteries
                      |  POWER  |
   Lead-acid  --------+  GAP   +------- Li-ion NMC
                      |         |
                      |         |   Flow batteries
                      +---------+
                      NaS battery
                           |
         Pumped hydro -----+-----  Compressed air
                           |
                           |  Hydrogen (fuel cell)
                           v
                    HIGH ENERGY DENSITY
                    (kWh/kg or kWh/L)

X-axis (power density): Supercap > Flywheel > Li-ion > Flow > Pumped hydro > H2
Y-axis (energy density): H2 >> Li-ion >> Flow > NaS > Pumped hydro > Supercap
```

### Ragone Plot: Energy Density vs. Power Density

```
RAGONE PLOT (specific energy vs. specific power)
=================================================

Specific      |
Energy        |  Li-S (theoretical)   H2 fuel cell
(Wh/kg)       |                   *  *
  1000 +       |             Li-air *
               |                Li-ion (NMC) *
   300 +       |          NCA *      *
               |     LFP *
   100 +       |  Pb-acid *   NaS
               |             * Flow battery (VRB)
    30 +       |    Supercapacitor
               |  * (EDLC)         Flywheel
    10 +       |
               +--+--------+--------+--------+----
               10  100    1000    10000   100000
                        Specific Power (W/kg)

DISCHARGE TIME BANDS:
  >10 hr: pumped hydro, flow battery, H2
  1-10 hr: Li-ion, NaS, CAES
  0.1-1 hr: lead-acid, some flow
  <0.1 hr: flywheel, supercapacitor

GRID APPLICATIONS BY DURATION:
  Frequency regulation (<1 min): supercapacitor, flywheel, Li-ion
  Spinning reserve (10 min): Li-ion, flywheel
  Capacity shifting (1-4 hr): Li-ion, NaS
  Long duration (4-100 hr): flow battery, pumped hydro, CAES, H2
  Seasonal storage (weeks-months): H2, pumped hydro
```

---

## Storage Technology Categories

```
FIVE CATEGORIES OF GRID STORAGE
=================================

1. ELECTROCHEMICAL
   +-------------------------------------------+
   | BATTERIES: convert chemical energy <-> electrical energy
   | via electrochemical reactions at electrodes
   |
   | Li-ion: 150-300 Wh/kg, 80-95% RTE, 1-4 hr
   | Flow: 20-50 Wh/L (external tank), 65-80% RTE, 2-20 hr
   | Lead-acid: 30-50 Wh/kg, 70-85% RTE, 2-8 hr
   | NaS (sodium-sulfur): 150 Wh/kg, 70-80% RTE, operates at 300 C
   |
   | Supercapacitors (EDLC): electrostatic (no reaction)
   |   1-10 Wh/kg, 95%+ RTE, <1 min
   +-------------------------------------------+

2. MECHANICAL
   +-------------------------------------------+
   | Pumped hydro: E = mgh, 70-85% RTE
   |   1,600 GW deployed -- 96% of all grid storage
   | CAES: compressed air, 40-70% RTE (diabatic vs. adiabatic)
   | Flywheel: kinetic energy, 85-95% RTE, short duration
   | Gravity: mass raised, potential energy
   +-------------------------------------------+

3. THERMAL
   +-------------------------------------------+
   | Sensible heat: molten salt (CSP), water, rocks
   |   ETES (Electric Thermal Energy Storage)
   | Latent heat: phase change materials (PCM)
   |   Ice storage, paraffin wax, salt hydrates
   | Thermochemical: reversible reactions
   +-------------------------------------------+

4. CHEMICAL (Hydrogen and Derivatives)
   +-------------------------------------------+
   | Electrolysis: electricity -> H2
   | Compression/liquefaction: store H2
   | Fuel cell: H2 -> electricity
   | Chemical carriers: ammonia, LOHC
   | Round-trip: ~25-40% (electrolysis x FC)
   +-------------------------------------------+

5. BIOLOGICAL/OTHER
   +-------------------------------------------+
   | Batteries with bio-electrodes (research)
   | Biofuels (not storage per se, but renewable chemical energy)
   +-------------------------------------------+
```

---

## Round-Trip Efficiency (RTE) by Technology

| Technology | RTE (%) | Notes |
|------------|---------|-------|
| Supercapacitor (EDLC) | 95-98 | Near-lossless; tiny energy, high power |
| Lithium-ion (NMC/NCA) | 90-95 | Best battery RTE; charge/discharge losses |
| Lithium-ion (LFP) | 92-96 | Slightly better RTE than NMC |
| Lead-acid | 70-85 | Gassing losses; worse at high rate |
| Flywheel | 85-95 | Air drag and bearing losses |
| Pumped hydro (variable speed) | 78-82 | Head losses, turbomachinery efficiency |
| Pumped hydro (fixed speed) | 70-78 | Less efficient at partial load |
| Vanadium flow battery | 65-80 | Pumping power, shunt currents |
| NaS battery (NGK) | 75-80 | High-temp operation loss |
| CAES (adiabatic, A-CAES) | 60-70 | Compression heat stored + reused |
| CAES (diabatic, burn gas) | 42-55 | Heat input required; not pure storage |
| Hydrogen (elec. + compression + FC) | 25-40 | Large losses each step |
| Liquid air (LAES) | 50-60 | Liquefaction energy cost |

---

## Deployment Scale Context

```
STORAGE BY SCALE
=================

IoT / Wearables (mWh - Wh):
  Li-ion coin cells, LiPo
  Ultra-thin, flexible batteries
  Energy harvesting (piezo, solar) supplements storage

Consumer Electronics (1-100 Wh):
  Li-ion 18650, pouch cells
  iPhone 14: 12 Wh; MacBook: 100 Wh
  Daily cycle; 2-5 year product life

EV (20-100 kWh):
  Li-ion (NMC or LFP packs)
  Tesla Model 3 LR: 82 kWh
  BYD Atto 3: 60 kWh LFP
  1 full charge/day nominal; 2000+ cycle life target

Commercial BESS (1-100 MWh):
  Container-based Li-ion
  Hornsdale (Australia): 129 MWh LFP (Tesla Megapack)
  Frequency regulation, peak shifting

Grid-Scale (100 MWh - 10 GWh):
  Li-ion: dominates new deployments 2020-2030
  Flow batteries: growing (4-12 hr applications)
  Pumped hydro: existing installed base, new projects slow
  Target: co-locate with solar/wind to shift generation

Seasonal/Long-Duration (GWh - TWh):
  Pumped hydro: the only proven technology at this scale
  Hydrogen: long-term potential for seasonal storage
  LDES (Long-Duration Energy Storage): active R&D (ARPA-E DAYS)
  Iron-air (Form Energy): first commercial deployments ~2024-2025
```

---

## Cross-References Within This Directory

| File | Content |
|------|---------|
| 01-ELECTROCHEMICAL.md | Nernst, Butler-Volmer, SEI, overpotentials |
| 02-LITHIUM-ION.md | Cathode chemistries, anode, BMS, degradation |
| 03-ADVANCED-BATTERIES.md | Solid-state, Na-ion, Li-S, Li-air |
| 04-FLOW-BATTERIES.md | Vanadium redox, iron-air, architecture |
| 05-PUMPED-HYDRO.md | E=mgh, efficiency, global installed base |
| 06-COMPRESSED-AIR.md | CAES diabatic/adiabatic, LAES, gravity storage |
| 07-HYDROGEN.md | Electrolysis types, storage methods, fuel cell, economics |
| 08-GRID-ECONOMICS.md | LCOS, learning curves, revenue stacking, duck curve |
| 09-FUTURE.md | LDES roadmap, thermal, long-duration targets |

---

## Common Confusion Points

**"Batteries are the future of grid storage."** Li-ion batteries dominate SHORT-duration
grid storage (1-4 hours). For 10+ hour storage, the economics are very different -- pumped
hydro dominates today; flow batteries and long-duration storage are needed at scale for
100% renewable grids.

**"Efficiency is the main metric."** It is one metric. A 95% efficient technology that
costs $1000/kWh loses to a 75% efficient technology at $20/kWh for long-duration grid
storage where capital cost dominates. The relevant metric is Levelized Cost of Storage (LCOS).

**"Hydrogen is just a battery."** Hydrogen is a chemical fuel that can be produced from
electricity and converted back to electricity. The round-trip efficiency (~30-40%) is much
lower than batteries (~90-95%), but hydrogen offers seasonal storage and energy carrier
properties (transport, industrial feedstock) that batteries do not.

**"Pumped hydro is dead technology."** It is 96% of global grid storage by energy today
and will remain the dominant long-duration technology for decades. Its limitations
(geography, long build times) prevent rapid expansion, but it is not obsolete.
