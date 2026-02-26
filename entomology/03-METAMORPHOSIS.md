# Metamorphosis: Complete and Incomplete

## The Big Picture

Metamorphosis is the developmental architecture that separates insects into two major strategies: those where larva and adult share the same body plan (hemimetabola) and those where they are radically different organisms sharing a genome (holometabola). The holometabolous strategy is one of evolution's most successful innovations — it partitioned ecological roles so completely that larva and adult can exploit entirely different resources.

```
METAMORPHOSIS STRATEGIES IN INSECTS
======================================

  AMETABOLOUS            HEMIMETABOLOUS          HOLOMETABOLOUS
  (no metamorphosis)     (incomplete)            (complete)
  ==================     ============            ==============

  Egg                    Egg                     Egg
   |                      |                       |
  Nymph 1                Nymph 1                 Larva 1
  (tiny adult)            (resembles adult)       (completely different)
  Nymph 2                Nymph 2                 Larva 2
  ...                     ...                     ...
  Adult                  Nymph N                 Larva N
                          |                       |
                          Adult                   PUPA
                          (wings appear)          (histolysis/histogenesis)
                                                  |
                                                  Adult (imago)

  Zygentoma              Orthoptera              Coleoptera
  Archaeognatha          Hemiptera               Lepidoptera
                         Odonata                 Hymenoptera
                         Blattodea               Diptera
                         Orthoptera
                         Mantodea

  ~13% of insects        ~87% of insects (Holometabola)
```

---

## Hemimetabolous Development

### The Nymph Series

In hemimetabola, the immature stages (nymphs) resemble adults but lack functional wings and reproductive organs. Each instar adds wing pads that grow progressively. The terminal molt produces a functional adult.

```
HEMIMETABOLOUS DEVELOPMENT (example: grasshopper, Orthoptera)
==============================================================

  Egg
   |  hatching (eclosion)
  Instar 1 (nymph): no wing pads; full complement of legs
   |  ecdysis
  Instar 2: small wing pads visible (thoracic buds)
   |  ecdysis
  Instar 3: wing pads larger
   |  ecdysis
  Instar 4: wing pads cover several abdominal segments
   |  ecdysis
  Instar 5: wing pads nearly full
   |  imaginal molt (final ecdysis)
  ADULT (imago): functional wings, reproductive organs mature

  Each instar is ecologically similar to adult:
  - Same habitat (usually)
  - Same food resources
  - Same predators
  - Gradual developmental progression, no hidden restructuring
```

### Exopterygota — Wings Develop Externally

The defining character of hemimetabola is exopterygous wing development: wing buds are externally visible pads that enlarge through successive molts.

```
EXOPTERYGOUS WING DEVELOPMENT
===============================

  Nymph 3:  [small wing pads on notum]
  Nymph 4:  [larger pads, veins visible]
  Nymph 5:  [pads nearly full-sized, reversed]
  Adult:    [pads evert and expand at imaginal molt]

  The wing pads are the adult wing in compressed/folded form.
  Expansion driven by hemolymph hydraulic pressure at ecdysis.
  No reconstruction from imaginal discs needed.
```

---

## Holometabolous Development

### The Larva-Pupa-Adult Architecture

Complete metamorphosis introduces a dedicated non-reproductive growth phase (larva), a transition capsule (pupa), and a dedicated reproductive phase (adult). Larva and adult can be utterly different organisms morphologically and ecologically.

```
HOLOMETABOLOUS DEVELOPMENT (example: Lepidoptera)
===================================================

  Egg
   |
  Larva (caterpillar):
    - Soft-bodied, prolegs on abdomen (not homologous to thoracic legs)
    - Chewing mouthparts (herbivory)
    - Growth machine: eats constantly, grows 1000x body mass
    - Brain: simple; behavior: largely instinctive
    - Imaginal discs: clusters of undifferentiated cells (set aside early)
    |  L1 -> L2 -> L3 -> L4 -> L5 (5 instars typical)
    v
  PREPUPA: larva stops feeding, wanders, anchors
    |
  PUPA (chrysalis or cocoon):
    HISTOLYSIS: most larval tissues broken down
      - Larval muscles: dissolved
      - Larval gut: reorganized
      - Fat body: persists, provides nutrients
      Imaginal discs escape histolysis (protected by protein coat)
    HISTOGENESIS: imaginal discs proliferate + differentiate
      - Wing discs -> wings
      - Leg discs -> adult legs
      - Eye discs -> compound eyes
      - Antenna discs -> antennae
      - Genital disc -> reproductive organs
    |
  ADULT (imago):
    - Hardened cuticle (sclerotization in first hours)
    - Siphoning mouthparts (proboscis)
    - Compound eyes, wings
    - Reproductive: mate and oviposit
```

### Imaginal Discs: The Key Innovation

```
IMAGINAL DISCS
===============

What they are:
  Monolayer epithelial sheets of ~50-200 undifferentiated cells
  Set aside in embryo; grow by cell division throughout larval life
  Each disc gives rise to one adult structure

Location in larva:
  Wing discs: 3 pairs (fore, mid, hind thorax)
  Leg discs:  3 pairs (one per thoracic segment)
  Eye-antenna disc: 1 pair
  Genital disc: 1 (ventral, posterior)

During pupal histolysis:
  Discs are protected by surface coating (prevents autolysis)
  Ecdysone triggers eversion and differentiation
  Disc cells proliferate, fold into organ shape, differentiate

Size:
  A 3rd instar Drosophila wing disc: ~50 cells
  Same disc at pupal onset: ~50,000 cells
  Cell doubling time: ~8-10 hours (in Drosophila)

This is the reason holometabola can have larvae and adults
with completely incompatible body plans -- the adult is
built fresh from reserved stem-cell-like populations.
```

---

## Hormonal Control

The metamorphic transition is governed by two hormones operating as a binary switch. This is one of the most elegant developmental control systems in biology.

```
HORMONAL REGULATION OF METAMORPHOSIS
======================================

TWO KEY HORMONES:
  JH    = Juvenile Hormone (sesquiterpenoid)
          produced by: corpora allata (CA) behind brain
          function:    "stay juvenile" signal

  20E   = 20-hydroxyecdysone (steroid)
          produced by: prothoracic glands (PTG)
          function:    "molt" trigger

INTERACTION MODEL:
  JH HIGH + 20E LOW   =  growth (intermolt)
  JH HIGH + 20E HIGH  =  larval molt (nymph-to-nymph or larva-to-larva)
  JH LOW  + 20E HIGH  =  metamorphic molt (larva-to-pupa or pupa-to-adult)
  JH ZERO + 20E HIGH  =  terminal molt (-> adult)

JH TITER ACROSS INSTARS (holometabola):
  L1   [JH ||||||||||||||||||||||||]  20E [|] -> larval molt
  L2   [JH ||||||||||||||||||||||||]  20E [|] -> larval molt
  L3   [JH ||||||||||||||||||||||||]  20E [|] -> larval molt
  L4   [JH |||||||||||  ]            20E [||] -> prepupal commitment
  L5   [JH |      ]                  20E [|||||||] -> pupal molt
  Pupa [JH 0]                        20E [|||||||||||||||] -> adult
```

### PTTH: The Upstream Signal

```
NEUROENDOCRINE CASCADE
=======================

  Brain: detects environmental cues (photoperiod, temperature, nutrition)
         when growth complete: releases PTTH
         |
         v
  PTTH (Prothoracicotropic Hormone)
         |
         v
  Prothoracic Glands (PTG) -> release ecdysteroids (20E)
         |
         v
  Target cells: ecdysone receptor (EcR/USP heterodimer)
         |
         v
  Gene expression cascade -> ecdysis behavior + tissue remodeling

  Juvenile Hormone controlled separately:
  Corpora Allata produce JH; Corpus Cardiacum stores/releases
  Brain neuropeptides (PTTH, allatostatins) regulate CA
```

---

## The Diapause System

Diapause is programmed developmental arrest — the insect equivalent of a "hibernate until conditions improve" signal. It can occur at any stage.

```
DIAPAUSE TYPES AND TRIGGERS
=============================

  EMBRYONIC DIAPAUSE:  egg overwinters (Bombyx mori)
  LARVAL DIAPAUSE:     larva halts (some Lepidoptera, Diptera)
  PUPAL DIAPAUSE:      pupa overwinters (most temperate Lepidoptera)
  ADULT DIAPAUSE:      reproductive diapause (monarch butterfly,
                       many beetles, some Diptera)

TRIGGERS (sensed by brain -> neuroendocrine cascade):
  Photoperiod (primary): critical daylength threshold
    Short-day species: enter diapause in autumn (short days)
    Long-day species:  enter diapause in spring (long days)
  Temperature: often modifies photoperiod response
  Nutrition:   poor food can trigger diapause
  Crowding:    in some species (related to locust phase polyphenism)

TERMINATION:
  Cold exposure (chilling requirement) in many temperate species
  Photoperiod change
  Moisture
  JH application can terminate some diapauses (agricultural use)
```

---

## Evolutionary Origin of Holometaboly

```
ORIGIN OF COMPLETE METAMORPHOSIS
==================================

PROBLEM: How did the pupal stage evolve?

CLASSIC HYPOTHESIS (Berlese-Imms):
  Holometabola evolved from ancestors that hatched as protolarvae
  (undeveloped; essentially an "escape from egg" stage)
  Pupa = compressed hemimetabolous nymphal series
  This is still the dominant model

MOLECULAR PHYLOGENIES:
  Holometabola is monophyletic (~230 Mya divergence)
  All holometabolous orders share same imaginal disc system
  Same basic JH/20E regulatory logic
  -> single evolutionary origin of complete metamorphosis

WHY WAS IT SUCCESSFUL?
  1. Larva/adult niche separation eliminates intraspecific competition
     (caterpillar eats leaves; butterfly drinks nectar; no overlap)
  2. Larva optimized for growth; adult for dispersal/reproduction
  3. Pupa permits radical body reorganization impossible in gradual molts
  4. Holometabola = ~87% of insect species -- the radiation speaks for itself
```

---

<!-- @editor[bridge/P2]: No bridge — the JH/20E two-hormone binary switch maps directly to a finite state machine with two control signals; imaginal discs are a biological version of lazy initialization. One bridge would help the learner internalize the developmental architecture -->

## Decision Cheat Sheet

| Term | Meaning | Example |
|------|---------|---------|
| Hemimetabola | Incomplete metamorphosis; nymph -> adult | Grasshoppers, true bugs, dragonflies |
| Holometabola | Complete metamorphosis; larva -> pupa -> adult | Beetles, moths, flies, bees |
| Instar | Stage between molts | "5th instar caterpillar" |
| Imago | Adult insect | Final stage after all molting |
| Ecdysis | The molt itself (shedding old cuticle) | Triggered by 20E |
| Apolysis | Separation of epidermis from old cuticle (precedes ecdysis) | Early stage of molt |
| Juvenile Hormone | "Stay juvenile" signal from corpora allata | High -> larval character |
| 20-hydroxyecdysone | Steroid that triggers molting | Released by PTG via PTTH |
| Imaginal disc | Reserved undifferentiated cells -> adult structure | Wing disc, eye disc |
| Histolysis | Breakdown of larval tissues during pupation | Muscles dissolved |
| Histogenesis | Construction of adult tissues from imaginal discs | During pupation |
| Diapause | Programmed developmental arrest | Pupal overwintering |

---

## Common Confusion Points

**Metamorphosis is not the same as molting**: Molting (ecdysis) is the mechanical shedding of the old cuticle. Metamorphosis is the developmental transformation. Hemimetabola molt without metamorphosis (mostly). Holometabola undergo metamorphosis at the larval-pupal transition.

**Pupa does not "sleep"**: The pupal stage is metabolically active. Extensive tissue remodeling occurs. Neuroscience note: in Drosophila, olfactory memories formed in larvae survive metamorphosis — the mushroom body neurons connecting odor to memory persist through histolysis.

**Larval prolegs are not legs**: The abdominal prolegs of caterpillars are not homologous to the thoracic true legs. True legs = 3 pairs on thorax. Prolegs = fleshy false appendages on abdomen; lost at pupation.

**JH is not "growth hormone"**: JH doesn't cause growth — it specifies the molt type. Without JH, the molt is metamorphic. With JH, it's larval. JH analogs (juvenoids) are used as insecticides: they prevent larvae from completing metamorphosis.

**Not all flies have a "cocoon"**: Butterfly chrysalis = naked hardened pupal shell (pupal cuticle only). Moth cocoon = silk + pupal shell. Fly puparium = hardened last larval cuticle retained around pupa. These are three different structures.
