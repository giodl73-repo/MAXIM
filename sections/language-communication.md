# Language & Communication

7 directories · From phoneme to broadcast — the full stack of how humans encode and transmit meaning

---

## Landscape

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                         LANGUAGE & COMMUNICATION                                    │
└─────────────────────────────────────────────────────────────────────────────────────┘

 LANGUAGE STRUCTURE                        ENCODING / NOTATION
 ┌────────────────────────────────┐        ┌────────────────────────────────────────┐
 │         linguistics/           │        │              codes/                    │
 │  phonology · morphology        │        │  Morse · Braille · semaphore           │
 │  syntax · semantics            │──────▶ │  steganography · encoding systems      │
 │  Chomsky hierarchy             │        │  historical ciphers                    │
 │  acquisition · typology        │        └───────────────────┬────────────────────┘
 └───────────────┬────────────────┘                            │
                 │ cross-linguistic                            ▼
 ┌───────────────▼────────────────┐        ┌────────────────────────────────────────┐
 │       world-languages/         │        │             typography/                │
 │  language families             │        │  type anatomy · classification         │
 │  Indo-European tree            │        │  serif/sans/script/display             │
 │  Semitic · Sino-Tibetan        │        │  typesetting history · digital type    │
 │  writing systems               │        │  legibility science                    │
 │  endangered languages · creoles│        └───────────────────┬────────────────────┘
 └────────────────────────────────┘                            │ visual form
                                                               │ of language
 MEDIA / DISTRIBUTION                                          │
 ┌──────────────────────────────────────────────────────────── ▼ ──────────────────┐
 │                                                                                  │
 │  ┌───────────────────────┐   ┌───────────────────────┐   ┌──────────────────┐   │
 │  │   printing-publishing/│   │     cinema-film/       │   │ radio-television/│   │
 │  │  woodblock→offset     │   │  film tech · narrative │   │ AM/FM · spectrum │   │
 │  │  Gutenberg press      │──▶│  grammar · auteur      │◀──│ regulation       │   │
 │  │  industrialization    │   │  industry economics    │   │ formats · ratings│   │
 │  │  publishing economics │   │  digital transition    │   │ streaming shift  │   │
 │  │  digital disruption   │   └───────────────────────┘   └──────────────────┘   │
 │  └───────────────────────┘                                                       │
 │                                                                                  │
 └──────────────────────────────────────────────────────────────────────────────────┘

 KEY CROSS-SECTION BRIDGE
 linguistics/ ←──────────────────────────────────────────────────────────▶ computing/
 Chomsky hierarchy = formal language theory = automata theory  (same math, two literatures)
```

---

## Directories

| Directory | Focus | Entry Point | Bridges to |
|-----------|-------|-------------|------------|
| `linguistics/` | The scientific study of language structure: phonology (sound systems), morphology (word formation), syntax (phrase/sentence structure), semantics (meaning), pragmatics (use in context), language acquisition (Chomsky vs. Tomasello), typological universals across 7,000+ languages | `01-PHONOLOGY.md` — sound systems and the IPA, start here before syntax | Computing & Software (`formal-grammars/`): the Chomsky hierarchy — regular, context-free, context-sensitive, recursively enumerable — is automata theory; `codes/` for how phoneme → grapheme → encoded signal |
| `world-languages/` | Survey of the world's language families: Indo-European phylogeny (Germanic/Romance/Slavic/Indo-Iranian branches), Semitic (Arabic/Hebrew divergence), Sino-Tibetan tonal systems, Austronesian spread, writing system typology (logographic/syllabic/alphabetic/abjad), endangered language crisis, creole genesis | `01-OVERVIEW.md` — family tree overview and geographic spread | `linguistics/` for the underlying structural analysis; History & Ideas for migration patterns that explain family distributions |
| `codes/` | Non-cipher encoding systems: Morse code (history and transmission), Braille (cell system, contractions), semaphore (flag/optical telegraph), nautical signal flags, ASCII/Unicode (character encoding as a code problem), steganography (hiding information in plain sight), historical codes (Caesar, Vigenère, Enigma at conceptual level) | `01-MORSE.md` — the simplest pure encoding, establishes the encode/decode frame | Computing & Software `cryptography/` for when encoding becomes security-relevant; `typography/` for the encoding-to-visual-form handoff |
| `typography/` | Type anatomy (baseline, x-height, ascender, descender, kerning, tracking, leading), historical classification (old-style/transitional/modern/slab-serif/humanist-sans/geometric-sans/script/display), typesetting history from hand-composition through Linotype through PostScript through OpenType, legibility science (eye-tracking research, reading comprehension factors), digital type rendering (hinting, anti-aliasing, variable fonts) | `01-ANATOMY.md` — type anatomy and classification taxonomy | `printing-publishing/` for how type met industrial production; Arts & Culture `art-history/` for typography as visual design tradition |
| `printing-publishing/` | Technology and economics of print: woodblock and movable type (Bi Sheng, Gutenberg), the print revolution's epistemic effects, letterpress through offset lithography, phototypesetting, desktop publishing (Aldus PageMaker, PostScript), publishing industry structure (acquisitions/editorial/production/distribution), digital disruption (ebooks, print-on-demand, platform aggregators) | `01-GUTENBERG.md` — the Gutenberg press as inflection point, anchors everything after | History & Ideas for the intellectual history of the print revolution; `typography/` for the craft tradition that print industrialized |
| `cinema-film/` | Film as technology and as language: photochemical process (frame rates, persistence of vision, emulsion), narrative grammar (shot/scene/sequence, continuity editing, montage theory), genre as industrial category, auteur theory (Bazin/Cahiers du Cinéma), studio system economics, international cinema traditions (Italian neorealism, French New Wave, Hong Kong, Bollywood), digital transition (DI pipeline, streaming economics) | `01-TECHNOLOGY.md` — photochemical and digital capture, establishes the medium before the art | Arts & Culture for film as aesthetic form; `radio-television/` for the parallel broadcast medium |
| `radio-television/` | Broadcast technology and industry: AM/FM modulation, spectrum allocation and regulation (FCC/ITU), television standards (NTSC/PAL/SECAM), network-affiliate model, public broadcasting, audience measurement (Nielsen ratings, Arbitron), format history (soap opera/sitcom/news/talk), cable economics, the streaming transition (OTT, SVOD/AVOD/FAST models) | `01-TECHNOLOGY.md` — electromagnetic transmission and modulation fundamentals | `cinema-film/` for content that crossed between film and TV; Computing & Software for the digital infrastructure underneath streaming |

---

## Paths

### Language structure deep-dive
`linguistics/` → `world-languages/` → `codes/`
*Start with universal language structure, then see how it varies across families and writing systems, then step back to see encoding as the formal abstraction that underlies all of it — phoneme, grapheme, and signal bit are the same chain.*

### From glyph to page to broadcast
`typography/` → `printing-publishing/` → `radio-television/`
*Type design governs what gets printed; the industrialization of print created mass literacy and the publishing economy; broadcasting extended that mass audience model into the electromagnetic spectrum — each step is a new distribution layer over the same content economics.*

### Formal language theory bridge (for engineers)
`linguistics/` → Computing & Software `languages/` → Computing & Software `cryptography/`
*Chomsky's hierarchy was not metaphor — Type 3 grammars are finite automata, Type 2 grammars are pushdown automata. Read linguistics first, then see how compiler theory and type systems are the same formalism applied to programming languages, then see how stream ciphers (regular) and block ciphers (not) fit the same classification.*

---

## Adjacent Sections

| Section | The bridge |
|---------|------------|
| Computing & Software | The Chomsky hierarchy (regular/context-free/context-sensitive/recursively enumerable) is simultaneously a linguistics taxonomy and the core of formal language theory and automata theory — same mathematical object, two literatures. `codes/` overlaps directly with `cryptography/`: encoding vs. encipherment is a meaningful distinction only in context. |
| History & Ideas | `printing-publishing/` is inseparable from the intellectual history of the Reformation, Scientific Revolution, and Enlightenment — the press made possible the pamphlet, the journal, and the republic of letters. `economic-history/` connects here through publishing as industry and advertising as the financial model for broadcast. |
| Arts & Culture | `typography/` is a design discipline with deep roots in `art-history/` (Arts and Crafts, Bauhaus, Swiss Style). `cinema-film/` is simultaneously industrial product and art form — the same films appear in both sections' purview, analyzed differently. |
| Mathematics & Physics | `linguistics/` formal semantics (Montague grammar, model-theoretic semantics) uses predicate logic directly. `codes/` and `cryptography/` share information-theoretic foundations: Shannon's channel capacity theorem is the bridge. |
