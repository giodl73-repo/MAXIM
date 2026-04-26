# Lithium-Ion Batteries: Cathode Chemistry, Anodes, BMS, Degradation

## The Big Picture

Li-ion battery performance, cost, and safety are determined primarily by cathode chemistry.
The anode is dominated by graphite (mature, stable) but silicon is entering.
The Battery Management System (BMS) is the software/hardware layer that makes Li-ion
safe and reliable -- analogous to an OS managing unreliable hardware.

```
LI-ION CELL ARCHITECTURE
===========================

               CATHODE (positive)           ANODE (negative)
               ==================           ================
MATERIALS:     LiMO2 or LiFePO4            Graphite (LiC6) or Si
REACTION:      LiMO2 <-> Li(1-x)MO2 + xLi+ Graphite + xLi+ + xe- <-> LixC6
VOLTAGE:       ~3.0-4.5 V vs. Li/Li+        ~0.01-0.3 V vs. Li/Li+
CAPACITY:      100-250 mAh/g                372 mAh/g (graphite)

CELL CONSTRUCTION:
  Cathode: AM powder + carbon black (conductive) + PVDF binder -> coat on Al foil
  Anode:   AM powder + carbon black + CMC/SBR binder -> coat on Cu foil
  Separator: polyethylene (PE) or polypropylene (PP), 20-40 um, porous
  Electrolyte: LiPF6 in EC/EMC/DMC (fills separator and electrode pores)

  Formats:
    Cylindrical: 18650 (18mm x 65mm), 21700 (21mm x 70mm, Tesla standard)
    Prismatic: rigid metal or plastic case (EV packs, grid storage)
    Pouch: flexible laminate, highest energy density (EV, consumer)

CELL VOLTAGE NOMINAL: ~3.6-3.7 V (NMC); 3.2 V (LFP)
```

---

## Cathode Chemistries

### LFP: Lithium Iron Phosphate (LiFePO4)

```
LFP CATHODE
============

Crystal structure: olivine (Pnma space group)
  PO4 tetrahedra stabilize structure -- key to thermal stability
  Li in 1D channels (limited rate capability vs. layered oxides)

ELECTROCHEMISTRY:
  Discharge: LiFePO4 -> FePO4 + Li+ + e-  (Fe3+/Fe2+ couple)
  Charge:    FePO4 + Li+ + e- -> LiFePO4
  E° ~ 3.45 V vs. Li/Li+ (3.2 V nominal cell voltage with graphite anode)
  Flat voltage plateau (two-phase reaction: LiFePO4 <-> FePO4)
    -> very flat discharge curve (good for SOC estimation by capacity counting;
       bad for OCV-based SOC estimation -- flat = ambiguous)

PROPERTIES:
  Specific capacity:   170 mAh/g (theoretical, ~160 mAh/g practical)
  Energy density:      ~90-120 Wh/kg (cell level, lower voltage hurts)
  Cycle life:          3000-10,000+ cycles to 80% capacity
  Temperature range:   -20 to 60 C (more tolerant than NMC)
  Thermal runaway:     Onset >270 C (vs. NMC ~180 C)
  Cost:                Lowest among Li-ion cathodes (no Co, no Ni)
  Mn/Co/Ni content:    None (Fe and P only with Li)

APPLICATIONS:
  Grid energy storage (dominant)
  Commercial EVs: BYD Han, Tesla Model 3/Y (Standard Range)
    BYD "Blade Battery": LFP cell-to-pack, eliminates module
  E-buses, e-trucks (long cycle life, thermal safety preferred over energy density)
  Stationary backup power
  Grid ESS (Tesla Megapack: LFP as of 2021)

LFP vs. NMC for EV (2025):
  LFP: $55/kWh cell cost vs. NMC: $70-80/kWh cell cost
  LFP: 250 Wh/kg vs. NMC: 300 Wh/kg
  LFP wins on cost and cycle life; NMC wins on range (more kWh per kg)
```

### NMC: Lithium Nickel Manganese Cobalt Oxide

```
NMC CATHODE (LiNixMnyCozO2, x+y+z=1)
========================================

Crystal structure: layered oxide (R-3m, alpha-NaFeO2 type)
  Li layers interleave with transition metal layers
  Li+ diffuses in 2D planes -- high rate capability vs. LFP 1D channels

COMPOSITION VARIANTS:
  NMC 111 (equal Ni:Mn:Co = 1:1:1):
    E ~ 3.7 V; capacity ~160 mAh/g; first commercial NMC; stable
  NMC 532 (Ni:Mn:Co = 5:3:2):
    E ~ 3.7 V; capacity ~170 mAh/g; improved energy over 111
  NMC 622 (6:2:2):
    E ~ 3.7 V; capacity ~180 mAh/g; higher energy, less Co
  NMC 811 (8:1:1):
    E ~ 3.7 V; capacity ~200 mAh/g; highest energy density (highest Ni)
    Thermal runaway onset: ~180 C (more reactive at high SOC)
    Li/Ni mixing: Ni2+ (similar size to Li+) disordering at high Ni content
    Requires careful synthesis; more reactive cathode surface
    Used in: Panasonic 21700, LG, SK cells for premium EVs

COBALT:
  Co stabilizes structure and improves electronic conductivity
  High cost: ~$30/kg (volatile -- DRC mining concentration)
  Supply chain concerns: cobalt-free or low-cobalt is major research push
  NMC 811 reduces Co from 33% to 10% vs NMC111 (by molar)

HIGH-VOLTAGE NMC (4.4-4.5 V cutoff):
  More Li extracted -> higher capacity (>220 mAh/g for NMC811)
  Requires electrolyte additives or high-voltage electrolyte
  Cycle stability challenge: more aggressive for electrolyte and cathode surface
```

### NCA: Lithium Nickel Cobalt Aluminum Oxide

```
NCA CATHODE (LiNi0.8Co0.15Al0.05O2)
======================================

Similar to NMC but Al replaces Mn
Al substitution: improves thermal stability vs. pure LiNiO2

Properties:
  Capacity: ~200 mAh/g
  Voltage: ~3.7 V nominal
  Energy: ~300+ Wh/kg cell level (Tesla Model S / 3 original)

Tesla's original chemistry (Panasonic 18650 cells):
  NCA cathode, graphite (with trace Si) anode
  High energy density at premium price and complexity
  Thermal management: liquid cooling system (Octovalve, glycol loop) critical

NCA vs. NMC811:
  Similar energy density
  NCA: slightly better cycle life in some implementations
  Both trending toward lower Co content
  NMC811 has largely displaced NCA in new designs
```

### LMO and LNMO

```
LMO (LiMn2O4): spinel structure
  Capacity: ~100-120 mAh/g
  Voltage: 4.0 V (Mn4+/Mn3+ couple)
  Advantages: low cost, Mn abundant, no Co/Ni
  Disadvantages: capacity fade (Mn dissolution into electrolyte, Jahn-Teller distortion)
  Use: blended with NMC to reduce cost (Nissan Leaf Gen 1)

LNMO (LiNi0.5Mn1.5O4): high-voltage spinel
  Voltage: 4.7 V (Ni4+/Ni2+ couple, two-electron)
  Capacity: ~130-140 mAh/g
  Challenge: needs high-voltage electrolyte stable at 4.7 V
  Mn3+ content very low: minimal Jahn-Teller, good cycle stability in theory
  Status: in research; limited commercial deployment
```

---

## Anode Materials

```
ANODE COMPARISON
=================

Material     E vs Li/Li+   Capacity       Volume change  Status
-----------  ------------  -------------  -------------  ----------------
Graphite     0.01-0.2 V    372 mAh/g      ~10%           Production standard
Lithium      0 V           3860 mAh/g     200%+ (plating  Experimental (solid-state)
metal                      (theoretical)  instability)
Silicon      0.05-0.4 V    3579 mAh/g     ~300%          Partial (5-15% in graphite)
             (alloy)       (Li15Si4)
Silicon-C    0.05-0.4 V    800-1500 mAh/g  50-100%       Emerging (Amprius, etc.)
composite
Li4Ti5O12   1.5 V         175 mAh/g      ~0%           Niche (fast charge,
(LTO)                                                   no SEI, long life)
SnO2         0.5-0.8 V    790 mAh/g      250%          Research
```

**Graphite anode details:**
- Intercalation mechanism: Li inserts between graphene layers
- Staging: different LixC6 phases (Stage 4, 3, 2, 1) with characteristic voltages
- Fully lithiated: LiC6 (1 Li per 6 C atoms = 372 mAh/g)
- Volume change: 10.1% (manageable; stable SEI formation)
- Commercial types: natural graphite (higher capacity, more reactive) vs.
  synthetic graphite (more consistent, harder, better calendar aging)

---

## Battery Management System (BMS)

The BMS is the embedded control system that manages the battery pack -- analogous to
a hypervisor managing hardware resources to guarantee safety and performance.

```
BMS ARCHITECTURE
=================

                    +------------------+
                    |   VEHICLE / EMS  |  (Higher-level energy management)
                    +--------+---------+
                             | CAN / LIN / Ethernet
                    +--------+---------+
                    |    MASTER BMS    |  (Pack-level: SOC, SOH, thermal)
                    +--+-------+---+--+
                       |       |   |
           Cell voltage| Cell  | Temperature sensors
           monitoring  | balance| (NTC thermistors)
                       |       |
                    +--+---+ +-+-----+
                    | SLAVE| | SLAVE |  (Module-level)
                    | BMS  | | BMS   |
                    +--+---+ +--+----+
                       |        |
               +---+---+   +---+---+
               | Cell  | | | Cell  |
               | stack| | | stack  |
               +------+   +-------+

BMS FUNCTIONS:
  1. Cell voltage monitoring (every cell, 1-10 ms)
     Resolution: 0.1-1 mV
     Purpose: detect overvoltage (>4.2V for NMC = electrolyte oxidation)
              detect undervoltage (<2.5-3.0V = copper dissolution from anode)

  2. Current measurement (Hall effect or shunt resistor)
     Used for: Coulomb counting SOC estimation, overcurrent protection

  3. Temperature monitoring
     Multiple NTC sensors per module
     Charge inhibit if T < 0 C (Li plating risk)
     Discharge limit if T < -20 C
     Shutdown if T > 60 C
     Thermal runaway detection: rapid dT/dt rise

  4. Cell balancing
     Passive balancing: bleed energy from high-SOC cells via resistor
       Simple, cheap, generates heat, wastes energy
       Bleed current: 10-100 mA; balancing while charging (not discharging)
     Active balancing: transfer energy from high to low cells
       Switched capacitor, inductor, or transformer-based
       More complex, more expensive, energy-efficient
       Used in: premium EVs (some Teslas), grid storage with wide SOC variation

  5. SOC estimation
     Coulomb counting + EKF (Extended Kalman Filter)
     Input: V, I, T; Output: SOC estimate
     Accuracy: +/- 1-3% in well-designed BMS
     Error source: Coulomb efficiency <1.0 (parasitic reactions waste charge)

  6. SOH (State of Health) estimation
     SOH = (current capacity / rated capacity) * 100%
     Methods: incremental capacity analysis (dQ/dV peaks), Electrochemical Impedance
       Spectroscopy (EIS, requires brief perturbation), cycle counting models
     Battery end-of-life typically defined at SOH = 80%

  7. Fault protection
     Latching relay (contactor): disconnect pack on fault
     Faults: overvoltage, undervoltage, overcurrent, overtemperature, short circuit
     Two-contactor design: main + pre-charge (for capacitive loads)
```

---

## Degradation Mechanisms

```
LI-ION DEGRADATION TAXONOMY
==============================

                    CAPACITY FADE
                         |
          +--------------+----------------+
          |              |                |
   LITHIUM LOSS    ACTIVE MATERIAL    IMPEDANCE
   (most common)     LOSS             RISE
          |              |                |
   - SEI growth      - Particle crack  - SEI thickening
   - Li plating      - Mn dissolution  - Contact loss
   - Electrolyte     - Phase transf.   - Lithium plating
     reduction       - Co dissolution  - Electrode porosity

MECHANISM 1: SEI GROWTH (calendar + cycle aging)
  SEI grows continuously: thicker = more Li consumed = capacity loss
  Rate: proportional to sqrt(time) (diffusion-limited after initial layer)
  Accelerated by: high SOC (above 80%), high temperature, high voltage
  Mitigation: store at 50-60% SOC, cooler temperature, avoid >80% charge daily

MECHANISM 2: LITHIUM PLATING
  During fast charging: Li+ arrives at anode faster than it can intercalate
  -> Li deposits as metallic lithium on anode surface
  Conditions: high charge rate (>1C), low temperature (<15 C), high SOC (>80%)
  Consequences:
    a. Irreversible Li loss (plated Li becomes electrochemically inactive)
    b. Dendrite formation: metallic Li grows as needles -> can puncture separator
       Separator penetration -> internal short -> thermal runaway
  Detection: voltage plateau during discharge (at ~0 V) from Li stripping
  Mitigation: thermal preconditioning, rate limiting, charging curves (CC-CV)

MECHANISM 3: PARTICLE CRACKING (cathode, silicon anode)
  Repeated volume changes fatigue active material particles
  Cracked particles: expose fresh surface -> more electrolyte decomposition
  Also: isolated particle fragments lose electrical contact -> capacity loss
  NMC particles: cracking at grain boundaries (polycrystalline -> single crystal NMC)
  Silicon: catastrophic cracking unless nanostructured (see 09-APPLICATIONS.md)

MECHANISM 4: MANGANESE DISSOLUTION (LMO, some NMC)
  Mn3+ disproportionates: 2Mn3+ -> Mn4+ + Mn2+ (at elevated temperature)
  Mn2+ dissolves into electrolyte, migrates to anode, poisons graphite SEI
  Accelerated by: trace HF (from LiPF6 hydrolysis), elevated temperature
  Mitigation: HF scavenging additives, LiNO3, single-crystal cathode grains

DEGRADATION MODEL: Calendar + Cycle
  Total capacity fade = calendar aging + cycle aging
  Calendar: f(T, SOC) - Arrhenius temperature dependence (every 10 C: ~2x faster)
  Cycle: f(DOD, C-rate, T) - more aggressive cycles -> more degradation

  Typical end-of-life criteria: 80% capacity OR 80% power (whichever comes first)
  EV battery warranty: 8 years / 100,000 miles to 70% capacity (many OEMs)
```

---

## Decision Cheat Sheet

| Use Case | Cathode Chemistry | Why |
|----------|------------------|-----|
| Grid stationary storage | LFP | Long cycle life, thermal safety, low cost |
| EV maximum range | NMC 811 or NCA | Highest energy density |
| EV balanced (cost/range) | NMC 532/622 or LFP | Trade-off |
| Extreme temperature range | LFP | More tolerant vs. NMC |
| Fast charging application | LFP or LTO anode | LTO: no SEI, charge to 10C |
| Long calendar life (>15 yr) | LFP | Better calendar stability |
| Highest power density | LTO anode + NMC | LTO 5+ C charge/discharge |
| Lowest cost per kWh | LFP | No Co, simpler thermal management |

---

## Common Confusion Points

**"More Ni in NMC always means better battery."** Higher Ni (NMC811) means higher capacity,
but also more challenging synthesis (Li/Ni disorder), less thermal stability (onset ~180 C
vs. ~250 C for NMC111), and more reactive cathode surface (requires surface coatings,
electrolyte additives). NMC811 is not universally better -- it depends on application.

**"A BMS can prevent all battery failures."** The BMS can detect and respond to many faults,
but it cannot prevent thermal runaway once initiated. Once a cell vents and ignites,
the only defense is cell-level containment design. BMS prevents the conditions that lead
to runaway; it cannot extinguish it.

**"Fast charging always degrades the battery."** It depends on temperature and SOC. Fast
charging at high temperature (30+ C) and from 20-80% SOC is relatively benign. Fast
charging in cold (<15 C) or at high SOC (>80%) causes lithium plating -- the dangerous
degradation mode. Modern EVs pre-heat battery before fast charging (Ioniq 5, Tesla).

**"Passive cell balancing wastes energy."** True, but the energy dissipated is small
relative to total pack energy for a reasonably well-matched cell population. With cells
matched to <5 mAh variation, balancing current is minimal. Active balancing adds
significant cost/complexity -- justified only for packs with large SOC variations or
very high energy value per kWh.
