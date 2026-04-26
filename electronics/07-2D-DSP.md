# 07 — 2-D Digital Signal Processing

```
2D DSP LANDSCAPE
═══════════════════════════════════════════════════════════════════════════════

  1D DSP:  x[n]  →  X(e^(jω))     — one frequency axis ω
  2D DSP:  x[m,n] → X(e^(jω₁), e^(jω₂))  — two frequency axes ω₁, ω₂

  ┌────────────────────────────────────────────────────────────────────┐
  │  SPATIAL DOMAIN            FREQUENCY DOMAIN                        │
  │  x[m,n] — image pixels     X(ω₁,ω₂) — 2D spectrum                  │
  │                                                                    │
  │  Convolution (2D)          Multiplication (pointwise)              │
  │  y[m,n] = x[m,n] ** h[m,n]  Y = X · H                              │
  │                                                                    │
  │  Separable systems:        H(ω₁,ω₂) = H₁(ω₁) · H₂(ω₂)          │
  │  → row-by-row 1D then column-by-column 1D                          │
  └────────────────────────────────────────────────────────────────────┘

  Applications:
    Image filtering (blur, sharpen, edge detect)
    MRI k-space reconstruction
    CT reconstruction (filtered backprojection)
    Seismic array processing
    Optical diffraction (far-field = 2D FT of aperture)

  6.003 bridge: everything from 1D carries over with (m,n) indices.
  Standard MIT 6.003/6.341 material — the value-add here is MRI k-space
  reconstruction, CT filtered backprojection, and compressed sensing.
```

---

## 1. 2D Signals and Systems

### Notation and Indexing

```
  x[m,n]: m = row index (vertical), n = column index (horizontal)
  Origin at (0,0) — or sometimes at center after fftshift.

  Continuous-space analog: f(x,y) with Fourier pair F(u,v)
  Discrete-space: x[m,n] with 2D DTFT X(e^(jω₁), e^(jω₂))

  Image as 2D signal:
    Grayscale: x[m,n] ∈ [0,255] (uint8) or [0,1] (float)
    Color: three-channel x_R[m,n], x_G[m,n], x_B[m,n]
    Each channel processed independently for many operations.
```

### 2D LTI Systems

```
  Linear shift-invariant (LSI in 2D = LTI in 1D):
    Linearity: T{ax₁+bx₂} = aT{x₁} + bT{x₂}
    Shift-invariance: if y[m,n] = T{x[m,n]}, then
      T{x[m-m₀, n-n₀]} = y[m-m₀, n-n₀]   for all (m₀,n₀)

  Completely characterized by 2D impulse response h[m,n]:
    y[m,n] = x[m,n] ** h[m,n] = Σₖ Σₗ x[k,l] h[m-k, n-l]
```

---

## 2. 2D DFT

### Definition

```
  Analysis (forward):
    X[k,l] = Σₘ₌₀^(M-1) Σₙ₌₀^(N-1) x[m,n] e^(-j2πkm/M) e^(-j2πln/N)

  Synthesis (inverse):
    x[m,n] = (1/MN) Σₖ Σₗ X[k,l] e^(+j2πkm/M) e^(+j2πln/N)

  k=0,...,M-1 (vertical freq), l=0,...,N-1 (horizontal freq)
  DC at (k,l) = (0,0) — usually shifted to center for display.
```

### Separability and Computational Efficiency

```
  Key identity:
  e^(-j2πkm/M) e^(-j2πln/N) = [row transform of row m] × [col transform of col n]

  Algorithm:
    1. Apply N-point 1D DFT to each of the M rows
    2. Apply M-point 1D DFT to each of the N columns of the result

  Complexity: MN(log M + log N) operations — exactly two passes of 1D FFTs.
  Same as O(MN log(MN)) — optimal for separable transforms.

  Non-separable transforms (e.g., DFT on hexagonal grid): no shortcut.
  Most practical 2D transforms are separable.
```

### Circular Convolution in 2D

```
  DFT computes circular (not linear) convolution:
    Y[k,l] = X[k,l] · H[k,l]  →  y[m,n] = x[m,n] ⊛ h[m,n]  (circular)

  For linear convolution via DFT:
    Pad x and h with zeros so output size = (M+P-1) × (N+Q-1)
    where x is M×N and h is P×Q.
    Then zero-padded 2D DFT product → IDFT = linear convolution.
```

### Parseval's Theorem (2D)

```
  Σₘ Σₙ |x[m,n]|² = (1/MN) Σₖ Σₗ |X[k,l]|²

  Energy preserved. |X[k,l]|² = power spectral density in 2D.
```

---

## 3. 2D Convolution

### Direct Computation

```
  y[m,n] = Σₖ Σₗ x[k,l] h[m-k, n-l]

  For image x of size M×N and kernel h of size P×Q:
    Output size (linear): (M+P-1) × (N+Q-1)
    Operations: MN × PQ multiplications — O(MN·PQ)

  Practical:
    Small kernels (3×3, 5×5, 7×7): direct is fast (few operations per pixel)
    Large kernels (blur σ=50 on 4K image): FFT method vastly faster
    Crossover: roughly when P×Q > log(MN)
```

### Common Image Kernels

```
  Box filter (3×3 average):           Gaussian (σ=1):
  1/9 × [1 1 1]                       1/16 × [1 2 1]
         [1 1 1]                               [2 4 2]
         [1 1 1]                               [1 2 1]

  Sharpening (unsharp mask):          Laplacian (edge detect):
  [0 -1  0]                           [0  1  0]
  [-1  5 -1]                          [1 -4  1]
  [0 -1  0]                           [0  1  0]
  = δ + (δ - Gaussian)                (= 2D discrete Laplacian ∇²)

  Sobel (horizontal edges):           Sobel (vertical edges):
  [-1 0  1]                           [-1 -2 -1]
  [-2 0  2]                           [ 0  0  0]
  [-1 0  1]                           [ 1  2  1]
  (≈ horizontal derivative)          (≈ vertical derivative)
```

### Separable Kernels

```
  If h[m,n] = h₁[m] · h₂[n], the kernel is separable.

  2D convolution with separable kernel:
    y = x ** h = (x convolved with h₁ along rows) convolved with h₂ along columns

  Operations: MN(P+Q) instead of MN·PQ — major savings for large kernels.
  Gaussian is separable: G₂D(m,n) = G₁D(m) · G₁D(n).
  Sobel is not separable as one step, but can be decomposed.

  Test for separability: h is separable iff rank(h as matrix) = 1
    → SVD: σ₁ only nonzero → h = u₁ v₁ᵀ (outer product of two 1D filters)
```

---

## 4. 2D Frequency Domain Analysis

### Spatial Frequency

```
  ω₁ (vertical spatial frequency) in rad/pixel
  ω₂ (horizontal spatial frequency) in rad/pixel

  Range: [-π, π] in each dimension (DTFT, continuous ω)
         [0, M-1] or [-M/2, M/2-1] for M×N DFT (after fftshift)

  Physical meaning:
    Low frequencies (near DC): slowly varying content — large structures
    High frequencies: rapidly varying content — fine detail, edges, noise

  Edge = transition from dark to light = many high-frequency components needed.
  Smooth regions = primarily low-frequency content.
```

### Frequency Domain Visualization

```
  |X(ω₁, ω₂)|:  magnitude spectrum
  ∠X(ω₁, ω₂):  phase spectrum

  Typical image spectrum after fftshift (DC at center):
  ┌─────────────────────────────────┐
  │                                 │
  │          High freq              │
  │      (corners of spectrum)      │
  │                                 │
  │         ╔═══════╗               │
  │         ║  DC   ║               │
  │         ║ center║               │
  │         ╚═══════╝               │
  │                                 │
  │    Low freq near center         │
  └─────────────────────────────────┘
  Cross pattern: horizontal/vertical lines in image
  → horizontal/vertical high-amplitude frequencies

  Phase encodes structure (edges, shapes).
  Magnitude encodes energy distribution.
  Phase-swap experiment: swap phases of two images → result looks like
  the phase donor, even with the magnitude of the other.
```

### Ideal Filters in 2D

```
  Low-pass filter (circular):
    H(ω₁,ω₂) = 1 if √(ω₁²+ω₂²) < ωc, else 0
    → blurs image (removes fine detail)
    Impulse response: 2D jinc (J₁(r)/r) — Bessel function variant

  High-pass filter: H_HP = 1 - H_LP
    → enhances edges, removes smooth background

  Band-pass: H_LP_high - H_LP_low
    → isolates specific spatial frequency range
```

---

## 5. Image Filtering Applications

### Gaussian Blur

```
  H_G(ω₁,ω₂) = e^(-σ²(ω₁²+ω₂²)/2)   (Gaussian in frequency = Gaussian in space)

  Spatial: h[m,n] = (1/2πσ²) e^(-(m²+n²)/2σ²)
  σ controls blur radius.

  Properties:
    Rotationally symmetric (isotropic)
    Separable: apply 1D Gaussian to rows, then columns
    Self-similar: cascade of Gaussians is Gaussian (σ² additive)
    Scale-space: progressively blurring creates scale-space pyramid

  Box blur vs Gaussian:
    Box: uniform weight, fast (O(1) per pixel with integral image), but ringing
    Gaussian: smooth, no ringing, perceptually better, slightly slower
```

### Edge Detection

```
  Edges = image gradients. Two approaches:

  1. Gradient filter then threshold:
    Gx = Sobel_x * image   (horizontal gradient)
    Gy = Sobel_y * image   (vertical gradient)
    |G| = √(Gx² + Gy²)     (gradient magnitude)
    θ = arctan(Gy/Gx)       (gradient direction)
    Threshold |G| > T: edge pixels

  2. Laplacian of Gaussian (LoG):
    LoG(x,y) = -1/(πσ⁴)(1-(x²+y²)/2σ²) e^(-(x²+y²)/2σ²)
    Convolution with LoG → zero-crossings are edges
    Smoothed (Gaussian) first → "Marr-Hildreth edge detector"

  3. Canny edge detector (standard):
    a. Gaussian smooth
    b. Gradient magnitude and direction
    c. Non-maximum suppression (thin edges to 1 pixel)
    d. Double threshold + hysteresis (connect weak edges to strong)
    Best edge detector in practice; most implementations use it.
```

### Frequency Domain Image Enhancement

```
  Homomorphic filtering (illumination/reflectance separation):
    f(x,y) = i(x,y) · r(x,y)   (illumination × reflectance)
    log f = log i + log r        (additive)
    FT, apply HPF to reduce i (low freq), boost r (high freq), IFFT, exp

  Wiener filter (deblurring with noise):
    Observed: G(u,v) = H(u,v)·F(u,v) + N(u,v)
    Wiener: F̂(u,v) = [H*(u,v) / (|H|² + Snn/Sff)] · G(u,v)
    Balances deblurring (invert H) vs noise amplification.
    When SNR → ∞: becomes H*(u,v)/|H(u,v)|² (inverse filter)
    When SNR → 0: output → 0 (don't trust blurry data)
```

---

## Engineering Bridge: 2D Convolution and Neural Networks

```
2D DSP OPERATION                  CNN EQUIVALENT
──────────────────────────────────────────────────────────────────────────────
2D convolution kernel h[m,n]      Learned filter (weight matrix) in conv layer
  fixed, designed by engineer      learned via backpropagation from data

y[m,n] = x[m,n] ** h[m,n]        Feature map = input ** kernel
  cross-correlation (technically)   CNN "convolution" is actually cross-correlation
  slide kernel, multiply-accumulate same multiply-accumulate, same separability

Multiple kernels in parallel      Multiple output channels (filters per layer)
  edge detect, blur, sharpen        each channel learns a different feature

FFT-based fast convolution        cuDNN uses Winograd or FFT for large kernels
  O(MN log MN) vs O(MN·PQ)         same complexity tradeoff applies
──────────────────────────────────────────────────────────────────────────────
```

The CNN convolution layer is exactly 2D DSP convolution with learned kernels — the same operation this guide covers, but where the filter coefficients are optimized by gradient descent rather than designed from specifications. Hardware accelerators (DSP48 slices in FPGAs, NPU tensor cores in SoCs) execute the same multiply-accumulate dataflow for both classical DSP and neural network inference.

---

## 6. k-Space and MRI

### What Is k-Space?

```
  MRI measures signals S(kx, ky) directly in the Fourier domain
  (called "k-space" in MRI parlance).

  k = γ/(2π) · ∫ G(τ) dτ    (k-space position from gradient history)
  γ = gyromagnetic ratio (42.58 MHz/T for ¹H)
  G(t) = gradient waveform [mT/m]

  The spin density ρ(x,y) is the 2D inverse FT of S(kx,ky):
    ρ(x,y) = ∫∫ S(kx,ky) e^(+j2π(kxx+kyy)) dkx dky
```

### k-Space Trajectories

```
  Cartesian (standard EPI, spin echo):
    Fill k-space row by row.
    kx swept rapidly (frequency encode), ky stepped between echoes (phase encode).

  Radial:
    Collect spokes at angles 0,...,π.
    Golden-angle increment: θₙ = n·111.25°
    → uniform coverage as more spokes added.
    Motion-robust (center of k-space oversampled).

  Spiral:
    kx(t) = α(t)cos(ω(t)), ky(t) = α(t)sin(ω(t))
    Very fast acquisition.
    Sensitive to off-resonance (chemical shift, B₀ inhomogeneity).

  ┌─────────────────────────────────────────────────────┐
  │  k-SPACE REGIONS AND IMAGE FEATURES                 │
  │                                                     │
  │  Center of k-space (low k): contrast, large features │
  │  Periphery (high k): edges, fine detail             │
  │                                                     │
  │  Missing center → blurry, low contrast              │
  │  Missing periphery → smooth, loss of detail         │
  │                                                     │
  │  Corrupted k-space line → striping artifact         │
  │  (FT of a single point = sinusoid across image)     │
  └─────────────────────────────────────────────────────┘
```

### Compressed Sensing MRI

```
  Nyquist sampling: need full Cartesian k-space → long scan time.

  Compressed sensing (Candes, Romberg, Tao 2006):
  If image is sparse in some transform domain (wavelets, total variation),
  can reconstruct from far fewer samples.

  Solve: min ||Ψρ||₁  subject to  F_u ρ = data
    F_u = undersampled Fourier operator
    Ψ = sparsifying transform (wavelet, finite difference)

  Incoherence + sparsity + randomized undersampling → 4–10× acceleration.
  FDA-approved for cardiac, angiography, pediatric MRI.
```

---

## 7. CT Reconstruction — Filtered Backprojection

### Projection-Slice Theorem

```
  For 2D object f(x,y):
  Projection at angle θ: p_θ(t) = ∫ f(x,y) ds  (line integral at angle θ)

  Projection-slice (Fourier slice) theorem:
    FT{p_θ(t)} = F(u,v)|_{line through origin at angle θ}

  = The 1D Fourier transform of a projection at angle θ equals
    a slice through the 2D Fourier transform of f at that angle.

  Strategy: collect projections at many angles → fill 2D Fourier space → 2D IFFT
```

### Filtered Backprojection (FBP)

```
  Direct backprojection smears each projection back across image → blurry.

  FBP applies ramp filter |ω| before backprojection:
    1. Take 1D FT of each projection p_θ(t)
    2. Multiply by |ω| (ramp filter in Fourier)
    3. Inverse 1D FT
    4. Backproject (add filtered projection along each ray direction)

  The |ω| ramp comes from the polar-to-Cartesian Jacobian: dA = r dr dθ,
  so each annular ring in frequency needs to be weighted by its radius r = |ω|.

  Modified ramp filters:
    Ram-Lak: ideal ramp (no windowing)
    Shepp-Logan: ramp × sinc/π (smoother)
    Hanning: ramp × Hanning window (tradeoff noise vs resolution)
    All reduce noise at cost of resolution.

  Iterative reconstruction (MBIR, ADMM):
    Minimize ||Ax-y||² + λR(x)
    A = Radon transform, R(x) = regularizer (TV, wavelet L1)
    Much lower noise/dose than FBP, especially for sparse data.
    Standard in modern scanners (IR/MBIR options).
```

---

## 8. DCT and Image Compression

### 2D DCT-II (Used in JPEG)

```
  For N×N block (standard N=8):

  X[k,l] = α(k)α(l) Σₘ Σₙ x[m,n] cos[π(2m+1)k/2N] cos[π(2n+1)l/2N]

  α(0) = 1/√N,  α(k) = √(2/N) for k > 0

  Properties:
    All real (unlike DFT which has complex values)
    Energy compaction: most image energy in low-frequency (upper-left) coefficients
    Efficient: fast DCT via FFT tricks in O(N² log N)
    No Gibbs artifact at block boundary (cosine basis is symmetric)
```

### JPEG Compression Flow

```
  Encode:
  Image → 8×8 blocks → 2D DCT → Quantize (divide by Q table) →
  Zigzag scan → Run-length + Huffman encode → Bitstream

  Decode:
  Bitstream → Huffman decode → Inverse zigzag → Dequantize →
  2D IDCT → Reconstruct image

  Quantization:
    DCT coefficients divided by quality-dependent step size Q[k,l].
    Human Visual System (HVS) weights: high-freq coefficients use larger Q.
    Lossy step: integer rounding of X[k,l]/Q[k,l].

  Blocking artifact:
    At low quality (high Q), high-frequency coefficients zeroed.
    8×8 block boundaries become visible.
    Fix: JPEG2000 uses wavelet (no block boundaries).
    Fix: In-loop deblocking filter in H.264/265.
```

### JPEG 2000 — Wavelet-Based

```
  Replace 8×8 DCT with 2D discrete wavelet transform (DWT).
  Multi-resolution: CDF 9/7 wavelet (lossy) or 5/3 (lossless).

  Advantages over JPEG:
    No blocking artifact at high compression
    Progressive transmission (show coarse image, refine)
    Lossless option with same codec
    ROI coding: sharper quality in selected region

  Used in: medical imaging (DICOM), cinema (DCI), remote sensing.
  Not widely used for web (browser support patchy until recently).
```

---

## 9. Scale-Space and Multi-Resolution

### Gaussian Pyramid

```
  Level 0: original image I₀
  Level k: I_{k+1} = downsample(Gaussian_blur(Iₖ))
    - Blur with σ_k before downsampling (anti-aliasing)
    - Each level ½ the resolution

  ┌────────────────────────────────────┐
  │  ████████████████  ← level 0 (full res)
  │      ████████      ← level 1 (½ res)
  │        ████        ← level 2 (¼ res)
  │         ██         ← level 3 (⅛ res)
  └────────────────────────────────────┘

  Used in: image blending, optical flow, feature detection at multiple scales.
```

### Laplacian Pyramid

```
  L_k = I_k - upsample(I_{k+1})   (difference = band-pass image)
  Captures detail at each scale band.
  Exactly reconstructible: I_k = L_k + upsample(I_{k+1})

  Used in: image blending, HDR tone mapping, texture transfer.
  Different from Gaussian pyramid: Laplacian pyramid is the residual at each level.
```

### 2D Discrete Wavelet Transform

```
  One level: apply 1D DWT to each row, then to each column.
  Produces four subbands:
    LL: low-low (coarse approximation) → recursively decompose
    LH: low-high (horizontal edges, vertical oscillation)
    HL: high-low (vertical edges, horizontal oscillation)
    HH: high-high (diagonal features, noise)

  ┌──────┬──────┐   After one 2D DWT:
  │      │      │
  │  LL  │  LH  │   LL = coarse, blurry
  │      │      │   LH = horizontal detail
  ├──────┼──────┤   HL = vertical detail
  │      │      │   HH = diagonal detail
  │  HL  │  HH  │
  │      │      │
  └──────┴──────┘

  Apply recursively to LL subband → full multi-resolution decomposition.
```

---

## 10. Decision Cheat Sheet

| Task | Method |
|---|---|
| Convolve large image with large kernel | 2D FFT method (O(MN log MN)) |
| Convolve with small kernel (≤7×7) | Direct convolution (O(MN·PQ)) |
| Separable kernel (Gaussian blur) | Two passes of 1D convolution |
| Blur image smoothly | 2D Gaussian convolution |
| Detect edges | Canny (gold standard) or Sobel + threshold |
| Sharpen image | Unsharp mask = original + (original - blur) |
| Analyze image frequency content | 2D FFT → fftshift → log magnitude |
| Remove periodic noise (e.g., scan lines) | FFT, zero out offending peaks, IFFT |
| Reconstruct image from projections (CT) | Filtered backprojection (or iterative) |
| Reconstruct MRI image | 2D IFFT of k-space data |
| Compress image (lossy) | JPEG (DCT-based) |
| Compress image (no blocking artifacts) | JPEG2000 (wavelet-based) |
| Multi-resolution analysis | Gaussian/Laplacian pyramid or 2D DWT |
| Undersample MRI and still reconstruct | Compressed sensing (L1 optimization) |

---

## 11. Common Confusion Points

**1. fftshift is for display, not for computation**
The 2D FFT output has DC at (0,0), not at the center. fftshift reorders the output to place DC at center — this is purely a display convention. If you fftshift before applying a filter then IFFT, you must also ifftshift back, or use a filter mask in the unshifted indexing. Applying a centered filter to an unshifted spectrum (or vice versa) produces a phase-shifted, spatially-rotated result.

**2. Circular vs linear convolution — must zero-pad for images**
The 2D DFT computes circular convolution. For image filtering where the kernel doesn't wrap around, you must zero-pad both image and kernel before DFT. For small kernels (Gaussian 5×5), the wrap-around error is negligible. For large kernels, it causes obvious wrap-around artifacts at image borders.

**3. k-space center ≠ image center**
In MRI k-space: the origin (DC component, k=0) corresponds to the average signal over the whole object — it encodes contrast. The edges of k-space (high spatial frequency) encode fine detail. A corruption (spike) in k-space appears as a sinusoidal artifact across the entire image. A missing line in k-space causes a ghosting stripe. These are FT properties, not MRI-specific.

**4. Ramp filter in FBP is not optional**
Simple backprojection (without filtering) produces severe blurring: each object point creates a star-shaped smear. The ramp filter |ω| is mathematically required to undo this smearing — it comes from the change of variables from parallel projections to 2D Fourier domain in polar coordinates. Omitting it (or using a very smooth filter) reduces noise but degrades resolution severely.

**5. DCT block size of 8×8 in JPEG is a psychovisual choice**
The 8×8 block size matches human visual system sensitivity (HVS insensitive to spatial frequencies above ~10 cycles/degree at normal viewing distance). Larger blocks give better compression at the cost of larger blocking artifacts; smaller blocks reduce artifacts but reduce compression. The choice of 8 is empirical, not mathematically optimal.

**6. Separability and rank**
A 2D filter h[m,n] is separable if and only if, viewed as an M×N matrix, it has rank 1. The SVD reveals the separable decomposition: h = σ₁u₁v₁ᵀ. If rank > 1, the filter is not separable and cannot be implemented as two 1D passes. The Gaussian is rank 1 (separable). The Laplacian is not rank 1 (it's not separable into row and column operations). The Laplacian of Gaussian (LoG) can be approximated by a Difference of Gaussians (DoG = two separable operations subtracted) — this is the key efficiency trick in SIFT and scale-space edge detection.
