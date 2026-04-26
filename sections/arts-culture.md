# Arts & Culture

17 directories · Visual, built, performed, and ludic culture — from pigment on cave walls to sequential art and sports science

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
| [`art-history/`](../art-history/00-OVERVIEW.md) | Chronological survey from prehistoric cave paintings through contemporary art: movements (Renaissance/Baroque/Romanticism/Impressionism/Modernism/Postmodernism), technique evolution, patronage systems (church → court → bourgeoisie → market), iconographic programs, critical theory (formalism, iconology, psychoanalytic, Marxist, feminist, postcolonial), key works in context | [`01-PREHISTORIC-ANCIENT.md`](../art-history/01-PREHISTORIC-ANCIENT.md) — art before texts, starts the timeline | Material Culture for pigment chemistry and what artists actually worked with; History & Ideas for patronage as political economy; `architecture-history/` for the built environment that hosted art |
| [`architecture-history/`](../architecture-history/00-OVERVIEW.md) | Built form across time: Greek orders (Doric/Ionic/Corinthian — proportion systems not just column caps), Roman engineering (concrete, vault, basilica plan), Byzantine/Romanesque/Gothic structural logic, Renaissance humanism in plan, Baroque spatial drama, Neoclassicism as ideology, Arts and Crafts through Modernism (Sullivan, Wright, Mies, Corbusier), Postmodernism as critique | [`01-ANCIENT.md`](../architecture-history/01-ANCIENT.md) — Greek orders and Roman engineering, establishes structural vocabulary | `architecture/` for the design principles distilled from history; Material Culture `construction-materials/` for what these buildings are physically made of |
| [`architecture/`](../architecture/00-OVERVIEW.md) | Design as practiced discipline: parti and program, circulation hierarchy, structural systems (bearing wall/frame/shell/tension), environmental systems (daylighting, natural ventilation, thermal mass), site and context, building codes as design constraint, sustainability frameworks (LEED/Passivhaus), BIM workflow, contemporary computational design | [`01-SPATIAL-DESIGN.md`](../architecture/01-SPATIAL-DESIGN.md) — the fundamental design concepts that all other modules apply | `architecture-history/` for historical precedent; Engineering `structural/` for the structural engineering side; `colors/` for material palette decisions |
| [`music-theory/`](../music-theory/00-OVERVIEW.md) | The formal grammar of Western music: notation system (staff/clef/rhythm tree), scale construction (modes, pentatonic, chromatic, non-Western scales), harmony (triads through extended chords, voice leading, functional harmony), counterpoint (species through free), musical form (binary/ternary/sonata/rondo/theme-and-variations), tuning systems (Pythagorean/meantone/equal temperament — the math of frequency ratios), 20th-century extensions (serialism, set theory, spectralism) | [`01-PITCH-SCALES.md`](../music-theory/01-PITCH-SCALES.md) — notation and rhythm, the prerequisites for everything else | Mathematics for tuning system mathematics (frequency ratios, equal temperament as 12th root of 2); `watchmaking/` for the shared precision-timekeeping heritage |
| [`photography/`](../photography/00-OVERVIEW.md) | Photography from first principles: optics (lens design, focal length, aperture as solid angle), exposure triangle (aperture/shutter/ISO — photons as quantum events), photochemical process (silver halide, zone system, darkroom), color theory in photography (additive/subtractive, color balance, ICC profiles), genres (documentary, portrait, landscape, street, architectural), digital workflow (RAW pipeline, histogram, color grading), aesthetics (decisive moment, formal composition, conceptual photography) | [`01-OPTICS-LENSES.md`](../photography/01-OPTICS-LENSES.md) — lens physics, ties to Physics `optics/` directly | `colors/` for color science fundamentals; `art-history/` for photography's contested place in art history; Engineering `optics/` for lens design depth |
| [`colors/`](../colors/00-OVERVIEW.md) | Color as physics, perception, and culture: spectral physics (wavelength, CIE 1931 observer, color matching functions), human vision (trichromacy, opponent channels, metamers, color blindness), color order systems (Munsell, NCS, Pantone), colorimetry (CIE Lab/LCH, Delta-E), color spaces for different workflows (sRGB, Adobe RGB, DCI-P3, Rec. 2020), cultural color naming and symbolism, digital color (bit depth, color management, ICC profiles) | [`01-COLOR-PHYSICS.md`](../colors/01-COLOR-PHYSICS.md) — electromagnetic spectrum through perceptual color, establishes the whole framework | Material Culture `pigments/` for how color is physically produced; `photography/` and Computing for digital color management; `art-history/` for color in art practice |
| [`cartography/`](../cartography/00-OVERVIEW.md) | Maps as argument and as technology: the projection problem (all projections lie — which lies matter for which use), thematic mapping (choropleth, isoline, proportional symbol, flow maps), GIS concepts (vector vs. raster, coordinate reference systems, topology), historical cartography (portolan charts, Mercator's agenda, imperial mapping), map design principles (figure/ground, visual hierarchy, generalization), the power-knowledge critique (maps as political objects) | [`01-ANCIENT-MAPS.md`](../cartography/01-ANCIENT-MAPS.md) — the mathematics of projecting sphere to plane, the foundational problem | Mathematics for projection geometry; History & Ideas for cartography's role in colonialism and statecraft; `art-history/` for decorative cartography as art object |
| [`games-history/`](../games-history/00-OVERVIEW.md) | Games from Senet (3100 BCE) through Elden Ring: ancient board games (Go, Chess, Backgammon — origins and rule evolution), card games and probability theory (connection to gambling and early statistics), war games and the origins of tabletop RPGs, pinball through early video games (Spacewar!/Pong/Atari), the arcade era, home console generations (Atari/NES/PlayStation arc), PC gaming, mobile gaming economics, esports, live-service and loot-box economics | [`01-ANCIENT-GAMES.md`](../games-history/01-ANCIENT-GAMES.md) — ancient games as social technology, starts the lineage | Mathematics for game-theoretic analysis; Computing for the platform architecture underneath video games; History & Ideas for games as mirrors of their culture |
| [`sports-history/`](../sports-history/00-OVERVIEW.md) | Sport as institution: amateur origins and their class politics, professionalization (baseball/cricket/football — different paths), the modern Olympics (1896 mythology vs. political reality), globalization of sport (football/soccer as case study), labor economics (reserve clause, free agency, salary caps), doping and the science of performance enhancement, sports science (biomechanics, nutrition, sports psychology), media rights as the financial spine | [`01-ANCIENT-ATHLETICS.md`](../sports-history/01-ANCIENT-ATHLETICS.md) — pre-modern games through the amateur era, establishes the social framework | History & Ideas for sports as national identity and political instrument; `games-history/` for the ludic continuum; human biology for sports science foundations |
| [`watchmaking/`](../watchmaking/00-OVERVIEW.md) | Precision timekeeping as applied physics and craft: the problem of longitude and why accurate timekeeping mattered (Harrison's H4), escapement mechanics (verge/anchor/lever/co-axial — each a different engineering solution), complications (perpetual calendar, tourbillon, minute repeater — how they work mechanically), the Swiss industry structure (établissage system, valley specialization), the quartz crisis (1970s — a real industry near-extinction event), the mechanical revival (luxury goods economics, collector market), modern haute horlogerie | [`01-EARLY-TIMEKEEPING.md`](../watchmaking/01-EARLY-TIMEKEEPING.md) — the escapement problem, establishes the core engineering challenge | Engineering `mechanical/` for gear trains and tolerances; Physics for oscillator theory (the pendulum/balance wheel as harmonic oscillator); `art-history/` for the decorative arts tradition of enameling and engraving on watch dials |
| [`theater-performance/`](../theater-performance/00-OVERVIEW.md) | Greek origins (Dionysia, tragedy/comedy structure, chorus/masks), Roman and medieval drama (morality plays, commedia dell'arte), Renaissance/Baroque stage (Globe, Spanish golden age, opera origins), modern drama (naturalism/expressionism/absurdism/Brecht), acting theory (Stanislavski through Suzuki), stagecraft (set/lighting/sound history), opera (Baroque through Wagner/contemporary), dance (ballet/modern/world forms), performance studies (Turner/Schechner, ritual and performativity) | [`01-GREEK-ORIGINS.md`](../theater-performance/01-GREEK-ORIGINS.md) — the foundational context before performance theory | `music-theory/` (opera is the intersection); History & Ideas `anthropology/` (ritual and performance overlap); Language & Communication `rhetoric/` (speech act theory and performance studies share theoretical ground) |
| [`dance/`](../dance/00-OVERVIEW.md) | Dance as formal system and cultural practice: ballet (Baroque court origins through Petipa through Balanchine — technique, vocabulary, and the canon), modern dance (Isadora Duncan, Graham, Cunningham — each rejected the previous vocabulary), postmodern dance (Judson Dance Theater — everyday movement as dance, the aesthetic revolution that mirrors conceptual art), world dance forms (Kathak, Butoh, West African, flamenco — each a distinct formal system), Laban movement analysis (Effort/Shape/Space/Body — the notation and taxonomy of movement), choreographic composition (phrase, motif, development, spatial design), dance science (biomechanics of pointe work, injury prevention, motor learning in dance), cultural politics (ballet as European nationalism, dance in liberation movements) | [`01-BALLET.md`](../dance/01-BALLET.md) — ballet as the canonical technical tradition before alternatives | `music-theory/` (rhythm, meter, musical structure — dance and music are inseparable); `theater-performance/` (dance theater overlap in Pina Bausch and others); History & Ideas `anthropology/` (ritual dance in cultural context) |
| [`industrial-design/`](../industrial-design/00-OVERVIEW.md) | Design as the discipline that mediates between engineering constraints and human use: historical movements (Bauhaus synthesis of art and industry, American streamlining as sales strategy, Scandinavian craft humanism, Italian Radical Design), Braun and Dieter Rams (10 principles of good design — the most influential manifesto in the field), Jonathan Ive and Apple (how Rams' principles were applied to consumer electronics at scale), the design process (brief, research, ideation, prototyping, testing — iteration as the methodology), materials and manufacturing constraints in design (DFM — how material choice constrains form), ergonomics and human factors (anthropometrics, cognitive ergonomics, accessibility), interaction design and the product/screen boundary, sustainable design (cradle-to-cradle, circular economy, design for disassembly) | [`01-HISTORY-MOVEMENTS.md`](../industrial-design/01-HISTORY-MOVEMENTS.md) — history before principles, to ground the principles in context | `manufacturing/` (Engineering) for the making side; `architecture/` for the sister discipline; Language & Communication `graphic-design/` for two-dimensional parallel |
| [`graphic-design/`](../graphic-design/00-OVERVIEW.md) | The design of visual communication: Bauhaus visual vocabulary (point, line, plane — Klee and Kandinsky as teachers), Swiss International Style (Josef Müller-Brockmann's grid systems, Helvetica as ideological choice — neutral legibility vs. authorless design), American Modernism (Paul Rand's brand identity thinking, Saul Bass's title sequences, Milton Glaser's Dylan poster), grid systems in depth (modular grid, column grid, Gestalt principles applied to layout), typography in design (type as image, type hierarchy, leading/tracking as design decision not just readability), color in identity (brand color systems, cultural color meanings, color accessibility), brand identity as system design (logo as the smallest unit, the system as the product), digital transition (screen as medium, web design principles, UI as applied graphic design), contemporary tools | [`01-BAUHAUS.md`](../graphic-design/01-BAUHAUS.md) — Bauhaus as the origin of design education | `typography/` (Language & Communication) for type depth; Arts & Culture `art-history/` for the art movements that influenced design; `industrial-design/` for 3D sister discipline |
| [`fashion/`](../fashion/00-OVERVIEW.md) | Dress as economics, culture, and ethics: the haute couture system (how it works — seasonal collections, made-to-measure, loss-leader positioning for ready-to-wear and fragrance), Poiret through Chanel through Dior through Yamamoto and Kawakubo — the history as a sequence of formal innovations, ready-to-wear and its economics (scaling couture ideas to manufacturing), the fashion industry's supply chain (from fiber to fiber — cotton sourcing through garment assembly through retail), fast fashion economics (Zara's vertically integrated response model — 2-week cycle vs. industry 6-month), the Rana Plaza collapse (April 2013, Dhaka — structural failure, 1,134 deaths, the garment industry's accountability moment), sustainability (the environmental math of fashion, circular economy models, dead inventory problem), fashion theory (Veblen's conspicuous consumption, Barthes on the fashion system, gender and dress) | [`01-COUTURE-SYSTEM.md`](../fashion/01-COUTURE-SYSTEM.md) — the haute couture system as the origin of the industry structure | History & Ideas `economic-history/` (textile industrialization as economic history); Material Culture `textiles/` for the fiber and fabric side; `art-history/` for fashion as art |
| [`comics-sequential-art/`](../comics-sequential-art/00-OVERVIEW.md) | The art form of juxtaposed sequential images: McCloud's closure theory (the gutter between panels is where the reader's mind completes the action — the unique mechanism of comics), panel grammar and transitions (moment-to-moment, action-to-action, subject-to-subject, scene-to-scene, aspect-to-aspect, non-sequitur — Eisner and McCloud's taxonomies), American comics history (newspaper strips, Golden Age superheroes, EC horror/crime, Silver Age, underground comix, direct market), the Maus moment (Art Spiegelman winning the Pulitzer in 1992 — legitimating comics as literary form), alternative/art comics (Fantagraphics, L'Association, Drawn & Quarterly), manga as global phenomenon (shōnen/shōjo/seinen/josei demographics, weekly serialization economics, influence on global comics), the graphic novel as commercial and literary form, digital comics and webcomics economics | [`01-HISTORY-FORM.md`](../comics-sequential-art/01-HISTORY-FORM.md) — history before theory; McCloud's theory is better understood with historical examples | Language & Communication `literature/` (comics as literature — shared critical vocabulary); `art-history/` for comics art traditions; Language & Communication `cinema-film/` (storyboarding as shared visual grammar) |
| [`sports-science/`](../sports-science/00-OVERVIEW.md) | The science of human physical performance: exercise physiology foundations (three energy systems: phosphagen/glycolytic/oxidative — and their time domains), VO₂max as the gold standard measure of aerobic capacity (what limits it: cardiac output vs. peripheral extraction), lactate threshold as the practical performance predictor, strength and power (neuromuscular adaptations to resistance training — the neural first then hypertrophic adaptation sequence), biomechanics and movement analysis (ground reaction force, kinematic chain, technique optimization), training theory and periodization (Matveyev's periodization, block periodization, concurrent training interference), sports nutrition and ergogenic aids (carbohydrate loading, caffeine, creatine — the evidence-based ones), doping biochemistry (EPO, anabolic steroids, HGH — mechanisms and detection), sports psychology (self-efficacy, arousal-performance relationship, flow state — Csikszentmihalyi), injury epidemiology and return-to-play | [`01-EXERCISE-PHYSIOLOGY.md`](../sports-science/01-EXERCISE-PHYSIOLOGY.md) — energy systems before performance metrics | Life Sciences `human-biology/` (physiology substrate); `neuroscience/` (motor control, motor learning); History & Ideas `sports-history/` (the history context for the science) |

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
