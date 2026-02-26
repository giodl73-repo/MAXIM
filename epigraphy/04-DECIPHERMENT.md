# Decipherment Methods: Bilingual Texts, Statistical Analysis, Linear B, Maya

## The Big Picture

```
DECIPHERMENT PROBLEM SPACE
============================

WHAT YOU HAVE:         WHAT YOU NEED TO KNOW:
  Signs on material      What language?
  Sign inventory         What script type? (logo/syllabic/alpha)
  Distribution data      What sounds do signs represent?
  Possible bilingual     What do the words mean?
  texts

DECIPHERMENT STRATEGIES:
+------------------------------------------------------------------+
|  STRATEGY              REQUIRES                EXAMPLE           |
|  ------------------    --------                -------           |
|  Bilingual text        Known language partner  Rosetta Stone     |
|  Named entity anchor   Proper names in both    Cartouches        |
|  Statistical analysis  Large corpus            Sign frequency    |
|  Known language        Related lang. known     Linear B (Greek)  |
|  Typological inference Sign count tells type   Alphabetic guess  |
+------------------------------------------------------------------+

SUCCESS RATE: ~10 known decipherments of major scripts
FAILURES: ~5 major scripts still undeciphered (see 07)
```

---

## Principle 1: Sign Count as Script-Type Hypothesis

The number of signs in a corpus constrains the script type:

```
SIGN COUNT DIAGNOSTIC
======================

< 30 signs  -> Almost certainly ABJAD or ALPHABET
              (Ugaritic: 30; Greek: 24; Phoenician: 22)
              -> Each sign = one consonant (or phoneme)

30-100 signs -> SYLLABARY
              (Linear B: ~87; Cypriot syllabic: ~55)
              -> Each sign = a syllable (CV or V)

> 200 signs -> LOGO-SYLLABIC or LOGOGRAPHIC
              (Akkadian cuneiform: ~300; Chinese: thousands)
              -> Mix of word-signs and syllabic signs

APPLICATION:
  When you find a new script, COUNT THE SIGNS FIRST.
  This tells you what kind of system you're looking for
  before you can read a single word.

CAVEAT:
  Some scripts have variable corpus counts:
    Indus Valley: 400-600 signs
    -> Could be logo-syllabic (sign count consistent with that)
    -> Or an alphabet with many allographs (sign variants)
    -> This ambiguity is one reason Indus remains undeciphered
```

---

## Principle 2: Bilingual and Trilingual Texts

The "holy grail" of decipherment: the same text in a known and an unknown script.

```
BILINGUAL TEXT REQUIREMENTS
=============================

Ideal conditions:
  1. Text A: unknown script
  2. Text B: same content, known script
  3. Long text (more data = more constraints)
  4. Fixed proper nouns (names don't change across languages)

ROSETTA STONE (Ptolemy V, 196 BCE):
  Hieroglyphic + Demotic + Greek
  Greek was known; provided content
  Proper names (Ptolemy, Berenice) = anchor points
  Greek phrase count vs. hieroglyphic sign group count
  -> Approximately equal -> each group = a word
  Key limitation: short; many gaps in hieroglyphic section

BEHISTUN INSCRIPTION (Darius I, ~520 BCE):
  Old Persian + Elamite + Akkadian (Babylonian)
  Old Persian partially guessable from Zoroastrian texts
  -> bootstrapped Akkadian

BILINGUAL STELA FROM MESHA (MOABITE STONE):
  Not a true bilingual but parallels to Hebrew OT
  -> Allowed verification of Phoenician script readings

LYCIAN / CARIAN / LYDIAN:
  Greek-bilingual gravestones in Anatolia
  -> Deciphered in 20th c. with Greek help
```

---

## Principle 3: Proper Names as Entry Points

Proper names provide anchors because they can be identified in the known-language partner and matched to the same sign sequence in the unknown script.

```
PROPER NAME METHOD
===================

Step 1: Identify named entities in the known text
  "Ptolemy," "Berenice," "Alexander" -- in Greek

Step 2: Find the same named entities in the unknown text
  They should appear at the same frequency
  They should appear in structurally parallel positions
  Royal names may be in cartouches (visual marker helps)

Step 3: Extract phonetic values from name spellings
  P-T-O-L-E-M-A-I-O-S: each sign = a sound value
  Cross-reference with CLEOPATRA if available:
  K-L-E-O-P-A-T-R-A
  Shared sign for P, T, O, A, L = validated phonetic values

Step 4: Plug values into other words
  Try to read words using the extracted values
  Check against known language vocabulary if language identified
  Check for self-consistent readings (no contradictions)

Step 5: Extend to common vocabulary
  Frequently occurring sequences = likely common words
  Try substituting phonetic values
  Look for patterns consistent with known language family

WORKED EXAMPLE: Champollion on Cleopatra + Ptolemy
  P: same in both names -> one sign = 'p'
  T: shared -> sign = 't'
  O: shared -> sign = 'o'
  L: shared -> sign = 'l'
  A: shared in different positions -> sign = 'a'
  New signs from Cleopatra: K, E, R, A (end)
  Total after two names: 9 consonant/vowel values
```

---

## Linear B: Ventris's Syllabic Grid Method

Linear B is the most important 20th-century decipherment — methodologically sophisticated and fully documented.

```
LINEAR B BACKGROUND
====================

Script: Linear B
Found: Crete (Knossos) by Arthur Evans (1900)
       Mainland Greece: Pylos, Mycenae, Tiryns
Period: ~1450-1200 BCE (Late Bronze Age)
Text type: administrative clay tablets (inventories, personnel)
Language: unknown at time of discovery

Evans's error (and delay):
  Evans controlled the Knossos tablets
  Refused to share facsimiles until his publication
  Delayed by World War I, then Evans's own procrastination
  Facsimiles published: 1952 (Evans died 1941)
  35 years of unnecessary delay in decipherment attempts
```

### The Syllabic Grid Method

Michael Ventris (1922-1956) — an architect, not a professional linguist — developed a systematic approach:

```
VENTRIS'S SYLLABIC GRID METHOD
================================

Assumption: Linear B is a syllabary (sign count ~87 confirmed this)
Framework: create a grid of signs organized by their
           phonological relationships

Step 1: COMMUTATION ANALYSIS
  Find signs that appear in the same positions in different words
  Signs that alternate in same position = share a vowel (same V)
  Signs that appear together frequently = may share a consonant

Step 2: BUILD THE GRID
  Rows = consonants (C1, C2, C3...)
  Columns = vowels (a, e, i, o, u)
  Each cell = a CV syllable sign
  Fill cells by commutation and distribution patterns

  First grid (incomplete):
    The grid could not be filled from statistics alone
    -> Required testing hypotheses about values

Step 3: PLACENAME HYPOTHESIS
  Knossos tablets likely mention Knossos and other Cretan places
  If Linear B records a language used in Crete, placenames
  should appear and should correspond to known place names
  -> Three signs appear frequently together as a proper noun
  -> Hypothesis: these three signs = ko-no-so (Knossos)

Step 4: LANGUAGE IDENTIFICATION
  Plugging values from placenames into other words:
  They started producing sequences that looked like Greek
  June 1952: Ventris identified Linear B as Greek
  (an archaic Greek dialect -- now called "Mycenaean Greek")

VALIDATION:
  Blegan's Pylos tablets (1953): one tablet listed vessels
  with words reading: ti-ri-po = tripod? (ti-ri-podes)
  tri-po-de = three-legged
  Homeric word: tripous = tripod
  "With this text, Ventris's decipherment is proven"
  (John Chadwick, who became Ventris's collaborator)
```

### Why Linear B Could Be Deciphered

```
FAVORABLE CONDITIONS FOR LINEAR B
===================================

1. Known language (Greek) was identified -> vocabulary available
2. Sign count (~87) -> confirmed syllabary
3. Large corpus: ~5,000 tablets total
4. Administrative content: numbers, lists, inventories
   -> predictable vocabulary (grain, wine, sheep, people)
5. Placenames in both Linear B and later Greek sources
   -> proper name anchors
6. Related script: Linear A (Minoan, undeciphered) and Cypriot syllabic
   (Greek, deciphered from bilingual Phoenician) share some signs
   -> structural clues
```

---

## Maya Decipherment: A Case Study in Resistance

Maya decipherment took ~140 years because Western scholars systematically resisted key insights:

```
MAYA DECIPHERMENT TIMELINE
============================

1566: Diego de Landa's "Relacion de las Cosas de Yucatan"
  Spanish bishop describes Maya writing
  Includes an "alphabet" -- actually a syllabary excerpt
  AND burns Maya books (only 4 survive: Dresden, Madrid, Paris, Grolier)
  De Landa's alphabet was misunderstood for 400 years
  (He wrote the sign for the sound "b" when asked for "b",
   not the word "b" -- key confusion about what the alphabet was)

1880s-1940s: Western scholarly consensus
  Maya glyphs are NOT phonetic
  They are "symbolic" or "ideographic"
  Primary use: calendar and astronomical notation
  The "calendar school" dominated -- Goodman, Morley, Thompson

1952: Yuri Knorozov (Soviet linguist)
  Published: Maya glyphs ARE phonetic (syllabic)
  Evidence: applied de Landa's "alphabet" correctly
            as a syllabary, not a letter alphabet
  Result: readings of some signs confirmed
  Western reaction: dismissed (Cold War politics)
  "A Soviet who has never been to Mesoamerica
   cannot possibly understand Maya writing"
  (Thompson's response -- essentially ad hominem)

1960s-1970s: Tatiana Proskouriakoff
  Maya inscriptions are HISTORICAL (not just astronomical)
  Identified birth/death/accession dates for specific rulers
  -> Proved that texts record historical narratives
  This did not directly advance phonetic decipherment
  but broke the "calendar only" consensus

1973: Palenque Round Table (preliminary signs)
  Collaboration among scholars; phonetic principle gaining ground

1986: Dumbarton Oaks and Copan Workshop
  David Stuart (17 years old) presents analysis
  Linda Schele, Peter Mathews, Floyd Lounsbury collaborate
  Phonetic substitution principle confirmed:
    Different sign combinations can write the same word
    (if they produce the same sounds -- syllabic equivalence)
  This is the crucial methodological breakthrough

1990s: Decipherment accelerates
  Glyph blocks: paired columns, read left-to-right within pair,
                then down to next pair level
  ~70-80% of the corpus now readable
  Remaining ~20-30%: rare signs, dialect variation, damaged texts
```

---

## The General Decipherment Algorithm

```
DECIPHERMENT ALGORITHM (summary)
==================================

INPUT: corpus of inscriptions in unknown script

PHASE 1: INVENTORY
  Count signs -> script type hypothesis
  Map sign distribution (which signs appear where)
  Identify formal features (cartouches, determinatives, word dividers)

PHASE 2: STRUCTURE
  Find repeating sequences (words?)
  Find short sequences in predictable positions (articles? prepositions?)
  Find long sequences that appear in lists (names?)

PHASE 3: LANGUAGE HYPOTHESIS
  What language family is plausible from geography/archaeology?
  Any known related languages?
  Sign count consistent with that language's phonology?

PHASE 4: ANCHOR
  Find bilingual text -> extract values from proper names
  OR
  Identify probable placenames -> test against known geography
  OR
  Use sign distribution to build phonological grid (Ventris method)

PHASE 5: TEST AND EXTEND
  Plug extracted values into other words
  Check for self-consistency
  Check against known vocabulary of hypothesized language
  Look for new confirmations (predictive success)

VALIDATION:
  New undeciphered text translated BEFORE examining
  -> If prediction holds, decipherment is confirmed
  Chadwick's Pylos tablet with "tripod" is the model
```

---

## Decision Cheat Sheet

| Case | Key breakthrough | Method |
|------|-----------------|--------|
| Egyptian hieroglyphic | Cartouche = royal name; Coptic helps phonology | Bilingual (Rosetta Stone) + proper names |
| Akkadian cuneiform | Behistun trilingual; Old Persian as bridge | Trilingual; Old Persian partially known |
| Linear B | Mycenaean Greek; placename ko-no-so | Syllabic grid + language identification |
| Ugaritic | Small sign count (30); Semitic language | Sign count -> abjad; Semitic cognates |
| Maya | Phonetic substitution confirmed; de Landa correctly read | Phonetic principle + historical context |
| Lycian/Carian | Greek-bilingual gravestones | Bilingual proper names |

---

## Common Confusion Points

**Decipherment ≠ translation.** Decipherment establishes the reading system. Translation requires knowing the language. Linear B was deciphered in 1952; Mycenaean Greek texts were translated in subsequent years. For Maya, decipherment and translation proceeded together because related Maya languages are still spoken.

**The proper name method requires a true bilingual.** Names only tell you phonetic values. To read the rest of the text, you need to know the language (vocabulary, grammar). Without knowing the language, you can read the sounds but not understand the meaning.

**Sign count is a hypothesis, not a proof.** A script with 400 signs might be logo-syllabic (consistent with the count) or might be an alphabet with 400 allographs (stylistic variants). Statistical analysis of sign distribution can help distinguish these hypotheses.

**Thompson's resistance to Knorozov delayed decipherment by at least a decade.** This is a case study in how academic authority can suppress correct findings. Knorozov was right; Thompson was wrong; and Cold War politics allowed Thompson to suppress rather than engage with the evidence.

**"Partially deciphered" is a spectrum.** Maya: ~75% readable. Linear A: ~20% readable (some signs borrowed from Linear B). Indus: 0% readable. The percentage matters for what historical conclusions are possible.
