# Viscous Flow and Navier-Stokes

## The Big Picture

Viscosity is what makes fluid dynamics hard and interesting. Viscosity is momentum diffusion — it causes velocity gradients to smooth out over time, generates drag, and creates the no-slip condition at walls. The Navier-Stokes equations include viscosity and are the standard model for most engineering flows. Exact analytical solutions exist only for highly symmetric geometries (plane Couette flow, Poiseuille pipe flow, Stokes flow). For everything else, numerical methods are required. The Reynolds number Re = ρUL/μ is the ratio of inertia to viscosity — and it determines everything about how a flow behaves.

```
NAVIER-STOKES — FULL STRUCTURE
═══════════════════════════════════════════════════════════════════════════════

  INCOMPRESSIBLE, NEWTONIAN:

  ρ[∂**v**/∂t + (**v**·∇)**v**] = −∇p + μ∇²**v** + ρ**g**
  ∇·**v** = 0
  ──────────────────────────────────────────────────────────────────────
  LIMIT Re→0 (Stokes):         LIMIT Re→∞ (Euler, inviscid):
  μ∇²**v** = ∇p                ρ(**v**·∇)**v** = −∇p
  Linear! Solvable.             Nonlinear. No viscosity. No drag.
  Reversible.                   D'Alembert's paradox.
  Creeping flow.                Boundary layers (thin).
  ──────────────────────────────────────────────────────────────────────

  DIMENSIONLESS NAVIER-STOKES:
  Scale: L (length), U (velocity), L/U (time), ρU² (pressure)

  ∂**v***/∂t* + (**v***·∇*)**v*** = −∇*p* + (1/Re)∇*²**v*** + (1/Fr²)(ĝ)
  Re = ρUL/μ,   Fr = U/√(gL)
```

---

## Physical Interpretation of Viscosity

<!-- @editor[audience/P2]: Defines τ = μ(∂u/∂y) (Newton's law of viscosity) from scratch — learner calibration explicitly says this does NOT need explaining. Skip the constitutive law; open directly with the diffusivity interpretation and the μ vs ν distinction, which ARE new and useful. -->
**Dynamic viscosity μ**: Proportionality constant between shear stress and shear rate.

    τ = μ (∂u/∂y)    (Newton's law of viscosity)

**Kinematic viscosity ν = μ/ρ**: What appears in the N-S equations after dividing by ρ. Units: m²/s. Think of it as the "diffusivity of momentum."

```
VISCOSITY VALUES (approximate, 20°C):
  Water:   μ ≈ 10⁻³ Pa·s,  ν ≈ 10⁻⁶ m²/s
  Air:     μ ≈ 1.8×10⁻⁵ Pa·s,  ν ≈ 1.5×10⁻⁵ m²/s
  Honey:   μ ≈ 10 Pa·s
  Engine oil: μ ≈ 0.1–1 Pa·s

  Note: Air has LOWER dynamic viscosity but HIGHER kinematic viscosity than water.
  Kinematic viscosity = what matters for Re; this is why airplanes and submarines
  behave differently even at similar physical speeds.
```

The momentum equation at low Re:

    ∂**v**/∂t ≈ ν∇²**v** − (1/ρ)∇p

This is a diffusion equation for **v**. Viscosity diffuses momentum (smooths velocity gradients) exactly like thermal diffusivity diffuses temperature. The diffusion time scale is L²/ν.

---

## Exact Solutions to Navier-Stokes

### 1. Plane Couette Flow (steady, shear flow between two plates)

Two parallel plates, separation h. Lower plate stationary, upper plate moving at velocity U.

```
  Upper plate:  y = h  ──U──────────────────►
                         / / / / / / / / / /
  Fluid:       0 < y < h  u(y) = ? (solve N-S)
                         _ _ _ _ _ _ _ _ _ _
  Lower plate:  y = 0  ────────────────────── (stationary)
```

N-S (steady, fully developed, no pressure gradient):
    0 = μ d²u/dy²   ⟹   d²u/dy² = 0   ⟹   u = Ay + B

Boundary conditions: u(0) = 0, u(h) = U:

    **u(y) = Uy/h**    (linear velocity profile)

Shear stress: τ = μU/h (constant throughout). This is pure viscous shear — no pressure gradient needed.

### 2. Poiseuille Flow (pressure-driven pipe flow)

Steady flow in a circular pipe of radius R, driven by pressure gradient −dp/dx = G.

```
  ──────────────────────────────────────────────────
     →→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→ p₁
  r = R  wall  (no-slip: u = 0 at r = R)
                             → max u at center
  ──────────────────────────────────────────────────
  p₂ < p₁  (pressure decreases in flow direction)
```

N-S in cylindrical coordinates (fully developed, axisymmetric):
    0 = −G + μ(1/r)d/dr(r du/dr)
    u(r) = (G/4μ)(R² − r²)    (parabolic profile)

Maximum velocity: u_max = GR²/(4μ) at r = 0
Average velocity: U_avg = GR²/(8μ) = u_max/2

**Flow rate** (Poiseuille-Hagen law):

    Q = π R⁴ G / (8μ)    ∝ R⁴ (very sensitive to pipe radius!)

**Physical meaning**: Doubling pipe radius increases flow rate 16×. This is why arteries narrow (arteriosclerosis) dramatically reduces blood flow.

**Pressure drop**: ΔP = 8μLQ/(πR⁴) = 128μLQ/(πD⁴)

```
POISEUILLE VS TURBULENT (same pipe, same ΔP):
  Laminar (Re < 2300):   Q ∝ R⁴ΔP/(μL)    (Poiseuille)
  Turbulent:             Q ∝ R^{19/4}ΔP^{4/7}   (empirical — weak Re)

  Turbulent flow delivers MORE than Poiseuille prediction for same ΔP
  (flatter velocity profile, more efficient mixing)
```

### 3. Stokes Flow (Re → 0)

When Re << 1, inertia terms (**v**·∇)**v** are negligible. The Stokes equations are:

    −∇p + μ∇²**v** = 0
    ∇·**v** = 0

These are **linear** — a massive simplification. They describe flow of very viscous fluids (honey, lava, polymers) or very small objects (bacteria, particles in microsystems).

**Stokes drag on a sphere** (radius a, velocity U):

    F_drag = 6πμaU    (Stokes' law)

This is the exact solution to the Stokes equations for flow around a sphere. The drag is linear in velocity (unlike turbulent drag which is ∝ v²).

**Stokes paradox (2D)**: No solution exists for Stokes flow past an infinite cylinder in 2D. The equations have no solution that satisfies all boundary conditions. Correction requires Oseen term (partial inertia).

### 4. Stagnation Point Flow (Hiemenz Flow)

Near a stagnation point, the flow has the form:
    u = ax,   v = −ay    (outer Euler flow — straining flow)

The full N-S solution (including viscous effect near wall) gives exact similarity solution. Boundary layer thickness: δ ~ √(ν/a).

---

## Reynolds Number Regimes

The Reynolds number Re = ρUL/μ determines flow behavior:

```
Re REGIMES IN PIPE FLOW:
  Re < 2300        Laminar (Poiseuille — parabolic profile)
  2300 < Re < 4000 Transitional (intermittent turbulence)
  Re > 4000        Turbulent (flat profile, mixing)

  TRANSITION is not sharp: depends on inlet conditions,
  pipe roughness, external disturbances
  Hagen-Poiseuille prediction is exact only for laminar flow

Re REGIMES IN FLOW OVER FLAT PLATE:
  Re_x < 5×10⁵    Laminar boundary layer (Blasius)
  Re_x > 5×10⁵    Turbulent boundary layer (transition)
  (Re_x = Ux/ν where x is distance from leading edge)

Re REGIMES AROUND A CYLINDER:
  Re < 1           Stokes flow (symmetric, no separation)
  Re ~ 10          Separated wake (steady, recirculation)
  Re ~ 100         Periodic vortex shedding (Kármán street)
  Re ~ 10⁴         Complex turbulent wake
  Re > 5×10⁵       Turbulent boundary layer on cylinder (drag crisis)
```

---

## Dimensional Analysis and Buckingham Pi

Navier-Stokes in dimensionless form reveals all solutions collapse to a one-parameter family (by Re, plus Ma, Fr for compressible/gravitational effects).

**Buckingham Pi theorem**: A problem with n variables and k fundamental dimensions has n−k dimensionless parameters. For N-S:

    Variables: ρ, U, L, μ, p, t, g
    Dimensions: M, L, T → k = 3

    Dimensionless groups: Re = ρUL/μ,  Eu = p/(ρU²),  St = L/(UT),  Fr = U/√(gL)

**Similarity**: Two flows with the same Re (and other relevant dimensionless numbers) are dynamically similar — measurements from one predict the other.

**Wind tunnel testing**: Scale a ship or aircraft to a smaller model, adjust flow conditions to match Re. Results are dimensionally equivalent to full-scale. This is the foundational principle of experimental fluid mechanics.

---

## Viscous Energy Dissipation

Viscosity always converts kinetic energy to heat. The **dissipation function** Φ:

    Φ = 2μ eᵢⱼeᵢⱼ − (2μ/3)(∇·**v**)²    (Newtonian fluid)

For incompressible flow:

    Φ = μ Σᵢⱼ (∂vᵢ/∂xⱼ + ∂vⱼ/∂xᵢ)²/2

This is always ≥ 0 (viscous dissipation is irreversible — second law of thermodynamics).

In turbulence, viscous dissipation is important primarily at the smallest scales (Kolmogorov scale η where production = dissipation).

---

## Complex Fluid Effects

For completeness, beyond Newtonian:

**Power-law fluid**: τ = K(∂u/∂y)^n
- n < 1: shear-thinning (blood, ketchup, polymer solutions)
- n > 1: shear-thickening (cornstarch suspension, wet sand)
- n = 1: Newtonian

**Bingham plastic**: τ = τ₀ + μ_p(∂u/∂y) for τ > τ₀, else rigid
- Toothpaste, drilling mud, fresh concrete
- Flows only when shear stress exceeds yield stress τ₀

**Viscoelastic fluids**: Memory effects — stress depends on deformation history.
- Polymers exhibit first normal stress difference, rod climbing (Weissenberg effect), die swell
- Described by Oldroyd-B, FENE-P, or Giesekus models
- Relevant in plastic processing, blood rheology, food engineering

---

## The Navier-Stokes Millennium Problem

**Clay Prize Statement**: Prove (or disprove) that for smooth initial data **v**₀(x) with finite energy, there exists a smooth solution **v**(x,t) to the 3D incompressible Navier-Stokes equations for all time t > 0.

**Status (2026)**: Unsolved. $1M prize.

**What's known**:
- 2D: Global smooth solutions exist for all time (Ladyzhenskaya, 1960s)
- 3D: Local-in-time smooth solutions exist
- 3D: Global weak solutions (Leray, 1934) — not necessarily smooth
- 3D: Conditional regularity: if certain norms remain bounded, smooth solutions persist
- 3D: If a singularity forms, it must involve infinite velocity gradient

**Why it's hard**: The nonlinear term (**v**·∇)**v** can amplify vorticity through vortex stretching. The question is whether this amplification can outrun viscous diffusion to create a true singularity (infinite velocity in finite time). Numerical simulations suggest no — but simulations cannot prove regularity.

---

## Decision Cheat Sheet

| Situation | Solution/Approach |
|----------|-----------------|
| Steady viscous flow between parallel plates | Plane Couette (u = Uy/h) or Poiseuille (u ∝ y(h-y)) |
| Pressure drop in pipe | Hagen-Poiseuille: ΔP = 128μLQ/(πD⁴) |
| Drag on small sphere | Stokes: F = 6πμaU |
| Re << 1 (creeping flow) | Stokes equations (linearize N-S) |
| Re >> 1 | Boundary layer theory + inviscid outer flow |
| Check if laminar in pipe | Re < 2300 |
| Check if viscosity matters | Compare viscous time L²/ν to flow time L/U |
| Scale model to real flow | Match Reynolds number |

---

## Common Confusion Points

**Dynamic μ vs kinematic ν viscosity**: μ is in the constitutive law (τ = μ du/dy). ν = μ/ρ appears in the dimensionless N-S and in Re. Air has larger ν than water even though μ_air < μ_water, because ρ_air << ρ_water.

**Poiseuille applies only to laminar flow**: For turbulent pipe flow (Re > 4000), the velocity profile is flatter and friction is described by the Darcy-Weisbach equation with a friction factor. Hagen-Poiseuille systematically underpredicts pressure drop in turbulent flow.

**Stokes flow is reversible**: The Stokes equations are linear and time-reversible. If you reverse the boundary conditions (run them backwards), the flow reverses exactly. This is why swimming microorganisms cannot use reciprocal motions (Scallop Theorem) — you need non-reciprocal strokes to move at low Re.

**The N-S equations are deterministic but turbulent flow is chaotic**: Turbulence is not random noise added to N-S — it is the fully deterministic solution to N-S in highly nonlinear regimes. The chaos arises from sensitivity to initial conditions (Lyapunov instability), not from stochasticity in the equations.
