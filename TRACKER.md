# Reference Library — Tracker

**Status key:** ✅ Complete | 🔜 Stubs (files exist, content to write) | ❌ Not started

Each directory has a `STATUS.md` with its full file list.

---

## Summary Dashboard

| Directory | Files | Status |
|-----------|-------|--------|
| [`computing/`](computing/STATUS.md) | 28 | ✅ |
| [`ai-engineering/`](ai-engineering/STATUS.md) | 5 | ✅ |
| [`data-science/`](data-science/STATUS.md) | 17 | ✅ |
| [`mathematics/`](mathematics/STATUS.md) | 24 | ✅ |
| [`languages/`](languages/STATUS.md) | 19 | ✅ |
| [`query-languages/`](query-languages/STATUS.md) | 13 | ✅ |
| [`scripting/`](scripting/STATUS.md) | 10 | ✅ |
| [`os/`](os/STATUS.md) | 8 | ✅ |
| [`physics/`](physics/STATUS.md) | 10 | ✅ |
| [`electronics/`](electronics/STATUS.md) | 8 | ✅ |
| [`materials/`](materials/STATUS.md) | 7 | ✅ |
| [`neuroscience/`](neuroscience/STATUS.md) | 5 | ✅ |
| [`economics/`](economics/STATUS.md) | 5 | ✅ |
| [`information-theory/`](information-theory/STATUS.md) | 5 | ✅ |
| [`natural-sciences/`](natural-sciences/STATUS.md) | 18 | ✅ |
| [`astronomy/`](astronomy/STATUS.md) | 12 | ✅ |
| [`biology/`](biology/STATUS.md) | 7 | ✅ |
| [`quantum-computing/`](quantum-computing/STATUS.md) | 5 | ✅ |
| [`control-theory/`](control-theory/STATUS.md) | 5 | ✅ |
| [`finance/`](finance/STATUS.md) | 5 | ✅ |
| [`mechanical/`](mechanical/STATUS.md) | 6 | ✅ |
| [`structural/`](structural/STATUS.md) | 5 | ✅ |
| [`chemical-eng/`](chemical-eng/STATUS.md) | 6 | ✅ |
| [`nuclear/`](nuclear/STATUS.md) | 6 | ✅ |
| [`codes/`](codes/STATUS.md) | 10 | ✅ |
| [`world-languages/`](world-languages/STATUS.md) | 15 | ✅ |
| [`historical-geography/`](historical-geography/STATUS.md) | 18 | ✅ |
| [`periodic-table/`](periodic-table/STATUS.md) | 12 | ✅ |
| [`animal-phylogeny/`](animal-phylogeny/STATUS.md) | 13 | ✅ |
| [`mythology/`](mythology/STATUS.md) | 12 | ✅ |
| [`linguistics/`](linguistics/STATUS.md) | 10 | ✅ |
| [`music-theory/`](music-theory/STATUS.md) | 10 | ✅ |
| [`cognitive-science/`](cognitive-science/STATUS.md) | 10 | ✅ |
| [`human-biology/`](human-biology/STATUS.md) | 11 | 🔜 |
| [`disease/`](disease/STATUS.md) | 11 | 🔜 |
| [`medicine/`](medicine/STATUS.md) | 11 | 🔜 |
| [`philosophy/`](philosophy/STATUS.md) | 7 | 🔜 |
| [`aeronautics/`](aeronautics/STATUS.md) | 6 | 🔜 |
| [`law/`](law/STATUS.md) | 8 | 🔜 |
| [`organizational-behavior/`](organizational-behavior/STATUS.md) | 7 | 🔜 |
| [`cryptography/`](cryptography/STATUS.md) | 6 | 🔜 |
| [`statistics-applied/`](statistics-applied/STATUS.md) | 6 | 🔜 |
| [`climate-science/`](climate-science/STATUS.md) | 7 | 🔜 |
| [`political-science/`](political-science/STATUS.md) | 7 | 🔜 |
| [`psychology/`](psychology/STATUS.md) | 7 | 🔜 |
| [`geography/`](geography/STATUS.md) | 8 | 🔜 |
| [`spices/`](spices/STATUS.md) | 11 | 🔜 |
| [`pigments/`](pigments/STATUS.md) | 11 | 🔜 |

**Complete: 339 files | To write: 124 files across 43 directories**

---

## Session Prompts

One-line agent prompt for each session. Read `CLAUDE.md` + the directory's `STATUS.md` before writing.

| Session | Directory | Prompt |
|---------|-----------|--------|
| 15 | `human-biology/` | Every major body system — musculoskeletal, cardiovascular, respiratory, nervous, endocrine, immune, digestive, renal, reproductive, integumentary + overview |
| 16 | `disease/` | All disease categories — bacterial, viral, fungal/parasitic/prion, cancer, cardiovascular, metabolic/endocrine, autoimmune, neurological/psychiatric, genetic/developmental, epidemiology |
| 17 | `medicine/` | All drug classes — antibiotics, antivirals/vaccines, cardiovascular, CNS, endocrine/metabolic, cancer, immunomodulators, respiratory/GI, anesthesia, diagnostics/imaging + overview |
| — | `philosophy/` | Classical + modal logic (Gödel bridge), epistemology, metaphysics, philosophy of mind, ethics (AI ethics), philosophy of science — MIT TCS bridges throughout |
| — | `aeronautics/` | Aerodynamics, propulsion (Brayton/Isp), flight mechanics (6-DOF), avionics (INS/FMS), structures (aeroelasticity) |
| 18 | `law/` | Common law / civil law, contracts, IP/patents (Alice Corp, FOSS licensing), privacy (GDPR/CCPA), antitrust (tech cases), corporate, employment, international |
| 19 | `organizational-behavior/` | Motivation (self-determination/expectancy), leadership (servant/transformational), teams/groups, org design (Conway's Law/team topologies), strategy (Porter/OKRs/platform), change management |
| 20 | `cryptography/` | Symmetric (AES-GCM/ChaCha20), asymmetric (RSA-OAEP/ECDH/Ed25519/pairings), protocols (TLS 1.3/Signal), ZK/MPC (SNARKs/garbled circuits), post-quantum (Kyber/Dilithium FIPS 203/204) |
| 21 | `statistics-applied/` | Experimental design, A/B testing (CUPED/SRM/sequential testing/bandits), quasi-experimental (DiD/RDD/synthetic control/IV), Bayesian practice, reliability/SPC |
| 22 | `climate-science/` | Carbon cycle, GCMs (CMIP6), feedbacks/tipping points (AMOC/GIS/permafrost), emissions pathways (SSPs), impacts, mitigation + geoengineering (SAI/termination shock) |
| 23 | `political-science/` | IR theory (Waltz/Wendt/Mearsheimer), nuclear deterrence (MAD/credibility/arms control), geopolitics (Mackinder/Mahan/BRI/Indo-Pacific), comparative politics, institutions (Acemoglu/North), political economy |
| 24 | `psychology/` | Social (conformity/attribution/bystander), personality (Big Five/dark triad/MBTI critique), clinical (DSM-5/CBT), organizational, persuasion (Cialdini/ELM/dark patterns/inoculation), health/stress |
| 25 | `geography/` | Physical (plate tectonics/landforms/soils), climate zones (Köppen), ocean-atmosphere (AMOC/ENSO/monsoons), biogeography (Wallace line/island bio), population/urban (DTM/Zipf), geopolitics/resources (chokepoints/rare earths/Arctic), economic geography (GVCs/smile curve/ports) |
| 26 | `spices/` | Overview (trade eras/VOC/Columbian Exchange), pepper/salt, cinnamon/cassia, turmeric/ginger/galangal, saffron/vanilla, nutmeg/cloves/mace (Banda Islands), capsicum/chili (TRPV1/Scoville), cumin/coriander/fennel (Apiaceae), cardamom/star anise (Tamiflu), aromatics/herbs, spice chemistry (alkaloids/terpenes/phenylpropanoids) |
| 27 | `pigments/` | Overview (chromophore mechanisms), prehistoric/earth pigments (ochre/Blombos Cave), ancient synthetic (Egyptian blue/cinnabar), purple/red luxury (Tyrian/cochineal), blue rarity (lapis lazuli/synthetic ultramarine 1826), lead pigments (stack process), organic dyes/mordants (indigo/madder), Prussian blue era, Impressionist revolution (tube paint 1841/cadmiums), modern synthetic (TiO₂/phthalocyanines/quantum dots), conservation/authentication |

---

## Agent Prompt Template

```
You are writing session {N} of the reference library.

1. Read CLAUDE.md for style contract and learner profile
2. Read {directory}/STATUS.md for the full file list and planned coverage
3. Write every file listed. Follow computing/01-PACKAGE.md format exactly.
4. Each file: Big Picture diagram → layered sections → Decision Cheat Sheet → Common Confusion Points
5. Peer-level. No handholding. MIT TCS background assumed.
6. Update STATUS.md when done — mark all files ✅
```
