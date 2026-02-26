# German — Language Reference

## Profile at a Glance

```
+--------------------------------------------------------------------+
| GERMAN (Deutsch)                                                   |
+--------------------------------------------------------------------+
| Family:      Indo-European → Germanic → West Germanic             |
| Native spkrs: ~95M                                                 |
| Countries:   Germany, Austria, Switzerland, Liechtenstein,         |
|              South Tyrol (Italy), Belgium, Luxembourg              |
| Word order:  V2 (main clauses); SOV (subordinate clauses)          |
| Morphology:  Fusional — 4-case system                             |
| Tonal:       No                                                    |
| Gender:      Three-way (M/F/N)                                     |
| Script:      Latin (+ Umlauts: ä ö ü ß)                          |
| Cases:       4: Nominative, Accusative, Dative, Genitive           |
| FSI level:   Category II — ~900 hours                              |
+--------------------------------------------------------------------+
```

---

## The Big Picture

```
GERMAN GRAMMAR ARCHITECTURE
=============================

  NOUNS                      VERBS                   CASES
  ------                     -----                   -----
  3 grammatical genders      Strong vs weak           4 cases
  (der/die/das)              verbs                    determine
  All nouns capitalized      Modal verbs              role of noun
  in writing                 Separable verbs          in sentence
       |                          |                        |
       v                          v                        v
  Articles decline           V2 word order:          Subject = NOM
  across 4 cases             verb always 2nd         Direct obj = ACC
       |                     in main clause          Indirect obj = DAT
       v                          |                  Possession = GEN
  Adjectives agree           SOV in subord.              |
  (complex endings)          clause: verb LAST           v
                                                     Article endings
                                                     change accordingly
                                                     (der → den, etc.)

KEY INSIGHT:
  German word order can be scrambled BECAUSE case marks function.
  "Den Hund beißt der Mann" = "Der Mann beißt den Hund" = Man bites dog.
  (den = accusative → den Hund is the object regardless of position)
```

---

## The Case System

**The typed-function-parameter model:** German cases are syntactic role annotations carried by the article (and adjective endings), not by the noun itself. The article is the type annotation; the noun is the value. Swapping word order does not change meaning because the type annotation travels with the noun wherever it moves.

```
TYPED FUNCTION CALL ANALOGY:

  bite(subject: Person, object: Dog)
  bite(Den Hund beißt der Mann)
       ^^^^                ^^^
       ACC=object         NOM=subject

  The article "den" (ACC) tags "Hund" as the object.
  The article "der" (NOM) tags "Mann" as the subject.
  Word order is irrelevant — the type annotation encodes the role.

  Compare English (no case on nouns):
    "The man bites the dog" ≠ "The dog bites the man"
    → word order IS the type annotation in English
    → English encodes role by position; German encodes role by inflection

FOUR CASES = FOUR ARGUMENT ROLES:
  NOM (nominative) → subject (the doer, predicate subject)
  ACC (accusative) → direct object (the done-to), motion toward
  DAT (dative)     → indirect object (recipient), location, some prepositions
  GEN (genitive)   → possessor ("of"), some prepositions

ARTICLE = TYPE ANNOTATION, changes by case+gender:
  der Mann (NOM, M) → den Mann (ACC, M) → dem Mann (DAT, M) → des Mannes (GEN, M)
  die Frau (NOM, F) → die Frau (ACC, F) → der Frau (DAT, F) → der Frau (GEN, F)
  das Kind (NOM, N) → das Kind (ACC, N) → dem Kind (DAT, N) → des Kindes (GEN, N)

The article is doing the work that prepositions do in English:
  English: "I give TO the man" — preposition "to" marks indirect object
  German:  "Ich gebe dem Mann" — DAT article encodes the same relation
```

### Articles Declined by Case

```
DEFINITE ARTICLES (the):
+----------+-----------+---------+-----------+
| Case     | MASC      | FEM     | NEUT      | PLURAL |
+----------+-----------+---------+-----------+--------+
| NOM      | der       | die     | das       | die    |
| ACC      | den       | die     | das       | die    |
| DAT      | dem       | der     | dem       | den    |
| GEN      | des       | der     | des       | der    |
+----------+-----------+---------+-----------+--------+

INDEFINITE ARTICLES (a/an):
+----------+-----------+---------+-----------+
| Case     | MASC      | FEM     | NEUT      |
+----------+-----------+---------+-----------+
| NOM      | ein       | eine    | ein       |
| ACC      | einen     | eine    | ein       |
| DAT      | einem     | einer   | einem     |
| GEN      | eines     | einer   | eines     |
+----------+-----------+---------+-----------+

USAGE:
  NOM — subject:         Der Mann schläft. (The man sleeps.)
  ACC — direct object:   Ich sehe den Mann. (I see the man.)
  DAT — indirect object: Ich gebe dem Mann das Buch. (I give the man the book.)
  GEN — possession:      Das Buch des Mannes. (The man's book.)
```

### Case with Prepositions

```
PREPOSITIONS THAT TAKE ACCUSATIVE:
  durch (through), für (for), gegen (against), ohne (without), um (around)
  "Er fährt durch den Tunnel." (through the tunnel → ACC)

PREPOSITIONS THAT TAKE DATIVE:
  aus (from), bei (at/near), mit (with), nach (after/to), seit (since),
  von (from/of), zu (to), gegenüber (opposite), außer (except)
  "Er fährt mit dem Auto." (with the car → DAT)

TWO-WAY PREPOSITIONS (movement=ACC, location=DAT):
  an, auf, hinter, in, neben, über, unter, vor, zwischen

  ACC (where to?):   Ich gehe in den Garten. (I go into the garden.)
  DAT (where?):      Ich bin im Garten. (I am in the garden.)

  "in den Garten" ← movement (ACC)
  "im Garten" ← location (DAT) [im = in+dem]
```

### The Three Genders

```
GRAMMATICAL GENDER — cannot always be predicted
================================================
  der (MASC): der Mann, der Tisch, der Apfel, der Wagen
  die (FEM):  die Frau, die Tür, die Zeit, die Schule
  das (NEUT): das Kind, das Buch, das Haus, das Mädchen

GENDER CLUES (not rules):
  -ung, -heit, -keit, -schaft, -ion → always FEM (die Zeitung, die Freiheit)
  -er, -en, -el (agent nouns) → often MASC (der Lehrer, der Wagen, der Schlüssel)
  -chen, -lein (diminutives) → always NEUT (das Mädchen, das Fräulein)
  -nis, -tum → usually NEUT (das Ereignis, das Wachstum)
  -ment, -ium → usually NEUT (das Experiment, das Gymnasium)

  For everything else: memorize as compound (das Buch, not just Buch).
```

---

## Word Order: V2 and SOV

```
V2 RULE — Verb in Second Position (main clauses)
================================================
"The verb is always in position 2" — meaning the second CHUNK, not word.

  Subject first:
  [Ich]     [komme]  [morgen]  nach Hause.
   pos 1     pos 2    pos 3      pos 4

  Adverb first (inversion — NOT unusual):
  [Morgen]  [komme]  [ich]     nach Hause.
   pos 1     pos 2    pos 3

  Object first (topicalization):
  [Den Wein] [trinke]  [ich]  gerne.
   pos 1      pos 2    pos 3

SOV IN SUBORDINATE CLAUSES — verb LAST
  Main: Ich komme, weil ich müde bin.
                          ↑ because     ↑ verb at END

  All subordinating conjunctions trigger verb-last:
  weil (because), dass (that), wenn (when/if), obwohl (although),
  nachdem (after), bevor (before), damit (so that)

SEPARABLE VERBS — prefix detaches and goes to the END in main clause
  anrufen (to call): Ich rufe dich morgen AN.
                     prefix "an" kicked to end of clause
  aufmachen (to open): Sie macht die Tür AUF.
  In subordinate clause: prefix stays attached (verb last anyway)
  "..., weil ich dich anrufe."
```

---

## Verb System

### Regular and Irregular Verbs

```
WEAK (REGULAR) VERBS — machen (to make/do):
+-----------+---------+
| ich       | mache   |
| du        | machst  |
| er/sie/es | macht   |
| wir       | machen  |
| ihr       | macht   |
| sie/Sie   | machen  |
+-----------+---------+

STRONG (IRREGULAR) VERBS — vowel change pattern
  sprechen (to speak): ich spreche, du SPRICHST, er SPRICHT, wir sprechen
  fahren (to drive):   ich fahre, du FÄHRST, er FÄHRT, wir fahren
  sehen (to see):      ich sehe, du SIEHST, er SIEHT, wir sehen
  nehmen (to take):    ich nehme, du NIMMST, er NIMMT, wir nehmen

HIGHLY IRREGULAR (must memorize):
  SEIN (to be):  bin, bist, ist, sind, seid, sind
  HABEN (to have): habe, hast, hat, haben, habt, haben
  WERDEN (to become/will): werde, wirst, wird, werden, werdet, werden

PAST TENSE — two systems:
  Präteritum (simple past, WRITTEN): ich machte, er fuhr, sie sah
  Perfekt (compound past, SPOKEN):   ich habe gemacht, er ist gefahren
  Same split as French passé simple vs passé composé.
  In speech: use Perfekt for almost everything.
  Modal verbs: Präteritum preferred even in speech.
```

### Modal Verbs

```
MODAL VERBS
============
  dürfen — may (permission)
  können — can (ability)
  mögen  — like (preference); möchten — would like
  müssen — must (necessity)
  sollen — should (obligation from outside)
  wollen — want (own desire)

Frame: Modal in position 2 + infinitive at END of clause.
  Ich kann morgen nicht kommen. (I can't come tomorrow.)
  Er will das Buch lesen. (He wants to read the book.)
  Sie muss heute arbeiten. (She must work today.)
```

---

## Nouns, Compounds, and Capitalization

```
GERMAN COMPOUND WORDS — no spaces
====================================
German piles nouns together into single words:
  Donaudampfschifffahrtsgesellschaftskapitän
  = Danube+steam+ship+travel+company+captain
  (captain of a Danube steam shipping company)

  Practical compounds:
  Krankenhaus  = Kranken (sick) + Haus (house) = hospital
  Fernseher    = fern (far) + sehen (see) = television
  Handschuh    = Hand + Schuh (shoe) = glove
  Kühlschrank  = kühl (cool) + Schrank (cabinet) = refrigerator

  Last element determines gender: das Krankenhaus (das from Haus)

ALL NOUNS CAPITALIZED:
  der Mann, die Stadt, das Buch — capital M, S, B always.
  This makes reading easier — you can spot nouns instantly.
```

---

## Pronouns and Formal Address

```
FORMAL PRONOUN: Sie (capital S)
================================
  du  — informal singular (friends, family, children, peers, animals)
  ihr — informal plural
  Sie — formal singular AND plural (always capital S)
       = same form as 3rd person plural "sie" but always capitalized

  German workplaces: traditionally "Sie" until explicitly offered "du"
  (duzen = offering to switch to du)
  Modern startups and tech companies use "du" universally.
  Academic settings: often "Sie" for professor-student

REFLEXIVE PRONOUNS:
  sich — 3rd person reflexive: Er wäscht sich. (He washes himself.)
  Reflexive verbs important in German: sich freuen (to be happy),
  sich vorstellen (to introduce oneself), sich erinnern (to remember)
```

---

## Adjective Endings — The Matrix

```
STRONG (no article preceding):
  Masc NOM: kalter Kaffee   Fem NOM: kalte Milch   Neut NOM: kaltes Wasser

WEAK (after definite article der/die/das):
  Masc NOM: der alte Mann   Fem NOM: die alte Frau  Neut NOM: das alte Kind
  Masc ACC: den alten Mann  Fem ACC: die alte Frau  Neut ACC: das alte Kind
  DAT (all): dem/der alten...  GEN (all): des/der alten...+s/n noun

MIXED (after indefinite ein/eine/ein):
  NOM: ein alter Mann, eine alte Frau, ein altes Kind
  (needs strong ending because ein doesn't mark gender)

PRACTICAL APPROACH: Learn "weak" endings first (after der/die/das).
  Most adjective usage involves definite articles.
```

---

## 50 Essential Phrases

```
SURVIVAL GERMAN
================
Guten Morgen / Guten Tag / Guten Abend / Hallo
Auf Wiedersehen / Tschüss / Bis bald / Bis morgen
Bitte / Danke / Danke schön / Bitte sehr / Gern geschehen
Ja / Nein / Vielleicht / Natürlich
Entschuldigung / Entschuldigen Sie / Verzeihung / Es tut mir leid
Wie geht es Ihnen? (formal) / Wie geht's? (informal)
Gut, danke. / Es geht. / Nicht so gut.
Wie heißen Sie? / Ich heiße ___ / Mein Name ist ___
Woher kommen Sie? / Ich komme aus ___
Wie viel kostet das? / Das ist teuer. / Das ist günstig.
Wo ist ___? / Rechts / Links / Geradeaus
Sprechen Sie Englisch? / Ich spreche nicht gut Deutsch.
Ich verstehe nicht. / Können Sie das wiederholen? / Langsamer bitte.
Hilfe! / Rufen Sie die Polizei! / Rufen Sie einen Arzt!
Ich möchte ___ / Ich brauche ___
Haben Sie ___? / Es gibt kein/keine ___
Einen Tisch für zwei / Die Rechnung bitte
Wo ist die Toilette? / Der Flughafen / Das Hotel / Das Krankenhaus
Ich möchte eine Fahrkarte nach ___
Wann fährt der Zug? / Wann kommt er an?
```

---

## Decision Cheat Sheet

| Situation | German approach |
|-----------|----------------|
| Biggest hurdle | 3 genders + 4-case article declension |
| Second hardest | Word order: V2 main clause, SOV subordinate, separable verbs |
| First thing to learn | sein/haben/werden + present tense of regular verbs |
| Past tense in speech | Perfekt (ich habe gemacht) — not Präteritum |
| Formal vs informal | Sie (capital) vs du; err toward Sie with strangers |
| Compound words | Work backwards from last element for meaning + gender |
| Neighbor languages | Dutch is ~60% cognate. English has ~40% Germanic cognates. |

---

## Common Confusion Points

**"V2 doesn't mean verb is the second word"**
V2 means the verb is the second *constituent* (chunk, phrase).
"Den ganzen Tag" (all day) counts as ONE unit in position 1.
"Den ganzen Tag habe ich gearbeitet." — "habe" is still V2.

**"Perfekt vs Präteritum"**
Spoken German uses Perfekt for past events. Präteritum is for writing
and telling stories. The exception: sein/haben/modals use Präteritum
even in speech ("ich war" not "ich bin gewesen" for conversational past).

**"Sein vs haben in Perfekt"**
Verbs of movement/change of state use sein: ich bin gegangen, ich bin aufgewacht.
Most other verbs use haben: ich habe gesehen, ich habe gegessen.
Bleiben (to stay) uses sein: ich bin geblieben.

**"Das Mädchen — neuter girl?"**
Grammatical gender ≠ natural gender. Diminutive -chen/-lein → always neuter.
Das Mädchen (the girl) is grammatically neuter. Sie/ihr still used in
natural contexts; strict grammar allows es. Don't overthink it.

**"German ß (Eszett)"**
ß = double s after long vowels/diphthongs. After reform (1996):
  Short vowel + ss: dass, muss, Fluss
  Long vowel + ß: Straße, groß, Maß
  ß is only lowercase; uppercase = SS.
  Austria/Switzerland: ss used everywhere instead.
