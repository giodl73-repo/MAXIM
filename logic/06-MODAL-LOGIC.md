# Modal Logic: Necessity and Possibility

## The Big Picture

Modal logic extends classical logic with operators for **necessity** (box: □) and
**possibility** (diamond: ◇). Kripke semantics (1963) gives a clean model theory via
"possible worlds." Modal logic is the parent of temporal logic, epistemic logic,
deontic logic, and description logics — all engineering-relevant systems.

```
+-------------------------------------------------------------------+
|                    MODAL LOGIC LANDSCAPE                          |
|                                                                   |
|  SYNTAX              SEMANTICS               AXIOM SYSTEMS        |
|  +------------+      +------------------+    +-----------------+  |
|  | Classical  |      | Kripke frames:   |    | K (basic)       |  |
|  | logic plus |      | (W, R)           |    | T  (reflexive)  |  |
|  | Box phi    |      | W = worlds       |    | S4 (refl+trans) |  |
|  | Diamond phi|      | R = access rel.  |    | S5 (equiv rel.) |  |
|  |            |      | Valuation V      |    | GL (Godel-Lob)  |  |
|  | Box = nec. |      | M, w |= Box phi  |    | B   D   K4      |  |
|  | Diamond =  |      |   iff all w' in  |    +-----------------+  |
|  | possible   |      |   R(w): M,w'|=phi|                         |
|  +------------+      +------------------+                         |
|                                                                   |
|  EXTENSIONS                                                       |
|  +-----------------------------------------------------------+    |
|  | Epistemic logic: K_a phi = "agent a knows phi"           |    |
|  | Deontic: O phi = "phi is obligatory"                     |    |
|  | Temporal: G phi = "phi holds globally from now"          |    |
|  | Dynamic: [alpha] phi = "after action alpha, phi holds"   |    |
|  | Description logics: OWL, EL, ALC (knowledge bases)       |    |
|  +-----------------------------------------------------------+    |
+-------------------------------------------------------------------+
```

---

## Syntax

### Language

Modal propositional language:
```
  phi ::= p                   (atom)
        | top | bot
        | neg phi
        | phi land psi
        | phi lor psi
        | phi -> psi
        | Box phi              (necessarily phi)
        | Diamond phi          (possibly phi)
        | (phi)
```

Defined connective:
```
  Diamond phi  ===  neg Box neg phi
  (phi is possible iff its negation is not necessary)

  Box phi      ===  neg Diamond neg phi
  (phi is necessary iff its negation is not possible)
```

---

## Kripke Semantics

### Kripke Frames and Models

```
  KRIPKE FRAME: F = (W, R)
    W: non-empty set of "possible worlds" (or states)
    R: accessibility relation on W  (R subset W x W)
    R(w) = {w' : (w, w') in R}  ("worlds accessible from w")

  KRIPKE MODEL: M = (W, R, V)
    V: W -> P(Atoms)  (valuation: which atoms are true at each world)
    Or: V: Atoms -> P(W)  (for which atoms are true: set of worlds)
```

### Truth Conditions

```
  M, w |= p           iff   p in V(w)
  M, w |= top          always
  M, w |= bot          never
  M, w |= neg phi      iff   M, w |/= phi
  M, w |= phi land psi iff   M, w |= phi  and  M, w |= psi
  M, w |= phi lor psi  iff   M, w |= phi  or   M, w |= psi
  M, w |= phi -> psi   iff   M, w |/= phi  or  M, w |= psi
  M, w |= Box phi      iff   for all w' with (w, w') in R: M, w' |= phi
  M, w |= Diamond phi  iff   exists w' with (w, w') in R: M, w' |= phi
```

Intuition:
```
  Box phi is true at w if phi is true at ALL accessible worlds.
  Diamond phi is true at w if phi is true at SOME accessible world.

  If R(w) is empty:
    Box phi is VACUOUSLY TRUE at w (for any phi)
    Diamond phi is FALSE at w (for any phi)
```

---

## Axiom Systems and Frame Conditions

The key insight: different properties of the accessibility relation R correspond to
different modal axioms.

### Correspondence Table

```
  AXIOM                         FRAME CONDITION ON R

  K:  Box(phi -> psi) -> (Box phi -> Box psi)
      (Distribution axiom)      ANY frame (valid in all Kripke models)

  T:  Box phi -> phi            R is REFLEXIVE
      (Necessity implies truth) (w, w) in R for all w

  D:  Box phi -> Diamond phi    R is SERIAL
      (Obligation has a path)   For all w, exists w': (w, w') in R

  4:  Box phi -> Box Box phi    R is TRANSITIVE
      (S4 axiom)                (w,w') in R and (w',w'') in R => (w,w'') in R

  5:  Diamond phi -> Box Diamond phi   R is EUCLIDEAN
      (S5 axiom)                (w,w') in R and (w,w'') in R => (w'',w') in R

  B:  phi -> Box Diamond phi    R is SYMMETRIC
                                (w,w') in R => (w',w) in R

  GL: Box(Box phi -> phi) -> Box phi   R is well-founded transitive
      (Godel-Lob, provability logic)   (no infinite R-chains)
```

### Standard Systems

```
  K = {K} + modus ponens + necessitation (if |- phi then |- Box phi)
  (Bare minimum for modal logic)

  T = K + T axiom     (reflexive frames)
  "What is necessary is true"

  S4 = K + T + 4      (reflexive + transitive = preorder frames)
  "Necessity of necessity implies necessity"

  S5 = K + T + 5      (equivalence relation frames)
  "What is possibly possible is possible"
  = K + T + B + 4     (reflexive + symmetric + transitive)

  GL = K + 4 + GL axiom  (well-founded transitive = strict partial order)
  "Provability logic": Box = "is provable in PA"
  Löb's theorem = GL axiom
```

### Diagram of System Inclusions

```
         K
         |
      T     D
      |
     S4
    /   \
   B    S5    (S5 = S4 + B, or K + T + 5)
    \   /
     (S5)

  Separately: GL (not on this lattice)
```

---

## Completeness for Modal Logic

### Canonical Model Construction

Completeness of modal logic systems: every consistent formula has a Kripke model.

```
  CANONICAL MODEL for system S:
  Worlds: maximal consistent sets of formulas (in the language, consistent with S)
  Accessibility: Gamma R Delta  iff  {phi : Box phi in Gamma} subset Delta
  Valuation: p true at Gamma  iff  p in Gamma

  CANONICAL MODEL THEOREM:
  Every formula consistent with S is satisfied in the canonical model.
  Therefore S is complete with respect to its class of frames.
```

### Decidability

```
  Basic modal logic K: PSPACE-complete satisfiability.
  S4 and S5: PSPACE-complete.

  Proof: finite model property.
  If phi is satisfiable, it is satisfied in a model of size <= 2^|phi|.
  Decision procedure: enumerate bounded models.

  Comparison to FOL:
  FOL is semi-decidable. Modal logic (propositional variants) is decidable.
  This is because modal logic is essentially a fragment of FOL via standard translation.
```

---

## Standard Translation to FOL

Modal logic embeds into FOL:

```
  STANDARD TRANSLATION ST_x(phi):

  ST_x(p)         = P(x)               (unary predicate for p)
  ST_x(neg phi)   = neg ST_x(phi)
  ST_x(phi land psi) = ST_x(phi) land ST_x(psi)
  ST_x(Box phi)   = Forall y. (R(x,y) -> ST_y(phi))   (fresh y)
  ST_x(Diamond phi) = Exists y. (R(x,y) land ST_y(phi))  (fresh y)

  Example: Box(p -> q) -> (Box p -> Box q)
  ST: Forall y.(R(x,y)->(P(y)->Q(y))) -> (Forall y.(R(x,y)->P(y)) -> Forall y.(R(x,y)->Q(y)))
  This is a FOL tautology (K axiom is valid).
```

Modal logic is a **fragment of FOL** — specifically the fragment definable in the
two-variable fragment with one binary relation. This explains its decidability.

---

## Epistemic Logic

Modal logic applied to knowledge and belief:

```
  EPISTEMIC LOGIC (Hintikka 1962):
  K_a phi  =  "agent a knows phi"
  B_a phi  =  "agent a believes phi"

  Kripke semantics: worlds = information states
  (w, w') in R_a if w' is consistent with a's information at w

  AXIOMS for knowledge:
  K_a phi -> phi            (what is known is true)
  K_a phi -> K_a K_a phi    (positive introspection: I know what I know)
  neg K_a phi -> K_a neg K_a phi  (negative introspection)

  COMMON KNOWLEDGE: C phi = "everyone knows phi and knows that everyone knows..."
  C phi = phi land E phi land E E phi land ...
  (where E = "everyone knows")

  APPLICATION: distributed systems, cryptographic protocols.
  "All agents know the public key" = C(K_all pub_key)
  Muddy children puzzle, Byzantine agreement analyzed via epistemic logic.
```

---

## Dynamic Logic

Modal logic for program semantics:

```
  PROPOSITIONAL DYNAMIC LOGIC (PDL):
  [alpha] phi   =  "after every execution of program alpha, phi holds"
  <alpha> phi   =  "there exists an execution of alpha after which phi holds"

  Programs alpha:
    a          (atomic action)
    alpha; beta  (sequential composition)
    alpha union beta  (nondeterministic choice)
    alpha*     (Kleene star: 0 or more executions)
    phi?       (test: execute only if phi holds)

  HOARE LOGIC CONNECTION:
  {P} alpha {Q}  ===  P -> [alpha] Q
  Hoare pre/postcondition logic is a fragment of PDL.

  PDL is EXPTIME-complete.
```

---

## Provability Logic (GL)

Modal logic for Gödel provability:

```
  PROVABILITY LOGIC (Solovay 1976):
  Interpret Box phi as "phi is provable in PA" (i.e., Provable(gn(phi))).

  GL AXIOMS:
  K:  Box(phi -> psi) -> (Box phi -> Box psi)
  4:  Box phi -> Box Box phi       (if provable, provably provable)
  GL: Box(Box phi -> phi) -> Box phi  (= Lob's theorem!)

  KEY FACTS:
  Box phi -> phi is NOT an axiom:
    "If phi is provable, then phi is true."
    This fails: we cannot assert this in GL (by Godel G2 for Con(PA)).
  Box(Box phi -> phi) -> Box phi IS an axiom:
    Lob's theorem: if PA proves "provable -> true," then PA proves it directly.

  COMPLETE AXIOMATIZATION:
  Solovay 1976: GL is exactly the modal logic of PA provability.
  Every valid modal statement about PA provability follows from GL.
```

---

## Description Logics

Modal-logic-based languages for knowledge representation:

```
  DESCRIPTION LOGICS (DL):
  Used in Semantic Web (OWL), ontologies, databases.

  BASIC DL: ALC
  Concepts (unary predicates): Human, Animal, ...
  Roles (binary predicates): hasParent, worksFor, ...

  Concept constructors:
    C sqcap D   (intersection: and)
    C sqcup D   (union: or)
    neg C       (complement)
    Forall r. C  (universal restriction: all r-successors are C)
    Exists r. C  (existential restriction: some r-successor is C)

  KRIPKE SEMANTICS:
  Worlds = individuals, roles = accessibility relations.
  Forall r. C = Box_r C in modal logic.
  Exists r. C = Diamond_r C in modal logic.

  DL HIERARCHY (complexity):
    EL:   Exists r. C, sqcap only. P-time reasoning. (Used in SNOMED CT)
    ALC:  Add neg, lor. EXPTIME.
    SHIQ: Add cardinality restrictions, inverse roles. EXPTIME.
    OWL 2: Web ontology language. Based on SROIQ. Undecidable in full.
```

---

## Decision Cheat Sheet

| I want to... | Use |
|---|---|
| Express "necessarily phi" | Box phi |
| Express "possibly phi" | Diamond phi |
| Model "what is necessary is true" | T axiom / reflexive frames |
| Model knowledge (I know what I know) | S5 (equivalence relation) |
| Model provability | GL (Löb's theorem as axiom) |
| Model programs and Hoare logic | Dynamic logic (PDL) |
| Check satisfiability of modal formula | PSPACE SAT algorithm for K/S4/S5 |
| Use modal logic for ontologies | Description logics (OWL, ALC) |

---

## Common Confusion Points

**Box phi is vacuously true when no worlds are accessible.**
If w has no accessible worlds, Box phi holds at w for any phi. This is "vacuous necessity"
— a logical feature, not a bug. System D adds an axiom to rule it out (seriality: every
world has at least one accessible world).

**S4 vs. S5.**
S4: reflexive + transitive (preorder). S5: equivalence relation (also symmetric). S5 is
the epistemic logic of perfect introspection — an idealized agent that knows what it knows
and knows what it doesn't know. S4 lacks the "knows what you don't know" direction.

**Modal logic is not about "maybe."**
The term "possible worlds" is philosophical, but in CS the semantics is completely concrete:
worlds are states, accessibility is a transition relation. In temporal logic it is exactly
the state space of a system.

**Necessitation rule.**
In all normal modal logics, if |- phi then |- Box phi. This does NOT mean Box phi -> phi.
phi being provable means it's true in every model at every world. Box phi -> phi would
require reflexivity (system T). The rule says "universal truths are necessarily true,"
not "necessary statements must be actually true."
