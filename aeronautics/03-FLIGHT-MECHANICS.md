# 03 — Flight Mechanics

## Equations of Motion, Stability, Control, Performance

---

## Big Picture: Flight Mechanics Stack

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         FLIGHT MECHANICS FRAMEWORK                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  REFERENCE FRAMES & KINEMATICS                                              │
│    Earth axes (NED/ECEF) → Body axes → Stability axes → Wind axes          │
│    Euler angles (φ,θ,ψ) ↔ Quaternions (q₀,q₁,q₂,q₃)                      │
│                              │                                              │
│                              ▼                                              │
│  6-DOF EQUATIONS OF MOTION (Newton-Euler)                                   │
│    Translational: m(V̇ + Ω × V) = F    [3 equations: X, Y, Z]              │
│    Rotational:    I·Ω̇ + Ω × (I·Ω) = M  [3 equations: L, M, N]            │
│                              │                                              │
│                              ▼                                              │
│  TRIM (EQUILIBRIUM) CONDITIONS                                              │
│    Level flight / Climb / Turn / Pull-out                                   │
│    All derivatives = 0; find δe, δa, δr, throttle for given flight state   │
│                              │                                              │
│                              ▼                                              │
│  STABILITY ANALYSIS                                                         │
│    Linearize about trim → A matrix → eigenvalues → modes                   │
│    Longitudinal: Phugoid (slow) + Short-period (fast)                       │
│    Lateral-directional: Roll + Spiral + Dutch roll                          │
│                              │                                              │
│                              ▼                                              │
│  CONTROL & HANDLING                                                         │
│    Conventional: elevator/aileron/rudder authority                          │
│    Fly-by-wire: envelope protection, carefree handling, quadruplex          │
│    Cooper-Harper HQR scale; MIL-HDBK-1797 Level 1/2/3                      │
│                              │                                              │
│                              ▼                                              │
│  PERFORMANCE                                                                │
│    V-n diagram → loads → climb/descent → range/endurance → T/O & landing   │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 1. Reference Frames and Coordinate Systems

```
REFERENCE FRAMES:
  Earth-centered inertial (ECI):     Origin at Earth center; fixed to stars
  Earth-centered Earth-fixed (ECEF): Origin at Earth center; rotates with Earth
  Local geodetic / NED:              North-East-Down at aircraft position;
                                     quasi-inertial for most flight mechanics
  Body axes (B):    Origin at CG; x_b forward, y_b right wing, z_b down
  Stability axes (S): x_s along freestream projection onto symmetry plane
                      (same as body for symmetric flight; used for linearization)
  Wind axes (W):    x_w along freestream V∞; z_w in symmetry plane → "wind axes"

ANGLE OF ATTACK (α) AND SIDESLIP (β):
  α = arctan(w/u)       u,w = body-axis velocities (longitudinal plane)
  β = arcsin(v/V)       v = body-axis lateral velocity
  V = √(u² + v² + w²)  = total airspeed

EULER ANGLES — body-frame orientation relative to NED:
  ψ = yaw   (heading)  — rotation about z_E (positive nose right)
  θ = pitch (elevation) — rotation about y₁ (positive nose up)
  φ = roll  (bank)     — rotation about x_B (positive right wing down)

  Convention: ZYX (yaw → pitch → roll); applies to right-hand coordinate system

  Rotation matrix (CNED→B = Rx(φ)·Ry(θ)·Rz(ψ)):
  ┌                                                                         ┐
  │  cos θ cos ψ          cos θ sin ψ         -sin θ                        │
  │  sin φ sin θ cos ψ   sin φ sin θ sin ψ   sin φ cos θ                   │
  │ -cos φ sin ψ        +cos φ cos ψ                                        │
  │  cos φ sin θ cos ψ   cos φ sin θ sin ψ   cos φ cos θ                   │
  │ +sin φ sin ψ        -sin φ cos ψ                                        │
  └                                                                         ┘

GIMBAL LOCK:
  At θ = ±90° (pitch straight up/down), φ and ψ become indistinguishable —
  singularity in Euler angle kinematics. Not a real physical constraint, just
  a coordinate pathology.

QUATERNIONS (q = [q₀, q₁, q₂, q₃] = [scalar, vector]):
  q₀² + q₁² + q₂² + q₃² = 1  (unit quaternion constraint)
  Encodes same info as rotation matrix but no singularity
  q̇ = ½ · Ξ(q) · ω    where ω = [p, q, r] (body angular rates)
  ┌        ┐   ┌                    ┐ ┌   ┐
  │ q̇₀    │   │  0  -p  -q  -r    │ │ q₀│
  │ q̇₁    │ = │  p   0   r  -q    │ │ q₁│
  │ q̇₂    │   │  q  -r   0   p    │ │ q₂│
  │ q̇₃    │   │  r   q  -p   0    │ │ q₃│
  └        ┘   └                    ┘ └   ┘
  Advantage: no singularity; computationally efficient; avoids quadrant issues
  Used in: flight simulation, inertial nav, IMUs, quaternion AHRS filters
  Cost: less intuitive; 4 parameters instead of 3 (constrained)
```

---

## 2. 6-DOF Equations of Motion

```
NEWTON-EULER RIGID BODY DYNAMICS:
  Forces F applied at CG → translational acceleration
  Moments M about CG → rotational acceleration

TRANSLATIONAL (in body axes):
  m(u̇ + qw - rv) = X  (x-axis: "axial force")
  m(v̇ + ru - pw) = Y  (y-axis: "side force")
  m(ẇ + pv - qu) = Z  (z-axis: "normal force")

  Where: p = roll rate, q = pitch rate, r = yaw rate (body angular rates)
  Cross terms (qw, rv, etc.) are Coriolis — body is rotating

ROTATIONAL (assuming constant inertia tensor Iᵢⱼ):
  Iₓₓṗ - Iₓᵤ(ṙ + pq) - (Iyy - Izz)qr = L  (roll moment)
  Iyyq̇ + (Iₓₓ - Izz)pr + Iₓᵤ(p² - r²)  = M  (pitch moment)
  Izzṙ - Iₓᵤ(ṗ - qr) - (Iₓₓ - Iyy)pq  = N  (yaw moment)

  Iₓᵤ = cross-inertia; for symmetric aircraft (xz-plane of symmetry): Iₓᵤ ≠ 0,
  but Iₓy = Iyz = 0

INERTIA TENSOR for typical aircraft (symmetric about xz-plane):
  ┌              ┐
  │ Iₓₓ   0  -Iₓᵤ│
  │  0   Iyy   0  │
  │-Iₓᵤ   0   Izz│
  └              ┘

FORCES AND MOMENTS (components):
  Aerodynamic: functions of (α, β, p, q, r, δe, δa, δr, Mach, h)
    Using dimensionless stability derivatives:
    L = q∞ · S · CL    CL(α, δe, q, α̇)
    D = q∞ · S · CD    CD(CL, Mach)
    Y = q∞ · S · CY    CY(β, p, r, δr)
    Pitching moment: M = q∞ · S · c̄ · Cm  (c̄ = mean aerodynamic chord)
    Rolling moment:  L = q∞ · S · b · Cl   (b = wing span)
    Yawing moment:   N = q∞ · S · b · Cn

  Gravity (in body axes):
    Xg = -mg sin θ
    Yg =  mg cos θ sin φ
    Zg =  mg cos θ cos φ

  Thrust: usually along body x-axis with engine offset and cant angle corrections

KINEMATIC EQUATIONS (Euler angle rates from body angular rates):
  φ̇ = p + (q sin φ + r cos φ) tan θ
  θ̇ = q cos φ - r sin φ
  ψ̇ = (q sin φ + r cos φ) / cos θ   ← singularity at θ = ±90°

POSITION UPDATE (in NED):
  ẋN =  u cos θ cos ψ + v(sin φ sin θ cos ψ - cos φ sin ψ) + ...
  ẋE =  (full transformation using CNED→B transpose) ...
  ẋD = -u sin θ + v cos θ sin φ + w cos θ cos φ

FULL STATE VECTOR:
  x = [u, v, w, p, q, r, φ, θ, ψ, xN, xE, h]    (12 states)
  Control: u_c = [δe, δa, δr, δT]                  (elevator, aileron, rudder, throttle)
```

---

## 3. Trim (Equilibrium)

```
TRIM DEFINITION:
  Steady flight: all state derivatives = 0 (or periodic for oscillatory trim)
  Find control inputs u_c and/or flight state such that ẋ = f(x, u_c) = 0

STRAIGHT-AND-LEVEL TRIM (symmetric flight, β=0, φ=0):
  u̇ = 0: T cos α = D + mg sin γ
  ẇ = 0: T sin α + L = mg cos γ    (γ = flight path angle)
  q̇ = 0: Cm(α, δe, q=0) = 0       ← find δe for pitch equilibrium
  Level: γ = 0 → L = W, T = D

  Trim speed: V_trim determined by W = q∞ · S · CL(α_trim)
  Trim angle of attack: varies with CG position

CLIMBING TRIM:
  γ > 0; T cos(α - γ) = D + W sin γ  (thrust inclined, provides some lift component)
  For small angles: T ≈ D + W sin γ   → excess thrust → climb
  Climb rate: RC = V∞ sin γ ≈ (T-D)V/W = P_excess / W

COORDINATED TURN (constant altitude, φ = bank angle):
  L cos φ = W → L = W / cos φ       load factor n = 1/cos φ
  Turn radius: R = V²/(g tan φ)
  Turn rate: ψ̇ = g tan φ / V
  Load factor: n = 1/cos φ → 30° bank: n=1.15; 60° bank: n=2.0; 80° bank: n=5.76

TRIM MAP (for flight control design):
  Trim conditions computed over entire flight envelope: altitude × Mach grid
  Forms basis for gain-scheduled control law
  At each trim point: find [α, δe, T] such that steady flight is achieved
```

---

## 4. Static Stability

```
DEFINITION:
  Statically stable: if disturbed, aerodynamic restoring moment acts to return to trim
  Statically unstable: disturbance generates diverging moment (→ needs FBW active stabilization)

LONGITUDINAL STATIC STABILITY:
  Criterion: ∂Cm/∂CL < 0   (pitch moment decreases as lift increases → restoring)

  Cm(α) = Cm₀ + Cm_α · α + Cm_δe · δe   where:
    Cm_α = (CL_α)_tail × η_t × (lt/c̄) × (St/S) × (1 - dε/dα) - (CL_α)_w × (xCG - xac)/c̄
    η_t = q_t/q∞ = tail efficiency ratio
    lt = tail moment arm; dε/dα = downwash gradient at tail

  NEUTRAL POINT (NP): CG location at which Cm_α = 0 (marginal stability)
    NP = xac + (CL_α)_tail × η_t × (lt/c̄) × (St/S) × (1 - dε/dα) / CL_α_total
    (in fractions of c̄ from leading edge)

  STATIC MARGIN (SM):
    SM = (x_NP - x_CG) / c̄   (positive SM → stable)
    Typical: airliners 5-15% c̄; fighters 0 to -5% (relaxed/unstable for agility)
    Too much SM → sluggish; too little → handling problems (needs FBW)
    Concorde had negative SM at supersonic — pure FBW aircraft

  STICK FORCE GRADIENT:
    dFs/dV > 0 required by FAR 25 (pull back → nose up → decelerate; intuitive)
    Stick-free vs stick-fixed neutral point differ due to floating elevator

LATERAL STATIC STABILITY (dihedral effect):
  Cl_β < 0: if sideslip to right (β > 0), rolling moment raises right wing → restoring
  Physical: wing dihedral angle Γ → β creates differential angle of attack
  Swept wings contribute Cl_β (sweepback stabilizes, forward sweep destabilizes)
  Too much Cl_β → Dutch roll oscillation (see §5)

DIRECTIONAL STATIC STABILITY (weathercock):
  Cn_β > 0: if sideslip to right (β > 0), yawing moment turns nose right → aligns with flow
  Provided by vertical tail: Cn_β = (CL_α)_VT × (lVT/b) × (SVT/S) × η_VT
  Dorsal fin, ventral strakes: extend effective VT at high α
  T-tail: endplate effect increases VT efficiency (but T-tail stall risk)
```

---

## 5. Dynamic Stability — Modes and Eigenvalues

```
**LTI stability bridge:** This is exactly the state-space stability analysis from control theory. The matrix A is the Jacobian of f/dx evaluated at trim — the standard linearization of a nonlinear system. The stability modes (short period, phugoid, Dutch roll, spiral, roll) are the eigenvalues of A. Complex conjugate pairs = oscillatory modes (frequency = imaginary part, damping = negative real part). Real eigenvalues = monotone modes (stable if negative). The aircraft stability problem IS an LTI eigenvalue analysis where A depends parametrically on flight condition (Mach, altitude, CG location).

LINEARIZATION ABOUT TRIM:
  Δẋ = A·Δx + B·Δu   (small perturbation from trim)
  State: Δx = [Δu, Δw (or Δα), Δq, Δθ | Δv (or Δβ), Δp, Δr, Δφ]
           Longitudinal:            Lateral-directional:
           4 states                 4 states (decoupled for symmetric trim)

LONGITUDINAL MODES (2 pairs of complex eigenvalues):

  SHORT-PERIOD MODE:
    Fast oscillation in α (angle of attack) and q (pitch rate)
    Period: ~1-4 seconds; heavily damped
    Eigenvalue: λ = -ζ_sp ωn_sp ± iωn_sp√(1-ζ_sp²)
    Approximation: ωn_sp² ≈ -q∞·S·c̄·Cm_α / (Iyy)    (pure pitch stiffness)
    Damping: from pitch damping derivative Cm_q and Cm_α̇
    Handling: FAR 25 / MIL spec requires ζ_sp > 0.3 (Level 1: > 0.35, < 1.3 for ωn)

  PHUGOID MODE (Lanchester-Phugoid):
    Slow exchange of kinetic ↔ potential energy; nearly constant α
    Period: T ≈ π√2 · V / g ≈ 60-120 sec at cruise speeds
    Lightly damped (ζ_ph ≈ 1/(√2 × L/D)); stable in most aircraft
    Approximation: ωn_ph ≈ g√2 / V;  ζ_ph ≈ CD / (√2 · CL)
    Pilot can easily control phugoid (slow enough to see and respond)
    FAR 25 allows phugoid t₁/₂ > 55 sec (very mildly unstable allowed)

LATERAL-DIRECTIONAL MODES (2 real eigenvalues + 1 complex pair):

  ROLL MODE:
    Pure rolling motion; heavily damped; decays fast
    τ_roll = -Iₓₓ / (q∞·S·b·Cl_p)   (roll time constant)
    Cl_p < 0: roll damping (wing moving in direction of roll has increased α)
    Typical: τ_roll ≈ 0.1-0.5 sec; Level 1 requires τ_roll < 1 sec (FAR 25/MIL)

  SPIRAL MODE:
    Very slow; real eigenvalue (no oscillation)
    Interaction between directional stability and dihedral effect
    Cn_β · Cl_p - Cl_β · Cn_r > 0: stable spiral (→ diverges slowly)
    Most aircraft slightly spiral unstable (lazy autopilot wing-drop)
    FAR 25: stable or t₂ > 20 sec if unstable (slowly divergent allowed)

  DUTCH ROLL:
    Coupled yaw+roll oscillation; wings rock while yawing
    Period: ~5-15 sec; can be lightly damped
    ωn_DR ≈ √(q∞·S·b·Cn_β / Izz)    (yaw stiffness approximation)
    Damping from yaw damper: Cn_r < 0 (yaw rate opposes yaw)
    Most swept-wing jets need YAW DAMPER to stabilize Dutch roll
    FAR 25: ζ_DR ≥ 0.04 (minimum); pilot must be able to recover if yaw damper fails
    B707 without yaw damper was nearly unflyable on some flights

SUMMARY TABLE:
  Mode         | DOF      | Period    | Damping      | Control
  -------------|----------|-----------|--------------|-------------
  Short period | α, q     | 1-4 sec   | High (good)  | Elevator
  Phugoid      | V, γ     | 60-120s   | Low (OK)     | Throttle/elev
  Roll         | p        | <1 sec    | High         | Ailerons
  Spiral       | φ, β     | >100 sec  | Very low     | Rudder/aileron
  Dutch roll   | β, φ, r  | 5-15 sec  | Low (needs   | Yaw damper
               |          |           | yaw damper)  |
```

---

## 6. Control Surfaces and Effectiveness

```
PRIMARY CONTROL SURFACES:

  ELEVATOR (longitudinal):
    Hinged trailing edge of horizontal tail
    Generates ΔCm = Cm_δe · δe
    Authority: Cm_δe typically -0.01 to -0.04 per degree
    FAR 25: must achieve trim at VFE, minimum speed, maximum aft CG
    Trimmable horizontal stabilizer (THS): large authority trim for fuel burn CG shift;
      elevator handles short-term corrections

  AILERON (lateral):
    Differential trailing edge flaps on outer wing
    Roll rate: p = Cl_δa · δa · (2V/b) ... steady state from Cl_p damping
    Adverse yaw: aileron deflection creates drag → yawing opposite to roll
      → mitigated by differential aileron, frise aileron, rudder coordination
    High-speed ailerons (inboard): used above flap extension speed; reduce wing twist
    Spoilers: supplement or replace outboard ailerons at high speed (less aeroelastic twist)

  RUDDER (directional):
    Vertical tail trailing edge; controls sideslip β
    Cn_δr < 0: right rudder → nose left → coordinates turn
    Critical case: engine failure at Vmca (minimum control speed, air)
      must maintain straight flight with maximum asymmetric thrust + max rudder
    Rudder limiting: at high speed, full rudder would overstress fuselage/VT

SECONDARY/AUGMENTATION:
  FLAPS (high-lift, see aerodynamics module): ΔCL_max, ΔCm shift
  FLAPERONS: combined flap + aileron on some aircraft
  SPOILERS: roll control + ground spoilers (weight-on-wheels dump for braking)
  CANARD: forward lifting surface; elevon acts as control + contributes lift
  THRUST VECTORING: nozzle deflection (F-22, F-35B); post-stall maneuvering
  ELEVON: elevator + aileron on tailless/flying wing designs

CONTROL SURFACE SIZING (FAR 25 critical cases):
  Elevator: Vmca trim with aft CG; rotation at VR; flare authority at Vref
  Aileron + spoiler: FAR 25.147 lateral control (1-engine-out)
  Rudder: Vmca (engine failure); crosswind landing (±15 kt typical certification)
```

---

## 7. Fly-by-Wire (FBW)

```
CONVENTIONAL MECHANICAL vs FBW:

  Mechanical: cables/push rods → control surface; pilot input directly moves surface
    Mass: heavy cables; feel: direct (may be excessive force)
    Limits: no envelope protection; pilot can overstress aircraft
    Boeing 727, 737-Classic, DC-9: full mechanical (with hydraulic boost)

  Fly-by-Wire: pilot input → computer → actuator command → surface
    Pilot input is command to flight control law; not direct surface movement
    Signal path: LVDT/RVDT sensor → FCC (flight control computer) → EHSA (electrohydraulic actuator)

FBW ARCHITECTURE:

  Quadruplex (4-channel) typical: 4 independent computers; voter/monitor logic
  ┌──────────────────────────────────────────────────────────┐
  │  PILOT INPUT    INCEPTOR (sidestick or conventional yoke)│
  │       │                    │                             │
  │  ADIRS (air data / inertial ref): α, β, V, γ, Euler     │
  │       │                    │                             │
  │  ┌────┴────┐ ┌────┐ ┌────┐ ┌────┐  ← 4 FCCs             │
  │  │  FCC1   │ │FCC2│ │FCC3│ │FCC4│     majority voting    │
  │  └────┬────┘ └────┘ └────┘ └────┘                        │
  │       │                                                   │
  │  ACTUATORS (EHSA) → CONTROL SURFACES                      │
  │       ←── hydraulic + electrical power sources (3 hyd)   │
  └──────────────────────────────────────────────────────────┘

  Airbus A320 philosophy: "carefree" — FBW prevents pilot from:
    - Exceeding α_max (AOA protection)
    - Exceeding bank angle limit (±67° normal law)
    - Structural load factor limit (±2.5g / -1g)
    - Overspeed (VMO/MMO protection)

  Boeing 777/787 philosophy: FBW but pilot can override limits with sufficient force
    (slightly different design philosophy — pilot has ultimate authority)

FLIGHT CONTROL LAWS (FCL):
  Normal Law: full envelope protection; fly-by-wire with protections
  Alternate Law: some protections lost (e.g., β-protection gone); manual augmentation
  Direct Law: direct surface command (1:1); no protections; pilot flies like mechanical

  Degradation path: Normal → Alternate → Direct (with computer/sensor failures)
  Reconfiguration: sensors monitored; failed sensor removed from computation set

BENEFITS OF FBW:
  1. Weight reduction: 1-3% MTOW; lighter control runs
  2. Carefree handling: pilot can't inadvertently depart from controlled flight
  3. Control law optimization: pitch/roll response tuned for flying qualities
  4. Aeroelastic control: suppress flutter; active load alleviation (gust/maneuver)
  5. Mission adaptation: CG optimization by fuel transfer (A330 trim tank)
  6. Envelope protection: especially valuable for transport aircraft
  7. Relaxed stability: more efficient aircraft; computer provides stability augmentation

HANDLING QUALITIES vs INHERENT STABILITY:
  F-16: statically unstable in pitch (SM < 0); fast enough that pilot cannot correct;
    only flyable with FBW; gains: 10-15% drag reduction vs stable version
  B-2: inherently unstable in multiple axes; all FBW
  F-22: negative SM; also thrust vectoring for post-stall
```

---

## 8. Handling Qualities

```
COOPER-HARPER RATING SCALE (CHR):
  Quantifies pilot workload required to complete defined task
  ┌──────┬─────────────────────────────────────────────────────────┐
  │ CHR  │ Description                                             │
  ├──────┼─────────────────────────────────────────────────────────┤
  │  1   │ Excellent; minimal compensation required                │
  │  2   │ Good; compensation not factor                           │
  │  3   │ Fair; minimal compensation required                     │
  │  4   │ Minor deficiencies; moderate pilot compensation         │
  │  5   │ Moderately objectionable; considerable compensation     │
  │  6   │ Very objectionable; extensive compensation required     │
  │  7   │ Major deficiencies; adequate performance not achievable │
  │  8   │ Intense compensation; barely controllable               │
  │  9   │ Intense compensation; control maintained with luck      │
  │ 10   │ Loss of control                                         │
  └──────┴─────────────────────────────────────────────────────────┘

HANDLING QUALITY LEVELS (MIL-HDBK-1797 / MIL-F-8785C):
  Level 1 (CHR 1-3): clearly adequate for task; pilots prefer
  Level 2 (CHR 4-6): adequate to accomplish mission; increased workload
  Level 3 (CHR 7-9): controllable; mission compromised; safe recovery possible

FAR 25 HANDLING QUALITY REQUIREMENTS (selected):
  Short-period damping: ζ_sp = 0.35-1.3 (Level 1 range varies with ωn·n/α)
  Phugoid: must damp within defined time; t₁/₂ > 55 sec if unstable
  Dutch roll: ζ_DR × ωn_DR ≥ 0.05 rad/s; ζ_DR ≥ 0.08 (transport)
  Roll time constant: τ_roll < 1.0 sec (for Class III: large transport)
  Roll response: 30° bank in 1 engine out requires specific time to achieve

PILOT-INDUCED OSCILLATION (PIO):
  Closed-loop instability: pilot + aircraft form feedback loop that oscillates
  Common with FBW: phase lag between stick input and aircraft response
  Prevention: FBW control laws must have adequate bandwidth and phase margin
  Time delay budget: actuator + sensor + computation + comm < 50-100 ms total
  PIOS incidents: JAS 39 Gripen prototype crash (1989); YF-22 landing (1992)
```

---

## 9. V-n Diagram (Flight Envelope)

```
V-n DIAGRAM (Velocity vs Load Factor):

  Load factor: n = L/W = aerodynamic lift / weight
    Level flight: n = 1
    Pull-up maneuver: n > 1
    Push-over / inverted: n < 0

  ┌─────────────────────────────────────────────────────────────┐
  │  n                                                          │
  │   │      ┌────────────────────── structural limit (+)       │
  │ n_limit+ │·················· positive limit load factor     │
  │   │     /                                                   │
  │   │    /  ← stall boundary                                  │
  │   │   /   CL = CL_max; n = q·S·CL_max / W ∝ V²            │
  │ 1 │  /                                                      │
  │   │ /                                                       │
  │   │/_____________________ V_A    V_C    V_D   → V          │
  │   │\                                                        │
  │   │ \  ← negative stall boundary (CL = -CL_max)            │
  │ n_limit- └──────────────────── structural limit (-)         │
  └─────────────────────────────────────────────────────────────┘

KEY SPEEDS:
  VS = stall speed (1g; n=1): V_S = √(2W / (ρ·S·CL_max))
  VA = design maneuvering speed: max speed for full control deflection
     VA = VS × √(n_limit+)  → at VA, stall occurs before structural limit
     FAR 25: no structural damage from single full control input at VA
  VC = design cruise speed: normal ops; must be above required cruise + margin
  VD = design dive speed: VD ≥ 1.25 × VC typically; flutter-free to VD × 1.15
  VNE = never-exceed speed (demonstrated for piston/GA aircraft)

FAR 25 LIMIT LOAD FACTORS (transport category):
  Positive limit:  n_lim+ = 2.5  (clean); can be higher for aerobatic
  Negative limit:  n_lim- = -1.0 clean / -0.5 flaps
  Ultimate load:   1.5 × limit load factor (yield/fracture safety margin)

  Proof load test: 100% limit load → no permanent deformation
  Ultimate load test: 150% limit load → no collapse for ≥ 3 seconds

GUST ENVELOPE (superimposed on V-n):
  Ude = vertical gust velocity (FAR 25: 56 fps at VC; 25 fps at VD for transport)
  Δn = ρ·V·a·Kg·Ude / (2·W/S)    (Kg = gust alleviation factor ≈ 0.88)
  Gust loads often critical at light loading (low W/S → more gust-sensitive)
```

---

## 10. Performance

```
POINT PERFORMANCE (instantaneous):

CLIMB RATE (rate of climb, RC):
  RC = (T - D)·V / W = P_excess / W    [ft/min or m/s]
  Maximum RC: at speed where (T-D)·V is maximum
  For jets: approx at minimum drag speed (best L/D speed)
  Service ceiling: RC = 100 fpm (30 m/min)
  Absolute ceiling: RC = 0 (thrust = drag; no further excess thrust)

RANGE (Breguet range equation):
  R = (η_P / g) × (L/D) × (V/c_p) × ln(W₁/W₂)   [piston: η_P = prop efficiency]
  R = (V/g) × (L/D) × (1/c_j) × ln(W₁/W₂)        [jet: c_j = thrust SFC]

  Maximize range:
    Jet: fly at speed for maximum L/D × M = maximum "range parameter" (M·L/D)
    Piston: fly at maximum L/D speed (lower speed than jet optimum)
    Altitude effect: higher altitude → lower ρ → must fly faster to maintain L/D,
      but SFC of turbofan improves slightly → best cruise at high altitude/Mach

ENDURANCE (time in air):
  E = (η_P / g) × (CL^(3/2)/CD) × (1/c_p) × (1/√(2ρ/S)) × (√W₁ - √W₂)  [piston]
  Jet: maximum endurance at minimum fuel flow = minimum drag speed (V_min drag)
  Endurance maximized at lower speed than range (more time per fuel burned)

STEP CLIMB:
  As fuel burns, aircraft weight decreases → optimal altitude increases
  Step climb: airline climbs every ~2000 lb of fuel burn to higher FL
  Managed by FMS in step-climb mode

TURNING FLIGHT PERFORMANCE:
  Sustained turn rate (STR): maximum ψ̇ at constant altitude and speed (g limited)
  Instantaneous turn rate (ITR): maximum ψ̇ ignoring energy (structural limit)
  Corner speed: V* where both structural limit and aerodynamic limit intersect = maximum ITR
  Fighter merit figure: Energy maneuverability (EM) theory (Boyd)
    Ps = (T-D)·V / W = specific excess power → drives turn rate AND acceleration

TAKEOFF AND LANDING:

  GROUND ROLL (takeoff):
    a = g(T/W - μ - CD_gr/(CL_gr + 2W/ρV²S))  (friction + aerodynamic drag - lift)
    STO = V_R² / (2 · a_avg)   (approximation)
    V_R = rotation speed ≥ 1.05 V_MC; then climb to 50 ft = FAR 25 screen height

  BALANCED FIELD LENGTH (BFL):
    Decision speed V₁: if engine fails before V₁ → stop; after V₁ → continue
    BFL: accelerate-stop distance = accelerate-go distance (over 35 ft obstacle)
    Determines: maximum MTOW for given runway; or minimum runway for given weight
    OEI climb requirement: FAR 25 requires positive OEI climb gradient post-liftoff

  LANDING:
    Vref = 1.3 × VS_landing (50 ft screen height reference speed)
    Ground roll: reverse thrust + brakes; landing distance to full stop
    FAR 25: landing field length = 1/0.6 × actual stopping distance (60% correction)
    Wet runway: additional 15% penalty for hydroplaning correction

SPECIFIC ENERGY AND EM THEORY (John Boyd):
  Total specific energy: E_s = h + V²/(2g)   [altitude + velocity height]
  Specific excess power: Ps = dE_s/dt = (T-D)·V/W
  P_s = 0: maximum sustained turn rate at that altitude and speed
  Fighter EM diagram: Ps contours overlaid; want high Ps envelope vs adversary
```

---

## 11. Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| Longitudinal static stability criterion? | ∂Cm/∂CL < 0; equivalently: CG forward of neutral point |
| Neutral point location? | CG position at which Cm_α = 0; beyond NP → unstable |
| Static margin for modern airliner? | 5-15% c̄; fighters may use 0 to -5% (unstable, FBW) |
| Fastest mode of motion? | Short-period (α/q oscillation; ~1-4 sec period) |
| Slowest longitudinal mode? | Phugoid (V/γ exchange; ~60-120 sec; lightly damped) |
| What causes Dutch roll? | Swept wing high Cl_β (lateral) + weak Cn_β (dir.); needs yaw damper |
| Why FBW for fighters? | Allows negative SM → better maneuverability; computer provides stability |
| Corner speed? | Speed at which STR and ITR both maximize (structural + aerodynamic limits meet) |
| Maneuvering speed VA significance? | At VA, aircraft stalls before structural limit is reached with full control input |
| BFL stands for? | Balanced field length: stop distance = continue-and-climb distance at V₁ |
| Load factor in 60° banked turn? | n = 1/cos(60°) = 2.0 |
| Service ceiling definition? | Altitude where maximum RC = 100 fpm |
| Phugoid period approximation? | T ≈ π√2 × V/g ≈ 100 sec at cruise |
| What does Cm_δe < 0 mean? | Positive elevator → nose-down pitching moment (sign convention: up elevator = negative δe in most conventions) |
| Cooper-Harper 1-3 = ? | Level 1 handling qualities: clearly adequate |

---

## Common Confusion Points

**Body axes vs stability axes:** Body axes are fixed to the airframe; stability axes have x_s aligned with the freestream in the symmetry plane at trim. Stability derivatives (Cm_α, Cl_β) are defined in stability axes. When computing eigenvalues for linearized EoM, use stability axes.

**Static stability ≠ dynamic stability:** An aircraft can be statically stable but dynamically unstable (divergent oscillation if damping < 0). Usually static stability is necessary but not sufficient for dynamic stability. Phugoid is statically stable but can have low damping.

**Load factor n is not a force:** n = L/W is dimensionless — the number of "g's" experienced. At n=1, you feel normal gravity. At n=3, your body feels 3× its weight. The structural limit (2.5 for transport) limits the aerodynamic force magnitude.

**VA is not the maximum maneuvering speed:** VA is defined such that at VA with full control input, the aircraft stalls before the structural limit is exceeded. Below VA you can apply full deflection. Above VA, partial deflections only — structural damage possible from full input. VA decreases with decreasing weight (lighter aircraft → lower VA).

**FBW Airbus sidestick = rate command, not position command:** Sidestick center = hold current pitch/roll attitude (roughly). Full aft = maximum pitch rate command (with protection). No mechanical connection means two pilots can fight; separate warning system (priority pushbutton) resolves conflicts.

**Phugoid origin — Lanchester's insightful model:** In the phugoid, angle of attack is nearly constant. Aircraft oscillates between diving (gaining speed → gaining lift → pitching up → gaining altitude → losing speed → repeating). Energy exchange: kinetic ↔ potential. Damping from profile drag. High-L/D aircraft (gliders) have very lightly damped phugoid.

**Dutch roll vs spiral mode naming:** "Dutch roll" refers to a combined yaw-roll wobble (like a speed skater's motion). "Spiral mode" is a slow bank divergence (spiral dive if unstable). These are lateral-directional modes and always appear together — you can't fix one without affecting the other (tradeoff between Cl_β and Cn_β).
