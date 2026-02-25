# Material Analysis in Archaeology

## The Big Picture

```
+------------------------------------------------------------------+
|              ANALYTICAL METHODS AND WHAT THEY ANSWER            |
|                                                                  |
|  Question                  Method                               |
|  ───────────────────────────────────────────────────────────── |
|  Where was this made?      XRF / EMPA / lead isotopes           |
|  What did they eat?        Stable isotopes (δ¹³C, δ¹⁵N)        |
|  Where did they live?      Sr/O isotopes (migration)            |
|  Who were they genetically?Ancient DNA (aDNA)                   |
|  What was in this vessel?  Lipid residue analysis               |
|  What plants were present? Phytoliths / pollen / seeds          |
|  What was the diet detail? Zooarchaeology + faunal analysis     |
|  What's the elemental comp? XRF (portable or lab)               |
+------------------------------------------------------------------+
```

---

## Stable Isotope Analysis

Stable isotopes are non-radioactive isotope pairs that fractionate predictably through biological and geological processes. Measured by IRMS (Isotope Ratio Mass Spectrometry).

### Carbon and Nitrogen Isotopes (Diet)

```
δ¹³C FRACTIONATION (diet reconstruction):
  C3 plants: wheat, barley, rice, most vegetables
    δ¹³C ≈ −26 to −24‰ (per mil, relative to VPDB standard)
  C4 plants: maize (corn), millet, sorghum, sugarcane
    δ¹³C ≈ −12 to −10‰ (different photosynthetic pathway)
  Marine protein: δ¹³C ≈ −12 to −20‰

  Human bone collagen δ¹³C reflects diet:
  → C3-dominated diet: ≈ −20 to −18‰
  → Heavy C4 (maize) diet: ≈ −12 to −8‰
  → Mixed marine/terrestrial: intermediate values

ARCHAEOLOGICAL APPLICATION:
  Tracking spread of maize agriculture in North America:
  δ¹³C shift in skeletal collagen records dietary change
  Temporal transects across regions document when maize became dietary staple

δ¹⁵N FRACTIONATION (trophic level):
  Each step up the food chain enriches ¹⁵N by ~3–4‰
  Plants: δ¹⁵N ≈ 0–5‰
  Herbivores: δ¹⁵N ≈ 3–9‰
  Carnivores/omnivores: δ¹⁵N ≈ 6–12‰
  Nursing infants: elevated δ¹⁵N (breast milk = trophic step up)
    → Can identify age at weaning from skeletal record

  Breastfeeding signature: identifies nursing period in skeletal populations
  High δ¹⁵N: high animal protein diet; freshwater fish; marine diet
  Low δ¹⁵N: primarily plant diet; legume consumption (N-fixers deplete ¹⁵N)
```

**Dual isotope analysis** (C+N together): resolves ambiguities. High δ¹³C + low δ¹⁵N = maize diet. High δ¹⁵N + intermediate δ¹³C = marine protein diet.

### Strontium and Oxygen Isotopes (Migration)

```
δ¹⁸O (oxygen isotopes — provenance/migration):
  Rainwater ¹⁸O/¹⁶O varies with latitude, altitude, continentality
  → Geographic isotope map (isoscape)
  Ingested water → incorporated into tooth enamel during formation
  Tooth enamel doesn't remodel → records childhood location

  Compare skeletal δ¹⁸O to local bedrock/water δ¹⁸O:
  MATCH → local individual
  MISMATCH → migrant (moved before or after teeth formed)

⁸⁷Sr/⁸⁶Sr (strontium isotopes — geographic origin):
  Strontium derives from bedrock geology (different ratios in different rocks)
  Plants absorb Sr from local geology → animals eat plants → bones/teeth
  Tooth enamel ⁸⁷Sr/⁸⁶Sr = local geology at time of childhood

  MIGRATION DETECTION:
  Compare tooth enamel Sr to bone Sr:
  Enamel forms in childhood (childhood location)
  Bone remodels → adult diet location
  Enamel ≠ bone Sr → individual moved between childhood and death

FAMOUS APPLICATIONS:
  Amesbury Archer (Stonehenge era): buried near Stonehenge;
    O isotopes indicate childhood in Alps → migrant
  "Iceman" Ötzi: Sr isotopes place childhood in specific Alpine valleys
  Mass grave from Tollense Valley battle (Bronze Age, Germany):
    Many combatants were not local (foreign fighters → large-scale conflict)
```

---

## Ancient DNA (aDNA)

The ancient DNA revolution (2010–present) has completely transformed understanding of human prehistory.

### The Technical Challenge

```
ANCIENT DNA VS. MODERN DNA:
  Ancient DNA is:
    Highly fragmented: average fragment 40–100 bp (vs. kb in modern)
    Chemically damaged: cytosine deamination (C→T) at fragment ends
    Low in quantity: 0.01–1% of sequenced reads may be endogenous
    Contaminated: modern human DNA is everywhere (high quality, abundant)

SIGNAL-TO-NOISE PROBLEM:
  Ancient endogenous DNA: degraded, fragmented, damaged → hard to read
  Modern contaminant DNA: intact, long, undamaged → easy to read
  → Analysis pipeline must:
    1. Identify and map reads to target genome
    2. Apply deamination filter (keep C→T damage at ends as authenticity check)
    3. Calculate contamination rate (compare to modern reference)
    4. Authenticate by damage pattern analysis (mapDamage tool)

COLD AND DRY = BETTER PRESERVATION:
  Best conditions: permafrost, cold caves, extreme arid
  Worst: tropical humid environments (DNA degrades rapidly)
  Mammoth steppe remains: aDNA up to 1.2 Ma (horse, 2013 record)
  Tropical human remains: rarely exceeds 10,000 years of preservation

PETROUS BONE:
  The dense inner ear bone (petrous part of temporal bone)
  Has highest DNA yield of any skeletal element
  Standard: 50–100 mg sample drilled from petrous
```

### What aDNA Can Reveal

```
POPULATION GENETICS FROM aDNA:
  Genotype from thousands of SNPs across genome
  → Principal Component Analysis (PCA): plot samples in genetic space
  → ADMIXTURE analysis: estimate ancestry from reference populations
  → D-statistics / f-statistics: test for genetic mixing events
  → Runs of homozygosity (ROH): detect close relative matings, small population

MAJOR FINDINGS (2010–2024):
  Three-wave model of European ancestry (2015+):
    1. Western Hunter-Gatherers (WHG): post-LGM; Mesolithic Europe
    2. Early European Farmers (EEF): Anatolian Neolithic farmers (7000 BC)
    3. Steppe ancestry (CWC/Yamnaya): migration from Pontic steppe (~3000 BC)
    Modern Europeans: mixture of all three in varying proportions

  Out-of-Africa dispersals:
    Non-African genomes contain ~2% Neanderthal DNA
    Melanesian genomes contain ~4% Denisovan DNA
    → Modern humans interbred with archaic humans multiple times

  Plague (Yersinia pestis): ancient genome tracked across Eurasian history
    → First detection in Bronze Age steppe populations (~3000 BC)
    → Justinianic Plague (541 AD) and Black Death (1347) same Yersinia lineage

  Viking expansion: aDNA from burial sites across N. Atlantic, Russia, UK
    → Genetic diversity: Vikings came from diverse Scandinavian backgrounds
    → Non-Scandinavian ancestry in some burials traditionally called "Viking"
```

### Kinship Analysis

```
RELATEDNESS FROM aDNA:
  ROH (runs of homozygosity): long identical stretches → inbreeding
  Identity by descent: shared haplotype segments → recent shared ancestry
  First-degree relatives: parent-child, full siblings (high IBD sharing)

  APPLICATIONS:
    Megalithic tomb burials: who is buried together?
    Newgrange (Ireland): passage tomb; individual with ROH suggesting
      first-degree relative parents (incest → elite family structure)
    Stonehenge environs: multiple first-degree relatives in same tomb
    Elite mound burials: detect dynastic family structures
```

---

## XRF Compositional Analysis

**X-Ray Fluorescence (XRF)**: identifies and quantifies elements in artifacts by their characteristic X-ray emission (see mineralogy/09-MINERAL-IDENTIFICATION for physics).

```
PROVENANCE: where was this artifact made?

The key insight: raw materials have characteristic elemental/isotopic
"fingerprints" tied to their geological sources.
Match the artifact's composition to a known source = provenance.

OBSIDIAN PROVENANCE:
  Obsidian (volcanic glass) is geologically highly variable
  Each volcano has a characteristic major/trace element composition
  Portable XRF: measure at the object; compare to source database
  → Trace archaeologically invisible exchange networks
  → Obsidian from Lipari (Sicily) distributed across Mediterranean
  → Obsidian from Anatolian sources (Göllü Dağ) across Near East

METAL ANALYSIS:
  Copper alloys (bronze): Cu + Sn + Pb; trace elements (As, Sb, Ni, Co, Ag)
  → Fingerprint specific copper ore sources
  Lead isotopes: ²⁰⁶Pb/²⁰⁷Pb / ²⁰⁸Pb/²⁰⁴Pb ratios vary by source
  → Identify origin of lead in bronze, silver objects, pigments

CERAMIC ANALYSIS:
  Clay chemistry varies geologically
  NAA (Neutron Activation Analysis): 35+ elements; very high precision
  → Match pottery to clay source or production center
  → Track pottery distribution as trade proxy
```

---

## Lipid Residue Analysis

Fats and oils absorbed into pottery walls survive millennia in archaeological contexts.

```
METHOD:
  Solvent extraction from pottery sherd (sub-gram sample)
  → GC-MS (Gas Chromatography-Mass Spectrometry) analysis
  → Identify lipid biomarkers

WHAT IS IDENTIFIED:
  Animal fats: fatty acid profile distinguishes:
    Ruminant (cattle/sheep/goat): specific C18 fatty acid ratio
    Porcine (pig): different ratio; distinctive
    Dairy vs. carcass fat: δ¹³C of individual fatty acids
      → Dairy lipids are ¹³C-depleted relative to carcass fat

  Plant oils: olive oil, linseed, sesame distinctive profiles
  Beeswax: characteristic triterpenoids (ursolic acid, etc.)
  Aquatic resources: specific polyunsaturated fatty acids (DHA, EPA)

APPLICATIONS:
  First dairying: oldest direct evidence of milk processing
    → Neolithic Britain (6,000 BP): dairy lipids in pottery
    → Saharan rock art cattle: dairy lipids in pottery → herding lifestyle
  Wine/beer: tartaric acid (wine), biomarkers for fermented products
  Medicinal/ritual substances: specific plant biomarkers
  Cooking practices: plant vs. animal fats by vessel type
```

---

## Zooarchaeology (Animal Bone Analysis)

Faunal assemblages from archaeological sites record: diet, domestication, economy, season of occupation, taphonomy.

```
ZOOARCHAEOLOGICAL ANALYSIS:
  NISP: Number of Identified Specimens (raw count)
  MNI: Minimum Number of Individuals (minimum to account for all elements)
  MNE: Minimum Number of Elements

  MORTALITY PROFILE:
    Age at death from bone fusion + tooth eruption/wear
    Prime-adult kill: hunting wild prey
    Neonatal/juvenile: may indicate dairying (kill male calves)
    Old female kill: dairy herd management
    → Distinguish hunting vs. pastoralism vs. dairying strategies

  BUTCHERY MARKS:
    Cut marks from stone/metal tools on bone
    Identify which joints were processed; meat removal vs. skinning
    Percussion marks: marrow extraction
    Burnt bone: cooking, disposal

  SPECIES SPECTRUM:
    Wild vs. domestic proportions → intensification of agriculture
    Introduction of new domestic species → colonization record
    Fishing bones → diet, season, technology
    Birds + small mammals → complete picture of landscape use

BIOMOLECULAR:
  Collagen stable isotopes: diet of the individual animal
  ZooMS (Zooarchaeology by Mass Spectrometry): collagen peptide fingerprints
    → Species ID from tiny or fragmentary bone
    → Works on degraded material where morphology insufficient
    → Revolutionized ID of fragmentary faunal assemblages
```

---

## Phytoliths and Environmental Proxies

```
PHYTOLITHS: silica bodies formed in plant cells
  Morphology reflects plant family/genus
  Silica is inorganic → survives when charred organic material does not
  Survive in otherwise poor preservation contexts

  APPLICATIONS:
    Reconstruct past vegetation when pollen absent
    Identify crop processing activity (chaff phytoliths)
    Detect presence of grasses in sediments → grazing or agriculture
    Amazonian sites: phytoliths from maize in pre-contact deposits

POLLEN ANALYSIS (PALYNOLOGY):
  Pollen grains have distinctive shapes by genus/family
  Preserved in lake sediments, peat, waterlogged contexts
  → Reconstruct past vegetation communities
  → Environmental context of archaeological site
  → Impact of human deforestation visible as pollen shift

MACRO-PLANT REMAINS (ARCHAEOBOTANY):
  Charred seeds, nuts, fruit stones → crop types, plant diet
  Waterlogged wood → construction timber, wood fuel
  Flotation: bulk soil samples processed with water → seeds float
  → Dietary plants, weeds, cultivated fields, stored crops
```

---

## Decision Cheat Sheet

| Question | Best Method |
|----------|-------------|
| Where was this pottery made? | XRF/NAA + comparison to source database |
| What did these people eat? | δ¹³C + δ¹⁵N from bone collagen |
| Did these people migrate? | Sr + O isotopes in tooth enamel vs. bone |
| Who is genetically related in this cemetery? | aDNA kinship analysis |
| What was stored in this Bronze Age jar? | Lipid residue analysis (GC-MS) |
| How old was this animal when killed? | Bone fusion + tooth wear analysis |
| What crops were grown here? | Archaeobotany (flotation + microscopy) |
| What was the past vegetation? | Pollen (lake sediment) or phytoliths |
| Is this Roman silver from Spain or Greece? | Lead isotope ratios |

---

## Common Confusion Points

**δ¹³C diet vs. δ¹³C reservoir effect**: The same isotope system (carbon) is used for dietary reconstruction (stable ¹³C) and age correction in radiocarbon (reservoir effects on ¹⁴C). These are different applications of related phenomena. Don't confuse them: stable ¹³C is a proxy for diet; ¹⁴C (radioactive) is used for age. Measuring ¹³C on a sample tells you diet; measuring ¹⁴C tells you age.

**aDNA contamination is asymmetric**: Modern DNA is high quality, human genetics is familiar to the lab environment (human researchers), and contamination is difficult to eliminate entirely. The authentication methods (damage patterns, strict protocols for cold labs, comparison to lab personnel's DNA) are standard but imperfect. Results from tropical sites or samples with poor DNA preservation should be treated cautiously.

**Lipid residue = use, not manufacture**: Lipid analysis tells you what was stored/cooked in a vessel during its use life. It doesn't tell you where or by whom the pot was made. Provenance of manufacture = ceramic petrography or XRF. Use history = lipid residue.

**Stable isotopes reflect averages**: Bone collagen isotopes average ~10 years of diet (bone remodeling). Tooth enamel is fixed at formation (childhood). Hair (if preserved) gives seasonal resolution — each cm of hair represents ~1 month. The temporal resolution matters for interpreting results.

**ZooMS vs. aDNA for bone ID**: ZooMS (collagen peptide) identifies species from very degraded bone where aDNA might be too fragmented to recover. ZooMS can't identify individuals or populations. aDNA gives individual-level genetic information. They're complementary: ZooMS for species ID in bulk, aDNA for targeted individual-level questions.
