# 00-OVERVIEW — Natural Sciences: Field Taxonomy & Unifying Principles

> Scale hierarchy, field map, emergence, conservation laws, and the cross-disciplinary
> bridges that let chemistry, biochemistry, biology, Earth science, and plasma physics
> talk to each other.

---

## The Scale Hierarchy

Everything in natural science is an inquiry at a particular scale.
Understanding *which scale* determines which tools, approximations, and languages apply.

```
SCALE        SIZE            FIELD            GOVERNING FRAMEWORK
─────────────────────────────────────────────────────────────────────
Cosmological  >1 Mpc          Cosmology        GR + ΛCDM
Stellar        ~R☉            Astrophysics     plasma physics, nuclear
Planetary      ~R♁            Geophysics       continuum mechanics, MHD
                               Atmosphere       fluid dynamics, radiation
Macroscopic    cm–km           Classical mech.  Newtonian / thermo
Mesoscopic     µm–mm           Soft matter      stat mech, hydrodynamics
Cellular       1–100 µm        Cell biology     diffusion, reaction–diff.
Molecular      0.1–10 nm       Chemistry        QM + stat mech
Atomic         ~0.1 nm         Atomic physics   quantum mechanics (QM)
Nuclear        ~1 fm           Nuclear physics  QCD / nuclear force
Subatomic      <1 fm           Particle physics QFT / Standard Model
```

**Key insight**: each scale transition involves *emergence* — the tools that work
at one level become intractable at the next. Quantum chemistry computes H₂ exactly;
it cannot compute a protein fold from first principles. That gap *is not ignorance*,
it is irreducibility, and every field in this library lives in that gap.

---

## Field Map

```
NATURAL SCIENCES
│
├── PHYSICAL SCIENCES
│   ├── Chemistry                    ← atomic/molecular-scale matter transformations
│   │   ├── Physical chemistry       (thermochem, kinetics, quantum chem, spectroscopy)
│   │   ├── Organic chemistry        (C-H-N-O-P-S frameworks, reaction mechanisms)
│   │   ├── Inorganic chemistry      (coordination compounds, solid state, materials)
│   │   └── Analytical chemistry     (measurement, separation, detection)
│   │
│   ├── Physics                      ← (see physics/ directory)
│   │   ├── Classical / E&M / QM / QFT
│   │   └── Plasma physics           ← bridges to chemistry AND astrophysics
│   │
│   └── Earth Sciences               ← planetary-scale chemistry+physics
│       ├── Geophysics               (mantle dynamics, seismology, geomagnetism)
│       ├── Geochemistry             (element cycling, isotopes, dating)
│       └── Atmospheric science      (climate, weather, photochemistry)
│
└── LIFE SCIENCES
    ├── Biochemistry                 ← chemistry OF life (molecules, reactions, energetics)
    │   ├── Structural biochem.      (protein/nucleic acid structure–function)
    │   ├── Enzymology               (catalysis, kinetics, regulation)
    │   └── Metabolic biochem.       (pathways, energy coupling, biosynthesis)
    │
    └── Biology                      ← organization, behavior, evolution of living systems
        ├── Cell biology             (organelles, signaling, cytoskeleton, division)
        ├── Molecular biology        (DNA replication, transcription, translation)
        ├── Genetics / Genomics      (inheritance, mutation, population genetics)
        ├── Evolutionary biology     (selection, drift, speciation, evo-devo)
        └── Systems / Synthetic bio  (networks, design, engineering living systems)
```

---

## The Unifying Principles

Six principles recur across every field in this library.
Understanding them as *the same principle* at different scales is the meta-skill.

### 1. Conservation Laws

Derived from symmetries (Noether's theorem):

| Symmetry | Conserved Quantity | Where It Shows Up |
|----------|--------------------|-------------------|
| Time translation | Energy | Thermochem, metabolism, stellar structure |
| Space translation | Momentum | Fluid dynamics, plasma, collisions |
| Rotation | Angular momentum | Orbital mechanics, MHD, protein docking |
| U(1) gauge | Electric charge | Electrochemistry, ionic balance, membrane potential |
| SU(3) gauge | Color charge | Quarks (rarely appears at chemistry scale) |

Chemistry adds one near-conservation: **atom count** (balanced equations).
Biochemistry adds: **redox balance** (electrons must go somewhere).

### 2. The Second Law — Entropy and Free Energy

```
ΔG = ΔH − TΔS     (Gibbs, constant T and P — chemistry/biochemistry)
ΔA = ΔU − TΔS     (Helmholtz, constant T and V — statistical mechanics)
```

- **ΔG < 0**: spontaneous (exergonic). Drives chemistry forward.
- **ΔG > 0**: non-spontaneous (endergonic). Requires coupling to exergonic process.
- **Coupled reactions**: life works almost entirely by coupling ΔG < 0 reactions
  (ATP hydrolysis, proton gradients) to drive ΔG > 0 reactions (biosynthesis, transport).

The entropy arrow *does not* conflict with biological complexity:
organisms are open systems. Local order increases, global entropy increases faster.

### 3. Rate vs. Equilibrium — the Kinetic/Thermodynamic Distinction

Thermodynamics tells you *if* a reaction is favored (ΔG).
Kinetics tells you *how fast* it proceeds (rate constant k, activation energy Eₐ).

A reaction can be thermodynamically spontaneous and kinetically frozen
(diamond → graphite: ΔG = −2.9 kJ/mol; rate ≈ 0 at room temperature).

This distinction underlies:
- Catalysis (enzymes lower Eₐ without changing ΔG)
- Metastable states in geology (glasses, supersaturated solutions)
- Kinetic trapping in protein folding

### 4. Structure Determines Function

At every scale, spatial arrangement governs behavior:

```
Electrons in orbitals  → bonding type, reactivity, color
Molecular geometry     → polarity, solubility, drug binding
Protein fold           → catalytic activity, signaling, membrane anchoring
Chromatin structure    → gene expression (epigenetics)
Tissue architecture    → organ function
Mantle convection      → plate tectonics, volcanism
Plasma geometry        → confinement stability, instability modes
```

The structure–function principle is *why* techniques that reveal structure
(X-ray crystallography, cryo-EM, NMR, AFM) are central to every field.

### 5. Emergence and Downward Causation

Higher-level organization produces phenomena *not predictable* from lower-level rules:

| Lower level | Higher level | Emergent phenomenon |
|-------------|--------------|---------------------|
| Atoms | Molecules | Covalent bonds, chirality |
| Molecules | Lipid bilayer | Membrane permeability, self-sealing |
| Neurons | Brain | Consciousness (hard problem — unsolved) |
| Species | Ecosystem | Stability, trophic cascades |
| Individual cells | Organism | Development, regeneration |

Downward causation is real too: gene expression (molecular level) is
*controlled by* tissue context (cellular level) is *controlled by* organism
physiology (whole-body level). The arrow is bidirectional.

### 6. Information and Replication

Life is uniquely characterized by *information replication with variation under selection*.
Information has a substrate (DNA/RNA), but information content is distinct from substrate mass.

Shannon entropy H = -Σ pᵢ log₂ pᵢ enters biology:
- Genome information content
- Protein sequence space (~20^(length) combinations)
- Regulatory network complexity

This is why molecular biology converged with information theory
in the late 20th century — and why systems biology is now largely
a problem in network information theory.

---

## Cross-Disciplinary Hybrids

```
Field A            +  Field B             =  Hybrid
───────────────────────────────────────────────────────────────
Chemistry          +  Physics             =  Physical chemistry
Biology            +  Chemistry           =  Biochemistry
Biology            +  Physics             =  Biophysics
Chemistry          +  Earth science       =  Geochemistry / Cosmochemistry
Physics            +  Earth science       =  Geophysics
Biology            +  Earth science       =  Ecology / Biogeochemistry
Chemistry          +  Engineering         =  Chemical engineering
Biology            +  Engineering         =  Biotechnology / Synthetic biology
Physics (plasma)   +  Engineering         =  Fusion engineering
Statistics         +  Biology             =  Population genetics / Genomics
Information theory +  Biology             =  Systems biology / Bioinformatics
```

The boundaries are arbitrary and increasingly porous.
Seminal results often live at the seams:
- Watson/Crick: X-ray crystallography (physics) + organic chemistry + genetics
- Krebs cycle: organic chemistry mechanisms + thermodynamics + cell physiology
- Plate tectonics: seismology + mineralogy + paleomagnetism + fluid dynamics

---

## Mathematical Toolkit by Domain

| Domain | Core Math | Key Techniques |
|--------|-----------|----------------|
| Quantum chemistry | Linear algebra, PDEs | Schrödinger eq., variational methods, perturbation theory |
| Thermochemistry | Calculus, stat mech | Partition functions, Legendre transforms |
| Chemical kinetics | ODEs, stochastic | Rate equations, master equation, Gillespie |
| Structural biochem | Geometry, optimization | Ramachandran space, energy minimization |
| Metabolism | Graph theory, linear algebra | Flux balance analysis, stoichiometric matrices |
| Molecular biology | Information theory, combinatorics | Sequence alignment (DP), phylogenetics |
| Cell biology | Reaction–diffusion PDEs | Turing patterns, FRAP, optogenetics models |
| Genetics/evolution | Probability, stat | Hardy–Weinberg, Wright–Fisher drift, coalescent |
| Systems biology | ODEs, networks, control | Boolean/ODE network models, stability analysis |
| Geophysics | PDEs, tensors, fluid mech | Navier–Stokes, Stokes flow, seismic wave eq. |
| Atmospheric science | Fluid mech, radiative transfer | GCMs, Navier–Stokes + Coriolis + thermodynamics |
| Plasma science | Tensors, PDEs, stat mech | MHD, kinetic theory, Boltzmann/Vlasov eq. |

---

## The Reductionist Ladder — Where It Works and Where It Breaks

```
Reductionism works well:      │  Reductionism breaks (emergence):
──────────────────────────────┼─────────────────────────────────────
Atomic → molecular structure  │  Protein folding (17 modules = 10^300 conformations)
Orbital theory → bond angles  │  Cell behavior from protein interactions
Ideal gas law from kinetics   │  Consciousness from neurons
Nuclear binding energy        │  Ecosystem dynamics from species traits
Electron config → periodicity │  Evolution from mutation rates
Maxwell eq. → light speed     │  Weather beyond ~2 weeks (chaos)
```

Reductionism is the tool; emergence is the discovery.
Each module in this library is about one level of the ladder.

---

## Module Map for This Directory

```
natural-sciences/
│
├── CHEMISTRY  (01–05)
│   01-ATOMIC-QUANTUM.md    atomic structure, orbitals, quantum numbers, periodic table
│   02-BONDING.md           covalent/ionic/metallic, VSEPR, MO theory, hybridization
│   03-THERMOCHEM.md        enthalpy, entropy, Gibbs, Hess's law, phase equilibria
│   04-KINETICS.md          rate laws, Arrhenius, mechanisms, catalysis, transition state
│   05-ELECTROCHEMISTRY.md  redox, electrochemical cells, Nernst, Pourbaix, corrosion
│
├── BIOCHEMISTRY  (06–09)
│   06-BIOMOLECULES.md      amino acids, proteins, nucleic acids, lipids, carbohydrates
│   07-ENZYMES.md           Michaelis–Menten, inhibition, allostery, regulation
│   08-METABOLISM.md        glycolysis, TCA, oxidative phosphorylation, ATP accounting
│   09-MOLECULAR-BIO.md     replication, transcription, translation, regulation, CRISPR
│
├── BIOLOGY  (10–12)
│   10-CELL-BIOLOGY.md      organelles, membranes, signaling, cytoskeleton, division
│   11-EVOLUTION-GENETICS.md  Mendelian → molecular → population genetics → evo-devo
│   12-SYSTEMS-SYNTHETIC.md   network models, Boolean/ODE, synthetic circuits, optogenetics
│
├── EARTH SCIENCES  (13–14)
│   13-GEOPHYSICS.md        mantle dynamics, plate tectonics, seismology, geomagnetism
│   14-ATMOSPHERE-CLIMATE.md  atmospheric layers, radiation balance, GCMs, climate forcing
│
└── PLASMA SCIENCE  (15–16)
    15-PLASMA-FUNDAMENTALS.md   plasma state, Debye length, cyclotron, MHD, transport
    16-PLASMA-DYNAMICS.md       instabilities, confinement, fusion, astrophysical plasmas
```

---

## Decision Cheat Sheet — Which Field Answers Which Question

| Question | Field |
|----------|-------|
| Why does sodium explode in water? | Chemistry (reactivity, electronegativity) |
| Why does enzyme X slow down at high pH? | Biochemistry (ionization of active site residues) |
| How does a cell know when to divide? | Cell biology + molecular biology (signaling, checkpoints) |
| Why are antibiotic-resistant bacteria spreading? | Evolution + population genetics |
| Why does Earth's magnetic field flip? | Geophysics (core dynamics, MHD) |
| Why is the sky blue? | Physical chemistry / atmospheric science (Rayleigh scattering) |
| Why do proteins fold? | Physical chemistry + biochemistry (hydrophobic effect, ΔG) |
| What drives plate tectonics? | Geophysics (mantle convection, density contrast) |
| Why doesn't the Sun collapse? | Plasma physics (radiation pressure) + nuclear physics |
| How do tokamaks confine plasma? | Plasma dynamics (MHD equilibrium, instability suppression) |
| Why is CO₂ a greenhouse gas? | Atmospheric science + molecular quantum mechanics |
| How does insulin signal a cell? | Biochemistry + cell biology (receptor tyrosine kinase cascade) |

---

## Common Confusion Points

**"Organic" chemistry ≠ "natural" chemistry**
Organic = contains C–H bonds. Synthetic drugs, polymers, and explosives are all "organic."
"Natural" ≠ safe; "synthetic" ≠ dangerous. Categories based on C–H bonding, not origin.

**Energy vs. free energy**
ΔH (enthalpy) tells you heat released/absorbed.
ΔG (free energy) tells you if the reaction is spontaneous.
An exothermic reaction (ΔH < 0) can be non-spontaneous if TΔS is large enough to flip ΔG.

**Equilibrium ≠ dead**
Biological systems at "equilibrium" are dead.
Living systems are *far-from-equilibrium* open systems — they maintain order by
continuously consuming energy (food/light) and exporting entropy (heat/waste).

**Correlation ≠ causation in evolutionary biology**
Natural selection requires heritability + variation + differential reproduction.
Adaptations require all three. Traits that persist are not necessarily adaptive —
they may be neutral (genetic drift) or linked to selected traits (hitchhiking).

**Plasma is not ionized gas in the chemistry sense**
Plasma = collective behavior dominates (Debye length ≪ system size, ωₚ >> collision rate).
A weakly ionized gas in a lab discharge may or may not be "plasma" in the physics sense —
it depends on whether collective effects govern dynamics.

**Climate ≠ weather**
Weather = specific atmospheric state at a time/place (chaotic, predictable ~2 weeks).
Climate = statistical distribution of weather over decades (predictable trends despite weather chaos).
CO₂ forcing changes the distribution, not individual events — but shifts the probability of extremes.
