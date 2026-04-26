# Microbial Ecology

## The Big Picture

```
MICROBIAL ECOLOGY: MICROBES AS ECOSYSTEM ENGINEERS
====================================================

  Microbes drive ALL major biogeochemical cycles.
  Without microbial activity, multicellular life would collapse in months.

  ┌─────────────────────────────────────────────────────────────────┐
  │  ECOSYSTEM ROLES                                                │
  │                                                                 │
  │  PRODUCERS:      Cyanobacteria (photosynthesis, O₂ generation)  │
  │                  Chemoautotrophs (sulfur/iron oxidation)        │
  │                                                                 │
  │  DECOMPOSERS:    Soil bacteria + fungi → mineralization         │
  │                  Complete carbon cycle by returning C to CO₂    │
  │                                                                 │
  │  TRANSFORMERS:   Nitrogen fixers, nitrifiers, denitrifiers      │
  │                  Sulfate reducers, methanogens                  │
  │                  Iron reducers, manganese oxidizers             │
  │                                                                 │
  │  ENGINEERS:      Biofilm formers alter substrate chemistry      │
  │                  Stromatolites: First complex ecosystems (3.5 Ga)│
  │                  Coral reefs: Built on coral + Symbiodinium     │
  │                                                                 │
  │  SCALE:                                                         │
  │  ~10³⁰ bacteria on Earth (Kallmeyer et al.)                     │
  │  Deep subsurface: as many cells as surface + oceans combined    │
  │  Most not cultured; most metabolically novel                    │
  └─────────────────────────────────────────────────────────────────┘
```

---

## Biofilms: Microbial Cities

```
  BIOFILMS
  =========

  Biofilm = structured community of microbes attached to surface,
  enclosed in self-produced matrix (EPS = extracellular polymeric substances)

  95% of bacteria in nature exist as biofilms. Planktonic is the exception.

  BIOFILM FORMATION STAGES:
  ┌────────────────────────────────────────────────────────────────┐
  │                                                                │
  │  1. INITIAL ATTACHMENT                                         │
  │     Reversible adhesion → surface sensing                      │
  │     c-di-GMP (bis-(3'-5')-cyclic dimeric GMP):                 │
  │     Key second messenger; HIGH c-di-GMP → biofilm mode         │
  │     LOW c-di-GMP → planktonic/motile mode                      │
  │     Synthesized by DGCs (diguanylate cyclases)                 │
  │     Degraded by PDEs (phosphodiesterases)                      │
  │                                                                │
  │  2. IRREVERSIBLE ATTACHMENT                                    │
  │     Pili, adhesins anchor cell to surface                      │
  │     Flagella: Assists initial surface contact                  │
  │     curli fimbriae (E. coli): Amyloid-like; strong adherence   │
  │                                                                │
  │  3. MICROCOLONY FORMATION                                      │
  │     Division → mushroom-shaped towers                          │
  │     Water channels form between towers (nutrient delivery)     │
  │     Gene expression program shifts: different from planktonic  │
  │                                                                │
  │  4. MATURATION                                                 │
  │     EPS matrix: Polysaccharides, proteins, eDNA                │
  │     Alginate (P. aeruginosa): Viscous capsule                  │
  │     Pel, Psl (P. aeruginosa): Structural scaffold              │
  │     eDNA (extracellular DNA): Structural, also gene reservoir  │
  │                                                                │
  │  5. DISPERSAL                                                  │
  │     Subpopulation releases planktonic cells                    │
  │     Triggered by: nutrient limitation, low O₂, c-di-GMP fall   │
  │     Dispersal: Spreads infection to new sites                  │
  │                                                                │
  └────────────────────────────────────────────────────────────────┘

  ANTIBIOTIC RESISTANCE IN BIOFILMS:
  ─ 100–1,000x higher MIC than planktonic cells
  ─ WHY:
    (1) Diffusion barrier: EPS slows antibiotic penetration
    (2) Oxygen gradients: Deep cells anaerobic → most antibiotics
        require active metabolism + growth to work
    (3) Persister cells: Subpopulation of slow/non-growing cells
        → Tolerant (not resistant genetically) → regrow after treatment
    (4) Altered gene expression: Biofilm cells express different
        efflux pumps, stress responses
  ─ Clinical implications: Cystic fibrosis lung (P. aeruginosa biofilm),
    prosthetic joint infections, catheter infections, dental plaque
    → Often UNCURABLE without device removal
```

---

## Quorum Sensing in Ecological Context

```
  QUORUM SENSING: DENSITY-DEPENDENT GENE REGULATION
  ===================================================

  See also: 00-OVERVIEW.md (CS framing as distributed consensus algorithm)

  ECOLOGICAL SIGNIFICANCE:
  Quorum sensing synchronizes population behaviors to be ecologically effective
  only when cell numbers are sufficient to make behavior worthwhile.

  EXAMPLE: Vibrio fischeri (bioluminescence)
  ┌────────────────────────────────────────────────────────────────┐
  │  V. fischeri lives in light organ of bobtail squid (symbiosis) │
  │                                                                │
  │  Low density (in seawater):                                    │
  │  LuxI → low [AHL] (N-acyl homoserine lactone autoinducer)      │
  │  LuxR (receptor) not activated → no luciferase genes expressed │
  │  → No bioluminescence (no point — won't be visible)            │
  │                                                                │
  │  High density (inside squid light organ):                      │
  │  [AHL] accumulates → binds LuxR → LuxR activates luxICDABE     │
  │  → Luciferase expressed → bioluminescence                      │
  │  → Squid uses light for counter-illumination (camouflage)      │
  │                                                                │
  │  Cost: Produces AHL constantly at low density (waste)          │
  │  Payoff: Coordinates behavior for mutualistic function         │
  └────────────────────────────────────────────────────────────────┘

  SIGNALING MOLECULES BY CLASS:
  ─ AHL (acyl-homoserine lactones): Gram-negative intraspecies QS
  ─ AIP (autoinducing peptides): Gram-positive (Staphylococcus agr system)
  ─ AI-2 (autoinducer-2): LuxS-derived; interspecies (universal)
    → Present in both Gram+ and Gram- → cross-species communication
  ─ PQS (Pseudomonas quinolone signal): P. aeruginosa additional layer
    (has THREE QS systems: las, rhl, pqs — hierarchical control)

  ECOLOGICAL QS FUNCTIONS:
  ─ Biofilm formation: QS triggers transition to sessile life
  ─ Virulence factor production: P. aeruginosa LasA/LasB proteases, elastase
  ─ Sporulation coordination (Myxococcus): Entire colony coordinates
  ─ Bioluminescence (V. fischeri)
  ─ Competence for transformation (S. pneumoniae)
  ─ Antibiotic production (Streptomyces): QS coordinates antibiotic release
  ─ Swarming motility: Coordinated movement on surfaces

  QUORUM QUENCHING:
  Lactonases/acylases: Enzymes (from other bacteria) that degrade AHLs
  → Competition: Interfere with neighbors' QS circuits
  → Biotechnology: Quorum quenching as anti-virulence strategy
    (QQ compounds + biofilms + Pseudomonas infections: clinical trials)
```

---

## Soil Microbiome

```
  SOIL: THE MOST MICROBIALLY COMPLEX ECOSYSTEM
  ==============================================

  1 gram of soil: ~10⁸–10⁹ bacteria + 10⁴–10⁵ fungal cells
                  ~10,000 bacterial species (16S) per gram
  Total soil bacteria: ~10²⁵ cells in top 10 cm globally

  SOIL MICROBIOME ZONES:
  ┌────────────────────────────────────────────────────────────────┐
  │ RHIZOSPHERE: Root-associated zone                              │
  │   Root exudates (sugars, amino acids, organic acids) —         │
  │   up to 40% of photosynthetically fixed carbon released here   │
  │   Microbial density 10–100x higher than bulk soil              │
  │   Recruited community: More Proteobacteria/Actinobacteria      │
  │                                                                │
  │ RHIZOPLANE: Root surface itself                                │
  │   Tight adherence; biofilm-like communities                    │
  │   Nitrogen fixers (Rhizobium in legume root nodules)           │
  │                                                                │
  │ BULK SOIL: Away from roots                                     │
  │   Oligotrophic conditions → Acidobacteria dominate             │
  │   Low nutrient → slow-growing specialists                      │
  │                                                                │
  │ MYCORRHIZAL ZONE:                                              │
  │   Fungi colonize roots → massive hyphal networks               │
  │   Mycorrhizal network: "Wood wide web" — connects trees        │
  │   Transfer: C from tree → fungus; P/N from fungus → tree       │
  └────────────────────────────────────────────────────────────────┘

  SOIL ECOLOGY KEY ORGANISMS:
  ─ Bacillus: Sporulating; survives desiccation; B. subtilis model organism
  ─ Streptomyces: Antibiotic producers (most clinical antibiotics discovered here)
    Actinomycetes: Earthy soil smell = geosmin (isoprenoid) from Streptomyces
  ─ Nitrospira, Nitrobacter: Nitrifiers (NO₂⁻ → NO₃⁻)
  ─ Pseudomonas: Metabolic versatile; bioremediation workhorse
  ─ Rhizobium, Bradyrhizobium: Root-nodule nitrogen fixers
  ─ Mycorrhizal fungi: Glomus, Rhizophagus — phosphate mobilizers
  ─ Trichoderma: Fungal biocontrol agent; suppresses pathogens

  SOIL HEALTH METRICS (connecting to agriculture):
  ─ Microbial biomass carbon (MBC): mg C/kg soil
  ─ Enzyme activities: Urease, phosphatase, dehydrogenase
  ─ Diversity indices: qPCR + 16S amplicon
  ─ PLFA (phospholipid fatty acid) profiling
  ─ Healthy soil = high diversity + high function
  ─ Conventional agriculture: Reduced diversity vs. organic/no-till
```

---

## Marine Microbiology

```
  OCEAN MICROBIOME
  =================

  Oceans = ~71% of Earth's surface; largest habitable volume
  ~10²⁹ microbial cells in ocean; ~10³⁰ viruses (10x more than cells)

  MARINE MICROBIAL ZONES:
  ┌────────────────────────────────────────────────────────────────┐
  │ PHOTIC ZONE (0–200 m): Sun-lit; photosynthetic primary prod.   │
  │   Picoplankton: <2 μm; dominates biomass                       │
  │   Prochlorococcus: Most abundant photosynthetic organism       │
  │   on Earth; chlorophyll b/b₂ variant; ~10⁵ cells/mL            │
  │   Synechococcus: Slightly larger; broader geographic range     │
  │   Together: ~25% of global primary production                  │
  │                                                                │
  │ MESOPELAGIC (200–1000 m): Twilight zone; organic export        │
  │   Biological pump: Sinking particles carry fixed C down        │
  │   Bacteria remineralize: C→CO₂ before reaching deep            │
  │   SAR11 clade (Pelagibacter): Most abundant organism on Earth  │
  │   ~25% of marine bacterial cells; ultra-oligotrophic adapted   │
  │                                                                │
  │ DEEP SEA (>1000 m): Dark, cold, high pressure                  │
  │   Archaea dominate by cell number (Thaumarchaeota)             │
  │   Chemolithotrophs near hydrothermal vents                     │
  │   Vent ecosystems: Independent of sunlight energy              │
  │                                                                │
  │ HYDROTHERMAL VENTS:                                            │
  │   Sulfide-rich fluids (400°C); temperature gradient            │
  │   Sulfur-oxidizing bacteria (Thiomicrorhabdus, Beggiatoa)      │
  │   → Fix CO₂ via Calvin cycle using H₂S as electron donor       │
  │   → Primary production without sun → supports tube worms,      │
  │     crabs, shrimp in complete darkness                         │
  └────────────────────────────────────────────────────────────────┘

  MARINE VIRAL DYNAMICS:
  ─ ~10³⁰ viruses in ocean; every mL seawater has ~10⁷ viruses
  ─ Viral shunt: ~20–40% of marine bacteria killed daily by phage
  ─ → Instead of carbon flowing up food chain, it re-enters dissolved pool
  ─ → Stimulates bacterial production; short-circuits biological pump
  ─ SAR11 virophages: Constant arms race; major evolutionary pressure
  ─ Giant viruses (Mimivirus, Pandoravirus): Discovered in marine sediments
    Genome >1 Mb; larger than some bacteria; contain own tRNA genes

  TARA OCEANS (2009–2012):
  ─ Circumnavigation; collected 35,000+ samples
  ─ 40 million new microbial genes identified
  ─ Ocean Metagenome Reference Catalogue (2019): 195 million non-redundant genes
  ─ Reveals: Majority of ocean microbial genes have no known function
```

---

## Biogeochemical Cycles

```
  THE MICROBIAL ENGINE OF BIOGEOCHEMICAL CYCLES
  ===============================================

  NITROGEN CYCLE:
  ┌────────────────────────────────────────────────────────────────┐
  │   N₂ (atmospheric, 78%)                                        │
  │      │ NITROGEN FIXATION (only bacteria + archaea)             │
  │      ▼ Nitrogenase enzyme: N₂ + 8H⁺ + 16ATP → 2NH₃ + H₂        │
  │   NH₄⁺ (ammonium)                                              │
  │      │ NITRIFICATION (aerobic autotrophs)                      │
  │      │ Step 1: NH₄⁺ → NO₂⁻  (Nitrosomonas, Thaumarchaeota)     │
  │      │ Step 2: NO₂⁻ → NO₃⁻  (Nitrospira, Nitrobacter)          │
  │      ▼                                                         │
  │   NO₃⁻ (nitrate — plant-available form)                        │
  │      │ DENITRIFICATION (anaerobic heterotrophs)                │
  │      │ NO₃⁻ → NO₂⁻ → NO → N₂O → N₂                             │
  │      │ Pseudomonas, Paracoccus, Bacillus                       │
  │      ▼                                                         │
  │   N₂ (returns to atmosphere)                                   │
  │                                                                │
  │ ANAMMOX (anaerobic ammonium oxidation): Planctomycetes         │
  │   NH₄⁺ + NO₂⁻ → N₂ + H₂O (no O₂ needed)                        │
  │   Accounts for ~50% of oceanic N₂ production                   │
  └────────────────────────────────────────────────────────────────┘

  CARBON CYCLE:
  ─ Fixation: Cyanobacteria, purple/green bacteria (photoauto)
    + Chemolithotrophs (deep sea vents)
  ─ Decomposition: Bacteria + fungi → CO₂ + CH₄
    Anaerobic: Fermentation → acetate/H₂ → methanogens → CH₄
    Aerobic: Oxidation → CO₂
  ─ Biological pump (ocean): Sinking particles → carbon export to deep ocean
    ~2–12 Gt C/year export; slows atmospheric CO₂ accumulation
  ─ Permafrost thaw: ~1,500 Gt C frozen; methanogenic archaea release CH₄ as
    permafrost thaws → climate feedback loop

  SULFUR CYCLE:
  ─ Dissimilatory sulfate reduction: Desulfovibrio
    SO₄²⁻ + organic carbon → H₂S + CO₂ (anaerobic sediments)
  ─ Sulfur oxidation: Thiobacillus, Beggiatoa
    H₂S → S⁰ → SO₄²⁻ (aerobic or using nitrate)
  ─ DMS (dimethylsulfide): Marine phytoplankton produce DMSP
    Bacteria convert DMSP → DMS → released to atmosphere
    → Cloud nucleation → climate regulation (CLAW hypothesis)

  IRON CYCLE:
  ─ Iron-reducing bacteria: Geobacter, Shewanella
    Fe³⁺ → Fe²⁺ (anaerobic; significant in sediments + groundwater)
  ─ Iron-oxidizing bacteria: Gallionella, Leptothrix
    Fe²⁺ → Fe³⁺ (at oxic/anoxic interfaces)
  ─ Acid mine drainage: Acidithiobacillus ferrooxidans
    Pyrite (FeS₂) oxidation → H₂SO₄ + Fe³⁺ → highly acidic drainage
    Iron oxidation accelerated 10⁶x by bacterial activity vs. abiotic
```

---

## Extreme Environment Microbiology

```
  LIFE AT THE EDGES
  ==================

  THE CONCEPT: EVERY EXTREME ENVIRONMENT ON EARTH HAS A SPECIALIST
  Implication: Life's biochemistry is more flexible than standard biology suggests

  DEEP SUBSURFACE:
  ─ Bacteria and archaea found 5 km below surface
  ─ Some with doubling times of thousands of years (not dormant — active)
  ─ "Deep biosphere" may equal surface biomass
  ─ Energy: H₂ from water-rock reactions (serpentinization)
    2H₂O + 3FeO → Fe₃O₄ + H₂ (simplified)
    → Chemolithotrophs use H₂ as electron donor, CO₂ as carbon source
  ─ Implications: Life on other rocky planets plausible

  ACID ENVIRONMENTS:
  ─ Rio Tinto, Spain: pH ~2, high Fe, red river color
  ─ Acidithiobacillus, Ferroplasma: Active at pH 0–2
  ─ Internal pH still neutral: They pump out protons actively
  ─ AMD (acid mine drainage): Ecologically devastating; bioremediation challenge

  HYPERSALINE:
  ─ Dead Sea (30–35% salt), Brine Lakes (>40% NaCl)
  ─ Halophilic archaea: Halobacterium, Haloarcula
  ─ Adaptation: Accumulate K⁺ inside (salt-in strategy)
    OR accumulate compatible solutes (betaine, ectoine — salt-out strategy)
  ─ Bacteriorhodopsin: Light-driven proton pump; alternative photosynthesis
    → used in optogenetics research

  PERMAFROST AND CRYOSPHERE:
  ─ Active bacteria at −20°C (in brine films between ice crystals)
  ─ Permafrost thaw → release of ancient microbes + ancient carbon
  ─ Discovered in 30,000-year-old permafrost: Giant Pithovirus (viable after thaw)
  ─ Subglacial Lake Vostok (Antarctica): Microbial life in isolated lake
    under 4 km of ice; ~15 million years isolated; ~3,500 species detected

  RADIATION-RESISTANT:
  ─ Deinococcus radiodurans: Survives 5,000 Gy (10 Gy kills human)
  ─ Mechanism: Remarkable DNA repair; 10 copies of chromosome in one cell
    → reconstruct genome from fragments (reassembly in ~24 hours)
  ─ Polyextremophile: Also tolerates desiccation, H₂O₂, UV
  ─ Biotechnology: Engineering for bioremediation of radioactive waste sites
```

---

## Microbial Community Dynamics

```
  ECOLOGICAL PRINCIPLES IN MICROBIAL COMMUNITIES
  ================================================

  COMPETITIVE EXCLUSION (Gause's principle):
  Two species competing for identical niche cannot coexist
  BUT: Microbial communities have 1,000+ "species" in same gut
  Resolution: Niche differentiation — no two species have identical niche
  Coexistence mechanisms: Cross-feeding, spatial structure, temporal variation

  SYNTROPHY: OBLIGATE METABOLIC COOPERATION
  ┌────────────────────────────────────────────────────────────────┐
  │ Syntrophic acetate-oxidizing bacteria (SAOB) + methanogens:    │
  │                                                                │
  │ SAOB:   Acetate → H₂ + CO₂  (thermodynamically unfavorable)    │
  │ Methanogen: H₂ + CO₂ → CH₄  (removes H₂ → drives SAOB)         │
  │                                                                │
  │ Only works together — neither survives alone in this niche     │
  │ H₂ transfer at nanometer scale (interspecies electron transfer)│
  │ Also: Direct interspecies electron transfer (DIET) via pili    │
  │ Example: Geobacter-Methanosaeta consortia in anaerobic sludge  │
  └────────────────────────────────────────────────────────────────┘

  MUTUALISM AND SYMBIOSIS SPECTRUM:
  ─ Obligate mutualism: Lichens (fungus + algae/cyanobacteria)
  ─ Facultative mutualism: Root nodule N-fixers
  ─ Commensalism: Most gut bacteria (benefit host; host neutral)
  ─ Parasitism: Pathogens
  ─ Amensalism: Antibiotic production by Streptomyces → kills competitors

  MICROBIAL SUCCESSION:
  ─ Exposed rock → pioneer bacteria (cyanobacteria, Azotobacter)
  ─ Create organic matter + fix N₂ → enable plant colonization
  ─ Wound infection: Early aerobic organisms → consume O₂
    → creates anaerobic niche → anaerobes establish
  ─ Cheese ripening: Sequential microbial communities
    Starter cultures → secondary surface molds → final flavor organisms
```

---

## Decision Cheat Sheet

| Concept | Key Point |
|---------|-----------|
| Second messenger for biofilm | c-di-GMP: HIGH → biofilm; LOW → planktonic |
| Biofilm antibiotic resistance | 100–1000x MIC; persister cells + diffusion barrier |
| QS autoinducer in Gram-negative | AHL (acyl-homoserine lactone); sensed by LuxR family |
| QS in Gram-positive | Autoinducing peptides (AIP); e.g., Staph agr system |
| Most abundant photosynthetic organism | Prochlorococcus in ocean |
| Most abundant bacterium on Earth | SAR11 (Pelagibacter) in ocean |
| Where to find nitrogen fixation? | Root nodules, wetlands, termite guts, ocean (Trichodesmium) |
| Anammox: why important? | ~50% of oceanic N₂ production; no O₂ required |
| Deep biosphere | Life at 5+ km depth; doubling times in thousands of years |
| Deinococcus radiodurans superpower | Survives 5,000 Gy; reconstructs shattered genome |
| Viral shunt in ocean | Phage kill 20–40% bacteria/day; carbon stays dissolved |
| Syntrophy definition | Obligate metabolic cooperation; neither partner survives alone |

---

## Common Confusion Points

**"Microbes are simple organisms in simple communities"**: A gram of soil contains more metabolic diversity than all of human biochemistry combined. Microbial communities exhibit predation (Bdellovibrio), syntrophy, chemical warfare (antibiotics), social behavior (biofilms, QS), and evolutionary dynamics on human-observable timescales.

**Biofilm tolerance vs. resistance**: Biofilm bacteria are not genetically resistant to antibiotics — they are phenotypically tolerant. After dispersal, planktonic cells from a biofilm are just as antibiotic-sensitive as their ancestors. Persister cells are also phenotypically tolerant (not genetically resistant) — they regrow when antibiotics are removed, then new persisters form from the population. Resistance and tolerance are mechanistically distinct.

**Quorum sensing threshold in real environments**: In flowing aquatic environments, autoinducers are diluted away. QS works in microenvironments, biofilms, host tissues, and slow-moving environments. In the ocean, the typical cell density is too low for population-wide QS — it mostly occurs in aggregates and particles.

**Nitrogen fixation is O₂-sensitive**: Nitrogenase is irreversibly destroyed by O₂. This creates a paradox for aerobic nitrogen fixers — they need O₂ for energy but must protect nitrogenase. Solutions: (1) Legume root nodules: Leghemoglobin sequesters O₂, keeps internal pO₂ low; (2) Cyanobacteria: Heterocysts — specialized cells with thick wall + exclude O₂; (3) Temporal separation: Fix N₂ at night, photosynthesize during the day.
