# Radio Physics: EM Spectrum, Propagation Modes, AM/FM Modulation, Antenna Theory

## The Big Picture

Radio is applied electromagnetism. Maxwell's equations predict that oscillating electrical currents radiate energy as electromagnetic waves. Antenna theory determines how efficiently energy is radiated and in which directions. Modulation theory determines how information is encoded onto a carrier wave. The physics is continuous with digital communications — QAM and OFDM are just more efficient ways to solve the same problem.

```
ELECTROMAGNETIC SPECTRUM (Radio Relevant Portion)

Frequency    | Wavelength | Band Name  | Uses
-------------+------------+------------+-------------------------
3 Hz - 30 Hz | 100,000 km | ELF        | Submarine communications
30-300 Hz    | 10,000 km  | SLF        | Submarine comms
300-3000 Hz  | 1,000 km   | ULF        | Mines, earthquakes
3-30 kHz     | 100 km     | VLF        | Navigation (LORAN)
30-300 kHz   | 10 km      | LF         | AM radio (Europe/Asia), navigation
300-3000 kHz | 1 km       | MF         | AM radio (US/world), maritime
3-30 MHz     | 100 m      | HF         | Shortwave, amateur, aviation
30-300 MHz   | 10 m       | VHF        | FM radio, TV (ch 2-13), aviation
300-3000 MHz | 1 m        | UHF        | TV (ch 14+), mobile, WiFi 2.4G
3-30 GHz     | 10 cm      | SHF        | Microwave, WiFi 5G, satellite
30-300 GHz   | 1 cm       | EHF        | 5G mmWave, radar
300+ GHz     | < 1 mm     | Terahertz  | Imaging, research

KEY RELATIONSHIPS:
  v = λ × f        (wave speed = wavelength × frequency)
  c = 3×10^8 m/s   (speed of light = speed of EM waves in vacuum)
  λ = c/f          (wavelength = speed of light / frequency)

  1 MHz = 10^6 Hz; FM radio 100 MHz -> λ = 3m
  1 GHz = 10^9 Hz; WiFi 2.4 GHz -> λ = 12.5 cm
```

---

## Radio Wave Propagation Modes

Different frequency bands propagate differently. This is physics, not policy, and it determines what frequencies are useful for which applications.

```
THREE PROPAGATION MODES

1. GROUND WAVE (surface wave)
   Frequency: LF/MF/lower HF (<3 MHz)
   Mechanism: wave travels along Earth's surface
              Earth surface = conductor; wave "guided" along it
   Range: hundreds to thousands of km (low frequencies)
   Reliability: very stable; day/night variation small
   Affected by: terrain, ground conductivity
   Use: AM broadcast, maritime, naval

   [Transmitter] ~~wave follows Earth's curve~~ [Receiver]
   Useful: when you want coverage over horizon (ground wave bends)

2. SKY WAVE (ionospheric propagation)
   Frequency: HF (3-30 MHz), some MF at night
   Mechanism: wave travels up, reflects off ionosphere, returns
   Ionosphere: layers of ionized gases (D, E, F layers) 70-400 km up
   Day vs night: ionosphere changes (F layer dominant at night)
   Range: 1,000-15,000 km per hop; multiple hops = global
   Reliability: variable; depends on solar activity, time of day

   [Transmitter] up wave ~~reflects from ionosphere~~ down [Receiver]
   |------- skip zone (no coverage) --------|

   SKIP ZONE: area between end of ground wave coverage and where
              sky wave returns = no signal from this transmitter
   Use: shortwave broadcasting, amateur radio, military
   Solar maximum: enhanced ionosphere = better/longer skip
   Solar storms: can disrupt or eliminate sky wave (blackouts)

3. LINE-OF-SIGHT (direct wave / space wave)
   Frequency: VHF and above (>30 MHz)
   Mechanism: travels directly from transmitter to receiver
              No ground follow, no ionospheric reflection
              Bends slightly with Earth's atmosphere (tropospheric refraction)
   Range: limited to visual horizon (+ ~15-30% for refraction)
   Height formula: range = ~4.12 * sqrt(h_meters) km
                   TV tower at 300m: ~71 km range
   Reliability: very stable (no ionospheric variation)
   Use: FM radio, TV, microwave links, WiFi, mobile phones

   [High Tower] straight line of sight [Receiver within horizon]

   WHY TV IS VHF/UHF (not AM frequencies):
   TV requires wide bandwidth (4-6 MHz per channel)
   Wide bandwidth requires high frequencies (BW << carrier frequency)
   AM frequencies can't support TV bandwidth
   VHF/UHF: plenty of bandwidth but LOS only -> towers needed
```

---

## AM Modulation

```
AMPLITUDE MODULATION (AM)

CARRIER WAVE:
  Sinusoidal wave at carrier frequency (e.g., 1000 kHz)
  Amplitude: constant A_c
  Signal: A_c × sin(2π × f_c × t)

MODULATION:
  Audio signal (message): m(t) — varies with sound
  AM signal: [A_c + m(t)] × sin(2π × f_c × t)
  The audio signal varies the AMPLITUDE of the carrier

  VISUAL:
  No modulation:
  ~~~~~~~~~~~~~~~~~~~  (constant amplitude)

  With AM audio:
  ~~~^~~~^~~~  (amplitude varies with sound)
    \_/ \_/
  Envelope of amplitude = audio waveform

BANDWIDTH:
  Message bandwidth: 0-5 kHz (AM broadcast audio quality)
  AM signal bandwidth: 2 × message BW = 10 kHz
  US AM channel spacing: 10 kHz
  AM channel: 540 kHz to 1700 kHz (MW band)
  Number of channels: 116 channels (540-1700 kHz at 10 kHz spacing)

DEMODULATION:
  Envelope detector: simple, cheap
    Diode + capacitor + resistor
    Charges to peak, slowly discharges -> follows envelope
    The envelope IS the audio signal
  Easy to implement: AM receivers are cheap

NOISE SUSCEPTIBILITY:
  Electrical noise (lightning, motors, power lines): varies amplitude
  AM signal: also varies amplitude
  Detector: cannot distinguish noise from signal
  Result: AM = susceptible to amplitude noise
  "Static" on AM radio = electrical noise
  Day/night: AM range extends at night (sky wave) with more interference

MODULATION INDEX m:
  m = A_m / A_c (audio amplitude / carrier amplitude)
  m < 1: proper modulation
  m = 1: 100% modulation (maximum without distortion)
  m > 1: overmodulation -> severe distortion, splatter into adjacent channels
  Broadcast: m ≈ 0.9 typical (near maximum, avoid clipping)
```

---

## FM Modulation

```
FREQUENCY MODULATION (FM)

CONCEPT: Audio signal varies the FREQUENCY of the carrier,
         not the amplitude.

FM signal: A_c × sin(2π × [f_c + k_f × m(t)] × t)
  f_c: center frequency (carrier)
  k_f: frequency sensitivity constant
  m(t): audio message signal
  Instantaneous frequency: f_c + k_f × m(t)
  Amplitude: CONSTANT (A_c unchanged)

VISUAL:
  No modulation:
  ~~~~~~~~~~~~~~~  (uniform frequency)

  With FM audio:
  ~~~~ ~~ ~~~~~~   (frequency varies with sound)
  (spaces vary, amplitude constant)

BANDWIDTH (FM):
  Carson's rule: BW ≈ 2(Δf + f_max)
  Δf: max frequency deviation (FM broadcast: ±75 kHz)
  f_max: max audio frequency (FM broadcast: 15 kHz)
  BW = 2(75 + 15) = 180 kHz ≈ 200 kHz
  US FM channel spacing: 200 kHz
  FM band: 87.8 - 108.0 MHz (VHF band II)
  Number of FM channels: ~100 channels

NOISE ADVANTAGE:
  Amplitude noise: doesn't affect frequency -> doesn't distort signal
  FM limiter: explicitly removes amplitude variations before detection
  Result: FM has much better SNR than AM at same signal strength
  "Capture effect": stronger FM signal completely captures receiver
                    (two signals on same frequency: stronger wins cleanly)
  AM equivalent: both signals heard, mixed, annoying

FM DEVIATION AND QUALITY:
  More frequency deviation = more bandwidth = better audio quality
  Narrow-band FM (NBFM): ±2.5-5 kHz deviation
    Used: two-way radio, public safety
    Bandwidth: ~10-12.5 kHz per channel
    Audio: communication quality (voice, not music)
  Wide-band FM (WBFM): ±75 kHz deviation
    Used: FM broadcast radio
    Bandwidth: 200 kHz per channel
    Audio: high fidelity (20 Hz - 15 kHz)

FM STEREO (1961):
  Problem: add stereo to FM while remaining compatible with mono receivers
  Solution: pilot tone + difference signal multiplexing

  Stereo encoding:
  L+R: sum signal (mono, 50-15,000 Hz) -> mono receivers hear this
  L-R: difference signal at 23-53 kHz (double-sideband AM)
  38 kHz subcarrier: L-R modulated onto this
  19 kHz pilot tone: receiver detects, locks phase, regenerates 38 kHz

  Decoding:
  Mono: use L+R signal directly
  Stereo: use L+R and L-R to recover L = (L+R + L-R)/2, R = (L+R - L-R)/2
```

---

## Digital Radio Modulation (Bridge to Telecommunications)

```
DIGITAL MODULATION: RADIO IS JUST A CARRIER

Analog: vary amplitude OR frequency to encode audio
Digital: vary amplitude AND frequency AND phase to encode bits
Key difference: digital maps discrete symbol constellations

QAM (Quadrature Amplitude Modulation):
  Used in: cable TV, DSL, WiFi, LTE, cable modem
  Encode bits in both amplitude AND phase simultaneously
  QAM-16: 4 amplitude levels × 4 phase angles = 16 states = 4 bits/symbol
  QAM-64: 64 states = 6 bits/symbol
  QAM-256: 256 states = 8 bits/symbol

  Trade-off: higher QAM = more bits/Hz BUT requires better SNR
  WiFi 6 (802.11ax): QAM-1024 (10 bits/symbol) -- needs excellent signal

OFDM (Orthogonal Frequency Division Multiplexing):
  Used in: WiFi (802.11a/g/n/ac/ax), LTE, 5G NR, DVB-T, ATSC 3.0
  Divide channel into many narrow sub-carriers (e.g., 52 sub-carriers in WiFi)
  Each sub-carrier: modulated independently (QAM)
  "Orthogonal": sub-carriers don't interfere with each other
  Benefit: resistance to multipath fading (each narrow sub-carrier flat)
  Benefit: can skip sub-carriers with interference (dynamic spectrum use)

  AM/FM radio:  one carrier, analog modulation
  OFDM:         hundreds of carriers, digital QAM each
  Same spectrum; massively more information capacity

SHANNON CAPACITY AGAIN:
  C = B × log2(1 + S/N)
  AM radio (10 kHz channel, SNR 30 dB):
    C = 10,000 × log2(1001) ≈ 100 kbps theoretical
    Actual AM audio: ~10-30 kbps compressed
  FM radio (200 kHz channel, SNR 40 dB):
    C = 200,000 × log2(10001) ≈ 2.6 Mbps theoretical
    Actual FM: uncompressed 16-bit 44.1kHz stereo = 1.41 Mbps
  Digital broadcast (6 MHz TV channel, ATSC 3.0):
    C = 6,000,000 × log2(1 + SNR) >> analog NTSC
    ATSC 3.0: 25-35 Mbps in 6 MHz = HD video + surround audio
```

---

## Antenna Theory

```
ANTENNA FUNDAMENTALS

BASIC PRINCIPLE:
  Antenna = transducer: converts electrical signals to EM waves (TX)
            or EM waves to electrical signals (RX)
  Transmit/receive reciprocal: antenna gain pattern = same both ways

DIPOLE ANTENNA (reference):
  Half-wave dipole: two conductors, each λ/4 long
  Total length: λ/2
  FM dipole: 100 MHz -> λ = 3m -> dipole = 1.5m
  AM dipole: 1 MHz -> λ = 300m -> dipole = 150m (impractical)
  AM stations: use vertical monopoles (electrically equivalent to dipole)

  Dipole radiation pattern (side view):
     |
     ↑  (feed at center)
     |
  Pattern: donut shape around vertical axis
           radiates in all horizontal directions equally
           no radiation directly up/down

  Gain: 2.15 dBi (slightly above isotropic)
  Directional reference: isotropic = equal in all directions (theoretical)

AM BROADCAST TOWER:
  AM wavelengths: hundreds of meters
  Full-wave tower: 300m (1 MHz) — impractical but used
  Half-wave: 150m (1 MHz) — more practical
  Quarter-wave: 75m — minimum with ground plane
  Ground plane: radial wires buried, reflect return path
  Multiple towers: directional arrays (protect other stations)

FM BROADCAST ANTENNA:
  1-3m height (at 100 MHz)
  Mounted on tower for height above terrain
  Circular polarization: horizontally + vertically polarized combined
  Why circular: car antennas (vertical) + portable radios (various angle)
                circular polarization works for any receiver orientation

TV BROADCAST ANTENNA:
  UHF antennas: 30-50 cm (at 600 MHz)
  Directional gain: needed to cover city, avoid interference
  EIRP (Effective Isotropic Radiated Power):
    = transmitter power × antenna gain
    FCC limits: EIRP by station class
    High-power TV: EIRP up to 5 MW (or more with directional gain)

GAIN, DIRECTIVITY, EFFICIENCY:
  Directional antenna: focuses power in certain directions
  Gain (dBi) = directivity + efficiency
  High gain: more signal in desired direction but less in others
  Cell tower antenna: high gain in horizontal plane, minimal vertical
                      -> serves users in city, doesn't waste power vertically

PATH LOSS:
  Free-space path loss: PL = 20 log10(4πd/λ)
  Doubles with distance: signal power decreases as d^2
  Doubles with frequency: higher frequency = worse free-space path loss
  (For same transmit power, higher frequency = shorter range or lower signal)
  This is why: 5G mmWave (30 GHz) = short range; AM (1 MHz) = long range
```

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| What is AM? | Amplitude Modulation; audio varies carrier amplitude; 540-1700 kHz (US MF band); simple detection, noise-susceptible |
| What is FM? | Frequency Modulation; audio varies carrier frequency; 87.8-108 MHz (VHF); amplitude-noise immune, wider bandwidth |
| What is ground wave? | LF/MF propagation along Earth's surface; hundreds to thousands km range; AM stations' primary mode |
| What is sky wave? | HF propagation reflecting off ionosphere; thousands of km range; variable, day/night dependent |
| What is LOS propagation? | VHF/UHF line-of-sight; limited to horizon; FM, TV use this; requires tall towers for range |
| What is Carson's rule? | FM bandwidth ≈ 2(Δf + f_max); FM broadcast: ±75 kHz deviation, 15 kHz audio = 200 kHz BW |
| What is OFDM? | Orthogonal Frequency Division Multiplexing; many QAM subcarriers in one channel; WiFi, 5G, DVB use this |
| What is the capture effect? | FM: stronger of two co-channel signals wins completely; AM: both are heard simultaneously |

---

## Common Confusion Points

**"AM has worse audio than FM because AM is older."** AM is worse because of physics. Amplitude modulation is inherently susceptible to amplitude noise (static). FM is noise-immune because noise adds amplitude variations, which the FM demodulator's limiter explicitly removes. HD Radio (IBOC digital AM) partly solves this by encoding audio as digital data, but the channel width of AM (10 kHz) limits achievable audio quality even without noise.

**"Radio waves travel at the speed of light."** They do — 3×10^8 m/s in vacuum. In the atmosphere they're slightly slower (refractive index slightly > 1), but the difference is negligible for practical purposes. The confusion arises because people think "radio" and "light" are different things — they're both electromagnetic radiation, just at different frequencies.

**"Antennas need to be tuned to transmit frequency."** The antenna needs to be resonant at the operating frequency for best efficiency. An antenna operating off-resonance still works but has reduced efficiency (reflected power from impedance mismatch). Modern adaptive antenna systems can electronically tune the resonant frequency. Antenna tuners in transmitters match impedance even for non-resonant antennas.

**"Sky wave explains AM radio at night traveling farther."** Correct physics: at night, the D layer of the ionosphere (which absorbs HF and some MF during the day) disappears. The F layer, which reflects AM frequencies, becomes dominant. AM broadcast signals reflect off the F layer at night and can travel 500-1500 km, causing interference from distant stations. This is why AM stations reduce power at night or use directional antennas.
