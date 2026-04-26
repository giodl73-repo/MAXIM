# Atmospheric Dynamics — Forces, Coriolis, Geostrophic Balance, Jet Streams

## The Big Picture

Atmospheric motion is governed by the Navier-Stokes equations applied to a rotating, stratified fluid — the same NS equations from fluid dynamics, constrained to a thin spherical shell where the Coriolis term (2Ω × u) dominates over advective inertia at large scales (Rossby number Ro = U/fL ≪ 1), and vertical momentum is routinely dropped via the hydrostatic approximation (∂p/∂z = −ρg). The dominant force balance at synoptic scale (~1000 km) is geostrophic: pressure gradient force balanced by Coriolis deflection. Departures from geostrophic balance drive vertical motion, which drives weather.

```
+---------------------------------------------------------------+
|              ATMOSPHERIC FORCE BALANCE HIERARCHY              |
|                                                               |
|  SCALE      DOMINANT BALANCE        RESULT                    |
|  --------   -----------------------  -------------------------  |
|  Planetary  Pressure gradient +      Jet streams, trade winds |
|             Coriolis                 flowing along isobars    |
|                                                               |
|  Synoptic   Geostrophic balance      Cyclones/anticyclones;   |
|  (~1000km)  (PGF ≈ Coriolis)         winds parallel to isobars|
|                                                               |
|  Mesoscale  Non-geostrophic          Thunderstorm outflows,   |
|  (~100km)   (ageostrophic)           sea breezes, fronts      |
|                                                               |
|  Small      Inertial/viscous         Turbulence, boundary     |
|  scale                               layer                    |
+---------------------------------------------------------------+
```

---

## Forces Acting on the Atmosphere

### Pressure Gradient Force (PGF)
```
F_PGF = -(1/ρ) ∇P

Direction: from HIGH pressure to LOW pressure
Magnitude: proportional to pressure gradient (isobar spacing)
This is the ONLY force that can initiate motion from rest
```

### Coriolis Effect
Not a real force — an apparent deflection due to Earth's rotation. Acts on any moving object in the rotating reference frame:

```
In NORTHERN HEMISPHERE:
Moving object deflects to the RIGHT of motion

In SOUTHERN HEMISPHERE:
Moving object deflects to the LEFT of motion

At EQUATOR: Coriolis = 0 (no deflection)
At POLES:   Coriolis = maximum

Coriolis parameter: f = 2Ω sin(φ)
Where: Ω = Earth's rotation rate (7.27×10⁻⁵ rad/s)
       φ = latitude
```

### Gravity
- Vertical component dominates atmospheric structure
- Reduced gravity (gravity minus buoyancy effect) drives vertical motions

### Friction
- Significant only in boundary layer (lowest ~1–2 km)
- Causes winds to cross isobars toward low pressure (angle ~20–40°)
- Above boundary layer, friction negligible

---

## Geostrophic Balance — The Dominant Synoptic Balance

When PGF and Coriolis exactly balance, the result is **geostrophic flow** — air moves parallel to isobars (not toward low pressure):

```
PRESSURE MAP VIEW (Northern Hemisphere):

         HIGH (1030 mb)
              |
              | ←-- Pressure gradient force (toward LOW)
              |
   -------->  WIND (along isobars)
   (air flows counterclockwise around LOW; LOW is on its left)
              |
              | ←-- Coriolis deflection (to right, = rightward = away from LOW)
              |
         LOW (1000 mb)

GEOSTROPHIC WIND: V_g = -(1/fρ) × ∂P/∂n
(n = direction perpendicular to isobars)

NH:  LOW pressure on LEFT of wind direction
SH:  LOW pressure on RIGHT of wind direction
```

**Gradient wind** = geostrophic + centripetal acceleration (better for curved isobars):
- Flow around LOW (cyclone): slower than geostrophic (centripetal inward)
- Flow around HIGH (anticyclone): faster than geostrophic (centripetal outward)

---

## Divergence, Convergence, and Vertical Motion

```
CONVERGENCE (air flowing together) → VERTICAL MOTION REQUIRED
DIVERGENCE (air flowing apart)     → VERTICAL MOTION REQUIRED

UPPER LEVEL DIVERGENCE:
         ←← AIR SPREADING OUT →→   (upper troposphere)
                     |
                     ↓ (compensating vertical motion)
         SURFACE LOW PRESSURE develops
         (air sucked up = rising motion = clouds + rain)

UPPER LEVEL CONVERGENCE:
         →→ AIR PILING UP ←←      (upper troposphere)
                     |
                     ↓
         SURFACE HIGH PRESSURE
         (air pushed down = sinking = clear skies)

KEY INSIGHT: Upper-level divergence drives surface lows
             Upper-level convergence drives surface highs
```

**Vorticity** — spin of the atmosphere:
- Absolute vorticity η = relative vorticity ζ + planetary vorticity f
- Relative vorticity ζ: positive (counterclockwise/cyclonic) = cyclone
- Vorticity advection by jet stream creates divergence patterns → drives surface development

---

## Jet Streams

Fast, narrow rivers of air in the upper troposphere (~200–300 mb):

```
STRUCTURE OF JET STREAM (cross-section):
                                               200 mb (~12 km)
              |  Jet Core  |
    West     <|            |>                 Wind speed:
    East     <| max 100-   |>       East      100–200+ kt (>200 km/h)
             <| 200+ kts   |>
             <|            |>
                                               500 mb (~5.5 km)

LOCATION:
Polar Jet Stream:   ~60°N, highly meandering, ~9–12 km altitude
Subtropical Jet:    ~30°N, less meandering, ~13 km altitude
(NH winter both jets present; NH summer subtropical jet weakens)
```

**Jet stream formation** — marks strong horizontal temperature gradient (baroclinic zone). Where temperature gradient is strong (frontal zone between polar and subtropical air), thermal wind relationship requires strong westerly winds aloft. Jet stream = thermal wind response to upper tropospheric temperature gradient.

**Thermal wind relationship:**
```
∂V_g/∂p ∝ horizontal temperature gradient

In practice: increasing wind speed with height (westerlies) where cold air is to the north
             If temperature increases with height (inversion), wind decreases with height
```

---

## Rossby Waves — Planetary-Scale Dynamics

Large-scale meanders of the westerlies/jet stream. Key to understanding blocking, teleconnections, and week-2 forecasting:

```
TOP VIEW (Northern Hemisphere):
                    L     L     L
               .  .   .  .  .   .  .
            .    / \      / \    / \   .
           /    /   \    /   \  /   \   \
     60°N-o----+-----+--+-----++-----+---o--
          |     \   /    \   / \   /    |
           \     \ /      \ /   \ /    /
            `     `        `     `    '
     30°N

ROSSBY WAVE: sinusoidal north-south meanders
Wavelength: 3000–6000 km (typically 4–6 waves around hemisphere)
Speed: generally slow (retrogressive in strong flows)

CONSERVATION OF POTENTIAL VORTICITY drives the wave:
As air moves poleward (f increases), relative vorticity must decrease → anticyclonic turn
As air moves equatorward (f decreases), relative vorticity must increase → cyclonic turn
→ Propagation westward (retrogression) or stationary depending on mean flow
```

**Rossby wave propagation speed:**
```
c = U - β/k²
where: U = mean westerly wind speed
       β = ∂f/∂y = 2Ω cos(φ)/a (Rossby β parameter)
       k = wavenumber

Stationary Rossby wave: U = β/k² (when wave phase speed = 0)
Long waves (small k) propagate more slowly (or retrograde)
Short waves (large k) propagate faster eastward
```

---

## Atmospheric Boundary Layer (ABL)

The lowest ~1–2 km, where friction and surface heat fluxes are important:

```
DAYTIME:                    NIGHTTIME:
┌─────────────────────┐     ┌─────────────────────┐
│  Free troposphere   │     │  Free troposphere   │
├─────────────────────┤     ├─────────────────────┤
│  Entrainment zone   │     │  Residual layer     │
│  (ABL top ~1-2 km)  │     │  (~remnant daytime) │
├─────────────────────┤     ├─────────────────────┤
│  Mixed layer        │     │  Nocturnal inversion│
│  (turbulent, well-  │     │  (stable; radiation │
│   mixed by          │     │   cooling at        │
│   convection)       │     │   surface)          │
├─────────────────────┤     ├─────────────────────┤
│  Surface layer      │     │  Surface layer      │
│  (~10% of ABL)      │     │  (very stable)      │
└─────────────────────┘     └─────────────────────┘
  Ground heated by sun          Ground cooling by radiation
```

**Wind profile in ABL** — winds back (rotate counterclockwise, NH) and decrease in speed toward surface due to friction. Above the ABL, flow approaches geostrophic.

---

## Decision Cheat Sheet

| Observation | Dynamic Interpretation |
|-------------|------------------------|
| Wind flowing parallel to isobars | Geostrophic balance (above ABL) |
| Wind crossing isobars toward low | Friction (in boundary layer) or ageostrophic forcing |
| Strong ridge–trough pattern aloft | Rossby wave pattern; look for associated surface systems |
| Upper-level trough approaching surface low | Divergence aloft → surface cyclone intensification |
| Jet streak left exit region | Divergence → rising motion → convection favored |
| Temperature inversely related to height → strong capping | Stable layer; suppresses convection |

---

## Common Confusion Points

**Coriolis doesn't turn winds to low pressure** — The PGF is what pushes toward low pressure. Coriolis deflects the resulting motion to the right. The equilibrium (geostrophic) has winds flowing *parallel* to isobars, not toward low pressure. Low pressure is on the LEFT of the wind (NH).

**Why does the atmosphere rotate?** — Geostrophic balance means winds rotate counterclockwise around low pressure (cyclonic) and clockwise around high pressure (anticyclonic) in the NH. Not because of friction or anything mysterious — just PGF + Coriolis balanced. In SH, it's reversed.

**Rossby waves vs surface fronts** — Rossby waves are upper-level (300–500 mb) planetary-scale meanders. Surface fronts are boundaries between air masses driven by those upper-level waves. The surface frontal structure is largely "steered" by the upper-level flow.

**Jet stream speed and temperature gradient** — The jet stream is fastest where the horizontal temperature gradient is strongest (e.g., strong polar front in winter). A weaker equator-to-pole temperature gradient (as with Arctic warming) means a weaker, more meandering jet — associated with more persistent Rossby wave patterns and "blocking" events.
