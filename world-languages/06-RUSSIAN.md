# Russian — Language Reference

## Profile at a Glance

```
+--------------------------------------------------------------------+
| RUSSIAN (Русский)                                                  |
+--------------------------------------------------------------------+
| Family:      Indo-European → Slavic → East Slavic                 |
| Native spkrs: ~154M                                               |
| Total spkrs:  ~250M (L1+L2)                                        |
| Countries:   Russia, Kazakhstan, Belarus, Kyrgyzstan (co-official) |
|              Widely spoken: Ukraine, Baltics, Central Asia         |
| Word order:  Free (pragmatically constrained: topic-first typical) |
| Morphology:  Fusional — highly inflected                          |
| Tonal:       No (but stress is unpredictable and morphophonemic)   |
| Gender:      Three-way (M/F/N)                                     |
| Script:      Cyrillic                                              |
| Cases:       6: Nominative, Accusative, Dative, Genitive,          |
|              Instrumental, Prepositional                           |
| FSI level:   Category III — ~1100 hours                            |
+--------------------------------------------------------------------+
```

---

## Cyrillic Alphabet

```
RUSSIAN CYRILLIC — 33 LETTERS
================================
Printed  Sound    Notes
А а      [a]      like "a" in father
Б б      [b]
В в      [v]      looks like B, sounds like V — TRAP
Г г      [g]
Д д      [d]
Е е      [ye]     after consonant: [e]; after vowel/start: [ye]
Ё ё      [yo]     often written as Е in informal text — source of confusion
Ж ж      [zh]     like "s" in measure
З з      [z]
И и      [i]      like "ee"
Й й      [y]      short [j] — as in "boy"
К к      [k]
Л л      [l]
М м      [m]
Н н      [n]      looks like H, sounds like N — TRAP
О о      [o]      stressed: [o]; unstressed: [a] — REDUCTION
П п      [p]      looks like n, sounds like p — TRAP
Р р      [r]      trilled R — looks like P
С с      [s]      looks like C, sounds like S — TRAP
Т т      [t]
У у      [u]      like "oo"
Ф ф      [f]
Х х      [kh]     like Scottish "loch", not X
Ц ц      [ts]
Ч ч      [ch]
Ш ш      [sh]     hard sh
Щ щ      [sch]    softer sh/shch
Ъ ъ      hard sign — separates prefix from soft consonant+vowel
Ы ы      [ɨ]      back vowel — no English equivalent (between "i" and "u")
Ь ь      soft sign — palatalizes preceding consonant
Э э      [e]      open e, starts words (as opposed to Е)
Ю ю      [yu]
Я я      [ya]

CRITICAL TRAPS FOR LATIN-SCRIPT READERS:
  В = V (not B)   Н = N (not H)   Р = R (not P)
  С = S (not C)   Х = KH (not X)  Е = YE (not just E)
  Я = YA          Ю = YU          Г = G
```

---

## Pronunciation

```
VOWEL REDUCTION — Russian's key phonological feature
=====================================================
Unstressed О → [a]: молоко (milk) = [mala'ko] not [moloko]
Unstressed Е → [i]: переход = [pi'rikhot]

This means you CANNOT read Russian by the spelling alone.
Stress must be memorized for each word (dictionaries mark it: молоко́).

PALATALIZATION — soft sign (Ь) and soft vowels (Е,Ё,Ю,Я,И)
  Consonant before soft sign or soft vowel = PALATALIZED (tongue touches palate)
  брат (brother) [brat] — hard T
  брать (to take) [brat'] — soft T (palatalized)
  Russian distinguishes palatalized vs non-palatalized consonants phonemically.
  ~15 consonant pairs (hard/soft). English has none.

CONSONANT CLUSTERS:
  Russian allows extreme clusters: встреча (meeting) = vstryecha
  взгляд (glance) = vzglyad
  This is why "vodka" has the "vd" cluster — natural in Russian.
```

---

## Grammar: The 6-Case System

```
RUSSIAN CASES
==============
+------------------+------------------------------------------+
| Case             | Primary use                              |
+------------------+------------------------------------------+
| NOMINATIVE (NOM) | Subject of sentence                      |
| ACCUSATIVE (ACC) | Direct object; motion toward             |
| DATIVE (DAT)     | Indirect object; beneficiary             |
| GENITIVE (GEN)   | Possession; absence; partitive; numbers  |
| INSTRUMENTAL (INS)| Instrument; means; after some preps    |
| PREPOSITIONAL(PREP)| Location (в, на); about (о)           |
+------------------+------------------------------------------+

MASCULINE NOUN ENDINGS by case (стол = table):
+------+--------+--------+
| NOM  | стол   | столы  |
| ACC  | стол   | столы  |
| GEN  | стола  | столов |
| DAT  | столу  | столам |
| INS  | столом | столами|
| PREP | столе  | столах |
+------+--------+--------+

FEMININE NOUN ENDINGS (книга = book):
+------+--------+--------+
| NOM  | книга  | книги  |
| ACC  | книгу  | книги  |
| GEN  | книги  | книг   |
| DAT  | книге  | книгам |
| INS  | книгой | книгами|
| PREP | книге  | книгах |
+------+--------+--------+

NEUTER NOUN ENDINGS (слово = word):
+------+--------+---------+
| NOM  | слово  | слова   |
| ACC  | слово  | слова   |
| GEN  | слова  | слов    |
| DAT  | слову  | словам  |
| INS  | словом | словами |
| PREP | слове  | словах  |
+------+--------+---------+

ADJECTIVE AGREEMENT (новый/new, MASC):
  NOM: новый   ACC: нового(anim)/новый(inan)   GEN: нового
  DAT: новому  INS: новым   PREP: новом
```

---

<!-- @editor[bridge/P2]: Missing concept bridge — any developer coming from typed/relational systems needs this: aspect is orthogonal to tense like concurrency is orthogonal to scheduling — a 2x2 matrix (IMP/PERF x PAST/FUTURE) would click for this learner -->
## Aspect: Perfective vs Imperfective

```
VERBAL ASPECT — the core Slavic grammatical innovation
======================================================
Every Russian verb has TWO forms:
  IMPERFECTIVE: ongoing, repeated, process, general fact
  PERFECTIVE:   completed, single, result achieved

  читать (IMP) vs прочитать (PERF) — to read
  писать (IMP) vs написать (PERF) — to write
  говорить (IMP) vs сказать (PERF) — to speak/say

CHOOSING ASPECT:
  "I was reading" (ongoing) → Я читал. (imperfective past)
  "I read (finished) the book" → Я прочитал книгу. (perfective past)

  "I used to run every morning" → Я бегал каждое утро. (IMP — repeated)
  "I ran to the store" → Я прибежал в магазин. (PERF — single arrival)

IMPERATIVES:
  IMP imperative: process/gentle request: Читайте! (Keep reading!)
  PERF imperative: single completed action: Прочитайте это! (Read this [and finish it]!)
  Negative: always IMP: Не читайте это! (Don't read this!)

PREFIXES CREATE PERFECTIVES (and change meaning):
  писать (to write) → написать (to write [and finish])
                    → вписать (to write in)
                    → записать (to write down)
                    → подписать (to sign)
  Each prefix creates a new perfective + a related imperfective pair.
```

---

## No Articles + No "To Be" in Present

```
MISSING FEATURES (compared to English)
=======================================
NO ARTICLES:
  Russian has no "the" or "a/an".
  "Книга" = the book / a book / books — context determines.
  Definiteness expressed through word order and demonstratives.

NO COPULA IN PRESENT TENSE:
  "Он студент" = He [is] a student. (No form of "be")
  "Она красивая" = She [is] beautiful.
  "Это хорошо" = That [is] good.
  Dash sometimes used in written formal Russian: Москва — столица России.

Past tense: был/была/было/были (was/were) — IS present.
Future tense: буду/будешь/будет/будем/будут (will be) — IS present.
```

---

## Verb Conjugation

```
PRESENT TENSE (two conjugation patterns)
+-----------+----------+----------+
| Person    | -ать/I   | -ить/II  |
|           | читать   | говорить |
+-----------+----------+----------+
| я         | читаю    | говорю   |
| ты        | читаешь  | говоришь |
| он/она    | читает   | говорит  |
| мы        | читаем   | говорим  |
| вы        | читаете  | говорите |
| они       | читают   | говорят  |
+-----------+----------+----------+

KEY IRREGULAR VERBS:
  БЫТЬ (to be): есть (there is/are) — only present form in common use
  ИДТИ (to go on foot): иду, идёшь, идёт, идём, идёте, идут
  ЕХАТЬ (to go by vehicle): еду, едешь, едет, едем, едете, едут
  ХОТЕТЬ (to want): хочу, хочешь, хочет, хотим, хотите, хотят

MOTION VERBS — paired system:
  идти/ходить (on foot, one direction vs general/repeated)
  ехать/ездить (by vehicle)
  лететь/летать (by air)
  плыть/плавать (by water)
  бежать/бегать (running)
  везти/возить (to carry, by vehicle)
  вести/водить (to lead, on foot)
```

---

## Pronouns

```
PERSONAL PRONOUNS (NOM form):
  я (I)  ты (you-informal)  он/она/оно (he/she/it)
  мы (we)  вы (you-formal/plural)  они (they)

VY (Вы) — formal address:
  Capital Вы in writing = formal singular you
  вы lowercase = plural
  Like French vous / German Sie

CASE FORMS of я/ты/он:
+------+----+----+----+----+----+
|      | я  | ты | он | мы | вы |
+------+----+----+----+----+----+
| NOM  | я  | ты | он | мы | вы |
| ACC  | меня|тебя|его | нас| вас|
| GEN  | меня|тебя|его | нас| вас|
| DAT  | мне | тебе|ему| нам| вам|
| INS  | мной|тобой|им | нами|вами|
| PREP | мне | тебе|нём| нас| вас|
+------+----+----+----+----+----+
After prepositions, 3rd person pronouns gain Н-: у него, к ней, с ним.
```

---

## 50 Essential Phrases

```
SURVIVAL RUSSIAN
=================
Привет (informal) / Здравствуйте (formal)
До свидания / Пока (informal)
Пожалуйста / Спасибо / Не за что
Да / Нет / Может быть
Извините / Простите / Прошу прощения
Как дела? / Хорошо, спасибо. / Неплохо.
Как вас зовут? / Меня зовут ___
Откуда вы? / Я из ___
Сколько стоит? / Это дорого. / Это дёшево.
Где ___? / Направо / Налево / Прямо
Вы говорите по-английски? / Я плохо говорю по-русски.
Я не понимаю. / Повторите, пожалуйста. / Говорите медленнее.
Помогите! / Вызовите полицию! / Вызовите скорую!
Я хочу ___ / Мне нужно ___
Есть ли у вас ___? / Нет ___
Столик на двоих / Счёт, пожалуйста
Где туалет? / Аэропорт / Гостиница / Больница
Один билет до ___ / Когда отправляется поезд?
```

---

## Decision Cheat Sheet

| Situation | Russian approach |
|-----------|----------------|
| First step | Learn Cyrillic (1-2 weeks with focus — purely mechanical) |
| Script traps | В=V, Н=N, Р=R, С=S — learn by doing, not by pattern matching |
| Hardest grammar | Aspect (IMP/PERF) — no Western language equivalent |
| Second hardest | Stress — unpredictable, changes word meaning/form |
| Case introduction | Start with NOM/ACC for basic S-V-O; add others gradually |
| Free word order | Use topic-first (new info last) — pragmatically safe default |
| Mutual intelligibility | Ukrainian ~85%, Bulgarian ~70%, Polish ~60% |

---

## Common Confusion Points

**"Free word order but not arbitrary"**
Russian word order encodes pragmatic information (topic vs focus), not
grammatical roles (cases do that). Neutral order is SVO. Moving elements
adds emphasis: "Ивана убил Борис" (It was Boris who killed Ivan) vs
"Борис убил Ивана" (Boris killed Ivan).

**"Aspect is not tense"**
Aspect is orthogonal to tense. You can have imperfective past, perfective
past, imperfective future, perfective future. Aspect encodes how the speaker
frames the action — as process vs as completed event.

**"Genitive of absence"**
To say "there is no X" → genitive: Нет книги. (No book. / There is no book.)
To say "there is X" → nominative: Здесь книга. (There is a book here.)
Genitive for negation is pervasive.

**"After numbers, unexpected case"**
1 → nominative: 1 книга
2-4 → genitive singular: 2 книги
5+ → genitive plural: 5 книг
11-19 → always genitive plural: 11 книг
21, 22... → same pattern as 1, 2... again
Russian schoolchildren find this hard too.

**"Stressed vowel vs unstressed vowel"**
о pronounced [a] when unstressed — молоко sounds like [malako].
е/я pronounced [i] when unstressed. You cannot sound natural without
learning the stress pattern of common words.
