# Microbiology — Landscape Overview

## The Big Picture

```
THE MICROBIAL WORLD
====================

  THREE DOMAINS OF LIFE:
  ┌──────────────────────────────────────────────────────────────────┐
  │                         LUCA                                     │
  │              (Last Universal Common Ancestor)                    │
  │                    /           \                                 │
  │            BACTERIA          ARCHAEA ─── EUKARYA                 │
  │                                                                  │
  │  BACTERIA             ARCHAEA              EUKARYA (microbes)    │
  │  Prokaryote           Prokaryote           Eukaryote             │
  │  No nucleus           No nucleus           Nucleus + organelles  │
  │  Peptidoglycan wall   No peptidoglycan     Fungi, protozoa, etc. │
  │  All environments     Extreme environments All environments      │
  │  ~30,000 sp. described ~500 sp. described  Vast diversity        │
  │  E. coli, Staph,      Methanobacterium,    Saccharomyces,        │
  │  Streptococcus        Thermus, Haloarcula  Plasmodium, Candida   │
  │                                                                  │
  │  VIRUSES: Not alive (no metabolism); obligate intracellular      │
  │           ~10⁷ virus genomes per mL of ocean water               │
  └──────────────────────────────────────────────────────────────────┘

  SCALE:
  ┌────────────────────────────────────────────────────────────────┐
  │  Virus:        20–300 nm      (smaller than wavelength of light)│
  │  Bacterium:    0.5–5 μm       (smallest visible in microscope) │
  │  Yeast cell:   5–10 μm        (eukaryote, ~cell size)          │
  │  Red blood cell: 6–8 μm       (comparison)                     │
  │  Amoeba:       200–500 μm     (single-cell eukaryote)          │
  │  Human cell:   ~10–20 μm      (comparison)                     │
  │                                                                  │
  │  Earth biomass distribution (by carbon):                       │
  │  Plants:    82%    Bacteria:  13%    Archaea: 1.3%             │
  │  Fungi:     2.2%   Protists:  0.7%   Animals: 0.47%            │
  │  Humans: ~0.01% — yet dominate the biosphere's metabolism     │
  └────────────────────────────────────────────────────────────────┘
```

---

## Microbes as Computational Agents

```
  THE CS FRAMING: BACTERIA AS SIMPLE COMPUTING AGENTS
  =====================================================

  This is not just an analogy — bacteria literally implement
  information processing in their regulatory circuits:

  OPERON = IF-THEN LOGIC:
  lac operon: IF (lactose present AND glucose absent) THEN transcribe
  trp operon: IF (tryptophan absent) THEN transcribe
  These are genetic boolean circuits, formally equivalent to
  digital logic gates operating on chemical concentrations.

  TWO-COMPONENT SIGNALING = SENSOR + ACTUATOR:
  Sensor kinase (membrane): Detects environmental signal
  Response regulator: Changes gene expression
  ~30+ two-component systems in E. coli → modular sensing network
  Formally: sensor → ADC → register (response reg.) → output

  QUORUM SENSING = DISTRIBUTED CONSENSUS:
  Bacteria secrete autoinducers (AI)
  Each cell monitors local [AI] concentration
  When [AI] > threshold → all cells switch behavior simultaneously
  Applications: Biofilm formation, virulence factor secretion
  Formally: distributed threshold consensus algorithm in a
            network of N identical agents (Valiant's work applies)

  GENE REGULATORY NETWORK = BOOLEAN CIRCUIT:
  Transcription factors (activators + repressors)
  Build AND/OR/NOT gates from promoter architecture
  Complex programs (sporulation, chemotaxis, SOS response)
  all encoded as regulatory circuits in DNA
```

---

## The Metagenomics Revolution

```
  METAGENOMICS: SEQUENCING MICROBIAL COMMUNITIES
  ================================================

  PRE-METAGENOMICS PROBLEM:
  >99% of environmental bacteria cannot be cultured in a lab.
  Classical microbiology (streak a plate, pick a colony) misses
  almost everything.

  METAGENOMICS SOLUTION:
  Extract DNA directly from environment (no culturing)
  Sequence all DNA at once → computational assembly
  Identify organisms from sequence alone

  TWO APPROACHES:
  ┌──────────────────────────────────────────────────────────────┐
  │ 16S rRNA AMPLICON SEQUENCING                                  │
  │   PCR amplify 16S rRNA gene (present in all bacteria)        │
  │   Sequence amplicons → compare to database                  │
  │   Identifies which bacteria are present (who's there?)       │
  │   Cheap: ~$10–30/sample                                      │
  │   Limitation: Semi-quantitative; primer bias; no function    │
  │                                                               │
  │ SHOTGUN METAGENOMICS                                         │
  │   Sequence ALL DNA in sample (not just 16S)                  │
  │   Reconstruct genomes: metagenome-assembled genomes (MAGs)  │
  │   Identifies: Who's there + What they can do (function)     │
  │   Expensive: ~$100–500/sample                                │
  │   Tools: Kraken2/Bracken (classification), MetaSPAdes (assembly)│
  │           MetaPhlAn4 (species profiling), HUMAnN3 (function) │
  └──────────────────────────────────────────────────────────────┘

  SCALE OF MICROBIAL DIVERSITY REVEALED:
  Before metagenomics: ~5,000 bacterial species described
  After: Candidate Phyla Radiation (CPR): >70 new bacterial phyla
         Most life on Earth was unknown before 2000s
  Tara Oceans: 40 million new ocean microbial genes (2015)
  Human gut: ~1,000 species in healthy adult microbiome
```

---

## Why Microbiology Matters at Scale

```
  GLOBAL IMPACT OF MICROORGANISMS
  ================================

  BIOGEOCHEMICAL CYCLES:
  ─ Nitrogen fixation: ONLY bacteria + archaea can fix N₂ → NH₃
    (All nitrogen in food web ultimately from microbial fixation)
  ─ Oxygen in atmosphere: Cyanobacteria generated it (GOE, ~2.4 Ga)
  ─ Carbon cycle: Decomposition (soil bacteria + fungi)
  ─ Sulfur cycle: Sulfate-reducing bacteria in anaerobic sediments
  ─ Without microbes: Most multicellular life impossible

  HUMAN MICROBIOME:
  ─ ~38 trillion bacterial cells in/on human body
  ─ Roughly 1:1 ratio with human cells
  ─ ~150x more microbial genes than human genes in gut
  ─ Connected to: immunity, metabolism, mental health, drug response

  ANTIMICROBIAL RESISTANCE (AMR):
  ─ 1.27 million deaths/year attributable to AMR (2019, Lancet)
  ─ Drug-resistant tuberculosis: ~500,000 new cases/year
  ─ MRSA, CRE, carbapenem-resistant Acinetobacter: urgent threats
  ─ New antibiotics: Very few approved since 1990

  INDUSTRIAL BIOTECHNOLOGY:
  ─ ~$400 billion/year: antibiotics, enzymes, biofuels, fermented foods
  ─ Insulin: Produced in E. coli since 1982 (first biotech drug)
  ─ Vaccines: Many grown in mammalian or yeast cells
  ─ Bioplastics, bioethanol, biodegradable materials: emerging
```

---

## File Roadmap

| File | What It Covers |
|------|----------------|
| 01-BACTERIAL-BIOLOGY.md | Structure, growth, metabolism, horizontal gene transfer |
| 02-VIRAL-BIOLOGY.md | Virion structure, replication cycle, Baltimore classification, evolution |
| 03-ARCHAEA-EUKARYOTIC-MICROBES.md | Extremophiles, protists, microscopic fungi, algae |
| 04-MICROBIOME.md | Human microbiome, gut-brain axis, metagenomics |
| 05-MICROBIAL-ECOLOGY.md | Biofilms, quorum sensing, soil/ocean microbiomes, element cycles |
| 06-PATHOGEN-MECHANISMS.md | Virulence factors, invasion, immune evasion, Koch's postulates |
| 07-ANTIMICROBIAL-RESISTANCE.md | Resistance mechanisms, HGT, resistome, One Health, pipeline crisis |
| 08-MICROBIAL-GENETICS.md | Operons, two-component systems, CRISPR-Cas (natural), mobile elements |
| 09-APPLIED-MICROBIOLOGY.md | Fermentation, bioremediation, synthetic biology, probiotics |

---

## Decision Cheat Sheet

| Question | Where to Look |
|----------|--------------|
| How do bacteria communicate? | Quorum sensing — 05 |
| How do bacteria resist antibiotics? | Resistance mechanisms — 07 |
| What are the human gut microbiome constituents? | Microbiome overview — 04 |
| How does a virus replicate? | Viral biology (lytic/lysogenic) — 02 |
| Where did CRISPR come from? | Bacterial immune memory — 08 |
| How is insulin made industrially? | Applied/synthetic biology — 09 |
| What are Archaea known for? | Extremophiles — 03 |
| How does pathogen X invade host cells? | Pathogen mechanisms — 06 |
| What is metagenomics? | Metagenomics approach — 04, 05 |
| How do plasmids spread resistance? | HGT mechanisms — 07 |

---

## Common Confusion Points

**Bacteria vs. Archaea vs. Viruses**: Bacteria and Archaea are both prokaryotes (no nucleus) but are as different from each other as either is from eukaryotes (different cell wall chemistry, transcription machinery, membrane lipids). Viruses are not cells at all — they're genetic information packages. All three are "microbes" colloquially.

**Prokaryote ≠ simple**: Bacteria have evolved for 3.8 billion years. They have complex regulatory networks, sophisticated sensing systems, social behaviors (biofilms), immune memory (CRISPR), and metabolic capabilities no eukaryote possesses (nitrogen fixation, anaerobic respiration on metals). "Prokaryote = simple" is wrong.

**Most bacteria are not pathogens**: Only a small fraction of bacterial species cause disease. The majority are environmental decomposers, symbionts, or commensals. The human gut microbiome is mostly beneficial. Bacteria that cause disease usually have acquired specific virulence factors.

**Viruses are not alive (definitionally)**: Viruses don't have metabolism — they don't process energy, regulate their internal environment, or grow. They are information (DNA or RNA) inside a protein coat that hijacks cell machinery. Whether they count as "alive" is a definitional question; most biologists say no, but the boundary is philosophically interesting.
