# Magnetohydrodynamics — When Fluid Meets Field

## The Big Picture

MHD is the physics of electrically conducting fluids — liquid metals, plasmas,
ionized gases — in the presence of electromagnetic fields. The fluid carries
the field, the field drives the fluid. They are inseparable.

```
+------------------------------------------------------------------------+
|                         MHD LANDSCAPE                                  |
|                                                                        |
|   MAXWELL'S EQUATIONS          NAVIER-STOKES EQUATION                  |
|   (EM field evolution)          (fluid momentum)                       |
|                                                                        |
|   ∂B/∂t = ∇×(v×B) + η∇²B       ρ Dv/Dt = -∇p + η_v∇²v + J×B            |
|   ─────────────────────         ────────────────────────────           |
|   induction equation             fluid + magnetic body force           |
|        ↑                ↗                             ↑                |
|        └── v moves B ──┘         J×B forces fluid ───┘                 |
|                                                                        |
|   COUPLED: fluid velocity changes B; B creates forces on fluid.        |
|   You cannot solve one without the other.                              |
|                                                                        |
|   KEY DIMENSIONLESS NUMBERS:                                           |
|   Rm = μ₀σvL   (magnetic Reynolds — advection vs diffusion of B)       |
|   Ha = BL√(σ/ν) (Hartmann — magnetic braking vs viscosity)             |
|   β  = 2μ₀p/B²  (plasma beta — thermal vs magnetic pressure)           |
+------------------------------------------------------------------------+
```

---

## Fluid Mechanics Essentials

MHD couples Maxwell to fluid dynamics. The fluid side in brief:

**Navier-Stokes equation** — momentum per unit volume for a viscous fluid:

```
         Dv              ∂v
  ρ  ───── = ρ ( ─── + v·∇v ) = -∇p + η_v ∇²v + f_body
         Dt              ∂t

  ρ = fluid density (kg/m³)
  v = fluid velocity field (m/s)
  p = pressure
  η_v = dynamic viscosity (Pa·s)
  f_body = external body force per unit volume
```

The left side is mass × acceleration (per unit volume).
The right side: pressure gradient + viscous diffusion + body forces.

In MHD, the body force is the **Lorentz force per unit volume**:

```
  f_body = J × B    (N/m³)
```

This couples the fluid to the EM field.

**Continuity** (mass conservation):

```
  ∂ρ/∂t + ∇·(ρv) = 0
```

For incompressible flow (liquid metals, low-speed plasmas): ∇·v = 0.

**Reynolds number** (purely hydrodynamic — inertia vs viscosity):

```
  Re = ρvL/η_v = vL/ν    (ν = kinematic viscosity = η_v/ρ)

  Re << 1: viscous flow (laminar, creeping)
  Re >> 1: inertial flow (turbulent)
```

---

## The MHD Equations

The full coupled system. In the **low magnetic Reynolds number** or
**low frequency** approximation (v << c, displacement current dropped):

**Maxwell subset**:

```
  ∇×B = μ₀J          (Ampere, no displacement current)
  ∇×E = -∂B/∂t       (Faraday)
  ∇·B = 0
```

**Generalized Ohm's law** for a moving conductor:

```
  J = σ(E + v×B)
```

The v×B term is critical: moving a conductor through B drives current,
just as in a generator. In a fluid, every fluid element is a moving conductor.

**Navier-Stokes with Lorentz force**:

```
  ρ Dv/Dt = -∇p + η_v∇²v + J×B
```

**These four equations form the MHD system.** B and v are the primary unknowns.
J and E are derived from B and v through Ampere and Ohm.

---

## The Induction Equation

Eliminate J and E to get a single equation for B as a function of v and B.

From Ohm's law:  E = J/σ - v×B

From Ampere:  J = (1/μ₀)∇×B, so J/σ = (1/μ₀σ)∇×B

Therefore:  E = (1/μ₀σ)∇×B - v×B

Substitute into Faraday (∂B/∂t = -∇×E):

```
  ∂B/∂t = ∇×(v×B) - ∇×((1/μ₀σ)∇×B)
```

Using the identity ∇×(∇×B) = -∇²B (since ∇·B = 0):

```
  ┌─────────────────────────────────────────────────────────┐
  │                                                         │
  │   ∂B/∂t  =  ∇×(v×B)  +  η∇²B                            │
  │              ─────────     ─────                        │
  │              advection   diffusion                      │
  │             (fluid carries B)  (B diffuses through fluid)│
  │                                                         │
  │   η = 1/(μ₀σ)   magnetic diffusivity (m²/s)             │
  │                                                         │
  └─────────────────────────────────────────────────────────┘
```

This is the **magnetic induction equation** — the MHD analog of the
vorticity transport equation in ordinary fluid dynamics.

Two competing effects:
- **Advection**: fluid motion stretches, bends, and carries B field lines
- **Diffusion**: resistivity (1/σ) allows B to diffuse through the fluid,
  smoothing out gradients. In a perfect conductor (σ → ∞), η → 0 — no diffusion.

---

## Magnetic Reynolds Number

The ratio of advection to diffusion:

```
         |∇×(v×B)|     vB/L        vL
  Rm  = ─────────── ~ ──────  = ──────  = μ₀σvL
          |η∇²B|       ηB/L²        η
```

```
  Rm >> 1:   IDEAL MHD — advection dominates
             B is "frozen into" the fluid (Alfvén's theorem)
             Field lines move with the fluid, can be stretched/twisted

  Rm << 1:   DIFFUSIVE MHD — diffusion dominates
             B diffuses quickly relative to flow
             External field barely perturbed by fluid motion

  Rm ~ 1:    Both effects comparable — complex dynamics
```

**Rm for real systems**:

```
  System                   σ (S/m)      v (m/s)    L (m)      Rm
  ─────────────────────────────────────────────────────────────────
  Mercury, lab MHD device  10⁶          0.1        0.1        ~0.01
  Liquid sodium (reactor)  10⁷          1          1          ~10
  Earth's liquid iron core 5×10⁵        10⁻³       3×10⁶      ~2000
  Solar convection zone    10³ (plasma)  10²        10⁸        ~10⁸
  Galactic disk (plasma)   —            10⁴        3×10²⁰     ~10²³
```

Laboratory liquid metal MHD: Rm << 1 — external field barely changed by flow.
Earth's core, stars, galaxies: Rm >> 1 — field frozen into, advected by fluid.

---

## Frozen Flux Theorem (Ideal MHD, Rm >> 1)

When η → 0 (perfect conductor, or Rm >> 1):

```
  ∂B/∂t = ∇×(v×B)    (diffusion term gone)
```

This has a remarkable consequence: **magnetic flux through any surface
moving with the fluid is constant**. Field lines are frozen into the fluid —
they move with it, are stretched by it, cannot diffuse through it.

```
  STRETCHING A FIELD LINE:

  Before:   ─────────────    uniform B
                 │fluid moves
                 ↓
  After:    ──────╱╱╱──────   B amplified where stretched
                             (same flux, smaller area → stronger B)
```

This is the operating principle of astrophysical **dynamos**: fluid motions
stretch and fold field lines, amplifying B. The Earth's core generates and
sustains its magnetic field this way.

**Magnetic reconnection**: in real fluids (Rm large but finite), field lines
from opposite directions can break and reconnect — releasing stored magnetic
energy explosively. Solar flares are magnetic reconnection events.
Reconnection drives auroras (solar wind reconnects with Earth's magnetosphere).

---

## Alfvén Waves

In ideal MHD, small perturbations about a uniform B₀ and stationary fluid
produce waves. Consider B = B₀ẑ + b (small), v = small perturbation:

Linearize the induction equation and Navier-Stokes (dropping pressure):

```
  ∂v/∂t = (B₀/μ₀ρ) ∂b/∂z
  ∂b/∂t = B₀ ∂v/∂z
```

This is the wave equation for both v and b, with wave speed:

```
  ┌──────────────────────┐
  │        B₀            │
  │  v_A = ─────────     │  ← ALFVÉN SPEED
  │        √(μ₀ρ)        │
  └──────────────────────┘
```

**Physical picture**: Alfvén waves are transverse waves propagating along B₀,
like waves on a magnetic string. The magnetic tension B²/μ₀ acts as the
restoring force; density ρ provides the inertia.

```
  STRING ANALOGY:

  Tension T, linear mass density μ_s:  wave speed = √(T/μ_s)
  Magnetic tension B²/μ₀, volume density ρ:  v_A = √(B²/μ₀ρ) = B/√(μ₀ρ)
```

**Alfvén speed for real fluids**:

```
  Liquid sodium, B = 1 T:   v_A = 1/√(4π×10⁻⁷ × 930) ≈ 27 m/s
  Solar corona, B = 10 G:   v_A ~ 1000 km/s
  Earth's core, B = 30 G:   v_A ~ 1 cm/s (very dense liquid iron)
```

**Three MHD wave modes** (compressible MHD):

```
  Alfvén wave (shear):     v_A             — transverse, incompressible
  Fast magnetosonic:       √(v_A² + c_s²)  — compressional
  Slow magnetosonic:       v_A c_s/v_fast  — compressional

  c_s = √(γp/ρ) = sound speed
```

Alfvén waves are detected in the solar wind, Earth's magnetosphere,
and laboratory plasmas. They are fundamental to space weather.

---

## MHD Force Balance — Magnetic Pressure and Tension

The J×B force can be decomposed using Ampere (J = ∇×B/μ₀):

```
  J×B = (1/μ₀)(∇×B)×B

  Using the vector identity:

       B²          B²
  = -∇────  +  ─── (B·∇)B
      2μ₀        μ₀
    ──────────   ─────────────
    magnetic      magnetic
    pressure      tension
    gradient      (along field lines)
```

**Magnetic pressure** p_B = B²/2μ₀ acts like gas pressure — pushes outward,
perpendicular to field lines.

**Magnetic tension** B²/μ₀ along field lines — curved field lines have a
restoring force that tries to straighten them, like rubber bands.

**Plasma beta**:

```
         2μ₀p         thermal pressure
  β  =  ──────  =  ────────────────────
           B²         magnetic pressure

  β << 1:  magnetically dominated — B controls everything (solar corona, tokamak edge)
  β >> 1:  thermally dominated — B is a small perturbation (stellar interior)
  β ~ 1:   comparable — neither dominates
```

**MHD equilibrium** (J×B = ∇p):

```
  ∇(p + B²/2μ₀) = (1/μ₀)(B·∇)B

  Plasma pressure + magnetic pressure is balanced by magnetic tension.
  This is the condition for a magnetically confined plasma.
```

---

## Hartmann Flow

Classic MHD problem: conducting fluid in a rectangular duct, uniform external
field B₀ perpendicular to the flow, electrodes on the walls.

**Hartmann number**:

```
        B₀ L
  Ha = ──────  √(σ/η_v)
          1

  L = half-channel width, σ = conductivity, η_v = dynamic viscosity
```

For Ha >> 1, the flow profile changes dramatically:

```
  ORDINARY FLOW (Ha = 0):        MHD FLOW (Ha >> 1):
  parabolic profile               flat "plug" profile

      ↑↑↑↑↑↑↑↑↑↑↑                  ↑↑↑↑↑↑↑↑↑↑↑
    ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑                ↑↑↑↑↑↑↑↑↑↑↑↑↑
   ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑               ↑↑↑↑↑↑↑↑↑↑↑↑↑↑
    ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑                ↑↑↑↑↑↑↑↑↑↑↑↑↑
      ↑↑↑↑↑↑↑↑↑↑↑               thin Hartmann layers
  (maximum at center)            at walls, flat core
```

**Physical mechanism**: fluid moving in B₀ has induced EMF v×B₀. This drives
current J across the duct. The J×B₀ force opposes the flow — magnetic braking.
The braking is strongest where v is largest (center), flattening the profile.

**Hartmann layers**: thin boundary layers at the walls parallel to B₀, thickness δ_Ha ~ L/Ha.
Most of the velocity gradient is confined here.

Hartmann flow is used in:
- Electromagnetic flowmeters (measure voltage induced by flow → determine velocity)
- MHD pumps (apply current across duct → J×B drives the fluid)
- Crystal growth from metallic melts (control flow with B to suppress turbulence)

---

## MHD Devices

### Electromagnetic Pump

No moving parts. Apply current J perpendicular to flow, external B perpendicular
to both. J×B Lorentz force pushes the liquid metal along the duct.

```
      B (external, into page)
      ⊗ ⊗ ⊗ ⊗ ⊗ ⊗

  +── ────────────── ──→ flow
  I   liquid metal
  -── ────────────── ──
      J: current across duct (top to bottom)
      J×B: force along duct (left to right) → pumping

  No shaft, no seal, no impeller. Zero contact with the fluid.
```

Applications:
- Liquid sodium cooling loops in fast breeder nuclear reactors
- Aluminum and zinc die casting (precise flow control)
- Steel strand casting (suppress turbulence in mold)
- Future: liquid metal blankets in fusion reactors

### MHD Generator

Run the pump backwards: force fluid to flow, extract electrical power.

```
  Conducting fluid flows at velocity v in external B (perpendicular).
  v×B drives charges → EMF across the duct → electrodes collect current.

  Open circuit voltage: V = BvL  (L = electrode separation)
  Short circuit current: I = σ(v×B)·A  (A = cross section area)
```

For hot ionized combustion gas (seeded with potassium to boost σ):
MHD generator extracts power at ~2000°C, before gas is cool enough for
a steam turbine. The exhaust still runs a conventional steam cycle.
Combined cycle: 60%+ efficiency vs ~40% for pure steam cycle.

---

## Plasma Confinement — Tokamak

Plasma (fully ionized gas, T ~ 10⁸ K for fusion) cannot touch any wall.
Solution: confine it magnetically — design B field so charged particles
are trapped.

**Charged particle motion in B field**: spirals along field lines.
If field lines close on themselves (torus), particles spiral in circles forever.

**Simple torus problem**: in a purely toroidal field, particles drift off the field
lines due to the gradient and curvature of B. A purely toroidal field doesn't work.

**Tokamak solution**: add a poloidal field by driving current through the plasma.
The combined helical field traces a path that stays inside the torus.

```
  TOKAMAK CROSS SECTION:

  Toroidal field coils (external): B wraps around the long way
  Plasma current (Ip): driven by transformer action → poloidal B
  Combined helical field: charged particles trace helical paths, staying confined

         ╭─────────╮
        ╱  plasma   ╲
       │   current→  │
        ╲           ╱
         ╰─────────╯
```

**MHD instabilities** — the challenge of fusion:

```
  Kink instability: plasma column bends like a kinked hose
  Sausage instability: plasma pinches off in places
  Ballooning mode: plasma bulges outward where B is weaker
  Disruption: sudden loss of confinement, plasma hits wall
```

MHD stability conditions (Kruskal-Shafranov, Troyon limits) constrain how much
plasma pressure can be confined for a given B field. Exceeding these limits
causes disruption. ITER (world's largest tokamak, in France) is designed to
produce 500 MW fusion power from 50 MW input.

---

**Computational MHD**: The MHD equations are notoriously hard to solve numerically. Key challenges: (1) maintaining div B = 0 — standard finite-difference schemes violate this constraint, requiring constrained transport (CT) or divergence cleaning (hyperbolic/parabolic schemes); (2) the CFL condition couples the timestep to the fastest wave (fast magnetosonic, which can be much faster than the fluid velocity), making explicit schemes expensive; (3) at low magnetic Reynolds number Rm, the resistive term eta * nabla^2 B is stiff, requiring implicit solvers. Common approaches: spectral methods (Fourier basis for periodic domains — standard in turbulence simulations), Godunov-type finite volume methods (HLLD Riemann solver for MHD — used in astrophysical codes like Athena++, PLUTO), and lattice Boltzmann methods (LBM with BGK collision operator, increasingly used for industrial MHD). The state of the art in 2025: global 3D dynamo simulations resolve ~10^9 grid cells, but even these are far from realistic parameters (Earth's Rm ~ 2000, Pm ~ 10^-6).

## Natural MHD — Dynamos and Space Weather

**Earth's magnetic field**: generated by convecting liquid iron in the outer core.
Rm ~ 2000 — strongly ideal, field frozen into fluid.
The Coriolis force (Earth's rotation) organizes convection columns,
which stretch and twist field lines — the geodynamo.
Field reverses every ~300,000 years (chaotic, not periodic).
Currently weakening and possibly heading toward a reversal.

**Solar dynamo**: differential rotation (equator rotates faster than poles)
stretches toroidal field from poloidal field (the Ω-effect).
Convective cyclonic motions regenerate poloidal from toroidal (the α-effect).
11-year sunspot cycle is the surface manifestation of the dynamo cycle.

**Solar wind MHD**: the Sun continuously ejects plasma at ~400 km/s.
The frozen-in solar magnetic field is dragged into interplanetary space,
forming the Parker spiral (rotating solar field + radially flowing plasma).
When it hits Earth's magnetosphere, reconnection drives auroras.

**Accretion disks**: gas falling onto black holes or neutron stars forms a disk.
MHD turbulence (magnetorotational instability — MRI) provides the viscosity
that allows angular momentum transport and accretion to proceed.
Without MRI, accretion disks wouldn't work — no viscosity mechanism existed
until Balbus & Hawley 1991.

---

**Magnetic helicity**: H = integral(A dot B) dV is a topologically conserved quantity in ideal MHD. It measures the linkage, twist, and writhe of magnetic field lines — the same linking number from topology (see `topology/`). In ideal MHD (eta = 0), H is exactly conserved; in resistive MHD, H decays much more slowly than magnetic energy (Taylor relaxation). Helicity conservation constrains dynamo dynamics: a dynamo can amplify magnetic energy but must conserve helicity, which forces the field into large-scale organized structures. In reconnection events (solar flares, magnetotail), helicity is approximately conserved even as field topology changes rapidly — the reconnection converts helicity between twist and writhe forms. This connects MHD to topological field theory: the Chern-Simons form integral(A wedge dA) is the mathematical generalization of magnetic helicity.

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| Key coupling force | J×B (Lorentz body force on fluid) |
| Key equation for B evolution | ∂B/∂t = ∇×(v×B) + η∇²B |
| High Rm behavior | Flux frozen into fluid |
| Low Rm behavior | B diffuses through fluid, barely perturbed |
| Characteristic wave speed | v_A = B/√(μ₀ρ) (Alfvén speed) |
| Magnetic pressure | p_B = B²/2μ₀ |
| Flow profile in strong B | Flat (Hartmann) — plug flow |
| Pump liquid metal with no moving parts | EM pump — J×B drives flow |
| Generate power with hot gas | MHD generator — v×B drives current |
| Confine hot plasma | Tokamak — helical B field |
| Earth's magnetic field source | MHD dynamo in liquid iron outer core |

---

## Common Confusion Points

**MHD is not just Maxwell applied to fluids — it's a coupled nonlinear system.**
You cannot solve for B ignoring v, or v ignoring B. They must be solved together.
The nonlinearity (v×B in Ohm's law, v·∇v in Navier-Stokes, J×B body force)
makes analytic solutions rare and exact numerical solutions expensive.

**Alfvén waves require a background field B₀.**
In zero B, there are no Alfvén waves. The wave speed v_A = B/√(μ₀ρ) depends
on the background field. As B → 0, v_A → 0 — the wave disappears.

**Electromagnetic pump efficiency is low.**
J×B pumping is simple but the currents flowing through the fluid generate I²R
heating. Efficiency is typically 30-60%. It is chosen for reliability and
no-moving-parts, not efficiency.

**Ideal MHD is not always a good approximation — even at high Rm.**
The frozen-flux theorem requires Rm → ∞ globally. At current sheets (thin regions
where field reverses), local Rm can be small even if global Rm is large.
Reconnection happens at these current sheets — a finite-resistivity effect
in an otherwise ideal MHD plasma. Treating plasma as perfectly ideal misses
all reconnection physics.

**Plasma β depends strongly on location and conditions.**
In a tokamak, β ~ 0.05 (strong magnetic field, moderate plasma pressure).
In the solar interior, β >> 1 (radiation pressure dominates). In the corona,
β << 1 (low-density, strong field). The same "plasma" concept spans β from
10⁻⁴ to 10⁴ in different astrophysical contexts.
