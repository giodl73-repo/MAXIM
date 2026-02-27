# Digital Color — Bit Depth, ICC Profiles, Gamma, HDR

## The Big Picture

```
+------------------------------------------------------------------+
|           THE DIGITAL COLOR MANAGEMENT PIPELINE                  |
|                                                                  |
|  CAPTURE → ENCODE → STORE → PROCESS → DELIVER → DISPLAY        |
|                                                                  |
|  Camera sensor                                                   |
|    ↓ RAW (device-specific spectral sensitivities)               |
|  Color matrix correction → linear scene-referred XYZ            |
|    ↓                                                             |
|  Convert to working color space (sRGB / AdobeRGB / ProPhoto)    |
|    ↓                                                             |
|  Apply gamma encoding (sRGB TRC or log curve)                    |
|    ↓                                                             |
|  Store: JPEG/PNG (sRGB assumed) or TIFF/DNG (profile embedded)  |
|    ↓                                                             |
|  Edit: must linearize for correct math → re-encode for export   |
|    ↓                                                             |
|  ICC profile conversion: source profile → destination profile   |
|    ↓                                                             |
|  Display: output profile applied → physical light emitted       |
|                                                                  |
|  EVERY STEP HAS A FAILURE MODE if done without profile awareness |
+------------------------------------------------------------------+
```

---

## Bit Depth

```
BIT DEPTH: bits per channel (not per pixel)
  Common formats are specified per channel (R, G, B each get N bits)

8-BIT PER CHANNEL:
  256 levels per channel (2⁸)
  Total: 256 × 256 × 256 = 16,777,216 colors (~16.7M)
  Storage: 3 bytes per pixel (RGB) + 1 for alpha → 4 bytes
  JPEG, PNG, most consumer images: 8-bit
  Sufficient for: display delivery, most web content
  Problem: BANDING — visible steps in smooth gradients (sky gradient, skin tone)
    → Banding appears when bit depth insufficient for transition
    → More visible after edit operations (gamma, curves) that stretch values

10-BIT PER CHANNEL:
  1,024 levels per channel (2¹⁰)
  Total: ~1.07 billion colors
  Used for: HDR video streaming (Netflix, Apple TV+), HDR displays
  Formats: HEVC (H.265) with 10-bit, AV1 10-bit, DV (Dolby Vision)
  Eliminates most banding in HDR/WCG content

12-BIT PER CHANNEL:
  4,096 levels per channel (2¹²)
  Used in: RAW photo formats (most DSLRs), Dolby Vision 12-bit spec
  Most RAW converters work in 12 or 14 bits per channel

16-BIT PER CHANNEL:
  65,536 levels per channel (2¹⁶)
  Used in: professional photo editing workflow (Photoshop 16-bit mode)
  Avoids accumulation of rounding errors during multi-step edit
  Float vs integer 16-bit:
  • Integer 16-bit (uint16): 0–65535, fixed range
  • Half-precision float (float16): ~6 decimal digits, ±65504, scientific notation range
  TIFF (16-bit), PSD (16-bit): common archival formats

32-BIT FLOAT:
  ~7-8 decimal digits of precision
  Range: essentially unlimited (−10^38 to 10^38)
  Used in: compositing (OpenEXR), 3D rendering (intermediate buffers)
  Physically based rendering requires 32-bit float for HDR scene-referred data
  OpenEXR format (Industrial Light & Magic, 1999): 16-bit or 32-bit float per channel,
    arbitrary channel counts, standard for VFX/animation

BANDING ARTIFACT:
  Visible steps in gradient when encoding precision is too low
  Appears: sky gradients, skin tones, slow fades
  Workaround: add small amount of noise (dithering) before quantization
  → Breaks up systematic steps → less visually objectionable
  → Photoshop "Export As" PNG: dithering checkbox for this reason
```

---

## Gamma Encoding

```
THE PROBLEM (perceptual quantization):

Linear encoding (equal bits per unit luminance):
+-------+-------+-------+-------+-------+-------+-------+-------+
|  0    | 1/8L  | 2/8L  | 3/8L  | 4/8L  | 5/8L  | 6/8L  | 7/8L  |
+-------+-------+-------+-------+-------+-------+-------+-------+
→ Equal luminance steps
→ Human vision: JND in dark = MUCH smaller than JND in bright
→ Dark region uses 1/8 of bits for many visible steps
→ Bright region uses 1/8 of bits for few visible steps
→ WASTED: too many bits on bright values, not enough on dark

Gamma-encoded (sRGB):
+-------+-------+-------+-------+-------+-------+-------+-------+
| 0^2.2 |(.125)^|(.25)^ |(.375)^|(.5)^  |(.625)^|(.75)^ |(.875)^|
+-------+-------+-------+-------+-------+-------+-------+-------+
                              (each ^(1/2.2) before storage)
→ More code values allocated to dark range (where sensitivity is high)
→ Fewer code values allocated to bright range (where sensitivity is low)
→ Same perceptual quality with fewer bits (or better quality same bits)

THE sRGB TRANSFER FUNCTION:
  Encode: V_encoded = 12.92 × V_linear          (for V_linear ≤ 0.0031308)
          V_encoded = 1.055 × V_linear^(1/2.4) − 0.055  (otherwise)
  Decode: V_linear = V_encoded / 12.92           (for V_encoded ≤ 0.04045)
          V_linear = ((V_encoded + 0.055) / 1.055)^2.4   (otherwise)

  Effective gamma: ~2.2 across the full range (the linear segment near black
  raises the effective exponent slightly; hence "sRGB ≈ gamma 2.2")

  KEY POINT:
  • sRGB values 0-255: ENCODED (gamma-compressed), NOT linear light
  • rgb(128, 128, 128) is NOT 50% luminance
    → Actual luminance: 128/255 → after decode: ((128/255+0.055)/1.055)^2.4 ≈ 0.216
    → 128 encoded gray = ~21.6% luminance (not 50%)
  • rgb(186, 186, 186) ≈ 50% luminance gray (because 186^2.2 / 255^2.2 ≈ 0.5)
```

### The Gamma Bug in 3D Rendering

```
THE CLASSIC MISTAKE:
  Diffuse texture stored as sRGB JPEG (encoded)
  Renderer samples texture → uses encoded value directly in lighting math
  → Math: encoded_value × light_intensity → wrong (operating in gamma space)
  → Result: too dark in midtones, incorrect specular response

CORRECT LINEAR WORKFLOW:
  Texture (sRGB encoded) → linearize (decode gamma) → lighting calculation
  → result in linear space → re-apply sRGB gamma → display
                                    ↑
                              This is the step often missed

  In PBR shaders:
  • Albedo texture: usually authored in sRGB → must linearize ("sRGB" sampler flag)
  • Normal maps: NOT gamma-encoded (already linear) → must NOT linearize
  • Roughness/Metallic: NOT gamma-encoded (data, not color) → must NOT linearize
  Mixing these up produces subtle but visible rendering errors

UNITY/UNREAL: both have "Linear rendering" and "Gamma rendering" modes
  Linear rendering = correct physically based mode
  Gamma rendering = legacy mode for old projects
  → Default since ~2014: linear (correct)

WebGL: SRGB_EXT or WebGL2 sRGB framebuffer handling
THREE.js: renderer.outputEncoding = THREE.sRGBEncoding (legacy) →
          renderer.outputColorSpace = THREE.SRGBColorSpace (current)
```

---

## Color Spaces and ICC Profiles

```
COLOR SPACE HIERARCHY (in order of increasing gamut):
  sRGB (1996) < AdobeRGB (1998) < Display P3 (2015) < Rec.2020 < ProPhoto RGB

sRGB:
  Primaries: R(0.64, 0.33), G(0.30, 0.60), B(0.15, 0.06) in CIE xy
  White point: D65 (x=0.3127, y=0.3290)
  Transfer function: sRGB (≈ γ2.2)
  Coverage: ~35% of CIE 1931 gamut
  Use: consumer monitors, internet, delivery

Adobe RGB (1998):
  Primaries: R(0.64, 0.33), G(0.21, 0.71), B(0.15, 0.06)
  White point: D65
  Transfer function: γ = 2.199 (close to 2.2)
  Coverage: ~50% of CIE 1931 gamut (especially expanded green)
  Use: professional photography, print preparation (Epson printers use wide-gamut)
  IMPORTANT: If no profile is embedded, viewer assumes sRGB → AdobeRGB appears washed out
  → Always embed profile when sharing AdobeRGB images

Display P3:
  Primaries: R(0.680, 0.320), G(0.265, 0.690), B(0.150, 0.060)
  White point: D65
  Transfer function: sRGB (same as sRGB)
  Coverage: ~45% of CIE gamut
  Use: Apple devices (iPhone 7+, MacBook 2016+, iPad Pro 2016+)
  CSS: color(display-p3 1 0 0) = P3 red

Rec.2020:
  Primaries: near-monochromatic (R 700nm, G 532nm, B 467nm)
  Coverage: ~76% of CIE gamut
  Use: UHD HDR broadcast, HDR streaming standard
  Problem: no display achieves 100% Rec.2020

ProPhoto RGB:
  Covers ~91% of CIE gamut (includes colors humans can't see)
  Use: archival RAW editing only
  Risk: most colors are imaginary/invisible; editing requires care

ICC PROFILES:
  ICC: International Color Consortium (established 1993)
  Profile: describes a device's color behavior (input or output)

  PROFILE TYPES:
  Input (scanner, camera): describes how device maps scene to numbers
  Display (monitor): describes display's actual primaries and white point
  Output (printer): describes printer's color gamut for ink/paper combination
  Colorspace (abstract): defines a standard space (sRGB.icc, AdobeRGB1998.icc)

  CMS (Color Management System): converts between profiles
  • macOS: ColorSync
  • Windows: Windows Color System (WCS) / ICM
  • Photoshop: embedded CMS using ICC v4

  WORKFLOW:
  Image with embedded sRGB profile → open in Photoshop (knows it's sRGB)
  → Convert to working space (e.g., ProPhoto for editing)
  → Edit (all in high-bit linear)
  → Export: convert to output profile (sRGB for web, printer profile for print)
  → Embed output profile in exported file
```

---

## HDR (High Dynamic Range)

```
SDR vs HDR:
  SDR (standard dynamic range):
  • Maximum luminance: ~100-200 nits (display dependent)
  • Black level: ~0.1 nit (ideally)
  • Dynamic range: ~1000:1
  • Transfer function: gamma (sRGB/Rec.709)
  • Content: 8-bit, sRGB/Rec.709 gamut

  HDR:
  • Maximum luminance: 400-10,000 nits (display spec dependent)
  • Black level: ~0.001-0.005 nit (OLED) or 0.01-0.1 nit (LCD with local dimming)
  • Dynamic range: up to 1,000,000:1 (OLED with peak highlights)
  • Transfer functions: PQ or HLG
  • Content: 10-bit minimum, Rec.2020 container (actual gamut may be less)

PQ (Perceptual Quantizer, SMPTE ST 2084):
  Dolby-developed; absolute luminance reference
  0 = 0 nit, max = 10,000 nits
  Non-backward-compatible with SDR (SDR display shows PQ as very dark)
  Used in: HDR10, Dolby Vision, HDR10+
  PQ transfer function: designed to match human visual sensitivity
    → Unlike gamma (power law), PQ uses a specific perceptual model

HLG (Hybrid Log-Gamma, BBC/NHK):
  Backward-compatible with SDR
  Lower portion of signal (0-0.5): SDR gamma → plays on SDR display normally
  Upper portion (0.5-1.0): log curve → HDR information
  Used in: broadcast (UK, Japan, some streaming)
  Trade-off: less headroom than PQ; simpler implementation; works without metadata

HDR FORMATS:
+------------------+-------+--------+----------+-----------------------+
| FORMAT           | BITS  | GAMUT  | METADATA | USAGE                 |
+------------------+-------+--------+----------+-----------------------+
| HDR10            | 10    | Rec.2020| Static   | Universal baseline    |
| HDR10+           | 10    | Rec.2020| Dynamic  | Samsung, Amazon       |
| Dolby Vision     | 12    | Rec.2020| Dynamic  | Netflix, Apple TV+    |
| HLG              | 10    | Rec.2020| Implicit | Broadcast, BBC        |
+------------------+-------+--------+----------+-----------------------+

STATIC vs DYNAMIC METADATA:
  Static: single tone-mapping curve for entire film
  Dynamic: per-scene or per-frame tone-mapping guidance
  → Dynamic better for content with extreme luminance variation
  → Dolby Vision (dynamic) shows better highlight/shadow retention per scene

TONE MAPPING:
  HDR content → SDR display (or lower-spec HDR): must compress dynamic range
  HDR content on target display: content may exceed display's actual capabilities
  Tone mapping operators:
  • Reinhard: simple, global; no loss of detail but crushes highlights
  • ACES: film industry standard; handles very wide range gracefully
  • Display manufacturer: each TV has proprietary tone mapping (causes content differences)
  → Same HDR file can look very different on different HDR displays (no standardization below Dolby Vision)
```

---

## Color in CSS and Web

```
CSS COLOR EVOLUTION:
  CSS 1-2: #RRGGBB hex, rgb(r, g, b) — sRGB integers
  CSS 3: rgba(), hsl(), hsla() — hue/saturation/lightness
  CSS Color Level 4: wide-gamut, HDR, LAB/LCH, OKLab/OKLCh
    → Standardized in browsers ~2023

CURRENT CSS COLOR FUNCTIONS:
  #RRGGBB / #RRGGBBAA         — hex, sRGB
  rgb(r, g, b) / rgba()       — sRGB, 0-255 or 0%-100%
  hsl(h, s, l) / hsla()       — sRGB polar (intuitive manipulation)
  hwb(h, w, b)                — hue/whiteness/blackness (new in Level 4)
  lab(L, a, b)                — CIELAB (perceptually uniform, D50 white)
  lch(L, C, H)                — CIE LCh (cylindrical Lab)
  oklab(L, a, b)              — OKLab (more uniform than CIELAB, modern)
  oklch(L, C, H)              — OKLCh polar (most recommended modern space)
  color(display-p3 r g b)     — Display P3 gamut
  color(srgb r g b)           — sRGB normalized 0-1
  color(srgb-linear r g b)    — Linear sRGB (no gamma)
  color(rec2020 r g b)        — Rec.2020 (ultra-wide gamut)
  color(xyz r g b)            — CIE XYZ
  color(xyz-d65 r g b)        — CIE XYZ with D65 white point

HSL CAVEATS:
  hsl(H, S, L): intuitive for manipulation (adjust L for brightness, S for saturation)
  BUT: not perceptually uniform
  → hsl(180, 100%, 50%) (cyan) appears much lighter than hsl(240, 100%, 50%) (blue)
    at the "same" 50% lightness
  → OKLCh: oklch(L, C, H) is perceptually uniform and now preferred

OKLCH RECOMMENDATION (2023+):
  OKLab (Björn Ottosson, 2020): better perceptual uniformity than CIELAB
  Especially: better hue linearity (blue doesn't purple-shift when adjusted)
  oklch(L, C, H): L = 0-1, C = 0-0.4ish, H = 0-360°
  → Adjust L without hue shift
  → Predictable chroma scaling
  → Use for: CSS custom properties, palette generation, color manipulation APIs

BROWSER SUPPORT STATUS (~2024):
  All modern browsers (Chrome 111+, Firefox 113+, Safari 15.4+) support:
  • lab(), lch(), oklab(), oklch()
  • color() with p3, srgb-linear, rec2020, xyz
  color-mix(): mix two colors in a specified color space
  → color-mix(in oklch, blue 60%, red 40%): 60% blue + 40% red in OKLch space
  → Result differs by color space (oklch mixes through vivid colors; hsl through gray)
```

---

## Color in 3D Rendering and Photography

```
RAW WORKFLOW:
  Camera RAW: 12-14 bit linear data (before demosaicing/gamma)
  → White balance: multiplicative per-channel correction
  → Demosaicing: interpolate full RGB from Bayer/X-Trans pattern
  → Color matrix: camera-specific XYZ → output space conversion
  → Tone curve: apply gamma or log encoding
  → JPEG: bake in gamma, reduce to 8-bit, embed sRGB profile
  → DNG/RAW: preserve pre-bake state; edit non-destructively later

  White balance in RAW:
  • Daylight (D65): ~1.0× red, ~1.0× green, ~2.0× blue multipliers (typical)
  • Tungsten (2700K): ~0.6× red, ~1.0× green, ~2.5× blue (compensate warm light)
  → Changing WB in RAW: just changes multipliers; no quality loss
  → Changing WB in JPEG: lossy reinterpretation (already baked)

PHYSICALLY BASED RENDERING (PBR):
  REQUIRES LINEAR SPACE for all lighting calculations
  Disney Principled BSDF (Burley, 2012): industry-standard material model
  Parameters:
  • Basecolor: surface albedo (sRGB texture → must linearize)
  • Metallic: 0=dielectric, 1=metal (linear map, not color → don't linearize)
  • Roughness: 0=mirror, 1=completely diffuse (linear map)
  • Normal map: XYZ directions encoded as RGB → do not gamma-correct

  Fresnel reflectance (Schlick approximation):
  F(θ) = F₀ + (1-F₀)(1-cosθ)⁵
  F₀ = base reflectance at normal incidence
    → Metals: F₀ = 0.5-1.0 (colored)
    → Non-metals (dielectrics): F₀ = 0.02-0.08 (colorless, depends on n)

TONE MAPPING FOR RENDERS:
  Scene-referred (HDR) → display-referred (SDR or HDR)
  ACES (Academy Color Encoding System):
    • Input Transform (IDT): convert camera data to ACES
    • Reference Rendering Transform (RRT): ACES → output
    • Output Transform (ODT): for specific display
    • Standard in VFX/animation (used in Unreal Engine 4+)
  Filmic tone mapping (Blender default): S-curve; lifts shadows, compresses highlights
  Reinhard tone mapping: L' = L/(L+1) — global, simple, no loss
```

---

<!-- @editor[content/P2]: CIECAM02 appears in the colors/00-OVERVIEW.md module architecture diagram as "COLOR APPEARANCE MODELS: CIECAM02 and successors" but never appears in any guide in this section. 09-DIGITAL-COLOR.md covers ICC profiles and rendering intents, which are the direct application context for CIECAM02 (it is the foundation for the iCAM and CAM02 rendering intents in high-end ICC workflows). A brief section on color appearance models — what CIECAM02 adds over CIELAB (viewing conditions: luminance adaptation, surround, background contrast), why it matters for cross-media matching (print at 2000 lux vs screen at 200 lux), and the OKLab lineage (OKLab was designed as a practical approximation of CIECAM16/ZCAM JMh space) — would close this gap and tie together the entire module map. -->
## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| Why is rgb(128,128,128) not 50% gray? | sRGB is gamma-encoded. 128/255 after gamma decoding: ((128/255 + 0.055)/1.055)^2.4 ≈ 21.6% luminance. 50% luminance gray ≈ rgb(186,186,186). |
| What causes banding in gradients? | Insufficient bit depth — visible quantization steps in smooth transitions. Fix: 16-bit editing workflow; add dithering noise before export to 8-bit. |
| When should I use OKLCh instead of HSL in CSS? | When color manipulation needs to be perceptually uniform: OKLCh adjusting L doesn't shift hue; HSL's L is not perceptually uniform (cyan at 50% L appears much lighter than blue at 50% L). |
| What is the "gamma bug" in 3D rendering? | Using sRGB-encoded (gamma) texture values directly in lighting calculations (which need linear light). Result: incorrect midtone darkness, wrong specularity. Fix: decode gamma before lighting; re-encode for output. |
| When to use HDR10 vs Dolby Vision? | HDR10: universal baseline, static metadata. Dolby Vision: dynamic per-scene metadata → better highlight/shadow retention. Netflix/Apple TV+/Disney+ all offer DV where available. |
| What ICC rendering intent for photos? | Perceptual: compresses all colors, preserves relationships — best for photographs with large gamut. Relative Colorimetric: only clips out-of-gamut — best for logo/spot colors. |
| What is Display P3 and when does it matter? | Apple's wide-gamut display standard (iPhone 7+, MacBook 2016+). ~26% wider than sRGB. Use color(display-p3) in CSS for P3-native content on Apple devices. |

---

## Common Confusion Points

**"sRGB" can mean the color space or the transfer function:** sRGB has specific primaries (color space) AND a specific transfer function (~γ2.2). Display P3 uses sRGB's transfer function with different primaries. Rec.2020 uses PQ or HLG transfer function. These are separable properties that happen to share names.

**HDR display ≠ HDR content:** A display can claim HDR certification (e.g., "HDR400") while showing SDR content tone-mapped to the display's capability. True HDR requires both HDR-mastered content AND an HDR-capable display. Most "HDR" budget displays show very little improvement over SDR because their peak brightness is insufficient.

**Adobe RGB and sRGB look identical on a non-wide-gamut display:** If your display can't show the wider green of Adobe RGB, the two spaces appear identical. The extended gamut only manifests on a wide-gamut display. JPEG files tagged as Adobe RGB but displayed without color management on a system assuming sRGB appear desaturated/washed-out — this is a common mistake when sharing images.

**OKLCh is not yet in Photoshop (as of 2024):** Photoshop still uses traditional L*a*b* (CIELAB). OKLCh/OKLab is in CSS (all modern browsers) and in Figma (2023). The improved uniformity of OKLab matters most for programmatic color manipulation and palette generation — in manual editing, the difference from Lab is subtle.
