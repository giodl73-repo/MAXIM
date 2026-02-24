# Satellite Communications — A Layered Guide

## The Big Picture

Satellites provide coverage where terrestrial networks can't reach, and global connectivity
at scale. The orbit determines the fundamental trade-offs.

```
SATELLITE ORBIT COMPARISON
════════════════════════════════════════════════════════════════════

                           GEO
                        ●─────────────────────────────────────
                        │ 35,786 km altitude (Clarke orbit)
                        │ ~500 ms round-trip latency
                        │ 3 satellites cover most of Earth
                        │ Fixed position relative to Earth
                        │ High FSPL (~200 dB at Ku-band)
                        │

              MEO ─────────────────────────────────────────────
                   2,000–20,000 km altitude
                   20–200 ms latency
                   GPS (20,200 km), Galileo, O3b (8,000 km)

     LEO ─────────────────────────────────────────────────────
          160–2,000 km altitude
          ~20–40 ms latency (Starlink: 20-40 ms)
          Lower FSPL (~180 dB) but need many satellites
          Starlink: 1,584 (Phase 1) → 12,000+ planned

EARTH

                        ←──── EARTH'S RADIUS = 6,371 km ────►
```

---

## GEO Satellites

```
GEO (Geostationary Orbit) DETAILS:

PHYSICS: Orbital period = Earth's rotation period = 23h 56m 4s (sidereal day)
         Altitude = 35,786 km above equator
         Velocity: 3.07 km/s

Coverage: One GEO satellite sees ~42% of Earth's surface.
          Three GEOs at 120° spacing: near-global coverage (except poles > ~75°).

KEY SERVICES:
  Direct-to-home (DTH) TV: DirecTV, DISH, BSkyB, Astra
  VSAT (Very Small Aperture Terminal): enterprise data, oil platforms, ships
  Weather satellites: GOES (US), Meteosat (EU), Himawari (Japan)
  Fixed Satellite Service (FSS): broadcast contribution feeds, international telephony

FREQUENCY BANDS FOR GEO:
  C-band (4/6 GHz): 3.7-4.2 GHz down, 5.925-6.425 GHz up
    Robust to rain, widely deployed, 500 MHz bandwidth
  Ku-band (11-14 GHz): 10.7-12.75 GHz down, 14-14.5 GHz up
    Higher bandwidth, smaller dishes (0.6-1.2 m), dominant for DTH
  Ka-band (26.5-40 GHz): consumer broadband (HughesNet, ViaSat)
    High bandwidth (500 MHz+), small dish, but significant rain fade

HIGH THROUGHPUT SATELLITES (HTS):
  Traditional GEO: 1-5 Gbps total capacity
  HTS (ViaSat-3, Hughes Jupiter-3): 100-1000 Gbps via spot beam reuse
  Uses many narrow spot beams → high frequency reuse (each beam = new spectrum allocation)
```

---

## LEO Constellation: Starlink

```
STARLINK ARCHITECTURE

SpaceX Starlink: largest commercial satellite constellation

PHASE 1: 1,584 satellites, 550 km altitude, 72 orbital planes × 22 satellites
PHASE 2: Additional shells at different inclinations and altitudes (12,000 planned, 42,000 filed)

TERMINAL (user):
  "Dishy" — flat-panel phased array antenna
  500-600 mm flat dish
  Electronically steers beam → tracks moving satellites
  No mechanical pointing required

LINK:
  Ku-band downlink (10.7–12.75 GHz)
  Ka-band uplink (17.8–18.6 GHz)
  Between satellites: inter-satellite links (ISL) via laser (v2 satellites)
    → Routes packets via ISL, bypasses terrestrial internet backbone

LATENCY: 20–40 ms (vs 500 ms GEO)
  Orbital period: ~90 min → handover to new satellite every ~90 seconds
  Phased array tracks seamlessly

CAPACITY: ~100 Mbps per beam (shared among users in beam)
          Typical user: 50–200 Mbps downlink, 10–30 Mbps uplink

APPLICATIONS:
  Rural/maritime/aviation broadband
  Enterprise backup links
  Government/emergency services
  Aviation (in-flight WiFi replacing GEO VSAT Ku-band)
```

---

## GPS as Telecom Infrastructure

GPS is as critical to modern telecommunications as fiber or cellular towers.

```
GPS (NAVSTAR GPS)

CONSTELLATION: 30 satellites, 6 orbital planes, 20,200 km altitude (MEO)
  At any location: 4-12 satellites visible simultaneously (need min 4 for 3D fix)
  Orbital period: 12 hours

SIGNAL:
  L1 (1575.42 MHz): civilian C/A code + P(Y) code
  L2 (1227.6 MHz): P(Y) code only → now L2C for civilian
  L5 (1176.45 MHz): higher power, civil aviation

RANGING (pseudoranging):
  Each satellite broadcasts precise timing signal and ephemeris (position data)
  Receiver measures time of arrival → range = c × (tₐᵣᵣᵢᵥₐₗ - tₜₓ)
  4 unknowns: x, y, z, receiver clock error → need 4 satellites
  Accuracy: civilian ~2-5 m; military P(Y) code: ~0.3 m

TIMING PRECISION:
  GPS is a global, free, open timing infrastructure
  Each satellite has atomic clock (Cs or Rb), maintained to ~100 ns accuracy
  Telecom uses: 4G/5G base station synchronization (timing-critical MIMO coordination)
  Financial markets: high-frequency trading timestamps, audit trails
  Power grid: phasor measurement units (PMUs) sync'd to GPS
  Internet: NTP servers (stratum 1) reference GPS

GNSS (Global Navigation Satellite System): umbrella term
  GPS (USA) + GLONASS (Russia) + Galileo (EU) + BeiDou (China) + IRNSS (India) + QZSS (Japan)
  Multi-GNSS receiver: 40+ satellites → much better accuracy, reliability, availability
```

---

## Satellite Link Budget Example

```
VSAT (Ku-BAND SATELLITE) LINK BUDGET

Uplink (terminal to satellite):
  Terminal EIRP: +57 dBW  (1.8 m dish, 2 W amp, Gt ≈ 44 dBi)
  Free-space path loss (14 GHz, 36,000 km): -207 dB
  Pointing loss + margin: -1 dB
  ────────────────────────────────────
  Power at satellite input: -151 dBW

  Satellite receive G/T = 0 dB/K  (older satellite)
  Noise in receiver: kTB = -228.6 + 10·log(T) + 10·log(B)
  For T=350K, B=36 MHz: noise = -228.6 + 25.4 + 75.6 = -127.6 dBW
  Uplink C/N = -151 - (-127.6) = -23.4 dB  (from satellite perspective)

This analysis shows you need to trade off dish size, transmit power, and EIRP.
VSAT with 0.6 m dish is marginal; 1.8 m works well.

EFFECTIVE ISOTROPIC RADIATED POWER (EIRP):
  EIRP = Pt + Gt - cable_loss   (dBW or dBm)
  This is the key figure for satellite transmitter performance.
```

---

## VSAT Networks

```
VSAT TOPOLOGY

HUB (Master):                        REMOTE (VSAT terminal):
Large dish (3-9 m)                   Small dish (0.6-2.4 m)
High-power amplifier                 Low-power (2-16 W)
Manages the network                  Remote site (ship, store, office)
                │                              │
                │         Satellite            │
                └──────────────●───────────────┘
                              GEO

TOPOLOGIES:
1. Star (most common): remote → hub via satellite → hub → remote (double hop)
   Latency: 2 × 500ms + processing = ~1.1 s (unacceptable for real-time voice)
   Used for: data, slow SCADA, credit card terminals, backup internet

2. Mesh: remote ↔ remote directly (single hop via satellite)
   Latency: 500 ms (acceptable for voice if echo cancelled)
   Used for: rural telephony, remote area telephony

ACCESS SCHEMES:
  FDMA: each remote gets dedicated frequency slot (efficient, no contention)
  TDMA: remotes share time slots, hub assigns on demand
  DAMA (demand assigned MA): slots assigned based on traffic demand
  MF-TDMA: modern standard, flexible, bandwidth on demand
```

---

## Decision Cheat Sheet

| Requirement | Orbit/Technology |
|-------------|-----------------|
| Global TV/radio broadcast | GEO (1 satellite, wide beam) |
| Low-latency broadband (rural) | Starlink LEO (20-40 ms) |
| Maritime/aviation broadband | Starlink or HTS Ku/Ka GEO |
| Remote site enterprise backup link | VSAT (GEO, C or Ku band) |
| Global precise timing reference | GPS / GNSS |
| Navigation positioning | Multi-GNSS (GPS+Galileo+BeiDou) |
| Geostationary weather imagery | GEO (fixed, continuous view) |
| High-capacity broadband (HTS) | ViaSat / Hughes HTS with spot beams |

---

## Common Confusion Points

**GEO altitude is not arbitrary**: 35,786 km is the specific altitude where orbital period equals
Earth's rotational period. This is derived from Kepler's third law: T² ∝ r³. Any different altitude
gives a different period and the satellite drifts east or west relative to Earth.

**Starlink latency advantage is real but context-dependent**: LEO Starlink is 20-40 ms
round-trip. GEO is ~500 ms. For web browsing, the difference is noticeable. For streaming video,
both are fine (video buffering). For gaming, Starlink is competitive with cable; GEO is not.

**GPS works on signals from satellites, not vice versa**: GPS is receive-only. Your phone never
transmits to GPS satellites. The satellites just broadcast timing signals; you measure arrival times.
Your location is computed locally on your device (or by a server you upload data to).

**Ku-band and Ka-band are different satellite bands**: Ku = ~12-18 GHz; Ka = ~26-40 GHz.
Ka has more bandwidth but more rain fade. Consumer satellite broadband (HughesNet, Starlink) has
been moving to Ka for more capacity. Ku is still widely used for direct-to-home TV.
