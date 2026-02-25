# Digital Publishing: Desktop Publishing, PostScript, PDF, Ebooks, Print-on-Demand, Open Access

## The Big Picture

Desktop publishing (1985) was the last major technology disruption before the internet. It democratized layout and design the same way GitHub democratized code distribution. Then PDF became the document portability layer. Then ebooks (2007) moved the whole stack into walled gardens. The same platform dynamics as the app store era, applied to books.

```
DIGITAL PUBLISHING STACK

PRE-1985: Professional prepress workflow
  Writer         -> Manuscript (typed)
  Copy editor    -> Marked-up manuscript
  Designer       -> Layout specification
  Typesetter     -> Phototypesetter output (galleys)
  Paste-up artist-> Camera-ready boards
  Camera operator-> Film negatives
  Platemaker     -> Offset printing plates
  Press operator -> Printed sheets
  9 specialized roles -> 1 job with DTP

1985 DESKTOP PUBLISHING REVOLUTION:
  +------------------------+     +---------------------------+
  |  Apple Macintosh 128K  |  +  |  Aldus PageMaker 1.0     |
  |  (Jan 1984)            |     |  (July 1985)              |
  +------------------------+     +---------------------------+
            +                               +
  +------------------------+
  |  Apple LaserWriter     |
  |  (Jan 1985)            |
  |  PostScript engine     |
  +------------------------+
            |
            v
  One person can do typesetting, layout, output
  at ~1/10th the cost of professional prepress

1993: PDF RELEASED
  Document portability across platforms
  Print-quality output independent of local fonts/software

1995-2005: WEB DISRUPTION
  Online publishing without printing at all
  Blogs, wikis, news sites

2007: KINDLE LAUNCH
  eBook reading device + digital content store
  Walled garden: Amazon platform lock-in

2010s: FRAGMENTATION
  Multiple ebook formats (EPUB, MOBI, PDF, AZW3)
  Self-publishing platforms (KDP, Smashwords, Lulu)
  Open access (academic publishing disruption)
  Print-on-demand (POD) infrastructure

2020s: AI CONTENT GENERATION
  LLM-assisted writing, editing, translation
  Automated layout for templated documents
  Next disruption: unclear
```

---

## PostScript: A Programming Language for Pages

PostScript (Adobe Systems, 1984) is the technological foundation of desktop publishing. It is not a file format — it is a programming language.

```
POSTSCRIPT: TURING-COMPLETE PAGE DESCRIPTION

Authors: John Warnock and Chuck Geschke (Adobe Systems, 1982)
Purpose: device-independent page description
Released: 1984 (LaserWriter, January 1985)

WHAT IT IS:
  Turing-complete stack-based programming language
  Influenced by: Forth (stack-based), LISP (interpreted)

  A PostScript file is a PROGRAM that, when executed,
  produces a page. The laser printer runs a PostScript
  interpreter and executes your document as code.

EXAMPLE PostScript (draw a circle):
  72 72 translate        % move origin to 1 inch from corner
  36 0 0 360 arc         % draw arc: center (0,0) radius 36 full circle
  stroke                 % render the path

STACK-BASED EXECUTION:
  PostScript uses reverse Polish notation (like HP calculators, Forth)
  All operations on stack
  "moveto" pops x,y from stack, moves pen
  "lineto" pops x,y, draws line to that point
  Operators: push/pop/manipulate stack

KEY PROPERTIES:
  Device independent: same PostScript renders identically
    on 300 dpi laser printer and 2400 dpi imagesetter
  Resolution independent: all coordinates in points (1/72 inch)
    scaled by printer's resolution at render time
  Font handling: Type 1 fonts = programs that draw letter shapes
    Bézier curves, rendered at any resolution
    Identical on screen (with ATM) and paper

PRINT WORKFLOW WITH POSTSCRIPT:
  Application (PageMaker) generates PostScript code
  -> PostScript file sent to printer
  -> Printer's RIP (Raster Image Processor) executes code
  -> RIP produces bitmap (1-bit per pixel, print resolution)
  -> Printer's engine marks paper from bitmap

WHAT THIS ENABLED:
  Any application that generates PostScript = any printer
  Any printer with PostScript interpreter = any application
  Open standard (published specification)
  Separation of content creation from output device
  Same document: screen display + laser print + imagesetter film
```

---

## Desktop Publishing Revolution (1985)

```
THE SPECIFIC 1985 COMBINATION

Three components required simultaneously:

1. APPLE LASERWRITER (January 1985)
   300 dpi laser printer with built-in PostScript
   Price: $6,995 (~$19,000 in 2024 dollars)
   Processor: Motorola 68000 (same as Mac) running PostScript
   Memory: 1.5 MB (PostScript programs are large)
   Output: 300 dpi = near-typeset quality
   Previously: typeset output required $100,000+ imagesetter

2. ALDUS PAGEMAKER 1.0 (July 1985)
   Developer: Paul Brainerd (Aldus Corporation)
   Platform: Macintosh only
   Concept: WYSIWYG page layout
   Key features: place text + graphics on page,
                 flow text around objects,
                 typographic control (leading, kerning)
   Generates: PostScript for LaserWriter output
   Price: $695 (~$1,900 in 2024 dollars)

3. APPLE MACINTOSH (January 1984)
   GUI with mouse: direct manipulation of layout
   WYSIWYG: What You See Is What You Get
   Bit-mapped display: screen shows actual letter shapes
   Previously: display was ASCII text, print was different
   The Mac's GUI was essential: layout requires spatial thinking
   Command-line interface unusable for page layout

WHAT IT REPLACED:
  Phototypesetting systems: $50,000-500,000 per system
  Operators: required specialized training
  Prepress houses: commercial service bureaus
  Turnaround: days to weeks for typeset output

  With Mac + PageMaker + LaserWriter:
  One person, one machine: layout to output in hours
  Cost: ~$7,000 total vs $500,000+ for equivalent capability

FIRST APPLICATIONS:
  Church newsletters, club bulletins (immediate adopters)
  Small business: letterheads, price lists, catalogs
  "Ransom note aesthetic" early period:
    Too many fonts used badly = typographic chaos
    Desktop publishing democratized design
    AND the ability to produce ugly design at scale

PUBLISHING IMPACT:
  1985: Macintosh World magazine launched (desktop-published)
  1986: John Sculley coined term "desktop publishing"
  1987: QuarkXPress releases (competition to PageMaker)
  1990s: All major magazines and newspapers transition to DTP
  By 1995: virtually no commercial typesetting shops remain
```

---

## PDF — The Portable Document Format

```
PDF: DESIGN GOALS AND ARCHITECTURE

PURPOSE (1991-1993):
  Problem: PostScript files require PostScript interpreter to view
           Cannot be read without printing
           Cannot be searched, annotated, linked
  Problem: documents look different on different systems
           (fonts missing, layout reflows, images different)
  Goal: a document format that:
        - Renders identically on any system
        - Is viewable without specialized equipment
        - Is searchable and navigable
        - Encapsulates all required resources

DEVELOPMENT:
  John Warnock's "Camelot" paper (1991): described the vision
  Adobe Acrobat 1.0: June 1993
  Original: proprietary, expensive ($695 for Acrobat Distiller/Exchange)
  Free Reader: strategy to build installed base
  1993-2008: PDF was proprietary Adobe format
  2008: Adobe publishes PDF as open standard (ISO 32000-1)

PDF TECHNICAL ARCHITECTURE:

  +---------------------------------------------------+
  |  PDF FILE STRUCTURE                               |
  |                                                   |
  |  Header: %PDF-1.7 (version declaration)          |
  |                                                   |
  |  Objects (numbered references):                  |
  |    Pages: content streams for each page          |
  |    Content streams: PostScript-like drawing ops  |
  |    Font objects: embedded font data              |
  |    Image XObjects: compressed image data         |
  |    Annotations: links, comments, form fields     |
  |    Metadata: title, author, keywords             |
  |                                                   |
  |  Cross-reference table:                          |
  |    Maps object numbers to byte offsets           |
  |    Enables random access to pages without        |
  |    reading entire file                           |
  |                                                   |
  |  Trailer: points to cross-reference table        |
  +---------------------------------------------------+

PDF AS BYTECODE ANALOGY:
  PostScript: source code (human-readable programs)
  PDF: bytecode (optimized for delivery and viewing)
  Same relationship as: Java source -> JVM bytecode
  PostScript: general Turing-complete, flexible
  PDF: constrained, page-structured, optimized for viewing

  This is why Adobe Distiller ("compiles" PostScript to PDF)
  and Acrobat Reader ("executes" PDF for display) are the right
  mental model.

PDF VERSIONS AND FEATURES:
  PDF 1.0 (1993): basic text, graphics, images
  PDF 1.2 (1996): hyperlinks, forms, bookmarks
  PDF 1.4 (2001): transparency, metadata
  PDF 1.5 (2003): layers, JBIG2 compression
  PDF 1.6 (2004): 3D objects (U3D), encryption AES
  PDF 1.7 (2006): JavaScript execution, digital signatures
  PDF/A (2005): archival subset (no JavaScript, embedded fonts required)
  PDF/X (2001): print exchange (color management, bleed marks)
  PDF/UA (2012): universal accessibility (tagged structure)
  PDF 2.0 (2017): ISO 32000-2, security improvements
```

---

## Ebooks and the Kindle (2007)

```
EBOOK HISTORY

PRE-KINDLE EBOOK ATTEMPTS:
  Project Gutenberg (1971): Michael Hart, first digital text archive
  eBook readers (1990s): multiple attempts
    SoftBook (1998): $600, subscription model
    Rocket eBook (1998): $500, sync via modem
    All failed: too expensive, poor reading experience,
    no content ecosystem, no distribution infrastructure

  Microsoft Reader (2000): LCD screen, bad contrast
  Adobe Acrobat eBooks: PDF-based, no reflow
  Sony Reader (2006): E-ink, first good display, poor store

  Common failure mode: hardware or format without ecosystem
  Analogous to: early smartphone platforms without app stores

KINDLE (Amazon, November 19, 2007):
  Price: $399
  Display: E-ink (Vizplex, 6-inch, 800x600)
  Battery: ~1 week
  Connectivity: Whispernet (Sprint EVDO, free 3G for book downloads)
  Store: ~90,000 titles at launch, $9.99 standard price
  Format: Mobipocket/AZW (not open EPUB)

  KEY INSIGHT: Amazon already had the content relationships
               (existing book publisher contracts)
               Amazon already had the billing infrastructure
               Amazon already had the customer relationships
               The device was the interface to an existing platform

  WHAT MADE IT WORK:
  Free wireless at point of purchase (no PC sync required)
  One-click purchase from device
  Sync: start on Kindle, continue on phone (Whispernet sync)
  DRM: AZW format, locked to Amazon ecosystem

KINDLE ECOSYSTEM LOCK-IN:
  Books purchased: tied to Amazon account, AZW format
  Cannot be used in other ecosystems (EPUB readers)
  Amazon controls: format, DRM, pricing, discovery, search
  Publisher gets: ~35% or ~70% of ebook price (two models)
  Amazon keeps: 65% or 30%
  For reference: traditional print royalty = 10-15% of retail

  This is the App Store business model applied to books:
  Platform controls the store, takes significant cut,
  owns the customer relationship, controls discovery.

EBOOK MARKET:
  2010: ~9% of US book sales (ebooks)
  2014: ~23% peak penetration
  2020: ~21% (slight decline; print held on)
  Surprising: print didn't die. Physical books retained significant share.
  Unlike music (CDs -> streaming, mostly complete shift)
  Unlike video (DVD -> streaming, mostly complete shift)

  WHY PRINT SURVIVED:
  - Books are physical artifacts people display, give as gifts
  - Reading experience preference (eye strain, annotation)
  - Textbooks still mostly print (complex layout, annotations)
  - Children's books: illustrations, physical interaction
  - Coffee table books: visual experience
```

---

## Print-on-Demand (POD)

```
PRINT-ON-DEMAND: ECONOMICS AND TECHNOLOGY

TRADITIONAL PRINT ECONOMICS:
  Print run: minimum 500-1,000 copies (setup cost amortization)
  Per-copy cost vs print run size:
    1,000 copies: ~$5-8/copy
    5,000 copies: ~$2-3/copy
    20,000 copies: ~$1-1.50/copy
  Fixed cost: setup, plates, make-ready (~$500-2,000)
  Variable cost: paper, ink, binding, per copy

  This requires: predicting demand, warehousing inventory,
  returns from retailers (publishers eat ~30-40% returns)
  Risk: overprint = pulped inventory; underprint = stock-out

PRINT-ON-DEMAND TECHNOLOGY:
  Digital printing (laser/inkjet, no plates needed)
  Setup cost: near zero (just a file)
  Per-copy cost: ~$3-7 (books, regardless of quantity)
  Economically viable at: 1 copy

  Key technology: Xerox DocuTech (1990), Espresso Book Machine,
  Ingram's Lightning Source (1997), Amazon CreateSpace (2007)

POD WORKFLOW:
  Author or publisher uploads: PDF of interior + cover
  Customer orders 1 copy
  File sent to print facility
  Book printed and bound in ~minutes to hours
  Shipped directly to customer
  Per-copy economics: same at 1 unit as at 10,000 units

BUSINESS MODEL TRANSFORMATION:
  BEFORE POD:
    Publisher invests in print run -> warehouses -> distributes
    Risk: $100,000+ inventory may not sell
    Backlist management: keep inventory for slow-moving titles?

  WITH POD:
    Publisher uploads files -> zero inventory
    Books printed as ordered
    No warehousing, no returns, no inventory risk
    Backlist: every book can stay "in print" forever at no cost

  LONG TAIL ECONOMICS:
  Chris Anderson's "Long Tail" thesis (2004) is POD economics:
    Traditional: only bestsellers profitable (distribution cost)
    POD: every title profitable at any volume (no distribution overhead)
    Cumulative niche sales rival bestseller volume

SELF-PUBLISHING VIA POD:
  Amazon KDP (Kindle Direct Publishing): digital + POD
  IngramSpark: distribution to bookstores + POD
  Blurb, Lulu: consumer self-publishing

  Author receives: 40-70% of sale price (vs 10-15% traditional)
  Publisher provides: editing, marketing, distribution relationships
  Self-publisher provides: those functions themselves
  Trade-off: self-publishing economics better; reach/credibility worse
```

---

## Open Access — Academic Publishing Disruption

```
ACADEMIC PUBLISHING: THE PROBLEM

TRADITIONAL MODEL (1970s-2020s):
  Researcher: does research, funded by public grants
              writes paper, peer-reviews others' papers
              PAYS NOTHING, receives NO PAYMENT
  Journal publisher: collects papers, publishes journal
                     licenses back to universities via subscription
  University: pays $10,000-50,000/year per journal subscription
  Researcher: can only access journals their institution subscribes to

  Key absurdity:
    Public money funds research
    Researchers give content + labor free
    Publishers charge universities for access
    Universities (often publicly funded) pay back for access
    The public that funded research often can't access it

JOURNAL PRICING ESCALATION:
  1986-2016: journal subscription prices rose 6x inflation rate
  Elsevier 2020 profit margin: ~37% (higher than Apple)
  Some top journals: $10,000-50,000/year per subscription
  Total academic journal market: ~$25 billion/year globally

OPEN ACCESS MODELS:

  Gold OA: author pays "Article Processing Charge" (APC)
           $500-5,000 per article
           Article free to read immediately
           Pay-to-publish: can create quality concerns

  Green OA: author deposits preprint in repository
            Final published version in journal (paywalled)
            Preprint (pre-peer review) freely available
            arXiv (physics/math/CS, 1991): most successful
            bioRxiv/medRxiv (biology, 2013): COVID accelerated

  Diamond OA: no author charges, no reader charges
              Publisher is academic institution/community
              Funded by grants, volunteers, societies
              Uncommon but growing

  Preprint revolution:
    COVID-19 (2020): arXiv/bioRxiv model applied to biomedicine
    Results published as preprints weeks before journal peer review
    Benefit: speed (weeks vs 6-18 months)
    Risk: unreviewed science amplified by media

SCI-HUB: PIRACY SOLUTION (2011)
  Alexandra Elbakyan (Kazakhstan)
  Provides: free access to ~85 million academic papers
  Method: credential theft + download + redistribution
  Legal status: illegal in US, UK, EU
  Usage: massive, including in countries with subscriptions
  Publishers' lawsuit damages: $15M+ judgments (unenforced)
  Reality: widely used by researchers at wealthy institutions
           not just developing countries

OPEN ACCESS MANDATES:
  NIH (2022): all NIH-funded research must be OA immediately
  (Previously: 12-month embargo allowed)
  European funder coalition (Plan S, 2018):
  All European public research: immediate OA
  US Federal agencies (2022 OSTP memo): same as NIH

  Trajectory: publicly funded research moving toward
              mandatory open access within 5-10 years
```

---

## Decision Cheat Sheet

| Technology | Year | What It Enabled | Key Limitation |
|-----------|------|-----------------|----------------|
| PostScript | 1984 | Device-independent page description | Requires interpreter; not viewable without printing |
| PageMaker | 1985 | WYSIWYG layout for non-professionals | Mac only initially |
| LaserWriter | 1985 | Desktop quality output at ~$7K | 300 dpi (less than professional) |
| PDF | 1993 | Cross-platform portable documents | Proprietary until 2008 |
| Amazon Kindle | 2007 | Ecosystem for ebook purchase/reading | Proprietary format, walled garden |
| Print-on-demand | 1997+ | Zero-inventory publishing, infinite backlist | Higher per-unit cost than offset |
| Open access | 1991+ | Free research access | Funding model (APC creates pay-to-publish) |
| arXiv | 1991 | Preprint repository, physics/math/CS | Pre-peer-review quality varies |

---

## Common Confusion Points

**"PostScript is the same as PDF."** PostScript is a Turing-complete programming language; PDF is a structured document format. PostScript generates pages by executing code; PDF describes pages as structured data. A PostScript file is smaller and more general; a PDF file contains all resources (fonts embedded) and allows random page access without execution. Acrobat Distiller converts PostScript programs into PDF data structures.

**"EPUB is the standard ebook format."** EPUB is the open standard (maintained by W3C/IDPF). Amazon Kindle does not use EPUB — it uses AZW3 (Kindle Format 8), a proprietary format derived from Mobipocket/EPUB but DRM-locked to Amazon's ecosystem. Kindle does now support side-loaded EPUB via Calibre conversion or directly on newer devices (as of 2022), but purchased content remains in AZW3.

**"Self-publishing is the same as vanity publishing."** Vanity publishing (paying a company to publish your book, retaining little) is different from self-publishing (controlling the entire process through platforms like KDP). Self-publishing via Amazon KDP has produced significant commercial successes. The semantic distinction matters: "self-publishing" = author controls; "vanity publishing" = publisher takes money and control.

**"Open access solves the academic publishing problem."** Gold OA (author-pays APC) transfers cost from subscription model to publication model. APCs are often paid by grants, which are often publicly funded — so the public still pays, just differently. The rent extraction by publishers continues in a different form. Truly transformative solutions (diamond OA, preprint-first) face adoption and quality-certification challenges.

**"PDF/A and regular PDF are interchangeable."** PDF/A is a strict subset designed for long-term archiving. It prohibits: JavaScript execution, encryption, external content references, embedded audio/video, and LZW compression. It requires: embedded fonts, device-independent color (ICC profiles), XMP metadata. A regular PDF often cannot be directly archived as PDF/A without conversion. For legal, government, and archival use, the distinction is critical.
