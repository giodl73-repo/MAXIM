# Semiotics — Landscape and Taxonomy

## The Big Picture

Semiotics is the study of signs and sign systems — how meaning is produced, transmitted, and interpreted. It is broader than linguistics: any systematic process of meaning-making is semiotic. This includes visual design, architecture, film, music, ritual, and — crucially — programming languages, APIs, and user interfaces.

```
+-----------------------------------------------------------------------+
|                        SEMIOTICS MAP                                  |
|                                                                       |
|  SAUSSUREAN TRADITION              PEIRCEAN TRADITION                 |
|  (European, linguistics-based)     (American, logic-based)            |
|                                                                       |
|  Sign = Signifier + Signified      Sign = Representamen + Object      |
|  (binary, synchronic, arbitrary)   + Interpretant (triadic, typed)    |
|                                                                       |
|  Led to:                           Led to:                            |
|  Structuralism                     Pragmatism                         |
|  Post-structuralism                Formal semiotics                   |
|  Barthes, Lévi-Strauss, Lacan      Morris: syntax/semantics/pragmatics|
|                                    (the triad CS inherited)           |
|                                                                       |
|  +-----------------------------+  +------------------------------+    |
|  | STRUCTURAL BRANCH           |  | LOGICAL BRANCH               |    |
|  | codes, oppositions,         |  | sign types, abduction,       |    |
|  | paradigm/syntagm, myth      |  | icon/index/symbol            |    |
|  +-----------------------------+  +------------------------------+    |
|                    \                          /                       |
|                     \                        /                        |
|                      +--------------------+                           |
|                      | CULTURAL SEMIOTICS |                           |
|                      | Lotman, semiosphere|                           |
|                      | Eco: sign production|                          |
|                      +--------------------+                           |
+-----------------------------------------------------------------------+
```

---

## The Sign: Three Competing Definitions

These are NOT the same and are often conflated:

```
+-----------------------------------------------------------------------+
|  SAUSSURE (1916)        PEIRCE (~1900)          OGDEN & RICHARDS      |
|                                                  (1923)               |
|  Sign = dyad:           Sign = triad:            Semiotic triangle:   |
|  [Signifier/Signified]  Representamen →          symbol → thought/    |
|                         Object                   reference → referent |
|  Signifier =            via Interpretant                              |
|  acoustic image                                  No direct line from  |
|  (sound-form)           R: Representamen         symbol to referent!  |
|                         O: Object                (mediated by thought) |
|  Signified =            I: Interpretant                               |
|  concept / content      (sign for the sign;                           |
|                          can trigger further                          |
|  Relation: ARBITRARY    semiosis)                                     |
|  (conventional,                                                       |
|  not natural)           Relation: TYPED                               |
|                         icon / index / symbol                         |
+-----------------------------------------------------------------------+
```

---

## Peirce's Sign Typology

Peirce's most analytically useful contribution: three types of sign relation.

```
  ICON              INDEX               SYMBOL
  ----              -----               ------
  Resemblance       Causal or           Arbitrary
  to object         existential         convention
                    contiguity

  Photograph        Smoke → fire        Word "dog"
  Map               Footprint → person  Red = stop
  Onomatopoeia      Pointing finger     National flag
  Diagram           Fever → disease     Mathematical notation
  Portrait          Fingerprint         Programming keywords

  "looks like"      "connected to"      "we agreed
                    (physically)        this means"

  Most signs are MIXED:
  A thermometer: iconic (scale resembles temperature)
                 + indexical (causally connected to temp)
                 + symbolic (scale/units are conventions)
```

---

## Saussure's Key Concepts

```
  THE LINGUISTIC SIGN
  +------------------------------------------+
  |  SIGNIFIER ←—(arbitrary bond)—→ SIGNIFIED |
  |  (acoustic image / written form)          |
  |  "arbre" [arbr]                           |
  |                   mental concept of tree  |
  +------------------------------------------+

  Three foundational principles:

  1. ARBITRARINESS
     No natural link between form and content.
     "tree" (English) / "arbre" (French) / "Baum" (German)
     All pick out the same concept. Different sounds.
     Exception (apparent): onomatopoeia — but these vary
     by language ("cock-a-doodle-doo" vs "kikeriki" vs "cocorico")

  2. DIFFERENCE
     Signs have value only through opposition to other signs.
     "cat" means what it does partly because it ≠ "bat", "cut", "can".
     Meaning is RELATIONAL, not intrinsic.

  3. TWO STRUCTURAL AXES
     PARADIGMATIC (vertical): substitution class
       "The cat sat on the ___"
       {mat, roof, stool, chair} — equivalent positions, choose one

     SYNTAGMATIC (horizontal): combination rules
       "The cat sat on the mat" — sequence, grammar, co-occurrence
```

---

## Denotation / Connotation / Myth (Barthes' Layers)

```
  FIRST ORDER — DENOTATION
  +---------------------------+
  |  Signifier  |  Signified  |   "rose" (word) → rose (flower)
  +---------------------------+   Photo of steak → steak (food)
           |
           | whole first-order sign becomes a new Signifier
           v
  SECOND ORDER — CONNOTATION / MYTH
  +---------------------------+
  |  Sign₁     |  New         |   rose → ROMANCE / PASSION
  |  (first    |  Signified   |   steak → FRENCHNESS (Barthes)
  |  order)    |  (cultural,  |   white coat → MEDICAL AUTHORITY
  |            |  ideological)|   cowboy → AMERICAN FREEDOM
  +---------------------------+

  MYTH (Barthes): operates at second order.
  Takes historically contingent connotations and
  presents them as NATURAL and INEVITABLE.
  "This is just how things are."
  = ideology rendering contingency as necessity.
```

---

## Historical Arc

```
1916  Saussure: Course in General Linguistics (posthumous)
       Sign/signifier/signified, arbitrariness, synchrony
       |
~1900  Peirce: Collected Papers (published 1931-58)
       Triadic sign, icon/index/symbol, abduction, semiosis
       |
1928   Prague School: Jakobson, Mukařovský, Trubetzkoy
       Phonology as opposition, functions of language, markedness
       |
1949   Shannon: information theory — sign without meaning
       (but the vocabulary of "signal" and "code" transfers)
       |
1955   Lévi-Strauss: structural anthropology
       Myth = binary opposition worked through narrative
       |
1957   Barthes: Mythologies — ideology as naturalized second-order sign
       |
1966   High structuralism: Barthes, Lacan, Althusser, Foucault
       |
1967   Derrida: Of Grammatology — différance, critique of presence
       Deconstruction attacks the privileging of speech over writing
       |
1972   Greimas: structural narrative semantics, actantial model
       |
1976   Eco: A Theory of Semiotics — encyclopedic model, unlimited semiosis
       |
1984   Lotman: Universe of the Mind — semiosphere
       Cultural space as organized sign system, the boundary
       |
1990s  Visual semiotics (Kress & van Leeuwen), film semiotics (Metz)
       |
2000s  Computational semiotics, code as sign system
       Interface design as semiotic system
```

---

## Jakobson's Six Functions of Language

Essential framework: every communicative act orients toward one of six factors, activating a different function.

```
  +---------------------+
  |      CONTEXT        |   → REFERENTIAL function
  |  (what the message  |     (pointing to the world; informational)
  |    is about)        |
  +---------------------+
           |
  SENDER ——————→ MESSAGE ——————→ RECEIVER
  (EMOTIVE      (POETIC          (CONATIVE
  function:     function:        function:
  expresses     focused on       oriented
  speaker's     form of          toward
  state)        message itself)  addressee;
                                 commands,
                                 appeals)
           |
  +---------------------+
  |       CONTACT        |   → PHATIC function
  |   (channel/medium)   |     (maintaining contact: "Hello?",
  +---------------------+      "You know what I mean?")

  +---------------------+
  |       CODE           |   → METALINGUAL function
  |  (shared language)   |     (talking about the code itself:
  +---------------------+      "What do you mean by X?")
```

---

## Module Map

| File | Topic | Key Concepts |
|------|-------|-------------|
| 01-SAUSSURE.md | Sign, signifier, signified | Arbitrariness, difference, synchrony, paradigm/syntagm |
| 02-PEIRCE.md | Icon, index, symbol | Triadic sign, abduction, semiosis, interpretant |
| 03-STRUCTURALISM.md | Prague School, code, opposition | Jakobson functions, binary oppositions, markedness |
| 04-BARTHES.md | Myth, connotation, cultural sign | Mythologies, second-order systems, ideology |
| 05-POST-STRUCTURALISM.md | Derrida, deconstruction | Différance, trace, logocentrism, aporia |
| 06-NARRATIVE-SEMIOTICS.md | Greimas, Propp | Actantial model, narrative grammar, morphology |
| 07-VISUAL-SEMIOTICS.md | Visual and film semiotics | Metz, Kress & van Leeuwen, codes, grammar of visual design |
| 08-CULTURAL-SEMIOTICS.md | Lotman, semiosphere | Cultural space, boundary, modeling systems |
| 09-APPLICATIONS.md | Advertising, architecture, code | Applied semiotics across media |

---

## Decision Cheat Sheet

| Question | Answer | See |
|----------|--------|-----|
| Is the link between word and meaning arbitrary? | Yes — conventional all the way down (Saussure) | 01-SAUSSURE.md |
| How do signs relate to their objects? | Icon (resemble), index (causal/contiguous), symbol (arbitrary) | 02-PEIRCE.md |
| How does advertising produce ideology? | Naturalizing second-order connotations as denotation | 04-BARTHES.md |
| What is deconstruction? | Showing how texts destabilize their own binary oppositions | 05-POST-STRUCTURALISM.md |
| What structure underlies all narratives? | Actants and actantial roles (Greimas) | 06-NARRATIVE-SEMIOTICS.md |
| Is code a sign system? | Yes — programming syntax and semantics are both semiotic | 09-APPLICATIONS.md |
| What is Jakobson's contribution? | Six functions orienting communication toward context/sender/message/receiver/contact/code | 03-STRUCTURALISM.md |

---

## Common Confusion Points

**Saussure vs Peirce**: Developed independently; incompatible frameworks. Saussure's sign is binary (signifier/signified). Peirce's is triadic (representamen/object/interpretant). Most French literary and cultural theory is Saussurean. American and logical semiotics is Peircean. Do not conflate them.

**Signifier ≠ the physical sound**: The signifier is the acoustic image — a mental entity, not physical sound waves. Saussure is studying psychology and social convention, not phonetics.

**Arbitrariness ≠ randomness**: The link is conventional (not motivated by resemblance or causation), but once established it binds. You cannot unilaterally change what "cat" means. Arbitrariness is about the origin of the link, not its stability.

**Post-structuralism ≠ nihilism about meaning**: Derrida does not say meaning is impossible. He says it is never fully present, always deferred and differed (différance). Texts mean — they over-determine, contradict, and unsettle their own binary foundations.

**Semiotics vs semantics**: Semantics (in linguistics/logic) studies sentence meaning and truth conditions. Semiotics is broader — any sign system, including non-linguistic ones (images, gestures, architecture, traffic, dress codes).

**Morris's triad (syntax/semantics/pragmatics) = Peircean, not Saussurean**: Charles Morris adapted Peirce into this three-way distinction. When programming language theorists speak of "syntax vs semantics vs pragmatics," they are operating in a Peircean lineage.
