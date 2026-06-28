---
maxim_schema: maxim.frontmatter.v1
id: maxim:computer-graphics:color-and-perception
kind: guide
module: computer-graphics
section: computer-graphics
title: Color and Perception
status: source-custody
source_custody: partial
current_path: computer-graphics/08-COLOR-AND-PERCEPTION.md
canonical_path: computer-graphics/08-COLOR-AND-PERCEPTION.md
backsource_ids: [proof-backfill:computer-graphics:08-color, git-history:computer-graphics:08-color]
concepts: [color space, gamma, srgb, linear light, hdr, tone mapping, color management]
root_concepts: [color, perception]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# Color and Perception

## The Big Picture: Light Is Linear, Displays and Eyes Are Not

The single most consequential fact in rendering color: **lighting math must happen in
linear light**, but **storage and display are perceptually (gamma) encoded**. Getting the
encode/decode boundaries wrong is the most common correctness bug in graphics. This guide is
the bridge to `colors/` — that directory covers the full science of color; here we cover
exactly what a renderer must get right.

```
+--------------------------------------------------------------------------------------+
|                  THE COLOR PIPELINE (where linear vs encoded matters)                |
|                                                                                      |
|  DECODE          SHADE              EXPOSURE/         TONE MAP        ENCODE         |
|                  (linear)           HDR                                              |
|                                                                                      |
|  sRGB texture --> linear lighting --> HDR radiance --> map HDR -> --> sRGB / PQ      |
|  -> LINEAR       (BRDF, sum lights,   (values may      LDR        encode for         |
|  light           blend, filter --     exceed 1.0)      [0,1]      the display        |
|                  ALL in linear!)                                                     |
|                                                                                      |
|   [L2 decode]    [L1 linear math]    [L3 HDR]         [L4 tonemap]  [L2 encode]      |
+--------------------------------------------------------------------------------------+
```

Read left to right: decode inputs to linear, do *all* math in linear, then (for HDR) tone-map
the unbounded result back into the display's range and re-encode. Filtering, blending,
mipmapping, antialiasing — every average — is only correct in linear light.

---

## Layer 1: Why Lighting Must Be Linear

Light is **additive and linear**: two photons deliver twice the energy of one; combining two
light sources adds their radiances. The rendering equation (`04`) sums and integrates
radiance, so it is only valid on linear quantities.

```
  LINEAR LIGHT:  intensity 0.5 means HALF the photons of 1.0.
                 0.5 + 0.5 = 1.0    (two half-lights make a full light)  ✓

  If you do that math on GAMMA-ENCODED values, it's WRONG:
     encoded 0.5 represents ~0.21 linear (sRGB).
     averaging two encoded 0.5s gives 0.5 (encoded) = 0.21 linear...
     ...but the true average of the lights is 0.21 linear -> encode -> 0.5. (ok here)
     The bug shows on MIXED values: average of black(0) and white(1):
        in encoded space: (0 + 1)/2 = 0.5 encoded = 0.21 LINEAR  -> looks too DARK
        correct (linear):  (0 + 1)/2 = 0.5 LINEAR  = 0.73 encoded -> proper mid-gray
```

```
  THE CLASSIC BUG: dark fringes on antialiased edges / blurry mips

     averaging a white and a black pixel IN GAMMA SPACE -> too-dark gray
     -> AA edges look dirty, downsized images darken, alpha blends muddy
     FIX: decode to linear, average, re-encode.
```

This is why correct engines configure textures and framebuffers as sRGB so the hardware
auto-decodes on read and auto-encodes on write — the shader sees pure linear values.

---

## Layer 2: Gamma, sRGB, and the Encode/Decode Boundary

Human vision is roughly logarithmic — we discriminate dark tones far more finely than bright
ones. **Gamma encoding** exploits this to pack perceptually uniform steps into limited bits
(8 bits especially), devoting more codes to the shadows where the eye is sensitive.

```
  GAMMA / sRGB ENCODING (approx, the real sRGB curve has a small linear toe):

     encoded = linear ^ (1/2.2)      (store: brighten shadows -> more codes there)
     linear  = encoded ^ 2.2         (display/decode: undo it)

  WHY: with 8 bits, a pure-linear encoding would waste codes on highlights the eye
  can't distinguish and BAND the shadows visibly. Gamma spreads the codes to match
  perception -> smooth gradients in 8 bits.

     linear:   |..............................| (codes bunched bright, banding dark)
     sRGB:     |   .   .   .   .   .   .   .   | (codes spread to match the eye)
```

```
  WHERE TO DECODE / ENCODE (the rule):

   sRGB COLOR data (albedo, photos)      -> DECODE to linear before use
   LINEAR data (normals, roughness,      -> DO NOT decode (it was never encoded)
     metalness, depth, AO)
   final framebuffer for an SDR display  -> ENCODE to sRGB on write

   Hardware "sRGB texture/framebuffer formats" do this automatically and CORRECTLY
   (the decode happens BEFORE filtering, so mips/AA average in linear).
```

The `colors/09-DIGITAL-COLOR.md` guide covers gamma's perceptual basis in depth; the
renderer's job is just to keep the boundaries straight: decode color inputs, compute in
linear, encode outputs.

---

### Why Three Channels: Trichromacy and Metamerism

RGB is not arbitrary — it is a consequence of human eyes having exactly three cone types.

```
  THE RETINA has 3 cone types, sensitive to LONG / MEDIUM / SHORT wavelengths (L,M,S).
  Any spectrum is collapsed to just 3 numbers (the cone responses) before the brain.

  -> METAMERISM: two PHYSICALLY DIFFERENT spectra that produce the same (L,M,S) look
     IDENTICAL. This is the entire basis of color reproduction:
        a display emits only 3 primaries (R,G,B), yet can MATCH a continuous spectrum
        because it only needs to match the three cone responses, not the spectrum.

     real rainbow spectrum  ─┐
                              ├─> same (L,M,S) ─> same perceived color
     R+G+B from a monitor   ─┘
```

This is why three channels suffice and why a gamut is a *triangle* (three primaries spanning
a plane in the cone space). It also bounds what's reproducible: colors outside the primaries'
triangle have no nonnegative R,G,B mix — they are simply unreachable on that display, which is
what "out of gamut" means. The full perceptual story is in `colors/02-VISION-PERCEPTION.md`;
the renderer just needs to know that matching three responses, not spectra, is the whole game.

## Layer 3: Color Spaces and Gamuts

A **color space** is a choice of primaries (which red/green/blue), a white point, and a
transfer function (gamma curve). Same RGB triple, different space → different physical color.

```
  GAMUT = the triangle of colors a set of primaries can reproduce (in CIE xy):

     sRGB / Rec.709    the web/SDR standard; smallish triangle
     Display-P3        wider (Apple displays, DCI cinema-ish); ~25% more area
     Rec.2020          very wide (HDR/UHD target); few displays cover it fully
     ACEScg            huge working space for film compositing (AP1 primaries)

     CIE xy diagram (horseshoe = all visible colors):
            .-''''-.
          .'  2020  '.      sRGB is a SMALL triangle inside the visible horseshoe;
         /  .--P3--.  \     wider spaces enclose more real colors but need the
        | / sRGB  \  |      display + the whole pipeline to support them.
         \ '------'  /
          '.________.'
```

The CIE 1931 `XYZ` system (covered in `colors/03-COLOR-SYSTEMS.md`) is the device-independent
reference all these spaces convert through — a 3×3 matrix maps any RGB space's primaries to
`XYZ` and back, so color management is, at heart, a chain of linear-algebra basis changes
(plus the nonlinear transfer functions). **Old world → new world:** converting between color
spaces is a change of basis in `XYZ` — the learner's linear algebra, applied to perception.

---

### Bit Depth and Banding

Encoding interacts with *precision*. Gamma exists largely to make **8 bits** enough; deeper
buffers relax the requirement.

```
   8-bit  (256 levels/channel)  sRGB-encoded -> just enough for SDR; banding in smooth
                                gradients if you do linear math then re-quantize to 8-bit
   10-bit (1024 levels)         HDR10 displays; far less banding; Rec.2020 + PQ
   16-bit half-float            HDR RENDER targets (the linear working buffer; values >1)
   32-bit float                 depth, accumulation, GPGPU

   BANDING: too few codes across a gradient -> visible steps. Mitigate with DITHER
   (add sub-LSB noise before quantizing) -> trades banding for imperceptible noise.
```

The lesson for a renderer: keep the *working* buffer in 16-bit float linear (so lighting
sums and HDR highlights have headroom), and only quantize to 8/10-bit *after* tone-mapping
and encoding, ideally with a dither. Quantizing to 8-bit mid-pipeline is how banding creeps
into otherwise-correct color.

## Layer 4: HDR and Tone Mapping

Real scenes span an enormous dynamic range — a sunlit cloud is ~100,000× brighter than a
shadow. Linear shading (`04`) naturally produces radiance values **far above 1.0**. **HDR
rendering** keeps them in floating-point; **tone mapping** then compresses that unbounded
range into the display's limited output.

```
  HDR RENDERING:
     shade in floating-point linear -> values can be 0 .. thousands (no clamping yet)

  EXPOSURE:
     scale by an exposure factor (like a camera's aperture/ISO) -> chooses what's
     "middle gray" before compression (often auto-exposure from scene luminance)

  TONE MAPPING:  map [0, inf) -> [0, 1] for the display (an S-curve, like film)

     naive CLAMP:  min(x, 1)   -> highlights blow out to flat white (ugly)
     Reinhard:     x / (1 + x) -> simple, desaturates highlights
     filmic / ACES -> film-like S-curve; preserves highlight color & contrast (standard)

     output       1 |        _____------  (ACES rolls off highlights gracefully)
     (display)      |     _/
                    |   /
                  0 |_/______________ input radiance (linear, unbounded)
```

```
  HDR DISPLAY OUTPUT (when the panel itself is HDR):
     encode with the PQ (Perceptual Quantizer, SMPTE ST 2084) or HLG curve instead
     of sRGB, in Rec.2020, signalling absolute nits to the display.
     -> tone-map to the display's actual peak luminance, not a fixed 1.0.
```

Tone mapping is doing for *luminance* what gamma does for *encoding*: compressing a range the
medium can't reproduce into one it can, shaped to perception. The order is strict: shade
linear → expose → tone-map → encode. Tone-mapping before linear shading, or encoding before
tone-mapping, both produce wrong color.

---

### Chromatic Adaptation and White Balance

The eye *adapts*: a white sheet looks white under noon daylight (~6500 K) and under a tungsten
bulb (~3000 K), even though the physical spectra differ wildly. A renderer must account for
the **white point** of its lighting, or whites come out tinted.

```
  WHITE POINT: the chromaticity the pipeline treats as "neutral white".
     D65  (~6500 K)  the sRGB / Rec.709 / Rec.2020 standard white (daylight)
     D50  (~5000 K)  print / graphic-arts standard

  CHROMATIC ADAPTATION: convert colors from one white point to another so neutrals
  stay neutral. The standard method (Bradford transform) is a 3x3 matrix applied in
  a cone-response ("LMS") space:

     XYZ --M_Bradford--> LMS --scale by (dest white / src white)--> LMS' --inverse--> XYZ'

  This is the rendering analogue of CAMERA WHITE BALANCE: re-neutralize the dominant
  illuminant so the scene reads correctly.
```

For physically based rendering this matters when lights have color temperature: a warm
interior lamp tints everything, and either you embrace it (artistic intent) or adapt it out
(neutral grade). Either way it is, again, a change of basis — into the cone-response space,
scale, and back — the same linear-algebra spine as every other color conversion.

## Layer 5: The Full Color-Correct Pipeline

```
  ASSET (sRGB albedo)  --decode-->  LINEAR
  ASSET (normal/rough) --as is-->   LINEAR (never encoded)
                                       |
                        all lighting math (BRDF, sum lights,        [04]
                        blend, filter, mipmap, AA) IN LINEAR        [05]
                                       |
                                   HDR radiance (floating-point, unbounded)
                                       |
                                   exposure  (scene -> usable range)
                                       |
                                   tone map  (HDR -> display range; ACES filmic)
                                       |
                          +------------+------------+
                          |                         |
                      SDR display               HDR display
                      encode sRGB               encode PQ/HLG, Rec.2020
                      [0,1], 8-bit              absolute nits, 10-bit+
```

Every stage that *averages* values (filtering, mip generation, MSAA resolve, alpha blend)
must sit in the linear region. The two failure modes are (1) doing those averages in encoded
space (dark fringes, muddy blends) and (2) clamping HDR to `[0,1]` before tone mapping
(blown-out highlights). A correct pipeline is mostly bookkeeping discipline about *which side
of the encode boundary* each operation lives on.

---

## Worked Example: The Gamma-Space Averaging Bug

Resolve an antialiased edge: a pixel half-covered by white, half by black. Display values are
sRGB-encoded `white = 1.0`, `black = 0.0`.

```
  WRONG (average in encoded/sRGB space):
     result = (1.0 + 0.0) / 2 = 0.5 (sRGB)
     decode to check perceived linear: 0.5^2.2 ~ 0.218 linear
     -> the eye sees a gray that is only ~22% of full brightness: TOO DARK.
        Edges look like they have a dark halo.

  RIGHT (decode -> average -> encode):
     decode: white 1.0 -> 1.0 linear ; black 0.0 -> 0.0 linear
     average: (1.0 + 0.0)/2 = 0.5 LINEAR     (genuinely half the light: correct)
     encode for display: 0.5^(1/2.2) ~ 0.73 sRGB
     -> stored value 0.73, which the display decodes back to 0.5 linear. Proper mid-gray.

  Difference: 0.73 vs 0.50 stored -> a very visible error. This is exactly why
  AA edges, downscaled images, and alpha blends look dirty without linear handling.
```

The same arithmetic explains why an image downscaled in a naive image editor looks darker
than the original: every box-filter average happened in gamma space.

---

## Old World → New World Bridges

| You already know | Here it is |
|------------------|-----------|
| Change of basis | Color-space conversion through CIE XYZ (3×3 matrices) |
| Linearity required for superposition | Lighting math valid only in linear light |
| Log-scale to match perceived magnitude | Gamma encoding matches the eye's response |
| Fixed-point precision allocation | Gamma spreads 8-bit codes to where the eye is sensitive |
| Range compression / companding | Tone mapping: unbounded HDR → display range |
| sRGB/gamma in `colors/09-DIGITAL-COLOR` | Same curve, here as a render-pipeline boundary |
| Normalization vs raw data | sRGB color (decode) vs linear data maps (don't) |

---

## Decision Cheat Sheet

| Situation | Choice |
|---|---|
| Sampling an albedo/photo texture | sRGB sampler — decode to linear |
| Sampling normal/roughness/metal/AO | Linear sampler — no decode |
| Doing lighting / blending / filtering | In linear light, always |
| 8-bit storage of a color | Encode to sRGB (gamma) for code efficiency |
| Output to a normal monitor (SDR) | Tone-map → encode sRGB `[0,1]` |
| Output to an HDR display | Tone-map to peak nits → encode PQ/HLG, Rec.2020 |
| Compressing bright HDR highlights | ACES/filmic tone-map curve (not clamp) |
| Wide-gamut authoring (film) | Work in ACEScg / Display-P3 |
| Edges/mips look dirty or dark | You're averaging in gamma space — switch to linear |

---

## Common Confusion Points

### "If I just store and display sRGB, why convert to linear at all?"

Because *math* on color — lighting, blending, filtering, averaging — is only correct on
linear values, and sRGB is a nonlinear encoding. Storage and display want sRGB (perceptual,
bit-efficient); computation wants linear (physically additive). You decode in, compute
linear, encode out. Skipping the decode produces the dark-fringe/muddy-blend family of bugs.

### "Gamma 2.2 vs sRGB — same thing?"

Almost. The sRGB transfer function is approximately a 2.2 power curve but has a small *linear
segment* near black (to avoid an infinite slope at zero) and uses ~2.4 in its exponent
overall. For most purposes "gamma ≈ 2.2" is fine; for precision (and to match hardware sRGB
formats), use the exact sRGB piecewise function. Treating them as identical causes tiny
shadow errors.

### "Why does my downscaled image look darker than the original?"

Because the downsampler averaged pixels in gamma space. Each box average of encoded values
yields a too-dark linear result (the same bug as AA edges). Decode to linear, downsample,
re-encode and it matches. Many image tools historically got this wrong.

### "HDR rendering vs HDR display — same thing?"

No. **HDR rendering** means shading in floating-point linear so radiance can exceed 1.0 — you
do this even when outputting to a normal SDR monitor (you tone-map down at the end). **HDR
display** means the panel itself reproduces a wide luminance range, encoded with PQ/HLG. You
can render HDR and output SDR; an HDR display just changes the final encode and tone-map
target.

### "Is tone mapping just clamping bright values?"

No — clamping (`min(x,1)`) blows highlights to flat white and shifts their color. Tone mapping
applies a smooth S-curve (filmic/ACES) that rolls highlights off gracefully, preserving
contrast and hue the way film stock does. The distinction is very visible: clamped skies are
flat white blobs; tone-mapped skies retain color and gradient.
