# Manufacturing: Prepreg, Autoclave, and Infusion

## The Big Picture

```
+------------------------------------------------------------------+
|              COMPOSITE MANUFACTURING PROCESSES                   |
|                                                                  |
|   OPEN MOLD (wet lay-up)    CLOSED MOLD           AUTOMATED      |
|   ─────────────────────     ───────────           ─────────      |
|   Hand lay-up               RTM (Resin Transfer)  AFP/ATL        |
|   Spray-up                  HP-RTM                Filament wind  |
|   Infusion (VARTM)          Compression mold      Braiding       |
|                             Pultrusion             Robotic drape |
|                                                                  |
|   LOW COST / QUALITY ◄──────────────────────────► HIGH COST/Q  |
|                                                                  |
|   PREPREG + AUTOCLAVE: Aerospace gold standard                   |
|   → Highest Vf (60%), lowest void, controlled properties         |
|   → High cost, slow, large capital                               |
+------------------------------------------------------------------+
```

---

## Hand Lay-Up and Spray-Up

The simplest, lowest-capital processes. Still widely used for marine, civil,
and consumer products.

```
   HAND LAY-UP SEQUENCE:
   ──────────────────────
   1. Mold preparation: release agent (PVA, wax, mold release)
   2. Optional gel coat: surface cosmetic layer (polyester/vinyl ester)
   3. Layer resin on mold by brush or roller
   4. Apply fabric (woven GF/CSM) to wet resin
   5. Roll out air bubbles → consolidation
   6. Apply next resin layer
   7. Repeat to desired thickness
   8. Cure at room temperature (peroxide catalyst for UPE/VE)
   9. Demold after 2–24 hours

   Properties: Vf ~ 25–40%, void content ~ 2–5%
   Typical: GF/UPE or GF/VE
   Applications: boat hulls, pools, spa baths, architectural shapes
```

### Spray-Up

Gun applies chopped glass fiber (25–50 mm) + catalyzed resin simultaneously.
Lower skill requirement. Used for: bathtubs, shower trays, automotive hoods (low quality).
Properties: Vf ~ 15–25% (lower than hand lay-up), random fiber orientation.

---

## Vacuum Infusion (VARTM — Vacuum Assisted Resin Transfer Molding)

```
   SETUP:
   ──────
   Dry fiber preform placed in mold (or on tool)
   Peel ply → distribution mesh → vacuum bag (sealed)
   Vacuum port + resin inlet

   PROCESS:
   ─────────
   1. Pull vacuum on dry preform (check for leaks)
   2. Open resin inlet → resin drawn in by vacuum pressure differential
   3. Flow front progresses through preform (infusion time: 30 min–8 hours)
   4. Close inlet when fiber fully wetted
   5. Cure at ambient or elevated temperature

   TYPICAL PROPERTIES:
   ────────────────────
   Vf: 45–55%  (gravity drainage + vacuum consolidation)
   Void content: 1–3%

   MATERIALS: epoxy or vinyl ester (low viscosity <500 mPa·s needed)
   PART SIZE: unlimited in principle (largest: wind blade > 100 m)
   COST: moderate tooling, low equipment capital

   APPLICATIONS:
   ──────────────
   Wind turbine blades: >80% of all blades by VARTM/VIP process
   Large boat hulls (racing yacht hulls, workboats)
   Marine and infrastructure panels
   Aerospace secondary structures (cost-constrained)
```

### Flow Modeling for Infusion

Darcy's Law governs resin flow through fiber preform:

```
   v = (K/η) · ∇P

   v = flow velocity (m/s)
   K = permeability of fiber preform (m²) — measured property, ~10⁻¹¹–10⁻¹² m²
   η = resin viscosity (Pa·s) — critical: must stay < 500 mPa·s during fill
   ∇P = pressure gradient (Pa/m)

   Fill time approximation for flow distance L:
   t_fill ≈ L² · η / (2 · K · ΔP)

   Large wind blade (25 m infusion distance):
   At ΔP = 90 kPa (vacuum), K = 5×10⁻¹² m², η = 300 mPa·s
   t ≈ 25² × 0.3 / (2 × 5×10⁻¹² × 90,000) = ~200 hours (too long!)
   → Use distribution media (much higher K, 10⁻⁸ m²) for fast surface spread
   → Spiral inlet lines for large parts
```

---

## Prepreg Manufacturing and Handling

### What Is a Prepreg?

Fiber reinforcement pre-impregnated with partially-cured (B-staged) resin matrix.

```
   PREPREG STRUCTURE:
   ───────────────────
   Fiber: UD tape, fabric, or NCF
   Resin: epoxy at B-stage (partially cured, tack-y at room T)
   Backing paper: peel away before layup
   Areal fiber weight (AFW): 75–600 gsm
   Resin content: 30–42% (by weight)

   B-STAGE CHEMISTRY:
   ───────────────────
   Epoxy partially cured with DICY (dicyandiamide) — latent hardener
   At RT (< 25°C): effectively no cure progression for months
   Above 120°C: DICY activates → cure begins
   Above 160°C: fast cure → used for actual cure cycle
   → Shelf life at -18°C: 12–18 months
   → Out-life at 23°C: typically 3–30 days (before tack lost)
```

### Prepreg Manufacturing Process

```
   HOT MELT PREPREGGING (dominant method):
   ─────────────────────────────────────────
   1. Resin film cast onto release paper from hot melt
   2. Fiber collimated (UD tape) or from fabric
   3. Sandwich: paper/resin film + fiber + resin film/paper
   4. Heated calendar rolls: resin melts → impregnates fiber
   5. Cool → B-stage solidified → roll up with backing paper
   6. Cold storage at -18°C

   SOLUTION PREPREGGING (less common today):
   ───────────────────────────────────────────
   Resin dissolved in solvent → fiber drawn through bath → solvent removed
   Issues: residual solvent → voids in cure
   Used: low-viscosity systems, fabric prepreg for phenolic
```

---

## Autoclave Processing

The aerospace quality standard for thermoset composites.

### Autoclave Mechanism

```
   AUTOCLAVE:
   ──────────
   Pressure vessel + internal heating + vacuum bag provisions
   Gas: N2 (non-reactive, better safety than air for organics)
   Pressure: 0.35–0.70 MPa (50–100 psi) typically
   Temperature: 120°C (low-temp cure) or 180°C (standard aerospace)

   CURE CYCLE (standard 180°C epoxy):
   ────────────────────────────────────
   1. Room temperature: lay up plies on tool, apply vacuum bag
   2. Apply vacuum (100 mbar) — remove trapped air and volatiles
   3. Ramp to 110–120°C at 1–3°C/min
   4. Hold at 110°C: resin melts, flows, reduces viscosity
      Apply autoclave pressure (0.35–0.70 MPa) → compact plies
   5. Ramp to 180°C
   6. Hold at 180°C for 90–120 min (cure)
   7. Cool at 3–5°C/min under pressure
   8. Depressurize at < 60°C → demold

   WHY PRESSURE MATTERS:
   ──────────────────────
   External pressure + vacuum:
   → Compresses bag → consolidates plies → removes entrapped air
   → Maintains pressure on resin as it gels → forces out voids
   → Net driving force for void suppression:
     P_autoclave > P_vapor_water → water stays dissolved, not bubbles
```

### Vacuum Bag Assembly

```
   TOOL (aluminum, Invar, composite)
      │
      │ Release agent + peel ply
      │
   LAMINATE (prepreg plies stacked)
      │
      │ Peel ply
      │ Breather cloth (absorbs excess resin + allows vacuum flow)
      │ Vacuum bag film (Nylon 6 or 66 — resistant to epoxy)
      │ Sealing tape around perimeter
      │ Vacuum connector
      ▼
   TOOL surface (sealed bag)

   MONITORING:
   ────────────
   Thermocouples on tool and on top of laminate
   Vacuum gauge
   Dielectric cure monitoring (optional — tracks resin cure state)
```

### Tooling Materials

```
   ALUMINUM TOOLING:
   ──────────────────
   CTE: 23×10⁻⁶/°C (vs. CF/epoxy ≈ 2×10⁻⁶)
   CTE mismatch: large — thermal stresses on cure, dimensional issues
   Low cost, easy to machine
   Limited to ~500 cure cycles
   Use: low-volume, prototype, secondary structure

   INVAR 36 (Fe-Ni alloy):
   ────────────────────────
   CTE: 1.5×10⁻⁶/°C (nearly matches CF/epoxy)
   Heavy (~8,000 kg/m³ — heavy tools!)
   Very long tool life (>10,000 cycles)
   High cost to machine
   Use: high-precision large structure (aircraft skins, nacelles)

   COMPOSITE TOOL (CFRP):
   ───────────────────────
   CTE matched to composite part
   Lightweight
   Made from the same prepreg process (recursive!)
   Requires master (pattern) tool to make
   Use: large aircraft panels, wind blade molds
```

---

## Resin Transfer Molding (RTM)

Closed mold process: inject resin into closed mold containing dry fiber preform.

```
   RTM PROCESS:
   ─────────────
   1. Dry fiber preform cut + placed in closed mold (matched male/female)
   2. Mold closed, clamped (0.5–1.0 MPa clamp force)
   3. Resin injected under pressure (0.1–1.0 MPa injection) at 60–120°C
   4. Resin flows through preform, exits at vents (when resin appears = full)
   5. Cure in mold at 120–180°C
   6. Demold → post-cure

   Vf: 50–60%  Void: 1–3%  Cycle: 30–120 min

   ADVANTAGES:
   ────────────
   Both surfaces smooth (closed mold)
   Good dimensional control
   Moderate cost vs. autoclave (no pressure vessel, faster cycles)

   HIGH-PRESSURE RTM (HP-RTM, ULTRA-RTM):
   ────────────────────────────────────────
   Injection at 1–10 MPa, 80–150°C
   Cycle time: 3–15 min (fast epoxy or fast polyurethane)
   BMW i3, i8: HP-RTM for CFRP body panels
   Audi R8 spider: CFRP structural tub via HP-RTM
```

---

## Automated Fiber Placement (AFP) and ATL

AFP and Automated Tape Laying (ATL) are CNC machine methods for large structure layup.

```
   AFP (AUTOMATED FIBER PLACEMENT):
   ──────────────────────────────────
   Machine head: 8–32 slit-tape tows (3–12 mm wide)
   Applies prepreg tow-by-tow to tool surface
   Computer-controlled path planning
   Compaction roller + heat (laser or hot gas)
   → In-situ consolidation (for thermoplastic) or B-stage cure

   CAPABILITY:
   ────────────
   Curved surfaces (fuselage, nacelle)
   Complex contour following
   Variable-angle tow (VAT) — fiber direction follows design optimization
   Speed: up to 25 m/min effective deposition rate
   Layer thickness: 0.125–0.250 mm/pass

   ATL (AUTOMATED TAPE LAYING):
   ──────────────────────────────
   Wider tape (150–300 mm)
   Best for flat or gently curved surfaces (wing skin)
   Higher speed (50 m/min) for large panels
   Less suited to complex geometry than AFP

   USED FOR:
   ──────────
   Boeing 787: fuselage barrel sections (AFP on mandrel)
   Airbus A350: fuselage + wing lower skin (AFP/ATL)
   Wing spars, floor beams
   Wind blade spar caps (dry fiber AFP + infusion for large blades)
```

---

## Filament Winding

CNC-controlled winding of fiber roving (continuous tow) around rotating mandrel.

```
   PROCESS:
   ─────────
   Fiber passes through wet bath → wound onto rotating mandrel
   Winding angle: 5–90° (determined by mandrel rotation vs. carriage speed)
   Polar winding: ±15–30° (hoop-dominant)
   Helical: various angles
   Hoop: ±85–90° (pressure vessel circumferential)

   NETTING ANALYSIS — OPTIMAL ANGLE:
   ────────────────────────────────────
   Pressure vessel: biaxial load (σ_hoop = 2 × σ_axial)
   Optimal angle: θ = arctan(√2) = 54.7° (for equal biaxial from fiber alone)

   APPLICATIONS:
   ──────────────
   Pressure vessels (CNG / hydrogen storage for vehicles)
   Pipeline rehabilitation sleeves
   Drive shafts (automotive, helicopter)
   Launch vehicle casings (solid rocket motor)
   Tubes, bars, golf shafts

   Vf: 60–70%  (compaction by winding tension)
   Cost: low for rotationally symmetric shapes
   Limitation: concave shapes cannot be filament wound
```

---

## Pultrusion

Continuous profile production — the most cost-efficient composite process per unit length.

```
   PROCESS:
   ─────────
   Roving + mat → resin bath → die (heated) → pulling mechanism → cut to length
   Die: shaped steel (I, T, round, custom profile) at 120–180°C
   Pull speed: 0.5–5 m/min

   MATERIALS: E-glass + polyester or vinyl ester (most common)
              CF + epoxy (structural, more expensive)

   APPLICATIONS:
   ──────────────
   Window/door frames (GF/UPE — corrosion-free)
   Structural profiles (I-beams, channels for walkways, gratings)
   Utility poles, marine pilings
   Electrical cross-arm, ladder rails
   Bridge deck components

   Vf: 45–65%  Void: 1–3%  Cost: very low per meter for simple profile
   Limitation: constant cross-section only
```

---

## Decision Cheat Sheet

| Application | Process | Vf | Cost |
|-------------|---------|----|----|
| Aerospace primary structure | Prepreg + autoclave | 60% | Very high |
| Aerospace secondary | RTM or prepreg OOA | 55% | High |
| Wind turbine blade | Infusion (VARTM) | 50% | Medium |
| Automotive CFRP structural | HP-RTM or press | 55% | Medium-high |
| Marine hull (large) | Hand lay-up or infusion | 35–50% | Low-medium |
| Pressure vessel / pipe | Filament winding | 65% | Low |
| Structural profile (long) | Pultrusion | 55% | Very low |
| Complex fuselage/wing | AFP + autoclave | 60% | Very high |

---

## Common Confusion Points

**Out-of-autoclave (OOA) prepreg ≠ lower quality**: OOA prepregs designed for
vacuum-only consolidation (e.g., Cytec CYCOM 5320-1) achieve void contents
< 1% by relying on specially formulated resin that doesn't require external
pressure for void suppression. Properties are close to autoclave cure, at
much lower tooling cost. Boeing Dreamliner tooling shops use OOA.

**AFP head compaction roller ≠ consolidation**: In thermoset AFP, the compaction
roller keeps the tow in place and reduces wrinkles. It does not fully consolidate
the laminate — final consolidation still requires autoclave or OOA cure cycle.
For in-situ consolidation, thermoplastic AFP with laser heating achieves full
consolidation at the laydown head (no separate cure needed).

**Filament winding fiber cannot turn convex corners**: Winding can only apply
fiber on convex surfaces (where fiber stays in contact with mandrel). Concave
areas (closed ends, features with negative draft) require different approaches:
pre-wound piece or cutdown. This is why pressure vessels are always cylindrical
with dome ends — filament winding constraint, not just geometry convenience.
