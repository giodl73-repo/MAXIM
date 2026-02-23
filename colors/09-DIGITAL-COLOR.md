# 09 — Digital Color

## Bit Depth, ICC Profiles, Gamma, HDR, Color Management Pipeline

> **STUB** — outline only, content to be authored

**Planned coverage:**
- **Bit depth**: how many levels per channel; 8-bit per channel = 256 levels = 16.7M colors (sufficient for most display); 16-bit per channel = 65,536 levels (used in photo editing, avoids banding in smooth gradients); 10-bit per channel = 1,024 levels = 1.07B colors (HDR displays, streaming); 32-bit float = effectively unlimited (used in compositing/3D rendering); banding artifact = visible steps when bit depth insufficient for gradient
- **Gamma encoding**: human vision more sensitive to differences in dark tones than bright; linear encoding wastes bits on bright areas; gamma correction encodes dark values with more bits proportionally; sRGB uses approximately γ=2.2 (then a linear segment near black); display hardware applies inverse gamma; consequence: if gamma is applied twice or not applied → washed-out or too-dark image; common mistake in 3D rendering: operating in gamma-encoded (sRGB) space instead of linear space
- **Color spaces and profiles**:
  - sRGB: default internet/consumer standard; D65 white point; ~35% CIE gamut
  - Adobe RGB (1998): wider gamut (especially green), used for print preparation; incompatible with sRGB if profile ignored
  - ProPhoto RGB: extremely wide gamut (covers almost all visible colors); used for raw photo archiving; most colors outside sRGB, so only useful in editing workflow with proper management
  - Display P3: Apple display standard; ~25% wider than sRGB; default for iPhone/iPad content since ~2016
- **ICC profiles**: International Color Consortium; device profiles describe device's color behavior (input profile for scanner/camera, output profile for printer/display); color management system (CMS) converts between profiles; rendering intents determine how out-of-gamut colors are handled: Perceptual (compress all colors, preserve relationships — good for photos), Relative Colorimetric (clips out-of-gamut, maps white points — good for spot colors), Saturation (maximizes saturation — good for graphics), Absolute Colorimetric (exact match, no white point adjustment)
- **White balance**: cameras record scene as-lit; sensor doesn't know what's "white"; white balance adjusts for light source color temperature (tungsten ≈ 2850K, fluorescent ≈ 4000K, daylight ≈ 5500K, cloudy ≈ 6500K); incorrect WB = color cast; RAW files preserve original data + WB setting that can be changed in post; JPEG applies WB destructively
- **HDR (High Dynamic Range)**: extends luminance range beyond SDR (standard dynamic range, ~100 nits max); HDR10 (static metadata, 10-bit, Rec.2020, 1000 nits), HDR10+ (dynamic metadata), Dolby Vision (12-bit, up to 10,000 nits); PQ (Perceptual Quantizer) and HLG (Hybrid Log-Gamma) transfer functions replace gamma for HDR; tone mapping converts HDR content for SDR displays (and vice versa)
- **Color in CSS/web**: hex (#RRGGBB), rgb()/rgba(), hsl()/hsla() (hue/saturation/lightness — more intuitive for manipulation), hwb() (hue/whiteness/blackness), oklch() (modern perceptual uniform space), color() function for wider gamuts; P3 colors in CSS: `color(display-p3 1 0 0)` = P3 red; CSS Color Level 4 brings full HDR and wide-gamut support
- **Color in 3D rendering and compositing**: physically based rendering (PBR) requires linear light; texture authoring in gamma → must linearize before lighting calculations; metallic/roughness workflow (Disney principled BSDF); spectral rendering vs RGB rendering (spectral more accurate for complex light interactions like fluorescence, dispersion); EXR format (32-bit float, HDR, standard for VFX)
