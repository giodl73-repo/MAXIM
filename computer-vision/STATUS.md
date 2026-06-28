# computer-vision/ — Status

**10 files | Complete ✅**

| File | Topic | Status |
|------|-------|--------|
| `00-OVERVIEW.md` | The vision landscape — image formation → classical CV → deep vision → geometry; the inverse-graphics framing | ✅ |
| `01-IMAGE-FORMATION.md` | Pinhole camera model, intrinsics/extrinsics, projection matrix, lens distortion, sampling and color | ✅ |
| `02-FILTERING-AND-FEATURES.md` | Convolution vs correlation, Gaussian/Sobel, edge detection (Canny), Harris corners, SIFT/ORB descriptors | ✅ |
| `03-SEGMENTATION.md` | Thresholding, region growing, watershed, graph cuts, Mean Shift, semantic vs instance vs panoptic | ✅ |
| `04-CLASSICAL-RECOGNITION.md` | HOG, SIFT bag-of-visual-words, spatial pyramids, SVM/boosting classifiers, Viola-Jones | ✅ |
| `05-DEEP-VISION.md` | CNNs as learned filters, receptive fields, the architecture lineage (AlexNet→ResNet), transfer learning, ViT | ✅ |
| `06-MULTIVIEW-GEOMETRY.md` | Epipolar geometry, the fundamental and essential matrices, stereo, triangulation, RANSAC, homographies | ✅ |
| `07-DETECTION-AND-TRACKING.md` | R-CNN/YOLO families, anchors, NMS, IoU/mAP metrics, Kalman filter, optical flow, multi-object tracking | ✅ |
| `08-3D-AND-SLAM.md` | Structure-from-motion, bundle adjustment, MVS depth, point clouds, visual SLAM, NeRF/Gaussian splatting | ✅ |
| `09-APPLICATIONS.md` | OCR, face recognition, medical imaging, generative vision (GANs/diffusion), deployment and edge inference | ✅ |

## Coverage Notes

Computer vision as the inverse problem of image formation: given pixels, recover the
scene that produced them. The directory is organized along the natural pipeline. It
opens with the landscape (the inverse-graphics framing and the three eras — classical,
geometric, deep), then descends. The forward model comes first (the pinhole camera,
intrinsics/extrinsics, sampling and color), then the classical signal-processing layer
(convolution, edges, corners, SIFT/ORB), then segmentation and pre-deep recognition
(HOG, bag-of-visual-words, Viola-Jones), then the deep era (CNNs as learned filters,
receptive fields, the architecture lineage, ViT). Multi-view geometry is the
mathematical spine: epipolar constraints, the fundamental and essential matrices,
triangulation, RANSAC. The detection/tracking and 3D/SLAM guides put these pieces in
motion, and the applications guide closes with OCR, faces, medical, and generative
vision plus deployment.

This directory is **vision specifically** — image formation, classical CV, deep vision,
and geometry. Generic ML (what a neural net is, optimization, training theory) lives in
`ai-engineering/` and `machine-learning-theory/`; this directory cross-references those
rather than re-teaching them.

**Bridges:** `signal-processing/` (convolution, sampling, Fourier, correlation),
`computer-graphics/` (the forward rendering model that vision inverts; projective
geometry; homogeneous coordinates), `mathematics/` (linear algebra, SVD, least squares,
projective geometry), `ai-engineering/` and `machine-learning-theory/` (training,
generalization, transformers), `optics/` (lens physics, the physics of image formation),
`control-theory/` (the Kalman filter for tracking).
