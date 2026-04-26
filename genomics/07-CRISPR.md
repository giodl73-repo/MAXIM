# CRISPR Gene Editing

## The Big Picture

```
CRISPR: PROGRAMMABLE GENOME EDITING
=====================================

  ORIGIN: Discovered as a bacterial immune memory system
  Bacteria use it to remember and destroy viral DNA
  Jennifer Doudna + Emmanuelle Charpentier repurposed it (2012 Nobel, 2020)
  (→ microbiology/08-MICROBIAL-GENETICS.md for the natural system)

  CONCEPTUAL FRAMING:
  ┌──────────────────────────────────────────────────────────────────┐
  │ guide RNA (gRNA)   = search string    (20 nucleotide sequence)   │
  │ PAM sequence       = anchor/constraint (NGG for SpCas9)          │
  │ Cas9 protein       = the search + cut engine                     │
  │ DNA double-strand  = target data      (3 billion character string)│
  │                                                                  │
  │ System finds the first 20-nt match to gRNA adjacent to PAM,      │
  │ then cuts both strands of DNA. DNA repair mechanisms do the rest.│
  │                                                                  │
  │ Like regex search + cut on the human genome.                     │
  └──────────────────────────────────────────────────────────────────┘

  WHAT YOU CAN DO:
  ┌────────────────────────────────────────────────────────────────┐
  │ DISRUPT (knock out)    Cut + error-prone repair → frameshift   │
  │ CORRECT (knock in)     Cut + homology-directed repair template │
  │ BASE EDIT              Change 1 base without cutting DNA       │
  │ PRIME EDIT             Insert/delete/substitute without DSB    │
  │ REGULATE (CRISPRi/a)   Block or activate transcription         │
  │ LABEL (CRISPRimaging)  Fluorescent tag on specific locus       │
  │ SCREEN                 Library of gRNAs to find gene function  │
  └────────────────────────────────────────────────────────────────┘
```

---

## The Cas9 Mechanism

```
  CAS9 SEARCH AND CUT MECHANISM
  ================================

  STEP 1: PAM RECOGNITION
  Cas9 scans DNA looking for NGG (PAM: Protospacer Adjacent Motif)
  SpCas9 PAM: 5'–NGG–3' (N = any base)

  In the 3.2 Gb human genome:
  NGG occurs every ~8 bp on average → ~1 billion PAM sites total
  Any 20-nt target adjacent to NGG = potential edit site

  STEP 2: SEED REGION CHECK
  Bases 1–10 of gRNA (adjacent to PAM) = "seed region"
  Even 1–2 mismatches in seed region → no cutting
  This limits off-target effects

  STEP 3: R-LOOP FORMATION
  gRNA base-pairs with target DNA strand (20 bp)
  Creates R-loop: gRNA:DNA hybrid + displaced DNA strand

  ┌─────────────────────────────────────────────────────────────┐
  │  5'─ NNNNNNNNNNNNNNNNNNNNNGG ─3'  (genomic DNA, PAM strand) │
  │  3'─ NNNNNNNNNNNNNNNNNNNNN    ─5'  (non-PAM strand)         │
  │                                                             │
  │       ↑ 20-nt target sequence                               │
  │       └── guide RNA anneals here                            │
  └─────────────────────────────────────────────────────────────┘

  STEP 4: DOUBLE-STRAND BREAK (DSB)
  Two nuclease domains:
  - RuvC domain: cuts non-PAM strand
  - HNH domain: cuts PAM strand
  Result: Blunt-ended DSB at position 3 bp upstream of PAM

  EDIT SITE = 3 bp upstream of PAM
  NGG motif intact after cutting (on PAM strand fragment)
```

---

## DNA Repair After Cas9 Cutting

```
  TWO REPAIR PATHWAYS — DETERMINE EDIT OUTCOME
  ==============================================

  PATHWAY 1: NHEJ (Non-Homologous End Joining)
  ─────────────────────────────────────────────
  DEFAULT repair in most cells
  Fast, error-prone
  Ligates broken ends directly

  RESULT: Small insertions or deletions (indels)
  ─ Most common: 1-bp insertion (most common) or 1–20 bp deletion
  ─ ~50–80% of cuts produce frameshift mutations
  ─ Frameshift in coding exon → premature stop codon → protein KO

  USE CASE: Gene knockout
  ┌──────────────────────────────────────────────────────┐
  │ Wild-type: ATCGATCGATCGATCG → Protein: IDIDID        │
  │ +1 insertion: ATCG[A]ATCGATCGATCG → IDIDX (frame     │
  │   shift, garbage protein → nonsense-mediated decay)  │
  └──────────────────────────────────────────────────────┘

  PATHWAY 2: HDR (Homology-Directed Repair)
  ──────────────────────────────────────────
  Uses a DNA template for precise repair
  Template can be: single-stranded oligonucleotide (ssODN),
                   plasmid, or recombinant virus (AAV)

  RESULT: Precise insertion, deletion, or base substitution
  ─ Efficiency: 0.1–10% in most cells (vs. 50–80% for NHEJ)
  ─ Requires: Template DNA + cells actively dividing (S/G2 phase)
  ─ Best in: iPSCs, dividing cell lines, early embryos

  USE CASE: Gene correction, reporter knock-in, disease modeling

  ┌──────────────────────────────────────────────────────────┐
  │ CUT AT DISEASE MUTATION                                  │
  │ + ssODN template with corrected sequence                 │
  │ HDR uses template: MUTANT → WILD-TYPE restored           │
  │ Application: Sickle cell / beta-thalassemia correction   │
  └──────────────────────────────────────────────────────────┘
```

---

## CRISPR Delivery Methods

```
  DELIVERY VECTORS: GETTING CRISPR INTO CELLS
  =============================================

  CHALLENGE: Cas9 protein (~160 kDa) + gRNA (100 nt) must enter
             nucleus of target cells.

  ┌──────────────────────────────────────────────────────────────────┐
  │ METHOD          │ CARGO              │ PROS          │ CONS      │
  ├─────────────────┼────────────────────┼───────────────┼───────────┤
  │ Plasmid DNA     │ SpCas9 + gRNA gene │ Cheap, easy   │ Transient │
  │ electroporation │                    │ for cell lines│ immune    │
  ├─────────────────┼────────────────────┼───────────────┼───────────┤
  │ RNP             │ Cas9 protein       │ Low off-target│ Expensive │
  │ electroporation │ + gRNA (complex)   │ Transient     │ per-use   │
  ├─────────────────┼────────────────────┼───────────────┼───────────┤
  │ Lentivirus      │ Cas9 + gRNA gene   │ High efficiency│ Integrates│
  │                 │ (integrating)      │ for screens   │ genome    │
  ├─────────────────┼────────────────────┼───────────────┼───────────┤
  │ AAV             │ gRNA + template    │ In vivo       │ 4.7 kb    │
  │ (adeno-assoc.)  │ (small Cas9 only)  │ tissue-target │ size limit│
  ├─────────────────┼────────────────────┼───────────────┼───────────┤
  │ LNP             │ mRNA (Cas9) +      │ Transient     │ Liver-    │
  │ (lipid NP)      │ gRNA               │ No virus      │ tropic    │
  └──────────────────────────────────────────────────────────────────┘

  IN VIVO DELIVERY CHALLENGE:
  Ex vivo: Edit cells outside the body, infuse back (CAR-T, sickle cell)
  In vivo: Deliver editing machinery directly to tissue
           Liver: LNP works well (IV injection → ~80% liver)
           Eye: Local injection (accessible, immune-privileged)
           CNS: Still challenging; MiniCas9 + AAV or LNP in development
           Muscle: Some AAV serotypes (AAV8, AAV9) tropism

  CLINICAL EXAMPLE: CASGEVY (Vertex/CRISPR Therapeutics, 2023)
  ─ First approved CRISPR therapy (sickle cell + beta-thalassemia)
  ─ Ex vivo: Patient HSCs harvested → BCL11A enhancer disrupted
    (reactivates fetal hemoglobin) → cells infused back
  ─ Delivery: Electroporation of RNP (no viral vector)
```

---

## Base Editing

```
  BASE EDITING: CHEMICAL CONVERSION WITHOUT DSB
  ================================================

  PROBLEM WITH CAS9 CUTTING: DSBs can cause translocations,
  large deletions, and off-target edits.

  SOLUTION: Use catalytically dead Cas9 (dCas9) + deaminase enzyme
  to chemically convert one base to another WITHOUT cutting both strands.

  CBE (Cytosine Base Editor, David Liu lab):
  ┌────────────────────────────────────────────────────────────┐
  │ dCas9 + nicking + Cytosine Deaminase (APOBEC/AID)          │
  │ Converts: C → U → read as T after repair                   │
  │ Result: C:G → T:A base pair conversion                     │
  │ Editing window: positions 4–8 of gRNA (counting from PAM)  │
  └────────────────────────────────────────────────────────────┘

  ABE (Adenine Base Editor):
  ┌────────────────────────────────────────────────────────────┐
  │ dCas9 + evolved adenosine deaminase (ABE8e)                │
  │ Converts: A → I → read as G after repair                   │
  │ Result: A:T → G:C base pair conversion                     │
  │ Medically relevant: most pathogenic SNPs can be corrected  │
  │ with C→T or A→G conversion                                 │
  └────────────────────────────────────────────────────────────┘

  WHY BASE EDITING MATTERS:
  ─ ~60% of pathogenic point mutations correctable by ABE or CBE
  ─ Much lower indel rate than CRISPR cutting
  ─ Single-base precision: can correct one specific mutation
    without disturbing adjacent sequence

  LIMITATION: Only installs specific C→T or A→G changes.
  Can't: install arbitrary sequences, insert, delete, or
  make other transversion mutations.
```

---

## Prime Editing

```
  PRIME EDITING: THE MOST FLEXIBLE APPROACH (2019)
  ==================================================

  "Search-and-replace" genomic editing
  David Liu lab: pegRNA (prime editing guide RNA) + PE2/PE3/PE5

  MECHANISM:
  ┌────────────────────────────────────────────────────────────────┐
  │ pegRNA = gRNA + primer binding site (PBS) + reverse            │
  │          transcriptase template (RTT) encoding desired edit    │
  │                                                                │
  │ PE protein = Cas9 nickase (nicks one strand) +                 │
  │              M-MLV reverse transcriptase                       │
  │                                                                │
  │ PROCESS:                                                       │
  │ 1. pegRNA guides Cas9 to target; nicks PAM strand              │
  │ 2. 3' end of nicked strand hybridizes to PBS on pegRNA         │
  │ 3. RT uses RTT as template to copy desired edit                │
  │ 4. New DNA strand with edit replaces original                  │
  │ 5. PE3: second nick on opposite strand → promotes edit         │
  └────────────────────────────────────────────────────────────────┘

  CAPABILITIES (all four types of edit):
  C→T, A→G substitutions       (like base editors)
  All 12 types of point mutation (transversions included)
  Small insertions (≤44 bp)
  Small deletions (≤80 bp)
  Combinations of the above

  LIMITATION: Large insertions still challenging.
  ADVANTAGE: No DSB; works in non-dividing cells;
             installs nearly any small edit precisely.
```

---

## CRISPRi and CRISPRa

```
  CRISPR GENE REGULATION (WITHOUT EDITING)
  ==========================================

  CONCEPT: Use dCas9 (dead Cas9, no nuclease activity) as a
           programmable DNA-binding protein.
           Fuse transcription regulators to dCas9.
           Guide to any promoter → regulate that gene.

  CRISPRi (interference) — GENE SILENCING:
  ┌──────────────────────────────────────────────────────────┐
  │ dCas9–KRAB (Krüppel-associated box repressor domain)     │
  │ Target to gene promoter → block RNA Pol II               │
  │ + recruit H3K9me3 machinery → chromatin compaction       │
  │ Reversible: remove dCas9, gene re-activates              │
  │ Use: "soft knockdown" without permanent edit             │
  └──────────────────────────────────────────────────────────┘

  CRISPRa (activation) — GENE ACTIVATION:
  ┌──────────────────────────────────────────────────────────┐
  │ dCas9–VPR (VP64-p65-Rta activation domains)              │
  │ Or dCas9–SAM (synergistic activation mediator)           │
  │ Target to gene promoter → recruit transcription factors  │
  │ Result: 10–1,000-fold upregulation of target gene        │
  │ Use: Overexpress gene without additional copy insertion  │
  └──────────────────────────────────────────────────────────┘

  GENOME-SCALE SCREENS:
  ─ Library of 50,000–100,000 different gRNAs (5–10 per gene)
  ─ Lentiviral delivery: one gRNA per cell
  ─ Apply selection pressure (drug treatment, survival assay)
  ─ Read out: which gRNAs enriched or depleted?
  ─ Enriched = gene whose loss confers resistance
  ─ MAGeCK tool: statistical analysis of screen data
  ─ Result: genome-wide functional genetic map
```

---

## Off-Target Analysis

```
  OFF-TARGET EDITING: THE KEY SAFETY CONCERN
  ============================================

  A gRNA may bind imperfectly to other genomic locations:
  ─ Mismatches outside seed region (positions >10 from PAM)
  ─ Bulges (extra bases in gRNA or DNA)
  ─ If off-target site has NGG PAM → possible cut

  PREDICTION TOOLS:
  Cas-OFFinder: Enumerate all genomic sites with ≤N mismatches
  CRISPRscan/CHOPCHOP: Score gRNAs for on-target efficiency + off-target
  Rule set 2 / DeepCpf1: ML-based prediction

  EXPERIMENTAL VALIDATION:
  ┌─────────────────────────────────────────────────────────────────┐
  │ GUIDE-seq: Tag DSBs with oligo; sequence all cut sites          │
  │ CIRCLE-seq: In vitro Cas9 cut, circularize fragments; sequence  │
  │ DISCOVER-seq: Detect DSB repair marks (MRE11 ChIP-seq)          │
  │ Rhampseq: Deep sequencing at predicted off-target sites         │
  └─────────────────────────────────────────────────────────────────┘

  REDUCING OFF-TARGETS:
  ─ High-fidelity Cas9 variants: eSpCas9, HiFi Cas9 (fewer DSBs at mismatches)
  ─ Anti-CRISPR proteins: Turn off Cas9 after editing window
  ─ RNP delivery: Transient Cas9 → less exposure time
  ─ Truncated gRNAs: 17–18 nt instead of 20 nt → less off-target
  ─ Cas12a (Cpf1): Different PAM (TTTN), potentially fewer off-targets
  ─ Base/prime editing: No DSB → fewer chromosomal rearrangements
```

---

## Decision Cheat Sheet

| Goal | Approach |
|------|---------|
| Knock out a gene | SpCas9 + gRNA targeting coding exon |
| Correct a specific point mutation | ABE (A→G) or CBE (C→T) base editor |
| Install any small edit precisely | Prime editing (pegRNA + PE3) |
| Insert large sequence (>44 bp) | Cas9 HDR + ssODN/plasmid template |
| Silence gene without editing | CRISPRi (dCas9-KRAB) |
| Activate gene without editing | CRISPRa (dCas9-VPR) |
| Genome-scale functional screen | CRISPR KO library + MAGeCK |
| Edit cells for clinical use | RNP electroporation (ex vivo) |
| Deliver CRISPR to liver in vivo | LNP delivery (mRNA + gRNA) |
| Deliver CRISPR to muscle/CNS in vivo | AAV (miniCas9 or split Cas9) |
| Minimize off-target effects | HiFi Cas9 variant + GUIDE-seq validation |

---

## Common Confusion Points

**CRISPR vs. CRISPR-Cas9**: CRISPR (Clustered Regularly Interspaced Short Palindromic Repeats) is the bacterial immune system — the repeating DNA patterns. Cas9 is one protein that pairs with CRISPR sequences. There are many Cas proteins (Cas12a, Cas13, CasΦ, etc.) with different properties. "CRISPR" in popular usage means CRISPR-Cas9 editing.

**gRNA vs. sgRNA**: In the natural bacterial system, CRISPR uses two separate RNAs (crRNA + tracrRNA). In the lab, these were fused into a single guide RNA (sgRNA or just "guide RNA" / gRNA). The terms are used interchangeably in most literature.

**PAM is not part of the target sequence**: The PAM (NGG for SpCas9) is required for Cas9 binding but is not part of the sequence the guide RNA matches. The guide RNA matches the 20 nt immediately adjacent to (and upstream of) the PAM. The cut happens 3 bp into the protospacer (upstream of PAM).

**HDR requires cell division**: Homology-directed repair uses the S and G2 phases of the cell cycle when a sister chromatid is available as template. Non-dividing cells (neurons, cardiomyocytes) predominantly use NHEJ. This is why base editing and prime editing are important — they work in post-mitotic cells.

**Exon 1 knockout logic**: Not all indels cause frameshift. +3 bp or -3 bp = in-frame deletion (one amino acid deleted, rest preserved). To reliably knock out, target early exon, and verify that the distribution of indels predominantly includes frameshifts by deep sequencing (TIDE or ICE analysis).
