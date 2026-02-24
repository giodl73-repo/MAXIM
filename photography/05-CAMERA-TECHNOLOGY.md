# Camera Technology

## The Big Picture

Camera technology is the **electromechanical system** that controls light collection, timing, and delivery to the recording medium. Over 170 years, the evolution has been toward more accurate viewfinding, faster operation, and eventually elimination of moving parts.

```
CAMERA TECHNOLOGY EVOLUTION:

  Camera obscura (lens + box)     ~1600s: no chemistry, just optics
  Daguerreotype camera             1839: ground-glass focus, cap-uncover-cap shutter
  Large format view camera         1870s: bellows, rising front, ground glass back
  Hand-held cameras                1880s: roll film; mechanical shutter; waist-level VF
  Graflex SLR (large mirror)       1902: single-lens reflex, large format
  Leica 35mm (rangefinder)         1925: coupled rangefinder; accurate focusing without mirror
  Twin-lens reflex (Rolleiflex)    1928: waist-level through-lens viewing
  35mm SLR pentaprism             1954: eye-level SLR (Asahi Pentax)
  Auto-exposure                    1960s: built-in meters; aperture/shutter priority
  Autofocus SLR                    1985: Minolta AF system; phase detection AF
  Digital DSLR                     1991: CCD/CMOS sensor in SLR body; mirror box preserved
  Mirrorless interchangeable lens  2008+: EVF replaces mirror + optical VF
  Computational camera             2010+: multi-frame processing as fundamental feature
```

---

## Single-Lens Reflex (SLR) Mechanism

The SLR was the dominant serious camera format from ~1960 to ~2015.

```
SLR OPTICAL PATH:

Lens → 45° mirror → Pentaprism/Pentamirror → Eye

         ┌─────────────────────────────────────────────────────┐
         │                                                     │
 LENS →  │         ╱ mirror (raised for exposure)              │
         │  ┌───╱ mirror (down for viewing) ──────────────────►│
         │  │                                                  │ Pentaprism
         │  ▼                                                  │    │
         │ Focus screen (shows image projected by lens)        │    ▼
         │                                                     │ Eyepiece
         └─────────────────────────────────────────────────────┘
                                ↓ (at exposure)
                          Film / Sensor plane

OPERATION:
  Viewing: mirror down → image refracted up by mirror → projected on focus screen
           pentaprism (5-sided prism) corrects image: mirrors left-right twice
           → correct-orientation image at eye
  Exposure: press shutter → mirror flips up (blackout) → focal plane shutter opens
            → sensor/film exposed → shutter closes → mirror returns

FOCAL PLANE SHUTTER:
  Two curtains (blinds) that travel across the film/sensor plane
  First curtain opens (travels from one side) → exposes sensor
  Second curtain follows after delay = shutter speed
  At fast speeds: second curtain chases first → only a slit exposes at any moment
  X-sync (flash sync) speed: the slowest speed at which entire sensor is open simultaneously
    → required for flash synchronization
    Typical: 1/200s–1/250s for focal plane shutters
    Above sync speed: slit = only part lit by flash → dark band in image

MIRROR PROBLEMS:
  Mirror blackout during exposure: can't see through OVF during exposure
  Mirror slap: vibration from mirror flip → camera shake → reduces sharpness
               especially at 1/15s–1/125s range
  Mirror box depth: requires large back-focal distance → retrofocus wide angles
  Mass and complexity: mirror + pentaprism + focus screen + mirror drive mechanism
```

---

## Leaf Shutter

```
LEAF SHUTTER (in-lens):
  Shutter blades embedded in lens, not camera body
  Concentric blades open from center → close from edges

PROPERTIES:
  Flash sync at ALL shutter speeds (entire aperture exposes simultaneously at any speed)
  → Up to 1/1000s flash sync (vs 1/200s for focal plane)
  → Essential for fill-flash in bright daylight (high ambient → fast shutter needed)

USED IN:
  Medium format cameras (Hasselblad with CF lenses, Rolleiflex, Mamiya)
  Large format field cameras
  Some compact cameras (Leica X)
  High-end digital medium format (Fuji GFX with leaf shutter lenses)

LIMITATIONS:
  Each lens must contain its own shutter → complex, expensive lenses
  Maximum speed limited (~1/1000s) vs focal plane (1/4000s–1/8000s)
  Synchronization between lens shutter and camera back electronics needed
```

---

## Rangefinder

```
RANGEFINDER FOCUSING MECHANISM:

Double-window parallax-based distance measurement:
  Two optical windows separated by known baseline (usually ~50–70mm)
  One window: direct view to scene
  Second window: mirror/prism that reflects onto same eyepiece from different angle
  Coincidence focus: rotate focusing ring until two overlaid images align
  When images coincide → subject at correct focus distance
  Mechanism rotates a cam linked to focusing helicoid of lens

ADVANTAGES over SLR:
  No mirror → silent; no blackout; no mirror slap
  Compact body (no mirror box) → rangefinder lenses shorter and smaller
  Bright, lag-free optical viewfinder (not through lens → always bright)

LIMITATIONS:
  Parallax: VF not aligned with lens axis → framing shifts at close distances
  No through-lens viewing → difficult to judge DoF, bokeh
  Maximum magnification for rangefinder coupling (~500mm typical)
  Not practical for macro
  Calibration-sensitive: RF patch must be precisely aligned

CLASSIC RANGEFINDERS: Leica M-series (M3, M6, M10); Zeiss Ikon; Voigtländer Bessa
```

---

## Medium and Large Format

### Medium Format (120/220 Roll Film)

```
120 FORMAT: 6cm wide film roll; varying frame lengths
  6×4.5cm: "645" — 15 frames/roll; most compact
  6×6cm: square format; Hasselblad, Rollei; 12 frames/roll
  6×7cm: "portrait" format; Mamiya RB/RZ; 10 frames/roll
  6×9cm: panoramic-ish; landscape
  6×17cm: ultra-panoramic (specialist)

SENSORS MODERN DIGITAL:
  Phase One, Fujifilm GFX, Hasselblad: 53×40mm sensors ("medium format digital")
  (Not actual 6×6 — smaller, but larger than full-frame 36×24)

ADVANTAGES:
  Larger film → finer grain → better enlargement → cleaner 20×24" prints
  Square format (6×6): compose either orientation without rotating camera
  System cameras: interchangeable backs (film, Polaroid, digital)

LARGE FORMAT (4×5, 5×7, 8×10 sheet film):
  Individual sheets; slow, deliberate photography
  Every frame is precious (expense + handling)
  View camera: monorail or flatbed; bellows; front and back standards

MOVEMENTS (the primary advantage of view camera):
  SWING: rotate front/back standard around vertical axis
  TILT: rotate front/back standard around horizontal axis
  SHIFT: translate front/back standard up/down
  RISE/FALL: synonym for shift

SCHEIMPFLUG PRINCIPLE:
  When lens plane, subject plane, and film plane all meet at a common line
  → entire subject plane is in sharp focus regardless of depth
  → Tilt lens forward → field rows in sharp focus for landscape (horizontal plane)
  → Tilt backward → more vertical subject plane

  Normal: film plane ∥ lens plane → plane of sharp focus ∥ both planes
  Tilted lens: film plane still flat; lens tilted → sharp focus plane tilts
               per Scheimpflug, when extended planes meet at a line

APPLICATIONS:
  Architecture (shift to correct keystone distortion from tilted camera)
  Commercial product (tilt for plane of focus on horizontal surface)
  Landscape (Ansel Adams-style; total zone control)
  Portrait in studio (4×5 → contact print or limited enlargement → superb quality)
```

---

## Twin-Lens Reflex (TLR)

```
TLR DESIGN (Rolleiflex, 1928; Mamiya C330):
  Two coaxial lenses on front standard:
    Taking lens: identical focal length; opens for exposure
    Viewing lens: separate but same focal length; opens to focus screen (always)
  Waist-level viewing from above; viewing lens feeds upward to ground glass

ADVANTAGES:
  No viewfinder blackout (viewing lens always open — separate from taking lens)
  Quiet (leaf shutter in taking lens)
  No mirror box required

DISADVANTAGES:
  Parallax between taking and viewing lens (at close distance → framing shift)
  Waist-level viewing = awkward for eye-level work; reversed L-R image requires practice
  Single focal length (standard TLRs) — no zoom
  Square format (6×6) mostly

HISTORICAL SIGNIFICANCE:
  Dominant professional tool for photojournalism + portraiture 1940s–1960s
  Weegee (tabloid), Diane Arbus (social documentary) — characteristic aesthetic
  associated with waist-level framing, dramatic distortion, square format
```

---

## Mirrorless Cameras

The dominant professional system since ~2020. Eliminates the mirror box entirely.

```
MIRRORLESS DESIGN:

Light → Lens → Sensor (CMOS with PDAF pixels) → Electronic Viewfinder (EVF)

WHY MIRRORLESS WINS:
  Shorter flange distance: no mirror box → sensor much closer to lens mount
    Leica M: 27.8mm  Nikon Z: 16mm  Sony E: 18mm  Canon RF: 20mm
    vs DSLR: Canon EF: 44mm  Nikon F: 46.5mm

  Shorter flange distance advantages:
    → Wider lens design freedom (rear element can be very close to sensor)
    → Better performance at wide angles (telecentric design possible)
    → Thin, compact bodies

  No mirror slap → quieter; no blackout; faster burst

ELECTRONIC VIEWFINDER (EVF):
  High-resolution OLED or LCD (typically 3–5MP resolution, 0.5×–0.78× magnification)
  Shows exact image the sensor will record:
    → White balance preview
    → Exposure preview (histogram in viewfinder)
    → Focus peaking (colored edges on in-focus areas)
    → Magnified focus assist
    → Night/low-light: EVF brightens scene even when ambient is dim
  Lag (5–20ms modern) → imperceptible in most situations; top cameras now < 5ms

PHASE DETECTION AF ON SENSOR:
  DSLR PDAF: phase detection pixels on dedicated AF sensor in mirror box
             → could not work without mirror → AF not available in live view typically
  Mirrorless PDAF: phase detection pixels embedded in imaging sensor itself
    Dual-pixel AF (Canon): every pixel is split into two sub-pixels → full PDAF coverage
    Sony Exmor RS, Nikon BSI: similar dedicated PDAF pixels across sensor
    → Real-time PDAF for still and video; eye/face detection AF
    → Track subject face/eye at 20-30 fps with 100% coverage
```

### AF System Evolution

```
AUTOFOCUS HISTORY:

Passive AF:
  Contrast detection: maximize contrast in AF zone → find focus by hill-climbing
    → Slow (must move lens back and forth to find peak); no hunting pause possible
    → Reliable; used in compacts, early DSLRs in live view

  Phase detection (film SLR era, 1985+):
    Separated image from half-mirror → two light paths; compare phase shift
    Phase shift = direction and magnitude of defocus → move lens directly to focus
    → Fast; one-shot; predictive (calculates where moving subject will be)
    Phase detection sensors in DSLR mirror box: Minolta Maxxum 7000 (1985) → revolution

  Contrast + PDAF hybrid (modern mirrorless):
    PDAF for fast acquisition + speed; CDAF for final confirmation
    → Phase detect gets close; contrast verifies → best of both

Computational/AI AF (2018+):
  Deep learning models trained on face/eye/body/animal detection
  Sony Alpha-9, Nikon Z9, Canon R3, OM-1: real-time eye tracking at 30fps
  Tracks through blinks, turns, low contrast
  → Democratized professional sports/wildlife photography
```

---

## Camera Format Comparison

| Format | Sensor/film size | Crop factor | DoF equivalent | Best for |
|--------|-----------------|-------------|----------------|---------|
| Medium format digital | 53×40mm | 0.8× vs FF | Shallower DoF | Studio; landscape; commercial |
| Full frame (FF) | 36×24mm | 1× | Reference | All-around professional |
| APS-C | ~24×16mm | 1.5–1.6× | ~2× deeper vs FF | Wildlife; sports (reach); smaller bodies |
| Micro Four Thirds | 17×13mm | 2× | ~2× deeper vs APS-C | Travel; video; compact systems |
| 1-inch | 13×9mm | 2.7× | Deep DoF | Compact cameras; drones |
| Smartphone | ~5×4mm | ~7× | Very deep DoF | Computational photography; convenience |

---

## Decision Cheat Sheet

| Goal | Camera system |
|------|--------------|
| Maximum image quality | Medium format digital (Phase One, Fuji GFX) |
| Best all-around professional | Full-frame mirrorless (Sony A9 III, Nikon Z9, Canon R5) |
| Wildlife/sports (reach + speed) | APS-C + telephoto (Nikon Z8, Sony A6700) |
| Silent, discreet documentary | Rangefinder (Leica M); or mirrorless silent mode |
| Architecture (perspective control) | Large format + movements; or tilt-shift lens on FF |
| Flash at any shutter speed | Leaf shutter system (Hasselblad, Fuji GFX leaf lenses) |
| Film aesthetic, square format | Medium format 6×6 (Hasselblad 500, Rolleiflex) |
| Maximum DoF, studio | Large format 4×5 (Tilt + small aperture) |

---

## Common Confusion Points

**Mirrorless EVF lag is no longer relevant for most photography**
Early mirrorless (2010–2015) had EVF lag of 30–80ms — perceptible and bothersome for sports. Modern flagships (2022+) achieve <5ms EVF lag, matching or exceeding OVF mirror refresh. The complaint is now a historical artifact for consumer-grade cameras.

**Shutter speed on a DSLR is limited by focal plane shutter sync, not by any fundamental physics**
The X-sync limitation (1/200s) comes from the focal plane curtains needing time to travel across the full sensor. Leaf shutters in medium format lenses have no such limitation. High-speed sync (HSS) flash modes work above X-sync by pulsing the flash rapidly during the moving slit — but lose power efficiency dramatically.

**Full-frame does not simply "give more background blur"**
A full-frame sensor with a 50mm f/1.8 lens gives shallower DoF than an APS-C with a 35mm f/1.8 lens (same angle of view), because the FF lens is physically larger aperture. But a 35mm f/1.4 on APS-C can produce similarly shallow DoF to 50mm f/1.8 on FF. The relationship is focal length × aperture, accounting for crop factor equivalence.

**Rangefinder is NOT an autofocus system**
Rangefinder focusing is manual — the photographer manually aligns the rangefinder patch (turns the focus ring until overlaid images coincide). It's a manual focusing aid, more accurate than ground-glass estimation for the lens used, but not automated. The Contax G2 was unusual: motorized rangefinder AF, but that system's coupling mechanism was complex.

**Mirrorless cameras can use DSLR lenses via adapter — but AF may be compromised**
Mirrorless bodies have shorter flange distances. Via adapter, any DSLR lens can mount. Autofocus via adapter works when the camera has sensor-based PDAF that's protocol-compatible with the adapter/lens combination. Canon EF lenses on Canon RF bodies via EF-EOS R adapter: full AF. Canon EF lenses on Sony E-mount: third-party adapters; variable reliability. The shorter mount distance is actually an advantage for lens compatibility via adapters.
