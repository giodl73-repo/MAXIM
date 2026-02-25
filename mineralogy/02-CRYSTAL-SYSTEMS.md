# Crystal Systems and Crystallography

## The Big Picture

```
+------------------------------------------------------------------+
|           CRYSTAL SYMMETRY: FROM ATOMS TO PATTERN               |
|                                                                  |
|  Point symmetry operations         Space symmetry operations     |
|  (rotations, reflections,          (+ translations, screws,      |
|   inversions, roto-inversions)      glides)                      |
|         |                                  |                     |
|         v                                  v                     |
|  32 Point Groups              14 Bravais Lattices               |
|  (crystal classes)            (translational frameworks)         |
|         |                                  |                     |
|         +—————————————+———————————————————+                     |
|                       |                                          |
|                       v                                          |
|              230 Space Groups                                    |
|          (complete classification of                             |
|           all possible crystal symmetries)                       |
+------------------------------------------------------------------+
```

This is a theorem from finite group theory applied to 3D geometry. The 230 space groups were independently derived by Fedorov (1891), Schoenflies (1891), and Barlow (1894) — before X-rays were discovered.

---

## The Seven Crystal Systems

```
CRYSTAL SYSTEMS: UNIT CELL PARAMETERS
+------------------------------------------------------------------+
|                                                                  |
|  Parameter notation: a, b, c = edge lengths                      |
|                       α, β, γ = angles between axes             |
|                                                                  |
|  CUBIC (Isometric)      a = b = c;  α = β = γ = 90°            |
|  Highest symmetry.  4-fold rotation axes.                       |
|  Minerals: Halite, galena, pyrite, garnet, diamond, fluorite    |
|  Crystal habit: cubes, octahedra, dodecahedra                   |
|                                                                  |
|  TETRAGONAL             a = b ≠ c;  α = β = γ = 90°            |
|  One unique 4-fold rotation axis.                               |
|  Minerals: Zircon, cassiterite (SnO₂), chalcopyrite, anatase   |
|  Crystal habit: square prisms, bipyramids                       |
|                                                                  |
|  ORTHORHOMBIC           a ≠ b ≠ c;  α = β = γ = 90°            |
|  Three mutually perpendicular 2-fold axes.                      |
|  Minerals: Olivine, sulfur, barite, aragonite, topaz            |
|  Crystal habit: tabular, prismatic                              |
|                                                                  |
|  HEXAGONAL              a = b ≠ c;  α = β = 90°, γ = 120°      |
|  One 6-fold rotation axis.                                      |
|  Minerals: Quartz (at high T), beryl, graphite, apatite         |
|  Crystal habit: hexagonal prisms                                |
|                                                                  |
|  TRIGONAL (Rhombohedral) a = b = c; α = β = γ ≠ 90°            |
|  One 3-fold rotation axis. Subset of hexagonal.                 |
|  Minerals: Calcite, dolomite, corundum, tourmaline, quartz      |
|  Crystal habit: rhombohedra, scalenohedra                       |
|                                                                  |
|  MONOCLINIC             a ≠ b ≠ c;  α = γ = 90°, β ≠ 90°       |
|  One 2-fold rotation axis or mirror plane.                      |
|  Minerals: Orthoclase, augite, hornblende, gypsum, epidote      |
|  Crystal habit: prismatic, tabular                              |
|                                                                  |
|  TRICLINIC              a ≠ b ≠ c;  α ≠ β ≠ γ ≠ 90°            |
|  Lowest symmetry. Only inversion center (or none).             |
|  Minerals: Plagioclase, kyanite, rhodonite                      |
|  Crystal habit: tabular, pinacoidal                             |
+------------------------------------------------------------------+
```

---

## Group Theory Connection

This is the exact same group theory from abstract algebra — the classification of finite groups acting on 3D space.

**Symmetry operations**:
- **Rotation axes**: Cn — rotation by 360°/n (n = 1, 2, 3, 4, 6 in crystals; 5 and 7+ not possible with periodic tiling)
- **Mirror planes**: σ — reflection
- **Inversion center**: i — point reflection through origin
- **Roto-inversion**: S̄n — rotation + inversion combined

**Why not 5-fold symmetry?** A periodic lattice can tile with 2-, 3-, 4-, or 6-fold rotation — but not 5-fold. This is the crystallographic restriction theorem. (Quasicrystals, discovered by Dan Shechtman in 1984, have non-periodic long-range order with 5-fold symmetry — they're a separate category.)

```
THE 32 POINT GROUPS — organized by crystal system
+------------------------------------------------------------------+
|  Cubic:        23, m3, 432, 4̄3m, m3m        (5 groups)         |
|  Tetragonal:   4, 4̄, 4/m, 422, 4mm, 4̄2m, 4/mmm  (7 groups)   |
|  Orthorhombic: 222, mm2, mmm                 (3 groups)         |
|  Hexagonal:    6, 6̄, 6/m, 622, 6mm, 6̄m2, 6/mmm  (7 groups)   |
|  Trigonal:     3, 3̄, 32, 3m, 3̄m             (5 groups)        |
|  Monoclinic:   2, m, 2/m                     (3 groups)         |
|  Triclinic:    1, 1̄                          (2 groups)         |
|  Total: 32 point groups                                          |
+------------------------------------------------------------------+
```

**Space groups** add translational symmetry — screw axes (rotation + translation) and glide planes (reflection + translation) — to get from 32 to 230.

---

## Bravais Lattices

```
THE 14 BRAVAIS LATTICES — unique translational tilings of 3D space
+------------------------------------------------------------------+
|  Cubic system (3 lattices):                                      |
|    Simple cubic (P)         8 corner atoms only                  |
|    Body-centered cubic (I)  + 1 atom at cube center              |
|    Face-centered cubic (F)  + 1 atom at each face center         |
|                                                                  |
|  Tetragonal (2):  Simple (P), Body-centered (I)                 |
|  Orthorhombic (4): P, I, F, C (base-centered)                  |
|  Hexagonal (1):   Simple (P)                                     |
|  Rhombohedral (1): R                                            |
|  Monoclinic (2):  P, C                                          |
|  Triclinic (1):   P                                             |
|  Total: 14 Bravais lattices                                      |
|                                                                  |
|  Key insight: FCC = closest packing of equal spheres            |
|  → Explains structure of many metals (Cu, Al, Ni, Au)           |
|  → Halite (NaCl): FCC of Cl⁻ with Na⁺ in octahedral holes      |
|  → Fluorite (CaF₂): FCC of Ca²⁺ with F⁻ in all tetrahedral    |
|     holes (opposite of antifluorite structure)                  |
+------------------------------------------------------------------+
```

The 14 Bravais lattices are the complete enumeration of distinct ways to tile 3D space with translational periodicity — a result from group theory / topology. There are exactly 14; no more is possible.

---

## Crystal Habit and Form

**Habit** = characteristic external shape of a crystal; reflects internal symmetry but also growth conditions.

```
CRYSTAL HABITS AND WHAT CONTROLS THEM
+--------------------------------------------------+
|  Habit Name    | Shape         | Example         |
+--------------------------------------------------+
|  Cubic         | 6 square faces | Halite, pyrite |
|  Octahedral    | 8 triangular   | Diamond, spinel|
|  Prismatic     | elongated prism| Quartz, beryl  |
|  Tabular       | flat tablet    | Mica, graphite |
|  Acicular      | needle-like    | Rutile, natrolite|
|  Bladed        | flat blades    | Kyanite, gypsum|
|  Reniform      | kidney-shaped  | Hematite       |
|  Botryoidal    | grape clusters | Malachite      |
|  Dendritic     | tree-like      | Native copper  |
|  Massive       | no crystal faces| Chalcedony    |
+--------------------------------------------------+

Growth conditions override ideal habit:
→ Fast growth → skeletal crystals with incomplete faces
→ Impurities → modified habit, color zoning
→ Pressure → elongated forms
→ Hydrothermal → well-formed euhedral crystals (time for slow growth)
```

---

## Crystal Twinning

A twin is a single crystal in which two or more parts are related by a symmetry operation that is NOT part of the normal point group symmetry.

```
TYPES OF TWINNING
+------------------------------------------------------------------+
|  CONTACT TWINS: two individuals joined by a flat twin plane     |
|  Example: Gypsum butterfly twins, staurolite cross twins        |
|                                                                  |
|  PENETRATION TWINS: individuals interpenetrate                  |
|  Example: Orthoclase Carlsbad twin, fluorite penetration twin   |
|                                                                  |
|  POLYSYNTHETIC TWINS: many repeated fine lamellae              |
|  Example: Plagioclase — alternating twin orientations visible   |
|    under microscope (key identification feature)                |
|  Example: Calcite — deformation twinning under stress           |
|                                                                  |
|  IMPORTANCE:                                                     |
|  Plagioclase polysynthetic twinning = definitive ID in thin section
|  Magnetite twinning → magnetic domain structure                 |
|  Silicon semiconductor: twinning = manufacturing defect         |
+------------------------------------------------------------------+
```

---

## X-ray Diffraction — Bragg's Law

When X-rays hit a crystal, they scatter from each set of parallel crystal planes. Constructive interference occurs when path length difference = integer multiple of wavelength.

```
BRAGG'S LAW:  nλ = 2d·sin(θ)

     Incoming X-rays  Diffracted X-rays
          ↘    ↙
    --------·---------  ← atomic plane (spacing d)
          ↓ ↓
    --------·---------  ← next plane

  Path difference = 2d·sin(θ)
  Constructive interference when: nλ = 2d·sin(θ)
  where:
    n = integer (order of diffraction)
    λ = X-ray wavelength (~1.54 Å for Cu Kα radiation)
    d = interplanar spacing
    θ = angle of incidence/diffraction
```

**The XRD connection to Fourier analysis**:

The diffraction pattern is the Fourier transform of the electron density in the crystal. Each diffraction spot (peak) in the pattern corresponds to a specific set of crystal planes (hkl Miller indices). This is directly analogous to:
- Frequency domain analysis in signal processing
- The diffraction pattern = frequency domain representation
- The crystal structure = real-space representation

To get from diffraction pattern → crystal structure requires solving the phase problem (you measure |F|² but not the phase of F). This is a classic problem in signal reconstruction — the crystallographic equivalent of recovering a signal when you can only measure power spectral density, not the complex Fourier coefficients.

```
XRD WORKFLOW
+------------------------------------------------------------------+
|  Crystal or powder sample                                        |
|       |                                                          |
|       v                                                          |
|  Irradiate with monochromatic X-rays (λ known)                  |
|       |                                                          |
|       v                                                          |
|  Detector records intensity vs. 2θ angle                        |
|       |                                                          |
|       v                                                          |
|  Each peak: use Bragg → d-spacing for that plane family         |
|  Peak positions → unit cell parameters (a, b, c, α, β, γ)      |
|  Peak intensities → atom positions within unit cell             |
|  Peak widths → crystallite size (Scherrer equation)            |
|       |                                                          |
|  MINERAL IDENTIFICATION: match d-spacings to JCPDS/ICDD database|
|  (every mineral has a unique XRD fingerprint)                   |
+------------------------------------------------------------------+
```

**Powder XRD vs. single-crystal XRD**:

| Method | Sample | Output | Use case |
|--------|--------|--------|---------|
| Powder XRD | Ground mineral | 1D pattern (rings) | Mineral ID, phase analysis |
| Single-crystal XRD | Intact crystal | 3D diffraction spots | Full structure determination |
| Synchrotron XRD | Either | High resolution | Complex or tiny structures |

---

## Miller Indices — Describing Crystal Planes

Crystal planes are described by Miller indices (hkl) — reciprocals of the intercepts of the plane with the unit cell axes, cleared to smallest integers.

```
MILLER INDEX EXAMPLES
+--------------------------------------------------+
|  Plane       | h k l | Description              |
+--------------------------------------------------+
|  (100)       | 1 0 0 | perpendicular to a-axis  |
|  (110)       | 1 1 0 | diagonal plane           |
|  (111)       | 1 1 1 | diagonal through corners |
|  (001)       | 0 0 1 | basal plane (horizontal) |
+--------------------------------------------------+

Cleavage in calcite: {1011} — the rhombohedral cleavage
Cleavage in halite: {001} — the cubic face = cube cleavage
Cleavage in mica: {001} — basal cleavage = flat sheets
```

The notation {hkl} means all symmetrically equivalent planes (the whole family). (hkl) is one specific plane.

---

## Applied Crystallography Connections

| Field | How Crystal Symmetry Applies |
|-------|------------------------------|
| **Semiconductor mfg** | Silicon wafers are cut along specific crystal planes (001, 110, 111) to control etch behavior; crystal defects (dislocations, twins) degrade device performance |
| **Materials design** | Crystal structure → predicted elastic moduli, cleavage directions, optical behavior |
| **Pharmaceutical** | Drug polymorphs have different solubility, stability, bioavailability (Ritonavir disaster — same formula, wrong polymorph changed solubility) |
| **Metals** | BCC steel vs. FCC austenite → different slip systems → different deformation behavior |
| **Powder diffraction** | Quality control in manufacturing: cement phases, battery cathode materials, pigments |

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| How many crystal systems? | 7 (cubic, tetragonal, orthorhombic, hexagonal, trigonal, monoclinic, triclinic) |
| How many point groups? | 32 |
| How many space groups? | 230 |
| Why no 5-fold symmetry? | Crystallographic restriction theorem — 5-fold can't tile periodic 3D space |
| What does XRD measure? | d-spacings (via Bragg's law) → unit cell parameters → mineral identity |
| What's the phase problem? | You measure |F|² from XRD, not F; recovering phases requires direct methods or isomorphous replacement |
| What are Bravais lattices? | 14 distinct translational symmetry frameworks for 3D periodic structures |

---

## Common Confusion Points

**Trigonal vs. hexagonal**: Both use 4-axis hexagonal notation (a, a, a, c with 120° between a-axes). Trigonal has 3-fold symmetry; hexagonal has 6-fold. Some classifications merge them (6 systems total); others separate (7 systems). IMA currently uses 7.

**Habit vs. form**: A "form" in crystallography is the complete set of equivalent faces generated by applying the point group symmetry to a starting face. Habit is the overall shape of the real crystal, which may emphasize certain forms over others depending on growth conditions.

**Bragg angle vs. diffraction angle**: The convention varies. 2θ is the total angle between incident and diffracted beam. θ is the Bragg angle (half of 2θ). XRD patterns plot intensity vs. 2θ, not θ.

**d-spacing and lattice planes**: The d-spacing is the perpendicular distance between adjacent parallel planes in the (hkl) family. It is NOT the same as the unit cell parameter. For cubic crystals: d(hkl) = a/√(h²+k²+l²).

**Polycrystalline vs. single crystal**: Metals, rocks, and most minerals are polycrystalline aggregates of randomly oriented grains. A single crystal is a continuous, consistently oriented lattice. Semiconductor wafers are deliberately grown as large single crystals; most natural minerals are not.
