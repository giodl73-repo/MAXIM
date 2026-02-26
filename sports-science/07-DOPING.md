# Doping Biochemistry: Mechanisms and Detection

## The Big Picture

Doping in sport is an arms race between performance biochemistry and analytical chemistry. Understanding it requires: knowing what the substances do physiologically, why they work, and why detection is hard. It is also a policy and measurement system — the WADA framework is a global governance structure with its own logic and limitations.

```
DOPING LANDSCAPE:

  PROHIBITED SUBSTANCE/METHOD
  +-----------------------------------------------------------+
  |                                                           |
  |  ANABOLIC AGENTS      PEPTIDE HORMONES    BLOOD DOPING   |
  |  (testosterone,       (EPO, GH, IGF-1,   (autologous    |
  |   SARMs, others)       LH, CG, GHRH,      RBC transfusion|
  |                         insulin)           or rhEPO)      |
  |                                                           |
  |  BETA-2 AGONISTS      DIURETICS &         GENE DOPING    |
  |  (high dose —         MASKING AGENTS      (AAV-delivered |
  |   anabolic effect)    (probenecid,         transgenes,    |
  |                        furosemide)         CRISPR)        |
  |                                                           |
  |  STIMULANTS           NARCOTICS           CANNABINOIDS   |
  |  (amphetamines,       (in-competition     (in-competition|
  |   cocaine, etc.)       only)               only)         |
  +-----------------------------------------------------------+
                  |
                  v
  DETECTION FRAMEWORK
  +-----------------------------------------------------------+
  |  DIRECT DETECTION: find the substance or its metabolites  |
  |  INDIRECT DETECTION: biomarker profile changes           |
  |  LONGITUDINAL MONITORING: biological passport            |
  |  WHEREABOUTS: athlete must report location for testing   |
  +-----------------------------------------------------------+

  KEY WADA DOCUMENTS:
  Prohibited List: updated annually, effective 1 January.
  World Anti-Doping Code: framework for all sports/national bodies.
  Technical Documents: detection criteria per substance.
  Athlete Biological Passport (ABP): longitudinal hematological and
  steroidal biomarker profiling since 2008.
```

---

## EPO and Blood Doping

### Erythropoietin Biology

```
ERYTHROPOIETIN (EPO) PATHWAY:

  HYPOXIA SENSING:
  Low O₂ in tissue (altitude, anemia)
    → HIF-1α (Hypoxia-Inducible Factor) stabilized
      (normally degraded by VHL/PHD2 ubiquitination)
    → HIF-1α + HIF-1β → nucleus
    → Binds HRE (Hypoxia Response Element) on EPO gene
    → EPO transcription ↑ (primary site: kidney peritubular cells)
    → EPO secreted → bone marrow

  EPO RECEPTOR (EPOR) SIGNALING:
  EPO binds EPOR (JAK2-associated)
    → JAK2 dimerization → STAT5 phosphorylation
    → STAT5 dimer → nucleus → erythroid differentiation genes
    → Red blood cell precursor proliferation and differentiation
    → Mature RBC released (7–10 days after stimulus)
    → Hemoglobin rises over 3–6 weeks of EPO treatment

  NET PERFORMANCE EFFECT:
  More RBCs → more hemoglobin → more O₂ carrying capacity
  → VO2max increase: 5–10% per 1 g/dL Hb increase
  For endurance performance: ~1% change in VO2max ≈ meaningful
```

### Detection of EPO

```
THE DETECTION CHALLENGE:

  rhEPO (recombinant human EPO) is structurally nearly identical
  to endogenous EPO. The amino acid sequence is the same.
  Differences: glycosylation patterns (carbohydrate side chains)
               slightly differ by production system.

DETECTION METHODS:
  Urine isoelectric focusing (IEF):
    Developed 2000 (Sydney Olympics, but retroactive positives).
    Endogenous EPO: acidic isoforms (more sialic acid residues).
    rhEPO: slightly more basic band pattern on electrophoresis gel.
    Still gold standard for direct detection.
    Limitation: detectable for only ~3–4 days after subcutaneous dose.
                Athletes microdose strategically.

  Direct EPO in blood:
    ELISA-based; detects lower concentrations.
    Combination with urine test for improved window.

  MICRO-DOSE EPO:
  Modern strategy: very low doses, every 2–3 days.
  Hematocrit stays near 50% limit; EPO clears before testing.
  Blood passport catches the cumulative biomarker elevation.
  Direct EPO test still the gold standard but micro-dose window is narrow.

INDIRECT MARKERS (Biological Passport hematological module):
  Hemoglobin (Hb): direct O₂ carrier; rises with EPO.
  Hematocrit (Hct): % volume of RBCs; formerly a simple limit.
  Reticulocytes %: immature RBCs — high during active EPO stimulation;
                   paradoxically LOW shortly after EPO cessation
                   (feedback suppression of endogenous EPO).
  Reticulocyte-hemoglobin parameter: the "OFF-score."
  Abnormal Blood Profile Score (ABPS): Bayesian model.

  BIOLOGICAL PASSPORT PRINCIPLE:
  Not detecting the substance — detecting the BIOLOGICAL EFFECT.
  Each athlete has their own longitudinal passport.
  Statistical model: adaptive model of individual variation.
  Alert if parameters exceed individual's 99% confidence limits.
  Governed by ABP Operating Guidelines; Adaptive Model (ADAMS).
  First anti-doping passport sanctions: 2010–2011 (cycling).
```

### Autologous Blood Transfusion

```
BLOOD TRANSFUSION DOPING:
  Heterologous (donor blood): detectable by flow cytometry (two
  distinct RBC populations with different antigens/ages).
  Banned since 1985; easily detected; rarely used.

  Autologous (own blood): athlete stores own blood, reinfuses
  before competition. Hematocrit rises 3–5% per unit.
  UNDETECTABLE BY DIRECT METHODS (same DNA, same antigens).
  Only detectable via biological passport — sudden rise in RBC
  parameters not consistent with natural altitude acclimatization.

  Hypoventilation training / altitude tents:
  Technically not doping; legal.
  "Live high, train low" produces ~same effect as mild EPO.
  Effect: 3–5% VO2max increase.
  The legal version of what EPO was used for.
```

---

## Anabolic Androgenic Steroids (AAS)

### Mechanism

```
ANDROGEN RECEPTOR (AR) PATHWAY:

  Testosterone (endogenous) or synthetic AAS
    → Enters cell (lipophilic — crosses membrane passively)
    → Binds AR in cytoplasm
    → AR-AAS complex: heat shock proteins dissociate
    → Complex translocates to nucleus
    → Binds ARE (Androgen Response Element) on target genes
    → Transcription of:
        Myosin heavy chain, IGF-1, satellite cell activation genes
        (anabolic response)
        Also: sebaceous glands (acne), prostate, hair follicles
        (androgenic response)

  ANABOLIC:ANDROGENIC RATIO:
  Testosterone (reference): 1:1
  Nandrolone (Deca-Durabolin): 10:1 (more anabolic, less androgenic)
  Stanozolol (Winstrol): 30:1
  These ratios are approximate (in-vivo response differs from assay).

EFFECTS ON PERFORMANCE:
  Lean mass: +5–10 kg over a cycle; persists partially post-cycle.
  Strength: 5–20% 1RM increases in controlled trials.
  Recovery: accelerated protein synthesis → can train more frequently.
  All effects synergistic with resistance training.

ADVERSE EFFECTS:
  HPTA suppression: exogenous androgens → GnRH/LH/FSH suppression
    → testicular atrophy, oligospermia/azoospermia.
    May be partially reversible; recovery 6–24 months post-cycle.
  Cardiovascular: HDL decrease (-20 to -50%), LDL increase,
    left ventricular hypertrophy (pathological), cardiomyopathy.
    Long-term AAS users: significantly elevated cardiovascular mortality.
  Hepatotoxicity: oral 17α-alkylated AAS (methyltestosterone, stanozolol)
    — liver stress; peliosis hepatis; rare hepatocellular carcinoma.
    Injectable esters: much lower hepatic stress.
  Women: virilization (irreversible voice deepening, clitoral enlargement).
  Adolescents: premature epiphyseal closure → stunted height.
  Psychiatric: "roid rage" is anecdotal and inconsistent in controlled
    trials; dependence and withdrawal depression are better documented.
```

### Detection

```
TESTOSTERONE DETECTION:

  TESTOSTERONE/EPITESTOSTERONE (T/E) RATIO:
  Endogenous T:E ratio ≈ 1:1 (range 0.5–3.5).
  Exogenous testosterone administration: T rises; E remains stable.
  WADA threshold: T/E > 4:1 triggers investigation (not automatic positive).
  Some athletes are natural high ratios (polymorphism in UGT2B17 gene
  — the conjugation enzyme for testosterone glucuronide).
  High UGT2B17 variants: naturally higher T/E; exogenous harder to detect.

  ISOTOPE RATIO MASS SPECTROMETRY (IRMS):
  The definitive test when T/E elevated.
  Carbon isotope ratio (δ¹³C):
  Pharmaceutical testosterone: synthesized from plant sterols
    (soy/yam) → depleted ¹³C (more ¹²C) due to C3 plant photosynthesis.
  Endogenous testosterone: ¹³C ratio reflects dietary input.
    Omnivore diet: intermediate ¹³C.
    Athlete who consumes large amounts of C4 crops (corn, sugarcane):
    naturally more depleted ¹³C — can complicate interpretation.
  IRMS result: δ¹³C of the testosterone metabolite vs. endogenous
    reference compound (5β-pregnane-3,20-dione) — a steroid not
    derived from exogenous testosterone.
  If δ¹³C(testosterone) - δ¹³C(reference) < -3‰: positive.
  This is the gold standard for exogenous testosterone confirmation.

  DESIGNER STEROIDS:
  Molecules not yet on the prohibited list or modified to evade
  current detection methods.
  Examples: THG (Tetrahydrogestrinone — BALCO scandal 2003);
            clostebol, trenbolone derivatives.
  Detection lag: new compounds found in USADA/WADA research;
                 specific metabolite identification published;
                 detection method validated and deployed.
  Cat-and-mouse with detection chemistry.
```

---

## Human Growth Hormone (GH)

```
GH/IGF-1 AXIS:

  Hypothalamus: GHRH → Pituitary
  Pituitary: GH pulsatile release (sleep > waking; exercise > rest)
  Liver + peripheral tissues: IGF-1 production
  IGF-1: primary mediator of GH anabolic effects

  GH EFFECTS ON BODY COMPOSITION:
  Increases: lean mass (fluid + protein), bone density, lipolysis.
  Decreases: fat mass (particularly visceral fat).
  Does NOT consistently increase STRENGTH in controlled trials.
  Subjects: well-trained athletes show smaller responses than sedentary.
  Conclusion: GH improves body composition; performance effect unclear
              and smaller than AAS.

  GH AS DOPING:
  Used since 1980s; became available as recombinant GH (rhGH, Humatrope)
  after 1985. Previously: cadaveric pituitary GH (CJD risk).
  Detected poorly for years; prohibited since 1989 but undetectable
  until 2000s.

DETECTION METHODS:
  ISOFORM DIFFERENTIAL IMMUNOASSAY ("GH-2000" test):
  Pituitary secretes GH as mixture of isoforms: primarily 22 kDa,
  plus 20 kDa and other forms.
  rhGH: almost entirely 22 kDa (recombinant process yields single isoform).
  After rhGH injection: 22 kDa proportion rises → ratio of 22 kDa:total GH
  deviates from normal.
  Detection window: 24–36 hours after injection.
  Limitation: requires blood; narrow window.

  BIOMARKER PANEL ("GH-2004" test):
  Measures GH-responsive biomarkers that change over weeks:
    IGF-1: rises with GH use, stays elevated for days-weeks.
    P-III-NP (Procollagen type III N-terminal propeptide): bone/connective
    tissue synthesis marker; rises with GH treatment.
    BAP (Bone Alkaline Phosphatase): bone formation marker.
  Algorithm: combination of biomarkers vs. sex/age norms.
  Detection window: up to 2 weeks — much longer than isoform test.
  GH-2000 and GH-2004 used in combination for maximum window.
```

---

## Beta-2 Agonists

```
BETA-2 AGONISTS:
  Therapeutic use: asthma and exercise-induced bronchoconstriction.
  Mechanism: β₂ receptor agonism → bronchodilation (airway smooth muscle).
  Common: salbutamol (albuterol), formoterol, salmeterol, terbutaline.

  WHY ATHLETES ABUSE THEM:
  At high systemic doses (IV or oral): anabolic effect via β₂ receptors
  in skeletal muscle → cAMP → protein synthesis.
  Effect smaller than AAS but detectable.
  Clenbuterol (not approved for human use): strong β₂ agonist;
  historically used for fat loss + lean mass retention.
  Clenbuterol contamination in meat (especially in Mexico, China):
  documented cases of inadvertent positives in athletes.

  WADA STATUS:
  Salbutamol: permitted by inhalation (therapeutic use) up to 1,600 μg/day.
              Urinary threshold: 1,000 ng/mL.
              Oral salbutamol produces higher urinary levels than inhaled.
  Formoterol: permitted by inhalation up to 54 μg/day; urinary threshold.
  Salmeterol: permitted by inhalation; no threshold (low systemic exposure).
  Clenbuterol: prohibited at all times (not approved therapeutic).

  THERAPEUTIC USE EXEMPTION (TUE):
  Athletes with documented asthma/EIB can apply for TUE to use
  otherwise prohibited substances. TUE granted based on medical evidence.
  Controversy: high prevalence of asthma diagnoses in elite endurance
  athletes (vs. general population) — some real, some questioned.
```

---

## The Biological Passport

```
ATHLETE BIOLOGICAL PASSPORT (ABP) — ARCHITECTURE:

  MODULES:
  1. Hematological: hemoglobin, hematocrit, reticulocytes, ABPS, OFF-score.
  2. Steroidal: testosterone, epitestosterone, T/E ratio, LH, DHEA-S,
                 androsterone, etiocholanolone — longitudinal patterns.
  3. Endocrine (developing): GH-related biomarkers.

  DATA COLLECTION:
  Anti-doping organizations collect blood/urine according to testing pools.
  Registered Testing Pool (RTP): elite athletes required to submit whereabouts
  (location for 60-minute window per day).
  Out-of-competition testing: unannounced; required for hematological passport.
  ADAMS: WADA's Anti-Doping Administration and Management System.

  STATISTICAL MODEL (Adaptive Bayesian):
  Population prior: based on sport, sex, altitude, age.
  Individual posterior: updated each time a sample is collected.
  Alert threshold: 99% upper/lower limits on individual's model.
  Expert panel review: if alert triggered → 3 hematological experts
  examine blindly; consensus required for AAF (Adverse Analytical Finding).

  WHEREABOUTS SYSTEM:
  Elite athletes must file whereabouts quarterly in ADAMS.
  60-minute daily window (fixed location for testing).
  3 "filing failures" or "missed tests" in 12 months = violation.
  Privacy controversy: constant location tracking.
  Legal challenges in several jurisdictions.

CASE STUDY — LANCE ARMSTRONG:
  7 Tour de France wins (1999–2005); one of the most tested athletes.
  USADA Reasoned Decision (2012): detailed 202-page investigation.
  Evidence:
    - Teammate and staff testimony (Floyd Landis, Tyler Hamilton, Johan Bruyneel).
    - Physiological data showing hematocrit manipulation.
    - EPO and blood doping program run by Dr. Michele Ferrari.
    - The biological passport did not exist in the 2000s; post-hoc analysis
      of stored samples showed EPO positives.
  Armstrong stripped of all results; banned for life (2012).
  Key lesson: the passport is most effective going forward (longitudinal);
  the pre-passport era had very limited detection capability.

  ANALYTICAL FAILURE POINT: Armstrong's era had the T/E ratio test and
  IEF for EPO, but the testing program had systemic failures — sample
  handling, transparency, and institutional corruption (French lab leak
  allegations, Hein Verbruggen/UCI cover-up allegations per USADA).
```

---

## Gene Doping

```
GENE DOPING — THEORETICAL AND EMERGING:

  DEFINITION (WADA): "the non-therapeutic use of cells, genes, genetic
  elements, or of the modulation of gene expression."

  WHY IT IS THEORETICALLY ATTRACTIVE:
  EPO gene delivered via viral vector → cells produce EPO continuously.
  No injectable drug to detect.
  IGF-1 gene: local muscle production → bypass circulating detection.
  ACTN3 R577X: natural "sprint gene" — cannot yet be altered safely in adults.
  Myostatin inhibitor genes: myostatin limits muscle growth; blocking it
  (as in Belgian Blue cattle genetics) → massive muscle hypertrophy.

  AAV (ADENO-ASSOCIATED VIRUS) VECTORS:
  Not integrating (mostly episomal); low immunogenicity.
  The standard vector for gene therapy.
  Sickle cell, hemophilia A/B, spinal muscular atrophy: FDA-approved AAV
  gene therapies now exist.
  Off-label/black market gene therapy: documented in bodybuilding community
  (follistatin AAV injections circulating in underground channels ~2010s+).

  DETECTION CHALLENGES:
  The transgene is in the genome → no drug to excrete.
  Detection strategies:
    Transcriptome analysis: unusual gene expression patterns.
    Epigenetic markers: CpG methylation patterns differ between endogenous
    and delivered gene.
    Sequence-based: next-gen sequencing of blood/muscle biopsy to find
    vector sequences or unusual exogenous promoters.
    Muscle biopsy: invasive; not routine testing.

  CRISPR DOPING:
  CRISPR-Cas9 can edit the genome directly.
  Theoretical: edit EPOR gain-of-function (as in Eero Mantyranta's natural
  mutation — Finnish cross-country skier had EPOR mutation giving him
  high hematocrit naturally).
  Detection: sequence-based approach for telltale edit signatures (small
  insertions/deletions at cut site, guide RNA sequences in genome).
  Current status: not yet detected in athletes; technology advancing.

  WADA ROADMAP:
  Gene doping working group; research funding for detection methods.
  Blood and muscle biobank for retroactive testing.
  The threat is real; the detection capability is developing but behind.
```

---

## Detection System Overview

```
SAMPLE COLLECTION:
  Urine: most common. Non-invasive. Detects small molecules and metabolites.
  Blood: required for biological passport, peptide hormones (EPO, GH).
  Both: complementary; WADA requires both for complete passport.

LABORATORY METHODS:

  GC-MS (Gas Chromatography — Mass Spectrometry):
    Gold standard for small molecule steroids, diuretics, stimulants.
    Derivatization: steroids made volatile; separated by GC column.
    MS: molecular fragmentation pattern = fingerprint.
    Sensitivity: sub-nanogram per milliliter.

  LC-MS/MS (Liquid Chromatography — Tandem Mass Spectrometry):
    Peptides and proteins (EPO, GH, insulin, CG, LH).
    No derivatization needed; better for thermolabile compounds.
    Modern workhorse for most doping analysis.

  IRMS (Isotope Ratio Mass Spectrometry):
    See testosterone detection above.
    Measures ¹³C/¹²C ratio; distinguishes plant-derived from human-derived.
    Required for testosterone positive confirmation.

  IEF (Isoelectric Focusing):
    Protein gel electrophoresis for EPO isoform patterns.
    Still gold standard for direct EPO detection.

ACCREDITATION:
  All WADA-accredited labs must meet ISO 17025 + WADA ISL (International
  Standard for Laboratories).
  ~35 labs globally. WADA conducts proficiency testing.
  Lab results: adverse analytical finding (AAF) — then athlete disciplinary
  process (right of analysis of B sample, hearing, appeal to CAS).

THE DECISION FRAMEWORK:
  For most substances: any detectable amount = violation.
  For threshold substances (salbutamol, T/E, caffeine — caffeine removed
  from prohibited list 2004): must exceed threshold.
  Specified substances (lower sanction risk for inadvertent use).
  Strict liability: athlete is responsible regardless of how substance entered.
  Medical exemptions: TUE granted prior to use.
```

---

## Decision Cheat Sheet

| Substance | Mechanism | Why It Works | Detection Method | Window |
|-----------|-----------|-------------|-----------------|--------|
| EPO (rhEPO) | JAK2-STAT5 → erythropoiesis | VO2max ↑ via more RBCs | Urine IEF (direct); Biological Passport (indirect) | 3–4 days (direct); weeks (passport) |
| Autologous blood transfusion | Direct RBC infusion | Hematocrit ↑ | Biological Passport only; no direct test | Passport: weeks |
| Testosterone/AAS | AR → gene transcription | Lean mass, strength, recovery | T/E ratio + IRMS; Steroidal Passport | GC-MS: varies; IRMS: confirmation |
| GH (rhGH) | GH/IGF-1 axis | Body composition (lean up) | Isoform test (blood); Biomarker panel (IGF-1, P-III-NP) | 24–36h (isoform); ~2 weeks (biomarker) |
| Clenbuterol | β₂ agonism → cAMP → protein synthesis | Lean mass, fat loss | LC-MS/MS in urine | Days |
| EPO gene doping | Continuous endogenous production of transgenic EPO | Undetectable by conventional means | Transcriptome; epigenetic markers; biopsy | Research phase |
| Insulin | IGF-1R crosstalk; glucose → glycogen | Recovery; hypertrophy | LC-MS/MS synthetic insulin isoforms | Hours |

---

## Common Confusion Points

**The T/E ratio is not a test for testosterone — it is a test for exogenous testosterone**: endogenous testosterone fluctuates but epitestosterone tracks it. A high T/E ratio (>4:1) means testosterone has risen disproportionately to epitestosterone, suggesting exogenous source. The IRMS then confirms by carbon isotope ratio — the actual definitive test.

**EPO is legal as a therapeutic drug**: erythropoietin is used clinically for anemia of chronic kidney disease, cancer-related anemia. The same molecule is prohibited in sports. The WADA framework prohibits performance-enhancing use, not the molecule itself in a clinical context. A cancer patient receiving EPO is not doping.

**The biological passport does not detect the drug**: it detects the physiological consequences of doping. This is detection by inference. The advantage is a longer detection window. The limitation is that natural outliers (altitude training, high altitude residence, polycythemia vera) can produce passport alerts without doping. Expert panel review exists to adjudicate these cases.

**Strict liability creates harsh outcomes for contamination cases**: an athlete who tests positive due to contaminated meat (clenbuterol in Mexico) or contaminated supplement still faces a violation. Strict liability means intent is irrelevant to the violation finding; intent is relevant to the sanction length. Contamination can reduce sanctions (2 years → lower) but does not excuse the positive.

**Lance Armstrong's era was not caught by the biological passport**: the passport did not exist during his TdF wins. He was brought down by witness testimony, financial investigation, and retroactive analysis of stored samples using methods not available at the time of collection. The passport framework was designed to prevent a repeat, not to retroactively convict.

**GH does not reliably improve performance in controlled trials**: the ergogenic effect of GH on strength and power is weak in well-trained athletes. It improves body composition (lean mass up, fat down) and sprint performance modestly. The belief that GH dramatically improves performance is not well-supported by RCTs; the effect is much smaller than EPO or AAS. Athletes use it partly for body composition and partly due to belief amplification.
