# Psychology — Overview

## The Big Picture

Psychology is the scientific study of behavior and mental processes. It occupies
awkward terrain between biology and social science, using methods borrowed from both.
The replication crisis exposed how much of the field's apparent consensus was methodological
artifact. What survived is still substantial — and important to know precisely because
of what didn't.

```
+----------------------------------------------------------------------+
|                    PSYCHOLOGY FIELD MAP (LAYERED)                     |
|                                                                      |
|  BIOLOGICAL ◄─────────────────────────────────────────► SOCIAL      |
|                                                                      |
|  Behav. neuroscience ─────────────────────────── Social psychology  |
|  Neuropsychology ──────────────────────────────── Cross-cultural     |
|  Psychopharmacology ───────────────────────────── Organizational     |
|  Evolutionary psych ───────────────────────────── Political psych    |
|  Behavioral genetics ──────────────────────────── Sociology (border) |
|                            │                                         |
|                    COGNITIVE LAYER (center)                          |
|                    Perception · Memory · Attention                   |
|                    Decision-making · Language                        |
|                    (overlaps cognitive-science/)                     |
|                            │                                         |
|  ┌─────────────────────────┴────────────────────────────────────┐    |
|  │          CLINICAL / APPLIED (cross-cutting layer)            │    |
|  │  Clinical · Counseling · Health · I-O · Forensic             │    |
|  │  These apply models from all three layers above              │    |
|  └──────────────────────────────────────────────────────────────┘    |
+----------------------------------------------------------------------+
```

---

## Section 1: The Replication Crisis

The most important context for evaluating psychological findings:

```
  OPEN SCIENCE COLLABORATION (2015):
  Reproduced 100 original psychology studies
  - 97% of originals found significant results (p < 0.05)
  - Only 36% of replications found significant results
  - Mean effect size in replications: ~50% of original

  WHAT COLLAPSED:
  ┌────────────────────────────────────────────────────────────────┐
  │ Social/behavioral priming (money primes greed, etc.)           │
  │ Ego depletion (using self-control depletes "muscle" of         │
  │ willpower) — major industry collapsed in meta-analysis        │
  │ Power posing (Amy Cuddy — testosterone/cortisol changes)       │
  │ Facial feedback hypothesis (pencil in mouth smiling study)    │
  │ "Macbeth effect" (moral cleansing through physical washing)    │
  │ Stereotype threat: effect size much smaller than original claim│
  └────────────────────────────────────────────────────────────────┘

  WHAT SURVIVED:
  ┌────────────────────────────────────────────────────────────────┐
  │ Big Five personality structure and validity                     │
  │ Cognitive dissonance effects (Festinger)                       │
  │ Classical and operant conditioning                             │
  │ Fear conditioning (amygdala) — robust across species          │
  │ Implicit memory and priming (basic, not social)               │
  │ Attachment theory (basic patterns)                             │
  │ Milgram-type obedience (Burger 2009 partial replication)      │
  │ CBT for depression and anxiety — effect sizes hold             │
  │ Intelligence/GMA prediction of outcomes                        │
  └────────────────────────────────────────────────────────────────┘
```

### Why It Happened

```
  STRUCTURAL CAUSES:
  ┌────────────────────────────────────────────────────────────────┐
  │ Publication bias: journals published positive results only     │
  │ → File drawer problem: failed replications unpublished        │
  │                                                                │
  │ Small samples: median psychology study N ~20-40               │
  │ → Underpowered → high false positive rate when replicated     │
  │                                                                │
  │ p-hacking / QRPs (Questionable Research Practices):           │
  │ Run analysis multiple ways; report only significant           │
  │ Add subjects until p < 0.05 (optional stopping)               │
  │ Hypothesize After Results Known (HARKing)                     │
  │                                                                │
  │ Analyst degrees of freedom: many plausible analysis choices;  │
  │ pick the one that works                                        │
  └────────────────────────────────────────────────────────────────┘

  REFORM MEASURES:
  Pre-registration (OSF, AsPredicted): hypotheses + analysis plan before data
  Registered Reports: peer review before data collection; publication guaranteed
  Open data + materials: replication enabled
  Multi-site replications (MANY Labs): different labs run same study
  Effect size emphasis over p-values
```

---

## Section 2: Effect Sizes in Context

```
  COHEN'S d REFERENCE:
  d = 0.2: small (difference between heights of 15/16-yr-old girls)
  d = 0.5: medium
  d = 0.8: large (IQ difference between college students/prison inmates)

  TYPICAL PSYCHOLOGY EFFECT SIZES:
  Social priming effects (mostly failed): ~d=0.3 claimed → ~0 replicated
  Stereotype threat: original d~0.7 → meta-analytic ~0.3–0.4
  CBT for depression: d~0.7–1.0 (one of the strongest effects)
  Big Five predicting job performance: r~0.2–0.5 depending on facet
  GMA predicting job performance: r~0.51 (robust)

  PRACTICAL SIGNIFICANCE ≠ STATISTICAL SIGNIFICANCE:
  With N=10,000, r=0.02 is statistically significant (p<0.05)
  But r=0.02 explains 0.04% of variance → practically trivial

  RULE OF THUMB: Before believing a psychology result:
  - Was it pre-registered?
  - Has it been independently replicated?
  - What is the effect size (not just significance)?
  - What is the sample (WEIRD?)
```

---

## Section 3: Historical Lineage

```
  PSYCHOLOGY HISTORY:
  ┌────────────────────────────────────────────────────────────────┐
  │ 1879 Leipzig: Wundt's first psychology lab                     │
  │ Structuralism (Wundt/Titchener): introspection to map mental  │
  │ elements; limited scientific traction                          │
  │                                                                │
  │ 1900s: Functionalism (James): what does mind DO? → adaptive   │
  │ Psychoanalysis (Freud): unconscious drives; clinical influence │
  │                                                                │
  │ 1920-1960: BEHAVIORISM (Watson/Skinner)                        │
  │ "Psychology should be a science of behavior, not mind"        │
  │ S-R (stimulus-response) associations; conditioning            │
  │ Mind as black box; reject introspection                        │
  │                                                                │
  │ 1956: COGNITIVE REVOLUTION                                     │
  │ Miller (7±2), Chomsky critique of Skinner, Simon/Newell AI    │
  │ Information processing models; mental representations OK again │
  │                                                                │
  │ 1980s+: Social-cognitive, evolutionary, neuroscience integration│
  │ Gene-environment interaction research                          │
  │                                                                │
  │ 2010s+: Replication crisis → reform → more rigorous science   │
  └────────────────────────────────────────────────────────────────┘
```

---

## Section 4: Key Methodological Tensions

### WEIRD Problem

```
  HENRICH/HEINE/NORENZAYAN (2010): "The Weirdest People in the World?"

  96% of psychology studies use Western/Educated/Industrialized/Rich/Democratic
  samples, yet claim universal human nature

  DOCUMENTED VARIATION:
  Visual perception: Müller-Lyer illusion — Western populations see it;
                    Zulus and Namibians much less susceptible
  Fairness norms: Ultimatum game — Western students reject "unfair" offers;
                  some societies accept ANY positive offer (rational)
  Moral psychology: harm/care vs purity/authority vary dramatically
  Conformity: Asch experiments replicate less in individualistic cultures
  Perception: figure vs ground emphasis (Norenzayan/Masuda — East vs West)

  IMPLICATION: Treat many "universal" psychological findings with caution;
  replication in diverse populations essential
```

### Nature vs Nurture

```
  FALSE DICHOTOMY:
  Every behavioral trait is BOTH genetic AND environmental
  Heritability (h²) = proportion of variance due to genetic differences
  h² is NOT a fixed property of a trait — it depends on the range
  of environments in the sample

  Gene × Environment (G×E) interaction:
  Some genes expressed only in certain environments
  MAOA ("warrior gene") + childhood abuse → aggression (replicated weakly)
  Serotonin transporter (5-HTTLPR) + stress → depression — failed to replicate

  BEHAVIORAL GENETICS LESSONS:
  - Almost every trait is substantially heritable (~30-70%)
  - Shared environment (growing up in same home) matters surprisingly little
    for personality, IQ, many outcomes in adulthood
  - Non-shared environment (experiences that differ between siblings) matters more
  - Many specific candidate genes (GWAS) have tiny effects
```

---

## Module Map

| Module | Topic | Key Concepts |
|--------|-------|-------------|
| `01-SOCIAL-PSYCHOLOGY` | Conformity, obedience, attribution, attitude | Asch, Milgram, FAE, dissonance, SIT |
| `02-PERSONALITY` | Big Five, heritability, Dark Triad | OCEAN, NEO-PI-R, stability, MBTI critique |
| `03-CLINICAL` | Disorders and treatments | DSM-5, CBT/DBT/ACT, effect sizes, psychopharmacology |
| `04-ORGANIZATIONAL` | I-O psychology, selection, performance | GMA validity, structured interviews, JD-R, burnout |
| `05-PERSUASION-INFLUENCE` | Cialdini, ELM, disinformation | 6 principles + mechanism, prebunking, nudge theory |
| `06-HEALTH-STRESS` | HPA axis, allostatic load, well-being | Cortisol, ACEs, resilience, PERMA, mindfulness |

---

**Formal bridge:** Psychology's experimental methodology is identical to the
software engineering empiricism you already use. Hypothesis testing is A/B testing.
Statistical controls are the equivalent of holding variables constant in a system
experiment. Effect sizes map to practical significance metrics — the difference
between "this feature lifted conversion by 0.001%" (statistically significant in a
large log) and "this feature lifted conversion by 15%." Pre-registration maps to
committing to a success criterion before running the experiment, which any rigorous
A/B test framework requires. The replication crisis is the field's version of
discovering that most internal benchmarks don't hold up under production load: the
measurement instrument (p-hacking in lab conditions with N=30 undergrads) was optimized
for generating publishable results, not for producing generalizable knowledge. The
reforms — pre-registration, open data, multi-site replication, effect sizes over p-values
— are the same principles as rigorous experiment design in systems engineering.

## Decision Cheat Sheet

**Evaluating a psychology claim — checklist:**

| Gate | Check | Fail condition |
|------|-------|----------------|
| Pre-registration | Was the hypothesis registered before data collection? | Post-hoc hypotheses may be HARKing |
| Independent replication | Has it replicated in at least 2 independent labs? | Single-study findings are provisional |
| Effect size | Is d or r large enough to matter for your application? | d < 0.2 or r < 0.1 rarely matters practically |
| Sample | WEIRD? College undergrads? US only? | Generalization to other populations is unclear |
| Lab vs field | Does it replicate outside controlled conditions? | Lab effects often shrink in field settings |

**What to use when:**

| Question | Evidence-Based Answer |
|---|---|
| Which psychological findings are reliable? | Big Five, conditioning, cognitive phenomena, clinical CBT effects |
| Which famous findings failed replication? | Ego depletion, power posing, social priming, some stereotype threat magnitudes |
| Best predictor of job performance? | GMA (general mental ability) r~0.51; structured interviews r~0.58 |
| Does personality predict outcomes? | Yes — Conscientiousness predicts job performance, longevity; Neuroticism predicts mental health |
| Do MBTI types predict anything? | No — poor reliability and validity; not used by personality researchers |
| Is mindfulness evidence-based? | Moderate effects on anxiety/depression/pain; hype exceeds evidence for many claims |
| Best treatment for depression? | CBT (d~0.7-1.0); medication (similar); combined superior for severe; CBT-I for sleep-related |

---

## Common Confusion Points

**Replication crisis ≠ psychology is fake**: it means specific claims were overstated and
methodology was insufficient. The methodological problems have been widely identified and
reforms are underway. Robust findings remain robust.

**Heritability ≠ genetic determinism**: h² = 60% for IQ doesn't mean 60% of your
intelligence is fixed by genes. It means 60% of the VARIANCE in IQ in a given population
in a given environment is explained by genetic variance. In a world with no environmental
variation (everyone had identical environments), h² would approach 100% even though
environment still matters enormously.

**Effect size context**: psychology studies routinely report "significant" results that
explain 1-4% of variance. These might be statistically real but practically trivial.
The question is always: is this large enough to matter for any real application?

**p < 0.05 is not "the result is true"**: the p-value is the probability of observing
data this extreme IF the null hypothesis were true. It says nothing directly about the
probability that the hypothesis is true. With multiple comparisons, publication bias,
and p-hacking, the false discovery rate in the literature was estimated at >50% before
reform efforts.
