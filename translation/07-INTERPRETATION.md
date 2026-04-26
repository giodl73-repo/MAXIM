# Simultaneous and Consecutive Interpretation

## The Big Picture

```
INTERPRETATION MODES — OVERVIEW
════════════════════════════════════════════════════════════════════

  SIMULTANEOUS INTERPRETATION (SI):
  Interpreter works in real time, with ~2-5 second lag
  behind the speaker. The speaker never stops.

  ┌──────────────────────────────────────────────────────────┐
  │  SPEAKER → [soundproof booth] INTERPRETER → HEADPHONES   │
  │                                                          │
  │  Speaker speaks: "The delegation from France has..."     │
  │  Interpreter: (2 seconds later) "La délégation de..."    │
  │               (while speaker is still talking)           │
  │                                                          │
  │  Result: Audience hears continuous interpretation        │
  │  with no break in the speaker's presentation             │
  └──────────────────────────────────────────────────────────┘

  CONSECUTIVE INTERPRETATION (CI):
  Speaker pauses (after 1-5 minutes); interpreter renders
  from notes; speaker resumes.

  ┌──────────────────────────────────────────────────────────┐
  │  Speaker speaks 3 minutes → pauses                       │
  │  Interpreter renders 3 minutes from notes                │
  │  Speaker resumes → pauses                                │
  │  Interpreter renders again                               │
  │                                                          │
  │  Result: Meeting takes 2x as long                        │
  │  Interpretation can be more accurate                     │
  │  (more processing time; complete message heard first)    │
  └──────────────────────────────────────────────────────────┘

  OTHER MODES:
  Whispered interpretation (chuchotage): interpreter
  whispers simultaneously to 1-2 persons; no booth
  Community / liaison interpretation: bidirectional;
  conversation interpreting (medical, legal, social)
  Sight translation: read written text aloud in
  another language in real time
```

---

## Seleskovitch's Interpretive Theory

Danica Seleskovitch developed the dominant cognitive theory of interpretation at ESIT (Ecole Supérieure d'Interprètes et de Traducteurs), Paris, 1970s:

**Core claim**: Interpretation is not word-for-word or even phrase-for-phrase translation. It is a three-stage process:

```
SELESKOVITCH'S INTERPRETIVE THEORY — THREE STAGES
════════════════════════════════════════════════════════════════

  STAGE 1: COMPREHENSION
  ┌──────────────────────────────────────────────────────┐
  │ The interpreter listens and builds a meaning         │
  │ representation. This is NOT a linguistic             │
  │ representation — it is a concept/meaning             │
  │ representation that has been "deverbalized."         │
  │                                                      │
  │ The words drop away; the meaning remains.            │
  │                                                      │
  │ This is why you often cannot remember the exact      │
  │ words of something you understood — you retained     │
  │ the meaning and discarded the linguistic form.       │
  └──────────────────────────────────────────────────────┘
            │
            ▼
  STAGE 2: DEVERBALIZATION
  ┌──────────────────────────────────────────────────────┐
  │ The meaning is held briefly as a non-linguistic      │
  │ concept — the "sense" that Cicero and Nida           │
  │ were talking about.                                  │
  │                                                      │
  │ This is the interpretive moment — the cognitive      │
  │ gap where the interpreter holds meaning without      │
  │ words.                                               │
  └──────────────────────────────────────────────────────┘
            │
            ▼
  STAGE 3: RE-EXPRESSION
  ┌──────────────────────────────────────────────────────┐
  │ The meaning is re-expressed in the target language.  │
  │ The interpreter chooses target-language words to     │
  │ encode the deverbalized meaning.                     │
  │                                                      │
  │ The target-language words are NOT derived from       │
  │ the source-language words directly — they are        │
  │ derived from the meaning.                            │
  └──────────────────────────────────────────────────────┘

  WHY THIS MATTERS:
  It explains why trained interpreters often produce more
  natural target-language output than word-for-word
  translators: they are NOT translating words, they
  are expressing meanings.

  It also explains a failure mode:
  If the interpreter does not understand (no deverbalization),
  they fall back on word-for-word — which produces
  errors and unnatural target text.
```

---

## Gile's Effort Model

Daniel Gile (*Basic Concepts and Models for Interpreter and Translator Training*, 1995) provides a cognitive load model for simultaneous interpretation:

```
GILE'S EFFORT MODEL FOR SIMULTANEOUS INTERPRETATION
════════════════════════════════════════════════════════════════

  TOTAL PROCESSING CAPACITY
  ┌────────────────────────────────────────────────────────┐
  │  L (Listening and Analysis Effort)                     │
  │  + M (Memory Effort — working memory management)       │
  │  + P (Production Effort)                               │
  │  + C (Coordination Effort — coordinating the above)    │
  │  ≤ Available Processing Capacity                       │
  └────────────────────────────────────────────────────────┘

  CRISIS: When L + M + P + C > Available Capacity
  → Interpretation degrades
  → Errors, omissions, unintelligible output

  TRIGGERS FOR OVERLOAD:
  ┌─────────────────────────────────────────────────────┐
  │ • Speaker talks too fast                            │
  │ • Unfamiliar topic or terminology                   │
  │ • Dense information (lists of numbers, proper names) │
  │ • Long sentences requiring held memory              │
  │ • Accent or voice quality requiring extra L effort  │
  │ • Background noise increasing L effort              │
  └─────────────────────────────────────────────────────┘

  COPING STRATEGIES:
  • Simplification (produce simpler target text)
  • Omission (drop parts of the message)
  • Approximation (use near-synonyms)
  • Delay (increase lag to complete processing)
  • Switch to consecutive (if possible — conference rules)

  THE PARADOX:
  The fastest speakers cause the most errors —
  but the interpreter has no control over speech rate.
  This is why conference organizers and interpreters
  sometimes negotiate speaker rate limits.

BOUNDED-RESOURCE SCHEDULING — THE FORMAL MODEL:
  Gile's model is a bounded-resource scheduling problem.
  The constraint: L + M + P + C ≤ Available Capacity.
  This is formally identical to:
    CPU scheduling: total CPU demand ≤ available CPU time
    Bandwidth allocation: Σ(flow demands) ≤ link capacity
    Thread pool management: work queue depth ≤ pool size × time

  The interpreter is a single-threaded system with limited
  working memory (buffer). The demands on the buffer
  (incoming speech, held memory, outgoing production)
  compete for a shared resource.

  THROUGHPUT VS LATENCY TRADEOFF:
    The interpreter can trade latency for accuracy:
    Increase lag (hold more input before producing output) →
      better comprehension of full sentences (lower error rate)
      but higher latency and higher M (memory load).
    Decrease lag (stay close to the speaker) →
      lower latency but higher error rate on long dependencies.
    This is the classic throughput/latency tradeoff in
    streaming systems: larger buffers → better batch decisions
    but higher end-to-end latency.

  COPING STRATEGIES AS SCHEDULING POLICIES:
    Simplification → reduce work per unit (lower per-item cost)
    Omission → drop items from the queue (priority scheduling)
    Approximation → reduce precision requirement (lossy compression)
    Delay → increase buffer size (larger working set)
    These are exactly the strategies a scheduler uses when
    demand approaches capacity: drop, simplify, or delay.

  TRIGGERS FOR OVERLOAD ↔ SYSTEM LOAD SPIKES:
    Dense information (numbers, proper names) →
      spikes in M effort (each item requires held memory)
      equivalent to a sudden burst of cache-miss-heavy requests
    Long sentences requiring held memory →
      working set overflow; items must be evicted before complete
      equivalent to buffer overflow under sustained high throughput
    Background noise →
      increases L effort; equivalent to noise on a channel
      requiring more processing per bit for error correction
```

---

## Nuremberg Trials: First Large-Scale SI

The International Military Tribunal at Nuremberg (1945-46) was the first major deployment of simultaneous interpretation. Four working languages: English, French, Russian, German.

```
NUREMBERG INTERPRETATION SETUP
════════════════════════════════════════════════════════════════

  SYSTEM DESIGNED BY: IBM engineer assigned to project
  (building on earlier radio simultaneous interpretation
  experiments at League of Nations in the 1930s)

  4 LANGUAGE BOOTHS: English, French, Russian, German
  Each booth: team of interpreters working in shifts
  (SI was so cognitively demanding that 30-minute
   shifts were standard — still standard today)

  YELLOW LIGHT: Signal to speaker to slow down
  RED LIGHT: Signal to speaker to stop

  KEY EPISODE:
  Hermann Göring's testimony: he spoke extremely quickly,
  was technically sophisticated, often digressed.
  Interpreters struggled. The presiding judge repeatedly
  had to intervene to slow him down.
  Some of Göring's testimony is interpreted with errors
  in the official record — identified by subsequent
  scholars comparing German stenographic record
  with English interpretation.

  HISTORICAL SIGNIFICANCE:
  Nuremberg established simultaneous interpretation
  as the standard for international forums.
  UN, European Parliament, WTO — all use SI.
  Consecutive interpretation now reserved for
  smaller meetings, bilateral diplomacy, negotiations.
```

---

## UN and EU Interpreter Training

### The UN Model

The UN has six official languages: Arabic, Chinese, English, French, Russian, Spanish. UN interpreters are typically trained at recognized interpreter schools and pass competitive examinations.

Typical career path:
- University education (often in multiple fields)
- Language combination: typically 3 languages, one as A (mother tongue), two as B/C (working languages)
- Training program at ESIT (Paris), SAIS (Bologna), ETI (Geneva), or equivalent
- UN examination: tests consecutive and simultaneous at speed and under pressure

### The European Parliament Model

The European Parliament is the most demanding interpreting environment in the world: 24 official languages, all combinations potentially active. Not 24 × 23 = 552 possible combinations (most impossible to staff) but a "relay" system:

```
RELAY INTERPRETATION (EU Parliament)
════════════════════════════════════════════════════════════════

  PROBLEM: No interpreter can work from all 24 EU languages.
  What if someone speaks Finnish (less common) and needs
  to be heard in Portuguese?

  RELAY SYSTEM:
  Finnish speaker → Finnish→English interpreter
                    (or Finnish→French; depends on
                     what relay languages are used)
  English interpretation → English→Portuguese interpreter

  The Portuguese interpreter "listens off" the English
  intermediate interpretation, not the Finnish original.

  QUALITY DEGRADATION:
  Each relay hop can introduce errors; the Portuguese
  interpreter is working from an already-interpreted text.
  The European Parliament tries to minimize relay
  combinations and maximize direct interpretation.
```

---

## Community and Healthcare Interpreting

"Conference interpreting" (UN, EU, diplomatic) is the prestige end. But most interpretation globally happens in community settings: hospitals, courts, immigration offices.

```
COMMUNITY INTERPRETATION — DIFFERENT CHALLENGES
════════════════════════════════════════════════════════════════

  HEALTHCARE SETTING:
  • Bidirectional (doctor ↔ patient)
  • Consecutive mode (doctor speaks, interpreter, patient speaks)
  • High stakes: misinterpretation can lead to wrong diagnosis,
    wrong medication, missed consent
  • Confidentiality + emotional weight
  • Interpreters often not professionally trained —
    family members used (children interpreting for parents!)
    → Ethical problem: children should not hear adult
       medical information; power relationship distorted

  COURT INTERPRETATION:
  • Accuracy requirements are near-total (legal standard)
  • Verbatim interpretation usually required
    (witness's exact words, not paraphrase)
  • Consecutive mode typically
  • Oath: court interpreter swears to interpret accurately
  • Interpreter neutrality: not an advocate for either party

  INTERPRETER NEUTRALITY vs. ADVOCACY DEBATE:
  Traditional: interpreter is a neutral conduit — says
  what is said, nothing more.
  Advocacy position: in community settings, strict
  neutrality can harm vulnerable parties. If a doctor
  is being unclear and the interpreter knows it,
  should the interpreter intervene?
  Current professional consensus: announce interventions
  ("The interpreter notes that...") rather than silent
  distortion.
```

---

## Signed Language Interpretation

Sign languages (ASL, BSL, LSF, etc.) are full natural languages, not systems of gestured English/French. They are often radically different grammatically from their surrounding spoken languages.

```
SIGNED LANGUAGE INTERPRETATION — KEY FACTS
════════════════════════════════════════════════════════════════

  ASL ≠ SIGNED ENGLISH:
  American Sign Language has its own grammar:
  • Topic-comment structure (not SVO)
  • Spatial grammar (locations in signing space
    represent referents; agreement is spatial)
  • Non-manual markers (facial expression, mouth movement)
    are grammatical, not emotional

  INTERPRETING SPOKEN → SIGNED:
  Not substituting English words with ASL signs.
  Must reconstruct grammatical structure in ASL
  spatial grammar. Similar cognitive demands to
  spoken SI, plus the production effort of
  signed language is physical-motor, not verbal.

  CONSECUTIVE INTERPRETATION:
  More common for signed languages in community settings —
  allows the interpreter to fully process spoken message
  before producing ASL output.

  COGNITIVE COST:
  Signed language interpretation is cognitively equivalent
  to or more demanding than spoken SI. The motor production
  effort is additional. Professional signed language
  interpreters take 20-30 minute shifts.
```

---

## The Cognitive Science of Bilingual Switching

Simultaneous interpretation is the most demanding form of bilingual processing. What does the research show?

```
SI AND COGNITIVE NEUROSCIENCE
════════════════════════════════════════════════════════════════

  FMRI STUDIES OF SIMULTANEOUS INTERPRETERS:
  • Increased activation in prefrontal cortex
    (executive control — switching, inhibiting)
  • Broca's area and Wernicke's area bilaterally activated
  • Caudate nucleus: bilingual language control
    (lesions impair language switching)
  • Less activation per unit of language in experienced
    interpreters vs. novices (automaticity effect)

  BILINGUAL SWITCHING COST:
  Monolingual: no switching cost (by definition)
  Bilingual switching: measurable RT cost for each switch
  Simultaneous interpreter: switching cost reduced through
  practice — not eliminated but managed

  INHIBITORY CONTROL:
  The key cognitive skill in SI is suppressing the
  non-active language. When interpreting from French to
  English, you must suppress English while processing
  French, then suppress French while producing English —
  simultaneously, in the same ~3-second processing window.

  This is a core executive function task.
  Professional interpreters show enhanced executive
  control vs. bilinguals vs. monolinguals.
  "The interpreter effect" in cognitive science:
  SI training appears to develop general executive
  function beyond language-specific skills.
```

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| What is the difference between SI and CI? | SI: real-time with lag; CI: speaker pauses, interpreter renders from notes. SI used in large conferences; CI for smaller meetings, diplomatic contexts |
| What is Seleskovitch's theory? | Three stages: comprehension → deverbalization (meaning without words) → re-expression in target. Explains why trained interpreters produce natural output, not word-for-word |
| What is Gile's effort model? | SI requires L + M + P + C ≤ total capacity. Overload occurs when speech is fast, dense, or unfamiliar — producing errors, omissions, simplification |
| Why did Nuremberg matter for SI? | First large-scale deployment of SI (4 languages); IBM-designed system; established 30-minute rotation standard still in use |
| What is relay interpretation? | Interpreting from an intermediate interpretation (Finnish → English → Portuguese); used when no direct language combination available; introduces quality degradation |
| What is the interpreter neutrality debate? | Traditional: neutral conduit; advocacy position: intervene when vulnerable party at risk; consensus: announce interventions explicitly |

---

## Common Confusion Points

**SI is not faster interpretation of the same cognitive process**: SI is a qualitatively different cognitive activity from reading a text and then translating it. The temporal constraint forces different strategies (deverbalization, coping), greater cognitive load, and higher error rates. Experienced SI interpreters are not just fast — they have developed automated cognitive routines that reduce load.

**Deverbalization is not a metaphysical claim**: Seleskovitch's "deverbalization" is an empirical claim about cognitive processing, supported by the observation that trained interpreters produce natural output even when source syntax is very different from target syntax. It doesn't claim that meaning is language-independent in a philosophical sense — only that during interpretation processing, the linguistic form is temporarily released.

**Family members interpreting is a serious problem**: Using family members (especially children) as medical or legal interpreters is common globally, particularly in immigrant communities. The practice systematically distorts communication: children shouldn't hear adult medical information; family members have interests (and vocabulary gaps) that distort interpretation; the power relationship between doctor/lawyer and patient/defendant is not mediated by a neutral party.

**ASL is not "gestured English"**: This is the most common misconception. ASL has its own complete grammar, its own syntax, its own history (developed at American School for the Deaf, Hartford, CT, 1817). It is as unrelated to English as Chinese is. A hearing person who learns to produce English words in manual signs (Manually Coded English) is NOT speaking ASL.
