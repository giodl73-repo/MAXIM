# Darkroom

## The Big Picture

The darkroom is where **exposed and developed film becomes a final print** — the photographic negative is projected onto light-sensitive paper, chemically processed, and physically fixed. The darkroom gives the photographer control over every tonal parameter of the final image.

```
DARKROOM WORKFLOW:

NEGATIVE (developed film)
     │
     ▼ ─── ENLARGER ─── optical projection
     │     magnifies negative onto easel
     ▼
EXPOSED PAPER (silver halide emulsion on fiber or RC base)
     │
     ▼ ─── DEVELOP ─── same chemistry as film (paper developer)
     │
     ▼ ─── STOP ─── arrest development
     │
     ▼ ─── FIX ─── dissolve unexposed halide
     │
     ▼ ─── WASH ─── remove residual fixer
     │
     ▼ ─── DRY
     │
FINAL PRINT
```

---

## The Enlarger

### Optics and Mechanical Design

```
ENLARGER ANATOMY:

     Lamphouse (light source: diffusion or condenser)
         │
         ▼
     Negative stage (holds negative in carrier)
         │
         ▼
     Enlarging lens (50mm for 35mm; 75mm for 645; 105mm for 4×5)
         │
         ▼
     Easel (holds paper flat; defines white borders)

ENLARGER LENS:
  Image-forming lens optimized for 1:1 to ~20× magnification range
  Aperture: f/2.8–f/5.6 for focusing; f/8–f/11 for printing
  → Same aperture/DoF tradeoff as camera: larger aperture = brighter → easier to
    focus; smaller aperture = sharper (reduced aberrations) but longer exposure
  → Diffraction limit applies: f/22+ makes prints softer; optimal around f/8–f/11
  Lens alignment critical: parallelism of negative, lens board, easel
  → Misalignment → one edge sharp, opposite edge blurry → shimming needed
```

### Light Sources: Diffusion vs Condenser

```
CONDENSER ENLARGERS:
  Collector lens focuses lamp light uniformly through negative
  Produces specular (directional) illumination
  Effect: reveals grain more clearly; higher microcontrast ("acutance")
         Callier effect: silver grain scatters light → extra contrast vs diffusion
  Best for: maximum sharpness; when grain is desired or acceptable

DIFFUSION ENLARGERS:
  Cold-cathode fluorescent, LED matrix, or diffusion box
  Light from all directions through negative
  Effect: grain less visible (light bypasses grain shadow effect)
         Lower contrast baseline → needs higher paper contrast grade
  Best for: portrait printing; hiding grain in high-speed film negatives
  Preferred in professional (fine-art) fiber darkrooms

DICHROIC HEAD (for color printing):
  Three filters (cyan, magenta, yellow) adjustable dials
  Used for variable contrast B&W printing and color printing
  Allows precise filtration without physical filter swapping
```

---

## Photographic Paper

### Paper Types

| Type | Base | Description | Dry-down | Archival |
|------|------|-------------|---------|---------|
| Fiber-based (FB) | Baryta-coated paper | Gelatin emulsion on cotton paper | Significant | Excellent (100+ yr) |
| Resin-coated (RC) | Polyethylene-coated paper | Emulsion on PE-coated paper | Minimal | Good (~50 yr) |
| Baryta (fine art RC variant) | Baryta RC | PE base with barium sulfate layer → FB look | Minimal | Very good |

Dry-down: FB paper appears ~10–15% lighter after drying than when wet. RC paper dries very close to wet appearance. FB printers must account for this.

### Graded vs Variable Contrast Paper

```
GRADED PAPER:
  Fixed emulsion sensitivity; grade number indicates contrast
  Grade 0: extremely soft (very low contrast)
  Grade 2: normal
  Grade 3–4: high contrast
  Grade 5: extreme contrast (soot-and-chalk)
  → Each grade is a separate product; need multiple boxes

VARIABLE CONTRAST (VC) PAPER (Ilford Multigrade, Kodak Polycontrast):
  Two emulsion layers with different sensitivities:
    High-contrast layer: sensitive to blue light
    Low-contrast layer: sensitive to green light
  Filters change the ratio of blue:green reaching paper
    → Yellow filter (removes blue): exposes only low-contrast layer → Grade 0–2
    → Magenta filter (removes green): exposes mainly high-contrast layer → Grade 3–5
    → Dichroic head: dials control magenta/yellow amounts → half-grade steps

PRACTICAL:
  VC paper with filters replaces entire set of graded paper boxes
  Also allows "split-grade printing" (combine two separate exposures at different grades)
  and local contrast control (dodge/burn with different grades)
```

---

## Making a Test Strip and Print

```
PRINT WORKFLOW:

1. FOCUS
   Open lens to maximum aperture (f/2.8–f/4)
   Use grain focuser (magnifier to view grain in projected image)
   Focus on actual grain — not just sharpness of projected image from distance
   Stop lens to printing aperture (f/8–f/11)

2. TEST STRIP
   Cut paper into strip; cover 4/5 with black card
   Expose in increments (e.g., 5s each step)
   Develop fully → observe range of exposures
   Choose correct exposure step

3. DETERMINE CONTRAST GRADE
   If highlights block up (no detail): paper contrast too high; use lower grade
   If shadows have no density: paper contrast too low; use higher grade
   Target: full range from paper maximum black to clean white

4. MAKE PRINT
   Expose at determined time and grade
   Develop for full development time (typically 1.5–2.5 min at 20°C)
   → Vary exposure, NOT development time for density control
   (under-developing for lighter prints = muddy shadows)

5. EVALUATE WET AND DRY
   FB paper: add 10–15% density to compensate for dry-down
   RC paper: wet appearance ≈ dry
```

---

## Zone System for Printing

Adams' zone system applies to printing as well as exposure:

```
ZONE SYSTEM IN PRINTING:

NEGATIVE DENSITY RANGE:
  Shadow detail: thin area of negative (high density on print = dark)
  Highlight detail: dense area of negative (thin area on print = light)

PAPER RESPONSE CURVE:
  Paper has a characteristic curve (like film):
  Toe: shadow region — compressed, dark tones
  Straight portion: midtones — proportional response
  Shoulder: highlight region — compressed, bright tones

PRINTING CONTROLS:
  Exposure → places overall zones on paper
  Contrast grade → stretches or compresses tonal scale
  Dodging/burning → local zone manipulation

FULL SCALE PRINT:
  Maximum black: pure black shadows (Dmax of paper)
  Minimum white: clean paper white (no exposure)
  Midtones: zones III–VII placed by exposure + grade choice
```

---

## Dodging and Burning

Local exposure control — the fundamental creative tool of darkroom printing.

```
DODGING: reducing exposure to LIGHTEN a local area
  Tool: card or paddle on wire; hands; custom shapes cut from card
  Technique: hold between lens and paper during exposure; keep it moving
             to avoid sharp edge
  Effect: lightens the area → reveals shadow detail; brightens overexposed areas
  Adams: dodges dark shadow areas to open them up to Zone II–III

BURNING: increasing exposure to DARKEN a local area
  Tool: card with hole; hands cupped
  Technique: additional exposure after main exposure through hole
             directed only at target area
  Effect: darkens → reduces washed-out highlights; adds drama to skies
  Adams: burned in skies to get Zone VI–VII cloud texture

SPLIT-GRADE PRINTING (VC paper):
  Expose shadows at Grade 5 (hard) for black shadow foundation
  Expose highlights at Grade 0 (soft) for smooth gradation in light areas
  Result: maximum shadow density + gentle highlight rendering
          superior to any single-grade exposure for complex negatives

DODGING/BURNING TECHNIQUE:
  • Keep the tool in motion — any pause creates a visible edge
  • Distance from paper: further = softer edge; closer = sharper
  • A 5-second dodge in a 20-second exposure = 25% reduction
  • Multiple separate burns better than one long
  • Practice on paper you'll discard first
```

---

## Ansel Adams Zone System — Complete Framework

```
THE 11 ZONES (0–X):

Zone   Description                  Subject examples
────────────────────────────────────────────────────────────────
  0    Total black — no detail      Darkest shadows; pure black
  I    Near-black — just off Dmax   Very dark shadows; no discernible detail
  II   Darkest detail               Shadows with just-visible texture
  III  Dark detail clearly visible  Dark foliage, dark wood, shadow under subject
  IV   Dark middle tones            Average dark values; typical shadow on face
  V    Middle gray (18% gray card)  Clear north sky, dark skin in sun, old weathered wood
  VI   Average Caucasian skin       White skin in sun, light sand, snow in shade
  VII  Light textures               Brilliant highlights with texture, near-white fabric
  VIII Light values near white      Very bright areas, light concrete in sun
  IX   Near-white                   Snow in bright sun — just visible texture
  X    Paper white                  Specular highlights, light sources — no detail

PRE-VISUALIZATION:
  Before pressing shutter, Adams would "see" the final print
  → Identify key zones: where does the most important shadow fall? the critical highlight?
  → Meter shadow zones (expose for shadows)
  → Identify if development needs to expand or contract the scale
  → Choose developer and development time to realize the visualization

EXPOSE FOR SHADOWS, DEVELOP FOR HIGHLIGHTS:
  Shadow density on negative is controlled primarily by EXPOSURE
    → Underexpose: lose shadow detail (not recoverable)
    → Overexpose: shadow detail gained, but highlights may block up
  Highlight density on negative is controlled primarily by DEVELOPMENT TIME
    → Overdevelop: highlights block up (no detail in bright areas)
    → Underdevelop: highlights are thin → flat, gray print
    → N-1 development: reduce highlight buildup for contrasty scenes
    → N+1 development: increase highlight contrast for flat, low-contrast subjects

EFFECTIVE FILM SPEED:
  Adams often rated film at half box speed to ensure shadow detail
  ISO 400 film → expose as if ISO 200 (one stop more exposure)
  → Guarantees Zone III or better in important shadows
```

---

## Archival Processing

Silver images are chemically vulnerable to residual fixer (causes yellowing/bleaching) and atmospheric sulfur compounds.

```
ARCHIVAL WASHING:

Fiber-based (FB) paper:
  Fixer penetrates deeply into paper fibers → requires thorough washing
  Standard: 60–120 min in running water (single tray)
  Efficient: Hypercat™, archival washer (separate streams per print)
  Hypo Eliminator / Selenium toner (partial archival): replaces some washing

Resin-coated (RC) paper:
  PE coating prevents deep penetration → 4–6 min wash sufficient
  RC prints: ~50 year archival life under good storage conditions

RESIDUAL FIXER TEST:
  HT-2 Test Solution or KODAK residual hypo test:
  Apply to print → orange stain indicates hypo remaining
  No stain (pale yellow) → archivally washed

SELENIUM TONING:
  Dilute selenium toner (1:9 to 1:20) applied after washing
  Converts silver to silver selenide → more chemically stable
  Also slightly increases Dmax and slightly warms/cools tone depending on paper
  Archival benefit: 2–3× longer estimated life
  Processing silver into a more stable compound is real protection

GOLD TONING:
  Most archival treatment available; extremely stable Au-Ag compound
  Protector: adds very thin gold layer on silver surface
  Very expensive; mostly used for museum-quality master prints

STORAGE:
  pH-neutral, acid-free boxes or mat board
  Separate each print (interleave or sleeve)
  Cool, dark, low humidity (45–55% RH)
  Avoid: sulfur compounds (cardboard, rubber bands, some woods)
```

---

## Contact Printing vs Projection Printing

```
CONTACT PRINTING:
  Negative placed directly on paper surface (emulsion to emulsion)
  Exposed to white light or UV (AZO paper uses UV-contact only)
  Print size = exact negative size
  → Only practical for large format (4×5, 8×10, 11×14)
  → Maximum sharpness: no enlarger lens artifacts, diffraction
  → Adams used 8×10 negatives → 8×10 contact prints → extraordinary sharpness

  AZO paper (no longer manufactured; modern alternative: Lodima Fine Art):
  Very slow ISO ~3 → contact-print-only with floodlights or sunlight
  Near-zero grain artifacts → limited only by negative quality
  Revered for tonality and sharpness by large-format practitioners

PROJECTION PRINTING (enlarging):
  35mm or medium format → enlarged
  Enlarger introduces: lens resolution limit, diffraction, focus alignment issues
  But: practical for most practitioners; flexible sizing
  High-quality enlarging lenses (Schneider Componon-S, Rodenstock Rodagon):
  Very well-corrected for projection distances → near-contact quality at f/8–f/11
```

---

## Decision Cheat Sheet

| Goal | Darkroom choice |
|------|----------------|
| Maximum archival permanence | FB paper + selenium tone + full wash + acid-free storage |
| Maximum sharpness | Large format negative + contact print |
| Flexible tonal control | VC paper + dichroic head + split-grade technique |
| Fine portrait printing | Diffusion enlarger; lower contrast; dodge highlights |
| Landscape with full tonal scale | Condenser enlarger; Adams zone method; burn skies |
| Fastest processing workflow | RC paper (4–6 min wash) |
| Control local density precisely | Dodge/burn + split-grade |
| Calibrate your process | Sensitometry: test strips, step wedge, densitometer |

---

## Common Confusion Points

**Development time controls contrast, not density (primarily)**
Print density is set by exposure. Development time affects contrast (shadow separation) and can push or pull overall density slightly, but developing a print for 30 seconds instead of 2 minutes produces a muddy, gray print — not just a lighter print. Always develop fully; control print lightness/darkness with exposure.

**Zone V is a meter reading, not an absolute value**
A reflected light meter returns a reading that will produce Zone V if used without correction. The meter "sees" middle gray and renders everything it measures as middle gray. Snow in a scene: meter says "give this exposure" → Zone V rendering of snow → Zone V is wrong for snow (should be Zone VIII). You must deliberately place the zone, not just follow the meter.

**Fiber-based paper dry-down is significant and must be planned for**
A wet FB print that looks perfect under safelight will be 10–15% lighter when dry. If you print to the wet tone you want, the final dry print will be too light. Experience is the teacher: add density (extra exposure) knowing it will dry down to your target.

**The Zone System is a discipline for previsualization, not a recipe**
Adams developed the zone system as a framework for consistent creative vision — to help photographers translate what they see into what they want the print to show. It requires calibrating your specific film, developer, camera, paper, and enlarger combination. The exact "zones" for your system are determined by testing, not assumed from tables.

**Dodging and burning are additive, not magic**
You can only work with what's in the negative. If shadow detail was never captured (negative too thin in shadows — underexposure), no amount of dodging will reveal it. If highlights blocked up (negative too dense — overexposure + overdevelopment), burning will only reveal what texture survived. The darkroom refines a well-exposed negative; it cannot rescue a fundamentally flawed one.
