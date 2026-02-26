# Electrochemical Fundamentals: Nernst Equation, Electrode Kinetics, SEI Layer

## The Big Picture

Electrochemical energy storage converts between chemical energy and electrical energy
via controlled redox reactions at solid-liquid interfaces. Understanding the
thermodynamics (Nernst), kinetics (Butler-Volmer), and interfacial chemistry (SEI)
is essential for understanding battery behavior, performance, and failure.

```
ELECTROCHEMICAL CELL OVERVIEW
================================

                  EXTERNAL CIRCUIT (electron flow)
        e- <------+---------------------------+------> e-
                  |                           |
           NEGATIVE                       POSITIVE
           ELECTRODE                      ELECTRODE
           (Anode on                      (Cathode on
            discharge)                    discharge)
                  |                           |
           Oxidation:                    Reduction:
           M -> M^n+ + ne-               M^n+ + ne- -> M
                  |                           |
                  +-----ELECTROLYTE-----------+
                    (ion transport: M^n+ flow)

TERMINOLOGY:
  Anode: electrode where oxidation occurs (releases e-)
    In battery DISCHARGE: negative electrode (e.g., graphite)
    In battery CHARGE: negative electrode IS STILL anode (confusion common)
  Cathode: electrode where reduction occurs (accepts e-)
    In battery DISCHARGE: positive electrode (e.g., LiCoO2)

  Cell voltage: V_cell = phi_cathode - phi_anode
    (always positive for spontaneous discharge)
```

---

## Thermodynamics: Nernst Equation

### Electrode Potentials

The standard electrode potential E° is defined relative to the Standard Hydrogen
Electrode (SHE: H2/H+ at unit activity, assigned E° = 0 V by convention).

```
STANDARD ELECTRODE POTENTIALS TABLE
=====================================

Half-reaction                         E° (V vs. SHE)
--------------------------------------  ---------------
Li+ + e- -> Li                         -3.04  (most negative = strongest reductant)
Na+ + e- -> Na                         -2.71
Mg2+ + 2e- -> Mg                       -2.37
Al3+ + 3e- -> Al                       -1.66
Zn2+ + 2e- -> Zn                       -0.76
Fe2+ + 2e- -> Fe                       -0.44
Ni2+ + 2e- -> Ni                       -0.25
2H+ + 2e- -> H2                         0.00  (reference)
Cu2+ + 2e- -> Cu                       +0.34
O2 + 2H2O + 4e- -> 4OH-               +0.40
I2 + 2e- -> 2I-                        +0.54
Fe3+ + e- -> Fe2+                      +0.77
Ag+ + e- -> Ag                         +0.80
O2 + 4H+ + 4e- -> 2H2O               +1.23  (oxygen evolution/reduction)
F2 + 2e- -> 2F-                        +2.87  (most positive = strongest oxidant)

BATTERY CELL VOLTAGE = E°(cathode) - E°(anode)

Li-ion (LiCoO2 cathode, graphite anode):
  E°_cathode (LiCoO2): ~+0.6 V vs. SHE
  E°_anode (LiC6): ~-3.0 V vs. SHE
  E°_cell ~ 3.6 V (this is why Li-ion has high voltage -- Li anode very negative)

Lead-acid (PbO2 cathode, Pb anode):
  E°_cathode (PbO2): +1.69 V
  E°_anode (Pb): -0.36 V
  E°_cell = 2.05 V per cell; 12V battery = 6 cells
```

### Nernst Equation: Real vs. Standard

```
NERNST EQUATION
================

At non-standard conditions (activity a_i not equal to 1):

  E = E° - (RT / nF) * ln(Q)

where:
  E  = cell potential at actual conditions
  E° = standard cell potential
  R  = 8.314 J/mol/K
  T  = temperature (K)
  n  = number of electrons transferred per formula unit
  F  = Faraday constant = 96,485 C/mol
  Q  = reaction quotient = product of activity terms

At 298 K (25 C):
  RT/F = (8.314 * 298) / 96485 = 0.02569 V (thermal voltage)
  (2.303 * RT/F) = 0.0592 V (for log base 10)
  Nernst simplification: E = E° - (0.0592/n) * log(Q)

EXAMPLE: Li+ insertion into graphite
  Li+ + e- + 6C (graphite) -> LiC6
  Q = a(LiC6) / [a(Li+) * a(C)^6]
  As battery discharges: Li+ concentration in cathode decreases -> Q increases
  -> E drops (discharge curve slopes downward)

  Temperature dependence:
    Higher T: RT/nF larger -> more Nernst variation
    Lower T: smaller Nernst term -> flatter curve but slower kinetics
    Li-ion at -20 C: capacity drops 30-50% (kinetics dominate)
```

---

## Kinetics: Butler-Volmer Equation

The Nernst equation gives equilibrium (no current). When current flows, the
potential deviates from equilibrium by the overpotential eta = E - E_eq.

```
BUTLER-VOLMER EQUATION
========================

  i = i_0 * [exp(alpha_a * F * eta / RT) - exp(-alpha_c * F * eta / RT)]

where:
  i      = current density (A/cm^2)
  i_0    = exchange current density (A/cm^2)  -- kinetic parameter
  alpha_a = anodic transfer coefficient (typically 0.3-0.7, often ~0.5)
  alpha_c = cathodic transfer coefficient = 1 - alpha_a
  F       = Faraday constant
  eta     = overpotential = E - E_eq
  RT/F    = thermal voltage (26 mV at 25 C)

EXCHANGE CURRENT DENSITY i_0:
  Rate of forward and reverse electron transfer at equilibrium
  Large i_0: fast kinetics (reaction proceeds easily at small overpotential)
  Small i_0: slow kinetics (need large overpotential to drive reaction)
  Units: A/cm^2 of electrode area
  Pt in H2SO4: i_0 ~ 10^-3 A/cm^2 (fast -- good HER catalyst)
  Li+ intercalation in graphite: i_0 ~ 10^-6 A/cm^2 at room temp (slower)
  Li+ at low T (-20 C): i_0 << 10^-6 (very slow -- why Li-ion fails in cold)

TAFEL APPROXIMATION (large overpotential limit, |eta| >> RT/F = 26 mV):
  eta >> 26 mV:   i ~ i_0 * exp(alpha_a * F * eta / RT)
  eta << -26 mV:  i ~ -i_0 * exp(-alpha_c * F * eta / RT)

  Taking log: eta = (RT / alpha_a * F) * ln(i/i_0)  =  Tafel equation
  Plot eta vs. log(i): straight line (Tafel slope = 2.303*RT / alpha*F)
  At alpha=0.5, 25C: Tafel slope = 0.118 V/decade = 118 mV/decade

  Larger |eta| needed for same current -> slower electrode reaction
```

---

## Overpotential Components: Why Batteries Lose Voltage

```
OVERPOTENTIAL DECOMPOSITION
=============================

Measured cell voltage during discharge:
  V_cell = V_OCV - eta_ohmic - eta_activation - eta_concentration

V_OCV: Open circuit voltage (Nernst potential, no current)
       = equilibrium potential, determined by thermodynamics

eta_ohmic = i * R_internal
  R_internal = electrolyte resistance + current collector + contacts
  Ohm's law -- instantaneous (no delay)
  Manifests as: IR drop when current applied (immediate voltage step)
  Reduced by: higher electrolyte conductivity, thinner electrodes, better contacts

eta_activation (Butler-Volmer):
  Energy to overcome activation barrier for electron transfer
  Reduced by: higher temperature, better catalytic electrode surface, i_0 > larger
  Manifests as: curved V-I relationship, Tafel slope

eta_concentration (diffusion limitation):
  Reactant depletion near electrode surface
  Li+ ions cannot diffuse to interface fast enough at high current
  Manifests as: voltage cliff at high current rates (rate capability limit)
  Reduced by: thinner electrodes, porous structure, higher T (faster diffusion)

TYPICAL INTERNAL RESISTANCE FOR Li-ion cell (18650, room temp):
  R_ohmic: ~50-100 mOhm (electrolyte + separator + contacts)
  R_charge_transfer: ~50-200 mOhm (anode + cathode activation)
  R_diffusion: rate-dependent, rises with SOC and rate
  Total: ~100-400 mOhm (new cell); rises with aging

At 2A discharge in 18650 (capacity ~3 Ah = 3.5V nominal):
  Power to internal resistance: I^2 * R = 4 * 0.15 = 0.6 W
  Cell heat generation: 0.6 W
  At 40% SOC: rate contribution to total heat is significant
  Thermal management critical above 1C rate
```

---

## SEI: Solid Electrolyte Interphase

The SEI is the most important and least understood element of lithium-ion batteries.
It governs cycle life, safety, and degradation.

```
SEI FORMATION AND COMPOSITION
================================

WHERE: Forms on negative electrode (anode -- graphite or silicon)
WHEN: First charge cycle (and ongoing)

WHY IT FORMS:
  Graphite anode operates at ~0-0.2 V vs. Li/Li+
  Electrolyte window: liquid electrolyte (EC/DMC with LiPF6) is stable only
    above ~1 V vs. Li/Li+ (on the reductive side)
  Below 1 V: electrolyte components reduced by electrode electrons:
    EC (ethylene carbonate) + 2e- + 2Li+ -> Li2CO3 + CH2=CH2 (gas)
    EC (another pathway) -> LEDC (lithium ethylene dicarbonate)
    DMC -> CH3OLi + ...
  These decomposition products are insoluble -> deposit on electrode surface
  -> BUILD SEI LAYER

SEI COMPOSITION:
  Inorganic inner layer (close to electrode):
    Li2CO3, LiF, Li2O (dense, ionically conductive)
  Organic outer layer:
    LEDC, ROCO2Li species (porous, less dense)
  Total thickness: 10-100 nm (grows slowly over thousands of cycles)

SEI PROPERTIES:
  Electrically insulating: prevents further electrolyte reduction (self-passivating)
  Li+ ionically conductive: allows Li+ to pass through (critical)
  Mechanically: must withstand volume changes of electrode (~10% for graphite, 300% for Si)

SEI FIRST CYCLE CONSEQUENCES:
  Li consumed irreversibly (forms SEI, not returned on discharge)
  First cycle Coulombic efficiency (CE): 85-95% for graphite
    CE = discharge capacity / charge capacity
    If CE = 0.90 on first cycle: 10% of Li is permanently lost to SEI
  Manufacturers pre-lithiate or account for SEI loss in cell design
  Silicon anode CE: 70-85% on first cycle (more SEI due to more surface area)

SEI FAILURE MODES:
  1. Mechanical cracking (Si expansion 300%): exposes fresh Si -> new SEI forms
     -> each cycle consumes more Li -> capacity fade
  2. Li+ plating: at high rate or low T, Li deposits as metal on SEI surface
     -> dendrites risk (safety: Li metal can puncture separator -> short circuit)
  3. Dissolution: HF from LiPF6 hydrolysis attacks Li2CO3 in SEI
     -> SEI thinning -> more electrolyte decomposition -> continued fade
  4. Impedance rise: SEI thickens over lifetime -> higher resistance -> power fade
```

---

## Electrolyte Requirements

```
BATTERY ELECTROLYTE REQUIREMENTS
===================================

1. IONIC CONDUCTIVITY (sigma_i):
   Must transport Li+ ions between electrodes
   Target: >1 mS/cm (10^-3 S/cm)
   LiPF6 in EC/DMC (1 M): sigma ~ 10-11 mS/cm (excellent)
   Solid electrolyte (ceramic): 1-10 mS/cm (depends on type)
   Polymer PEO at 25 C: 0.01-0.1 mS/cm (too low for fast charging)
   PEO at 80 C: 1+ mS/cm (used in Bolloré Bluecar)

2. ELECTROCHEMICAL STABILITY WINDOW:
   Must be stable (not oxidized or reduced) at electrode potentials
   Graphite anode: ~0.1 V vs. Li/Li+
   NMC cathode: ~4.0-4.3 V vs. Li/Li+
   Required window: 0 to 4.3 V vs. Li/Li+ (or wider for high-voltage cathodes)
   LiPF6/EC/DMC: stable 1-4.5 V vs. Li/Li+
     Below 1 V: forms SEI (useful but consumes Li)
     Above 4.5 V: electrolyte oxidizes at cathode
   High-voltage electrolytes (LiNi0.5Mn1.5O4 at 4.7 V): requires additives

3. LITHIUM TRANSFERENCE NUMBER (t+):
   Fraction of ionic current carried by Li+ (vs. anion PF6-)
   LiPF6 in EC/DMC: t+ ~ 0.3-0.4 (Li+ carries only ~35% of current)
   Remaining current from PF6- movement (anion does not react at electrode)
   -> Concentration gradients build -> concentration overpotential
   Single-ion conductors (polymers with bound anion): t+ -> 1.0 (ideal)
   Better: solid electrolyte with t+ ~ 1 (all charge carried by Li+)

4. THERMAL STABILITY:
   Must not decompose or ignite at operating temperature
   LiPF6: decomposes above 60 C: LiPF6 -> LiF + PF5 (Lewis acid, reacts with moisture)
   EC/DMC: flash point ~25 C (flammable) -- the source of battery fire risk
   Solid electrolyte: nonflammable -- key safety advantage

ELECTROLYTE TYPES:
  Liquid organic: LiPF6 in EC/EMC/DMC -- current commercial standard
  Liquid ionic: ionic liquids (nonflammable, low vapor pressure, poor conductivity at RT)
  Gel polymer: PEO + Li salt + plasticizer -- lithium-metal batteries
  Solid oxide: LLZO, LATP -- see 03-ADVANCED-BATTERIES.md
  Solid sulfide: LGPS, Li6PS5Cl -- see 03-ADVANCED-BATTERIES.md
```

---

## Capacity, Energy, and Power

```
KEY ELECTROCHEMICAL QUANTITIES
================================

CAPACITY:
  Q = n * F * m / M_w
  where n = electrons per formula unit, m = mass (g), M_w = molar mass (g/mol)

  Specific capacity (mAh/g):
    Graphite (LiC6): n=1, M_w(C6)=72 -> Q = F/72 = 96485/(72*3600) = 372 mAh/g
    LiFePO4:         n=1, M_w=158    -> Q = 96485/(158*3600) = 170 mAh/g
    LiCoO2 (practical): n=0.5, M_w=98 -> Q = 137 mAh/g (only half Li can be used)
    Silicon (Li15Si4): n=3.75, M_w=28 -> Q = 3579 mAh/g (theoretical max)

ENERGY DENSITY:
  E = Q * V_avg
  Specific energy (Wh/kg): = (capacity mAh/g) * (V_avg) / 1000
  NMC811 cathode paired with graphite at cell level: ~300 Wh/kg
    Cell adds inactive mass: current collectors, separator, electrolyte, packaging

C-RATE:
  Normalized discharge current relative to capacity
  1C rate: fully discharge in 1 hour
    If capacity = 3 Ah, 1C = 3 A; 2C = 6 A; C/2 = 1.5 A
  Effect on capacity: higher C-rate -> more losses -> apparent capacity lower
    NMC cell: 0.1C capacity = 100%, 1C capacity = 95%, 3C capacity = 85% (typical)
    This is concentration overpotential limiting capacity at high rates

STATE OF CHARGE (SOC) ESTIMATION:
  Coulomb counting: integrate current over time
    SOC(t) = SOC(0) - integral(I dt) / Q_rated
    Problem: cumulative error from small measurement offset
  OCV method: measure open-circuit voltage -> look up in OCV-SOC curve
    Problem: equilibration time needed; hysteresis between charge/discharge
  Kalman filter: combines both, models cell dynamics
    Extended Kalman Filter (EKF): standard BMS approach
    SOC accuracy: +/- 1-3% with EKF
```

---

## Decision Cheat Sheet

| Electrochemical concept | What it determines |
|------------------------|-------------------|
| Standard electrode potential (E°) | Maximum theoretical cell voltage |
| Nernst equation | How voltage changes with SOC and temperature |
| Exchange current density (i_0) | Kinetic speed of electrode reaction |
| Tafel slope | How much overpotential per decade of current |
| Ohmic resistance | IR drop (immediate voltage loss under load) |
| SEI first-cycle loss | Irreversible capacity consumed on formation |
| Electrolyte stability window | Maximum cathode/anode voltage limits |
| Transference number | Concentration gradient buildup, limiting high rates |

---

## Common Confusion Points

**"Higher voltage always means better battery."** Only if the electrode active materials
can sustain it. High-voltage cathodes (>4.5V) require matching electrolytes that are
stable at that potential. LiPF6/EC/DMC oxidizes at 4.5V -- hence the need for specialized
high-voltage electrolytes for next-generation cathodes.

**"The SEI is a problem to be eliminated."** The SEI is essential. Without it, the
electrolyte would continuously decompose, consuming lithium and generating gas.
A stable, thin, conductive SEI is what makes graphite anodes work at all.
The goal is controlling SEI quality, not eliminating it.

**"Capacity fade means the electrode materials degraded."** Often it means lithium
was lost to the SEI, or to lithium plating, or to inactive phases -- not necessarily
structural degradation of active materials. Capacity can often be recovered
(in part) by slow trickle charge (reconstituting plated Li). The mechanism matters
for diagnosis and mitigation.

**"Butler-Volmer applies everywhere."** It applies to simple electron transfer reactions.
For battery electrodes involving multiple steps (solid-state diffusion, phase transitions,
nucleation), Butler-Volmer is an approximation of the charge transfer step only.
The full electrode model includes solid-state diffusion (Fickian) and phase change kinetics.
