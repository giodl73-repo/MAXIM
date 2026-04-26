# The Life Nonmetals — C, N, O, P, S

## The Big Picture

Five elements from the p-block define biochemistry. Carbon provides the backbone,
nitrogen gives functional identity, oxygen drives energy transfer, phosphorus stores
and signals energy, sulfur provides structure and catalysis.

```
CHNOPS minus H (covered in 01-HYDROGEN.md):

  Element   Z   Config      EN    bp(°C)  State@STP  Abundance in crust  Human body (% mass)
  ─────────────────────────────────────────────────────────────────────────────────────────────
  Carbon    6   [He]2p²    2.55  −subli.  solid      200 ppm              18.5%
  Nitrogen  7   [He]2p³    3.04  −196    gas (N₂)    60 ppm (atm: 78%)     3.3%
  Oxygen    8   [He]2p⁴    3.44   −183    gas (O₂)    46% (most abundant)  65%
  Phosphorus 15 [Ne]3p³    2.19  +280(red) solid      1050 ppm             1.1%
  Sulfur    16  [Ne]3p⁴    2.58  +445     solid       340 ppm              0.25%

Together these 5 elements make up >96% of living cell mass (by atom count, even more).
```

---

## Carbon (C, Z=6) — The Framework Element

### Allotropes

```
ALLOTROPES OF CARBON:
  ┌─────────────────────────────────────────────────────────────────────────┐
  │  DIAMOND              GRAPHITE             GRAPHENE                     │
  │  ─────────────        ─────────────        ────────                     │
  │  sp³, tetrahedral     sp², layered         sp², monolayer               │
  │  3D covalent network  hexagonal planes      2D crystal                  │
  │  Hardest natural      Planes slide on       Strongest material known    │
  │  material (10 Mohs)   each other (0.01 μm)  per unit thickness        │
  │  Electrical insulator Electrical conductor  Semi-metal (zero-gap)     │
  │  Best thermal cond.   Lubricant, electrode  Thermal cond. ~5000 W/mK  │
  │  3 × silicon in heat                        Quantum Hall effect at RT │
  │                                                                         │
  │  FULLERENES                    CARBON NANOTUBES (CNTs)                  │
  │  ─────────────                 ────────────────────────                 │
  │  C₆₀ (buckminsterfullerene)    Single-wall (SWCNT): graphene rolled     │
  │  sp² carbon in cage            Multi-wall (MWCNT): nested tubes         │
  │  C₆₀ = 20 hexagons +          Tensile strength: ~100× steel           │
  │         12 pentagons (soccer ball)  Ballistic conductors (armchair)   │
  │  Superconducting when doped    Field emission displays, composites      │
  │  (K₃C₆₀: Tc = 18 K)                                                   │
  │                                                                         │
  │  AMORPHOUS CARBON                  DIAMOND-LIKE CARBON (DLC)            │
  │  Coal, charcoal, coke              Mixed sp²/sp³; hard, amorphous     │
  │  Active carbon: high surface area  Hard coatings (cutting tools,      │
  │  (~1000 m²/g) → adsorption, filter  razor blades, automotive)         │
  └─────────────────────────────────────────────────────────────────────────┘

Phase diagram: at normal pressure, diamond → graphite spontaneously (ΔG < 0)
but rate is negligible at room temperature (kinetically trapped)
High P (~5 GPa) + high T: graphite → diamond (industrial synthesis)
CVD diamond: carbon vapor deposited → thin film or thick poly-crystal diamond
```

### Organic Chemistry Gateway

```
CARBON'S UNIQUE POSITION:
  • 4 valence electrons → forms 4 bonds (tetravalent)
  • C–C single bond: 346 kJ/mol (strong enough to be stable)
  • C=C double bond: 614 kJ/mol
  • C≡C triple bond: 839 kJ/mol
  • Small size → bonds are short → ring strain possible but manageable
  • Mid-range EN (2.55) → forms polar and nonpolar bonds readily

These properties → essentially unlimited structural diversity.
Number of known organic compounds: ~100 million+ (CAS registry).

Functional groups (quick index):
  –OH (alcohol/phenol), –COOH (carboxylic acid), –NH₂ (amine), –C=O (aldehyde/ketone)
  –COO– (ester), –CONH– (amide), –SH (thiol), –S–S– (disulfide), –Ph (phenyl)
  See natural-sciences/17-ORGANIC-CHEMISTRY.md for full treatment.
```

### CO₂ and the Carbon Cycle

```
CO₂ CHEMISTRY:
  Molecular structure: O=C=O  (linear, sp hybrid on C, no dipole despite polar bonds)
  Dissolves in water: CO₂ + H₂O ⇌ H₂CO₃ ⇌ H⁺ + HCO₃⁻ ⇌ H⁺ + CO₃²⁻
    pKa₁ = 6.35, pKa₂ = 10.33
  Ocean acidification: absorbed CO₂ → carbonic acid → lower pH → dissolves CaCO₃ shells

CARBONATE SYSTEM:
  CaCO₃ (limestone) + CO₂ + H₂O ⇌ Ca²⁺ + 2 HCO₃⁻
  (karst caves, coral dissolution, marine chemistry)

SUPERCRITICAL CO₂ (scCO₂):
  Tc = 31.1°C, Pc = 73.8 atm → easily achievable
  Acts as a solvent: "green" extraction of caffeine (supercritical decaffeination),
  hop extraction, perfumes, dry cleaning alternative
  Carbon capture and storage (CCS): liquid/scCO₂ injected into geological formations
```

---

## Nitrogen (N, Z=7) — The Stubborn Triple Bond

### The Nitrogen Problem

```
N₂ STABILITY:
  N≡N triple bond energy: 945 kJ/mol (most stable homonuclear diatomic after CO)
  Bond dissociation requires ~3000 K in the absence of catalysts
  → atmospheric N₂ is essentially biologically inert (despite being 78% of air)

CONSEQUENCE:
  Life needs fixed nitrogen (NH₃, NO₃⁻, amino groups) but N₂ is unavailable.
  Before Haber-Bosch: available fixed N from guano (bird/bat droppings), Chile saltpeter
  (NaNO₃), and biological nitrogen fixation.

BIOLOGICAL NITROGEN FIXATION:
  N₂ + 8H⁺ + 8e⁻ + 16 ATP → 2 NH₃ + H₂ + 16 ADP + 16 Pi  (nitrogenase enzyme)
  Enzyme: Mo-Fe nitrogenase (most common); also V-Fe and Fe-only nitrogenase
  Organisms: Rhizobium (root nodules of legumes), Azotobacter (free-living), cyanobacteria
  Problem: O₂ irreversibly destroys nitrogenase → legume nodules maintain micro-anaerobic zone

NITROGEN CYCLE:
  N₂ → NH₃ (fixation: biological or Haber-Bosch)
  NH₃ → NO₂⁻ → NO₃⁻ (nitrification: Nitrosomonas → Nitrobacter)
  NO₃⁻ → N₂ (denitrification: Pseudomonas in anaerobic soils)
  Organic N → NH₄⁺ (ammonification)
```

### Haber-Bosch — World-Changing Reaction

```
THE HABER-BOSCH PROCESS:
  N₂ + 3 H₂ ⇌ 2 NH₃    ΔH = −92 kJ/mol (exothermic)

  THERMODYNAMICS vs KINETICS:
    Low T → favors NH₃ (Le Chatelier: exothermic + decreasing moles of gas)
    Low T → too slow for industrial production (activation energy ~240 kJ/mol)
    Compromise: 400–500°C, 150–300 atm, Fe catalyst (with K₂O and Al₂O₃ promoters)
    Conversion: only ~15-25% per pass → unreacted gases recycled

  CATALYST MECHANISM:
    Rate-limiting step: N₂ adsorption and dissociation on Fe surface
    K₂O (electronic promoter): increases electron density on Fe → better N₂ binding
    Al₂O₃ (structural promoter): prevents Fe sintering at high T

  SCALE AND IMPACT:
    ~180 million tonnes NH₃/yr (2024) — second most produced industrial chemical after H₂SO₄
    ~80% → fertilizers (ammonium nitrate, urea, ammonium phosphate)
    Estimated: ~50% of nitrogen atoms in current human bodies came through Haber-Bosch
    Fritz Haber: Nobel 1918, also developed chemical warfare agents (Cl₂, phosgene)
    Karl Bosch: Nobel 1931 (high-pressure industrial chemistry)
```

### NOₓ and Other N Chemistry

```
NITROGEN OXIDES (NOₓ):
  NO:  colorless gas, unstable (reacts with O₂ → NO₂), biological signaling molecule
       Endothelium-derived relaxing factor → vasodilation → nitrates for angina
       Nitrogen monoxide in combustion → smog precursor
  NO₂: brown gas (paramagnetic), acid rain precursor, lung irritant
       2 NO₂ + H₂O → HNO₃ + HNO₂ (part of acid rain chemistry)
  N₂O: "laughing gas" — anesthetic, dental use, also potent GHG (265× CO₂ over 100yr)
       Agricultural N₂O from soil denitrification — major climate concern

NITRIC ACID (HNO₃):
  Made by Ostwald Process: 4 NH₃ + 5 O₂ → 4 NO + 6 H₂O  (Pt/Rh catalyst)
  Then: 4 NO + 3 O₂ + 2 H₂O → 4 HNO₃ (final acid)
  Uses: fertilizers (NH₄NO₃), explosives (TNT, RDX, nitroglycerine), dyes

LIQUID NITROGEN (LN₂):
  bp = −196°C; cheap (from fractional distillation of liquid air)
  Cryogenic preservation: cells, tissues, sperm, embryos
  Food industry: flash-freezing (IQF), nitrogen ice cream (rapid freeze → small ice crystals)
  Shrink fitting: cool part → insert into slightly smaller hole → warms → interference fit
  NMR magnets: LN₂ shield around liquid He core (reduced He evaporation)

NITROGEN INERTNESS:
  N₂ used as inert atmosphere (cheaper than Ar for most lab purposes)
  Tire inflation: N₂ doesn't permeate rubber as fast as O₂ + no moisture → stable pressure
  Food packaging: modified atmosphere (N₂ + CO₂ displaces O₂ → retards spoilage)
```

---

## Oxygen (O, Z=8) — The Electronegative Driver

### Combustion and Respiration

```
COMBUSTION:
  Generic: fuel + O₂ → CO₂ + H₂O + energy
  Why O₂? Thermodynamics: ΔG°rxn very negative because O₂ has weak O=O bond (498 kJ/mol)
           while the products (H₂O, CO₂) have very stable C=O and O–H bonds

  FIRE TRIANGLE:
  Fuel + Oxidizer + Heat → Combustion
  Remove any one → fire goes out

AEROBIC RESPIRATION:
  C₆H₁₂O₆ + 6 O₂ → 6 CO₂ + 6 H₂O + 32 ATP (net; actual ≈ 30 ATP in mitochondria)
  Electron transport chain: NADH + ½O₂ + H⁺ → NAD⁺ + H₂O (Complex IV: cytochrome c oxidase)
  O₂ is the terminal electron acceptor

OXYGEN TOXICITY:
  High pO₂ → reactive oxygen species (ROS): O₂⁻ (superoxide), H₂O₂, OH• (hydroxyl radical)
  Hyperoxia in diving: O₂ > 0.5 atm partial pressure → CNS seizures → drowning
  Neonatal O₂ excess → retinopathy of prematurity
  Normal protection: superoxide dismutase (SOD), catalase, glutathione peroxidase
```

### Ozone (O₃)

```
OZONE STRUCTURE:
  Bent molecule (116.8°), resonance-stabilized, paramagnetic (one unpaired electron in some
  representations — actually 2 resonance forms average)
  O₃ ⇌ O₂ + O  (ΔH = +105 kJ/mol) → O₃ is thermodynamically unstable relative to O₂
  Strong oxidizer: E°(O₃/O₂) = +2.07 V

STRATOSPHERIC OZONE:
  Chapman cycle: O₂ + hν → 2O, then O + O₂ → O₃ (creates ozone layer)
  Ozone absorbs UV-B (280–315 nm) → essential UV shield for life
  CFC destruction: CFCl₃ + hν → CFCl₂• + Cl•; Cl• + O₃ → ClO + O₂ (catalytic cycle)
  One Cl atom destroys ~100,000 O₃ molecules before removal
  Montreal Protocol 1987 → CFCs phased out → ozone hole recovering (predicted full by ~2065)

INDUSTRIAL OZONE:
  Generated by corona discharge (O₂ + high voltage → O₃)
  Water treatment: stronger disinfectant than Cl₂, leaves no taste/odor residues
  Pulp bleaching: alternative to Cl₂
  Air purification, medical sterilization

O₂ PARAMAGNETISM:
  O₂ is paramagnetic (2 unpaired electrons in degenerate π* antibonding MOs)
  Liquid O₂ attracted to magnet — visible demonstration
  Singlet oxygen (¹O₂): excited state with paired electrons → more reactive
  Produced by sensitizers + hν → photodynamic therapy for cancer, acne treatment
```

---

## Phosphorus (P, Z=15) — Energy Currency and Information Storage

### ATP and Biochemical Energy

```
ATP (adenosine triphosphate):
  Structure: adenosine + 3 phosphate groups linked by high-energy phosphoanhydride bonds
  ATP ← ADP + Pᵢ  ΔG° = −30.5 kJ/mol (hydrolysis; in cell context ~−50 kJ/mol)

  WHY ATP IS "HIGH ENERGY":
    1. Resonance destabilization: phosphates repel each other (negatively charged)
    2. Resonance stabilization of products: ADP²⁻ and HPO₄²⁻ stabilized by resonance
    3. Solvation: products better solvated than ATP
    4. pKa shift: ADP²⁻ released → picks up H⁺ → entropy gain

  ATP PRODUCTION (net per glucose):
    Glycolysis: 2 ATP (substrate level)
    Pyruvate oxidation + TCA cycle: 6 NADH + 2 FADH₂ + 2 GTP
    Oxidative phosphorylation: ~28 ATP (NADH → 2.5 ATP; FADH₂ → 1.5 ATP each)
    Total: ~30-32 ATP

DNA AND RNA BACKBONE:
  Phosphodiester linkage: sugar-phosphate-sugar (negatively charged at pH 7)
  Phosphate groups: give DNA its negative charge → condensed by histones (positive)
  → chromosome packing: 2m of DNA fits in nucleus of 6 μm diameter

PHOSPHOLIPID BILAYER:
  Glycerophospholipids: glycerol + 2 fatty acids + phosphate + head group
  Head: negative charge (phosphate) with various functional groups (choline, serine, ethanolamine)
  Self-assemble into bilayer (hydrophobic core, hydrophilic exterior) → all cell membranes
```

**Phosphorus as a finite, non-substitutable supply chain risk:** Unlike nitrogen (fixed from atmospheric N₂ via Haber-Bosch), phosphorus has no atmospheric reservoir. It must come from mining phosphate rock — and reserves are geographically concentrated: Morocco controls ~70% of global reserves (and essentially 100% of high-quality reserves if you include the Western Sahara, which Morocco administers). China, Russia, and a few other nations hold most of the rest. There is no geological cycle returning phosphorus from ocean sediments to land on human timescales (the cycle takes ~10–100 Myr). Current USGS reserve estimates at current mining rates give ~300–400 years, but "peak phosphorus" (maximum rate of production before decline) may arrive within 50–80 years. The parallel to rare-earth supply chains (10-LANTHANIDES.md) is direct: a material with no substitute, concentrated geopolitical control, and a finite reserve. The engineering response being researched is phosphorus recovery from sewage (struvite precipitation: MgNH₄PO₄) and from agricultural runoff — essentially recycling the element rather than extracting it from rock.

### Phosphorus Allotropes

```
ALLOTROPES:
  White phosphorus (P₄):  tetrahedral P₄ units; mp 44°C; waxy solid; glows in dark
                          (chemiluminescence from slow oxidation); extremely toxic;
                          spontaneously ignites in air above 30°C; stored under water;
                          used in incendiary weapons (controversial under Geneva Protocol)

  Red phosphorus:         amorphous polymer network; stable in air; non-toxic;
                          strike strip on matchboxes (red P + KClO₃ + friction = fire);
                          made by heating P₄ at 250°C without air

  Black phosphorus:       most thermodynamically stable form; layered like graphite;
                          semiconductor (~0.3 eV bandgap); recently synthesized
                          in quantity; exfoliated to phosphorene (2D material, like graphene)
                          Direct bandgap at monolayer → promising for transistors, optics

FERTILIZERS:
  World's phosphorus rock (phosphate rock = Ca₃(PO₄)₂, fluorapatite)
  Limited reserves → phosphorus scarcity concern (finite unlike nitrogen)
  Superphosphate: Ca₃(PO₄)₂ + H₂SO₄ → Ca(H₂PO₄)₂ + CaSO₄ (Lawes, 1842)
  Triple superphosphate (TSP): Ca₃(PO₄)₂ + 3 H₃PO₄ → 3 Ca(H₂PO₄)₂ (higher P%)
  Monoammonium phosphate (MAP), diammonium phosphate (DAP): common granular fertilizers
  Struvite recovery: MgNH₄PO₄ from wastewater — sustainable P recycling
```

---

## Sulfur (S, Z=16) — Disulfides and Industrial Chemistry

### S₈ Structure and Allotropes

```
ELEMENTAL SULFUR:
  Most stable form: rhombic sulfur (α-S) — puckered S₈ rings, yellow crystals
  Above 96°C: monoclinic sulfur (β-S) — same S₈ units, different crystal packing
  Above 119°C: liquid (mobile, yellow)
  Above 160°C: viscous red (S₈ rings open → polymeric chains — tangled)
  Above 200°C: mobile again (chains break shorter)
  bp = 445°C (sulfur vapor contains S₂, S₄, S₆, S₈ species)
```

### Disulfide Bridges in Proteins

```
PROTEIN STRUCTURE:
  Cys-SH + Cys-SH  →(oxidation)→  Cys-S-S-Cys + 2H⁺ + 2e⁻

  Disulfide bonds (S-S, ~240 kJ/mol) covalently cross-link protein chains
  → major contribution to tertiary/quaternary structure stability

  Examples:
    Insulin: 2 chains linked by 2 inter-chain S-S bonds + 1 intra-chain S-S
    Immunoglobulins (antibodies): S-S bonds in hinge region connecting heavy chains
    Keratin (hair/nails): extensive S-S network → hardness and tensile strength
    Permanent wave (perm): reduce S-S bonds (with thioglycolate), reshape hair, reoxidize

IRON-SULFUR CLUSTERS:
  [2Fe-2S] and [4Fe-4S] clusters in proteins (ferredoxins, NADH dehydrogenase, etc.)
  Iron coordinated by cysteine residues and bridging S²⁻
  Function as electron carriers (redox potential tunable by protein environment)
  Ancient: likely present in early life before O₂ atmosphere
  Complex I (NADH dehydrogenase) has 8 Fe-S clusters

COENZYME A (CoA):
  Contains pantothenate + thioethylamine terminating in –SH (thiol)
  Acyl-CoA (R-CO-S-CoA): thioester high-energy bond
  Central metabolic intermediate: acetyl-CoA feeds TCA cycle, fatty acid synthesis
```

### H₂SO₄ Industrial Chemistry

```
SULFURIC ACID — most produced industrial chemical by volume
  ~200 million tonnes/yr (global production)

CONTACT PROCESS:
  S or FeS₂ + O₂ → SO₂
  2 SO₂ + O₂ →(V₂O₅ catalyst, 400-600°C)→ 2 SO₃
  SO₃ + H₂SO₄ → oleum (H₂S₂O₇) — then diluted with water
  (Direct addition of SO₃ to water is too exothermic and produces acid mist)

H₂SO₄ USES:
  Fertilizers: Ca₃(PO₄)₂ + H₂SO₄ → superphosphate, also (NH₄)₂SO₄
  Lead-acid batteries: H₂SO₄ electrolyte (12M, ~37%)
  Chemical manufacturing: HNO₃, HCl, various organics
  Petroleum refining: alkylation (isobutane + olefins → high-octane gasoline)
  Metals processing: pickling (remove oxide scale from steel), hydrometallurgy

ACID RAIN:
  Coal combustion → SO₂ → SO₃ → H₂SO₄ (in atmosphere, drops pH of rain)
  Also NOₓ → HNO₃
  Impacts: lake acidification, forest damage, limestone monument dissolution
  SO₂ scrubbing with Ca(OH)₂ → CaSO₄ (gypsum byproduct → wallboard)
```

---

## The Five Elements Together — A Systems View

```
C/N/O/P/S METABOLIC WEB:

  ATMOSPHERE
  CO₂ (C+O)  ←──────────────────────────────────────────┐
  N₂         ←──────────────────────────┐               │
                                         │               │
  Photosynthesis                         │ Respiration    │
  (C+O: CO₂ → glucose)                  │ (C+O: glucose  │ Decomposition
                                         │  → CO₂)       │ (all 5 elements
  ┌─────────────────────────────────────┐│               │  released)
  │          LIVING CELL                ││               │
  │                                     ││               │
  │  DNA/RNA ─────── C+N+O+P ─────────────────────→ DEAD ORGANIC
  │  (phosphodiester │ backbone)         │            MATTER
  │                  │                   │               │
  │  Protein ─────── C+N+O+S  ──────→  │               │
  │  (amino acids,   │ disulfides)       │               │
  │  enzymes)        │                   │               │
  │                  │                   │               │
  │  ATP ──────────  C+N+O+P            │              │
  │  (energy         phosphoanhydride    │               │
  │   currency)      bonds               │               │
  │                  │                   │               │
  │  Membrane ─────  C+O+P              │               │
  │  (phospholipid   polar head +        │               │
  │   bilayer)       fatty acid tails    │               │
  │                  │                   │               │
  │  Redox ────────  S (Fe-S clusters), N (NAD+)         │
  │  (electron       CoA thioester                       │
  │   transport)                         │               │
  └──────────────────────────────────────┘               │
                │                                         │
                └──────────────────── Decomposers (fungi, bacteria) ───┘

KEY FLUX CONSTRAINTS:
  C: freely cycled via atmosphere (CO₂ ↔ organic carbon)
  N: atmosphere reservoir (N₂) accessible only via Rhizobium/Azotobacter/Haber-Bosch
  O: freely cycled (O₂ ↔ H₂O ↔ CO₂)
  P: NO atmospheric reservoir → LIMITING NUTRIENT in many ecosystems
     must come from rock weathering or recycled organic matter
  S: mostly cycled; can limit in some agricultural soils (acid rain adds inadvertent SO₄²⁻)
```

ELEMENTAL SCARCITY IN THE BIOSPHERE:
  C, N, O: readily cycled through atmosphere (CO₂, N₂, O₂)
  P: LIMITING NUTRIENT in many ecosystems — no gaseous form, must come from weathering
     Liebig's Law of the Minimum: growth limited by the scarcest required nutrient
     P is often the limiting nutrient in freshwater lakes (→ eutrophication when added)
  S: often limiting in soils that lack pyrite/gypsum; atmospheric SO₂ from acid rain
     can inadvertently fertilize S-deficient soils
```

---

## Decision Cheat Sheet

| Need | Element | Key chemistry |
|------|---------|---------------|
| Structural polymer (carbon-based) | C | C–C backbone, functionalized |
| Nitrogen fertilizer at scale | N | NH₃ via Haber-Bosch → urea, ammonium nitrate |
| Metabolic energy currency | P | ATP (phosphoanhydride bond) |
| Oxidative metabolism terminal acceptor | O | O₂ → H₂O via cytochrome c oxidase |
| Protein structural crosslinking | S | Disulfide (Cys-S-S-Cys) |
| Industrial chemical of largest volume | S | H₂SO₄ (contact process) |
| Cell membrane architecture | P | Phospholipid bilayer |
| UV screen (stratosphere) | O | O₃ (absorbs 280–315 nm) |
| Electron carrier in respiration | S | Fe-S clusters, CoA thioester |

---

## Common Confusion Points

**"Why can't we just use atmospheric N₂ directly?"**
Plants cannot break the N≡N triple bond (945 kJ/mol) with normal enzymes.
Only nitrogenase (which uses 16 ATP per N₂) and lightning (thermal dissociation) fix it.
Haber-Bosch requires 400–500°C and 200 atm for the same reason.

**"ATP hydrolysis — where does the energy actually come from?"**
The energy isn't stored in a "high-energy bond" the way that implies. The G released is a
thermodynamic function of the reaction going forward under cellular concentrations. The
reasons: resonance stabilization of products, relief of charge repulsion, solvation effects.
You can't light a fire with ADP. The energy comes from the overall concentration-driven
thermodynamic favorable equilibrium.

**"Oxygen makes things burn — but living things use oxygen and don't combust"**
Living things carefully control the reaction. O₂ is reduced at Complex IV via a series of
electron transfer steps, releasing energy incrementally as H⁺ gradient (proton-motive force)
rather than as heat all at once. The rate is controlled by ATP demand. ROS are produced as
byproducts and neutralized by antioxidant enzymes (SOD, catalase, GPx).
