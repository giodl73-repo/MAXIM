# Recovery 07 — Electricity, Networks & Modern Systems

## The Big Picture

This Recovery Codex volume belongs to **Technology**. Its job is to preserve the
capability to recover electrical power, signaling, batteries, controls, sensors,
motors, radio, and networked systems without mistaking modern devices for magic.

```
ELECTRICITY, NETWORKS, AND MODERN SYSTEMS

Modern systems recover only after power, signals, controls, and safety recover.

SOURCE -----> CIRCUIT -----> LOAD
generator,    conductor,     lamp, motor,
battery       switch, fuse   radio, tool
   |             |             |
   v             v             v
MEASURE ----> CONTROL ----> NETWORK
voltage,       relay, valve,  node, route,
current        feedback       protocol
   |             |             |
   v             v             v
SAFETY -----> MAINTAIN ---> SCALE
shock, fire,   repair, logs   grid, telecom,
isolation      spares         automation

Electricity is useful work made invisible.
That invisibility makes measurement and safety non-negotiable.
```

---

## Minimum Viable Capability

Recovered electrical technology means a society can generate small power, store
some of it, distribute it safely, measure voltage/current/resistance, protect
against shock and fire, build simple motors/generators, send signals, maintain
batteries, and teach operators not to improvise around lethal hazards.

```
generate -> store -> switch -> protect -> measure -> signal -> control -> maintain
```

---

## The Recovery Ladder

| Level | Recovery Task | What Must Survive |
|---|---|---|
| Remember | Electricity kills silently and starts fires | insulation, fuses, grounding, lockout |
| Recognize | Identify sources, conductors, loads, shorts, corrosion, heat | diagrams, color codes, labels |
| Measure | Use meters, test lamps, reference cells, continuity checks | voltmeter, ammeter, ohmmeter, logs |
| Rebuild | Make small generation, batteries, wiring, radio, motors, controls | copper, magnets, acids, insulation |
| Teach | Train electricians, radio operators, battery stewards, control technicians | labs, safety drills, schematics |

---

## Layer 1: Power Sources and Storage

| Source / Store | Recovery Role | Failure Mode |
|---|---|---|
| Hand / animal generator | small emergency power | low output, fatigue |
| Waterwheel / turbine | steady mechanical-to-electrical power | flood, bearing wear |
| Wind | remote power | intermittency, storms |
| Solar thermal / PV salvage | light-to-power where available | fragile supply chain |
| Lead-acid battery | storage, radio, lighting | acid, lead, sulfation |
| Primary cells | experiments, signaling | chemicals consumed |
| Flywheel / lifted weight | mechanical storage | rupture, injury |

Energy rule:

```
source + storage + load discipline = usable power
```

---

## Layer 2: Circuits, Protection, and Fire

Electricity needs a complete path and a safe failure path.

| Element | Purpose | Recovery Hazard |
|---|---|---|
| Conductor | carries current | overheating, theft, corrosion |
| Insulator | prevents unintended path | cracking, moisture |
| Switch | controlled interruption | arcing |
| Fuse / breaker | sacrificial protection | bypassed protection |
| Ground / earth path | fault management | false confidence |
| Enclosure | touch and weather protection | trapped heat |
| Label | safe operation | unlabeled lethal circuit |

Circuit rule:

```
every source needs protection before the load
```

---

## Layer 3: Signals, Radio, and Networks

Electrical recovery is not only power; it is communication.

| System | Recovery Use | Key Requirement |
|---|---|---|
| Telegraph / wired signal | robust text over distance | wire, battery, code |
| Field telephone | voice coordination | line discipline |
| Radio receiver | weather, coordination, education | tuning, antenna, power |
| Radio transmitter | emergency broadcast | frequency discipline |
| Sensor | temperature, pressure, level, motion | calibration |
| Relay network | remote switching | contact maintenance |
| Packet / digital network | later-stage data | power, protocol, clocks |

Network rule:

```
node + link + protocol + power + repair crew
```

---

## Layer 4: Control, Automation, and Safety Cases

Control systems amplify both competence and mistakes.

| Control Element | Use | Failure Risk |
|---|---|---|
| Relay | remote switching | welded contacts |
| Governor | speed control | runaway machine |
| Thermostat | heat control | fire or freeze |
| Float valve | water level | overflow |
| Interlock | prevents unsafe sequence | bypassed safety |
| Alarm | draws attention | alarm fatigue |
| Log | learns from incidents | hidden drift |

Control rule:

```
sensor -> decision -> actuator -> feedback -> safe default
```

---

## Cross-Domain Recovery Map

| Domain | Electrical / Network Need |
|---|---|
| Health | lighting, sterilization heat, refrigeration, communication |
| Water | pumps, sensors, controls |
| Food | milling, cold storage, drying, alarms |
| Transmission | radio, printing support, archive climate |
| Governance | emergency broadcast, records, coordination |
| Computing | power, clocks, storage, cooling |

---

## Cargo-Cult Traps

| Trap | Why It Fails | Countermeasure |
|---|---|---|
| Device worship | black boxes die without parts | preserve principles and schematics |
| Protection bypass | short-term power, long-term fire | fuses and lockout rules |
| Battery neglect | storage silently dies | charge logs and maintenance |
| Radio without protocol | chaos on shared channels | call signs, schedule, discipline |
| Automation without manual fallback | controller failure stops system | bypass plans and drills |

---

## Practical Reconstruction Sequence

```
1. electrical safety, insulation, fuses, and meters
2. small batteries and low-voltage lighting
3. generators from mechanical sources
4. telegraph, field telephone, and radio receiving
5. motors, pumps, and protected circuits
6. radio transmission and network discipline
7. controls, alarms, interlocks, logs, and maintenance
```

---

## Decision Cheat Sheet

| If you need to... | Start With | Key Caveat |
|---|---|---|
| Recover power | Source, storage, protection, load discipline | Generation without safety burns settlements |
| Wire a circuit | Conductor size, insulation, fuse, switch, enclosure | Hidden heat is failure |
| Trust a battery | Chemistry, charge state, corrosion, ventilation, log | Batteries are chemical systems |
| Build communications | Power, antenna, code/protocol, schedule, repair | Shared channels need discipline |
| Add automation | Sensor, actuator, feedback, safe default, manual fallback | Controls fail dangerously when bypassed |
| Scale a network | Standards, spares, trained crews, incident records | Networks are maintenance organizations |

---

## Common Confusion Points

**Electricity is not just power** — It is also measurement, control, signaling,
timing, and coordination.

**Low voltage is not no risk** — Heat, acid, fire, and short circuits still
matter.

**A grid is not wires** — It is generation, protection, standards, operators,
loads, reserves, and repair.

**Automation is not intelligence** — It is control under assumptions.

---

## Connection Forward

Recovery 07 follows Recovery 06 and leads to `08-institutions-markets-governance`,
because modern systems require operators, standards, rules, and public trust.

