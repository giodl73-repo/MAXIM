# Spacecraft Design and Subsystems

## The Big Picture

A spacecraft is an integrated system of subsystems, each serving a specific function. The challenge is that every subsystem must work perfectly in an environment of vacuum, extreme temperatures, radiation, and microgravity — with no possibility of repair on most missions.

```
+------------------------------------------------------------------+
|                    SPACECRAFT SUBSYSTEM MAP                       |
+------------------------------------------------------------------+
|                                                                  |
|  STRUCTURE (S/C)    POWER (EPS)     THERMAL (TCS)               |
|  -----------        ----------      ---------                   |
|  Primary structure  Solar panels    Radiators                   |
|  Secondary struct.  Batteries       Multi-layer insulation (MLI)|
|  Separation system  Power cond.     Heat pipes                  |
|  Mechanisms         Dist. unit      Heaters/coolers             |
|                                                                  |
|  COMMS (RF/COM)     ATTITUDE (ADCS)  PROPULSION (ACS)           |
|  ---------          ----------       ----------                  |
|  High gain antenna  Star trackers    Thrusters (mono/bi/electric)|
|  Low gain antenna   Sun sensors      Fuel tank                  |
|  Transponders       Gyroscopes       Pressure transducers       |
|  Amplifiers         Reaction wheels                             |
|  Modems             Magnetometers                               |
|                                                                  |
|  PAYLOAD            C&DH            GNC                         |
|  -------            ----            ---                         |
|  Science instruments On-board comp. Trajectory planning        |
|  Mission-specific    Mass memory    Orbit determination         |
|  OBDH software      Fault management                           |
+------------------------------------------------------------------+
```

---

## Power System (EPS)

```
ELECTRICAL POWER SYSTEM
========================

  POWER GENERATION:
    Solar panels (photovoltaic): most common; 28-33% efficiency (triple-junction GaAs)
    Near-Sun: ISS generates ~84-120 kW from 2500 m² of panels
    Far from Sun: power ∝ 1/r²; Jupiter: 1/25× Earth flux; Saturn: 1/90×

    RTG (Radioisotope Thermoelectric Generator):
    ²³⁸Pu → decay heat → thermoelectric conversion
    Power density: ~4-8 W/kg
    Cassini: 870 W from 3 RTGs (1997); New Horizons: ~200 W; Perseverance: 110 W
    Limited Pu supply (DOE production); allocated only to science missions
    MMRTG (Multi-Mission): standard unit ~125 W initial

    Fuel cells: H₂ + O₂ → electricity + water
    Used: Apollo, Shuttle; not used on current missions (tanks too heavy)

  ENERGY STORAGE:
    Lithium-ion batteries: current standard; ~150-250 Wh/kg
    NiH₂ (nickel-hydrogen): legacy; ISS uses NiH₂ → being upgraded to LiIon
    Charging during sunlit period; discharge during eclipse
    Eclipse fraction: for 400 km LEO orbit, ~35 min eclipse per 92-min orbit

  POWER DISTRIBUTION:
    Regulated bus (constant voltage): most reliable; extra components
    Unregulated bus: simpler; voltage varies with solar conditions (ripple)
    Typical bus voltages: 28 V (small), 50 V, 100 V, 120 V (ISS)
    RTG: direct battery charging; no MPPT (max power point tracking)
```

---

## Thermal Control System (TCS)

```
THERMAL ENVIRONMENT
====================

  HEAT INPUTS:
    Solar flux: 1361 W/m² at 1 AU (direct solar radiation)
    Albedo (reflected Earth): ~30% of solar flux; varies with Earth coverage
    Earth IR: ~230 W/m²; important in LEO
    Internal dissipation: electronics, batteries, instruments

  HEAT REMOVAL:
    Radiation: only mechanism in vacuum (conduction requires contact; convection needs fluid)
    P = ε × σ × A × T⁴  (Stefan-Boltzmann law)
    Radiator temperature determines minimum size needed

  THERMAL DESIGN CHALLENGE:
    Sunlit side: ~120°C (stagnant) or higher if absorber
    Shadow side: -180°C (can drop to cryogenic temperatures)
    Electronics: typically 0-50°C operating range
    Solution: passive + active thermal control

  PASSIVE METHODS:
    Multi-Layer Insulation (MLI): aluminized Mylar/Kapton blankets
      Reduces radiated heat loss; ~20-30 layers; like thermos bottle
    Surface coatings: absorptance (α) / emittance (ε) ratio
      Low α/high ε: radiator (white paint, OSR — optical solar reflectors)
      High α/low ε: absorber (black paint)
    Heat pipes: capillary-driven fluid loop; spreads heat passively
      Ammonia heat pipes: common in spacecraft; no moving parts

  ACTIVE METHODS:
    Heaters: resistance heaters (survival heaters) on cold-sensitive components
    Thermostat controlled: on if < -10°C; off if > 0°C (example)
    Louvers: variable-area radiator; bi-metallic strips control opening
    Cryocoolers: Stirling cycle coolers for IR instruments (cool to 70 K)
    Fluid loops: pumped fluid (water, Freon) for large heat loads (ISS)

  DEEP SPACE THERMAL:
    Beyond Jupiter: solar flux negligible; RTG heat must be managed
    Cassini: heat pipes + louvers to distribute RTG heat + reject electronics heat
    Near Venus/Sun: sunshield (Parker Solar Probe: 11.4 cm carbon foam shield)
    Parker Solar Probe: perihelion 9 solar radii; heat shield ~1400°C sunward face
```

---

## Attitude Determination and Control (ADCS)

```
ATTITUDE DETERMINATION AND CONTROL
=====================================

  PURPOSE: Point spacecraft (instruments, antennas, solar panels, thrusters)

  ATTITUDE DETERMINATION (sensing):
    STAR TRACKER: most precise; compares star pattern to catalog
      Accuracy: 0.001° (arcseconds); autonomous identification
      Works in any attitude; autonomous "lost in space" initialization
    SUN SENSOR: simple; coarse (1°) or fine (0.001°)
      Course/acquisition: first step after anomaly
    EARTH SENSOR: horizon scanner; for nadir-pointing in LEO
    MAGNETOMETER: senses Earth's magnetic field; 0.5-3° accuracy
    GYROSCOPE (IMU): measures angular rate; drifts over time
      Fiber optic gyro (FOG): no moving parts; ~0.001°/hr drift
      Ring laser gyro: similar
      MEMS gyro: small, cheap; higher drift

  ATTITUDE CONTROL (actuation):
    REACTION WHEELS (RWs): spin up/down to produce torque
      Conservation of angular momentum: wheel accelerates → body decelerates
      3 wheels (+ spare) for 3-axis control
      Max torque: 0.03-0.5 N·m; momentum stored: 1-100 N·m·s
      Saturation: wheel at max RPM → must desaturate by dumping to magnetorquer or thruster
    MAGNETORQUERS: interact with Earth's B field → small torque
      No propellant; limited to Earth-orbiting missions with B field
      Used for desaturation + coarse control
    THRUSTERS: hydrazine or cold gas; used for large maneuvers
      Attitude control = monoprop thrusters in pairs (torque couples)
    CONTROL MOMENT GYROSCOPES (CMGs): gyroscopes that change axis
      ISS: 4 CMGs; Hubble: 6 gyroscopes
      Much higher torque than RWs at same mass
    MAGNETIC ATTITUDE (passive): permanent magnet aligns with B field
      Simple + cheap; used on early small satellites

  POINTING REQUIREMENTS:
    Star trackers: ~0.001° accuracy → JWST, Hubble (fine guidance)
    GEO comms: antenna pointing to <0.1° for high-gain downlink
    Science imagers: 0.001-0.01° (arcsec level)
    Solar panels: 5-10° sufficient for power generation
```

---

## Communications (RF)

```
SPACECRAFT COMMUNICATIONS
===========================

  LINK BUDGET FUNDAMENTALS:
    P_received = P_transmit + G_transmit - L_path + G_receive - L_misc

    EIRP (Effective Isotropic Radiated Power): P_tx + G_tx antenna (dBW)
    L_path = free-space path loss = 20 log₁₀(4πR/λ) [dB]
    G_receive = receive antenna gain
    Required minimum: S/N ratio for chosen modulation + coding

  FREQUENCY BANDS:
    UHF (300 MHz - 3 GHz):   Low gain; passes through ionosphere poorly;
                               used for launch/entry telemetry
    S-band (2-4 GHz):         Low-medium; TDRSS relay; most spacecraft
    X-band (8-12 GHz):        High gain; deep space (DSN standard); ~500 kbps-10 Mbps
    Ka-band (26-40 GHz):      Very high gain; broadband downlink; rain fade on ground
    Optical/Laser:             Gbps+ potential; demonstration stage (LCRD, TBIRD)

  ANTENNAS:
    HGA (High Gain Antenna): parabolic dish; must point at Earth/DSN
                              High data rate; narrow beamwidth (0.1-1°)
    MGA (Medium Gain): intermediate; small dish or horn
    LGA (Low Gain Antenna): omnidirectional; low data rate; always in view
                              Critical for anomaly recovery (no pointing needed)

  DEEP SPACE NETWORK (DSN):
    NASA's 3-complex network: Goldstone (CA), Madrid (Spain), Canberra (AU)
    70 m and 34 m dish antennas
    Supports all NASA planetary missions + others (ESA, JAXA)
    Bottleneck: limited assets shared among many missions

  DATA RATE EXAMPLES:
    Voyager 1 (now ~23 light-hours away): ~160 bits/sec
    Mars Reconnaissance Orbiter: 6 Mbps peak
    Hubble: 1-2 Mbps
    ISS to ground: 3-450 Mbps (via TDRSS)
    TBIRD (2022): 200 Gbps optical demo
```

---

## Structures and Mechanisms

```
SPACECRAFT STRUCTURES
=====================

  PRIMARY STRUCTURE:
    Carries all loads during launch (axial G + lateral G + vibration)
    Typical materials: Aluminum alloys (Al-6061, Al-7075)
                       Carbon fiber composite (CFRP) for high-performance
                       Titanium for hot structures and fasteners

  LOAD CASES (launch environment):
    Quasi-static: 6-8G axial; 1-2G lateral (sustained)
    Vibro-acoustic: ~140-145 dB SPL (severe acoustic forcing on large surfaces)
    Sine sweep: structural modes excited by launch vehicle resonances
    Random vibration: broadband (0.01-0.05 G²/Hz peak)
    Shock: pyrotechnic separation events; 1000+ G at brief duration

  MECHANISMS:
    Solar array deployment: spring + motor deployment
    Antenna deployment: pyrotechnic release + spring/motor
    Separation system: marman clamp or separation plane
    Instrument covers: protect during launch; open on-orbit
    Docking mechanisms: CBM (Common Berthing Mechanism, ISS) or NDS (IDSS standard)

  MARGINS (spacecraft design):
    Design safety factor: 1.5× yield; 2× ultimate
    Test loads: 1.25-1.5× design loads
    Mass margin: 20-30% at PDR; 10-15% at CDR; <5% at launch
    Power margin: 20% minimum

  MASS BUDGET:
    Typical breakdown (science orbiter):
    Structure: 20-30%
    Propulsion: 15-25% (incl. propellant)
    Power: 15-25% (panels + batteries)
    Comms: 5-10%
    ADCS: 5-10%
    Thermal: 3-8%
    C&DH: 2-5%
    Payload: 10-30% (science instruments)
```

---

## Radiation Environment

```
SPACE RADIATION ENVIRONMENT
==============================

  SOURCES:
    VAN ALLEN BELTS:
      Inner belt: ~1000-6000 km altitude; protons (MeV), electrons
      Outer belt: ~15,000-30,000 km; electrons (MeV)
      Slot region: ~8,000-15,000 km; relatively benign
      South Atlantic Anomaly (SAA): Van Allen belt dips at ~200-800 km

    SOLAR EVENTS:
      Solar Flares: X-ray + EUV burst; ionizing dose
      Solar Energetic Particles (SEPs): proton events; MeV-GeV; days duration
      Worst SEP events: August 1972, October 2003 ("Halloween storms")

    GALACTIC COSMIC RAYS (GCRs):
      Isotropic; ions (H, He, Fe) at near-relativistic energies
      Blocked by solar wind during solar maximum
      Peak during solar minimum; 10-100 MeV/nucleon dominant
      Most penetrating; no shielding fully stops them

  EFFECTS ON ELECTRONICS:
    Total Ionizing Dose (TID): accumulated radiation damage; charge trapping
    Displacement Damage: atom displacements in crystal structure; dark current
    Single Event Effects (SEEs):
      SEU (Single Event Upset): bit flip; recoverable
      SET (Single Event Transient): glitch in analog circuits
      SEL (Single Event Latchup): supply-current latch; potentially destructive
      SEG (Single Event Gate Rupture): gate oxide breakdown → permanent

  MITIGATION:
    Shielding: aluminum + polyethylene absorb protons; electrons scatter
    Rad-hard parts: radiation-hardened ICs (RH devices); higher cost
    Error-correcting codes (EDAC): SECDED (single-error correct, double-detect)
    Watchdog timers: reset after anomalous behavior
    Redundancy: cold/warm/hot spares; vote logic for critical functions
    Orbit selection: avoid worst radiation (GEO somewhat worse than LEO in SAA)
```

---

## Decision Cheat Sheet

| Question | Answer |
|---|---|
| What is the only heat removal mechanism in space? | Radiation (Stefan-Boltzmann); no atmosphere means no conduction to surroundings and no convection. Radiators must be sized to reject all internal + solar heat. |
| Why do spacecraft use star trackers? | Most accurate attitude sensor (0.001° = arcseconds); identifies attitude from star patterns autonomously; works in any orientation; required for precision pointing missions |
| What is reaction wheel saturation? | When a reaction wheel reaches maximum RPM, it can no longer absorb angular momentum from external torques; must desaturate by firing thrusters or using magnetorquers to dump momentum |
| Why do deep space missions use X-band? | Better than S-band for path loss at deep space distances; Ka-band is even better but requires more precise pointing; X-band is the DSN standard for deep space |
| What is MLI? | Multi-layer insulation: aluminized Mylar/Kapton blankets that reduce radiated heat loss; works like a thermos; essential for maintaining electronics at operational temperatures in eclipse |
| What is an SEU? | Single Event Upset: cosmic ray flips a bit in memory; causes software errors; mitigated by EDAC memory and watchdog/recovery logic |
| Why is the South Atlantic Anomaly a problem? | The inner Van Allen belt dips low over the South Atlantic due to Earth's geomagnetic field asymmetry; LEO satellites pass through higher radiation there; electronics must cope with increased SEE rate |

---

## Common Confusion Points

**Solar panels are not simply "power = panels × efficiency"**: Solar panels must be oriented toward the Sun; power varies with angle (cosine function). Panels degrade over time (radiation). Temperature affects output (colder = more efficient). The EPS must handle variable input and provide regulated power through eclipse.

**Triple redundancy in spacecraft is not like software redundancy**: Hardware redundancy in spacecraft uses voting logic (majority-vote processor) or cold/warm standby. But "triple redundant" means triple the mass and power. Designers select critical components for redundancy; non-critical items may be single-string. Cost and mass constraints limit how much redundancy is practical.

**Spacecraft communication links are not like network connections**: Space links are one-way delay (light-speed limited); Mars: 3-22 minute one-way delay; no real-time control possible. Spacecraft must be autonomous for critical events. Ground contact times are limited (windows when DSN antenna is in view). Protocols are designed for high-latency, lossy, one-way links — very different from TCP/IP assumptions.

**Heat pipes work without pumps**: A spacecraft heat pipe uses capillary pressure (wick structure) to move liquid from hot end (evaporation) to cold end (condensation). No pump needed; no moving parts; extremely reliable. Common misconception: they require gravity (wick provides the driving force, not gravity).
