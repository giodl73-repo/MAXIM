# Glass Science — Silicate Networks, Viscosity, Annealing, Tg

## The Big Picture

Glass is defined by its structure: a random network of SiO₄ tetrahedra with no long-range order. Understanding the structural chemistry explains every observable property — why it's transparent, why its expansion coefficient matters, why it anneals, why it devitrifies, and why different compositions have radically different working ranges.

```
SILICATE GLASS STRUCTURE
=========================

PURE SILICA (SiO₂ — fused silica):
  Si atom at center, 4 O atoms at corners — SiO₄ tetrahedron
  Each O bridging: shared between 2 Si atoms
  3D continuous random network
  Every oxygen = bridging oxygen (BO)
  Result: very high Tg (~1,200°C), very low CTE, high chemical durability
  Too refractory to work practically → must add modifiers

SODA-LIME-SILICA (add Na₂O + CaO):
  Na⁺ sits in network interstices
  Each Na₂O provides: one O that becomes NON-bridging oxygen (NBO)
                      breaks one Si-O-Si linkage
  NBOs weaken the network:
    ↓ Viscosity at any temperature   ↓ Tg
    ↑ Workability                    ↓ Chemical durability
  CaO (Ca²⁺): similar but each CaO provides one O → creates 2 NBOs
  Tradeoff: without Ca, Na-silicate glass dissolves readily in water;
            CaO restores chemical durability

ZACHARIASEN/WARREN CLASSIFICATION (1932):
  Network formers:   Small, high-charge cations; form glass alone
    SiO₂ (Si⁴⁺), B₂O₃ (B³⁺), P₂O₅ (P⁵⁺), GeO₂ (Ge⁴⁺)
  Network modifiers: Cannot form glass; break up network; lower Tg
    Na₂O, K₂O, CaO, MgO, BaO, PbO
  Intermediates:     Can substitute in network or act as modifier
    Al₂O₃ (usually network former, replacing Si), ZnO, TiO₂

BOROSILICATE GLASS STRUCTURE:
  B₂O₃ is also a network former (triangular BO₃ groups)
  At low modifier content: B acts as former → low CTE (boron anomaly)
  At higher modifier: B shifts to tetrahedral BO₄ → acts more like Si
  Net effect: borosilicate glass has lower Tg and lower CTE than
              pure silica while being workable at lower temperatures
```

---

## Viscosity and the Working Range

Glass shaping is viscosity management. Every forming technique operates at a specific viscosity window.

```
VISCOSITY REFERENCE POINTS — SODA-LIME GLASS
=============================================

Point            Temp (°C)  Log(η Pa·s)  Physical Meaning
—————————————    ——————————  ———————————  ——————————————————————————
Melting           ~1,500      ~1          Fluid homogeneous melt
Working point     ~1,100      ~3          Blow/press/draw; holds form briefly
Softening point   ~720        ~7.6        Glass deforms under own weight
Annealing point   ~550        ~12.4       Internal stresses relax in minutes
Strain point      ~515        ~13.8       Stresses fixed; glass "frozen"

BOROSILICATE vs SODA-LIME COMPARISON:
 Borosilicate working point: ~1,200°C (higher → needs hotter equipment)
 Borosilicate Tg: ~565°C (close to soda-lime)
 Borosilicate at working point is stiffer than soda-lime → harder to work
 Lampworkers use oxy-propane torch (hotter) for borosilicate

FUSED SILICA (pure SiO₂):
 Working point: ~2,200°C (extreme; special equipment required)
 Tg: ~1,200°C
 At 1,100°C (soda-lime working point), fused silica viscosity ~10¹⁷·⁵ Pa·s
  = completely solid; comparable to metallic solid
 Applications demanding fused silica must accept the processing difficulty

LEAD GLASS:
 Working point lower than soda-lime (~950-1,000°C)
 Easily worked; suitable for hand-cutting (softer)
 Historically preferred for fine handcraft tableware and optical glass
```

---

## Annealing

```
ANNEALING — WHY AND HOW
=========================

THE STRESS PROBLEM:
 Glass outer surface cools and stiffens first
 Interior cools later → contracts → inner layer tries to pull away
  from already-stiff outer layer
 Result: outer layer in compression; inner layer in tension
 In worst case: spontaneous fracture (the "stressed glass" pop)
 In less dramatic case: invisible residual stress → unpredictable breakage
  under later mechanical load

ANNEALING PROCESS:
 1. Bring glass to annealing point (stresses relax in minutes)
 2. Hold briefly to equalize temperature through thickness
 3. Cool SLOWLY and UNIFORMLY through annealing range
    → stresses relax continuously as they form
    → rate: slow enough that temperature gradient → stress < fracture stress
 4. Below strain point: cool freely (stresses now permanent but minimal)

COOLING RATES:
 Float glass lehr: large continuous ribbon; 60-100m long
  Typical rate: 5-20°C/minute through annealing range
 Thick pressed glass (lens blanks): much slower (1-2°C/hour)
  Thick glass → larger thermal gradient → faster = more stress
 Studio glass: small electric kilns with programmable controller
  Annealing cycle: hold 30 min at annealing point; cool 50°C/hr to 400°C;
  then off (cooling below quartz inversion is less critical for glass)

TEMPERED GLASS — INTENTIONAL STRESS:
 Opposite of annealing: deliberately quench rapidly
 Creates LARGE surface compression stress (~100-200 MPa)
 Results in stronger glass that fractures in a specific way (dice)
 See 06-SAFETY-GLASS for full treatment
```

---

## Thermal Expansion and CTE

```
CTE — COEFFICIENT OF THERMAL EXPANSION
========================================

Critical when:
 1. Fusing glass components together (must match or seal fails)
 2. Glass-to-metal seals (Kovar alloy matched to borosilicate)
 3. Thermal shock resistance (lower CTE → survives larger ΔT)
 4. Coating adhesion (optical coatings, Low-E coatings)

VALUES (×10⁻⁶/°C):
 Glass type         CTE
 ———————————————    ————
 Soda-lime          ~9
 Borosilicate       ~3.3
 Aluminosilicate    ~4-6
 Fused silica       ~0.55
 Zerodur             ~0.02 (glass-ceramic, near-zero)
 Kovar alloy         ~5.1 (Fe-Ni-Co; matches borosilicate for seals)

THERMAL SHOCK RESISTANCE:
 Resistance (R) ∝ (fracture strength × thermal conductivity) / (E × CTE)
 Practically: lower CTE = better thermal shock resistance
 Soda-lime glass: pour boiling water → cold glass → fractures
 Borosilicate (Pyrex): withstands sudden temperature changes
  (that's the entire point of Pyrex cookware)

CTE MISMATCH IN PRACTICE:
 Fusing different glass types: the mismatch creates stress at interface
  "Compatibility" test: fuse two glass rods → anneal → look for cracking
  Hotline glass suppliers publish CTE ranges; must match within ±0.5×10⁻⁶
 Solar cell encapsulation: EVA interlayer accommodates CTE mismatch
  between glass (~9) and silicon (~2.6); designed to flex rather than bond rigidly
```

---

## Optical Properties

```
OPTICAL PROPERTIES OF GLASS
=============================

REFRACTIVE INDEX (RI):
 Soda-lime: ~1.52; borosilicate: ~1.47; dense flint: up to ~1.9
 Lead oxide (PbO): increases RI → sparkle in cut crystal
 Heavy metal oxides (La₂O₃, Nb₂O₅, Ta₂O₅): very high RI for optics
 RI controlled by composition → entire catalog of optical glasses
  each with specific RI at specific wavelength

ABBE NUMBER (V-NUMBER = DISPERSION):
 V = (n_d - 1) / (n_F - n_C)  [Fraunhofer D, F, C lines]
 High V = low dispersion (crown glass) = colors focused similarly
 Low V = high dispersion (flint glass) = colors spread apart
 Achromatic lens: pair crown (high V) + flint (low V) → corrections cancel
 Fluorite/CaF₂: V = 95 — very low dispersion → used in apochromatic lenses

TRANSMISSION WINDOW:
 Soda-lime: absorbs below ~350nm (UV) and above ~3μm (mid-IR)
 Fused silica: transmits down to ~180nm (deep UV) → semiconductor litho
 Chalcogenide glass: transmits in mid- and far-IR (8-14μm) → thermal imaging
 Fluoride glass (ZBLAN): transmits broadly IR → theoretical <0.01 dB/km fiber

WHY GLASS IS TRANSPARENT:
 Electronic transitions in Si-O bonds lie in UV (high energy)
 Phonon vibrations (absorption) in IR (low energy)
 Visible light (400-700nm) falls between these → passes through
 Colorants absorb specific visible wavelengths by d-electron transitions
  in transition metal ions (Fe²⁺ → blue-green; Co²⁺ → deep blue; etc.)
```

---

## Devitrification

```
DEVITRIFICATION — THE ENEMY OF GLASSMAKERS
============================================

WHAT IT IS:
 Conversion of glassy (amorphous) material to crystalline material
 by nucleation and crystal growth
 Glass = metastable below Tm (thermodynamically wants to be crystalline)
 Prevented by kinetics: cooling too fast for crystal nucleation/growth

WHEN IT HAPPENS:
 During cooling: if cooling rate too slow through nucleation temperature range
 During reheating: if glass is held at nucleation/growth temperature
  (especially in range 600-900°C for many silicate glasses)
 On surfaces: contamination, scratches → nucleation sites

CONSEQUENCES:
 Opaque white or milky crystalline patches
 Completely ruins optical glass, container glass, flat glass
 Mechanical weakening (crystal-glass interface stresses)
 In furnace glass: can generate crystalline "stones" in melt
  which flow into product

PREVENTION:
 Control time-temperature profile (avoid nucleation range)
 Add nucleation inhibitors:
  Al₂O₃: raises viscosity at nucleation temperatures (slows growth)
  La₂O₃, ZrO₂: suppress nucleation rate
 Keep furnace well-homogenized (prevent compositional gradients)

CONTROLLED DEVITRIFICATION = GLASS-CERAMICS:
 Deliberate: add nucleating agents (TiO₂, ZrO₂, P₂O₅)
 Heat treat at precise temperatures to nucleate then grow crystals
 Result: polycrystalline material with glassy matrix
 Properties: can be radically different from parent glass
 Examples: Pyroceram (Corning, 1957), Zerodur (near-zero CTE),
           Corelle dinnerware, stovetop ceramics (Schott Ceran)
 See 05-SPECIALTY-GLASS for full treatment
```

---

## Chemical Durability

```
GLASS CORROSION — ION EXCHANGE AND LEACHING
============================================

ATTACK BY WATER:
 Glass in contact with water undergoes ion exchange:
  Na⁺ (or K⁺) in glass ↔ H⁺ (or H₃O⁺) in water
  Slow at room temp; faster at high temp; faster at high pH (alkali attack)
 Result: sodium-depleted layer at surface; silica-rich surface gel
  → surface becomes slightly rough, potentially cloudy
 "Water weathering" of antique glass: iridescent film from ion exchange
  (thin-film interference on leached surface layer)

DURABILITY HIERARCHY:
 Best: fused silica (no modifiers to leach)
 Very good: borosilicate Type I pharmaceutical glass
 Good: typical soda-lime window glass (outdoor durability decades)
 Poor: high-alkali glass, potash glass, lead glass
  Lead crystal decanter stored with wine/port: Pb leaches into liquid
  EU and US restricted storage in lead crystal for acidic beverages

PHARMACEUTICAL GLASS TYPES:
 Type I (borosilicate): highest chemical resistance; injectable drugs
 Type II (treated soda-lime): surface sulfur treatment improves durability;
  less demanding drug formulations
 Type III (soda-lime): oral preparations, not injectables

MUSEUM GLASS DISEASE:
 "Crizzling" or "crisselling": network of fine cracks in antique glass
  from ion exchange expansion/contraction cycling
 "Weeping glass": droplets form on surface from moisture condensation
  on ion-exchange modified surface
 ~40% of glass in major museum collections showing some deterioration
 Conservation: controlled humidity; minimize handling; climate control
```

---

## Common Confusion Points

**Random network ≠ liquid structure**:
Glass has short-range order (SiO₄ tetrahedra are very regular) but no long-range periodicity. It's not completely random — the tetrahedra are well-defined; only how they connect lacks order. Calling it a liquid (even "frozen liquid") is misleading.

**Tg vs Tm**:
Crystalline materials have a sharp melting point (Tm) with a latent heat. Glass has Tg — a range over which viscosity changes, not a sharp transition. Soda-lime glass at 700°C is not "melted" — it's a very viscous fluid that can be pressed or drawn.

**Annealing glass vs annealing metals**:
Annealing in both cases involves controlled slow cooling, but the mechanism differs. Metal annealing relieves dislocations (defects in crystal lattice). Glass annealing relieves frozen-in viscoelastic stress. The principle (slow controlled cooling = lower stress) is similar but the physics differs.

**Borosilicate ≠ indestructible**:
Borosilicate has excellent thermal shock resistance because of low CTE. But it can still break from mechanical impact, chemical attack, or thermal shock beyond its limits. Pyrex baking dishes fail if placed directly from freezer to oven — thermal gradient even low-CTE glass can't tolerate.

---

## Decision Cheat Sheet

| Property Question | Answer |
|-------------------|--------|
| Why soda-lime glass is workable at 1,100°C | Na₂O breaks network → lowers viscosity |
| Why borosilicate survives oven heat | Low CTE → small thermal stress |
| Why lead crystal sparkles | High PbO → high RI and dispersion |
| Why glass in UV darkens (solarization) | Fe²⁺ and other redox from UV |
| Why decanters shouldn't store port | Pb leaches into acidic alcohol |
| Why fused silica for chip fabrication | Withstands >1,000°C; ultra-pure; UV-transparent |
| Why glass is transparent | Gap between UV electronic and IR phonon absorption |
| CTE mismatch: glass fusing | Must be within ~0.5×10⁻⁶/°C or seal fails |
| Why annealing prevents spontaneous fracture | Relieves residual thermal stress below strain point |
