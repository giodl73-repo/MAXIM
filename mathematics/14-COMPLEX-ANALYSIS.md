# Complex Analysis — Complete Reference

## The Big Picture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         COMPLEX ANALYSIS                                    │
│         The study of functions f: ℂ → ℂ that are complex-differentiable    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Layer 1: Algebra                                                           │
│  ℂ = algebraic closure of ℝ  →  z = x + iy, |z|, arg z, polar form        │
│                                                                             │
│  Layer 2: Geometry                                                          │
│  Complex plane ℂ ≅ ℝ² + extra structure from multiplication                │
│  Riemann sphere: ℂ ∪ {∞}  (one-point compactification)                    │
│                                                                             │
│  Layer 3: Analysis — the key concept                                        │
│  Holomorphic = complex-differentiable ⟺ Cauchy-Riemann equations          │
│  Holomorphic ⟹ analytic (equals its Taylor series)  ← NOT true in ℝ      │
│                                                                             │
│  Layer 4: Integration theory                                                │
│  Cauchy's theorem → Cauchy integral formula → residue theorem              │
│                                                                             │
│  Layer 5: Applications                                                      │
│  Real integrals • Fourier/Laplace inversion • Fluid dynamics               │
│  Conformal maps • Quantum mechanics • Signal processing                    │
│                                                                             │
│  The miracle: differentiability in ℂ is enormously more                   │
│  constraining than in ℝ. Once-differentiable ⟹ infinitely differentiable. │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## The Complex Numbers

### Algebraic Structure

ℂ = ℝ[i]/(i² + 1) — the ring of real polynomials modulo the relation i² = −1.
Every complex number: **z = x + iy**, x = Re(z), y = Im(z).

ℂ is algebraically closed (Fundamental Theorem of Algebra): every non-constant
polynomial over ℂ has a root. ℝ is not — x² + 1 = 0 has none.

**Operations**:
```
z₁ + z₂ = (x₁+x₂) + i(y₁+y₂)
z₁z₂   = (x₁x₂ − y₁y₂) + i(x₁y₂ + x₂y₁)
z̄ = x − iy    (complex conjugate)
|z|² = zz̄ = x² + y²
z⁻¹ = z̄/|z|²  (for z ≠ 0)
```

### Polar Form and Euler's Formula

```
z = r·e^(iθ) = r(cos θ + i sin θ)    r = |z|,  θ = arg z ∈ (-π, π]

Multiplication in polar form:
  z₁z₂ = r₁r₂ · e^(i(θ₁+θ₂))   — magnitudes multiply, angles add

De Moivre's theorem:  zⁿ = rⁿ e^(inθ)  →  (cos θ + i sin θ)ⁿ = cos nθ + i sin nθ

nth roots of unity:  ωₖ = e^(2πik/n),  k = 0,1,...,n−1
```

### The Riemann Sphere

Stereographic projection from the unit sphere S² in ℝ³ onto the complex plane,
with the north pole N mapping to ∞. Result: ℂ̂ = ℂ ∪ {∞} (the **Riemann sphere**,
also written ℙ¹(ℂ)).

Under this identification, Möbius transformations (see below) become exactly
the rotations/reflections of the Riemann sphere — a beautiful geometric fact.

---

## Holomorphic Functions: The Central Concept

### Complex Differentiability

f: U → ℂ (U ⊂ ℂ open) is **holomorphic** at z₀ if the limit

```
f'(z₀) = lim      f(z₀ + h) - f(z₀)
         h→0 (h∈ℂ)  ──────────────────
                           h
```

exists. The catch: **h → 0 along any path in ℂ** — not just along the real or
imaginary axis. This is a far stronger condition than real differentiability.

### Cauchy-Riemann Equations

Write f(x+iy) = u(x,y) + iv(x,y). f is holomorphic at z₀ = x₀ + iy₀ iff:

```
∂u/∂x = ∂v/∂y
∂u/∂y = −∂v/∂x

Compact notation:  ∂f/∂z̄ = 0   where  ∂/∂z̄ = ½(∂/∂x + i∂/∂y)
```

**Geometric meaning**: the Jacobian of f as a map ℝ² → ℝ² is a **rotation + scaling**
(conformal map) — the CR equations are exactly the condition that the Jacobian matrix
is of the form [[a, -b],[b, a]], i.e., multiplication by a complex number.

**Consequence**: if f = u + iv is holomorphic, then both u and v are **harmonic**:
∇²u = ∂²u/∂x² + ∂²u/∂y² = 0, and same for v. They are harmonic conjugates.

### The Miracle: C¹ ⟹ C∞ ⟹ Analytic

In real analysis, C¹ ⊋ C∞ ⊋ analytic (each containment is strict).
In complex analysis:

```
Holomorphic ⟺ C¹ + CR equations ⟺ C∞ ⟺ Analytic (equals Taylor series)
```

A function that's once complex-differentiable is automatically infinitely
differentiable and equals its Taylor series. There is no complex analogue of
smooth bump functions with compact support — those have no holomorphic extension.

### Standard Holomorphic Functions

| Function | f(z) | Notes |
|----------|------|-------|
| Polynomials | aₙzⁿ + ... + a₀ | Entire (holomorphic everywhere) |
| Rational | p(z)/q(z) | Holomorphic away from zeros of q |
| eᶻ | eˣ(cos y + i sin y) | Entire, periodic with period 2πi |
| sin z, cos z | (eⁱᶻ ∓ e⁻ⁱᶻ)/2i, (eⁱᶻ + e⁻ⁱᶻ)/2 | Entire, unbounded in imaginary direction |
| log z | ln|z| + i arg z | Multi-valued! Needs branch cut |
| zᵃ | e^(a log z) | Multi-valued for a ∉ ℤ |
| 1/z | z̄/|z|² | Holomorphic on ℂ\{0}; prototype for poles |

---

## Complex Integration

### Line Integrals

For a curve γ: [a,b] → ℂ (piecewise C¹):

```
∫_γ f(z) dz = ∫_a^b f(γ(t)) γ'(t) dt
```

This is a complex number. Key example:

```
∫_{|z|=r} z^n dz = { 2πi   if n = −1
                    { 0     if n ∈ ℤ, n ≠ −1
```

This single calculation is the engine of the whole theory.

### Cauchy's Theorem

**Statement**: If f is holomorphic on a simply connected domain U, and γ is a
closed curve in U, then:

```
∮_γ f(z) dz = 0
```

**Intuition**: Holomorphic functions have no "source" or "sink" — the integrand
has no residue to contribute. Contrast with 1/z on ℂ\{0}: ∮_{|z|=1} dz/z = 2πi ≠ 0
because 0 is excluded from the domain.

**Green's theorem connection**: Stokes' theorem in disguise. The CR equations
make the integrand exact.

### Cauchy Integral Formula

If f is holomorphic on and inside a simple closed curve γ (counterclockwise),
and z₀ is inside γ:

```
f(z₀) = (1/2πi) ∮_γ f(z)/(z−z₀) dz
```

**This is extraordinary**: the value of a holomorphic function at any interior
point is completely determined by its values on any surrounding curve.

Differentiating under the integral sign (valid for holomorphic f):

```
f^(n)(z₀) = (n!/2πi) ∮_γ f(z)/(z−z₀)^(n+1) dz
```

So all derivatives exist (confirming the miracle above), and are themselves given
by explicit contour integrals.

**Liouville's theorem**: A bounded entire function is constant.
*Proof*: |f'(z₀)| ≤ M/r for any circle of radius r, by the Cauchy estimate.
Let r → ∞. Then f'(z₀) = 0 everywhere.

**Fundamental Theorem of Algebra** (from Liouville): If p(z) has no roots, then
1/p(z) is entire and bounded → constant. Contradiction.

---

## Series and Singularities

### Taylor Series

If f is holomorphic at z₀, it has a Taylor series converging in the largest disk
centered at z₀ that fits inside the domain of holomorphicity:

```
f(z) = Σ_{n=0}^∞ aₙ(z−z₀)ⁿ,    aₙ = f^(n)(z₀)/n! = (1/2πi) ∮ f(z)/(z−z₀)^(n+1) dz
```

The radius of convergence R equals the distance from z₀ to the nearest singularity.
**This is why the Taylor series of 1/(1+x²) at x=0 has radius 1** — the nearest
singularity is at z = ±i, distance 1 from the origin, even though 1/(1+x²) is
perfectly smooth on all of ℝ.

### Laurent Series and Singularities

If f is holomorphic on an annulus r < |z−z₀| < R, it has a Laurent series:

```
f(z) = Σ_{n=−∞}^∞ cₙ(z−z₀)ⁿ = ... + c₋₂/(z−z₀)² + c₋₁/(z−z₀) + c₀ + c₁(z−z₀) + ...
```

The **principal part** is the sum of terms with n < 0. Classification of isolated
singularities at z₀:

```
┌─────────────────────────────────────────────────────────────────────────┐
│  SINGULARITY TYPES                                                      │
│                                                                         │
│  Removable singularity                                                  │
│  Principal part = 0. lim f(z) exists as z→z₀.                         │
│  Example: sin(z)/z at z=0. Define f(0)=1 → holomorphic everywhere.    │
│                                                                         │
│  Pole of order m                                                        │
│  cₙ = 0 for n < −m, c₋ₘ ≠ 0.  |f(z)| → ∞ as z → z₀.               │
│  Example: 1/z² has a pole of order 2 at 0.                            │
│  g(z) = (z−z₀)^m f(z) is holomorphic at z₀.                         │
│                                                                         │
│  Essential singularity                                                  │
│  Infinitely many negative terms.                                       │
│  Example: e^(1/z) at z=0.                                             │
│  Picard's Great Theorem: in any punctured neighborhood of an           │
│  essential singularity, f takes every complex value (with at most      │
│  one exception) infinitely often.                                       │
└─────────────────────────────────────────────────────────────────────────┘
```

**Meromorphic function**: holomorphic except for poles. Rational functions are
meromorphic on ℂ̂. The Gamma function Γ(z) is meromorphic on ℂ with simple
poles at z = 0, −1, −2, ...

---

## The Residue Theorem

### Residues

The **residue** of f at an isolated singularity z₀ is the coefficient c₋₁ in
the Laurent expansion:

```
Res(f, z₀) = c₋₁ = (1/2πi) ∮_{|z−z₀|=ε} f(z) dz
```

For a **simple pole** (order 1): `Res(f, z₀) = lim_{z→z₀} (z−z₀)f(z)`

For a **pole of order m**:
```
Res(f, z₀) = 1/(m−1)! · lim_{z→z₀} d^(m−1)/dz^(m−1) [(z−z₀)^m f(z)]
```

For f = g/h with simple zero of h at z₀:  `Res(f, z₀) = g(z₀)/h'(z₀)`

### The Residue Theorem

If γ is a positively oriented simple closed curve and f is holomorphic inside
and on γ except at isolated singularities z₁, ..., zₙ inside γ:

```
∮_γ f(z) dz = 2πi · Σₖ Res(f, zₖ)
```

**This is Cauchy's theorem + the Laurent expansion**, unified.

### Evaluating Real Integrals

This is where complex analysis becomes a superpower. Three standard techniques:

#### Type 1: Rational functions of sin and cos

```
∫₀^{2π} R(cos θ, sin θ) dθ
```
Substitute z = e^{iθ}, cos θ = (z+z⁻¹)/2, sin θ = (z−z⁻¹)/2i, dθ = dz/iz.
Converts to ∮_{|z|=1} rational function dz → residues at poles inside unit circle.

**Example**:
```
∫₀^{2π} dθ/(2 + cos θ) = 2π/√3
```

#### Type 2: Rational functions on the real line

```
∫_{-∞}^{∞} P(x)/Q(x) dx,   deg Q ≥ deg P + 2,  Q has no real roots
```

Close the contour with a large semicircle in the upper half-plane. The arc integral
→ 0 by Jordan's lemma. Result = 2πi · (sum of residues in upper half-plane).

**Example**:
```
∫_{-∞}^{∞} dx/(x²+1) = 2πi · Res(1/(z²+1), i) = 2πi · 1/(2i) = π
```

#### Type 3: Fourier-type integrals

```
∫_{-∞}^{∞} f(x) e^{iax} dx,   a > 0
```

Use upper semicircle (a > 0 makes e^{iaz} decay in upper half-plane).
Jordan's lemma ensures arc → 0. This is the Fourier transform evaluated by residues.

**Example**:
```
∫_{-∞}^{∞} e^{iax}/(x²+1) dx = πe^{-a}   (a > 0)
```

#### Keyhole contour, Bromwich contour, etc.

For integrands with branch cuts (√x, xᵃ, log x): use a keyhole contour that
wraps around the branch cut. For inverse Laplace transform: Bromwich contour
(vertical line in the s-plane, closed to the left). These are engineering workhorses
— the Laplace inversion formula is literally a residue calculation.

---

## Multivalued Functions and Branch Cuts

### The Logarithm

log z = ln|z| + i arg z is multivalued because arg z is defined only mod 2π.
To get a single-valued function, introduce a **branch cut** — a curve from 0 to ∞
that z is not allowed to cross.

**Principal branch**: cut along the negative real axis, arg z ∈ (−π, π]:
```
Log z = ln|z| + i Arg z    (capital Log = principal branch)
```

Holomorphic on ℂ \ (−∞, 0]. The discontinuity across the cut: the argument
jumps by 2π.

**Riemann surface**: the proper home for log z is a helical Riemann surface —
infinitely many sheets, one for each branch, connected along the branch cut.
On the Riemann surface, log z is single-valued and holomorphic.

### Branch Cuts for zᵃ

```
zᵃ = e^{a·Log z}    (principal branch)
```

For a = 1/2: the two branches of √z correspond to the two sheets of a
2-sheeted Riemann surface. Branch points at 0 and ∞.

For a = 1/n: n-sheeted surface, cyclic monodromy group ℤ/nℤ.

**Monodromy**: as z travels once around a branch point, the value of the
multivalued function gets permuted by a monodromy transformation. This connects
to covering spaces and the fundamental group (π₁).

---

## Conformal Mappings

### Definition

A holomorphic function f with f'(z₀) ≠ 0 is **conformal** (angle-preserving)
at z₀: it maps infinitesimal angles at z₀ to the same angles at f(z₀).
Magnitude |f'(z₀)| = local scaling factor. Argument arg f'(z₀) = rotation angle.

Conformal maps preserve the **shape** of infinitesimal figures (not size).

### Möbius Transformations (Fractional Linear Transformations)

```
f(z) = (az + b)/(cz + d),    ad − bc ≠ 0
```

**Properties**:
- Maps ℂ̂ → ℂ̂ bijectively
- Sends circles and lines to circles and lines (lines are "circles through ∞")
- Composed: Möbius ∘ Möbius = Möbius; the group is PGL(2,ℂ) ≅ PSL(2,ℂ)
- Three points in ℂ̂ determine a unique Möbius transformation sending them
  to any three other points (three degrees of complex freedom)
- The cross-ratio (z−z₃)(z₂−z₄)/((z−z₄)(z₂−z₃)) is preserved

**Standard maps**:

| Map | Formula | Use |
|-----|---------|-----|
| Translation | z + c | Shift domain |
| Rotation/scaling | az | Rotate and scale |
| Inversion | 1/z | Swaps 0 and ∞, inside/outside of unit circle |
| Joukowski | z + 1/z | Circle → ellipse/airfoil — fluid dynamics |
| Cayley map | (z−i)/(z+i) | Upper half-plane → unit disk |

### Riemann Mapping Theorem

**Statement**: Any simply connected proper open subset U of ℂ is conformally
equivalent to the unit disk 𝔻 = {|z| < 1}.

This is remarkable: the complex plane with a single point removed, a half-plane,
any polygon interior, a star-shaped domain — all conformally equivalent to each
other and to the disk.

The map is unique up to the three-parameter family of automorphisms of the disk:

```
Aut(𝔻) = { e^{iθ} (z−a)/(1−āz) : θ ∈ ℝ, a ∈ 𝔻 }   (Möbius transformations)
```

**Schwarz-Christoffel formula**: Explicit conformal map from the upper half-plane
to a polygon with interior angles α_k π:

```
f(z) = C ∫ dz / Π_k (z − xₖ)^{1−αₖ}
```

Used in fluid dynamics (flow around corners) and electrostatics (capacitor shapes).

---

## Harmonic Functions

### Connection to Complex Analysis

If f = u + iv is holomorphic, both u and v satisfy Laplace's equation:
∇²u = 0, ∇²v = 0. They are **harmonic conjugates**.

Conversely, any harmonic function u on a simply connected domain has a harmonic
conjugate v (unique up to constant), and u + iv is holomorphic.

**Mean value property**: if u is harmonic, its value at any point equals the
average over any circle centered at that point:

```
u(z₀) = (1/2π) ∫₀^{2π} u(z₀ + re^{iθ}) dθ
```

This is a consequence of the Cauchy integral formula.

### Dirichlet Problem

**Problem**: Find a harmonic function u in a domain U satisfying given boundary
conditions u = f on ∂U.

**Solution via conformal mapping**: Map U conformally to the unit disk (Riemann
mapping theorem), solve the Dirichlet problem on the disk via the Poisson kernel:

```
u(re^{iθ}) = (1/2π) ∫₀^{2π} P_r(θ−t) f(e^{it}) dt
P_r(θ) = (1 − r²)/(1 − 2r cos θ + r²)   (Poisson kernel)
```

Then pull back to U. This is the classical method for solving electrostatics,
heat conduction, and potential flow in 2D domains.

---

## Analytic Continuation

### The Principle

A holomorphic function defined on a small disk U₀ can often be extended to a
larger domain by "continuing" it along paths. The extension, if it exists, is
**unique** (identity theorem: two holomorphic functions agreeing on a set with a
limit point in a connected domain are identical everywhere).

```
Identity theorem: if f, g holomorphic on connected domain U,
and f = g on any set with an accumulation point in U, then f ≡ g on U.
```

This is the complex analytic version of "determined by infinitesimally small data."

### The Gamma Function

The Gamma function:
```
Γ(z) = ∫₀^∞ t^{z−1} e^{-t} dt    (Re z > 0)
```

Extended to all of ℂ by analytic continuation, with simple poles at z = 0, −1, −2, ...
Satisfies Γ(z+1) = zΓ(z), so Γ(n+1) = n! for n ∈ ℕ.

Reflection formula: Γ(z)Γ(1−z) = π/sin(πz).
Stirling: Γ(z) ~ √(2π/z) · (z/e)^z as |z| → ∞.

### The Riemann Zeta Function

```
ζ(s) = Σ_{n=1}^∞ n^{-s}   (Re s > 1)
```

Analytically continued to all of ℂ except s = 1 (simple pole).
Functional equation: ζ(s) = 2^s π^{s−1} sin(πs/2) Γ(1−s) ζ(1−s).

**Riemann Hypothesis**: all non-trivial zeros lie on the critical line Re s = 1/2.
Equivalent to the sharpest possible error term in the prime counting function:
π(x) = Li(x) + O(√x log x).

### Zeta Function and the Primes

The deepest connection between ζ and number theory runs through complex analysis:

```
Euler product (Re s > 1):
  ζ(s) = Π_{p prime} (1 − p^{-s})^{-1}

This is the fundamental bridge between ζ and the primes.
Proof: Σ n^{-s} = Π_p (1 + p^{-s} + p^{-2s} + ...) = Π_p (1-p^{-s})^{-1}
by unique factorization.

Consequence: ζ(s) ≠ 0 for Re s > 1 (product of nonzero factors).
The behavior of ζ near Re s = 1 governs the distribution of primes.

Prime number theorem via complex analysis:
  π(x) ~ x/log x  as x → ∞.
  Proof strategy: Perron's formula converts sum Σ_{n≤x} f(n) to a contour
  integral (1/2πi) ∫_{c-i∞}^{c+i∞} F(s) x^s/s ds.
  For f(n) = Λ(n) (von Mangoldt): ψ(x) = (1/2πi) ∫ (-ζ'/ζ)(s) x^s/s ds.
  Moving the contour left: contributions come from poles of -ζ'/ζ.
  The pole at s=1 gives ψ(x) ~ x.
  Non-trivial zeros ρ of ζ give error terms x^ρ/ρ.
  Zero-free region Re s > 1 - c/log|Im s| bounds the error:
    ψ(x) = x + O(x e^{-c√log x})  → PNT with error bound.
  Riemann Hypothesis ⟹ ψ(x) = x + O(√x log² x)  (optimal).

Dirichlet L-functions: L(s, χ) = Σ_{n=1}^∞ χ(n) n^{-s}
  χ: (ℤ/qℤ)* → ℂ* is a Dirichlet character (completely multiplicative).
  Euler product: L(s, χ) = Π_p (1 - χ(p)p^{-s})^{-1}.
  Same analytic methods prove Dirichlet's theorem:
    If gcd(a,q) = 1, there are infinitely many primes p ≡ a (mod q).
  Proof: show L(1, χ) ≠ 0 for non-principal χ, so the product doesn't vanish.
```

---

## Riemann Surfaces

Riemann surfaces are the natural domain for multivalued functions like log z and
√z — they make these functions single-valued by "unfolding" the sheets.

```
Definition: A Riemann surface is a 1-dimensional complex manifold:
  a Hausdorff space with a holomorphic atlas (compatible complex charts).
  Every open subset of ℂ is trivially a Riemann surface.
  Non-trivial examples are constructed via analytic continuation or as
  algebraic curves.

Construction: algebraic curves P(z, w) = 0.
  Given a polynomial relation P(z, w) = 0, the set of solutions (z, w) ∈ ℂ²
  (with smooth points) forms a Riemann surface. The function w = f(z)
  defined implicitly by P is single-valued on this surface.

Example: w² = z (square root)
  2-sheeted surface: two solutions w = ±√z glued along the branch cut.
  Branch points at z = 0 and z = ∞ (where the two sheets join).
  Topologically: S² with two punctures glued in a specific way — a sphere.

Example: w² = z(z-1)(z-2)  (genus-1 curve)
  4 branch points (0, 1, 2, ∞). Glue two sheets along two cuts.
  Topologically: a torus (genus 1 — one handle).

Genus formula (Riemann-Hurwitz):
  For a degree-d holomorphic map f: S → T between compact Riemann surfaces:
    2g(S) - 2 = d(2g(T) - 2) + Σ (e_p - 1)
  where the sum is over ramification points p and e_p is the ramification index.
  For an algebraic curve defined by w^n = Π(z - aᵢ)^{mᵢ}: count branch points,
  compute genus. Genus 0 = rational function (sphere). Genus 1 = elliptic curve.

Compact Riemann surfaces = smooth projective algebraic curves over ℂ.
  This is the entry point into algebraic geometry.
  Classification: completely determined (up to isomorphism) by genus g and
  moduli — for g ≥ 2, by 3g−3 complex parameters (Riemann's moduli count).
```

---

## Applications

### Fluid Dynamics (Potential Flow)

2D incompressible irrotational flow: velocity field **v** = ∇φ where ∇²φ = 0
(potential flow). With stream function ψ (∇²ψ = 0), the **complex potential**
w = φ + iψ is holomorphic.

```
Velocity:  u − iv = dw/dz = complex velocity

Flow past a cylinder:  w(z) = U(z + a²/z)
Joukowski airfoil:    w(z + 1/z) maps cylinder → airfoil
```

The Kutta-Joukowski theorem: lift L = ρU·Γ where Γ = ∮ **v**·d**l** is the
circulation — a residue calculation.

### Electrostatics (2D)

Electric potential V satisfies ∇²V = 0 (Laplace's equation) between conductors.
The complex potential φ + iψ maps the geometry to a standard form via conformal
maps. Capacitance, field lines, equipotentials all follow.

### Quantum Mechanics

- **Path integrals**: Wick rotation t → iτ (imaginary time) converts the
  oscillatory Feynman integral to a Gaussian → tractable.
- **Operator spectrum**: Poles of the resolvent (zI − H)⁻¹ in the complex
  z-plane are exactly the eigenvalues of the Hamiltonian H.
- **S-matrix**: Scattering amplitude as a function of complex energy; poles =
  bound states, cuts = scattering thresholds.

### Laplace Inversion (Bromwich Contour)

The inverse Laplace transform:
```
f(t) = (1/2πi) ∫_{c−i∞}^{c+i∞} F(s) e^{st} ds   (Bromwich contour)
```

is evaluated by closing the contour to the left and summing residues of F(s)e^{st}
at the poles of F. For F(s) = 1/(s(s+1)): poles at s=0 and s=−1,
giving f(t) = 1 − e^{-t}. Every inverse Laplace table entry is a residue computation.

### Signal Processing: Hardy Spaces

H² (Hardy space) = holomorphic functions on the unit disk with bounded L²-norm
on the boundary.

```
Paley-Wiener theorem (precise bridge between Fourier and complex analysis):
  f ∈ L²(ℝ) with supp(f) ⊆ [0, ∞)
  ⟺  its Fourier transform F(ω) = ∫ f(t)e^{-iωt}dt
      extends to a holomorphic function in the upper half-plane with
      sup_{y>0} ∫ |F(x+iy)|² dx < ∞  (i.e., F ∈ H²(upper half-plane)).

  In other words: causal L² signals in time ↔ H² functions in frequency.
  This gives the precise complex-analytic characterization of causality.

Inner-outer factorization:
  Every H² function f = f_inner · f_outer (uniquely up to constants).

  Inner function: |f_inner(e^{iθ})| = 1  a.e. on the boundary.
    Finite Blaschke products: f_inner = e^{iθ} Π (z-aₖ)/(1-āₖz)
    (zeros inside the disk with their reflections outside — all-pass filters)
    Infinite Blaschke products or singular inner functions: pure phase, no zeros.
    Engineering interpretation: inner functions = all-pass filters (magnitude 1,
    only phase shift). Minimum phase condition: no zeros in the disk.

  Outer function: determined entirely by its boundary modulus |f_outer(e^{iθ})|.
    f_outer(z) = exp((1/2π) ∫ e^{iθ}+z/e^{iθ}-z · log|f(e^{iθ})| dθ)
    Engineering interpretation: outer functions = minimum-phase components —
    the part of a filter that can be causally inverted.

H∞ (bounded analytic functions on disk): appear in robust control theory.
  H∞ control: minimize ‖T‖_∞ = sup_ω |T(jω)| over stabilizing controllers.
  The H∞ norm bounds worst-case gain over all frequencies.
  Solved via Riccati equations and related to the small-gain theorem.
```

---

## Key Theorems — Reference Card

| Theorem | Statement |
|---------|-----------|
| **Cauchy-Riemann** | f holomorphic ⟺ ∂f/∂z̄ = 0 ⟺ Jacobian is a scaled rotation |
| **Cauchy's theorem** | ∮_γ f dz = 0 for f holomorphic inside γ |
| **Cauchy integral formula** | f(z₀) = (1/2πi) ∮ f(z)/(z−z₀) dz |
| **Taylor theorem** | Holomorphic ⟺ analytic (equals its Taylor series) |
| **Laurent expansion** | Classifies singularities: removable / pole / essential |
| **Residue theorem** | ∮_γ f dz = 2πi Σ Res(f, zₖ) |
| **Liouville** | Bounded entire ⟹ constant |
| **FTA** | Every non-constant polynomial over ℂ has a root (from Liouville) |
| **Riemann mapping** | Simply connected proper open U ≅ unit disk |
| **Identity theorem** | Two holomorphic functions agreeing on a set with a limit point are identical |
| **Picard's great theorem** | Near an essential singularity, f takes every value except one, infinitely often |
| **Open mapping** | Non-constant holomorphic maps are open maps |
| **Maximum modulus** | |f| cannot have an interior maximum |
| **Riemann-Hurwitz** | 2g(S)−2 = d(2g(T)−2) + Σ(e_p−1) for branched cover S → T |

---

## Decision Cheat Sheet

| Need | Technique |
|------|-----------|
| Evaluate ∫₀^{2π} R(cos θ, sin θ) dθ | Substitute z = e^{iθ}, use residues inside unit circle |
| Evaluate ∫_{-∞}^{∞} rational dx | Close semicircle, residues in upper half-plane |
| Evaluate ∫_{-∞}^{∞} f(x)e^{iax} dx | Close upper semicircle (a > 0), Jordan's lemma |
| Evaluate ∫₀^{∞} f(x)xᵃ dx | Keyhole contour around branch cut on positive real axis |
| Invert Laplace transform F(s) | Bromwich contour, residues of F(s)e^{st} |
| Solve 2D Laplace equation in a domain | Conformal map to disk, Poisson kernel |
| Determine if f is holomorphic | Check CR equations: ∂u/∂x = ∂v/∂y, ∂u/∂y = −∂v/∂x |
| Find type of singularity at z₀ | Compute Laurent series; count negative-index terms |
| Compute a specific residue | For simple pole: lim (z−z₀)f(z); for order m: derivative formula |
| Extend f to a larger domain | Analytic continuation along paths; unique where it exists |
| Count zeros of f inside a contour | Argument principle: (1/2πi)∮ f'/f dz = Z − P |
| Connect primes to ζ(s) | Euler product + Perron's formula + zero-free region |
| Characterize causal L² signals | Paley-Wiener: Fourier transform ∈ H²(upper half-plane) |
| Factor a filter into all-pass + minimum-phase | Inner-outer factorization of H² |

---

## Common Confusion Points

**Real vs. complex differentiability**: A function ℝ² → ℝ² can be C∞ without
being complex differentiable. The CR equations are the extra constraint.
e.g., f(z) = z̄ = x − iy is C∞ as a map ℝ² → ℝ² but **not** holomorphic:
∂u/∂x = 1 ≠ −1 = ∂v/∂y fails.

**Analyticity in ℂ vs ℝ**: In ℝ, "smooth" and "analytic" are genuinely different.
The function e^{−1/x²} (extended by 0 at x=0) is C∞ but not analytic at 0.
In ℂ, once-differentiable ⟹ analytic. The gap that exists in ℝ doesn't exist in ℂ.

**Branch cuts**: log z and z^(1/2) are not functions on ℂ; they're sections of
line bundles on ℂ\{0}, or single-valued functions on Riemann surfaces.
Choosing a branch cut is choosing a trivialization of that bundle.

**Poles vs. zeros**: if f has a zero of order m at z₀, then 1/f has a pole of
order m there. Zeros and poles cancel when multiplied. The order of a zero is
positive; the order of a pole is negative — meromorphic functions have "orders."

**Contour orientation**: Counterclockwise is positive in the residue theorem.
The interior is to the left when traversing the boundary — same convention as
Stokes' theorem (and it is Stokes' theorem).

**Multi-valuedness and path-dependence**: ∫_γ dz/z from 1 to 1 around a
circle gives 2πi, not 0, because log z is multi-valued. Cauchy's theorem requires
f holomorphic on the enclosed region — here z=0 prevents that.

**Riemann surfaces vs. branch cuts**: A branch cut is a surgery that makes a
multivalued function single-valued by forbidding certain paths. A Riemann surface
is the intrinsic geometric object — no forbidden paths, just a different space.
The branch cut approach is local and convenient; the Riemann surface is global and
canonical. For topology (monodromy, fundamental group), always use the surface.
