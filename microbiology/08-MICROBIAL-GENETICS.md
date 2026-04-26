# Microbial Genetics

## The Big Picture

```
MICROBIAL GENETICS: REGULATION AS COMPUTATION
===============================================

  Bacteria implement information processing in their regulatory circuits.
  This is not an analogy — it is formally equivalent to digital logic.

  ┌─────────────────────────────────────────────────────────────────┐
  │  REGULATORY ARCHITECTURE OVERVIEW                               │
  │                                                                 │
  │  GENE REGULATION LEVELS:                                        │
  │  1. Transcription:  Promoter, sigma factors, activators,        │
  │                     repressors, enhancers (rare in bacteria)    │
  │  2. Post-transcription: sRNA, RNA-binding proteins, riboswitches│
  │  3. Translation:   Ribosome binding site, start codon context   │
  │  4. Post-translation: Proteolysis, modification, localization   │
  │                                                                 │
  │  COMPUTATIONAL FRAMING:                                         │
  │  Operon          = IF-THEN logic gate                           │
  │  Regulon         = Module (multiple operons, one regulator)     │
  │  Signal cascade  = Pipeline with amplification                  │
  │  Two-component   = Sensor + ADC + register + actuator           │
  │  Sigma factor    = Runtime-loadable OS module                   │
  │  CRISPR-Cas      = Immune memory database + pattern matching    │
  └─────────────────────────────────────────────────────────────────┘
```

---

## Operons and Gene Expression Logic

```
  OPERON ARCHITECTURE
  ====================

  DEFINITION: Operon = co-transcribed gene cluster under single promoter
  Purpose: Coordinate expression of functionally related genes

  THE lac OPERON (E. coli model system):
  ┌────────────────────────────────────────────────────────────────┐
  │  Gene: lacI  lacP  lacO   lacZ    lacY     lacA                │
  │  Role: Rep   Prom  Oper   β-gal   permease transacetylase      │
  │                                                                │
  │  FULL LOGIC (two-input AND gate):                              │
  │  ACTIVE when: (lactose present) AND (glucose absent)           │
  │  → Avoids wasting energy if glucose (preferred) is available   │
  │                                                                │
  │  Signal 1: Lactose present                                     │
  │  Allolactose (lactose metabolite) → binds LacI repressor       │
  │  → Conformational change → LacI releases operator              │
  │  → RNA pol can transcribe operon                               │
  │                                                                │
  │  Signal 2: Glucose absent (catabolite repression)              │
  │  Low glucose → high cAMP (adenylate cyclase active)            │
  │  cAMP binds CAP (CRP): Activator protein                       │
  │  cAMP-CAP complex binds CAP site upstream of promoter          │
  │  → Increases RNA pol binding affinity                          │
  │  → Enhances transcription                                      │
  │                                                                │
  │  RESULT: Full expression only when BOTH conditions met         │
  │  Partial expression: lactose present + glucose present (low)   │
  │  No expression: lactose absent (repressor blocks)              │
  │  OR: glucose present (cAMP low; no CAP activation)             │
  └────────────────────────────────────────────────────────────────┘

  THE trp OPERON (feedback repression):
  ┌────────────────────────────────────────────────────────────────┐
  │  OPPOSITE LOGIC: Active when Trp absent; silent when Trp present│
  │                                                                │
  │  TrpR (apo-repressor) alone: Inactive → operon ON              │
  │  TrpR + tryptophan (corepressor): Active repressor             │
  │  → Binds trpO operator → operon OFF                            │
  │                                                                │
  │  ATTENTUATION (second control layer):                          │
  │  Leader peptide region: Contains Trp codons                    │
  │  If ribosome stalls (Trp scarce): forms anti-terminator stem   │
  │  → RNA pol reads through → transcription continues             │
  │  If ribosome runs through (Trp plentiful): forms terminator    │
  │  → RNA pol falls off before structural genes                   │
  │  → Coupling between Trp supply and ribosome translation speed  │
  │  → Elegant analog control: more Trp → more attenuation         │
  └────────────────────────────────────────────────────────────────┘

  SIGMA FACTORS: RUNTIME MODULE LOADING
  ┌────────────────────────────────────────────────────────────────┐
  │ Sigma (σ) factor: Dissociable subunit of RNA polymerase core   │
  │ Core RNAP (α₂ββ'ω): Catalytic; binds σ to form holoenzyme      │
  │ σ factor recognizes promoter −10 and −35 elements              │
  │                                                                │
  │ E. COLI SIGMA FACTORS:                                         │
  │ σ⁷⁰ (RpoD):   Housekeeping; vegetative growth; most genes      │
  │ σ³²  (RpoH):  Heat shock; activated 42°C; DnaK, GroEL induction│
  │ σ²⁴ (RpoE):   Extreme heat + envelope stress                   │
  │ σ³⁸ (RpoS):   Stationary phase + stress; "general stress σ"    │
  │ σ²⁸ (FliA):   Flagellar genes (motility program)               │
  │ σ⁵⁴ (RpoN):   Nitrogen limitation; requires activator ATP      │
  │                                                                │
  │ Anti-sigma factors: Inhibit σ until signal releases them       │
  │ FlgM: Anti-σ²⁸; keeps flagellar program off until hook built   │
  │ RseA: Anti-σ²⁴; degraded by DegS protease on envelope stress   │
  │                                                                │
  │ SPORULATION (B. subtilis): σ cascade orchestrates development  │
  │ σᴴ → initiates sporulation → σᶠ (forespore) + σᴱ (mother cell)│
  │ → σᴳ + σᴷ: Late sporulation programs                           │
  │ Each σ activates next tier + previous tier genes turned off    │
  └────────────────────────────────────────────────────────────────┘
```

---

## Regulons and Global Regulation

```
  REGULONS: MODULES FOR COORDINATED RESPONSES
  =============================================

  Regulon = Set of operons all regulated by same regulator
  (across multiple chromosomal locations; not co-localized like operon)

  KEY REGULONS:
  ┌────────────────────────────────────────────────────────────────┐
  │ SOS RESPONSE (LexA regulon):                                   │
  │   Trigger: DNA damage → stalled replication → ssDNA exposed    │
  │   RecA binds ssDNA → becomes coprotease                        │
  │   RecA* cleaves LexA repressor → LexA auto-degrades            │
  │   → >40 SOS genes derepressed simultaneously                   │
  │   Genes: RecA, UvrABC (nucleotide excision repair),            │
  │           UmuDC (error-prone pol V → translesion synthesis),   │
  │           sulA (filamentation inhibitor → cell division arrest)│
  │   LexA resynthesis → eventual repression (quenching)           │
  │                                                                │
  │ HEAT SHOCK REGULON (σ³²):                                      │
  │   Trigger: Temperature rise → misfolded proteins               │
  │   DnaK/DnaJ chaperones sequester σ³² normally                  │
  │   Misfolded proteins titrate DnaK → free σ³² → transcription   │
  │   Genes: GroEL/GroES, DnaK, DnaJ, ClpB, HtpG (chaperones)      │
  │           Lon, ClpXP, FtsH proteases (degrade misfolded prot)  │
  │                                                                │
  │ PhoP/PhoQ (VIRULENCE REGULON in Salmonella):                   │
  │   Two-component system (see next section)                      │
  │   Induces: Low Mg²⁺, antimicrobial peptide exposure            │
  │   → Activates >100 genes; LPS modification, Mg²⁺ uptake        │
  │   → Critical for intramacrophage survival                      │
  │                                                                │
  │ FNR REGULON (anaerobic response):                              │
  │   FNR: O₂-sensing transcription factor                         │
  │   Active under anaerobiosis (4Fe-4S cluster lost in O₂)        │
  │   → Activates: anaerobic respiratory genes (nitrate, fumarate)│
  │   → Represses: aerobic respiratory genes                       │
  └────────────────────────────────────────────────────────────────┘
```

---

## Two-Component Signal Transduction

```
  TWO-COMPONENT SYSTEMS (TCS)
  ============================

  Most common bacterial signal transduction paradigm
  E. coli: 36 TCS pairs; Streptomyces: >80 pairs

  CANONICAL ARCHITECTURE:
  ┌────────────────────────────────────────────────────────────────┐
  │                                                                │
  │  SENSOR HISTIDINE KINASE (HK):                                 │
  │  ┌────────────────────────────────────────────────────────┐    │
  │  │ SENSOR DOMAIN (periplasmic/membrane)                   │   │
  │  │ Detects: pH, osmolarity, nutrients, peptides, etc.     │   │
  │  │                ↓ Signal detected                        │   │
  │  │ DHPT domain: Phosphorylatable His (ATP donor)          │   │
  │  │ Autophosphorylation: HK-His-PO₄                        │   │
  │  └────────────────────────────────────────────────────────┘   │
  │                    ↓ Phosphoryl transfer                       │
  │  RESPONSE REGULATOR (RR):                                      │
  │  ┌────────────────────────────────────────────────────────┐   │
  │  │ RECEIVER DOMAIN: Asp phosphorylation site              │   │
  │  │ Phosphorylated Asp → conformational change             │   │
  │  │ → Activates or inhibits OUTPUT DOMAIN                  │   │
  │  │ OUTPUT: DNA-binding domain OR enzyme activity          │   │
  │  └────────────────────────────────────────────────────────┘   │
  │                                                                 │
  │  SIGNAL: Sensor   →   HK-His-P   →   RR-Asp-P   →  Gene expr. │
  │                                                                 │
  └────────────────────────────────────────────────────────────────┘

  KEY TCS EXAMPLES:
  ┌────────────────────────────────────────────────────────────────┐
  │ SYSTEM     HK     RR      SIGNAL           OUTPUT              │
  │ EnvZ/OmpR  EnvZ   OmpR    Osmolarity       OmpF/OmpC (porins)  │
  │ PhoP/PhoQ  PhoQ   PhoP    Low Mg²⁺, AMPs   Virulence genes     │
  │ PhoR/PhoB  PhoR   PhoB    Phosphate limit  Pho regulon         │
  │ VncS/VncR  VncS   VncR    Vancomycin       Resistance genes    │
  │ NtrB/NtrC  NRII   NtrC    Nitrogen limit   σ⁵⁴-activated genes│
  │ KinA/Spo0A KinA   Spo0A   Starvation/crowd Sporulation in Bacillus│
  └────────────────────────────────────────────────────────────────┘

  COMPLEXITY: PHOSPHORELAYS
  ─ Some systems: HK → phosphotransfer protein → RR (3-component)
  ─ Spo0 sporulation: 4-component phosphorelay
  ─ Acts as signal integration AND delay (temporal filtering)
  ─ Input/output logic: Same HK can phosphorylate multiple RRs (crosstalk)
    Insulated by: Kinetic discrimination, physical interaction domains

  CROSSTALK PREVENTION:
  ─ Tight co-evolution of HK + RR (co-specificity)
  ─ Specificity residues: "Interaction surfaces" that match only cognate pair
  ─ Structural studies: 12 specificity-determining residue positions on RR
    decoder domain that match 2 specificity positions on HK
  ─ Rewiring experiments (Laub lab): Swap specificity residues → redirect signal
```

---

## Small RNAs (sRNAs) and Post-Transcriptional Regulation

```
  SMALL REGULATORY RNAs
  ======================

  Bacteria have hundreds of sRNAs (50–500 nt; non-coding)
  Function: Post-transcriptional regulation (after transcription, before/during translation)

  MECHANISM:
  ┌────────────────────────────────────────────────────────────────┐
  │ Trans-acting sRNA:                                             │
  │   Base-pairs with target mRNA at RBS (ribosome binding site)   │
  │   → Blocks ribosome access → TRANSLATIONAL REPRESSION          │
  │   OR: Opens secondary structure → ACTIVATES translation        │
  │   Often requires Hfq: RNA chaperone; facilitates sRNA-mRNA     │
  │   pairing; protects sRNA from degradation                      │
  │                                                                │
  │ Hfq-mediated regulation:                                       │
  │   Hfq: Sm-like protein; hexameric ring                         │
  │   Binds AU-rich sequences (Distal face) + sRNA (Proximal face) │
  │   → Increases effective local concentration → faster pairing   │
  │   → Also recruits RNase E → coupled mRNA degradation           │
  └────────────────────────────────────────────────────────────────┘

  KEY sRNA EXAMPLES:
  ─ RyhB (E. coli): Activated under iron limitation
    → Represses iron-using proteins (non-essential ones)
    → Spares iron for essential functions (respiration, DNA repair)
    Regulon: >20 mRNA targets; coordinates entire iron economy
  ─ MicF: Represses OmpF (outer membrane porin) translation
    → Reduces outer membrane permeability in stress
  ─ GcvB: Represses amino acid transport systems (overflow prevention)
  ─ RprA, DsrA, ArcZ: Multiple sRNAs activate RpoS (σ³⁸) translation
    → Redundant inputs integrate multiple stress signals into one output

  RIBOSWITCHES (cis-regulatory RNA elements):
  ┌────────────────────────────────────────────────────────────────┐
  │ Definition: 5' UTR of mRNA that folds around metabolite        │
  │ → Ligand binding changes RNA structure → regulates expression  │
  │ No protein regulator needed — direct metabolite sensing        │
  │                                                                │
  │ EXAMPLES:                                                      │
  │ TPP riboswitch: Thiamine-PP binding → terminator hairpin       │
  │   → Terminates transcription (negative feedback)               │
  │ SAM riboswitch: S-adenosylmethionine → represses expression    │
  │ Cobalamin (B12) riboswitch: Sequesters RBS; ~200 nt aptamer    │
  │ Lysine riboswitch: Lysine → premature termination              │
  │ Fluoride riboswitch: F⁻ detection → induces F⁻ exporter        │
  │                                                                │
  │ BIOTECHNOLOGY: Riboswitches as biosensors + genetic switches   │
  │ Synthetic biology: Engineer riboswitches to respond to         │
  │ non-natural ligands → programmable genetic control             │
  └────────────────────────────────────────────────────────────────┘
```

---

## CRISPR-Cas: Bacterial Immune Memory

```
  CRISPR-CAS IN BACTERIA — THE NATURAL SYSTEM
  =============================================

  Note: This is the BACTERIAL immune system origin story.
  For Cas9 editing technology, see genomics/07-CRISPR.md.

  FUNCTION: Adaptive immunity against phage and plasmids
  Found in: ~50% of bacteria and ~90% of archaea

  MECHANISM — THREE STAGES:
  ┌────────────────────────────────────────────────────────────────┐
  │                                                                │
  │  STAGE 1: ADAPTATION (memory acquisition)                      │
  │  ─────────────────────────────────────────                     │
  │  Phage infects cell → some cells survive                       │
  │  Cas1-Cas2 complex: Captures short DNA from invader (~30 bp)   │
  │  → Inserts as new SPACER at leader end of CRISPR array         │
  │  CRISPR array: [Leader][Repeat-Spacer][Repeat-Spacer]...       │
  │  Leader proximal = most recent memory; leader distal = oldest  │
  │  Each spacer = record of past infection                        │
  │  PAM recognition: Cas1 recognizes PAM adjacent to protospacer  │
  │  → Prevents self-targeting (host genome lacks PAM context)     │
  │                                                                │
  │  STAGE 2: BIOGENESIS (crRNA production)                        │
  │  ─────────────────────────────────────                         │
  │  CRISPR array transcribed as long pre-crRNA                    │
  │  Processing: RNase III (Type II) or Cas6 (Types I/III)         │
  │  → Mature crRNA: One spacer + partial repeats                  │
  │  crRNA guides Cas effector to target                           │
  │                                                                │
  │  STAGE 3: INTERFERENCE (target destruction)                    │
  │  ─────────────────────────────────────────                     │
  │  crRNA + Cas effector complex scans for complementary sequence │
  │  PAM verification (safety check vs. self)                      │
  │  Target DNA/RNA bound → cleaved                                │
  │  Phage genome destroyed → cell survives → immunity hereditary  │
  │                                                                │
  └────────────────────────────────────────────────────────────────┘

  CRISPR TYPES:
  ┌────────────────────────────────────────────────────────────────┐
  │ Type I:   Multi-subunit Cascade complex; Cas3 helicase/nuclease│
  │           Most common (~60% of CRISPR systems)                 │
  │ Type II:  Single Cas9 effector; requires tracrRNA + crRNA      │
  │           → sgRNA engineering → the genome editing workhorse   │
  │ Type III: RNA-targeting + ssDNA targeting; Csm/Cmr complexes   │
  │ Type V:   Cas12a/Cas12b: PAM on 5' end; staggered cuts         │
  │ Type VI:  Cas13: RNA-only targeting; collateral RNA cleavage   │
  │           → SHERLOCK diagnostic platform (see genomics/)       │
  └────────────────────────────────────────────────────────────────┘

  ANTI-CRISPR PROTEINS:
  ─ Phage counter-evolution: Phages encode anti-CRISPR (Acr) proteins
  ─ AcrII (Type II CRISPR inhibitors): Acr-IIA4 mimics DNA → blocks Cas9
  ─ AcrIIC1-3: Multiple inhibition mechanisms
  ─ Biotechnology: Anti-CRISPR proteins used to control editing (on/off switch)
  ─ Arms race: CRISPR → phage escape (PAM mutation) → new CRISPR spacer acquired
```

---

## Mobile Genetic Elements

```
  MOBILE GENETIC ELEMENTS (MGEs)
  ================================

  INSERTION SEQUENCES (IS):
  ─ Simplest transposable elements: Only transposase + terminal IRs
  ─ ~1–2 kb; found in virtually all bacterial genomes
  ─ When IS flanks a gene → composite transposon formed
  ─ Tn10: Two IS10 elements flanking tetracycline resistance
  ─ Tn3: Carries bla (β-lactamase); TnpA (transposase) + TnpR (resolvase)
  ─ Mechanism: Replicative (copy-and-paste) vs. Conservative (cut-and-paste)

  INTEGRONS:
  ─ Not transposons — can't move by themselves
  ─ Have site-specific recombination system (IntI integrase + attI site)
  ─ Capture gene cassettes: Each cassette has attC site; integrase recombines
    attI × attC → cassette integrates at leader position
  ─ Class 1 integrons: Tn402-derived; most clinically important
  ─ Capture drug resistance cassettes + other adaptive functions
  ─ Can accumulate 5–8 cassettes → encode resistance to many drug classes

  CONJUGATIVE TRANSPOSONS (ICE — Integrative Conjugative Elements):
  ─ Both transpose AND conjugate: Can transfer chromosome-to-chromosome
  ─ Tn916 (Enterococcus): First characterized; carries tetM
  ─ SXT (V. cholerae): Large ICE; carries multiple resistance genes
  ─ Unlike plasmids: Replicate only as part of chromosome
    → Cannot be "cured" by plasmid elimination strategies

  GENOMIC ISLANDS:
  ─ Large regions (10–200 kb) of foreign origin
  ─ Include pathogenicity islands (covered in 06-PATHOGEN-MECHANISMS.md)
  ─ Metabolic islands: Novel metabolic capabilities (degradation pathways)
  ─ Resistance islands: Clusters of resistance genes (AbaR1 in Acinetobacter)
  ─ Flanked by: Direct repeats, tRNA genes, IS elements
  ─ Identification: GC% deviation, codon usage deviation from host
```

---

## Experimental Evolution

```
  EXPERIMENTAL EVOLUTION: WATCHING DARWIN IN REAL TIME
  ======================================================

  Bacteria evolve fast enough to observe evolution in laboratory experiments.
  E. coli: 1 generation/20 min → ~26,000 generations/year

  LENSKI LONG-TERM EVOLUTION EXPERIMENT (LTEE):
  ┌────────────────────────────────────────────────────────────────┐
  │ Started: 1988 (Richard Lenski, Michigan State)                 │
  │ Organism: E. coli B (REL606)                                   │
  │ Conditions: 12 replicate populations; minimal glucose medium   │
  │ Duration: >75,000 generations (as of 2024 — ongoing!)          │
  │                                                                │
  │ KEY FINDINGS:                                                  │
  │ 1. Fitness increases rapidly then decelerates (hyperbolic)     │
  │    →30% fitness gain over 50,000 gen; still slowly increasing  │
  │                                                                │
  │ 2. CITRATE UTILIZATION (Cit+) phenotype:                       │
  │    E. coli normally cannot use citrate in aerobic conditions   │
  │    At ~31,500 generations: ONE population evolved Cit+         │
  │    Mechanism: Tandem gene duplication of rnk-citT region       │
  │    → citT (citrate transporter) under aerobic promoter         │
  │    → "Evolutionary leap" requires multiple mutations (rare)    │
  │    Demonstrates: Epistasis, historical contingency             │
  │                                                                │
  │ 3. Hypermutator clones: 6/12 populations evolved mutator       │
  │    phenotype (mutL, mutS inactivation — mismatch repair loss)  │
  │    → Higher mutation rate → faster adaptation initially        │
  │    → Then fitness cost as deleterious mutations accumulate     │
  │                                                                │
  │ 4. Parallel evolution: Same genes mutated in multiple lineages │
  │    (topA, nadR, spoT — convergent adaptation to condition)     │
  └────────────────────────────────────────────────────────────────┘

  DIRECTED EVOLUTION:
  ─ Artificial selection for desired properties in lab
  ─ Frances Arnold Nobel Prize 2018: Directed enzyme evolution
  ─ Protocol: Mutate gene → express → screen/select for desired function
    → Take best variant → mutagenize again → repeat
  ─ Thermostable enzymes, novel substrate specificities, altered stereospecificity
  ─ Industrial applications: All major industrial enzymes improved by directed evolution

  ANTIBIOTIC RESISTANCE EVOLUTION:
  ─ In vitro evolution: Serial passage in increasing antibiotic concentrations
  ─ Can evolve high-level resistance in ~10–20 passages (~days to weeks)
  ─ Trajectory: Specific SNPs in target gene → efflux pump activation →
    additional target mutations → compensatory mutations restore fitness
  ─ Fitness cost: Initial resistance mutations often reduce growth
    Compensatory mutations: Restore growth WITHOUT losing resistance
    → Resistant strains become as fit as susceptible progenitors
```

---

## Decision Cheat Sheet

| Concept | Key Detail |
|---------|-----------|
| lac operon logic | Two-input AND: lactose present AND glucose absent |
| trp operon control | Feedback repression + attenuation (ribosome stalling) |
| sigma factor function | Swappable RNAP subunit; determines promoter −10/−35 recognition |
| σ³² function | Heat shock response; released by DnaK titration |
| Two-component system | HK autophosphorylates His → transfers to RR Asp → gene expression |
| SOS response trigger | ssDNA → RecA coprotease → LexA cleavage → >40 genes |
| sRNA regulatory mechanism | Base-pair with mRNA at RBS; requires Hfq chaperone |
| Riboswitch mechanism | 5' UTR directly binds metabolite; no protein required |
| CRISPR adaptation | Cas1-Cas2 integrates new spacers from phage DNA |
| Anti-CRISPR | Phage-encoded inhibitors; Acr-IIA4 mimics DNA; blocks Cas9 |
| Class 1 integron function | Captures gene cassettes via attI × attC recombination |
| LTEE key finding | Citrate+ evolution at ~31,500 gen; historical contingency |

---

## Common Confusion Points

**Operon vs. regulon**: An operon is a single promoter → polycistronic mRNA unit. A regulon is multiple operons (anywhere in the genome) all controlled by the same regulator. The PhoP/PhoQ regulon includes many scattered operons, all bearing PhoP binding sites, all regulated simultaneously when PhoP is phosphorylated.

**CRISPR natural function vs. editing tool**: CRISPR-Cas in bacteria is an adaptive immune system against phage. It has nothing to do with genome editing until Jennifer Doudna and Emmanuelle Charpentier (Nobel 2020) recognized that Cas9 could be reprogrammed with a synthetic guide RNA to cut any DNA sequence. The bacteria discovered this ~3 billion years ago; we discovered how to exploit it in 2012.

**Sigma factor anti-sigma: why the complexity?**: Anti-sigma factors allow rapid, reversible post-translational regulation of σ activity. This is faster than transcriptional control (no need to synthesize/degrade σ; just release it from anti-sigma). This is analogous to post-translational activation of transcription factors in eukaryotes (e.g., NF-κB held by IκB).

**Two-component phosphorylation is not just ON/OFF**: TCS response regulators can be phosphorylated to varying degrees, creating graded responses. Additionally, some RRs are bifunctional: same HK acts as phosphatase of RR when signal is absent. This prevents "leaky" phosphorylation by small molecules (acetyl phosphate etc.) from constitutively activating the system — important for signal fidelity.
