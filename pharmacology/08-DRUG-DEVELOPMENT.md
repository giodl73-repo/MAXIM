# Drug Development: Discovery to Approval

## The Big Picture

Drug development is a 10-15 year, $2-3 billion process from identifying a target to a marketed drug. Failure rates are staggering: ~90% of drugs that enter clinical trials never reach approval. Understanding the pipeline architecture clarifies why drugs cost what they do and why failures are economically catastrophic.

```
+──────────────────────────────────────────────────────────────────+
|              DRUG DEVELOPMENT PIPELINE                           |
|                                                                  |
|  TARGET   →  LEAD       →  PRECLINICAL  →  CLINICAL TRIALS  →    |
|  ID          DISCOVERY     TESTING         Phase I/II/III        |
|  ~2 yr       ~2 yr         ~3-4 yr         ~6-8 yr               |
|                                                                  |
|  Failure rate: ────────────────────────────────────────────────  |
|  Target ID    Lead        Enter      Phase I   Phase II  Ph III  |
|  10-20% of   ~90% of     IND:       63% fail  66% fail  44%      |
|  targets     compounds   10% pass                        fail    |
|  validated   eliminated              ← Only ~10% through III →   |
|                                                                  |
|  → FDA REVIEW → APPROVAL → POST-MARKETING SURVEILLANCE (PV)      |
|     6-12 mo                           Ongoing forever            |
+──────────────────────────────────────────────────────────────────+
```

---

## Target Identification and Validation

```
TARGET IDENTIFICATION
──────────────────────
  DISEASE HYPOTHESIS → MOLECULAR TARGET

  Methods:
  • Genetic linkage / GWAS: SNPs associated with disease → pathway
  • CRISPR screens: knockout each gene → find which causes disease phenotype
  • Proteomics: which proteins are differentially expressed/modified?
  • Metabolomics: what metabolic changes accompany disease?
  • Literature mining / pathway analysis

  Good drug target characteristics:
  • Disease-causative (not just correlated)
  • Druggable (has binding pocket for small molecule; or accessible epitope for antibody)
  • Essential for disease but dispensable in normal tissue
  • Biomarker exists to measure target engagement

TARGET VALIDATION
──────────────────
  Genetic: knockout/knockin animal models, patient loss-of-function mutations
  Pharmacological: tool compounds → if modulating target → disease effect
  Biomarker: measure target to confirm it's relevant in human disease

  Classic validation success: BCR-ABL in CML
    t(9;22) → BCR-ABL fusion → constitutive kinase → imatinib works brilliantly.
    Causative, druggable, and biomarker (Philadelphia chromosome) all confirmed.

  Classic validation failure: tau in Alzheimer's
    Tau aggregates in AD brains. But causality uncertain.
    Many anti-tau drugs failed Phase II/III.
    Amyloid hypothesis similarly suffered many failures.
    Target validation remains the hardest step in CNS drug discovery.
```

---

## Lead Discovery and Optimization

```
LEAD DISCOVERY APPROACHES
───────────────────────────

PHENOTYPIC SCREENING (old-school but resurging)
  Screen libraries of compounds for effect on cell or organism.
  No predetermined target. Mechanism worked out later.
  Historically produced many approved drugs (e.g., aspirin origin).
  Advantage: finds drugs targeting unknown mechanisms.
  Disadvantage: mechanism unknown → harder to optimize.

STRUCTURE-BASED DRUG DESIGN (SBDD)
  X-ray crystallography or cryo-EM of target protein.
  Design molecules that fit the active site.
  Build drug around 3D structure.
  Fragment-based screening: start with small fragments that bind weakly,
  link them together → high-affinity drug.

HIGH-THROUGHPUT SCREENING (HTS)
  Robotic screening of 10⁶+ compounds vs target.
  Fluorescence or luminescence readout.
  Hit rate: ~0.01-0.1% → 100-1000 hits from 10⁶ compounds.

VIRTUAL SCREENING / AI-BASED
  Molecular docking: computational simulation of binding.
  Generative AI: design novel compounds in silico.
  AlphaFold: predict 3D structure of target when crystallography unavailable.
  AI-designed drugs in clinical trials (as of 2025-2026): Insilico Medicine's ISM001-055
  (IPF, Phase II completed with signals of efficacy); Recursion Pharmaceuticals multiple
  programs in Phase I/II; Exscientia/Evotec partnerships; Absci (zero-shot antibody design);
  Generate Biomedicines (protein design). The first AI-designed drug to reach Phase II
  efficacy data was ISM001-055 (Insilico/Corcept) in 2024.

LEAD OPTIMIZATION
  Hit → Lead → Candidate:
  Modify hit compound to:
  (1) ↑Potency: improve binding to target
  (2) ↑Selectivity: reduce off-target effects
  (3) Improve PK: increase oral bioavailability, reduce metabolism
  (4) Reduce toxicity: remove reactive groups, improve safety profile

LIPINSKI'S RULE OF 5 (for oral bioavailability)
  MW ≤ 500 Da
  H-bond donors ≤ 5
  H-bond acceptors ≤ 10
  logP ≤ 5 (lipophilicity)
  Violations predict poor oral absorption/permeability.
  Biologics (antibodies, peptides) don't obey Rule of 5 — different delivery.
```

---

## Preclinical Development

```
PRECLINICAL TESTING REQUIREMENTS
──────────────────────────────────
Before first human dose, must demonstrate:
  (1) Desired pharmacological effect in animal models
  (2) Characterization of PK (ADME) in animals
  (3) Safety: No unacceptable acute/chronic toxicity
  (4) Genotoxicity: Ames test (bacteria), micronucleus test
  (5) Safety pharmacology: heart (hERG), CNS, respiratory

ANIMAL MODELS
  In vitro: Cell lines, primary cells, organoids
  In vivo: Rodents (mouse, rat), then non-rodents (dog, monkey)
  Regulatory requirement: 2 species for toxicology (1 rodent + 1 non-rodent)

ALLOMETRIC SCALING (dose translation)
  Starting dose in Phase I estimated from:
    NOAEL (No-Observed-Adverse-Effect Level) in most sensitive species
    × Safety factor (usually 1/10 the NOAEL expressed as mg/kg)
    × Body surface area or weight-based conversion to humans
  Biologics: use minimum anticipated biological effect level (MABEL)

IND (Investigational New Drug Application to FDA)
  After preclinical, sponsor files IND:
  • Chemistry, manufacturing, controls (CMC)
  • Preclinical data package
  • Clinical protocol for Phase I
  • Investigators' brochure

  If FDA doesn't object within 30 days → can start Phase I.
  FDA can put on "clinical hold" if safety concerns.
```

---

## Clinical Trials: Phase I, II, III

```
PHASE I: FIRST IN HUMAN
────────────────────────
  Purpose:     Safety, tolerability, PK, PD
               Find maximum tolerated dose (MTD)
  Design:      Dose escalation (3+3 design, accelerated titration, BOIN, mTPI)
  Population:  Healthy volunteers (non-oncology)
                OR cancer patients with advanced disease (oncology)
  Size:        20-80 patients
  Duration:    1-2 years

  DOSE ESCALATION DESIGN
  3+3 Classic:  3 patients at dose level.
               If 0/3 DLT → escalate. If 1/3 → add 3 more.
               If ≥2/6 DLT → stop, MTD = previous level.
  Modern adaptive: BOIN, mTPI use Bayesian methods → more efficient.

  Dose Limiting Toxicity (DLT): predefined severe adverse events in first cycle.
  MTD: highest dose with DLT in < 33% of patients.
  OBD (optimal biological dose): for biologics, not MTD but effective dose.

PHASE II: PROOF OF CONCEPT
────────────────────────────
  Purpose:     Preliminary efficacy signal; dose selection; biomarker development
  Design:      Single-arm (response rate vs historical control)
               OR randomized Phase II (vs placebo or active comparator)
  Population:  Target disease patient population; biomarker-selected
  Size:        50-300 patients
  Endpoint:    Response rate (ORR), progression-free survival (PFS), biomarkers
  Duration:    1-3 years

  Key decision gate:
  Go/No-Go for Phase III based on:
  • Efficacy signal sufficient to power Phase III?
  • Toxicity acceptable?
  • Appropriate patient population and dose identified?

PHASE III: CONFIRMATORY
────────────────────────
  Purpose:     Efficacy vs standard of care (or placebo); safety profile
  Design:      Randomized Controlled Trial (RCT); double-blind; superiority/non-inferiority
  Population:  Large, representative disease population
  Size:        300-5,000+ patients (depends on effect size and endpoint)
  Primary endpoint: Typically overall survival (OS) or PFS (surrogate for OS)
  Duration:    2-5 years

  STATISTICAL DESIGN
  Power: typically 80-90% to detect minimum clinically meaningful difference.
  Type I error: α = 0.05 (5% chance of false positive).
  Interim analyses with pre-specified stopping rules (futility, efficacy).
  Adaptive designs: modify sample size or arms based on interim data.
```

---

## FDA Approval Process

```
FDA SUBMISSION TYPES
─────────────────────
  NDA (New Drug Application): Small molecule drugs
  BLA (Biologics License Application): Vaccines, proteins, gene therapy
  ANDA (Abbreviated NDA): Generic drugs (bioequivalence, not safety/efficacy)
  510(k): Medical devices (substantially equivalent to predicate device)

NDA/BLA SECTIONS
  Module 1: Administrative and prescribing information
  Module 2: Common technical document summaries
  Module 3: Quality (CMC — chemistry, manufacturing, controls)
  Module 4: Nonclinical (animal) study reports
  Module 5: Clinical study reports

REVIEW TIMELINES
  Standard review: 10 months
  Priority review: 6 months (serious condition + addresses unmet need)
  Breakthrough therapy designation: more intense guidance; may qualify for priority review
  Accelerated approval: approval on surrogate endpoint; confirmatory trial required
  Fast track: frequent interactions with FDA; rolling review allowed

ADVISORY COMMITTEES
  FDA convenes advisory committees (AdComs) for complex decisions.
  External experts vote on approvability questions.
  FDA not bound by vote but usually follows it.
  High-profile examples: alzheimer's drugs (aducanumab controversy)

POST-MARKETING SURVEILLANCE (PHARMACOVIGILANCE)
  REMS (Risk Evaluation and Mitigation Strategy): required for dangerous drugs.
    Thalidomide (iPLEDGE): extreme teratogen; pregnancy test required before dispensing.
    Clozapine: CBC monitoring program for agranulocytosis.
    Isotretinoin (iPLEDGE): severe teratogen; multiple pregnancy tests/contraception.
  Phase IV trials: post-approval; required or voluntary; detect rare toxicities.
  Pharmacovigilance databases: FDA FAERS, VigiBase (WHO).
```

---

## Engineering Bridge: Drug Development as Software Release Pipeline

The drug development pipeline and Bayesian clinical trial design have direct engineering analogs.

```
  DRUG DEVELOPMENT              SOFTWARE RELEASE / ENGINEERING PARALLEL
  ──────────────────────────────────────────────────────────────────────
  Target identification         Requirements definition:
                                What is the biological problem to solve?
                                What is the measurable endpoint?

  Lead discovery (HTS + AI)     Architecture / proof-of-concept:
                                Does the approach work at all?
                                Hit rate 0.01-0.1% → architecture studies
                                have similar low-signal searches.

  Preclinical testing           Unit + integration testing:
                                In vitro = unit tests; in vivo = integration
                                tests. NOAEL is the passing threshold.
                                IND filing = design review gate (FDA has 30
                                days to object before "approval by silence").

  Phase I (safety, PK, MTD)     Alpha / internal testing:
                                20-80 users; find failure modes;
                                dose-escalation = binary search for MTD.
                                3+3 design = conservative escalation with
                                DLT stop rule. Bayesian adaptive (BOIN) =
                                online learning dose-escalation.

  Phase II (efficacy signal)    Beta / limited GA rollout:
                                50-300 users; preliminary efficacy signal.
                                Go/no-go gate: is this worth a Phase III?
                                Power often limited → many false negatives.

  Phase III (confirmatory RCT)  GA candidate / staged rollout:
                                300-5000+ users; powered for hard endpoint.
                                Double-blind RCT = the A/B test. Interim
                                analysis with alpha-spending = sequential
                                hypothesis testing. Adaptive design =
                                midpoint sample-size re-estimation.

  FDA review (NDA/BLA)          Compliance certification / security audit:
                                Independent review of all evidence. Advisory
                                committee = external security review board.
                                Accelerated approval = conditional production
                                deploy with required follow-up confirmation.

  Post-marketing surveillance   Production monitoring / incident response:
  (pharmacovigilance)           FAERS = incident database. REMS = privileged
                                access control for dangerous drugs (requires
                                a certified process to use). Phase IV =
                                post-deploy validation studies.

  Failure rate (~90% attrition) Product funnel: 10,000 compounds → 1 NDA.
                                Phase II → Phase III: ~30% success.
                                Oncology has the lowest Phase III success
                                (~40%); CNS the lowest overall (~8%).
  ──────────────────────────────────────────────────────────────────────
```

---

## Generics, Biosimilars, and Drug Pricing

```
GENERIC DRUGS (ANDA)
─────────────────────
  Same active ingredient, same dose, same route.
  Must demonstrate bioequivalence (Cmax and AUC within 80-125% of original).
  Approved via ANDA — no safety/efficacy trials needed.
  Hatch-Waxman Act (1984): 180-day exclusivity period for first generic filer.
  Authorized generics: branded company makes "own generic" to compete.

BIOSIMILARS
  Biologics are complex proteins — cannot be identically reproduced.
  Biosimilar: "highly similar" to reference biologic; no clinically meaningful differences.
  More evidence required than small-molecule generics:
    Structural characterization
    Functional assays
    PK/PD studies
    Clinical data (1 or more trials)
  FDA Purple Book: biosimilar reference database.
  Interchangeability designation: pharmacist can substitute without prescriber sign-off.
  Examples: Zarxio (filgrastim-sndz), Inflectra (infliximab-dyyb), multiple adalimumab biosimilars.

PATENT PROTECTION AND DATA EXCLUSIVITY
  Standard patent: 20 years from filing (often ~10 years remaining at approval)
  Data exclusivity (Hatch-Waxman): 5 years for new chemical entity; 3 years for new indication
  Pediatric exclusivity: 6 months additional if pediatric studies conducted
  Orphan drug exclusivity: 7 years (prevalence < 200,000 US patients)
  Biologic data exclusivity: 12 years (Biologics Price Competition and Innovation Act)
```

---

## Decision Cheat Sheet

| Development Stage | Key Question | Key Measure |
|------------------|-------------|-------------|
| Target ID | Does target cause disease? | Genetic/functional validation |
| Lead discovery | Does compound bind target? | IC50, Kd |
| Lead optimization | Is oral bioavailability acceptable? | Lipinski's rules, F% in animals |
| Preclinical safety | NOAEL in two species | mg/kg starting dose for Phase I |
| Phase I | What's the maximum safe dose? | MTD, DLT rate |
| Phase II | Is there an efficacy signal? | ORR, PFS, biomarker |
| Phase III | Better than standard of care? | OS or PFS, powered RCT |
| FDA review | Does benefit outweigh risk? | Complete response vs approval |
| Post-marketing | What rare events emerge at scale? | FAERS reports, REMS programs |

---

## Common Confusion Points

**"Phase I is about finding the right dose — why doesn't everyone start at the right dose from animal studies?"**
Because allometric scaling is imprecise. Animals metabolize drugs differently (different CYP profiles), have different receptor affinities, and different body compositions. The NOAEL-to-human conversion uses safety factors specifically because the translation is uncertain. Phase I's job is to find the safe clinical dose with actual human PK/PD data.

**"Accelerated approval on a surrogate endpoint — why is that acceptable?"**
For serious or life-threatening conditions with unmet need, waiting for overall survival data can take years. Surrogates like tumor response rate or CD4 count (HIV) often predict long-term benefit. The tradeoff: drugs approved faster on surrogates must have confirmatory trials to verify actual clinical benefit. If the confirmatory trial fails, FDA can withdraw approval (this rarely happens in practice, creating tension).

**"Why do drugs cost $50,000-$500,000 a year?"**
Fully loaded development cost: ~$2.6 billion per approved drug (DiMasi et al.), including the cost of the ~90% that failed. Revenue from approved drugs must recoup costs of failed drugs, preclinical research, regulatory infrastructure, and ongoing pharmacovigilance. Orphan drugs (rare diseases) are more expensive because smaller patient populations over which to amortize costs. The economic model is heavily criticized but reflects the true capital intensity of drug development.
