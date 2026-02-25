# Radio and Television — Overview

## The Big Picture

Radio and television are electromagnetic distribution systems that achieved mass reach by exploiting spectrum as a shared resource. The regulatory and economic history is a case study in how a public good (spectrum) gets privatized, monopolized, disrupted, and re-disrupted — the same pattern as broadband, mobile, and cloud infrastructure.

```
BROADCAST MEDIA TECHNOLOGY AND BUSINESS ARC

PHYSICS LAYER:
  Maxwell's equations (1864) -> Hertz demonstrates EM waves (1887)
  -> Marconi transatlantic (1901) -> Continuous wave (1906)
  -> Vacuum tube amplification (de Forest Audion, 1907)
  -> Commercial broadcasting (KDKA Pittsburgh, 1920)

TECHNOLOGY LAYER:
  Analog modulation:
    AM (Amplitude Modulation): 1900s-present
    FM (Frequency Modulation): 1933-present
  Television:
    Mechanical scanning: Nipkow disc (1884), Baird (1926)
    Electronic: Farnsworth (1927), Zworykin (1929)
    Standard: NTSC (US 1941/1953), PAL (Europe 1967), SECAM (France 1967)
  Digital:
    ATSC (US, DTV 2009), DVB (Europe), ISDB (Japan)
    HDTV, 4K broadcast

ECONOMIC LAYER:
  +------------------+    +------------------+    +------------------+
  | NETWORK ERA      | -> | CABLE/SATELLITE  | -> | STREAMING ERA    |
  | 1920s-1970s      |    | 1970s-1990s      |    | 2010s-present    |
  |                  |    |                  |    |                  |
  | Big Three (radio)| -> | CNN (1980)       | -> | Netflix 2007+    |
  | ABC/CBS/NBC      |    | HBO (1972)       |    | SVOD/AVOD/FAST   |
  | Regulated        |    | Channel          |    | Algorithmic      |
  | Oligopoly        |    | proliferation    |    | programming      |
  | Advertiser       |    | Subscription +   |    | On-demand        |
  | funded           |    | advertising      |    | Long tail        |
  +------------------+    +------------------+    +------------------+

REGULATORY LAYER:
  Radio Act 1912 -> Radio Act 1927 -> Communications Act 1934 (FCC)
  ITU spectrum coordination (1906+)
  Fairness Doctrine (1949-1987)
  Digital TV mandate (FCC, 2009)
  Spectrum auctions (1994+)
  5G reallocation (2010s-2020s)
```

---

## The Spectrum as Shared Resource

Spectrum is the fundamental constraint that makes radio economics different from all other media. Unlike paper or bandwidth, spectrum is finite, non-excludable in its physics, and requires coordination to use.

```
SPECTRUM AS PUBLIC GOOD PROBLEM

PHYSICAL REALITY:
  Two radio stations broadcasting on same frequency in same area:
  -> Interference: both signals degrade, neither usable
  -> "Spectrum commons" without coordination = chaos

  Radio Act of 1912: response to Titanic disaster
    Titanic sank 1912; amateur operators blocked distress signals
    Congress: licensed operators, reserved distress frequencies
    First federal spectrum management

SPECTRUM SCARCITY vs ABUNDANCE:
  Early radio: each station = unique frequency
               Spectrum seems infinite (few stations)
               No scarcity problem

  1922-1927: 600+ US stations start broadcasting
             Interference widespread
             Stations deliberately moved to competitors' frequencies
             FRC (Federal Radio Commission) established 1927:
             License regime, spectrum assignment

SPECTRUM = LICENSED PROPERTY RIGHT:
  FRC/FCC: assigns specific frequencies to specific licensees
  License: permission to use specific frequency, specific power,
           specific geographic area
  Property right, but not permanent:
    License: renewable (broadcast licenses: 5-8 years)
    Revocable: violate public interest standard -> lose license
    Not transferable? Actually: assignment allowed with FCC approval
  Effectively: a quasi-property right

INFORMATION THEORY PERSPECTIVE:
  Shannon capacity: C = B * log2(1 + S/N)
  B = bandwidth (Hz), S/N = signal-to-noise ratio
  More bandwidth -> more capacity
  Better modulation -> more bits per Hz
  Spectrum = information-theoretic resource
  Digital modulation (QAM-256, OFDM) >> analog modulation efficiency
  ATSC 3.0: 25-35 Mbps in 6 MHz channel vs NTSC: 1 SD channel
  Same spectrum; 25-35x more information capacity with digital
```

---

## Directory Contents

| File | Topic |
|------|-------|
| 01-RADIO-PHYSICS.md | EM spectrum, propagation, AM/FM modulation, antenna theory |
| 02-EARLY-RADIO.md | Maxwell/Hertz, Marconi, spark gaps, continuous wave, Audion tube |
| 03-BROADCASTING-REGULATION.md | Radio Acts, FCC, public interest standard, ITU, fairness doctrine |
| 04-RADIO-GOLDEN-AGE.md | Network radio 1920s-1950s, NBC/CBS/ABC, soap operas, War of the Worlds |
| 05-TELEVISION-TECHNOLOGY.md | Mechanical scanning, electronic TV, NTSC/PAL/SECAM, CRT to flat panel |
| 06-NETWORK-ERA.md | Big Three, news (Murrow/Cronkite), sitcoms, color transition, Nielsen ratings |
| 07-CABLE-SATELLITE.md | CATV origins, CNN 1980, HBO premium model, DBS, channel proliferation |
| 08-SPECTRUM-MANAGEMENT.md | FCC auctions, DTV transition 2009, white space, 5G spectrum |
| 09-STREAMING-TRANSITION.md | Netflix pivot, streaming wars, cord cutting, SVOD/AVOD/FAST models |

---

## Key Inflection Points

| Year | Event | Significance |
|------|-------|-------------|
| 1887 | Hertz proves EM waves | Physics confirmation of Maxwell |
| 1901 | Marconi transatlantic | Wireless = global communication possible |
| 1907 | De Forest Audion tube | Vacuum tube amplification enables radio broadcasting |
| 1912 | Radio Act 1912 | First federal spectrum regulation (post-Titanic) |
| 1920 | KDKA Pittsburgh | First commercial radio broadcasting |
| 1926 | NBC founded | First radio network; advertising model established |
| 1927 | Radio Act 1927 | FRC established; license regime |
| 1934 | Communications Act | FCC established; broadcast regulation consolidated |
| 1938 | War of the Worlds | Radio's power to convince demonstrated |
| 1941 | NTSC standard | US television technical standard established |
| 1948 | Coaxial cable TV | First cable TV systems (community antenna) |
| 1953 | Color TV standard | NTSC color (compatible with B&W) |
| 1961 | Communications satellite | Telstar 1962; satellite broadcasting concept |
| 1972 | HBO launches | First premium cable channel; subscription model |
| 1980 | CNN launches | First 24-hour news network; cable news category |
| 1994 | FCC spectrum auctions | Spectrum sold to highest bidder; market mechanism |
| 2009 | DTV transition | Analog TV terminated; digital mandatory in US |
| 2013 | Netflix streaming | Original content + streaming dominates |

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| What is AM? | Amplitude Modulation: sound signal changes amplitude of carrier wave; susceptible to electrical noise |
| What is FM? | Frequency Modulation: sound signal changes frequency of carrier; more noise-immune, better fidelity |
| What is NTSC? | National Television System Committee; US/Japan analog color standard (525 lines, 60Hz, 1941/1953) |
| What is the FCC? | Federal Communications Commission; US broadcast regulator (1934); assigns licenses, enforces standards |
| What is the public interest standard? | FCC condition for broadcast licenses: serve public interest, convenience, necessity |
| What is a DMA? | Designated Market Area; Nielsen geographic rating unit; US has 210 DMAs |
| What is SVOD? | Subscription Video On Demand (Netflix, Disney+); fixed monthly fee, no ads |
| What is FAST? | Free Ad-Supported Streaming TV (Pluto TV, Tubi); no subscription, ads support |

---

## Common Confusion Points

**"Spectrum is free."** Spectrum use requires government license (in most countries). The license itself is free for some uses (amateur radio, unlicensed bands like WiFi at 2.4/5 GHz), but broadcast and commercial licenses were historically granted at no charge to the licensee. Since 1994, the FCC has auctioned spectrum for commercial use (billions of dollars). The question of who should benefit from spectrum value (taxpayers vs licensees) is ongoing.

**"Cable TV doesn't use spectrum."** Cable TV uses physical coaxial or fiber cable — not spectrum for signal delivery. But the content may originate from satellite (which uses spectrum) and many cable channels also broadcast over the air (which uses spectrum). The distinction: cable = licensed physical wired infrastructure; broadcast = spectrum-based wireless. Cable systems still require franchise agreements with local governments, which is a different regulatory layer.

**"Streaming ended TV."** Television viewing (defined as video content consumption, including streaming) has increased. What ended is linear scheduled broadcast TV as the dominant form. The habit of watching content at the time a network schedules it — that ended. The habit of watching video content (on any device, any time) continues and grows. The business model changed; the behavior persists in evolved form.

**"The FCC regulates the internet."** The FCC has authority over telecommunications infrastructure and has debated/regulated aspects of internet access (net neutrality battles, 2010-2024). But the FCC does not regulate content on the internet (First Amendment). Broadcasting regulation (indecency, public interest obligations) applies to licensed broadcasters. The same company (Comcast) is both an FCC-regulated cable/broadband provider and an unregulated content creator (NBCUniversal).
