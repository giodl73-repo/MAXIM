# Advanced Polymers: Engineering and High-Performance

## The Big Picture

```
+------------------------------------------------------------------+
|              HIGH-PERFORMANCE POLYMER LANDSCAPE                  |
|                                                                  |
|   USE TEMP     POLYMER          KEY PROPERTY          MARKET     |
|   ────────     ───────          ────────────          ──────     |
|   >300°C       Polyimide (PI)   Extreme T + chem      Aerospace  |
|   250°C        PTFE             Teflon — min friction  Seals,wire |
|   250°C        PPS (Ryton)      Xtal + chem resist    Automotive |
|   250°C+       PEEK             Best overall balance  Aerospace  |
|   200°C        PSU / PES        Transparent at T      Medical    |
|   200°C        PEI (Ultem)      Amorphous, moldable   Aircraft   |
|   200°C+       LCP              Near-zero CTE, low µ  Electronics|
|   150°C        POM (Delrin)     Best gear polymer     Precision  |
|   ────────────────────────────────────────────────────────────── |
|   ALL: >$10/kg, often $50–200+/kg, used in grams not kilograms  |
+------------------------------------------------------------------+
```

---

## PEEK (Polyether Ether Ketone)

The benchmark high-performance thermoplastic. Continuous service to 250°C;
short-term to 300°C. Can be melt-processed (Tm = 343°C).

### Chemistry

```
   REPEAT UNIT:
   ─O─C6H4─O─C6H4─CO─C6H4─
   ether    ether   ketone   (aromatic backbone → high Tg and Tm)

   Tg = 143°C
   Tm = 343°C  (requires 360–400°C melt processing)
   χ_c = 30–35% (semi-crystalline — amorphous quench also possible)
```

**Crystallization is mandatory for structural use**: Amorphous PEEK (quenched)
has Tg = 143°C. Crystallized PEEK can withstand continuous 250°C because the
crystallites (Tm = 343°C) act as reinforcing filler above Tg. Mold temperature
must be 160–190°C to ensure crystallization.

### PEEK Grades and Properties

| Grade | Notes | Tensile (MPa) | Mod (GPa) |
|-------|-------|---------------|-----------|
| Unfilled | Pure PEEK | 100 | 3.6 |
| 30% CF | Carbon fiber | 200 | 14 |
| 30% GF | Glass fiber | 160 | 9 |
| Bearing grade | PTFE + graphite | 95 | 3.5 |
| CF + tribological | Best wear | 185 | 16 |

### Chemical Resistance

PEEK resists almost all organic solvents, acids, and bases at room temperature.
Attacked by: concentrated H2SO4, halogenated solvents at elevated temperature.
Approved: steam sterilization (autoclave), gamma irradiation (medical devices).

### Applications

```
   AEROSPACE:
   ──────────
   Fan blade root inserts, cable insulation, aircraft brackets
   Replaces aluminum in non-structural parts (weight saving)
   Firewall clips, hydraulic end fittings

   MEDICAL:
   ────────
   Spinal cage implants (radiolucent — MRI transparent)
   Dental implant components
   Surgical instruments (autoclave-stable, chemical-resistant)
   Note: PEEK modulus ~ cortical bone — better than titanium (too stiff)

   OIL & GAS:
   ──────────
   Downhole seals (150–200°C, chemical, pressure)
   Bearing components in pumps
   Wear rings in submersible pumps

   SEMICONDUCTOR:
   ──────────────
   Wafer handling (clean room, chemical compatibility)
   Process equipment components
```

---

## PTFE (Polytetrafluoroethylene)

The most chemically inert engineering polymer. Fluorine atoms completely
shield the carbon backbone.

### Chemistry and Why It's Exceptional

```
   REPEAT UNIT:  –(CF2–CF2)n–

   F–C bond energy: 485 kJ/mol (vs. H–C: 415 kJ/mol)
   F completely shields C-C backbone
   C-C bond: 347 kJ/mol — protected by F atoms

   Consequences:
   • No adhesion to anything — lowest surface energy of any solid (18 mJ/m²)
   • No common solvent can dissolve it (δ ~ 12 MPa^0.5)
   • Attacked only by: alkali metals (Na, K), fluorine gas, strong Lewis acids
   • Excellent electrical insulator (εr = 2.1, lowest of solids)
   • Very high Tm = 327°C (fully crystalline version)
   • Tg = –97°C (extremely flexible chain)
```

<!-- @editor[content/P2]: No mention of PFAS regulatory context — PTFE and fluoropolymer processing byproducts are under intense regulatory scrutiny (EU PFAS restriction proposal, US EPA PFAS action); significant for anyone evaluating fluoropolymer specification -->

### The Processing Problem

PTFE has no melt viscosity — it doesn't flow. It undergoes a gel-phase
transition at ~327°C but viscosity is ~10^12 Pa·s (not processable by screw).

```
   PROCESSING METHODS:
   ────────────────────
   Ram extrusion: solid plug pushed through heated die (wire coating, rod)
   Paste extrusion: PTFE powder + lubricant → low-T paste → sinter
   Compression molding: powder → press → sinter at 370°C
   Skiving: machined film from sintered billet → tape, film

   PFAS ALTERNATIVE GRADES:
   ──────────────────────────
   PFA (perfluoroalkoxy): melt-processable, similar properties to PTFE
   FEP (fluorinated ethylene propylene): melt-processable, Tm = 260°C
   ETFE (ethylene-TFE): tougher, lower T, melt-processable — stadium roofs
```

### PTFE Properties Summary

| Property | PTFE | Notes |
|----------|------|-------|
| Service T | –200°C to +260°C | Widest of any polymer |
| Tensile | 20–35 MPa | Low for engineering polymer |
| E-modulus | 0.4–0.6 GPa | Very low — deforms easily |
| COF | 0.04–0.10 | Lowest static COF of any solid |
| Chemical resist | Excellent | Only attacks: Na, F2, strong Lewis acid |
| Dielectric const | 2.1 | Lowest solid |
| Density | 2.2 g/cm³ | Heavy for polymer |
| Creep | High | Cold-flow under load — design issue |

PTFE creep ("cold flow") limits its use as a structural load-bearing material.
Under sustained load, it flows. Bearing and seal designs must accommodate this.

---

## PPS (Polyphenylene Sulfide)

```
   REPEAT UNIT:  –C6H4–S–   (para-phenylene sulfide)
   Tg = 85°C  Tm = 280°C  χ_c = 50–60%
```

Semi-crystalline, so modulus retained well above Tg (crystallites as filler).
Excellent inherent flame resistance (LOI ~ 44%) — no FR additive needed.
Outstanding chemical resistance to most solvents, fuels, acids.

```
   TYPICAL GRADES:
   ────────────────
   40% GF + mineral: stiff, good weld strength
   40% CF: high stiffness and strength
   Glass + PTFE: bearing grade (self-lubricating)

   APPLICATIONS:
   ──────────────
   Automotive: pump housings, throttle bodies, coolant connectors
   Electronics: SMT-capable connectors (withstands 260°C solder reflow)
   Chemical processing: pump impellers, valve bodies
   Aircraft: brackets, housings (lightweight vs. aluminum)
```

---

## Polysulfone Family (PSU, PES, PPSU)

Amorphous high-performance thermoplastics. Transparent. Excellent hydrolysis
resistance. All can withstand steam sterilization (134°C).

```
   PSU  (polysulfone, Udel):       Tg = 185°C
   PES  (polyethersulfone, Radel): Tg = 220°C   amber-colored
   PPSU (polyphenylsulfone, Radel R): Tg = 220°C   best toughness

   APPLICATIONS:
   ──────────────
   Medical: surgical instruments, trays (autoclave)
   Water filtration membranes (PSU, PES)
   Printed circuit board assemblies (PES: T > wave solder)
   Baby bottles, reusable containers (before BPA fears moved to PPSU from PC)
   Dental instruments: PPSU cups
```

---

## PEI (Polyetherimide) — Ultem

```
   Structure: imide + ether linkages, amorphous, amber/translucent
   Tg = 217°C  (Ultem 1010)
   No Tm (amorphous — melt processable unlike true polyimides)
```

Unique position: high Tg approaching polyimide, but melt-processable. Can be
injection molded. FAR 25.853 flame certification → aircraft interiors.

Applications: aircraft interior components, medical devices (gamma sterilizable),
electrical connectors operating >180°C, microwave cookware.

---

## Liquid Crystal Polymers (LCP)

```
   LIQUID CRYSTAL POLYMER CONCEPT:
   ──────────────────────────────────
   Rigid rod-like molecules self-align in melt state
   Form ordered "nematic" liquid crystal phase above Tm
   On solidification: retain orientation → anisotropic solid

   In-flow direction (MD): E ~ 15–20 GPa, tensile ~ 200 MPa
   Cross-flow direction (TD): E ~ 6–10 GPa, tensile ~ 100 MPa

   Consequences:
   • Near-zero CTE in MD (critical for electronics: thermal matching to Cu)
   • Extremely low moisture absorption (<0.02%)
   • Excellent chemical resistance
   • Very easy flow in melt (low melt viscosity — thin-wall molding)
   • Weld lines: catastrophically weak — must design flow to avoid
```

Applications dominate electronics: multi-functional connector housings (100%
SMT), 5G antenna components (low dielectric loss), antenna-in-package.

Ticona Vectra, Celanese, Sumitomo Solvay are the main LCP producers.

---

## POM (Polyoxymethylene / Acetal / Delrin)

```
   REPEAT UNIT:  –(CH2–O)n–   (polyformaldehyde)
   Tg = –60°C  Tm = 165°C (homopolymer) / 155°C (copolymer)
   χ_c ~ 75–85%  (highest crystallinity of any thermoplastic)
```

POM is the best "gear polymer" — highest crystallinity → lowest creep, best
fatigue, best wear resistance of commodity engineering polymers.

```
   HOMOPOLYMER (Delrin, DuPont):
   ─────────────────────────────
   Higher crystallinity, higher strength and stiffness
   Less stable at elevated temperature (depolymerization)

   COPOLYMER (Celcon, Hostaform):
   ───────────────────────────────
   Slightly lower properties but better thermal stability
   Less susceptible to acid/alkali attack at ends
```

Applications: gears, bushings, bearings, door handles, fuel system components,
precision mechanical parts (watches, firearms components, zippers, pens).

**POM and formaldehyde**: Thermal or chemical degradation releases formaldehyde
— must be processed at correct temperature (180–220°C) and ventilated.

---

## High-Performance Polymer Property Comparison

| Polymer | Tg (°C) | Tm (°C) | Max T (°C) | Tensile (MPa) | E (GPa) | Chemical res. | Cost ($/kg) |
|---------|---------|---------|-----------|---------------|---------|---------------|-------------|
| PEEK | 143 | 343 | 250 | 100 | 3.6 | Excellent | 80–200 |
| PPS | 85 | 280 | 200 | 65 | 3.3 | Excellent | 20–60 |
| PEI (Ultem) | 217 | amorphous | 170 | 105 | 3.3 | Very good | 30–80 |
| PSU | 185 | amorphous | 150 | 70 | 2.7 | Very good | 15–30 |
| PPSU | 220 | amorphous | 180 | 70 | 2.4 | Excellent | 25–60 |
| LCP | 180–290 | 280–350 | 200–300 | 150–200 (aniso) | 10–20 (aniso) | Excellent | 20–60 |
| PTFE | –97 | 327 | 260 | 25 | 0.5 | Exceptional | 15–40 |
| POM | –60 | 165 | 100 | 65 | 2.8 | Good | 5–10 |
| PI (Kapton-type) | >300 | none | 300+ | 165 (film) | 2.5 | Excellent | 100–300 |

---

<!-- @editor[content/P2]: Section is thin — vitrimers and SMPs each deserve the same quantitative treatment (property tables, application examples, commercial status) given to PEEK/PTFE/PPS above -->

## Emerging: Self-Healing and Stimuli-Responsive Polymers

```
   SELF-HEALING CONCEPTS:
   ──────────────────────
   Intrinsic: reversible bonds in backbone (Diels-Alder adducts,
              hydrogen bonds, ionomers, vitrimers)
   Extrinsic: microencapsulated healing agent released on crack

   Vitrimers (Leibler, 2011):
   ─────────────────────────
   Thermoset-like network but with dynamic covalent bonds
   (transesterification, disulfide exchange, etc.)
   Can flow and be reshaped above topology freezing T (Tv)
   Recyclable thermosets — addresses the end-of-life problem
   Commercial: Epoxy vitrimer (IFP Energies, Mallinda, etc.)

   SHAPE MEMORY POLYMERS (SMP):
   ─────────────────────────────
   Two-phase structure: fixed phase (high-Tm or cross-linked)
                        + switching phase (Tg or Tm tuned to trigger T)
   Medical: self-expanding stents, sutures
   Aerospace: deployable structures
   PU, PCL-based systems most commercial
```

---

## Decision Cheat Sheet

| Requirement | Polymer |
|-------------|---------|
| Highest temperature + best overall balance | PEEK |
| Chemical inertness, non-stick, lowest COF | PTFE (or PFA for moldable) |
| Flame retardant, chemical resist, automotive | PPS |
| Steam sterilization, medical/food | PSU, PPSU, PEI (Ultem) |
| Precision gears, zero creep, best fatigue | POM (Delrin or Celcon) |
| 5G electronics, ultra-thin wall connector | LCP |
| Aircraft interior (FAA flame cert) | PEI (Ultem), PPS |
| Oil/gas downhole (150–200°C + chemical) | PEEK or PPSU |
| Recycle a thermoset (emerging) | Vitrimer-based systems |
| Highest T continuous (>300°C) | Polyimide (Kapton, Vespel) |

---

## Common Confusion Points

**PEEK must be crystallized to be useful**: Amorphous PEEK (mold at 25°C) has
Tg = 143°C — only marginally better than PC. Crystallized PEEK (mold at
160–190°C) is stable to 250°C. Mold temperature is not optional — it changes
the material.

**PTFE cannot be injection molded**: Even at 400°C, PTFE melt viscosity is
~10^12 Pa·s. The screw cannot generate that pressure. Only ram-based processes
work. PFA and FEP are processable alternatives at lower property levels.

**LCP weld lines are catastrophic**: In LCP, weld lines (where two flow fronts
meet) are ~10% of unreinforced tensile strength — essentially delamination
planes. LCP part design must ensure flow meets at non-critical areas. This is a
fundamental design constraint, not a defect to correct.

**POM and formaldehyde**: POM degrades to formaldehyde when overheated or
treated with strong acid/alkali. Processing above 240°C or burning POM will
release formaldehyde — an occupational hazard. Always vent injection molding
machines processing POM.
