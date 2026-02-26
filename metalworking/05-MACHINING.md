# Machining

## The Big Picture

Machining is **controlled material removal** — using cutting tools harder than the workpiece to shear away material and produce precise geometry. It's the process of last resort for tolerances that casting, forging, or rolling cannot achieve: bores, threads, precision surfaces, and complex 3D profiles.

```
MACHINING LANDSCAPE:

  SINGLE-POINT CUTTING          MULTI-POINT CUTTING          ABRASIVE
  (one cutting edge)            (multiple edges)              (many cutting grains)
  ─────────────────────         ──────────────────────        ────────────────────
  Turning (lathe)               Milling (end mill,            Grinding (wheel)
  Boring (boring bar)            face mill)                   Honing (sticks)
  Planning                      Drilling (drill bit)          Lapping (compound)
  Shaping                       Reaming                       Superfinishing
  Threading (single-point)      Broaching (pull)              EDM (spark erosion)
  Parting/Grooving              Tapping (thread)

  Coarser, faster                                             Finer, slower
  Less accurate                                              More accurate
  Less capital                                               More capital (grinding)
```

---

## Cutting Mechanics

### The Metal Cutting Zone

```
CUTTING GEOMETRY (orthogonal model):

  WORKPIECE → moves into tool OR tool moves through workpiece

  Cutting zone (chip formation):
  ┌─────────────────────────────────────────────────────────────┐
  │   Uncut chip thickness (t₁)                                 │
  │   ─────────────────────────────────────────────             │
  │                              ╱╱╱╱╱╱╱╱╱╱╱╱╱ chip flows     │
  │                         ╱ PRIMARY         along tool face   │
  │                    ╱ SHEAR ZONE ╲                           │
  │               ╱   (45°±rake/2)  ╲                          │
  │          ╱ (material shears here) ╲                         │
  │      ─────────────────────────────╲──────                   │
  │                        TOOL    ╲   Flank face               │
  │                            Rake angle α                      │
  └─────────────────────────────────────────────────────────────┘

RAKE ANGLE (α): angle between tool face and perpendicular to cutting direction
  Positive rake (tool face tilts toward workpiece direction):
    → Lower cutting force; thinner chip; better surface finish
    → Weaker cutting edge (sharper angle = less material behind edge)
    → Used for: ductile materials (aluminum, copper, soft steel)
  Negative rake:
    → Higher cutting force; tougher edge (more material support)
    → Used for: hard materials (hardened steel, ceramics) with ceramic/CBN tools
    → Harder materials need stronger (more negative rake) tools

RELIEF (clearance) ANGLE:
  Angle between flank face and machined surface
  Prevents tool heel from rubbing machined surface → must be positive
  Too large: weak edge; Too small: rubbing → heat → tool failure

CHIP FORMATION TYPES:
  Continuous chip: ductile materials (Al, mild steel); smooth cutting
  Segmental chip: many engineering materials; periodic fracture
  Discontinuous chip: brittle materials (cast iron, hard plastics); broken chunks
  Built-up edge (BUE): work material welds to tool at low speeds
                        → changes effective rake; creates rough surface; must avoid
                        → increase speed to avoid BUE temperature regime
```

### The Three Zones of Heat Generation

```
HEAT IN CUTTING:
  ~90–95% of cutting energy → HEAT (only 5–10% goes into surface work hardening)

  1. PRIMARY SHEAR ZONE: highest heat generation — shear work in primary zone
  2. SECONDARY ZONE (rake face/chip contact): friction + secondary shear
  3. TERTIARY ZONE (flank/machined surface): minor rubbing

  Heat destination:
    60–80%: carried away in chip → good (evacuated with chip)
    10–20%: into workpiece → bad (causes thermal distortion, residual stress)
    5–15%: into tool → bad (tool temperature limit → tool wear, failure)

  Temperature at cutting edge: 500–1200°C depending on material and conditions
  This is the primary limit on cutting speed
```

---

## Turning

Turning is rotation of the workpiece while a single-point tool traverses along it.

```
TURNING PARAMETERS:

SPINDLE SPEED (n, rpm):
  Surface cutting speed: Vc = π·D·n/1000   [m/min or sfm]
  D = diameter (mm), n = rpm
  → Specify Vc first (material-dependent), calculate n: n = 1000·Vc/(π·D)

FEED (f, mm/rev):
  How far the tool advances per revolution of workpiece
  Fine (0.05–0.2 mm/rev): better surface finish
  Coarse (0.2–0.8 mm/rev): faster material removal, rougher finish

DEPTH OF CUT (ap, mm):
  Radial depth the tool penetrates into workpiece
  Roughing: 2–8mm (maximize MRR)
  Finishing: 0.1–0.5mm (minimize forces → better accuracy)

MATERIAL REMOVAL RATE (MRR):
  MRR = Vc · f · ap  [cm³/min]

SURFACE ROUGHNESS (theoretical):
  Ra ≈ f² / (8·r)   where r = tool nose radius
  → Smaller feed + larger nose radius = smoother surface
  → Actual Ra worse than theoretical due to tool wear, vibration, BUE
```

### Lathe Machine

```
ENGINE LATHE / CNC TURNING CENTER:

  Headstock (drives spindle + chuck) ←── WORKPIECE ──► Tailstock
                                      Bed (ways)
  Carriage (holds tool, traverses along Z)
  Cross-slide (moves tool in X = radial)
  Compound (set angle for taper turning)

  Operations:
  Turning: reduce OD
  Facing: machine end face (flat)
  Boring: enlarge/finish internal bore
  Parting: cut-off to part from bar
  Threading: feed coordinated with spindle → helical thread
  Knurling: press knurl pattern into surface (actually forms, not cuts)

  CNC turning center: same operations with NC control
    Turret: multiple tools indexed automatically
    Live tooling: rotating tools for milling/drilling on lathe
    Sub-spindle: machine back of part without rechucking
```

---

## Milling

Rotating multi-tooth cutter; workpiece traverses beneath or tool moves through workpiece.

```
MILLING GEOMETRY:

Peripheral milling:
  CLIMB MILLING (down milling): cutter rotates in same direction as feed
    Chip thickness: thick at entry → thin at exit
    Advantage: less rubbing → better surface finish; lower power
    Advantage: forces push workpiece into table → less vibration
    Requirement: machine with backlash-free ballscrew (CNC) — otherwise backlash
                  causes table to grab → chatter/damage
    Standard for CNC milling

  CONVENTIONAL MILLING (up milling): cutter rotates against feed
    Chip thickness: thin at entry → thick at exit
    More rubbing at entry → heat; worse surface; work hardening
    Historical necessity with manual machines (backlash in lead screw)
    Still used in special cases: hardened material, interrupted cuts

FACE MILLING: large cutter flat-ends face of workpiece → flat surface
  90% of milling stock removal in production machining

END MILLING: smaller cutter mills slot, pocket, contour, shoulder
  2-flute: aluminum (more chip room, higher speeds)
  4-flute: steel (more cutting edges, better surface)
  High-helix (45°): aluminum, excellent finish and chip evacuation
  Ball-nose: contour milling, 3D surfaces

SPEEDS AND FEEDS IN MILLING:
  Cutting speed Vc → RPM: n = 1000·Vc / (π·D)
  Feed per tooth: fz (mm/tooth)
  Table feed (feed rate): Vf = fz · Z · n   [mm/min]  Z = number of teeth
  MRR = Vf · ae · ap  (ae = radial depth, ap = axial depth)
```

---

## Grinding

Abrasive machining using a bonded wheel; each grain acts as a miniature cutting tool with random rake angles (usually very negative).

```
GRINDING WHEEL SPECIFICATION:
  A 46 H 8 V
  │ │  │ │ │
  │ │  │ │ └── Bond type: V=vitrified, R=rubber, B=resinoid
  │ │  │ └─── Structure (grain spacing): open-8, dense-1
  │ │  └──── Grade (hardness of bond): soft-A, hard-Z
  │ └─────── Grit size: coarse-16, fine-120, very fine-320
  └───────── Abrasive type: A=alumina, C=silicon carbide, B=CBN, D=diamond

GRINDING PARAMETERS:
  Wheel peripheral speed: 25–35 m/s (conventional); up to 180 m/s (high-speed)
  Workpiece speed: much slower (for OD grinding: 15–30 m/min)
  Depth of cut: 0.001–0.05mm (much finer than turning/milling)
  Coolant: critical — grinding generates intense local heat → burns surface if insufficient

GRINDING OPERATIONS:
  Surface grinding: flat surfaces; reciprocating table
  Cylindrical OD grinding: between centers; wheel traverses axially
  Internal grinding (ID): very small wheel inside bore
  Centerless grinding: no spindle; workpiece between wheel + regulating wheel → pass-through
  Thread grinding: precision threads (lead screws, worm gears)

SURFACE INTEGRITY CONCERNS:
  Grinding burns: blue/brown temper colors → local overheating → residual stress
  Grinding cracks: thermal cracks → fatigue initiation sites → failure
  Work hardening or annealing of surface depending on conditions
  Detection: Barkhausen noise test (magnetic), nital etch
  Prevention: correct wheel, adequate coolant, light cuts on hardened steel
```

---

## Cutting Tool Materials

Evolution in cutting tool materials is the primary driver of productivity improvement in machining over 150 years.

```
TOOL MATERIAL EVOLUTION (hardness → wear resistance → allows higher Vc):

  HIGH-SPEED STEEL (HSS) → Tungsten Carbide (WC) → Ceramics/Cermets → CBN → Diamond

  ┌──────────────────────────────────────────────────────────────────┐
  │                                               CUBIC BORON NITRIDE│ ← hardened steel
  │                                  CERAMICS     (CBN)             │
  │                 WC/CO CARBIDE    Al₂O₃/Si₃N₄  3500 HV          │
  │   HSS            400–1800 HV    1600–3000HV    Vc: 200–600m/min │
  │   700–900HV       Vc: 100–400     coated:      for hard turning  │
  │   Vc: 15–50m/min   m/min (steel)  up to 1000m/min               │
  │                                                           DIAMOND│ ← non-ferrous
  └──────────────────────────────────────────────────────────────────┘

HSS (High-Speed Steel, ~1900):
  Alloyed tool steel: W, Mo, V, Co, Cr additions
  Retains hardness to ~600°C (vs carbon steel losing hardness at 200°C)
  Applications: drills, taps, end mills, form tools — complex shapes
  Advantage: tough, can be reground; inexpensive
  Speed limits: ~30–50 m/min for steel

WC/Co CEMENTED CARBIDE (1920s–present, dominant):
  WC grains (HV 2600) in cobalt binder
  Grades: ISO P (steel), K (cast iron), M (stainless), N (nonferrous), S (superalloys)
  WC+TiC: P grades for steel (TiC reduces crater wear)
  WC+Co only: K grades for cast iron, non-ferrous
  Insert grades with coatings (CVD/PVD):
    TiN: yellow; general purpose; reduces BUE
    TiCN: harder; wear-resistant
    Al₂O₃: excellent at high temperature; oxidation resistant
    TiAlN: PVD; excellent for dry machining at high speeds
    Diamond (CVD): for non-ferrous only
  Speeds: 100–400+ m/min depending on material and coating

CERAMICS (Al₂O₃, Si₃N₄):
  Very hard, hot-hard, oxidation resistant → very high speeds
  Brittle: require rigid setup; no interrupted cuts; no coolant shock
  Typical applications: high-speed cast iron, superalloy finish turning
  Silicon nitride (Si₃N₄) whisker-reinforced: toughened for SiC-reinforced Al

CBN (Cubic Boron Nitride):
  Second hardest material after diamond; stable at high temperature
  Can machine hardened steel (60+ HRC) → replaces grinding for some operations
  "Hard turning": tight tolerances + CBN → replaces cylindrical grinding
  Applications: hardened tool steel, hardened gears, bearing races

DIAMOND (PCD and CVD):
  Hardest material; excellent for non-ferrous
  Cannot machine ferrous: Fe dissolves carbon → diamond diffusion wear → catastrophic
  Applications: aluminum, copper, brass, graphite, composites, carbide
  Speeds: very high (> 1000 m/min for aluminum); excellent surface finish
```

---

## CNC and G-Code

Computer Numerical Control: coordinates machine axes via numerical commands.

```
CNC EVOLUTION:

  NC (1950s): MIT Servomechanism Lab + US Air Force
    Punched tape; 2–3 axis; no computer → hard-wired logic
    → First CNC machine: MIT 1952 milling machine

  CNC (1970s): dedicated mini-computer in each machine
    Magnetic tape, then floppy disk
    Conversational programming (dialog at machine)

  CAD/CAM integration (1980s–90s):
    Design in CAD → post-process to G-code → machine
    CATIA, Pro/E (now Creo), Mastercam, SurfCAM (acquired by Hexagon/Vero)

  Modern CNC (2000s+):
    5-axis simultaneous machining
    High-speed machining (HSM): very high RPM (50,000+) + light cuts → fast material removal
    Adaptive machining: measure part in-process; adjust program
    Intelligent fixture: in-situ measurement, self-compensation
    Current CAM packages: Fusion 360 CAM (Autodesk, cloud-linked CAD/CAM),
      Mastercam (standalone, high-end shop standard), SolidCAM / HSMWorks
      (SolidWorks integrated), Siemens NX CAM (aerospace/defense tier)

G-CODE BASICS (RS-274D standard):
  Geometric codes:
    G00: Rapid positioning (traverse speed, not cutting)
    G01: Linear interpolation (at programmed feed rate)
    G02: Circular arc CW
    G03: Circular arc CCW
    G17/18/19: XY/XZ/YZ plane selection

  Machine operation codes:
    M03/M04: Spindle start CW/CCW
    M05: Spindle stop
    M06: Tool change
    M08/M09: Coolant on/off
    M30: End of program

  Example: Turning a 25mm OD diameter on a lathe
    N10 G21          (metric mode)
    N20 G95          (feed per revolution)
    N30 G97 S1500    (constant spindle speed 1500 RPM)
    N40 T0101 M06    (select tool 1)
    N50 M03          (spindle on CW)
    N60 G00 X27 Z2   (rapid to starting position)
    N70 G01 X25 F0.2 (plunge to diameter, feed 0.2mm/rev)
    N80 Z-50         (turn for 50mm length)
    N90 G00 X50 Z5   (rapid clear)
    N100 M30         (end)
```

---

## Speeds and Feeds Reference

| Material | Tool | Cutting speed Vc | Feed (turning) | Notes |
|---------|------|-----------------|----------------|-------|
| Low-C steel | Carbide coated | 200–400 m/min | 0.2–0.5 mm/rev | Dry or flood |
| Alloy steel | Carbide coated | 150–300 m/min | 0.15–0.4 mm/rev | Flood coolant |
| Hardened steel (60HRC) | CBN | 100–250 m/min | 0.05–0.2 mm/rev | Dry (CBN tolerates heat) |
| Cast iron | Carbide K-grade | 150–400 m/min | 0.2–0.5 mm/rev | Dry (fine chips) |
| Aluminum 6061 | PCD or 2-flute end mill | 400–1500 m/min | 0.1–0.5 mm/rev | Flood/mist |
| Titanium Ti-6Al-4V | Carbide TiAlN coated | 40–80 m/min | 0.05–0.15 mm/rev | Flood (critical!) |
| Inconel 718 | Carbide PVD coated | 15–40 m/min | 0.05–0.2 mm/rev | Flood; high tool pressure |

---

## Decision Cheat Sheet

| Requirement | Process |
|-------------|---------|
| Tight tolerance bore (H7) | Boring then ream; or precision CNC turn |
| External precision OD | CNC turning + cylindrical grinding |
| Complex 3D surface | 5-axis CNC milling |
| Flat precision surface (Ra < 0.8µm) | Surface grinding |
| Thread cutting (precision) | Single-point turning or thread grinding |
| High-volume, simple shapes | Broaching or gear hobbing |
| Hardened steel (60 HRC) | CBN hard turning; or cylindrical grinding |
| Non-ferrous (Al/Cu) at speed | PCD tools; high RPM; flood coolant |

---

## Common Confusion Points

**Cutting speed (m/min) ≠ spindle speed (RPM)**
Cutting speed is the velocity of the work surface relative to the tool — a material property of the cutting condition. RPM depends on the diameter: for the same cutting speed, a small diameter needs much higher RPM than a large diameter. CNC programs often specify cutting speed and the control calculates RPM dynamically as diameter changes.

**Climb milling is preferred on CNC; conventional milling was historical necessity**
Climb milling's chip-thickens-at-exit characteristic is better for tool life and surface finish. It required CNC's backlash-free ballscrews to avoid the table grabbing. On manual mills with lead screws, backlash made climb milling dangerous. On CNC with zero-backlash ballscrews, climb is standard.

**Grinding is not just "fine finishing" — it's a separate cutting process**
Grinding uses abrasive grains with random, large-negative rake angles. The cutting geometry is nothing like turning or milling. Each grain plows and shears the material. The process parameters (wheel grade, conditioning, coolant) are completely independent of turning parameters. You can't just substitute a grinding wheel for a milling cutter.

**CBN for hardened steel; diamond for non-ferrous — not interchangeable**
Diamond dissolves in iron at cutting temperatures → catastrophic tool failure on steel. CBN doesn't have this reaction but lacks diamond's hardness advantage on soft materials. The chemical affinity issue is the reason diamond can't be used on ferrous metals even though it's harder than CBN.

**CNC doesn't make machining easy — it makes complex geometries repeatable**
CNC automates the execution of a programmed tool path. You still need to know: cutting conditions (speeds/feeds/tools), fixture design to hold the part, part setup and coordinate system definition, and how to verify the program won't crash the machine. CNC without machining knowledge is how you destroy expensive machines.
