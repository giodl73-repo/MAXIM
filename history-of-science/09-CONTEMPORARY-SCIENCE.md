# Contemporary Science — Replication Crisis, AI, and the Metascience Turn

## The Big Picture

Science in the 21st century faces structural problems that have always existed but are now documented with enough precision to require systemic response. The replication crisis is not about fraud — it is about how the standard incentive structure and statistical practices of scientific publishing systematically produce false results. AI is beginning to change the epistemic infrastructure of science itself.

```
+------------------------------------------------------------------+
|         CONTEMPORARY SCIENCE -- KEY TENSIONS                     |
+------------------------------------------------------------------+
|                                                                   |
|  STRUCTURAL PROBLEM                REFORM RESPONSE               |
|                                                                   |
|  p-hacking + HARKing               Preregistration               |
|  Publication bias (+results only)  Registered Reports            |
|  Small samples + low power         Power calculations required    |
|  Researcher degrees of freedom     Pre-analysis plans             |
|  Replication not rewarded          Dedicated replication journals |
|  Data not shared                   Open Data requirements        |
|  Peer review: slow/biased/secret   Preprints + open review       |
|                                                                   |
|  AI TRANSFORMATION                                                |
|  AlphaFold2: protein structure solved                             |
|  LLM-assisted hypothesis generation                              |
|  AI-driven materials discovery                                    |
|  Automated literature synthesis                                  |
|  AI-assisted theorem proving                                      |
|                                                                   |
+------------------------------------------------------------------+
```

---

## Layer 1: The Statistical Foundation of the Problem

### Ioannidis (2005) — The Mathematical Argument

John Ioannidis published "Why Most Published Research Findings Are False" in PLoS Medicine (2005). This paper is unusual: its argument is mathematical, not empirical — it argues from the statistics of hypothesis testing that most published findings must be false.

```
IOANNIDIS'S ARGUMENT:

Key variables:
  R = prior probability that a tested relationship is true
       (odds ratio of true to false hypotheses in a field)
  alpha = Type I error rate (false positive rate), typically 0.05
  beta = Type II error rate (false negative rate), typically 0.2
         (statistical power = 1 - beta = 0.8)
  u = bias factor (researcher degrees of freedom, HARKing, etc.)

POSITIVE PREDICTIVE VALUE (PPV):
Probability that a published significant finding is true:

PPV = (1-beta)*R + u*beta*R / (alpha + R*(1-beta-alpha) + u*alpha)
        [true positives]         [false positives]

Simple version (no bias):
PPV = (1-beta)*R / ((1-beta)*R + alpha)

For R=0.1 (10% prior), alpha=0.05, power=0.8:
PPV = 0.8*0.1 / (0.8*0.1 + 0.05*(1-0.1)) = 0.08 / (0.08 + 0.045) = 64%

For R=0.01 (exploratory), alpha=0.05, power=0.5:
PPV = 0.5*0.01 / (0.5*0.01 + 0.05*0.99) = 0.005 / (0.0545) = 9%

INTERPRETATION:
In exploratory fields with many tested hypotheses and low power:
most positive results are false.

THE BIAS TERM:
Researcher degrees of freedom inflate the effective alpha rate.
If alpha_effective = 0.20 instead of 0.05 (due to undisclosed flexibility):
PPV drops substantially.
```

### Base Rate Neglect

The core problem is a **base rate** problem — the same one as the famous "positive HIV test" probability puzzle:

```
BASE RATE NEGLECT:

Suppose: prevalence of HIV = 0.1%
         Test specificity (true positive rate) = 99%
         Test sensitivity (false positive rate) = 1%

Person tests positive. What is the probability they have HIV?
(Answer: ~9%, not 99%)

MEDICAL RESEARCH ANALOG:
Prior probability of hypothesized effect being real: 10%
(Most exploratory hypotheses are wrong)
Test: publish if p < 0.05 (significance test)

Observed positive test (p < 0.05):
Probability the effect is real: NOT 95%

Actual: depends on prior probability and power.
With R=0.1, power=0.5: about 50%.
Exploratory research with low power: flip of a coin whether
a published significant result is true.

WHY THIS IS COUNTERINTUITIVE:
Researchers don't think about the base rate (prior probability)
of their hypotheses being true.
p < 0.05 FEELS like strong evidence.
But p-value is a conditional probability given H0 is true,
not the probability H1 is true.
```

---

## Layer 2: p-Hacking Mechanics

### What p-Hacking Actually Is

p-hacking is not (primarily) deliberate fraud. It is the systematic exploitation of **researcher degrees of freedom** — legitimate-seeming decisions that inflate the false positive rate.

```
RESEARCHER DEGREES OF FREEDOM (Simmons, Nelson, Simonsohn 2011):

In a typical study, researchers make many decisions:
  - Which subjects to include/exclude
  - Which outcomes to analyze (primary vs secondary)
  - Whether to control for covariates (and which ones)
  - When to stop collecting data
  - How to handle outliers
  - Which statistical test to use
  - Whether to combine or split conditions

EACH DECISION:
If made after looking at the data, can be used to "find"
significance. Individually, each seems reasonable.
Collectively: the effective alpha is no longer 0.05.

SIMULATION RESULT (Simmons et al.):
Two conditions, no real effect.
Researcher with full degree of freedom (stops when p<0.05,
tries both ANOVAs and t-tests, controls for gender if it
helps, removes 2 most extreme subjects):
~60% chance of reporting p < 0.05 for a null result.

Nominal alpha = 0.05
Actual false positive rate = 60%
Factor of 12x inflation.
```

### The Garden of Forking Paths

Andrew Gelman's concept: researchers don't deliberately cheat. They navigate a garden of forking paths — multiple decision points where each choice seems defensible, but the path taken is influenced by the data itself.

```
FORKING PATHS EXAMPLE:

Study: does power pose affect cortisol? (Carney et al. 2010)

Decision tree:
Start
  |
  +-- Which cortisol measure? (before-after, % change, absolute)
  |     |
  |     +-- When to exclude outliers?
  |           |
  |           +-- Which covariates? (gender, BMI, time of day, ...)
  |                 |
  |                 +-- One-tail or two-tail test?

Each path produces a different p-value.
The researcher follows the path that "looks interesting."
The reported path is not the only one tried -- just the best.

WHAT WAS ACTUALLY DONE:
The researcher may have genuinely not tried all paths.
But unconscious hypothesis-confirming choices guide the path.
The resulting p-value is not from a single pre-specified test --
it is the best of many implicit comparisons.

This is like testing a coin 100 times, selecting the 5 runs
where it came up heads 7 times in a row, and reporting
"significant evidence of bias." Technically each run was
a real experiment. The selection invalidates the inference.
```

### p-Value Misinterpretation

```
WHAT p < 0.05 MEANS:
"If the null hypothesis were true, the probability of
observing data at least this extreme is less than 5%."

WHAT p < 0.05 DOES NOT MEAN:
- "The probability that H0 is true is 5%"
- "The probability that H1 is true is 95%"
- "The effect is large or important"
- "The result will replicate"
- "The study is well-designed"

THRESHOLD FETISHISM:
The 0.05 threshold was set by Fisher (1925) as a rough guide.
Fisher: "The convenient hypothesis... that the result is
not due to chance... [is] that the observed result is at
the 5% level of significance."
Fisher NEVER said p < 0.05 is a publication threshold.

JOURNAL PRACTICE:
p < 0.05: publishable (significant!)
p = 0.051: not publishable (not significant)
Difference in underlying evidence: essentially zero.
Publication discontinuity at p = 0.05 is clearly visible
in published p-value distributions.
```

---

## Layer 3: HARKing and Publication Bias

### HARKing

**HARKing** = Hypothesizing After Results Known (Kerr, 1998). The practice of presenting post-hoc hypotheses as a priori predictions.

```
HARKING MECHANISM:

1. Explore data: try many analyses.
2. Find something significant (real or spurious).
3. Write paper AS IF you had predicted this a priori.
4. Reviewer doesn't know what was explored vs predicted.

HOW HARKING INFLATES FALSE POSITIVES:

True exploratory analysis with 20 comparisons:
Expected false positives at alpha=0.05: 1 per 20 comparisons

If you explore 20 hypotheses and report the 1 that hits:
Reported p < 0.05 but true alpha used = 1.0 (you were guaranteed
to find something if you tried enough)

COMPARED TO CONFIRMATORY RESEARCH:
Confirmatory: pre-specified hypothesis, collect data, test once.
Exploratory + HARKed as confirmatory: same statistical format,
radically different evidential value.
Readers can't tell the difference.

LEGITIMATE VERSION:
"In an exploratory analysis, we found [effect]. This should be
treated as hypothesis-generating, not confirmatory."
HARKing removes this qualifier.
```

### Publication Bias

```
THE FILE DRAWER PROBLEM (Rosenthal, 1979):

Suppose: no effect exists.
Run 20 independent studies, each at alpha=0.05.
Expected false positives: 1 study.

If:
  - The 1 false positive gets published (significant result)
  - The 19 null results go in file drawers (unpublished)

Reader sees: 1 published study showing the effect.
Infers: effect is real.
Reality: 5% false positive rate doing exactly what it should.

SCALE OF THE PROBLEM:
Survey of psychology journals: 97% of results are significant.
If there were no publication bias, you'd expect ~65-70%
significant results (assuming researchers study real effects).
The gap is massive.

FUNNEL PLOT ASYMMETRY:
In meta-analysis, plot each study's effect size vs sample size.
If no bias: symmetric distribution around true effect.
If publication bias: small negative studies absent (file drawer);
funnel is asymmetric.
Egger test: formal test for funnel asymmetry.
```

---

## Layer 4: Replication Projects

### The Reproducibility Project: Psychology

Brian Nosek led the Open Science Collaboration's Reproducibility Project (2011-2015): replicated 100 published psychology studies.

```
RESULTS (Science, 2015):

Of 100 replicated studies:
  39 replicated (significant effect in same direction)
  61 failed to replicate (or got smaller effect)

CRITERIA:
Original p < 0.05: 97 of 100
Replication p < 0.05: 36 of 100
Significant effect in same direction AND CI overlap: 47 of 100
Replication effect size relative to original: ~50% on average

INTERPRETATION:
Not that 61% of original findings are false.
Could be: smaller samples in replications, different populations,
subtle procedural differences, regression to the mean
(original effect sizes were inflated by publication bias).

BUT: the gap is large enough to be a genuine problem.
The average effect in replications is ~half the original.
This is consistent with publication bias + p-hacking inflating
the original effects.
```

### Field-Specific Failure Rates

```
REPLICATION RATES BY FIELD:

Social priming (powerful subliminal cues affecting behavior):
~0% replication in independent pre-registered studies.
E.g.: "money priming" makes people more selfish (Kathleen Vohs):
      meta-analysis: no effect when pre-registered.
E.g.: "professor prime" improves quiz performance:
      multiple failures to replicate.

Cancer biology:
Begley & Ellis (2012): Amgen tried to replicate 53 landmark
cancer biology papers. Reproduced: 6 out of 53 (11%).
These were papers that had influenced drug development programs.

Nutrition epidemiology:
"Coffee causes cancer" / "Coffee prevents cancer":
most findings from observational studies do not replicate.
Confounders (smokers drank more coffee historically) explain many.

Preclinical drug development:
"Valley of death": ~90% of drugs that succeed in animal studies
fail in human trials. Partly replication failure of animal models.
```

---

## Layer 5: Structural Reforms

### Preregistration

Preregistration means publicly registering your hypothesis and analysis plan before collecting data. Key platforms:

```
PREREGISTRATION PLATFORMS:

OSF (Open Science Framework): osf.io
  General purpose; most fields
  Time-stamped protocol registry
  Public or embargoed (embargoed: private until paper submitted)

AsPredicted: aspredicted.org
  Simple 8-question format
  Fast; minimalist
  Increasingly required by some journals

ClinicalTrials.gov:
  Required for human clinical trials (FDA mandate since 2007)
  Prior to trial start: hypothesis, endpoints, sample size
  Reduces outcome switching (registering different primary
  endpoint after seeing which one was significant)

WHAT PREREGISTRATION PREVENTS:
- HARKing (can verify predictions were made before data)
- Outcome switching (primary endpoint locked in)
- Optional stopping (sample size pre-specified)
- Covariate fishing (specified in advance)

WHAT IT DOESN'T FIX:
- Poorly designed studies still preregistered
- Researcher can run un-preregistered exploratory analysis
  and report as separate paper
- Adherence not always verified
```

### Registered Reports

Registered Reports take preregistration further: the journal makes a **conditional acceptance decision based on the methods alone**, before data collection.

```
REGISTERED REPORTS WORKFLOW:

Stage 1: Author submits hypothesis and methods
  Reviewers evaluate: Is the question important? Is the design
  adequate to answer it? Is the analysis plan appropriate?
  Journal: conditional acceptance (IPA -- In Principle Acceptance)

Stage 2: Author collects data and reports results
  Journal: accepts paper regardless of outcome
  (if methods followed as preregistered)

WHY THIS FIXES PUBLICATION BIAS:
Null results get published (conditional acceptance doesn't
depend on whether H1 was supported)
Underpowered studies not accepted (reviewers evaluate power)
HARKing structurally impossible (analysis plan pre-specified)

EVIDENCE:
Studies accepted as Registered Reports have higher replication rates.
Effect sizes smaller (less publication bias inflation).
More null results published.

ADOPTION:
300+ journals now offer Registered Reports option (as of 2024).
Not yet dominant -- most papers still traditional.
```

---

## Layer 6: AI in Science

### AlphaFold2 — A Genuine Paradigm Shift

The protein folding problem: given an amino acid sequence, predict the 3D structure of the resulting protein.

```
HISTORY OF THE PROBLEM:

1961: Anfinsen hypothesis: protein structure is determined by
      amino acid sequence alone (thermodynamic minimum).
      Nobel Prize 1972.

1994: CASP competition begins (Critical Assessment of Structure Prediction)
      Biennial competition: blind prediction of experimentally-determined
      structures from sequence.
      Progress: slow. Best methods ~50% accuracy for some domains.

2018: AlphaFold1 (DeepMind) enters CASP13.
      GDT score: 58.9 (vs 38.8 for second place)
      Significant improvement but not solved.

2020: AlphaFold2 enters CASP14.
      Median GDT score: 92.4
      Most proteins: predicted within experimental error.
      The problem is essentially solved.

2021: AlphaFold2 paper published (Jumper et al., Nature).
      Code and weights released open-source.
      AlphaFold Protein Structure Database: 200+ million structures.
      Previously known structures: ~180,000 (50 years of crystallography).
      AlphaFold structures: millions, from any sequenced organism.
```

### Why AlphaFold2 is Kuhnian

```
KUHNIAN ANALYSIS OF ALPHAFOLD2:

Normal science: biophysics + molecular dynamics + homology modeling
Anomaly: 50 years of effort, fundamental limits on accuracy
Crisis: CASP competitions showing slow progress
Paradigm shift: deep learning replaces physics-based modeling

WHAT CHANGED:
Before: protein structure required years of crystallography
        or cryo-EM per protein, $millions/structure
After: ~minutes per structure, free, open-source

IMMEDIATE SCIENTIFIC IMPACT:
Drug discovery: structure-based drug design now trivially accessible
Molecular biology: function inference from structure
Evolution: comparative proteomics at scale
Medicine: understanding disease mutations via structural effects

THE DEEPER POINT:
AlphaFold2 learned the relationship between sequence and structure
WITHOUT explicit physical modeling.
The network implicitly learned the biophysics.
This challenges the idea that physical understanding is required
for scientific prediction -- a form of Feyerabendian instrumentalism
implemented in silicon.

IS THIS UNDERSTANDING?
The AlphaFold2 network cannot explain WHY a protein folds as it does.
It predicts the structure with high accuracy.
This is the protein folding equivalent of Ptolemy:
excellent prediction, unclear whether it represents understanding.
```

### AI Across Scientific Domains

```
AI IN SCIENCE -- CURRENT STATUS:

STRUCTURAL BIOLOGY:
AlphaFold2 (2021): proteins
RoseTTAFold: alternative architecture (Baker lab)
ESMFold (Meta AI): faster, lower accuracy
RF-Diffusion: protein design (inverse problem)
Status: SOLVED for most proteins; ongoing for complexes, dynamics

MATERIALS SCIENCE:
MatBERT, GNoME (DeepMind, 2023):
  Predicted 2.2 million stable crystal structures
  (vs 48,000 previously known)
  Experimental validation ongoing
Status: major acceleration, validation bottleneck

DRUG DISCOVERY:
Generative models for molecular design (various)
Binding affinity prediction
ADMET (absorption, distribution, metabolism, excretion, toxicity)
Status: meaningful acceleration; clinical trial failure rate unchanged
        (biology validation remains hard)

MATHEMATICS:
LLMs as informal assistants: useful for exploration
Formal verification: Lean, Coq, Isabelle
DeepMind's FunSearch: found new asymptotic bounds for cap set problem
AlphaProof/AlphaGeometry: IMO-level geometry problems
Status: early but genuine; theorem proving more tractable than conjectured

GENOMICS:
Large language models for DNA/RNA sequences (Nucleotide Transformer, etc.)
Predicting regulatory elements
Understanding splicing
Status: active, some validated applications
```

---

## Layer 7: Peer Review — Origins, Problems, Alternatives

### Brief History

```
PEER REVIEW HISTORY:

1665: Philosophical Transactions (Royal Society) -- no formal review
      Henry Oldenburg makes editorial decisions himself

1731: Royal Society of Edinburgh -- referee reports introduced
      First formal peer review by external experts

1830-1900: Gradual adoption of external review
           Referee system becomes standard

1944: Nature adopts external peer review formally

1960s-1970s: Double-blind review introduced
             (reviewer doesn't know author's identity)
             Single-blind still common (reviewer anonymous, author known)

CURRENT SCALE:
~3 million papers published per year
~15 million peer review reports written per year (estimated)
Unpaid labor: reviewers receive no compensation
Time to decision: 3-12 months typical; longer in some fields
```

### Peer Review's Problems

```
PEER REVIEW FAILURES:

SPEED:
Average time submission to publication: 12-18 months
Fastest major journals: 3-6 months
Preprints (arXiv, bioRxiv): immediate

BIAS:
Famous author bias: famous names get easier reviews
Gender bias: women receive harsher reviews for equivalent work
Confirmation bias: reviewers favor results consistent with their views
Novelty bias: novel surprising results accepted over replications

EFFECTIVENESS:
Does peer review actually catch errors?
Mixed evidence. Meta-analyses: peer review modestly improves quality.
Doesn't catch: subtle statistical errors, fabricated data, HARKing
Doesn't catch: papers that replicate badly

SECRECY:
Traditional: reviews are secret, not published
Reviewer has no accountability for poor quality review
Author cannot respond to factually wrong review claims

ALTERNATIVES:
Preprint + post-publication review: arXiv model
  Papers available immediately; community comments over time
  Widely adopted in physics (arXiv since 1991), genomics (bioRxiv, 2013)
  Currently spreading to more fields

Open review: reviews are public (with or without names)
  PeerJ, F1000Research, eLife (after 2022)
  Reviewers accountable; authors can see review quality
  Evidence: review quality improves when public

Registered Reports: review before data collection (see above)

Preregistered replication as review:
  Community-coordinated replications as quality control
```

---

## Layer 8: Metascience

### Science Studying Itself

Metascience — studying science with scientific methods — has become a recognized field:

```
KEY METASCIENCE FINDINGS:

CITATION PRACTICES:
Most-cited papers: not most replicable
Citation does not track truth, tracks influence
Highly cited wrong papers get cited even after retractions

TEAM SCIENCE:
Papers with more authors: higher citations, broader reach
BUT: large author lists obscure individual contributions
Team diversity (gender, institution, discipline) correlates with
higher-quality outputs (more controlled for publication bias)

GEOGRAPHY:
Science is increasingly concentrated in US, China, and a few EU nations.
English language dominance: 90%+ of high-impact papers in English
Scientists in non-English-speaking countries: disadvantaged

REPLICATION RATES VS JOURNAL PRESTIGE:
Counterintuitive: high-prestige journal papers replicate less well.
Explanation: high-prestige journals select for surprising/novel results.
Surprising results have lower prior probability of being true.
More selection pressure for significance means more p-hacking accepted.

FUNDING EFFECTS:
Industry-funded studies show industry-favorable results more than
government-funded studies of same compounds.
Tobacco industry: classic case (internal documents proved bias)
Pharmaceutical industry: publication bias in clinical trials
```

### AI-Accelerated Science — Implications

```
IF AI ACCELERATES HYPOTHESIS GENERATION:

Current situation:
Human scientist generates O(1-10) testable hypotheses per year
Experimental validation: rate-limiting step

AI-accelerated:
LLM explores literature, generates O(1000+) hypotheses
Experimental validation still rate-limiting

IMPLICATION:
The bottleneck shifts from hypothesis generation to experimental validation.
The ratio of false positives generated to validated increases.
Metascience challenges multiply.

FOR FORMAL SCIENCES (mathematics):
AI theorem provers: O(millions) conjectures per day
Human verification: ~1 theorem per mathematician per year
Gap between conjectured and verified grows.
How do we prioritize which AI-generated conjectures to verify?

FOR DRUG DISCOVERY:
GAN-generated molecules: millions per day
Synthesis + bioassay: O(thousands per month) with robotics
Clinical validation: years per compound
The bottleneck is now biology (clinical trials), not chemistry.

EPISTEMOLOGICAL ISSUE:
Science built on human cognitive limits.
Publication + peer review designed for human-scale output.
AI changes scale by orders of magnitude.
Do our epistemological frameworks still work?
```

---

## Decision Cheat Sheet

| You want to understand... | Key concept | Key point |
|---------------------------|------------|-----------|
| Why most research findings might be false | Ioannidis base rate argument | PPV depends on prior probability + power; low prior + high alpha = mostly false |
| What p-hacking actually is | Researcher degrees of freedom | Legitimate-seeming post-hoc decisions that inflate alpha |
| Why HARKing inflates false positives | Exploratory presented as confirmatory | Multiple implicit comparisons hidden; no multiple testing correction |
| What preregistration fixes | Locks hypothesis and analysis plan before data | Prevents HARKing and covariate fishing |
| Why AlphaFold2 is scientifically significant | 50-year problem solved | Deep learning solved protein folding without explicit biophysics; Kuhnian shift |
| What's wrong with peer review | Speed, bias, secrecy, effectiveness | Works better than nothing; poor at catching subtle errors; preprints challenging it |

---

## Common Confusion Points

**The replication crisis does not mean science is broken.** It means the false positive rate in published literature is higher than the nominal p=0.05 implies. Pre-registered, high-powered, direct replications of well-understood phenomena work fine. The crisis is concentrated in exploratory research with low power and high degrees of freedom.

**p-hacking is not usually deliberate fraud.** Most researchers doing it are not consciously manipulating. The decisions are made in good faith; the problem is that the decisions are influenced by the data. The cure is structural (preregistration), not character reform.

**AlphaFold2 did not "solve" protein folding.** It solved protein structure prediction for single proteins in standard conditions with ~98% accuracy. It does not predict protein dynamics, disorder, binding-induced conformational change, membrane protein structures in bilayers, or protein-protein complex structures at the same level. These are active areas.

**Preregistration is not a silver bullet.** A poorly-powered, poorly-designed preregistered study produces bad science reliably. Preregistration ensures you study what you said you'd study; it doesn't guarantee you studied the right thing well.

**The replication crisis is not equally distributed.** Physics (particle, condensed matter, astrophysics) has strong replication norms (independent group replication before major claims) and low crisis. Social psychology, nutritional epidemiology, and preclinical biomedical research have high crisis. Engineering (applied results in controlled settings) less crisis than discovery science.
