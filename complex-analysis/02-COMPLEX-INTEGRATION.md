# Complex Integration and Cauchy's Theorem

## The Big Picture

Complex integration transforms "what is the value of a line integral?" into "what singularities does f have inside the contour?" For holomorphic functions, line integrals are completely path-independent. Cauchy's theorem and the Cauchy integral formula are the core results, with the formula being perhaps the most remarkable identity in analysis: the value of a holomorphic function at any interior point is completely determined by its values on any surrounding contour.

```
COMPLEX INTEGRATION — CONCEPTUAL FLOW
═══════════════════════════════════════════════════════════════════════════════

  CONTOUR INTEGRAL:  ∮_C f(z) dz  where C is a curve, f holomorphic on/inside C

  ┌─────────────────────────────────────────────────────────────────────┐
  │  CAUCHY'S THEOREM (Green's theorem + CR)                            │
  │                                                                     │
  │  f holomorphic on simply connected domain Ω, C closed curve in Ω   │
  │                                                                     │
  │  ⟹   ∮_C f(z) dz = 0                                              │
  │                                                                     │
  │  Consequence: path integrals ∫_γ f dz are PATH INDEPENDENT          │
  │  (depend only on endpoints, not on the specific path)               │
  └─────────────────────────────────────────────────────────────────────┘
                              │
                              ▼
  ┌─────────────────────────────────────────────────────────────────────┐
  │  CAUCHY INTEGRAL FORMULA                                            │
  │                                                                     │
  │  f holomorphic on/inside simple closed curve C                      │
  │  z₀ in the interior of C                                            │
  │                                                                     │
  │  f(z₀) = (1/2πi) ∮_C f(z)/(z − z₀) dz                            │
  │                                                                     │
  │  For derivatives:                                                   │
  │  f^(n)(z₀) = (n!/2πi) ∮_C f(z)/(z − z₀)^{n+1} dz                │
  └─────────────────────────────────────────────────────────────────────┘
                              │
                              ▼
  ┌─────────────────────────────────────────────────────────────────────┐
  │  RESIDUE THEOREM (see 03-RESIDUES-POLES.md)                         │
  │  If f has isolated singularities inside C:                          │
  │  ∮_C f dz = 2πi × Σ Res(f, aₖ)                                    │
  └─────────────────────────────────────────────────────────────────────┘
```

---

## Contour Integrals — Definition

A **contour** (path) γ: [a,b] → ℂ is a piecewise-smooth curve. The contour integral is:

    ∫_γ f(z) dz = ∫_a^b f(γ(t)) γ'(t) dt

This is a line integral in the complex plane, computable by substituting z = γ(t), dz = γ'(t)dt.

**Key estimate (ML inequality)**:

    |∫_γ f(z) dz| ≤ max_{z∈γ} |f(z)| · L(γ)

where L(γ) = ∫_a^b |γ'(t)| dt is the arc length of γ. Used constantly to show integrals vanish as contours shrink or grow.

---

## The Key Integral That Drives Everything

    ∮_{|z|=r} z^n dz = ?   (counterclockwise circle of radius r)

Parametrize: z = re^{iθ}, dz = ire^{iθ}dθ, θ: 0 → 2π:

    ∮ z^n dz = ir^{n+1} ∫_0^{2π} e^{i(n+1)θ} dθ

    = ir^{n+1} · { 0      if n+1 ≠ 0  (orthogonality of e^{imθ})
                 { 2π     if n+1 = 0  (i.e., n = −1)

```
∮_{|z|=r} z^n dz = { 2πi   if n = −1
                    { 0      if n ≠ −1, n ∈ ℤ
```

This is the fundamental coefficient-selector: 1/z is the only power of z with nonzero integral around a circle. It drives the entire theory of residues.

---

## Cauchy's Theorem — Proof via Green's Theorem

Write f = u + iv, z = x + iy, dz = dx + i dy:

    ∮_C f dz = ∮_C (u + iv)(dx + i dy)
             = ∮_C (u dx − v dy) + i ∮_C (v dx + u dy)

Apply Green's theorem (∮_C P dx + Q dy = ∬_D (∂Q/∂x − ∂P/∂y) dA):

    Real part:  ∬_D (∂(−v)/∂x − ∂u/∂y) dA = ∬_D (−∂v/∂x − ∂u/∂y) dA
    Imag part:  ∬_D (∂u/∂x − ∂v/∂y) dA

Using Cauchy-Riemann (∂u/∂x = ∂v/∂y, ∂u/∂y = −∂v/∂x):

    Real part = ∬ (−(−∂u/∂y) − ∂u/∂y) dA = 0
    Imag part = ∬ (∂v/∂y − ∂v/∂y) dA = 0

So ∮_C f dz = 0 whenever f is holomorphic inside and on C. □

This is Cauchy-Riemann meeting Green's theorem. The CR equations are precisely the condition that makes both surface integrals vanish.

---

## Winding Numbers

The **winding number** of a closed curve γ around a point a not on γ:

    n(γ, a) = (1/2πi) ∮_γ dz/(z − a)

Counts how many times γ winds around a counterclockwise (signed integer).

```
WINDING NUMBER EXAMPLES

  Simple closed CCW:   n = +1 for interior points,  n = 0 for exterior
  Simple closed CW:    n = −1 for interior points,  n = 0 for exterior
  Double loop CCW:     n = +2 for points inside both loops
  Figure-8:            n = +1 or −1 depending on which loop, 0 outside
```

**Jordan Curve Theorem**: A simple closed curve divides ℂ into exactly two connected components: bounded interior (|n| = 1) and unbounded exterior (n = 0).

---

## Cauchy's Theorem — General Formulation

**Simply connected version**: If Ω is simply connected and f is holomorphic on Ω, then ∮_C f dz = 0 for every closed curve C in Ω.

**Homology version**: For a cycle γ in a domain Ω,
    ∮_γ f dz = 0 for all f holomorphic on Ω
    ⟺  n(γ, a) = 0 for all a ∉ Ω   (γ doesn't wind around holes)

**Key consequence**: Holomorphic functions on simply connected domains have antiderivatives. If ∮_C f dz = 0 for all closed C, then F(z) = ∫_{z₀}^{z} f dz is well-defined (path-independent) and F' = f.

---

## Cauchy Integral Formula — Proof

For f holomorphic on/inside simple closed CCW curve C, z₀ in the interior:

The integrand f(z)/(z − z₀) has a singularity at z₀. Strategy: shrink the contour around z₀.

By deforming C to a small circle Cₑ of radius ε around z₀ (valid since f(z)/(z−z₀) is holomorphic in the annulus between C and Cₑ):

    ∮_C f(z)/(z − z₀) dz = ∮_{Cₑ} f(z)/(z − z₀) dz

On Cₑ: z = z₀ + εe^{iθ}. Write f(z) = f(z₀) + (f(z) − f(z₀)):

    ∮_{Cₑ} f(z)/(z − z₀) dz = f(z₀) ∮_{Cₑ} dz/(z − z₀) + ∮_{Cₑ} [f(z)−f(z₀)]/(z−z₀) dz
                              = f(z₀) · 2πi + ∮_{Cₑ} [f(z)−f(z₀)]/(z−z₀) dz

For the remaining integral, by ML inequality with |f(z)−f(z₀)| ≤ δ(ε) → 0 by continuity:

    |∮_{Cₑ} [f(z)−f(z₀)]/(z−z₀) dz| ≤ (δ(ε)/ε) · 2πε = 2π δ(ε) → 0

Therefore:

    ∮_C f(z)/(z − z₀) dz = 2πi · f(z₀)

    ⟹  f(z₀) = (1/2πi) ∮_C f(z)/(z − z₀) dz  □

**Meaning**: The value of f at any interior point is a complex-weighted average of its boundary values. This is why holomorphic functions are "rigid" — they cannot be wiggled at an interior point without changing their boundary values.

---

## Derivative Formulas

Differentiating the Cauchy integral formula n times under the integral sign (justified by uniform convergence):

    f^(n)(z₀) = (n!/2πi) ∮_C f(z)/(z − z₀)^{n+1} dz

**Morera's Theorem** (converse): If f is continuous on Ω and ∮_T f dz = 0 for every triangle T ⊂ Ω, then f is holomorphic on Ω. Proves holomorphicity when direct differentiation is hard.

---

## Cauchy Inequality and Liouville's Theorem

From the derivative formula, C = {|z − z₀| = r}:

    |f^(n)(z₀)| ≤ (n! / rⁿ) · max_{|z−z₀|=r} |f(z)|     (Cauchy's inequality)

**Liouville's Theorem**: If f is entire (holomorphic on all ℂ) and |f(z)| ≤ M for all z, then f is constant.

*Proof*: Apply Cauchy's inequality for n=1: |f'(z₀)| ≤ M/r for all r > 0. Let r → ∞: f'(z₀) = 0 for all z₀. So f' ≡ 0, f constant. □

**Fundamental Theorem of Algebra**: Every non-constant polynomial p(z) has a root in ℂ.

*Proof via Liouville*: If p had no roots, 1/p(z) would be entire and bounded (since |p(z)| → ∞ as |z| → ∞). Liouville: 1/p constant, so p constant — contradiction. □

---

**Cohomological reading (MIT topology bridge)**: The homology version of Cauchy's theorem is a statement about de Rham cohomology. The form ω = f(z)dz is closed (dω = 0, by holomorphicity). Cauchy says: ω is exact (∮_γ ω = 0 for all cycles γ) iff γ doesn't wind around any hole. The obstruction lives in H¹(Ω, ℤ): the winding number n(γ, a) is the pairing of the 1-cycle γ with the cohomology class [dz/(z−a)] ∈ H¹_dR(Ω). The multiply connected case below is precisely the case where H¹(Ω) ≠ 0.

---

## Simply Connected vs Multiply Connected

```
SIMPLY CONNECTED (no holes)          MULTIPLY CONNECTED (has holes)
┌────────────────────┐                ┌────────────────────┐
│                    │                │   ┌──┐      ┌──┐  │
│   any closed curve │                │   │h₁│      │h₂│  │
│   bounds a disk    │                │   └──┘      └──┘  │
│   inside the domain│                │  holes = topological │
│                    │                │  obstacles to shrinking│
└────────────────────┘                └────────────────────┘
  ∮_C f dz = 0 always                ∮_C f dz depends on which
  for holomorphic f                   holes C encircles
                                      → need residue theorem
```

For multiply connected domains with holes at a₁, ..., aₖ:

    ∮_C f dz = 2πi Σⱼ n(C, aⱼ) Res(f, aⱼ)

(sum over all singularities, weighted by winding numbers)

---

## Contour Deformation

A key technique: deform the contour without changing the integral, as long as f is holomorphic in the region between old and new contours.

```
ORIGINAL CONTOUR C₁    →    DEFORMED CONTOUR C₂

  ┌──────────┐                    ┌──┐
  │    D     │     f holomorphic  │  │
  │  no sgts │  =============>   │  │
  │          │    in between      └──┘
  └──────────┘
  ∫_{C₁} = ∫_{C₂}                smaller but same integral

If you deform ACROSS a singularity at a:
  The integral changes by ±2πi · Res(f, a)
```

This is the operational principle behind most contour integral calculations: replace a complicated contour with a simpler one, picking up residue contributions whenever you pass through a singularity.

---

## Evaluation Techniques

### Closing in the Upper Half-Plane

To evaluate ∫_{-∞}^{∞} f(x) dx:

1. Consider ∮_C f(z) dz over C = real axis + large semicircle in upper half-plane
2. Show semicircle contribution vanishes as R → ∞ (Jordan's lemma for oscillatory integrands)
3. Result = 2πi × (sum of residues in upper half-plane)

```
     Im
      │         large semicircle
      │     ╭─────────────────╮
      │   ╭╯                   ╰╮
      │  ╭╯     × ×             ╰╮   ← residues here contribute
      │──┼───────────────────────┼──── Re
           ─R                   R
           └─────────────────────┘
                real axis path
```

**Jordan's Lemma**: For f(z)e^{iaz} with a > 0, if |f(z)| → 0 uniformly for Im(z) ≥ 0 as |z| → ∞, then the integral over the large semicircle vanishes.

---

## Decision Cheat Sheet

| Situation | Approach |
|-----------|----------|
| ∮_C f dz, f holomorphic inside C | = 0 (Cauchy) |
| ∮_C f(z)/(z−z₀) dz, z₀ inside, f holomorphic | = 2πi f(z₀) |
| ∮_C f(z)/(z−z₀)^{n+1} dz | = 2πi f^(n)(z₀)/n! |
| Show integral → 0 | ML inequality: bound max|f| × length |
| f entire and bounded | Constant (Liouville) |
| Prove f holomorphic (given continuity) | Morera: show ∮_T f = 0 for triangles |
| Real integral ∫_{-∞}^{∞} | Close contour in ℂ; residue theorem |
| Deform contour past singularity | Pick up ±2πi × residue |

---

## Common Confusion Points

**Cauchy's theorem requires simply connected domain**: ∮ dz/z = 2πi around the unit circle because 0 is inside and 1/z has a singularity there. The theorem requires no singularities inside — or working in a simply connected domain that avoids the singularity.

**Orientation always counterclockwise for standard formulas**: Clockwise orientation gives a sign flip. The Cauchy integral formula assumes C is traversed counterclockwise (the positive orientation — region to the left).

**Green's theorem proof uses continuity of partials**: Goursat's original proof avoids this, showing that just the *existence* of f'(z) (without assuming its continuity) is sufficient for ∮ f dz = 0 over triangles.

**Contour deformation only works in holomorphic regions**: You cannot deform across a singularity without picking up a residue. The principle is: the integral changes by 2πi × (sum of residues of singularities crossed, with winding number signs).

**The ML inequality gives a bound, not the value**: ML says |∫ f dz| ≤ M·L. It is used to show integrals over shrinking circles or growing arcs tend to zero, not to compute values. To get exact values, use Cauchy's formula or residues.
