# Arabic — Language Reference

## Profile at a Glance

```
+--------------------------------------------------------------------+
| ARABIC (العربية al-ʿArabiyya)                                      |
+--------------------------------------------------------------------+
| Family:      Afro-Asiatic → Semitic → Central Semitic             |
| Native spkrs: ~274M (L1)                                           |
| Total spkrs:  ~422M (L1+L2)                                        |
| Countries:   22 countries (Arab League) + widespread diaspora      |
| Word order:  VSO (Classical/MSA) → SVO (most dialects)            |
| Morphology:  Fusional, root-based (trilateral root system)         |
| Tonal:       No                                                    |
| Gender:      Binary (M/F)                                          |
| Script:      Arabic abjad (right-to-left, 28 letters)             |
| Cases:       3: Nominative, Accusative, Genitive (MSA only)        |
| FSI level:   Category IV — ~2200 hours (hardest for English)       |
+--------------------------------------------------------------------+

CRUCIAL DIGLOSSIA ISSUE:
  Modern Standard Arabic (MSA/Fusha): written language, news, formal speech.
  No native speakers of MSA. No one grows up speaking it.
  Colloquial dialects: what people actually speak.
  Gap = roughly like Latin vs Italian — same script, very different spoken form.
  Dialects are MUTUALLY UNINTELLIGIBLE across regions.
  Which to learn: MSA for reading/writing; pick a dialect for speaking.
```

---

## The Big Picture

```
ARABIC LANDSCAPE
=================

  WRITTEN FORM               SPOKEN FORMS (dialects)
  +-----------+              +----------+------------+----------+----------+
  |    MSA    |              | Egyptian | Levantine  | Gulf     | Maghrebi |
  |Modern Std |              | ~100M    | Syria/Leb  | Saudi/   | Morocco/ |
  |Arabic     |              | speakers | /Jordan    | UAE/Iraq | Algeria/ |
  |           |              | Most     | /Palestine | Oil      | Tunisia  |
  |Formal,    |              | widely   |            | states   |          |
  |Literary,  |              | understood            |          |          |
  |Quran-     |              | in media              |          |          |
  |adjacent   |              +----------+------------+----------+----------+
  +-----------+

  QURANIC ARABIC: Classical Arabic (7th century). Different from MSA.
  MSA is derived from Quranic Arabic but simplified/modernized.
  Reading the Quran ≠ reading a newspaper ≠ speaking with locals.

  RECOMMENDATION:
    - Learn MSA for: literacy, travel across all Arab countries, news
    - Add Egyptian Arabic for: widest spoken understanding (media/film)
    - Add Gulf Arabic for: business in GCC countries
```

---

## The Arabic Script (Abjad)

```
ARABIC WRITING SYSTEM
======================
  Type: Abjad — consonants only. Vowels are optional diacritical marks.
  Direction: RIGHT-TO-LEFT
  Letters: 28
  Each letter has 4 forms: ISOLATED, INITIAL (word-start), MEDIAL, FINAL

  Example with ب (ba):
    Isolated: ب
    Initial:  بـ  (connects to letter on right only)
    Medial:   ـبـ (connects on both sides)
    Final:    ـب  (connects to letter on left only)

  Not all letters connect: ا د ذ ر ز و — connect on right only.
  When these appear, the next letter must start a new "chain".

THE 28 LETTERS:
+------+--------+--------+-------+------+
| Form | Name   | Sound  | Initial|Final|
+------+--------+--------+-------+------+
| ا    | alif   | [a/ā]  |  ا   | ـا  |
| ب    | ba     | [b]    |  بـ  | ـب  |
| ت    | ta     | [t]    |  تـ  | ـت  |
| ث    | tha    | [θ]    |  ثـ  | ـث  |
| ج    | jim    | [dʒ]   |  جـ  | ـج  |
| ح    | ha     | [ħ]    |  حـ  | ـح  | (pharyngeal H — no English equiv)
| خ    | kha    | [x]    |  خـ  | ـخ  | (like "loch")
| د    | dal    | [d]    |  د   | ـد  |
| ذ    | dhal   | [ð]    |  ذ   | ـذ  | (like "the")
| ر    | ra     | [r]    |  ر   | ـر  |
| ز    | zay    | [z]    |  ز   | ـز  |
| س    | sin    | [s]    |  سـ  | ـس  |
| ش    | shin   | [ʃ]    |  شـ  | ـش  |
| ص    | sad    | [sˤ]   |  صـ  | ـص  | (emphatic S)
| ض    | dad    | [dˤ]   |  ضـ  | ـض  | (emphatic D)
| ط    | ta     | [tˤ]   |  طـ  | ـط  | (emphatic T)
| ظ    | dha    | [ðˤ]   |  ظـ  | ـظ  | (emphatic DH)
| ع    | ain    | [ʕ]    |  عـ  | ـع  | (pharyngeal — no English equiv)
| غ    | ghain  | [ɣ]    |  غـ  | ـغ  | (like French R / gargling)
| ف    | fa     | [f]    |  فـ  | ـف  |
| ق    | qaf    | [q]    |  قـ  | ـق  | (uvular stop, back of throat)
| ك    | kaf    | [k]    |  كـ  | ـك  |
| ل    | lam    | [l]    |  لـ  | ـل  |
| م    | mim    | [m]    |  مـ  | ـم  |
| ن    | nun    | [n]    |  نـ  | ـن  |
| ه    | ha     | [h]    |  هـ  | ـه  |
| و    | waw    | [w/ū]  |  و   | ـو  | (also long vowel ū)
| ي    | ya     | [j/ī]  |  يـ  | ـي  | (also long vowel ī)
+------+--------+--------+-------+------+

VOWELS — optional diacritics (harakat):
  َ  (fatha)  = short a, written above consonant
  ِ  (kasra)  = short i, written below consonant
  ُ  (damma)  = short u, written above consonant
  ً  (tanwin) = final -an (indefinite accusative)
  ْ  (sukun)  = no vowel follows this consonant
  ّ  (shadda) = consonant doubled

Only used in: Quran, children's books, language teaching materials.
Adult Arabic text has NO vowel markings. You must know the word.
```

---

## The Trilateral Root System

**The database projection model:** The Arabic trilateral root system is a morphological database. The 3-consonant root is a primary key. Vowel patterns (wazn, pl. awzān) are view definitions — each pattern projects the root through a transform to produce a derived form. Learning a root gives you free access to all its projections; learning a pattern gives you free decoding of any root applied through that pattern.

```
ROOT = 3-LETTER PRIMARY KEY
k-t-b (domain: writing, recording)

PATTERN (wazn) = VIEW DEFINITION:
  CaCaCa    → fʕala pattern → kataba (he wrote) [verb, past active]
  yaCCuCu   → yafʕulu pattern → yaktūbu (he writes) [verb, present]
  CiCāC     → fiʕāl pattern → kitāb (book) [noun, instrument/artifact]
  CiCāCa    → fiʕāla pattern → kitāba (writing) [noun, verbal noun/gerund]
  CāCiC     → fāʕil pattern → kātib (writer) [active participle, "one who does"]
  maCCūC    → mafʕūl pattern → maktūb (written) [passive participle]
  maCCaC    → mafʕal pattern → maktab (office/desk) [noun of place]
  maCCaCa   → mafʕala pattern → maktaba (library) [noun of place + collective]

QUERY ANALOGY:
  SELECT verb_past FROM k_t_b_table USING pattern_CaCaCa → kataba
  SELECT place_noun FROM k_t_b_table USING pattern_maCCaC → maktab
  SELECT agent_noun FROM k_t_b_table USING pattern_CāCiC → kātib

THE SYSTEMATIC PAYOFF:
  Roots × Patterns → Arabic lexicon.
  ~6,000 roots × ~30 productive patterns = exponentially large vocabulary
  Once you know the pattern, you can DECODE any unknown word:
    maCCaC = "place of" → madrasa (school, from d-r-s = study)
                        → masjid (mosque, from s-j-d = prostrate)
                        → matbakh (kitchen, from t-b-kh = cook)
    fāʕil = "one who" → dāris (student), kātib (writer), qāriʾ (reader)
```

**Why this matters for learning:** Arabic vocabulary acquisition is not rote memorization of word-pairs. It is pattern recognition over a root-pattern decomposition. Native Arabic speakers use this system productively — encountering an unknown word, they decompose it into root + pattern and infer the meaning from the semantic domain of the root and the grammatical category of the pattern. Learners who internalize ~10 high-frequency roots × ~10 productive patterns have immediate access to ~100 decodable words and a framework for the rest.

```
ARABIC ROOT SYSTEM — the defining feature of Semitic morphology
================================================================
Every Arabic word derives from a root of (usually) 3 consonants.
The root carries the core semantic domain.
Different vowel patterns applied to the same consonants → different words.

ROOT k-t-b (writing, books):
  كَتَبَ  kataba    — he wrote (verb, past)
  يَكْتُبُ yaktuba  — he writes (verb, present)
  كِتَاب  kitāb     — book (noun)
  كِتَابَة kitāba   — writing (verbal noun/gerund)
  كَاتِب  kātib     — writer (active participle / person who writes)
  مَكْتُوب maktūb   — written / letter (passive participle)
  مَكْتَب  maktab   — office / desk (place noun = place of writing)
  مَكْتَبَة maktaba — library / bookstore (place + collective)
  كَتَّاب  kattāb   — intensive writer / scribe
  كِتَابِي kitābī   — my book (1st person possessive)

ROOT d-r-s (studying, lessons):
  دَرَسَ darasa     — he studied
  دَرْس  dars       — lesson
  دَارِس dāris      — student
  مَدْرَسَة madrasa — school

ROOT q-r-a (reading):
  قَرَأَ qaraʾa     — he read
  قِرَاءَة qirāʾa  — reading
  قَارِئ qāriʾ      — reader

This system means: learning a root gives you a cluster of words.
Pattern recognition replaces rote memorization.
Arabic morphology is highly systematic once you internalize the patterns.
```

---

## Grammar Core

### Nouns and Agreement

```
GENDER:
  Masculine: default, no marker
  Feminine:  usually ends in ة (ta marbuta = "tied t") — pronounced [a] in pausa
    مُعَلِّم muʿallim (male teacher) vs مُعَلِّمَة muʿallima (female teacher)
    Some feminines irregular: أُم umm (mother), أَرْض arḍ (earth), شَمْس shams (sun)

NUMBER — THREE numbers:
  Singular: كِتَاب  kitāb (book)
  Dual:     كِتَابَان kitābān (two books) — suffix -ān/-ayn
  Plural:   كُتُب  kutub (books) — BROKEN PLURAL (internal vowel change)
            Regular plural also exists: مُعَلِّمُون muʿallimūn (m), مُعَلِّمَات (f)

BROKEN PLURALS — unpredictable, must be memorized:
  بَيْت bayt (house) → بُيُوت buyūt
  كَلْب kalb (dog)   → كِلَاب kilāb
  رَجُل rajul (man)  → رِجَال rijāl
  عَيْن ʿayn (eye)  → عُيُون ʿuyūn

THREE CASES (MSA):
  Nominative: subject — -u ending (usually unmarked in unvoweled text)
  Accusative: object — -a ending
  Genitive:   after prepositions, in idafa — -i ending

IDAFA — the possessive/noun-noun construct
  "the book of the student" = كِتَابُ الطَّالِبِ kitābu l-ṭālibi
  First noun: no article, case depends on sentence role
  Second noun: always genitive
  "the student's book" = same structure: book-of-the-student
```

### Verb System

```
VERB PATTERNS (binyanim in Semitic terminology)
================================================
Arabic has 10 major verb forms (measures), each with predictable meaning shift:
  Form I:   فَعَلَ faʿala — basic action
  Form II:  فَعَّلَ faʿʿala — intensify/causative (double middle consonant)
  Form III: فَاعَلَ fāʿala — reciprocal/attempt
  Form IV:  أَفْعَلَ ʾafʿala — causative (ʾa- prefix)
  Form V:   تَفَعَّلَ tafaʿʿala — reflexive of Form II
  Form VI:  تَفَاعَلَ tafāʿala — reflexive of Form III
  Form VII: اِنْفَعَلَ ʾinfaʿala — passive/reflexive
  Form VIII:اِفْتَعَلَ ʾiftaʿala — reflexive/middle
  Form IX:  اِفْعَلَّ ʾifʿalla — colors/physical defects
  Form X:   اِسْتَفْعَلَ ʾistafʿala — to consider/request

Example with root k-t-b:
  Form I:  كَتَبَ kataba — to write
  Form II: كَتَّبَ kattaba — to make write / teach writing
  Form III:كَاتَبَ kātaba — to correspond with
  Form X: اِسْتَكْتَبَ istaktaba — to ask someone to write

PAST TENSE conjugation (kataba, he wrote):
  كَتَبَ  kataba (he)       كَتَبَتْ katabat (she)
  كَتَبْتَ katabta (you m.) كَتَبْتِ katabti (you f.)
  كَتَبْتُ katabtu (I)
  كَتَبُوا katabū (they m.) كَتَبْنَ katabna (they f.)
  كَتَبْنَا katabnā (we)
```

---

## Numbers in Arabic

```
ARABIC NUMBERS
===============
Interestingly, the WRITTEN numerals (١٢٣٤٥٦٧٨٩٠) are read left-to-right
even though text goes right-to-left. Western numerals (1 2 3...) are
derived from these "Hindu-Arabic" numerals.

١ wahid (1)   ٢ ithnan (2)   ٣ thalatha (3)   ٤ arbaʿa (4)
٥ khamsa (5)  ٦ sitta (6)    ٧ sabʿa (7)      ٨ thamaniya (8)
٩ tisʿa (9)   ١٠ ʿashara (10)

Arabic number agreement is REVERSED for 3-10:
  3 masculine things → uses feminine number (3: ثَلَاثَة thalātha with ta marbuta)
  3 feminine things → uses masculine number (3: ثَلَاث thalāth without ta marbuta)
  Called "gender polarity" — this is counterintuitive and a known difficulty.
```

---

## 50 Essential Phrases (MSA + widely understood)

```
SURVIVAL ARABIC
================
مرحبا / أهلاً (marhaba / ahlan) — Hello
السلام عليكم (as-salāmu ʿalaykum) — Peace be upon you (universal Islamic greeting)
وعليكم السلام (wa-ʿalaykum as-salām) — Response
صباح الخير / مساء الخير (ṣabāḥ al-khayr / masāʾ al-khayr) — Good morning/evening
مع السلامة (maʿa s-salāma) — Goodbye (go in safety)
من فضلك / لو سمحت (min faḍlak / law samaḥt) — Please
شكراً / شكراً جزيلاً (shukran / shukran jazīlan) — Thank you / Thank you very much
عفواً (ʿafwan) — You're welcome / Excuse me
نعم / لا (naʿam / lā) — Yes / No
آسف / أنا آسف (āsif / anā āsif) — Sorry / I'm sorry
كيف حالك؟ (kayfa ḥālak?) — How are you?
بخير، شكراً (bi-khayr, shukran) — Fine, thank you
ما اسمك؟ (mā ismak?) — What is your name?
اسمي ___ (ismī ___) — My name is ___
من أين أنت؟ (min ayna anta?) — Where are you from?
أنا من ___ (anā min ___) — I am from ___
كم الثمن؟ (kam al-thaman?) / بكم هذا؟ (bi-kam hādhā?) — How much does this cost?
أين ___؟ (ayna ___?) — Where is ___?
لا أفهم (lā ʾafham) — I don't understand
هل تتكلم الإنجليزية؟ (hal tatakallam al-ʾinjilīziyya?) — Do you speak English?
النجدة! (an-najda!) — Help!
اتصل بالشرطة! (ittaṣil bi-sh-shurṭa!) — Call the police!
أين دورة المياه؟ (ayna dawrat al-miyāh?) — Where is the toilet?
المستشفى / المطار / الفندق — Hospital / Airport / Hotel
```

---

## Decision Cheat Sheet

| Situation | Arabic approach |
|-----------|----------------|
| Start reading | Learn the alphabet first (~1 month) — it IS learnable |
| Which variant | MSA for literacy; Egyptian for spoken comprehension |
| Root system | Learn 50 key roots → hundreds of words fall out automatically |
| Pharyngeal sounds | ح (ħ) and ع (ʿ) — practice daily, they don't exist in English |
| Numbers | Memorize 1-10 + gender polarity rule early |
| Diglossia | Expect to feel you learned "wrong Arabic" when you travel — normal |
| Dialects | Egyptian is most understood; Gulf Arabic for UAE/Saudi business |

---

## Common Confusion Points

**"No vowels in text?"**
Correct for normal adult text. Vowels are written only in the Quran,
children's books, and language learning materials. You read consonants +
context + word knowledge to fill in vowels. This is why reading is slow
at first — you're pattern-matching entire word shapes.

**"VSO order?"**
Classical/MSA Arabic is VSO: "Akala r-rajulu t-tuffāḥata" (Ate the-man the-apple).
Modern spoken dialects have largely shifted to SVO. MSA writing can use both.

**"Dual forms everywhere?"**
Arabic has a dual number for exactly two of something.
اِثْنَانِ ithnanī (two books) is different from كُتُب kutub (books plural).
Dual has special verb, pronoun, and noun forms. Dialects simplify this.

**"Sun letters and moon letters"**
The definite article is always written الـ (al-), but the l assimilates
to the first consonant if it's a "sun letter" (coronal consonants: t,d,s,z,n,r,l...):
  الشَّمْس ash-shams (the sun) — sh is a sun letter, l → sh
  القَمَر al-qamar (the moon) — q is a moon letter, l stays l
  14 sun letters, 14 moon letters — just memorize the sun letters.

**"ʿAyn (ع) is a consonant?"**
Yes. It's a voiced pharyngeal fricative — a voiced constriction in the pharynx.
Pronouncing it wrong vs not at all: ʿAyn is the difference between
عَلَم ʿalam (flag) and أَلَم ʾalam (pain). It's phonemic.
