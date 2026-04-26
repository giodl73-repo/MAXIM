# Watchmaking — 09 Movement Anatomy
## The Complete Technical Tour: Mainspring to Balance Wheel

---

## The Big Picture

A mechanical watch movement is a miniature machine that converts 40–70 hours of stored elastic energy into ~1,400,000 regulated pulses per day (at 28,800 vph), maintaining 20–50 µm tolerances over a 50+ year service life, in a package roughly 30 mm in diameter and 3–5 mm thick. The gear train is a ~14,000:1 ratio reduction from the barrel to the escape wheel.

```
ENERGY FLOW: MAINSPRING TO HANDS

┌──────────────────────────────────────────────────────────────────────┐
│  POWER STORAGE     POWER DELIVERY     TIMEKEEPING     DISPLAY        │
│                                                                      │
│  ┌──────────┐     ┌─────────────────────────────────┐  ┌──────────┐  │
│  │Mainspring│     │     GOING TRAIN (gear train)     │  │  HANDS   │ │
│  │(coiled   │──►──│                                 │──►│          │ │
│  │ steel    │     │ Barrel → Center → Third →       │  │ Hours    │ │
│  │ strip)   │     │ Fourth → Escape wheel           │  │ Minutes  │ │
│  │          │     │                                 │  │ Seconds  │ │
│  │ ~48 hrs  │     │ Ratio: ~14,400:1                │  └──────────┘ │
│  │ reserve  │     │ (barrel to escape wheel)        │               │
│  └──────────┘     └─────────────────────────────────┘               │
│       │                         │                                    │
│       │                         ▼                                    │
│       │              ┌──────────────────────┐                       │
│       │              │   ESCAPEMENT         │                       │
│       │              │   Lever + escape wheel│                      │
│       │              │   Controls energy    │                       │
│       │              │   release            │                       │
│       │              └──────────────────────┘                       │
│       │                         │                                    │
│       │              ┌──────────────────────┐                       │
│       │              │   REGULATOR          │                       │
│       │              │   Balance wheel      │                       │
│       │              │   + hairspring       │                       │
│       │              │   Sets the tempo     │                       │
│       │              └──────────────────────┘                       │
│       │                                                              │
│  ┌────┴──────┐                                                       │
│  │KEYLESS    │   (winding + setting mechanism)                       │
│  │WORKS      │                                                       │
│  └───────────┘                                                       │
└──────────────────────────────────────────────────────────────────────┘
```

---

## Power Storage: Mainspring and Barrel

### Mainspring

The mainspring is a coiled strip of hardened spring steel (or Nivarox alloy — see Materials section) stored in a cylindrical container called the barrel.

```
MAINSPRING CROSS-SECTION

Fully wound state:             Mid-wind state:        Nearly run-down:
┌──────────────────────┐      ┌──────────────────────┐  ┌──────────────────────┐
│ ██████████████████   │      │    ████████████      │  │         ████         │
│ ████████████████     │      │   ██████████         │  │        ████          │
│ ██████████████       │      │  ████████            │  │       ████           │
│ ████████████         │      │ ██████               │  │      ████            │
│ outer edge           │      │                      │  │                      │
│ (arbor end)          │      │                      │  │                      │
└──────────────────────┘      └──────────────────────┘  └──────────────────────┘

  Torque: HIGH                  Torque: MEDIUM              Torque: LOW
  (most coils under tension)    (partially spent)           (few coils engaged)

Typical torque ratio: 2.5–4× difference between fully wound and run-down
This torque variation → rate variation in the going train (faster when wound)
Mitigated by: fusee (historical), barrel slippage (modern), constant force mechanisms
```

**Dimensions (typical ladies' watch):**
- Length: 250–350 mm uncoiled
- Width (height): 1.0–1.4 mm
- Thickness: 0.1–0.15 mm

**Materials evolution:**

```
MAINSPRING MATERIALS

Plain carbon steel (pre-1900s):
  Strength: moderate; brittle fracture common
  Magnetic: yes → rate affected by magnetic fields
  Corrosion: rust in humidity

Carbon steel + bluing (heat treatment):
  Oxidation layer slightly improves corrosion resistance
  Still magnetic; fracture risk

Elinvar (1920s, Guillaume):
  Ni-Cr-Fe alloy; ELINVAR = ELastic INVARiant
  Elasticity nearly constant with temperature
  Still magnetic

Nivarox (1933, Reinhard Straumann; NIVeau + regARX):
  Base: Fe-Ni-Cr with Be, Ti, Mn, Si additions
  Key properties:
    - Low temperature coefficient of elasticity: ±2 ppm/°C
      (brass spring: ±100 ppm/°C)
    - Non-magnetic (below saturation field)
    - Good corrosion resistance
    - No lubrication required on spring
    - Will not rust
  Nivarox SA (subsidiary of Swatch Group since 1983):
    Manufactures ~90% of world's precision hairsprings
    Also makes balance springs, lever springs, click springs
    Significant market power within Swiss watch supply chain
```

### Barrel

The barrel is a cylindrical container with an outer toothed rim that functions as the first wheel of the going train.

```
BARREL ANATOMY

      barrel lid (covers mainspring)
         ┌─────────────────────────────┐
        /│  toothed outer rim           │\
       / │  (= first wheel of train)    │ \
      │  │                              │  │
      │  │   ████████ mainspring ██████ │  │
      │  │                              │  │
      │  │       arbor (central shaft)  │  │
       \ │       (= ratchet wheel axle) │ /
        \│                              │/
         └─────────────────────────────┘
                        │
                    barrel arbor
                        │
              to ratchet wheel + click spring
              (prevents unwinding; ratchet)

POWER RESERVE:
  Fully wound: ~48 hours for most modern Swiss watches
  Actually usable: manufacturers typically claim the period while
  maintaining accuracy specifications — often 80% of total spring travel.
  A watch with 48h power reserve may be "out of spec" after 40h.
```

**Click and click spring:** The ratchet wheel (on the barrel arbor) is engaged by a click (pawl) under spring tension. This prevents the barrel from reversing when winding force is removed — the same mechanism as a ratchet wrench. Without the click, the mainspring would unwind whenever you stopped winding.

**Barrel slippage (bridle):** The innermost coil of the mainspring is attached to the barrel arbor by a "bridle" — a friction-fitted clip rather than a rigid connection. When the mainspring is fully wound, further winding force causes the inner coil to slip on the arbor. This prevents overwinding and breakage. It also has a beneficial secondary effect: in the "fully wound" zone, the spring is at its minimum-torque-variation region because slipping prevents storing more energy. Result: less torque variation delivered to the going train near full wind.

---

## The Going Train: Gear Ratios

The going train is the gear reduction chain from the barrel to the escape wheel. It reduces the barrel's slow rotation (~one revolution per 8 hours in a 48h movement) to the escape wheel's rapid stepping (~6–10 Hz).

```
GOING TRAIN — TYPICAL RATIOS (28,800 vph = 8 Hz movement)

WHEEL          TEETH   PINION   RATIO    PERIOD
─────────────────────────────────────────────────────────────────
Barrel         80 teeth                 ~8 hours/revolution
Center wheel   80/7.5 pinion  8h/1h    1 revolution/hour → MINUTE HAND
(= 2nd wheel)  80 teeth on wheel         (center wheel drives minute hand)

Third wheel    80/10 pinion   60min/4min  1 revolution/4 minutes
               80 teeth on wheel

Fourth wheel   80/10 pinion   4min/4sec   1 revolution/4 seconds... wait:
               80 teeth                   actually:
               If 4th wheel → one revolution per minute:
                 that drives the SECONDS HAND (center seconds watches)
                 or sub-seconds register at 6 o'clock

Escape wheel   15/7 pinion    ...
               15 teeth

Total ratio from barrel to escape wheel: approximately 14,400:1 to 16,000:1

GEAR TRAIN CALCULATION (28,800 vph = 4 Hz balance):

  Step 1: Balance oscillates at 4 Hz → 8 beats/sec
    Each beat advances escape wheel by 1 tooth.
    Escape wheel: 8 teeth advanced per second.

  Step 2: Escape wheel (21 teeth, ETA 2824-type):
    8 teeth/sec ÷ 21 teeth/rev = 0.381 rev/sec

  Step 3: Fourth wheel drives escape wheel pinion.
    Fourth wheel (60t) meshes with escape pinion (8t).
    Fourth wheel speed = 0.381 × (8/60) = 0.0508 rev/sec
    = 1 revolution per 19.7 seconds.

  Note: The fourth wheel carries the seconds hand
    ONLY when tooth counts are chosen to give exactly
    1 rev/60 sec. In the ETA 2824, the center wheel
    indirect seconds mechanism achieves 60-second
    rotation. Tooth counts vary by caliber — the
    illustrative numbers above show the principle,
    not a specific caliber's exact ratios.

  Step 4: Working backward from design targets:
    Center wheel: 1 rev/hour (carries minute hand)
    Third wheel: intermediate reduction
    Fourth wheel: 1 rev/min (if it carries seconds hand)
    Escape wheel: driven at 8 teeth/sec by balance
    Tooth counts are selected to hit these exact targets.
```

**Pinions:** The small driving gears (pinions) in the going train have far fewer teeth (6–10 typically) than the wheels they drive (60–100 teeth). This large ratio between wheel teeth and pinion leaves (teeth on pinion) provides the reduction. Pinion leaves are wider and more robust than wheel teeth.

---

## Jewel Bearings

The pivot points of every wheel and pinion in the going train rotate millions of times per day against bearing surfaces. Metal-on-metal at pivot points would wear rapidly and create inconsistent friction.

**Synthetic ruby bearings** replaced natural jewels around 1902 (Verneuil flame fusion process made synthetic sapphire/ruby cheap). Ruby (corundum, Al₂O₃) has:
- Hardness: 9 Mohs (diamond is 10; steel pivots ~7)
- Extremely smooth surface when polished
- Hydrophobic: doesn't absorb or wick oil (unlike metals)
- Low friction against polished steel pivots

```
JEWEL BEARING TYPES

CAP JEWEL (endstone):
  ──────── ◯ ────────── flat disk; pivot tip rests on its flat face
                        prevents axial movement ("end-shake" limited)

HOLE JEWEL (bushing):
  ──────── ⬬ ────────── cylindrical hole; pivot rotates inside
  The critical friction-reducing bearing

OIL RESERVOIR:
  Hole jewel + cap jewel combination creates
  a tiny enclosed space that holds lubricant:
  ┌────────────────────────────────┐
  │  cap jewel (flat)              │
  │  ─────────────────── ← oil     │
  │  hole jewel (cup-shaped)       │
  │  ──── ─ ─ ── ─ ──── pivot rotating inside
  └────────────────────────────────┘
  The cup shape of the hole jewel seat capillary-holds
  a tiny drop of watch oil (0.01–0.001 µL)
```

**Standard jewel count (17 jewels — a complete lever watch):**

```
JEWEL ALLOCATION — 17-JEWEL MOVEMENT

Escape wheel pivot (2 hole + 2 cap)     = 4 jewels
Lever pivot (2 hole + 2 cap)            = 4 jewels
Balance pivot (2 hole + 2 cap)          = 4 jewels
Fourth wheel pivot (2 hole)             = 2 jewels
Third wheel pivot (1 hole)              = 1 jewel
Center wheel pivot (1 hole)             = 1 jewel
Pallet stones (entry + exit)            = 2 jewels (actually these are friction pads,
                                           not bearings, but count as jewels)
Total:                                   = 17 jewels
                                           (standard since early 20th century)
```

Jewels above 17 cover additional bearing points (keyless works, date mechanism levers) or are purely decorative. The "jewel count as quality" marketing was exposed as misleading by the 1960s; the US FTC took regulatory action against fraudulent jewel count claims.

**Synthetic ruby manufacturing (Verneuil process, 1902):**
- Aluminum oxide powder + chromium oxide (for red color) melted in an oxyhydrogen flame
- Crystals grow downward on a pedestal
- Resulting boules (egg-shaped crystals) ~5 cm long, ~2 cm diameter
- Sliced, drilled (using laser drilling since ~1960s), ground, and polished
- Cost: ~$0.01–$0.05 per jewel at volume

---

## The Regulator: Balance Wheel and Hairspring

The balance wheel and hairspring together are the oscillator that determines the watch's rate. This is the most sensitive and critical assembly in the movement.

### Balance Wheel

```
BALANCE WHEEL GEOMETRY

Top view:
        ╭────────────────────────────╮
       /   rim (heavy; most mass here) \
      /  ┌─────────────────────────┐   \
     /   │   spokes (light)        │    \
    │    │    ┌───────────────┐    │ │
    │    │    │ hub/arbor     │    │     │
    │    │    └───────────────┘    │     │
     \   └─────────────────────────┘   /
      \                               /
       ╰────────────────────────────╯

Period of oscillation:
  T = 2π × √(I / k)
  where:
    I = moment of inertia of balance (kg⋅m²)
    k = stiffness of hairspring (N⋅m/rad)

  Frequency: f = (1/2π) × √(k/I)
  Common frequencies:
    18,000 vph = 5 bph = 2.5 Hz (older movements, 5 times per second)
    21,600 vph = 6 bph = 3 Hz (standard mid-century)
    28,800 vph = 8 bph = 4 Hz (modern standard; COSC tested)
    36,000 vph = 10 bph = 5 Hz (high-beat; Zenith El Primero, IWC Spitfire)
    72,000 vph = 20 bph = 10 Hz (Zenith Defy Lab; extreme)

  Why higher beat rate?
    - Each beat is shorter → less time for perturbation to act
    - But more beats → more oil consumption, more wear
    - Energy consumption scales as f³ (quadratic in frequency × beats/day)
    - Tradeoff: 28,800 vph is well-established sweet spot
```

The balance wheel is a torsional harmonic oscillator — structurally identical to an LC tank circuit: moment of inertia I maps to inductance L (stores kinetic energy), spring constant k maps to 1/C (stores potential energy). The frequency stability is limited by the temperature coefficients of I and k, which is why Nivarox and Glucydur exist: their dI/dT and dk/dT are chosen to cancel each other over the operating temperature range. This is the same design problem as a temperature-stable LC oscillator — use components whose temperature coefficients compensate.

**Balance wheel materials:** Brass (historical), monometallic copper-beryllium (for reduced temperature coefficient), Glucydur (copper-beryllium alloy, developed 1950s — near-zero temperature coefficient of inertia, non-magnetic).

### Hairspring (Balance Spring)

The hairspring is a flat coil of metal alloy attached at its inner end to the balance staff (arbor) and at its outer end to the regulator mechanism or a fixed stud.

```
HAIRSPRING PROFILES

Standard flat coil:
  ╭──────────────────────────╮
 /  ╭──────────────────────╮  \
│  /  ╭────────────────╮   \ │
│ │  /  ╭──────────╮   \    │  │
│ │     │  /   ╭────╮  \    │   │  │
│ │ │   │   center │   │  │   ││
│ │     │  \   ╰────╯  /    │   │  │
│ │  \  ╰──────────╯   /    │  │
│  \  ╰────────────────╯   /   │
 \  ╰──────────────────────╯  /
  ╰──────────────────────────╯
  stud (outer end fixed here)

Problem: as spring expands/contracts, its "breathing center"
doesn't coincide with the balance pivot → slightly elliptical motion
of the effective balance → isochronism error

Breguet overcoil:
  Same flat coil BUT the terminal outer coil is bent upward
  (out of the flat plane) and curves back over the coil:

  ──────────────────── terminal coil in different plane
       ╭──────────────────────────╮   ←
      /  ╭──────────────────────╮  \  ← "overcoil" bent upward here
     │  /  ╭────────────────╮   \     │
     ... (same flat inner portion) ...

  Result: more uniform "breathing" of the spring
  → better isochronism across amplitude range
  → used in higher-quality movements
  → Breguet's 1780s invention; still considered best practice
```

**Hairspring materials:**

```
HAIRSPRING MATERIALS EVOLUTION

Steel (18th–19th century):
  High temperature coefficient of elasticity (~100 ppm/°C)
  → spring softer in heat → clock runs slow in summer
  Magnetic → affected by magnetic fields

Elinvar (1920s):
  Temperature coefficient of elasticity: ±5 ppm/°C
  (20× better than steel)
  Slightly magnetic

Nivarox (1933–present):
  Temperature coefficient of elasticity: ±1–2 ppm/°C
  Non-magnetic (up to ~1,000 Gauss saturation field)
  Standard for all quality Swiss watches
  Nivarox SA (Swatch Group) dominates supply

Parachrom (Rolex, 2000):
  Nb-Zr alloy (niobium-zirconium, no nickel)
  Insensitive to magnetic fields to 2,000 Gauss
  Breguet overcoil; very stable

Silinvar/DRIE silicon (Patek Philippe, 2005; others since):
  Single-crystal silicon etched by Deep Reactive Ion Etching (DRIE)
  Temperature coefficient of elasticity: ±0.03 ppm/°C (30× better than Nivarox)
  Completely non-magnetic
  No lubrication needed at lever pallet-escape wheel interface
    (silicon has very low surface adhesion)
  Brittle (fractures rather than deforming; less shock-tolerant)
  Surface oxide layer (SiO₂) provides some wear protection
```

### Rate Regulation

How do you adjust the watch to run faster or slower?

```
TWO REGULATION METHODS

Method 1: INDEX REGULATION (traditional)
  Regulator plate with two curb pins that straddle the hairspring:
    ─┬─  ─┬─  curb pins
     │    │
  ───┼────┼───  hairspring coil (passes between the pins)
     │    │

  Moving the pins closer to the stud shortens the ACTIVE length of hairspring:
    → shorter active spring → stiffer → higher frequency → watch runs faster
  Moving pins toward center lengthens active spring:
    → longer → softer → lower frequency → runs slower

  Rate adjustment: ~+/-5 sec/day per tiny movement of index
  Disadvantage: friction between curb pins and spring introduces
    positional variability (hairspring binds slightly at pins)

Method 2: FREE-SPRUNG / ADJUSTED MASS (higher quality)
  Outer end of hairspring fixed rigidly to stud (no curb pins)
  Balance wheel has small adjustable "timing weights" (eccentric screws)
  Moving weights outward: increase moment of inertia → runs slower
  Moving weights inward: decrease moment of inertia → runs faster

  Advantages:
    - No friction on hairspring → better isochronism
    - Rate doesn't change when watch is serviced (no pin position to track)
    - Less sensitive to shock (no pins to be displaced)
  Used by: Patek Philippe, Rolex (Microstella screws), Audemars Piguet
```

---

## Shock Protection

Watch movements contain tiny jewel bearings (hole jewels as small as 0.2 mm diameter). A sharp shock can fracture the jewel or (more commonly) bend the delicate balance staff pivot (smallest pivot in the movement, ~0.07–0.1 mm diameter at the pivot tip).

**Incabloc (Swiss, 1934) and Kif Flector (Swiss, 1944):**

```
INCABLOC SHOCK PROTECTION

Without Incabloc:
  Balance pivot → hole jewel → rigid plate
  Shock → lateral force on pivot → SNAP (pivot breaks)

With Incabloc:
  Balance pivot → hole jewel → spring-loaded holder
                                      │
                               spring mount (lyre-shaped)
                               allows jewel to displace laterally
                               then spring returns it

  Under shock: jewel holder deflects, absorbs energy → pivot survives
  After shock: spring centers jewel and pivot back to original position

  The jewel assembly is:
  ┌─────────────────────────────────────────┐
  │ cap jewel  ← sits in spring-loaded nest │
  │ hole jewel ← same nest                  │
  │ spring (Incabloc shape):                │
  │   ╭────────────────╮ lyre shape         │
  │   │ slots for tab  │ catches on plate   │
  │   │ of hole jewel  │ protrusions        │
  │   ╰────────────────╯                    │
  └─────────────────────────────────────────┘

  Normal operating: float = ~0.05 mm (extremely tight tolerance)
  Shock displacement: up to ~0.3 mm before pivot contacts anything

ISO shock resistance standard: survive 5,000 g half-sine shock
  (simulates dropping on hard floor from 1 meter)
```

Nearly all modern wristwatch movements include some form of shock protection. Incabloc and Kif dominate; some in-house implementations (Rolex's Paraflex since 2012) are proprietary variations on the same principle.

---

## Keyless Works: Winding and Setting

The keyless works is the mechanism that converts crown rotation into winding (pushing mainspring) or time-setting (rotating hands).

```
KEYLESS WORKS — POSITIONS AND FLOW

Crown position 0 (fully pushed in — normal running):
  Crown rotation → winding pinion → ratchet wheel → barrel arbor
  → mainspring winds

           crown ──► crown wheel ──► ratchet wheel
                         (teeth engage winding pinion while crown position 0)
                                    (one-way: click allows winding not unwinding)

Crown position 1 (partially pulled out — date setting, if present):
  Crown rotation → stem → different engagement
  → date mechanism gears only

Crown position 2 (fully pulled out — time setting):
  Setting lever engages
  Stem drives setting wheel → minute wheel → cannon pinion
  Cannon pinion is friction-fit on center wheel arbor:
    → rotate hands without disturbing going train (which keeps running)
    → setting is against friction: when you stop, cannon pinion
       stays in its new position

MECHANICAL STATE MACHINE:
  Crown position         | Winding  | Setting
  ───────────────────────┼──────────┼──────────
  0: pushed in           | YES      | NO
  1: mid-pull            | NO       | DATE
  2: fully out           | NO       | TIME

Pull-out piece (lever): detects crown axial position
Setting lever: engages/disengages setting wheel based on pull-out piece position
Stem: axial (push/pull) AND rotational input; different mechanisms respond to each
```

**The cannon pinion friction:** The cannon pinion (drives the minute hand) sits on the center wheel arbor via a friction fit — tight enough to turn with the going train during normal operation, but loose enough to slip when you forcibly rotate the hands during time setting. This friction coupling is carefully calibrated; too tight = can't set hands easily; too loose = hands slip during shock or strong winding.

---

## Movement Finishing: The Aesthetics of Craftsmanship

In high-quality movements viewed through exhibition casebacks, every surface is decorated. This is not purely aesthetic — some finishing techniques reduce friction, improve corrosion resistance, or make wear patterns visible during inspection.

```
FINISHING TECHNIQUES

CÔTES DE GENÈVE (Geneva stripes):
  Parallel straight lines polished into flat surfaces of plates and bridges
  Angle: 45° to the wheel alignment (by convention)
  Applied by: abrasive stick moved in parallel passes across surface
  Visibility: only on flat surfaces (bridges, plates)
  Functional: smooth surface, shows quality of base metal preparation

PERLAGE (circular graining / pearling):
  Overlapping circles of fine abrasive applied with rotating peg
  Each circle ~0.5–1 mm diameter; overlapping by 50%
  Applied to: recessed surfaces, inside of plates (hidden surfaces)
  Functional: holds oil (texture acts as micro-reservoir);
  Appearance: matte pearlescent surface; shows on movement back surfaces

ANGLAGE (beveling + polishing edges):
  Every edge of every plate, bridge, and wheel arm is:
    1. Filed to a 45° bevel (~0.1–0.3 mm width)
    2. Polished to a mirror finish using pegwood sticks and diamond paste
  Required on: ALL visible edges in a finished movement
  Effect: beveled edges catch light; creates bright line around every component
  Difficulty: curved edges (on wheel spokes, bridge arms) are done by hand
  Time: ~30 min per bridge on a simple component; hours for complex pieces
  Anglage quality is the single best visual indicator of hand finishing quality

BLACK POLISHING (specular polishing):
  Some steel surfaces (lever, escape wheel, some springs) polished to
  optical flatness using pegwood + diamond paste + tin plate
  Result: "mirror black" — surface so flat it appears black in ambient light,
  mirror-bright under direct light
  Difficulty: requires absolutely flat substrate; any scratch restarts process
  Used: on steel parts; screws; levers

BLUED SCREWS:
  Steel screws heat-treated in a brass tray on a heat plate
  ~250–290°C → oxidation layer forms → deep blue color
  Not lacquer; actual iron oxide (Fe₃O₄)
  Functional: slight corrosion resistance improvement; aesthetic
  Blue color is a thin-film optical interference effect (same physics as blue steel gun finish)
```

**The finishing hierarchy:**

```
FINISHING LEVEL → MOVEMENT TYPE → EXAMPLES

No decoration:       Utility movement (ETA 2824 base grade)
                     Parts machined, no hand finishing
                     Unseen under opaque caseback

Basic decoration:    Côtes de Genève on bridges
                     Perlage on plates
                     (standard Swiss assembly grade)
                     ETA Elaboré / Top grade

Full decoration:     + Anglage on all edges (hand-beveled)
                     + Blued screws
                     + Black polish on steel parts
                     In-house manufacture movement
                     (Omega, Rolex)

Haute horlogerie:    All of the above + hand-chamfered wheel spokes
                     + polished bevels on wheel spokes (extremely difficult)
                     + "chamfered in the round" (curved anglage)
                     + custom skeletonization or openworking
                     Patek Philippe, AP, Lange, Breguet, JLC
```

---

## Materials: Alloys and Properties

```
CRITICAL ALLOY PROPERTIES

Component          | Material          | Key Property        | Modern Alternative
───────────────────┼───────────────────┼─────────────────────┼──────────────────────
Mainspring         | Nivarox 1 or 2    | Low temp coeff;     | Nivarox (no change)
                   |                   | non-magnetic;       |
                   |                   | corrosion resistant |
Hairspring         | Nivarox 1         | ~±1 ppm/°C elast.  | Silicon (Silinvar)
                   |                   | coefficient         |
Balance wheel      | Glucydur          | Low temp coeff      | Titanium; silicon
                   | (Cu-Be alloy)     | of inertia;         |
                   |                   | non-magnetic        |
Escape wheel       | Brass (plated)    | Machineable;        | Silicon (DRIE)
Lever              | Steel             | hard pivot zones    | Silicon
Pivot bearings     | Synthetic ruby    | Hard, smooth,       | Unchanged (still ruby)
                   | (Al₂O₃ + Cr₂O₃)  | non-oil-absorbing   |
Plates/bridges     | Brass (tombak)    | Machineable;        | Unchanged
                   |                   | Cu-Zn ~75/25        |
Wheels (going train)| Brass           | Teeth geometry      | Unchanged
Pinions (going train)| Steel          | Harder than brass   | Unchanged
Springs (click,    | Carbon steel      | Springiness;        | Nivarox variants
 detent, etc.)     | or Nivarox        | fatigue resistance  |
```

**Anti-magnetic watches:**

Nivarox hairsprings resist up to approximately 1,000 Gauss before saturation. Modern smartphones, tablet magnets (case closures), and handbag magnetic clasps can expose watches to 100–500 Gauss; MRI machines reach 15,000–60,000 Gauss. Two anti-magnetic approaches:

1. **Faraday cage:** Soft iron inner case (mu-metal or silicon steel) surrounds the movement, redirecting magnetic flux around the movement. Classic approach: Rolex Milgauss (1956), IWC Ingenieur. Limitation: the case opening (crystal, crown) is a gap in the cage.

2. **Non-magnetic components:** Replace steel and Nivarox parts with non-magnetic equivalents. Patek Philippe Aquanaut 5968 (silicon hairspring, titanium balance). Omega Master Chronometer (Nivarox but rated to 15,000 Gauss — a 15× improvement over standard).

---

## COSC Certification Testing Protocol

```
COSC TEST MATRIX — 16 DAYS, 5 POSITIONS, 3 TEMPERATURES

Day  | Position      | Temperature | Test Parameter
─────┼───────────────┼─────────────┼──────────────────────────────────────
1–10 | Dial up       | 23°C        | Mean daily rate (days 1–10)
11   | Dial down     | 23°C        | Rate vs dial-up difference
12   | Crown up      | 23°C        | Rate variation (max - min of all positions)
13   | Crown down    | 23°C        | Mean variation (all days)
14   | Crown left    | 23°C        | Greatest rate in any position
15   | Dial up       | 8°C         | Temperature coefficient (8° vs 23°)
16   | Dial up       | 38°C        | Temperature coefficient (38° vs 23°)

CRITERIA:
  Mean daily rate:           -4 to +6 seconds/day
  Mean variation in rate:    ≤2 sec/day
  Greatest variation:        ≤5 sec/day
  Dial-up vs dial-down diff: ≤10 sec/day
  Rate change per °C:        ≤0.6 sec/day/°C
```

The asymmetric allowance (-4 to +6, not ±5) is intentional: a watch running fast is preferable to one running slow (you can read a fast watch correctly; a slow watch risks missing appointments). Movement is adjusted to run slightly fast by the watchmaker.

---

## Decision Cheat Sheet: Movement Selection

```
USE CASE                        | MOVEMENT TYPE           | TYPICAL ACCURACY
────────────────────────────────┼─────────────────────────┼──────────────────────
Basic mechanical, budget        | ETA 2824-2 (standard)   | ±10–15 sec/day
  (<$300 watch)                  | or Sellita SW200-1      |

Mid-tier, practical accuracy    | ETA 2824-2 (top grade)  | ±5–7 sec/day
  ($300–$1,000 watch)            | or Miyota 9015          |

COSC-certified accuracy         | ETA 2892-A2 (Elaboré)   | ±4–6 sec/day
  ($1,000–$3,000 watch)          | or Sellita SW300 COSC   |

In-house, high quality          | Rolex 3235 (Cal)        | ±2 sec/day (Rolex)
  ($5,000–$15,000 watch)         | Omega 8800 Co-Axial     | ±0 to +5 sec/day (Omega)
                                 | JLC 899A               | ±2–4 sec/day

Grand complication               | Patek 240 Q (perpetual) | ±2 sec/day
  ($50,000+ watch)               | AP 2897 (tourbillon)    | ±5–10 sec/day
                                 | (complications add      | (tourbillon no accuracy
                                 |  mechanisms but not     |  benefit in wristwatch)
                                 |  rate accuracy)         |
```

---

## Common Confusion Points

**"A watch with more jewels is more accurate."**
17 jewels covers all functional bearing points. Additional jewels (21, 25, etc.) cover keyless works, date mechanism, and/or are decorative. The most important accuracy factors — hairspring quality, balance poise (balance wheel perfectly centered), escapement geometry, and regulation — are not related to jewel count above 17.

**"Nivarox is a type of alloy; it's generic."**
Nivarox is a brand name owned by Nivarox-FAR SA (Swatch Group subsidiary). It's also used generically to refer to the class of cobalt-beryllium-iron alloys used for hairsprings. Patek Philippe's Silinvar, Rolex's Parachrom, and Omega's Co-Axial platform use different proprietary formulations or materials (silicon in Patek's case). "Nivarox" in a watch spec sheet means the genuine Nivarox-FAR alloy.

**"The mainspring provides constant force to the gear train."**
The mainspring provides decidedly non-constant force — it's roughly 2.5–4× more powerful when fully wound than when nearly run down. Modern watches mitigate this with barrel slippage (which limits the maximum torque at full wind) and sometimes with a remontoire (a small secondary spring that is regularly rewound by the going train, providing constant force for the last gear stages). Without compensation, a watch would run fast when freshly wound and slow as it runs down.

**"Silicon parts will eventually replace all metal parts in watch movements."**
Silicon excels for parts that require: extreme dimensional stability, non-magnetic properties, and low lubrication requirements (escape wheel, lever, hairspring). It's poorly suited for: mainsprings (needs ductility and very high elastic strain), gear train wheels (silicon is brittle; wheels need to survive shock), barrels (need ductility). The likely outcome is hybrid movements: silicon for the escapement assembly and hairspring; traditional alloys for the going train and mainspring.

**"A mechanical watch never needs a battery, so it needs no maintenance."**
Oil degrades: watch oils polymerize over time, becoming sludge that increases friction and causes rate errors. Service interval: 5–10 years for most movements. A service involves: complete disassembly, ultrasonic cleaning, inspection under magnification, replacement of worn parts, reassembly with fresh oil, regulation (timing in multiple positions), and reassembly into the case. Cost: $150–$500 for standard movements; $500–$5,000+ for complications or haute horlogerie.
