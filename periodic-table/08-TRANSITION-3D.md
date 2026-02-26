# 3d Transition Metals — Sc, Ti, V, Cr, Mn, Fe, Co, Ni, Cu, Zn

## The Big Picture

The first-row transition metals (Period 4, Groups 3–12) are where d-orbital chemistry comes alive:
variable oxidation states, colored compounds, catalytic activity, and the metals that built civilization.

```
3d TRANSITION METALS — ELECTRON CONFIGURATIONS

  Z   Symbol   Config                d electrons  Common ox. states
  ────────────────────────────────────────────────────────────────────
  21  Sc       [Ar] 3d¹ 4s²          1           +3 (only)
  22  Ti       [Ar] 3d² 4s²          2           +4, +3
  23  V        [Ar] 3d³ 4s²          3           +5, +4, +3, +2
  24  Cr       [Ar] 3d⁵ 4s¹ *        5           +6, +3, +2
  25  Mn       [Ar] 3d⁵ 4s²          5           +7, +4, +3, +2
  26  Fe       [Ar] 3d⁶ 4s²          6           +3, +2
  27  Co       [Ar] 3d⁷ 4s²          7           +3, +2
  28  Ni       [Ar] 3d⁸ 4s²          8           +2
  29  Cu       [Ar] 3d¹⁰ 4s¹ *      10           +2, +1
  30  Zn       [Ar] 3d¹⁰ 4s²        10           +2 (only)

  * Exceptions to Aufbau: Cr and Cu both steal one 4s electron to fill/half-fill 3d
    (3d⁵ half-filled + 4s¹ for Cr; 3d¹⁰ full + 4s¹ for Cu — extra stability)

TRANSITION METAL DEFINITION:
  Strict (IUPAC): has incomplete d subshell in element OR common ions
  → Zn is borderline: Zn⁰ and Zn²⁺ both have d¹⁰ → sometimes excluded
  → Sc is borderline: Sc³⁺ has d⁰ → sometimes excluded
```

---

## Why d Orbitals Change Everything

```
d-ORBITAL SET IN AN OCTAHEDRAL FIELD (Crystal Field Theory):

  Free ion: 5 d orbitals degenerate (same energy)
  Octahedral ligand field: splits into two sets

  ENERGY:
      ╔═══════════════════════════╗     eg set: dx²-y², dz² (higher, point at ligands)
      ║    eg  (+0.6 Δoct)       ║
      ╠══════════════════╦════════╣
      ║   Δoct           ║        ║
      ║ (crystal field   ║ t2g set: dxy, dxz, dyz (lower, point between ligands)
      ║  splitting)      ║        ║
      ╚══════════════════╩════════╝     t2g (-0.4 Δoct)

  Δoct depends on:
    • Metal (higher Z, higher row → larger Δ)
    • Ligand: spectrochemical series (I⁻ < Br⁻ < Cl⁻ < F⁻ < OH⁻ < H₂O < NH₃ < CN⁻ < CO)
              "weak field" ← ───────────────────────────────────────────────── → "strong field"

  CONSEQUENCES:
    Color: d-d transitions absorb visible light → complementary color observed
    Magnetism: high-spin (weak field, electrons in eg) vs low-spin (strong field, all in t2g)
    CFSE: crystal field stabilization energy → affects thermodynamics, kinetics

COLOR TABLE (aquo complexes):
  Ti³⁺: purple/violet (1 d electron, d-d transition)
  V³⁺:  green
  Cr³⁺: blue-green/violet
  Mn²⁺: very pale pink (d⁵ high-spin, transitions spin-forbidden → nearly colorless)
  Fe³⁺: pale yellow (d⁵ high-spin — spin-forbidden transitions)
  Fe²⁺: pale green
  Co²⁺: pink
  Ni²⁺: green
  Cu²⁺: blue
  Zn²⁺: colorless (d¹⁰ — no d-d transitions possible)
```

---

**From d-d transitions to UV-Vis spectrophotometry:** The colors in the table above are directly measurable by UV-Vis absorption spectrophotometry — the analytical instrument that reads out the wavelength and extinction coefficient (ε, L/mol·cm) of each transition. Beer-Lambert law: A = εcl, where A = absorbance, c = concentration, l = path length. A solution of Cu²⁺ (blue, absorbs ~600–700 nm orange-red) with known ε can have its concentration read directly from the absorbance at the peak wavelength. This is how clinical labs measure hemoglobin (Soret band at 415 nm), how wastewater treatment monitors Cr⁶⁺ contamination (Cr₂O₇²⁻ absorbs at 350 nm), and how plate reader assays in pharmaceutical labs quantify enzyme activity. Ligand field splitting (Δ_oct) is the variable that shifts the absorption peak — which is why the same Cu²⁺ ion looks different colors in different solvent/ligand environments (blue in water, deep blue in ammonia as Cu(NH₃)₄²⁺, colorless in anhydrous organic solvents).

## Iron (Fe, Z=26) — The Metal That Built Civilization

### Iron Metallurgy

```
IRON ABUNDANCE:
  4th most abundant element in Earth's crust (5.6%)
  Most abundant element in Earth overall (core is mostly iron)

BLAST FURNACE (primary steel production):
  Raw materials: iron ore (Fe₂O₃, Fe₃O₄), coke (C), limestone (CaCO₃)

  REACTIONS (schematic):
  Zone 1 (top, 200-700°C):  C + O₂ → CO₂, then CO₂ + C → 2CO
  Zone 2 (mid, 700-1000°C): Fe₂O₃ + 3CO → 2Fe + 3CO₂
  Zone 3 (hot, >1200°C):    FeO + CO → Fe + CO₂ (final reduction)
  Slag:                      CaCO₃ → CaO + CO₂; CaO + SiO₂ → CaSiO₃ (liquid slag)

  Product: pig iron (~4% C, plus Si, Mn, P, S) — brittle due to high C

STEELMAKING (BOF — Basic Oxygen Furnace):
  Pig iron → BOF → oxygen blown in → burns off excess C
  [C] 4% → target 0.1-2% (steel composition determines properties):
    Low C (<0.2%): mild steel — structural, cheap, weldable
    Medium C (0.2-0.6%): stronger, less weldable
    High C (0.6-1.5%): tool steel, hardened by heat treatment
    Cast iron (>2%): brittle but cheap and castable

ALLOY STEELS:
  Stainless (316L): 16-18% Cr, 10-14% Ni, 2-3% Mo → corrosion resistant
  Tool steel (HSS): W, Mo, V, Co → red hardness (maintains hardness at high T)
  TRIP/TWIP steel: automotive — advanced high-strength for crash safety
  Electrical steel: 3% Si → higher resistivity → reduced eddy current losses in transformers
```

### Iron in Biology — Hemoglobin and Beyond

```
HEMOGLOBIN:
  4 subunits (2α + 2β), each with one heme group
  Heme: iron-porphyrin complex (Fe²⁺ in center of protoporphyrin IX ring)
  Fe²⁺ coordinates: 4 N from porphyrin + 1 N from histidine (His F8) + O₂ binding site

  O₂ BINDING COOPERATIVITY (T/R state model):
    Deoxygenated (T state): low O₂ affinity, tense quaternary structure
    First O₂ binds → conformational shift → R state → higher affinity
    Sigmoidal binding curve (Hill coefficient ~2.8) vs simple hyperbola

  CARBON MONOXIDE (CO) TOXICITY:
    CO binds Fe²⁺ with 250× higher affinity than O₂
    → HbCO → prevents O₂ transport → tissue hypoxia
    Also binds cytochrome c oxidase (Complex IV) → blocks mitochondrial respiration
    Treatment: 100% O₂ (mass action) → t½(HbCO) drops from 5hr to 1hr

MYOGLOBIN:
  Single subunit (1 heme), O₂ storage in muscle
  Higher O₂ affinity than Hb → accepts O₂ from Hb in capillaries
  Hyperbolic binding curve (Hill = 1, no cooperativity — single subunit)

IRON STORAGE AND TRANSPORT:
  Ferritin: hollow protein cage (24 subunits), stores ~4500 Fe³⁺ as ferrihydrite
  Transferrin: blood transport protein, 2 Fe³⁺ binding sites
  Hemosiderin: insoluble Fe storage aggregate (iron overload)
  Fe deficiency: most common nutritional deficiency globally (anemia, impaired O₂ transport)
  Fe overload (hemochromatosis): organ damage (liver, heart, pancreas) from Fe free radical damage

FENTON CHEMISTRY:
  Fe²⁺ + H₂O₂ → Fe³⁺ + OH• + OH⁻  (Fenton reaction)
  Hydroxyl radical (OH•) is the most reactive oxidant in biology
  → DNA strand breaks, lipid peroxidation, protein oxidation
  Why cells sequester Fe in ferritin: prevent free Fe²⁺ from generating OH•
  Why antioxidants matter: scavenge OH• before damage
```

---

## Copper (Cu, Z=29)

### Electrical Conductor of Choice

```
Cu ELECTRICAL PROPERTIES:
  Resistivity: 1.68 μΩ·cm (second lowest metal after Ag at 1.59)
  Ag is 6% better conductor but costs ~70× more per kg → Cu wins for almost everything

  COMPARISON TABLE:
  Metal    Resistivity   Density   Cost     Use case
           (μΩ·cm)       (g/cm³)   (relative)
  Ag       1.59          10.5      $$$$     High-frequency PCB, solar cell contacts
  Cu       1.68           8.9      $$       General wiring, motors, transformers
  Au       2.44          19.3      $$$$$    Semiconductor wire bonding, connectors
  Al       2.82           2.7      $        High-voltage transmission lines (lighter per km)
  W        5.6           19.3      $$       Filaments (high-temp), semiconductor gate contact
  Fe       10.1           7.9      $        Structural, not for conductivity

ANNEALING AND WORK HARDENING:
  Cu work-hardens quickly → needs intermediate annealing during wire drawing
  Oxygen-free high-conductivity (OFHC) copper: <5 ppm O → prevents hydrogen embrittlement
  Electrodeposited Cu: semiconductor back-end (Damascene process, Cu lines in Si chip)
    Introduced in 1997 (IBM) replacing aluminum → 30% lower resistivity → faster chips
```

### Copper in Biology

```
COPPER PROTEINS:
  Type 1 (blue): intense blue color (d-d + charge transfer) → single Cu, electron transfer
    → plastocyanin (photosynthesis), azurin, laccase
  Type 2 (normal): colorless, O₂ activation
    → cytochrome c oxidase (Complex IV — 2 Cu centers: CuA and CuB)
    → dopamine β-hydroxylase (norepinephrine synthesis — requires Cu)
  Multicopper oxidases: 4 Cu, 4-electron O₂ reduction → ceruloplasmin (plasma ferroxidase)

CYTOCHROME c OXIDASE:
  Reduces O₂ to H₂O using 4 electrons from cytochrome c
  Pumps protons across mitochondrial inner membrane → contributes ~40% of proton gradient
  4 Cu (CuA binuclear site receives electrons; CuB with heme a3 binds and reduces O₂)

Wilson's disease: autosomal recessive, ATPA7B mutation → Cu accumulates in liver/brain/eyes
  Kayser-Fleischer rings (Cu deposits in cornea), liver cirrhosis, neurological symptoms
  Treatment: D-penicillamine (chelates Cu for excretion) or zinc (blocks absorption)

Menkes disease: X-linked, ATP7A mutation → Cu malabsorption → Cu deficiency
  Connective tissue defects (lysyl oxidase needs Cu for collagen/elastin crosslinking)
```

### Copper Alloys and Corrosion

```
ALLOYS:
  Brass (Cu-Zn): 30% Zn common; gold-colored; used in plumbing fittings, musical instruments
  Bronze (Cu-Sn): 10% Sn typical; harder than brass; bearings, sculpture, marine propellers
  Cupronickel (Cu-Ni): corrosion-resistant; US "silver" coins (75% Cu / 25% Ni),
                        marine condensers, heat exchangers

PATINA:
  Cu → Cu₂O (red, matte) → CuO (black) → Cu₂CO₃(OH)₂ (green verdigris) over years
  The green is basic copper carbonate — stable, protective
  Statue of Liberty: ~80 tonnes Cu, green by 1900 (~20 years after completion)

ANTIMICROBIAL COPPER:
  Cu surfaces kill bacteria within hours (Cu ions disrupt bacterial membranes, enzymes)
  EPA registered antimicrobial: alloys >60% Cu qualify
  Hospital trials: Cu surfaces in ICU → reduced HAI (hospital-acquired infection) rates
```

---

## Chromium (Cr, Z=24)

```
OXIDATION STATES:
  Cr(II): Cr²⁺ (reducing), blue-violet solutions
  Cr(III): Cr³⁺ (stable, green) — insoluble in water, low toxicity, essential micronutrient
  Cr(VI): CrO₄²⁻ (chromate, yellow) and Cr₂O₇²⁻ (dichromate, orange-red) — CARCINOGEN

STAINLESS STEEL:
  Cr ≥ 10.5% → thin Cr₂O₃ passive layer → stainless
  304 (18-8): 18% Cr + 8% Ni → most common, kitchen equipment
  316 (18-10-2): + 2% Mo → chloride resistance → marine, pharmaceutical
  Ferritic (430): 17% Cr, no Ni → magnetic, cheaper, cutlery
  Martensitic (410): 12% Cr, higher C → hard, knife blades

CHROME TANNING (leather):
  Cr(III) sulfate cross-links collagen chains → flexible, durable leather
  ~80% of global leather tanned with Cr(III) — safe
  Cr(VI) is the carcinogen — requires strict wastewater control in tanneries

CHROMATE CONVERSION COATING:
  Alodine/Iridite: Cr(VI) treatment on Al/Mg → corrosion protection + paint adhesion
  Now transitioning to Cr(III) coatings (REACH regulation in EU)

HEXAVALENT CHROMIUM TOXICITY:
  Cr(VI) easily crosses cell membranes → reduced intracellularly to Cr(III) + reactive intermediates
  → DNA damage, lung cancer (occupational: chrome platers, ferrochrome workers)
  Erin Brockovich case: Pacific Gas & Electric contaminated groundwater with Cr(VI) at Hinkley, CA
  → 1996 settlement $333M — largest class action in US history at that time
```

---

## Manganese (Mn, Z=25)

```
OXIDATION STATES (full range: +2 to +7):
  Mn²⁺: pale pink, most stable in solution; d⁵ high-spin → almost colorless (spin-forbidden)
  Mn³⁺: violet; oxidizing; Jahn-Teller distorted
  MnO₂ (Mn⁴⁺): black solid; primary cathode material in dry cells and alkaline batteries
  Mn₂O₇ (Mn⁷⁺): green liquid, explosive — extreme oxidizer
  MnO₄⁻ (permanganate, Mn⁷⁺): intense purple; strong oxidant; water treatment, disinfection,
                                 organic synthesis (KMnO₄ oxidizes alkenes, alkynes)

BATTERIES:
  Alkaline (primary): MnO₂ cathode + Zn anode + KOH electrolyte
    MnO₂ + H₂O + e⁻ → MnOOH + OH⁻ (cathode)
    Zn + 2OH⁻ → ZnO + H₂O + 2e⁻ (anode)
    ~7 billion alkaline cells per year (AA, AAA, etc.)

  Li-Mn-O (LMO, LiMn₂O₄): spinel structure, Li-ion battery cathode
    Safe (no Co), but moderate energy density and cycle life

STEEL ALLOYING:
  Mn removes oxygen and sulfur (forms MnO and MnS slag → floats off)
  Work hardening steel (Hadfield steel): 12-14% Mn → extreme toughness, self-hardens on impact
  Used in: railroad switches, rock crushers, military armor

BIOLOGICAL ROLE:
  Manganese superoxide dismutase (MnSOD): in mitochondrial matrix
  Mn₄CaO₅ cluster in Photosystem II: splits water (2H₂O → O₂ + 4H⁺ + 4e⁻)
  Most Mn in mitochondria; neurological damage from overexposure (manganism ≈ Parkinson's-like)
```

---

## Cobalt (Co, Z=27)

```
[Ar] 3d⁷ 4s²  — common ox. states: +2, +3

VITAMIN B₁₂ (cobalamin):
  Only vitamin containing a metal
  Co³⁺ at center of corrin ring (like porphyrin but smaller)
  Two biologically active forms:
    Adenosylcobalamin: cofactor for mutase reactions (isomerization)
    Methylcobalamin: methyl group donor (homocysteine → methionine)
  Deficiency: megaloblastic anemia, peripheral neuropathy, subacute combined degeneration
  Sources: exclusively animal products → vegans must supplement
  Intrinsic factor (gastric glycoprotein) required for absorption → pernicious anemia if absent

COBALT BLUE:
  CoAl₂O₄ (cobalt aluminate) — intense stable blue pigment
  Used since ancient Egypt (cobalt silicate blue frit)
  Remarkably stable to heat and UV → fine art, ceramics, glass

ALNICO MAGNETS:
  Al-Ni-Co alloy → permanent magnets (before rare earth magnets)
  Alnico 5: 51% Fe + 24% Co + 14% Ni + 8% Al + 3% Cu
  Used in: guitar pickups, microphones, speakers, motors
  Now largely replaced by NdFeB (stronger) but still used for high-T applications

COBALT IN SUPERALLOYS:
  Co-based superalloys (Haynes 188, L-605): cobalt with Cr, W, Ni
  Maintain strength at temperatures where Ni superalloys start to soften (~1000°C+)
  Aerospace hot section components, medical implants (CoCrMo)

COBALT-60:
  ⁶⁰Co: t½ = 5.27 yr, β⁻ + γ (1.17 + 1.33 MeV)
  Radiation therapy: teletherapy units (replacing Ra), food irradiation, industrial radiography
  Produced: ⁵⁹Co + n → ⁶⁰Co in reactor
```

---

## Nickel (Ni, Z=28)

```
[Ar] 3d⁸ 4s²  — common ox. state: +2

CATALYTIC HYDROGENATION:
  Ni Raney (Ni-Al alloy leached with NaOH → spongy Ni) — heterogeneous hydrogenation catalyst
  R-CH=CH₂ + H₂ → R-CH₂-CH₃  (alkene saturation)
  Food: vegetable oil + H₂ → margarine (partially hydrogenated → trans fats, now restricted)
  Industrial: petroleum refining, NH₃ synthesis (though Fe is standard for Haber-Bosch)

STAINLESS STEEL:
  Austenitic (304, 316): Ni stabilizes austenite (FCC) phase to room temperature
  Ni-base superalloys (Inconel, Hastelloy, Waspaloy): turbine blades
    IN718: ~54% Ni + Cr + Mo + Nb; precipitation hardened by Ni₃Nb (γ'' phase)
    Operates at 90% of its own melting point (with thermal barrier coatings)

Ni-Cd BATTERIES (NiCad):
  Cd anode, NiOOH cathode, KOH electrolyte
  Memory effect (partial discharge → capacity loss) → superseded by NiMH then Li-ion
  Cd toxicity → restricted use (power tools, emergency lighting remain)

Ni-MH BATTERIES:
  Metal hydride (LaNi₅H₆) anode, NiOOH cathode
  Hybrid vehicles (Toyota Prius pre-2010 used large NiMH packs)
  Still used in HEV and power tools

CARBONYL PROCESS (Mond process, nickel refining):
  Ni + 4 CO → Ni(CO)₄ (colorless liquid, bp 43°C, EXTREMELY TOXIC) → distill → Ni + 4CO
  High-purity nickel without electrolysis; also used for nickel plating
```

---

## Zinc (Zn, Z=30) — Most Versatile Enzyme Cofactor

```
[Ar] 3d¹⁰ 4s²  — only +2 oxidation state (d¹⁰, no d-d transitions → colorless)
"Post-transition metal" by strict IUPAC definition but universally discussed here

ZINC IN ENZYMES (>300 enzymes in human body):
  Structural Zn: stabilizes protein fold (zinc finger proteins → transcription factors, DNA binding)
  Catalytic Zn: Lewis acid at active site (activates water or substrates)

KEY ENZYMES:
  Carbonic anhydrase: CO₂ + H₂O ⇌ HCO₃⁻ + H⁺ (Zn activates water)
    Rate: 10⁶ s⁻¹ (among fastest enzymes)
    Function: CO₂ transport from tissues to lungs; gastric acid secretion; pH regulation
  Carboxypeptidase: digest proteins from C-terminus (Zn activates substrate)
  Alcohol dehydrogenase: metabolizes ethanol (Zn coordinates substrate + NAD⁺)
  Matrix metalloproteinases: Zn-dependent, degrade ECM in wound healing, cancer invasion
  RNA polymerase, DNA polymerase: structural Zn fingers

ZINC FINGER PROTEINS:
  Cys₂His₂ motif: 2 Cys + 2 His coordinate one Zn²⁺
  Fold stabilized by Zn → small domain that inserts α-helix into DNA major groove
  ~3% of human genome encodes zinc finger proteins
  Zinc finger nucleases (ZFNs): engineered → gene editing (before CRISPR)

GALVANIZING:
  Hot-dip galvanizing: steel dipped in molten Zn → Zn-Fe alloy layers + pure Zn top
  Electrogalvanizing: electrodeposition → thinner, more uniform
  Zn protects steel two ways: (1) physical barrier, (2) sacrificial anode (Zn is more reactive)
  Galvanized steel lasts 50-70+ years in typical exposure vs untreated steel (~10 yr)

ZnO (zinc oxide):
  White powder, wide band gap (3.37 eV, direct) → UV absorber
  Sunscreen (physical blocker — reflects/scatters UV, no skin penetration)
  Semiconductor: piezoelectric, photocatalytic, nanowire arrays
  Rubber vulcanization: ZnO + stearic acid → zinc stearate activates sulfur crosslinking
  Ceramics, paints, pharmaceuticals (zinc cream for diaper rash)
```

---

**Note on coverage order:** This guide covers Fe, Co, Ni, Cu, Zn in depth first (industrial/biological significance), then circles back to the early transition metals. Scandium and Titanium (Z=21-22) follow here; Vanadium (Z=23) and Chromium/Manganese (Z=24-25) are covered in their own sections below to give each its due weight.

## Scandium (Sc, Z=21) and Titanium (Ti, Z=22)

```
SCANDIUM:
  [Ar] 3d¹ 4s²  → Sc³⁺ only (d⁰ — no d-d transitions, no color)
  Rare: 22 ppm in crust but very dispersed (no rich ore deposits)
  Sc₂O₃ additive in Al alloys: Al-Mg-Sc alloys → fine grain size → high strength
    Used in baseball bats, bicycle frames, Russian MiG-29 airframe
  Sc-Na lamps: ScI₃ + NaI in Hg arc → excellent white light (Color Rendering Index ~90)

TITANIUM:
  [Ar] 3d² 4s²  → +4 (TiO₂ most common), also +3
  Density: 4.5 g/cm³ | Strength-to-weight: best of any structural metal
  Corrosion resistance: exceptional (TiO₂ passivation layer even in seawater, HCl, body fluids)

  AEROSPACE:
    Ti-6Al-4V (Grade 5): workhorse alloy (6% Al + 4% V)
    Heat shields, compressor blades, airframe (777 is ~8% Ti by weight)
    SR-71 Blackbird: ~93% Ti — withstands aerodynamic heating at Mach 3.2

  BIOMEDICAL:
    Ti implants: bone screws, hip/knee replacements, dental implants
    Osseointegration: TiO₂ surface → bone cells adhere → implant integrates with bone
    No ion release → no immune response → ideal long-term implant

  TiO₂ PIGMENT:
    ~5 million tonnes/yr — most widely used white pigment
    High refractive index (2.7 rutile vs ~1.5 for most white solids) → high opacity
    Paint, paper, plastics, sunscreen, food coloring (E171 — regulatory review ongoing)
    Photocatalyst: UV + TiO₂ → •OH radicals → oxidize organics → self-cleaning surfaces
```

---

## Vanadium (V, Z=23)

```
[Ar] 3d³ 4s²  → multiple stable oxidation states: +5 (yellow), +4 (blue), +3 (green), +2 (violet)

VANADIUM REDOX FLOW BATTERY:
  All-vanadium design (Skyllas-Kazacos, 1986):
  Anolyte: V²⁺/V³⁺  |  Catholyte: VO²⁺/VO₂⁺ (V⁴⁺/V⁵⁺)
  Same element on both sides → no cross-contamination → infinite cycle life
  Storage scales independently from power (tank size vs cell stack)
  Grid-scale storage for renewable integration (GW·h deployments in China)

V₂O₅ IN CONTACT PROCESS:
  V₂O₅ catalyst oxidizes SO₂ → SO₃ (Ostwald/contact process for H₂SO₄)
  Cycle: V⁵⁺ + SO₂ → V⁴⁺ + SO₃; V⁴⁺ + ½O₂ → V⁵⁺ (catalyst regenerated)

STEEL MICROALLOYING:
  0.1-0.2% V in steel → VC/V(N,C) precipitates → fine grain → high-strength low-alloy (HSLA)
  Used in: high-strength structural steel, pipelines, automotive
```

---

## Decision Cheat Sheet

| Application | Metal | Key property |
|-------------|-------|--------------|
| Structural steel | Fe | Cheap, strong, alloyed |
| Stainless steel | Fe + Cr (+Ni) | Cr₂O₃ passivation |
| Electrical wiring | Cu | Low resistivity, cost |
| Aerospace structure | Ti | Strength/weight, corrosion |
| Biomedical implants | Ti (or CoCrMo) | Osseointegration, bioinert |
| Enzyme cofactor (widest) | Zn | 300+ enzymes, zinc fingers |
| O₂ transport (blood) | Fe (heme) | Hemoglobin Fe²⁺ |
| Vitamin B₁₂ | Co | Corrin-Co³⁺ |
| Grid-scale flow battery | V | Vanadium redox both sides |
| White pigment | Ti (TiO₂) | High refractive index |
| Permanent magnets (classic) | Co (Alnico) | Before rare earth era |
| Catalytic hydrogenation | Ni (Raney) | Heterogeneous surface |

---

## Common Confusion Points

**"Cr(III) vs Cr(VI) — same element, wildly different toxicity. Why?"**
Cr(VI) as chromate (CrO₄²⁻) is isoelectronic with sulfate → enters cells via sulfate transporters.
Once inside, it's reduced to Cr(III) — generating reactive Cr(IV)/Cr(V) intermediates and
reactive oxygen species that damage DNA. Cr(III) by itself cannot enter cells readily and is
essentially non-toxic at dietary levels (may even be a micronutrient for insulin signaling).
This is a rare case where chemistry inside the cell is what matters, not the initial species.

**"Why does Fe²⁺ (not Fe³⁺) bind O₂ in hemoglobin, but form rust (Fe₂O₃) in air?"**
In hemoglobin, the protein environment carefully controls the Fe oxidation state.
The proximal histidine (His F8) donates electron density; the distal histidine (His E7) controls
access and prevents O₂ from fully oxidizing Fe²⁺ to Fe³⁺ (methemoglobin, which can't bind O₂).
In air, Fe²⁺ in simple solution is freely oxidized → Fe³⁺ → rust. Proteins create a microenvironment
that stabilizes the Fe²⁺–O₂ complex.

**"Zinc has a full d shell — why is it called a transition metal?"**
It's often not, strictly speaking (IUPAC defines transition metals as having incomplete d subshells).
But Zn is almost universally discussed in the same context — same row, same industrial/biological
relevance, similar coordination chemistry. The distinction is definitional, not chemical. Same
debate applies to Sc (d⁰ in +3 state) and the Group 12 metals (Zn, Cd, Hg).
