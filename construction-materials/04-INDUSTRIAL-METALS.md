# Construction Materials — Industrial Metals

## The Big Picture: Iron and Steel Evolution

```
IRON AND STEEL METALLURGY TIMELINE
┌──────────────────────────────────────────────────────────────────────────────┐
│                                                                              │
│  1709  Darby smelts iron with coke (not charcoal) → scale increases          │
│  1779  Ironbridge, Coalbrookdale → first cast iron bridge                    │
│  1784  Cort's puddling process → wrought iron at industrial scale            │
│  1820  Tredgold's "Practical Essay on Cast Iron" → design rules emerge       │
│  1851  Crystal Palace, London → prefab cast iron + glass system              │
│  1856  Bessemer converter → cheap mild steel in bulk                         │
│  1864  Open-hearth furnace (Siemens-Martin) → better steel quality control   │
│  1880  American hot-rolling mills → standard I-beam sections                 │
│  1885  Home Insurance Building, Chicago → first steel skeleton frame         │
│  1890s Riveted connections standard → replaced by bolting post-1950          │
│  1950s Electric arc furnace → scrap-based steelmaking                        │
│  1960s Bolted high-strength connections → A325/A490                          │
│  1970s Continuous casting → replaces ingot pouring                           │
│  1980s TMCP steels → higher strength through process control                 │
│  2000s EAF + DRI (direct reduced iron) → lower CO₂ steelmaking               │
│                                                                              │
│  CARBON CONTENT IS EVERYTHING:                                               │
│  Pig iron (blast furnace output):   3–5% C → very brittle                    │
│  Cast iron (remelted + poured):     2–4% C → brittle in tension              │
│  Wrought iron (worked, slag-rich):  <0.1% C → ductile, fibrous               │
│  Mild steel (structural):           0.15–0.30% C → balanced properties       │
│  High-carbon steel:                 0.6–1.5% C → hard but brittle            │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Cast Iron: Metallurgy and Structural Properties

### Microstructure

Cast iron (2–4% carbon) has carbon in two forms depending on cooling rate:

```
CAST IRON MICROSTRUCTURES
──────────────────────────────────────────────────────────────────────────────
  GREY CAST IRON:  slow cooling → carbon forms graphite flakes
    Graphite flakes: act as internal notches → stress concentrators
    → brittle in tension (flakes = pre-existing crack-like defects)
    Comp. strength: ~570 MPa  ← excellent
    Tensile strength: ~140–280 MPa  ← poor relative to comp.
    E: ~100–170 GPa
    CRITICAL RATIO: σ_comp / σ_tens ≈ 4:1
    → design cast iron ONLY in compression; avoid tension and bending

  WHITE CAST IRON:  fast cooling → carbon forms iron carbide (Fe₃C, cementite)
    Hard, brittle, harder than grey → abrasion-resistant
    Too brittle for structural use; used for mill rolls, brake drums

  MALLEABLE CAST IRON:  white iron heat-treated (anneal) → temper carbon nodules
    Better ductility than grey; used for fittings, brackets

  DUCTILE (NODULAR) CAST IRON:  Mg addition → spherical graphite nodules
    Much better tensile: ~420–900 MPa
    Modern "ductile iron": used for cast iron pipes, manhole covers
    Still stiffer and more brittle than steel
```

### Cast Iron in Structural Use: Coalbrookdale Bridge (1779)

The Iron Bridge at Coalbrookdale was the first cast iron arch bridge in the world.
It reveals both the promise and the limitation of cast iron as a structural material.

```
IRON BRIDGE, COALBROOKDALE: STRUCTURAL LOGIC
──────────────────────────────────────────────────────────────────────────────
  Span: 30.5 m  Rise: 12 m  (shallow arch, semi-circular segments)
  Construction: each main rib cast as two half-ribs, bolted at crown
  LOAD PATH: vehicular + self-weight → compression in arch ribs → abutments
  → arch is pure compression → cast iron's strength: CORRECT application
  → all connections: mortise-and-tenon joints CAST IN to members
    (i.e., carpenter geometry applied to iron — designers had no iron joint vocabulary)

  PROBLEM REVEALED:
  Wind loads + thermal movement + live load eccentricity → BENDING in ribs
  → tension in bottom flange of any rib → cast iron fails suddenly
  → multiple ring members cracked within first decade
  → bridge patched and eventually closed to traffic

  LESSON: cast iron arch = correct structural form
          cast iron beam = dangerous (tension in bottom fiber)
          cast iron column = works if short and well-braced
```

### Cast Iron Columns: Acceptable Use

Hollow cast iron columns were used extensively 1800–1870 in mill buildings.
Under concentric axial compression they work well. The critical failure mode
is eccentric loading (column not truly concentric) → bending → tensile crack
on the tension face → sudden collapse.

```
CAST IRON COLUMN BEHAVIOUR
──────────────────────────────────────────────────────────────────────────────
  CONCENTRIC LOAD:    all faces in compression → cast iron works
  ECCENTRIC LOAD:     one face in tension → crack initiates → brittle collapse
  FIRE:               rapid temperature rise → no ductile warning → sudden fail
                      cast iron loses strength rapidly above 450°C

  DISASTERS from cast iron:
  Dee Bridge (1847): Robert Stephenson design — cast iron beams over 29.0 m
    → tension in bottom flange → transverse crack → collapse under train load
    → 5 deaths; Fairbairn subsequently proved cast iron beam inadequacy
  Bradford nightclub fire (1995): cast iron columns in older building
    → sudden collapse when heated; no plastic deformation warning

  RECOGNITION: cast iron vs wrought iron vs steel (visual/site test):
  Cast iron: file marks leave white/grey dust; dull mottled break; cannot spark-test
  Wrought iron: fibrous fracture (like wood); spark test → long, bushy spark trail
  Steel: regular grain; spark test → bright star burst sparks
```

---

## Wrought Iron: The Transition Material

### Puddling Process (Cort, 1784)

Wrought iron production before the Bessemer converter required the "puddling" process:

```
WROUGHT IRON PUDDLING PROCESS
──────────────────────────────────────────────────────────────────────────────
  1. Pig iron (3–4% C) charged into reverberatory furnace
     → fuel (coke/coal) burns; flame reflected onto iron
     → pig iron melts
  2. Puddler stirs the molten iron with iron rods through furnace ports
     → oxygen from furnace atmosphere reacts with carbon:
        C + O → CO (carbon removed as gas)
  3. As carbon drops, iron solidifies (it melts at higher temp as C drops)
     → pasty mass ("bloom") → carbon content drops to <0.1%
  4. Bloom removed; hammered under tilt-hammer → squeezes out slag
     → slag inclusions remain as stringers → FIBROUS MICROSTRUCTURE
  5. Rolled into bars, sheets, angles, rails

  SLAG INCLUSIONS ARE IMPORTANT:
  → give wrought iron directional strength like timber
  → parallel to rolling direction: strong in tension (σ_t ~ 280–350 MPa)
  → perpendicular to rolling: weaker
  → this is why wrought iron bridge and truss elements often show specific orientation

  SCALE LIMITATION:
  Puddling is manual, skill-intensive, slow
  One furnace + one skilled puddler → ~200 kg/day
  → impossible to scale to Chicago skeleton frame demand
  → Bessemer converter solved this
```

### Wrought Iron Properties vs Cast Iron and Steel

| Property | Cast iron | Wrought iron | Mild steel (A36) |
|---|---|---|---|
| Carbon content | 2–4% | <0.1% | 0.15–0.30% |
| Tensile strength | 140–280 MPa | 280–350 MPa | 400 MPa |
| Compressive strength | 570 MPa | 350–400 MPa | 400 MPa |
| Yield strength | No yield (brittle) | ~230–280 MPa | 250 MPa |
| Elongation at failure | 0.5–1% | 15–25% | 20–30% |
| Young's modulus E | 100–170 GPa | 190–200 GPa | 200 GPa |
| Weldability | Very poor | Poor | Good |
| Behaviour in tension | Brittle fracture | Ductile | Ductile |

---

## Bessemer Converter: Mass Production of Structural Steel

```
BESSEMER CONVERTER PROCESS (1856)
┌──────────────────────────────────────────────────────────────────────────────┐
│                                                                              │
│  1. Tilt converter → charge with ~15–20 tonnes molten pig iron (3.5–4% C)    │
│                                                                              │
│  2. Upright → blast air through tuyères in converter bottom                  │
│      O₂ in air → reacts with C, Si, Mn in molten iron                        │
│      C + O₂ → CO₂/CO  (carbon removed; violent reaction; intense flame)      │
│      Si + O₂ → SiO₂ (into slag)                                              │
│      Mn + O₂ → MnO (into slag)                                               │
│                                                                              │
│  3. Blow duration: ~15–20 minutes                                            │
│     → C drops from ~4% to <0.1% (OVER-blown) → iron oxidized                 │
│                                                                              │
│  4. Add ferromanganese: re-carburizes to target C; deoxidizes                │
│     → target C: 0.15–0.30% for mild steel                                    │
│                                                                              │
│  5. Tilt → pour into ladle → teemed into ingot molds                         │
│                                                                              │
│  PROBLEMS:                                                                   │
│  Cannot remove phosphorus (need basic lining → Thomas converter, 1878)       │
│  Nitrogen pickup from air → strain-age embrittlement                         │
│  Tight carbon control difficult → variable product                           │
│  → superseded by open-hearth furnace by 1900 for quality work                │
│                                                                              │
│  REVOLUTION:                                                                 │
│  15–20 minutes for 20 tonnes vs 5 hours/200 kg for wrought iron puddling     │
│  Cost drop: steel price fell ~85% between 1865 and 1880                      │
│  → skeleton steel frame buildings viable                                     │
│  → the Chicago School of architecture became economically possible           │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

### Open-Hearth → Basic Oxygen → Electric Arc: Process Evolution

```
STEELMAKING PROCESSES COMPARED
──────────────────────────────────────────────────────────────────────────────
  OPEN-HEARTH FURNACE (Siemens-Martin, 1864):
    Heat time: 8–10 hours per heat
    Capacity: 100–400 tonnes
    Chemistry control: good (samples taken during heat)
    Input: mix of pig iron and scrap
    Dominated 1900–1960s; now obsolete
    Advantage over Bessemer: time → better composition control

  BASIC OXYGEN FURNACE (BOF, 1952–present):
    Heat time: 20–40 minutes
    Capacity: 200–400 tonnes
    Process: pure O₂ blown through lance onto pig iron (not air)
      → much faster than open-hearth; no nitrogen pickup
    Input: ~80% hot metal (from blast furnace) + 20% scrap
    World dominant process for new iron input steelmaking
    CO₂: ~2 tCO₂/t steel (blast furnace + BOF integrated route)

  ELECTRIC ARC FURNACE (EAF, 1960s–present):
    Heat time: 60–90 minutes
    Capacity: 50–400 tonnes
    Process: graphite electrodes arc to melt scrap
    Input: up to 100% steel scrap
    CO₂: ~0.3–0.6 tCO₂/t steel (scrap-based; uses grid electricity)
    → Low-carbon future: EAF + green electricity = near-zero carbon steel
    Direct reduced iron (DRI): Fe₂O₃ + H₂ → Fe + H₂O (green H₂ route)
      → bypasses coke-based blast furnace → feeds EAF
      → SSAB HYBRIT process: first hydrogen-DRI steel 2021
      → cost parity with conventional: ~2030s projected

  Current CO₂:
    Integrated (BF+BOF): ~1.8–2.1 tCO₂/t crude steel
    Scrap EAF:           ~0.3–0.6 tCO₂/t crude steel
    → ASTM A36 from EAF scrap: embodied carbon ~0.6–1.0 kgCO₂e/kg
    → vs ~1.8–2.5 kgCO₂e/kg for integrated route
    → recycled content specification now normal in green procurement
```

---

## Steel Grades for Structural Use

```
STRUCTURAL STEEL GRADES (ASTM / AISC system)
┌──────────────────────────────────────────────────────────────────────────────┐
│                                                                              │
│  GRADE       Fy (MPa)  Fu (MPa)  C max   NOTES                               │
│  ─────────────────────────────────────────────────────────────────────────   │
│  A36         250       400       0.26%   Most common; weldable; ductile      │
│  A572 Gr.50  345       450       0.23%   High-strength low-alloy (HSLA)      │
│  A572 Gr.60  415       520       —       Less common; thin plates mainly     │
│  A913 Gr.65  450       550       0.20%   Quench+temper+self-temp; seismic    │
│  A514        690       760       0.21%   High-strength Q+T; bridges, cranes  │
│  A992        345       450       0.23%   Wide-flange shapes; seismic (Fy/Fu) │
│  S275 (EU)   275       430       —       Euronorm equivalent of A36          │
│  S355 (EU)   355       490       —       Euronorm equivalent of A572 Gr.50   │
│  S460 (EU)   460       540       —       High strength; bridges              │
│                                                                              │
│  HSLA (High-Strength Low-Alloy) concept:                                     │
│    Add small amounts of Nb, V, Ti → precipitation hardening                  │
│    → Fy 50–100% higher than mild steel; no loss of weldability               │
│    → less steel needed → lighter structure → less embodied carbon            │
│                                                                              │
│  THERMO-MECHANICALLY CONTROLLED PROCESS (TMCP):                              │
│    Controlled rolling temperature + accelerated cooling                      │
│    → fine grain structure → high Fy without heavy alloying                   │
│    → better weldability (lower carbon equivalent)                            │
│                                                                              │
│  A992 SEISMIC REQUIREMENT:                                                   │
│    Fy/Fu ≤ 0.85 (strain-hardening ratio)                                     │
│    → ensures ductile yielding zone before fracture                           │
│    → critical for plastic hinge behaviour in seismic frames                  │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Hot Rolling: From Ingot to Section

```
HOT ROLLING SEQUENCE
──────────────────────────────────────────────────────────────────────────────
  INGOT  →  BLOOM  →  BILLET or SLAB  →  FINISHED SECTION
  (cast)    (250mm+)  (< 250mm sq / flat)  (beam/plate/rebar)

  Temperatures: rolling at 1100–1250°C (above recrystallization temperature)
    → steel is soft, ductile → plastic deformation without fracture
    → grain structure recrystallizes after each pass → refined grain

  BLOOM → BEAM (I-section):
  Multiple passes through shaped rolls progressively:

  Pass 1-3: [  ] → initial I-shape rough form
  Pass 4-7: [  ] → deeper web, broader flanges
  Pass 8-12: [  ] → final dimensions approached
  Finished:  [I ] → web + flanges at final thickness

  WIDE FLANGE vs STANDARD I-BEAM:
  Standard I (S-beam): tapered flanges (inner face angled); older design
  Wide flange (W-beam): parallel flanges; easier to weld, bolt to flat surface
    → W-series dominates modern construction
    → notation: W18×97 = 18" nominal depth × 97 lb/ft weight

  WHY I-SECTION GEOMETRY:
  Bending stress: σ = Mc/I  →  maximize I (second moment of area)
  Most material should be far from neutral axis (flanges)
  Web: resists shear; needs minimum area, not position
  → I-section achieves maximum I for minimum material
  → specific 2nd moment: I/A (I per unit area) maximized
```

---

## Connections: Riveted → Bolted → Welded

### Riveted Connections (1850s–1950s)

```
RIVETED CONNECTION: HOW IT WORKS
──────────────────────────────────────────────────────────────────────────────
  HOT RIVET PROCESS:
  1. Rivet heated to cherry-red (~900°C) in portable forge
  2. Tossed to holder-up who catches in bucket on far side of joint
  3. Placed in pre-punched/drilled hole
  4. Buck-up bar holds tail of rivet
  5. Riveting hammer (pneumatic) forms head on near side → 3–8 seconds
  6. Rivet cools → CONTRACTS → clamping force on plates
  → clamping force: σ_clamp ≈ 150–200 MPa (from thermal contraction)

  LOAD TRANSFER in RIVETED CONNECTION:
  Friction: clamping force × μ × contact area (governs small loads)
  Bearing: rivet shank bears against hole edge (governs large loads)
  Shear: rivet shank in shear across the interface plane

  WHY RIVETS ARE RELIABLE:
  → thermal clamping is self-locking; no torque relaxation
  → ductile failure mode (rivet yields before fracture)
  → inspectable (loose rivet sounds hollow when tapped)

  DISADVANTAGE:
  → skilled 4-person gang per rivet; slow; hot; loud
  → 1940s: HSFG bolts arrived → bolts increasingly replace
  → post-1950s bridges/buildings: bolted or welded
```

### High-Strength Friction Grip (HSFG) Bolts

```
HSFG BOLT CONNECTION TYPES
──────────────────────────────────────────────────────────────────────────────
  ASTM A325: medium strength (F_u = 825 MPa)
  ASTM A490: high strength (F_u = 1040 MPa)
  EN 8.8, 10.9: European equivalents

  CONNECTION TYPES:

  SLIP-CRITICAL (friction):
    Bolt torqued to specified pretension (typically 70% proof load)
    → plates clamped together; frictional resistance carries shear
    → no slip at service loads; joint behaves as rigid
    Required for: seismic; vibrating loads; connections where slip = structural problem
    Friction surfaces: Class A (clean mill scale, μ = 0.33) to Class D (hot-dip zinc, μ = 0.35)

  BEARING (non-slip):
    Bolt torqued to snug-tight only (wrench effort by one person)
    → bolt shank bears against hole edge at service load
    → hole slightly larger than bolt → slip occurs → bolt bears
    Required: lower stress connections; non-seismic
    Cheaper to install than slip-critical

  PRETENSIONING METHODS:
  Turn-of-nut: snug tight + specified nut rotation (1/3 to 1 full turn)
  Direct tension indicator (DTI): washer with protrusions that squash at correct tension
  Torque wrench: specific torque → tension (less reliable; torque vs tension variability)
  Tension-control bolt: shear-break installation → breaks when tension reached
```

### Welded Connections

```
STRUCTURAL WELDING PROCESSES
──────────────────────────────────────────────────────────────────────────────
  SMAW (Shielded Metal Arc Welding): stick welding
    → consumable electrode with flux coating → flux burns → gas shield
    → manual; versatile; all positions; slower
    → site welding; repair work

  FCAW (Flux Cored Arc Welding): semi-automatic
    → wire electrode with flux core; continuous wire feed
    → semi-auto; faster than SMAW; often used with CO₂ shield gas
    → fabrication shop and site use

  SAW (Submerged Arc Welding): automatic, high deposition
    → arc under granular flux blanket → high deposition rate
    → flat or horizontal only; high quality; high productivity
    → shop fabrication of girders (web-to-flange welds)

  WELD TYPES:
  Fillet weld: most common; triangular cross-section at joint corner
    Design strength: 0.6 × F_u × (a/√2)  per unit length
    where a = leg size
  Full penetration butt weld (FPBW): full thickness fusion; strongest; expensive
  Partial penetration (PPBW): cheaper; do not use where tension perpendicular to weld

  PRE-HEAT AND POST-WELD HEAT TREATMENT (PWHT):
  Pre-heat: prevents hydrogen cracking (cold cracking)
    Required for: thicker plates (>25 mm); higher CE (carbon equivalent)
    CE = C + Mn/6 + (Cr+Mo+V)/5 + (Ni+Cu)/15
    If CE > 0.40: pre-heat required; if > 0.70: significant pre-heat
  PWHT: stress relieve after welding
    Required for: pressure vessels; fatigue-critical details; high-restraint joints
    Not routine for building frames but sometimes for plate girders
```

---

## Crystal Palace (1851): Prefabrication Revolution

```
CRYSTAL PALACE: MODULAR PREFABRICATION SYSTEM
──────────────────────────────────────────────────────────────────────────────
  Total floor area:    72,000 m²  (26 acres under glass)
  Construction time:   17 weeks from bare ground to complete building
  Designed by:         Joseph Paxton (gardener → engineer)
  Structural system:   Cast iron + wrought iron + glass; modular grid

  MODULE: 7.3 m (24 ft) × 7.3 m plan grid
    → dictated by: maximum glass sheet size available (1.2 m × 0.25 m)
    → entire building is multiple of this module
    → enables advance fabrication of all identical cast iron columns + beams

  CAST IRON COLUMNS:  hollow cylinder; 4.9 m long + socket-and-spigot joints
    → stacked to 3 heights (14.6 m max)
    → 3,300 columns total; all identical → cast from one pattern

  WROUGHT IRON ROOF TRUSSES:  Paxton's lightweight lattice trusses
    → span 7.3 m between columns; pre-fabricated off-site

  GLASS:  Chance Brothers (Birmingham); cylinder process
    → 300,000 panes of glass; 84,000 m² total

  INNOVATION: No wet trades. All components dry-assembled, bolted, slotted.
    → modern prefabrication/DfMA (Design for Manufacture and Assembly) concept
    → cost: £79,000 (vs £300,000+ for conventional masonry building)
```

---

## Decision Cheat Sheet

| Question | Answer |
|---|---|
| Cast iron beam — safe to use? | No: brittle in tension; use only in compression (column, arch) |
| Identify cast iron vs steel on site? | Spark test (steel → bright stars; cast iron → dull red sparks) or fibrous fracture (wrought iron) |
| High-strength steel saves material — but when not to use? | Long columns: Euler buckling depends on E (=200 GPa all grades); Fy doesn't help |
| Slip-critical vs bearing bolt connection? | Slip-critical: seismic, vibration, high shear reversal; bearing: normal static connection |
| EAF steel vs BOF steel — why specify? | EAF from scrap = 60–80% lower embodied carbon; specify recycled content % |
| Pre-heat required for site weld? | Check CE value: CE > 0.40 → pre-heat; consult welding engineer |
| W-beam vs S-beam — which for modern construction? | W-beam (parallel flanges): simpler bolting, better for welded connections |
| Rivets — when to retain in historic structure? | Leave in place unless loose (tap test) or corroded through; replacement difficult |
| A992 vs A36 — seismic design? | A992 specifies Fy/Fu ≤ 0.85 → ductile plastic hinge behaviour; use A992 for seismic moment frames |

---

## Common Confusion Points

**Higher-grade steel does NOT increase column buckling resistance.** Euler critical
load P_cr = π²EI/L_eff² depends on E (always 200 GPa for all steel grades) and I
(geometric property). Using A514 (Fy = 690 MPa) instead of A36 (Fy = 250 MPa) does
not help a slender column. Grade upgrade only helps stocky columns (short, large r)
where yielding governs, not buckling.

**The Bessemer converter used AIR — this is why it failed to replace open-hearth for
quality work.** Air contains 78% nitrogen. Nitrogen dissolves into molten steel →
strain-age embrittlement over time. Open-hearth furnace had no nitrogen pickup (air
not blown through melt). BOF uses pure O₂ → no nitrogen → much better than Bessemer.

**Welding and riveting require completely different design approaches.** Riveted
connections: shear in rivet shank; bearing on hole edge; friction (clamping). Welded
connections: shear/tension/compression in weld throat; preheat to avoid cracking.
An existing riveted connection cannot simply be "upgraded" by adding welds — the
load paths are different and incompatible.

**Cast iron columns failed in fires — NOT because iron is flammable.** Cast iron is
non-combustible. The problem is: cast iron has NO plastic deformation zone. At
~450–500°C, cast iron columns simply shatter (brittle fracture under thermal stress +
floor loads). Wrought iron and mild steel deform before failing — giving structural
warning and slower collapse. Post-Grenfell: even steel columns need intumescent
protection because ductile steel loses 50% strength at 550°C regardless.

**Continuous casting (post-1970) changed everything about product quality.** Old
ingot casting → segregation of carbon and alloying elements → heterogeneous slab →
variable properties. Continuous casting → controlled cooling → uniform composition →
consistent mechanical properties. Modern structural steel is significantly more
consistent than pre-1970 material — important for historic building assessment.
