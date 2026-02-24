# Irrigation — Water Delivery, Efficiency, Salinization

## The Big Picture

Irrigation enables agriculture where rainfall is insufficient or unreliable. It covers ~20% of cropland but produces ~40% of global food — the most productive land on Earth. But it comes at a cost: 70% of global freshwater withdrawals, depletion of fossil aquifers, salinization of ~20% of irrigated land, and downstream ecosystem destruction. Precision water delivery is arguably agriculture's most critical efficiency challenge.

```
+---------------------------------------------------------------+
|              IRRIGATION SYSTEM OVERVIEW                        |
|                                                                |
|  WATER SOURCES:                                                |
|  Surface: Rivers, canals, reservoirs, lakes                   |
|  Groundwater: Wells pumping aquifers                          |
|  Treated wastewater: Increasing (Israel, Singapore)           |
|                                                                |
|  DELIVERY METHODS    EFFICIENCY (applied/evapotranspired)     |
|  ───────────────────  ─────────────────────────────────────  |
|  Flood/surface       50-65%  (significant deep percolation)  |
|  Sprinkler           70-80%  (wind drift + evaporation)      |
|  Drip/micro          85-95%  (direct to root zone)           |
|  Subsurface drip     90-95%  (below evaporation)             |
|                                                                |
|  WATER BUDGET: ET demand = crop water need                   |
|  Effective rainfall + Irrigation = ET + leaching fraction    |
+---------------------------------------------------------------+
```

---

## Water Requirements — Crop ET

**Evapotranspiration (ET)** = combined water loss from soil evaporation + plant transpiration. This is what crops actually need.

```
REFERENCE ET (ETo): ET from a reference crop (grass) under given climate
  Calculated from: temperature, humidity, wind, solar radiation
  (Penman-Monteith equation — FAO standard)

CROP ET (ETc) = ETo × Kc
  Kc = crop coefficient (varies by growth stage)
  Kc initial (germination): 0.3–0.4
  Kc mid-season (full canopy): 1.0–1.3 (depends on crop)
  Kc late (maturity): 0.6–0.9

WATER STRESS: When soil water < critical threshold, crop experiences stress
  Stomata close → less CO₂ → reduced photosynthesis and yield
  "Turgor loss point" = wilting; cells collapse
```

**Crop water requirements (approximate annual totals):**

| Crop | ET (mm/season) | Sensitivity |
|------|---------------|-------------|
| Wheat | 300–450 | Medium |
| Rice (flooded) | 800–1200 | High (requires standing water) |
| Maize | 400–600 | High at pollination |
| Cotton | 700–1000 | Medium |
| Sugarcane | 1200–1500 | High |
| Tomato (drip) | 400–600 | High at fruit set |
| Olives | 250–400 | Drought tolerant |
| Alfalfa | 800–1400 | Very high; year-round |

---

## Surface Irrigation Methods

**Flood (basin) irrigation** — entire field flooded from inlet:

```
         WATER INLET
              ↓
 _______________________________________________
|               FLOODED FIELD                   |
|_______________________________________________|

SUITABLE FOR: Paddy rice (essential for anaerobic soil; controls weeds)
              Level fields only
EFFICIENCY: 40-65%
PROBLEMS: Significant deep percolation and surface runoff
          Saturation → anoxia for non-paddy crops
          Requires precise leveling (now done with laser-leveling)
```

**Furrow irrigation** — water runs down channels between raised crop rows:
- Better than flood for row crops (water not on plant leaves)
- Efficiency 55–65%
- Tailwater runoff can be captured and recycled

**Border strip irrigation** — thin sheets of water across sloped strips:
- Hay, small grains
- Efficiency 60–75% when managed well

---

## Sprinkler Irrigation

Water pressurized and distributed through nozzles:

```
TYPES:
  Solid-set: Permanent risers + stationary nozzles
             (orchards, high-value crops)

  Center pivot: Rotating arm on towers circling well/pump
                (up to 800m arm; covers circular field)
                → Distinctive circles seen from satellites over US Plains

  Linear move: Same as pivot but travels linearly
               (rectangular fields)

  Traveling gun: Single large nozzle pulled across field
                (less common; high pressure, wind-sensitive)

EFFICIENCY: 70-80% (evaporation from droplets, canopy interception, wind drift)
APPLICATION: Most adaptable; can apply on uneven terrain
PROBLEMS: Wet foliage → fungal diseases; high energy costs (pressure needed)
```

**Rain guns and micro-jets** — smaller sprinklers for trees (under-tree irrigation): 75–85% efficiency.

---

## Drip Irrigation — Precision Water Delivery

Water delivered directly to root zone through emitters on tubes:

```
SURFACE DRIP:           SUBSURFACE DRIP (SDI):
Tubing on surface       Tubing buried 30-50 cm below surface
     ↓                        ↓
Emitters at plant         Emitters at root zone
base (0.5–4 L/hr)        Below evaporation → higher efficiency
                          Below tillage → permanent installation

EMITTER SPACING: 10-50 cm (depends on soil and crop)
WORKING PRESSURE: 0.5–1.5 bar (low; unlike sprinkler)

ADVANTAGES:
  Efficiency 85-95% (only wets root zone)
  Fertigation: dissolve fertilizer directly in water → precision
  Lower disease pressure (no wet foliage)
  Works on any terrain
  Reduces weed germination (inter-row stays dry)

DISADVANTAGES:
  High capital cost ($500–2000+/ha installation)
  Emitter clogging (requires filtration)
  Rodent damage (surface drip)
  Requires monitoring (can't see if working)
```

---

## Salinization — The Slow Agricultural Disaster

Irrigation water always contains dissolved salts. Evapotranspiration removes pure water; salts remain and accumulate:

```
SALT ACCUMULATION PROCESS:
  Irrigation water (low salt) → Crop evapotranspiration removes water
                              ↓
  Residual salt concentration increases in root zone
  If drainage is poor:
  → Salt builds up in soil over years → decades
  → Electrical conductivity (EC) rises beyond crop tolerance
  → Osmotic stress (plant can't extract water even if present)
  → Reduced yields → abandoned fields

EXTENT:
  ~20% of world's irrigated land (30 million ha) significantly affected
  An estimated 2000 ha/day lost to salinization
  1.5 million ha abandoned to salinization per year globally
  Ancient Mesopotamian collapse partly attributed to soil salinization
```

**Crop salt tolerance (ECe threshold before yield loss begins):**

| Crop | ECe (dS/m) | Tolerance |
|------|-----------|-----------|
| Strawberry | 1.0 | Sensitive |
| Onion | 1.2 | Sensitive |
| Bean | 1.0 | Sensitive |
| Maize | 1.7 | Moderate |
| Wheat | 6.0 | Tolerant |
| Cotton | 7.7 | Tolerant |
| Barley | 8.0 | Very tolerant |
| Sugar beet | 7.0 | Tolerant |
| Date palm | 4.0 | Moderate |

**Leaching fraction** — deliberate over-irrigation to push salts below root zone:
```
LF = ECw / (5 × ECe - ECw)
(fraction of applied water that must leach below root zone)

Requires: drainage (tile drains, surface outlets) to remove leached salt
Without drainage: leaching just raises water table → secondary salinization
```

**Remediation:** Gypsum (CaSO₄) application replaces Na⁺ with Ca²⁺ on exchange sites → Na leaches. Expensive. Prevention far better than cure.

---

## Groundwater Depletion — The Hidden Crisis

Many of the world's most productive agricultural regions depend on "fossil" aquifers:

```
CRITICAL AQUIFER SITUATIONS:

OGALLALA AQUIFER (US Great Plains):
  ~450,000 km²; recharge: 1 cm/yr; extraction: ~30 cm/yr
  Powers irrigation of ~5 million ha (wheat, corn, sorghum, cotton)
  Water table declining 1–3 m/year in heavily pumped areas
  Estimated remaining economic life: 25–50 years in some areas
  (Kansas, Texas panhandle most affected)

INDUS PLAINS (Pakistan/India):
  ~16 million ha irrigated (world's largest contiguous irrigation system)
  Groundwater depletion 20–25 mm/yr in Punjab
  Dependent on Himalayan glacier melt + monsoon + pumping

NORTH CHINA PLAIN:
  Feeds ~200 million people; wheat + maize
  Water table declining 1–3 m/yr
  By satellite (GRACE): 8 km³/yr water loss
```

**The fundamental problem:** Groundwater depletion is invisible (unlike surface water), politically difficult to regulate (diffuse ownership), and essentially irreversible on human timescales.

---

## Decision Cheat Sheet

| Irrigation situation | Best approach |
|---------------------|--------------|
| High-value fruit/vegetable crop | Surface or subsurface drip; precision fertigation |
| Paddy rice | Flood irrigation essential (anaerobic conditions required) |
| Large-scale grain on flat terrain | Center pivot sprinkler |
| Saline water source | Salt-tolerant varieties; leaching fraction; drainage |
| Water-scarce region | Deficit irrigation (deliberately under-irrigate at less sensitive stages) |
| Sloping terrain, erosion risk | Sprinkler or drip; not flood |
| Over-irrigated soil with waterlogging | Install tile drainage; check irrigation scheduling |

---

## Common Confusion Points

**Irrigation "efficiency" doesn't mean water saved at basin scale** — High-efficiency drip reduces field losses, but if "losses" (percolation, runoff) were returning to aquifer or river, basin-scale water availability doesn't change. Efficiency matters most when percolation goes to saline groundwater or to evaporative sinks with no return.

**Rice is inherently water-intensive but not wasteful in all contexts** — Flooded rice transpires ~500–1200 mm but standing water also cools the crop, suppresses weeds, and in many Asian systems recharges shallow aquifers and supports fish/duck polyculture. "Alternate wetting and drying" (AWD) can cut water 30–50% with small yield loss and is gaining adoption.

**Salinization ≠ just in deserts** — Salinization occurs anywhere with irrigation + poor drainage + any evaporative water loss. The Imperial Valley (California), Murray-Darling Basin (Australia), and Po Valley (Italy) all have salinization problems despite non-desert climates.

**Drip's economic case depends entirely on water price** — Where water is cheap (surface irrigation rights), drip's capital costs don't pay back. Where water is scarce/expensive (Israel, California), drip is economically compelling. Policy (water pricing reform) often matters more than technology.
