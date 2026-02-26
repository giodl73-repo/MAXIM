# Egyptian Hieroglyphics: Script Architecture and Champollion's Decipherment

## The Big Picture

```
EGYPTIAN WRITING SYSTEM ARCHITECTURE
=======================================

HIEROGLYPHIC     HIERATIC          DEMOTIC           COPTIC
Formal, carved   Scribal cursive   Administrative    Greek alphabet +
Monumental use   Papyrus, ostraka  cursive           6 Demotic signs
3100 BCE - 4 CE  2600 BCE - 4 CE   650 BCE - 5 CE    1st c. CE - present

Same language at different stages; different scripts for different contexts

+------------------------------------------------------------------+
|  HIEROGLYPHIC SIGN TYPES                                         |
|                                                                  |
|  LOGOGRAMS           PHONETIC SIGNS         DETERMINATIVES       |
|  (word-signs)        (sound-signs)          (semantic classifiers)|
|  One sign = one word  One sign = sound(s)   No sound value       |
|                                             Categorize meaning   |
|  ~100 in common use   Unilateral: ~26       ~150 in common use   |
|  (the "alphabet"      Bilateral: ~80        Follow the word      |
|   letter + word)      Trilateral: ~50       Signal word category  |
+------------------------------------------------------------------+
```

---

## Hieroglyphic Sign Architecture

### The Three Sign Types in Detail

```
1. LOGOGRAMS (WORD-SIGNS / IDEOGRAMS)
=======================================

The simplest case: sign = word
  Picture of sun = "sun" / "day" (ra/hrw in Egyptian)
  Picture of man = "man" (s)
  Picture of house = "house" (pr)

Used for:
  Common nouns that can be depicted
  Often accompanied by a stroke (logogram marker)
    to indicate "read this as a word"

Limits:
  Cannot depict abstract concepts directly
  Cannot depict grammatical elements
  -> Phonetic signs needed for everything else

2. PHONETIC SIGNS
==================

UNILATERAL (alphabetic, one consonant):
  26 signs, one for each Egyptian consonant
  These ARE an alphabet embedded in hieroglyphics
  But Egyptians did not use them alone as an alphabet
  Instead: mixed with bilateral and trilateral signs

BILATERAL (two consonants):
  One sign = two consonant sounds
  e.g.: sign nfr = n+f+r (the consonants, not the vowels)
  About 80 in common use

TRILATERAL (three consonants):
  One sign = three consonant sounds
  e.g.: sign 'nh = 'aleph+n+h (ankh = life)
  About 50 in common use

CRITICAL POINT: Egyptian is an abjad (consonantal script)
  Vowels are NOT written in classical Egyptian
  Reader supplies vowels from context and linguistic knowledge
  "Egyptologists" conventionally insert e between consonants
  -> "nfr" pronounced conventionally as "nefer" (beautiful)
  -> Actual ancient vowels unknown

3. DETERMINATIVES (SEMANTIC CLASSIFIERS)
==========================================

Signs placed after a word that indicate its semantic category
NOT pronounced; purely classification aids

Examples:
  Seated man: follows personal name (male person)
  Seated woman: follows female personal name or -t nouns
  Walking legs: follows words meaning motion
  Sun: follows words for time, light, astronomical concepts
  Roll of papyrus: follows abstract nouns (invisible-thing)
  Crocodile: follows dangerous animal names
  House: follows words for buildings and rooms

Why determinatives exist:
  Egyptian has many homophones (same consonant pattern)
  Determinative disambiguates which word is intended
  Analogous to Chinese semantic radicals in combined characters
```

---

## Hieratic and Demotic

```
HIERATIC (2600 BCE - 4 CE)
===========================

Script: cursive simplification of hieroglyphic
Medium: primarily papyrus, ostraka (pottery sherds)
Direction: right to left (hieroglyphic = either direction)
Users: scribes, administrators, priests
Content: literary, religious, administrative, personal letters

Relationship to hieroglyphic:
  One-to-one sign correspondence (can be transliterated to hieroglyphic)
  Signs simplified for rapid writing
  Ligatures (signs joined) common
  Not a phonetic simplification -- same phonology, different letterforms

Think of hieratic as: cursive script
Think of hieroglyphic as: printed/formal script

DEMOTIC (650 BCE - 5 CE)
=========================

Script: further cursive simplification from hieratic
Used from: 26th Dynasty (Saite period) onward
Medium: papyrus, ostraka; also carved on stone in bilingual contexts
Direction: right to left
Users: secular administration, legal documents, private letters

Key feature: more ligatures; often unreadable without training
  Demotic = "popular" writing (demotics = people, Greek name)
  Despite the name, it was still a scribal/literate-class script

Historical significance:
  Administrative language of Ptolemaic Egypt (323-30 BCE)
  Legal contracts, tax records, petitions in Demotic
  The Rosetta Stone middle register is Demotic
  Demotic survived as administrative and religious script
  into the Roman period (5 CE latest known text)
```

---

## Coptic

```
COPTIC (1st century CE - present as liturgical)
=================================================

Script: Greek alphabet (25 letters) + 6 additional letters
        (from Demotic, for Egyptian sounds not in Greek)

The 6 Demotic additions:
  sh, f, kh, h, dj, ti (sounds without Greek equivalents)

Why Greek alphabet for Egyptian:
  Ptolemaic period: Greek education system widespread
  Christians (2nd-3rd c. CE) needed to write Coptic
  Greek alphabet was more accessible than hieroglyphic/Demotic
  CRITICAL: Coptic WRITES THE VOWELS (unlike hieroglyphic)
  -> First time Egyptian vowels are recorded in writing
  -> Coptic is invaluable for reconstructing ancient Egyptian phonology

Historical significance for Egyptology:
  Champollion knew Coptic (trained by Silvestre de Sacy's students)
  Coptic gave him access to Egyptian vowels
  Allowed reconstruction of how signs should sound
  Coptic = a "Rosetta Stone" for phonology

Current use: Coptic Orthodox Church liturgy
  Still used in Egypt for religious purposes
  Not a spoken community language; liturgical only
```

---

## The Rosetta Stone: Champollion's Decipherment

### The Object

```
ROSETTA STONE
==============

Physical: dark granodiorite stele, ~114 cm x 72 cm
Date: 196 BCE (Year 9 of Ptolemy V Epiphanes)
Content: Ptolemy V decree for priesthood tax exemptions
         and honors following suppression of rebellion

Three registers:
  TOP: Hieroglyphic (official language, divine authority)
       14 lines (stele was broken; originally more)
  MIDDLE: Demotic (administrative language of Egypt)
          32 lines
  BOTTOM: Greek (language of the Ptolemaic administration)
          54 lines

Discovery: French soldiers near Rosetta (Rashid), 1799
           during Napoleon's Egyptian campaign
           Recognized significance immediately
Capture: British took it in 1801 (Treaty of Alexandria)
Current location: British Museum, London (since 1802)
```

### The Decipherment Process

```
CHAMPOLLION'S BREAKTHROUGH (1822)
===================================

Prior work:
  Thomas Young (English, 1819):
    Identified that cartouche ovals = royal names
    Deciphered Ptolemy's name in cartouche (Greek known)
    Suggested some hieroglyphic signs = phonetic
    But: still believed most signs were symbolic/ideographic
    Did not crack the system

Jean-Francois Champollion (French, 1790-1832):
  Advantages over Young:
    Knew Coptic fluently (Egyptians' own language descendants)
    Had access to more inscriptions (not just the Rosetta Stone)

KEY INSIGHT #1: Cartouches = royal names
  The oval outline around certain sign groups
  = indicates a proper name (royal name)
  Bilingual: Greek "Ptolemy" identified in cartouche
  Same sign group = "Ptolemaios" in transliteration

KEY INSIGHT #2: Proper names are phonetic
  Cleopatra on the Philae obelisk (bilingual, Young found)
  P-T-O-L-E-M-A-I-O-S shares signs with:
  K-L-E-O-P-A-T-R-A
  Shared signs P, T, O, L, A = same sounds in both names
  Cross-referencing: builds up an alphabet

KEY INSIGHT #3: Not all signs are phonetic
  Some signs are determinatives (unpronounced)
  Some signs are logograms
  The system is MIXED -- this is why Young failed
  He could not accept that a "sophisticated" writing system
  would mix phonetic and non-phonetic signs

September 14, 1822: Champollion's letter to Dacier
  "I've got it!" moment
  Demonstrated reading of non-Greek royal names
  (Ramesses, Thutmose) -- proved the system extended
  beyond Ptolemaic period names
```

---

## Reading Hieroglyphs: Practical Mechanics

```
READING DIRECTION
==================

Hieroglyphs can be written:
  Right to left (most common)
  Left to right
  Top to bottom (in columns)

Rule: the signs FACE the direction of reading
  Human and animal faces point toward the start
  So: if the bird faces right -> read left to right
      if the bird faces left  -> read right to left

No spaces between words in hieroglyphic
Determinatives help identify word boundaries
Vowels not written (must be supplied)

PHONETIC COMPLEMENTATION:
  A common feature: logogram followed by phonetic signs
  repeating some of its consonants
  e.g.: pr (house) + r (phonetic "r") -> prr = "go out"
  The phonetic complement confirms which sounds to read
  and guides the reader to the correct pronunciation

CARTOUCHE (shenu):
  Oval or oblong enclosure
  Contains royal names (living and dead pharaohs)
  Also divine names in some contexts
  The cartouche + serekh (palace facade box) = royal identity markers
  Key entry points for decipherment: known from Greek
```

---

## Hieroglyphic Writing in Material Context

```
INSCRIPTION CONTEXTS
=====================

MONUMENTAL (formal register):
  Temple walls: religious texts, royal victories, divine scenes
  Tomb walls: offering formulas, biographical inscriptions,
              funerary spells (Book of the Dead)
  Obelisks: royal dedications to solar deities
  Stelae: votive, funerary, commemorative

FUNERARY FORMULAS:
  Hotep-di-nesw: "An offering which the king gives"
  Standard formula: "May the king give [Osiris/deity]
                     an offering of bread and beer,
                     oxen and fowl, alabaster and linen,
                     for the ka of [the deceased]"
  Abbreviated: htp-di-nsw + deity name + deceased name
  This formula appears on thousands of monuments
  -> Recognition of formulaic text aids reading

ADMINISTRATIVE (hieratic/demotic):
  Papyri in libraries and archives (Egypt's dry climate = survival)
  Ostraka: informal records, school exercises, letters
  Wax tablets: perishable, mostly lost
```

---

## Decision Cheat Sheet

| Script | Period | Medium | Register |
|--------|--------|--------|---------|
| Hieroglyphic | 3100 BCE - 4 CE | Stone, wood, metal | Formal, monumental |
| Hieratic | 2600 BCE - 4 CE | Papyrus, ostraka | Administrative, literary |
| Demotic | 650 BCE - 5 CE | Papyrus, occasional stone | Administrative, legal |
| Coptic | 1st c. CE - present | Papyrus, vellum | Christian religious |

| Sign type | Pronunciation | Function |
|-----------|--------------|---------|
| Logogram | The word it depicts | Writes a whole word |
| Unilateral | Single consonant | "Alphabetic" element |
| Bilateral | Two consonants | Syllabic shorthand |
| Trilateral | Three consonants | Root-sign |
| Determinative | Silent | Semantic category marker |

---

## Common Confusion Points

**Hieroglyphs are not primarily pictures of objects.** Most hieroglyphic text is phonetic (syllabic signs). The pictorial quality is real but secondary to the phonetic system. Champollion had to overcome the assumption that they were symbolic ideograms.

**Egyptian did not write vowels.** The system is an abjad — consonants only. Modern transliterations that show vowels (e.g., "nefertiti") are conventional approximations. Coptic gives us some vowel information, but ancient Egyptian pronunciation is only partially reconstructable.

**The Rosetta Stone did not crack the code alone.** Champollion used many additional inscriptions, especially the Philae obelisk. The Rosetta Stone was a starting point; the decipherment used a corpus.

**Thomas Young was partly right.** He correctly identified the phonetic principle for proper names and correctly read "Ptolemaios" in the cartouche. His failure was in assuming the phonetic principle was limited to foreign names. Champollion's insight was that it applied throughout.

**Coptic is still used.** As the liturgical language of the Coptic Orthodox Church (Egypt, diaspora), Coptic is actively maintained. It is not spoken as a native language, but it is read and chanted. Its survival made Egyptian phonology partially recoverable.
