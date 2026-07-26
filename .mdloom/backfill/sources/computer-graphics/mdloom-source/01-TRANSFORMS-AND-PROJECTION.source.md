---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "01-TRANSFORMS-AND-PROJECTION.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:computer-graphics:transforms-and-projection
kind: guide
module: computer-graphics
section: computer-graphics
title: Transforms and Projection
status: source-custody
source_custody: partial
current_path: computer-graphics/01-TRANSFORMS-AND-PROJECTION.md
canonical_path: computer-graphics/01-TRANSFORMS-AND-PROJECTION.md
backsource_ids: [mdloom-backfill:computer-graphics:01-transforms, git-history:computer-graphics:01-transforms]
concepts: [homogeneous coordinates, model matrix, view matrix, projection matrix, clip space, perspective divide]
root_concepts: [coordinate transforms]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# Transforms and Projection

## The Big Picture: One Vertex's Journey Through Five Spaces

A vertex authored in a model's local frame must end up at an integer pixel. It passes
through a chain of coordinate systems, each reached by one matrix multiply (plus one
nonlinear divide at the end).

```
+--------------------------------------------------------------------------------------+
|                       THE COORDINATE PIPELINE (one vertex)                           |
|                                                                                      |
|  OBJECT       WORLD        CAMERA/EYE     CLIP          NDC          SCREEN/WINDOW   |
|  SPACE        SPACE        SPACE          SPACE         SPACE        SPACE           |
|  (local)      (shared)     (eye=origin)   (4D cube)     (cube /w)    (pixels)        |
|                                                                                      |
|    v   --M-->   v   --V-->   v    --P-->   v_clip --÷w-->  v_ndc --vp--> v_screen    |
|        model        view          proj          perspective    viewport              |
|        matrix       matrix        matrix         divide         transform            |
|                                                                                      |
|     [x,y,z,1]      [x,y,z,1]     [x,y,z,1]    [x,y,z,w]    [x/w,y/w,z/w,1] [px,py,d] |
|                                                                                      |
|   MVP = P · V · M     (column-vector convention: v' = M·v, applied right-to-left)    |
+--------------------------------------------------------------------------------------+
```

Three matrix multiplies (M, V, P), then a divide by `w` (the *perspective divide*, the
only nonlinear step), then a fixed viewport scale to pixels. The vertex shader (`06`)
emits the **clip-space** position; the GPU's fixed-function hardware does the divide and
viewport map.

> **Convention warning.** This guide uses **column vectors** and **right-to-left**
> composition: `v' = M·v`, and `P·V·M` means "apply M first." Some APIs/textbooks
> (notably classic Direct3D and DirectXMath) use **row vectors** with `v·M` and the
> *reverse* multiplication order. The math is identical; the matrices are transposes of
> each other. Pick one convention and never mix.

---

## Layer 1: Why Homogeneous Coordinates

The single conceptual hurdle. A 3×3 matrix is a *linear* map: it fixes the origin, so it
can rotate, scale, and shear — but it can **never translate** (`A·0 = 0` always). Yet
translation is the most basic transform we need. The fix is to embed 3D points in 4D.

```
  3D point  (x, y, z)   ->   homogeneous  (x, y, z, w),  with w = 1 for points

  Translation as a 4x4 matrix:        A 3x3 linear map CANNOT do this:

  | 1  0  0  tx |   | x |   | x+tx |       | a b c | | x |   no column
  | 0  1  0  ty | · | y | = | y+ty |       | d e f |·| y |   adds a constant
  | 0  0  1  tz |   | z |   | z+tz |       | g h i | | z |   -> origin fixed
  | 0  0  0  1  |   | 1 |   |  1   |

  The translation lives in the 4th COLUMN.
  Because w=1, that column is added verbatim.
```

The deeper truth: points and directions differ by their `w`.

```
  POINT      w = 1   ->  affected by translation (the 4th column adds)
  DIRECTION  w = 0   ->  IMMUNE to translation (0 · tx = 0)  [normals, ray dirs]
```

This is why you transform a *position* with the full matrix but a *direction* (or normal)
with `w = 0` — a surface normal must not pick up the object's translation. (Normals have
an extra subtlety: under non-uniform scale they transform by the **inverse transpose** of
the upper-left 3×3, to stay perpendicular to the surface.)

---

## Layer 2: The Model Matrix (object → world)

Places each object into the shared world. Built by composing translation, rotation, and
scale. **Order matters** — matrix multiplication is non-commutative.

```
  M = T · R · S      ("scale first, then rotate, then translate" — the usual choice)

  Applied to vertex v (right to left):
    1. S scales the model about its local origin
    2. R rotates it
    3. T moves it into place

  Why this order: scaling AFTER rotation would shear; translating BEFORE rotation
  would orbit the object around the world origin instead of spinning in place.
```

```
   T·R  (rotate, then translate)        R·T  (translate, then rotate)
   --------------------------------     --------------------------------
   object spins in place, then          object pushed out, then the whole
   slides to its position               thing swept around world origin
        +                                      .  <-- orbits this point
       /|\  spin here                          |
      / | \                                  +---+
     +--+--+ ---> slide                       \ | /  big arc
                                               \|/
   THESE ARE DIFFERENT. T·R != R·T.
```

**Old world → new world.** If you have ever multiplied a chain of affine transforms — a
change of basis, a graphics 2D matrix, a robotics DH transform — this is the same algebra.
The only new wrinkle is the homogeneous lift and the convention discipline.

### Representing Rotation: Matrix vs Euler vs Quaternion

Rotation is the part of the model matrix worth its own discussion, because there are three
common representations and each has a failure mode.

```
  ROTATION MATRIX (3x3, orthonormal, det = +1)
     pros: composes by multiplication; applies directly to vectors
     cons: 9 numbers for 3 DOF; drifts off SO(3) under repeated float ops
           (must re-orthonormalize); awkward to interpolate

  EULER ANGLES (yaw, pitch, roll — 3 numbers)
     pros: human-readable, compact
     cons: GIMBAL LOCK — at pitch = ±90°, yaw and roll axes align and one DOF is lost;
           order-dependent (XYZ vs ZYX differ); bad to interpolate through

  QUATERNION (unit q = w + xi + yj + zk on the 4-sphere, 4 numbers, 3 DOF)
     pros: no gimbal lock; cheap to compose; SLERP gives constant-speed shortest-arc
           interpolation; renormalize by one divide; numerically stable
     cons: not directly multiplicable with a position vector (convert to matrix, or
           use q·v·q^-1); double-cover (q and -q are the same rotation)
```

```
  GIMBAL LOCK (why Euler angles fail):

     pitch 0°:   yaw axis  _|_  roll axis      (3 independent DOF)
     pitch 90°:  yaw axis  ||   roll axis      (they coincide -> only 2 DOF left)

  -> a smooth path through pitch=90° snaps/spins. Apollo's IMU hit this in 1969.
  Quaternions have no such singularity because they parametrize SO(3) without
  a coordinate chart that degenerates.
```

The practical rule: **store and interpolate orientation as a quaternion** (animation,
cameras, physics), **convert to a matrix** to fold into the MVP. SLERP (spherical linear
interpolation) between two quaternions traces the shortest great-circle arc on the unit
4-sphere at constant angular speed — exactly what you want for tweening a camera between two
orientations, and what naive matrix or Euler interpolation gets wrong.

**Old world → new world.** A unit quaternion is to 3D rotation what a unit complex number
`e^{iθ}` is to 2D rotation — multiplication composes rotations, and the unit-magnitude
constraint keeps you on the rotation manifold. The MIT background pays off directly: SO(3),
its double cover SU(2), and the 4-sphere are the clean way to see why quaternions avoid the
Euler singularity.

---

## Layer 3: The View Matrix (world → camera)

The camera doesn't really "move." Instead we move the *world* so the camera sits at the
origin looking down `-z` (OpenGL convention). The view matrix is the **inverse** of the
camera's world transform.

```
  Camera placed in world by:  C = T_cam · R_cam
  View matrix:                V = C^-1 = R_cam^-1 · T_cam^-1

  A "look-at" view is built from three vectors:
     eye    : camera position
     center : point being looked at
     up     : approximate world-up (e.g. +y)

     f = normalize(center - eye)      forward
     r = normalize(cross(f, up))      right
     u = cross(r, f)                  true up (re-orthogonalized)

           |  r.x  r.y  r.z  -dot(r,eye) |
     V  =  |  u.x  u.y  u.z  -dot(u,eye) |
           | -f.x -f.y -f.z   dot(f,eye) |
           |  0    0    0     1          |
```

The upper-left 3×3 is an **orthonormal basis** (the camera's axes) — and for an orthonormal
rotation, the inverse is just the transpose, which is why the rows are `r, u, -f`. The
last column un-translates the eye. This is precisely a **change of basis** into the
camera's frame — the learner's linear algebra applied directly.

---

## Layer 4: Projection — Orthographic vs Perspective

Projection maps the visible volume (the *view frustum*) into a canonical cube so clipping
and the depth test are uniform. Two kinds.

```
  ORTHOGRAPHIC                          PERSPECTIVE
  ------------                          -----------
  parallel lines stay parallel          parallel lines converge (vanishing pts)
  no foreshortening (size = const)      farther = smaller (foreshortening)
  view volume is a BOX                  view volume is a FRUSTUM (truncated pyramid)

  +--------------------------------------------------------------------------+
  |    .--------.                              /----\                        |
  |    |        |   camera                    /      \    camera             |
  |    |        |   at infinity              /        \   at apex (eye)      |
  |    '--------'                           .----------.                     |
  |                                         near      far                    |
  +--------------------------------------------------------------------------+

  Use: CAD, 2D UI, shadow maps,          Use: anything that should look 3D
       isometric games                        to a human eye
```

### Perspective Projection Matrix

The defining trick: write `-z` into the output `w`, so the later divide shrinks distant
geometry. With vertical field of view `fovy`, aspect ratio `a`, and near/far planes
`n`, `f` (OpenGL-style, NDC `z` in `[-1, 1]`):

```
        let  t = 1 / tan(fovy / 2)

        |  t/a   0      0              0          |
   P =  |  0     t      0              0          |
        |  0     0   -(f+n)/(f-n)  -2fn/(f-n)     |
        |  0     0     -1              0          |   <-- bottom row puts -z into w

   Apply to (x, y, z, 1):   w_clip = -z      <-- the magic
```

After the divide by `w_clip = -z`:

```
  x_ndc = (t/a)·x / (-z)      <-- x shrinks as |z| grows  => foreshortening
  y_ndc =  t·y   / (-z)
  z_ndc = [-(f+n)z - 2fn] / [(f-n)(-z)]      <-- nonlinear in z
```

---

## Layer 5: The Perspective Divide and Depth Nonlinearity

```
  CLIP SPACE  (x, y, z, w)
        |
        |   ÷ w   (perspective divide — the ONLY nonlinear step in the pipeline)
        v
  NDC  (x/w, y/w, z/w)   each component now in [-1, 1]  (OpenGL)
```

A crucial consequence: NDC depth is **nonlinear** in eye-space `z`. Most precision sits
near the near plane; far away, many eye-space distances map to the same depth value.

```
  Z-FIGHTING and precision:

  eye-space z:   n |---------|---------|---------|---------| f
  NDC depth:       0    0.5      0.75    0.875    ...     1     (bunched up far away)

  => far surfaces compete for the same depth bits  -> flickering ("z-fighting")

  Fixes: push the near plane out (biggest lever), use a 32-bit/float depth buffer,
         or a REVERSED-Z buffer (map near->1, far->0) which pairs float mantissa
         precision with where the nonlinearity needs it. Reversed-Z is now standard.
```

This nonlinearity is not a bug — it is the direct result of the `÷w` that creates
perspective. The reversed-Z trick exploits floating-point's higher precision near 0 to
counteract the projection's compression at the far plane.

---

## Worked Example: A Vertex End to End

Take a vertex at the model's local origin offset, with a simple setup. Suppose after the
model and view matrices a vertex lands in **eye space** at `(1, 0, -10, 1)` — one unit
right of center, 10 units in front of the camera. Use `fovy = 90°` (so `t = 1`),
`aspect a = 1`, `n = 1`, `f = 100`.

```
  Apply P:
    x_clip = (t/a)·x = 1·1 = 1
    y_clip = t·y     = 0
    z_clip = -(f+n)/(f-n)·z - 2fn/(f-n)·1
           = -(101/99)·(-10) - (200/99)·1
           = 10.20 - 2.02 = 8.18
    w_clip = -z = 10

  Perspective divide (÷ w = 10):
    x_ndc = 1 / 10 = 0.10        <-- close to center because it's far away
    y_ndc = 0
    z_ndc = 8.18 / 10 = 0.818    <-- already past midpoint of [-1,1] at z=-10

  Viewport map to an 800x600 window:
    px = (x_ndc + 1)/2 · 800 = (1.10)/2 · 800 = 440
    py = (1 - (y_ndc+1)/2) · 600 = 300        (y flipped: screen y grows downward)

  Result: pixel (440, 300), depth 0.818.
```

The same vertex moved to `z = -2` (closer) would give `x_ndc = 1/2 = 0.5` → pixel 600 —
the *same world offset* projects farther from center when nearer. That is foreshortening,
falling straight out of the `÷w`.

---

## Old World → New World Bridges

| You already know | Here it is |
|------------------|-----------|
| Affine map = linear part + translation | The homogeneous 4×4 packs both into one matrix |
| Change of basis matrix | The view matrix — rebasing world into camera frame |
| Inverse of an orthonormal matrix is its transpose | Why the view matrix rows are the camera axes |
| Non-commutative matrix products | `T·R ≠ R·T` — transform order changes the result |
| Projective geometry / points at infinity | `w = 0` directions; perspective as a projective map |
| Inverse-transpose for dual vectors | Normals transform by the inverse transpose of the 3×3 |
| Floating-point precision near zero | Reversed-Z depth buffer exploits exactly this |

---

## Decision Cheat Sheet

| Situation | Choice |
|---|---|
| Human-eye 3D look (games, viz) | Perspective projection |
| CAD, 2D UI, isometric, shadow maps | Orthographic projection |
| Transforming a position | Multiply by full matrix, `w = 1` |
| Transforming a direction / ray | `w = 0` (immune to translation) |
| Transforming a normal under non-uniform scale | Inverse transpose of the upper-left 3×3 |
| Object should spin in place then move | `M = T · R · S` |
| Z-fighting on distant geometry | Push near plane out; float depth; reversed-Z |
| Mixing two libraries' matrices | Confirm row vs column convention first |
| Building a camera from eye/center/up | `lookAt` → view matrix |

---

## Common Confusion Points

### "Why does pushing the near plane out fix z-fighting more than pulling far in?"

Depth precision is dominated by the **near** plane because the `1/z` nonlinearity crowds
precision near it. The usable depth range scales roughly with `f/n`; halving `n` is far
worse than doubling `f`. Set the near plane as far out as your scene tolerates.

### "Is the order P·V·M or M·V·P?"

With **column vectors** (`v' = M·v`), it is `P·V·M` and you read it right-to-left: M
applied first. With **row vectors** (`v' = v·M`), it is `M·V·P` read left-to-right. Same
geometry; the matrices are transposes. The error mode is silently using one library's
matrices with the other's multiply order.

### "Clip space vs NDC — what's the difference?"

**Clip space** is the 4D homogeneous result *before* the divide; clipping against the
frustum happens here (against `-w ≤ x,y,z ≤ w`) precisely because doing it pre-divide
avoids dividing by zero or negative `w`. **NDC** is the 3D result *after* dividing by `w`,
living in the canonical cube. Clipping before the divide is why the hardware keeps the
4-vector around.

### "Why does z come out nonlinear when x and y are 'linear'?"

All three are linear in clip space; the divide by `w = -z` is what makes *depth*
nonlinear, because depth itself is the thing being divided by. X and Y are also divided by
`-z`, which is exactly the foreshortening — there's no asymmetry, depth just *looks*
special because we store it.

### "OpenGL says NDC z is [-1,1] but Vulkan/D3D say [0,1] — who's right?"

Both, by convention. OpenGL uses `[-1, 1]` for NDC depth; Direct3D, Vulkan, and Metal use
`[0, 1]`. This changes the third row of the projection matrix (and pairs naturally with
reversed-Z in the `[0,1]` APIs). It's a convention choice, not a correctness one — but you
must match the API you target.
