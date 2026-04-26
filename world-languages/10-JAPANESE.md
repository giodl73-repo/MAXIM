# Japanese — Language Reference (Deep Dive)

## Profile at a Glance

```
+--------------------------------------------------------------------+
| JAPANESE (日本語 Nihongo)                                          |
+--------------------------------------------------------------------+
| Family:      Japonic (language isolate family — no proven relative)|
| Native spkrs: ~125M                                               |
| Total spkrs:  ~128M                                               |
| Countries:   Japan (only major country)                            |
| Word order:  SOV — strict verb-final                              |
| Morphology:  Agglutinative                                         |
| Tonal:       Pitch accent (dialect-dependent, not strictly tonal)  |
| Gender:      None (grammatical)                                    |
| Script:      THREE scripts used simultaneously:                    |
|              Hiragana + Katakana + Kanji (+ Rōmaji occasionally)  |
| Cases:       None — particles mark grammatical roles              |
| FSI level:   Category IV — ~2200 hours (hardest for English)       |
+--------------------------------------------------------------------+
```

---

## The Big Picture: Three Scripts

```
JAPANESE SCRIPT SYSTEM
=======================
Three scripts interleave in every sentence:

  +------------------+------------------+------------------+
  | HIRAGANA         | KATAKANA         | KANJI            |
  | (ひらがな)        | (カタカナ)        | (漢字)            |
  +------------------+------------------+------------------+
  | 46 syllables     | 46 syllables     | ~2136 jōyō       |
  | (+ diacritics)   | (+ diacritics)   | (required chars) |
  | Native Japanese  | Foreign loanwords| Sino-Japanese    |
  | words + grammar  | + emphasis       | vocabulary +     |
  | Grammar particles| Scientific names | native compound  |
  | Verb endings     | Sound effects    | words            |
  | Children's texts | (manga)          |                  |
  +------------------+------------------+------------------+

EXAMPLE SENTENCE:
  私はコーヒーを飲みます。
  私  は コーヒー を 飲み  ます
  Watashi wa kōhī    wo nomi  masu
  [KANJI] [H] [KATAKANA] [H] [KANJI+H][H]
  I    [topic] coffee  [obj] drink [polite]
  "I drink coffee."

  は = wa (topic particle) → hiragana
  を = wo (object particle) → hiragana
  コーヒー = kōhī (coffee) → katakana (loanword)
  飲み = nomi (stem of drink) → kanji 飲 + hiragana み
  ます = masu (polite ending) → hiragana

READING ORDER: horizontal left-to-right OR vertical top-to-bottom right-to-left
  Vertical: traditional books, manga (right-to-left page turn)
  Horizontal: internet, technical documents, most modern text
```

---

## Hiragana — Full Table

```
HIRAGANA (ひらがな) — 46 basic + diacritics
===========================================
     a     i     u     e     o
  あ    い    う    え    お
  ka  き   く   け   こ
  か    き    く    け    こ
  sa  し   す   せ   そ
  さ    し    す    せ    そ    (shi = し not "si")
  ta  ち   つ   て   と
  た    ち    つ    て    と    (chi = ち, tsu = つ)
  na  に   ぬ   ね   の
  な    に    ぬ    ね    の
  ha  ひ   ふ   へ   ほ
  は    ひ    ふ    へ    ほ    (fu = ふ not "hu")
  ma  み   む   め   も
  ま    み    む    め    も
  ya       ゆ        よ
  や         ゆ         よ
  ra  り   る   れ   ろ
  ら    り    る    れ    ろ    (r = flap, between R and L)
  wa                 を
  わ                   を    (wo = を — only used as object particle)
  n/m
  ん    (syllable-final nasal — varies by context)

DAKUTEN DIACRITICS (゛adds voiced):
  か→が  き→ぎ  く→ぐ  け→げ  こ→ご  (k→g)
  さ→ざ  し→じ  す→ず  せ→ぜ  そ→ぞ  (s→z)
  た→だ  ち→ぢ  つ→づ  て→で  と→ど  (t→d)
  は→ば  ひ→び  ふ→ぶ  へ→べ  ほ→ぼ  (h→b)
HANDAKUTEN (゜adds p):
  は→ぱ  ひ→ぴ  ふ→ぷ  へ→ぺ  ほ→ぽ  (h→p)

COMBINATION SYLLABLES (small や/ゆ/よ):
  きゃ(kya) きゅ(kyu) きょ(kyo)
  しゃ(sha) しゅ(shu) しょ(sho)
  ちゃ(cha) ちゅ(chu) ちょ(cho)
  にゃ(nya) みゃ(mya) りゃ(rya) etc.
```

---

## Katakana — Full Table

```
KATAKANA (カタカナ) — mirrors hiragana in sounds
================================================
     a     i     u     e     o
  ア    イ    ウ    エ    オ
  カ    キ    ク    ケ    コ
  サ    シ    ス    セ    ソ
  タ    チ    ツ    テ    ト
  ナ    ニ    ヌ    ネ    ノ
  ハ    ヒ    フ    ヘ    ホ
  マ    ミ    ム    メ    モ
  ヤ         ユ         ヨ
  ラ    リ    ル    レ    ロ
  ワ                   ヲ
  ン    (final nasal)
  ー    (chōonpu: long vowel extender — コーヒー = kō-hī)

KATAKANA USED FOR:
  Foreign loanwords: テレビ (terebi = TV), コンピューター (konpyūtā = computer)
  Foreign names: マイクロソフト (Maikurosofuto = Microsoft)
  Scientific/technical: アルコール (arukōru = alcohol)
  Sound effects/onomatopoeia in manga: ドキドキ (dokidoki = heartbeat)
  Emphasis (like italics): これはヤバい = THIS is bad

LOAN WORD TRANSFORMATION:
  English → katakana involves approximation:
  "McDonald's" → マクドナルド (Makudonarudo)
  "smartphone" → スマートフォン (sumātofon)
  "convenience store" → コンビニ (konbini — clipped)
  "air conditioner" → エアコン (eakon — clipped)
  Long words often clipped in everyday speech.
```

---

## Kanji System

```
KANJI — CHINESE CHARACTERS IN JAPANESE
========================================
Japan borrowed Chinese characters ~1500 years ago.
~2136 jōyō kanji required for functional adult literacy.
Japanese educated adult knows ~3000-4000 kanji.

TWO READING SYSTEMS per kanji:
  ON'YOMI (音読み) — Chinese-derived reading
    Used in: Sino-Japanese compound words (多い words)
    General pattern: 2+ kanji together → on'yomi
    Example: 日 (nichi/jitsu) in 日本 (Nihon = Japan)

  KUN'YOMI (訓読み) — native Japanese reading
    Used in: single kanji standalone, with hiragana okurigana
    Example: 日 (hi) alone = day/sun; 今日 (kyō) = today

EXAMPLES OF DUAL READINGS:
  山 (mountain):  on = san  (in 富士山 Fuji-san)
                  kun = yama (alone: 山 yama)
  水 (water):     on = sui  (in 水泳 suiei = swimming)
                  kun = mizu (alone: 水 mizu)
  大 (big):       on = dai/tai (大学 daigaku = university)
                  kun = ō/ōkii (大きい ōkii = big adjective)

LEARNING STRATEGY:
  Learn kanji in context, not isolation.
  JLPT N5 (~100 kanji) → N4 (~300) → N3 (~650) → N2 (~1000) → N1 (~2000)
  Radicals help: 氵(water) in all water-related kanji: 海/河/泳/洗
  Mnemonics systems (Heisig's Remembering the Kanji) for writing production.
  Recognition (reading) comes faster than writing production.

FURIGANA — small hiragana above kanji showing pronunciation:
  Used in: children's books, learner materials, manga for younger readers
  Some adult manga/novels use furigana for uncommon kanji.
```

---

## Grammar Core

### Particles — The Structural Foundation

```
JAPANESE PARTICLES — markers that follow nouns to show role
===========================================================
Every noun phrase needs a particle. No particles = ungrammatical.

+--------+--------+-----------------------------------------------+
| Part.  | Romaji | Function                                      |
+--------+--------+-----------------------------------------------+
| は     | wa     | TOPIC — "as for X" (sets what sentence is about)|
| が     | ga     | SUBJECT — marks grammatical subject           |
| を     | wo/o   | OBJECT — marks direct object                  |
| に     | ni     | Location (static), direction, indirect obj,   |
|        |        | time point, purpose                           |
| で     | de     | Location (action), means/instrument, cause    |
| の     | no     | Possession, modification (A-no-B = A's B)     |
| も     | mo     | Also/either: "too"                            |
| から   | kara   | From (starting point, cause)                 |
| まで   | made   | Until, up to                                  |
| と     | to     | And (exhaustive), with, quotation             |
| か     | ka     | Question marker (sentence-final)              |
| よ     | yo     | Assertion / new info for listener             |
| ね     | ne     | Seeking agreement / soft statement            |
+--------+--------+-----------------------------------------------+

WA vs GA — the hardest distinction in Japanese:
  は wa = topic (what the sentence is ABOUT — can be subject or object)
  が ga = subject (neutral subject marker, new information, exhaustive identification)

  猫は魚を食べる。 = As for cats, [they] eat fish. (general statement)
  猫が魚を食べる。 = The CAT eats fish. (not the dog)
  猫が好きです。  = I like cats. (が marks the object of liking, not subject)
  私は猫が好きです。 = As for me, I like cats. (wa = topic は; が = subject of 好き)
```

### Verb System

```
VERB CONJUGATION — GODAN vs ICHIDAN
=====================================
All verbs end in -u in dictionary form.
Two classes: GODAN (Group 1) and ICHIDAN (Group 2)

GODAN (u-verbs) — stem changes:
  書く kaku (write): stem changes → ka-ki-ku-ke-ko-ka
  飲む nomu (drink): stem changes → nom-/nin-/now-
  行く iku (go): irregular godan

ICHIDAN (ru-verbs) — stem doesn't change:
  食べる taberu (eat): stem = tabe-, drop -ru for masu, te, ta forms
  見る miru (see): stem = mi-

POLITE vs PLAIN FORMS:
  Plain (dictionary): 食べる taberu — used in casual speech, subordinate clauses
  Polite (masu):     食べます tabemasu — used in formal speech, most daily situations

CONJUGATION TABLE (食べる taberu):
+-------------------+----------+-------------+
| Form              | Plain    | Polite      |
+-------------------+----------+-------------+
| Present/Future    | 食べる   | 食べます    |
| Past              | 食べた   | 食べました  |
| Negative pres.    | 食べない  | 食べません  |
| Negative past     | 食べなかった| 食べません  |
|                   |          | でした      |
| Te-form (connect) | 食べて   | —           |
| Potential (can)   | 食べられる| 食べられます|
| Passive           | 食べられる| 食べられます|
| Causative         | 食べさせる| 食べさせます|
| Conditional (-ば) | 食べれば  | —           |
| Volitional (let's)| 食べよう  | 食べましょう|
+-------------------+----------+-------------+

KEY IRREGULAR VERBS:
  する suru (do): します/した/しない/できる(potential)
  くる kuru (come): きます/きた/こない
  ある aru (exist, inanimate): あります/あった — NO negative aru (use ない)
  いる iru (exist, animate): います/いた/いない
```

### Adjective System

```
TWO ADJECTIVE TYPES in Japanese
==================================
I-ADJECTIVES (い形容詞) — end in い, conjugate directly:
  大きい ōkii (big)
  Past: 大きかった  Neg: 大きくない  Neg past: 大きくなかった
  Adverb: 大きく (+ verb)

NA-ADJECTIVES (な形容詞) — need な before noun, conjugate via だ/です:
  きれい kirei (beautiful/clean) → きれいな花 (beautiful flower)
  静か shizuka (quiet) → 静かな部屋 (quiet room)
  Past: きれいだった  Neg: きれいじゃない  (like nouns)

ADJECTIVE POSITION: BEFORE the noun (Japanese is head-final)
  日本語: 赤い車 (red car) — adjective BEFORE noun
  English: red car — same order (unusually, English is also head-initial with adjectives)
```

---

## Keigo: The Honorific Register System

**The access-control model:** Japanese keigo is a grammatically encoded permission system. Each utterance carries an authorization level that reflects the relative social position of speaker, listener, and the third party being described. The verb form IS the access token:

```
ACCESS CONTROL TABLE — KEIGO:

+-----------+--------------------+-----------------+-----------------------------+
| Register  | System             | Direction       | Use context                 |
+-----------+--------------------+-----------------+-----------------------------+
| SONKEIGO  | Elevated verbs     | Raises OTHER     | Describing what someone     |
| (尊敬語)  | for the other      | person's actions → superior or in-group guest   |
|           | person's actions   | (grants elevated | is doing. Never use for     |
|           |                    | access to them)  | yourself.                   |
|           | 行く→いらっしゃる  |                 |                             |
|           | 言う→おっしゃる    |                 |                             |
|           | 食べる→召し上がる  |                 |                             |
+-----------+--------------------+-----------------+-----------------------------+
| KENJŌGO   | Humble verbs for   | Lowers YOUR OWN | Describing your own actions|
| (謙譲語)  | the speaker's own  | actions         | to a superior or customer.  |
|           | actions            | (requests lower | Humbling yourself =         |
|           |                    | access for self) | elevating the other.       |
|           | 行く→参る          |                 |                             |
|           | 言う→申す          |                 |                             |
|           | 食べる→いただく    |                 |                             |
+-----------+--------------------+-----------------+-----------------------------+
| TEINEIGO  | Polite copula/     | Neutral —        | Safe default. All formal    |
| (丁寧語)  | verb endings       | baseline secure  | situations, strangers,      |
|           | (masu/desu forms)  | tier             | service interactions.       |
|           |                    |                 | Does not assert relative    |
|           |                    |                 | rank.                       |
+-----------+--------------------+-----------------+-----------------------------+
| Plain     | Dictionary forms   | No access token | Close friends, family,      |
| (常体)    |                    | asserted         | internal monologue, writing.|
|           |                    |                 | Using this to a superior    |
|           |                    |                 | = dropped connection.       |
+-----------+--------------------+-----------------+-----------------------------+

PRACTICAL DISPATCH:
  stranger/customer/superior → teineigo baseline
  describing their action → switch to sonkeigo for THEIR verbs
  describing your own action in response → switch to kenjōgo for YOUR verbs
  close friend/peer → plain form is fine

  In a business email or customer service interaction:
  "先生はいらっしゃいますか?" (Is the teacher here? — sonkeigo for teacher)
  "私は後ほど参ります。" (I will come later — kenjōgo for self)
  Both in the same utterance — the encoding is per-verb, per-agent.
```

**The architectural point:** Keigo is not politeness as an attitude; it is an encoding of social topology in grammar. The verb form carries a mandatory access-level annotation that declares the speaker's model of who occupies which position in the social graph. Misfiring this encoding is not "slightly impolite" — it is a syntactically-detectable access violation.

```
JAPANESE HONORIFICS (敬語 keigo)
===================================
Japanese has THREE honorific levels encoded grammatically.

SONKEIGO (尊敬語) — elevates the OTHER person's actions:
  行く → いらっしゃる (iku → irassharu) — to go/be (elevated)
  言う → おっしゃる (iu → ossharu) — to say (elevated)
  食べる → 召し上がる (taberu → meshiagaru) — to eat (elevated)
  "先生はどちらへいらっしゃいますか?" — Where is the teacher going?

KENJŌGO (謙譲語) — humbles the SPEAKER's own actions:
  行く → 参る (iku → mairu) — I go (humble)
  言う → 申す (iu → mōsu) — I say (humble)
  食べる → いただく (taberu → itadaku) — I eat (humble)
  "私は明日参ります。" — I will go tomorrow. (humble)

TEINEIGO (丁寧語) — general politeness (masu/desu forms):
  食べます tabemasu — polite "I eat"
  です desu — polite copula

PRACTICAL LEVELS:
  ます/です — safe default for all formal situations
  Plain forms — close friends, family, internal monologue
  Sonkeigo/kenjōgo — business settings, service industry, formal writing

In a Japanese company, using plain form to a superior = rude.
Service industry workers speak highly elevated keigo to customers.
O- and go- prefixes elevate nouns: お水 (o-mizu = water, politely).
```

---

## Topic-Prominent Structure

```
TOPIC PROMINENCE — Japanese focuses on "what we're talking about"
==================================================================
Japanese is "topic-prominent" — sentences center around the topic (は wa).

Subject can be dropped when understood from context (pro-drop):
  A: 田中さんはどこですか? (Where is Tanaka-san?)
  B: (田中さんは)コンビニに行きました。 ([He] went to the convenience store.)
     → Subject dropped because clear from context.

Topics can be objects or other elements:
  魚は猫が食べた。 (As for fish, the cat ate [it].) — object topicalized
  日本語は難しい。 (As for Japanese, it's difficult.) — subject topicalized
  東京は物価が高い。 (As for Tokyo, prices are expensive.) — place topicalized
```

---

## Counters (Japanese Counting System)

```
JAPANESE COUNTERS — similar to Chinese measure words
=====================================================
Every type of object has a counter suffix. Number + counter = correct.

COMMON COUNTERS:
+--------+-------+-------------------------------------------+
| 本 hon | books | Also: long thin objects: pens, bottles,   |
|        |       | rivers, roads, fingers                    |
| 枚 mai |       | Flat thin objects: paper, shirts, slices  |
| 台 dai |       | Machines: cars, computers, TVs            |
| 匹 hiki|       | Small animals: cats, dogs, fish           |
| 頭 tou |       | Large animals: horses, cows, elephants    |
| 羽 wa  |       | Birds + rabbits                           |
| 冊 satsu|      | Bound books, notebooks                    |
| 杯 hai |       | Cups, glasses, bowls of liquid/food       |
| 足 soku|       | Pairs of footwear                         |
| 着 chaku|      | Clothing items                            |
| 人 nin | people| (ひとり hitōri=1, ふたり futari=2 — irregular)|
| 個 ko  |       | General small objects (default)           |
| 回 kai | times | Number of times/occurrences               |
| 番 ban |       | Order/rank (first, second...)             |
| 階 kai | floors| Floor of building (1F=一階)               |
+--------+-------+-------------------------------------------+

NUMBER FORMS: 1 and 2 have irregular native forms for people:
  1 person = ひとり (hitōri)    2 people = ふたり (futari)
  3+ people = 三人 (sannin), 四人 (yonin)...
```

---

## 50 Essential Phrases

```
SURVIVAL JAPANESE
==================
こんにちは (Konnichiwa) — Hello (daytime)
おはようございます (Ohayō gozaimasu) — Good morning (formal)
こんばんは (Konbanwa) — Good evening
さようなら / じゃあね (Sayōnara / Jā ne) — Goodbye (formal/informal)
お願いします (Onegaishimasu) — Please (requesting)
ありがとうございます (Arigatō gozaimasu) — Thank you (formal)
どういたしまして (Dōitashimashite) — You're welcome
はい / いいえ (Hai / Iie) — Yes / No
すみません (Sumimasen) — Excuse me / I'm sorry (attention-getter)
ごめんなさい (Gomen nasai) — I'm sorry (apology)
お元気ですか？(O-genki desu ka?) — How are you? (formal)
元気です、ありがとう。(Genki desu, arigatō.) — I'm fine, thank you.
お名前は何ですか？(O-namae wa nan desu ka?) — What is your name?
私は ___ です。(Watashi wa ___ desu.) — I am ___.
どこから来ましたか？(Doko kara kimashita ka?) — Where did you come from?
これはいくらですか？(Kore wa ikura desu ka?) — How much is this?
高いですね。(Takai desu ne.) — It's expensive, isn't it.
___はどこですか？(___ wa doko desu ka?) — Where is ___?
右 / 左 / まっすぐ (Migi / Hidari / Massugu) — Right/Left/Straight
英語を話せますか？(Eigo wo hanasemasu ka?) — Can you speak English?
わかりません (Wakarimasen) — I don't understand
もう一度言ってください (Mō ichido itte kudasai) — Please say it again
ゆっくり話してください (Yukkuri hanashite kudasai) — Please speak slowly
助けて！(Tasukete!) — Help!
警察を呼んでください！(Keisatsu wo yonde kudasai!) — Please call the police!
お手洗いはどこですか？(O-tearai wa doko desu ka?) — Where is the toilet?
空港 / ホテル / 病院 (Kūkō / Hoteru / Byōin) — Airport/Hotel/Hospital
___ をください (___ wo kudasai) — Please give me / I'll have ___
メニューをください (Menū wo kudasai) — Menu please
お会計をお願いします (O-kaikei wo onegaishimasu) — Check please
```

---

## Decision Cheat Sheet

| Situation | Japanese approach |
|-----------|-----------------|
| First priority | Hiragana — 1-2 weeks. Then katakana — 1 week. Essential. |
| Script order | Hiragana → Katakana → Kanji (parallel) |
| Kanji strategy | Context-first: learn by frequency + JLPT levels |
| Grammar | SOV + verb-final is the biggest adjustment from SVO |
| Politeness | Default to ます/です (polite form) with anyone except close friends |
| Keigo | Passive recognition of sonkeigo/kenjōgo enough for most learners |
| On/kun | Learn in vocabulary context, not as abstract pairs |
| Particles | は/が distinction: don't force it early — natural acquisition works |

---

## Common Confusion Points

**"は wa vs が ga — which one is the subject?"**
Both can mark the grammatical subject. は marks topic (what sentence is about).
が marks new info or exhaustive identification. In "私は学生です" — は makes
"I" the topic. In "誰が来た？田中さんが来た" — が identifies who came.
Best approach: absorb via exposure; don't try to resolve it with rules.

**"Japanese pitch accent?"**
Japanese has a pitch accent system (high-low pitch patterns) that can
distinguish words: 橋 hashi (bridge) vs 箸 hashi (chopsticks) differ in pitch.
Tokyo accent: most words have one pitch drop point.
This is far less demanding than Mandarin tones but still present.
Most learners can communicate without mastering it.

**"Japanese R is not English R or L?"**
The Japanese ら行 (r-row) sound is a flap [ɾ] — tongue briefly touches
the alveolar ridge, like the "dd" in "ladder" or "t" in British "better".
Not the English R (retroflex) nor the English L (lateral).
"ラ" sounds between R and L to English speakers.

**"Passive is also used for receiving something unfortunate?"**
Japanese has "adversative passive" — passive used to express that the
subject was negatively affected by someone else's action.
"雨に降られた" (ame ni furareta) = I was rained on / Rain fell [on me].
This use has no English equivalent grammatical form.

**"Verb at the end — how do you know where the sentence ends?"**
In conversation: pauses + the characteristic falling intonation of verb-final.
In writing: the main verb is the last element before sentence-final particles
(よ, ね, か, わ) or sentence boundary.
Subordinate clauses come BEFORE their main verb, so nested sentences
look like: [[[clause] clause] main verb].
