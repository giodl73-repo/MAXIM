# Digital Transition: Screen and Web Design

## The Big Picture

```
+------------------------------------------------------------------+
|              PRINT -> SCREEN: THE TRANSITION (1984-2010)          |
|                                                                  |
|  1984: Macintosh + LaserWriter + Aldus PageMaker                 |
|  1987: PostScript enables screen -> print fidelity               |
|  1991: Tim Berners-Lee: World Wide Web (HTML)                    |
|  1993: NCSA Mosaic: images in browser                            |
|  1996: CSS 1.0 (separation of content and presentation)          |
|  1998: Google; web design matures as discipline                  |
|  2004: Web 2.0 / AJAX / dynamic interfaces                       |
|  2007: iPhone: touchscreen paradigm shift                        |
|  2010: Responsive web design (Marcotte)                          |
|  2010s: Figma, Sketch; design systems; design-to-code pipelines  |
|  2020s: AI-assisted design; variable fonts; CSS Grid; OKLCH      |
+------------------------------------------------------------------+
```

---

## The Desktop Publishing Revolution (1984-1991)

Before 1984, graphic design was physical: paste-up, typesetting machines, stat
cameras, mechanical boards. Type was set by specialist typesetters; designers
laid out physical galleys of type.

```
PRE-DIGITAL PRODUCTION WORKFLOW
---------------------------------

1. Designer creates comp (marker sketch, tissue overlay)
2. Typesetter sets type on phototype machine
3. Type output (bromide paper) delivered to studio
4. Designer/paste-up artist cuts and positions type
5. Artwork photographed; film negatives made
6. Printer burns plates from film
7. Printing

TIME: 4-6 weeks for a brochure

POST-DESKTOP-PUBLISHING WORKFLOW
----------------------------------

1. Designer lays out in PageMaker / QuarkXPress
2. Fonts embedded via PostScript
3. Laser proof printed in-studio
4. File sent to bureau for film output (imagesetter)
5. Printer burns plates

TIME: 1-2 weeks; client changes in hours not days

IMPACT:
  Jobs consolidated (designer = typesetter = paste-up artist)
  Small design studios viable (no expensive typesetting equipment)
  Type quality initially dropped (desktop fonts vs. professional)
  Speed advantage transformed client expectations forever
```

---

## PostScript: The Technical Foundation

```
POSTSCRIPT (Adobe, 1985)
  A programming language describing pages in device-independent terms.

  Key properties:
  - Resolution independent: same file, 300dpi or 2400dpi imagesetter
  - Fonts as mathematical descriptions (Type 1), not bitmaps
  - Page description = program; can be reinterpreted at any output device

  BEFORE POSTSCRIPT: screen and print were different worlds
  AFTER POSTSCRIPT:  WYSIWYG (What You See Is What You Get) becomes real

  Technical note: PostScript = stack-based programming language.
  Moving to TrueType (Apple, 1991) then OpenType (Adobe/Microsoft, 1996)
  -- OpenType = TrueType container + PostScript or TrueType outlines
  -- OpenType variable fonts (2016) = a single file, interpolated design space

TRUETYPE vs TYPE 1 vs OPENTYPE
  Type 1: PostScript curves (cubic bezier), 256 glyphs max, two files
  TrueType: Quadratic bezier, one file, cross-platform
  OpenType: Unifies both; unlimited glyphs; Unicode; one file
  Variable: OpenType with multiple design axes
```

---

## The Web as Design Medium

### HTML and the Document Paradigm

```
TIM BERNERS-LEE'S WEB (1991)
  Designed for: sharing scientific documents at CERN
  Format: HTML (HyperText Markup Language) = structured text
  Model: documents with links
  NO DESIGN INTENT: Browsers were free to display as they chose

THE PROBLEM FOR DESIGNERS:
  Designers want control over appearance.
  HTML said: here is the content structure.
  Browsers said: I'll decide how to display it.

  Designers wanted: "put this text here, in this font, this size"
  HTML said: "this is a heading; this is a paragraph"

EARLY WEB "DESIGN" HACKS (1993-1996)
  <TABLE> for layout (not intended for layout)
  <FONT> tags with color/size (inline presentation in content)
  Spacer GIFs: 1px transparent image stretched to push things
  Fixed-width: 640px then 760px then 1024px (monitor assumption)
```

### CSS: Separation of Concerns

```
CSS 1.0 (1996) THESIS:
  Separate CONTENT (HTML) from PRESENTATION (CSS)

  HTML: <h1>Title</h1>
  CSS:  h1 { font-size: 48px; color: #000; }

  Designer controls appearance in one place (the stylesheet)
  Content remains semantically clean

CSS EVOLUTION
  CSS 1 (1996): basics -- color, font, margin, padding
  CSS 2 (1998): positioning, z-index, media types
  CSS 2.1 (2004): fixed / clarified the messy parts
  CSS 3 (2011+): modular; each feature its own spec
    Border-radius, shadows, transitions, animations,
    media queries, web fonts (@font-face), flexbox
  CSS Grid (2017): first real 2D layout system
  CSS Custom Properties (2015+): variables
  CSS color level 4 (2023): OKLCH, Display P3, etc.
```

---

## Screen-Specific Design Challenges

```
PRINT vs SCREEN: WHAT CHANGES
-------------------------------

RESOLUTION
  Print: 300+ DPI; hairline serifs visible
  Screen early: 72 DPI; hinted bitmaps required
  Screen modern: 96-400+ PPI (Retina); vector quality restored

VIEWPORT SIZE
  Print: fixed page; design controls every mm
  Screen: variable; 320px phone to 3840px 4K monitor

COLOR GAMUT
  Print: CMYK; some colors unrepresentable
  Screen early: sRGB; saturated but contained
  Screen modern: Display P3 (wide gamut); more saturated than print

INTERACTIVITY
  Print: static; one-time design decision
  Screen: hover, click, tap, keyboard, scroll; states matter
  A button has: default, hover, active, focused, disabled states

CONTENT VARIABILITY
  Print: exact content known at design time
  Web: user data; variable text lengths; unknown images
  Design must handle: "short name" and "very long name indeed"

LOADING / TIME
  Print: instant (page is there)
  Web: requests, latency, progressive rendering
  Design must handle: loading states, skeleton screens, errors
```

---

## Key Screen Design Paradigms

### Responsive Web Design (2010)

```
ETHAN MARCOTTE, "RESPONSIVE WEB DESIGN" (A LIST APART, 2010)

THREE INGREDIENTS:
  1. Fluid grids (proportional widths, not fixed pixels)
  2. Flexible images (max-width: 100%)
  3. Media queries (CSS changes at viewport breakpoints)

CSS MEDIA QUERY:
  @media (max-width: 768px) {
    .sidebar { display: none; }
    .main { width: 100%; }
  }

BREAKPOINTS (typical):
  Mobile:  < 768px   (phones)
  Tablet:  768-1024px
  Desktop: > 1024px
  Wide:    > 1440px

BEFORE THIS: Mobile web was a separate site (m.example.com)
             2x design and maintenance cost
AFTER THIS:  One design, one codebase, all screen sizes
             "Mobile first" (start with smallest, add complexity)
```

### Flat Design and Material Design

```
SKEUOMORPHISM (pre-2012)
  UI elements simulate physical objects
  Buttons look like physical buttons (raised, lit from top-left)
  Notebooks look like leather-bound books
  Calendar looks like paper calendar

  Apple iOS 1-6: heavy skeuomorphism

  PROBLEM: Inconsistency, visual noise, cultural translation issues

FLAT DESIGN (2012)
  Windows Phone "Metro" (2010) was early; iOS 7 (2013) popularized
  Remove all simulated depth, texture, gradients
  Pure color, minimal or no shadow
  Typography-forward

  OVERCORRECTION: Icons and UI elements lost affordance cues
  (Is this clickable? Is this a button?)

MATERIAL DESIGN (Google, 2014)
  Middle ground: flat but with elevation metaphor
  Surfaces at different z-heights cast real (but computed) shadows
  Motion conveys causality (tap here -> thing comes from here)
  Systematic: 8px baseline grid, defined elevations, defined typography

APPLE HUMAN INTERFACE GUIDELINES (HIG)
  Parallel system for iOS/macOS
  Different philosophy: translucency, depth, organic motion
  Both: systematic; both: visual design grounded in interaction model
```

---

## The UX/UI Convergence

Graphic designers doing screen work became UX/UI designers. The fields merged:

```
GRAPHIC DESIGNER SKILLS         UI DESIGNER ADDITIONAL SKILLS
-----------------------         ------------------------------
Typography                      Interaction states (hover, active)
Color theory                    Information architecture
Grid / layout                   User flows and journeys
Visual hierarchy                Prototyping (Figma / Framer)
                                 Accessibility (WCAG)
                                 Design systems / tokens
                                 Responsive behavior
                                 Handoff to engineers
                                 Usability principles

UX DESIGNER ADDITIONAL SKILLS (vs UI)
  User research (interviews, surveys, usability testing)
  Journey mapping
  Information architecture
  Wireframing (structure without visual design)
  A/B testing interpretation

FIGMA (2016+)
  First truly cloud-native design tool
  Real-time collaboration (think Google Docs for design)
  Components, auto-layout, variants, variables
  Prototype mode (interactions, transitions)
  Dev mode (inspect, extract CSS, design tokens)
  Replaced: Sketch (single-user), Adobe XD (killed 2023)
```

---

## Design-to-Code Pipeline (Modern)

```
DESIGN SYSTEM AS SINGLE SOURCE OF TRUTH
-----------------------------------------

FIGMA                       CODEBASE
------                      --------
Color styles    ----------> CSS custom properties / Tokens
Text styles     ----------> Typography utility classes
Components      ----------> React/Vue/Angular components
Spacing system  ----------> Spacing scale (Tailwind, CSS vars)
Motion styles   ----------> CSS transitions / keyframes

DESIGN TOKEN FORMATS:
  Figma Tokens plugin -> tokens.json
  Style Dictionary (Amazon): transforms tokens to platform outputs
  tokens.json -> CSS vars, iOS Swift, Android XML, all from one source

EXAMPLE PIPELINE:
  Designer changes brand blue in Figma token library
  -> Token JSON file updated (in git)
  -> CI/CD runs Style Dictionary
  -> New CSS variables deployed
  -> All products update automatically

THIS IS THE SAME PATTERN as configuration-driven systems:
  Change one source; derived outputs update automatically.
  Same as Azure Data Factory connection strings -> all pipelines.
```

---

## Common Confusion Points

**"Web design is just putting print layouts on screen"** -- Print designers who
tried this in the 1990s-2000s made fixed-width sites that looked like PDFs.
Screen design is genuinely different: variable viewport, interactivity, states,
loading, accessibility, and motion are not bolt-ons, they are core.

**"Figma replaced design"** -- Figma is a tool. The thinking (hierarchy, color,
type, composition) is the design. Figma makes collaboration and handoff faster;
it does not produce good design from bad thinking.

**"Flat design was a trend"** -- Flat design was a corrective reaction to
skeuomorphic excess. The current state (2025) is "neumorphism" and "glassmorphism"
as reactions to flat going too far. These pendulum swings happen; what persists
is functional visual communication.

**"Design tokens are just CSS variables"** -- CSS variables are one output of
design tokens. Design tokens are the source of truth that can generate CSS,
Swift, Android XML, and any other platform-specific format from one definition.

---

## Decision Cheat Sheet

| I want to understand...                         | Key reference                     |
|-------------------------------------------------|-----------------------------------|
| Why we have CSS at all                          | W3C separation of concerns (1996) |
| How responsive design works technically         | Media queries + fluid grids       |
| Why iOS 7 looked so different from iOS 6        | Flat design reaction (2012-2013)  |
| How Material Design differs from Apple HIG      | Elevation/shadow vs. translucency |
| How design systems connect to code              | Design tokens + Style Dictionary  |
| What Figma actually does better than Sketch     | Cloud collab + auto-layout +      |
|                                                 | dev mode + token support          |
| The history of web typography                   | PostScript -> TrueType -> OpenType|
|                                                 | -> Variable fonts                 |
| What a UX designer does vs a UI/graphic designer| Research + IA vs. visual execution|
