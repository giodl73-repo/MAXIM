# Spanish — Language Reference

## Profile at a Glance

```
+--------------------------------------------------------------------+
| SPANISH (Español)                                                  |
+--------------------------------------------------------------------+
| Family:      Indo-European → Romance → Ibero-Romance              |
| Native spkrs: ~475M (2nd most by native speakers)                 |
| Total spkrs:  ~600M (L1+L2)                                       |
| Countries:   20 countries official language                        |
| Word order:  SVO (flexible with pro-drop)                         |
| Morphology:  Fusional (inflectional)                              |
| Tonal:       No                                                    |
| Gender:      Binary (masculine/feminine)                           |
| Script:      Latin                                                 |
| Cases:       None (prepositions carry case meaning)               |
| FSI level:   Category I — ~600-750 hours                          |
+--------------------------------------------------------------------+
```

---

<!-- @editor[bridge/P3]: Natural bridge to formal language theory missing — learner knows automata/formal grammars from MIT; a note connecting fusional morphology to the concept of "paradigm as finite-state table" would resonate -->
## The Big Picture: Grammar System

```
SPANISH GRAMMAR ARCHITECTURE
==============================

  NOUNS                    VERBS                      PRONOUNS
  ------                   -----                      --------
  All have gender          3 infinitive classes       Subject often dropped
  (M/F)                    -AR, -ER, -IR              (pro-drop language)
       |                        |                            |
       v                        v                            v
  Articles agree           6-person paradigm          Tú (informal)
  el/la (sing)             yo/tú/él/                  Usted (formal)
  los/las (plur)           nosotros/                  Vosotros (Spain only)
                           vosotros/ellos              Ustedes (LatAm formal+informal)
       |                        |
       v                        v
  Adjectives agree         TENSE SYSTEM
  (gender + number)             |
  hombre alto (m)          +---------+--------+--------+
  mujer alta (f)           |INDICATIVE|SUBJUNC |IMPERATIVE|
  hombres altos            +---------+--------+--------+
  mujeres altas            Present   Present  Commands
                           Preterite Imperfect
                           Imperfect Past Perf
                           Future    Future
                           Cond      Cond
                           Perf      +pluperfect
                           Pluperf
```

---

## Sound System

```
SPANISH PHONOLOGY — KEY POINTS
================================

VOWELS: Pure, consistent — 5 vowels ONLY (a,e,i,o,u)
  No diphthongs that change quality. "a" is always [a], never like English "cat".
  This is why Spanish is easy to pronounce — no schwa vowel.

CONSONANTS — differences from English:
+----------+------------------+-------------------------------------+
| Letter   | Spanish sound    | Trap for English speakers           |
+----------+------------------+-------------------------------------+
| R        | tapped [ɾ] (single)| "pero" - single tap (like "butter")|
| RR       | trilled [r]      | "perro" - true trill                |
| LL       | [j] or [ʎ]       | "llamar" = "yamar" (mostly)         |
| Y        | [j] (consonant)  | "yo" = "jo" (in Argentina = "sho") |
| Ñ        | [nj]/[ɲ]         | "mañana" ≠ "manana"                |
| H        | SILENT           | "hola" = "ola"                     |
| V        | Same as B        | "vino" and "bino" sound identical   |
| C before E/I| [θ] Spain; [s] LatAm | "cielo" = "thyelo" vs "syelo" |
| Z        | [θ] Spain; [s] LatAm | "cerveza" distinction            |
| J / G+E/I| [x] velar fric   | "jardín" = guttural h              |
| QUE/QUI  | [ke]/[ki]        | U is silent: "quiero" = "kyero"    |
+----------+------------------+-------------------------------------+

STRESS RULES (regular):
  Default: stress on second-to-last syllable
  Words ending in consonant (not N/S): stress on last syllable
  Accent marks override: están (last syllable), árbol (first)
```

---

## Grammar Core

### Nouns and Articles

```
GENDER SYSTEM
==============
  Masculine: el, los, un, unos
  Feminine:  la, las, una, unas

  Predictors (not rules):
    -o ending → usually M (el libro, el perro)
    -a ending → usually F (la casa, la mesa)
    EXCEPTIONS: el día (m), la mano (f), el problema (m), el tema (m)
    Words from Greek -ma/-pa: el programa, el poema, el clima → masculine

  PLURALS:
    Vowel ending:   add -s  (casa → casas, libro → libros)
    Consonant end:  add -es (ciudad → ciudades, árbol → árboles)
    -z ending:      -z→-ces (vez → veces, voz → voces)
```

### Verb Conjugation — The Core System

```
THREE INFINITIVE CLASSES
==========================
   -AR (hablar)    -ER (comer)    -IR (vivir)

PRESENT INDICATIVE:
+-----------+-----------+----------+-----------+
| Person    | -AR       | -ER      | -IR       |
+-----------+-----------+----------+-----------+
| yo        | habl-o    | com-o    | viv-o     |
| tú        | habl-as   | com-es   | viv-es    |
| él/ella   | habl-a    | com-e    | viv-e     |
| nosotros  | habl-amos | com-emos | viv-imos  |
| vosotros  | habl-áis  | com-éis  | viv-ís    |
| ellos     | habl-an   | com-en   | viv-en    |
+-----------+-----------+----------+-----------+

PRETERITE (completed past):
+-----------+-----------+----------+-----------+
| yo        | habl-é    | com-í    | viv-í     |
| tú        | habl-aste | com-iste | viv-iste  |
| él/ella   | habl-ó    | com-ió   | viv-ió    |
| nosotros  | habl-amos | com-imos | viv-imos  |
| vosotros  | habl-asteis|com-isteis|viv-isteis|
| ellos     | habl-aron | com-ieron| viv-ieron |
+-----------+-----------+----------+-----------+

IMPERFECT (ongoing/habitual past):
+-----------+-----------+----------+
| yo        | habl-aba  | com-ía   |
| tú        | habl-abas | com-ías  |
| él/ella   | habl-aba  | com-ía   |
| nosotros  | habl-ábamos| com-íamos|
| ellos     | habl-aban | com-ían  |
+-----------+-----------+----------+

FUTURE (formed from infinitive + endings):
  hablar + é = hablaré, hablarás, hablará, hablaremos, hablaréis, hablarán
  Irregular futures: tener→tendr-, poder→podr-, saber→sabr-, venir→vendr-

CONDITIONAL (from infinitive + endings):
  hablaría, hablarías, hablaría, hablaríamos, hablaríais, hablarían
```

### The SER vs ESTAR Distinction

```
SER vs ESTAR — Both mean "to be"
==================================

SER (permanent/defining characteristics)          ESTAR (temporary states/location)
-------------------------------------------        ---------------------------------
  Identity:     Soy médico. (I am a doctor.)         Location: Estoy en Madrid.
  Origin:       Soy de España.                        State:    Estoy cansado.
  Material:     Es de metal.                          Emotion:  Estoy feliz.
  Relationship: Ella es mi hermana.                   Result:   La puerta está abierta.
  Time:         Son las tres.                         Progressive: Estoy comiendo.
  Passive voice: El libro fue escrito.

TRICK: Adjectives change meaning with ser vs estar:
  aburrido: Es aburrido = he is boring (personality)
             Está aburrido = he is bored (state)
  listo:    Es listo = he is clever
             Está listo = he is ready
  malo:     Es malo = he is evil
             Está malo = he is sick
  bueno:    Es bueno = he is good (moral)
             Está bueno = it tastes good
```

### Preterite vs Imperfect

```
PRETERITE vs IMPERFECT
========================

PRETERITE                          IMPERFECT
---------                          ---------
Completed action                   Ongoing / habitual past
Clear beginning & end              No defined endpoint
Interrupting action                Background action
Sequence of events                 "Used to" / "was __ing"

Ayer comí una pizza.               De niño, comía pizza todos los viernes.
(Yesterday I ate a pizza.)         (As a child, I used to eat pizza every Friday.)

Cuando llegó Juan, yo dormía.      → llegó = preterite (event)
(When Juan arrived, I was sleeping.)→ dormía = imperfect (background)
```

### Subjunctive — The Core Triggers

```
SUBJUNCTIVE TRIGGERS
=====================
Spanish subjunctive required when:

1. Desire/want/prefer (different subject):
   Quiero que tú vengas. (I want you to come.)
   Compare: Quiero venir. (same subject — no subjunctive)

2. Doubt/negation of knowledge:
   No creo que sea verdad. (I don't believe it's true.)
   Dudo que venga. (I doubt he'll come.)

3. Emotion:
   Me alegra que estés aquí. (I'm glad you're here.)

4. Impersonal expressions:
   Es importante que estudies. (It's important that you study.)

5. Adverbial clauses with:
   para que, antes de que, a menos que, aunque (sometimes), cuando (future)
   Llámame cuando llegues. (Call me when you arrive — future event)
   Compare: Llámame cuando llegas. (= Call me when you arrive — habitual)
```

### Reflexive Verbs

```
REFLEXIVE VERBS (verbos reflexivos/pronominales)
=================================================
Subject acts on itself:
  levantarse — to get up (lit: to raise oneself)
  Me levanto a las siete. (I get up at 7.)

Many verbs change meaning when reflexive:
  ir (to go) → irse (to leave/go away)
  dormir (to sleep) → dormirse (to fall asleep)
  poner (to put) → ponerse (to put on [clothing]; to become)

Reflexive pronouns: me, te, se, nos, os, se
Position: before conjugated verb or attached to infinitive/gerund
  Me voy. / Voy a irme. / Estoy yéndome.
```

---

## Regional Variation: Spain vs Latin America

```
+---------------------------+---------------------+---------------------+
| Feature                   | Spain               | Latin America       |
+---------------------------+---------------------+---------------------+
| 2nd person plural (inform)| vosotros (coméis)   | ustedes (comen)     |
| C/Z pronunciation         | [θ] "thin"          | [s] "see"           |
| LL/Y pronunciation        | [ʎ] or [j]          | [j] (mostly)        |
|                           | (yeísmo spreading)  |                     |
| "Vos" pronoun             | Not used            | Argentina/Uruguay/  |
|                           |                     | C.America — replaces|
|                           |                     | tú with own endings |
| Vocabulary                | coche (car),        | carro, computador,  |
|                           | ordenador, piso     | apartamento...      |
| Leísmo (le for lo)        | Common in Spain     | Less common         |
+---------------------------+---------------------+---------------------+
```

---

## 50 Essential Phrases / Vocabulary

```
SURVIVAL SPANISH
==================
Hola / Buenos días / Buenas tardes / Buenas noches
Adiós / Hasta luego / Hasta mañana / Chao
Por favor / Gracias / De nada / Con mucho gusto
Sí / No / Quizás / A veces
Perdón / Lo siento / Disculpe
¿Cómo estás? (informal) / ¿Cómo está usted? (formal)
Bien, gracias. / Regular. / Mal.
¿Cuál es tu nombre? / Me llamo ___
¿De dónde eres? / Soy de ___
¿Cuánto cuesta? / ¿Cuánto es? / Es caro. / Es barato.
¿Dónde está ___? / Aquí / Allí / A la derecha / A la izquierda
¿Habla inglés? / No hablo español bien.
No entiendo. / ¿Puede repetir? / Más despacio, por favor.
¡Ayuda! / ¡Socorro! / ¡Llame a la policía! / ¡Llame a una ambulancia!
Quiero ___ / Necesito ___
¿Tiene ___? / No hay ___ / Hay ___
Una mesa para dos / La cuenta, por favor
¿Dónde está el baño? / El aeropuerto / El hotel / El hospital
Quiero un billete a ___
¿A qué hora sale? / ¿A qué hora llega?
```

---

## Key Irregular Verbs (the unavoidable ones)

```
+--------+--------+--------+--------+--------+
| Verb   | SER    | ESTAR  | TENER  | IR     |
+--------+--------+--------+--------+--------+
| yo     | soy    | estoy  | tengo  | voy    |
| tú     | eres   | estás  | tienes | vas    |
| él     | es     | está   | tiene  | va     |
| nos    | somos  | estamos| tenemos| vamos  |
| ellos  | son    | están  | tienen | van    |
+--------+--------+--------+--------+--------+
| Verb   | PODER  | QUERER | SABER  | HABER  |
+--------+--------+--------+--------+--------+
| yo     | puedo  | quiero | sé     | he     |
| tú     | puedes | quieres| sabes  | has    |
| él     | puede  | quiere | sabe   | ha     |
| nos    | podemos|queremos| sabemos| hemos  |
| ellos  | pueden | quieren| saben  | han    |
+--------+--------+--------+--------+--------+
```

---

## Decision Cheat Sheet

| I want to... | What to focus on |
|---|---|
| Start speaking immediately | Present tense of regular -AR verbs + ser/estar |
| Discuss the past | Preterite vs imperfect distinction |
| Express opinions/wishes | Subjunctive present tense |
| Read any Spanish text | Silent H, C/Z variants, accent marks as stress guides |
| Sound less foreign | Rolled R practice, pure vowels, final -s is sibilant |
| Understand LatAm vs Spain | Vosotros vs ustedes, seseo vs distinción |
| Move to Portuguese | Only 11% divergence — massive free transfer |

---

## Common Confusion Points

**"Ser vs estar" — permanent vs temporary is a myth**
The real distinction: ser = intrinsic/defining identity, estar = state/condition.
"Está muerto" (he is dead) — death is permanent but it's a state.
"Es eterno" (he is eternal) — temporal concept but identity.

**"Preterite vs imperfect" — not just completed vs not**
Preterite frames an event as a discrete unit. Imperfect presents it as
ongoing background or habitual. "Trabajé ayer" (I worked yesterday — event).
"Trabajaba mucho" (I used to work a lot / I was working a lot).

**"Direct vs indirect object pronouns"**
me, te, le/lo/la, nos, os, les/los/las
le/les = indirect (to him/her/them) — often doubled: "Le di el libro a Juan"
In Spain, "leísmo": le/les used for masculine direct objects too.

**"Personal a"**
Direct object animate nouns require "a":
"Veo a María" (I see Maria) vs "Veo el libro" (I see the book).

**"Mismo subject, no subjunctive"**
"Quiero venir" (I want to come) — no subjunctive (same subject).
"Quiero que tú vengas" (I want you to come) — subjunctive (different subject).
