---
maxim_schema: maxim.frontmatter.v1
id: maxim:computer-vision:segmentation
kind: guide
module: computer-vision
section: computing-software
title: Segmentation
status: source-custody
source_custody: partial
current_path: computer-vision/03-SEGMENTATION.md
canonical_path: computer-vision/03-SEGMENTATION.md
backsource_ids: [proof-backfill:computer-vision:03-segmentation, git-history:computer-vision:03-segmentation]
concepts: [thresholding, region growing, watershed, graph cuts, mean shift, semantic segmentation, instance segmentation, panoptic]
root_concepts: [image segmentation]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# Segmentation

## The Big Picture: Partitioning the Image

Segmentation assigns every pixel to a group. The groups can be arbitrary regions
("these pixels belong together"), object classes ("these pixels are *road*"), or object
instances ("these pixels are *car #3*"). It is the bridge from low-level features
(guide 02) to scene understanding. The methods span a spectrum from a single global
threshold to a deep network that labels every pixel.

```
+------------------------------------------------------------------------------+
|                   SEGMENTATION: ASSIGN EVERY PIXEL A LABEL                   |
|                                                                              |
|   INPUT IMAGE             METHOD FAMILIES               OUTPUT               |
|   .---------.      .-------------------------.      .-------------.          |
|   |         |      | thresholding (global)   |      | region map  |          |
|   |  scene  | ---> | region growing / split  | ---> | each pixel  |          |
|   |         |      | watershed (topographic) |      | -> a label  |          |
|   |         |      | graph cuts / mean shift |      |             |          |
|   |         |      | DEEP (semantic/instance)|      |             |          |
|   '---------'      '-------------------------'      '-------------'          |
|                                                                              |
|   classical = group by appearance;  deep = group by learned semantics        |
+------------------------------------------------------------------------------+
```

---

## The Three Flavors (Know Which You Need)

The word "segmentation" hides three distinct tasks. Choosing the wrong one wastes
effort, so fix the target output first.

```
+------------------------------------------------------------------------------+
|             SEMANTIC vs INSTANCE vs PANOPTIC  (what the labels mean)         |
|                                                                              |
|  SEMANTIC            INSTANCE              PANOPTIC                          |
|  --------            --------              --------                          |
|  per-pixel CLASS     per-OBJECT mask       semantic + instance unified       |
|  "road, car, sky"    "car1, car2, car3"   "road (stuff) + car1,2,3 (things)" |
|                                                                              |
|  two cars share      two cars are          stuff gets a class; things get    |
|  ONE label "car"     SEPARATE masks        class AND an instance id          |
|                                                                              |
|  no object count     counts objects        complete scene labeling           |
+------------------------------------------------------------------------------+
```

| Task | Output | Distinguishes instances? | Labels every pixel? |
|------|--------|--------------------------|---------------------|
| **Semantic** | Class per pixel | No | Yes |
| **Instance** | Mask per object | Yes | No (only "things") |
| **Panoptic** | Class + instance id per pixel | Yes | Yes (stuff + things) |

"Stuff" = amorphous regions (sky, road, grass). "Things" = countable objects (car,
person). Panoptic unifies both.

---

## Layer 1: Thresholding — The Simplest Cut

Pick an intensity threshold `T`; pixels above are foreground, below are background.
Trivial but still the right tool for high-contrast cases (document scans, microscopy).

```
   Binary:   B(x,y) = 1 if I(x,y) > T else 0

   OTSU'S METHOD picks T automatically by maximizing between-class variance
   (equivalently minimizing within-class variance) over a bimodal histogram:

      histogram          T splits the two peaks
      count |   .-.          .-.
            |  /   \        /   \
            | /     \  T   /     \
            |/       \-|--/       \
            +----------+-----------> intensity
            background  | foreground
```

| Variant | Idea |
|---------|------|
| Global (Otsu) | One `T` for the whole image; assumes bimodal histogram |
| Adaptive / local | `T` varies per region; handles uneven lighting |
| Multi-level | Several thresholds → several classes |

---

## Layer 2: Region-Based — Growing and Splitting

Group pixels by similarity and adjacency rather than a global threshold.

```
   REGION GROWING               SPLIT-AND-MERGE (quadtree)
   --------------               -----------------
   start from seeds;            split image into quadrants
   add neighbor pixels that     recursively until each is
   meet a similarity test       homogeneous; then merge
   (intensity / color / texture) adjacent similar quadrants

   .--+--.        seed o     .--------.      .--+--+--.
   |  |  |   -->   grows  --> | merged |  <-- |  |  |  |  split then merge
   +--+--+        outward     | region |      +--+--+--+
   |  |o |                    '--------'      |  |  |  |
   '--+--'                                    '--+--+--'
```

These are intuitive but order-dependent and sensitive to seed/threshold choice. They
survive mostly in medical and microscopy pipelines where regions are well-behaved.

---

## Layer 3: Watershed — The Topographic Metaphor

Treat the gradient-magnitude image as a *terrain*: bright = high, dark = low. Flood from
the minima; where two basins meet, build a "dam" (the watershed line). Those dams are
the segment boundaries.

```
+------------------------------------------------------------------------------+
|                       WATERSHED  (immersion analogy)                         |
|                                                                              |
|   gradient as terrain:    /\        /\        each LOCAL MINIMUM is a basin; |
|                          /  \  /\  /  \       flooding the basins, the lines |
|              ___/\_____/    \/  \/    \___    where waters MEET are the      |
|             basin A        watershed    B     segment boundaries.            |
|                              line                                            |
|                                                                              |
|   Problem: OVER-SEGMENTATION (every tiny minimum starts a basin).            |
|   Fix: MARKER-CONTROLLED watershed -- flood only from user/auto markers.     |
+------------------------------------------------------------------------------+
```

Watershed excels at separating *touching* objects (cells, coins) that a threshold would
merge — the dam falls exactly at the pinch point. The classic failure is
over-segmentation from noise, cured by marker-controlled flooding.

---

## Layer 4: Mean Shift — Mode-Seeking in Feature Space

Mean Shift clusters pixels by climbing the density gradient in a joint
spatial-plus-color feature space. Each pixel walks uphill to a density mode; pixels
that converge to the same mode form a segment. No need to pre-specify the number of
clusters.

```
   Each pixel = a point in (x, y, r, g, b) space.
   Iterate: move each point to the mean of neighbors within a bandwidth h.

      .  .  .            modes (peaks of density)
       . o.  .   --->        O          O
      .  .. .             converged   converged
                          cluster 1   cluster 2

   bandwidth h_spatial controls region size; h_color controls color tolerance.
```

| Method | Needs #clusters? | Strength | Weakness |
|--------|------------------|----------|----------|
| K-means (on pixels) | Yes (`k`) | Simple, fast | Spherical clusters only |
| Mean Shift | No | Arbitrary cluster shapes | Bandwidth-sensitive, slow |
| SLIC superpixels | Yes (#superpixels) | Compact, fast over-segmentation | Not final objects |

Superpixels (e.g. **SLIC**) are a popular pre-processing step: over-segment into ~1000
compact regions, then reason about regions instead of pixels — a big speedup for graph
cuts and CRFs.

---

## Layer 5: Graph Cuts — Segmentation as Energy Minimization

Model the image as a graph: pixels are nodes; edges encode similarity. Add a source
(foreground) and sink (background) terminal. The **minimum cut** separating source from
sink is the optimal binary segmentation — and by the max-flow/min-cut theorem it is
computed exactly and efficiently.

```
+------------------------------------------------------------------------------+
|             GRAPH CUTS  (segmentation = min-cut = energy minimization)       |
|                                                                              |
|              SOURCE (foreground)                                             |
|              /    |     \                                                    |
|         t-link  t-link  t-link     t-links: how much each pixel "wants" to   |
|           |       |       |        be FG vs BG (DATA term)                   |
|         [p1]----[p2]----[p3]       n-links: penalty for cutting between      |
|           |       |       |        SIMILAR neighbors (SMOOTHNESS term)       |
|         t-link  t-link  t-link                                               |
|              \    |     /                                                    |
|              SINK (background)                                               |
|                                                                              |
|   Energy:  E(L) = SUM data(p, L_p)  +  lambda * SUM smooth(L_p, L_q)         |
|   Min-cut on this graph = global minimum of E for two labels (exact).        |
+------------------------------------------------------------------------------+
```

This is the cleanest example of the **MRF / energy-minimization** view of vision: a
*data term* pulls each pixel toward the label its appearance suggests, a *smoothness
term* (a pairwise Markov Random Field) penalizes label changes between similar
neighbors, and `lambda` trades them off. **GrabCut** is the famous interactive version:
the user drags a box, and iterated graph cuts refine a Gaussian-mixture color model.

**Bridge — optimization / TCS:** two-label graph cut is exactly solvable via max-flow
(Ford-Fulkerson, Boykov-Kolmogorov). Multi-label is NP-hard in general but
alpha-expansion gives strong approximate solutions. The same min-cut machinery appears
in stereo (guide 06) and image stitching seam selection.

---

## Layer 6: Deep Segmentation — Learning the Labels

Classical methods group by *appearance*; deep methods group by learned *semantics*. The
breakthrough was the **Fully Convolutional Network** (FCN, 2015): replace a
classifier's dense layers with convolutions so the output is a dense label map at the
input resolution.

```
+------------------------------------------------------------------------------+
|              DEEP SEGMENTATION ARCHITECTURES  (encoder-decoder)              |
|                                                                              |
|   ENCODER (downsample, learn what)        DECODER (upsample, restore where)  |
|   image -> conv -> conv -> ... -> small -> upconv -> ... -> per-pixel labels |
|              |        |                       ^         ^                    |
|              +--------+-----skip connections--+---------+                    |
|                       (U-Net: copy fine detail across to recover boundaries) |
|                                                                              |
|   FCN     : first dense per-pixel net                                        |
|   U-Net   : symmetric encoder-decoder + skips (medical imaging standard)     |
|   DeepLab : atrous/dilated convolution + CRF for sharp boundaries            |
|   Mask R-CNN : detection + a mask head -> INSTANCE segmentation              |
|   SAM     : promptable, foundation-model segmentation (2023)                 |
+------------------------------------------------------------------------------+
```

| Architecture | Task | Key idea |
|--------------|------|----------|
| **FCN** | Semantic | Fully convolutional dense prediction |
| **U-Net** | Semantic (medical) | Encoder-decoder + skip connections |
| **DeepLab** | Semantic | Atrous convolution for large receptive field |
| **Mask R-CNN** | Instance | Add a per-RoI mask branch to detection (guide 07) |
| **SAM** | Promptable | Foundation model; segment "anything" from a prompt |

The CNN/transformer machinery itself is covered in guide 05; here the point is that the
*output* is a label map, and instance segmentation (Mask R-CNN) reuses the detector of
guide 07.

---

## Old World → New World Bridges

| You already know | Segmentation analogue |
|------------------|------------------------|
| Min-cut / max-flow (algorithms) | Graph-cut segmentation is literally min-cut |
| Clustering (k-means, EM) | Mean Shift / SLIC group pixels in feature space |
| Markov Random Fields / CRFs | The data+smoothness energy is an MRF |
| Quadtrees / spatial subdivision | Split-and-merge region segmentation |
| Encoder-decoder (autoencoders) | U-Net is an encoder-decoder with skips |

---

## Decision Cheat Sheet

| I want to... | Use |
|---|---|
| Binarize a high-contrast scan | Otsu thresholding |
| Threshold under uneven lighting | Adaptive (local) thresholding |
| Separate touching round objects | Marker-controlled watershed |
| Cluster without picking k | Mean Shift |
| Fast over-segmentation for downstream | SLIC superpixels |
| Interactive foreground extraction | GrabCut (graph cuts) |
| Label every pixel by class | Semantic seg (FCN/U-Net/DeepLab) |
| Separate object instances | Instance seg (Mask R-CNN) |
| Full scene (stuff + things) | Panoptic segmentation |
| Segment arbitrary objects from a prompt | SAM |

---

## Common Confusion Points

### "Semantic vs instance — when does the difference actually matter?"

Counting and tracking. If you need to know *how many* cars or follow car #3 across
frames, you need instance (or panoptic) segmentation — semantic merges all cars into one
"car" blob. If you only need "what fraction of this pixel-map is road," semantic is
enough and cheaper. Autonomous driving needs panoptic: road as stuff, each pedestrian
as a distinct thing.

### "Watershed over-segments everything — why use it?"

Raw watershed floods from every local minimum, so noise spawns thousands of basins. The
practical version is **marker-controlled**: you supply markers (from thresholding,
distance transform, or clicks) and flood only from those. With good markers it is the
best classical tool for splitting *touching* objects, which thresholding and region
growing cannot do.

### "Graph cuts give the global optimum — so why did deep learning win?"

Graph cuts optimize a *hand-designed* energy with a *fixed* appearance model. They are
globally optimal *for that energy*, but the energy encodes no semantics — it cannot know
a brown blob is a dog. Deep nets learn the appearance-to-class mapping from data. Modern
systems sometimes combine them: a CNN provides the data term, a CRF/graph-cut sharpens
boundaries (DeepLab's original design).

### "Is segmentation just detection with masks?"

They overlap but differ in output granularity. Detection (guide 07) gives a *box* per
object; instance segmentation gives a per-pixel *mask*. Mask R-CNN makes the link
explicit: it is a detector (box proposals) plus a mask head. Semantic segmentation has
no boxes at all — it is pure per-pixel classification with no notion of objects.
