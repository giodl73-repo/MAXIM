# 03 — Genetics

## Mendelian Genetics, Chromosome Theory, Molecular Genetics, Genomics, Epigenetics, CRISPR

---

## Big Picture: Heredity Information Flow

```
GENETICS: How information is stored, transmitted, and expressed
──────────────────────────────────────────────────────────────────

DNA SEQUENCE  →  PHENOTYPE
(genotype)        (observable trait)

Via:
  Transcription    DNA → mRNA (gene expression)
  Translation      mRNA → Protein
  Post-translational modification (phosphorylation, glycosylation, etc.)
  Epigenetic control (methylation, histone modification)
  Development (tissue-specific expression from same genome)

THREE LEVELS OF HEREDITY:
  Mendelian:   gene = allele inheritance, discrete traits, Mendel's laws
  Chromosomal: genes on chromosomes, linkage, recombination, sex-determination
  Molecular:   DNA sequence → mutability, repair, gene regulation, epigenetics

FIELDS:
  Classical genetics:    Mendel-Morgan era; trait transmission rules
  Molecular genetics:    DNA structure → mutation → gene expression
  Population genetics:   allele frequencies in populations; evolution
  Quantitative genetics: polygenic traits, heritability, GWAS
  Genomics:              whole-genome sequencing, comparative genomics
  Epigenetics:           heritable changes not encoded in DNA sequence
──────────────────────────────────────────────────────────────────
```

---

<!-- @editor[bridge/P2]: No old-world bridge — genetic code = encoding scheme (redundant, error-minimizing, nearly universal = standardized protocol), CRISPR = find-and-replace with regex -->

## Mendelian Genetics

```
MENDEL'S LAWS (rediscovered 1900; pea experiments 1856-1863)

Law 1 — Segregation:
  Two copies of each gene (alleles) segregate during gamete formation
  Each gamete carries exactly one allele per gene
  Diploid organism: two alleles per locus (same = homozygous, different = heterozygous)

Law 2 — Independent Assortment:
  Genes on different chromosomes assort independently into gametes
  Produces 4 phenotypic classes in 9:3:3:1 ratio in F₂ dihybrid cross
  Exception: linked genes on same chromosome violate this (Morgan, 1910)

DOMINANCE RELATIONSHIPS:
  Complete dominance: A/a → A phenotype (a is recessive, A masks it)
  Incomplete dominance: A/a → intermediate phenotype (neither fully expressed)
  Codominance: A/a → both alleles expressed (ABO blood type: AB has both A and B antigen)

MONOHYBRID CROSS: Aa × Aa
  Gametes: A or a (each parent produces equally)
  Offspring ratio: 1 AA : 2 Aa : 1 aa  (genotypic)
                   3 A_ : 1 aa          (phenotypic, if A dominant)

DIHYBRID CROSS: AaBb × AaBb
  9 A_B_ : 3 A_bb : 3 aaB_ : 1 aabb
  (Law of Independent Assortment — genes on different chromosomes)

EXTENSIONS TO MENDELISM:
  Epistasis: one gene affects expression of another (coat color in dogs, mice)
    Recessive epistasis: aa masks B, giving 9:3:4 ratio
    Dominant epistasis: A_ masks, giving 12:3:1 ratio
  Multiple alleles: more than 2 alleles in population (ABO: I^A, I^B, i)
  Polygenic traits: multiple genes contribute to one trait (height, skin color)
  Pleiotropy: one gene affects multiple traits (sickle cell: anemia + malaria resistance)
```

---

## Chromosome Theory

```
CHROMOSOME THEORY OF HEREDITY (Sutton & Boveri, 1902-1903):
  Genes are on chromosomes
  Chromosomes behave like Mendel's factors: pair, segregate
  Chromosomes carry heredity from parent to offspring

MORGAN'S DROSOPHILA EXPERIMENTS (1910+):
  White eye gene on X chromosome → sex-linked inheritance pattern
  Autosomal vs sex-linked: males (XY) express X-linked recessive traits more often
  Linked genes: genes on same chromosome tend to be inherited together
  Recombination (crossing over): linked genes can be separated by meiotic crossover

GENETIC LINKAGE AND MAPS:
  Recombination frequency ≈ physical distance (up to 50 cM = unlinked)
  1 centimorgan (cM) = 1% recombination frequency ≈ ~1 Mb of DNA (rough average)
  Mapping: pairwise recombination frequencies → genetic map
  LOD score (Z): log₁₀(likelihood with linkage / likelihood without linkage)
    Z > 3 = strong evidence for linkage (1000:1 odds)

SEX DETERMINATION:
  XX/XY (mammals, Drosophila): SRY gene on Y triggers male development
  ZW/ZZ (birds, butterflies): females heterogametic (ZW)
  X inactivation (Lyon hypothesis): one X randomly inactivated in female cells → Barr body
    → dosage compensation; calico cat coloring (random X inactivation mosaic)
  Chromosomal abnormalities: XXY (Klinefelter), XO (Turner) — nondisjunction

MEIOSIS AND RECOMBINATION:
  Meiosis I: homologs pair (synapsis), crossing over (chiasmata), separate
  Meiosis II: sister chromatids separate (like mitosis)
  Synaptonemal complex: protein scaffold holding homologs during pachytene
  Crossover: DNA break + strand exchange (Holliday junction) → recombination
  1-3 crossovers per chromosome pair on average
  Obligate crossover: at least one per pair to ensure proper segregation
```

---

## DNA Mutation and Repair

```
MUTATION TYPES:
  Point mutations:
    Transition:      purine → purine (A↔G) or pyrimidine → pyrimidine (C↔T)
    Transversion:    purine → pyrimidine or vice versa
    Silent (synonymous): codon change → same amino acid (degenerate code)
    Missense:        codon change → different amino acid
    Nonsense:        codon → stop codon (truncated protein)
  Insertion/deletion (indel):
    Frameshift: ±1 or ±2 bp → reading frame shift → usually loss-of-function
    In-frame: ±3 bp → add/remove amino acid without frameshift
  Larger structural:
    Copy number variants (CNVs): segments duplicated or deleted (common in human genome)
    Inversions, translocations

MUTATION RATE:
  Human germline: ~1.1 × 10⁻⁸ per bp per generation
  → ~70 new mutations per individual per generation
  Somatic mutations: much higher per cell division; accumulate in cancer
  Mutagens: UV (pyrimidine dimers), alkylating agents, reactive oxygen species

DNA REPAIR PATHWAYS:
  Base excision repair (BER): glycosylase removes damaged base; fills gap
  Nucleotide excision repair (NER): removes bulky adducts (UV dimers); ~25-30 nt excised
    XP (Xeroderma Pigmentosum): NER deficiency → extreme UV sensitivity → skin cancer
  Mismatch repair (MMR): corrects replication errors
    Lynch syndrome: MMR mutation → colorectal + endometrial cancer risk
  Double-strand break repair:
    NHEJ (Non-Homologous End Joining): fast, error-prone
    HR (Homologous Recombination): accurate, requires sister chromatid (S/G2 phase)
    BRCA1/BRCA2: HR pathway → breast/ovarian cancer when mutated
  DNA damage checkpoint:
    ATM → CHK2 → p53 → cell cycle arrest or apoptosis ("guardian of the genome")
```

---

## Molecular Genetics: Gene Expression

```
GENE STRUCTURE (eukaryote):
  5' UTR — Exon 1 — Intron 1 — Exon 2 — Intron 2 — ... — Exon n — 3' UTR — poly-A signal

  Promoter elements:
    TATA box (~30 bp upstream) — basal transcription factor assembly
    CpG islands — often at promoters, methylation regulates access
    Enhancers — can be kb to Mb distant; looping brings to promoter
    Silencers — repress transcription

  Pre-mRNA processing:
    5' capping: 7-methylguanosine cap (protects, ribosome recognition)
    3' polyadenylation: poly-A tail (stability, export)
    Splicing: spliceosome removes introns (U1/U2/U4/U5/U6 snRNPs)
    Alternative splicing: ~95% of multi-exon genes → protein diversity from one gene
      DSCAM (Drosophila): up to 38,016 isoforms (axon guidance)

GENE REGULATION (eukaryote):
  Transcription factors (TF): bind DNA → activate or repress RNA Pol II
    Master regulators: MyoD (muscle), Pax6 (eye), Oct4/Sox2/Klf4/c-Myc (pluripotency)
  Chromatin remodeling: SWI/SNF complex moves nucleosomes to expose DNA
  Histone modifications:
    H3K4me3  → active promoter
    H3K27ac  → active enhancer
    H3K27me3 → Polycomb silencing
    H3K9me3  → constitutive heterochromatin
  Non-coding RNAs:
    miRNA: ~22 nt; binds mRNA 3' UTR → translation repression or degradation
    lncRNA: >200 nt; XIST (X inactivation), HOTAIR (chromatin regulation)
    siRNA: exogenous dsRNA → RISC complex → mRNA cleavage
```

---

## Epigenetics

```
EPIGENETICS: heritable changes in gene expression NOT in DNA sequence

DNA METHYLATION:
  5-methylcytosine (5mC) at CpG dinucleotides
  DNMT1: maintenance methyltransferase (copies pattern after replication)
  DNMT3A/3B: de novo methyltransferases (establish new patterns)
  TET enzymes: oxidize 5mC → demethylation pathway
  CpG island promoter methylation → gene silencing

GENOMIC IMPRINTING:
  ~80-100 imprinted genes in mammals
  Allele-specific methylation set during gametogenesis
  Prader-Willi syndrome: deletion of paternal 15q11-q13
  Angelman syndrome: same deletion, maternal origin → completely different phenotype
  → demonstrates epigenetic identity of alleles

HISTONE CODE:
  Histone tails → post-translational modifications
  Readers, writers, erasers for each modification:

  Mark       Writer     Effect
  ─────────────────────────────────────────────────
  H3K4me3    MLL/SET1   Active promoter
  H3K27me3   EZH2       Polycomb silencing
  H3K9me3    SUV39H     Constitutive heterochromatin
  H3K27ac    CBP/p300   Active enhancer

TRANSGENERATIONAL EPIGENETICS:
  Strong evidence in plants and C. elegans; debated in mammals
  Resetting at fertilization (near-global demethylation)
  Some loci escape → potential inherited epigenetic effects
  Dutch Hunger Winter: prenatal famine → measurable epigenetic changes 60 years later
```

---

## Genomics

```
SEQUENCING TECHNOLOGIES:
  Sanger (1977): dideoxy chain termination; gold standard accuracy; low throughput
  Next-generation sequencing (NGS):
    Illumina: short reads 150-300 bp, massively parallel, low error rate (~0.1%)
    PacBio HiFi: 10-25 kb reads, <1% error rate (long + accurate)
    Oxford Nanopore: real-time, portable, reads up to Mb, ~5% error (improving)

  Cost trajectory:
    2000: ~$100M per genome
    2007: ~$1M
    2009: $10K
    2022: ~$200 → genomics as big data

GENOME SEQUENCING MILESTONES:
  2001: Draft human genome (HGP + Celera), 92% assembled
  2003: Human Genome Project "complete" (still had ~8% gaps)
  2022: T2T Consortium — truly complete (all centromeres, all repeats)
  Pan-genome: multiple reference genomes capture human diversity (2023 draft)

GWAS (Genome-Wide Association Studies):
  Scan ~5M SNPs across genome for disease association
  Manhattan plot: −log₁₀(p) vs genomic position
  Significance threshold: p < 5×10⁻⁸ (multiple testing correction)
  Linkage disequilibrium (LD): nearby SNPs correlated → tag haplotypes
  Challenge: most GWAS hits in non-coding regulatory regions

FUNCTIONAL GENOMICS TOOLKIT:
  RNA-seq:          all expressed transcripts + levels; differential expression
  ChIP-seq:         protein-DNA binding (TFs, histone marks)
  ATAC-seq:         open chromatin (accessible regulatory regions)
  scRNA-seq:        single-cell transcriptomics → cell type atlas
  Hi-C:             3D genome organization (TADs, loops, A/B compartments)
  Spatial transcriptomics: mRNA levels with tissue spatial coordinates

COMPARATIVE GENOMICS:
  Human-chimp: ~98.7% identical
  Human-mouse: ~85% coding identity; ~50% overall
  Non-coding constraint: ~5-8% of genome under purifying selection
  Synteny: conserved gene order → identify homologous regions
```

---

## CRISPR-Cas9

```
NATURAL FUNCTION:
  Bacterial adaptive immune system (Barrangou 2007)
  CRISPR loci: array of spacers (captured viral sequences)
  Cas proteins use spacer as guide to cut re-infecting viral DNA

MECHANISM (Doudna, Charpentier 2012 — Nobel 2020):
  1. Single-guide RNA (sgRNA): 20 nt guide + scaffold
  2. Cas9:sgRNA complex scans DNA
  3. PAM recognition: 5'-NGG-3' (required; on non-target strand adjacent to 20 nt target)
  4. Guide-target complementarity → R-loop formation
  5. HNH nuclease cuts guide-complementary strand
     RuvC nuclease cuts other strand → blunt DSB 3 bp upstream of PAM

REPAIR OUTCOMES:
  NHEJ: indels at cut site → frameshift → gene knockout
  HDR (with donor template): precise edit; requires S/G2 phase; low efficiency in vivo

ADVANCED TOOLS:
  dCas9 (dead): DNA binding only, no cut
    CRISPRi: dCas9-KRAB → transcriptional repression
    CRISPRa: dCas9-VPR → transcriptional activation
  Base editors (David Liu):
    CBE: C → T at target position (no DSB; cytosine deaminase)
    ABE: A → G at target position (no DSB; tRNA adenosine deaminase)
  Prime editing:
    pegRNA encodes both guide + edit (up to 44 nt insertion; all 12 base substitutions)
    Cas9 nickase + reverse transcriptase; no DSB; "search and replace"

THERAPEUTIC STATUS (2024):
  Casgevy (exa-cel): FDA approved Dec 2023 for sickle cell + β-thalassemia
    CRISPR edit of BCL11A enhancer → reactivates fetal hemoglobin
  Multiple Phase 1/2 trials: TTR amyloidosis, Duchenne MD, leukemia (allogeneic CAR-T)
  Delivery challenges for in vivo: LNP (liver), AAV (CNS), ex vivo edit + reinfuse (blood)
```

---

## Decision Cheat Sheet

| Goal | Method | Key Caveat |
|------|--------|------------|
| Knockout gene (cell line) | CRISPR-Cas9 + NHEJ | Verify with sequencing; beware frameshift +3 |
| Correct pathogenic SNP | Base editor (CBE/ABE) | Need C→T or A→G; check editing window position |
| Activate/repress without editing | CRISPRa/CRISPRi | Reversible; no sequence change |
| Find disease variant associations | GWAS | Need large N; most hits in non-coding |
| Whole transcriptome expression | RNA-seq | Normalize; bioinformatics pipeline needed |
| Single-cell heterogeneity | scRNA-seq | Batch correction; clustering algorithm choice |
| Map regulatory elements | ATAC-seq + ChIP-seq | Antibody quality critical for ChIP |
| Understand inheritance pattern | Mendelian analysis | Check penetrance, expressivity, epistasis |
| Identify functional non-coding regions | Evolutionary constraint (PhyloP/PhastCons) | High constraint = likely functional |
| Assign epigenetic state | Histone marks (H3K4me3/H3K27ac etc.) | Combinatorial; need multiple marks |

---

## Common Confusion Points

**Recessive ≠ rare**: Cystic fibrosis carrier frequency ~1/30 in Europeans — common allele. Recessiveness is about expression pattern, not allele frequency.

**X-linked recessive in females**: A female with one affected X allele is a carrier. She can pass it to sons (50% affected) or daughters (50% carriers). Males have only one X, so they either express or don't.

**Epigenetics ≠ Lamarckism**: Epigenetic marks are reset in germline mostly. Acquired somatic epigenetic changes don't generally transmit to offspring. Dutch Hunger Winter effects are real but don't constitute Lamarckian inheritance.

**CRISPR PAM is on the non-target strand**: Design guides matching the strand that does NOT have NGG immediately after the target. The 20 nt in the guide RNA matches the strand that IS cut by HNH (complementary to PAM strand).

**HDR efficiency in vivo**: Efficient in rapidly dividing cells (bacteria, yeast, cancer cell lines, iPSCs). Very inefficient in quiescent somatic cells. For therapeutic editing in liver/blood: base editing or ex vivo approaches.

**Missing heritability in GWAS**: Discovered GWAS SNPs typically explain 10-40% of heritability. The rest is in rare variants, gene-gene interactions (epistasis), structural variants, and potentially epigenetic variation — not that traits aren't heritable.

**Alternative splicing multiplies proteome**: ~20,000 protein-coding genes → >100,000 protein isoforms. DSCAM has ~38,000 isoforms from one gene. Gene count alone understates biological complexity.
