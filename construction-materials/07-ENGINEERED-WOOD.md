# Construction Materials — Engineered Wood

## The Big Picture: Solid Timber → Engineered Wood Products

```
SOLID TIMBER vs ENGINEERED WOOD PRODUCTS
┌──────────────────────────────────────────────────────────────────────────────┐
│                                                                              │
│  SOLID SAWN TIMBER     STRUCTURAL ISSUES           ENGINEERED SOLUTION       │
│  ─────────────────────────────────────────────────────────────────────────   │
│  Knots, splits          Random defects → weak spots  LVL: parallel lam;      │
│                                                       averages out defects   │
│                                                                              │
│  Short lengths          Forests grow limited lengths  Finger-joint → any L   │
│  (max ~6–8m usable)                                  Glulam: laminated       │
│                                                                              │
│  Limited section size   Large trees scarce; slow grow Glulam: assemble from  │
│                                                       small boards           │
│                                                                              │
│  Anisotropic (one        Weak perpendicular to grain  PLY: 90° rotation      │
│  direction)              limits sheet applications    CLT: orthogonal lam    │
│                                                                              │
│  Dimensional instability Moisture → swell/shrink      CLT/LVL: reduced EMC   │
│                                                        swings; stable        │
│                                                                              │
│  Variable quality        Natural variability          E-rated, MSR graded    │
│                          → design conservatively      → consistent values    │
│                                                                              │
│  PRODUCT FAMILY:                                                             │
│  ┌─────────┬────────────┬──────────────┬─────────────┬─────────────────┐   │
│  │Plywood  │  LVL       │  Glulam      │   CLT       │ Mass timber     │   │
│  │(sheets) │ (beams)    │ (beams/cols) │ (panels)    │ (buildings)     │   │
│  │Cross-lam│ Parallel   │ Parallel     │ Cross-lam   │ CLT+glulam+LVL  │   │
│  │veneers  │ veneers    │ lamellas     │ lamellas    │ hybrid systems  │   │
│  └─────────┴────────────┴──────────────┴─────────────┴─────────────────┘   │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Timber Properties: The Grain Direction Problem

```
TIMBER ANISOTROPY: STRENGTH VARIES WITH GRAIN DIRECTION
──────────────────────────────────────────────────────────────────────────────
  Softwood (typical Sitka spruce, C24 structural grade):

  DIRECTION        COMPRESSION   TENSION      SHEAR      MODULUS
  ────────────────────────────────────────────────────────────────────────
  Parallel (//)    21 MPa        14 MPa        2.5 MPa   11,000 MPa (E₀)
  to grain                                               670 MPa (E₀,mean)
  Perpendicular(⊥) 2.5 MPa       0.4 MPa       —        370 MPa (E₉₀)
  to grain

  RATIO:  E₀ / E₉₀ = 11,000 / 370 = ~30:1  (30× stiffer along grain)
          Compressive // / ⊥ = 21 / 2.5 = ~8:1
          Tensile // / ⊥ = 14 / 0.4 = ~35:1

  PRACTICAL CONSEQUENCES:
  1. Beams must span parallel to grain (always true for sawn lumber)
  2. Perpendicular-to-grain tension → splitting → avoid in connections
     → use screws at angle to grain; self-tapping reinforcement screws
  3. Cross-grain bending (load ⊥ to grain over span //) → catastrophic split
     → this is why I-joists and LVL have consistent grain direction

  VARIABILITY:
  Solid sawn timber: characteristic strength based on 5th percentile of test data
  → C16, C24, C30: "C" = characteristic bending strength (MPa)
  → C24: f_m,k = 24 MPa bending; f_t,0,k = 14 MPa tension
  Large natural variability (σ ~ 30–40% COV for strength) → design conservatively

  MOISTURE CONTENT CORRECTION:
  Timber properties worsen in wet conditions (service class 2: up to 20% MC)
  EN 1995 (Eurocode 5): k_mod = modification factor
    Permanent load, SC2: k_mod = 0.7 (30% strength reduction vs. dry)
    Short duration, SC1: k_mod = 1.1
  Also: creep factor k_def = 0.8 (SC2) for deflection calculations
```

---

## Plywood

Plywood is the simplest biaxial engineered wood panel — alternating veneer layers
with grain rotated 90° between plies.

```
PLYWOOD CONSTRUCTION
┌──────────────────────────────────────────────────────────────────────────────┐
│                                                                              │
│  3-PLY CONSTRUCTION (simplest):                                              │
│  ──────────────────────────────                                              │
│  Face veneer:   grain → → → → → → (along panel length direction)           │
│  Core veneer:   grain ↑↑↑↑↑↑↑↑↑↑ (across; 90° to face)                     │
│  Back veneer:   grain → → → → → → (same as face; panel balanced)             │
│                                                                              │
│  ALWAYS ODD NUMBER OF PLIES:                                                 │
│  3, 5, 7, 9 plies → always symmetric about mid-plane                         │
│  → no residual bending moment from moisture change → stays flat              │
│  Asymmetric panel (even plies): warps on drying/wetting                      │
│                                                                              │
│  EFFECT OF CROSS-LAMINATION:                                                 │
│  1. Dimensional stability: perpendicular plies restrain swelling/shrinkage   │
│     Net in-plane movement: ~0.02% per 1% MC change vs ~0.3% for solid wood   │
│  2. Biaxial stiffness: load sharing in both directions                       │
│     (though face grain direction is still stiffer)                           │
│  3. Splits blocked: crack along grain in one ply stopped by next ply       │
│                                                                              │
│  STANDARD SIZES:                                                             │
│  2440 × 1220 mm (8 × 4 ft) — universally dominant                          │
│  1250 × 2500 mm (metric equivalent)                                          │
│  Thicknesses: 3, 4, 6, 9, 12, 15, 18, 25, 32 mm                           │
│                                                                              │
│  GRADES (face/back):                                                         │
│  A-A: both faces clear; furniture; expensive                                 │
│  B-C: one good face; one filled face; typical construction                   │
│  C-D (CDX): unsanded; exterior; sheathing → structural use                   │
│  Structural (EN 636): F grades; specified by bending strength                │
│                                                                              │
│  BONDING:                                                                    │
│  Interior (E0/E1): UF (urea formaldehyde); for dry conditions only           │
│  Exterior (WBP): PF (phenol formaldehyde); fully waterproof; boil-proof      │
│  EN 314 bond quality: Class 3 (exterior) required for structural             │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## LVL (Laminated Veneer Lumber)

LVL: all veneers with grain PARALLEL (same direction). Not cross-laminated like plywood.

```
LVL vs PLYWOOD: KEY DISTINCTION
──────────────────────────────────────────────────────────────────────────────
  Plywood: alternating 90° grain → biaxial panel (dimensional stability)
  LVL:     all parallel grain → optimized for one-direction beam action

  LVL PRODUCTION:
  1. Peel logs → continuous veneer ribbon (2–4 mm thick)
  2. Dry to MC ~ 5–8%
  3. Scarfed (overlapping) joints between ribbon lengths → continuous strand
  4. Stack with phenol-resorcinol-formaldehyde (PRF) adhesive between plies
  5. Hot press at 130–150°C → bonded billet
  6. Cut to required section (45–90 mm wide; 200–600 mm deep; lengths to 20+ m)

  PROPERTIES vs SOLID TIMBER:
    Defects (knots, splits) distributed randomly across many thin veneers
    → no single defect occupies full section width
    → characteristic strength higher than solid: f_m,k ~ 30–48 MPa
    → variability lower: COV ~10% vs ~30% for sawn timber

  SECTIONS AVAILABLE:
    Beams/headers: 45–90 mm wide × 200–600 mm deep × up to 20 m long
    Columns: laminated up to 200×200 mm
    Rim boards: 45 mm thick × full floor depth; stiff rim joist
    Scaffold planks: long lengths, consistent properties

  APPLICATIONS:
    Long-span floor beams (replace rolled steel WF for some spans)
    Ridge beams, headers over wide openings
    Combined with steel: LVL flanges on steel web → hybrid "flitch beam"
    Stair stringers, structural headers
```

---

## Glulam (Glued-Laminated Timber)

Glulam assembles small-section sawn lamellas (laminations) with structural adhesive
into large sections with any depth or length.

```
GLULAM PRODUCTION AND GEOMETRY
┌──────────────────────────────────────────────────────────────────────────────┐
│                                                                              │
│  LAMELLA: 35–45 mm thick sawn boards, typically 90–185 mm wide               │
│                                                                              │
│  END-JOINING: finger joints between board lengths                            │
│  ┌─────────────────────────────────────────────────────────────────────┐     │
│  │ board 1 ──────────╱╲╱╲╱╲───── board 2 continuing                   │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│  Finger profile: length 20–45mm; pitch 4–10mm; tip 0.5–2mm                 │
│  Adhesive: PRF (phenol-resorcinol), EPI (emulsion polymer isocyanate),     │
│    or MUF (melamine-urea-formaldehyde)                                       │
│  Glued under pressure (finger joint machine) → adequate bending strength   │
│                                                                              │
│  LAYER ASSEMBLY (grade combination for glulam):                             │
│  ─────────────────────────────────────────────                               │
│  Top (comp) outer:    T1 grade: lower quality OK (in compression)           │
│  Top (comp) inner:    T2 grade: intermediate                                 │
│  Web lamellas:        T2 grade: moderate                                    │
│  Bottom (tens) inner: T2 grade                                               │
│  Bottom (tens) outer: T1 grade: high quality (in tension — critical)        │
│  ─────────────────────────────────────────────                               │
│  → "combination" layup: strongest grade at highest-stress tension face     │
│  → "homogeneous" layup: all same grade; used for elements with varying M   │
│                                                                              │
│  CAMBER: beams may be pre-cambered (upward bow) to offset dead load sag    │
│    Typical camber: L/200 to L/300 upward for long beams                     │
│    Achieved during pressing: stack on curved form → adhesive cures to shape │
│                                                                              │
│  ADHESIVES (EN 301 compliance):                                              │
│    PRF (phenol-resorcinol-formaldehyde): traditional; dark glueline; durable│
│      → outdoor; exposed; EN 301 type I (fully waterproof)                  │
│    MUF (melamine-urea-formaldehyde): lighter glueline colour; indoor use   │
│      → EN 301 type II (high humidity; not continuous wet)                   │
│    EPI (emulsion polymer isocyanate): formaldehyde-free; newer; versatile  │
│      → indoor; gaining market share for low-VOC specifications              │
│    PRF dominates structural outdoor glulam; EPI growing for interior mass timber│
│                                                                              │
│  GLULAM GRADES (EN 14080):                                                   │
│    GL24h, GL28h, GL32h: homogeneous (h) layup; number = bending f_m,k      │
│    GL24c, GL28c, GL32c, GL36c: combination (c) layup                        │
│    → GL36c: f_m,k = 36 MPa; E₀,mean = 14,700 MPa; ρ_k = 430 kg/m³        │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## CLT (Cross-Laminated Timber)

CLT is the structural panel product enabling mass timber construction.
Think: plywood at architectural scale.

```
CLT CONSTRUCTION
┌──────────────────────────────────────────────────────────────────────────────┐
│                                                                              │
│  5-PLY CLT (common floor panel):                                             │
│                                                                              │
│  Layer 1 (top/outer):  → → → → → →  major direction (span direction)       │
│  Layer 2:              ↑↑↑↑↑↑↑↑↑↑  minor direction (90°)                   │
│  Layer 3 (core):       → → → → → →  major direction                          │
│  Layer 4:              ↑↑↑↑↑↑↑↑↑↑  minor direction                         │
│  Layer 5 (bottom/outer): → → → → →  major direction                          │
│                                                                              │
│  PANEL SIZES:                                                                │
│    Width: up to 3.0 m (limited by press width)                               │
│    Length: up to 20 m (limited by transport)                                 │
│    Thickness: 60mm (3-ply) to 400mm+ (7+ ply)                              │
│    Common floor panels: 140–200 mm (5-ply); wall panels: 100–200 mm        │
│                                                                              │
│  TWO-WAY PLATE ACTION:                                                       │
│    Unlike I-beams or one-way slabs, CLT panel distributes load in 2D         │
│    Orthotropic elastic plate: D₁₁ ≠ D₂₂  (different stiffness per direction)│
│    D₁₁ (major): governed by layers 1,3,5 (strong direction)                │
│    D₂₂ (minor): governed by layers 2,4  (weaker direction)                   │
│    Torsional stiffness D₁₂: provided by cross layers                       │
│    → stiffness matrix Dij used in FEM plate analysis                         │
│    → for panel-level design: simplified Kxyz method or Gamma method        │
│                                                                              │
│  ROLLING SHEAR:                                                              │
│    Shear in the transverse layers (layers 2, 4) → rolling shear failure      │
│    Rolling shear: shear parallel to glue face in cross layer                 │
│    f_r,k = 1.0–1.5 MPa (very low; governs in thick panels with short spans)│
│    → critical detail: CLT-to-CLT connection; spline joint; notched beam      │
│    → avoid large concentrated loads without stiffener or reinforcement       │
│                                                                              │
│  CONNECTIONS (structural critical path):                                     │
│    Self-tapping screws (STS): fully threaded; draw panels together;        │
│      can be inclined (45°) → resist axial + shear in 3D                    │
│      capacity: ~12–25 kN/screw depending on diameter (8–14mm) and angle    │
│    Angle brackets: steel; screwed to CLT; bolted/nailed to steel support   │
│    LVL spline: LVL strip glued/screwed into routed groove → panel-to-panel │
│    Hold-down anchors (HDA): tension resist; for uplift and racking walls   │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

### CLT Span Tables (Indicative)

| CLT Panel | Application | Span (m) | Load (kPa) | Notes |
|---|---|---|---|---|
| 3-ply, 60 mm | Internal wall | — | — | Non-structural partition |
| 5-ply, 140 mm | Floor slab | 5.0–6.0 | 3.0 | Simple span; 28-day shrinkage |
| 5-ply, 160 mm | Floor slab | 6.0–7.5 | 3.0 | Residential/office |
| 5-ply, 200 mm | Floor slab | 7.0–9.0 | 5.0 | Higher load; check vibration |
| 7-ply, 260 mm | Long span floor | 9.0–11.0 | 3.5 | Vibration governs above ~8m |
| 3-ply, 80 mm | Roof panel | 4.0–5.5 | 1.5 | Snow + access |
| 5-ply, 160 mm | Shear wall | — | — | Racking resistance per m run |

**Vibration governs.** Above ~7 m spans in CLT floor panels, vibration (human comfort,
1-Hz walking excitation) often controls design ahead of deflection or strength.
EN 1995-1-1 vibration check: unit point load deflection + fundamental frequency.
Typical requirement: w(1kN) ≤ 0.5–1.5 mm and f₁ ≥ 8 Hz.

---

## Mass Timber: Buildings at Scale

```
TALL TIMBER BUILDINGS: CASE STUDIES
┌──────────────────────────────────────────────────────────────────────────────┐
│                                                                              │
│  BROCK COMMONS TALLWOOD HOUSE (Vancouver, 2017)                              │
│  18 stories; 53 m tall                                                       │
│  Structural system:                                                          │
│    CLT floor panels: 5-ply 169 mm span ~8.2 m between columns              │
│    Glulam columns: continuous vertical post-and-beam                         │
│    RC cores × 2: lateral stability (seismic + wind)                          │
│    RC ground floor: transfer slab + podium (fire access)                   │
│    Hybrid: CLT + glulam structure; concrete lateral system                   │
│  CLT prefabricated with pre-drilled connection holes → fast erection         │
│  One floor per day at peak rate                                              │
│  CO₂ stored in CLT structure: ~1,628 tCO₂ sequestered                      │
│                                                                              │
│  ASCENT (Milwaukee, 2022)                                                    │
│  25 stories; 86.6 m — currently tallest mass timber building in world        │
│  CLT + glulam + RC core hybrid                                               │
│                                                                              │
│  TYPICAL MASS TIMBER STRUCTURAL SCHEME:                                      │
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────┐             │
│  │                     CLT floor plate                          │            │
│  │ (diaphragm + floor spanning between glulam beams)           │            │
│  │ ──────┬──────────────────────┬─────────────────── floor     │            │
│  │       │ glulam beam          │                              │            │
│  │  GLB  │ spans column-column  │  GLB                         │            │
│  │       │                      │                              │            │
│  │ col   col                  col   col  ← glulam posts        │            │
│  │       │                      │                              │            │
│  │  ─────┼──────────────────────┼─────  floor below            │            │
│  │       │                      │                              │            │
│  │    [RC core] ← lateral resist.                              │            │
│  └─────────────────────────────────────────────────────────────┘            │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Fire Performance of Mass Timber

```
TIMBER CHARRING AND FIRE RESISTANCE
┌──────────────────────────────────────────────────────────────────────────────┐
│                                                                              │
│  CHARRING PROCESS:                                                           │
│  At ~270–300°C: wood surface begins pyrolysis → char layer forms             │
│  Char rate (β₀): ~0.65 mm/min for glulam/CLT softwood (EN 1995-1-2)        │
│  Hardwood: ~0.5 mm/min (slower → better fire resistance per mm)            │
│                                                                              │
│  RESIDUAL SECTION UNDER FIRE:                                                │
│  After t minutes of fire:                                                    │
│    Char depth: d_char = β₀ × t + k₀ × (depth of zero-strength layer, 7mm) │
│    Residual section: original section − d_char on all exposed faces        │
│                                                                              │
│  EXAMPLE: 120 × 120 mm glulam post, 4-sides exposed, 60-min fire           │
│    Char per side: 0.65 × 60 + 7 = 46 mm                                    │
│    Residual section: 120 − 2×46 = 28 mm on each axis                      │
│    → too small; would fail → must be 160 × 160 mm minimum for REI60        │
│                                                                              │
│  MASS TIMBER FIRE COMPARISON vs STEEL:                                       │
│                                                                              │
│  ┌────────────────────────────────────────────────────────────────────┐      │
│  │              STEEL                    MASS TIMBER (CLT/Glulam)     │     │
│  │  Behaviour:  Non-combustible          Combustible + chars           │     │
│  │  Fire behav: Softens above 500°C     Chars predictably             │     │
│  │  Failure:    Rapid (15 min exposed)  Gradual (char insulates core)  │     │
│  │  Warning:    Progressive sag         Progressive (visible char)    │     │
│  │  Protection: Intumescent/board       None needed for sized section  │     │
│  │  After fire: Deformed steel          Char removed; often reusable   │     │
│  └────────────────────────────────────────────────────────────────────┘     │
│                                                                              │
│  CRITICAL POINT: Mass timber has PREDICTABLE fire resistance tied to        │
│  physical residual section. Steel has unpredictable rapid failure above     │
│  550°C without cladding. For same REI60 performance:                        │
│  → Steel: requires intumescent paint or boarding (adds cost + time)        │
│  → CLT/glulam: add 40–50 mm char allowance to design section (adds volume)│
│                                                                              │
│  EXPOSED VS ENCAPSULATED:                                                    │
│    Exposed CLT: char depth must be added to required structural section     │
│    Encapsulated (plasterboard): board protects from fire; smaller section  │
│    Many mass timber buildings expose structure as design feature             │
│    → "engineered exposure": calculate char; size accordingly; no board     │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Adhesives in Engineered Wood: Chemistry and Classes

```
STRUCTURAL ADHESIVE COMPARISON
──────────────────────────────────────────────────────────────────────────────
  ADHESIVE    CHEMISTRY          PROPERTIES              USE CASES
  ────────────────────────────────────────────────────────────────────────────
  PRF         Phenol-resorcinol  Type I (fully waterproof) Glulam, LVL outdoor
              formaldehyde       Dark glueline (red/brown)  Marine, exposed
                                 High strength; rigid       EN 301 Type I
                                 Formaldehyde emissions     Still dominant outdoor

  MUF         Melamine-urea      Type I/II                  Indoor glulam
              formaldehyde       Light-coloured glueline    Furniture
                                 Lower formaldehyde         CLT lamellas
                                 than UF alone              Good workability

  EPI         Emulsion polymer   Formaldehyde-free!         Growing market
              isocyanate         Type I: outdoor; fully WP  CLT; LVL; Glulam
                                 Light coloured glueline    Low-VOC specs
                                 Excellent gap-fill         Fire performance OK
                                 Moisture-tolerant press

  UF          Urea formaldehyde  Interior only              Particleboard
                                 Not durable in moisture    MDF; interior ply
                                 High formaldehyde (E2/E1)  Non-structural

  PUR         1-component PUR    Moisture-curing            Finger joints
                                 High viscosity; gap-fill    Site repairs
                                 Good long-term outdoor     Not for glulam lams.

  EPOXY       2-part epoxy       Structural repair          Crack injection
                                 High strength; rigid       Rod installation
                                 Excellent to concrete      Mixed substrates
```

---

## Glulam, LVL, CLT Span Comparison

```
INDICATIVE SPAN RANGES (commercial/institutional loading ~3–5 kPa)
──────────────────────────────────────────────────────────────────────────────
  ELEMENT TYPE           SPAN RANGE     DEPTH              NOTES
  ─────────────────────────────────────────────────────────────────────────
  Sawn timber floor joist 3–5 m         150–250 mm         SC1 only
  LVL floor beam          5–12 m         250–600 mm         Replaces steel WF
  Glulam beam (simple)    8–25 m         450–1,200 mm       Mid-rise; long-span
  Glulam beam (tied arch) 20–60 m        arch rise varies   Stadiums, arenas
  CLT floor panel (5-ply) 4–9 m          140–200 mm         Vibration check >7m
  CLT roof panel (3-ply)  4–7 m          80–160 mm          Snow + live load
  Glulam portal frame     10–30 m (span) 600–1500 mm deep   Agricultural, sports
  CLT shear wall          —              3–5 m tall panels  Racking design per EC5

  RULE OF THUMB: Glulam beam depth ≈ span/15 to span/20 (deflection-governed)
  LVL beam depth ≈ span/16 to span/22
  Compare: steel W-beam depth ≈ span/18 to span/25 (similar order of magnitude)
  BUT steel density 16× timber → timber beam weighs much less per unit volume
```

---

## Decision Cheat Sheet

| Question | Answer |
|---|---|
| LVL vs glulam — which for beam? | LVL: consistent, shallower depth options, off-the-shelf. Glulam: curved forms, larger sections, exposed appearance. |
| CLT vs RC flat slab — trade-offs? | CLT: faster erection, lower carbon, lighter. RC: better thermal mass, acoustic, no moisture sensitivity. |
| CLT floor vibration — when does it govern? | Above ~6–7 m span in residential. Check f₁ ≥ 8 Hz and unit point load deflection ≤ 0.5 mm |
| Best adhesive for outdoor glulam? | PRF (phenol-resorcinol formaldehyde) — EN 301 Type I, fully waterproof |
| Mass timber + RC core hybrid — why? | CLT/glulam efficient for gravity; RC core reliable for lateral (seismic, wind); complies with codes more easily |
| Fire: exposed CLT beam, REI60 required? | Add char allowance: 0.65 mm/min × 60 min + 7 mm = ~46 mm per exposed face to structural section |
| CLT connection at panel edge to panel edge? | LVL spline in groove; or self-tapping screws (inclined or surface-mounted); or half-lapped joint |
| Plywood exterior — which bond class? | Bond class 3 (exterior, boil-proof): phenol formaldehyde (PF) adhesive (WBP) |
| Glulam cambering — what for and how much? | To offset dead load deflection; typically L/200 to L/300 pre-camber; pressed in curved form |

---

## Common Confusion Points

**CLT rolling shear is a critical failure mode often overlooked.** In the cross layers
(layers 2, 4 in a 5-ply), the shear plane is parallel to the glue line and perpendicular
to the grain. This "rolling shear" strength (f_r,k ~1.0–1.5 MPa) is far lower than
the longitudinal shear strength (~3.5 MPa). At concentrated loads or connections,
rolling shear can govern design when beam shear would not.

**Glulam beam grain is always parallel to the beam axis.** Unlike plywood, glulam is
not cross-laminated. All lamellas are parallel. The cross-lamination in CLT is what
distinguishes it from glulam. Glulam is essentially a large sawn timber, but with
defects averaged across many laminations and unlimited in length and depth.

**Mass timber buildings still need lateral systems.** CLT panels can act as shear
walls (racking resistance from connections) but most mass timber buildings taller
than 4–5 stories use RC or steel cores for lateral stability. The mass timber handles
gravity loads (floors, beams, columns); the stiff RC core handles wind and seismic.
This hybrid is how Brock Commons and most commercial mass timber towers work.

**Char layer is NOT a charred piece of wood — it is a sacrificial zone.**
The char itself has near-zero mechanical strength. What the char DOES is insulate
the inner wood at lower temperature, slowing further pyrolysis. The design assumption
is that wood behind the char front is at ambient strength. Remove the char post-fire
and the residual section may be structurally adequate — this is why post-fire mass
timber buildings are sometimes repaired rather than demolished.

**E (Young's modulus) in CLT is not a single number.** CLT is an orthotropic plate.
The effective bending stiffness in the span direction (EI_eff,1) and perpendicular
(EI_eff,2) differ significantly. The Gamma method (EN 1995-1-1, Annex B) or the
k-method accounts for the shear deformation in the cross layers. For a 5-ply CLT
panel, the effective EI in the strong direction is ~70–80% of what you'd calculate
ignoring the cross layer compliance.
