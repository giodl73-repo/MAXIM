# Linguistics — Overview & Theoretical Foundations

## The Big Picture: What Linguistics Studies

Linguistics is the scientific study of language — not prescriptive rules ("don't split infinitives"), but the systematic structure that lets humans acquire, produce, and understand language at all.

```
+------------------------------------------------------------------+
|              THE LINGUISTICS PIPELINE — LAYERED SYSTEM           |
|                                                                  |
|  PHONETICS / PHONOLOGY                                           |
|  (sound inventory, phoneme rules, prosody)                       |
|  Output: segmented phoneme stream                                |
|                        |                                         |
|                        v  feeds                                  |
|  MORPHOLOGY                                                      |
|  (morpheme segmentation, inflection, derivation)                 |
|  Output: words with internal structure labeled                   |
|                        |                                         |
|                        v  feeds                                  |
|  SYNTAX                                                          |
|  (phrase structure, movement, binding)                           |
|  Output: hierarchical tree with grammatical relations            |
|                        |                                         |
|                        v  feeds                                  |
|  SEMANTICS                                                       |
|  (truth conditions, compositionality, λ-calculus)               |
|  Output: logical form — meaning representation                   |
|                        |                                         |
|                        v  feeds                                  |
|  PRAGMATICS                                                      |
|  (speaker intent, implicature, discourse)                        |
|  Output: interpreted utterance in context                        |
|                                                                  |
|  CROSS-CUTTING:                                                  |
|  Historical Linguistics (change over time — diachronic layer)    |
|  Sociolinguistics (variation by speaker/community)               |
|  Language Acquisition (how the pipeline is built)               |
|  Computational Linguistics / NLP (formal + statistical models)   |
+------------------------------------------------------------------+
```

The subfields nest and feed each other. Syntax draws on morphology; semantics builds on syntax; pragmatics extends semantics into discourse.

---

## Module Map

| File | Subfield | TCS Bridge |
|------|----------|------------|
| `00-OVERVIEW.md` | Foundations + frameworks | Chomsky hierarchy |
| `01-PHONETICS-PHONOLOGY.md` | Sound systems | Phonological rules as rewriting |
| `02-MORPHOLOGY.md` | Word structure | Morphological parsing |
| `03-SYNTAX.md` | Sentence structure | CFG, X-bar, minimalism |
| `04-SEMANTICS.md` | Meaning | λ-calculus, type theory |
| `05-PRAGMATICS.md` | Meaning in context | Game theory, Bayesian inference |
| `06-HISTORICAL-LINGUISTICS.md` | Language change | PIE reconstruction, comparative method |
| `07-LANGUAGE-ACQUISITION.md` | How children learn | Poverty of stimulus, UG vs statistical learning |
| `08-SOCIOLINGUISTICS.md` | Language + society | Variationist quantitative methods |
| `09-COMPUTATIONAL-LINGUISTICS.md` | NLP + formal grammars | CYK, Earley, neural language models |

---

## Part I: Saussurean Foundations

Ferdinand de Saussure (1857–1913) established the framework that modern linguistics still debates and extends.

### The Sign

```
+-------------------------------------------------+
|                THE LINGUISTIC SIGN               |
|                                                 |
|   SIGNIFIER                  SIGNIFIED          |
|   (sound image /kæt/)  <-->  (concept of CAT)  |
|                                                 |
|   The bond between them is ARBITRARY           |
|   "cat" / "chat" / "Katze" — all for same beast|
|   Only exceptions: onomatopoeia (weak)         |
+-------------------------------------------------+
```

**Key Saussurean distinctions:**

| Concept | Definition | Modern restatement |
|---------|------------|--------------------|
| **Langue** | The abstract language system shared by a community | Grammatical competence, I-language |
| **Parole** | Actual speech acts by individuals | Performance, E-language |
| **Syntagmatic** | Relationships along the linear chain ("The cat sat") | Sequential / combinatorial axis |
| **Paradigmatic** | Relationships between items that could substitute ("cat/dog/hat") | Substitutional axis |
| **Synchronic** | Language at one point in time | A snapshot |
| **Diachronic** | Language change over time | Historical linguistics |
| **Arbitrariness** | No natural link between form and meaning | Except iconicity (see below) |

**Arbitrariness vs. Iconicity:**
The claim is not absolute. Onomatopoeia (buzz, crash) is iconic. Phonetic symbolism: in ~70% of languages, "small" meanings favor front vowels (/i/ — "tiny", "petit") over back vowels. But these are edges — the system is overwhelmingly arbitrary.

---

## Part II: Chomsky's Revolution — Competence vs. Performance

### The Core Distinction

```
COMPETENCE                          PERFORMANCE
(I-language, internalized)          (E-language, external)
+---------------------------+       +---------------------------+
| The mental grammar:        |       | Actual utterances:         |
| - phonological rules       |       | - contain errors           |
| - morphological rules      |       | - trail off                |
| - syntactic rules          |       | - are interrupted          |
| - semantic rules           |       | - reflect memory limits    |
|                            |       | - show false starts        |
| This is what linguistics   |       |                            |
| should model               |       | This is what you hear      |
+---------------------------+       +---------------------------+
```

Linguistics aims to characterize the abstract **competence** system, not predict every messy performance token. This is the same move as: analyze quicksort as an algorithm, not profile every execution.

### Universal Grammar (UG)

Chomsky's central hypothesis:

```
POVERTY OF THE STIMULUS ARGUMENT
+---------------------------------------------------------------+
|  Children receive:                                            |
|  - incomplete, error-filled input (performance)              |
|  - no explicit negative evidence ("*goed is wrong")          |
|  - finite data                                               |
|                                                              |
|  Yet they converge on:                                        |
|  - the same complex grammar at roughly the same age          |
|  - grammaticality judgments for sentences never heard        |
|  - cross-linguistic structural regularities                  |
|                                                              |
|  Conclusion: part of grammar must be innate — UG             |
+---------------------------------------------------------------+
```

**UG principles proposed:**

| Principle | Example | Language(s) |
|-----------|---------|-------------|
| Structure-dependence | Rules operate on constituents, not linear position | All languages |
| Movement leaves traces | "What did you see ___?" — "what" moved, trace remains | All languages with wh-movement |
| Subjacency / Islands | Can't extract from within certain phrase types | Cross-linguistically robust |
| ECP (Empty Category Principle) | Constraints on what can be deleted/moved | Generative tradition |
| Binding conditions A/B/C | Reflexives, pronouns, and names have distinct binding requirements | Universal (with parameter variation) |

**Parameters:** Where languages vary (head-initial vs. head-final, null-subject allowed vs. not, wh-in-situ vs. wh-fronting). The **Principles & Parameters** approach: UG fixes the principles; acquisition is setting the parameters on exposure.

---

## Part III: Usage-Based Alternative

The nativist UG account has a serious challenger: **usage-based linguistics** (Tomasello, Goldberg, Langacker).

```
NATIVIST VIEW                       USAGE-BASED VIEW
+---------------------------+       +---------------------------+
| Rich innate UG             |       | Minimal innate substrate   |
| Grammar is modular         |       | Grammar = statistical      |
| Acquisition = parameter    |       |   patterns over usage      |
|   setting                  |       | Acquisition = statistical  |
| Competence ≠ performance   |       |   learning + intention-    |
| Poverty of stimulus is     |       |   reading                  |
|   real                     |       | Poverty of stimulus is     |
|                            |       |   overstated — input is    |
|                            |       |   richer than claimed      |
+---------------------------+       +---------------------------+
```

Key evidence for usage-based:
- Verb island constructions (children learn "I want X" before abstract DO NP) — item-specific learning
- Statistical learning: 8-month-olds segment words from fluent speech via transition probabilities (Saffran et al. 1996)
- Frequency effects persist in adults — high-frequency irregulars resist regularization ("went" not "*goed")

Key evidence for nativist:
- Cross-linguistic UG effects (island constraints in unrelated languages)
- Species-specificity — no other species acquires language naturally
- Critical period evidence

**Current consensus:** Neither extreme. Statistical learning is real and powerful; some biologically-determined language-specific structure also appears likely.

---

## Part IV: The Sapir-Whorf Spectrum

```
STRONG DETERMINISM                    WEAK RELATIVITY
(discredited)                         (empirically supported)
+-------------------+                 +--------------------+
| Language determines|                 | Language influences |
| thought. Without a |                 | cognition in soft,  |
| word for "blue" you|                 | domain-specific,    |
| cannot perceive    |                 | measurable ways     |
| blue.              |                 |                     |
+-------------------+                 +--------------------+
         |                                     |
         X (falsified by color perception      v
           experiments in Pirahã, Zuni,   Supported examples:
           Dani — can discriminate fine    - Russian: lexical blue/
           color distinctions despite        glight-blue → faster
           impoverished color vocabulary)    discrimination
                                          - Pirahã: no recursion →
                                            no counting?
                                          - Turkish: evidential mood
                                            → attention to info source
                                          - Spatial frames (absolute
                                            vs relative) → navigation
                                            strategies differ
```

Boroditsky's experiments: Spanish/German grammatical gender for nouns correlates with gendered descriptions in unrelated tasks (bridges: "elegant" in Spanish — *puente* is masc; "sturdy" in German — *Brücke* is fem). Effect is real but modest.

---

## Part V: The Chomsky Hierarchy — The TCS Bridge

You know this cold from 6.840/6.045. Here's how it maps onto linguistics:

```
CHOMSKY HIERARCHY (TCS)              LINGUISTIC REALIZATION
+-------------------------------+    +---------------------------+
|  Type 0                        |    | Unrestricted grammar       |
|  Unrestricted grammars         |    | (beyond natural language)  |
|  Turing machines               |    |                            |
+-------------------------------+    +---------------------------+
         ⊃
+-------------------------------+    +---------------------------+
|  Type 1                        |    | Context-sensitive grammar  |
|  Context-sensitive grammars    |    | Some cross-serial          |
|  Linear-bounded automata       |    | dependencies in Swiss      |
|                                |    | German subordinate clauses |
+-------------------------------+    +---------------------------+
         ⊃
+-------------------------------+    +---------------------------+
|  Type 2                        |    | Context-free grammar       |
|  Context-free grammars         |    | MOST syntactic structure:  |
|  Pushdown automata             |    | phrase structure rules,    |
|                                |    | X-bar theory, PCFG in NLP  |
+-------------------------------+    +---------------------------+
         ⊃
+-------------------------------+    +---------------------------+
|  Type 3                        |    | Regular grammar            |
|  Regular grammars              |    | Morphological patterns:    |
|  Finite-state automata         |    | simple affixation,         |
|                                |    | agreement paradigms        |
+-------------------------------+    +---------------------------+
```

**Key results from formal linguistics:**

1. **Finite-state is not enough for syntax**: Center-embedding requires a stack. English "The rat the cat the dog chased killed ate the malt" is grammatical (barely processable) — demonstrating nested push-down structure.

2. **Natural languages are mildly context-sensitive**: Shieber (1985) showed Swiss German cross-serial dependencies require at least indexed grammars (beyond CFG). The claim "natural languages are context-free" (Chomsky 1956) is false.

3. **But**: For most practical purposes, PCFGs (probabilistic CFGs) approximate natural language syntax well enough for parsing. The extra power (CSL) is needed only for specific constructions.

4. **TAG, CCG, HPSG**: Modern syntactic formalisms that sit between CFG and CSG — exactly the mild context-sensitivity natural languages need.

```
FORMAL POWER NEEDED FOR NATURAL LANGUAGE:
  Morphology → Type 3 (finite state, with some exceptions)
  Most syntax → Type 2 (CFG / PCFG)
  Cross-serial deps → Type 1 (context-sensitive / TAG)
  Full semantics → Type 0 (undecidable in general)
```

---

## The Compiler-Pipeline Bridge

The pipeline diagram above is not a coincidence. Natural language processing and compiler design are the same problem at different levels of formalization:

```
COMPILER STAGE           LINGUISTIC STAGE         WHAT IT DOES
-----------------        ----------------         ----------------
Lexer / tokenizer        Phonology +              Segments raw signal into
                         Morphology               discrete units with type
                                                  labels (tokens = words
                                                  with morphological analysis)

Parser                   Syntax                   Builds hierarchical
                                                  structure from token
                                                  stream — the parse tree
                                                  IS a phrase-structure tree

Type checker             Semantics                Validates well-formedness
                                                  at the meaning level;
                                                  compositional type
                                                  derivation (Montague:
                                                  λ-calculus over types
                                                  e and t) mirrors
                                                  bidirectional type inference

Optimizer /              Pragmatics               Transforms the logical
 dead-code analyzer                               form to serve the actual
                                                  communicative goal —
                                                  "what does this DO,
                                                  given context?"

Runtime / linker         Discourse /              Resolves external
                         Coreference              references, manages
                                                  shared state across
                                                  multiple utterances
```

**The key difference:** Compilers process an unambiguous formal language with a deterministic grammar; natural language is massively ambiguous at every level and requires probabilistic or game-theoretic disambiguation. The formal pipeline exists; it just runs on noisy, underspecified input.

**The formal parallel runs deep:** CYK parsing of PCFGs is structurally identical to Viterbi decoding in HMMs. The inside-outside algorithm (for PCFG parameter estimation) is the forward-backward algorithm under a different name. Formal language theory and computational linguistics are not analogous — they are the same mathematical substrate applied to different input alphabets.

---

## Part VI: Linguistics as Science

### Data types

| Data type | Description | Reliability |
|-----------|-------------|-------------|
| **Grammaticality judgments** | Native speaker introspection: ✓ or ✗ | High for clear cases; fuzzy at edges |
| **Corpus data** | What people actually say/write | Reflects performance + competence |
| **Experimental psycholinguistics** | RT, eye-tracking, ERP | Reveals processing, not always grammar |
| **Cross-linguistic typology** | Frequency of patterns across languages | Reveals tendencies, not universals |
| **Fieldwork** | Eliciting data from understudied languages | Ground truth for typological claims |
| **Computational modeling** | Fit models to corpus | Tests formal hypotheses |

### Major theoretical frameworks

| Framework | Core idea | Proponent | Active? |
|-----------|-----------|-----------|---------|
| **Generative grammar / Minimalism** | Innate UG; Merge as core operation | Chomsky | Yes |
| **Head-Driven Phrase Structure Grammar** | Constraint-based, lexicalist, no movement | Pollard & Sag | Yes |
| **Lexical-Functional Grammar** | Two levels: c-structure + f-structure | Bresnan | Yes |
| **Construction Grammar** | Form-meaning pairings as primitives | Goldberg, Fillmore | Yes |
| **Role and Reference Grammar** | Crosslinguistic typology-first | Van Valin | Yes |
| **Cognitive Linguistics** | Language in general cognition; schemas | Langacker, Lakoff | Yes |
| **Dependency Grammar** | Labeled arcs not phrase structure | Tesniére | Yes (in NLP: UD) |

---

## Decision Cheat Sheet — Which Subfield?

| Question type | Subfield |
|---------------|----------|
| Why can't I say "*I saw yesterday John"? | Syntax |
| What does "bank" mean in context? | Pragmatics / Semantics |
| Why does "feet" not follow "foot + -s" rule? | Morphology |
| Where does the English vowel shift come from? | Historical Linguistics |
| Why do children say "goed" then self-correct? | Language Acquisition |
| Why do New Yorkers drop /r/ in some contexts? | Sociolinguistics |
| How does CYK parsing work? | Computational Linguistics |
| What's the truth condition of "The king of France is bald"? | Formal Semantics |
| What's the difference between /p/ and /b/? | Phonetics / Phonology |
| What did the speaker imply vs. literally say? | Pragmatics |

---

## Common Confusion Points

**"Chomsky hierarchy" vs. "Chomsky's linguistics":**
The hierarchy is from his 1956 formal language paper. His generative syntax (Minimalism, GB theory) is a separate body of work. They connect but are distinct research programs.

**"Universal" doesn't mean "in all languages":**
Linguistic universals are either *absolute* (truly in every language) or *implicational* (if a language has X, it has Y). Most "universals" are the latter. Don't confuse UG (the innate mechanism) with typological universals (cross-linguistic tendencies).

**Competence is not performance:**
You can be a fully competent native speaker and make performance errors constantly. Grammaticality judgments probe competence; corpus frequencies probe the interaction of competence + processing + social factors.

**Sapir-Whorf is not dead — just weakened:**
Strong determinism (no thought without words) is falsified. Weak relativity (language shapes perception in measurable ways) has solid experimental support. Don't dismiss it entirely.

**Linguistics is not language learning:**
A linguist studying Mandarin phonology doesn't necessarily speak Mandarin. The object of study is the system, not the skill.

**Prescriptivism vs. descriptivism:**
Linguistics is descriptive. "Ain't" and "he don't" are linguistically systematic (with regular paradigms) even if nonstandard. The linguist's job is to describe the system, not enforce schoolbook norms.
