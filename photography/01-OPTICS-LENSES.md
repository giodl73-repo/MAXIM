# Optics and Lenses

## The Big Picture

A camera lens is a **spatial Fourier filter** applied to scene light before it reaches the recording medium. Everything that degrades image quality — blur, aberrations, diffraction — can be understood as unwanted modification of the spatial frequency spectrum.

```
SCENE → LIGHT RAYS → LENS SYSTEM → IMAGE PLANE

The lens does four things:
  1. COLLECT light — aperture determines how much
  2. FOCUS light — focal length determines where the plane of sharp focus is
  3. SCALE the image — focal length × magnification = image size
  4. FILTER spatially — aberrations reduce contrast at high spatial frequencies

Key tension: larger aperture → more light + shallower DoF + more aberrations
             smaller aperture → less light + deeper DoF + diffraction softening
```

---

## The Thin Lens Equation

For an idealized thin lens (all refraction at a single plane):

```
1/f = 1/dₒ + 1/dᵢ

  f  = focal length (lens property; fixed by design)
  dₒ = object distance (scene to lens)
  dᵢ = image distance (lens to sensor/film)

Rearranged for focus distance:
  dᵢ = f·dₒ / (dₒ - f)

For objects at infinity (dₒ → ∞): dᵢ → f
  → "Focused at infinity" means image forms at exactly one focal length behind lens

For close-up (macro): dₒ approaches f → dᵢ grows → need to extend lens further
  Macro at 1:1 reproduction: dₒ = dᵢ = 2f (lens is 2× focal lengths from sensor)

Magnification m = -dᵢ/dₒ  (negative = inverted image)
```

### Focal Length and Angle of View

Angle of view is not a property of the lens alone — it depends on sensor size.

```
Horizontal angle of view: α = 2 · arctan(sensor_width / (2 · f))

Same focal length, different sensors:
  50mm on full-frame (36mm wide): α ≈ 40°   ("normal" lens — matches eye's perspective)
  50mm on APS-C (24mm wide):    α ≈ 27°   ("portrait" compression)
  50mm on 1-inch (13mm wide):   α ≈ 15°   (telephoto apparent perspective)

"Equivalent focal length" (EFL) = f × crop factor
  A 35mm lens on APS-C (1.5×) behaves like 52mm on full frame
```

---

## f-Number and Light Collection

```
f/N = focal length / entrance pupil diameter

N = f/D  where D = aperture diameter

Why it's defined as ratio:
  At f/2.8 regardless of focal length, the same IRRADIANCE (W/m²) hits
  the image plane — because longer lenses have larger pupils in exact proportion

f-number sequence (geometric, each stop = ×√2 ≈ 1.41 diameter = ×2 area):
  f/1   f/1.4  f/2  f/2.8  f/4  f/5.6  f/8  f/11  f/16  f/22  f/32

Each full stop change:
  1 stop open  → ×2 light (double exposure)
  1 stop close → ÷2 light (half exposure)

T-stop (transmission stop):
  f-stops are geometrical; actual transmission depends on glass absorption + reflections
  Cinema lenses use T-stops (calibrated for actual transmittance)
  T2.8 lens at f/2.8 may actually transmit only T3.2 of light
```

---

## Depth of Field

Depth of field is the range of object distances that appear acceptably sharp.

```
DEPTH OF FIELD GEOMETRY:

  Scene                Lens              Sensor

  ──── far limit ────►
  ──── SHARP ZONE ────►──────────────► image plane
  ──── near limit ───►
  ──── out of focus ──►──────────────► blur circle (diameter c)

Circle of confusion (CoC): diameter of acceptable blur on output
  Standard: d/1500 where d = sensor diagonal
  Full-frame (43mm diagonal): CoC ≈ 0.029mm = 29µm
  This assumes ~25cm viewing distance of an 8×10" print

Depth of field formulas:
  DoF ≈ 2·u²·N·c / f²   (for u >> f, simplified)

  where u = focus distance, N = f-number, c = CoC, f = focal length

What this means:
  DoF increases with:   larger N (smaller aperture), shorter focal length,
                        closer focus distance (paradox — but true for hyperfocal math)
  DoF decreases with:   larger aperture, longer focal length, closer subject

Hyperfocal distance H = f² / (N·c)
  Focus at H → everything from H/2 to infinity is acceptably sharp
  Used for landscape photography to maximize zone of apparent focus
```

### Bokeh and Out-of-Focus Rendering

```
"Bokeh" (Japanese ボケ = blur/haze): quality of out-of-focus rendering

Geometric bokeh shape:
  Circular aperture → circular blur circles
  Hexagonal diaphragm blades → hexagonal specular highlights
  Nikon "cat-eye" → elliptical near edges from vignetting of aperture

Bokeh quality factors:
  Apodization (Gradual ND filter over aperture): edges of blur circles are
    softer → smoother, more film-like bokeh (Sony STF, Fuji APD)
  Spherical aberration: positive SA → bright-edge circles (harsh "nervous")
                        negative SA → dark-edge circles (smooth, filmic)
  Longitudinal CA: color fringing of blur circles fore/aft of focus plane
```

---

## Lens Aberrations

A real lens deviates from the ideal thin lens in multiple ways. Aberrations are classified systematically (Seidel aberrations for monochromatic; chromatic separate).

### Monochromatic Aberrations (Seidel/Third-Order)

```
┌─────────────────────────────────────────────────────────────────┐
│ ABERRATION        │ CAUSE              │ MANIFESTATION          │
├─────────────────────────────────────────────────────────────────┤
│ Spherical         │ Marginal rays focus│ Soft at wide apertures;│
│                   │ differently than   │ "glowing" in highlights│
│                   │ paraxial rays      │ Stops down to sharpen  │
├─────────────────────────────────────────────────────────────────┤
│ Coma              │ Off-axis rays from │ "Seagull" or "comet"  │
│                   │ different pupil    │ flare on bright stars/ │
│                   │ zones focus at     │ point sources at edges │
│                   │ different points   │                        │
├─────────────────────────────────────────────────────────────────┤
│ Astigmatism       │ Off-axis: sagittal │ Lines in different     │
│                   │ and meridional     │ orientations focus at  │
│                   │ planes focus at    │ different distances;   │
│                   │ different distances│ star shapes into cross │
├─────────────────────────────────────────────────────────────────┤
│ Field curvature   │ Flat sensor vs     │ Sharp center → blurry  │
│ (Petzval)         │ curved focal plane │ edges, or vice versa   │
├─────────────────────────────────────────────────────────────────┤
│ Distortion        │ Off-axis magnif.   │ Barrel (wide angle)    │
│                   │ varies with angle  │ or pincushion (tele)   │
│                   │                    │ Lines bow in/out       │
└─────────────────────────────────────────────────────────────────┘
```

### Chromatic Aberrations

```
LONGITUDINAL (axial) CA:
  Glass refractive index varies with wavelength (dispersion)
  → different wavelengths focus at different distances
  → color fringing (magenta/green) on high-contrast edges throughout image
  Reduced by: apochromatic design (APO/apo), extra-low dispersion (ED/LD) glass,
              fluorite elements (CaF₂ — very low dispersion)

LATERAL (transverse) CA:
  Off-axis: different wavelengths focus at different heights on sensor
  → color fringing only at edges of image (not center)
  → easily corrected in software (simple scaling per channel)

Abbe number V = (nd - 1) / (nF - nC)
  nd = index at 589nm (yellow), nF = 486nm (blue), nC = 656nm (red)
  High V (>60): low dispersion glass (crown glass family)
  Low V (<30): high dispersion glass (flint glass family)
  Doublet design (crown + flint) corrects CA by combining divergent and convergent
  elements with complementary dispersions → achromat
```

---

## Modulation Transfer Function (MTF)

MTF is the single most informative characterization of a lens + sensor system.

```
MTF = (I_max - I_min) / (I_max + I_min) at spatial frequency f (cycles/mm or lp/mm)

MTF = 1.0: perfect contrast reproduction
MTF = 0:   no contrast at all (can't resolve that frequency)
MTF = 0.5: typically considered resolving limit for critical work
MTF = 0.1: Rayleigh criterion (just barely distinguishable)

MTF curve shape:
  High MTF →    ██████████▄▄▄▄────
  (good lens)   |         |    |
               DC   10lp/mm  40lp/mm

Perfect diffraction-limited lens (Airy pattern):
  MTF_diff(f) = (2/π)[arccos(f/fc) - (f/fc)√(1-(f/fc)²)]
  where fc = 1/(λN) = cutoff frequency
  At f/2.8, λ=0.55µm: fc = 1/(0.55×10⁻³ × 2.8) ≈ 649 lp/mm
  Pixel-limited cutoff (e.g., 24MP FF, 6µm pixel): 1/(2×6µm) = 83 lp/mm
  → Real sensor resolution limited by pixel pitch, not diffraction, at moderate apertures
```

---

## Anti-Reflection Coatings

Uncoated glass reflects ~4% per surface (Fresnel reflection, n≈1.5):
- A 10-element/8-group lens has 20 air-glass surfaces → 0.96²⁰ ≈ 44% transmission
- Every reflection also appears as a ghost or flare element

AR coating: thin film of lower-index material deposited on glass surface.

```
SINGLE LAYER AR COATING (quarter-wave):

  Air (n₁ = 1.0)
  ─────────────────── reflected ray 1 (from air-coating interface)
  Coating (n₂ = √(n₁n₃)) ← optimal index
  thickness = λ/4 (at design wavelength)
  ─────────────────── reflected ray 2 (from coating-glass interface)
  Glass (n₃ ≈ 1.5)

  Rays 1 and 2 are 180° out of phase (λ/4 round trip = λ/2) → destructive interference
  → Reflection drops from ~4% to ~1% at design wavelength

  Single layer: good at one wavelength, purple/magenta color cast at others

MULTILAYER COATING (modern lenses):
  Multiple λ/4 layers of alternating high/low index
  → Reflection reduced to 0.1–0.5% across visible spectrum (400–700nm)
  → Appears green/blue (remaining reflection) — the "T*" (Zeiss), "SMC" (Pentax)

NANO-CRYSTAL COATING (Nikon Nano-Crystal Coat):
  Sub-wavelength structures reduce reflection by graded-index transition
  → Effective against wide-angle flare from oblique light
```

---

## Lens Design Architecture

```
SIMPLE LENS (singlet): 1 element, spherical. Strong aberrations. Only for simple optics.

DOUBLET (achromatic): 2 elements (crown + flint cemented). Corrects longitudinal CA.
  Standard for low-cost telescope objectives, enlarger lenses.

TESSAR (4 elements / 3 groups): Carl Zeiss 1902. Compact, sharp at f/4.5–f/8.
  "The eagle eye" — millions produced in Kodak-equivalent cameras.

DOUBLE GAUSS (6 elements): Basis for most 50mm f/1.4 primes to this day.
  Symmetric design cancels coma, distortion. Used since 1896.

RETROFOCUS (reversed telephoto): Extra negative front element → long back focal
  distance needed for SLR mirror clearance. All wide-angle SLR lenses.

TELEPHOTO: Positive front group + negative rear → shorter physical length than focal length.
  e.g., 400mm focal length in 280mm physical barrel.

ZOOM LENS: Multiple groups that translate to change focal length while maintaining
  focus. Modern optical design + CAD enables zooms approaching prime quality.
  Key: varifocal (focus shifts with zoom) vs parfocal (stays in focus — cinema standard).
```

---

## Decision Cheat Sheet

| Goal | Choice |
|------|--------|
| Max low-light performance | Fast prime (f/1.4–f/1.8); accept narrow DoF |
| Max depth of field, sharp throughout | Stop down to f/8–f/11; watch diffraction limit |
| Minimize CA on telephoto | APO/ED glass elements; budget for them |
| Best corner sharpness | Stop down 1–2 stops from maximum |
| Max resolution (pixel-level) | Stay above diffraction limit: f/8 is often optimum for FF |
| Minimize distortion | Prime lenses; or correct barrel/pincushion in post |
| Best flare resistance | Multi-coated modern lens; lens hood; avoid shooting into sun |

---

## Common Confusion Points

**Focal length doesn't change with sensor size**
A 50mm lens is a 50mm lens on any camera. What changes is the angle of view because the sensor sees a different portion of the projected image circle. "Crop factor" describes this relationship but doesn't change the optical properties of the lens.

**Stopping down doesn't always improve sharpness**
Optimal aperture for sharpness is a peak, not a monotone. Wide open: aberrations degrade sharpness. Optimal: ~f/5.6–f/8 for most lenses. Stopped down further: diffraction takes over. Specific optimum depends on the lens design and pixel pitch of the sensor.

**"Sharp" is a system property, not just a lens property**
MTF at the image plane = lens MTF × sensor MTF × anti-aliasing filter × motion (shake/subject). A theoretically perfect lens looks soft on a camera with significant camera shake. Sharpening in post can restore some apparent acutance but cannot recover truly lost detail.

**Bokeh is not just about aperture size**
Background blur amount is a function of aperture, focal length, focus distance, and background distance. Bokeh quality (whether it's pleasing) is determined by the lens's spherical aberration profile, aperture blade count, and field curvature. Same f/1.4 aperture on different lenses produces very different looking blur.

**f-stop isn't the only factor in exposure**
Equivalent exposures: f/2.8 at 1/250s at ISO 400 = f/4 at 1/125s at ISO 400 = f/2.8 at 1/500s at ISO 800. All these produce the same total light exposure but have very different DoF, motion blur, and noise properties. Exposure is the sum; each triangle vertex trades against the others.
