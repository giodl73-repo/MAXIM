# Gödel's Incompleteness Theorems

## The Big Picture

The two incompleteness theorems (1931) are the most profound results in the foundations of
mathematics. They place absolute limits on what formal systems can prove about themselves.
Every sufficiently strong consistent formal system is incomplete — and cannot prove its own
consistency.

```
+-------------------------------------------------------------------+
|                 GODEL'S RESULTS IN CONTEXT                        |
|                                                                   |
|  Godel Completeness (1929):     FOL proof system is complete.     |
|  Godel Incompleteness (1931):   PA is incomplete.                 |
|                                                                   |
|  TIMELINE OF FOUNDATIONAL RESULTS                                 |
|  +-----------------------------------------------------------+    |
|  | 1900  Hilbert's program: axiomatize all math, prove       |    |
|  |        consistency by finitary means.                     |    |
|  | 1902  Russell's Paradox: naive set theory is inconsistent.|    |
|  | 1910  Principia Mathematica: type theory to fix paradox.  |    |
|  | 1929  Godel Completeness: FOL is complete.                |    |
|  | 1931  Godel Incompleteness I: G is undecidable in PA.     |    |
|  | 1931  Godel Incompleteness II: PA cannot prove Con(PA).   |    |
|  | 1936  Church-Turing: FOL validity is undecidable.         |    |
|  | 1936  Tarski: Truth is undefinable within the system.     |    |
|  | 1963  Cohen: CH is independent of ZFC (completing ZF).    |    |
|  +-----------------------------------------------------------+    |
|                                                                   |
|  WHAT THEY REQUIRE              WHAT THEY CONCLUDE                |
|  +----------------------+       +---------------------------+     |
|  | T is consistent      |       | T is incomplete (G1)      |     |
|  | T is recursively     |       | T cannot prove Con(T)(G2) |     |
|  |  axiomatizable       |       |                           |     |
|  | T interprets         |       |                           |     |
|  |  Robinson Arithmetic |       |                           |     |
|  +----------------------+       +---------------------------+     |
+-------------------------------------------------------------------+
```

---

## Setup: What is Required

### Formal Systems in Scope

The theorems apply to any formal system T such that:
1. **Consistent**: T does not prove bot (contradiction).
2. **Recursively axiomatizable**: There is an algorithm that recognizes axioms of T.
3. **Sufficiently strong**: T can interpret Robinson Arithmetic (Q) — a very weak system.

This is a very broad class. It includes:
- Peano Arithmetic (PA)
- ZFC set theory
- ZFC + large cardinals
- Any reasonable foundation for mathematics

Systems *not* in scope: propositional logic (too weak), Presburger arithmetic (not strong
enough to interpret Q, and it is decidable).

### Gödel Numbering

The key technical trick: encode formulas and proofs as natural numbers.

```
  GODEL NUMBERING:

  Assign each symbol a unique number:
    0 -> 1, s -> 2, + -> 3, * -> 4, = -> 5, ( -> 6, ) -> 7,
    neg -> 8, land -> 9, lor -> 10, -> -> 11, Forall -> 12, ...
    Variable_n -> prime(n)

  Formula as sequence of symbols -> encode sequence as product of primes:
    [a1, a2, ..., ak] -> 2^a1 * 3^a2 * 5^a3 * ... * p_k^ak

  This is the Godel number: gn(phi)

  Key property: the mapping gn is:
    - Injective (different formulas get different numbers)
    - Computable (given phi, compute gn(phi))
    - "Invertible" (given a number, test if it codes a formula)
```

Once formulas are numbers, **predicates about proofs become number-theoretic predicates**
that can be expressed inside PA.

### Representability

A relation R(x1,...,xk) on naturals is **representable** in T if there is a formula phi such that:
```
  R(n1,...,nk)  =>  T |- phi(n1,...,nk)
  not R(n1,...,nk)  =>  T |- neg phi(n1,...,nk)
```

Key fact: all recursive (computable) functions and relations are representable in PA.

This lets us define:
```
  Proof(p, n)  =  "p is the Godel number of a proof of the formula with Godel number n"
               (this is a decidable relation, hence representable in PA)

  Provable(n)  =  Exists p. Proof(p, n)
               (this is a Sigma-1 formula in PA)
```

---

## First Incompleteness Theorem

### The Diagonal Lemma (Fixed-Point Theorem)

Before the main theorem, Gödel proved:

```
  DIAGONAL LEMMA (Godel):
  For any formula phi(x) with one free variable, there exists a sentence G such that:
    T |- G <-> phi(gn(G))

  G "talks about itself" by referring to its own Godel number.
```

This is the formalization of the Liar Paradox ("This statement is false") and the proof
machinery behind Cantor diagonalization.

### Gödel Sentence

Apply the Diagonal Lemma to phi(x) = neg Provable(x):

```
  G <-> neg Provable(gn(G))

  G says: "I am not provable (in T)."
```

### The Argument

```
  CASE 1: T |- G  (T proves G)
    Then G is provable, so Provable(gn(G)) is true.
    But G says neg Provable(gn(G)).
    So T |- neg G.
    T proves both G and neg G: T is INCONSISTENT.
    Contradiction with our assumption that T is consistent.

  CASE 2: T |- neg G  (T proves neg G)
    Then neg G is provable.
    neg G says: G is provable.
    So T |- G. Again, T proves G and neg G: INCONSISTENT.
    Contradiction.

  [Under omega-consistency, Case 2 argument is: if T |- neg G then
   T |- Exists p. Proof(p, gn(G)), so T |- Proof(0, gn(G)) or
   T |- Proof(1, gn(G)) or ..., but none of these are true.
   Rosser 1936 used a cleverer construction to get T-consistency alone.]

  CONCLUSION: G is independent of T. Neither T |- G nor T |- neg G.
              T is INCOMPLETE.
```

### Rosser's Strengthening (1936)

Rosser replaced G with a sentence that makes the argument work under plain consistency
(not omega-consistency):

```
  R <-> Forall p. (Proof(p, gn(R)) -> Exists q < p. Proof(q, gn(neg R)))

  R says: "If I have a proof, there is a shorter proof of my negation."
  This symmetry allows the argument under just T-consistency.
```

---

## Second Incompleteness Theorem

### Statement

```
  If T is consistent, then T does not prove Con(T).

  Con(T) is the sentence: neg Provable(gn(bot))
  i.e., "T cannot prove contradiction."
```

### The Argument (Sketch)

The proof of G1 (within T-meta-reasoning) can be formalized inside T:

```
  T can prove: Con(T) -> neg Provable(gn(G))

  But G <-> neg Provable(gn(G)), so:
  T can prove: Con(T) -> G

  Now if T |- Con(T), then T |- G (by modus ponens).
  But G is unprovable in T (by G1, assuming consistency).
  Contradiction.

  Therefore: T does not prove Con(T).
```

### What This Means for Hilbert's Program

```
  HILBERT'S PROGRAM (1900-1930):
    "Prove the consistency of mathematics using only finitary methods."

  GODEL G2 (1931):
    "No sufficiently strong consistent system can prove its own consistency."

  CONSEQUENCE:
    No finitary subsystem of PA can prove Con(PA).
    (Finitary = primitive recursive arithmetic PRA, which interprets Q.)
    Hilbert's program, as originally stated, is IMPOSSIBLE.

  GENTZEN'S CONSISTENCY PROOF (1936):
    PA is consistent — provable using transfinite induction up to epsilon_0.
    This is valid, but requires epsilon_0-induction which PA cannot prove.
    It doesn't contradict G2: it uses a principle stronger than PA.
```

---

## What Gödel Did Not Say

Common misreadings, corrected:

```
  MYTH: "There are truths mathematics can never prove."
  FACT: G is unprovable in T, but provable in T + Con(T), or in stronger systems.
        From outside T, we can prove G. There is no absolute unprovability.

  MYTH: "Human minds can do things computers cannot."
  FACT: This (Lucas/Penrose argument) is a philosophical extrapolation.
        It equivocates between different formal systems. Most logicians reject it.

  MYTH: "Any statement is either provable or unprovable."
  FACT: Incompleteness says some specific sentences are independent.
        Most mathematical statements are provable or refutable in PA.

  MYTH: "Godel showed math is inconsistent."
  FACT: Godel showed consistent systems are incomplete.
        The two conditions (consistent, complete) cannot both hold for strong systems.
        Inconsistent systems are trivially "complete" (they prove everything).

  MYTH: "G is a weird self-referential trick, not real mathematics."
  FACT: After Cohen (1963), natural mathematical statements like CH are
        independent of ZFC. Incompleteness is about real mathematics.
```

---

## Tarski's Undefinability Theorem

A companion result (Tarski 1936):

```
  TARSKI UNDEFINABILITY:
  There is no formula True(x) in the language of PA such that for all sentences phi:
    PA |- True(gn(phi))  iff  phi is true in the standard model.

  PROOF:
  Suppose True(x) exists. By Diagonal Lemma, there exists L with:
    PA |- L <-> neg True(gn(L))
  L says "I am not true" (Liar Paradox).
  If L is true: True(gn(L)) holds, so neg True(gn(L)) holds. Contradiction.
  If L is false: neg True(gn(L)) holds, so True(gn(L)) holds. Contradiction.
  So no such True(x) can exist.
```

**Consequence**: A formal system cannot define its own truth predicate. Truth requires
a meta-language (Tarski's hierarchy of object/meta/meta-meta languages).

This is why programming languages need external type systems or reflection with care:
a language cannot fully describe its own semantics within itself.

---

## Löb's Theorem

A further result that shows how little provability can say about truth:

```
  LOB'S THEOREM:
  If T |- (Provable(gn(phi)) -> phi), then T |- phi.

  Equivalently: T cannot "trust its own provability predicate" without actually proving.
  The hypothesis "if this is provable then it is true" is only provable when phi is provable.

  CONTRAST WITH G2:
  G2: T cannot prove Con(T) = neg Provable(gn(bot))
  Lob: T cannot prove Provable(gn(phi)) -> phi unless phi is already provable.
```

---

## Arithmetic Hierarchy Perspective

Incompleteness has a computability-theoretic reading you know from TCS:

```
  ARITHMETIC HIERARCHY POSITIONS:

  phi is Sigma-1:    Exists x. R(x) where R is decidable.
                     Equivalent: phi is semi-decidable / recursively enumerable.

  phi is Pi-1:       Forall x. R(x). Negation of Sigma-1.

  phi is Delta-1:    Both Sigma-1 and Pi-1. Equivalent: decidable.

  Provable(n) is Sigma-1  (there exists a proof of n).
  Con(T) = neg Provable(gn(bot)) is Pi-1.

  The Godel sentence G = neg Provable(gn(G)) is Pi-1.

  KEY:
    Sigma-1 truths: T can prove them (if true, a proof exists and T can exhibit it).
    Pi-1 truths:    T may not be able to prove them.
    G is a Pi-1 sentence that is true (in the standard model) but unprovable.
```

This connects to Rice's theorem and the halting problem:
- Halting problem = Pi-1 sentence about a Turing machine.
- "T is consistent" = Pi-1 sentence.
- Both are true but unprovable in T.

---

## Concrete Independent Statements

After Gödel, are there "natural" independent statements?

| Statement | Independent of |
|-----------|----------------|
| Continuum Hypothesis (CH) | ZFC (Gödel 1938, Cohen 1963) |
| Axiom of Choice (AC) | ZF (Gödel 1938, Cohen 1963) |
| Suslin's Hypothesis | ZFC |
| Paris-Harrington (PH) Theorem | PA (Paris-Harrington 1977) |
| Goodstein Sequences termination | PA (Kirby-Paris 1982) |
| Friedman's TREE(n) termination | PA (much more) |

Paris-Harrington and Goodstein are remarkable: they look like ordinary combinatorial
statements about natural numbers, but they transcend PA. TREE(3) is a tower of towers
beyond comprehension in height.

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| What does G1 say? | Every consistent, recursively axiomatizable, sufficiently strong T is incomplete. |
| What does G2 say? | Such T cannot prove Con(T). |
| What's the Gödel sentence? | G <-> neg Provable(gn(G)): "I am not provable." |
| What is Gödel numbering? | Encoding formulas/proofs as natural numbers. |
| Can G be proved in a stronger system? | Yes — G is provable in T + Con(T). |
| Does G2 prove PA is inconsistent? | No — it says PA cannot prove its own consistency. |
| What is Tarski undefinability? | No formula in PA can serve as its own truth predicate. |
| What is Löb's theorem? | T |- Box phi -> phi only when T |- phi. |

---

## Common Confusion Points

**G1 vs G2 vs Gödel completeness (1929).**
Three theorems, often confused.
- Completeness (1929): FOL proof system is complete. Every FOL tautology is provable.
- G1 (1931): PA is incomplete. There are true PA sentences that PA cannot prove.
- G2 (1931): PA cannot prove Con(PA).

**"Independent of T" vs "false."**
G is independent of T (neither provable nor refutable). In the standard model of arithmetic,
G is TRUE. It is only "undecidable" within T, not unknown or unknowable absolutely.

**Omega-consistency vs. consistency.**
Original G1 required omega-consistency (T doesn't prove Exists x. phi(x) while refuting
all phi(0), phi(1), phi(2),...). Rosser's 1936 strengthening needs only consistency.

**What "sufficiently strong" means.**
Robinson Arithmetic (Q) is the minimal system needed: it can represent all computable
functions, which is what the proof requires. Presburger arithmetic (add, no multiply) is
NOT strong enough — it is decidable and complete, so incompleteness doesn't apply.
