# Material Culture

11 directories · How things are made — craft traditions, trade materials, and the process knowledge of human fabrication

---

## Landscape

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                            MATERIAL CULTURE                                         │
└─────────────────────────────────────────────────────────────────────────────────────┘

 SURFACE CHEMISTRY                         FIBER / FABRIC
 ┌────────────────────────────────┐        ┌────────────────────────────────────────┐
 │           pigments/            │        │               textiles/                │
 │  chromophore chemistry         │        │  natural fibers: cotton/wool/silk       │
 │  prehistoric ochres            │        │  synthetics: nylon/polyester/spandex   │
 │  ancient synthetics            │        │  spinning · weaving · dyeing           │
 │  Tyrian purple · ultramarine   │────────▶  leatherworking · fashion industry     │
 │  Industrial Rev. pigments      │  color  └────────────────────────────────────────┘
 │  modern synthetic pigments     │  on
 └───────────────┬────────────────┘  fiber
                 │ pigment → binder
                 ▼ = paint
 ┌───────────────────────────────┐
 │            coatings/          │
 │  paint composition            │
 │  binders / solvents           │
 │  industrial coatings          │
 │  powder · anodizing · PVD     │
 │  adhesives · sealants         │
 │  surface preparation          │
 └───────────────────────────────┘

 CERAMIC / GLASS                            METALWORK / PRECIOUS
 ┌──────────────────────────────┐           ┌──────────────────────────────────────┐
 │          ceramics/           │           │            metalworking/             │
 │  clay mineralogy             │           │  metallurgy (phase diagrams)         │
 │  forming: wheel/cast/press   │           │  casting · forging · rolling         │
 │  firing: sintering kinetics  │           │  drawing · machining                 │
 │  glazes: glass-phase chemistry│──────────▶  welding · finishing                 │
 │  porcelain: Song → Meissen   │  glass     │  tool steels + heat treatment       │
 │  industrial: alumina/SiC/ZrO2│  chemistry └──────────────┬───────────────────────┘
 └──────────────────────────────┘                           │ precious metals
                                                            ▼ are metalworking +
 ┌──────────────────────────────┐           ┌──────────────────────────────────────┐
 │          glassmaking/        │           │              jewelry/                │
 │  random network theory       │           │  precious metal alloys               │
 │  float glass (Pilkington)    │◀──────────│  gemology: crystal systems · 4Cs    │
 │  borosilicate · Gorilla Glass│  optical  │  cutting/faceting: total internal    │
 │  optical fiber               │  precision│  reflection physics                  │
 │  art glass traditions        │           │  metalworking: granulation/filigree  │
 └──────────────────────────────┘           │  hallmarking systems                 │
                                            └──────────────────────────────────────┘

 SCOPE NOTE: Engineering/materials/ covers the physics of material properties.
 This section covers process knowledge, craft traditions, and trade history.
 ┌───────────────────────────────────────────────────────────────────────────────────┐
 │  The distinction: materials/ asks "why is steel hard?" — this section asks        │
 │  "how did Damascus smiths make it, and what did they know that we lost?"          │
 └───────────────────────────────────────────────────────────────────────────────────┘
```

---

## Directories

| Directory | Focus | Entry Point | Bridges to |
|-----------|-------|-------------|------------|
| [`pigments/`](../pigments/00-OVERVIEW.md) | Color from chemistry: chromophore theory (transition metal d-d transitions, charge transfer, conjugated systems), prehistoric pigments (ochre, manganese black, charcoal — natural and heat-treated), ancient synthetics (Egyptian blue as the first synthetic pigment, lead white, verdigris), luxury colors (Tyrian purple from Murex shellfish, ultramarine from lapis lazuli — why these were worth their weight in gold), Industrial Revolution chemistry (Prussian blue as accident, chrome yellow, cobalt blue), modern synthetics (phthalocyanines, quinacridones, azo compounds) | [`01-PREHISTORIC-EARTH.md`](../pigments/01-PREHISTORIC-EARTH.md) — color from first principles, ties the chemistry to what you see | Arts & Culture `colors/` for the physics and perception side; `coatings/` for how pigments are formulated into usable paint; `art-history/` for the cultural history of luxury pigments |
| [`coatings/`](../coatings/00-OVERVIEW.md) | Paint and surface science: paint anatomy (pigment + binder + solvent + additives — each component's role), binder chemistry (oils: oxidative polymerization; acrylics: emulsion; epoxies: crosslinking; polyurethanes: isocyanate chemistry), solvent systems (water-borne vs. solvent-borne, VOC regulation), industrial coatings beyond paint (powder coating: triboelectric and corona charging; anodizing: electrochemical aluminum oxide; PVD: physical vapor deposition for hard coatings), adhesives and sealants (pressure-sensitive, structural, sealant rheology), surface preparation (blasting, phosphating, conversion coatings as adhesion layer) | [`01-PAINT-HISTORY.md`](../coatings/01-PAINT-HISTORY.md) — what paint is made of before anything else | `pigments/` for the colorant side; Engineering `materials/` for coating performance science; `metalworking/` for the substrate these coatings protect |
| [`textiles/`](../textiles/00-OVERVIEW.md) | Fiber, fabric, and fashion industry: natural fiber science (cotton cellulose structure, wool keratin and felting, silk fibroin — why it drapes the way it does, linen vs. hemp), synthetic fiber development (nylon as the first fully synthetic fiber, polyester economics, spandex/Lycra elasticity, aramids for performance), spinning (ring spinning vs. open-end, yarn twist and tenacity), weaving fundamentals (plain/twill/satin — each is a different interlacement geometry), knitting vs. weaving structure, dyeing (fiber-reactive, acid, disperse — matched to fiber chemistry), leatherworking (tanning: vegetable vs. chrome), fashion industry economics (fast fashion supply chain, luxury goods economics, sustainability pressure) | [`01-NATURAL-FIBERS-PLANT.md`](../textiles/01-NATURAL-FIBERS-PLANT.md) — natural and synthetic fiber properties, the material substrate for everything downstream | Material World `coatings/` for textile finishing treatments; History & Ideas `economic-history/` for textile industrialization as a driver of the Industrial Revolution |
| [`ceramics/`](../ceramics/00-OVERVIEW.md) | Clay to finished ceramic: clay mineralogy (kaolinite, illite, montmorillonite — why different clays behave differently), forming techniques (wheel throwing, slip casting, pressing, extrusion), drying stress (why pots crack and how to prevent it), firing physics (sintering: particle bonding without full melting, vitrification, shrinkage calculation), glaze chemistry (glass-phase formation, colorants, surface texture — matte/satin/gloss/crystalline), historical porcelain (Song dynasty Jingdezhen as industrial production center, Meissen's industrial espionage, hard-paste vs. soft-paste), studio ceramics tradition, industrial technical ceramics (alumina for electrical insulators, zirconia for dental crowns, silicon carbide for armor and kiln furniture) | [`01-CLAY-TYPES.md`](../ceramics/01-CLAY-TYPES.md) — clay mineralogy and the forming fundamentals | Engineering `materials/` for technical ceramics in structural/thermal applications; `glassmaking/` for glaze chemistry which shares glass-phase science |
| [`glassmaking/`](../glassmaking/00-OVERVIEW.md) | Glass science and glass-making trades: random network theory (glass as a frozen liquid — the structural model), the silicate network (SiO4 tetrahedra, modifier ions changing properties), float glass process (Pilkington's 1950s invention — molten glass floating on molten tin, still the dominant flat-glass process), specialty glasses (borosilicate: low thermal expansion for labs and cookware; aluminosilicate: Gorilla Glass ion exchange strengthening; fused silica: UV transmission for semiconductor lithography), optical fiber (preform drawing, total internal reflection, attenuation limits), art glass traditions (Venetian murrine and filigrana, Bohemian crystal, studio glass movement) | [`01-GLASS-SCIENCE.md`](../glassmaking/01-GLASS-SCIENCE.md) — the random network model, explains every processing and property fact that follows | Engineering for optical fiber in telecommunications; Arts & Culture `art-history/` for stained glass as medieval architectural element; `ceramics/` for shared high-temperature processing |
| [`jewelry/`](../jewelry/00-OVERVIEW.md) | Precious materials and jeweler's craft: precious metal metallurgy (gold alloys by karat — why 18k vs. 24k, sterling silver 92.5% and why, platinum group metals), gemology fundamentals (crystal systems and why diamond is cubic, the 4Cs — cut/clarity/color/carat — and the physics behind each), cutting and faceting (brilliant cut as a total internal reflection optimization problem — Tolkowsky's 1919 calculation), goldsmithing and silversmithing techniques (forging, soldering, granulation — Etruscan technique still not fully reproduced, filigree, chasing and repoussé, electroforming), stone setting styles (prong/bezel/pavé/channel — each is a different structural solution), hallmarking systems (UK assay office system as the oldest consumer protection scheme) | [`01-PRECIOUS-METALS.md`](../jewelry/01-PRECIOUS-METALS.md) — metal alloys first, gemology second, then fabrication | `metalworking/` for the heavy-metal fabrication techniques that fine jewelry scales down; Arts & Culture `art-history/` for jewelry as portable wealth and political object |
| [`metalworking/`](../metalworking/00-OVERVIEW.md) | Metal from ore to finished part: physical metallurgy (phase diagrams, Fe-C system, hardenability, heat treatment: anneal/normalize/quench/temper), casting processes (sand casting, die casting, investment casting/lost-wax — grain structure implications of each), bulk forming (hot/cold rolling, forging — why forged is stronger than cast for dynamic loads, deep drawing), wire and tube drawing (reduction schedules, die materials), machining operations (turning, milling, drilling — chip formation mechanics, cutting tool geometry), welding (fusion: SMAW/GMAW/GTAW/SAW; solid-state: friction stir, diffusion bonding), finishing (grinding, honing, lapping tolerances, electropolishing), tool steels and carbides | [`01-EXTRACTION-SMELTING.md`](../metalworking/01-EXTRACTION-SMELTING.md) — phase diagrams and the Fe-C system, the physical foundation | Engineering `mechanical/` and `structural/` for the engineering application of metalwork output; `jewelry/` for the fine-scale end of the same craft tradition |
| [`plastics-polymers/`](../plastics-polymers/00-OVERVIEW.md) | The century of synthetic materials — polymer science from first principles: polymer chemistry (monomer, repeat unit, degree of polymerization, molecular weight distributions Mn/Mw/PDI), thermal transitions (Tg and Tm — the difference between amorphous and semicrystalline behavior), major thermoplastic families (PE/PP/PET/PS/PVC — structure/property relationships), thermosets (epoxy, polyurethane, phenolic — why they can't be remelted), elastomers (natural rubber through EPDM, vulcanization), processing methods (injection molding, extrusion, blow molding, thermoforming), compounding and additives (plasticizers, stabilizers, flame retardants), environmental reality (microplastics — sources, fate, toxicology; the recycling rate myth), bioplastics (PLA, PHA — what they actually offer vs. marketing claims), high-performance engineering polymers (PEEK, Kevlar, Vectran) | [`01-POLYMER-CHEMISTRY.md`](../plastics-polymers/01-POLYMER-CHEMISTRY.md) — molecular structure before processing or applications | Engineering `materials/` (Math & Physics) for polymer physics depth; Engineering `composite-materials/` for fiber-reinforced polymer composites; `papermaking/` for cellulosic polymers |
| [`papermaking/`](../papermaking/00-OVERVIEW.md) | The substrate of civilization's memory — the technology and economics of paper: history (Cai Lun's invention ca. 105 CE as the commonly cited date, the Arab spread west, the European paper mill, the Fourdrinier continuous papermaking machine of 1803 as the industrial leap), raw materials (cellulose fiber sources: wood pulp primary, cotton rag for archival, agricultural residues), the Kraft (sulfate) pulping process (chemistry: white liquor dissolves lignin and hemicellulose while preserving cellulose, black liquor recovery for energy), the paper machine (fourdrinier: headbox → forming section → press section → drying), paper chemistry (beating/refining, sizing for ink holdout, coating for smoothness and brightness), archival paper science (acid-hydrolysis of cellulose, buffering, cotton rag as the gold standard — directly relevant to this library's printing), specialty papers (banknote security features, filter media, release liners), digital disruption and packaging as the growth driver | [`01-HISTORY.md`](../papermaking/01-HISTORY.md) — history establishes the progression of technologies | Engineering `materials/` for cellulose polymer science; Arts & Culture `printing-publishing/` for the industrial relationship between paper and print |
| [`composite-materials/`](../composite-materials/00-OVERVIEW.md) | Engineered combinations of matrix and reinforcement that outperform either constituent: composite fundamentals (rule of mixtures for density and modulus, Voigt and Reuss bounds — why the fiber direction matters), fiber types (carbon fiber: PAN precursor, oxidation, carbonization, graphitization; glass fiber: E-glass/S-glass; aramid: Kevlar structure and ballistic performance), matrix systems (thermoset: epoxy, vinyl ester, BMI; thermoplastic: PEEK, nylon), classical laminate theory (CLT: ply stiffness matrix, ABD matrix, coupling between bending and extension), manufacturing processes (prepreg and autoclave as the quality standard; vacuum infusion for larger parts; RTM; filament winding for pressure vessels), structural design and analysis (failure criteria: Tsai-Wu; buckling of composite panels), Boeing 787 case study (50% composite by weight — design decisions, manufacturing challenges, in-service experience), end-of-life crisis (no economical recycling — the industry's unresolved problem) | [`01-FUNDAMENTALS.md`](../composite-materials/01-FUNDAMENTALS.md) — rule of mixtures and the fiber/matrix concept before laminate theory | Engineering `materials-processing/` for the adjacent metals processing; Engineering `manufacturing/` for the production side; `plastics-polymers/` for the polymer matrix science |
| [`furniture/`](../furniture/00-OVERVIEW.md) | Furniture as applied craft, engineering, and cultural production: wood joinery as applied geometry (mortise-and-tenon geometry, dovetail mechanics — why angled tails resist pull-out, the furniture maker's version of structural analysis), period furniture styles (Gothic through Chippendale through Regency — each a different vocabulary of form), Bauhaus and modernist furniture (Marcel Breuer's tubular steel chairs as the Industrial Revolution's aesthetic crystallization), Eames as engineering (DCM/LCW — plywood forming with new technologies, the molded fiberglass shell, the Lounge Chair as material language), Scandinavian design tradition (craft humanism, democratic design, natural materials), modern materials (plywood, MDF, powder-coated steel — how industrial materials enabled new forms), IKEA and flat-pack as industrial design problem (KD hardware, visual assembly instructions as a language without words), ergonomics of seating (spine curvature, contact pressure, active seating), digital fabrication (CNC routing, parametric joinery) | [`01-WOOD-JOINERY.md`](../furniture/01-WOOD-JOINERY.md) — joinery as the structural logic of furniture before style history | Arts & Culture `industrial-design/` (furniture as industrial design); `architecture/` (furniture and interior design relationship); Material Culture `metalworking/` for metal furniture fabrication |

---

## Paths

### Surface treatment from chemistry to application
`pigments/` → `coatings/` → `metalworking/`
*Start with why certain molecules produce color (chromophore chemistry), then how pigments are formulated into coatings with binders and solvents, then see industrial coatings on their actual substrates — metal parts that require corrosion protection, adhesion layers, and tribological surfaces.*

### High-temperature craft traditions
`ceramics/` → `glassmaking/` → `metalworking/`
*Three trades that all rely on controlling high-temperature phase transformations: ceramic sintering, glass vitrification, and metal phase diagrams share underlying thermodynamic principles. Each section approaches the same physics from its own craft tradition.*

### Precious materials and cultural value
`pigments/` → `jewelry/` → Arts & Culture `art-history/`
*The luxury pigments (ultramarine, Tyrian purple) and precious stones share a history of extreme value, long-distance trade, and cultural signification — reading pigments and jewelry together then anchoring them in art history reveals how materials shape culture.*

---

## Adjacent Sections

| Section | The bridge |
|---------|------------|
| Engineering | `metalworking/` is the craft-level version of what Engineering `mechanical/` and `structural/` treat analytically — the same steel, different vantage. `glassmaking/` connects to Engineering `optics/` through optical fiber and lens blanks. `coatings/` connects to `materials/` through tribology, corrosion science, and surface engineering. |
| Mathematics & Physics | Glaze chemistry and glass science are applied solid-state physics (random network theory, ionic conductivity, thermal expansion mismatch). Gemstone optics is applied electromagnetism (Snell's law and TIR explain brilliant-cut design). Casting and forming processes involve solidification physics and dislocation mechanics. |
| Arts & Culture | `pigments/` is the material substrate of painting — art history and pigment chemistry are two accounts of the same objects. `textiles/` feeds directly into fashion and decorative arts traditions in `art-history/`. `jewelry/` and `ceramics/` are decorative arts categories. |
| Natural World | The chemistry of natural dyes and mordants (textiles) connects to the organic chemistry in `natural-sciences/`. Gemstone formation connects to `geology/` and mineral science. Fiber animals (silk moth, merino sheep) and fiber plants (cotton, flax) connect to `animal-phylogeny/` and `food-plants/`. |
