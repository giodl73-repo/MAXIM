# 03 — Heat Transfer

## Conduction, Convection, Radiation, Heat Exchangers

```
THREE MODES OF HEAT TRANSFER

CONDUCTION          CONVECTION           RADIATION
─────────────       ─────────────        ─────────────
q = −kA dT/dx       q = hA(Ts − T∞)     q = εσA(Ts⁴ − Tsurr⁴)
                                          ↑ no medium needed
Through solid       Fluid motion          Electromagnetic waves
or stationary       carries energy        even through vacuum
fluid
                    Forced: pump/fan      Black body: ideal emitter
k = material        drives flow           Real: ε < 1
conductivity
                    Natural: buoyancy
                    drives flow

All three often act simultaneously in real problems
```

---

## Thermal Conductivity Reference

| Material | k [W/(m·K)] | Notes |
|----------|------------|-------|
| Diamond | 2000 | Highest known solid |
| Copper | 401 | Best common metal for cooling |
| Aluminum | 237 | Standard heat sink material |
| Steel (carbon) | 50 | Lower — structural use |
| Stainless steel | 15 | Much lower — poor conductor |
| Glass | 1.4 | Insulating compared to metals |
| Water (liquid) | 0.6 | Surprisingly good for a liquid |
| Polyurethane foam | 0.03 | Building insulation |
| Air (still) | 0.026 | Why cavities insulate |
| Aerogel | 0.015 | Best practical insulator |

---

## Conduction

### Fourier's Law

```
q = −kA dT/dx    [W]           (1D, heat flow in x)
q" = −k dT/dx   [W/m²]         (heat flux, per unit area)
```

For steady 1D: q = kA(T₁ − T₂)/L  → thermal resistance R_cond = L/(kA)

### Thermal Resistance Network (exact analogy to electrical)

```
Electrical:  ΔV = I × R_elec
Thermal:     ΔT = q × R_therm

R_wall = L/(kA)              (plane wall)
R_cyl  = ln(r₂/r₁)/(2πkL)  (cylindrical wall, per unit length: ln(r₂/r₁)/(2πk))
R_conv = 1/(hA)              (convection resistance)
R_contact = 1/(h_c A)        (contact resistance — often dominant in electronics)

Series: R_total = ΣR_i  (same heat flux through each layer)
Parallel: 1/R_total = Σ(1/R_i)  (same ΔT across each path)
```

**Composite wall example (house wall):**
```
Outside air → convection → siding → conduction → insulation → drywall → convection → inside air
R_total = 1/(h_out A) + L_siding/(k_s A) + L_ins/(k_i A) + L_dry/(k_d A) + 1/(h_in A)
```

### Extended Surfaces (Fins)

Fins increase surface area to enhance convection:
```
Fin efficiency η_f = actual heat transfer / heat transfer if entire fin at base temperature

For straight rectangular fin:
  η_f = tanh(mL)/(mL)
  where m = √(hP/(kAc))
        P = perimeter, Ac = cross-sectional area

Fin effectiveness ε_f = fin heat transfer / heat transfer without fin
  ε_f = q_fin / (hAc,b(Tb − T∞))

Worth adding fins if ε_f > 2 (doubling is break-even)
```

### Transient Conduction

**Lumped capacitance** (uniform temperature throughout object):
Valid when Biot number Bi = hLc/k < 0.1 (surface resistance >> internal resistance)
```
Bi = h(V/A)/k    [Lc = V/A for general shape]

If Bi < 0.1:
  (T − T∞)/(Ti − T∞) = exp(−t/τ)
  τ = ρVc/(hA)   ← time constant

If Bi > 0.1: use Heisler charts or full PDE solution
```

**Semi-infinite solid** (sudden surface temperature change):
```
T(x,t) − Ts / Ti − Ts = erf(x / (2√(αt)))

where α = k/(ρc) = thermal diffusivity [m²/s]
erf = error function
```

---

## Convection

### Governing Dimensionless Numbers

```
Nusselt:    Nu = hL/k        (dimensionless convection coefficient, ratio of convective to conductive)
Reynolds:   Re = ρvL/μ       (inertia/viscous in fluid)
Prandtl:    Pr = c_p μ/k = ν/α  (momentum diffusivity/thermal diffusivity)
Grashof:    Gr = gβΔTL³/ν²  (buoyancy/viscous, for natural convection)
Rayleigh:   Ra = Gr × Pr     (natural convection parameter)

Useful form: Nu = C Re^m Pr^n  (forced convection correlations all have this form)
```

Dimensionless numbers arise from Buckingham Pi theorem: any physically meaningful equation can be restated in terms of dimensionless groups. Systems with identical dimensionless groups (Re, Pr, Nu) exhibit identical physics regardless of absolute scale — this is why wind tunnel models work. The groups collapse the parameter space: instead of varying velocity, density, viscosity, and length independently, we need only vary Re.

**Prandtl number intuition:**
- Pr ≪ 1 (liquid metals: Pr ~ 0.003–0.03): thermal BL >> velocity BL
- Pr ≈ 1 (gases: Pr ~ 0.7): similar thicknesses
- Pr ≫ 1 (viscous oils: Pr ~ 100–10,000): velocity BL >> thermal BL

### Forced Convection — Internal Flow (Pipe)

**Thermal entry length:**
```
Hydrodynamic: x_fd,h ≈ 0.05 Re D  (laminar)
Thermal:      x_fd,t ≈ 0.05 Re Pr D

Fully developed laminar (Ts = const): Nu = 3.66
Fully developed laminar (qs = const): Nu = 4.36
```

**Turbulent (Dittus-Boelter, 0.6 < Pr < 160, Re > 10,000):**
```
Nu = 0.023 Re^0.8 Pr^n   (n = 0.4 heating, n = 0.3 cooling)
```

**Gnielinski** (more accurate, 0.5 < Pr < 2000, 3000 < Re < 5×10⁶):
```
Nu = (f/8)(Re − 1000)Pr / [1 + 12.7(f/8)^(1/2)(Pr^(2/3) − 1)]
f = friction factor from Moody chart
```

### Forced Convection — External Flow

**Flat plate:**
```
Laminar (Re_x < 5×10⁵):  Nu_x = 0.332 Re_x^(1/2) Pr^(1/3)  (local)
Turbulent (Re > 5×10⁵):  Nu_x = 0.0296 Re_x^(4/5) Pr^(1/3)
Average over plate: Nu_L = 0.664 Re_L^(1/2) Pr^(1/3)  (all laminar)
```

**Cylinders in crossflow (Churchill-Bernstein):**
```
Nu = 0.3 + 0.62 Re^(1/2) Pr^(1/3) / [1+(0.4/Pr)^(2/3)]^(1/4) × [1+(Re/282000)^(5/8)]^(4/5)
```

**Spheres (Whitaker):**
```
Nu = 2 + (0.4 Re^(1/2) + 0.06 Re^(2/3)) Pr^0.4 (μ/μ_s)^(1/4)
Limiting case Re → 0: Nu = 2 (pure conduction to sphere)
```

### Natural (Free) Convection

Driven by buoyancy from density differences due to temperature gradients.

**Vertical plate (Churchill-Chu):**
```
Nu^(1/2) = 0.825 + 0.387 Ra^(1/6) / [1 + (0.492/Pr)^(9/16)]^(8/27)
```
Valid for all Ra. Ra = Gr × Pr.

**Natural vs forced convection criterion:**
```
Gr/Re² ≈ 1 → mixed convection
Gr/Re² ≪ 1 → forced convection dominates
Gr/Re² ≫ 1 → free convection dominates
```

---

## Boiling and Condensation

### Pool Boiling Curve (Nukiyama 1934)

```
q" (heat flux)
     │
     │              D (critical heat flux, CHF)
     │           ╱
     │          ╱ Nucleate boiling
     │    C ───╱
     │   ╱
     │  ╱  Transition
     │ ╱   (unstable)
     │╱
     B ──────────────────── Film boiling
     │                      (Leidenfrost point)
     │
     A (onset of nucleation)
     └────────────────────── T_s − T_sat (excess temperature)
```

**Regimes:**
- Natural convection (A): q" ∝ (Ts − Tsat)^(5/4), single phase
- Nucleate boiling (A→D): bubbles nucleate at surface, very high h (up to 10⁵ W/m²K)
- Critical heat flux (D): vapor blanket starts forming, q"_max ≈ 1.5 MW/m² for water at 1 atm
- Transition (D→E): unstable, h drops dramatically
- Film boiling (E→): stable vapor film, low h — Leidenfrost effect (droplets skitter on hot surface)

**Critical heat flux (Zuber correlation):**
```
q"_max = 0.131 h_fg ρ_v [σg(ρ_l − ρ_v)/ρ_v²]^(1/4)
```

### Condensation

**Film condensation on vertical plate (Nusselt analysis):**
```
h̄ = 0.943 [ρ_l (ρ_l − ρ_v) g k_l³ h_fg'] / (μ_l ΔT L)^(1/4)

where h_fg' = h_fg + 0.68 c_p,l ΔT  (modified latent heat)
```

Dropwise condensation: 5–10× higher than film condensation (no liquid film resistance).
Promoting dropwise condensation (hydrophobic surfaces) is an active research area.

---

## Radiation

### Blackbody Radiation

A perfect emitter/absorber (idealization):
```
Planck distribution (spectral emissive power):
  E_b,λ = C₁ / [λ⁵(exp(C₂/λT) − 1)]
  C₁ = 3.742×10⁸ W·μm⁴/m², C₂ = 1.439×10⁴ μm·K

Wien's displacement law (peak wavelength):
  λ_max T = 2898 μm·K
  Sun (5800K): λ_max ≈ 0.5 μm (visible)
  Human body (310K): λ_max ≈ 9.3 μm (far infrared)

Stefan-Boltzmann law (total power):
  E_b = σT⁴   where σ = 5.67×10⁻⁸ W/(m²·K⁴)
```

### Real Surface Properties

```
Emissivity:       ε = E/E_b  (0 ≤ ε ≤ 1)
Absorptivity:     α = absorbed/incident
Reflectivity:     ρ = reflected/incident
Transmissivity:   τ = transmitted/incident
                  α + ρ + τ = 1

Kirchhoff's law: ε = α  (at thermal equilibrium, or for grey surfaces)
Grey surface: ε independent of wavelength
```

**Typical emissivities:**
| Surface | ε |
|---------|---|
| Blackbody | 1.0 |
| Polished copper | 0.03 |
| Polished aluminum | 0.05 |
| White paint | 0.90–0.98 |
| Black paint | 0.96–0.98 |
| Brick | 0.90–0.93 |
| Human skin | 0.95 |

### View Factors (Shape Factors)

F₁₂ = fraction of radiation leaving surface 1 that reaches surface 2.

```
Reciprocity: A₁F₁₂ = A₂F₂₁
Summation:   ΣFᵢⱼ = 1  (enclosure)
Superposition, crossed-string method for 2D

Common F₁₂:
  Concentric cylinders (inner to outer): F₁₂ = 1
  Large parallel plates (A₁=A₂, close together): F₁₂ = 1
  Small object in large enclosure: F₁₂ = 1
```

### Radiation Network Method (Grey-Diffuse Enclosure)

```
For each surface:
  E_b = σT⁴              (blackbody power)
  J = radiosity          (power leaving surface = emitted + reflected)

  Surface resistance: (1−ε)/(εA)   connects E_b to J
  Space resistance:   1/(A_i F_ij) connects J_i to J_j

Radiation exchange between two grey-diffuse surfaces:
  q₁₂ = σ(T₁⁴ − T₂⁴) / [(1−ε₁)/(ε₁A₁) + 1/(A₁F₁₂) + (1−ε₂)/(ε₂A₂)]
```

---

## Heat Exchangers

### LMTD Method (Log Mean Temperature Difference)

```
q = U A ΔT_lm

ΔT_lm = (ΔT₁ − ΔT₂) / ln(ΔT₁/ΔT₂)

For counterflow: ΔT₁ = T_h,in − T_c,out,  ΔT₂ = T_h,out − T_c,in
For parallel flow: ΔT₁ = T_h,in − T_c,in,  ΔT₂ = T_h,out − T_c,out

Overall heat transfer coefficient:
  1/(UA) = 1/(h_h A_h) + R_fouling,h + R_wall + R_fouling,c + 1/(h_c A_c)
```

**Counterflow advantage:** Counterflow allows T_c,out > T_h,out (impossible in parallel flow). Higher LMTD → smaller area for same duty.

### NTU-Effectiveness Method

Better when outlet temperatures are unknown:
```
Effectiveness: ε = q / q_max

q_max = C_min × (T_h,in − T_c,in)   where C_min = min(ṁc_p) stream

NTU = UA / C_min   (Number of Transfer Units)

For counterflow HX:
  If C_min/C_max = c < 1:
    ε = [1 − exp(−NTU(1−c))] / [1 − c·exp(−NTU(1−c))]
  If c = 1:
    ε = NTU / (NTU + 1)
```

**Fouling factor R_f:** Deposits on surfaces add resistance over time. TEMA standards specify R_f for different fluids. Clean new HX has lower resistance than after months of operation.

### Heat Exchanger Types

```
Type            Geometry              Typical use
──────────────────────────────────────────────────────────────
Shell-and-tube  Tubes inside shell    Oil refining, power plants
Plate frame     Corrugated plates     Food/pharma (easy cleaning)
Double-pipe     Pipe within pipe      Small duty, lab use
Finned tube     Fins on outer surface HVAC, radiators, condensers
Cross-flow      Perpendicular flows   Automotive radiator, air coolers
Spiral          Spiral passages       Viscous fluids, slurries
Heat pipe       Wick + vapor          Electronics cooling, spacecraft
```

---

## Data Center / Electronics Cooling

This is where thermal and computing intersect. A 1U server might dissipate 300–1000W.

```
Package → TIM → Heatsink → Airflow

Thermal resistance path (CPU package):
  R_junction-case:  0.1–0.5 K/W  (chip to package lid)
  R_TIM:           0.05–0.3 K/W  (thermal interface material)
  R_case-heatsink: 0.1–0.5 K/W  (heatsink base)
  R_heatsink-air:  0.3–2 K/W    (fin array + forced convection)

T_junction = T_air + q × R_total
Max T_junction for modern CPUs: ~105°C (Intel), ~95°C (AMD)
Data center PUE (Power Usage Effectiveness) = total facility power / IT power
  World average: ~1.6, Best: ~1.05 (Google/hyperscalers with liquid cooling)
```

**Liquid cooling trend:** Water-cooled cold plates (data centers), two-phase immersion cooling.
Water specific heat ~4200 J/(kg·K) vs air ~1005 J/(kg·K) → 4× more heat per unit mass.
Water density ~830× air density → massive improvement in volumetric heat capacity.

---

## Common Confusion Points

**Conduction vs convection coefficient h:** k is a material property (W/m·K). h is a system property (depends on flow, geometry) — you cannot look up h, you calculate Nu from correlations.

**Lumped capacitance validity:** Bi < 0.1 means internal resistance << external resistance → temperature nearly uniform internally. High-conductivity metals with forced air cooling often satisfy this; plastic parts or large bodies rarely do.

**View factors are geometric only:** F₁₂ depends only on geometry, not on temperature or emissivity. Emissivity enters in the radiation network.

**LMTD for multipass:** Standard LMTD formula is for pure counterflow or parallel flow. Multipass shell-and-tube HX needs correction factor F: q = U A F ΔT_lm,cf.

**Radiation at low temperatures:** σT⁴ — radiation scales as T⁴. At room temperature (300K): q" ≈ 460 W/m². At 100°C (373K): q" ≈ 1100 W/m². Radiation matters even at moderate temperatures when ε is high and convection is low (e.g., bare heater in still air).

---

## Decision Cheat Sheet

| Problem type | Method | Key formula |
|-------------|--------|------------|
| Conduction, composite wall | Thermal resistance network | ΔT = q × R_total |
| Thin object cooled rapidly | Lumped capacitance | Check Bi < 0.1 first |
| Forced convection in pipe | Dittus-Boelter (turbulent) | Nu = 0.023 Re^0.8 Pr^n |
| Natural convection, vertical plate | Churchill-Chu | Nu from Ra = Gr×Pr |
| HX design with known T's | LMTD method | q = UA × ΔT_lm |
| HX design with unknown outlet T's | NTU-effectiveness | ε = f(NTU, C_min/C_max) |
| Radiation between grey surfaces | Network method | q = σ(T₁⁴−T₂⁴)/Σ_resistances |
| Electronics thermal budget | Series resistance | T_junction = T_ambient + q×R_total |
| Boiling / CHF | Nukiyama curve | Know critical heat flux regime |
