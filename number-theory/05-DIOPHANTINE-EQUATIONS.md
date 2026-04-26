# Diophantine Equations

## The Big Picture

```
+====================================================================+
|           DIOPHANTINE EQUATIONS — CLASSES AND METHODS              |
+====================================================================+
|                                                                    |
|  LINEAR           QUADRATIC          CUBIC / ELLIPTIC  GENERAL    |
|  ax + by = c      x² - Dy² = 1       y² = x³ + ax + b  xⁿ+yⁿ=zⁿ |
|  +-----------+    +-----------+       +---------------+ +-------+ |
|  |Bezout     |    |Pell eq.   |       |Elliptic curves| |Fermat | |
|  |condition  |    |continued  |       |finite/infinite| |Last   | |
|  |gcd(a,b)|c |    |fractions  |       |rational pts   | |Theorem| |
|  |           |    |fund. sol. |       |Mordell-Weil   | |(1994) | |
|  +-----------+    +-----------+       +---------------+ +-------+ |
|                                                                    |
|  PYTHAGOREAN      SUMS OF SQUARES     WARING'S PROBLEM            |
|  a²+b²=c²        x₁²+...+xₖ²=n       every n = sum of k kth pows |
|  +----------+    +-------------+      +-----------------+         |
|  |param.    |    |Fermat-Euler |      |g(k): min k works|         |
|  |solution  |    |2 squares iff|      |g(2)=4, g(3)=9   |         |
|  |family    |    |no p≡3(mod 4)|      |all g(k) known   |         |
|  +----------+    +-------------+      +-----------------+         |
+====================================================================+
```

---

## Linear Diophantine Equations

```
PROBLEM: Find integer solutions to ax + by = c.

EXISTENCE: Solutions exist ⟺ gcd(a,b) | c.

GENERAL SOLUTION: If (x₀, y₀) is one solution:
  x = x₀ + (b/d)t
  y = y₀ - (a/d)t
  for any t ∈ Z, where d = gcd(a,b).

FINDING x₀, y₀:
  Extended Euclidean gives sa + tb = d.
  Multiply by c/d: s(c/d)·a + t(c/d)·b = c.
  So x₀ = sc/d, y₀ = tc/d.

Example: 6x + 10y = 14
  d = gcd(6,10) = 2. Does 2|14? Yes (14/2=7). ✓
  Extended Euclidean: 6(-1) + 10(1) = 4... wait, gcd(6,10):
  10 = 1·6 + 4  →  gcd(6,4)
   6 = 1·4 + 2  →  gcd(4,2)
   4 = 2·2 + 0  →  gcd = 2
  Back-substitute: 2 = 6 - 1·4 = 6 - 1·(10-1·6) = 2·6 - 1·10
  So s=2, t=-1, d=2.
  x₀ = 2·7 = 14, y₀ = -1·7 = -7.
  Check: 6·14 + 10·(-7) = 84 - 70 = 14 ✓
  General: x = 14 + 5t, y = -7 - 3t.
```

### Multiple Variables

```
a₁x₁ + a₂x₂ + ... + aₙxₙ = c

Existence: gcd(a₁, ..., aₙ) | c.
Solve recursively: reduce to 2-variable problem using gcd of first two, etc.
```

---

## The Pell Equation

```
PROBLEM: Find positive integer solutions to x² - Dy² = 1 (D > 0, not a perfect square).

Named after John Pell, but actually studied by Brahmagupta (628 AD) and solved by
Fermat, then formalized by Lagrange.

FUNDAMENTAL THEOREM:
  For any non-square D > 0, x² - Dy² = 1 has infinitely many positive solutions.
  The smallest positive solution (x₁, y₁) is the FUNDAMENTAL SOLUTION.
  All solutions are:
    xₙ + yₙ√D = (x₁ + y₁√D)ⁿ  for n = 1, 2, 3, ...

Example: D=2.  x² - 2y² = 1.
  Fundamental: (x₁,y₁) = (3,2). Check: 9 - 8 = 1 ✓
  (3+2√2)² = 17+12√2 → (17,12). Check: 289 - 288 = 1 ✓
  (3+2√2)³ = 99+70√2 → (99,70). Check: 9801 - 9800 = 1 ✓
```

### Continued Fractions Method

```
The fundamental solution is found via the continued fraction expansion of √D.

√D = a₀ + 1/(a₁ + 1/(a₂ + 1/(a₃ + ...)))
  = [a₀; a₁, a₂, a₃, ...]  (periodic for irrational √D)

Convergents: pₙ/qₙ → √D
  The fundamental solution appears among the convergents.
  Specifically: x₁ = pₖ₋₁, y₁ = qₖ₋₁ where k is the period length.

Example: √2 = [1; 2, 2, 2, ...]
  Convergents: 1/1, 3/2, 7/5, 17/12, ...
  Period = 1 (a₁ = 2). Fundamental solution: p₀/q₀ = 1/1? No. p₁/q₁ = 3/2. ✓
  x₁=3, y₁=2: 3² - 2·2² = 9-8=1 ✓

Example: √61 = [7; 1,4,3,1,2,2,1,3,4,1,14,...]  period=11
  Fundamental solution: (x₁,y₁) = (1766319049, 226153980) — enormous!
  The size of fundamental solutions can be exponential in √D.
```

### Connection to Algebraic Number Theory

```
Z[√D] = {a + b√D : a,b ∈ Z}  (ring of integers for D ≡ 2,3 mod 4)

x² - Dy² = 1 ⟺ N(x + y√D) = 1  (the NORM map: a+b√D ↦ a²-Db²)
Units of Z[√D] = {±1} × {fundamental unit}^Z

Pell equation = finding units in real quadratic fields.
Dirichlet's unit theorem: O_K has finitely generated unit group
  of rank r₁ + r₂ - 1 (r₁ = real embeddings, r₂ = complex embedding pairs).
For Q(√D), D>0: r₁=2, r₂=0 → rank 1. One fundamental unit generates all.
```

---

## Pythagorean Triples

```
PROBLEM: Find all positive integer solutions to a² + b² = c².

COMPLETE PARAMETERIZATION:
  Every primitive Pythagorean triple (gcd(a,b,c)=1) is:
    a = m² - n²,  b = 2mn,  c = m² + n²
  for integers m > n > 0 with gcd(m,n) = 1 and m-n odd.
  (Swap a,b for the other orientation.)

All triples: multiply any primitive triple by a common factor k.

Examples:
  m=2, n=1: (3, 4, 5)
  m=3, n=2: (5, 12, 13)
  m=4, n=1: (15, 8, 17)
  m=4, n=3: (7, 24, 25)
  m=5, n=2: (21, 20, 29)

PROOF SKETCH:
  a² = c² - b² = (c-b)(c+b).
  Since gcd(a,b,c)=1 and c,b are opposite parity (one even, one odd):
  gcd(c-b, c+b) = 2.
  Let c-b = 2n², c+b = 2m² → c = m²+n², b = m²-n², a = 2mn.
  (Wait — swap: if b is even, then b = 2mn, a = m²-n².)
```

### Geometric Interpretation

```
Pythagorean triples ↔ rational points on the unit circle.

a² + b² = c²  ⟺  (a/c)² + (b/c)² = 1

So: parametrize rational points on x² + y² = 1.
  Line through (-1, 0) with slope t (rational):
    y = t(x+1)
    Substitute: x² + t²(x+1)² = 1
    Solve: x = (1-t²)/(1+t²), y = 2t/(1+t²)

Setting t = n/m: a/c = (m²-n²)/(m²+n²), b/c = 2mn/(m²+n²).
This is the same as the parametric formula above.

This technique generalizes: rational points on any conic via pencil of lines.
For higher-degree curves (elliptic curves), it fails — no simple parametrization.
```

---

## Sums of Squares

```
QUESTION: Which n can be written as n = x₁² + ... + xₖ²?

TWO SQUARES: n = x² + y² iff in the prime factorization of n,
  every prime p ≡ 3 (mod 4) appears to an even power.

  Equivalently: n is a sum of two squares iff all its "3 mod 4" prime
  factors have even exponent.

  Primes that are sums of two squares:
    2 = 1²+1² ✓
    p ≡ 1 (mod 4): always a sum of two squares (Fermat's theorem on sums)
    p ≡ 3 (mod 4): NEVER a sum of two squares

  Proof sketch via Gaussian integers Z[i]:
    Z[i] is a PID. The prime p factors in Z[i] iff p = a²+b² for some a,b.
    p factors iff -1 is a QR mod p iff p ≡ 1 (mod 4).

FOUR SQUARES: Every n ≥ 0 is a sum of four squares (Lagrange, 1770).
  Identity: (a²+b²+c²+d²)(e²+f²+g²+h²) = sum of four squares (Euler/Brahmagupta)
  n=4k+3 cannot be 1 or 2 squares. Always 4 suffices.

THREE SQUARES: n = x²+y²+z² iff n ≠ 4ᵃ(8b+7) for a,b ≥ 0.
  (Legendre's three-square theorem)
```

---

## Fermat's Last Theorem

```
THEOREM (Wiles, 1994): For n ≥ 3, there are no positive integer solutions
  to xⁿ + yⁿ = zⁿ.

Stated by Fermat in the margin of Diophantus's Arithmetica (1637):
  "I have discovered a truly marvelous proof of this, which this margin
   is too narrow to contain."
  No such proof was ever found — modern proof uses 20th-century mathematics.

PROOF STRATEGY (Wiles):
  1. Assume aᵖ + bᵖ = cᵖ for prime p ≥ 5 (reduces to prime exponents)
  2. Frey Curve (Frey, 1984): y² = x(x-aᵖ)(x+bᵖ)
     This is an elliptic curve with bizarre discriminant.
  3. Ribet's Theorem (1986): The Frey curve corresponds to a level-2 modular form.
     But level-2 modular forms don't exist.
  4. Modularity Theorem (Wiles 1994, Taylor-Wiles): Every semistable elliptic curve
     over Q is modular (i.e., corresponds to a modular form).
  5. Contradiction: Frey curve exists → modular form exists → doesn't exist.
     So the assumption aᵖ + bᵖ = cᵖ is false.
```

### Historical Partial Results

```
n=3:  Euler (1770) — no solution (with a gap filled by Gauss)
n=4:  Fermat himself — no solution (infinite descent)
n=5:  Dirichlet + Legendre (1825)
n=7:  Lamé (1839)
General:  Kummer (1850s) — proved for "regular" primes (most primes)
         Irregular primes: 37, 59, 67, 101, ...
         All irregular primes checked computationally up to 4×10^6 — FLT holds.
         Wiles — complete proof, 1994.

Kummer's insight: Work in Z[ζₙ] (n-th roots of unity) instead of Z.
  UFT fails in Z[ζₙ] → introduced ideal numbers to fix it.
  This led directly to algebraic number theory and ideal class groups.
```

---

## Elliptic Curves

```
DEFINITION: An elliptic curve over Q is
  E: y² = x³ + ax + b  (Weierstrass form)
  with discriminant Δ = -16(4a³+27b²) ≠ 0 (no repeated roots).

MORDELL-WEIL THEOREM (1922):
  The set of rational points E(Q) is a finitely generated abelian group:
  E(Q) ≅ Z^r ⊕ E_tors(Q)
  r = rank (can be any non-negative integer, possibly 0)
  E_tors = torsion subgroup (finite, classified by Mazur's theorem)

MAZUR'S TORSION THEOREM:
  E_tors(Q) is isomorphic to Z/n for n ∈ {1,...,10,12} or Z/2 × Z/2n for n ∈ {1,...,4}.

GROUP LAW: "Chord-tangent" construction.
  P + Q: draw line through P,Q; it meets E in a third point R; reflect over x-axis.
  P + P: tangent line at P.

Cryptographic note: Over F_p, E(F_p) is an abelian group of order p ± O(√p)
  (Hasse's theorem). The discrete log problem in E(F_p) is the ECDLP.
```

The chord-tangent group law on E is not ad hoc — it is the group structure of Pic^0(E), the divisor class group of degree-0 divisors modulo principal divisors. For a smooth projective curve of genus g, Pic^0 is a g-dimensional abelian variety (the Jacobian). For elliptic curves, g = 1, so the Jacobian is the curve itself: E ≅ Jac(E). This is what makes elliptic curves the simplest non-trivial case: genus 0 curves have no interesting Pic^0; genus >= 2 curves have Jacobians of dimension >= 2 (harder to work with). The chord-tangent construction is the explicit realization of the abstract group law on Pic^0.

### Birch-Swinnerton-Dyer Conjecture

```
BSD (one of 7 Millennium Prize Problems, $1M prize):

Let L(E,s) = Euler product over primes p of the local factors.

CONJECTURE: ord_{s=1} L(E,s) = rank(E(Q))
  i.e., the order of vanishing of L(E,s) at s=1 equals the rank.

If true:
  - L(E,1) = 0 iff E has infinitely many rational points
  - The rank is computable from the L-function
  - Connects geometry (rational points) to analysis (L-function zeros)

Status: Proved for rank 0 and 1 (Coates-Wiles, Gross-Zagier-Kolyvagin).
  Rank ≥ 2: open.
```

---

## Decision Cheat Sheet

| Equation type | Key theorem | Method |
|---------------|-------------|--------|
| ax + by = c | Bezout: d=gcd(a,b) must divide c | Extended Euclidean |
| x² - Dy² = 1 (Pell) | Fundamental solution via continued fractions | CF expansion of √D |
| a² + b² = c² (Pythagorean) | Complete parametrization | m,n formula |
| n = x² + y² | p ≡ 3 mod 4 must appear to even power | Gaussian integers |
| n = sum of 4 squares | Always possible (Lagrange) | Constructive, but complex |
| xⁿ + yⁿ = zⁿ (FLT) | No solutions for n ≥ 3 (Wiles) | N/A — no solutions exist |
| y² = x³ + ax + b (EC) | Mordell-Weil: finitely generated | Descent algorithms |

---

## Common Confusion Points

**"Pell equation x² - Dy² = ±1 — the ±1 doesn't matter."**
It does. x² - Dy² = -1 may or may not have solutions. It has solutions iff
the continued fraction period of √D is odd. Example: D=5, x²-5y²=-1 has
solution (2,1): 4-5 = -1 ✓. D=3, x²-3y²=-1 has NO solutions (parity argument).

**"FLT was proved for all n in ancient times."**
Fermat proved n=4. Euler proved n=3 (with a gap). The general proof waited
until 1994. The case n = p (prime) implies all composite n, so it suffices
to prove for primes.

**"Elliptic curves are just curves."**
They carry a group structure that is not obvious from the equation. The
group law uses the chord-tangent construction. Over number fields, the group
of rational points has deep arithmetic significance (BSD conjecture). Over
finite fields, the group is used for cryptography (ECC). Over C, an elliptic
curve is topologically a torus (genus 1 surface).

**"Pythagorean triples are an isolated curiosity."**
The parameterization technique — intersecting a conic with a line through
a known rational point — is a fundamental method in Diophantine geometry.
Rational points on degree-2 curves are completely understood. Degree-3
curves (elliptic) are mostly understood (Mordell-Weil). Degree ≥ 4 curves
of genus ≥ 2 have only finitely many rational points (Faltings, 1983) —
this is why FLT for high n follows from Faltings before Wiles (but Faltings
doesn't give explicit bounds on n).

The genus hierarchy is the organizing principle: genus = topological handle count of the curve over C. Genus 0 (conics) are rational, so their Diophantine theory is trivial. Genus 1 (elliptic curves) are tori, which is why they carry a group structure — the unique handle gives the additive structure. Genus >= 2 curves have only finitely many rational points (Faltings, 1983). This is why degree matters: higher degree generally means higher genus, and higher genus means fewer rational points.

Wiles's proof of FLT via the modularity theorem (every semistable elliptic curve over Q is modular) was the first major instance of a non-abelian Langlands correspondence proved — placing FLT within the larger Langlands program that connects Galois representations to automorphic forms. See `06-ALGEBRAIC-NUMBER-THEORY.md` for class field theory (the abelian case) and `07-ANALYTIC-NUMBER-THEORY.md` for L-functions.
