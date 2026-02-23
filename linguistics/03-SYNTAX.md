# Syntax — Sentence Structure

## The Big Picture

Syntax is the study of how words combine into phrases, clauses, and sentences — and how grammatical structure determines interpretation.

```
+------------------------------------------------------------------+
|                    SYNTAX LANDSCAPE                               |
|                                                                  |
|  PHRASE STRUCTURE              TRANSFORMATIONS                   |
|  (what hierarchical            (how structures                   |
|   structure sentences have)    are derived from base)           |
|  X-bar theory, CFGs            Movement operations,              |
|  constituency tests            traces, copies                    |
|                                                                  |
|  BINDING THEORY                WORD ORDER                        |
|  (how NPs refer and            (universals + parameters          |
|   corefer — reflexives,        SOV/SVO/VSO/OVS/OVS/VOS)        |
|   pronouns, R-expressions)                                       |
|                                                                  |
|  FROM GENERATIVE GRAMMAR:                                        |
|  Government and Binding (GB) → Minimalist Program (MP)          |
|  Core operation: MERGE builds hierarchical structure             |
+------------------------------------------------------------------+
```

---

## Part I: Constituency and Phrase Structure

### Constituency Tests

How do we know what groups into constituents?

**1. Substitution**: Replace a sequence with a single pronoun/pro-form:
```
[The old man] saw [a ghost] yesterday.
He/She/They saw one/it yesterday.
→ "the old man" and "a ghost" are constituents (NPs)
→ "old man saw" is NOT a constituent (can't substitute with single proform)
```

**2. Movement**: Constituents can be fronted/moved together:
```
[A ghost], the old man saw yesterday.  ✓ (topic fronting)
[Yesterday], the old man saw a ghost.  ✓ (adverb front)
*[Man saw], the old a ghost yesterday. ✗ (not a constituent)
```

**3. Do-so substitution**: Replace a VP:
```
John [[saw a ghost] yesterday] and Mary did so too.
→ "saw a ghost yesterday" is a VP constituent
```

**4. Cleft/pseudo-cleft**:
```
It was [a ghost] that the old man saw. ✓ → NP constituent
What the old man saw was [a ghost]. ✓ → NP constituent
*It was [old man saw] that the the yesterday. ✗ → not constituent
```

### Context-Free Grammar — The TCS Bridge

Syntactic phrase structure rules are exactly CFG productions:

```
PHRASE STRUCTURE RULES (early Chomsky 1957):

  S  → NP VP
  NP → (Det) (Adj)* N (PP)*
  VP → V (NP) (PP)* (AdvP)*
  PP → P NP
  AP → (AdvP) A

These are CFG productions: A → α, where α ∈ (V ∪ T)*

Parse tree for "The cat saw a mouse":
            S
           / \
         NP   VP
        /  \  / \
      Det   N V  NP
      |     |  | / \
     The   cat saw Det N
                   |   |
                   a  mouse
```

The pushdown automaton (PDA) perspective: recursive embedding requires a stack, which is why finite-state automata fail for syntax. "The rat the cat the dog chased killed ate the malt" — legal but requires tracking nested subject-verb pairs.

**But natural language is not quite CFG:**
- Cross-serial dependencies in Swiss German subordinate clauses require indexed grammars (beyond CFG)
- TAG (Tree-Adjoining Grammar) and CCG (Combinatory Categorial Grammar) are mildly context-sensitive, covering these cases

---

## Part II: X-bar Theory

Bare phrase structure rules (above) are too unconstrained. X-bar theory imposes universal structure:

```
X-BAR SCHEMA:

       XP  (maximal projection)
      /  \
  (Spec)  X'  (X-bar)
         / \
      X    (Complement)
    (head)

X can be: N, V, A, P, I (Inflection), C (Complementizer)

Rules:
  XP  → (Spec) X'
  X'  → X (Complement)
  X'  → X' (Adjunct)   [adjuncts attach to X', creating multiple X' levels]
```

### Full NP Structure

```
NP: "all the very big red books about syntax"

         NP (DP in more recent analysis)
        /  \
    (all)   N'
           /   \
        Det     N'
        (the)  /   \
            AdjP    N'
           /   \   /   \
         AdvP  Adj N'    PP
         (very)(big) |   |
                    Adj  N   (about syntax)
                   (red)(books)
```

### Verb Phrase Structure

```
VP: "quietly gave her a book yesterday"

         VP
        / \
      AdvP  V'
     (quietly) |
               V'
              / \
             V   NP       (indirect object)
           (gave)(her)
                  |
                  V'
                 / \
                V   NP     (direct object)
               (t)  (a book)
                       \
                       PP
                    (yesterday)

[Modern analysis: ditransitives have two VP shells — "little v" theory]
```

---

## Part III: The DP Hypothesis

```
Classical analysis:          Modern DP analysis:
    NP                           DP
   / \                          / \
 Det  N'                       D   NP
 the  |                       the  |
      N                            N
    book                          book

The determiner, not the noun, is the head.
Evidence: languages without articles use pronouns in Det position.
John's book = [DP [D' [D John's] [NP book]]]
```

---

## Part IV: Transformations — Movement

**The basic insight**: Surface word order ≠ underlying structure. Some structures are derived by movement operations.

### Wh-Movement

```
Underlying: You saw what yesterday?
Surface:    What did you see ___ yesterday?

"What" has moved from its base position (object of "see") to SpecCP.
The base position is marked by a TRACE t (or COPY in Minimalism):

         CP
        / \
     What_i  C'
            / \
           C   IP
          did  / \
              NP  I'
             you  / \
                 I   VP
                past  |
                      V'
                     / \
                    V   NP
                  see  [t_i]  ← trace / copy of "what"
```

**Islands**: Certain structures block movement:

```
Complex NP Island:
  I met [NP the woman [CP who bought it]].
  *What did you meet [NP the woman [CP who bought ___]]?
  ✗ — can't extract from within a complex NP

Wh-Island:
  I wonder [CP who bought what].
  *What do you wonder [CP who bought ___]?
  ✗ — can't extract from embedded wh-question
```

These island constraints are remarkably cross-linguistic — supporting UG claims.

### Passivization

```
Active:  John   saw    Mary.
         NP_subj V     NP_obj

Passive: Mary  was seen (by John).
         NP_subj  pass    (PP)

Structural description:
  NP_i was [VP V+en t_i]  (NP moved from VP-internal position to subject)
```

**Passive isn't just stylistic** — it changes what's available for binding:

```
John_i saw himself_i. ✓
*Himself_i was seen by John_i. ✗ (or marginal — binding from demoted subject different)
```

### Raising vs. Control

A classic diagnostic for abstract structure:

```
RAISING:
  John seems [to be sick].

  "John" is base-generated as subject of "be sick" and RAISED to matrix subject.
  Evidence: "There seems to be a problem." — "there" is expletive, not agent of "seems"
  John seems → John is raised, leaving expletive possible

CONTROL:
  John wants [PRO to leave].

  "John" is matrix subject and CO-REFERS with PRO (controlled null subject).
  Evidence: "There wants *(John) to be a problem." — can't put expletive in controller position
```

---

## Part V: Binding Theory

**Government and Binding (GB)** includes three conditions governing NP interpretation:

```
BINDING THEORY (simplified):

CONDITION A: Anaphors (reflexives, reciprocals) must be bound in their binding domain.
  John_i saw himself_i.        ✓ (anaphor bound by local c-commanding NP)
  *John_i thinks that Mary saw himself_i.  ✗ (anaphor not bound locally)
  John_i and Mary_j saw each other_{i,j}.  ✓

CONDITION B: Pronouns must be free in their binding domain.
  John_i saw him_{j≠i}.        ✓ (pronoun free in domain — refers to someone else)
  *John_i saw him_i.           ✗ (pronoun can't be bound locally — use reflexive)
  John_i thinks that Mary saw him_i.  ✓ (pronoun free in its local domain — OK from higher)

CONDITION C: R-expressions (names, full NPs) must be free everywhere.
  He_i said that John_i left.  ✗ (R-expression "John" can't be co-indexed with c-commanding "he")
  He_i said that John_j left.  ✓ (different indices — John is someone else)
```

**C-command** (the key structural notion):

```
A C-COMMANDS B iff:
  A does not dominate B, and
  every node dominating A also dominates B.

       IP
      / \
    NP_A  VP
    John  / \
         V   NP_B
        saw  him

  John c-commands him (every node dominating John — IP — also dominates him)
  him does NOT c-command John (VP dominates him but not John)
```

---

## Part VI: Government and Binding → Minimalism

The history of Chomsky's syntax in brief:

```
GENERATIVE EVOLUTION:
  Syntactic Structures (1957)    — phrase structure + transformations
  Aspects (1965)                 — deep structure / surface structure, sub-categorization
  Government and Binding (1981)  — Principles and Parameters framework,
                                   modularity: X-bar, Theta, Case, Binding, Bounding, Control
  Minimalist Program (1995→)     — reduce to absolute minimum
                                   Single operation: MERGE
                                   Economy: shortest derivation wins
                                   Interface conditions: PF and LF
```

### Minimalist Merge

```
MERGE: takes two syntactic objects α and β, creates {α, β}

INTERNAL MERGE = movement (merge with already-present element)
EXTERNAL MERGE = combine two new elements

Structure building is bottom-up:
  1. Select: saw, a, mouse
  2. Merge(saw, a) → {V, D} ← nope, Merge(a, mouse) first
  3. Merge(a, mouse) → DP: {D, N} = [DP a mouse]
  4. Merge(saw, [DP a mouse]) → VP: {V, DP}
  5. Merge([NP the cat], VP) → IP: {NP, VP}
  ...continue until CP

INTERNAL MERGE for questions:
  [CP What_i [IP did [VP you [V' see [DP t_i]]]]]
  "what" is internally merged to SpecCP from its base DP position
```

**Economy principles:**
- Procrastinate: delay movement as long as possible
- Greed (Earliness): move only when you must (for feature checking)
- Fewest Steps

---

## Part VII: Word Order Universals

### Greenberg's Universals (1963)

After surveying 30 languages, Greenberg found:

```
BASIC WORD ORDER FREQUENCIES:
  SOV  — subject, object, verb       ~41%  (Japanese, Turkish, Hindi, Latin, Korean)
  SVO  — subject, verb, object       ~35%  (English, Mandarin, French, Swahili)
  VSO  — verb, subject, object       ~9%   (Classical Arabic, Irish, Welsh)
  OVS  — object, verb, subject       ~3%   (Hixkaryana)
  OVS  — (same)
  VOS  — rare (Malagasy)
  Free — Russian, Finnish (case-marked → order expressive)
```

**Greenberg's implicational universals (selected):**

| Number | Universal |
|--------|-----------|
| 1 | VSO languages always have prepositions |
| 4 | SOV languages always have postpositions |
| 2 | Preposition languages are SVO or VSO |
| 12 | If subject follows verb, then object also follows verb (SOV rare in VSO) |
| 18 | Suffixing languages are more common than prefixing |
| 25 | If a language has plural, it has singular |
| 38 | If a language has case, there are at least 2 |

### Head-Directionality Parameter

```
HEAD-INITIAL (VP has V before complement):
  English: [VP see [NP the cat]]     V NP
  French:  [VP voir le chat]
  Predicts: prepositions (P NP), complementizer before S, relative clause after N

HEAD-FINAL (VP has V after complement):
  Japanese: [VP [NP neko-wo] mi-ru]   NP V
  Turkish:  [VP [NP kedi-yi] gör-mek]
  Predicts: postpositions, complementizer after S, relative clause before N

One parameter (head-initial/final) predicts many correlations.
```

---

## Part VIII: Binding Theory Summary + Interaction with Movement

```
ANAPHOR BINDING — must be local:
  [IP John_i [VP saw [NP himself_i]]]  ✓ (himself c-commanded by John in same IP)

CROSSING COREFERENCE — Principle C violation:
  [CP [DP Which picture of him_i] did John_i like]
  "him" is an R-expression relative to John? No — "him" is a pronoun.
  Actually: [CP [DP Which picture of him_i]_k did John_j like t_k]?
  Now: does John c-command him? After movement, trace position — complex.

WEAK CROSSOVER:
  *[CP What_i does his_i mother love?]
  "his" tries to corefer with moved "what" — fails.
  Compare: [CP Who_i loves his_i mother?] ✓ (forward binding, no movement crossing)
```

---

## Decision Cheat Sheet

| Construction | Analysis | Key operation |
|-------------|----------|---------------|
| "What did you see?" | Wh-movement | Internal Merge to SpecCP |
| "The cat seems to be sick" | Raising | NP moves from embedded to matrix Spec-IP |
| "John wants to leave" | Control | PRO controlled by matrix subject |
| "John saw himself" | Condition A | Anaphor locally bound |
| "John saw him" (different person) | Condition B | Pronoun free in domain |
| "He said John left" (≠ coreference) | Condition C | R-expression must be free everywhere |
| Verb-final in Japanese | Head-final parameter | Head follows complement |
| Cross-serial dependency in Swiss German | Beyond CFG | Indexed grammar / TAG |

---

## Common Confusion Points

**Deep structure ≠ semantic representation:**
In GB, deep structure (D-structure) is where theta-roles are assigned. Logical Form (LF) is where semantic interpretation happens. They're different levels — both abstract, but distinct.

**Movement leaves a copy, not just absence:**
In Minimalism, movement = INTERNAL MERGE. The original position has a copy (which is usually deleted for pronunciation). "What did you see?" = [CP [DP what] C [IP you see [DP what]]] — lower copy not pronounced.

**Phrase structure is NOT linear order:**
The tree represents hierarchical constituency. Linear order is a separate dimension (derived from tree by linearization rules — Kayne's Linear Correspondence Axiom). The tree is the grammar; the string is derived.

**X-bar doesn't apply uniformly across theories:**
DP hypothesis (D heads nominal projections), vP (little-v) for VP shells, CP/TP/AspP in the left periphery — modern cartographic syntax adds many projections. X-bar was a simplification; the full left periphery (Rizzi 1997) has ForceP, TopP, FocP, FinP, etc.

**Binding domain is not just the clause:**
Binding domains are defined technically (smallest full IP containing the NP and a subject) — not just "sentence." Long-distance reflexives in Icelandic, Japanese, and Chinese bind across clause boundaries under specific structural conditions. Condition A is not as simple as "must be in the same sentence."

**Not all "movement" theories are equal:**
Minimalism's copy theory, HPSG's movement-free constraint-based approach, LFG's f-structure factored out from c-structure — these make different empirical and formal commitments. "Movement" is a generative theory's tool, not a fact about language.
