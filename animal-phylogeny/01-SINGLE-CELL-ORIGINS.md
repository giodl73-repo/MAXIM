# Single-Cell Origins — From LUCA to the First Animals

## The Big Picture

```
+---------------------------------------------------------------+
|                    TREE OF LIFE                               |
|                                                               |
|  LUCA (~3.8 Ga)   ─── Last Universal Common Ancestor          |
|        |                                                      |
|   +----+----+                                                 |
|   |         |                                                  |
| BACTERIA  ARCHAEA                                              |
|   |         |                                                  |
|   |    (some Archaea + some Bacteria)                          |
|   |         |                                                  |
|   |    EUKARYOTA  (endosymbiotic merger)                       |
|   |         |                                                  |
|   |    +----+-------+--------+--------+                        |
|   |    |            |        |        |                        |
|   |  Plants       Fungi   Animals  Other protists              |
|   |                                                            |
|  (no nucleus)          (nucleus, membrane-bound organelles)    |
+---------------------------------------------------------------+

TIME
4000 Ma  First prokaryotes (stromatolites 3500 Ma)
2400 Ma  Great Oxidation Event — cyanobacteria dump O₂
2100 Ma  First eukaryotes (fossil record)
1200 Ma  First multicellular red algae
600 Ma   First animals (Ediacaran)
541 Ma   Cambrian explosion
```

---

## Layer 1 — Prokaryotes: The Invisible Majority

### Cell Architecture

```
PROKARYOTE (Bacteria / Archaea)
+------------------------------------------------+
|  Cell wall (peptidoglycan in Bacteria,         |
|            pseudopeptidoglycan in Archaea)     |
|  +-----------------------------------------+   |
|  |  CYTOPLASM                              |  |
|  |                                         |  |
|  |  Nucleoid region  (DNA, no membrane)    |  |
|  |  70S ribosomes    (not 80S like Euk.)   |  |
|  |  Plasmids         (extra circular DNA)  |  |
|  |  Flagella (different structure in Arch) |  |
|  +-----------------------------------------+  |
|  Plasma membrane                              |
+------------------------------------------------+
SIZE: 0.1 – 10 μm  (compare eukaryote: 10–100 μm)
```

### Bacterial Diversity (by metabolism)

| Metabolic Type | Energy Source | Carbon Source | Examples |
|---------------|--------------|---------------|---------|
| Photoautotroph | Light | CO₂ | Cyanobacteria, purple sulfur bacteria |
| Chemoautotroph | Inorganic molecules | CO₂ | Nitrifying bacteria, sulfur oxidizers |
| Photoheterotroph | Light | Organic compounds | Purple non-sulfur bacteria |
| Chemoheterotroph | Organic molecules | Organic compounds | E. coli, most pathogens |

### Gram Stain: The Primary Bacterial Divide

```
GRAM POSITIVE                   GRAM NEGATIVE
+-------------------------+     +-----------------------------+
| Thick peptidoglycan     |     | Thin peptidoglycan          |
| (retains crystal violet)|     | + outer membrane            |
|                         |     | (doesn't retain dye)        |
| Staphylococcus aureus   |     | E. coli                     |
| Streptococcus           |     | Salmonella                  |
| Clostridium             |     | Helicobacter pylori         |
| Bacillus anthracis      |     | Pseudomonas                 |
+-------------------------+     | Neisseria (meningitis)      |
                                 +-----------------------------+
Clinical importance: outer membrane blocks many antibiotics
→ Gram-negative infections harder to treat
```

### Archaea — The "Third Domain"

Long misclassified as bacteria, Archaea share features with both Bacteria and Eukaryotes:

| Feature | Bacteria | Archaea | Eukaryota |
|---------|---------|---------|----------|
| Nuclear envelope | No | No | Yes |
| Cell wall | Peptidoglycan | Pseudopeptidoglycan / S-layer | Varies |
| Ribosome | 70S | 70S but euk-like proteins | 80S |
| RNA polymerase | Simple (4 subunit) | Complex (like euk) | Complex |
| Introns | Rare | Yes | Yes |
| Histones | No | Yes (histone-like) | Yes |
| Ether-linked membrane lipids | No | **Yes** (key difference) | No |

```
ARCHAEA ECOLOGICAL NICHES (extremophiles + mainstream)
+---------------------------------------------------------+
| Methanogens      Anaerobic, produce CH₄                 |
|                  In cow guts, rice paddies, human colon |
| Halophiles       High salt (Dead Sea, salt lakes)       |
|                  Halobacterium uses light (bacteriorhodopsin)|
| Thermophiles     90–121°C (deep sea hydrothermal vents) |
|                  Sulfolobus, Pyrolobus fumarii          |
| Acidophiles      pH < 3 (mine drainage)                 |
| Psychrophiles    Sub-zero (Antarctic brines)            |
| "Normal" archaea In soils, oceans, human microbiome     |
+---------------------------------------------------------+
```

---

Bacterial and archaeal classification is a clustering problem on a high-dimensional feature space: the character matrix is metabolic type (carbon source, energy source, electron acceptor/donor), morphology, 16S rRNA sequence, and membrane lipid type. 16S rRNA distance is the standard clustering key — a pairwise distance matrix that feeds hierarchical clustering (UPGMA or Neighbor-Joining) to produce the prokaryote tree of life. The 97% 16S similarity threshold for "same species" is an arbitrary cluster cutoff, exactly like choosing k in k-means. Whole-genome average nucleotide identity (ANI ≥ 95%) is the more principled modern threshold — higher-dimensional, harder to compute, but much more accurate. The entire metagenomics field is unsupervised clustering applied to environmental sequence data: extract DNA from soil → sequence → cluster by similarity → assign to known or novel lineages, no culturing required.

## Layer 2 — The Great Oxidation Event

```
TIMELINE OF ATMOSPHERIC OXYGEN

3500 Ma  |  O₂ ~ 0%  Anaerobic world. Life is all prokaryotes.
          |
          |  Cyanobacteria evolve oxygenic photosynthesis
          |  (using H₂O as electron donor, releasing O₂)
          |
2400 Ma  |  "GREAT OXIDATION EVENT"
          |  Free O₂ begins accumulating
          |  Kills most anaerobes (mass extinction)
          |  Rusts iron → Banded Iron Formations (BIFs)
          |
1500 Ma  |  O₂ ~ 2%  Still low
          |
800 Ma   |  O₂ rising with multicellular algae
          |
541 Ma   |  O₂ ~ 10–15%  Cambrian explosion possible
          |
280 Ma   |  O₂ ~ 35%  Carboniferous peak → huge insects
          |
Present  |  O₂ ~ 21%

WHY O₂ MATTERS FOR ANIMALS:
Aerobic respiration yields ~38 ATP/glucose vs ~2 ATP anaerobic
Large, motile animals need the energy density
```

---

## Layer 3 — LUCA: Last Universal Common Ancestor

```
EVIDENCE FOR LUCA (~3.8 Ga)
+----------------------------------------------------+
| All life shares:                                   |
|   DNA as genetic material (not RNA)                |
|   Same 4 DNA bases (A/T/G/C)                       |
|   Same genetic code (64 codons → 20 amino acids)   |
|   ATP as energy currency                           |
|   Ribosomes (though subtly different)              |
|   Left-handed amino acids, right-handed sugars     |
|   Lipid bilayer membranes                          |
+----------------------------------------------------+

LUCA was NOT the first life — it was the survivor of early
horizontal gene transfer chaos. Think of it as the last
common trunk before Bacteria and Archaea diverged.

RNA World Hypothesis (before LUCA):
  RNA first → both stores information AND catalyzes reactions
  Ribozymes: RNA that acts as enzyme (still seen in ribosomes)
  DNA more stable → took over information storage
  Proteins more versatile → took over catalysis
  RNA became the intermediary (mRNA)
```

---

## Layer 4 — Eukaryogenesis: The Endosymbiotic Merger

```
THE ENDOSYMBIOTIC THEORY (Lynn Margulis, 1967)

~2 billion years ago:

Step 1: Large archaeal (or proto-eukaryotic) cell
        engulfs (but does not digest)
        α-proteobacterium

Step 2: Permanent endosymbiosis
        Engulfed bacterium → MITOCHONDRION

Step 3: Later, some eukaryote lineages engulf cyanobacterium
        Cyanobacterium → CHLOROPLAST

EVIDENCE IT HAPPENED:
+--------------------------------------------------+
| Feature         | Mitochondria | Chloroplast     |
|-----------------|-------------|-----------------|
| Own DNA         | ✓ (circular)| ✓ (circular)     |
| Double membrane | ✓           | ✓                |
| 70S ribosomes   | ✓           | ✓                |
| Binary fission  | ✓           | ✓                |
| Sequence sim.   | α-proteo    | cyanobacteria    |
| Gene transfer   | ✓ (to nucleus)| ✓ (to nucleus) |
+--------------------------------------------------+

The eukaryotic cell is therefore a CHIMERA —
part archaeal host, part bacterial endosymbiont(s)
```

---

## Layer 5 — Protists: The Eukaryotes That Didn't Become Animals

"Protist" = informal grade, not a clade. Any eukaryote that isn't a plant, fungus, or animal.

```
SAR CLADE (Stramenopiles + Alveolata + Rhizaria)
+---------------------------------------------------------+
| Stramenopiles                                           |
|   Diatoms — silica frustules, 20–25% of global O₂       |
|   Brown algae — kelp forests (Macrocystis 45m long)     |
|   Water molds (Oomycetes) — caused Irish potato famine  |
|                                                         |
| Alveolata                                               |
|   Dinoflagellates — marine, some bioluminescent,        |
|     symbiotic as zooxanthellae in coral                 |
|   Ciliates — Paramecium, Stentor (two nuclei: macro/micro)|
|   Apicomplexans — all parasitic: Plasmodium (malaria),  |
|     Toxoplasma, Cryptosporidium                         |
|                                                         |
| Rhizaria                                                |
|   Foraminifera — tests of CaCO₃, chalk/limestone        |
|   Radiolaria — intricate silica shells                  |
+---------------------------------------------------------+

EXCAVATA
  Giardia — no mitochondria (secondarily lost), human pathogen
  Trypanosoma — sleeping sickness, Chagas disease
  Euglena — has chloroplast (secondary endosymbiosis)

ARCHAEPLASTIDA
  Red algae — first to engulf cyanobacterium
  Green algae — gave rise to land plants (Charophytes)
    Volvox — colonial green alga: model for multicellularity
    (8 cell types, germ-soma division — proto-body plan)

OPISTHOKONTA (animals + fungi share this ancestor)
  Choanoflagellates — collar cells, single-celled BUT
    form colonies, nearly identical to sponge choanocytes
    → DIRECT ANCESTOR-TYPE of animals
```

The choanoflagellate-to-animal transition is a monolith-to-microservices decomposition: start with identical generalist cells (each does everything — metabolize, reproduce, sense, move), then specialization emerges (differentiated cell types each do one function well). The Volvox lineage shows the progression in real time: Chlamydomonas (one cell, all functions), Gonium (8-32 cells, loose division of labor), Volvox (~1000 cells, strict germ-soma split — somatic cells sacrifice reproduction to serve the germ line). The analogy holds structurally: the monolith is simpler per-unit, more resilient if a cell fails; the specialized system has higher throughput but requires coordination overhead and cannot survive if the germ-line "service" fails.

### The Transition to Multicellularity

```
VOLVOCINE GREEN ALGAE (model lineage)

Chlamydomonas          Gonium              Volvox
(unicellular)       (4–32 cells,        (~1000 cells,
    ↓               flat sheet)          sphere)
    ↓                   ↓                    ↓
All cells identical  Mild adhesion    GERM-SOMA division:
                                      ~16 reproductive cells
                                      ~1000 somatic cells
                                      Individual cells die for
                                      the colony's benefit

This is the EVOLUTION OF MULTICELLULARITY in action.
At least 25 independent origins of multicellularity are known.
Animals represent ONE such origin, ~800 Ma.
```

---

## Protist Reference Table

| Group | Locomotion | Feeding | Medical/Ecological Importance |
|-------|-----------|---------|------------------------------|
| Amoeba (Amoebozoa) | Pseudopods | Phagocytosis | Entamoeba histolytica (dysentery) |
| Paramecium | Cilia | Filter feeding | Model organism |
| Plasmodium | None (intracellular) | Red blood cells | Malaria: 200M cases/yr |
| Trypanosoma | Flagellum | Blood proteins | Sleeping sickness, Chagas |
| Diatoms | None (sinking) | Photosynthesis | Base of marine food chain |
| Dinoflagellates | Two flagella | Photosynthesis/predation | Red tides; coral symbiont |
| Foraminifera | Pseudopods | Phagocytosis | Chalk, limestone deposits |
| Choanoflagellates | Flagellum | Filter via collar | Closest relative of animals |

---

## Decision Cheat Sheet

```
Is it prokaryotic (no nucleus)?
  +-- Has ether-linked membrane lipids, complex RNA pol → ARCHAEA
  +-- Has peptidoglycan cell wall, 4-subunit RNA pol     → BACTERIA

Is it eukaryotic (has nucleus)?
  Is it multicellular with differentiated tissues?
    Photosynthetic → PLANT
    Cell wall, absorptive → FUNGUS
    No cell wall, ingestive → ANIMAL

  Is it unicellular or colonial without specialized tissues?
    → PROTIST (informal group; which one?)

    Has cilia → Ciliophora (Paramecium, Stentor)
    Has chloroplast, flagellum → Euglenozoa or Dinoflagellate
    Intracellular parasite → Apicomplexan (Plasmodium etc.)
    Pseudopods, shell → Foraminifera or Rhizaria
    Closest to animals, collar → CHOANOFLAGELLATE
```

---

## Common Confusion Points

**Archaea ≠ ancient bacteria.**
Despite the name, Archaea are not "primitive bacteria." They have a distinct evolutionary lineage, different cell biology, and are actually more closely related to eukaryotes in key molecular features (RNA polymerase, histones).

**Mitochondria DNA is circular — like bacteria.**
This is the smoking gun for endosymbiosis. Human mitochondrial DNA is ~16,600 bp of circular DNA encoding 37 genes. Over 2 billion years, most mitochondrial genes migrated to the nucleus — but the relic remains.

**Protists aren't a kingdom.**
"Kingdom Protista" was taxonomically useful but phylogenetically garbage — it's a wastebasket of unrelated lineages. Modern systematics abolished it.

**Choanoflagellates are not animals.**
But they're the sister group to all animals. Their collar cells are morphologically identical to sponge choanocytes. The gene regulatory toolkit for multicellularity was likely already present in the choanoflagellate ancestor.

**Oxygenic vs anoxygenic photosynthesis.**
Cyanobacteria do oxygenic photosynthesis (H₂O → O₂). Green/purple sulfur bacteria do anoxygenic photosynthesis (H₂S → S, no O₂ released). Only cyanobacteria changed the atmosphere.

**The RNA World is inferred, not observed.**
No RNA-only organisms exist today. But ribosomes are catalytic RNA (ribozymes) doing the core job of protein synthesis — the ribosome is a fossil of the RNA World embedded in every cell on Earth.
