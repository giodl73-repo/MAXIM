# 09-MOLECULAR-BIO — Molecular Biology

> DNA replication, transcription, translation, gene regulation, CRISPR.
> The central dogma: how sequence information flows from storage to function,
> and the machinery that enforces every step.

---

## The Central Dogma

```
              Replication
          ┌──────────────────┐
          ▼                  │
         DNA ──Transcription──▶ RNA ──Translation──▶ Protein
          │
          └── Reverse transcription (retroviruses, telomerase)

Exceptions to "one-way" flow:
  RNA → DNA:     Reverse transcriptase (HIV, LINE retrotransposons, telomerase)
  RNA → RNA:     RNA-dependent RNA polymerase (RNA viruses, RNAi pathway)
  Protein → ?:   No known mechanism for protein→nucleic acid (prions alter folding, not sequence)

Information is in the sequence:
  DNA:  4-letter alphabet (A, T, G, C), double-stranded, stable, archive
  RNA:  4-letter alphabet (A, U, G, C), single-stranded, transient, working copy
  Protein: 20-letter alphabet, 3D fold, functional executor
```

---

## DNA Replication

### Semi-Conservative Replication

Each daughter cell receives one original strand + one new strand.
Proved by Meselson-Stahl (1958): density-labeled ¹⁵N DNA replicated in ¹⁴N → hybrid bands.

### The Replisome

```
INITIATION:
  Origin of replication (ori): specific sequences where replication begins
    Prokaryotes: single circular chromosome, one ori (oriC in E. coli)
    Eukaryotes: multiple origins (thousands per chromosome) → parallel firing

  Origin Recognition Complex (ORC): marks origins
  Helicase loading: MCM2-7 helicase loaded at G1, activated at S phase
  Replication fires → two diverging replication forks

FORK STRUCTURE (both strands replicated simultaneously):

  ─────────────── 3'→5' template (leading)
  ←══════════════ Leading strand (synthesized 5'→3', continuous)

  ─────────────── 5'→3' template (lagging)
  ═════════════→  Lagging strand (synthesized 5'→3' = AWAY from fork)
  ↑               Okazaki fragments (~1–2 kb in eukaryotes, ~1–2 kb in bacteria)
  synthesized in short discontinuous pieces, joined by DNA ligase
```

### Key Enzymes

```
Enzyme                   Function
──────────────────────────────────────────────────────────────
Helicase (MCM2-7)        Unwinds double helix (ATP-dependent, moves 5'→3')
Topoisomerase I          Nicks one strand → relieves torsional stress (ahead of fork)
Topoisomerase II         Nicks both strands → decatenation (separates daughter chromosomes)
Primase (DnaG)           Synthesizes RNA primer (~10 nt) — DNA pol can't start de novo
DNA Pol δ (eukaryote)    Lagging strand synthesis (with PCNA clamp)
DNA Pol ε (eukaryote)    Leading strand synthesis
DNA Pol α                Primase-associated, initiates Okazaki fragments
RNase H / FEN1           Removes RNA primers
DNA Ligase               Seals nicks (NAD⁺ in bacteria, ATP in eukaryotes)
PCNA                     Sliding clamp (processivity factor, ring loads onto DNA)
RFC                      Clamp loader (loads PCNA, ATP-dependent)
RPA                      Single-stranded DNA binding (protects ssDNA at fork)
```

### Proofreading and Fidelity

```
Error rate without proofreading: ~10⁻⁵ per base
After 3'→5' exonuclease proofreading (DNA pol): ~10⁻⁷
After mismatch repair (MMR): ~10⁻⁹–10⁻¹⁰

Mismatch repair (MMR):
  MutS (eukaryote: MSH2/MSH6) recognizes mismatch
  MutL (MLH1/PMS2) recruits MutH
  MutH nicks the unmethylated strand (newly synthesized, not yet methylated)
  Exonuclease removes mispaired region, resynthesis + ligation
  HNPCC (hereditary colon cancer): MMR gene mutations
```

### Telomeres and Telomerase

```
Problem: DNA pol requires primer → can't replicate chromosome ends fully
→ "end replication problem" → telomeres shorten with each division

Telomere structure: TTAGGG repeats (vertebrates), 5–15 kb
Shelterin complex: TRF1/TRF2/POT1/TIN2/TPP1/RAP1 → caps telomere, prevents
  DDR (DNA damage response) activation and end-to-end fusions

Telomerase: ribonucleoprotein (TERT + TERC RNA template)
  Uses its RNA as template to extend 3' overhang
  Then primase fills in complementary strand
  Active in: stem cells, germline, most cancers
  Inactive in: most somatic cells → progressive shortening → Hayflick limit (~50 divisions)

Cancer and telomerase: >85% of cancers reactivate telomerase → immortalization
Alternative lengthening of telomeres (ALT): recombination-based (15% of cancers)
```

---

## Transcription

### Prokaryotic Transcription

```
RNAP (E. coli): α₂ββ'ω core + σ factor (holoenzyme)
σ factor: recognizes promoter, destabilizes after initiation (σ⁷⁰ for housekeeping genes)

Promoter elements (consensus):
  −35 box: TTGACA   (σ recognition)
  −10 box: TATAAT   (Pribnow box — melted/unwound for initiation)
  Spacer: 17 bp between −35 and −10

Stages:
  Closed complex: RNAP binds promoter, double-stranded
  Open complex: ~14 bp melted (ATP not required in bacteria)
  Initiation: first ~10 nt synthesized (often abortive)
  Promoter escape: σ released, elongation complex stable
  Elongation: ~40–80 nt/s, highly processive, template read 3'→5'
  Termination:
    Rho-independent: hairpin in RNA + U-rich → destabilizes RNA:DNA hybrid
    Rho-dependent: Rho helicase (ATP-dep.) tracks mRNA, catches paused RNAP
```

### Eukaryotic Transcription — More Complex

```
Three nuclear RNAPs:
  RNA Pol I:   rRNA (45S precursor in nucleolus)
  RNA Pol II:  mRNA + most non-coding RNA (snRNA, miRNA)
  RNA Pol III: tRNA, 5S rRNA, small stable RNAs

RNA Pol II promoter elements:
  TATA box (~−25): bound by TBP (TATA-binding protein)
  Inr (initiator): at +1 transcription start
  BRE, DPE, MTE: additional elements
  Enhancers: 100s–1000s of bp away, orientation-independent, cell-type specific
             bind transcription factors → loop to promoter via Mediator

General transcription factors (GTFs):
  TFIID (TBP+TAFs) → TFIIB → Pol II/TFIIF → TFIIE → TFIIH
  TFIIH: helicase (unwinds DNA), CTD kinase (phosphorylates Pol II tail → elongation)

CTD (C-terminal domain of Pol II): 52 heptad repeats (YSPTSPS)
  Hypophosphorylated: associates with Mediator (initiation)
  Ser5-P: early elongation, capping enzyme recruitment
  Ser2-P: active elongation, splicing factor recruitment, 3' processing
```

### Pre-mRNA Processing (Eukaryotes Only)

```
5' CAPPING (co-transcriptional, at ~25 nt):
  7-methylguanosine cap added in 5'→5' triphosphate linkage (unusual bond)
  Functions: protects from 5' exonucleases, ribosome recognition (eIF4E binding)

SPLICING (co-transcriptional and post-transcriptional):
  Spliceosome: U1, U2, U4, U5, U6 snRNAs + ~100 proteins
  Two-step transesterification:
    1. 2'-OH of branch point A attacks 5' splice site → lariat intermediate
    2. 3'-OH of exon 1 attacks 3' splice site → ligation of exons, lariat released

  Splice sites (consensus):
    5' splice site: GU (GT in DNA) — nearly invariant
    3' splice site: AG — nearly invariant
    Branch point: YNYURAY (~30 nt upstream of 3' ss)
    Polypyrimidine tract: between branch point and 3' ss

ALTERNATIVE SPLICING:
  ~95% of human multi-exon genes alternatively spliced
  Types: exon skipping, alternative 5'/3' splice sites, intron retention, mutually exclusive exons
  Creates proteome diversity >> genome size
  Cell-type specific splicing factors (SR proteins, hnRNPs) control patterns

3' POLYADENYLATION:
  AAUAAA signal (~20 nt upstream of cleavage site)
  Cleavage + addition of 150–250 A residues by poly(A) polymerase
  Functions: export, stability, translation efficiency
```

---

## Translation

### The Genetic Code

```
CODON TABLE (standard genetic code):
  64 codons: 61 sense + 3 stop (UAA, UAG, UGA)
  20 amino acids → code is REDUNDANT (degenerate)
  Third position often wobble (less constrained) — synonymous codons

  Start codon: AUG (Met) — also defines reading frame
  Stop codons: UAA (ochre), UAG (amber), UGA (opal/umber)

  Code is nearly universal — exceptions: mitochondria (UGA → Trp), ciliates (UAA/UAG → Gln)
  Wobble (Crick, 1966): tRNA anticodon position 34 can pair with multiple codons
    G34 pairs with U or C; I (inosine, modified A) pairs with U, C, or A
```

### Ribosome Structure

```
Prokaryote (70S):          Eukaryote (80S):
  Small: 30S (16S rRNA)      Small: 40S (18S rRNA)
  Large: 50S (23S+5S rRNA)   Large: 60S (28S+5.8S+5S rRNA)

Three tRNA binding sites on ribosome:
  A site (aminoacyl): accepts incoming aminoacyl-tRNA
  P site (peptidyl): holds growing peptide chain
  E site (exit): departing tRNA

rRNA is catalytic: peptidyl transferase activity resides in 23S/28S rRNA
  (proteins provide structural scaffold only)
  → another example of ribozyme catalysis
```

### Translation Mechanism

```
INITIATION (prokaryote):
  30S + mRNA (Shine-Dalgarno: AGGAGG, ~5–10 nt upstream of AUG)
  IF1, IF2 (GTPase), IF3
  fMet-tRNA binds P site at AUG
  50S joins → GTP hydrolysis → IFs released → 70S initiation complex

INITIATION (eukaryote — scanning model):
  43S complex: 40S + eIF1/1A/3/5 + Met-tRNA·eIF2·GTP
  eIF4F (cap-binding complex): eIF4E (cap) + eIF4G (scaffold) + eIF4A (helicase)
  Scans 5'→3' until AUG in Kozak context (GCCRCCAUGG)
  eIF5 triggers GTP hydrolysis → 60S joining

ELONGATION:
  EF-Tu (prokaryote) / eEF1A (eukaryote): delivers aminoacyl-tRNA to A site (GTPase)
  Proofreading: codon-anticodon mismatch → GTP hydrolysis before full accommodation
  Peptidyl transfer: peptide bond formation (ribosome catalysis, no energy input)
  Translocation: EF-G/eEF2 (GTPase) moves ribosome 3 nt → P→E, A→P
  Rate: ~20 aa/s (prokaryote), ~5 aa/s (eukaryote)

TERMINATION:
  Stop codon in A site → release factor (RF1/RF2 in bacteria, eRF1 in eukaryotes)
  Peptidyl-tRNA hydrolysis → polypeptide release
  Ribosome recycling factor (RRF) + EF-G dissociate ribosome

POLYRIBOSOMES (polysomes): multiple ribosomes translating same mRNA simultaneously
```

---

## Gene Regulation

### Prokaryotic: The lac Operon

```
lacI ──┬── lacZ (β-galactosidase) ── lacY (permease) ── lacA (transacetylase)
       │
       └── Repressor (LacI protein)

NO lactose, NO glucose:
  Repressor binds operator → blocks transcription
  CAP (CRP) + cAMP binds → activates promoter (cAMP high when glucose low)

NO lactose, HIGH glucose:
  Repressor ON (no inducer), CAP OFF (low cAMP) → transcription off

LACTOSE present, NO glucose:
  Allolactose (lactose metabolite) binds repressor → conformational change → off DNA
  CAP ON (high cAMP) → full transcription activation
  → express lactose-metabolizing genes only when needed AND glucose unavailable

LACTOSE present, GLUCOSE present:
  Repressor OFF (allolactose present), but CAP OFF (low cAMP) → low transcription
  → glucose preferred; lac genes minimally expressed (catabolite repression)
```

### Eukaryotic Gene Regulation

```
Layers of eukaryotic regulation:
  1. Chromatin (DNA accessibility):
       Nucleosome: 147 bp DNA wrapped ~1.65 turns around H2A/H2B/H3/H4 octamer
       Histone code: modifications to histone tails
         H3K4me3: active promoter marker
         H3K27me3: Polycomb repression
         H3K9me3: heterochromatin
         H3K27ac: active enhancer
         H4K16ac: chromatin opening
       Chromatin remodelers (SWI/SNF, NuRD): reposition nucleosomes

  2. DNA methylation:
       CpG methylation (5-methylcytosine): gene silencing
       Promoter CpG islands (CpG dense regions): unmethylated → active
       Gene body methylation: associated with active transcription
       Imprinting: differential methylation of maternal vs paternal alleles

  3. Transcription factors:
       Combinatorial: multiple TFs → AND/OR/NOT logic
       Enhancers: bound by TF combos → loop to promoter via cohesin/CTCF
       Super-enhancers: large clusters of enhancers → cell identity genes

  4. Post-transcriptional:
       miRNA (miRISC): seed sequence (~6-7 nt) base-pairs with mRNA 3'UTR
         → mRNA degradation or translational repression
       Nonsense-mediated decay (NMD): degrades mRNA with premature stop codons
       RNA-binding proteins: stability, splicing, localization
```

---

## CRISPR-Cas9 Mechanism

```
NATURAL FUNCTION (bacterial adaptive immunity):
  Bacteria capture fragments of invading phage DNA → store in CRISPR array
  Array transcribed → crRNA + tracrRNA → processed → guides Cas9 to matching sequence
  Cas9 + guide RNA → cleave matching foreign DNA

MECHANISM:
  1. Guide RNA (sgRNA = crRNA + tracrRNA fusion): ~100 nt
  2. sgRNA base-pairs with target DNA strand (20 nt protospacer)
  3. PAM (protospacer adjacent motif): NGG for SpCas9 — REQUIRED, on non-target strand
  4. R-loop formation: DNA unwinds, sgRNA:DNA hybrid forms
  5. RuvC domain cleaves non-template strand
     HNH domain cleaves template strand
  6. DSB (double-strand break) generated at position 3 nt upstream of PAM

REPAIR PATHWAYS:
  NHEJ (non-homologous end joining): error-prone ligation → insertions/deletions (indels)
    → frameshift → loss-of-function (gene knockout)
  HDR (homology-directed repair): template provided → precise edit
    → gene correction, insertion of sequence (less efficient, requires S/G2)

CRISPR VARIANTS:
  Cas12a (Cpf1): T-rich PAM, cuts 5' of PAM, staggered cut, processes own crRNA
  Cas13: targets RNA (not DNA) — knockdown without genome editing
  dCas9 (dead Cas9, D10A+H840A): no cutting activity
    + transcriptional activator (VPR, SAM) → CRISPRa
    + transcriptional repressor (KRAB) → CRISPRi
    + base editor (adenine or cytosine deaminase) → A→G or C→T without DSB
    + prime editor (reverse transcriptase) → precise edits without DSB or template
```

---

## Central Dogma Exceptions and Edge Cases

```
Retroviruses (HIV):
  RNA genome → Reverse Transcriptase → dsDNA → integrates as provirus → transcribed

Retrotransposons (LINEs, SINEs):
  ~45% of human genome by mass
  LINEs encode reverse transcriptase → copy-paste mechanism → genome expansion

Telomerase:
  Specialized reverse transcriptase; uses internal RNA template to extend telomeres

Prions:
  Infectious misfolded proteins (PrPᶜ → PrPˢᶜ)
  Protein conformation can "replicate" by templating misfolding of normal copies
  Not a violation of central dogma (sequence not altered), but information in
  protein conformation propagates — a form of epigenetic inheritance

RNA self-splicing (group I and II introns):
  Catalytic RNA performs own splicing without proteins
  Group II introns: proposed ancestor of spliceosomal snRNAs

Selenocysteine / pyrrolysine:
  21st and 22nd amino acids encoded by UGA/UAG stop codons in specific contexts
  Require special tRNAs and recoding factors — expand the genetic code
```

---

## Decision Cheat Sheet

| Question | Concept | Key detail |
|----------|---------|-----------|
| Why does lagging strand need Okazaki fragments? | 5'→3' synthesis constraint | DNA pol can only add to 3'-OH; lagging template runs wrong way |
| What prevents re-replication of origins? | MCM licensing | ORC/MCM loaded at G1; Geminin inhibits re-loading in S/G2 |
| Why does eukaryotic Pol II need cap before elongation? | CTD phosphorylation | TFIIH phosphorylates Ser5 → triggers capping enzyme recruitment |
| What does the TATA box do? | TBP binding | Positions RNA Pol II at +1; not all promoters have TATA box |
| Why is alternative splicing important? | Proteome diversity | ~20,000 genes → >100,000 proteins via differential exon inclusion |
| What stops translation at stop codons? | Release factors | No tRNA recognizes stop; eRF1 mimics tRNA shape |
| How does miRNA silence genes? | RISC complex | miRNA:mRNA base pairing → deadenylation, decapping, or repression |
| Why does CRISPR need PAM? | Cas9 mechanism | PAM recognition triggers R-loop; prevents Cas9 cutting its own CRISPR array |
| What is the Kozak sequence? | Eukaryotic initiation | Context around AUG affects 43S scanning efficiency |
| Why do retroviruses integrate? | Proviral strategy | dsDNA copy inserted by integrase; expressed by host RNA Pol II |

---

## Common Confusion Points

**Template strand vs coding strand vs sense strand**
Template strand: read by RNA polymerase (3'→5') — the actual template.
Coding strand (= non-template = sense strand): same sequence as mRNA (with T→U).
By convention, gene sequences are given in the 5'→3' direction of the coding strand.
"Antisense" in RNAi/siRNA refers to the strand complementary to mRNA.

**Transcription and translation are not coupled in eukaryotes**
In bacteria: ribosomes attach to mRNA as it's being transcribed (coupled).
In eukaryotes: transcription in nucleus, processing, export via nuclear pore,
then translation in cytoplasm. Each step is a regulatory checkpoint.

**The spliceosome removes introns — but "intron" is defined operationally**
"Intron" = sequence removed from pre-mRNA. Some introns are regulatory in other contexts
(intronic enhancers, circRNA from back-splicing, miRNAs encoded in introns).
The genome doesn't neatly divide into "coding" and "junk" — it's deeply interleaved.

**CRISPR edits are permanent in dividing cells but not in all tissues**
A CRISPR edit in a cell's genome is heritable to daughter cells.
But in post-mitotic cells (neurons, muscle), HDR is unavailable.
In vivo delivery of CRISPR (AAV, LNP) must reach the right cells.
"Gene editing" a whole organism requires editing the germline or very early embryo.

**mRNA stability varies enormously**
Bacterial mRNA: half-life ~2 min (tight coupling of expression to need).
Eukaryotic mRNA: seconds (unstable) to hours/days (stable).
Stability determinants: AU-rich elements (AREs) in 3'UTR, codon optimality,
5' cap protection, miRNA targeting, poly(A) tail length.
