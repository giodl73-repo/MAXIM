# Cinematography and Optics: Lenses, Exposure Triangle, Film Stocks vs Digital Sensors, Dynamic Range

## The Big Picture

Cinematography is applied optics. The variables you control — focal length, aperture, shutter, sensitivity — determine what information reaches the recording medium and how it appears. Understanding the physics makes the aesthetic choices legible. The tradeoffs are physical, not arbitrary conventions.

```
OPTICAL SYSTEM OVERVIEW

  SCENE           LENS           APERTURE         SENSOR/FILM
(light source)  (focuses       (controls         (captures
                light into     light amount       intensity
                image)         + depth of field)  distribution)
     |               |               |                 |
     +-------+-------+-------+-------+-----------------+
             |
             v
     RECORDED IMAGE
     (spatial intensity distribution on recording medium)

EXPOSURE TRIANGLE:
     +-------------------+
     |   EXPOSURE        |
     |                   |
     |   Aperture  <--+  |
     |   Shutter   <--+--+-- All three determine
     |   ISO/ASA   <--+  |   TOTAL LIGHT on sensor
     |                   |   One up = another down
     +-------------------+   for same exposure

Each variable has a SIDE EFFECT beyond exposure:
  Aperture -> depth of field
  Shutter speed -> motion blur
  ISO -> noise/grain
These side effects are the creative tools of cinematography.
```

---

## Focal Length and Lenses

```
FOCAL LENGTH: THE FUNDAMENTAL LENS PARAMETER

Definition: Distance from optical center to focal plane
            when focus set to infinity
Units: millimeters (35mm, 50mm, 85mm, etc.)
Reference: typically for 35mm full-frame equivalent

FOCAL LENGTH EFFECTS:
  Short focal length (WIDE ANGLE): e.g., 24mm, 28mm
    Large field of view (sees more of scene)
    Objects appear farther apart than natural (expansion)
    Background appears small relative to foreground
    Depth of field: large (more in focus)
    Distortion: barrel distortion at extremes (fisheye)
    Use: environments, action, claustrophobia with compression

  "Normal" focal length: ~50mm (35mm sensor)
    Approximates human visual angle
    Perspective: "natural" (similar to how eye perceives)
    Minimal distortion

  Long focal length (TELEPHOTO): e.g., 85mm, 135mm, 300mm
    Narrow field of view (sees less)
    Objects appear closer together (compression)
    Background appears large relative to subject (flattening)
    Depth of field: shallow (less in focus)
    Requires: greater physical distance between camera and subject
    Use: subject isolation, emotional intimacy, surveillance feel

PERSPECTIVE DISTORTION:
  MYTH: Wide angle lens distorts faces (makes noses big)
  REALITY: It's camera-to-subject DISTANCE that changes perspective
  Physics:
    Wide angle: must be close to fill frame -> nose is much closer than ears
                ratio of distances exaggerated -> nose appears bigger
    Telephoto: must be far to fill frame -> nose and ears similar distance
               ratio preserved -> natural face proportions
  "Telephoto compression" and "wide angle expansion" are
  distance effects, not lens effects. The lens determines where
  you stand; the distance creates the perspective.

SPECIFIC LENS USE:
  16-24mm: architecture, environment, extreme wide shots
  28-35mm: documentary, street photography, news
  50mm: normal, classic portraits, narrative cinema default
  85mm: portrait lens, classic face shots, least distortion for faces
  100-135mm: telephoto portraits, product shots
  200-400mm: sports, wildlife, surveillance aesthetic
  400-600mm: long-range sports, nature
```

---

## Aperture and Depth of Field

Aperture controls two things simultaneously: light level and depth of field. These cannot be separated.

```
APERTURE: f-STOP SYSTEM

f-stop = focal_length / aperture_diameter

  Wide aperture: small f-number (f/1.4, f/2.0, f/2.8)
    Large opening -> more light -> faster shutter possible
    Shallow depth of field

  Narrow aperture: large f-number (f/8, f/11, f/16)
    Small opening -> less light -> slower shutter required
    Deep depth of field

f-STOP SCALE (each step = 1 stop = 2x light):
  f/1.0 | f/1.4 | f/2 | f/2.8 | f/4 | f/5.6 | f/8 | f/11 | f/16 | f/22
  <-- more light ----------------------------------------- less light -->
  <-- shallower DoF ---------------------------------------- deeper DoF -->

DEPTH OF FIELD (DoF):

  Definition: range of distances in focus
  "Circle of confusion": how much defocus is acceptable

  FACTORS:
    Aperture: wider -> shallower DoF
    Focal length: longer -> shallower DoF
    Subject distance: closer -> shallower DoF
    Sensor size: larger -> shallower DoF (for same field of view)

  HYPERFOCAL DISTANCE:
    Aperture/focal length combination where DoF extends from
    half-hyperfocal to infinity
    Deep focus: shoot at or beyond hyperfocal distance
    Everything front-to-back in focus

CINEMATOGRAPHIC USE:
  SHALLOW DoF (wide aperture):
    Subject in focus, background blurry (bokeh)
    Isolates subject from environment
    "Cinematic" look
    Requires: precise focus pulling (changing focus during shot)

  DEEP DoF (narrow aperture):
    Multiple planes all in focus simultaneously
    Orson Welles: Citizen Kane (Gregg Toland, DP)
    Welles needed: conversations with multiple characters in frame
    All in focus simultaneously
    Required: extremely bright lights (required narrow aperture)
    Theatrical staging: deep space

BOKEH:
  Out-of-focus highlights: circles of confusion
  Shape: determined by aperture blade geometry
    Circular aperture -> round bokeh
    6-blade -> hexagonal bokeh
    Anamorphic lenses: oval bokeh (wider than tall)
  Quality: "smooth" bokeh = creamy, gradual falloff
           "nervous" bokeh = edges, pattern, distracting
```

---

## Shutter Speed and Motion Blur

```
SHUTTER SPEED AND MOTION BLUR

FILM CAMERA SHUTTER:
  Rotating disc with opening(s)
  Opening angle: how long per revolution the film is exposed
  At 24fps: 1/24 second per frame
  Shutter open for PORTION of that 1/24 second

  180° SHUTTER RULE:
    Standard: shutter angle = 180° (half the revolution = exposed)
    At 24fps: exposure time = 1/48 second
    This gives "natural" motion blur that matches eye's perception

  RESULT OF 1/48 SECOND EXPOSURE:
    Moving subjects: blur during 1/48 second exposure
    This blur is what makes motion appear "natural" in cinema
    Too short: stroboscopic (crisp but unnatural motion)
    Too long: excessive blur, smear

DIGITAL CAMERA EQUIVALENT:
  No mechanical shutter (usually): electronic shutter control
  Standard: shutter angle = 180° -> shutter speed = 1/(fps*2)
    24fps -> 1/48 sec
    30fps -> 1/60 sec
    48fps -> 1/96 sec

HIGH FRAME RATE (HFR) MOTION BLUR:
  Peter Jackson: Hobbit (48fps) with 180° shutter = 1/96 second
  Less motion blur than 24fps (1/48 sec exposure)
  Why: each frame exposed for half the time
  Effect: "hyper-real", "too smooth", "soap opera effect"
  Audience discomfort: different from learned "film look"
```

---

## ISO / ASA — Sensitivity

```
SENSITIVITY: ISO/ASA SYSTEM

Film ASA / digital ISO: measures sensitivity to light
  Low ISO (100, 200): less sensitive, requires more light
  High ISO (3200, 12800): more sensitive, less light needed

  ISO doubles: one stop increase (same as 1 aperture stop or
               1 shutter stop in exposure terms)

FILM GRAIN:
  Light-sensitive silver halide crystals in emulsion
  Larger crystals: more sensitive (higher ASA) but more visible grain
  Smaller crystals: less sensitive but sharper, finer
  GRAIN: visible texture is exposed crystal clusters
         part of the analog photography aesthetic

  Film stocks (35mm cinema):
  Kodak Vision3 50D: very fine grain, daylight-balanced, low ASA
  Kodak Vision3 500T: fast, visible grain, tungsten-balanced
  Kodak Double-X (5222): B&W, medium grain, documentary classic
                          (used in Schindler's List, Raging Bull B&W scenes)

DIGITAL NOISE:
  Sensor photosites: each captures photons, converts to charge
  Shot noise: statistical variation in photon count (physics, not fixable)
  Read noise: electronics reading signal, adds noise floor
  Dark current: thermal electrons (heat creates false signal)
  High ISO: amplify signal -> also amplify all noise
  ISO invariance: some modern sensors capture full dynamic range
                  at base ISO; increasing ISO = just amplifying
                  (better to push in post vs raise ISO)
  PATTERN NOISE: sensor-specific fixed-pattern noise
  Random noise: easier to remove than pattern noise

  Modern sensors (2024): usable ISO 25,600-102,400 in many cameras
  35mm film equivalent: pushing Kodak 500T to ASA 3200 = very grainy
  Digital: much cleaner at high ISO than film
```

---

## Film Stocks vs Digital Sensors

```
FILM VS DIGITAL COMPARISON

                  FILM (35mm)          DIGITAL (modern)
------------------+---------------------+---------------------
Resolution        | ~5-8K equivalent    | 4K-8K native;
                  | (varies by stock)   | IQ-4 150MP medium format
Color response    | Non-linear, latitude | Linear capture + LUT
                  | Variable per stock  | All starts identical
                  | Unique character    | Graded to look different
Latitude          | ~13-15 stops        | ~14-17 stops (top sensors)
                  | (dynamic range)     | (more than film)
Grain vs noise    | Organic grain       | Electronic noise
                  | (predictable size,  | (random, harder to love)
                  |  texture, color)    |
Aspect ratio      | 35mm: 1.33 native   | Sensor-dependent
                  | (1.33x crop)        |
Speed (sensitivity)| Fixed per roll     | Adjustable per shot
Cost per minute   | High (stock+process)| Low after fixed cost
Archival          | Stable if stored    | Format obsolescence
                  | cold+dark: 100yrs   | concern
Look              | "Film look":        | "Digital look":
                  | certain color       | Extremely clean,
                  | rendition, grain    | may require grading
                  | texture             | for "warmth"

DIGITAL INTERMEDIATE (DI):
  Scan film negative to digital
  Color grade in digital domain
  Output to DCP (digital cinema) or back to film
  Enabled by: O Brother Where Art Thou? (2000) first DI
  Now: all major productions use DI
  Film-shot productions: scan negative for DI
  Digital-shot: no scan needed; DI is native

WHEN FILM IS STILL USED (2020s):
  Christopher Nolan: Dunkirk (2017), Oppenheimer (2023)
  Quentin Tarantino: all films in 35mm / 70mm
  Paul Thomas Anderson: film or hybrid
  Reasons: aesthetic preference, forcing discipline on production,
           "film look", archival (Kodak: physical archive in cave)
  Cost: ~$2,000/hour of 35mm film + processing
         vs digital: essentially free after fixed costs
```

---

## Dynamic Range

```
DYNAMIC RANGE IN CINEMATOGRAPHY

Definition: ratio of lightest to darkest values captured
Units: stops (each stop = 2x light)
       or EV (exposure value, same as stop)

HUMAN VISUAL SYSTEM:
  Static: ~12-14 stops at any moment
  Dynamic (adapted): ~20 stops total adaptation range
  Eye continuously adapts: step from bright to dark = adjustment time

PRACTICAL SCENE DYNAMIC RANGE:
  Interior vs window: window can be 10-14 stops brighter
  Sunny exterior: ~12-16 stops from shadows to highlights
  Night scene with lights: 20+ stops

SENSOR/FILM LATITUDE:
  Film (35mm): ~13-15 stops latitude
  Sony VENICE 2: ~16 stops
  ARRI ALEXA 35: ~17 stops
  RED MONSTRO 8K: ~17 stops
  iPhone 15 Pro: ~12-13 stops
  Consumer cameras: ~10-13 stops

HANDLING HIGH DYNAMIC RANGE:
  EXPOSE TO THE RIGHT: maximize exposure without clipping highlights
                        (digital noise in shadows easier to fix than
                         blown-out highlights; film more forgiving of
                         over-exposure in highlights)

  HIGH DYNAMIC RANGE VIDEO (HDR):
    SDR (Standard Dynamic Range): 100 nits peak white
    HDR10: 1000 nits peak white, 10-bit
    Dolby Vision: 4000-10000 nits, 12-bit, frame-by-frame metadata
    HLG (Hybrid Log-Gamma): broadcast HDR

  LOG GAMMA:
    Cameras record in "log" profile: compressed dynamic range
    Normal-looking image: appears flat, washed out
    Full dynamic range preserved in compressed form
    Color grade in post: expand log -> display gamma
    Maximizes bit depth utilization across full dynamic range

    ARRI Log C, Sony S-Log3, Red Log3G10: manufacturer-specific
    Each needs specific LUT or manual grade to look correct
    Color science differences are now a DP aesthetic choice
```

---

## The Exposure Triangle as Creative Tool

```
EXPOSURE TRIANGLE: CREATIVE APPLICATION

Scenario: shoot interview, available office light

Option A: f/2.8, 1/50s, ISO 800
  Result: subject in focus, background blurry (shallow DoF)
  Motion: slight blur if subject moves
  Noise: moderate
  Aesthetic: intimate, isolated, slightly soft

Option B: f/8, 1/50s, ISO 6400
  Result: deep focus, background sharp
  Motion: slight blur
  Noise: significant
  Aesthetic: documentary, environmental, slightly grainy

Option C: f/5.6, 1/200s, ISO 3200
  Result: moderate DoF
  Motion: sharp (fast shutter)
  Noise: moderate
  Aesthetic: clean, crisp, neutral

Option D (add light, lower ISO):
  Add 800W LED panel -> can now shoot f/5.6, 1/50s, ISO 400
  DoF: moderate
  Motion: natural blur
  Noise: minimal
  Aesthetic: controlled, clean, filmmaking craft visible

Same "scene" = infinite options. The DP makes choices based on:
  What the director wants to emphasize
  What the narrative needs in this moment
  What the available light allows
  What the format/sensor can achieve
  Personal aesthetic vision

"Good exposure" is not a single answer — it's a navigated tradeoff.
```

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| What does focal length control? | Field of view (angle) + perspective effects (via necessary shooting distance) |
| Why does telephoto "flatten" perspective? | Forces camera far away; near/far objects at similar distances = less relative difference |
| What does aperture control? | Light level + depth of field (cannot be separated) |
| What is the 180° shutter rule? | Set shutter speed to double the fps (24fps -> 1/48s); gives natural motion blur |
| What is film grain vs digital noise? | Grain = silver crystal clusters, organic texture. Noise = electronic signal variation, less organic |
| What is a digital intermediate? | Scan film to digital, grade, output to DCP or back to film; enables modern color grading |
| What is dynamic range? | Stops from darkest to brightest captured detail; modern cinema cameras 14-17 stops |
| What is log gamma? | Compressed recording of full dynamic range; looks flat; expanded in post to display gamma |

---

## Common Confusion Points

**"Wide angle lenses distort faces."** The lens doesn't distort; the required close distance does. If you shoot a portrait at 24mm (wide) vs 85mm (telephoto) at the same framing (filling the frame with the face), the 24mm requires being much closer. At close distance, the nose-to-ear distance ratio changes relative to the total distance — the near parts look larger. Move the 24mm lens far away (and step in to crop) and the distortion disappears. The lens choice determines the shooting distance; the shooting distance determines the perspective.

**"Higher resolution is always better."** For cinema, resolution is one factor among many. ARRI ALEXA cameras (1920x1080 to 4K) are used for high-end productions because of their dynamic range, color science, and noise characteristics — not despite having lower resolution than some competitors. A 17-stop dynamic range at 2.8K may produce a better result than 8K at 12 stops for a high-contrast scene.

**"Digital cinema looks better than film."** They're different. Modern digital captures more dynamic range than 35mm film. Film grain is organic and aesthetically pleasing to many; digital noise less so. Color rendition from different film stocks has unique character; digital starts neutral and is graded. Many cinematographers prefer shooting on film for the quality of the negative, then scanning for DI grading. Neither is objectively better; they're tools with different characteristics.

**"F-stop numbers are confusing — f/2.8 is bigger than f/11."** Yes, because f-stop is a ratio (focal_length / diameter). A larger denominator means a smaller physical aperture. f/2.8 = focal_length / 2.8 (large hole); f/11 = focal_length / 11 (small hole). The confusing direction makes sense when you remember it's a fraction: 1/2.8 > 1/11 (more light through f/2.8 than f/11).
