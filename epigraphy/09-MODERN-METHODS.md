# Modern Methods: RTI, 3D Scanning, Multispectral, Corpus Databases

## The Big Picture

```
MODERN EPIGRAPHIC METHODS STACK
=================================

+------------------------------------------------------------------+
|  PROBLEM                METHOD               OUTPUT              |
|  -------                ------               ------              |
|  Worn/faded text        RTI imaging          Virtual re-lighting |
|  3D surface detail      Photogrammetry       3D model + normals  |
|  Very damaged text      Multispectral        Contrast recovery   |
|  Large-scale recording  Photogrammetry       Measurable model    |
|  Corpus management      Database + XML       Searchable archive  |
|  Text transcription     AI assistance        Draft + flags       |
|  Traditional copy       Epigraphic squeeze   Paper impression    |
|  Dating                 3D + statistical     Letter form date    |
+------------------------------------------------------------------+

UNDERLYING PRINCIPLE: The inscription contains more information
than visible to the naked eye. Physical methods reveal it.
```

---

## Reflectance Transformation Imaging (RTI)

RTI is currently the most important single technique in field epigraphy:

```
RTI METHOD
===========

PROBLEM: Worn or faintly inscribed text
  Characters that have been weathered, polished, or damaged
  are invisible in flat ambient light
  The eye and standard photography cannot reveal them

PHYSICAL PRINCIPLE:
  Shallow surface relief (carved letters) casts shadows
  Shadow direction depends on light direction
  Different light directions reveal different micro-topography
  By combining many light positions, you can reconstruct
  the full surface normal map

PROCESS:
  1. Set up camera on fixed tripod above the inscription
  2. Take ~100 photographs, each with a light source
     at a different position around the object
     (fixed camera position; varied light position)
  3. Each photograph: note light direction precisely
     (or use a reflective sphere to calculate it)
  4. RTI software (Hewlett Packard Labs / Cultural Heritage Imaging)
     computes per-pixel surface normal from the light variation
  5. RESULT: interactive viewer where you can move
     the virtual light source to any direction

RTI VIEWER MODES:
  - Default diffuse: normal photograph appearance
  - Specular enhancement: increase specular response
    -> Reveals toolmarks, chisel direction
  - Normal map visualization: surface orientation
    -> Shows letter depth and carving technique
  - Diffuse gain: amplify surface detail contrast

OPTIMAL USE CASES:
  Very worn stone: marble gravestones, soft limestone
  Clay tablet cuneiform: reveals individual wedge impressions
  Metal objects: fibulae, curse tablets
  Wax impressions: seals
  Papyrus and parchment (yes -- for writing pressure)
```

### RTI in Practice: A Case Study

```
CASE STUDY: ROMAN MILITARY DIPLOMA (British Museum)
====================================================

Object: bronze military diploma (discharge certificate)
        2nd c. CE; heavily corroded and worn
Problem: inscription partially illegible
         earlier photographs and squeezes incomplete

RTI process:
  Camera: fixed overhead
  Light: ~96 positions (hand-held LED lamp, 60cm from object)
  Sphere: used to calculate light angles precisely
  Software: RTIbuilder (free, Cultural Heritage Imaging)

Result:
  Names previously unreadable: revealed
  Mint mark: identified
  Specific letter forms for dating: measurable
  Text corrections to previous published readings: 3

TIME: setup ~2 hours; photography ~1 hour; processing ~30 min
COST: free software; hardware cost ~$500-1000 (camera + lamp)
This is one of the most cost-effective imaging advances
in the history of epigraphy
```

---

## 3D Photogrammetry

```
3D PHOTOGRAMMETRY
==================

TECHNIQUE: Structure from Motion (SfM)
  Takes 50-500 overlapping photographs
  Photogrammetry software (Agisoft Metashape, Reality Capture)
  identifies common points across images
  Triangulates 3D positions from camera geometry
  Generates: dense point cloud -> mesh -> textured model

EPIGRAPHIC APPLICATIONS:
  1. Dimensional measurement:
     Letter height, stroke width, spacing -> dating by form
     Previously: hand measurement (slow, less precise)
     Now: measure from 3D model in software (fast, precise)

  2. Permanent record:
     3D model is a permanent, measurable archive
     Can be re-examined long after excavation
     Open access: models can be shared as files

  3. Virtual restoration:
     Broken fragments: align in 3D before physical handling
     Damaged text: compare with parallel examples in 3D

  4. Communication:
     3D models for publication, exhibition, education
     Anyone can examine in Sketchfab, MorphoSource

COMPARISON WITH TRADITIONAL CAST:
  Traditional: plaster or rubber cast (contact with object)
  Photogrammetry: non-contact (no risk to object)
  Traditional advantage: high fidelity texture transfer
  Photogrammetry advantage: dimensional accuracy, fast, cheap

HARDWARE:
  Minimum: any DSLR + free software (Meshroom)
  Professional: calibrated camera array + Agisoft Metashape
  Mobile: photogrammetry apps (adequate for documentation,
          not for publication-quality metric analysis)
```

---

## Laser Scanning

```
LASER SCANNING (LiDAR / Structured Light)
==========================================

TYPES:
  Terrestrial LiDAR (TLS): tripod-mounted scanner
    Sends laser pulses; measures return time
    Generates millions of 3D points per second
    Use: large objects, architecture, entire inscription surfaces

  Structured light scanning: project pattern, photograph deformation
    Very high resolution for small objects
    Use: small finds, coins, tablets, figurines

  Handheld scanners: portable but lower precision

ADVANTAGES OVER PHOTOGRAMMETRY:
  More accurate in poorly-lit conditions
  Captures surface where photogrammetry struggles
  (uniform texture: marble, polished bronze)
  Millimeter-level accuracy standard

DISADVANTAGES:
  Cost: professional TLS scanner ~$30,000-100,000
  Processing time: large datasets are slow
  Expertise: specialized software (Leica Cyclone, FARO Scene)

EPIGRAPHIC USE:
  Runestone surveys: Swedish National Heritage Board
    scanned thousands of runestones at mm resolution
  Cuneiform tablets: British Museum mass scanning project
  Cave inscriptions: where physical access is limited
  Roman milestones: landscape survey + inscription
```

---

## Multispectral Imaging

```
MULTISPECTRAL IMAGING
======================

PRINCIPLE:
  Different materials reflect/absorb light differently
  at different wavelengths
  Ink, paint, and engraving that are invisible to the eye
  may be visible in infrared (IR), ultraviolet (UV),
  or specific narrow-band wavelengths

APPLICATIONS:
  INFRARED (IR, ~700-1000nm):
    Carbon-based ink absorbs IR even when faded
    Readable under UV-opaque overlayers
    Key use: palimpsest manuscripts (erased text)
    Archimedes Palimpsest: IR revealed erased 10th c. text
    -> recovered lost mathematical works of Archimedes

  ULTRAVIOLET (UV, ~320-380nm):
    Organic materials (parchment, papyrus) fluoresce
    Ink does not fluoresce -> dark on bright background
    Key use: faded ink on parchment/papyrus

  RAKING LIGHT (oblique illumination):
    Not multispectral but closely related
    Emphasizes surface topography
    Reveals impressed or engraved marks invisible in flat light

  XRF (X-Ray Fluorescence):
    Identifies elemental composition of pigments/inks
    Non-destructive
    Determines: which metal pigments (verdigris vs. azurite)
    Can distinguish original ink from later additions
    Key use: authenticating inscriptions; detecting forgeries

SPECIFIC INSTRUMENT: Reflectance Spectroscopy
  Measures reflectance across 200-2500nm wavelengths
  Per-pixel data in processed images
  Output: false-color images enhancing different features
```

---

## Epigraphic Squeeze (Traditional Method)

Not modern, but still used:

```
EPIGRAPHIC SQUEEZE
===================

Method:
  Wet paper or papier-mache pressed into inscription
  Pushed into incised letters with stiff brush
  Allowed to dry in place
  Removed: mirror impression of the inscription

Advantages:
  Captures exact letter forms at full scale
  Can be examined later in the lab
  Squeezes from the 19th-20th c. are now primary sources
    for inscriptions since damaged or destroyed
  "Squeeze libraries" at major universities

Limitations:
  Damages fragile surfaces (friction, absorption)
  Metric accuracy depends on paper uniformity
  Color information lost
  Not suitable for fragile objects

Modern replacement: RTI + photogrammetry is preferred
  for primary recording; squeezes still made for
  specific research purposes and working copies

SQUEEZE COLLECTIONS:
  Epigraphical Museum Athens
  Ashmolean Museum Oxford
  British School at Rome
  Harvard Art Museums
  -> Historical squeezes are irreplaceable archives
```

---

## Corpus Databases

```
MAJOR EPIGRAPHIC DATABASES
============================

PHI GREEK INSCRIPTIONS (inscriptions.packhum.org):
  ~190,000 Greek inscriptions
  Searchable text; linked to print publications (IG, etc.)
  Free, maintained by Packard Humanities Institute
  Best for: searching Greek inscriptions across geographic areas

EDCS (Epigraphik-Datenbank Clauss-Slaby):
  ~490,000 Latin inscriptions (largest)
  Free at edcs.uni-erlangen.de
  Searchable by formula, word, geographic area
  Links to CIL volume and page references
  Best for: Latin formulaic search, geographic distribution

EDH (Epigraphische Datenbank Heidelberg, HD):
  ~75,000 Latin inscriptions
  More structured metadata than EDCS
  Geographic visualization
  Best for: georeferenced Latin epigraphy

DĀMOS (Mycenaean Greek, Oslo):
  All Linear B tablets (complete corpus)
  Fully tagged with lemmas, grammar
  Best for: Mycenaean Greek research

CDLI (Cuneiform Digital Library Initiative, UCLA):
  ~330,000 cuneiform tablets
  Images where available
  Free at cdli.ucla.edu
  Best for: Mesopotamian cuneiform

EPIDOC (standards):
  EpiDoc is an XML markup standard for ancient inscriptions
  Based on TEI (Text Encoding Initiative)
  Used by PHI, DĀMOS, and many national epigraphic projects
  Captures: text + uncertainty + abbreviation + damage + apparatus
  The format is an interoperability standard across databases
```

---

## AI Transcription and Assistance

```
AI IN EPIGRAPHY (current state 2025)
======================================

WHAT AI CAN DO:
  1. Character recognition on clean inscriptions:
     High-accuracy OCR for well-preserved Latin/Greek
     Google DeepMind's Ithaca (2022):
       Trained on 78,000 Greek inscriptions
       Partial text completion: ~62% accuracy
       Geographic attribution: ~71% accuracy
       Dating: predicted within 30-year window for ~73% of texts

  2. Optical character segmentation:
     Isolate individual characters from images
     Helps human expert work faster; reduces search space

  3. Corpus analysis:
     Identify parallel formulas across large databases
     Find statistically anomalous inscriptions
     Cluster similar inscription types

  4. Palaeographic dating:
     AI letter-form analysis can produce probabilistic
     date ranges from sign shapes
     Currently outperforms average expert; below best expert

WHAT AI CANNOT DO:
  1. Decipher unknown scripts:
     Without language identification, ML models cannot
     produce phonetic values from statistical patterns alone

  2. Handle ambiguity as a human expert can:
     Damaged text requires contextual knowledge
     (which formula, which period, which region)
     that AI currently handles poorly for rare cases

  3. Read truly damaged inscriptions:
     When text is physically missing, prediction is guessing

ITHACA (DeepMind, 2022):
  Published in Nature
  Collaborative tool (AI assists human expert, not replaces)
  "Human + AI" performance > either alone
  Human: 27% geography attribution alone
  Ithaca alone: 71%
  Human + Ithaca: 72% (marginal improvement from collaboration)
  Interpretation: humans contribute other knowledge beyond
  what the training distribution covers; AI fills in baseline
```

---

## Field Recording Workflow

```
MODERN FIELD RECORDING WORKFLOW
=================================

ARRIVAL AT INSCRIPTION:
  1. Condition assessment (damage, weathering, setting)
  2. Photograph: overview + detail in raking light
  3. Measurements: object dimensions + inscription field

IMAGING:
  4. RTI if surface relief important
  5. Photogrammetry if dimensional data needed
  6. Multispectral if fading suspected
  7. Squeeze only if other methods insufficient

TRANSCRIPTION:
  8. Text transcription on site (paper + digital)
  9. Leiden conventions for damage/uncertainty marking
  10. Cross-reference with any existing publications

METADATA:
  11. GPS coordinates, site ID, inventory number
  12. EpiDoc XML tagging for database deposit
  13. Digital photographs uploaded to secure storage (3-2-1 rule)

PUBLICATION:
  14. Critical edition with apparatus
  15. Transcription in standardized fonts (Gentium for Greek)
  16. Database deposit (PHI, EDCS, EDH as appropriate)

LEIDEN CONVENTIONS (text marking standard):
  [abc]   = restored text (gap filled by editor)
  ((abc)) = abbreviation expanded
  {abc}   = text deleted by editor (error)
  <abc>   = text omitted by ancient engraver
  .       = one illegible character
  ---     = unknown number of lost characters
  vacat   = empty space (intentional blank)
```

---

## Decision Cheat Sheet

| Problem | Best method |
|---------|-------------|
| Worn letters, relief inscription | RTI |
| Dimensional measurement, 3D model | Photogrammetry |
| Faded ink on papyrus/parchment | Multispectral (IR/UV) |
| Small object, very high detail | Structured light scanning |
| Large site, architectural inscription | Terrestrial LiDAR |
| Working copy, traditional record | Epigraphic squeeze |
| Search Latin corpus by formula | EDCS (edcs.uni-erlangen.de) |
| Search Greek corpus | PHI (inscriptions.packhum.org) |
| Cuneiform tablets | CDLI (cdli.ucla.edu) |
| AI text completion assistance | Ithaca (DeepMind tool) |

---

## Common Confusion Points

**RTI is not 3D scanning.** RTI captures surface normals (direction of surface at each point) from multiple light positions. It does not produce an absolute 3D model with metric dimensions. Photogrammetry and laser scanning produce true 3D models.

**Multispectral imaging is not X-ray.** X-ray penetrates the substrate and reveals internal structure. Multispectral imaging captures surface reflectance at different wavelengths. They are different techniques with different information content.

**AI cannot decipher unknown scripts.** This is a common misconception. Ithaca and similar tools are trained on known scripts in known languages. They can assist human experts on those scripts. They cannot crack Indus Valley or Linear A.

**EpiDoc and Leiden are different things.** Leiden conventions are a text-markup standard for how to represent damaged/uncertain text in print publications (square brackets, etc.). EpiDoc is an XML encoding standard that implements Leiden and adds structured metadata. You use Leiden conventions when transcribing; you use EpiDoc when digitally encoding.

**"Human + AI" does not always outperform both.** The Ithaca paper showed marginal improvement when human and AI collaborated vs. AI alone on geography attribution. For date attribution, human + AI was meaningfully better than either alone. The benefit depends on what distinct knowledge each brings — when they bring the same knowledge, collaboration provides no benefit.
