# Image Processing: Geometric Correction, Atmospheric Correction, Classification

## The Big Picture

An EO image is a measurement of electromagnetic energy, distorted by the sensor optics, the satellite's position and attitude, the atmosphere, and terrain geometry. Image processing removes these distortions and extracts thematic information. The pipeline is always: geometric -> radiometric -> thematic.

```
PROCESSING LAYERS

  RAW IMAGE (DN values)
         |
         | GEOMETRIC CORRECTION
         v
  GEOREFERENCED IMAGE (pixel = known lat/lon)
         |
         | ATMOSPHERIC CORRECTION
         v
  SURFACE REFLECTANCE (physics: what the surface actually reflects)
         |
         | CLASSIFICATION / FEATURE EXTRACTION
         v
  THEMATIC MAP (land cover, change, index, temperature)
         |
         | ACCURACY ASSESSMENT
         v
  VALIDATED PRODUCT (confusion matrix, kappa, F1)
```

---

## Geometric Correction

Raw imagery has geometric distortions from four sources:

```
DISTORTION SOURCES

1. SENSOR GEOMETRY (interior orientation)
   Lens distortion: radial and tangential
   Focal length variation across array
   Detector misregistration
   -> Corrected by sensor calibration (lab + in-orbit)

2. PLATFORM ATTITUDE AND POSITION (exterior orientation)
   Satellite not perfectly nadir-pointing
   Roll, pitch, yaw variations (IMU measurements)
   GPS position error
   -> Corrected by: collinearity equations from star trackers + GNSS

3. EARTH'S CURVATURE AND ROTATION
   Earth rotates during acquisition (for pushbroom sensors scanning one line at a time)
   Curved Earth geometry
   -> Corrected by Earth model (WGS84 ellipsoid)

4. TERRAIN (relief displacement)
   Hills cause pixel displacement proportional to height
   Tall buildings "lean" away from nadir in high-res imagery
   -> Corrected by DEM (orthorectification)
```

### Sensor Models

**Rigorous sensor model** (physics-based): uses full interior orientation (camera calibration matrix K) and exterior orientation (rotation R, translation t) parameters. Collinearity equation:

```
  [x_image]     1    | r11 r12 r13 | | X_world - Xs |
  [y_image]  = --- * | r21 r22 r23 | | Y_world - Ys |
              c     | r31 r32 r33 | | Z_world - Zs |

  where c = focal length, (Xs,Ys,Zs) = sensor position
  r_ij = rotation matrix elements from attitude (roll/pitch/yaw)
```

**Rational Polynomial Coefficients (RPCs)**: commercial satellites provide RPCs instead of physical sensor model (proprietary). RPCs are coefficients of a ratio of polynomials approximating the true sensor model. Accurate to 1-2 pixels without GCPs, sub-pixel with GCPs.

### Ground Control Points (GCPs)

GCPs are points with known ground coordinates (GPS-measured) that appear in the image. Used to refine sensor model parameters:

```
  GCP selection criteria:
    - Sharp, distinctive features (road intersections, building corners)
    - Stable over time (not vegetation that changes)
    - Well-distributed spatially across image
    - At least 9-20 for stable polynomial model
    - More near the image edges (curvature is worst there)

  Residuals: RMS error between predicted and measured GCP locations
  Acceptable: < 0.5 pixels RMSE for orthorectification
  For InSAR: < 1/4 pixel required
```

### Orthorectification

Corrects for terrain-induced parallax (relief displacement). Requires a DEM:

```
  INPUT: Distorted image + DEM + sensor model + GCPs
  PROCESS:
    For each output pixel (lat, lon):
      1. Look up terrain height Z from DEM
      2. Use sensor model to project (lat, lon, Z) into image space
      3. Bilinear interpolation of raw image at projected location
      4. Assign to output pixel
  OUTPUT: Orthophoto/orthoimage where each pixel = correct lat/lon

  CRITICAL: DEM quality determines orthorectification quality
    Forest canopy: use bare-earth DEM (not DSM) or significant errors
    Mountain terrain: use high-quality SRTM or Copernicus DEM
    SRTM 30m global DEM: adequate for Landsat (30m)
    Copernicus DEM 10m: needed for Sentinel-2 (10m)
```

---

## Co-registration

Two images taken at different times must be spatially aligned to detect change. Even after individual orthorectification, residual misregistration remains:

```
APPROACH 1: Normalized Cross-Correlation (NCC)
  For each chip (e.g., 64x64 pixels) in reference image:
    Slide template over search window in target image
    Compute NCC at each offset (dx, dy):
      NCC(dx,dy) = corr(I1_chip, I2_chip_shifted(dx,dy))
    Peak of NCC surface = best match offset
  Sub-pixel accuracy via parabolic interpolation near peak

APPROACH 2: Mutual Information (MI)
  MI = H(I1) + H(I2) - H(I1, I2)
  where H = Shannon entropy
  Works across different sensors (Landsat -> Sentinel-2)
  Does not require similar brightness patterns

APPROACH 3: Feature-based (SIFT, ORB)
  Detect keypoints (corners, blobs) in each image
  Match corresponding keypoints
  Estimate affine or homography transformation
  Good for large offsets; less accurate than patch-based

SENTINEL-2 CO-REGISTRATION ACCURACY:
  Band-to-band (within sensor): < 0.3 pixel
  Between S-2A and S-2B: < 0.3 pixel (measured ~0.08 pixel)
  Key for vegetation indices that mix bands
```

---

## Atmospheric Correction

The atmosphere adds path radiance and absorbs/scatters signal between surface and sensor. Removing this to recover surface reflectance is "atmospheric correction."

### Dark Object Subtraction (DOS)

The simplest and most widely used method:

```
ASSUMPTION: Some pixel in each band has zero surface reflectance.
  Dark water, deep shadow, etc. -> measured DN in that pixel = path radiance only

PROCEDURE:
  1. Find minimum DN in each band (or use histogram percentile ~1%)
  2. Subtract from all pixels in that band
  3. Convert to reflectance using solar irradiance

LIMITATIONS:
  - Assumes dark object has exactly 0% reflectance
  - Ignores wavelength-dependent absorption (treats atm as additive only)
  - Cannot correct for atmospheric absorption (only scattering)
  - Error: typically 5-15% in blue band, 2-5% in NIR

WHEN TO USE: Quick vegetation indices analysis over large areas,
  historical imagery where atmospheric profiles not available
```

### MODTRAN / 6S Radiative Transfer

Physics-based models simulate the full radiative transfer through the atmosphere:

```
6S (Second Simulation of the Satellite Signal in the Solar Spectrum)
MODTRAN (MODerate resolution TRANsmittance)

INPUTS:
  - Atmospheric profile: water vapor column, ozone column
    Source: NCEP/NCAR reanalysis, MERRA-2, ERA5
  - Aerosol optical depth (AOD): MODIS/MISR aerosol product
  - Sun-sensor geometry: solar zenith, view zenith, azimuth
  - Sensor spectral response functions

OUTPUTS:
  - Atmospheric transmittance for each band
  - Path radiance contribution
  - Downwelling diffuse irradiance

INVERSION:
  rho_surface = (rho_TOA - rho_atm) / (T_up * T_down + rho_atm * S * rho_surface_neighborhood)

  S = spherical albedo of atmosphere (multiple scattering term)
  This is an implicit equation (solved iteratively for dense, bright areas)

IMPLEMENTATIONS:
  LaSRC: Landsat Collection 2 surface reflectance (USGS standard)
  Sen2Cor: Sentinel-2 Level-2A (ESA standard, included in SNAP)
  Py6S: Python wrapper for 6S (open source)
  FORCE: Processing framework for ARD generation (Sentinel + Landsat)
```

---

## Classification

Land cover classification assigns each pixel (or object) to a thematic category. The fundamental split is supervised (training data) vs. unsupervised (no labels).

### Unsupervised: K-Means and ISODATA

```
K-MEANS:
  1. Initialize k cluster centers randomly in spectral space
  2. Assign each pixel to nearest center (Euclidean distance)
  3. Recompute centers as mean of assigned pixels
  4. Repeat until convergence

  ISODATA extends k-means: allows clusters to split (too large) or merge (too close)
  Output: k spectral classes -> user manually labels each class ("water", "forest", etc.)
  Problem: spectral cluster != thematic class. Forest and shadow may share a cluster.
```

### Supervised: SVM and Random Forest

```
SUPPORT VECTOR MACHINE (SVM)
  Finds maximum-margin hyperplane separating classes in feature space
  Kernel trick: maps to high-dimensional space to handle non-linear boundaries
  Kernel choice: RBF (radial basis function) most common for EO data
  Parameters: C (penalty), gamma (RBF width) -> require tuning
  Strengths: works well with small training sets, handles high-dim features
  Weaknesses: slow on large datasets, no probability output (natively)

RANDOM FOREST (RF)
  Ensemble of decision trees, each trained on bootstrap sample
  Features randomly subsampled at each node split
  Output: majority vote across all trees
  Outputs class probability (fraction of trees voting for class)
  Strengths: fast, handles class imbalance, built-in feature importance
  Best performer for most EO classification tasks historically

CNN / DEEP LEARNING
  Feature extraction and classification jointly learned
  Requires large labeled training sets (hundreds to thousands per class)
  Transfer learning from ImageNet: pretrained CNNs (ResNet, EfficientNet) fine-tuned
  U-Net: semantic segmentation architecture widely used for satellite
  Superiority: context-aware, handles textures better than per-pixel RF
```

### Accuracy Assessment

**Never evaluate on training data.** Independent test set required.

```
CONFUSION MATRIX (2-class example)

              PREDICTED
              Water  Land
ACTUAL  Water |  92  |  8  |   Producer Accuracy: 92%
        Land  |  15  | 85  |   Producer Accuracy: 85%
              User Acc: 86% 91%

METRICS:
  Overall Accuracy (OA): sum(diagonal) / total = (92+85)/200 = 88.5%
  Producer Accuracy: TP / (TP + FN) = recall for each class
  User Accuracy: TP / (TP + FP) = precision for each class

  Kappa coefficient:
    kappa = (P_o - P_e) / (1 - P_e)
    P_o = observed agreement, P_e = expected chance agreement
    kappa > 0.8 = strong agreement; 0.6-0.8 = moderate

  F1 score = 2 * precision * recall / (precision + recall)
    Better than accuracy for class-imbalanced datasets
    Use macro-averaged F1 for multi-class
```

---

## Change Detection

```
SIMPLE IMAGE DIFFERENCING:
  dI = I_t2 - I_t1 (after co-registration and atmospheric correction)
  Threshold |dI| > T to detect change
  Fast, sensitive to calibration errors

CHANGE VECTOR ANALYSIS (CVA):
  Magnitude: |dI| = sqrt(sum (Bi_t2 - Bi_t1)^2)   -> how much change
  Direction: arctan(dB2/dB1)                         -> what type of change
  Both magnitude and direction of spectral change vector

CCDC (Continuous Change Detection and Classification):
  Zhu and Woodcock 2014
  Fit harmonic model (seasonal cycles) to long time series per pixel
  Detect departures from expected seasonal pattern -> change
  Enables monitoring of deforestation, urban growth, crop rotation
  Works with Landsat entire archive (1984-present)
  Also in Google Earth Engine as built-in algorithm

SAR-based:
  Ratio: sigma0_t2 / sigma0_t1 (log ratio in dB)
  Coherence change: compare InSAR coherence before/after
  Damage proxy map: coherence loss -> surface disruption (earthquake, landslide)
```

---

## Decision Cheat Sheet

| Task | Method | Requirement |
|------|---------|-------------|
| Quick atmospheric correction | DOS | No aux data; historical imagery |
| Production surface reflectance | LaSRC (Landsat), Sen2Cor (S2) | Standard product, free |
| Aquatic environments | ACOLITE, C2RCC | Specialized water algorithms |
| Rapid land cover map | Random Forest | 50-100 training samples per class |
| High accuracy urban mapping | CNN (U-Net) | Large labeled dataset |
| Global consistent classification | Pre-existing products (ESA WorldCover) | 10m annual, free |
| Time series change | CCDC, LandTrendr | Full archive Landsat |
| Post-disaster rapid mapping | SAR coherence ratio | All-weather, rapid |
| Accuracy reporting | Confusion matrix + F1 | Independent test set required |

---

## Common Confusion Points

**Orthorectification vs. geocoding**: Geocoding assigns coordinates to an image using a simple affine/polynomial transform. Orthorectification uses a DEM to correct terrain-induced parallax. For flat terrain, they are nearly identical. For mountains or tall buildings, orthorectification is required.

**Sen2Cor output is not equivalent to LaSRC output**: Both produce surface reflectance, but use different atmospheric correction algorithms. Time series mixing Sentinel-2 and Landsat requires harmonization (HLS product from NASA does this).

**The confusion matrix must use an independent test set** -- A common error: sampling the training polygons for assessment, or using the same field sites for training and testing. This inflates accuracy. A completely independent probability sample from the study area is required for valid accuracy estimates.

**Kappa is now controversial** -- Stehman and Foody (2019) argued kappa is mathematically flawed as an accuracy metric and should be abandoned. Use OA, producer's accuracy, user's accuracy, and F1 instead. Kappa remains common in older literature.
