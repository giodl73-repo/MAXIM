---
maxim_schema: maxim.frontmatter.v1
id: maxim:computer-graphics:texturing-and-sampling
kind: guide
module: computer-graphics
section: computer-graphics
title: Texturing and Sampling
status: source-custody
source_custody: partial
current_path: computer-graphics/05-TEXTURING-AND-SAMPLING.md
canonical_path: computer-graphics/05-TEXTURING-AND-SAMPLING.md
backsource_ids: [proof-backfill:computer-graphics:05-texturing, git-history:computer-graphics:05-texturing]
concepts: [UV mapping, texture filtering, mipmaps, aliasing, antialiasing, sampling theorem, MSAA, SSAA]
root_concepts: [texturing, sampling]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---

# Texturing and Sampling

## The Big Picture: Painting Detail, Then Fighting Aliasing

Textures store per-point surface data (color, normals, roughness) in an image, mapped onto
geometry via UV coordinates. The moment you sample a texture — or rasterize an edge — you
are doing *signal sampling*, and the sampling theorem governs everything that follows. Half
this guide is mapping data on; the other half is preventing the aliasing that sampling
causes.

```
+--------------------------------------------------------------------------------------+
|                     TEXTURING + SAMPLING PIPELINE                                    |
|                                                                                      |
|  AUTHOR          MAP             SAMPLE          FILTER           ANTIALIAS          |
|                                                                                      |
|  texture     --> UV coords   --> fetch texels --> magnify /    --> edge AA (MSAA)    |
|  image          per vertex       at (u,v)        minify          + texture AA        |
|  (color/        (unwrap)         per fragment     - bilinear      (mipmaps)          |
|   normal/                                         - trilinear     + temporal (TAA)   |
|   PBR maps)                                       - anisotropic                      |
|                                                                                      |
|   [L1]           [L1 UV]         [L2 fetch]       [L3 filter]     [L4 mip] [L5 AA]   |
+--------------------------------------------------------------------------------------+
```

The throughline is the **sampling theorem** (`signal-processing/`): a signal must be
band-limited to below half the sampling rate (Nyquist) or high frequencies *alias* into low
ones. Textures viewed at a distance, and geometric edges, are full of frequencies above
Nyquist — so we either pre-filter (mipmaps) or supersample (MSAA/SSAA).

---

## Layer 1: UV Mapping — Geometry to Texture Space

Each vertex carries a 2D **texture coordinate** `(u, v)` in `[0, 1]²`. The rasterizer
interpolates UVs across the triangle (perspective-correct, `02`), and the fragment shader
fetches the texel there.

```
   3D MESH SURFACE                TEXTURE SPACE (UV)
   ---------------                ------------------
        /\                         (0,1) +--------+ (1,1)
       /  \   each vertex                |  the   |
      /    \  -> a (u,v)                 | unwrap |
     /______\                            |  image |
                                   (0,0) +--------+ (1,0)

   "UV unwrapping" = flattening the 3D surface onto the 2D image without too much
   distortion (like peeling an orange flat). Seams are unavoidable on closed surfaces.
```

UVs aren't only for color. The same mechanism delivers a *stack* of maps that drive PBR
shading (`04`):

```
  ALBEDO / BASE COLOR   the diffuse color           (sRGB-encoded -> decode to linear!)
  NORMAL MAP            per-texel surface normal     (tangent space; linear data)
  ROUGHNESS / METAL     microfacet params for PBR    (linear data)
  HEIGHT / DISPLACEMENT geometric detail             (parallax or real displacement)
  AO MAP                baked ambient occlusion       (linear)
```

A subtlety that matters for correctness: **color maps are sRGB-encoded** and must be
decoded to linear before lighting math; **data maps (normal/roughness/AO) are linear** and
must *not* be gamma-decoded. Mixing this up is a pervasive bug — see `08`.

---

## Layer 2: The Sampling Problem

A texture is a discrete grid of texels; the screen is a discrete grid of pixels; they
rarely line up. Two regimes:

```
  MAGNIFICATION  (texture too small for screen area: one texel -> many pixels)
     problem: blocky / blurry. fix: interpolate between texels (bilinear).

  MINIFICATION   (texture too big: many texels -> one pixel)   <-- the dangerous one
     problem: ALIASING. one pixel covers many texels but samples only one
              -> shimmering, moiré, crawling patterns as the camera moves.
```

```
  WHY MINIFICATION ALIASES (the sampling theorem):

  far-away textured surface -> high spatial frequency at the pixel grid
  one sample per pixel -> sampling rate fixed
  frequencies above NYQUIST (half the pixel rate) fold back as FALSE low frequencies

     true signal  /\/\/\/\/\/\   (high freq, e.g. a fine grid receding to horizon)
     sampled at   .   .   .   .  (too coarse)
     reconstructed ~~~~~~~        (a bogus low-freq pattern = MOIRÉ / shimmer)

  Fix options: (a) raise the sampling rate (supersample), or
               (b) BAND-LIMIT the signal first (pre-blur) -> mipmaps.
```

This is identical to the aliasing in audio/DSP (`signal-processing/`): the cure is the same
two choices — sample faster, or low-pass filter before sampling.

---

## Layer 3: Texture Filtering

How to compute a texel value when the sample point lands between texels (magnification) or
spans many texels (minification).

```
  NEAREST       pick closest texel             blocky; cheapest
  BILINEAR      weighted avg of 4 texels       smooth magnification; 1 mip level
  TRILINEAR     bilinear on 2 mip levels +     smooth across mip transitions
                interpolate between them        (no visible mip "banding")
  ANISOTROPIC   sample along the projected      sharp textures at GRAZING angles
                footprint (multiple taps)        (roads, floors viewed edge-on)
```

```
  WHY ANISOTROPIC FILTERING EXISTS:

  A pixel's footprint on a surface viewed at a grazing angle is a long, thin ellipse,
  not a square. Trilinear assumes a square footprint -> picks a blurry high mip ->
  the floor goes mushy in the distance. Anisotropic takes several samples ALONG the
  long axis of the footprint, keeping it sharp.

     pixel footprint on a floor seen edge-on:   [=================]  (long ellipse)
     trilinear samples: one blurry square        [###]  -> over-blurred
     anisotropic: many taps along the ellipse    [=][=][=][=][=]    -> sharp
```

---

### Wrap Modes and Beyond Color

A `(u, v)` outside `[0, 1]` needs an addressing rule, and textures carry far more than color.

```
  WRAP / ADDRESS MODES (what happens outside [0,1]):
     REPEAT     tile the texture (u mod 1) — for surfaces with repeating detail
     CLAMP      hold the edge texel — avoids seams on a decal/gradient
     MIRROR     reflect each tile — hides the repeat seam
     BORDER     a fixed border color outside the range

  TEXTURE DIMENSIONS:
     2D         the common case (surfaces)
     CUBE MAP   6 faces of a cube — environment maps, reflections, point-light shadows
     3D         a volume (u,v,w) — clouds, LUTs (a 3D color-grading lookup, 08), noise
     ARRAY      a stack of 2D layers indexed by an integer — material atlases, CSM cascades
```

The cube map deserves note: it samples by a *direction* vector (not a 2D coordinate),
picking the face and texel a ray would hit on a surrounding cube — exactly what reflection
and image-based lighting (`04`) need to look up "what's in this direction." A 3D texture is
how a color grade ships as a single LUT (`08`) the GPU samples per pixel.

## Layer 4: Mipmaps — Pre-Filtering for Minification

A **mipmap** is a precomputed pyramid of the texture at successively halved resolutions,
each level a band-limited (averaged-down) version of the one above. At render time the GPU
picks the level whose texels roughly match the pixel footprint — sampling a *pre-blurred*
image instead of undersampling a sharp one.

```
   MIP PYRAMID (each level = previous averaged 2x2 -> 1)

     level 0:  512 x 512   (full detail; used up close)
     level 1:  256 x 256
     level 2:  128 x 128
     ...                    GPU computes the right level from the UV
     level 9:    1 x 1      derivatives (du/dx, dv/dx) across the pixel quad
                            -> "how fast are UVs changing per pixel?" = footprint size

   Memory cost: +1/3 of the base texture (geometric series 1 + 1/4 + 1/16 + ... = 4/3).
```

The level-of-detail `λ` is chosen from the **UV derivatives** the GPU computes per 2×2 pixel
quad: faster-changing UVs (surface receding, minified) → higher (blurrier) mip. This is the
*band-limiting* option (b) from Layer 2: instead of sampling a high-frequency signal too
coarsely, sample a pre-low-passed version at the matching rate. Mipmapping is why distant
textures shimmer *without* it and sit calm *with* it. Trilinear filtering then blends
adjacent mip levels to hide the jump between them.

---

### Texture Compression and Memory

Textures dominate a renderer's memory and bandwidth, so GPUs sample from **block-compressed**
formats decoded in hardware on the fly — unlike PNG/JPEG, these allow random per-texel access.

```
  BLOCK COMPRESSION (BCn / DXT / ASTC): fixed-ratio, GPU-decodable per 4x4 block.

     BC1 (DXT1)  4x4 block -> 2 endpoint colors + 2-bit indices  -> 8:1, no/1-bit alpha
     BC3 (DXT5)  + compressed alpha block                        -> 4:1, RGBA
     BC5         two channels (great for NORMAL maps: store X,Y, reconstruct Z)
     BC6H        HDR (float) textures
     BC7 / ASTC  high-quality, variable block size (ASTC)        -> 4:1..8:1

  Why not JPEG? GPUs need O(1) random access to any texel during filtering. Block
  schemes decode one tiny block independently; JPEG/PNG require sequential decode.
```

The mip chain is *also* compressed, so the +1/3 memory cost is on top of an already-
compressed base. Choosing the right format (BC5 for normals, BC7 for albedo, BC6H for HDR
environment maps) is a real bandwidth lever — and getting it wrong (e.g. BC1 on a normal map)
introduces visible block artifacts in shading.

## Layer 5: Antialiasing — Edges and Everything Else

Mipmaps fix *texture* aliasing. **Geometric edges** alias too — a triangle edge crossing a
pixel grid produces jagged "stair-step" boundaries because each pixel is either fully in or
fully out. Antialiasing estimates *partial coverage*.

```
  SSAA (Supersample AA)        render at NxN resolution, average down.
                               Shades every subsample -> correct but ~N^2 cost. Brutal.

  MSAA (Multisample AA)        store coverage + depth at K sample points per pixel,
                               but run the FRAGMENT SHADER ONCE per pixel per primitive.
                               -> antialiases EDGES at a fraction of SSAA's cost.
                               Does NOT antialias shader-internal aliasing (specular,
                               alpha-test) -- only geometric coverage.

  FXAA / SMAA                  post-process: detect edges in the final image, blur them.
                               Cheapest; can soften the whole image.

  TAA (Temporal AA)            jitter the camera each frame, accumulate over time using
                               motion vectors to reproject. Effectively free supersampling
                               across frames; can ghost/blur on disocclusion. Now dominant
                               (and the basis for DLSS/FSR upscalers).
```

```
  EDGE WITHOUT AA            EDGE WITH AA (coverage estimated)
  --------------            ---------------------------------
   ##                        ##
   ####                      ###.        partial pixels get a
   ######      (jaggies)     ####:       blended (gray) value
   ########                  #####.       proportional to coverage
```

| Method | What it samples | Cost | Catches | Misses |
|---|---|---|---|---|
| **SSAA** | Everything, N×N | Very high (N² shading) | All aliasing | Nothing (just expensive) |
| **MSAA** | Coverage/depth ×K, shade ×1 | Moderate | Geometric edges | Shader/specular/alpha aliasing |
| **FXAA/SMAA** | Final image edges | Very low | Visible edges | Sub-pixel detail; blurs |
| **TAA** | Jittered samples over time | Low | Edges + shader aliasing | Stable scenes only; ghosting |

The MSAA/SSAA distinction is the key one: **SSAA shades every subsample** (correct, costly);
**MSAA shades once per pixel** but stores multiple coverage/depth samples (cheap, but only
fixes *edge* aliasing, since shading isn't supersampled). That's why MSAA does nothing for
specular shimmer or alpha-tested foliage — those alias *inside* the shader, where MSAA only
runs once.

---

## Worked Example: Choosing a Mip Level

A 1024×1024 texture on a quad. At the current camera distance, one screen pixel's footprint
spans about 4 texels in `u` and 4 in `v` (UVs change by `4/1024` per pixel).

```
  Footprint = 4 texels across.
  Mip level halves resolution each step, so it DOUBLES the texels-per-texel coverage:

     level 0: 1 texel  per base texel
     level 1: covers 2-texel footprints
     level 2: covers 4-texel footprints   <-- matches our 4-texel pixel footprint

  LOD λ = log2(footprint) = log2(4) = 2.0   ->  sample mip level 2 (256x256).

  Trilinear blends levels 2 and 3 if λ landed between them (e.g. λ = 2.3 ->
  70% level 2 + 30% level 3).

  If the surface tilts to a grazing angle so the footprint becomes 1 x 16 texels,
  isotropic LOD would pick λ = log2(16) = 4 (very blurry). ANISOTROPIC instead keeps
  λ near log2(1)=0 along the short axis and takes ~16 taps along the long axis -> stays
  sharp where trilinear would smear.
```

The `log2(footprint)` rule is exactly "match the sampling rate to the signal's frequency" —
the sampling theorem applied per pixel.

---

## Old World → New World Bridges

| You already know | Here it is |
|------------------|-----------|
| Nyquist sampling theorem (DSP) | Texture/edge aliasing — *the same theorem*, in 2D |
| Anti-alias filter before an ADC | Mipmaps: band-limit before sampling |
| A mip pyramid = a Gaussian/box pyramid | Image pyramid, precomputed per texture |
| Oversampling an ADC | SSAA — sample above Nyquist, then decimate |
| Decimation filter after oversampling | The downsample step of SSAA / mip generation |
| Temporal accumulation / running average | TAA — supersample across frames via reprojection |
| Lerp / bilinear interpolation | Texture magnification filtering |
| Linear vs gamma-encoded data | sRGB color maps vs linear normal/roughness maps (`08`) |

---

## Decision Cheat Sheet

| Situation | Choice |
|---|---|
| Texture too small for the screen | Bilinear magnification |
| Texture minified (distant surface) | Mipmaps + trilinear |
| Surfaces at grazing angles (floors, roads) | Anisotropic filtering |
| Jagged geometric edges, cheap budget | MSAA (or FXAA if very tight) |
| Reference-quality, cost no object | SSAA |
| Modern real-time, want shader AA too | TAA (basis of DLSS/FSR) |
| Color/albedo texture | sRGB sampler (decode to linear) |
| Normal/roughness/AO texture | Linear sampler (no decode) |
| Specular/foliage still shimmers under MSAA | Need TAA/SSAA or shader-side prefiltering |

---

## Common Confusion Points

### "Why does my distant textured floor shimmer without mipmaps?"

Because a distant pixel covers many texels but samples one — undersampling a high-frequency
signal, which folds high frequencies into a moving moiré (aliasing). Mipmaps pre-blur the
texture so the sampled level is band-limited to the pixel's rate. It is the exact 2D analogue
of audio aliasing without an anti-alias filter.

### "MSAA is on but specular highlights still sparkle — why?"

MSAA only supersamples **coverage and depth**, then runs the fragment shader **once** per
pixel per primitive. Aliasing that originates *inside* the shader — sharp specular,
alpha-test cutouts, high-frequency normal maps — isn't sampled multiple times, so MSAA can't
fix it. You need SSAA, TAA, or to prefilter the offending signal (e.g. roughness/normal
mipmapping, specular antialiasing).

### "Trilinear vs anisotropic — isn't trilinear already smooth?"

Trilinear is smooth but assumes a *square* pixel footprint. At grazing angles the footprint
is a long thin ellipse; trilinear picks a high (blurry) mip to cover the long axis,
over-blurring the short axis. Anisotropic samples along the ellipse's long axis with
multiple taps, keeping the texture sharp where trilinear goes mushy.

### "Why is TAA everywhere now despite the ghosting?"

It amortizes supersampling across *frames* (jitter + reproject via motion vectors), so it
antialiases edges *and* shader aliasing at low per-frame cost — and the same accumulation
buffer powers upscalers (DLSS/FSR). The price is ghosting/blur on disocclusion and fast
motion, which modern variants mitigate with history clamping. The cost/quality tradeoff
simply beats MSAA for today's deferred, shader-heavy renderers.

### "Do mipmaps make textures blurry?"

Only if the wrong (too-high) level is chosen — which is exactly what anisotropic filtering
prevents at grazing angles. With correct LOD selection, mipmaps make distant textures
*stable* (no shimmer) at their proper sharpness; the alternative (no mips) is sharper but
aliases badly. The +1/3 memory cost buys both stability and speed (better cache locality on
minified fetches).
