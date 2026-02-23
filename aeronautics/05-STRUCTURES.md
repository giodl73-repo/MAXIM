# 05 — Aerospace Structures

## Loads, Stress Analysis, Materials, Fatigue, Aeroelasticity, Certification

---

## Big Picture: Structures Design Framework

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      AEROSPACE STRUCTURES FRAMEWORK                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  LOAD DEFINITION (what forces act on the structure)                         │
│   Flight loads: maneuver (V-n envelope) + gust (Ude × factor)               │
│   Ground loads: landing impact, taxiing, towing, jacking                    │
│   Pressurization: hoop stress in fuselage from cabin ΔP                     │
│   Thermal loads: aerodynamic heating, CTE mismatch at joints                │
│                              │                                              │
│                              ▼                                              │
│  STRUCTURAL ANALYSIS (how the structure responds)                           │
│   Global: stick model / beam model → internal forces (M, V, T)              │
│   Component: box beam / panel models → stress distributions                 │
│   Detailed: FEM shell models → stress concentrations, joints, cutouts       │
│                              │                                              │
│                              ▼                                              │
│  MATERIAL CHARACTERIZATION                                                  │
│   Metals: Al alloys, Ti-6Al-4V, steel (yield, UTS, fracture toughness)     │
│   Composites: CFRP, GFRP — CLT, ply angles, orthotropic stiffness          │
│                              │                                              │
│                              ▼                                              │
│  DESIGN PHILOSOPHIES                                                        │
│   Static: limit load × 1.5 = ultimate; no yield at limit; no fracture at UL│
│   Fatigue: S-N curves; service life; inspection intervals                   │
│   Damage tolerance: assume flaw; crack growth < critical in inspection span │
│   Fail-safe: redundant load paths; partial failure must be detectable       │
│                              │                                              │
│                              ▼                                              │
│  AEROELASTICITY (structure + aerodynamics coupling)                         │
│   Static: divergence, aileron reversal                                      │
│   Dynamic: flutter (catastrophic), buffet, gust response                   │
│                              │                                              │
│                              ▼                                              │
│  CERTIFICATION (FAR 25 structural substantiation)                           │
│   Analysis + test: static ultimate load test; full-scale fatigue test       │
│   Ground Vibration Test (GVT): flutter clearance; structural modes          │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 1. Structural Architecture

```
SEMI-MONOCOQUE CONSTRUCTION:
  Load carried by: skin (shear + hoop) + stringers (bending tension/compression)
                 + frames/ribs (shape; transverse loads) + spars (bending + shear)
  "Semi": spars/frames contribute; true monocoque is pure skin (fragile)

WING BOX CROSS-SECTION:
  ┌──────────────────────────────────────────────────┐
  │                  SKIN (upper)                    │
  │  ┌─┐   ┌─┐ ┌─┐   ┌─┐    ← Stringers (Z/L/T)   │
  │  │ │   │ │ │ │   │ │                             │
  │──┼─┼───┼─┼─┼─┼───┼─┼──  ← FRONT SPAR (web+caps)│
  │  │ │   │ │ │ │   │ │                             │
  │──┼─┼───┼─┼─┼─┼───┼─┼──  ← REAR SPAR             │
  │                                                  │
  │                  SKIN (lower)                    │
  └──────────────────────────────────────────────────┘
  Upper skin: compression (buckling critical)
  Lower skin: tension (fatigue critical)
  Spars: web carries shear; caps carry bending
  Ribs: maintain section shape; spanwise intervals 18-30" typically

FUSELAGE STRUCTURE:
  Frames (rings): circular hoops; maintain cross-section; bear concentrated loads
  Stringers: longitudinal; carry bending + axial loads
  Skin: carry shear + pressurization hoop stress
  Keels, beams: at floors; support cabin floor loads; emergency loads

LOAD PATHS — CRITICAL CONCEPT:
  Every external load must have a continuous path through structure to primary structure
  Interrupted load path (e.g., cutout for window/door) → stress concentration
  Doublers/reinforcements around cutouts: restore load path continuity
  Frame at each cutout: transfers load around the opening

FUSELAGE PRESSURIZATION HOOP STRESS:
  ΔP = cabin pressure − ambient (typically 0.56 atm at cruise at 40,000 ft)
  Hoop stress: σ_θ = ΔP × R / t   (thin-walled cylinder)
  Longitudinal stress: σ_x = ΔP × R / (2t)
  Fuselage radius R ≈ 3-4 m; skin thickness ~2-4 mm Al → σ ≈ 50-100 MPa
  This is fatigue-critical: pressurize + depressurize every flight cycle
```

---

## 2. Stress Analysis Fundamentals

```
STRESS STATE (3D):
  Stress tensor:  ┌σxx  τxy  τxz┐
                  │τxy  σyy  τyz│
                  └τxz  τyz  σzz┘
  Symmetric (6 independent components)

PRINCIPAL STRESSES:
  Transform coordinates to eliminate shear: σ₁, σ₂, σ₃ (principal stresses)
  Maximum shear stress: τ_max = (σ₁ - σ₃) / 2
  Von Mises criterion: σ_VM = √((σ₁-σ₂)² + (σ₂-σ₃)² + (σ₃-σ₁)²) / √2 ≤ σ_y
  Tresca criterion: (σ₁-σ₃) ≤ σ_y

MOHR'S CIRCLE (2D):
  Center: C = (σx + σy) / 2
  Radius: R = √((σx - σy)²/4 + τxy²)
  Principal stresses: σ₁,₂ = C ± R
  Max shear: τ_max = R
  Used for: transforming stress components between coordinate systems

THIN-WALLED STRUCTURES:

  SHEAR FLOW q = τ × t:
    In an open thin-walled section (cut spar web), shear flow varies along perimeter:
    q(s) = q₀ - (Vy/Iz) × ∫₀ˢ t(s')·y(s')·ds'   (first moment of area Q(s))
    Shear center: point about which applied shear produces no twisting
    Open sections have shear center outside web → can be well off centroid

  TORSION OF CLOSED SECTION (Bredt-Batho):
    For single-cell closed section: T = 2·A_enc × q   (A_enc = enclosed area)
    Shear flow from torsion: q = T / (2 × A_enc)   [constant around closed section]
    Twist rate: dφ/dx = T / (4·A_enc² × G) × ∮ ds/t

    Multi-cell box (wing box with ribs): simultaneous equations for q per cell
    Wing box is multi-cell: front spar + rear spar + top + bottom skin form 2 cells
    → more efficient torsional stiffness than single-cell equivalent

BEAM THEORY:
  Euler-Bernoulli: M = EI·κ; σ = M·y/I; plane sections remain plane
    Valid for: slender beams (L/h >> 10); shear deformation neglected
  Timoshenko: adds shear deformation; important for short thick beams (L/h < 10)
    Relevant for: composite beam analysis; short fuselage frames; stiffened panels

  DEFLECTION:
    d²v/dx² = M(x)/(EI)    [Euler-Bernoulli]
    Boundary conditions: cantilever, simply supported, clamped-clamped

  BENDING OF WING:
    Wing is a cantilever: root = clamped; tip = free
    Running load: lift distribution (elliptic ideal) → spanwise bending moment
    Shear: ∫ from tip to root of lift distribution
    Bending moment: maximum at root; for elliptic lift → M_root = L × b/π (approx)
```

---

## 3. Stability — Buckling

```
EULER COLUMN BUCKLING:
  Critical load: P_cr = π²·EI / (K·L)²   where K = effective length factor:
    K=1: pin-pin;  K=0.5: fixed-fixed;  K=0.7: fixed-pin;  K=2: fixed-free
  Slenderness ratio: λ = KL/r  (r = radius of gyration = √(I/A))
  Johnson parabola: short columns fail by yielding, not elastic buckling

PANEL BUCKLING:
  Thin panel: critical shear stress τ_cr = k_s · π²·E / (12(1-ν²)) × (t/b)²
  Stiffened panels: stringers increase effective stiffness; prevent global buckling
  Post-buckling: panels carry more load after buckling (tension field action)
    Wagner beam: web buckles → diagonal tension field; effective web in tension only
  Crippling: local buckling of stiffener flanges → ultimate load

COMPRESSION IN WING UPPER SKIN:
  Critical loading condition: positive maneuver → upper skin in compression
  Stringers: increase t/b effectively; prevent skin buckling before limit load
  Fail condition: if stringer fails → skin loses support → catastrophic buckling

FATIGUE OF FUSELAGE LOWER SKIN:
  Lower skin: bending + pressurization → tension → fatigue crack initiation
  S-N (Woehler) design: detail stress × cycles ← must be below knee of curve
  Pressure vessel cycling: Comet disasters (1954): square windows → stress concentration ×3
  Square → oval windows: all airliners after Comet
```

---

## 4. Materials

```
ALUMINUM ALLOYS:
  2xxx series: Cu alloyed; high strength + good fatigue; used in tension-critical parts
    2024-T3: fuselage skin, lower wing panels (good fracture toughness)
    2024-T4: good formability for complex parts
  7xxx series: Zn alloyed; highest strength; used in compression-critical parts
    7075-T6: upper wing skin, spar caps (highest strength Al)
    7150, 7055: improved corrosion resistance vs 7075; newer aircraft
    7xxx stress corrosion susceptibility: must manage moisture exposure
  Allowables from MIL-HDBK-5 / MMPDS: statistically-derived design values

TITANIUM:
  Ti-6Al-4V: dominant structural titanium; two-phase α+β; ρ ≈ 4.43 g/cm³
  High strength-to-weight; corrosion resistant; low CTE (6 ppm/°C vs Al 23, CFRP ~2)
  Excellent at elevated temperature → turbine structures, hot airframe sections
  Used: engine pylons, landing gear, high-stress frames, fasteners
  Cost: ~10× aluminum per kg; limited to where needed

STEEL:
  300M, HY-180: landing gear (require very high strength; ~1800 MPa UTS)
  Stainless (17-4 PH, 15-5 PH): fasteners, fuel system, high-corrosion areas
  Heavy but needed for landing gear impact loads (ultra-high strength required)

CARBON FIBER REINFORCED POLYMER (CFRP):
  Properties:
    E_fiber ≈ 230-390 GPa (TorayT300/T700/T800/T1000)
    σ_UTS fiber ≈ 3,500-7,000 MPa (unidirectional composite)
    ρ ≈ 1.55-1.65 g/cm³ (vs Al 2.7, Ti 4.4)
    Specific stiffness: E/ρ ≈ 2-4× aluminum
    Specific strength: σ/ρ >> metals

  Anisotropy: properties depend on fiber direction
  Ply: single layer of unidirectional (UD) or woven fibers in matrix
  Laminate: multiple plies at various orientations [0/+45/-45/90]_s notation

  Boeing 787: 50% CFRP by weight (wings, fuselage barrels)
  A350: 53% composites; CFRP wing + fuselage; Al-Li + Ti elsewhere
  A380: 22% composites (mostly empennage + fairings; metallic wing)
  B777X: composite wing (new vs metallic B777)

GLASS FIBER (GFRP):
  Lower stiffness than CFRP (E_glass ≈ 70 GPa)
  Cheaper; used for: radomes (RF transparent), fairings, interior panels
  Woven glass/epoxy: common for non-structural composite parts

Al-Li ALLOYS:
  Li addition reduces density ~3% per 1% Li; increases stiffness
  A350 fuselage uses Al-Li 2198/2196 skin; lighter than 2024
  Challenges: lower toughness; anisotropy; higher cost than conventional Al
```

---

## 5. Composite Mechanics

```
PLY CONSTITUTIVE RELATIONS (Orthotropic):
  In principal material axes (1 = fiber, 2 = transverse, 3 = through-thickness):
  ┌ε₁ ┐   ┌ 1/E₁    -ν₁₂/E₁    0  ┐ ┌σ₁ ┐
  │ε₂ │ = │-ν₁₂/E₁   1/E₂      0  │ │σ₂ │
  └γ₁₂┘   └  0         0      1/G₁₂┘ └τ₁₂┘

  Typical UD CFRP (T300/epoxy):
    E₁ = 137 GPa, E₂ = 9 GPa, G₁₂ = 5 GPa, ν₁₂ = 0.3

  Transformed stiffness [Q̄]: rotate ply compliance to structural axes (x-y)
  Uses transformation matrix T(θ) where θ = ply angle

CLASSICAL LAMINATE THEORY (CLT):
  Laminate stacking: [θ₁/θ₂/.../θₙ]; symmetric = [θ₁/θ₂/...]_s
  Midplane strains ε₀ and curvatures κ:
    ┌N┐   ┌A  B┐ ┌ε₀┐
    │ │ = │    │ │  │
    └M┘   └B  D┘ └κ ┘
  A = extensional stiffness: Σ Q̄ₖ × tₖ  (×1 for in-plane)
  B = bending-extension coupling; = 0 for symmetric laminate
  D = bending stiffness: Σ Q̄ₖ × (z_k³ - z_{k-1}³) / 3

  Balanced laminate: equal ±θ plies → no in-plane shear-extension coupling (A₁₆=A₂₆=0)
  Quasi-isotropic: [0/±45/90]_s → in-plane properties same in all directions;
    very common for airframe applications

FAILURE CRITERIA:
  Maximum stress: each stress component compared to allowable independently
  Maximum strain: each strain compared to ultimate
  Tsai-Wu: interactive criterion accounting for biaxial stress interaction
    F₁σ₁ + F₂σ₂ + F₁₁σ₁² + F₂₂σ₂² + 2F₁₂σ₁σ₂ + F₆₆τ₁₂² ≤ 1

  First ply failure (FPF): first ply to fail; conservative but useful for stiffness check
  Last ply failure (LPF): progressive failure until last ply; ultimate strength

OPEN HOLE COMPRESSION (OHC) and OPEN HOLE TENSION (OHT):
  Critical allowable for composite panels: hole (fastener) causes stress concentration
  OHC typically governs upper wing compression; reduced by ~50% vs unnotched
  Bearing/bypass: fastener loads through composite panel; complex interaction

DELAMINATION:
  Separation between plies; interlaminar shear or normal stress driven
  Inspection: ultrasonic C-scan detects delamination area
  Impact damage: barely visible impact damage (BVID) — hard to see; dangerous
  BVID tolerance: structural allowables already account for expected BVID per AC 25.571
```

---

## 6. Fatigue

```
STRESS-LIFE (S-N / WOEHLER) APPROACH:
  Cyclic loading: max stress S_max, stress ratio R = S_min/S_max
  S-N curve: log(N_f) vs S; slope = -1/b in Basquin representation
  Endurance limit (steels): below ~500 MPa, some steels don't fatigue in 10⁷ cycles
  Aluminum: no true endurance limit — specify at 10⁸ or 10⁹ cycles
  Factors: surface finish, stress concentration, environment (corrosion → fatigue life reduction)

STRESS CONCENTRATION FACTOR Kt:
  Kt = σ_max / σ_nom   (ratio of local peak stress to nominal)
  Circular hole in infinite plate: Kt = 3 (biaxial)
  Elliptical hole: Kt = 1 + 2a/b  (a = major axis perpendicular to load)
  Comet disaster: square window → Kt ≈ 6 → fatigue life dramatically reduced
  Rivet holes: Kt mitigated by cold expansion (compressive residual stress)

MEAN STRESS EFFECTS:
  Goodman relation: S_a/S_e + S_m/UTS = 1
  Gerber parabola: S_a/S_e + (S_m/UTS)² = 1
  Stress ratio R = -1: fully reversed; R = 0.1: common aircraft structural loading
  Tension mean stress (positive R) reduces fatigue life

MINER'S RULE (cumulative damage):
  D = Σ (nᵢ / Nᵢ)   where nᵢ = actual cycles at stress Sᵢ, Nᵢ = life at Sᵢ
  Failure when D = 1 (Palmgren-Miner linear damage hypothesis)
  Conservative: scatter factor of 2-4× applied in aircraft fatigue substantiation

AIRCRAFT FATIGUE SPECTRUM:
  Pressurization cycles: ground→cruise→ground; 1× per flight
  Gust loading: continuous random; specified by power spectral density or exceedance curves
  Maneuver loads: turns, pull-outs; lower frequency than gusts
  Landing impact: gear loads; once per landing
  Total spectrum: combined for full fatigue analysis per AC 25.571
```

---

## 7. Fracture Mechanics and Damage Tolerance

```
LINEAR ELASTIC FRACTURE MECHANICS (LEFM):

STRESS INTENSITY FACTOR K:
  K = σ · √(π·a) · F(geometry)   [MPa√m]
  Mode I (opening): KI; Mode II (shear); Mode III (tearing)
  F(geometry): correction for finite width, crack proximity to edge, etc.
  Example: central crack in infinite plate: K = σ · √(πa)

FRACTURE TOUGHNESS K_IC:
  Material property: critical KI at which rapid fracture occurs
  2024-T3: KIC ≈ 33 MPa√m (reasonably tough; fuselage applications)
  7075-T6: KIC ≈ 24 MPa√m (less tough; not for fuselage skin)
  7050-T7451: KIC ≈ 35 MPa√m (improved toughness thick sections)
  Ti-6Al-4V: KIC ≈ 44-66 MPa√m
  CFRP: depends on layup; typically KIC ≈ 1-3 MPa√m (lower toughness → delamination risk)

CRITICAL CRACK SIZE:
  a_c = (1/π) · (K_IC / (σ · F))²
  For design stress σ and K_IC: minimum detectable crack must be ≤ a_c/2
  Smaller K_IC → smaller critical crack → harder inspection requirement

PARIS LAW (fatigue crack propagation):
  da/dN = C · (ΔK)^m    [crack growth per cycle]
  ΔK = ΔS · √(πa) · F   (stress intensity range)
  C, m = material constants; for 2024-T3: m ≈ 3-4
  Integration: N = ∫ da / (C · ΔK^m) from a_initial to a_critical
  → gives crack propagation life (inspection interval)

DAMAGE TOLERANCE DESIGN (FAR 25.571):
  Assume initial flaw size (from inspection limit) exists in most critical location
  Calculate: how fast does it grow under service spectrum loading?
  Inspection interval = a × (number of flights to grow from detectable to critical) / SF
  Safety factor (SF): typically 2× on crack growth life
  Residual strength: cracked structure must sustain limit load with assumed crack

SAFE-LIFE vs FAIL-SAFE vs DAMAGE TOLERANCE:
  ┌──────────────────┬───────────────────────────────────────────────────────┐
  │ Safe-life        │ Retire part before predicted failure; used for:        │
  │                  │ landing gear, wing attach fittings (single load path)  │
  │                  │ Scatter factor 3-4 on test life                        │
  ├──────────────────┼───────────────────────────────────────────────────────┤
  │ Fail-safe        │ Multiple load paths; partial failure detectable before │
  │                  │ total failure; fuselage skin, stringers                │
  │                  │ Must sustain 80% design limit load with element failed  │
  ├──────────────────┼───────────────────────────────────────────────────────┤
  │ Damage tolerant  │ Fracture mechanics; flaw assumed present; crack growth │
  │                  │ rate analyzed; inspection interval set                 │
  │                  │ Now dominant philosophy per FAR 25.571 Amendment 45    │
  └──────────────────┴───────────────────────────────────────────────────────┘
```

---

## 8. Aeroelasticity

```
AEROELASTICITY TRIANGLE (Collar's triangle):
  Three disciplines interact:
    Aerodynamics (A): air loads depend on shape
    Elasticity (E): shape deforms under loads
    Inertia (I): mass resists acceleration
  Intersections:
    A+E: static aeroelasticity (divergence, aileron reversal, load redistribution)
    A+I: aerodynamic flutter — wait, this is all three
    E+I: structural vibration (free vibration)
    A+E+I: dynamic aeroelasticity (flutter)

DIVERGENCE (static; A+E):
  Wing under lift → twists (pitch up) → more lift → more twist → divergence
  Divergence speed: q_D where aerodynamic pitching moment gradient overcomes torsional stiffness
  q_D = GJ / (e × a × c × l)   (simplified; e = distance from AC to EA)
  Forward-swept wing (FSW): strongly susceptible to divergence
    Experimental X-29: used CFRP to tailor stiffness; avoided divergence artificially
  Swept-back wing: geometry provides wash-out → more divergence-resistant

AILERON REVERSAL (static; A+E):
  Aileron down → nose-down twisting moment on wing → wash-out → less lift
  At reversal speed: aileron has zero effect (down aileron → wing twists → net zero roll)
  Above reversal speed: aileron has reversed effect
  Mitigation: use spoilers instead of outboard ailerons at high speed (B747, B777)
  Modern FBW: inboard ailerons only above certain speed; no reversal issue

FLUTTER (dynamic; A+E+I):
  Coupled bending-torsion oscillation; amplitude grows exponentially if not damped
  Physical mechanism: aerodynamic moment in phase with torsional velocity → energy input
  Flutter speed V_F: must be > 1.15 × VD (design dive speed) per FAR 25.629
  Eigenvalue analysis: structural modes + aerodynamic damping → eigenvalues
    Flutter occurs when imaginary part of eigenvalue crosses zero → unstable
  V-g plot: structural damping g vs airspeed V; flutter when required g < structural damping
  Prevention: increase torsional stiffness; add mass balance at leading edge (raises coupling freq)
    Boeing 787 GVT: ~3,000 accelerometers; maps all structural modes before first flight

GROUND VIBRATION TEST (GVT):
  Aircraft suspended on soft supports; swept-sine or random excitation; measure response
  Extract: natural frequencies, damping ratios, mode shapes (bending, torsion, combined)
  Flutter analysis: use GVT-verified structural model + aero model → flutter clearance
  Required: before first flight; after major structural modification

LOAD ALLEVIATION (active aeroelasticity):
  Gust load alleviation (GLA): detect gust (accelerometers); deflect spoilers/ailerons fast
    → reduce structural loads; allows lighter wing; Boeing 787 uses GLA actively
  Maneuver load alleviation (MLA): during maneuvers, shift lift inboard; reduce wing bending moment
  Wing flex: A350 tip deflects ~4-5 m at limit load; B787 ~7 m; must analyze aerodynamics
    on deformed shape (aeroelastic coupling = geometrically nonlinear problem)
```

---

## 9. Thermal Loads and High-Speed Structures

```
AERODYNAMIC HEATING:
  Recovery temperature: T_r = T_∞ × (1 + r × (γ-1)/2 × M²)
    r = recovery factor ≈ 0.85 (laminar), 0.88 (turbulent)
  At M=2: T_r ≈ 400 K (127°C); Al alloys lose strength (Al limit ~120°C sustained)
  At M=3 (SR-71): T_r ≈ 600 K (327°C); titanium required (Ti-6Al-4V good to ~550°C)
  Concorde M=2.0: titanium + Al-Cu skin; carefully managed heating

THERMAL EXPANSION MISMATCH:
  CTE mismatch at CFRP-metal joints:
    Al: α ≈ 23 ppm/°C
    CFRP (0° laminate): α ≈ -1 to +2 ppm/°C (near-zero or negative axially)
    Ti: α ≈ 8.6 ppm/°C
  Temperature excursions from -55°C (cruise) to +70°C (ground soak): ΔT = 125°C
  Thermal stress: σ = E × Δα × ΔT → need compliant joints or careful layup

COMPOSITE-METAL INTERFACE (A350/B787):
  CFRP fuselage barrel → titanium frames/intercostals → Al floor structure
  Joint design: shimming, sealant layers, titanium/CFRP fastener pairs
  Galvanic corrosion: CFRP is cathodic relative to Al → must isolate with glass ply/fiberglass
  Moisture absorption: CFRP swells slightly; must account for hygroscopic expansion

SPACE STRUCTURES:
  Extreme ΔT: -170°C (shadow) to +120°C (sunlight) → ΔT = 290°C
  All-CFRP boom structures: near-zero CTE needed for dimensional stability
  INVAR (Fe-Ni36): near-zero CTE; used for tooling, mirror mounts, spacecraft booms
```

---

## 10. Structural Certification (FAR 25)

```
FAR 25 STRUCTURAL REQUIREMENTS:

LOAD FACTORS:
  Limit load: maximum loads expected in service (once per lifetime probability basis)
  Ultimate load: 1.5 × limit load; must sustain for ≥ 3 seconds without collapse
  Proof load: 1.0 × limit load; no permanent deformation

STATIC TEST:
  Physical test of airframe or component to ultimate load (1.5 × limit)
  Most destructive test: take structure to failure; verify failure mode and margin
  Full-scale static test: one complete airframe; representative loading via hydraulic jacks
  Test article must be structurally representative; material coupons verify properties

FATIGUE / DAMAGE TOLERANCE TESTS:
  Full-scale fatigue test: two-lifetime spectrum test (2 × DSO — design service objective)
  DSO: service life in cycles; B737 original DSO = 75,000 flights; 737-900 = 75,000+
  Test article: second complete airframe; pressurized + maneuver loads applied cyclically
  Special fatigue tests: fuselage panels (blowout), wing root attachments, landing gear

SERVICE BULLETIN COMPLIANCE:
  Age/stress/corrosion: mandatory service bulletins (airworthiness directives — ADs)
    from FAA/EASA require inspection or repair by flight cycle/hour limits
  B737 classic: multiple corrosion/fatigue ADs from age
  A380 wing rib foot cracking: SB + AD for inspection/repair (2012 discovery)

WEIGHT AND BALANCE:
  Structural analysis requires known CG range; FAR 25 specifies forward/aft CG limits
  Structural limits vary with CG → loading envelope documents
  OEM issues weight and balance manual; operator tracks ZFW CG on every flight

CERTIFICATION TESTING SUMMARY:
  ┌─────────────────────────────────────────────────────────────────┐
  │  Test Type          | Article | Objective                       │
  ├─────────────────────────────────────────────────────────────────┤
  │  Material coupons   | coupons | Allowables database            │
  │  Component tests    | part    | Joint/fitting strength          │
  │  Subcomponent tests | section | Panel/box beam strength         │
  │  Full-scale static  | airframe| Ultimate load; failure margin  │
  │  Full-scale fatigue | airframe| 2× DSO; crack growth/inspection │
  │  GVT               | airframe| Flutter clearance modes         │
  │  Drop test          | gear    | Landing energy absorption      │
  │  Bird strike        | windshield/fan| Regulatory requirement   │
  └─────────────────────────────────────────────────────────────────┘
```

---

## 11. Finite Element Method in Aerospace

```
FEM OVERVIEW:
  Discretize structure into elements connected at nodes; solve for nodal displacements
  Global: [K]{u} = {F}   (stiffness × displacement = force)
  Element types for aerospace:
    Rod elements: axial force only (stringers, cables)
    Beam elements: bending + shear + torsion (frames, spars)
    Plate/shell elements: thin 2D; bending + in-plane (skin panels)
    Solid elements: 3D; rarely used in global models (too many DOF)

AEROSPACE FEM HIERARCHY:
  ┌────────────────────────────────────────────────────────────┐
  │  Level 1: Stick model (beam elements)                      │
  │    Entire wing as beam; global load distribution; fast     │
  │    Used: loads surveys, aeroelastic analysis               │
  ├────────────────────────────────────────────────────────────┤
  │  Level 2: Box beam model (plate elements)                  │
  │    Wing box with panels; skin, spars, ribs                 │
  │    Millions of DOF; used for stress analysis               │
  ├────────────────────────────────────────────────────────────┤
  │  Level 3: Detailed models (local submodels)                │
  │    Fastener patterns, cutouts, ply-by-ply composites       │
  │    Driven by boundary conditions from Level 2              │
  └────────────────────────────────────────────────────────────┘

PRACTICAL NOTES:
  Element quality: avoid distorted elements (aspect ratio > 5-10); check Jacobian
  Boundary conditions: correctly replicate support conditions; not too stiff, not too free
  Mesh convergence: refine mesh at stress concentrations; check convergence of max stress
  Buckling analysis: linear eigenvalue → approximate; nonlinear FEM for true post-buckling

NASTRAN (MSC/NX): dominant aerospace FEM solver; bulk data deck format; legacy
ABAQUS: popular for nonlinear analysis (crash, impact, fatigue)
ANSYS: widely used; good for composites, thermal coupling
```

---

## 12. Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| Upper vs lower wing skin critical failure mode? | Upper: compression/buckling; Lower: tension/fatigue |
| Limit vs ultimate load? | Limit = max expected service; Ultimate = 1.5 × limit; must not collapse at ultimate |
| Fail-safe vs damage tolerance? | Fail-safe = redundant paths; damage tolerance = fracture mechanics + inspection intervals |
| Best Al alloy for fuselage skin? | 2024-T3 (good fracture toughness, fatigue); not 7075 (lower toughness) |
| Why CFRP for primary structure? | Specific stiffness/strength much higher than metals; also enables tailored CTE |
| Galvanic issue with CFRP on Al? | CFRP cathodic, Al anodic → Al corrodes at junction; isolate with glass ply |
| Flutter prevention approaches? | Increase torsional stiffness; mass balance leading edge; reduce chord; FBW active |
| What is the Bredt-Batho formula for? | Shear flow in closed thin-walled section under torsion: T = 2·A_enc·q |
| Paris law exponent m for Al? | m ≈ 3-4; higher m = faster growth per ΔK increment |
| V_F requirement per FAR 25? | Flutter must not occur below 1.15 × V_D (design dive speed) |
| Critical crack size formula? | a_c = (K_IC / (σ√π · F))² / π |
| Symmetric laminate B matrix? | B = 0 (no bending-extension coupling) |
| Aileron reversal solution for high speed? | Use inboard ailerons + spoilers; FBW limits to inboard surface above cutover speed |
| GVT purpose? | Extract structural modes; verify flutter analysis model before first flight |

---

## Common Confusion Points

**Limit load ≠ yield load:** FAR 25 says no permanent deformation at limit load (so yield is the limit), and no collapse at ultimate (1.5× limit). The 1.5× safety factor is the legacy safety factor for structural uncertainty, not the factor against yield.

**Fatigue life vs fracture mechanics life:** S-N is initiation-dominated (how long to form a crack). Paris law is propagation-dominated (how fast an existing crack grows). Real aircraft use both: S-N to screen for hot spots; fracture mechanics to set inspection intervals once cracking is expected.

**Static aeroelasticity ≠ flutter:** Divergence and aileron reversal are static phenomena — they occur at a steady speed without oscillation. Flutter is dynamic — requires the interaction of bending and torsion frequencies with aerodynamic phase shift. Both are problems; flutter is catastrophic (exponentially growing oscillation), while divergence is a static instability.

**7075 vs 2024 selection:** 7075 has higher static strength → better for compression (upper wing). 2024 has better fracture toughness → better for tension/fatigue/fuselage. Using 7075 on fuselage is a mistake (happened historically → stress corrosion problems). Not just about ultimate strength — fracture toughness for damage tolerance governs fuselage selection.

**CFRP zero CTE is directional:** CFRP has near-zero CTE along fiber direction, but ~30-40 ppm/°C in the transverse direction (through thickness). Quasi-isotropic layup gives roughly 3-5 ppm/°C in-plane — much lower than metals but not zero. Tailored layup required for dimensional stability applications (optical structures, space structures).

**FEM stress concentration convergence:** Stress at a singularity (sharp re-entrant corner, point load) diverges with mesh refinement — infinite stress in elastic theory. Real structures don't have perfect corners; use design notch radius or fracture mechanics approach rather than trying to converge the FEM at the singular point.
