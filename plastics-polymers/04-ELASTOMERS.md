# Elastomers: Natural and Synthetic Rubber

## The Big Picture

```
+------------------------------------------------------------------+
|                 THE ELASTOMER LANDSCAPE                          |
|                                                                  |
|   NATURAL            SYNTHETIC GENERAL       SPECIALTY           |
|   ─────────          ──────────────────       ─────────          |
|   NR (cis-PI)        SBR (tire tread)         NBR (oil resist)   |
|   Hevea brasiliensis BR  (tire sidewall)       CR  (neoprene)    |
|   ~14M t/yr          EPDM (weather seal)       IIR (butyl)       |
|                       IR  (synthetic isoprene) VMQ (silicone)    |
|                       SBR ~60% of synth         FVMQ, FKM        |
|                                                                  |
|   THERMOPLASTIC ELASTOMERS (TPE) — processable like plastics     |
|   SBS/SEBS  TPU  TPV  COPE  PEBA                                 |
+------------------------------------------------------------------+
```

Elastomers are distinguished by enormous reversible deformation (100–800%)
and low elastic modulus (0.01–0.1 GPa vs. 1–100 GPa for stiff polymers).
The physics: long chains between cross-link points store entropy — stretching
reduces chain conformational entropy, which drives elastic recovery.

---

## The Physics of Rubber Elasticity

```
   UNSTRETCHED                 STRETCHED
   ───────────                 ─────────
   ~~~~~ (coiled chain)        ─────── (extended chain)
   Many conformations          Few conformations
   High entropy                Low entropy (ordered)

   F = -T(∂S/∂L)   restoring force is entropic, not energetic
   (unlike metal spring: F = -k·x, energy-based)
```

Rubber's modulus increases with temperature (unlike metals): E ~ T/Mc
- Higher T → more thermal energy → higher entropy elasticity
- Metal spring: E decreases with T (weaker bonds)

**Affine network model** (Gaussian chains):
  σ = ν_e · k · T · (λ - λ^-2)
  where ν_e = crosslink density, λ = extension ratio.

This is why rubber compounders talk about "crosslink density" constantly — it's
the primary control knob for modulus and elastic recovery.

---

## Vulcanization: From Sap to Structural Material

Raw natural rubber (masticated, unvulcanized): Tg = –73°C, creeps and flows
at room temperature. Useful for nothing structural.

**Vulcanization** (Goodyear, 1839): sulfur cross-linking at 140–160°C.

```
   RAW NR CHAINS:   ~~~|~~~ (entangled only, no chemical bonds)

   + S8 (elemental sulfur) + accelerator + zinc oxide + stearic acid
   + heat 140–160°C for 15–60 min

   VULCANIZED:   ~~~|~~~S-S-S~~~|~~~   (polysulfidic bridges)
                    or
                 ~~~|~~~S~~~|~~~       (monosulfide, with accelerator)
```

Sulfur bridges per crosslink:
- **Polysulfidic** (–Sx–, x=3–8): more flexible, dynamic fatigue resistance
- **Disulfide** (–S2–): intermediate
- **Monosulfide** (–S–): less fatigue, better heat and reversion resistance
- **Carbon-carbon** (peroxide cure): no sulfur, best heat/chemical resistance

Accelerator systems (CBS, TBBS, MBT, TMTD) control cure rate, crosslink type,
and scorch safety.

---

## Natural Rubber (NR)

**Source**: Latex from *Hevea brasiliensis* (98% of commercial supply).
Coagulate latex → dried sheets → masticated → compound.

**Chemistry**: cis-1,4-polyisoprene. The *cis* configuration is critical —
trans-1,4-polyisoprene is gutta-percha (hard, leathery, melts at 65°C, used
in golf ball covers and 19th-century telegraph cable insulation).

```
   cis-1,4-polyisoprene:
       CH3
        |
   ~~ C=C ~~          Low Tg (–73°C), high flexibility, coils tightly
      H  H

   trans-1,4-polyisoprene:
       CH3   H
        |    |
   ~~ C=C  ~~         Crystallizes at room T, stiff (gutta-percha)
      H
```

**Strain-induced crystallization**: NR crystallizes when stretched (χ_c up to
50%). This provides exceptional tear strength and cut/crack growth resistance
that no synthetic rubber fully replicates. Critical for truck tires, conveyor
belts, medical gloves.

| Property (vulcanized NR) | Typical range |
|--------------------------|--------------|
| Elongation at break | 500–800% |
| Tensile strength | 20–35 MPa (unfilled) |
| Hardness | 30–80 Shore A |
| Max service T | ~100°C (aging), 120°C short-term |
| Min service T | –50°C (Tg = –73°C) |
| Chemical resistance | Poor (oils, hydrocarbons) |
| Ozone resistance | Poor |
| Key advantage | Strain-induced crystallization, heat buildup |

---

## Styrene-Butadiene Rubber (SBR)

World's largest-volume synthetic rubber (~60% of all synthetic rubber).
Developed during WWII to replace NR from Southeast Asia.

**Chemistry**: Random copolymer of styrene (23–25%) and 1,3-butadiene.
Tg ~ –60°C (vs. NR –73°C) — slightly stiffer at low temperature.

No strain-induced crystallization → lower raw tensile strength than NR.
Must be carbon black reinforced to achieve useful mechanical properties.

```
   SBR + 50 phr N330 carbon black:
   Tensile strength: 20–25 MPa (vs. 5–8 MPa unfilled)
   Hardness: 55–65 Shore A
   Modulus at 300%: 8–12 MPa
```

**Key advantages over NR**:
- Better ozone/aging resistance (no double bonds in main chain ratio)
- Better abrasion resistance (tire tread wear)
- Lower heat buildup at moderate rolling frequency
- No supply dependency on Hevea (geopolitical)

**Tire tread application**: SBR gives wet grip; BR (butadiene rubber, Tg = –90°C)
gives rolling resistance and abrasion. Commercial treads blend SBR + BR in
ratios optimized for the wet/dry/wear triangle.

---

## EPDM (Ethylene-Propylene-Diene Monomer)

Terpolymer: ethylene + propylene (backbone, fully saturated) + small amount
of diene (ENB, DCPD, or 1,4-hexadiene — pendant diene for vulcanization site).

```
   ~CH2-CH2-CH2-CH(CH3)-CH2-CH2~   [mostly saturated backbone]
                |
   [occasional ENB pendant group] — crosslink site
```

**Saturated backbone = extraordinary ozone and UV resistance.** No double
bonds in the main chain to attack. Ozone testing: 50 pphm, 20% elongation,
40°C, 96h → no cracks (vs. NR fails in 30 min).

Applications: automotive weather seals, window gaskets, roofing membranes,
pond liners, electrical cable jacketing, steam hose.

| Property | Value |
|----------|-------|
| Tg | –50 to –60°C |
| Service temp | –50°C to +150°C |
| Elongation | 250–600% |
| Tensile | 10–25 MPa (CB reinforced) |
| Ozone/UV | Excellent |
| Oil resistance | Very poor |

---

## Nitrile Rubber (NBR)

Copolymer: butadiene + acrylonitrile (AN content 18–50%).

The nitrile groups (–CN) provide polar attraction → excellent oil, fuel, and
solvent resistance. Higher AN → more polar → better oil resistance but lower
low-temperature flexibility (Tg rises).

```
   AN content vs. properties:

   AN%     Tg (°C)    Oil resistance    Low-T flex
   18%     –50        Moderate          Excellent
   28%     –35        Good              Good
   40%     –15        Excellent         Poor
   50%     +10        Best              Very poor
```

Applications: O-rings, fuel hose, hydraulic seals, oil-resistant gloves,
printer rolls, aircraft fuel systems.

**HNBR**: Hydrogenated NBR — selective hydrogenation of remaining C=C bonds.
Much better heat and ozone resistance than NBR, up to 150–165°C. Used in
automotive timing belts and demanding seals.

---

## Silicone Rubber (VMQ / PDMS)

Backbone: not carbon-based. Alternating Si-O-Si backbone (siloxane).

```
        CH3         CH3
         |           |
   ~~ Si-O-Si-O-Si-O ~~
         |           |
        CH3         CH3

   Si-O bond: longer and more flexible than C-C
   Si-O bond energy: 452 kJ/mol (strong)
   Very low barrier to rotation
```

This gives the most extreme temperature range of any elastomer:
- Tg: –123°C (PDMS homopolymer, even lower with modification)
- Service: –60°C to +200°C continuous, up to 250°C short-term

**Properties**:

| Property | VMQ | Notes |
|----------|-----|-------|
| Tg | –80 to –123°C | Phenyl or fluoroalkyl groups adjust |
| Service T | –60 to +200°C | Peroxide cure preferred |
| Elongation | 100–600% | Good |
| Tensile (reinforced) | 5–15 MPa | Fumed silica filler essential |
| Chemical resistance | Poor to solvents | Good to water/dilute acids |
| Flame resistance | Self-extinguishing | Low smoke |
| Biocompatibility | Excellent | Medical implants, food contact |
| Cost | High ($5–20/kg base polymer) | |

**Filler requirement**: Silicone unfilled has very poor mechanical strength.
Fumed silica (15–40 phr) is mandatory — provides reinforcement via silanol–PDMS
interaction.

---

## Thermoplastic Elastomers (TPEs)

TPEs process like thermoplastics (melt, injection mold) but behave like
crosslinked rubbers at service temperature. Physical crosslinks (not covalent)
that break down on heating.

```
+--------------------+----------------------------------------------+
|  TPE Family        |  Architecture                                |
+--------------------+----------------------------------------------+
|  SBS / SEBS        |  Hard PS blocks + soft PB or PEB mid-block   |
|  (styrenic TPE)    |  PS microdomains = physical crosslinks       |
+--------------------+----------------------------------------------+
|  TPU               |  Hard MDI+chain ext segments + soft polyol   |
|                    |  H-bonding between hard segments             |
+--------------------+----------------------------------------------+
|  TPV (Santoprene)  |  Vulcanized EPDM particles in PP matrix     |
|                    |  Dynamic vulcanization during melt mixing    |
+--------------------+----------------------------------------------+
|  COPE (TEEE)       |  Hard PBT crystalline blocks + soft polyol   |
|  (Hytrel)          |  High-temp, fatigue resistance               |
+--------------------+----------------------------------------------+
|  PEBA              |  Hard Nylon blocks + soft polyether          |
|  (Pebax)           |  Running shoes, ski boot liners              |
+--------------------+----------------------------------------------+
```

TPE vs. thermoset rubber tradeoffs:

| Attribute | TPE | Thermoset rubber |
|-----------|-----|-----------------|
| Processing | Injection mold, extrude | Compression/transfer mold, long cure |
| Recyclable | Yes (in theory) | No |
| Compression set | Higher | Lower |
| Service T (max) | 100–180°C | Up to 250°C (silicone) |
| Cost | Medium-high | Low-medium |

---

## Synthetic Rubber at a Glance

| Type | Tg (°C) | Max T | Key strength | Key weakness |
|------|---------|-------|--------------|--------------|
| NR | –73 | 100°C | Strain xtal, tear strength | Oil, ozone, heat |
| SBR | –60 | 100°C | Tire tread wear, cost | No strain xtal |
| BR | –90 | 100°C | Rolling resist, cold flex | Poor tear |
| EPDM | –55 | 150°C | Ozone, UV, weathering | Oil resistance |
| NBR | –15 to –50 | 120°C | Oil, fuel, solvent | Ozone, cold flex |
| CR | –40 | 120°C | Moderate oil + ozone | Cost |
| IIR (butyl) | –70 | 120°C | Gas impermeability | Cure rate |
| VMQ | –80 | 200°C | Extreme T range, bio | Strength, cost |
| FKM (Viton) | –15 to –20 | 200°C | Fuel, chemical, heat | Cold flex, cost |

---

## Decision Cheat Sheet

| Application | Primary choice | Why |
|-------------|---------------|-----|
| Tire tread | SBR + BR blend | Wear + wet grip + rolling resistance |
| Tire inner liner | IIR (butyl) | Gas impermeability |
| Automotive weather seal | EPDM | Ozone, UV, temperature |
| Engine bay O-ring (oil) | FKM (Viton) | Heat + fuel resistance |
| Medical implant / tubing | VMQ (silicone) | Biocompatibility, sterilizable |
| Fuel line / hydraulic hose | HNBR or FKM | Oil + heat |
| Pond liner / roofing | EPDM | UV, ozone, weather |
| Athletic shoe foam midsole | eTPU or PEBA | Lightweight, energy return |
| Grip / overmold on PP | SEBS TPE | Co-injection with PP possible |
| High-performance tire (race) | NR | Strain crystallization, grip |

---

## Common Confusion Points

**NR is not inferior to synthetic rubber**: NR outperforms synthetic rubbers
in tear resistance and fatigue due to strain-induced crystallization. Large truck
tires, aircraft tires, and high-load conveyor belts use NR-dominant compounds
for exactly this reason.

**"Rubber" refers to both vulcanized thermoset and TPEs**: TPEs like Santoprene
(TPV) and Hytrel (COPE) are marketed as "rubber" but process like plastics.
Context — does it need to be recycled? Can it be compression-set tolerant?

**Silicone's low strength misleads**: Silicone unfilled has tensile strength ~0.5
MPa — barely a gel. The fumed silica reinforced product is 5–15 MPa. When
someone says "silicone is weak," they mean unfilled. Properly compounded,
it's adequate for all gasket, tubing, and seal applications.

**Ozone cracking is SBR/NR/CR's nemesis**: Even 0.01 pphm ozone attacks C=C
double bonds in the main chain. EPDM is immune. All other diene rubbers require
antiozonants (waxes + chemical antiozonants like 6PPD) in tire sidewalls.
