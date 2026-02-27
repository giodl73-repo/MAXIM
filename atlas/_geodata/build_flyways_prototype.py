"""
Build flyways map prototype (Map 08) with:
- Natural Earth coastlines (context tier)
- Major bird flyway routes
- PhyloPic silhouettes positioned along routes
- Whale migration routes
- Monarch butterfly corridor
"""

import re

def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def extract_path_d(svg_content):
    """Extract the first path d attribute from an SVG file."""
    match = re.search(r'<path[^>]*\bd="([^"]*)"', svg_content)
    return match.group(1) if match else ""

def extract_viewbox(svg_content):
    """Extract viewBox dimensions."""
    match = re.search(r'viewBox="([^"]*)"', svg_content)
    if match:
        parts = match.group(1).split()
        return [float(x) for x in parts]
    return [0, 0, 100, 100]

def make_silhouette_symbol(svg_file, symbol_id, size=6):
    """Create an SVG <symbol> from a PhyloPic silhouette, normalized to a bounding box."""
    content = read_file(svg_file)
    path_d = extract_path_d(content)
    vb = extract_viewbox(content)
    vb_str = f"{vb[0]} {vb[1]} {vb[2]} {vb[3]}"
    return f'  <symbol id="{symbol_id}" viewBox="{vb_str}">\n    <path d="{path_d}"/>\n  </symbol>'


# Load coastlines
CONTEXT = read_file('world_context_int.svg')

# Build silhouette symbols
symbols = []
symbols.append(make_silhouette_symbol('silhouettes/barnacle_goose.svg', 'goose'))
symbols.append(make_silhouette_symbol('silhouettes/humpback_whale.svg', 'whale'))
symbols.append(make_silhouette_symbol('silhouettes/monarch_butterfly.svg', 'monarch'))
symbols.append(make_silhouette_symbol('silhouettes/black_tern.svg', 'tern'))
symbols.append(make_silhouette_symbol('silhouettes/bar-tailed_godwit.svg', 'godwit'))

symbols_block = "\n".join(symbols)

html = f'''<!DOCTYPE html>
<html><head><title>Atlas Prototype — Map 08 Flyways & Migration</title>
<style>
body{{margin:40px;font-family:Georgia,serif;max-width:1200px;color:#333}}
h1{{border-bottom:2px solid #444;padding-bottom:8px}}
h2{{margin-top:40px;border-bottom:1px solid #ccc;padding-bottom:6px}}
svg{{display:block;margin:20px 0}}
p{{line-height:1.6;max-width:80ch}}
.note{{color:#888;font-size:14px;font-style:italic}}
</style>
</head><body>
<h1>08 — Flyways & Migration Routes (Prototype)</h1>
<p><em>2♥ The Collector — paths of the living world.</em></p>
<p class="note">Natural Earth coastlines + PhyloPic silhouettes + hand-drawn flyway routes.</p>

<h2>Major Bird Flyways</h2>
<p>Eight major flyways funnel billions of birds between breeding and wintering grounds each year.
The routes follow coastlines, river valleys, and mountain passes — the same corridors humans use.</p>

<svg viewBox="-185 -90 370 180" width="960" height="480" xmlns="http://www.w3.org/2000/svg" style="background:#faf8f5; font-family: Georgia, serif;">

  <!-- Silhouette symbol definitions -->
  <defs>
{symbols_block}
  </defs>

  <!-- Grid -->
  <line x1="-180" y1="0" x2="180" y2="0" stroke="#e0ddd8" stroke-width="0.3"/>
  <line x1="-180" y1="-30" x2="180" y2="-30" stroke="#e0ddd8" stroke-width="0.2"/>
  <line x1="-180" y1="30" x2="180" y2="30" stroke="#e0ddd8" stroke-width="0.2"/>
  <line x1="-180" y1="-60" x2="180" y2="-60" stroke="#e0ddd8" stroke-width="0.2"/>
  <line x1="-180" y1="60" x2="180" y2="60" stroke="#e0ddd8" stroke-width="0.2"/>

  <!-- Lat/lon labels -->
  <text x="182" y="2" font-size="2.5" fill="#aaa">0°</text>
  <text x="182" y="-28" font-size="2.5" fill="#aaa">30°N</text>
  <text x="182" y="32" font-size="2.5" fill="#aaa">30°S</text>
  <text x="182" y="-58" font-size="2.5" fill="#aaa">60°N</text>

  <!-- Natural Earth coastlines -->
{CONTEXT}

  <!-- FLYWAY ROUTES — colored curves -->

  <!-- 1. Atlantic Americas Flyway (Arctic Canada → Tierra del Fuego) — blue -->
  <path d="M-75,-70 L-72,-60 L-68,-50 L-70,-40 L-75,-30 L-78,-20
           L-75,-10 L-70,0 L-65,10 L-60,20 L-55,30 L-58,40 L-65,50"
        fill="none" stroke="#3070b0" stroke-width="1.2" stroke-dasharray="3,1.5"
        marker-end="url(#arrowBlue)"/>
  <text x="-62" y="-45" font-size="2.5" fill="#3070b0" font-weight="bold">Atlantic</text>
  <text x="-62" y="-42" font-size="2.5" fill="#3070b0" font-weight="bold">Americas</text>

  <!-- 2. Mississippi Flyway (Hudson Bay → Gulf of Mexico) — blue -->
  <path d="M-90,-60 L-92,-50 L-93,-40 L-92,-30 L-88,-25 L-85,-20"
        fill="none" stroke="#3070b0" stroke-width="1.0" stroke-dasharray="2,1"/>
  <text x="-98" y="-35" font-size="2" fill="#3070b0">Mississippi</text>

  <!-- 3. Pacific Americas Flyway (Alaska → Patagonia) — teal -->
  <path d="M-155,-62 L-140,-55 L-128,-45 L-122,-35 L-118,-25
           L-110,-15 L-105,-5 L-95,5 L-85,15 L-78,25 L-72,35"
        fill="none" stroke="#308080" stroke-width="1.0" stroke-dasharray="2,1"/>
  <text x="-140" y="-48" font-size="2" fill="#308080">Pacific Americas</text>

  <!-- 4. East Atlantic Flyway (Scandinavia → W Africa) — green -->
  <path d="M10,-70 L5,-60 L0,-50 L-5,-40 L-8,-30 L-10,-20
           L-12,-10 L-10,0 L-5,10 L0,20 L5,30"
        fill="none" stroke="#408040" stroke-width="1.2" stroke-dasharray="3,1.5"/>
  <text x="12" y="-50" font-size="2.5" fill="#408040" font-weight="bold">East</text>
  <text x="12" y="-47" font-size="2.5" fill="#408040" font-weight="bold">Atlantic</text>

  <!-- 5. Central Asian Flyway (Siberia → India) — orange -->
  <path d="M70,-65 L68,-55 L65,-45 L62,-35 L65,-28 L70,-22
           L75,-15 L78,-10 L80,-5 L82,0"
        fill="none" stroke="#c07030" stroke-width="1.2" stroke-dasharray="3,1.5"/>
  <text x="55" y="-50" font-size="2.5" fill="#c07030" font-weight="bold">Central</text>
  <text x="55" y="-47" font-size="2.5" fill="#c07030" font-weight="bold">Asian</text>

  <!-- 6. East Asian-Australasian Flyway (Siberia → Australia/NZ) — red -->
  <path d="M120,-65 L125,-55 L128,-45 L130,-35 L128,-25
           L125,-15 L120,-5 L115,5 L118,15 L125,25 L135,35"
        fill="none" stroke="#b04040" stroke-width="1.2" stroke-dasharray="3,1.5"/>
  <text x="132" y="-40" font-size="2.5" fill="#b04040" font-weight="bold">East Asian-</text>
  <text x="132" y="-37" font-size="2.5" fill="#b04040" font-weight="bold">Australasian</text>

  <!-- 7. West Pacific Flyway (Japan/Korea extension) -->
  <path d="M140,-50 L138,-40 L135,-30 L130,-20 L125,-10"
        fill="none" stroke="#b04040" stroke-width="0.8" stroke-dasharray="2,1"/>

  <!-- 8. African-Eurasian Flyway (N Europe → Sub-Saharan) — green -->
  <path d="M25,-60 L28,-50 L30,-40 L32,-30 L35,-20
           L36,-10 L35,0 L33,10 L30,20"
        fill="none" stroke="#408040" stroke-width="1.0" stroke-dasharray="2,1"/>
  <text x="36" y="-35" font-size="2" fill="#408040">African-Eurasian</text>

  <!-- WHALE MIGRATION — dashed blue-gray -->
  <!-- Humpback: Antarctic → tropics -->
  <path d="M-70,58 L-72,45 L-75,30 L-70,18 L-62,10 L-55,5"
        fill="none" stroke="#607090" stroke-width="1.0" stroke-dasharray="4,2"/>
  <text x="-80" y="50" font-size="2" fill="#607090" font-style="italic">Humpback whale</text>
  <text x="-80" y="53" font-size="1.8" fill="#607090">Antarctic → tropics</text>

  <!-- Gray whale: Alaska → Baja -->
  <path d="M-165,-58 L-145,-50 L-130,-42 L-120,-35 L-115,-28"
        fill="none" stroke="#607090" stroke-width="0.8" stroke-dasharray="3,2"/>
  <text x="-152" y="-42" font-size="1.8" fill="#607090" font-style="italic">Gray whale</text>

  <!-- MONARCH BUTTERFLY — orange dotted -->
  <path d="M-100,-45 L-98,-38 L-97,-30 L-100,-22 L-103,-18"
        fill="none" stroke="#d08020" stroke-width="0.8" stroke-dasharray="1,1"/>
  <text x="-105" y="-40" font-size="1.8" fill="#d08020">Monarch</text>
  <text x="-105" y="-37" font-size="1.6" fill="#d08020">butterfly</text>

  <!-- SILHOUETTE MARKERS — positioned along flyway routes -->
  <!-- Goose on East Atlantic flyway -->
  <use href="#goose" x="-2" y="-42" width="6" height="6" fill="#408040" opacity="0.7"/>

  <!-- Tern on Atlantic Americas flyway -->
  <use href="#tern" x="-72" y="-30" width="5" height="5" fill="#3070b0" opacity="0.7"/>

  <!-- Godwit on East Asian-Australasian flyway -->
  <use href="#godwit" x="122" y="-20" width="5" height="5" fill="#b04040" opacity="0.7"/>

  <!-- Whale in South Atlantic -->
  <use href="#whale" x="-67" y="28" width="7" height="7" fill="#607090" opacity="0.6"/>

  <!-- Monarch in Central America -->
  <use href="#monarch" x="-104" y="-25" width="4" height="4" fill="#d08020" opacity="0.7"/>

  <!-- Goose on Central Asian flyway -->
  <use href="#goose" x="67" y="-35" width="5" height="5" fill="#c07030" opacity="0.7"/>

  <!-- Legend -->
  <rect x="-178" y="62" width="55" height="22" fill="#faf8f5" stroke="#ddd" stroke-width="0.3" rx="1"/>
  <line x1="-175" y1="66" x2="-165" y2="66" stroke="#3070b0" stroke-width="1.0" stroke-dasharray="3,1.5"/>
  <text x="-163" y="67" font-size="2" fill="#444">Bird flyway (Americas)</text>
  <line x1="-175" y1="70" x2="-165" y2="70" stroke="#408040" stroke-width="1.0" stroke-dasharray="3,1.5"/>
  <text x="-163" y="71" font-size="2" fill="#444">Bird flyway (Africa-Eurasia)</text>
  <line x1="-175" y1="74" x2="-165" y2="74" stroke="#c07030" stroke-width="1.0" stroke-dasharray="3,1.5"/>
  <text x="-163" y="75" font-size="2" fill="#444">Bird flyway (Central Asian)</text>
  <line x1="-175" y1="78" x2="-165" y2="78" stroke="#b04040" stroke-width="1.0" stroke-dasharray="3,1.5"/>
  <text x="-163" y="79" font-size="2" fill="#444">Bird flyway (East Asian-Australasian)</text>
  <line x1="-175" y1="82" x2="-165" y2="82" stroke="#607090" stroke-width="1.0" stroke-dasharray="4,2"/>
  <text x="-163" y="83" font-size="2" fill="#444">Whale migration</text>

  <!-- Scale bar -->
  <line x1="140" y1="68" x2="150" y2="68" stroke="#444" stroke-width="0.4"/>
  <line x1="140" y1="67" x2="140" y2="69" stroke="#444" stroke-width="0.3"/>
  <line x1="150" y1="67" x2="150" y2="69" stroke="#444" stroke-width="0.3"/>
  <text x="142" y="72" font-size="2.2" fill="#444">~1,100 km</text>

  <!-- Attribution -->
  <text x="-178" y="88" font-size="1.5" fill="#bbb">Silhouettes: PhyloPic (CC0/CC-BY). Coastlines: Natural Earth (public domain).</text>

</svg>

<h2>Silhouette Credits</h2>
<table border="1" cellpadding="4" style="border-collapse:collapse;font-size:14px">
<tr><th>Organism</th><th>Species</th><th>License</th><th>Source</th></tr>
<tr><td>Goose</td><td><em>Branta leucopsis</em></td><td>CC-BY 4.0</td><td>PhyloPic</td></tr>
<tr><td>Whale</td><td><em>Balaenoptera novaeangliae</em></td><td>CC0</td><td>PhyloPic</td></tr>
<tr><td>Butterfly</td><td><em>Danaus plexippus</em></td><td>CC0</td><td>PhyloPic</td></tr>
<tr><td>Tern</td><td><em>Chlidonias niger</em></td><td>CC0</td><td>PhyloPic</td></tr>
<tr><td>Godwit</td><td><em>Limosa lapponica</em></td><td>CC-BY 3.0</td><td>PhyloPic</td></tr>
</table>

</body></html>
'''

with open('../_prototype_flyways.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Wrote _prototype_flyways.html ({len(html):,} chars)")
