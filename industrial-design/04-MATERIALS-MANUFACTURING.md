# Materials and Manufacturing Constraints

## The Big Picture

Materials and manufacturing processes are not background constraints on design -- they ARE design. The material determines possible forms; the process determines possible features; the cost model determines what can be built at scale. Ignoring these in early design is the single most common reason designs fail to reach production.

```
+----------------------------------------------------------------------+
|           DFM: DESIGN FOR MANUFACTURABILITY                          |
|                                                                      |
|  DESIGN INTENT            MANUFACTURING CONSTRAINT     RESULT        |
|  (what designer wants)    (what process allows)         (trade-offs) |
|                                                                      |
|  Sharp internal corner    Injection mold min radius     Radii needed |
|  Perfectly flat surface   Warpage in plastics           Ribs needed  |
|  Invisible seam           Parting line always visible   Locate seam  |
|  Uniform wall thickness   Thin walls cool unevenly      Redesign     |
|  Seamless enclosure       Assembly requires access      Add seam     |
|  Tight tolerances         Cost scales with precision    Relax specs  |
|                                                                      |
|  BRIDGE: This is exactly constraints programming. The design         |
|  solution space is the intersection of:                              |
|  aesthetic intent ∩ engineering specs ∩ manufacturing envelope       |
+----------------------------------------------------------------------+
```

---

## Material Selection: The Decision Framework

### Material Properties That Drive Design Choice

```
MATERIAL PROPERTIES MATRIX

PROPERTY          WHAT IT DETERMINES                 TESTING METHOD
-----------------+----------------------------------+------------------
Tensile strength  Maximum stress before failure      ASTM D638 (plastics)
                  Wall thickness; rib spacing         ASTM E8 (metals)

Stiffness (E)     Deflection under load              Flexural modulus
                  Snap-fit design; hinge design       Young's modulus

Hardness          Surface scratch resistance          Shore A/D (plastics)
                  Durability of visible surfaces      Rockwell (metals)

Impact strength   Drop resistance                    Charpy/Izod test
                  How thick walls must be

Thermal expansion How dimensions change with temp    CTE value
                  Joint design; outdoor products

Density           Weight; shipping cost              g/cm3
                  Perceived quality ("heft")

Chemical resist.  Cleaning products, solvents        Exposure tests
                  Medical/food contact compatibility

Color capability  Whether can achieve desired color  Pigment compatibility
                  UV stability of color over time

Cost per kg       Direct manufacturing cost          Market price
```

### Material Families: Industrial Design Choices

**Polymers (plastics):**

```
POLYMER SELECTION FOR INDUSTRIAL DESIGN

ABS (Acrylonitrile Butadiene Styrene):
  -- Properties: impact-resistant, machinable, paintable
  -- Processing: injection molding, vacuum forming, machining
  -- Design use: consumer electronics housings (classic choice)
  -- Apple used: early Macs (Bondi blue iMac G3)
  -- Limitation: UV yellowing; not suitable for outdoor long-term

PC (Polycarbonate):
  -- Properties: high impact strength, transparent options, heat resistant
  -- Processing: injection molding; difficult to machine
  -- Design use: lenses, screens, transparent panels, safety equipment
  -- Apple: MacBook polycarbonate unibody (2009)
  -- Limitation: stress cracking in contact with solvents

PC/ABS blend:
  -- Best of both: impact strength (ABS) + heat/warp resistance (PC)
  -- Most common material for complex housing assemblies
  -- Used heavily in automotive interior trim

Polypropylene (PP):
  -- Properties: flexible, chemical resistant, living hinges
  -- Living hinge: can flex millions of times without breaking
  -- Design use: containers, caps, flexible snap-fit parts
  -- Cost: very low; recyclable; food-safe grades

PETG:
  -- Properties: transparent, tough, easier to print than PC
  -- Processing: 3D printing (prototyping); injection molding
  -- Design use: transparent prototypes; packaging

TPE/TPU (thermoplastic elastomers):
  -- Properties: rubber-like; soft touch; co-moldable with rigid plastics
  -- Design use: grips, seals, overmolds on hard housings
  -- iPhone rubber bumper cases: TPU
```

**Metals:**

```
METAL SELECTION FOR INDUSTRIAL DESIGN

ALUMINUM:
  -- Properties: light (2.7 g/cm3), corrosion resistant, machinable
  -- Processing: die casting, CNC machining, extrusion, sheet metal
  -- Design use: premium consumer electronics (MacBook unibody)
  -- Apple unibody process: CNC milled from solid billet (wasteful but beautiful)
  -- Anodizing: creates hard, colorable oxide layer (the Apple color family)
  -- ALLOYS:
    6061-T6: structural (machined parts, extrusions)
    7075-T6: stronger, aerospace-grade (premium devices)
    5052: sheet metal (formable)

STAINLESS STEEL:
  -- Properties: very hard, corrosion resistant, heavy (8.0 g/cm3)
  -- Design use: watch cases, surgical instruments, premium kitchen tools
  -- Apple Watch: Stainless Steel model (heavier, more scratch-resistant than Al)
  -- PVD coating: physical vapor deposition of hard metal coatings (black, gold)

MAGNESIUM:
  -- Properties: lightest structural metal (1.74 g/cm3); die castable
  -- Design use: laptop chassis behind the screen; camera bodies
  -- Limitation: poor surface quality; usually coated/painted; flammable
  -- Thinkpad, Dell Latitude: magnesium for thin, light structural elements

TITANIUM:
  -- Properties: strongest/lightest metal for structural use; biocompatible
  -- Density: 4.5 g/cm3 (between aluminum and steel)
  -- Cost: very high; difficult to machine
  -- Design use: premium watches, medical implants, aerospace
  -- Apple Watch Ultra: Grade 5 titanium case
```

**Glass and Ceramics:**

```
GLASS IN CONSUMER PRODUCTS

Corning Gorilla Glass (aluminosilicate glass):
  -- Ion exchange process: surface compression layer
  -- Much harder/tougher than standard glass
  -- Versions 1 (2007) through 7 (2022+): increasing strength
  -- Current: 4x harder than soda-lime glass
  -- Used: all major smartphone screens

Sapphire (aluminum oxide single crystal):
  -- Hardness: 9 on Mohs scale (diamond = 10)
  -- Extremely scratch-resistant; expensive
  -- Apple Watch sapphire option; camera lens covers
  -- Limitation: harder = more brittle (doesn't absorb impact well)
  -- Drop test: Gorilla Glass often beats sapphire despite lower hardness

Ceramic (ZrO2, zirconia):
  -- Properties: very hard, biocompatible, can be made white or black
  -- Design use: Apple Watch Hermès ceramic case; high-end watches
  -- More scratch-resistant than metal; less shock-resistant
  -- Process: sintering (high-temp powder consolidation)
```

---

## Manufacturing Processes: The Designer's Constraint Map

### Injection Molding

The dominant process for plastic consumer products:

```
INJECTION MOLDING: HOW IT WORKS

PROCESS:
  1. Plastic pellets melted in heated barrel (200-300°C)
  2. Screw pushes molten plastic into closed mold
  3. Mold chilled; plastic solidifies (seconds to minutes)
  4. Mold opens; part ejected
  5. Repeat: cycle time 15 seconds to 5 minutes

ECONOMIC MODEL:
  Mold cost: $5,000 (simple) to $500,000 (complex)
  Part cost: $0.05 (simple, large volume) to $50 (complex, small volume)
  Break-even: typically 10,000-100,000 units before mold cost amortized
  Volume sweet spot: 10,000+ units per year

DESIGN RULES:
  1. DRAFT ANGLES:
     Walls must taper 1-3 degrees (helps part release from mold)
     No vertical walls (locked in mold)

  2. UNIFORM WALL THICKNESS:
     Thick sections cool slower -> sink marks on surface
     Target: 1.5-3mm wall thickness; avoid thick bosses
     Use ribs (thin fins) instead of solid thick sections for stiffness

  3. NO UNDERCUTS (or use slides):
     An undercut is a feature that prevents part from sliding out of mold
     Options: design to avoid; add side action (costly); use collapsible core

  4. PARTING LINE:
     Where the two mold halves meet; always visible as a seam
     Design locations the parting line will appear; make it a feature

  5. GATE AND RUNNERS:
     Where plastic enters: small mark always visible
     Locate gate in hidden area or design gate scar into feature

  6. MINIMUM FEATURE SIZE:
     Text: minimum 0.5mm depth; prefer 0.8mm
     Holes: minimum 0.8mm; prefer 1.5mm
     Walls: minimum 0.6mm; prefer 1.2mm+
```

### CNC Machining

```
CNC MACHINING (Computer Numerical Control)

PROCESS:
  Computer-controlled cutting tools remove material from solid billet
  Multi-axis mills (3, 4, 5 axis): 3 translational + rotational axes
  Tolerances achievable: ±0.01mm (vs ±0.2mm for injection molding)

ECONOMIC MODEL:
  No tooling cost (no mold)
  Part cost: $10 (simple) to $5,000 (complex)
  Volume sweet spot: 1-5,000 parts (before injection molding wins on cost)

APPLE'S USE OF CNC:
  MacBook unibody: entire top case from single aluminum billet
  Process: 6+ separate CNC operations; takes ~0.5 hours per part
  Cost: ~$10-20 in machining per laptop top case
  Benefit: perfect surface quality; impossible to achieve by any other means
  The aesthetic of seamlessness is manufactured by machining, not molding.

DESIGN CONSIDERATIONS:
  -- All machined features require tool access (no internal cavities)
  -- Threads: must be specified precisely for tap size
  -- Surface finish: achievable from Ra 0.4 (mirror) to Ra 6.3 (rough)
  -- Cannot create internal features without assembly
```

### Sheet Metal

```
SHEET METAL PROCESSES

STAMPING (press forming):
  Punch + die; blanks formed in single stroke
  Very high speed (300-1000 parts/minute for simple parts)
  Mold cost: $50,000-500,000 for production dies
  Part cost: <$1 at volume
  Design use: appliance panels, structural brackets

LASER CUTTING:
  CNC-controlled laser cuts flat sheet
  No tooling cost (programmed)
  Cost-effective for prototype and low volume
  Cannot form 3D features (flat profiles only; bend afterward)

BENDING (press brake):
  Sheet bent to angles; typical minimum bend radius = sheet thickness
  Design rule: holes near bends distort; keep holes 3x thickness from bend

DEEP DRAWING:
  Sheet stretched over punch into bowl/cup shapes
  Aluminum cans: 2-piece drawn construction
  Design use: recessed panels, cups, enclosures
```

### 3D Printing / Additive Manufacturing

```
3D PRINTING PROCESSES COMPARISON

PROCESS         MATERIAL      ACCURACY    SURFACE    USE IN DESIGN
--------------+-------------+-----------+-----------+------------------
FDM            Thermoplastics  Low       Visible     Early concept
(Fused Dep.)   (PLA, ABS, PETG) ±0.5mm  layer lines  models

SLA            Photopolymer    High      Smooth      Appearance models
(Stereolith.)  resin           ±0.1mm   (post-cure)  fine detail test

SLS            Nylon, PA       Medium    Slightly    Functional parts;
(Selective     powder          ±0.2mm   rough       small mechanisms
Laser Sint.)

MJF            PA12 nylon      High      Smooth      Production-grade
(Multi Jet     (HP process)    ±0.1mm                small volumes
Fusion)

DMLS/SLM       Metal powder    High      Rough pre-  Production metal
(Metal SLS)    (Ti, SS, Al)    ±0.1mm   finish      < 100 parts

DESIGN FOR ADDITIVE:
  -- Overhangs > 45 degrees require support (FDM/SLA)
  -- No mold cost; no draft angles required
  -- Internal geometries possible (lattices, internal channels)
  -- Anisotropic: strength varies by print direction
  -- NOT for mass production (cost per part too high)
```

---

## Surface Finishing: Where Aesthetics Meet Manufacturing

```
SURFACE FINISH OPTIONS

PROCESS              MATERIALS     EFFECT              DESIGN USE
-------------------+-------------+-------------------+-----------------
ANODIZING          Aluminum      Hard colored oxide   Consumer electronics
                                 layer; 5-20 micron   Space Gray, Gold,
                                 thickness            Silver on Apple

PAINTING           Any solid     Any color; texture   Automotive; appliances
                   substrate     options (matte/gloss/ Consumer electronics
                                 texture)             (PC era Thinkpads)

POWDER COATING     Metal         Tough, durable;      Industrial; furniture;
                                 textured options     outdoor equipment

PLATING            Metal or      Thin metal layer     Watch bezels; jewelry;
(electroplating)   plateable     (chrome, nickel,     connector contacts
                   plastic       gold, silver)

PVD COATING        Metal         Very hard thin film   Watch cases (DLC =
(Physical Vapor    (and some      (black, rainbow,     diamond-like carbon);
Deposition)        plastics)      gold effects)        Apple Watch Ultra

BRUSHING           Aluminum,     Directional texture   Apple product sides;
                   stainless     (satin finish)        architectural

POLISHING          Metal         Mirror finish         Watch cases;
                                                       medical devices

IN-MOLD DECORATION Plastic       Pattern/texture       Automotive interior;
(IMD)                            trapped under         consumer electronics
                                 plastic surface       textured surfaces

TEXTURE (mold)     Plastic       Mold surface texture  Tool grip surfaces;
                   injection     transferred directly   anti-fingerprint
```

---

## Design for Assembly (DFA)

```
DFA PRINCIPLES

GOAL: Minimize assembly cost, time, and error potential

PRINCIPLES:
1. MINIMIZE PART COUNT:
   Each part added = more assembly steps, more tolerance stack-up,
   more failure points, more inventory
   Ask: can this part be integrated into an adjacent part?

2. DESIGN FOR TOP-DOWN ASSEMBLY:
   All parts should assemble from above (Z-axis insertion)
   Lateral insertion requires fixtures; increases cost/error

3. SNAP FITS > SCREWS (when possible):
   No tools needed; faster; no lost screws
   But: lower holding force; less adjustable/repairable

4. MISTAKE-PROOFING (poka-yoke):
   Design parts that can only go in one way
   Asymmetric shapes; color coding; geometric constraints
   USB-A example failure: 50% chance of wrong orientation
   USB-C success: fully symmetric

5. TOLERANCE STACK-UP MANAGEMENT:
   Each part has dimensional variation (±tolerance)
   Stacked assembly: tolerances add
   At 5 parts with ±0.2mm each: final variation = ±1.0mm
   Critical dimensions: reduce intermediate parts in chain

6. SERVICEABILITY:
   Can it be disassembled for repair?
   Right-to-repair tension: seamless aesthetic vs replaceable battery
   EU Right to Repair Directive (2023): requires spare parts for 10 years
```

---

## Decision Cheat Sheet

| Design requirement | Material/process choice |
|-------------------|-----------------------|
| Low cost at high volume (>100K units) | Injection molded plastic |
| Premium appearance; one-piece | CNC machined aluminum |
| Transparent panel | PC injection molding or glass |
| Soft touch grip area | TPE overmold |
| Prototype; fast; any geometry | SLA or MJF 3D printing |
| Outdoor durability; colorfast | Powder-coated steel or anodized aluminum |
| Extreme scratch resistance (display) | Gorilla Glass or sapphire |
| Light, structural chassis | Die cast magnesium |
| Biocompatibility required | Medical-grade PP, PETG, titanium |
| Recycle at end of life | Mono-material design; marked recyclables |

---

## Common Confusion Points

**"Seamless" products are assembled, not grown.**
The iPhone looks seamless because every seam is precisely designed and located. The glass-metal interface has tolerance of ±0.05mm. This is not "no seams" -- it is seams so precisely designed and executed that they are invisible. Seamlessness is a manufacturing achievement, not the absence of manufacturing.

**Draft angle is not optional in injection molding.**
Without draft, the part cannot be ejected from the mold without surface damage. This means vertical walls are physically impossible in standard injection molding. Every "vertical wall" in a plastic product has some degree of draft -- typically 1-3 degrees, which is often invisible but always present.

**3D printing cannot replace injection molding for high-volume production.**
The cost crossover between additive and injection-molded parts is approximately 100-1,000 units depending on complexity. Above that volume, the amortized tooling cost of injection molding makes it cheaper per unit. The industries are complementary: additive for prototype and low volume, injection molding for mass production.

**Material cost is a small fraction of product cost.**
The aluminum billet for a MacBook top case costs ~$3. The machining, anodizing, and finishing costs ~$30-50. The material is 5-10% of the component cost. This is why exotic materials (titanium, sapphire, ceramics) are accessible in premium products: the material premium is smaller than it appears in the context of total manufacturing cost.

**Tolerances are not free.**
Every ±0.01mm improvement in tolerance specification roughly doubles the manufacturing cost for that dimension. Tight tolerances require: slower processes, more inspection, more scrap, specialized tooling. The designer's job is to specify the tolerance that is required for function -- not tighter.
