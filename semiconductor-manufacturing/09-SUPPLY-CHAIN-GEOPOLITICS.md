# Supply Chain and Geopolitics — A Layered Guide

## The Big Picture

Semiconductor manufacturing is the most geographically concentrated critical
technology in the world. A single company (TSMC) in a single contested territory
(Taiwan) produces ~90% of the world's leading-edge logic chips. A handful of
equipment suppliers and materials companies represent irreplaceable chokepoints.

```
SEMICONDUCTOR SUPPLY CHAIN DEPENDENCIES
════════════════════════════════════════════════════════════════════

DESIGN EDA TOOLS:             EQUIPMENT (Fab Tools):
Synopsys, Cadence,            ASML (EUV litho: 100% monopoly)
Mentor (Siemens)              Applied Materials (AMAT): CVD, PVD, CMP, implant
  ~80% US market share          largest equipment co by revenue
                              Lam Research: etch, deposition
                              KLA: inspection, metrology
IP CORES:                     Tokyo Electron (TEL): CVD, clean, litho track
Arm (SoftBank/UK):            Kokusai/SCREEN: diffusion, clean
  95%+ mobile CPUs            ASML, Nikon, Canon: DUV litho (ASML dominant)
  ~50% datacenter
                            MATERIALS:
FOUNDRIES:                    Shin-Etsu, Sumco (Japan): ~60% Si wafers
TSMC (Taiwan): leading edge   JSR, TOK, Fujifilm (Japan): photoresists
Samsung (Korea): logic+DRAM   Air Products, Linde: ultra-pure gases
Intel Foundry: rebuilding      BASF, Entegris: specialty chemicals
SMIC (China): ≤7 nm blocked   Mitsui/Sumco: SOI wafers

ASSEMBLY/TEST (ATP):          END CUSTOMERS:
ASE, Amkor (Taiwan/Korea):    Apple, NVIDIA, AMD, Qualcomm
  package + test most chips   Broadcom, MediaTek, Marvel
```

---

## Equipment Chokepoints

```
CRITICAL EQUIPMENT SUPPLIERS

ASML (Netherlands) — EUV LITHOGRAPHY:
  Revenue: ~€27B (2023)
  Market share: 100% of EUV scanner market
  Why irreplaceable:
    EUV involves: Zeiss optics (Germany), Trumpf laser (Germany),
    Cymer source (ASML subsidiary), USHIO light source —
    decades of integration by thousands of engineers
    No competitor has attempted the full system (Nikon/Canon license ASML technology)
  DUV (193i) market: ASML ~83%, Nikon ~15%, Canon ~2%

  NXE:3400D EUV price: ~$150M
  High-NA NXE:5000: ~$380M (2024)
  Lead time: 12-18 months per tool
  ASML builds ~50-60 EUV tools/year; increasing to ~90+ with High-NA

APPLIED MATERIALS (AMAT, USA):
  Largest semiconductor equipment company by revenue ($26B, 2023)
  Products: CVD, PVD, ion implant, CMP, epitaxy, ALD
  No single AMAT monopoly (competition from Lam, TEL, Kokusai) but deep embedding
  Largest single player across unit processes

LAM RESEARCH (USA):
  Dominant in: plasma etch (~50% market share), ALD deposition (~30%)
  Critical for: FinFET/GAA etch, memory high-aspect-ratio etch
  Revenue: ~$17B (2023)

KLA CORPORATION (USA):
  Dominant in: wafer inspection (~55% share), CD-SEM, overlay measurement
  Without KLA tools: can't detect defects → can't improve yield
  Revenue: ~$10B (2023)

TOKYO ELECTRON (TEL, Japan):
  CVD and ALD equipment: strong position in gate oxide, spacer films
  Thermal systems (oxidation, diffusion furnaces): dominant
  Clean track (photoresist coat/develop): ~45% market share with SCREEN
  Revenue: ~¥2T (2023)

CONCENTRATION:
  ASML + AMAT + Lam + KLA + TEL + SCREEN = ~80% of fab tool market
  All from: Netherlands, USA, Japan
  China has domestic alternatives (AMEC for etch, NAURA for some CVD) but
  significantly behind at leading edge
```

---

## Materials Chokepoints

```
CRITICAL MATERIALS

SILICON WAFERS:
  Shin-Etsu (Japan) + Sumco (Japan): ~65% of 300 mm wafer market
  Siltronic (Germany), SK Siltron (Korea): most of rest
  China wafer production: growing but quality and purity lag for leading edge

PHOTORESISTS AND ANCILLARY CHEMICALS:
  ArF/EUV resists: JSR (Japan), TOK (Japan), Fujifilm (Japan), Inpria (USA)
    Japan: ~90% of leading-edge photoresist market
  PAG (photo-acid generators): specialized Japanese chemistry supply
  BARC (bottom anti-reflective coating): JSR, Brewer Science
  EUV metal-oxide resists: Inpria (acquired by JSR)

ULTRA-PURE GASES:
  Process gases: Air Products, Linde (Germany/USA), Air Liquide (France)
  Specialty gases: Neon (Ne) for excimer laser → 70% from Ukraine (before 2022 war)
    Ukraine conflict 2022: spike in Ne/Kr prices → prompted US/European supply expansion
  Fluorine compounds (NF₃, F₂ for chamber clean): Mitsui, Air Products
  Germanium (GeH₄ for SiGe epitaxy): 70%+ of mining in China and Russia

CMP SLURRIES:
  Cabot, CMC Materials (USA), Fujimi (Japan): leading suppliers
  High-purity SiO₂ abrasives, specialty chemistries per layer

SPUTTERING TARGETS:
  High-purity metals (Ta, TaN, Ti, W, Co, Ru): Materion, Plansee, Tosoh
  Ruthenium (Ru): emerging for next-gen barriers; South Africa, Russia primary mining
  Cobalt (Co): primarily Democratic Republic of Congo (DRC) mining

EXTREME PURITY REQUIREMENTS:
  CMP slurry: metals < 1 ppb
  Process gases: 99.9999% (6N) purity minimum
  Si wafer: metal contamination < 10¹⁰ atoms/cm²
  A single ppm of wrong metal in process can kill an entire wafer run
```

---

## Taiwan Concentration Risk

```
TAIWAN RISK

THE NUMBERS:
  TSMC: ~90% of leading-edge logic (≤7 nm) by revenue
  Taiwan: ~64% of all foundry revenue (TSMC + others)
  TSMC Hsinchu/Tainan: physically in disputed territory ~160 km from China
  Apple, NVIDIA, AMD, Qualcomm, Google: 100% dependent on TSMC for leading-edge

GEOPOLITICAL SCENARIO:
  If Taiwan is blockaded or invaded:
  - Every leading-edge chip in production (AI accelerators, iPhones, AMD CPUs) stops
  - Global GDP impact estimated: $600B-$1T+ (Boston Consulting Group, 2021)
  - 2-3 year minimum to rebuild equivalent capacity elsewhere (optimistic)
  - Reality: 5-10 years due to tool lead times (ASML backlog), process knowledge transfer

"SILICON SHIELD" THEORY:
  Taiwan's chip production makes it too costly for China to destroy
  Counter: military planners may assume precision strikes can be avoided
  Counter-counter: TSMC CEO Morris Chang warned of self-destruction contingency

DIVERSIFICATION EFFORTS:
  TSMC Arizona: Fab 21 (N4P, operational 2024; N3 planned 2026)
    Cost overruns: $30B+; labor/supply chain challenges
  TSMC Japan (Kumamoto): N12/N16 with Sony, operational 2024
  TSMC Germany (Dresden): N28/N22 with Bosch, NXP, Infineon (automotive focus, 2027)
  Samsung Texas: N4 expansion
  Intel Ohio: Intel 18A/20A fabs (construction 2024-2026)

REALISTIC DIVERSIFICATION TIMELINE:
  Even with $52B CHIPS Act + equivalent EU/Japanese funding:
  2030: TSMC Taiwan still ~60-70% of leading-edge capacity
  Diversification helps at trailing edge (28 nm for automotive, IoT): significant progress
  Leading edge: Taiwan concentration reduced but not eliminated by 2030
```

---

## CHIPS Act and Government Response

```
SEMICONDUCTOR POLICY ACTIONS (2022-2025)

US CHIPS AND SCIENCE ACT (August 2022):
  $52.7B total:
    $39B manufacturing incentives (fab construction grants)
    $11B research (NSTC, CHIPS R&D, fab workforce)
    $2B legacy chips (automotive/defense)
  Guard rails: 10-year ban on expanding China advanced capacity for subsidy recipients
  Recipients:
    TSMC Arizona: ~$6.6B + $5B loans
    Intel: ~$8.5B grant + $11B loans (largest)
    Samsung Texas: ~$6.4B
    Micron (memory): ~$6.1B
    Wolfspeed (SiC): ~$750M
    GlobalFoundries: ~$1.5B
  EDA/IP export: additional controls on Synopsys/Cadence selling to China

EU CHIPS ACT (2022):
  €43B target by 2030 → 20% of global chip production (from current ~10%)
  Major facilities: TSMC Dresden, Intel Magdeburg (~€30B, partially paused 2024),
    ST/GlobalFoundries Crolles (France)

JAPAN:
  ¥3.9T (~$26B) in semiconductor subsidies
  TSMC Kumamoto (¥476B govt support), TSMC Kumamoto 2 (announced)
  Rapidus: Japanese government-backed startup → TSMC N2-equivalent technology by 2027
    (highly ambitious, on tight timeline)

INDIA:
  India Semiconductor Mission: $10B subsidy scheme
  Tata Electronics + PSMC (Taiwan): fab in Gujarat (28 nm, announced)
  Micron: OSAT (assembly/test) facility in Gujarat ($2.75B, $1.5B US+India support)

CHINA'S RESPONSE:
  CSET estimates China invested $50B+ in semiconductors 2014-2023
  SMIC: achieved 7 nm equivalent with DUV multi-patterning (2022, Huawei Kirin 9000S)
    But EUV denied → multi-patterning limits scaling below 5 nm reliably
  Domestic EUV: SMEE (Shanghai Micro Electronics Equipment) — decades behind
  Wafer: NCETC, Okmetic China expansions
  Goal: self-sufficiency at mature nodes by 2027; leading edge: much longer
```

---

## Export Controls

```
US EXPORT CONTROLS ON SEMICONDUCTORS

OCTOBER 2022 CONTROLS (BIS, Commerce Department):
  Banned: export to China of
  1. Advanced chips: GPU ≥ 4800 TOPS aggregate performance (A100 level)
     → NVIDIA created A800/H800 (lower bandwidth) for China → later restricted further
  2. Fab equipment for ≤14 nm (later tightened)
  3. EDA tools for ≤3 nm (GAAFET + FinFET design)
  4. US persons: banned from supporting Chinese advanced fabs (workforce control)

OCTOBER 2023 UPDATES:
  Closed loopholes: lowered chip performance thresholds
  NVIDIA H100 variant banned; H20 (restricted version) allowed until...
  Extended: multilateral export controls — Netherlands/Japan agreed to restrict
    ASML: EUV banned to China (already since 2019); DUV also now restricted (some)
    Tokyo Electron: some tools restricted

2024 FURTHER TIGHTENING:
  NVIDIA H20 added to control list (2024)
  Entity list additions: CXMT (Chinese DRAM), YMTC (Chinese NAND)

IMPACT:
  NVIDIA China revenue: ~20% of total ($10B+/yr) before controls
  ASML China revenue: ~20% of total (~€5B) — now declining for advanced tools
  Huawei: forced to develop in-house chips (HiSilicon) with SMIC help → 7 nm chips
  Chinese foundries: SMIC, CXMT building capacity at older nodes to reduce dependence

DUTCH AND JAPANESE CONTROLS:
  Netherlands: ASML restricted from exporting DUV immersion tools (2023)
    ASML EUV already restricted since 2019 (Dutch government denied license)
  Japan: TEL, Nikon, Shin-Etsu, Sumco export licenses required for China
  This multilateral coordination is key — unilateral US controls insufficient alone
```

---

## Industry Concentration Map

```
GEOGRAPHIC CONCENTRATION BY FUNCTION (2024)

DESIGN (EDA + IP):
  USA: ~70% of global semiconductor IP value (Synopsys, Cadence, Arm UK)
  Chokepoint: Synopsys + Cadence = ~85% of advanced EDA market

CAPITAL EQUIPMENT:
  USA: AMAT, Lam, KLA (~45% of market value)
  Netherlands: ASML (~20%)
  Japan: TEL, Kokusai, Screen, Nikon (~25%)
  Non-US/NL/JP: <10%

MATERIALS:
  Japan: ~50% (wafers, resists, process chemicals, gases)
  Germany: ~10% (Siltronic, specialty gases, industrial)
  USA: ~15% (Entegris, Cabot, Air Products)
  Other: ~25%

ADVANCED LOGIC MANUFACTURING:
  Taiwan (TSMC): ~90% of ≤7 nm by revenue
  South Korea (Samsung Foundry): ~7%
  USA (Intel Foundry): ~1-2% (ramping)
  China: <1% at ≤7 nm (access restricted)

MEMORY MANUFACTURING:
  Samsung, SK Hynix (Korea): ~70% of DRAM
  Micron (USA): ~25% DRAM
  Samsung, SK Hynix, Kioxia/WD (Japan), Micron: NAND broadly distributed
  YMTC (China): growing NAND but on entity list

ATP (ASSEMBLY, TEST, PACKAGING):
  Taiwan (ASE, TSMC): ~40%
  South Korea: ~15%
  China: ~25% (increasingly restricted for advanced)
  Rest of Asia (Malaysia, Philippines, Vietnam): ~15%
```

---

## Decision Cheat Sheet

| Risk / Strategy | Key Fact |
|-----------------|----------|
| Geographic diversification of leading-edge fab | Possible but $50B+ and 5-10 years; Taiwan remains dominant through 2030 |
| Chokepoint that's hardest to replicate | ASML EUV (20+ years R&D, 800+ suppliers, 6 global locations) |
| US leverage over Chinese chip access | Export controls on EDA + equipment + advanced chips, multilateral with NL/Japan |
| Materials risk most overlooked | Japanese photoresists (~90% market), neon from Ukraine, germanium from China |
| CHIPS Act effectiveness | Good for trailing/mid-node (+28 nm), limited impact on leading-edge by 2030 |
| China's path to advanced chips | Long: EUV blocked → mature nodes only; SMIC 7 nm equivalent only w/ DUV tricks |

---

## Common Confusion Points

**ASML's EUV monopoly isn't just equipment — it's knowledge**: China could theoretically
buy all ASML's suppliers individually, but the integration, calibration expertise, and process
knowledge accumulated over decades at ASML can't be replicated by collecting components. This is
why export controls on ASML tools matter — it's not just hardware.

**"Built in America" chips ≠ independent supply chain**: A TSMC fab in Arizona still uses ASML
tools (Dutch), Tokyo Electron CVD (Japanese), Shin-Etsu wafers (Japanese), and JSR photoresists
(Japanese). Geographic fab diversification reduces the Taiwan risk but doesn't create full supply
chain independence.

**SMIC's "7 nm" is not competitive with TSMC's N7**: SMIC achieved 7 nm-class density using
DUV multi-patterning (SADP/SAQP without EUV). This requires 2-3× the mask layers, yields lower,
and is power-inefficient. The Huawei Mate 60 Pro's Kirin 9000S chip demonstrates it's feasible
but not economically competitive for high volume.

**Export controls affect future capability, not current inventory**: China had already stockpiled
significant quantities of ASML DUV tools (hundreds), AMAT/Lam equipment, and advanced chips
before 2022 controls. The controls limit future capability buildup but don't immediately reverse
existing infrastructure. The effect is felt over 5-10 year horizons.
