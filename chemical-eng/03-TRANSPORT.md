# 03 — Transport Phenomena

## Momentum, Energy, and Mass Transfer (Bird-Stewart-Lightfoot Framework)

```
THE BSL UNIFICATION

Transport type     Flux equation              Transport coefficient
─────────────────────────────────────────────────────────────────────
Momentum         τ = −μ dv_x/dy              μ (dynamic viscosity)
(viscous flow)                                ν = μ/ρ (kinematic)

Heat             q = −k dT/dy                k (thermal conductivity)
(conduction)                                  α = k/(ρCp) (thermal diffusivity)

Mass             J_A = −D_AB dC_A/dy          D_AB (binary diffusivity)
(diffusion)

Same structure: flux = −(diffusivity) × d(concentration)/dy
```

Transport phenomena (BSL after Bird, Stewart & Lightfoot) unifies the three transport modes.
This reveals deep analogies that let you transfer correlations across domains.

---

## Molecular Transport (Constitutive Laws)

### Newton's Law of Viscosity
```
τ_yx = −μ (dv_x/dy)    [Pa = N/m²]

τ_yx = shear stress on a y-face in x-direction
dv_x/dy = velocity gradient (shear rate)
μ = dynamic viscosity [Pa·s]

For a Newtonian fluid: μ independent of shear rate
Non-Newtonian: power law fluid τ = m γ̇ⁿ  (n<1: shear-thinning, n>1: shear-thickening)
```

### Fourier's Law of Heat Conduction
```
q_y = −k (dT/dy)    [W/m²]

q_y = heat flux in y-direction
k = thermal conductivity [W/(m·K)]
```

### Fick's First Law of Diffusion
```
J_A = −D_AB (dC_A/dy)    [mol/(m²·s)]

J_A = molar flux of A relative to molar average velocity
D_AB = binary diffusivity of A in B [m²/s]
```

---

## Diffusivity Values Reference

### Gas-Phase Binary Diffusivities (at 25°C, 1 atm)

| Pair | D_AB [cm²/s] |
|------|-------------|
| O₂-Air | 0.208 |
| CO₂-Air | 0.164 |
| H₂O-Air | 0.256 |
| H₂-N₂ | 0.779 |
| NH₃-Air | 0.236 |

Correlation: D_AB ∝ T^1.5/p (Chapman-Enskog for low-density gases)

### Liquid-Phase Diffusivities (dilute solutions at 25°C)

| Solute in Solvent | D [cm²/s] |
|-------------------|----------|
| Small ions in water | ~10⁻⁵ |
| O₂ in water | 2.5×10⁻⁵ |
| Sucrose in water | 5.2×10⁻⁶ |
| Proteins in water | ~10⁻⁷ |

Wilke-Chang correlation: D ∝ T/(μ V_A^0.6)

---

## Shell Balance Method (Deriving Governing Equations from First Principles)

Procedure:
1. Choose coordinate system and shell geometry
2. Write steady-state balance: Rate in − Rate out + Generation = Accumulation (=0 for steady state)
3. Divide by shell volume, take limit as shell → 0 → differential equation
4. Integrate with boundary conditions

### Example: Laminar Flow in a Tube (Hagen-Poiseuille)

```
Shells: cylindrical annuli at radius r, thickness Δr, length L

Momentum balance (z-direction):
  (τ_rz × 2πr L)|_r − (τ_rz × 2πr L)|_{r+Δr} + (p₀ − p_L)(2πr Δr) = 0

Divide by 2π L Δr, take Δr → 0:
  d(r τ_rz)/dr = −(p_L − p₀)r/L  ≡  (P₀ − P_L)r/L

Integrate:  r τ_rz = (P₀−P_L)r²/(2L) + C₁
  BC: finite at r=0 → C₁ = 0

Substitute Newton's law τ_rz = −μ dv_z/dr:
  dv_z/dr = −(P₀−P_L)r/(2μL)

Integrate: v_z = (P₀−P_L)(R²−r²)/(4μL)   [parabolic profile!]

Max velocity (centerline): v_max = (P₀−P_L)R²/(4μL)
Average velocity: v_avg = v_max/2

Hagen-Poiseuille: Q = πR⁴(P₀−P_L)/(8μL)   ← Volume flow rate
```

---

## Convective Transport Correlations

### The BSL Dimensionless Analogy

```
Heat transfer:    Nu = f(Re, Pr)    Nu = hL/k
Mass transfer:    Sh = f(Re, Sc)    Sh = k_c L/D_AB

Same function! If you know Nu correlation, replace Pr with Sc:
  Dittus-Boelter (heat): Nu = 0.023 Re^0.8 Pr^0.33
  Analogous (mass):      Sh = 0.023 Re^0.8 Sc^0.33
```

### Chilton-Colburn Analogy (j-factor)

For turbulent flow in pipes and over flat plates:
```
j_H = j_D = f/2  (friction factor f/2 = Fanning friction factor)

j_H = (h/ρCp v) Pr^(2/3)  = St Pr^(2/3)    (heat)
j_D = (k_c/v) Sc^(2/3)    = St_mass Sc^(2/3)  (mass)

Implications:
  h/(k_c) = ρ Cp (Pr/Sc)^(2/3) = ρ Cp Le^(2/3)   (Le = α/D_AB)
  For Le = 1: h = k_c ρ Cp   (Lewis analogy for air-water systems)
```

---

## Mass Transfer

### Fick's Second Law (Unsteady Diffusion)

```
∂C_A/∂t = D_AB ∇² C_A   (no convection, no reaction)

1D:  ∂C_A/∂t = D_AB ∂²C_A/∂x²

Solutions analogous to transient heat conduction:
  Penetration theory: surface renewal, average k_c = 2√(D_AB/(πt))
  Lumped: Bi_mass = k_c L/D_AB < 0.1 for uniform concentration
```

### Convective Mass Transfer Coefficient

```
N_A = k_c (C_As − C_A∞)    [mol/(m²·s)]

Relationship to Sherwood:   k_c = Sh × D_AB / L

Example correlations:
  Flat plate, laminar:    Sh = 0.664 Re^(1/2) Sc^(1/3)
  Tube, turbulent:        Sh = 0.023 Re^0.8 Sc^(1/3)
  Sphere:                 Sh = 2 + 0.6 Re^(1/2) Sc^(1/3)  (Ranz-Marshall)
```

### Two-Film Theory (Interphase Mass Transfer)

For gas-liquid systems (absorption, distillation):
```
N_A = k_G (p_A − p_Ai) = k_L (C_Ai − C_A)

where subscript i = interface; G = gas film; L = liquid film

Henry's law: p_Ai = H C_Ai   (interface equilibrium)

Overall gas-phase coefficient:
  1/K_G = 1/k_G + H/k_L    (series resistance)

Overall liquid-phase coefficient:
  1/K_L = 1/(k_L) + 1/(H k_G)

H ≪ 1 (high solubility): K_L ≈ k_L  (gas film negligible — liquid film controls)
H ≫ 1 (low solubility): K_G ≈ k_G  (liquid film negligible — gas film controls)
```

---

## Packed Beds

Widely used: fixed-bed reactors, absorption columns, adsorbers.

**Pressure drop — Ergun equation:**
```
ΔP/L = 150 μ v_s (1−ε)² / (d_p² ε³) + 1.75 ρ v_s² (1−ε) / (d_p ε³)
             ↑                                   ↑
          viscous term                       inertial term
      (Kozeny-Carman)                        (Burke-Plummer)

ε = void fraction (typically 0.35–0.45 for random packing)
d_p = particle diameter, v_s = superficial velocity
```

**Mass transfer in packed beds:**
```
k_c a = 1.17 Re^(-0.415) D_AB/d_p × (Re Sc^(1/3))
      ≈ Sh correlation with a = 6(1−ε)/d_p  (specific interfacial area)

Colburn j-factor for beds:  j_D = 1.17 Re^(-0.415)  (range Re = 10–10,000)
```

---

## Dimensional Analysis in Transport

Buckingham Π theorem applied to transport problems.

**Example: forced convection heat transfer in pipe**
```
Variables: h, v, D, ρ, μ, Cp, k
n = 7, k_dim = 4 (M, L, T, θ) → 7−4 = 3 Π groups
Π₁ = Nu = hD/k,  Π₂ = Re = ρvD/μ,  Π₃ = Pr = Cpμ/k
→ Nu = f(Re, Pr)  → all forced convection heat transfer correlations have this form
```

**Transport numbers and Lewis analogy:**
```
Le = α/D_AB = Sc/Pr   (Lewis number)

For Lewis = 1 (common approximation for gases):
  Wet bulb temperature equation: T_wb = T_dry − (h_vap/Cp)(y_s − y)
  h ≈ k_c ρ Cp   (heat and mass transfer coefficients linked)
```

---

## Transport in Complex Systems

### Simultaneous Heat and Mass Transfer (Drying)

```
Constant rate period: surface wet, rate = k_c (C_As − C_A∞)
  → controlled by external mass transfer + heat transfer
  → wet bulb temperature at surface

Falling rate period: surface dries, diffusion within solid limits
  → rate decreases → longer drying time

Characteristic drying curve: rate vs moisture content

Spray drying: droplets in hot gas → simultaneous heat/mass → fast drying
```

### Reactive Absorption (e.g., CO₂ scrubbing with amine)

```
CO₂ absorbed at gas-liquid interface → reacts with amine in liquid film
Enhancement factor E: actual rate / physical absorption rate

For fast reaction: E ≫ 1 (reaction in film enhances mass transfer)
For instantaneous reaction: E_i = 1 + D_A C_Bi / (b D_B C_Ai)
  b = stoichiometric coefficient
```

---

## Common Confusion Points

**Flux direction conventions:** In BSL, flux is in direction of decreasing concentration/temperature/velocity. Negative sign in Fick's/Fourier's/Newton's laws ensures flux is positive in direction of transport. Check signs carefully when setting up shell balances.

**Molar flux J_A vs N_A:** J_A = flux relative to molar average velocity (used in binary diffusion). N_A = absolute molar flux (includes both diffusion and convective transport). For dilute solutions: N_A ≈ J_A. For concentrated systems: N_A = J_A + x_A(N_A + N_B).

**Two-film theory: which film controls?** Look at H (Henry's constant):
- Oxygen in water: H very large → oxygen very sparingly soluble → gas film irrelevant → liquid film controls
- CO₂ in water: moderate H → both films matter
- Ammonia in water: H small → very soluble → gas film can control

**Peclet number in different contexts:** In BSL, Pe = vL/D_AB (mass transport). In heat transfer, Pe_heat = vL/α = Re×Pr. In reactor engineering, Pe = vL/D_a (axial dispersion). All the same mathematical form, different diffusivities.

---

## Decision Cheat Sheet

| Problem | Approach | Key formula |
|---------|---------|------------|
| Velocity profile in tube | Shell balance or N-S | Hagen-Poiseuille |
| Heat transfer coefficient | Nusselt correlation | Nu = 0.023 Re^0.8 Pr^0.4 |
| Mass transfer coefficient | Sherwood correlation | Sh = same with Sc |
| Gas-liquid absorption | Two-film theory | 1/K_G = 1/k_G + H/k_L |
| Packed bed pressure drop | Ergun equation | Viscous + inertial terms |
| Unsteady diffusion | Fick's second law | Penetration or Heisler |
| Scale heat/mass correlations | Analogy + j-factors | j_H = j_D = f/2 |
| Combined drying | Characteristic drying curve | Constant rate then falling rate |
