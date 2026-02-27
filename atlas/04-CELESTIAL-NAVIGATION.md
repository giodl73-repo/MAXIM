# 04 — Celestial Navigation Chart

*3♠ The Voyager — stars that guide the traveler home.*

---

## Finding North — The Polaris Method

The single most important celestial navigation skill. Works anywhere in the Northern Hemisphere.

```
FINDING POLARIS (NORTH STAR)

  Step 1: Find the Big Dipper (Ursa Major)
  Step 2: Follow the "pointer stars" (Dubhe and Merak)
  Step 3: They point straight to Polaris

                        · Polaris (North Star)
                        ★
                        |   altitude above horizon
                        |   = your LATITUDE
                        |
                  5× ───┤
                  the   |
                  pointer|
                  distance|
                        |
              Dubhe ·───|───· Merak     ← "pointer stars"
                  /           \
                 /  BIG DIPPER \
                ·       ·       ·
               Megrez  Phecda
                 \             /
                  ·           ·
                 Mizar     Alioth
                    \     /
                     ·   ·
                    Alkaid

  POLARIS IS NOT THE BRIGHTEST STAR IN THE SKY.
  It is moderately bright (magnitude +2.0). You find it
  by its POSITION (via the pointer stars), not its brightness.

  LATITUDE CHECK:
  Polaris altitude (angle above horizon) = your latitude.
    · Polaris on horizon → you're at the equator (0°N)
    · Polaris at 45° → you're at 45°N (e.g., Minneapolis)
    · Polaris overhead → you're at the North Pole (90°N)

  Measure angle with your fist at arm's length:
    · 1 fist width ≈ 10°
    · 1 finger width ≈ 2°
```

---

## Northern Sky — Key Navigation Stars

```
NORTHERN HEMISPHERE SKY MAP — LOOKING NORTH

  This is the sky as seen looking straight up from ~40°N latitude.
  Stars rotate counterclockwise around Polaris once per day.

                           N
                           ·
                      Kochab·    · Pherkad
                        ·  LITTLE  ·
                         · DIPPER ·
                    Polaris ★ (north celestial pole)
                           |
            Dubhe ·        |                    · Deneb
            Merak ·        |               ·  CYGNUS  ·
              BIG DIPPER   |              · (Northern ·
            ·    ·    ·    |              ·   Cross)  ·
            ·    ·         |                    · Vega
            Mizar·         |               (LYRA — very bright)
             Alkaid        |
                           |              Altair ·
      W ───────────────────┼─────────────────────────── E
                           |              (AQUILA)
        Capella ·          |
        (AURIGA — very     |
         bright, yellow)   |        Arcturus ·
                           |       (BOOTES — follow
                           |        the arc of the
       ·  ·  ·  ·         |        Big Dipper's handle)
       CASSIOPEIA          |
       (W-shape, opposite  |
        side of Polaris    |
        from Big Dipper)   |
                           |         Spica ·
                           |        (VIRGO)
                           ·
                           S

  KEY NAVIGATION ASTERISMS:
  ─────────────────────────────────────────────
  Big Dipper     → points to Polaris (north)
  Cassiopeia     → opposite side of Polaris from Big Dipper
                   (use when Big Dipper is below horizon)
  Summer Triangle → Vega + Deneb + Altair (overhead in summer)
  Arc to Arcturus → follow Big Dipper handle's curve
```

---

## Southern Hemisphere — Finding South

No bright star marks the south celestial pole. Use the Southern Cross instead.

```
FINDING SOUTH — THE SOUTHERN CROSS METHOD

  Step 1: Find the Southern Cross (Crux) — 4 bright stars
  Step 2: Extend the long axis 4.5× its length
  Step 3: That point is the south celestial pole
  Step 4: Drop straight down to the horizon → that's south

                · Gacrux (top)
                |
                |
     Delta ·────┼────· Mimosa
     Crucis     |    (Beta Crucis)
                |
                · Acrux (bottom — brightest, Alpha Crucis)
                |
                |  extend 4.5× this length
                |
                |
                |
                ↓
           ─ ─ ★ ─ ─  south celestial pole
                |      (no bright star here)
                |
                ↓
  ══════════════════════  horizon
              SOUTH

  DISTINGUISH FROM FALSE CROSS:
  The real Southern Cross has a 5th dim star inside it
  and two bright "pointer stars" (Alpha and Beta Centauri)
  nearby to its left. The False Cross is larger and has
  no pointer stars.

       · · Pointer Stars
      Alpha  Beta
     Centauri Centauri        · Gacrux
       · ·                    |
         ╲                · ──┼── ·
          ╲                   |
           → confirms this    · Acrux
             is the TRUE
             Southern Cross
```

---

## Southern Sky — Key Navigation Stars

```
SOUTHERN HEMISPHERE SKY MAP — LOOKING SOUTH

  As seen from ~35°S latitude, looking straight up.
  Stars rotate clockwise around the south celestial pole.

                           S
                           ·
                      ★ south celestial pole
                     ╱     (no bright star)
                   ╱
      Pointer ·  ╱   · Gacrux
      Stars  · ╱     |
      Alpha ·╱   ·───┼───·     · Canopus
      Beta       SOUTHERN       (2nd brightest star
      Centauri   CROSS          in entire sky)
                  · Acrux
                                        · Achernar
                                        (ERIDANUS)
      W ────────────────────────────────────────── E
                           |
         Sirius ·          |
        (brightest star    |
         in the sky —      |
         visible from      |
         both hemispheres) |
                           |
        · · ·  ORION  · · ·
        Betelgeuse  Rigel  |
            · · ·          |
           (belt)          |
            · · ·          |
                           ·
                           N

  KEY NAVIGATION ASTERISMS:
  ─────────────────────────────────────────────
  Southern Cross  → points to south celestial pole
  Pointer Stars   → confirm true Cross vs. False Cross
  Canopus         → 2nd brightest star, circumpolar from far south
  Magellanic Clouds → two fuzzy patches near south pole
                      (satellite galaxies of Milky Way)
```

---

## Navigation Star Visibility

Which stars can you see from where? Declination determines visibility: a star at declination D is visible from latitudes north of (D - 90°) to south of (D + 90°). In practice, atmospheric extinction limits naked-eye visibility to ~5° above the horizon.

<svg viewBox="-185 -95 370 185" width="960" height="480" xmlns="http://www.w3.org/2000/svg" style="background:#faf8f5; font-family: Georgia, serif;">

  <!-- Star visibility by latitude. Stars are plotted at their declination (y-axis)
       and spread across the x-axis for readability only — x-position is NOT geographic. -->

  <!-- Grid -->
  <line x1="-180" y1="0" x2="180" y2="0" stroke="#e0ddd8" stroke-width="0.3"/>
  <line x1="-180" y1="-30" x2="180" y2="-30" stroke="#e0ddd8" stroke-width="0.2"/>
  <line x1="-180" y1="30" x2="180" y2="30" stroke="#e0ddd8" stroke-width="0.2"/>
  <line x1="-180" y1="-60" x2="180" y2="-60" stroke="#e0ddd8" stroke-width="0.2"/>
  <line x1="-180" y1="60" x2="180" y2="60" stroke="#e0ddd8" stroke-width="0.2"/>
  <line x1="-180" y1="-90" x2="180" y2="-90" stroke="#e0ddd8" stroke-width="0.15"/>
  <line x1="-180" y1="90" x2="180" y2="90" stroke="#e0ddd8" stroke-width="0.15"/>

  <!-- Simplified land outlines — very light context -->
  <path d="M-168,-65 L-120,-73 L-80,-68 L-55,-50 L-75,-42 L-88,-25 L-105,-20 L-125,-35 L-155,-60 L-168,-65 Z"
        fill="#e8e4dc" fill-opacity="0.25" stroke="none"/>
  <path d="M-82,-10 L-50,-2 L-35,5 L-50,28 L-68,48 L-75,55 L-55,25 L-65,-5 L-82,-10 Z"
        fill="#e8e4dc" fill-opacity="0.25" stroke="none"/>
  <path d="M-18,-35 L20,-35 L42,-12 L50,2 L38,18 L15,18 L-10,-12 L-18,-35 Z"
        fill="#e8e4dc" fill-opacity="0.25" stroke="none"/>
  <path d="M-10,-72 L40,-70 L40,-60 L20,-42 L-5,-38 L-10,-60 L-10,-72 Z"
        fill="#e8e4dc" fill-opacity="0.25" stroke="none"/>
  <path d="M50,-68 L155,-62 L180,-50 L120,-22 L80,10 L50,2 L35,-35 L50,-68 Z"
        fill="#e8e4dc" fill-opacity="0.25" stroke="none"/>
  <!-- India -->
  <path d="M68,-22 L80,-8 L73,6 L68,5 L73,-15 L68,-22 Z"
        fill="#e8e4dc" fill-opacity="0.25" stroke="none"/>
  <path d="M112,12 L152,20 L145,35 L118,28 L112,12 Z"
        fill="#e8e4dc" fill-opacity="0.25" stroke="none"/>

  <!-- POLARIS visibility band — everything north of equator -->
  <rect x="-180" y="-90" width="360" height="90" fill="#c0d8f0" fill-opacity="0.10"/>
  <text x="-178" y="-83" font-size="3" fill="#4060a0" font-weight="bold">POLARIS visible (N hemisphere)</text>
  <text x="-178" y="-79" font-size="2.2" fill="#6080b0">altitude above horizon = your latitude</text>

  <!-- SOUTHERN CROSS visibility band — south of ~25°N, full to south pole -->
  <rect x="-180" y="-25" width="360" height="115" fill="#f0d0c0" fill-opacity="0.10"/>
  <text x="40" y="55" font-size="3" fill="#a06040" font-weight="bold">SOUTHERN CROSS visible</text>
  <text x="40" y="59" font-size="2.2" fill="#b08060">(south of ~25°N)</text>

  <!-- BOTH-HEMISPHERE overlap zone — equatorial band -->
  <rect x="-180" y="-25" width="360" height="25" fill="#d0e0c0" fill-opacity="0.12"/>
  <text x="-60" y="-8" font-size="2.5" fill="#608040" font-weight="bold">OVERLAP: Orion, Sirius, Arcturus, Spica, Altair visible from both hemispheres</text>

  <!-- Latitude markers -->
  <text x="182" y="-88" font-size="2.5" fill="#aaa">90°N</text>
  <text x="182" y="-58" font-size="2.5" fill="#aaa">60°N</text>
  <text x="182" y="-28" font-size="2.5" fill="#aaa">30°N</text>
  <text x="182" y="2" font-size="2.5" fill="#aaa">EQ</text>
  <text x="182" y="32" font-size="2.5" fill="#aaa">30°S</text>
  <text x="182" y="62" font-size="2.5" fill="#aaa">60°S</text>
  <text x="182" y="88" font-size="2.5" fill="#aaa">90°S</text>

  <!-- Star position dots (plotted at declination; x spread for readability only) -->

  <!-- Northern stars — blue -->
  <circle cx="-30" cy="-89" r="1.2" fill="#4060a0"/>
  <text x="-27" y="-88" font-size="2.2" fill="#333" font-weight="bold">Polaris +89°</text>

  <circle cx="-80" cy="-39" r="1" fill="#4060a0"/>
  <text x="-77" y="-38" font-size="2" fill="#333">Vega +39°</text>

  <circle cx="60" cy="-46" r="1" fill="#4060a0"/>
  <text x="63" y="-45" font-size="2" fill="#333">Capella +46°</text>

  <circle cx="-140" cy="-45" r="0.8" fill="#4060a0"/>
  <text x="-137" y="-44" font-size="1.8" fill="#333">Deneb +45°</text>

  <!-- Equatorial stars — green (visible from both hemispheres) -->
  <circle cx="100" cy="-19" r="1" fill="#608040"/>
  <text x="103" y="-18" font-size="2" fill="#333">Arcturus +19°</text>

  <circle cx="-20" cy="-9" r="0.8" fill="#608040"/>
  <text x="-17" y="-8" font-size="1.8" fill="#333">Altair +9°</text>

  <circle cx="30" cy="11" r="0.8" fill="#608040"/>
  <text x="33" y="12" font-size="1.8" fill="#333">Spica -11°</text>

  <circle cx="-100" cy="17" r="1.2" fill="#608040"/>
  <text x="-97" y="18" font-size="2.2" fill="#333" font-weight="bold">Sirius -17°</text>

  <circle cx="140" cy="26" r="0.8" fill="#608040"/>
  <text x="143" y="27" font-size="1.8" fill="#333">Antares -26°</text>

  <!-- Southern stars — warm -->
  <circle cx="120" cy="53" r="1.0" fill="#a06040"/>
  <text x="123" y="54" font-size="2.2" fill="#333" font-weight="bold">Canopus -53°</text>

  <circle cx="-60" cy="63" r="0.8" fill="#a06040"/>
  <text x="-57" y="64" font-size="2" fill="#333">Acrux -63° (S. Cross)</text>

  <!-- Note about x-axis -->
  <text x="-178" y="86" font-size="1.8" fill="#999" font-style="italic">Stars spread horizontally for readability — x-position is not geographic longitude.</text>

  <!-- Scale bar -->
  <line x1="150" y1="82" x2="160" y2="82" stroke="#444" stroke-width="0.3"/>
  <line x1="150" y1="81" x2="150" y2="83" stroke="#444" stroke-width="0.2"/>
  <line x1="160" y1="81" x2="160" y2="83" stroke="#444" stroke-width="0.2"/>
  <text x="152" y="86" font-size="1.8" fill="#444">~1,100 km</text>

</svg>

---

## The 15 Navigation Stars

These are the stars that navigators have used for centuries. Learn these and you can fix your position from any latitude.

| Star | Constellation | Magnitude | Declination | Hemisphere | Navigation Use |
|------|--------------|-----------|-------------|------------|----------------|
| **Polaris** | Ursa Minor | +2.0 | +89° | N only | TRUE NORTH. Altitude = latitude. |
| **Sirius** | Canis Major | -1.5 | -17° | Both | Brightest star. Rises in east. |
| **Canopus** | Carina | -0.7 | -53° | S mainly | 2nd brightest. Southern pointer. |
| **Arcturus** | Bootes | -0.1 | +19° | Both | Arc from Big Dipper handle. |
| **Vega** | Lyra | +0.0 | +39° | N mainly | Summer Triangle. Very blue-white. |
| **Capella** | Auriga | +0.1 | +46° | N mainly | Yellow, high in northern sky. |
| **Rigel** | Orion | +0.1 | -8° | Both | Orion's foot. Blue-white. |
| **Betelgeuse** | Orion | +0.4 | +7° | Both | Orion's shoulder. Red giant. |
| **Altair** | Aquila | +0.8 | +9° | Both | Summer Triangle. Fast rotator. |
| **Deneb** | Cygnus | +1.3 | +45° | N mainly | Summer Triangle. Northern Cross. |
| **Acrux** | Crux | +0.8 | -63° | S only | Southern Cross bottom. |
| **Spica** | Virgo | +1.0 | -11° | Both | Arc to Arcturus, spike to Spica. |
| **Antares** | Scorpius | +1.1 | -26° | Both | Red. "Rival of Mars." Low south. |
| **Fomalhaut** | Piscis Aust. | +1.2 | -30° | Both | Lonely bright star in autumn S. |
| **Aldebaran** | Taurus | +0.9 | +17° | Both | Orange. Orion's belt points to it. |

---

## Latitude from Stars

```
LATITUDE DETERMINATION — THREE METHODS

  METHOD 1: POLARIS ALTITUDE (Northern Hemisphere only)
  ─────────────────────────────────────────────────────
  Your latitude = altitude of Polaris above the horizon.
  Accuracy: ±1° with careful measurement.

  Hold fist at arm's length: 1 fist ≈ 10°
  ┌────────────────────────────────────────┐
  │ Polaris at 5 fists up → you're at ~50°N│
  │ Polaris at 3 fists up → you're at ~30°N│
  │ Polaris at 1 fist up  → you're at ~10°N│
  └────────────────────────────────────────┘

  METHOD 2: MERIDIAN TRANSIT (any star, any hemisphere)
  ─────────────────────────────────────────────────────
  When a star crosses due south (its highest point):
    Latitude = 90° − star's altitude + star's declination

  Need: star's declination (from table above) +
        its maximum altitude (measured or estimated).

  METHOD 3: SOUTHERN CROSS ALTITUDE (Southern Hemisphere)
  ─────────────────────────────────────────────────────
  The south celestial pole's altitude = your latitude south.
  Extend the Cross 4.5×, estimate that point's altitude.
```

---

## Direction from the Sun

When stars aren't visible.

```
SUN NAVIGATION — DAYTIME METHODS

  METHOD 1: SHADOW STICK (most reliable, any latitude)
  ─────────────────────────────────────────────────────
  1. Plant a stick vertically in flat ground.
  2. Mark the tip of its shadow.        shadow tip ·─── stick │
  3. Wait 15-30 minutes.                                     │
  4. Mark the new shadow tip.           new tip ·────── stick │
  5. Draw a line between the marks.
  6. That line runs EAST-WEST.
     (First mark = west, second mark = east)
  7. A perpendicular line = north-south.

       (first mark)           (second mark)
           ·W ─────────────────── E·
                      │
                      │  ← this line is
                      │     NORTH-SOUTH
                      N
                      (northern hemisphere:
                       shadow points north)

  METHOD 2: WATCH METHOD (rough, northern hemisphere)
  ─────────────────────────────────────────────────────
  Point the hour hand at the sun.
  Bisect the angle between the hour hand and 12 o'clock.
  That bisector points south.

  METHOD 3: SUNRISE / SUNSET
  ─────────────────────────────────────────────────────
  Sun rises approximately east, sets approximately west.
  EXCEPT: only exactly east/west at equinoxes (Mar 20, Sep 22).
  Summer: rises NE, sets NW.
  Winter: rises SE, sets SW.
  Nearer the equator → less variation.
```

---

## Moon Navigation

```
DIRECTION FROM THE MOON

  CRESCENT MOON METHOD (quick and simple):
  ─────────────────────────────────────────
  Draw an imaginary line connecting the two horns (tips)
  of a crescent moon. Extend that line down to the horizon.
  Where it meets the horizon is approximately SOUTH
  (in Northern Hemisphere) or NORTH (in Southern Hemisphere).

        ╭─╮  ← horns
       ╱   ╲
      │  ·  │     line connecting horns
       ╲   ╱      extended down to horizon
        ╰─╯          │
            ╲         │
             ╲        │
              ╲       │
  ═════════════╪══════════════ horizon
             SOUTH
         (N. hemisphere)

  MOON PHASE TIMING:
  ──────────────────
  First quarter moon (right half lit):
    · rises at noon, highest at 6pm, sets at midnight
    · at midnight it's in the WEST

  Full moon:
    · rises at sunset, highest at midnight, sets at sunrise
    · behaves like the sun but 12 hours offset
    · at midnight it's due SOUTH (N. hemisphere)

  Last quarter moon (left half lit):
    · rises at midnight, highest at 6am, sets at noon
    · at midnight it's in the EAST
```

---

## Seasonal Sky Changes

```
WHAT'S VISIBLE WHEN — NORTHERN HEMISPHERE

  The sky rotates through constellations over the year because
  Earth orbits the Sun. Different stars dominate each season.

  WINTER (Dec-Feb):
  ┌────────────────────────────────────────┐
  │  ORION dominates (south, unmistakable) │
  │  Sirius (brightest star) below Orion   │
  │  Aldebaran, Capella high overhead      │
  │  Big Dipper low in northeast           │
  │  Best: clearest skies, longest nights  │
  └────────────────────────────────────────┘

  SPRING (Mar-May):
  ┌────────────────────────────────────────┐
  │  Big Dipper high overhead              │
  │  Arc to Arcturus → spike to Spica      │
  │  Leo (Regulus) in south                │
  │  Orion sinking in west                 │
  └────────────────────────────────────────┘

  SUMMER (Jun-Aug):
  ┌────────────────────────────────────────┐
  │  SUMMER TRIANGLE dominates overhead:   │
  │    Vega (Lyra) + Deneb (Cygnus)       │
  │    + Altair (Aquila)                   │
  │  Scorpius + Antares low in south       │
  │  Milky Way visible in dark skies       │
  │  Note: short nights, less time to see  │
  └────────────────────────────────────────┘

  AUTUMN (Sep-Nov):
  ┌────────────────────────────────────────┐
  │  Summer Triangle sinking in west       │
  │  Cassiopeia (W-shape) high in north    │
  │  Fomalhaut lonely in south             │
  │  Andromeda Galaxy visible (fuzzy patch)│
  │  Orion rising in east (winter coming)  │
  └────────────────────────────────────────┘
```

---

## The Longitude Problem

Latitude is geometry — measure a star's altitude and you know how far north or south you are. Navigators have done this since antiquity. But longitude is a *time* problem, and it went unsolved for 3,000 years.

```
WHY LONGITUDE REQUIRES A CLOCK

Earth rotates 360 degrees in 24 hours = 15 degrees per hour.

If you know what time it is at a REFERENCE POINT (Greenwich)
and what time it is WHERE YOU ARE (from the sun's position),
the difference tells you your longitude.

  1 hour difference  =  15 degrees of longitude
  4 minutes          =  1 degree
  4 seconds          =  1 arcminute (~1.85 km at equator)

THE CATCH: you need an accurate clock that keeps
Greenwich time at sea for months. Pendulum clocks
don't work on a rolling ship. Spring-driven clocks
of the era drifted minutes per day.

SOLVED: John Harrison's marine chronometer H4 (1761).
Lost only 5 seconds over 81 days at sea.
Won the Longitude Prize (eventually, after politics).

Before Harrison, dead reckoning was the only option:
estimate speed x time = distance. Errors compounded.
Ships wrecked. Thousands died.
```

This connects Map 01 (Earth's rotation drives the 15-degrees-per-hour relationship) forward to the technology maps where timekeeping becomes infrastructure.

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| Find north at night (N. Hemisphere)? | Big Dipper pointer stars → Polaris |
| Find south at night (S. Hemisphere)? | Southern Cross long axis × 4.5 → south pole |
| Find my latitude? | Polaris altitude (N) or meridian transit method |
| Find direction during the day? | Shadow stick: first mark = W, second = E |
| Brightest star in sky? | Sirius (-1.5 mag), below Orion in winter |
| Stars visible from both hemispheres? | Orion belt stars, Sirius, Arcturus, Spica, Altair |
| Best season for night navigation? | Winter (longest nights, clearest skies, Orion up) |
| How accurate is star navigation? | ±1° latitude (±111 km) with care. Longitude is harder. |
| Can I navigate by the Moon? | Yes — crescent horns line points S (N. Hem), phase timing gives rough direction |
| One thing to memorize? | Big Dipper → Polaris. Everything else builds from there. |

---

## Cross-References

- **Celestial mechanics** → [astronomy/](../astronomy/00-OVERVIEW.md)
- **Map projections** → [atlas/31-MAP-PROJECTIONS.md](31-MAP-PROJECTIONS.md) *(planned)*
- **Magnetic declination** → [atlas/29-MAGNETIC-DECLINATION.md](29-MAGNETIC-DECLINATION.md) *(planned)*
- **Exploration routes** → [atlas/41-EXPLORATION-ROUTES.md](41-EXPLORATION-ROUTES.md) *(planned)*
- **Cartography** → [cartography/](../cartography/00-OVERVIEW.md)
