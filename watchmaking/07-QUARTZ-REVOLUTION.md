# Watchmaking — 07 The Quartz Revolution
## Piezoelectric Oscillation, 32,768 Hz, the Swiss Crisis, and the Swatch Response

---

## The Big Picture

The quartz revolution is the most disruptive technology transition in the history of timekeeping. In less than a decade (1969–1978), quartz wristwatches went from nonexistent to dominant. Swiss watch employment fell 69% over 18 years. The mechanism was simple: quartz oscillators are inherently more stable than mechanical balance wheels by a factor of ~1000, and integrated circuit manufacturing made them cheap.

```
MECHANICAL vs QUARTZ: THE ACCURACY GAP

Mechanical lever watch (COSC certified):  ±4 sec/day = ±24 min/year
Uncompensated quartz wristwatch:          ±15 sec/year (typical consumer grade)
TCXO quartz watch:                        ±1 sec/year
GPS-disciplined quartz:                   ±0.001 sec/year

Ratio mechanical to consumer quartz: 365×86400 / (±4×365) vs (±15)
  = ±1460 sec/year vs ±15 sec/year
  = ~100× accuracy improvement for $10 quartz vs $1000 COSC watch

The quartz oscillator's advantage is not incremental — it's structural.
A balance wheel's frequency stability (Q factor) ~10^3.
A quartz crystal's frequency stability (Q factor) ~10^5 to 10^7.
Two orders of magnitude better at the fundamental physics level.
```

---

## Piezoelectricity: The Physics

**Discovery:** Pierre and Jacques Curie, 1880. They observed that certain crystals (quartz, Rochelle salt, tourmaline) develop an electric charge when subjected to mechanical stress. They also observed the converse (inverse piezoelectric effect): applying an electric voltage across the crystal causes it to mechanically deform.

**Crystal structure behind the effect:**

```
PIEZOELECTRIC MECHANISM (quartz, SiO₂)

Quartz crystal structure: spiral arrangement of SiO₄ tetrahedra
  Silicon atoms: positive charge centers
  Oxygen atoms: negative charge centers

Unstressed state:
  Positive and negative charge centers coincide
  No net dipole → no electric field

Mechanically stressed:
  Crystal lattice deforms
  Positive and negative centers SHIFT relative to each other
  Net electric dipole moment appears → charge on crystal faces

Inverse piezoelectric:
  Apply voltage → forces on charges → lattice deforms
  Apply AC voltage at resonant frequency → sustained oscillation

For quartz: the piezoelectric axes are along the crystallographic a-axes.
The cut angle relative to these axes determines the resonant frequency
and its temperature coefficient.
```

**Key quartz cuts:**

```
QUARTZ CRYSTAL CUTS

AT-cut: standard for wristwatches and TCXO
  - Cut at ~35°15' to the optical (Z) axis
  - Frequency-temperature characteristic: cubic curve
    passes through zero temperature coefficient at ~25°C
    → frequency very stable near room temperature
  - Frequency: 32,768 Hz for wristwatch crystals (tuning fork shape)

SC-cut (Stress-Compensated): for high-stability OCXO
  - Double-rotated cut; stress-compensated
  - Better close-in phase noise; better aging
  - Used in precision oscillators, not wristwatches

IT-cut, BT-cut: older, less common

Temperature coefficient of AT-cut quartz (near 25°C):
  f(T) = f₀ × [1 + a(T-T₀) + b(T-T₀)² + c(T-T₀)³]
  where a≈0, b≈-0.034 ppm/°C², c≈0.11 ppb/°C³
  → variation ≈ ±30 ppm over 0°C to 50°C range
  → ±30 ppm × 86400 sec/day = ±2.6 sec/day if uncompensated
```

---

## Why 32,768 Hz?

The standard quartz wristwatch crystal oscillates at 32,768 Hz. This is not arbitrary:

```
32,768 = 2^15

A binary counter circuit that divides by 2 fifteen times:
  32,768 Hz → /2 → 16,384 Hz
  16,384 Hz → /2 → 8,192 Hz
  8,192 Hz  → /2 → 4,096 Hz
  4,096 Hz  → /2 → 2,048 Hz
  2,048 Hz  → /2 → 1,024 Hz
  1,024 Hz  → /2 → 512 Hz
  512 Hz    → /2 → 256 Hz
  256 Hz    → /2 → 128 Hz
  128 Hz    → /2 → 64 Hz
  64 Hz     → /2 → 32 Hz
  32 Hz     → /2 → 16 Hz
  16 Hz     → /2 → 8 Hz
  8 Hz      → /2 → 4 Hz
  4 Hz      → /2 → 2 Hz
  2 Hz      → /2 → 1 Hz  ← drives second hand stepper motor

15 binary divide-by-2 stages → exactly 1 Hz output
Binary division is trivially implemented in CMOS logic (T flip-flops)
No analog components required in the divider chain
Power consumption: nanowatts per flip-flop stage at 3V
```

<!-- @editor[bridge/P2]: The quartz oscillator circuit (inverter + crystal + feedback capacitors) is a Pierce oscillator topology. This reader likely knows oscillator circuits from EE fundamentals. The parallel: the crystal's mechanical Q (80,000–100,000) is doing the work that an LC tank circuit does in a Colpitts oscillator, but with 100× better selectivity. The stability advantage of quartz over LC: Q_crystal / Q_LC ≈ 10^5 / 10^2 = 1000× — which is exactly the mechanical watch vs quartz accuracy gap. The Q factor is the unifying concept across the entire watchmaking series: foliot Q ≈ 1, pendulum Q ≈ 10^4, quartz Q ≈ 10^5–10^7, atomic transition Q ≈ 10^10–10^17. Bridge this explicitly here. -->
**The crystal shape:** Wristwatch quartz crystals are tuning-fork shaped (not the rectangular blocks used in oscillator modules for electronics). Tuning-fork resonators vibrate in a flexural mode (the tines bend toward and away from each other). This mode:
- Operates at lower frequency (32kHz vs MHz for thickness-mode crystals) with smaller physical size
- Consumes less current (important for battery life)
- Is less sensitive to mechanical shock than thickness-shear mode
- Can be photolithographically manufactured on a wafer

```
TUNING FORK CRYSTAL DIMENSIONS (typical wristwatch)

     ┌──┐  ┌──┐
     │  │  │  │  ← tines (2 mm long, 0.1 mm wide, 0.1 mm thick)
     │  │  │  │
     └──┘  └──┘
        \  /
         \/
         /\
        /  \
       └────┘  ← base (1 mm wide)

Electrodes deposited on tine surfaces
AC voltage at 32,768 Hz drives flexural vibration
Piezoelectric charges on tine surfaces → feedback to sustain oscillation

Entire unit: 1.5–2.5 mm long, 0.5 mm wide, 0.1 mm thick
Mass: ~0.001 g
Frequency tolerance: ±20 ppm from target (at manufacture)
Aging rate: ±1–2 ppm/year (crystal ages as surface stress relaxes)
```

---

## Quartz Oscillator Circuit

```
QUARTZ OSCILLATOR — SCHEMATIC PRINCIPLE

        ┌─────────────────────────────────┐
        │         XTAL (32,768 Hz)        │
        │                                 │
        │    ┌──────────────────────┐     │
        │    │  inverter gate (CMOS)│     │
        │    │                      │     │
        │   ─┤ input         output├──── feedback
        │  ┌─┤               ┌─────┤     │
        │  │ └──────────────────────┘     │
        │  │                              │
        │  C₁ (load capacitor)  C₂       │
        │  │    (adjustable trim for     │
        │  GND   frequency calibration)  │
        └─────────────────────────────────┘

Operation:
1. Noise starts oscillation (or power-on transient)
2. Inverter amplifies signal at crystal's resonant frequency
3. Crystal's narrow-band resonance filters everything else out
4. Positive feedback sustains oscillation at 32,768 Hz
5. Crystal's mechanical Q (typically 80,000–100,000 for tuning fork)
   determines selectivity — only frequencies within a few Hz of
   32,768 Hz can sustain oscillation

Load capacitance (C₁, C₂) affects the effective crystal resonance
slightly. Trimmer capacitor allows factory calibration of ±1–2 sec/day
resolution on the final frequency.
```

---

## Temperature Compensation

The quartz crystal's frequency varies with temperature — about ±30 ppm over normal wearing temperatures. Several grades of compensation exist:

```
OSCILLATOR ACCURACY GRADES

Grade         | Technology           | Typical Stability  | Power     | Application
──────────────┼──────────────────────┼────────────────────┼───────────┼────────────────
None          | XO (bare crystal)    | ±30 ppm            | 0.5–2 µW  | Cheap watches
              | (Crystal Oscillator) | (±2.6 sec/day)     |           |
              |                      | ±15 sec/year over  |           |
              |                      | typical temp range |           |
              |                      |                    |           |
TCXO          | Temperature-         | ±1–2 ppm           | 2–5 mW    | Quality watches
(Temperature- | Compensated Crystal  | (±0.09 sec/day)    |           | GPS receivers
Compensated   | Oscillator           | ±1–3 sec/year      |           |
XO)           | Thermistor measures  |                    |           |
              | temp; correction     |                    |           |
              | applied to crystal   |                    |           |
              | voltage or output    |                    |           |
              | frequency            |                    |           |
              |                      |                    |           |
OCXO          | Oven-Controlled      | ±0.01–0.1 ppm      | 0.5–2 W   | Test equipment
(Oven-        | Crystal Oscillator   | (±0.001–0.01 s/day)|           | Telecom
Controlled    | Crystal heated to    | ±0.3–3 sec/year    |           | infrastructure
XO)           | constant temperature |                    |           | GPSDO reference
              | (typically 80–90°C)  |                    |           |
              | Tight thermal        |                    |           |
              | control ~±0.001°C    |                    |           |
```

**TCXO in consumer watches:** Citizen Eco-Drive Satellite Wave (GPS-synchronized every sync); Seiko Astron GPS Solar; Casio G-Shock GPW series. These are GPS-disciplined — they receive a time signal from GPS satellites and synchronize automatically, giving them atomic-clock-level accuracy without an atomic clock.

---

## The Quartz Crisis: Seiko Astron and its Aftermath

### CEH and the Swiss Near-Miss

The Swiss watch industry developed quartz technology first. The Centre Electronique Horloger (CEH), founded in 1962 by Ebauches SA (the Swiss ébauche consortium) in Neuchâtel, developed the Beta 21 quartz movement in 1967. It was publicly demonstrated at the Neuchâtel Observatory in 1967, winning the observatory competition with accuracy far exceeding any mechanical entry.

**What the Swiss did with it:** Licensed Beta 21 to 16 Swiss manufacturers who released quartz watches in 1970. Prices were high ($1,000–$2,000), positioning was as precision instruments, production was limited.

**What Seiko did:** Developed quartz technology in parallel at the Suwa Seikosha research lab. The **Seiko Quartz Astron** was launched December 25, 1969 — the day before the Swiss Beta 21 consortium's scheduled announcement (the date was specifically chosen to claim priority).

```
SEIKO QUARTZ ASTRON (1969) vs SWISS BETA 21 (1970)

                        Seiko Astron        Beta 21 (Swiss)
Launch date:            Dec 25, 1969        January 1970
Production quantity:    100 units           16 brands, limited
Price:                  ¥450,000 (~$1,250)  $1,000–$2,000
Crystal frequency:      8,192 Hz            8,192 Hz
Power source:           Battery             Battery
Accuracy (claimed):     ±5 sec/year         ±1 min/month (±12 sec/year)
Case:                   Gold, 42 mm         Various

Both used similar technology at similar cost.
The strategic difference emerged in the next 5 years.
```

### The Price Collapse

The critical difference was not 1969–1970 but 1972–1975. Japanese electronics firms (Seiko, Citizen, Casio) applied their consumer electronics manufacturing expertise:

```
QUARTZ WATCH PRICE TRAJECTORY

1969: Seiko Astron        $1,250
1972: Swiss quartz        $700–$1,500
      Japanese quartz     $300–$500
1974: Japanese quartz     $100–$300
1976: Texas Instruments    $9.95 (!!) — disposable digital quartz
      (LED display, battery lasts 1 year)
1978: LCD quartz watches   $5–$20 widely available
      Casio F-7 (1974):    ¥3,900 (~$13)
```

Texas Instruments did to the watch what it had done to the calculator: used silicon manufacturing scale to drive prices below the cost of mechanical labor. By 1978, a $10 digital quartz watch was more accurate than a $1,000 mechanical Swiss watch.

### Swiss Industry Collapse

```
SWISS WATCH INDUSTRY — EMPLOYMENT

1970: ~90,000 employed in watch industry
1975: ~65,000 (Hissing of market)
1980: ~47,000 (Full crisis)
1984: ~28,000 (-69% from peak)

COMPANY CASUALTIES:
  Lanco: liquidated
  Movado: survived but diminished
  Longines: sold (to SSIH group, later SMH/Swatch Group)
  Omega: sold (to ASUAG, later SMH/Swatch Group)
  Certina, Tissot: absorbed into groups
  Hamilton: sold (to ASUAG)
  Multiple Vallée de Joux makers: consolidated or closed

Surviving companies:
  Rolex: privately held; successfully repositioned as luxury;
         entered quartz only briefly (1977 Oysterquartz); withdrew
  Patek Philippe: private; focused ultra-high-end; survived
  Audemars Piguet: private; survived (Royal Oak 1972 launch
                   had diversified into luxury sport watches)
```

### The Nicolas Hayek Intervention

In 1982, Swiss banks (holding the assets of bankrupt ASUAG and SSIH groups) hired consultant Nicolas Hayek to advise on liquidation. His recommendation: don't liquidate, restructure and fight back with a new strategy.

**Hayek's insight:** The Japanese had commoditized the low end. The Swiss could not compete on manufacturing cost. The solution: don't compete on cost — compete on brand and fashion positioning. The watch doesn't need to be better at telling time; it needs to be a **fashion accessory** and **status signal**.

**Swatch (1983):**

```
SWATCH DESIGN PHILOSOPHY

Name: "Second watch" (fashion watch you buy multiple of)
      or "Swiss watch" (sa-WATCH) — both interpretations intended

Engineering constraints:
  - Cost target: under SFr 15 wholesale (retail SFr 50)
    (Competing with ¥3,900 Casio)
  - Must be manufactured entirely in Switzerland
    (for Swiss Made positioning)
  - Must be assembled in ≤51 operations (vs 150+ for traditional watch)

Design innovations:
  - Plastic case (polycarbonate or polyamide)
  - Movement mounted DIRECTLY in case back
    (eliminates separate movement holder → fewer parts)
  - 51 components total (vs 91 for traditional Swiss quartz)
  - Ultrasonic welding of case → sealed permanently
    (no serviceability but no service needed; battery lasts 3 years)
  - Movement accessed by cutting open the case
    (no need for removable case back)

ETA Delirium-derived movement (ETA 255.111):
  Thinnest mass-production quartz movement: 0.98 mm thick
  32,768 Hz tuning fork crystal
  ±15 sec/year accuracy (standard, no TCXO)
```

**Commercial result:** Swatch launched in March 1983. By end of 1983, 1 million Swatch watches sold. By 1992, 100 million Swatch watches produced. The Swatch Group (ASUAG + SSIH merged 1983, renamed 1998) became the world's largest watch group.

---

## Modern Quartz: MEMS and the Next Generation

<!-- @editor[bridge/P2]: MEMS section mentions photolithographic manufacture but misses the key bridge: MEMS oscillators are already in every smartphone as the timing reference for the cellular baseband and Wi-Fi PHY. The SiTime SIT1602 or Microchip DSC1001 are in devices this reader carries. The transition from quartz to MEMS in watches is the same transition already completed in the telecom/mobile stack — the watch industry is 10–15 years behind smartphones on this. Also: the "integration with IC" row in the table is the key competitive advantage — a MEMS resonator can be fabricated on the same die as the digital divider chain, collapsing the quartz crystal + CMOS IC stack into a single die. The cost and power implications are significant. -->
**MEMS oscillators** (Micro-Electro-Mechanical Systems) are silicon-based resonators made by photolithographic processes — the same semiconductor fabs that make microchips.

```
MEMS OSCILLATOR vs QUARTZ CRYSTAL

                     | Quartz Crystal      | MEMS Silicon
─────────────────────┼─────────────────────┼────────────────────────
Manufacturing        | Grown crystal, cut  | Photolithography;
                     | and polished        | batch fabrication
Size                 | 1–3 mm (tuning fork)| 0.2–0.5 mm
Cost at volume       | ~$0.50              | ~$0.10
Temperature coeff    | ±30 ppm (AT-cut)    | ±1–3 ppm (with MEMS TCXO)
Frequency aging      | ±1–2 ppm/year       | ±0.1–1 ppm/year
Integration with IC  | External component  | Can be integrated
                     |                     | on same die
Fragility            | Brittle quartz      | Silicon (also brittle)

MEMS oscillators (SiTime, Microchip/Vectron) are already in:
  - Cell phones (timing ICs)
  - IoT sensors
  - Industrial equipment

Not yet in watches (as of 2024): power consumption and long-term
aging performance still optimized for quartz in wearables.
Expected to penetrate watch market in 2020s–2030s.
```

---

## Accuracy Comparison: The Full Spectrum

```
TECHNOLOGY                  | ACCURACY          | DAILY ERROR | APPLICATION
────────────────────────────┼───────────────────┼─────────────┼────────────────────
Verge/foliot mechanical     | ±15 min/day       | ±900 sec    | Pre-1656 tower clocks
Lever mechanical (unregul.) | ±30–60 sec/day    | ±30–60 sec  | Basic mechanical watch
Lever mechanical (COSC)     | ±4 sec/day        | ±4 sec      | COSC chronometer
Standard quartz (XO)        | ±15 sec/year      | ±0.04 sec   | Consumer quartz watch
TCXO quartz                 | ±1–5 sec/year     | ±0.003 sec  | Quality quartz watch
GPS-disciplined quartz      | ±0.001 sec/year   | effectively | GPS radio watch
                            |                   | atomic accuracy
OCXO (lab)                  | ±0.1 ppm          | 0.009 sec   | Lab/telecom ref
Rubidium atomic             | ±5×10⁻¹¹          | 4×10⁻⁶ sec  | GPS satellites (Rb)
Cesium beam (commercial)    | ±2×10⁻¹²          | 2×10⁻⁷ sec  | Primary ref
Cesium fountain (NIST-F2)   | ±3×10⁻¹⁶          | 3×10⁻¹¹ sec | National standard
Optical lattice             | ±1×10⁻¹⁸          | 9×10⁻¹⁴ sec | Frontier research

MECHANICAL vs QUARTZ: The ratio is approximately 100:1 in favor of quartz.
This is the gap that destroyed the Swiss industry.
```

---

## Decision Cheat Sheet: Quartz Technology Selection

```
NEED                               | TECHNOLOGY              | COST (movement)
───────────────────────────────────┼─────────────────────────┼────────────────────
Fashion/casual watch, accuracy     | Standard quartz XO      | $1–$5
  not critical                     | 32,768 Hz, no comp      |

General purpose, ±15 sec/year      | Consumer quartz         | $3–$15
                                   | (most watch movements)  |

Precision dress watch              | TCXO quartz watch       | $20–$100 (movement)

Navigation, field use              | GPS-radio watch         | $50–$200+ (watch)
  (Citizen Eco-Drive GPS,           | Syncs to GPS/radio daily|
   Seiko Astron, Casio Oceanus)     |                         |

Timing reference on local network  | GPS-disciplined OCXO    | $500–$5,000
  (PTP grandmaster clock)           | (GPSDO)                 |

Telecom/5G synchronization         | Rubidium oscillator     | $1,000–$10,000
                                   | + GPS discipline         |

National primary standard          | Cesium fountain         | $500,000+
```

---

## Common Confusion Points

**"Quartz watches need battery replacement but mechanical watches don't."**
Mechanical watches need periodic service (lubrication degrades, parts wear) — every 5–10 years is common. Battery replacement in a quartz watch is typically $5–$15 at a jeweler, every 2–5 years. A mechanical watch service costs $150–$2,000 (brand and complication dependent). The "no battery" advantage of mechanical is real for avoiding routine chemistry, but not for avoiding maintenance cost.

**"All quartz watches are equally accurate."**
No. A standard 32,768 Hz XO watch: ±15 sec/year. A TCXO watch: ±1–5 sec/year. A GPS-disciplined watch: effectively atomic accuracy during reception, then TCXO drift between syncs. The crystal frequency, compensation circuitry, and trim capacitor calibration at manufacture all matter significantly.

**"The Swiss invented quartz watches and then Japan stole the market."**
The Swiss invented the technology (CEH/Neuchâtel, 1967) and chose not to aggressively commercialize it at low prices. Seiko independently developed the same technology, launched first, and more importantly drove the manufacturing cost down with consumer electronics scale production. This was a strategic failure by the Swiss industry, not intellectual property theft.

**"Swatch saved the Swiss watch industry because it was accurate."**
Swatch watches are not particularly accurate (±15 sec/year — standard consumer quartz, no TCXO). Swatch saved the low end of the Swiss industry because it was cheap, fashionable, and reasserted Swiss Made branding at the consumer level, stopping the price collapse. It also gave SMH/Swatch Group the revenue and volume to maintain ETA's ébauche business, which supplied the entire mid-tier Swiss industry.

**"MEMS oscillators will replace quartz crystal in watches soon."**
Probably eventually, but several barriers remain: quartz tuning fork crystals are extremely cheap ($0.50), highly optimized, and well-understood. MEMS oscillators have advantages in integration and high-volume production but haven't demonstrated sufficient long-term aging performance for watch applications. The transition from quartz to MEMS in watches will take longer than the transition in cell phones, where power consumption and size dominate over long-term aging.
