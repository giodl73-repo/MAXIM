# Heat Treatment

## The Big Picture

Heat treatment is **controlled heating and cooling to alter the microstructure of a metal** without changing its chemistry or shape. For steel, the iron-carbon phase diagram determines what phases are possible; the TTT/CCT diagrams determine which phases actually form given a particular cooling rate. Heat treatment is how you make the same steel composition into a spring, a gear, or a bearing — they differ only in thermal history.

```
HEAT TREATMENT GOALS AND PROCESSES:

  Goal                    Process              Mechanism
  ──────────────────────────────────────────────────────────────────────
  Soften for machining    Annealing            Full austenitize → slow cool → pearlite
  Normalize structure     Normalizing          Austenitize → air cool → fine pearlite
  Maximize hardness       Quenching            Austenitize → fast cool → martensite
  Reduce brittleness      Tempering            Reheat martensite → tempered martensite
  Surface hardness only   Case hardening       Enrich surface with C or N; then quench
  Age hardening (Al)      Precipitation HT     Dissolve → quench → age → precipitates

STEEL HEAT TREATMENT SEQUENCE:
  RAW STEEL
       │
  [Annealing] ─────────────────────── Soft, machinable state
       │                               Pearlite or spheroidite
       │
  [Machine to shape]
       │
  [Austenitize: ~750–950°C]
       │
  [Quench: oil/water/air]────────── Martensite (hard, brittle)
       │
  [Temper: 150–600°C] ──────────── Tempered martensite (tough, strong)
       │
  [Optional: case harden] ─────── Surface hardness + tough core

  Result: high strength + toughness (spring/gear/bearing steel)
```

---

## Iron-Carbon Phase Diagram

```
Fe-C PHASE DIAGRAM (simplified, 0–2.1% C, 0–1000 °C):

  Vertical axis: temperature in °C.
  Horizontal axis: carbon content (%C), 0 to ~1.2.

  Key isotherms and regions:
    1000 °C and above:     γ (austenite) phase region.
    912 °C (A₃ line):      boundary between α+γ region (left) and γ region.
    727 °C (A₁ line):      eutectoid temperature.
                           Below A₁: α + Fe₃C (pearlite) on the left;
                                     γ + Fe₃C (upper) on the right.
    Below 727 °C, low %C:  α (ferrite).
    Eutectoid composition: 0.77 %C.

CRITICAL TEMPERATURES:
  A₁ (eutectoid): 727°C — lower critical; below = no austenite stable
  A₃: upper critical for hypoeutectoid (< 0.77%C); above = fully austenite
  Acm: upper critical for hypereutectoid (> 0.77%C)
  Ac₁ / Ac₃: actual transformation on heating (c = chauffage, heating)
  Ar₁ / Ar₃: actual transformation on cooling (r = refroidissement, cooling)
  → Heating/cooling hysteresis: Ac temperatures higher than Ar temperatures

PHASES:
  Ferrite (α): BCC iron; soft (~80 HB); ductile; <0.02% C solubility
  Austenite (γ): FCC iron; nonmagnetic; 0.02–2.1% C solubility; exists above A₁
  Cementite (Fe₃C): 6.67% C; hard (~700 HB); brittle; iron carbide
  Pearlite: alternating lamellar (α + Fe₃C) at ~0.77% C; moderate strength
  Martensite: supersaturated α; BCT structure; carbon trapped → high hardness
  Bainite: intermediate (below pearlite, above Ms); acicular; tough

EUTECTOID REACTION:
  At 727°C, 0.77% C:
  γ (0.77%C) → α (0.02%C) + Fe₃C (6.67%C)  [slow cooling]
  This is pearlite formation — lamellar spacing depends on cooling rate
  Faster cooling → finer lamellae → higher hardness (fine pearlite harder than coarse)
```

---

## Annealing, Normalizing, Quenching, Tempering

### Annealing

```
FULL ANNEALING:
  Heat 30–50°C above A₃ (hypoeutectoid) or A₁ (hypereutectoid)
  → Fully austenitic
  Slow furnace cool (~25°C/hr) → coarse pearlite forms
  Result: softest possible state; maximum ductility; lowest strength
  Use: after hot working, before severe cold working or machining

PROCESS ANNEALING (subcritical annealing):
  Heat BELOW A₁ (~550–700°C)
  No austenitizing → no phase transformation
  → Relieves cold work (recrystallization); partial softening
  Use: between cold-drawing passes (wire, strip)

SPHEROIDIZING ANNEALING:
  Heat just below or cycle around A₁
  → Fe₃C in pearlite dissolves partially → spheroidizes (surface energy minimization)
  Result: spheroidite (globular carbide in ferrite matrix) → most machinable state
  Use: high-carbon steels (>0.6%C) that are otherwise difficult to machine
  Required: must start from pearlite or martensite + time at temperature

STRESS RELIEF ANNEALING:
  Below A₁ (~595–650°C) — same as PWHT for welding
  → No microstructural transformation; only residual stress relief via creep
```

### Normalizing

```
NORMALIZING:
  Heat 30–50°C above A₃ → fully austenitic
  Air cool (faster than furnace anneal; slower than quench)
  → Finer pearlite than full anneal → slightly harder + stronger + better toughness
  → More uniform microstructure (homogenizes composition gradients)

  Normalized vs Annealed:
    Normalized: fine pearlite; harder; better machinability for low-carbon steel
    Annealed: coarse pearlite; softest; better for high-carbon steel machining
    → Low-C steel: normalize (sufficient softness + better finish)
    → High-C steel: spheroidize anneal (coarse pearlite too hard to machine easily)
```

### Quenching

```
QUENCHING:
  Austenitize → rapidly cool below Ms (martensite start temperature)
  Martensitic transformation: diffusionless; shear mechanism; carbon trapped in BCT lattice

  HARDNESS DEPENDS ON CARBON CONTENT:
    0.2% C → max ~35 HRC
    0.4% C → max ~55 HRC
    0.6% C → max ~62 HRC
    0.8% C → max ~65 HRC  (approximately: max HRC ≈ 30 + 50×%C for %C < 0.5)

  QUENCH MEDIA (cooling severity, fastest to slowest):
    Brine (10% NaCl): very fast → most distortion/cracking risk
    Water:            fast → common for water-hardening tool steels
    Oil:              moderate → most common for alloy steels
    Polymer (PAG):    adjustable rate → modern alternative to oil
    Air:              slow → air-hardening grades (D2, H13) only

  DISTORTION AND CRACKING:
    Thermal gradients → differential expansion/contraction
    Martensite transformation: volumetric expansion ~4%
    Surface: cools and transforms first; core: lags
    → Residual stress: surface compression (often good for fatigue)
    → If gradient too steep: quench crack
    → Prevention: preheat before austenitizing; use slower quench medium;
                  austempering (hold in salt bath above Ms)

  MARTENSITE START / FINISH:
    Ms (martensite start): temperature at which martensite begins forming
    Mf (martensite finish): complete martensite (~0% austenite)
    Ms ≈ 530 − 350×(C%) − 40×(Mn%) − 20×(Cr%) − 10×(Mo%) − 17×(Ni%)
    → High C + alloy → low Ms → retained austenite (soft spots; dimensional instability)
    → Deep cryogenic treatment: sub-zero cooling to complete martensite transformation
```

### Tempering

```
TEMPERING:
  Reheat martensite below A₁ → tempered martensite
  Purpose: reduce brittleness; relieve residual stress; controlled hardness reduction

  STAGES OF TEMPERING:
    100–200°C: ε-carbide precipitation; some stress relief; slight hardness decrease
               → High hardness retained; use for wear parts, cutting tools, cold work
    250–350°C: ε-carbide → cementite; continued precipitation
               AVOID: "tempered martensite embrittlement" (blue brittleness) peak
    400–600°C: Fe₃C spheroidizes; increasing toughness; significant hardness drop
               → Structural steels (bolts, gears, shafts): temper here
    >600°C:    Approaching annealed state; coarse cementite; very tough, low hardness

  STRENGTH-TOUGHNESS TRADEOFF:
    Low temper temperature → high hardness → low toughness (brittle fracture risk)
    High temper temperature → lower hardness → high toughness
    Engineering: temper to meet toughness/hardness requirement simultaneously
    Charpy impact test: validates toughness at service temperature (especially sub-zero)

DOUBLE TEMPERING:
  High-alloy tool steels: temper twice (with air cool between)
  First temper: converts retained austenite to fresh martensite + tempers original
  Second temper: tempers the fresh martensite
  → Required for D2, M2, H13 etc.
```

---

## TTT and CCT Diagrams

```
TTT DIAGRAM (Time-Temperature-Transformation):
  Isothermal (constant temperature) diagram
  X-axis: time (log scale); Y-axis: temperature
  Curves mark START and FINISH of transformation at each temperature

  Temperature
    A₃ ─────────────────────────────────────────
    A₁ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─
        │                                         Pearlite start (nose)
        │                 ┌──── Pearlite finish
        │             ────┤
        │         ────    └────────────
    B─  │     ────  ←────── Bainite region
    s   │ ────────────────────────────────────
    Ms ─│─────────────────────────────── Martensite start
    Mf ─│─────────────────────────────── Martensite finish
         ──────────────────────────────────────►
         0.1s     1s     1min   1hr    time

  "NOSE" of TTT: shortest time to begin transformation (~550°C for most steels)
  To get martensite: cooling rate must exceed the critical cooling rate
    (cooling must reach Ms before touching the nose)

CCT DIAGRAM (Continuous Cooling Transformation):
  More relevant for practice (actual quenching is continuous, not isothermal)
  Similar shape to TTT but nose shifted right and down
  Shows transformation products for given continuous cooling curves
  → Oil cooling curve passing left of nose → martensite
  → Air cooling curve passing through nose → mixed pearlite/bainite/martensite

  PRACTICAL USE:
    From CCT: read off what microstructure you get for a given quench medium
    → Critical cooling rate: minimum rate to get 100% martensite
    → Alloy elements: shift nose to right → more time available → allows air or oil quench
```

---

## Hardenability (Jominy End-Quench Test)

```
HARDENABILITY DEFINITION:
  The ability of steel to be hardened (form martensite) to a given depth
  NOT the same as maximum hardness (which is a function of carbon content)

  Distinction:
    Carbon content → maximum hardness achievable at surface
    Hardenability → how deep through the section that hardness extends

JOMINY TEST (ASTM A255):
  Standard 1-inch diameter × 4-inch bar
  Austenitize at standard temp; water quench one end only → standard spray
  After quench: measure hardness at intervals from quenched end (HRC every 1/16")

  Result: Jominy curve → hardness vs distance from quenched end
    High hardenability steel: hardness stays high far from quenched end
    Low hardenability steel: hardness drops off rapidly

  Physical interpretation: distance from quenched end → cooling rate
    0 mm: fastest cooling (near water) → martensitic if carbon sufficient
    25 mm: moderate cooling → depends on hardenability
    50+ mm: slow cooling → pearlite/bainite even in hardened steel

FACTORS INCREASING HARDENABILITY:
  Carbon: increases hardness achievable (not hardenability by itself)
  Alloying elements (Cr, Mo, Ni, Mn, Si):
    → Shift TTT nose to right → slower critical cooling rate → deeper hardening
    Mo: most potent per weight; suppresses pearlite formation
    Cr: carbide former; increases both hardenability and hardness
    Ni: increases hardenability + toughness (no carbide formation)
    B (boron): extremely potent in trace amounts (0.0005–0.003%); affects grain boundary

IDEAL CRITICAL DIAMETER (DI):
  Section diameter that can be through-hardened with a theoretically infinite quench
  Used to compare hardenability of different steels and predict section response
```

---

## Case Hardening

```
CASE HARDENING PURPOSE:
  Combine: hard, wear-resistant surface + tough, ductile core
  Applications: gears (hard teeth; tough core absorbs impact), cams, shafts, bearing races

CARBURIZING:
  Process: expose low-carbon steel to carbon-rich atmosphere at 870–950°C
  Carbon diffuses into surface → carbon gradient from ~0.8% at surface to bulk ~0.2%
  After carburizing: quench + temper → hard case; tough core

  Types:
    Gas carburizing: atmosphere furnace with CH₄/CO/CO₂ mix → industrial standard
    Pack carburizing: steel packed in charcoal + BaCO₃ → batch; slower; old method
    Vacuum carburizing (LPC): low pressure; precise control; no intergranular oxidation
    Liquid carburizing: molten salt bath (NaCN-based) → fast but toxic cyanide

  Case depth: 0.1–2.5 mm depending on time, temperature, steel
  Surface carbon: 0.7–0.9% target (avoid excessive cementite → brittle)

NITRIDING:
  Process: expose steel to ammonia (NH₃) atmosphere at 480–550°C
  Nitrogen diffuses in → iron nitride (γ'-Fe₄N and ε-Fe₂₋₃N) compound layer + diffusion zone
  No quench required: hardening occurs during nitriding itself
  → Less distortion than carburizing + quench

  Properties: white layer (compound zone) → very hard (~70 HRC equivalent)
              diffusion zone → harder than core
  Applications: crank shafts, cam shafts, gears — precision parts

  Gas nitriding (traditional): NH₃ atmosphere 25–150 hr → thick case
  Plasma nitriding: ionized nitrogen; faster; controllable white layer thickness
  Salt bath nitriding (Tenifer/Ferritic Nitrocarburizing): 570°C; short time;
    moderate hardness; good corrosion resistance → automotive camshafts

INDUCTION HARDENING:
  Selective surface heating by induced eddy currents (electromagnetic induction)
  High-frequency coil surrounds part → rapid surface heating to austenitic
  Quench immediately → martensitic surface; core unchanged

  Not a diffusion process — no chemistry change; geometry-specific heating
  Time to heat: seconds; very fast; localized
  Applications: crankshafts (journals only), gear teeth, steering rack, valve seats
  Residual compressive stress: large (benefits fatigue life significantly)
```

---

## Precipitation Hardening (Aluminum)

```
AGE HARDENING MECHANISM:

  Most common: 2000/6000/7000 series Al alloys
  Requires: solid solubility that decreases with decreasing temperature

  THREE STAGES:

  1. SOLUTION TREATMENT (Solutionizing):
     Heat to ~500–540°C → all solute (Cu, Mg, Zn, Si) dissolves into solid solution
     → Uniform, single-phase alloy (α-Al, FCC, supersaturated)

  2. QUENCH:
     Rapid cooling → supersaturated solid solution (SSSS) at room temperature
     Solute atoms trapped in aluminum matrix → soft, ductile state (T4 temper)

  3. AGING (Precipitation):
     Hold at room temperature (natural aging) or elevated temperature (artificial aging)
     → Solute atoms cluster → form coherent precipitate zones → GP zones
     → GP zones → intermediate precipitates (θ', S', η', β')
     → Equilibrium precipitates (θ, S, η, β) — overaged state

HARDNESS vs AGING TIME:
     Hardness
        │                   Peak aging
        │              ╱────╲
        │         ╱────       ────╲
        │    ╱────                  ────╲ (overaging)
        │╱─                              ────
        └──────────────────────────────────────►
        T4                                       T7
        SSSS          Peak (T6)           Overaged

  UNDERAGED (T3/T4): GP zones forming; moderate strength; excellent formability
  PEAK AGED (T6): maximum strength; GP zone → coherent precipitates
  OVERAGED (T7): loss of coherency → precipitates coarsen → lower strength
                 but better: stress corrosion cracking resistance
                 7XXX alloys: T73 overaged for aerospace (better SCC vs T6)

TEMPER DESIGNATIONS:
  -T4: solution treated + naturally aged (room temp)
  -T6: solution treated + artificially aged (peak strength)
  -T651: T6 + stretching (stress relief) + artificial age
  -T73: overaged (7xxx alloys, SCC resistance)
  -T851: T8 (cold worked after quench) + stretch + age

ALLOY EXAMPLES:
  2024-T3 (Al-Cu-Mg): aerospace structure (wing skin)
  6061-T6 (Al-Mg-Si): general structural; weldable
  7075-T6 (Al-Zn-Mg-Cu): highest strength Al; aerospace
  7075-T73: same, overaged for SCC resistance
  6063-T5: extrusions (architectural); softer, excellent finish
```

---

## Decision Cheat Sheet

| Goal | Process |
|------|---------|
| Softest state for heavy machining | Spheroidize anneal (high-C) or full anneal (low-C) |
| Uniform fine microstructure, moderate strength | Normalize |
| Maximum hardness (surface + through) | Austenitize + water/oil quench |
| Hard + tough (most engineering applications) | Quench + temper (Q&T) |
| Hard surface + tough core, low-carbon steel | Carburize + quench + temper |
| Hard surface + tough core, precision/no distortion | Nitriding (no quench) |
| Selective surface hardening, localized | Induction hardening |
| Maximum strength in aluminum | Solution treat + T6 artificial age |
| High strength + SCC resistance (7xxx Al) | T73 overaging |
| Predict through-hardening depth | Jominy test + hardenability curve |

---

## Common Confusion Points

**Hardenability ≠ maximum hardness**
Carbon content determines maximum achievable hardness (HRC at the quenched surface). Hardenability (measured by Jominy test) determines how deep that hardness extends into the section. A high-carbon low-alloy steel can have high max hardness but poor hardenability — only the skin hardens. A lower-carbon alloy steel can through-harden a 3-inch diameter shaft.

**The TTT diagram shows isothermal transformation; real quenching is not isothermal**
CCT diagrams are more practically useful. The critical cooling rate from the CCT determines quench media selection. Engineers use CCT to verify whether oil quenching will produce full martensite in a given section, or whether water is needed. TTT is useful for understanding the thermodynamics; CCT is for process design.

**Tempering "embrittlement" is a specific phenomenon, not a general effect**
All tempering reduces hardness. "Tempered martensite embrittlement" (TME) occurs specifically in the 250–350°C range for many steels — hardness drops less than toughness, creating a peculiar brittle zone. "Temper embrittlement" (Cr-Mn steels, 450–600°C slow cool) is a different phenomenon: phosphorus segregation to grain boundaries during slow cooling or long hold. Neither is "tempering always causes problems" — they're specific conditions.

**Age hardening in aluminum is not heat treatment in the steel sense**
Steel heat treatment controls which phase forms (martensite vs pearlite). Aluminum precipitation hardening creates a supersaturated solution and then allows coherent precipitates to form. The strengthening mechanism is different: precipitates impede dislocation movement (obstacle hardening), not the martensite lattice distortion mechanism in steel.

**Induction hardening does not change the steel's chemistry**
It only changes thermal history — the same effect as quenching, but localized. The steel must have sufficient hardenability already. Induction-hardenable grades: 1045, 4140, 4340, 52100. Low-carbon steels (<0.3% C) cannot be meaningfully hardened by induction alone; they would need prior carburizing.
