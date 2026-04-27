# Welding

## The Big Picture

Welding is **permanent joining by fusion** — creating a continuous metallic bond through localized melting, with or without filler metal. It is distinguished from brazing (base metal doesn't melt), soldering (lower-temp brazing), and mechanical fastening (no metallurgical bond). The central engineering challenge is managing the severe thermal gradient: melting at ~1500°C while room temperature exists 50mm away, in microseconds.

```
WELDING PROCESS LANDSCAPE:

  HEAT SOURCE           PROCESS              SHIELDING        TYPICAL USE
  ─────────────────────────────────────────────────────────────────────────
  Electric arc          SMAW (stick)         Flux coating     Field repair, pipework
  (consumable)          GMAW / MIG           Gas (Ar/CO₂)     Production steel/Al
                        FCAW                 Flux core        Outdoor steel
                        SAW                  Flux granular    Heavy plate, ship hull

  Electric arc          GTAW / TIG           Gas (Ar/He)      Thin SS, Ti, root pass
  (non-consumable)      PAW                  Gas + plasma     Precision, aero

  Resistance            Spot / seam          Self (squeeze)   Automotive body panels
  High energy           Laser / EBW          Vacuum/gas       Aero, medical, precision

  No fusion             Friction stir (FSW)  None needed      Al aerospace (no HAZ)
                        Explosive welding    None             Clad plate, dissimilar

ENERGY DENSITY SPECTRUM:
  SMAW                  ~10² W/cm²  — wide HAZ, low speed
  GMAW/SAW              ~10³ W/cm²  — moderate
  Laser/EBW             ~10⁶ W/cm²  — narrow HAZ, high speed, high distortion risk

INPUTS → WELD → OUTPUTS:
  Voltage (V)                             Weld bead geometry
  Current (A)           ──────────►       HAZ width and character
  Travel speed (mm/s)   (Heat input)      Dilution ratio
  Wire feed rate                          Residual stress + distortion
  Shielding gas                           Microstructure of weld zone
```

---

## Process Mechanics: SMAW, GMAW, GTAW, SAW

### SMAW — Shielded Metal Arc Welding (Stick)

```
SMAW (ELECTRODE 7018 — LOW HYDROGEN):

  Power supply                  Flux coating (calcite, rutile, or cellulosic)
  (DCEP or AC)    Electrode     ─────────────────┐
                    │           Core wire (ER)    │
  60–90V OCV        │           ←────────────────┤
  20–30V arc        ▼           Slag forms over   │
                  ══════ arc    molten pool ───── ┘
                  ════════════
                  Base metal → puddle → solidifies under slag

ELECTRODE DESIGNATION (E7018):
  E = electrode
  70 = 70 ksi tensile strength
  1 = all-position (flat/horiz/vert/overhead)
  8 = low-hydrogen flux; DCEP or AC; ~8% iron powder

SHIELDING MECHANISM:
  Flux coating decomposes → CO₂ + CO gas shield (keeps O₂/N₂ out)
  Slag floats on pool → covers while solidifying → remove after
  Low-hydrogen electrodes (7018): minimize H₂ → prevent cold cracking

CHARACTERISTICS:
  Heat input: moderate (depends on travel speed + current)
  Deposition rate: low (~1–3 kg/hr)
  Positions: all (welder controls travel speed, angle)
  Setup: minimal — can work in field, wind, awkward position
  Limitations: stub loss (~50mm per electrode); stop/starts; slag removal
```

### GMAW — Gas Metal Arc Welding (MIG)

```
GMAW PROCESS:

  Wire spool → wire feed motor → contact tip → arc → weld pool
  Shielding gas nozzle surrounds wire → blankets pool

TRANSFER MODES (determined by voltage, current, wire diameter, gas):

  SHORT CIRCUIT  (<22V, low current):
    Wire dips into pool → short circuits → melts off → arc re-establishes
    ~100 Hz rate; low heat input; thin material; good out-of-position
    Risk: incomplete fusion if parameters wrong

  GLOBULAR        (intermediate — avoid in practice):
    Large irregular droplets → spatter; poor control

  SPRAY           (>26V, >200A, >80% Ar in shield gas):
    Continuous stream of fine droplets across arc; stable; high deposition
    High heat input → flat/horizontal only; excellent fusion
    Typical for heavy structural steel

  PULSE (GMAW-P):
    Electronically alternates high/low current → spray transfer but lower avg heat
    Joins spray fusion quality with positional capability
    Required for aluminum (prevents burn-through) and some stainless

GAS SELECTION:
  C25 (75% Ar / 25% CO₂): standard for mild steel; balance arc stability vs cost
  100% CO₂: cheaper; more spatter; deeper penetration
  100% Ar: aluminum (CO₂ causes contamination/porosity in Al)
  Tri-mix (Ar/He/CO₂): stainless — controls carbon contamination risk

DEPOSITION: ~3–8 kg/hr; continuous wire → high productivity vs SMAW
```

### GTAW — Gas Tungsten Arc Welding (TIG)

```
GTAW PROCESS:

  Non-consumable W electrode → arc to base metal
  Filler rod added by hand (or autogenous — no filler)
  Inert gas (Ar or He) — 100% coverage; no flux

TORCH:
  Tungsten electrode (pure W for AC/Al; 2% ThO₂ or LaO₂ for DCEN SS/steel)
  Cup (ceramic/glass) + gas lens → laminar shielding
  Foot pedal amperage control → ramp up for starts; down for crater fill

POLARITY EFFECTS:
  DCEN (electrode negative, base positive):
    Deep penetration; narrow bead; electrode stays cool → smaller tip
    → Standard for steel, stainless, titanium, copper

  DCEP (electrode positive):
    Shallow; wide bead; but → cathodic cleaning removes Al₂O₃ oxide
    → Necessary for aluminum (breaks oxide before fusion)

  AC (alternating): combines both — DCEP half-cycle cleans Al₂O₃;
                    DCEN half-cycle provides penetration
    → Standard for aluminum GTAW

CHARACTERISTICS:
  Heat input: low → precise
  Deposition rate: very low (0.5–2 kg/hr) — speed is not the point
  Weld quality: highest → no slag, no spatter, precise bead
  Applications: root passes in pipe, thin-wall stainless, titanium, aero
  Limitations: slow; requires highly skilled operator; sensitive to contamination

INTER-PASS AND ROOT PASS:
  TIG root pass → SMAW or GMAW fill passes (common pipe procedure)
  Root pass quality determines structural integrity of full weld
```

### SAW — Submerged Arc Welding

```
SAW PROCESS:

  Bare wire electrode (continuous) → beneath granular flux blanket
  Arc is invisible (submerged) → no UV hazard
  Flux: fused or agglomerated (SiO₂, MnO, CaO, etc.)

  Wire reel → contact tip
  Hopper → flux blanket ────────────────────────────
                          ══════ arc (invisible)  ══
                          ████████ molten pool ████
                          solidified weld + slag flux

CHARACTERISTICS:
  Heat input: very high → deep penetration; narrow weld for thick plate
  Deposition rate: 10–40 kg/hr → highest productivity
  Position: flat only (flux would fall off in vertical/overhead)
  Weld quality: excellent → no atmospheric contamination

APPLICATIONS:
  Heavy structural steel (shipbuilding, pressure vessels, pipelines)
  Longitudinal seam welds on large diameter pipe
  Spiral pipe production
  Heavy plate overlay (cladding)

HEAT INPUT FORMULA:
  HI (kJ/mm) = (Voltage × Current × 60) / (1000 × Travel Speed mm/min)
  Typical SAW: 3–5 kJ/mm vs TIG: 0.3–1 kJ/mm
  High heat input → larger HAZ → more distortion
  Low heat input → risk of incomplete fusion, hydrogen cracking
```

---

## Process Comparison Matrix

```
PROCESS COMPARISON:

  Process   Shield      Position    Deposition  Quality  Cost/Setup  Skill
  ─────────────────────────────────────────────────────────────────────────
  SMAW      Flux coat   All         Low         Good     Very low    High
  GMAW      Gas         All*        Mod-high    Good     Moderate    Moderate
  FCAW      Flux+gas    All         High        Good+    Moderate    Moderate
  GTAW      Gas         All         Very low    Highest  High        Very high
  SAW       Flux gran   Flat only   Very high   High     High        Moderate
  Laser     None/gas    All         Low         High     Very high   Automated

  *GMAW short-circuit mode for out-of-position; spray = flat/horiz only

KEY SELECTION DRIVERS:
  Field repair, no infrastructure → SMAW
  Production steel fabrication → GMAW (spray) or FCAW
  Critical root pass, thin/exotic material → GTAW
  Heavy plate, high volume → SAW
  Automotive panels, galvanized → resistance spot
  Aerospace aluminum structure → FSW (no fusion = no HAZ solidification crack)
```

---

## Weld Metallurgy

### Heat Affected Zone (HAZ)

```
WELD CROSS-SECTION ZONES:

  ← PARENT METAL | HAZ |←──── WELD METAL ────→| HAZ | PARENT METAL →

  Temperature during welding:
                                ↑ Liquidus (~1500°C for steel)
  Weld metal ──────────────────▲
  (solidified from melt)        │
                    ┌──────────┐│
  Coarse-grain HAZ  │          ││ δ-ferrite + austenite → martensite (rapid cool)
  (>1100°C)         │ CGHAL    ││ Grain growth → coarsen → lower toughness
  ──────────────────┘          │
  Fine-grain HAZ    ┌──────────┘
  (900–1100°C)      │ FGHAL     Reaustenitized but rapid → fine grain → good tough.
  ──────────────────┘
  Intercritical HAZ ┌──────────
  (700–900°C)       │ Partial re-austenitizing → mixed microstructure
  ──────────────────┘
  Tempered zone     ┌──────────
  (<700°C)          │ Softening of previously hardened microstructure
  ──────────────────┘
  BASE METAL        Unaffected

HAZ WIDTH:
  Increases with heat input, preheat; decreases with high travel speed
  Typical: SMAW = 3–10mm; TIG = 1–3mm; laser = 0.1–0.5mm
```

### Martensite Formation in HAZ

```
MARTENSITE RISK:

  Carbon equivalent (CE) predicts hardenability:
  CE = C + Mn/6 + (Cr+Mo+V)/5 + (Ni+Cu)/15

  CE < 0.40 → no preheat needed (most structural mild steels)
  CE 0.40–0.60 → preheat 100–200°C
  CE > 0.60 → high preheat + post-weld heat treatment (PWHT)

WHY MARTENSITE IS DANGEROUS IN HAZ:
  Rapid cooling (quench rate from ~1000°C to ambient):
  Austenite cannot transform to ferrite+pearlite → transforms to martensite
  Martensite = high hardness (>500 HV vs ~150 HV for ferrite)
  Martensite = hard + brittle + hydrogen trapping sites

COLD CRACKING (Hydrogen-Assisted Cracking — HAC):
  Three necessary conditions:
  1. Susceptible microstructure (martensite)
  2. Hydrogen (from moisture in flux, electrode coating, base metal)
  3. Tensile stress (residual stress from weld)
  → Can occur hours to days after welding (hydrogen diffuses to stress concentration)
  Prevention: low-hydrogen process/consumables + preheat + PWHT

PREHEAT FUNCTION:
  Slows cooling rate → martensite formation suppressed or reduced
  Drives hydrogen out (H₂ diffuses faster at elevated temperature)
  Reduces thermal gradient → less residual stress
  Required temperature depends on CE, plate thickness, hydrogen level
```

---

## Distortion and Residual Stress

```
DISTORTION MECHANISMS:

  Localized heating → thermal expansion → compression (constrained)
  Cooling → contraction → tension → residual stress

  ANGULAR DISTORTION (butt joint):
    Top of weld shrinks more than bottom (more heat at surface)
    → Joint closes at top → angular change

    Before welding: two flat plates butted together at a square joint.
    After welding:  the top of the joint closes inward, producing an
                    angular change (V-shape distortion).

  TRANSVERSE SHRINKAGE: weld metal cools → joint pulls inward
  LONGITUDINAL SHRINKAGE: along weld axis → bowing of long members

RESIDUAL STRESS DISTRIBUTION:
  Longitudinal (along weld):
    At weld centerline: tensile up to yield strength (≈ Fy)
    Near HAZ boundary: compressive (balanced)
  Transverse: tensile across weld; may reach yield in constrained joints

  Residual stress + applied load can exceed local yield → fatigue + fracture risk
  High-cycle fatigue life severely reduced by tensile residual stress

DISTORTION CONTROL STRATEGIES:
  Pre-setting: tack joints with gap/angle opposite to expected distortion
  Backstep welding: weld short segments in opposite direction to travel
  Clamps and fixtures: constrain joint during welding
  Balanced welding: alternating sides; distributes stress symmetrically
  Minimizing heat input: smaller beads; higher travel speed
  Weld sequence: weld toward free end; don't trap shrinkage

POST-WELD CORRECTION:
  Flame straightening: localized heating + forced cooling → controlled distortion
  Mechanical straightening: press, rolls (must not cold-crack)
  Vibratory stress relief (VSR): alternative to thermal for some alloys
```

---

## Pre- and Post-Weld Heat Treatment

```
PREHEAT:
  Purpose: slow cooling → avoid martensite; drive out hydrogen; reduce residual stress
  Applied: oxy-fuel torch, electric blankets, induction coils
  Temperature: held throughout welding (check with temperature crayon / thermocouple)
  Interpass temperature: minimum (keep warm) and maximum (don't overheat — austenite grain growth)

POST-WELD HEAT TREATMENT (PWHT):
  Also: Stress Relief Heat Treatment (SRHT)

  Temperature: ~595–650°C for carbon/low-alloy steel
    (below lower critical temperature Ac1 — no phase transformation)
  Hold time: 1 hr per inch of maximum thickness (minimum 1 hr)
  Heating/cooling rate: controlled (<55°C/hr for thick sections) to avoid thermal shock

  MECHANISMS:
    Residual stress relief: steel creeps at 600°C → stresses relax
    Hydrogen effusion: H₂ diffuses out rapidly at elevated temperature
    Martensite tempering: hard martensite → tempered martensite (tougher, softer)
    Carbide precipitation in sensitized SS (avoid PWHT 450–850°C range in austenitic SS)

  REQUIRED WHEN:
    Code requirement (ASME B31.3, AWS D1.1, ASME Section VIII)
    Heavy sections (>32mm typically)
    High CE steels
    Pressure vessels, cryogenic, nuclear service
    Hardness limit exceeded in HAZ

  SOLUTION ANNEALING (austenitic stainless):
    After welding → sensitization risk (Cr carbide precipitation at grain boundaries)
    Full solution anneal at 1040–1120°C → re-dissolves carbides → quench
    Alternatively: use low-carbon grades (304L, 316L) or stabilized (321, 347)
```

---

## Non-Destructive Testing (NDT)

```
NDT METHOD OVERVIEW:

  Method    Principle              Finds                   Limitations
  ─────────────────────────────────────────────────────────────────────
  VT        Visual                 Surface defects only    Resolution limit ~0.1mm
  PT        Liquid penetrant       Surface-open defects    Surface only; clean needed
  MT        Magnetic particle      Surface + near-surface  Ferromagnetic only
  UT        Ultrasound             Volumetric + surface    Operator skill; geometry
  RT        X-ray / gamma         Volumetric (all inside)  Radiation; 2D image only
  ACFM      Eddy current variant   Surface cracks          Conductive materials only
  TOFD      UT time-of-flight      Accurate flaw sizing    Requires calibration

VT — Visual Testing:
  First inspection step; always done
  Inspector eyes + mirror + light; magnifying glass (10×)
  Must meet: undercut limits, bead profile, spatter, crater cracks, size/length
  Enhanced: Video endoscope (borescope) for inaccessible areas

PT — Penetrant Testing:
  Apply penetrant (low-viscosity dye, red or fluorescent)
  Dwell time: 5–30 min (capillary action pulls into cracks)
  Remove excess penetrant
  Apply developer (white powder absorbs penetrant from crack → indication)
  Inspect: visible light or UV (fluorescent PT)
  Detects: surface cracks, porosity (open), laps, seams
  NOT for: subsurface flaws; rough surfaces mask indications

MT — Magnetic Particle Testing:
  Magnetize part (yoke, coil, prod) → apply iron particles (dry or wet)
  Magnetic flux leaks at surface/near-surface discontinuities → particles collect
  Only works on ferromagnetic metals (steel, iron, nickel)
  Detects: surface cracks, near-surface inclusions, lap defects

UT — Ultrasonic Testing:
  Transducer → high-frequency sound wave (~1–10 MHz) into material
  Sound reflects at interfaces (voids, cracks, inclusions, back wall)
  Echo time-of-flight → distance to reflector
  Amplitude → size estimate (with calibration)

  SCAN TYPES:
    A-scan: single point, amplitude vs time (oscilloscope view)
    B-scan: line scan → cross-section image
    C-scan: area scan → plan view (phased array, TOFD)

  Phased array UT (PAUT): electronically steered/focused beam
    → Replace multiple angle probes; real-time image; code-compliant

RT — Radiographic Testing:
  X-ray (60–400 kV) or gamma (Ir-192, Co-60, Se-75) source
  Film or digital detector behind part
  Dense inclusions absorb more → lighter on film; voids → darker
  Detects: porosity, slag, lack of fusion, cracks (if oriented to beam)
  Code films: IQI (image quality indicator) mandatory on every shot
  Limitations: radiation safety; 2D projection misses cracks perpendicular to beam

NDT SELECTION BY WELD DEFECT TYPE:
  Surface crack → VT + PT or MT
  Porosity/slag → RT (most intuitive) or UT
  Lack of fusion → UT (especially PAUT) or RT
  Undercut → VT + MT
  Lamellar tear → UT
  Root crack in pipe → RT or TOFD
```

---

## Weld Procedure Qualification (WPS/PQR)

The WPS/PQR/welder-qualification triad is structurally identical to a qualified CI/CD deployment pipeline: the procedure must be validated before use (PQR = integration test run), the operator must be individually certified (welder qualification = deployment approval gate), and the essential variables in the WPS are locked — changing base metal, filler, preheat, or process requires re-qualification, just as changing a pinned dependency or runtime version requires re-running the test suite. The system is auditable by code (AWS D1.1, ASME Section IX) rather than individual judgment.

```
QUALIFICATION SYSTEM (AWS D1.1, ASME Section IX):

  WPS (Weld Procedure Specification):
    Written document specifying all essential variables:
    → Base metal (P-number in ASME; group in AWS)
    → Filler metal (F-number, A-number)
    → Process (GMAW, GTAW, etc.)
    → Preheat + interpass temperature
    → Post-weld heat treatment
    → Position
    → Joint design + backing
    → Electrical parameters (voltage, current, wire feed)
    → Travel speed → heat input range

  PQR (Procedure Qualification Record):
    Actual test weld made to the WPS
    Test specimens extracted → destructive testing
    → Tensile: must meet base metal UTS minimum
    → Bend: root + face bend (2 of each) — no cracks >3mm
    → Charpy impact (if required by code/service temp)
    → Macro-etch: cross-section examination
    → Hardness traverse (HAZ hardness limit, e.g., 248 HV for sour service)
    PQR supports the WPS → must be kept as permanent record

  WELDER QUALIFICATION:
    Separate from WPS/PQR — qualifies the individual welder
    Welder performs a test groove weld → destructive + visual examination
    Passes → qualified for position, process, material group, thickness range
    Qualification expires if welder stops welding that process for >6 months

ESSENTIAL VARIABLES:
  Change outside qualified range → new PQR required
  Examples: base metal P-number change; filler metal F-number change;
            PWHT added/removed; position change (1G only → must retest for 6G)
  Non-essential variables: can change on WPS without re-qualification (travel speed, bead width)
```

---

## Decision Cheat Sheet

| Situation | Best Process |
|-----------|-------------|
| Field repair, no gas supply, wind | SMAW (self-shielded or FCAW-S) |
| Production steel fabrication, flat/horiz | GMAW spray or SAW |
| Out-of-position structural | GMAW short-circuit or FCAW |
| Thin stainless, titanium, root pass | GTAW |
| Heavy plate (>25mm) high volume | SAW |
| Aluminum aerospace (no HAZ crack) | FSW or GMAW pulse |
| Automotive body panels | Resistance spot |
| Detect internal defects volumetrically | RT (porosity/slag) or UT/PAUT (cracks) |
| Detect surface crack, non-ferrous | PT |
| Detect surface/near-surface, ferrous | MT |
| High-carbon/alloy steel welding | Preheat per CE + PWHT if required |
| Austenitic SS to avoid sensitization | Use 304L/316L or solution anneal |

---

## Common Confusion Points

**GMAW "MIG" is not one process — it's 3 different transfer modes**
Short-circuit, globular, and spray transfer have completely different heat inputs, penetration profiles, and positional capability. "Use MIG" is underspecified — you need to specify the transfer mode and shielding gas to define the process.

**The HAZ is more likely to fail than the weld metal itself**
In modern quality welds, the deposited weld metal is overmatched (higher strength than base metal). Failure under fatigue and fracture typically initiates in the HAZ (particularly the coarse-grain zone adjacent to the fusion line), not the weld center. NDT is focused there for this reason.

**Preheat slows cooling; it does not heat-treat**
Preheat prevents martensite by reducing the cooling rate. It is not the same as post-weld heat treatment (PWHT), which relieves residual stress and tempers any martensite already formed. Both may be required.

**RT detects volumetric defects; UT is better for planar defects**
Radiography is excellent for porosity and slag (volumetric, show as density contrast). But planar defects (cracks, lack of fusion) only show on RT if their plane is parallel to the X-ray beam — otherwise invisible. UT detects planar defects regardless of orientation.

**WPS and welder qualification are independent requirements**
A qualified WPS does not mean the welder is qualified. And a qualified welder doesn't validate the procedure. Both must be independently demonstrated and documented before production welding can proceed under code.
