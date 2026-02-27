# Naturalis — Visual Companion to the Natural World

*A cabinet of silhouettes, plates, and specimen illustrations.*

---

## Purpose

The reference library's 52 volumes describe the living world in text, tables, and ASCII diagrams. Naturalis is the visual companion — organism silhouettes for atlas maps, and illustrated plates for identification and beauty.

Two layers:

1. **Silhouettes** — black vector outlines (SVG) from [PhyloPic](https://www.phylopic.org/), positioned as map markers in atlas files. Scientific accuracy, taxonomic precision, scalable to any size.

2. **Plates** — full illustrations from the [Biodiversity Heritage Library](https://www.biodiversitylibrary.org/) and other public domain sources. Historical engravings, watercolors, and scientific diagrams. For identification, reference, and the sheer pleasure of looking.

---

## Silhouette Library

67 organism silhouettes downloaded from PhyloPic. Each is a single SVG `<path>` — pure black on transparent, scales perfectly as an inline map marker.

### By Category

| Category | Count | Organisms |
|----------|-------|-----------|
| **Birds** | 10 | albatross, crane, eagle, flamingo, pelican, penguin, barnacle goose, black tern, bar-tailed godwit, chicken |
| **Mammals** | 18 | caribou, cow, dog, dolphin, elephant, gorilla, horse, jaguar, koala, lemur, llama, orangutan, panda, pig, rat, rhinoceros, sheep, tiger, wildebeest |
| **Reptiles & Amphibians** | 5 | crocodile, frog, lizard, sea turtle, snake |
| **Fish** | 3 | fish, salmon, shark |
| **Invertebrates** | 7 | ant, bee, flea, monarch butterfly, mosquito, silkworm, tick |
| **Plants** | 14 | aloe, baobab, barley, cactus, cannabis, coffee, conifer, eucalyptus, fern, maize, moss, oak, palm, poppy, rice, spruce, wheat |
| **Fungi** | 1 | mushroom |
| **Other** | 1 | coral, homo sapiens |

### Source & Licensing

All silhouettes from [PhyloPic](https://www.phylopic.org/). Licenses vary per image:
- **CC0 (public domain)**: ~45 images — no attribution required
- **CC-BY**: ~15 images — attribution required (credited in manifest)
- **CC-BY-SA**: ~5 images — attribution + share-alike

Full manifest: `atlas/_geodata/silhouettes/_manifest.json`

### Usage in Atlas Maps

Silhouettes are embedded as SVG `<symbol>` + `<use>` elements positioned at geographic coordinates:

```xml
<defs>
  <symbol id="whale" viewBox="0 0 1000 1000">
    <path d="M..."/>
  </symbol>
</defs>

<!-- Humpback whale marker at 30°S, 50°W -->
<use href="#whale" x="-50" y="30" width="7" height="7" fill="#607090" opacity="0.6"/>
```

---

## Plates (Planned)

Illustrated plates organized by taxonomy. Sources:
- [Biodiversity Heritage Library](https://www.biodiversitylibrary.org/) — 150,000+ public domain illustrations
- Wikimedia Commons — curated botanical and zoological art
- Ernst Haeckel's *Kunstformen der Natur* (1904) — 100 plates, public domain

### Proposed Sections

| Section | Content | Source Era |
|---------|---------|-----------|
| Trees & Forests | Major timber and forest species | 18th-19th century botanical art |
| Grains & Crops | Wheat, rice, maize, barley, cotton | Agricultural illustration tradition |
| Medicinal Plants | Pharmacopoeia illustrations | Herbal tradition, 16th-19th century |
| Birds of Passage | Migratory species, flyway markers | Audubon, Gould, 19th century |
| Marine Life | Fish, corals, cephalopods | Haeckel, deep-sea expedition art |
| Insects | Pollinators, vectors, silk producers | Merian, 17th-18th century |
| Mammals | Iconic species per biome | Buffon, 18th century |
| Fungi & Microbes | Mushrooms, lichens, cultures | Mycological illustration |

---

## Cross-References

- **Atlas maps** → `atlas/` (silhouettes used as geographic markers)
- **Botany** → [botany/](../botany/00-OVERVIEW.md)
- **Zoology** → [zoology/](../zoology/00-OVERVIEW.md)
- **Ornithology** → [ornithology/](../ornithology/00-OVERVIEW.md)
- **Entomology** → [entomology/](../entomology/00-OVERVIEW.md)
- **Marine biology** → [marine-biology/](../marine-biology/00-OVERVIEW.md)
- **Mycology** → [mycology/](../mycology/00-OVERVIEW.md)
- **Food plants** → [food-plants/](../food-plants/00-OVERVIEW.md)
- **Animal phylogeny** → [animal-phylogeny/](../animal-phylogeny/00-OVERVIEW.md)
