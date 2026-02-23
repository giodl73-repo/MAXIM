# 01 — Logic

## Classical, Modal, Intuitionistic Logic; Proof Theory; Gödel's Incompleteness

---

## Big Picture: Logic Landscape

```
┌──────────────────────────────────────────────────────────────────────────┐
│                         LOGIC LANDSCAPE                                  │
├────────────────────────────────────────┬─────────────────────────────────┤
│  CLASSICAL LOGIC                       │  NON-CLASSICAL LOGICS            │
│  ──────────────                        │  ─────────────────               │
│  Propositional (PL)                    │  Modal (K, T, S4, S5)            │
│  First-order predicate (FOL)           │  Intuitionistic (BHK)            │
│  Second-order (SOL)                    │  Temporal (LTL, CTL)             │
│  Higher-order type theory              │  Description logics (OWL)        │
│                                        │  Paraconsistent (tolerate ⊥)     │
│                                        │  Relevance logic                 │
├────────────────────────────────────────┴─────────────────────────────────┤
│  PROOF THEORY                          │  MODEL THEORY                    │
│  Natural deduction                     │  Interpretations/structures      │
│  Sequent calculus                      │  Soundness + completeness        │
│  Resolution (automated)               │  Compactness theorem             │
│  Hilbert systems                       │  Löwenheim-Skolem                │
└────────────────────────────────────────┴─────────────────────────────────┘
```

---

## 1. Propositional Logic

### Syntax and Semantics

```
WELL-FORMED FORMULAS (WFF):
  Atoms: p, q, r, ... (propositional variables)
  Compound: ¬φ, (φ ∧ ψ), (φ ∨ ψ), (φ → ψ), (φ ↔ ψ)

TRUTH-FUNCTIONAL CONNECTIVES:
  ¬ (negation): ¬T = F, ¬F = T
  ∧ (conjunction): T only when both true
  ∨ (disjunction): F only when both false (inclusive or)
  → (material conditional): F only when antecedent T and consequent F
    Controversy: "if p then q" is true when p is false — vacuous truth
    "If the moon is cheese, then 2+2=5" is TRUE (vacuously)
    This is not how "if...then" works in natural language; logic idealizes it
  ↔ (biconditional): T when both have same truth value

TAUTOLOGY: true under all valuations (¬(p ∧ ¬p), p ∨ ¬p, (p → q) ↔ (¬q → ¬p))
CONTRADICTION: false under all valuations (p ∧ ¬p)
SATISFIABLE: true under some valuation

NORMAL FORMS:
  CNF (conjunctive normal form): conjunction of clauses (each clause = disjunction of literals)
    (p ∨ q) ∧ (¬p ∨ r) ∧ (q ∨ ¬r)
    Key for SAT solvers (DPLL, CDCL)
  DNF (disjunctive normal form): disjunction of conjunctions
  Every WFF equivalent to CNF and DNF
  3-SAT: satisfiability of CNF with exactly 3 literals per clause — NP-complete (Cook-Levin)
```

### Proof Systems for PL

```
HILBERT SYSTEM: axiom schemas + modus ponens
  Axiom schemas (e.g., Łukasiewicz):
    H1: p → (q → p)
    H2: (p → (q → r)) → ((p → q) → (p → r))
    H3: (¬q → ¬p) → (p → q)  [or similar for classical logic]
  Modus ponens: from φ and φ → ψ, infer ψ
  Proofs are long but theoretically clean; only one inference rule

NATURAL DEDUCTION (Gentzen/Prawitz):
  Introduction and elimination rules for each connective
  ∧I: from φ, ψ, conclude φ ∧ ψ
  ∧E: from φ ∧ ψ, conclude φ (or ψ)
  →I: from assuming φ and deriving ψ, conclude φ → ψ (discharge assumption)
  →E: from φ → ψ and φ, conclude ψ (modus ponens)
  ¬E: from φ and ¬φ, conclude ψ (ex falso quodlibet — explosion)
  Classical logic adds: ¬¬E (double negation elimination) or excluded middle (φ ∨ ¬φ)
  INTUITIONISTIC logic omits ¬¬E / excluded middle (see §3)
  Curry-Howard: ND proofs ↔ simply typed lambda calculus terms (proof = program)

SEQUENT CALCULUS (Gentzen LK):
  Sequent: Γ ⊢ Δ (from context Γ, derive one of Δ)
  Structural rules: weakening, contraction, cut
  Cut elimination theorem (Gentzen's Hauptsatz):
    Every proof can be converted to cut-free form
    → Logic has the subformula property (all subformulas in cut-free proof appear in conclusion)
    → Consistency follows: no cut-free proof of ⊢ (empty sequent) = no contradiction
```

---

## 2. First-Order Logic (Predicate Logic)

### Syntax

```
VOCABULARY:
  Constants: a, b, c, ... (name specific objects)
  Variables: x, y, z, ... (range over domain)
  Function symbols: f, g, ... (n-ary functions on domain)
  Predicate symbols: P, Q, R, ... (n-ary relations)
  Logical: ∧, ∨, ¬, →, ↔, ∀, ∃, =

TERMS: constants, variables, f(t₁,...,tₙ)
FORMULAS: P(t₁,...,tₙ), φ ∧ ψ, ¬φ, ∀x φ, ∃x φ
  Closed formula (sentence): no free variables

EXAMPLE:
  ∀x(Person(x) → ∃y(Loves(x,y)))
  "Every person loves someone"
```

### Semantics and Key Theorems

```
STRUCTURE (interpretation): M = ⟨D, I⟩
  D: non-empty domain (universe of discourse)
  I: interpretation function (maps constants/predicates/functions to domain objects/sets/functions)
  Truth of φ in M under variable assignment s: M, s ⊨ φ

VALIDITY: true in all structures
SATISFIABILITY: true in some structure

COMPLETENESS THEOREM (Gödel 1930):
  Every valid FOL sentence has a proof (syntactic derivation)
  ⊨ φ → ⊢ φ
  Converse (soundness): ⊢ φ → ⊨ φ (trivial; proofs preserve truth)
  Combined: the proof system is complete

COMPACTNESS THEOREM:
  Σ ⊨ φ iff some FINITE subset of Σ ⊨ φ
  Equivalently: if every finite subset of Σ is satisfiable, then Σ is satisfiable
  Proof: via completeness (proofs are finite; use only finitely many premises)
  Applications: non-standard models of arithmetic; "overspill" arguments

LÖWENHEIM-SKOLEM THEOREMS:
  Downward: if Σ has infinite model, has countable model
  Upward: if Σ has infinite model, has model of every infinite cardinality
  Implication: FOL cannot characterize uncountable structures (real numbers are not
    categorically axiomatizable in FOL — any FOL theory with infinite model has a
    countable model that satisfies the same sentences)
  Skolem's paradox: ZFC (which proves uncountable sets exist) has a countable model!
    Resolution: "uncountable" is relative to the model; inside the model, no bijection exists;
    outside the countable model, a bijection exists that the model can't see

UNDECIDABILITY OF FOL (Church-Turing 1936):
  No algorithm decides whether an arbitrary FOL sentence is valid
  Contrast: propositional logic is decidable (DPLL/CDCL; coNP-complete)
  Semi-decidable: if valid, proof search will eventually find it; if not, may loop
  TCS bridge: FOL validity ≡ Halting Problem in undecidability class (Σ₁ complete)
```

---

## 3. Modal Logic

### Basic Modal Operators

```
□ (box/necessity): "it is necessarily the case that"
◇ (diamond/possibility): "it is possibly the case that"
◇φ ≡ ¬□¬φ (what is possible is not necessarily not the case)
□φ ≡ ¬◇¬φ

KRIPKE SEMANTICS (possible worlds):
  Frame: ⟨W, R⟩ where W = set of possible worlds, R = accessibility relation
  Model: M = ⟨W, R, V⟩ where V assigns propositions to sets of worlds
  M, w ⊨ □φ iff for all v with wRv, M, v ⊨ φ
  M, w ⊨ ◇φ iff for some v with wRv, M, v ⊨ φ
```

### Modal Axiom Systems

```
MODAL SYSTEMS characterized by properties of accessibility relation R:

  K (no constraints on R):
    □(φ → ψ) → (□φ → □ψ)  [K axiom: distribution]
    Base system; all modal logics extend K

  T (reflexive: wRw for all w):
    □φ → φ  [T axiom: what is necessary is actual]
    "If necessarily P, then actually P" — reasonable for epistemic/alethic modality

  B (symmetric: wRv → vRw):
    φ → □◇φ  [B axiom: what is actual is necessarily possible]

  S4 (reflexive + transitive):
    T + □φ → □□φ  [4 axiom: what is necessary is necessarily necessary]
    Models epistemic logic, provability logic

  S5 (reflexive + transitive + symmetric = equivalence relation):
    T + ◇φ → □◇φ  [5 axiom: what is possible is necessarily possible]
    Standard for alethic modality (de dicto necessity)
    All worlds accessible from all worlds; simplest frame structure

INTERPRETATIONS OF MODALITY:
  Alethic: □ = necessarily true; ◇ = possibly true
  Epistemic: □ = known; ◇ = epistemically possible (consistent with knowledge)
  Deontic: □ = obligatory; ◇ = permissible
  Temporal: □ = always true; ◇ = sometimes true
  Provability: □φ = Bew(φ) in arithmetic; S4 = Löb's provability logic

TEMPORAL LOGIC (LTL, CTL) — TCS DOMAIN:
  LTL operators: ○ (next), □ (always), ◇ (eventually), U (until)
  CTL: branching time; quantifiers over paths (AF, EF, AG, EG)
  Model checking: verify temporal logic formula against finite-state system (PSPACE for LTL)
```

---

## 4. Intuitionistic Logic

### The Constructivist Turn

```
BROUWER-HEYTING-KOLMOGOROV (BHK) INTERPRETATION:
  A proof of φ ∧ ψ = (proof of φ, proof of ψ)
  A proof of φ ∨ ψ = (left proof of φ) or (right proof of ψ) [with explicit tag]
  A proof of φ → ψ = function taking proof of φ to proof of ψ
  A proof of ∀x.φ(x) = function taking x to proof of φ(x)
  A proof of ∃x.φ(x) = (witness a, proof of φ(a))
  A proof of ⊥ = none (cannot prove falsity)
  A proof of ¬φ = proof of φ → ⊥

KEY DIFFERENCE FROM CLASSICAL LOGIC:
  Excluded middle (φ ∨ ¬φ): NOT provable in general!
    Why: no constructive proof — you'd need to produce either a proof of φ or a proof of ¬φ
    For any arbitrary proposition, you can't always do this
  Double negation elimination (¬¬φ → φ): NOT provable in general!
    Classical: ¬¬φ → φ by contradiction
    Intuitionistic: ¬¬φ means "a proof that there's no proof of ¬φ" — not the same as a proof of φ

GÖDEL-GENTZEN TRANSLATION:
  Every classical theorem translates to an intuitionistic theorem (with double negation prefix)
  Classical logic ≡ intuitionistic logic + excluded middle
  Classical proof can always be "embedded" in intuitionistic framework

CURRY-HOWARD ISOMORPHISM:
  Propositions ↔ Types
  Proofs       ↔ Terms/Programs
  Propositional logic ↔ Simply typed lambda calculus (STLC)
  Predicate logic    ↔ Dependent type theory (Π-types, Σ-types)
  Modal logic        ↔ Various type theories (comonadic, monadic)
  Intuitionistic logic: the "right" logic for constructive math and type theory
  Classical logic + Curry-Howard: control operators (call/cc = Peirce's law)

  CONSEQUENCES FOR PROOF ASSISTANTS:
    Coq, Agda, Lean: based on intuitionistic dependent type theory (CIC/MLTT)
    To use excluded middle or classical axioms: explicitly import Classical module
    Proofs in intuitionistic type theory = verified programs
    Extracting code from Coq proofs: turns proof of ∃x.P(x) into program producing x
```

---

## 5. Proof Theory and Gödel's Incompleteness

### Arithmetic and Formal Systems

```
PEANO ARITHMETIC (PA):
  Language: 0, S (successor), +, ×, = over natural numbers
  Axioms: zero not successor of any number; S injective; induction schema;
    recursive definitions of + and ×
  PA is consistent (we believe; can prove consistency in stronger systems)
  PA is strong enough to express "this sentence is not provable in PA"

GÖDEL NUMBERING:
  Assign a natural number to each symbol, formula, and sequence of formulas
  Symbols: 1→'0', 2→'S', 3→'+', ... (any injective coding)
  Formula: encode as product of primes: if formula uses symbols s₁,...,sₙ:
    ⌈φ⌉ = 2^s₁ × 3^s₂ × 5^s₃ × ... (unique by fundamental theorem of arithmetic)
  Proof: sequence of formulas; similarly encoded
  → Arithmetical relations about formulas become arithmetical relations about numbers
  Pf(x, y): number y is the Gödel number of a proof of the formula with Gödel number x
  Provable(x): ∃y Pf(x, y)
```

### The First Incompleteness Theorem

```
CONSTRUCTION OF G:
  Diagonal lemma: for any formula F(x), there is a sentence G such that
    PA ⊢ G ↔ F(⌈G⌉)
    (G says "F holds of my own Gödel number")

  Apply with F(x) = ¬Provable(x):
    G ↔ ¬Provable(⌈G⌉)
    G says: "G is not provable in PA"

PROOF:
  Case 1: PA ⊢ G
    By soundness of PA: G is true in the standard model
    G says G is not provable → contradiction with PA ⊢ G
    → If PA is consistent and sound: PA ⊬ G

  Case 2: PA ⊢ ¬G
    ¬G says G is provable
    PA proves ¬G → (if PA is ω-consistent): there is no proof of G
    → If PA is ω-consistent: PA ⊬ ¬G

  Conclusion: PA ⊬ G and PA ⊬ ¬G (assuming consistency / ω-consistency)
    → G is independent of PA; PA is incomplete

  ω-CONSISTENCY vs CONSISTENCY: Rosser's improvement (1936) only needs simple consistency,
    not ω-consistency, by using a more refined sentence

TRUE ARITHMETIC (all sentences true in ℕ): not recursively axiomatizable
  → No effective axiom system can capture all arithmetical truths
```

### Second Incompleteness Theorem

```
CON(PA): arithmetical sentence expressing "PA is consistent"
  Can be expressed in PA's language using Gödel numbering
  CON(PA) ≡ ¬Provable(⌈⊥⌉)

THEOREM: If PA is consistent, PA ⊬ CON(PA)
PROOF IDEA:
  First Incompleteness Theorem formalizes: PA ⊢ CON(PA) → G
    (if PA is consistent, then G is not provable — provable in PA itself)
  If PA ⊢ CON(PA): then PA ⊢ G → contradiction (PA ⊬ G by First Theorem)
  Therefore: PA ⊬ CON(PA)

CONSEQUENCES:
  You cannot prove the consistency of arithmetic using only arithmetic
  Hilbert's Program (prove math consistent using finitary methods within math): impossible
  Relative consistency: can prove Con(PA) in stronger systems (ZFC, PA + Con(PA), etc.)
  Ordinal analysis: Gentzen proved Con(PA) using transfinite induction up to ε₀
    (beyond arithmetical induction; uses the first ordinal PA can't reach by recursion)

COMMON MISUNDERSTANDINGS:
  "Gödel proves math is broken": No. ZFC is sufficient for all of ordinary mathematics.
    The independent sentences G are mathematically unnatural (self-referential)
  "We can't know anything for sure": PA is sound; G is TRUE; we just can't prove it in PA
  "AI can never be as smart as humans" (Lucas-Penrose): The argument doesn't work.
    A sufficiently powerful AI system would be subject to its own Gödel sentences too.
    The argument conflates proof-within-a-system with human mathematical intuition.
```

---

## 6. Automated Reasoning

```
RESOLUTION (Robinson 1965):
  Ground for SAT; lifted for FOL
  CNF required; unification for FOL
  Refutation complete: if Σ ⊨ φ, can prove ⊥ from Σ ∪ {¬φ} by resolution
  Not complete for finding proofs; complete for refutation
  PROLOG: backward-chaining Horn clause resolution

SAT SOLVERS:
  Davis-Putnam-Logemann-Loveland (DPLL): backtracking + unit propagation
  CDCL (Conflict-Driven Clause Learning): DPLL + clause learning from conflicts
    State-of-the-art; solves millions-variable SAT in practice
  SMT (Satisfiability Modulo Theories): SAT + background theories (linear arithmetic, arrays, bitvectors)
    Z3 (Microsoft), CVC5, Yices: used in program verification, symbolic execution

FIRST-ORDER THEOREM PROVERS:
  Resolution-based: Vampire, E, Prover9
  Tableau: semantic tableau; methodical; Lean 4's metaprogramming
  Higher-order: Leo-III, Satallax (HOL provers)

PROOF ASSISTANTS vs AUTOMATED PROVERS:
  Automated: find proofs automatically; limited expressiveness; no user direction
  Interactive (proof assistant): user guides proof; verifies each step mechanically
    Coq, Lean, Isabelle/HOL, Agda, TLAPS (TLA+)
    Fully formal verification: every step checked; no "obvious" steps skipped
    Compcert (verified C compiler), seL4 (verified OS kernel), Lean 4 mathlib
```

---

## Decision Cheat Sheet

| Logic | Key Feature | Application |
|-------|------------|-------------|
| Classical PL | Truth-functional; decidable (SAT NP-complete) | Circuit design; boolean reasoning |
| FOL | Quantifiers; undecidable validity; complete | Spec languages; automated provers |
| Modal S5 | Alethic necessity/possibility over all possible worlds | Formal ontology; knowledge logic |
| Modal S4 | Transitive necessity; not symmetric | Provability logic; intuitionistic semantics |
| Temporal LTL | Linear time; □, ◇, U operators | Software model checking |
| Intuitionistic | Constructive; no excluded middle | Type theory; proof assistants |
| Description Logic | OWL-DL; tractable fragments of FOL | Semantic web; knowledge graphs |

---

## Common Confusion Points

**Classical logic's material conditional is counterintuitive:** "If it rains, I'll bring an umbrella" — false only when it rains and I don't bring umbrella. In classical logic, the conditional is also "true" on all sunny days regardless. This is not how we reason about conditionals in real life. Relevance logic and conditional logic address this, but for formal purposes, the material conditional works.

**Completeness ≠ Decidability:** FOL is complete (every valid formula is provable) but undecidable (no algorithm to check validity). PL is decidable (truth tables). These are different properties. Completeness is about the proof system reaching all truths; decidability is about the computational complexity of verification.

**Gödel's G is true but not provable in PA:** "True" here means true in the standard model ℕ. There are non-standard models of PA where G is false (and hence the axioms are consistent). This is the full picture: G is independent of PA; its truth value depends on which model you're in.

**Curry-Howard doesn't make all types propositions:** The correspondence says: types ↔ propositions, terms ↔ proofs. Not every type in a real programming language has a clear propositional reading. The isomorphism is cleanest in simply typed or dependently typed calculi designed for it. Rust's type system has some correspondences but is not a proof assistant.

**Modal logic S4 ≠ S5:** S5 collapses the accessibility relation to an equivalence relation — all worlds see all other worlds. S4 only has transitivity + reflexivity. S5 is the right system for absolute metaphysical necessity; S4 is right for provability. Using the wrong system leads to wrong conclusions about what's necessarily necessary.
