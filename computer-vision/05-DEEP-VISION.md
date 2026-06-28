---
maxim_schema: maxim.frontmatter.v1
id: maxim:computer-vision:deep-vision
kind: guide
module: computer-vision
section: computing-software
title: Deep Vision - CNNs and Transformers
status: source-custody
source_custody: partial
current_path: computer-vision/05-DEEP-VISION.md
canonical_path: computer-vision/05-DEEP-VISION.md
backsource_ids: [proof-backfill:computer-vision:05-deep-vision, git-history:computer-vision:05-deep-vision]
concepts: [convolutional neural network, receptive field, residual networks, transfer learning, vision transformer, learned filters]
root_concepts: [deep vision]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# Deep Vision — CNNs and Transformers

## The Big Picture: Learning the Filters

The classical pipeline (guide 04) hand-designed the filters (HOG, SIFT) and learned only
the classifier. Deep vision learns *everything* end-to-end: the convolution kernels are
parameters, optimized by backpropagation so that early layers discover edge filters,
middle layers discover parts, and late layers discover objects. This guide assumes you
already know what a neural net is and how backprop trains it (see `ai-engineering/` and
`machine-learning-theory/`); the focus here is the *spatial* architecture — what makes a
vision network a vision network.

```
+------------------------------------------------------------------------------+
|               THE CNN AS A LEARNED FEATURE HIERARCHY  (image -> label)       |
|                                                                              |
|   IMAGE     LAYER 1        LAYER 2..k        DEEP LAYERS      HEAD           |
|   +-----+   edges,         textures,         object parts,    softmax        |
|   |     |   oriented  -->  corners,    -->   wheels, eyes -->  "car: 0.97"   |
|   |     |   bars           color blobs        whole objects                  |
|   +-----+   (Gabor-like)                                                     |
|              |                                                               |
|              +-- These early filters look like LEARNED Sobel/SIFT filters.   |
|                 Deep learning AUTOMATED the feature engineering of guide 04. |
|                                                                              |
|   Spatial size SHRINKS (pooling/stride); channel depth GROWS (more filters). |
+------------------------------------------------------------------------------+
```

---

## Layer 1: The Convolution Layer — Weight Sharing as a Prior

A convolution layer applies a small bank of learned kernels across the whole image. Two
architectural priors make this work where a fully-connected net would fail:
**translation equivariance** (the same filter slides everywhere — a cat is a cat in any
corner) and **parameter sharing** (one kernel, not one weight per pixel pair).

```
   A conv layer: input C_in channels -> output C_out channels.
   Each output channel = SUM over input channels of (input * kernel) + bias.

      input HxWxC_in   --[ K kernels, each kxkxC_in ]-->   output H'xW'xC_out

   Parameters per layer:  k*k * C_in * C_out  (+ C_out biases)
   -- INDEPENDENT of image size. A dense layer would need H*W*C weights per unit.

   Stride s: step the kernel by s -> downsamples by s.
   Padding p: pad the border to control output size.
   Output size: H' = floor((H + 2p - k)/s) + 1
```

| Prior | What it buys |
|-------|--------------|
| Local connectivity | Each unit sees a small patch — matches image locality |
| Weight sharing | Far fewer parameters; translation equivariance |
| Pooling / stride | Spatial invariance + a growing receptive field |
| Channel depth | Many filters per location → rich feature banks |

**Bridge — signal processing:** each channel is a learned 2D FIR filter (guide 02). The
layer is a *filter bank*; depth stacks banks. The "convolution" is technically
correlation (no kernel flip) — see guide 02 — but the learned weights absorb it.

---

## Layer 2: The Receptive Field — How Much Each Unit Sees

The **receptive field** of a unit is the region of the input image that can influence it.
It is the deep-net analogue of a kernel's support, and it grows with depth, stride, and
pooling. A unit must "see" an object to classify it, so receptive-field growth is what
lets deep layers reason about whole objects from local convolutions.

```
+------------------------------------------------------------------------------+
|                       RECEPTIVE FIELD GROWTH WITH DEPTH                      |
|                                                                              |
|   input        layer1 (3x3)     layer2 (3x3)      layer3 (3x3)               |
|   pixel grid   sees 3x3         sees 5x5          sees 7x7                   |
|                                                                              |
|   o o o o o     [ o o o ]                                                    |
|   o o o o o     [ o o o ]  -> stacking two 3x3 = one 5x5 RF, fewer params    |
|   o o o o o     [ o o o ]     and more nonlinearity (the VGG insight)        |
|                                                                              |
|   Stride/pooling MULTIPLY RF growth; dilation (atrous) ENLARGES RF without   |
|   adding parameters or losing resolution (used in DeepLab, guide 03).        |
+------------------------------------------------------------------------------+
```

The VGG insight (2014): two stacked 3x3 convolutions have the same 5x5 receptive field as
one 5x5 convolution but with fewer parameters and an extra nonlinearity. Small kernels,
stacked deep, became the default.

---

## Layer 3: The Building Blocks

A modern conv net is assembled from a handful of standard layers.

| Layer | Role | Key detail |
|-------|------|-----------|
| **Convolution** | Learned filtering | The feature extractor |
| **ReLU** (activation) | Nonlinearity | `max(0,x)`; cheap, avoids vanishing gradient |
| **Pooling** | Downsample / invariance | Max or average over a window; no parameters |
| **Batch norm** | Stabilize training | Normalizes activations per mini-batch |
| **Stride / dilation** | Control resolution & RF | Stride downsamples; dilation enlarges RF |
| **1x1 convolution** | Channel mixing / bottleneck | Reduces depth cheaply (Network-in-Network) |
| **Global avg pool** | Spatial → vector | Replaces dense layers before the head |

```
   A typical block:   conv -> batch norm -> ReLU  (repeat)  -> pool
   Classifier tail:   ... -> global average pool -> dense -> softmax
```

---

## Layer 4: The Architecture Lineage

Vision architectures evolved by solving the problem the previous one exposed. Knowing the
lineage tells you *why* each design exists.

```
+------------------------------------------------------------------------------+
|                  CNN ARCHITECTURE LINEAGE  (problem -> fix)                  |
|                                                                              |
|  LeNet (1998)    first conv net (digits)                                     |
|      |                                                                       |
|  AlexNet (2012)  ReLU + dropout + GPUs; WON ImageNet -> ignited deep vision  |
|      |                                                                       |
|  VGG (2014)      deep stacks of 3x3 convs; simple, uniform                   |
|      |                                                                       |
|  GoogLeNet/      Inception modules: parallel multi-scale convs + 1x1         |
|  Inception       bottlenecks -> efficiency                                   |
|      |                                                                       |
|  ResNet (2015)   RESIDUAL connections: y = F(x) + x  -> trains 100+ layers   |
|      |          (solves vanishing-gradient/degradation) -- the turning point |
|      |                                                                       |
|  DenseNet,       feature reuse, depthwise-separable convs (MobileNet),       |
|  EfficientNet    compound scaling -> accuracy/compute frontier               |
|      |                                                                       |
|  ViT (2020)      pure transformer on image patches -- a new branch (below)   |
+------------------------------------------------------------------------------+
```

### ResNet — why residual connections matter

The central problem deep nets hit was *degradation*: adding layers made training error go
*up*, not down — not overfitting, an optimization failure. ResNet's fix is the **residual
(skip) connection**: a layer learns a residual `F(x)` added to its input `x`.

```
   Plain block:     y = F(x)                  hard to learn identity
   Residual block:  y = F(x) + x              identity is FREE (set F=0)

         x ----------------+
         |                 |  (skip / identity)
         v                 v
       [ weight layers ]   +  ----> y = F(x) + x
       (learn F(x))

   Gradient flows directly through the +x path -> deep nets become trainable.
   This single idea unlocked networks of 50, 101, 152+ layers.
```

**Bridge — numerical methods:** the residual form makes each block a perturbation of the
identity, which keeps the Jacobian near `I` and the gradients well-conditioned — the deep
analogue of a well-scaled iterative update.

---

## Layer 5: Transfer Learning — The Practical Workhorse

Training from scratch needs millions of labeled images. In practice you almost never do
it: you take a network pre-trained on ImageNet and adapt it. The early layers' filters
(edges, textures) are nearly universal across visual domains, so they transfer.

```
+------------------------------------------------------------------------------+
|                       TRANSFER LEARNING STRATEGIES                           |
|                                                                              |
|  PRE-TRAINED BACKBONE (ImageNet)        +------------------------+           |
|  [ generic early layers ] [ later ]     | YOUR small dataset     |           |
|                                          +------------------------+          |
|                                                                              |
|  STRATEGY                  FREEZE              TRAIN                         |
|  --------                  ------              -----                         |
|  Feature extraction        all conv layers     just a new head               |
|  Fine-tuning (light)       early layers         later layers + head          |
|  Fine-tuning (full)        nothing              everything (low LR)          |
|                                                                              |
|  Less data / more similar -> freeze more. More data / less similar -> train  |
|  more. This is the single highest-leverage technique in applied vision.      |
+------------------------------------------------------------------------------+
```

| Your situation | Strategy |
|----------------|----------|
| Tiny dataset, similar domain | Freeze backbone, train new head only |
| Moderate dataset | Fine-tune later layers + head |
| Large dataset, different domain | Fine-tune all, low learning rate |
| No labels | Self-supervised pretraining (SimCLR, MAE), then fine-tune |

**Bridge — ML theory:** why transfer works connects to the generalization and
representation-learning material in `machine-learning-theory/`. The early filters
approximate a universal visual basis (Gabor-like), so they need not be relearned.

---

## Layer 6: Vision Transformers — Attention Instead of Convolution

The Vision Transformer (ViT, 2020) discarded convolution entirely: split the image into
patches, embed each as a token, and run a standard transformer encoder. Self-attention
lets every patch interact with every other patch directly — a global receptive field from
layer one, where a CNN builds global context only gradually.

```
+------------------------------------------------------------------------------+
|                    VISION TRANSFORMER (ViT) PIPELINE                         |
|                                                                              |
|  image -> split into 16x16 PATCHES -> linear-embed each -> add POSITIONAL    |
|           encoding -> prepend [CLS] token -> TRANSFORMER ENCODER (self-      |
|           attention + MLP, repeated) -> [CLS] output -> classify             |
|                                                                              |
|   +--+--+--+      patch1 patch2 ... patchN                                   |
|   |  |  |  |  ->  [emb] [emb] ... [emb]  --self-attention--> every patch     |
|   +--+--+--+      + pos  + pos      + pos    attends to EVERY other patch    |
|   |  |  |  |                                                                 |
|   +--+--+--+      GLOBAL receptive field immediately (no locality prior)     |
+------------------------------------------------------------------------------+
```

| Aspect | CNN | Vision Transformer |
|--------|-----|--------------------|
| Inductive bias | Strong (locality, translation equivariance) | Weak (must learn it from data) |
| Data appetite | Moderate | Large (or heavy augmentation / pretraining) |
| Receptive field | Grows with depth | Global from layer 1 |
| Compute scaling | Linear in pixels | Quadratic in #patches (attention) |
| Best when | Small/medium data | Large data, scale, multimodal |

**Bridge — transformers:** the self-attention mechanism is the same one in
`ai-engineering/` for language; ViT applies it to patches. The trade-off is the classic
*inductive bias vs data* exchange — a CNN bakes in locality (free generalization, less
data), a ViT learns it (needs more data, scales further). Hybrids (Swin Transformer)
reintroduce locality and a hierarchy, recovering CNN-like efficiency.

---

## Old World → New World Bridges

| You already know | Deep vision analogue |
|------------------|----------------------|
| FIR filter banks (signal) | A conv layer is a learned, stacked filter bank |
| HOG/SIFT feature engineering | Replaced by learned early conv filters |
| Well-conditioned iterative updates | Residual blocks keep the Jacobian near `I` |
| Spatial pyramid (guide 04) | Pooling hierarchy learns coarse-to-fine spatial bins |
| Caching / reuse | Transfer learning reuses a pretrained backbone |
| Attention (transformers, NLP) | ViT applies the same self-attention to patches |

---

## Decision Cheat Sheet

| I want to... | Use |
|---|---|
| A strong default image classifier | ResNet (50/101) backbone |
| Maximum accuracy/compute efficiency | EfficientNet / ConvNeXt |
| Run on mobile / edge | MobileNet / depthwise-separable convs |
| Adapt to my small dataset | Transfer learning (freeze + new head) |
| Train with no labels first | Self-supervised pretraining (MAE/SimCLR) |
| Scale to huge data / multimodal | Vision Transformer (ViT / Swin) |
| Enlarge receptive field without losing resolution | Dilated (atrous) convolution |
| Reduce channel depth cheaply | 1x1 convolution bottleneck |
| Train very deep nets stably | Residual connections + batch norm |

---

## Common Confusion Points

### "A CNN does convolution — is it the same convolution as signal processing?"

Architecturally yes (a sliding learned kernel), mechanically it computes
cross-*correlation* (no kernel flip — guide 02). Because the kernel is learned, the flip
is absorbed into the weights, so the distinction is moot for the network's behavior. The
deeper point: the early-layer kernels, when visualized, look like the Gabor/edge filters
a signal-processing engineer would design by hand — the net rediscovers them.

### "ViT has no convolution — did it make CNNs obsolete?"

No. ViTs win at large scale and on multimodal tasks, but CNNs remain superior on small
and medium datasets because their locality prior is free generalization a ViT must learn.
Most production vision still runs CNNs; the frontier is hybrids (Swin, ConvNeXt) that
borrow the best of both. The real lesson is the inductive-bias/data trade-off, not a
winner.

### "Receptive field vs kernel size — aren't they the same?"

Kernel size is per-layer (e.g. 3x3). Receptive field is cumulative — the total input
region a deep unit depends on, growing with depth, stride, and pooling. A network of 3x3
kernels can have a receptive field covering the whole image after enough layers. Match
the receptive field to your object scale: if it never covers the object, the net cannot
"see" it whole.

### "Why pre-train on ImageNet for a totally different domain like X-rays?"

Because the *early* features — edges, textures, gradients — are domain-agnostic, and they
are the expensive thing to learn. You inherit them for free and only retrain the later,
task-specific layers. When the domain is very different (medical, satellite), full
fine-tuning or self-supervised pretraining on in-domain images does better — but even
then, ImageNet initialization usually beats random.

### "Pooling throws away spatial information — isn't that bad for localization?"

It trades spatial precision for invariance and a bigger receptive field, which helps
*classification* but hurts *localization* and *segmentation*. That is exactly why
segmentation nets (guide 03) use encoder-decoder structures with skip connections to
recover the spatial detail that pooling discarded, and why detectors (guide 07) use
feature pyramids. The fix is architectural, not a reason to avoid pooling.
