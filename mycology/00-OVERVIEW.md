# Mycology — Overview and Landscape

## The Big Picture

```
+------------------------------------------------------------------+
|                    KINGDOM FUNGI: THE LANDSCAPE                  |
|                                                                  |
|  Estimated 5.1 million species (ITS-based estimates, 2017)     |
|  ~150,000 described (~3% of total)                              |
|  Oldest known fungi: ~1 billion years (marine, Proterozoic)    |
|                                                                  |
|  THE FUNGAL PARADOX:                                            |
|  Sessile, like plants → heterotrophic, like animals             |
|  Cell-walled, like plants → no chlorophyll, no photosynthesis  |
|  More closely related to animals than to plants (!!)            |
|                                                                  |
<!-- @editor[diagram/P2]: Diagram lists facts but doesn't show how the major branches (saprotrophs, mycorrhizal, pathogens, industrial) relate to each other — rework as layered system view showing ecological/economic roles branching from the kingdom -->
|  WHERE FUNGI ARE:                                               |
|  Everywhere — soil, air, water, inside plants, inside animals  |
|  1 teaspoon of forest soil: 100 million to 1 billion fungal cells|
|  Your skin + gut: permanent fungal communities (mycobiome)      |
+------------------------------------------------------------------+
```

---

## Breaking the Plant/Animal Binary
<!-- @editor[bridge/P2]: No universal CS bridge here — the reclassification parallels taxonomy refactoring (e.g., moving a class to a different module when inheritance was wrong). Any senior engineer who has done a major taxonomy overhaul would connect to this. -->

The reclassification of fungi as a separate kingdom is one of the genuinely counterintuitive reorganizations in biology:

```
THE EVOLUTIONARY SURPRISE

NAÏVE VIEW:
  Living things are either:
  Plants (photosynthetic, sessile, cell-walled) OR
  Animals (mobile, heterotrophic, no cell wall)
  Fungi look like plants → classified with plants historically

CORRECT VIEW:
  OPISTHOKONTS (single clade):
    Animals (Metazoa)
    Choanoflagellates (unicellular; closest relatives of animals)
    Fungi (Mycota)

  Animals + Fungi are SISTER GROUPS — more closely related to each
  other than either is to plants.

WHAT MAKES FUNGI DISTINCT:
  Cell walls: CHITIN (N-acetylglucosamine polymer)
    → Same chitin as insect exoskeletons
    → Plants have cellulose cell walls; bacteria have peptidoglycan
  Nutrition: osmotrophic — secrete enzymes externally, absorb nutrients
    → NOT photosynthetic, NOT phagocytic (like animals)
  Storage carbohydrate: GLYCOGEN (same as animals; plants use starch)
  Cell membrane: contains ERGOSTEROL (not cholesterol as in animals)
    → This ergosterol difference = target for antifungal drugs
```

---

## Structural Organization

```
FUNGAL BODY PLAN (Thallus)
+------------------------------------------------------------------+
|  HYPHAE: the basic unit                                         |
|  Tubular filaments, 2–10 µm diameter                           |
|  Cell wall: chitin + glucans                                    |
|  Growth: apical extension (tip elongates, not cell division)   |
|                                                                  |
|  MYCELIUM: network of branching hyphae                         |
|  The "body" of the fungus                                      |
|  Invisible for most of fungal life cycle                       |
|  Can be enormous: Oregon Armillaria = 2,385 ha; ~8,000 tonnes  |
|    = possibly largest organism on Earth                        |
|                                                                  |
|  SEPTA: cross-walls dividing hyphae into compartments          |
|  Ascomycetes: septate (septa with central pore = Woronin body) |
|  Basidiomycetes: septate (dolipore septa = more complex)       |
|  Zygomycetes: aseptate (coenocytic — multinucleate)           |
|                                                                  |
|  FRUITING BODY: reproductive structure                         |
|  Mushroom: basidiomycete fruiting body                        |
|  Cup fungus: ascomycete fruiting body                         |
|  → Only a small fraction of mycelial biomass                  |
|  → What you see is NOT the fungus; the mycelium IS the fungus  |
+------------------------------------------------------------------+
```

---

## Ecological Roles

```
FUNGI AS ECOSYSTEM ENGINEERS
+------------------------------------------------------------------+
|  DECOMPOSERS / SAPROTROPHS:                                     |
|  Break down dead organic matter                                 |
|  Only organisms that can degrade LIGNIN (white rot fungi)      |
|  Without fungi: dead wood would accumulate forever             |
|  Carbon cycle: fungi return C to atmosphere as CO₂             |
|                                                                  |
|  MYCORRHIZAL SYMBIONTS:                                        |
|  ~80% of land plants form mycorrhizal partnerships             |
|  Ectomycorrhizal: hyphal sheath outside root (forest trees)    |
|  Arbuscular mycorrhizal (AM): hyphae penetrate root cells      |
|  Fungus: gets photosynthate (sugar) from plant                 |
|  Plant: gets phosphorus, water, minerals from fungal network   |
|  → Not optional for most plants; obligate mutualism            |
|                                                                  |
|  PATHOGENS:                                                     |
|  Plant pathogens: wheat rust, potato blight (oomycete), corn smut|
|  Animal pathogens: Aspergillus, Candida, Cryptococcus          |
|  Amphibian pathogens: Batrachochytrium → global amphibian crisis|
|                                                                  |
|  ENDOPHYTES:                                                    |
|  Live inside healthy plants without causing disease            |
|  May confer drought tolerance, pest resistance                 |
|  Nearly every plant contains endophytic fungi                  |
|                                                                  |
|  LICHENS:                                                       |
|  Fungal partner + photosynthetic partner (alga or cyanobacteria)|
|  ~20,000 species; pioneer colonizers of bare rock              |
+------------------------------------------------------------------+
```

---

## Human Significance

```
FUNGI AND HUMAN CIVILIZATION
+------------------------------------------------------------------+
|  FOOD:                                                           |
|  Edible mushrooms: Agaricus, Lentinula (shiitake), Pleurotus   |
|  Truffle (Tuber): most expensive food by weight (~€2,000/kg)   |
|  Fermentation: Saccharomyces (bread, beer, wine), Aspergillus   |
|    (soy sauce, miso, sake, shochu), Penicillium (aged cheeses) |
|                                                                  |
|  MEDICINE:                                                       |
|  Penicillin (Penicillium notatum, 1928): antibiotics revolution |
|  Cyclosporin (Tolypocladium): organ transplant immunosuppression|
|  Statins (Monascus, Aspergillus): lovastatin (cholesterol)     |
|  Psilocybin (Psilocybe): psychiatric treatment (clinical trials)|
|  Cephalosporins, fusidic acid, griseofulvin: from fungi        |
|                                                                  |
|  INDUSTRY:                                                       |
|  Citric acid (Aspergillus niger): food additive               |
|  Enzymes: amylases, lipases, cellulases, proteases             |
|  Mycoprotein (Quorn): fungal protein food (Fusarium)           |
|  Mycelium composites: packaging (Ecovative, Bolt Threads)      |
|  Biofuel: cellulolytic fungi degrade lignocellulosic biomass   |
|                                                                  |
|  PATHOGENS (cost):                                              |
|  Wheat stem rust: >20% global crop loss potential              |
|  Chestnut blight: destroyed American chestnut (near extinction) |
|  Fungal diseases: kill more people than malaria + tuberculosis  |
|    combined in immunocompromised patients                       |
|  White-nose syndrome: devastated North American bat populations |
+------------------------------------------------------------------+
```

---

## File Guide

| File | Topic | Core Concept |
|------|-------|--------------|
| 01-FUNGAL-BIOLOGY | Cell structure, nutrition, reproduction | Chitin, osmotrophy, spores |
| 02-PHYLOGENY-CLASSIFICATION | Major phyla, phylogenomics | Animal-fungi sister group |
| 03-ECOLOGY | Decomposition, mycorrhizae, lichens | Wood Wide Web |
| 04-EDIBLE-FUNGI | Commercial species, cultivation | From spawn to fruiting body |
| 05-TOXIC-FUNGI | Amatoxins, muscimol, orellanine | RNA Pol II inhibition mechanism |
| 06-PSYCHEDELIC-FUNGI | Psilocybin mechanism, clinical trials | 5-HT2A agonism and DMN |
| 07-PLANT-PATHOGENS | Rusts, smuts, Phytophthora (oomycete) | Ug99 wheat rust threat |
| 08-ANIMAL-PATHOGENS | Aspergillus, Candida, Bd | C. auris emergence |
| 09-INDUSTRIAL-MYCOLOGY | Penicillin, enzymes, mycelium materials | Fleming to Florey to industry |

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| Are fungi plants? | No — more closely related to animals than to plants |
| What is the cell wall made of? | Chitin (same as insect exoskeleton; not cellulose like plants) |
| What is the "Wood Wide Web"? | Mycorrhizal hyphal networks connecting forest trees; carbon/phosphorus exchange |
| How do fungi eat? | Osmotrophic: secrete enzymes, absorb digested nutrients externally |
| Most dangerous human fungal pathogen? | Cryptococcus neoformans (meningitis in immunocompromised); Candida auris (emerging drug-resistant) |
| Largest organism on Earth? | Possibly Armillaria ostoyae in Oregon: 2,385 ha mycelial mat |

---

## Common Confusion Points

**Fungi are not plants**: Despite superficial resemblance (sessile, growing from soil, often visible as mushrooms), fungi lack chlorophyll, photosynthesis, cellulose cell walls, and the plant-specific metabolic pathways. This is not a trivial reclassification — it changes how antifungals work (target ergosterol, not present in plants or animals) and how we understand fungal diseases.

**The mushroom is not the fungus**: The mushroom (fruiting body) is the reproductive structure — analogous to an apple on an apple tree. The fungus is the mycelium (the invisible underground network). The mycelium is the organism; the mushroom is transient.

**Estimated 5.1 million species is a model**: This figure (Hawksworth and Lücking, 2017) uses DNA barcode surveys and scaling to project total diversity. Very few environments have been comprehensively sampled. The 150,000 described species are the known fraction.

**Oomycetes are NOT fungi**: Phytophthora (potato blight), Pythium, Peronospora are oomycetes (water molds) — phylogenetically in Stramenopiles, closer to brown algae than to fungi. They are studied by mycologists by tradition and resemble fungi superficially, but they're not in Kingdom Fungi. This matters medically and practically: antifungals don't work on oomycetes.
