# 06 — Mixing Theory

## Additive vs Subtractive — RGB Light, CMY Pigment, Why They Differ

> **STUB** — outline only, content to be authored

**Planned coverage:**
- **Additive mixing** (light): start with darkness, add light; red + green + blue light → white; used in screens (each pixel has R/G/B sub-pixels), theatrical lighting, photography (RGB channels); adding primary lights increases luminance; the three primaries are defined by display hardware phosphors/LEDs, not universal
- **Subtractive mixing** (pigments/inks): start with white (paper/canvas), each pigment subtracts wavelengths from reflected light; cyan ink absorbs red, magenta absorbs green, yellow absorbs blue; CMY together → absorbs all visible wavelengths → black (theoretically); used in printing (CMYK), paint mixing; adding pigments decreases luminance
- Why CMY are the subtractive primaries: cyan = blue + green (absorbs red), magenta = red + blue (absorbs green), yellow = red + green (absorbs blue); they are the complements of RGB; mixing any two subtractive primaries produces an additive primary
- **CMYK and printing**: why K (black) in addition to CMY? Because CMY inks aren't pure → their "black" is a muddy brown; K (key/black) provides true black and saves expensive colored ink; halftone printing: dots of CMYK at different sizes and angles create illusion of continuous tone; moiré patterns from screen angle conflicts (traditional: C=15°, M=75°, Y=0°, K=45°)
- **Artist color wheel** (RYB — red/yellow/blue): traditional art school system; based on historical pigment mixing where red + yellow = orange, yellow + blue = green, red + blue = purple; NOT scientifically accurate for light (RGB) or ink (CMY); works approximately for opaque paint mixing because of real-world pigment absorption curves; persists in education; Itten's *The Art of Color* (Bauhaus), Josef Albers
- **Partitive/optical mixing** (pointillism): placing small dots of pure color near each other → eye mixes them at distance; not truly additive (reflected light, not emitted) but approximates it at distance; Seurat and Signac's Neo-Impressionism; color remains more vibrant than physical mixing (physical mixing → subtractive → darker result)
- **Transparency and glazing**: transparent pigment layer over another changes reflected color by absorbing specific wavelengths twice; oil painting glazing technique; different from opaque paint mixing (physical mixture vs optical layering)
- **Gamut**: the range of colors reproducible by a given system; sRGB = ~35% of CIE chromaticity; Display P3 = ~45%; Rec.2020 = ~76%; printing CMYK generally smaller gamut than sRGB for saturated colors; HDR requires wider gamut + higher luminance range; out-of-gamut colors must be mapped ("gamut compression") — different methods preserve different attributes
- **The color of shadows**: shadows from a warm light source → cool-colored shadows (complement of warm = cool); shadows lit by sky → slightly blue (skylight is blue); Impressionist "discovery" that shadows are colored, not just grey; explains purple shadows in Monet and Renoir
