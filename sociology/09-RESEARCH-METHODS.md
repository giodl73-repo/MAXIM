# Research Methods

## The Big Picture

Sociological methods are a toolkit for generating systematic knowledge about social life. The fundamental choice is between **quantitative** approaches (measure, correlate, generalize) and **qualitative** approaches (interpret meaning, understand context, generate theory). Each answers different kinds of questions and has different validity concerns. Most sophisticated sociology uses both — not to "triangulate" but because different methods access genuinely different aspects of social reality.

```
RESEARCH METHODS — LANDSCAPE:

  QUANTITATIVE                           QUALITATIVE
  ─────────────────────────────────────────────────────────────────
  Survey/questionnaire                   Ethnography/participant observation
  Administrative data                    In-depth interviews
  Experiment (rare in sociology)         Focus groups
  Comparative statistics                 Document/text analysis
  Social network analysis                Historical archives
  Content analysis (quantitative)       Content analysis (interpretive)

  DEDUCTIVE:                             INDUCTIVE:
  Theory → hypothesis → data             Data → patterns → theory
  Test existing theory                   Generate new theory

  Epistemology:                          Epistemology:
  Positivism: social facts are           Interpretivism: social reality is
  measurable; generalizable laws         meaningful; must be understood
  possible                               from within

  MIXED METHODS: use both; integrate findings across approaches
  Historical-comparative: Mill's methods on case studies across time/space
```

---

## Survey Methodology

### Sampling

```
SAMPLING — CONNECTING SAMPLE TO POPULATION:

  PROBABILITY SAMPLING (allows statistical inference):

    Simple random: every member of population has equal probability of selection
      → Theoretical ideal; often impractical (requires complete sampling frame)

    Systematic: every nth member from ordered list
      → Risk: periodic patterns in list can bias

    Stratified: divide population into groups (strata); random sample within each
      → Ensures representation of important subgroups
      → Proportionate: each stratum sampled proportional to size
      → Disproportionate: oversample small strata for analysis; weight back

    Cluster: randomly select groups (schools, districts); then sample within groups
      → Cost-efficient for geographically dispersed populations
      → Inflates standard errors (within-cluster correlation = design effect)
      → Must weight by cluster selection probability in analysis

    Multistage: combination; e.g., random counties → random blocks → random households
      → National surveys (General Social Survey, CPS): multistage stratified

  NON-PROBABILITY SAMPLING:

    Convenience: who is available → easy but non-generalizable
    Snowball: existing participants recruit others → for hard-to-reach populations
    Purposive: select cases that are theoretically relevant
    Quota: match population proportions non-randomly → not inference-valid

  SAMPLING FRAME PROBLEMS:
    Sampling frame: list of population members from which sample is drawn
    Frame errors: undercoverage (missing members); overcoverage (non-members)
    Cell phone era: landline-only RDD → systematic undercoverage of young/mobile → 2016 polling errors
    Online panels: not probability sample → requires weighting; debate about validity

SAMPLE SIZE AND POWER:
  Power: probability of detecting a true effect of given size
  For given power (0.80 standard): need n depends on effect size + variance
  Survey margin of error: ±2σ = ±2/√n
    n=1000: ±3.2 percentage points (95% CI)
    n=400: ±5 percentage points
    → Most national surveys: n=1000–2000; adequate for national estimates
    → Subgroup analysis requires larger n (subgroup n drives precision, not total n)
```

### Question Design

```
QUESTION WORDING EFFECTS:
  Small changes in wording → large changes in responses
  → Social desirability bias: respondents answer based on what seems acceptable
    not their actual behavior/attitude
  → Question framing: "allowing" vs. "forbidding": same policy framed differently
     → "Should Congress pass laws to allow abortion?" vs "forbid abortion" → ~10% different

ACQUIESCENCE BIAS (yea-saying):
  Respondents tend to agree with statements regardless of content
  → Problem: Likert scale items that all point the same way
  → Solution: reverse-coded items (some items where "agree" = negative on construct)

RESPONSE SET:
  Using same response category regardless of question content
  Extreme response style: preferring scale endpoints
  → Cultural variation: East Asian respondents more moderate; US respondents more extreme

QUESTION ORDER EFFECTS:
  Earlier questions change how later questions are interpreted
  → Priming: mention race/crime → subsequent evaluation questions shift
  → Satisficing: mental shortcuts; less thinking as survey progresses → random responses

SENSITIVE QUESTIONS:
  Direct questions: underreporting of illegal behavior, sexual behavior, drug use, income
  Randomized response technique: respondent privately decides which of two questions to answer
    → Researcher knows probability distribution but not individual response → plausible deniability
  List experiments (item count technique): control group lists N neutral items; treatment adds sensitive item
    → Difference in mean count = estimate of sensitive behavior prevalence; individual answers not revealed

MODE EFFECTS:
  Face-to-face: higher social desirability bias; higher response rate
  Phone (CATI): cheaper; moderate response rate; decreasing as call refusal rises
  Mail: low response rate; cheap; useful for complex questionnaires
  Online: cheapest; lowest social desirability; question order easy to randomize
           but: selection into online panels; device-specific effects (phone vs desktop)
  Interviewer effects: race, gender, apparent attitude of interviewer → responses shift
```

---

## Ethnography

### Participant Observation

```
ETHNOGRAPHY — DEFINITION:
  Immersive, long-term fieldwork in a social setting
  Researcher participates in and observes social life → produces "thick description"
  Classic texts: Whyte (Street Corner Society, 1943), Goffman (Asylums, 1961),
                 Liebow (Tally's Corner, 1967), Venkatesh (Gang Leader for a Day, 2008)

PARTICIPANT OBSERVATION SPECTRUM:

  COMPLETE OBSERVER ◄─────────────────────► COMPLETE PARTICIPANT
  Covert watching                            Full membership; concealed identity
  No interaction                             Hidden research role

  OBSERVER AS PARTICIPANT: researcher role known; limited participation
  PARTICIPANT AS OBSERVER: full participation; researcher role known; primary role is member

GOING NATIVE:
  Risk: over-identifying with group → loss of analytical distance
  Signs: cease to notice what was initially strange; accept group's own explanations
         stop questioning; protective of group against outside analysis
  Balance: "sufficient alienation" — enough distance to analyze what is taken for granted
  Gold's typology of observer roles — all positions have methodological implications

DETACHMENT STRATEGIES:
  Regular breaks from field → return to outsider perspective
  Field notes: written immediately → capture strangeness before it becomes familiar
  Debrief with outside colleagues → verify analytical clarity
  Multiple perspective-taking: interview different status positions in the field

FIELD NOTE PRACTICES:
  Jottings: brief notes during or immediately after interactions (avoid during interactions when disruptive)
  Full field notes: same day; chronological narrative + analytical memos
  Head notes: mental notes (unreliable; selective; must be written soon)
  Reflective memos: analytical observations separated from description
  Key distinctions: observation notes (what happened) vs. inference notes (what it might mean)

ETHICAL ISSUES:
  Informed consent: usually required but creates problems (subjects perform differently when observed)
  Covert research: some studies require covert entry (Goffman in Asylums; some workplace studies)
    → Justified by: can't do research otherwise + public interest; contested
  Vulnerable populations: special obligations; protection from identification; power asymmetry
  Going public: risk to subjects from identification in published work
  Reciprocity: researcher takes from community; what is given back?
```

### Thick Description

```
CLIFFORD GEERTZ (The Interpretation of Cultures, 1973):

THICK DESCRIPTION (from Gilbert Ryle):
  "Thin description": recording what happens (man's eyelid twitched)
  "Thick description": recording what it means in context
    (was that a twitch, a wink, a mock-wink, a rehearsal of a wink?)
  → The same physical act has radically different meanings depending on context
  → Sociology's job: produce interpretations of meaning, not mere behavioral record

"CULTURE AS TEXT":
  Geertz: cultures are webs of significance; analysis = interpretation, not experiment
  Ethnographer: doesn't study a culture, reads it — like reading a foreign document
  "Over my shoulder": informants' interpretations of their own behavior
  → Unlike psychology: ethnographer never escapes the hermeneutic circle
  → Meaning from the actors' perspective is the object of study

THE BALINESE COCKFIGHT (Geertz 1973):
  Methodological: the event that broke his anonymity with villagers → created rapport
  Analytical: cockfight as text about Balinese culture — machismo, status, fate, passion
  → Reading the cockfight: Balinese society dramatizing itself for itself
  → Not: cockfight explains Bali; rather: cockfight is a story Balinese tell about themselves
  Critical reception: some criticized for: researcher-imposed interpretation; what Balinese
    actually said about cockfight vs. Geertz's interpretation

ETHNOGRAPHIC VALIDITY:
  Construct validity: did researcher observe what they claim to have observed?
  Reactivity: observer changes what's being observed (Hawthorne-like)
  Positionality: researcher's identity affects what they can observe
    → Venkatesh (South Asian male, academic) saw different things in the Chicago housing project
       than a Black female researcher from that community would have seen
  Member checking: show analysis to informants → do they recognize it?
    → Both agreement and disagreement can be informative
```

---

## Content Analysis

```
CONTENT ANALYSIS:
  Systematic analysis of communicative content (text, image, audio, video)
  Can be quantitative (frequency counts) or qualitative (interpretive)

QUANTITATIVE CONTENT ANALYSIS:
  Unit of analysis: word, sentence, paragraph, article, image, scene
  Coding scheme: operationalize concepts → assign codes to units
  Reliability: two independent coders → interrater reliability (Cohen's κ or Krippendorff's α)
  → κ > 0.8: good; κ > 0.6: acceptable; κ < 0.6: recode

  EXAMPLE:
    Research question: How is immigration covered in NY Times vs Fox News (2015–2020)?
    Sample: all articles containing "immigration" or "immigrant" (automated retrieval)
    Codes: frame (economic/security/humanitarian); tone (negative/neutral/positive);
           sources quoted (politician/expert/affected person/other)
    Analysis: compare distributions across outlets × time

COMPUTATIONAL TEXT ANALYSIS:
  Word frequency / TF-IDF: term frequency vs. inverse document frequency → topic salience
  Word embeddings (Word2Vec, BERT): semantic relationships → machine-readable meaning
  Topic modeling (LDA): identifies latent topics across corpus without human coding
  Sentiment analysis: classify positive/negative/neutral automatically
  LIMITATION: all require validation against human coding; automated often misses irony,
    context, implicit meaning → combine with qualitative reading

QUALITATIVE CONTENT ANALYSIS / DISCOURSE ANALYSIS:
  Close reading of texts → identify frames, ideologies, power relations, silences
  Critical Discourse Analysis (CDA — Fairclough, van Dijk):
    Language is not neutral → reproduces or challenges power
    How is "the immigrant" discursively constructed?
    What is said and what is silenced?
    → CDA explicitly normative: texts are analyzed for ideological effects
```

---

## Comparative Historical Sociology

```
HISTORICAL-COMPARATIVE METHODS:
  Comparative across cases (nations, institutions, periods) to generate and test theory
  Classic works: Weber (Protestant Ethic), Moore (Social Origins of Dictatorship and Democracy),
                 Skocpol (States and Social Revolutions), Tilly (The Contentious French)

MILL'S METHODS (John Stuart Mill, 1843 — "Method of Agreement" and "Difference"):

  METHOD OF AGREEMENT:
    Cases: all share same outcome (all had revolution)
    Vary on many things; look for what they all share
    → If X always present when outcome Y occurs → X is a candidate cause
    Risk: confounding; many possible shared causes

  METHOD OF DIFFERENCE:
    Cases: similar on most things; differ on outcome and on one factor
    → Control case (no revolution) + treatment case (revolution)
    → If X present in revolution case and absent in non-revolution → X is candidate cause
    → Better: controls confounding if cases really are similar on other factors

MOST SIMILAR SYSTEMS DESIGN (MSSD):
  Compare cases that are similar on many background factors but differ on outcome
  → Control for background variation; highlight causal variable
  Example: Why did England industrialize before France despite similar conditions?
  Risk: cases are never truly "most similar"; unobserved differences remain

MOST DIFFERENT SYSTEMS DESIGN (MDSD):
  Compare cases that differ on most background factors but share the same outcome
  → The causal factor must be present in very different contexts to be truly robust
  Example: Why did widely different societies all develop modern states?
  → Shared factor despite different contexts = robust causal candidate

QUALITATIVE COMPARATIVE ANALYSIS (QCA — Ragin 1987):
  Combines: causal complexity (necessary + sufficient conditions) + comparative analysis
  Conditions: coded as present/absent (crisp set) or 0–1 (fuzzy set)
  Outcome: also coded
  QCA identifies: necessary conditions (present in all cases with outcome)
                  sufficient conditions (when present → outcome follows)
                  Boolean algebra: find minimal formula that explains outcome
  Advantage: handles small-N better than regression; models causal complexity
  Criticism: arbitrary calibration of fuzzy sets; sensitivity to case inclusion
```

---

## Mixed Methods

```
MIXED METHODS RATIONALE:
  Different methods access different aspects of social reality
  → Quantitative: distribution, correlation, generalizability
  → Qualitative: meaning, process, mechanism, exception explanation

  NOT just "triangulation" (checking same finding with different methods)
  Rather: complementarity — each method answers what the other can't

DESIGNS:

  SEQUENTIAL EXPLORATORY:
    Qualitative first → generates hypotheses/items/variables
    → Quantitative second → tests hypotheses on large sample
    Use: developing survey instruments from interview themes
         theory-building from ethnography → large-scale test

  SEQUENTIAL EXPLANATORY:
    Quantitative first → identifies patterns, outliers, puzzles
    → Qualitative second → explains the patterns in depth
    Use: regression finds unexpected interaction → ethnography explains why
         survey shows group X differs → interviews unpack mechanism

  CONCURRENT/EMBEDDED:
    Both methods simultaneously; one embedded within the other
    Use: RCT + qualitative (implementation study: why did the intervention work/not work?)
         Survey + in-depth interview subsample → enriches data from same sample

  METHODOLOGICAL INTEGRATION LEVELS:
    Data collection: separate instruments, joint fieldwork
    Analysis: separate analyses, joint analysis
    Interpretation: separate write-ups, integrated interpretation
    → Full integration (joint analysis + interpretation): most challenging; most powerful
```

---

## Sociology of Knowledge

### Standpoint Epistemology

```
STANDPOINT EPISTEMOLOGY (Sandra Harding, Patricia Hill Collins, Dorothy Smith):

CORE CLAIM:
  "Knowledge" is not produced from a neutral "view from nowhere"
  Where you stand (your social position, identity, experience) affects what you can see
  → Marginalized groups have epistemological advantages in certain domains
     because their subordinate position requires them to understand BOTH
     the dominant culture AND their own experience

  Hill Collins: Black women's standpoint
    → Double consciousness: must understand white/male perspective to navigate society
    → Also have intimate knowledge of their own experience
    → Can see structural dynamics that are invisible to those who benefit from them
    → "The outsider-within": Black academics in white institutions → distinctive standpoint

IMPLICATIONS FOR RESEARCH:
  Who produces knowledge matters: a discipline dominated by white men → blind spots
  Reflexivity: researchers should make their standpoint explicit
  Collaboration with researched communities → reciprocal knowledge production
  "Strong objectivity" (Harding): standpoints of marginalized give more complete knowledge
    → More objective because: includes perspectives normally excluded
    → vs. "weak objectivity" (neutral observer): actually just encodes dominant standpoint

CRITICISM:
  Relativism: if all knowledge is standpoint-based → no truth, only perspectives
    → Harding: no; "strong objectivity" is more objective, not less
    → Response: some interpretations are better supported than others
  Essentialism: "women's standpoint" → not all women share the same position
    → Intersectionality: standpoints are multiple and intersecting (not monolithic)
  Scope: some knowledge (physics, mathematics) seems less standpoint-dependent
    → Social construction of science more contested than of social science

REFLEXIVITY IN SOCIOLOGY:
  Researcher position: write about how your identity, access, relationships affected fieldwork
  Pierre Bourdieu: "participant objectivation" — apply sociological analysis to your own practice
    → Most honest sociology: acknowledges researcher is embedded in social field being analyzed
  "Positionality statements" in qualitative papers: now standard practice
```

### Other Epistemological Positions

```
POSITIVISM (Durkheim's legacy):
  Social facts: external to individuals; constraining; measurable
  Goal: discover causal laws governing social behavior
  Method: quantitative; statistical; deductive
  Replication and generalization: marks scientific knowledge

INTERPRETIVISM (Weber, Geertz, symbolic interactionism):
  Social action: meaningful; must be understood ("Verstehen") not just explained
  Goal: interpretive understanding of meaning from within
  Method: qualitative; inductive; comparative
  Validity: internal coherence, resonance, richness of interpretation

CRITICAL THEORY (Frankfurt School, CDA):
  Knowledge is always value-laden; serves interests
  Goal: emancipatory; challenge taken-for-granted ideologies
  Method: critique of existing social arrangements; normative engagement
  Criterion: not "true/false" but "liberatory/oppressive"

PRAGMATISM (Dewey; contemporary social science):
  Use whatever methods work for the question
  Methods should be chosen for their utility, not their epistemological purity
  Basis for mixed methods; rejects quantitative/qualitative wars
```

---

## Decision Cheat Sheet

| Question type | Best method |
|--------------|-------------|
| How many people hold attitude X? | Survey (probability sample) |
| Why do people hold attitude X? | In-depth interviews or focus groups |
| How does institution X actually work? | Ethnography (participant observation) |
| What caused revolution/welfare state/etc.? | Historical-comparative (Mill's methods, QCA) |
| How is issue X framed in media? | Content analysis (quantitative + discourse analysis) |
| Does intervention X work? (causal) | Experiment; or natural experiment + diff-in-diff |
| Why did respondents answer Y on the survey? | Sequential explanatory mixed methods |
| Is researcher A's interpretation accurate? | Member checking, reflexivity, rival hypotheses |

---

## Common Confusion Points

**Reliability and validity are different problems**
Reliability: does the measure give consistent results? (same result if measured twice)
Validity: does the measure capture what it claims to measure?
A question can be highly reliable (consistent) but invalid (consistently measuring the wrong thing). Example: measuring height with a consistent but miscalibrated ruler → reliable but invalid. In survey research: response consistency (test-retest) ≠ construct validity (am I measuring what I claim?).

**Qualitative research is not pre-scientific or merely exploratory**
Ethnography and interpretive sociology produce systematic, rigorous, falsifiable claims — they just have different validity criteria than quantitative research. "I observed X in 6 months of fieldwork with Y people" is not weaker evidence than "I surveyed 200 respondents"; it's different evidence answering a different question. Qualitative findings that resist member checking or fail to account for disconfirming cases are bad research by qualitative standards, just as surveys with low response rates are bad by quantitative standards.

**Mixed methods is not just using two methods — it requires integration**
Running a survey and an interview study and putting both in the same paper is multi-method, not mixed methods. Mixed methods requires methodological integration: using the qualitative findings to interpret the quantitative results, or using quantitative patterns to guide qualitative sampling. True integration is difficult and often not achieved despite the label.

**Standpoint epistemology is a claim about access to evidence, not about identity determining truth**
The argument is that social position shapes what aspects of reality are visible to you — marginalized people have experienced things that dominant-group members have not and cannot claim to understand. It is not a claim that "only Black people can study racism" or that identity automatically conveys expertise. The standpoint is a starting point for analysis, not a conclusion; it requires the same rigor as any other research.

**Mill's methods identify candidate causes; they don't prove causation**
The Method of Agreement (all outcome cases share X) and Method of Difference (X present in outcome case, absent in comparison case) are systematic ways to identify what factors are associated with outcomes across cases. But they can't rule out unobserved confounders, they depend on case selection, and they assume the researcher has identified the right variables to examine. They are tools for structured comparison, not proof by elimination.
