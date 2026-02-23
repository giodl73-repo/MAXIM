# 03 — Structural Analysis

## Matrix Stiffness Method, FEM, Dynamics

```
EVOLUTION OF STRUCTURAL ANALYSIS

Hand methods (1800s–1950s):   Slope-deflection, moment distribution (Hardy Cross)
Matrix methods (1960s–today): Direct stiffness → implemented in every FEA code
Computational FEM (1960s–):   General purpose — any geometry, material, loading
Nonlinear + dynamics:         Geometric nonlinearity, material nonlinearity, time history
```

**The direct stiffness method is the mathematical foundation of every structural software package
(SAP2000, ETABS, STAAD, ANSYS, ABAQUS, LS-DYNA).** Understanding it lets you interpret results
and know when your model is wrong.

---

## Degrees of Indeterminacy

```
Degree of Static Indeterminacy (DSI):
  2D frame: DSI = 3m + r − 3j    (m = members, r = reactions, j = joints)
  2D truss: DSI = m + r − 2j

DSI = 0:  statically determinate
DSI > 0:  statically indeterminate (DSI = number of redundants)
DSI < 0:  mechanism (unstable)

Degree of Kinematic Indeterminacy (DKI):
  Number of unknown joint displacements (DOF not restrained by BC)
  2D frame: up to 3 DOF per joint (Δx, Δy, θ)
  DKI drives size of stiffness matrix

Stiffness method: solves for DKI unknowns (displacements)
Force method: solves for DSI unknowns (forces)
```

---

## Matrix Stiffness Method (Direct Stiffness)

**Concept:** Write element stiffness equations, assemble into global system, apply BCs, solve.

```
Global system:
  [K] {d} = {F}

[K] = global stiffness matrix (assembled from element matrices)
{d} = vector of unknown nodal displacements (DOFs)
{F} = vector of applied loads (forces and moments)
```

### Truss Element Stiffness (2D)

```
Local coordinates (along member axis):
  k_local = (AE/L) × [1  −1]
                      [−1  1]

Transform to global (θ = angle from horizontal):
  T = [cos θ  sin θ   0      0   ]
      [0       0    cos θ  sin θ ]

  k_global = T^T k_local T   (4×4 matrix in global x,y)

Assembly: add each element's contribution to global [K] at its DOF locations
```

### Beam Element Stiffness (Euler-Bernoulli)

**4 DOFs per element:** v₁, θ₁ (left node), v₂, θ₂ (right node)

```
k_beam = (EI/L³) × [ 12    6L   -12    6L  ]
                    [  6L   4L²  -6L    2L² ]
                    [-12   -6L    12   -6L  ]
                    [  6L   2L²  -6L    4L² ]

Consistent load vector (UDL w):
  {f} = (wL/12) × {6L/L, 1, 6L/L, -1}  ← {6, L, 6, -L} times wL/12
  = {wL/2, wL²/12, wL/2, -wL²/12}
```

### Frame Element

Combines truss (axial) + beam (bending): 6 DOF per element (u₁,v₁,θ₁,u₂,v₂,θ₂).
Local 6×6 stiffness assembled from axial and bending sub-matrices.

### Assembly Procedure

```
1. Number all free DOFs (unconstrained)
2. For each element:
   a. Compute k_element in local coordinates
   b. Transform to global: k_global = T^T k T
   c. Add contributions to global K at corresponding DOF rows/columns
3. Apply boundary conditions (set DOF = 0 for supports)
4. Partition: [K_ff]{d_f} = {F_f} (free DOFs)
5. Solve: {d_f} = [K_ff]^{-1} {F_f}
6. Recover reactions: {F_r} = [K_rf]{d_f}
7. Recover element forces from element displacements
```

---

## Finite Element Method (FEM)

FEM generalizes the matrix stiffness method to arbitrary geometry and loading.

### Displacement-Based FEM

```
1. Discretize domain into elements (mesh)
2. Choose displacement field within element using shape functions N_i(x,y):
   u(x,y) = Σ N_i(x,y) u_i    (interpolated from nodal values)

3. Strain-displacement: ε = B u_e  where B = [∂N/∂x, ∂N/∂y, ...]

4. Stress-strain: σ = D ε = D B u_e   (D = elasticity matrix)

5. Element stiffness: k_e = ∫ B^T D B dV   (volume integral over element)

6. Consistent force: f_e = ∫ N^T b dV   (body force) + surface tractions

7. Assemble K = Σ k_e,  F = Σ f_e
8. Solve K d = F (applying BCs)
9. Post-process: strains → stresses at Gauss points
```

### Common Element Types

| Element | Geometry | DOF/node | Notes |
|---------|----------|----------|-------|
| CST (constant strain triangle) | 3-node triangle | 2 (u,v) | Simple, poor accuracy (constant strain) |
| LST (linear strain triangle) | 6-node triangle | 2 | Better accuracy |
| Q4 (bilinear quad) | 4-node quad | 2 | Standard 2D; shear locking in bending |
| Q8/Q9 (serendipity) | 8-node quad | 2 | Good general purpose 2D |
| T4 (linear tet) | 4-node tet | 3 (u,v,w) | Easy meshing, stiff, poor accuracy |
| T10 (quadratic tet) | 10-node tet | 3 | Preferred for 3D solid |
| H8 (linear hex) | 8-node brick | 3 | Preferred when mesh possible |
| H20 (quadratic hex) | 20-node brick | 3 | High accuracy 3D |

**Isoparametric formulation:** Same shape functions for geometry and displacement interpolation.
Natural coordinates (−1 to +1) → Jacobian maps to real coordinates.
Gauss quadrature for integration.

### Convergence and Mesh Quality

```
h-refinement: increase number of elements → smaller elements
p-refinement: increase polynomial order (shape function degree)
hp-refinement: both simultaneously → exponential convergence for smooth problems

Convergence indicators:
  - Mesh independence study: refine until results change < tolerance
  - Strain energy plot vs mesh size (should converge from below)
  - Stress jumps across element boundaries → need refinement in high-gradient zones

Ill-conditioned elements:
  - Skewed (large aspect ratio): condition number of K degrades
  - Nearly degenerate (very small angles): interpolation error
  - Jacobian determinant < 0: inverted element → always error
```

---

## Classical Methods for Indeterminate Structures

### Moment Distribution (Hardy Cross Method)

Iterative, excellent for hand analysis of continuous beams and non-sway frames.

```
Concepts:
  Distribution Factor (DF): proportion of unbalanced moment distributed to each member
    DF_ij = K_ij / ΣK_ij    K = stiffness = 4EI/L (far end fixed) or 3EI/L (far end pinned)

  Carry-over Factor (COF):
    = 0.5 for far end fixed
    = 0 for far end pinned or free

Algorithm:
  1. Lock all joints (compute fixed-end moments FEM from load tables)
  2. At each joint, compute unbalanced moment = ΣM_applied
  3. Distribute: ΔM_i = −DF_i × unbalanced
  4. Carry over: CM = COF × ΔM to far end
  5. Iterate until moments converge
  6. Final moment = initial FEM + Σ(distributed + carried-over moments)
```

---

## Structural Dynamics

### Single DOF (SDOF) Equation of Motion

```
mẍ + cẋ + kx = F(t)

m = mass, c = damping coefficient, k = stiffness

Natural frequency: ω_n = √(k/m)   [rad/s]    f_n = ω_n/(2π)   [Hz]
Damping ratio: ζ = c/(2mω_n) = c/(2√(km))

Underdamped response (ζ < 1, typical for structures: ζ ≈ 1–5%):
  x(t) = e^(−ζω_n t) [A cos(ω_d t) + B sin(ω_d t)] + x_particular
  ω_d = ω_n √(1−ζ²)   (damped natural frequency)
```

### Frequency Response Function (FRF)

```
Harmonic loading: F(t) = F₀ sin(ωt)
Steady-state response amplitude:
  X = (F₀/k) / √[(1−r²)² + (2ζr)²]
  r = ω/ω_n (frequency ratio)

Dynamic Amplification Factor (DAF): X/(F₀/k) = 1/√[(1−r²)² + (2ζr)²]
  r = 0:   DAF = 1 (static)
  r = 1:   DAF = 1/(2ζ) → RESONANCE (limited only by damping!)
  r >> 1:  DAF → 0 (isolation regime)
```

### Multi-DOF Modal Analysis

```
[M]{ẍ} + [C]{ẋ} + [K]{x} = {F(t)}

Free vibration (undamped):
  [K]φ = ω²[M]φ → eigenvalue problem
  Solutions: ω₁ < ω₂ < ... < ω_n (natural frequencies)
             φ₁, φ₂, ..., φ_n (mode shapes = eigenvectors)

Mode shapes orthogonal: φᵢᵀ[M]φⱼ = 0  (i≠j) — mass orthogonality
                         φᵢᵀ[K]φⱼ = 0  (i≠j) — stiffness orthogonality

Modal superposition: x(t) = Σ qᵢ(t) φᵢ
  → Decouples N coupled equations into N independent SDOF equations
```

### Seismic Analysis

**Response spectrum:** Plots maximum SDOF response vs natural period T = 2π/ω_n, for given damping ratio and ground motion record.

```
Base shear: V = S_a(T₁) × W / g × k_distribution_factor

where S_a(T₁) = spectral acceleration at fundamental period
      W = seismic weight (dead load + fraction live)

SRSS modal combination: V = √(Σ V_i²)  (acceptable when modes well-separated)
CQC combination: V = √(Σ_i Σ_j r_ij V_i V_j)  (more accurate when modes closely spaced)
```

---

## Influence Lines

An influence line for a response quantity (reaction, shear, moment at a point) shows how that quantity varies as a unit load traverses the structure.

```
Müller-Breslau principle:
  The influence line for a quantity Q is equal to the deflected shape
  of the structure when a unit virtual displacement is imposed at Q.

Applications:
  Maximum moment at midspan: place live loads over positive IL region
  Maximum shear at a section: separately find max +V and max -V load positions
  Moving loads: convolve load distribution with IL to find max response
```

---

## Common Confusion Points

**Local vs global stiffness:** Element stiffness matrix is in local (element) coordinates. Must transform before assembling into global stiffness. Forgetting the transformation is a classic FEM implementation error.

**Consistent vs lumped mass matrix:** Consistent mass from shape functions (full matrix). Lumped mass (diagonal) easier to invert but less accurate. For dynamic analysis, consistent is more accurate. Many codes offer both.

**Resonance = amplification = potential failure:** Machinery on structures: avoid ω_n within ±20% of forcing frequency. Bridges: check pedestrian (1–2 Hz), wind vortex shedding. Seismic: fundamental period determines spectral demand.

**FEM mesh refinement direction:** Refine where gradients are large (stress concentrations, corners, load application points). Uniform refinement is wasteful. Adaptive refinement is the state of the art.

**Mode shape normalization:** Mode shapes are unique in shape, not magnitude. Can be mass-normalized (φᵀMφ=1) or max-value-normalized (max component = 1). Don't compare magnitudes across normalizations.

---

## Decision Cheat Sheet

| Problem type | Method | Advantage |
|-------------|--------|---------|
| Simple indeterminate beam | Moment distribution | Fast hand calculation |
| Any frame or truss | Direct stiffness / FEM | Systematic, coded |
| 3D arbitrary geometry | 3D FEM (ANSYS, Abaqus) | No analytical solution exists |
| Earthquake analysis | Response spectrum (code) | Standard practice per ASCE 7 |
| Time history | Newmark-β integration | Non-uniform damping, nonlinear |
| Natural frequencies | Eigenvalue solve [K]φ = ω²[M]φ | LAPACK/ARPACK sparse solver |
| Influence lines (design) | Müller-Breslau principle | Visual, fast for standard structures |
| Mesh quality check | Jacobian, aspect ratio | Check before trusting results |
