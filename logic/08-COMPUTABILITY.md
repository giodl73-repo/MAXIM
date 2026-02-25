# Logic and Computability: Undecidability

## The Big Picture

Computability theory and mathematical logic are the same subject viewed from two angles.
The undecidability of FOL validity (Church-Turing 1936) and the incompleteness of PA
(Gödel 1931) are two facets of the same phenomenon: the halting problem. The arithmetic
hierarchy stratifies the degrees of undecidability.

```
+-------------------------------------------------------------------+
|           LOGIC AND COMPUTABILITY: THE CONNECTION                 |
|                                                                   |
|  COMPUTABILITY THEORY        LOGIC                                |
|  +--------------------+      +----------------------------+       |
|  | Turing machines    | <--> | Formal proof systems       |       |
|  | Decidable          | <--> | Recursive sets             |       |
|  | Semi-decidable     | <--> | Recursively enumerable     |       |
|  | Undecidable        | <--> | Not RE or not co-RE        |       |
|  | Rice's theorem     | <--> | Undecidability of props.   |       |
|  | Halting problem    | <--> | FOL validity undecidable   |       |
|  +--------------------+      +----------------------------+       |
|                                                                   |
|  ARITHMETIC HIERARCHY                                             |
|  +-----------------------------------------------------------+    |
|  | Sigma-0 = Pi-0 = Delta-1 = Recursive (decidable)          |    |
|  | Sigma-1 = RE (semi-decidable)                             |    |
|  | Pi-1 = co-RE                                              |    |
|  | Sigma-n, Pi-n for all n: the analytical hierarchy         |    |
|  | True arithmetic: not in any Sigma-n                       |    |
|  +-----------------------------------------------------------+    |
+-------------------------------------------------------------------+
```

---

## The Church-Turing Thesis

The foundational identification:

```
  CHURCH-TURING THESIS:
  Every effectively computable function is computable by a Turing machine.

  "Effective computability" = intuitively algorithmic = Turing-computable.

  This is a THESIS, not a theorem. It identifies an informal notion with a
  formal one. It has been confirmed by:
  - Lambda calculus (Church 1936) computing the same class
  - General recursive functions (Herbrand-Gödel) computing the same class
  - Register machines, RAM models, string rewriting systems — all equivalent
  - No counterexample in 90 years of computing
```

---

## The Halting Problem

```
  HALTING PROBLEM:
  Given a Turing machine M and input w, does M halt on w?

  HALTING = {(M, w) : M halts on input w}

  UNDECIDABILITY PROOF (Turing 1936):
  Assume for contradiction that HALT is decidable by H.

  Build D:
    D(M):
      if H(M, M) says "halts": loop forever
      if H(M, M) says "does not halt": halt

  What does D(D) do?
    H(D, D) says "halts" => D(D) loops forever. Contradiction.
    H(D, D) says "does not halt" => D(D) halts. Contradiction.

  Therefore H cannot exist. HALT is undecidable.
```

The diagonalization argument is exactly Gödel's construction in proof-theoretic form:
D is the computational analog of the Gödel sentence G = neg Provable(G).

---

## Church's Theorem: FOL Validity Is Undecidable

```
  CHURCH'S THEOREM (1936):
  The set of valid FOL sentences (tautologies) is not decidable.

  Equivalently: FOL satisfiability is not decidable.

  PROOF SKETCH (Reduction from Halting Problem):
  Given M and w, construct a FOL sentence phi_{M,w} such that:
    phi_{M,w} is valid  iff  M halts on w.

  The construction encodes:
    - Tape contents as sequences of symbols
    - Head position as a number
    - State transitions as FOL axioms
    - "M halts" as a FOL sentence

  Since HALT is undecidable, FOL validity is undecidable.

  SEMI-DECIDABILITY:
  FOL validity IS semi-decidable (recursively enumerable):
  If phi is valid, a proof exists (Godel completeness), and we can
  enumerate all proofs to find it. If phi is not valid, we may run forever.
```

---

## Tarski-Vaught and Decidable FOL Fragments

FOL is undecidable overall but specific theories are decidable:

```
  DECIDABILITY OF SPECIFIC THEORIES (revisited):

  Theory of real closed fields (Tarski):    DECIDABLE
    Proof: quantifier elimination (every formula equivalent to QF formula)
    Algorithm: Cylindrical Algebraic Decomposition

  Presburger arithmetic (N, 0, 1, +):      DECIDABLE (2EXP)
    Proof: quantifier elimination with divisibility predicates.

  Theory of Boolean algebras:               DECIDABLE
  Theory of linear orders:                  DECIDABLE

  Peano arithmetic (N, 0, s, +, *):         UNDECIDABLE
    Proof: can interpret all of FOL / encode Turing machines.

  ZFC set theory:                           UNDECIDABLE

  DECIDABLE FRAGMENTS OF FOL:
  +------------------+------------------+------------------+
  | Fragment         | Decidability     | Notes            |
  +------------------+------------------+------------------+
  | Propositional    | PSPACE           | No quantifiers   |
  | Monadic (no func)| DECIDABLE        | Lowenheim 1915   |
  | 2-variable (FO2) | NEXPTIME         | Two vars only    |
  | Guarded fragment | EXPTIME          | Modal basis      |
  | DL (ALC)         | EXPTIME          | Modal + TBox     |
  | Horn clause FOL  | Undecidable      | But useful       |
  +------------------+------------------+------------------+
```

---

## The Arithmetic Hierarchy

Stratifying complexity of logical definability:

### Definitions

```
  A relation R(x) on natural numbers is:

  Sigma-0 = Pi-0 = Delta-1:
    Decidable (recursive). Algorithm exists.

  Sigma-1:
    Exists y. R'(x, y) where R' is decidable.
    Equivalent: recursively enumerable (RE).
    Semi-decidable: if R(x), we can confirm it (enumerate y).
    Examples: HALT, validity of FOL sentences.

  Pi-1:
    Forall y. R'(x, y) where R' is decidable.
    Equivalent: co-RE (complement of RE).
    Semi-decidable from below: if NOT R(x), we can confirm it.
    Examples: TOTALITY (does M halt on all inputs?), consistency of PA.

  Delta-2 = Sigma-1 intersect Pi-1:
    Both RE and co-RE => decidable? NO! Delta-1 = RE inter co-RE = decidable.
    Wait: Delta-1 = recursive, Delta-2 = Turing degree 0' (halting oracle).

  Sigma-2:
    Exists y. Forall z. R'(x,y,z).
    Higher level: RE relative to the halting oracle.
    Example: "M is total" (halts on all inputs) is Pi-2.
    Actually: TOTALITY = {M : M halts on all inputs} is Pi-2-complete.

  In general:
    Sigma-{n+1}: Exists y1. Pi-n formula
    Pi-{n+1}: Forall y1. Sigma-n formula
    Delta-n: Sigma-n intersect Pi-n
```

### Diagram

```
  ARITHMETIC HIERARCHY:

          Pi-1    Sigma-1
         /    \  /    \
     co-RE     RE     ...
         \    /
       Delta-1
       (recursive)

  Sigma-2
  Pi-2
  Sigma-3
  Pi-3
  ...

  True Arithmetic Th(N) = all true sentences of PA:
  Not in any Sigma-n (Tarski undefinability of truth).
  Degree: 0^(omega) (omega-th jump of the halting problem).
```

### Key Examples

| Statement | Position |
|-----------|----------|
| M halts on w (HALT) | Sigma-1-complete |
| M does NOT halt on w | Pi-1-complete |
| M halts on all inputs (TOTAL) | Pi-2-complete |
| M halts on some input | Sigma-1-complete |
| T is consistent (Con(PA)) | Pi-1 (if T is RE) |
| Validity of a FOL sentence | Sigma-1-complete |
| Unsatisfiability of FOL sentence | Pi-1-complete |
| First-order theory of N | Not in any Sigma-n |

---

## Reductions and Completeness

Just as NP-completeness captures the hardest problems in NP, Sigma-1-completeness captures
the "hardest" semi-decidable problems:

```
  MANY-ONE REDUCTION (m-reduction):
  A reduces to B (A <=_m B) if there exists a computable f such that:
    x in A  iff  f(x) in B

  SIGMA-1-COMPLETE:
  B is Sigma-1-complete if:
    (1) B is Sigma-1
    (2) Every Sigma-1 set A reduces to B

  EXAMPLES:
  HALT is Sigma-1-complete (hardest semi-decidable problem)
  FOL validity is Sigma-1-complete
  Post Correspondence Problem (PCP) is Sigma-1-complete

  TURING REDUCTION (T-reduction):
  A <=_T B if A is decidable given an oracle for B.
  B <=_T A AND A <=_T B: A and B have the same Turing degree.
  The halting problem defines degree 0' ("zero-jump").
```

---

## Rice's Theorem and Its Generalizations

```
  RICE'S THEOREM (1953):
  Let P be any non-trivial semantic property of Turing machines.
  (Non-trivial: some TMs have it, some don't.
   Semantic: depends only on the function computed, not the TM description.)

  Then {M : TM M has property P} is UNDECIDABLE.

  Examples of properties covered by Rice:
  - "M halts on input 0"
  - "M computes a total function"
  - "The language of M is regular"
  - "M accepts the empty string"
  - "M accepts any string"
  - "M computes the same function as M2"

  Non-examples (syntactic, not semantic):
  - "M has exactly 5 states" (decidable, just check)
  - "M's transition table has 20 entries" (decidable)

  PROOF SKETCH:
  Assume P is decidable. We can decide HALT:
  Given (M, w), construct M' that ignores its input, simulates M on w,
  then acts like a fixed machine with property P.
  If M halts on w: M' has property P.
  If M doesn't halt: M' doesn't have P.
  Using P-decider to decide HALT. Contradiction.
```

### Rice-Shapiro Theorem (for RE languages)

```
  RICE-SHAPIRO:
  For any semi-decidable property P of RE languages:
  L(M) has property P  iff  some FINITE subset of L(M) has property P.

  This characterizes which properties of RE sets are themselves RE.
  "Contains the string 'hello'" is RE (witness: 'hello' in L(M)).
  "Is infinite" is NOT RE (no finite witness for infinity).
```

---

## Post Correspondence Problem (PCP)

Another canonical undecidable problem, useful for reductions in formal language theory:

```
  POST CORRESPONDENCE PROBLEM (PCP):
  Given a finite set of pairs (u_i, v_i) of strings:
  Does there exist a sequence i_1, i_2, ..., i_k such that:
    u_{i_1} u_{i_2} ... u_{i_k} = v_{i_1} v_{i_2} ... v_{i_k}?

  Example: pairs (ab, a), (b, ab), (c, bc)
  i_1=2, i_2=1, i_3=3: b*ab*c = ab*a*bc? No, check...

  PCP is UNDECIDABLE (Post 1946).

  APPLICATIONS (PCP as a reduction tool):
  Undecidability of ambiguity in CFGs
  Undecidability of equivalence of context-free grammars
  Undecidability of emptiness of intersection of two CFGs
```

---

## Gödel and Computability: The Same Phenomenon

```
  GODEL'S G (1931)           TURING'S D (1936)
  -------------------        -------------------
  G is true but not          HALT is true but not
  provable in PA.            decidable.

  CONSTRUCTION:              CONSTRUCTION:
  G <-> neg Provable(G)      D(M): if H(M,M)="halt" then loop,
  (diagonal on proofs)            if H(M,M)="loop" then halt.
                             (diagonal on TMs)

  PROOF:                     PROOF:
  If PA |- G: PA is          If H decides HALT: D(D) contradicts H.
  inconsistent.

  COMMON STRUCTURE:
  Both use self-reference (diagonalization).
  Both show: no system can fully "see" its own behavior.
  The Godel sentence = the halting problem for PA's provability relation.
```

### Precise Formulation

```
  PROVABILITY AS SIGMA-1 PREDICATE:
  Provable_PA(n) is Sigma-1: "exists a proof of sentence n."
  This is RE: if phi is provable, we can find the proof by enumeration.

  GODEL'S G is Pi-1: "no proof exists for me" = Forall p. not Proof(p, G).
  Pi-1 sentences can be true but unprovable (like non-halting witnesses).

  CONSISTENCY of PA, Con(PA) = neg Provable_PA(gn(bot)):
  This is Pi-1. It is true (PA is consistent) but unprovable in PA.
  Exactly analogous to: "this TM does not halt" (Pi-1, can be true but
  unverifiable from within the system).
```

---

## Oracles and the Turing Hierarchy

```
  ORACLE TURING MACHINES:
  A TM M^A has an oracle tape; querying A costs one step.
  M^HALT = TM with access to halting oracle.

  JUMP OPERATOR:
  A' = HALT^A = {e : e in W_e^A}  (halting relative to oracle A)

  DEGREES:
  0 = degree of decidable sets (no oracle needed)
  0' = degree of HALT (one halting oracle)
  0'' = degree of HALT^HALT (two halting oracles)
  ...
  0^(omega) = degree of True Arithmetic

  ARITHMETICAL HIERARCHY DEGREES:
  Sigma-1-complete problems all have degree 0'.
  Sigma-2-complete problems have degree 0''.
  True Arithmetic has degree 0^(omega).
```

---

## Decision Cheat Sheet

| I want to... | Answer |
|---|---|
| Is FOL satisfiability decidable? | No. Semi-decidable (Sigma-1-complete). |
| Is FOL validity decidable? | No. Semi-decidable (Sigma-1-complete). |
| What is Rice's theorem? | No non-trivial semantic property of TMs is decidable. |
| Where does HALT sit in the hierarchy? | Sigma-1-complete (= RE-complete). |
| Where does "M is total" sit? | Pi-2-complete. |
| What is the Godel-Turing connection? | Diagonalization: same construction, different domains. |
| Is consistency of PA decidable? | No. Con(PA) is Pi-1, true but unprovable in PA. |
| What fragments of FOL are decidable? | Monadic, Presburger, RCF, guarded, 2-variable. |

---

## Common Confusion Points

**Semi-decidable vs. decidable.**
Semi-decidable (RE): if the answer is yes, we eventually say yes. If no, we might run forever.
Decidable: we always halt with yes or no. HALT is semi-decidable. TOTAL ("M halts on all
inputs") is NOT semi-decidable (it's Pi-2).

**Rice's theorem requires "semantic."**
"M has 5 states" is syntactic and decidable. "M computes a total function" is semantic
and undecidable (Rice). The distinction is: does the property depend only on what M
computes, or on the description of M?

**Church's theorem vs. Gödel's theorems.**
Church (1936): FOL validity is undecidable.
Gödel G1 (1931): PA is incomplete.
Gödel G2 (1931): PA cannot prove its own consistency.
These are related but distinct results. Church showed undecidability of the decision problem.
Gödel showed incompleteness of specific axiom systems.

**The arithmetic hierarchy is infinite.**
There are Sigma-n-complete problems for every n, and none of them are in Sigma_{n-1} or
Pi_{n-1}. The hierarchy is strict. True arithmetic is not in any level.
