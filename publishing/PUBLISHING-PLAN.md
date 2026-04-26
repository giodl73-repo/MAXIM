# Publishing Plan — MAXIM Reference Library

*52 volumes + Card 0 · 206 directories · 2,178 files · 5,063,843 words*
*"Three Rings for the Elven-kings under the sky..."*

---

## The Rings

```
                    ┌─────────────────────────────────┐
                    │     THE ONE RING (source repo)  │
                    │  Git + MkDocs + Markdown master │
                    │   "One Ring to rule them all"   │
                    └──────────┬──────────────────────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
              ▼                ▼                ▼
    ┌─────────────────┐ ┌───────────┐ ┌──────────────────┐
    │   THREE ELVEN   │ │   SEVEN   │ │   NINE RINGS     │
    │     RINGS       │ │  DWARVEN  │ │   OF MEN         │
    │                 │ │   RINGS   │ │                  │
    │ Archival sets   │ │ Standard  │ │ Paperback /      │
    │ Smyth sewn      │ │ hardcover │ │ print-on-demand  │
    │ Acid-free       │ │ PUR bound │ │ POD via Amazon / │
    │ Cloth boards    │ │ Printed   │ │ IngramSpark      │
    │ Foil-stamped    │ │ boards    │ │                  │
    │                 │ │           │ │ Internet-         │
    │ 3 complete sets │ │ ~7 sets   │ │ available to all  │
    │ Narya · Nenya   │ │           │ │                  │
    │ · Vilya         │ │           │ │                  │
    └─────────────────┘ └───────────┘ └──────────────────┘
```

---

## Tier Definitions

### Tier 1 — The Three Elven Rings (Archival)

*"Three Rings for the Elven-kings under the sky"*

| Attribute | Specification |
|-----------|--------------|
| **Copies** | 3 complete sets (53 books each = 159 books) |
| **Binding** | Smyth sewn signatures + case bound |
| **Paper** | Acid-free, lignin-free, ANSI Z39.48-compliant (500+ year rated) |
| **Cover** | Library buckram cloth over rigid boards |
| **Spine** | Foil-stamped: volume number, section name, card suit |
| **Interior** | B&W, monospace font for diagrams (JetBrains Mono or IBM Plex Mono) |
| **Trim** | 8.5" × 11" (per book.md binding spec) |
| **Extras** | Ribbon bookmark, head/tail bands |
| **Purpose** | Survive. Three locations. One for use, one stored, one off-site. |
| **Target cost** | $20–30/book → ~$3,200–4,800 per set → ~$9,500–14,400 total |
| **Vendor class** | Short-run specialty: Lightning Press, Gorham Printing, or Kase Printing |

**Ring names and locations:**
- **Narya** (Ring of Fire) — Primary copy. Active use. Home library.
- **Nenya** (Ring of Water) — Stored copy. Climate-controlled. Secondary location.
- **Vilya** (Ring of Air) — Off-site copy. Safe deposit or trusted holder.

### Tier 2 — The Seven Dwarven Rings (Standard Hardcover)

*"Seven for the Dwarf-lords in their halls of stone"*

| Attribute | Specification |
|-----------|--------------|
| **Copies** | ~7 sets (or as gifted — the number is thematic, adjust to need) |
| **Binding** | PUR adhesive + case bound (50–100 year durability) |
| **Paper** | Acid-free white, 80 lb text (decent but not archival-grade) |
| **Cover** | Printed laminated boards (matte finish) |
| **Spine** | Printed: volume number + section name |
| **Interior** | B&W, same layout as Elven |
| **Trim** | 8.5" × 11" |
| **Purpose** | Gift sets. Handsome shelf presence. Readable for decades. |
| **Target cost** | $12–18/book → ~$640–950 per set → ~$4,500–6,700 for 7 sets |
| **Vendor class** | Same short-run printer (bundle with Elven order for volume discount) |

### Tier 3 — The Nine Rings of Men (Paperback / POD)

*"Nine for Mortal Men doomed to die"*

| Attribute | Specification |
|-----------|--------------|
| **Copies** | Print-on-demand — unlimited, ordered individually |
| **Binding** | Perfect bound (trade paperback) |
| **Paper** | Standard cream or white, 60 lb |
| **Cover** | Glossy or matte cardstock with printed cover art |
| **Interior** | B&W |
| **Trim** | 6" × 9" (trade paperback — smaller for POD economics) |
| **Purpose** | Internet-available. Anyone can order. Low price point. |
| **Target cost** | $5–10/book retail (you set the price; POD takes a cut) |
| **Vendor class** | Amazon KDP, IngramSpark, Lulu, or Blurb |
| **Distribution** | Amazon, Barnes & Noble, bookshop.org, libraries (via Ingram) |

### Tier 0 — The One Ring (Digital)

*"One Ring to rule them all, One Ring to find them"*

| Channel | Format | Cost |
|---------|--------|------|
| **MkDocs site** | HTML, searchable, cross-linked | Free (GitHub Pages or similar) |
| **PDF downloads** | One PDF per volume, print-ready | Free |
| **EPUB** | E-reader format | Free |
| **GitHub repo** | Raw Markdown source | Free (public repo) |

---

## Production Pipeline

```
┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐
│ STAGE 1  │──▶│ STAGE 2  │──▶│ STAGE 3  │──▶│ STAGE 4  │──▶│ STAGE 5  │
│ Content  │   │ PDF Gen  │   │ Design   │   │ Proof    │   │ Print    │
│ Complete │   │ Pipeline │   │ & Layout │   │ Review   │   │ Runs     │
└──────────┘   └──────────┘   └──────────┘   └──────────┘   └──────────┘
     │              │              │              │              │
     ▼              ▼              ▼              ▼              ▼
  Batches       MkDocs →       Cover art      Single copy    Elven →
  7–12 done     per-volume     Spine design   of each tier   Dwarven →
  @editor P1    PDF with       Interior       Read, mark     Human POD
  tags clear    print CSS      typography     up, iterate    setup
                               Page layout
```

### Stage 1 — Content Completion ✅ DONE

| Task | Status |
|------|--------|
| Batches 1–13 content complete | ✅ All 217 directories written |
| @editor tags cleared across all files | ✅ Zero outstanding tags |
| `read-this-first/` volume finalized | ✅ |
| Concept Index / Atlas | ✅ 314 entries |

**Gate passed. All 53 volumes ready for Stage 2.**

### Stage 2 — PDF Generation Pipeline

| Task | Status | Notes |
|------|--------|-------|
| Choose MkDocs PDF plugin | ⬜ Not started | `mkdocs-with-pdf` or `mkdocs2book` |
| Design print CSS (margins, headers, footers) | ⬜ Not started | 7×10 trim, 0.75" margins |
| Choose monospace font for diagrams | ⬜ Not started | JetBrains Mono or IBM Plex Mono |
| Choose body font | ⬜ Not started | Palatino, Garamond, or Charter |
| Generate test PDF for one volume | ⬜ Not started | Pick a complete volume (computing/) |
| Verify ASCII diagrams render correctly | ⬜ Not started | Critical — boxes must align |
| Build per-volume PDF generation script | ⬜ Not started | One PDF per card (53 total) |
| Generate all 53 PDFs | ⬜ Not started | Depends on content completion |

### Stage 3 — Cover Design & Layout

| Task | Status | Notes |
|------|--------|-------|
| Design cover template (Elven tier) | ⬜ Not started | Buckram color scheme per section |
| Design cover template (Dwarven tier) | ⬜ Not started | Printed board design |
| Design cover template (Human tier) | ⬜ Not started | Paperback cover art |
| Spine layout — foil stamp spec | ⬜ Not started | Volume #, section, card suit |
| Interior title page design | ⬜ Not started | Per-volume title page |
| Table of contents per volume | ⬜ Not started | Auto-generated from headings |
| Colophon / copyright page | ⬜ Not started | Licensing, attribution, archival note |
| ISBN assignment (if distributing) | ⬜ Not started | Bowker — $295 for 10 ISBNs, $575 for 100 |

### Stage 4 — Proof Review

| Task | Status | Notes |
|------|--------|-------|
| Order 1 proof copy (Elven spec) | ⬜ Not started | From chosen vendor |
| Order 1 proof copy (Dwarven spec) | ⬜ Not started | Same or different vendor |
| Order 1 proof copy (Human spec) | ⬜ Not started | POD platform proof order |
| Physical review — binding, paper, readability | ⬜ Not started | Check diagram legibility |
| Physical review — spine text alignment | ⬜ Not started | Does foil stamp read correctly? |
| Iterate on issues found | ⬜ Not started | Fix PDF, re-proof if needed |

### Stage 5 — Print Runs & Distribution

| Task | Status | Notes |
|------|--------|-------|
| **Elven:** Place order — 3 sets × 53 books | ⬜ Not started | Lightning Press / Gorham |
| **Dwarven:** Place order — ~7 sets × 53 books | ⬜ Not started | Same vendor (bundle) |
| **Human:** Set up POD listings | ⬜ Not started | KDP + IngramSpark |
| **Digital:** Deploy MkDocs site | ⬜ Not started | GitHub Pages / Netlify |
| **Digital:** Upload PDFs for download | ⬜ Not started | GitHub Releases or site |
| **Digital:** Generate EPUB versions | ⬜ Not started | Pandoc or mkdocs2book |
| Ship Narya to location A | ⬜ Not started | — |
| Ship Nenya to location B | ⬜ Not started | — |
| Ship Vilya to location C | ⬜ Not started | — |

---

## Vendor Research

### Can One Vendor Do All Three Tiers?

**Short answer: No.** You need two vendors minimum.

| Tier | Vendor Type | Why |
|------|------------|-----|
| Elven + Dwarven | **Short-run specialty printer** | Smyth sewn binding, acid-free stock, cloth boards — these are custom specs that POD platforms don't offer |
| Human | **POD platform** (KDP / IngramSpark) | Different business model entirely — they print one copy at a time on commodity equipment |

**Best strategy:** Use one short-run printer for Elven + Dwarven (volume discount on ~530 books total), and a POD platform for Human tier.

### Shortlisted Vendors

#### For Elven + Dwarven Tiers

| Vendor | Location | Smyth Sewn | Acid-Free | Min Order | Notes |
|--------|----------|-----------|-----------|-----------|-------|
| **Lightning Press** | Sacramento, CA | ✅ | ✅ | 10 books | Ultra-low qty specialist. US-made. |
| **Gorham Printing** | Centralia, WA | ✅ | ✅ | 25 books | Self-publisher friendly. Transparent pricing. |
| **Kase Printing** | Hudson, NH | Ask | ✅ (PUR standard) | Low | Short-run specialist. |
| **Mixam** | Online | ✅ (default) | Ask | 1 book | Good for proof copies. |

#### For Human Tier (POD)

| Platform | Distribution | Hardcover? | Paperback | Notes |
|----------|-------------|-----------|-----------|-------|
| **Amazon KDP** | Amazon only | ✅ (case laminate) | ✅ | Largest market. Lowest royalty friction. |
| **IngramSpark** | 40,000+ retailers | ✅ | ✅ | Libraries, bookstores, B&N. Best reach. |
| **Lulu** | Lulu + Amazon | ✅ | ✅ | Easiest setup. Good for direct sales. |

**Recommendation:** KDP (for Amazon presence) + IngramSpark (for everything else). Many self-publishers use both.

### Can I (Claude) Order This?

No — I can't place orders, make purchases, or interact with vendor systems. But I can:

- ✅ Build the entire PDF generation pipeline (MkDocs → print-ready PDF)
- ✅ Generate cover templates and spine layouts
- ✅ Write the interior CSS/layout for all three tiers
- ✅ Prepare KDP/IngramSpark-compliant files (they have specific PDF specs)
- ✅ Draft the vendor RFQ email for the Elven/Dwarven tiers
- ✅ Track the entire pipeline in this document
- ✅ Automate everything up to the "click Buy" moment

---

## Cost Summary

| Tier | Books | Per Book | Per Set | Total |
|------|-------|---------|---------|-------|
| Elven (3 sets × 53) | 159 | $20–30 | $1,060–1,590 | **$3,200–4,800** |
| Dwarven (7 sets × 53) | 371 | $12–18 | $640–950 | **$4,500–6,700** |
| Human (POD setup) | — | — | — | **$0–575** (ISBN costs only) |
| Digital (hosting) | — | — | — | **$0** (GitHub Pages) |
| **Proof copies** | ~6 | $25–35 | — | **$150–210** |
| **ISBN block** | — | — | — | **$575** (100 ISBNs from Bowker) |
| | | | | |
| **TOTAL** | 530+ | | | **$8,400–12,300** |

*Human tier ongoing cost: $0 — POD prints on demand, you get royalty per sale.*

---

## Decision Log

| # | Decision | Options | Chosen | Date | Notes |
|---|----------|---------|--------|------|-------|
| 1 | Tier structure | Flat / tiered | Three tiers (Elven/Dwarven/Human) | 2026-02-26 | LOTR metaphor |
| 2 | Archival binding | Smyth sewn / PUR / perfect | Smyth sewn (Elven) | 2026-02-26 | 100+ year target |
| 3 | Archival paper | Standard / acid-free | ANSI Z39.48 acid-free | 2026-02-26 | 500+ year rating |
| 4 | POD platform | KDP / Ingram / Lulu | TBD | — | Likely KDP + IngramSpark |
| 5 | Short-run vendor | Lightning / Gorham / Kase | TBD | — | Need quotes |
| 6 | Trim size | 6×9 / 7×10 / 8.5×11 | 7×10 (Elven/Dwarven), 6×9 (Human) | 2026-02-26 | Standard technical ref size |
| 7 | Body font | Palatino / Garamond / Charter | TBD | — | Test in proof |
| 8 | Mono font | JetBrains / IBM Plex / Fira | TBD | — | ASCII diagram fidelity |
| 9 | ISBNs | Skip / 10-pack / 100-pack | TBD | — | Need 53+ if distributing all volumes |
| 10 | Cover design | DIY / commission artist | TBD | — | |
| 11 | Dwarven count | 7 / fewer / more | 7 (thematic) | 2026-02-26 | Adjust as needed |

---

## Open Questions

- [ ] Do Dwarven sets get the same interior layout as Elven, just cheaper binding/paper?
- [ ] Should Human tier include ALL 53 volumes, or a curated subset?
- [ ] Box/slipcase for Elven sets? (adds ~$50–100 per set but gorgeous)
- [ ] Creative Commons license for digital tier, or all rights reserved?
- [ ] Do we want the card-suit motif on the physical covers?
- [ ] Index volume (53rd book) — same content as the digital concept index?

---

## Next Actions

1. **Continue content completion** — Batches 7–12 are the long pole
2. **Prototype the PDF pipeline** — Pick one complete volume, generate a print-ready PDF
3. **Test monospace font rendering** — ASCII diagrams are make-or-break for this library
4. **Get vendor quotes** — Email Lightning Press and Gorham with the project scope
5. **Decide on ISBNs** — Needed before POD setup, not before short-run printing
