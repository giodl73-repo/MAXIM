# Theory Foundations — Turing, Church, Post

## Era Overview

```
THE FOUNDATIONS DECADE: 1928–1941
===================================

  1928 ─── HILBERT poses Entscheidungsproblem:
           "Is there a mechanical procedure to decide truth of any
           mathematical statement?" (decision problem)

  1931 ─── GÖDEL: Incompleteness theorems.
           Some true statements are unprovable within a formal system.
           First crack in Hilbert's program.

  1934 ─── CHURCH: Lambda calculus paper draft.
           Computation as function application and reduction.

  1936 ─── TURING: "On Computable Numbers" — halting problem, universal machine.
  1936 ─── CHURCH: Lambda calculus published. Church's thesis.
  1936 ─── POST: Post correspondence problem, tag systems.
           All three, independently, define the same class of computable functions.
           This is not coincidence — it is convergent discovery of a real object.

  1937 ─── TURING visits Princeton. Works with Church.
           Church-Turing thesis: the intuitive notion of "algorithm"
           equals lambda calculus equals Turing machine.

  1941 ─── TURING at Bletchley Park. Bombe machine. Enigma broken.
```

---

## Alan Turing (1912–1954)

### Bio Snapshot

Cambridge undergraduate (King's College), studied under Max Newman. PhD at Princeton under Church. Bletchley Park during WWII — designed the Bombe electromechanical device that cracked Enigma, directly shortening the war. Post-war: designed ACE computer at NPL, worked on morphogenesis. Convicted of gross indecency (homosexuality) in 1952, forced chemical castration. Died of cyanide poisoning (ruled suicide, disputed) in 1954 at 41.

### The Turing Machine

**Context**: Hilbert asked whether there is a "decision procedure" — a mechanical method that, given any mathematical statement, would determine whether it is true or false. To answer this, Turing needed a precise definition of "mechanical procedure."

```
TURING MACHINE — FORMAL DEFINITION
====================================

  A Turing Machine M = (Q, Σ, Γ, δ, q₀, q_accept, q_reject) where:

  Q         = finite set of states
  Σ         = input alphabet (does not include blank ␢)
  Γ         = tape alphabet (includes ␢; Σ ⊆ Γ)
  δ: Q × Γ → Q × Γ × {L, R}
              = transition function
              (current state, current symbol) →
              (new state, write symbol, move direction)
  q₀ ∈ Q   = start state
  q_accept  = accept state
  q_reject  = reject state (≠ q_accept)

  TAPE: infinite in both directions, divided into cells.
  HEAD: reads/writes one cell at a time, moves left or right.

  COMPUTATION:
    Start: q₀, head at leftmost input symbol, rest of tape = ␢
    Step:  apply δ to (current state, current symbol)
    Halt:  reach q_accept or q_reject
    Loop:  some inputs never halt
```

The Turing Machine is not a design for a real machine — it is the simplest possible model that captures all computable functions. The simplicity is the point: if something cannot be computed by a Turing Machine, it cannot be computed at all.

**The Universal Turing Machine (UTM)**: Turing showed that there exists a single Turing Machine U that, given the description of any Turing Machine M and input w, simulates M on w. This is the stored-program concept in its purest form: program and data on the same tape, the machine that runs machines.

```
UNIVERSAL TURING MACHINE
=========================

  Input to U:  ⟨M⟩ w
               (encoding of machine M) (input to M)

  U simulates M on w:
    - U reads ⟨M⟩ to learn M's transition table
    - U maintains a "simulated tape" for M's tape contents
    - U maintains M's current state
    - For each step: look up M's transition, execute it

  U accepts iff M accepts w.
  U rejects iff M rejects w.
  U loops iff M loops on w.

  This is literally: program = data.
  Von Neumann saw this and built it in silicon.
```

### The Halting Problem

**Theorem (Turing, 1936)**: There is no Turing Machine that decides, for arbitrary M and input w, whether M halts on w.

**Proof by contradiction (diagonalization)**:

```
HALTING PROBLEM UNDECIDABILITY
================================

  Assume HALT exists: on input ⟨M, w⟩, accepts if M halts on w,
                                        rejects if M loops on w.

  Construct D:
    D(⟨M⟩): run HALT(⟨M, ⟨M⟩⟩)
              if HALT accepts (M halts on ⟨M⟩): D loops
              if HALT rejects (M loops on ⟨M⟩): D halts

  Now ask: what does D do on input ⟨D⟩?
    HALT(⟨D, ⟨D⟩⟩) = ?
    If D halts on ⟨D⟩ → HALT accepts → D loops on ⟨D⟩    CONTRADICTION
    If D loops on ⟨D⟩ → HALT rejects → D halts on ⟨D⟩    CONTRADICTION

  Therefore HALT cannot exist. □
```

This is the same diagonal argument Cantor used to prove uncountability of the reals (1874) and that Gödel used in his incompleteness proof. Turing was explicitly aware of Cantor and Gödel.

**Why it matters for software**: Every modern language's type system, static analyzer, and program verifier is constrained by this result. You cannot write a general tool that determines whether any program will terminate — Rice's Theorem extends this: essentially no non-trivial semantic property of programs is decidable.

### The Turing Test

In "Computing Machinery and Intelligence" (1950), Turing reformulates "Can machines think?" as the imitation game: can an interrogator, via text chat, distinguish a human from a machine? He predicted that by 2000, a machine would fool a 30% success rate for 5 minutes.

The test is often misunderstood as a definition of intelligence. Turing presented it as a way to avoid philosophical deadlock about "what is consciousness." It has been criticised (Searle's Chinese Room, 1980) but remains the most-cited framing in AI philosophy.

### Bletchley and the Bombe

During WWII, Turing designed the Bombe — an electromechanical device that exploited known cribs (guesses at plaintext) to eliminate impossible Enigma settings. The key insight: Enigma never enciphered a letter as itself. This, combined with repeated stereotyped message openings ("WETTER" for weather reports), allowed the cryptanalysts to specify a constraint and have the Bombe test all 159 quadrillion settings against it, eliminating them in bulk.

This is early constraint-satisfaction search — not general computation, but an application of the same logical reduction ideas.

---

## Alonzo Church (1903–1995)

### Bio Snapshot

Princeton mathematician. PhD advisor to both Turing and Stephen Kleene. Published lambda calculus in 1936, the same year as Turing's paper. Lived to 92 — one of computing theory's longest careers.

### Lambda Calculus

Church's approach to defining computation was entirely different from Turing's: rather than a machine model, he defined computation as function application.

```
LAMBDA CALCULUS — CORE SYNTAX
===============================

  Term ::= x           (variable)
         | λx.M        (abstraction — defines a function)
         | M N         (application — applies M to N)

  RULES:
    α-conversion: λx.M = λy.M[x:=y]   (rename bound variables)
    β-reduction:  (λx.M) N → M[x:=N]  (substitute N for x in M)
    η-reduction:  λx.Mx → M            (if x not free in M)

  EXAMPLE: Identity function
    λx.x
    Applied to y: (λx.x) y → y

  EXAMPLE: Constant function (K combinator)
    λx.λy.x
    Applied: (λx.λy.x) a b → (λy.a) b → a

  Church numerals: encode natural numbers as functions
    0 = λf.λx.x
    1 = λf.λx.f x
    2 = λf.λx.f (f x)
    n = λf.λx.f^n x
    (n applied to f and x applies f n times to x)
```

**Church's thesis**: Any function that is "effectively computable" (by any reasonable procedure) is computable by lambda calculus. This is not provable — it is a philosophical claim about the nature of computation. It was vindicated empirically: every formal model of computation anyone has proposed (Turing machines, register machines, lambda calculus, recursive functions, cellular automata) computes exactly the same class of functions.

**Lambda calculus → modern languages**: Church's formalism is the direct ancestor of every functional programming language.

```
  Lambda calculus
       └─→ Lisp (McCarthy, 1958) — lambda as first-class function
       └─→ ML (Milner, 1973)
               └─→ Haskell, OCaml, F#
       └─→ ALGOL (Backus et al, 1960) — blocks/closures
               └─→ C, Pascal, ...
       └─→ Modern lambda expressions in Java 8, C# LINQ, Python lambda
               └─→ C# delegates/lambdas you use in LINQ are
                   direct descendants of Church's 1936 formalism
```

### Church's Undecidability Result

Church proved the same result as Turing — that the Entscheidungsproblem has no solution — using lambda calculus. The two papers appeared within months of each other in 1936, independently. Church's theorem: there is no algorithm to determine whether any lambda calculus formula has a normal form (i.e., whether computation terminates).

---

## Emil Post (1897–1954)

### Bio Snapshot

Polish-American mathematician. Columbia PhD. Independently discovered many of the same undecidability results as Turing and Church in 1936 — but did not publish them promptly, losing priority. Struggled with bipolar disorder. Died of a heart attack following electroconvulsive therapy.

### Post Correspondence Problem

Post's most famous result is the **Post Correspondence Problem (PCP)**, published 1946:

```
POST CORRESPONDENCE PROBLEM
============================

  Given: finite set of pairs of strings (dominoes):
    P = { (a₁, b₁), (a₂, b₂), ..., (aₙ, bₙ) }

  Question: Is there a finite sequence of indices i₁, i₂, ..., iₖ such that:
    a_{i₁} a_{i₂} ... a_{iₖ} = b_{i₁} b_{i₂} ... b_{iₖ}
    (concatenating top strings = concatenating bottom strings)

  Example that HAS a solution:
    (a, ab), (b, c), (abc, c)
    Pick: 1, 2, 3  →  top: a·b·abc = ababc
                     bottom: ab·c·c = abcc   NO
    Pick: 1, 2, 3, 2 → top: a·b·abc·b = ababcb
                        bottom: ab·c·c·c = abccc  NO
    ... (PCP requires systematic search)

  PCP is UNDECIDABLE. No algorithm exists that solves all instances.
```

PCP is important because:
1. It is easy to state (no machine models required)
2. It is undecidable (proved by reduction from the halting problem)
3. It is the go-to reduction target for proving other problems undecidable — many grammar problems, type-checking problems, and reachability problems reduce to PCP

**Tag systems**: Post also invented tag systems — a rewriting formalism that is Turing-complete despite extreme simplicity. A tag system deletes a fixed number of symbols from the front of a string and appends a suffix that depends on the first symbol. Used to prove undecidability of many pattern-matching problems.

### Post's Completeness Theorem

Less famous but equally foundational: Post proved (1941) that propositional calculus is **complete** — every tautology is provable. This is the companion result to Gödel's incompleteness (which applies to first-order arithmetic, not propositional logic). Post's proof established that truth tables are a decision procedure for propositional logic — the basis for all SAT solvers.

---

## Comparison Table

| Figure | Life | Key Paper | Core Model | Proved |
|--------|------|-----------|-----------|--------|
| Turing | 1912–1954 | On Computable Numbers (1936) | Turing Machine | Halting undecidable |
| Church | 1903–1995 | An Unsolvable Problem of Elementary Number Theory (1936) | Lambda calculus | Entscheidungsproblem no |
| Post | 1897–1954 | Finite Combinatory Processes (1936, pub. 1947) | Post Machine | PCP undecidable |

---

## Who to Cite for What

| Concept | Figure |
|---------|--------|
| Formal definition of algorithm / computation | Turing (TM) or Church (lambda) |
| Halting problem undecidable | Turing (1936) |
| Lambda calculus | Church (1936) |
| Church-Turing thesis | Church + Turing jointly |
| Universal machine / stored-program concept | Turing UTM |
| Functional languages' theoretical basis | Church |
| Post Correspondence Problem | Post (1946) |
| Propositional logic completeness | Post (1941) |
| Rice's Theorem (no semantic property decidable) | Rice (1953), built on Turing |

---

## Common Confusion Points

**"Turing invented the halting problem."**
Turing defined it and proved it undecidable. The question of whether computation terminates is implicit whenever you write a loop — Turing named the impossibility.

**"Church's lambda calculus is the lambda in modern languages."**
Direct descent, not metaphor. C# lambdas, Python `lambda`, Java lambdas — all are syntactic sugar for Church's beta reduction. The runtime semantics differ (most languages are call-by-value; lambda calculus is typically call-by-name or call-by-need), but the structural identity is exact.

**"Turing and Church got different results."**
They proved the same thing: the Entscheidungsproblem is unsolvable, and there is a class of functions (the "computable functions") that is the maximum extent of what any algorithm can compute. They used different formalisms and the results are provably equivalent.

**"The Church-Turing thesis is a theorem."**
It is not provable — it is a hypothesis about the relationship between mathematical formalism and physical reality. It says that the intuitive notion of "what a human can compute following a procedure" equals "what a Turing machine can compute." You cannot prove this because "intuitive notion" is not a formal object. It has held up empirically for 90 years.

**"Post was a minor figure."**
Post independently discovered computability theory, undecidability, and propositional completeness. His delayed publication cost him priority on multiple theorems. His Post Correspondence Problem is the canonical "easy to state, undecidable" result — used in every complexity theory textbook.
