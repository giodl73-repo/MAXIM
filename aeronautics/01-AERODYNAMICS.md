# 01 — Aerodynamics

## Lift, Drag, Boundary Layers, Compressible Flow, Wing Theory

---

## Big Picture: Aerodynamic Flow Regimes

```
┌──────────────────────────────────────────────────────────────────────────┐
│                    AERODYNAMIC FLOW HIERARCHY                            │
├──────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  GOVERNING EQUATIONS                                                     │
│  Navier-Stokes: full viscous, compressible flow                         │
│       │                                                                  │
│       ├── High Re, inviscid: EULER EQUATIONS                            │
│       │   → Potential flow, lifting line, panel methods                 │
│       │                                                                  │
│       └── Viscous region: BOUNDARY LAYER EQUATIONS (Prandtl)           │
│           → Skin friction, separation, transition                        │
│                                                                          │
│  FLOW REGIMES by Mach:                                                  │
│  M < 0.3: incompressible (ρ = const) — good for GA aircraft             │
│  0.3 < M < 0.8: compressible subsonic — transonic corrections           │
│  0.8 < M < 1.2: transonic — mixed regions, shock waves forming         │
│  M > 1.2: supersonic — oblique shocks, expansion fans                  │
│  M > 5: hypersonic — chemistry, ablation                               │
│                                                                          │
└──────────────────────────────────────────────────────────────────────────┘
```

---

## 1. Governing Equations

### Navier-Stokes

```
CONTINUITY (mass conservation):
  ∂ρ/∂t + ∇·(ρ**u**) = 0
  Incompressible (ρ = const): ∇·**u** = 0

MOMENTUM (N-S):
  ρ(∂**u**/∂t + **u**·∇**u**) = −∇p + μ∇²**u** + ρ**g**
  Left: inertia; Right: pressure gradient + viscous + body force
  Incompressible + steady: ρ(**u**·∇)**u** = −∇p + μ∇²**u**

ENERGY (for compressible):
  ρDe/Dt = −p(∇·**u**) + Φ + ∇·(k∇T)
  Φ = viscous dissipation; k = thermal conductivity

REYNOLDS NUMBER: Re = ρVL/μ = VL/ν
  Ratio of inertial to viscous forces
  Low Re (< ~10³): viscous dominated; laminar; no separation
  High Re (>10⁶): inertia dominated; thin boundary layer; potential flow core
  Transition: Re_crit ≈ 5×10⁵ for flat plate; variable for airfoils (depends on pressure gradient)

BERNOULLI EQUATION (incompressible, inviscid, steady, along streamline):
  p + ½ρV² + ρgh = constant = p₀ (total pressure)
  Dynamic pressure: q = ½ρV²
  Stagnation (total) pressure: p₀ = p + q
  Pitot tube: measures p₀; static port measures p; q = p₀ - p → V = √(2q/ρ)
```

### Potential Flow

**PDE bridge:** Potential flow solves Laplace's equation (nabla^2 phi = 0) — the same equation governing electrostatic potential and steady-state heat conduction. The full toolkit from complex analysis applies: analytic functions map conformally, and the Joukowski transform maps the solved cylinder+vortex problem to airfoil shapes. Thin airfoil theory replaces the airfoil with a singularity distribution on the chord line — a method-of-moments approach on Laplace's equation. This is why potential flow aerodynamics is a solved PDE problem, and why panel methods (discretized boundary integral equations) work so well.

```
IRROTATIONAL FLOW: ∇×**u** = 0 → exists velocity potential φ: **u** = ∇φ
  Incompressible: ∇²φ = 0 (Laplace equation — same as electrostatics)
  Superposition: sum of solutions is a solution

ELEMENTARY FLOWS (building blocks):
  Uniform flow: φ = U∞x (flow from left)
  Source/sink: φ = (Q/2π)ln(r) (radial flow; Q = volume flow rate)
  Doublet: source + sink at same point
  Free vortex: φ = (Γ/2π)θ; ψ = −(Γ/2π)ln(r); circulation Γ

CYLINDER IN UNIFORM FLOW (doublet + uniform flow):
  ψ = U∞(r − R²/r)sin(θ)
  CL = 0 (symmetric flow; no lift by d'Alembert's paradox)
  D'Alembert's paradox: perfect inviscid flow → zero drag (no shear; symmetric pressure)
  → Viscosity and separation are essential for drag

CYLINDER + VORTEX (with circulation):
  Adds vortex φ = (Γ/2π)θ to doublet + uniform flow
  → Asymmetric stagnation points → lift!
  Kutta-Joukowski Theorem: L = ρ∞V∞Γ per unit span
    Lift = density × freestream velocity × circulation
    This is the FUNDAMENTAL lift equation; applies to any 2D body in inviscid flow
```

---

## 2. Airfoil Theory

### Airfoil Geometry and Nomenclature

```
NACA 4-DIGIT (e.g., NACA 2412):
  2: maximum camber = 2% of chord
  4: maximum camber location = 40% of chord (from LE)
  12: maximum thickness = 12% of chord

NACA 5-DIGIT: more flexible camber line definition
NACA 6-SERIES: designed for specific pressure distributions (transition delay, low drag bucket)
  NACA 64-212: 6-series; min pressure at 40% chord; CL_design = 0.2; 12% thick

SUPERCRITICAL AIRFOIL (Whitcomb, NASA):
  Flat upper surface → lower peak suction → delayed Mcrit
  Used on all modern transonic aircraft (Boeing 787, Airbus A350)

AIRFOIL PERFORMANCE PARAMETERS:
  CL (lift coefficient): non-dimensional lift = L/(qS)
  Angle of attack (α): between chord line and freestream
  CLα = dCL/dα = 2π per radian (thin airfoil theory for symmetric airfoil)
  Stall: flow separation from upper surface at CLmax; α_stall ≈ 15°-20° typical
  Zero-lift angle α₀: cambered airfoils lift even at α = 0° → α₀ < 0° (nose-down for positive camber)
  Moment coefficient: Cm about aerodynamic center (typically c/4 from LE)
    Aerodynamic center (AC): point where Cm is constant with α (≈ c/4 for subsonic)
    Center of pressure (CP): moves with α; where net aerodynamic force acts
    CP forward of CG → destabilizing; CP behind CG → stabilizing (horizontal tail provides this)
```

### Thin Airfoil Theory

```
FUNDAMENTAL EQUATION (Glauert):
  1/(2π) ∫₀^π γ(θ) (1 - cos θ) / (cos θ - cos θ₀) dθ = V∞(α - dZ_c/dx)
  γ = vortex sheet strength along chord; Z_c = camber line ordinate
  Solution via Fourier series: γ(θ) = 2V∞[A₀(1+cos θ)/sin θ + Σ Aₙ sin(nθ)]

  A₀ = α - (1/π)∫₀^π (dZ_c/dx) dθ₀
  Aₙ = (2/π)∫₀^π (dZ_c/dx) cos(nθ₀) dθ₀

RESULTS:
  CL = 2π(α - α₀)  [linear lift slope = 2π for thin airfoil]
  Cm_AC = -π/2 × A₁  [depends only on camber, not α]
  AC at quarter-chord (x/c = 0.25) for all thin airfoils

  Symmetric airfoil: α₀ = 0, Cm_AC = 0
  Cambered airfoil: α₀ = -(1/π)∫ (dZ_c/dx) dθ₀ < 0
```

---

## 3. Boundary Layer Theory

### Prandtl's Boundary Layer

**Singular perturbation bridge:** Prandtl's boundary layer is a singular perturbation of Navier-Stokes: the small parameter is 1/Re, and the boundary layer is the inner solution in a matched asymptotic expansion. The outer solution is inviscid potential flow; the inner solution satisfies the boundary layer equations (parabolic PDE). The Blasius solution is a self-similar ODE reduction. This explains why BL thickness scales as delta ~ Re^(-1/2) and why the technique breaks down at separation (where the parabolic assumption fails).

```
PHYSICAL PICTURE:
  For high Re: thin viscous layer near surface; inviscid flow outside
  Within BL: velocity goes from 0 at wall (no-slip) to U∞ at edge
  Thickness: δ ≈ 5.0 x / √(Re_x) for laminar flat plate (Blasius)
  Displacement thickness: δ* = ∫₀^∞ (1 - u/U) dy (effective "thickening" of body)
  Momentum thickness: θ = ∫₀^∞ (u/U)(1 - u/U) dy

BOUNDARY LAYER EQUATIONS (2D incompressible):
  u ∂u/∂x + v ∂u/∂y = −(1/ρ)dp/dx + ν ∂²u/∂y²
  Thin: ∂p/∂y ≈ 0 (pressure across BL ≈ constant; set by external flow)

LAMINAR vs TURBULENT:
  Laminar BL: Blasius profile; skin friction Cf = 0.664 / √(Re_x)
  Turbulent BL: thicker; fuller profile; skin friction Cf ≈ 0.074 / Re_x^0.2 (Prandtl's 1/7 power law)
    Higher skin friction BUT more resistant to separation (fuller profile; higher momentum near wall)
  Transition: Re_crit ≈ 3×10⁵ to 3×10⁶ depending on free-stream turbulence, pressure gradient

SEPARATION:
  Adverse pressure gradient: dp/dx > 0 (pressure increasing, decelerating flow)
  Momentum near wall insufficient → flow reverses → separation
  Separated flow: dead air; massive drag increase; lift loss
  Airfoil stall = boundary layer separation from upper surface (leading edge or trailing edge)
  Turbulent BL resists separation better than laminar (more momentum near wall)

TRANSITION CONTROL:
  Natural laminar flow (NLF): smooth surface; favorable pressure gradient → delay transition
    NACA 6-series designed for this; Boeing 787, A320neo nacelles
  Suction: remove BL through perforations → maintain laminar BL further
  Roughness trips (turbulators): intentionally trigger turbulent BL ahead of potential separation
    → turbulent BL separates later; counterintuitive benefit
    Golf ball dimples: same principle
```

---

## 4. Finite Wings — 3D Aerodynamics

### Lifting Line Theory (Prandtl)

```
INDUCED DRAG: consequence of finite wing generating lift
  Wing tip vortices: trailing vortex pair (clockwise from right tip; counterclockwise from left)
  Induced downwash w: velocity field pointing downward behind wing from tip vortices
  Local effective angle of attack reduced by downwash: αeff = α - εi
  Induced angle: εi = w/V∞
  Induced drag: Di = L × sin(εi) ≈ L × εi for small εi

PRANDTL LIFTING LINE (elliptical distribution):
  For elliptical spanwise lift distribution (optimal):
    CL_i = 2CL / (πAR)
    CDi = CL² / (πAR)    ← fundamental result
    AR = b² / S (aspect ratio; b = span; S = wing area)

  Key insight: Induced drag ∝ CL²/AR
    High AR → low induced drag (gliders, airliners)
    Low AR → high induced drag (fighters, supersonic)
    Winglets: increase effective AR, reduce tip vortex strength

SPAN EFFICIENCY: CDi = CL² / (πeAR)  where e ≤ 1 (Oswald efficiency factor)
  Elliptical distribution: e = 1 (optimal)
  Most aircraft: e ≈ 0.8-0.95
  Winglets: e can exceed 1 for isolated wing (reduce induced drag below elliptical prediction)

SWEEP EFFECTS:
  Leading edge sweep: reduces effective velocity component perpendicular to LE
    → delays Mcrit (∝ cos Λ); reduces transonic wave drag
    → reduces effective lift slope (CLα ∝ cos Λ)
  Swept-back wing: aerodynamic center shifts rearward → more stable; needs smaller tail
  Forward swept: AC shifts forward; less tail needed; but unstable → needs FBW
    (X-29 demonstrator: intentionally unstable + fly-by-wire)
```

---

## 5. Compressible Flow and Shock Waves

### Subsonic Compressibility

```
PRANDTL-GLAUERT CORRECTION (subsonic):
  CL_compressible = CL_incompressible / √(1 - M²)
  Lift increases with Mach number (for same α) due to compressibility
  Valid for M < Mcrit (where first shock forms on wing upper surface)

CRITICAL MACH NUMBER (Mcrit):
  Mach at which local flow first reaches M = 1 somewhere on the wing (usually upper surface peak)
  Typical transonic airliners: Mcrit ≈ 0.72-0.80
  Beyond Mcrit: normal shock appears → wave drag + potential buffet

AREA RULE (Whitcomb, 1952):
  Transonic wave drag ∝ second derivative of cross-sectional area distribution
  Smooth area distribution → minimum transonic drag
  "Waist" fuselage (coke bottle shape) compensates for wing cross-section at fuselage junction
```

### Supersonic Flow

```
NORMAL SHOCK RELATIONS (Rankine-Hugoniot):
  Properties across normal shock (from state 1 upstream to state 2 downstream):

  M₂² = (M₁² + 5) / (7M₁² - 1)  [for γ = 1.4]
  p₂/p₁ = (7M₁² - 1) / 6
  ρ₂/ρ₁ = 6M₁² / (M₁² + 5)
  T₂/T₁ = (7M₁² - 1)(M₁² + 5) / (36M₁²)

  M₂ < 1 always (flow behind normal shock is subsonic)
  Entropy increases (irreversible); stagnation pressure decreases → drag (wave drag)

OBLIQUE SHOCKS:
  At angle β to freestream; deflection angle θ
  θ-β-M relationship: connects deflection to shock angle for given M
  Weaker than normal shock; less entropy production
  Minimum detachment: at some θ_max, oblique shock becomes detached (normal shock)
  Used: supersonic inlets (ramp system for multiple oblique shocks)
         supersonic nozzle flows

EXPANSION FAN (Prandtl-Meyer):
  When supersonic flow turns outward (convex corner): accelerates → expands
  Isentropic (reversible); flow expands through Mach waves
  Opposite of shock: increase M, decrease p, T, ρ
  ν(M) = Prandtl-Meyer function; relates turning angle to Mach number

SUPERSONIC AIRFOILS:
  Flat plate: thin airfoil; lower wave drag (sharp LE)
  Diamond (double wedge): shock on LE + expansion + shock at TE
  CL = 4α / √(M²-1) per thin supersonic airfoil theory
  CD_wave = 4α² / √(M²-1) + 4(t/c)² / √(M²-1) [thickness + angle contributions]
  Area-rule applies: smooth cross-sectional area distribution minimizes drag
```

---

## 6. High-Lift Devices

```
WHY: Cruise airfoil optimized for Mcrit, L/D at Mach 0.78-0.85 is not optimal at landing
  Takeoff/Landing: need high CL at low speed (low dynamic pressure)
  Must increase CL_max substantially

FLAPS: increase effective camber and area
  Plain flap: deflects trailing edge → ↑ camber → ↑ CL, ↑ CD, nose-down moment
  Split flap: bottom surface only; simple; more drag
  Slotted flap: slot between wing and flap; energizes BL → delays separation
    Single/double/triple slotted: progressively more complex; ΔCL_max = 0.9-1.3 per slot
  Fowler flap: moves rearward while deflecting → ↑ effective chord + camber; highest lift gain
    Modern airliners: double/triple Fowler flaps; ΔCL_max ≈ 1.5-2.0

SLATS: extend and/or droop leading edge → ΔCL_max ≈ 0.5-1.0
  Fixed slat: simple; drag penalty in cruise (non-retractable)
  Variable-camber Krueger flap: under-wing; pops forward
  LE slat (most common): retractable slot between slat and wing → BL re-energization

TOTAL CL_max:
  Clean wing: CL_max ≈ 1.2-1.5
  Takeoff flaps: CL_max ≈ 2.0-2.5
  Landing flaps + slats: CL_max ≈ 2.5-3.2
  V_stall = √(2W / (ρ S CL_max)) → 1.23 V_stall = V₂ (takeoff safety speed)
```

---

## Decision Cheat Sheet

| Parameter | Effect | Key Relation |
|-----------|--------|-------------|
| Angle of attack | ↑ α → ↑ CL (until stall) | CL = 2π(α - α₀) [thin airfoil] |
| Aspect ratio | ↑ AR → ↓ induced drag | CDi = CL²/(πeAR) |
| Reynolds number | ↑ Re → ↑ skin friction; ↓ separation | Re = ρVL/μ |
| Mach number | ↑ M → ↑ CL (Prandtl-Glauert); above Mcrit: wave drag | CL ∝ 1/√(1-M²) |
| Wing sweep | ↑ Λ → ↑ Mcrit; ↓ effective CLα | Mcrit ∝ 1/cos Λ (approx) |
| Flaps deployed | ↑ CL_max; ↑ CD; ↓ nose-up moment | ΔCL_max ≈ 0.3-2.0 depending on type |

---

## Common Confusion Points

**Bernoulli's equation and lift:** The popular "air moves faster over top because longer path" explanation is wrong (equal transit fallacy — air doesn't need to arrive simultaneously). Bernoulli does apply within streamlines, but the reason air moves faster over the upper surface is the circulation imposed by the wing — which must be set by the Kutta condition at the trailing edge. Lift = ρVΓ.

**Boundary layer thickness vs displacement thickness:** The physical boundary layer thickness δ (where u ≈ 0.99 U∞) is 5-10× larger than the displacement thickness δ* (the effective body "thickening"). Aerodynamicists use δ* and momentum thickness θ for shape factor H = δ*/θ in separation prediction.

**Induced drag depends on CL², not V²:** At cruise, CL is smaller (airplane goes fast; same lift at lower angle). Induced drag decreases quadratically with speed. Parasite drag increases quadratically with speed. Total drag minimum at best L/D speed.

**Swept wings are not just for supersonic:** Even on subsonic transonic aircraft (M = 0.78-0.85), sweep delays the formation of shocks on the wing by reducing the component of velocity perpendicular to the leading edge. Without sweep, M_crit would be around M = 0.6-0.7, requiring much lower cruise speeds.

**Normal shocks and supersonic flight:** Once a normal shock forms on a wing in transonic flight, stagnation pressure loss across it creates wave drag. This is why transonic aircraft have smooth area distributions (Whitcomb's area rule), swept wings, and supercritical airfoils — all to push Mcrit higher and minimize wave drag at cruise.
