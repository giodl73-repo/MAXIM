# Flow Batteries: Architecture, Vanadium Redox, and Iron-Air

## The Big Picture

Flow batteries decouple energy capacity (tank size) from power rating (electrochemical
stack size). This separation is architecturally significant: it is the battery equivalent
of a gas turbine where fuel storage is separate from the engine. It makes flow batteries
ideal for long-duration grid storage where Li-ion's fixed energy/power ratio is a constraint.

```
FLOW BATTERY ARCHITECTURE
===========================

                 POWER SUBSYSTEM              ENERGY SUBSYSTEM
                 ================             =================

           +--- ELECTROCHEMICAL STACK ---+   +--- ELECTROLYTE TANKS ---+
           |                             |   |                          |
           |  NEGATIVE        POSITIVE   |   |  Negative    Positive    |
           |  ELECTRODE       ELECTRODE  |   |  electrolyte electrolyte |
           |    |                  |    |   |  (reduced)   (oxidized)  |
    e- <---|----+------------------+-----|   |   [Tank A]    [Tank B]   |
           |    |                  |    |   |                          |
           | Ion-exchange membrane |    |   +----+-----+   +-----+----+
           |    |  (H+, Cl-...) |  |    |        |     |         |    |
           +----+---------------+--+    |       Pump       Pump       |
                |               |       +-------+-----+---+-----+-----+
                |               |               |         |
           Flow in          Flow out     Electrolyte circulates through stack

KEY DISTINCTION FROM LI-ION:
  Li-ion: energy stored IN solid electrodes (fixed per cell design)
  Flow: energy stored IN external liquid tanks (changeable, scalable)

  Scale up ENERGY: add bigger tanks (cheap)
  Scale up POWER:  add more cell stacks (expensive, fixed cost per kW)
```

### Power vs. Energy Cost

```
COST STRUCTURE COMPARISON
===========================

LI-ION:
  Energy and power inextricably linked
  Adding kWh also adds kW (same cell adds both)
  $/kWh and $/kW scale together

FLOW BATTERY:
  Power: stack (electrode + membrane + bipolar plates): ~$200-400/kW (expensive)
  Energy: tanks + electrolyte: $20-150/kWh (cheap at long duration)

  Cost break-even vs. Li-ion: ~4-8 hours duration
  At <4 hr: Li-ion wins (stack cost dominates, energy cheap for Li-ion)
  At >8 hr: Flow wins (tank cost cheap, Li-ion needs proportionally more expensive cells)

  For 12-hour storage:
    Li-ion: ~$250-400/kWh (cell cost x 12h duration)
    VRB: ~$150-250/kWh (fixed stack cost amortized over 12h, cheap vanadium tanks)
```

---

## Vanadium Redox Flow Battery (VRFB / VRB)

### Chemistry and Structure

```
VRFB CHEMISTRY
===============

NEGATIVE ELECTRODE (anode during charge, cathode during discharge):
  V3+ + e- -> V2+  (charge, reduction, E° = -0.26 V vs. SHE)
  V2+ -> V3+ + e-  (discharge, oxidation)

POSITIVE ELECTRODE (cathode during charge, anode during discharge):
  VO2+ + H2O -> VO2+ + 2H+ + e-  (charge, oxidation)
  VO2+ + 2H+ + e- -> VO2+ + H2O  (discharge, reduction)
  E° = +1.00 V vs. SHE

FULL CELL:
  V2+ | membrane | VO2+  discharge: cell voltage ~ 1.26 V (standard)
  V3+ | membrane | VO2+  fully discharged: lower voltage
  Open circuit at full SOC: ~1.4-1.6 V (concentration-dependent via Nernst)

KEY ADVANTAGE -- SAME ELEMENT IN BOTH TANKS:
  Cross-contamination does NOT permanently degrade electrolyte
  If V2+ crosses membrane to VO2+ tank: both become a mix of V(II) and V(V)
  -> Re-charge restores separation
  Vs. other flow chemistries (Fe/Cr, Zn/Br): cross-contamination = irreversible contamination

  This is why VRFB has 10,000+ cycle life claim (vs. ~2000 for most batteries)
  Electrolyte degradation mechanism: HVO4- formation at high T (>45 C)
    Reversible if kept in temperature range; manageable
```

### VRFB Performance Specifications

```
VRFB PERFORMANCE (commercial systems, 2025)
=============================================

Parameter              Value                 Notes
---------------------  --------------------  --------------------------------
Cell voltage           1.25-1.55 V           SOC dependent (Nernst)
Stack power density    60-100 mW/cm^2        Improving with better membranes
Specific energy        20-40 Wh/L            Lower than Li-ion (liquid electrolyte)
                       15-30 Wh/kg           (includes tank + electrolyte mass)
Round-trip efficiency  65-80%                Depends on C-rate and system
Cycle life             10,000+ cycles        Electrolyte doesn't degrade (V is stable)
Calendar life          25+ years             Tank and stack life (stack < tank)
Self-discharge         Low (pump off: none)  Electrolyte in separate tanks
Temperature range      10-40 C (optimal)     Below 10 C: V2+ precipitation risk
                                             Above 45 C: electrolyte degradation risk
Response time          <100 ms (power)       Pumps add seconds for standby
Depth of discharge     100% (safe)           Unlike Li-ion (limit to 80% for life)

VANADIUM COST:
  V2O5 feedstock: ~$5-10/kg (2024, was $40/kg in 2018 -- volatile)
  Electrolyte: ~$20-40/kWh (at current V prices)
  Total installed VRFB system: $200-400/kWh (2025)
  Projected 2030: $150-250/kWh (learning curve + V price normalization)
```

### Commercial Deployments

Notable VRFB installations:

| Project | Location | Scale | Year | Notes |
|---------|----------|-------|------|-------|
| Rongke Power, Dalian | China | 200 MW / 800 MWh | 2022 | Largest in world |
| Sumitomo Electric, Hokkaido | Japan | 15 MW / 60 MWh | 2015 | Wind balancing |
| Invinity / Pacific Crest | Various | 1-10 MW | 2022+ | Multiple sites |
| Largo Clean Energy | US | 3-10 MW pilot | 2021 | V from mine operations |

---

## Iron-Air Batteries (Form Energy)

### Chemistry and Promise

```
IRON-AIR BATTERY
==================

NEGATIVE ELECTRODE (iron): Fe + 2OH- -> Fe(OH)2 + 2e-  (discharge oxidation)
POSITIVE ELECTRODE (air):  1/2 O2 + H2O + 2e- -> 2OH-  (discharge reduction)

OVERALL: Fe + 1/2 O2 + H2O -> Fe(OH)2  (rust formation -- discharge)
CHARGE:  Fe(OH)2 + 2e- -> Fe + 2OH-    (un-rust -- charge)

KEY INSIGHT:
  This is literally controlled rusting and un-rusting
  Iron: $0.05/kg (most abundant and cheap structural metal)
  Oxygen: free from air (like Li-air, cathode is open to atmosphere)
  Alkaline electrolyte: KOH (cheap)

  This is why Form Energy claims $20/kWh cost target -- raw materials are trivially cheap

THEORETICAL ENERGY DENSITY:
  Fe theoretical: 960 mAh/g (2-electron)
  Average cell voltage: ~1.0 V (lower than Li-ion)
  Theoretical: ~960 Wh/kg (Fe only)
  Practical (with iron electrode, KOH, air electrode, housing): ~50-100 Wh/kg
  Lower than Li-ion BUT: $20/kWh target vs. $80-100/kWh for Li-ion
  Energy density doesn't matter for stationary storage: only $/kWh counts

ADVANTAGES:
  Abundant, cheap materials (Fe, O2, KOH)
  Non-toxic, non-flammable (no organic electrolyte)
  Long duration: designed for 100+ hours (vs. 4-hour Li-ion)
  Fully dischargeable (100% DoD safe)
  Calendar life: 20+ years target (iron doesn't dissolve)

CHALLENGES:
  ROUND-TRIP EFFICIENCY: ~45% (vs. 90-95% Li-ion)
    Iron electrode: significant overpotential (charge voltage >> discharge voltage)
    Air electrode: oxygen reduction is kinetically slow (same problem as fuel cells)
    Hydrogen evolution: side reaction at iron anode during charging steals current
  SLOW CHARGE/DISCHARGE: designed for multi-day operation, not fast response
  HYDROGEN EVOLUTION (HER): Fe electrode competes with 2H2O + 2e- -> H2 + 2OH-
    H2 produced during charging (small amount): must be managed/vented
    HER reduces Coulombic efficiency; hydrogen safety in enclosed space
  POWER DENSITY: ~100 W/m^2 (very low) -- requires large electrode area for power
```

### Form Energy and Iron-Air Status

```
FORM ENERGY (Cambridge, MA -- founded 2017)
============================================

Technology: Iron-air battery for 100-hour grid storage
Target cost: <$20/kWh (vs. Li-ion ~$80-100/kWh for 4-hr systems)
Target RTE: 45% (acceptable for long-duration arbitrage given low cost)

Timeline:
  2021: $240M Series D (Bill Gates' Breakthrough Energy Ventures, Eni)
  2022: Factory announcement (Weirton, WV -- former steel plant)
  2023: First customer pilot deployments (Georgia Power)
  2024-2025: Factory production scaling
  2026+: Grid-scale deployments

Why 45% RTE is acceptable economically:
  Arbitrage: buy electricity at $20/MWh (night), sell at $100/MWh (peak)
  Even at 45% RTE: store 1 MWh, recover 0.45 MWh
  Revenue: 0.45 * $100 = $45, Cost: 1.0 * $20 = $20 -> Margin: $25/MWh stored
  Compare: Li-ion at 90% RTE: 0.9 * $100 = $90, Cost: $20 -> Margin: $70/MWh
  Li-ion better revenue per cycle, but MUCH higher capital cost
  Iron-air: ~$1,000-1,500/kW (power), $20/kWh (energy) -- capital very cheap for 100-hr
```

---

## Other Flow Battery Chemistries

```
FLOW BATTERY CHEMISTRY ALTERNATIVES
======================================

ZINC-BROMINE (Zn/Br2):
  Negative: Zn2+ + 2e- -> Zn   (E = -0.76 V)
  Positive: Br2 + 2e- -> 2Br-  (E = +1.07 V)
  Cell voltage: ~1.83 V (high voltage for flow battery)
  Energy density: ~60-80 Wh/L (high for flow; Br2 complexed to reduce vapour pressure)
  Challenge: Br2 is corrosive, toxic; Zn dendriting if poorly managed
  Companies: RedT, ZBB Energy, Eos Energy (hybrid: zinc-manganese)

IRON-CHROMIUM (Fe/Cr):
  Historical first (NASA 1970s)
  E_cell ~ 1.0 V; cross-contamination problem (different metals -- permanent)
  Lower RTE (~65%), catalyst needed for Cr2+/Cr3+ kinetics
  Low material cost; being revisited by EnergyNor, Jing New Energy

ORGANIC FLOW (quinone-based):
  Quinone/hydroquinone redox couples (carbon-oxygen molecules from biomass)
  Neutral pH: safer than acid/base aqueous systems
  Theoretical low cost (organic synthesis from renewable feedstocks)
  Challenges: quinone degradation mechanisms; commercial maturity low
  Harvard, Kemiwatt, CMBlu developing

AQUEOUS ORGANIC HYBRID:
  Organic negative, bromine positive: voltage ~1.0 V
  High energy density, non-toxic negative, but Br2 concern remains

COMPARISON:
  Technology    Cell V   Energy/L    RTE    Maturity     Cost Target
  VRFB           1.26V   20-40 Wh/L  65-80%  Commercial  $150-250/kWh
  Zn-Br          1.83V   60-80 Wh/L  65-75%  Limited commercial  $150/kWh
  Fe-air         1.0V    50-100 Wh/L  45%    Pilot       $20-30/kWh
  Organic        ~0.8V   20-30 Wh/L  ~75%   Research    $100/kWh (target)
```

---

## Decision Cheat Sheet

| Requirement | Technology |
|-------------|-----------|
| 4-8 hour grid storage, proven | VRFB or Li-ion (depending on cost/duration) |
| 8-24 hour grid storage | VRFB (better economics than Li-ion at long duration) |
| 24-100+ hour grid storage | Iron-air (if available) or pumped hydro |
| High cycle life (>10,000) | VRFB |
| Lowest cost long-duration | Iron-air ($20/kWh target) |
| Commercial-ready today | VRFB (Rongke, Invinity) |
| High energy density flow | Zn-Br or next-gen organic |
| Electrolyte reusable / reclaimed | VRFB (vanadium recoverable at end of life) |

---

## Common Confusion Points

**"Flow batteries have low energy density -- that's their weakness."** For stationary
storage, volumetric energy density is usually not the constraint. Land and building
footprint are available at grid scale. The constraint is $/kWh -- where flow batteries
compete well at long duration. Energy density matters for EVs and portable devices,
not for grid storage buildings.

**"VRFB round-trip efficiency of 65-80% vs. Li-ion 90-95% is disqualifying."** Only for
applications where energy efficiency matters a lot (peak shaving, frequency regulation).
For long-duration arbitrage, capital cost amortization over many cycles can overcome the
efficiency gap. At $150/kWh vs. $350/kWh for equivalent-duration Li-ion, the economics
can favor VRFB despite lower RTE.

**"Vanadium is rare and expensive."** Vanadium is the 20th most abundant element in
Earth's crust (~150 ppm, similar to zinc and nickel). The price volatility is from market
structure (most V produced as byproduct of steel and oil refining), not absolute scarcity.
VRFB deployments will increase V demand, which will drive more dedicated V mining and
price stabilization.

**"Iron-air 45% RTE is too low for grid storage."** For long-duration storage used for
seasonal/multi-day balancing, efficiency is less critical than capital cost. Solar
electricity costs <$20/MWh at scale in 2025 -- a 55% efficiency loss means you're
paying $20/0.45 = $44/MWh for stored electricity. If peak power is worth $100-200/MWh,
the arbitrage still works with iron-air economics.
