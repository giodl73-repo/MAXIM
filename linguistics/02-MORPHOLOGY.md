# Morphology — The Structure of Words

## The Big Picture

Morphology is the study of word structure — how morphemes combine to form words.

```
+----------------------------------------------------------------+
|                    MORPHOLOGY LANDSCAPE                         |
|                                                                |
|  MORPHEMES                    WORD FORMATION                  |
|  (minimal meaningful          Affixation: pre/in/suf/circum   |
|   units)                      Compounding: blackbird           |
|  +---------+                  Conversion: "to google"          |
|  | FREE     | — stand alone   Reduplication: zig-zag          |
|  | "cat"    |                 Clipping: advertisement→ad      |
|  +---------+                  Blending: smoke+fog=smog        |
|  | BOUND    | — must attach                                    |
|  | -s, pre- |                                                  |
|  +---------+                                                   |
|                                                                |
|  INFLECTION vs. DERIVATION                                     |
|  Inflection: grammatical   Derivation: creates new word       |
|  words → same lexeme       "teach" → "teacher" (new lexeme)   |
|  "walk/walks/walked"       "happy" → "unhappy" (new adjective)|
+----------------------------------------------------------------+
```

---

## Part I: Morphemes

**Morpheme**: the minimal unit of meaning or grammatical function.

```
"antidisestablishmentarianism"

ANTI + DIS + ESTABLISH + MENT + ARI + AN + ISM

anti-     (prefix: against)
dis-      (prefix: reversal/negation)
establish (root: free morpheme)
-ment     (suffix: action/result nominalization)
-ari      (suffix: relating to)
-an       (suffix: person associated with)
-ism      (suffix: ideology/doctrine)

7 morphemes. One word.
```

### Morpheme Classification

```
MORPHEMES
├── FREE (can stand alone)
│   ├── Content: cat, run, big, quickly (nouns, verbs, adjectives, adverbs)
│   └── Function: the, and, of, will (determiners, conjunctions, prepositions, auxiliaries)
│
└── BOUND (must attach to something)
    ├── Affixes
    │   ├── Prefix: un-, pre-, anti-, mis-
    │   ├── Suffix: -ness, -tion, -er, -s (past/plural/etc.)
    │   ├── Infix: -in- in "abso-bloody-lutely" (expressive, rare in English)
    │   └── Circumfix: ge-...-t in German past participle: ge+lern+t ("learned")
    │
    ├── Clitic (phonologically bound, but syntactically free)
    │   ├── Proclitic: French "le" in "le chat" (attached to following word)
    │   └── Enclitic: "'s" in "John's", "'ll" in "I'll" (attached to preceding word)
    │
    └── Root (bound root): -ceive (perceive, receive, conceive) — can't stand alone
```

### Morphs, Morphemes, and Allomorphs

Same abstraction as phoneme/allophone, one level up:

```
MORPHEME /plural/  →  morphs: [s], [z], [ɪz], and zero plural (sheep → sheep)
MORPHEME /past/    →  morphs: [t], [d], [ɪd], and ablaut (sing → sang, go → went)
MORPHEME /negation/→  morphs: un- (unhappy), in- (incomplete), im- (impossible),
                               il- (illegal), ir- (irregular) — place assimilation
```

**Suppletion**: allomorphs with no phonological relation — go/went, good/better, bad/worse. The morpheme is the same (/comparative/, /past/) but the forms are historical accidents.

---

## Part II: Affixation — All Types

### Prefix and Suffix (most common)

| Affix type | Position | English examples |
|------------|----------|-----------------|
| **Prefix** | Before root | un-happy, pre-view, mis-understand, dis-agree, re-write, anti-war |
| **Suffix** | After root | happi-ness, teach-er, nation-al, walk-ed, cat-s, beauti-ful |

### Less Common in English, Common Cross-linguistically

| Type | Position | Description | Example |
|------|----------|-------------|---------|
| **Infix** | Inside root | Morpheme inserted into root | Filipino: *sulat* (write) → *s-um-ulat* (wrote) — *um* infixed |
| **Circumfix** | Around root | Prefix + suffix as single morpheme | German: *ge-lern-t* (learned); Malay: *ke-besar-an* (bigness) |
| **Interfix** | Between morphemes | Linking element, no meaning | German: *Arbeit-s-platz* (workplace) — *-s-* is interfix |
| **Transfix** | Interspersed | Non-contiguous affixation | Arabic trilateral roots: K-T-B (write) + template → *katab* (he wrote), *kitāb* (book), *kātib* (writer) — vowel pattern is transfix |
| **Simulfix** | Replacement | Affix replaces part of root | — (theoretical; some ablaut analyses) |

---

## The Compiler Front-End Bridge

Morphological analysis is the linguistic equivalent of lexing + symbol-table lookup. The parallels are exact enough to be used directly as mental models:

```
COMPILER FRONT-END               MORPHOLOGICAL ANALYSIS
------------------               ----------------------
Lexer / tokenizer                Morphological segmenter:
                                 "readers" → [read][er][s]
                                 token boundaries ≈ morpheme boundaries

Token type (NUM, IDENT, OP)      Morpheme class:
                                 root (read), agentive suffix (-er),
                                 plural inflection (-s)

Symbol table / identifier        Lemma / lexeme:
  resolution                     "walked", "walks", "walking" all point
                                 to the same lexeme WALK —
                                 morphological analysis = lemmatization

Maximal munch rule               Maximal onset principle in syllabification;
                                 morpheme boundary disambiguation:
                                 "un-lock-able" = (un-)(lock)(able) or
                                 (un-)(lock-able)?  Scope ambiguity.

Regex-based lexer rules          Finite-state transducer (FST):
                                 morphological analysis implemented as
                                 an FST mapping surface forms to
                                 underlying morpheme sequences.
                                 (Koskenniemi 1983 two-level morphology —
                                 the standard for morphological tools.)

Lexer state machine              Phonologically conditioned allomorph
                                 selection: in- → im- before bilabials,
                                 il- before laterals. The allomorph
                                 selector is a finite-state transducer
                                 operating on the surface phonology.
```

**Typology maps to implementation strategy:**

| Morphological type | Parsing strategy | Analogy |
|---------------------|-----------------|---------|
| Isolating (Mandarin) | No morphology needed; tokenize on whitespace | Keywords only; no compound tokens |
| Agglutinative (Turkish) | Stack-based FST; strip suffix stack left-to-right | Left-recursive grammar; each suffix = one rule application |
| Fusional (Latin, Russian) | Paradigm table lookup; can't decompose further | Overloaded operators; one token encodes multiple semantic dimensions |
| Polysynthetic (Mohawk) | Full clause parser required to analyze one "word" | Macro expansion; a single token expands to a full AST |

**The FST connection:** Production-quality morphological analyzers (Foma, HFST, the Xerox tools) are literally finite-state transducers. The morpheme composition rules you write are transducer compositions. Context-free morphology (for polysynthetic languages) requires pushdown transducers. The Chomsky hierarchy applies here exactly as in formal language theory.

---

## Part III: Morphological Typology

Languages differ fundamentally in how morphology works:

```
MORPHOLOGICAL TYPOLOGY SPECTRUM

ISOLATING ←————————————————————→ SYNTHETIC ←—————→ POLYSYNTHETIC

Low morpheme/    Agglutinative:    Fusional:         Many morphemes
word ratio       one morpheme      morphemes fuse,   per word,
                 per slot, clear   hard to segment   clause in
                 boundaries                           one word
```

### Four Types with Examples

**1. Isolating (Analytic)**

One morpheme per word. Grammar expressed by word order and separate function words, not affixes.

```
MANDARIN:
  wǒ  gěi  tā  mǎi  le   yī  zhāng  shū
  I   give he  buy  PFV  one CL     book
  "I bought him a book"

  No affixes. PFV marker (了) is a separate particle.
  Zero inflection for person, number, tense — all context/particles.
```

Other isolating languages: Vietnamese, Thai, some creoles.

**2. Agglutinative**

One meaning per morpheme, morphemes stack transparently. Clear segment boundaries.

```
TURKISH:
  ev-ler-im-de-ki-ler-den
  house-PL-1SG.POSS-LOC-REL-PL-ABL
  "from those (things) in my houses"

  8 morphemes, 7 suffixes, each adds exactly one meaning.
  Stack them up, peel them off — like a data structure.

SWAHILI:
  ni-li-m-piga
  1SG.SUBJ-PAST-3SG.OBJ-hit
  "I hit him/her"

JAPANESE:
  tabe-rare-nakat-ta
  eat-POTENTIAL-NEG.PAST-PST
  "could not eat"
```

**3. Fusional (Inflectional)**

Morphemes fuse — one affix conveys multiple meanings simultaneously. Harder to segment.

```
LATIN:
  amo  =  am + o
  "I love"  =  love + 1SG.PRES.ACT.IND (all bundled in -o)

  amaba-m = love + IMPERFECT + 1SG (bundled in -bam → -m isn't separable from -ba-)

  portarum = porta + rum
  "of the gates" = gate + GEN.PL.FEM (three features, one suffix)

RUSSIAN:
  stol-a = table + GEN.SG (two features in -a, not separable)
  stol-y = table + NOM.PL (same -y that also appears in other cases for other nouns)
```

**4. Polysynthetic**

Words encode entire clauses. Morphemes incorporate arguments (subjects, objects) into the verb.

```
MOHAWK (Iroquoian):
  wa'kenaktahkwenies
  wa'-k-en-akt-ahkw-en-ie-s
  PAST-1SG.SUBJ-1SG.OBJ-bed-carry-TRANS-BEN-HAB
  "I usually carry around a bed for myself"

  One word = a full clause in English.

YUPIK (Eskimo-Aleut):
  tuntussuqatarniksaitengqiggtuq
  "He had not yet said again that he was going to hunt reindeer"
```

### Typological Metrics

| Metric | Definition | Isolating | Agglutinative | Fusional |
|--------|------------|-----------|---------------|---------|
| **Synthesis index** | Morphemes per word | ~1.0–1.5 | ~2–3 | ~2–3 |
| **Fusion index** | Morpheme-meaning pairs per morpheme | ~1 | ~1 | >1 |
| **Agglutination index** | Unambiguous segment boundaries | N/A | High | Low |

No language is a pure type — these are tendencies. English is historically fusional (from Proto-Indo-European) but has shifted toward analytic: losing case endings, relying on word order.

---

## Part IV: Inflection vs. Derivation

This is a crucial distinction:

```
INFLECTION                           DERIVATION
+-------------------------------+   +-------------------------------+
| Grammatically required        |   | Lexically creative             |
| Stays same lexeme/lexical class|   | Typically creates new lexeme   |
| Not listed separately in dict |   | Listed as separate entry       |
| Highly regular, few exceptions|   | Less regular, more idiosyncratic|
| Outer position in word        |   | Inner position (closer to root)|
+-------------------------------+   +-------------------------------+

INFLECTION examples:
  walk / walks / walked / walking — all the SAME word in different forms
  cat / cats — same word
  big / bigger / biggest — same adjective

DERIVATION examples:
  teach → teacher (new noun, different meaning)
  happy → unhappy (same class, opposite meaning)
  nation → national → nationalize → nationalization (each = new lexeme)
```

**The "outer layer" principle**: In most languages, inflectional morphology is outside (further from root) derivational morphology:

```
ROOT + DERIVATION + INFLECTION
  nation + al + ize + ation + s   (nations becomes nationalization's final form via derivation first)
  teach + er + s                   (teacher-s: derive first, then inflect for plural)
```

Counter-examples exist (especially in polysynthetic languages), but this ordering is a robust cross-linguistic tendency.

---

## Part V: Word Formation Processes

Beyond affixation:

### Compounding

Two or more roots combined:

```
blackbird ≠ black + bird  (blackbirds can be non-black; black birds can be non-blackbirds)
greenhouse ≠ green + house
heartburn — semantic bleaching
software — historical compound, now lexicalized

HEAD = the rightmost element in English: blackBIRD is a BIRD
       greenhouse is a HOUSE (semantically + grammatically)
```

Languages differ in compound headedness:
- English: right-headed (blackbird = a BIRD)
- Hebrew: left-headed (*beit sefer* = house-of-book = school; *beit* is head)
- German: right-headed (Abgasskandal = Abgas+Skandal = exhaust+scandal = diesel scandal)

### Conversion (Zero Derivation)

Change word class with no affix:
```
  to google (noun → verb)
  to text (noun → verb)
  a must (verb → noun)
  a google (proper noun → common noun)
  to up the ante (preposition → verb)
```

### Reduplication

Full or partial copying of root:

```
FULL: Malay buku-buku (book-book = plural)
PARTIAL: English zig-zag, ping-pong, tick-tock (ablaut reduplication)
REDUPLICATION for aspect: Tagalog: bili (buy) → bibili (will buy)
INTENSIVE reduplication: "very very" in many languages
```

### Clipping

```
advertisement → ad
examination → exam
laboratory → lab
microphone → mic/mike
gymnasium → gym
```

### Blending

```
smoke + fog = smog
breakfast + lunch = brunch
motor + hotel = motel
web + log = blog
pixel = picture + element
```

### Acronyms and Initialisms

```
ACRONYM (pronounced as word): laser, radar, scuba, NATO, UNESCO
INITIALISM (spelled out): FBI, CIA, IBM, SQL (pronounced "sequel" by some, initialism by others)
CLIPPING of phrase: sci-fi, hi-fi, A/C
```

### Backformation

Removing what looks like an affix:

```
editor → edit (back-formed from editor, as if editor = edit + -or)
pea — originally "pease" (singular), reanalyzed as plural → "pea" formed as singular
laze — back-formed from lazy
enthuse — back-formed from enthusiasm
```

---

## Part VI: Paradigms and Gaps

A **paradigm** is the full set of inflected forms for a lexeme:

```
LATIN NOUN PARADIGM (porta, -ae: gate):
         Singular    Plural
NOM      porta       portae
GEN      portae      portarum
DAT      portae      portis
ACC      portam      portas
ABL      porta       portis
VOC      porta       portae

6 cases × 2 numbers = 12 cells. The 1st declension has several syncretisms
(DAT.SG = GEN.SG = portae).
```

**Paradigm gaps (defective paradigms):** Some cells are simply missing — no form exists:

```
English: "beware" — only exists as imperative. *"I bewared" is ungrammatical.
Latin: "odi" (I hate) — only perfect forms exist. Present *"odio" doesn't exist.
French: "quérir" (to fetch) — used only in infinitive, never conjugated
Pluralia tantum: scissors, pants, glasses — only plural, no singular
```

**Suppletion revisited**: go/went, good/better — forms from historically different roots, but treated as one paradigm.

---

## Part VII: Allomorphy in Depth

Multiple morphs for one morpheme, conditioned by:

### Phonologically conditioned (predictable by rule)

```
English negation prefix:
  in-    before alveolars: in-complete, in-sane
  im-    before bilabials: im-possible, im-mature
  il-    before laterals: il-legal, il-literate
  ir-    before rhotics: ir-regular, ir-responsible
  i-     before nasals: i-mmune? (→ im-)

This is NASAL PLACE ASSIMILATION — the morpheme /in-/ assimilates
to the place of the following consonant.
```

### Morphologically conditioned (lexically specified)

```
English past tense:
  WEAK (regular): -ed → walked, jumped, painted
  STRONG (ablaut): sing/sang/sung, drive/drove/driven — class-specific vowel change
  SUPPLETIVE: go/went

The strong verb classes are memorized lexically; cannot be predicted from phonology alone.
```

### Grammatically conditioned

```
Russian genitive plural:
  After numerals 2-4: GEN.SG — "три дня" (three day-GEN.SG)
  After numerals 5+: GEN.PL — "пять дней" (five day-GEN.PL)
  (Historical: 2-4 took dual, 5+ took genitive plural. Dual is gone; GEN.SG remains for 2-4.)
```

---

## Decision Cheat Sheet

| Question | Analysis | Tool |
|----------|----------|------|
| Is "-er" in "teacher" vs "quicker" the same morpheme? | No — derivational vs comparative. Different morphemes, phonologically identical. | Inflection vs. derivation |
| How do I analyze Turkish word structure? | Stack morphemes in slots — agglutinative. | Morphological typology |
| Why does "mice" not follow the {-s} rule? | Ablaut (umlaut) — old Germanic morphological process, now lexicalized. | Allomorphy / suppletion |
| What's the head of "bookseller"? | "-seller" — rightmost element → English is right-headed. | Compound headedness |
| Can "obligate" be derived from "obligation"? | Yes — backformation (probably). Or independent derivation from Latin. | Word formation |
| Why no plural "scissors" → scissor? | Pluralia tantum — paradigm gap. Scissors is only plural. | Paradigm gaps |
| Is circumfix a real thing or two separate affixes? | Genuinely disputed — some analyses decompose, some treat as unitary. | Theoretical choice |

---

## Common Confusion Points

**Morpheme ≠ syllable:**
"Cats" = 1 syllable, 2 morphemes. "Understand" = 3 syllables, technically 2 morphemes (under + stand), though "stand" here is arguably a bound root. "Monkeys" = 2 syllables, 2 morphemes. "Cranberry" — "cran" is a *cranberry morph*: a bound morpheme with no meaning outside compounds (cranberry, cranberry sauce).

**Inflection creates word forms, not new words:**
"Walked" is not a different word from "walk" — it's a different **form** of the same word (lexeme). Dictionaries list "walk," not "walk/walks/walked/walking" separately.

**Agglutinative ≠ morphologically simple:**
Turkish is the opposite of simple — it's incredibly complex morphologically. "Agglutinative" means transparent, stackable morphology, not little morphology.

**"-ly" in English is not always the same morpheme:**
"Quick-ly" (adverb derivation, adjective → adverb) vs. "friend-ly" (adjective derivation, noun → adjective) — same phonological form, arguably two morphemes (or the same morpheme with broader scope).

**Homophony across morphemes:**
English -er: comparative (big-ger), agentive (teach-er), instrumental (open-er), locative (New York-er). Four different morphemes with the same phonological form. Context resolves.

**Zero morphemes are not nothing:**
"Sheep" plural is analyzed as sheep + ∅PL. The zero morpheme is licensed by the grammar to mark plural — it's not "no morphology," it's a morpheme with zero phonological realization. Controversial, but widely used in morphological theory.
