# Cyclones and Anticyclones — Lifecycle, Vorticity, Blocking

## The Big Picture

Cyclones (low pressure) and anticyclones (high pressure) are the dominant synoptic-scale weather systems of the mid-latitudes. Their development is governed by vorticity dynamics and the interaction between surface boundary conditions (fronts, temperature gradients) and upper-level flow (jet stream, Rossby waves). Understanding their lifecycle is the core of operational forecasting.

```
+---------------------------------------------------------------+
|         CYCLONE vs ANTICYCLONE COMPARISON                     |
|                                                               |
|  CYCLONE (LOW)               ANTICYCLONE (HIGH)               |
|  Pressure decreasing         Pressure increasing inward       |
|  inward                                                       |
|  NH: Counterclockwise        NH: Clockwise                    |
|  SH: Clockwise               SH: Counterclockwise             |
|  Surface convergence →       Surface divergence →             |
|  rising motion               sinking motion                   |
|  Clouds, precipitation       Clear skies, dry                 |
|  Warm/cold fronts            No fronts                        |
|  Active weather              Suppressed weather               |
+---------------------------------------------------------------+
```

---

## Vorticity — The Spin of the Atmosphere

Vorticity = rotation in the fluid. Critical for understanding cyclone development:

```
ABSOLUTE VORTICITY:  η = ζ + f

  ζ = RELATIVE VORTICITY (spin relative to Earth's surface)
      Positive (cyclonic, CCW in NH) = low pressure
      Negative (anticyclonic, CW in NH) = high pressure

  f = PLANETARY VORTICITY (Earth's spin; Coriolis parameter)
      f = 2Ω sin(φ); f > 0 in NH, f < 0 in SH, f = 0 at equator

CONSERVATION OF POTENTIAL VORTICITY:
  PV = (ζ + f) / thickness   [conserved for adiabatic flow]

  If air moves poleward (f increases):
    ζ must decrease → anticyclonic curvature

  If air moves equatorward (f decreases):
    ζ must increase → cyclonic curvature

  This conservation drives Rossby wave propagation
```

**Vorticity advection** drives pressure change. Positive vorticity advection (PVA) by the jet stream → divergence aloft → surface low development. Negative vorticity advection (NVA) → convergence aloft → surface high development.

---

## Extratropical Cyclone Development — Mechanisms

### Surface Factors

```
BAROCLINIC INSTABILITY: The fundamental mechanism

Baroclinicity = horizontal temperature gradients in the atmosphere
(zone between cold polar air and warm subtropical air)

A small perturbation along the polar front can grow by:
1. Warm air (less dense) rises poleward and northward
2. Cold air (more dense) sinks equatorward
3. This releases available potential energy (APE)
4. Cyclone grows as long as baroclinic zone supports it
```

**Cyclogenesis preferred locations** (NH):
- Lee of Rocky Mountains (Alberta clipper, Colorado low)
- Gulf Coast (Gulf Low, E. Coast Nor'easter)
- East Coast (Nor'easters: explosive cyclogenesis over warm Gulf Stream)
- Aleutian/Icelandic Low regions (storm tracks)

### Upper-Level Forcing — The Jet Stream Connection

```
                    TROUGH         RIDGE
         500 mb:   (cyclonic)     (anticyclonic)
              \        /                 \
               \      /                   \
              --\----/----         --------\---------
                \    /                      \
                 \  /    PVA ahead of trough  \
                  \/     → surface LOW          \

JET STREAK EXIT REGION:
  Jet streak = localized max wind in jet stream
  Left exit: divergence → rising motion → surface low favored
  Right entrance: convergence → sinking → surface high favored
```

**Explosive cyclogenesis (bombogenesis)** — rapid deepening of at least 24 mb in 24 hours (1 "Bergeron"):
- Requires: jet stream overhead + strong baroclinicity + oceanic heating (warm SST)
- Classic: Nor'easters over Gulf Stream; Pacific storms approaching West Coast
- Can deepen from 1000 mb to 960 mb in 24 hours → devastating storms

---

## Extratropical Cyclone Structure

```
MATURE EXTRATROPICAL CYCLONE (surface map):

          500 mb ridge
         (warm air aloft)
              /\
             /  \
    W front /    \ E
   (clouds, rain) \
                   L (center: lowest pressure)
        warm      |
        sector   \ |
  (warm, moist;   \|
   possible severe  \
   weather)          \
                      cold front (squall line/thunderstorms
                      possible with strong cold air)

CROSS-SECTION:
         Cold       Warm        Cold
         Air      Sector        Air
          \         /\          /
           \   W  /  \  C      /
            \  F /    \ F     /
             \  /  ~~~ \/    /
              \/ Ns  As  \  /
               ~~~~~~~~~~~\/
               (nimbostratus    (cumulus, cumulonimbus
                warm front)     cold front)
```

---

## Anticyclones — Blocking and Persistence

**Anticyclones** = high-pressure systems. Two types:

| Type | Origin | Duration | Associated Weather |
|------|--------|----------|-------------------|
| **Thermal high** | Surface heating of continental interior (summer) | Days–weeks | Hot, dry |
| **Cold high** | Radiative cooling of continental interior (winter) | Days–weeks | Cold, dry; very stable |
| **Dynamic high** | Subsidence in upper atmosphere (subtropical, blocking) | Weeks–months | Persistent dry |

### Blocking Anticyclones

A blocking anticyclone is a persistent (>5 days) high-pressure system that deflects the normal westerly flow:

```
NORMAL FLOW (zonal):
→→→→→→→→→→→→→→→→→→→→→→→→→→→→→
(fast westerlies, quick weather progression)

BLOCKED FLOW (meridional):
     ↑      ↓
    /  \  /  \
→→→/    \/    \→→→→
   HIGH  LOW
(jet stream splits around blocking high;
 weather systems stagnate to north and south)

PATTERN: Omega block (looks like Greek Ω symbol)
         Rex block (HIGH over LOW)
```

**Consequences of blocking:**
- Prolonged heat waves (European heat wave 2003: ~70,000 excess deaths)
- Prolonged cold air outbreaks
- Persistent drought or flooding in fixed locations
- Forecast skill collapses beyond 10 days when blocking involved

**Blocking frequency** — naturally occurs in NH primarily in two preferred regions: North Pacific and North Atlantic. Arctic amplification (warmer Arctic relative to tropics) may be increasing blocking frequency — ongoing research.

---

## Tropical Cyclones — Fundamentally Different

**Tropical cyclones** (hurricanes, typhoons, cyclones) are warm-core, symmetric systems driven by ocean heat flux — completely different mechanism from extratropical cyclones:

```
TROPICAL CYCLONE STRUCTURE:
         ↑↑↑   ↑↑↑   ↑↑↑
        ____   ___   ____
       /    \_/   \_/    \  ← Rainbands
      |    Eye Wall       |
      |   /  EYE  \       |
      |   \        /      |  ← Eye: subsiding, warm, calm
      |    \______/       |
      |                   |
 ↓↓↓  |   Spiral inflow   |  ↓↓↓
      |___________________|
              Ocean
          (warm SST ≥ 26°C)
          (latent heat source)
```

**Tropical vs extratropical comparison:**

| Feature | Tropical | Extratropical |
|---------|----------|--------------|
| Core | Warm (subsiding in eye) | Cold (troughs aloft) |
| Fronts | None | Warm + cold fronts |
| Symmetry | Nearly symmetric | Asymmetric |
| Energy source | Ocean latent heat | Baroclinic APE |
| Size | 500–1000 km | 1000–5000 km |
| Formation | 5°–20° lat, warm ocean | 40°–65° lat, frontal zones |
| Wind max | Near eye wall (~30–50 km) | In squall lines/fronts |

**Extratropical transition** — tropical cyclones moving poleward eventually encounter the baroclinic zone and "transition" into extratropical systems. They may intensify again (baroclinic re-intensification), sometimes producing very deep storms even after losing tropical characteristics.

---

## Pressure Units and Reporting

```
STANDARD ATMOSPHERIC PRESSURE: 1013.25 mb = 1013.25 hPa = 1 atm = 760 mmHg

TYPICAL PRESSURE RANGES:
  Strong anticyclone:  1030–1050 mb (1050 mb: extreme continental high)
  Normal high:         1020–1030 mb
  Normal conditions:   1010–1020 mb
  Weak low:            995–1010 mb
  Strong low:          970–995 mb
  Explosive cyclone:   940–970 mb
  Typhoon/hurricane:   900–940 mb
  Most intense on record: Typhoon Tip 1979 = 870 mb
```

---

## Decision Cheat Sheet

| Forecast situation | Interpretation |
|-------------------|----------------|
| Strong PVA aloft (jet trough approaching) | Surface low development expected |
| Strong NVA aloft (ridge aloft approaching) | Surface high/anticyclogenesis |
| Rapid deepening (>24 mb/24 hr) | Bombogenesis; explosive cyclone |
| Persistent anomalous high for >5 days | Blocking event; skill for downstream weather collapses |
| Warm core, symmetric, over ocean | Tropical cyclone mechanics |
| Elongated, asymmetric, frontal structure | Extratropical cyclone |

---

## Common Confusion Points

**"Cyclone" doesn't mean just hurricane** — Cyclone = any closed low-pressure circulation. Extratropical cyclones (the mid-latitude storms on weather maps) are cyclones. "Tropical cyclone" is the generic term for hurricane/typhoon. The word "cyclone" in news sometimes means tropical, sometimes not — always check context.

**Surface pressure vs upper-level trough** — A surface cyclone (closed low on surface map) and an upper-level trough (Rossby wave trough at 500 mb) are different things. Troughs can exist without closed surface lows. Surface lows are typically collocated with or east of upper troughs at maturity.

**Anticyclone ≠ always nice weather** — Anticyclones produce fair weather in summer. In winter, a strong anticyclone over the continent can bring extreme cold, fog, ice storms, and terrible air quality (temperature inversion traps pollutants). California's "Ridiculously Resilient Ridge" (a blocking anticyclone) brought extreme drought 2012–2017.

**Hurricane eye pressure** — The extremely low pressure (870–900 mb in intense storms) is measured at the eye *center*. The gradient from ~1010 mb ambient to 870 mb over ~50 km = enormous pressure gradient → fierce winds. This gradient collapses rapidly after landfall.
