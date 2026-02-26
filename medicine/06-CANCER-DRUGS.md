# 06 — Cancer Drugs

## Cytotoxics, Targeted Therapy (Kinase Inhibitors, mAbs), Immunotherapy, ADCs, Hormone Therapy

---

**Systems Bridge:** Targeted oncology therapy exploits two related architectural vulnerabilities. Oncogene addiction is a SPOF (single point of failure) problem: a cancer cell that has amplified or constitutively activated a single oncogenic pathway becomes dependent on that pathway for survival — it has traded pathway redundancy for proliferative gain. When you inhibit that pathway (imatinib → BCR-ABL; trastuzumab → HER2; erlotinib → mutant EGFR), the cell has no fallback. Normal cells have parallel signaling pathways and tolerate the loss of one; the addicted cancer cell cannot. Synthetic lethality is the redundancy analysis version: if two repair pathways (BRCA homologous recombination + PARP base excision repair) are both individually essential for survival under DNA damage, and you knock out one (BRCA mutation in the tumor), then the other becomes the sole critical path. Inhibit the sole remaining path (PARP inhibitor) → the system crashes — but only in the BRCA-mutant cell, not in normal cells that still have both pathways. This is exactly the logic of fault injection against a system that has one redundancy layer already removed: inject a fault in the remaining path → failure. The precision of targeted therapy relative to cytotoxic chemotherapy comes from this architectural specificity: cytotoxics kill all dividing cells (low specificity); targeted drugs kill only cells with the specific vulnerability.

## Big Picture: Oncology Drug Landscape

```
┌──────────────────────────────────────────────────────────────────────────┐
│                   CANCER DRUG MECHANISMS                                 │
├─────────────────────┬────────────────────────────────────────────────────┤
│ CYTOTOXIC           │ DNA damage (alkylating, platinum, topo inhibitors) │
│ CHEMOTHERAPY        │ Antimetabolites (S-phase specific)                  │
│                     │ Microtubule poisons (mitosis block)                 │
├─────────────────────┼────────────────────────────────────────────────────┤
│ TARGETED THERAPY    │ Small molecule kinase inhibitors (-nibs)            │
│                     │ Monoclonal antibodies (-mabs)                       │
│                     │ PARP inhibitors (synthetic lethality)               │
│                     │ BCL-2 inhibitors (apoptosis restoration)            │
│                     │ CDK inhibitors (cell cycle)                         │
├─────────────────────┼────────────────────────────────────────────────────┤
│ IMMUNOTHERAPY       │ Checkpoint inhibitors (PD-1/PD-L1/CTLA-4)          │
│                     │ CAR-T cells                                         │
│                     │ Bispecific antibodies                               │
│                     │ Cancer vaccines (sipuleucel-T, mRNA-based)         │
├─────────────────────┼────────────────────────────────────────────────────┤
│ HORMONE THERAPY     │ Breast: SERMs, AIs, CDK4/6i, HER2-targeted         │
│                     │ Prostate: LHRH agonists, enzalutamide, abiraterone │
├─────────────────────┼────────────────────────────────────────────────────┤
│ ADC                 │ Antibody-Drug Conjugates: mAb + linker + payload   │
└─────────────────────┴────────────────────────────────────────────────────┘

SELECTIVITY problem: most cytotoxics = narrow TI; affect all dividing cells
  → Bone marrow, GI mucosa, hair follicles = most affected normal tissues
  Targeted therapy: broader TI but still toxicity (on-target, off-tumor)
  Immunotherapy: immune-related adverse events (irAEs) = collateral immune attack
```

---

## 1. Cytotoxic Chemotherapy

### Alkylating Agents

```
Mechanism: form covalent adducts with DNA nucleophiles (N7-guanine most common)
  → Intrastrand cross-links → blocks replication/transcription
  → Interstrand cross-links → DNA double strand breaks
  → Phase-nonspecific (kill in any cell cycle phase)

CYCLOPHOSPHAMIDE:
  Prodrug: activated by CYP2B6/3A4 → phosphoramide mustard (active alkylator) + acrolein
  Use: lymphomas, autoimmune (lupus nephritis, vasculitis), HSCT conditioning
  Acrolein → hemorrhagic cystitis → must co-administer MESNA (2-mercaptoethane sulfonate Na)
    or aggressive hydration to prevent bladder toxicity
  Myelosuppression, alopecia, teratogenic, secondary malignancies (leukemia 5–10yr later)
  SIADH at high doses

IFOSFAMIDE: similar to cyclophosphamide; higher encephalopathy (chloroacetaldehyde metabolite)
MELPHALAN: multiple myeloma conditioning
CHLORAMBUCIL: CLL (oral); single agent
BUSULFAN: HSCT conditioning; pulmonary fibrosis with chronic use

PLATINUM COMPOUNDS (produce intrastrand cross-links, unlike nitrogen mustards):
  CISPLATIN:
    Cross-links: 60–65% 1,2-GpG intrastrand; ↑ DNA repair complex assembly → p53 apoptosis
    Toxicities: NEPHROTOXICITY (irreversible tubular injury; pre-hydrate with NS; N-acetylcysteine);
      NEUROTOXICITY (glove-stocking neuropathy, ototoxicity — irreversible); myelosuppression; emetogenic
    Use: testicular (curative), bladder, lung (NSCLC), ovarian, head/neck
  CARBOPLATIN: less nephrotoxic/neurotoxic; more myelosuppression (thrombocytopenia);
    doses by AUC (Calvert formula using CrCl — "AUC dosing")
  OXALIPLATIN: colorectal cancer (FOLFOX); cold-triggered peripheral neuropathy (acute dysesthesia);
    cumulative neuropathy (limits dose)
```

### Antimetabolites (S-Phase Specific)

```
METHOTREXATE (MTX):
  Folate analog → competes with DHF for DHFR → ↓ THF → ↓ nucleotide synthesis
  Also inhibits TYMS → ↓ dTMP synthesis
  Uses: oncology (high-dose MTX in ALL, lymphoma, osteosarcoma), RA/psoriasis (low-dose anti-inflammatory)
  Leucovorin rescue: folinic acid (reduced folate) bypasses DHFR → rescues normal cells after high-dose MTX
    Timing critical: leucovorin 24h after MTX; monitor MTX levels
  Toxicity: mucositis, myelosuppression, hepatotoxicity (cirrhosis with chronic use), nephrotoxicity (high dose),
    pulmonary toxicity (pneumonitis), teratogenic (NTD, abort)

5-FLUOROURACIL (5-FU):
  Fluoropyrimidine → 5-FdUMP inhibits TYMS (covalent with folate cofactor)
  → ↓ dTMP → ↓ DNA synthesis (S-phase specific)
  Also incorporated into RNA as FUTP → disrupts RNA processing
  Leucovorin: stabilizes 5-FdUMP-TYMS-mTHF ternary complex → enhances inhibition (FOLFOX/FOLFIRI use leucovorin + 5-FU)
  Capecitabine (Xeloda): oral prodrug → 5-FU in tumor (tumor-specific thymidine phosphorylase)
  Toxicity: mucositis, diarrhea, myelosuppression, hand-foot syndrome (palmar-plantar erythrodysesthesia),
    cardiotoxicity (coronary vasospasm — rare, CI with recent MI)
  DPD (dihydropyrimidine dehydrogenase) deficiency → ↑ 5-FU levels → severe toxicity; test before prescribing

GEMCITABINE:
  Nucleoside analog → triphosphate incorporated → chain termination + RRNA inhibition
  S-phase specific; broad solid tumor use (pancreatic, lung, bladder, breast)
  Radiation sensitizer; capillary leak syndrome (hemolytic uremic syndrome variant) rare

CYTARABINE (ARA-C):
  Cytosine arabinoside; S-phase specific; AML cornerstone ("7+3" induction = cytarabine 7 days + daunorubicin 3 days)
  Ara-CTP inhibits DNA polymerase + chain termination
  High-dose: cerebellar toxicity, conjunctivitis (prophylaxis with steroid eye drops)
  "7+3" AML induction: standard of care for decades

PEMETREXED: multi-targeted antifolate (DHFR + TYMS + GARFT); lung adenocarcinoma; mesothelioma
  Supplement with folic acid + B12 before/during to ↓ toxicity (folate pathway disruption → myelosuppression/mucositis)
```

### Topoisomerase Inhibitors

```
TOPOISOMERASE I INHIBITORS (camptothecins):
  Mechanism: stabilize Topo I cleavable complex → "collision model" with replication fork
    → DNA single-strand breaks → converted to double-strand breaks when replication fork hits
  S-phase specific
  Irinotecan (CPT-11): FOLFIRI (5-FU + leucovorin + irinotecan); colorectal, lung, pancreatic
    Prodrug → SN-38 (active) via carboxylesterase; SN-38 glucuronidated by UGT1A1 → bile excretion
    UGT1A1*28 polymorphism (reduced glucuronidation → ↑ SN-38 → severe diarrhea + myelosuppression)
    Diarrhea: early (cholinergic — atropine) vs late (secretory — loperamide)
  Topotecan: ovarian, cervical, SCLC

TOPOISOMERASE II INHIBITORS (anthracyclines + others):
  Anthracyclines — mechanism:
    DNA intercalation → Topo II poison → DNA double-strand breaks
    Free radical generation (redox cycling of quinone group)
    Topoisomerase II inhibition (same as Topo I: stabilize cleavable complex)
  Drugs: doxorubicin (DOX), daunorubicin, epirubicin, idarubicin
  CARDIOTOXICITY: cumulative dose-dependent (>450mg/m² doxorubicin → ↑ cardiomyopathy risk)
    Mechanism: free radicals in cardiomyocytes (no superoxide dismutase) → oxidative damage
    Dexrazoxane: iron chelator → ↓ anthracycline cardiotoxicity; used in high-cumulative-dose patients
    Monitoring: baseline echo → q3 months during; liposomal formulation (less cardiotoxic)
  Etoposide (VP-16): Topo II poison; testicular, lymphoma, SCLC, HSCT conditioning
    Secondary AML (11q23/MLL rearrangement) with prolonged use
  Teniposide: similar to etoposide
```

### Microtubule Agents

```
TAXANES — stabilize (prevent depolymerization):
  Bind β-tubulin → lock microtubules in polymerized state → mitotic arrest (M-phase)
  Paclitaxel (Taxol): CREMOPHOR solvent → hypersensitivity (premedicate with steroids + diphenhydramine)
    Peripheral neuropathy (sensory > motor); myelosuppression; alopecia
    Use: breast, ovarian, lung
  Docetaxel: more potent; fluid retention syndrome (premedicate dex 3 days)
  Cabazitaxel: prostate cancer (docetaxel-resistant); ↑ CNS penetration
  Nab-paclitaxel (Abraxane): albumin-bound → no cremophor → no premedication; better tumor delivery
  Carbazitaxel vs paclitaxel P-gp resistance: cabazitaxel avoids MDR1 efflux → useful in resistant disease

VINCA ALKALOIDS — destabilize (prevent polymerization):
  Vincristine, vinblastine, vinorelbine: bind β-tubulin → prevent polymerization → disrupted spindle → mitotic arrest
  PERIPHERAL NEUROPATHY: vincristine predominant (dose-limiting); foot drop, cranial nerve palsies, autonomic
  Vincristine: ALL, lymphoma; NOT myelosuppressive (unusual among cytotoxics)
  Vinblastine: Hodgkin's (ABVD regimen); testicular
  Vinorelbine: NSCLC, breast
  VESICANT: severe tissue damage if extravasated; verify IV patency before administration
```

---

## 2. Targeted Therapy

### Kinase Inhibitors (-nibs)

```
IMATINIB (Gleevec) — the first successful targeted therapy:
  BCR-ABL (CML): Philadelphia chromosome t(9;22) → BCR-ABL fusion kinase → constitutive tyrosine kinase
  Imatinib: ATP-competitive; binds inactive ABL conformation; also inhibits PDGFR, c-KIT
  CML: response rates >90%; converted CML from median survival 3y → near-normal lifespan
  GIST: c-KIT or PDGFRA mutations → imatinib; continuation until progression
  T315I "gatekeeper" mutation: imatinib + 2nd-gen TKIs resistant → ponatinib (3rd-gen)

Second-generation BCR-ABL inhibitors:
  Dasatinib, nilotinib, bosutinib: ↑ potency vs most BCR-ABL mutations; CI T315I
  Ponatinib: active vs T315I; CV toxicity (arterial thrombosis) limits use

EGFR inhibitors:
  Erlotinib/gefitinib: EGFR exon 19 deletion or L858R mutation → NSCLC
  Afatinib, dacomitinib: irreversible 2nd/3rd-gen; wider EGFR mutation coverage
  Osimertinib: 3rd-gen; T790M resistance mutation → also 1st-line (FLAURA); CNS penetration
  Adverse: acneiform rash (paradoxically predicts response), diarrhea, paronychia, ILD

BRAF V600E inhibitors:
  Vemurafenib, dabrafenib: BRAF V600E (melanoma ~50%, thyroid, CRC ~5-10%)
  Paradoxical activation: BRAF inhibitor in BRAF WT cells → RAS activation → CRAF → ↑ MAPK
    → Paradoxical cutaneous squamous cell carcinomas; also need MEK inhibitor co-treatment
  Dabrafenib + trametinib (MEK inhibitor): standard; ↓ paradoxical SCC, improved response

MEK inhibitors: trametinib, cobimetinib, binimetinib — always in combination with BRAF-i

ALK/ROS1 inhibitors:
  Crizotinib (1st-gen): ALK+ NSCLC (~5%), ROS1 rearrangement; CNS escape common
  Alectinib, brigatinib, lorlatinib: 2nd/3rd-gen; better CNS penetration; lorlatinib even covers ALK G1202R

VEGFR inhibitors:
  Sorafenib, sunitinib: multi-kinase (VEGFR + PDGFR + RAF); HCC, RCC, GIST
  Axitinib, cabozantinib, lenvatinib: more selective VEGFR-2 focus
  Adverse: HTN (VEGF ↓ → endothelial NOS ↓ → vasoconstriction), hand-foot syndrome, thyroid dysfunction

BTK inhibitors:
  Ibrutinib (1st-gen): irreversible BTK inhibition (Cys481); CLL, MCL, WM, marginal zone lymphoma
    Adverse: atrial fibrillation (BTK in cardiomyocytes), bleeding (BTK in platelets), arthralgias
  Acalabrutinib, zanubrutinib: more selective → ↓ AF, ↓ bleeding vs ibrutinib

CDK4/6 inhibitors:
  Palbociclib, ribociclib, abemaciclib: ↓ CDK4/6 → ↓ Rb phosphorylation → G1/S block
  HR+ HER2- breast cancer: in combination with AI or fulvestrant → ↓ progression
  Myelosuppression (especially palbociclib); QTc (ribociclib); diarrhea (abemaciclib)

PI3K/AKT/mTOR pathway:
  mTOR inhibitors: everolimus (rapalog), temsirolimus — RCC, breast cancer, PNET
  PI3K inhibitors: idelalisib (PI3Kδ — CLL, follicular lymphoma); copanlisib; alpelisib (PI3Kα — PIK3CA-mutated HR+ BC)
  PTEN loss → pathway hyperactivation → resistance to many targeted therapies

PARP inhibitors (PARPi):
  Olaparib, rucaparib, niraparib, talazoparib: inhibit PARP1/2 → ↓ single-strand break repair
  SYNTHETIC LETHALITY: BRCA1/2 mutation → ↓ homologous recombination → rely on PARP for repair
    Double block (BRCA loss + PARP inhibition) → catastrophic DNA damage → cell death
    Cancer cells with BRCA deficiency are much more sensitive than normal BRCA+/+ cells
  FDA-approved: ovarian (BRCA and HRD), breast (BRCA1/2 germline), prostate (HRRm), pancreatic
  PARP trapping (olaparib > others): PARP-DNA complex stuck → more toxic than PARP catalytic inhibition
  Adverse: myelosuppression, nausea, fatigue; secondary MDS/AML (uncommon)

BCL-2 inhibitors:
  Venetoclax: BH3-mimetic → displaces pro-apoptotic proteins from BCL-2 → BAX/BAK activation → cytochrome c release → apoptosis
  CLL (especially with ibrutinib or obinutuzumab), AML (with azacitidine)
  TUMOR LYSIS SYNDROME (TLS): massive cell death → hyperuricemia, hyperkalemia, hyperphosphatemia, hypocalcemia → AKI/arrhythmia
    RAMP-UP dosing (5mg → 20 → 50 → 100 → 200 → 400mg over 5 weeks) to ↓ TLS risk
    Prophylaxis: allopurinol + hydration; hospitalize for first dose
```

### Monoclonal Antibodies (Oncology)

| Drug | Target | Indication | Mechanism | Key Toxicity |
|------|--------|-----------|-----------|-------------|
| Trastuzumab (Herceptin) | HER2 (ECD domain IV) | HER2+ breast + gastric | ↓ signaling + ADCC + ↓ HER2 shedding | Cardiotoxicity (↓ LVEF, reversible; avoid with anthracyclines) |
| Pertuzumab | HER2 (dimerization domain II) | HER2+ breast | ↓ HER2-HER3 heterodimers; combine with trastuzumab | Diarrhea, infusion reactions |
| Cetuximab | EGFR | Colorectal (RAS WT), H&N cancer | Blocks EGF binding + ADCC | Acneiform rash (paradox = response marker), hypomagnesemia, infusion reaction |
| Rituximab | CD20 | B-cell NHL, CLL, RA, autoimmune | CDC + ADCC + direct apoptosis | Infusion reactions (first dose), PML (JC virus → progressive multifocal leukoencephalopathy — rare) |
| Bevacizumab | VEGF-A | Colorectal, lung, ovarian, GBM | ↓ angiogenesis → tumor starvation | HTN, wound dehiscence, ↑ hemorrhage, thrombosis, bowel perforation |
| Obinutuzumab | CD20 | CLL | Enhanced ADCC + direct cell death vs rituximab | Infusion reactions, myelosuppression |
| Daratumumab | CD38 | Multiple myeloma | ADCC + CDC + ↓ regulatory cells | Infusion reactions, myelosuppression |

---

**Systems Bridge:** Immune checkpoints (PD-1, CTLA-4) are rate limiters and circuit breakers on T-cell activation — they exist to prevent runaway immune responses against self-tissue (autoimmunity) and to terminate responses after the threat is cleared. Tumors exploit these checkpoints by expressing PD-L1 (the ligand for PD-1) on their surface — effectively flashing a "self" credential that tells T-cells to stand down. Checkpoint inhibitors (anti-PD-1/PD-L1, anti-CTLA-4) remove the rate limiter — they allow T-cells that were being suppressed to activate and attack the tumor. The consequence is the same as removing a safety interlock in any system: the desired process (anti-tumor immunity) is unleashed, but so are the pathological processes the interlock was preventing (immune-related adverse events, irAEs — colitis, pneumonitis, hepatitis, thyroiditis, dermatitis). These are not drug toxicities in the traditional sense; they are the immune system attacking self-tissues once the brakes are off. irAEs are managed with corticosteroids (re-engaging immune suppression) and, in severe cases, permanent checkpoint inhibitor discontinuation. The trade-off — remove the rate limiter to achieve the desired effect, accept the risk of runaway side effects — is exactly the design dilemma in any system where you need to turn off a protective constraint to unlock performance.

## 3. Immunotherapy

### Checkpoint Inhibitors

```
NORMAL T-CELL ACTIVATION CHECKPOINTS:
  CTLA-4: expressed on T cells after activation → competes with CD28 for B7 (CD80/86) on APCs
    → limits T-cell expansion (brake on early activation)
  PD-1: expressed on T cells in chronic stimulation → binds PD-L1/PD-L2 on APCs or tumor cells
    → tumor cells exploit this → T-cell exhaustion → tumor immune escape

CHECKPOINT INHIBITORS: remove these brakes → unleash anti-tumor T cells

ANTI-CTLA-4:
  Ipilimumab (Yervoy): fully human IgG1; melanoma (1st approved checkpoint inhibitor, 2011)
  Higher irAE rate vs anti-PD-1; robust activation of early immune response
  Combination ipilimumab + nivolumab: ↑ efficacy, ↑ irAEs

ANTI-PD-1:
  Nivolumab (Opdivo): human IgG4; melanoma, NSCLC, RCC, HNSCC, MSI-H tumors, HCC, bladder
  Pembrolizumab (Keytruda): humanized IgG4; FDA-approved >20 solid tumor types
    PD-L1 testing: some indications require >50% tumor proportion score (TPS) for approval
    TMB (tumor mutational burden): high TMB → ↑ neoantigens → ↑ T cell recognition → ↑ response
    MSI-H (microsatellite instability-high) / dMMR: tumor-agnostic approval (any MSI-H solid tumor) — 2017

ANTI-PD-L1:
  Atezolizumab: IgG1 (Fc-modified to ↓ ADCC); bladder, NSCLC, TNBC, HCC
  Durvalumab: bladder, NSCLC (unresectable stage III)
  Avelumab: Merkel cell carcinoma, bladder

IMMUNE-RELATED ADVERSE EVENTS (irAEs):
  Mechanism: off-tumor T-cell activation → autoimmune attack of normal tissues
  Any organ, any time (even months after stopping)
  Most common: dermatologic (rash, vitiligo), GI (colitis — especially ipilimumab), endocrine (thyroid,
    adrenal, pituitary — hypophysitis), hepatitis, pneumonitis, nephritis
  Grade 1–2: continue checkpoint + symptomatic management
  Grade 3–4: hold checkpoint + high-dose corticosteroids (prednisone 1–2mg/kg/day)
    Grade 4 or steroid-refractory: infliximab (anti-TNF) for colitis; cyclophosphamide for others
  Endocrine irAEs: often permanent → replace hormones long-term even after steroids taper
  Hypophysitis: ↓ ACTH, TSH, LH/FSH → adrenal insufficiency (dangerous), hypothyroidism, hypogonadism
  Timing of irAEs: dermatologic early (2–4 weeks), GI/hepatic (6–12 weeks), endocrine (variable, can be late)
```

### CAR-T Cells

```
Process:
  1. Leukapheresis: collect patient's T cells
  2. Ex vivo engineering: lentiviral transduction → chimeric antigen receptor (CAR) gene
  3. CAR structure: extracellular single-chain antibody (scFv) + hinge + transmembrane domain +
     intracellular CD3ζ signaling domain + co-stimulatory domains (CD28 or 4-1BB/CD137)
  4. Ex vivo expansion → infusion back into patient
  5. CAR-T cells bind target antigen (no MHC restriction) → T-cell activation → tumor killing

Current approvals:
  CD19 (B-cell malignancies): tisagenlecleucel (Kymriah — ALL, DLBCL), axicabtagene ciloleucel (Yescarta — DLBCL),
    brexucabtagene autoleucel (Tecartus — MCL), lisocabtagene maraleucel (Breyanzi — DLBCL)
  BCMA (multiple myeloma): idecabtagene vicleucel (Abecma), ciltacabtagene autoleucel (Carvykti)

TOXICITIES:
  CRS (cytokine release syndrome):
    Massive cytokine release from activated T cells + macrophages
    Onset: 1–14 days; fever → hypotension → hypoxia → multiorgan failure
    Key mediator: IL-6 → treatment: tocilizumab (anti-IL-6R) + steroids
    Graded by ASTCT criteria (grade 1 = fever only; grade 4 = life-threatening)
  ICANS (immune effector cell-associated neurotoxicity syndrome):
    Confusion, aphasia, seizures, cerebral edema
    BBB disruption → cytokines cross → endothelial activation
    Treatment: dexamethasone (not tocilizumab — IL-6R not on brain endothelium)
  Cytopenias: prolonged (months) after CAR-T; infectious complications
  Hypogammaglobulinemia: if prolonged B-cell aplasia → IVIg replacement
```

### Bispecific Antibodies

**Blinatumomab (Blincyto):** CD3 × CD19 bispecific T-cell engager (BiTE); engages endogenous T cells to CD19+ B cells; ALL (relapsed/refractory, MRD-positive); continuous IV infusion; CRS, neurotoxicity.

**Mosunetuzumab, glofitamab:** CD3 × CD20; follicular lymphoma, DLBCL.

**Talquetamab, teclistamab:** CD3 × BCMA or GPRC5D; multiple myeloma.

---

## 4. Hormone Therapy

### Breast Cancer

```
ER+ (estrogen receptor positive) breast cancer: estrogen drives proliferation → deprivation = treatment

SERMS:
  Tamoxifen: competitive ER antagonist in breast (+ agonist in uterus/bone)
    → ↓ recurrence/mortality in early + advanced ER+ breast cancer
    Metabolized by CYP2D6 → endoxifen (active); CYP2D6 PMs → ↓ benefit (avoid paroxetine/fluoxetine)
    Adverse: hot flashes, thromboembolism (DVT/PE), endometrial cancer (agonist effect on uterus)
    Pre- and post-menopausal women

AROMATASE INHIBITORS (AIs): anastrozole, letrozole, exemestane
  Block CYP19A1 (aromatase) → ↓ peripheral androgen→estrogen conversion → ↓ estrogen in postmenopausal women
  Postmenopausal only (ovaries still producing estrogen in premenopausal → AIs insufficient alone)
  Adverse: musculoskeletal symptoms (arthralgias/myalgias, "AI arthralgia"), osteoporosis, vaginal dryness
  Exemestane: steroidal (irreversible); anastrozole/letrozole: non-steroidal (reversible)
  Superior to tamoxifen for post-menopausal ER+ breast cancer

FULVESTRANT: SERD (selective estrogen receptor degrader) — binds ER → ↓ receptor protein expression
  Pure antagonist (no agonist effects); IM injection; post-menopausal + ESR1 mutation resistance

ELACESTRANT, CAMIZESTRANT: oral SERDs; ESR1-mutated (resistance to AIs); improved delivery vs IM fulvestrant

CDK4/6 inhibitors + AI: first-line standard for HR+ HER2- metastatic breast cancer
  Palbociclib, ribociclib, abemaciclib + letrozole/anastrozole or fulvestrant → doubled PFS
  MONARCH E (abemaciclib): benefit in early-stage high-risk HR+ BC

ALPELISIB: PIK3CA inhibitor; HR+ BC + PIK3CA mutation (>40% of HR+ BC); + fulvestrant
  Adverse: hyperglycemia (PI3Kα in pancreatic β-cells and insulin signaling), rash

HER2-targeted (breast):
  Trastuzumab → pertuzumab → trastuzumab-emtansine (T-DM1 = ADC) → trastuzumab-deruxtecan (T-DXd)
  Lapatinib: oral dual EGFR/HER2 TKI; CNS activity
  Neratinib, tucatinib: irreversible or more selective HER2 TKIs; CNS penetration (tucatinib)
```

### Prostate Cancer

```
ANDROGEN DEPRIVATION THERAPY (ADT):
  Testosterone drives prostate cancer growth (AR signaling)

LHRH agonists (GnRH agonists): leuprolide, goserelin, triptorelin
  Initial: ↑ LH/FSH surge ("flare") → transient ↑ testosterone (weeks) → add anti-androgen at start
  Continuous: pituitary GnRH receptor downregulation → ↓ LH → ↓ testosterone (castrate level <50 ng/dL)
  Depot formulations (monthly/3-monthly/yearly)

LHRH antagonists (GnRH antagonists): degarelix, relugolix
  Direct GnRH receptor blockade → no testosterone flare; faster castration
  Relugolix (oral): ↓ CV events vs LHRH agonists (relugolix pivotal trial)

ANTI-ANDROGENS (AR antagonists):
  1st gen: bicalutamide, flutamide, nilutamide (partial agonist at high AR — cause resistance)
  2nd gen: enzalutamide, apalutamide, darolutamide (no CNS penetration → less CNS toxicity)
    Mechanism: ↓ AR translocation, ↓ DNA binding, ↓ co-activator recruitment; no agonist activity

ABIRATERONE:
  Irreversible inhibitor of CYP17A1 (17α-hydroxylase/17,20-lyase) → ↓ androgen synthesis in adrenals + tumor
  ↓ ALL androgens including precursor pathways
  Combined with prednisone (↑ mineralocorticoid precursors → HTN/hypokalemia → corticosteroid needed)
  Oral; hepatic metabolism; food-dependent absorption (take fasted or with low-fat meal)
```

---

## 5. Antibody-Drug Conjugates (ADCs)

```
STRUCTURE: Antibody → linker → cytotoxic payload

Antibody: targeting component (selectivity to tumor antigen)
Linker: cleavable (lysosomal pH/protease) or non-cleavable (metabolism)
  Cleavable linkers release payload inside tumor cell (or neighborhood — bystander effect)
  Non-cleavable: payload released only in cell, no bystander effect (need high target expression)
Payload: ultra-potent cytotoxin (can't use systemically due to TI)
  DM1/DM4 (maytansinoids → tubulin): T-DM1 (ado-trastuzumab emtansine)
  MMAE (monomethyl auristatin E → tubulin): brentuximab vedotin (anti-CD30), polatuzumab vedotin
  Dxd (deruxtecan = camptothecin derivative → Topo I): T-DXd, enfortumab vedotin in development
  Calicheamicin (DNA alkylator): gemtuzumab ozogamicin, inotuzumab ozogamicin

Key ADCs:
  T-DM1 (ado-trastuzumab emtansine, Kadcyla): anti-HER2 + DM1; HER2+ breast cancer
  T-DXd (trastuzumab deruxtecan, Enhertu): anti-HER2 + DXd; HER2+ and HER2-low breast/gastric/lung
    "HER2-low" (IHC 1+ or 2+/ISH-): previously untreatable with HER2-targeted therapy
    Interstitial lung disease (ILD) → important toxicity; bystander effect (membrane-permeable payload)
  Brentuximab vedotin (Adcetris): anti-CD30 + MMAE; Hodgkin lymphoma, ALCL
  Enfortumab vedotin (Padcev): anti-Nectin-4 + MMAE; urothelial carcinoma
  Sacituzumab govitecan (Trodelvy): anti-TROP2 + SN-38 (irinotecan metabolite); TNBC, urothelial
  Inotuzumab ozogamicin (Besylomib): anti-CD22 + calicheamicin; B-cell ALL
```

---

## Decision Cheat Sheet

| Cancer Type | Key Targeted Therapy / Driver | Drug |
|------------|------------------------------|------|
| CML | BCR-ABL (Ph+) | Imatinib → dasatinib/nilotinib → ponatinib (T315I) |
| NSCLC EGFR-mutated | EGFR ex19del/L858R | Osimertinib (1st-line or T790M) |
| NSCLC ALK-rearranged | ALK fusion | Alectinib (1st-line) → lorlatinib |
| NSCLC BRAF V600E | BRAF V600E | Dabrafenib + trametinib |
| Melanoma BRAF V600E | BRAF V600E | Dabrafenib + trametinib or vemurafenib + cobimetinib |
| Melanoma (immunotherapy) | High TMB/MSI-H | Ipilimumab + nivolumab → pembrolizumab |
| HER2+ breast | HER2 amplified | Pertuzumab + trastuzumab + taxane → T-DXd (if relapsed) |
| HR+ HER2- metastatic BC | ER+, HER2- | CDK4/6i + AI or fulvestrant |
| Prostate (mCRPC) | AR signaling | Enzalutamide or abiraterone + prednisone |
| CLL | BTK pathway | Ibrutinib/acalabrutinib (BTK) or venetoclax + obinutuzumab |
| AML | FLT3-ITD/D835 | Midostaurin (+ chemo), gilteritinib (relapsed) |
| AML BCL-2 | All AML (elderly/unfit) | Venetoclax + azacitidine |
| Ovarian BRCA1/2 | BRCA1/2 germline/somatic | Olaparib maintenance; niraparib (all-comer) |
| MSI-H any solid tumor | MMR deficiency | Pembrolizumab (tumor-agnostic) |

---

## Common Confusion Points

**Cytotoxic vs targeted selectivity:** Cytotoxics exploit differential growth rate (cancer cells divide faster → more DNA synthesis → more drug incorporation). Targeted therapy exploits oncogene addiction (cancer relies on one pathway; inhibit it → die). Neither is perfectly selective.

**PARP inhibitor synthetic lethality mechanism:** BRCA1/2 are needed for HR (homologous recombination) repair. Normal cells use HR when PARP is inhibited (BER backup lost but HR works). BRCA-mutant cells have NO HR backup → catastrophic DSBs → death. Normal cells fine.

**Checkpoint inhibitors and autoimmunity:** The irAEs are not "side effects" per se — they are the on-target mechanism occurring in normal tissues. Every organ can be affected. The T cells are working as intended; they just can't distinguish tumor from self. Endocrine irAEs (thyroid, adrenal, pituitary) are often irreversible — replace lifelong.

**CAR-T vs bispecific T-cell engager:** CAR-T = engineering patient's T cells ex vivo; long-lived response; one-time (usually); expensive manufacturing time; needs lymphodepletion. Bispecific (BiTE): engages endogenous T cells in vivo; continuous infusion; no manufacturing delay; can be more broadly applied.

**Anthracycline cardiotoxicity:** Mechanism = free radicals (ROS), not direct toxin. Cumulative dose of doxorubicin >450–550 mg/m² = ↑ risk. Dexrazoxane chelates iron (prevents Fe-catalyzed radical formation). Liposomal formulations (Doxil) ↓ peak levels → ↓ cardiac exposure. But liposomal doxorubicin = hand-foot syndrome.

**BCR-ABL imatinib resistance:** T315I gatekeeper mutation = resistant to imatinib AND 2nd-gen TKIs. Only ponatinib (3rd-gen) and asciminib (allosteric site) overcome T315I. Always sequence correctly.
