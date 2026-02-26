# Early Modern Mathematicians — Descartes, Pascal, Newton, Leibniz, Bernoulli Family

## Timeline and Intellectual Lineage

```
                    EARLY MODERN MATHEMATICS (1600–1720)
                    =====================================

1596            1623          1643          1646        1654 (birth)
  |               |             |             |             |
DESCARTES       PASCAL        NEWTON        LEIBNIZ    Joh. BERNOULLI
  |               |             |             |       (+ brother Jakob
  |               |             |             |         b.1655)
  v               v             v             v             v
Analytic       Pascal's       Fluxions,    Calculus,    Calculus
geometry       triangle,      Principia,   notation,    wars (took
Cartesian      probability    optics,      binary,      Leibniz side)
coordinates    (with          gravity      logic        + hydrodynamics
Method of      Fermat)                     machines
Doubt
(philosophy)

KEY INTELLECTUAL CONNECTIONS:
  Descartes → coordinates → Newton & Leibniz (algebraic calculus possible)
  Fermat + Pascal → probability → Bernoullis → Laplace → statistics
  Newton ↔ Leibniz → calculus (independent discovery, different notation)
  Leibniz → binary → Boolean algebra → computing
  Bernoullis → series, differential equations → Euler
```

---

## René Descartes (1596–1650)

### Who He Was

French philosopher and mathematician. Lived mostly in the Dutch Republic to
escape religious and political pressure. *Discourse on the Method* (1637) was
the main work — philosophy plus three appendices: *Dioptrics*, *Meteorology*,
and *La Géométrie*.

### The Contribution: Analytic Geometry

*La Géométrie* (1637) is a single appendix that transformed mathematics.
Descartes showed that geometric problems could be translated into algebraic
equations, solved algebraically, and translated back.

```
WHAT ANALYTIC GEOMETRY UNIFIED
================================

Before Descartes:
  Geometry  ←──────────┐    Two separate domains.
                        │    Geometric problems solved geometrically.
  Algebra   ←──────────┘    Algebraic problems solved algebraically.

After Descartes:
  Geometric curve  ←──→  Algebraic equation
                              |
                          Can now use algebra to solve geometry
                          Can now visualize algebra geometrically

Example: "circle of radius r centered at origin"
  Before: geometric construction
  After:  x² + y² = r²
  You can now differentiate it, parameterize it, substitute, combine with
  other equations — the full power of algebra applied to geometry.
```

**The coordinate system**: A point in the plane uniquely specified by (x, y).
This is now so obvious it is invisible. Before Descartes, there was no such
universal system. Every geometric proof was specific to the figure at hand.
Coordinates made geometry **computational**.

**The degree/dimension connection**: A degree-1 equation is a line. Degree-2
is a conic. Degree-3 is a cubic surface. The algebraic degree of an equation
determines the geometric complexity of the curve. This is now fundamental to
algebraic geometry.

### What He Actually Proved

Descartes gave the first general method for finding tangent lines to curves —
a precursor to differentiation. He also solved the classic problem of
Pappus (relating a point to multiple lines by cross-ratio conditions) using
his coordinate method, demonstrating the technique's power.

### Descartes' Rule of Signs

If p(x) is a polynomial with real coefficients, the number of positive real
roots is equal to the number of sign changes in the sequence of coefficients,
or less by an even number. This is still taught and used.

---

## Blaise Pascal (1623–1662)

### Who He Was

French mathematician, physicist, inventor, philosopher. Child prodigy:
reportedly proved Euclidean theorems himself as a child before reading Euclid.
Built one of the first mechanical calculators (the Pascaline) at age 18.
Late in life had a religious conversion and devoted himself to theology.

### The Contribution: Probability Theory and Pascal's Triangle

**Pascal's triangle** (known earlier in Islamic and Chinese mathematics, but
Pascal systematized its properties):

```
PASCAL'S TRIANGLE
=================
         1
        1 1
       1 2 1
      1 3 3 1
     1 4 6 4 1
    1 5 10 10 5 1
           ...

Row n, position k = C(n,k) = n! / (k!(n-k)!)

Properties:
  - Each entry = sum of two above it
  - Row n sums to 2ⁿ
  - Diagonal 1: natural numbers
  - Diagonal 2: triangular numbers 1, 3, 6, 10, ...
  - Diagonal 3: tetrahedral numbers 1, 4, 10, 20, ...
  - Fibonacci numbers appear as diagonal sums
  - Sierpinski triangle appears when coloring odd/even entries
```

**Probability theory** — Pascal and Fermat (in correspondence, 1654) solved the
"problem of points": if two players are gambling and must stop early, how should
the stakes be divided? Their exchange is the founding document of probability theory.

```
THE PROBLEM OF POINTS
======================
Player A needs 3 more wins. Player B needs 2 more wins.
How to divide stakes fairly?

Pascal/Fermat's key insight:
  Consider all games that COULD be played (even if not needed).
  At most 3+2-1 = 4 more games needed.
  Enumerate all 2⁴ = 16 scenarios.
  Count wins for each player.
  Divide stakes proportionally.

This is EXPECTED VALUE reasoning, which is the foundation of:
  - Actuarial science (insurance)
  - Options pricing (Black-Scholes)
  - Bayesian inference
  - Machine learning loss functions
```

**Pascal's wager** — the first attempt at applying decision theory to theology.
Wrong in many ways, but the **structure** of the argument (expected value under
uncertainty with infinite payoffs) is mathematically interesting.

### Pascal's Theorem (Projective Geometry)

If a hexagon is inscribed in a conic (circle, ellipse, etc.), the three pairs
of opposite sides meet at collinear points. A purely geometric result, proved
by a 16-year-old.

---

## Isaac Newton (1643–1727)

### Who He Was

English mathematician and physicist. Cambridge Lucasian Professor of Mathematics.
One of the two independent inventors of calculus. His *Principia Mathematica* (1687)
is the most influential scientific text ever written. He held the same professorship
later held by Stephen Hawking and currently by Michael Cates.

### The Contribution: Calculus (Fluxions)

Newton developed his calculus ("method of fluxions") starting ~1665–1666, during
the plague years when Cambridge was closed. He did not publish it until much later,
which triggered the priority dispute with Leibniz.

```
NEWTON'S FLUXIONS — WHAT HE ACTUALLY DID
==========================================

Newton's framing:
  A "fluent" (flowing quantity) — what we'd call a variable that changes with time
  A "fluxion" — the rate of change of the fluent (what we'd call the derivative)
  An "ultimate ratio" — what we'd call the limit of Δy/Δx as Δx → 0

Newton's notation (what died):
  ẋ (dot above) = dx/dt  (velocity if x is position)
  ẍ (two dots)  = d²x/dt²  (acceleration)

Leibniz's notation (what survived):
  dy/dx  (the differential ratio — suggests a fraction, enables chain rule)
  ∫ y dx  (elongated S for summa — integral)

Newton's method gave correct answers but Leibniz's notation was
more manipulable — you could push symbols around and get results.
This is why Leibniz's notation dominates.
```

Newton's **Second Fundamental Theorem of Calculus** (which he proved):
differentiation and integration are inverse operations.

```
FUNDAMENTAL THEOREM OF CALCULUS
=================================

d/dx [ ∫ₐˣ f(t) dt ] = f(x)

That is: differentiation undoes integration.
Equivalently: ∫ₐᵇ f'(x) dx = f(b) - f(a)

This connects two apparently separate concepts:
  - The derivative (instantaneous rate of change)
  - The integral (area under a curve)
They are inverse operations. This is not obvious.
Newton proved it. Leibniz proved it independently.
```

### The Principia — Applied Calculus at Civilizational Scale

*Philosophiæ Naturalis Principia Mathematica* (1687):
- Newton's three laws of motion
- Law of universal gravitation: F = Gm₁m₂/r²
- Proof that Kepler's laws follow mathematically from gravitation
- Tidal theory, precession of equinoxes, motion of comets

The Principia was written in geometric form (to be understood by those who knew
Euclid but not calculus). The underlying derivations used calculus. Newton then
translated the results into geometric proofs for publication.

### The Binomial Theorem (General Form)

Newton extended the binomial theorem to fractional and negative exponents:
(1+x)ⁿ = 1 + nx + n(n-1)x²/2! + n(n-1)(n-2)x³/3! + ...
for any real n (not just positive integers). This is an infinite series when n
is not a positive integer, and it converges for |x| < 1.

---

## Gottfried Wilhelm Leibniz (1646–1716)

### Who He Was

German polymath — mathematician, philosopher, jurist, diplomat, librarian.
Independent inventor of calculus, simultaneously with Newton. His notation
is what we use. He also invented binary arithmetic, designed mechanical
calculators, and developed a philosophical system (Monadology) that influenced
German idealism.

### The Contribution: Calculus (with Better Notation)

Leibniz developed his calculus independently ~1675–1677, published in 1684–1686
— before Newton published, though Newton developed it first.

```
LEIBNIZ'S NOTATIONAL GENIUS
=============================

Leibniz was obsessive about notation — he believed good symbols did
half the mathematical work. He was right.

The integral sign ∫ — elongated S for "summa" (sum of infinitesimals)
The differential dx — "an infinitely small change in x"

Chain rule in Leibniz notation:
  dy/dx = (dy/du)(du/dx)
  This "looks like" fraction cancellation. That's not why it works,
  but the notation makes it suggestive and manipulable.

Product rule:
  d(uv) = u dv + v du
  Looks like you're just distributing d.

Compare Newton's notation:
  (uv)' = u'v + uv'
  Correct, but doesn't suggest the substitution tricks.

Leibniz notation is why calculus is "algebraically manipulable."
```

### Binary Arithmetic

Leibniz independently developed binary (base-2) arithmetic, inspired by the
I Ching. He saw binary as philosophically deep: from 0 and 1, everything.
He built no computers — that took 250 years — but the arithmetic system
underlying every computer is Leibniz's.

### The Calculus Priority Dispute

```
TIMELINE OF THE DISPUTE
========================

1665-1666: Newton develops fluxions (not published)
1673: Leibniz visits London, sees some Newton manuscripts
1675-1677: Leibniz develops his calculus independently
1684: Leibniz publishes calculus in Acta Eruditorum
1687: Newton publishes Principia (uses calculus, doesn't fully disclose method)
1693: Newton publishes calculus in Wallis's Algebra
1700s: British loyalists accuse Leibniz of plagiarism
1713: Royal Society investigation — chaired by Newton himself (!)
       Finds Leibniz guilty — conflicts of interest ignored
1716: Leibniz dies, largely abandoned by patrons, isolated

Modern verdict: Independent discovery.
Newton first. Leibniz's notation better. Leibniz published first.
The dispute set British mathematics back ~100 years
(British stubbornly using Newton's notation, avoiding Leibniz's superior system).
```

---

## The Bernoulli Family (Late 1600s–1800)

### Who They Were

```
BERNOULLI FAMILY TREE (mathematical members)
=============================================

Nikolaus Bernoulli (1623-1708) — merchant, not mathematician
           |
    +-------+-------+
    |               |
Jakob I         Johann I        ← The two great brothers
(Jacques)       (Jean)
(1654-1705)     (1667-1748)
    |               |
    |           +---+---+---+
    |           |       |   |
 Nikolaus I  Nikolaus II  Daniel   Johann II
 (1687-1759) (1695-1726) (1700-1782) (1710-1790)
                              |
                          Hydrodynamics
                          Bernoulli's principle
                          Bernoulli trials
                          St. Petersburg paradox
```

### Jakob Bernoulli (1654–1705)

**Series**: Proved divergence of the harmonic series Σ 1/n → ∞.
Computed the sum Σ 1/n² (proved it converges) but could not find the exact value.
His brother Johann also couldn't. It took Euler (their student).

**Bernoulli numbers**: In *Ars Conjectandi* (published posthumously 1713), defined
the numbers B₁, B₂, ... that appear in the sums of powers formulas:
Σₖ₌₁ⁿ kᵐ = (polynomial in n involving Bernoulli numbers)
These appear in the Taylor series for tan(x), in number theory, and famously
in the first computer program: Ada Lovelace's algorithm to compute them.

**The Brachistochrone Problem**: "Find the curve of fastest descent."
(Posted as a challenge to mathematicians.) Johann solved it. Jakob solved it
differently. The answer: the cycloid. This led to the calculus of variations.

**Bernoulli's inequality**: (1+x)ⁿ ≥ 1 + nx for x > -1, n ≥ 1.
Used everywhere in analysis.

### Johann Bernoulli (1667–1748)

**L'Hôpital's Rule**: Johann Bernoulli taught Guillaume de l'Hôpital calculus
and sold him the right to publish his discoveries. The rule for evaluating limits
of the form 0/0 by taking derivatives of numerator and denominator is actually
Bernoulli's. L'Hôpital published it (legally — he paid), but it's Bernoulli's.

```
L'HOPITAL'S RULE (ACTUALLY BERNOULLI'S)
========================================

  lim[x→a] f(x)/g(x) where both f(a)=g(a)=0

  = lim[x→a] f'(x)/g'(x)   if this limit exists

Application: lim[x→0] sin(x)/x = lim[x→0] cos(x)/1 = 1
This is used constantly in Fourier analysis, signal processing, etc.
```

**Exponential integral**: Johann worked out properties of eˣ and its integral.
He also computed the catenary (shape of a hanging chain) — an important
structural engineering curve (the Gateway Arch is a catenary).

### Daniel Bernoulli (1700–1782)

**Hydrodynamics**: *Hydrodynamica* (1738) established the relationship between
fluid pressure and velocity — Bernoulli's principle:

```
BERNOULLI'S PRINCIPLE
=====================
For inviscid incompressible flow along a streamline:

  P + ½ρv² + ρgh = constant

  P = pressure, ρ = density, v = velocity, h = height

Qualitative: where fluid speeds up, pressure drops.

Applications:
  - Airplane lift (faster air over wing → lower pressure on top)
  - Venturi meter (flow rate from pressure difference)
  - Carburetor (fuel injection by low pressure)
  - Pitot tube (airspeed indicator)
```

**Bernoulli trials** (named after Jakob, applied by Daniel): A sequence of
independent experiments each with probability p of success. The foundation
of the binomial distribution and modern probability.

**St. Petersburg Paradox**: A coin-flip game where the expected monetary payoff
is infinite, yet no rational person would pay much to play it. Daniel Bernoulli's
resolution: **diminishing marginal utility** — a dollar is worth less to a rich
person than a poor one. This is the first formal treatment of utility in economics,
foundational to game theory and behavioral economics.

---

## Comparison Table

| Figure | Dates | Core Contribution | Built On | Built Into |
|--------|-------|-------------------|----------|------------|
| **Descartes** | 1596–1650 | Analytic geometry, coordinates | Vieta (algebra), Euclid | Newton, Leibniz (calculus needed coordinates) |
| **Pascal** | 1623–1662 | Probability theory, Pascal's triangle | Fermat (correspondence) | Huygens, Bernoullis, Laplace |
| **Newton** | 1643–1727 | Calculus (fluxions), universal gravitation | Descartes, Barrow, Kepler | All of classical mechanics, physics |
| **Leibniz** | 1646–1716 | Calculus (better notation), binary | Descartes, Pascal, Newton | All modern calculus notation, computing |
| **Jakob Bernoulli** | 1654–1705 | Series, Bernoulli numbers, probability | Leibniz (his teacher) | Euler, number theory, statistics |
| **Johann Bernoulli** | 1667–1748 | Calculus applications, L'Hôpital's rule | Leibniz | Euler (his student), fluid mechanics |
| **Daniel Bernoulli** | 1700–1782 | Hydrodynamics, expected utility | Newton, Jakob Bernoulli | Aerodynamics, economics |

---

## Who to Cite for What

| Concept | Cite | Notes |
|---------|------|-------|
| Cartesian coordinates | Descartes | *La Géométrie* (1637) |
| Analytic geometry / curves as equations | Descartes | |
| Pascal's triangle properties | Pascal | Though known earlier in Asia/Islam |
| Probability (founding) | Pascal + Fermat | 1654 correspondence |
| Expected value | Pascal | Problem of Points |
| Calculus — fundamentals, physics applications | Newton | Published later, but developed first |
| Calculus — notation, symbolic manipulation | Leibniz | Published first; his notation is used |
| Binary arithmetic | Leibniz | ~1679, published 1703 |
| L'Hôpital's Rule (actual) | Johann Bernoulli | Published under l'Hôpital |
| Bernoulli numbers | Jakob Bernoulli | *Ars Conjectandi* |
| Bernoulli's principle (fluids) | Daniel Bernoulli | *Hydrodynamica* |
| Diminishing marginal utility | Daniel Bernoulli | St. Petersburg paradox (1738) |

---

## Common Confusion Points

**"Leibniz stole calculus from Newton"** — The Royal Society investigation of 1713
was chaired by Newton himself. Its verdict was not neutral. Modern historians of
mathematics consider the evidence for independent discovery strong. Leibniz saw
some Newton manuscripts in 1673, but these were on series expansions, not the
full calculus. The core ideas of his calculus are in letters dated before any
contact with Newton's calculus.

**"The Principia proves gravity with calculus"** — The Principia is written in
classical geometric form (like the Elements), not in calculus. Newton translated
his calculus results into geometry for publication, because that was the accepted
language of proof. The calculus was the working method; the published proofs
look Euclidean.

**"L'Hôpital's Rule is l'Hôpital's"** — It is Johann Bernoulli's. Guillaume de
l'Hôpital paid for tutoring rights and publication rights. The arrangement was
legally sound for the time; the naming was accidental history.

**"Bernoulli's principle is why planes fly"** — It contributes, but the
Bernoulli effect alone doesn't explain airplane lift correctly (the "equal
transit time" fallacy). Lift comes from the angle of attack and Newton's third
law (air pushed down = lift force up) in combination with pressure effects.
"Pure Bernoulli" lift explanations in textbooks are simplified to the point of
error.

**"Pascal invented the calculator"** — He built a functional mechanical calculator
(the Pascaline) that could add and subtract (with carrying). Leibniz later built
one that could multiply. Neither was practically useful — too unreliable, too
expensive. But they are conceptual ancestors of mechanical computing.
