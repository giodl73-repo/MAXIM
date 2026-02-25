# Arts & Culture

10 directories · Visual, built, performed, and ludic culture — from pigment on cave walls to game economies

---

## Landscape

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                              ARTS & CULTURE                                         │
└─────────────────────────────────────────────────────────────────────────────────────┘

 VISUAL ARTS                               BUILT FORM
 ┌──────────────────────────┐              ┌───────────────────────────────────────┐
 │       art-history/       │              │        architecture-history/          │
 │  prehistoric → contemp.  │              │  ancient orders → modernism           │
 │  movements · patronage   │◀────────────▶│  styles · materials · key buildings   │
 │  iconography · crit. theory             │  cultural + structural context        │
 └──────────┬───────────────┘              └──────────────┬────────────────────────┘
            │                                             │ principles carried
            │ extends to lens                             ▼ into practice
 ┌──────────▼───────────────┐              ┌───────────────────────────────────────┐
 │       photography/       │              │           architecture/               │
 │  optics · exposure       │              │  design principles · structure        │
 │  darkroom · color theory │              │  program/circulation · enviro systems │
 │  genres · digital        │              │  contemporary practice                │
 │  aesthetics              │              └───────────────────────────────────────┘
 └──────────┬───────────────┘
            │ color is shared substrate
 ┌──────────▼───────────────┐
 │         colors/          │
 │  color physics · vision  │
 │  CIE/sRGB/Munsell        │
 │  naming/culture          │
 │  digital color           │
 └──────────────────────────┘

 PERFORMANCE / TIME ARTS                   REPRESENTATION
 ┌──────────────────────────┐              ┌───────────────────────────────────────┐
 │       music-theory/      │              │            cartography/               │
 │  notation · scales       │              │  projections · thematic mapping       │
 │  harmony · counterpoint  │              │  GIS · historical maps · design       │
 │  form · tuning systems   │              └───────────────────────────────────────┘
 │  20th-c extensions       │
 └──────────────────────────┘
 ┌──────────────────────────┐
 │       watchmaking/       │              LEISURE / CULTURE
 │  horology · escapements  │              ┌──────────────────────────────────────┐
 │  complications           │              │          games-history/              │
 │  Swiss industry          │              │  ancient boards → video games        │
 │  quartz crisis · revival │              │  rules · culture · tech · economics  │
 └──────────────────────────┘              └──────────────────────────────────────┘
                                           ┌──────────────────────────────────────┐
                                           │          sports-history/             │
                                           │  origins · professionalization       │
                                           │  Olympics · labor · performance sci. │
                                           └──────────────────────────────────────┘

 NOTE: typography/ (type as visual form of language) lives in Language & Communication
       but connects here via Bauhaus, Swiss Style, and book-arts traditions
```

---

## Directories

| Directory | Focus | Entry Point | Bridges to |
|-----------|-------|-------------|------------|
| `art-history/` | Chronological survey from prehistoric cave paintings through contemporary art: movements (Renaissance/Baroque/Romanticism/Impressionism/Modernism/Postmodernism), technique evolution, patronage systems (church → court → bourgeoisie → market), iconographic programs, critical theory (formalism, iconology, psychoanalytic, Marxist, feminist, postcolonial), key works in context | `01-PREHISTORIC-ANCIENT.md` — art before texts, starts the timeline | Material Culture for pigment chemistry and what artists actually worked with; History & Ideas for patronage as political economy; `architecture-history/` for the built environment that hosted art |
| `architecture-history/` | Built form across time: Greek orders (Doric/Ionic/Corinthian — proportion systems not just column caps), Roman engineering (concrete, vault, basilica plan), Byzantine/Romanesque/Gothic structural logic, Renaissance humanism in plan, Baroque spatial drama, Neoclassicism as ideology, Arts and Crafts through Modernism (Sullivan, Wright, Mies, Corbusier), Postmodernism as critique | `01-ANCIENT.md` — Greek orders and Roman engineering, establishes structural vocabulary | `architecture/` for the design principles distilled from history; Material Culture `construction-materials/` for what these buildings are physically made of |
| `architecture/` | Design as practiced discipline: parti and program, circulation hierarchy, structural systems (bearing wall/frame/shell/tension), environmental systems (daylighting, natural ventilation, thermal mass), site and context, building codes as design constraint, sustainability frameworks (LEED/Passivhaus), BIM workflow, contemporary computational design | `01-PRINCIPLES.md` — the fundamental design concepts that all other modules apply | `architecture-history/` for historical precedent; Engineering `structural/` for the structural engineering side; `colors/` for material palette decisions |
| `music-theory/` | The formal grammar of Western music: notation system (staff/clef/rhythm tree), scale construction (modes, pentatonic, chromatic, non-Western scales), harmony (triads through extended chords, voice leading, functional harmony), counterpoint (species through free), musical form (binary/ternary/sonata/rondo/theme-and-variations), tuning systems (Pythagorean/meantone/equal temperament — the math of frequency ratios), 20th-century extensions (serialism, set theory, spectralism) | `01-NOTATION.md` — notation and rhythm, the prerequisites for everything else | Mathematics for tuning system mathematics (frequency ratios, equal temperament as 12th root of 2); `watchmaking/` for the shared precision-timekeeping heritage |
| `photography/` | Photography from first principles: optics (lens design, focal length, aperture as solid angle), exposure triangle (aperture/shutter/ISO — photons as quantum events), photochemical process (silver halide, zone system, darkroom), color theory in photography (additive/subtractive, color balance, ICC profiles), genres (documentary, portrait, landscape, street, architectural), digital workflow (RAW pipeline, histogram, color grading), aesthetics (decisive moment, formal composition, conceptual photography) | `01-OPTICS.md` — lens physics, ties to Physics `optics/` directly | `colors/` for color science fundamentals; `art-history/` for photography's contested place in art history; Engineering `optics/` for lens design depth |
| `colors/` | Color as physics, perception, and culture: spectral physics (wavelength, CIE 1931 observer, color matching functions), human vision (trichromacy, opponent channels, metamers, color blindness), color order systems (Munsell, NCS, Pantone), colorimetry (CIE Lab/LCH, Delta-E), color spaces for different workflows (sRGB, Adobe RGB, DCI-P3, Rec. 2020), cultural color naming and symbolism, digital color (bit depth, color management, ICC profiles) | `01-PHYSICS.md` — electromagnetic spectrum through perceptual color, establishes the whole framework | Material Culture `pigments/` for how color is physically produced; `photography/` and Computing for digital color management; `art-history/` for color in art practice |
| `cartography/` | Maps as argument and as technology: the projection problem (all projections lie — which lies matter for which use), thematic mapping (choropleth, isoline, proportional symbol, flow maps), GIS concepts (vector vs. raster, coordinate reference systems, topology), historical cartography (portolan charts, Mercator's agenda, imperial mapping), map design principles (figure/ground, visual hierarchy, generalization), the power-knowledge critique (maps as political objects) | `01-PROJECTIONS.md` — the mathematics of projecting sphere to plane, the foundational problem | Mathematics for projection geometry; History & Ideas for cartography's role in colonialism and statecraft; `art-history/` for decorative cartography as art object |
| `games-history/` | Games from Senet (3100 BCE) through Elden Ring: ancient board games (Go, Chess, Backgammon — origins and rule evolution), card games and probability theory (connection to gambling and early statistics), war games and the origins of tabletop RPGs, pinball through early video games (Spacewar!/Pong/Atari), the arcade era, home console generations (Atari/NES/PlayStation arc), PC gaming, mobile gaming economics, esports, live-service and loot-box economics | `01-ANCIENT-BOARDS.md` — ancient games as social technology, starts the lineage | Mathematics for game-theoretic analysis; Computing for the platform architecture underneath video games; History & Ideas for games as mirrors of their culture |
| `sports-history/` | Sport as institution: amateur origins and their class politics, professionalization (baseball/cricket/football — different paths), the modern Olympics (1896 mythology vs. political reality), globalization of sport (football/soccer as case study), labor economics (reserve clause, free agency, salary caps), doping and the science of performance enhancement, sports science (biomechanics, nutrition, sports psychology), media rights as the financial spine | `01-ORIGINS.md` — pre-modern games through the amateur era, establishes the social framework | History & Ideas for sports as national identity and political instrument; `games-history/` for the ludic continuum; human biology for sports science foundations |
| `watchmaking/` | Precision timekeeping as applied physics and craft: the problem of longitude and why accurate timekeeping mattered (Harrison's H4), escapement mechanics (verge/anchor/lever/co-axial — each a different engineering solution), complications (perpetual calendar, tourbillon, minute repeater — how they work mechanically), the Swiss industry structure (établissage system, valley specialization), the quartz crisis (1970s — a real industry near-extinction event), the mechanical revival (luxury goods economics, collector market), modern haute horlogerie | `01-ESCAPEMENTS.md` — the escapement problem, establishes the core engineering challenge | Engineering `mechanical/` for gear trains and tolerances; Physics for oscillator theory (the pendulum/balance wheel as harmonic oscillator); `art-history/` for the decorative arts tradition of enameling and engraving on watch dials |

---

## Paths

### Visual arts foundation
`colors/` → `art-history/` → `photography/`
*Start with the physics and perception of color — what artists and photographers are actually manipulating — then trace art history with that substrate in mind, then see photography as both a continuation of pictorial art and a technical medium with its own optics.*

### Built environment
`architecture-history/` → `architecture/` → `cartography/`
*Historical precedent grounds the design vocabulary; contemporary practice shows how those principles are applied now; cartography extends spatial thinking to representation at urban and geographic scale.*

### Precision and craft
`watchmaking/` → `music-theory/` → `games-history/`
*Watchmaking and music theory share a deep relationship with time, rhythm, and mechanical precision. Games-history closes the loop on leisure culture and the human impulse to create formal systems with rules — the same impulse behind both musical notation and escapement design.*

---

## Adjacent Sections

| Section | The bridge |
|---------|------------|
| History & Ideas | `art-history/` and `architecture-history/` are inseparable from political and economic history — patronage, propaganda, nationalist iconography, colonial collecting, and the art market are all historical phenomena. `military-history/` connects to art history through the art of war documentation and monumental architecture. |
| Material Culture | `colors/` and `pigments/` are two sides of the same phenomenon — one from the physics/perception side, one from the chemistry/trade side. `architecture/` depends on `construction-materials/` and `glassmaking/`. `art-history/` requires understanding what materials (pigments, canvas, stone, bronze) artists actually worked with. |
| Language & Communication | `cartography/` uses a visual language with its own notation conventions — legend, scale bar, projection note. `typography/` (in Language & Communication) connects here through book arts, poster design, and the Bauhaus synthesis of type and image. |
| Mathematics & Physics | `music-theory/` tuning systems are a direct application of number theory (frequency ratios) and group theory (the octave as a cyclic group). `cartography/` projections require differential geometry. `watchmaking/` escapements are harmonic oscillators. `photography/` optics is applied electromagnetic theory. |
