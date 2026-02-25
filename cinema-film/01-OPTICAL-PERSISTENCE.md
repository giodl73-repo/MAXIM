# Optical Persistence and Motion: Phi Phenomenon, Critical Flicker Fusion, Pre-Cinema Devices, Muybridge

## The Big Picture

Cinema depends on a perceptual trick. The mechanism is not what most people believe. Correcting the misconception requires understanding the actual neuroscience of apparent motion — which is far more interesting than the myth.

```
THE PERCEPTUAL MECHANISMS OF CINEMA

MYTH: "Persistence of Vision"
  Retinal afterimage of frame persists while next frame appears
  -> Frames blur into apparent continuous motion
  STATUS: INCORRECT. Afterimages are too slow and too weak.
          This was Peter Mark Roget's 1824 hypothesis.
          Disproven by 20th century perceptual psychology.

REALITY: Two distinct mechanisms work together:

  1. PHI PHENOMENON (Wertheimer, 1912)
     Two stationary lights alternating rapidly
     -> Brain perceives ONE light moving between positions
     No actual motion required
     This is apparent motion: a neural computation
     Operates at: ~10-100ms alternation intervals

  2. CRITICAL FLICKER FUSION (CFF)
     Flicker frequency at which light appears continuous
     Threshold: ~16-20 Hz (cycles/second) for typical conditions
     Below threshold: flicker visible
     Above threshold: steady light perceived
     At 24 fps: each frame lasts 41.7ms -> just above CFF
     Projector shutter: opens 3x per frame -> 72 flashes/sec
                        (well above CFF; no flicker perceived)

  3. BETA MOVEMENT (Korte, 1915)
     Specific type of apparent motion for discrete stimuli
     Object A at position 1, disappears
     Object B at position 2, appears (short delay)
     -> Brain perceives A moving from 1 to 2
     This is what makes an actor "walk across the screen"
```

---

## The Phi Phenomenon in Detail

Max Wertheimer's 1912 experiments (Gestalt psychology) established that apparent motion is a fundamental perceptual computation, not an illusion or error.

```
WERTHEIMER'S EXPERIMENT (1912)

Setup: Two slits in a dark box, illuminated alternately

Case 1: Very fast alternation (< 30ms interval)
  Both lights appear to be ON simultaneously
  (No motion perceived; simultaneous)

Case 2: Optimal interval (~60ms)
  ONE light appears to move from slit 1 to slit 2
  This is PHI PHENOMENON
  The brain interpolates a trajectory that doesn't exist

Case 3: Very slow alternation (> 200ms)
  Two separate lights blinking alternately
  No motion perceived; succession only

THE CRITICAL INSIGHT:
  In Case 2, the brain is not "seeing" something that exists.
  It is generating a percept (motion) from two still frames.
  The motion is a NEURAL COMPUTATION, not a physical event.

  This is exactly what cinema exploits.
  Each frame is a still photograph.
  The motion you perceive is constructed by your visual cortex.

  Computational analogy:
  Your visual system is running a motion estimation algorithm
  (similar to optical flow algorithms in computer vision)
  Input: two successive still frames
  Output: perceived motion vector

  OpenCV: cv2.calcOpticalFlow()
  Visual cortex: MT/V5 area processes motion perception
```

---

## Critical Flicker Fusion

```
CRITICAL FLICKER FUSION (CFF) THRESHOLD

Definition: Minimum frequency at which a flickering light
            appears perceptually continuous (steady)

FACTORS AFFECTING CFF:
  Light intensity: brighter -> higher CFF required
    (Brighter light -> more demanding signal -> more sensitive to flicker)
    Dim light: CFF ~10 Hz
    Bright light (cinema screen): CFF ~16-20 Hz
    Very bright light: CFF up to ~60 Hz (peripheral vision)

  Retinal area: peripheral retina has higher CFF than fovea
    (Rod-dominated periphery is more motion-sensitive)
    TV refresh rate 60Hz: designed for periphery, not just fovea

  Fatigue: tired observers have lower CFF

CINEMA FRAME RATES AND FLICKER MANAGEMENT:

  Early cinema: 16-18 fps
    Problem: visible flicker in bright scenes
    Projector shutter: 2-blade (each frame shown 2x = 32-36 flashes/sec)
    This reduces flicker but not eliminating it

  Standard sound cinema: 24 fps (established ~1927)
    3-blade projector shutter: each frame shown 3x = 72 flashes/sec
    72 Hz >> CFF threshold -> no flicker perceived

  Television: 25 fps (PAL, Europe) / 30 fps (NTSC, US)
    60 Hz refresh (US power line frequency synchronization)
    Interlaced scanning: two fields/frame
    No flicker problem

  High Frame Rate (HFR):
    Peter Jackson: The Hobbit (2012) at 48 fps
    "Too smooth", "looks like video" - audience complaints
    The "film look" is partly the motion blur of 24 fps
    Higher frame rate = less motion blur = different aesthetic
    James Cameron: Avatar sequels at 48 fps (mixed)
    Sports/broadcast: 50/60 fps preferred (less motion blur helpful)
```

---

## Pre-Cinema Optical Toys

The sequence of inventions that decoded the persistence of motion problem.

```
PRE-CINEMA OPTICAL DEVICES TIMELINE

1824: Peter Mark Roget — "Persistence of Vision" paper
      (Royal Society, London)
      Proposed mechanism (later proven incorrect)
      But: stimulated interest in motion perception experiments

1825: THAUMATROPE
      Two-sided disc on a string
      Side 1: bird        Side 2: cage
      Spin disc: bird appears INSIDE cage
      Mechanism: alternation too fast to resolve separately
      Simple demonstration of apparent fusion

      +-------+        +-------+
      |  Bird |  spin  | Cage  |
      |  (1)  | -----> | (2)   |
      +-------+        +-------+
                           -> Bird in cage perceived

1832: PHENAKISTOSCOPE (Plateau, Belgium; Stampfer, Austria, simultaneously)
      Slotted disc with sequential animation drawings around edge
      Spin disc, view through slots in mirror
      Slots: act as shutter (block view between frames)
      Sequential drawings: apparent motion
      First device to create smooth apparent motion from still images

1834: ZOETROPE ("wheel of life")
      Cylinder with slots, sequential drawings on inside strip
      Spin cylinder, look through slots
      No mirror needed; multiple viewers simultaneously
      More practical than phenakistoscope

1868: FLIP BOOK (kineograph, John Barnes Linnett)
      Simple: drawings on pages, flip rapidly
      Still the clearest demonstration of the principle
      Familiar to anyone who drew stick figures in textbook corners

1877: PRAXINOSCOPE (Reynaud, France)
      Replaced slots with inner ring of mirrors
      Mirrors reflect image from opposite wall of cylinder
      Brighter, clearer image than zoetrope
      1888: Reynaud adds projection + painted film strips (théâtre optique)
      First public projected animation (1892) — before Lumières
```

---

## Eadweard Muybridge and Motion Decomposition (1872-1887)

```
MUYBRIDGE'S MOTION STUDIES

LELAND STANFORD'S QUESTION (1872):
  Does a galloping horse have all four feet off the ground
  simultaneously? (Stanford bet $25,000 that it did)

  Problem: Human eye cannot resolve ~1/100 second events
           No camera fast enough + no film fast enough

MUYBRIDGE'S SOLUTION (Sacramento, 1872; Palo Alto, 1877-78):
  Multiple cameras triggered in sequence
  12-24 cameras in a row
  Tripwires connected to camera shutters
  Horse gallops through, breaks wires in sequence
  Each camera captures one moment of the stride

  SETUP:
  Camera 1   Camera 2   Camera 3 ... Camera 12
     |          |          |             |
  Wire 1 ---Wire 2 ---Wire 3 ---...Wire 12
  Attached to ground and to camera shutters

  Exposure time: 1/1000 to 1/2000 second
  (Required: collodion wet plate chemistry + improvised fast shutter)

RESULT:
  The horse IS fully airborne — but not at the apex/extension
  All four feet off ground during the TUCKED phase
  (When front legs tucking back and rear legs sweeping forward)
  This is the opposite of intuitive expectation

SIGNIFICANCE:
  Proved photography could decompose continuous motion
  into analyzable discrete frames
  -> Foundation for chronophotography (Marey)
  -> Foundation for cinema

ANIMAL LOCOMOTION (1887):
  781 plates, ~20,000 photographs
  Humans, horses, dogs, cats, birds in motion
  Published by University of Pennsylvania
  Used by artists, anatomists, scientists

  Digital equivalent: motion capture + point cloud data
  Same question: how does a body actually move in time?
```

---

## Étienne-Jules Marey and Chronophotography

```
MAREY'S CHRONOPHOTOGRAPHY (France, 1882-1895)

MAREY'S APPROACH: different from Muybridge
  Muybridge: multiple cameras, one photo each
  Marey: single camera, multiple exposures on same plate

CHRONOPHOTOGRAPHIC GUN (1882):
  Camera shaped like rifle
  Rotating disc shutter: 12 exposures/second
  All images on single glass plate
  Single image shows all positions of motion on one frame

  [Single plate shows bird wing positions at 12 positions]
  Reveals: wing geometry, thrust vectors, aerodynamic principles

ADVANTAGES:
  Shows continuous path of motion (positions in sequence)
  Relative timing preserved
  Used for: birds, humans, insects, smoke patterns
  Scientific instrument more than entertainment device

PAPER BAND FILM (1888):
  Paper roll replaced glass plates
  Longer sequences possible
  Precursor to celluloid film strip

PHYSIOLOGICAL INSIGHT:
  Marey analyzed: walking, running, jumping
  Force distribution in gait
  Used by physical therapists and sports scientists
  Modern motion capture is direct descendant

EDISON'S AWARENESS:
  Edison visited Marey's Paris lab in 1889
  Saw the chronophotographic work
  Dickson (Edison's assistant) designed Kinetoscope based on
  combining Marey's film strip idea with phonograph-cylinder concept
```

---

## The 35mm Film Standard

```
35mm STANDARD (1892-1909)

W.K.L. DICKSON (Edison laboratory):
  Working from Marey + Eastman's roll film
  Chose: 35mm wide celluloid film strip
  Perforations: 4 round holes per frame (Kinetoscope sprocket)
  Frame size: 18 x 24mm

  WHY 35mm?
  Edison wanted film to use his phonograph cylinder as reference
  Dickson: took Eastman's 70mm still photography film
           Cut lengthwise in half: 35mm
           (Convenient, not scientifically derived)

INTERNATIONAL STANDARDIZATION (1909):
  Paris congress standardized:
  Film width: 35mm
  Perforations: 4 per frame (Eastman/Edison style)
  Frame size: 18 x 24mm (later 18 x 22mm for Academy ratio)
  Speed: variable (sound required standard: 24fps = 1927)

IMPLICATIONS:
  35mm persisted as primary cinema format for 100+ years
  Sound film (1927): 24fps
  Academy ratio (1932): 1.375:1 aspect ratio
  "Academy flat" = standard framing for 60 years
  Digital projection: replaced physical 35mm (2012 widespread)
  IMAX: 65mm negative, 70mm print (much larger frame)

PERFORATIONS AS CLOCK:
  Film transport: perforations engage sprocket wheels
  Frame positioning: perforations define exact frame location
  Sound synchronization: frame count = timing reference
  Digital equivalent: timecode (SMPTE)
```

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| What is persistence of vision? | Incorrect theory: retinal afterimages persist between frames. Actual mechanisms are phi phenomenon + CFF. |
| What is the phi phenomenon? | Brain perceives motion between two sequentially presented stationary stimuli (Wertheimer, 1912) |
| What is critical flicker fusion? | ~16-20 Hz threshold below which light appears to flicker; cinema uses 72 flashes/sec (3-blade shutter x 24fps) |
| Who is Muybridge? | Eadweard Muybridge: decomposed horse gallop into sequential photos (1878); proved all-4-feet-airborne |
| Who is Marey? | Étienne-Jules Marey: chronophotographic gun (1882); multiple exposures on single plate; motion science |
| Why 35mm film? | Dickson cut Eastman 70mm film lengthwise; arbitrary choice that became international standard (1909) |
| Why 24fps? | Sound synchronization standard (1927); minimum for flicker-free experience at practical film speeds |
| What is a zoetrope? | Slotted rotating cylinder with sequential drawings inside; 1834; multiple viewers simultaneously |

---

## Common Confusion Points

**"24 frames per second is the minimum for the persistence of vision effect."** The mechanism is not persistence of vision (see above). The phi phenomenon works at different rates depending on conditions. 24fps was chosen for economic reasons (film stock conservation) and became standardized when sound sync required a fixed rate. 12fps can produce apparent motion; 24fps is just the accepted standard for imperceptible flicker at cinema screen brightness.

**"Muybridge invented motion pictures."** He invented multi-camera sequential still photography and demonstrated motion decomposition. He did not project continuous motion at a standard rate — he used a modified zoetrope with his slides. The sequence: Muybridge (decomposition) -> Marey (chronophotography, film strip) -> Dickson/Edison (continuous film strip at speed) -> Lumières (projection) -> cinema.

**"High frame rate (48fps+) is objectively better."** Higher frame rate reduces motion blur and makes action clearer. Whether that's "better" depends on purpose. Sports broadcasting prefers 60fps for clarity. Narrative cinema at 24fps has an associated aesthetic — the motion blur, the temporal resolution — that audiences have 100 years of association with. "Film look" is partly the 24fps artifact. 48fps feels different, not uniformly better.

**"The phi phenomenon is an illusion."** It's not an illusion in the sense of being erroneous — it's a fundamental feature of perceptual processing. The visual system is making the most statistically likely inference from available data (two similar images at nearby positions in rapid succession most likely indicate motion). It's correct perception of a physical scenario; the scenario just happens to be simulated.
