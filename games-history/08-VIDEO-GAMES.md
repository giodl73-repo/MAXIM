# 08 — Video Games
## Spacewar! to Esports: The Complete Technical and Cultural History

---

## The Big Picture

```
VIDEO GAME HISTORY — 60 YEARS, COMPRESSED
==========================================

1962        1972        1978        1983        1985        1989        1994        2000        2004        2008        2012        2017        2020
  │           │           │           │           │           │           │           │           │           │           │           │           │
ORIGIN    HOME/ARCADE  GOLDEN AGE  CRASH      RENAISSANCE  16-BIT WAR  3D SHIFT   ONLINE     MASSIVELY  MOBILE      ESPORTS    BATTLE     NEXT-GEN
          BIRTH                                              SNES/GEN    PS1/N64    BROADBAND  WoW/MMO    APP STORE   BOOM       ROYALE     SSD ERA
  │           │           │           │           │           │           │           │           │           │           │           │
Spacewar!  Pong/Odyssey  Space Inv.  Atari/ET   NES Seal   Mode 7     CD-ROM     Xbox Live  WoW 12M   Angry Birds  LoL/SC2   Fortnite   PS5/XSX
PDP-1       discrete     Pac-Man     quality    Quality    blast proc  polygon    Halo KA    sub model  F2P rise    TI $40M   Battle Pass  Game Pass
MIT         logic        Donkey Kong control    control    cart vs CD  budget     online sub             whale econ  streaming  cosmetics  xCloud
hacker      chips        ghost AI    flood      gatekeep   64-bit RISC music rev  $50 game              ARPU/LTV    Twitch     live event  sub model
culture     TV display   vector/rast  crash                            FMV        Quake net              $0.99 drop              cross-plat

PLATFORM LAYERS
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
HARDWARE    Mainframe  Discrete   Z80/6502  Custom     RISC       RISC       32/64-bit  x86/GPU   PC homo-   ARM SoC    ARM+GPU    x86 mid   NVMe SSD
            PDP-1      logic ICs  4KB RAM   PPU/mapper 68k/65816  3D chips   MIPS/PS1   dominance genized    mobile     mobile    range GPU  decompres

SOFTWARE    None       ROM        ROM cart  Cart       Cart       Cart/CD    CD-ROM     DVD/Online HDD/DVD   Flash/     Unity      Unreal 4   Unreal 5
            bare       fixed      fixed prg fixed prg  mapper     32 MB      700 MB     4.7 GB    patch DL   App Store  cross-plat ray trace  nanite/lumen

NETWORK     None       None       None      None       None       BBs/serial None       Modem/DSL  Broadband  3G/4G      4G/5G      CDN/       Edge/
                                                                             dial-up    online sub 10Mbps+    LTE        streaming  rollback   cloud
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
```

---

## Section 1: Origins — The Hacker Culture Incubator

### Spacewar! (1962) — MIT, PDP-1, Steve Russell

The first canonical video game was not made by a corporation. It was made by MIT graduate students with unauthorized night access to a $120,000 PDP-1 — the first commercial computer with a real-time CRT display.

```
PDP-1 HARDWARE CONTEXT (1961)
══════════════════════════════

  ┌─────────────────────────────────┐
  │  DEC PDP-1                      │
  │  18-bit word, ~100 KIPS         │
  │  4K × 18-bit ferrite core RAM   │
  │  Type 30 CRT display            │
  │  $120,000 (~$1.1M 2025 dollars) │
  └──────────────┬──────────────────┘
                 │
        ┌────────▼────────┐
        │  Spacewar! (1962)│
        │  Steve Russell   │
        │  Martin Graetz   │
        │  Wayne Wiitanen  │
        └────────┬────────┘
                 │
   Two-player: each ship has thrust,
   rotation, fire. Central star has
   gravity. Limited fuel and torpedoes.
   Switches on front panel = controls.
```

**Why it matters technically:**
- Gravity simulation in real time in 1962 — Russell wrote a stellar-mass gravity calculation running at display refresh rate
- The star field background was added by Peter Samson: he computed actual star positions from an ephemeris — astronomically accurate
- First game to have a physics simulation as a core mechanic (not just moving sprites)
- Spread virally across PDP-1 installations without distribution infrastructure — paper tape copies shared between labs

**Cultural significance:**
Stewart Brand's famous 1972 Rolling Stone article "Spacewar: Fanatic Life and Symbolic Death Among the Computer Bums" coined the term "hacker" in its celebratory sense. The thesis: Spacewar! demonstrated that computers were not just tools for the military-industrial complex — they could be **toys**, and that reframing would eventually drive the entire consumer software industry.

The MIT hacker ethic: information wants to be free, code should be shared, and the playful exploration of a system's limits is the highest form of intellectual engagement. This culture flows directly to the early Homebrew Computer Club → Apple → Linux → open source → GitHub lineage.

---

### Ralph Baer and the Magnavox Odyssey (1972)

While MIT hackers were using million-dollar mainframes, Ralph Baer at Sanders Associates (defense contractor) was asking a different question: can you display something interactive on a consumer TV?

```
ODYSSEY ARCHITECTURE — PURE ANALOG
═════════════════════════════════════

  ┌──────────────────────────────────┐
  │  Magnavox Odyssey (1972)         │
  │                                  │
  │  NO CPU. NO ROM. NO MICROCHIP.   │
  │                                  │
  │  Discrete transistor/resistor    │
  │  circuits generating:            │
  │  - Two vertical lines (players)  │
  │  - One square dot (ball)         │
  │  - Horizontal line (field)       │
  │                                  │
  │  Controls: potentiometers        │
  │  (knobs) → voltage → position    │
  │                                  │
  │  Score: MANUAL. Players use      │
  │  poker chips to track score.     │
  │  The machine cannot count.       │
  └──────────────────────────────────┘
          │
          │  Color and context added by:
          ▼
  ┌──────────────────────────────────┐
  │  Plastic screen overlays         │
  │  (transparent sheets taped to TV)│
  │  12 games = 12 overlays          │
  │  Tennis overlay, ski slope, etc. │
  └──────────────────────────────────┘
```

Baer filed his patent in 1966. This matters because Atari's Nolan Bushnell later claimed he conceived Pong independently — but he had demonstrably seen the Odyssey demo at a trade show before tasking Al Alcorn with building Pong. Magnavox won the subsequent patent infringement suit and collected royalties from nearly every console manufacturer for two decades.

---

### Atari Pong (1972 arcade / 1975 home) — From Analog to Chips

Nolan Bushnell's genius was not invention but commercialization. Pong's arcade cabinet (1972) used a custom IC to implement what Baer had done with discrete components. The home version (1975) went further: a single dedicated chip, the "Pong on a chip" (AY-3-8500 by General Instrument), did everything — generating video signals, tracking score, detecting collisions.

This is the transition that matters: **discrete logic → dedicated silicon → programmable CPU**. Each step made games cheaper to produce and more complex to play.

---

## Section 2: The Arcade Golden Age (1978–1983)

```
ARCADE ECONOMICS MODEL
═══════════════════════

  ┌──────────────────────────────────────────────────────────┐
  │  MANUFACTURER                                            │
  │  Taito, Midway, Namco, Atari, Williams, Bally            │
  │  Makes PCB (printed circuit board) + cabinet             │
  │  Sells to: operator (NOT end user)                       │
  └──────────────────┬───────────────────────────────────────┘
                     │ sells cabinet $1,500–$3,000
                     ▼
  ┌──────────────────────────────────────────────────────────┐
  │  OPERATOR (location owner or route operator)             │
  │  Buys cabinets, places in arcades, bars, pizza places    │
  │  Revenue: quarters. Split with location: ~50/50           │
  │  Typical payback period: 6–18 months                     │
  │  PCB SWAP MODEL: buy new PCB for existing cabinet        │
  │  when game gets stale — major cost reducer               │
  └──────────────────┬───────────────────────────────────────┘
                     │ revenue share
                     ▼
  ┌──────────────────────────────────────────────────────────┐
  │  LOCATION (arcade, convenience store, bowling alley)     │
  │  Gets: foot traffic, revenue share, no capital risk      │
  └──────────────────────────────────────────────────────────┘

  KEY INSIGHT: The operator's incentive is coins-per-minute,
  not player satisfaction. Ideal arcade game: fun enough to
  insert another quarter, hard enough to not last long.
  Difficulty ramp calibrated to exactly this.
```

### Space Invaders (1978) — Taito, Tomohiro Nishikado

The first game to be microprocessor-driven at scale. Nishikado used an Intel 8080 (same chip as the Altair). He had to design custom hardware to get the display performance he needed — a hardware sprite system that didn't exist yet. He designed the chips himself.

**Technical novelty that became standard:**
- The invaders slow down as they're eliminated — not by design initially; the Z80 (later port) had to calculate fewer collision points, so the main loop ran faster with fewer enemies alive. Players noticed the game speeding up as a difficulty curve. Nishikado kept it.
- First game to track and display a high score persistently
- Caused a 100-yen coin shortage in Japan in 1978 — Bank of Japan had to quadruple production

**The Loop Problem:** Space Invaders was the first game with a documented infinite loop phenomenon. Players who survived long enough (rare at first) found the game simply restarted. The concept of "beating" an arcade game via loops became arcade culture vocabulary.

### Pac-Man (1980) — Namco, Toru Iwatani

```
PAC-MAN GHOST AI STATE MACHINE
════════════════════════════════

  Each ghost has 3 states:
  ┌─────────────┐   ┌─────────────┐   ┌─────────────┐
  │   SCATTER   │   │    CHASE    │   │ FRIGHTENED  │
  │             │   │             │   │             │
  │ Move toward │   │ Move toward │   │ Random walk │
  │ home corner │   │ Pac-Man     │   │ Slower speed│
  │ (fixed tile)│   │ (algorithm  │   │ Can be eaten│
  │             │   │  varies by  │   │             │
  │ Blinky:NE   │   │  ghost)     │   │ Triggered by│
  │ Pinky:NW    │   │             │   │ power pellet│
  │ Inky:SE     │   │ Timers      │   │ (flashing=  │
  │ Clyde:SW    │   │ control     │   │ ending soon)│
  └──────┬──────┘   │ transitions │   └─────────────┘
         │          └──────┬──────┘
         └─────────────────┘
                  ↑
          Level-specific timer
          controls scatter/chase
          alternation schedule

  CHASE ALGORITHMS (each ghost different):
  ┌────────┬─────────────────────────────────────────────┐
  │ Blinky │ Targets Pac-Man's exact tile (direct chase) │
  │ Pinky  │ Targets 4 tiles AHEAD of Pac-Man's facing  │
  │ Inky   │ Vector from Blinky + Pinky offset (complex) │
  │ Clyde  │ Direct chase if far; retreats if close <8t  │
  └────────┴─────────────────────────────────────────────┘

  RESULT: Emergent complex behavior from simple per-ghost rules.
  "Patterns" exist because scatter targets are deterministic —
  skilled players memorized scatter-phase routes to clear boards
  without using power pellets.
```

**Cultural shift:** Pac-Man was deliberately designed for a broader audience — Iwatani wanted women in arcades. The eating mechanic, non-military theme, and character design worked. The demographics of arcade visitors shifted noticeably. The licensed merchandise (lunchboxes, cartoons, hit pop songs) showed that games could be cultural IP, not just entertainment machines.

### Donkey Kong (1981) — Miyamoto, Nintendo

Shigeru Miyamoto's first game design. The innovation: platform-based narrative structure. The player has a goal (rescue Pauline) that motivates traversal. Donkey Kong introduced:
- **Narrative framing** in an arcade game (not just "eliminate enemies")
- **Level-as-character** — each level looks different, tells a different part of the scenario
- **The platformer genre** — side-scroll with jumping as primary mechanic

Nintendo licensed it to Coleco for home play and the relationship that eventually became the NES was seeded here.

### Vector Displays vs. Raster Displays

```
DISPLAY TECHNOLOGY SPLIT (1978–1983)
══════════════════════════════════════

  RASTER (most games)              VECTOR (Atari, Cinematronics)
  ═══════════════════              ════════════════════════════

  ┌────────────────────┐          ┌────────────────────┐
  │ Scan lines top-to- │          │ Electron beam draws │
  │ bottom, left-right │          │ lines point-to-point│
  │ Fixed resolution   │          │ NOT pixel grid      │
  │ 256×224 typical    │          │ Infinitely sharp    │
  └────────────────────┘          └────────────────────┘

  Pac-Man, Donkey Kong,           Asteroids (1979)
  Space Invaders                  Battlezone (1980)
  Galaga (1981)                   Tempest (1981)
  Centipede (1980)                Star Wars (1983)

  Sprites: hardware-managed       "Objects": just vectors
  tiles composited per            no sprite limit but
  scan line                       can't fill areas easily

  WHY VECTORS DIED: Color raster got cheaper and richer.
  Vectors can't do filled polygons without massive HW cost.
  By 1984 all new cabinets were raster.
```

### What Killed Arcades

The standard story — "home consoles replaced arcades" — is too simple. The actual mechanism:

1. **Atari crash (1983)** — operator confidence in the PCB-swap revenue model collapsed when consumers could play comparable games at home. Operators stopped buying new cabinets.
2. **Quality collapse** — ET (1982) and a flood of shovelware destroyed consumer trust. Operators who hadn't already pulled back did so now.
3. **Suburban mall restructuring (1980s)** — family entertainment zones replaced the grimy standalone arcade. The economics of the standalone arcade were already marginal.

Arcades didn't die immediately — fighting game arcades (Street Fighter II, 1991; Mortal Kombat, 1992) had a second wind. But the PCB-swap model was gone. By 2000 the freestanding arcade was effectively dead in the US (Japan's arcade culture persisted much longer via UFO catchers and rhythm games).

---

## Section 3: Console Genealogy — Full Technical History

```
CONSOLE GENEALOGY: HARDWARE → MARKET IMPACT
═════════════════════════════════════════════

1977  ┌─────────────────────────────────────────────────────┐
      │  Atari 2600                                         │
      │  MOS 6507 @ 1.19 MHz (crippled 6502)                │
      │  128 BYTES RAM (not KB — BYTES)                     │
      │  TIA chip: Television Interface Adapter             │
      │  SCANLINE RACING: programmer writes TIA registers   │
      │  mid-scanline to change colors per line             │
      │  No sprite hardware — TIA has 2 players, 1 ball     │
      │  Game = ROM cartridge (2–4 KB typical)              │
      └─────────────────────────────────────────────────────┘
              │
              │  Sold 30M units. Changed consumer electronics.
              │  Then: ET (1982), Pac-Man port (1982) = CRASH
              ▼
1983  ┌─────────────────────────────────────────────────────┐
      │  ATARI CRASH                                        │
      │  Root cause: NO quality control. Atari licensed     │
      │  anything and everything. Market flooded with       │
      │  shovelware. Consumer trust = 0.                    │
      │  Industry revenue: $3.2B (1983) → $100M (1985)     │
      │  Everyone assumed video games were a fad.           │
      └─────────────────────────────────────────────────────┘
              │
              ▼
1985  ┌─────────────────────────────────────────────────────┐
      │  Nintendo NES (Famicom 1983 Japan, NES 1985 US)     │
      │  Ricoh 2A03 @ 1.79 MHz (6502 variant, no decimal)  │
      │  2 KB RAM + 2 KB VRAM                               │
      │  PPU: Picture Processing Unit — hardware sprites    │
      │  64 sprites, 8 per scanline, 16 colors from 52      │
      │  MAPPER CHIPS in cartridges extend address space:   │
      │    MMC1 (1MB+), MMC3 (add IRQ for scroll effects)   │
      │  KEY INNOVATION: Nintendo Seal of Quality           │
      │    - Lockout chip (10NES) prevents unlicensed carts │
      │    - Nintendo approves every game released          │
      │    - Publishers pay per-cart manufacturing fee      │
      │    - Quality floor enforced by economic gatekeeping │
      └─────────────────────────────────────────────────────┘
              │
              │  Revived industry. 62M units worldwide.
              │  Super Mario Bros. (1985): killer app that
              │  moved hardware. Platform game perfected.
              ▼
1989  ┌─────────────────────────────────────────────────────┐
      │  Sega Genesis (Mega Drive)                          │
      │  Motorola 68000 @ 7.6 MHz (same as Mac, Amiga)      │
      │  Zilog Z80 @ 3.58 MHz (sound co-processor)          │
      │  64 KB RAM + 64 KB VRAM                             │
      │  "BLAST PROCESSING" — Sega marketing term           │
      │  Not technically meaningful. The 68000 could        │
      │  address bus during DMA, unlike SNES. Sega made     │
      │  this sound like a performance multiplier.          │
      │  Actual advantage: faster CPU for some genres.      │
      └─────────────────────────────────────────────────────┘
      ┌─────────────────────────────────────────────────────┐
1990  │  Super Nintendo (SNES)                              │
      │  Ricoh 5A22 @ 3.58 MHz (65816 variant, 16-bit)      │
      │  128 KB RAM + 64 KB VRAM                            │
      │  MODE 7: hardware matrix transform applied to a     │
      │  single background layer — rotation + scaling       │
      │  Used for F-Zero road, Mario Kart track, etc.       │
      │  Not true 3D: single plane transformed per frame    │
      │  DSP chips in some cartridges for 3D assist         │
      │  (Super Mario Kart DSP-1, Star Fox Super FX)        │
      └─────────────────────────────────────────────────────┘
              │
              │  16-bit war: Genesis had head start + Sonic.
              │  SNES had Mode 7, better sound, Donkey Kong
              │  Country (pre-rendered 3D sprites, 1994).
              │  SNES won on quality; Genesis on library/price.
              ▼
1994  ┌─────────────────────────────────────────────────────┐
      │  Sony PlayStation                                   │
      │  MIPS R3000A @ 33 MHz                               │
      │  2 MB RAM + 1 MB VRAM                               │
      │  GEOMETRY TRANSFORMATION ENGINE: dedicated 3D       │
      │    polygon pipeline, ~360K polygons/sec             │
      │  CD-ROM (700 MB vs cartridge 32 MB MAX)             │
      │  CD cost: $1–2 to press vs $15–25 for cartridge     │
      │  RESULT: Sony could undercut Nintendo retail price  │
      │  by $10 and still make more margin                  │
      │  How Sony got here: Nintendo licensed Sony to make  │
      │  a CD add-on, then canceled the deal. Sony pivoted  │
      │  to compete directly.                               │
      └─────────────────────────────────────────────────────┘
      ┌─────────────────────────────────────────────────────┐
1996  │  Nintendo 64                                        │
      │  MIPS R4300i @ 93.75 MHz (64-bit)                   │
      │  4 MB RDRAM (fast but expensive / limited)          │
      │  Reality Signal Processor: geometry + rasterizer    │
      │  CARTRIDGE holdout — no CD-ROM                      │
      │    Nintendo's stated reason: load times             │
      │    Actual result: Square goes to Sony (Final        │
      │    Fantasy VII). Huge library gap.                  │
      │  Super Mario 64: 3D platformer as reference design  │
      │  Ocarina of Time: Z-targeting, context-sensitive    │
      │  actions — copied by every 3D action game since     │
      └─────────────────────────────────────────────────────┘
              │
              ▼
2000  ┌─────────────────────────────────────────────────────┐
      │  PS2 / Dreamcast / Xbox (2000–2001 window)          │
      │  DREAMCAST (1999): first online-capable console     │
      │    56K modem built-in, browser, online gaming       │
      │    Piracy via CD-R killed it before its time        │
      │  PS2 (2000): Emotion Engine @ 294 MHz               │
      │    DVD player Trojan horse — cheapest DVD player    │
      │    on market at launch. People bought it as DVD     │
      │    player and discovered gaming.                    │
      │    155M units — best-selling console ever           │
      │  XBOX (2001): Microsoft's entry                     │
      │    Intel Pentium III @ 733 MHz + NVIDIA GPU         │
      │    8 GB HDD — first console with persistent storage │
      │    HALO: COMBAT EVOLVED — FPS as console killer app │
      │    Xbox Live (2002): $50/yr subscription, online MP │
      │    Established: online play requires paid tier      │
      └─────────────────────────────────────────────────────┘
              │
              ▼
2005  ┌─────────────────────────────────────────────────────┐
      │  Xbox 360 / PS3 / Wii (2005–2006)                   │
      │  XBOX 360 (2005): first to HD (720p/1080i)          │
      │    3-core PowerPC @ 3.2 GHz, ATI Xenos GPU          │
      │    Red Ring of Death: thermal design failure        │
      │    Microsoft replaced 54% of units; $1.15B charge  │
      │  PS3 (2006): Cell processor                         │
      │    1 PPE (PowerPC) + 7 SPE vector units             │
      │    Extremely difficult to program                   │
      │    Blu-ray Trojan horse (vs HD-DVD on 360 optional) │
      │    Won the format war — Blu-ray standard today      │
      │  WII (2006): 729 MHz Broadway (PowerPC G3)          │
      │    Motion controls (Wiimote/MotionPlus)             │
      │    1/5 the GPU power of competitors                 │
      │    100M units: casual gaming revolution             │
      │    Grandparents playing Wii Sports = cultural moment│
      └─────────────────────────────────────────────────────┘
              │
              ▼
2013  ┌─────────────────────────────────────────────────────┐
      │  PS4 / Xbox One (2013) — x86 Commoditization        │
      │  BOTH: AMD x86-64 CPU + AMD GCN GPU (essentially    │
      │    PC hardware in a box)                            │
      │    8 core Jaguar @ 1.6–1.75 GHz                     │
      │    8 GB GDDR5 (PS4) / DDR3+ESRAM (Xbox One)         │
      │  SIGNIFICANCE: x86 ended the era of alien hardware  │
      │    Development ported trivially. PS4 dev kit = PC.  │
      │  Online subscription normalized: PS Plus mandatory  │
      │    for online play (Sony copied Xbox Live model)    │
      │  Digital distribution: 30–40% of sales digital     │
      └─────────────────────────────────────────────────────┘
              │
              ▼
2020  ┌─────────────────────────────────────────────────────┐
      │  PS5 / Xbox Series X — SSD as Architecture          │
      │  PS5: custom AMD Zen 2 + RDNA 2                     │
      │    5.5 GB/s SSD (custom NVMe, ~100× PS4 HDD)        │
      │    No loading screens = design philosophy change    │
      │    Ratchet & Clank: Rift Apart — instant dimension  │
      │    shifts impossible on HDD-era hardware            │
      │  XBOX SERIES X: similar specs                       │
      │    GAME PASS: $10–$15/mo, 300+ game catalog         │
      │    Day-one first-party on Game Pass                 │
      │    Microsoft's shift: platform → subscription       │
      │    Azure backend: xCloud streaming ~1080p/60        │
      │    Bought Bethesda ($7.5B), Activision ($68.7B)     │
      └─────────────────────────────────────────────────────┘
```

---

## Section 4: PC Gaming — The id Software Tech Tree

PC gaming evolved on a completely separate track from consoles. The critical genealogy runs through a single studio.

```
ID SOFTWARE TECHNICAL LINEAGE
══════════════════════════════

  Commander Keen (1990)
  ├── EGA smooth scrolling on PC — previously "impossible"
  └── John Carmack's adaptive tile refresh: only redraw changed tiles

            ↓

  Wolfenstein 3D (1992)
  ├── RAYCASTING engine (NOT ray tracing — completely different)
  │   ┌─────────────────────────────────────────────────────┐
  │   │  RAYCASTING ALGORITHM                               │
  │   │  For each screen column (320 wide):                 │
  │   │  1. Cast a ray from player position at that angle   │
  │   │  2. Find first wall intersection via DDA algorithm  │
  │   │  3. Wall distance → column height on screen         │
  │   │  4. Texture column mapped proportionally            │
  │   │  CONSTRAINT: walls must be 90° grid-aligned         │
  │   │  CONSTRAINT: no floor/ceiling textures (colored)    │
  │   │  CONSTRAINT: no height variation in walls           │
  │   └─────────────────────────────────────────────────────┘
  ├── Shareware distribution: Episode 1 free, buy E2+E3
  │   → invented the commercial shareware model
  └── Apogee as distributor — the template for digital distribution

            ↓

  DOOM (1993)
  ├── BSP TREES replace simple raycasting
  │   ┌─────────────────────────────────────────────────────┐
  │   │  BSP (Binary Space Partition) TREE                  │
  │   │  Precompute level geometry into a tree where:       │
  │   │  - Each node is a dividing plane                    │
  │   │  - Left subtree = "front" of plane                  │
  │   │  - Right subtree = "back" of plane                  │
  │   │  At runtime: traverse back-to-front (painter's algo)│
  │   │  ALLOWS: variable floor/ceiling height              │
  │   │  ALLOWS: non-orthogonal walls (still 2D map)        │
  │   │  STILL: no true 3D (map is 2D, rendered 2.5D)       │
  │   └─────────────────────────────────────────────────────┘
  │   <!-- @editor[bridge/P2]: BSP trees are a direct application of space partitioning / computational geometry — the learner with MIT TCS background knows BSP trees from the computational geometry literature (de Berg et al.); a one-line note that BSP tree construction is O(n²) in worst case but empirically fast for architectural geometry, and that the same data structure appears in ray tracers (kd-trees are a BSP variant) and collision detection, would tie this to the learner's CS foundations -->
  ├── Multiplayer via IPX (LAN) and serial/modem
  ├── WAD file format → moddability → huge community
  │   WAD = "Where's All the Data" — separated engine from assets
  │   First major game designed to be modded from day one
  └── IWAD/PWAD distinction: commercial vs fan-made levels

            ↓

  Quake (1996)
  ├── TRUE 3D: BSP + PVS (Potentially Visible Set)
  │   ┌─────────────────────────────────────────────────────┐
  │   │  PVS = precomputed visibility set per BSP leaf       │
  │   │  At runtime: look up which leaves are visible from  │
  │   │  current player leaf → only render those            │
  │   │  True volumetric 3D: floors above floors possible   │
  │   │  Lighting: static lightmaps baked offline           │
  │   └─────────────────────────────────────────────────────┘
  ├── GLQuake (1996): first OpenGL-accelerated game
  │   Required a 3Dfx Voodoo card ($200) — created the
  │   consumer GPU market as we know it
  ├── QuakeC scripting — game logic in interpreted language
  ├── CLIENT-SERVER NETWORKING: authoritative server model
  │   that became the standard for competitive FPS
  │   Lag compensation (later), client-side prediction — all
  │   Quake-originated patterns
  └── TCP/IP native → internet play without LAN
           → QuakeWorld (1996): delta compression,
             client-side prediction invented here
```

**Half-Life (1998):** Valve's entry built on the Quake engine. The innovation was narrative integration — the game world is continuous, no cutscenes cut away from first-person perspective, NPCs react to the player contextually. Every subsequent FPS narrative structure traces to Half-Life. Valve also released the SDK immediately, spawning Team Fortress (mod), Counter-Strike (mod), and the modding-as-R&D-pipeline model.

### RTS: Dune II → StarCraft

```
RTS LINEAGE
════════════

  Dune II (1992, Westwood)
  └── Invented the genre conventions:
      base building, resource harvesting, unit production,
      fog of war, mouse-click unit orders

          ↓

  Warcraft: Orcs & Humans (1994, Blizzard)
  └── Fantasy reskin with more personality.
      Multiplayer via IPX.

          ↓

  Command & Conquer (1995, Westwood)
  └── FMV cutscenes, parallel campaign structure

          ↓

  StarCraft (1998, Blizzard)
  ├── Three asymmetric races (Terran/Zerg/Protoss)
  │   Each with different macro economy mechanics
  ├── APM (Actions Per Minute) as skill metric
  │   Top Korean pros: 300–400 APM sustainable
  │   That's 5–7 distinct keyboard/mouse actions per second
  ├── Micro vs Macro distinction:
  │   MACRO: base management, production queues, expansion
  │   MICRO: individual unit control in engagements
  │   (Marine micro: "stutter-stepping" to maximize DPS)
  └── Brood War (1998 expansion): rebalanced to near-perfection
      Korean pro scene: 1999–2012 dominant esport
```

### Steam (2003): Valve's Platform Pivot

Steam launched as DRM for Counter-Strike — Valve needed a way to force updates and fight cheating. Initially hated by players (slow, required internet for single-player). Valve bet that the convenience value of digital distribution would overcome initial resistance.

The bet paid off spectacularly. By 2010 Steam had 30M users. By 2020: 120M active accounts, 30,000 titles, $4.3B annual revenue estimated. Valve takes 30% of every sale — the App Store model, but for PC games, 5 years before the App Store.

Key structural decision: **Steam Workshop** (user-created content distribution integrated into platform) and **Steam Community Market** (real-money trading of in-game items, Valve takes a cut). The item economy in CS:GO/Dota 2 generates hundreds of millions annually for Valve while adding zero development cost.

---

## Section 5: Online Multiplayer — From MUDs to Metaverse

```
ONLINE GAMING EVOLUTION
════════════════════════

  1978  MUDs (Multi-User Dungeons)
        └── Text-based, university Unix systems
            Roy Trubshaw + Richard Bartle, Essex University
            Persistent world, multiple simultaneous users
            Template for all MMORPGs

  1985  BBS online games
        └── Tradewars 2002, Legend of the Red Dragon
            Synchronous + async play, 1200 baud limits

  1993  DOOM multiplayer via modem + IPX LAN
        └── Deathmatch invented. "Frag" enters vocabulary.

  1996  Quake: first internet-native competitive FPS
        └── QuakeWorld with lag compensation
            LAN parties: bring-your-own-PC, rented venue

  1997  Ultima Online — first mainstream MMORPG
        └── Persistent world, player-driven economy
            Player Killing (PKing) controversy
            Bartle's player types (see below)

  1999  EverQuest — "EverCrack"
        └── Grinding mechanic. First addiction discourse.
            Economists studied EQ economy (Castronova 2001)

  2002  Xbox Live
        └── Console online subscription normalized
            Friends lists, voice chat, achievements prototype

  2004  World of Warcraft
        └── Peak: 12M subscribers (2010)
            Raiding: 40-person coordination problem

  2004  Counter-Strike 1.6 competitive scene solidifies
        └── AWP, economy meta, ranked servers

  2009  League of Legends → MOBA genre dominance
        └── Riot's platform: PC client, ranked system

  2012  Diablo III RMAH: real-money auction house
        └── Experiment in formalized RMT — failed, removed

  2017  Battle royale explosion (PUBG/Fortnite)
        └── 100 players, one survives
```

### Bartle's Player Types (1996)

Richard Bartle's analysis of MUD player behavior produced four archetypes that remain the most widely-cited taxonomy in game design:

| Type | Motivation | Action orientation | Representative |
|------|------------|-------------------|----------------|
| **Achievers** | Points, levels, completion | Acting on world | Trophy hunters, 100% completionists |
| **Explorers** | Discovery, lore, hidden systems | Discovering world | Map completers, lore players |
| **Socializers** | Relationships, community | Interacting with players | Guild officers, RP communities |
| **Killers** | Dominance, impact on others | Acting on players | PvP griefers, competitive ranked |

The distribution matters for game design: an MMO needs enough Socializers to hold communities, enough Achievers to drive gear progression, enough Explorers to justify content investment, and just enough Killers to create tension without driving everyone else away.

### World of Warcraft as Organizational Problem

WoW raiding at the 40-man level (Classic/Vanilla) was a coordination problem that had no precedent in game design:

- 40 people with heterogeneous skill levels, schedules, and hardware
- 2–4 hour time commitment per session
- 3–4 sessions per week at progression level
- Strict role distribution: tanks, healers, DPS at defined ratios
- Guild banks, DKP (Dragon Kill Points) loot systems
- Officer hierarchy with clear domain ownership

WoW guilds invented their own HR practices. Raid leaders evaluated performance data from combat logs before modern esports analytics existed. The coordination patterns were isomorphic to production operations management — resource allocation under time pressure with role-specialized team members.

---

## Section 6: Mobile Gaming Economics

```
MOBILE GAMING REVENUE FUNNEL (F2P MODEL)
══════════════════════════════════════════

  Total Downloads
  ─────────────────────────────────────────  100%
  │
  │ 97–98% never spend money
  │
  Active players (monthly)
  ─────────────────────────────────────────   40%
  │
  │ 95% of these never convert
  │
  Paying players ("minnows") ← $1–$10 total  ~2–3%
  ─────────────────────────────────────────
  │
  │ 90% of paying players are minnows
  │
  "Dolphins" ← $10–$100/month               ~0.2%
  ─────────────────────────────────────────
  │
  "Whales" ← $100–$10,000+/month            ~0.01–0.1%
  ─────────────────────────────────────────
  │
  └── Whales generate 50–70% of total revenue
      Top 10% of paying players = 90% of revenue

  KEY METRICS:
  ┌────────────────────────────────────────────────────┐
  │  ARPU  = Average Revenue Per User (total)          │
  │  ARPPU = Average Revenue Per Paying User           │
  │  LTV   = Lifetime Value (per user, discounted)     │
  │  DAU   = Daily Active Users                        │
  │  MAU   = Monthly Active Users                      │
  │  D1/D7/D30 = Day 1/7/30 retention rates            │
  │                                                    │
  │  CPI (Cost Per Install) < LTV = profitable         │
  │  Typical mobile CPI: $1–5 (casual), $10–30 (mid)  │
  │  Typical mobile LTV: varies wildly; $1–200+        │
  └────────────────────────────────────────────────────┘

  MECHANICS DESIGNED FOR WHALE EXTRACTION:
  ├── Energy timers: play for free but wait 4hrs or pay
  ├── Gacha/loot boxes: variable ratio reinforcement schedule
  │   (same psychology as slot machines; illegal in Belgium/NL)
  ├── FOMO events: limited-time skins/characters
  ├── Social pressure: guild contribution requirements
  └── Power creep: old purchases made obsolete by new releases
```

<!-- @editor[bridge/P2]: The F2P whale economics maps cleanly to network effects and price discrimination (first/second/third degree) — the learner's background in platform economics would recognize that F2P is perfect price discrimination (each player pays their reservation price via whale/dolphin/minnow segmentation) combined with a two-sided platform problem (more players → better match quality → more engagement → more spending); this bridge from platform economics to the ARPU funnel would resonate -->
**App Store Price Compression:** When the App Store launched in 2008, Myst — the benchmark prestige game — cost $5.99. Within six months, $.99 was the ceiling for perceived "fair" pricing. The entire industry collapsed to $0.99 or free + IAP. The discovery algorithm rewarded new releases, creating a treadmill where sustainable revenue required IAP rather than unit sales.

**Genshin Impact (2020)** as the inflection point: a console-quality open-world RPG, free to play, monetized through gacha character pulls. Made $2.8B in first year. Demonstrated that the quality ceiling of mobile games was no longer a constraint — the platform could deliver AAA experiences with F2P monetization.

---

## Section 7: Esports — From Korean Internet Cafes to $40M Prize Pools

```
ESPORTS INFRASTRUCTURE STACK
══════════════════════════════

  ┌──────────────────────────────────────────────────────────┐
  │  GAMES (the IP)                                          │
  │  StarCraft BW, CS:GO, LoL, Dota 2, Fortnite, Valorant  │
  └──────────────────────────┬───────────────────────────────┘
                             │
  ┌──────────────────────────▼───────────────────────────────┐
  │  ORGANIZERS / LEAGUES                                    │
  │  Riot (LCS/LCK/LEC) — publisher-run                     │
  │  Valve (The International) — community-funded prize pool │
  │  ESL/BLAST/PGL — third-party tournament organizers       │
  │  Overwatch League — traditional sports franchise model   │
  └──────────────────────────┬───────────────────────────────┘
                             │
  ┌──────────────────────────▼───────────────────────────────┐
  │  TEAMS / ORGANIZATIONS                                   │
  │  Team Liquid, Cloud9, Fnatic, NAVI, T1                   │
  │  Revenue: prize money + sponsorship + merch + media      │
  │  Roster management, bootcamps, sports psychologists      │
  └──────────────────────────┬───────────────────────────────┘
                             │
  ┌──────────────────────────▼───────────────────────────────┐
  │  BROADCAST / MEDIA                                       │
  │  Twitch (Amazon, acquired 2014, $970M)                   │
  │  YouTube Gaming                                          │
  │  AfreecaTV (Korea) — precursor to Twitch                 │
  │  ESPN esports, dedicated channels                        │
  └──────────────────────────┬───────────────────────────────┘
                             │
  ┌──────────────────────────▼───────────────────────────────┐
  │  INFRASTRUCTURE                                          │
  │  Riot/Valve game servers, spectator APIs                 │
  │  LAN event arenas (KeyArena, Barclays, Mercedes-Benz)    │
  │  Production (OB trucks, replay systems, statistics)      │
  └──────────────────────────────────────────────────────────┘
```

### StarCraft: Brood War in Korea (1998–2012)

<!-- @editor[bridge/P2]: StarCraft as a partially observable stochastic game (POSG) deserves explicit framing for the TCS reader — unlike chess (perfect information) or poker (imperfect information, no real-time), SC:BW is a real-time game with fog of war, simultaneous moves, and continuous action space (unit positions, timing); this places it in a distinct complexity class from the games discussed in 00-OVERVIEW.md; AlphaStar's challenges compared to AlphaZero (chess) trace directly to these structural differences -->
The anomaly that created professional esports: South Korea in 1998 had a perfect storm — post-Asian financial crisis, government investment in PC bang (internet cafe) infrastructure, cheap gigabit broadband, and StarCraft: Brood War as the game.

**OGN (Ongamenet)** launched the first professional StarCraft league in 1999. **MBC Game** followed. The top players signed to teams backed by Korean chaebols (SK Telecom T1, KT Rolster, Samsung Khan). These were salaried athletes with coaches, practice schedules, and fan clubs.

**APM as athletic metric:** The best players sustained 300+ actions per minute for 40-minute games. Lee "Flash" Young-Ho, considered the greatest BW player, achieved 400+ sustained APM with near-perfect macro efficiency. The comparison to physical athletes is apt: the motor control requirement is genuinely athletic.

**Jaedong vs. Flash:** In 2010–2012, the rivalry between Lee "Jaedong" Jae-dong (Zerg) and Lee "Flash" Young-Ho (Terran) was followed like Ali/Frazier. OSL/MSL finals drew millions of Korean TV viewers. This comparison is not hyperbole — BW finals aired on prime-time national television.

### League of Legends — The Dominant Model

Riot's design decisions for LoL were explicitly esport-forward:
- Free to play (all champions eventually acquirable for free currency)
- Cosmetics-only monetization (no pay-to-win)
- Quarterly balance patches = evolving meta = sustained viewership
- LCS/LCK/LEC franchised leagues with revenue sharing

The regional league structure mirrors conventional sports: LCS (North America), LCK (Korea), LPL (China), LEC (Europe). Each has regular season, playoffs, and World Championship (Worlds). Peak Worlds viewership: 73M concurrent in 2020.

### Dota 2 and The International Prize Pools

Valve's approach was the inverse of Riot's: open ecosystem, minimal publisher control, community-funded prize pools via the Battle Pass (cosmetic item subscription where 25% goes to tournament prize pool).

```
THE INTERNATIONAL PRIZE POOL HISTORY
══════════════════════════════════════

  Year  │ Prize Pool  │ Winning Team
  ──────┼─────────────┼──────────────────────────────
  2011  │ $1.6M       │ Natus Vincere (Ukraine)
  2013  │ $2.9M       │ Alliance (Sweden)
  2014  │ $10.9M      │ Newbee (China)
  2015  │ $18.4M      │ Evil Geniuses (USA)
  2016  │ $20.8M      │ Wings Gaming (China)
  2017  │ $24.8M      │ Team Liquid (multi-national)
  2018  │ $25.5M      │ OG (multi-national)
  2019  │ $34.3M      │ OG (back-to-back; unprecedented)
  2021  │ $40.0M      │ Team Spirit (Russia/CIS)
  ──────┴─────────────┴──────────────────────────────

  For comparison:
  Wimbledon 2021 total purse:    $34.5M (singles: $2.3M)
  US Open golf 2021 total:       $12.5M (winner: $2.25M)
  PGA Tour season earnings cap:  ~$30M
```

### CS:GO Skins Economy and the Gambling Scandal (2016)

In 2013, Valve added weapon skins to CS:GO, tradeable on the Steam Community Market. Players could buy "cases" (loot boxes) with real money, opening them for random skins of varying rarity. Top skins ("contraband" tier) trade for thousands of dollars.

The Steam Market lets players sell skins for Steam wallet credit. Third-party sites emerged offering real-money cash-out, functioning as unregulated gambling sites. In 2016, two popular YouTube personalities (ProSyndicate, Phantoml0rd) were exposed for owning a skin gambling site they promoted without disclosure while winning suspiciously often. The scandal triggered FTC investigations, lawsuits against Valve, and state-level regulatory scrutiny. Belgium subsequently declared loot boxes illegal gambling.

### Battle Royale and Fortnite's Platform Innovation

**PUBG (2017)** operationalized the battle royale concept (100 players drop onto a map, last person alive wins) into a retail product. The map shrinking via "blue zone" mechanic created natural time pressure without arbitrary timers.

**Fortnite (2017, Epic Games)** added the building mechanic to the formula and made it free to play. The monetization innovation: **the Battle Pass**.

```
BATTLE PASS MODEL vs. TRADITIONAL DLC
═══════════════════════════════════════

  TRADITIONAL DLC (pre-2017)               BATTLE PASS
  ────────────────────────────             ─────────────────────────
  $15–60 for content pack                 $10 per season (~90 days)
  Pay once, have it                       Pay per season to "unlock" rewards
  One-time revenue                        Recurring subscription revenue
  Content gate creates haves/have-nots    All players play same game;
                                          cosmetics are progression rewards
  Players annoyed by fragmentation        Players motivated to play daily
                                          to progress tier
  ─────────────────────────────────────────────────────────────────
  Fortnite generated $9B in 2018–2019 from V-Bucks (virtual currency)
  and Battle Pass purchases.
  Epic's revenue: $5.1B in 2021 on Fortnite alone.
```

**Live events as media:** Fortnite's in-game live events (Travis Scott concert 2020: 12.3M concurrent viewers; Ariana Grande 2021: 7.9M concurrent) established the game as broadcast medium. This had no precedent.

---

## Section 8: Game Design as Craft

### MDA Framework — Hunicke, LeBlanc, Zubek (2004)

```
MDA FRAMEWORK
══════════════

  DESIGNER                                         PLAYER
  perspective                                      perspective
      │                                                │
      ▼                                                ▼
  ┌──────────────┐   generate  ┌──────────────┐  produce  ┌──────────────┐
  │  MECHANICS   │ ──────────► │   DYNAMICS   │ ─────────►│ AESTHETICS   │
  │              │             │              │            │              │
  │ Rules of the │             │ Emergent     │            │ Emotional    │
  │ game system  │             │ behavior at  │            │ response in  │
  │              │             │ runtime      │            │ the player   │
  │ e.g., chess  │             │              │            │              │
  │ piece moves  │             │ Opening      │            │ Tension of   │
  │              │             │ theory,      │            │ endgame      │
  │              │             │ blunders,    │            │              │
  │              │             │ positional   │            │              │
  │              │             │ pressure     │            │              │
  └──────────────┘             └──────────────┘            └──────────────┘

  Key insight: Designers create mechanics. They cannot directly
  control dynamics or aesthetics — only engineer toward them.

  "Aesthetics" in MDA = emotional goals, not visual appearance:
  Sensation, Fantasy, Narrative, Challenge, Fellowship,
  Discovery, Expression, Submission (masochism/idle)
```

### Core Loop Architecture

```
GAME LOOP HIERARCHY
════════════════════

  ┌─────────────────────────────────────────────────────┐
  │  META-GAME LOOP (weeks/months)                      │
  │  Progression: level up, unlock, rank increase       │
  │  Social: guild, leaderboard, season pass            │
  └───────────────────┬─────────────────────────────────┘
                      │ rewards from
  ┌───────────────────▼─────────────────────────────────┐
  │  PROGRESSION LOOP (hours/sessions)                  │
  │  Quest chain, dungeon clear, battle pass tier       │
  │  "Always be working toward the next reward"         │
  └───────────────────┬─────────────────────────────────┘
                      │ advances
  ┌───────────────────▼─────────────────────────────────┐
  │  CORE LOOP (minutes)                                │
  │  The basic verb: shoot-loot-upgrade, match-buy-play │
  │  Must be intrinsically satisfying at base           │
  │  The loop players describe when they say "just one  │
  │  more" — e.g., Tetris, Candy Crush, Hades run       │
  └─────────────────────────────────────────────────────┘
```

### Key Design Theorems

**Sid Meier:** "A game is a series of interesting decisions." Corollary: any mechanic that doesn't present a genuine decision is padding.

**Richard Garfield on luck vs. skill (Magic: The Gathering):** A game of pure skill (chess) is solved once one player outskills the other enough. A game of pure luck (slot machine) has no depth. The optimum for sustained engagement: luck provides variance that keeps weaker players competitive, while skill provides consistent expected-value advantage over time. MTG draft format: the best players win ~70% over large sample sizes despite random card draws.

**Will Wright's possibility space:** SimCity's cities, The Sims' stories, Spore's creatures — Wright designs systems that generate possibility spaces for players to explore, then steps back. The "game" is the space itself, not a prescribed path through it. Contrast with linear narrative games where the designer controls the journey.

**Roguelike design principles:**
- **Permadeath** — not punishment, but anti-save-scumming. Forces genuine decisions because reversibility is removed. A save-anywhere system means the player can always undo mistakes; permadeath means mistakes have weight.
- **Procedural generation** — Binding of Isaac, Hades, Spelunky all generate layouts differently each run. The skill is in reading and adapting to novel configurations, not memorizing optimal paths.
- **Meta-progression** — modern roguelikes (Hades model) add permanent unlocks across runs, providing the "progression loop" layer above the "core loop."

**Dark Souls vs. Adaptive Difficulty:** Dark Souls refuses to reduce difficulty based on player failure count. The prevailing design philosophy in 2009 was "keep failure from frustrating players." FromSoftware's bet: the difficulty IS the product. Overcoming a boss after 40 attempts is a narrative — the player writes it. The adaptive difficulty approach removes that narrative. Dark Souls spawned Souls-like as a genre and returned "mastery" as a mainstream game design value after 15 years of accessibility-driven casualization.

---

## Section 9: Computational Milestones — Games as AI Benchmarks

Games are measurable, deterministic (or precisely probabilistic), and have centuries of human performance data. They are ideal AI benchmarks.

| Year | System | Game | Significance |
|------|--------|------|--------------|
| 1992 | TD-Gammon (Tesauro) | Backgammon | First neural net trained via TD-learning to reach expert play. Self-play RL before it had a name. |
| 1997 | Deep Blue (IBM) | Chess | Defeated Kasparov match (3.5-2.5). 200M positions/second, custom VLSI. First "computer beats world champion" moment. |
| 1997 | Logistello (Buro) | Othello | Defeated world champion Murakami 6-0. Less famous but technically cleaner than Deep Blue. |
| 2011 | Watson (IBM) | Jeopardy! | Defeated Jennings and Rutter. NLP + knowledge retrieval under time pressure. IR architecture, not generative. |
| 2016 | AlphaGo (DeepMind) | Go | Defeated Lee Sedol 4-1. Go was considered AI-hard for decades (branching factor ~250 vs chess ~35). MCTS + two deep nets. |
| 2017 | AlphaZero (DeepMind) | Chess/Shogi/Go | Trained from random play 4 hours → defeated Stockfish 8 (strongest chess engine) 28-0+72 draws. Zero human prior knowledge beyond rules. |
| 2019 | OpenAI Five | Dota 2 | Defeated OG (reigning world champions) 2-0. First AI to beat top humans in a complex 5v5 real-time game with partial observability. |
| 2019 | AlphaStar (DeepMind) | StarCraft II | Defeated top pros (Serral, MaNa). Used a different APM limit and fog-of-war than humans; controversy about the constraints. |
| 2019 | Pluribus (CMU/FAIR) | 6-player Poker | First AI to beat top pros in 6-player no-limit hold'em — the hardest poker variant for AI due to multi-agent imperfect information. Libratus (2017) had already solved heads-up limit hold'em. |

**Why these matter for software engineers:**

AlphaZero is architecturally the most important: it demonstrates that a self-improving system can surpass all human knowledge in a formally-specified domain given only the rules. The architecture (MCTS + residual CNN + self-play RL) is the direct predecessor of techniques used in modern LLM alignment (RLHF = RL from Human Feedback, which is RL from soft labels rather than self-play, but same algorithmic family).
<!-- @editor[bridge/P2]: The connection between MCTS UCB1 selection and the multi-armed bandit problem is missing — MCTS's selection policy (UCB1: Upper Confidence Bound) is a direct solution to the exploration-exploitation tradeoff from the multi-armed bandit literature (Auer-Cesa-Bianchi-Fischer 2002); for a TCS learner who has seen bandit problems, naming UCB1 explicitly and noting it provides O(√(n log n)) regret would make the "why MCTS works" story complete -->

The progression Chess → Go → StarCraft II represents increasing action space complexity, partial observability, and multi-agent dynamics. OpenAI Five solving Dota 2 is significant precisely because the game has continuous state, partial observability (fog of war), heterogeneous agents (5 different heroes per side), and extremely long time horizons (50-minute games with credit assignment across ~20,000 steps).

---

## Console Hardware Specifications — Comparison Table

| Console | CPU | RAM | Storage | Key chip | Units |
|---------|-----|-----|---------|----------|-------|
| Atari 2600 (1977) | MOS 6507 @ 1.19 MHz | 128 B | ROM cart 2–4 KB | TIA (video) | 30M |
| NES (1985) | Ricoh 2A03 @ 1.79 MHz | 2 KB | ROM cart 256K–1MB | PPU (sprites) | 62M |
| Sega Genesis (1989) | Motorola 68000 @ 7.6 MHz | 64 KB | ROM cart | VDP (video) | 30M |
| SNES (1990) | Ricoh 5A22 @ 3.58 MHz | 128 KB | ROM cart + DSP | PPU + Mode 7 | 49M |
| PlayStation (1994) | MIPS R3000A @ 33 MHz | 2 MB | CD-ROM 700 MB | GTE (3D) | 102M |
| Nintendo 64 (1996) | MIPS R4300i @ 93.75 MHz | 4 MB RDRAM | Cartridge 64 MB | RSP (3D) | 33M |
| PS2 (2000) | Emotion Engine @ 294 MHz | 32 MB | DVD + HDD opt | GS (graphics) | 155M |
| Xbox (2001) | Pentium III @ 733 MHz | 64 MB DDR | DVD + 8 GB HDD | NVIDIA NV2A | 24M |
| Xbox 360 (2005) | 3× PowerPC @ 3.2 GHz | 512 MB GDDR3 | DVD + HDD opt | ATI Xenos | 84M |
| PS3 (2006) | Cell (1 PPE + 7 SPE) | 256 MB + 256 MB | Blu-ray + HDD | RSX (NVIDIA) | 87M |
| Wii (2006) | Broadway (PPC G3) @ 729 MHz | 88 MB | DVD (no DL) | Hollywood (GPU) | 101M |
| PS4 (2013) | AMD Jaguar 8-core @ 1.6 GHz | 8 GB GDDR5 | Blu-ray + HDD | AMD GCN GPU | 117M |
| Xbox One (2013) | AMD Jaguar 8-core @ 1.75 GHz | 8 GB DDR3 | Blu-ray + HDD | AMD GCN GPU | 51M |
| PS5 (2020) | AMD Zen 2 8-core @ 3.5 GHz | 16 GB GDDR6 | 825 GB NVMe SSD | AMD RDNA 2 | 50M+ |
| Xbox Series X (2020) | AMD Zen 2 8-core @ 3.8 GHz | 16 GB GDDR6 | 1 TB NVMe SSD | AMD RDNA 2 | ~20M |

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| What was the first video game? | Spacewar! (1962, MIT, PDP-1) by Steve Russell — though "first" is contested. Cathode-Ray Tube Amusement Machine (1947) is earlier but analog. |
| What caused the 1983 crash? | Atari's lack of quality control: flooded market with licensed shovelware. ET didn't cause it alone — it was a symptom. |
| What saved the industry? | Nintendo Seal of Quality — economic gatekeeping via lockout chip + publisher approval. |
| Why did N64 lose to PS1 on third-party? | Cartridge manufacturing cost ($15–25) vs CD ($1–2). Square moved Final Fantasy to PS1. Libraries diverged fatally. |
| What is "blast processing"? | Sega marketing term. The 68000 could access the bus during DMA; SNES couldn't. Not a meaningful performance multiplier. |
| Why did PS2 outsell everything? | DVD player economics. Cheapest DVD player on market at launch — people bought it as home theater hardware. |
| What is raycasting vs. ray tracing? | Raycasting (Wolfenstein 3D): cast rays until first wall hit, approximate 3D from 2D map. Ray tracing: simulate light physically, bounce multiple times. Completely different algorithms. |
| Why did id Software matter? | Tech tree: shareware distribution → BSP trees → PVS → OpenGL → client-server networking. Every FPS owes its architecture to id. |
| What is the MDA framework? | Mechanics → Dynamics → Aesthetics. Designer controls mechanics; emergent dynamics produce player emotional response. |
| What is a whale in F2P? | Player spending $100–$10,000+/month. Top 0.1% of players generating 50–70% of revenue. Entire F2P economy optimized around extracting whale spend. |
| What is the Battle Pass innovation? | Recurring seasonal subscription ($10/season) that provides cosmetic progression, replacing one-time DLC. Creates daily engagement loop + predictable recurring revenue. |
| Which AI milestone matters most for ML engineers? | AlphaZero (2017): tabula rasa self-play RL + MCTS beats all prior knowledge in Chess/Go/Shogi. Direct lineage to RLHF in LLMs. |
| When did Korea professionalize esports? | StarCraft Brood War + OGN league, 1999. Salaried players, national TV coverage, chaebol team sponsorship. |
| What is the Bartle taxonomy? | Four player types in multiplayer: Achievers (points), Explorers (discovery), Socializers (community), Killers (domination). |
| How does The International fund its prize pool? | Battle Pass IAP: 25% of all Battle Pass revenue goes to TI prize pool. Community funds its own tournament. |

---

## Common Confusion Points

**Raycasting is not ray tracing.** These terms are constantly conflated. Raycasting (Wolfenstein 3D, early Doom techniques) fires a ray from the viewpoint in the player's direction and stops at the first hit — it's a visibility algorithm approximating perspective, not a lighting algorithm. Ray tracing simulates photon physics: rays bounce off surfaces, refract through transparent objects, and accumulate color contributions. Ray tracing is O(n) more computationally expensive and wasn't feasible in real-time games until NVIDIA RTX in 2018.

**The Atari crash was about quality, not technology.** The common narrative is "home consoles killed arcades" or "the industry was disrupted." The actual cause was Atari's decision to license anything — ET, the Atari 2600 Pac-Man port — without quality review. The market became indistinguishable from the toy aisle because it literally shared shelf space with non-games. Nintendo's business insight was that the quality floor matters for platform trust, not just individual title quality.

**"3D" in the SNES/Mode 7 era was not 3D.** Mode 7 applies an affine transformation (scale + rotation, no perspective correction) to a single background plane. F-Zero's road is Mode 7. Super Mario Kart's track is Mode 7. The depth illusion comes from scaling a top-down texture, not from rendering a 3D environment. True perspective-correct 3D on SNES required DSP coprocessors in the cartridge (Super FX chip for Star Fox).

**Blast processing was marketing.** The Motorola 68000's ability to continue address-bus operations during DMA was real. Sega's advertising department turned this into "BLAST PROCESSING" implying a dramatic performance advantage. The actual difference mattered only in specific bandwidth-constrained scenarios, not as a general multiplier.

**CD-ROM did not kill cartridges because of capacity alone.** The decisive factor was manufacturing cost economics: $1–2 to press a CD vs. $15–25 to manufacture a cartridge. This gave Sony a retail margin advantage of $13–23 per unit sold, which compound across a catalog of 100+ games represents hundreds of millions in developer/publisher relationship advantages. The capacity (700 MB vs. 32–64 MB) mattered for FMV and audio, but the real kill shot was margin economics.

**Xbox Live established the paid-online-subscription norm, not innovation necessity.** There was no technical reason online multiplayer required a subscription — PC games had been doing it for free since Quake (1996). Xbox Live bundled matchmaking, voice chat, and friends lists into a $50/year service because it could, and because console owners were accustomed to paying for content. Sony initially resisted (PS3 online was free) then capitulated with PS4 (PS Plus required for online). The model transferred approximately $3B/year from gamers to platform holders at scale.

**Esports salaries are not equivalent to traditional sports.** The top LoL/CS:GO players earn $500K–$2M annually, comparable to mid-tier professional athletes in minor sports. But team organizations are often unprofitable — the Overwatch League franchise fee was $20M for rights to a competition that many teams are now exiting. Prize pool visibility (TI at $40M) obscures that most esports players earn $30K–$80K, similar to minor league baseball. The economics are still stabilizing.

**AlphaGo vs. AlphaZero are architecturally different.** AlphaGo (vs. Lee Sedol, 2016) was trained on human game records as a starting point, then refined via self-play. AlphaZero starts from tabula rasa — only the rules, no human games. The significance of AlphaZero: it found approaches to Chess that 150 years of human theory had not. Its opening repertoire included moves that were considered positionally unsound and turned out to be deeply correct.

**Battle royale as genre did not originate with PUBG.** The BR mode in Minecraft (Hunger Games servers) predated PUBG by 5+ years. The DayZ battle royale mod (Brendan Greene/PlayerUnknown, 2013) directly preceded PUBG. Greene created the standalone PUBG after working on H1Z1: King of the Kill. The genre had multiple predecessors; PUBG operationalized it at commercial scale.
