# Continuum Mechanics and Governing Equations

## The Big Picture

Fluid dynamics is founded on the continuum hypothesis: treat the fluid as a continuous medium, ignoring molecular structure. This is valid when the Knudsen number Kn = λ/L (mean free path / characteristic length) is small, which holds for virtually all engineering flows. The governing equations are conservation laws — mass, momentum, energy — written in differential form. The material derivative is the key operator that connects spatial (Eulerian) descriptions to particle-following (Lagrangian) perspectives.

```
CONTINUUM MECHANICS — STRUCTURE
═══════════════════════════════════════════════════════════════════════════════

  KINEMATICS  (geometry of deformation — no forces yet)
  ┌──────────────────────────────────────────────────────────────────────┐
  │  Velocity field:  **v**(x, t)   Eulerian description               │
  │  Material derivative: D/Dt = ∂/∂t + **v**·∇                       │
  │  Strain rate tensor: e_{ij} = (1/2)(∂vᵢ/∂xⱼ + ∂vⱼ/∂xᵢ)          │
  │  Vorticity: **ω** = ∇ × **v**    (local rotation rate, 2ω)        │
  └──────────────────────────────────────────────────────────────────────┘
                              ↓
  CONSERVATION LAWS (continuum versions of F = ma)
  ┌──────────────────────────────────────────────────────────────────────┐
  │  Mass:       ∂ρ/∂t + ∇·(ρ**v**) = 0                               │
  │  Momentum:   ρ D**v**/Dt = ∇·σ + ρ**g**                           │
  │  Energy:     ρ De/Dt = σ:∇**v** − ∇·**q** + ρr                   │
  └──────────────────────────────────────────────────────────────────────┘
                              ↓
  CONSTITUTIVE RELATIONS (material-specific: what σ looks like)
  ┌──────────────────────────────────────────────────────────────────────┐
  │  Ideal fluid:    σ = −pI  (pressure only, no viscosity)            │
  │  Newtonian:      σ = −pI + μ(∇**v** + ∇**v**ᵀ) + λ(∇·**v**)I    │
  │  Non-Newtonian:  σ = σ(strain rate tensor) — various models        │
  └──────────────────────────────────────────────────────────────────────┘
```

---

## Eulerian vs Lagrangian Descriptions

**Eulerian** (field-based): Fix a point x in space; observe what passes through.
**Lagrangian** (particle-based): Follow a specific fluid parcel as it moves.

Both descriptions are equivalent — they describe the same physics from different perspectives.

```
COMPARISON:
  Eulerian:   velocity field **v**(x, t)   — snapshot at each space-time point
  Lagrangian: particle position X(a, t)   — track parcel initially at a
              velocity of parcel:  dX/dt = **v**(X, t)

  Eulerian streamline:  tangent to **v** at fixed t (flow visualization)
  Lagrangian pathline:  trajectory X(a, t) (what a particle actually does)
  Streakline:           locus of particles that passed through a point (dye)

  For STEADY flow: streamlines = pathlines = streaklines (all the same)
  For UNSTEADY flow: these are three different curves
```

---

## The Material Derivative

The most important operator in fluid mechanics:

    D/Dt = ∂/∂t + **v**·∇    (material derivative = "following the fluid")

**Physical meaning**: the rate of change of a quantity as seen by a fluid parcel moving with the flow.

    Df/Dt = ∂f/∂t + (v_x ∂f/∂x + v_y ∂f/∂y + v_z ∂f/∂z)
              ↑              ↑
         local change    convective change (fluid carries f with it)

**Newton's second law for a fluid parcel**:
    mass × acceleration = forces
    ρ(D**v**/Dt) = divergence of stress + body forces

The D/Dt form is the natural "Lagrangian" form; ∂/∂t + **v**·∇ is the "Eulerian" equivalent.

---

## Kinematics: Strain Rate and Vorticity

Decompose the velocity gradient tensor dv_i/dx_j into symmetric and antisymmetric parts — the standard Hermitian + skew-Hermitian splitting of any linear operator applied to the velocity gradient matrix:

    ∂vᵢ/∂xⱼ = eᵢⱼ + ωᵢⱼ

**Strain rate tensor** (symmetric part, actual deformation):

    eᵢⱼ = (1/2)(∂vᵢ/∂xⱼ + ∂vⱼ/∂xᵢ)

    e₁₁ = ∂u/∂x  (stretching in x)
    e₁₂ = (1/2)(∂u/∂y + ∂v/∂x)  (shear)

**Rotation tensor** (antisymmetric part, rigid rotation):

    ωᵢⱼ = (1/2)(∂vᵢ/∂xⱼ − ∂vⱼ/∂xᵢ)

The associated **vorticity vector**: **ω** = ∇ × **v** (with ω_k = −2ωᵢⱼ ε_{ijk})

**Vorticity meaning**: 2**ω** = ∇ × **v** = local angular velocity of the fluid element (twice, because of the tensor convention).

    Irrotational flow:  **ω** = 0  (∇ × **v** = 0)  → **v** = ∇φ (potential flow)

---

## Conservation of Mass — Continuity Equation

**Integral form** (Reynolds transport theorem):

    d/dt ∫∫∫_V ρ dV + ∯_{∂V} ρ**v**·dA = 0

**Differential form** (Gauss divergence theorem on integral form):

    ∂ρ/∂t + ∇·(ρ**v**) = 0

**Material derivative form**:

    Dρ/Dt + ρ∇·**v** = 0

**Incompressible flow** (Dρ/Dt = 0 for each parcel):

    ∇·**v** = 0    (solenoidal velocity field)

This means the divergence of velocity vanishes — no net volumetric expansion or compression. For incompressible flow, the velocity field is divergence-free.

---

## Conservation of Momentum — Euler and Navier-Stokes

**Cauchy's equation** (for any continuum):

    ρ D**v**/Dt = ∇·**σ** + ρ**f**

where **σ** is the Cauchy stress tensor and **f** is the body force per unit mass.

### Inviscid Fluid (Ideal Fluid, Euler Equations)

Stress tensor: **σ** = −pI (pressure only, no viscous stresses).

    ρ(∂**v**/∂t + (**v**·∇)**v**) = −∇p + ρ**g**    (Euler equations)
    ∇·**v** = 0  (incompressible)

### Newtonian Viscous Fluid

Stress tensor: **σ** = −pI + **τ** where

    τᵢⱼ = μ(∂vᵢ/∂xⱼ + ∂vⱼ/∂xᵢ) + λ(∇·**v**)δᵢⱼ = 2μeᵢⱼ + λ(∇·**v**)δᵢⱼ

For incompressible flow (∇·**v** = 0), the last term vanishes:

    **τ** = 2μ**e**    (viscous stress = 2μ × strain rate)

**Navier-Stokes equations** (incompressible):

    ρ(∂**v**/∂t + (**v**·∇)**v**) = −∇p + μ∇²**v** + ρ**g**
    ∇·**v** = 0

The Laplacian ∇²**v** arises because ∇·(2μ**e**) = μ∇²**v** (using incompressibility).

```
NAVIER-STOKES TERM BY TERM:
  ρ ∂**v**/∂t    = rate of change of momentum (local)
  ρ(**v**·∇)**v** = inertia: fluid carries its own momentum (NONLINEAR)
  −∇p            = pressure pushes fluid from high to low pressure
  μ∇²**v**       = viscosity diffuses momentum like heat diffusion
  ρ**g**         = gravity (or other body forces)
```

---

## Conservation of Energy

For a compressible fluid, energy conservation (per unit mass e = internal energy):

    ρ De/Dt = −p∇·**v** + Φ − ∇·**q** + ρr

where:
- −p∇·**v** = pressure work (pdV work)
- Φ = viscous dissipation = **τ**:∇**v** ≥ 0 (always positive — heat generated)
- **q** = heat flux = −k∇T (Fourier's law)
- r = volumetric heat source

**Total energy form** (e + v²/2 = internal + kinetic):

    ρ D/Dt(e + v²/2) = −∇·(p**v**) + ∇·(μ **v**·(∇**v**+∇**v**ᵀ)) − ∇·**q** + ρ**f**·**v**

For incompressible flow without heat transfer, the energy equation decouples from mass/momentum and only matters when temperature is needed.

---

## Reynolds Transport Theorem

The bridge between integral (volume) and differential (pointwise) conservation laws.

For any scalar quantity B per unit mass, let b = ρB:

    d/dt ∫∫∫_{V(t)} ρB dV = ∫∫∫_{V(t)} ρ(DB/Dt) dV

For a fixed control volume V:

    d/dt ∫∫∫_V ρB dV = ∫∫∫_V ∂(ρB)/∂t dV + ∯_{∂V} ρB(**v**·**n**) dA

**Physical meaning**: Rate of change of B in a fixed volume = rate of change *inside* + flux of B *through the boundary*.

This is the basis for all CFD control-volume formulations. Each cell in a finite-volume mesh is a "fixed control volume," and fluxes through faces are computed and summed.

---

## Vorticity Equation

Taking the curl of the Navier-Stokes equations:

    D**ω**/Dt = (**ω**·∇)**v** + ν∇²**ω** + ∇ρ × ∇p / ρ²

Term by term:
- D**ω**/Dt = material derivative of vorticity (vorticity of each parcel)
- (**ω**·∇)**v** = **vortex stretching** (most important 3D term)
- ν∇²**ω** = viscous diffusion of vorticity
- ∇ρ × ∇p / ρ² = baroclinic term (creates vorticity in stratified flows)

**Vortex stretching** is the key mechanism in turbulence: when a vortex tube is stretched (by strain in the velocity field), its vorticity intensifies (angular momentum conservation). This is how turbulence cascades to small scales.

**In 2D**: The (ω·∇)v term vanishes (vorticity is perpendicular to the 2D plane, **v** has no component in that direction). So 2D flows have no vortex stretching → turbulence is qualitatively different in 2D (energy cascades upward to large scales, not downward).

---

## Boundary Conditions

```
COMMON BOUNDARY CONDITIONS:

  No-slip (solid wall):          **v** = **v**_wall   (viscous flows)
  Free-slip (inviscid):          **v**·**n** = 0  (normal velocity matches)
                                  no constraint on tangential velocity
  Outflow / far-field:           **v** → **v**_∞  (uniform stream)
  Symmetry plane:                **v**·**n** = 0  (like free-slip)
  Interface (two fluids):        velocity continuity + stress balance
                                  with surface tension: [p] = γκ
```

The no-slip condition at solid walls is the origin of boundary layers. In ideal (inviscid) flow, the fluid can slip past walls — which gives wrong predictions for drag but useful ones for lift.

---

## Decision Cheat Sheet

| Need to... | Use |
|-----------|-----|
| Track a fluid parcel | Material derivative D/Dt |
| Write mass balance | Continuity: ∂ρ/∂t + ∇·(ρ**v**) = 0 |
| Check incompressibility | ∇·**v** = 0 |
| Find vorticity | **ω** = ∇ × **v** |
| Check irrotationality | **ω** = 0 → potential flow φ exists |
| Write inviscid momentum | Euler: ρ D**v**/Dt = −∇p + ρ**g** |
| Write viscous momentum | Navier-Stokes: +μ∇²**v** |
| Derive field from integral form | Reynolds transport theorem + divergence |
| Track vorticity evolution | Vorticity equation with stretching term |

---

## Common Confusion Points

**Eulerian vs Lagrangian derivatives**: ∂f/∂t is the rate of change at a *fixed point in space*. Df/Dt is the rate of change *following a fluid parcel*. For a steadily flowing river, the temperature at a fixed point (Eulerian) is constant, but a water parcel moving through may experience temperature changes (Lagrangian).

**Incompressibility ≠ ∇·**v** = 0 always**: ∇·**v** = 0 is the incompressibility condition for each fluid parcel conserving volume (Dρ/Dt = 0). A flow can have non-uniform density and still be incompressible (e.g., stratified ocean). The condition is on the divergence of velocity, not on whether density varies spatially.

**Viscous stress tensor vs stress tensor**: τᵢⱼ is the viscous stress (deviatoric part). The full Cauchy stress σᵢⱼ = −pδᵢⱼ + τᵢⱼ includes the pressure. The pressure is isotropic (same in all directions); viscous stress is anisotropic (depends on velocity gradients).

**Vorticity ≠ angular velocity**: Vorticity ω = ∇ × **v** equals twice the local angular velocity of the fluid element. A solid-body rotation with angular velocity Ω has vorticity 2Ω everywhere. Potential vortex flow (swirling but irrotational except at the axis) has zero vorticity outside the core.
