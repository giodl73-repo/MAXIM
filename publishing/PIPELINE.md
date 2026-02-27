# Publishing Pipeline — Status Tracker

*Operational tracking. Master plan in [PUBLISHING-PLAN.md](PUBLISHING-PLAN.md).*

---

## Pipeline Overview

```
 STAGE 1          STAGE 2         STAGE 3         STAGE 4         STAGE 5
 Content          PDF Gen         Design          Proof           Print
 ━━━━━━━━         ━━━━━━━         ━━━━━━          ━━━━━          ━━━━━
 ████████         ░░░░░░░░        ░░░░░░░░        ░░░░░░░░       ░░░░░░░░
  100%            not started     not started     blocked         blocked
  DONE            (unblocked!)    (unblocked!)    (needs S3)     (needs S4)
```

---

## Stage 1 — Content Readiness (per volume)

All volumes passed both gates:
1. **Content complete** — all 217 directories written, zero stubs
2. **Review clean** — zero `@editor` tags in any content file

| Card | Volume | Section | Content | Review | Ready? |
|------|--------|---------|---------|--------|--------|
| 0 | — | Read This First | ✅ | ✅ | ✅ |
| 2♣ | NW·I | Natural World | ✅ | ✅ | ✅ |
| 2♦ | NW·II | Natural World | ✅ | ✅ | ✅ |
| 2♥ | NW·III | Natural World | ✅ | ✅ | ✅ |
| 2♠ | NW·IV | Natural World | ✅ | ✅ | ✅ |
| 3♣ | ES·I | Earth & Space | ✅ | ✅ | ✅ |
| 3♦ | ES·II | Earth & Space | ✅ | ✅ | ✅ |
| 3♥ | ES·III | Earth & Space | ✅ | ✅ | ✅ |
| 3♠ | ES·IV | Earth & Space | ✅ | ✅ | ✅ |
| 4♣ | MC·I | Material Culture | ✅ | ✅ | ✅ |
| 4♦ | MC·II | Material Culture | ✅ | ✅ | ✅ |
| 4♥ | MC·III | Material Culture | ✅ | ✅ | ✅ |
| 4♠ | MC·IV | Material Culture | ✅ | ✅ | ✅ |
| 5♣ | LS·I | Life Sciences | ✅ | ✅ | ✅ |
| 5♦ | LS·II | Life Sciences | ✅ | ✅ | ✅ |
| 5♥ | LS·III | Life Sciences | ✅ | ✅ | ✅ |
| 5♠ | LS·IV | Life Sciences | ✅ | ✅ | ✅ |
| 6♣ | HI·I | History & Ideas | ✅ | ✅ | ✅ |
| 6♦ | HI·II | History & Ideas | ✅ | ✅ | ✅ |
| 6♥ | HI·III | History & Ideas | ✅ | ✅ | ✅ |
| 6♠ | HI·IV | History & Ideas | ✅ | ✅ | ✅ |
| 7♣ | M·I | Mechanics | ✅ | ✅ | ✅ |
| 7♦ | M·II | Mechanics | ✅ | ✅ | ✅ |
| 7♥ | M·III | Mechanics | ✅ | ✅ | ✅ |
| 7♠ | M·IV | Mechanics | ✅ | ✅ | ✅ |
| 8♣ | T·I | Technology | ✅ | ✅ | ✅ |
| 8♦ | T·II | Technology | ✅ | ✅ | ✅ |
| 8♥ | T·III | Technology | ✅ | ✅ | ✅ |
| 8♠ | T·IV | Technology | ✅ | ✅ | ✅ |
| 9♣ | SS·I | Social Sciences | ✅ | ✅ | ✅ |
| 9♦ | SS·II | Social Sciences | ✅ | ✅ | ✅ |
| 9♥ | SS·III | Social Sciences | ✅ | ✅ | ✅ |
| 9♠ | SS·IV | Social Sciences | ✅ | ✅ | ✅ |
| 10♣ | LC·I | Language & Comm | ✅ | ✅ | ✅ |
| 10♦ | LC·II | Language & Comm | ✅ | ✅ | ✅ |
| 10♥ | LC·III | Language & Comm | ✅ | ✅ | ✅ |
| 10♠ | LC·IV | Language & Comm | ✅ | ✅ | ✅ |
| J♣ | MP·I | Math & Physics | ✅ | ✅ | ✅ |
| J♦ | MP·II | Math & Physics | ✅ | ✅ | ✅ |
| J♥ | MP·III | Math & Physics | ✅ | ✅ | ✅ |
| J♠ | MP·IV | Math & Physics | ✅ | ✅ | ✅ |
| Q♣ | AC·I | Arts & Culture | ✅ | ✅ | ✅ |
| Q♦ | AC·II | Arts & Culture | ✅ | ✅ | ✅ |
| Q♥ | AC·III | Arts & Culture | ✅ | ✅ | ✅ |
| Q♠ | AC·IV | Arts & Culture | ✅ | ✅ | ✅ |
| K♣ | C·I | Computing & SW | ✅ | ✅ | ✅ |
| K♦ | C·II | Computing & SW | ✅ | ✅ | ✅ |
| K♥ | C·III | Computing & SW | ✅ | ✅ | ✅ |
| K♠ | C·IV | Computing & SW | ✅ | ✅ | ✅ |
| A♣ | P·I | People | ✅ | ✅ | ✅ |
| A♦ | P·II | People | ✅ | ✅ | ✅ |
| A♥ | P·III | People | ✅ | ✅ | ✅ |
| A♠ | P·IV | People | ✅ | ✅ | ✅ |

**All 53 volumes ready for Stage 2. Content gate passed.**

---

## Stage 2 — PDF Generation

| Task | Owner | Status | Notes |
|------|-------|--------|-------|
| Evaluate `mkdocs-with-pdf` | — | ⬜ | |
| Evaluate `mkdocs2book` | — | ⬜ | |
| Evaluate Pandoc direct approach | — | ⬜ | May give more control |
| Select monospace font | — | ⬜ | Must test ASCII box alignment |
| Select body font | — | ⬜ | |
| Write print CSS stylesheet | — | ⬜ | 7×10 trim, margins, headers |
| Build generation script | — | ⬜ | `generate-volume.sh <card>` |
| Test: generate computing/ volume | — | ⬜ | First proof-of-concept |
| Test: verify diagram fidelity | — | ⬜ | |

---

## Stage 3 — Design

| Task | Owner | Status | Notes |
|------|-------|--------|-------|
| Cover design brief | — | ⬜ | Section colors? Card suits? |
| Elven cover spec (buckram + foil) | — | ⬜ | |
| Dwarven cover spec (printed board) | — | ⬜ | |
| Human cover spec (paperback) | — | ⬜ | |
| Interior title page template | — | ⬜ | |
| Colophon / copyright page | — | ⬜ | |
| ISBN acquisition | — | ⬜ | Bowker — need 53+ |

---

## Stage 4 — Proofing

| Task | Owner | Status | Notes |
|------|-------|--------|-------|
| Order Elven proof (1 volume) | — | ⬜ | |
| Order Dwarven proof (1 volume) | — | ⬜ | |
| Order Human proof (1 volume) | — | ⬜ | |
| Physical inspection checklist | — | ⬜ | |
| Iterate and re-proof if needed | — | ⬜ | |

---

## Stage 5 — Print & Ship

| Task | Owner | Status | Notes |
|------|-------|--------|-------|
| Elven: place full order (159 books) | — | ⬜ | |
| Dwarven: place full order (~371 books) | — | ⬜ | |
| Human: set up KDP listings | — | ⬜ | |
| Human: set up IngramSpark listings | — | ⬜ | |
| Digital: deploy MkDocs site | — | ⬜ | |
| Digital: publish PDFs | — | ⬜ | |
| Digital: generate EPUBs | — | ⬜ | |
| Ship Narya → Location A | — | ⬜ | |
| Ship Nenya → Location B | — | ⬜ | |
| Ship Vilya → Location C | — | ⬜ | |

---

## Blockers & Risks

| Risk | Impact | Mitigation |
|------|--------|-----------|
| ASCII diagrams break in PDF | Entire library unreadable | Test early — Stage 2 gate |
| Vendor can't do Smyth sewn at qty 53 | Elven tier compromised | Have backup vendor |
| Content batches 7–12 take too long | Delays everything | Can print completed volumes first |
| ISBNs expensive for 53 volumes | $575 for 100-pack | Only needed for POD distribution |
| Font licensing for print | Legal issue | Use OFL-licensed fonts (JetBrains, IBM Plex) |

---

*Last updated: 2026-02-26*
