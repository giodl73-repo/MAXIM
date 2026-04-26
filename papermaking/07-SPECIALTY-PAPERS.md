# Specialty Papers: Technical and Security Papers

## The Big Picture

```
+------------------------------------------------------------------+
|              SPECIALTY PAPER LANDSCAPE                           |
|                                                                  |
|   SECURITY          THERMAL        FILTER        CIGARETTE       |
|   ────────          ───────        ──────        ─────────       |
|   Banknotes         Receipts       Lab / coffee  Controlled      |
|   Passports         Labels         Water / air   porosity        |
|   Certificates      Tickets        Separation    Burn rate       |
|                                                                  |
|   RELEASE / SILICONE   ELECTRICAL    CARBONLESS   MEDICAL        |
|   ─────────────────    ──────────    ──────────   ───────        |
|   Label backing        Capacitor     NCR copies   Sterilization  |
|   Baking parchment     Transformer   Self-copying  Wrapping      |
|                        winding                                   |
+------------------------------------------------------------------+
```

Specialty papers = small-volume, high-value segments typically requiring
specific functional properties that commodity papers cannot provide.
Combined: ~5–10% of global paper volume but ~25–35% of paper industry value.

---

## Security Paper

### Banknotes: The Most Demanding Paper Application

Banknote paper must be:
- Durable: 1,000–3,000 folds before tearing (vs. <20 for office paper)
- Chemically stable: resistant to washing machine, food stains, alcohol
- Authenticatable: unique physical features to detect counterfeiting
- Dimensionally stable: consistent dimensions for ATM handling

```
   BANKNOTE PAPER COMPOSITION:
   ─────────────────────────────
   BASE FIBER: Cotton 100% (most traditional) or cotton/linen blend
   Typical: 75–80% cotton linter + 20–25% flax/abaca bast fiber
   No wood pulp — wood pulp degrades, lower tear resistance

   COTON FIBER ADVANTAGES:
   ─────────────────────────
   No lignin → no yellowing, no acid generation
   DP ~5000–7000 → very high tensile/tear
   Wet strength (intrinsic) much better than wood fiber
   Crispness and tactile feel consumers associate with authenticity
```

### Security Features: Layers of Authentication

```
   SUBSTRATE (Level 0 — paper itself):
   ─────────────────────────────────────
   Security fibers: colored or UV-fluorescent fibers dispersed in pulp
   Watermark: 3D density variation created by raised/lowered wire design
               Visible in transmitted light — very difficult to replicate
   Security thread: embedded metal or plastic thread
                    May have holographic, microprinting, or windowed features

   LEVEL 1 (visible, public authentication):
   ────────────────────────────────────────────
   Hologram: diffraction grating on hot-stamped patch
   Color-shifting ink (OVI): changes color at different viewing angles
   Intaglio printing: raised ink (feel with fingernail) — banknote trademark
   Fluorescent ink: UV-visible features
   Serial numbers: laser or letterpress

   LEVEL 2 (machine-readable, ATM / counting machine):
   ─────────────────────────────────────────────────────
   Magnetic ink: machine-detectable magnetic particles
   IR reflectance pattern: specific IR-absorbing/reflecting inks
   UV luminescent patterns: fluorescence under specific UV frequencies

   LEVEL 3 (forensic, government only):
   ─────────────────────────────────────
   Covert chemical or physical markers
   Not publicly disclosed
```

### Watermarks: Technical Details

```
   WATERMARK CREATION:
   ────────────────────
   Dandy roll (for Fourdrinier) or mold (for cylinder molds):
   Metal wire design raised above or recessed below normal wire level

   RAISED WIRE (light watermark):
   ─────────────────────────────
   Less fiber deposits → thinner area → more light transmits → looks lighter

   RECESSED WIRE (dark watermark):
   ────────────────────────────────
   More fiber deposits → thicker area → less light → looks darker

   MULTI-TONE WATERMARK: combination of raised + recessed
   Produces photographic-quality portrait watermarks (Euros, pounds)
```

### Polymer Banknotes (Alternative to Paper)

Australia's polymer notes (1988, De La Rue / RBA initiative) — BOPP (biaxially
oriented polypropylene) substrate with window features:

```
   POLYMER NOTE ADVANTAGES:
   ─────────────────────────
   Longer life: 2.5–4× cotton paper
   Machine-washable without damage
   Transparent window elements (harder to replicate)
   RFID or holographic integration

   LIMITATIONS:
   ─────────────
   Cannot convey traditional watermark
   Different tactile feel (reduced cultural acceptance in some markets)
   Less environmentally sustainable per-note (polymer, not cotton rag)
   Australia, UK (2016), Canada (2013), NZ, Thailand use polymer notes
```

---

## Thermal Paper

### How Thermal Paper Works

```
   THERMAL PAPER LAYER STRUCTURE:
   ──────────────────────────────────
   TOPCOAT:     protective layer (optional), reduces head wear
   THERMAL LAYER: color former (leuco dye) + developer + sensitizer
   BARRIER:     prevents thermal layer seeping into base paper
   BASE PAPER:  typically 55–80 gsm wood-free or mechanical
   BACKCOAT:    anti-curl, anti-stick (optional)

   REACTION:
   ──────────
   Thermal printhead: local heating to 60–70°C
   Heat melts sensitizer (low Tm, ~55–65°C)
   Sensitizer creates mobile eutectic with developer
   Developer (phenolic) + leuco dye → colored dye form (black)
   Cooling: color formation locked in

   LEUCO DYE MECHANISM:
   ─────────────────────
   Crystal violet lactone (CVL), fluorene derivatives
   Colorless lactone form (closed ring)
   + proton from phenolic developer → ring opens → colored quinoid form
```

### BPA Controversy and Alternatives

```
   BISPHENOL A (BPA) was dominant developer for decades:
   ──────────────────────────────────────────────────────
   Effective, cheap, good image stability
   BUT: BPA is an endocrine disruptor (REACH SVHC 2016)
   Thermal paper is a significant BPA dermal exposure source
   (Cash register operators: 3–5× higher BPA urine levels)

   ALTERNATIVES:
   ──────────────
   BPS (bisphenol S): similar EDC concerns — not a clean solution
   BPAP, BPF: under regulatory review
   D-8: Pergafast 201 (D-8, Meiwa Kasei): more expensive but BPA-free
   Leuco dye + non-bisphenol developers: increasing market share
   EU: BPA banned in thermal paper from January 2020
```

### Thermal Paper Applications

| Application | Grammage | Special requirements |
|-------------|----------|---------------------|
| Point-of-sale receipt | 55–65 gsm | High-speed printing, cost |
| ATM receipt | 55–80 gsm | Durability, storage stability |
| Lottery ticket | 75–80 gsm | Fraud resistance, security features |
| Shipping label | 90–120 gsm | Weather resistance, adhesive |
| Parking ticket | 75–90 gsm | UV stability, outdoor |
| Medical chart recorder | 80–120 gsm | Long-term record (25+ years) |

---

## Filter Paper

Filter paper must have precise, reproducible pore structures and well-
controlled flow rates.

```
   LABORATORY FILTER PAPER (Whatman-type):
   ─────────────────────────────────────────
   Fiber: pure cotton linters (no cellulose fines — would clog pores)
   Basis weight: 80–200 gsm
   Pore size: defined by cellulose fiber diameter + wet-web drainage
   Grade system (Whatman 1–5, 40–43, etc.):
     Grade 1: 11 µm retention — general purpose (coffee filtration)
     Grade 2: 8 µm — light precipitates, clarification
     Grade 4: 20–25 µm — fast flow rate, coarse precipitates
     Grade 5: 2.5 µm — fine precipitates, slow
   Hardened grades (Grade 541, 542): treated with HNO3, acid-washed
     → More precise pore, stable in aggressive solvents

   AUTOCLAVING: cotton filter paper can be autoclaved (121°C, 15min)
   without loss of integrity (unlike glass fiber or polymer membranes)
```

### Coffee Filter Paper

```
   COFFEE FILTER (commercial pour-over / drip):
   ──────────────────────────────────────────────
   Grammage: 80–120 gsm
   Fiber: often softwood kraft or cotton blend
   Pore size: 10–30 µm retention target
   Wet strength essential: saturated with hot water, must not tear
   Taste neutrality: no bleach odor → typically ECF or TCF bleached
   Folding patterns (Melitta, conical): designed to optimize flow
   Oxygen-bleached "natural brown" vs. bleached white: same filtration
```

### Automotive and Industrial Filters

```
   AIR FILTER (engine intake, HVAC):
   ────────────────────────────────────
   Media: glass fiber + cellulose blend, often wet-laid nonwoven
   Efficiency rating: HEPA (99.97% @ 0.3 µm), MERV system
   Formation quality critical: local pore anomalies = bypass
   Calendering to precise thickness for housing fit

   FUEL FILTER:
   ─────────────
   Cellulose + glass fiber wet-laid
   Must resist fuel (hydrocarbons, alcohols, FAME)
   Wet-strength treatment essential
   Water separation efficiency: removes dissolved water from diesel
```

---

## Cigarette Paper

One of the most precisely engineered papers in terms of porosity control.

```
   CIGARETTE PAPER REQUIREMENTS:
   ──────────────────────────────
   Grammage: 18–26 gsm (extremely thin)
   Air permeability: 10–150 CU (Coresta Units) — controlled precisely
   Burn rate: must match tobacco burn for even smoke delivery
   Ash: white, cohesive ash (CaCO3 filler to control)
   Burn additives (fire standards): potassium citrate/acetate (cigarette
     paper burn rate modifier); newer "fire safe cigarette" regulations
     require banding (reduced-permeability bands)

   FIBER: usually flax (high purity, good porosity) or wood blend
   Bleaching: ECF or TCF (taste neutrality essential)
   Sizing: minimal — must be porous, not sized

   REGULATED DESIGN:
   ──────────────────
   EU/US fire standards mandate "low ignition propensity" (LIP):
   Bands of reduced-permeability paper (high-citrate sizing)
   → Cigarette self-extinguishes if not puffed
   → Reduces ignition fires
```

---

## Release Paper (Silicone-Coated)

Used as the backing for pressure-sensitive adhesive (PSA) labels and tapes.

```
   FUNCTION:
   ──────────
   Paper coated with silicone → very low surface energy (~21 mJ/m²)
   PSA adhesive on one side, silicone release layer on other
   → Label peels from silicone cleanly

   RELEASE LINER CONSTRUCTION:
   ─────────────────────────────
   BASE PAPER:  glassine, SCK (super-calendered kraft), clay-coated
   PRIMER:      polyethylene or acrylate (improves silicone adhesion to paper)
   SILICONE:    solvent-based, solvent-free, or emulsion silicone coating
                Thermal cure or UV cure
                Coat weight: 0.5–2 g/m² (very thin)
   PSA ADHESIVE: applied by label converter

   SILICONE RELEASE FORCE:
   ──────────────────────────
   Low release (tight): paper-based, high-speed dispensing
   Medium release: standard label and tape applications
   High release (easy): hand-applied, slow dispensing
   Controlled by: silicone type, cure level, surface roughness, anchor layer
```

---

## Technical / Electrical Papers

```
   CAPACITOR TISSUE:
   ──────────────────
   Very thin (4–10 gsm), uniform density
   Electrolytic capacitor winding (aluminum foil + paper electrolyte)
   Requires: extreme formation uniformity, no conductive particles,
             controlled pore structure, pure cellulose (no ionic extractives)

   TRANSFORMER INSULATION (crepe paper):
   ────────────────────────────────────────
   Kraft paper crêped for flexibility and extensibility
   Oil-impregnated (mineral oil): provides electrical insulation + cooling
   Use: transformer winding insulation (oil-filled transformers)
   Dielectric breakdown voltage > 10 kV/mm required

   BATTERY SEPARATOR:
   ───────────────────
   Cellulose / regenerated cellulose (viscose)
   Non-conducting, porous, electrolyte-wettable
   Used in lead-acid batteries (separators between plates)
   Increasingly displaced by polyolefin separators in Li-ion
```

---

## Defense-in-Depth Bridge

Banknote security architecture is defense-in-depth applied to physical authentication:

```
BANKNOTE SECURITY — LAYERED AUTHENTICATION ARCHITECTURE
=========================================================

LAYER           SECURITY ELEMENT         DETECTION METHOD
=====           ================         ================
Substrate       Cotton/linen fiber        Feel (softness, crinkle)
(physical)      Security thread           Backlight (embedded strip)
                Watermark                 Backlight (portrait/numeral)
                Colored security fibers   UV lamp (fluoresce)
                → defeats: home printer, photocopier, inkjet

Visible         Intaglio (raised ink)     Fingernail (tactile ridge)
(overt)         Color-shifting ink (OVI)  Tilt (green→gold shift)
                Microprinting            10× loupe
                UV fluorescent ink       UV lamp
                → defeats: high-res scanner, offset replica

Machine-        Magnetic ink (MICR)       Reader at cash machine
readable        IR transparency           Banknote sorter
(covert)        Currency authentication   Verification terminal
                machine (CIS sensors)
                → defeats: visual-only counterfeits

Forensic        Chemical taggants         Lab analysis only
(covert         Isotopic markers          Mass spectrometry
advanced)       Machine-readable serial   Central database query
                number encoding
                → defeats: sophisticated forgeries that pass
                           all prior layers

ARCHITECTURE PRINCIPLE:
  Each layer catches what the previous one misses. No single layer
  is sufficient. Identical to network security defense-in-depth:
  perimeter firewall → network IDS → host-based IDS → application
  WAF → SIEM monitoring. An attacker who defeats layer N still faces
  layer N+1. The multi-layer design means the cost of defeating ALL
  layers exceeds the value of successful forgery.

  The counterfeit detection heuristic: "check the easy layer first"
  (feel, tilt) — same as security triage: check for missing TLS
  before running a full pentest. Obvious failures exit early; the
  expensive forensic layer is reserved for edge cases.
```

## Decision Cheat Sheet

| Specialty need | Paper type |
|---------------|------------|
| Banknote / currency | Cotton/linen security paper, security thread, watermark |
| Receipt / point of sale | BPA-free thermal paper |
| Long-term medical record | High-density thermal (25+ year image life) |
| Coffee filtration | 80–120 gsm, ECF-bleached, wet-strength cotton/SW blend |
| Lab filtration precise pore | Whatman-type hardened cotton filter |
| Air filter media | Glass fiber / cellulose wet-laid composite |
| Label backing | Glassine + silicone release coating |
| Capacitor | Ultra-clean, ultra-thin (6–8 gsm) tissue |
| Cigarette paper | 18–26 gsm, controlled porosity, flax-based |

---

## Common Confusion Points

**Watermarks cannot be digitally replicated**: A watermark is a three-dimensional
density variation embedded in the paper fiber web itself, visible only in
transmitted light. Digital printing on paper surface cannot replicate this —
any attempt to photocopy and print a watermark requires a non-watermarked
substrate that will lack the effect. This is why traditional cotton banknote
paper remains in use despite polymer alternatives.

**Thermal paper images are not permanent**: Heat, solvents (alcohols, hand
sanitizers), UV light, and moisture can bleach thermal images over time. "Extended
life thermal" (25-year rated) grades exist for medical records but cost 5–10×
standard receipt paper. Standard receipt paper: expect 2–7 year image life under
normal storage.

**All filter papers are not equivalent**: The Whatman grade system is not
just marketing — pore size reproducibility (±20% on retention rating) is
achieved through fiber selection and controlled beating. Substituting a
different brand "equivalent grade" in a validated analytical method requires
performance re-validation.
