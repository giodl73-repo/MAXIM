# Animal Development and Evo-Devo

## The Big Picture

Developmental biology studies how a single fertilized cell becomes a complex multicellular organism with hundreds of cell types in precise spatial arrangements. Evolutionary developmental biology (evo-devo) asks how developmental processes evolve — and reveals that macroevolutionary morphological change is largely driven by modifications to gene regulation, not protein sequence changes. The discovery that ~600 Mya diverged organisms share the same genetic toolkit for development was the major surprise of molecular developmental biology.

```
EVO-DEVO CONCEPTUAL MAP
==========================

  DEVELOPMENT (how it happens in one organism)
       |
       v
  Fertilized egg --> Blastula --> Gastrula --> Organogenesis --> Adult
       |                 |            |              |
  Cell division    Cell signaling  Germ layers   Morphogenesis
  Cleavage         Position info   Specified     Pattern formation
                   Gradients       Three layers  Growth control

  EVO-DEVO (how developmental processes evolve)
       |
       v
  Same Hox genes in fruit fly, mouse, whale
  Same cell signaling pathways across phyla
  Changes in gene REGULATION (not sequence) drive morphological evolution
  Heterochrony, heterotopy, heterometry change when/where/how much genes express
```

---

## Early Development: Fertilization to Gastrulation

```
EARLY DEVELOPMENT STAGES
===========================

FERTILIZATION:
  Sperm + egg fusion -> block to polyspermy (fast: membrane depolarization;
  slow: cortical reaction -> zona pellucida hardening)
  Syngamy: pronuclei fuse -> diploid zygote
  Cytoplasmic determinants: maternal mRNA + proteins asymmetrically distributed
    -> establish axes of future embryo BEFORE first cleavage

CLEAVAGE:
  Rapid cell division without growth
  Cytoplasm partitioned among cells (blastomeres)
  Holoblastic: entire egg divided (sea urchin, amphibian, mammal)
  Meroblastic: partial (yolky eggs: bird, fish, reptile)
    Discoidal: bird; only blastodisc cleaves
    Superficial: insect; only surface cleaves
  Determinate (mosaic): blastomere fate fixed early (most protostomes)
  Indeterminate (regulative): blastomere fate not fixed (deuterostomes)
    -> twinning possible; isolated blastomere -> complete embryo

BLASTULA:
  Hollow ball of cells; central blastocoel
  Fate map: spatial correspondence of blastula regions to adult tissues
  Classic fate maps: sea urchin (1921 Hörstadius), amphibian (Vogt 1929)

GASTRULATION:
  Cell movements that establish three germ layers
  Blastopore: site of gastrulation; "lips" → dorsal/ventral
  Ectoderm: outer layer
  Mesoderm: middle layer (arises by invagination/ingression/delamination)
  Endoderm: inner layer -> gut lining
  Archenteron: primitive gut formed by gastrulation
  Spemann organizer (amphibian): dorsal lip of blastopore
    -> induces neural plate; establishes dorsal-ventral axis
    Discovery: transplant dorsal lip -> second embryo on ventral side
    Molecules: Noggin, Chordin (BMP inhibitors) establish dorsal identity
```

---

## Axis Formation and Pattern Specification

```
AXIS FORMATION
================

DROSOPHILA (best understood system):
  Anterior-Posterior axis:
    Bicoid mRNA: localized to anterior pole by cytoskeletal anchor
    Bicoid protein: gradient from anterior -> posterior
    [anterior: high Bicoid] [posterior: low Bicoid, high Nanos]
    Bicoid concentration: determines segment identity threshold
    -> Gradient gives spatial POSITION INFORMATION to nuclei

  Dorsal-Ventral axis:
    Toll receptor: activated on ventral side
    -> NF-kB homolog (Dorsal): enters nuclei ventrally
    -> activates ventral genes; represses dorsal genes
    (Same NF-kB pathway: vertebrate immunity uses same molecule)

VERTEBRATE AXIS:
  A-P axis: established by Spemann organizer + Wnt signaling
  D-V axis: BMP pathway (ventral) vs Chordin/Noggin (dorsal)
    -> SAME BMP pathway as Drosophila D-V axis BUT INVERTED
    (what is "dorsal" in fly corresponds to "ventral" in vertebrate)
    -> axis inversion in bilaterian evolution?
    Gegenbaur (1859) proposed axis inversion; molecular data supports it

  Left-Right axis:
    Nodal cilia: rotate unidirectionally -> leftward extracellular flow
    KIF3A/B kinesin motor: drives ciliary rotation (knockouts: situs inversus)
    Nodal/Lefty/Pitx2 cascade: left side specific; conserved vertebrates
```

---

## Hox Genes: Body Plan Specification

```
HOX GENES AND BODY AXIS IDENTITY
====================================

DISCOVERY:
  Antennapedia mutation (Drosophila): leg where antenna should be
  Bithorax mutation: extra thoracic segment with wings
  Lewis (1978): these map to same gene cluster -> Nobel Prize 1995

HOX GENE CLUSTER:
  Linear arrangement on chromosome correlates with body position
  5' genes expressed in posterior; 3' genes in anterior
  (Spatial colinearity: chromosome position = body position)

  Drosophila ANT-C:  lab  pb  Dfd  Scr  Antp
  Drosophila BX-C:                  Ubx  abd-A  Abd-B
  Vertebrate HoxA:   A1  A2  A3  A4  A5  A6  A7  A9  A10  A11  A13
  (4 vertebrate Hox clusters: Hoxa, Hoxb, Hoxc, Hoxd -- from 2 WGD events)

FUNCTION:
  Transcription factors (homeobox = DNA-binding domain)
  Specify REGIONAL IDENTITY along A-P axis
  Do not directly build structures; regulate downstream morphogenetic genes

HOMEOTIC TRANSFORMATIONS:
  Misexpression of posterior Hox gene in anterior segment
  -> Anterior segment acquires posterior identity
  Vertebrate examples:
    HoxA11 knockout: no radius/ulna (forearm); wrist bones absent
    HoxC8 overexpression: ribs form where there should be none

CONSERVATION (DEEP HOMOLOGY):
  Fly Antp expressed in thoracic segment (legs)
  Mouse HoxC6 expressed in thoracic region (where ribs form)
  -> Paralogous genes; similar expression domain; similar function
  -> 600 million years since separation; same positional function retained
```

---

## Cell Signaling in Development

```
MAJOR DEVELOPMENTAL SIGNALING PATHWAYS
=========================================

These ~6-8 pathways are re-used repeatedly across development in all animals.
"Re-used" = same molecules, different contexts = "toolkit" concept.

WNT PATHWAY:
  Ligand: Wnt proteins (19 in humans)
  Receptor: Frizzled + LRP
  Canonical: stabilizes beta-catenin -> transcription factor (nuclear)
  Functions: A-P axis; neural development; stem cell maintenance; cancer
  Mutated in: ~50% of colorectal cancers (APC gene: Wnt pathway component)

NOTCH PATHWAY:
  Ligand: Delta/Jagged (on adjacent cell; cell-to-cell contact required)
  Receptor: Notch (membrane; cleaved on activation)
  Function: lateral inhibition; fate decisions; somitogenesis clock
  Lateral inhibition: if one cell becomes neuron (expresses Delta)
    -> neighboring cells inhibited via Notch -> cannot become neurons
    -> spacing + patterning of neural cells

HEDGEHOG (SHH) PATHWAY:
  Ligand: Sonic Hedgehog (SHH); Indian Hedgehog (IHH)
  Function: CNS patterning; limb development; hair follicle; lung branching
  SHH in limb: secreted from Zone of Polarizing Activity (ZPA = posterior limb)
    -> gradient specifies digit identity (high SHH = pinky; low = thumb)
  Mutation: polydactyly (SHH ectopic expression); holoprosencephaly

FGF PATHWAY:
  Fibroblast Growth Factors (~23); FGFRs (~4)
  Function: mesodermal induction; limb outgrowth; lung branching
  FGF8: maintains limb bud growth; knock out -> no limbs

BMP PATHWAY:
  Bone Morphogenetic Proteins (26+ ligands)
  Functions: D-V axis; bone formation; apoptosis; neural restriction
  BMP4 inhibition: neural plate induction (BMP off = neural fate)
  BMP4 active: epidermal fate
  Inhibitors (Noggin, Chordin, Follistatin): create BMP-free domains

RECEPTOR TYROSINE KINASE:
  Growth factors (EGF, PDGF, etc.) -> Ras -> MAPK cascade
  Function: proliferation; differentiation; survival
  Mutations: most human cancers (Ras: ~30% of cancers; EGF receptor amplified)
```

---

## Evo-Devo: How Development Evolves

### The Toolkit and Modularity

```
THE TOOLKIT HYPOTHESIS
========================

OBSERVATION: Animals as different as fly and mouse share same signaling pathways,
             same Hox genes, same Pax6 for eyes, same Nkx2-5 for hearts.

IMPLICATION: The protein-coding toolkit was largely complete in the Cambrian.
             Macroevolutionary change is driven by REGULATORY evolution
             (changes in when/where/how much genes are expressed)
             not by new gene sequences.

CATACLYSM EVIDENCE: Most large animals use essentially the same set of ~20-25
                    transcription factor families and signal transduction pathways.
                    Innovation comes from deploying them in new combinations.

CIS-REGULATORY ELEMENTS (CREs) / ENHANCERS:
  Non-coding DNA sequences that control gene expression
  Bind transcription factors -> activate/repress target gene
  Each gene may have dozens of independent enhancers (modularity)
  Modular control: change one enhancer -> change expression in one tissue
                   without affecting other tissues (pleiotropy avoidance)

  Example: stickleback spine reduction:
    Freshwater stickleback: reduced pelvic spines (no predators)
    Marine stickleback: large pelvic spines (predator defense)
    GENE: Pitx1 (same gene in both)
    CHANGE: pelvic enhancer of Pitx1 deleted in freshwater populations
    -> Pitx1 still expressed in other tissues; only pelvic fin affected
    -> Independent cis-regulatory change; same gene; tissue-specific
```

### Heterochrony and Heterotopy

```
MECHANISMS OF EVO-DEVO CHANGE
================================

HETEROCHRONY: change in timing of developmental events
  Paedomorphosis: adult retains juvenile features
    Neoteny (slow somatic development; reproductive timing normal):
      Axolotl (Ambystoma mexicanum): sexually mature but never undergoes
      full metamorphosis; stays aquatic; neotenic
      Human neoteny (Gould proposal): humans retain juvenile ape features
        (large head, flat face, hairlessness) relative to adults
    Progenesis (early sexual maturation; rest of development truncated):
      Many cave animals: small, sexually mature quickly
  Peramorphosis: adult exceeds ancestral juvenile condition

  EXAMPLE: Giant Panda skull
    Large, round face evolved from small carnivore ancestor
    Heterochrony: retention of juvenile skull proportions
    + enlarged masseter muscles for bamboo chewing

HETEROTOPY: change in position of developmental expression
  Same gene/process; different spatial domain
  Example: limb reduction in snakes
    Hox genes that specify limb position still present
    Expression domain shifted: SHH not expressed in forelimb region
    -> Forelimbs absent; vestigial hindlimb bones in pythons
  Cetacean forelimb -> flipper:
    Same Hox genes; modified regulatory regions -> shorter digits; webbed

HETEROMETRY: change in amount of expression
  Up/down-regulation without timing or spatial change
  Beak depth in Darwin's finches (Geospiza): BMP4 levels
    High BMP4 in beak mesenchyme -> deeper beak (cactus finch)
    Low BMP4 -> shallow beak (warbler finch)
    Not a new gene; not new protein; different amount of same BMP4
```

---

## Model Organisms in Developmental Biology

```
KEY MODEL ORGANISMS
====================

Drosophila melanogaster:
  ~14,000 genes; 3-day generation; forward + reverse genetics
  Gap genes, pair-rule, segment polarity: A-P segmentation complete
  Nobel: Morgan 1933 (chromosome theory); Lewis/Nusslein-Volhard/Wieschaus 1995 (body plan)

Xenopus laevis / tropicalis:
  Large eggs (1mm); easy microinjection; organizer transplantation
  Spemann organizer (1924 Nobel); gastrulation mechanics
  Tadpole -> frog metamorphosis; thyroid hormone regulation

Caenorhabditis elegans:
  959 cells; complete cell lineage known; transparent; 3-day generation
  Apoptosis (Sulston, Brenner, Horvitz Nobel 2002); developmental timing; aging
  Complete connectome (302 neurons); first metazoan genome sequenced (1998)

Danio rerio (zebrafish):
  Transparent embryos; optical imaging; large-scale forward genetics
  Hearts; fins; pigmentation; regeneration (can regenerate heart after partial resection)
  Fast: fertilization to 24h: complete body plan visible

Mus musculus (mouse):
  ~90% genome conserved with human; conditional knockouts (Cre-lox)
  Most mammalian development studies; placentation; organogenesis

Strongylocentrotus purpuratus (sea urchin):
  Gene Regulatory Network (GRN): most completely mapped animal GRN
  200 cells at blastula; all transcription factor connections known in early stages
  Davidson (2006): endomesoderm GRN (~60 genes; complete causative diagram)
```

---

## Decision Cheat Sheet

| Process | When | Key molecules | Consequence if disrupted |
|---------|------|---------------|--------------------------|
| A-P axis specification | Early cleavage | Bicoid/Nanos gradient (insect); Wnt (vertebrate) | Segmentation defects |
| Neural induction | Gastrulation | BMP inhibition (Noggin, Chordin) | No neural plate |
| Hox specification | Early organogenesis | Hox genes (A1-D13 in vertebrates) | Homeotic transformations |
| Limb patterning | Organogenesis | SHH (digits); FGF8 (growth); Wnt (D-V) | Polydactyly, missing limbs |
| Lateral inhibition | Throughout | Notch-Delta | Excess neurons or none |
| Cell death (apoptosis) | Throughout | Caspases; Bcl-2 family | Webbed fingers; brain malformation |

---

## Common Confusion Points

**Evo-devo and "protein sequence change"**: The central insight is that most macroevolutionary morphological change is driven by regulatory evolution (enhancer changes) not protein-coding sequence changes. The protein toolkit is conserved; the regulatory wiring changes. This is why you can see identical proteins (SHH, BMP4, Pax6) deployed in radically different morphological contexts.

**Homeotic mutations are not "hopeful monsters"**: A homeotic mutation (leg where antenna) demonstrates that the gene specifies position identity. It is not the mechanism by which evolution proceeds. Evolution of new body plans involves many small regulatory changes; homeotic mutations are experimental probes of what a gene does.

**Gastrulation mechanism varies across animal phyla**: Gastrulation = forming three germ layers. The mechanism (invagination vs ingression vs delamination vs epiboly) varies greatly. The OUTPUT (three germ layers + archenteron) is conserved; the MECHANISM varies. Don't assume the sea urchin model applies to insects or vertebrates.

**The Spemann organizer was the first major transplant demonstration**: Spemann and Mangold (1924, Nobel 1935): transplant dorsal blastopore lip to ventral side -> second embryo forms on ventral side. Shows organizer secretes diffusible signals. The signals turned out to be BMP inhibitors (not activators of dorsal fate — just blockers of ventral default).

**Neoteny as human evolution**: Gould's argument that humans are neotenous relative to great apes (retaining juvenile skull proportions into adulthood) is interesting but contested. Some features fit (retention of juvenile face); others don't (brain continues growing; humans have much longer developmental delay than predicted by simple neoteny). "Developmental life history evolution" is more nuanced than simple neoteny.
