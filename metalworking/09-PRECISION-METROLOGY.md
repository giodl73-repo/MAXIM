# Precision Metrology

## The Big Picture

Metrology is **the science of measurement** — establishing that a component's actual geometry, surface, and properties are within specified limits. No manufacturing process produces perfect parts; metrology determines whether the parts produced are acceptable. The central framework is **tolerance**: the allowable variation around a nominal dimension that still permits the part to function. Everything downstream — gauging, CMM, SPC — is a system for verifying conformance to tolerance.

```
METROLOGY HIERARCHY:

  DESIGN: nominal dimension + tolerance (GD&T callouts)
       │
  PROCESS CAPABILITY: does the process hold the tolerance? (Cp, Cpk)
       │
  IN-PROCESS GAUGING: real-time feedback during machining
       │
  INSPECTION (CMM, surface): did this specific part meet spec?
       │
  GAUGE R&R: is the measurement system reliable enough to detect non-conforming parts?
       │
  SPC: control chart → process trending → intervention before out-of-spec

TOLERANCE MAGNITUDE EXAMPLES:
  Free-machined surfaces:     ±0.5–1 mm   (rough fixtures, brackets)
  Standard machined:          ±0.05–0.1 mm (general precision)
  Close-tolerance:            ±0.01 mm     (fits, bearing bores)
  Precision ground:           ±0.001 mm    (1 micron — gauge components)
  Ultra-precision:            ±0.0001 mm   (100 nm — optical components, silicon wafers)
  → 1 micron = 1/70 of human hair; 100 nm = virus size
```

---

## Dimensional Tolerances and ISO 286 Fits

### ISO 286 System

```
ISO 286 FITS — SHAFT AND HOLE NOTATION:

  Fit: relationship between mating shaft and hole dimensions

  HOLE DESIGNATION: letter (uppercase) + number
    H = fundamental deviation = 0 (lower limit = nominal)
    H7: hole with zero lower deviation + IT7 tolerance grade
    → H7 hole: actual size between +0 and +IT7 above nominal

  SHAFT DESIGNATION: letter (lowercase) + number
    f, g, h: clearance-producing (shaft smaller than hole)
    j, k, m, n: transition (can be either)
    p, r, s: interference-producing (shaft larger than hole)

FIT TYPES:

  CLEARANCE FIT:
    Hole always larger than shaft
    → Always has gap (clearance); shaft slides or rotates in hole
    Examples:
      H7/f7: loose running fit (sliding + rotating; large clearance)
      H7/g6: running fit (bearings; snug but rotates freely)
      H8/h9: easy clearance (non-precision sliding)

  TRANSITION FIT:
    May be clearance OR interference depending on actual dimensions
    → Design intent: precise location without guaranteed interference
    Examples:
      H7/k6: keying fit (pressed lightly; usually slight interference)
      H7/n6: used for gears, couplings; slight interference typical

  INTERFERENCE FIT (PRESS FIT):
    Shaft always larger than hole → must be assembled by force or thermal method
    → Held by friction force from elastic/plastic deformation of both parts
    Examples:
      H7/p6: light press fit (permanent assembly; requires low force)
      H7/s6: medium drive fit (significant force or temperature)
      H7/u6: force fit (must heat or cool to assemble; very tight)

TOLERANCE GRADES (IT grades):
  IT = International Tolerance Grade
  IT1 (finest) → IT18 (coarsest): specified tolerance width as function of nominal size
  IT6: typical precision machining (CNC turning, grinding)
  IT7: standard for running fits (H7 holes)
  IT9–IT11: free-machined, rough

EXAMPLE — 50mm H7/g6 running fit:
  50mm H7 hole: +0 to +25 μm (25 μm tolerance band)
  50mm g6 shaft: −9 to −25 μm (16 μm tolerance band)
  → Clearance: minimum = 9 μm; maximum = 50 μm
  → Shaft always smaller → always rotates; bearing fit
```

### GD&T — Geometric Dimensioning and Tolerancing

```
GD&T (ASME Y14.5 / ISO 1101):
  Traditional tolerancing: ±X on each dimension → tolerance cube (over-constrains)
  GD&T: tolerance on the GEOMETRY itself → more precisely describes design intent

DATUM REFERENCE FRAME:
  Three mutually perpendicular planes (A, B, C) define the coordinate system
  Datums: surfaces or features designated as measurement reference
  → Must be established in specific order (primary, secondary, tertiary)
  → CMM: probe datum surfaces first → establish coordinate system → measure features

GD&T SYMBOLS AND TOLERANCES:
  Form:
    Flatness: ─ (flat face within tolerance zone)
    Straightness: ─ ─ (line element within tolerance zone)
    Circularity: ○ (cross-section within two concentric circles)
    Cylindricity: ◎ (full cylinder within two coaxial cylinders)

  Orientation (require datums):
    Perpendicularity: ⊥ (axis or surface perpendicular to datum)
    Parallelism: ∥ (surface/axis parallel to datum within tolerance)
    Angularity: ∠ (specific angle to datum)

  Location:
    True position: ⊕ (axis or feature within cylindrical or spherical tolerance zone)
      Most important: locates holes, bosses, pins precisely
      Circular tolerance zone (⊕0.1) = more tolerance than ±0.07 square zone (same area)
    Concentricity/Coaxiality: ◎ (axis within cylindrical tolerance relative to datum)
    Symmetry: ═ (feature symmetric about datum)

  Profile:
    Profile of a line / surface: complex curved profiles within tolerance band

  Runout:
    Circular runout: surface element variation while rotating about datum axis
    Total runout: full surface variation while rotating → includes both radial and axial

MAXIMUM MATERIAL CONDITION (MMC) MODIFIER ⓂC:
  Bonus tolerance: as shaft is machined smaller (away from MMC), tolerance increases
  Physical reasoning: if shaft is smaller, hole can be less precisely located and still fit
  Only applies to: size features (holes, shafts, tabs)
  → Common on bolt patterns: when all holes are larger, their true position can be looser
```

---

## Surface Roughness

```
SURFACE TEXTURE PARAMETERS:

  All measured by profilometer (stylus or optical) along a trace length

  Ra (arithmetic mean roughness):
    Average absolute deviation from mean line over evaluation length
    Ra = (1/L) ∫|z(x)| dx
    Most widely used; insensitive to single spikes

  Rq (RMS roughness):
    Root mean square of profile deviations
    Rq = √(1/L ∫z(x)² dx)
    More sensitive to outliers than Ra; used in optics (wavefront error)
    Rq ≈ 1.25 × Ra for typical surfaces

  Rz (mean roughness depth):
    Average of peak-to-valley heights of 5 consecutive sampling lengths
    More sensitive to individual peaks than Ra
    → Important for: surfaces that fail on peak contact (seals, gaskets)
    Rz typically 4–8× Ra

  Typical Ra values:
    Rough turned:      Ra 3.2–12.5 μm (0.125–0.5 μin Ra equiv)
    Fine turned:       Ra 0.8–3.2 μm
    Ground:            Ra 0.2–1.6 μm
    Honed:             Ra 0.025–0.4 μm (bearing bores)
    Lapped/polished:   Ra 0.012–0.1 μm
    Optical surface:   Ra < 0.001 μm (1 nm — superpolish)

MEASUREMENT METHODS:

  STYLUS PROFILOMETER:
    Diamond stylus (2 μm tip radius) traverses surface at constant speed
    Vertical motion of stylus → electrical signal → profile trace
    → Cannot measure very deep grooves (stylus can't fit) or very fine features
    Standards: ISO 4287; ASME B46.1

  OPTICAL PROFILERS:
    White light interferometry (WLI): coherence scanning → phase map → 3D surface
    Confocal microscopy: depth discrimination from focus → nm resolution
    Laser scanning: fast; non-contact; nm vertical resolution
    No stylus contact → can measure fragile, soft, or very fine surfaces
    → Semiconductor wafers, optical elements: non-contact required

  ROUGHNESS vs. WAVINESS vs. FORM:
    Form error: gross shape deviation (bow, taper) — removed by least-squares fit
    Waviness: medium frequency (fixturing, machine tool vibration)
    Roughness: high frequency (cutting action)
    → Filters separate these: λc (cutoff wavelength) separates roughness from waviness
    → Standard Gaussian filter: λc = 0.8 mm (Ra), 2.5 mm, 8 mm for rougher surfaces
```

---

## Coordinate Measuring Machines (CMMs)

```
CMM ARCHITECTURE:

  Structure: granite surface plate + Cartesian bridge (or arm) + spindle
  Probing: ruby-ball probe (2mm diameter) on precision quill
  Position sensing: glass scales (linear encoders) at each axis; resolution 0.1–0.01 μm
  Control: CNC or DCC (direct computer control) — programmable measurement routines

  TYPES:
    Bridge CMM: gantry over part → most common; stable; limited part height
    Horizontal arm: arm extends over large part → for car bodies, large structures
    Portable CMM (FARO arm): articulated arm with encoders → for field measurement
    Optical CMM: structured light or fringe projection → non-contact; fast; less precise

PROBE QUALIFICATION:
  Must establish the probe's exact tip radius and position in machine coordinates
  Qualification sphere (precision chrome steel, 25mm diameter, known exactly)
  → Touch qualification sphere at multiple points → find actual center → calibrate tip
  Run at each probe orientation change; temperature-sensitive → re-qualify periodically

  PROBE TYPES:
    Touch-trigger (Renishaw): electrical contact → signal to controller; binary touch/no touch
    Scanning probe: continuous analog measurement; traces contours; better for complex geometry
    Optical probe: laser spot or structured light; non-contact; for soft/fragile surfaces

MEASUREMENT OF GD&T FEATURES:
  HOLE (TRUE POSITION):
    Touch minimum 4 points on bore circle → fit circle → find center
    Compare center XY to nominal → compute deviation → compare to position tolerance
    With CMM: full 3D position in datum reference frame

  FLATNESS:
    Touch N points on surface → fit plane → find maximum deviation from plane
    Compare to flatness tolerance

  CYLINDRICITY:
    Touch multiple circles at multiple heights → fit best-fit cylinder
    Maximum deviation from cylinder → compare to cylindricity tolerance

  PROFILE OF A SURFACE:
    Scan or measure dense point grid → compare to nominal CAD surface
    → Each point: deviation from nominal → check within tolerance band

CMM ACCURACY FACTORS:
  Temperature: granite and part expand thermally → CMM rooms: 20°C ±0.5°C controlled
  Cleanliness: chips/coolant on surface → false readings
  Part clamping: over-clamped part distorts → measure unclamped
  Probe qualification frequency: critical for accuracy
  CMM calibration: against NIST-traceable gauge blocks + reference spheres annually
```

---

## Gauge R&R

```
GAUGE R&R (REPEATABILITY AND REPRODUCIBILITY):
  Measurement system analysis — quantifies how much variation comes from the measurement
  system vs. actual part-to-part variation

COMPONENTS OF VARIATION:
  Total variation = Part variation + Gauge R&R
  Gauge R&R = Repeatability + Reproducibility

  Repeatability: variation when ONE operator measures SAME part MULTIPLE TIMES
    → Equipment variation; inherent gauge precision
  Reproducibility: variation when MULTIPLE operators measure SAME part
    → Operator effect; training; interpretation
  Part variation: actual manufacturing variation (what we want to measure)

CONDUCTING GAUGE R&R (AIAG MSA method):
  10 parts × 2 operators × 2 trials (minimum)
  Each operator measures each part twice; operators blind to each other's results
  ANOVA: separate sources of variation
  Compute: %Study Variation = (σ_gauge / σ_total) × 100

ACCEPTANCE CRITERIA:
  %Gauge R&R < 10%: acceptable → measurement system is adequate
  10–30%: marginal → may be acceptable depending on application
  > 30%: unacceptable → measurement system cannot reliably detect non-conforming parts

  NDC (Number of Distinct Categories):
  NDC = (√2 × σ_parts) / σ_gauge
  NDC ≥ 5: acceptable; measurement system can distinguish 5+ categories
  NDC < 2: gauge is essentially useless for process control

PRACTICAL IMPLICATIONS:
  Gauge R&R > 30%: if inspection rejects a lot, could be measurement system, not parts
  Gauge R&R < 10%: inspection decisions are reliable
  → Must conduct Gauge R&R before using measurement system for production go/no-go
  → Especially critical: attribute gauges (go/no-go) → confusion between borderline parts
```

---

<!-- @editor[bridge/P3]: Natural bridge to CI/CD observability — SPC control charts are the manufacturing equivalent of production metrics dashboards: control limits = alerting thresholds, Cpk = process health score, Western Electric rules = anomaly detection rules; the learner's VSTS/DevOps background maps directly -->
## Statistical Process Control (SPC)

```
SPC CONTROL CHARTS:
  Track process output over time → detect when process has shifted or increased variation
  → Take corrective action BEFORE producing out-of-spec parts

SHEWHART CONTROL CHART:
  X̄-R chart (for subgroup means and ranges):
    X̄ (X-bar): average of subgroup of n measurements → tracks CENTERING
    R (Range): max-min within subgroup → tracks VARIATION
    UCL/LCL: control limits at ± 3σ from centerline (99.73% of normal distribution)
    → Points outside limits: signal; process shifted or variation increased

  I-MR chart (individuals and moving range):
    For n=1 (single measurement per time point)
    I: individual value; MR: moving range between consecutive values
    → Used when subgroups aren't practical (slow processes, destructive testing)

CONTROL CHART SIGNALS (Western Electric rules):
  1. One point outside ±3σ
  2. Two of three consecutive points outside ±2σ (same side)
  3. Four of five consecutive points outside ±1σ (same side)
  4. Eight consecutive points on same side of centerline
  → Each rule: ~1/1000 false alarm probability if applied alone; combined ~0.8%

CAPABILITY INDICES:
  Cp = (USL − LSL) / (6σ)   [spread capability]
    Voice of customer (spec) vs. Voice of process (±3σ)
    Cp = 1.0: process fits exactly; expect 2700 ppm outside spec
    Cp = 1.33: ±4σ; ~63 ppm outside
    Cp = 1.67: ±5σ; ~0.57 ppm
    Cp = 2.0: ±6σ (Six Sigma): 2 ppm (accounts for ±1.5σ shift → 3.4 DPMO)

  Cpk = min(Cpu, Cpl)   [centered capability]
    Cpu = (USL − X̄) / 3σ;  Cpl = (X̄ − LSL) / 3σ
    Cpk accounts for process being off-center
    Cpk < Cp: process is not centered on nominal
    → Both Cp ≥ 1.33 AND Cpk ≥ 1.33 needed to claim process is capable AND centered

SPC IN MACHINING:
  In-process gauging: measure every nth part → plot on X̄-R chart
  Tool wear: gradual dimensional drift → trend toward control limit → offset tool before OOL
  Thermal drift: early in shift → dimensions shift as machine warms → monitor
  Setup variation: first article inspection → verify process centered
  → Modern CNC: automatic measurement + automatic tool offset correction → closed loop
```

---

## Laser Tracker for Large Parts

```
LASER TRACKER (FARO, Leica, API):
  CMM for large-scale measurement (1–100+ meters)
  Measures: 3D position of a retro-reflective target (SMR — spherically mounted retroreflector)

PRINCIPLE:
  Laser beam → retroreflector → reflected exactly back
  Interferometer: measures distance change (continuous tracking mode)
  Angular encoders (two axes): measure azimuth + elevation
  → Full 3D position: r, θ, φ → X, Y, Z

  ABSOLUTE DISTANCE MEASUREMENT (ADM):
    Measures absolute distance (not just change)
    → Can re-acquire target if tracking is lost; doesn't need continuous beam
    Modern trackers: ADM + interferometry combined

ACCURACY:
  Volumetric accuracy: ±15–50 μm at 10–15 m (FARO Vantage, Leica AT403)
  Angular resolution: 0.07 arc-seconds
  Working volume: up to 80m radius (some models)
  → For 10m measurement: ±50 μm = 0.005 mm → acceptable for aerospace structures

APPLICATIONS:
  Aircraft fuselage assembly: align fuselage sections (±0.5 mm over 30m)
  Ship block assembly: position hull sections for welding
  Wind turbine: measure tower straightness, nacelle alignment
  Automotive tooling: verify jig/fixture geometry; build-to-tolerance
  CMM verification: check CMM calibration against laser tracker standard

COMPARISON TO PORTABLE CMM ARM:
  FARO arm:     range 1.5–4m; accuracy ±25–50 μm; contact; flexible
  Laser tracker: range 10–80m; accuracy ±15–50 μm; non-contact; tripod-mounted
  → Small parts in shop: FARO arm; large structures in field: laser tracker
  → Photogrammetry (camera + coded targets): comparable accuracy; denser point cloud;
    lower cost for specific applications (complete object scan)
```

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| Choose fit for rotating shaft in bearing | H7/g6 (clearance running fit) |
| Choose fit for press-fit gear on shaft | H7/p6 or H7/s6 (interference) |
| Locate hole pattern precisely | True position (⊕) GD&T callout; not ±X, ±Y |
| Measure complex 3D geometry | CMM with scanning probe; compare to CAD model |
| Measure very large aircraft assembly | Laser tracker |
| Verify measurement system before use | Gauge R&R; target <10% study variation |
| Monitor process drift over time | X̄-R or I-MR control chart |
| Specify surface roughness for bearing journal | Ra 0.4–0.8 μm (fine ground or honed) |
| Measure optical/fragile surface roughness | White light interferometry (non-contact) |
| Determine if process is centered + capable | Both Cp ≥ 1.33 AND Cpk ≥ 1.33 |

---

## Common Confusion Points

**Cp and Cpk are different; both are required**
Cp measures whether the process spread fits within the tolerance band, regardless of centering. Cpk measures the worst-case capability accounting for how far off-center the process is. Cp = 2.0 and Cpk = 0.5 means: the process has enough potential spread to produce excellent parts, but is so far off nominal that it's currently making mostly out-of-spec parts. Both indices are always needed.

**ISO 286 fit notation specifies both the hole and shaft tolerance**
"H7/g6" is not one thing — it's a pair: H7 specifies the hole tolerance; g6 specifies the shaft tolerance. You select the combination that gives the required fit characteristics. "H7" alone doesn't specify a fit; it specifies only the hole side. The complete fit designation requires both.

**GD&T true position tolerance zone is cylindrical, not square**
Traditional ±X, ±Y tolerancing creates a square tolerance zone. A hole allowed ±0.1mm in X and ±0.1mm in Y can be 0.141mm off nominal at the corner (diagonal) and still be in spec — effectively a 0.28mm diameter circle. GD&T true position ⊕0.1mm creates a circular zone of diameter 0.1mm — more restrictive at corners, more permissive along axes. For equivalent coverage, a circular zone is 57% of the area of the square zone.

**Surface roughness Ra alone is insufficient for functional specification**
Ra averages out spikes and valleys. A surface with deep isolated grooves and a surface with uniform waviness can have the same Ra. For sealing surfaces: Rz or Rpk (reduced peak height) better predicts leakage. For bearing surfaces: Rsk (skewness — negative = more valleys = more lubricant retention) matters. Ra is a starting point; functional specification requires additional parameters.

**SPC control limits are not the same as specification limits**
Control limits (UCL/LCL) are ±3σ from the process mean — statistical estimates of process variation. Specification limits (USL/LSL) are engineering requirements from the design. They are independent: a process can be in statistical control (all points within control limits) while producing out-of-spec parts (if it's off-center). A capable, centered process has its ±3σ well inside the ±spec limits.
