# Vision & Perception — Cones, Opponent Process, Metamerism

## The Big Picture

```
+------------------------------------------------------------------+
|              HOW THE EYE AND BRAIN CONSTRUCT COLOR               |
|                                                                  |
|  STEP 1: RETINAL SAMPLING (photoreceptors)                       |
|  ~6M cones: L (peak 564nm), M (534nm), S (420nm)                 |
|  ~120M rods: single type, peak 498nm, no color discrimination    |
|  → 3D compression: infinite spectrum → 3 numbers (LMS)           |
|                                                                  |
|  STEP 2: OPPONENT ENCODING (horizontal cells → ganglion cells)   |
|  Channel 1: L − M  (red-green axis)                              |
|  Channel 2: (L+M) − S  (yellow-blue axis)                        |
|  Channel 3: L + M + S  (luminance, light-dark)                   |
|  → 3 channels transmitted to brain via optic nerve               |
|                                                                  |
|  STEP 3: CORTICAL PROCESSING (V1, V4, etc.)                      |
|  Color constancy adjustments (for illuminant)                    |
|  Context effects (simultaneous contrast)                         |
|  → Perceptual color experience constructed                       |
|                                                                  |
|  KEY: Color is computed, not measured. The brain is              |
|  solving an inference problem: "given these cone signals,        |
|  what are the likely surface reflectances under this illuminant?"
+------------------------------------------------------------------+
```

---

## The Three Cone Types

```
CONE PHOTOPIGMENTS (opsins):
  Each cone contains one opsin protein + 11-cis-retinal chromophore
  Photon absorbed → retinal isomerizes → opsin changes shape → signal cascade

  L-cone (OPN1LW): peak sensitivity ~564 nm ("red")
  M-cone (OPN1MW): peak sensitivity ~534 nm ("green")
  S-cone (OPN1SW): peak sensitivity ~420 nm ("blue")

  CRITICAL DETAIL: L and M cones are nearly overlapping
  +--------------+------------+------------+-----------+
  |              | L-cone     | M-cone     | S-cone    |
  +--------------+------------+------------+-----------+
  | Peak (nm)    | 564        | 534        | 420       |
  | Overlap      | Heavy L/M overlap       | Separate  |
  | Count        | ~60%       | ~30%       | ~10%      |
  | Density      | Densely packed in fovea            |
  +--------------+------------------------------------+

  IMPLICATION:
  L-M signal (red-green) distinguishes very similar curves → poor for isoluminant
  L+M signal (luminance) is very robust
  S signal (blue-yellow) is separate but coarsely sampled

  Why red-green color blindness is common:
  L and M opsin genes are adjacent on X chromosome → tandem duplication errors
  → X-linked inheritance (8% of males, 0.5% females)
```

---

## Trichromacy (Young-Helmholtz Theory, ~1800-1860)

```
PRINCIPLE:
  Any visible color can be matched by a mixture of three primaries
  → Because there are only 3 cone types, 3 numbers describe any color
  → The CIE XYZ system is the formalization of this

  "Color matching functions": x̄(λ), ȳ(λ), z̄(λ)
  Derived from Guild/Wright experiments (1920s): human observers matched
  monochromatic test lights by mixing three primaries

WHAT TRICHROMACY ENABLES:
  RGB monitors: 3 primaries (R, G, B LEDs/phosphors) can match perceptually
  any color within their gamut → because humans only have 3 cone channels

  A mantis shrimp (16 photoreceptor types) would see through a monitor:
  it would see 16 primaries and know it's looking at a fake.
  For humans with 3 cone types, 3 primaries suffice.

WHAT TRICHROMACY DOESN'T MEAN:
  "Three primaries can reproduce all visible colors" — FALSE
  Three primaries span a triangular gamut on the CIE diagram
  Colors outside the triangle are out-of-gamut → cannot be reproduced
  No set of 3 real primaries covers the full CIE diagram
  (The horseshoe has a curved boundary; triangles only inscribe it)
```

---

## Opponent Process Theory (Hering, 1878)

```
OBSERVATION (Ewald Hering):
  Colors appear in opponent pairs:
  Red vs Green: you can have reddish-yellow, reddish-blue, but not reddish-green
  Yellow vs Blue: you can have yellowish-red, yellowish-green, but not yellowish-blue
  Light vs Dark: luminance axis

  These opponent pairs are mutually exclusive at extremes:
  → "Reddish-green" doesn't exist as a color experience
  → "Yellowish-blue" doesn't exist as a color experience
  (unique hues: red, green, yellow, blue — cannot be "seen in" each other)

NEURAL BASIS (confirmed ~1950s):
  After cones, neurons encode opponent contrasts:

  L − M → RED-GREEN axis
    L > M → signal = red
    M > L → signal = green
    In balance → achromatic (no red-green)

  (L+M) − S → YELLOW-BLUE axis
    L+M > S → signal = yellow
    S > L+M → signal = blue
    In balance → achromatic

  L + M + S → LUMINANCE (brightness)

EXPLAINS:
  1. Afterimages: stare at red → L channel fatigues → see green afterimage
     (opponent neutralized; M channel's baseline perceived as green)
  2. "Unique hues": unique yellow = balance of L/M channels, pure S-stimulation
  3. Simultaneous contrast: gray on red field looks greenish (L-M contrast enhanced)
  4. Why complementary colors "cancel" to gray (additive mixing)
  5. Color blindness phenotypes follow opponent-channel lines
```

---

## Metamerism

```
DEFINITION:
  Two stimuli with DIFFERENT spectral power distributions
  that produce IDENTICAL LMS cone responses
  → Appear identical to a human under given conditions
  → Appear DIFFERENT under different conditions

FORMAL: Two spectral reflectances R₁(λ) and R₂(λ) are metamers if:
  ∫ R₁(λ)·L(λ)·I(λ) dλ = ∫ R₂(λ)·L(λ)·I(λ) dλ  (L-cone match)
  and same for M and S
  Where I(λ) = illuminant SPD

CHANGE THE ILLUMINANT:
  ∫ R₁(λ)·L(λ)·I'(λ) dλ ≠ ∫ R₂(λ)·L(λ)·I'(λ) dλ
  → They no longer match!

INDUSTRIAL PROBLEM:
  Paint batch #1 and batch #2 matched under factory fluorescent
  Customer sees them under incandescent → they look different
  → "Metameric mismatch" — real quality control failure

  Solutions:
  • Measure spectrally (spectrophotometer), not visually
  • Formulate to minimize metameric index (MI)
  • Use same pigments/dyes to minimize divergence

CAMERA METAMERISM:
  Camera sensor (RGB filters) ≠ human L/M/S response curves
  Colors that match visually may not match in camera
  Colors that match in camera may not match visually
  → Why cameras need colorimetric correction matrices

ILLUMINANT METAMERISM IN ART:
  Old masters viewed works by candlelight (~2000K)
  Museums use daylight or 3200K spotlights
  Different illuminants → some colors appear different from intended
  Cannot be fully corrected (the original spectral conditions are unknown)
```

---

## Simultaneous Contrast

```
PHENOMENON:
  The perceived color/lightness of a region depends on its surroundings.

  LIGHTNESS CONTRAST:
  Same gray patch on white background → appears darker
  Same gray patch on black background → appears lighter
  Weber's law operates locally: JND ∝ background luminance

  COLOR CONTRAST:
  Same gray on red background → appears slightly greenish
  Same gray on green background → appears slightly reddish
  Opponent channels: local L-M signal adjusted relative to surround

CHEVREUL (1839) — DISCOVERED FOR TEXTILES:
  Michel Eugène Chevreul at Gobelin tapestry factory
  Noticed adjacent colored threads appeared to shift each other's color
  "De la loi du contraste simultané des couleurs" (1839)
  Influenced Impressionists (Seurat specifically applied Chevreul's principles)

JOSEF ALBERS — INTERACTION OF COLOR (1963):
  Systematic pedagogical exploration: same color appears different in context
  Famous "nested squares" demonstrations
  Yale Bauhaus tradition: perceptual training before color theory

SIMULTANEOUS CONTRAST IN DESIGN:
  Red CTA button on green background: vibration effect, hard to read
  Pure complementary pairings: maximum vibration, usually unpleasant
  Analogous colors: low contrast, harmonious, less demanding
  High-saturation adjacent complements: use in small amounts for accents

"THE DRESS" (2015 INTERNET DEBATE):
  Blue/black dress appearing white/gold to ~30% of people
  → Color constancy failure: ambiguous illumination prior
  People with "outdoor" prior (cool shadow illusion) see blue/black
  People with "indoor" prior (warm light illusion) see white/gold
  Actual dress: blue/black (Lace by Roman)
```

---

## Color Constancy

```
PHENOMENON:
  A white piece of paper looks white under:
  • Midday sunlight (D65, 6500K)
  • Incandescent light (2700K, much more red)
  • Fluorescent office light (3500K, spiky spectrum)

  Despite radically different actual light reaching the eye from that paper.

MECHANISM (Von Kries model, approximate):
  Brain estimates illuminant color from scene statistics
  Divides cone responses by estimated illuminant
  → Normalizes away the illuminant tint
  → Surfaces appear with their "true" color

  More complete models (CIECAM02, etc.) account for:
  • Chromatic adaptation (cone sensitivity gain control)
  • Background/surround effects
  • Luminance level effects (Hunt effect: saturation increases with luminance)

LIMITS OF CONSTANCY:
  • Ambiguous illuminant cues → constancy fails
  • Novel light sources (sodium vapor, monochromatic) → colors desaturate
  • The Dress: ambiguous whether dress is in shadow (cool) or direct light (warm)
  • Works of art under museum lighting ≠ original intended illuminant

ADAPTATION IN PRACTICE:
  Entering dark room: ~20 min dark adaptation (rods adapt)
  Entering bright light: few seconds (cones overwhelmed, then recover)
  Chromatic adaptation: stare at red field → red channel desensitizes →
    white appears greenish briefly → readapts within seconds
```

---

## Color Blindness

```
PREVALENCE:
  Red-green: 8% males, 0.5% females (X-linked)
  Blue-yellow (tritanopia): ~0.01% (autosomal, chromosome 7)
  Complete (achromatopsia): ~0.003% (rod monochromacy)

TYPES:
+------------------+------------------+-------------------------------+
| TYPE             | MECHANISM        | EFFECT                        |
+------------------+------------------+-------------------------------+
| Protanopia       | L-cones missing  | Red-green confusion; reds dim |
| Deuteranopia     | M-cones missing  | Red-green confusion; no lumen |
| Protanomaly      | L-cones shifted  | Reduced red-green             |
| Deuteranomaly    | M-cones shifted  | Reduced red-green (common)    |
| Tritanopia       | S-cones missing  | Blue-yellow confusion         |
| Achromatopsia    | Cones absent     | Grayscale; photophobia        |
+------------------+------------------+-------------------------------+

DESIGN IMPLICATIONS:
  Never use red/green alone for information transmission
  Safe: blue/orange, purple/yellow, colorblind-safe palettes (Okabe-Ito)
  Test with tools: Sim Daltonism, Coblis, browser devtools accessibility

  % of population affected:
  8% of male users cannot distinguish red from green
  For any product with millions of users: millions are red-green blind
  Not an edge case — a large population

ISHIHARA PLATES:
  Standard 38-plate test for red-green CVD
  Pseudoisochromatic: number hidden in colored dot pattern
  Cannot detect blue-yellow CVD (different plates needed)
  Pass rate for protan: ~20% of normal plates; severe = none

TETRACHROMACY (functional):
  ~50% of women are carriers of anomalous L/M opsin gene
  → Some have 4 cone types (two M variants, or L+M variant)
  → True tetrachromats can distinguish colors trichromats cannot
  Psychophysically confirmed in a small number of subjects
  Congenitally color-blind mother → tetrachromat daughter
```

---

## Lightness Perception and Gamma

```
WEBER'S LAW (for lightness):
  Just-noticeable difference (JND) ∝ background luminance
  → Relative, not absolute: need ~2% change to notice at any level

IMPLICATION FOR DIGITAL ENCODING:
  Linear encoding (equal bits per unit luminance):
  → Wastes most bits on bright values (less perceptually useful)
  → Not enough bits for dark values (most sensitive range)

GAMMA ENCODING (perceptual quantization):
  Encode: encoded = linear^(1/γ)  (γ ≈ 2.2 for sRGB)
  Decode: linear = encoded^γ
  → More bits allocated to dark range → fewer visible banding artifacts

  PERCEPTUAL LIGHTNESS (CIE L*):
  L* = 116 × (Y/Yn)^(1/3) − 16  (for Y/Yn > 0.008856)
  → Cube-root transformation of luminance Y
  → Perceptually uniform: ΔL* = 1 ≈ 1 JND throughout range
  → This is why CIELAB is the right space for computing color differences

GAMMA BUG IN 3D RENDERING (very common):
  Problem: texture authored in sRGB (gamma-encoded)
  Mistake: use that texture directly in lighting calculations (linear space needed)
  Result: lighting calculations wrong (too dark in midtones, wrong specularity)
  Fix: gamma-correct (linearize) textures before lighting; re-apply gamma before display
  → Called "linear workflow" or "physically based rendering workflow"
```

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| What are the three cone types and their peak sensitivities? | L (~564 nm), M (~534 nm), S (~420 nm) — massive L/M overlap; S is separate |
| Why don't reddish-green or yellowish-blue colors exist? | Opponent process: L-M and (L+M)-S channels encode these as mutually exclusive axes — simultaneous stimulation of both extremes of an axis = neutralization |
| What is metamerism? | Two different spectral distributions that produce identical LMS cone responses — appear identical under one illuminant, different under another |
| Why do afterimages show the complement? | Cone channel fatigue: stare at red → L-channel desensitized → when viewing neutral surface, M-channel signal predominates → green afterimage |
| What fraction of males are red-green color blind? | ~8% — due to X-linked tandem duplication errors in L/M opsin genes |
| What does "The Dress" illustrate? | Color constancy failure: ambiguous illumination prior — people differ in assumed light source, which changes what color the visual system infers |
| Why does gamma correction exist? | Weber's law: lightness perception is logarithmic. Linear encoding wastes bits on bright values. Gamma encoding (~2.2) redistributes bits toward dark range where perception is most sensitive. |
| What is simultaneous contrast? | Adjacent colors/lightness values shift each other's apparent color/lightness via opponent channel local contrast normalization — Chevreul's (1839) discovery |

---

## Common Confusion Points

**L-cone = "red cone" is misleading:** The L-cone peaks at 564 nm (yellow-green range, not red). It's called "L" because it's the LONG wavelength cone. It responds strongly to red, but its peak isn't red. The L-M difference signal (not L alone) encodes the red-green axis.

**Color blindness severity varies:** "Red-green color blindness" covers a spectrum: from mild anomalous trichromacy (shifted cones, slightly reduced discrimination) to complete dichromacy (missing cone class, major confusion). Deuteranomaly (shifted M-cone) is the most common form and relatively mild.

**Metamerism isn't failure:** Metamers are unavoidable in any 3-channel recording/display system. The goal isn't to eliminate metamerism but to engineer for the right illuminant (matching metamers under the expected viewing conditions).

**Color constancy isn't perfect:** The brain's illuminant estimate can be wrong. Colored lights in theaters, unusual LED spectra, or scenes with only one hue can fool constancy. Photographers know to set white balance; the brain does it automatically but imperfectly.
