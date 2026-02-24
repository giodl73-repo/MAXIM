# Deposition — A Layered Guide

## The Big Picture

Deposition adds material to the wafer with atomic-level control. Every film —
gate oxide, gate metal, barrier layer, dielectric, copper seed — is deposited
by one of three fundamental mechanisms: chemical vapor deposition (CVD),
atomic layer deposition (ALD), or physical vapor deposition (PVD).

```
DEPOSITION METHODS — SELECTION MAP
════════════════════════════════════════════════════════════════════

                    CONFORMAL?        THICKNESS CONTROL
                    ──────────────    ────────────────────
CVD (thermal)       Good              Continuous (rate × time)
PECVD               Moderate-Good     Continuous (rate × time)
ALD                 Excellent         Atomic-layer exact (cycles × layer thickness)
PVD/Sputtering      Line-of-sight     Continuous (rate × time)
Epitaxy             Crystalline       Atomic monolayers

                    BEST USE
                    ────────────────────────────────────────
CVD (thermal)       SiO₂, Si₃N₄, poly-Si, HDP oxide gap fill
PECVD               Low-k ILD, SiN hardmask, lower temp allowed
ALD                 High-k gate oxide, barrier/liner layers, conformal everywhere
PVD/Sputtering      Metals (Ti/Ta/TaN/W seed), aluminum, copper seed
MBE/CVD Epitaxy     Strained SiGe source/drain, Si channel, III-V for RF/optoelectronics
```

---

## Chemical Vapor Deposition (CVD)

```
CVD FUNDAMENTALS

PRINCIPLE:
  Gas-phase precursors flow over heated wafer
  Chemical reaction at surface deposits solid film + volatile byproducts

GENERIC REACTION:
  SiH₄ + 2H₂O → SiO₂ + 4H₂   (silane oxidation — TEOS variant common)
  3SiH₂Cl₂ + 4NH₃ → Si₃N₄ + 6HCl + 6H₂   (LPCVD silicon nitride)

REACTION REGIMES:
  Surface-reaction limited (lower T):
    Rate controlled by surface chemistry
    Excellent uniformity (wafer rotates; uniform gas supply)
    Better step coverage/conformality
  Mass-transport limited (higher T):
    Rate controlled by gas diffusion to surface
    Non-uniform (center vs edge differences)
    Preferred for thick films needing speed

CVD VARIANTS:

APCVD (Atmospheric Pressure CVD):
  Simple, fast, mass-transport limited
  Poor uniformity and step coverage
  Used: BPSG (borophosphosilicate glass) reflow layers at older nodes

LPCVD (Low Pressure CVD):
  10-100 Pa vacuum
  Batch process: 100-200 wafers vertical tube furnace at 550-900°C
  Surface-reaction limited → excellent uniformity and conformality
  Films: poly-Si (gate), Si₃N₄ (hardmask, spacer), TEOS-SiO₂
  Downside: high temperature (not CMOS-compatible for back end)

HDP-CVD (High Density Plasma CVD):
  Simultaneous deposition + ion bombardment (sputter-etch)
  Net deposition where deposition > etch rate
  → Self-planarizing void-free gap fill in narrow trenches
  Fills aspect ratio 4:1+ without voids
  Used for: STI (Shallow Trench Isolation) fill, pre-metal dielectric

SACVD (Sub-Atmospheric CVD):
  TEOS + ozone at 200-600°C, ~40 kPa
  Excellent conformality without plasma
  USG (undoped silicate glass) or BPSG fill between metal lines
```

---

## Plasma-Enhanced CVD (PECVD)

```
PECVD

MOTIVATION:
  Many back-end materials can't withstand 600°C+ LPCVD temperatures
  (Copper melts at 1084°C but interconnect dielectrics must deposit on Cu at <400°C)
  Plasma provides energy to drive reactions at 200-400°C

MECHANISM:
  RF plasma (13.56 MHz typical) dissociates precursor gases into reactive radicals
  Radicals react at wafer surface at much lower temperature than thermal CVD
  Ion bombardment can increase film density

FILMS DEPOSITED:
  SiO₂:  SiH₄ + N₂O → SiO₂   (PECVD oxide, fast, low-temp)
  SiN:   SiH₄ + NH₃ → SiNx   (etch stop, diffusion barrier, passivation)
  SiCN:  Used as barrier layer between Cu and dielectric
  Low-k SiCOH: carbon-doped oxide (k = 2.7-3.0); 193i PMD, ULKD (k ≈ 2.4)
  SiC:   Hard mask for EUV/193i patterning
  a-Si:  Amorphous silicon (sacrificial), TFTs for displays

PLASMA TYPES:
  CCP (Capacitively Coupled Plasma): simple, moderate density
  ICP (Inductively Coupled Plasma): higher density, better conformality
  HDPCVD: densest plasma, simultaneous sputter-etch capability

CONFORMAL DEPOSITION:
  PECVD films moderate conformality — sidewall coverage 70-80% of top coverage
  Not ideal for high-aspect-ratio features → ALD fills that role
```

---

## Atomic Layer Deposition (ALD)

```
ALD — ATOMIC LAYER DEPOSITION

THE KEY INNOVATION:
  Self-limiting surface chemistry → exactly one atomic monolayer per cycle
  Cycle precision: 0.05-0.20 nm per cycle depending on material
  Conformal to any geometry: 100:1 aspect ratio trenches still get uniform coating

HALF-REACTION CYCLE:
  Film: Al₂O₃ from TMA + H₂O (the textbook example)

  Pulse A: TMA (trimethylaluminum) — Al(CH₃)₃
    ─ TMA adsorbs on OH-terminated surface: Al bonds to surface O
    ─ Methyl groups remain attached (self-limiting: no more reaction after monolayer)
    ─ Purge excess TMA and CH₄ byproduct with N₂

  Pulse B: H₂O (water)
    ─ H₂O reacts with surface methyl groups: −Al-CH₃ + H₂O → −Al-OH + CH₄
    ─ Surface returned to OH state, ready for next cycle
    ─ Purge excess H₂O and CH₄

  One cycle ≈ 0.1 nm Al₂O₃
  100 cycles = 10 nm Al₂O₃ (uniform, conformal, pinhole-free)

THERMAL ALD vs PLASMA ALD:
  Thermal ALD: both pulses are just precursor gases + purge; requires higher T
  PEALD (Plasma-Enhanced ALD): oxidant is O₂ plasma or N₂ plasma
    → Lower temperature, higher reactivity, used for metals and nitrides

CRITICAL APPLICATIONS IN LEADING-EDGE LOGIC:

HIGH-k GATE DIELECTRIC (HfO₂):
  Gate oxide SiO₂ can't scale below ~0.8 nm (leakage + reliability)
  ALD HfO₂: k = 22 vs SiO₂ k = 3.9
  Equivalent oxide thickness (EOT) achieved with physically thicker HfO₂
    Physical 2 nm HfO₂ → EOT = 2 × (3.9/22) = 0.35 nm
  ALD control essential: must be exactly the right thickness, uniform

BARRIER LAYERS (TaN/Ta for Cu damascene):
  Cu diffuses into SiO₂ and Si at room temperature → killer contamination
  ALD TaN (0.5-2 nm): conformal barrier lining all Cu trenches and vias
  Followed by ALD Ta or PVD Ta → Cu seed layer

SPACER/LINER DIELECTRICS:
  Transistor spacers (Si₃N₄, SiO₂) now deposited by ALD for conformality
  Etch stop layers: SiN or SiCN by ALD

CONFORMAL FILL:
  ALD in combination with ATOMIC LAYER ETCH (ALE):
  ALD fills bottom-up; ALE trims sides → true 3D structure control
  Key for GAA nanosheet fabrication (inner spacers between nanosheets)

ALD THROUGHPUT:
  Cycle time: 0.5-2 seconds per cycle (purge time dominates)
  To deposit 5 nm HfO₂: ~50 cycles = 25-100 seconds per wafer
  Single-wafer ALD tool: 100-200 wafers/hour depending on target thickness
  Spatial ALD: multiple zones, wafer moves through instead of purging → higher throughput
```

---

## Physical Vapor Deposition (PVD) / Sputtering

```
PVD / SPUTTERING

PRINCIPLE:
  Physical ejection of atoms from a target material; no chemical reaction
  Target material atom-for-atom becomes film

SPUTTERING PROCESS:
  1. Chamber evacuated to ~10⁻⁸ Torr base pressure
  2. Ar gas admitted (~10⁻³ Torr)
  3. DC or RF power ionizes Ar → plasma
  4. Ar⁺ ions accelerated to target (at high negative voltage)
  5. Ar⁺ physically knocks out target atoms (sputtering yield ~1-3 atoms/ion)
  6. Target atoms travel in nearly straight lines → deposit on wafer
  7. Result: thin film of target material on wafer

LINE-OF-SIGHT LIMITATION:
  PVD is directional → poor step coverage in high-aspect-ratio features
  Solution: collimated PVD (long mean free path) or ionized metal PVD (IMPVD)
  IMPVD: metal atoms ionized → directed by substrate bias → fills vias better

KEY PVD APPLICATIONS:

TITANIUM / TITANIUM NITRIDE (Ti/TiN):
  Ti: adhesion + contact layer for W plugs in FEOL
  TiN: diffusion barrier (old node), hard mask, gate metal (in HKMG)
  Deposited by PVD; TiN also by reactive sputtering (Ti target + N₂)

TANTALUM / TANTALUM NITRIDE (Ta/TaN):
  Combined ALD TaN (barrier) + PVD Ta (wetting) + PVD Cu seed
  TaN by reactive PVD (Ta target + N₂) or ALD; Ta by PVD

ALUMINUM (Al):
  Top-level bond pads still Al (easier wire bonding than Cu)
  Al sputter deposition: reflowed at 400-450°C to fill contacts

COPPER SEED:
  ALD/PVD barrier → thin PVD Cu seed layer → electroplating (ECD) for bulk Cu fill
  PVD Cu seed: 20-50 nm conformal seed for subsequent electroplating

REACTICE SPUTTERING:
  Target + reactive gas → compound film
  TiN: Ti + N₂ → TiN
  TaN: Ta + N₂ → TaN
  ZrO₂: Zr + O₂ → ZrO₂ (gate dielectric in older processes)
```

---

## Epitaxy

```
EPITAXIAL DEPOSITION

PRINCIPLE:
  Atomic layer by layer deposition that maintains crystalline alignment with substrate
  Homo-epitaxy: same material (Si on Si)
  Hetero-epitaxy: different material on substrate (SiGe on Si, GaAs on Si)

WHY EPITAXY MATTERS FOR TRANSISTORS:
  Source/drain STRAIN ENGINEERING (critical since 90 nm node):
    SiGe has 4.2% larger lattice constant than Si
    Compressively strained SiGe in p-MOS S/D → compresses Si channel laterally
    → Increases hole mobility 50-100% → faster p-MOS
    Tensile SiP (Si:P) in n-MOS S/D → stretches Si channel
    → Increases electron mobility ~20%
    Intel introduced this at 90 nm (2003): "Strained Si" — one of the biggest
    single-generation performance leaps

CVD EPITAXY PROCESS:
  Si and SiGe: reduced pressure CVD (RPCVD) at 650-800°C
  Precursors: SiH₂Cl₂ (dichlorosilane, DCS) or SiH₄ + GeH₄ (for SiGe)
  H₂ carrier gas
  Selective epitaxy: grows only on exposed Si, not on SiO₂ spacers
    → Epitaxial raised source/drain without depositing everywhere

MOLECULAR BEAM EPITAXY (MBE):
  Ultra-high vacuum (10⁻¹⁰ Torr)
  Effusion cells evaporate source materials → molecular beams → substrate
  Shutter control: monolayer-by-monolayer growth
  Very slow, very controlled
  Used for: III-V semiconductors (GaAs, InP, AlGaAs), research, RF/optoelectronics
  NOT used in CMOS production (too slow, batch size 1)

III-V EPITAXY FOR RF:
  GaN-on-SiC: AlGaN/GaN heterostructure HEMT (high-electron-mobility transistor)
  GaAs pHEMT: power amplifiers in mobile phones
  InP HBT: millimeter-wave circuits, Ethernet lasers
  All grown by MOCVD (Metal-Organic CVD) or MBE on semi-insulating substrates
```

---

## Decision Cheat Sheet

| Material / Application | Deposition Method |
|-----------------------|-------------------|
| High-k gate dielectric (HfO₂) | Thermal ALD (TDMAH + O₃/H₂O) |
| Cu barrier (TaN, 0.5-2 nm) | ALD TaN (most conformal) |
| Cu seed layer | PVD Cu (~20-50 nm) |
| Tungsten (W) plug fill | CVD W (WF₆ + H₂/SiH₄) |
| STI gap fill (SiO₂) | HDP-CVD or FCVD (flowable CVD) |
| Low-k interlayer dielectric | PECVD SiCOH (k ≈ 2.5-3.0) |
| Transistor spacer (Si₃N₄) | ALD (conformal) |
| Strained SiGe source/drain | Selective CVD epitaxy (RPCVD) |
| TiN hard mask / gate metal | PVD or ALD TiN |
| III-V RF device epi | MOCVD (InP, GaAs, GaN) |

---

## Common Confusion Points

**ALD is not just "slow CVD"**: ALD is self-limiting by chemistry — the surface saturates and
stops reacting regardless of exposure time. This is fundamentally different from CVD where more
gas = more film. ALD's thickness precision is inherent to the mechanism, not just careful timing.

**CVD and ALD don't leave gas bubbles**: A common mental model is that films have interior
voids. They don't — atoms deposit on the surface atom by atom. Voids form at the macro scale
from shadowing (PVD) or insufficient fill (CVD at high aspect ratio) — HDP-CVD sputter-etch
mechanism is specifically designed to prevent this.

**"Conformal" has a specific meaning**: A conformal film has the same thickness on horizontal
surfaces, vertical sidewalls, and in corners. PVD is non-conformal (thicker on horizontal surfaces,
thin on sidewalls). ALD is perfectly conformal. CVD varies. For a 10:1 aspect ratio trench, only
ALD reliably coats the bottom.

**Epitaxy strain has limits**: If the SiGe or other epitaxial layer exceeds the "critical thickness"
for a given Ge content, the lattice relaxes by forming dislocations — defeating the purpose.
Critical thickness for Si₀.₈Ge₀.₂ (20% Ge) ≈ 15 nm. Transistor source/drain designs must
stay within this limit.
