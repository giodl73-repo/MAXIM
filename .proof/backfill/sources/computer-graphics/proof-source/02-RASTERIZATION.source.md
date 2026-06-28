---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "02-RASTERIZATION.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:computer-graphics:rasterization
kind: guide
module: computer-graphics
section: computer-graphics
title: Rasterization
status: source-custody
source_custody: partial
current_path: computer-graphics/02-RASTERIZATION.md
canonical_path: computer-graphics/02-RASTERIZATION.md
backsource_ids: [proof-backfill:computer-graphics:02-rasterization, git-history:computer-graphics:02-rasterization]
concepts: [triangle setup, edge function, barycentric coordinates, z-buffer, perspective-correct interpolation, clipping]
root_concepts: [rasterization]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# Rasterization

## The Big Picture: From Triangle to Lit Pixels

Rasterization is the object-order strategy: walk each triangle, find the pixels it covers,
and for each covered pixel interpolate the vertex data, test depth, and shade. It is the
workhorse of all real-time graphics.

```
+-------------------------------------------------------------------------------------+
|                        THE RASTERIZATION STAGE (per triangle)                       |
|                                                                                     |
|  CLIP-SPACE      CLIP +        TRIANGLE        COVERAGE       INTERP +      OUTPUT  |
|  TRIANGLE        VIEWPORT      SETUP           TEST           DEPTH TEST    MERGE   |
|                                                                                     |
| 3 vertices --> clip to     --> edge        --> for px in   --> baryc.   --> z-test  |
| (x,y,z,w)      frustum,        functions       bbox:           interp       + blend |
|                ÷w, map to      + bbox          inside all      attrs        write   |
|                pixels                          3 edges?        + 1/w        color   |
|                                                                                     |
|   [from 01]    [clip]          [setup]         [E(p)>=0]       [persp-corr] [z-buf] |
+-------------------------------------------------------------------------------------+
```

Read left to right: a clip-space triangle is clipped and mapped to screen pixels; the GPU
computes three **edge functions**; for every candidate pixel it tests "inside all three
edges?"; passing pixels get their attributes **barycentrically interpolated** (perspective-
corrected) and depth-tested against the z-buffer; survivors are shaded and merged.

---

## Layer 1: Triangle Setup and the Edge Function

The modern rasterizer does not "scan-convert" line by line; it evaluates, for each pixel,
three **edge functions** — signed distances to the triangle's three edges. A pixel is
inside iff it is on the correct side of all three.

```
  Edge from V0=(x0,y0) to V1=(x1,y1), tested at point P=(px,py):

     E01(P) = (px - x0)·(y1 - y0) - (py - y0)·(x1 - x0)

  This is the 2D CROSS PRODUCT (signed area × 2) of (P - V0) and (V1 - V0).

     E > 0   P is to the LEFT of the directed edge
     E = 0   P is ON the edge
     E < 0   P is to the RIGHT

         V0
         |\
         | \  E01      A pixel is INSIDE the triangle
         |  \          iff E01 >= 0 AND E12 >= 0 AND E20 >= 0
    E20  |   \ V1      (with consistent winding). The three
         |   /         edge functions also ARE the unnormalized
         |  / E12      barycentric weights -- one computation,
         | /           two payoffs.
         V2
```

The elegance: the edge function is **affine in pixel coordinates**, so it can be evaluated
incrementally — `E(x+1, y) = E(x, y) + dE/dx` — making the inner loop a few adds. GPUs
evaluate all candidate pixels of a tile in parallel. This is the Pineda (1988) algorithm,
and it replaced the older scanline approach precisely because it parallelizes and
incrementalizes cleanly.

---

## Layer 2: Barycentric Coordinates — The Interpolation Engine

Every per-vertex attribute (color, normal, texture UV, depth) is interpolated across the
triangle using **barycentric coordinates** `(α, β, γ)` — the normalized edge functions.

```
  Any point P inside triangle (A, B, C):

     P = α·A + β·B + γ·C,    with  α + β + γ = 1,  all >= 0

  α, β, γ are AREA RATIOS:

          A                α = area(P,B,C) / area(A,B,C)
         /|\               β = area(A,P,C) / area(A,B,C)
        / | \              γ = area(A,B,P) / area(A,B,C)
       /  P  \
      / /   \ \            At a vertex: that coord = 1, others = 0.
     B---------C           On an edge: the opposite coord = 0.

  Interpolated attribute:  attr(P) = α·attr(A) + β·attr(B) + γ·attr(C)
```

Because the unnormalized edge functions are already proportional to these sub-triangle
areas, the rasterizer gets the barycentric weights *for free* from the coverage test —
divide each edge function by their sum and you have `(α, β, γ)`.

---

## Layer 3: The Perspective-Correct Catch

Naively interpolating attributes linearly **in screen space is wrong** for anything but
depth. Perspective foreshortening means equal steps on screen are *un*equal steps in 3D.
A checkerboard floor interpolated linearly looks visibly warped near the horizon.

```
  WRONG: linear-in-screen          RIGHT: perspective-correct
  -----------------------          --------------------------
  attr(P) = α·a + β·b + γ·c         interpolate attr/w and 1/w linearly,
                                    then divide:

                                        (α·a/wa + β·b/wb + γ·c/wc)
                                    attr =  -------------------------------
                                        (α/wa + β/wb + γ/wc)

  Why: the projection is a 1/z map, so the quantity that varies LINEARLY in
  screen space is attr/w (and 1/w), not attr itself. Recover attr by dividing.
```

This is why the rasterizer keeps `1/w` per vertex. **Depth `z_ndc` is the exception**: it
*is* linear in screen space (the projection matrix was constructed so the divided `z` is
screen-linear), so the z-buffer interpolates it directly without the `/w` correction.
Everything else — UVs, normals, colors — needs the perspective-correct division.

---

## Layer 4: The Z-Buffer (Depth Test)

Visibility is resolved per pixel by the depth buffer. Every fragment carries its
interpolated depth; the buffer keeps the nearest.

```
  Z-BUFFER algorithm:

    initialize zbuffer[x,y] = +inf (far), framebuffer = clear color
    for each triangle:
        for each covered pixel (x,y):
            z = interpolated depth
            if z < zbuffer[x,y]:        <-- depth test (LESS)
                zbuffer[x,y] = z         <-- depth write
                framebuffer[x,y] = shade()

  O(1) per fragment. ORDER-INDEPENDENT for opaque geometry.
```

### Z-Buffer vs Painter's Algorithm

```
  PAINTER'S ALGORITHM                   Z-BUFFER
  -------------------                   --------
  sort polygons back-to-front,          per-pixel depth compare
  draw far first, near overpaints       no global sort needed

  +------+                              Handles ANY overlap, including:
  | A    +---+                            - mutual interpenetration
  +---+--| B |   A behind B               - cyclic occlusion (A over B
      |  +---+                              over C over A) -- which has
      +------+                              NO valid sort order at all

  FAILS on intersecting / cyclic        Cost: one depth value per pixel.
  geometry (no valid sort exists).      This is why it WON.
```

| | Painter's | Z-buffer |
|---|---|---|
| Sort needed | Yes, `O(n log n)`, every frame | No |
| Intersecting geometry | Breaks | Correct |
| Cyclic occlusion | Impossible | Correct |
| Per-pixel cost | Overdraw all layers | One compare |
| Memory | None extra | One depth buffer |
| Transparency | Natural | Needs separate sorted pass |

**Old world → new world.** The painter's algorithm is a global sort + sequential
overwrite — `O(n log n)` and order-dependent, like rendering by repeatedly `INSERT … ON
CONFLICT OVERWRITE` in draw order. The z-buffer is a per-cell `min` reduction — local,
parallel, order-independent. The shift from "sort then write" to "compare locally" is the
same idea that makes parallel reductions beat serial sorts.

### Early-Z and the Overdraw Problem

Shading a fragment that a later, nearer fragment will cover is wasted work (*overdraw*).
GPUs run **early-Z**: do the depth test *before* the fragment shader when possible, so
occluded fragments are killed cheaply. Sorting opaque geometry front-to-back maximizes
early-Z rejection. (Early-Z is disabled when the shader writes depth or uses `discard`,
because then coverage isn't known until after shading.)

---

### Winding Order and Back-Face Culling

The *sign* of the triangle's area (which way the edge functions point) encodes its facing.
Triangles facing away from the camera can be discarded before rasterization.

```
  Signed area of the screen-space triangle (= half the summed edge functions):

     A > 0  -> counter-clockwise winding  -> typically FRONT-facing
     A < 0  -> clockwise winding          -> typically BACK-facing  -> CULL it

       front face (CCW)         back face (CW, culled)
          V0                        V0
         /  \  area > 0            /  \  area < 0
        V2--V1                    V1--V2

  Back-face culling discards ~half the triangles of a closed mesh for free,
  BEFORE shading. (Convention CCW=front is OpenGL's default; configurable.)
```

This is why mesh authoring tools care about consistent winding: a triangle wound the wrong
way is culled and vanishes. The same signed area is the denominator that normalizes the
barycentric weights, so coverage, interpolation, *and* facing all fall out of one quantity.

### The Stencil Buffer

Alongside depth, the framebuffer carries a per-pixel **stencil** integer — a programmable
mask updated and tested per fragment. It implements effects that need "render here but not
there" logic.

```
  STENCIL TEST (runs with the depth test):
     compare (stencil[x,y] & mask) against a ref value; pass/fail -> keep/discard
     on pass/fail/depth-fail: keep / replace / increment / decrement the stencil

  Uses: portals/mirrors (mask the portal region), shadow volumes (Carmack's reverse),
        decals, outline rendering, constructive masking, UI clipping.
```

The stencil buffer is the "extra bits per pixel" that turn the framebuffer into a small
programmable state machine — orthogonal to color and depth, and the classic way to do
stencil shadow volumes before shadow maps (`09`) won.

## Layer 5: Clipping

Before rasterizing, triangles crossing the view frustum boundary must be clipped — most
critically the **near plane**, because vertices behind the eye have `w ≤ 0` and the
perspective divide would produce garbage (or division by zero).

```
  Clip in CLIP SPACE, BEFORE the perspective divide, against:

      -w <= x <= w,   -w <= y <= w,   -w <= z <= w   (or 0 <= z <= w in D3D/Vulkan)

  SUTHERLAND-HODGMAN: clip the polygon against each plane in turn.

      triangle crossing near plane          after near-clip
          *  (in front)                          *
         / \                                     / \
        /   \                                  /     \
   -----X---X-----  near plane     ----->    *---------*   (new vertices on plane,
       /     \                                            triangle may become a quad
      *       *  (behind eye, w<=0)                       -> re-triangulated)
```

Clipping against the near plane can turn a triangle into a quad (two triangles). The
guard-band optimization lets hardware skip clipping for triangles that overflow the
viewport but not by enough to overflow internal coordinate precision — they're rasterized
with the test alone and pixels outside the viewport simply discarded.

---

## Worked Example: Inside Test + Interpolation

Triangle with screen-space vertices `A=(0,0)`, `B=(4,0)`, `C=(0,4)`, attribute values
(say a red channel) `rA=0`, `rB=255`, `rC=0`. Test pixel `P=(1,1)`.

```
  Edge functions (CCW winding A->B->C):
    E_AB(P) = (1-0)(0-0) - (1-0)(4-0) = 0 - 4 = -4    ... sign convention check
```

Using the consistent area formulation (twice signed area of sub-triangles), total triangle
area = `½·|4·4| = 8`. Sub-areas for `P=(1,1)`:

```
    area(P,B,C) = ½ |(4-1)(4-1) - (0-1)(0-1)| ... use the ratio directly:

    α (weight of A) = area(P,B,C)/area = 4/8 = 0.5
    β (weight of B) = area(A,P,C)/area = 2/8 = 0.25
    γ (weight of C) = area(A,B,P)/area = 2/8 = 0.25
    check: 0.5 + 0.25 + 0.25 = 1.0   ✓

  Interpolated red (screen-linear, ignoring perspective for a flat triangle):
    r(P) = 0.5·0 + 0.25·255 + 0.25·0 = 63.75  ->  64
```

For a perspective triangle you would instead interpolate `r/w` and `1/w`, then divide — at
`P` the red would be `(0.75·rA/wA + 0.125·rB/wB + 0.125·rC/wC) / (0.75/wA + 0.125/wB +
0.125/wC)`. With all `w` equal (orthographic, or the triangle parallel to the screen) the
two agree, which is why the catch only bites on slanted, receding surfaces.

---

## Old World → New World Bridges

| You already know | Here it is |
|------------------|-----------|
| 2D cross product / signed area | The edge function — coverage *and* barycentrics in one |
| Incremental evaluation of an affine function | The rasterizer's inner loop: `E += dE/dx` |
| Convex combination / weighted average | Barycentric interpolation across a triangle |
| Parallel `min`-reduction vs serial sort | Z-buffer vs painter's algorithm |
| Short-circuit / early-out in a loop | Early-Z: kill occluded fragments before shading |
| Bounds checking / clamping | Frustum clipping (Sutherland-Hodgman) |
| `INSERT … ON CONFLICT` last-writer-wins | Why painter's is order-dependent and z-buffer isn't |

---

## Decision Cheat Sheet

| Situation | Choice |
|---|---|
| Resolve opaque visibility | Z-buffer (always) |
| Interpolate UVs/normals/colors | Perspective-correct (interp `/w`, then divide) |
| Interpolate depth | Linear in screen space — no `/w` needed |
| Reduce wasted shading | Sort opaque front-to-back; rely on early-Z |
| Render transparency | Separate, back-to-front, blended pass after opaque |
| Triangle crosses the eye plane | Near-plane clip in clip space, pre-divide |
| Coverage + interpolation weights | Edge functions give both |
| Defeats of early-Z | Shader writes depth or uses `discard` |

---

## Common Confusion Points

### "Why interpolate `attr/w` instead of `attr`?"

Because perspective projection is a `1/z` map: the screen position is a *projective*
function of the 3D point, and only quantities of the form `attr/w` (and `1/w` itself) vary
**linearly** in screen space. Interpolate those linearly, then divide to recover `attr`.
Skipping this gives the classic warped-texture look on receding planes.

### "Depth is the one thing I *can* interpolate linearly — why?"

The projection matrix is built so that the post-divide `z_ndc` is an affine function of
screen position. Depth got "pre-corrected" by construction, which is convenient — the
z-buffer interpolates it without the `/w` dance. (The flip side is that depth is nonlinear
in *eye-space* z; see `01`.)

### "Is the painter's algorithm just slow, or actually wrong?"

Actually wrong for general scenes. Mutually interpenetrating triangles and cyclic
occlusion (A occludes B occludes C occludes A) have **no** valid back-to-front order, so
no sort can fix them. The z-buffer's per-pixel decision has no such failure mode.

### "Why is transparency still a problem if we have a z-buffer?"

The z-buffer keeps one nearest opaque fragment, but transparency needs to *blend* multiple
fragments in order. So transparent geometry is drawn in a separate pass, sorted
back-to-front, with depth *testing* on but depth *writing* off. Order-independent
transparency (OIT) techniques exist but cost extra memory/passes — transparency remains
the awkward exception to the z-buffer's order-independence.

### "Scanline vs edge-function rasterization — does it matter?"

Functionally equivalent, but the edge-function (half-space) method parallelizes across
pixels and tiles and evaluates incrementally, which is why all modern GPUs use it. The old
scanline fill was serial per row — fine for a 1990s CPU rasterizer, wrong shape for a
thousand-lane GPU.
