# Robotics — Sensors

## The Big Picture

Sensors are the robot's interface to physical reality. Two categories:
proprioceptive (self-sensing: what are my joints doing?) and exteroceptive
(world-sensing: what is in the environment?).

```
+===========================================================================+
|                           ROBOT SENSORS LANDSCAPE                         |
+===========================================================================+
|                                                                           |
|  PROPRIOCEPTIVE (self)              EXTEROCEPTIVE (world)                  |
|  =====================              ====================                   |
|                                                                           |
|  Encoders                           Distance / Range                      |
|    Optical / magnetic               LiDAR (2D, 3D)                        |
|    Absolute / incremental           Ultrasonic                            |
|    Resolution: 12-24 bit            IR (short range)                      |
|                                                                           |
|  IMU (Inertial Measurement)         Vision                                |
|    Accelerometer (MEMS)             Monocular camera                      |
|    Gyroscope (MEMS)                 Stereo camera                         |
|    Integration drift               RGB-D (depth)                          |
|    Allan variance noise model       Event camera                          |
|                                                                           |
|  Current / Torque sensors           Contact / Force                       |
|    Motor current -> torque          Force/torque (6-axis)                  |
|    Strain gauge load cells          Tactile arrays                         |
|                                     Bump sensors                          |
|                                                                           |
|  SENSOR FUSION: combine multiple sensors to get better state estimate     |
|    Kalman Filter (linear)           Extended Kalman Filter (nonlinear)    |
|    Complementary Filter             Particle Filter                        |
|                                                                           |
+===========================================================================+
```

---

## Proprioceptive Sensors

### Encoders

Encoders measure joint angle (rotary) or position (linear). They are the most
fundamental robot sensor — every joint needs one for closed-loop control.

```
ENCODER TYPES:
===============

INCREMENTAL ENCODER                   ABSOLUTE ENCODER
+------------------+                  +------------------+
| Counts pulses as | Loses count      | Outputs absolute | Retains position
| disk rotates.    | on power cycle.  | angle (Gray code | through power
| Requires homing  | Homing routine   | or SSI/BiSS      | cycle. No homing
| after power-on.  | on startup.      | protocol).       | needed.
+------------------+                  +------------------+
  Cheaper.                              More expensive.
  Most industrial servos use this.      Surgical robots, cobots.

OPTICAL ENCODER: LED + photodetector array reads slots in disk.
  Resolution: 512 to 1,000,000 counts/rev (10-20 bit).
  Fragile (vibration, contamination).

MAGNETIC ENCODER: Hall effect + magnetic pole disk.
  Less precise than optical but more robust (IP67+).
  Resolution: 12-16 bit.
  Common in harsh environments (welding, outdoor).

QUADRATURE DECODING:
  Two channels A and B, 90 degrees phase offset.
  Decoding A/B transitions gives direction + 4x resolution.
  A___----____----   <- channel A
  B_----____----_   <- channel B (90 deg shifted)
  Rising edge of A with B=0: forward. B=1: reverse.

RESOLUTION vs ACCURACY:
  Resolution: smallest detectable motion (counts/rev).
  Accuracy:   actual angular error (depends on disk quality, bearing).
  High resolution != high accuracy. Eccentricity causes periodic error.
```

### IMUs (Inertial Measurement Units)

IMUs measure angular rate (gyroscope) and specific force (accelerometer).
Modern IMUs are MEMS — microelectromechanical systems on a silicon chip.

```
IMU COMPONENTS:
===============

MEMS ACCELEROMETER:
  A proof mass suspended by springs on a chip.
  Acceleration deflects the mass; measured by capacitance change.
  Measures: specific force = a_true + g
            (cannot separate true acceleration from gravity!)
  Noise model: white noise + bias + scale factor error.

MEMS GYROSCOPE:
  Coriolis-effect sensor: vibrating proof mass.
  When rotated, Coriolis force deflects the mass perpendicular to vibration.
  Measures: angular rate (rad/s).
  Does NOT measure angle directly. Angle = integral of rate.
  Problem: integration accumulates drift over time.

IMU FUSION (typical 6-DOF IMU: 3-axis accel + 3-axis gyro):
  Gyro: low noise, short-term accurate, long-term drifts.
  Accel: long-term stable (gravity is constant), short-term noisy.
  Fusion goal: best of both worlds.
```

### IMU Noise Model and Allan Variance

```
NOISE TERMS (per axis, gyro example):
  n(t) = bias + random_walk(t) + noise(t)

  Angle Random Walk (ARW):    sqrt(rad/s) -- white noise on rate
  Bias Instability:           rad/s -- slow drift of zero offset
  Rate Random Walk (RRW):     rad/s/sqrt(s) -- slow random walk of bias
  Quantization noise:         digital resolution of ADC

ALLAN VARIANCE (sigma_A vs tau):
  Standard characterization plot: log-log of sigma_A vs integration time tau.

  tau:  0.001 s    -> dominated by quantization noise
  tau:  0.01-1 s   -> white noise floor (ARW)
  tau:  ~1-100 s   -> bias instability minimum (best operating point)
  tau:  >100 s     -> rate random walk dominates (increases with tau)

  A good IMU has a low bias instability minimum (< 1 deg/hr for tactical grade).
  Consumer MEMS: 10-100 deg/hr. Tactical MEMS: 1-10 deg/hr.
  Navigation grade (fiber optic gyro): 0.001-0.01 deg/hr.
```

---

## Exteroceptive Sensors

### LiDAR (Light Detection and Ranging)

LiDAR measures distance by timing laser pulses. The workhorse of mobile robot localization.

```
LIDAR OPERATING PRINCIPLES:
============================

TIME-OF-FLIGHT (ToF):   d = c * t / 2
  Pulse laser -> measure round-trip time.
  Accurate at long range. Limited by pulse repetition rate.
  Examples: Velodyne VLP-16, Ouster OS1, Livox Mid-360.

FMCW (Frequency-Modulated Continuous Wave):
  Chirp signal -> measure beat frequency between transmitted and received.
  Also measures radial velocity (Doppler).
  Better for moving targets. More complex.
  Examples: Aeva Aeries II, Mobileye Iris+ (automotive).

PHASE-SHIFT:
  Continuous wave, measure phase offset.
  Short range only (<100 m). Used in some 2D LiDAR.

2D vs 3D LIDAR:
+------------------+-----------------------------------------+
| 2D (planar)      | Spinning laser in one plane.            |
|                  | Single ring. Good for indoor nav.       |
|                  | Examples: SICK TiM, Hokuyo URG.         |
+------------------+-----------------------------------------+
| 3D (multi-beam)  | Multiple laser beams at different       |
|                  | vertical angles -> point cloud.         |
|                  | 16, 32, 64, 128 beams common.           |
|                  | Examples: Velodyne HDL-64, Ouster OS2.   |
+------------------+-----------------------------------------+
| Solid-state 3D   | No mechanical rotation.                 |
|                  | MEMS mirror or VCSEL array.             |
|                  | Smaller, cheaper, longer lifespan.      |
|                  | Examples: Livox Avia, Hesai AT128.      |
+------------------+-----------------------------------------+

POINT CLOUD OUTPUT:
  Each laser return -> (x, y, z, intensity, ring_id, timestamp).
  Velodyne VLP-16: 16 rings, 300,000 points/sec, 100m range.
  Ouster OS2-128: 128 rings, 2.6M points/sec, 240m range.
```

### Cameras

```
MONOCULAR CAMERA:
  Single RGB sensor. Cheap, lightweight.
  No direct depth. Depth requires scale estimation or fusion with IMU/LiDAR.
  Used in: visual SLAM (ORB-SLAM3), object detection, inspection.
  Key parameters: focal length (f), principal point (cx, cy), distortion (k1,k2,p1,p2).

STEREO CAMERA:
  Two cameras, known baseline b (separation).
  Depth from disparity: Z = f * b / disparity
  Good depth up to ~5-10 * baseline distance.
  Semi-Global Matching (SGM) algorithm for disparity computation.
  Examples: ZED 2, Intel RealSense D435 (IR-assisted stereo), Stereolabs ZED X.

RGB-D (STRUCTURED LIGHT):
  IR projector emits dot pattern. IR camera captures pattern deformation.
  Depth from triangulation between projector and camera.
  Indoor only (sunlight saturates IR). Range: 0.2 - 5 m.
  Examples: Microsoft Kinect, Intel RealSense (earlier models).

RGB-D (ACTIVE STEREO / ToF):
  ToF: each pixel measures phase shift of modulated IR. Real depth per pixel.
  More robust to sunlight. Range up to 10-15 m.
  Examples: Azure Kinect, Orbbec Astra, newer RealSense models.

EVENT CAMERA:
  Not a frame camera. Each pixel fires independently when brightness CHANGES.
  Output: stream of (x, y, timestamp, polarity) events.
  No motion blur. Dynamic range >140 dB (vs 60 dB standard cameras).
  Microsecond latency per event.
  Useful for: high-speed tracking, HDR environments, neural interface.
  Challenge: algorithms must be redesigned for event data.
  Examples: Prophesee EVK4, DAVIS346.
```

### Force/Torque Sensors

```
6-AXIS F/T SENSOR (wrist-mounted):
  Measures: Fx, Fy, Fz (forces) + Tx, Ty, Tz (torques).
  Principle: strain gauges on a mechanical structure.
    - Applied force deforms the structure.
    - Strain gauge = resistor whose resistance changes with strain.
    - Wheatstone bridge circuit converts strain to voltage.
  Located between robot wrist and end-effector.
  Applications: assembly insertion, surface following, surgery, grinding.

SPECIFICATIONS:
  Range:       +/- 50 N to +/- 2000 N (forces), +/- 5 N*m to +/- 200 N*m (torques)
  Resolution:  ~0.01 N, ~0.001 N*m
  Bandwidth:   0-1 kHz (limited by mechanical structure resonance)
  Overload:    rated to survive 5-10x overload (crash protection)

EXAMPLES: ATI Gamma (standard), Robotiq FT 300S, OnRobot HEX-E.

JOINT TORQUE SENSING (cobots only):
  Each joint has its own torque sensor.
  Enables whole-arm collision detection (not just wrist).
  Franka Panda, KUKA iiwa, Kinova Gen3 have this.
  Allows compliant behavior throughout the arm, not just at tool tip.
```

---

## Sensor Comparison Table

| Sensor | Range | Resolution | Hz | Cost | Failure modes |
|--------|-------|------------|-----|------|---------------|
| Optical encoder | N/A | 12-20 bit | 1-10 kHz | $ | Dust, shock, vibration |
| Magnetic encoder | N/A | 12-16 bit | 1-10 kHz | $ | Strong magnetic fields |
| MEMS IMU (consumer) | N/A | 16 bit | 100-1000 Hz | $ | Bias drift, vibration |
| MEMS IMU (tactical) | N/A | 16-24 bit | 100-4000 Hz | $$ | Vibration, temperature |
| 2D LiDAR | 0.1-30 m | 1-10 mm | 10-50 Hz | $$ | Dust, rain, glass |
| 3D LiDAR (16-beam) | 0.5-100 m | 1-3 cm | 10-20 Hz | $$$ | Rain, fog, glass |
| Monocular camera | N/A | pixel | 30-120 Hz | $ | Lighting, blur |
| Stereo camera | 0.2-10 m | ~1% of depth | 30-90 Hz | $$ | Textureless surfaces |
| RGB-D (structured light) | 0.2-5 m | 1-5 mm | 15-90 Hz | $$ | Sunlight, reflections |
| 6-axis F/T sensor | 0-2000 N | 0.01 N | 100-1000 Hz | $$$$ | Overload, fatigue |
| Event camera | N/A | pixel | 1 MHz event | $$$$ | High cost, new algorithms |

---

## Sensor Fusion

Single sensors are noisy, biased, or incomplete. Sensor fusion combines multiple
measurement streams to obtain a better state estimate than any sensor alone.

### Kalman Filter (Linear Systems)

The Kalman filter is the optimal linear state estimator for Gaussian noise. Every
other fusion method in robotics is a variation on this.

```
STATE ESTIMATE: x (e.g., position + velocity + orientation)
PROCESS MODEL: x_{k+1} = A * x_k + B * u_k + w_k
MEASUREMENT MODEL: z_k = H * x_k + v_k

where:
  A: state transition matrix (how state evolves without input)
  B: control input matrix
  u_k: control input (e.g., commanded velocity)
  H: measurement matrix (maps state to what sensor observes)
  w_k ~ N(0, Q): process noise (model uncertainty)
  v_k ~ N(0, R): measurement noise (sensor noise)
  Q: process noise covariance
  R: measurement noise covariance

TWO STEPS:

PREDICT:
  x_k|k-1 = A * x_{k-1} + B * u_k         (propagate state estimate)
  P_k|k-1 = A * P_{k-1} * A^T + Q          (propagate uncertainty covariance)

UPDATE (when measurement z_k arrives):
  K_k = P_k|k-1 * H^T * (H * P_k|k-1 * H^T + R)^{-1}    (Kalman gain)
  x_k = x_k|k-1 + K_k * (z_k - H * x_k|k-1)             (correct estimate)
  P_k = (I - K_k * H) * P_k|k-1                          (update covariance)

KALMAN GAIN INTUITION:
  K_k = P_predicted / (P_predicted + R)   (simplified scalar case)
  K near 0: trust prediction, ignore measurement (sensor very noisy).
  K near 1: trust measurement, ignore prediction (model very uncertain).
  K is computed optimally every step -- no manual tuning needed.
```

### Extended Kalman Filter (EKF)

Robot state estimation is nonlinear (IMU orientation uses quaternions, camera
geometry involves projections). EKF linearizes at the current estimate:

```
EKF MODIFICATION:
  Replace A with: F = df/dx |_{x_{k-1}}   (Jacobian of process model at x)
  Replace H with: H = dh/dx |_{x_{k|k-1}} (Jacobian of measurement model at x)

  Otherwise the predict/update equations are identical to standard KF.

  COST: one Jacobian computation per step.
  RISK: linearization error causes filter inconsistency if nonlinearity is large.

  Used in: EKF-SLAM, IMU pre-integration, GPS/IMU fusion, visual-inertial odometry.
```

### Complementary Filter (IMU + Encoder)

For robots with encoders and IMU, the complementary filter is simpler and computationally
cheap. It exploits the complementary noise properties of gyro (good short-term) and
accelerometer (good long-term):

```
COMPLEMENTARY FILTER:

  angle = alpha * (angle + gyro * dt)  +  (1-alpha) * accel_angle

  where:
    alpha: blend factor (0.95-0.99 typical)
    gyro * dt: angle from integrating gyroscope (fast, drifts)
    accel_angle: angle from accelerometer gravity vector (slow, stable)

  At alpha=0.98:
    98% weight on gyro integration (fast transients tracked)
    2% weight on accelerometer correction (drift corrected slowly)

FREQUENCY DOMAIN INTUITION:
  Gyro: highpass filter (believe gyro at high frequency / fast motion)
  Accel: lowpass filter (believe accel at low frequency / steady state)
  Complementary: highpass(gyro) + lowpass(accel) = allpass (covers all frequencies)
```

### Sensor Fusion Architecture for a Mobile Robot

```
INPUTS:
  Wheel encoders (100 Hz)
  IMU (200 Hz)
  LiDAR (10-20 Hz)
  Camera (30 Hz)

FUSION PIPELINE:

  IMU + Wheel encoder                LiDAR / Camera
  -------------------                -------------------
  Complementary filter          Scan matching / Feature tracking
  or EKF                        Loop closure detection
  -> Odometry (high rate,        -> SLAM pose graph update
     100-200 Hz, drifts)        (low rate, but globally consistent)
         |                               |
         +-----------> fuse <------------+
                          |
                    Final pose estimate
                    (continuous, globally consistent)
```

This is the **eventual consistency with authoritative reconciliation** pattern from distributed systems: high-frequency local state updates (odometry) accumulate drift unboundedly, and periodic low-frequency authoritative corrections (SLAM loop closure, GPS fix) reset accumulated error across the entire trajectory. The same pattern appears in vector clock reconciliation, optimistic concurrency control with periodic checkpoints, and any system where local operations proceed optimistically until a global consistency check corrects accumulated divergence.

---

## Calibration

Sensors need calibration before use. This is not optional.

```
ENCODER CALIBRATION:
  Homing: move to hard stop or index mark to establish absolute reference.
  Gear backlash compensation: measure hysteresis, add to control law.

CAMERA INTRINSIC CALIBRATION (Zhang's method):
  Capture 15-20 images of a checkerboard pattern from different angles.
  Solve for: focal length (fx, fy), principal point (cx, cy), distortion (k1,k2,p1,p2).
  Tool: OpenCV calibrateCamera(), ROS camera_calibration package.

STEREO EXTRINSIC CALIBRATION:
  Calibrate each camera intrinsically.
  Then calibrate the relative transform between cameras (R, T).
  Tools: OpenCV stereoCalibrate(), Kalibr (ETH toolkit).

IMU-CAMERA CALIBRATION (for visual-inertial SLAM):
  Find time offset and spatial transform between IMU and camera.
  Tool: Kalibr (ETH), Allan variance first to characterize IMU noise.

LiDAR-CAMERA CALIBRATION:
  Find the rigid transform between LiDAR frame and camera frame.
  Tools: lidar_camera_calibration (ROS), targetless methods using scene geometry.
```

---

## Decision Cheat Sheet

| Need | Sensor Choice |
|------|---------------|
| Joint angle, high accuracy | Optical encoder (absolute for cobots) |
| Joint angle, harsh environment | Magnetic encoder |
| Robot orientation (fast) | MEMS IMU + complementary filter |
| Robot orientation (accurate, slow) | EKF fusing IMU + encoder |
| Indoor localization (2D) | 2D LiDAR + scan matching |
| Outdoor / autonomous vehicle 3D map | 3D LiDAR (Ouster, Velodyne) |
| Visual features for SLAM | Monocular or stereo camera |
| Dense depth indoors | RGB-D (RealSense D435, Azure Kinect) |
| Contact force for assembly | Wrist-mounted 6-axis F/T sensor |
| Compliant whole-arm contact | Cobots with joint torque sensors (Franka, iiwa) |
| High-speed visual tracking | Event camera |
| Sensor fusion, linear system | Kalman filter |
| Sensor fusion, nonlinear (robot pose) | EKF or UKF |
| IMU + camera no-drift fusion | Visual-inertial odometry (ORB-SLAM3-Inertial, VINS-Mono) |

---

## Common Confusion Points

**"Accelerometer measures acceleration" — partial truth**
An accelerometer measures specific force = a_true - g. At rest on a table, it reads
+9.81 m/s^2 upward (supporting its weight against gravity), not 0. You must subtract
the gravity component (estimated from orientation) to get true linear acceleration.
This is why IMU orientation estimate is needed before integrating to velocity.

**Encoder resolution vs position accuracy**
A 20-bit encoder has 2^20 = 1,048,576 counts/rev. But gear backlash may be 0.1 deg.
The encoder resolution is far beyond the mechanical precision of the transmission.
Resolution and accuracy are not the same; the weakest link in the chain dominates.

**2D LiDAR for navigation vs 3D for mapping**
2D LiDAR is sufficient for flat-floor indoor navigation (most warehouse robots).
3D LiDAR is needed when the robot navigates over uneven terrain, stairs, or needs
to understand vertical structure. Cost difference is significant (5-10x).

**RGB-D range limitations**
Structured-light RGB-D (Kinect-style) fails outdoors because sunlight saturates the
IR sensor. ToF-based depth cameras work better but have lower resolution. Neither
works well on reflective or transparent surfaces (mirrors, glass, water). For these
cases, stereo vision with texture or LiDAR is needed.

**IMU drift is inevitable**
No MEMS IMU is drift-free. Integrating gyroscope once gives angle (drifts in minutes).
Integrating accelerometer twice gives position (drifts in seconds). Visual-inertial
systems correct this by periodically anchoring IMU integration to visual features.
Dead-reckoning with IMU alone is only useful over short time horizons (<30 seconds).
