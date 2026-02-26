# Cancer

## The Big Picture: Hallmarks of Cancer

```
Hanahan & Weinberg (2000, updated 2011, 2022)
Ten Hallmarks + Two Enabling Characteristics:

CORE HALLMARKS:
  1. Sustaining proliferative signaling       (grow without external signals)
  2. Evading growth suppressors               (ignore stop signals)
  3. Resisting cell death                     (apoptosis resistance)
  4. Enabling replicative immortality         (telomerase, unlimited divisions)
  5. Inducing / accessing vasculature         (angiogenesis for O₂/nutrients)
  6. Activating invasion and metastasis       (escape primary tumor, colonize)
  7. Reprogramming cellular metabolism        (Warburg effect, nutrient capture)
  8. Evading immune destruction               (PD-L1, CTLA-4, immune exclusion)

ENABLING CHARACTERISTICS:
  9. Genome instability and mutation          (driver mutations accumulate)
  10. Tumor-promoting inflammation            (cytokines drive proliferation, angiogenesis)

Each hallmark = a specific cellular capability that must be acquired
Most require 2–8 "driver" mutations; passenger mutations are just noise
```

---

**Systems Bridge:** The oncogene/tumor-suppressor distinction maps directly to positive vs negative regulators in any control system. Oncogenes are accelerators: a gain-of-function mutation in a single allele is sufficient to drive proliferation — the mutant protein is constitutively active regardless of signal (RAS G12C stuck in GTP-bound "on" state; BCR-ABL kinase always firing). This is dominance in the genetic sense, and it parallels any positive-feedback component where a stuck-open valve or stuck-on transistor overrides normal regulation. Tumor suppressors are brakes: both alleles must be inactivated before the brake is fully released — the "two-hit" model (Knudson). This is the redundancy model: the system is designed with two independent inhibitory mechanisms, and both must fail before function is lost. Any critical safety system is engineered this way. The clinical consequence: oncogene mutations are targetable with single inhibitors (imatinib blocks BCR-ABL; the target is the constitutively active mutant). TSG loss is harder to drug directly — you can't "restore" a deleted gene pharmacologically — which is why TSG-loss strategies focus on synthetic lethality (exploit the dependency that arises from the loss rather than trying to replace the loss).

## Oncogenes

Proto-oncogene → oncogene by **gain-of-function** mutations (dominant — one mutant allele sufficient):

### Classes and Examples

```
GROWTH FACTOR RECEPTORS (RTKs — receptor tyrosine kinases):
  HER2/ERBB2: amplified in 20% breast cancer, 15% gastric
    → constitutively active ErbB2 → RAS-MAPK + PI3K-AKT → proliferation
    Drug: trastuzumab (Herceptin), pertuzumab (anti-HER2 mAbs), T-DM1
  EGFR: activating mutations (exon 19 del, L858R in NSCLC)
    Drug: erlotinib, osimertinib (3rd gen T790M resistant)
  ALK: EML4-ALK fusion in NSCLC (~5%)
    Drug: crizotinib, alectinib

SIGNAL TRANSDUCERS:
  RAS (KRAS, NRAS, HRAS): GTPase; mutations at codon 12/13/61 → "always on" GTP-bound state
    → cannot hydrolyze GTP → constitutive MAPK/ERK + PI3K/AKT signaling
    Mutated in ~30% all cancers: 90% pancreatic, 40% colon, 30% NSCLC
    KRAS G12C: now druggable — sotorasib, adagrasib (first KRAS inhibitors)
  BRAF V600E: constitutive RAF kinase → MAPK cascade
    Mutated in 60% melanoma, 40-50% papillary thyroid, 10% CRC (microsatellite stable → worse prognosis)
    Drug: vemurafenib, dabrafenib (BRAF inhibitors) + trametinib (MEK inhibitor)

TRANSCRIPTION FACTORS:
  MYC: amplified in many cancers; transcription factor driving proliferation, metabolism, ribosome biogenesis
    MYCN: amplified in neuroblastoma → poor prognosis
  (MYC currently undruggable directly — no pocket; targets downstream)

FUSION KINASES:
  BCR-ABL: t(9;22) Philadelphia chromosome → CML (chronic myeloid leukemia)
    Constitutively active ABL tyrosine kinase → proliferation + survival
    Drug: imatinib (Gleevec) — first rationally designed targeted therapy; dramatic efficacy; paradigm shift
    Subsequent: dasatinib, nilotinib, ponatinib (T315I resistant mutation)
  PML-RARA: t(15;17) → APML (AML-M3)
    Fusion blocks RAR-α → myeloid differentiation arrested at promyelocyte stage
    Drug: ATRA (all-trans retinoic acid) → differentiation therapy; arsenic trioxide
    APML has best prognosis of all AML subtypes when treated appropriately
```

---

## Tumor Suppressors

**Loss-of-function** — both alleles must be inactivated (recessive; Knudson's two-hit hypothesis):

### Two-Hit Hypothesis

```
HEREDITARY CANCER SYNDROMES:
  Germline hit #1 (inherited) + somatic hit #2 (acquired) → tumor
  Loss of heterozygosity (LOH): second hit by deletion, loss of chromosome, mutation

SPORADIC:
  Both hits somatic → less likely per cell → later onset, often single tumor

Knudson studied retinoblastoma:
  Hereditary: ~bilateral, earlier onset (< 5 years)
  Sporadic: unilateral, later onset
  Conclusion: inherited form starts with 1 hit → just needs 1 more
```

### Key Tumor Suppressors

```
RB1 (Retinoblastoma protein):
  G1/S checkpoint gatekeeper: Rb binds + inactivates E2F (transcription factor for S-phase genes)
  CDK4/6-cyclin D phosphorylates Rb → E2F released → S-phase entry
  Loss of Rb: uncontrolled S-phase → retinoblastoma, osteosarcoma, SCLC
  HPV E7 binds Rb → degrades it → cervical cancer
  CDK4/6 inhibitors (palbociclib, ribociclib): restore Rb braking → breast cancer treatment

TP53 (p53 — "guardian of the genome"):
  Mutated in ~50% of all human cancers (most commonly mutated gene in cancer)
  Functions: G1 arrest (p21 → CDK inhibitor), apoptosis (BAX upregulation), DNA repair, senescence
  Activated by: DNA damage, oncogene signaling, hypoxia
  MDM2: E3 ubiquitin ligase → ubiquitinates p53 → proteasomal degradation (feedback inhibitor)
    MDM2 inhibitors: nutlin-3, AMG-232 — restore p53 in MDM2-amplified tumors (liposarcoma)
  Li-Fraumeni syndrome: germline TP53 mutation → multiple early-onset cancers

BRCA1/BRCA2:
  DNA repair: homologous recombination (HR) of double-strand breaks
  BRCA1: also checkpoint signaling, transcription regulation
  Germline mutation (BRCA1 or BRCA2):
    BRCA1: breast 60-80%, ovarian 40%, other (pancreatic, prostate)
    BRCA2: breast 45-85%, ovarian 15-20%, pancreatic 5%, prostate
  SYNTHETIC LETHALITY: BRCA1/2 mutant tumors rely on PARP (base excision repair)
    PARP inhibitors (olaparib, rucaparib, niraparib): kill BRCA-mutant cells specifically
    → Approved for BRCA+ breast, ovarian, pancreatic, prostate cancer

APC (Adenomatous Polyposis Coli):
  Wnt pathway: normally APC in destruction complex → phosphorylates β-catenin → ubiquitination
  Loss of APC → β-catenin accumulates → nucleus → TCF/LEF transcription → MYC, Cyclin D1
  Familial Adenomatous Polyposis (FAP): germline APC → hundreds of colonic polyps → CRC certain if untreated
  APC mutation is earliest genetic event in sporadic CRC (Fearon-Vogelstein model)

VHL (von Hippel-Lindau):
  Normally: VHL → targets HIF-1α for ubiquitination in normoxia
  Loss of VHL → HIF-1α stabilized even in normoxia → VEGF, PDGF, EPO overexpression
  → Clear cell renal cell carcinoma (VHL deleted in ~90%)
  → VHL syndrome: bilateral RCC, hemangioblastoma, pheochromocytoma
  Drugs: HIF-2α inhibitors (belzutifan) — new targeted approach
```

---

## Cell Cycle Checkpoints and Cancer

```
                G1          S           G2          M
  ─────────────────────────────────────────────────────────
  Checkpoints:  G1/S ←    ─→  Intra-S   G2/M      Spindle assembly
                (Rb/p53)       checkpoint checkpoint  (SAC)

G1/S CHECKPOINT (most relevant to cancer):
  Restriction point: past here, cell commits to division regardless of mitogen withdrawal
  Rb: hypophosphorylated (active) → binds E2F → S-phase OFF
  Cyclin D-CDK4/6 + Cyclin E-CDK2: phosphorylate Rb → release E2F
  p21 (CIP1): CDK inhibitor induced by p53 → prevents Rb phosphorylation → arrest

G2/M CHECKPOINT:
  CHK1/CHK2 (activated by ATM/ATR on DNA damage) → phosphorylate CDC25C → sequester it → CDK1 inactive → no mitosis
  ATM/ATR inhibitors being developed as cancer therapeutics

SPINDLE ASSEMBLY CHECKPOINT (SAC):
  BubR1, Mad2: sequester CDC20-APC/C until all kinetochores attached → prevents premature chromatid separation
  Chromosome instability (CIN) in cancer: SAC failure → aneuploidy → rapid evolution
  Taxanes (paclitaxel): stabilize microtubules → SAC activation → mitotic arrest → apoptosis
  Vinca alkaloids (vincristine): depolymerize microtubules → SAC activation
```

---

## DNA Repair Pathways and Cancer

```
BER (Base Excision Repair): single-base damage (oxidation, alkylation)
  PARP1 recruits repair machinery; PARP inhibitors exploit BRCA deficiency

NER (Nucleotide Excision Repair): bulky adducts (UV-induced pyrimidine dimers)
  XP (Xeroderma Pigmentosum): NER deficiency → extreme UV sensitivity → skin cancer

MMR (Mismatch Repair): replication errors (insertions/deletions at microsatellites)
  MSH2, MLH1, MSH6, PMS2 — heterodimers scan newly replicated DNA
  Loss of MMR → MICROSATELLITE INSTABILITY (MSI-High): repetitive sequences mutate
  Lynch syndrome: germline MMR gene mutation → CRC, endometrial, ovarian, gastric cancer
  MSI-H tumors: hypermutated → high neoantigen load → excellent response to PD-1 inhibitors

HR (Homologous Recombination): DSB (double-strand breaks) in S/G2
  BRCA1/2, RAD51, PALB2: strand invasion/template repair
  HR deficiency → rely on NHEJ (error-prone) → chromosomal instability

NHEJ (Non-Homologous End Joining): error-prone DSB repair
  Ku70/80, DNA-PKcs: rejoin broken ends without template
  Active in G1 (no sister chromatid); translocations can occur → oncogenic fusions
```

---

## Epigenetics in Cancer

```
DNA METHYLATION:
  CpG methylation (DNMT enzymes) → gene silencing
  Cancer: CpG ISLAND HYPERMETHYLATION of promoters → TSG silencing
  e.g., MLH1 (promoter methylation → sporadic MSI-H CRC), p16 (CDKN2A), BRCA1 (some tumors)
  Also: global hypomethylation → reactivate transposons, ↑ genomic instability

HISTONE MODIFICATIONS:
  Acetyltransferases (HATs): add acetyl → open chromatin → transcription
  Deacetylases (HDACs): remove acetyl → closed chromatin → silencing
  HDAC inhibitors (vorinostat, romidepsin): approved for CTCL, PTCL
  PRC2 (EZH2): H3K27 methyltransferase → gene silencing
  EZH2 inhibitors (tazemetostat): follicular lymphoma, EZH2 gain-of-function mutations

ONCOFUSION TRANSCRIPTION FACTORS:
  PML-RARA: blocks myeloid differentiation (APML)
  EWS-FLI1: Ewing sarcoma — drives oncogenic transcription program
  SS18-SSX: synovial sarcoma
```

---

## Metastasis Cascade

```
1. LOCAL INVASION:
   Loss of E-cadherin (cell-cell adhesion): allows detachment
   MMP (matrix metalloproteinases) secretion: degrade basement membrane + ECM
   EPITHELIAL-MESENCHYMAL TRANSITION (EMT):
     Epithelial markers (E-cad, CK) → Mesenchymal (N-cad, vimentin, fibronectin)
     TGF-β, Wnt, Notch, Snail/Slug/Twist transcription factors drive EMT
     EMT increases motility, invasion, stem-like properties, therapy resistance

2. INTRAVASATION: enter blood or lymphatics
   Tumor cells travel as CTCs (circulating tumor cells) — shed by millions/day
   Most die (anoikis, shear forces, NK killing); < 0.01% form metastases

3. SURVIVAL IN CIRCULATION:
   CTCs can aggregate with platelets → evade NK cells (platelets shield)
   CTCs can aggregate with WBCs (neutrophils) → enhanced metastatic potential

4. ARREST AND EXTRAVASATION:
   Physical trapping in small capillaries or receptor-mediated adhesion
   Extravasation: reverse of intravasation; MMP-mediated

5. COLONIZATION (rate-limiting step):
   Metastatic niche: pre-metastatic niche prepared by tumor-derived exosomes, VEGF, LOX
   Dormancy: micrometastases can remain dormant years before outgrowth
   Organotropism: "seed and soil" (Paget 1889) — specific tumor types prefer specific organs:
     Breast → bone (SDF-1/CXCL12 axis), lung, liver, brain
     Prostate → bone (osteoblastic metastases — unique)
     Colon → liver (portal blood drainage)
     Melanoma → liver, lung, brain, everywhere
     Lung → adrenal, bone, brain, liver
```

---

## Tumor Staging: TNM System

```
T — Primary Tumor
  Tis: carcinoma in situ (no invasion through basement membrane)
  T1-T4: increasing size and/or depth of invasion (varies by cancer type)

N — Regional Lymph Node involvement
  N0: no regional node metastasis
  N1-N3: increasing number/extent of nodal involvement

M — Distant Metastasis
  M0: no distant metastasis
  M1: distant metastasis present (may be subdivided M1a/b/c)

STAGE GROUPING (combines T, N, M → Stage I-IV):
  Stage I-II: localized (better prognosis)
  Stage III: locally advanced / regional nodes
  Stage IV: distant metastasis (worst prognosis, usually systemic treatment)

CANCER GRADING (separate from staging):
  Grade 1: well-differentiated (resembles normal tissue, slower)
  Grade 2: moderately differentiated
  Grade 3: poorly differentiated
  Grade 4: undifferentiated/anaplastic (no resemblance to origin, aggressive)
```

---

## Cancer Epidemiology and Screening

```
MOST COMMON CANCERS (Global, 2020):
  Incidence: breast > lung > colorectal > prostate > stomach > liver > cervical
  Mortality: lung > colorectal > liver > stomach > breast

USA:
  Incidence ♂: prostate > lung > colorectal > bladder > melanoma
  Incidence ♀: breast > lung > colorectal > uterine > melanoma
  Mortality ♂: lung >> prostate > colorectal > pancreatic > liver
  Mortality ♀: lung >> breast > colorectal > pancreatic > ovarian

SCREENING PRINCIPLES:
  Wilson-Jungner criteria (1968) — still valid:
  1. Important health problem with known natural history
  2. Detectable preclinical stage
  3. Effective treatment at early stage
  4. Suitable test (sensitive/specific/acceptable)
  5. Diagnosis and treatment infrastructure available
  6. Cost-effective

PROVEN SCREENING (survival benefit shown):
  Cervical: Pap smear (cytology) + HPV test
  Breast: mammography (guidelines vary: 40-50 start, controversy)
  Colorectal: colonoscopy (gold standard), FIT test, stool DNA (Cologuard), CT colonography
  Lung: low-dose CT in high-risk smokers (USPSTF: 50-80 yo, 20 pack-year, currently smoking or quit < 15 yr)
  Prostate: PSA (shared decision-making 55-69 — high false positive rate)
```

---

## Liquid Biopsy

```
ctDNA (circulating tumor DNA): fragmented DNA from apoptotic/necrotic tumor cells
  In blood plasma (cell-free DNA fraction)
  Detection: ultra-sensitive sequencing (ddPCR, next-gen deep sequencing)
  Applications:
    Mutation detection: KRAS, EGFR, BRAF etc. in plasma (if tissue biopsy inaccessible)
    Minimal residual disease (MRD) detection: post-treatment ctDNA → recurrence prediction
    Treatment response monitoring: ctDNA fraction falls with response
    Resistance mutation detection: T790M (EGFR) emerges in liquid biopsy before clinical progression
  Multi-cancer early detection (MCED) tests (Galleri, etc.):
    Methylation patterns in cfDNA → cancer signal + tissue of origin prediction
    Still in validation; potential for population screening

CTCs (circulating tumor cells): intact tumor cells shed into blood
  EpCAM capture (CellSearch): FDA-approved for prognosis in metastatic breast/colorectal/prostate
  Single-cell sequencing from CTCs: heterogeneity analysis

Tumor-educated platelets (TEPs), exosomes: also explored as biomarkers
```

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| Why are TSGs recessive but oncogenes dominant? | TSGs: need to lose both functional copies (two hits). Oncogenes: one gain-of-function allele sufficient to drive proliferation. |
| BRCA1/2 mutation → what targeted therapy? | PARP inhibitors (olaparib, niraparib): exploit synthetic lethality — BRCA-deficient cells can't repair DSBs without HR + PARP inhibited. |
| What does BCR-ABL fusion do? | Constitutively active ABL tyrosine kinase (no regulatory domain) → continuous cell proliferation + survival → CML |
| MSI-H tumors respond well to what? | PD-1 / PD-L1 checkpoint inhibitors (pembrolizumab) — hypermutated → high neoantigens → T cell response when brakes released |
| Warburg effect: why do tumor cells use glycolysis even with O₂? | Speed and biosynthetic precursors: aerobic glycolysis (pyruvate → lactate) is wasteful for ATP but supplies carbon for nucleotides, lipids, amino acids faster; also acidifies microenvironment |
| What predisposes to chromosomal translocations? | NHEJ (error-prone DSB repair) misligates two broken ends from different chromosomes; radiation, topoisomerase inhibitors, DNA-damaging agents |

---

## Common Confusion Points

**Tumor vs cancer vs neoplasm vs malignancy**
- Neoplasm: any new abnormal growth (benign or malignant)
- Tumor: any mass ("swelling") — benign or malignant
- Cancer: malignant neoplasm specifically (invades, metastasizes)
- Malignant ≠ "will kill you" — grade/stage/treatment matter enormously

**Driver vs passenger mutations**
Driver: confers growth advantage (selected for). Passenger: neutral bystander (just accumulated). Most tumors have 2–8 drivers in ~30,000 coding mutations. Distinguishing driver vs passenger is a core bioinformatics problem (COSMIC, OncoKB, IntOGen databases).

**Clonal evolution is Darwinian, not teleological**
Cancers don't "decide" to become resistant or more aggressive. Resistant subclones are present at low frequency before treatment; therapy kills sensitive clones → resistant ones expand. Treatment resistance is evolutionary inevitability, slowed by combination therapy that raises mutation-combination barrier.

**Metastasis kills, not the primary tumor**
~90% of cancer mortality is from metastatic disease, not the primary. The primary tumor itself is usually surgically resectable if localized. Understanding and preventing metastasis is the key unmet need.
