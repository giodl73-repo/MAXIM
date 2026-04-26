# Nanoelectronics: Transistor Limits, Single-Electron Devices, and Quantum Substrates

## The Big Picture

Nanoelectronics tracks the consequence of scaling transistors to single-digit nanometers.
Classical MOSFET operation breaks down. New device concepts emerge -- some implemented
commercially (FinFET, GAA), some in research (SET, molecular switches), some enabling
future computing platforms (spin qubits, superconducting qubits).

```
NANOELECTRONICS LANDSCAPE
==========================

PRODUCTION (NOW)               EMERGING                  RESEARCH
====================           ========                  ========
FinFET (5-7 nm node)           Gate-all-around (GAA)     Single-electron transistor
SOI MOSFET                     Monolithic 3D IC           Molecular electronics
High-k/metal gate              2D material FET (MoS2)     Spin qubit
EUV lithography                CNT transistors (IBM)      Topological qubit
Cu/low-k interconnects         Ferroelectric FET (FeRAM)  Neuromorphic devices
3D NAND flash                  MRAM (magnetic)            Quantum neural network
DRAM                           Racetrack memory
Phase-change memory (PCM)
ReRAM / Memristor
```

---

## MOSFET Scaling: From Dennard to the End of Classical Scaling

### Dennard Scaling (1974-2005)

```
DENNARD SCALING RULES
======================

Robert Dennard's 1974 observation: if you scale all dimensions by 1/k,
and scale voltage by 1/k:

  Dimension (L, W, tox, xj)  scaled by  1/k
  Voltage (Vdd, Vth)         scaled by  1/k
  Doping concentration        scaled by  k

Result:
  Transistor density:         k^2 increase (more transistors per chip)
  Clock frequency:            k increase (faster)
  Power per transistor:       1/k^2 decrease
  Power density (W/cm^2):     CONSTANT (density up k^2, power per tx down k^2)

THIS WAS THE GIFT: you got faster AND cooler with each generation

Held from ~1970 to ~2005 (k ~ 1.4 every 18-24 months, Moore's Law cadence)
```

### Dennard Scaling Breakdown (~2005)

```
WHY DENNARD SCALING ENDED
==========================

PROBLEM 1: Threshold voltage scaling hit a floor
  Vth cannot scale below ~0.3V: subthreshold leakage becomes too large
  Leakage current: I_leak ~ exp(-Vth / n*Vth_thermal)
    where Vth_thermal = kT/q = 26 mV at 300K
  If Vth = 0.2V: leakage = exp(-0.2/0.026) ~ 10^-3 of on-current
  Acceptable leakage is ~10^-4 to 10^-6 of on-current
  Can't go lower on Vth without exponentially growing standby power

PROBLEM 2: Oxide tunneling at tox < 2 nm
  Gate oxide (SiO2) tunneling current: J ~ exp(-2*sqrt(2m*phi_b)*tox/hbar)
  At tox = 1.2 nm: direct tunneling leakage ~ 10 A/cm^2 (enormous)
  Solution: high-k dielectrics (HfO2, k~22 vs. SiO2 k~3.9)
    Same electrical thickness (EOT) at 3x physical thickness
    Intel 45nm node (2007): first high-k/metal gate
    Reduced gate leakage by 10x while maintaining gate control

RESULT POST-2005:
  Voltage stuck at ~1V (Vdd), not scaling further
  Power density increasing: ~100 W/cm^2 in CPU hot spots
  Frequency scaling stopped: ~3-4 GHz ceiling since ~2004
  Performance now comes from more cores, not higher frequency
  Dark silicon: at advanced nodes, only fraction of chip can run simultaneously

NUMBERS:
  2000: Pentium 4 @ 1.5 GHz, 1.7V, 42 W, 180 nm
  2004: Pentium 4 at 3.8 GHz, 1.4V, 115 W, 90 nm (power crisis)
  2010: Core i7 @ 3.33 GHz, 1.0V, 130 W, 32 nm (multicore era)
  2024: Apple M4 @ 4.4 GHz, ~0.9V, ~30W SoC, 3 nm (efficiency wins)
```

---

## FinFET and Gate-All-Around

### FinFET (3D Transistor)

```
FINFET STRUCTURE
=================

PLANAR MOSFET (pre-2011):
  Gate electrode above channel
  Gate controls channel from one side only
  At short channel: drain electric field penetrates to source (DIBL -- drain-induced
    barrier lowering) -> leakage, threshold shift

FINFET:
  Channel raised as a vertical fin
  Gate wraps around three sides (top + two sidewalls)
  Better electrostatic control: gate sees channel from 3 sides

  Side view:              Top view (looking down):
  +----------+            +---------+---------+---------+
  |   Gate   |            |  Source |  Gate   |  Drain  |
  +----+--+--+            +---------+---------+---------+
       | fin |                      | Fin |
       |     |                      +-----+
  [Source] [Drain]

Advantages:
  Higher Ion/Ioff ratio (better off-state control)
  Lower leakage current at same Vth
  Enables continued scaling where planar fails
  Width quantized by fin pitch (you add fins, not continuous width)

Intel Ivy Bridge (2012): first production FinFET, 22nm node
  All advanced nodes since then (Apple, TSMC, Samsung, Intel): FinFET

Limitations at sub-5nm:
  Fin width becomes too small for desired conductance
  Variability: few-nm variation in fin dimensions -> threshold variation
```

### Gate-All-Around (GAA) Transistors

```
GATE-ALL-AROUND (NANOSHEET) TRANSISTOR
========================================

NANOSHEET (or nanowire):
  Horizontal sheets of Si stacked
  Gate wraps entirely around each sheet (360 degrees)
  Better control than FinFET (4 sides vs. 3 sides)

  Cross-section through gate:
  +-----------------------------+
  |         Gate metal          |
  | +--+  +----------+  +--+    |
  | |  |  | Nanosheet |  |  |  | <- gate dielectric wraps nanosheet
  | +--+  +----------+  +--+   |
  |        (another)           |
  |         Gate metal         |
  +-----------------------------+

STACKED NANOSHEETS:
  Multiple (2-5) nanosheets stacked vertically
  All driven by same gate
  Equivalent width without horizontal area

TSMC 3nm N3 (2022): still FinFET
SAMSUNG 3nm SF3E (2022): first production GAA (nanosheet), 3nm node
TSMC N2 (2025): GAA transition
Intel 20A/18A: RibbonFET (Intel's name for GAA nanosheet)

CFET (Complementary FET):
  Stack n-type nanosheet DIRECTLY on top of p-type nanosheet
  Same gate contact drives both
  50% footprint reduction for CMOS inverter vs. side-by-side
  Research: Samsung, Imec demonstrating; production 2028+
```

---

## Single-Electron Transistor (SET)

```
SINGLE-ELECTRON TRANSISTOR
============================

PRINCIPLE: Coulomb blockade

A tiny metallic or semiconductor "island" connected to source and drain
via tunnel junctions (thin insulators). Gate capacitively coupled.

   Source ---[tunnel]--- ISLAND ---[tunnel]--- Drain
                             |
                           Gate (capacitive only, no tunnel)

Energy to ADD one electron to island:
  E_C = e^2 / (2 * C_total)
  where C_total = sum of all capacitances to island

For very small islands (C_total ~ 10^-18 F = 1 aF):
  E_C = (1.6e-19)^2 / (2 * 10^-18) ~ 13 meV

COULOMB BLOCKADE CONDITION:
  If E_C >> kT: electrons cannot tunnel onto island at random
  kT at 300K = 26 meV
  kT at 4K   = 0.34 meV
  kT at 100 mK = 0.0086 meV

  For room temperature SET: need E_C >> 26 meV -> C < ~3 aF -> island < ~3 nm

OPERATION:
  With gate voltage: tune electrostatic potential of island
  At Vg such that N and N+1 electrons are degenerate in energy:
    Coulomb blockade lifted; current flows (one electron at a time)
  Periodic Coulomb blockade oscillations as Vg increases:
    Period = e/C_gate

CURRENT STATUS:
  Room-temperature SET: demonstrated in research (Si nanoparticle, NiO junctions)
  Practical room-T SET: requires island <5 nm -- hard to fabricate reproducibly
  Cryo-T SET (4K, 20 mK): standard tool in quantum transport research
  Used as: extremely sensitive electrometer (attocoulomb sensitivity)
           qubit readout in spin qubit circuits
           fundamental physics (shot noise, Cooper pair tunneling)
  NOT in production logic (thermal noise and fabrication variability problems)
```

---

## Molecular Electronics

### The Aviram-Ratner Proposal (1974)

```
MOLECULAR RECTIFIER (AVIRAM-RATNER, 1974)
==========================================

Proposed: single molecule could function as a diode (rectifier)
Architecture: D-sigma-A (donor-bridge-acceptor)

  Donor: TTF (tetrathiafulvalene) -- electron rich
  Bridge: sigma (insulating aliphatic bridge)
  Acceptor: TCNQ (tetracyanoquinodimethane) -- electron poor

  Electrode --- TTF --- bridge --- TCNQ --- electrode

Forward bias: electrons flow easily from TCNQ to TTF (acceptor to donor, downhill)
Reverse bias: electrons cannot flow easily (uphill)
-> Asymmetric I-V curve -> rectification

Experimental verification: demonstrated in 1997 by Metzger
But: single-molecule measurement is hard; reproducibility is the central challenge
```

### Tour Switches and Molecular Machines

```
MOLECULAR SWITCHES:
  Azobenzene: trans/cis photoisomerization under UV/vis light
    Changes molecular length ~0.4 nm: can close/open gap contacts
  Diarylethene: photochromic switch, robust, >10^4 switching cycles
  Stilbene, spiropyran: other photoswitches

STATUS OF MOLECULAR ELECTRONICS:
  Single-molecule transistor: YES, demonstrated in many labs (break junction technique)
  Molecular memory: YES, demonstrated
  Reproducible, scalable production: NO

CORE PROBLEM: Reproducibility
  Metal-molecule interface: resistance varies 10^2 to 10^3 between measurements
  Reason: exact geometry of metal-molecule contact is uncontrolled
          single atom positional difference changes conductance 10-100x
  Solution: needs atomic-scale control of contact geometry -- not achieved

BREAK JUNCTION TECHNIQUE (how single molecule is measured):
  Mechanically controllable break junction (MCBJ) or STM break junction
  Au nanowire broken by piezo movement
  Molecule from solution self-assembles into gap
  Current measured vs. gap distance
  Statistics: measure hundreds of breaking events, histogram conductance values
```

---

## Memristors

```
MEMRISTOR: RESISTANCE-SWITCHING MEMORY
========================================

HP Labs (2008): Stanley Williams, Dmitri Strukov
TiO2-based device: resistance switches between high (Roff) and low (Ron) state
Non-volatile: state retained without power

MECHANISM (TiO2):
  TiO2 with oxygen vacancy profile:
  TiO2-x (conducting, vacancy-rich) | TiO2 (insulating)
  Applied field: moves oxygen vacancies
    +V: vacancies move toward interface -> conducting region grows -> Ron
    -V: vacancies move away -> insulating region grows -> Roff

  State equation: dw/dt = mu_v * Ron * I / D
    (drift equation for vacancy front position w)

PROPERTIES:
  On/off ratio: 10 to 10^3 (chemistry-dependent)
  Switching time: ns to us
  Endurance: 10^5 to 10^12 cycles (material-dependent)
  Non-volatile retention: >10 years at room temp

APPLICATIONS:
  Crossbar memory array (ReRAM: Resistive RAM):
    4F^2 cell (minimum possible 2D area)
    Multi-level cell (MLC): store 2-4 bits per device via analog resistance levels
    Products: Intel Optane (PCM, not exactly memristor but similar), SK Hynix, Weebit Nano

  Neuromorphic computing:
    Memristor as artificial synapse: weight = resistance value
    Spike timing: write pulses modify resistance (Hebbian learning)
    In-memory computing: matrix-vector multiply in O(1) time (physics computes it)
    Intel Loihi, IBM TrueNorth: use CMOS but target memristor for next generation

CURRENT LIMITATION:
  Variability: resistance states variable across cells
  Sneak current paths in crossbar (half-select problem)
  Multi-level reliability: difficult to maintain 4+ distinct states over lifetime
```

---

## Quantum Computing Substrates

### Superconducting Qubits

```
SUPERCONDUCTING QUBIT (TRANSMON)
==================================

Operating temperature: 10-20 mK (dilution refrigerator)

Hardware:
  Josephson junction: two superconductors separated by ~1-2 nm tunnel barrier (Al/AlOx/Al)
  Creates anharmonic quantum oscillator (LC circuit with quantum nonlinearity)
  Qubit states: |0> and |1> are specific energy levels
  Frequency: 4-8 GHz (microwave range)

TRANSMON QUBIT (Koch 2007):
  Large capacitance shunting Josephson junction
  Reduces sensitivity to charge noise (the dominant noise source in charge qubits)
  E_J / E_C >> 1 (Josephson energy >> charging energy)
  Trade-off: less anharmonicity (harder to address individually in multi-qubit system)

Gate operations: microwave pulses at qubit frequency
Readout: dispersive measurement via coupled microwave resonator

Coherence times (2025):
  T1 (energy relaxation): 0.1 - 1 ms (best devices)
  T2 (dephasing): 0.1 - 1 ms (echo, best devices)
  Gate fidelity: 99.5-99.9% for single-qubit gates
  Two-qubit gate fidelity: 99-99.7%
  Error correction threshold: ~99% (surface code)

Companies: IBM (1121-qubit Condor), Google (72-qubit Sycamore, 1000+ in development),
           Rigetti, IQM, Alice&Bob

Nanoscale requirement: Josephson junction (Al/AlOx/Al) 100-200 nm x 100-200 nm
Fabrication: electron beam lithography + shadow evaporation
```

### Silicon Spin Qubits

```
SILICON SPIN QUBIT
===================

Physical qubit: spin of a single electron (or nuclear spin) in a Si quantum dot

Structure:
  Si/SiGe heterostructure or Si-MOS
  Metallic gates at nm scale pattern quantum dots
  Single electron loaded by tuning gate voltages
  Qubit: spin up = |0>, spin down = |1>

ADVANTAGES OF SPIN QUBITS:
  Long coherence: Si is free of nuclear spins (^28Si isotope, 95.3% natural, 0 nuclear spin)
  Use ^28Si enriched to 99.9995%: T2* > 30 ms demonstrated (T2 > 1 s with CPMG)
  Small: quantum dot 20-50 nm; can leverage semiconductor fab technology
  High temperature operation: single spin qubits demonstrated at 1-4 K
    (vs. 10-20 mK for superconducting) -- lower cooling cost eventually

CHALLENGES:
  Multi-qubit connectivity: engineering exchange interactions between distant dots
  Readout speed: spin readout requires tunneling to reservoir (slow, ~1 us)
  Variability: atomic-scale disorder in Si/SiGe interface affects qubit parameters
  Scale-up: connecting thousands of qubits with classical control electronics

Companies: Intel (12-spin-qubit chip), QuTech (Delft), Silicon Quantum Computing (Australia)
Fabrication: requires sub-20 nm patterning of gates (standard semiconductor fab tooling)
```

---

## Decision Cheat Sheet

| Scenario | Device / Approach |
|----------|------------------|
| Production digital logic, 3nm | GAA nanosheet (Samsung SF3E, TSMC N2) |
| Production digital logic, 5-7nm | FinFET (established) |
| Sensitive charge detector (research) | Single-electron transistor (cryogenic) |
| Non-volatile fast memory, high density | Memristor/ReRAM crossbar |
| Neuromorphic analog weight | Memristor synapse |
| Quantum computing (most deployed) | Superconducting transmon qubit |
| Quantum computing (long coherence) | Silicon spin qubit (28Si enriched) |
| RF electronics, >100 GHz | GaN HEMT or InP HEMT (compound semiconductor) |
| Nanoscale molecular switch (research) | STM break junction, Tour-type molecule |

---

## Common Confusion Points

**"Moore's Law is over."** Transistor count per die continues to increase (Apple M3 Ultra:
134 billion transistors). What ended is Dennard scaling (clock speed + voltage scaling).
Performance per watt still improves but from architecture (parallelism, cache), not
just transistor speed.

**"FinFET ended at 5nm."** No. Intel, TSMC, and Samsung used FinFET well into 5nm and
7nm nodes. Samsung made the leap to GAA at 3nm (2022). TSMC transitioned at N2 (2025).
The transition is driven by short-channel effects, not an arbitrary rule.

**"Memristors will replace DRAM."** The HP/memristor announcement in 2008 created massive
hype. Current status: PCM-based Optane (now discontinued), ReRAM in embedded applications.
DRAM remains dominant for main memory due to superior endurance (>10^15 cycles vs. 10^8-10^12
for ReRAM) and manufacturing maturity.

**"Quantum computers will run normal software."** Not how they work. Quantum computers
are hardware accelerators for specific problem classes (unstructured search, factoring,
quantum simulation). Classical instruction streams run on classical processors.
