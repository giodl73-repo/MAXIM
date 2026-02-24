# Extraction and Smelting

## The Big Picture

Smelting is **thermochemical reduction** — using heat and a reducing agent (carbon, electricity, hydrogen) to strip oxygen and sulfur from metal-bearing minerals. Every primary metal has its own chemistry; none is interchangeable.

```
ORE → CONCENTRATE → SMELTING → REFINING → PRIMARY METAL

Iron:
  Fe₂O₃ (hematite) → Blast furnace (coke + limestone) → pig iron → BOF/EAF → steel

Aluminum:
  Al₂O₃·xH₂O (bauxite) → Bayer process (leach) → alumina (Al₂O₃) → Hall-Héroult → Al

Copper:
  CuFeS₂ (chalcopyrite) → concentrating → flash smelting → matte → conversion → Cu
```

---

## Iron Ore and the Blast Furnace

### Iron Ore Types

| Ore | Chemical formula | Fe content | Notes |
|-----|-----------------|------------|-------|
| Hematite | Fe₂O₃ | 65–70% Fe | Best grade, preferred; direct ship |
| Magnetite | Fe₃O₄ | 65–70% Fe | Magnetic → beneficiation easy; requires pelletizing |
| Limonite | FeO(OH)·nH₂O | 35–55% Fe | Lower grade, hydrated |
| Taconite | Low-grade magnetite | 20–30% Fe | US iron range; requires pelletizing + beneficiation |
| Siderite | FeCO₃ | 48% Fe | Less common; calcined before use |

Low-grade ores require **beneficiation** before the blast furnace:
- Crushing and grinding
- Magnetic separation or froth flotation
- Pelletizing (agglomeration into 10–15mm balls for blast furnace burden)
- Sintering (fusing fine ore with coke breeze)

### Blast Furnace Chemistry

The blast furnace is a countercurrent reduction reactor: ore descends, hot gases rise.

```
┌──────────────────────────────────────────────────────────────┐
│                      BLAST FURNACE                           │
│                                                              │
│  CHARGE (top): Iron ore/sinter/pellets                       │
│                Coke (fuel + reducing agent)                  │
│                Limestone (CaCO₃ — flux)                      │
│                                                              │
│  ZONES (temperature increases downward):                     │
│                                                              │
│  1. Stack / Upper zone (200–500°C):                         │
│     H₂O driven off, indirect reduction begins               │
│     3Fe₂O₃ + CO → 2Fe₃O₄ + CO₂                            │
│     Fe₃O₄ + CO → 3FeO + CO₂                                │
│                                                              │
│  2. Bosh (600–900°C):                                       │
│     CaCO₃ → CaO + CO₂  (limestone calcination)             │
│     FeO + CO → Fe + CO₂  (final reduction)                  │
│                                                              │
│  3. Combustion zone / Tuyeres (~2000°C):                    │
│     2C + O₂ → 2CO  (coke + hot blast air)                  │
│     CO rises — is the primary reductant                     │
│                                                              │
│  OUTPUTS (from bottom):                                      │
│  Pig iron (liquid): ~94% Fe, 4–4.5% C, + Si, Mn, S, P     │
│  Slag (liquid): CaO·SiO₂·Al₂O₃ — floats on iron           │
│                 → granulated for cement, road base           │
│                                                              │
│  INPUTS (bottom): Hot blast air (1200°C), sometimes O₂     │
└──────────────────────────────────────────────────────────────┘

Net reaction: Fe₂O₃ + 3CO → 2Fe + 3CO₂
But actually a complex sequence of partial reductions;
CO₂ reacts with coke to regenerate CO (Boudouard reaction):
  CO₂ + C → 2CO  (at > ~700°C)
```

Key metrics of a blast furnace campaign:
- Coke rate: kg coke per tonne of hot metal (~350 kg/t modern; ~500 kg/t older)
- Productivity: tonnes of hot metal per m³ hearth volume per day
- Campaign life: 10–20 years between major relining

---

## Steelmaking: BOF vs EAF

Pig iron from the blast furnace is not steel — it's high-carbon cast iron (~4.5% C) that is hard and brittle. Steelmaking removes excess carbon and impurities.

### BOF — Basic Oxygen Furnace

```
BOF CYCLE (~40 minutes total, makes ~300 tonnes/heat)

CHARGE:
  Hot metal (pig iron, ~1400°C, ~70% of charge)
  Scrap steel (~30% of charge)
  Lime (CaO, flux)
  ↓
BLOWING (17–25 min):
  Pure O₂ blown through supersonic lance at ~Mach 2
  O₂ + C → CO + CO₂  (C burned off from 4.5% → <0.05%)
  O₂ also oxidizes Si, Mn, P → slag
  Temperature rises to ~1700°C from exothermic reactions
  No external heat needed — the carbon combustion provides it
  ↓
TAPPING:
  Steel tapped through tap hole into ladle (~1600°C)
  Slag poured separately
  ↓
SECONDARY METALLURGY (ladle furnace, RH degasser):
  Fine-tune composition: add alloys (Mn, Si, Nb, V, Cr)
  Desulfurization
  Vacuum degassing (removes H₂, N₂, O — critical for high-quality steel)
  ↓
CONTINUOUS CASTING (see 02-CASTING.md)
```

### EAF — Electric Arc Furnace

```
EAF CYCLE (~60–90 min, makes 50–200 tonnes/heat)

CHARGE:
  Scrap steel (80–100% of charge) — the recycling route
  Sometimes DRI (Direct Reduced Iron) or pig iron for lower residuals
  ↓
MELTING:
  3 graphite electrodes strike arc to scrap
  Temperature: up to 3000°C at arc
  Power input: 400–700 kWh/tonne
  ↓
REFINING:
  O₂ injection: burn remaining C
  Lime addition: form slag, remove P, S
  Temperature control to target ~1600°C
  ↓
TAPPING → secondary metallurgy → casting
```

### BOF vs EAF Comparison

| Parameter | BOF | EAF |
|-----------|-----|-----|
| Feed | 70% hot metal + 30% scrap | 80–100% scrap (or DRI) |
| Energy source | Chemical (carbon combustion) | Electrical (arc) + chemical |
| Energy consumption | ~0 external (exothermic) | ~400–700 kWh/tonne |
| CO₂ intensity | High (2t CO₂/t steel integrated) | Lower (0.4–0.6 t/t if green grid) |
| Heat time | ~40 min | ~60–90 min |
| Steel quality | Very low residuals (no scrap Cu, Sn contamination) | Residuals from scrap composition |
| Typical products | Flat-rolled sheet for auto / appliance | Long products (rebar, structural, sections) |
| Capital cost | Very high (integrated mill with blast furnace) | Moderate (mini-mill) |
| Trend | Declining share globally | Growing — green steelmaking path |

**Green steel**: Replace coke with green hydrogen as reductant:
  Fe₂O₃ + 3H₂ → 2Fe + 3H₂O (no CO₂)
  HYBRIT (SSAB/LKAB/Vattenfall) produced world's first fossil-free steel (2021)

---

## Direct Reduced Iron (DRI)

An alternative to blast furnace + BOF: reduce iron ore directly with syngas (CO+H₂) or H₂ in solid state — no melting, no coke.

```
DRI PROCESS (Midrex or HYL process):

  Iron ore pellets (shaft furnace) + Reducing gas (CO + H₂)
  Temperature: ~900°C (below melting point)
  Result: "Sponge iron" — solid, ~90–95% metallized Fe
  Density: porous, looks like a sponge (hence the name)

  DRI + EAF → high-quality steel with no blast furnace

  Advantage: can run on natural gas (lower CO₂ than BF route)
             can ultimately run on H₂ (zero-CO₂)
  Disadvantage: DRI is pyrophoric (reacts with air/water) → handling challenge
               Residuals from ore gangue → need higher quality ore
```

---

## Aluminum: Hall-Héroult Process

### Why Aluminum Was Once Precious

Aluminum is the 3rd most abundant element in Earth's crust (~8%). Yet before 1886, aluminum was more expensive than gold. The Washington Monument's aluminum cap (1884) was a prestige material.

The problem: aluminum is found exclusively in compounds (Al₂O₃, silicates) — never as native metal. The Al-O bond is extremely strong (→ Al is an excellent reducing agent, which is why thermite works). Carbothermic reduction (blast furnace approach) doesn't work for Al.

### Bayer Process (1887) — Ore to Alumina

```
BAUXITE (Al₂O₃·xH₂O + Fe₂O₃ + SiO₂ + TiO₂)
     │
     ▼ Dissolve in hot NaOH (240°C, 35 atm)
     │   Al₂O₃ + 2NaOH → 2NaAlO₂ + H₂O
     │   Fe₂O₃, TiO₂ don't dissolve → "red mud" (toxic waste problem)
     ▼
SODIUM ALUMINATE SOLUTION (clarified)
     │
     ▼ Cool + seed with Al(OH)₃ crystals → precipitation
     │   NaAlO₂ + 2H₂O → Al(OH)₃ + NaOH
     ▼
ALUMINUM HYDROXIDE → calcine at 1000°C → Al₂O₃ (alumina, white powder)

4–6 tonnes bauxite → 2 tonnes alumina → 1 tonne aluminum
```

### Hall-Héroult Process (1886) — Alumina to Aluminum

Independently invented by Charles Hall (US) and Paul Héroult (France) in the same year, 1886. Both were 22 years old. This simultaneous invention dropped aluminum price by 99%.

```
HALL-HÉROULT ELECTROLYTIC CELL:

    Carbon anodes (+) →
   ┌─────────────────────────────────────────────────┐
   │  Molten cryolite (Na₃AlF₆) electrolyte, ~960°C │
   │  with dissolved Al₂O₃ (~2–8%)                  │
   │  (cryolite lowers melting point of Al₂O₃       │
   │   from 2072°C to ~960°C — crucial innovation)  │
   └─────────────────────────────────────────────────┘
    Carbon cathode lining (-) ←
                    ↓
            Liquid aluminum collects on bottom
            (density > molten electrolyte — sinks)
            Tapped periodically

ELECTRODE REACTIONS:
  Cathode: Al³⁺ + 3e⁻ → Al(l)
  Anode:   2O²⁻ → O₂ + 4e⁻
           O₂ + C (anode) → CO₂ (anode consumed — cost ~0.4 kg C/kg Al)
  Net:     2Al₂O₃ + 3C → 4Al + 3CO₂

ENERGY: ~13–15 kWh per kg of aluminum
  → Aluminum is "congealed electricity"
  → Smelters locate near cheap hydropower (Pacific Northwest, Iceland, Norway, Quebec)
  → Recycling uses only ~5% of the energy of primary production — massive advantage
```

Key numbers:
- World aluminum production: ~70 million tonnes/year
- Electricity cost: ~40% of smelter operating cost
- Anode effect: if alumina level drops too low → CF₄ + C₂F₆ (GHG) — must prevent

---

## Copper: Flash Smelting

Copper ores are sulfide-based (mostly chalcopyrite CuFeS₂). Processing route:

```
MINING → CONCENTRATING → SMELTING → CONVERTING → REFINING

1. Mining: open pit or underground; typical ore grade 0.3–2% Cu
2. Concentrating: crush → grind → froth flotation → 20–30% Cu concentrate
3. Flash smelting (Outokumpu process):

   Concentrate + O₂ + SiO₂ (flux) blown into reaction shaft at 1300°C
   CuFeS₂ + O₂ → Cu₂S·FeS (matte, ~60–70% Cu) + FeO·SiO₂ (slag) + SO₂
   SO₂ captured → sulfuric acid (H₂SO₄) production — not waste, by-product

4. Pierce-Smith Converter:
   Matte blown with O₂ → blister copper (~98.5% Cu) + SO₂

5. Fire refining: remove O₂, residual S
   Blister copper → anode copper (99.5% Cu)

6. Electrolytic refining:
   Anode dissolves electrochemically; pure Cu plates on cathode (99.99% Cu)
   Anode slime: gold, silver, platinum group metals recovered — significant value
```

### Key Metals and Their Primary Routes

| Metal | Ore type | Primary process | Energy driver | Major producers |
|-------|---------|-----------------|---------------|----------------|
| Steel (Fe) | Hematite, magnetite | Blast furnace + BOF | Coke combustion | China, India, Japan |
| Aluminum (Al) | Bauxite | Bayer + Hall-Héroult | Electricity | China, India, Russia |
| Copper (Cu) | Chalcopyrite CuFeS₂ | Flash smelting + ER | Electricity (ER) | Chile, Peru, China |
| Zinc (Zn) | Sphalerite ZnS | ISP (pyrometallurgy) or RLE | Electricity (RLE) | China, Peru, India |
| Lead (Pb) | Galena PbS | Imperial smelting or QSL | Coke combustion | China, Australia |
| Nickel (Ni) | Laterites or sulfides | Flash smelt (sulfide) or HPAL | Electricity/heat | Indonesia, Philippines |
| Titanium (Ti) | Rutile/ilmenite | Kroll process (Mg reduction) | Mg + heat | Japan, Russia, Kazakhstan |

---

## Refining and Alloying

Primary smelter output is rarely used directly. Post-smelting:

```
PRIMARY METAL (pig iron, Al ingot, Cu cathode)
     │
     ▼
SECONDARY METALLURGY (for steel) / CASTING (for all)
  - Ladle furnace: fine alloy additions (Mn, Si, V, Nb, Cr, Mo, Ni)
  - Vacuum degassing: remove H₂ (causes porosity), N₂, O₂
  - Desulfurization: Ca injection → CaS → slag
     │
     ▼
ALLOY DESIGNATION
  Steel: AISI/SAE grades (1020, 4140, 316) or EN/DIN equivalents
  Aluminum: Temper designations: T6 = solution heat treated + artificially aged
             2024-T3: solution treated, cold worked, naturally aged
  Copper: UNS designations: C11000 (ETP copper), C26000 (cartridge brass)
```

---

## Decision Cheat Sheet

| Goal | Process |
|------|---------|
| Iron ore → steel | Blast furnace → BOF (integrated route) |
| Scrap → steel | EAF (mini-mill route) |
| Lower-CO₂ steel | EAF + green electricity; future: H₂ DRI + EAF |
| Bauxite → aluminum | Bayer process → Hall-Héroult electrolysis |
| Scrap aluminum → aluminum | Remelt + refine (uses 5% energy of primary) |
| Copper ore → conductor | Flash smelt → convert → electrorefine |
| Remove H₂/N₂ from steel | Vacuum degassing (RH, VOD, VD) |
| Add precise alloy content | Ladle furnace + FeSi, FeMn, FeV additions |

---

## Common Confusion Points

**Pig iron ≠ steel ≠ cast iron**
Pig iron (~4.5% C) is the blast furnace product — not useful directly. Cast iron (2–4% C) is pig iron that's been cast and used as-is (engine blocks, cookware). Steel (< 2% C, typically < 1%) is pig iron with carbon removed in BOF/EAF. The key transition is carbon removal.

**Coke ≠ coal**
Coke is coal that has been heated to ~1100°C in an oxygen-free oven (coking), driving off volatile matter (tar, BTX, ammonia). What remains is nearly pure carbon — strong enough structurally to support a blast furnace burden. Not all coal can be converted to metallurgical-grade coke (coking coal is a specific scarce resource).

**Hall-Héroult consumes the anodes**
The carbon anodes in an aluminum cell are oxidized: C + O²⁻ → CO₂. Each tonne of aluminum requires ~400 kg of carbon anode. Anode fabrication (baked carbon blocks from petroleum coke + pitch) is a major ancillary industry. Inert anodes that don't oxidize are a major research goal (would produce O₂ instead of CO₂).

**Electrolytic refining is not electrolytic smelting**
Hall-Héroult electrolyzes a molten salt to extract Al from a compound — this is electrolytic smelting. Copper electrorefining starts with impure solid copper anodes, dissolves them electrochemically, and plates pure copper at the cathode — this is electrorefining. Both use electrolysis but for very different purposes.

**Slag is not waste — it's a co-product**
Blast furnace slag is sold as ground granulated blast furnace slag (GGBFS), a cement supplementary material that reduces CO₂ by substituting clinker. Steel slag is used as road base aggregate. Copper anode slimes (containing Au, Ag, PGMs) can be worth more than the copper itself.
