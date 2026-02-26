# Neural MT Evaluation and What BLEU Misses

## The Big Picture

```
MT EVALUATION — THE QUALITY MEASUREMENT PROBLEM
════════════════════════════════════════════════════════════════════

  THE FUNDAMENTAL PROBLEM:
  Translation quality has multiple orthogonal dimensions.
  Any single automated metric captures at most a projection.

  DIMENSIONS OF TRANSLATION QUALITY:
  ┌─────────────────────────────────────────────────────────┐
  │ • Adequacy: is the meaning transferred?                 │
  │ • Fluency: does it read naturally in the target?        │
  │ • Faithfulness: are all source elements represented?    │
  │ • Pragmatics: is register, tone, illocution preserved?  │
  │ • Cultural adequacy: appropriate cultural adaptation?   │
  │ • Terminology: domain-appropriate terms used?           │
  └─────────────────────────────────────────────────────────┘

  METRICS CHART:
  BLEU ──────────────────── n-gram overlap (surface)
  METEOR ────────────────── n-gram + synonyms + stems
  chrF ──────────────────── character n-gram overlap
  TER ───────────────────── edit distance
  BERTScore ─────────────── embedding similarity (contextual)
  COMET ─────────────────── trained regression model
  MQM ───────────────────── human annotation framework
  (Human eval) ──────────── ground truth, expensive
```

---

## BLEU: How It Works

BLEU (Bilingual Evaluation Understudy, Papineni et al., 2002) is the most widely used automated MT metric and has been since its introduction.

### The Mechanics

```
BLEU SCORE COMPUTATION
════════════════════════════════════════════════════════════════

  INPUT:
  • Candidate translation (MT output)
  • Reference translation(s) (1+ human translations)

  STEP 1: N-GRAM PRECISION (for n = 1, 2, 3, 4)
  Count how many n-grams in the candidate appear in
  any reference translation.
  Clip count: an n-gram can only match as many times
  as it appears in the reference.

  EXAMPLE:
  Candidate: "the cat the cat sat on the mat"
  Reference: "the cat sat on the mat"
  1-gram "the" appears 3 times in candidate;
  only 2 times in reference → clipped count = 2.
  Without clipping: naive system could repeat "the"
  indefinitely and get high 1-gram precision.

  STEP 2: BREVITY PENALTY
  If candidate is shorter than reference: penalize.
  (Otherwise a system that outputs one correct word
   gets 100% precision)

  BP = 1 if c > r
  BP = e^(1 - r/c) if c ≤ r
  (c = candidate length, r = reference length)

  STEP 3: GEOMETRIC MEAN OF N-GRAM PRECISIONS
  BLEU = BP × exp(Σ wₙ × log pₙ)
  where wₙ = 1/4 (equal weights for n=1,2,3,4)
  and pₙ is the modified n-gram precision for order n

  RANGE: 0 to 1 (sometimes reported as 0-100)
  INTERPRETATION:
  ~0.0: random or completely wrong
  ~0.3: understandable; significant errors
  ~0.5-0.6: close to professional quality (rough guideline)
  ~0.6+: generally professional quality (language-pair dependent)
  1.0: identical to reference (impossible in practice with one reference)
```

---

## BLEU's Known Failures

BLEU has been extensively critiqued since its introduction. The critique is not that it's useless — it correlates reasonably well with human judgment for ranking systems — but that it fails in systematic and important ways:

```
BLEU FAILURE MODES
════════════════════════════════════════════════════════════════

  1. DOES NOT CAPTURE FLUENCY
  Candidate: "sat cat the mat the on the"
  Reference: "the cat sat on the mat"
  BLEU score: high (all unigrams match, several bigrams)
  Human judgment: completely unintelligible

  2. ONE CORRECT TRANSLATION PENALIZES OTHERS
  Reference: "the cat sat on the mat"
  Candidate: "the cat was sitting on the mat"
  BLEU: lower than reference match
  Human judgment: acceptable paraphrase
  The problem: BLEU doesn't know about paraphrase

  3. IGNORES PRAGMATICS AND REGISTER
  Source (formal): "Veuillez agréer l'expression de mes sentiments distingués"
  Reference: "Yours sincerely,"
  Candidate (literal): "Please accept the expression of my distinguished sentiments"
  BLEU: candidate scores low (different from reference)
  Human judgment: candidate is technically accurate but pragmatically wrong —
  no one ends an English business letter that way.
  BLEU cannot detect pragmatic failure.

  4. IGNORES CULTURAL ADEQUACY
  Source mentions "a rice cooker" (culturally familiar in Japan)
  Reference: "a rice cooker"
  Candidate: "a special pot" (culturally adapted)
  BLEU: candidate scores low
  Human judgment: may depend on audience —
  for a Japanese-culture text for a Japanese audience, wrong;
  for explaining the concept to Western readers, possibly right.

  5. IGNORES HALLUCINATION
  Source: "The meeting was on Tuesday."
  Candidate: "The meeting was on Tuesday, and the chairman resigned."
  BLEU: candidate may score normally or low (depending on reference)
  Human judgment: the added information is fabricated —
  critical error in any high-stakes domain.
  BLEU has no mechanism to detect additions that weren't in the source.

  6. GENDER BIAS
  Source (generic masculine in Spanish): "El médico llegó tarde"
  Reference (English): "The doctor arrived late"
  Candidate (gendered): "He arrived late" (male default)
  BLEU: may score fine against "The doctor arrived late"
  Feminist MT critique: NMT systematically defaults to male
  for professional roles, female for service roles.
  BLEU is blind to this.
```

---

## Alternative Metrics

```
MT EVALUATION METRICS — COMPARISON
════════════════════════════════════════════════════════════════

  METEOR (Banerjee & Lavie, 2005):
  ┌──────────────────────────────────────────────────────────┐
  │ Adds to BLEU: synonym matching, stemming, recall         │
  │ Correlates better with human judgment than BLEU          │
  │ More computationally expensive                           │
  │ Language-specific modules (worse for low-resource)       │
  └──────────────────────────────────────────────────────────┘

  TER (Translation Error Rate):
  ┌──────────────────────────────────────────────────────────┐
  │ Edit distance: how many edits needed to go from          │
  │ candidate to reference?                                  │
  │ Allows reordering (with additional cost)                 │
  │ Lower = better; 0 = perfect match; >1 = very bad         │
  │ Good for post-editing time estimation                    │
  └──────────────────────────────────────────────────────────┘

  chrF (Popovic, 2015):
  ┌──────────────────────────────────────────────────────────┐
  │ Character n-gram F-score                                  │
  │ Better for morphologically rich languages                │
  │ (Turkish, Finnish, Czech)                                │
  │ No tokenization required — language-neutral              │
  │ Correlates well with human for many languages            │
  └──────────────────────────────────────────────────────────┘

  BERTScore (Zhang et al., 2019):
  ┌──────────────────────────────────────────────────────────┐
  │ Compare candidate and reference using BERT contextual    │
  │ embeddings rather than surface n-gram overlap            │
  │ Captures semantic similarity even when paraphrased       │
  │ "cat sat on mat" ≈ "feline rested on carpet" (higher     │
  │ score than BLEU would give)                              │
  │ Requires BERT model; computationally heavier             │
  │ Still doesn't capture pragmatics, hallucination          │
  └──────────────────────────────────────────────────────────┘

  COMET (Rei et al., 2020):
  ┌──────────────────────────────────────────────────────────┐
  │ Trained neural model that takes source + candidate +     │
  │ reference and predicts human quality judgment score      │
  │ Trained on direct assessment (DA) human annotations      │
  │ Currently best correlation with human judgments          │
  │ Multiple variants: COMET-DA, COMET-QE (no reference)    │
  │ Requires source sentence (unlike BLEU/METEOR which       │
  │ only need reference)                                     │
  └──────────────────────────────────────────────────────────┘
```

---

## Human Evaluation Protocols

When automated metrics are inadequate, human evaluation is required. The field has developed structured protocols:

```
HUMAN MT EVALUATION FRAMEWORKS
════════════════════════════════════════════════════════════════

  ADEQUACY/FLUENCY (classic):
  Each translation segment rated on:
  • Adequacy (1-5): how much meaning is conveyed?
  • Fluency (1-5): how well-formed is the target text?
  Simple; fast; widely used in early MT evaluation.
  Problem: evaluators don't agree on scale meaning;
  conflates many quality dimensions.

  DIRECT ASSESSMENT (DA) (Graham et al. 2013):
  Rate translation quality on a 0-100 continuous scale.
  Single question: "How adequately does this translation
  express the meaning of the source?"
  Standardized per annotator to handle scale differences.
  Better inter-annotator agreement than 5-point scale.
  Used by WMT as primary human evaluation method.

  MQM (Multidimensional Quality Metrics):
  ┌──────────────────────────────────────────────────────────┐
  │ Hierarchical error typology for professional use:        │
  │                                                          │
  │ ACCURACY (is the source meaning conveyed?)               │
  │   • Mistranslation                                       │
  │   • Addition (content not in source)                     │
  │   • Omission (source content missing)                    │
  │   • Untranslated                                         │
  │                                                          │
  │ FLUENCY (is the target well-formed?)                     │
  │   • Grammar                                              │
  │   • Spelling                                             │
  │   • Punctuation                                          │
  │   • Register (formal/informal mismatch)                  │
  │   • Locale convention (dates, numbers, addresses)        │
  │                                                          │
  │ TERMINOLOGY                                              │
  │   • Inconsistent (same term, different translations)     │
  │   • Incorrect (wrong domain term)                        │
  │                                                          │
  │ SEVERITY: Critical / Major / Minor                       │
  │                                                          │
  │ SCORE: Sum of weighted error penalties                   │
  │                                                          │
  │ Used by: Google, Microsoft, professional LSPs            │
  │ Advantage: actionable for post-editing; specific errors  │
  │ Disadvantage: expensive; requires trained annotators     │
  └──────────────────────────────────────────────────────────┘
```

---

## NMT Hallucination

Hallucination is one of the most serious quality problems in NMT — and is systematically missed by reference-based metrics like BLEU.

```
MT HALLUCINATION — TYPES AND CAUSES
════════════════════════════════════════════════════════════════

  DEFINITION: Output contains content not supported by
  (or contradicted by) the source text.

  TYPES:
  FULL HALLUCINATION: Translation has no relation to source
  (can happen with very short inputs or language pairs
   where the model has poor alignment)

  PARTIAL HALLUCINATION: Most of the translation is correct;
  some elements are invented.
  "The patient was given 500mg of ibuprofen" →
  "The patient was given 500mg of ibuprofen three times a day"
  (three times a day not in source)

  NAME/NUMBER ERRORS: Hallucinated proper nouns or numbers
  common; these are low-frequency in training data and
  model "fills in" plausibly wrong values.

  CAUSES:
  • Exposure to translation of similar text during training
    → model generates likely-sounding text from priors
    rather than strictly decoding the source
  • Attention failure: model stops attending to relevant
    source positions
  • Out-of-domain text: model falls back on language model
    prior when source is unfamiliar

  DETECTION:
  QE (Quality Estimation) models (COMET-QE, TransQuest):
  Score translation quality without reference; trained to
  detect likely errors. Can flag hallucination patterns.

  Source-conditional metrics: metrics that compare
  candidate to source (not reference) to detect
  additions and omissions.

  HUMAN ANNOTATION: Most reliable; not scalable.

  IMPLICATIONS FOR HIGH-STAKES USE:
  Medical, legal, financial MT: hallucination is
  potentially dangerous. BLEU score of 0.6 does
  not mean 0 hallucinations. Human review required
  for high-stakes text.
```

---

## Gender Bias in MT

```
MT GENDER BIAS — THE PROBLEM
════════════════════════════════════════════════════════════════

  SOURCE: Languages with grammatical gender (Spanish,
  French, German, Arabic, Hebrew) encode gender
  in verbs, adjectives, nouns.

  TRANSLATION TO ENGLISH: English lacks grammatical gender;
  pronouns (he/she/they) are the main marker.

  PROBLEM:
  When a gendered pronoun is required in English but
  ambiguous in source, NMT systems use historical
  training data biases:

  Spanish: "El médico llegó tarde. Él/Ella dijo..."
  → English training data: doctors → male
  NMT output: "The doctor arrived late. He said..."
  Ground truth: may be "she said" — impossible to know from source

  DOCUMENTED CASES:
  Google Translate (2018, tested by journalists):
  Turkish (gender-neutral pronoun "o"):
  "O bir doktor" → "He is a doctor"
  "O bir hemşire" → "She is a nurse"
  Systematic male default for high-status professions;
  female default for care professions.

  RESPONSES:
  Google introduced gender-specific translations (2018):
  "He is a doctor / She is a doctor" both offered.
  But this only works when the source clearly disambiguates.

  ROOT CAUSE:
  Training data reflects historical (and current) gender
  representation in professional roles.
  The model learns the correlation; can't "know" the source
  is genuinely ambiguous.

  MEASUREMENT:
  WinoMT benchmark (Stanovsky et al. 2019):
  Test set of gender-balanced professional roles in coreference
  sentences. Used to measure gender bias across MT systems.
```

---

## The Adequacy vs. Fluency Tradeoff

One of the consistent findings in MT evaluation:

```
ADEQUACY vs. FLUENCY TRADEOFF
════════════════════════════════════════════════════════════════

  NMT produces FLUENT output.
  FLUENCY does not imply ADEQUACY.

  CLASSIC EXAMPLES:
  RBMT output: "The minister held yesterday conference
               of the press"
  → Low fluency; medium adequacy (all information present)

  NMT output: "The minister held a press conference yesterday"
  → High fluency; high adequacy (in this case both)

  BUT NMT can also produce:
  NMT output: "The minister held an important press conference"
  → High fluency; LOWER adequacy ("important" not in source)
  The hallucinated "important" is fluent and plausible,
  making it harder for a reader to detect the error.

  THE PARADOX:
  NMT's fluency advantage is also a risk: fluent errors
  are harder to detect than disfluent errors.
  RBMT's ungrammatical output signals "this is a translation;
  check carefully." NMT's fluent output signals "this looks
  normal" — even when it contains errors.

  IMPLICATIONS FOR POST-EDITING:
  Human post-editors find NMT errors harder to catch than
  PBSMT errors, even when NMT has fewer errors per sentence.
```

---

## The Pivot Language Problem

```
PIVOT LANGUAGE IN MT
════════════════════════════════════════════════════════════════

  PROBLEM: Many language pairs have very little parallel
  data (Swahili-Japanese, etc.)

  SOLUTION: Pivot through a third language (usually English)
  Swahili → [English pivot] → Japanese

  QUALITY COST:
  Each translation step introduces errors.
  Pivot MT quality is roughly the geometric mean
  of the two component steps.

  ALTERNATIVE: Zero-shot cross-lingual transfer
  in multilingual models (NLLB-200).
  Quality: usually better than cascaded pivot for
  language pairs covered by multilingual training.

  RELIGIOUS PIVOT PROBLEM:
  For languages where the Bible is the only parallel
  corpus: the "pivot" through English is through
  a biblical register. Domain mismatch for
  everyday translation.

  BACK-TRANSLATION (Sennrich et al. 2016):
  Generate synthetic source-language text by:
  1. Translate target monolingual text into source (MT)
  2. Use (synthetic source, real target) as training pair
  Dramatically improves NMT quality especially for
  high-quality target language output.
  Used by almost all modern MT systems.
```

---

## Where NMT Beats Humans and Where It Fails

```
NMT vs. HUMAN TRANSLATION — HONEST COMPARISON
════════════════════════════════════════════════════════════════

  NMT BEATS HUMAN (or is competitive):
  ┌──────────────────────────────────────────────────────────┐
  │ • Speed: tens of thousands of words per second           │
  │ • Consistency: same source text → same translation       │
  │ • High-resource language pairs (EN-FR, EN-DE, EN-ZH):    │
  │   professional quality on news and technical text        │
  │ • Cost: effectively free after training                  │
  │ • Terminology: if given a glossary, consistent           │
  │   terminology (translation memory equivalent)            │
  └──────────────────────────────────────────────────────────┘

  HUMAN BEATS NMT:
  ┌──────────────────────────────────────────────────────────┐
  │ • Literary translation: style, rhythm, cultural          │
  │   resonance, untranslatables                             │
  │ • Legal and medical text: hallucination risk;            │
  │   human review remains required                         │
  │ • Low-resource languages: NMT quality poor for           │
  │   most African, indigenous, minority languages           │
  │ • Pragmatics and register: irony, humor, implicature     │
  │ • Cultural adaptation: Anthea Bell problems              │
  │ • High-stakes errors: one bad number can be critical     │
  │ • New terminology: domain-specific terms not in          │
  │   training data produce neologisms or hallucinations     │
  └──────────────────────────────────────────────────────────┘

  CURRENT INDUSTRY MODEL:
  NMT → Human post-editing (MTPE)
  Humans review and correct NMT output.
  Faster and cheaper than human translation from scratch.
  MQM used to measure post-editing quality and effort.
  "Fit for purpose" standard: not perfect, good enough
  for the use case.
```

---

## Decision Cheat Sheet

| Metric | What it measures | Misses | Best for |
|--------|-----------------|--------|---------|
| BLEU | Surface n-gram overlap with reference | Fluency, pragmatics, hallucination, synonyms | Ranking systems in development; rough comparison |
| METEOR | N-gram + synonyms + stems + recall | Pragmatics, hallucination, cultural | Better than BLEU for system development |
| chrF | Character n-gram F-score | Pragmatics, hallucination | Morphologically rich languages |
| BERTScore | Semantic similarity via embeddings | Pragmatics, hallucination, cultural | Paraphrase-tolerant evaluation |
| COMET | Learned quality model | Domain shift; new error types | Best automated metric; WMT evaluation |
| MQM | Human error annotation taxonomy | Nothing (it's the ground truth) | Production quality assurance; post-editing |

---

## Common Confusion Points

**BLEU 0.5 does not mean 50% of words are correct**: BLEU is a geometric mean of n-gram precisions with a brevity penalty. A BLEU of 0.5 (score of 50 on 0-100 scale) means something like "the 4-gram precision is reasonable" — but doesn't map linearly to word accuracy. And "word accuracy" itself is the wrong frame (wrong word in the right place is worse than a missing word in some contexts).

**BLEU score 1.0 is impossible in practice**: Even if you submit the reference as your "candidate," a single-reference BLEU with one reference is rarely 1.0 because of tokenization differences. Multi-reference BLEU (more than one human reference translation) gives more room and correlates better with human judgment.

**COMET is not evaluation-neutral**: COMET is trained on human DA annotations from specific language pairs and time periods. It can fail on out-of-domain text, newly coined terminology, and language pairs underrepresented in its training. It is currently the best automated metric, but it is itself a trained model with all of a trained model's failure modes.

**Hallucination in MT is not the same as hallucination in LLMs**: In MT, hallucination means the translation contains content not in the source. In general LLMs, hallucination means the model generates factually incorrect content. They share a mechanism (model generates plausible-sounding text from prior rather than being grounded in input) but in MT the "ground truth" is the source sentence, which is always available. This makes MT hallucination more tractable to detect using source-comparison methods.

**MQM is not a metric — it's a framework**: MQM defines an error typology and severity levels. Different MQM instantiations (used by different companies and research groups) may have different error categories, weights, and thresholds. When someone says "we use MQM," ask which version and what the weights are.
