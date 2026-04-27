# Animal Phylogeny — Overview & Tree of Life

## The Big Picture

```
DOMAINS OF LIFE:

  BACTERIA  (most diversity; E.coli, cyanobacteria, Firmicutes, Proteobacteria)
  ARCHAEA   (extremophiles, methanogens, thermophiles)
  EUKARYOTA (nucleus, membrane-bound organelles)
   |
   +-- Excavata (Giardia, Trypanosoma)
   +-- SAR clade (diatoms, forams, ciliates)
   +-- Archaeplastida (red/green algae, land plants)
   +-- Opisthokonta
        |
        +-- Fungi
        +-- ANIMALIA (this guide)

ANIMALIA TREE — simplified grade/clade ladder:

  Non-bilaterian grade:
    Porifera (sponges)  — most ancient
    Placozoa            — simplest body plan
    Ctenophora          — comb jellies (position debated)
    Cnidaria            — jellyfish, corals, sea anemones
                              |
                              v
  BILATERIA (3 germ layers, bilateral symmetry)
   |
   +-- PROTOSTOMIA (blastopore → mouth)
   |    |
   |    +-- Lophotrochozoa (annelids, molluscs, flatworms, rotifers)
   |    +-- Ecdysozoa (molting; arthropods, nematodes)
   |
   +-- DEUTEROSTOMIA (blastopore → anus)
        |
        +-- Echinodermata (sea stars, sea urchins)
        +-- Chordata (vertebrates, tunicates, lancelets)
```

---

## Geological Time Scale + Major Transitions

```
Eon / Era         Ma (million years ago)   Key Event
+------------------------------------------------------------------+
Hadean            4600–4000                Earth forms, heavy bombardment
Archean           4000–2500                LUCA, first prokaryotes ~3800 Ma
                                           First evidence of life: stromatolites
Proterozoic       2500–541
  Paleoproterozoic 2500–1600               Great Oxidation Event 2400 Ma
                                           Endosymbiosis → first eukaryotes ~2100 Ma
  Mesoproterozoic  1600–1000               Sexual reproduction, first multicellular algae
  Neoproterozoic   1000–541
    Cryogenian     720–635                 Snowball Earth episodes
    Ediacaran      635–541                 FIRST MACROSCOPIC ANIMALS
                                           Ediacaran biota (Dickinsonia, Charnia)

Phanerozoic       541–present
  Cambrian        541–485                  CAMBRIAN EXPLOSION — most animal phyla appear
                                           Burgess Shale (508 Ma), Chengjiang (520 Ma)
  Ordovician      485–444                  Marine diversity peak; mass extinction -444 Ma
  Silurian        444–419                  First land plants; jawed fish diversify
  Devonian        419–359                  "Age of Fishes"; first tetrapods (Tiktaalik 375 Ma)
                                           First land plants with seeds; mass extinction -359
  Carboniferous   359–299                  Vast coal swamps; first amniotes ~320 Ma
  Permian         299–252                  Synapsid radiation; Great Dying -252 Ma (96% species lost)
  Triassic        252–201                  Dinosaur + mammal origins; mass extinction -201 Ma
  Jurassic        201–145                  Dinosaur dominance; first birds (Archaeopteryx 150 Ma)
  Cretaceous      145–66                   Flowering plants; K-Pg extinction -66 Ma
  Paleogene       66–23                    Mammal radiation; first large whales ~50 Ma
  Neogene         23–2.6                   Grasslands; hominins diverge ~6 Ma
  Quaternary      2.6–0                    Ice ages; Homo sapiens ~300 Ka; Holocene 11.7 Ka
+------------------------------------------------------------------+
```

---

## How Phylogeny Works

Cladistics is a maximum parsimony problem on a character-state matrix. Each taxon is a row vector of binary or multi-state characters (presence/absence of a trait, nucleotide at a position). Finding the most parsimonious tree — the tree requiring the fewest evolutionary changes to explain the observed character states — is NP-hard (equivalent to Steiner tree on a weighted graph). In practice: branch-and-bound for small datasets, heuristic tree-rearrangement (SPR/TBR moves) for larger ones. Bayesian phylogenetics replaces parsimony with posterior probability (Bayes' theorem over tree topology × branch lengths × substitution model), computed by MCMC over tree space. The molecular clock is a Poisson process: mutations accumulate at a roughly constant rate per site per unit time, so genetic distance ≈ time since divergence × substitution rate. Calibrate against fossil dates → absolute divergence times.

### Cladistics: The Core Method

```
KEY CONCEPTS
+---------------------------------------------------------------+
| Clade (monophyletic group):                                   |
|   An ancestor + ALL its descendants                           |
|   "Mammals" is a clade. "Reptiles" (without birds) is NOT.    |
|                                                               |
| Synapomorphy:                                                 |
|   Shared derived character — evidence of common ancestry      |
|   Example: hair/fur = synapomorphy of all mammals             |
|                                                               |
| Homoplasy (convergence):                                      |
|   Same trait evolving independently in different lineages     |
|   Example: wings in insects, birds, bats, pterosaurs          |
|                                                               |
| Outgroup:                                                     |
|   A related group used to determine which traits are ancestral|
+---------------------------------------------------------------+

CLADOGRAM READING:

  Taxa: A, B, C, D
  (A,B) form sister-pair → joined first
  (C,D) form sister-pair → joined first
  Then (A,B) pair joins (C,D) pair at a deeper node.

Interpretation:
- (A,B) are sister taxa — share a more recent common ancestor
- (A,B,C,D) form a clade (node at bottom = their common ancestor)
- Horizontal distance = NOTHING (not time or genetic distance)
- Branch length = meaningful in phylograms, not in cladograms
```

**The computational pipeline for molecular phylogenetics:** Sequence alignment (Needleman-Wunsch for global, Smith-Waterman for local) produces a multiple sequence alignment — the character matrix for phylogenetic inference. BLAST provides the rapid database search to find homologs before the slower alignment step. Distance methods (UPGMA, Neighbor-Joining) build trees from a pairwise distance matrix (O(n²) space); character-based methods (maximum parsimony, maximum likelihood) operate directly on aligned sequences and are computationally heavier. The MAFFT → IQ-TREE → FigTree pipeline is the current standard for phylogenomics.

### Molecular vs Morphological Phylogenetics

| Approach | Data Source | Strengths | Weaknesses |
|----------|-------------|-----------|------------|
| Morphological | Skeletal, soft-tissue, fossils | Includes extinct taxa | Convergence fools it |
| Molecular (16S rRNA) | Ribosomal RNA sequences | Universal, conserved | No fossil data |
| Molecular (whole genome) | Comparative genomics | High resolution | Requires sequenced genomes |
| Total-evidence | Morphology + molecules | Most complete | Computationally intense |

**The revolution**: Molecular phylogenetics overturned many morphological classifications.
- "Reptilia" (traditional) = paraphyletic grade — birds are dinosaurs
- Whales nest inside Artiodactyla (even-toed ungulates) — closer to hippos than to any other living mammal
- Fungi are closer to animals than to plants

---

## Body Plan Innovations — The Ladder of Complexity

```
+-------------------------------------------------------------+
|  No tissues      → Porifera (sponges)                       |
|  Two germ layers → Cnidaria, Ctenophora (ecto + endo)       |
|  Radial symmetry → Cnidaria, Ctenophora                     |
|  Three germ layers → BILATERIA (+ mesoderm = muscles)       |
|  Bilateral symmetry → BILATERIA                             |
|  True coelom     → Annelida, Mollusca, Arthropoda,          |
|                    Echinodermata, Chordata                  |
|  Segmentation    → Annelida, Arthropoda (Chordata too,      |
|                    via somites)                             |
|  Exoskeleton     → Arthropoda (chitin)                      |
|  Endoskeleton    → Echinodermata (calcium carbonate),       |
|                    Vertebrata (bone/cartilage)              |
|  Pharyngeal slits → Chordata (including vertebrates)        |
|  Notochord       → Chordata                                 |
|  Vertebral column → Vertebrata                              |
|  Jaws            → Gnathostomata (all vertebrates except    |
|                    lampreys/hagfish)                        |
|  Paired limbs    → Tetrapoda (4 limbs)                      |
|  Amniotic egg    → Amniota (reptiles, birds, mammals)       |
|  Placenta        → Eutheria (placental mammals)             |
+-------------------------------------------------------------+
```

---

## The Phylum Index

```
ANIMALIA — 35 recognized phyla (only major ones listed)

NON-BILATERIA
  Porifera          ~9,000 sp   Sponges
  Placozoa          ~1 sp       Trichoplax
  Cnidaria          ~11,000 sp  Jellyfish, corals, sea anemones, hydra
  Ctenophora        ~100–200 sp Comb jellies

BILATERIA
  LOPHOTROCHOZOA
    Platyhelminthes  ~29,000 sp  Flatworms (planarians, flukes, tapeworms)
    Nemertea         ~1,300 sp   Ribbon worms
    Annelida         ~22,000 sp  Segmented worms (earthworms, polychaetes)
    Mollusca         ~85,000 sp  Snails, clams, squids, octopi
    Rotifera         ~2,200 sp   Microscopic filter feeders
    Bryozoa          ~6,000 sp   Moss animals (colonial)
    Brachiopoda      ~400 sp     Lamp shells (once dominant)

  ECDYSOZOA
    Nematoda         ~25,000 sp  Roundworms (C. elegans, hookworms)
                     (estimated 1 million+ total)
    Tardigrada       ~1,300 sp   Water bears
    Onychophora      ~180 sp     Velvet worms
    Arthropoda       ~1.1M sp    Insects, spiders, crabs, centipedes
      Chelicerata    ~100,000 sp Spiders, scorpions, mites, horseshoe crabs
      Myriapoda      ~13,000 sp  Centipedes, millipedes
      Crustacea      ~67,000 sp  Shrimp, crabs, barnacles, copepods
      Insecta        ~1,000,000 sp The dominant class on Earth

  DEUTEROSTOMIA
    Echinodermata    ~7,500 sp   Sea stars, sea urchins, sea cucumbers
    Hemichordata     ~130 sp     Acorn worms, pterobranchs
    Chordata         ~60,000 sp
      Urochordata    ~3,000 sp   Tunicates, sea squirts
      Cephalochordata ~32 sp     Lancelets (amphioxus)
      Vertebrata     ~57,000 sp  Fish, amphibians, reptiles, birds, mammals
```

---

## The Cambrian Explosion

```
Pre-Cambrian (~600 Ma):
+----------------------+
| Soft-bodied Ediacara |
| Dickinsonia          |
| Charnia (frond)      |
| Kimberella (mobile)  |
| No shells            |
| No eyes              |
| No heads             |
+----------------------+

Cambrian (~520-508 Ma):
+--------------------------------+
| Hard parts: shells, exoskeleton|
| Mineralized teeth, armor       |
|                                |
| BURGESS SHALE (508 Ma, Canada) |
| Anomalocaris (apex predator)   |
| Opabinia (5 eyes, trunk)       |
| Hallucigenia (spiny)           |
| Pikaia (possible chordate)     |
| CHENGJIANG FAUNA (520 Ma)      |
| Yunnanozoon, Myllokunmingia    |
+--------------------------------+
WHY the explosion?
- Rising O₂ levels enabling larger active animals
- Arms race dynamics (predation → defense → counter)
- Ecological opportunity (empty niches)
- Hox gene duplication enabling body plan diversification
```

---

## Protostome vs Deuterostome Development

```
EMBRYONIC FATE OF THE BLASTOPORE (the hole in the gastrula)

PROTOSTOMIA                    DEUTEROSTOMIA
+-------------------+          +-------------------+
| Blastopore →      |          | Blastopore →      |
|   MOUTH           |          |   ANUS            |
|                   |          |                   |
| Spiral cleavage   |          | Radial cleavage   |
| Determinate       |          | Indeterminate     |
| (cell fate fixed  |          | (cell fate not    |
|  early)           |          |  fixed early)     |
|                   |          |                   |
| Coelom from       |          | Coelom from       |
| mesoderm splits   |          | outpocketing of   |
| (schizocoely)     |          | gut (enterocoely) |
|                   |          |                   |
| Includes:         |          | Includes:         |
| Annelids, Molluscs|          | Echinoderms       |
| Arthropods,       |          | Hemichordates     |
| Nematodes         |          | Chordates         |
+-------------------+          +-------------------+
```

---

## Module Map — This Series

| File | Topic | Key Groups |
|------|-------|-----------|
| `00-OVERVIEW.md` | This file | Full tree of life |
| `01-SINGLE-CELL-ORIGINS.md` | Prokaryotes → Protists | Bacteria, Archaea, Eukaryota |
| `02-EARLY-ANIMALS.md` | Pre-bilaterian | Sponges, Cnidaria, Ctenophora |
| `03-LOPHOTROCHOZOA-WORMS.md` | Worm-grade lophotrochozoans | Flatworms, annelids, rotifers |
| `04-NEMATODA-ECDYSOZOA.md` | Molting non-arthropod worms | Nematoda, tardigrades, velvet worms |
| `05-MOLLUSCA.md` | Soft-bodied protostomes | Snails, clams, cephalopods |
| `06-ARTHROPODA.md` | Most species-rich phylum | Insects, spiders, crustaceans |
| `07-DEUTEROSTOMES-ECHINODERMS.md` | Deuterostome non-chordates | Sea stars, acorn worms |
| `08-CHORDATA-ORIGINS.md` | Phylum Chordata basal groups | Tunicates, lancelets, vertebrate origin |
| `09-FISH.md` | Aquatic vertebrates | Jawless, cartilaginous, bony, lobe-finned |
| `10-AMPHIBIA.md` | First tetrapods | Frogs, salamanders, caecilians |
| `11-REPTILIA-BIRDS.md` | Amniotes (non-mammalian) | Turtles, lizards, snakes, crocs, birds |
| `12-MAMMALIA.md` | Crown mammals | Monotremes, marsupials, placentals |

---

## Decision Cheat Sheet — Which Phylum Is This?

```
START: You have an animal specimen. What is it?

  Has tissues?
   |
   +-- No  → Porifera (sponge)
   +-- Yes
        |
        Bilateral symmetry?
         |
         +-- NO (radial)
         +-- YES → BILATERIA

  Non-bilaterian options:
    Two germ layers → Cnidaria or Ctenophora
    Simplest body   → Placozoa

BILATERIA:
Blastopore → mouth? → PROTOSTOMIA
  Molts exoskeleton? → ECDYSOZOA
    Jointed legs?   → Arthropoda
    No legs, cuticle→ Nematoda (or Tardigrada/Onychophora)
  Does not molt?    → LOPHOTROCHOZOA
    Segmented body? → Annelida
    Shell/mantle?   → Mollusca
    Flat, no coelom?→ Platyhelminthes

Blastopore → anus? → DEUTEROSTOMIA
  Water vascular system? → Echinodermata
  Notochord at some stage→ Chordata
    Has vertebrae?       → Vertebrata
```

---

## Common Confusion Points

**"Fish" is not a clade.**
"Fish" describes an evolutionary grade — the paraphyletic assemblage of non-tetrapod vertebrates. Lungfish are more closely related to you than to a shark.

**"Reptiles" (traditional) is paraphyletic.**
Birds ARE dinosaurs. The correct clade including all reptiles plus birds is Amniota minus Mammalia, but taxonomists now often use Reptilia to explicitly include birds.

**Sponges and plants are not related.**
Both are sessile filter/photo-producers, but convergent ecology. Sponges are animals.

**Arthropods are not worms.**
"Worm" is a body-shape grade (elongated, limbless) — not a clade. Earthworms (Annelida), flatworms (Platyhelminthes), roundworms (Nematoda), and tapeworms (Platyhelminthes) are in different phyla.

**Coral is an animal.**
Coral polyps are cnidarians. Their color comes from symbiotic dinoflagellates (zooxanthellae) living in their tissues — the algae is expelled during bleaching.

**Invertebrate = not a clade.**
"Invertebrates" = everything except Vertebrata. That's ~96% of animal species, across dozens of unrelated phyla. Useful colloquially, not phylogenetically.

**Convergent complexity in cephalopods.**
Octopus/squid camera eyes and vertebrate camera eyes evolved independently — same physics (lens + retina) but different embryological origin (skin-derived vs brain-derived). The octopus eye is actually better designed: photoreceptors face forward, no blind spot.
