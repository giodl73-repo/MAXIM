# Nanomaterials: Quantum Dots, Nanoparticles, and Size-Dependent Properties

## The Big Picture

Nanomaterials are materials with at least one dimension in the 1-100 nm range, giving them
properties that differ from their bulk counterparts. The field spans semiconductor nanocrystals,
metal nanoparticles, metal oxide nanoparticles, and bio-derived nanostructures.

```
NANOMATERIALS TAXONOMY
=======================

                    NANOMATERIALS
                          |
          +---------------+---------------+
          |               |               |
   SEMICONDUCTOR     METAL NP         METAL OXIDE
   NANOCRYSTALS      --------         -----------
   (Quantum Dots)    Gold NP          TiO2
     CdSe/ZnS        Silver NP        ZnO
     InP             Copper NP        Fe3O4 (iron oxide)
     Perovskite QD   Platinum NP      CeO2
          |               |               |
     DISPLAYS        DETECTION         CATALYSIS
     BIOIMAGING      ANTIMICROBIAL     BIOMEDICAL
     SOLAR CELLS     CATALYSIS         ENERGY

          |
   BIO-DERIVED / NATURAL
   --------------------
   Nanocellulose (CNC, CNF): wood-derived
   Silk nanofibers
   Ferritin (iron storage protein, 8 nm)
   Viral capsids (20-300 nm geometric particles)
```

---

## Quantum Dots (QD)

### CdSe/ZnS Core-Shell Quantum Dots

```
CdSe/ZnS CORE-SHELL STRUCTURE
================================

          ZnS shell (1-2 nm)
      +----------------------+
      |   +----------------+ |
      |   |                | |
      |   |   CdSe core    | |
      |   |   (2-6 nm)     | |
      |   |                | |
      |   +----------------+ |
      +----------------------+
      |  Ligand layer       |
      |  (TOPO, oleic acid) |
      +---------------------+

WHY CORE-SHELL?
  CdSe core: quantum confinement, emission wavelength set by size
  ZnS shell: wider bandgap (3.6 eV vs. CdSe 1.74 eV)
    -> confines exciton to core (prevents leakage to surface)
    -> passivates surface traps (non-radiative recombination)
  Result: quantum yield improves from ~10% (core only) to ~85% (core-shell)

Ligands:
  Tri-octylphosphine oxide (TOPO): original synthesis, soluble in organic solvents
  Oleic acid / oleylamine: shorter ligands, better packing
  Water-soluble ligands (PEG-thiol): required for biomedical use

SYNTHESIS (hot-injection method, Bawendi 1993):
  Cadmium precursor (Cd-oleate) in high-boiling solvent (ODE) at 280-300 C
  Inject selenium precursor (TOPSe) rapidly
  Burst of nucleation (classical LaMer mechanism)
  Stop nucleation by temperature drop; growth continues
  Quench reaction to stop at desired size
  Post-synthesis: size-selective precipitation to narrow distribution
```

### QD Applications

| Application | Technology | Notes |
|-------------|-----------|-------|
| QLED displays | CdSe/ZnS or InP on LED backlight | Narrow emission, wide color gamut |
| Bioimaging | Water-soluble QD-antibody conjugate | Photobleaching resistant vs. organic dyes |
| Single-molecule tracking | Single QD on cell surface | Blink on/off is a challenge |
| QD solar cells | CdS, PbS, perovskite QD | Bandgap tuning for multi-junction |
| Photodetectors | PbS QD, IR range | Night vision, SWIR imaging |

**Toxicity note**: Cd-containing QDs release Cd2+ ions in biological environments.
Significant toxicity concern limits medical use. InP/ZnS (cadmium-free) QDs have
similar optical properties with less toxicity -- increasingly preferred in displays and biomedical.

---

## Gold Nanoparticles (AuNP)

### Synthesis and Plasmon Resonance

```
GOLD NANOPARTICLE SYNTHESIS
============================

TURKEVICH METHOD (1951, still standard):
  HAuCl4 in water at 100 C + sodium citrate (reducing + stabilizing agent)
  Au3+ reduced to Au0; citrate caps surface (negative charge = electrostatic stabilization)
  Size controlled by HAuCl4:citrate ratio
  Typical: 5-100 nm spheres; narrow size distribution ~10% CV
  Color: wine red (20 nm), blue-purple (100 nm)

SEED-MEDIATED GROWTH:
  Grow larger particles from small seeds
  Better size control for 10-200 nm range
  Shape control: add surfactants (CTAB) to direct growth to rods, prisms, etc.

PLASMON RESONANCE (LSPR):
  See 01-NANOSCALE-PHYSICS.md for physics
  LSPR wavelength:
    Sphere: 520-580 nm (moves with size, solvent refractive index)
    Rod: two modes -- transverse (~520 nm) + longitudinal (600-900 nm, tunable by aspect ratio)
    Shell/cage: 700-1200 nm (NIR)

  NIR AuNP are important for biomedical:
    Tissue is relatively transparent at 700-1100 nm ("optical window")
    NIR Au nanorods/nanocages: photothermal therapy (heat tumor with near-IR laser)
```

### AuNP Applications

**Pregnancy test lateral flow assay**: 20 nm AuNP conjugated to antibody.
When hCG (pregnancy hormone) is present, antibody-AuNP accumulates at test line,
producing visible red band. No instruments, room temperature, 1 minute. One of the
highest volume nanomaterial applications in the world.

```
COLORIMETRIC DETECTION WITH AuNP
==================================

AuNP (red, dispersed)  +  target analyte  ->  AuNP (blue, aggregated)

Mechanism:
  Analyte crosslinks AuNP via bifunctional linker or aptamer
  Aggregation shifts LSPR from 520 to 600+ nm -> color shift red to blue
  Visible to naked eye or spectrophotometric

Applications:
  Pregnancy test (lateral flow)
  Heavy metal detection (Pb2+, Hg2+ at ppb level)
  DNA hybridization detection
  SERS: aggregated AuNP creates "hot spots" (|E|^2 >> 10^6 enhancement)
    -> single molecule Raman detection possible
```

---

## Iron Oxide Nanoparticles (IONP)

```
IRON OXIDE NP TYPES
====================

Fe3O4 (magnetite): ferrimagnetic (high magnetization ~80-90 emu/g)
gamma-Fe2O3 (maghemite): also magnetic, more stable to oxidation
Fe2O3 (hematite): antiferromagnetic, not useful for these applications

SUPERPARAMAGNETISM:
  Single-domain nanoparticles (<20-30 nm for Fe3O4)
  Magnetic moment fluctuates randomly when kT > magnetic anisotropy energy
  No net magnetization without applied field (no remanence, no coercivity)
  BUT: very large susceptibility in applied field (paramagnetic-like but 10^3 stronger)

  This is critical for biomedical use:
  - No field: NPs don't aggregate (no permanent magnetism)
  - Apply field: NPs respond strongly (MRI contrast, magnetic hyperthermia, separation)

MRI CONTRAST AGENTS:
  Fe3O4 NP shortens T2 relaxation time of water protons in surrounding tissue
  Creates dark regions on T2-weighted MRI images
  Typical: 5-10 nm core, dextran or PEG coating, ~100 nm hydrodynamic diameter
  Ferumoxides (Feridex): FDA-approved 1996 (withdrawn 2008 for business reasons)
  SPION research: lymph node mapping, liver lesion detection, cellular tracking

MAGNETIC HYPERTHERMIA:
  Alternating magnetic field (100-500 kHz, ~10-15 kA/m)
  IONP absorb energy via Neel relaxation (spin flip) and Brownian relaxation
  Specific absorption rate (SAR): 10-1000 W/g Fe
  Temperature rises 5-20 C in tumor microenvironment
  MagForce AG (Berlin): first clinical approval (Germany 2011) for glioblastoma
  Challenge: achieving therapeutic temperature without systemic toxicity
```

---

## Silver Nanoparticles (AgNP): Antimicrobial Mechanism

```
SILVER NANOPARTICLE ANTIMICROBIAL ACTION
==========================================

THREE-PATHWAY MODEL:

1. Ag+ ION RELEASE:
   AgNP oxidize in aqueous/aerobic environment: 4Ag + O2 + 2H2O -> 4Ag+ + 4OH-
   Ag+ is the primary antimicrobial agent (same as silver nitrate wound treatment)
   Ag+ binds to thiol groups (-SH) of bacterial proteins -> inhibits enzymes
   Ag+ disrupts electron transport chain
   MIC (minimum inhibitory concentration): 0.1-10 ppm Ag+ for E. coli, S. aureus

2. REACTIVE OXYGEN SPECIES (ROS):
   AgNP surface catalyzes ROS generation (superoxide O2-, hydroxyl OH*)
   ROS oxidize lipids, proteins, DNA
   Particularly effective against biofilms

3. DIRECT NP-MEMBRANE INTERACTION:
   NP <10 nm can penetrate cell membrane
   Disrupts membrane integrity
   Less important than Ag+ for most organisms

APPLICATIONS:
  Wound dressings: Acticoat (Smith & Nephew), Mepilex Ag -- silver ion releasing
  Textiles: odor-resistant sportswear (kills odor-causing bacteria)
  Catheters: reduced biofilm formation
  Surface coatings: hospital surfaces, HVAC

ENVIRONMENTAL CONCERNS:
  AgNP persist in environment, release Ag+ in soil/water
  Toxic to aquatic organisms at low ppb levels
  Wastewater treatment removes some but not all
  EPA monitoring: AgNP-containing products must disclose under FIFRA
```

---

## Titanium Dioxide (TiO2) Nanoparticles

```
TiO2 PHOTOCATALYSIS
====================

Crystal structures:
  Anatase: bandgap 3.2 eV (UV at 387 nm) -- better photocatalytic activity
  Rutile: bandgap 3.0 eV (UV at 413 nm) -- more stable, used in sunscreen
  Brookite: metastable, research interest

PHOTOCATALYTIC MECHANISM:
  TiO2 + hv (UV, > 3.2 eV) -> e- (conduction band) + h+ (valence band)

  Oxidation pathway (h+):
    h+ + H2O -> OH* (hydroxyl radical) -- highly oxidizing (E = +2.8 V)
    OH* oxidizes organics, bacteria, pollutants to CO2 + H2O

  Reduction pathway (e-):
    e- + O2 -> O2*- (superoxide) -> further oxidizing species

  Net: UV light + TiO2 + O2 + H2O -> mineralization of organics

APPLICATIONS:
  Self-cleaning glass (Pilkington Activ):
    TiO2 coating, anatase phase
    UV from sunlight -> OH* generation -> breaks down organic grime
    Also superhydrophilic: water sheets off rather than beads -> washes dirt away

  Air purification:
    TiO2-coated surfaces in hospitals, HVAC filters
    Degrades formaldehyde, VOCs, pathogens under UV light

  Sunscreen:
    Rutile TiO2 nanoparticles (5-50 nm): absorb and scatter UV-A and UV-B
    Transparent to visible light (vs. bulk TiO2 which is white)
    Non-toxic at cosmetic surface concentrations (GRAS status)

  Water treatment:
    Advanced oxidation process (AOP): UV + TiO2 + H2O2
    Degrades pharmaceuticals, endocrine disruptors at ppb-ppt levels
    Challenge: UV light source energy cost; visible-light photocatalysts (doping N, C)
```

---

## Nanocellulose (CNC and CNF)

Nanocellulose is derived from wood pulp or plant cellulose by controlled hydrolysis or
mechanical processing. It is bio-sourced, biodegradable, and has extraordinary mechanical
properties.

```
NANOCELLULOSE TYPES
====================

CNC (Cellulose Nanocrystals):
  Also: NCC (nanocrystalline cellulose) or CNW (cellulose nanowhiskers)
  Size: 5-20 nm wide, 100-500 nm long (rod-shaped)
  Process: sulfuric acid hydrolysis (dissolves amorphous regions, leaves crystalline)
  Surface: sulfate ester groups from H2SO4 (negative charge, good colloidal stability)
  Crystallinity: ~90% (vs. ~65% in native cellulose)
  Young's modulus: ~150 GPa (comparable to Kevlar, fraction of carbon fiber cost)
  Tensile strength: ~7.5 GPa (theoretical)

CNF (Cellulose Nanofibrils):
  Also: NFC (nanofibrillated cellulose), MFC (microfibrillated cellulose at larger end)
  Size: 3-20 nm wide, 0.5-2 um long (fibril, more flexible than CNC)
  Process: mechanical defibrillation (high-pressure homogenizer, microfluidizer)
           often with enzymatic or TEMPO pre-treatment
  Higher aspect ratio than CNC; forms gels readily

PROPERTIES COMPARISON:
  Property        CNC              CNF
  Width           5-20 nm          3-20 nm
  Length          100-500 nm       0.5-2 um
  Aspect ratio    5-50             100-500
  Crystallinity   ~90%             ~50-70%
  Suspension      Isotropic->chiral gel phase  Forms gel at ~0.5 wt%
  Strength        Very high        High, flexible
  Surface groups  Sulfate (H2SO4)  Carboxyl (TEMPO), hydroxyl

APPLICATIONS:
  Composites: CNC in epoxy or PLA (bioplastic) -- stiffness + strength improvement
  Transparent flexible films: CNF paper for flexible electronics substrates
  Hydrogels: CNF in wound dressings, tissue engineering scaffolds
  Rheology modifier: food (fat replacement), coatings, drilling fluids
  Barrier coatings: CNC films reduce O2 permeability in food packaging
  Template: liquid crystal phase of CNC used to template nanostructures

PRODUCTION:
  Commercially produced: CelluForce (Canada), American Process Inc., USDA Forest Products
  Cost: ~$1,000-5,000/kg (CNC, 2025) -- high, limiting applications
  Wood pulp feedstock is renewable and abundant; cost will decline with scale
```

---

## Nanomaterial Properties Comparison

| Material | Size Range | Key Property | Primary Application |
|----------|-----------|--------------|---------------------|
| CdSe/ZnS QD | 2-8 nm | Tunable emission | QLED displays |
| InP/ZnS QD | 2-6 nm | Tunable emission, Cd-free | Next-gen QLED |
| Gold NP | 5-200 nm | LSPR, biocompatible | Diagnostics, photothermal |
| Silver NP | 5-100 nm | Antimicrobial | Wound care, textiles |
| Fe3O4 NP | 5-30 nm | Superparamagnetic | MRI, hyperthermia |
| TiO2 NP | 5-50 nm | Photocatalysis, UV absorption | Sunscreen, self-cleaning |
| ZnO NP | 10-100 nm | UV absorption, photocatalysis | Sunscreen, antimicrobial |
| Pt NP | 1-10 nm | Catalytic activity | Fuel cells, catalytic conv. |
| CNC | 5x200 nm | High stiffness, bio-based | Composites, coatings |
| CNF | 5nm x 1um | Flexible, high aspect ratio | Gels, transparent films |

---

## Decision Cheat Sheet

| Need... | Use... |
|---------|--------|
| Tunable visible emission, displays | CdSe/ZnS or InP/ZnS quantum dots |
| Colorimetric biosensor (naked eye) | Gold nanoparticles (LSPR color shift) |
| MRI contrast enhancement | Fe3O4 superparamagnetic nanoparticles |
| Antimicrobial surface coating | Silver nanoparticles |
| UV-blocking transparent coating | TiO2 or ZnO nanoparticles |
| Self-cleaning surface | TiO2 nanoparticles (photocatalytic) |
| Bio-based mechanical reinforcement | Cellulose nanocrystals (CNC) |
| Gel-forming rheology modifier | Cellulose nanofibrils (CNF) |
| Photothermal cancer therapy | Gold nanorods (NIR absorbing) |
| Magnetic hyperthermia cancer therapy | Fe3O4 nanoparticles + AC field |

---

## Common Confusion Points

**"Quantum dots and quantum wells are the same."** No. Quantum dots are 0D (confined in
all three dimensions, discrete energy levels). Quantum wells are 2D (confined in one
dimension, subbands but still continuous in 2D). Different physics, different applications.

**"Gold nanoparticles are biocompatible because gold is inert."** Gold NP have been
extensively studied and are generally considered low-toxicity. But surface chemistry
matters: bare Au NP vs. citrate-capped vs. PEG-coated have different cellular interactions.
"Biocompatible" is application- and coating-specific, not intrinsic to the material.

**"Larger surface area always means higher reactivity."** Generally true, but shape and
exposed crystal facets matter. A 5 nm Au NP with all (111) facets may be less reactive than
a 10 nm Au NP with corner/edge sites. Catalytic selectivity is also face-dependent.

**"Nanocellulose is a nanomaterial, so it must be expensive/exotic."** It comes from wood,
the most abundant structural biomass on Earth. It is already produced commercially. The
challenge is processing cost, not feedstock scarcity.
