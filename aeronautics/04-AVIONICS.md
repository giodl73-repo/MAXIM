# 04 — Avionics

## Navigation, Autopilot, Sensor Fusion, Data Buses, Displays, Surveillance

---

## Big Picture: Avionics Architecture

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                          AVIONICS SYSTEM STACK                               │
├──────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  SENSORS (physical world → data)                                             │
│   Air Data: pitot-static → ADC (Vt, Mach, altitude, VSI, AOA)               │
│   Inertial:  IMU (gyros + accels) → IRU/IRS (position, velocity, attitude)   │
│   Radio Nav: VOR, ILS LOC/GS, DME, ADF, GPS/GNSS, RA (radio altimeter)      │
│   Vision/LIDAR: enhanced vision (EVS), synthetic vision (SVS)                │
│                              │                                               │
│                              ▼                                               │
│  NAVIGATION COMPUTERS                                                        │
│   Air Data / Inertial Reference System (ADIRS): fuses air data + inertial    │
│   GPS receiver: pseudorange → position; RAIM integrity                       │
│   Sensor fusion (Kalman filter): GPS/INS hybrid → blended solution           │
│                              │                                               │
│                              ▼                                               │
│  FLIGHT MANAGEMENT SYSTEM (FMS)                                              │
│   Navigation database (NAVDB): airways, fixes, procedures, terrain           │
│   Route management: LNAV (lateral) + VNAV (vertical) profile computation     │
│   Performance computation: cost index, step climb, speed schedule            │
│   RNAV/RNP: required navigation performance on approach/en route             │
│                              │                                               │
│                              ▼                                               │
│  AUTOPILOT / AUTOTHROTTLE / FBW                                              │
│   Outer loops: AP (altitude/speed/heading hold) → FBW inner loops           │
│   Flight Director (FD): guidance bars displayed to pilot for hand-flying     │
│   Autothrottle (AT): thrust management (CLMB/CRZ/SPD modes)                 │
│                              │                                               │
│                              ▼                                               │
│  DISPLAYS + HUMAN INTERFACE                                                  │
│   PFD: Primary Flight Display (attitude, speed, altitude, vertical speed)    │
│   ND: Navigation Display (map, weather, TCAS, waypoints)                     │
│   ECAM/EICAS: systems monitoring (engines, fuel, hydraulics, pressurization) │
│   HUD: Head-Up Display (military + some commercial)                          │
│                              │                                               │
│                              ▼                                               │
│  SURVEILLANCE / COMMUNICATION                                                │
│   TCAS II / ACAS-X: collision avoidance                                      │
│   ADS-B Out/In: automatic position broadcast + reception                     │
│   ILS/GLS/MLS: precision approach guidance                                   │
│   VHF COM / HF COM / ACARS / SELCAL / datalink (CPDLC)                      │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## 1. Avionics Architecture: Federated vs IMA

```
FEDERATED ARCHITECTURE (legacy — pre-1990s):
  One box = one function: separate autopilot computer, TCAS box, FMS, ADC...
  Each box has own processor, power supply, I/O; interconnected by point-to-point wiring
  Advantages: simple certification (one function per DO-178 approval); isolation
  Disadvantages: weight (many boxes), inflexibility, large wiring harness

INTEGRATED MODULAR AVIONICS (IMA) — ARINC 651 / DO-297:
  Shared computing resource: partitioned CPUs run multiple apps on common hardware
  ┌───────────────────────────────────────────────────────────┐
  │  COMMON COMPUTING RESOURCE (CCR / GPM — General Processing│
  │  Module)                                                  │
  │  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐      │
  │  │ FMS App  │ │ TCAS App │ │ FCC App  │ │ BITE App │     │
  │  │ (DAL B)  │ │ (DAL B)  │ │ (DAL A)  │ │ (DAL C)  │     │
  │  └──────────┘ └──────────┘ └──────────┘ └──────────┘     │
  │            ARINC 653 OS — temporal + spatial partitioning │
  │            Time budget per partition; no cross-partition  │
  │            memory; hard real-time scheduling              │
  └───────────────────────────────────────────────────────────┘
  Advantages: reduced weight/boxes, easier upgrades, common sparing
  Challenges: certification complexity (mixed DAL on same hardware); ARINC 653

**Software verification bridge:** DO-178C's DAL-A MC/DC (Modified Condition/Decision Coverage) is the most stringent test coverage criterion in production use — it requires that every boolean sub-condition independently affects every decision outcome. This is strictly stronger than branch coverage (DAL-B), statement coverage (DAL-C), or any typical CI/CD coverage metric. The verification hierarchy for DAL-A also includes formal methods: model checking (exhaustive state exploration) and theorem proving for safety-critical properties. IEC 61508 Safety Integrity Levels (SIL 1-4) apply the same graduated rigor to industrial control systems.

DO-178C — SOFTWARE ASSURANCE:
  Design Assurance Levels (DAL): A (catastrophic) → E (no safety effect)
  DAL-A: MC/DC (Modified Condition/Decision Coverage) + independence review
  DAL-B: decision coverage required
  DAL-C: statement coverage
  Verification: review, analysis, testing; tool qualification (DO-330)

ARINC 653 RTOS:
  Time-partitioning: each application gets fixed CPU time slice; cannot exceed it
  Space-partitioning: memory regions isolated; one app cannot corrupt another
  Health monitoring: partition health table; error confinement at partition boundary
  Used in: VxWorks 653, LynxOS-178, PikeOS, Green Hills INTEGRITY

A380/A350/B787: full IMA; far fewer LRUs (line replaceable units) than 747
```

---

## 2. Air Data System

```
PITOT-STATIC SYSTEM:
  Pitot tube: measures stagnation (total) pressure p_t
  Static port: measures static pressure p_s
  Differential: q = p_t - p_s = dynamic pressure → airspeed

  For incompressible flow: q = ½ρV² → V_IAS = √(2q/ρ₀)  (SL density)
  Compressibility correction: CAS from isentropic relation
    p_t/p_s = (1 + (γ-1)/2 · M²)^(γ/(γ-1))
    CAS → EAS (√σ correction) → TAS

  Blockages/icing: pitot heat mandatory (FAR 25); multiple ports for redundancy
  Position error: static port location affects reading; corrected to CAS

AIR DATA COMPUTER (ADC):
  Inputs: p_t, p_s, TAT (total air temperature)
  Outputs:
    IAS / CAS: from differential pressure
    Pressure altitude: from p_s vs standard atmosphere table
    Mach number: M = √(2/(γ-1) × ((p_t/p_s)^((γ-1)/γ) - 1))
    SAT (static air temperature): T_SAT = T_TAT / (1 + (γ-1)/2 · M²) ≈ T_TAT/(1 + 0.2M²)
    TAS: V_TAS = M × a = M × √(γ·R·T_SAT)
    VSI (vertical speed indicator): altitude rate = dh/dt

TRIPLEX ADIRU (Air Data Inertial Reference Unit):
  3 independent units; pilot selects ADR1/2/3 on overhead panel
  Cross-comparison: any two agree → majority vote; disagree warning
  Unreliable airspeed procedure: manually set pitch/power from memory card

RADIO ALTIMETER (RA):
  FM-CW radar: transmit frequency-modulated continuous wave; measure Δf between
    transmit and received (reflected from ground); Δf ∝ height AGL
  Accurate 0-2500 ft AGL; used for: GPWS/TAWS terrain warnings, autoland flare
  TCAS: not radio altimeter — uses transponder replies
```

---

## 3. Inertial Navigation System (INS/IRS)

```
IMU (INERTIAL MEASUREMENT UNIT):
  3 accelerometers: measure specific force (acceleration − gravity)
  3 gyroscopes: measure angular rate

  Gyro technologies:
    Ring Laser Gyro (RLG): Sagnac effect — counter-rotating laser beams; freq diff ∝ rotation rate
      MTBF ~50,000 hrs; laser lock-in at low rates → dither mechanism
    Fiber Optic Gyro (FOG): same Sagnac principle; longer optical path via fiber coil
      Cheaper than RLG; slightly less accurate; used in IRS upgrades
    MEMS gyro: micro-electromechanical; very cheap; lower accuracy → used in AHRS, not INS
    Hemispherical Resonator Gyro (HRG): vibrating quartz shell; very high reliability
      Northrop Grumman SIRU; used in spacecraft, no moving parts

STRAPDOWN INS INTEGRATION:
  Old platform INS: gimbal-mounted, keeps platform level; gyros measure rotation of platform
  Strapdown: IMU fixed to airframe; software does what gimbals did
  Integration steps:
    1. Gyro measurement → quaternion update → body→nav attitude transform
    2. Accel measurement → rotate to navigation frame
    3. Subtract gravity model (WGS-84 normal gravity + Eötvös correction)
    4. Integrate once → velocity (North, East, Down)
    5. Integrate again → position (lat, lon, alt)

  Error growth: INS position error grows with time (gyro drift, accel bias)
    Typical: 0.1-1 nmi/hr for high-quality RLG INS (ADIRS-class)
    Error mechanism: gyro drift → attitude error → residual gravity component → velocity error → position error
    Schuler oscillation: 84-minute period (pendulum length = Earth radius); dominates bounded error

**Why Kalman:** The Kalman filter is the optimal linear estimator (minimum variance) for a system with Gaussian process noise (INS drift) and measurement noise (GPS). It is the recursive form of weighted least squares, updating the state estimate as each GPS measurement arrives. The innovation sequence (GPS position minus INS predicted position) is the key diagnostic: if innovations are white noise, the filter is correctly tuned; correlated innovations indicate model mismatch. See control-theory/04-KALMAN-FILTER.md for the full treatment.

GPS/INS COUPLING (Kalman filter integration):
  Loosely coupled: GPS provides position/velocity; INS position/velocity as state
  Tightly coupled: GPS raw pseudoranges; better for degraded GPS (< 4 SVs)
  Ultra-tightly coupled: correlator-level integration (classified/research)

  State vector: [Δpos_N, Δpos_E, Δpos_D, Δv_N, Δv_E, Δv_D, Δφ, Δθ, Δψ, δb_a (3), δb_g (3)]
    = 15 error states
  Measurement: GPS position − INS position = innovation
  Filter: corrects INS solution continuously; reset Schuler oscillation

  During GPS outage: INS coasts on last Kalman state estimates; errors grow
  In RNP approach: 10 sec GPS outage tolerance for CAT IIIB autoland
```

---

## 4. GPS/GNSS

```
GPS SIGNAL STRUCTURE:
  Constellation: 30+ satellites in 6 orbital planes (MEO, ~20,200 km, 12-hr orbit)
  Two civilian frequencies: L1 (1575.42 MHz, C/A code), L5 (1176.45 MHz, safety-of-life)
  PRN codes: pseudo-random noise spreading codes; unique per satellite; CDMA
  Navigation message: satellite ephemeris, clock correction, ionospheric model; 50 bps

PSEUDORANGE MEASUREMENT:
  Receiver correlates received PRN with local replica → timing offset
  Pseudorange ρ_i = c · Δt_i = distance + receiver clock error × c
  4 pseudoranges → 4 unknowns: (x, y, z, t_receiver)  ← GDOP = Geometric Dilution of Precision
  PDOP (position): want < 2 (excellent) < 6 (acceptable)

ERROR SOURCES:
  Ionospheric delay: ~2-10 m; model (Klobuchar) or dual-frequency removal
  Tropospheric delay: ~2.5 m zenith; Saastamoinen model
  Multipath: reflections off terrain/buildings; aviation antenna design minimizes
  Receiver noise: ~0.3-1 m; reduced by carrier smoothing (Hatch filter)
  Satellite geometry: GDOP multiplies all errors
  Total SPS (civil L1): ~2-5 m RMS

AUGMENTATION SYSTEMS:
  SBAS — Satellite-Based Augmentation System:
    Ground reference stations observe GPS errors → upload correction messages via geostationary sat
    USA: WAAS; Europe: EGNOS; Japan: MSAS; India: GAGAN
    Provides: differential corrections + UDRE + ionospheric grid + integrity
    Enables: LPV-200 approaches (≈ CAT I ILS equivalent); 200 ft DH, 1/2 sm vis
    WAAS: 7.6 m horizontal, 3 m vertical (95%) → enables LNAV/VNAV and LPV
  GBAS — Ground-Based Augmentation System:
    Local ground station at airport; broadcasts VHF corrections
    GLS (GBAS Landing System): CAT I/II/III approaches via single GBAS station
    One GBAS covers all runways at airport vs ILS per runway
  RAIM — Receiver Autonomous Integrity Monitoring:
    Overdetermined solution: use extra SVs to self-check consistency
    Fault detection: detect satellite failure before it affects navigation
    Fault exclusion (RAIM FD+FE): identify and remove faulty SV
    Protection level (PL): statistical bound on position error; must be < alert limit

GALILEO / GLONASS / BeiDou:
  Multi-constellation receiver now standard; redundancy + improved geometry
  Multi-frequency: removes ionospheric error directly (L1/L5 dual freq)
  ARAIM: advanced RAIM using multiple constellations → enables LPV-200
```

---

## 5. Flight Management System (FMS)

```
FMS FUNCTIONS:
  1. Navigation: position determination (GPS/IRS blend); route computation
  2. Performance: fuel prediction, step climb optimization, cost index
  3. Guidance: LNAV/VNAV profile; autothrottle speed references
  4. Display: ND map; CDU/MCDU interface

NAVIGATION DATABASE (NAVDB):
  Updated every 28 days (AIRAC cycle); Jeppesen or Navtech supply
  Contains: runways, waypoints, airways, SIDs/STARs, approaches, airways, notams
  Stored as ARINC 424 format records
  Protected: FMS cannot modify NAVDB; only certified update process

RNP (REQUIRED NAVIGATION PERFORMANCE):
  Performance-based navigation (PBN): aircraft must prove navigation accuracy in real time
  RNP value = lateral accuracy (95%); e.g., RNP 0.1 = 0.1 nmi accuracy (95%)
  RNAV: uses any navigation source to meet accuracy; no onboard monitoring
  RNP: same as RNAV + onboard alerting when performance not met
  RNP AR (Authorization Required): RNP 0.1 + RF (radius-to-fix) legs → curved approaches
    Enables approaches around mountains (e.g., Innsbruck, Kathmandu, Queenstown)
  VNAV: vertical path computation; meets required descent profile

FMS CDU (Control Display Unit) / MCDU:
  12-character alphanumeric lines; LSK (line select keys) for data entry
  Pages: INIT (route initialization), F-PLN (flight plan), PERF (performance), PROG (progress)
  Cost index (CI): 0 = minimum fuel; 99/100 = minimum time
    CI = cost of time ($/min) / cost of fuel ($/kg or $/lb)
    → Optimizes trade between fuel cost and crew/time cost for airline

LNAV (Lateral Navigation):
  Path: WPT-to-WPT great circle legs; holding patterns; procedure legs (type A-Z per ARINC 424)
  Transition: RF leg (radius to fix), DF leg (direct to fix), etc.
  Track keeping: FMS computes cross-track error (XTE); drives autopilot lateral mode

VNAV (Vertical Navigation):
  Climb profile: engine thrust limit → climb speed schedule (250 kt < 10,000 ft; then IAS/Mach)
  Cruise: step climb to optimal FL; constant Mach
  Descent: top of descent (TOD); path angle (typically 3° nominal); IDLE thrust preferred
    Economy descent: FMS manages idle + speed brake to arrive at restriction
  VNAV constraints: at/above/below altitude; speed constraints at waypoints
```

---

## 6. Autopilot and Autothrottle Architecture

```
AUTOPILOT CONTROL LAW ARCHITECTURE:
  Inner loop (FBW): attitude control (roll, pitch); bandwidth ~2-5 Hz
  Outer loop (AP): reference commands to inner loop; bandwidth ~0.1-0.5 Hz

  ┌──────────────────────────────────────────────────────────────────┐
  │  OUTER LOOP (AUTOPILOT)                                          │
  │  Alt hold: altitude → VS → pitch command → inner loop            │
  │  Hdg hold: heading → bank angle cmd → roll inner loop            │
  │  Spd hold: airspeed error → pitch or throttle (VNAV)             │
  │  ILS: localizer → roll; glideslope → pitch (inner coupling)      │
  │                                                                  │
  │  INNER LOOP (FBW / attitude control)                             │
  │  Pitch: θ_cmd → q_cmd → elevator; gains vary with Mach/alt       │
  │  Roll: φ_cmd → p_cmd → aileron + rudder; roll/yaw coordination   │
  │                                                                  │
  │  AUTOTHROTTLE (AT):                                              │
  │  Speed mode: target CAS/Mach → throttle PID                      │
  │  Thrust mode: N1/EPR target → throttle PID (for CLMB, MCT, IDLE)│
  └──────────────────────────────────────────────────────────────────┘

AUTOPILOT MODES (Airbus A320-family nomenclature):
  HDG/VS: heading-select + vertical speed; pilot sets both
  NAV:    LNAV from FMS
  OP CLB / OP DES: open-climb/descent at pilot-set speed; AP holds speed
  CLB/DES: managed mode; FMS VNAV profile
  APPR:   ILS localizer + glideslope capture and track
  LAND:   autoland; CAT II/III; flare + rollout modes

AUTOLAND (CAT III):
  Sequence: APP → LAND → FLARE → ROLLOUT
  LOC: captures localizer; tracks to centerline at touchdown
  G/S: captures glideslope; follows to flare height (~50 ft RA)
  FLARE: at 50 ft RA, pitch up 2-3°; throttle to idle; sink rate reduction
  ROLLOUT: nose gear steering + differential braking to runway centerline
  Redundancy: requires dual AP engaged; triple IRU; dual LOC/G/S signals
  Fail-passive vs fail-operational: fail-passive → pilot takes over after failure;
    fail-operational → second system takes over; allows CAT IIIb (15 m DH or zero)

FLIGHT DIRECTOR (FD):
  Guidance bars on EADI/PFD: show pilot where to point aircraft
  Computed by FMS + AP computer; pilot flies to bars manually
  Not autopilot: FD gives guidance; pilot controls surfaces
  Useful for: IFR approaches without engaging full AP; training
```

---

## 7. ILS, GLS, and Approach Systems

```
ILS — INSTRUMENT LANDING SYSTEM:
  Localizer (LOC): VHF 108-112 MHz; 150 Hz vs 90 Hz AM modulation depth difference
    Course deviation: fly toward greater 90 Hz signal
    Beam width: ±2.5° (full deflection); provides azimuth guidance on final
    Course width (half) ≈ 3° → at DH 200 ft, lateral ±75 ft roughly
  Glideslope (G/S): UHF 329-335 MHz; same 90/150 Hz DDM scheme but vertical
    Angle: 3° standard (2.5° to 3.5° variable by airport geometry)
    Beam width: ±0.175° → tighter than LOC (precision required vertically)
  Marker beacons: OM/MM/IM at set distances from threshold (largely replaced by DME)
  DME/LOC: distance from runway via collocated DME transponder

ILS CATEGORIES:
  Category I:   DH 200 ft; visibility 800 m (1/2 sm); good ILS + basic AP
  Category II:  DH 100 ft; vis 400 m; dual AP; enhanced equipment
  Category IIIa: DH 50 ft; vis 200 m; autoland; redundant systems
  Category IIIb: DH 15 ft (or zero); vis 50 m; fail-operational autoland
  Category IIIc: zero-zero (discussed but not operationally certified)

GLS — GBAS LANDING SYSTEM:
  GBAS ground station broadcasts: GPS differential corrections + approach path data
  Aircraft FMS computes precise guidance from GBAS corrections
  Advantages: one station covers all runways; no localizer/glideslope antennas per runway;
    programmable glidepath angle; offset approaches
  Status: CAT I approved; CAT III in certification phase (2020s)
  Frankfurt, Zürich, Brisbane: early GBAS deployments

RNAV APPROACH MINIMA:
  LNAV: lateral only; MDA (min descent altitude); GPS + altimeter
  LNAV/VNAV: GPS lateral + Baro-VNAV or SBAS vertical; DH ~300 ft
  LPV (Localizer Performance with Vertical guidance): WAAS/SBAS; DH 200 ft → CAT I equiv
  LPV-200: WAAS LPV; exact CAT I equivalent; 98% US instrument runways now LPV

RADAR ALTIMETER (RA):
  Used in: autoland flare initiation (50 ft), GPWS/EGPWS (terrain alerts), minima callout
  FM-CW: transmitted freq modulated over ±60 MHz; received delay → height
  Two independent RAs on CAT III aircraft (redundancy)
```

---

## 8. TCAS II and Collision Avoidance

```
TCAS II — TRAFFIC COLLISION AVOIDANCE SYSTEM (version 7.1):
  Interrogates nearby transponders on 1030 MHz (Mode C/S replies on 1090 MHz)
  Builds traffic picture: range, bearing, altitude of nearby aircraft
  TA (Traffic Advisory): "Traffic, Traffic" — visual alert on ND, no evasive action
  RA (Resolution Advisory): "Climb, climb" or "Descend, descend" — mandatory maneuver
    Pilots must follow RA immediately; ATC instruction secondary during RA
  Coordinated RAs: two TCAS units communicate via Mode S data link (1090/1030 MHz)
    Ensure complementary maneuvers (one climbs, one descends)

TCAS LOGIC:
  CPA (Closest Point of Approach): computed in range and altitude rate
  TA threshold: τ_TA = 20-48 sec depending on altitude
  RA threshold: τ_RA = 15-35 sec depending on altitude
  Vertical rate RA: command +/- 1500, 2500, or modified vertical speed

VERSION 7.1 improvements over 7.0:
  "Adjust vertical speed" RA: avoid aggressive maneuver if traffic above resolution
  Reversal logic improvement: fewer unnecessary reversals

ACAS-X (FAA/Eurocontrol next generation):
  Tables replace rule-based logic → more optimal advisories
  Handles: drones (uUAS), surface ops, reduced separation scenarios
  ACAS Xa: conventional aircraft; ACAS Xo: oceanic; ACAS Xu: unmanned
  Status: ACAS Xa under development; ICAO SARPs revision in progress

ADS-B OUT (Automatic Dependent Surveillance — Broadcast):
  Aircraft broadcasts its own position (from GPS), velocity, flight ID via 1090ES squitter
  1090 MHz Extended Squitter (ES): 112-bit message; position accuracy NACp ≥ 8 (< 0.05 nmi)
  FAA mandate: ADS-B Out required in Class A/B/C + above 10,000 ft since Jan 2020
  Update rate: 1 Hz; precise timing relative to GPS

ADS-B IN:
  Receive neighbors' broadcasts; display on cockpit displays (CDTI - Cockpit Display of Traffic)
  Enables: airborne separation; FIM (Flight Interval Management); SURF TA
  Not yet TCAS equivalent (no RAs from ADS-B In alone)

MULTILATERATION (MLAT):
  Ground stations: 4+ synchronized receivers; measure TDOA (time difference of arrival)
  Compute aircraft position without aircraft broadcasting — passive surveillance
  Airport surface monitoring; approach path surveillance where ADS-B insufficient
```

---

## 9. Aircraft Data Buses

```
ARINC 429 (legacy; still most common):
  Unidirectional: one transmitter → up to 20 receivers; separate wire pairs per direction
  Bit rate: 12.5 kbps (low speed) or 100 kbps (high speed)
  32-bit word: 8-bit label + SDI (2-bit) + 19-bit data + SSM (2-bit) + parity (1-bit)
  Protocol: simple broadcast; no addressing; no acknowledgment
  Wire count: large aircraft has 4,000+ ARINC 429 wire pairs → weight problem
  Still used: avionics sensors (ADC, IRS) → FMS, AP, display systems

MIL-STD-1553 (military):
  Bidirectional, shared bus; commander/responder architecture
  1 MHz; 1 Mbps; TDM (time-division multiplexed)
  Deterministic timing: commander controls all bus access
  Used: military avionics, weapons systems; also some civil helicopters

ARINC 664 / AFDX (Avionics Full-Duplex Switched Ethernet):
  IEEE 802.3 Ethernet adapted for deterministic avionics use
  Switched architecture: virtual links (VL) with guaranteed bandwidth + latency
  100 Mbps (or 1 Gbps); deterministic via traffic shaping per VL
  A380, A350, B787: full AFDX backbone; replaced thousands of ARINC 429 wire pairs
  AFDX improvements over plain Ethernet: no collision (switched), bounded latency,
    integrity checks (redundant sub-nets), max frame interval enforced

  Virtual Link concept:
    Each VL has: BAG (bandwidth allocation gap = 1/bandwidth), max frame size
    Switch enforces: no VL exceeds its allocation → determinism without collisions
    Two sub-networks (A + B): every VL replicated; end system selects valid copy

CAN BUS (Controller Area Network):
  Vehicle (auto) standard; some use in aircraft: landing gear, doors, cabin systems
  Multi-master; 1 Mbps; priority-based arbitration; short frames
  Not DO-178 certified historically; CANFD (flexible data-rate) emerging

OPEN STANDARDS TREND:
  ARINC 653 + AFDX: standard IMA interconnect
  DO-178C / DO-254: software + hardware certification standards
  Future: Time-Sensitive Networking (TSN) based on 802.1Q; even higher bandwidth
```

---

## 10. Cockpit Displays

```
EFIS — ELECTRONIC FLIGHT INSTRUMENT SYSTEM:
  Replaces: analog airspeed, altimeter, HSI, gyro horizon — all on LCD screens
  PFD (Primary Flight Display):
    Attitude: artificial horizon; bank angle; pitch scale
    Speed tape: TAS/IAS scale on left; speed trend vector; mach below
    Altitude tape: right side; QNH/QFE setting; metric alt option
    Vertical speed indicator (VSI): rightmost; also TCAS RA display
    FD (flight director) bars: guidance command
    ILS deviation indicators: loc/GS crosshairs when ILS selected
    Radio altitude: numerical display below horizon < 2500 ft AGL
    Minimums bug: decision height indicator

  ND (Navigation Display):
    MAP/ARC/PLAN/VOR/ILS modes
    Map mode: moving map; aircraft centered; waypoints/airports/NDB/VOR overlaid
    Weather radar overlay: WXR range selector
    TCAS traffic: TAs (amber), RAs (red) on traffic layer
    Wind vector: current wind speed/direction

  ECAM (Airbus) / EICAS (Boeing):
    Systems monitoring: engine parameters (N1, N2, EGT, FF), fuel, hydraulics, pressurization
    Warning hierarchy: WARNING (red + continuous aural) → CAUTION (amber + chime) → ADVISORY (amber)
    Failure isolation: ECAM identifies failed system; provides checklist procedure
    ECAM actions: "ECAM ACTIONS" call → memory items + ECAM-directed non-normal checklist

HUD — HEAD-UP DISPLAY:
  Optical combiner: collimates imagery at optical infinity (focus matches outside view)
  Displays: aircraft state on glass, pilot looks through it at runway
  Applications: CAT IIIb autoland (pilot monitors HUD during rollout); EFVS (EVS sensor overlay)
  Military HUD: aiming symbology, weapon delivery cues, stores management
  Commercial HUD: FlightVision (United), HeadUp Technologies, Rockwell Collins; optional FAR 25

SYNTHETIC VISION SYSTEM (SVS):
  Database terrain model rendered from pilot perspective; always current depiction
  Shows: terrain, runways, obstacles; removes spatial disorientation risk
  Not precision nav: for situational awareness; enhances CFIT (controlled flight into terrain) prevention

ENHANCED VISION SYSTEM (EVS):
  Forward-looking infrared (FLIR) or visible camera; sensor overlay on HUD or PFD
  FAA: EFVS (enhanced flight vision system) regulations → credit for visibility below CAT I minimums
```

---

## 11. Cybersecurity in Avionics

```
ATTACK SURFACE (layered):
  ┌──────────────────────────────────────────────────────────┐
  │  CABIN / PASSENGER NETWORK (IFE, Wi-Fi)                  │
  │    Boeing 787 controversy: shared domain controller;     │
  │    firewall between cabin and avionics domains           │
  │    IFE systems: not DO-178C certified; can have vulns    │
  ├──────────────────────────────────────────────────────────┤
  │  EFB — ELECTRONIC FLIGHT BAG                             │
  │    Tablet-based: iPad/Surface with Jeppesen charts       │
  │    Class 3 EFB: installed; aviation-grade; more rigor    │
  │    Class 2 EFB: portable; software security concerns     │
  │    ACARS/datalink: FMS update via ACARS → verify/auth    │
  ├──────────────────────────────────────────────────────────┤
  │  AVIONICS NETWORK (FMS, TCAS, ADS-B, AFDX)               │
  │    ADS-B spoofing: GPS spoofing → false position in ADSB │
  │    GPS jamming: legitimate GNSS signal overwhelmed       │
  │    ACARS injection: FMS load via ACARS; data verification│
  ├──────────────────────────────────────────────────────────┤
  │  CONTROL DOMAIN (FBW, FCC, ADIRS)                        │
  │    Air-gapped from cabin; hardened physical separation   │
  │    Update path: secure ground maintenance only           │
  └──────────────────────────────────────────────────────────┘

STANDARDS:
  DO-326A: airworthiness security process standard (SAE ARP4754A equivalent for security)
  DO-356A: airworthiness security methods and considerations
  ED-202A / ED-203A: European equivalents (EUROCAE)
  FAA Order 8110.121: airworthiness security reviews in FAR 25

GPS SPOOFING / JAMMING THREAT:
  Spoofing: transmit fake GPS signals → FMS shows wrong position
  Incidents: Middle East 2019-2023; vessels in Black Sea; multiple commercial flights
  Mitigation: multi-constellation receiver; RAIM integrity monitoring; RNAV/IRS cross-check;
    inertial coasting when GPS anomaly detected; crew procedures

ADS-B SECURITY:
  No authentication in current 1090ES ADS-B Out protocol
  Ghost aircraft injection: transmit fake ADS-B messages → false traffic on ND
  Physical: 1090 MHz receiver can pick up spoofed transmissions
  Next-generation: ACAS-X uses probabilistic models; authenticated ADS-B under study
```

---

## 12. Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| IMA vs federated? | IMA: shared computing resource with ARINC 653 partitioning; reduces LRUs; harder cert |
| ARINC 429 directionality? | Unidirectional; one TX → many RX; 12.5/100 kbps; separate wire pairs each direction |
| AFDX advantage over plain Ethernet? | Switched + virtual links with guaranteed BW + latency; deterministic; dual redundant |
| Loosely vs tightly coupled GPS/INS? | Loose: GPS position/velocity; Tight: raw pseudoranges; tight works with <4 SVs |
| SBAS enables what approach type? | LPV or LPV-200 (≈CAT I ILS); 200 ft DH; 1/2 sm visibility |
| GBAS vs ILS? | GBAS: one ground station covers all runways; programmable glidepath; GLS approaches |
| TCAS II RA — what must pilot do? | Follow RA immediately; ATC instruction secondary during RA (ICAO standard) |
| ADS-B Out mandate US? | Required Jan 2020 in Class A/B/C and above 10,000 ft MSL (1090ES) |
| CAT IIIb ILS requirements? | DH 15 ft (or zero DH); 50 m vis; fail-operational autoland; redundant all systems |
| Cost index 0 vs 100? | CI=0: minimum fuel (fly slow, use less fuel); CI=100: minimum time (fly fast) |
| DAL-A coverage requirement? | MC/DC (Modified Condition/Decision Coverage) |
| Schuler period? | 84 minutes — free oscillation of a pendulum equal to Earth radius; dominates INS error |
| What does RAIM protect against? | Satellite failure causing position error; alerts pilot before exceeding protection level |
| PFD vs ND primary content? | PFD: attitude/speed/alt/VSI; ND: navigation map/weather/traffic |

---

## Common Confusion Points

**GPS gives position — but not integrity alone:** GPS hardware gives a position, but for approach navigation you need RAIM or SBAS to assure the position is actually correct (integrity). Without RAIM, a failed satellite could silently give wrong position. RAIM failure → GPS can't be used for precision approach.

**ILS CAT I/II/III is about ground equipment AND aircraft equipment:** A CAT I ILS approach requires both a CAT I-qualified ILS ground installation AND sufficient aircraft equipment. CAT IIIb requires: dual autoland, triple IRS, dual RA, specific FBW functionality. The aircraft certification (AFM) specifies what categories are approved.

**FBW inner/outer loop confusion:** The FBW system (inner loop) controls attitude. The autopilot (outer loop) commands what attitude. The FMS tells the autopilot what path to follow. These are nested control loops at different bandwidths. Pilots interact with the FMS for routing and FCP (flight control panel) for mode selection; the inner FBW loops are transparent.

**TCAS vs ADS-B:** TCAS actively interrogates Mode C/S transponders (uses radar-like interrogation); ADS-B is passive broadcast (aircraft broadcasts; others listen). TCAS is the collision avoidance system with RA authority. ADS-B provides traffic awareness but no RAs in current implementation.

**ARINC 429 word format — label first or last?** ARINC 429 sends LSB first; the 8-bit label is transmitted first (LSB of the 32-bit word), but label value is conventionally read MSB-first as an octal number. Painful bit-reversal that trips up every new avionics engineer.

**IMA mixed DAL doesn't mean lowest DAL wins:** ARINC 653 spatial/temporal partitioning ensures a DAL-C FMS app cannot corrupt a DAL-A flight control app's memory or timing. Certification shows the partition boundaries are robust — then each partition is certified independently at its own DAL level. The hardware itself must be certified at the highest DAL hosted on it.
