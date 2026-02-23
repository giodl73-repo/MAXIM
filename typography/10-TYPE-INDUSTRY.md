# 10 — The Type Industry: Foundries, Licensing, and the Business of Type

## The Big Picture

The type industry is one of the oldest continuously operating software businesses — fonts are intellectual property sold under license. The structural parallels to the software industry are direct: companies sell intangible products, manage IP portfolios through acquisition, deal with piracy, and have gone through the full arc from craft monopolies to commoditization via open source.

```
TYPE INDUSTRY CONSOLIDATION MAP
────────────────────────────────────────────────────────────────────────────────

1450s–1880s  Artisan type foundries  (punch cutters; separate profession)
                    │
1884–1970s   Hot metal era           (Linotype / Monotype duopoly)
             Linotype Co. ─────────────────────────────────────────────────┐
             Monotype Corp ────────────────────────────────────────────────┤
             ATF (American Type Founders) ──────────────────────┐         │
             Stempel ────────────────────────────────┐          │         │
             Bauer ──────────────────────────────────┤          │         │
                    │                                │          │         │
1970s        ITC founded (licensing intermediary)   │          │         │
                    │                                │          │         │
1980s        Adobe (PostScript, Type 1)             │          │         │
             FontShop (FF library)                  │          │         │
             Emigre (digital type revolution)        │          │         │
                    │                                │          │         │
1990s        Monotype digitizes entire library ──────┘          │         │
             Linotype digitizes + merges Stempel ───────────────┘         │
                    │                                                       │
2000s–2010s  CONSOLIDATION:                                                │
             Monotype acquires:                                            │
               - Linotype (2006)  ←─────────────────────────────────────  │
               - ITC (2008)                                                │
               - Bitstream (2012)                                          │
               - FontShop (2014)                                           │
               - Hoefler & Co (2021)                                       │
               - others...                                                 │
             Adobe Fonts (Typekit acquired 2011)                           │
             Google Fonts (2010 — free, open source)                       │
                    │
Current      MONOTYPE GROUP  ← largest commercial type library
             ADOBE FONTS     ← subscription, Creative Cloud bundle
             GOOGLE FONTS    ← free, open-source; largest by usage
             Independent foundries: hundreds (FontBureau, Commercial Type,
               Klim Type, Dinamo, OHno Type, Colophon, Process Type, etc.)

────────────────────────────────────────────────────────────────────────────────
```

---

## The Major Players

### Monotype Group

```
MONOTYPE GROUP — CURRENT STATE
──────────────────────────────────────────────────────────────────────

History:
  Monotype Corporation (1897, UK): hot metal typesetting
  Digitized library 1980s; survived the transition
  Went public; acquired by Bertram Capital (private equity) 2004
  Aggressive acquisition strategy:

Acquisitions:
  2006  Linotype GmbH (Heidelberger Druckmaschinen → Monotype)
        With Linotype: entire Linotype type library + Stempel library
        Includes: Helvetica, Univers, Optima, Palatino, Frutiger
  2008  ITC (International Typeface Corporation)
        With ITC: Avant Garde Gothic, Souvenir, American Typewriter,
        Lubalin Graph, ITC Garamond, large ITC library
  2012  Bitstream
        With Bitstream: Charter (Matthew Carter), Vera fonts, others
  2013  MyFonts (largest retail font marketplace by volume)
  2014  FontShop (FontFont library: FF Meta, FF Scala, FF Dax, FF Beowolf)
        Erik Spiekermann's foundry; key humanist sans library
  2015  Monsen Communications (type technology patents)
  2021  Hoefler & Co
        With H&Co: Gotham, Archer, Hoefler Text, Chronicle, Ideal Sans
        (Gotham = Obama campaign 2008; Barack Obama = Gotham's cultural peak)

Current holdings:
  ~150,000+ font assets
  Libraries: Linotype, Monotype, ITC, Bitstream, FontShop, H&Co
  Operations: licensing (enterprise, desktop, webfont), type technology
  Major revenue: enterprise licensing deals (large companies)

IMPLICATIONS:
  Most "legacy" typefaces trace to Monotype Group
  If you need Helvetica, Univers, Optima, Palatino, Frutiger, FF Meta,
  Gotham, Hoefler Text: you're dealing with Monotype
  Licensing: per user, per CPU, or enterprise deals
──────────────────────────────────────────────────────────────────────
```

### Adobe Fonts

```
ADOBE FONTS (formerly Typekit)
──────────────────────────────────────────────────────────────────────

History:
  Typekit: founded 2008 by Jeffrey Veen + Ryan Carver
  First commercial web font service; subscription model
  Acquired by Adobe: 2011
  Rebranded: Adobe Fonts (2019)
  Integrated into Creative Cloud subscription

Current:
  ~20,000 fonts from major foundries and independent designers
  Included with all Creative Cloud subscriptions (no additional charge)
  Web fonts: delivered via CDN; included in CC subscription

Adobe's own library:
  Adobe Originals: Myriad, Minion, Garamond Premier, Warnock, Trajan,
  Source Sans, Source Serif, Source Code Pro (all open source)
  Collaboration with type designers worldwide

Licensing model:
  Included in Creative Cloud ($55/month for individual)
  Fonts available for desktop + web use within CC subscription
  Not standalone: requires active CC subscription to use web fonts
  (fonts remain active while subscription active; deactivate if cancelled)

NOTABLE ADOBE FONTS:
  Myriad (Twombly/Slimbach, 1992) — Apple used for many years
  Minion (Slimbach, 1990) — excellent Garalde for books
  Garamond Premier Pro (Slimbach, 2005) — finest digital Garamond
  Source Sans Pro (Paul Hunt, 2012) — open source; excellent humanist sans
  Source Serif Pro (Frank Grießhammer, 2014) — open source; book quality
  Source Code Pro (Paul Hunt, 2012) — open source; programming monospace
──────────────────────────────────────────────────────────────────────
```

### Google Fonts

```
GOOGLE FONTS (2010–present)
──────────────────────────────────────────────────────────────────────

Launch: 2010; free web font service
Current: ~1,400+ font families
License: SIL Open Font License (OFL) or Apache 2.0 (majority OFL)
Usage: serves billions of font requests per day

HOW IT CHANGED THE INDUSTRY:
  Before: professional type was expensive; most web text used system fonts
  After: professional-quality free type; web typography democratized
  Result: "use Georgia and Arial" gave way to "use Roboto or Inter"

  Downside for designers:
  - Google pays designers (one-time or ongoing) but rates lower than
    traditional foundry sales → crowded out paid market for similar faces
  - Pressure to release fonts free to be "on Google Fonts"
  - Some designers refuse Google Fonts; others embrace the distribution reach

TECHNICAL IMPLEMENTATION:
  Automatic subsetting by unicode-range:
    Browser requests font URL with text sample
    Google serves only needed glyph subsets (Latin Basic, Latin Extended, etc.)
    Dramatically reduces download size
    The @font-face CSS from Google Fonts includes unicode-range declarations

  CDN delivery:
    Google's CDN; globally distributed; latency-optimized
    Cache headers: fonts cached long-term (365 days)
    GDPR note: Google Fonts logs IP addresses; some EU deployments use
    self-hosted copies to avoid EU data residency issues

  Variable font support:
    Most major Google Fonts now have variable versions
    URL syntax: fonts.googleapis.com/css2?family=Inter:wght@100..900

OFL LICENSE EXPLAINED:
  SIL Open Font License:
    - Free to use for any purpose (personal + commercial)
    - May be bundled with software (e.g., in an app or website)
    - May be modified; modified versions must be released under OFL
    - Cannot be sold standalone (but can be bundled in paid products)
    - Requires attribution only if embedded in document or software
    - Font name cannot be used for modified versions

  Practical upshot:
    Use in web projects: free, no attribution required in most cases
    Bundle in mobile app: allowed under OFL
    Modify and redistribute: allowed; must keep OFL license
    Cannot: charge money specifically for the font files themselves

NOTABLE GOOGLE FONTS:
  Roboto (Christian Robertson, 2011) — default Android font; everywhere
  Lato (Łukasz Dziedzic, 2010) — humanist sans; warm; widely used
  Montserrat (Julieta Ulanovsky, 2012) — geometric sans; display-focused
  Open Sans (Steve Matteson, 2010) — humanist sans; versatile
  Noto (Google, 2013+) — universal coverage; "No Tofu"; all Unicode scripts
  Inter (Rasmus Andersson, 2017) — screen-optimized UI sans; most recommended
  Playfair Display (Claus Eggers Sørensen, 2011) — elegant transitional serif
  Merriweather (Sorkin Type, 2010) — readable screen serif
  EB Garamond (Georg Duffner, 2011) — open source Garamond revival
──────────────────────────────────────────────────────────────────────
```

### Independent Foundries

```
NOTABLE INDEPENDENT FOUNDRIES
──────────────────────────────────────────────────────────────────────

EMIGRE (Berkeley, 1984–2013; type still available)
  Zuzana Licko + Rudy VanderLans
  Early Macintosh digital type pioneers
  Licko designed specifically for the pixel grid of early Macs
  Famous designs: Oakland, Modula, Emigre, Matrix, Mrs Eaves (Licko, 1996
  — named for Sarah Eaves, Baskerville's housekeeper and later wife)
  Mrs Eaves: humanist interpretation of Baskerville; very popular
  Historical significance: first foundry to fully embrace digital type

FONT BUREAU (Boston, David Berlow + Roger Black, 1989)
  Custom typefaces for publications (Rolling Stone, Boston Globe)
  Notable: Benton Sans, Poynter Oldstyle (newspaper serifs)

COMMERCIAL TYPE (New York, 2006)
  Christian Schwartz + Paul Barnes
  High-quality editorial faces
  Notable: Graphik (humanist sans), Guardian Egyptian, Chronicle (H&Co later)

KLIM TYPE FOUNDRY (Wellington, NZ, Kris Sowersby)
  Highly regarded independent; premium quality
  Notable: Tiempos Text, Calibre, Domaine, Söhne
  Söhne: "the memory of Helvetica" — the ideal neo-grotesque for screens

DINAMO (Basel, 2014)
  Contemporary type; experimental and commercial
  Notable: Favorit (clean grotesque), ABC Diatype

OHNO TYPE CO. (James Edmondson, SF)
  Playful, expressive display faces; strong design voice
  Notable: Ohno Blazeface, Bluu Suuperstar

DARDEN STUDIO (Minneapolis, Joshua Darden)
  High-quality text faces
  Notable: Freight (versatile serif family), Halyard (clean humanist sans)

PROCESS TYPE FOUNDRY (Eric Olson, Minneapolis)
  Clean sans-serif work
  Notable: Maple, Trilby

COLOPHON FOUNDRY (London + Los Angeles, 2009)
  International scope; book and screen-focused
  Notable: Aperçu (geometric/humanist hybrid), Reader Pro
──────────────────────────────────────────────────────────────────────
```

---

## Font Licensing Models

```
FONT LICENSING — COMPLETE BREAKDOWN
──────────────────────────────────────────────────────────────────────────────

DESKTOP LICENSE (traditional):
  Use type on a computer for print, PDF, and static use
  Typically: per user (number of people using it) AND/OR
             per CPU (number of computers it's installed on)
  Common tiers: 1 user, 3 users, 5 users, 10 users, site license

  What you can do:
  - Install on licensed computers
  - Create print materials (PDFs, brochures, books, presentations)
  - Embed in PDF with some restrictions (subsetting OK; full embedding may not be)

  What you CANNOT do (without additional licenses):
  - Serve as a web font (requires webfont license)
  - Embed in an app (requires app license)
  - Embed in an ebook (requires ebook license)
  - Render on a server to generate dynamic images (requires server license)

WEBFONT LICENSE:
  Serve font via @font-face for web delivery
  Typically: per domain AND/OR per pageview tier
  Common tiers: <10K pageviews/month, 10K–100K, 100K–1M, 1M+

  WOFF2 delivery: font file hosted on your server or served via CDN
  The font file itself is licensed; must not be directly downloadable

  Gotcha: desktop license does NOT include web font rights
  Many companies have violated this unknowingly

APP LICENSE:
  Embed font in a mobile app (.ipa / .apk) or desktop app
  Typically: per app, sometimes per number of app installations
  Ebook/epub also usually requires separate license

SERVER LICENSE:
  Render text to images on server (dynamic generation, PDF printing)
  Per server or per-CPU tiers
  Required for: generating social cards with type, PDF generation services,
  invoice/report generation with specific fonts

ENTERPRISE/CUSTOM LICENSING:
  Large organizations often negotiate:
  - All employees; any use
  - All domains owned by company
  - Unlimited pageviews
  Usually multi-year contracts; custom pricing

LICENSE TRACKER TABLE:
  ┌────────────────────┬────────┬────────┬─────┬────────┬────────┐
  │ Use Case           │Desktop │Webfont │ App │E-book  │Server  │
  ├────────────────────┼────────┼────────┼─────┼────────┼────────┤
  │ Print document     │   ✓    │        │     │        │        │
  │ PDF (embedded)     │   ✓    │        │     │        │        │
  │ Website @font-face │        │   ✓    │     │        │        │
  │ Mobile app         │        │        │  ✓  │        │        │
  │ Desktop app        │   ✓    │        │ ✓?  │        │        │
  │ Ebook (.epub)      │        │        │     │   ✓    │        │
  │ Server PDF gen.    │        │        │     │        │   ✓    │
  │ Social card gen.   │        │        │     │        │   ✓    │
  └────────────────────┴────────┴────────┴─────┴────────┴────────┘
  NOTE: Some foundries bundle some of these; always check specific EULA

──────────────────────────────────────────────────────────────────────────────
```

---

## Type Piracy and IP

```
FONT PIRACY AND IP FRAMEWORK
──────────────────────────────────────────────────────────────────────

US COPYRIGHT POSITION:
  Letterform designs: NOT copyrightable (utilitarian exception)
    — You can look at Helvetica and draw new letterforms inspired by it
    — The shape of letters is "useful art" not "fine art"
  Font software (the digital file): IS copyrightable as a computer program
    — The .ttf/.otf/.woff2 file is copyrighted software
    — Copying the file without a license = copyright infringement

  Practical result:
    Creating a typeface "inspired by" Helvetica: legal (Arial exists)
    Copying the Helvetica font file and redistributing: infringement

GERMANY / EU POSITION:
  Germany: font designs themselves are protected (design protection law)
  EU: similar; the design may have design right protection for 25 years
  This creates geo-specific exposure for foundries (Berthold sued US companies)

PIRACY REALITY:
  Widespread. Fonts are trivially copyable files.
  Common piracy vectors:
  - Torrent sites and font-sharing websites
  - Fonts bundled with pirated applications (Adobe CS, etc.)
  - "Free font" sites serving paid fonts without license
  - Colleague email ("I have this font, want it?")

  Enforcement:
  - MyFonts watermarking: fonts served by MyFonts have embedded metadata
  - Piracy detection services: automated crawler finds unlicensed @font-face
  - Cease-and-desist letters (most common resolution)
  - Civil lawsuits (rare but precedent-setting)

THE "I FOUND IT FREE ONLINE" DEFENSE:
  Finding a font file for free download on a random website does not
  mean it is free to use commercially. Many pirated fonts circulate
  on font-sharing sites as free. Check the license file bundled with
  the font, or purchase from the original foundry. If you can't identify
  the source, don't use it in commercial work.

RECOGNITION TEST:
  Before using any font, check:
  1. Where did this file come from?
  2. Is there a license file (.txt, .rtf, OFL.txt) included?
  3. Does that license cover my use case (web, app, commercial)?
  Foundry websites: myfonts.com, fonts.adobe.com, typography.com, klim.co.nz
──────────────────────────────────────────────────────────────────────
```

---

## Corporate Custom Typefaces

Large organizations invest in custom typefaces for the same reason they invest in any brand asset — consistent, unique visual identity that cannot be appropriated by competitors:

```
CORPORATE TYPEFACE INVESTMENTS
──────────────────────────────────────────────────────────────────────

IBM PLEX (2017)
  Designer: Bold Monday (Mike Abbink + Paul van der Laan)
  Why: IBM's previous brand fonts (Helvetica) available to anyone;
       IBM wanted type that embodied the IBM brand
  Scope: Plex Sans, Plex Serif, Plex Mono + 13 script variants
  Open source: released under OFL; available free
  Now: used across all IBM products, documentation, marketing
  Investment: estimated ~$2M+ design + engineering work

APPLE SF PRO / SF MONO (2015–present)
  Designed in-house by Apple Typography team
  SF Pro: system font for macOS, iOS, iPadOS, watchOS, tvOS
  SF Mono: developer/code editor use
  Not licensed to third parties; Apple platform only
  Notable: optical size variants (SF Pro Display, SF Pro Text) built in
  The only system font stack with genuine optical sizing in common use

MICROSOFT SEGOE UI (2004–present, various)
  Gary Munch (Monotype); developed for Windows Vista brand
  Segoe: clean humanist sans; designed to work at Windows UI sizes
  Segoe UI Variable (2021): variable font version built into Windows 11
    wght axis + opsz axis; system-level variable font
  Microsoft's investment: multiple designers over 15+ years; now the
  Windows platform identity font

GITHUB MONASPACE (2023)
  Designers: Lettermatic (Bianca Berning + Jeremie Hornus)
  GitHub's custom programming font family
  Five variable monospace typefaces: Neon, Argon, Xenon, Radon, Krypton
  "Texture healing": proportional spacing for equal-width characters
  Open source (OFL)

BBC REITH (2017)
  Designers: Dalton Maag
  Replace old Gill Sans (problematic designer history + generic feel)
  Reith Sans + Reith Serif; variable fonts
  Named for John Reith, BBC's first Director-General
  Commissioned for full media spectrum: screens, apps, print

GOOGLE PRODUCT SANS / GOOGLE SANS
  Geometric sans; used in Google products and branding
  Not publicly licensed; Google's internal use
  Google Fonts has open alternatives (Nunito for geometric; Inter for humanist)

TYPICAL CUSTOM TYPEFACE INVESTMENT RANGE:
  Small brand/startup:    $15,000–$50,000   (1–2 weights; limited coverage)
  Mid-size company:       $50,000–$300,000  (full family; multiple scripts)
  Large enterprise/brand: $300,000–$2M+     (comprehensive; variable; multilingual)
  FAANG-scale:            $2M–$10M+         (full system; all scripts; engineering)

ROI CALCULATION:
  License fees eliminated: a company using Helvetica Neue for everything
  might pay $50K–$200K/year in licensing fees
  Custom font: one-time investment; perpetual use
  Break-even: 2–5 years if current licensing fees are high

  Non-financial value: brand distinctiveness, consistency, trademark protection
  (Custom typefaces can sometimes be trademarked as trade dress)
──────────────────────────────────────────────────────────────────────
```

---

## Choosing Your Font Strategy

```
FONT STRATEGY DECISION TREE
──────────────────────────────────────────────────────────────────────────────

1. WHAT ARE YOUR REQUIREMENTS?
   ┌──────────────────────────────────────────────────────────────┐
   │ Need unique brand identity? → Custom or licensed distinctive │
   │ Standard UI / internal tool? → System stack or Google Fonts  │
   │ Consumer app? → Google Fonts, Adobe Fonts, or licensed       │
   │ Print/publishing? → Licensed desktop fonts                   │
   └──────────────────────────────────────────────────────────────┘

2. SYSTEM FONT STACK (ZERO COST, ZERO HTTP):
   Best for: internal tools, dashboard UI, performance-critical
   CSS:
     font-family: -apple-system, BlinkMacSystemFont, "Segoe UI Variable",
                  "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
   Result:
     Apple: San Francisco (humanist sans, excellent)
     Windows 11: Segoe UI Variable (humanist sans, variable, excellent)
     Android: Roboto (humanist sans, good)
   When to use: always consider this first; many products don't need more

3. GOOGLE FONTS (FREE, OPEN SOURCE):
   Best for: web projects where you want a specific typeface
   Quality tier: professional to excellent (varies by font)
   Recommendation:
     UI sans: Inter (best choice 2024)
     Long-form text: Literata, Merriweather
     Display serif: Playfair Display, Fraunces
     Code: JetBrains Mono (or use system monospace stack)
   Hosted or self-hosted:
     Hosted: fonts.googleapis.com (performance + GDPR tradeoff)
     Self-hosted: copy files; use CSS @font-face; no Google tracking

4. LICENSED FONTS (PAID):
   Best for: brand-critical uses; specific historical faces; premium quality
   Sources:
     MyFonts (myfonts.com): largest commercial selection; simple checkout
     Fontspring: perpetual license; no pageview tiers (flat fee)
     Fonts.com: Monotype Group catalog; subscription option
     Type Foundry websites: buy direct (Type-Together, Klim, Commercial Type)
     Adobe Fonts: if already CC subscriber; excellent selection

5. CUSTOM COMMISSIONED:
   Best for: enterprise; brand differentiation; protecting identity
   Timeline: 6–18 months for quality work
   Budget: $50K minimum for anything useful; $300K+ for complete family

──────────────────────────────────────────────────────────────────────────────
```

---

## Decision Cheat Sheet

| Scenario | Recommended Approach | Budget |
|----------|---------------------|--------|
| Internal tool / dashboard | System font stack | $0 |
| Consumer web app | Google Fonts (Inter + Merriweather) | $0 |
| Startup landing page | Google Fonts or Fontspring licensed | $0–$500 |
| Mid-size company web presence | Licensed from Monotype/foundry or Google Fonts | $200–$5K/yr |
| Consumer app (iOS/Android) | Embed Google Fonts (OFL); or system fonts | $0 |
| Print materials (internal) | System fonts or desktop license | $0–$1K |
| Brand/marketing use | Desktop + webfont license; distinctive typeface | $500–$5K |
| Enterprise platform | Enterprise license negotiation | $10K–$100K+/yr |
| Full brand identity | Commission custom | $100K–$2M |

---

## Common Confusion Points

**Adobe Fonts requires a live subscription**
Unlike a purchased desktop license where you own the font, Adobe Fonts are accessible only while your Creative Cloud subscription is active. If you cancel CC, web fonts hosted through Adobe Fonts stop serving. Self-hosting and perpetual licenses from foundries do not have this constraint.

**Google Fonts' "free" has nuances for some uses**
Google Fonts are free and OFL-licensed, but self-hosting removes dependency on Google's servers (DNS lookup latency; Google IP logging; potential GDPR issues for EU visitors). For privacy-sensitive products, self-host Google Fonts rather than loading from fonts.googleapis.com.

**Fontspring vs MyFonts vs foundry direct**
Fontspring offers mostly perpetual licenses (one-time payment; no per-pageview tiers) — usually the most cost-effective for stable web use. MyFonts has the largest selection but uses per-pageview webfont pricing (ongoing cost). Foundry direct (e.g., klim.co.nz, commercial.type) sometimes offers better terms and is the morally correct choice (more money to the designer), but may have less convenient checkout.

**"We used Helvetica in our logo, we own it"**
A designer using Helvetica to create your logo does not give you the right to use Helvetica in your digital products or printed materials. That designer had a desktop license for their design work. Your use of the resulting artwork is fine. But if you then want to use Helvetica on your website or in your apps, you need to license it separately for those uses.

**The type industry is not dead despite free fonts**
Monotype Group, Commercial Type, Klim, and independent foundries continue to do substantial business. The market has bifurcated: commodity web use → Google Fonts; differentiated brand use → paid licenses and custom commissions. The custom typeface business in particular is larger than ever, driven by the recognition that brand visual identity (including type) is a strategic asset for large companies.
