# Wood Properties: Grain, Density, Hardness, Shrinkage, Moisture

## The Big Picture

Wood is an orthotropic material — three independent axes, three different stiffness/strength/shrinkage values in each direction. Every property that matters practically (how a plank moves, how strong a beam is, how it machines) flows from this fundamental anisotropy.

```
WOOD ANISOTROPY — THREE PRINCIPAL AXES

             L (Longitudinal)
             ^
             |      Along fiber axis
             |      Strongest; least shrinkage
             |
             +-----------> T (Tangential)
            /               Tangent to growth rings
           /                Most shrinkage; flatsawn face
          v
       R (Radial)
       Pith to bark
       Intermediate shrinkage
       Quartersawn face

  PROPERTY ORDERING:
  Strength:   EL >> ER >= ET       (EL ~ 10–15× ET)
  Shrinkage:  ΔL << ΔR < ΔT        (ΔT ~ 1.5–2× ΔR; ΔL ~ 0.1–0.3%)
  Permeability: varies; often L >> T > R
```

---

## Section 1 — Grain and Figure

"Grain" and "figure" are distinct concepts that are frequently conflated.

### Grain Direction

Grain = the orientation of wood fibers relative to the long axis of the piece.

```
  STRAIGHT GRAIN:    fibers parallel to piece axis
                     --> maximum strength, easiest to split/plane
                     --> most structural lumber

  CROSS GRAIN:       fibers deviate from axis
                     --> strength reduced; splits unpredictably
                     --> caused by spiral growth, interlocked grain, or sawing angle

  SPIRAL GRAIN:      fibers wind helically around trunk
                     --> common in young-growth conifers
                     --> causes boards to twist as they dry

  INTERLOCKED GRAIN: alternate layers spiral left and right
                     --> tropical hardwoods (sapele, iroko)
                     --> high shear strength; resists splitting; difficult to plane

  WAVY GRAIN:        fibers undulate regularly
                     --> produces "fiddleback" or "curly" figure
                     --> valued aesthetically; weakens along grain

  GRAIN ANGLE RULE:  1-in-12 slope = ~90% of straight-grain strength
                     1-in-8 slope = ~75%; 1-in-4 slope = ~50%
```

### Figure

Figure = the visual pattern on the sawn surface. Determined by:
- Ray size and orientation (quartersawn oak ray fleck)
- Growth ring width variation (bird's-eye, quilted)
- Local grain deviation (curly, burl, crotch)
- Resin/extractive patterns (spalting — fungal staining)

```
SAWING ORIENTATION AFFECTS FIGURE:

  LOG CROSS-SECTION:
  +---------------------------+
  |          ))))             |  Growth rings
  |        )(   )(            |
  |       )(     )(           |
  |        )(   )(            |
  |          ))))             |
  +---------------------------+

  FLATSAWN (plain sawn):       QUARTERSAWN:
  Board face ≈ tangential       Board face ≈ radial
  Cathedral arch grain pattern  Straight grain lines
  More figure variation         Ray fleck visible (oak)
  More movement with humidity   Less movement with humidity
  Cheaper to produce            More waste; more expensive
```

---

## Section 2 — Density

Wood density is the single best predictor of most mechanical properties.

### Measurement Standards

- **Specific gravity (SG)** or **relative density**: ratio of oven-dry wood mass to volume of water displaced (typically at 12% MC or green volume)
- **Air-dry density** (at 12% MC): most common commercial standard
- Units: kg/m³ or lb/ft³

### Density Range

```
DENSITY SPECTRUM (air-dry, 12% MC):

  Balsa (Ochroma)     ~170 kg/m³   (lightest commercial wood)
  Western red cedar   ~370 kg/m³
  Eastern white pine  ~400 kg/m³
  Douglas-fir         ~530 kg/m³
  White oak           ~770 kg/m³
  Hard maple          ~740 kg/m³
  Hickory (pecan)     ~850 kg/m³
  Lignum vitae        ~1230 kg/m³  (denser than water; sinks)
  Ironwood (Krugiod.) ~1300 kg/m³  (heaviest known)
  Water density       ~1000 kg/m³  (reference)
```

### Density Drivers

- **Latewood proportion**: High latewood = high density. Latewood cells have thick walls, small lumens — walls occupy more volume fraction.
- **Cell wall thickness**: Independent of cell size. Thick-walled fibers (e.g., tropical hardwood fibers) increase density.
- **Extractive content**: Heartwood extractives add mass. Teak heartwood is denser than sapwood by ~5–15%.
- **Microfibril angle (MFA)**: High MFA (juvenile wood, reaction wood) reduces stiffness; low MFA (mature wood) maximizes modulus.

---

## Section 3 — Janka Hardness

Janka hardness measures **surface hardness** — resistance to indentation — not overall strength.

**Method**: Force required to embed a steel ball (diameter 11.28 mm, area = 1 cm²) to half its diameter into the wood face perpendicular to grain.

Units: **lbf** (US) or **kN** (metric). Conversion: 1 kN = 224.8 lbf.

```
JANKA HARDNESS SCALE (side-grain, approximate):

  Balsa              ~100 lbf   (not structural)
  Eastern white pine ~380 lbf
  Douglas-fir        ~660 lbf
  Black cherry       ~950 lbf   (quality furniture threshold)
  Black walnut       ~1010 lbf
  Hard maple         ~1450 lbf  (flooring standard)
  White oak          ~1360 lbf
  Hickory (shagbark) ~1820 lbf  (tool handles)
  Brazilian cherry   ~2350 lbf  (tropical hardwood flooring)
  Ipe (Brazilian ww) ~3684 lbf  (decking, extreme durability)
  Australian buloke  ~5060 lbf  (hardest known commercial)
```

**End-grain hardness** is 2–4× higher than side-grain. Relevant for cutting boards, end-grain flooring blocks, wooden mallets.

---

## Section 4 — Moisture Content, EMC, and the Fiber Saturation Point

Wood is hygroscopic — its water content and consequently its dimensions respond continuously to ambient humidity.

### Moisture Content Definition

```
  MC% = (mass_wet - mass_oven_dry) / mass_oven_dry × 100

  Example: 125 g wet, 100 g dry
  MC = (125-100)/100 × 100 = 25%

  Green wood:  >30% MC (above FSP); wood just felled
  Air-dried:   12–19% MC (depending on climate)
  Kiln-dried:  6–12% MC (interior use standard)
  Oven-dry:    0% MC (theoretical; instantaneously reabsorbs moisture)
```

### Fiber Saturation Point (FSP)

FSP is the critical threshold: the moisture content at which cell walls are fully saturated with bound water but no free water remains in cell lumens.

```
  ABOVE FSP (~28–30% MC):                BELOW FSP:
  Cell lumens contain free water          Only bound water in cell walls
  No dimensional change with MC change    Shrinkage/swelling occurs
  Strength and stiffness relatively low   Strength and stiffness INCREASE
  Fungal decay possible above ~20% MC     Below ~19% = too dry for decay fungi

  KEY RULE: Shrinkage and swelling ONLY occur below FSP
```

### Equilibrium Moisture Content (EMC)

EMC is the moisture content wood reaches when in equilibrium with a given temperature and relative humidity. This is the target for specifying kiln-drying.

```
SELECTED EMC VALUES (approximate):

  RH 30%, 21°C --> EMC ~6.2%   (heated interior, winter, arid climate)
  RH 65%, 21°C --> EMC ~12.0%  (temperate, outdoor covered storage)
  RH 80%, 21°C --> EMC ~16.5%  (humid climate, poorly ventilated)
  RH 95%, 21°C --> EMC ~22.5%  (near-saturation; near FSP)

  PRACTICAL TARGETS:
  Interior furniture/flooring:  8–10% (heated N. American interior)
  Exterior millwork:           12–14%
  Concrete formwork:           15–20% (prevent excessive absorption)
```

---

## Section 5 — Shrinkage Coefficients and Wood Movement Math

Shrinkage values are reported as **percent shrinkage from green (FSP) to oven-dry**.

### Shrinkage Reference Table

| Species | Radial (R%) | Tangential (T%) | T/R Ratio | Classification |
|---------|-------------|-----------------|-----------|----------------|
| Eastern white pine | 2.1 | 6.1 | 2.9 | Low movement |
| Douglas-fir | 4.8 | 7.6 | 1.6 | Medium |
| Southern yellow pine | 5.4 | 7.7 | 1.4 | Medium |
| Hard maple | 4.8 | 9.9 | 2.1 | High movement |
| White oak | 5.6 | 10.5 | 1.9 | High |
| Red oak | 4.0 | 8.6 | 2.2 | High |
| Black walnut | 5.5 | 7.8 | 1.4 | Medium |
| Teak | 2.5 | 5.8 | 2.3 | Low-medium |
| Western red cedar | 2.4 | 5.0 | 2.1 | Low |
| Balsa | 3.0 | 7.6 | 2.5 | — |

### Shrinkage Calculation

To calculate expected movement between two moisture contents:

```
  FORMULA:
  ΔD = D_initial × (ΔMC / 30) × S_direction

  Where:
    ΔD       = dimensional change (same units as D_initial)
    D_initial = initial dimension
    ΔMC      = moisture content change (percentage points)
    30       = assumed FSP (%) — use species-specific FSP if known
    S        = total shrinkage coefficient for that direction (as decimal)

  EXAMPLE: 150 mm wide quartersawn white oak board
    drying from 18% to 8% MC (ΔMC = 10 percentage points)
    Tangential shrinkage total = 10.5% = 0.105
    (quartersawn = mostly radial face, but width is tangential for flatsawn)

    For FLATSAWN (width is tangential):
    ΔD = 150 × (10/30) × 0.105 = 150 × 0.333 × 0.105 = 5.25 mm movement

    For QUARTERSAWN (width is radial):
    Radial S = 5.6% = 0.056
    ΔD = 150 × (10/30) × 0.056 = 150 × 0.333 × 0.056 = 2.8 mm movement

  CONCLUSION: Quartersawn oak moves roughly HALF as much as flatsawn oak
  across the same humidity swing — central reason for quartersawing premium furniture
```

### Movement Classification

| Category | Radial | Tangential | Example |
|----------|--------|------------|---------|
| Very small | < 3% | < 6% | Western red cedar, teak |
| Small | 3–4% | 6–8% | Douglas-fir, pine |
| Medium | 4–5% | 8–10% | Black walnut, cherry |
| Large | > 5% | > 10% | Oak, ash, hard maple |

---

## Section 6 — Mechanical Properties

### Key Mechanical Properties

```
PROPERTY HIERARCHY (structural selection):

  Stiffness (MOR)  --> beams, flooring (deflection-limited)
  Strength (MOR)   --> rafters, joists (stress-limited)
  Hardness (Janka) --> flooring, tool handles (wear-limited)
  Toughness        --> tool handles, sports equipment (impact-limited)
  Shear            --> fastener resistance, dowel joints

  MODULUS OF ELASTICITY (E, or MOE):
  Measures stiffness — resistance to deflection
  EL range: 5–20 GPa for most commercial woods
  Douglas-fir: ~13 GPa | Hard maple: ~12 GPa | Balsa: ~3.5 GPa

  MODULUS OF RUPTURE (MOR):
  Measures bending strength — force to break a beam
  Hard maple: ~110 MPa | Douglas-fir: ~85 MPa | Balsa: ~21 MPa
```

### Compression vs. Tension Asymmetry

Wood is significantly stronger in tension parallel to grain than in compression. Under bending loads, the compression face buckles before the tension face fractures. This is why wooden beams often fail by crushing on the compression side first.

```
  BENDING BEAM:
  [Load applied at center]
      ↓
  +=======================+  <-- compression face (fails first; buckling)
  |                       |
  +=======================+  <-- neutral axis (no stress)
  |                       |
  +=======================+  <-- tension face (high strength; fails second)

  Rule of thumb: compression strength || grain ≈ 50–65% of tension strength || grain
```

---

## Section 7 — Natural Durability

Natural durability (heartwood resistance to decay and insects without treatment) depends on extractive chemistry, not density alone.

```
DURABILITY CLASSES (EN 350 / European standard):

  Class 1: Very durable   -- >25 yr in-ground    (teak, olive, robinia)
  Class 2: Durable        -- 15–25 yr            (sweet chestnut, Douglas-fir, western red cedar)
  Class 3: Moderately dbl -- 10–15 yr            (Oregon pine, larch)
  Class 4: Slightly dbl   -- 5–10 yr             (Scots pine, Norway spruce)
  Class 5: Not durable    -- < 5 yr              (birch, beech, ash, lime — ALL require treatment)
```

| Species | Key Extractive | Durability |
|---------|---------------|------------|
| Teak | Tectoquinone, silica | Class 1 |
| Robinia (black locust) | Robinetin, phenolics | Class 1 |
| Western red cedar | Thujaplicins (tropolones) | Class 2 |
| White oak | Tannins + tyloses | Class 2 |
| Douglas-fir | Pinosylvin, flavonoids | Class 3 |
| Scots pine (sapwood) | None | Class 5 |

---

## Decision Cheat Sheet

| Need | Species / Cut to Choose |
|------|------------------------|
| Minimum movement in furniture (solid wood) | Quartersawn teak or white oak; small T/R ratio |
| Hardest domestic flooring | Hard maple (1450 lbf) or hickory (1820 lbf) |
| Maximum stiffness/weight beam | Douglas-fir (high E/density ratio) |
| Tool handle (impact toughness) | Hickory (energy absorption), ash |
| Outdoor decking without treatment | Teak, ipe, black locust |
| Lightweight structure (aircraft, model) | Balsa core + composite facing |
| Musical instrument soundboard (Sitka spruce) | High E/density, straight grain, low damping |

---

## Common Confusion Points

**Janka hardness is a surface indentation test, not a general strength test.**
A high Janka value does not mean the wood is strong in bending or tension. Balsa is weak in every way. Teak is moderately hard but extremely durable outdoors. These are independent properties.

**Shrinkage is from green to oven-dry, but real-world movement is partial.**
If a spec sheet says "tangential shrinkage 9.9%," that is the total shrinkage from ~30% MC to 0% MC. Your real-world board will move through a fraction of that range (e.g., 8% to 16% MC = ~27% of the total range), so multiply by the fractional MC change.

**"Dry" lumber at the lumberyard is not your interior EMC target.**
Kiln-dried to 15% for shipping will still gain or lose moisture before equilibrating to 8–10% in a heated North American interior. Wood movement calculations must account for the MC change from purchase to installation.

**Density from a reference is specific gravity at a stated condition — always check.**
"Specific gravity 0.68" at green volume is not the same as at air-dry volume. Air-dry SG is typically 5–10% higher than green-volume SG because the wood has shrunk.

**Figure is not grain.**
"Figured maple" has wavy grain that creates the curly or quilted visual pattern — but the grain deviation reduces strength along the piece axis. Beautiful ≠ structurally optimal.
