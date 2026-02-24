# Z-Transform — A Layered Guide

## The Big Picture

The Z-transform is to discrete-time systems what the Laplace transform is to continuous-time.
It converts difference equations into polynomial algebra, and maps system behavior onto the complex plane.

```
TRANSFORM CORRESPONDENCE

Continuous-Time                    Discrete-Time
─────────────────────────────────────────────────────────────────

Signal:   x(t)                     x[n]
Transform: X(s) = ∫x(t)e^{-st}dt  X(z) = Σ x[n]z^{-n}
Variable:  s ∈ ℂ                   z ∈ ℂ
Plane:     s-plane                 z-plane

Stability:  poles in left half      poles inside unit circle
           Re(s) < 0               |z| < 1

Freq resp: s = jω (imaginary axis) z = e^{jω} (unit circle)
           X(jω) = CT Fourier       X(e^{jω}) = DTFT

Mapping:   s → z via:  z = e^{sTs} (relation: bilinear approx)
```

---

## Z-Transform Definition

```
             +∞
X(z) = Z{x[n]} = Σ  x[n] · z^{-n}
              n=-∞

where z ∈ ℂ (complex variable, think of z = r·e^{jω})

INVERSE Z-TRANSFORM:
x[n] = (1/2πj) ∮ X(z) · z^{n-1} dz
        (contour integral around ROC — rarely computed directly)

Practical inverse: partial fraction expansion + table lookup
```

**Common Z-transform pairs**:

| x[n] | X(z) | ROC |
|------|------|-----|
| δ[n] | 1 | All z |
| u[n] (unit step) | z/(z-1) = 1/(1-z⁻¹) | \|z\| > 1 |
| a^n u[n] | z/(z-a) = 1/(1-az⁻¹) | \|z\| > \|a\| |
| -a^n u[-n-1] | z/(z-a) | \|z\| < \|a\| |
| n·a^n u[n] | az⁻¹/(1-az⁻¹)² | \|z\| > \|a\| |
| cos(ω₀n)u[n] | z(z-cosω₀)/(z²-2z·cosω₀+1) | \|z\| > 1 |

---

## Region of Convergence (ROC)

The ROC is the set of z values for which the Z-transform sum converges.
Different signals with the same X(z) can have different ROCs — the ROC defines which signal.

```
ROC GEOMETRY IN Z-PLANE

Finite-length sequence:    ROC = entire z-plane (except possibly z=0 or z=∞)

Right-sided sequence:      ROC = |z| > rmax   (outside a circle)
x[n] = 0 for n < n₁

Left-sided sequence:       ROC = |z| < rmin   (inside a circle)
x[n] = 0 for n > n₂

Two-sided sequence:        ROC = rmin < |z| < rmax   (annular region)
(if ROC exists)

Im(z)
  │         ROC for causal (right-sided) signal:
  │         ╔════════════════
  │     ────╬─────────────── Im(z)
  │         ║                  │
  ├─────────╬──────────────── Re(z)
  │         ║    │ pole at z=a
  │         ╚════╪════
  │              └── ROC is |z| > |a|
```

**Key ROC rules**:
1. ROC is an annular region centered at origin
2. ROC contains no poles (by definition)
3. For causal (right-sided) sequences: ROC extends outward from outermost pole
4. For anti-causal (left-sided): ROC is interior region
5. For finite-length sequences: ROC = all z except possibly 0 or ∞

**DTFT exists** iff ROC includes the unit circle |z| = 1.

---

## Poles and Zeros

The transfer function of an LTI system is a rational function of z:

```
        B(z)   b₀ + b₁z⁻¹ + ... + b_M z⁻M
H(z) = ──── = ─────────────────────────────────
        A(z)   1 + a₁z⁻¹ + ... + a_N z⁻N

Equivalently in factored form:

        b₀ · z^{N-M} · (z-z₁)(z-z₂)...(z-z_M)
H(z) = ──────────────────────────────────────────
              (z-p₁)(z-p₂)...(z-p_N)

Zeros: roots of B(z) → at z₁, z₂, ..., z_M
Poles: roots of A(z) → at p₁, p₂, ..., p_N
```

**Pole-zero plot in z-plane**: Poles marked ×, zeros marked ○.
The frequency response H(e^{jω}) at each point on the unit circle is determined by:
- Distance from that point to each zero (multiply)
- Distance from that point to each pole (divide)

```
FREQUENCY RESPONSE FROM POLE-ZERO PLOT

At frequency ω = ω₀ (point on unit circle z = e^{jω₀}):

|H(e^{jω₀})| = b₀ · ∏|e^{jω₀} - zₖ| / ∏|e^{jω₀} - pₖ|
                       zeros                  poles

∠H(e^{jω₀}) = ∠b₀ + Σ∠(e^{jω₀}-zₖ) - Σ∠(e^{jω₀}-pₖ)

INTUITION:
• Pole near unit circle at angle θ → magnitude peak near ω = θ (resonance)
• Zero on unit circle at angle θ → magnitude = 0 at ω = θ (notch)
• Poles far inside circle → broad, weak influence on response
```

---

## Stability

**BIBO stability** (bounded input → bounded output):
An LTI system is stable iff all its poles are inside the unit circle: |pₖ| < 1 for all k.

```
STABILITY REGIONS IN Z-PLANE

Im(z)
  │         × (unstable pole, |z|>1)
  │       ╱
  │──────╱──────── unit circle
  │    ╱  ┌─────┐
  │──╱───|  ○ ×  |────── Re(z)
  │      └─────┘
  │   stable poles  ← |z| < 1
  │   (inside circle)

Marginally stable: poles ON unit circle → oscillates forever (not practical)
Unstable: any pole outside → grows without bound
```

**For FIR filters**: H(z) = B(z) (numerator only, poles only at z=0). Always stable.

**Determining stability**: Given IIR filter with denominator A(z), compute roots.
Alternatively, use Schur-Cohn criterion or check if all coefficients of a Jury table are positive.

---

## Relationship to Difference Equations

The Z-transform converts difference equations to algebraic equations:

```
DIFFERENCE EQUATION → Z-DOMAIN

Difference equation:
y[n] = b₀x[n] + b₁x[n-1] + ... + b_M x[n-M]
     - a₁y[n-1] - a₂y[n-2] - ... - a_N y[n-N]

Z-transform (using delay property: Z{x[n-k]} = z⁻k·X(z)):

Y(z) = (b₀ + b₁z⁻¹ + ... + b_M z⁻M)·X(z)
     - (a₁z⁻¹ + ... + a_N z⁻N)·Y(z)

Solving for H(z) = Y(z)/X(z):

         b₀ + b₁z⁻¹ + ... + b_M z⁻M
H(z) = ─────────────────────────────────
          1 + a₁z⁻¹ + ... + a_N z⁻N
```

**Round-trip workflow**:
1. Specify filter specs (passband, stopband)
2. Design H(z) using filter design tools
3. Factor → poles/zeros, verify stability
4. Convert back to difference equation for implementation
5. Implement as direct form II or biquad cascade

---

## Digital Biquad Implementation

The second-order section (biquad) is the universal building block:

```
BIQUAD TRANSFER FUNCTION AND IMPLEMENTATION

H(z) = (b₀ + b₁z⁻¹ + b₂z⁻²) / (1 + a₁z⁻¹ + a₂z⁻²)

Direct Form II (transposed):

x[n] ──────────────────────────────────► + ──► y[n]
         │                              ▲  ×b₀
         │                              │
         ▼                              │
       ×(-a₁) ──────► [z⁻¹] ──────► + ──► ×b₁
         │                ▲             │
         ▼                │             │
       ×(-a₂)    [z⁻¹] ──┘        ×b₂──┘

State variables w[n]:
w[n] = x[n] - a₁·w[n-1] - a₂·w[n-2]
y[n] = b₀·w[n] + b₁·w[n-1] + b₂·w[n-2]

Implementation (C-like):
float biquad(float x, float* w) {
    float y = b0*x + b1*w[0] + b2*w[1] - a1*w[0] - a2*w[1];
    // Wait, actually Direct Form II transposed:
    float y = b0*x + w[0];
    w[0] = b1*x - a1*y + w[1];
    w[1] = b2*x - a2*y;
    return y;
}
// Two state variables, no temporary copies, numerically best
```

---

## Z-Transform Properties Summary

| Property | Time domain | Z-domain |
|----------|-------------|----------|
| Linearity | a·x₁[n] + b·x₂[n] | a·X₁(z) + b·X₂(z) |
| Time shift | x[n-k] | z⁻k · X(z) |
| Multiply by n | n·x[n] | -z · d/dz X(z) |
| Multiply by aⁿ | aⁿ · x[n] | X(z/a) |
| Convolution | x₁[n] ★ x₂[n] | X₁(z) · X₂(z) |
| Correlation | Rxy[n] | X(z⁻¹) · Y(z) |
| Initial value | x[0] | lim_{z→∞} X(z) |
| Final value (if stable) | lim_{n→∞} x[n] | lim_{z→1} (z-1)X(z) |

---

## Decision Cheat Sheet

| Problem | Z-transform approach |
|---------|---------------------|
| Analyze stability of a difference equation | Compute H(z), find poles, check |z|<1 |
| Find frequency response | Evaluate H(z) on unit circle, z = e^{jω} |
| Design a notch filter | Place zero ON unit circle at notch frequency |
| High-Q resonator | Pole near unit circle at resonant frequency |
| Check if filter matches difference equation | Z-transform the equation → H(z) |
| Implement IIR filter | Factor into biquad cascade |

---

## Common Confusion Points

**ROC must be specified for uniqueness**: Two different time-domain signals can have the same
rational X(z) but different ROCs. The ROC specifies whether the sequence is causal, anti-causal,
or two-sided. For digital filter design, we always assume causal systems (ROC includes |z|>rmax).

**Unit circle vs imaginary axis**: The DTFT is the Z-transform evaluated on the unit circle
(z = e^{jω}). The CT Fourier transform is the Laplace transform on the imaginary axis (s = jω).
This is the fundamental sampled ↔ continuous correspondence.

**Poles on unit circle**: A pole exactly on the unit circle gives a marginally stable system —
the impulse response oscillates at constant amplitude forever. In practice, poles must be
slightly inside the circle due to coefficient quantization.

**Relationship to Laplace**: z = e^{sTs}. This means s = σ+jΩ maps to z with magnitude e^{σTs}.
Stable region (σ<0) maps to |z| < 1. The mapping wraps: s = jΩ maps to z = e^{jΩTs}, which repeats
with period 2π/Ts — that's why all DT spectra are 2π-periodic.
