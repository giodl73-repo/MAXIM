# Synthetic Biology and Astrobiology

## The Big Picture

```
+-----------------------------------------------------------------------+
|              SYNTHETIC BIOLOGY / ASTROBIOLOGY INTERSECTION            |
+-----------------------------------------------------------------------+
|                                                                       |
|  TOOL DIRECTION: SYNBIO --> ASTROBIOLOGY                             |
|  +-------------------------------------------------+                 |
|  | Build alien-like biochemistries to understand   |                 |
|  | what "life" fundamentally requires              |                 |
|  | Test whether alternatives to DNA/RNA/protein    |                 |
|  | are capable of Darwinian evolution              |                 |
|  +-------------------------------------------------+                 |
|                                                                       |
|  APPLICATIONS:                                                        |
|  +-------------------+  +-------------------+  +---------------+    |
|  | XENOBIOLOGY       |  | MINIMAL GENOME    |  | SYNTHETIC     |    |
|  | XNA, alt. genetic |  | What is the       |  | CELLS         |    |
|  | codes, non-       |  | minimum set of    |  | Bottom-up     |    |
|  | canonical AAs     |  | genes for life?   |  | construction  |    |
|  +-------------------+  +-------------------+  +---------------+    |
|                                                                       |
+-----------------------------------------------------------------------+
```

Synthetic biology turns astrobiology questions into experiments: instead of asking "what life could exist elsewhere," it asks "can we build life with different chemistry and make it work?" This is the hardest empirical test of theories about the universality of biochemistry.

---

## Xenobiology: Alternative Genetic Polymers

```
THE CENTRAL DOGMA AND ITS ALTERNATIVES
========================================

STANDARD CENTRAL DOGMA:
  DNA --> RNA --> Protein
  Information storage: DNA (deoxyribose backbone)
  Catalysis: Proteins
  Information transfer: RNA

QUESTION FOR ASTROBIOLOGY:
  Is the ribose backbone (RNA) or deoxyribose backbone (DNA)
  chemically inevitable, or is it one solution among many?

XNA: XENO NUCLEIC ACIDS
  Replace the sugar backbone with alternative chemistry.
  Still use the same 4 bases (A, T/U, G, C) but different backbone.

SYNTHETIC ALTERNATIVE BACKBONES:
+------+---------------------+-----------------------------------+
| Name | Backbone            | Properties                        |
+------+---------------------+-----------------------------------+
| TNA  | Threose nucleic acid| 4-carbon sugar; simpler than RNA  |
|      |                     | Can template RNA synthesis        |
|      |                     | Precursor to RNA world?          |
+------+---------------------+-----------------------------------+
| HNA  | Hexitol nucleic acid| 6-carbon hexitol                  |
|      |                     | Watson-Crick base pairing with RNA|
|      |                     | Can evolve (in vitro selection)   |
+------+---------------------+-----------------------------------+
| FANA | 2'F-arabino nucleic | Fluorine substitution             |
|      | acid                | Nuclease resistant                |
|      |                     | First XNA shown to evolve         |
|      |                     | (Pinheiro et al. 2012, Science)  |
+------+---------------------+-----------------------------------+
| LNA  | Locked nucleic acid | Bicyclic backbone                 |
|      |                     | Very high Tm, stable              |
|      |                     | Therapeutic applications          |
+------+---------------------+-----------------------------------+
| CeNA | Cyclohexene nucleic | Cyclohexene ring                  |
|      | acid                | Cross-pairs with DNA and RNA      |
+------+---------------------+-----------------------------------+

KEY RESULT (Pinheiro et al. 2012, Science):
Six XNAs (TNA, HNA, CeNA, LNA, FANA, ANA) can:
1. Store genetic information (like DNA)
2. Be read and copied by engineered polymerases
3. Evolve in vitro to bind target molecules (aptamers)

INTERPRETATION: The specific chemistry of RNA/DNA backbones is
not required for genetic information storage and evolution.
Life on other worlds might use alternative polymers.
```

---

## Expanded Genetic Code

```
NON-CANONICAL AMINO ACIDS (ncAAs)
====================================

Standard genetic code: 64 codons, 20 amino acids + stop
(plus selenocysteine #21 in some organisms)

EXPANDING THE CODE:
  Stop codons (UAG, UAA, UGA) can be "hijacked" to encode
  a new amino acid if you:
  1. Supply orthogonal tRNA + orthogonal synthetase
  2. Suppress natural stop codon readthrough
  3. Engineer out release factors for the codon (amber suppression)

CHIN LAB (Cambridge) / SCHULTZ LAB (Scripps):
  Incorporated >150 non-canonical amino acids into living bacteria
  using amber (UAG) suppression
  Examples of capabilities added:
  - Photo-cross-linkers (photo-activatable crosslinks for protein
    interaction studies)
  - Bio-orthogonal chemistry handles (click chemistry, biotin)
  - Fluorescent amino acids
  - Metal-chelating amino acids

MOST RADICAL: RECODED GENOME (Chin 2019, Nature)
  Rebuilt the entire E. coli genome with all UAG codons replaced
  by alternative synonyms (51 codons compressed to 61)
  Result: codon-compression allows UAG to be freed entirely
  Then: amber is reassigned exclusively to new amino acid
  Cell now has 21-amino acid genetic code!
  Cell cannot exchange genetic material with natural bacteria
  (genetically isolated -- biosafety feature)

ASTROBIOLOGICAL IMPLICATION:
  The genetic code is not uniquely optimal.
  Life with different codon assignments is viable.
  Life on other worlds might use:
  - More or fewer amino acids
  - Different codon assignments
  - Different "stop" mechanisms
  The canonical genetic code is one solution, not the only one.
```

---

## Minimal Genomes: JCVI-Syn3.0

```
JCVI MINIMAL GENOME PROJECT
=============================

Goal: determine the minimum set of genes required for cellular life.

HISTORY:
1995: First sequenced genome (Haemophilus influenzae, ~1,800 genes)
1995: First synthetic genome (Craig Venter institute)
2010: Synthia (JCVI-syn1.0) -- first cell with entirely synthetic genome
      Mycoplasma mycoides JCVI-syn1.0: genome designed by computer,
      synthesized by chemical synthesis, transplanted into cell.
      1.08 Mb, 473 genes.
      "First self-replicating synthetic bacterial cell."

2016: JCVI-syn3.0 -- MINIMAL GENOME
      Method: systematic gene knockouts to find essential genes
      Result: 531,000 bp, 473 protein-coding genes
      + 35 genes with no known function (essential but unknown!)

JCVI-syn3.0 GENE CATEGORIES:
+-----------------------------------+------------------+
| Function                          | Genes            |
+-----------------------------------+------------------+
| Genome expression (transcr./transl)| 195 (41%)       |
| Cell membrane + cell division     | 84 (18%)         |
| Cytosolic metabolism              | 81 (17%)         |
| DNA replication/repair            | 34 (7%)          |
| Cell membrane + lipids            | 31 (7%)          |
| Transport                         | 17 (4%)          |
| Unknown function (essential!)     | 35 (7%)          |
+-----------------------------------+------------------+

THE 35 UNKNOWN-FUNCTION ESSENTIAL GENES:
This is the profound result.
7% of the essential genes for life have NO KNOWN FUNCTION.
We don't know what they do, but the cell dies without them.
Life has secrets we haven't deciphered.

IMPLICATION FOR ASTROBIOLOGY:
What is the truly "minimal" life?
Viroids (naked RNA) can replicate but require host machinery.
A free-living cell requires ~473 genes minimum.
This sets a complexity floor for what we're looking for.
```

---

## Bottom-Up Synthetic Cells

```
BOTTOM-UP SYNTHETIC CELL CONSTRUCTION
=======================================

APPROACH: Assemble a cell from purified components.
No cell chassis, no transplanted genome.
Pure chemistry assembling into something cell-like.

KEY SYSTEMS:

1. GENE EXPRESSION IN VITRO (Noireaux & Libchaber 2004):
   Purified transcription/translation machinery from E. coli.
   Encapsulated in lipid vesicles.
   Added DNA template.
   Result: protein synthesis inside a vesicle.
   First "cell-free" expression in a protocell analog.

2. COUPLED TRANSCRIPTION-TRANSLATION-REPLICATION:
   Multiple groups: encoding RNA polymerase on the enclosed DNA.
   DNA --> RNA polymerase mRNA --> RNA polymerase protein --> copies DNA
   Self-encoding system in a vesicle.
   Not fully autonomous, but key steps demonstrated.

3. VESICLE DIVISION:
   Szostak lab: fatty acid vesicles grow by addition of lipid micelles.
   When grown large, will divide into daughters.
   Non-enzymatic! Thermodynamic driving force.
   Connection to lipid world hypothesis.

4. CURRENT FRONTIER (2025):
   BaSyC (Netherlands) / MaxSynBio (Germany) consortia:
   Building a minimal cell from scratch.
   Need: self-replication of DNA + membrane growth + division
   All coupled and self-sustaining.
   Not yet achieved fully.

WHAT SUCCESS WOULD MEAN:
  If we build a functioning cell from pure chemistry,
  we demonstrate that abiogenesis is in principle straightforward.
  The specific chemistry used tells us what constraints are universal.
```

---

## Alternative Solvents

```
ALTERNATIVE BIOCHEMISTRIES: OTHER SOLVENTS
==========================================

FORMAMIDE (HCONH2):
  Boiling point: 210 C (vs. water 100 C)
  Freezing point: 2.5 C
  High polarity (similar to water)
  Nucleobase synthesis from formamide: adenine, guanine, cytosine,
  uracil all synthesize from concentrated formamide under UV/heat
  Ribonucleoside phosphates synthesized from formamide by Saladino et al.
  Problem: formamide requires concentration; dilute conditions degrade products.
  Prebiotic chemistry may have used formamide in dry/hot environments.

AMMONIA (NH3):
  Liquid range: -77 to -33 C (at 1 atm)
  Hydrogen bonding: yes (N-H...N)
  Solvent properties: similar to water, different dielectric
  Potential biochemistry on cold bodies (Europa before ocean froze?)
  Lab challenges: difficult to work with below -33 C

SUPERCRITICAL CO2:
  Above 31 C and 74 atm: supercritical fluid
  Non-polar solvent -- could support non-polar biochemistry
  Most biopolymers are insoluble in supercritical CO2
  Speculative; no experimental progress on CO2-based life

SULFURIC ACID:
  Venus cloud hypothesis (see 03-HABITABLE-ENVIRONMENTS)
  Concentrated H2SO4 is a desiccant and oxidant
  Destroys most biomolecules
  Some organisms tolerate dilute sulfuric acid (pH 0)
  Not the same as concentrated H2SO4 environment of Venus clouds
```

---

## Biosafety and Dual-Use Concerns

```
BIOSAFETY CONSIDERATIONS
==========================

PLANETARY PROTECTION (outward):
  Synthetic organisms designed for astrobiology experiments
  on Mars or other bodies would represent novel contamination
  that could confuse future biosignature searches.
  COSPAR: any organism sent to a body of astrobiological
  interest must be cataloged, sterilized, or contained.

BIOSAFETY LEVELS FOR SYNTHETIC ORGANISMS:
  Engineered organisms are assessed on:
  - Novel capabilities (pathogens, toxic synthesis)
  - Ability to escape and persist in environment
  - Horizontal gene transfer risk

  Genetically isolated organisms (recoded genome, non-canonical AAs,
  XNA-based life) are generally considered SAFER:
  - Cannot exchange genes with natural organisms
  - Cannot survive in natural environments without supplied precursors
  - This is a biosafety feature, not just an academic quirk

GAIN-OF-FUNCTION PARALLEL:
  Synthetic biology for astrobiology sometimes involves:
  - Making organisms more radiation-resistant
  - Making organisms survive in low water activity
  - Testing "minimal life" designs

  These capabilities are dual-use. A radiation-resistant microorganism
  could be (theoretically) weaponized.
  The scientific community has self-governance mechanisms:
  - ISSCR guidelines (for stem cell research)
  - IAP guidelines (for synthetic biology)
  - Oversight varies significantly by country
```

---

## CRISPR in Extremophile Engineering

```
CRISPR APPLICATIONS IN ASTROBIOLOGY
======================================

ENGINEERING EARTH ORGANISMS FOR SPACE:
  Goal: engineer microbes that can survive Mars surface conditions.
  Applications:
  - Terraforming (speculative, controversial)
  - In-situ resource utilization (ISRU) -- producing organics on Mars
  - Biosensors for astronaut life support

  CURRENT WORK:
  Rothschild lab (NASA Ames): engineering cyanobacteria for Mars
  Synechococcus (cyanobacteria) + CRISPR modifications:
  - Enhanced desiccation tolerance (ectoine production)
  - UV radiation resistance
  - Perchlorate tolerance

  These are proof-of-concept experiments, not space-ready organisms.

UNDERSTANDING EXTREMOPHILE MECHANISMS:
  CRISPR allows precise insertion of extremophile genes into
  model organisms to test which genes are sufficient for
  specific tolerances.
  Deinococcus: which specific genes confer radiation resistance?
  (Beyond RecA and nucleoid condensation -- additional factors?)
  Systematic deletion studies: ongoing.

  "If we understand what makes Deinococcus resistant,
  we understand the molecular minimum for surviving Mars."
```

---

## Decision Cheat Sheet

| Question | Answer | Key ref |
|---|---|---|
| Can non-DNA polymers store and evolve information? | Yes — HNA, FANA shown to evolve in vitro | Pinheiro 2012 |
| What is the minimum number of genes for life? | ~473 (JCVI-syn3.0) | Hutchison 2016 |
| Is water the only possible biochemical solvent? | Formamide and ammonia are alternatives; speculative | Saladino 2012 |
| Can we build a cell from scratch? | Partial — gene expression in vesicles yes; full cell no | BaSyC consortium |
| Can we add new amino acids to the genetic code? | Yes — >150 ncAAs incorporated in bacteria | Chin/Schultz labs |
| Can we make organisms for Mars? | Engineering experiments ongoing, not space-ready | Rothschild NASA |

---

## Common Confusion Points

**"XNA life means aliens probably use XNA."**
XNA research demonstrates that alternative backbones can work. It does not predict what life elsewhere uses. It establishes that the space of possible biochemistries is larger than CHON + ribose/deoxyribose. It makes us more open to biochemical diversity without specifying what that diversity is.

**"JCVI-syn3.0 is artificial life."**
Synthia and JCVI-syn3.0 use synthetic DNA (chemically synthesized) but transplanted into a natural cell chassis (enucleated Mycoplasma). The cell machinery (ribosomes, enzymes, membranes) is natural. It is closer to "cell with synthetic genome" than "life built from scratch." Bottom-up synthetic cells (BaSyC) are working toward the truly from-scratch version.

**"35 unknown essential genes means we don't understand life."**
It means we don't fully understand the minimal cell. 7% of essential genes in the simplest free-living cell have no known function. This is a gap in biochemistry, not in physics. Presumably they do something — structural, regulatory, metabolic — that hasn't been characterized. It's a humbling reminder that even our model organism is not fully characterized.

**"If we can engineer radiation-resistant organisms, that proves panspermia."**
Engineering a radiation-resistant organism tells us what molecular mechanisms are required for that tolerance. It doesn't say anything about whether natural organisms with those properties transferred between planets. The existence of tardigrades and Deinococcus already establishes that natural radiation resistance is achievable.

**"Synthetic biology for astrobiology is dangerous."**
Some engineered organisms represent biosafety concerns. However, organisms designed for astrobiology applications (surviving space, low water activity, radiation) are typically engineered with multiple auxotrophies (nutritional dependencies) so they cannot survive in nature. The "genetically isolated" organisms (recoded genome) are additionally biosafe. The concern is real but manageable with proper oversight.
