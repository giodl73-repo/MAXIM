# Bacterial Biology

## The Big Picture

```
BACTERIAL CELL: A SIMPLE BUT SOPHISTICATED AGENT
==================================================

  CELL ANATOMY:
  ┌─────────────────────────────────────────────────────────────────┐
  │  GRAM-POSITIVE                    GRAM-NEGATIVE                 │
  │                                                                 │
  │  ┌──────────────────┐             ┌─────────────────────────┐   │
  │  │ Thick             │             │ Outer membrane          │   │
  │  │ Peptidoglycan    │             │ (LPS in gram-)          │   │
  │  │ (20–80 nm)       │             │ Thin peptidoglycan      │   │
  │  ├──────────────────┤             │ (2–7 nm)                │   │
  │  │ Cytoplasmic      │             │ Periplasmic space        │  │
  │  │ membrane         │             │ Cytoplasmic membrane    │   │
  │  │                  │             │                         │   │
  │  │ Cytoplasm:       │             │ Cytoplasm               │   │
  │  │ Nucleoid (DNA)   │             │ Nucleoid (circular DNA) │   │
  │  │ Ribosomes (70S)  │             │ Ribosomes (70S)         │   │
  │  │ Plasmids         │             │ Plasmids                │   │
  │  └──────────────────┘             └─────────────────────────┘   │
  │  Examples: Staphylococcus,       Examples: E. coli, Salmonella, │
  │  Streptococcus, Bacillus,         Pseudomonas, H. influenzae,    │
  │  Clostridium, Listeria            N. meningitidis                 │
  └─────────────────────────────────────────────────────────────────┘

  GRAM STAIN (clinical workhorse):
  Crystal violet → Gram+ retains purple (thick wall traps dye)
  Crystal violet → Gram- decolorized by alcohol (outer membrane disrupted)
  Safranin counterstain → Gram- stains pink/red
  Result in 1 hour → guides antibiotic choice before culture available
```

---

## Cell Structure Details

### Gram Staining and Cell Wall

```
  CELL WALL CHEMISTRY
  ====================

  PEPTIDOGLYCAN (murein):
  Alternating N-acetylglucosamine (NAG) and N-acetylmuramic acid (NAM)
  Cross-linked by peptide bridges
  Gives shape + osmotic protection

  GRAM-POSITIVE EXTRAS:
  ─ Teichoic acids: Polyol-phosphate polymers in peptidoglycan
  ─ Lipoteichoic acids: Anchored to membrane, extend to surface
  ─ Detected by: TLR2 (innate immune recognition)

  GRAM-NEGATIVE EXTRAS:
  ─ Outer membrane: Phospholipid bilayer, asymmetric
  ─ LPS (lipopolysaccharide):
    Lipid A: Embedded in outer leaflet → TLR4 agonist → endotoxin
    Core: Conserved oligosaccharide
    O-antigen: Highly variable polysaccharide → bacterial serotyping
  ─ Porins: β-barrel channels in outer membrane (passive transport)
  ─ Periplasmic space: Between inner and outer membranes
    Contains: β-lactamases (destroy penicillins), drug efflux proteins

  ANTIBIOTIC TARGETS IN CELL WALL:
  β-lactam antibiotics: Block penicillin-binding proteins (PBPs)
    → PBPs are transpeptidases that cross-link peptidoglycan
    → Weakened cell wall → osmotic lysis
  Vancomycin: Binds D-Ala-D-Ala terminus of peptide bridge
    → Blocks transpeptidase substrate access
  Polymyxins: Disrupt outer membrane (gram-negative specific)

  EXCEPTIONS (neither gram+ nor gram-):
  Mycobacteria: Acid-fast stain; mycolic acid-rich wall (waxy)
    → Impermeable → many antibiotics don't penetrate
    → TB: requires months of therapy
  Mycoplasma: No cell wall → intrinsically resistant to β-lactams
```

---

## Bacterial Growth

```
  BACTERIAL GROWTH KINETICS
  ===========================

  BINARY FISSION: One cell → two daughter cells
  Doubling time varies:
    E. coli: ~20 minutes (favorable conditions)
    Mycobacterium tuberculosis: ~20 hours
    Treponema pallidum: ~30 hours (syphilis — hard to culture)

  GROWTH CURVE:
  ┌───────────────────────────────────────────────────────────────┐
  │       Log N│                                                  │
  │            │              ╔══════╗                            │
  │            │          ╔═══╝      ╚═══╗                        │
  │            │      ╔═══╝               ╚══╗                    │
  │            │  ╔═══╝                       ╚═══                │
  │            │══╝                                               │
  │            └───────────────────────────────────────────────── │
  │                Lag   Exponential  Stationary   Death          │
  │                                                               │
  │ LAG PHASE:     Adaptation, enzyme synthesis, DNA repair       │
  │ EXPONENTIAL:   Maximum growth rate; most antibiotic-sensitive │
  │ STATIONARY:    Nutrient limitation; stress responses          │
  │ DEATH PHASE:   Toxic products, nutrient depletion             │
  └───────────────────────────────────────────────────────────────┘

  MINIMUM INHIBITORY CONCENTRATION (MIC):
  Lowest [antibiotic] that prevents visible growth
  MIC ≤ breakpoint → susceptible; MIC > breakpoint → resistant
  Breakpoints: Set by EUCAST or CLSI based on pharmacokinetics

  BIOFILM GROWTH (different from planktonic):
  Sessile bacteria in matrix are 100–1,000x more resistant to antibiotics
  Different physiology: slow growth, altered gene expression
  Clinical problem: Catheters, prosthetic joints, chronic infections
```

---

## Bacterial Metabolism

```
  METABOLIC DIVERSITY
  ====================

  ENERGY SOURCE:
  Chemotrophs: Chemical energy (organic = chemoorganotrophs; inorganic = chemolithotrophs)
  Phototrophs: Light energy

  CARBON SOURCE:
  Heterotrophs: Organic carbon (sugars, amino acids)
  Autotrophs: CO₂ fixation

  ELECTRON ACCEPTOR:
  Aerobic: O₂ → H₂O
  Anaerobic: NO₃⁻, SO₄²⁻, Fe³⁺, CO₂, fumarate → different products

  THE METABOLIC MATRIX:
  ┌────────────────────────────────────────────────────────────────┐
  │ Photoautotrophs:  Cyanobacteria (produced Earth's O₂),         │
  │                   purple/green sulfur bacteria                 │
  │                                                                │
  │ Chemoheterotrophs: Most human pathogens (E. coli, Staph, Strep)│
  │                    Fermenters, aerobic respirers               │
  │                                                                │
  │ Chemolithotrophs:  "Eat rocks"; sulfur oxidizers (Thiobacillus)│
  │                    Iron oxidizers, hydrogen oxidizers          │
  │                    Important in acid mine drainage, deep sea   │
  │                                                                │
  │ Nitrogen fixers:   Rhizobium (in root nodules), Azotobacter,   │
  │                    Clostridium (anaerobic)                     │
  │                    Nitrogenase enzyme: N₂ + 8H⁺ → 2NH₃ + H₂    │
  │                    (ATP-expensive; inhibited by O₂)            │
  └────────────────────────────────────────────────────────────────┘

  FERMENTATION vs. RESPIRATION:
  FERMENTATION: No external electron acceptor
    → Substrate-level phosphorylation only
    → Products: Lactic acid (homofermentative Lactobacillus)
                Ethanol + CO₂ (Saccharomyces — connection to fermentation-spirits/)
                Mixed acid (E. coli), butyrate (Clostridium)

  AEROBIC RESPIRATION: O₂ as terminal electron acceptor
    → ETC (electron transport chain) + ATP synthase
    → ~30–32 ATP per glucose (vs. 2–3 for fermentation)

  ANAEROBIC RESPIRATION: Non-O₂ electron acceptor
    → Sulfate reducers: SO₄²⁻ → H₂S (produces H₂S in sediments)
    → Nitrate reducers: NO₃⁻ → N₂ (denitrification)
    → Iron reducers: Fe³⁺ → Fe²⁺ (important in soil)
```

---

## Horizontal Gene Transfer (HGT)

```
  HORIZONTAL GENE TRANSFER: CODE SHARING BETWEEN ORGANISMS
  ==========================================================

  In software terms: HGT is like runtime loading of new modules
  from external sources — even from different "codebases" (species).
  The genome is not fixed; it's dynamically reconfigurable.

  THREE MECHANISMS:
  ┌──────────────────────────────────────────────────────────────────┐
  │                                                                  │
  │  TRANSFORMATION                                                  │
  │  ─────────────                                                   │
  │  Cell takes up naked DNA from environment                        │
  │  "Competent cells": Express DNA uptake machinery                 │
  │  Natural: Streptococcus pneumoniae (Griffith's experiment 1928)  │
  │  Artificial: Heat shock or electroporation for lab transformation│
  │                                                                  │
  │  TRANSDUCTION                                                    │
  │  ──────────────                                                  │
  │  Bacteriophage accidentally packages bacterial DNA               │
  │  → Infects new bacterium → delivers packaged bacterial DNA       │
  │  Generalized: Random bacterial DNA packaged (Pac site error)     │
  │  Specialized: Lambda phage → only flanking genes transferred     │
  │                                                                  │
  │  CONJUGATION                                                     │
  │  ─────────────                                                   │
  │  Direct cell-to-cell contact via pilus + mating bridge           │
  │  Plasmid with tra (transfer) genes: F-plasmid in E. coli         │
  │  Transfers plasmid DNA unidirectionally                          │
  │  Most clinically important for resistance spread                 │
  │  Resistance plasmids can transfer between species: E. coli →     │
  │  Klebsiella → Acinetobacter                                      │
  └──────────────────────────────────────────────────────────────────┘

  HGT AND BACTERIAL EVOLUTION:
  ─ HGT makes bacterial evolution non-tree-like (web of life)
  ─ Resistance genes travel on plasmids between species/genera
  ─ Pathogenicity islands: Blocks of virulence genes acquired by HGT
  ─ Rate: Can occur in minutes (conjugation faster than cell division)
  ─ The Pangenome: Core genome (all strains) + accessory genome (some strains)
    E. coli pangenome: Core ~2,000 genes; total >90,000 different genes

  PLASMID BIOLOGY:
  ─ Extrachromosomal circular DNA, 1–1,000 kb
  ─ Replicate independently (origin of replication)
  ─ Transfer independently of chromosome
  ─ Resistance plasmids may carry multiple resistance genes at once
  ─ Conjugative plasmids: Self-transmissible (carry tra genes)
  ─ Non-conjugative plasmids: Transfer only with helper plasmid
  ─ Copy number: 1–2 copies (low) to >100 copies (high-copy ColE1)
```

---

## Bacterial Genetics: The Core Mechanisms

```
  BACTERIAL CHROMOSOME
  =====================

  ORGANIZATION:
  ─ Single circular chromosome (most bacteria)
  ─ Some: Linear chromosome (Borrelia, Streptomyces)
  ─ Some: Multiple chromosomes (Vibrio cholerae: 2 chromosomes)
  ─ E. coli K-12: 4.6 Mb, ~4,400 genes
  ─ M. tuberculosis: 4.4 Mb, ~4,000 genes
  ─ M. genitalium: 0.58 Mb, ~470 genes (near minimal genome)

  NUCLEOID ORGANIZATION:
  ─ Bacterial DNA is ~1,000 μm when fully extended
  ─ Compacted into ~1–2 μm nucleoid body via:
    Topoisomerases (supercoiling), HU, H-NS, IHF (histone-like proteins)
  ─ No histones (eukaryote), but analogous compaction mechanisms

  TRANSCRIPTION + TRANSLATION COUPLING:
  ─ No nuclear envelope → ribosomes attach to mRNA while still
    being transcribed (cotranslational translation)
  ─ Gene → Protein in ~2–5 minutes at 37°C
  ─ This coupling enables rapid regulatory responses

  OPERON ARCHITECTURE:
  [Promoter]──[Operator]──[Gene1]──[Gene2]──[Gene3]──[Terminator]
  Single mRNA: Polycistronic → encodes multiple proteins
  Promoter: σ factor binding site (−10 and −35 consensus)
  Operator: Repressor binding site (overlaps promoter)
  Repressor bound: RNA pol blocked → operon off
  Inducer removes repressor: Operon on
```

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| Gram+ or Gram-? Thick vs. thin peptidoglycan | Gram+ thick; Gram- thin + outer membrane |
| What does LPS activate? | TLR4 → NF-κB → sepsis cascade |
| Fastest bacteria doubling time | E. coli: ~20 minutes |
| Slowest clinically relevant | Mycobacteria: ~20 hours |
| Fastest way to spread resistance genes | Conjugation (plasmid transfer) |
| How do bacteria acquire entirely new traits? | Pathogenicity islands via HGT |
| How does β-lactam work? | Blocks PBP (transpeptidase) → no peptidoglycan cross-linking |
| Why is TB hard to treat? | Waxy mycolic acid wall, slow growth, intracellular |
| Why do biofilm bacteria resist antibiotics? | Slow growth + matrix barrier + efflux pumps |
| Gene expression control in bacteria | Operons: repressor + promoter architecture |

---

## Common Confusion Points

**Gram stain results are about cell wall structure, not taxonomic relatedness**: Some Gram-positive organisms (Mycobacteria, Nocardia) don't take the Gram stain well and require the acid-fast stain instead. The Gram stain tells you about peptidoglycan thickness; it's a practical clinical tool, not a phylogenetic classification.

**Plasmid vs. chromosome**: Not all DNA in a bacterial cell is on the chromosome. Plasmids are additional DNA that may carry important traits (resistance, virulence). Some bacteria have no plasmids; some have 10+. Losing a plasmid (plasmid curing) removes the traits it encodes.

**Transformation in nature vs. lab**: "Transformation" in the lab (heat shock or electroporation of E. coli with plasmid) is a forced version of what naturally competent bacteria do — take up DNA from their environment. Griffith's 1928 experiment showed transformation before anyone knew DNA was the genetic material.

**Horizontal gene transfer challenges the "tree of life"**: The tree of life model assumes genes are inherited vertically (parent to offspring). HGT means genes can jump horizontally between species, even distantly related ones. This is why rRNA-based phylogeny (which genes are in the genome) doesn't always tell you how organisms are actually related for specific traits.
