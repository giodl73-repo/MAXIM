---
maxim_schema: maxim.frontmatter.v1
id: maxim:computer-vision:classical-recognition
kind: guide
module: computer-vision
section: computing-software
title: Classical Recognition (Pre-Deep)
status: source-custody
source_custody: partial
current_path: computer-vision/04-CLASSICAL-RECOGNITION.md
canonical_path: computer-vision/04-CLASSICAL-RECOGNITION.md
backsource_ids: [proof-backfill:computer-vision:04-classical-recognition, git-history:computer-vision:04-classical-recognition]
concepts: [HOG, bag of visual words, spatial pyramid, SVM, boosting, Viola-Jones, feature encoding]
root_concepts: [object recognition]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# Classical Recognition (Pre-Deep)

## The Big Picture: Hand-Crafted Features Plus a Classifier

Before 2012, recognition was a two-stage pipeline: a *fixed*, hand-engineered feature
extractor turned an image into a vector, and a *learned* classifier mapped that vector to
a label. The art was in the features (HOG, SIFT) and the encoding (bag-of-visual-words);
the classifier (SVM, boosting) was off-the-shelf. Understanding this pipeline is the key
to understanding what deep learning automated — a CNN (guide 05) folds *both* stages into
one learned function.

```
+------------------------------------------------------------------------------+
|             THE CLASSICAL RECOGNITION PIPELINE  (image -> label)             |
|                                                                              |
|   IMAGE        FEATURE EXTRACT      ENCODE            CLASSIFY               |
|   .-----.      .-------------.      .-----------.     .-----------.          |
|   |     | ---> | HOG / SIFT  | ---> | fixed-len | --> | SVM /     | -> "cat" |
|   |     |      | dense or    |      | vector    |     | boosting/ |          |
|   |     |      | keypoints   |      | (BoVW,    |     | random    |          |
|   '-----'      '-------------'      |  pyramid) |     | forest)   |          |
|                  HAND-DESIGNED       HAND-DESIGNED      LEARNED              |
|                                                                              |
|   Only the last box is trained. Deep learning makes ALL of it learned.       |
+------------------------------------------------------------------------------+
```

---

## Layer 1: HOG — Histogram of Oriented Gradients

HOG (Dalal & Triggs, 2005) is the workhorse descriptor for *detection of structured
objects* — most famously pedestrians. The insight: object appearance and shape are
captured well by the *distribution of local edge orientations*, independent of exact
position.

```
+------------------------------------------------------------------------------+
|                          HOG DESCRIPTOR (4 steps)                            |
|                                                                              |
|  1. GRADIENTS    compute Gx, Gy per pixel -> magnitude + orientation         |
|  2. CELLS        divide window into small cells (e.g. 8x8 px)                |
|                  build a histogram of orientations per cell (e.g. 9 bins)    |
|  3. BLOCKS       group cells into overlapping blocks (e.g. 2x2 cells)        |
|                  NORMALIZE within each block (contrast invariance)           |
|  4. CONCATENATE  all block histograms -> one long feature vector             |
|                                                                              |
|     +--+--+--+--+      each cell ->  \ | /  histogram of                     |
|     |  |  |  |  |                    -- + --  gradient orientations          |
|     +--+--+--+--+                    / | \   (9 bins, 0..180 deg)            |
|     |  |  |  |  |      block = 2x2 cells, L2-normalized together             |
|     +--+--+--+--+                                                            |
+------------------------------------------------------------------------------+
```

Block-level normalization is the crucial trick: it cancels local contrast and
illumination changes. HOG + a linear SVM was the state-of-the-art pedestrian detector
for years. **Bridge:** HOG is essentially a coarse, dense, fixed version of SIFT's
gradient-histogram descriptor (guide 02) — same gradient-orientation idea, computed on a
regular grid rather than at sparse keypoints.

---

## Layer 2: Bag-of-Visual-Words — Borrowing from Text Retrieval

For *whole-image classification* with many local features, you need a fixed-length
vector regardless of how many keypoints an image has. Bag-of-Visual-Words (BoVW) solves
this by quantizing descriptors into a "visual vocabulary" — the direct analogue of
bag-of-words in document retrieval.

```
+------------------------------------------------------------------------------+
|            BAG-OF-VISUAL-WORDS  (text bag-of-words, for images)              |
|                                                                              |
|  1. EXTRACT    dense or keypoint SIFT descriptors from many images           |
|  2. CLUSTER    k-means over all descriptors -> k cluster centers =           |
|                the "VISUAL VOCABULARY" (each center is a "visual word")      |
|  3. ASSIGN     each descriptor -> nearest visual word                        |
|  4. HISTOGRAM  count word occurrences -> k-D histogram = the image vector    |
|                                                                              |
|   image -> {sift1, sift2, ...} -> [w3,w17,w3,w42,...] -> histogram over k    |
|                                                                              |
|   Like a document = a histogram of words, an image = a histogram of          |
|   visual words. Order/position discarded ("bag").                            |
+------------------------------------------------------------------------------+
```

**Bridge — information retrieval:** this is exactly the term-frequency vector from
document search, and the same refinements apply: **tf-idf** weighting down-weights
ubiquitous visual words; an **inverted index** enables fast image retrieval. This is the
foundation of pre-deep content-based image search.

The "bag" discards all spatial layout — a face scrambled into pieces has the same BoVW
vector as an intact face. That weakness motivates the next layer.

---

## Layer 3: Spatial Pyramid — Putting Position Back In

The spatial pyramid (Lazebnik et al., 2006) restores coarse spatial information by
computing BoVW histograms over a pyramid of increasingly fine grid cells and
concatenating them.

```
   Level 0          Level 1            Level 2
   .-------.        .---+---.          .-+-+-+-.
   |       |        |   |   |          +-+-+-+-+
   | whole |        +---+---+          +-+-+-+-+
   | image |        |   |   |          +-+-+-+-+
   '-------'        '---+---'          '-+-+-+-'
   1 histogram      4 histograms       16 histograms

   Concatenate all levels (weighted) -> a spatially-aware image vector.
   "A face has eyes in the TOP cells, mouth in the BOTTOM cells."
```

This was the dominant whole-image classification representation immediately before deep
learning. **Bridge:** the spatial pyramid prefigures the spatial-pooling hierarchy of a
CNN — coarse-to-fine spatial bins are what pooling layers (guide 05) learn to build.

---

## Layer 4: The Classifiers

The feature vector feeds a learned classifier. These are general ML methods covered in
`machine-learning-theory/`; here is how they slot into vision.

| Classifier | How it works | Vision role |
|------------|--------------|-------------|
| **Linear SVM** | Max-margin hyperplane in feature space | HOG + linear SVM detection; fast at test time |
| **Kernel SVM** | Implicit nonlinear mapping (RBF, chi-squared) | BoVW classification; chi-squared kernel fits histograms |
| **AdaBoost** | Weighted sum of weak learners | Viola-Jones face detection (next layer) |
| **Random Forest** | Ensemble of decision trees | Kinect body-part labeling, fast pixel classifiers |
| **Nearest neighbor** | Match to labeled exemplars | Simple retrieval baselines |

```
   LINEAR SVM in HOG space:        the learned weight vector w, reshaped to
                                   the HOG cell grid, LOOKS like the object --
   w . x + b  > 0  -> object       a "template" of oriented edges. A sliding
                < 0  -> background  window evaluates w.x+b at every location.
```

**Bridge — ML theory:** the SVM's max-margin objective and VC-dimension generalization
bounds are developed in `machine-learning-theory/`. For histogram features, the
**chi-squared** and **histogram-intersection** kernels outperform RBF because they
respect the histogram geometry.

---

## Layer 5: Viola-Jones — Real-Time Face Detection

Viola-Jones (2001) was the first robust real-time face detector and shipped in every
point-and-shoot camera. It is a masterclass in classical engineering: three ideas
combine to make a scanning detector run at frame rate on 2001 hardware.

```
+------------------------------------------------------------------------------+
|                      VIOLA-JONES  (three key ideas)                          |
|                                                                              |
|  1. HAAR FEATURES        sum(white region) - sum(black region):              |
|       +----+----+        captures edges/lines (e.g. eyes darker than cheeks) |
|       |XXXX|    |                                                            |
|       |XXXX|    |        thousands of such rectangle features per window     |
|       +----+----+                                                            |
|                                                                              |
|  2. INTEGRAL IMAGE       precompute a summed-area table: ANY rectangle sum   |
|                          in O(1) (4 lookups), regardless of size             |
|                                                                              |
|  3. ADABOOST CASCADE     boost selects the few best features; arrange as a   |
|                          CASCADE -- early simple stages reject most windows  |
|                          instantly; only face-like windows reach later       |
|                          stages -> huge average speedup                      |
|                                                                              |
|   cascade:  [stage1]--reject-->X   [stage2]--reject-->X  ...  [stageN]->FACE |
|                |pass                |pass                                    |
|                v                    v                                        |
+------------------------------------------------------------------------------+
```

The integral image is the standout trick: a summed-area table lets you compute the sum
over *any* rectangle in constant time, so a Haar feature costs the same whether it is
2x2 or 200x200 pixels. The cascade exploits the fact that *most* image windows are
obviously not faces — reject them cheaply and spend computation only on hard cases.

**Bridge — graphics:** the summed-area table is the same data structure used for fast
box filtering and mipmap generation in `computer-graphics/`. **Bridge — old → new:** the
cascade-of-rejectors idea reappears as the multi-stage / coarse-to-fine design in modern
detectors (guide 07).

---

## The Whole Pipeline, Compared

```
+------------------------------------------------------------------------------+
|            CLASSICAL vs DEEP RECOGNITION  (what got automated)               |
|                                                                              |
|  CLASSICAL (pre-2012)                  DEEP (2012+)                          |
|  --------------------                  -----------                           |
|  feature design: HOG, SIFT (FIXED)     features: LEARNED conv filters        |
|  encoding: BoVW, spatial pyramid       encoding: LEARNED pooling hierarchy   |
|  classifier: SVM / boosting (LEARNED)  classifier: LEARNED softmax head      |
|                                                                              |
|  human picks features, machine          machine learns features AND          |
|  learns only the final boundary         classifier end-to-end from pixels    |
|                                                                              |
|  interpretable, low-data, modular       higher accuracy, data-hungry,        |
|                                         opaque, monolithic                   |
+------------------------------------------------------------------------------+
```

---

## Old World → New World Bridges

| You already know | Classical recognition analogue |
|------------------|--------------------------------|
| Bag-of-words / tf-idf / inverted index (search) | Bag-of-visual-words image retrieval |
| k-means clustering | Builds the visual vocabulary |
| Max-margin / SVM theory | The classical recognizer's decision stage |
| Summed-area table / prefix sums | Viola-Jones integral image |
| Boosting (ensemble methods) | AdaBoost feature selection + cascade |
| Sliding-window scan | Template detection (HOG+SVM, Viola-Jones) |

---

## Decision Cheat Sheet

| I want to... | Use |
|---|---|
| Detect rigid structured objects (pedestrians) | HOG + linear SVM, sliding window |
| Classify whole images, pre-deep | BoVW + spatial pyramid + kernel SVM |
| Search a large image database | BoVW + tf-idf + inverted index |
| Detect faces in real time on weak hardware | Viola-Jones (Haar + integral image + cascade) |
| Compare histogram features | Chi-squared / histogram-intersection kernel |
| Fast pixel-wise classification | Random forest |
| Understand what a CNN automated | This whole pipeline → one learned net |

---

## Common Confusion Points

### "Why learn classical recognition if deep learning beats it?"

Three reasons. First, it explains *what deep learning does* — a CNN is a learned version
of feature-extract-then-classify, so the classical pipeline is the conceptual skeleton.
Second, classical methods still win when data is scarce, interpretability is required, or
compute is tiny (Viola-Jones still runs on microcontrollers). Third, hybrid systems use
classical features (SIFT/ORB) inside geometric estimators (guides 06, 08) where deep
nets offer no advantage.

### "Bag-of-visual-words throws away position — isn't that fatal?"

For *classification* ("is there a beach in this image?") global statistics often suffice,
so BoVW works surprisingly well. For *localization* it fails, which is why the spatial
pyramid adds coarse position back, and why detection (guide 07) needs explicit spatial
reasoning. The progression BoVW → spatial pyramid → CNN is a steady reintroduction of
spatial structure.

### "HOG vs SIFT — they both use gradient histograms. Same thing?"

Same building block, different deployment. SIFT computes a gradient-orientation histogram
*at sparse, scale-and-rotation-normalized keypoints* for matching. HOG computes them
*densely on a fixed grid* for detection, and adds block normalization for contrast
invariance. SIFT is for correspondence; HOG is for sliding-window detection.

### "What made Viola-Jones fast — the features or the cascade?"

Both, working together. The integral image makes each Haar feature O(1) regardless of
size; the cascade makes the *average* window cost tiny by rejecting easy negatives in the
first one or two stages. Neither alone would hit frame rate on 2001 hardware. The cascade
is the more transferable idea — early-exit / coarse-to-fine rejection recurs throughout
efficient vision.
