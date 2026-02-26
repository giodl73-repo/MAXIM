# Drying & Firing — Greenware, Bisque, Cone System, Kiln Types

## The Big Picture

Firing is the transformation: plastic clay → permanent ceramic. Every step in the kiln has a specific chemical reaction. Understanding the sequence means understanding why slow cooling through 573°C matters, why organic materials must burn out before reduction, and why earthenware must be glazed to hold water.

**Process control bridge:** A kiln firing schedule is a programmed thermal profile — the ceramic analog of a reflow oven profile in PCB assembly or a crystal growth recipe in semiconductor fab. The controller tracks temperature vs time, holds at specific setpoints to complete reactions (dehydroxylation, carbon burnout), then ramps through critical phase transition points (573°C quartz inversion) at controlled rates. Modern electric kilns run PID controllers with programmable multi-segment ramps. The failure modes map directly onto process control concepts: overshoot at 573°C = thermal shock cracking; insufficient hold at 600°C = carbon trapping in reduction atmosphere = black core in porcelain. The "heat-work" concept (effect depends on both temperature and time, not temperature alone) is identical to the Arrhenius-based accumulated thermal exposure in solder joint reliability.

```
FIRING SEQUENCE: TEMPERATURE VS TRANSFORMATION
===============================================

°C      Event                              What's happening
===     =====                              ================
100     Free water evaporates              Remaining surface moisture leaves
        (MUST be slow for thick work)       Steam can shatter wet clay

120–200 All free water gone                Clay feels bone dry

400–500 Organic burnout begins             Paper, organics combust (needs O₂)

500–600 DEHYDROXYLATION                    Al₂Si₂O₅(OH)₄ → metakaolinite + H₂O
        (irreversible transformation)       Structural -OH groups leave as steam
                                           Clay permanently changed; cannot re-wet

573     QUARTZ INVERSION                   α-quartz ⇌ β-quartz
        (both heating AND cooling)         2% volume change; thermal shock risk
                                           Must cool SLOWLY through 573°C on way down

600–900 Organic matter fully burned        Carbon gases CO, CO₂ must escape
        (earthenware organic burnout)       Reduction before this = carbon trapping

900–1000 SINTERING BEGINS                  Flux oxides (feldspar → K₂O, Na₂O)
                                           begin melting; glass phase forms;
                                           pores start filling

1000–1100 Earthenware fully fired         Partial vitrification; some porosity
          (Cone 06 to ~Cone 2)             remains unless glazed

1050+   MULLITE NUCLEATION                 3Al₂O₃·2SiO₂ needles grow
        (primary strengthening phase)       in glass matrix → strength ↑

1200+   Stoneware vitrification            Extensive glass phase; body dense,
        (Cone 4–6 range)                   low porosity

1280+   Porcelain maturation               High glass + mullite; translucency
        (Cone 8–10+)                       in thin walls; maximum density
```

---

## The Cone System

```
ORTON PYROMETRIC CONES
=======================

What they are: small ceramic pyramids designed to melt and bend
               at specific conditions; used to verify actual kiln
               atmosphere and heat-work, not just temperature

Why not just use a thermometer?
 Ceramics respond to HEAT-WORK: combination of temperature AND time
 Firing at 1,200°C for 1 hour ≠ firing at 1,260°C for 10 minutes
 A cone bends when the clay body receives enough heat-work
 → better indicator of maturation than temperature alone

 Instrumentation analog: thermocouples measure instantaneous temperature
 (dose rate); cones measure accumulated heat-work (cumulative dose) — same
 distinction as radiation dose rate (mGy/hr) vs integrated dose (Gy).
 A thermocouple tells you where you are; a cone tells you what the material
 has actually experienced. Both are needed.

WITNESS CONES (three in a set):
 Guide cone (one number BELOW target): begins bending first
 Firing cone (target): should bend to 90° at peak
 Guard cone (one number ABOVE target): should not have bent

CONE NUMBER SYSTEM (Orton, standard for US/Canada/global):
 010, 09, 08, 07, 06...LOW                      HIGH...10, 11, 12, 13, 14
 ←——————————————————————————————————————————————————————→
 LOW FIRE                  MID FIRE          HIGH FIRE

KEY CONES AND APPROXIMATE TEMPERATURES (at standard firing rate 150°C/hr):
Cone 022: ~600°C   Luster firings; overglaze enamels (lowest)
Cone 018: ~696°C   Typical overglaze enamel range
Cone 015: ~790°C   Overglaze colors
Cone 010: ~919°C   Low bisque; luster
Cone 06:  ~999°C   Standard low-fire earthenware; majolica
Cone 04:  ~1,063°C Low bisque for stoneware
Cone 02:  ~1,120°C Low-fire limit; some stoneware bisque
Cone 4:   ~1,186°C Mid-fire stoneware
Cone 6:   ~1,222°C Common studio mid-fire
Cone 8:   ~1,263°C High stoneware
Cone 10:  ~1,285°C Classic high-fire stoneware
Cone 13:  ~1,350°C Some porcelain
Cone 14:  ~1,400°C High porcelain; some technical ceramics

Note: temperatures vary with firing rate. Faster firing rate =
       cone bends at higher temperature for same cone number.
       The Orton Foundation publishes conversion tables.
```

---

## Bisque Firing

The first firing. Converts raw greenware into bisqueware — permanently transformed, porous, and ready to glaze.

```
BISQUE FIRING PARAMETERS
=========================
Temperature:  Low bisque: Cone 010–08 (~900–950°C)
              Standard: Cone 06–04 (~1,000°C for earthenware;
              Cone 08-06 for stoneware/porcelain bodies)
Atmosphere:   Oxidizing (electric is default; gas with damper open)
              Must burn out all organics before reducing atmosphere
Duration:     8–12 hours typical (slow ramp to ensure water out)

BISQUEWARE PROPERTIES:
 Porous → absorbs glaze well (glaze "grabs" the surface)
 Hard enough to handle during glazing
 Still reactive to glaze bonding in glaze fire
 Not vitrified → color is body color before flux melting

SINGLE-FIRE (RAW GLAZING) ALTERNATIVE:
 Chinese traditional: glaze applied to greenware; single firing
 Pros: one firing saves fuel and kiln time
 Cons: higher skill required; glaze/clay shrinkage matching critical
       slip-glazes can be used; some industrial bodies designed for this
```

---

## Glaze Firing (Glost Firing)

The second (and usually final) firing. Glaze melts, flows, and bonds permanently to the body.

```
GLAZE FIRING PROCESS
=====================
Kiln loading:
 Kiln wash on shelves (alumina + silica; prevents pieces fusing to shelf
 if glaze runs; renewed periodically)
 Pieces must NOT touch each other (glazed surfaces would fuse)
 Stilts (for earthenware) support glazed bases
 Stoneware/porcelain typically unglazed foot ring (placed directly on shelf)

Temperature sequence:
 Ramp slowly to 600°C (burn off any remaining organics, wax resist)
 Increase rate to 150–200°C/hr to peak
 Peak soak: 10–30 minutes at peak temperature
            Allows temperature equalization throughout kiln
 Cooling: controlled to 573°C (quartz inversion — slow here)
          Free below 573°C

Glaze maturing:
 Silica+flux begins melting ~800°C
 Full melt and flow occurs at maturation temperature
 Surface tension draws glaze smooth
 Glaze bonds chemically to clay body at boundary layer
```

---

## Kiln Types

```
ELECTRIC KILN
=============
Heating element: Kanthal (FeCrAl alloy) coils or rods
                 Kanthal A1: up to Cone 6–8; standard
                 Super-kanthal (MoSi₂): Cone 10+
Temperature uniformity: excellent (thermocouple + controller)
Atmosphere:      Oxidizing only (no combustion)
                 Cannot produce reduction effects without special methods
                 (saggar with carbon; reduction inserts)

ADVANTAGES: clean, safe, programmable, consistent, no fossil fuel
LIMITATIONS: no natural reduction effects; limited to Cone 10 typically
             (higher = expensive high-temp elements)

Electric kilns dominate:
 Schools (safety); small studios; commercial production; technical ceramics

GAS KILN
========
Fuel:       Natural gas or propane
Burner:     Venturi or forced-air burners; 2–12+ burners typical
Atmosphere: CONTROLLABLE
            Oxidation: sufficient air for complete combustion
            Reduction: reduce air damper → CO forms → reduces metal oxides

Types:
 Updraft: simple; heat rises from bottom; floor pieces overtire
 Downdraft: flue at bottom forces hot gas to flow down → back up → out;
             better temperature uniformity

GAS KILN ATMOSPHERE CONTROL:
 Heavy reduction: close primary air → strong CO → dramatic effects
  - Iron: Fe₂O₃ → FeO → Fe³⁺ (red) becomes Fe²⁺ (blue-green, celadon)
  - Copper: Cu²⁺ → Cu⁰/Cu⁺ → copper reds (sang de boeuf) — famous Song effect
 Neutral: balanced; minimal color shift
 Oxidation: open flue; full combustion → clean colors

Reading the kiln: flame color and smoke indicate atmosphere
 Clear flame, no smoke = oxidation
 Orange flame, some smoke = light reduction
 Black smoke = heavy reduction (also carbon deposition risk)

WOOD KILN
=========
Types:
 Anagama: single-chamber tunnel kiln; Japanese origin; long chamber;
           stoking hole at front; single flue at back
           Firing: 3–5 days; constant team stoking; very high temperature
           Effects: ash glaze (wood ash settles on ware → silica + K₂O/CaO
                    glaze naturally), "flashing" (color variations from
                    ash and flame paths), carbon trapping

 Noborigama: multi-chamber climbing kiln; Japanese (Arita, Shigaraki);
              each chamber uses hot gas from chamber below; efficient fuel use

Ash glaze formation:
 Wood ash: K₂O + CaO + SiO₂ (varies by wood species)
 Ash settles on hot clay surface → reacts with clay's silica
 → natural ash glaze only where ash reaches (exterior facing fire)
 → unglazed or differently glazed on sheltered sides

SALT / SODA KILN
================
Salt glaze: Rock salt (NaCl) thrown into kiln at ~1,260°C peak temperature
 Sodium vapors (NaO) react with surface silica of clay body:
 2NaCl + SiO₂ → Na₂SiO₃ (sodium silicate glaze) + Cl₂
 Result: "orange peel" texture on exterior surfaces;
         interior and sheltered surfaces NOT glazed (sodium doesn't reach)
 Traditional: German Rhineland stoneware (16th century); still used

Soda glaze: sodium bicarbonate (NaHCO₃) or sodium carbonate sprayed in
             Easier to control; less chlorine emission; environmental advantage

Characteristics: texture resembles orange peel; vitreous but not smooth;
                  captures marks from kiln environment; distinctive aesthetic
```

---

## Firing Atmospheres in Detail

```
OXIDATION vs REDUCTION COMPARISON
===================================

OXIDATION                          REDUCTION
(sufficient O₂ in kiln)            (insufficient O₂; CO forms)
================                   ================
Fe³⁺ state                         Fe²⁺ state
→ red, orange, tan, brown          → gray, green (celadon), black (tenmoku)

Copper: Cu²⁺                       Copper: Cu⁰ / Cu⁺
→ turquoise, green                  → copper red! (sang de boeuf, flambe)

Cobalt: blue (same)                Cobalt: blue (same — atmosphere-stable)

Manganese: purple, brown           Manganese: similar

Clean body and glaze colors        Unpredictable beauty; dramatic effects

Easy to achieve (electric)         Requires gas/wood kiln skill;
                                    timing and degree of reduction critical

REDUCTION TIMING:
 Light early reduction (600–800°C): carbon trapping (biscuit body)
 Reduction at peak (1,200–1,280°C): affects glaze color
 Post-firing reduction (raku): carbon effects; metallic lusters
```

---

## Kiln Furniture

```
KILN FURNITURE
==============
Purpose: support ware during firing; separate pieces; allow circulation

MATERIAL: Cordierite (Mg₂Al₄Si₅O₁₈)
 Exceptional thermal shock resistance
 Low thermal expansion coefficient
 Withstands rapid heating/cooling without cracking
 Standard for kiln shelves worldwide

TYPES:
 Shelves (flatware): 12"×12" to 18"×24" standard; 1/2" to 3/4" thick
 Posts: various heights; position shelves at different levels
 Kiln wash: alumina/silica powder + water; brushed on shelves;
            prevents glaze adhesion to shelf (critical!)
            Must be renewed when worn or flaked
 Stilts: three-point or star-shaped; supports glazed bases off shelf
         (for earthenware with glazed bottoms)
         Not used for stoneware/porcelain (foot ring unglazed)
 Saggers: cylindrical protective containers; used in wood/salt kilns
          to protect ware from ash or sodium vapors

KILN FURNITURE IS CONSUMABLE:
 Thermal cycling eventually cracks shelves
 Kiln wash degrades; must be reapplied
 Posts crack if improperly loaded
 Replace cracked furniture immediately (risk of piece damage)
```

---

## Cooling Protocols

```
CRITICAL COOLING POINTS
========================

DO NOT RUSH COOLING through:

600–550°C (quartz inversion zone):
 MUST cool slowly (30-60°C/hr or slower through this zone)
 α⇌β quartz inversion: 2% volume change
 Too rapid = thermal shock = cracks appearing after perfect firing
 "Dunting" = cracking from too-fast cooling or heating through inversions
 Rule of thumb: cool naturally without opening the kiln below 120°C minimum

100–200°C (residual steam):
 If any moisture entered kiln, steam can still cause problems
 Allow thermal equilibration at this range before opening

WHEN TO OPEN:
 Standard: kiln at ≤80°C → safe to open
            Impatient opening at 100–200°C risks: thermal shock on ware,
            burns to hands, cold air draft into hot kiln interior
```

---

## Common Confusion Points

**"Cone 06" is lower temperature than "Cone 6"**:
Counterintuitive numbering. The cone scale reads: Cone 022 (very low) → ... → Cone 06 → ... → Cone 1 → Cone 2 → ... → Cone 14 (very high). The "0" prefix indicates low-fire cones. Cone 06 ≈ 999°C; Cone 6 ≈ 1,222°C.

**Bisque temperature should be lower than glaze temperature**:
For most two-fire ceramics, bisque at Cone 06–04 and glaze fire at the body's maturation temperature (higher). The bisque fires the body just enough to handle and glaze, but leaves body porous enough to absorb glaze.

**Reduction at the wrong time traps carbon**:
If you apply heavy reduction before organic materials have fully burned out (~600–900°C range), carbon gets trapped in the clay body — leaving a black core visible in the clay body cross-section. Not necessarily a problem structurally but aesthetically obvious.

**Electric kilns can do reduction** (with effort):
Yes, with combustible materials (paper, wood chips, carbon-heavy materials) in a saggar, you can create local reduction in an electric kiln. Not as dramatic as gas reduction; more unpredictable; damages elements if overdone.

---

## Decision Cheat Sheet

| Goal | Firing Choice |
|------|--------------|
| Simple, reliable firing | Electric kiln, Cone 06 (earthenware) or Cone 6 (stoneware) |
| Celadon green (iron glaze) | Gas reduction kiln, Cone 10 |
| Copper red / sang de boeuf | Gas reduction kiln; precise atmosphere control |
| Natural ash glaze | Wood anagama kiln |
| Orange-peel texture exterior | Salt or soda kiln |
| Carbon flashing effects | Wood kiln or western raku |
| Bright commercial colors | Low-fire electric (Cone 06); overglaze enamels |
| Maximum density/strength | High-fire (Cone 10) stoneware |
| White translucent porcelain | Cone 10 (or higher) in oxidation or neutral |
