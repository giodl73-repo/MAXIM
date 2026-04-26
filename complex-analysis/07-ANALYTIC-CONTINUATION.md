# Analytic Continuation

## The Big Picture

Analytic continuation is the process of extending a holomorphic function beyond its original domain of definition. The key fact making this possible: a holomorphic function is uniquely determined by its values on any set with an accumulation point (Identity Theorem). So if two definitions of a function agree on an overlapping region, they *must* agree everywhere they are both defined. This rigidity allows systematic extension.

The applications are profound: the Riemann zeta function starts as a series convergent only for Re(s) > 1, but can be continued to all of ℂ (except s=1) where it encodes information about primes. The gamma function, hypergeometric functions, and most "special functions" of mathematical physics are defined by analytic continuation.

```
ANALYTIC CONTINUATION — PROCESS
═══════════════════════════════════════════════════════════════════════════════

  START: f holomorphic on Ω₁
         ↓  find overlap with Ω₂ where another g is holomorphic
         ↓  check: f = g on Ω₁ ∩ Ω₂
         ↓
  EXTEND: g is the analytic continuation of f to Ω₂

  ┌─────────────────────────────────────────────────────────────────────┐
  │  IDENTITY THEOREM (uniqueness of continuation)                      │
  │                                                                     │
  │  f, g holomorphic on connected domain Ω                             │
  │  f = g on a set S ⊂ Ω with an accumulation point in Ω             │
  │  ⟹  f ≡ g on all of Ω                                             │
  │                                                                     │
  │  Consequence: continuation is UNIQUE when it exists                 │
  └─────────────────────────────────────────────────────────────────────┘

  MULTI-VALUED CONTINUATION (monodromy issue):
  Continuing along different paths may give different values
  if the path winds around a branch point
  → Resolved by Riemann surfaces (05-RIEMANN-SURFACES.md)
```

---

## Identity Theorem — Proof and Implications

**Theorem**: If f: Ω → ℂ is holomorphic on a connected domain Ω and the zero set Z(f) = {z ∈ Ω: f(z) = 0} has an accumulation point in Ω, then f ≡ 0.

**Proof**: Let Z̊ = interior of Z(f) and Z' = Ω \ Z̊. Both are open (Z̊ by definition; Z' because if z₀ ∈ Z' is not a zero, by continuity f ≠ 0 in a neighborhood; if z₀ is an isolated zero, the neighborhood minus z₀ has no zeros). Since Ω is connected and Ω = Z̊ ∪ Z', either Z̊ = ∅ or Z' = ∅.

If Z(f) has an accumulation point a, then a ∈ Z̊: the power series of f at a has all terms zero (if f^(n)(a) ≠ 0 for some n, then f would have an isolated zero at a — contradiction). So Z̊ ≠ ∅, hence Z' = ∅, hence f ≡ 0. □

**Consequence for continuation**: If f and g agree on a sequence aₙ → a ∈ Ω, then f − g = 0 on that sequence, which has accumulation point a, so f − g ≡ 0, i.e., f = g everywhere.

```
IDENTITY THEOREM IN ACTION:
  Two different formulas that agree on a small open set
  or an infinite sequence with accumulation point
  MUST be the same holomorphic function

  Examples:
  1) sin(z) and its Taylor series agree on ℝ ∩ D(0,ε)
     ⟹ sin(z) = Σ (-1)^n z^{2n+1}/(2n+1)!  everywhere on ℂ
  2) Γ(n+1) = n! for positive integers
     ⟹ Γ is the UNIQUE holomorphic extension of factorial
  3) ζ(s) = Σ n^{-s} for Re(s) > 1 has at most one continuation
```

---

## Power Series Continuation

**Direct continuation**: Given power series f(z) = Σ aₙ(z − z₀)ⁿ converging in disk D(z₀, R), pick a new center z₁ ∈ D(z₀, R). The Taylor series of f at z₁:

    f(z) = Σ_{n=0}^∞ f^(n)(z₁)/n! · (z − z₁)ⁿ

converges in D(z₁, R₁) where R₁ = dist(z₁, nearest singularity of f).

If the nearest singularity of f from z₁ is farther than from z₀ (which can happen when z₁ is displaced away from the singularity), then R₁ > R − |z₁ − z₀|. The new series may extend beyond the original disk.

```
CHAIN OF DISKS:

    D(z₀,R) ──z₁──→ D(z₁,R₁) ──z₂──→ D(z₂,R₂) ──→ ...

    Each new disk may extend beyond the previous one.
    Keep going to reach any point connected to z₀ by a path
    not hitting a singularity.
```

**Natural boundary**: Some functions cannot be continued beyond their circle of convergence because singularities are dense on the boundary circle. Example: f(z) = Σ z^{n!} has the unit circle as a natural boundary (singularities accumulate everywhere on |z| = 1).

---

## Monodromy Theorem

When you continue a function along two different paths from z₀ to z₁, you might get different values at z₁ (for multi-valued functions like log or √). The Monodromy Theorem characterizes when this happens:

**Theorem**: Let Ω be a simply connected domain and f a function element (power series) at z₀ ∈ Ω. If f can be analytically continued along any path in Ω starting at z₀, then the resulting continuation is path-independent: the value at z₁ depends only on z₁, not on the path.

In other words, on simply connected domains, analytic continuation gives a well-defined single-valued holomorphic function.

**Failure on multiply connected domains**: On ℂ \ {0}:
- Continuation of log(z) (principal branch starting at z=1) along CCW path around 0 gives log(z) + 2πi
- The monodromy map (z ↦ z, log z ↦ log z + 2πi) generates the multi-valuedness of log

```
MONODROMY OF log z:
  Path γ₁ (not encircling 0):  analytic continuation gives same branch
  Path γ₂ (encircling 0 once CCW):  log z ↦ log z + 2πi  (shifts branch)
  Path γ₃ (encircling 0 twice CCW): log z ↦ log z + 4πi

  Monodromy group of log z on ℂ \ {0}:  ℤ  (generated by +2πi shift)
```

---

## Schwarz Reflection Principle

A special and powerful technique for continuation across a boundary:

**Theorem**: Let Ω be a domain in the upper half-plane {Im(z) > 0} with part of its boundary on the real axis (a real interval I = (a,b)). Suppose f is holomorphic on Ω, continuous on Ω ∪ I, and **real-valued on I**. Then f extends analytically to the reflection Ω* = {z̄: z ∈ Ω} by:

    f(z̄) = f̄(z)    for z in the reflection Ω*

```
SCHWARZ REFLECTION PRINCIPLE:

       Upper half-plane          Lower half-plane
       ┌─────────────────┐       ┌─────────────────┐
       │     Ω ⊂ ℍ       │       │      Ω*         │
       │   f defined     │       │  f(z̄) = f̄(z)    │
       └─────────────────┘       └─────────────────┘
              │                        │
              └──────── I (real axis) ──┘
                          f real here

CONDITION: f real on I  ↔  f takes ℝ to ℝ  ↔  f satisfies the "reflection"
```

**Generalization**: If f maps an arc to a circle (not necessarily the real line), then f extends across the arc by the reflection in both the original arc and the image circle.

---

## From Continuation to the Prime Number Theorem

The analytic continuation of ζ(s) is not an end in itself — it is the first step in a proof chain that yields the Prime Number Theorem (PNT): π(x) ~ x/ln(x).

```
PROOF CHAIN:  CONTINUATION → FUNCTIONAL EQN → ZERO-FREE REGION → PNT
═══════════════════════════════════════════════════════════════════════

1. ANALYTIC CONTINUATION (this section):
   ζ(s) extends to all ℂ, meromorphic with pole at s=1.

2. FUNCTIONAL EQUATION:
   ξ(s) = ξ(1−s) confines non-trivial zeros to the critical strip 0 ≤ Re(s) ≤ 1.

3. ZERO-FREE REGION (de la Vallée-Poussin, 1896):
   ζ(1 + it) ≠ 0 for all t ∈ ℝ.
   Proof uses: Re(3 + 4cos θ + cos 2θ) ≥ 0 applied to log ζ.
   Strengthened: ζ(σ + it) ≠ 0 for σ > 1 − c/log|t| (classical zero-free region).

4. PERRON'S FORMULA (contour integration extracts π(x)):
   ψ(x) = Σ_{n≤x} Λ(n) = (1/2πi) ∫_{c-i∞}^{c+i∞} [-ζ'(s)/ζ(s)] x^s/s ds

   Shift contour left, picking up residues at:
   - s = 1 (pole of ζ): contributes x  (the main term)
   - s = ρ (non-trivial zeros): contribute -Σ_ρ x^ρ/ρ  (oscillatory corrections)

5. EXPLICIT FORMULA (von Mangoldt):
   ψ(x) = x − Σ_ρ x^ρ/ρ − log(2π) − (1/2)log(1 − x^{-2})

   The zero-free region forces |x^ρ| = x^{Re(ρ)} ≤ x^{1−c/log x} = x/e^c.
   So the sum over zeros is o(x), giving ψ(x) ~ x, which is the PNT.
```

The deeper the zero-free region (larger c), the better the error term. RH (Re(ρ) = 1/2 for all ρ) would give π(x) = Li(x) + O(√x log x) — the best possible error.

**Dirichlet L-functions and primes in progressions.** L(s, χ) = Σ χ(n) n^{−s} generalizes ζ to arithmetic progressions. For non-trivial characters χ, L(s, χ) continues to an *entire* function (no pole at s = 1 — the character orthogonality annihilates the divergence). The key step for Dirichlet's theorem: L(1, χ) ≠ 0 for all non-trivial χ mod q. This non-vanishing, proved via the same complex-analytic machinery (functional equation + zero-free region), gives: every arithmetic progression {a, a+q, a+2q, ...} with gcd(a,q) = 1 contains infinitely many primes.

---

## Analytic Continuation in Practice — The Riemann Zeta Function

This is the canonical, deepest example.

### Step 1: Dirichlet Series Definition (Re(s) > 1)

    ζ(s) = Σ_{n=1}^∞ n^{-s} = 1 + 2^{-s} + 3^{-s} + ...

Converges absolutely for Re(s) > 1. This is a Dirichlet series, not a power series.

### Step 2: Continuation to Re(s) > 0 (Step 1)

Use the **Abel summation / Euler-Maclaurin** method: write

    ζ(s) = s/(s−1) − s ∫_1^∞ {x}/x^{s+1} dx

where {x} = x − ⌊x⌋ is the fractional part. The integral converges for Re(s) > 0, giving an analytic continuation to Re(s) > 0 except for a simple pole at s = 1.

### Step 3: Continuation to all of ℂ (Riemann's Method)

Use the **integral representation** and the **functional equation**.

Start from the Mellin transform of e^{-t}:

    Γ(s) = ∫_0^∞ t^{s−1} e^{-t} dt    (Re(s) > 0)

Substituting t = nπx:
    Γ(s/2) π^{-s/2} n^{-s} = ∫_0^∞ x^{s/2−1} e^{-nπx} dx

Summing over n and using θ(x) = Σ e^{-nπx} (Jacobi theta function):

    π^{-s/2} Γ(s/2) ζ(s) = ∫_0^∞ x^{s/2−1} θ(x) dx    (schematically)

The Jacobi theta function satisfies the **functional equation**:

    θ(x) = x^{-1/2} θ(1/x)    (modularity)

This symmetry allows splitting the integral to obtain:

    ξ(s) = (1/2)s(s−1) π^{-s/2} Γ(s/2) ζ(s)

**Functional equation**: ξ(s) = ξ(1−s)

This extends ζ to all of ℂ:
- The factor Γ(s/2) has poles at s = 0, −2, −4, ... canceling corresponding poles
- ζ has a simple pole at s = 1 (from Γ(s/2) having a zero there... actually from the s−1 factor)
- ζ(s) extends meromorphically to all ℂ with one pole at s = 1

```
ζ(s) — ANALYTIC STRUCTURE AFTER CONTINUATION:

  Pole: s = 1  (simple, residue 1)
  Trivial zeros: s = −2, −4, −6, ... (from Γ(s/2) poles)
  Non-trivial zeros: in strip 0 ≤ Re(s) ≤ 1
                     symmetric about Re(s) = 1/2 (functional equation)
                     symmetric about real axis (complex conjugation)
  ζ(0) = −1/2,  ζ(−1) = −1/12,  ζ(−2) = 0 (trivial zero)
```

### The Enigmatic Values

Via the functional equation:
    ζ(−2n) = 0  (trivial zeros)
    ζ(2n) = (−1)^{n+1} (2π)^{2n} B_{2n} / (2·(2n)!)   (Bernoulli numbers)
    ζ(2) = π²/6,  ζ(4) = π⁴/90,  ζ(6) = π⁶/945

Regularization: ζ(−1) = −1/12 appears in string theory (Casimir effect regularization) as the "sum" 1 + 2 + 3 + ... = −1/12.

---

## Analytic Continuation and the Gamma Function

The Gamma function provides another clean example. Starting with:

    Γ(s) = ∫_0^∞ t^{s−1} e^{-t} dt    (converges for Re(s) > 0)

**Continuation via functional equation**: Γ(s+1) = s·Γ(s). Since Γ is defined for Re(s) > 0, this extends it to Re(s) > −1 (except s=0): Γ(s) = Γ(s+1)/s. Repeat: Γ(s) = Γ(s+n)/[s(s+1)···(s+n−1)] extends to Re(s) > −n.

Result: Γ extends to a meromorphic function on all of ℂ, with simple poles at s = 0, −1, −2, ... and no zeros.

---

## Special Functions as Analytic Continuations

Many "special functions" are defined by analytic continuation:

| Function | Original Definition | Continued To |
|---------|---------------------|-------------|
| ζ(s) | Σ n^{-s}, Re(s) > 1 | ℂ \ {1} |
| Γ(s) | ∫ t^{s-1}e^{-t}dt, Re(s) > 0 | ℂ \ {0,−1,−2,...} |
| L(s, χ) | Σ χ(n) n^{-s}, Re(s) > 1 | Entire (for non-trivial χ) |
| ₂F₁(a,b;c;z) | Power series, |z| < 1 | ℂ \ [1,∞) via integral |
| Bessel Jν(z) | Power series, all z | Entire in z |
| Polylogarithm Lin(z) | Σ z^k/k^n, |z| < 1 | ℂ \ [1,∞) |

---

## Decision Cheat Sheet

| Situation | Tool |
|----------|------|
| Extend f beyond its power series disk | Expand at new center; chain of disks |
| Show two formulas define the same function | Identity theorem: agree on sequence with accumulation point |
| Continue f across the real axis (f real on ℝ) | Schwarz reflection principle |
| Multi-valued continuation (paths matter) | Track monodromy; use Riemann surface |
| Extend ζ(s) to all of ℂ | Riemann's functional equation via theta function |
| Extend Γ(s) to negative reals | Repeated use of Γ(s) = Γ(s+1)/s |
| Prove continuation is unique | Identity theorem (connected domain) |

---

## Common Confusion Points

**Analytic continuation may not exist**: A function defined on Ω may have a natural boundary — a curve beyond which no continuation is possible. f(z) = Σ z^{n!} cannot be continued beyond the unit disk because the set of singularities on |z|=1 is dense.

**Continuation changes the domain, not the function**: The continued function is THE SAME function — it just has a larger domain. The uniqueness from the Identity Theorem means there is only one holomorphic function on any connected domain that agrees with f on Ω. So "analytic continuation of f" is unambiguous (on simply connected paths).

**The functional equation ξ(s) = ξ(1−s) is not obvious from the Dirichlet series**: The series Σ n^{-s} gives no indication of what happens at s = 1/2 or negative s. Only after continuation via the theta function integral does the functional equation emerge. This is the deep content of Riemann's original 1859 paper.

**ζ(−1) = −1/12 does not mean Σ n = −1/12**: The series 1+2+3+... diverges. ζ(−1) is the value of the CONTINUED zeta function at s=−1. It is a well-defined complex number but it is NOT the sum of 1+2+3+... in the usual sense. The equality ζ(s) = Σ n^{-s} holds only for Re(s) > 1.

**Schwarz reflection requires f to be REAL on the axis**: If f maps the real axis to a circle (not a line), you use the generalized reflection through that circle, not z ↦ z̄.
