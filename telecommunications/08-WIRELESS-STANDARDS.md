# Wireless Standards — A Layered Guide

## The Big Picture

Short-range wireless standards cover the space from Bluetooth earbuds to LoRa covering
entire cities. Each standard occupies a distinct niche defined by range, power, and data rate.

```
WIRELESS STANDARDS LANDSCAPE
════════════════════════════════════════════════════════════════════

Data Rate
(Mbps)
│
10,000 ─   WiFi 7 (802.11be)
           ─────────────────────────────────●
 1,000 ─   WiFi 6E (802.11ax, 6 GHz)
           ──────────────────────────●
  100 ─    WiFi 5 (802.11ac/5G)
           ──────────────────────●
           Bluetooth BR/EDR 2-3 Mbps  ●
   10 ─    Zigbee (250 kbps) ●   UWB ●─
    1 ─
  0.1 ─    NFC 424 kbps ●
0.01 ─     LoRa 0.3-50 kbps ●
0.001 ─    NB-IoT ●
           │
           └─────────────────────────────────────────────────────►
           1 cm  10 cm  1 m   10 m  100 m  1 km  10 km  100 km
                                                     Range
```

---

## WiFi (802.11 Series)

```
WIFI GENERATION HISTORY

Gen    Standard  Year   Band        Max PHY   Key Innovation
───────────────────────────────────────────────────────────────────────
─      802.11    1997   2.4 GHz     2 Mbps    Original standard (FHSS/DSSS)
─      802.11b   1999   2.4 GHz     11 Mbps   CCK modulation, cheap chipsets
WiFi 1 802.11a   1999   5 GHz       54 Mbps   OFDM, 5 GHz, 8 channels
WiFi 2 802.11g   2003   2.4 GHz     54 Mbps   OFDM at 2.4 GHz, backward compat
WiFi 4 802.11n   2009   2.4/5 GHz   600 Mbps  MIMO (4×4), 40 MHz channels, beamforming
WiFi 5 802.11ac  2013   5 GHz       6.9 Gbps  256-QAM, 80/160 MHz channels, MU-MIMO DL
WiFi 6 802.11ax  2019   2.4/5 GHz   9.6 Gbps  OFDMA, MU-MIMO UL+DL, BSS coloring, TWT
WiFi 6E 802.11ax 2021   6 GHz       9.6 Gbps  6 GHz band (1.2 GHz new spectrum)
WiFi 7 802.11be  2024   2.4/5/6 GHz 46 Gbps   4096-QAM, 320 MHz, multi-link operation
───────────────────────────────────────────────────────────────────────

KEY INNOVATIONS:

802.11n / WiFi 4: MIMO
  Multiple spatial streams: 2×2, 3×3, 4×4 MIMO
  Uses multipath reflections as independent channels (just like LTE MIMO)
  40 MHz bonding: combines two 20 MHz channels → 2× throughput

802.11ac / WiFi 5:
  160 MHz channel (4× wider than 802.11n in 5 GHz)
  MU-MIMO downlink: AP serves 4 clients simultaneously (different beams)
  802.11ac Wave 2: 8 spatial streams for AP, up to 8 clients simultaneously

802.11ax / WiFi 6/6E:
  OFDMA: divide each channel into multiple resource units (RUs)
    → 9 to 74 simultaneous users per channel (vs. 1 at a time in earlier WiFi)
    → Key for dense environments (stadium, apartment building)
  Target Wake Time (TWT): IoT devices agree on wake schedule → battery savings
  BSS Coloring: spatial reuse by color-coding Basic Service Sets → fewer defer transmissions
  UL MU-MIMO: 8 clients can transmit simultaneously (vs DL-only in ac)

802.11be / WiFi 7:
  Multi-Link Operation (MLO): use multiple bands simultaneously per connection
  320 MHz channels: double WiFi 6 channel width
  4096-QAM: 12 bits/symbol (vs 10 in WiFi 6)
```

**WiFi channels**:
```
2.4 GHz CHANNELS (North America, 20 MHz wide):
  Channels 1-13, spacing 5 MHz
  Only 3 non-overlapping: 1, 6, 11 (each 22 MHz wide with rolloff)

5 GHz CHANNELS (20 MHz, non-overlapping, US):
  UNII-1: ch 36,40,44,48 (indoor low power)
  UNII-2A: ch 52,56,60,64 (DFS required, radar detection)
  UNII-2C: ch 100-144 (DFS required)
  UNII-3: ch 149-177 (outdoor ok)
  24 non-overlapping 20 MHz channels → bonded to 40/80/160 MHz

6 GHz CHANNELS (WiFi 6E):
  1.2 GHz of new spectrum in US (5.925-7.125 GHz)
  59 non-overlapping 20 MHz channels, 14× 80 MHz, 7× 160 MHz
  No DFS required, much less interference (legacy WiFi excluded)
```

---

## Bluetooth

```
BLUETOOTH VERSIONS

CLASSIC BLUETOOTH (BR/EDR):
  Frequency: 2.4 GHz ISM band
  Frequency hopping: 1600 hops/sec over 79 channels (spread spectrum anti-interference)
  Basic Rate (BR): 1 Mbps (GFSK)
  Enhanced Data Rate (EDR): 2 Mbps (π/4-DQPSK) or 3 Mbps (8DPSK)
  Range: ~10 m (Class 2, 2.5 mW) to ~100 m (Class 1, 100 mW)
  Use: audio (headphones, speakers), data transfer, serial port profile

BLUETOOTH LOW ENERGY (BLE / Bluetooth 4.0+):
  Frequency: 2.402-2.480 GHz, 40 channels, 2 MHz spacing
  Advertising channels: 3 (ch 37, 38, 39) → announce presence
  Data channels: 37 channels for connected data
  PHY options:
    LE 1M: 1 Mbps (original BLE)
    LE 2M: 2 Mbps (Bluetooth 5)
    LE Coded (125k / 500k bps): long range, up to 4× range (Bluetooth 5)
  Tx power: 0.01–100 mW, typical 1 mW
  Current in deep sleep: µA range → years on coin cell battery

BLUETOOTH VERSIONS:
  5.0 (2016): LE 2M, LE Coded, advertising extensions
  5.1 (2019): Direction finding (AoA/AoD) → cm-level indoor positioning
  5.2 (2020): LE Audio (LC3 codec), isochronous channels
  5.3 (2021): Power improvements, connection subrating
  5.4 (2023): Periodic Advertising with Responses (PAwR) for large-scale IoT

LE AUDIO (Bluetooth 5.2+):
  New codec: LC3 (Low Complexity Communication Codec) → better quality at lower bitrate than SBC
  Auracast broadcast audio: one source → unlimited BLE receivers (like FM radio but digital)
  Multi-stream: separate streams to each ear → better stereo sync, hearing aids
```

---

## Zigbee / Z-Wave / Matter

```
LOW-RATE WPAN (Wireless Personal Area Network)

ZIGBEE (IEEE 802.15.4):
  Frequency: 2.4 GHz (16 ch) or 868/915 MHz
  Data rate: 250 kbps (2.4 GHz)
  Range: 10-100 m (mesh extends further)
  Mesh networking: each node acts as router → self-healing network
  Power: sleep current ~µA → years on batteries
  Stack: Zigbee PRO, Zigbee 3.0 (unified profile)
  Use: smart home (lighting, sensors), industrial automation, medical monitors

Z-WAVE:
  Frequency: 900 MHz (US: 908.42 MHz, EU: 868.42 MHz)
  Rate: 9.6 / 40 / 100 kbps
  Range: 30 m indoor, 100 m outdoor
  Always uses mesh
  Max network: 232 devices per controller
  Advantage: operates at 900 MHz → less congested than 2.4 GHz (no WiFi/BT interference)
  Certification: stricter interoperability than Zigbee
  Use: smart home security, thermostats, door locks

MATTER (formerly CHIP — 2022):
  Application-layer protocol, not a radio protocol
  Runs over: WiFi, Thread (802.15.4 based), Ethernet
  Backed by: Apple, Google, Amazon, Samsung, chip vendors
  Goal: unified smart home standard across ecosystems
  Apple HomeKit, Google Home, Amazon Alexa — all Matter-compatible
  Thread: low-power IPv6 mesh (similar to Zigbee PHY but IP stack)
```

---

## LoRa / LoRaWAN

```
LORA / LORAWAN — Low Power Wide Area Network (LPWAN)

LORA (Long Range):
  Physical layer: Chirp Spread Spectrum (CSS) modulation
  Frequency: 433/868/915 MHz (regional specific)
  Data rate: 0.3–50 kbps (depends on spreading factor)
  Range: 5–15 km urban, 15–45 km rural, 100+ km LoS
  Sensitivity: -137 dBm → enables very long range

SPREADING FACTOR (SF):
  SF7-SF12: trade-off between range and data rate
  SF7: 5 kbps, shorter range
  SF12: 0.3 kbps, maximum range, >1000x SF7 signal capture
  Different SFs are orthogonal (can coexist in same channel)

LORAWAN (Network Protocol):
  End device → LoRa gateway → LoRaWAN Network Server → Application Server
  Class A (default): end device initiates, 2 receive windows after each uplink
  Class B: scheduled receive windows (lower latency downlink)
  Class C: always listening (highest latency, highest power)

CAPACITY:
  Each SF/channel combination: duty cycle limited (0.1-1% in Europe per ETSI)
  Gateway: 8-16 channels simultaneously; can serve 1000s of devices
  Scalable: multiple gateways for coverage, network server deduplicates

USE CASES:
  Smart metering (water, gas, electricity) — monthly read interval fine
  Environmental sensors (weather, air quality)
  Asset tracking (slow-moving: pallets, bikes)
  Smart agriculture (soil moisture, livestock tracking)
  Building automation
```

---

## NFC and RFID

```
NFC (Near Field Communication):
  Frequency: 13.56 MHz (ISM)
  Range: <4 cm (magnetic induction, not propagating wave)
  Rates: 106, 212, 424 kbps
  Modes:
    Reader/Writer: phone reads/writes NFC tag
    Peer-to-peer: two NFC devices exchange data
    Card emulation: phone emulates credit card, transit card (Apple Pay, Google Pay)
  Standards: ISO 14443 (contactless card), ISO 18092 (NFC), ISO 15693 (vicinity)
  Security: NFC inherently short-range → reduces eavesdropping risk; payment secured by EMV

RFID VARIANTS:
  LF (125-134 kHz): 1-3 cm range, animal ID, old access cards
  HF (13.56 MHz): NFC range, smart cards, library books (NFC is a subset)
  UHF (860-960 MHz): 1-10 m range, warehouse logistics, retail inventory
    EPC Gen 2 (ISO 18000-6C): global standard, billions of tags shipped
    100s of reads/sec, simultaneous (anti-collision)
  SHF (2.45/5.8 GHz): vehicle tolling, personnel access
    EZ-Pass: 5.8 GHz, 915 MHz backup, read at 100+ mph
    Passive tags get power from reader field; active tags have batteries
```

---

## Decision Cheat Sheet

| Application | Standard | Why |
|-------------|----------|-----|
| Home WiFi (modern) | WiFi 6E (802.11ax 6 GHz) | Clean spectrum, OFDMA |
| Dense deployment (office, stadium) | WiFi 6 with OFDMA | Concurrent users |
| Audio headphones / speakers | Bluetooth BR/EDR or LE Audio | Established ecosystem |
| IoT sensor, coin cell power | BLE or Zigbee | µA sleep current |
| Smart home ecosystem | Matter over Thread/WiFi | Interoperability |
| Wide-area IoT (city scale) | LoRaWAN | km-range, free spectrum |
| Cellular IoT (reliable, wide coverage) | NB-IoT or LTE-M (Cat-M1) | Cellular reliability |
| Contactless payment / transit | NFC (ISO 14443) | Secure, universal |
| Warehouse inventory | UHF RFID (EPC Gen 2) | Bulk reading at distance |

---

## Common Confusion Points

**Zigbee and Z-Wave are not compatible**: Both are mesh IoT protocols for smart home but use
different radio frequencies and protocols. A Zigbee hub cannot talk to Z-Wave devices natively.
Matter aims to fix this at the application layer but requires new or updated devices.

**BLE is not "Bluetooth but slower"**: BLE and Classic Bluetooth are almost completely different
protocols that share the 2.4 GHz band. BR/EDR is optimized for streaming audio; BLE is optimized
for bursty low-power sensor data and advertisements. Most modern phones support both simultaneously.

**WiFi speed ratings are theoretical maximums**: "WiFi 6: 9.6 Gbps" requires 8×8 MU-MIMO, 160 MHz
channel, 1024-QAM, zero interference. Real-world throughput: 1-3 Gbps under ideal conditions,
200-800 Mbps in typical home use. Half of the theoretical maximum is a reasonable expectation.

**LoRa duty cycle limits capacity significantly**: In Europe, ETSI limits ISM band transmitters
to 0.1-1% duty cycle. A device sending one 10-byte packet per hour uses ~0.003% duty cycle —
fine. A device sending 10 packets per minute uses 30% duty cycle — not compliant. LoRaWAN
networks may throttle devices that violate duty cycle rules.
