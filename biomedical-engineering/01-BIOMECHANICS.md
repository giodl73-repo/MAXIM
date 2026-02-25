# Biomechanics — Mechanics of Biological Systems

## The Big Picture

Biomechanics applies continuum mechanics — the same stress/strain tensor formalism you know
from structural engineering — to biological materials. The difference: biological materials are
nonlinear, anisotropic, viscoelastic, heterogeneous, and alive (they remodel in response to load).

```
+---------------------------------------------------------------------+
|              BIOMECHANICS — LANDSCAPE                               |
+---------------------------------------------------------------------+
|                                                                     |
|  HARD TISSUE           SOFT TISSUE           WHOLE-BODY MOTION      |
|  MECHANICS             MECHANICS             ANALYSIS               |
|                                                                     |
|  Bone: cortical,       Cartilage: biphasic   Gait analysis          |
|  cancellous, Wolff     Tendon/ligament:       (force plates,        |
|  Implant fixation      toe/linear/failure     motion capture,       |
|  Stress shielding      Muscle: Hill model     inverse dynamics)     |
|  Fatigue, fracture     Viscoelasticity        EMG                   |
|                        (creep/relaxation)                           |
|       |                    |                    |                   |
|       +--------------------+--------------------+                   |
|                            |                                        |
|                            v                                        |
|               COMPUTATIONAL BIOMECHANICS                            |
|               Finite Element Analysis (FEA)                         |
|               CT/MRI -> mesh -> material assignment                 |
|               -> boundary conditions -> validation                  |
+---------------------------------------------------------------------+
```

---

## Bone Mechanics

### Structure

Bone is a hierarchical composite material. At the nano level: collagen fibrils (~40%,
provides toughness) + hydroxyapatite crystals (~60%, provides stiffness). At the micro
level: Haversian systems (osteons) in cortical bone; open trabecular lattice in cancellous bone.

```
  BONE STRUCTURAL HIERARCHY
  =========================

  Nano scale:
  [Collagen triple helix] + [Ca10(PO4)6(OH)2 crystals]
  -> 67nm periodic banding
  -> fiber-reinforced composite behavior

  Micro scale:
  CORTICAL BONE                    CANCELLOUS BONE
  +------------------+             +------------------+
  | Osteons (Havers- |             | Trabeculae       |
  | ian systems)     |             | (plate and rod   |
  | Lamellae around  |             | lattice ~30%     |
  | central canal    |             | volume fraction) |
  | Porosity: 5-10%  |             | Porosity: 70-90% |
  +------------------+             +------------------+
  Location: diaphysis (shaft)      Location: metaphysis,
  of long bones, cortex            vertebrae, femoral head

  Macro scale:
  Cortex (shell) + cancellous core + marrow cavity
```

### Mechanical Properties

```
  BONE MECHANICAL PROPERTIES
  ==========================

  Property              Cortical        Cancellous
  ------------------    --------        ----------
  Young's modulus       15-25 GPa       0.1-5 GPa
                        (longitudinal)  (density-dependent)
  Tensile strength      130-190 MPa     1-20 MPa
  Compressive strength  170-240 MPa     1-20 MPa
  Shear strength        65-70 MPa       ---
  Fracture toughness    2-12 MPa√m      0.1-0.8 MPa√m

  Anisotropy:
  - Cortical: stiffer and stronger along bone axis (longitudinal)
    than transverse — aligned with Haversian system orientation
  - Cancellous: orthotropic — stiffest along principal trabecular
    direction (aligned with habitual stress state per Wolff's law)

  Bridge to structural engineering:
  Cortical bone stiffness (~20 GPa) is between aluminum (~70 GPa)
  and PEEK (~4 GPa). It is NOT as stiff as steel (~200 GPa).
  This matters enormously for implant-bone stress transfer.
```

### Wolff's Law and Stress Shielding

Bone remodels to its habitual mechanical environment — Julius Wolff, 1892. The density and
orientation of trabeculae follow the principal stress trajectories.

```
  BONE REMODELING — WOLFF'S LAW
  =============================

  STIMULUS: strain energy density or strain rate
     |
     v
  MECHANOSENSING: osteocytes (embedded in bone matrix, connected
  via canalicular network, respond to fluid flow from strain)
     |
     v
  EFFECTOR CELLS:
  - Osteoblasts: bone formation (lay down osteoid -> mineralize)
  - Osteoclasts: bone resorption (dissolve mineral + matrix)
  - Osteocytes: mechanosensor and orchestrator
     |
     v
  NET EFFECT:
  High strain region -> net formation (bone added)
  Low strain region  -> net resorption (bone removed)
  Normal range       -> homeostasis

  STRESS SHIELDING (implant complication):
  +-----------------------------+
  |  Rigid implant (steel/Ti)   |
  |  carries most of the load   |
  |  -> adjacent bone sees      |
  |     reduced strain          |
  |  -> bone resorbs around     |
  |     the implant             |
  |  -> implant loosens         |
  +-----------------------------+
  Solution: match implant stiffness to bone (carbon fiber PEEK),
  or use porous implant surfaces that encourage ingrowth.
```

---

## Cartilage Mechanics — Biphasic Theory

Articular cartilage (hyaline cartilage at joint surfaces) has no blood supply and extremely
limited repair capacity. Its mechanical behavior is governed by the interaction between its
fluid phase and solid phase.

```
  CARTILAGE BIPHASIC MODEL (Mow, 1980)
  =====================================

  CARTILAGE = FLUID PHASE + SOLID PHASE

  Fluid phase (~80% by weight):
  - Water + dissolved ions
  - Pressurizes under compressive load
  - Carries the majority of load acutely (>90% in some models)
  - Exudes slowly through matrix (drag resistance)

  Solid phase (~20% by weight):
  - Collagen type II (tensile stiffness)
  - Proteoglycans (aggrecan) — negatively charged, attract Na+,
    create osmotic swelling pressure
  - Carries increasing proportion of load as fluid exudes

  VISCOELASTIC BEHAVIORS:

  CREEP:                           STRESS RELAXATION:
  Apply constant stress            Apply constant strain
       +------ stress constant      |
  disp.|     /------ creep          |      stress
       |    /  equilibrium         |     /
       |   /                        |    /  relaxes
       |  /                         |   /
       | /                          |  /
       |/                           | /
       +----------> time            +--> time

  Creep: fluid keeps exuding until equilibrium (pressure = 0)
  Stress relaxation: fluid redistributes, solid bears more load
  Both behaviors measured in indentation or confined compression.
```

---

## Muscle Mechanics — Hill Model

The Hill muscle model (A.V. Hill, 1938) represents muscle as three mechanical elements.
Still the dominant model for musculoskeletal simulation.

```
  HILL MUSCLE MODEL
  =================

         CE          SE
  F --[=====]---[///]--- F
              |
             [///]
              PE

  CE = Contractile Element (active, generates force)
  SE = Series Elastic Element (tendon + cross-bridge compliance)
  PE = Parallel Elastic Element (passive connective tissue)

  FORCE-VELOCITY RELATIONSHIP (CE only):
  Force
    ^
    |\ Fmax (isometric)
    | \
    |  \     Shortening side:
    |   \    faster shortening = less force
    |    \   F * (v + a) = constant (Hill's equation)
    |     \
    |      \____
    +-----------> velocity
    eccentric  0  concentric

  FORCE-LENGTH RELATIONSHIP:
  Force
    ^
    |     /\
    |    /  \
    |   /    \
    |  /      \
    | /        \
    |/          \____
    +-------------------> length
       optimal length (maximal thick-thin filament overlap)
  Below optimal: fewer cross-bridge interactions
  Above optimal: fewer cross-bridge interactions
  Passive force from PE increases at long lengths

  ACTIVE vs PASSIVE:
  Total force = Active (CE+SE) + Passive (PE)
  At rest: only passive force (if stretched beyond slack length)
  During activation: both contribute
```

---

## Gait Analysis

Gait analysis quantifies human locomotion. Clinical gait labs use:
1. Force plates (kinetics — ground reaction forces)
2. Motion capture (kinematics — joint angles)
3. Electromyography (muscle activation timing)

The combination enables inverse dynamics — computing net joint moments without directly
measuring internal forces.

```
  GAIT ANALYSIS PIPELINE
  ======================

  DATA COLLECTION
  +--------------+    +------------------+    +---------------+
  | Force Plates |    | Motion Capture   |    | EMG           |
  | Ground       |    | (Vicon, Qualisys)|    | Surface or    |
  | reaction     |    | Retroreflective  |    | fine-wire     |
  | force (GRF)  |    | markers on skin  |    | electrodes    |
  | 6-DOF: Fx,   |    | 3D position of   |    | Raw EMG ->    |
  | Fy, Fz,      |    | markers at 100Hz |    | envelope ->   |
  | Mx, My, Mz   |    |                  |    | timing        |
  +--------------+    +------------------+    +---------------+
        |                     |
        v                     v
  INVERSE KINEMATICS         SEGMENT KINEMATICS
  Marker positions ->        Joint angles (hip, knee,
  body segment positions ->  ankle in 3 planes):
  joint center estimation    flexion/extension
  (functional or predictive) abduction/adduction
                             internal/external rotation
        |                     |
        +----------+----------+
                   |
                   v
          INVERSE DYNAMICS
          Newton-Euler equations applied
          distal to proximal (foot -> ankle -> knee -> hip)

          Net joint moment = I*alpha - F*d
          (inertial term - external force contribution)

          Outputs: Net joint moments (Nm) and joint powers (W)
                   "Net" = combined effect of all muscles crossing joint
```

### Gait Cycle Terminology

```
  GAIT CYCLE (one full cycle = heel strike to heel strike, same foot)
  ===================================================================

  STANCE PHASE (60%):                SWING PHASE (40%):
  Initial contact (heel strike)      Toe-off -> heel strike
  Loading response                   Foot clears ground
  Mid stance (single limb support)   Foot advances forward
  Terminal stance
  Pre-swing (push-off)

  Ground reaction force (normal walking):
  Force
    ^  1.2 BW         BW = body weight
    |  /\    /\
    | /  \  /  \
    |/    \/    \
    +------------> % gait cycle
    0%  IC  50%  60%  TO
    (IC = Initial Contact, TO = Toe Off)
  First peak: loading response (braking)
  Valley: mid-stance (center of mass at highest point)
  Second peak: push-off (propulsion)
```

---

## Fracture Mechanics and Fatigue

### Fracture Toughness

Fracture mechanics uses linear elastic fracture mechanics (LEFM) for brittle materials like
cortical bone. For ductile metals (implants), elastic-plastic fracture mechanics (EPFM).

```
  FRACTURE MECHANICS IN BIOMECHANICS
  ===================================

  Stress intensity factor:
  K = sigma * sqrt(pi * a) * F(geometry)

  Where:
  sigma = applied stress
  a = crack half-length
  F = geometry correction factor

  Critical: when K >= KIC (fracture toughness), crack propagates

  Material          KIC (MPa√m)   Notes
  --------          -----------   -----
  Cortical bone     2-12          Anisotropic; higher longitudinal
  PMMA bone cement  1-2           Low -> fatigue concerns
  Ti-6Al-4V         55-115        High -> good implant choice
  Co-Cr alloy       ~100          Good for fatigue
  Cortical bone     2-12          Much lower than metals
```

### Fatigue (S-N Curves)

```
  BONE FATIGUE (S-N CURVE)
  ========================

  Stress
  (MPa)  |
    200  |*
         | *
    150  |   *
         |     *
    100  |       * *
         |           * *
     50  |               * * *
         +----------------------------> Cycles (N)
         10^3  10^4  10^5  10^6  10^7

  Bone endurance limit: ~60-80 MPa (vs. bone UTS ~170 MPa)
  Note: bone REPAIRS fatigue damage during rest (remodeling)
  When damage accumulation > repair rate: stress fracture

  IMPLANT FATIGUE (clinical failure mode):
  - Cyclic loading at stress concentrations (screw holes, notches)
  - Ti-6Al-4V: better fatigue resistance than stainless steel
  - CoCrMo: best fatigue resistance among common implant metals
  - Surface finish critical: rough surfaces nucleate fatigue cracks
  - Fretting at modular junctions: micro-motion + corrosion
```

---

## Computational Biomechanics — FEA

Finite element analysis in biomechanics follows the same mathematics as structural FEA, but
material models are far more complex.

```
  FEA WORKFLOW FOR BONE/IMPLANT SYSTEM
  =====================================

  1. IMAGE ACQUISITION
     CT scan (for bone geometry + density)
     MRI (for soft tissue geometry)
     Resolution: 0.5-1mm voxels typical

  2. SEGMENTATION
     Threshold CT by Hounsfield units:
     Air: -1000 HU  ->  not bone
     Fat: -100 HU   ->  not bone
     Water: 0 HU    ->  not bone
     Soft tissue: 20-80 HU -> not bone
     Cortical bone: >700 HU -> bone
     Use: ITK-SNAP, 3D Slicer, Mimics

  3. MESH GENERATION
     Surface -> tetrahedral or hexahedral volume mesh
     Element size: 1-3mm (convergence study required)
     Implant: CAD geometry meshed separately

  4. MATERIAL ASSIGNMENT
     Cortical bone: linear elastic, orthotropic
     E_longitudinal ~20 GPa, E_transverse ~12 GPa
     Cancellous: density-dependent (empirical equations)
     E = a * rho^b (power law from Hounsfield units)
     Implant metals: isotropic linear elastic (simpler)

  5. BOUNDARY CONDITIONS
     Applied loads (from gait analysis)
     Constraints (periosteum, ligaments, joint contact)
     Contact interfaces (bone-implant: bonded or frictional)

  6. SOLVE
     Linear static for stiffness/stress distribution
     Nonlinear for large deformation, contact, plasticity

  7. POST-PROCESSING
     Von Mises stress (implant failure prediction)
     Principal strains (bone remodeling stimulus)
     Interface stress (fixation integrity)

  8. VALIDATION
     Compare to in vitro experiments (strain gauges,
     photoelastic models, digital image correlation)
     Sensitivity analysis: how much do results change
     with +/-20% material property uncertainty?
```

---

## Common Confusion Points

**Stiffness vs. strength**: Bone's Young's modulus (~20 GPa for cortical) is stiffness — how
much it deforms per unit stress. Bone's yield strength (~130 MPa) is when permanent damage
begins. Fracture toughness (~5 MPa√m) is how resistant it is to crack propagation. They are
three different material properties describing three different failure modes.

**Viscoelasticity vs. pure elasticity**: Cartilage (and many soft tissues) is viscoelastic —
the stress-strain relationship is time-dependent and rate-dependent. A viscoelastic material
under a suddenly applied stress will creep over time even though stress is constant. A purely
elastic material would not. Most FEA analyses oversimplify by using elastic material models.

**Inverse kinematics vs. inverse dynamics**: Inverse kinematics converts marker positions to
joint angles (kinematics = position/velocity/acceleration, no forces). Inverse dynamics then
takes those kinematics plus force plate data to compute joint moments and forces. Both are
called "inverse" because you're working backward from measured outputs to infer internal
quantities.

**Net joint moment**: The net joint moment from inverse dynamics is NOT the force in any one
muscle. It is the resultant of all muscles, ligaments, and joint contact forces crossing that
joint. Decomposing this into individual muscle forces requires optimization (static
optimization or EMG-driven models) because it is indeterminate — more muscles than unknowns.

**Wolff's law in implant design**: Stress shielding is not just theoretical. Massive ingrowth
hip stems from the 1980s had well-documented proximal femoral bone loss on radiographs because
the stiff stem bypassed load to the distal femur. Modern implants use shorter stems, proximal
porous surfaces, and lower-modulus materials to reduce this.

---

## Decision Cheat Sheet

| I need to analyze... | Use this approach |
|---|---|
| Bone stiffness and strength | Linear elastic FEA with CT-derived material properties |
| Implant-bone stress transfer | Nonlinear contact FEA, validate with in vitro experiment |
| Cartilage in joint loading | Biphasic FEA (requires specialized code: FEBio, Abaqus UEL) |
| Muscle forces during activity | Musculoskeletal simulation (OpenSim, AnyBody) |
| Joint moments during gait | Inverse dynamics pipeline (Vicon Nexus, Visual3D) |
| Fracture risk in osteoporosis | QCT-based FEA, Vert-IQ, Bone Profiler |
| Implant fatigue life | S-N curve analysis, stress concentration factors |
| Bone remodeling around implant | Adaptive remodeling algorithm (Huiskes, Stanford remodeling) |
| 3D motion of joint in vivo | Fluoroscopy-based kinematics (RSA, biplane X-ray) |
