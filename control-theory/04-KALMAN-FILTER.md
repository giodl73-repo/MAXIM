# Kalman Filter, EKF, UKF & Sensor Fusion

## The Big Picture

```
+------------------------------------------------------------------+
|               STATE ESTIMATION LANDSCAPE                         |
+------------------------------------------------------------------+
|                                                                    |
|  PROBLEM:  Estimate x(t) from noisy measurements y(t)            |
|            when x(t) evolves according to a dynamic model         |
|                                                                    |
|  LINEAR + GAUSSIAN        NONLINEAR          NONLINEAR (precise)  |
|  ──────────────────       ────────────────   ────────────────     |
|  Kalman Filter (KF)       Extended KF (EKF)  Unscented KF (UKF)  |
|  Optimal, closed-form     Linearize around   Sigma-point approx  |
|                           current estimate   3rd order accurate   |
|                                                                    |
|  LARGE STATE / PARTICLES  BAYESIAN FRAMEWORK                      |
|  ─────────────────────    ─────────────────                       |
|  Particle Filter (PF)     All estimators are Bayesian filters     |
|  Sequential Monte Carlo   KF = exact Bayes for linear Gaussian    |
|  Handles multimodal       PF = exact Bayes (approx via samples)   |
+------------------------------------------------------------------+
```

The Kalman filter (1960) is the optimal linear estimator — it solves the
problem of estimating state from noisy measurements in closed form.
It's a recursive Bayesian filter that maintains a Gaussian belief state.

---

## The State Estimation Problem

```
SYSTEM MODEL:
  ẋ = Ax + Bu + w     w ~ N(0, Q_w)  process noise (covariance Q_w)
  y = Cx + v          v ~ N(0, R_v)  measurement noise (covariance R_v)

DISCRETE-TIME VERSION:
  x[k+1] = A_d x[k] + B_d u[k] + w[k]   w[k] ~ N(0, Q_d)
  y[k]   = C x[k] + v[k]                 v[k] ~ N(0, R)

WHAT WE WANT:
  ̂x[k|k] = E[x[k] | y[0], y[1], ..., y[k]]   (posterior mean given all measurements)
  P[k|k] = Var[x[k] | y[0],...,y[k]]           (posterior covariance)

FOR LINEAR GAUSSIAN SYSTEMS: This posterior is exactly Gaussian.
  ̂x[k|k], P[k|k] fully characterize the belief state.
  Kalman filter computes both recursively and optimally.
```

---

## Kalman Filter Algorithm

Two phases: predict and update.

```
INITIALIZATION:
  ̂x[0|-1] = x₀  (prior mean)
  P[0|-1] = P₀   (prior covariance)

────────────────────────────────────────────────────────────────
PREDICT (time update):
  ̂x[k|k-1] = A_d ̂x[k-1|k-1] + B_d u[k-1]    (predicted state)
  P[k|k-1]  = A_d P[k-1|k-1] A_dᵀ + Q_d       (predicted covariance)

────────────────────────────────────────────────────────────────
UPDATE (measurement update) — when measurement y[k] arrives:

  Innovation:   ỹ[k] = y[k] − C ̂x[k|k-1]        (prediction error)
  Innovation cov: S[k] = C P[k|k-1] Cᵀ + R        (innovation uncertainty)
  Kalman gain:  K[k] = P[k|k-1] Cᵀ S[k]⁻¹         (optimal weighting)

  ̂x[k|k] = ̂x[k|k-1] + K[k] ỹ[k]               (updated estimate)
  P[k|k]  = (I − K[k]C) P[k|k-1]                (updated covariance)

  Numerically stable form: P[k|k] = (I−KC)P(I−KC)ᵀ + KRKᵀ (Joseph form)

────────────────────────────────────────────────────────────────
```

### Interpretation

The Kalman filter is the mathematically optimal answer to "how do I reconstruct system state from noisy telemetry?" — exactly what an observability platform does. The Kalman gain K implements the same trust-weighting logic used in Bayesian A/B testing and anomaly detection: when the sensor (metric) is noisy (high R), trust the model prediction; when the sensor is reliable (low R), update aggressively toward the measurement. Anomaly detectors in monitoring systems (including Azure Monitor) use Kalman-type filters for this reason.

```
Kalman gain K mediates between model and measurement:

  K → 0  (R large, noisy sensor):    trust the model prediction more
          ̂x[k|k] ≈ ̂x[k|k-1]

  K → C⁻¹ (R small, perfect sensor): trust measurement
           ̂x[k|k] ≈ C⁻¹ y[k]

  K = P Cᵀ (C P Cᵀ + R)⁻¹:
    Numerator P Cᵀ: how uncertain is state × how it affects output
    Denominator S: total output uncertainty (model + sensor)

GEOMETRIC VIEW:
  KF is weighted average of prior prediction and measurement.
  Weights inversely proportional to uncertainties.
  P[k|k] ≤ P[k|k-1] always (measurement always helps).
  (In PSD ordering: more information = smaller covariance.)
```

---

## Steady-State Kalman Filter

For time-invariant systems, P converges to a fixed value P∞:

```
P∞ satisfies the Algebraic Riccati Equation (dual of LQR ARE):
  A P∞ + P∞ Aᵀ − P∞ Cᵀ R⁻¹ C P∞ + Q_w = 0

Steady-state Kalman gain:
  K∞ = P∞ Cᵀ R⁻¹

Once P∞ converges, the filter has constant gain K∞ — can be precomputed.
This is the "steady-state observer" used in LQG control.

Condition for convergence (P∞ finite and unique):
  (A, C) detectable  (unstable modes must be observable)
  (A, Γ) stabilizable where Q_w = ΓΓᵀ  (noise must excite unstable modes)

Python: P∞, K∞ = scipy.linalg.solve_continuous_are(A, C.T, Q_w, R)
```

---

## Continuous-Time Kalman Filter

```
Continuous-time system:
  ẋ = Ax + Bu + w     w ~ N(0, Q_w) (power spectral density)
  y = Cx + v          v ~ N(0, R)   (PSD)

Kalman-Bucy filter:
  ̂ẋ = Aẑ + Bu + K(t)(y − Cẑ)    (observer ODE)
  K(t) = P(t) Cᵀ R⁻¹             (time-varying gain)

Riccati ODE for P(t):
  Ṗ = AP + PAᵀ − PC^T R⁻¹ CP + Q_w,   P(0) = P₀

Steady state: Ṗ = 0 → solves ARE above.

Note: In continuous time, process noise Q_w has units of power spectral
density, not covariance. Discretization: Q_d ≈ Q_w T_s.
```

---

## Extended Kalman Filter (EKF)

For nonlinear systems — linearize around current estimate:

```
NONLINEAR SYSTEM:
  x[k+1] = f(x[k], u[k]) + w[k]     f: nonlinear state transition
  y[k]   = h(x[k]) + v[k]           h: nonlinear measurement model

EKF ALGORITHM:

PREDICT:
  ̂x[k|k-1] = f(̂x[k-1|k-1], u[k-1])     (nonlinear propagation)
  F[k] = ∂f/∂x |_{̂x[k-1|k-1]}            (Jacobian of f)
  P[k|k-1]  = F[k] P[k-1|k-1] F[k]ᵀ + Q_d (linearized covariance)

UPDATE:
  H[k] = ∂h/∂x |_{̂x[k|k-1]}              (Jacobian of h)
  ỹ[k] = y[k] − h(̂x[k|k-1])             (innovation)
  S[k] = H[k] P[k|k-1] H[k]ᵀ + R
  K[k] = P[k|k-1] H[k]ᵀ S[k]⁻¹
  ̂x[k|k] = ̂x[k|k-1] + K[k] ỹ[k]
  P[k|k]  = (I − K[k]H[k]) P[k|k-1]

EKF LIMITATIONS:
  Jacobians required (analytical or numerical — autograd helps)
  Linearization error: P can become inconsistent (pessimistic/optimistic)
  Diverges if initial estimate far from truth (bad linearization)
  Not optimal (unlike KF for linear systems)

WHEN EKF FAILS:
  Highly nonlinear f or h (large higher-order terms)
  Large uncertainty P (linearization around wrong point)
  Non-Gaussian posterior (multimodal, heavy tails)
```

---

## Unscented Kalman Filter (UKF)

Better nonlinear approximation — no Jacobians, 3rd order accuracy:

```
UNSCENTED TRANSFORM:
  Instead of linearizing, propagate carefully chosen "sigma points"
  through the exact nonlinear function.

  For state dimension n and state estimate ̂x with covariance P:
  2n+1 sigma points:
    χ₀ = ̂x
    χᵢ = ̂x + (√((n+λ)P))ᵢ    for i = 1,...,n
    χᵢ = ̂x − (√((n+λ)P))ᵢ₋ₙ  for i = n+1,...,2n

  where λ = α²(n+κ) − n (scaling parameter, α ∈ [10⁻⁴,1], κ = 0 or 3-n)

WEIGHTS:
  W₀ᵐ = λ/(n+λ),  W₀ᶜ = λ/(n+λ) + (1−α²+β),  β=2 for Gaussian
  Wᵢᵐ = Wᵢᶜ = 1/(2(n+λ))  for i=1,...,2n

UKF PREDICT:
  Propagate: γᵢ = f(χᵢ)                        (exact nonlinear)
  ̂x[k|k-1] = Σ Wᵢᵐ γᵢ                         (weighted mean)
  P[k|k-1] = Σ Wᵢᶜ (γᵢ−̂x)(γᵢ−̂x)ᵀ + Q_d       (weighted covariance)

UKF UPDATE:
  Measurement sigma points: ζᵢ = h(γᵢ)
  ŷ = Σ Wᵢᵐ ζᵢ
  S = Σ Wᵢᶜ (ζᵢ−ŷ)(ζᵢ−ŷ)ᵀ + R
  Cross-covariance: P_xy = Σ Wᵢᶜ (γᵢ−̂x)(ζᵢ−ŷ)ᵀ
  K = P_xy S⁻¹
  ̂x[k|k] = ̂x[k|k-1] + K(y[k] − ŷ)
  P[k|k] = P[k|k-1] − KSKᵀ

ADVANTAGES OVER EKF:
  No Jacobians required
  Captures mean and covariance to 3rd order (EKF: 1st order)
  More robust for nonlinear systems
  Similar O(n³) cost (square root implementations: O(n²))

WHEN UKF FAILS:
  Highly multimodal posteriors (particle filter needed)
  Dimension n very large (cost prohibitive)
```

---

## Particle Filter (Sequential Monte Carlo)

For highly nonlinear, non-Gaussian systems:

```
IDEA: Represent p(x[k]|y[0:k]) as weighted samples (particles):
  {χᵢ[k], wᵢ[k]}ᵢ₌₁ᴺ   (N particles, each a state hypothesis)

SEQUENTIAL IMPORTANCE RESAMPLING (SIR):
  1. PREDICT: propagate each particle through dynamics (with noise)
     χᵢ[k|k-1] = f(χᵢ[k-1|k-1]) + w_sample

  2. UPDATE: weight by likelihood of measurement:
     wᵢ[k] ∝ wᵢ[k-1] · p(y[k] | χᵢ[k|k-1])
             (Gaussian: exp(-½(y-h(χ))ᵀ R⁻¹ (y-h(χ))))

  3. NORMALIZE: Σwᵢ = 1

  4. RESAMPLE: when effective sample size N_eff = 1/Σwᵢ² drops below N/2:
     resample N particles with replacement proportional to weights
     (avoids degeneracy — all weight on one particle)

ESTIMATES:
  Mean: ̂x[k] = Σ wᵢ χᵢ
  Covariance: P[k] = Σ wᵢ (χᵢ−̂x)(χᵢ−̂x)ᵀ

COMPLEXITY: O(N·n) per step, N = 100–10000+ particles for reasonable accuracy
ADVANTAGE: Can handle multimodal distributions, any noise model, any f,h
DISADVANTAGE: High computational cost; degeneracy in high dimensions
```

---

## SLAM (Simultaneous Localization and Mapping)

**Scalability parallel:** EKF-SLAM's O(L^2) cost as landmarks grow mirrors the scaling challenge in distributed tracing: naive correlation of all spans across L services is quadratic. The same argument that drove robotics from EKF-SLAM to Graph SLAM (sparse factored representations) drives observability platforms toward sampling-based and indexed trace strategies.

The flagship application combining Kalman filtering with robotics:

```
PROBLEM: Robot navigates unknown environment.
  - Estimate robot pose x_r (position + orientation)
  - Simultaneously build map of landmarks m = {mᵢ}
  - Observations: range/bearing to landmarks, odometry

STATE: x = [x_r, m₁, m₂, ..., m_L]ᵀ  (grows as landmarks discovered)

EKF-SLAM:
  State covariance P captures correlations between robot pose AND map.
  As map grows: O(L²) covariance → becomes O(L²) cost per step → not scalable.

GRAPH SLAM (modern):
  Optimize over all past poses + landmarks together.
  Factor graph formulation: pose-graph optimization.
  Solves sparse linear system (sparse Cholesky) → O(n) in practice.

  g2o, iSAM2/GTSAM libraries: real-time factor graph optimization.

LIDAR SLAM stack (ROS 2):
  IMU → dead reckoning (high-freq)
  LIDAR → scan matching (ICP, NDT, LOAM)
  GNSS → global anchor (if available)
  EKF/UKF → fuse all sensors (robot_localization package)
```

---

## Sensor Fusion Architecture

```
LOOSELY COUPLED:
  Each sensor runs its own filter → fuse output state estimates
  Simple, handles dropout gracefully
  Less accurate (discards cross-correlations)

TIGHTLY COUPLED:
  All sensor measurements fused in one filter
  Better accuracy (exploits correlations)
  More complex, harder to maintain

GPS/IMU FUSION:
  IMU: high-rate (100–1000 Hz), drifts over time (6-DOF: acc + gyro)
  GPS: low-rate (1–10 Hz), absolute position, noisy
  EKF: IMU = process model (predict), GPS = measurement (update)
  INS: Inertial Navigation System = integrated IMU

COMPLEMENTARY FILTER:
  Simple fusion: high-pass-filter IMU + low-pass-filter slower sensor
  Gyro: good short-term → high-pass (rate integration)
  Accelerometer: good long-term → low-pass (absolute tilt)
  Madgwick filter: efficient attitude estimation, widely used in robotics/drones
```

---

## Implementation Notes

```
NUMERICAL ISSUES:
  P must remain symmetric positive definite.
  Round-off can make P non-symmetric or near-singular.

  Fix 1: P = (P + Pᵀ)/2  (symmetrize after update)
  Fix 2: Joseph form: P = (I−KC)P(I−KC)ᵀ + KRKᵀ (always PSD)
  Fix 3: Square-root filter (Cholesky factor of P) — most numerically stable

SQUARE-ROOT KALMAN FILTER:
  Propagate S = chol(P) instead of P.
  Predict: S_pred from QR decomposition of [A·S; Q^{1/2}]
  Update: S_post from QR decomposition of [H·S_pred; R^{1/2}]
  Always P = S·Sᵀ > 0 by construction.

ADAPTIVE COVARIANCE:
  Q_w and R often unknown in practice.
  Adaptive: estimate from innovation statistics.
  Innovation whiteness test: if innovations are white (uncorrelated),
    filter is consistent. If not: adjust Q or R.

  Innovation-based Q adaptation:
    Q_est[k] = K[k] ỹ[k] ỹ[k]ᵀ Kᵀ[k]  (windowed average)
```

---

## Decision Cheat Sheet

| Situation | Estimator |
|-----------|-----------|
| Linear dynamics + Gaussian noise | Kalman Filter (KF) — optimal |
| Mildly nonlinear, unimodal | Extended Kalman Filter (EKF) |
| Moderately nonlinear, n < 50 | Unscented Kalman Filter (UKF) |
| Highly nonlinear, multimodal | Particle Filter (PF) |
| Robot localization with known map | EKF/UKF SLAM |
| Robot in unknown environment | Graph SLAM (GTSAM, iSAM2) |
| IMU + GPS fusion | EKF or Complementary Filter |
| P becoming non-PSD numerically | Joseph form or Square-Root filter |
| Need to estimate Q, R online | Adaptive KF with innovation monitoring |

---

## Common Confusion Points

**"Kalman filter requires knowing Q and R"** — yes, and this is the hardest
part in practice. Q (process noise) is often set from physics insight;
R (sensor noise) from datasheet or empirical calibration. Misspecification
degrades performance but rarely causes instability.

**"EKF linearizes the dynamics"** — not the dynamics for propagating the
state estimate (that uses the exact nonlinear f). EKF linearizes only for
propagating the covariance P via Jacobians.

**"KF assumes the Gaussian assumption will hold"** — it propagates a
Gaussian belief, but reality may not be Gaussian. For linear systems with
Gaussian noise, KF is exactly optimal. For nonlinear/non-Gaussian, it's
an approximation (often good enough).

**"Kalman smoother is same as Kalman filter"** — filter = causal estimate
using past measurements only (real-time). Smoother = optimal estimate using
all measurements including future ones (offline). Rauch-Tung-Striebel (RTS)
smoother runs the KF forward, then backward.

**"More sensors = better estimate"** — yes if correctly fused, but wrong
if covariances are misspecified. Overconfident R (R too small) makes the
filter trust measurements too much → biased estimates if sensor has systematic
error. Match R to actual sensor statistics.
