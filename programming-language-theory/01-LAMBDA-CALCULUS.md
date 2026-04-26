# Lambda Calculus: Syntax, Reduction, Normal Forms, Encodings

## The Big Picture

You know this. The question is: what aspects matter for understanding modern language design decisions? The answer: Church-Rosser (confluence), normal form hierarchy (why Haskell does WHNF), CBV vs. CBN vs. CBNeed operational distinction, and de Bruijn indices as the canonical representation in proof assistants.

```
+--------------------------------------------------------------------------+
|                    LAMBDA CALCULUS LANDSCAPE                             |
+--------------------------------------------------------------------------+
|                                                                          |
|  THE FORMAL SYSTEM:                                                      |
|  Syntax: t ::= x | λx.t | t t      (variable, abstraction, application) |
|  β-reduction: (λx.t) s → t[s/x]    (capture-avoiding)                  |
|  η-equivalence: λx.(f x) = f       (when x ∉ FV(f))                    |
|                                                                          |
|  THE KEY THEOREMS:                                                       |
|  Church-Rosser: if t →* t₁ and t →* t₂, then ∃t₃: t₁ →* t₃, t₂ →* t₃ |
|  → Reduction order doesn't affect the final value (if it terminates)    |
|  → Why CBV and CBN give the same *result* for terminating pure programs  |
|  → Why lazy vs. strict semantics are observationally equivalent (pure)  |
|                                                                          |
|  THE NORMAL FORM HIERARCHY:                                              |
|  NF (normal form): no β-redex anywhere                                  |
|  HNF (head normal form): head position not a redex                      |
|  WHNF (weak head normal form): head position reduced, body not entered  |
|  → Haskell evaluates to WHNF (lazy evaluation stops here)               |
+--------------------------------------------------------------------------+
```

---

## 1. Formal Machinery — The Parts That Matter

You know the Church calculus. The key formal details for PL work:

**Capture-avoiding substitution** is the operational core:
```
t[s/x] — substitute s for free occurrences of x in t

(y)[s/x]     = s         if x = y
             = y         if x ≠ y
(t₁ t₂)[s/x] = (t₁[s/x]) (t₂[s/x])
(λy.t)[s/x]  = λy.(t[s/x])     if y ≠ x AND y ∉ FV(s)
             = λz.(t[z/y][s/x]) if y ∈ FV(s)   ← RENAME to avoid capture
                                                    (α-conversion first)

THE CAPTURE PROBLEM:
  (λy. λx. y) x → λx. x   ← WRONG (x captured by inner λ)
  Should give: λz. x  (rename bound variable to fresh z)

  α-equivalence: λx.x = λy.y = λz.z
  (bound variable names are arbitrary; it's the binding structure that matters)
```

**Why this matters**: Every interpreter implements substitution. The capture-avoiding version is subtle. De Bruijn indices (Section 5) eliminate this entirely by making binding structure explicit.

---

## 2. Church-Rosser and What It Means

**The theorem** (Church and Rosser, 1936): The λ-calculus reduction relation → is confluent: if t →* s₁ and t →* s₂ then there exists s₃ with s₁ →* s₃ and s₂ →* s₃.

```
CONFLUENCE DIAGRAM:

         t
        / \
       /   \
      s₁   s₂
       \   /
        \ /
         s₃

Any two reduction sequences from the same term
can be completed to a common reduct.
```

**Corollary — uniqueness of normal forms**: If t has a normal form, it is unique (up to α-equivalence). You can't reduce to two different values.

**The practical consequence for language design**:
```
CBV (call by value): evaluate argument before substitution
  (λx. x + 1) (2 + 3)
  → (λx. x + 1) 5     (evaluate argument first)
  → 5 + 1
  → 6

CBN (call by name): substitute without evaluating
  (λx. x + 1) (2 + 3)
  → (2 + 3) + 1       (substitute unevaluated expression)
  → 5 + 1
  → 6

SAME RESULT (confluence guarantees this for terminating pure programs).
DIFFERENT BEHAVIOR for:
  1. Non-terminating arguments: CBN can skip evaluating Ω (diverging)
     (λy. 42) Ω → 42 in CBN; diverges in CBV
  2. Side effects: evaluation order matters for IO

WHY HASKELL IS CBNeed (lazy, not just CBN):
  CBN re-evaluates shared arguments each time they're used.
  CBNeed = CBN + memoization (thunks: evaluate once, cache result)
  Same result as CBN for pure programs; asymptotically more efficient.
  Confluence: denotational semantics of lazy vs. strict programs agree
  for pure programs (operational semantics differ).
```

---

## 3. Normal Form Hierarchy

Critical for understanding Haskell's evaluation model:

```
TERM: (λf. f 3) (λx. x + 1)

β-redex: any (λx.t) s subterm

NORMAL FORM (NF):
  No β-redex anywhere (fully evaluated)
  (λf. f 3) (λx. x + 1) → (λx. x + 1) 3 → 3 + 1 → 4
  NF: 4

HEAD NORMAL FORM (HNF):
  Head position is not a redex; body may contain redexes
  Head of (λx. t): the entire abstraction
  Head of (f t₁ ... tₙ): f applied to args

WEAK HEAD NORMAL FORM (WHNF):
  Outer constructor or abstraction reached; do NOT reduce under λ
  λx. (λy.y) x  ← WHNF (it's a λ; don't look inside)
  But: fully evaluated: λx. x  ← NF (no more redexes anywhere)

HASKELL EVALUATES TO WHNF:
  ghci> :sprint xs = [1, 2+1, 4]
  Haskell sees the outer [] constructor (WHNF)
  Does NOT evaluate 2+1 until it's needed
  This is lazy evaluation: reduce to WHNF only, on demand

  Implications:
    seq :: a → b → b  evaluates first arg to WHNF (not NF)
    deepseq evaluates to NF
    Pattern matching forces to WHNF (constructor head visible)
```

---

## 4. Encodings: Church, Scott, and Beyond

**Church numerals** — you know these. Why they exist and why they matter:

```
CHURCH NUMERALS:
  0 = λs. λz. z          (zero: apply s zero times to z)
  1 = λs. λz. s z         (one: apply s once to z)
  n = λs. λz. sⁿ z

  This works: addition, multiplication, predecessor all definable
  ADD = λm. λn. λs. λz. m s (n s z)
  MUL = λm. λn. λs. m (n s)

WHY CHURCH NUMERALS MATTER:
  Show that pure λ-calculus is Turing-complete (encode all data)
  But they're INEFFICIENT: predecessor is O(n)
  Real language runtimes use native machine integers, not Church encoding

THE LIMITATION OF CHURCH NUMERALS IN LAZY CONTEXTS:
  Church numerals are strict in the iteration count
  Doesn't compose well with lazy streams
  → Scott encoding for lazy-friendly data
```

**Scott encoding** — designed for lazy evaluation and pattern matching:
```
SCOTT ENCODING:
  Encodes data as its own case/pattern-match function

  For a type T = A | B x y:
    encode(A)   = λa. λb. a           (choose first branch)
    encode(B x y) = λa. λb. b x y    (choose second branch, pass fields)

  For natural numbers (Peano):
    zero = λz. λs. z              (0: choose zero branch)
    succ n = λz. λs. s n          (n+1: choose succ branch, pass predecessor)

  KEY DIFFERENCE FROM CHURCH:
    Scott predecessor is O(1): (succ n) applied to (λz.λs.s) → n
    Church predecessor is O(n): need to re-build n-1 from scratch

  WHY LAZY-FRIENDLY:
    Scott encoding doesn't force evaluation of all elements
    Natural fit for recursive types in lazy languages
    Codata (streams, infinite trees) uses Scott-style encoding
```

**Binary Church numerals** (Mogensen 1995):
```
BINARY ENCODING:
  Instead of unary iteration, encode as binary tree
  zero   = λz. λe. λo. z
  even n = λz. λe. λo. e (encode n)   (2n)
  odd n  = λz. λe. λo. o (encode n)   (2n+1)

  Addition and multiplication now O(log n) instead of O(n)
  Used in: theorem prover implementations where performance matters
```

---

## 5. The Y Combinator

```
Y COMBINATOR: Y = λf. (λx. f (x x)) (λx. f (x x))

  Y F →  (λx. F (x x)) (λx. F (x x))
       →  F ((λx. F (x x)) (λx. F (x x)))
       →  F (Y F)

  Y F = F (Y F)  ← Y F is a fixed point of F

WHY IT EXISTS:
  Pure lambda calculus has no let rec or def
  Recursion requires a function calling itself by name
  But lambda terms are anonymous
  Y provides general recursion from the anonymous calculus

CALL-BY-VALUE VARIANT (Turing combinator):
  Y doesn't work directly under CBV (eager evaluation diverges)
  Z = λf. (λx. f (λv. x x v)) (λx. f (λv. x x v))
  Z F = F (λv. Z F v)
  The λv. ... is a "thunk" that delays evaluation

  This is exactly how CBV languages implement recursion:
  let rec f x = ... becomes a fixed point with an explicit thunk
```

---

## 6. CBV vs. CBN vs. CBNeed

Operational comparison (pure programs):

```
+-----------------------------------------------------------------------+
|                    EVALUATION STRATEGIES                              |
+-----------------------------------------------------------------------+
|              CBV                 CBN              CBNeed               |
|         (call by value)    (call by name)    (call by need/lazy)       |
+-----------------------------------------------------------------------+
| Arguments  Evaluated         Not evaluated      Not evaluated         |
| evaluated: before call       before call        before call (WHNF)    |
|                                                                       |
| Sharing:   N/A (value)       No sharing:        Shared: thunk         |
|                               re-evaluate        evaluated once,      |
|                               each use           cached               |
|                                                                       |
| Diverging  (λy.42) Ω        (λy.42) Ω          (λy.42) Ω              |
| argument:  diverges          = 42                = 42                 |
|                                                                       |
| Languages: ML, Scheme,       (no mainstream      Haskell, Miranda,    |
|            Python, Rust,      pure-CBN)           lazy Racket         |
|            JavaScript,        (CBN with           (with memoization)  |
|            OCaml              effects = messy)                        |
|                                                                       |
| Efficiency: Good for I/O,   Re-evaluation       Best for data         |
|             effects         overhead            structures;           |
|                             (no sharing)        worst for simple      |
|                                                 scalars               |
+-----------------------------------------------------------------------+

DENOTATIONAL EQUIVALENCE (pure programs):
  For pure (effect-free) programs, CBV and CBN give the same value
  when they terminate. (Church-Rosser corollary.)
  CBNN = CBN + memoization = same values, better complexity.

  In practice: Haskell's lazy evaluation is observationally equivalent
  to CBN for pure functions but more efficient due to sharing.
```

---

## 7. De Bruijn Indices

De Bruijn (1972) invented a nameless representation for lambda terms:

```
DE BRUIJN NAMELESS REPRESENTATION:

  Instead of variable names, use numbers indicating
  how many binders to skip to reach the binding λ.

  Named:     λx. λy. x y       (x bound by outer λ; y by inner λ)
  De Bruijn: λ   λ   1 0        (1 skip to outer λ; 0 = innermost)

  Named:     λx. λy. λz. x (y z)
  De Bruijn: λ   λ   λ   2 (1 0)

SUBSTITUTION WITHOUT CAPTURE:
  No need for renaming (α-conversion) because there are no names
  Substitution becomes: shift indices (when a term is moved under binders)
    shift↑(k, d, x):
      if k ≤ x then x + d   (add offset if above cutoff)
      else x                 (below cutoff, leave alone)

  substitute(t, s, k):
    substitute s for de Bruijn index k in t

USES IN PRODUCTION:
  Coq, Agda, Lean: internally use de Bruijn (or related nameless rep)
  Proof assistants need canonical forms for comparison, substitution
  Without names: α-equivalence = syntactic equality
  → Critical for performance in type-checking (no α-renaming overhead)

LIFTING AND OPENING:
  When you go under a binder (enter λ body), you must adjust
  free variables of the substituted term (shift up by 1)
  When you exit a binder, you shift down
  This bookkeeping replaces the α-renaming of named calculus
```

---

## Decision Cheat Sheet

| Concept | Why it matters | Where it shows up |
|---------|---------------|-------------------|
| Capture-avoiding substitution | Every interpreter is built on this | All language implementations |
| Church-Rosser | CBV = CBN for pure programs (same results) | Why Haskell and OCaml can share a formal semantics |
| WHNF | Haskell's evaluation strategy | Understanding seq, deepseq, laziness bugs |
| Church numerals | Data in pure λ-calculus (Turing completeness) | Theory; not production |
| Scott encoding | O(1) predecessor; lazy-friendly | Coq inductives, Haskell data types |
| Y combinator | General recursion from anonymous calculus | Compiler treatment of let rec |
| De Bruijn indices | Canonical nameless terms; no α-renaming | Coq, Agda, Lean internals |
| CBV vs. CBNeed | Performance and evaluation order | Haskell (lazy) vs. OCaml/Rust (eager) |

---

## Common Confusion Points

**Church-Rosser does not mean CBV = CBN always**: It means they agree *when both terminate*. Non-terminating arguments behave differently: CBN may skip them (λy.42 applied to diverging term = 42 in CBN, diverges in CBV). This is the reason Haskell can implement `const x y = x` without evaluating y — the diverging term is never forced.

**WHNF and NF are different**: In Haskell, `seq x y` forces x to WHNF, not NF. A constructor like `Just (bottom)` is in WHNF (Just is the outer constructor) but not NF (the argument is ⊥). This is the source of many Haskell laziness bugs — you think you've evaluated something but you've only reached the outer constructor.

**Scott numerals are not the same as Peano in Coq**: Coq's `Nat` is an inductive type with `O` and `S` constructors — this is the Peano representation in type theory. Scott encoding is a lambda-calculus trick for encoding inductives in the pure untyped calculus. Both are conceptually related but different representations.

**The Y combinator doesn't work in CBV**: Standard Y diverges under call-by-value because the self-application `x x` is evaluated before the result is used. You need either the Z combinator (CBV fixed-point combinator) or native `let rec` (which all CBV languages provide, implemented via mutable reference or heap-allocated closure).
