# SVG Map Prototype — Florida

## Test 1: Minimal monochrome schematic

<svg viewBox="-90 24 16 8" width="800" height="400" xmlns="http://www.w3.org/2000/svg" style="background:#fff; font-family: 'EB Garamond', Georgia, serif;">

  <!-- Grid lines (light) -->
  <line x1="-90" y1="25" x2="-74" y2="25" stroke="#ddd" stroke-width="0.02"/>
  <line x1="-90" y1="27" x2="-74" y2="27" stroke="#ddd" stroke-width="0.02"/>
  <line x1="-90" y1="29" x2="-74" y2="29" stroke="#ddd" stroke-width="0.02"/>
  <line x1="-90" y1="31" x2="-74" y2="31" stroke="#ddd" stroke-width="0.02"/>
  <line x1="-88" y1="24" x2="-88" y2="32" stroke="#ddd" stroke-width="0.02"/>
  <line x1="-86" y1="24" x2="-86" y2="32" stroke="#ddd" stroke-width="0.02"/>
  <line x1="-84" y1="24" x2="-84" y2="32" stroke="#ddd" stroke-width="0.02"/>
  <line x1="-82" y1="24" x2="-82" y2="32" stroke="#ddd" stroke-width="0.02"/>
  <line x1="-80" y1="24" x2="-80" y2="32" stroke="#ddd" stroke-width="0.02"/>
  <line x1="-78" y1="24" x2="-78" y2="32" stroke="#ddd" stroke-width="0.02"/>
  <line x1="-76" y1="24" x2="-76" y2="32" stroke="#ddd" stroke-width="0.02"/>

  <!-- Gulf of Mexico label -->
  <text x="-89" y="27.5" font-size="0.4" fill="#999" font-style="italic">Gulf of Mexico</text>

  <!-- Atlantic label -->
  <text x="-76.5" y="28" font-size="0.4" fill="#999" font-style="italic">Atlantic</text>

  <!-- Florida outline (simplified) -->
  <path d="M-87.6,30.5 L-85.5,30.3 L-84.8,30.5 L-84.3,30.1 L-83.5,29.8 L-82.5,30
           L-82,29.8 L-81.5,30.3 L-81.3,30.5 L-81.6,31 L-81.5,31.5
           L-80.8,30.8 L-80.5,30.2 L-80.3,29.5 L-80.2,28.5 L-80.1,27.5
           L-80.2,26.5 L-80.4,25.8 L-80.5,25.3 L-81,24.7 L-81.5,24.5
           L-81.8,24.8 L-82,25.2 L-82.2,25.8 L-82.5,26.2 L-82.7,27
           L-82.6,27.8 L-82.8,28.2 L-83,28.8 L-83.5,29.2 L-84,29.5
           L-84.5,29.8 L-85,30 L-85.5,30 L-86,30 L-87,30.2 L-87.6,30.5 Z"
        fill="#e8e4dc" stroke="#333" stroke-width="0.05" />

  <!-- Panhandle extension west -->
  <path d="M-87.6,30.5 L-88,30.4 L-88.5,30.3 L-89,30.4 L-89.5,30.3"
        fill="none" stroke="#333" stroke-width="0.05" />

  <!-- Georgia / Alabama coastline (north context) -->
  <path d="M-81.5,31.5 L-81.2,31.2 L-80.8,31.5 L-80.5,31.8 L-80,32 L-79.5,31.8"
        fill="none" stroke="#999" stroke-width="0.03" stroke-dasharray="0.1"/>

  <!-- Lake Okeechobee -->
  <ellipse cx="-80.8" cy="26.9" rx="0.3" ry="0.2" fill="#c8dce8" stroke="#666" stroke-width="0.02"/>
  <text x="-80.3" y="27" font-size="0.22" fill="#666">L. Okeechobee</text>

  <!-- Everglades -->
  <text x="-81.2" y="25.8" font-size="0.25" fill="#555" font-style="italic">Everglades</text>

  <!-- Cities -->
  <circle cx="-81.66" cy="30.33" r="0.08" fill="#333"/>
  <text x="-81.5" y="30.2" font-size="0.25" fill="#333">Jacksonville</text>

  <circle cx="-81.38" cy="28.54" r="0.06" fill="#333"/>
  <text x="-81.1" y="28.4" font-size="0.22" fill="#333">Orlando</text>

  <circle cx="-82.46" cy="27.95" r="0.07" fill="#333"/>
  <text x="-82.9" y="27.8" font-size="0.25" fill="#333">Tampa</text>

  <circle cx="-82.53" cy="26.64" r="0.05" fill="#333"/>
  <text x="-82.9" y="26.6" font-size="0.22" fill="#333">Sarasota</text>

  <circle cx="-80.19" cy="25.76" r="0.08" fill="#333"/>
  <text x="-79.9" y="25.6" font-size="0.25" fill="#333">Miami</text>

  <circle cx="-81.78" cy="24.56" r="0.05" fill="#333"/>
  <text x="-81.5" y="24.4" font-size="0.22" fill="#333">Key West</text>

  <circle cx="-82.64" cy="30.44" r="0.06" fill="#333"/>
  <text x="-83.3" y="30.3" font-size="0.22" fill="#333">Tallahassee</text>

  <circle cx="-87.22" cy="30.41" r="0.06" fill="#333"/>
  <text x="-87.8" y="30.2" font-size="0.22" fill="#333">Pensacola</text>

  <circle cx="-80.06" cy="26.72" r="0.06" fill="#333"/>
  <text x="-79.7" y="26.6" font-size="0.22" fill="#333">West Palm</text>

  <!-- Cape Canaveral -->
  <text x="-79.8" y="28.5" font-size="0.2" fill="#555">Cape Canaveral</text>

  <!-- Keys chain (simplified) -->
  <path d="M-81,24.7 L-81.2,24.6 L-81.5,24.55 L-81.8,24.56 L-82,24.6"
        fill="none" stroke="#333" stroke-width="0.03"/>

  <!-- Lat labels -->
  <text x="-74.5" y="25.1" font-size="0.25" fill="#999">25°N</text>
  <text x="-74.5" y="27.1" font-size="0.25" fill="#999">27°N</text>
  <text x="-74.5" y="29.1" font-size="0.25" fill="#999">29°N</text>
  <text x="-74.5" y="31.1" font-size="0.25" fill="#999">31°N</text>

  <!-- Lon labels -->
  <text x="-88.2" y="24.3" font-size="0.25" fill="#999">88°W</text>
  <text x="-86.2" y="24.3" font-size="0.25" fill="#999">86°W</text>
  <text x="-84.2" y="24.3" font-size="0.25" fill="#999">84°W</text>
  <text x="-82.2" y="24.3" font-size="0.25" fill="#999">82°W</text>
  <text x="-80.2" y="24.3" font-size="0.25" fill="#999">80°W</text>
  <text x="-78.2" y="24.3" font-size="0.25" fill="#999">78°W</text>
  <text x="-76.2" y="24.3" font-size="0.25" fill="#999">76°W</text>

  <!-- Scale bar -->
  <line x1="-89" y1="31.8" x2="-87.2" y2="31.8" stroke="#333" stroke-width="0.04"/>
  <line x1="-89" y1="31.7" x2="-89" y2="31.9" stroke="#333" stroke-width="0.04"/>
  <line x1="-87.2" y1="31.7" x2="-87.2" y2="31.9" stroke="#333" stroke-width="0.04"/>
  <text x="-88.5" y="32" font-size="0.22" fill="#333">200 km</text>

</svg>

## Test 2: Dark/minimal — atlas style

<svg viewBox="-90 24 16 8" width="800" height="400" xmlns="http://www.w3.org/2000/svg" style="background:#1a1a1a; font-family: 'EB Garamond', Georgia, serif;">

  <!-- Grid lines -->
  <line x1="-90" y1="25" x2="-74" y2="25" stroke="#333" stroke-width="0.02"/>
  <line x1="-90" y1="27" x2="-74" y2="27" stroke="#333" stroke-width="0.02"/>
  <line x1="-90" y1="29" x2="-74" y2="29" stroke="#333" stroke-width="0.02"/>
  <line x1="-90" y1="31" x2="-74" y2="31" stroke="#333" stroke-width="0.02"/>
  <line x1="-88" y1="24" x2="-88" y2="32" stroke="#333" stroke-width="0.02"/>
  <line x1="-86" y1="24" x2="-86" y2="32" stroke="#333" stroke-width="0.02"/>
  <line x1="-84" y1="24" x2="-84" y2="32" stroke="#333" stroke-width="0.02"/>
  <line x1="-82" y1="24" x2="-82" y2="32" stroke="#333" stroke-width="0.02"/>
  <line x1="-80" y1="24" x2="-80" y2="32" stroke="#333" stroke-width="0.02"/>
  <line x1="-78" y1="24" x2="-78" y2="32" stroke="#333" stroke-width="0.02"/>
  <line x1="-76" y1="24" x2="-76" y2="32" stroke="#333" stroke-width="0.02"/>

  <!-- Water labels -->
  <text x="-89" y="27.5" font-size="0.4" fill="#445566" font-style="italic">Gulf of Mexico</text>
  <text x="-76.5" y="28" font-size="0.4" fill="#445566" font-style="italic">Atlantic</text>

  <!-- Florida fill -->
  <path d="M-87.6,30.5 L-85.5,30.3 L-84.8,30.5 L-84.3,30.1 L-83.5,29.8 L-82.5,30
           L-82,29.8 L-81.5,30.3 L-81.3,30.5 L-81.6,31 L-81.5,31.5
           L-80.8,30.8 L-80.5,30.2 L-80.3,29.5 L-80.2,28.5 L-80.1,27.5
           L-80.2,26.5 L-80.4,25.8 L-80.5,25.3 L-81,24.7 L-81.5,24.5
           L-81.8,24.8 L-82,25.2 L-82.2,25.8 L-82.5,26.2 L-82.7,27
           L-82.6,27.8 L-82.8,28.2 L-83,28.8 L-83.5,29.2 L-84,29.5
           L-84.5,29.8 L-85,30 L-85.5,30 L-86,30 L-87,30.2 L-87.6,30.5 Z"
        fill="#2a2a28" stroke="#aa9977" stroke-width="0.05" />

  <!-- Panhandle west -->
  <path d="M-87.6,30.5 L-88,30.4 L-88.5,30.3 L-89,30.4 L-89.5,30.3"
        fill="none" stroke="#aa9977" stroke-width="0.05" />

  <!-- Georgia coast context -->
  <path d="M-81.5,31.5 L-81.2,31.2 L-80.8,31.5 L-80.5,31.8 L-80,32 L-79.5,31.8"
        fill="none" stroke="#555" stroke-width="0.03" stroke-dasharray="0.1"/>

  <!-- Lake Okeechobee -->
  <ellipse cx="-80.8" cy="26.9" rx="0.3" ry="0.2" fill="#223344" stroke="#556677" stroke-width="0.02"/>
  <text x="-80.3" y="27" font-size="0.22" fill="#778899">L. Okeechobee</text>

  <!-- Everglades -->
  <text x="-81.2" y="25.8" font-size="0.25" fill="#667755" font-style="italic">Everglades</text>

  <!-- Cities -->
  <circle cx="-81.66" cy="30.33" r="0.08" fill="#aa9977"/>
  <text x="-81.5" y="30.15" font-size="0.25" fill="#ccbbaa">Jacksonville</text>

  <circle cx="-81.38" cy="28.54" r="0.06" fill="#aa9977"/>
  <text x="-81.1" y="28.4" font-size="0.22" fill="#ccbbaa">Orlando</text>

  <circle cx="-82.46" cy="27.95" r="0.07" fill="#aa9977"/>
  <text x="-82.9" y="27.8" font-size="0.25" fill="#ccbbaa">Tampa</text>

  <circle cx="-80.19" cy="25.76" r="0.08" fill="#aa9977"/>
  <text x="-79.9" y="25.6" font-size="0.25" fill="#ccbbaa">Miami</text>

  <circle cx="-81.78" cy="24.56" r="0.05" fill="#aa9977"/>
  <text x="-81.5" y="24.4" font-size="0.22" fill="#ccbbaa">Key West</text>

  <circle cx="-82.64" cy="30.44" r="0.06" fill="#aa9977"/>
  <text x="-83.3" y="30.3" font-size="0.22" fill="#ccbbaa">Tallahassee</text>

  <circle cx="-87.22" cy="30.41" r="0.06" fill="#aa9977"/>
  <text x="-87.8" y="30.2" font-size="0.22" fill="#ccbbaa">Pensacola</text>

  <!-- Cape Canaveral -->
  <text x="-79.8" y="28.5" font-size="0.2" fill="#667755">Cape Canaveral</text>

  <!-- Keys -->
  <path d="M-81,24.7 L-81.2,24.6 L-81.5,24.55 L-81.8,24.56 L-82,24.6"
        fill="none" stroke="#aa9977" stroke-width="0.03"/>

  <!-- Lat labels -->
  <text x="-74.5" y="25.1" font-size="0.25" fill="#555">25°N</text>
  <text x="-74.5" y="27.1" font-size="0.25" fill="#555">27°N</text>
  <text x="-74.5" y="29.1" font-size="0.25" fill="#555">29°N</text>
  <text x="-74.5" y="31.1" font-size="0.25" fill="#555">31°N</text>

  <!-- Lon labels -->
  <text x="-88.2" y="24.3" font-size="0.25" fill="#555">88°W</text>
  <text x="-86.2" y="24.3" font-size="0.25" fill="#555">86°W</text>
  <text x="-84.2" y="24.3" font-size="0.25" fill="#555">84°W</text>
  <text x="-82.2" y="24.3" font-size="0.25" fill="#555">82°W</text>
  <text x="-80.2" y="24.3" font-size="0.25" fill="#555">80°W</text>
  <text x="-78.2" y="24.3" font-size="0.25" fill="#555">78°W</text>
  <text x="-76.2" y="24.3" font-size="0.25" fill="#555">76°W</text>

  <!-- Scale bar -->
  <line x1="-89" y1="31.8" x2="-87.2" y2="31.8" stroke="#aa9977" stroke-width="0.04"/>
  <line x1="-89" y1="31.7" x2="-89" y2="31.9" stroke="#aa9977" stroke-width="0.04"/>
  <line x1="-87.2" y1="31.7" x2="-87.2" y2="31.9" stroke="#aa9977" stroke-width="0.04"/>
  <text x="-88.5" y="32" font-size="0.22" fill="#aa9977">200 km</text>

</svg>

## Test 3: Line-only — maximum simplicity

<svg viewBox="-90 24 16 8" width="800" height="400" xmlns="http://www.w3.org/2000/svg" style="background:#fff; font-family: monospace;">

  <!-- Florida outline only -->
  <path d="M-87.6,30.5 L-85.5,30.3 L-84.8,30.5 L-84.3,30.1 L-83.5,29.8 L-82.5,30
           L-82,29.8 L-81.5,30.3 L-81.3,30.5 L-81.6,31 L-81.5,31.5
           L-80.8,30.8 L-80.5,30.2 L-80.3,29.5 L-80.2,28.5 L-80.1,27.5
           L-80.2,26.5 L-80.4,25.8 L-80.5,25.3 L-81,24.7 L-81.5,24.5
           L-81.8,24.8 L-82,25.2 L-82.2,25.8 L-82.5,26.2 L-82.7,27
           L-82.6,27.8 L-82.8,28.2 L-83,28.8 L-83.5,29.2 L-84,29.5
           L-84.5,29.8 L-85,30 L-85.5,30 L-86,30 L-87,30.2 L-87.6,30.5 Z"
        fill="none" stroke="#000" stroke-width="0.06" />

  <!-- Panhandle -->
  <path d="M-87.6,30.5 L-88,30.4 L-88.5,30.3 L-89,30.4 L-89.5,30.3"
        fill="none" stroke="#000" stroke-width="0.06" />

  <!-- Keys -->
  <path d="M-81,24.7 L-81.2,24.6 L-81.5,24.55 L-81.8,24.56 L-82,24.6"
        fill="none" stroke="#000" stroke-width="0.04"/>

  <!-- Lake Okeechobee -->
  <ellipse cx="-80.8" cy="26.9" rx="0.3" ry="0.2" fill="none" stroke="#000" stroke-width="0.03"/>

  <!-- Cities as dots + labels -->
  <circle cx="-81.66" cy="30.33" r="0.07" fill="#000"/>
  <text x="-81.45" y="30.2" font-size="0.28" fill="#000">Jacksonville</text>

  <circle cx="-82.46" cy="27.95" r="0.07" fill="#000"/>
  <text x="-83.2" y="27.85" font-size="0.28" fill="#000">Tampa</text>

  <circle cx="-80.19" cy="25.76" r="0.07" fill="#000"/>
  <text x="-79.95" y="25.6" font-size="0.28" fill="#000">Miami</text>

  <circle cx="-81.38" cy="28.54" r="0.05" fill="#000"/>
  <text x="-81.15" y="28.4" font-size="0.24" fill="#000">Orlando</text>

  <circle cx="-82.64" cy="30.44" r="0.05" fill="#000"/>
  <text x="-83.6" y="30.35" font-size="0.24" fill="#000">Tallahassee</text>

  <circle cx="-87.22" cy="30.41" r="0.05" fill="#000"/>
  <text x="-88.2" y="30.3" font-size="0.24" fill="#000">Pensacola</text>

  <circle cx="-81.78" cy="24.56" r="0.05" fill="#000"/>
  <text x="-81.55" y="24.4" font-size="0.24" fill="#000">Key West</text>

  <text x="-81.3" y="25.8" font-size="0.24" fill="#555" font-style="italic">Everglades</text>
  <text x="-80.3" y="27" font-size="0.2" fill="#555">L. Okeechobee</text>
  <text x="-79.8" y="28.5" font-size="0.2" fill="#555">C. Canaveral</text>

  <!-- Scale bar -->
  <line x1="-89" y1="31.5" x2="-87.2" y2="31.5" stroke="#000" stroke-width="0.04"/>
  <line x1="-89" y1="31.4" x2="-89" y2="31.6" stroke="#000" stroke-width="0.04"/>
  <line x1="-87.2" y1="31.4" x2="-87.2" y2="31.6" stroke="#000" stroke-width="0.04"/>
  <text x="-88.5" y="31.8" font-size="0.22" fill="#000">200 km</text>

</svg>

## Notes

- SVG viewBox uses **real lat/lon coordinates** as the coordinate system — no conversion math needed
- The Y axis is inverted (SVG y increases downward, but latitude increases upward) — however since we're using negative longitudes and the viewBox handles it, the map renders correctly if we treat latitude as-is (higher latitude = smaller y value in our coordinate system — the viewBox `"−90 24 16 8"` means start at lon −90, lat 24, span 16° wide × 8° tall)
- All city positions are real coordinates (pulled from USGS)
- Coastline is ~20 control points — enough to be recognizable, not trying to be USGS
- Three styles shown: light/warm, dark/parchment, pure line drawing
- Font is EB Garamond (the MkDocs Material serif font for this site) with monospace fallback
- Each SVG is ~2KB — 52 maps at this density ≈ 100KB total, trivial
