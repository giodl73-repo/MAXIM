# Damage Mechanics and NDT Inspection

## The Big Picture

```
+------------------------------------------------------------------+
|              COMPOSITE DAMAGE AND INSPECTION LANDSCAPE           |
|                                                                  |
|   DAMAGE TYPES            NDT METHODS           DECISIONS        |
|   ────────────            ───────────           ─────────       |
|   Impact (BVID/VID)       Ultrasonic C-scan      Repair          |
|   Delamination            Tap test               No action       |
|   Matrix cracking         Thermography           Monitor         |
|   Fiber fracture          Shearography           Remove from svc |
|   Bond failure            X-ray (CT)                             |
|   Disbond                 Eddy current           REPAIR TYPES:   |
|   Moisture ingress        Acoustic emission       Resin injection |
|                                                                  |
|   BARELY VISIBLE IMPACT DAMAGE (BVID) — the critical concept   |
|   Definition: damage not detectable in normal walk-around       |
|   Design must tolerate BVID for entire service life             |
+------------------------------------------------------------------+
```

---

## Damage Mechanisms in Composites

### Impact Damage — Primary Concern

```
   LOW-VELOCITY IMPACT (< 10 m/s):
   ─────────────────────────────────
   Source: tools dropped during maintenance, runway debris, hail
   Typical mass × velocity: 1 kg × 5 m/s, 2.3 kg × 6 m/s (FAA requirement)

   DAMAGE SEQUENCE:
   ──────────────────
   Initial contact: compressive through-thickness stress cone
   → Matrix cracks propagate radially from impact point
   → Delaminations grow at ply interfaces (driven by interlaminar shear)
   → Conical delamination pattern (each ply interface, growing with depth)
   → Fiber fracture at back face (tension) when contact force high

   SURFACE APPEARANCE:
   ────────────────────
   Small dent (0.1–3 mm depth for BVID threshold)
   Subsurface: large delamination (~3–10× projected surface damage area)
   "Iceberg effect": most damage invisible from surface

   BVID DEFINITION (FAA AC 20-107B):
   ───────────────────────────────────
   Damage not found during walk-around / preflight inspection
   ≤ 0.3 in. (7.6 mm) dent depth → BVID
   > 0.3 in. and visible from 1.5 m → VID (Visible Impact Damage)
   Structure must sustain BVID for full design service life
   Structure must sustain limit load with VID
```

### Delamination

```
   DELAMINATION SOURCES:
   ──────────────────────
   Impact damage (see above)
   Manufacturing defects (incorrect cure, poor consolidation, trapped air)
   Fatigue cracking from cyclic loads at ply interfaces
   Free edge interlaminar stresses (CLT analysis misses this)
   Ply drop-offs: thickness change → interlaminar stress concentration
   Joints and fastener holes: peel stresses

   DELAMINATION GROWTH:
   ─────────────────────
   Static: above critical G > GIc or GIIc (fracture mechanics)
   Fatigue: Paris law: da/dN = C · ΔG^m
   Mixed mode: interaction (GI/GIc + GII/GIIc)^n = 1 or similar

   COMPRESSION AFTER IMPACT (CAI):
   ──────────────────────────────────
   Delamination buckling under compressive load
   Buckled delamination → propagation → catastrophic
   Critical: delamination orthogonal to load direction
```

### Matrix Cracking

```
   TRANSVERSE MATRIX CRACKS:
   ───────────────────────────
   Grow perpendicular to fiber direction in off-axis plies
   Onset: σ2 > X2T or τ12 > S12 at ply level
   Detectable by: X-ray with dye penetrant, edge replication, CT
   Not immediately structural failure but:
   → Reduce ply stiffness
   → Provide moisture ingress path to fiber-matrix interface
   → Initiate delamination at crack tips

   CRACK DENSITY:
   ───────────────
   Increases with applied load
   Saturates at "characteristic damage state" (CDS) — matrix crack spacing
   equal to ply thickness
   Beyond CDS: delaminations connect transverse cracks → rapid degradation
```

---

## Non-Destructive Testing (NDT) Methods

### Ultrasonic Testing (UT) — Gold Standard

```
   PULSE-ECHO METHOD (single transducer):
   ──────────────────────────────────────
   Transducer emits ultrasonic pulse (2–10 MHz typical for CFRP)
   Pulse travels through material
   Echoes from defects (delaminations, voids) detected
   Time of flight → depth of defect
   Signal amplitude → defect severity

   THROUGH-TRANSMISSION (TTU — two transducers):
   ───────────────────────────────────────────────
   Transmitter on one side, receiver on other
   Signal attenuation → defect presence
   Cannot determine depth — only presence
   Faster than pulse-echo for large panels

   C-SCAN:
   ───────
   Automated scanning of transducer across part
   Amplitude or TOF mapped as grayscale image
   Shows plan-view map of defect location
   Resolution: 1–5 mm depending on frequency and scan resolution
   Result: C-scan image with defect areas shown dark (attenuation)

   WATER COUPLING:
   ───────────────
   Ultrasound requires coupling medium (air has huge impedance mismatch)
   Water squirter (jet of water between transducer and part)
   Immersion tank (for small parts)
   Phased array (electronic scanning — faster, better for complex geometry)

   AUTOMATED UT FOR 787 BARRELS:
   ────────────────────────────────
   Robotic C-scan systems: ~8 m × 6 m barrel scanned in ~2–4 hours
   Every barrel inspected before assembly
   Typical reject rate: ~2–5% of barrels need repair or reject
```

### Tap Test

Simplest method: tap the surface and listen.

```
   TAP TEST:
   ──────────
   Tap composite surface with coin, hammer, or calibrated device
   Sound:
   - "Solid" (high pitch): good laminate, no delamination
   - "Dull/hollow" (lower pitch): delamination below surface

   PHYSICS:
   ────────
   Bonded area: high bending stiffness → high resonant frequency
   Delaminated area: reduced stiffness → lower frequency (dull sound)

   LIMITATIONS:
   ─────────────
   Only detects surface-parallel delaminations
   Not quantitative (depth, size not determinable)
   Operator-dependent (subjective interpretation)
   Effective for thin laminates and accessible surfaces

   DIGITAL TAP HAMMER:
   ────────────────────
   Accelerometer in tip: measures contact duration
   Short contact: good laminate
   Long contact: delamination (softer surface)
   Provides quantitative indication, printable record
   Used: Boeing, Airbus repair stations for routine inspection
```

### Thermography (Infrared Thermography)

```
   PULSED THERMOGRAPHY:
   ──────────────────────
   Flash lamp: 1–5 ms pulse heats composite surface
   IR camera records surface temperature vs. time
   Heat diffuses into material: T(x,t) ~ Gaussian diffusion

   AT DELAMINATION:
   ──────────────────
   Air gap (delamination): blocks heat diffusion
   Above delamination: surface stays hotter longer → "hot spot" in IR image
   Image at appropriate time delay → defect map

   LOCK-IN (MODULATED) THERMOGRAPHY:
   ─────────────────────────────────────
   Periodic heating at frequency f
   Lock-in amplifier: detect amplitude and phase of surface temperature
   Phase image: less sensitive to surface emissivity variations
   Better for thick materials

   ADVANTAGES:
   ────────────
   Full-field, fast inspection (large area in one shot)
   Non-contact
   One-sided access only needed

   LIMITATIONS:
   ─────────────
   Depth resolution limited (d_max ~ few mm for CFRP)
   Less sensitive than UT for deep or small defects
   Emissivity variation: surface paint, contamination affects result

   APPLICATIONS:
   ──────────────
   Aircraft maintenance inspection (wings, empennage)
   Production inspection of large panels
   Honeycomb structure: excellent for skin/core disbond detection
```

### Shearography

```
   DIGITAL SHEAROGRAPHY:
   ──────────────────────
   Laser illuminates composite surface
   Camera captures speckle pattern
   Load applied (vacuum, thermal, vibration)
   Subtract before/after speckle patterns → differential displacement map

   PHYSICS:
   ─────────
   Defect (delamination, void): changes local deformation under load
   → Anomalous displacement gradient → shearogram shows fringe anomaly

   ADVANTAGES:
   ────────────
   Full-field, fast
   Not sensitive to rigid body motion (gradient measurement)
   Can inspect curved surfaces
   Used in industry: aircraft, wind blade inspection

   LIMITATIONS:
   ─────────────
   Requires access to apply load (not always possible in service)
   Depth: moderate sensitivity
   Quantitative calibration: complex

   AEROSPACE USE:
   ───────────────
   Airbus inspection of large aircraft panels
   Wind turbine blade delamination mapping
```

### X-Ray Computed Tomography (CT)

```
   INDUSTRIAL X-RAY CT:
   ──────────────────────
   Rotate sample through 360° while X-ray source scans
   Reconstruct 3D volume from 2D projection images
   Resolution: 5–200 µm (depending on part size vs. focal spot)

   CAN DETECT:
   ────────────
   Voids (void content, shape, distribution)
   Delaminations (3D crack map)
   Fiber architecture (misalignment, fiber waviness)
   Matrix cracks (at high resolution)
   Internal metallic inclusions

   APPLICATIONS IN COMPOSITES:
   ────────────────────────────
   Coupon characterization (research, development)
   Failure analysis: post-test damage mapping
   Production: spot check for critical parts
   Not used for large structures (size limit: ~300mm diameter typically)

   SYNCHROTRON CT:
   ────────────────
   Very high resolution (sub-micron)
   Can visualize individual fiber fracture
   Only at synchrotron facilities
   Research tool, not production inspection
```

---

## Damage Assessment and Repair Decisions

### Damage Assessment Framework

```
   DAMAGE CLASSIFICATION:
   ──────────────────────
   Category 1: Normal degradation (superficial)
   → No repair needed
   Category 2: Allowable damage limits (ADL)
   → Repair allowed later / monitor
   Category 3: Repairable within AMM (Aircraft Maintenance Manual)
   → Repair per Boeing/Airbus approved procedure
   Category 4: Repairable by manufacturer/specialized shop
   → Part removal + factory repair
   Category 5: Replace the component
   → Beyond repair limits
```

### Repair Methods

```
   RESIN INJECTION:
   ──────────────────
   Delamination with accessible edge or through-hole
   Low-viscosity epoxy injected under vacuum
   → Re-bonds delamination plane
   Strength recovery: ~80–90% of original (depending on surface quality)
   Use: shallow delaminations, matrix cracks

   BONDED PATCH (FLUSH OR EXTERNAL):
   ────────────────────────────────────
   Material removed / cleaned around damage
   CFRP or woven CF/epoxy patch bonded with structural adhesive (FM300, EA9696)

   EXTERNAL (bolted or bonded):
   Over-ply patch
   → Quick, no removal of parent material
   → Aerodynamic surface disturbed (only for non-critical applications)

   FLUSH REPAIR (step or taper):
   → Remove damaged material in tapered/stepped region
   → Wet lay-up or prepreg scarf repair
   → Vacuum cure or heat blanket cure
   → Restore original contour
   → Required for primary aerodynamic structure

   SCARF RATIO: typically 1:20 to 1:50 for repairs
   1:20 = for every 1 mm depth, 20 mm scarf radius
   → Large repair footprint for thick structure
```

---

## Inspection Intervals and Regulations

```
   FAA/EASA REGULATORY BASIS:
   ─────────────────────────────
   14 CFR 25.571: Damage Tolerance requirements for transport category
   → Structure must sustain limit load with maximum damage not
     detectable by inspection (BVID)
   → Fail-safe: no catastrophic failure before detection (VID)

   787 INSPECTION PROGRAM (sample):
   ──────────────────────────────────
   Pre-flight walk-around: visual for VID
   "A" check (~500 flight hours): detailed visual inspection
   "C" check (~3,000–5,000 hours): tap test + UT scan critical areas
   Structural inspection plan: specific UT zones at defined intervals
   Impact event report: any impact → mandatory inspection

   WIND TURBINE BLADES:
   ──────────────────────
   Annual visual inspection (BVID threshold ~1 mm depth)
   Thermography scan: every 2–5 years
   UT shear wave scan: specific zones at 5–10 year intervals
   Drone-based visual inspection: becoming standard
```

---

## Decision Cheat Sheet

| Inspection need | Method |
|-----------------|--------|
| Quick area scan, large panel | UT pulse-echo C-scan or phased array |
| One-sided, non-contact, large area | Pulsed thermography |
| Curved surfaces, rapid survey | Shearography |
| Field repair shop (hands-on) | Digital tap test |
| Characterize void content (lab) | X-ray CT |
| Through-thickness crack / disbond | UT through-transmission |
| Honeycomb skin disbond | Thermography or tap test |
| Matrix crack mapping (research) | Dye-penetrant X-ray or micro-CT |

---

## Common Confusion Points

**BVID is not "invisible damage"**: It's damage not detectable in a normal
walk-around inspection (looking from a distance, no special equipment). Under
close inspection with UT or thermography, BVID-threshold dents (0.3 mm = 0.012 in.)
and the underlying delaminations are clearly detectable. The definition is
calibrated to inspection practice, not to detectability in principle.

**Tap test misses delaminations parallel to outer surface at depth**: A delamination
at, say, 5 mm depth in a 6 mm thick skin may not change surface tap frequency
enough to detect. UT sees it. Tap test is reliable for shallow (< 2–3 mm)
delaminations and thin laminates. Don't substitute tap test for UT on primary
structure.

**Repair restores strength but not all properties**: A properly executed scarf
repair restores ~80–90% of original static strength. Fatigue properties of the
repaired region are less well-characterized. Repairs near critical details
(fastener holes, load introduction, curved zones) may not fully restore
damage-tolerant behavior — reason for strict repair limitations in AMM.
