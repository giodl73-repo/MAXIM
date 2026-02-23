# Watchmaking — 01 Early Timekeeping
## Before the Escapement: Sundials, Water Clocks, and Astronomical Time

---

## The Big Picture

Every pre-mechanical timekeeping system reduces to one of three physical phenomena: the motion of celestial bodies (shadow casting, star positions), fluid flow (water, sand), or combustion (candle, incense). Each has a characteristic error source, and the engineering history of each is the story of compensating for that error.

```
PRE-MECHANICAL TIMEKEEPING TAXONOMY

┌─────────────────────────────────────────────────────────────────┐
│                    TIME MEASUREMENT METHODS                      │
│                      (before ~1280 CE)                           │
└─────────────────────────────────────────────────────────────────┘
           │                    │                    │
           ▼                    ▼                    ▼
┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐
│  ASTRONOMICAL    │  │  FLOW-BASED      │  │  COMBUSTION      │
│                  │  │                  │  │                  │
│ Sundial (shadow) │  │ Clepsydra (water)│  │ Candle clock     │
│ Gnomon           │  │ Sand glass       │  │ Incense clock    │
│ Armillary sphere │  │                  │  │ Oil lamp clock   │
│ Nocturnal        │  │                  │  │                  │
│ Astrolabe        │  │                  │  │                  │
└──────────────────┘  └──────────────────┘  └──────────────────┘
       │                      │                      │
   ERRORS:              ERRORS:               ERRORS:
   Equation of time     Pressure varies       Rate varies with
   Cloud cover          with head height      temperature,
   Latitude-specific    Temperature           humidity, draft
   Night unusable       viscosity             Fuel quality
                        Evaporation
```

The key point: **none of these methods have a natural frequency**. They measure duration by measuring something else (shadow length, water volume, wax consumed) and inferring elapsed time. This is fundamentally different from a resonant oscillator (pendulum, balance spring, quartz crystal) that counts periods.

---

## Sundials

### The Gnomon: Simplest Astronomical Clock

A gnomon is any vertical object whose shadow indicates the time of day. The simplest is a stick in the ground. The shadow moves because the Earth rotates — one full rotation in approximately 24 hours, so the shadow sweeps 360° in 24 hours, or 15° per hour.

**Equatorial sundial geometry:**

```
                    Celestial North Pole
                           ↑
                          /|
                         / |
                        /  |
                       /   |  gnomon (pole) aligned to
                      /    |  Earth's rotation axis
                     /  φ  |  angle = latitude φ
                    /──────┤
                   /       |
                  /        |
                EQUATORIAL PLANE
                (hour marks equally spaced: 15° apart)

For a horizontal sundial at latitude φ:
- Hour lines are NOT equally spaced on the horizontal plate
- Hour angle H maps to: tan(line_angle) = sin(φ) × tan(H)
- At equator (φ=0°): all hour lines collapse to a single line (useless)
- At poles (φ=90°): all hour lines equally spaced (equatorial dial)
```

The critical engineering insight: a gnomon aligned to the Earth's rotation axis (not vertical, but angled at the latitude) casts a shadow that sweeps at a constant angular rate on an equatorial plane. This is why proper sundials have the gnomon tilted, not vertical.

### Unequal (Seasonal) Hours vs Mean Solar Hours

Before the mechanical clock era, Western Europe and the ancient Mediterranean world used **unequal hours** (also: temporal hours, seasonal hours):

- Daylight divided into 12 equal parts regardless of season
- A summer daytime hour at 50°N latitude ≈ 75 minutes in modern solar time
- A winter daytime hour at 50°N latitude ≈ 45 minutes in modern solar time
- Night hours also divided into 12 (different lengths from day hours)
- Canonical hours (Prime, Terce, Sext, None, Vespers...) based on this scheme

This was not ignorance — it was a deliberate choice that kept "noon" always at the 6th hour and preserved the symmetry of religious observance throughout the year. Equal hours became standard only when mechanical clocks (which could only measure equal periods) replaced sundials as the primary timekeeping technology.

**Historical note on "None":** The canonical hour None (9th hour, approximately 3 PM modern time) gave us the word "noon" — the word migrated from the 9th hour to midday over centuries as church practice shifted toward midday prayer.

### The Equation of Time: Why a Perfect Sundial Disagrees with a Perfect Clock

Even with a perfect gnomon and perfect construction, a sundial will disagree with a perfectly accurate clock by up to ±16 minutes over the course of a year. This is not an error in the sundial — it is a real physical effect called the **equation of time**.

Two causes:

**Cause 1: Earth's orbital eccentricity (elliptical orbit)**

By Kepler's Second Law, Earth moves faster when closer to the Sun (perihelion, ~January 3) and slower when farther (aphelion, ~July 4). Since the solar day is defined by how long it takes the Sun to return to the meridian, and Earth's orbital speed varies, the solar day is slightly longer in January than in July. A clock that assumes a constant-length day (mean solar time) will diverge from a sundial (apparent solar time) by this effect alone — amplitude ±7.7 minutes, period 1 year.

**Cause 2: Earth's axial tilt (obliquity = 23.44°)**

The Sun appears to move along the ecliptic, which is tilted 23.44° to the equatorial plane. Even if Earth's orbit were perfectly circular, the projection of the Sun's motion onto the equatorial plane varies through the year. Near the equinoxes, the Sun moves mostly along the equator — its right ascension increases quickly. Near the solstices, the Sun moves mostly in declination — its right ascension increases slowly. This creates a ±9.9 minute oscillation with a 6-month period.

**Combined effect:**

```
EQUATION OF TIME (Apparent Solar Time − Mean Solar Time)

+16 min ─┤                        ╭──╮
         │                       /    \
+12 min ─┤                      /      \
         │                     /        \
 +8 min ─┤       ╭─╮          /          \
         │      /   \        /            \
 +4 min ─┤     /     \      /              \
         │    /       \    /                \
   0 min ─┼──/─────────\──/──────────────────\─
         │              \/                    \
 -4 min ─┤                                     \
         │                                      \
 -8 min ─┤                                       ╰──╮
         │                                           \
-12 min ─┤                                            \
         │                                             \
-16 min ─┤                                              ╰
         └─────────────────────────────────────────────────
          Jan  Feb  Mar  Apr  May  Jun  Jul  Aug  Sep  Oct  Nov  Dec

Four times per year the equation of time passes through zero:
~April 15, ~June 14, ~September 1, ~December 25
These are the only days when a sundial and a mean-time clock agree exactly.
```

**The analemma:** If you photograph the Sun at the same clock time every day for a year and superimpose the images, you get a figure-8 curve. The horizontal spread encodes the equation of time; the vertical spread encodes the change in the Sun's declination (seasons). Every accurate sundial must either have the equation of time plotted on it, or use a specially shaped figure-8 gnomon shadow-caster to correct for it automatically.

**Practical implication for early clockmakers:** Once mechanical clocks became accurate enough (roughly 1700s), the equation of time had to be understood, tabulated, and corrected for. Early precision clockmakers like George Graham worked from solar time (sundial) as their reference and had to apply the equation of time correction to evaluate their clocks. Before accurate tables existed, this was a significant source of confusion.

---

## Water Clocks (Clepsydra)

### The Basic Problem: Variable Flow Rate

A clepsydra (Greek: kleptein = to steal, hydor = water) measures time by water flow. The simplest design: a vessel with a small hole at the bottom; the water level at any elapsed time gives the total time. Conversely, outflow vessels mark time by the level dropping to calibrated marks.

The fundamental engineering problem:

```
OUTFLOW CLEPSYDRA — PRESSURE PROBLEM

┌─────────────────────────┐
│ ████████████████████   │ h₁  full: flow rate Q₁ = Cd·A·√(2g·h₁)
│                         │
│ ████████████            │ h₂  half full: Q₂ = Cd·A·√(2g·h₂)
│                         │     Q₂ = Q₁ × √(h₂/h₁) = Q₁/√2
│ ██                      │       = 71% of original rate
│                         │
│         ─┼─             │  orifice (area A)
└─────────────────────────┘
           │
           ▼
        outflow

Torricelli's law: v = √(2gh)
Time marks are NOT equally spaced — they compress as the vessel empties.
A clepsydra calibrated at full is fast when full, slow when nearly empty.
```

**Solution: constant-head design.** If you keep the water level (head h) constant, the flow rate is constant, and equal time intervals produce equal volumes of outflow. Methods:

1. **Overflow vessel:** A supply vessel continuously overflows into the measuring vessel; the overflow keeps the measuring vessel's level constant. The spilled water is wasted but the head is constant.
2. **Float valve:** Ctesibius of Alexandria (~270 BCE) — a float that rises with the water level and partially occludes the inlet orifice, maintaining constant head. Functionally identical to a toilet tank float valve. Same mechanism, ~2300 years old.

### Ctesibius of Alexandria (~270 BCE)

Ctesibius (Ktesibios) was the head of the Musaeum at Alexandria (the research institution associated with the Library of Alexandria). His inventions:

- **The float valve** for constant-head water supply
- **The first float-controlled clepsydra** — water level in the measuring vessel raised a float, which drove a gear train that rotated an indicator pointer against a calibrated dial
- **Pneumatic catapult** and **water organ** (hydraulis)

His clepsydra incorporated:
- Constant-head supply → constant flow rate
- Float rising on outflow vessel
- Rack-and-pinion gear coupling float to rotating drum or pointer
- Hour marks on the drum accounting for seasonal hours (different scales for each month)

This is the **first known gear train** in history. The gear was not invented for clockwork — it was invented for automating time display.

```
CTESIBIUS CLEPSYDRA (~270 BCE)

Supply vessel          Measuring vessel
┌──────────┐          ┌──────────────┐
│          │          │              │
│ overflow │──────────│ float ──────┬┼── gear train ──► rotating drum
│ level    │  orifice │ (rises as   │                   with hour marks
│          │  (const  │  water      │
│ drain    │   head)  │  rises)     │                   indicator pointer
└──────────┘          └─────────────┘
   supply
```

Accuracy improvement over simple outflow: substantial. A well-built Ctesibius clepsydra could achieve approximately ±15 minutes per day — comparable to early mechanical verge clocks 1500 years later.

### Roman Clepsydra in the Courts

In Rome, the clepsydra measured speech time in the courts. Advocates were allocated a set number of water-jar units of time (so many "clepsydras" of speaking time). The phrase "clepsydram dare" (to give the water-clock) meant to grant speaking time. When an advocate wanted more time, he asked for more clepsydras; when he was interrupted, the water was stopped ("aquam dare" and "aquam intercludere"). This is the direct ancestor of the speaker's hourglass in parliamentary procedure.

### Su Song's Astronomical Clock Tower (1088 CE)

The most sophisticated pre-mechanical timekeeping machine in history was built in China, not Europe, 200 years before the European mechanical clock.

Su Song (1020–1101 CE), a government minister and polymath, built a 10-meter tower clock in Kaifeng for Emperor Zhezong. It incorporated:

```
SU SONG'S CLOCK TOWER — SCHEMATIC (~1088 CE)

┌─────────────────────────────────────────────────────┐
│  TOP: Armillary sphere (bronze, ~30 cm diameter)     │
│       Motor-driven to track celestial coordinates    │
│       Astronomer could sight star positions          │
├─────────────────────────────────────────────────────┤
│  MIDDLE: Celestial globe (bronze)                    │
│          Rotated once per sidereal day               │
│          Showed positions of sun, moon, planets      │
├─────────────────────────────────────────────────────┤
│  FRONT: Five-story pagoda                            │
│         36 wooden jacks on rotating platform        │
│         Appeared at windows to announce:             │
│           Hours (red tablets)                        │
│           Watches (green tablets)                    │
│           Quarter-hours (bells)                      │
│           Special announcements (drums, gongs)       │
├─────────────────────────────────────────────────────┤
│  CORE: Water-wheel escapement (the key innovation)   │
│        36 scoops on wheel; each holds water          │
│        When scoop fills to set weight: trips lever   │
│        Wheel advances one step; timer resets         │
├─────────────────────────────────────────────────────┤
│  BASE: Constant-head water supply (Ctesibius method) │
│        Clepsydra feeds wheel scoops at constant rate │
└─────────────────────────────────────────────────────┘
```

The **water-wheel escapement** is the conceptual ancestor of the mechanical escapement. Instead of a falling weight being released in steps by a lever, here a water wheel advances in steps when each scoop achieves the correct weight. The tripping lever locks the wheel between beats and releases it at the correct moment — exactly the function of the mechanical escapement's pallet.

Su Song published the design in a technical manual ("Xin Yi Xiang Fa Yao," 1092 CE) with detailed diagrams — probably the world's first engineering documentation of a complex machine. The original tower was dismantled after a dynastic change; a working reconstruction exists at the National Museum of Natural Science in Taichung, Taiwan.

---

## Sand Glasses and Incense Clocks

### The Sand Glass (Hourglass)

The sand glass is a fixed-interval timer, not a clock. You cannot tell absolute time with an hourglass; you can only measure that a fixed interval has elapsed since the last turn.

**Error sources:**
- Humidity: sand clumps in humid conditions, reducing flow rate
- Temperature: affects the glass neck dimensions (thermal expansion)
- Inclination: must be exactly vertical
- Aging: sand particles abrade each other and the glass, changing particle size and flow characteristics

Historical sand fillings were not always quartz sand — powdered eggshell, lead dust, and metal filings appear in surviving examples. These materials are smoother and less humidity-sensitive than fine silica sand.

Sand glasses appeared in Europe in the 14th century. At sea before chronometers, 30-minute sand glasses were turned by a ship's boy every half hour, with a tick mark on a log board. Accumulated ticks plus sextant readings gave dead-reckoning position. Missing a turn by 10 minutes compounded over days of navigation.

### Chinese Incense Clocks

Calibrated incense sticks and incense trails functioned as timed alarm systems and interval timers in China and Japan:

```
CHINESE INCENSE CLOCK

Tray with carved groove:
┌──────────────────────────────────────────────┐
│                                              │
│   ←──────── incense powder in groove ──────► │
│                                              │
│  start ●─────────────────────────────● end  │
│        │← alarm thread (weight attached)    │
│             burns at calibrated rate         │
│                                              │
│  When fire reaches thread: weight falls      │
│  into metal tray → audible alarm             │
└──────────────────────────────────────────────┘

More sophisticated: spiral grooves, branching grooves for multiple alarms,
different incense blends for different times of day.
```

The Japanese kōdō (way of incense) formalized incense timing in ceremonial contexts. Identifying incense type blindfolded while timing the burn was a court game. The timing element has been largely ceremonial for centuries.

---

## Medieval Bell-Ringing Automata

### The Original Horologium

The word "horologium" in medieval Latin did not mean a clock that displayed the time — it meant a machine that **rang bells at canonical hours**. The primary purpose of the first mechanical clocks was not to show time but to automate the work of a monastic bell-ringer.

In a Benedictine monastic schedule, the day was divided into eight canonical hours (Matins, Lauds, Prime, Terce, Sext, None, Vespers, Compline). A human had to be awake before each to ring the church bells. The mechanical clock replaced that human — hence "horologium."

Early tower clocks:
- No hands or dial
- No external indication of time at all
- Just a gear train, escapement, and striking train with a bell
- The "display" was the sound

**The Salisbury Cathedral clock (1386):**

```
┌─────────────────────────────────────────────────────────────┐
│              SALISBURY CATHEDRAL CLOCK, 1386                │
│                                                             │
│  Status: Still running (with 17th-century modifications)    │
│  One of the oldest mechanical clocks still in operation     │
│                                                             │
│  Components:                                                │
│  - Wrought iron frame (no brass — all iron)                 │
│  - Two weight-driven trains:                               │
│    1. Going train (drives escapement + tolls the hour)      │
│    2. Quarter-striking train (was present; later removed)   │
│  - Verge-and-foliot escapement (original; replaced 1790s)   │
│  - No original dial (faces installed 1884 for tourists)     │
│                                                             │
│  Accuracy: ±15 min/day at best                              │
│  Corrected: Daily by comparison to sundial in the close     │
└─────────────────────────────────────────────────────────────┘
```

Other notable early clocks:
- **Wells Cathedral clock** (1386–1392): astronomical display dial, jousting knights on the quarter-hour — very early automata integrated with timekeeping
- **Strasbourg Cathedral astronomical clock** (1354, rebuilt 1574, rebuilt 1842): three generations of increasingly complex automata, calendar mechanisms, and astronomical displays
- **Prague Orloj** (1410): still functioning; shows solar time, lunar phase, positions of sun and moon in the zodiac, and sidereal time on a single astronomical dial; moving figures added 1490

---

## The Astrolabe: Astronomical Computing Engine

The astrolabe (Greek: "star-taker") is not strictly a timekeeping device but is the predecessor to the astronomical clock and shares its design genealogy. It deserves mention because it explains why medieval clockmakers were obsessed with astronomical displays.

An astrolabe is a **stereographic projection** of the celestial sphere onto a flat plate, with a rotating overlay (the "rete") representing fixed star positions.

```
ASTROLABE STRUCTURE

         rete (rotatable)
           ┌──────────┐
           │  *    *  │  star positions (pierced fretwork)
           │    ☉    │  ecliptic ring (sun path)
           │  *      │
           └──────────┘
                |
           mater (fixed base)
           ┌──────────┐
           │  tympan  │  horizon + hour lines for specific latitude
           │          │  (swappable for different latitudes)
           └──────────┘

By rotating the rete until a star is at the observed altitude,
you read off the local sidereal time from the hour circle.
```

From astrolabe to astronomical clock is a small conceptual step: instead of rotating the rete manually to match observations, let a gear train rotate it automatically, driven by a weight. That is exactly what the Strasbourg and Wells clocks did.

---

## Summary: Error Comparison Table

```
TIMEKEEPING METHOD         | APPROX DATE  | ACCURACY       | PORTABLE | NOTES
───────────────────────────┼──────────────┼────────────────┼──────────┼───────────────
Simple sundial (gnomon)    | ~3500 BCE    | ±15–30 min     | Fixed    | Outdoors only
Calibrated sundial (EoT)   | ~500 BCE     | ±1–2 min       | Fixed    | EoT correction
Simple clepsydra           | ~400 BCE     | ±30 min        | Portable | Variable head
Ctesibius clepsydra        | ~270 BCE     | ±15 min/day    | Large    | Constant head
Su Song water clock        | 1088 CE      | ~±5 min/day    | Fixed    | Water escapement
Sand glass (30 min)        | ~1300 CE     | ±2–3 min/use   | Portable | Interval only
Candle / incense clock     | ~700 CE      | ±5–10 min      | Portable | Interval only
Verge tower clock          | ~1300 CE     | ±15 min/day    | Fixed    | Mechanical step
```

---

## Common Confusion Points

**"The equation of time is an error in sundials."**
No. The equation of time represents the true difference between apparent solar time (what the Sun actually does) and mean solar time (what a clock keeping equal hours shows). A sundial shows real solar time. A mean-time clock is more convenient for coordinating with other people at a distance. The equation of time is the conversion between the two, not an error in either.

**"Water clocks were primitive and inaccurate."**
The Ctesibius clepsydra achieved ±15 min/day — comparable to early mechanical clocks 1500 years later. They failed not from imprecision but from temperature sensitivity (water viscosity changes ~2% per °C, so a 10°C temperature swing shifts rate by ~20%) and difficulty of maintaining them in cold climates. In Mediterranean and Chinese climates, they worked well.

**"Medieval people didn't know what time it was."**
Medieval people knew canonical time extremely well — they had bells, regulated sundials on church walls (scratch dials), and later tower clocks. What they lacked was portable precise timekeeping or equal-hour coordination across distance. The demand for precise equal-hour timekeeping emerged from commerce, navigation, and astronomy, not from daily life.

**"The first clocks showed time on a dial."**
The first mechanical clocks had no dials. They rang bells. Dials came later, and displaying the hours required solving the additional mechanical problem of translating the escapement's counting into the position of a hand on a face. The word "clock" derives from the French cloche (bell) and Latin clocca — it originally meant "bell machine," not "time display."
