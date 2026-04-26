# The p-Block Remainder — B, Al, Si, Ge/As/Sb, Se/Te/Po, Sn, Pb, Bi

## The Big Picture

After removing the elements already covered (C, N, O, P, S, halogens, noble gases),
the remaining p-block elements span Groups 13–16 from Period 2 through Period 6.

```
P-BLOCK REMAINDER — PERIODIC TABLE POSITION

 Group:   13       14        15       16
          B        C*        N*       O*
Period 2  boron    (C→06)    (N→06)   (O→06)

Period 3  Al       Si        P*       S*
          aluminum silicon   (P→06)   (S→06)

Period 4  Ga       Ge        As       Se
          gallium  germanium arsenic  selenium

Period 5  In       Sn        Sb       Te
          indium   tin       antimony tellurium

Period 6  Tl       Pb        Bi       Po
          thallium lead      bismuth  polonium

* covered in 06-LIFE-NONMETALS.md

METALLOID STAIRCASE:
  B / Si / Ge / As / Sb / Te / Po (sometimes At)
  Left of staircase = metals | Right = nonmetals | Staircase = metalloids (semiconductors)
```

---

## Boron (B, Z=5) — Electron-Deficient Chemistry

### The Boron Anomaly

```
ELECTRON CONFIGURATION: [He] 2s² 2p¹
Boron has only 3 valence electrons → forms only 3 bonds in simple compounds
→ electron deficient (less than octet in Lewis structures)

BF₃:     trigonal planar, sp² hybridized
          F has lone pairs → partial π donation into empty p orbital on B
          But still a Lewis acid (accepts e⁻ pair) → key reagent/catalyst

BCl₃ + NH₃ → H₃N:BCl₃  (Lewis acid-base adduct, dative bond)
```

### Boranes — 3-Center 2-Electron Bonds

```
DIBORANE (B₂H₆): simplest borane, textbook example of electron-deficient bonding

  H   H   H
   \ / \ /
    B   B
   / \ / \
  H   H   H
       (wrong — this implies 4-center bond)

ACTUAL STRUCTURE:
  ┌─────────────────────────────────────────────────────────┐
  │  Each B has 2 terminal H (normal 2c-2e bonds)           │
  │  Two bridging H atoms: each shared between both B atoms │
  │                                                         │
  │      Ht    Hb    Ht                                     │
  │       \   / \   /                                       │
  │        B       B                                        │
  │       /   \ /   \                                       │
  │      Ht    Hb    Ht                                     │
  │                                                         │
  │  The B–Hb–B bridge: 3-center 2-electron bond            │
  │  2 electrons delocalized over B–H–B (banana bond)       │
  └─────────────────────────────────────────────────────────┘

Higher boranes: B₄H₁₀, B₅H₉, icosahedral B₁₂H₁₂²⁻ closo-borane
Wade's rules predict borane cage geometries (electron counting)
Carboranes: replace B–H with C–H in the cage (heteroatom analogs)
```

### Boron Applications

```
BOROSILICATE GLASS (Pyrex):
  SiO₂ + B₂O₃ (typically ~13% B₂O₃) + Al₂O₃ + Na₂O
  B₂O₃ reduces thermal expansion coefficient → Pyrex ~3.3×10⁻⁶/°C vs soda lime ~9×10⁻⁶/°C
  Result: thermal shock resistant → labware, cookware, telescopes

NEUTRON CAPTURE:
  ¹⁰B has huge neutron capture cross-section (3840 barns — 10× most elements)
  ¹⁰B + n → ⁷Li + α (+ 2.31 MeV, short-range)
  Boron Neutron Capture Therapy (BNCT): B-laden drug → tumor; irradiate with slow neutrons
  → α particles kill tumor cells at μm range (no systemic damage)
  Clinical in Japan (melanoma, head/neck cancer)

  Control rods in nuclear reactors: B₄C (boron carbide) rods absorb neutrons → power control

BORIC ACID AND BORAX:
  H₃BO₃ (boric acid): mild antiseptic, eye wash, cockroach bait (disrupts metabolism)
  Na₂B₄O₇·10H₂O (borax): laundry booster (buffer + stain removal), glass/ceramics flux

ORGANOBORON IN SYNTHESIS:
  Miyaura borylation, Suzuki coupling (see 09-TRANSITION-4D5D.md for Pd catalysis)
  Boronic acids R-B(OH)₂ → key partners in Pd-catalyzed cross-coupling
  Proteasome inhibitor Bortezomib (Velcade): B as pharmacophore — treats multiple myeloma
```

---

## Aluminum (Al, Z=13) — Most Abundant Metal

### Structure and Properties

```
[Ne] 3s² 3p¹ → Al³⁺ (always +3 in normal chemistry)
Density: 2.7 g/cm³ (1/3 of steel)
Tensile strength (pure): 90 MPa (low — but alloys fix this)
Electrical conductivity: 61% of copper (but 1/3 density → better per kg for wires)
Thermal conductivity: 205 W/m·K (good, but below Cu)
```

### Hall-Héroult Process

```
Al₂O₃ REDUCTION (cannot use carbon reduction — Al₂O₃ too stable; SiO₂ can be reduced):

  BAYER PROCESS (refining Al₂O₃ from bauxite):
    Bauxite (Al(OH)₃ + AlOOH + impurities) + NaOH (hot) → Na[Al(OH)₄] in solution
    Impurities (Fe₂O₃ → "red mud") settle out
    Cool → Al(OH)₃ precipitates (seeding)
    Calcine: 2 Al(OH)₃ → Al₂O₃ + 3 H₂O (1200°C)

  HALL-HÉROULT ELECTROLYSIS:
    Al₂O₃ dissolved in molten cryolite (Na₃AlF₆) at ~960°C (lowers mp from 2054°C)
    Carbon anode (consumed): 2 Al₂O₃ + 3 C → 4 Al + 3 CO₂
    Cathode: Al³⁺ + 3e⁻ → Al(l)  (liquid Al collects at bottom)
    Energy: ~13-15 kWh/kg Al — energy-intensive (electricity = largest cost)
    → "Aluminium is solidified electricity"
    Recycling Al uses only 5% of primary production energy → recycling highly economic
```

### Passivation and Corrosion Resistance

```
NATIVE OXIDE LAYER:
  Al + O₂ → Al₂O₃ (forms instantly, ~4 nm thick)
  Al₂O₃ is hard, dense, adheres strongly → seals underlying metal from further oxidation
  This is why Al is corrosion-resistant despite very negative E° (−1.66 V)

ANODIZING:
  Electrolytic process: Al anode in sulfuric acid → thicker Al₂O₃ (up to 25 μm)
  Porous oxide → dye absorption → color anodizing (MacBooks, iPhones)
  Sealing: hot water / nickel acetate → closes pores → final corrosion barrier

THERMITE REACTION:
  Al₂O₃ is so stable that Al can reduce less stable metal oxides:
  2 Al + Fe₂O₃ → Al₂O₃ + 2 Fe + 3600 kJ  (ΔT > 2000°C)
  Used for: welding railroad tracks, incendiary materials, emergency cutting
```

### Aluminum Alloys

```
ALLOYING SYSTEMS:
  2xxx (Al-Cu): high strength, aerospace (2024 — wings, structural); not weldable
  5xxx (Al-Mg): marine, weldable, moderate strength
  6xxx (Al-Mg-Si): extrusions, automotive, architectural (6061, 6063); heat treatable
  7xxx (Al-Zn-Mg-Cu): highest strength Al alloys (7075, 7068); aerospace fuselage, wings
  8xxx (Al-Li): aerospace (Al-Li 2099, 2199) — Li reduces density by ~3% per 1% Li added

AGE HARDENING (precipitation hardening):
  Quench from ~500°C → supersaturated solid solution
  Age at 120-200°C → fine precipitates form (e.g., Mg₂Si in 6xxx)
  Precipitates block dislocation motion → strength increases dramatically
  T6 temper = solution heat treated + artificially aged (peak strength)
```

---

## Silicon (Si, Z=14) — The Semiconductor Foundation

### Crystal Structure and Band Gap

```
DIAMOND-CUBIC STRUCTURE:
  Each Si atom: 4 covalent bonds to neighbors, tetrahedral geometry
  Lattice parameter: 5.43 Å
  Hardness: 6.5 Mohs (harder than most metals, less than diamond)

ELECTRONIC PROPERTIES:
  Band gap: 1.12 eV (indirect) — ideal for solar cells, transistors
  Intrinsic carrier concentration: 1.5×10¹⁰ cm⁻³ at 300 K
  (Ge: 2.4×10¹³ — more intrinsic carriers, worse high-T performance)
  (GaAs: 2×10⁶ — fewer intrinsic carriers, faster but more expensive)

DOPING:
  n-type: Group 15 dopants (P, As, Sb) → donor electrons → extra electrons conduct
  p-type: Group 13 dopants (B, Al, Ga) → acceptors → holes conduct
  Carrier concentration controlled from 10¹⁰ to 10²⁰ cm⁻³ (10 orders of magnitude!)
```

### Silicon in Earth's Crust and Glass

```
SILICON ABUNDANCE:
  Second most abundant element in Earth's crust (28%, after oxygen)
  Silicon doesn't occur free — always bonded to oxygen (SiO₂ or silicates)

SILICA (SiO₂):
  Three-dimensional covalent network: each Si bonds to 4 O, each O to 2 Si
  mp = 1713°C; density = 2.2 g/cm³ (amorphous) / 2.65 (quartz)
  Polymorphs: quartz (common), tridymite, cristobalite, coesite (high P), stishovite (ultrahigh P)
  Fused quartz/silica: very high melting, low thermal expansion, UV transparent
  → optical fiber (high-purity silica → loss <0.2 dB/km)

SILICATES (most minerals):
  [SiO₄]⁴⁻ tetrahedra as building blocks
  Orthosilicate: isolated [SiO₄]⁴⁻ (olivine: Mg₂SiO₄)
  Pyroxene: single-chain [SiO₃]²⁻  (enstatite)
  Mica: double-layer sheets [Si₄O₁₀]⁴⁻ (muscovite, biotite → easily cleaved)
  Feldspar: 3D framework (orthoclase KAlSi₃O₈ — most common mineral on Earth surface)
  Zeolites: 3D framework with open channels → molecular sieve, catalysis, ion exchange

GLASS:
  SiO₂ + Na₂O + CaO → soda-lime glass (windows, bottles; mp ~700°C)
  Add B₂O₃ → borosilicate (Pyrex)
  Add PbO → lead crystal (high refractive index, high density)
  Add rare earth oxides → optical glass with specific n/dispersion
```

Silicon's band gap of 1.12 eV sits at the sweet spot for room-temperature transistor operation: large enough that thermal fluctuations don't spontaneously flip bits (a 0.1 eV gap would be unusable at 300 K), small enough that gate voltage on a MOSFET can easily modulate the channel from insulating to conducting. The CMOS inverter — the NOT gate that every digital circuit reduces to — is two complementary MOSFETs (n-type + p-type) wired so that exactly one conducts at a time: near-zero static power draw, which is why ~17 billion transistors on a CPU die don't simply melt. Every .NET runtime, every Azure VM allocation, every SQL Server page fault ultimately executes as electron flow controlled by doped silicon junctions manufactured at atomic precision.

### Semiconductor Manufacturing

```
SILICON PURIFICATION (metallurgical → electronic grade):
  1. Metallurgical Si (98%): SiO₂ + 2C → Si + 2CO (electric arc furnace)
  2. Siemens process → polysilicon (9N purity):
     Si + 3 HCl → SiHCl₃ (trichlorosilane) → distill → SiHCl₃ + H₂ → Si + 3 HCl (CVD rod)
  3. Czochralski process: seed crystal pulled from molten Si → single-crystal boule (300 mm dia)
  4. Float-zone refinement (alternative): zone melt passes → impurities swept to ends

SILICON IN COMPUTERS:
  MOSFET: Metal-Oxide-Semiconductor Field Effect Transistor
    Gate oxide (SiO₂ or HfO₂) insulates gate from Si channel
    Applying gate voltage → controls channel conductance
    CMOS: complementary n+p MOSFET pairs → near-zero static power
  TSMC N3 (2022): 3 nm process node → ~17 billion transistors/cm²
  End of Dennard scaling (2006): power per transistor stopped decreasing → chiplet era
```

---

## The Metalloid Staircase — Ge, As, Sb, Se, Te, Po

### Germanium (Ge, Z=32)

```
[Ar] 3d¹⁰ 4s² 4p²  — same group as Si and C (Group 14)
Band gap: 0.67 eV (indirect, narrower than Si → detects lower-energy photons)
Used before Si dominated (first transistors, 1947, Bell Labs — Ge)
Current uses:
  Fiber optic doping: GeO₂ raises refractive index → graded-index fiber core
  Infrared optics: Ge is transparent to 2–16 μm (IR), opaque to visible
    → IR lenses, night-vision cameras, FLIR, missile seekers
  SiGe alloys: HBT (heterojunction bipolar transistors) — high-frequency RF (cell phones)
  Eka-silicon: predicted by Mendeleev 1871, discovered 1886 — one of his three famous hits
```

### Arsenic (As, Z=33)

```
[Ar] 3d¹⁰ 4s² 4p³  — Group 15 metalloid
Gray arsenic: most stable, semimetal, layered structure
As₄O₆: white arsenic (As₂O₃) — historical poison (tasteless in small doses)
        Marsh test (1836): converts As compounds to AsH₃ gas → silver mirror → detect

SEMICONDUCTOR:
  GaAs (gallium arsenide): direct band gap 1.42 eV
    High electron mobility (8500 cm²/V·s vs Si 1400)
    Used in: microwave devices, solar cells (multi-junction concentrators), LEDs/lasers
    MESFET, pHEMT for RF amplifiers (cell phone front-end)
  InAs: narrow gap → IR detectors
  AlGaAs/GaAs heterostructures → 2DEG (2D electron gas) → quantum Hall effect

TOXICITY:
  Inorganic As (As³⁺, As⁵⁺): IARC Group 1 carcinogen
  Affects enzyme function (binds vicinal dithiols like lipoic acid)
  Groundwater contamination → massive poisoning crisis in Bangladesh, West Bengal
  Chronic: Mees' lines on nails, hyperpigmentation, peripheral neuropathy, cancers
  Organic As in seafood (arsenobetaine): relatively non-toxic — body excretes intact
```

### Antimony (Sb, Z=51), Selenium (Se, Z=34), Tellurium (Te, Z=52)

```
ANTIMONY (Sb):
  [Kr] 4d¹⁰ 5s² 5p³
  Lead-antimony alloys: Sb hardens Pb → lead-acid battery plates, lead shot, solder
  Flame retardants: Sb₂O₃ synergizes with halogenated flame retardants (Sb-halide radicals)
  SbCl₃/SbF₃: Lewis acid catalysts, precursors

SELENIUM (Se, Z=34):
  [Ar] 3d¹⁰ 4s² 4p⁴
  Photoconductor: Se changes electrical resistance when struck by light → early photocopiers
    (Xe lamp + Se drum → toner transfer → xerography, Xerox 914, 1959)
  Selenoproteins: Sec (selenocysteine, the "21st amino acid") in glutathione peroxidase
    GPx scavenges H₂O₂ → antioxidant defense; Se deficiency → Keshan disease (cardiomyopathy)
  Dietary essential: RDA ~55 μg/day; toxic above ~400 μg/day (narrow therapeutic window)
  CIGS solar cells: CuInGaSe₂ — thin-film PV, 22%+ efficiency, flexible substrates

TELLURIUM (Te, Z=52):
  [Kr] 4d¹⁰ 5s² 5p⁴
  Extremely rare (0.001 ppm crust — rarer than platinum)
  CdTe solar cells: First Solar's technology — 22% efficiency, cheapest thin-film PV
  PbTe thermoelectrics: figure of merit ZT ≈ 2 at 500–800 K → waste heat recovery
  Bi₂Te₃: room-temperature thermoelectric → thermoelectric coolers (Peltier modules)
  GeSbTe alloys: phase-change memory (crystalline vs amorphous → different reflectivity/resistance)
    → optical discs (DVD-RW, Blu-ray RW) and PCM non-volatile memory (Intel Optane)
```

### Gallium (Ga, Z=31) and Thallium (Tl, Z=81) — Group 13 Remainder

```
GALLIUM (Ga, Z=31):
  [Ar] 3d¹⁰ 4s² 4p¹  — mp = 29.8°C (melts in your hand); bp = 2204°C
  Predicted by Mendeleev (eka-aluminium, 1871), discovered 1875 → confirmed his predictions

  GaN (gallium nitride): direct bandgap 3.4 eV → wide bandgap semiconductor
    LEDs: GaN/InGaN → blue/UV LEDs (Nakamura, Nobel 2014)
           Blue + YAG phosphor → white LED (every light bulb after ~2010)
    Power electronics: GaN transistors switch at higher voltage/frequency than Si
           → fast-charging USB-C adapters (Gallium Nitride chargers, 2019+)
           → SiC and GaN replacing Si in EV inverters, data center PSUs
    RF: GaN HEMTs dominate microwave power amplifiers (5G base stations, radar)

  GaAs (gallium arsenide): direct bandgap 1.42 eV
    High electron mobility (6× Si) → fast RF switching
    Multi-junction solar cells: GaInP/GaAs/Ge stack → 40%+ efficiency (space PV)
    Lasers and LEDs at 800–900 nm (fiberoptic, CD/DVD)

  Gallium supply: byproduct of aluminum smelting (bauxite processing)
    ~400 tonnes/yr global production; China ~80%
    Critical material designation (EU, US DoD) — GaN chips are supply chain concern

THALLIUM (Tl, Z=81):
  [Xe] 4f¹⁴ 5d¹⁰ 6s² 6p¹  — +1 and +3 states; Tl⁺ chemically mimics K⁺ (same size)

  TOXICOLOGY:
    Tl⁺ (thallous ion) competes with K⁺ in biology → disrupts Na/K ATPase, substitutes
    in K⁺ channels, blocks mitochondrial K⁺ transport
    Symptoms: delayed 2–5 days → hair loss (alopecia — classic sign), peripheral neuropathy,
    Mees' lines on nails, CNS damage
    Historically used as rat/insect poison (tasteless, odorless) and in criminal poisonings
    Antidote: Prussian blue (Fe₄[Fe(CN)₆]₃) — binds Tl⁺ in gut via ion exchange, prevents
    re-absorption → approved for Cs-137 and Tl poisoning

  APPLICATIONS:
    Tl-201: γ emitter for cardiac stress test imaging (myocardial perfusion)
            accumulates in viable heart muscle (K⁺ analog); largely replaced by Tc-99m
    TlBr: scintillator for γ-ray detectors; room-temperature operation
    Tl₂SO₄: was used as rodenticide; now banned in most countries (human poisoning risk)
```

### Polonium (Po, Z=84)

```
[Xe] 4f¹⁴ 5d¹⁰ 6s² 6p⁴
All isotopes radioactive; ²¹⁰Po most accessible (t½ = 138 days, α emitter)
Only element with simple cubic crystal structure (at room temp)
PRODUCTION: neutron bombardment of ²⁰⁹Bi → ²¹⁰Bi (β⁻) → ²¹⁰Po

α emitter → extreme specific activity (166 TBq/g) → intense internal hazard
POISONING: Alexander Litvinenko (2006) — ingested Po-210 in London; fatal polonium poisoning

USES:
  Antistatic devices: α particles ionize air → dissipates static charge → film processing,
                      clean rooms, printing (Am-241 now more common)
  RTG (historic): Po-210 heat source in early Soviet Lunik probes
  Research: high-intensity α source, but handling requires extreme precautions
```

---

## Tin (Sn, Z=50) and Lead (Pb, Z=82) — Group 14 Metals

### Tin

```
[Kr] 4d¹⁰ 5s² 5p²  — two oxidation states: Sn²⁺ (stannous) and Sn⁴⁺ (stannic)
Allotropes:
  β-Sn (white tin): metallic, stable >13.2°C
  α-Sn (gray tin): semiconducting, diamond-cubic — stable below 13.2°C
  Tin pest: β → α at very low T → crumbling (destroyed equipment in Arctic expeditions;
            Scott's Antarctic fuel cans soldered with Sn failed due to tin pest)

APPLICATIONS:
  Solder (traditional): Sn-Pb (63:37 eutectic, mp 183°C) → electronics soldering
    Lead-free solder (RoHS): Sn-Ag-Cu (SAC, e.g., SAC305: 96.5 Sn + 3% Ag + 0.5% Cu)
    mp = 217-220°C → higher reflow temp → board stress concerns
  Tinplate: thin Sn coating on steel (food cans) — Sn passivates, protects from rust
    Electrolytic tinning: 0.2–0.5 μm Sn on steel strip
  Bronze: Cu + Sn (90:10 typical) → harder than pure Cu, lower mp than Cu → casting
  Pewter: Sn + Cu + Sb (modern) or Sn + Pb (historical)
  Organotin compounds: Bu₂SnX₂ → PVC stabilizers (historically); tributyltin (TBT) →
                       antifouling marine paint — now banned (endocrine disruption in mollusks)
```

### Lead (Pb, Z=82)

```
[Xe] 4f¹⁴ 5d¹⁰ 6s² 6p²
Density: 11.3 g/cm³ (very dense — radiation shielding, ballast, fishing weights)
Soft metal (1.5 Mohs), low mp (327°C), easily alloyed

LEAD-ACID BATTERIES:
  Anode: Pb → Pb²⁺ + 2e⁻
  Cathode: PbO₂ + 4H⁺ + 2e⁻ → Pb²⁺ + 2H₂O
  Electrolyte: H₂SO₄ (35–40% by weight)
  Cell voltage: ~2 V; car battery 12 V = 6 cells
  High current → SLI (starting, lighting, ignition) and UPS
  Low energy density (~35 Wh/kg) but cheap, robust, recyclable (>99% recovery rate)

RADIATION SHIELDING:
  High Z (82) and density → excellent γ-ray/X-ray attenuation
  ½ value layer at 100 keV: Pb ~0.12 mm; concrete ~4 cm
  X-ray rooms, medical imaging suites, nuclear reactor rooms
  Lead apron: ~0.5 mm Pb equivalent

LEAD TOXICITY:
  Lead poisoning (plumbism): affects brain development, IQ in children; causes anaemia,
  kidney damage, peripheral neuropathy
  Routes: leaded gasoline (TEL: tetraethyllead, antiknock additive, banned globally by ~2000)
          lead paint (homes pre-1978 in US — ongoing hazard from renovation dust)
          lead pipes (Flint, Michigan 2014-2019 water crisis)
  Mechanism: Pb²⁺ mimics Ca²⁺ → disrupts Ca-dependent enzymes, calmodulin,
             inhibits δ-ALAD → heme synthesis disruption → elevated blood protoporphyrin
  "Safe" blood lead level: currently <5 μg/dL (children); CDC revised down from 10 μg/dL
  Historical exposure: Rome's lead plumbing, lead-sweetened wine (Pb acetate = "sugar of lead")

TETRAETHYLLEAD (TEL):
  (CH₃CH₂)₄Pb: knocking suppressant in gasoline, 1921–1970s+ adoption
  Antiknock mechanism: Pb• radical scavenges combustion radicals → prevents pre-ignition
  Phased out: catalytic converter incompatibility + health evidence (Clair Patterson, 1970s)
  Patterson: measured lead in ice cores → proved 200× increase since industrial era → clean air act
```

---

## Bismuth (Bi, Z=83) — Least Toxic Heavy Metal

```
[Xe] 4f¹⁴ 5d¹⁰ 6s² 6p³
The last stable or near-stable element by proton number
²⁰⁹Bi: technically radioactive (α decay, t½ = 1.9×10¹⁹ yr — ~10⁹× age of universe)
         Effectively stable for all practical purposes
High density (9.8 g/cm³), brittle, low melting point (271°C)
Bismuth metal: iridescent oxide coating → rainbow surface (step terracing + thin film interference)

APPLICATIONS:
  Pepto-Bismol: bismuth subsalicylate (BSS) — treats nausea, indigestion, traveler's diarrhea
    Mechanism: Bi³⁺ has antimicrobial activity (precipitates bacterial proteins)
    + salicylate anti-inflammatory + antidiarrheal effect
  H. pylori treatment: bismuth quadruple therapy (Bi + metronidazole + tetracycline + PPI)
  Lead-free solders: Bi-In, Bi-Sn low-melting alloys (Wood's metal: Bi-Pb-Sn-Cd, mp 70°C)
  Fusible alloys: sprinkler heads, fire safety systems (low-mp Bi alloys)
  BiFeO₃: multiferroic (simultaneous ferroelectric + antiferromagnetic) → data storage research
  Bi₂Te₃: thermoelectric (see Te above)
  Oncology: Bi-213 α-emitter for targeted alpha therapy (Bi-DOTA-peptide conjugates)
```

---

## Decision Cheat Sheet

| Application | Element | Why |
|-------------|---------|-----|
| Semiconductor foundation | Si | Band gap 1.12 eV, purity controllable, SiO₂ gate oxide |
| IR optics / night vision | Ge | Transparent 2–16 μm, high refractive index |
| High-frequency RF transistors | GaAs (As) | High electron mobility, direct band gap |
| CdTe or CIGS solar cells | Te or Se | Thin-film PV materials |
| Thermal neutron absorption | B | ¹⁰B cross-section 3840 barns |
| Lead-free solder | Sn | SAC alloys (Sn-Ag-Cu) replace Sn-Pb |
| Lead-acid battery | Pb | Cheap, high current, recyclable |
| Radiation shielding | Pb | High Z + density = best γ attenuation per cost |
| Stomach remedy / H. pylori | Bi | BSS, non-toxic Bi³⁺ antimicrobial |
| Antistatic device | Po (or Am) | α ionizes air → discharges static |

---

## Common Confusion Points

**"Why is aluminum so cheap when it's so hard to extract?"**
Because it was expensive until Hall and Héroult independently invented electrolysis of Al₂O₃ in
molten cryolite in 1886. Before that, it cost more than gold (Napoleon served it to honored guests
on aluminum plates, regular guests got gold plates). The Hall-Héroult process requires massive
cheap electricity, which is why smelters are near hydroelectric dams (Iceland, Norway, PNW).

**"GaAs vs Si — why doesn't everything switch to GaAs?"**
GaAs has 6× higher electron mobility and a direct band gap (Si is indirect → poor light emission).
But: GaAs substrates are expensive and fragile (brittle), no native oxide for MOSFET gate,
wafer sizes are smaller, and Si manufacturing infrastructure is incomparably mature. GaAs wins
where performance dominates (RF, LEDs, solar) but Si wins everywhere else on cost/scale.

**"What's the difference between a metalloid and a semiconductor?"**
Metalloid is a chemical classification (location near the staircase, intermediate properties).
Semiconductor is a physical classification (band gap 0–3 eV, conductivity tunable by doping).
All elemental metalloids are semiconductors, but many semiconductors are not metalloids
(GaAs, InP, CdTe are compounds; diamond C is classified as a nonmetal but is a semiconductor).
