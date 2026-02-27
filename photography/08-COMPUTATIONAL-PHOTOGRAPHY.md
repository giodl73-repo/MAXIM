# Computational Photography

## The Big Picture

Computational photography is **photography where computation is a fundamental part of image formation** — not post-processing applied to an optically-captured image, but algorithms that execute during capture to produce images that a single optical exposure could not create. The smartphone has made computational photography the dominant form of photography by count, because computation can compensate for physically small apertures, sensors, and fixed focal lengths.

```
COMPUTATIONAL PHOTOGRAPHY — TAXONOMY:

  MULTI-FRAME TECHNIQUES:
    HDR:             Multiple exposures → merged tone map
    Focus stacking:  Multiple focal planes → extended depth of field
    Panorama:        Multiple views → extended field of view
    Multi-frame NR:  Multiple captures of same scene → noise reduction
    Super-resolution: Multiple subpixel offsets → increased apparent resolution
    Night mode:      30+ frames, aligned and merged → bright/sharp at low light

  SINGLE-FRAME COMPUTATIONAL:
    Bokeh simulation: depth map → artificial aperture blur
    Semantic segmentation: sky/grass/face detection → zone-specific processing
    Tone mapping:     Map HDR sensor data → display-renderable image
    Lens correction:  Correct distortion/CA digitally (embedded profile)

  DEPTH ESTIMATION:
    Stereo (dual camera): disparity → depth
    Time-of-flight LiDAR: pulse timing → precise depth
    Focus cues (single camera): sharpness gradient → rough depth
    Structured light (Face ID): projected pattern → face depth

  AI-BASED:
    Super-resolution:  CNN upscaling beyond optical resolution
    AI denoising:      Learned noise removal
    AI sky replacement: Semantic segmentation + replacement
    Portrait mode:     AI hair/edge segmentation for precise matte
```

---

## HDR — High Dynamic Range

### Capture

```
HDR CAPTURE STRATEGIES:

  EXPOSURE BRACKETING:
    Capture N exposures (typically 3, 5, or 7) at different EVs
    E.g., −2 EV, 0 EV, +2 EV (2-stop brackets)
    Each exposure optimal for different tonal range:
      −2 EV → highlights (sky, sun) properly exposed
       0 EV → midtones
      +2 EV → shadows (dark interior) properly exposed
    Merge: select best-exposed values per pixel → linear HDR image

  GHOSTING:
    Moving objects (clouds, water, people) appear in different positions across brackets
    → Appear as transparent ghost when images merged
    Deghosting: for each pixel, detect if the value is inconsistent with reference frame
      → Reject outlier values; use reference frame instead
    Modern deghosting (Lightroom, PTGui): motion detection per region → smart selection
    Limitation: fast motion + large brackets → deghosting artifacts

  SINGLE-FRAME HDR (modern sensors):
    Dual gain readout: each pixel read at two amplification levels simultaneously
    Or: dual exposure (interleaved rows/frames at 2 different ISOs)
    → No ghosting (single moment capture)
    → Less total DR than bracketed but avoids motion issues

  DUAL NATIVE ISO:
    Camera has two distinct gain paths (Sony A7S III: ISO100 + ISO640/1280)
    Each native ISO has its own low noise floor
    → In video: alternating frame ISO → HDR video (HDR HLG)
```

### Tone Mapping

```
TONE MAPPING PROBLEM:
  HDR radiance map: 10,000:1 or more dynamic range (100,000 cd/m² sun → 1 cd/m² shadow)
  Display: sRGB monitor = 100:1 typical DR; HDR display = 1,000–10,000:1
  → Must compress huge HDR range into smaller display range
  → Naïve solution (global linear scaling) → flat, low-contrast image

GLOBAL TONE MAPPING OPERATORS:

  Reinhard (2002) — most influential:
    Luminance mapping: L_d = L_w / (1 + L_w)
    Automatic: 0 → 0; large L_w → 1.0 (asymptote)
    Extended Reinhard: adds "white point" parameter Lwhite
      L_d = L_w × (1 + L_w / Lwhite²) / (1 + L_w)
    Property: very bright highlights → compressed; midtones → preserved
    Visual: natural; loses some "pop"; popular for real-world photography

  Drago (2003) — logarithmic:
    L_d = (L_dmax × 0.01 / log₁₀(Lmax + 1)) × log₁₀(L + 1) × (bias function)
    Bias: user-controlled compression of dark vs. bright regions
    Visual: preserves local contrast well; can appear slightly washed out

  Gamma compression: L_d = L_w^(1/γ), γ typically 2.2
    Simplest; used in cameras; maps linear sensor to gamma-encoded display
    Not a true HDR tone mapper — just gamma encoding

LOCAL TONE MAPPING OPERATORS:
  Key insight: human visual system adapts locally (eye adapts dark and bright simultaneously)
  Local operators: compute spatially-varying tone mapping — each region mapped differently

  BILATERAL TONE MAPPING (Durand 2002):
    Decompose image into base layer (large-scale luminance) + detail layer
    Compress only the base layer (reduces large dynamic range)
    Preserve + add back detail layer (maintains local contrast)
    → Result: feels more "real"; local contrast preserved; no halos if done well
    Halo artifact: if base/detail decomposition is imperfect → dark ring around bright areas

  UNSHARP MASKING / LOCAL CONTRAST:
    Boost local contrast after global compression → "pop" look
    Commonly used in consumer HDR (including smartphone HDR processing)

  AI / DEEP LEARNING TONE MAPPING (2020+):
    End-to-end trained networks: input HDR linear map → output display image
    Can learn perceptually optimal mappings without analytical assumptions
    Used in: Apple ProRAW HDR, Google HDR+ photon transfer model
```

---

## Focus Stacking

```
FOCUS STACKING PURPOSE:
  Single exposure: plane of sharp focus is a thin slice through 3D scene
  Focus stacking: multiple exposures, each focused at different depth
    → Merge: keep sharpest region from each exposure → extended DoF throughout

  Applications:
    Macro photography: DoF measured in millimeters → must stack many frames
    Landscape: infinity to foreground in focus simultaneously
    Product photography: technical detail across 3D objects
    Microscopy: standard technique (depth sectioning)
    Focus-bracketing cameras: Olympus/OM System, Sony, Nikon → automated in-camera

DEPTH-FROM-FOCUS CUES:
  Sharpness metric: how focused is each pixel in each frame?
  Laplacian (second derivative of intensity): high → sharp; low → blurry
  Gradient magnitude: local contrast measure
  Tenengrad: sum of squared Sobel filter responses
  DCT frequency content: high spatial frequencies → sharpness
  → For each pixel: find frame with highest sharpness metric → select that frame's value

FOCUS STACK WORKFLOW:
  1. Capture N frames (same position; change focus by known step)
     Step size: depends on DoF at each magnification/aperture; usually automated
  2. Align frames: even on tripod, small vibrations cause pixel-level shifts
     ECC alignment (enhanced correlation coefficient) or feature-based
  3. Depth map estimation: assign depth to each pixel based on focus stack
  4. Fusion: blend pixels from appropriate depth frames

ALGORITHMS:

  HELICON SOFT:
    Method A (Weighted average):
      Weight per pixel = sharpness metric → weighted average across frames
      → Smooth transitions; slightly reduced sharpness; handles transparent objects
    Method B (Depth map from stack):
      Compute depth map → sharp selection → surface interpolation
      → Sharper but can have artifacts where depth estimation fails
    Method C (Pyramidal):
      Multi-scale blend (similar to multiband blending in panoramas)
      → Best overall; handles noise, transparency, fine detail

  ZERENE STACKER:
    PMax: maximum sharpness pixel selection (like Method B; very sharp)
    DMap: depth map + interpolation (handles artifacts better)
    → Zerene: preferred by professional macro photographers for fine detail

ARTIFACTS:
  Halo/fringing: sharp subject against soft background → edge artifact where frame transitions
  Ghosting: subject movement between frames (insects, flowers moving)
  "Busy" textures: transitions between depth layers → unnatural texture discontinuity
  → Retouching required for critical work; stack 2–3× more frames than needed
```

---

## Panorama Stitching

```
PANORAMA PIPELINE:
  1. Capture overlapping images (typically 30–50% overlap)
  2. Feature detection: SIFT, SURF, ORB, or deep features → keypoints in each image
  3. Feature matching: find corresponding points across image pairs
  4. Geometric transformation estimation: homography or cylindrical/spherical projection
  5. RANSAC: reject outlier matches (robust estimation)
  6. Bundle adjustment: globally minimize reprojection error across all images + cameras
  7. Seam finding: optimal blend seam selection (avoid seams at edges)
  8. Blending: feathered blend or multi-band blend across seams

HOMOGRAPHY:
  Maps one planar image to another via 3×3 projective transformation matrix H:
  [x'] = H × [x]
  [y']       [y]
  [w']       [1]

  H has 8 degrees of freedom (homogeneous: scale-independent)
  Computed from ≥4 point correspondences (8 equations; 8 unknowns)
  Valid for: planar scenes, or camera rotation only (no translation)
  Fails: camera translation + non-planar scene → parallax → H doesn't fit

CYLINDRICAL / SPHERICAL PROJECTION:
  For wide panoramas: each image mapped to cylinder or sphere before stitching
  Cylindrical: images projected as if from inside a cylinder → correct for horizontal pan
  Spherical (equirectangular): maps entire 360° scene → used for VR/360 panoramas
  Fish-eye unwrap: specific projection model for ultra-wide-angle capture

RANSAC (Random Sample Consensus):
  For feature matching: many false matches (outliers) exist
  Algorithm:
    1. Randomly sample minimum correspondences to estimate model (4 for H)
    2. Count inliers (points fitting model within threshold)
    3. Repeat N times → keep model with most inliers
    4. Re-estimate model using all inliers
  Highly effective: works even if >50% of matches are outliers
  Used in: panorama (homography), 3D reconstruction (fundamental matrix), AR (pose estimation)

MULTI-BAND BLENDING:
  Simple feathering: weighted average at seam → visible if exposure/color differs
  Multi-band (Burt & Adelson 1983):
    Decompose into Laplacian pyramid (frequency bands)
    Blend each frequency band independently (wide transition in low freq; narrow in high)
    → Low frequencies: long blend zone → smooth gradients
    → High frequencies: short blend zone → sharp detail
  Result: invisible seams even with moderate exposure variation across source images
```

---

## Smartphone Computational Pipeline

```
GOOGLE NIGHT SIGHT / PIXEL PIPELINE (published in SIGGRAPH papers):

  CAPTURE:
    User presses shutter → capture 6–30+ frames (short exposures, auto exposure)
    Long exposure (full Night Sight): multiple seconds of short bursts
    Each frame: 12–14 ms exposure → prevents blur; motion can be handled

  MOTION ROBUST ALIGNMENT:
    Optical flow (pixel-level motion estimation) between all frames
    Handle: camera shake, subject motion (people, leaves)
    "Burst photography" alignment: translational + rotational + slight deformation

  MULTI-FRAME NR:
    Each aligned frame: pixels with same scene value → average → SNR = √N improvement
    N=16 frames → 4× SNR improvement → 2 stops effective noise reduction
    Outlier rejection: pixels that don't match (motion, occlusion) → weighted less
    → Effectively: same SNR as sensor 4× larger aperture area

  SEMANTIC UNDERSTANDING:
    Computational sky: detect sky → boost blue saturation; tone map separately
    Face detection: detect faces → reduce sharpening on skin; preserve exposure
    Subject/background: depth estimation → differential sharpening or exposure
    Night sky: detect star field → specialized processing (no noise reduction on stars)

APPLE PHOTONIC ENGINE (iPhone 14+):
  Capture: multiple frames at every shutter press (even single shot)
  Deep fusion (2019): 9 frames per shot → ML merge → texture detail + noise reduction
  Smart HDR 4: bracket exposure + merge; AI scene analysis
  Photographic styles: semantic segmentation → zone-specific color grading at capture

PORTRAIT MODE (BOKEH SIMULATION):
  Hardware: dual camera → stereo depth; or structured light; or monocular ML depth
  Depth map: ~8-bit depth per pixel (~256 depth levels)
  Segmentation: ML model → person vs background → precise edge matte (hair-level)
  Blur application: Gaussian blur scaled by depth value → background blur
  Limitations: depth estimation fails at: glass, reflective surfaces, hair, complex edges
  vs real optical bokeh:
    Real: actual out-of-focus blur from physics; continuous; no edge artifacts
    Simulated: hard edge at depth discontinuity; uniform blur regardless of texture
    → Gap closing with ML improvements; still distinguishable in critical analysis

AI UPSCALING / SUPER-RESOLUTION:
  Classical: bicubic interpolation → blurry enlarged image
  SRCNN (2014): first deep learning upscaling → sharper edges
  ESRGAN (2018): GAN-based; can hallucinate plausible texture → may not be real
  Real-ESRGAN (2021): trained on real-world degradation → practical use
  Apple ProRes RAW + ProRes → upscaling uses content-aware ML
  Lightroom AI Enhance (Super Resolution):
    4× pixel count upscaling; trained on high-res references
    Genuinely adds detail (through learned priors); not pure interpolation
    Artifacts: can hallucinate plausible-but-wrong textures in uniform areas
```

---

## LiDAR for Depth

```
TIME-OF-FLIGHT LIDAR (iPhone 12 Pro+, iPad Pro):

  Principle: emit near-IR laser pulse → measure return time
  Speed of light: 3×10⁸ m/s → 1 ns = 15 cm round-trip
  Pixel array: direct time-of-flight (dToF) SPAD sensor (single-photon avalanche diode)
  Range: 5 meters in direct sunlight; 40 meters indoors

  Distance = (c × Δt) / 2

  ADVANTAGES:
    Works in dark: emits its own IR illumination
    Fast: captures full depth map in <1ms (no passive light dependency)
    Accurate: ±1 cm at 1 meter; ±3% at 5 meters
    Complements camera depth: iPhone uses LiDAR for AF at low light (extremely fast)

  INDOOR AR:
    AR plane detection: LiDAR builds room mesh in real-time
    Occlusion: AR objects can be hidden behind real objects (depth test)
    Shadow casting: AR objects cast shadows on real surfaces

  COMPARED TO STRUCTURED LIGHT (Face ID):
    Face ID: projects 30,000 dot pattern → distortion = depth → very precise, short range
    LiDAR: time-of-flight → longer range; lower resolution; outdoor-capable

  PHOTOGRAMMETRY (3D SCANNING):
    LiDAR + camera → point cloud + texture → 3D models
    Apps: Scaniverse, Polycam → scan rooms, objects for 3D printing or AR
    Industrial: LIDAR point clouds replace manual measurement for as-built documentation
```

### Structure-from-Motion and Photogrammetry

SfM reconstructs 3D geometry from multiple 2D images — the computational photography technique with the most direct ML/CV connections.

```
SfM PIPELINE:
  Images → Feature detection (SIFT/ORB/SuperPoint)
       → Feature matching across image pairs
       → RANSAC (outlier rejection for geometric consistency)
       → Bundle adjustment (jointly optimize camera poses + 3D points)
       → Dense reconstruction (Multi-View Stereo / MVS)
       → Textured mesh or point cloud output

  Same core as panorama stitching: both use RANSAC + bundle adjustment.
  Panorama stitches 2D; SfM recovers full 3D structure.

ML EXTENSIONS (2020+):
  NeRF (Neural Radiance Fields, Mildenhall et al. 2020):
    Represent scene as MLP: (x,y,z,θ,φ) → (color, density)
    Train on posed images; render novel views via volume rendering.
    Slow training (~hours), slow rendering, but photorealistic.

  3D Gaussian Splatting (Kerbl et al. 2023):
    Represent scene as millions of oriented 3D Gaussians.
    Differentiable rasterization → real-time rendering at 100+ fps.
    Trains in minutes, renders in real-time. Rapidly displacing NeRF
    for many applications (AR, VR, gaming, digital twins).

  Consumer apps: Polycam, Scaniverse, KIRI Engine, RealityCapture.
```

---

## Decision Cheat Sheet

| Goal | Technique |
|------|----------|
| High contrast scene (sky + shadow) | HDR bracketing + tone mapping OR ETTR single RAW |
| Maximum sharpness throughout macro subject | Focus stacking (Zerene DMap or Helicon C) |
| Wide landscape scene | Panorama with cylindrical/spherical projection |
| Reduce noise at high ISO | Multi-frame NR (Lightroom Enhance, Topaz, or in-camera burst) |
| Enlarge small image | AI super-resolution (Lightroom AI Enhance, Real-ESRGAN) |
| Portrait bokeh (no fast lens) | Dual-camera depth + ML segmentation (portrait mode) |
| Room scanning / AR | LiDAR depth capture + photogrammetry app |
| Night photography (handheld) | Smartphone Night Mode (multi-frame handheld) or DSLR + tripod |

---

## Common Confusion Points

**Tone mapping is not color grading**
Tone mapping converts an HDR luminance range to a smaller range for display. Color grading adjusts the stylistic appearance of an already properly-exposed image. Many HDR mobile processing pipelines do both simultaneously, which is why "HDR" on a phone camera can look oversaturated or stylized — the tone mapping algorithm is doing heavy creative lifting, not just physics-based compression.

**AI super-resolution is not recovering information that was there**
When a super-resolution algorithm sharpens a 12MP image to apparent 48MP, it is hallucinating plausible detail based on training data, not recovering data that existed in the original. For most images this looks correct and is practically useful. But the "detail" may not match the actual subject — a smooth wall might gain fabricated texture, a face might subtly distort. Real information recovery requires the original scene data.

**Smartphone portrait "bokeh" fails at depth discontinuities**
Real optical bokeh blurs smoothly because out-of-focus blur is a physical effect that transitions continuously. Simulated bokeh segments the image into "sharp" and "blurred" regions based on a depth map — at edges where depth changes abruptly, the segmentation produces artifacts (halo, hard edge, incorrect blur of foreground objects partially overlapping background). This is most visible on: fine hair, glasses frames, wind-blown fabric.

**Focus stacking and HDR fail for moving subjects differently**
HDR failure: moving subjects appear at different positions → ghosting (transparency artifact) → deghosting algorithms needed. Focus stacking failure: same problem — moving insect in a macro stack appears ghosted at edges. But focus stacking requires more extreme alignment precision because magnification is higher — tiny vibrations matter. Single-frame HDR and in-camera focus stacking (pixel-shift mode) solve both problems for still subjects.

**LiDAR in smartphones is not what autonomous vehicle LiDAR is**
Automotive LiDAR (Velodyne, Luminar): spinning or solid-state; 360° coverage; 200m range; centimeter-level accuracy at distance; designed for real-time 3D scene understanding. iPhone LiDAR: small SPAD array; 5m range; ~20-50 depth pixels equivalent; consumer price point. They share the time-of-flight principle but are orders of magnitude apart in capability and cost.
