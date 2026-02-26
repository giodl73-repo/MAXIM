# Cancer Pharmacology and Chemotherapy

## The Big Picture

Cancer pharmacology kills tumor cells by exploiting differences between tumor and normal cells — a progressively smaller differential the more targeted the therapy. Traditional chemotherapy exploits rapid proliferation; targeted therapy exploits specific oncogenic mutations; immunotherapy activates the immune system.

```
+──────────────────────────────────────────────────────────────────+
|              CANCER PHARMACOLOGY LANDSCAPE                       |
|                                                                  |
|  GENERATION 1: Traditional Chemotherapy (1950s–1980s)           |
|  • Targets rapidly dividing cells (all of them, not just tumor) |
|  • High toxicity to bone marrow, GI tract, hair                 |
|  • Alkylating agents, antimetabolites, topoisomerase inhibitors  |
|                                                                  |
|  GENERATION 2: Targeted Therapy (1990s–present)                  |
|  • Targets specific oncogenic protein (kinase, EGFR, HER2, etc.) |
|  • Requires biomarker selection (tumor genotyping)               |
|  • Small molecules (-ibs) and monoclonal antibodies (-mabs)      |
|                                                                  |
|  GENERATION 3: Immunotherapy (2010s–present)                     |
|  • Activates or redirects immune system against tumor           |
|  • Checkpoint inhibitors (PD-1/PD-L1, CTLA-4)                   |
|  • CAR-T cells, bispecific antibodies                            |
|                                                                  |
|  SELECT PATIENT → MATCH MECHANISM → MANAGE RESISTANCE           |
+──────────────────────────────────────────────────────────────────+
```

---

## Cell Cycle and Chemotherapy Targets

```
CELL CYCLE PHASES AND DRUG TARGETS
────────────────────────────────────
                         M (mitosis)
                       ╱           ╲
                    G2               G1
                  ╱                    ╲
              S (DNA synthesis)         G0 (quiescent)

  G1 → S:  Checkpoint; CDK4/6 + cyclin D (target: palbociclib)
  S phase: DNA replication (target: antimetabolites, hydroxyurea)
  G2 → M: Checkpoint; CDK1 + cyclin B
  M phase: Mitosis; spindle formation (target: vinca alkaloids, taxanes)

CELL CYCLE-SPECIFIC DRUGS (only work in specific phase)
  S-phase:  Antimetabolites (5-FU, methotrexate, cytarabine)
  M-phase:  Taxanes (paclitaxel), vinca alkaloids (vincristine)
  G1/S:     CDK4/6 inhibitors (palbociclib, ribociclib)

CELL CYCLE NON-SPECIFIC (work in any phase)
  Alkylating agents (cyclophosphamide, cisplatin)
  Anthracyclines (doxorubicin)
  Bleomycin (G2 arrest; lung toxicity)
  Nitrosoureas (carmustine — crosses BBB)
```

---

## Traditional Chemotherapy Classes

```
ALKYLATING AGENTS
──────────────────
Mechanism: Form covalent crosslinks in DNA (inter- and intrastrand).
           DNA cannot replicate or transcribe. Apoptosis triggered.
           Also crosslink RNA and proteins.

Classes:
  Nitrogen mustards:  Cyclophosphamide, ifosfamide, mechlorethamine
                      (prodrugs activated by CYP2B6 in liver)
  Platinum compounds: Cisplatin, carboplatin, oxaliplatin
                      Form DNA adducts; cisplatin → renal + neuro toxicity
  Nitrosoureas:       Carmustine (BCNU), lomustine — cross BBB; used in CNS tumors
  Alkyl sulfonates:   Busulfan — myeloablation in stem cell transplant prep
  Triazines:          Temozolomide — oral; methylates DNA; glioblastoma (MGMT unmethylated = resistant)

TOXICITIES
  HEMORRHAGIC CYSTITIS: Cyclophosphamide/ifosfamide → acrolein metabolite → bladder
                         Prevent with MESNA (thiol trapping agent) + hydration
  NEPHROTOXICITY: Cisplatin → proximal tubule damage → amifostine protection
  NEUROTOXICITY: Cisplatin → peripheral neuropathy, ototoxicity (irreversible)
  CARBOPLATIN: Dose formula uses GFR (Calvert formula): dose = AUC × (GFR + 25)
               Primarily myelosuppression; less neuro/renal than cisplatin

ANTIMETABOLITES
────────────────
Mechanism: Structural analogs of nucleotides/precursors → disrupt DNA synthesis.

  ANTIFOLATES
  Methotrexate: Inhibits DHFR → ↓tetrahydrofolate → ↓purine + thymidylate synthesis
    High-dose: CNS; requires leucovorin (folinic acid) rescue
    Intrathecal: CNS prophylaxis in leukemia
    Toxicity: myelosuppression, mucositis, nephrotoxicity

  PYRIMIDINE ANALOGS
  5-Fluorouracil (5-FU): Prodrug → FdUMP → inhibits thymidylate synthase
    Colon cancer (FOLFOX: 5-FU + leucovorin + oxaliplatin)
    Leucovorin enhances 5-FU binding to thymidylate synthase
    Capecitabine: oral 5-FU prodrug (activated in tumor by thymidine phosphorylase)
    Cytarabine (Ara-C): incorporated into DNA → chain termination → AML

  PURINE ANALOGS
  6-Mercaptopurine (6-MP): Metabolized by TPMT (pharmacogenomics!)
  Fludarabine: B-cell malignancies (CLL)

TOPOISOMERASE INHIBITORS
─────────────────────────
  Topo I inhibitors:  Irinotecan (CPT-11), topotecan
    Form stable Top-I:DNA complex → strand breaks → apoptosis
    SN-38 (active metabolite of irinotecan) via carboxylesterase
    UGT1A1 inactivates SN-38 (pharmacogenomics: *28 variant → toxicity)

  Topo II inhibitors: Etoposide, anthracyclines (intercalate + Top-II)
    Doxorubicin: Most widely used anthracycline; breast, lymphoma, sarcoma
    Cumulative cardiotoxicity (cardiomyopathy) → dose limit ~450-500 mg/m²
    Dexrazoxane: iron chelator; reduces cardiotoxicity if needed beyond limit

MITOTIC INHIBITORS
───────────────────
  Taxanes: Paclitaxel (Taxol), docetaxel
    Hyperstabilize microtubules → cannot depolymerize → mitosis arrest
    Hypersensitivity reactions (paclitaxel cremophor vehicle)
    Nab-paclitaxel: albumin-bound nanoparticle → no Cremophor needed
    Neuropathy (dose-limiting), alopecia, myelosuppression

  Vinca alkaloids: Vincristine, vinblastine, vinorelbine
    PREVENT tubulin polymerization → spindle cannot form
    Vincristine: peripheral neuropathy (dose-limiting); minimal myelosuppression
                 Used in ALL, lymphoma
    Vinblastine: myelosuppression dominant; testicular cancer (BEP regimen)
```

---

## Targeted Therapy

```
KINASE INHIBITORS (small molecules, -tinib/-nib suffix)
─────────────────────────────────────────────────────────
  TARGET              DRUG                  INDICATION
  ─────────────────── ──────────────────── ──────────────────────────
  BCR-ABL             Imatinib (Gleevec)    CML, Ph+ ALL
                      Dasatinib, nilotinib  Imatinib resistance
  EGFR (mutant)       Erlotinib, gefitinib  NSCLC (EGFR mut)
                      Osimertinib           T790M resistance mutation
  HER2                Neratinib, tucatinib  HER2+ breast cancer
  BRAF V600E          Vemurafenib, dabrafenib Melanoma BRAF V600E
  MEK (+ BRAF combo)  Trametinib, cobimetinib Melanoma (resistance prevention)
  ALK fusion          Crizotinib, alectinib  NSCLC ALK+
  CDK4/6              Palbociclib, ribociclib HR+ HER2- breast cancer (+ AI)
  PI3K/mTOR           Alpelisib, everolimus  PIK3CA mut, HR+ breast/renal
  BTK                 Ibrutinib, acalabrutinib CLL, MCL, Waldenström

IMATINIB: THE PARADIGM SHIFT
  BCR-ABL: fusion oncogene from t(9;22) → Philadelphia chromosome
  Constitutively active tyrosine kinase → uncontrolled proliferation
  Imatinib: ATP-competitive BCR-ABL inhibitor
  CML: ~90% complete cytogenetic response (from median survival ~5 yr → near normal)
  Mechanism of resistance: BCR-ABL T315I "gatekeeper" mutation → ponatinib needed

MONOCLONAL ANTIBODIES (-mab suffix)
  Trastuzumab (Herceptin): HER2+ breast cancer; ADCC + inhibits HER2 signaling
  Bevacizumab (Avastin): anti-VEGF; anti-angiogenic; colorectal, lung, ovarian
  Cetuximab (Erbitux): anti-EGFR; colorectal cancer (only if KRAS/NRAS wild-type)
  Rituximab (Rituxan): anti-CD20; B-cell lymphoma, CLL, autoimmune diseases
  ADCs (antibody-drug conjugates): antibody delivers cytotoxin to tumor
    Ado-trastuzumab emtansine (T-DM1): HER2 + emtansine (maytansinoid)
    Sacituzumab govitecan: TROP-2 + SN-38 (topoisomerase inhibitor)
```

---

## Immunotherapy

```
CHECKPOINT INHIBITORS
──────────────────────
T cells are activated by TCR-antigen + costimulatory signals.
Checkpoint proteins turn T cells off (physiologic immune suppression).
Tumors exploit checkpoints to evade immune destruction.

  CHECKPOINT    INHIBITOR CLASS        APPROVED DRUGS
  ────────────  ────────────────────   ─────────────────────────────────
  PD-1          Anti-PD-1              Nivolumab, pembrolizumab, cemiplimab
  PD-L1         Anti-PD-L1             Atezolizumab, durvalumab, avelumab
  CTLA-4        Anti-CTLA-4            Ipilimumab

  PD-1/PD-L1 AXIS
    Tumor cells overexpress PD-L1 → binds T cell PD-1 → T cell suppressed.
    Anti-PD-1 or anti-PD-L1 antibodies block this → T cells attack tumor.
    Works in: NSCLC, melanoma, urothelial, renal, HCC, MSI-high tumors

  CTLA-4
    Expressed on T cells; binds B7 on APCs → T cell non-activation.
    Ipilimumab blocks CTLA-4 → ↑T cell priming in lymph nodes.
    Mostly melanoma; higher toxicity than anti-PD-1.

  IRRELATED ADVERSE EVENTS (irAE): Immune-mediated inflammation of ANY organ
    Colitis, pneumonitis, hepatitis, endocrinopathy (thyroid, adrenal, pituitary)
    Treatment: high-dose corticosteroids (not tumor suppressing); hold checkpoint drug

PREDICTIVE BIOMARKERS
  PD-L1 expression (IHC): predicts response to anti-PD-1 in some tumors
  MSI-H / dMMR: Hypermutated tumors → more neoantigens → excellent response
  TMB (tumor mutational burden): High → more neoantigens → better response

CAR-T CELLS
  Patient's T cells extracted, genetically engineered to express Chimeric Antigen Receptor.
  CAR targets tumor antigen (CD19 for B-cell, BCMA for myeloma).
  T cells infused → attack tumor.
  Approved for: B-ALL, DLBCL, multiple myeloma
  Toxicity: CRS (cytokine release syndrome) → high fever, hypotension, organ failure
            Treated with tocilizumab (IL-6 receptor antagonist)
            Neurotoxicity (ICANS)
```

---

## Bispecific Antibodies

```
BISPECIFIC ANTIBODIES (BiTEs AND RELATED)
──────────────────────────────────────────
  Concept: One antibody with TWO binding specificities.
  One arm binds tumor antigen; other arm binds CD3 (T cells) or NK cell receptor.
  → Physical proximity forces immune effector cell to engage and kill tumor cell.
  → No need for antigen presentation; bypasses major tumor immune escape mechanisms.

  BiTE (Bispecific T cell Engager) FORMAT:
    Single-chain, very short half-life → continuous infusion initially
    Half-life extended formats now available (blinatumomab → amivantamab)

  KEY APPROVED AGENTS:
    Blinatumomab (Blincyto): CD19×CD3 BiTE → ALL (B-cell), Ph-negative r/r
      First approved BiTE. Impressive responses in refractory ALL.
      Neurotoxicity and CRS are dose-limiting.

    Teclistamab (Tecvayli): BCMA×CD3 → multiple myeloma (r/r, post 4 prior lines)
      First anti-BCMA BiTE. Deep responses in heavily pretreated patients.
      Infections (esp. serious bacterial/viral) a major concern with T-cell activation.

    Talquetamab (Talvey): GPRC5D×CD3 → multiple myeloma
      Non-BCMA target; important for post-BCMA resistance.
      Nail/skin/taste side effects (GPRC5D expressed in stratified epithelium).

    Mosunetuzumab (Lunsumio): CD20×CD3 → follicular lymphoma (r/r)
      Fixed-duration (SC, subcutaneous): 8 cycles. Low-grade CRS; high CR rates.

    Epcoritamab (Epkinly): CD20×CD3 → DLBCL, follicular lymphoma

  BiTE vs CAR-T COMPARISON:
    BiTEs:   Off-the-shelf, immediate use, no manufacturing lag
             Re-dosable, adjustable (infusion rate ↔ toxicity)
             Lower persistence than CAR-T → maintenance needed
    CAR-T:   Durable remission, one-time infusion
             Manufacturing time: 4-6 weeks; costly; specialized centers
             Higher toxicity ceiling (CRS, ICANS)
             Primary resistance: antigen loss, poor T-cell fitness
```

---

## Engineering Bridge: Resistance as Evolutionary Selection

Drug resistance is Darwinian selection applied to a tumor cell population under treatment pressure. The strategies are directly analogous to adversarial robustness in security engineering.

```
  ONCOLOGY RESISTANCE           SECURITY / SYSTEMS PARALLEL
  ──────────────────────────────────────────────────────────────────────
  Pre-existing resistant clones Heterogeneous population with rare
  (Darwinian selection)         pre-existing variants. Treatment = adversarial
                                selection pressure. Resistant clone outcompetes
                                sensitive cells. "Selection, not induction."
                                Exactly: existing zero-day vulnerabilities
                                selected by a specific patch (treatment).

  Combination therapy rationale Defense-in-depth:
  (attack multiple pathways)    P(resistance to A AND B) = P(A) × P(B)
                                if mechanisms are independent. With
                                simultaneous targeting of BCR-ABL + MDM2,
                                simultaneous resistance requires two
                                independent mutations → much lower probability.
                                Same logic as requiring two independent
                                system failures for an outage.

  Acquired target mutation      Exploit evolves past the patch:
  (BCR-ABL T315I, EGFR T790M)  The drug defines the selection pressure;
                                the resistance mutation is the evolved counter.
                                Each generation of targeted therapy is an
                                exploit-patch cycle: imatinib → T315I →
                                ponatinib (third-gen, covers T315I).

  ctDNA monitoring for          Real-time adversarial monitoring:
  resistance mutations          Liquid biopsy tracks the emerging resistant
                                subclone in real time — analogous to
                                continuous security monitoring for novel
                                attack signatures before full outbreak.

  MDR1 / P-glycoprotein         Transport-layer evasion: tumor cells
  (drug efflux pump)            overexpress efflux pumps to exclude the drug.
                                Analogous to egress filtering in a network:
                                the target machine actively ejects the payload.
  ──────────────────────────────────────────────────────────────────────
```

---

## Drug Resistance

```
MECHANISMS OF DRUG RESISTANCE
────────────────────────────────
  PHARMACOKINETIC RESISTANCE
  • ↑P-glycoprotein (MDR1): Pumps drug out of cells
  • ↓Drug uptake transporters: Less drug enters
  • ↑Drug metabolism: Faster inactivation

  PHARMACODYNAMIC RESISTANCE
  • Target mutation: BCR-ABL T315I, EGFR T790M, BRAF→MEK
  • Target amplification: Too much target to inhibit
  • Alternative pathway activation: bypass the blocked target
    KRAS wild-type required for EGFR inhibitor → KRAS mutation = resistance
  • Antiapoptotic upregulation: BCL-2 → venetoclax target

  TUMOR HETEROGENEITY
  • Pre-existing resistant clones selected by therapy
  • Darwinian evolution under drug pressure
  • Liquid biopsies: ctDNA tracks resistance mutations in real time

COMBINATION THERAPY RATIONALE
  1. Overcome resistance mechanisms (attack multiple pathways)
  2. Dose reduction (toxicity of each drug at lower dose)
  3. Synergy: different mechanisms enhance each other
  4. Cell cycle coverage (S-phase + M-phase agents together)

  BEP regimen (testicular cancer):
    Bleomycin (G2) + Etoposide (Topo II) + Cisplatin (alkylating)
    90%+ cure rate for disseminated non-seminoma — chemotherapy's best result
```

---

## Decision Cheat Sheet

| Cancer Type | Mechanism to Check | Targeted Drug |
|-------------|-------------------|---------------|
| CML | BCR-ABL / Ph chromosome | Imatinib → dasatinib if resistant |
| NSCLC | EGFR mut? ALK fusion? KRAS G12C? | Osimertinib, alectinib, sotorasib |
| Melanoma | BRAF V600E? | Dabrafenib + trametinib |
| Breast | HER2+? HR+? BRCA? | Trastuzumab, palbociclib, olaparib |
| Colorectal | KRAS/NRAS/BRAF status? MSI? | Cetuximab only if WT-KRAS; pembrolizumab if MSI-H |
| B-cell ALL | CD19 | CAR-T (tisagenlecleucel) |
| CLL | BTK pathway | Ibrutinib, acalabrutinib, venetoclax |
| Any solid tumor | MSI-H? High TMB? | Pembrolizumab |
| Chemo-induced nausea | 5-HT3 + NK1 + dex | Ondansetron + aprepitant + dexamethasone |

---

## Common Confusion Points

**"Targeted therapy doesn't have side effects — unlike chemo"**
False. Targeted therapy has a different side effect profile, not an absent one. EGFR inhibitors: acneiform rash (paradoxically correlates with response), diarrhea, paronychia. BCR-ABL inhibitors: pleural effusion, QT prolongation, hepatotoxicity. BRAF inhibitors: secondary squamous cell carcinomas (paradoxical MAPK pathway activation in WT-BRAF cells). Checkpoint inhibitors: immune-mediated adverse events in any organ.

**"The tumor must have the biomarker for targeted therapy to work"**
Mostly true but not universally. KRAS wild-type is required for EGFR antibody benefit in colorectal cancer — KRAS mutation = primary resistance. But HER2 status in breast cancer: HER2+ responds dramatically to trastuzumab; HER2-low (1+ IHC) can respond to ADCs (T-DXd). The biomarker-therapy relationship is being refined continuously with newer drugs.

**"Platinum regimens are the same — cisplatin, carboplatin, oxaliplatin"**
They all form DNA adducts but with distinct profiles. Cisplatin: renal + ototoxicity + severe nausea. Carboplatin: dose by GFR (Calvert formula); myelosuppression dominant; less nausea. Oxaliplatin: cold-induced peripheral neuropathy (acute); cumulative sensory neuropathy (chronic); used in GI cancers. Not interchangeable in all settings.
