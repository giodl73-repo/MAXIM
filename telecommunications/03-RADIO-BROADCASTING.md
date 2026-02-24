# Radio Broadcasting — A Layered Guide

## The Big Picture

Radio broadcasting converts information to EM waves and propagates them through space.
The antenna is the critical interface between circuit and wave; the link budget quantifies
the complete power budget from transmitter to receiver.

```
RADIO LINK COMPLETE PICTURE
════════════════════════════════════════════════════════════════════

Transmitter         Transmission    Antenna     Free Space        Rx Antenna
   │                   Line         (Tx)          Path            (Rx)    Receiver
   │                      │           │              │               │        │
[Power     ──► [Coax/   ──► [Dipole/ ──► [FSPL +  ──► [Dipole/ ──►  [LNA + ─► [Demod]
 Amp]           Waveguide]   Yagi/     atm. loss    Yagi/           Filter]
                             Parabolic + fading +   Parabolic]
                             dish]     multipath]
   │               │           │              │               │
   Pt            cable loss   Gt           path loss          Gr
  (dBm)          (dB)         (dBi)          (dB)           (dBi)

Received power: Pr = Pt + Gt - cable_loss - L_path + Gr  (all in dB)
```

---

## Antenna Fundamentals

An antenna is a transducer that converts between guided waves (transmission line) and
free-space electromagnetic waves. All antennas are reciprocal — same gain for transmit and receive.

```
DIPOLE ANTENNA (half-wave λ/2):

         │ Current maximum at center
─────────┼─────────────────────────
         │ Length = λ/2
─────────┼─────────────────────────
         │ End: current minimum

Radiation pattern (donut shape):
         Top view:    circular (omnidirectional in horizontal plane)
         Side view:   figure-8 (null at tips of dipole)

Gain: 2.15 dBi (slightly more than isotropic, concentrated in horizontal plane)
Feed impedance: ~73 Ω resistive (matched to 75 Ω coax)
```

**Key antenna parameters**:

```
ANTENNA PARAMETERS

Gain G (dBi): Power density at best direction / isotropic average
  G = η · D
  η = radiation efficiency (loss in antenna)
  D = directivity (purely geometric focusing)

Effective Aperture Ae:
  Ae = G · λ²/(4π)   (m²)
  Received power: Pr = S · Ae  where S = incident power density (W/m²)

Beamwidth (HPBW — half-power beamwidth, -3 dB):
  High-gain antenna: narrow beam
  Approximate: HPBW ≈ 70λ/D degrees  (D = aperture diameter)
  Parabolic dish 1 m dia at 12 GHz: HPBW ≈ 70×0.025/1 = 1.75°

Bandwidth: frequency range where VSWR < 2:1 (or gain > peak - 3 dB)
  Dipole: ~10-15% bandwidth
  Log-periodic: broadband (decades of frequency)
  Parabolic dish: broadband (limited by feed horn)

Polarization: orientation of E-field oscillation
  Linear: vertical (V) or horizontal (H) — most terrestrial
  Circular: RHCP or LHCP — satellite, GPS
  Cross-pol isolation: how much of orthogonal polarization is rejected (30+ dB typical)
```

---

## Common Antenna Types

```
ANTENNA TYPES AND APPLICATIONS

Half-wave dipole (λ/2):        2.15 dBi  Broadband reference standard
Folded dipole:                  2.15 dBi  TV antenna input, higher impedance
Ground plane monopole (λ/4):    ~5 dBi   Mobile radios, car antenna
Yagi-Uda array:
  3 elements (reflector+dipole+director): ~7 dBi  TV antennas
  10 elements:                           ~12 dBi  Long-range UHF
  16 elements:                           ~15 dBi  Amateur radio DX
Log-periodic:                   5-11 dBi  Broadband (HF-UHF), scanner antennas
Helix (axial mode):             12-15 dBi Satellite circular polarization, GPS
Patch/microstrip:               5-8 dBi   Mobile phones, WiFi, GPS (flat, low profile)
Parabolic reflector:
  0.3 m at 10 GHz:              ~35 dBi   Point-to-point microwave
  1 m at 12 GHz:                ~40 dBi   VSAT terminals
  3 m at 12 GHz:                ~50 dBi   Large satellite earth station
Phase-array (steerable):        20-40+ dBi Radar, 5G massive MIMO, AESA
```

---

## AM/FM/Shortwave Broadcasting

```
AM BROADCASTING (Medium Wave, 530-1700 kHz):

Standard: ITU Region 1 (Europe/Africa): 9 kHz spacing
          ITU Region 2 (Americas): 10 kHz spacing
Transmit power: 5 kW (local) to 500 kW (clear channel, night)
Modulation: DSB-AM with full carrier (simple receivers)
Coverage:
  Daytime: ground wave ~200-400 km radius
  Nighttime: D layer disappears → F layer reflection → 1000+ km
  "Clear channel" stations: 50 kW, protected frequency, 1000+ km range

FM BROADCASTING (87.5-108 MHz):
Standard: channel spacing 200 kHz (EU), 100 kHz (US)
Transmit power: 0.1 W (local) to 50+ kW ERP (regional)
Modulation: Stereo multiplex (pilot 19 kHz, stereo diff 23-53 kHz, RDS 57 kHz)
  Left/right channels: (L+R) at baseband + (L-R) DSB-SC at 38 kHz carrier
  Receiver demodulates both, recovers L and R
Coverage: LoS + diffraction, typically 30-100 km radius
Audio bandwidth: 30 Hz – 15 kHz (broadcast quality)

DIGITAL RADIO:
HD Radio (USA): in-band on-channel (IBOC) — digital signal alongside analog
DAB/DAB+ (Europe): dedicated digital bands (174-240 MHz), OFDM, AAC+ codec
Digital Audio Broadcasting gives CD-quality audio, additional data services
```

---

## Propagation Models

Empirical models predict path loss in real environments beyond FSPL.

```
OKUMURA-HATA MODEL (urban macrocell, 150-1500 MHz):

L_u = 69.55 + 26.16·log(f) - 13.82·log(h_b) - a(h_m) + (44.9 - 6.55·log(h_b))·log(d)

f = frequency (MHz), h_b = base station height (m), h_m = mobile height (m), d = distance (km)
a(h_m) = mobile antenna correction factor

Large city (f > 300 MHz): a(h_m) = 3.2·(log(11.75·h_m))² - 4.97  dB

EXAMPLE: f=900MHz, h_b=30m, h_m=1.5m, d=3km, large city:
L_u ≈ 69.55 + 26.16×2.954 - 13.82×1.477 - 3.2 + 35.29×0.477 ≈ 130 dB
(FSPL alone would be ~104 dB — extra 26 dB from buildings/terrain)

COST 231 HATA (1800-2000 MHz): extends Okumura-Hata

INDOOR PROPAGATION MODELS:
Multi-wall model: L = FSPL + n_walls · L_wall + n_floors · L_floor
L_wall ≈ 3-15 dB (interior wall: 3 dB; exterior wall: 10-15 dB)
L_floor ≈ 15-25 dB per floor

RAY TRACING: More accurate but computationally expensive. Uses 3D geometry databases.
Used for: indoor planning, campus environments, 5G dense deployment.
```

---

## Link Budget Example (FM Broadcasting)

```
FM BROADCASTING LINK BUDGET

Transmitter:
  Transmit power:          +77 dBm  (50 kW)
  TX line + combiner loss:  -3 dB
  TX antenna gain (3×λ/2):  +8 dBi
  ──────────────────────────────────
  Effective Radiated Power: +82 dBm (ERP = 158 kW equivalent)

Path:
  FSPL at 100 MHz, 30 km: -104 dB
  Ground clutter:           -10 dB
  ──────────────────────────
  Total path loss:          -114 dB

Receiver:
  Rx antenna (simple dipole): +2 dBi
  ──────────────────────────────────
  Received power: 82 - 114 + 2 = -30 dBm

Threshold:
  FM receiver threshold: -100 dBm (20 dB SINAD)
  ──────────────────────────────────
  Link margin: -30 - (-100) = +70 dB  (plenty!)

FM has huge excess margin — that's why portable radios work in cars and buildings.
```

---

## Decision Cheat Sheet

| Need | Antenna Choice |
|------|---------------|
| Broadcast (omnidirectional) | Vertical monopole (1/4λ) or stacked dipoles |
| TV reception (outdoor) | Yagi-Uda (directional, fixed-aim at tower) |
| Point-to-point microwave | Parabolic dish (high gain, narrow beam) |
| Mobile phone | Patch/PIFA (compact, on-body) |
| WiFi AP | Omnidirectional vertical dipole or patch array |
| Satellite receive (fixed) | Parabolic dish sized for link budget |
| Wideband spectrum scan | Log-periodic (decades of bandwidth) |
| 5G base station (massive MIMO) | Phased array panel (64-192 elements) |

---

## Common Confusion Points

**ERP vs EIRP**: Effective Radiated Power (ERP) is relative to a half-wave dipole.
EIRP (Effective Isotropic Radiated Power) is relative to isotropic. EIRP = ERP + 2.15 dB.
Regulators sometimes specify in ERP, sometimes EIRP. Always check the reference.

**Antenna gain doesn't create power**: A high-gain antenna focuses the transmitted power
into a narrower beam. Total radiated power is the same; it's just concentrated directionally.
You gain in the beam direction at the expense of other directions.

**"dBd" vs "dBi" on product specs**: Consumer antennas often quote dBd (gain vs dipole),
which adds 2.15 dB to make the number look smaller. A "5 dBd" antenna = 7.15 dBi.
Watch for this in WiFi and amateur radio antenna specs.

**FM 50 dBuV threshold**: The standard FM threshold is expressed in microvolts at the antenna
terminals into 75 Ω. Convert: V = 50 dBuV = 316 µV. Power = V²/R = (316e-6)²/75 = 1.3×10⁻⁹ W = -88.9 dBm.
So the FM threshold of ~-89 dBm is consistent with your link budget.
