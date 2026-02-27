# 01 — Engineering Statics

## Equilibrium, Free Bodies, Trusses, Frames, Distributed Loads

```
THE STATICS WORKFLOW

 IDENTIFY            DRAW FBD           APPLY                SOLVE
 the body     →      (isolate body,  →  ΣF = 0,         →   for unknowns
 of interest        show all forces     ΣM = 0               (reactions,
                    and moments)                               member forces)
```

Statics is the foundation — the FBD is the interface contract between structural components.
Get the free body diagram wrong, everything downstream is wrong. The core structural
question is not force balance (which you know) but **determinacy**: does equilibrium
alone suffice, or do you need compatibility equations?

---

## Equilibrium and Determinacy

```
2D (planar):                    3D (general):
  ΣFx = 0                         ΣFx = 0,  ΣFy = 0,  ΣFz = 0
  ΣFy = 0        (3 equations)     ΣMx = 0,  ΣMy = 0,  ΣMz = 0   (6 equations)
  ΣM_A = 0

2D determinacy:
  r = number of unknown reactions
  r = 3: statically determinate
  r < 3: mechanism (unstable)
  r > 3: statically indeterminate (degree = r − 3)
```

---

## Support Conditions and Reactions

### 2D Supports

```
Support type     Reactions provided    Schematic     Unknown count
──────────────────────────────────────────────────────────────────
Pin (hinge)      Fx, Fy (2 forces)     △             2
Roller           Fy only (1 force)     ○─             1
Fixed            Fx, Fy, M (2F+1M)    ─┤             3
Link/cable       1 force along link    ──○             1

Rule of thumb: total reactions must = 3 (2D determinate) or 6 (3D determinate)
```

### 3D Supports

| Support | Reactions | DOF constrained |
|---------|-----------|----------------|
| Ball and socket | Fx, Fy, Fz | 3 forces |
| Journal bearing | Two of three forces | 2 forces (allows rotation on axis) |
| Fixed wall | Fx, Fy, Fz, Mx, My, Mz | All 6 |
| Smooth surface | Normal force only | 1 |

---

## Distributed Forces

### Uniformly Distributed Load (UDL)

```
  w [N/m]
  ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓
  ─────────────────────
  A                    B
  |←──────  L  ────────→|

Resultant: F_R = w × L  (total load)
Acts at centroid: x̄ = L/2  (mid-span for UDL)
```

### Triangularly Distributed Load

```
  Intensity: 0 at A, w₀ at B
  F_R = ½ w₀ L   (acts at x = 2L/3 from A, toward the larger end)
```

### General Distributed Load

```
F_R = ∫₀^L w(x) dx        (area under load diagram)
x̄ = ∫₀^L x w(x) dx / F_R   (centroid of area)
```

### Area Centroids (Common Shapes)

| Shape | Area | x̄ from left |
|-------|------|------------|
| Rectangle (b × h) | bh | b/2 |
| Right triangle (base b) | bh/2 | 2b/3 from vertex, b/3 from base |
| Semicircle (r) | πr²/2 | 4r/(3π) from diameter |
| Parabola (concave up) | 2bh/3 | 3b/8 from curved side |

---

## Centroids and Area Moments of Inertia

### Composite Method

```
For composite shapes, divide into simple parts:
  x̄ = Σ(A_i × x̄_i) / ΣA_i
  ȳ = Σ(A_i × ȳ_i) / ΣA_i

For holes (voids): use negative areas
```

### Area Moment of Inertia (Second Moment of Area)

Critical for beam bending (σ = My/I) and column buckling (P_cr = π²EI/L²).

```
I_x = ∫ y² dA    (about x-axis)
I_y = ∫ x² dA    (about y-axis)
J = I_x + I_y    (polar moment, for torsion)

Common values:
  Rectangle (b wide, h tall): Ix = bh³/12 (centroidal), bh³/3 (base)
  Circle (radius r):          Ix = Iy = πr⁴/4,  J = πr⁴/2
  Hollow circle:              Ix = π(r_o⁴ − r_i⁴)/4

Parallel axis theorem:
  I = Ī + A d²
  where Ī = centroidal moment of inertia, d = distance between axes
```

---

## Truss Analysis

A truss: two-force members connected at pinned joints; loads applied only at joints.
All members carry axial forces only (no bending, no shear in members).

**Determinacy (2D truss):**
```
m + r = 2j   → statically determinate
m = members, r = reactions, j = joints
m + r < 2j   → mechanism (unstable)
m + r > 2j   → statically indeterminate
```

### Method of Joints

Solve joint by joint, starting at joints with 2 unknowns.
```
At each joint: ΣFx = 0, ΣFy = 0
Convention: assume member in TENSION (positive = tension, negative = compression)

Procedure:
1. Find support reactions from overall FBD
2. Start at a joint with only 2 unknown member forces
3. Apply equilibrium → solve 2 unknowns
4. Move to adjacent joint, repeat
```

**Zero-force members** (by inspection):
- If two non-collinear members meet at unloaded joint with no external load → both zero-force
- If three members at unloaded joint, two collinear → third member is zero-force

### Method of Sections

Cut the truss to expose member forces, use equilibrium on one side.
More efficient when you need only specific member forces.
```
Cut through ≤ 3 members → 3 unknowns → solvable with 3 equilibrium equations
Pick moment point at intersection of two unknowns → direct solution for third
```

---

## Frames and Machines

**Frames:** Rigid structures with at least one multi-force member (carries bending).
**Machines:** Movable, transform input forces/moments.

Analysis: disassemble into individual members, expose pin forces, solve each member FBD.
```
Key: at each pin, force on member A from pin = −(force on member B from pin)   [Newton's 3rd]
Sequence: identify two-force members first (simpler), then multi-force members
```

---

## Shear and Moment Diagrams

**Sign convention (standard):**
```
V positive: right section faces up (downward shear on right face)
M positive: beam bends concave up (sagging), tension on bottom fiber
```

**Differential relations:**
```
dV/dx = −w(x)     (shear changes at distributed load rate)
dM/dx = V(x)      (moment changes at shear rate)
```
**Integral relations:**
```
V₂ − V₁ = −∫w dx   (change in shear = negative area under load diagram)
M₂ − M₁ = ∫V dx    (change in moment = area under shear diagram)
```

**Procedure:**
1. Find support reactions
2. Start left end: V₀ = +R_A, M₀ = 0 (if free end)
3. Traverse beam left to right:
   - Concentrated force P downward: V drops by P
   - Concentrated moment M_applied: M jumps by M
   - Distributed load w: V changes as −∫w dx (linear if w = const)
4. Check: right end V = 0, M = 0 (if free end)

**Maximum moment occurs where V = 0** (or changes sign).

---

## Friction

**Coulomb friction model:**
```
Impending slip: F_f = μ_s N    (static friction coefficient)
Sliding:        F_f = μ_k N    (kinetic, μ_k < μ_s typically 0.75μ_s)

angle of friction: φ = arctan(μ)

Tipping vs sliding: Compare line of action of resultant — if it falls outside base → tip
```

**Belt/rope friction (Euler-Eytelwein):**
```
T₂/T₁ = e^(μβ)    β = angle of wrap (radians)
T₂ = tight side, T₁ = slack side
For V-belt: use μ' = μ/sin(α/2) where α = groove angle
```

**Wedge:** Applied to lifting heavy machines and machinery alignment.
Self-locking condition: φ_wedge < 2φ_friction → wedge won't slip back under load.

**Screw jack:**
```
Lifting torque:  M = r_mean × W × tan(λ + φ')
Lowering torque: M = r_mean × W × tan(φ' − λ)
Self-locking:    λ < φ'  (lead angle < friction angle)
```

---

## Virtual Work

**Principle of virtual work:** For a body in equilibrium, the total virtual work done by all
forces during any virtual displacement consistent with constraints = 0. This is the Euler-Lagrange equation of the total potential energy functional specialized to statics: delta Pi = 0 at equilibrium. The same variational principle, applied to continuous displacement fields rather than rigid-body virtual displacements, is the foundation of FEM — minimize Pi over the space of trial functions to get [K]{d}={F}.

```
δU = 0   (virtual work = 0 for equilibrium)

Useful for: finding one specific reaction/force without solving full system
Virtual displacement δ: consistent with constraints (don't violate supports)
```

**Application:** Machines, linkages — apply virtual displacement to input, compute output force.

---

## Common Confusion Points

**Free body diagram — one body at a time:** The most common error is including forces that act on an adjacent body, not the body being analyzed. Isolate one rigid body. Show ALL forces and moments acting on it from the environment (supports, other members).

**Moment arm = perpendicular distance:** M = F × d_perp, not F × r. The moment arm d is the perpendicular distance from the line of action of the force to the moment reference point.

**Zero-force member ≠ unnecessary member:** Zero-force members carry no load under the specified loading, but they provide stability (prevent mechanism formation) and carry load under other load cases.

**Method of sections — moment point selection:** Always choose a moment point at the intersection of the unknown forces you don't want to find. This eliminates them from the moment equation and gives a direct solution for the one you do want.

**Truss assumption validity:** Real gusset plates add moment capacity → real members carry some bending. The pinned joint assumption is acceptable for preliminary design; FEM analysis for final design.

---

## Decision Cheat Sheet

| Problem | Method | When |
|---------|--------|------|
| Find support reactions | Overall FBD equilibrium | Always first step |
| Find all truss member forces | Method of joints | Systematic, all members |
| Find specific truss member | Method of sections | Only 3 members cut |
| Frame with multi-force members | Disassemble into FBDs | Expose pin forces |
| Distributed load → resultant | Centroid of load area | Before applying eq. |
| Shear/moment diagram | Differential relations | Building block for MoM |
| Self-locking check | Compare λ vs φ | Screw, wedge, wedge brake |
