"""Generate Batch 12 and Batch 13 stub directories."""
import os

BASE = 'C:/src/reference'

DIRS = {

    # ── BATCH 12 ──────────────────────────────────────────────────────────────
    # Group 12A — Natural World ♠ (NW·IV) part 1
    # ─────────────────────────────────────────────────────────────────────────

    'dendrology': (
        'Tree biology, wood anatomy, dendrochronology, forest ecology, and silviculture. '
        'Covers the full arc from cellular wood structure to forest-level dynamics. '
        'Connects to soil-science/ (forest soils), freshwater-biology/ (riparian systems), '
        'ecology/ (forest ecology), and construction-materials/ (structural timber).',
        [
            ('OVERVIEW',            'Dendrology: Tree Biology, Wood, and Forests — Landscape'),
            ('TREE-ANATOMY',        'Tree Anatomy: Vascular Cambium, Sapwood, Heartwood, Bark'),
            ('WOOD-PROPERTIES',     'Wood Properties: Grain, Density, Hardness, Shrinkage, Moisture'),
            ('DENDROCHRONOLOGY',    'Dendrochronology: Tree Rings, Climate Records, Cross-Dating'),
            ('FOREST-ECOLOGY',      'Forest Ecology: Succession, Canopy Gaps, Nutrient Cycling'),
            ('TEMPERATE-TREES',     'Temperate Tree Species: Oak, Maple, Beech, Ash, Conifer Families'),
            ('TROPICAL-TREES',      'Tropical Tree Diversity: Rainforest Structure, Emergents, Epiphytes'),
            ('SILVICULTURE',        'Silviculture: Plantation, Selection Cutting, Clear-Cut, Coppice'),
            ('FOREST-ECONOMICS',    'Forest Economics: Timber Markets, Certification, Carbon Credits'),
            ('CONSERVATION',        'Forest Conservation: Old-Growth, Deforestation, Reforestation'),
        ]
    ),

    'freshwater-biology': (
        'Limnology and freshwater ecology: lakes, rivers, wetlands, and their inhabitants. '
        'Covers physical stratification, nutrient dynamics, food webs, and conservation. '
        'Connects to soil-science/ (watershed), hydrology/ (water cycle), '
        'ecology/ (ecosystem processes), and marine-biology/ (aquatic life comparison).',
        [
            ('OVERVIEW',            'Freshwater Biology: Lakes, Rivers, Wetlands — Landscape'),
            ('LAKE-STRATIFICATION', 'Lake Stratification: Thermocline, Turnover, Anoxic Zones'),
            ('RIVER-ECOLOGY',       'River Ecology: Continuum Concept, Hydraulics, Riparian Zones'),
            ('WETLANDS',            'Wetlands: Classification, Hydrology, Carbon Sequestration, Services'),
            ('FRESHWATER-ORGANISMS','Freshwater Organisms: Fish, Amphibians, Invertebrates, Algae, Macrophytes'),
            ('NUTRIENT-CYCLES',     'Nutrient Cycling: Nitrogen, Phosphorus, Silicon in Freshwater'),
            ('EUTROPHICATION',      'Eutrophication: Causes, Algal Blooms, Hypoxia, Remediation'),
            ('AQUATIC-FOOD-WEBS',   'Aquatic Food Webs: Trophic Cascades, Keystone Species, Bioaccumulation'),
            ('CONSERVATION',        'Freshwater Conservation: Invasive Species, Dam Impacts, Flow Regimes'),
            ('WATER-QUALITY',       'Water Quality: Chemistry, Indicator Species, Monitoring Standards'),
        ]
    ),

    'soil-science': (
        'Pedology, soil chemistry, soil physics, and soil microbiology. '
        'Covers soil formation from parent material through horizons, nutrient dynamics, '
        'erosion, and land management. Connects to geology/ (parent material), '
        'agriculture/ (crop soils), ecology/ (nutrient cycling), and freshwater-biology/ (watershed).',
        [
            ('OVERVIEW',            'Soil Science: Pedology, Chemistry, Biology — Landscape'),
            ('SOIL-FORMATION',      'Soil Formation: Parent Material, Weathering, CLORPT Factors'),
            ('SOIL-HORIZONS',       'Soil Horizons: O, A, B, C Horizons — Profiles and Classification'),
            ('TEXTURE-STRUCTURE',   'Soil Texture and Structure: Sand/Silt/Clay Triangle, Aggregates'),
            ('SOIL-CHEMISTRY',      'Soil Chemistry: CEC, pH, Redox, Mineral Nutrients, Buffering'),
            ('SOIL-MICROBIOLOGY',   'Soil Microbiology: Bacteria, Fungi, Mycorrhizae, Soil Food Web'),
            ('NUTRIENT-CYCLING',    'Nutrient Cycling: Nitrogen Fixation, Nitrification, Phosphorus Cycle'),
            ('SOIL-WATER',          'Soil Water: Field Capacity, Wilting Point, Hydraulic Conductivity'),
            ('EROSION-DEGRADATION', 'Soil Erosion and Degradation: Wind, Water, Salinization, Compaction'),
            ('SOIL-MANAGEMENT',     'Soil Management: Tillage Systems, Cover Crops, Carbon Sequestration'),
        ]
    ),

    # Group 12B — Natural World ♠ (NW·IV) part 2 + Material Culture ♠ start
    # ─────────────────────────────────────────────────────────────────────────

    'coral-reefs': (
        'Coral reef biology, ecology, bleaching, formation, and conservation. '
        'The most biodiverse marine ecosystem and among the most climate-threatened. '
        'Connects to marine-biology/ (organisms and ecology), oceanography/ (ocean chemistry), '
        'climate-science/ (bleaching drivers), and freshwater-biology/ (ecosystem comparison).',
        [
            ('OVERVIEW',            'Coral Reefs: Biology, Ecology, and Crisis — Landscape'),
            ('REEF-FORMATION',      'Reef Formation: Carbonate Accretion, Atoll Development, Types'),
            ('CORAL-BIOLOGY',       'Coral Biology: Polyp Structure, Skeleton, Growth Rates, Reproduction'),
            ('SYMBIOSIS',           'Symbiosis: Zooxanthellae, Photosynthesis, and the Bleaching Trigger'),
            ('REEF-ECOLOGY',        'Reef Ecology: Zones, Fish Communities, Invertebrates, Food Webs'),
            ('BLEACHING',           'Bleaching: Thermal Stress, El Nino Events, Recovery and Mortality'),
            ('REEF-DIVERSITY',      'Reef Diversity: Indo-Pacific vs. Caribbean, Hotspots, Species Counts'),
            ('REEF-CHEMISTRY',      'Reef Chemistry: Ocean Acidification, Aragonite Saturation, pH Trends'),
            ('HUMAN-IMPACTS',       'Human Impacts: Overfishing, Runoff, Physical Damage, Tourism'),
            ('RESTORATION',         'Reef Restoration: Coral Gardening, Assisted Evolution, Seeding'),
        ]
    ),

    'woodworking': (
        'Woodworking: wood selection, hand tools, power tools, joinery, and finishing. '
        'Covers the craft from species selection and grain reading through furniture construction. '
        'Connects to dendrology/ (wood properties), construction-materials/ (structural timber), '
        'furniture/ (design and construction), and manufacturing/ (industrial wood processing).',
        [
            ('OVERVIEW',            'Woodworking: Wood, Tools, Joinery, and Finishing — Landscape'),
            ('WOOD-SELECTION',      'Wood Selection: Species, Grain, Figure, Defects, Moisture Content'),
            ('HAND-TOOLS',          'Hand Tools: Planes, Chisels, Saws, Marking Tools — Setup and Use'),
            ('POWER-TOOLS',         'Power Tools: Table Saw, Band Saw, Router, Lathe — Safety and Use'),
            ('JOINERY',             'Joinery: Mortise-Tenon, Dovetail, Box Joint, Biscuit, Dowel'),
            ('SURFACE-PREPARATION', 'Surface Preparation: Flattening, Thickness Planing, Scraping, Sanding'),
            ('FINISHING',           'Finishing: Oils, Waxes, Shellac, Lacquer, Varnish, Water-Based'),
            ('FURNITURE-CONSTRUCTION','Furniture Construction: Case Work, Frame and Panel, Chair Joinery'),
            ('TURNING-CARVING',     'Turning and Carving: Lathe Basics, Bowl Turning, Relief Carving'),
            ('SHOP-SETUP',          'Shop Setup: Workbench Design, Tool Storage, Dust Collection, Safety'),
        ]
    ),

    'leatherworking': (
        'Leatherworking from tanning through finishing: types of leather, tooling, '
        'stitching, and hardware. Covers the full craft process and historical traditions. '
        'Connects to textiles/ (fiber arts comparison), dyeing-fiber/ (surface treatment), '
        'rope-cordage/ (animal fiber traditions), and material-culture overview.',
        [
            ('OVERVIEW',            'Leatherworking: Tanning, Tooling, and Craft — Landscape'),
            ('LEATHER-TYPES',       'Leather Types: Full-Grain, Top-Grain, Split, Suede, Exotic'),
            ('TANNING-PROCESSES',   'Tanning Processes: Vegetable, Chrome, Brain, Alum — Chemistry and History'),
            ('PATTERN-MAKING',      'Pattern Making: Measurement, Templates, Seam Allowance, Layout'),
            ('CUTTING-SKIVING',     'Cutting and Skiving: Knives, Punches, Thinning for Edges and Folds'),
            ('TOOLING-CARVING',     'Tooling and Carving: Swivel Knife, Bevelers, Stamps, Casing'),
            ('DYEING-FINISHING',    'Dyeing and Finishing: Alcohol Dyes, Antique Finishes, Edge Finishing'),
            ('STITCHING-SEWING',    'Stitching: Saddle Stitch, Machine Sewing, Thread Selection, Awls'),
            ('HARDWARE-ASSEMBLY',   'Hardware and Assembly: Rivets, Snaps, Buckles, D-Rings, Gussets'),
            ('CARE-MAINTENANCE',    'Care and Maintenance: Conditioning, Storage, Repair, Patina'),
        ]
    ),

    # Group 12C — Material Culture ♠ (MC·IV) part 2 + Language & Comm ♠ start
    # ─────────────────────────────────────────────────────────────────────────

    'masonry': (
        'Masonry: brick, stone, mortar, structural masonry, arches, vaults, and restoration. '
        'Covers unit masonry from historic hand-laying through modern reinforced systems. '
        'Connects to construction-materials/ (structural analysis), structural/ (load paths), '
        'geology/ (stone types), and rope-cordage/ (pre-industrial building craft).',
        [
            ('OVERVIEW',            'Masonry: Units, Mortar, Structure, and History — Landscape'),
            ('MASONRY-UNITS',       'Masonry Units: Brick Sizes/Grades, CMU, Natural Stone, Adobe, Tile'),
            ('MORTAR-GROUT',        'Mortar and Grout: Portland Types, Lime Mortars, Mix Design, Compatibility'),
            ('BRICKLAYING',         'Bricklaying: Bonds (Running, Flemish, English), Courses, Leads, Corners'),
            ('STONEWORK',           'Stonework: Ashlar, Rubble, Dry-Stone, Coursed vs. Random'),
            ('STRUCTURAL-MASONRY',  'Structural Masonry: Load Paths, Slenderness, Reinforced Masonry, Codes'),
            ('ARCHES-VAULTS',       'Arches and Vaults: Thrust Line, Voussoirs, Barrel, Groin, Gothic'),
            ('HISTORIC-MASONRY',    'Historic Masonry: Roman Concrete, Medieval Cathedrals, Islamic Brick'),
            ('REPAIR-RESTORATION',  'Repair and Restoration: Repointing, Crack Repair, Compatibility Issues'),
            ('MODERN-APPLICATIONS', 'Modern Masonry: Veneer Systems, Glass Block, Thin Brick, Insulated CMU'),
        ]
    ),

    'rope-cordage': (
        'Rope and cordage from fiber selection through braiding, splicing, and application. '
        'Covers natural and synthetic fibers, the mathematics of twist and braid, '
        'knot taxonomy, and historical cordage traditions. Connects to textiles/ '
        '(fiber arts), leatherworking/ (craft traditions), and marine-biology/ (marine use).',
        [
            ('OVERVIEW',            'Rope and Cordage: Fiber, Structure, and Application — Landscape'),
            ('FIBER-MATERIALS',     'Fiber Materials: Hemp, Manila, Sisal, Cotton, Nylon, Polyester, Dyneema'),
            ('SPINNING-TWISTING',   'Spinning and Twisting: S-Twist, Z-Twist, Lay, Ply Construction'),
            ('BRAIDING-PLAITING',   'Braiding and Plaiting: 8-Strand, 16-Strand, Hollow Braid, Kernmantle'),
            ('ROPE-PROPERTIES',     'Rope Properties: Breaking Strength, Elongation, Abrasion, UV Resistance'),
            ('KNOTS-SPLICES',       'Knots and Splices: Ashley Nomenclature, Eye Splice, Back Splice, Whipping'),
            ('HISTORICAL-CORDAGE',  'Historical Cordage: Ancient Egypt, Inca Quipu, Viking Rigging, Sailmaking'),
            ('MARINE-APPLICATIONS', 'Marine Applications: Standing vs. Running Rigging, Mooring, Anchor Rodes'),
            ('INDUSTRIAL-USE',      'Industrial Use: Crane Slings, Arborist Lines, Rescue, Mining Hoist'),
            ('MODERN-SYNTHETICS',   'Modern Synthetics: UHMWPE, Aramid, HMPE — Performance and Trade-offs'),
        ]
    ),

    'journalism': (
        'Journalism: news gathering, reporting, editorial standards, press freedom, '
        'and the transition to digital media. Covers the full arc from penny press '
        'to algorithmic news feeds. Connects to printing-publishing/ (production history), '
        'radio-television/ (broadcast journalism), digital-media/ (contemporary platforms), '
        'and rhetoric/ (persuasion and argument).',
        [
            ('OVERVIEW',            'Journalism: Reporting, Standards, and the Press — Landscape'),
            ('HISTORY',             'History of Journalism: Penny Press, Yellow Journalism, Wire Services, Watergate'),
            ('NEWS-GATHERING',      'News Gathering: Beat Reporting, Source Cultivation, FOIA, Verification'),
            ('REPORTING-WRITING',   'Reporting and Writing: Inverted Pyramid, Narrative, Data Journalism'),
            ('EDITORIAL-STANDARDS', 'Editorial Standards: Objectivity, Balance, Corrections, Conflict of Interest'),
            ('INVESTIGATIVE',       'Investigative Journalism: Long-Form, Document Analysis, Whistleblowers'),
            ('PRESS-FREEDOM',       'Press Freedom: First Amendment, Committee to Protect Journalists, Censorship'),
            ('PHOTOJOURNALISM',     'Photojournalism: Ethics of Image, Decisive Moment, Staged vs. Candid'),
            ('BROADCAST',           'Broadcast Journalism: Television News, Radio, Live Reporting, Chyrons'),
            ('DIGITAL-JOURNALISM',  'Digital Journalism: Social Media, Newsletters, Podcast, Platform Dependence'),
        ]
    ),

    # Group 12D — Language & Communication ♠ (LC·IV) part 2
    # ─────────────────────────────────────────────────────────────────────────

    'oral-tradition': (
        'Oral tradition: composition, memory techniques, epic traditions, folklore, '
        'transmission, and the transition to literacy and digital preservation. '
        'Covers the Parry-Lord oral-formulaic theory through comparative epic traditions. '
        'Connects to rhetoric/ (persuasion without text), world-languages/ (oral cultures), '
        'literature/ (written tradition emergence), and epigraphy/ (early writing).',
        [
            ('OVERVIEW',            'Oral Tradition: Memory, Performance, and Transmission — Landscape'),
            ('ORAL-COMPOSITION',    'Oral Composition: Parry-Lord Theory, Formulaic Phrases, Theme Clusters'),
            ('HOMERIC-TRADITION',   'Homeric Tradition: Iliad and Odyssey as Oral Composition — Evidence'),
            ('MEMORY-TECHNIQUES',   'Memory Techniques: Method of Loci, Formulaic Memory, Oral vs. Literate Mind'),
            ('WORLD-EPIC',          'World Epic Traditions: Mahabharata, Beowulf, Gilgamesh, Sundiata, Mwindo'),
            ('FOLKLORE',            'Folklore and Myth: Propp Morphology, Tale Types, Urban Legend, Rumor'),
            ('TRANSMISSION',        'Transmission and Variation: Drift, Version, Censorship, Community Control'),
            ('PERFORMANCE',         'Performance Context: Bard, Griot, Storyteller — Occasion and Audience'),
            ('ORAL-HISTORY',        'Oral History as Method: Interview Technique, Archive, Reliability'),
            ('DIGITAL-PRESERVATION','Digital Preservation: Recording, Archive Projects, Language Revitalization'),
        ]
    ),

    'epigraphy': (
        'Epigraphy: the study of inscriptions on durable materials. Covers ancient Near East, '
        'Greek and Latin traditions, Egyptian hieroglyphics, runic scripts, Mesoamerican writing, '
        'and modern decipherment methods. Connects to archaeology/ (material context), '
        'world-languages/ (writing systems), oral-tradition/ (literacy emergence), '
        'and historical-geography/ (geographic spread).',
        [
            ('OVERVIEW',            'Epigraphy: Inscriptions, Scripts, and Decipherment — Landscape'),
            ('ANCIENT-NEAR-EAST',   'Ancient Near East: Cuneiform, Sumerian, Akkadian, Ugaritic Alphabet'),
            ('GREEK-LATIN',         'Greek and Latin Inscriptions: Votive, Funerary, Official, Graffiti'),
            ('EGYPTIAN',            'Egyptian Hieroglyphics: Hieratic, Demotic, Champollion and Decipherment'),
            ('DECIPHERMENT',        'Decipherment Methods: Bilingual Texts, Statistical Analysis, Linear B, Maya'),
            ('RUNIC',               'Runic Scripts: Elder Futhark, Younger Futhark, Anglo-Saxon Futhorc'),
            ('MESOAMERICAN',        'Mesoamerican Writing: Maya Glyphs, Aztec Pictography, Zapotec'),
            ('INDUS-UNDECIPHERED',  'Undeciphered Scripts: Indus Valley, Linear A, Proto-Elamite, Rongorongo'),
            ('MEDIEVAL',            'Medieval Inscriptions: Church Latin, Vernacular, Tomb Stones, Coins'),
            ('MODERN-METHODS',      'Modern Methods: Photography, RTI, 3D Scanning, Corpus Databases'),
        ]
    ),

    'digital-media': (
        'Digital media: web content, social platforms, UX writing, content strategy, '
        'the attention economy, misinformation, and the evolving digital public sphere. '
        'Connects to journalism/ (news in digital context), radio-television/ (broadcast legacy), '
        'printing-publishing/ (publishing transition), semiotics/ (sign systems), '
        'and computing/ (platform architecture).',
        [
            ('OVERVIEW',            'Digital Media: Platforms, Content, and Attention — Landscape'),
            ('WEB-WRITING',         'Web Writing: Scanability, Hypertext Structure, SEO, Readability'),
            ('SOCIAL-PLATFORMS',    'Social Media Platforms: Architecture, Algorithm, Feed Design, Network Effects'),
            ('CONTENT-STRATEGY',    'Content Strategy: Audit, Taxonomy, Governance, Voice and Tone'),
            ('UX-WRITING',          'UX Writing: Microcopy, Error Messages, Onboarding, Conversational UI'),
            ('SEARCH-ALGORITHMS',   'Search Algorithms: PageRank, Query Understanding, Featured Snippets, Ads'),
            ('ATTENTION-ECONOMY',   'Attention Economy: Engagement Metrics, Dark Patterns, Persuasive Design'),
            ('DIGITAL-STORYTELLING','Digital Storytelling: Interactive Narrative, Data Visualization, Scrollytelling'),
            ('MISINFORMATION',      'Misinformation: Viral Spread, Prebunking, Fact-Checking, Platform Responsibility'),
            ('FUTURE-TRENDS',       'Future Trends: Generative Media, Synthetic Content, Spatial Computing'),
        ]
    ),

    # Group 12E — Computing & Software ♠ (C·IV)
    # ─────────────────────────────────────────────────────────────────────────

    'distributed-systems': (
        'Distributed systems: consistency models, consensus algorithms, replication, '
        'distributed transactions, and operational patterns. Covers the CAP theorem '
        'through Paxos/Raft through modern cloud-native patterns. '
        'The VP bridge: VSTS and Azure DevOps are distributed systems — '
        'this is what is happening under the scale you built. '
        'Connects to cloud-architecture/, security-engineering/, os/, and computer-architecture/.',
        [
            ('OVERVIEW',            'Distributed Systems: Consistency, Consensus, Replication — Landscape'),
            ('CAP-THEOREM',         'CAP Theorem: Consistency, Availability, Partition Tolerance — Proofs and Limits'),
            ('CONSISTENCY-MODELS',  'Consistency Models: Linearizability, Sequential, Causal, Eventual'),
            ('CONSENSUS',           'Consensus: Paxos, Raft, Viewstamped Replication — Algorithm Internals'),
            ('REPLICATION',         'Replication: Single-Leader, Multi-Leader, Leaderless — Trade-offs'),
            ('DISTRIBUTED-TXN',     'Distributed Transactions: 2PC, Sagas, CRDT, Conflict Resolution'),
            ('DISTRIBUTED-DB',      'Distributed Databases: Spanner, CockroachDB, DynamoDB — Design Choices'),
            ('MESSAGE-QUEUES',      'Message Queues and Streaming: Kafka Architecture, At-Least-Once, Ordering'),
            ('MICROSERVICES',       'Microservices Patterns: Service Mesh, Circuit Breaker, Bulkhead, Backpressure'),
            ('OBSERVABILITY',       'Observability in Distributed Systems: Tracing, Correlation IDs, Chaos Engineering'),
        ]
    ),

    'security-engineering': (
        'Security engineering: threat modeling, secure design principles, vulnerability '
        'management, secure SDLC, identity and access, incident response. '
        'The engineering discipline behind security — not cryptography theory (cryptography/) '
        'but how to build secure systems. VP bridge: Azure security posture, DevSecOps, SDL at Microsoft. '
        'Connects to cryptography/, cloud-architecture/, distributed-systems/, and formal-methods/.',
        [
            ('OVERVIEW',            'Security Engineering: Threat, Design, Response — Landscape'),
            ('THREAT-MODELING',     'Threat Modeling: STRIDE, DREAD, Attack Trees, PASTA — Process and Output'),
            ('SECURE-DESIGN',       'Secure Design Principles: Least Privilege, Defense in Depth, Zero Trust'),
            ('VULNERABILITY-MGMT',  'Vulnerability Management: CVE, CVSS, Patch Prioritization, SLA Frameworks'),
            ('SECURE-SDLC',         'Secure SDLC: SDL at Microsoft, SAST/DAST, Dependency Scanning, Fuzzing'),
            ('IDENTITY-ACCESS',     'Identity and Access: OAuth 2.0, OIDC, RBAC, PAM, Service Accounts'),
            ('NETWORK-SECURITY',    'Network Security: Segmentation, Firewall Rules, TLS Pinning, DNSSEC'),
            ('INCIDENT-RESPONSE',   'Incident Response: Detection, Containment, Eradication, Post-Mortem'),
            ('RED-BLUE-TEAM',       'Red and Blue Team: Penetration Testing, Purple Team, Tabletop Exercises'),
            ('COMPLIANCE',          'Security Compliance: SOC 2, ISO 27001, FedRAMP, GDPR Security Controls'),
        ]
    ),

    'cloud-architecture': (
        'Cloud architecture: IaaS/PaaS/SaaS models, compute and storage patterns, '
        'microservices at scale, serverless, data platforms, and cost optimization. '
        'Azure-first framing throughout (VP background). '
        'Connects to distributed-systems/ (consistency and consensus underneath), '
        'security-engineering/ (cloud security posture), and os/ (virtualization layer).',
        [
            ('OVERVIEW',            'Cloud Architecture: Models, Patterns, and Trade-offs — Landscape'),
            ('CLOUD-MODELS',        'Cloud Models: IaaS/PaaS/SaaS/FaaS, Shared Responsibility, Deployment Models'),
            ('COMPUTE-PATTERNS',    'Compute Patterns: VMs, Containers, Kubernetes, Spot/Reserved/On-Demand'),
            ('STORAGE-PATTERNS',    'Storage Patterns: Object, Block, File, Database — Azure Blob, S3, EBS'),
            ('NETWORKING',          'Cloud Networking: VNet, Peering, Load Balancer, DNS, CDN, ExpressRoute'),
            ('MICROSERVICES',       'Microservices at Scale: AKS, Service Mesh, API Gateway, Event Grid'),
            ('SERVERLESS',          'Serverless: Azure Functions, Event-Driven, Cold Start, State Management'),
            ('DATA-PLATFORMS',      'Cloud Data Platforms: Synapse, Databricks, BigQuery — Lakehouse Pattern'),
            ('COST-OPTIMIZATION',   'Cost Optimization: FinOps, Reserved Capacity, Autoscaling, Tagging'),
            ('MULTI-CLOUD',         'Multi-Cloud and Hybrid: Arc, Anthos, Outposts — Trade-offs and Governance'),
        ]
    ),

    # Group 12F — Technology ♠ (T·IV)
    # ─────────────────────────────────────────────────────────────────────────

    'nanotechnology': (
        'Nanotechnology: nanoscale physics, nanofabrication, MEMS/NEMS, nanomaterials, '
        'carbon nanostructures, self-assembly, and bionanotechnology. '
        'Covers the fundamental physics at 1-100 nm and the engineering that exploits it. '
        'Connects to semiconductor-manufacturing/ (nanofab tools), materials/ '
        '(nanoscale material properties), and biomedical-engineering/ (nanomedicine).',
        [
            ('OVERVIEW',            'Nanotechnology: Physics, Fabrication, and Application — Landscape'),
            ('NANOSCALE-PHYSICS',   'Nanoscale Physics: Quantum Confinement, Surface-to-Volume, van der Waals'),
            ('NANOFABRICATION',     'Nanofabrication: E-Beam Lithography, AFM Lithography, Soft Lithography'),
            ('MEMS-NEMS',           'MEMS and NEMS: Accelerometers, Pressure Sensors, Resonators, Fabrication'),
            ('NANOMATERIALS',       'Nanomaterials: Quantum Dots, Nanoparticles, Nanowires, Properties'),
            ('CARBON-NANOSTRUCTURES','Carbon Nanostructures: Fullerenes, Nanotubes, Graphene — Properties and Use'),
            ('SELF-ASSEMBLY',       'Self-Assembly: DNA Origami, Block Copolymers, Colloidal Assembly'),
            ('NANOELECTRONICS',     'Nanoelectronics: Single-Electron Transistors, Molecular Electronics, Limits'),
            ('BIONANOTECHNOLOGY',   'Bionanotechnology: Nanoparticle Drug Delivery, Biosensors, Theranostics'),
            ('APPLICATIONS',        'Applications: Nanocomposites, Coatings, Catalysis, Energy — Current State'),
        ]
    ),

    'energy-storage': (
        'Energy storage: electrochemical fundamentals, lithium-ion chemistry, advanced '
        'batteries, flow batteries, pumped hydro, compressed air, hydrogen, and '
        'grid-scale economics. The critical enabling technology for renewable energy transition. '
        'Connects to energy-systems/ (generation and grid integration), '
        'electrical-grid/ (grid balancing), and chemistry (electrochemistry foundations in natural-sciences/).',
        [
            ('OVERVIEW',            'Energy Storage: Electrochemical, Mechanical, Thermal — Landscape'),
            ('ELECTROCHEMICAL',     'Electrochemical Fundamentals: Nernst Equation, Electrode Kinetics, SEI Layer'),
            ('LITHIUM-ION',         'Lithium-Ion Batteries: Cathode/Anode Chemistry, BMS, Degradation Mechanisms'),
            ('ADVANCED-BATTERIES',  'Advanced Batteries: Solid-State, Sodium-Ion, Lithium-Sulfur, Li-Air'),
            ('FLOW-BATTERIES',      'Flow Batteries: Vanadium Redox, Iron-Air, Architecture and Trade-offs'),
            ('PUMPED-HYDRO',        'Pumped Hydro: Physics, Sites, Round-Trip Efficiency, Dominance of Deployment'),
            ('COMPRESSED-AIR',      'Compressed Air and Gravity Storage: CAES, Advanced Adiabatic, Iron Weights'),
            ('HYDROGEN',            'Hydrogen Storage: Electrolysis, Fuel Cells, Compressed vs. Liquid vs. Solid'),
            ('GRID-ECONOMICS',      'Grid-Scale Economics: LCOS, Learning Curves, Capacity vs. Energy Cost'),
            ('FUTURE',              'Future Technologies: Long-Duration Storage Roadmap, ARPA-E Programs'),
        ]
    ),

    'infrastructure-systems': (
        'Infrastructure systems: classification, interdependency, resilience frameworks, '
        'failure modes, lifecycle management, smart infrastructure, climate adaptation, '
        'and governance. The discipline of understanding critical systems as systems. '
        'Connects to electrical-grid/, plumbing/, transportation/, urban-planning/, '
        'telecommunications/, and systems-engineering/ (complex system methods).',
        [
            ('OVERVIEW',            'Infrastructure Systems: Classification, Interdependency, Resilience — Landscape'),
            ('CLASSIFICATION',      'Infrastructure Classification: CISA 16 Sectors, Lifeline Infrastructure'),
            ('INTERDEPENDENCY',     'Interdependency: Cascading Failure, Coupled Infrastructure, Rinaldi Model'),
            ('RESILIENCE',          'Resilience Framework: Absorb, Adapt, Recover — Metrics and Assessment'),
            ('FAILURE-MODES',       'Infrastructure Failure Modes: Physical, Cyber, Natural Hazard, Human Error'),
            ('LIFECYCLE',           'Lifecycle Management: Asset Management, Condition Assessment, Capital Planning'),
            ('SMART-INFRA',         'Smart Infrastructure: Sensors, Digital Twins, Predictive Maintenance, IoT'),
            ('CLIMATE-ADAPTATION',  'Climate Adaptation: Flood Risk, Heat Stress, Sea Level, Hardening Strategies'),
            ('SECURITY',            'Infrastructure Security: SCADA Vulnerabilities, ICS Security, Insider Threat'),
            ('GOVERNANCE',          'Governance and Policy: Public-Private Ownership, Regulation, Funding Models'),
        ]
    ),

    # ── BATCH 13 ──────────────────────────────────────────────────────────────
    # Group 13A — Earth & Space + Material Culture + History & Ideas
    # ─────────────────────────────────────────────────────────────────────────

    'remote-sensing': (
        'Remote sensing: electromagnetic spectrum, passive and active sensors, SAR, '
        'LiDAR, satellite orbits, image processing, InSAR, and Earth observation platforms. '
        'The observational frontier of Earth and Space science. '
        'Connects to astronomy/ (space platforms), geology/ (surface mapping), '
        'climate-science/ (global monitoring), geography/ (land cover), '
        'and oceanography/ (sea surface temperature).',
        [
            ('OVERVIEW',            'Remote Sensing: Observation, Sensors, and Applications — Landscape'),
            ('EM-SPECTRUM',         'Electromagnetic Spectrum: Optical, IR, Microwave, Radio — Atmospheric Windows'),
            ('PASSIVE-SENSORS',     'Passive Sensors: Multispectral, Hyperspectral, Thermal — Landsat, MODIS, Sentinel'),
            ('ACTIVE-SENSORS-SAR',  'Active Sensors and SAR: RADAR Principles, Synthetic Aperture, Polarimetry'),
            ('LIDAR',               'LiDAR Systems: Airborne, Terrestrial, Bathymetric — Point Clouds and DEM'),
            ('SATELLITE-ORBITS',    'Satellite Orbits: Sun-Synchronous, Geostationary, Repeat Cycles'),
            ('IMAGE-PROCESSING',    'Image Processing: Geometric Correction, Atmospheric Correction, Classification'),
            ('INSAR',               'InSAR Applications: Ground Deformation, Subsidence, Earthquake, Volcano'),
            ('PLATFORMS',           'Earth Observation Platforms: Sentinel-1/2, Landsat-9, NISAR, Planet Labs'),
            ('APPLICATIONS',        'Applications: Agriculture, Forestry, Urban, Disaster Response, Ice'),
        ]
    ),

    'dyeing-fiber': (
        'Dyeing and fiber arts: natural dye sources, mordanting chemistry, spinning, '
        'weaving basics, and historical traditions from antiquity through synthetic dyes. '
        'The pre-industrial textile arts that feed into textiles/ and leatherworking/. '
        'Connects to textiles/ (industrial continuation), pigments/ (colorant chemistry), '
        'coatings/ (surface treatment), and material-culture overview.',
        [
            ('OVERVIEW',            'Dyeing and Fiber Arts: Color, Fiber, and Craft — Landscape'),
            ('NATURAL-DYE-SOURCES', 'Natural Dye Sources: Woad, Indigo, Madder, Weld, Cochineal, Iron Gall'),
            ('MORDANTING',          'Mordanting: Alum, Iron, Copper, Tannins — Chemistry of Color Fixation'),
            ('DYE-CHEMISTRY',       'Dye Chemistry: Chromophores, Auxochromes, Fiber-Dye Bonding, Fastness'),
            ('FIBER-PREPARATION',   'Fiber Preparation: Scouring, Carding, Combing, Roving — Wool and Plant Fiber'),
            ('SPINNING',            'Spinning: Drop Spindle, Spinning Wheel, Drafting Techniques, Yarn Structure'),
            ('WEAVING',             'Weaving Basics: Loom Types, Plain Weave, Twill, Satin, Tapestry'),
            ('HISTORIC-TRADITIONS', 'Historic Traditions: Tyrian Purple, Batik, Ikat, Resist Dyeing Worldwide'),
            ('SYNTHETIC-DYES',      'Synthetic Dyes: Perkin and Mauveine (1856), Aniline Dyes, Industrial Revolution'),
            ('CONTEMPORARY',        'Contemporary Practice: Natural Dye Revival, Slow Fashion, Fiber Art'),
        ]
    ),

    'historiography': (
        'Historiography: the theory, methodology, and history of historical writing. '
        'Covers ancient historians through Rankean positivism, the Annales school, '
        'social and cultural history, postmodern challenge, and digital humanities. '
        'Connects to intellectual-history/ (history of ideas), social-history/ (methodology), '
        'philosophy-of-science/ (epistemology of history), and digital-media/ (digital humanities).',
        [
            ('OVERVIEW',            'Historiography: Theory and Method of Historical Writing — Landscape'),
            ('ANCIENT-MEDIEVAL',    'Ancient and Medieval Historians: Thucydides, Herodotus, Ibn Khaldun, Bede'),
            ('ENLIGHTENMENT',       'Enlightenment Historicism: Voltaire, Gibbon, Hume — Progress and Reason'),
            ('RANKEAN-POSITIVISM',  'Rankean Positivism: Primary Sources, Archive, Wie es eigentlich gewesen'),
            ('ANNALES-SCHOOL',      'Annales School: Braudel, Longue Duree, Mentalites, Total History'),
            ('SOCIAL-CULTURAL-TURN','Social and Cultural Turn: New Social History, Microhistory, Geertz'),
            ('POSTMODERN-CHALLENGE','Postmodern Challenge: Hayden White, Metahistory, Narrative, Linguistic Turn'),
            ('DIGITAL-HUMANITIES',  'Digital Humanities: Text Mining, Network Analysis, GIS in History'),
            ('GLOBAL-HISTORY',      'Global and World History: Connected Histories, Provincializing Europe'),
            ('PHILOSOPHY-OF-HIST',  'Philosophy of History: Causation, Explanation, Periodization, Counterfactuals'),
        ]
    ),

    # Group 13B — History & Ideas + Technology + Social Sciences
    # ─────────────────────────────────────────────────────────────────────────

    'philosophy-of-science': (
        'Philosophy of science: logical positivism, Popper falsification, Kuhn paradigms, '
        'Lakatos research programs, scientific realism, underdetermination, causation, '
        'and the social studies of science. Connects to history-of-science/ (actual history), '
        'historiography/ (methodology parallel), logic/ (formal foundations), '
        'and intellectual-history/ (Vienna Circle context).',
        [
            ('OVERVIEW',            'Philosophy of Science: Knowledge, Method, and Structure — Landscape'),
            ('LOGICAL-POSITIVISM',  'Logical Positivism: Vienna Circle, Verification Principle, Carnap, Schlick'),
            ('POPPER',              'Popper and Falsificationism: Demarcation, Corroboration, Critical Rationalism'),
            ('KUHN-PARADIGMS',      'Kuhn and Paradigms: Normal Science, Crisis, Revolution, Incommensurability'),
            ('LAKATOS',             'Lakatos and Research Programs: Hard Core, Protective Belt, Progressive vs. Degenerating'),
            ('UNDERDETERMINATION',  'Underdetermination and the Duhem-Quine Thesis: Theory Choice, Holism'),
            ('SCIENTIFIC-REALISM',  'Scientific Realism: Inference to Best Explanation, Anti-Realism, van Fraassen'),
            ('CAUSATION',           'Causation and Explanation: Hempel DN Model, Causal Mechanisms, Interventionism'),
            ('SOCIAL-STUDIES',      'Social Studies of Science: SSK, Laboratory Studies, Actor-Network Theory'),
            ('BY-FIELD',            'Philosophy by Field: Physics, Biology, Economics, Psychology — Specifics'),
        ]
    ),

    'geotechnical-engineering': (
        'Geotechnical engineering: soil mechanics, effective stress, consolidation, '
        'shear strength, slope stability, shallow and deep foundations, retaining structures, '
        'and ground improvement. The foundation engineering discipline. '
        'Connects to structural/ (load transfer to soil), construction-materials/ (buried structure), '
        'geology/ (subsurface characterization), and soil-science/ (pedology overlap).',
        [
            ('OVERVIEW',            'Geotechnical Engineering: Soil Mechanics and Foundation Design — Landscape'),
            ('SOIL-CLASSIFICATION', 'Soil Classification: Unified Soil Classification System, Atterberg Limits'),
            ('EFFECTIVE-STRESS',    'Effective Stress: Terzaghi Principle, Pore Pressure, Stress Paths'),
            ('CONSOLIDATION',       'Consolidation: Primary, Secondary Settlement, Terzaghi 1D Theory, Time Rates'),
            ('SHEAR-STRENGTH',      'Shear Strength: Mohr-Coulomb, Drained vs. Undrained, Failure Envelopes'),
            ('SLOPE-STABILITY',     'Slope Stability: Limit Equilibrium, Bishop Method, Landslide Mechanics'),
            ('SHALLOW-FOUNDATIONS', 'Shallow Foundations: Bearing Capacity (Terzaghi/Meyerhof), Settlement, Mats'),
            ('DEEP-FOUNDATIONS',    'Deep Foundations: Driven Piles, Drilled Shafts, Capacity Methods, Lateral Load'),
            ('RETAINING',           'Retaining Structures: Gravity Walls, Sheet Piles, Soldier Piles, MSE Walls'),
            ('GROUND-IMPROVEMENT',  'Ground Improvement: Preloading, Stone Columns, Grouting, Deep Soil Mixing'),
        ]
    ),

    # Group 13C — Social Sciences + Computing & Software
    # ─────────────────────────────────────────────────────────────────────────

    'development-studies': (
        'Development studies: history and theory of economic development, growth theory, '
        'human development, institutions, aid effectiveness, microfinance, trade, '
        'gender, and the SDGs. Covers Sen, Sachs, Easterly, Acemoglu. '
        'Connects to economics/ (growth theory), political-science/ (institutions), '
        'international-relations/ (geopolitics of development), and public-health/ (HDI).',
        [
            ('OVERVIEW',            'Development Studies: Growth, Human Development, Institutions — Landscape'),
            ('HISTORY',             'History of Development: Modernization Theory, Dependency, Post-Development'),
            ('GROWTH-THEORY',       'Growth Theory: Harrod-Domar, Solow, Endogenous Growth, Convergence'),
            ('HUMAN-DEVELOPMENT',   'Human Development: Sen Capabilities Approach, HDI, IHDI, MPI'),
            ('INSTITUTIONS',        'Institutions and Governance: Acemoglu/Robinson, Property Rights, Rule of Law'),
            ('AID-EFFECTIVENESS',   'Aid Effectiveness: Sachs vs. Easterly Debate, RCTs, Conditional Cash Transfers'),
            ('MICROFINANCE',        'Microfinance and Poverty: Grameen Bank, Impact Evidence, Debt Traps'),
            ('TRADE',               'Trade and Industrialization: Export-Led Growth, Industrial Policy, China Model'),
            ('GENDER',              'Gender and Development: Boserup, Women in Development, Care Economy'),
            ('SUSTAINABILITY',      'Sustainability and Development Goals: SDGs, Planetary Boundaries, Degrowth'),
        ]
    ),

    'programming-language-theory': (
        'Programming language theory: lambda calculus, type theory, operational and '
        'denotational semantics, the Curry-Howard correspondence, dependent types, '
        'effect systems, and modern frontiers. '
        'VP bridge: MIT TCS background means this is review and connection-making — '
        'the lambda calculus you know from theory courses shows up here as the foundation '
        'of every modern type system. Connects to languages/ (applied), computing/ (PLT in practice), '
        'cryptography/ (type-theoretic verification), and formal-methods/ (proof assistants).',
        [
            ('OVERVIEW',            'Programming Language Theory: Foundations and Frontiers — Landscape'),
            ('LAMBDA-CALCULUS',     'Lambda Calculus: Syntax, Beta Reduction, Normal Forms, Church Encoding'),
            ('TYPE-THEORY',         'Type Theory: Simple Types, Polymorphism (System F), Subtyping, Hindley-Milner'),
            ('OPERATIONAL-SEM',     'Operational Semantics: Small-Step, Big-Step, Abstract Machines'),
            ('DENOTATIONAL-SEM',    'Denotational Semantics: Scott Domains, Continuity, Full Abstraction'),
            ('CURRY-HOWARD',        'Curry-Howard Correspondence: Proofs as Programs, Types as Propositions'),
            ('DEPENDENT-TYPES',     'Dependent Types: Pi and Sigma Types, Coq, Agda, Idris — Proof-Carrying Code'),
            ('EFFECT-SYSTEMS',      'Effect Systems: Algebraic Effects, Monads as Effects, Capability-Based Types'),
            ('COMPILER-SEMANTICS',  'Compiler Semantics: Denotation-Preserving Transforms, SSA, CPS Conversion'),
            ('MODERN-FRONTIERS',    'Modern Frontiers: Gradual Typing, Refinement Types, Session Types, Linear Types'),
        ]
    ),
}

STATUS_HEADER = '| File | Topic | Status |\n|------|-------|--------|\n'

for dir_name, (notes, files) in DIRS.items():
    dir_path = os.path.join(BASE, dir_name)
    os.makedirs(dir_path, exist_ok=True)

    rows = []
    for i, (slug, title) in enumerate(files):
        fname = f'{i:02d}-{slug}.md'
        fpath = os.path.join(dir_path, fname)
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(f'# {title}\n\n> Stub — to be written.\n')
        rows.append(f'| {fname} | {title} | \U0001f51c |')

    status = (
        f'# {dir_name}/ \u2014 Status\n\n'
        f'## Files\n\n'
        + STATUS_HEADER
        + '\n'.join(rows)
        + f'\n\n## Coverage Notes\n\n{notes}\n'
    )
    with open(os.path.join(dir_path, 'STATUS.md'), 'w', encoding='utf-8') as f:
        f.write(status)

    print(f'Created {dir_name}/ ({len(files)} content files + STATUS.md)')

print(f'\nDone. {len(DIRS)} directories scaffolded.')
