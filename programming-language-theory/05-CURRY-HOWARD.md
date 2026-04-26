# Curry-Howard Correspondence: Proofs as Programs, Types as Propositions

## The Big Picture

The Curry-Howard correspondence is the deepest structural insight in PLT: type systems *are* logical systems, typed programs *are* proofs, and evaluation *is* proof normalization. This is not a metaphor or an analogy — it is a precise mathematical equivalence between two independently developed formalisms.

```
+--------------------------------------------------------------------------+
|                    CURRY-HOWARD CORRESPONDENCE                           |
+--------------------------------------------------------------------------+
|                                                                          |
|     LOGIC (Intuitionistic)          TYPE THEORY / PROGRAMS               |
|     ────────────────────────        ──────────────────────────           |
|     Proposition P              ↔    Type τ                               |
|     Proof of P                 ↔    Program of type τ                    |
|     Proof normalization        ↔    Program evaluation (β-reduction)     |
|     Implication P → Q          ↔    Function type τ → σ                 |
|     Conjunction P ∧ Q          ↔    Product type τ × σ                  |
|     Disjunction P ∨ Q          ↔    Sum type τ + σ                      |
|     Truth ⊤                    ↔    Unit type ()                         |
|     Falsehood ⊥                ↔    Empty type Void (no inhabitants)    |
|     Universal ∀x.P(x)          ↔    Dependent function Π(x:A).B(x)     |
|     Existential ∃x.P(x)        ↔    Dependent pair Σ(x:A).B(x)         |
|                                                                          |
|     STLC ↔ propositional intuitionistic logic                           |
|     System F ↔ second-order propositional logic                         |
|     Martin-Löf TT ↔ first-order intuitionistic predicate logic          |
|     Coq CIC ↔ calculus of constructions (dependent types + induction)   |
|                                                                          |
|     Classical logic ↔ CPS transform (Griffin 1990): callcc corresponds  |
|                        to Peirce's law ((P→Q)→P)→P                      |
|     Linear logic ↔ Linear types / resource sensitivity (Girard 1987)    |
|     Session types ↔ linear propositions (communications)                |
+--------------------------------------------------------------------------+
```

---

## 1. The Basic Correspondence: STLC ↔ Propositional Logic

The simple typed lambda calculus corresponds to propositional intuitionistic logic:

```
PROPOSITIONS AS TYPES:

  Propositional logic formula: P → Q (if P then Q)
  Type theory type:            τ → σ  (function from τ to σ)

  Proof of P → Q = function f : τ → σ
    (given a proof/value of type τ, produce a proof/value of type σ)

CONJUNCTION AND PRODUCT:

  Logic: P ∧ Q (P and Q are both true)
  Type:  τ × σ  (pair of values of types τ and σ)
  Proof: (p, q) where p : τ and q : σ
  Elimination: fst (p,q) = p  [∧-elim for P]
               snd (p,q) = q  [∧-elim for Q]

DISJUNCTION AND SUM:

  Logic: P ∨ Q (at least one of P, Q is true)
  Type:  τ + σ  (either a value of type τ or a value of type σ)
  Proof: Left p where p : τ   [∨-intro left]
         Right q where q : σ  [∨-intro right]
  Elimination (case analysis): case x of Left p → f p | Right q → g q
    (corresponds to: if P∨Q, and P→R, and Q→R, then R)

TRUTH AND UNIT:

  Logic: ⊤ (trivially true)
  Type:  () (unit type with one value)
  Proof: () (the unique proof/value)

FALSEHOOD AND EMPTY TYPE:

  Logic: ⊥ (false; no proof exists)
  Type:  Void (empty type; no values)
  Ex falso quodlibet: from ⊥ you can prove anything
  absurd :: Void → a   (this function exists in Haskell; type: Void → a)
```

**The key isomorphism**: Typing derivations *are* natural deduction proofs. The STLC typing rules are exactly the natural deduction introduction and elimination rules for intuitionistic propositional logic:

```
TYPING RULES = NATURAL DEDUCTION RULES:

  STLC T-Abs:                    NJ →-Introduction:
  Γ, x:τ ⊢ t : σ                Γ, P ⊢ Q
  ─────────────────              ─────────────
  Γ ⊢ λx:τ.t : τ → σ           Γ ⊢ P → Q

  STLC T-App:                    NJ →-Elimination (Modus Ponens):
  Γ ⊢ t₁ : τ → σ    Γ ⊢ t₂ : τ  Γ ⊢ P → Q    Γ ⊢ P
  ────────────────────────────    ─────────────────────
  Γ ⊢ t₁ t₂ : σ                 Γ ⊢ Q

  The typing context Γ = undischarged assumptions = hypothesis set
  A typing derivation = a proof tree in natural deduction
```

---

## 2. Proof Normalization = Computation

The computational content of the correspondence:

```
PROOF NORMALIZATION = β-REDUCTION:

  Logic: "detour" = apply ∧-introduction then immediately ∧-elimination:
    Prove P ∧ Q, then immediately extract the P component.
    The proof contains an unnecessary detour (can be simplified).

  Type theory: β-redex = apply a function then immediately β-reduce
    fst (a, b) →_β a
    (λx. t) s →_β t[s/x]

  NORMALIZATION THEOREM (for STLC):
    Every proof/program has a unique normal form.
    Normalization = cut elimination in logic = evaluation in PLT.

STRONG NORMALIZATION:
  STLC: all terms normalize (no infinite loops; STLC can't express recursion)
  System F: also strongly normalizing
  Martin-Löf TT: normalizes (requires termination checker for recursion)
  PCF (+ recursion): NOT normalizing (can loop; fix is not provably terminating)

  THIS IS WHY COQ/AGDA REQUIRE TERMINATION PROOFS:
    In the proof interpretation, a non-terminating program would be a
    circular proof (using the conclusion in its own derivation = paradox)
    Requiring termination = preventing circular proofs = consistency
```

---

## 3. The BHK Interpretation

Brouwer-Heyting-Kolmogorov (BHK) interpretation — the philosophical foundation of the correspondence:

```
BHK INTERPRETATION (constructive proofs):

  A proof of P → Q = a CONSTRUCTION that converts proofs of P to proofs of Q
                   = a function

  A proof of P ∧ Q = a PAIR (proof of P, proof of Q)

  A proof of P ∨ Q = either a proof of P OR a proof of Q, clearly labeled
                   = a tagged union

  A proof of ∀x.P(x) = a construction that for any x produces a proof of P(x)
                      = a function (dependent)

  A proof of ∃x.P(x) = a specific witness x, PLUS a proof that P(x) holds
                      = a dependent pair

KEY PHILOSOPHICAL POINT:
  In classical logic: P ∨ ¬P holds for all P (law of excluded middle)
  BHK interpretation: this would require: for any P, you can either
    provide a proof of P or a proof of ¬P
    → This is NOT constructively valid in general

  CLASSICAL LOGIC ≠ INTUITIONISTIC LOGIC under BHK
  Intuitionistic logic requires WITNESSES (constructive proofs)
  Classical logic allows proof by contradiction without construction
```

**Why intuitionistic, not classical?**

```
CONSTRUCTIVE = ALGORITHMIC:

  A constructive proof of ∃n. n > 100 AND prime(n) must EXHIBIT n.
  A classical proof may just show: "suppose no such n exists → contradiction"
    without ever naming n.

  For algorithms and programs:
    Constructive proof → extract a program
    Classical proof → no program extractable (the witness isn't provided)

  COROLLARY: Type-theoretic proof assistants (Coq, Agda, Lean) use
  intuitionistic logic because we want to EXTRACT PROGRAMS from proofs.

  You can ADD classical axioms to Coq:
    Classical.classic : ∀ P, P ∨ ¬ P
  But then you lose computability of extracted programs.
```

---

## 4. Classical Logic and CPS

Tim Griffin (1990) discovered that classical logic corresponds to the CPS transform:

```
GRIFFIN'S INSIGHT:

  In classical logic, Peirce's law holds:
    ((P → Q) → P) → P

  In type theory, this is:
    callcc : ((α → β) → α) → α
    (call-with-current-continuation)

  WHY:
    Callcc captures the "continuation" (rest of the computation)
    as a first-class function.
    Using callcc, you can implement "abort" — throw away the continuation.
    Aborting = classical non-constructive reasoning (ignoring the context).

  THE CPS TRANSFORM (Plotkin 1975) embeds STLC into classical logic:
    Every function call passes an explicit continuation k.
    callcc becomes: λk. k (λv. /* ignore current k, use saved k */)

DOUBLE NEGATION TRANSLATION:

  Classical logic can be EMBEDDED in intuitionistic logic via:
    P_classical corresponds to ¬¬P_intuitionistic
    (double negation translation: Gödel, Gentzen)

  In types: this corresponds to CPS transform!
    A classical type τ corresponds to (τ → ⊥) → ⊥ in intuitionistic types
    = a computation that calls its continuation with a τ-value

  PRACTICAL CONSEQUENCE:
    Any classical proof can be made constructive via CPS transform
    Continuations = classical reasoning in types
    → call/cc in Scheme = adding classical axiom to the type theory
```

---

## 5. System F ↔ Second-Order Logic

```
SYSTEM F (Universal polymorphism):
  ∀α. τ  — polymorphic type
  Λα. t  — type abstraction

SECOND-ORDER PROPOSITIONAL LOGIC:
  ∀P. F(P)  — quantify over propositions
  (Second-order: quantify over propositional variables)

CORRESPONDENCE:
  System F type  ∀α. α → α     ↔     Formula  ∀P. P → P
  System F term  Λα. λx:α. x   ↔     Proof    "for all P, if P then P"
                                              = the proof of P → P universally

IMPREDICATIVITY:
  In second-order logic, ∀P ranges over all propositions including
  propositions containing ∀P itself.
  This allows encoding of induction (via Church-encoding):
    ℕ = ∀α. α → (α → α) → α   (natural number = a proof scheme for induction)
  But impredicativity makes consistency more delicate
    (Girard's paradox: full impredicativity → inconsistency)
```

---

## 6. Linear Logic ↔ Linear Types ↔ Rust

Girard (1987) invented linear logic. Its key feature: formulas are resources — each hypothesis must be used exactly once.

```
LINEAR LOGIC CONNECTIVES:

  LINEAR IMPLICATION:  A ⊸ B  (consume A to produce B)
    Compare classical:  A → B  (A can be used multiple times, ignored)

  TENSOR PRODUCT:      A ⊗ B  (have BOTH A and B, each usable once)
    Compare product:   A × B  (can project out either A or B multiple times)

  PAR (additive or):   A ⅋ B
  PLUS (additive or):  A ⊕ B  (have exactly one of A or B)
  OF COURSE:           !A    (A is a classical resource = can use multiple times)
  WHY NOT:             ?A    (A can be discarded, duplicated)

RESOURCE SENSITIVITY:
  Without !: every formula used exactly once
  !A = "classical" resource: can be duplicated and discarded
  → Linear logic embeds classical logic via the !-modality

CORRESPONDENCE WITH LINEAR TYPES:

  Linear type  f : A ⊸ B   ↔   Function that consumes A to produce B
                                (A cannot be used after calling f)

  Rust ownership:
    T = owned value (linear resource, must be used exactly once or moved)
    &T = shared reference = !T (can duplicate, cannot modify)
    &mut T = exclusive reference = affine T (can use, modifies the resource)

  AFFINE TYPES (use AT MOST ONCE):
    Less restrictive than linear (can also discard)
    Rust is an affine type system (you can drop values without using them)

SESSION TYPES (Honda 1993) as linear logic propositions:
  A communication channel has a protocol type (linear proposition)
  Sending a message = using the A resource
  Channel type = remaining protocol (linear continuation type)
  → Deadlock freedom follows from linearity
```

---

## 7. The Taxonomy of Logic-Type Correspondences

```
+--------------------------------------------------------------+
|  LOGIC                    TYPED SYSTEM           USE         |
+--------------------------------------------------------------+
|  Intuitionistic prop.     STLC                  Foundations  |
|  Second-order prop.       System F              Haskell Core |
|  First-order pred.        Dep. types (MLTT)     Coq, Agda   |
|  Higher-order pred.       CIC (Coq)             Proof asst. |
|  Classical prop.          STLC + call/cc        Scheme callcc|
|  Classical (via ¬¬)       CPS transform         Compilers   |
|  Linear logic             Linear types          Rust (affine)|
|  Linear logic session     Session types         Protocols   |
|  Homotopy type theory     Univalent foundations Lean 4, Agda|
+--------------------------------------------------------------+
```

---

## Decision Cheat Sheet

| Concept | Type theory counterpart | Production example |
|---------|------------------------|--------------------|
| Implication P → Q | Function type A → B | Every function in every language |
| Conjunction P ∧ Q | Product type A × B | Tuples, structs |
| Disjunction P ∨ Q | Sum type A + B | Rust enum, Haskell Either |
| Falsehood ⊥ | Empty type Void | Rust !, Haskell Void |
| Classical double negation | CPS transform | Compiler IR |
| Callcc / Peirce's law | First-class continuations | Scheme, Delimited continuations |
| Linear implication A ⊸ B | Affine/linear function types | Rust ownership |
| !A (of course) | Unrestricted use | Haskell default (pure functions) |
| Normalization = computation | β-reduction terminates | Coq terms always terminate |

---

## Common Confusion Points

**Curry-Howard doesn't mean "every type is a useful proposition"**: The type `Int → Int` corresponds to the proposition "if P then P" for any P — which is trivially true. The correspondence tells you about the *structure* of types and proofs, not that every type is an interesting theorem.

**Intuitionistic ≠ classical logic**: In intuitionistic logic, law of excluded middle (P ∨ ¬P) is not provable. Adding it gives classical logic, which corresponds to callcc. This is not a deficiency — intuitionistic logic is the correct setting for constructive proofs and program extraction.

**Linear types ≠ Rust's borrow checker exactly**: Rust uses affine types (use at most once) not linear types (use exactly once). Additionally, Rust's borrow system is more flexible than simple affine typing — the borrow checker allows temporary shared borrows (&T) which act as !T (unlimited use) for the duration of the borrow. The formal semantics is captured by RustBelt (Stacked Borrows).

**Proof normalization = β-reduction only in pure calculi**: In STLC and System F, β-reduction is the only computation rule and all terms normalize. In calculi with recursion (PCF), let rec, or Coq's Fixpoint, you need additional reduction rules (ι-reduction for inductive types). Consistency (no proof of False) requires that the calculus still normalizes — which is why Coq requires structural recursion.
