# Soil Water: Field Capacity, Wilting Point, Hydraulic Conductivity

## The Big Picture

Water in soil exists on a continuum from completely saturated (all pores filled) to completely dry (all water molecules tightly adsorbed to mineral surfaces). Plants access only water held at tensions between roughly 33 kPa and 1,500 kPa — a specific "plant available water" window. Below and above that window, the water is either draining away by gravity or held too tightly for roots to extract.

```
SOIL WATER ENERGY STATES

  SATURATION (θs)                    ALL pores filled; O2 displaced
  |           matric potential = 0 kPa
  |
  |  GRAVITATIONAL DRAINAGE (hrs–days)
  |           Water drains by gravity; air returns to macropores
  |
  FIELD CAPACITY (θFC)               Macropores drained; mesopores full
  | (matric potential ~ -33 kPa)     --> UPPER LIMIT of plant available water
  |
  |  PLANT AVAILABLE WATER RANGE
  |  Roots extract water from mesopores
  |  Root-soil water potential equilibrium drives uptake
  |
  PERMANENT WILTING POINT (θPWP)     Only micropores + adsorbed water remain
  | (matric potential ~ -1500 kPa)   --> LOWER LIMIT of plant available water
  |           Stomata close; wilting permanent if not irrigated
  |
  AIR-DRY SOIL                       Very tightly adsorbed; hygroscopic water
  |           matric potential ~ -10,000 kPa
  |
  OVEN-DRY SOIL (0% MC)              Only mineral-adsorbed water remains
  |           matric potential ~ -1,000,000 kPa
```

---

## Section 1 — Matric Potential and Water Energy

### Soil Water Potential

Water moves in soil from regions of higher total potential to lower total potential. Total potential has several components:

```
  TOTAL WATER POTENTIAL:
  ψ_total = ψ_matric + ψ_gravitational + ψ_osmotic + ψ_pressure

  MATRIC POTENTIAL (ψm):
  Capillary + adsorptive forces holding water to soil matrix
  Always negative in unsaturated soil (water is at lower energy than free water)
  At saturation: ψm = 0
  At field capacity: ψm ≈ -33 kPa (1/3 bar)
  At wilting point: ψm ≈ -1500 kPa (15 bar)

  GRAVITATIONAL POTENTIAL:
  ψg = ρw × g × z (height above datum)
  Water flows downward under gravity when matric potential is low
  Drives drainage from saturated profiles

  OSMOTIC POTENTIAL:
  Solutes lower water potential; drives water across semipermeable membranes
  Important for: salt-stressed plants; plant water uptake

  PRESSURE POTENTIAL:
  Positive in saturated soil under a water table
  Important for: groundwater flow; artesian conditions
```

### Capillary Rise

```
  CAPILLARY RISE:
  h = 2T × cos(θ) / (ρw × g × r)

  Where:
    h = capillary rise height (m)
    T = surface tension of water (0.0728 N/m at 20°C)
    θ = contact angle (0° for clean silica = perfect wetting)
    ρw = water density (1000 kg/m³)
    g = 9.8 m/s²
    r = pore radius (m)

  TYPICAL CAPILLARY RISE BY TEXTURE:
  Sand (r = 0.1 mm): h ≈ 15 cm
  Loam (r = 0.01 mm): h ≈ 150 cm
  Clay (r = 0.001 mm): h ≈ 1500 cm = 15 m
  (But clay has very slow movement; fine pores resist flow)

  PRACTICAL: Clay soils can supply water from > 1 m depth by capillary flow
              but flow rate is very slow (Darcy velocity in cm/day)
```

---

## Section 2 — Field Capacity, Wilting Point, and Plant Available Water

### Field Capacity (FC)

Field capacity is the water content of a well-drained soil after gravitational drainage has essentially ceased — typically 1–3 days after full wetting.

```
  FIELD CAPACITY:
  Matric potential: approximately -33 kPa (-1/3 bar) for many mineral soils
  (Note: highly variable; sandy soils: -10 kPa; some soils: -50 kPa)
  Condition: all macropores have drained; mesopores still full
  Determination: laboratory pressure plate at -33 kPa or field measurement
                  2 days after irrigation/rain

  VOLUMETRIC WATER CONTENT AT FC (θFC):
  Sandy soil:    ~0.10–0.20 m³/m³ (10–20% by volume)
  Loam:          ~0.22–0.35 m³/m³
  Clay loam:     ~0.30–0.40 m³/m³
  Clay:          ~0.35–0.45 m³/m³
  Organic soil:  ~0.40–0.60 m³/m³
```

### Permanent Wilting Point (PWP)

```
  PERMANENT WILTING POINT:
  Matric potential: -1500 kPa (-15 bar) by convention
  Condition: stomata remain permanently closed; wilting is irreversible
             without re-wetting even when plant is placed in moist air
  Determination: laboratory pressure plate at -1500 kPa

  VOLUMETRIC WATER CONTENT AT PWP (θPWP):
  Sandy soil:    ~0.03–0.10 m³/m³
  Loam:          ~0.10–0.15 m³/m³
  Clay loam:     ~0.15–0.20 m³/m³
  Clay:          ~0.20–0.28 m³/m³

  WHY PWP VARIES WITH TEXTURE:
  Clay soils retain more water at -1500 kPa because:
  +-- More micropores that remain full at high tensions
  +-- Larger surface area for water adsorption
  But this water is unavailable (too tightly held for roots to extract)
```

### Plant Available Water Capacity (PAWC)

```
  PLANT AVAILABLE WATER CAPACITY:
  PAWC = (θFC - θPWP) × soil depth

  Example: Silt loam, 60 cm rooting depth
  θFC = 0.32 m³/m³; θPWP = 0.12 m³/m³
  PAWC = (0.32 - 0.12) × 600 mm = 0.20 × 600 = 120 mm of water

  PAWC BY TEXTURE (typical values per 30 cm depth):
  Sand:          ~25–35 mm per 30 cm
  Loamy sand:    ~30–45 mm per 30 cm
  Sandy loam:    ~45–70 mm per 30 cm
  Loam:          ~70–90 mm per 30 cm
  Silt loam:     ~90–110 mm per 30 cm  (HIGHEST; optimal texture)
  Clay loam:     ~70–90 mm per 30 cm
  Clay:          ~60–80 mm per 30 cm   (FC minus PWP is narrower despite high FC)

  IMPORTANT PARADOX:
  Clay soils have high total water content but LESS plant available water
  than silt loam because the PWP is also very high
  Silt loam has the maximum PAWC of any texture
```

---

## Section 3 — Darcy's Law and Hydraulic Conductivity

Darcy's Law (Henry Darcy, 1856) describes water flow through porous media. It is the fundamental equation of soil water movement.

```
  DARCY'S LAW:
  q = -K × (dh/dz)

  Or in 3D:
  q = -K × ∇H

  Where:
    q  = Darcian flux = volumetric flow rate per unit area (m/s; cm/hr)
    K  = hydraulic conductivity (m/s; cm/hr; mm/day)
    dh/dz = hydraulic gradient (change in hydraulic head / distance)
         = (ψm + z) per unit depth
    ∇H = gradient of total hydraulic head

  SATURATED HYDRAULIC CONDUCTIVITY (Ks):
  K when all pores are water-filled; maximum value
  Proportional to r⁴ (pore radius to the 4th power): Poiseuille's Law
  --> Macropores dominate saturated flow; even 1% macropores can carry 99% of flow

  UNSATURATED HYDRAULIC CONDUCTIVITY K(θ):
  Decreases dramatically as soil dries (pores drain; water moves only through films)
  K at FC: 10-100× less than K at saturation
  K at PWP: ~10-8× less than K at saturation

  RELATIVE MAGNITUDES:
  One earthworm burrow (5 mm diameter) = same K as 1 cm² of fine sandy loam
  This is why macropore flow (preferential flow) dominates in structured soils
```

### Hydraulic Conductivity by Texture

```
  SATURATED Ks BY SOIL TEXTURE:

  Texture             Ks (mm/hr)    Ks (cm/day)    Drainage class
  Coarse sand         >180           >400           Excessively drained
  Sand                100–180        240–400        Somewhat excessively drained
  Loamy sand          50–100         120–240        Somewhat excessively drained
  Sandy loam          25–50          60–120         Well drained
  Loam                12–25          30–60          Well drained
  Silt loam           6–12           15–30          Moderately well drained
  Sandy clay loam     1–6            2–15           Somewhat poorly drained
  Clay loam           0.5–1          1–2            Somewhat poorly drained
  Silty clay loam     0.1–0.5        0.25–1         Poorly drained
  Clay                < 0.1          < 0.25         Very poorly drained
  Organic (peat)      1–100          Variable       Variable (depends on humification)
```

---

## Section 4 — Preferential Flow

Preferential flow is the movement of water and solutes through a small fraction of the soil volume much faster than would be predicted by Darcy's Law applied to the average soil matrix.

```
  PREFERENTIAL FLOW TYPES:

  MACROPORE FLOW:
  Earthworm channels (5–10 mm): rapid gravitational drainage during rain
  Old root channels: linear continuity from surface to subsoil
  Structural cracks (Vertisols): significant bypass when dry soil wets
  Impact: fertilizer, pesticides, bacteria can bypass soil matrix entirely
          and reach groundwater or tile drainage in hours, not months

  FUNNEL FLOW:
  Textural discontinuities concentrate flow (water moves to coarse layer boundary)
  Example: silt loam over sand; water ponds at interface, then flows rapidly down
           funnel-shaped pathways in overlying fine material

  FINGERED FLOW (unstable wetting fronts):
  Occurs during infiltration into dry sandy soils
  Wetting front develops fingers instead of sharp planar advance
  Fingers carry water rapidly to depth; matrix between fingers stays dry

  ENVIRONMENTAL SIGNIFICANCE:
  Atrazine detected in groundwater within 24 hours of application
  under heavy rainfall in structured soils (macropore transport)
  Nitrate leaching: 30–50% may move via preferential flow pathways
  E. coli after manure application: can reach tile drains in 1 day
```

---

## Section 5 — Drainage and Irrigation Management

### Tile Drainage

```
  TILE DRAINAGE:
  Perforated pipes or clay tiles installed 0.8–1.5 m depth; 6–20 m spacing
  Remove excess water from saturated zone; lower water table
  Effect: increases air-filled porosity; enables field access in spring
  Cost: $500–2000/ha installation; 15–30 yr lifespan

  DRAINAGE RATIO:
  Drainage coefficient = maximum water removal rate (mm/day or in/day)
  Typical design: 12–25 mm/day for humid Midwest agricultural soils
  Corn root zone: must drain within 24–48 hr of saturation to avoid damage

  ENVIRONMENTAL TRADE-OFF:
  Benefits: higher crop yield; trafficability; soil aeration
  Costs: NO3- leaching increases (denitrification reduced in drained soil)
         Tile discharge contributes to stream flashiness
         Wetland drainage destroys ecosystem services
```

### Irrigation Scheduling

```
  IRRIGATION TIMING USING SOIL WATER:
  Irrigate when: θ < θFC - 50% PAWC (mild stress threshold)
  Or: when soil matric potential < -80 kPa (tensiometer threshold; crop-dependent)

  IRRIGATION AMOUNT:
  Irrigation depth = (θFC - θcurrent) × rooting depth
  Example: θFC = 0.32, θcurrent = 0.18, rooting depth = 700 mm
  Irrigation = (0.32 - 0.18) × 700 = 0.14 × 700 = 98 mm of water
  (adds water to refill profile to field capacity)

  REFERENCE EVAPOTRANSPIRATION (ET0):
  Penman-Monteith equation (FAO-56 standard):
  ET0 = f(net radiation, wind speed, vapor pressure deficit, temperature)
  Units: mm/day
  Crop ET = Kc × ET0 (Kc = crop coefficient; varies by growth stage)
  Corn at silking: Kc ~ 1.2; soil evaporation: Kc ~ 0.3–0.4
```

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| Which texture holds the most plant-available water? | Silt loam (PAWC ~90–110 mm per 30 cm depth) |
| What is field capacity and when is it relevant? | Water remaining after 1–3 days drainage; the upper limit for plant available water; target for irrigation |
| What does -1500 kPa matric potential mean? | Permanent wilting point; water held too tightly for roots to extract; plant wilts permanently |
| Why does clay have less plant available water than loam despite holding more total water? | Both FC and PWP are higher in clay; the difference (FC - PWP) is smaller |
| What is the dominant control on saturated hydraulic conductivity? | Pore size (r⁴ relationship); macropores created by earthworms/roots dominate despite small area fraction |
| What is preferential flow and why does it matter for contamination? | Water bypasses soil matrix through macropores; pesticides/bacteria reach groundwater in hours |
| How do you calculate plant available water capacity? | (θFC - θPWP) × rooting depth |

---

## Common Confusion Points

**Field capacity is not at the same matric potential in all soils.**
The conventional -33 kPa (-1/3 bar) threshold is an approximation valid for medium-textured soils. Sandy soils reach field capacity at -10 kPa; structured clay soils may not fully drain until -50 kPa. Site-specific calibration is important for precision irrigation.

**Wilting point is not where plants first experience water stress.**
Drought stress begins long before -1500 kPa. Stomata start closing around -100 to -300 kPa in most crop plants, reducing photosynthesis and growth. By -1500 kPa (PWP), the damage is already severe. Irrigation management uses a much earlier threshold.

**Darcy's Law applies to the average soil matrix, not to macropore flow.**
In structured soils (most agricultural soils), significant water movement occurs through macropores that violate Darcy's assumptions (steady-state, uniform porous medium). Macropore flow models are needed for accurate prediction of rapid drainage and contaminant transport.

**Capillary rise calculations assume smooth cylindrical pores — reality is more complex.**
Real soil pores are irregular, interconnected, and often partially blocked. Capillary rise equations give a maximum theoretical height; actual rise is limited by pore geometry, connectivity, and tortuosity. Never use capillary rise formulas to predict how high water will actually rise in a soil profile without field verification.
