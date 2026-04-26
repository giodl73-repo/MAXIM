# Proof Theory: Natural Deduction and Sequent Calculus

## The Big Picture

Proof theory is the study of **formal derivations** — what can be proved and how. It treats
proofs as mathematical objects, analyzes their structure, and uses that structure to prove
meta-theorems (consistency, decidability, proof lengths).

```
+-------------------------------------------------------------------+
|                    PROOF SYSTEMS LANDSCAPE                        |
|                                                                   |
|  HILBERT SYSTEMS          NATURAL DEDUCTION      SEQUENT CALCULUS |
|  +-----------------+      +----------------+     +-------------+  |
|  | Many axioms,    |      | Few axioms,    |     | Symmetric,  |  |
|  | few rules       |      | many rules     |     | best for    |  |
|  | (Modus Ponens   |      | Intro/Elim     |     | meta-proofs |  |
|  | only)           |      | per connective |     | LK (Gentzen)|  |
|  | Awkward to use  |      | Readable       |     | LJ (intuit.)|  |
|  | Easy to analyze |      | Curry-Howard   |     |             |  |
|  +-----------------+      +----------------+     +-------------+  |
|                                                                   |
|  RESOLUTION               TABLEAU                AUTOMATED        |
|  +-----------------+      +----------------+     +-------------+  |
|  | Clause-based    |      | Semantic tree  |     | SAT/SMT     |  |
|  | Single rule     |      | Branch-closing |     | Lean/Coq    |  |
|  | Basis of Prolog |      | Used in ATP     |     | Isabelle    |  |
|  +-----------------+      +----------------+     +-------------+  |
|                                                                   |
|  META-THEOREMS                                                    |
|  +-----------------------------------------------------------+    |
|  | Soundness  Completeness  Cut Elimination  Normalization   |    |
|  | Curry-Howard  Gentzen's Hauptsatz  Ordinal Analysis       |    |
|  +-----------------------------------------------------------+    |
+-------------------------------------------------------------------+
```

---

## Hilbert-Style Systems

The oldest formal proof systems. Axiomatically heavy, inference-rule-light.

```
  Structure:
    Axiom schemas: infinite families of tautologies
    Rules: typically just Modus Ponens:
           from phi and phi -> psi, derive psi

  Classic axioms for propositional logic (one axiomatization):
    (H1)  phi -> (psi -> phi)
    (H2)  (phi -> (psi -> chi)) -> ((phi -> psi) -> (phi -> chi))
    (H3)  (neg phi -> neg psi) -> (psi -> phi)
    Plus Modus Ponens.

  Problem: proofs are extremely long and unreadable.
  "A -> A" takes several steps even in this simple system.
```

Hilbert systems are primarily of theoretical interest — they show that a minimal set of rules
suffices. Nobody actually writes proofs in them.

---

## Natural Deduction (Gentzen 1935)

Designed to match how mathematicians actually reason. Each connective has introduction
(how to prove it) and elimination (how to use it) rules.

### Proof Structure

Natural deduction proofs are **trees** with hypotheses at leaves and conclusion at root:

```
  [phi]   [psi]               [phi]
    ...     ...                ...
    chi     chi                psi
   ───────────── (lor-E)      ────── (->-I, discharging [phi])
   phi lor psi  chi           phi -> psi
```

Hypotheses in brackets [...] are discharged (cancelled) by certain rules.

### Rules for Propositional Logic

```
  CONJUNCTION:
    phi   psi                  phi land psi           phi land psi
   ──────────── (land-I)       ──────────── (land-E1)  ──────────── (land-E2)
   phi land psi                   phi                     psi

  DISJUNCTION:
     phi                psi          [phi] [psi]
   ──────────── (lor-I1) ──────────── (lor-I2)    phi lor psi  chi  chi
   phi lor psi         phi lor psi                ─────────────────────── (lor-E)
                                                          chi

  IMPLICATION:
    [phi]
     ...
     psi                      phi    phi -> psi
   ──────── (->-I, discharge phi)   ──────────────── (->-E = Modus Ponens)
   phi -> psi                              psi

  NEGATION:
    [phi]
     ...               phi   neg phi
     bot               ─────────────── (neg-E = ex falso)
   ──────── (neg-I)         psi
   neg phi

  DOUBLE NEGATION (classical only):
     neg neg phi
    ──────────── (DNE)
       phi
```

### Quantifier Rules

```
  UNIVERSAL:
    phi[t/x]                          [x arbitrary, not free in hypotheses]
   ──────────── (Forall-E, t any term)        ...
  Forall x. phi                              phi
                                       ──────────── (Forall-I)
                                       Forall x. phi

  EXISTENTIAL:
  phi[t/x]                     [Exists x. phi]  [phi[c/x]]
  ──────────────── (Exists-I)        ...              ...
  Exists x. phi                        psi             psi
                               ─────────────────────── (Exists-E)
                                         psi
```

### Example Proof: (A -> B) -> (B -> C) -> (A -> C) [transitivity]

```
  [A -> B]  [A]
  ───────────── (->-E)
       B         [B -> C]
       ────────────── (->-E)
             C
           ──────────── (->-I, discharging [A])
           A -> C
         ──────────────────── (->-I, discharging [B -> C])
         (B -> C) -> (A -> C)
       ──────────────────────────── (->-I, discharging [A -> B])
       (A -> B) -> (B -> C) -> (A -> C)
```

### Intuitionistic vs. Classical ND

Remove the double negation elimination (DNE) rule: you get **intuitionistic natural deduction**.
Intuitionistic logic rejects "proof by contradiction" (neg neg A => A). The law of excluded
middle (A lor neg A) is not a theorem. This connects directly to constructive mathematics
and type theory (Curry-Howard, Module 09).

---

## Sequent Calculus (Gentzen 1935)

Gentzen's LK system. More symmetric than natural deduction. Better for meta-proofs.

### Sequents

A sequent is:  Gamma |- Delta

where Gamma (antecedent) and Delta (succedent) are sets/multisets of formulas.

```
  Intuition:
    Gamma |- Delta  means:
    "Assuming all of Gamma, at least one of Delta holds."

  Or equivalently:
    "The conjunction of Gamma implies the disjunction of Delta."

  Special cases:
    phi |- psi          means phi implies psi
    |- phi              means phi is a tautology (no assumptions needed)
    phi |-              means phi is contradictory
    |-                  means absurdity (empty antecedent and succedent)
```

### Structural Rules

```
  IDENTITY:      phi |- phi   (axiom)

  CUT:           Gamma |- Delta, phi    phi, Gamma' |- Delta'
                 ─────────────────────────────────────────────
                         Gamma, Gamma' |- Delta, Delta'

  WEAKENING:
    Gamma |- Delta              Gamma |- Delta
   ─────────────── (W-L)      ─────────────── (W-R)
   phi, Gamma |- Delta         Gamma |- Delta, phi

  CONTRACTION:
   phi, phi, Gamma |- Delta   Gamma |- Delta, phi, phi
   ─────────────────── (C-L)  ─────────────────────── (C-R)
     phi, Gamma |- Delta          Gamma |- Delta, phi
```

### Logical Rules (Left and Right for each connective)

```
  CONJUNCTION:
   phi, Gamma |- Delta        psi, Gamma |- Delta
  ─────────────────── (L1)   ─────────────────── (L2)
  phi land psi, G |- D       phi land psi, G |- D

  Gamma |- Delta, phi    Gamma |- Delta, psi
  ────────────────────────────────────────── (R)
           Gamma |- Delta, phi land psi

  IMPLICATION:
  Gamma |- Delta, phi    psi, Gamma' |- Delta'
  ──────────────────────────────────────────── (L)
   phi -> psi, Gamma, Gamma' |- Delta, Delta'

  phi, Gamma |- Delta, psi
  ─────────────────────── (R)
  Gamma |- Delta, phi -> psi
```

### The Cut Elimination Theorem (Gentzen's Hauptsatz)

The most important theorem in proof theory:

```
  HAUPTSATZ (Main Theorem):
  Every sequent provable in LK (with cut) is provable without the cut rule.

  Proof: by a complex double induction on proof structure.
  The cut formula is "interpolated out" by transforming the proof tree.
```

**Why it matters:**

```
  WITH CUT:                          WITHOUT CUT (cut-free):
  Proofs can use lemmas.             Proofs are analytic.
  Proof may be much shorter.         Subformulas of conclusion only appear.
  Non-constructive.                  Subformula property holds.

  Subformula property: every formula in a cut-free proof is a
  subformula of the endsequent. This is the key to decidability
  and proof search.
```

Cut elimination gives:
1. **Consistency**: If bot is provable from empty, the cut-free proof of |- bot would require
   an axiom phi |- phi where phi is a subformula of bot — but bot has no subformulas.
2. **Decidability** (for propositional logic): proof search is finite (bottom-up).
3. **Interpolation** (Craig interpolation): if phi |- psi then there exists chi over their
   common language such that phi |- chi and chi |- psi.

---

## Proof Normalization (Natural Deduction)

The natural deduction analog of cut elimination.

```
  A DETOUR: Introducing then immediately eliminating a connective.

  Example:
    A    B
   ────────── (land-I)
   A land B
   ────────── (land-E1)
       A

  This can be reduced to:
       A     (immediate — the detour is removed)

  REDUCTION RULES (beta-reduction analog):
    land-I followed by land-E1:     reduces to left component
    land-I followed by land-E2:     reduces to right component
    ->-I followed by ->-E:          reduces to body with argument substituted
    lor-I1 followed by lor-E:       reduces to left branch with phi
    Exists-I followed by Exists-E:  reduces to body with witness substituted
```

### Normal Form

A proof is in **normal form** if it contains no detours. The normalization theorem says
every proof can be reduced to a normal proof. This is:
- The proof-theoretic analog of cut elimination.
- Via Curry-Howard: the analog of beta-reduction in lambda calculus.
- Strong normalization: every reduction sequence terminates (implies consistency).

---

## Curry-Howard Correspondence (Preview)

The connection between proof theory and type theory, covered in depth in Module 09:

```
  PROOF THEORY (Natural Deduction)    TYPE THEORY (Lambda Calculus)
  ──────────────────────────────────  ────────────────────────────
  Formula phi                    <--> Type A
  Proof of phi                   <--> Term of type A
  Hypothesis [phi]               <--> Variable of type A
  ->-Introduction                <--> Lambda abstraction  (lam x. t)
  ->-Elimination (MP)            <--> Function application (t u)
  land-Introduction              <--> Pair construction   (t, u)
  land-Elimination               <--> Projection          (fst, snd)
  lor-Introduction               <--> Injection            (inl, inr)
  lor-Elimination                <--> Case analysis        (case)
  Proof normalization            <--> Beta reduction
  Normal proofs                  <--> Normal (beta-normal) terms
  Strong normalization           <--> Termination of computation
  Classical DNE                  <--> call/cc (continuations)
  Intuitionistic logic           <--> Simply-typed lambda calculus
  System F (2nd order)           <--> Polymorphic lambda calculus
  Dependent types                <--> Proof-carrying code, Lean, Coq
```

The Curry-Howard correspondence says **proofs are programs, propositions are types**. This
is not a metaphor — it is an exact isomorphism. The proof objects computed by Lean and Coq
are literally lambda terms.

---

## Ordinal Analysis and Proof Strength

Proof theory measures the "strength" of formal systems using ordinals. This is not abstract bookkeeping — it answers three concrete questions:

1. **What does this system actually prove?** Two systems may look different syntactically but prove exactly the same arithmetic theorems — their proof-theoretic ordinal identifies them as equiconsistent.
2. **What axioms do you actually need?** Reverse mathematics (Harvey Friedman) inverts the usual direction: instead of proving theorems from axioms, you ask what axioms are *necessary* for a theorem. The proof-theoretic ordinal calibrates this.
3. **How long can proofs get?** Systems with larger proof-theoretic ordinals can produce much shorter proofs of theorems that weaker systems can also prove but only with enormous proofs — proof length is sensitive to the strength hierarchy.

```
  PROOF-THEORETIC ORDINALS (strength hierarchy):

  System                              Ordinal          What it measures
  ─────────────────────────────────────────────────────────────────────
  PRA (Primitive Recursive Arithmetic) omega^omega     Finitary arithmetic;
                                                       Hilbert's "safe" base
  PA (Peano Arithmetic)               epsilon_0        Full first-order arithmetic
                                       = omega^omega^omega^...  (tower)
  ACA_0 (Arithmetical Comprehension)  epsilon_0        Same ordinal as PA —
                                                       ACA_0 is conservative
                                                       over PA for arithmetic
  ATR_0 (Arithmetical Trans. Rec.)    Gamma_0          Needed for: comparability
                                                       of well-orderings,
                                                       open Ramsey theory
  Pi^1_1-CA_0                        Psi(Omega_omega)  Needed for: Kruskal's
                                                       tree theorem, graph minor
                                                       theorem (Robertson-Seymour)
  ID_1 (one inductive definition)    phi_{epsilon_0}(0) Iterated inductive defs
  ZFC                                very large /       Most of mathematics;
                                     unknown in full    exact ordinal not computed
```

**Why epsilon_0 specifically?** Gentzen (1936) proved PA consistent using transfinite induction up to epsilon_0 — the smallest ordinal that cannot be proved well-founded within PA itself. This is a precise statement: PA can handle induction up to any specific ordinal below epsilon_0, but not "up to epsilon_0" uniformly. Gentzen's proof is therefore not circular (it uses a principle PA cannot express) but it does require trusting transfinite induction, which is a meaningful assumption.

**Reverse mathematics — the practical payoff**: Harvey Friedman's program asks: for each mathematical theorem T, what is the weakest subsystem of second-order arithmetic that proves T? The answer sorts mathematics into a small number of "natural" strength levels:

```
  RCA_0       (Recursive comprehension): computable analysis; most basic analysis
  WKL_0       (Weak König's Lemma): Hahn-Banach, Brouwer fixed-point, compactness
  ACA_0       (Arithmetical comprehension): Bolzano-Weierstrass, sequential completeness
  ATR_0       (Arithmetical transfinite recursion): open Ramsey, comparability of ordinals
  Pi^1_1-CA_0 (Pi^1_1 comprehension): Kruskal's tree theorem, Nash-Williams

  FINDING: The vast majority of ordinary mathematical theorems fall into one of
  these five levels. The axioms you need are precisely calibrated — not "all of ZFC"
  but a specific, minimal fragment. This is audit-grade axiom accounting.
```

**Proof-search complexity and ordinals**: In cut-free sequent calculus, proof search terminates because the subformula property bounds the search space. But proof length can be non-elementary in the nesting depth of quantifiers. The relationship between proof-theoretic strength and proof-search complexity (how long proofs can be) is captured by: stronger systems have longer "shortest proofs" for the theorems they share with weaker systems. This is the proof-theoretic analog of the gap between polynomial-time computability and what requires exponential certificates.

---

## Decision Cheat Sheet

| I want to... | Use |
|---|---|
| Read a natural proof of A -> A | Natural deduction: hypothesis -> conclusion |
| Prove consistency via a syntactic argument | Cut elimination (Hauptsatz) |
| Connect logic to type theory | Curry-Howard (proofs = programs, types = propositions) |
| Find a proof-search procedure | Cut-free sequent calculus (subformula property) |
| Normalize a proof, remove detours | Normalization theorem |
| Measure how strong a formal system is | Proof-theoretic ordinal |
| Prove Craig interpolation | Via cut elimination in sequent calculus |

---

## Common Confusion Points

**Natural deduction vs. sequent calculus: which to use?**
Use natural deduction when writing proofs by hand — it matches mathematical intuition.
Use sequent calculus for meta-proofs (consistency, interpolation, cut elimination) — the
symmetric structure makes inductions cleaner. Lean/Coq use natural deduction under the hood.

**Cut elimination vs. normalization.**
Both eliminate "detours." Cut elimination is for sequent calculus; normalization is for
natural deduction. They are equivalent by the Curry-Howard-de Bruijn correspondence.

**Intuitionistic vs. classical.**
Classical logic adds either double negation elimination (in ND) or the rule Gamma |- Delta, phi, neg phi
(excluded middle sequent rule). Everything intuitionistic is also classically valid; the
converse fails. Intuitionistic proofs are constructive — they contain witnesses.

**Structural rules and substructural logics.**
Linear logic drops contraction and weakening. This gives resource-sensitive reasoning:
every assumption is used exactly once. Relevant logic drops weakening. These generate
different logics with different computational interpretations.

**Hilbert's program and its failure.**
Hilbert wanted to prove mathematics consistent using only finitary ("safe") methods.
Gödel's second incompleteness theorem (Module 04) shows this is impossible: no
sufficiently strong consistent theory can prove its own consistency.
