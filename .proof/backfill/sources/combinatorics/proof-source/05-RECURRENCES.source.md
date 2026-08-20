---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "05-RECURRENCES.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:combinatorics:recurrences
kind: guide
module: combinatorics
section: combinatorics
title: Recurrences and Their Solutions
status: source-custody
source_custody: partial
current_path: combinatorics/05-RECURRENCES.md
canonical_path: combinatorics/05-RECURRENCES.md
backsource_ids: [proof-backfill:combinatorics:05-recurrences, git-history:combinatorics:05-recurrences]
concepts: [recurrences, characteristic equation, catalan, divide and conquer, master theorem]
root_concepts: [recurrences]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# Recurrences and Their Solutions

## The Big Picture

```
+============================================================================+
|                  A RECURRENCE IS A COUNT DEFINED BY ITSELF                 |
+============================================================================+
|                                                                            |
|   LINEAR, CONSTANT COEFFS         NONLINEAR / CONVOLUTION                  |
|   a_n = c1 a_{n-1}+...+ck a_{n-k}  a_{n+1}=SUM a_i a_{n-i} (Catalan)       |
|        |                                  |                                |
|        v                                  v                                |
|   CHARACTERISTIC EQUATION           GENERATING FUNCTION (file 03)          |
|   x^k = c1 x^{k-1}+...+ck            functional eqn -> closed form         |
|   roots r_i ->                                                             |
|   a_n = SUM A_i r_i^n                                                      |
|   (repeated root r: r^n, n r^n,...)                                        |
|                                                                            |
|   .------------------.   .------------------.   .-------------------.      |
|   | HOMOGENEOUS      |   | INHOMOGENEOUS    |   | DIVIDE & CONQUER  |      |
|   | a_n = c a_{n-1}  |   | a_n = c a_{n-1}  |   | T(n)=a T(n/b)+f(n)|      |
|   |       homog. sol |   |    + g(n)        |   | -> Master Theorem |      |
|   |                  |   | homog + particular|  | (cross: graph-alg)|      |
|   '------------------'   '------------------'   '-------------------'      |
+============================================================================+
```

A recurrence expresses `a_n` in terms of earlier terms — the discrete analog of
a differential equation, and the natural output of any recursive counting
argument ("condition on the last element / first move / root of the tree"). The
solution method depends on the *form*: linear-constant-coefficient yields to the
**characteristic equation**; convolution recurrences yield to **generating
functions** (`03`); divide-and-conquer recurrences yield to the **Master
Theorem**.

---

## Layer 1 — Linear Recurrences with Constant Coefficients

```
   ORDER-k HOMOGENEOUS:
   a_n = c1 a_{n-1} + c2 a_{n-2} + ... + ck a_{n-k}

   SOLUTION RECIPE
   1. Write the CHARACTERISTIC POLYNOMIAL:
        x^k - c1 x^{k-1} - c2 x^{k-2} - ... - ck = 0
   2. Find its roots r_1, ..., r_k (with multiplicity).
   3. GENERAL SOLUTION is a linear combination of root powers:
        a_n = A_1 r_1^n + A_2 r_2^n + ... + A_k r_k^n
   4. Fit constants A_i to the k initial conditions (linear system).
```

**Why root powers?** Try `a_n = r^n`. Substituting gives
`r^k = c_1 r^{k-1} + ... + c_k`, i.e. `r` must satisfy the characteristic
equation. The solution space of an order-`k` linear recurrence is a
`k`-dimensional vector space; the `r_i^n` form a basis (when roots are distinct),
and initial conditions pin down the coordinates. This is the discrete twin of
solving a linear ODE via `e^{λt}`.

### Repeated roots

```
   If root r has MULTIPLICITY m, it contributes m basis solutions:
        r^n,  n r^n,  n^2 r^n,  ...,  n^{m-1} r^n.

   Example: a_n = 4 a_{n-1} - 4 a_{n-2}.
   Char. poly x^2 - 4x + 4 = (x-2)^2, double root r=2.
   General solution:  a_n = (A + B n) 2^n.
```

The polynomial prefactor `n^j` for a multiplicity-`(j+1)` root is the discrete
analog of `t^j e^{λt}` for a repeated ODE root — same algebra, same reason.

### Inhomogeneous recurrences

```
   a_n = c1 a_{n-1} + ... + ck a_{n-k} + g(n)
        \________________________/   \____/
            homogeneous part         forcing term

   SOLUTION = homogeneous solution  +  ONE particular solution.
   Guess the particular solution by the SHAPE of g(n):
     g(n) const      -> try constant          (or n*const if 1 is a root)
     g(n) = d^n      -> try B d^n             (or n B d^n if d is a root)
     g(n) polynomial -> try polynomial same degree
```

The "multiply your guess by `n`" rule when the forcing term collides with a
homogeneous root is the **resonance** case — identical to the method of
undetermined coefficients for ODEs.

---

## Layer 2 — Worked Example: Fibonacci and Tilings

```
   PROBLEM: # of ways to tile a 1xn strip with 1x1 squares and 1x2 dominoes.
   Condition on the LAST tile:
     - ends in a square  -> tilings of length n-1
     - ends in a domino  -> tilings of length n-2
   => f_n = f_{n-1} + f_{n-2},   f_0 = 1, f_1 = 1.   (Fibonacci, shifted)

   CHAR. EQN  x^2 - x - 1 = 0,  roots phi=(1+sqrt5)/2, psi=(1-sqrt5)/2.
   a_n = A phi^n + B psi^n.  Fit f_0=1, f_1=1:
   f_n = (phi^{n+1} - psi^{n+1}) / sqrt5.

   Since |psi| < 1, f_n ~ phi^{n+1}/sqrt5  (geometric growth, rate phi).
```

This is the same Fibonacci closed form derived via generating functions in `03`
— two roads to Binet's formula. The characteristic-equation road is faster when
the recurrence is already linear-constant-coefficient; the generating-function
road is necessary when it is not (convolution, polynomial coefficients).

---

## Layer 3 — The Catalan Recurrence (convolution → GF)

Some recurrences are **not** linear with constant coefficients — the Catalan
recurrence sums over *all* split points:

```
   C_0 = 1,   C_{n+1} = SUM_{i=0}^{n} C_i C_{n-i}.

   This convolution arises everywhere:
     - binary trees on n internal nodes: pick a root, split into
       left subtree (i nodes) and right subtree (n-i nodes)
     - triangulations of an (n+2)-gon: fix an edge, the triangle on it
       splits the polygon into two smaller polygons
     - balanced parenthesizations, Dyck paths, ...

   Convolution => use a generating function (file 03):
       C(x) = 1 + x C(x)^2   =>   C(x) = (1 - sqrt(1-4x))/(2x)
       C_n = (1/(n+1)) C(2n, n).

   C_n: 1, 1, 2, 5, 14, 42, 132, 429, ...   (grows like 4^n / n^{3/2}).
```

The tell that you need a generating function rather than a characteristic
equation: the recurrence involves `Σ a_i a_{n-i}` (a self-convolution) or has
*polynomial* coefficients in `n`. Full bijective treatment of Catalan objects is
in `07-SPECIAL-NUMBERS.md`.

---

## Layer 4 — Divide-and-Conquer Recurrences and the Master Theorem

Recursive algorithms produce recurrences of the form `T(n) = a T(n/b) + f(n)`.
The **Master Theorem** reads off the asymptotics by comparing `f(n)` to the
**watershed** `n^{log_b a}`.

```
   T(n) = a T(n/b) + f(n),   a >= 1, b > 1.
   Let  c* = log_b(a)   (the "critical exponent").

   CASE 1  f(n) = O(n^{c*-eps})         => T(n) = Theta(n^{c*})
           (leaves dominate)
   CASE 2  f(n) = Theta(n^{c*} log^k n) => T(n) = Theta(n^{c*} log^{k+1} n)
           (balanced)
   CASE 3  f(n) = Omega(n^{c*+eps})     => T(n) = Theta(f(n))
           and a f(n/b) <= c f(n) for c<1 (root dominates, regularity)
```

| Recurrence | `a, b, c*` | Master case | Result |
|------------|-----------|-------------|--------|
| `T(n)=2T(n/2)+n` (mergesort) | 2,2,1 | 2 (k=0) | `Θ(n log n)` |
| `T(n)=2T(n/2)+1` (tree traversal) | 2,2,1 | 1 | `Θ(n)` |
| `T(n)=T(n/2)+1` (binary search) | 1,2,0 | 2 (k=0) | `Θ(log n)` |
| `T(n)=7T(n/2)+n^2` (Strassen) | 7,2,2.807 | 1 | `Θ(n^{log₂7})` |
| `T(n)=4T(n/2)+n^3` | 4,2,2 | 3 | `Θ(n^3)` |

This is a **CS bridge by construction** — the Master Theorem lives in algorithm
analysis (`graph-algorithms/` uses it for recursive graph algorithms). The
combinatorial content: the recursion tree has `a^i` nodes at depth `i`, each of
size `n/b^i`; summing `f` over the tree is a geometric series whose dominant end
(root, leaves, or balanced) is what the three cases distinguish. The
Akra–Bazzi theorem generalizes to unequal/variable splits.

---

## Old World → New World Bridges

| You know | Maps to |
|----------|---------|
| Solving linear ODE via `e^{λt}` | characteristic-equation method (`r^n`) |
| Resonance / `t·e^{λt}` for repeated ODE roots | `n·r^n` for repeated recurrence roots |
| Method of undetermined coefficients | particular-solution guessing |
| Recursion-tree / call-graph cost analysis | divide-and-conquer recurrence + Master Theorem |
| Z-transform of a difference equation | generating function of the recurrence (`03`) |
| `T(n)=2T(n/2)+n` in a code review | mergesort = `Θ(n log n)` |

**Old → new (DSP/control).** A linear constant-coefficient recurrence *is* a
discrete-time LTI filter; its characteristic roots are the **poles**, and the
solution's stability (does `a_n` blow up?) is exactly `|r_i| < 1` pole-inside-
unit-circle reasoning. Combinatorial growth rate = dominant pole magnitude.

---

## Decision Cheat Sheet

| Recurrence shape | Method | Reference |
|------------------|--------|-----------|
| `a_n = c_1 a_{n-1}+...+c_k a_{n-k}` (const coeffs) | Characteristic equation | this file |
| ...with forcing term `g(n)` | Homogeneous + particular | this file |
| Repeated characteristic root `r` (mult m) | `r^n, n r^n, ..., n^{m-1}r^n` | this file |
| Convolution `a_{n+1}=Σ a_i a_{n-i}` | Generating function | `03`, `07` |
| Polynomial coefficients in `n` | Generating function / hypergeometric | `03` |
| `T(n) = a T(n/b) + f(n)` | Master Theorem | this file |
| Uneven splits `T(n)=T(αn)+T(βn)+f` | Akra–Bazzi | this file |
| Just want asymptotics, not exact | Dominant root / singularity analysis | `03` |

---

## Common Confusion Points

### "Characteristic equation or generating function?"

If the recurrence is **linear with constant coefficients**, the characteristic
equation is faster — factor a polynomial, combine root powers, fit constants.
Reach for a **generating function** when the recurrence has a *convolution* term
(Catalan), *polynomial* coefficients in `n`, or you want a unified object to
manipulate. They agree where both apply (Fibonacci): the GF denominator is the
characteristic polynomial with reversed coefficients.

### "Why does a repeated root add a factor of n?"

Because a double root collapses two basis solutions `r_1^n, r_2^n` into one as
`r_2 → r_1`; the limit `(r_2^n - r_1^n)/(r_2 - r_1) → n r^{n-1}` supplies the
missing dimension. The solution space is always `k`-dimensional for an order-`k`
recurrence; the `n^j` factors restore the dimensions a repeated root would
otherwise lose. (Same reason `t e^{λt}` appears for repeated ODE roots.)

### "The Master Theorem doesn't apply to my recurrence."

The three cases leave gaps — notably when `f(n)` is between `n^{c*}` and
`n^{c*} polylog` but not matching Case 2's `log^k` form, or when the Case-3
regularity condition fails. For those, use the **recursion-tree method**
directly (sum the work level by level) or **Akra–Bazzi** (handles variable
splits and a broader `f`). The Master Theorem is a convenient special case, not
a universal solver.

### "My recurrence grows like `r^n` — is `r` the largest root?"

Yes, asymptotically. With distinct roots, `a_n = Σ A_i r_i^n` is dominated by the
term with the largest `|r_i|` (the **dominant root**), provided its coefficient
`A_i ≠ 0`. So the *growth rate* is the magnitude of the largest characteristic
root — Fibonacci grows like `φ^n` because `φ ≈ 1.618 > |ψ| ≈ 0.618`. This is the
combinatorial analog of the dominant-pole rule for filter response.
