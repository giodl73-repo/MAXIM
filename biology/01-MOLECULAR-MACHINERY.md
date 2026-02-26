# Molecular Machinery — DNA, RNA, Proteins, Central Dogma

---

## Big Picture

```
INFORMATION FLOW:

  DNA (storage)
   │
   │ TRANSCRIPTION (RNA polymerase reads DNA → makes mRNA)
   ▼
  mRNA (message)
   │
   │ TRANSLATION (ribosome reads mRNA → makes protein)
   ▼
  Protein (function)

  KEY: DNA is the blueprint. RNA is the working copy.
       Proteins are the machines that do everything.

SCALE:
  DNA → 2 nm diameter, ~3.2 Gbp, 2 m long (packed into 10 μm nucleus)
  mRNA → 1.5-12 kb typical, lifetime hours-days
  Protein → 50-5000 aa, 2-50 nm diameter, folds in ms-s, lifetime hours-weeks
```

---

## Engineering Bridges

```
MOLECULAR MACHINERY ←→ SYSTEMS ENGINEERING

DNA replication = distributed copy-on-write with checksums
  Semi-conservative: like copy-on-write — one old strand retained as reference
  DNA Pol III: proofreading 3'→5' exonuclease = inline error correction
  Mismatch repair (MMR): post-copy audit pass
  Final error rate ~10⁻⁹/bp ≈ single-bit error in a 1 GB file

Gene regulation = multi-layer access control + caching
  Chromatin state: coarse-grained (open/closed) = filesystem permissions
  Histone marks: fine-grained combinatorial code = role-based ACL
  Transcription factors: combinatorial logic gates (AND/OR/NOT) on promoter
  mRNA half-life: TTL on cached computation product

Protein folding = constrained optimization on a high-dimensional energy landscape
  Levinthal's paradox: brute force is 10^34 years; biology solves in milliseconds
  Solution: guided funnel, not exhaustive search (like branch-and-bound, not brute force)
  Chaperones: constraint-relaxation scaffolding during optimization
  AlphaFold2: transformer + equivariant geometry → competitive with 50 years of crystallography

CRISPR-Cas9 = regular expression search-and-cut on DNA
  sgRNA (20 nt): the pattern — must match exactly + require PAM motif ("NGG")
  Cas9: the engine — scans ~3 billion base pairs for the pattern
  HNH + RuvC nucleases: the cutter — blunt DSB at match
  Base editors (David Liu): search-and-replace without making the cut
  Prime editing: piggyback the replacement sequence on the guide RNA itself

Ribosome = programmable molecular machine with kinetic proofreading
  Error rate ~10⁻⁴ per codon — two GTP hydrolysis checkpoints (reject wrong tRNA)
  Kinetic proofreading (Hopfield 1974): use irreversible energy expenditure to
  discriminate between substrates beyond equilibrium limits
  → Same mechanism used in immune T cell receptor discrimination
```

## DNA Structure

### Double Helix (Watson-Crick 1953)

```
TWO ANTIPARALLEL STRANDS:
  5' ── A-T-G-C-C-G ── 3'   (5' to 3' = direction of synthesis)
  3' ── T-A-C-G-G-C ── 5'   (complementary, antiparallel)

BASE PAIRING:
  A = Adenine (purine) — pairs with T (2 hydrogen bonds)
  T = Thymine (pyrimidine) — pairs with A
  G = Guanine (purine) — pairs with C (3 hydrogen bonds)
  C = Cytosine (pyrimidine) — pairs with G

  Purines: double-ring (A, G)
  Pyrimidines: single-ring (T, C, U)
  A·T: 2 H-bonds (weaker); G·C: 3 H-bonds (stronger → GC-rich regions more stable)

HELIX PARAMETERS (B-form, physiological):
  Pitch: 3.4 nm per turn
  Base pairs per turn: 10.5
  Rise per bp: 0.34 nm
  Diameter: 2 nm
  Major groove: wide (12 Å), accessible to proteins
  Minor groove: narrow (6 Å), AT-rich sequences have spine of hydration
```

### DNA Organization in the Nucleus

```
CHROMATIN HIERARCHY:
  DNA (2 nm)
  → Nucleosome (11 nm): DNA wraps 1.7× around histone octamer (H2A, H2B, H3, H4)×2
    146 bp of DNA per nucleosome; ~10 bp linker DNA between
  → "Beads on a string" (11 nm fiber) [open chromatin]
  → 30 nm fiber (solenoid): nucleosomes fold into helical array
  → Loops (~300 nm): chromatin loops anchored by cohesin+CTCF
  → TADs (topologically associating domains): ~100 kb - 1 Mb regions of self-interaction
  → Chromosome territories (~μm scale)

DNA PACKING RATIO: 2 m DNA → 10 μm nucleus → packing ~200,000×

HISTONES: H2A, H2B, H3, H4 — highly conserved across evolution
  Histone tails (N-terminal): modified post-translationally
  H3K27me3: repressive mark (Polycomb)
  H3K4me3: active promoter mark
  H3K9ac: active transcription mark
  H3K9me3: heterochromatin/silencing
  → Histone code: combinatorial modifications = epigenetic memory
```

---

## DNA Replication

```
SEMI-CONSERVATIVE: each daughter cell gets one original strand + one new strand

STEPS:
  1. Helicase: unwinds double helix at origin of replication
     Creates replication fork (two singlestranded templates)
  2. SSB (single-strand binding protein): stabilizes single strands
  3. Primase: synthesizes short RNA primer (~10 nt)
     → DNA polymerase cannot initiate; needs free 3' OH
  4. DNA Polymerase III (main replicative pol): extends from 3' OH
     → reads 3'→5', synthesizes 5'→3'
     → proofreading: 3'→5' exonuclease corrects mismatches
     Error rate: ~10⁻⁷ per bp; with mismatch repair: ~10⁻⁹ per bp

LEADING vs LAGGING STRAND:
  Leading: synthesis continuous (same direction as fork movement)
  Lagging: synthesis discontinuous → Okazaki fragments (~200 nt each)
  Okazaki fragments: RNA primer + DNA → RNA removed by RNase H → gaps filled by Pol I → ligase joins

TELOMERES: repetitive sequences (TTAGGG in humans) at chromosome ends
  Problem: lagging strand cannot fully replicate end → shortening
  Solution: Telomerase (reverse transcriptase with RNA template) extends telomeres
  Cancer cells often reactivate telomerase → immortality
  Aging: telomere shortening → cellular senescence → Hayflick limit (~50 divisions)
```

---

## Transcription

```
PROMOTER: DNA sequence recognized by RNA polymerase (RNAP) + general transcription factors
  TATA box: 30 bp upstream of start site (TATAAA) — core promoter element
  GC box, CAAT box: enhance transcription initiation frequency
  Enhancers: can be 10s of kb away → loop to promoter via cohesin/mediator

RNA POLYMERASE II (mRNA synthesis in eukaryotes):
  Large complex with CTD (C-terminal domain)
  CTD phosphorylation: Ser5-P at initiation; Ser2-P at elongation
  Elongation rate: ~40-80 nt/sec
  Total mRNA: ~300,000 mRNA molecules per mammalian cell
  Transcription factories: RNAP II clusters at active enhancers/promoters

5' CAPPING: 7-methylguanosine cap added co-transcriptionally
  → Protects from 5' exonuclease degradation
  → Required for ribosome recognition (translation initiation)

3' POLYADENYLATION:
  Cleavage at poly(A) signal (AAUAAA, ~200 nt from end)
  Poly(A) polymerase adds ~200 A residues
  → Protects from 3' degradation; helps export from nucleus; enhances translation

mRNA SPLICING (eukaryotes):
  Pre-mRNA contains INTRONS (intervening sequences, non-coding)
  Intron-exon junctions: 5' GU...AG 3' (nearly universal)
  SPLICEOSOME: large ribonucleoprotein complex (snRNA U1,U2,U4,U5,U6)
  Reaction: two-step transesterification → excised intron lariat → joined exons
  Alternative splicing: ~95% of human genes alternatively spliced
    → One gene → multiple mRNA/protein isoforms
    → Increases proteome diversity without increasing gene number
```

---

## Translation

```
GENETIC CODE:
  3-nucleotide CODONS specify amino acids
  4³ = 64 possible codons for 20 amino acids + 3 stop codons
  Degenerate/redundant: multiple codons per amino acid (synonymous codons)
  Start codon: AUG (Met) — initiates all proteins
  Stop codons: UAA, UAG, UGA

THE CODE IS NEARLY UNIVERSAL:
  Same in bacteria, archaea, eukaryotes, mitochondria (with minor variations)
  Evidence: common ancestor; horizontal gene transfer would scramble if code varied
  Not arbitrary: optimized to minimize error impact (similar AAs = similar codons)

RIBOSOME:
  ~25 nm particle, ~4.3 MDa
  Two subunits: small (40S in eukaryotes, decodes mRNA) + large (60S, catalyzes peptide bond)
  Together: 80S (eukaryotes), 70S (bacteria, mitochondria)
  Active sites:
    A site (aminoacyl): accepts incoming aminoacyl-tRNA
    P site (peptidyl): holds growing peptide chain
    E site (exit): releases deacylated tRNA

ELONGATION CYCLE:
  1. tRNA selection: aminoacyl-tRNA·EF-Tu·GTP → A site
     GTP hydrolysis: energy for accuracy (kinetic proofreading)
  2. Peptide bond formation: peptidyl transferase (23S/28S rRNA = RIBOZYME!)
     Transfers growing chain from P-site tRNA to A-site amino acid
  3. Translocation: ribosome moves 3 nt (A→P→E), requires EF-G·GTP

  Speed: ~20 aa/sec → 400 aa protein = 20 sec
  Accuracy: ~10⁻⁴ errors per codon (kinetic proofreading: 2 GTP hydrolysis checkpoints)

tRNA: ~80 nt, cloverleaf secondary structure, L-shaped tertiary
  Anticodon: 3 nt that base-pair with mRNA codon
  3' CCA: amino acid attached here
  Wobble: base 3 of codon can pair with multiple tRNA anticodon bases
  → 61 sense codons, but only ~45 tRNA species in humans
```

---

## Protein Structure

### Four Levels

```
PRIMARY: amino acid sequence (linear chain)
  20 amino acids, encoded by genetic code
  Connected by peptide bonds (-CO-NH-)
  Sequence determines structure determines function

SECONDARY: local regular structures
  α-HELIX:
    3.6 residues per turn, pitch = 0.54 nm
    H-bond: i → i+4 (backbone C=O to backbone N-H)
    Right-handed; hydrophobic residues on one face → membrane anchors

  β-SHEET (parallel or antiparallel):
    Extended strands H-bonded between adjacent chains
    Antiparallel: more stable (H-bonds perpendicular to strand)
    β-barrels: formed by β-sheets → membrane protein pores (porin)

  LOOPS (turns): connect helices and sheets
    No regular structure; often at protein surface; often functional sites
    Ramachandran plot: φ, ψ backbone dihedral angles cluster in allowed regions

TERTIARY: overall 3D fold of single chain
  Hydrophobic core (nonpolar residues buried)
  Disulfide bonds (Cys-Cys): stabilize extracellular proteins
  Metal ions: Zn²⁺ fingers (DNA binding), Fe-S clusters (electron transport)
  Domains: independently folding units (50-200 aa) with distinct function

QUATERNARY: assembly of multiple polypeptide chains
  Homodimer (2 identical) → collagen (trimer) → hemoglobin (α₂β₂ tetramer)
  Subunit cooperativity (hemoglobin): binding O₂ to one subunit increases affinity in others
```

### Protein Folding

```
LEVINTHAL'S PARADOX:
  If 100-aa protein samples all conformations: 3^100 ≈ 10^47 states
  At 10^13 conformations/sec: ~10^34 years → impossible
  YET: proteins fold in microseconds to seconds
  Solution: folding proceeds by guided pathway, not random search

FOLDING FUNNEL:
  Energy landscape shaped like funnel → funnels toward native state
  Small proteins: 2-state (unfolded ↔ folded)
  Large proteins: kinetic intermediates, possible misfolding
  Chaperones (HSP70, HSP90, GroEL): prevent aggregation during folding
    → Provide folding chamber (GroEL/GroES: "Anfinsen cage")
    → Especially important for large, multidomain proteins

ALPHAFOLD2 (DeepMind, 2021):
  Input: amino acid sequence
  Output: 3D atomic coordinates (predicted per-residue accuracy pLDDT)
  Architecture: transformer-based with equivariant geometry module
  Performance: CASP14 TM-score ~0.9 (near experimental accuracy)
  Impact: 200M+ protein structures predicted (covers entire known proteome)
  Nobel Chemistry 2024: Jumper, Hassabis + Rumelhart (former)

PROTEIN MISFOLDING DISEASES:
  Amyloid β / Tau (Alzheimer's): β-sheet aggregates
  PrP prion (prion diseases): misfolded PrP templates normal PrP to misfold
  α-synuclein (Parkinson's): Lewy bodies
  Huntingtin (Huntington's): polyQ repeat expansion → aggregation
```

---

## Gene Regulation

```
TRANSCRIPTION FACTORS (TFs): proteins that bind specific DNA sequences → control transcription
  Activation domain: recruits RNAP or chromatin remodelers (HATs)
  Repressor domain: recruits HDACs, PRC complexes
  DBD (DNA-binding domain): zinc finger, bHLH, homeobox, leucine zipper

CIS-REGULATORY ELEMENTS:
  Promoter: immediately upstream of TSS (transcription start site)
  Enhancer: distal (10s kb - 1 Mb away), loops to promoter
    → Super-enhancers: multiple enhancers cluster → drive cell-identity genes
  Silencer: represses transcription
  Insulator (CTCF sites): block enhancer-promoter interactions

SIGNAL TRANSDUCTION → GENE REGULATION:
  Extracellular signal → receptor → cascade → TF modification → gene expression
  Examples:
    Wnt: β-catenin stabilized → enters nucleus → activates Wnt target genes
    MAPK: Ras → Raf → MEK → ERK → phosphorylates Elk1 → immediate early genes
    NF-κB: IκB degraded → NF-κB enters nucleus → inflammatory genes
    p53 (tumor suppressor): DNA damage → p53 stabilized → cell cycle arrest or apoptosis

EPIGENETIC REGULATION:
  DNA methylation: CpG methylation → transcription repression
    Maintained by DNMT1 (maintenance) and DNMT3A/B (de novo)
    Demethylation: TET enzymes (5mC → 5hmC → 5fC → 5caC → unmodified C)
  Histone modifications: post-translational modifications of histone tails
    Writers: HAT (histone acetyltransferase), HMT (histone methyltransferase)
    Erasers: HDAC (deacetylase), KDM (demethylase)
    Readers: BRD (bromodomain binds acetyl-lys), PHD (binds methyl-lys)
  Chromatin remodeling: SWI/SNF, ISWI complexes → move/eject nucleosomes
```

---

## Non-Coding RNAs

```
miRNA (microRNA): ~22 nt, regulates mRNA stability/translation
  Processed from hairpin precursor (Drosha → Dicer → RISC)
  Partial complementarity to 3'UTR → mRNA degradation or translational repression
  ~2500 human miRNAs; each regulates dozens to hundreds of mRNAs
  Development, differentiation, cancer (e.g., miR-21 oncomiR)

siRNA (small interfering RNA): ~21 nt, perfect complementarity → mRNA cleavage
  Natural: viral defense; therapeutic: RNAi knockdown (Alnylam drugs, Nobel 2006)
  RNAi therapeutics: siRNA packaged in LNP → liver delivery → knockdown target gene

lncRNA (long non-coding RNA): >200 nt, diverse functions
  XIST: X chromosome inactivation (coats X chromosome, recruits PRC2 → H3K27me3)
  MALAT1: pre-mRNA splicing regulation
  NEAT1: nuclear paraspeckle formation
  ~20,000 human lncRNAs (comparable to protein-coding genes!)

rRNA (ribosomal RNA): 28S, 18S, 5.8S, 5S — structural + catalytic in ribosome
  28S/5.8S = peptidyl transferase activity (true ribozyme!)
  Most abundant RNA in cell (~80% of total RNA)

tRNA: adaptor between codon and amino acid (~45 species in human)

snRNA: spliceosome components (U1, U2, U4, U5, U6)
snoRNA: guide RNA modification in nucleolus (rRNA 2'-O-methylation, pseudouridylation)
```

---

## Decision Cheat Sheet

| Level | What | Stored where | Error rate | Corrected by |
|-------|------|-------------|------------|-------------|
| DNA | Blueprint | Nucleus (both strands) | ~10⁻⁹/bp/division | MMR, BER, NER, DSBR |
| mRNA | Working copy | Cytoplasm | ~10⁻⁵/nt | NMD (nonsense-mediated decay) |
| Protein | Machine | Throughout cell | ~10⁻⁴/codon | Proteasome/autophagy |

| Feature | Prokaryote | Eukaryote |
|---------|-----------|---------|
| Nucleus | No | Yes |
| mRNA splicing | Rare (introns rare) | Yes (95% genes, many introns) |
| Ribosome | 70S | 80S |
| Transcription/translation coupling | Yes (co-translational) | No (separate compartments) |
| mRNA cap/poly(A) | No | Yes |
| Histone-based chromatin | No (most) | Yes |
| Operon organization | Yes | Rare |
| Transcription start | σ factor–10/–35 box | GTFs + TATA box / BRE |

---

## Common Confusion Points

**"Junk DNA" is wrong**: The term originated when only protein-coding sequences were considered functional. ~50% of the human genome is transposable elements — many are functional or have been co-opted as regulatory elements. ~8% is under purifying selection (ENCODE). Only ~1.5% encodes protein. The non-coding majority is complex, not random.

**mRNA is not a 1:1 copy of a gene**: Pre-mRNA undergoes 5' capping, 3' polyadenylation, and splicing (removing introns). ~95% of multi-exon genes are alternatively spliced → one gene locus → multiple distinct protein isoforms. The mRNA that reaches ribosomes may represent any of many possible exon combinations.

**DNA polymerase cannot start de novo**: All DNA pols require a free 3' OH — hence the need for RNA primers laid down by primase. On the lagging strand this creates the Okazaki fragment problem. Telomere shortening is a direct consequence of this primer requirement.

**Ribozymes are real catalysts**: The peptidyl transferase center of the ribosome (28S rRNA) is an RNA enzyme, not a protein enzyme. RNA predates proteins evolutionarily — this is the "RNA world" evidence. RNA can both store information (like DNA) and catalyze reactions (like protein).

**Protein half-life varies 100-fold**: Some proteins (e.g., cyclins, c-Myc) turn over in minutes; others (histones, structural proteins) last weeks. The ubiquitin-proteasome system targets proteins with degradation signals (degrons). Half-life is regulated, not constant.

**AlphaFold2 predicts structure, not dynamics**: AF2 produces a single static structure with per-residue confidence (pLDDT). It does not model conformational flexibility, allosteric changes, or binding-induced folding. Intrinsically disordered regions (IDRs) — common in regulatory proteins — are not well-handled.
