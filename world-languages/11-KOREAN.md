# Korean — Language Reference (Deep Dive)

## Profile at a Glance

```
+--------------------------------------------------------------------+
| KOREAN (한국어 Hangugeo / 조선어 Joseoneo)                         |
+--------------------------------------------------------------------+
| Family:      Koreanic (language isolate family — no proven cognate)|
| Native spkrs: ~77M                                                 |
| Total spkrs:  ~80M                                                 |
| Countries:   South Korea (한국), North Korea (조선)                 |
|              Significant diaspora: China, USA, Japan               |
| Word order:  SOV — strict verb-final                               |
| Morphology:  Agglutinative — extremely productive suffix system    |
| Tonal:       No (Seoul dialect — no tonal distinction)             |
| Gender:      None (no grammatical gender)                          |
| Script:      Hangul (한글) — one of the world's great script       |
|              designs, created 1443 CE                              |
| Cases:       None — postpositional particles                       |
| FSI level:   Category IV — ~2200 hours                             |
+--------------------------------------------------------------------+
```

---

## Hangul: The Designed Script

```
HANGUL — ENGINEERED LANGUAGE TECHNOLOGY
=========================================
Invented 1443 CE by King Sejong the Great and scholars of the Hall of Worthies.
Prior to Hangul: Korean written with Classical Chinese (hanja).
Design principles:
  1. One symbol per phoneme
  2. Consonant shapes reflect articulation anatomy
  3. Vowels built from horizontal/vertical lines + dots
  4. Symbols arranged into syllable BLOCKS, not linear strings

BLOCK STRUCTURE:
  Each syllable = one block, composed of consonant + vowel (+ optional final consonant)

  Basic patterns:
  ┌──┐    ┌──┐    ┌────┐
  │C │    │C │    │ C  │
  │V │    ├──┤    │ V  │
  └──┘    │V │    ├────┤
          └──┘    │ C  │
  CV     CVV     CVC
  Example: 한 = ㅎ+ㅏ+ㄴ (h+a+n) — one block, one syllable
           국 = ㄱ+ㅜ+ㄱ (g+u+k)
           어 = ㅇ+ㅓ (silent initial + eo vowel) — ㅇ is placeholder
```

### Consonants

```
HANGUL CONSONANTS — 14 basic
================================
The shape encodes the articulation:
  ㄱ — side view of tongue at velum → [g/k]
  ㄴ — tongue tip at alveolar ridge → [n]
  ㄷ — same + stroke → [d/t]
  ㄹ — complex tongue movement → [r/l] (flap intervocalic, l word-final)
  ㅁ — outline of lips → [m]
  ㅂ — both lips → [b/p]
  ㅅ — teeth → [s]
  ㅇ — zero/null initial; [ŋ] as final → placeholder / ng
  ㅈ — [j/ch]
  ㅊ — [ch] (aspirated ㅈ)
  ㅋ — [k] (aspirated ㄱ)
  ㅌ — [t] (aspirated ㄷ)
  ㅍ — [p] (aspirated ㅂ)
  ㅎ — [h]

THREE-WAY STOP CONTRAST (unique to Korean):
  ㄱ [g~k]   ㅋ [kʰ]   ㄲ [k͈] — plain, aspirated, tense
  ㄷ [d~t]   ㅌ [tʰ]   ㄸ [t͈] — plain, aspirated, tense
  ㅂ [b~p]   ㅍ [pʰ]   ㅃ [p͈] — plain, aspirated, tense
  ㅅ [s]                ㅆ [s͈] — plain, tense
  ㅈ [dʒ~tʃ] ㅊ [tʃʰ]  ㅉ [t͈ɕ] — plain, aspirated, tense

  "Tense" consonants (ㄲ ㄸ ㅃ ㅆ ㅉ): glottalized/fortis — no direct English equiv.
  Plain at start of syllable → tends toward voiced.
  Plain after nasal → always voiced.
  No English speaker hears these distinctions naturally — must train.
```

### Vowels

```
HANGUL VOWELS — 10 basic
===========================
Designed from heaven/earth/man (·, ─, │):

Basic:
  ㅏ [a]    ㅓ [eo/ʌ]   ㅗ [o]    ㅜ [u]    ㅡ [eu/ɯ]
  ㅣ [i]    ㅐ [ae]     ㅔ [e]    ㅚ [oe]   ㅢ [ui]

Compound (y+vowel):
  ㅑ [ya]   ㅕ [yeo]    ㅛ [yo]   ㅠ [yu]
  ㅒ [yae]  ㅖ [ye]

Compound (w+vowel):
  ㅘ [wa]   ㅙ [wae]    ㅝ [wo/weo]  ㅞ [we]   ㅟ [wi]

CRITICAL VOWELS TO MASTER:
  ㅓ [eo] — rounded, mid-back vowel, like "uh" in British "uh-oh"
  ㅡ [eu] — high back unrounded — like "ugh" without the ugh
  ㅔ vs ㅐ — [e] vs [ae] — increasingly merged in Seoul dialect
  ㅢ [ui] — diphthong; as particle = [e]; after consonant = [i]
```

### Phonological Rules (Batchim Patterns)

```
FINAL CONSONANT (받침 batchim) RULES
======================================
Korean has complex phonological rules at syllable boundaries.

NASALIZATION: stop before nasal → nasal
  국물 (gukmul) → [궁물] gungmul (broth)
  입니다 (imnida) → [임니다] imnida
  닫는 (datneun) → [단는] danneun

LIAISON: final consonant links to next initial ㅇ (null):
  먹어 (meogeo) → [머거] meogeo (eat + informal ending)
  닭이 (dalgi) → [달기] dalgi (chicken + subject particle)

ASPIRATION: ㅎ + plain stop → aspirated stop (or reverse):
  좋다 (joh-da) → [조타] jota (good)
  많다 (manh-da) → [만타] manta (many)

TENSIFICATION: after certain environments, following stop becomes tense:
  학교 (hagyo) → [학꾜] hakkyo (school) — ㄱ before ㄱ → tense

These rules mean PRONUNCIATION ≠ SPELLING in Korean.
You must learn the rules or Korean sounds will be incomprehensible.
```

---

## Grammar Core

### Particles (Postpositions)

```
KOREAN PARTICLES — follow nouns, mark grammatical role
======================================================
+--------+--------+---------------------------------------------+
| Ptcl   | Roman  | Function                                    |
+--------+--------+---------------------------------------------+
| 이/가  | i/ga   | Subject particle (이 after consonant,       |
|        |        | 가 after vowel)                             |
| 은/는  | eun/neun| Topic particle (은 after consonant,        |
|        |        | 는 after vowel)                             |
| 을/를  | eul/reul| Object particle (을 after consonant,       |
|        |        | 를 after vowel)                             |
| 의     | ui/e   | Possessive (A-의-B = A's B)                 |
| 에     | e      | Location (static), time, direction (to)     |
| 에서   | eseo   | Location (action), from (origin)            |
| 으로/로| euro/ro| Direction (toward), instrument, means       |
| 와/과  | wa/gwa | And (formal), with (after vowel/consonant)  |
| 하고   | hago   | And (colloquial), with                      |
| 도     | do     | Also, even                                  |
| 만     | man    | Only                                        |
| 부터   | buteo  | From (starting point, time)                 |
| 까지   | kkaji  | Until, up to                                |
+--------+--------+---------------------------------------------+

TOPIC vs SUBJECT (은/는 vs 이/가):
  Similar to Japanese は vs が — same distinction, harder to articulate:
  은/는 = topic (what sentence is about, contrast, background)
  이/가 = subject (neutral subject, new information, exhaustive identification)
  나는 사과가 좋아요. — I (TOPIC) apples (SUBJECT) like. = I like apples.
  [Topic는 + subject가 + verb is common pattern for preferences/abilities]
```

### Speech Levels — The Permission Tier Model

Korean speech levels are a graduated permission system encoded in verb endings. The verb termination IS the auth token — it declares the speaker's assertion of the social relationship between speaker and listener. Choosing the wrong tier is not a stylistic error; it is a social protocol violation that the listener immediately detects.

```
SPEECH LEVEL TIERS (API version analogy):

+----------+----------+------------+--------------------------------------+
| Level    | Name     | Formality  | Use case (when to invoke this tier)  |
+----------+----------+------------+--------------------------------------+
| 합쇼체   | Haesyo   | Formal     | NEWS broadcasts, military briefings, |
|          |          | polite     | formal speeches, official documents. |
|          |          | (최고등급) | Marks you as respecting the audience |
|          |          |            | AS AN INSTITUTION, not just a person.|
+----------+----------+------------+--------------------------------------+
| 해요체   | Haeyo    | Informal   | DEFAULT TIER. Use with:              |
|          |          | polite     | Strangers, service workers, casual   |
|          |          | (기본등급) | adults you don't know well.          |
|          |          |            | Safe to use until a closer tier is   |
|          |          |            | explicitly established.              |
+----------+----------+------------+--------------------------------------+
| 하게체   | Haege    | Semi-      | Older speaker to younger adult.      |
|          |          | formal     | Professor to grad student (some).    |
|          |          |            | Increasingly rare in modern usage.   |
+----------+----------+------------+--------------------------------------+
| 해라체   | Haera    | Plain /    | Written Korean: newspapers, grammar  |
|          |          | literary   | books, instruction manuals.          |
|          |          |            | NOT used in spoken address except    |
|          |          |            | imperatives, or with children.       |
+----------+----------+------------+--------------------------------------+
| 해체     | Hae      | Intimate   | Close friends (established),         |
| (반말)   | (banmal) | (친근체)   | family, clearly younger speakers.    |
|          |          |            | Using banmal to a stranger/senior =  |
|          |          |            | "I'm treating you as my inferior."   |
+----------+----------+------------+--------------------------------------+
| 하오체   | Hao      | Archaic    | Historical dramas, classical texts.  |
| / 하소서 |          |            | Not used in modern speech.           |
+----------+----------+------------+--------------------------------------+

VERB SUFFIX = AUTH TOKEN (먹다, meokda = to eat):
  먹습니다 (meokseumnida)   — formal polite (합쇼체)
  먹어요   (meogeoyo)       — informal polite DEFAULT (해요체)
  먹어     (meogeo)         — intimate (해체/banmal)
  먹었어요 (meogeoosseoyo)  — informal polite PAST
  먹었어   (meogeoosseo)    — intimate PAST

TIER TRANSITION PROTOCOL:
  A senior person can invite a junior to use banmal: "반말 해도 돼"
  This is an explicit downgrade offer — similar to a "du" offer in German.
  The junior person does NOT unilaterally switch tiers.
  Switching to banmal without invitation = access violation.
```

```
KOREAN SPEECH LEVELS (경어법 gyeongeobbeop)
============================================
Korean has 7 speech levels encoded in verb endings.
Using the wrong level is a significant social error.

LEVELS (formal → informal):
+----------+-----------+----------------------------------+
| Level    | Name      | Usage                            |
+----------+-----------+----------------------------------+
| 합쇼체   | Haesyo    | Formal polite — news, speeches,  |
|          | (높임)    | business presentations           |
| 해요체   | Haeyo     | Informal polite — daily service, |
|          |           | strangers, non-close adults      |
|          |           | THIS IS THE DEFAULT LEVEL        |
| 하게체   | Haege     | Semiformal to younger adults     |
|          |           | (older speaker to younger adult) |
| 해라체   | Haera     | Plain — writing, newspapers,     |
|          |           | grammar books, imperatives       |
| 하오체   | Hao       | Archaic — seen in dramas/history |
| 해체     | Hae       | Intimate — close friends, family |
|          | (반말)    | Juniors, children, lovers        |
+----------+-----------+----------------------------------+

PRACTICAL:
  해요체 (haeyo) = safe default for all strangers and acquaintances
  반말 (banmal, informal 해체) = only with close friends or people younger
  Using banmal with a stranger/older person = rude

VERB ENDING DIFFERENCES (먹다 meokda = to eat):
  먹습니다 (meokseumnida) — formal polite
  먹어요 (meogeoyo) — informal polite (default)
  먹어 (meogeo) — intimate/banmal
  먹었어요 (meogeoosseoyo) — informal polite past
  먹었어 (meogeoosseo) — intimate past

HONORIFIC SUBJECT SUFFIX: -(으)시- inserted for respected person's action
  선생님이 가세요. (The teacher goes.) — 가 + 시 = 가세요 (honorific)
  vs 친구가 가요. (The friend goes.) — no honorific
```

### Verb Structure — Agglutination in Action

```
KOREAN VERB MORPHOLOGY — stacking suffixes
==========================================
Korean verbs are the most agglutinative part of the language.
Suffixes stack in order: STEM + [honorific] + [tense/aspect] + [mood] + [speech level]

STEM: 먹 meok- (eat)
  + 으시 (honorific) → 드시
  + 었 (past) → 먹었
  + 겠 (conjecture/future) → 먹겠
  + 어/아 (informal connective) → 먹어
  + 고 (sequential connective) → 먹고
  + 면 (conditional) → 먹으면
  + 어서 (because/and) → 먹어서
  + 지만 (but/however) → 먹지만
  + 는데 (background/contrast) → 먹는데
  + 아/어요 (polite ending) → 먹어요
  + ㄹ/을 거예요 (future intent) → 먹을 거예요

LONG CHAIN EXAMPLE:
  먹었겠어요?
  meok-eoss-gess-eoyo
  eat + PAST + CONJECTURE + POLITE QUESTION
  = "Would [they] have eaten?"
```

---

## Two Counting Systems

```
SINO-KOREAN vs NATIVE KOREAN NUMBERS
======================================
Korean has TWO complete sets of numbers, used in different contexts.

SINO-KOREAN (from Chinese):     NATIVE KOREAN:
  일(1) 이(2) 삼(3) 사(4)          하나(1) 둘(2) 셋(3) 넷(4)
  오(5) 육(6) 칠(7) 팔(8)          다섯(5) 여섯(6) 일곱(7) 여덟(8)
  구(9) 십(10) 백(100)             아홉(9) 열(10) — stops at 99

SINO-KOREAN used for:             NATIVE KOREAN used for:
  Dates (삼월 = March)             Hours of the clock (두 시 = 2 o'clock)
  Money (오천 원 = 5000 won)        Counting objects (책 한 권 = 1 book)
  Phone numbers                    Ages in informal speech
  Minutes (삼십 분 = 30 minutes)   People (up to ~10, then Sino)
  Floor numbers
  Mathematics

MIXED TIME TELLING:
  두 시 삼십 분 = 2:30
  [two hours = native] [thirty minutes = Sino]

  열두 시 = 12 o'clock (native 열=10 + 두=2)
  오전/오후 (Sino) + 시 (hour, native counting)
```

---

## 50 Essential Phrases

```
SURVIVAL KOREAN
================
안녕하세요 (Annyeonghaseyo) — Hello (formal polite)
안녕히 가세요 / 계세요 (Annyeonghi gaseyo / gyeseyo) — Goodbye (to one leaving/staying)
감사합니다 / 고마워요 (Gamsahamnida / Gomawoyo) — Thank you (formal/polite)
죄송합니다 / 미안해요 (Joesonghamnida / Mianhaeyo) — I'm very sorry / Sorry
천만에요 (Cheonmaneyo) — You're welcome
네 / 아니요 (Ne / Aniyo) — Yes / No
실례합니다 (Sillyehamnida) — Excuse me (formal)
잠깐만요 (Jamkkanmanyo) — Just a moment, please
어떻게 지내세요? (Eotteoke jinaeseyo?) — How are you?
잘 지내요, 감사해요. (Jal jinaeyo, gamsahaeyo.) — I'm doing well, thank you.
이름이 뭐예요? (Ireumi mwoyeyo?) — What is your name?
저는 ___ 예요/이에요. (Jeoneun ___ yeyo/ieyo.) — I am ___.
어디서 오셨어요? (Eodiseo osyeosseoyo?) — Where are you from?
이게 얼마예요? (Ige eolmayeyo?) — How much is this?
너무 비싸요. (Neomu bissayo.) — Too expensive.
___이/가 어디 있어요? (___ i/ga eodi isseoyo?) — Where is ___?
오른쪽 / 왼쪽 / 직진 (Oreunjjok / Oenjjok / Jikjin) — Right/Left/Go straight
영어 할 수 있어요? (Yeongeo hal su isseoyo?) — Can you speak English?
모르겠어요 (Moreugesseoyo) — I don't understand / I don't know
다시 말해 주세요 (Dasi malhae juseyo) — Please say it again
천천히 말해 주세요 (Cheoncheonhi malhae juseyo) — Please speak slowly
도와주세요! (Dowajuseyo!) — Please help!
경찰을 불러주세요! (Gyeongchareul bulleojuseyo!) — Please call the police!
화장실이 어디예요? (Hwajangshiri eodiyeyo?) — Where is the restroom?
공항 / 호텔 / 병원 (Gonghang / Hotel / Byeongwon) — Airport/Hotel/Hospital
___ 주세요 (___ juseyo) — Please give me ___
메뉴 주세요 (Menyu juseyo) — Menu please
계산해 주세요 (Gyesanhae juseyo) — Check please
```

---

## Korean vs Japanese: Key Structural Similarities and Differences

```
KOREAN vs JAPANESE COMPARISON
================================
Both are SOV, topic-prominent, verb-final, agglutinative.
But they are NOT genetically related (despite structural parallels).

+----------------------------+--------------------+--------------------+
| Feature                    | Korean             | Japanese           |
+----------------------------+--------------------+--------------------+
| Script                     | Hangul (phonemic)  | 3 scripts (mixed)  |
| Script difficulty          | Easy (~2 weeks)    | Hard (years)       |
| Verb structure             | Suffix stacking    | Suffix stacking    |
| Topic marker               | 은/는             | は                  |
| Subject marker             | 이/가             | が                  |
| Object marker              | 을/를             | を                  |
| Speech levels              | 7 (complex)        | ~3-4 (complex)     |
| Honorifics                 | -(으)시- suffix   | Different verb forms|
| Counting                   | Two systems        | Multiple systems   |
| Tones                      | None (Seoul)       | Pitch accent only  |
| Sino vocab                 | ~60% of vocabulary | ~60% of vocabulary |
| Chinese characters         | Hanja (rare today) | Kanji (daily use)  |
| Verb conjugation           | Agglutinative      | Agglutinative      |
| Adjectives                 | Verb-like (conjugate)| Two types (i/na) |
+----------------------------+--------------------+--------------------+
```

---

## Decision Cheat Sheet

| Situation | Korean approach |
|-----------|----------------|
| Script | Hangul in 1-2 weeks: phonemic, designed, fast to learn |
| After Hangul | Pronunciation rules (nasalization, tensification) before speaking |
| Speech levels | Master 해요체 first; everything else is incremental |
| Verb morphology | Learn common suffixes as chunks (-고 싶다, -어서, -(으)면) |
| Counting | Sino-Korean default for most things; native for hours + objects |
| Japanese comparison | Grammar is parallel; learn one and second is ~30% faster |
| TOPIK exam | Test of Proficiency in Korean — industry standard |

---

## Common Confusion Points

**"Hangul looks hard but it isn't"**
Unlike kanji or Arabic, Hangul is purely phonemic and was scientifically
designed. The 24 letters can be learned in a day; fluent reading in
1-2 weeks of practice. The blocks look like logograms but are phoneme groups.

**"은/는 vs 이/가 — same problem as Japanese は vs が"**
Yes, exactly the same distinction. Topic vs subject. Korean learners
from Japanese have this free. English speakers: start with 이/가 for
new info and 은/는 for known/contrast topics. Full mastery = immersion.

**"Verbs agree with what?"**
Korean verbs don't agree with subject in person/number (no conjugation
for I/you/he). They conjugate for TENSE, ASPECT, SPEECH LEVEL, MOOD, and
HONORIFICS (for the subject or object being honored). This is a fundamentally
different grammatical dimension from European agreement.

**"Adjectives conjugate like verbs?"**
Yes. Korean adjectives (형용사 hyeongyongsa) conjugate for tense,
speech level, etc. like verbs:
크다 (big, plain) → 커요 (big, polite) → 컸어요 (was big, polite past)
This is similar to Japanese i-adjectives but more systematic.

**"No spaces in North Korean?"**
North Korean orthography uses different spacing rules (fewer spaces).
South Korean spaces between words/phrases but rules are complex.
Learners sometimes see text with no spaces in informal contexts (texting).
