# Control Theory — Field Map & Orientation

## The Big Picture

Control theory is the mathematics of making systems behave as desired despite uncertainty,
disturbances, and complex dynamics. It spans everything from a thermostat to an aircraft
autopilot to a self-driving car. The core insight: **feedback transforms an unpredictable
open-loop system into a predictable closed-loop one**.

```
+------------------------------------------------------------------+
|               CONTROL THEORY LANDSCAPE                            |
+------------------------------------------------------------------+
|                                                                   |
|  CLASSICAL CONTROL          MODERN (STATE-SPACE)    ADVANCED     |
|  ┌────────────────┐         ┌──────────────────┐   ┌─────────┐ |
|  │ PID controller │         │ State-space       │   │ Optimal │ |
|  │ Transfer fcns  │         │ ẋ = Ax + Bu       │   │ LQR/LQG │ |
|  │ Root locus     │         │ y = Cx + Du       │   │ H∞      │ |
|  │ Bode plots     │         │                  │   │         │ |
|  │ Nyquist        │         │ Controllability   │   │ Robust  │ |
|  │ Lead/lag comp. │         │ Observability     │   │ Adaptive│ |
|  │ Gain/phase mgn │         │ Pole placement    │   │         │ |
|  └────────────────┘         │ Luenberger obs.   │   │ MPC     │ |
|  SISO, frequency domain     │ Kalman filter     │   │ Nonlin. │ |
|  Intuitive but limited      │ Separation princ. │   │ RL ctrl │ |
|  to linear, stable systems  └──────────────────┘   └─────────┘ |
|                             MIMO, time domain                     |
|  OPEN-LOOP vs CLOSED-LOOP   Handles multi-input/output           |
|  ┌──────────────────────────────────────────────────────────┐   |
|  │  Open loop:  reference → [controller] → [plant] → output │   |
|  │                                                          │   |
|  │  Closed loop (feedback):                                 │   |
|  │  reference → Σ → [controller] → [plant] → output        │   |
|  │              ↑                               |           │   |
|  │              └───────── feedback ────────────┘           │   |
|  └──────────────────────────────────────────────────────────┘   |
+------------------------------------------------------------------+
```

---

## Core Concepts

### System Representation

A **plant** is the physical system being controlled (motor, aircraft, chemical reactor).
The **controller** generates inputs to drive the plant to desired behavior.

```
TIME DOMAIN (ODE)            FREQUENCY DOMAIN             STATE SPACE
───────────────────────────  ─────────────────────────   ───────────────────────
mẍ + cẋ + kx = F(t)         G(s) = Y(s)/U(s)             ẋ = Ax + Bu
                             = k/(ms²+cs+k)               y = Cx + Du
Spring-mass-damper           Transfer function
                             (Laplace of ODE)             x ∈ ℝⁿ: state vector
Second order, SISO           SISO only                    u ∈ ℝᵐ: input
                             Works for LTI systems        y ∈ ℝᵖ: output

Transition:
ODE → Laplace transform → transfer function → poles/zeros in s-plane
OR
ODE → state variables → state matrices A, B, C, D
```

### Stability — The Foundational Concept

```
STABILITY TYPES              DEFINITION                   TEST
────────────────────────     ─────────────────────────    ──────────────────────
BIBO stable                  Bounded input → bounded      Poles strictly in
(Bounded I/O)                output                       left half s-plane (LTI)

Lyapunov stable              Small perturbation → stays   ∃ Lyapunov function
                             near equilibrium             V(x) > 0, V̇(x) ≤ 0

Asymptotically stable        Stable + convergence to      V̇(x) < 0 (strict)
                             equilibrium                  Poles have Re(λ) < 0

Marginally stable            Stable but doesn't converge  Poles on jω axis,
                                                          no repeated poles

Unstable                     Small perturbation → grows   Any pole with Re(λ) > 0
```

---

## Control Taxonomy

```
CONTROL PARADIGM       KEY IDEA                    USED WHEN
─────────────────────  ──────────────────────────  ─────────────────────────────
Classical / PID        Error-proportional control  Single loop, well-understood
                       Tuned by frequency methods  plant, SISO

State feedback         Full state measurement →     MIMO, fast dynamics,
                       u = -Kx                      pole placement needed

Observer-based         Estimate state from          Full state unmeasurable;
(Luenberger/Kalman)    outputs, then feed back      combines with state feedback

Optimal (LQR/LQG)      Minimize cost functional     Trade-off between control
                       J = ∫(x'Qx + u'Ru)dt        effort and tracking error

H∞ robust             Minimize worst-case gain     Significant model uncertainty,
                       from disturbance to output   guaranteed stability margins

Model Predictive (MPC) Solve optimization over      Constraints on inputs/states,
                       receding horizon             slow-enough plants (process)

Adaptive              Adjust parameters online      Unknown or time-varying plant

Nonlinear (feedback    Cancel nonlinearities via    Highly nonlinear plants where
linearization, sliding) exact algebraic inversion   linearization fails

Reinforcement learning  Learn policy from reward    Unknown dynamics, complex
                        (policy gradient, SAC)      cost functions, simulation
```

---

## The s-Domain Mental Model

Classical control lives in the s-plane (Laplace domain). The MIT 6.003/6.302 perspective:

```
s-PLANE GEOMETRY                WHAT IT MEANS
──────────────────────────────  ────────────────────────────────────────────
     jω                         Poles in LEFT half-plane  → stable
      |  X   ← pole at         Poles in RIGHT half-plane → unstable
  ────┼────────── σ             Poles on jω axis          → marginally stable
      |      X                  (pure oscillation, no damping)
      |
  (Re(s)=0 is the               Zero = frequency where system has no response
  stability boundary)           Pole = frequency where system resonates/blows up

Natural frequency: ωn = √(k/m)  Damping ratio: ζ = c/(2√km)
Characteristic equation: s² + 2ζωn·s + ωn² = 0
Poles: s = -ζωn ± ωn√(ζ²-1)

ζ < 0: unstable (growing oscillation)
ζ = 0: marginally stable (sustained oscillation)
0 < ζ < 1: underdamped (decaying oscillation)
ζ = 1: critically damped (fastest no-overshoot)
ζ > 1: overdamped (slow, no overshoot)
```

---

## Old-World Bridges

The control loop pattern is everywhere in software engineering:

```
CONTROL CONCEPT              SOFTWARE ENGINEERING ANALOG
────────────────────────     ────────────────────────────────────────────────
Feedback loop                Any closed-loop process: CI/CD feedback, load
                             balancer health checks, autoscaler

PID controller               TCP congestion control (CUBIC/BBR is essentially
                             a control system tracking bandwidth-delay product)

Set point                    Desired state (replica count in Kubernetes HPA)

Integrator                   Integral in HPA: accumulated error drives action

Steady-state error           Configuration drift without reconciliation loops

Kalman filter                Sensor fusion in robotics, GPS/INS dead reckoning,
                             Azure anomaly detection (hidden Markov + Kalman)

Model Predictive Control     Receding-horizon planning in logistics optimization

State observer               Log-based state reconstruction (observability pillar
                             in 15-OBSERVABILITY.md — same mathematical concept)

<!-- @editor[bridge/P2]: The observability bridge is named but not developed. Kalman-sense observability (can internal state be inferred from outputs?) is structurally identical to distributed systems observability (can service internal state be inferred from traces/metrics?). The rank condition on the observability matrix maps directly to whether logs emit enough signal to reconstruct system state. Worth one concrete sentence here and expansion in 04-KALMAN-FILTER.md. -->

Stability margin             "How much can deployment parameters vary before
                             the system goes unstable" — same Bode margin idea
```

---

## Session Arc for This Directory

```
00-OVERVIEW.md       ← You are here (field map, stability, taxonomy)
01-PID-CLASSICAL     ← PID controller + frequency-domain methods (Bode, Nyquist)
02-STATE-SPACE       ← State-space representation, controllability, pole placement
03-OPTIMAL-CONTROL   ← LQR/LQG, Pontryagin, HJB equation, dynamic programming
04-KALMAN-FILTER     ← Kalman filter, EKF/UKF, sensor fusion, SLAM
```

<!-- @editor[content/P2]: Session Arc lists only 5 files but the directory contains 10. Files 05-09 (Robust Control, Nonlinear Control, MPC, Adaptive Control, Learning-Based Control) are missing from this navigation map — a reader will not know they exist from the overview. Extend the arc table. -->

---

## Decision Cheat Sheet

| You want to...                              | Use this                    |
|---------------------------------------------|-----------------------------|
| Control a single loop (temperature, speed)  | PID controller              |
| Understand why the system oscillates        | Bode plot / root locus      |
| Guarantee stability margins                 | Nyquist criterion           |
| Control multiple inputs/outputs             | State-space + pole placement |
| Handle unmeasured states                    | Luenberger observer         |
| Balance tracking vs. control effort         | LQR optimal control         |
| Add noise/uncertainty to LQR               | LQG (LQR + Kalman)          |
| Guarantee robustness to model error         | H∞ control                  |
| Handle constraints on inputs/states         | Model Predictive Control    |
| Fuse sensors (GPS + IMU)                    | Kalman filter / EKF         |
| Unknown nonlinear dynamics                  | Reinforcement learning      |

## Common Confusion Points

**Stability is not the same as good performance.** A system can be stable but extremely
slow to converge, or stable but with large overshoot. Gain/phase margins quantify
*how much* stability margin exists.

**Transfer functions are SISO; state-space is MIMO.** Classical PID and Bode/Nyquist
methods work naturally for single-input single-output. For multi-variable plants (jet
engine with 4 actuators and 6 sensors), you need state-space methods.

**Open-loop vs closed-loop poles.** Root locus shows how open-loop poles move as gain
changes. The closed-loop poles are what actually determine stability and response.

**Observer ≠ Kalman filter** (in general). The Luenberger observer is deterministic pole
placement. The Kalman filter is the optimal observer for stochastic linear systems (Gaussian
noise). In practice, Kalman is almost always preferred over Luenberger.

**LQR does not guarantee robustness.** LQR is optimal for the modeled system but can have
poor performance for mismatched dynamics. LQG (LQR + Kalman) can actually have zero gain
margin — dovetail loop transfer recovery (LTR) or H∞ is needed for robustness guarantees.
