# Computer Vision
## CNN Theory, Architectures, Detection, Segmentation, ViT, and Self-Supervised Learning

```
COMPUTER VISION ARCHITECTURE TIMELINE

  AlexNet (2012) → VGG → GoogLeNet → ResNet (2015) → DenseNet
       ↓                                    ↓
  Deep learning    ImageNet turns           Skip connections
  takes vision     (error: 26%→16%)         solve depth
                                                ↓
                                         EfficientNet, RegNet
                                         (scaling laws for CNNs)
                                                ↓
                                         ViT (2020)   ← transformers enter vision
                                                ↓
                                         Swin, DeiT, BEiT
                                         ConvNeXt (CNN revival)
                                                ↓
                                         CLIP, DINO, MAE   ← self-supervised
```

---

## Signal Processing Bridge — Manual Filters → Learned Filters

Classical image processing and DSP practitioners already know convolutional filters —
they just hand-designed them. CNNs learn the same filters from data:

```
Classical image processing filter          CNN equivalent
──────────────────────────────────────     ────────────────────────────────────────────
Gaussian blur (low-pass filter):           Smooth activation map in early layers
  K = [[1,2,1],[2,4,2],[1,2,1]]/16          First layer filters often resemble Gabor
  → attenuates high frequencies               filters (oriented Gaussians) = learned
  → removes noise                             blur + edge in one kernel

Sobel operator (edge detection):           Learned 3×3 edge detector in layer 1
  K_x = [[-1,0,1],[-2,0,2],[-1,0,1]]       AlexNet, VGG layer 1 filters ≈ Sobel-like
  → ∂I/∂x ← gradient in x direction         on Gabor basis
  K_y = Kᵀ                                  Network discovers these automatically

Laplacian of Gaussian (LoG):               Deep layer features: corners, textures
  ∇²(G*I) ← second derivative              LoG is a "corner detector" — layer 2/3
  Used in: blob detection, SIFT              CNNs learn these

Sharpening filter:                         High-pass component in residual learning
  K = [[0,-1,0],[-1,5,-1],[0,-1,0]]        ResNet's F(x) = H(x) - x is the residual
  = I + Laplacian                           "high-frequency" part on top of identity

Downsampling (stride-2):                   CNN stride=2 in convolution or pooling
  Decimate signal by factor 2               Stride-2 conv = filter + downsample
  Aliasing if not low-pass filtered first   BN/ReLU before stride reduces aliasing
  (Nyquist: must sample at 2× bandwidth)

Receptive field in DSP:                    Receptive field in CNNs
  An FIR filter of order k processes        Layer 1: 3×3 = 3 pixels
  k+1 samples around each output            Layer 2: 5×5 = 5 pixels (stacked 3×3)
  → finite impulse response ↔ convolution  Layer L: (2L+1)×(2L+1) field
```

**The key insight**: classical CV required a human expert to design the filter kernel
(Sobel, LoG, Gabor). A CNN is an end-to-end learning system that discovers the
optimal set of filters jointly with the downstream task. Every `Conv2d` layer is a
bank of learned finite-impulse-response (FIR) filters applied in parallel.

---

## 1. Convolution — Mathematical Foundation

**2D convolution** (in practice, cross-correlation):
```
  (I * K)[i,j] = Σ_{m,n} I[i+m, j+n] · K[m,n]

  I ∈ ℝ^{H×W}: input feature map
  K ∈ ℝ^{k×k}: convolutional kernel (filter)
  Output: ℝ^{(H-k+1)×(W-k+1)} without padding

  With padding p and stride s:
  Output size: ⌊(H + 2p - k)/s⌋ + 1
```

**Convolution layer**: learns K (the filter). Multiple input channels C_in, multiple output channels C_out:
```
  Output[c_out, i, j] = Σ_{c_in} Σ_{m,n} Input[c_in, i·s+m, j·s+n] · K[c_out, c_in, m, n]

  Parameters: C_out × C_in × k × k  (much fewer than a dense layer)
```

**Key properties**:
```
  Translation equivariance:  f(T(x)) = T(f(x))   shift input → shift output
  Weight sharing:            same kernel applied everywhere → parameter efficiency
  Local connectivity:        receptive field of size k, not full input

  These three properties are the inductive bias of CNNs for visual data.
```

**Receptive field** grows with depth:
```
  Layer 1 (k=3): each output sees 3×3 input
  Layer 2 (k=3): each output sees 5×5 input (3 + 2×1 dilation)
  Layer L (k=3): each output sees (2L+1)×(2L+1) input

  Dilated convolution (atrous): skip pixels, k=3 with dilation d → effective k=2d+1
  Effective receptive field ≠ theoretical: center pixels influence output more
```

**Pooling**: downsamples spatially, builds translation invariance (not equivariance):
```
  Max pooling: max over k×k window → invariant to small shifts
  Average pooling: mean over window → smoother
  Global average pooling (GAP): reduce to 1×1 → classification head without FC layers
```

---

## 2. Classical CNN Architectures

**VGG (Simonyan & Zisserman, 2014)**:
```
  All 3×3 convolutions, 2×2 max pool (stride 2)
  Two 3×3 convolutions = one 5×5 receptive field, fewer params
  16-19 layers, ~138M params (VGG-16)
  Very regular structure → easy to transfer
```

**Inception (GoogLeNet, 2014)**:
```
  Inception module: parallel convolutions with different k (1×1, 3×3, 5×5)
  1×1 convolutions as "bottleneck": reduce channel dim before expensive convolutions
  Auxiliary classifiers during training (vanishing gradient hack — now deprecated)
```

**ResNet (He et al., 2015)** — skip connections solve depth:
```
  Residual block:
    x ──────────────────────► (+) ──► output
    └──► Conv → BN → ReLU → Conv → BN ──┘

  H(x) = F(x) + x  (residual learning)

  Why it works:
  1. Gradient flow: ∂L/∂x = ∂L/∂output · (∂F/∂x + I)
     Identity term I ensures gradient always flows back, even if F saturates
  2. Ensemble interpretation: exponential number of effective paths through skip connections
  3. Preconditioning: learning F = H - x (residual) is easier when H ≈ I

  ResNet-50: 50 layers, 25M params; ResNet-152: 60M params
```

**Batch normalization** (every conv layer):
```
  Without BN: very deep nets couldn't train
  BN enables: higher LR, less careful init, acts as regularizer (slight noise from batch statistics)
```

**EfficientNet (Tan & Le, 2019)**: compound scaling of depth/width/resolution:
```
  d = α^φ, w = β^φ, r = γ^φ   subject to α·β²·γ² ≈ 2
  NAS-found base architecture, scale uniformly → Pareto-optimal
```

---

## 3. Object Detection

### Two-Stage Detectors

**RCNN family**:
```
  R-CNN (2014):    selective search → crop → CNN → classify
  Fast R-CNN:      run CNN once on full image, RoI pool from feature map
  Faster R-CNN:    Region Proposal Network (RPN) — anchor-based proposals in network

  Faster R-CNN pipeline:
  Image → Backbone (ResNet) → Feature Pyramid Network (FPN)
       → Region Proposal Network (anchors → objectness score + box regression)
       → RoI Align (interpolated pooling from feature map at proposal location)
       → Classification head + box refinement
```

**Feature Pyramid Network (FPN)**: multi-scale feature hierarchy:
```
  Bottom-up: standard CNN backbone (C2, C3, C4, C5 feature maps at different scales)
  Top-down: upsample from deep levels, merge with shallow levels (lateral connections)
  Output: {P2, P3, P4, P5} — all semantically strong, all at different resolutions
  Key insight: combine high-resolution (shallow) with high-semantics (deep)
```

### One-Stage Detectors

**YOLO (You Only Look Once)**:
```
  Divide image into S×S grid
  Each cell predicts B bounding boxes (x,y,w,h,confidence) + C class scores
  Single forward pass → predictions
  Much faster than two-stage, slightly less accurate

  YOLO v5/v8: anchor-free, CSP backbone, PANet neck, decoupled head
  Real-time at 30-60fps on GPU
```

**SSD / RetinaNet**:
```
  SSD: predictions at multiple scales (multi-scale feature maps)
  RetinaNet: FPN backbone + Focal Loss

  Focal Loss (Lin et al. 2017): down-weight easy negatives:
  FL(p) = -α(1-p_t)^γ log(p_t)
         ↑             ↑
     balancing    focusing: reduces loss for easy positives/negatives
  One-stage detectors fail on class imbalance — foreground << background
  Focal loss fixes this: γ=2, easy examples (p_t=0.9) downweighted by (0.1)²=0.01
```

**DETR (Carion et al. 2020)** — transformers for detection:
```
  End-to-end: no anchors, no NMS
  CNN backbone → transformer encoder/decoder
  Decoder queries (N=100 learned "object queries") attend to image features
  Hungarian matching loss (bipartite matching between predictions and GT)

  Advantage: no hand-designed anchors or NMS hyperparameters
  Disadvantage: slow training convergence (requires ~300 epochs vs ~12 for Faster RCNN)
  Deformable DETR, DAB-DETR: fix convergence speed
```

---

## 4. Semantic and Instance Segmentation

**Semantic segmentation**: assign class label to every pixel (no instance distinction).

**FCN (Fully Convolutional Network)**:
```
  Replace FC layers with 1×1 convolutions → maintains spatial resolution
  Upsampling via transposed convolutions (or bilinear interp)
  Shortcut connections from early layers for fine detail
```

**U-Net (Ronneberger et al. 2015)** — encoder-decoder with skip connections:
```
  Encoder ──────────────────────────────────────────────► Decoder
  (downsampling + increasing channels)      (upsampling + decreasing channels)
                  ↑─────────────skip connections──────────↑

  Skip connections concatenate encoder feature maps to decoder at same resolution
  → Fine-grained spatial info (edges) + semantic info (what) combined
  → Dominant for medical imaging
```

**DeepLab**: dilated convolutions to increase receptive field without downsampling:
```
  ASPP (Atrous Spatial Pyramid Pooling):
    Parallel dilated convolutions with rates {6, 12, 18}
    + image-level global pooling
    → captures multi-scale context
```

**Instance segmentation**: detect + segment each instance separately.

**Mask RCNN (He et al. 2017)**: Faster RCNN + mask branch:
```
  RoI Align (instead of RoI Pool): bilinear interpolation preserves spatial accuracy
  Mask head: small FCN applied to each RoI → binary mask per class per instance
  Key fix: RoI Align removes quantization artifacts crucial for pixel-level masks
```

---

## 5. Vision Transformer (ViT)

**Architecture** (Dosovitskiy et al. 2020):
```
  Image x ∈ ℝ^{H×W×C}

  1. Patch embedding:
     Divide into N = HW/P² patches of size P×P
     Flatten each patch: ℝ^{P²C}
     Linear projection: ℝ^{P²C} → ℝ^D  (patch embedding)

  2. Prepend [CLS] token (classification token)

  3. Add learned positional embeddings (no 2D structure assumed)

  4. Standard transformer encoder (L layers of MHSA + FFN)

  5. [CLS] token output → classification head

  Sequence length: N+1 = (HW/P²)+1   (e.g., 224/16 → 196+1 = 197 tokens)
```

**ViT vs CNN**:
```
  CNN                                ViT
  ────────────────────────────       ────────────────────────────────
  Translation equivariance built-in  No built-in translation invariance
  Local receptive fields             Global receptive fields from layer 1
  Inductive bias → data efficient    Inductive bias-free → needs more data
  Good for small-medium datasets     Shines with large datasets (100M+)
  Faster inference (parallelism)     More flexible architecture
```

**ViT scaling**: ViT-B (86M), ViT-L (307M), ViT-H (632M). Performance scales with data and compute — ImageNet-21k pretraining bridges the data gap.

**Swin Transformer** (Liu et al. 2021):
```
  Hierarchical: feature maps at different resolutions (like FPN for CNNs)
  Shifted window attention: attention within local windows (O(n) vs O(n²))
  Window size 7×7, shifted by (3,3) each layer for cross-window connections
  → Achieves CNN-like locality and hierarchy with transformer flexibility
  → Dominates dense prediction tasks (detection, segmentation)
```

**ConvNeXt** (Liu et al. 2022): modernize ResNet with ViT design choices:
```
  Larger kernels (7×7), depthwise separable convolutions
  Fewer activation functions, LayerNorm instead of BatchNorm
  Inverted bottleneck (wide FFN, narrow residual)
  → Matches Swin with much simpler architecture
```

---

## 6. Self-Supervised Learning

Goal: learn visual representations without labels.

### Contrastive Methods

**SimCLR** (Chen et al. 2020):
```
  Given image x, create two augmented views x̃₁, x̃₂ (crop, flip, color jitter)
  Encode: z₁ = f(x̃₁),  z₂ = f(x̃₂)  (ResNet backbone)
  Project: h₁ = g(z₁),  h₂ = g(z₂)  (2-layer MLP head)

  NT-Xent loss (normalized temperature-scaled cross-entropy):
  L = -log( exp(sim(h₁,h₂)/τ) / Σ_{k≠i} exp(sim(hᵢ,hₖ)/τ) )

  Positive pair: (x̃₁, x̃₂) from same image
  Negatives: all other images in batch
  Requires large batch (4096+) for enough negatives
```

**MoCo** (He et al. 2020): memory bank / momentum encoder to decouple batch size from # negatives.

### Non-Contrastive Methods

**BYOL** (Bootstrap Your Own Latent):
```
  No negative pairs. Online network predicts target network's representation.
  Target network = exponential moving average of online network.
  Collapse prevented by momentum update (not theoretically understood — empirically works).
```

**DINO** (Caron et al. 2021): self-distillation + transformers:
```
  Student and teacher networks, teacher = EMA of student
  Multi-crop augmentation strategy
  Key finding: ViT trained with DINO learns segmentation without labels
  DINO features cluster by semantic content → attention maps ≈ unsupervised segmentation
```

### Masked Autoencoders (MAE)

**MAE** (He et al. 2022):
```
  Mask 75% of image patches randomly
  Encoder: ViT applied to visible patches only (efficient)
  Decoder: lightweight transformer reconstructs masked patches from pixel values

  Key design choices:
    High masking ratio (75%): makes task hard, prevents simple interpolation
    Pixel reconstruction (not discrete tokens): simpler, works better
    Decoder applied to ALL positions (mask tokens + visible)

  Result: strong representations with less compute than contrastive methods
  Scaling: MAE + ViT-H ≈ supervised ViT-H performance (ImageNet)
```

---

## 7. Vision-Language Models

**CLIP** (Radford et al. 2021):
```
  Train on 400M image-text pairs from web
  Image encoder (ViT or ResNet) + Text encoder (Transformer)

  Contrastive loss over N image-text pairs:
    Maximize similarity of correct (image, text) pairs
    Minimize similarity of incorrect pairs
    N²-N negative pairs per batch (N ≈ 32768)

  Zero-shot transfer: for classification, embed class names as text
    "a photo of a {class}" → text embedding
    Compare image embedding → argmax → classification
  → Competitive with supervised ResNet-50 on ImageNet with zero training on it

  CLIP features: extremely general, transferable, language-aligned
```

---

## 8. Decision Cheat Sheet

| Task | Model | Notes |
|------|-------|-------|
| Image classification, small data | ResNet, EfficientNet | Strong inductive bias |
| Image classification, large data | ViT, Swin | Scale benefits transformers |
| Object detection, accuracy | Swin + DINO + DETR | SOTA, slow |
| Object detection, speed | YOLOv8, RTDETR | Real-time |
| Semantic segmentation | Mask2Former, Swin-UperNet | Transformer backbone + FPN-like |
| Instance segmentation | Mask RCNN, Mask2Former | |
| Medical imaging | U-Net variants | Skip connections critical |
| Self-supervised pretraining | MAE (ViT) | Efficient, strong |
| Image-text tasks | CLIP + adapter | Zero/few-shot transfer |

---

## 9. Common Confusion Points

1. **"Convolution is translation invariant"** — CNNs are translation equivariant (shift input → shift output). Translation invariance (shift input → same output) is achieved by pooling. Global average pooling gives full translation invariance.

2. **"ResNet skip connections are just for gradient flow"** — The "highway gradient" interpretation is compelling but incomplete. Ensemble interpretation (exponential paths) and implicit preconditioning are also operating. ResNet trains deeper because all three effects combine.

3. **"ViT needs huge datasets"** — With modern self-supervised pretraining (DINO, MAE, CLIP), ViT can match CNNs on small-medium datasets. The "data hungry" property was for supervised training from scratch.

4. **"NMS is part of detection"** — Traditional detectors use NMS to remove duplicate boxes. DETR eliminates NMS via Hungarian matching. The trend is toward NMS-free detectors.

5. **"Semantic and instance segmentation are the same"** — Semantic: every pixel gets a class (two people = same class). Instance: each object instance gets a separate mask (two people = two distinct masks). Panoptic segmentation = both.

6. **"Self-supervised = unsupervised"** — Self-supervised uses the data itself as supervision (predict masked patches, contrastive view consistency). Unsupervised typically means no signal from the data structure. Self-supervised is more specific and more powerful.

7. **"Contrastive learning requires negative pairs"** — BYOL and SimSiam showed you can learn strong representations without negative pairs using momentum networks and stop-gradient. Why this doesn't collapse is still not fully understood theoretically.
