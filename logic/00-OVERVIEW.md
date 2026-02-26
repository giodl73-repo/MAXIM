# Logic — Landscape and Taxonomy

## The Big Picture

Logic is the formal study of **valid inference**. The field spans formal systems from Boolean
algebra all the way to Gödel's incompleteness results that place hard limits on what any
consistent system can prove.

```
+-------------------------------------------------------------------+
|                    THE LOGIC LANDSCAPE                            |
|                                                                   |
|  CLASSICAL LOGICS              NON-CLASSICAL LOGICS               |
|  +----------------------+      +----------------------------+     |
|  | Propositional (PL)   |      | Modal (K, S4, S5, GL)      |     |
|  | (Boolean / Zeroth    |      | Temporal (LTL, CTL, CTL*)  |     |
|  |  Order)              |      | Intuitionistic             |     |
|  |                      |      | Paraconsistent             |     |
|  | First-Order (FOL)    |      | Fuzzy / Many-valued        |     |
|  | (Predicate Logic)    |      | Description Logics         |     |
|  |                      |      | Linear / Relevance         |     |
|  | Second-Order (SOL)   |      +----------------------------+     |
|  | Higher-Order         |                                         |
|  +----------------------+                                         |
|                                                                   |
|  PROOF THEORY                  MODEL THEORY                       |
|  +----------------------+      +----------------------------+     |
|  | Natural Deduction    |      | Tarski Semantics           |     |
|  | Sequent Calculus     |      | Completeness (Godel '29)   |     |
|  | Hilbert Systems      |      | Compactness                |     |
|  | Resolution           |      | Lowenheim-Skolem           |     |
|  +----------------------+      +----------------------------+     |
|                                                                   |
|  COMPUTABILITY / LIMITS                                           |
|  +-----------------------------------------------------------+    |
|  | Decidability  Completeness  Incompleteness (Godel '31)    |    |
|  | Halting Problem  Arithmetical Hierarchy  Rice's Theorem   |    |
|  +-----------------------------------------------------------+    |
|                                                                   |
|  APPLICATIONS                                                     |
|  +-----------------------------------------------------------+    |
|  | Program Verification  Model Checking  SAT / SMT           |    |
|  | Type Theory  Curry-Howard  Dependent Types (Lean, Coq)    |    |
|  | AI Reasoning  Knowledge Representation  Description Logic |    |
|  +-----------------------------------------------------------+    |
+-------------------------------------------------------------------+
```

---

## Field Taxonomy by Expressiveness

The classical hierarchy, weakest to strongest:

```
WEAKEST ─────────────────────────────────────────────── STRONGEST

Propositional   First-Order     Second-Order    Higher-Order
   (PL)           (FOL)           (SOL)            (HOL)

Variables:      Variables:      Variables:       Variables:
Boolean only    Objects in      Objects +        Objects +
                domain          sets of          sets of sets,
                                objects          etc.

Quantifiers:    Quantifiers:    Quantifiers:     Quantifiers:
None            Forall x,       ForallP,         Over any
                Exists y over   ExistsR over     type
                objects         sets/relations

Decidable:      Decidable:      Decidable:       Decidable:
Yes             No (semi-dec)   No               No

Complete:       Complete:       Complete:        Complete:
Yes (trivially) Yes             No               No
                (Godel 1929)    (Godel 1931
                                 consequence)
```

The jump from PL to FOL adds **quantifiers over a domain**. The jump from FOL to SOL adds
**quantification over predicates** — that is where full incompleteness kicks in.

---

## Anatomy of a Logic

Every logic has the same basic structure:

```
+----------------------------------------------------------+
|                    ANATOMY OF A LOGIC                    |
|                                                          |
|  SYNTAX                   SEMANTICS                      |
|  +----------------+       +--------------------------+   |
|  | Language       |       | Interpretation / Model   |   |
|  | (alphabet,     | ====> | (what the symbols mean)  |   |
|  |  formulas)     |       |                          |   |
|  +----------------+       +--------------------------+   |
|          |                            |                  |
|          v                            v                  |
|  PROOF SYSTEM              TRUTH DEFINITION              |
|  +----------------+       +--------------------------+   |
|  | Axioms         |       | M |= phi                 |   |
|  | + Rules        |       | (formula phi is true in  |   |
|  | |- phi          |       |  model M)                |   |
|  +----------------+       +--------------------------+   |
|          |                            |                  |
|          +──────────┐  ┌─────────────+                  |
|                     v  v                                 |
|              SOUNDNESS / COMPLETENESS                    |
|        |- phi  iff  |= phi  (for classical logics)       |
+----------------------------------------------------------+
```

Core vocabulary:

| Term | Meaning |
|------|---------|
| **Tautology** | True in every interpretation |
| **Satisfiable** | True in at least one interpretation |
| **Contradiction** | False in every interpretation |
| **Valid argument** | If premises true, conclusion must be true |
| **Sound proof system** | Only proves true things (|- phi => |= phi) |
| **Complete proof system** | Proves all true things (|= phi => |- phi) |
| **Decidable theory** | Algorithm exists to check |= phi |
| **Consistent** | No contradiction |- bot is derivable |

---

## The Expressiveness vs. Decidability Tradeoff

The fundamental tension in logic:

```
MORE EXPRESSIVE ────────────────────────────────────────►

   PL           FOL          SOL          HOL
   Low          Medium        High         Very High

LESS DECIDABLE ────────────────────────────────────────►

   PL           FOL           SOL          HOL
   Yes          Semi-dec.     No           No
  (DPLL, BDD)  (Sigma1-complete
                for validity)

COMPLETENESS (proof system proves all truths):
   PL           FOL           SOL          HOL
   Yes          Yes           No           No
               (Godel 1929)  (Godel 1931 forces this)
```

FOL is the sweet spot: expressive enough for most mathematics, complete proof system, and
satisfiability is only semi-decidable (not fully decidable, but provability is enumerable).

---

## Proof vs. Truth Duality

```
  SYNTACTIC WORLD               SEMANTIC WORLD
  (proof-theoretic)             (model-theoretic)
  -----------------             ----------------
  Derivations                   Interpretations
  |- (turnstile)                |= (double turnstile)
  "is provable"                 "is true"
  Hilbert / Gentzen             Tarski

  Rules are mechanical.         Truth requires a model.
  String rewriting.             Set-theoretic definitions.

  ─────────────────────────────────────────────────────
  BRIDGE: Soundness and Completeness theorems
  (Godel 1929 for FOL: |- phi  iff  |= phi)
  ─────────────────────────────────────────────────────
```

Gödel's completeness theorem (1929) — distinct from the incompleteness theorems (1931) — says
syntactic derivability and semantic truth coincide in FOL. The incompleteness theorems then
show this nice situation fails for second-order arithmetic.

---

## The MIT TCS Connection

You know automata, formal languages, and computability. Logic is the other side of the coin:

```
AUTOMATA / FORMAL LANGUAGES        LOGIC

DFA / NFA                    <---> Propositional logic (both decidable)
Context-free grammars        <---> Certain FOL decidable fragments
Turing machines              <---> Provability in formal systems
Rice's theorem               <---> Undecidability of properties
Chomsky hierarchy            <---> Arithmetic hierarchy (Sigma-n, Pi-n)
Regular languages            <---> Star-free <---> FO[<] (McNaughton-Papert)
Push-down automata           <---> Second-order logic fragment (MSO on trees)
```

The Curry-Howard correspondence then maps proofs to programs and types to propositions. Your
lambda calculus background connects directly to natural deduction in Module 03 and to
dependent type theory in Module 09.

---

## Guide Map

| File | Topic | Key Results |
|------|-------|-------------|
| 01-PROPOSITIONAL.md | Boolean logic, truth tables, normal forms | SAT, DPLL, BDDs, Resolution |
| 02-PREDICATE.md | FOL syntax, semantics, quantifiers | Tarski truth, unification |
| 03-PROOF-THEORY.md | Natural deduction, sequent calculus | Cut elimination, normalization |
| 04-GODEL.md | Incompleteness theorems | Gödel 1931, Tarski, Löb |
| 05-MODEL-THEORY.md | Models, completeness, compactness | Gödel 1929, Löwenheim-Skolem |
| 06-MODAL-LOGIC.md | Kripke semantics, possible worlds | K, S4, S5, GL axiom systems |
| 07-TEMPORAL-LOGIC.md | LTL, CTL, CTL*, model checking | State explosion, symbolic MC |
| 08-COMPUTABILITY.md | Undecidability via logic | Halting, arithmetic hierarchy |
| 09-APPLICATIONS.md | Verification, SAT/SMT, type theory | Z3, Lean, Coq, Curry-Howard |

---

## Decision Cheat Sheet

| Use this logic / tool when... | What / where | Notes |
|-------------------------------|-------------|-------|
| You need a decidable Boolean constraint solver (SAT, circuit verification) | Propositional logic → 01-PROPOSITIONAL.md | DPLL/CDCL solvers; NP-complete but industrially fast; basis of SMT |
| You need to quantify over a domain (all x, some x) | First-order logic (FOL) → 02-PREDICATE.md | Semi-decidable; complete proof system (Gödel 1929); sweet spot for mathematics |
| You want to understand proof as a mathematical object (cut elimination, normalization) | Proof theory → 03-PROOF-THEORY.md | Curry-Howard: proofs = programs; sequent calculus for meta-proofs |
| You need to understand exactly what Gödel proved and what it means | Incompleteness → 04-GODEL.md | Gödel 1931: no consistent r.e. extension of PA is complete; Gödel 1929: FOL proof system IS complete — these are different results |
| You need to reason about structures that satisfy a theory (non-standard models, compactness) | Model theory → 05-MODEL-THEORY.md | Compactness; Löwenheim-Skolem; ultraproducts; quantifier elimination → decidability |
| You need necessity/possibility, knowledge, provability operators | Modal logic → 06-MODAL-LOGIC.md | Kripke semantics; K/S4/S5/GL; GL is the provability logic of PA |
| You need to verify temporal properties of a finite-state system | Temporal logic + model checking → 07-TEMPORAL-LOGIC.md | LTL (path quantification) vs. CTL (branching time); symbolic model checking; SPIN/NuSMV/TLA+ |
| You want to connect logic and computability theory | Computability → 08-COMPUTABILITY.md | Halting problem via diagonalization; arithmetical hierarchy (Σₙ, Πₙ); Rice's theorem |
| You want to verify programs, use SAT/SMT, or write machine-checked proofs | Applications → 09-APPLICATIONS.md | Hoare logic; Dafny/Frama-C; Z3/CVC5; Lean 4/Coq/Isabelle; description logics |
| Expressiveness is the constraint (need to quantify over sets/relations) | Second-order / higher-order logic | Accept: no complete proof system, no compactness; gain: full mathematical expressiveness |
| Decidability is the hard constraint (e.g., automated verification must terminate) | Choose a decidable fragment: PL, Presburger arithmetic, DLO, RCF, description logics | Quantifier elimination gives decidability for specific theories |

---

## Common Confusion Points

**"Completeness" means two different things.**
Gödel completeness (1929): FOL's proof system is complete — every semantic truth is provable.
Gödel incompleteness (1931): Peano Arithmetic is incomplete — there exist truths not provable.
These are about different objects: the first is about a proof system, the second about a theory.

**"Consistent" vs "complete" for theories.**
A theory T is *consistent* if it does not prove bot. It is *complete* if for every sentence phi,
either T |- phi or T |- neg phi. Gödel 1931 says no consistent recursively axiomatizable
extension of PA can be complete.

**Syntax vs. semantics.**
Beginners conflate "provable" (|-) with "true" (|=). Soundness and completeness theorems are
precisely the results that let you move between them — and incompleteness shows the bridge breaks
for sufficiently strong theories.

**Modal vs. temporal.**
Modal logic adds box (necessarily) and diamond (possibly). Temporal logic is modal logic applied
to a time structure. LTL quantifies over paths; CTL quantifies over branching futures. Both
underlie hardware and software model checking.
