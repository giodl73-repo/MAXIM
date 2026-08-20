---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "09-APPLICATIONS.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:computer-vision:applications
kind: guide
module: computer-vision
section: computing-software
title: Applications and Deployment
status: source-custody
source_custody: partial
current_path: computer-vision/09-APPLICATIONS.md
canonical_path: computer-vision/09-APPLICATIONS.md
backsource_ids: [proof-backfill:computer-vision:09-applications, git-history:computer-vision:09-applications]
concepts: [OCR, face recognition, medical imaging, generative vision, GAN, diffusion, deployment, edge inference]
root_concepts: [vision applications]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# Applications and Deployment

## The Big Picture: Where the Pipeline Earns Its Keep

The previous guides built the machinery: formation, features, recognition, geometry,
detection, 3D. This guide shows how that machinery composes into real systems — OCR, face
recognition, medical imaging, generative vision — and then how you *ship* a vision model:
quantization, edge inference, and the engineering realities a VP signs off on. Each
application is a recipe that selects and chains components from earlier guides.

```
+------------------------------------------------------------------------------+
|            APPLICATIONS = RECIPES OVER THE VISION STACK                      |
|                                                                              |
|  APPLICATION        COMPONENTS USED (from earlier guides)                    |
|  -----------        -----------------------------------                      |
|  OCR                detect text (07) -> recognize chars (05, sequence)       |
|  Face recognition   detect (07) -> align (06 H) -> embed (05) -> match       |
|  Medical imaging    segment (03 U-Net) -> classify/detect (05/07)            |
|  Generative vision  learn image distribution -> GAN / DIFFUSION              |
|  3D capture / AR     SLAM (08) + detection (07) + rendering (graphics)       |
|                                                                              |
|  Then: TRAIN -> OPTIMIZE (quantize/prune) -> DEPLOY (cloud / edge)           |
+------------------------------------------------------------------------------+
```

---

## Application 1: OCR — Reading Text in Images

Optical Character Recognition turns pixels of text into character strings. Modern OCR is a
two-stage pipeline — *detect* where text is, then *recognize* what it says — and the
recognition stage is a sequence model, because characters form ordered strings.

```
+------------------------------------------------------------------------------+
|                       OCR PIPELINE  (detect -> recognize)                    |
|                                                                              |
|  1. TEXT DETECTION    find text regions (EAST, DBNet) -> oriented boxes      |
|                       (a specialized detector, guide 07)                     |
|  2. RECTIFY           warp each region to a horizontal strip (homography,    |
|                       guide 06) -- handles rotation/perspective              |
|  3. RECOGNITION       CNN extracts features -> sequence model reads chars:   |
|                       CRNN + CTC loss, or an attention/transformer decoder   |
|  4. POST-PROCESS      language model / dictionary correction                 |
|                                                                              |
|   "no segmentation of individual characters needed" -- CTC aligns a          |
|   variable-length character sequence to the feature columns automatically.   |
+------------------------------------------------------------------------------+
```

The key idea in recognition is **CTC** (Connectionist Temporal Classification): it lets a
network output a character sequence without pre-segmenting individual characters, by
marginalizing over all alignments of labels to feature columns. **Bridge:** this is the
same CTC used in speech recognition (`signal-processing/`) — text and audio are both
variable-length sequence-labeling problems.

---

## Application 2: Face Recognition — Embeddings and Metric Learning

Face recognition is not classification into a fixed identity set — you must recognize
people never seen in training. The solution is **metric learning**: map each face to an
embedding vector such that same-person faces are close and different-person faces are far.

```
+------------------------------------------------------------------------------+
|                  FACE RECOGNITION  (detect -> align -> embed -> match)       |
|                                                                              |
|  1. DETECT     find faces (MTCNN / RetinaFace) -> box + landmarks            |
|  2. ALIGN      warp eyes/nose/mouth to a canonical position (similarity      |
|                transform) -> pose-normalized face                            |
|  3. EMBED      CNN -> a fixed embedding vector (e.g. 512-D)                  |
|  4. MATCH      compare embeddings by cosine/Euclidean distance               |
|                                                                              |
|   TRAINING uses metric losses that shape the embedding space:                |
|     - triplet loss: anchor closer to positive than negative by a margin      |
|     - ArcFace: additive ANGULAR margin -> tighter identity clusters          |
|                                                                              |
|   VERIFICATION (1:1, "is this the same person?") vs                          |
|   IDENTIFICATION (1:N, "who is this?" -> nearest neighbor in a gallery)      |
+------------------------------------------------------------------------------+
```

| Term | Meaning |
|------|---------|
| Verification (1:1) | Same person? Threshold a distance |
| Identification (1:N) | Who is this? Nearest neighbor in a gallery |
| Triplet loss | Anchor–positive closer than anchor–negative by a margin |
| ArcFace | Angular-margin softmax → highly separable embeddings |

**Bridge — old → new:** the classical pipeline was Eigenfaces (PCA on face images,
`mathematics/` SVD) → Fisherfaces (LDA). Deep embeddings replaced these hand-built linear
subspaces with a learned nonlinear one, but the *retrieval-by-distance* structure is
identical. This is also a domain with serious bias, privacy, and consent stakes — a
deployment concern, not just an accuracy one.

---

## Application 3: Medical Imaging — Where Errors Cost Lives

Medical vision (radiology, pathology, ophthalmology) is high-value and high-stakes. It
leans heavily on segmentation (U-Net was *designed* for biomedical images, guide 03) and
classification, with domain-specific constraints that reshape the engineering.

```
+------------------------------------------------------------------------------+
|              MEDICAL IMAGING: THE CONSTRAINTS THAT CHANGE EVERYTHING         |
|                                                                              |
|  TASK TYPES                            DOMAIN CONSTRAINTS                    |
|  ----------                            ------------------                    |
|  segmentation (tumor, organ, vessel)   small/imbalanced labeled datasets     |
|  classification (malignant?)           3D volumes (CT/MRI), not just 2D      |
|  detection (lesions, nodules)          calibration + uncertainty REQUIRED    |
|  registration (align scans over time)  regulatory approval (FDA/CE)          |
|                                        interpretability for clinicians       |
|                                                                              |
|   Metrics shift: not just accuracy but SENSITIVITY (catch every disease)     |
|   vs SPECIFICITY, Dice/IoU for segmentation, AUC of the ROC curve.           |
+------------------------------------------------------------------------------+
```

What makes medical vision distinct: tiny labeled datasets (transfer learning and
augmentation are mandatory), 3D volumetric data (3D convolutions or slice-wise + fusion),
and an absolute need for **calibrated uncertainty** — a confident wrong answer can be fatal,
so the model must "know what it doesn't know." Metrics weight **sensitivity** (don't miss
disease) heavily, and the **Dice coefficient** (equivalent to F1 on pixels) is the standard
segmentation score.

---

## Application 4: Generative Vision — Synthesizing Images

Generative models learn the *distribution* of images and sample new ones. This closes the
inverse-graphics loop from guide 00: a generator is a learned *forward* model, and
conditioning it inverts cleanly. Two families dominate, with diffusion now ascendant.

```
+------------------------------------------------------------------------------+
|                     GENERATIVE VISION: GAN vs DIFFUSION                      |
|                                                                              |
|  GAN (2014)                            DIFFUSION (2020+)                     |
|  ----------                            ----------------                      |
|  generator vs discriminator,           gradually ADD noise (forward) then    |
|  adversarial minimax game              LEARN to DENOISE step by step         |
|                                        (reverse the noising process)         |
|                                                                              |
|  noise -> G -> fake image              x0 -> +noise -> ... -> pure noise     |
|                  ^                              <- denoise <- (sampling)     |
|                  | D: real or fake?                                          |
|                                                                              |
|  fast sampling, training UNSTABLE      stable training, high quality,        |
|  (mode collapse)                       slower sampling (many denoise steps)  |
|                                                                              |
|  Text-to-image (Stable Diffusion, DALL-E): a diffusion model conditioned     |
|  on text embeddings (CLIP), often in a compressed LATENT space for speed.    |
+------------------------------------------------------------------------------+
```

| Model family | Mechanism | Strength | Weakness |
|--------------|-----------|----------|----------|
| **GAN** | Adversarial generator vs discriminator | Fast sampling | Unstable training, mode collapse |
| **VAE** | Encode to latent, decode | Stable, structured latent | Blurry samples |
| **Diffusion** | Iterative denoising | High quality, stable training | Slow sampling (many steps) |
| **Autoregressive** | Predict pixels/tokens in order | Tractable likelihood | Slow, sequential |

**Bridge — signal/physics:** diffusion's forward process is literally adding Gaussian noise
(a stochastic process); the reverse is learned denoising — score matching, with roots in
non-equilibrium thermodynamics. Latent diffusion runs the process in a VAE-compressed space
for tractability. **Bridge — graphics:** text-to-3D and NeRF generation (guide 08) extend
this to 3D, completing the vision-graphics convergence.

---

## Layer 5: Deployment — From Notebook to Production

A trained model is not a product. Shipping vision means hitting a latency/cost/accuracy
target on real hardware — often a phone, camera, or embedded device, not a datacenter GPU.

```
+------------------------------------------------------------------------------+
|                   THE DEPLOYMENT PATH  (train -> ship)                       |
|                                                                              |
|  TRAINED MODEL (FP32, large)                                                 |
|       |                                                                      |
|       v   OPTIMIZE                                                           |
|  .-------------------------------------------.                               |
|  | QUANTIZATION  FP32 -> INT8 (4x smaller,   |  accuracy drop usually tiny   |
|  |               faster on int hardware)     |  with calibration/QAT         |
|  | PRUNING       remove low-weight channels  |                               |
|  | DISTILLATION  train a small student net   |                               |
|  | FUSION        fold conv+BN+ReLU into one  |                               |
|  '-------------------------------------------'                               |
|       |                                                                      |
|       v   PACKAGE                                                            |
|  ONNX / TensorRT / Core ML / TFLite  (runtime + hardware backend)            |
|       |                                                                      |
|       v   DEPLOY                                                             |
|  CLOUD GPU (throughput, batch)   vs   EDGE (latency, privacy, offline)       |
+------------------------------------------------------------------------------+
```

| Decision | Cloud | Edge (device) |
|----------|-------|---------------|
| Latency | Network round-trip | Local, low |
| Privacy | Data leaves device | Stays on device |
| Cost | Per-inference GPU cost | One-time hardware |
| Model size | Large OK | Must be small (quantized/pruned) |
| Connectivity | Required | Works offline |

```
   The throughput levers a VP cares about:
     - QUANTIZATION (INT8) -- the biggest single win; ~4x size, ~2-4x speed
     - BATCHING -- amortize GPU launch overhead in the cloud
     - HARDWARE -- NPU/TPU/edge accelerators vs general GPU
     - the right SPEED/ACCURACY POINT -- a smaller model that fits the SLA
       beats a SOTA model that misses latency
```

**Bridge — systems:** this is the same accuracy/latency/cost trade-off and the same
build-vs-buy, cloud-vs-edge calculus as any service-deployment decision. **Bridge — old →
new:** quantization is lossy compression applied to weights; the calibration step that
preserves accuracy is analogous to choosing quantization tables in JPEG (`signal-processing/`).

---

## Old World → New World Bridges

| You already know | Application analogue |
|------------------|----------------------|
| Sequence labeling / CTC (speech) | OCR recognition stage |
| PCA / SVD subspaces (Eigenfaces) | Replaced by learned face embeddings |
| ROC / sensitivity / specificity | Medical model evaluation |
| Lossy compression (JPEG) | Quantization of model weights |
| Cloud vs edge service deployment | Vision inference placement decision |
| Distillation / model compression | Shrinking nets for the edge |

---

## Decision Cheat Sheet

| I want to... | Use |
|---|---|
| Read text from images | Text detector + CRNN/CTC or transformer OCR |
| Recognize people not seen in training | Face embeddings (ArcFace) + nearest neighbor |
| Verify "same person?" | 1:1 embedding distance + threshold |
| Segment a tumor with little data | U-Net + transfer learning + augmentation |
| Weigh false negatives heavily | Optimize sensitivity; report Dice/AUC |
| Generate photoreal images | Diffusion (Stable Diffusion) |
| Generate from text prompts | Latent diffusion conditioned on CLIP text |
| Shrink a model 4x with little accuracy loss | INT8 quantization (+ QAT if needed) |
| Run on-device, offline, private | Edge deployment (TFLite/Core ML/TensorRT) |
| Maximize datacenter throughput | Batching + GPU/TPU + quantization |

---

## Common Confusion Points

### "Face recognition is just classification, right?"

No — that is why it is interesting. Classification assigns to a *fixed* label set; face
recognition must handle identities never seen in training and galleries that change daily.
The trick is metric learning: train an embedding so distance encodes identity, then match by
nearest neighbor. Adding a new person means adding one embedding to the gallery — no
retraining. Verification (1:1) and identification (1:N) are both distance operations on that
embedding space.

### "GAN vs diffusion — did diffusion just win?"

Diffusion dominates high-quality image generation today (stable training, no mode collapse,
better coverage of the distribution), and it powers the famous text-to-image systems. GANs
remain competitive where *sampling speed* matters — a GAN generates in one forward pass,
diffusion in many denoising steps (though distillation is closing that gap). It is a
quality/stability vs speed trade-off, not a clean knockout.

### "Why quantize? Won't INT8 wreck accuracy?"

Usually not. Networks are over-parameterized and robust to weight precision, so post-training
INT8 quantization with a small calibration set typically loses well under a percent of
accuracy while cutting model size ~4x and speeding inference 2–4x on integer hardware. When
the drop matters, quantization-aware training recovers it. For edge deployment it is the
single highest-leverage optimization — the difference between fitting on a phone NPU and not.

### "Medical vision is just classification with a CNN — what's special?"

The engineering constraints invert the usual priorities. Data is scarce and imbalanced;
inputs are often 3D volumes; and — critically — a confident wrong answer is dangerous, so
*calibrated uncertainty* and *sensitivity* matter more than raw accuracy. There is also
regulatory approval, clinician interpretability, and distribution shift between scanners and
hospitals. The model is the easy part; the validation, calibration, and deployment discipline
are the hard part.

### "These applications all reuse earlier guides — is there anything new here?"

That is exactly the point. Applications are *compositions* — OCR is detection plus
sequence recognition; face recognition is detection plus alignment plus embedding; AR is
SLAM plus detection plus rendering. The new content is the *recipe* (which components, in
what order, with what domain constraints) and the *deployment* layer that turns a model into
a shippable system. Mastering the components (guides 01–08) is what makes the applications
assemble cleanly.
