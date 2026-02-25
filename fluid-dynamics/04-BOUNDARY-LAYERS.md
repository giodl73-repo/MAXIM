# Boundary Layer Theory

## The Big Picture

Prandtl's 1904 boundary layer theory resolved the D'Alembert paradox and revolutionized fluid mechanics. The key idea: at high Reynolds number, viscosity matters only in a thin layer near solid surfaces. Outside this layer, the flow is well approximated by inviscid (potential flow) theory. Inside, the full Navier-Stokes equations simplify dramatically because the layer is thin. This matched asymptotics approach — separate the flow into an outer inviscid region and an inner viscous layer, then match them — is one of the most powerful techniques in applied mathematics.

```
BOUNDARY LAYER STRUCTURE
═══════════════════════════════════════════════════════════════════════════════

  HIGH Re FLOW OVER A FLAT PLATE:

  ────────────────────────────────────────────────────────────────── ← U∞ (outer flow, ≈ inviscid)
                              edge of boundary layer (δ)
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ╔══════════════════════════════════════════════════╗ ← δ(x) growing
  ║  viscous boundary layer  u: 0 → U∞ over δ       ║
  ╚══════════════════════════════════════════════════╝
  ───────────────────────────────────── wall (u = 0)

  PARAMETER SCALES:
  x: streamwise, 0 to L              (long)
  y: wall-normal, 0 to δ             (short)
  δ/L ~ 1/√Re    (boundary layer is thin at high Re)
  Re_L = U∞L/ν
```

---

## Prandtl's Boundary Layer Equations

**Physical argument for simplification**:

At high Re, two regions:
1. Outer flow: inviscid, governed by Euler equations
2. Inner thin layer (δ << L): viscous effects comparable to inertia

**Scaling analysis**: In the boundary layer:
- x-scale: L (streamwise)
- y-scale: δ ~ L/√Re_L (wall-normal)
- u-scale: U∞ (streamwise velocity)
- v-scale: U∞(δ/L) ~ U∞/√Re (wall-normal velocity, small)

The full N-S x-momentum equation becomes, after dropping terms O(1/Re):

    **Prandtl boundary layer equations:**

    u ∂u/∂x + v ∂u/∂y = U_e dU_e/dx + ν ∂²u/∂y²
    ∂u/∂x + ∂v/∂y = 0    (continuity)

    Boundary conditions:
    u = v = 0 at y = 0  (no-slip)
    u → U_e(x) as y → ∞  (matching outer flow)

where U_e(x) is the edge velocity from the outer (inviscid) solution.

**Key simplification**: Only ∂²u/∂y² survives in viscous terms (the thinness of the layer makes ∂²u/∂x² negligible). The pressure gradient ∂p/∂y ≈ 0 (pressure constant across the layer), so p(x) = p_e(x) from the outer flow.

---

## Blasius Solution — Flat Plate with Zero Pressure Gradient

For a flat plate (U_e = U∞ = const, so dU_e/dx = 0):

    u ∂u/∂x + v ∂u/∂y = ν ∂²u/∂y²

**Similarity solution**: Introduce similarity variable η = y√(U∞/νx) = y/δ(x)

Let u = U∞ f'(η) where f(η) is the **Blasius function**. The PDE reduces to the **Blasius ODE**:

    **2f''' + f f'' = 0**
    f(0) = 0,  f'(0) = 0  (no-slip)
    f'(∞) = 1             (matching outer flow)

This ODE has no closed-form solution — it must be solved numerically. Key results:

```
BLASIUS BOUNDARY LAYER:

  Boundary layer thickness:  δ₉₉ ≈ 5x/√Re_x  (where u = 0.99 U∞)
  Displacement thickness:    δ* = 1.72x/√Re_x
  Momentum thickness:        θ = 0.664x/√Re_x
  Wall shear stress:         τ_w = 0.332 ρU∞² / √Re_x
  Skin friction coefficient: C_f = 0.664 / √Re_x

  Where Re_x = U∞x/ν  (local Reynolds number based on x)
```

**Physical meaning of thicknesses**:

    Displacement thickness δ* = ∫_0^∞ (1 − u/U∞) dy
    (volume flow deficit compared to ideal — shifts outer flow outward)

    Momentum thickness θ = ∫_0^∞ (u/U∞)(1 − u/U∞) dy
    (momentum deficit — controls drag)

---

## Von Kármán Momentum Integral

The von Kármán equation avoids solving the full BL equations — it integrates across the boundary layer to give a single ODE for θ(x):

    τ_w/(ρU_e²) = dθ/dx + (2θ + δ*)/U_e · dU_e/dx

For flat plate (dU_e/dx = 0):

    τ_w = ρU_e² dθ/dx    ⟹   θ(x) = √(0.664νx/U_e)  (matches Blasius)

The von Kármán equation works for **any assumed velocity profile** — plug in a family of profiles (polynomial, exponential, etc.) and solve for θ(x). This is the **integral method** for boundary layers.

---

## Pressure Gradient Effects

The pressure gradient dU_e/dx (from the outer flow) critically affects boundary layer behavior.

### Favorable Pressure Gradient (dU_e/dx > 0, dp/dx < 0)

Flow accelerates. Boundary layer stays thin. Flow remains attached.
Example: converging channel, leading edge of airfoil.

### Adverse Pressure Gradient (dU_e/dx < 0, dp/dx > 0)

Flow decelerates. Boundary layer thickens. Can lead to separation.
Example: diverging channel, rear of airfoil, after maximum thickness.

```
VELOCITY PROFILES WITH PRESSURE GRADIENT:

  No pressure gradient (flat plate):
    u/U_e →→→→→→→→→→→→  smooth S-curve

  Favorable:
    u/U_e →→→→→→→→  fuller, thinner layer

  Adverse:
    u/U_e →→→     inflection point in profile
                  S-shape less full

  Separation:
    u/U_e → (∂u/∂y)_wall = 0  at some x  →  SEPARATION POINT
             reverse flow downstream
```

**Separation criterion**: Separation occurs when the wall shear stress τ_w = μ(∂u/∂y)|_y=0 = 0.

---

## Boundary Layer Separation

**Separation** = the boundary layer detaches from the wall. Downstream of separation: reversed flow, recirculation zone, wake formation.

```
SEPARATION SEQUENCE:

  Attached BL:
  Wall → ↗↗↗↗↗↗↗↗↗ attached streamlines
         smooth flow

  At separation point (τ_w = 0):
  Wall → ↗↗↗↗↗↗→ horizontal at wall

  Separated:
  Wall → ↗↗↗↗↘↙↙↙ reversed flow (backflow near wall)
              ↑
           separation bubble
```

**Consequences of separation**:
- **Pressure drag (form drag)**: Separated wake has low pressure, creating net backward force
- **Stall**: Airfoil loses lift abruptly when separation covers the top surface
- **Flow unsteadiness**: Separated regions often oscillate (Kármán vortex street)

**Delaying separation**:
- Favorable pressure gradient (streamlined bodies)
- Turbulent boundary layer (transitions earlier but resists separation better)
- Surface suction (removes low-momentum fluid)
- Vortex generators (energize the BL with high-momentum fluid)

---

## Turbulent Boundary Layers

At Re_x > ~5×10⁵ (flat plate), the laminar boundary layer transitions to turbulent. Key differences:

```
LAMINAR vs TURBULENT BL:
  Feature               Laminar (Blasius)       Turbulent
  ────────────────────────────────────────────────────────
  Velocity profile      Smooth, S-shaped        Flatter, fuller
  BL thickness δ        ~5x/√Re_x               ~0.37x/Re_x^{1/5}
  Wall friction C_f     0.664/√Re_x             0.0592/Re_x^{1/5}
  Separation resistance Poor (adverse dp/dx)    Better
  Drag                  Lower                   Higher (more friction)
```

**Why turbulent BL resists separation better**: Turbulent mixing brings high-momentum fluid from the outer flow down to near the wall, "energizing" the layer. The fuller velocity profile can sustain a larger adverse pressure gradient before reversing.

**This is the golf ball dimple paradox**: Dimples trip the boundary layer to turbulence earlier. The turbulent BL stays attached longer around the ball → smaller wake → less pressure drag. Net result: dimpled golf ball travels ~2× farther than smooth.

---

## Log Law of the Wall

In turbulent boundary layers, the velocity profile near the wall obeys a universal **law of the wall**:

**Viscous sublayer** (y⁺ < 5):

    u⁺ = y⁺    (linear profile, dominated by viscosity)

**Log layer / overlap region** (30 < y⁺ < 300):

    u⁺ = (1/κ) ln(y⁺) + B ≈ 2.44 ln(y⁺) + 5.0

where:
- u⁺ = u/u_τ (velocity in wall units)
- y⁺ = y u_τ/ν (distance in wall units)
- u_τ = √(τ_w/ρ) (friction velocity)
- κ ≈ 0.41 (Kármán constant)
- B ≈ 5.0 (log-law constant)

```
TURBULENT BL STRUCTURE:
  y⁺ < 5      Viscous sublayer  (u⁺ = y⁺)
  5-30         Buffer layer     (transition)
  30-300       Log layer        (u⁺ = (1/κ)ln y⁺ + B)
  > 300        Outer layer      (wake region)
```

The log law is one of the most important empirical laws in turbulence — it is approximately universal (applies to all turbulent flows near smooth walls).

---

## Transition from Laminar to Turbulent

**Natural transition** (flat plate, Re_x ~ 5×10⁵):
1. Tollmien-Schlichting waves grow in BL (linear stability)
2. Three-dimensional effects develop (secondary instability)
3. Turbulent spots form (lambda vortices)
4. Spots spread and merge → fully turbulent

**Bypass transition** (rough walls, high freestream turbulence): Skips the TS wave stage; much earlier transition.

**Relaminarization**: Flow can transition back to laminar under strong favorable pressure gradients (Re decreasing along flow). Unusual but documented.

---

## Kármán Vortex Street

Flow past a circular cylinder at Re ~ 40–200:

```
KÁRMÁN VORTEX STREET:

  →→ CYLINDER →→
         → vortex formed top, sheds clockwise
         → then vortex formed bottom, sheds counterclockwise
         → alternating pattern downstream
  ○○○○○  ⊙ ○ ⊙ ○ ⊙ ← periodic shedding

  Shedding frequency: St = fD/U∞ ≈ 0.2  (Strouhal number)

  Famous failure: Tacoma Narrows Bridge (1940) — resonance with K.V.S.
```

**Strouhal number** St = fD/U∞ characterizes oscillatory flows. St ≈ 0.2 is universal for circular cylinders over Re = 100 to 10⁶.

---

## Decision Cheat Sheet

| Need to... | Use |
|-----------|-----|
| Estimate boundary layer thickness | δ ≈ 5x/√Re_x (Blasius, flat plate, laminar) |
| Estimate skin friction | C_f = 0.664/√Re_x (laminar), 0.0592/Re_x^{1/5} (turbulent) |
| Find when separation occurs | Adverse dp/dx → τ_w = 0 → separation |
| Compute integrated drag | Von Kármán integral: D = ρU_e² θ(L) |
| Know turbulent BL structure | Three layers: sublayer, buffer, log |
| Estimate transition location | Re_x ~ 5×10⁵ (natural, flat plate) |
| Predict vortex shedding frequency | St = fD/U ≈ 0.2 (circular cylinder) |

---

## Common Confusion Points

**Boundary layer thickness is not where u = 0**: The BL thickness δ₉₉ is conventionally defined where u = 0.99 U_e. The velocity asymptotically approaches U_e — there's no sharp edge. The δ₉₉ is just a practical definition.

**Turbulent BL has higher skin friction but resists separation**: This seems contradictory. Turbulent BL generates more drag (friction) per unit area, but it can stay attached on curved surfaces where laminar BL would separate. For streamlined bodies (e.g., airfoils at small angle of attack), laminar BL gives less total drag. For bluff bodies, turbulent BL gives less drag (because pressure drag from wake is reduced). The golf ball exploits this.

**Separation is not necessarily catastrophic**: At low Re, separated flow reattaches downstream (laminar separation bubble). At high Re or large angles of attack, full separation occurs (stall). A small separation bubble actually triggers transition to turbulent BL, which then reattaches.

**The law of the wall uses wall units (y⁺), not y in meters**: y⁺ = yu_τ/ν is a Reynolds-number-scaled wall coordinate. At high Re, the log layer extends over a larger range of physical y, but the y⁺ range (30–300) is universal.
