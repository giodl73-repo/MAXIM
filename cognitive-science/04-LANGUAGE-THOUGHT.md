# Language and Thought — Cognitive Science

## The Big Picture

Does language shape thought, or does thought shape language? The question has a long history and a messy empirical record. The modern answer: *some* effects, in specific domains, of modest magnitude — but the strong version (language determines thought) is dead.

Separately: what *is* a concept, how does language processing work at the neural level, and is there a Language of Thought distinct from natural language?

```
+------------------------------------------------------------------+
|  LANGUAGE-THOUGHT RELATIONS: LANDSCAPE                           |
+------------------------------------------------------------------+
|                                                                  |
|  STRONG DETERMINISM          WEAK RELATIVITY          NO EFFECT  |
|  (Whorf, 1940s)              (Boroditsky, Levinson,   (universal  |
|                               Lucy, Kay)               cognition) |
|  Language constrains         Language influences       Language   |
|  what we can think           attention, memory,        is just    |
|                              categorization at         a tool     |
|  Status: FALSIFIED           the margins               for output |
|                              Status: SUPPORTED         Status:    |
|  Pirahã count "one,          (specific domains)        TOO SIMPLE |
|  two, many" — hard           Color, time, space,                  |
|  to represent >2             number, spatial                      |
|  but this is rare            direction                            |
|  and disputed                                                     |
+------------------------------------------------------------------+
```

---

## The Neural Architecture of Language

**Broca-Wernicke-Geschwind model** (19th century, revised):

```
LATERAL LEFT HEMISPHERE:

  FRONTAL LOBE         PARIETAL LOBE
  +───────────────+    +─────────────────+
  |  BROCA'S AREA |    |                 |
  |  (IFG,        |    |   SUPRAMARGINAL |
  |   BA 44/45)   |    |   GYRUS         |
  |               |    |  (phonology +   |
  |  Production   |    |   reading)      |
  |  Syntax       |    +─────────────────+
  |  Articulation |           |
  +───────────────+    ARCUATE FASCICULUS
          |            (white matter tract
          └────────────connecting Broca+Wernicke)
  TEMPORAL LOBE         ↓
  +───────────────────────────────────────+
  |  WERNICKE'S AREA (STG, BA 22)         |
  |  Comprehension, lexical access        |
  |  Semantic-phonological mapping        |
  +───────────────────────────────────────+
```

**Aphasia types from lesions**:

| Aphasia | Lesion | Fluency | Comprehension | Repetition | Example |
|---------|--------|---------|---------------|------------|---------|
| **Broca's** | Left IFG | Non-fluent, halting | Relatively intact | Impaired | "Walk...park...wife...no...can't" |
| **Wernicke's** | Left STG | Fluent, but | Impaired | Impaired | "The frub goes to the market |
| | | word salad | | | grobish the tailing" |
| **Conduction** | Arcuate fasciculus | Fluent | Intact | Impaired | Can speak and understand but |
| | | | | | cannot repeat what just heard |
| **Anomic** | Distributed | Fluent | Intact | Intact | Word-finding difficulty; |
| | | | | | "the thing you use to...you know..." |

**Modern revision** (since ~2000 with fMRI): The model is too simple.
- Language is *bilateral* — right hemisphere contributes (especially prosody, metaphor, discourse)
- Broca's area does much more than production: also working memory, action, music
- The ventral pathway (temporal–frontal) handles semantic/syntactic composition; dorsal pathway (parietal–frontal) handles sensorimotor mapping and syntax
- Language is distributed across a network, not localized in two spots

---

## Psycholinguistics — Methods and Key Results

**Methods**:

| Method | What it measures |
|--------|-----------------|
| **Lexical decision task** | RT to decide if string is a word; reveals lexical access |
| **Reading-time / eyetracking** | Fixation duration = processing difficulty |
| **ERP (event-related potential)** | Neural response to specific word types |
| **Priming** | Does related word speed access to target? |
| **Sentence completion** | Reveals prediction during comprehension |

**Key ERP components**:
- **N400** (negative peak ~400ms): semantic incongruity ("He spread the warm bread with *socks*"). Larger N400 = more surprising word semantically.
- **P600** (positive peak ~600ms): syntactic anomaly and reanalysis ("The horse raced past the barn *fell*").

**Garden path sentences** — incremental parsing revealed:
```
"The horse raced past the barn fell."
         ↑
Processor commits to: horse = subject, raced = main verb
                      past the barn = PP → sentence complete
         ↓
"fell" arrives → reanalysis required:
                 horse raced past the barn = reduced relative clause
                 = "the horse THAT WAS raced past the barn fell"
```

Processing is *incremental* (commit to interpretation word-by-word) and *garden paths* show that early commitments can be wrong and require backtracking.

**Lexical access models**:
- **Cohort model** (Marslen-Wilson): Spoken word activates all words sharing initial sound; cohort narrows as more of word heard
- **TRACE** (McClelland & Elman): Interactive activation model — features→phonemes→words, with top-down feedback

---

## Sapir-Whorf Hypothesis — What the Data Shows

**Strong version (Whorf 1940s)**: Language determines thought. Different languages produce different *cognitive categories* — you can't think what you can't say. **Status: falsified.**
- Speakers of languages without color terms can still *discriminate* colors they can't name
- Pirahã (Everett): no recursion, no number words beyond "few/many" — but disputed on evidence quality

**Weak version** (Linguistic Relativity): Language *influences* perception, memory, and categorization for specific domains. **Status: supported with caveats.**

### Color
- Russian has two basic terms where English has one: *siniy* (dark blue) vs *goluboy* (light blue)
- Russian speakers are faster to discriminate dark-blue/light-blue pairs than English speakers (Winawer et al. 2007)
- Effect is right-hemisphere absent (left hemisphere = language-dominant) → only appears in right visual field
- Effect is reduced under verbal interference task → language is doing the work, not just perceptual difference

### Spatial Direction
- Guugu Yimithirr (Australia): no egocentric left/right; uses absolute cardinal directions (north/south/east/west) always
- Speakers maintain extraordinary sense of absolute direction; think and gesture in cardinal terms even in unfamiliar buildings
- **Whorfian interpretation**: Using cardinal directions in language creates habitual attention to absolute space

### Number
- Pirahã (Everett): disputed, but languages with few number words show impaired exact number tracking
- Mundurukú speakers (Pica et al. 2004): approximate arithmetic intact; exact arithmetic for large numbers impaired — language for exact numbers may scaffold exact representation

### Time
- Mandarin speakers more likely to use vertical metaphors for time (earlier = up, later = down) than English speakers
- Priming with vertical spatial layout facilitates temporal reasoning in Mandarin speakers more than English

**The consensus summary**:
```
Language DOES:                        Language DOES NOT:
  Habituate attention                   Determine thought
  Influence categorization speed        Prevent thinking unnameable things
  Scaffold exact counting               Cause qualitatively different
  Affect memory encoding                cognition
  Modulate right-hemisphere             Override non-verbal inference
  processing                            for spatial/perceptual tasks
```

---

## Concepts and Categories

How does the mind represent knowledge of what things *are*?

### Classical View (Aristotle, traditional AI)
Concepts are defined by necessary and sufficient features.
- "Bachelor" = adult + male + unmarried
- "Triangle" = three-sided closed plane figure

**Problem** (Wittgenstein, "Philosophical Investigations"): Most everyday concepts don't have crisp defining features. What are the necessary and sufficient features of "game"? Of "furniture"? This is the **family resemblance** problem.

### Prototype Theory (Rosch 1975)
Concepts are organized around **best examples** (prototypes).

```
BIRD concept:
  Prototype: robin, sparrow (good birds — fly, sing, nest)
  Poor members: ostrich, penguin (bad birds — don't fly)
  Graded membership: is a bat a bird? closer to bird than fish?
```

**Empirical signatures**:
- **Typicality effects**: Typical members judged faster (robin = bird faster than penguin = bird)
- **Basic level advantage**: "Dog" faster to classify than "animal" or "golden retriever" — basic level is most natural
- **Graded membership**: Not all-or-nothing; membership is a matter of degree

**Problem**: Prototypes can't capture productivity or context-dependence. "Pet fish" ≠ average of pet prototype + fish prototype. "Small for an elephant" ≠ small.

### Theory-Theory (Carey 1985; Keil 1989)
Concepts are embedded in **intuitive theories** — not just lists of features or similarity to prototype, but causal/explanatory structure.

- You know a bat is *not* a bird because you know something about biological origins, not just appearance
- Transformation experiments (Keil): a skunk altered to look exactly like a raccoon is still judged a skunk by children who understand biological kinds

### Dual Basis: Prototype + Exemplar + Theory
Most psychologists now accept that concepts involve multiple representations:
- Prototype effects arise from both average-instance and exemplar storage
- Theories constrain what counts as relevant features
- Context selects which representation is active

---

## The Chomsky Hierarchy and Natural Language

The formal language hierarchy is the backbone of computational linguistics. The empirical question: **where does natural language sit?**

```
CHOMSKY HIERARCHY                    NATURAL LANGUAGE STATUS
──────────────────────────────────────────────────────────────────────────────
Type 3: Regular (FSA)                INSUFFICIENT
  Finite-state grammars               Cannot handle center-embedding:
  Right-linear rules                  "The cat [the dog [the rat bit] chased] fled"
  Chomsky (1956) proved this          Requires unbounded nesting → needs stack

Type 2: Context-Free (PDA)           ALMOST — but not quite
  Phrase-structure grammars           English: mostly CFG-parseable
  Pushdown automaton                  Swiss German: cross-serial dependencies
                                      (Shieber 1985) — provably not CF
                                      a^n b^m c^n d^m requires > CF power

Type 1: Context-Sensitive (LBA)      OVERSHOOT
  Too powerful — predicts structures
  natural languages don't exhibit

MILDLY CONTEXT-SENSITIVE             CURRENT CONSENSUS (Joshi 1985)
  Tree-Adjoining Grammars (TAG)       Captures cross-serial dependencies
  Combinatory Categorial Grammar      Polynomial parsing (not NP-hard)
  (CCG — Steedman)                    Slightly beyond CFG, well below CSG
  Linear Context-Free Rewriting       Most natural language constructions
  Systems (LCFRS)                     fit within this class
```

**The succession of formal grammar theories:**
- **Transformational Grammar** (Chomsky 1957–65): Deep structure → surface structure via transformations. Turing-complete if unconstrained.
- **GPSG** (Gazdar 1985): Context-free, no transformations. Handles most English but can't do Swiss German cross-serial.
- **LFG** (Bresnan): Functional structures + CFG c-structure. Mildly context-sensitive.
- **Minimalism** (Chomsky 1993+): Merge as the single combinatory operation. Computational status debated.

**The empirical bottom line**: Natural languages require slightly more than context-free power (Shieber's 1985 proof for Swiss German is definitive) but far less than context-sensitive. The "mildly context-sensitive" class — parseable in polynomial time, capturing limited cross-serial dependencies — is the current best formal characterization.

This directly constrains the Language of Thought debate below: if mental representations must support natural language productivity, they need at minimum mildly context-sensitive generative capacity — more than a finite-state machine, less than a Turing machine.

---

## Language of Thought — Mentalese (Fodor)

**Formal language theory connection**: Fodor's productivity argument — infinite thoughts from finite resources via recursive combination — is structurally identical to the argument that regular languages (FSA) cannot capture unbounded center-embedding. If you accept that thought exhibits productivity (unbounded recursive structure), you've already accepted that mental representations require at minimum pushdown-automaton-level (CFL) generative power. The systematicity argument (if you can think "A loves B" then you can think "B loves A") further requires that the combinatory operations preserve structural roles — this is compositionality, the same property that makes CFGs useful for parsing.

**The claim** (Jerry Fodor, "The Language of Thought," 1975):
Thinking is computation over a **structured symbolic mental language** (Mentalese) that is distinct from any natural language.

```
Natural language (English, Mandarin...)
    |
    v
Translation into / expression from
    |
    v
MENTALESE (the language of thought)
  - Compositional (JOHN LOVES MARY as structure)
  - Systematic (if you can think A loves B you can think B loves A)
  - Productive (infinite thoughts from finite vocabulary)
  - Amodal (not in any sensory modality)
  - Universal (shared across all humans, perhaps innate core)
```

**Arguments for LoT**:
1. **Systematicity**: Cognitive capacities come in systematic families. If you can think "John loves Mary," you can think "Mary loves John." This requires compositional structure.
2. **Productivity**: Infinite novel thoughts from finite resources → requires recursive combinatorial structure.
3. **Non-inferential learning**: Learning concepts requires innate conceptual primitives (you can't learn ALL your concepts by hypothesis formation from more basic concepts — infinite regress).

**Arguments against / modifications**:
- Connectionist challenge: Smolensky showed distributed representations can exhibit approximate systematicity without explicit symbols
- Embodied cognition: Concepts may be grounded in sensorimotor simulation (Barsalou "perceptual symbols"), not amodal symbols
- Neural imaging: conceptual knowledge is distributed in modality-specific areas (color concepts in color areas, motor concepts in motor areas)

**Current status**: The systematicity/productivity arguments are still the strongest case for LoT-like structure. Fodor won the *theoretical* argument but lost the empirical battle for radical nativism. Some kind of structured representation seems required; whether it's amodal symbols or structured sensorimotor patterns is open.

---

## Conceptual Metaphor (Lakoff & Johnson)

**"Metaphors We Live By"** (1980): Most abstract thought is structured by **conceptual metaphors** — systematic mappings from a concrete *source* domain to an abstract *target* domain.

These are not poetic flourishes — they *structure* cognition:

```
ARGUMENT IS WAR:
  "Your claims are indefensible"
  "She attacked every weak point"
  "His criticism was right on target"
  "I demolished his argument"

TIME IS MONEY:
  "Spending time"
  "Wasting time"
  "Saving time"
  "Running out of time"

UNDERSTANDING IS SEEING:
  "I see what you mean"
  "That's crystal clear"
  "I'm in the dark about this"
  "Let me shed light on that"
```

**Primary metaphors** (Lakoff & Johnson "Philosophy in the Flesh" 1999): arise from embodied experience:
- AFFECTION IS WARMTH (based on infant experience of warm contact)
- KNOWING IS SEEING (based on visual system's role in information)
- MORE IS UP (based on physical piles growing upward)

**Empirical support**:
- People are faster to respond to spatially consistent vs inconsistent prime-target pairs for metaphors
- Warming hands increases judgments of social warmth (Williams & Bargh 2008 — *failed to replicate robustly*)
- Holding heavy clipboards increases perception of importance of topics (Ackerman et al. — *replication mixed*)

**Caveat**: The *behavioral priming* studies supporting embodied metaphor have had a terrible replication record (priming effects in general). The linguistic evidence for conceptual metaphor is much more robust than the behavioral priming evidence.

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| Does language cause differences in color perception? | Yes, for adjacent color pairs straddling a lexical boundary, lateralized to left hemisphere |
| Can Pirahã speakers count? | Approximately, but not exactly for large numbers — disputed |
| Why is the Wason task hard? | Formal conditional logic is not naturally computed; deontic framing reveals domain-specific social-rule competence |
| Where is language in the brain? | Distributed left-hemisphere network (Broca + Wernicke + arcuate + angular gyrus + STG); not just two spots |
| What's a concept? | Prototype structure + exemplar similarity + embedded causal theory; multiply represented |
| Is there a Language of Thought? | Something like structured compositional representations seems required; amodal vs grounded debate open |
| Do conceptual metaphors shape thought? | The linguistic evidence is robust; the behavioral priming evidence is mostly failed replications |

---

## Common Confusion Points

**Broca's area ≠ "production only"**: Patients with Broca's aphasia have production deficits but also subtle syntactic comprehension deficits (especially for non-canonical sentence structures). Broca's area contributes to syntax comprehension, not just articulation.

**Wernicke's area ≠ "just comprehension"**: Wernicke's aphasia impairs comprehension, but patients also produce fluent but senseless output (word salad, paraphasias). The area contributes to lexical-phonological mapping, which affects both input and output.

**Sapir-Whorf is not "does language affect thought at all"**: The question is the *form* and *depth* of the influence. Nobody denies that learning a new word helps you think about the concept. The debate is about whether language *restructures* perceptual/spatial/numerical cognition and whether the effects operate online in non-linguistic tasks.

**Conceptual metaphors ≠ linguistic metaphors**: Lakoff's claim is about the *underlying conceptual structure*, not the surface expression. The metaphors are in the thought, not just the language. "I see what you mean" is evidence of the UNDERSTANDING IS SEEING metaphor whether or not you consciously use it as a metaphor.

**The Chomsky hierarchy's empirical status for natural language** (see the full treatment in the Chomsky Hierarchy section above): Natural language is provably not context-free (Shieber 1985, Swiss German cross-serial dependencies) but sits within the mildly context-sensitive class (TAGs, CCG). This directly bears on both the Sapir-Whorf and LoT discussions: if the computational complexity of a language's grammar varies (some constructions require more than CF power), does that affect the cognitive resources required to process those constructions? The evidence suggests yes — processing garden-path sentences with center-embedding is measurably harder than processing right-branching equivalents, consistent with the stack depth required by a pushdown automaton.

**Cross-reference**: For the formal linguistic treatment of syntax and semantics (Chomsky hierarchy, lambda calculus semantic composition), see `linguistics/03-SYNTAX.md` and `linguistics/04-SEMANTICS.md` (Session 12). For the neural implementation of language areas, see `neuroscience/02-SYSTEMS-CIRCUITS.md`.
