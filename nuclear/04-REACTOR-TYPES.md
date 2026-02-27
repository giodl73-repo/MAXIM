# 04 — Reactor Types

## PWR, BWR, CANDU, Advanced Designs, SMRs, Gen IV

```
REACTOR CLASSIFICATION MATRIX

                   Moderator
                   ┌──────────┬───────────┬──────────┬──────────┐
Coolant            │  H₂O     │   D₂O     │ Graphite │  None    │
───────────────────┼──────────┼───────────┼──────────┼──────────┤
H₂O (light)        │ PWR, BWR │  —        │  RBMK*   │  —       │
D₂O (heavy)        │  —       │  CANDU    │  —       │  —       │
Liquid Na (sodium) │  —       │  —        │  —       │  SFR     │ ← Fast spectrum
Molten salt        │  —       │  —        │  —       │  MSR     │ ← Liquid fuel
He gas             │  —       │  —        │  —       │  VHTR/GFR│ ← High temp
Pb / Pb-Bi         │  —       │  —        │  —       │  LFR     │ ← Fast spectrum
Supercritical H₂O  │ SCWR     │  —        │  —       │  —       │ ← Future
───────────────────┴──────────┴───────────┴──────────┴──────────┘

Thermal spectrum: moderated reactors (max fissions at 0.025 eV)
Fast spectrum: no moderation (max fissions at 0.1–1 MeV)
*RBMK: graphite moderator + water coolant — unusual combination
```

Reactor type selection is a multi-dimensional trade-off matrix — structurally identical to database engine selection (relational vs document vs columnar) or compute platform selection (VM vs container vs serverless). Each design locks in coupled constraints: PWR's high-pressure primary enables subcooled operation but requires a thick pressure vessel; CANDU's natural uranium fuel eliminates enrichment dependency but requires expensive D2O. The "best" design is always context-dependent — optimized for fuel cycle, safety behavior, capital cost, or operating simplicity.

Understanding reactor types means understanding what each design choice trades:
moderator/coolant selection drives spectrum, pressure, temperature, coolant chemistry,
safety behavior, and fuel cycle. Every type is a different engineering trade-off solution.

---

## Pressurized Water Reactor (PWR)

### System Architecture

```
PRIMARY LOOP:                          SECONDARY LOOP:
                                         (no radioactivity under normal conditions)
Reactor                Steam
Vessel   →  Primary   Generator  →   Turbine → Generator
  ↑          Pump      (U-tube)         ↑
  │                      ↓              │
  │           Pres-    Feedwater ←   Condenser ← Cooling water
  └── fuel ───surizer   Pump
  core

Key: PRIMARY and SECONDARY are separated by steam generator tubes
     → radioactive primary water NEVER contacts turbine
     → allows turbine maintenance without decontamination
```

### PWR Parameters (Westinghouse 4-Loop, ~1100 MWe)

```
Parameter                   Value
──────────────────────────────────────────────────────
Thermal power               3411 MWt
Electrical output           ~1150 MWe (efficiency ~33.5%)
Primary pressure            155.1 bar (15.51 MPa)
Primary coolant temp (in)   291°C
Primary coolant temp (out)  325°C
T_sat at 155 bar            345°C  (35°C subcooling margin)
Secondary steam pressure    ~68 bar
Steam temperature           ~285°C (saturated)
Number of fuel assemblies   193
Fuel: 17×17 array, 264 fuel rods + 24 guide tubes + 1 instrumentation tube
Fuel type                   UO₂ pellets, 3.1–4.8% enrichment
Cladding                    Zircaloy-4 or ZIRLO
Active fuel length           3.66 m (12 ft)
Number of RCPs              4 (Reactor Coolant Pumps)
Number of steam generators  4
Control system              RCCA (Rod Cluster Control Assemblies) + soluble boron
```

### PWR Control Methods

```
1. Soluble boron (chemical shim):
   H₃BO₃ dissolved in primary coolant
   Worth: ~8–11 pcm/ppm
   Used for: slow reactivity changes (cycle burnup compensation, cold shutdown)
   Concentration: 0 ppm (HFP, end of cycle) → ~1200 ppm (HFP, BOC) → ~2000 ppm (cold)

   Advantage: no power peaking (uniform poison distribution)
   Disadvantage: takes hours to dilute/borate; cannot respond to rapid transients

2. Control Rod Cluster Assemblies (RCCA):
   Ag-In-Cd (typical) or B₄C
   Banks: 4 shutdown banks (full insertion for trip) + regulating banks (modulated)
   Worth: total ~7000–10000 pcm; shutdown requires top bank value >> largest worth rod
   Fast response: rods drop by gravity in 1–2 seconds when tripped

3. Burnable absorbers (fixed in fuel):
   Gadolinia (Gd₂O₃) mixed in fuel pellets
   or IFBA (integral fuel burnable absorber: ZrB₂ coating on pellets)
   Burns out over cycle → compensates initial excess reactivity without boron
```

### PWR Variants

```
Westinghouse AP1000: Generation III+ passive safety (see 05-SAFETY)
  2-loop design, 1100 MWe, passive ECCS, passive containment cooling

VVER (Russian PWR):
  Key differences from Westinghouse:
  - Hexagonal fuel assemblies (not square)
  - Horizontal steam generators (not vertical U-tube)
  - Horizontal ECCS injection (not top-down)
  - Cold leg ECCS injection (not direct vessel)
  VVER-1000 (1000 MWe): most common Russian design
  VVER-1200: Generation III+, AES-2006 project

EPR (European Pressurized Reactor, Framatome/EDF):
  1650 MWe, 4 trains safety systems, 60-year life
  Core catcher for severe accidents (melt containment)
  Operating: Olkiluoto-3 (Finland 2023), Flamanville-3 (France 2024 startup)

APR-1400 (Korean):
  1400 MWe, improved safety, UAE Barakah units operating
```

---

## Boiling Water Reactor (BWR)

### Single-Loop Design

```
BWR vs PWR KEY DIFFERENCE: Steam generated INSIDE reactor vessel
  → no steam generators
  → steam (slightly radioactive N-16 from O-16(n,p) reaction) goes directly to turbine
  → turbine and condenser are radiologically controlled areas

REACTOR VESSEL
  ┌─────────────────────────────┐
  │  Steam separators/dryers    │ ← Steam 285°C, 70 bar exits here
  │  ─────────────────────      │
  │  Core (fuel assemblies)     │ → BWR fuel: 10×10, ATRIUM-10 design
  │  ─────────────────────      │
  │  Jet pumps (16 per vessel)  │ ← Recirculation pumps drive jet pumps
  │  Lower plenum               │
  └─────────────────────────────┘
           ↓ Recirculation → External pumps → Back up via jet pumps
```

### BWR Parameters (GE BWR/6, ~1000 MWe)

```
Parameter                   Value
──────────────────────────────────────────────────────
Thermal power               3579 MWt
Electrical output           ~1200 MWe (efficiency ~33.5%)
Primary pressure            ~72 bar (7.2 MPa)  ← lower than PWR!
Core inlet temp             ~278°C
Core exit quality           ~12–15%
Fuel type                   UO₂, 2.5–4.0% enrichment (lower than PWR — fewer epithermal captures)
Cladding                    Zircaloy-2
Active fuel length           3.7 m
Control system              CRD (Control Rod Drives) from below + jet pump flow
No soluble boron in coolant during operation
```

### BWR Control

```
BWR control methods:
  1. Control rods from BELOW (unusual! necessitated by steam separators at top)
     → hydraulically driven CRDs (not gravity-drop; must overcome buoyancy)
     → SCRAM: high-pressure nitrogen drives rods in rapidly

  2. Recirculation flow control:
     Reduce recirculation pump speed → less coolant flow → more steam → negative void → power DOWN
     This allows ~25% power range control WITHOUT moving control rods
     Faster response than chemical changes

  3. No soluble boron during power operation:
     Simplifies chemistry management, avoids MTC complications
     But: critical with pure water means no chemical backup for scram

Stability concern:
  Density-wave oscillations (thermal-hydraulic coupling) at low-flow/high-power
  BWROG stability solution: oscillation power range monitors (OPRM) + operating limits
```

### BWR Generation Evolution

```
GE BWR series:
  BWR/1 (1960): prototype Dresden-1; separate steam drum
  BWR/2–BWR/5 (1960s–70s): progressive improvements, larger power
  BWR/6 (1970s–80s): current design, Grand Gulf/Perry/Clinton
  ABWR (Advanced BWR, 1990s):
    Eliminated external recirculation pipes (LOCA risk reduction)
    Internal recirculation pumps on vessel bottom
    Reinforced containment, shorter LOCA progression
    Operating: Kashiwazaki-Kariwa in Japan
  ESBWR (Economic Simplified BWR):
    Passive safety — natural circulation in core (no recirculation pumps!)
    Gravity-driven cooling system
    NRC design certification obtained
  GE-Hitachi BWRX-300: SMR descendant, 300 MWe, simplified ESBWR design
```

---

## CANDU (CANada Deuterium Uranium)

### Unique Design Philosophy

```
PRESSURE TUBE DESIGN (vs monolithic pressure vessel in LWR):

  Calandria vessel (low pressure, ~1 bar)  ← D₂O moderator at ~70°C, low pressure
    contains thousands of pressure tubes
    Each pressure tube:
      ← D₂O coolant at high pressure (~104 bar) and ~310°C
      ← 37-element fuel bundle (natural UO₂, 0.711% U-235!)

  NO PRESSURE VESSEL: eliminates PWR/BWR large-break LOCA vulnerability
  Individual tube failure: isolated, does not cascade to full core
```

### CANDU Characteristics

```
Parameter                   CANDU 6     ACR-1000
──────────────────────────────────────────────────────────────
Power (MWe)                 ~700        ~1200
Fuel                        Natural UO₂  Slightly enriched (~2%)
Moderator                   D₂O         D₂O
Coolant                     D₂O         Light water (H₂O)
Pressure (bar)              104          ~130
On-power refueling          YES          YES  ← continuous fueling!
Capacity factor             ~90%+       projected high

Key advantages:
  - Natural uranium fuel (no enrichment required) → no enrichment dependence
  - Continuous on-power refueling: no refueling outages → high capacity factor
  - High neutron economy (D₂O, few parasitic absorptions)
  - Can burn thorium, recycled uranium, MOX

D₂O cost: ~$700/kg → significant capital cost; must contain carefully
D₂O leaks: tritium (H-3) content makes D₂O radiologically controlled material
```

### CANDU Safety Considerations

```
Positive void coefficient: CANDU has α_void > 0
  Reason: coolant is D₂O (but not the moderator — moderator is separate cold D₂O)
  If coolant voids: less D₂O absorption in hot channels → slight power increase
  BUT: much smaller effect than RBMK because moderator and coolant are separate

Mitigated by:
  Two independent safety systems: Shutoff Rod System (28 rods) + Liquid Poison Injection
  Both operate on 2-of-3 logic; highly reliable
  Negative temperature coefficient provides additional stability

Pressure tube degradation: key life-limiting issue
  Hydrogen uptake → zirconium hydride → embrittlement
  Pressure tube replacement programs (expensive) at 25–30 years
```

---

## RBMK (Soviet Graphite-Moderated Channel Reactor)

```
Design: graphite moderator, boiling water coolant, individual pressure tubes
  Similar concept to CANDU in channel design; DIFFERENT in physics

Fatal flaw: LARGE POSITIVE VOID COEFFICIENT at low power
  Reason: graphite moderates neutrons; water acts as ABSORBER (not moderator)
  When water boils (voids): less absorption → MORE multiplication → more power → more boiling
  At low power: instability amplified (positive feedback runaway)

  At HIGH power: negative Doppler and temperature coefficients stabilize
  At LOW power (<20%): positive void coefficient dominates → UNSTABLE

Chernobyl Unit 4 (April 26, 1986):
  - Running safety test at low power (~200 MWt, design 3200 MWt)
  - Power excursion: positive void coefficient + reactor in unstable regime
  - AZ-5 (SCRAM): positive "steamroller" effect of graphite tips at rod bottom
    → brief positive reactivity insertion at start of SCRAM → power spike
  - Power excursion to >30,000 MWt → steam explosion + graphite fire
  - No containment → large release of fission products

Post-Chernobyl RBMK modifications:
  - Increased enrichment from 2% to 2.8% (reduces positive void coefficient)
  - Added absorbers to reduce positive steam void coefficient
  - Added graphite displacers to rod ends (eliminates positive scram effect)
  - Reduced minimum power limit from 10% to 20%
  - Currently operating: ~8 units in Russia (Smolensk, Leningrad, Kursk)
  - All new designs globally now require negative void coefficient
```

---

## Generation III/III+ Designs

### Design Philosophy Shift

```
Generation I (1950s–60s): proof-of-concept, low safety margins, short lives
Generation II (1970s–90s): operating fleet today, active safety systems
  → PWR, BWR, CANDU 6, VVER — most of 440 currently operating reactors

Generation III (1990s): evolutionary improvements
  → Better fuel economy, higher capacity factors, lower operating costs
  → 60-year design life (vs 40 years for Gen II)
  → ABWR, System 80+, AP-600

Generation III+ (2000s–present): PASSIVE safety revolution
  KEY CHANGE: passive safety systems require NO AC POWER, NO OPERATOR ACTION
  → Gravity-driven, natural circulation, stored water tank drainage
  → AP1000 (Westinghouse), EPR (Framatome), APR-1400 (KEPCO)

  Fukushima validation: AP1000 passive systems would have prevented accident
  (72-hour coping capability without external power)
```

### AP1000 Passive Safety Features

```
Core:
  ADS (Automatic Depressurization System): 4-stage pressure relief → depressurize quickly
  CMT (Core Makeup Tanks): 2 × 70 m³ tanks, pressurized with N₂ → inject on SIAS

  Accumulators: 2 × large → passive injection at intermediate pressure
  IRWST (In-containment Refueling Water Storage Tank): 1700 m³ above core
    → passive injection once pressure drops to near atmospheric
    → provides 72 hours of core cooling by gravity

Containment cooling:
  PCS (Passive Containment Cooling): baffle + air chimney + water from roof tank
    → condensation on steel containment shell → water flows down → air cooling
    → no pumps or fans → lasts 72 hours on stored water, indefinitely on air alone

Fukushima comparison:
  All AP1000 passive safety function without ANY external power or operator action
  72+ hour grace period before any operator action required
```

---

## Small Modular Reactors (SMRs)

### Definition and Motivation

```
SMR: < 300 MWe per module (typical definition)
  Some sources say < 1000 MWe (broader)

Why SMRs?
  Large conventional plants: ~$10B, 10+ year construction → major financial risk
  SMRs: factory fabrication → learning curve → serial production cost reduction
  Modular deployment: start small, add modules as demand grows
  Siting flexibility: smaller site, lower water needs, remote/isolated locations

  Current status (2024):
    NuScale NRC certification: first SMR design approved (2022); BUT
    NuScale VOYGR project cancelled (2023) due to cost escalation
    Many designs in development; commercial viability still unproven at scale
```

### Key SMR Designs

```
NuScale Power Module (LWR SMR):
  77 MWe per module, up to 12 modules per plant (924 MWe total)
  Integral design: steam generators inside reactor pressure vessel
  Fully passive: no pumps needed — natural circulation in primary loop
  Underground pool: modules sit in shared water pool (passive heat sink)
  Status: design certified; economic challenges paused initial deployment

BWRX-300 (GE-Hitachi):
  300 MWe, simplified ESBWR (boiling water design)
  10× material reduction vs standard BWR
  Natural circulation core cooling (no recirculation pumps)
  Progress: agreements with Ontario Power Generation, TVA

Kairos KP-FHR (Kairos Power):
  140 MWe, fluoride salt coolant + TRISO pebble fuel
  Low pressure (1 bar), high temperature → very different from LWRs
  First-of-kind regulatory path in US; demonstration plant permitted

Terrestrial Energy IMSR (Molten Salt SMR):
  195 MWe, integral design, 7-year operational cassette, clean MSR approach

Holtec SMR-300:
  300 MWe, PWR-type integral, passive safety
  UK and other market targets
```

---

## Generation IV Reactor Concepts

### GIF Framework (Generation IV International Forum)

Six concepts selected in 2002 for development toward 2040+ deployment:

### Sodium-cooled Fast Reactor (SFR)

```
Coolant: liquid sodium (Na), ~500°C, near atmospheric pressure
Spectrum: fast neutrons (no moderation — Na has some moderating effect but small)
Fuel: mixed oxide (MOX) or metal alloy (U-Pu-Zr)

Advantages:
  Breeder potential: converts fertile U-238 → fissile Pu-239 (BR > 1.0)
  Actinide burning: can fission long-lived minor actinides (Np, Am, Cm)
    → reduces waste radiotoxicity timescale from 300,000 → ~1000 years
  Higher efficiency: ~40% (vs ~33% LWR) due to higher temperatures

Challenges:
  Sodium chemistry: reactive with water → Na-H₂O explosions; opaque → difficult inspection
  Intermediate loop: primary Na → intermediate Na → steam generator (prevents Na-water contact)
  Positive void coefficient possible: must design carefully

Operating:
  BN-800 (Russia): 800 MWe, operating since 2016, MOX fuel
  BN-1200: planned, commercial-scale Russian SFR
  China CFR-600: under construction, 600 MWe

  Historical: EBR-II (US, 1964-1994), Phenix/SuperPhenix (France), Monju (Japan, closed)
  IFR (Integral Fast Reactor): EBR-II metal fuel + pyroprocessing; cancelled 1994 by Clinton
```

### Molten Salt Reactor (MSR)

```
Key innovation: LIQUID FUEL — uranium dissolved in fluoride salt (LiF-BeF₂-UF₄ = FLiBe)
  → No fuel fabrication costs, no fuel damage from radiation
  → Online fission product removal (volatile gases bubble out)
  → Strongly negative void/temperature coefficient (liquid fuel expands when hot → less dense)
  → Drains safely on loss of power ("drain tank" freeze plug melts)

Configurations:
  Thermal MSR (MSRE Oak Ridge 1965-1969): graphite moderated, well-characterized
  Fast-spectrum MSR: no moderator, higher actinide utilization
  Chloride fast reactor (TerraPower): NaCl-UCl₃ fuel, fast spectrum

Thorium potential: MSR suited for thorium cycle
  Th-232 + n → Pa-233 → U-233 (fissile) → can run on thorium
  India's AHWR program; ThorCon (Indonesia contract)

Challenges:
  Tritium production (from Li-6 in FLiBe) → permeation through heat exchangers
  Materials: fluoride salts highly corrosive, especially hot and irradiated
  Hastelloy-N, new alloys needed
  Online reprocessing: proliferation concern (continuous fissile material processing)

Commercial players: Terrestrial Energy, Thorcon, Moltex Energy, Elysium Industries
```

### Very High Temperature Reactor (VHTR)

```
Coolant: helium gas (inert, no activation problem)
Outlet temperature: 850–1000°C (vs ~325°C LWR) → MUCH higher efficiency + process heat

TRISO fuel: TRistructural ISOtropic particle
  UO₂ or UCO kernel (0.5 mm) surrounded by:
    Buffer layer (porous carbon)
    Inner PyC (pyrolytic carbon)
    SiC layer (primary fission product barrier, melts at 2800°C)
    Outer PyC
  Packed in graphite sphere (pebble bed) or cylindrical compact

  Fission product retention: TRISO particles retain FPs up to 1600°C
  Pebble bed: ~20,000 pebbles per m³, gravity flow, continuous fueling possible
  → "Walk-away safe": passive decay heat removal by radiation + conduction → never melt

Applications beyond electricity:
  Process heat: >900°C enables hydrogen production (thermochemical H₂S-I cycle)
  Steel, petrochemical, cement industries

  X-Energy Xe-100: 80 MWe pebble bed HTGR, US DOE ARDP funding, TVA site agreement
  HTR-PM (China): two 250 MWt modules at Shidao Bay → operating 2021
  PBMR (South Africa): cancelled 2010 due to funding
```

### Other Gen IV Concepts

```
Gas-cooled Fast Reactor (GFR):
  He coolant + fast spectrum → breed + burn actinides like SFR but with He
  Challenge: He provides almost NO emergency cooling (unlike sodium or water)
  → requires dedicated decay heat removal systems

Lead-cooled Fast Reactor (LFR):
  Pb or Pb-Bi coolant: high boiling point (1743°C), low pressure, near-transparent
  Natural circulation decay heat removal feasible
  BREST-OD-300 (Russia): lead-cooled, under construction at Seversk
  Lead bismuth used in Russian Alpha-class submarine reactors (operational experience)

Supercritical Water-cooled Reactor (SCWR):
  Water above critical point (374°C, 221 bar) → single-phase fluid (no boiling crisis)
  Efficiency ~44% (vs 33% LWR)
  Challenge: extremely harsh environment for materials; corrosion very difficult
```

---

## Fusion Reactors

### ITER and the Lawson Criterion

```
D-T fusion:  D + T → ⁴He (3.5 MeV) + n (14.1 MeV)   Q = 17.6 MeV

Lawson criterion for breakeven: n τ_E T > 3×10²¹ m⁻³·s·keV
  n = plasma density [m⁻³]
  τ_E = energy confinement time [s]
  T = plasma temperature [keV]

ITER (International Thermonuclear Experimental Reactor):
  Purpose: demonstrate Q = 10 (fusion power / heating power)
  n ≈ 10²⁰ m⁻³,  τ_E ≈ 3–4 s,  T ≈ 150 million K (10 keV)
  Plasma current: 15 MA; B_toroidal = 5.3 T (superconducting REBCO magnets)
  Expected first plasma: 2025–2027; Q ≥ 10 experiments: ~2035
  Tritium breeding: Li-6 blanket → T must be bred (no natural supply)

SPARC (Commonwealth Fusion Systems + MIT):
  High-field compact tokamak: B = 12 T (REBCO HTS magnets — 3× ITER field!)
  Net fusion power demonstration target: Q > 2; smaller, faster, cheaper
  Target: commercial first-of-kind ~2040

NIF (National Ignition Facility) — Inertial Confinement Fusion:
  December 2022: first ignition achieved (3.15 MJ out / 2.05 MJ laser in → Q=1.5)
  But: laser requires ~400 MJ from grid → overall Q << 1
  Path to commercial: need driver efficiency ×100 improvement + rep rate ×1,000,000
  IFE remains research-stage; no credible commercial timeline
```

---

## Fuel Cycles

```
Fuel cycle options:

"Once-through" (open cycle):
  Mine U → Enrich → Fabricate → Reactor → Spent fuel storage → Permanent repository
  US, Canada, Sweden, Finland
  ~96% of spent fuel is unfissioned U-238 + ~1% Pu — all "wasted"

Limited reprocessing:
  Mine U → Enrich → Reactor → Reprocessing (PUREX) → MOX fuel + HLW vitrification
  France, UK, Japan, Russia
  ~25% reduction in waste volume; Pu recycled as MOX (one pass)
  Proliferation concern: separated Pu (weapons-usable material)

Thorium cycle (potential):
  Th-232 (abundant, monoisotopic) + n → Pa-233 → U-233 (fissile)
  U-233 contains U-232 (hard gamma) → proliferation-resistant (self-protecting)
  India AHWR (Advanced Heavy Water Reactor): designed for Th-U-233 cycle
  MSR-based thorium: online reprocessing enables continuous Pa-233 removal + thorium economy

Full actinide recycling (advanced fuel cycle):
  SFR + pyroprocessing → breed Pu from U-238, burn minor actinides (Np, Am, Cm)
  → converts long-lived waste to shorter-lived fission products
  IFR concept: 300,000 year → 500 year waste radiotoxicity reduction (claimed)
```

---

## Common Confusion Points

**PWR vs BWR radiation zoning:** In a PWR, the turbine building is NOT radiologically
controlled under normal conditions (secondary loop is clean). In a BWR, the turbine
building IS controlled (primary steam contains N-16, activated corrosion products).
BWR turbine maintenance during power operation requires significant dose management.

**CANDU on-power refueling is not the same as not having outages:** CANDU has
planned maintenance outages. On-power refueling eliminates the long refueling outage
of LWRs (~30–40 days) but doesn't eliminate all scheduled outages.

**SMRs are not inherently safer per se:** Some SMR designs have enhanced passive
safety (NuScale, BWRX-300). But "SMR" is a size designation, not a safety classification.
A poorly designed 100 MWe reactor can be less safe than a well-designed 1600 MWe EPR.

**Gen IV = commercially viable around 2040:** The "GIF 2040" vision dates to 2002.
As of 2024, only SFR has significant operational experience (Russia, China). MSR, VHTR,
LFR are at demonstration scale. Don't expect Gen IV commercial dominance before 2050.

**Fusion is always "30 years away":** Now more specifically: ITER D-T operations ~2035,
SPARC ignition ~2027, first commercial fusion ~2040s at optimistic estimates.
The NIF 2022 result was scientifically significant but not on the commercial path (laser ICF).

---

## Decision Cheat Sheet

| Design question | Consideration | Answer |
|----------------|---------------|--------|
| Why use D₂O instead of H₂O? | Neutron economy | Allows natural uranium fuel; no enrichment needed |
| Why does PWR have two loops? | Turbine contamination | Separates radioactive primary from steam turbine |
| BWR vs PWR: which is simpler? | System count | BWR: no steam generators, but radioactive turbine |
| What makes RBMK dangerous? | Void coefficient | Positive α_void → unstable at low power |
| Why passive safety? | Station blackout | No AC power needed → Fukushima-proof |
| Best breeding ratio? | Fast reactor | SFR BR > 1.0 → creates more Pu than it burns |
| Highest outlet temperature? | VHTR/MSR | 850–1000°C → H₂ production, industrial process heat |
| Most proliferation-resistant thermal cycle? | Thorium + U-233 | U-232 gamma makes U-233 self-protecting |
| Status of SMRs? | Commercial readiness | Early stage; NuScale certified but delayed economically |
| When will fusion contribute? | Timeline | Commercial ~2040–2050 at optimistic estimates |
