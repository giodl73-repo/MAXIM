---
maxim_schema: maxim.frontmatter.v1
id: maxim:historical-geography:overview
kind: guide
module: historical-geography
section: historical-geography
title: Historical Geography and the Feudal World - Overview
status: source-custody
source_custody: partial
current_path: historical-geography/00-OVERVIEW.md
canonical_path: historical-geography/00-OVERVIEW.md
backsource_ids: [proof-backfill:historical-geography:00-overview, git-history:historical-geography:00-overview]
concepts: [overview]
root_concepts: [overview]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Historical Geography & the Feudal World — Overview

## The Big Picture: What a Medieval Map Actually Shows

Modern maps show **states** — sovereign territories with fixed borders, administered uniformly.
Medieval maps show **claims** — overlapping webs of personal obligation, dynastic accident, and contested right.

```
MODERN STATE MODEL:
  FRANCE
    - One sovereign
    - One legal system
    - Fixed borders
    - Uniform administration
    - Citizens owe allegiance to the state

MEDIEVAL FEUDAL MODEL:
  King of France holds:
    - Ile-de-France (demesne)

  The same king also claims suzerainty over:
    - Duke of Normandy (also King of England by personal union)
    - Count of Champagne
    - Duke of Aquitaine (Plantagenet marriage tie)
    - Duke of Burgundy (cadet branch)
    - Count of Toulouse (claims disputed)

  Each owes knight service and suit of court,
  but each may ignore the obligation in practice.
```

The fundamental difference: **feudalism is a personal relationship system**, not a territorial one.
A county belongs to whoever the count is sworn to — and the count's heir may owe allegiance somewhere else.

---

## Transfer Mechanisms — How Territory Moves

```
CONQUEST:
  House A holds County X -> House B holds County X

INHERITANCE:
  Count dies without male heir -> eldest son, daughter, or nearest agnate
  (varies by law; see below)

MARRIAGE:
  Lady holds Duchy Y by inheritance -> husband gains rights jure uxoris
  ("by right of wife")

PURCHASE:
  Count needs cash -> buyer receives land outright or as pledge
  (crusade finance and Treaty of Paris examples)

ELECTION:
  Throne vacant -> electors choose new ruler
  (HRE, Poland, Papacy, and some lordships)

ESCHEAT:
  Vassal dies without heirs, or is convicted of treason -> lord reclaims fief

CRUSADE GRANT:
  Crusade targets territory -> leader receives fiefs from conquered territory
  (Outremer, Albigensian Crusade, Teutonic conquests)
```

---

## The Feudal Pyramid

```
                    EMPEROR / HIGH KING
                    (claims overlordship; enforces erratically)

             DUKE / ARCHBISHOP    PRINCE / ELECTOR    MARQUIS / COUNT
             (great vassals)       (top tier)          (medium lord)

             Counts / Viscounts    Barons / Castellans    Minor lords

             Knights / Sergeants   Free peasants

             Serfs / Villeins
```

**Key insight:** Each level owes the level above:
- **Military service** (primary — the whole point)
- **Counsel** (attend the lord's court, give advice)
- **Aid** (money payments on four specific occasions — see 01-FEUDAL-MECHANICS)

The level above owes back:
- **Protection** (defend the vassal against enemies)
- **Justice** (the court resolves disputes)
- **Non-interference** (don't invade your own vassal's territory)

When these obligations broke down — which was constantly — you got warfare.

---

## Why Medieval Maps Look Nothing Like Modern Ones

### Problem 1: Personal Union
A single person holds multiple titles inherited or won separately.
```
Edward III of England (r. 1327–1377):
  King of England
  Duke of Aquitaine (as vassal of France)
  Claimant to the throne of France (through his mother Isabella)
  → This contradiction triggered the Hundred Years War
```

### Problem 2: Sub-infeudation
A lord grants a fief to a vassal who grants sub-fiefs to sub-vassals.
The grantor of the sub-fief now stands between the king and the sub-vassal.
Quia Emptores (1290, England) stopped this — but only in England.

### Problem 3: Allodial Land
Land held outright with no overlord. The exception that proves the rule.
```
  FEUDAL LAND:           ALLODIAL LAND:
  Lord → Vassal          Owner holds free
  (service owed)         (no service owed)
  Most land in           Rarer — old Frankish
  feudal Europe          freeholders, some
                         Swiss communes,
                         Norwegian odal rights
```

### Problem 4: Competing Claims
Two lords can both have legitimate (to them) claims to the same territory.
Neither claim is necessarily fraudulent — they derive from different transfer events.

### Problem 5: Ecclesiastical Enclaves
Bishoprics and abbeys hold land as quasi-secular lords.
The bishop is both a spiritual official (appointed by Church) and a feudal lord (owes knight service).
The Investiture Controversy was entirely about this contradiction.

---

## Time Scope

This library covers approximately **500–1600 CE** as the core period with earlier backstory where essential.

```
500   -------+---------------------------------------------+------- 1600
             |                                             |
        Justinian I                                  Spanish conquest
        (Eastern Rome                                of Americas;
         survives)                                   Ottoman peak;
                                                     Reformation
             |                                             |
         ~600: Islam emerges
         ~700: Arab Caliphate at maximum extent
         ~800: Charlemagne / Carolingian Empire
         ~900: Viking age peak; feudal fragmentation in France
         ~1000: Seljuk Turks emerge; Kievan Rus peak
         ~1066: Norman Conquest of England
         ~1095: First Crusade called
         ~1200: Mongol expansion begins
         ~1300: Bubonic plague precursor conditions
         ~1347: Black Death devastates Europe
         ~1453: Fall of Constantinople
         ~1492: Columbus / end of Reconquista
         ~1517: Reformation begins
```

---

## Index of Regions in This Library

| File | Region | Core Period | Key Tension |
|------|---------|-------------|-------------|
| `01-FEUDAL-MECHANICS.md` | Conceptual framework | 800–1400 | How the system actually worked |
| `02-TITLE-GLOSSARY.md` | Reference | All | What every title means |
| `03-WESTERN-EUROPE.md` | France, Iberia, England, Italy | 900–1500 | Capetian expansion, Reconquista, Plantagenets |
| `04-HOLY-ROMAN-EMPIRE.md` | German-speaking core | 962–1648 | Fragmentation vs centralization |
| `05-SCANDINAVIA-NORSE.md` | Scandinavia + Norse diaspora | 793–1397 | Viking expansion, three-kingdom consolidation |
| `06-SILESIA-BORDERLANDS.md` | Central European micro-territories | 900–1740 | Habsburg title accumulation |
| `07-EASTERN-EUROPE.md` | Poland, Bohemia, Hungary, Baltic | 900–1550 | Jagiellonian, Hussite, Ottoman pressure |
| `08-BYZANTINE-EMPIRE.md` | Eastern Roman successor | 330–1453 | Contraction, revival, final fall |
| `09-ISLAMIC-CALIPHATES.md` | Caliphates + regional sultanates | 632–1500 | Succession crisis, fragmentation, reconstitution |
| `10-RUSSIA-RUTHENIAN.md` | Rus principalities → Muscovy | 862–1584 | Mongol yoke, Moscow's rise |
| `11-MONGOL-EMPIRE.md` | Steppe empire + four khanates | 1206–1370 | Unification, conquest, divergent Islamization |
| `12-CRUSADES-LEVANT.md` | Outremer | 1096–1291 | Crusader states, Saladin, military orders |
| `13-AFRICA-KINGDOMS.md` | Sub-Saharan Africa | 700–1600 | Trade routes, Islamic vector, Mansa Musa |
| `14-SOUTH-ASIA-MEDIEVAL.md` | India | 600–1700 | Delhi Sultanate, Mughals, Marathas |
| `15-EAST-ASIA-FEUDAL.md` | China, Japan, Korea | 600–1800 | Dynastic cycle, shogunate, Joseon |
| `16-AMERICAS-PRE-COLUMBIAN.md` | Americas | 900–1521 | Aztec, Inca, Maya, Haudenosaunee |
| `17-OTTOMAN-RISE.md` | Ottoman Empire | 1299–1566 | Beylik to world power |

---

## How to Read a Feudal Political Map

**Step 1:** Identify the title-holder, not the territory name.
"Burgundy" means nothing without knowing *which* Burgundy and *who holds it right now*.

**Step 2:** Identify the overlord chain.
Who does this count owe homage to? Is that duke also a king somewhere else?

**Step 3:** Identify contested borders.
Almost every border on a medieval map is contested by at least one party.

**Step 4:** Note the date.
A map from 1200 and a map from 1300 of "France" look almost nothing alike.

**Step 5:** Ask what just happened.
Most maps are snapshots after a key event: a battle, a marriage, a death without heirs.

---

## Common Confusion Points

**"Holy Roman Empire" ≠ contiguous territory**
The HRE was a patchwork of hundreds of entities — free cities, prince-bishoprics, counties, duchies — with varying relationships to imperial authority. Some ignored the emperor entirely.

**"England" vs "Britain" vs "Great Britain"**
England is one kingdom. Wales was conquered 1282. Scotland was independent until 1603 (Union of Crowns) and 1707 (Act of Union). "Britain" before 1603 is anachronistic.

**"France" as Capetian demesne**
In 1000 CE, the King of France directly controlled roughly the Île-de-France — Paris and surroundings. The rest was held by powerful vassals who did as they pleased. "France" as a unified kingdom is an achievement of 1453+, not a starting condition.

**"Byzantine Empire" ≠ self-description**
The Byzantines called themselves the Roman Empire (Βασιλεία Ῥωμαίων). "Byzantine" is a historiographic term coined in the 16th century. They considered themselves the direct continuation of Rome.

**Dates of "falls" are contested**
The "fall of Rome" is 476 CE (traditional), 480 CE, or maybe never — the Eastern Empire continued. "Fall of Constantinople" is clear (1453) but Byzantines had been contracted to a city-state for decades before.

**Regnal years vs calendar years**
Medieval dating often uses regnal years ("in the 14th year of Edward III"). Converting to calendar years requires knowing when the king's reign started — and those dates are sometimes themselves disputed.
