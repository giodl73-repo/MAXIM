---
maxim_schema: maxim.frontmatter.v1
id: maxim:computer-vision:detection-and-tracking
kind: guide
module: computer-vision
section: computing-software
title: Detection and Tracking
status: source-custody
source_custody: partial
current_path: computer-vision/07-DETECTION-AND-TRACKING.md
canonical_path: computer-vision/07-DETECTION-AND-TRACKING.md
backsource_ids: [proof-backfill:computer-vision:07-detection-and-tracking, git-history:computer-vision:07-detection-and-tracking]
concepts: [object detection, R-CNN, YOLO, non-maximum suppression, IoU, mAP, Kalman filter, optical flow, tracking]
root_concepts: [object detection]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# Detection and Tracking

## The Big Picture: Where, Not Just What

Classification (guide 05) answers *what* is in an image. Detection answers *what and
where* — it returns a box and a label per object. Tracking extends detection through
time — it follows each object across video frames, maintaining identity. This guide
covers the two detector families (region-based R-CNN and single-shot YOLO), the metrics
that govern them (IoU, mAP), the cleanup step (NMS), and the temporal machinery (Kalman
filtering, optical flow, multi-object tracking).

```
+------------------------------------------------------------------------------+
|              CLASSIFY -> DETECT -> TRACK  (adding location, then time)       |
|                                                                              |
|  CLASSIFY            DETECT                    TRACK                         |
|  "cat"              "cat @ box1, 0.9"         "cat#3 @ box1 -> box1' -> ..." |
|                     "dog @ box2, 0.8"          maintain IDENTITY over frames |
|                                                                              |
|  .-------.          .-------.                  frame t      frame t+1        |
|  | whole |          | [box] |                  .--[#3]--.   .---[#3]-.       |
|  | image |          |  [box]|                  |        |   |        |       |
|  '-------'          '-------'                  '--------'   '--------'       |
|   one label         many boxes + labels        boxes LINKED across time      |
+------------------------------------------------------------------------------+
```

---

## Layer 1: IoU — The Metric Everything Rests On

**Intersection over Union** measures how well a predicted box matches a ground-truth box.
It is the atom of every detection metric, the matching criterion in NMS, and the
assignment cost in tracking.

```
   IoU = area(intersection) / area(union)

        +----------+
        |  GT      |          intersection = overlap region
        |    +-----+----+     union = total area covered by both
        |    | // |    |
        +----+----+    |      IoU = 0   -> no overlap
             | pred    |      IoU = 1   -> perfect match
             +---------+      IoU > 0.5 -> conventionally a "correct" detection
```

A detection is counted **correct** if its IoU with a ground-truth box of the same class
exceeds a threshold (commonly 0.5). Higher thresholds (0.75, or the 0.5:0.95 average used
by COCO) demand tighter localization.

---

## Layer 2: NMS — Removing Duplicate Boxes

Detectors fire many overlapping boxes on the same object. **Non-Maximum Suppression**
keeps the highest-confidence box and removes its near-duplicates by IoU.

```
+------------------------------------------------------------------------------+
|                  NON-MAXIMUM SUPPRESSION (per class)                         |
|                                                                              |
|  1. SORT all boxes by confidence (descending)                                |
|  2. TAKE the top box; add it to the KEEP list                                |
|  3. REMOVE every remaining box with IoU > threshold against it               |
|  4. REPEAT with the next highest-confidence survivor                         |
|                                                                              |
|   before NMS:  [==][=][===]  three boxes on one object                       |
|   after NMS:   [===]          keep the most confident, drop overlaps         |
|                                                                              |
|   Soft-NMS: instead of deleting, DECAY overlapping boxes' scores             |
|   (better for crowded scenes where objects truly overlap).                   |
+------------------------------------------------------------------------------+
```

NMS is the standard post-process for almost every detector. Its IoU threshold is a
tuning knob: too low merges distinct nearby objects; too high leaves duplicates.

---

## Layer 3: mAP — The Detection Scoreboard

**Mean Average Precision** is the headline detection metric. Build it up:
precision-recall → average precision (area under the PR curve) per class → mean over
classes.

```
+------------------------------------------------------------------------------+
|                        BUILDING UP mAP                                       |
|                                                                              |
|  precision = TP / (TP + FP)     "of my detections, how many are right?"      |
|  recall    = TP / (TP + FN)     "of real objects, how many did I find?"      |
|                                                                              |
|  Vary the confidence threshold -> trace a PRECISION-RECALL curve.            |
|                                                                              |
|   precision 1|`-._                                                           |
|              |    `-._         AP = area under this PR curve (per class)     |
|              |        `-.__                                                  |
|              +-------------`---> recall                                      |
|                                                                              |
|  AP   = area under PR curve for ONE class at ONE IoU threshold               |
|  mAP  = mean of AP over ALL classes                                          |
|  COCO mAP = mean over classes AND IoU thresholds 0.50:0.05:0.95              |
+------------------------------------------------------------------------------+
```

| Metric | Meaning |
|--------|---------|
| AP@0.5 | Average precision at IoU ≥ 0.5 (PASCAL VOC convention) |
| AP@0.75 | Stricter localization |
| mAP (COCO) | Averaged over IoU 0.5–0.95 *and* classes — the standard headline |
| AR | Average recall (object-finding ability) |

**Bridge — ML:** precision/recall and AUC are the same concepts as in any classifier
evaluation; detection adds the IoU-based notion of a "correct" positive.

---

## Layer 4: Two-Stage Detectors — The R-CNN Family

The first deep detectors *propose* candidate regions, then *classify* each. Accuracy was
high; speed was the problem the lineage solved.

```
+------------------------------------------------------------------------------+
|                 R-CNN LINEAGE  (two-stage: propose -> classify)              |
|                                                                              |
|  R-CNN (2014)      ~2000 region proposals (selective search) ->              |
|                    run the CNN on EACH crop -> classify+regress. SLOW.       |
|      |                                                                       |
|  Fast R-CNN        run the CNN ONCE on the whole image; RoI-pool features    |
|                    for each proposal. Much faster.                           |
|      |                                                                       |
|  Faster R-CNN      replace selective search with a learned REGION PROPOSAL   |
|                    NETWORK (RPN) sharing the backbone -> end-to-end, fast.   |
|      |                                                                       |
|  Mask R-CNN        add a per-RoI MASK branch -> instance segmentation        |
|                    (the link back to guide 03)                               |
+------------------------------------------------------------------------------+
```

The Region Proposal Network introduced **anchors**: a fixed grid of reference boxes at
multiple scales and aspect ratios. The network predicts, per anchor, an objectness score
and a box refinement. Anchors became the dominant detection mechanism for years.

---

## Layer 5: Single-Stage Detectors — The YOLO Family

YOLO ("You Only Look Once") reframed detection as a *single* regression: one forward pass
of the image directly outputs all boxes and classes on a grid. No separate proposal
stage — hence real-time speed.

```
+------------------------------------------------------------------------------+
|                 YOLO  (single-stage: one pass -> all boxes)                  |
|                                                                              |
|  divide image into an SxS grid. Each cell predicts:                          |
|    - B bounding boxes (x, y, w, h) + an objectness/confidence                |
|    - class probabilities                                                     |
|  ALL predicted in ONE network pass -> then NMS to clean up.                  |
|                                                                              |
|   +--+--+--+--+      each cell: "is an object centered here? box + class"    |
|   |  |  |  |  |                                                              |
|   +--+--+--+--+      vs R-CNN's propose-then-classify, YOLO regresses        |
|   |  |##|  |  |      everything at once -> faster, slightly less accurate    |
|   +--+--+--+--+      on small/dense objects (historically).                  |
|   |  |  |  |  |                                                              |
|   +--+--+--+--+                                                              |
+------------------------------------------------------------------------------+
```

```
+------------------------------------------------------------------------------+
|              TWO-STAGE vs SINGLE-STAGE  (accuracy vs speed)                  |
|                                                                              |
|  TWO-STAGE (Faster R-CNN)              SINGLE-STAGE (YOLO, SSD, RetinaNet)   |
|  --------------------------            ----------------------------------    |
|  propose regions, then classify        regress boxes+classes in one pass     |
|  higher accuracy, esp. small obj       faster, real-time                     |
|  slower                                slightly lower accuracy (gap closing) |
|  anchors via RPN                       dense anchors / anchor-free (FCOS)    |
|                                                                              |
|  RetinaNet's FOCAL LOSS fixed the class imbalance that hurt single-stage     |
|  detectors (vast majority of anchors are background).                        |
|                                                                              |
|  DETR (2020): transformer, set-prediction, NO anchors, NO NMS.               |
+------------------------------------------------------------------------------+
```

| Detector | Type | Hallmark |
|----------|------|----------|
| Faster R-CNN | Two-stage | RPN + anchors; accuracy benchmark |
| YOLO (v1→v8+) | Single-stage | Real-time grid regression |
| SSD | Single-stage | Multi-scale feature maps |
| RetinaNet | Single-stage | Focal loss fixes foreground/background imbalance |
| FCOS | Single-stage | Anchor-free (per-pixel prediction) |
| DETR | Transformer | Set prediction; no anchors, no NMS |

---

## Layer 6: Optical Flow — Pixel Motion Between Frames

Optical flow estimates the apparent motion of each pixel between consecutive frames — a
dense `(u, v)` displacement field. It rests on the **brightness constancy** assumption: a
moving point keeps its intensity.

```
   Brightness constancy:  I(x, y, t) = I(x+u, y+v, t+1)

   First-order Taylor expansion gives the OPTICAL FLOW CONSTRAINT EQUATION:

        Ix*u + Iy*v + It = 0      (one equation, two unknowns -> ill-posed:
                                   the "aperture problem")

   Solutions add a constraint:
     LUCAS-KANADE: assume constant flow in a window -> least squares (2x2
                   system uses the SAME structure matrix as Harris, guide 02)
     HORN-SCHUNCK: add a global smoothness term -> variational, dense flow
     RAFT (deep):  learn flow with iterative refinement -> current SOTA
```

The **aperture problem** — one equation, two unknowns — is why flow needs an extra
assumption (local smoothness or a window). Lucas-Kanade's window least-squares uses the
same gradient structure matrix `M` as the Harris detector (guide 02): flow is well-posed
exactly where `M` has two strong eigenvalues, i.e. at corners.

---

## Layer 7: The Kalman Filter — Tracking as Recursive Estimation

To follow an object through video you maintain a *belief* about its state (position,
velocity) and update it each frame. The **Kalman filter** is the optimal recursive
estimator for a linear-Gaussian system — predict the state forward, then correct with the
new measurement.

```
+------------------------------------------------------------------------------+
|                THE KALMAN FILTER  (predict-correct loop)                     |
|                                                                              |
|  STATE x: [position, velocity]   COVARIANCE P: uncertainty                   |
|                                                                              |
|  PREDICT (motion model F):                                                   |
|     x_pred = F x         (where will it be next frame?)                      |
|     P_pred = F P F^T + Q (uncertainty GROWS)                                 |
|                                                                              |
|  CORRECT (measurement z, model H):                                           |
|     K = P_pred H^T (H P_pred H^T + R)^-1     <- KALMAN GAIN                  |
|     x = x_pred + K (z - H x_pred)            <- blend prediction + detection |
|     P = (I - K H) P_pred                     <- uncertainty SHRINKS          |
|                                                                              |
|   Gain K trades trust between the motion prediction and the new detection.   |
|   Nonlinear motion -> Extended (EKF) or Unscented (UKF) Kalman filter.       |
+------------------------------------------------------------------------------+
```

**Bridge — control theory:** the Kalman filter is the same estimator developed in
`control-theory/`; tracking is one of its purest applications. The state-space, the
predict-correct cycle, and the gain are identical — vision just supplies the
measurements (detections) and the motion model.

---

## Layer 8: Multi-Object Tracking — Tracking-by-Detection

The dominant paradigm runs a detector each frame and *associates* detections to existing
tracks. Two pieces: motion prediction (Kalman) and data association (matching).

```
+------------------------------------------------------------------------------+
|                  TRACKING-BY-DETECTION  (e.g. SORT / DeepSORT)               |
|                                                                              |
|  frame t: tracks {T1, T2, T3}  +  new detections {d1, d2, d3, d4}            |
|                                                                              |
|  1. PREDICT    Kalman-predict each track's box for this frame                |
|  2. ASSOCIATE  build a cost matrix (1 - IoU, or appearance distance);        |
|                solve assignment with the HUNGARIAN algorithm                 |
|  3. UPDATE     matched tracks: Kalman-correct with the detection             |
|  4. MANAGE     unmatched detections -> new tracks;                           |
|                unmatched tracks -> age out / delete                          |
|                                                                              |
|   SORT: IoU + Kalman + Hungarian.                                            |
|   DeepSORT: adds a learned APPEARANCE embedding -> survives occlusion.       |
+------------------------------------------------------------------------------+
```

**Bridge — operations research:** data association is the assignment problem, solved
optimally by the Hungarian algorithm — the same combinatorial-optimization tool from
`operations-research/`. The identity-switch problem (two tracks swapping IDs after an
occlusion) is why DeepSORT adds an appearance embedding to disambiguate.

---

## Old World → New World Bridges

| You already know | Detection/tracking analogue |
|------------------|------------------------------|
| Precision/recall, AUC (ML eval) | mAP is PR-curve area + IoU correctness |
| Kalman filter / state estimation (control) | Object tracking's predict-correct core |
| Assignment problem / Hungarian (OR) | Detection-to-track data association |
| Structure tensor / eigen-analysis (guide 02) | Lucas-Kanade flow well-posedness |
| Greedy non-max / dedup | NMS removing duplicate boxes |

---

## Decision Cheat Sheet

| I want to... | Use |
|---|---|
| Highest detection accuracy | Faster R-CNN (two-stage) |
| Real-time detection | YOLO (single-stage) |
| Fix foreground/background imbalance | RetinaNet (focal loss) |
| Detection without anchors or NMS | DETR (transformer set prediction) |
| Box + per-object mask | Mask R-CNN |
| Remove duplicate boxes | NMS (Soft-NMS in crowds) |
| Score a detector | mAP (COCO 0.5:0.95) |
| Dense pixel motion | Optical flow (Lucas-Kanade / RAFT) |
| Follow one object smoothly | Kalman filter |
| Track many objects with IDs | SORT / DeepSORT (Kalman + Hungarian) |

---

## Common Confusion Points

### "Two-stage vs single-stage — is one just obsolete?"

It is a genuine accuracy/speed trade-off, though the gap has narrowed. Two-stage (Faster
R-CNN) still edges ahead on small and dense objects because the proposal stage focuses
computation; single-stage (YOLO) dominates real-time use. RetinaNet's focal loss and
anchor-free designs (FCOS) closed much of the accuracy gap, and DETR removed anchors and
NMS entirely. Pick by your latency budget, not by "newest."

### "IoU shows up everywhere — metric, NMS, tracking. Same threshold?"

Same *quantity*, different *thresholds* for different jobs. As an evaluation criterion,
IoU ≥ 0.5 (or 0.5:0.95) marks a "correct" detection. In NMS, the IoU threshold decides
when two boxes are duplicates (often ~0.5–0.7). In tracking association, `1 - IoU` is a
*cost*. The number is tuned per role; do not reuse one value blindly.

### "Optical flow vs tracking — aren't both 'motion'?"

Different granularity. Optical flow is *dense and pixel-level* — a displacement for every
pixel, with no notion of objects. Tracking is *sparse and object-level* — a box and a
persistent identity per object. Flow can *feed* tracking (predict where pixels went), but
tracking adds identity and a motion model. The Kalman filter operates on object state, not
pixels.

### "Why a Kalman filter when the detector already gives me boxes each frame?"

Detections are noisy, occasionally missing, and have no identity link across frames. The
Kalman filter smooths the trajectory, *predicts* through frames where the detector misses
(brief occlusion), and provides the predicted box that data association matches against.
It turns a sequence of independent detections into coherent, identified tracks. Detection
answers "where now"; the filter answers "where next, and which object."

### "DETR has no NMS — how does it avoid duplicate boxes?"

DETR predicts a *fixed set* of boxes and trains with a bipartite (Hungarian) matching loss
that assigns exactly one prediction to each ground-truth object. Because duplicates are
penalized during training, the model learns not to emit them — so no NMS post-process is
needed. It moves the deduplication from a hand-coded test-time step into the learned
objective.
