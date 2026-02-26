# Television Technology: Mechanical Scanning, Electronic TV, NTSC/PAL/SECAM, CRT to Flat Panel

## The Big Picture

Television is a solved problem in the sense that the fundamental requirement — converting 2D spatial information to a 1D temporal signal, transmitting it, and reconstructing the image — has exactly one general family of solutions. The evolution was from mechanical to electronic scanning, then from analog to digital, then from cathode-ray to flat panel. Each transition involved a key physical insight.

```
TELEVISION TECHNOLOGY EVOLUTION

MECHANICAL SCANNING ERA (1884-1937):
  Nipkow disc (1884) -> Baird mechanical TV (1926)
  Concept: spinning disc with holes scans image sequentially
  Resolution: 30-240 lines, very limited
  Fundamental limit: mechanical speed limits scan rate
  End: electronic scanning made mechanical obsolete

ELECTRONIC SCANNING ERA (1927-2009):
  Philo Farnsworth: electron beam scanning (1927, patent filed)
  Vladimir Zworykin (RCA): iconoscope camera, kinescope display
  RCA vs Farnsworth: patent wars
  NTSC standard (US 1941): black and white, 525 lines, 60 fields/sec
  Color (1953): NTSC color standard
  PAL (1967 Europe), SECAM (1967 France): color alternatives
  All-analog: modulated RF signal, raster scan display

CRT ERA (1938-2000s):
  Cathode Ray Tube: electron beam steered by magnetic fields
  Phosphor screen: glows where electron beam hits
  Color CRT: three electron guns (R/G/B), shadow mask/aperture grille
  Best CRT: 40M+ pixels addressable, excellent color
  CRT died: plasma/LCD flat panels better in all practical ways (size, weight)

FLAT PANEL ERA (2000s-present):
  Plasma (PDP): 2000-2015
  LCD (TFT-LCD): 2005-present (dominant)
  OLED: 2013-present (premium)
  MicroLED: emerging

DIGITAL BROADCAST:
  ATSC (US, 1998 rollout): digital OTA broadcast
  DVB-T (Europe, 1998+): digital OTA broadcast
  ATSC 3.0 (2017+): IP-based digital broadcast
  Analog switchoff: US 2009, UK 2012, Europe complete ~2012-2015
```

---

## Mechanical Television: Nipkow Disc

```
NIPKOW DISC (1884)

Paul Nipkow: German engineering student, 1884
Patent: "Electric Telescope" (but never built working system)

CONCEPT:
  Scanning disc = a rotating disc with holes arranged in a spiral
  Hole positions: each hole at a slightly different radius
  As disc spins: each hole sweeps across a different horizontal line
  With enough holes: disc sweeps complete image

  DIAGRAM:
  Disc (edge view):
    . <- hole 1 (outermost, scans line 1)
   .  <- hole 2 (slightly inner, scans line 2)
  .   <- hole 3 (slightly more inner, scans line 3)
  ... etc.

  How it scans:
  One rotation = one frame (each hole sweeps one line)
  Frame rate: limited by how fast disc can spin
  Resolution: number of holes = number of scan lines

CAMERA SIDE:
  Bright light illuminates scene
  Disc spins in front of photocell (selenium)
  As each hole sweeps: photocell sees brightness of that image point
  Output: varying electrical signal = brightness over time

DISPLAY SIDE:
  Matching disc at receiver, synchronized to transmitter
  Neon lamp behind disc: brightness controlled by received signal
  As holes sweep: lamp illuminated at correct time = image reconstructs

LIMITATIONS:
  Frame rate: ~12-18 fps max (mechanical speed limit)
  Resolution: 30-240 lines practical
  Synchronization: mechanical systems had sync problems
  Brightness: dim (neon lamp + spinning disc = little light)
  Size: image tiny (postcard-sized at best)
  Mechanical vibration: distorted image at high speeds

JOHN LOGIE BAIRD (Scotland/England, 1888-1946):
  First to demonstrate working mechanical television (1926)
  First transatlantic TV signal: 1928
  First color TV (mechanical): 1928 (crude)
  First electronic color TV: 1944
  BBC: chose electronic (EMI) system over Baird's mechanical in 1936
  Baird: continued experiments until death; also worked on 3D TV
```

---

## Electronic Television: Farnsworth and Zworykin

```
ELECTRONIC SCANNING: THE KEY INSIGHT

PROBLEM WITH MECHANICAL:
  Mechanical disc: image must be reproduced at exactly the same
  rate the disk scans (all in one plane, one point at a time)
  Physical limits: 200+ lines too fast for disc to spin accurately

ELECTRONIC SOLUTION:
  Replace spinning disc with electron beam
  Electron beam: can be steered by magnetic fields (electromagnets)
  Steering speed: nearly instantaneous (electrons travel at 10-30% c)
  Resolution: limited only by beam focus, not mechanical speed

PHILO FARNSWORTH (1906-1971):
  Idaho farm boy, 14 years old (1920): first conceived CRT scanning
  Idea: electrons could scan image like plowing a field (row by row)
  Patent: filed January 1927 (age 20, San Francisco)
  First working electronic image: September 7, 1927
    First image transmitted: a straight line
    Then: slide with dollar sign (because backers wanted to see money)
  Key patents: image dissector camera tube (1927), electron beam scanning

VLADIMIR ZWORYKIN (1888-1982):
  Russian-American, RCA employee under Sarnoff
  Iconoscope camera tube: patent filed 1923 (disputed dates)
  Kinescope (picture tube): 1929 patent
  RCA: massively funded Zworykin's work ($50M investment)
  Farnsworth vs RCA: patent interference proceedings
  Result (1939): RCA must pay Farnsworth royalties
  (Unusual: RCA almost always won patent battles; Farnsworth = exception)

HOW ELECTRONIC SCANNING WORKS:

  CAMERA TUBE (iconoscope/orthicon/vidicon):
  Scene light -> photosensitive mosaic target
  Electron beam: scans target row by row
  At each point: measures stored charge = scene brightness at that point
  Output: time-varying signal = brightness values in scan order

  PICTURE TUBE (kinescope/CRT):
  Received signal: controls electron beam intensity
  Electron beam: scanned row by row by deflection coils
  Phosphor screen: glows where beam hits
  Brightness = received signal value at that scan point
  Human eye: perceives complete image (scan happens faster than eye integrates)

  SYNCHRONIZATION:
  Camera scan rate must exactly match display scan rate
  Sync pulses: transmitted with video signal
  Display: locked to sync pulses -> always in step with camera
  Without sync: image tears, rolls, scrambles

RCA vs FARNSWORTH RESOLUTION:
  Farnsworth refused to sell: became independent broadcaster
  RCA eventually paid licensing fee (1939)
  WWII: Farnsworth's company diverted to military work
  Post-WWII: Farnsworth sold company (health problems, financial pressures)
  Farnsworth: received very little from television despite foundational patents
  Sarnoff: claimed RCA invented television; this claim was false
  Sarnoff-Farnsworth: one of the great injustices in technology history
```

---

## NTSC, PAL, SECAM Standards

```
ANALOG TV STANDARDS COMPARISON

NTSC (National Television System Committee):
  Adopted: US 1941 (B&W), 1953 (color)
  Also: Japan, most of Americas
  Specs:
    Lines: 525 total, 480-486 visible
    Field rate: 59.94 Hz (interlaced: two fields = one frame)
    Frame rate: 29.97 fps (29.97 ≈ 30 with color subcarrier adjustment)
    Color: 3.58 MHz subcarrier, NTSC color encoding
    Channel bandwidth: 6 MHz
    Aspect ratio: 4:3
  Reputation: "Never The Same Color" (informal)
    Color accuracy: drifted; required hue control on TV sets
    US TVs: had "hue" knob for manual adjustment (European TVs didn't)

PAL (Phase Alternating Line):
  Adopted: UK, Germany, most of Europe 1967
  Also: Australia, China, most of world
  Specs:
    Lines: 625 total, 575-576 visible
    Field rate: 50 Hz
    Frame rate: 25 fps
    Color: 4.43 MHz subcarrier, phase alternation
  "PAL delay line": each line's color information averaged with previous
    Self-correcting: phase errors canceled out by alternation
    Result: better color stability than NTSC
    No hue control needed
  Higher line count: slightly better vertical resolution than NTSC
  50 Hz field rate: matches European power line (avoids flicker from lights)
  60 Hz NTSC: US power line; same reason

SECAM (Séquentiel couleur à mémoire):
  Adopted: France 1967, Russia/Eastern Europe
  Fundamentally different: frequency modulation for color (vs QAM for PAL/NTSC)
  Color: R-Y and B-Y transmitted on alternate lines (not both on same line)
  Needs delay line: stores previous line for simultaneous R-Y + B-Y
  Incompatible: with PAL/NTSC at video signal level
  Political: France chose incompatible standard partly for independence
  Consumer: French TVs can't receive German broadcasts without transcoding
  Legacy: now effectively gone (digital replacement used DVB-T like rest of Europe)

COMPARING STANDARDS:

Feature          | NTSC        | PAL         | SECAM
-----------------+-------------+-------------+---------
Lines visible    | 480-486     | 575-576     | 575-576
Frame rate       | 29.97 fps   | 25 fps      | 25 fps
Power sync       | 60 Hz       | 50 Hz       | 50 Hz
Color stability  | Poor (manual)| Good (auto)| Good (auto)
Bandwidth/channel| 6 MHz       | 8 MHz       | 8 MHz
Hue control      | Yes         | No          | No
Regions          | Americas, JP| Europe, AU  | France, Russia
```

---

## Interlaced vs Progressive Scanning

```
INTERLACED vs PROGRESSIVE

INTERLACED SCANNING:
  Transmit: odd lines, then even lines (two "fields" per frame)
  Field 1: lines 1, 3, 5, 7... (odd lines)
  Field 2: lines 2, 4, 6, 8... (even lines)
  Frame: field 1 + field 2 interleaved

  NTSC: 60 fields/sec = 30 frames/sec
  PAL: 50 fields/sec = 25 frames/sec

  WHY INTERLACED?
  Bandwidth: full-frame at 60fps requires 2x bandwidth
  Interlaced: transmit half the picture each field
              Perceived flicker: at field rate (60 Hz) not frame rate (30 Hz)
              60 Hz > CFF threshold: no perceptible flicker
              But: only half vertical resolution per field

  LIMITATION:
  Interlaced "combing": horizontal detail shows alternating fields
  Fast horizontal motion: "comb" artifact visible
  Deinterlacing algorithms: required for display on progressive screens

PROGRESSIVE SCANNING:
  Transmit all lines in order (1, 2, 3, 4...):
  No interleaving
  Every frame: complete image
  480p: 480 progressive lines (DVD standard)
  720p: 720 progressive lines (HD)
  1080p: 1080 progressive lines (Full HD)
  4K: 2160 progressive lines (UHD)

  Computer monitors: always progressive (better for text)
  Broadcast still uses some interlaced (1080i):
    "1080i60" = 1080 interlaced, 60 fields/sec = 30 frames/sec
    "1080p30" = 1080 progressive, 30 frames/sec (same bandwidth)
    "1080p60" = 1080 progressive, 60 frames/sec (2x bandwidth)

  Streaming and consumer: all progressive
  Broadcast production: 1080i60 still common (matches existing infrastructure)
```

---

## Color Television Technology

```
COLOR TV: HOW IT WORKS

TECHNICAL REQUIREMENT:
  Color signal must be COMPATIBLE with existing B&W sets
  (When color launched 1953, most TVs were B&W)
  Color transmission: B&W sets must show B&W; color sets show color
  Solution: color information encoded SEPARATELY from brightness

LUMINANCE AND CHROMINANCE:
  All color TV standards separate signal into:
  Y: luminance (brightness) - this is what B&W TV uses
  Cb (or U): blue-yellow chrominance difference
  Cr (or V): red-cyan chrominance difference

  YCbCr color space (or YUV, YIQ for NTSC):
  Human eye: more sensitive to brightness than color detail
  Exploit this: transmit Y at full resolution
               Transmit Cb, Cr at lower resolution (chroma subsampling)
  Result: perceptually equivalent quality at lower bandwidth

NTSC COLOR ENCODING:
  Color subcarrier: 3.58 MHz added to existing 4 MHz video bandwidth
  Chosen carefully: subcarrier frequency causes no visible interference with B&W
  QAM modulation: I and Q (in-phase and quadrature) encode Cr, Cb
  Phase of subcarrier: encodes hue
  Amplitude of subcarrier: encodes saturation
  Burst signal: 8-10 cycles of 3.58 MHz at start of each line
    Reference: receiver uses burst to lock to subcarrier phase
    Without correct phase: colors shift (NTSC hue problem)
    Receiver "hue" control: manually adjust phase reference

PAL PHASE ALTERNATION:
  PAL: alternate the phase of color subcarrier each line
  If phase error occurs: error on line N cancels error on line N+1
  Human eye: averages adjacent lines -> error disappears
  Result: no manual hue control needed
  Cost: slightly more complex encoder/decoder circuitry
```

---

## CRT Technology

```
CATHODE RAY TUBE (CRT): HOW IT WORKED

COMPONENTS:
  Electron gun: heated cathode, control grid, focusing anodes
  Deflection system: two pairs of deflection coils (or plates)
  Phosphor screen: coating on inside of glass face

OPERATION:
  Electron gun: emits electron beam from hot cathode
  Control grid: voltage controls beam current (brightness)
  Focusing anodes: electromagnetic lenses focus beam to tiny spot
  Horizontal deflection coil: steers beam left-right
  Vertical deflection coil: steers beam up-down
  Sync circuits: track sync pulses, steer beam to correct position
  Phosphor: glows when hit by electrons; decay time = persistence
  Persistence: short enough for no ghosting, long enough for eye integration

COLOR CRT:
  Three electron guns: R, G, B
  Shadow mask (aperture grille): thin metal screen with tiny holes
  Each hole: aligns with one red, one green, one blue phosphor dot/stripe
  Each gun: aimed at slightly different angle -> hits only its color phosphor
  From viewing distance: R, G, B dots blend -> full color
  Dot pitch: how close dots are; finer = sharper image

CRT ADVANTAGES (still relevant to understand):
  Response time: microseconds (electrons hit phosphor instantly)
  Color: phosphors produce pure spectral colors; excellent gamut
  Viewing angle: perfect (emissive display)
  Black level: turn off beam = true black (no backlight bleed)
  Resolution: analog, variable (scan lines, not pixels)

CRT WEAKNESSES:
  Weight: 25-inch CRT = 35-40 kg
  Depth: 50 cm+ for large screen
  Power: 100-200W typical
  Geometric distortion: requires correction circuits
  Magnetic interference: can cause color purity problems
  High voltage: internal 25,000+ V required for beam acceleration

TRANSITION TO FLAT PANEL (2004-2012):
  LCD: won on size/weight/power; inferior black level + motion response initially
  2005-2010: LCD quality improved enough for consumer acceptance
  2010: CRT production essentially ceased for TVs
  Gaming/video production: some CRT use continues (legacy equipment)
```

---

## Flat Panel Display Technologies

```
FLAT PANEL COMPARISON

LCD (TFT-LCD):
  Backlight: LED array (was fluorescent/CCFL earlier)
  Liquid crystal layer: each pixel = liquid crystal cell
    Liquid crystal: rotates light polarization when voltage applied
    With voltage: blocks backlight (dark)
    Without voltage: passes backlight (bright)
  Color filter: R/G/B filter on each subpixel
  Advantages: thin, light, cheap, good brightness
  Disadvantages: backlight = not true black; limited viewing angle (IPS better)
  IPS (In-Plane Switching): better viewing angles, better color; common

OLED (Organic Light-Emitting Diode):
  Each pixel = tiny organic LED
  Self-luminous: no backlight
  Off pixel = true black (no light emitted at all)
  Advantages: perfect black level, instant response, thin, wide viewing angle
  Disadvantages: burn-in (permanent image persistence if static content),
                 peak brightness limited vs LCD (improves annually)
                 cost (especially large sizes)
  Use: premium TVs, smartphones (iPhone, Samsung AMOLED)

QLED (Quantum LED):
  LCD with quantum dot enhancement layer
  Quantum dots: nanometer-scale crystals that emit specific color wavelengths
  Improves: color gamut and brightness over standard LCD
  Still: LCD fundamentals (backlight, not self-emissive)
  Samsung marketing term; technically: QD-LED or QD-LCD

MicroLED:
  Tiny inorganic LEDs: each pixel = actual LED (like OLED but inorganic)
  Advantages: no burn-in, higher brightness than OLED, similar black level
  Status (2024): very expensive, primarily commercial/large-format
  Apple Vision Pro: micro-OLED per eye (Sony-manufactured), extremely high density — not microLED
  Consumer TVs: expected 2025+ at premium prices
```

---

## Decision Cheat Sheet

| Technology | Era | Key Feature | Limitation |
|-----------|-----|-------------|-----------|
| Nipkow disc | 1884-1937 | Mechanical scanning concept | Low resolution, mechanical speed limits |
| Farnsworth electron scanning | 1927+ | Electronic beam replaces mechanical | Required patent battle with RCA |
| Iconoscope | 1930s | RCA camera tube | Noisy, limited sensitivity |
| NTSC | 1941/1953 | US B&W + color standard, 525 lines | Color instability (hue drift) |
| PAL | 1967 | European color; phase alternation corrects hue | 25fps (50Hz power grid) |
| CRT | 1938-2012 | Perfect black, response time, color | Heavy, deep, high voltage |
| LCD | 2000s-present | Thin, light, cheap | Backlight bleed, viewing angle (improved by IPS) |
| OLED | 2013-present | True black, perfect contrast | Burn-in risk, brightness limit |

---

## Common Confusion Points

**"HDTV is 1080i or 1080p."** Both are called HD, but they're different. 1080i (interlaced, 60 fields/sec) = 30 complete frames/sec. 1080p (progressive, 60 frames/sec) = 60 complete frames/sec. For sports and fast motion, 1080p60 is substantially better. For film content at 24fps, both look essentially the same. "HD" resolution (1080 lines) doesn't specify whether the scan is progressive or interlaced.

**"4K is twice as sharp as 1080p."** 4K (3840x2160) = 4x the pixel count of 1080p (1920x1080) — 2x horizontal, 2x vertical. "Twice as sharp" in both directions. Whether you can see the difference depends entirely on viewing distance and screen size. For a 55-inch screen viewed from 10 feet, 4K vs 1080p is difficult to see. For a 77-inch screen at 5 feet, the difference is visible.

**"OLED TVs always have burn-in."** Modern OLED TVs have pixel shift, screen savers, and compensation algorithms that make burn-in rare for typical TV use. Static HUD elements in video games (health bars, maps) watched for thousands of hours can cause temporary image retention or permanent burn-in. Normal TV viewing with varied content: burn-in is not a practical concern for typical usage patterns and lifespans.

**"The Farnsworth/Zworykin dispute is irrelevant because they both developed TV."** It's historically and morally important: Farnsworth filed key patents first, won the patent interference, and RCA had to pay him. Sarnoff then spent decades claiming RCA invented television and erasing Farnsworth from the official history. The RCA version dominated until the 1970s. This is a significant case in the history of corporate narrative control over technological history.
