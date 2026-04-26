# Film Chemistry

## The Big Picture

Photographic film is a **chemical amplifier**: a few photons create a latent image (a few silver atoms), and development amplifies that by a factor of 10⁸–10¹⁰ to produce a visible silver image. The remarkable sensitivity comes from this extreme amplification.

```
EXPOSURE → LATENT IMAGE → DEVELOPMENT → VISIBLE IMAGE

  Photon hits AgBr crystal
      ↓ ~10 photons sufficient for latent image
  Silver atom cluster (Ag₃–Ag₆) forms at sensitivity speck
      ↓ development amplifies ×10⁸
  Entire silver halide crystal reduced to opaque metallic silver
      ↓
  Black metallic silver grain visible in negative
```

---

## Silver Halide Crystals

### Why Silver?

Silver (Ag) is uniquely suited for photography:
- Ag⁺ ions in ionic crystal lattice
- AgBr, AgCl, AgI all photoactive — absorb UV/visible light → photoelectron
- Ag metal is opaque (black in microcrystalline form)
- Ag⁺ → Ag⁰ is electrochemically reversible → fixable with thiosulfate
- Quantum efficiency of latent image formation: ~1 electron per 20 photons absorbed

### Halide Selection

| Halide | Inherent sensitivity | Color sensitivity | Common use |
|--------|---------------------|------------------|-----------|
| AgCl | Low (UV only) | Blue-UV | Low-speed papers; contact printing |
| AgBr | Medium | Blue + some green | Most black-and-white film |
| AgI | High (when added to AgBr) | Extends to green | AgBrI: high-speed emulsions |
| AgBrI | Highest | Needs spectral sensitization | Modern high-speed films |

### Crystal Structure and Grain Morphology

```
SILVER BROMIDE CRYSTAL STRUCTURE:
  Face-centered cubic (rock salt type)
  Ag⁺ and Br⁻ alternate in 3D lattice
  Crystal defects are critical: Frenkel defects (Ag⁺ in interstitial position)
  Mobile Ag⁺ ions → migrate to sensitivity specs during development

GRAIN EVOLUTION (by annealing history during manufacture):
  Cubic crystals: slow emulsions, fine grain
  Tabular grains (T-grains, Kodak 1982 innovation):
    High aspect ratio plates (width/thickness > 5:1)
    Same AgBr mass but larger surface area
    → Better light absorption per grain
    → Faster (more sensitive) without larger overall grain size
    → Better sharpness (thinner emulsion layer possible)
    Kodak T-MAX, Fuji Neopan 400 Crystal are T-grain emulsions

Grain size vs speed vs grain appearance:
  Fine grain (sub-micron): slow (ISO 50–100), fine-grained prints, high resolution
  Medium grain: ISO 100–400, balanced
  Large grain: ISO 800–3200, visible grain texture, impressionistic rendering
```

---

## Latent Image Formation: The Gurney-Mott Mechanism (1938)

R.W. Gurney and N.F. Mott's quantum-mechanical model explains how a few photons produce a stable latent image.

```
STEP-BY-STEP MECHANISM:

1. PHOTON ABSORPTION:
   hν absorbed by AgBr crystal
   Br⁻ → Br⁰ + e⁻ (electron promoted to conduction band)

2. ELECTRON TRAPPING:
   Conduction-band electron migrates through crystal
   Trapped at sensitivity speck (surface defect, often Ag₂S from sulfur sensitization)
   Sensitivity speck becomes negatively charged

3. ION MIGRATION:
   Attracted Ag⁺ (interstitial Frenkel defect) migrates to speck
   Ag⁺ + e⁻ → Ag⁰ (neutral silver atom)
   Single Ag atom unstable — often re-ionizes

4. GROWTH OF SILVER CLUSTER:
   Second photon event → second Ag⁰ at same speck
   Two Ag atoms = more stable
   Continue: Ag₂ → Ag₃ → Ag₄
   At ~3–4 atoms: latent image speck is stable (threshold)

5. LATENT IMAGE COMPLETE:
   Ag₃–Ag₆ cluster at sensitivity speck = latent image
   Crystal with speck: DEVELOPABLE (will be fully reduced by developer)
   Crystal without speck: NOT developable

AMPLIFICATION FACTOR:
  10 photons → 4–5 Ag atoms in latent image
  Development → reduces entire crystal (~10⁹ Ag atoms) to metallic Ag
  Amplification: ~10⁸

THERMAL INSTABILITY:
  AgBr crystals can slowly reverse: Ag⁰ re-ionizes → latent image fades
  Reciprocity failure: very long exposures → same light hitting same spot
  → Frenkel defects migrate away → less efficient trapping
  → Film needs 1–3 stops extra exposure for multi-second exposures
```

### Spectral Sensitization

Pure AgBr is only sensitive to UV and blue (< ~500nm). The visible spectrum needs chemical dyes adsorbed to grain surfaces.

```
SPECTRAL SENSITIZATION DYES:
  Cyanine dyes adsorbed to Ag halide surface
  Dye absorbs light at its characteristic wavelength
  → excited dye molecule → electron → conduction band of AgBr
  → proceeds as normal Gurney-Mott mechanism

EVOLUTION OF COLOR SENSITIVITY:
  Orthochromatic: UV + Blue + Green sensitized (still no red)
  Panchromatic: UV + Blue + Green + Red — full visible spectrum
               → First used widely: 1926; standard from 1930s
  Extended red / infrared: sensitized into 700–900nm (Kodak HIE)

DESENSITIZATION by development room safelight:
  Orthochromatic film: can be developed under red safelight (red blind)
  Panchromatic film: must be developed in complete darkness
```

---

## The Development Process

### Developer Chemistry

Development is **selective chemical reduction**: the developer reduces Ag⁺ → Ag⁰, but only in crystals that have latent image speeks (the Ag cluster acts as a catalyst for reduction). Unexposed crystals are not reduced at normal development times.

```
DEVELOPER REDUCING AGENT:
  Developing agents are organic molecules that donate electrons to Ag⁺

  Most common:
  • Metol (p-methylaminophenol, Kodak Elon): fast-working, fine grain
  • Hydroquinone (1,4-dihydroxybenzene): high contrast, coarse grain
  • Phenidone: superadditive with hydroquinone; sharper results
  • Pyrocatechin (catechol): staining developer; used for UV-cut for AZO printing
  • Ascorbate: "vitamin C developer" — low toxicity, effective

SUPERADDITIVITY (synergism):
  Metol alone: moderate activity
  Hydroquinone alone: sluggish
  Metol + Hydroquinone (MQ): far more active than either alone
  Mechanism: hydroquinone regenerates oxidized metol (semiquinone exchange)
  D-76 and most film developers are MQ or PQ formulas

DEVELOPER COMPONENTS:
  Developing agent: Metol + Hydroquinone (or Phenidone + HQ)
  Preservative:    Sodium sulfite (Na₂SO₃) — prevents aerial oxidation of developer
                   Also acts as solvent for silver halide → fine grain effect
  Accelerator:    Sodium or potassium carbonate (pH ~9–10)
                   or borax (pH ~8.5 for fine grain)
                   Alkaline pH needed for development activity
  Restrainer:     Potassium bromide (KBr)
                   Prevents fog (development of unexposed crystals)
```

### Development Sequence: Developer → Stop → Fix

```
STEP 1: DEVELOPER (developing agent reduces Ag⁺ → Ag⁰ in exposed crystals)
  D-76 (Kodak), HC-110, Rodinal, XTOL, ID-11
  Temperature control critical: 20°C ± 0.1°C for consistent results
  Agitation: ensures fresh developer contacts emulsion
  Time: typically 6–15 minutes
  Controlled by: time × temperature × dilution × agitation

STEP 2: STOP BATH (arrest development)
  Dilute acetic acid (1–2%) — neutralizes alkaline developer rapidly
  Without stop: overdevelopment as developer drains
  Plain water rinse: acceptable for prints, less reliable for film

STEP 3: FIXER (sodium thiosulfate — dissolves unexposed Ag halide)
  Na₂S₂O₃ + AgBr → [Ag(S₂O₃)₂]³⁻ (water-soluble silver thiosulfate complex)
  Removes unexposed silver halide → image becomes stable, no longer light-sensitive
  Ammonium thiosulfate (rapid fixer): 1–2 min for film vs 5–10 min sodium
  Over-fixing: thiosulfate attacks developed silver → bleached, reduced density

STEP 4: WASH (remove fixer)
  Residual fixer causes slow browning of image (oxidation of Ag)
  Archival wash: 20 min running water; or hypo clear → wash for permanence
  Hypo Clear (sodium sulfite wash): exchanges fixer for easily-washed compound

STEP 5: DRY
  Photoflo (wetting agent): reduces surface tension → no drying marks
```

---

## Zone System — Adams' Visualization Framework

Ansel Adams (with Fred Archer) formalized a system for metering, exposure, and development control in B&W photography.

```
ZONE SYSTEM: 11 zones (0–X) from pure black to pure white

  Zone 0:   Solid black (no detail) — shadows below exposure threshold
  Zone I:   Near-black with slight texture
  Zone II:  First visible shadow detail
  Zone III: Dark shadow textures clearly visible
  Zone IV:  Average dark skin, dark foliage
  Zone V:   Middle gray (18% gray card — camera meter reference)
  Zone VI:  Average Caucasian skin in diffuse light
  Zone VII: Bright highlights with texture
  Zone VIII: Very bright, near-featureless highlights
  Zone IX:  Just-visible texture in near-white
  Zone X:   Pure white (no detail)

KEY INSIGHT: Exposure places zones; development controls their separation

  Expose for shadows (you can't add detail to underexposed film)
  Develop to control highlight density (development affects highlights most)

  N development:   normal (EI = box speed)
  N+1 development: increase contrast (expand tonal range)
  N-1 development: decrease contrast (compress tonal range)
  → Useful in flat or very contrasty lighting

Pre-visualization: "see" the final print tones before pressing shutter
  → Choose exposure and development to realize that vision
```

---

## Color Film Chemistry

Black-and-white film is conceptually simple (silver); color film is chemically elaborate.

### Color Negative Film (C-41 Process)

Color negative film has **three emulsion layers** sensitized to different colors, with couplers that form dyes during development.

```
LAYER STRUCTURE (cross-section):
  ┌─────────────────────────────────────────────────────┐
  │  Protective overcoat                                │
  ├─────────────────────────────────────────────────────┤
  │  Blue-sensitive layer + yellow dye coupler           │
  │  (yellow filter dye layer prevents blue below)       │
  ├─────────────────────────────────────────────────────┤
  │  Green-sensitive layer + magenta dye coupler        │
  ├─────────────────────────────────────────────────────┤
  │  Red-sensitive layer + cyan dye coupler              │
  ├─────────────────────────────────────────────────────┤
  │  Anti-halation layer (black)                        │
  │  Polyester base (0.1–0.15mm)                        │
  └─────────────────────────────────────────────────────┘

DYE COUPLING DEVELOPMENT (C-41):
  CD-4 color developer (para-phenylenediamine derivative)
  Develops silver AND activates dye coupler:
    Oxidized developer + coupler → colored dye
    Yellow (where blue was absorbed), Magenta (green), Cyan (red)

  After color development: bleach-fix (blix)
    Bleach converts Ag⁰ → Ag⁺ (usually ferricyanide or persulfate)
    Fix dissolves Ag⁺ (thiosulfate)
    → Only the dye image remains (silver removed)

COLOR NEGATIVE:
  Orange cast: orange mask corrects for impure dye absorption
  (Cyan and magenta dyes also absorb some blue/green → mask compensates)
  Negative in color: yellow where scene was blue, magenta where green, cyan where red
```

### Kodachrome — The Exceptional Case

Kodachrome (1935–2010) used a completely different system with no couplers in the film itself.

```
KODACHROME UNIQUE SYSTEM:

Film layers: 3 silver halide layers, NO COUPLERS IN FILM

Development process (K-14):
  1. Black-and-white develop all 3 layers (conventional B&W)
  2. Reexpose only red-sensitive layer (from bottom with red light)
  3. Color develop red layer → cyan dye forms (couplers in developer, not film)
  4. Reexpose only blue-sensitive layer (from top with blue light)
  5. Color develop blue layer → yellow dye
  6. Fog remaining layer (green-sensitive) chemically
  7. Color develop → magenta dye
  8. Bleach-fix → remove all silver → pure dye image

Why Kodachrome had exceptional properties:
  • No couplers in film → thinner emulsion layers → better sharpness
  • Extremely stable dyes (inorganic couplers in developer)
  • Archival stability: 100+ years without significant dye fade
  • Limitation: process complexity → only Dwayne's Photo (closed 2010) for last years

Why it was discontinued:
  • K-14 process uses benzene-derivative developers → toxic, expensive to handle
  • Digital captured its market
  • Last roll processed: December 30, 2010
```

### E-6 / Ektachrome / Fujifilm Reversal Film

Color reversal (slide) film: positive image directly on the film.

```
E-6 PROCESS:
  1. First developer: black-and-white develop all layers
     (exposed silver halide → Ag⁰)
  2. Reversal: remaining unexposed halide fogged chemically or by light
  3. Color developer: forms dyes in fogged (formerly unexposed) areas
  4. Bleach + fix: remove all silver
  5. Result: positive dye image where original scene had highlights/colors

KEY DIFFERENCE FROM NEGATIVE:
  Slide film has very narrow exposure latitude (~3–5 stops vs 12+ for neg)
  Overexpose → washed out highlights (no orange mask correction available)
  Underexpose → shadow detail lost immediately
  Must meter precisely — made photographers disciplined
```

---

## Film Speed and Grain

```
ISO/ASA FILM SPEED:
  Based on the exposure (H, in lux-seconds) needed to produce a defined density
  ISO 400: needs 1/4 the light of ISO 100 for same density
  Technical definition: ISO 100 → H = 1/100 lux·s at the defined point

SPEED-GRAIN-SHARPNESS TRADEOFF:
  Higher ISO = larger crystals = less resolution + more visible grain
  Acutance: edge sharpness (how abruptly density changes at an edge)
  Resolution: how fine a repeating pattern can be distinguished
  Grain: macro-texture visible in large prints

Modern fast film compromises:
  T-grain design (Kodak T-MAX, Fuji Acros): tabular grains → fast but finer grain
  Fuji Acros 100: arguably best sharpness/grain balance in modern film
  Kodak Tri-X 400: classic cubic grain — more visible grain, loved aesthetically

PUSH PROCESSING:
  Expose at higher ISO than rated → shorter exposure time
  Compensate: longer development (N+1 or N+2)
  Effect: increased grain, increased contrast, loss of shadow detail
  Useful: low light without changing lens; aesthetic grain effect
```

---

## Decision Cheat Sheet

| Goal | Film choice / process |
|------|----------------------|
| Maximum sharpness, fine grain | ISO 25–100 fine-grain (Rollei RPX 25, Adox Silvermax) |
| Balanced quality, versatile | ISO 100–400 T-grain (Kodak T-MAX 100/400, Fuji Acros) |
| Available light, artistic grain | ISO 400–3200 (Kodak Tri-X, Ilford HP5, Delta 3200) |
| Best archival color slides | E-6 reversal (Fuji Velvia, Ektachrome) |
| Widest exposure latitude, most forgiving | Color negative (Portra 400, Fuji 400H) |
| Maximum archival dye stability | Color neg (Kodak Portra) or scan+digital preserve |
| Fine-grain developer, classic look | D-76 or XTOL (dilute) |
| Acutance / sharpness over grain | Rodinal (highly dilute, compensating) |
| Speed increase without quality loss | T-MAX developer with T-MAX film |

---

## Common Confusion Points

**The Gurney-Mott mechanism requires a minimum number of photons**
A single photon is not enough to create a stable latent image. Below ~3–4 photons per grain (forming a ~3-atom Ag cluster), the latent image is unstable and fades. This is the physical basis of reciprocity failure: very dim light (each grain rarely hit) + very long exposure = less efficient than the math predicts.

**Development increases contrast, not just density**
D-76 at normal dilution vs dilute (1:1) gives different gradient (gamma) relationships. Overexposure + underdevelopment (N-1) produces a thick-based, low-contrast negative. Underexposure + overdevelopment (N+1) produces a thin, high-contrast negative. These are distinct manipulations.

**Kodachrome is not the same as Ektachrome**
Kodachrome had no couplers in the film; its unique dye stability required the extremely complex K-14 process. Ektachrome (E-6) has couplers in the film — processable at home or in commercial labs. The dye stability of E-6 is significantly less than Kodachrome. This is why Kodachrome archivists weep.

**Film grain is silver, not dye**
In B&W film, the visible grain in a developed negative is metallic silver. In color film after processing, the silver is bleached out entirely — what you see is the dye image. Color film grain is effectively dye cloud size, which correlates with original silver grain size but is not the same thing.

**Fixing is not just stopping development**
Fixing does two distinct things: (1) dissolves unexposed silver halide (making the image stable in light), and (2) removes it from the emulsion. Under-fixing leaves invisible residual silver halide that will slowly darken in light. Over-fixing attacks the developed silver image. The endpoint is when the "clearing time" is reached (when the milky undeveloped halide clears visually) — then continue for the same time again.
