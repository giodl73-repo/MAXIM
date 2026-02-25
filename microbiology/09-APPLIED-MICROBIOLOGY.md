# Applied Microbiology

## The Big Picture

```
APPLIED MICROBIOLOGY: MICROBES AS INDUSTRIAL ASSETS
=====================================================

  Microbes are the original chemical engineers.
  Industrial biotechnology: ~$400 billion/year global market.

  ┌─────────────────────────────────────────────────────────────────┐
  │  APPLICATION SECTORS                                             │
  │                                                                   │
  │  FOOD + BEVERAGE:    Fermentation — bread, cheese, beer, wine  │
  │                      Yogurt, vinegar, miso, tempeh, kimchi      │
  │                      ~$250 billion food fermentation market     │
  │                                                                   │
  │  PHARMACEUTICALS:   Antibiotics (penicillin, streptomycin)     │
  │                      Insulin (E. coli / S. cerevisiae)          │
  │                      Biologics: mAbs in CHO cells               │
  │                      Vaccines: yeast-produced HBsAg, HPV VLPs  │
  │                                                                   │
  │  INDUSTRIAL ENZYMES: Proteases (detergent), lipases,           │
  │                       amylases (starch), cellulases (biofuel)   │
  │                       ~$6 billion/year market                   │
  │                                                                   │
  │  BIOFUELS:           Ethanol (Saccharomyces, E. coli)          │
  │                       Butanol, isobutanol, fatty acids          │
  │                       Algal biodiesel                           │
  │                                                                   │
  │  BIOREMEDIATION:     Petroleum degradation (Pseudomonas)        │
  │                       Heavy metal reduction (Geobacter)         │
  │                       Chlorinated solvent degradation           │
  │                                                                   │
  │  SYNTHETIC BIOLOGY:  Engineered chassis; non-natural products  │
  │                       Biosensors; programmable living medicines │
  └─────────────────────────────────────────────────────────────────┘
```

---

## Industrial Fermentation

```
  FERMENTATION TECHNOLOGY
  ========================

  HISTORY + MODERN CONTEXT:
  Fermentation = oldest biotechnology (>10,000 years — Neolithic brewing)
  Modern industrial fermentation: Precision-controlled bioreactors
  Key realization (1940s): Same microbial biochemistry = both bread AND antibiotics

  PENICILLIN: THE FERMENTATION REVOLUTION
  ┌────────────────────────────────────────────────────────────────┐
  │  1928: Fleming observes Penicillium mold killing Staphylococcus│
  │  1940: Florey/Chain purify penicillin (Oxford)               │
  │  1943: Industrial production using Penicillium chrysogenum    │
  │  Problem: Original yield: 2 units/mL → insufficient          │
  │  Solution: Strain improvement + fermentation optimization      │
  │   ─ UV mutagenesis → higher-yielding mutants                 │
  │   ─ Corn steep liquor as medium component (key discovery)     │
  │   ─ Submerged deep-tank fermentation (not surface culture)    │
  │   ─ Oxygen supply: Aeration + agitation critical              │
  │  Result: 100,000 units/mL by end of WWII                     │
  │  Modern titers: >50 g/L (25 million-fold improvement!)       │
  │                                                                 │
  │  Still produced by fermentation: Penicillium chrysogenum      │
  │  ~60,000 tonnes of penicillin/year globally                  │
  └────────────────────────────────────────────────────────────────┘

  BIOREACTOR TYPES:
  ┌────────────────────────────────────────────────────────────────┐
  │ STIRRED TANK REACTOR (STR): Industry standard                 │
  │   Agitator: Impeller breaks air bubbles; mixes nutrients      │
  │   Sparger: Introduces sterile air/O₂                         │
  │   Sensors: pH, dissolved O₂, temperature, pressure, turbidity │
  │   Scale: 10 L (lab) → 100,000 L (industrial)                │
  │   Challenge: Mixing at large scale; O₂ transfer limitation   │
  │                                                                 │
  │ FED-BATCH (most common for high-density culture):             │
  │   Start: Low substrate concentration                          │
  │   Feed: Continuous or periodic substrate addition            │
  │   → Prevents substrate inhibition (glucose repression)       │
  │   → Achieves very high cell density                          │
  │   E. coli: 80–120 g/L dry cell weight achievable             │
  │                                                                 │
  │ CONTINUOUS (CHEMOSTAT):                                        │
  │   Continuous feed-in + overflow-out                          │
  │   Steady state: Growth rate = dilution rate (D = μ)          │
  │   Selects for fastest-growing mutants over time              │
  │   Use: Research; some industrial cheese/beer production       │
  │                                                                 │
  │ AIRLIFT: No mechanical agitator; air circulates broth        │
  │   Gentle mixing → shear-sensitive organisms (plant cells)    │
  └────────────────────────────────────────────────────────────────┘

  DOWNSTREAM PROCESSING (DSP): Often >50% of total cost
  ─ Cell harvest: Centrifugation or filtration (tangential flow)
  ─ Cell disruption (if intracellular product): High-pressure homogenizer
  ─ Purification: Chromatography (ion exchange, hydrophobic, size, affinity)
  ─ Concentration + formulation: UF/DF, lyophilization
  ─ Quality control: Bioburden, endotoxin (LAL test), potency assays
```

---

## Food Fermentation

```
  THE MICROBIOLOGY OF FERMENTED FOODS
  =====================================

  BEER + WINE (connection to fermentation-spirits/ in reference library):
  ─ Saccharomyces cerevisiae: Primary fermentor (ale yeast top-ferments 18–22°C)
  ─ S. pastorianus (carlsbergensis): Lager yeast (bottom-ferments 8–14°C)
    Hybrid of S. cerevisiae × S. eubayanus
  ─ Beer: Glucose → ethanol + CO₂ (Embden-Meyerhof pathway + PDC + ADH)
  ─ Malolactic fermentation (wine): Oenococcus oeni → Malic acid → Lactic acid
    → Reduces sharp acidity; complexity; done after primary fermentation

  CHEESE (complex ecology):
  ┌────────────────────────────────────────────────────────────────┐
  │ STAGE          ORGANISMS               BIOCHEMISTRY            │
  │                                                                 │
  │ Primary ferm.  Lactococcus lactis      Lactose → lactic acid   │
  │                Lactobacillus spp.      pH drop → casein coag.  │
  │                                                                 │
  │ Surface molds  Penicillium camemberti  Brie/Camembert: white   │
  │                Penicillium roqueforti  Blue cheese: blue veins │
  │                                        Lipolysis → flavor      │
  │                                                                 │
  │ Smear/wash     Brevibacterium linens   Limburger, Munster       │
  │ rind           Arthrobacter spp.       Orange rind; methanethiol│
  │                                                                 │
  │ Aging (long)   Propionibacterium       Swiss/Emmental eyes      │
  │                freudenreichii          Propionic acid + CO₂    │
  └────────────────────────────────────────────────────────────────┘

  YOGURT + FERMENTED DAIRY:
  ─ Starter: Streptococcus thermophilus + Lactobacillus bulgaricus (symbiotic)
  ─ S. thermophilus: Provides CO₂ + formate → stimulates L. bulgaricus
  ─ L. bulgaricus: Protease activity → provides amino acids → stimulates S. therm.
  ─ Both produce lactic acid → pH 4.0–4.5 → gel formation
  ─ Acetaldehyde: Key flavor compound (L. bulgaricus primary source)

  SOURDOUGH:
  ─ Wild-capture community: Lactobacillus sourdough species + wild yeasts
  ─ Lactobacillus sanfranciscensis (now: Fructilactobacillus sanfranciscensis)
  ─ Organic acids: Acetic + lactic acid (ratio determines taste profile)
  ─ Phytase activity: Breaks down phytic acid → increases mineral availability
  ─ Long fermentation → lower glycemic index (acid modifies starch structure)

  VINEGAR:
  ─ Two-stage process:
    Stage 1: Yeasts → ethanol (anaerobic fermentation)
    Stage 2: Acetobacter aceti → oxidizes ethanol → acetic acid (aerobic)
  ─ Acetobacter: Obligate aerobe; surface or submerged aeration processes
  ─ Traditional: Open vat; Orleans process (slow, surface culture)
  ─ Industrial: Frings acetator (submerged; fine bubble aeration; fast)
```

---

## Bioremediation

```
  BIOREMEDIATION: MICROBES CLEANING UP HUMAN MESSES
  ===================================================

  CONCEPT: Use microbial metabolic capabilities to degrade or immobilize
  environmental contaminants. Exploits naturally occurring pathways.

  HYDROCARBON DEGRADATION:
  ┌────────────────────────────────────────────────────────────────┐
  │ PETROLEUM HYDROCARBONS: Major environmental contaminants      │
  │                                                                 │
  │ AEROBIC DEGRADATION:                                           │
  │   Initial attack: Oxygenases (monooxygenase or dioxygenase)  │
  │   → Introduce -OH groups → activate for β-oxidation pathway  │
  │   Key organisms: Pseudomonas putida (toluene, xylene, naphthalene)│
  │                  Rhodococcus (aromatic + aliphatic)           │
  │                  Marinobacter (marine hydrocarbons)           │
  │                                                                 │
  │ DEEPWATER HORIZON (2010): Field case study                    │
  │   200 million gallons crude oil → Gulf of Mexico             │
  │   Autochthonous (native) hydrocarbon-degrading bacteria bloom │
  │   Oceanospirillales, Colwellia, Cycloclasticus                │
  │   Dramatic increase in hydrocarbon-degrading populations     │
  │   → Biodegraded much of deep plume before reaching surface    │
  │   BUT: Dispersant (Corexit) reduced biodegradation in some   │
  │        studies (toxicity to degraders + oil bioavailability)  │
  └────────────────────────────────────────────────────────────────┘

  CHLORINATED SOLVENT DEGRADATION:
  ─ PCE (tetrachloroethylene), TCE (trichloroethylene): Common groundwater pollutants
    (dry-cleaning fluids; industrial solvents)
  ─ Reductive dechlorination:
    PCE → TCE → cis-DCE → vinyl chloride → ethylene (non-toxic)
  ─ Dehalococcoides mccartyi: OBLIGATE organohalide respirer
    Uses chlorinated compounds as terminal electron acceptor
    Requires: H₂ (provided by fermenting organisms in consortium)
  ─ Bioaugmentation: Add Dehalococcoides culture to contaminated site
  ─ Biostimulation: Add electron donor (molasses, lactate) → stimulate native
    Dehalococcoides already present

  HEAVY METAL BIOREMEDIATION:
  ─ Uranium: Geobacter sulfurreducens reduces soluble U(VI) → insoluble U(IV)
    → Uranium precipitates → immobilized (not degraded but immobilized)
    UMTRA project: Field biostimulation with acetate → Geobacter bloom → U removal
  ─ Mercury: Merb gene (organomercury lyase) + MerA (mercuric reductase)
    → Convert methylmercury → inorganic Hg → Hg⁰ (volatile; leaves soil)
  ─ Arsenic: As(III) oxidizers: Agrobacterium tumefaciens aioA
    As(V) reducers: arr genes; convert mobile As(V) → potentially mobile As(III)
    Complex; oxidation preferred for immobilization

  BIOPLASTICS:
  ─ PHAs (polyhydroxyalkanoates): Intracellular carbon storage polymers
  ─ PHB (polyhydroxybutyrate): Produced by Cupriavidus necator from CO₂/H₂ or
    organic carbon under nitrogen limitation
  ─ Properties: Thermoplastic; biodegradable; similar to polypropylene
  ─ Limitation: High production cost vs. petroleum plastics
  ─ Advances: Metabolic engineering → novel PHA compositions; co-products
```

---

## Synthetic Biology

```
  SYNTHETIC BIOLOGY: ENGINEERING MICROBES AS PROGRAMMABLE SYSTEMS
  =================================================================

  PARADIGM SHIFT: From studying biological systems → designing them
  Engineering approach: Design, build, test, iterate (same as software)

  KEY CHASSIS ORGANISMS:
  ┌────────────────────────────────────────────────────────────────┐
  │ Escherichia coli K-12 (MG1655, BL21, DH5α):                  │
  │   Advantages: Fast growth, well-characterized, extensive tools│
  │   Genetic tools: >5,000 characterized promoters, ribosome    │
  │   binding sites, terminators in registries                    │
  │   Insulin production: 1982, first recombinant biologic       │
  │   Protein overexpression: T7 system (pET vectors)            │
  │   Limitations: Doesn't glycosylate proteins; inclusion bodies │
  │                at high expression; endotoxin in products     │
  │                                                                 │
  │ Saccharomyces cerevisiae:                                      │
  │   Advantages: Post-translational modifications; GRAS status  │
  │   Established: Hepatitis B vaccine (HBsAg, 1986)            │
  │   HPV vaccine (VLP): VLPs assembled in yeast                 │
  │   Artemisinic acid: Amyris engineered yeast (see below)      │
  │   Tools: CRISPR-Cas9 very efficient; strong selection markers │
  │                                                                 │
  │ Bacillus subtilis:                                             │
  │   Industrial enzyme production (amylases, proteases)          │
  │   Gram-positive: Secretes directly to media (easy purification)│
  │   GRAS status; no endotoxin                                   │
  │                                                                 │
  │ Pichia pastoris (now: Komagataella phaffii):                  │
  │   Yeast with methanol-inducible promoter (AOX1): Ultra-strong │
  │   Secreted proteins; glycosylation; high-density fermentation │
  │   Used for: Insulin, EPO, mAb fragments                      │
  │                                                                 │
  │ Chinese Hamster Ovary (CHO) cells:                            │
  │   Mammalian: Human-like glycosylation → therapeutic mAbs     │
  │   ~70% of biologic drugs produced in CHO                     │
  │   Technically cell culture, not microbe; included for context │
  └────────────────────────────────────────────────────────────────┘

  SYNTHETIC BIOLOGY CASE STUDIES:
  ┌────────────────────────────────────────────────────────────────┐
  │ ARTEMISININ (antimalarial): The landmark project              │
  │   Plant-derived: Artemisia annua (sweet wormwood)            │
  │   Problem: Plant supply unreliable; price volatile            │
  │   Keasling lab (2006, Nature): Engineered S. cerevisiae       │
  │   → Mevalonate pathway extended to artemisinic acid           │
  │   → Amyris commercialized (2013): Semisynthetic artemisinin  │
  │   → Stable supply; reduced drug cost                         │
  │                                                                 │
  │ SHIKIMATE PATHWAY PRODUCTS:                                    │
  │   Shikimic acid: Oseltamivir (Tamiflu) precursor             │
  │   Original: Star anise (limited supply during H5N1 fears)    │
  │   Engineered E. coli: Roche-independent supply               │
  │   Amino acid analogs, flavonoids, stilbenes via same pathway  │
  │                                                                 │
  │ INSULIN PRODUCTION:                                            │
  │   1982: Humulin (Eli Lilly × Genentech) — first recombinant   │
  │   drug; E. coli expression                                    │
  │   A-chain + B-chain expressed separately → combined → fold   │
  │   Now: Mostly S. cerevisiae or P. pastoris (native-like)     │
  │   mRNA-based insulin: In development (not approved yet)      │
  └────────────────────────────────────────────────────────────────┘

  GENETIC PARTS REGISTRY (iGEM BioBrick Standard):
  ─ Parts = standardized genetic elements (promoters, RBS, CDS, terminators)
  ─ Assembly: RFC 10 standard; BioBrick prefix+suffix restriction sites
  ─ Registry: registry.igem.org; >20,000 standard parts contributed
  ─ iGEM Competition: Undergraduate teams using standard parts
  ─ Golden Gate Assembly: More modern; BsaI type IIS restriction enzyme
  ─ Gibson Assembly: Isothermal; seamless joining; no restriction sites needed

  GENETIC CIRCUITS — FROM BIOLOGY TO ENGINEERING:
  ┌────────────────────────────────────────────────────────────────┐
  │ Toggle Switch (Gardner 2000, Nature):                          │
  │   Two mutually repressing promoters → bistable system         │
  │   Promoter1 → repressor2; Promoter2 → repressor1             │
  │   → Two stable states; switched by inducer pulses             │
  │   → Proof that synthetic genetic bistability possible         │
  │                                                                 │
  │ Repressilator (Elowitz 2000, Nature):                          │
  │   Three repressors in a ring: LacI → TetR → CI → LacI        │
  │   → Oscillations (~150 min period) — first synthetic clock   │
  │   → Later improved: Sicker oscillator with >1000 hours stable │
  │                                                                 │
  │ AND gates, NOR gates: Implemented with transcription factors  │
  │ Multi-layer circuits: Cascade amplification; coherent FFLs    │
  └────────────────────────────────────────────────────────────────┘
```

---

## Probiotics and Clinical Evidence

```
  PROBIOTICS: EVIDENCE-BASED REVIEW
  ===================================

  DEFINITION (WHO): "Live microorganisms that, when administered in
  adequate amounts, confer a health benefit on the host"

  KEY SPECIES IN USE:
  ─ Lactobacillus rhamnosus GG (LGG): Most studied single strain
  ─ Lactobacillus acidophilus NCFM: Common in supplements
  ─ Bifidobacterium longum, B. animalis subsp. lactis Bb12
  ─ Saccharomyces boulardii: Non-colonizing yeast probiotic
  ─ Lactobacillus reuteri DSM17938: Infantile colic

  EVIDENCE STRENGTH BY INDICATION:
  ┌────────────────────────────────────────────────────────────────┐
  │ STRONG EVIDENCE:                                               │
  │   Acute infectious diarrhea: LGG, S. boulardii               │
  │   → Meta-analysis: 1 day reduction in duration (Cochrane)    │
  │   AAD (antibiotic-associated diarrhea): S. boulardii + LGG   │
  │   → NNT ~13 (not dramatic but consistent effect)             │
  │   C. diff prevention: S. boulardii during antibiotic course  │
  │   → Reduced CDI recurrence (not primary prevention)          │
  │   Pouchitis (UC after colectomy): VSL#3 (8-strain mixture)  │
  │   → Only approved probiotic for a specific GI condition      │
  │                                                                 │
  │ MODERATE EVIDENCE:                                             │
  │   IBS: Multi-strain products; symptom reduction in some trials│
  │   Infantile colic: L. reuteri DSM17938 → reduced crying time │
  │   Necrotizing enterocolitis prevention (premature infants):   │
  │   → Multiple Cochrane analyses favor probiotic use            │
  │   → Many NICUs now use routinely                             │
  │                                                                 │
  │ WEAK / INSUFFICIENT EVIDENCE:                                  │
  │   Depression/anxiety: Small trials; promising but not enough  │
  │   Obesity: No consistent clinical benefit yet                 │
  │   Atopic dermatitis: Prevention in at-risk infants: modest   │
  │   Systemic infection prevention: Not demonstrated in most     │
  │   populations; CAUTION in immunocompromised (sepsis risk)    │
  └────────────────────────────────────────────────────────────────┘

  MECHANISM:
  ─ Competitive exclusion: Outcompete pathogens for binding sites
  ─ Barrier reinforcement: LGG → increases tight junction proteins
  ─ Immune modulation: TLR2/4 stimulation; Treg induction
  ─ Antimicrobial peptide production (bacteriocins, H₂O₂, organic acids)
  ─ S. boulardii: Secretes protease cleaving C. diff toxin A receptor

  POSTBIOTICS: EMERGING CONCEPT
  ─ Killed bacteria or bacterial products (metabolites, cell wall frags)
  ─ Advantage: No viability required → heat-killed, shelf-stable
  ─ Example: Pasteurized Akkermansia muciniphila (in Phase 1/2 trials 2024)
  ─ Better standardization + safety profile vs. live probiotics
```

---

## Decision Cheat Sheet

| Application | Organism | Key Product/Function |
|-------------|----------|---------------------|
| Penicillin production | Penicillium chrysogenum | β-lactam antibiotic; >50 g/L titers |
| Human insulin | E. coli / S. cerevisiae | First recombinant biologic (1982) |
| Hepatitis B vaccine | S. cerevisiae | HBsAg VLP; first recombinant vaccine |
| Malt whisky fermentation | S. cerevisiae | Ethanol; congener production |
| Blue cheese | Penicillium roqueforti | Lipolysis + flavor; blue veins |
| Swiss cheese eyes | Propionibacterium freudenreichii | CO₂ + propionic acid from lactate |
| Vinegar (stage 2) | Acetobacter aceti | Ethanol → acetic acid (aerobic) |
| Petroleum bioremediation | Pseudomonas putida | Oxygenase-mediated ring opening |
| Chlorinated solvent cleanup | Dehalococcoides mccartyi | Reductive dechlorination |
| Bioplastic | Cupriavidus necator | PHB from CO₂/H₂ under N-starvation |
| Artemisinin | Engineered S. cerevisiae | Mevalonate pathway extension |
| Anti-diarrhea probiotic | LGG, S. boulardii | Competitive exclusion; mucosal barrier |

---

## Common Confusion Points

**Natural vs. industrial fermentation**: "Fermentation" in biochemistry means anaerobic ATP production without external electron acceptor (glycolysis only). In industrial fermentation, the term is used loosely to mean any large-scale microbial process, including aerobic ones (penicillin fermentation is highly aerobic). Beer fermentation is technically fermentation in the biochemical sense; penicillin production is not.

**Biostimulation vs. bioaugmentation**: Biostimulation = add nutrients (electron donor/acceptor) to stimulate native organisms already present. Bioaugmentation = add specific organisms (like Dehalococcoides cultures) to a site. Both are used in bioremediation but applied to different scenarios: biostimulate when native organisms are present but limited; bioaugment when native population is insufficient or wrong species.

**Probiotic vs. prebiotic vs. synbiotic**: Probiotic = live organism. Prebiotic = non-digestible food component that selectively stimulates beneficial organisms (FOS, inulin, HMOs). Synbiotic = both together. The evidence base is strongest for specific probiotic-indication pairs. Blanket "probiotics are good" is not supported — strain specificity and indication specificity matter enormously.

**Why E. coli for biologics but CHO for mAbs?**: E. coli is excellent for simple proteins (insulin, growth hormone) — fast, cheap, high yield. But E. coli cannot glycosylate proteins. Most therapeutic antibodies (mAbs) REQUIRE correct human-like glycosylation for function (Fc receptor binding, half-life). CHO cells provide mammalian glycosylation. Trade-off: 10–100x more expensive to produce in CHO vs. E. coli. The field is engineering yeast to produce humanized glycosylation, which could change this economics.
