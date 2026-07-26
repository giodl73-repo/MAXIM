---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "06-PERIPHERALS-AND-BUSES.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:embedded-systems:peripherals-and-buses
kind: guide
module: embedded-systems
section: embedded-systems
title: Peripherals and Buses - UART, SPI, I2C, CAN, USB, ADC, DAC
status: source-custody
source_custody: partial
current_path: embedded-systems/06-PERIPHERALS-AND-BUSES.md
canonical_path: embedded-systems/06-PERIPHERALS-AND-BUSES.md
backsource_ids: [mdloom-backfill:embedded-systems:06-peripherals-and-buses, git-history:embedded-systems:06-peripherals-and-buses]
concepts: [uart, spi, i2c, can, usb, adc, dac, serial buses]
root_concepts: [serial buses]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# Peripherals and Buses — UART, SPI, I2C, CAN, USB, ADC, DAC

## The Big Picture

Peripherals are how the MCU touches the world: serial buses move bytes to other
chips, analog converters bridge the continuous and digital domains. Each bus is
a different trade among pin count, speed, distance, multi-drop topology, and
robustness. You know networking protocols at a high level; these are the
*physical-layer, board-level* protocols — measured in pins and microseconds,
not packets and milliseconds. Picking the right one is a recurring embedded
design decision.

```
+-----------------------------------------------------------------------+
|                  THE BUS / PERIPHERAL LANDSCAPE                       |
|                                                                       |
|  pins  speed       topology          typical use                      |
|  ----  -----       --------          -----------                      |
|  UART   2   ~Mbps   point-to-point   console, GPS, modules            |
|  SPI   4+   ~10-50M master/multi-slave  flash, displays, fast ADC     |
|  I2C    2   100k-3.4M  multi-master bus  sensors, EEPROM, config      |
|  CAN    2   ~1-8Mbps  multi-drop bus    automotive/industrial nets    |
|  USB   2(+) 12M-5G+  host/device       PC connectivity, mass storage  |
|                                                                       |
|  ANALOG BRIDGE                                                        |
|  ADC: voltage -> number   (sensors in)                                |
|  DAC: number  -> voltage  (signals out)                               |
+-----------------------------------------------------------------------+
```

**Read it as a selection table.** Fewer pins and multi-drop (I2C, CAN) trade
speed for wiring simplicity; more pins (SPI) buy speed; UART is the simplest
point link. The rest of this file is the signaling reality of each.

---

## UART — The Simplest Serial Link

UART (Universal Asynchronous Receiver/Transmitter) is point-to-point,
asynchronous (no shared clock — both ends agree on a *baud rate* in advance),
and the default "console" of embedded. Two wires: TX and RX, crossed between
the two devices.

```
  UART FRAME (8N1: 8 data, No parity, 1 stop)
   idle    start   d0 d1 d2 d3 d4 d5 d6 d7   stop   idle
  HIGH ----+      +--+  +-----+  +--+        +------ HIGH
           |      |  |  |     |  |  |        |
           +------+  +--+     +--+  +--------+
           ^                                ^
           falling edge = RX starts sampling at the agreed baud rate
           (LSB first). No clock line -- timing is by baud agreement.

  Wiring (note the CROSS):
   Device A  TX ------------> RX  Device B
   Device A  RX <------------ TX  Device B
   GND ------------------------- GND  (common ground required)
```

| UART parameter | Meaning | Common value |
|----------------|---------|--------------|
| Baud rate | Bits/sec; both ends MUST match | 9600, 115200 |
| Data bits | Bits per frame | 8 |
| Parity | Error-check bit | None (N) usually |
| Stop bits | Frame terminator | 1 |
| Flow control | RTS/CTS handshake | Often none |

The classic UART failure is a **baud mismatch** — one end at 9600, the other
115200 — yielding garbage. There is no clock to recover from; if the agreed
rates differ by more than a few percent, framing breaks. Variants: **RS-232**
is UART at higher bipolar voltages for longer cables; **RS-485** is a
differential, multi-drop industrial version. (Bridge: UART is to board-level
comms what a raw TCP socket is to networking — the lowest common denominator
everyone falls back to.)

---

## SPI — Fast, Full-Duplex, Master-Driven

SPI (Serial Peripheral Interface) is synchronous (shared clock), full-duplex
(send and receive simultaneously), and the fastest common bus. The master
drives the clock; each slave gets its own chip-select line.

```
  SPI BUS (one master, two slaves)
            +-----------------------------------------+
   MASTER   | SCLK  ----.----------------.----        |
            | MOSI  ----|----.-----------|----.       |
            | MISO  ----|----|-----.-----|----|--.    |
            | CS1   ----'    |     |     |    |  |    |
            | CS2   ---------|-----|-----'    |  |    |
            +---------------'|-----|---------'|--|----+
                            ||     |         ||  |
                         +--..--+  |      +--..--..-+
                         |SLAVE1|  |      | SLAVE 2 |
                         +------+  |      +---------+
   SCLK = clock (master)   MOSI = master out/slave in
   MISO = master in/slave out   CSn = chip select (active low, per slave)
```

```
  ONE SPI BYTE (full-duplex shift)
  As the master clocks 8 SCLK edges, master and slave SWAP a byte:
    master's MOSI byte shifts out  --->  into slave
    slave's  MISO byte shifts out  <---  into master
  Both directions happen on the SAME clocks. To "just read," the master
  sends a dummy byte to generate the clocks.
```

| SPI knob | Meaning |
|----------|---------|
| Clock polarity (CPOL) | Idle clock level (high/low) |
| Clock phase (CPHA) | Sample on first or second edge |
| Mode 0–3 | The four CPOL/CPHA combinations; both ends MUST match |
| Chip select | One line per slave; assert (low) to talk to that slave |
| Bit order | MSB-first (usual) or LSB-first |

SPI is fast (tens of MHz) and dead-simple electrically, but **pin-hungry**:
3 shared wires + 1 chip-select per slave. Add ten SPI chips and you've spent
13 pins. It has no addressing (the chip-select *is* the addressing) and no
acknowledgment — the master assumes the slave kept up. Used for anything fast:
display panels, external flash, high-rate ADCs, SD cards.

---

## I2C — Two Wires, Many Devices

I2C (Inter-Integrated Circuit) trades speed for wiring: just **two wires**
(SDA data, SCL clock) shared by every device on the bus, each addressed by a
7-bit (or 10-bit) address. Both lines are **open-drain** with pull-up
resistors — devices only ever pull low; the pull-ups make high.

```
  I2C BUS (open-drain, shared, addressed)
        +Vcc
         |  |
        [R][R]   <- pull-up resistors (required!)
         |  |
   SDA --+--+----+--------+--------+----  data
   SCL -----+----+--------+--------+----  clock
                 |        |        |
            +----+--+ +---+---+ +--+----+
            |MASTER | |SENSOR | |EEPROM |
            |       | | @0x48 | | @0x50 |
            +-------+ +-------+ +-------+
   Address selects which device; open-drain lets any pull low.
```

```
  I2C TRANSACTION
  START | addr(7) | R/W | ACK | data(8) | ACK | ... | STOP
   |       |        |     |                            |
   |       |        |     slave pulls SDA low to ACK   |
   |       |        read=1 / write=0                   STOP: SDA rises
   |       which device                                while SCL high
   START: SDA falls while SCL high (a unique condition)
```

| I2C feature | Detail |
|-------------|--------|
| Wires | 2 (SDA, SCL) + pull-ups, shared by all |
| Addressing | 7-bit (128 addrs) or 10-bit; in-band |
| Speeds | 100 kHz (standard), 400 kHz (fast), 1 MHz (fast+), 3.4 MHz (HS) |
| ACK/NACK | Receiver pulls SDA low to acknowledge each byte |
| Multi-master | Supported, with bus arbitration |
| Clock stretching | A slow slave can hold SCL low to pause the master |

I2C's two-wire economy is why every cheap sensor uses it: a board with 10 I2C
sensors still uses just 2 pins. The price is speed and fragility — open-drain
lines are slow to rise (pull-up sizing matters, see `electronics/`), and a
single device that hangs holding SDA low **wedges the entire bus**. Address
collisions (two devices at 0x48) are a common integration headache; some chips
offer 2–3 address-select pins to dodge it.

### SPI vs I2C — the recurring choice

```
  SPI                                  I2C
  ---                                  ---
  4+ pins (3 + 1 CS per device)        2 pins total (shared)
  fast (10s of MHz)                    slower (0.1-3.4 MHz)
  full-duplex                          half-duplex
  no addressing (chip-select)          7/10-bit addresses
  no built-in ACK                      per-byte ACK
  point/star to each slave             multi-drop bus
  -> displays, flash, fast ADC          -> sensors, EEPROM, config
```

---

## CAN — The Robust Multi-Drop Bus

CAN (Controller Area Network) is the automotive/industrial workhorse: a
differential, multi-drop, *message-oriented* bus built for electrically noisy
environments and guaranteed delivery priority. No master — every node arbitrates
for the bus by message ID.

```
  CAN BUS (differential pair, multi-drop, terminated)
  [120R] --- CANH --------+--------+--------+--- [120R]
              CANL --------+--------+--------+
                           |        |        |
                       +---+--+ +---+--+ +---+--+
                       | ECU1 | | ECU2 | | ECU3 |
                       +------+ +------+ +------+
   Differential (CANH-CANL) rejects common-mode noise.
   120-ohm terminators at BOTH ends prevent reflections.
```

```
  CAN ARBITRATION (non-destructive, by message ID)
  Nodes start transmitting their ID simultaneously. The bus is
  "wired-AND": a dominant 0 beats a recessive 1.
    Node A id: 0 1 1 0 0 ...
    Node B id: 0 1 0 ...        <- B sends 0 where A sends 1
    Bus:       0 1 0 ...        <- B's dominant 0 wins; A sees a
                                   mismatch and BACKS OFF gracefully.
  Lower ID number = higher priority = wins the bus. No collision,
  no retransmit needed -- the winner keeps going uninterrupted.
```

| CAN property | Detail |
|--------------|--------|
| Wires | 2 differential (CANH, CANL) + termination |
| Topology | Multi-drop, no master, message-addressed |
| Arbitration | Non-destructive, by ID (lower ID wins) |
| Speed | Classic up to 1 Mbps; CAN FD to ~8 Mbps |
| Robustness | Differential + CRC + auto-retransmit + error states |
| Message | ID + up to 8 (classic) / 64 (FD) data bytes |

CAN's non-destructive arbitration is its genius: when two nodes transmit at
once, the higher-priority message wins *without corrupting either* — the loser
detects it and retries later, the winner never even pauses. Combined with
differential signaling and a strong CRC, that makes CAN the bus you trust to
carry brake and engine messages. (Bridge: arbitration-by-priority with
guaranteed delivery is what made CAN the field bus where Ethernet's
collision-and-retry was unacceptable.)

---

## USB — The Host-Centric Universal Bus

USB on an MCU is the bridge to the PC world. It is fundamentally
**host-centric**: a host (PC) initiates everything; devices (your MCU) only
respond. Enumeration, descriptors, and device classes let one connector serve a
keyboard, a serial port, or a disk.

```
  USB (host orchestrates everything)
  .--------.   D+/D-   .-----------------------------.
  |  HOST  |<--------->|  DEVICE (your MCU)           |
  |  (PC)  |  differen-|  enumerates -> presents a    |
  '--------'  tial pair|  CLASS:                       |
                       |   CDC  = virtual COM port     |
                       |   HID  = keyboard/mouse       |
                       |   MSC  = mass storage (disk)  |
                       |   DFU  = firmware update      |
                       '-----------------------------'
   Speeds: Low 1.5M, Full 12M, High 480M, SuperSpeed 5G+
```

For most MCU work, USB shows up as one of a few **device classes**: CDC-ACM
(makes your device appear as a serial COM port — the most common, since it lets
you reuse all your UART-style code over USB), HID (keyboards/mice, driverless),
MSC (mass storage — your device looks like a USB drive), and DFU (device
firmware update — flashing over USB, see `09`). You rarely implement raw USB;
you configure a stack (TinyUSB, vendor middleware) and pick the class.

---

## ADC and DAC — Crossing the Analog Boundary

The world is analog; the MCU is digital. The ADC (Analog-to-Digital Converter)
turns a voltage into a number; the DAC does the reverse. This is where sensors
and actuators meet firmware.

```
  ADC: SAMPLE then QUANTIZE
  analog in  ~~~/\~~~  -- sample/hold --> | quantize | --> number
                                          12-bit -> 0..4095
   Vin = 1.65V, Vref = 3.3V, 12-bit:
   code = round( Vin / Vref * (2^12 - 1) ) = round(0.5 * 4095) = 2048

  DAC: number -> voltage
   code 2048, Vref 3.3V, 12-bit:  Vout = 2048/4095 * 3.3V ~= 1.65V
```

| Converter spec | Meaning | Why it matters |
|----------------|---------|----------------|
| Resolution | Bits (e.g. 12) → 2^N codes | Smallest distinguishable step |
| Reference (Vref) | Full-scale voltage | Sets the volts-per-code |
| Sample rate | Conversions/sec | Must satisfy Nyquist (`signal-processing/`) |
| LSB size | Vref / 2^N | The quantization step (e.g. 3.3V/4096 ≈ 0.8 mV) |
| Sampling time | Charge time of sample-hold cap | Too short → wrong reading |
| ENOB | Effective number of bits | Real resolution after noise |

Two facts a systems peer should internalize:

- **Nyquist**: to capture a signal of frequency f you must sample at > 2f, or
  higher frequencies *alias* down into your band as false low frequencies. An
  anti-aliasing filter (analog, before the ADC) enforces this. The theory is in
  `signal-processing/` and `information-theory/`.
- **ADC + DMA is the canonical pairing**: a free-running ADC dumping samples
  into a circular DMA buffer (`05`) is how you stream sensor data at high rate
  without the CPU servicing every sample. ADC → DMA → ping-pong buffer is the
  standard data-acquisition pattern.

> The op-amps, references, filters, and signal conditioning *in front of* the
> ADC are `electronics/`. The sampling theory *behind* it is
> `signal-processing/`. Here the ADC/DAC is the MCU peripheral that bridges them.

---

## Common Confusion Points

### "My UART prints garbage"

Baud-rate mismatch, almost always. Both ends must agree on baud, data bits,
parity, and stop bits, and there's no clock to recover timing from. Check both
sides are 115200 8N1 (or whatever you intend). Second-most-common: TX/RX not
crossed, or no common ground.

### "My whole I2C bus is dead after one sensor misbehaves"

I2C is open-drain and shared: one device stuck holding SDA low wedges every
device on the bus. Recovery is clocking SCL manually to free the stuck slave,
or a bus-level reset. This shared-fate fragility is the cost of the two-wire
economy.

### "SPI vs I2C — which for a new sensor?"

Pins vs speed. Need high throughput (display, fast ADC) or have spare pins →
SPI. Many slow sensors and want to spend only 2 pins → I2C. If the sensor
offers both, choose by your pin budget and required sample rate.

### "Why does CAN beat Ethernet in a car?"

Non-destructive, priority-based arbitration with guaranteed bounded latency for
high-priority messages, plus differential noise immunity and built-in error
handling. Classic Ethernet's collide-and-retry gives unbounded latency under
load — unacceptable for a brake message. (Automotive Ethernet now coexists with
CAN for high-bandwidth links, but CAN still owns the deterministic control bus.)

### "How big is one ADC step?"

LSB = Vref / 2^N. With Vref = 3.3 V and 12 bits, one code ≈ 3.3/4096 ≈ 0.806 mV.
Noise below that is invisible; signal swings smaller than a few LSBs need a
higher-resolution ADC or analog gain in front of it.

---

## Decision Cheat Sheet

| I need to... | Reach for |
|---|---|
| Simplest point-to-point serial link | UART |
| Console / log output from the MCU | UART (or USB CDC) |
| Fast link to a display / flash / SD card | SPI |
| Many slow sensors on 2 pins | I2C |
| Long-cable, multi-drop industrial link | RS-485 or CAN |
| Robust, prioritized vehicle/industrial net | CAN (CAN FD for more data) |
| Appear as a COM port to a PC | USB CDC-ACM |
| Appear as a USB drive | USB MSC |
| Flash firmware over USB | USB DFU (`09`) |
| Read a voltage / sensor | ADC (mind Vref, resolution, Nyquist) |
| Output an analog voltage | DAC |
| Stream sensor data at high rate | ADC → DMA → circular ping-pong buffer (`05`) |
| Avoid I2C address collisions | Address-select pins, or move a device to SPI |
