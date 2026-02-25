# Spatial Design Principles

## The Big Picture

Space is the core medium of architecture. Not walls, not floors, not roofs — the void those elements define. A wall is just a wall; it becomes architecture when it bounds space that humans can inhabit and experience.

```
+--------------------------------------------------------------------+
|                  THE SPATIAL DESIGN STACK                          |
|                                                                    |
|  PHENOMENOLOGY / EXPERIENCE                                        |
|  What it feels like to be in the space                            |
|  Prospect/refuge, compression/release, procession                 |
|                       |                                            |
|  ENVIRONMENTAL PSYCHOLOGY                                          |
|  How humans respond to spatial attributes                          |
|  Crowding, personal space, biophilia, restorative environments     |
|                       |                                            |
|  SPATIAL SEQUENCE                                                  |
|  How spaces connect and transition                                 |
|  Circulation, thresholds, borrowed light                          |
|                       |                                            |
|  PROPORTION SYSTEMS                                                |
|  Rules governing dimensional relationships                         |
|  Golden section, Modulor, classical orders, Ken module             |
|                       |                                            |
|  URBAN LEGIBILITY                                                  |
|  How spaces read at city scale                                     |
|  Lynch imageability: paths/edges/districts/nodes/landmarks         |
|                       |                                            |
|  SPACE PLANNING / PROGRAMMING                                      |
|  Translating requirements into spatial arrangements                |
|  Program → adjacency matrix → bubble diagram → floor plan          |
+--------------------------------------------------------------------+

  Design moves top-down (intent → form) and bottom-up (code/budget → constraints).
  The architect negotiates both directions simultaneously.
```

---

## Space Planning and Programming

### The Programming Sequence

Programming is the pre-design phase that translates client requirements into a spatial brief. Done correctly, it prevents the most expensive class of design errors.

```
  CLIENT REQUIREMENTS               ARCHITECTURAL PROGRAM
  -------------------               ---------------------
  "We need a 500-person office"  →  Area schedule:
  "Teams of 8–12 work together"     - Open office: 14,000 sqft
  "We need focus space"             - Private offices: 2,400 sqft (24 × 100sf)
  "We host external clients"        - Phone rooms: 800 sqft (20 × 40sf)
  "Food is part of our culture"     - Conference (small): 1,200 sqft (6 × 200sf)
                                    - Conference (large): 2,000 sqft (2 × 1,000sf)
                                    - Café / dining: 2,500 sqft
                                    - Lobby / reception: 800 sqft
                                    - Support / storage: 1,500 sqft
                                    - Circulation (35%): ~9,100 sqft
                                    ─────────────────────────────
                                    TOTAL: ~34,300 sqft (net + circ)

  Rule of thumb: add 15–20% for structure/walls/mech to get gross area
  ~34,300 × 1.17 = ~40,000 sqft gross floor area (GFA)
```

### Adjacency Matrix

After the area schedule comes the adjacency matrix: which spaces MUST be near each other, which CANNOT be near each other, and which are neutral.

```
  ADJACENCY MATRIX (sample office)
  ═══════════════════════════════════════════════════════════
                    Lobby  Open   Conf  Café  Exec  Support
                           Office
  ─────────────────────────────────────────────────────────
  Lobby              —      O      ●     O     ●      X
  Open Office        O      —      ●     ●     O      O
  Conference         ●      ●      —     O     O      X
  Café               O      ●      O     —     X      O
  Executive          ●      O      O     X     —      O
  Support            X      O      X     O     O      —
  ─────────────────────────────────────────────────────────
  ● = Must be adjacent / highly desirable
  O = Neutral / acceptable
  X = Must NOT be adjacent (noise, confidentiality, incompatible use)
```

### Bubble Diagram → Block Plan → Floor Plan

```
  STEP 1: BUBBLE DIAGRAM               STEP 2: BLOCK PLAN
  (relationships, no scale)            (scaled zones, still diagrammatic)

    [LOBBY]                              ┌──────────┬──────────┐
       |                                 │  LOBBY   │   EXEC   │
    [OPEN OFFICE]──[CONF]               ├──────────┴──────────┤
       |                                 │                     │
    [CAFÉ]──────[SUPPORT]               │    OPEN OFFICE      │
                                         │                     │
                                         ├──────────┬──────────┤
                                         │   CONF   │  CAFÉ    │
                                         └──────────┴──────────┘

  STEP 3: FLOOR PLAN
  (resolved geometry, structure grid, dimensions, code-compliant egress)
```

---

## Circulation Theory

### The 35% Rule

In most building types, circulation eats 30–40% of gross floor area. This is not waste — it is infrastructure for access, egress, and the spatial experience of moving through a building.

```
  BUILDING TYPE          TYPICAL CIRCULATION %
  ─────────────────────────────────────────────
  Office                 25–35%
  Hospital               40–50% (high circulation intensity)
  Hotel                  30–40%
  Museum                 35–45% (gallery connectors)
  Residential apartment  25–35%
  University teaching    30–40%
  Data center            15–25% (access aisles, service corridors)

  The hospital number explains why hospitals are so expensive per sqft:
  high mechanical intensity + high circulation intensity.
```

### Circulation Hierarchy

```
  PRIMARY CIRCULATION (public, main arteries)
  │  Lobbies, main corridors, atria
  │  Design driver: procession, arrival, wayfinding
  │  Width: 8–12 ft minimum in commercial
  │
  ├── SECONDARY CIRCULATION (departmental)
  │   Internal corridors within zones
  │   Width: 5–8 ft
  │
  └── TERTIARY / SERVICE CIRCULATION
      Back-of-house, service corridors, loading
      Width: 8–10 ft for equipment, carts
      KEY PRINCIPLE: separate service from public
      (cross-contamination is a planning failure)
```

### Path vs Node

Kevin Lynch's framework (from urban design but fully applicable to building interiors):

```
  PATHS                              NODES
  ─────                              ─────
  The routes people travel.          Point features where paths
  Should be legible — a clear        intersect or terminate.
  hierarchy, identifiable            Lobbies, elevator banks,
  character, visual termination.     stairs, reception desks.

  LEGIBLE PATH STRATEGY:             GOOD NODE STRATEGY:
  - Distinguish main from            - Identify nodes at path
    secondary corridors                intersections
  - Provide visual termination       - Make them landmarks
    (art, window, destination)       - Provide orientation cues
  - Avoid identical corridors          (view to outside, art)
    (hotel-corridor effect)
```

### The Promenade Architecturale

Le Corbusier's concept: the building is experienced as a sequence of spaces along a path of movement. The Villa Savoye (1929) is the canonical example — you arrive by car, ramp to entry, ramp through sections to roof garden. Every threshold is choreographed.

```
  PROCESSION SEQUENCE (Baroque and Corbusian both use this):

  APPROACH          ARRIVAL           ASCENT/DESCENT      CLIMAX
  ─────────         ───────           ──────────────      ──────
  Long view of      Entry             Ramp or stair       Principal
  building          compression:      (change of          space:
  (anticipation,    low ceiling,      level creates       Uffizi gallery,
  scale reference)  narrow →          spatial             Villa Savoye
                    release into      punctuation)        living room,
                    lobby                                 cathedral nave

  Compression and release is to architecture what tension and
  resolution is to music. The architect is composing experience in time.
```

---

## Anthropometrics and Human Dimensions

Architecture is a human-scaled discipline. The primary data source is Neufert *Architects' Data* (1936, now in its 4th edition), the bible of dimensional standards.

```
  CRITICAL HUMAN DIMENSIONS
  ==========================

  Standing person:            1,800–1,900mm (5'11"–6'3") tall
  Shoulder width:             500–600mm
  Arm reach (up):             2,100–2,400mm
  Arm reach (horizontal):     750–900mm each side

  WHEELCHAIR (ADA critical dimensions):
  Wheelchair width:           660mm (26")
  Turning radius (360°):      1,525mm (5'-0") diameter clear circle
  Clear passage width:        815mm (32") minimum; 915mm (36") preferred
  Reach range (forward):      380–1,220mm (15"–48") above floor
  Reach range (side):         230–1,370mm (9"–54") above floor

  DOOR CLEARANCES (ADA):
  Clear opening width:        815mm (32") minimum at latch side
  Maneuvering clearance:      varies by approach direction (600–1,525mm)
  Threshold height:           13mm (1/2") maximum

  TABLE / DESK:
  Work surface height:        720–760mm (28"–30")
  Knee clearance below:       660mm (26") height, 750mm (30") depth

  CORRIDOR WIDTHS:
  1 person comfortable:       900mm (3'-0")
  2 persons passing:          1,525mm (5'-0")
  ADA + 1 person:             1,830mm (6'-0")
  Commercial corridor min:    1,500mm (5'-0")
  Hospital corridor (beds):   2,440mm (8'-0") minimum
```

---

## Proportion Systems

Proportion is the discipline of making dimensional relationships feel coherent. These are not magic — they are culturally conditioned responses to harmonic ratios that appear throughout nature and human perception.

### The Golden Section

φ = (1 + √5) / 2 ≈ 1.618

```
  THE GOLDEN RECTANGLE
  ════════════════════

  ┌────────────────────────────────────┬─────────────┐
  │                                    │             │
  │                                    │             │
  │         GOLDEN RECTANGLE          │   SQUARE    │
  │             (φ : 1)               │   (1 : 1)   │
  │                                    │             │
  │                                    │             │
  └────────────────────────────────────┴─────────────┘
  ←──────────────── φ ──────────────────→←── 1 ────→

  Remove the square → what remains is ANOTHER golden rectangle.
  This self-similarity is what makes it feel harmonically "right."

  Fibonacci sequence: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55...
  Ratio of successive terms → φ
  This appears in spiral phyllotaxis, nautilus shells, human body
  proportions — hence Le Corbusier's argument for its use in
  architectural proportion.
```

Applied: facade bay widths, room proportions, window dimensions. The Parthenon's facade fits within a golden rectangle (though the exact proportionality is contested by scholars).

### Le Corbusier's Modulor

The Modulor (1945) is a proportional system based on a 1.83m (6'-0") man — specifically the English detective in novels, who Le Corbusier decided was standard.

```
  THE MODULOR SERIES
  ==================

  Two interleaved series:

  RED SERIES (based on 113 cm navel height):
  ...27, 43, 70, 113, 183, 296, 479...
  Each term = previous × φ (1.618)

  BLUE SERIES (based on 226 cm upward reach):
  ...53, 86, 140, 226, 366, 592...
  Each term = previous × φ (1.618)

  KEY DIMENSIONS:
  183 cm = height of standing man (6'-0")
  226 cm = upward reach (7'-5")
  113 cm = navel height (3'8")
   86 cm = standard table height? (controversial)

  Le Corbusier used this to set: ceiling heights, window sill
  heights, stair dimensions, room proportions in the Unité
  d'Habitation (Marseille, 1952).

  CRITICISM: The system is beautiful as theory. In practice,
  it does not resolve contractor tolerances, structural grids,
  or material module conflicts. Architects use it as a guide,
  not a calculator.
```

### Classical Orders

The five classical orders (Doric, Ionic, Corinthian, Tuscan, Composite) are each proportion systems relating column diameter to entablature height to building height.

```
  COLUMN PROPORTIONS (column height : column diameter)
  ════════════════════════════════════════════════════

  Tuscan:      6:1  (heaviest, simplest)
  Doric:       6–8:1
  Ionic:       8–9:1
  Corinthian:  9–10:1  (most slender)
  Composite:   10:1 (lightest, most ornate)

  The orders encode structural efficiency: slender columns in
  stone require lower loads. The proportions evolved empirically
  from actual stone construction behavior.
```

---

## Spatial Sequences and Experience

### Figure-Ground

Gestalt psychology applied to the urban plan: buildings (solid) as figures against the ground (open space). The Nolli map of Rome (1748) reversed the convention — drew public interior spaces (churches, markets) as white (open), everything else as black. This revealed how much of "indoor" Rome was effectively public.

```
  FIGURE-GROUND ANALYSIS
  ======================

  CONVENTIONAL MAP:              NOLLI READING:
  ┌─────┐ ┌─────┐               ████ ████ ████
  │BLDG │ │BLDG │               ████ ░░░░ ████
  └─────┘ └─────┘               ████ ░░░░ ████
    ░░░░░░░░░░░░                 ████ ████ ████
  ┌─────┐ ┌─────┐
  │BLDG │ │BLDG │
  └─────┘ └─────┘
                                 ░░░░ = publicly accessible
                                        (including interior
                                        public spaces)
  Building mass as figure.       Both inside and outside
  Open space as ground.          public space reads as figure.
```

### Compression and Release

```
  THRESHOLD SEQUENCE DIAGRAM
  ===========================

  EXTERIOR                         INTERIOR
  ────────────────────────────────────────────────────────
  Street      Entry      Lobby     Corridor    Main Space
  ────────────────────────────────────────────────────────

  HEIGHT:  varies → LOW ──→  HIGH ──→  LOW ─────→  HIGH

  WIDTH:   wide ──→ narrow ─→  wide ─→  narrow ──→  wide

  LIGHT:   bright → dim ────→  bright ─→  dim ────→  bright

  EFFECT:  relaxed → compressed → released → compressed → arrived

  The sequence is music. The architect composes it.
  Ignoring it produces dead, disorienting buildings.
```

### Borrowed Light / Borrowed View

Spaces without direct exterior access can receive light and visual connection via:

```
  TECHNIQUES FOR INTERIOR SPACES
  ================================

  Borrowed light:    Glazed partition or clerestory
                     between interior room and
                     exterior-facing corridor/space.
                     ┌──────────────┬──────────────┐
                     │ EXTERIOR     │ INTERIOR     │
                     │ ROOM         │ ROOM         │
                     │    light ──→ │    [glass]   │
                     │  (window)    │    ↑          │
                     └──────────────┴──────────────┘

  Borrowed view:     Interior room with view to
                     atrium or courtyard rather
                     than exterior.

  Light well:        Narrow vertical void through
                     building cross-section.
                     Minimum 1:3 width:height ratio
                     for useful daylighting.
```

---

## Kevin Lynch's Imageability

Lynch's *The Image of the City* (1960) established five elements people use to mentally map urban environments. These apply equally at building and campus scale.

```
  LYNCH'S FIVE ELEMENTS
  ======================

  PATHS         Channels along which people move.
                Roads, walkways, transit lines.
                "I live near the highway / the river walk."

  EDGES         Linear elements that are not paths.
                Boundaries: walls, shores, railroad cuts.
                Can be barriers or seams (depending on permeability).

  DISTRICTS     Medium-large areas with common character.
                "Downtown," "the waterfront," "the medical campus."
                Recognized from inside and referenced from outside.

  NODES         Strategic focal points.
                Junctions, intersections, concentrations.
                "Meet at the fountain," "by the elevator bank."

  LANDMARKS     External point references.
                Usually building or structure.
                Used for orientation, not entry.
                Tall tower, unusual form, distinctive material.

  APPLIED TO A BUILDING INTERIOR:
  ────────────────────────────────
  Paths    →  main corridors, primary circulation routes
  Edges    →  department boundaries, floor-to-floor transitions
  Districts→  zones (clinical, administrative, research)
  Nodes    →  elevator lobbies, reception desks, atrium base
  Landmarks→  art installations, distinctive view windows, stairs
```

---

## Environmental Psychology

### Prospect and Refuge

Jay Appleton's prospect-refuge theory (1975): humans have an evolved preference for environments that offer simultaneous prospect (visual access, ability to survey surroundings) and refuge (shelter, protection from behind).

```
  PROSPECT-REFUGE BALANCE
  ========================

  HIGH PROSPECT /      HIGH PROSPECT /      LOW PROSPECT /
  HIGH REFUGE          LOW REFUGE           HIGH REFUGE
  ─────────────        ──────────────       ──────────────
  Window seat          Open plaza           Cave, bunker
  Bay window nook      Unshaded roof deck   Windowless room

  MOST PREFERRED       Uncomfortable,       Claustrophobic,
  Offers view +        exposed, anxious     oppressive,
  shelter              feeling              disorienting

  DESIGN APPLICATION:
  - Seating alcoves with view to space
  - Low-ceiling zones (refuge) opening to high-ceiling spaces (prospect)
  - Window seats, reading nooks
  - Corner seating preferred in restaurants (both walls = refuge)
  - Openable windows (prospect + some environmental control)
```

### Hall's Proxemics

Edward Hall's *The Hidden Dimension* (1966): cultural anthropology of personal space.

```
  PROXEMIC ZONES (North American culture)
  ═════════════════════════════════════════

  INTIMATE      0 – 18"       Touching to close comfort
                               Reserved for family, close friends

  PERSONAL      18" – 4'      "Arm's length"
                               Conversation with friends, colleagues

  SOCIAL        4' – 12'      Formal interaction
                               Work relationships, consultations

  PUBLIC        12' and beyond Public speaking, performance
                               No personal connection required

  DESIGN IMPLICATIONS:
  ─────────────────────
  Open office: desk spacing of 4–5' keeps workers in social zone
  (productive tension) vs. 6'+ (impersonal) vs. 3' (invasive)

  Conference table width: 36–42" keeps participants in social zone
  Wider tables create public-zone distance — good for formal,
  bad for collaborative.

  Health care: exam room must accommodate physician-patient
  interaction at 3–4' (personal/social boundary) while accommodating
  family seated farther away.
```

### Ulrich's Hospital Study

Roger Ulrich (1984): patients in rooms with window views of nature recovered faster, required less pain medication, and had shorter stays than patients with views of a brick wall. The effect size was large enough to be clinically significant.

This study launched evidence-based design as a discipline and drove adoption of daylit patient rooms, nature views, and biophilic elements in healthcare architecture.

---

## Phenomenological Tradition

### Norberg-Schulz: Genius Loci

Christian Norberg-Schulz (*Genius Loci: Towards a Phenomenology of Architecture*, 1979): every place has a character — "spirit of place" — that architecture should respond to and reinforce rather than override.

The genius loci of a forest clearing is different from a harbor, a desert plateau, an urban street. Architecture that ignores place character feels rootless and alienating.

### Pallasmaa: Haptic Architecture

Juhani Pallasmaa (*The Eyes of the Skin*, 1996): modern architecture privileges vision at the expense of other senses. Great architecture engages touch (material texture, thermal mass warmth), sound (acoustic resonance, footstep sound), smell (cedar, stone, earth), and proprioception (body awareness in space).

The cool stone floor of a Romanesque church is an acoustic, thermal, and tactile experience as much as a visual one.

---

## Decision Cheat Sheet

| Design problem | Spatial design tool | Key principle |
|----------------|---------------------|---------------|
| Client can't articulate spatial needs | Area schedule + adjacency matrix | Translate requirements to spatial brief before design starts |
| Plan feels confusing to navigate | Lynch analysis — paths, nodes, landmarks | Create legible hierarchy; add nodes at decision points |
| Corridor feels oppressive | Compression / release analysis | Check height-to-width ratio; add borrowed light or view windows |
| Interior rooms lack light | Borrowed light / light wells | Glazed partitions, clerestory, min 1:3 well ratio |
| Space feels cold and institutional | Prospect-refuge, proxemics, biophilia | Alcoves, natural materials, views, scale variation |
| Client wants "open" office but staff complain | Proxemics — personal zone violation | Increase inter-desk spacing; add acoustic absorption; provide refuge spaces |
| Circulation consuming too much area | Circulation % audit | Double-loaded corridor vs. single-loaded; combine paths with program |
| Building doesn't feel like "somewhere" | Genius loci response | Reference site character in material, light quality, scale |

---

## Common Confusion Points

**Program is not design**: The architectural program (area schedule + adjacency matrix) is a pre-design document. Writing it does not constrain design — it enables it. Architects who skip programming and go straight to form lose control of the design process when the client's requirements conflict with the emerging design.

**Circulation vs program area**: "Net area" is usable space. "Gross area" includes circulation, structure, and mechanical. Clients always want to know gross area (what they're paying for). Architects track both. The ratio is the efficiency factor — higher is not always better (hospitals need high circulation intensity).

**Golden section is not a rule**: It is a proportional relationship that recurs throughout nature and that human perception tends to find harmonious. It is not magic. Applying it mechanically does not produce good architecture. Understanding why it feels right is more useful than applying it as a formula.

**Modulor criticism**: Le Corbusier's Modulor was criticized extensively — first, by the British, who noted that a 6-foot man is not the universal standard, and second, by any contractor who had to figure out how to build 113 cm modules when material comes in standard metric or imperial sheets. The system works better as a proportional guide than a dimensional standard.

**Lynch at building scale**: Lynch developed his framework for city-scale analysis. It translates directly to buildings and campuses, but the scale shifts the meaning — a "district" in a hospital is a wing, not a neighborhood; a "landmark" is a staircase, not a tower. The framework is structural; the scale is variable.
