# 02 — Mechanics of Materials

## Stress, Strain, Bending, Shear, Torsion, Deflection

```
STRESS ─► STRAIN ─► DEFORMATION

  σ = F/A     ε = σ/E = δ/L    δ = FL/(AE)
  τ = V/A     γ = τ/G          φ = TL/(GJ)
                                 y(x) from EI y'' = M
```

Mechanics of materials is the link between structural analysis (internal forces) and
structural design (is the material adequate?). Given N, V, M, T — compute stresses
and deformations, check against material limits.

---

## Stress and Strain

### Basic Definitions

```
Normal stress:   σ = F_normal / A    [Pa = N/m²]
Shear stress:    τ = F_shear  / A    [Pa]
Bearing stress:  σ_b = F / A_bearing  (projected area)
```

**Engineering strain (small deformations):**
```
Normal: ε = δ/L₀ = (L − L₀)/L₀   (dimensionless)
Shear:  γ = angular change [rad]   (shear strain)

Volumetric: e = ΔV/V = ε_x + ε_y + ε_z
```

### Material Constants

```
Young's modulus:  E = σ/ε  [Pa]        (resistance to normal deformation)
Shear modulus:    G = τ/γ  [Pa]        (resistance to shear)
Bulk modulus:     K = −p/e  [Pa]       (resistance to volume change)
Poisson's ratio:  ν = −ε_lat/ε_axial   (lateral contraction per axial extension)

Relation: G = E / [2(1+ν)]     K = E / [3(1−2ν)]
Typical for steel: E = 200 GPa, G = 77 GPa, ν = 0.30
Typical for Al:    E = 70 GPa,  G = 26 GPa, ν = 0.33
Concrete:          E = 30 GPa,  ν ≈ 0.2 (elastic range only)
```

### Generalized Hooke's Law (3D)

<!-- @editor[bridge/P2]: Generalized Hooke's Law appears as a set of equations without the connection to continuum mechanics (the constitutive relation σ = C:ε where C is the 4th-order elasticity tensor). For this learner, the insight is that the full 3D Hooke's law is an isotropic linear map from a symmetric 3×3 strain tensor to a symmetric 3×3 stress tensor — exactly the matrix equation it is. Isotropy reduces 81 coefficients to 2 (E and ν). This is the bridge from linear algebra to continuum mechanics. -->
```
ε_x = (σ_x − ν(σ_y + σ_z)) / E
ε_y = (σ_y − ν(σ_x + σ_z)) / E
ε_z = (σ_z − ν(σ_x + σ_y)) / E
γ_xy = τ_xy / G    (similarly for xz, yz)
```

---

## Axial Loading

**Deformation:**
```
δ = PL / (AE)   (single member, constant P, A, E)

Variable cross-section or load:
  δ = ∫₀^L P(x) dx / [A(x) E]

Multiple members in series:
  δ_total = Σ P_i L_i / (A_i E_i)
```

**Statically indeterminate axial members:**
```
1. Equilibrium: ΣF = 0 → one equation, two unknowns
2. Compatibility: δ_total = prescribed (e.g., wall gap) → second equation
3. Force-deformation: δ_i = P_i L_i/(A_i E_i)

Example: Bar with fixed ends, concentrated load P at midpoint
  R_A + R_B = P    (equilibrium)
  δ_A = δ_B       (compatibility: both ends fixed, midpoint moves same amount)
```

**Thermal stresses:**
```
Free expansion: δ_T = α ΔT L
Constrained: σ_thermal = −E α ΔT   (compressive if heating, constrained)
Combined: σ = E(ε − α ΔT) = E(δ/L − αΔT)
```

---

## Torsion

### Circular Shafts

```
Shear stress:     τ = Tc/J  (max at outer surface, c = radius)
                  τ(r) = Tr/J  (varies linearly with radial distance)

Angle of twist:   φ = TL/(GJ)  [radians]

Polar moment:     Solid circle:  J = πd⁴/32 = πr⁴/2
                  Hollow circle: J = π(d_o⁴ − d_i⁴)/32
```

**Power transmission:**
```
P = Tω = T × 2πN/60    [Watts, T in N·m, N in rpm]
→ T = P/(2πN/60) = 9549 P/N   [Torque in N·m]
```

**Statically indeterminate torsion:** Same approach as axial — equilibrium + compatibility.

### Non-Circular Sections (Prandtl Membrane Analogy)

**Thin-walled closed tubes (Bredt's formula):**
```
Shear flow: q = T/(2A_m)   (constant around perimeter, A_m = enclosed area)
Shear stress: τ = q/t      (varies with wall thickness t)
Angle of twist: φ = TL/(4A_m²) × ∮(ds/t)   (line integral around perimeter)

Circular tube at T/t thin: most efficient torsion cross-section
```

**Open thin-walled sections (channel, angle, I):** Extremely poor in torsion.
```
J_open ≈ Σ b_i t_i³ / 3   (much less than closed tube of same material)
Warping torsion becomes important — flanges carry torsion by bending
```

---

## Beam Bending

### Flexure Formula (Euler-Bernoulli)

```
Assumptions:
  - Plane sections remain plane and perpendicular to neutral axis (Kirchhoff hypothesis)
  - Neutral axis: zero normal stress (for homogeneous, symmetric section: passes through centroid)
  - Small deflections, elastic material

Normal stress due to bending:
  σ = −My/I

  M = bending moment [N·m]
  y = distance from neutral axis [m]  (positive upward)
  I = area moment of inertia about neutral axis [m⁴]

Maximum stress (at extreme fiber ±c):
  σ_max = Mc/I = M/S    where S = I/c = section modulus [m³]
```

**Sign convention:**
- M positive → sagging (concave up) → bottom fiber tension (σ > 0), top compression (σ < 0)
- M negative → hogging → bottom fiber compression, top tension

### Shear Stress in Beams

```
Horizontal (longitudinal) shear stress:
  τ = VQ/(Ib)

  V = shear force at cross-section
  Q = first moment of area above (or below) the horizontal cut:
      Q = ȳ' A'  (centroidal distance of area A' above cut × area A')
  I = moment of inertia of entire cross-section
  b = width of cross-section at the cut

Maximum shear: at neutral axis (Q is maximum there)
Zero at top and bottom surfaces (free surfaces, no horizontal shear)

For rectangular cross-section:
  τ_max = 1.5 V/A   (at mid-height)

For wide flange (I-beam):
  ~90% of shear carried by web; τ_avg,web ≈ V/A_web
  Flanges carry little shear but provide most of I (bending resistance)
```

**Shear flow q = VQ/I:** Useful for built-up sections (fastener spacing).
Fastener shear: F/spacing = q → spacing = F_allowable_fastener / q

---

## Beam Deflection

**Governing differential equation:**
```
EI d²y/dx² = M(x)    (Euler-Bernoulli, small deflection, elastic)

Integrate twice:
  EI dy/dx = ∫M dx + C₁     (slope)
  EI y = ∬M dx dx + C₁x + C₂  (deflection)

Apply boundary conditions to find C₁, C₂
```

### Macaulay Bracket Notation

For discontinuous loads, use brackets ⟨x−a⟩ⁿ:
- If x < a: ⟨x−a⟩ⁿ = 0
- If x ≥ a: ⟨x−a⟩ⁿ = (x−a)ⁿ

```
Example: Point load P at x=a:
  EI y'' = R_A x − P⟨x−a⟩

Integrate: EI y' = R_A x²/2 − P⟨x−a⟩²/2 + C₁
           EI y  = R_A x³/6 − P⟨x−a⟩³/6 + C₁x + C₂

Apply BCs: y(0)=0 and y(L)=0 for simply supported beam
```

### Superposition (Standard Cases)

| Loading | δ_max | Location | θ_max |
|---------|-------|---------|-------|
| Simply supported, midpoint load P | PL³/48EI | midspan | PL²/16EI |
| Simply supported, UDL w | 5wL⁴/384EI | midspan | wL³/24EI |
| Cantilever, end load P | PL³/3EI | free end | PL²/2EI |
| Cantilever, UDL w | wL⁴/8EI | free end | wL³/6EI |
| Simply supported, moment M at end | ML²/9√3 EI | x=L/√3 | ML/6EI |

Superposition: δ_total = Σδ_i for each load acting alone (valid only in linear elastic range).

---

## Column Buckling

<!-- @editor[bridge/P2]: Column buckling (P_cr = π²EI/L²) is presented without connecting to the eigenvalue problem it is: the buckling mode is the eigenmode of the beam differential operator, and P_cr is the smallest eigenvalue. This learner would immediately recognize the solution — deflection shape is the first eigenfunction of EId²y/dx² = -Py, giving sinusoidal modes with eigenvalue P_cr = n²π²EI/L². The connection to the eigenvalue decomposition of the stiffness matrix in FEM (buckling = solve [K]φ = λ[Kg]φ) is the modern form of the same idea. -->
**Euler critical load (long column, pin-pin):**
```
P_cr = π²EI / L_e²

L_e = effective length = K × L
K = effective length factor:
  Pin-pin:       K = 1.0  (theoretical + practical)
  Pin-fixed:     K = 0.7  (theoretical 0.699)
  Fixed-fixed:   K = 0.5  (theoretical, rarely achieved in practice)
  Fixed-free:    K = 2.0  (flagpole)
```

**Slenderness ratio:** r = √(I/A) = radius of gyration
```
λ = KL/r   (slenderness ratio)

Long columns (large λ): Euler buckling governs (elastic)
Short columns (small λ): Yielding governs (material failure, not buckling)
Intermediate: Johnson parabola (inelastic buckling)

Transition at: λ_c = π√(2E/S_y) → λ < λ_c: short column
```

---

## Inelastic Bending

### Plastic Hinge Formation

```
Elastic range: σ_max ≤ S_y → full Euler-Bernoulli applies
First yield: M_y = S_y × I/c = S_y × S   (section modulus S = I/c)
Fully plastic: M_p = S_y × Z             (plastic section modulus Z = Q_upper + Q_lower)

Shape factor: f = M_p/M_y = Z/S   (typical values: rectangle=1.5, W-shape≈1.12, circle=1.7)
```

**Plastic hinge:** A cross-section at which M = M_p (fully plastified, acts like a pin in further loading).

**Collapse mechanism:** Sufficient plastic hinges form to convert structure into mechanism.
For a simply supported beam: 1 plastic hinge (at midspan) → collapse.
For a propped cantilever: 2 plastic hinges → collapse.

---

## Combined Loading

When multiple internal forces act simultaneously:

```
Superposition of stresses (linear elastic):
  Axial + bending: σ = N/A + My/I   (add algebraically, check sign)
  Bending + torsion: requires principal stress analysis
  Combined normal + shear: apply von Mises or Tresca

Example — shaft with torque T and bending M:
  σ = My/I (bending, max ±Mc/I)
  τ = Tr/J (torsion)
  Principal stresses: σ₁,₂ = σ/2 ± √((σ/2)² + τ²)
  von Mises: σ_vm = √(σ² + 3τ²)   (for biaxial stress state with one normal + one shear)
```

---

## Stress Transformation and Mohr's Circle

```
Stress transformation equations (plane stress):
  σ_x' = (σ_x+σ_y)/2 + (σ_x−σ_y)/2 cos2θ + τ_xy sin2θ
  τ_x'y' = −(σ_x−σ_y)/2 sin2θ + τ_xy cos2θ

Principal stresses (θ_p where dσ/dθ = 0):
  σ₁,₂ = (σ_x+σ_y)/2 ± √[((σ_x−σ_y)/2)² + τ_xy²]
  tan(2θ_p) = 2τ_xy/(σ_x−σ_y)

Maximum shear stress:
  τ_max = √[((σ_x−σ_y)/2)² + τ_xy²]
  occurs at θ = θ_p ± 45°
```

**Mohr's circle construction:**
1. Plot point A = (σ_x, τ_xy) and point B = (σ_y, −τ_xy)
2. Center C = ((σ_x+σ_y)/2, 0)
3. Draw circle through A and B with center C
4. Intersections with σ-axis = principal stresses σ₁, σ₂
5. Top/bottom of circle = ±τ_max

---

## Thick-Walled Cylinders (Lamé Equations)

For pressure vessels where wall thickness ≥ 1/10 of inner radius:
```
Hoop stress:   σ_θ = (p_i r_i² − p_o r_o² + (p_i − p_o)r_i²r_o²/r²) / (r_o² − r_i²)
Radial stress: σ_r = (p_i r_i² − p_o r_o² − (p_i − p_o)r_i²r_o²/r²) / (r_o² − r_i²)

Internal pressure only (p_o = 0):
  σ_θ = p_i r_i²/(r_o²−r_i²) × (1 + r_o²/r²)   → max at r = r_i
  σ_r = p_i r_i²/(r_o²−r_i²) × (1 − r_o²/r²)   → compressive through wall

Thin-walled approximation (r_i/t > 10):
  σ_θ ≈ pr/t    (hoop)
  σ_L = pr/(2t) (longitudinal)
```

---

## Common Confusion Points

**Section modulus S vs plastic section modulus Z:** S = I/c (elastic, first yield). Z = Σ|ȳ_i A_i| (plastic, fully yielded). Z > S always; shape factor Z/S = 1.0–1.7.

**Neutral axis shifts in plastic bending:** In elastic bending, NA passes through centroid. In plastic bending with a non-symmetric section, the plastic NA divides the section into equal areas (not equal first moments) — it shifts toward the smaller area side.

**Shear stress in beams is NOT V/A:** τ = VQ/(Ib) is the correct formula. V/A gives an average; actual distribution is parabolic for rectangles, peaks at the NA. The Q factor accounts for the geometry.

**Euler buckling = elastic buckling only:** P_cr = π²EI/L_e² assumes no yielding before buckling. Check: critical stress σ_cr = P_cr/A must be ≤ 0.5 S_y for Euler to be valid. Otherwise use Johnson or tangent modulus.

**Superposition of stresses:** Only valid in linear elastic range. Never superpose after nonlinear (post-yield) behavior or after large deflections that change geometry.

---

## Decision Cheat Sheet

| Situation | Formula | Notes |
|-----------|---------|-------|
| Normal stress in member | σ = N/A | Axial loading |
| Bending stress | σ = My/I | Max at extreme fiber |
| Shear stress in beam | τ = VQ/(Ib) | Max at neutral axis |
| Torsional shear (circular) | τ = Tc/J | Max at surface |
| Deflection (standard case) | Superposition tables | Check linearity |
| Deflection (general) | EIy'' = M(x), integrate twice | Apply BCs |
| Column buckling check | P_cr = π²EI/(KL)² | Check slenderness first |
| Combined loading | σ_vm = √(σ²+3τ²) | Plane stress, von Mises |
| Thick-walled cylinder | Lamé equations | r_i/t < 10 |
| First yield load | M_y = S × S_y | S = section modulus |
| Collapse load | M_p = Z × S_y | Z = plastic section modulus |
