# Classical Laminate Theory (CLT)

## The Big Picture

```
+------------------------------------------------------------------+
|              CLASSICAL LAMINATE THEORY (CLT)                    |
|                                                                  |
|   GOAL: Predict laminate behavior from ply properties            |
|   via linear elastic mechanics                                   |
|                                                                  |
|   INPUT:  Ply properties (E1, E2, G12, ν12, ply thickness)      |
|           Stacking sequence [0/45/-45/90]s                       |
|                                                                  |
|   OUTPUT: [A][B][D] matrices → stiffness                        |
|           Strains/stresses in each ply under loads              |
|           Failure prediction when combined with criteria         |
|                                                                  |
|   ASSUMPTIONS:                                                   |
|   1. Kirchhoff-Love plate theory (thin plate, plane stress)      |
|   2. Linear elastic material behavior                            |
|   3. Perfect bonding between plies (no delamination)            |
|   4. Plane stress through thickness (σ3 = τ23 = τ13 = 0)       |
+------------------------------------------------------------------+
```

CLT is to composite design what beam bending theory is to structural steel —
the foundational analytical model that all composite analysis builds on.

---

## Ply Stress-Strain in Material Coordinates

### The Reduced Stiffness Matrix [Q]

For a ply in its material coordinate system (1 = fiber direction, 2 = transverse):

```
   PLANE STRESS CONSTITUTIVE LAW (material axes):
   ─────────────────────────────────────────────────
   {σ1}   [Q11  Q12   0 ] {ε1}
   {σ2} = [Q12  Q22   0 ] {ε2}
   {τ12}  [0    0    Q66] {γ12}

   Where:
   Q11 = E1 / (1 - ν12·ν21)    ≈ E1 for high E1/E2 ratio
   Q22 = E2 / (1 - ν12·ν21)
   Q12 = ν12·E2 / (1 - ν12·ν21)
   Q66 = G12
   ν21 = ν12 · E2/E1  (reciprocal relation)

   For CF/epoxy IM7/977: E1=165, E2=9.5, G12=5.7, ν12=0.34 [GPa]
   Q11 = 165/(1-0.34×0.022) = 165.77 GPa
   Q22 = 9.5/0.992 = 9.58 GPa
   Q12 = 0.34×9.5/0.992 = 3.26 GPa
   Q66 = 5.7 GPa
```

### Coordinate Transformation

When a ply is oriented at angle θ to the laminate x-axis:

```
   TRANSFORMATION (ply at θ degrees to x-axis):
   ──────────────────────────────────────────────
   {σx}     [T]^{-1} {σ1}
   {σy}   =          {σ2}    (and inverse for strains)
   {τxy}             {τ12}

   [T] = [c²     s²    2cs ]
         [s²     c²   -2cs ]
         [-cs   cs   c²-s² ]
   where c = cos(θ), s = sin(θ)

   TRANSFORMED REDUCED STIFFNESS [Q̄]:
   ─────────────────────────────────────
   {σx}     [Q̄11  Q̄12  Q̄16] {εx}
   {σy}   = [Q̄12  Q̄22  Q̄26] {εy}
   {τxy}    [Q̄16  Q̄26  Q̄66] {γxy}

   Key: Q̄16 and Q̄26 ≠ 0 for off-axis plies (bending-shear coupling)
   For θ = 0° or 90°: Q̄16 = Q̄26 = 0 (no coupling)
```

---

## The ABD Matrix

The core of CLT. Relates in-plane loads {N} and moments {M} to
midplane strains {ε⁰} and curvatures {κ}:

```
   {N}   [A  B] {ε⁰}
   {M} = [B  D] {κ}

   Written out:
   [Nx]   [A11 A12 A16 | B11 B12 B16] [ε⁰x]
   [Ny]   [A12 A22 A26 | B12 B22 B26] [ε⁰y]
   [Nxy]  [A16 A26 A66 | B16 B26 B66] [γ⁰xy]
   ─────  ─────────────────────────── ──────
   [Mx]   [B11 B12 B16 | D11 D12 D16] [κx]
   [My]   [B12 B22 B26 | D12 D22 D26] [κy]
   [Mxy]  [B16 B26 B66 | D16 D26 D66] [κxy]
```

### Computing A, B, D

```
   h = total laminate thickness
   hk = z-coordinate of top of ply k (measured from midplane)
   h_{k-1} = z-coordinate of bottom of ply k

   Aij = Σ [Q̄ij]k · (hk - h_{k-1})           [stiffness × thickness]
   Bij = ½ Σ [Q̄ij]k · (hk² - h_{k-1}²)       [stiffness × first moment]
   Dij = ⅓ Σ [Q̄ij]k · (hk³ - h_{k-1}³)       [stiffness × second moment]
```

Physical meaning:
- **[A]** = in-plane extensional stiffness (N/m)
- **[B]** = extension-bending coupling (N — moment from axial load)
- **[D]** = bending stiffness (N·m)

---

## Stacking Sequence Effects

### Symmetric Laminates: B = 0

If the laminate is symmetric about the midplane, [B] = 0.
This is critical for manufacturing: asymmetric laminates warp on cure
(differential thermal shrinkage, B coupling thermal load into curvature).

```
   SYMMETRIC NOTATION: [0/45/-45/90]s
   The 's' means reflect: [0/45/-45/90/90/-45/45/0]
   → 8 plies total
   → B = 0 → no extension-bending coupling
   → No curvature on cooling from cure temperature

   ASYMMETRIC EXAMPLE: [0/45/-45/90]
   4 plies, B ≠ 0
   Flat when hot, warped when cool
   Only use asymmetric if warped shape is desired (e.g., snap-through)
```

### Balanced Laminates: A16 = A26 = 0

For every +θ ply, a –θ ply exists at the same or mirrored position.
This eliminates in-plane shear-extension coupling:

```
   BALANCED: [0/+45/-45/90]s (balanced and symmetric)
   → A16 = A26 = 0 (no shear-extension coupling)
   → D16 ≠ 0 unless also [0/+45/-45/90/90/-45/+45/0] (mid-plane symmetry only)

   QUASI-ISOTROPIC: [0/+45/-45/90]s
   → A matrix is isotropic in-plane: A11 = A22, A16 = A26 = 0
   → But D matrix is NOT isotropic (bending stiffness varies with direction)
   → "Quasi-isotropic" means in-plane only
```

### Common Stacking Sequences

```
   [0]n     — Unidirectional, maximum E1, minimum E2
              All load must be in fiber direction
              UD test specimens only

   [0/90]s  — Cross-ply, balanced symmetric
              E = average of E1 and E2 in both directions
              Good for biaxial loading (tanks, pressure vessels)

   [0/+45/-45/90]s — Quasi-isotropic (QI)
              In-plane: same E in any direction = E_QI
              E_QI ≈ (E1 + E2 + 2·E1·ν21)/(2·(1-ν12·ν21)) ... (complex)
              Approximate: E_QI ≈ 3/8·E1 + 5/8·E2 (crude)
              For CF/epoxy: E_QI ≈ 50–55 GPa vs. E1 = 130–165 GPa
              Aviation preference: simple analysis, no directional optimization

   [0/±60]s — Quasi-isotropic 3-direction (triaxial braid equivalent)
              Three balanced directions at 60°

   [+45/-45]s — Pure shear panel, optimized for shear webs
               High G_xy, low E_x and E_y
```

---

## Ply Strains from Applied Loads

Invert the [ABD] relation to get compliance [a,b,d]:

```
   Compliance form:
   {ε⁰}   [a  b^T] {N}
   {κ}  = [b  d  ] {M}

   [a] = [A]^{-1} + [A]^{-1}[B][d][B][A]^{-1}
   [d] = ([D] - [B][A]^{-1}[B])^{-1}
   [b] = -[A]^{-1}[B][d]

   For symmetric laminates ([B]=0):
   {ε⁰} = [A]^{-1} · {N}
   {κ}  = [D]^{-1} · {M}
   Decoupled! — much simpler.
```

From midplane strains and curvatures, find ply strains at any z:

```
   {ε}(z) = {ε⁰} + z·{κ}

   Convert to material axes:
   {ε₁} = [T]·{εx}  (at z-position of ply centroid or top/bottom)

   Ply stresses in material axes:
   {σ₁} = [Q]·{ε₁}
```

---

## Thermal and Hygroscopic Effects

Composite laminates are strongly affected by temperature (cure residual stress)
and moisture (swelling).

### Thermal Residual Stress

```
   CURING AT 180°C, COOLING TO 25°C:
   ──────────────────────────────────
   ΔT = -155°C

   Each ply has CTE:
   α1 ≈ 0.1×10⁻⁶/°C (carbon fiber CTE in fiber direction — very small)
   α2 ≈ 28×10⁻⁶/°C  (transverse — epoxy dominates)

   In a [0/90]s laminate:
   0° plies want to shrink more in transverse direction
   90° plies constrain that shrinkage
   → Residual compressive stress in fiber direction of 0° plies
   → Residual tensile stress perpendicular to fibers in 0° plies

   Residual thermal stress can be significant fraction of failure stress
   → This is why cure simulation and residual stress analysis matters for
     thick sections and asymmetric laminates
```

### Hygroscopic Swelling

```
   MOISTURE CONCENTRATION: Mm (kg moisture / kg resin)
   Typical saturation: 2–5% (epoxy)

   Swelling coefficient:
   β1 = 0 (no fiber direction swelling — fiber restrains)
   β2 = 0.005–0.010 mm/mm per %MM (transverse swelling)

   Effect: moisture partially cancels thermal residual stress
   (thermal: shrinkage; moisture: expansion)
   Engineering use: wet/hot condition often near stress-free from these
                    competing effects

   IMPORTANT: moisture reduces Tg → reduces hot/wet allowables
```

---

## Failure Criteria

CLT provides stresses in each ply. Need criteria to determine when a ply fails.

### Maximum Stress Criterion (simplest)

```
   FAILURE in any mode if:
   σ1 ≥ X1T  (fiber tensile failure)
   σ1 ≤ -X1C (fiber compressive failure)
   σ2 ≥ X2T  (matrix tensile failure)
   σ2 ≤ -X2C (matrix compressive failure)
   |τ12| ≥ S12 (matrix shear failure)

   Simple but ignores interaction between stress components.
```

### Tsai-Wu Criterion (interaction)

```
   F1·σ1 + F2·σ2 + F11·σ1² + F22·σ2² + F66·τ12² + 2F12·σ1·σ2 = 1

   Failure index (FI) = left side; FI ≥ 1 → failure
   Reserve factor (RF) = 1/√FI (how far to scale loads for failure)

   Coefficients:
   F1  = 1/X1T - 1/X1C         F2  = 1/X2T - 1/X2C
   F11 = 1/(X1T·X1C)           F22 = 1/(X2T·X2C)
   F66 = 1/S12²                 F12 = interaction term (empirical, -½√(F11·F22))

   Tsai-Wu is a good default criterion for initial design in aerospace.
```

### Progressive Failure Analysis (PFA)

```
   FIRST PLY FAILURE (FPF): first ply to reach failure criterion
   PLY PROPERTY DEGRADATION: failed ply properties reduced
   CONTINUE ANALYSIS: redistribute loads, find next failure
   LAST PLY FAILURE (LPF): laminate ultimate load

   FPF ≠ structural failure: often matrix cracking (off-axis plies)
   Aerospace design: often designed to FPF with safety factors
   Marine/civil: may design to LPF with larger safety factors
```

---

## Effective Laminate Properties

For a general laminate analysis, effective engineering constants:

```
   Ex  = 1/(a11·h)          (in-plane modulus in x)
   Ey  = 1/(a22·h)
   Gxy = 1/(a66·h)
   νxy = -a12/a11

   For [0/+45/-45/90]s CF/epoxy IM7 (each ply 0.125 mm):
   Total thickness: 8 × 0.125 = 1.0 mm
   Ex ≈ Ey ≈ 55 GPa  (quasi-isotropic — equal in all directions)
   Gxy ≈ 21 GPa
   νxy ≈ 0.31

   Bending stiffness dominated by outer plies (× z³ in D):
   [0/+45/-45/90]s vs [90/+45/-45/0]s: same [A], different [D]
   Outer 0° plies → higher bending stiffness in fiber direction
   Design: put stiff plies on outside for bending-critical structures
```

---

## Decision Cheat Sheet

| Design need | Laminate approach |
|-------------|------------------|
| Maximize in-plane stiffness in one direction | High fraction of 0° plies |
| Isotropic in-plane behavior | Quasi-isotropic [0/±45/90]s |
| Avoid warpage on cure | Symmetric laminate about midplane |
| Avoid shear-extension coupling | Balanced (+θ for every –θ) |
| Maximum shear stiffness | ±45° dominant layup |
| Maximize bending stiffness | 0° plies on outer faces |
| Minimize thermal residual stress | Symmetric + balanced + low ΔT cure |

---

## Common Confusion Points

**CLT assumes thin plate, plane stress**: For thick laminates (t/width > 1/10)
or near free edges, through-thickness stresses (σ3, τ13, τ23) become important.
These are interlaminar stresses — not captured by CLT — and can initiate
delamination. 3D finite element analysis with solid elements needed.

**Quasi-isotropic is not isotropic**: QI means equal in-plane moduli (Aij
matrix isotropic). The bending stiffness Dij is still anisotropic. A QI
laminate will warp differently under bending loads depending on loading direction.

**The outer plies dominate bending stiffness**: D ~ z³. An outer ply at z = h/2
contributes (h/2)³ to D while a central ply at z ~ 0 contributes nearly nothing.
Sandwich structures exploit this: thin stiff facesheets far from neutral axis
dominate D with minimal weight penalty — the "I-beam" principle in composite form.
