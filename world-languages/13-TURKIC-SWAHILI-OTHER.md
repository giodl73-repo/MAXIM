# Turkish, Persian, Swahili, Polish, Tamil — Language Profiles

## Overview

```
DIVERSE LANGUAGE PROFILES
===========================
Five languages from five different families — each illustrating
a distinct structural principle:

  +------------------+----------+-------+-------+--------+---------+
  | Language         | Family   | Order | Tones | Gender | Type    |
  +------------------+----------+-------+-------+--------+---------+
  | Turkish          | Turkic   | SOV   | No    | None   | Agg     |
  | Persian/Farsi    | Iranian  | SOV   | No    | None   | Fus-ish |
  | Swahili          | Bantu    | SVO   | No    | Noun   | Agg     |
  |                  |          |       |       | classes|         |
  | Polish           | Slavic   | Free  | No    | M/F/N  | Fus     |
  | Tamil            | Dravidian| SOV   | No    | M/F/N  | Agg     |
  +------------------+----------+-------+-------+--------+---------+
```

---

## Turkish

### Profile

```
+--------------------------------------------------------------------+
| TURKISH (Türkçe)                                                   |
+--------------------------------------------------------------------+
| Family:      Turkic → Oghuz → Western Oghuz                       |
| Native spkrs: ~79M                                                 |
| Countries:   Turkey (official), Cyprus (co-official)               |
|              Significant diaspora: Germany (~3M), Netherlands, etc.|
| Word order:  SOV — strict verb-final                              |
| Morphology:  Agglutinative — highly regular and productive         |
| Tonal:       No                                                    |
| Gender:      NONE (no grammatical gender)                          |
| Script:      Latin (reformed 1928 under Atatürk from Arabic script)|
| Cases:       6: Nominative, Accusative, Dative, Locative,          |
|              Ablative, Genitive                                    |
| FSI level:   Category III — ~1100 hours                            |
+--------------------------------------------------------------------+
```

### Vowel Harmony

```
VOWEL HARMONY — Turkish's defining feature
===========================================
Suffix vowels must AGREE with the last vowel of the root.
Every root belongs to a back-vowel or front-vowel class.

BACK VOWELS: a, ı, o, u
FRONT VOWELS: e, i, ö, ü

Rules:
  After back vowel: suffixes use a, ı, o/u
  After front vowel: suffixes use e, i, ö/ü

EXAMPLE with 2-way harmony (a/e):
  ev (house) + -de (locative at) = evde (at the house) [front → e]
  okul (school) + -da (locative at) = okulda (at the school) [back → a]

EXAMPLE with 4-way harmony (ı/i/u/ü):
  Definite accusative: -ı / -i / -u / -ü
  ev-i (the house-ACC) [front e → i]
  okul-u (the school-ACC) [back u → u]
  gün-ü (the day-ACC) [front ü → ü]
  araba-yı (the car-ACC) [back a → ı, +y- buffer]

  ALL suffix vowels harmonize — not just one.
  Harmony makes suffixes phonologically predictable once learned.
```

### Agglutination in Turkish — The Pipeline Model

Turkish agglutination is a suffix-chaining pipeline: each suffix is a deterministic transform applied to the current stem, producing a new stem for the next transform. The order is fixed (slot grammar), the composition is left-to-right, and each suffix has a clear semantic/grammatical contribution. This is structurally identical to method chaining or a builder pattern:

```
BUILDER PATTERN ANALOGY:

  word = stem
    .add(plural)         // -ler/-lar (vowel harmony)
    .add(possessive)     // -im/-ım/-um/-üm (1sg), -in/-ın/... (2sg)
    .add(case)           // -de/-da (LOC), -e/-a (DAT), -den/-dan (ABL)
    .toString()          // surface form

  evlerimde = ev + ler + im + de
              house + PL + 1sg.POSS + LOC = "in my houses"

VERB PIPELINE:
  word = verb_stem
    .add(causative?)     // -tir/-dir (make X do)
    .add(passive?)       // -il/-in (be done)
    .add(reflexive?)     // -in (do to oneself)
    .add(reciprocal?)    // -iş (do to each other)
    .add(negative?)      // -me/-ma (not)
    .add(ability?)       // -ebil/-abil (can)
    .add(tense/mood)     // -iyor (present), -di (past), -ecek (future)...
    .add(person/number)  // -im (1sg), -sin (2sg), etc.

  sevdirilememek = sev + dir + il + eme + mek
  = love + CAUS + PASS + NEG-ABILITY + INF
  = "to be unable to be made to love"
  (not common, but grammatically well-formed and parseable)
```

```
TURKISH AGGLUTINATION — stacking suffixes
==========================================
Word = stem + [aspect] + [negative] + [tense] + [person]

ev (house):
  evler (houses) — ev + -ler (plural)
  evlerde (in houses) — ev + -ler + -de (plural + locative)
  evlerimde (in my houses) — ev + -ler + -im + -de (plural + 1sg poss + loc)
  evlerimden (from my houses) — + -den (ablative "from")

VERB NEGATION with -me/-ma:
  git-me-di-m = go + NEG + PAST + 1sg = "I didn't go"
  gid-ecek-miş-im = go + FUT + EVID + 1sg = "apparently I will go"

FAMOUSLY LONG WORD:
  Çekoslovakyalılaştıramadıklarımızdanmışsınızcasına
  = "as if you were one of those we couldn't make Czechoslovakian"
  This is grammatically legitimate (though comically constructed for demonstration).

TURKISH CASES:
+----------+--------+-----------+----------------------------------+
| Case     | Suffix | Example   | Meaning                          |
+----------+--------+-----------+----------------------------------+
| NOM      | —      | ev        | house (subject)                  |
| ACC      | -(y)ı  | evi       | house (direct object, definite)  |
| DAT      | -(y)e  | eve       | to/toward house                  |
| LOC      | -de    | evde      | at/in house                      |
| ABL      | -den   | evden     | from house                       |
| GEN      | -(n)in | evin      | of/house's                       |
+----------+--------+-----------+----------------------------------+

(vowels vary by harmony: -de/-da, -den/-dan, -(y)e/-(y)a, etc.)
```

### Turkish Survival Phrases

```
SURVIVAL TURKISH
=================
Merhaba / Selam (informal) — Hello
İyi günler / İyi akşamlar — Good day / Good evening
Güle güle (to one leaving) / Hoşça kal (said by one leaving) — Goodbye
Lütfen — Please
Teşekkür ederim / Teşekkürler — Thank you (formal/informal)
Rica ederim / Bir şey değil — You're welcome
Evet / Hayır — Yes / No
Özür dilerim / Pardon — I'm sorry / Excuse me
Nasılsınız? — How are you? (formal)
İyiyim, teşekkürler. — I'm fine, thank you.
Adınız ne? — What is your name?
Benim adım ___ — My name is ___
Bu ne kadar? — How much is this?
___ nerede? — Where is ___?
Sağ / Sol / Düz — Right / Left / Straight
İngilizce biliyor musunuz? — Do you speak English?
Anlamıyorum — I don't understand
İmdat! — Help!
Polis çağırın! — Call the police!
Tuvalet nerede? — Where is the toilet?
Havalimanı / Otel / Hastane — Airport / Hotel / Hospital
```

---

## Persian / Farsi

### Profile

```
+--------------------------------------------------------------------+
| PERSIAN / FARSI (فارسی Fārsī)                                      |
+--------------------------------------------------------------------+
| Family:      Indo-European → Indo-Iranian → Iranian → Western     |
| Native spkrs: ~57M (Iran) + ~8M (Afghanistan as Dari)             |
|              + ~9M (Tajikistan as Tajik)                           |
| Total spkrs:  ~110M                                                |
| Countries:   Iran (official as Farsi), Afghanistan (as Dari),      |
|              Tajikistan (as Tajik — Cyrillic script)               |
| Word order:  SOV                                                   |
| Morphology:  Fusional (lighter than Arabic, heavier than Turkish) |
| Tonal:       No                                                    |
| Gender:      NONE (exceptional for an IE language)                 |
| Script:      Perso-Arabic (Arabic script adapted, right-to-left)   |
|              4 additional letters for Persian sounds: پ چ ژ گ      |
| FSI level:   Category III — ~1100 hours                            |
+--------------------------------------------------------------------+
```

### Persian Grammar Highlights

```
PERSIAN STRUCTURE
==================
VERB FINAL: subject-object-verb order
  من کتاب می‌خوانم. (Man ketāb mi-khānam.) — I book read. = I read a book.

EZĀFE — noun chaining with -e/-ye:
  The "connective particle" links modifier to modified (order: head-modifier):
  کتاب من (ketāb-e man) = book of me = my book
  خانه بزرگ (khāne-ye bozorg) = house big = big house
  کتاب قرمز من (ketāb-e qermez-e man) = book-of red-of me = my red book
  Ezāfe chains modifiers rightward (opposite English left-modification).

NO GRAMMATICAL GENDER:
  Exceptional for an Indo-European language.
  او (u) = he/she/it (one pronoun for all).
  No agreement between adjective and noun.
  "خانه بزرگ" = big house (m/f/n irrelevant — same form).

VERB SYSTEM:
  Present: stem + personal endings (می mi- + present stem + ending)
  Past: simple past stem + endings
  Tense markers: می (mi-) for imperfective aspect
  Negative: نه (na-) prefix

PERSIAN NUMBERS:
  ۰ ۱ ۲ ۳ ۴ ۵ ۶ ۷ ۸ ۹ (East Arabic numerals used in Iran/Afghanistan)
  یک (yek=1) دو (do=2) سه (se=3) چهار (chahār=4) پنج (panj=5)
  شش (shesh=6) هفت (haft=7) هشت (hasht=8) نه (noh=9) ده (dah=10)
```

### Persian Survival Phrases

```
SURVIVAL PERSIAN
=================
سلام (Salām) — Hello
خداحافظ (Khodāhāfez) — Goodbye (God-guardian = God be your keeper)
ممنون / متشکرم (Mamnun / Motashakeram) — Thank you
خواهش می‌کنم (Khāhesh mikonam) — You're welcome / Please
بله / نه (Bale / Na) — Yes / No
ببخشید (Bebakhshid) — Excuse me / Sorry
حال شما چطور است؟ (Hāl-e shomā chetour ast?) — How are you?
اسم شما چیست؟ (Esm-e shomā chist?) — What is your name?
این چقدر است؟ (In cheghadr ast?) — How much is this?
___ کجاست? (___ kojāst?) — Where is ___?
کمک! (Komak!) — Help!
دستشویی کجاست؟ (Dastshui kojāst?) — Where is the toilet?
فرودگاه / هتل / بیمارستان — Airport / Hotel / Hospital
```

---

## Swahili

### Profile

```
+--------------------------------------------------------------------+
| SWAHILI (Kiswahili)                                                |
+--------------------------------------------------------------------+
| Family:      Niger-Congo → Atlantic-Congo → Bantu → Sabaki        |
| Native spkrs: ~16M                                                 |
| Total spkrs:  ~80-150M (lingua franca of East Africa)             |
| Countries:   Official: Tanzania, Kenya, Uganda, DRC, Rwanda        |
|              Widely used: Burundi, Comoros, Mozambique, Somalia    |
|              African Union: one of its official languages          |
| Word order:  SVO                                                   |
| Morphology:  Agglutinative — extensive prefix system               |
| Tonal:       No (exceptional for Bantu family — most are tonal)   |
| Gender:      NO biological gender — NOUN CLASSES (~15 classes)     |
| Script:      Latin (Arabic Ajami historically; rarely used now)    |
| FSI level:   Category II — ~900 hours                              |
+--------------------------------------------------------------------+
```

### Noun Class System

**The generic type parameter model:** Swahili's noun classes are a runtime type tag system. Every noun carries a class membership (encoded in its prefix). That class membership propagates through the entire sentence via agreement — every verb, adjective, and possessive that relates to that noun must carry a matching class prefix. This is structurally identical to a generic type parameter flowing through a call chain:

```
GENERIC TYPE ANALOGY:

  // Swahili noun class system:
  class KitabuWord<Class7_8> {  // kitabu = book, class 7 (ki-/vi-)
    prefix = "ki-";             // singular: ki-
    pluralPrefix = "vi-";       // plural: vi-
  }

  // Agreement = type parameter propagation:
  kitabu    ki-zuri    ki-ngu    ki-li-anguka
  book.CL7  CL7-good   CL7-mine  CL7-PAST-fall
  "My good book fell."

  // Change the noun → change ALL class markers in the sentence:
  vitabu    vi-zuri    vi-ngu    vi-li-anguka
  books.CL8 CL8-good   CL8-mine  CL8-PAST-fall
  "My good books fell."

  // The type parameter (class) flows through every constituent.
  // One change at the noun → cascade update through the entire predicate.

PRACTICAL CONSEQUENCE:
  Agreement errors (using wrong class prefix on verb/adjective) are
  ALWAYS wrong, not just "awkward" — they are like type errors.
  Native speakers correct them immediately and categorically.
```

```
BANTU NOUN CLASS SYSTEM — the signature of Swahili grammar
===========================================================
~15 classes (paired singular/plural), each with a prefix.
Every noun belongs to a class. Adjectives, verbs, and subject/object
agreement ALL must match the noun's class prefix.

Like gender agreement in European languages, but with ~15 classes
based roughly on semantic categories (not arbitrary).

KEY CLASSES:
+-------+------+------+---------------------------+-----------------------+
| Class | Sing | Plur | Typical nouns             | Agreement prefix      |
+-------+------+------+---------------------------+-----------------------+
| 1/2   | m-   | wa-  | People, animate agents:   | a- / wa-             |
|       |      |      | mtu (person), mtoto (child)|                     |
| 3/4   | m-   | mi-  | Trees, plants, body parts:| u- / i-              |
|       |      |      | mti (tree), mji (town)    |                     |
| 5/6   | Ø/ji-| ma-  | Fruits, large objects:    | li- / ya-            |
|       |      |      | tunda (fruit), jicho (eye)|                     |
| 7/8   | ki-  | vi-  | Objects, languages, tools:| ki- / vi-            |
|       |      |      | kitabu (book), kisu (knife)|                    |
| 9/10  | N-   | N-   | Animals, loanwords:       | i- / zi-             |
|       |      |      | ndege (bird), gari (car)  |                     |
| 11    | u-   | —    | Abstracts, elongated obj: | u-                   |
|       |      |      | uso (face), ukuta (wall)  |                     |
| 15    | ku-  | —    | Verbal nouns (infinitives):| ku-                 |
|       |      |      | kusoma (reading)          |                     |
+-------+------+------+---------------------------+-----------------------+

AGREEMENT IN ACTION:
  "The good books are expensive."
  Vitabu vizuri ni vya bei ghali.
  vi-tabu  vi-zuri  ni  vi-a  bei  ghali
  CL7.plur book  CL7.ADJ good  COP CL7.POSS price  expensive

  Every underlined element agrees with class 7/8 (ki-/vi-) of "kitabu".

VERB SUBJECT/OBJECT AGREEMENT:
  Mtoto anasoma. — The child reads. (m- class → a- verb agreement)
  Watoto wanasoma. — The children read. (wa- class → wa- verb agreement)
  Kisu kinakata. — The knife cuts. (ki- class → ki- verb agreement)
```

### Swahili Verb System

```
SWAHILI VERB STRUCTURE
========================
Verbs are highly synthetic:
  SUBJECT MARKER + TENSE MARKER + OBJECT MARKER + ROOT + FINAL VOWEL

  ni-na-soma  = I-PRES-read = I read
  u-na-soma   = you-PRES-read = you read
  a-na-soma   = s/he-PRES-read = s/he reads
  tu-na-soma  = we-PRES-read = we read
  m-na-soma   = you.pl-PRES-read = you read
  wa-na-soma  = they-PRES-read = they read

TENSE MARKERS:
  -na- (present)   -li- (past)   -ta- (future)   -me- (perfect)
  wa-li-soma = they read (past)
  tu-ta-soma = we will read
  ni-me-soma = I have read

OBJECT INCORPORATION:
  ni-na-m-soma = I-PRES-him-read = I read him/her (object prefix)
  ni-li-ki-nunua = I-PAST-it(ki-class)-buy = I bought it

NEGATION:
  ha-ni-soma = NEG-I-read = I don't read
  Past negative: si-ku-soma = NEG-PAST-read = I didn't read
```

### Swahili Survival Phrases

```
SURVIVAL SWAHILI
=================
Habari / Hujambo — Hello / How are you (formal)
Sijambo / Nzuri — I'm fine / Good (response to Hujambo)
Kwaheri — Goodbye
Tafadhali — Please
Asante / Asante sana — Thank you / Thank you very much
Karibu / Sawa — You're welcome / OK/Sure
Ndiyo / Hapana — Yes / No
Samahani — Sorry/Excuse me
Bei gani? / Ngapi? — How much?
___ iko wapi? — Where is ___?
Sielewi — I don't understand
Je, unazungumza Kiingereza? — Do you speak English?
Msaada! / Saidia! — Help!
Choo kiko wapi? — Where is the toilet?
Uwanja wa ndege / Hoteli / Hospitali — Airport / Hotel / Hospital
```

---

## Polish

### Profile

```
+--------------------------------------------------------------------+
| POLISH (Język polski)                                              |
+--------------------------------------------------------------------+
| Family:      Indo-European → Slavic → West Slavic → Lechitic      |
| Native spkrs: ~45M                                                 |
| Countries:   Poland (official); significant diaspora worldwide     |
| Word order:  Free (SVO most neutral; pragmatically driven)        |
| Morphology:  Fusional — highly inflected                          |
| Tonal:       No                                                    |
| Gender:      Three: M/F/N (+ animate/inanimate M subgender)       |
| Script:      Latin + 9 additional characters: ą ć ę ł ń ó ś ź ż  |
| Cases:       7: NOM/ACC/DAT/GEN/INS/LOC/VOC                       |
| FSI level:   Category III-IV — ~1100 hours                        |
+--------------------------------------------------------------------+
```

### Polish Sound System

```
POLISH PHONOLOGY — CONSONANT CLUSTERS
=======================================
Polish has the most complex consonant cluster phonology in the Indo-European family.
Clusters arise from historical vowel deletion — "fleeting vowels" disappeared,
leaving adjacent consonants in contact.

SIBILANT SERIES (4-way distinction — most languages have 2):
  sz  [ʃ]  like English "sh" — hard palatal
  ś   [ɕ]  soft palatal sibilant (between sh and s, tongue forward)
  cz  [tʃ] like English "ch"
  ć   [tɕ]  soft affricate (between ch and c)
  ż/rz[ʒ]  like English "s" in "measure"
  ź   [ʑ]  soft version
  dż  [dʒ] like English "j" in "jump"
  dź  [dʑ] soft version

  The ś/ć/ź/dź series = palatalized versions (tongue raised toward palate).
  Minimal pairs: szal (scarf) vs ściana (wall) vs szczaw (sorrel).

CLUSTER EXAMPLES:
  trzy (three)     [tʃɨ]      — moderately hard
  źródło (source)  [ʑruːdwɔ]  — harder
  chrząszcz (beetle)[xʂɔw̃ʂtʂ] — 6+ consonants, one syllable
  dżdżownica (earthworm) — starts with two affricates [dʒdʒ]

NASAL VOWELS:
  ą [ɔ̃]  — nasal o (at end of word, often denasalized to [ɔw])
  ę [ɛ̃]  — nasal e (at end of word, often just [ɛ])
  Nasal quality less stable than in French — varies by position and speaker.
```

### Polish Verb Conjugation

```
VERB CONJUGATION (present tense)
=================================
THREE CONJUGATION CLASSES (like Spanish/Russian):

CLASS 1 — -ować / -iwać / -ywać → -uję:
  pracować (to work): pracuję / pracujesz / pracuje / pracujemy / pracujecie / pracują

CLASS 2 — stems ending in palatalized consonant → -ę/-isz:
  pisać (to write): piszę / piszesz / pisze / piszemy / piszecie / piszą

CLASS 3 — e-class verbs → -ę/-esz:
  mieć (to have): mam / masz / ma / mamy / macie / mają  [irregular]
  wiedzieć (to know): wiem / wiesz / wie / wiemy / wiecie / wiedzą [irregular]

PAST TENSE — agrees with subject in gender AND number:
  pisać (to write) past:
  +-----------+----------+----------+----------+
  | Person    | MASC     | FEM      | NEUT/PL  |
  +-----------+----------+----------+----------+
  | 1sg       | pisałem  | pisałam  |          |
  | 2sg       | pisałeś  | pisałaś  |          |
  | 3sg       | pisał    | pisała   | pisało   |
  | 1pl       | pisaliśmy| pisałyśmy|          |
  | 2pl       | pisaliście|pisałyście|         |
  | 3pl       | pisali   | pisały   |          |
  +-----------+----------+----------+----------+
  MASC PLURAL (pisali) vs FEM/NEUT PLURAL (pisały):
  "virile" (masculine personal) plural vs non-virile plural.
  A group of all-male or mixed-gender: pisali.
  A group of all-female, or objects: pisały.

ASPECT: Same system as Russian — every verb has IMP/PERF pair:
  pisać (IMP) → napisać (PERF): to write / to write and finish
  czytać (IMP) → przeczytać (PERF): to read / to finish reading
```

### Polish vs Russian — Slavic Comparison

```
+-----------------------------+-------------------+-------------------+
| Feature                     | Russian           | Polish            |
+-----------------------------+-------------------+-------------------+
| Cases                       | 6 (NOM/ACC/GEN/   | 7 (adds VOCATIVE) |
|                             | DAT/INS/PREP)     |                   |
| Script                      | Cyrillic          | Latin             |
| Nasal vowels                | None              | ą ę               |
| Vowel reduction             | Heavy: unstressed | Minimal: all      |
|                             | о→[ɐ], е→[ɪ]     | vowels clear      |
| Aspect system               | IMP/PERF pairs    | IMP/PERF pairs    |
|                             | (same)            | (same)            |
| Word order                  | Free (SVO neutral)| Free (SVO neutral)|
| Past tense gender           | Yes               | Yes (+virile plur)|
| Verbal noun use             | Common            | Less common       |
| Mutual intelligibility      | Low (script diff  | ~30-40% spoken;   |
| with the other              | + phonology)      | more in writing   |
+-----------------------------+-------------------+-------------------+

COGNATE COMPARISON:
  Russian: вода (voda) / Polish: woda — water (same)
  Russian: хорошо (khorosho) / Polish: dobrze — well/good (different word)
  Russian: пожалуйста / Polish: proszę — please (different word)
  Russian: здравствуйте / Polish: dzień dobry — hello (different)
```

### Polish Key Features

```
POLISH GRAMMAR HIGHLIGHTS
===========================
7 CASES (vs Russian's 6):
  NOM / ACC / DAT / GEN / INS / LOC / VOC (vocative — for direct address)
  "Panie Kowalski!" (Mr. Kowalski! — vocative)

4-WAY MASCULINE SUBGENDER:
  Masculine animate (personal): masculine nouns for men/male animals
  Masculine animate (non-personal): male animals
  Masculine inanimate: objects
  Each takes different accusative form.

CONSONANT CLUSTERS — the hardest part phonologically:
  Polish has some of the most complex consonant clusters in any language:
  "Szczebrzeszyn" (town name) — pronunciation guide needed
  chrząszcz (beetle) = [ˈxʂɔw̃ʂtʂ]  — 8 consonants, 1 syllable
  Brzęczyszczykiewicz (fictional name) = 7+ consonant cluster
  These are extreme examples, but Polish casual speech has clusters
  that are genuinely hard: trzy (three), źródło (source), dżdżownica (earthworm)

ASPECT SYSTEM: same as Russian — every verb has IMP/PERF pair.
  pisać (IMP, to write) vs napisać (PERF, to write and finish)

POLISH ALPHABET SPECIAL CHARACTERS:
  ą [ɔ̃] — nasal o (like French on)
  ę [ɛ̃] — nasal e (at end of word often just [ɛ])
  ó [u]  — rounded u (same sound as u in modern Polish)
  ł [w]  — like English w
  ś ź ć ń — soft sibilants/nasals (palatalized s/z/c/n)
  ż [ʒ]  — like 's' in measure
  sz [ʃ] — like 'sh' (two letters, one sound)
  cz [tʃ] — like 'ch' in check
  dz [dz], dź [dʑ], dż [dʒ] — affricate series

Polish survival phrases:
  Dzień dobry — Good day
  Cześć (informal) — Hello/Bye
  Do widzenia — Goodbye
  Proszę — Please / You're welcome / Here you are
  Dziękuję — Thank you
  Tak / Nie — Yes / No
  Przepraszam — Sorry/Excuse me
  Ile to kosztuje? — How much does it cost?
  Gdzie jest ___? — Where is ___?
  Nie rozumiem — I don't understand
```

---

## Tamil

### Profile

```
+--------------------------------------------------------------------+
| TAMIL (தமிழ் Tamiḻ)                                                 |
+--------------------------------------------------------------------+
| Family:      Dravidian → South Dravidian → Tamil-Kannada           |
| Native spkrs: ~78M                                                 |
| Countries:   India (Tamil Nadu official), Sri Lanka (official),    |
|              Singapore (one of 4 official), Malaysia, diaspora     |
| Word order:  SOV — strict                                          |
| Morphology:  Agglutinative                                         |
| Tonal:       No (unlike many Dravidian languages)                  |
| Gender:      Three: Rational (M+F) / Irrational (things/animals)  |
| Script:      Tamil script — unique, abugida                        |
| FSI level:   Category III-IV — ~1100 hours                         |
+--------------------------------------------------------------------+
```

### Tamil Sound System

```
TAMIL PHONOLOGY — MAJOR FEATURES
==================================
Tamil has a unique sound system among major world languages.

RETROFLEX CONSONANTS — 3 stops + nasal + lateral:
  ட [ʈ]  retroflex t — tongue curled back to palate ridge
  ட [ɖ]  retroflex d
  ண [ɳ]  retroflex n
  ள [ɭ]  retroflex l (distinct from dental l: ல [l])
  ழ [ɻ]  retroflex approximant — particularly distinctive Tamil sound
         Found almost nowhere else; approximates "rl" combined.

DENTAL vs RETROFLEX distinction is phonemic:
  தல taḷa (head region) vs தள taḷa (level surface) — minimal pair
  Lost on most non-native speakers.

VOWELS — 12, each with long/short distinction = 18 total vowel distinctions:
  அ ஆ (a/ā), இ ஈ (i/ī), உ ஊ (u/ū), எ ஏ (e/ē), ஐ (ai)
  ஒ ஓ (o/ō), ஔ (au)
  Vowel length is phonemically contrastive: வேல் vēl (spear) ≠ வெல் vel (win)

DIGLOSSIA — formal vs colloquial gap:
  Written/formal Tamil and spoken Tamil are SIGNIFICANTLY different.
  Written (செந்தமிழ்/centamiḻ): complex morphology, archaic vocabulary.
  Spoken (கொடுந்தமிழ்): simplified, fast-changing, regional dialects.
  TV/media Tamil: intermediate style.
  Impact on learning: textbook Tamil may be useless for daily conversation.
```

### Tamil Script

```
TAMIL SCRIPT — 247 CHARACTERS
===============================
Type: Abugida (consonant with inherent vowel 'a'; diacritics modify vowel)
Direction: Left to right

BASE CHARACTERS:
  12 independent vowels: அ ஆ இ ஈ உ ஊ எ ஏ ஐ ஒ ஓ ஔ
  18 consonants, each with inherent /a/: க் ங் ச் ஞ் ட் ண் த் ந் ப் ம் ய் ர் ல் வ் ழ் ள் ற் ன்
  Consonant without vowel: puḷḷi marker (dot above): க் = /k/ with no vowel
  Consonant + vowel = combined form:
    க + ா = கா (ka+ā = kā)   க + ி = கி (ka+i = ki)   க + ு = கு (ka+u = ku)
  Full grid: 18 consonants × 12 vowels = 216 vowel-consonant combos + 18 pure consonants + 12 vowels + ஃ = 247

UNIQUE FEATURES:
  The "ழ" (ḻ) character represents a sound unique to Tamil and Malayalam —
  a retroflex approximant not found in other major world scripts.
  Tamil numerals have their own system: ௧ ௨ ௩ ௪ ௫ ௬ ௭ ௮ ௯ ௦ (1-9, 0)
  Traditional fraction symbols also exist: ½=½, ¼=¼ — still used in temple
  inscriptions and formal/religious contexts.
```

### Tamil Verb Conjugation

```
TAMIL VERB SYSTEM
==================
TENSE: 3 synthetic tenses (past/present/future) + person/number/gender agreement.

STEM + TENSE MARKER + PERSON MARKER:

  செல் (cel, to go) — a strong verb:
  +-----------+----------+----------+----------+
  | Person    | PAST     | PRESENT  | FUTURE   |
  +-----------+----------+----------+----------+
  | 1sg (M/F) | சென்றேன் | செல்கிறேன்| செல்வேன் |
  | 2sg (M/F) | சென்றாய் | செல்கிறாய்| செல்வாய் |
  | 3sg M     | சென்றான் | செல்கிறான்| செல்வான் |
  | 3sg F     | சென்றாள் | செல்கிறாள்| செல்வாள் |
  | 3sg N     | சென்றது | செல்கிறது | செல்வது  |
  | 1pl incl  | சென்றோம் | செல்கிறோம்| செல்வோம் |
  | 2pl       | சென்றீர்கள்| செல்கிறீர்கள்| செல்வீர்கள்|
  | 3pl Rat   | சென்றார்கள்| செல்கிறார்கள்| செல்வார்கள்|
  | 3pl Irrat | சென்றன  | செல்கின்றன| செல்வன  |
  +-----------+----------+----------+----------+

RATIONAL/IRRATIONAL agreement:
  3rd person distinguishes RATIONAL (humans + deities) from IRRATIONAL (animals, things).
  Verb forms and pronouns differ by this distinction.
  This is the Tamil equivalent of animacy in Slavic languages — but more grammatically pervasive.

NEGATION — a separate paradigm (not just a particle):
  Negative verbs conjugate completely separately:
  செல்கிறேன் (I go) → செல்லவில்லை (I do not go) — not just "not + go"
```

### Tamil Key Features

```
TAMIL GRAMMAR HIGHLIGHTS
=========================
DIGLOSSIC LANGUAGE:
  Written/formal Tamil (செந்தமிழ் centamiḻ) and spoken Tamil differ
  significantly — verb forms, vocabulary, and grammar diverge.
  Similar to Arabic MSA vs spoken dialect, but within one country.

DRAVIDIAN SOV — not related to Indo-European at all:
  Tamil word order: Subject + Object + Verb (like Japanese/Korean)
  But no genetic connection to those languages.

THREE-WAY GENDER (Rational/Irrational):
  Masculine: Tamil men + male deities (he)
  Feminine:  Tamil women + female deities (she)
  Neuter:    animals, things, children — "it" (irrational gender)
  Most European languages have animate/inanimate; Tamil: rational/irrational.

NOUN CASE SYSTEM (8 cases):
  Nominative, Accusative, Dative, Sociative/Comitative,
  Instrumental, Ablative, Genitive, Locative

VERB PERSON AGREEMENT:
  Verbs agree with subject in person/number/gender
  3 persons × plural/singular × gender = complex agreement table

TAMIL SCRIPT:
  247 characters (12 vowels + 18 consonants + 216 vowel-consonant combos + ஃ)
  Derived from Brahmi, highly distinctive curvilinear forms
  Sample: தமிழ் = t+a + m+i + ḻ = Tamil (reading left-right)
  Vowel diacritics attach to consonants in various positions.

Tamil survival phrases:
  வணக்கம் (Vaṇakkam) — Hello/Greetings
  நன்றி (Naṉḏṟi) — Thank you
  ஆம் / இல்லை (Ām / Illai) — Yes / No
  மன்னிக்கவும் (Maṉṉikkavum) — Sorry/Excuse me
  இது எவ்வளவு? (Itu evvaḷavu?) — How much is this?
  ___ எங்கே இருக்கிறது? — Where is ___?
  உதவி! (Utavi!) — Help!
```

---

## Decision Cheat Sheet

| Language | Best reason to learn | Unique feature | Time (FSI) |
|----------|---------------------|----------------|-----------|
| Turkish | Turkey travel/business, Turkic gateway | Vowel harmony + agglutination | ~1100 hrs |
| Persian | Iran/Afghanistan, beautiful literature | No gender, ezāfe construction | ~1100 hrs |
| Swahili | East Africa travel/business, easiest Bantu | Noun class agreement system | ~900 hrs |
| Polish | Poland business, European gateway | 7 cases + consonant clusters | ~1100 hrs |
| Tamil | Tamil Nadu/Sri Lanka, ancient literature | Rational/irrational gender | ~1100 hrs |

---

## Common Confusion Points

**"Turkish grammar is so regular?"**
Yes — remarkably so. The vowel harmony and suffix system are consistent
and rule-governed. Once you learn the ~7 suffix paradigms, you can
generate grammatically correct forms reliably. The challenge is vocabulary
(Turkic root, not Indo-European) and SOV word order with verb-final clauses.

**"Persian and Arabic are related?"**
No — unrelated families. Persian is Indo-European (like English, German, French).
Arabic is Afro-Asiatic (like Hebrew, Amharic). Persian borrowed the Arabic script
after the Islamic conquest and has ~40% Arabic loanwords, but the grammar
is completely different (no root system, no trilateral roots, no gender agreement).

**"Swahili is an easy African language?"**
The noun class system is genuinely complex and requires internalizing ~15 agreement
paradigms. The verb prefix system is agglutinative and systematic. What's "easy":
no tones, Latin script, regular morphology, large English/Arabic/Portuguese loan
vocabulary. Conversational level is achievable in 6-9 months.

**"Polish R is the same as Russian R?"**
Polish "r" (trilled [r]) vs "rz" ([ʒ] = voiced retroflex fricative).
"Rz" sounds like the "s" in "measure". Polish also has "ż" with the same
sound [ʒ]. Historical rz was a trilled r + zh; now merged with ż.
Polish phonology has more consonant contrasts than Russian.
