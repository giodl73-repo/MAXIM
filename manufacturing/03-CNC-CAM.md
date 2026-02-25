# CNC Machining and CAM Programming

## The Big Picture

CNC (Computer Numerical Control) replaces manual machine operation with programmed axis motion. The workflow: CAD model → CAM software generates toolpaths → post-processor outputs G-code → CNC controller executes motions.

```
WORKFLOW: DESIGN TO CHIP
──────────────────────────────────────────────────────────────────
┌──────────┐    ┌──────────┐    ┌───────────┐    ┌──────────────┐
│  CAD     │    │  CAM     │    │  Post     │    │  CNC         │
│  Model   │───►│  Software│───►│ Processor │───►│  Controller  │
│          │    │          │    │           │    │              │
│ SolidWks │    │ Mastercam│    │ Haas.pst  │    │ G-code runs  │
│ CATIA    │    │ HSMWorks │    │ Fanuc.pst │    │ axes move    │
│ NX       │    │ NX CAM   │    │ Siemens   │    │ part made    │
└──────────┘    └──────────┘    └───────────┘    └──────────────┘
                     │
                Toolpath = cutter center path + cutting conditions
                (feed rate, spindle speed, depth, strategy)
```

**Bridge**: CAM is analogous to a compiler. The CAD model = source code. The CAM toolpath = IR (intermediate representation). The G-code = machine code. The post-processor = target-specific backend. The CNC controller = CPU executing instructions.

---

## CNC Coordinate Systems

### Machine Coordinate System

```
STANDARD AXIS ORIENTATION (Right-Hand Rule)
──────────────────────────────────────────────────────────────────

VMC (Vertical Machining Center):
         +Z (spindle up)
          │
          │
          └────── +X (right looking at machine)
         /
        / +Y (toward machine column = away from operator)

        Right-hand rule: curl fingers X→Y, thumb points +Z

HMC (Horizontal Machining Center):
  +Z = spindle axis (horizontal, toward table)
  +X = left/right
  +Y = up

Lathe:
  +Z = along spindle axis (+ = toward tailstock)
  +X = radial (+ = away from center)
```

### Work Coordinate Systems (WCS)

```
Multiple WCS allow programming relative to part, not machine home.

G54 = Work offset 1  (primary part datum)
G55 = Work offset 2  (second part or second datum)
G56–G59 = more offsets

Machine home (G28 = reference) is fixed.
Work offset G54 = distance from machine home to your part datum.
All program coordinates are relative to G54.

Multi-fixture setup:
┌────────────────────────────────────────────────────────┐
│  Machine Table                                         │
│  ┌────────┐         ┌────────┐         ┌────────┐     │
│  │ Part 1 │G54      │ Part 2 │G55      │ Part 3 │G56  │
│  │        │         │        │         │        │     │
│  └────────┘         └────────┘         └────────┘     │
│  Machine home ◄─────────────────────────────────────  │
└────────────────────────────────────────────────────────┘
```

---

## G-Code Reference

### Core Modal Codes (Machine State)

```
MOTION MODES (modal — stay active until changed)
  G00  Rapid positioning       (max machine speed, no cutting)
  G01  Linear interpolation    (cutting, specified feed rate)
  G02  Circular arc CW         (in current plane)
  G03  Circular arc CCW
  G04  Dwell (pause)           P = milliseconds or seconds

PLANE SELECTION
  G17  XY plane  (default on VMC for arcs and canned cycles)
  G18  XZ plane
  G19  YZ plane

COORDINATE SYSTEM
  G20  Inch mode
  G21  Metric mode
  G54–G59  Work offsets
  G90  Absolute coordinates    (relative to work origin)
  G91  Incremental coordinates (relative to last position)
  G92  Set current position as work origin (use sparingly)

TOOL LENGTH COMPENSATION
  G43  Apply TLC, H word = offset register
  G44  Negative TLC
  G49  Cancel TLC

CUTTER RADIUS COMPENSATION
  G41  Left offset (climb milling outer profile)
  G42  Right offset
  G40  Cancel CRC

UNITS / SPEED
  G94  Feed per minute (in/min or mm/min)
  G95  Feed per revolution (in/rev or mm/rev) — turning
  G96  Constant surface speed (SFM or m/min) — turning
  G97  Constant RPM

RETURN / HOME
  G28  Return to machine home (through intermediate point)
  G29  Return from reference
```

### Canned Cycles (Fixed Cycles)

```
G81  Drill               Simple drill cycle, no peck
G82  Drill + dwell       Spot drill, countersink
G83  Peck drill          Deep hole, pecks to clear chips
G84  Tap               Rigid tapping (synchronizes spindle/feed)
G85  Bore               Bore in, feed out
G86  Bore + stop         Bore in, orient, rapid out (leave drag line)
G87  Back bore           Bore going up (from underside)
G89  Bore + dwell        Bore in, dwell, feed out

Format example (G83 peck drill):
  G83 X1.000 Y1.000 Z-1.500 R0.100 Q0.200 F5.0
       │      │      │       │      │      │
       X pos  Y pos  depth   R plane peck   feed
```

### M Codes (Miscellaneous Functions)

```
M00  Program stop (operator must restart)
M01  Optional stop (only if "optional stop" active on control)
M02  End of program
M03  Spindle on CW (mill: looking down at tool)
M04  Spindle on CCW
M05  Spindle stop
M06  Tool change (ATC — automatic tool changer)
M07  Coolant mist on
M08  Flood coolant on
M09  Coolant off
M30  End of program + rewind
M98  Call subprogram
M99  Return from subprogram
```

---

## CAM Strategies

### 2D Operations

```
CONTOUR (2D profiling)
  Tool follows part outline at full depth or step-down passes
  Left/right offset (G41/G42) maintains programmed surface
  Lead-in/lead-out arcs prevent entrance/exit marks

POCKET (2D pocket clearing)
  Strategies: raster, offset/spiral, trochoidal
  Trochoidal (dynamic milling): small radial engagement,
    full axial depth, high material removal, less heat

FACE MILLING
  Large-diameter face mill, passes across top of part
  Overlap ~40–50% for even finish

DRILLING / TAPPING
  Drill cycles (G83 for deep holes)
  Rigid tap requires synchronized spindle-feed
```

### 3D Operations

```
PARALLEL (RASTER) FINISH
  Back-and-forth passes at constant Z or projected
  Best for: shallow surfaces, large flat-ish areas
  Stepover = scallop height tradeoff

SCALLOP / CONSTANT Z
  Contour passes at constant Z level
  Best for: steep walls, complex profiles
  Leaves ridges at flatter areas

PENCIL (PENCIL MILLING)
  Small tool traces into corners, finds concave edges
  Final cleanup pass

HORIZONTAL AREA CLEAR
  Semi-finish: removes most stock
  Leaves uniform stock for finish pass

ADAPTIVE / DYNAMIC (3D Trochoidal)
  Maintains constant chip load in 3D
  Mastercam Hybrid, Fusion 360 Adaptive, HSM Adaptive
  Best for: titanium, Inconel, hardened steel roughing
```

### 5-Axis Strategies

```
3+2 (POSITIONAL 5-AXIS)
  3 linear axes move while 2 rotary are fixed at an angle
  Access undercuts and compound angles
  Common for: indexing operations, multiple faces
  Most machine time is still 3-axis

SIMULTANEOUS 5-AXIS
  All 5 axes move at once
  Required for: impellers, blisks, turbine airfoils
  Complex toolpath calculation, longer programming time
  Difficult collision avoidance (tool, holder, fixture)
```

---

## Tool Path Parameters

### Speed and Feed Calculation

```
STARTING POINT: Lookup recommended SFM for tool/material pair
  (from manufacturer's speeds and feeds chart)

Step 1: RPM = (SFM × 12) / (π × D_tool)     [inch]
        RPM = (m/min × 1000) / (π × D_tool)  [metric]

Step 2: Feed rate = RPM × chip_load × number_of_teeth
        Feed (in/min) = N × fz × Nt

Example: 0.500" 4-flute carbide end mill in 6061 aluminum
  Recommended: 600 SFM, chip load 0.003 in/tooth
  RPM = (600 × 12) / (π × 0.5) = 7200 / 1.571 = 4584 rpm
  Feed = 4584 × 0.003 × 4 = 55 in/min
  Axial depth: up to 2×D = 1.000"
  Radial depth (finishing): 0.050–0.100"
  Radial depth (roughing dynamic): 0.050" (but full depth Ap)
```

### Depth and Width of Cut

```
AXIAL DEPTH (Ap):
  Roughing: 1×D to 2×D (conventional slotting)
  Dynamic/trochoidal: 2×D to 4×D (reduced radial engagement)
  Finishing: 0.010–0.030" (light passes for surface quality)

RADIAL ENGAGEMENT (Ae):
  Slotting: 100% = 1×D (highest load)
  Roughing: 50–75% (conventional profiling)
  Dynamic: 5–15% (high-efficiency toolpaths)
  Finishing: 5–20% (to achieve target Ra)

Chip thinning: when Ae < 50% D, actual chip thickness
  t_actual = fz × √(Ae / D)
  CAM compensates by increasing programmed feed.
```

---

## CNC Controller Fundamentals

### Fanuc (Most Common)

```
FANUC 0i / 30i — dominant in VMCs, HMCs, lathes
Block format: N___ G__ X__ Y__ Z__ F__ S__ T__ M__

Program structure:
%                    (start of tape)
O1001                (program number)
(PROGRAM COMMENT)
G20 G17 G40 G49 G80  (safety cancels: inch, XY, no CRC, no TLC, no cycle)
G90 G94              (absolute, feed/min)
T01 M06              (tool change: tool 1)
G43 H01 Z10.0 M03 S3000  (activate tool length, move Z safe, spindle on CW)
G54                  (activate work offset 1)
...                  (machining)
M09                  (coolant off)
G28 Z0               (return Z to machine home)
M30                  (end program, rewind)
%                    (end of tape)
```

### Haas (Common in Job Shops, US)

Haas uses Fanuc-compatible G-code but adds many proprietary macros and functions (macro B, probing cycles). Conversational programming (Intuitive Machining) for simple operations.

### Siemens Sinumerik

Common in European machines and aerospace (DMG Mori). Cycle structure differs from Fanuc. CYCLE81 instead of G81. More powerful macro language (APT-like).

---

## Toolholding and Setup

```
TOOLHOLDER TYPES (affects rigidity and accuracy)
──────────────────────────────────────────────────────────────────
R8 collet        Manual mills, Bridgeports
CAT40/BT40       Standard production machining (40-taper = medium)
CAT50/BT50       Heavy roughing, large machines
HSK-A63          High-speed (hollow-shank taper, face contact)
                 Better accuracy, higher RPM (>20K)
Shrink fit       Zero-runout, no moving parts, requires heater
Hydraulic chuck  Good balance between rigidity and tool change time
ER collet chuck  General purpose, wide size range

RUNOUT MATTERS:
  ±0.001" TIR (total indicator reading) = poor
  ±0.0005" TIR = acceptable
  ±0.0001" TIR = premium holders needed for finish work
  Runout doubles surface roughness and halves tool life
```

---

## Workholding

```
WORKHOLDING OPTIONS
──────────────────────────────────────────────────────────────────
Machine vise        Most common, accurate, fast setup
                    Step jaws for thin parts
                    Machinable soft jaws for complex profiles

Fixture plate       Modular, T-slots or Uniforce
                    Multiple parts per setup

Vacuum chuck        Sheet/slab work, zero-mark fixturing
                    Aluminum plate, printed circuit boards

Toe clamps          When vise can't reach, manual setup
                    Always down-force, never sideways

Kurt vise           Industry standard, 6" jaw width
                    Parallels for consistent Z height
                    Pull-down feature eliminates jaw lift
```

---

## Probing and Automatic Tool Setting

```
WORKPIECE PROBING (Renishaw RMP60 / OMP60):
  CNC program runs probe routine
  Probe touches part surfaces
  Automatically sets work offsets (G54)
  Eliminates manual edge-finding (reduces setup time)

TOOL LENGTH MEASUREMENT (TLS):
  Probe on table
  Tool runs into probe → measures actual Z length
  Updates H register (G43)
  Eliminates manual tool length measurement

IN-PROCESS GAUGING:
  Measure feature after machining while in machine
  Automatically adjust offsets for next pass
  Closes loop between machining and inspection
  Expensive but reduces CMM time, catches drift early
```

---

## Decision Cheat Sheet

| I need to... | Approach |
|--------------|----------|
| Machine simple 2D profiles | 3-axis VMC, 2D contour toolpaths |
| Machine 3D surfaces | 3+2 or simultaneous 5-axis |
| Minimize setups for a complex part | Turn-mill or 5-axis, B-axis live |
| High-volume production | HMC with palletized tombstones |
| Deep pockets in hard material | Dynamic/trochoidal toolpaths |
| Thread an existing hole (tapping) | Rigid tap (G84), sync spindle/feed |
| Generate G-code from CAD model | CAM software (Fusion 360, Mastercam) |
| Set work offset accurately | Probing routine (edge finding) |
| Compensate for worn tool | Cutter radius compensation G41/G42 |
| Machine titanium efficiently | Adaptive clearing, CBN tools, MQL |

---

## Common Confusion Points

**G90 vs G91 confusion**: Most programs run in G90 (absolute) for safety. G91 incremental is useful for drilling patterns (repeat offsets) and homing moves. Mixing them accidentally in the same block causes crashes.

**TLC sign**: G43 (+ offset) is standard. If the measured tool length is 5.237", H01 = 5.237. The controller adds this to Z positions. If the sign is wrong, the tool crashes into the part or misses it by twice the tool length. Always verify first cut is in air.

**Post-processor mismatch**: CAM output is generic. Post-processor converts to machine-specific syntax. Using the wrong post (Haas post on a Fanuc control) usually produces invalid code — some features silently drop, others crash. Every machine model may need a tuned post.

**Feed rate in rapids**: G00 ignores F word — always moves at maximum rapid rate. Never program a cutting move with G00. G01 at an appropriate F is always required for material removal.

**Cutter compensation and the "lead-in" requirement**: G41/G42 must be activated on a non-cutting move (typically a linear move into the part). You cannot activate CRC while already in contact — the control cannot compute compensation without the "look-ahead" block. Always program lead-in arcs.
