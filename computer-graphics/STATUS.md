# computer-graphics/ — Status

**10 files | Complete ✅**

| File | Topic | Status |
|------|-------|--------|
| `00-OVERVIEW.md` | The rendering landscape — scene → geometry → rasterize/trace → shade → display; the two grand strategies | ✅ |
| `01-TRANSFORMS-AND-PROJECTION.md` | Homogeneous coordinates, model/view/projection matrices, perspective vs orthographic, the clip-space pipeline | ✅ |
| `02-RASTERIZATION.md` | Triangle setup, edge functions, barycentric interpolation, z-buffer vs painter's algorithm, clipping | ✅ |
| `03-RAY-TRACING.md` | Ray-surface intersection, recursive Whitted tracing, path tracing, BVH/kd-tree acceleration structures | ✅ |
| `04-SHADING-AND-LIGHTING.md` | Phong → PBR, BRDFs and energy conservation, the rendering equation (Kajiya 1986), global illumination | ✅ |
| `05-TEXTURING-AND-SAMPLING.md` | UV mapping, the sampling theorem applied to texturing, mipmaps, filtering, aliasing and antialiasing (MSAA/SSAA) | ✅ |
| `06-GPU-AND-SHADERS.md` | The programmable pipeline, vertex/fragment/compute shaders, SIMT execution, the GPU memory hierarchy | ✅ |
| `07-GEOMETRY-AND-MESHES.md` | Mesh representations, parametric curves and surfaces (Bézier/NURBS), subdivision surfaces, LOD | ✅ |
| `08-COLOR-AND-PERCEPTION.md` | Color spaces, gamma vs linear light, sRGB, HDR, tone mapping; the bridge to colors/ | ✅ |
| `09-REAL-TIME-PIPELINES.md` | Forward vs deferred shading, shadow techniques, post-processing, modern explicit APIs (Vulkan/D3D12/Metal) | ✅ |

## Coverage Notes

Computer graphics as the discipline of turning a mathematical scene description into
pixels. The directory is organized around the rendering pipeline: it opens with the
landscape (the scene-to-display dataflow and the two grand strategies — rasterization
and ray tracing), then drills down each stage. The mathematical spine is explicit
throughout: homogeneous coordinates and the model/view/projection composition; the
edge-function and barycentric machinery of rasterization; ray-surface intersection
and acceleration structures; the rendering equation (Kajiya 1986) and physically
based BRDFs with energy conservation; the sampling theorem behind texture filtering
and antialiasing; the SIMT execution model of GPUs; parametric and subdivision
geometry; and color science (gamma, sRGB, linear light, HDR, tone mapping).

**Bridges:** colors/ (color science, gamma, perception), mathematics/ (linear algebra,
projective geometry, variational calculus), computer-architecture/ (GPU SIMT,
memory hierarchy), signal-processing/ (sampling theorem, reconstruction, aliasing),
optics/ (the physics of light transport), physics/ (radiometry).
