---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "07-GEOMETRY-AND-MESHES.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:computer-graphics:geometry-and-meshes
kind: guide
module: computer-graphics
section: computer-graphics
title: Geometry and Meshes
status: source-custody
source_custody: partial
current_path: computer-graphics/07-GEOMETRY-AND-MESHES.md
canonical_path: computer-graphics/07-GEOMETRY-AND-MESHES.md
backsource_ids: [mdloom-backfill:computer-graphics:07-geometry, git-history:computer-graphics:07-geometry]
concepts: [triangle mesh, bezier curve, nurbs, subdivision surface, level of detail, mesh data structures]
root_concepts: [geometry, meshes]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# Geometry and Meshes

## The Big Picture: How Shape Is Stored

Before anything is shaded, the scene's *shape* must be represented. There is a spectrum from
smooth mathematical surfaces (compact, exact, editable) to dense triangle meshes (universal,
fast to render). Authoring tends to live at the smooth end; rendering at the triangle end;
*tessellation* converts between them.

```
+--------------------------------------------------------------------------------------+
|                    THE GEOMETRY SPECTRUM (smooth <-> discrete)                       |
|                                                                                      |
|  PARAMETRIC          SUBDIVISION         TRIANGLE MESH        LOD / POINT            |
|  CURVES & SURFACES   SURFACES            (the workhorse)      CLOUDS / VOXELS        |
|                                                                                      |
|  Bezier / B-spline   Catmull-Clark   --> vertices + faces --> simplified meshes      |
|  NURBS               Loop                + attributes          per distance          |
|  (exact, compact,    (smooth from a       (universal, GPU-     point clouds,         |
|   CAD/fonts)          coarse cage)         native, flat        SDFs, voxels          |
|                                            triangles)                                |
|                                                                                      |
|        <------------------ TESSELLATION converts smooth -> triangles ----------->    |
|   [L2 curves]        [L3 subdiv]          [L1 meshes]          [L4 LOD]              |
+--------------------------------------------------------------------------------------+
```

The triangle mesh is the rendering hub because a triangle is always planar and convex, has
trivial barycentric interpolation (`02`), and intersects rays cheaply (`03`). Everything
smoother is usually *tessellated* down to triangles before it reaches the rasterizer or ray
tracer.

---

## Layer 1: The Triangle Mesh

A mesh is vertices plus connectivity. The minimal modern form is an **indexed mesh**: a
vertex array (positions + attributes) and an index array (triangles as vertex-index
triples).

```
   VERTEX BUFFER                 INDEX BUFFER
   pos        normal  uv         triangles (indices into vertex buffer)
   v0 (...)   (...)   (...)      (0,1,2)
   v1 (...)   (...)   (...)      (0,2,3)
   v2 (...)   (...)   (...)      (2,4,3)
   v3 (...)   (...)   (...)      ...
   v4 (...)   (...)   (...)

   Why INDEXED: a shared vertex is stored ONCE, referenced many times.
     non-indexed cube: 12 triangles x 3 = 36 vertices
     indexed cube:     8 vertices + 36 indices -> far less data, vertex-cache reuse
```

### Vertex Attributes and the GPU's Vertex Cache

A vertex is more than a position — it's a small struct of attributes, and the *index* buffer
exists partly to exploit a hardware cache.

```
  A VERTEX carries (interleaved or in parallel streams):
     position (xyz)   normal (xyz)   tangent (xyzw)   uv (uv)   color   bone weights...

  POST-TRANSFORM VERTEX CACHE: the GPU caches recently transformed vertices by index.
     a vertex shared by 6 triangles is transformed ONCE if its uses are close in the
     index buffer. Reordering indices for cache locality (Forsyth / Tom Forsyth's
     algorithm, or "tipsify") cuts vertex-shader work measurably.

  -> the index buffer isn't just dedup; its ORDER is a performance knob.
```

This is why mesh tools run an index-optimization pass: the same triangle list, reordered so
shared vertices are referenced close together, hits the post-transform cache more often and
runs the vertex shader fewer times. It's the geometry analogue of cache-friendly array
traversal — locality of *reference* into the vertex buffer.

### Connectivity structures

Rendering only needs the indexed buffers, but *editing* (subdivision, simplification, normal
computation) needs neighbor queries — "which faces touch this edge?" The **half-edge** (DCEL)
structure answers these in O(1).

```
  HALF-EDGE: each edge split into two opposite directed half-edges.

     each half-edge knows:  its origin vertex, its face,
                            its NEXT half-edge (around the face),
                            its TWIN (the opposite half-edge)

  -> walk around a face, walk around a vertex's neighbors, find adjacent faces, all O(1).
  Manifold meshes only (each edge shared by exactly 2 faces).
```

**Old world → new world.** An indexed mesh is normalization: factor repeated vertex data into
a lookup table referenced by index — the same deduplication as a foreign key into a
dimension table. The half-edge structure is an adjacency representation of a planar graph,
chosen (like a doubly-linked structure) so the traversals you do most are O(1).

Per-vertex **normals** are computed by averaging adjacent face normals (area- or
angle-weighted); **smooth vs faceted** shading is just whether vertices on a hard edge are
*split* (duplicated with different normals) or *shared*.

---

## Layer 2: Parametric Curves and Surfaces

Smooth shapes are defined by control points and basis functions — compact, resolution-
independent, and the native language of CAD and fonts.

### Bézier Curves

```
  Cubic Bezier: 4 control points P0..P3, parameter t in [0,1]:

     B(t) = (1-t)^3 P0 + 3(1-t)^2 t P1 + 3(1-t) t^2 P2 + t^3 P3
            \________________ Bernstein basis polynomials ________/

         P1 ____ P2          - passes through P0 and P3 (endpoints)
         /        \          - P1, P2 pull the curve (tangent handles)
        /          \         - stays inside the CONVEX HULL of the control points
      P0            P3       - de Casteljau's algorithm: repeated lerps -> evaluate + split
```

de Casteljau evaluation is just repeated linear interpolation — numerically stable and the
basis for *subdividing* a curve. Bézier curves are what fonts (TrueType uses quadratics,
PostScript/OTF use cubics) and vector graphics are built from.

### B-splines and NURBS

```
  B-SPLINE   piecewise polynomial with LOCAL control (moving one control point
             affects only a few segments) + a KNOT VECTOR setting segment boundaries.

  NURBS      Non-Uniform Rational B-Spline = B-spline with per-control-point WEIGHTS
             and a rational (w-divided) form.
             -> the rational part can represent CONIC SECTIONS EXACTLY:
                a true circle/ellipse, which polynomial Beziers only approximate.
             -> the CAD industry standard (exact engineering surfaces).
```

The "rational" in NURBS is the same homogeneous-coordinate trick from `01`: dividing by a
weight `w` lets a polynomial curve trace an exact conic — a circle is a NURBS but never a
plain Bézier. A **tensor-product surface** `S(u,v)` is the 2D generalization: a grid of
control points with curve bases in each parameter direction.

| | Bézier | B-spline | NURBS |
|---|---|---|---|
| Control | Global (per segment) | Local | Local |
| Exact circles | No | No | **Yes** (rational) |
| Knot vector | No | Yes | Yes |
| Weights | No | No | Yes |
| Home | Fonts, vector art | Smooth paths | CAD/engineering |

### Continuity: C⁰, C¹, C², G¹

When curve segments join, *how smoothly* they meet has a precise vocabulary — it's the
difference between a visible crease and a seamless surface.

```
  C⁰  positions match           the curve is connected (but may have a corner/kink)
  C¹  + first derivatives match tangent is continuous (no kink), AND same speed
  C²  + second derivatives      curvature is continuous (no sudden bend) -> looks "fair"
  G¹  tangents POINT the same    geometric smoothness; direction matches but speed may not
      direction (not same mag)   (weaker than C¹; usually what the eye actually needs)

      C⁰ only:  __/\__   (corner)        C¹/G¹:  __/‾‾   (smooth tangent)
```

A uniform cubic B-spline is automatically C² across its joints — one reason it produces
"fair" curves for free, where stitching Bézier segments requires manually aligning control
points to get even C¹. Surfaces inherit this: a reflection sweeping across a car body reveals
curvature discontinuities (less than C²) as a visible flaw, which is why automotive CAD insists
on C² (or higher) class-A surfaces.

---

## Layer 3: Subdivision Surfaces

Subdivision builds a smooth surface as the *limit* of repeatedly refining a coarse control
mesh (the "cage"). It combines the editability of a low-poly mesh with the smoothness of a
spline — the dominant approach in film/character modeling.

```
  CATMULL-CLARK (quad meshes; Pixar's workhorse):

    each refinement step:
      1. FACE point   = average of the face's vertices
      2. EDGE point   = average of edge endpoints + adjacent face points
      3. update VERTEX = weighted blend of itself, edge midpoints, face points
      -> connectivity refines (each quad -> 4 quads); surface approaches a limit

    cage (8 verts)  ->  step 1  ->  step 2  ->  ...  ->  smooth limit surface
      [][]               finer       finer              (a bicubic B-spline
                                                          away from irregular verts)

  LOOP subdivision: the triangle-mesh analogue (different masks; for triangle cages).
```

The key property is **local refinement to a known limit**: artists edit a sparse cage, the
renderer evaluates (or tessellates to) the smooth limit. Catmull-Clark surfaces are bicubic
B-splines except at *extraordinary vertices* (valence ≠ 4), where the limit is still smooth
but not polynomial — this is why subdivision, not raw NURBS patches, handles arbitrary
topology gracefully.

---

### Other Representations: Point Clouds, SDFs, Voxels

Triangles dominate, but several non-mesh representations matter for specific jobs.

```
  POINT CLOUD     unconnected 3D points (+ attributes) — the raw output of LiDAR /
                  photogrammetry. No surface yet; rendered as splats or reconstructed
                  into a mesh (Poisson reconstruction). Gaussian Splatting (2023) renders
                  them directly as anisotropic blobs for photoreal novel views.

  SDF (signed     a function f(x) = signed distance to the nearest surface
  distance field) (negative inside). Rendered by SPHERE TRACING (march along a ray in
                  steps of |f(x)| — guaranteed not to overshoot). Exact smooth surfaces,
                  cheap CSG (min/max combine shapes), soft shadows + AO almost free.
                  The demoscene/Shadertoy staple; also used for font/decal rendering.

  VOXELS          a 3D grid of cells. Natural for volumetric data (medical CT, clouds,
                  fluids) and easy boolean edits; costly in memory (O(n³)) -> sparse
                  voxel octrees (SVO) compress empty space.
```

Each trades the triangle's universality for a property triangles lack: point clouds capture
*measured* reality, SDFs give *exact* smooth surfaces and trivial CSG, voxels represent
*volumes* (interiors, not just boundaries). Most pipelines convert these to triangles for the
rasterizer, but ray marching an SDF or splatting points renders them directly.

## Layer 4: Level of Detail (LOD)

A mesh seen across the room needn't carry the polygon count it deserves up close. **LOD**
swaps in cheaper geometry with distance — fewer triangles where they wouldn't be seen anyway,
matching geometric detail to screen-space frequency (the sampling-theorem logic of `05`,
applied to *geometry*).

```
  DISCRETE LOD       precompute LOD0 (full), LOD1, LOD2 ... ; pick by distance.
                     risk: visible "popping" when switching -> cross-fade or dither.

  CONTINUOUS LOD     simplify on the fly (edge collapse) to a target triangle budget.

  GEOMORPHING        smoothly interpolate vertex positions between LODs to hide popping.

  NANITE-style (UE5) cluster the mesh into hierarchical "meshlets"; stream and pick
                     the right cluster LOD per-region per-frame -> ~pixel-sized triangles,
                     virtually unlimited source detail.

  MESH SIMPLIFICATION (building LODs):
     QUADRIC ERROR METRICS (Garland-Heckbert): collapse the edge whose removal
     introduces the least geometric error, measured by a per-vertex quadric.
```

```
   distance ->   close            mid             far
   LOD       ->  LOD0 (50k tris)  LOD1 (5k tris)  LOD2 (500 tris)
                  /\/\/\/\          /\/\            /\
   triangles roughly match the PIXELS they cover -> no wasted detail, no aliasing.
```

The principle is the same band-limiting as texture mipmaps: don't feed the rasterizer
geometric frequencies finer than a pixel — they only cost time and *alias* (sub-pixel
triangles shimmer and thrash the rasterizer). LOD is mip-mapping for shape.

---

## Worked Example: Subdividing a Bézier (de Casteljau)

Split a cubic Bézier at `t = 0.5` into two curves, by repeated midpoint lerps. Control
points `P0, P1, P2, P3`.

```
  Level 1 (midpoints of consecutive control points):
     A = (P0+P1)/2     B = (P1+P2)/2     C = (P2+P3)/2
  Level 2:
     D = (A+B)/2       E = (B+C)/2
  Level 3:
     F = (D+E)/2     <- the point ON the curve at t=0.5

  The two halves of the original curve are:
     left  curve: P0, A, D, F
     right curve: F, E, C, P3

  -> exact subdivision via only averages: numerically stable, and the basis for
     adaptive tessellation (keep splitting until each piece is within a flatness
     tolerance, then emit a triangle edge).
```

This is how a curved patch becomes triangles: recursively subdivide until each segment is
flat to within a screen-space tolerance, then connect the endpoints. It is also how the GPU
tessellation stage (`06`) refines patches on the fly.

---

## Old World → New World Bridges

| You already know | Here it is |
|------------------|-----------|
| Normalization / foreign keys | Indexed mesh — vertices stored once, referenced by index |
| Adjacency list of a planar graph | Half-edge (DCEL) structure for O(1) neighbor queries |
| Homogeneous coords / rational forms | NURBS weights — exact circles via the `w`-divide |
| Polynomial basis / interpolation | Bernstein basis of Bézier curves |
| Fixed-point / limit of an iterated map | Subdivision surface as the refinement limit |
| Mipmaps band-limiting textures (`05`) | LOD band-limiting geometry by distance |
| Greedy cost-minimizing simplification | Quadric error metric edge collapse |
| Streaming/paging a working set | Nanite-style cluster LOD streaming |

---

## Decision Cheat Sheet

| Situation | Choice |
|---|---|
| Render anything on a GPU | Indexed triangle mesh |
| Edit topology / compute normals / subdivide | Half-edge structure |
| Fonts, vector graphics, animation paths | Bézier curves |
| Exact engineering surfaces, true circles | NURBS |
| Smooth characters from an editable cage | Catmull-Clark (quads) / Loop (tris) subdivision |
| Cut triangle count with distance | LOD (discrete, continuous, or Nanite-style) |
| Hide LOD "popping" | Geomorphing / dither cross-fade |
| Build LODs automatically | Quadric error metric simplification |
| Smooth surface -> renderable triangles | Tessellation (adaptive de Casteljau) |

---

## Common Confusion Points

### "Why triangles and not quads or n-gons?"

A triangle is *always* planar and convex; a quad's four vertices may not be coplanar
(ambiguous surface) and an n-gon may be non-convex (hard to rasterize/intersect).
Barycentric interpolation (`02`) and ray intersection (`03`) are trivial for triangles.
Modeling tools love quads (clean subdivision, edge loops), but everything is triangulated
before rendering.

### "NURBS vs subdivision — both make smooth surfaces, so which?"

NURBS give *exact*, analytically defined surfaces (and exact conics), ideal for engineering
where tolerances are contractual — but they struggle with arbitrary topology (you stitch
trimmed patches). Subdivision handles any topology from a single editable cage and degrades
gracefully at irregular vertices, which is why film/games favor it for organic shapes. CAD →
NURBS; characters → subdivision.

### "Is a Bézier curve the same as a spline?"

A Bézier is a single polynomial segment with *global* control (each handle affects the whole
segment). A B-spline chains segments with *local* control and a knot vector, so editing is
local and continuity is automatic. NURBS adds weights for exact conics. Think Bézier ⊂
B-spline ⊂ NURBS in generality.

### "LOD vs mipmaps — related?"

Same principle, different domain. Mipmaps band-limit *texture* detail to the pixel rate; LOD
band-limits *geometry* detail to the pixel rate. Both prevent feeding the sampler frequencies
above Nyquist (which only cost time and alias). Sub-pixel triangles are the geometric
equivalent of an unmipped distant texture — they shimmer and waste the rasterizer.

### "What's an 'extraordinary vertex' and why care?"

A vertex whose valence isn't the regular value (4 for Catmull-Clark quads, 6 for Loop
triangles). At regular vertices the subdivision limit is a standard B-spline; at extraordinary
ones it's still smooth (C¹) but not a simple polynomial, needing special evaluation. They're
unavoidable on closed surfaces of nontrivial topology (you can't tile a sphere with only
valence-4 quads), so robust subdivision implementations handle them explicitly.
