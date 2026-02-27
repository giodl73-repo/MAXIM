# Packaging — A Layered Guide

## The Big Picture

Packaging connects the die to the outside world — power, signals, cooling — while
protecting it physically. Modern packaging has evolved from simple wire bonding to
complex 3D stacks with TSVs, hybrid bonding, and chiplet architectures that are
now a core part of the performance scaling roadmap.

```
PACKAGING HIERARCHY
════════════════════════════════════════════════════════════════════

DIE LEVEL (bare silicon chip)
  │
  ▼ First-level interconnect (connects die to package)
PACKAGE (IC package)
  Wire bond / Flip-chip / Embedded / Fan-out WLP
  │
  ▼ Second-level interconnect (connects package to PCB)
PCB (Printed Circuit Board)
  BGA solder balls / LGA pads / QFP leads
  │
  ▼ System-level
SYSTEM (server, phone, car module)

ADVANCED PACKAGING (2.5D / 3D):
  Interposer or bridge connects multiple dies in same package
  → "System in Package" (SiP): near-die integration of memory + logic
  → Near-chiplet performance with mix-and-match fabrication
```

---

## Wire Bonding

```
WIRE BONDING — LEGACY, STILL DOMINANT FOR COST SEGMENTS

MECHANISM:
  Gold (Au) or copper (Cu) or aluminum (Al) wire (15-75 µm diameter)
  Thermosonic bonding (heat + ultrasonic + pressure):
    Ball bond: wire melts → gold ball → bonded to die pad (Al bond pad)
    Stitch bond: wedge bond to package substrate or leadframe
    Result: electrical connection from die pad to package terminal

PROCESS:
  Die flip face-up → attach to substrate (epoxy or solder)
  Capillary tool: form ball → position over die pad → press + ultrasonic
  → Pull wire arc → form stitch on substrate pad → clip wire
  High-speed: 10-20 bonds/second per machine head

PITCH LIMITATION:
  Bond pad pitch: 40-60 µm (fine pitch) down to ~25 µm (ultra-fine)
  Wire span: up to 5 mm (longer → sagging, cross-shorting risk)

ADVANTAGES:
  Simple, low cost, mature, robust
  Suitable for: commodity DRAM, mobile processors in cost-sensitive designs,
               microcontrollers, power ICs, analog, automotive

DISADVANTAGES:
  Long wire = inductance (bad for RF, high-speed)
  Pad area on die = wasted silicon
  Not suitable for >1000 I/O at fine pitch
  Single-sided (die face up → wire out)
```

---

## Flip-Chip (C4 Bumps)

```
FLIP-CHIP — THE DOMINANT HIGH-PERFORMANCE PACKAGE INTERCONNECT

CONCEPT:
  Die flipped face-down → solder bumps directly on die surface → attach to substrate
  No wire: solder bump = shortest possible electrical path

C4 BUMPS (Controlled Collapse Chip Connection — IBM, 1964):
  Solder bumps on die: SnPb (old) → lead-free SnAgCu (SAC) solder
  Bump diameter: 50-250 µm (area-array across full die surface)
  Pitch: 100-200 µm (peripheral) or 150-250 µm (area array) for traditional FC
  Micro-bumps (advanced): 20-50 µm diameter at 40-100 µm pitch

PROCESS:
  Wafer-level: deposit UBM (Under-Bump Metallurgy: Ti/NiV/Cu) → electro-plate SnAg
  Reflow: solder wets to substrate pads → self-aligns (surface tension)
  Underfill: capillary-fill epoxy between die and substrate → CTE mismatch relief

UNDERFILL:
  Die: Si, CTE = 3 ppm/°C
  Organic substrate: CTE = 14-18 ppm/°C
  Temperature cycles (−40 to +125°C): 100+ ppm strain differential → solder fatigue
  Underfill epoxy distributes stress across entire die-substrate interface → reliability

ADVANTAGES OVER WIRE BOND:
  Much higher I/O count (area array, not perimeter only) → 10,000+ I/O on large die
  Lower inductance (shorter path)
  Better electrical performance (signal integrity, power delivery)
  Smaller package footprint

SUBSTRATE (flip-chip BGA):
  Organic laminate: FR4 or ABF (Ajinomoto Build-up Film)
  Fine lines: 8/8 µm (line/space) → 2/2 µm (advanced ABF)
  RDL (redistribution layer): routes from bump pitch to BGA ball pitch
```

---

## Fan-Out Wafer-Level Packaging (FOWLP)

```
FAN-OUT WLP (FOWLP) — THIN, SUBSTRATE-FREE PACKAGING

CONCEPT:
  No traditional substrate — RDL built directly around die
  "Fan-out": I/O extends beyond die footprint using embedded routing

PROCESS:
  1. Pick dies → embed in molding compound (reconstituted wafer)
  2. CMP flatten to expose die back + mold compound surface
  3. Build RDL (redistribution layers) directly on top of die + mold
  4. Solder balls on RDL
  5. Dice into individual packages

InFO (Integrated Fan-Out, TSMC):
  Apple A12-A17 iPhones: logic die + memory in same mold compound
  No PCB substrate: ultra-thin package (good for phone form factor)
  Advanced InFO: 2-4 RDL layers, sub-10 µm line/space on top RDL

ADVANTAGES:
  Very thin (phone-friendly)
  Lower parasitics than BGA substrate
  Integrates multiple dies without silicon interposer cost

EWLB (Embedded Wafer Level Ball Grid Array, Infineon/STM):
  Similar concept, widely used for RF chips, sensors, analog
```

---

Chiplet disaggregation is **microservice decomposition applied to silicon**: splitting a monolithic SoC into independently manufactured dies (CPU compute die + I/O die + HBM stacks), each built on its optimal process node, connected by standardized interconnect contracts (UCIe is the API contract, specifying bandwidth/latency/protocol). The yield benefit is the same as deploying independent services: a defect in one chiplet doesn't scrap the entire package, and each function can iterate on its own release cadence.

## 2.5D: Interposer and CoWoS

```
2.5D INTEGRATION (INTERPOSER-BASED)

CONCEPT:
  Multiple dies placed side-by-side on an interposer (intermediate substrate)
  Short high-bandwidth connections between dies on the interposer
  → Logic die + HBM (High Bandwidth Memory) in same package

SILICON INTERPOSER:
  Passive Si die with through-silicon vias (TSVs) and fine RDL routing
  TSVs: 10 µm diameter × 100 µm deep → connect front RDL to solder bumps below
  Top RDL: 0.4-1 µm line/space (vs ABF substrate: 2-8 µm) → much finer pitch
  Enables: micro-bumps at 40-55 µm pitch between logic die and HBM stack

CoWoS (Chip-on-Wafer-on-Substrate, TSMC):
  Process:
    1. Build silicon interposer wafer with TSVs
    2. Flip-chip attach multiple dies onto interposer wafer
    3. Dice interposer into individual multi-die units
    4. Mount on organic BGA substrate

CoWoS-S (Silicon interposer): NVIDIA A100, H100, H200 → largest logic + 6× HBM2e/HBM3
CoWoS-R (RDL interposer): organic or glass RDL, lower cost, moderate fine-pitch
CoWoS-L (Chip-last): chips mounted on pre-built silicon bridge

HBM MEMORY STACK:
  8-12 DRAM dies stacked using TSVs → very high I/O count (~1024-bit wide bus)
  HBM3: 1024-bit bus, 3.2 Gbps/pin → 409 GB/s per stack
  4-6 HBM stacks on A100: 2+ TB/s total bandwidth (vs 1× DDR5: 51 GB/s)

CURRENT CUSTOMERS:
  NVIDIA A100/H100/H200/B200: CoWoS-S with 6-8 HBM3 stacks
  AMD MI300X: 3D HBM + logic over interposer
  Google TPUv5: custom interposer packaging
```

---

## 3D IC Stacking: TSV and Hybrid Bonding

```
3D IC — THROUGH-SILICON VIA (TSV) STACKING

TSV PROCESS:
  Via etching: DRIE Bosch process through partial or full wafer
    TSV diameter: 5-10 µm; depth: 50-100 µm for backside TSV
  Insulation: ALD SiO₂ liner (prevents Cu diffusion to Si)
  Barrier: ALD TaN
  Fill: Cu electroplating
  Reveal: thin wafer to 50-100 µm → expose TSV tips on backside
  Micro-bump: Cu pillar or µ-solder on both die surfaces

MEMORY STACKING (HBM):
  DRAM die thinned to 50-70 µm
  TSVs through each DRAM die: ~Ø10 µm × 70 µm deep
  TC (thermocompression) bonding: heat + pressure bonds Cu-Cu pillars
  Stack: base logic die + 4-12 DRAM dies
  Benefits: massive bandwidth (1024-bit wide), low power vs DDR (shorter path)

HYBRID BONDING (DIRECT BOND INTERCONNECT, DBI):
  No bumps at all — direct Cu-to-Cu atomic bonding
  Process:
    1. CMP polish Cu pad surface to <0.5 nm roughness
    2. Align die/wafer using sub-µm vision systems
    3. Low-temperature (200-350°C) anneal → Cu diffuses across interface
    4. Result: continuous Cu joint (no bump, no solder)
  Pitch: 1-10 µm (vs 40-100 µm for micro-bumps)
  → 100-1000× more connections per mm² than flip-chip micro-bumps

HYBRID BONDING PRODUCTS:
  Sony IMX image sensors: stacked pixel + logic using hybrid bonding (since 2012)
  Apple A17 Pro: SRAM stacked on top of SoC using hybrid bonding
  AMD 3D V-Cache: L3 SRAM chiplet stacked on CPU using hybrid bonding (2022)
  SK Hynix HBM4: hybrid bonding for chip-to-chip in stack (2025+)
  Bandwidth density: hybrid bonding → 1 TB/s+ per mm² feasible
```

---

## Chiplet Architecture

```
CHIPLET DISAGGREGATION

MOTIVATION:
  Monolithic die: as die area increases, yield falls exponentially
  10 cm² monolithic die at 90% yield/cm² → overall yield ≈ 1%
  Split into 2×5 cm² chiplets at 95% yield/cm² → 90% system yield
  → Yield economics drive chiplet adoption at leading edge

  Different functions benefit from different nodes:
  Logic: needs 3 nm for performance/power
  I/O: works fine at 7 nm (simpler, cheaper)
  SRAM: optimized at 5 nm
  → Mix and match chiplets from optimal nodes per function

CHIPLET EXAMPLES:
  AMD EPYC Genoa (2022):
    12 × Zen 4 CCD (Core Complex Die): 5 nm TSMC, 8 cores each
    1 × IOD (I/O Die): 6 nm TSMC (PCIe, memory controller)
    Assembled on organic substrate

  Intel Meteor Lake (2023):
    CPU Tile: Intel 4 (EUV)
    GPU Tile: TSMC N5
    I/O Tile: TSMC N6
    SoC Tile: TSMC N6
    Connected by Intel Foveros 3D stacking + die-to-die interconnects

  AMD MI300X:
    4 × GPU dies (5 nm TSMC) + 4 × HBM stacks + 1 × CDNA3 base logic
    Interposer-based + 3D stacking

CHIPLET INTERCONNECT STANDARDS:

UCIe (Universal Chiplet Interconnect Express — 2022):
  Open standard for die-to-die interconnect
  Backed by: Intel, AMD, Arm, Qualcomm, Google, Samsung, TSMC, ASML
  Standard Package (organic substrate): 2 Tbps/mm width, <0.5 pJ/bit
  Advanced Package (silicon bridge): 16 Tbps/mm width, <0.2 pJ/bit
  Goal: mix chiplets from different vendors/foundries → ecosystem

AIB (Advanced Interface Bus, Intel): proprietary, Intel ecosystem
BoW (Bunch of Wires, OIF): optical interconnect oriented
XSR (Short Reach SerDes): TSMC/Broadcom standard
```

---

## Decision Cheat Sheet

| Application | Packaging Approach |
|-------------|-------------------|
| Mobile phone AP (cost, thin) | Flip-chip + InFO FOWLP (Apple, Qualcomm) |
| AI accelerator (max bandwidth) | CoWoS-S + HBM3/HBM3E (NVIDIA, AMD) |
| Server CPU (max I/O, performance) | Flip-chip on organic substrate + chiplets |
| AMD 3D V-Cache (stacked SRAM) | Hybrid bonding (direct Cu-Cu) |
| Commodity MCU/analog | Wire bond (low cost, mature) |
| 3D NAND memory | Wafer-level monolithic 3D stacking (no TSV) |
| DRAM HBM | TSV through DRAM dies + TC bonding |
| Mixed-node chiplet system | UCIe interconnect on Si bridge or RDL interposer |

---

## Common Confusion Points

**"3D" in 3D V-Cache, 3D NAND, and 3D IC all mean different things**: AMD 3D V-Cache uses
hybrid bonding to attach SRAM chiplet on top of CPU die (chip-on-chip). 3D NAND grows flash
memory cells vertically on a single wafer (monolithic z-direction). HBM is a stack of DRAM dies
with TSVs. All involve vertical integration but via completely different mechanisms.

**Interposer is "2.5D", not 3D**: When dies sit side-by-side on an interposer (CoWoS), they're
horizontally arranged — the die faces up, the interposer is below. The "2.5D" label means you have
more connectivity than a flat substrate but less vertical integration than true 3D (stacked dies).

**Chiplets aren't just smaller dice**: Chiplets require designed interfaces (UCIe, AIB), known-good
die testing, and compatible packaging. You can't just saw an existing monolithic die into pieces.
Chiplet design starts at the architecture stage — what functions go on which die, what interconnect
standard, what target pitch.

**Hybrid bonding is a fab-class process, not assembly**: Achieving <0.5 nm surface roughness and
<200 nm alignment for hybrid bonding requires cleanroom conditions and precision tools similar
to wafer fab. It's not traditional "assembly house" work. TSMC and Samsung perform hybrid bonding
in their fabs, blurring the fab/package boundary.
