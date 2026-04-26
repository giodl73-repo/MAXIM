# Severe Weather — Supercells, Tornadoes, Tropical Cyclones

## The Big Picture

Severe weather requires three ingredients: instability (CAPE), moisture, and wind shear. The wind shear component — both speed shear and directional shear — is what separates ordinary thunderstorms from organized, long-lived severe weather systems.

```
+---------------------------------------------------------------+
|              THUNDERSTORM ORGANIZATION SPECTRUM               |
|                                                               |
|  SHEAR    LOW ←————————————————→ HIGH                         |
|           |                                                   |
|   CAPE    |   Isolated            Squall        Supercell     |
|   HIGH    |   single cell         line /        (rotating     |
|           |   (pulse)             QLCS          mesocyclone)  |
|           |                                                   |
|   CAPE    |   Stratus/            Organized     Supercell     |
|   MOD     |   Stratiform          QLCS          less likely   |
|           |                                                   |
|  Short-lived →                     Organized,  ← Long-lived   |
|  < 1 hour                           multi-hour                |
+---------------------------------------------------------------+
```

---

## Thunderstorm Types

### Single-Cell (Pulse) Thunderstorm

Lifecycle ~30–60 minutes. One updraft/downdraft cycle:

```
CUMULUS → MATURE → DISSIPATING

Cumulus:      Updraft dominates; cloud grows
              LCL → LFC → parcel accelerates upward

Mature:       Precipitation initiates (Bergeron or coalescence)
              Downdraft develops (evaporative cooling + precip drag)
              Both updraft and downdraft coexist
              MOST LIGHTNING, heaviest rain, possible hail

Dissipating:  Downdraft overwhelms updraft; cuts off moisture supply
              Rain-cooled outflow undercuts updraft
              Cloud spreads out; stratiform rain/virga
```

### Multicell Cluster and Squall Line (QLCS)

Multiple cells arranged in a line (cold front, dryline, or outflow boundary). New cells form on the flank:
- **Squall line** = organized linear MCS (Mesoscale Convective System)
- **QLCS** = Quasi-Linear Convective System; can produce tornadoes (brief, embedded)
- Typical severe weather: large hail, strong winds (derecho potential), heavy rain

### Supercell

A supercell is a long-lived (hours), organized thunderstorm with a **rotating updraft (mesocyclone)**. The only thunderstorm type capable of producing significant (EF2+) tornadoes:

```
SUPERCELL STRUCTURE (overhead view):

         FORWARD FLANK
         PRECIPITATION        ← forward-flank downdraft (FFD)
         (rain/small hail)        (behind the FFD = "bear's cage")
              |
         Storm motion →
              |
              UPDRAFT/         Flanking line
              MESO-            (new cell development)
              CYCLONE          |
              (wall cloud)     v
              |                REAR-FLANK DOWNDRAFT (RFD)
              v                → wraps around updraft → tornado genesis
         TORNADO REGION
         (near RFD/FFD boundary)
```

**Mesocyclone formation — wind shear tilting and stretching:**

```
1. AMBIENT VORTEX TUBES (horizontal rotation from wind shear):
   Wind shear creates horizontal "rolling" tubes of air

2. TILTING:
   Thunderstorm updraft tilts horizontal vorticity into vertical
   (horizontal rolling → vertical spinning = mesocyclone)

3. STRETCHING:
   Updraft intensifies and stretches the vortex tube vertically
   → Vorticity amplifies (conservation of angular momentum)
   → Mesocyclone intensifies
```

**Radar signature of supercell:**
- Hook echo (classic: RFD wraps around meso)
- BWER (Bounded Weak Echo Region / vault) — near-zero reflectivity surrounded by high Z = strong inflow
- Strong rotation in velocity product (couplet of inbound + outbound)

---

## Tornadoes

A tornado is a violently rotating column of air extending from a cumulonimbus to the ground:

```
TORNADO GENESIS (tilting/stretching mechanism):
1. RFD (rear-flank downdraft) wraps cyclonically around mesocyclone
2. RFD creates a baroclinic zone near the surface (cold RFD + warm inflow)
3. Horizontal vorticity in baroclinic zone tilted/stretched vertically
4. Vortex descends from mesocyclone to ground as RFD occludes
5. Once touchdown confirmed → tornado

TORNADO STRUCTURE:
  Wall cloud → Rotating contact → Funnel cloud → Dust whirl → Condensation funnel
  (funnel appears as condensation where pressure < dewpoint;
   the tornado itself extends even when funnel isn't visible)
```

### Enhanced Fujita Scale

```
SCALE   WIND EST.   TYPICAL DAMAGE
------  ----------  -----------------------------------
EF0     105-137km/h Some damage to chimneys, branches broken
EF1     138-177km/h Roof surfaces peeled, mobile homes overturned
EF2     178-217km/h Roofs torn off, mobile homes destroyed, large trees uprooted
EF3     218-266km/h Entire stories of houses leveled, cars lifted
EF4     267-322km/h Houses leveled, cars thrown, weaker structures obliterated
EF5     >322 km/h   Strong houses swept away, steel-reinforced structures damaged
```

**Annual US tornadoes:** ~1,200 average; peak April–June in Tornado Alley (TX/OK/KS/NE) and Dixie Alley (MS/AL/TN). The EF0–EF1 constitute ~80% of all tornadoes; EF4–EF5 are ~1% but cause majority of fatalities.

**Tornado outbreak** — multiple tornadoes in a short period from one weather system. Super outbreak April 25–28, 2011: 360 tornadoes in 4 days, 324 deaths.

---

## Derecho — Straight-Line Wind Event

A derecho is a long-lived, widespread, straight-line wind damage event associated with a squall line:

```
REQUIREMENTS:
- Damage swath > 400 km long
- Wind gusts > 93 km/h (58 mph) along most of the path
- Several reports of ≥ 120 km/h

MECHANISM:
  Squall line develops strong rear-inflow jet at mid-levels
  → Descends to surface → "bow echo" on radar
  → Straight-line damage (not rotating like tornado)

BOW ECHO:
  Leading line bows forward due to strong rear-inflow jet
     →→→
    / bow\
   /      \
  bookend  bookend
  vortex   vortex
   (cyclonic at N end → can produce brief tornadoes)
```

---

## Tropical Cyclones — Heat Engine Mechanics

A tropical cyclone is a Carnot heat engine: takes heat from warm ocean, converts some to mechanical energy (wind), exhausts at cold tropopause.

```
ENERGY CYCLE:
  Warm Ocean (SST ~28°C) → Evaporation → Latent heat input
           ↓
  Air flows inward near surface, spiraling in (friction spiraling)
           ↓
  Updraft in eyewall → Latent heat released → Drives circulation
           ↓
  Outflow layer (~12 km altitude) → Exports warm air → Cold exhaust
           ↓
  Maximum potential intensity:
    V²_max ∝ (SST - T_outflow) × Ck/Cd
    (SST = sea surface T; Ck = enthalpy exchange; Cd = drag)
```

### Tropical Cyclone Stages

```
TROPICAL DISTURBANCE → TROPICAL DEPRESSION (< 63 km/h)
→ TROPICAL STORM (63–119 km/h) → HURRICANE/TYPHOON (≥ 119 km/h)
   [Atlantic: Hurricane; W. Pacific: Typhoon; Indian: Cyclone]
```

**Saffir-Simpson Hurricane Wind Scale:**

| Category | Wind Speed | Storm Surge | Damage |
|----------|-----------|-------------|--------|
| 1 | 119–153 km/h | 1.2–1.5 m | Some damage |
| 2 | 154–177 km/h | 1.8–2.4 m | Extensive damage |
| 3 | 178–208 km/h | 2.7–3.7 m | Devastating; major |
| 4 | 209–251 km/h | 4.0–5.5 m | Catastrophic |
| 5 | ≥ 252 km/h | > 5.5 m | Catastrophic; few structures survive |

**Most deaths from storm surge**, not wind. Katrina 2005: Category 3 at landfall but 3–8 m storm surge → 1,800+ deaths.

### Tropical Cyclone Formation Requirements

```
1. Warm SST (≥26°C, ~50 m depth)  ← heat source
2. Coriolis force (>5° latitude)   ← needed for rotation
3. Low wind shear                   ← shear disrupts warm core
4. Pre-existing disturbance         ← initial vorticity
5. High relative humidity           ← reduces entrainment of dry air
6. Sufficient ocean heat content    ← not just surface T
```

**Rapid intensification (RI)** = pressure drop ≥ 35 mb in 24 hours. Occurs over warm open water, low shear. Very difficult to forecast. Major challenge for preparation lead times.

### Hurricane Structure

```
EYE (10–50 km diameter):
- Calm, partly sunny
- Subsiding air → warm
- Lowest pressures

EYEWALL:
- Maximum winds (just outside eye)
- Tallest clouds (to tropopause ~15 km)
- Heaviest precipitation
- Eyewall replacement cycle: outer eyewall forms,
  contracts, replaces inner → storm reorganizes
  (can temporarily weaken then re-intensify)

RAINBANDS:
- Spiral bands of showers/storms extending outward
- Can extend 500–1000 km from center
- Tornadoes possible in outer rainbands
```

---

## Decision Cheat Sheet

| Situation | Interpretation |
|-----------|---------------|
| Hook echo on radar | Supercell with rotating mesocyclone; tornado possible |
| Tight velocity couplet on Doppler | Rotation; mesocyclone confirmed; tornado warning |
| Bow echo with book-end vortices | Derecho potential; damaging straight-line winds |
| Wall cloud rotating, lowering | Tornado imminent |
| Weak radar signature with strong rotation | Possible "landspout" or weak tornado; not supercell type |
| Rapid RI (pressure drop >35mb/24hr) | Hurricane rapidly intensifying; watch forecasts carefully |
| Large area of reflectivity moving linearly | Squall line / MCS; multiple hazards (hail, wind, tornadoes) |

---

## Common Confusion Points

**Fujita scale doesn't measure wind directly** — EF ratings are based on *damage indicators*. Teams survey damage post-tornado and assess what structures experienced, then back-calculate approximate wind range. There's significant uncertainty, especially for EF5 determinations.

**Tornado vs downburst** — Both can produce ~100 km/h winds at the surface. Tornado: rotating, narrow path, convergent winds. Downburst: divergent winds (spreading out from impact point), no rotation. Radar can distinguish by velocity data; damage patterns are diagnostic (tornado = rotary pattern, downburst = radial/fanning).

**Hurricane category and storm surge** — Category is based on *wind speed only*. Storm surge depends on: storm size, angle of approach, coastal geometry, bathymetry. A large, slow Category 2 can produce more surge than a fast, compact Category 4. Never use the wind category alone to assess surge risk.

**Eye = calm but not the weakest winds** — The eye is calm/clear, but the eyewall immediately surrounding it has the strongest winds. The transition from violent eyewall to calm eye can be abrupt. Ships and aircraft can be suddenly thrown into intense conditions when emerging from the eye on the other side.
