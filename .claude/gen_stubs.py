import os

BASE = 'C:/src/reference'

DIRS = {
    # Batch 7A — Mathematics & Physics
    'complex-analysis': (
        'Complex analysis: analytic functions, Cauchy-Riemann equations, contour integration, residues, conformal maps, Riemann surfaces',
        [
            ('OVERVIEW', 'Landscape and Taxonomy'),
            ('ANALYTIC-FUNCTIONS', 'Analytic Functions and Cauchy-Riemann Equations'),
            ('COMPLEX-INTEGRATION', 'Contour Integration and Cauchy\'s Theorem'),
            ('RESIDUES-POLES', 'Residues, Poles, and Laurent Series'),
            ('CONFORMAL-MAPS', 'Conformal Mappings and Applications'),
            ('RIEMANN-SURFACES', 'Riemann Surfaces'),
            ('ENTIRE-MEROMORPHIC', 'Entire and Meromorphic Functions'),
            ('ANALYTIC-CONTINUATION', 'Analytic Continuation'),
            ('HARMONIC-FUNCTIONS', 'Harmonic Functions and the Dirichlet Problem'),
            ('APPLICATIONS', 'Applications to Physics and Engineering'),
        ]
    ),
    'fluid-dynamics': (
        'Fluid dynamics: Navier-Stokes equations, inviscid flow, boundary layers, turbulence, CFD, aerodynamic and hydrodynamic applications',
        [
            ('OVERVIEW', 'Landscape and Taxonomy'),
            ('CONTINUUM-MECHANICS', 'Continuum Mechanics and Governing Equations'),
            ('INVISCID-FLOW', 'Ideal and Inviscid Flow'),
            ('VISCOUS-FLOW', 'Viscous Flow and Navier-Stokes'),
            ('BOUNDARY-LAYERS', 'Boundary Layer Theory'),
            ('TURBULENCE', 'Turbulence: Models and Structure'),
            ('COMPRESSIBLE-FLOW', 'Compressible Flow and Shock Waves'),
            ('AERODYNAMICS', 'Aerodynamics: Lift, Drag, and Wings'),
            ('HYDRODYNAMICS', 'Hydrodynamics and Free-Surface Flows'),
            ('CFD', 'Computational Fluid Dynamics'),
        ]
    ),
    'statistical-mechanics': (
        'Statistical mechanics: ensembles, partition functions, phase transitions, renormalization group, non-equilibrium systems',
        [
            ('OVERVIEW', 'Landscape and Taxonomy'),
            ('FOUNDATIONS', 'Probability and the Boltzmann Distribution'),
            ('MICROCANONICAL', 'Microcanonical Ensemble'),
            ('CANONICAL', 'Canonical and Grand Canonical Ensembles'),
            ('QUANTUM-STATS', 'Quantum Statistics: Fermi-Dirac and Bose-Einstein'),
            ('PHASE-TRANSITIONS', 'Phase Transitions and Critical Phenomena'),
            ('RENORMALIZATION', 'Renormalization Group'),
            ('ISING-MODELS', 'Ising Model and Lattice Systems'),
            ('NON-EQUILIBRIUM', 'Non-Equilibrium Statistical Mechanics'),
            ('CONNECTIONS', 'Connections to Thermodynamics and Information Theory'),
        ]
    ),
    # Batch 7B — Mathematics & Physics
    'partial-differential-equations': (
        'PDEs: classification, elliptic/parabolic/hyperbolic equations, Fourier methods, Green\'s functions, distributions, numerical methods',
        [
            ('OVERVIEW', 'Landscape and Taxonomy'),
            ('CLASSIFICATION', 'Classification and Well-Posedness'),
            ('FIRST-ORDER', 'First-Order PDEs and Method of Characteristics'),
            ('WAVE-EQUATION', 'Wave Equation and Hyperbolic Systems'),
            ('HEAT-EQUATION', 'Heat Equation and Parabolic Systems'),
            ('LAPLACE-POISSON', 'Laplace and Poisson Equations'),
            ('FOURIER-METHODS', 'Fourier Methods and Separation of Variables'),
            ('GREENS-FUNCTIONS', "Green's Functions and Distributions"),
            ('VARIATIONAL-WEAK', 'Variational Formulation and Weak Solutions'),
            ('NUMERICAL-PDES', 'Numerical Methods for PDEs'),
        ]
    ),
    'variational-calculus': (
        'Variational calculus: Euler-Lagrange equations, functionals, Lagrangian and Hamiltonian mechanics, optimal control, connections to ML',
        [
            ('OVERVIEW', 'Landscape and Taxonomy'),
            ('FUNCTIONALS', 'Functionals and the Variational Derivative'),
            ('EULER-LAGRANGE', 'Euler-Lagrange Equations'),
            ('CONSTRAINTS', 'Constrained Variation and Lagrange Multipliers'),
            ('LAGRANGIAN-MECHANICS', 'Lagrangian Mechanics'),
            ('HAMILTONIAN-MECHANICS', 'Hamiltonian Mechanics and Phase Space'),
            ('SECOND-VARIATION', 'Second Variation and Stability'),
            ('DIRECT-METHODS', 'Direct Methods and Sobolev Spaces'),
            ('OPTIMAL-CONTROL', 'Optimal Control and Pontryagin Principle'),
            ('ML-CONNECTIONS', 'Connections to Machine Learning and Gradient Flows'),
        ]
    ),
    'lie-groups': (
        'Lie groups and algebras: matrix groups, exponential map, representation theory, root systems, applications to physics and geometry',
        [
            ('OVERVIEW', 'Landscape and Taxonomy'),
            ('MATRIX-GROUPS', 'Matrix Lie Groups: GL, SL, O, U, Sp'),
            ('LIE-ALGEBRAS', 'Lie Algebras and the Exponential Map'),
            ('REPRESENTATIONS', 'Representation Theory'),
            ('SU2-SO3', 'SU(2), SO(3), and Angular Momentum'),
            ('ROOT-SYSTEMS', 'Root Systems and Dynkin Diagrams'),
            ('SEMISIMPLE', 'Semisimple Lie Algebras and Classification'),
            ('GAUGE-THEORY', 'Lie Groups in Gauge Theory and the Standard Model'),
            ('DIFFERENTIAL-GEOMETRY', 'Lie Groups as Differentiable Manifolds'),
            ('APPLICATIONS', 'Applications to Physics, Robotics, and Computer Vision'),
        ]
    ),
    # Batch 7C — Life Sciences
    'evolutionary-biology': (
        'Evolutionary biology: natural selection, population genetics, Hardy-Weinberg, drift, speciation, phylogenetics, evo-devo',
        [
            ('OVERVIEW', 'Landscape and Taxonomy'),
            ('NATURAL-SELECTION', 'Natural Selection: Mechanism and Evidence'),
            ('POPULATION-GENETICS', 'Population Genetics: Hardy-Weinberg and Drift'),
            ('MOLECULAR-EVOLUTION', 'Molecular Evolution and Neutral Theory'),
            ('SPECIATION', 'Speciation: Mechanisms and Models'),
            ('PHYLOGENETICS', 'Phylogenetics and Molecular Clocks'),
            ('EVO-DEVO', 'Evolutionary Developmental Biology (Evo-Devo)'),
            ('SEXUAL-SELECTION', 'Sexual Selection and Life History Theory'),
            ('COEVOLUTION', 'Coevolution and Arms Races'),
            ('MACROEVOLUTION', 'Macroevolution, Mass Extinctions, and the Fossil Record'),
        ]
    ),
    'virology': (
        'Virology: virus structure, Baltimore classification, replication cycles, quasispecies, immune evasion, antiviral strategies, pandemic biology',
        [
            ('OVERVIEW', 'Landscape and Taxonomy'),
            ('VIRUS-STRUCTURE', 'Virus Structure and Genome Organization'),
            ('BALTIMORE-CLASSIFICATION', 'Baltimore Classification System'),
            ('REPLICATION-CYCLES', 'Viral Replication Cycles'),
            ('HOST-INTERACTIONS', 'Virus-Host Interactions and Tropism'),
            ('IMMUNE-EVASION', 'Immune Evasion Strategies'),
            ('QUASISPECIES', 'Quasispecies Theory and Viral Evolution'),
            ('ANTIVIRAL-STRATEGIES', 'Antiviral Drugs and Resistance Mechanisms'),
            ('PANDEMIC-BIOLOGY', 'Pandemic Biology: Emergence and Spread'),
            ('APPLICATIONS', 'Viruses as Tools: Phage Therapy and Gene Delivery'),
        ]
    ),
    'biophysics': (
        'Biophysics: protein folding, cryo-EM, membrane biophysics, Hodgkin-Huxley, single-molecule techniques, AlphaFold context',
        [
            ('OVERVIEW', 'Landscape and Taxonomy'),
            ('THERMODYNAMICS-BIO', 'Thermodynamics of Biological Systems'),
            ('PROTEIN-FOLDING', 'Protein Folding: Energy Landscapes and Prediction'),
            ('STRUCTURAL-METHODS', 'Structural Methods: X-ray, NMR, Cryo-EM'),
            ('MEMBRANE-BIOPHYSICS', 'Membrane Biophysics and Ion Channels'),
            ('HODGKIN-HUXLEY', 'Hodgkin-Huxley Model and Electrophysiology'),
            ('MOLECULAR-MOTORS', 'Molecular Motors and Cytoskeletal Dynamics'),
            ('SINGLE-MOLECULE', 'Single-Molecule Techniques'),
            ('STOCHASTIC-BIO', 'Stochastic Processes in Biology'),
            ('ALPHAFOLD-ERA', 'AlphaFold and the Protein Structure Revolution'),
        ]
    ),
    # Batch 7D — Arts & Culture / Natural World
    'dance': (
        'Dance: Laban notation, ballet to contemporary, world forms, choreographic structure, dance as cultural expression',
        [
            ('OVERVIEW', 'Landscape and Taxonomy'),
            ('BALLET', 'Ballet: Technique, Vocabulary, and History'),
            ('MODERN-POSTMODERN', 'Modern and Postmodern Dance'),
            ('WORLD-FORMS', 'World Dance Forms and Traditions'),
            ('LABAN-NOTATION', 'Labanotation and Movement Analysis'),
            ('CHOREOGRAPHIC-STRUCTURE', 'Choreographic Structure and Composition'),
            ('MUSIC-DANCE', 'Music-Dance Relationships'),
            ('DANCE-SCIENCE', 'Dance Science: Biomechanics and Training'),
            ('CULTURAL-HISTORY', 'Dance as Cultural and Political History'),
            ('DIGITAL-DANCE', 'Digital Dance: Motion Capture and New Forms'),
        ]
    ),
    'industrial-design': (
        'Industrial design: Bauhaus through Braun through Ive, design process, materials, ergonomics, design as engineering constraint satisfaction',
        [
            ('OVERVIEW', 'Landscape and Taxonomy'),
            ('HISTORY-MOVEMENTS', 'History: Bauhaus, Streamlining, and Modernism'),
            ('BRAUN-RAMS', 'Braun and Dieter Rams: Functionalist Canon'),
            ('DESIGN-PROCESS', 'Design Process: Brief to Prototype'),
            ('MATERIALS-MANUFACTURING', 'Materials and Manufacturing Constraints'),
            ('ERGONOMICS', 'Ergonomics and Human Factors'),
            ('INTERACTION-DESIGN', 'Product to Interaction Design'),
            ('SUSTAINABILITY', 'Sustainable Design and Circular Economy'),
            ('CONTEMPORARY-PRACTICE', 'Contemporary Practice and Digital Tools'),
            ('DESIGN-CRITICISM', 'Design Criticism and Cultural Theory'),
        ]
    ),
    'marine-biology': (
        'Marine biology: ocean zones, chemosynthesis, bioluminescence, deep sea ecosystems, coral reefs, marine ecology and conservation',
        [
            ('OVERVIEW', 'Landscape and Taxonomy'),
            ('OCEAN-ZONES', 'Ocean Zones and Physical Environment'),
            ('MARINE-ORGANISMS', 'Major Marine Organism Groups'),
            ('CORAL-REEFS', 'Coral Reef Ecosystems'),
            ('OPEN-OCEAN', 'Pelagic Zone and Open Ocean Ecology'),
            ('DEEP-SEA', 'Deep Sea: Hydrothermal Vents and Hadal Zone'),
            ('CHEMOSYNTHESIS', 'Chemosynthesis and Alternative Energy Pathways'),
            ('BIOLUMINESCENCE', 'Bioluminescence: Mechanisms and Functions'),
            ('MARINE-ECOLOGY', 'Marine Food Webs and Trophic Dynamics'),
            ('CONSERVATION', 'Marine Conservation and Anthropogenic Impacts'),
        ]
    ),
    # Batch 8A — History & Ideas
    'logic': (
        'Logic: propositional and predicate logic, proof theory, Godel incompleteness, modal logic, temporal logic, model checking',
        [
            ('OVERVIEW', 'Landscape and Taxonomy'),
            ('PROPOSITIONAL', 'Propositional Logic and Truth Tables'),
            ('PREDICATE', 'First-Order Predicate Logic'),
            ('PROOF-THEORY', 'Proof Theory: Natural Deduction and Sequent Calculus'),
            ('GODEL', "Godel's Incompleteness Theorems"),
            ('MODEL-THEORY', 'Model Theory and Completeness'),
            ('MODAL-LOGIC', 'Modal Logic: Necessity and Possibility'),
            ('TEMPORAL-LOGIC', 'Temporal Logic and Model Checking'),
            ('COMPUTABILITY', 'Logic and Computability: Undecidability'),
            ('APPLICATIONS', 'Applications: Program Verification and AI Reasoning'),
        ]
    ),
    'intellectual-history': (
        'Intellectual history: history of ideas as sociology of knowledge, paradigm shifts, Kuhn and Mannheim, major intellectual movements',
        [
            ('OVERVIEW', 'Landscape and Taxonomy'),
            ('METHODOLOGY', 'Methodology: How to Write the History of Ideas'),
            ('SOCIOLOGY-KNOWLEDGE', 'Sociology of Knowledge: Mannheim and Merton'),
            ('SCIENTIFIC-REVOLUTIONS', 'Scientific Revolutions: Kuhn and Critics'),
            ('ENLIGHTENMENT', 'The Enlightenment and Its Discontents'),
            ('19TH-CENTURY', '19th Century: Darwin, Marx, Nietzsche'),
            ('20TH-CENTURY-PHILOSOPHY', '20th Century Philosophy and Science'),
            ('POSTSTRUCTURALISM', 'Structuralism and Poststructuralism'),
            ('HISTORY-SCIENCE-IDEAS', 'History of Science as Intellectual History'),
            ('CONTEMPORARY', 'Contemporary Intellectual Landscape'),
        ]
    ),
    'social-history': (
        'Social history: Annales school, Braudel\'s longue duree, quantitative history, history from below, material and daily life',
        [
            ('OVERVIEW', 'Landscape and Taxonomy'),
            ('ANNALES-SCHOOL', 'The Annales School and Total History'),
            ('LONGUE-DUREE', "Braudel and the Longue Duree"),
            ('HISTORY-FROM-BELOW', 'History from Below: Workers and Everyday Life'),
            ('QUANTITATIVE-HISTORY', 'Quantitative and Cliometric History'),
            ('GENDER-HISTORY', 'Gender History and Feminist Historiography'),
            ('POSTCOLONIAL', 'Postcolonial and Subaltern History'),
            ('MATERIAL-CULTURE', 'Material Culture and the History of Things'),
            ('MEMORY-HISTORY', 'Collective Memory and Public History'),
            ('DIGITAL-HISTORY', 'Digital History and Big Data Methods'),
        ]
    ),
    # Batch 8B — Engineering
    'manufacturing': (
        'Manufacturing: GD&T, tolerancing, CNC, additive manufacturing, lean/TPS, Industry 4.0 as cyber-physical systems',
        [
            ('OVERVIEW', 'Landscape and Taxonomy'),
            ('GDT-TOLERANCING', 'GD&T and Tolerancing (ASME Y14.5)'),
            ('MACHINING', 'Machining: Turning, Milling, and Grinding'),
            ('CNC-CAM', 'CNC Machining and CAM Programming'),
            ('ADDITIVE', 'Additive Manufacturing: FDM, SLA, DMLS'),
            ('CASTING-FORMING', 'Casting, Forging, and Forming Processes'),
            ('JOINING', 'Joining: Welding, Brazing, and Adhesives'),
            ('LEAN-TPS', 'Lean Manufacturing and the Toyota Production System'),
            ('QUALITY', 'Quality Systems: SPC, Six Sigma, ISO 9001'),
            ('INDUSTRY-40', 'Industry 4.0: Cyber-Physical Manufacturing'),
        ]
    ),
    'systems-engineering': (
        'Systems engineering: V-model, SysML, FMEA, requirements management, large system design as an engineering discipline',
        [
            ('OVERVIEW', 'Landscape and Taxonomy'),
            ('SE-PROCESS', 'Systems Engineering Process and Lifecycle'),
            ('REQUIREMENTS', 'Requirements Engineering and Management'),
            ('ARCHITECTURE', 'System Architecture and Trade Studies'),
            ('V-MODEL', 'The V-Model and Verification/Validation'),
            ('SYSML', 'SysML: Systems Modeling Language'),
            ('FMEA-RELIABILITY', 'FMEA, Fault Trees, and Reliability Engineering'),
            ('INTERFACE-MANAGEMENT', 'Interface Management and Integration'),
            ('MBSE', 'Model-Based Systems Engineering (MBSE)'),
            ('CASE-STUDIES', 'Case Studies: Aerospace, Defense, and Software'),
        ]
    ),
    'materials-processing': (
        'Materials processing: TTT diagrams, heat treatment, fracture mechanics, bridge between materials science and manufacturing',
        [
            ('OVERVIEW', 'Landscape and Taxonomy'),
            ('PHASE-TRANSFORMATIONS', 'Phase Transformations and TTT/CCT Diagrams'),
            ('HEAT-TREATMENT', 'Heat Treatment: Annealing, Quenching, Tempering'),
            ('SOLIDIFICATION', 'Solidification and Casting Metallurgy'),
            ('DEFORMATION', 'Plastic Deformation and Work Hardening'),
            ('FRACTURE-MECHANICS', 'Fracture Mechanics and Fatigue'),
            ('SURFACE-TREATMENT', 'Surface Treatments and Coatings'),
            ('POWDER-PROCESSING', 'Powder Processing and Sintering'),
            ('POLYMERS-PROCESSING', 'Polymer Processing: Extrusion, Molding'),
            ('CHARACTERIZATION', 'Materials Characterization Techniques'),
        ]
    ),
    # Batch 8C — Social Sciences
    'criminology': (
        'Criminology: rational choice, strain theory, white-collar crime, mass incarceration, desistance, criminal justice policy',
        [
            ('OVERVIEW', 'Landscape and Taxonomy'),
            ('CLASSICAL-THEORIES', 'Classical and Rational Choice Theories'),
            ('STRAIN-ANOMIE', 'Strain Theory and Anomie'),
            ('SOCIAL-CONTROL', 'Social Control and Labeling Theory'),
            ('WHITE-COLLAR', 'White-Collar Crime: Sutherland and Beyond'),
            ('ORGANIZED-CRIME', 'Organized Crime and Networks'),
            ('POLICING', 'Policing: Strategies, Bias, and Reform'),
            ('INCARCERATION', 'Mass Incarceration as Policy Choice'),
            ('DESISTANCE', 'Desistance, Reentry, and Rehabilitation'),
            ('COMPARATIVE', 'Comparative Criminology and International Systems'),
        ]
    ),
    'media-studies': (
        "Media studies: McLuhan's tetrad, Frankfurt School, Baudrillard simulacra, platform capitalism, attention economy",
        [
            ('OVERVIEW', 'Landscape and Taxonomy'),
            ('MEDIUM-IS-MESSAGE', "McLuhan: Medium Is the Message and the Tetrad"),
            ('FRANKFURT-SCHOOL', 'Frankfurt School and Critical Theory'),
            ('BAUDRILLARD', 'Baudrillard: Simulacra and Hyperreality'),
            ('POLITICAL-ECONOMY', 'Political Economy of Media'),
            ('PLATFORM-CAPITALISM', 'Platform Capitalism and the Attention Economy'),
            ('JOURNALISM', 'Journalism: Norms, Crisis, and Digital Disruption'),
            ('AUDIENCES', 'Audiences, Reception, and Participatory Culture'),
            ('ALGORITHMS', 'Algorithmic Media and Filter Bubbles'),
            ('GLOBAL-MEDIA', 'Global Media Flows and Cultural Imperialism'),
        ]
    ),
    'education': (
        'Education: spacing effect, retrieval practice, Piaget, Vygotsky, learning theory, MOOC crisis, educational technology',
        [
            ('OVERVIEW', 'Landscape and Taxonomy'),
            ('LEARNING-THEORY', 'Learning Theory: Behaviorism to Constructivism'),
            ('PIAGET-VYGOTSKY', 'Piaget, Vygotsky, and Developmental Learning'),
            ('COGNITIVE-SCIENCE-EDU', 'Cognitive Science Applied: Spacing and Retrieval'),
            ('CURRICULUM', 'Curriculum Design and Learning Objectives'),
            ('ASSESSMENT', 'Assessment: Formative, Summative, and Authentic'),
            ('HIGHER-EDUCATION', 'Higher Education: Structure and Crises'),
            ('MOOCS-DIGITAL', 'MOOCs, EdTech, and the Completion Crisis'),
            ('EQUITY', 'Equity, Access, and the Sociology of Education'),
            ('FUTURE-LEARNING', 'The Future of Learning: AI Tutors and Personalization'),
        ]
    ),
    # Batch 8D — Language & Communication / Computing
    'philosophy-of-language': (
        "Philosophy of language: Frege's sense/reference, Russell, Wittgenstein, speech acts, possible worlds semantics, formal semantics",
        [
            ('OVERVIEW', 'Landscape and Taxonomy'),
            ('FREGE', "Frege: Sense, Reference, and Concept Script"),
            ('RUSSELL', "Russell: Descriptions and Logical Atomism"),
            ('EARLY-WITTGENSTEIN', 'Early Wittgenstein: Tractatus and Picture Theory'),
            ('LATE-WITTGENSTEIN', 'Late Wittgenstein: Language Games and Meaning as Use'),
            ('SPEECH-ACTS', 'Speech Act Theory: Austin and Searle'),
            ('POSSIBLE-WORLDS', 'Possible Worlds Semantics: Kripke and Lewis'),
            ('FORMAL-SEMANTICS', 'Formal Semantics: Montague Grammar'),
            ('PRAGMATICS', 'Pragmatics: Grice and Implicature'),
            ('COMPUTING-BRIDGE', 'Language and Computing: Formal Semantics to Type Theory'),
        ]
    ),
    'semiotics': (
        'Semiotics: Saussure vs Peirce, structuralism, post-structuralism, sign systems, cultural semiotics',
        [
            ('OVERVIEW', 'Landscape and Taxonomy'),
            ('SAUSSURE', 'Saussure: Sign, Signifier, Signified'),
            ('PEIRCE', 'Peirce: Icon, Index, Symbol'),
            ('STRUCTURALISM', 'Structuralism and the Prague School'),
            ('BARTHES', 'Barthes: Myth, Connotation, and Cultural Signs'),
            ('POST-STRUCTURALISM', 'Derrida and Deconstruction'),
            ('NARRATIVE-SEMIOTICS', 'Narrative Semiotics: Greimas and Propp'),
            ('VISUAL-SEMIOTICS', 'Visual and Film Semiotics'),
            ('CULTURAL-SEMIOTICS', 'Cultural Semiotics: Lotman and the Semiosphere'),
            ('APPLICATIONS', 'Semiotic Applications: Advertising, Architecture, Code'),
        ]
    ),
    'computer-architecture': (
        'Computer architecture: ISA/microarchitecture split, x86/ARM/RISC-V, pipelining, cache coherence, GPU SIMT model',
        [
            ('OVERVIEW', 'Landscape and Taxonomy'),
            ('ISA-FUNDAMENTALS', 'ISA Fundamentals: RISC vs CISC'),
            ('X86-ARCHITECTURE', 'x86 and x86-64 Architecture'),
            ('ARM-RISC-V', 'ARM and RISC-V: Modern RISC Designs'),
            ('PIPELINING', 'Pipelining: Stages, Hazards, and Forwarding'),
            ('MEMORY-HIERARCHY', 'Memory Hierarchy: Caches to DRAM'),
            ('CACHE-COHERENCE', 'Cache Coherence and Memory Consistency'),
            ('SUPERSCALAR-OOO', 'Superscalar and Out-of-Order Execution'),
            ('GPU-ARCHITECTURE', 'GPU Architecture and SIMT Execution Model'),
            ('FUTURE-ARCHITECTURE', 'Future Architectures: Neuromorphic, Quantum, Accelerators'),
        ]
    ),
    # Batch 9A — Natural World
    'entomology': (
        'Entomology: insect diversity, eusociality, metamorphosis, insect-plant interactions, pollination crisis, economic entomology',
        [
            ('OVERVIEW', 'Landscape and Taxonomy'),
            ('INSECT-BODY-PLAN', 'Insect Body Plan and Physiology'),
            ('DIVERSITY-CLASSIFICATION', 'Diversity and Classification: Major Orders'),
            ('METAMORPHOSIS', 'Metamorphosis: Complete and Incomplete'),
            ('EUSOCIALITY', 'Eusociality: Ants, Bees, Wasps, and Termites'),
            ('INSECT-PLANT', 'Insect-Plant Interactions and Coevolution'),
            ('POLLINATION', 'Pollination Biology and Pollinator Decline'),
            ('INSECT-ECOLOGY', 'Insect Ecology and Population Dynamics'),
            ('ECONOMIC-ENTOMOLOGY', 'Economic Entomology: Pests and Biocontrol'),
            ('FORENSIC-MEDICAL', 'Forensic and Medical Entomology'),
        ]
    ),
    'ornithology': (
        'Ornithology: avian evolution, flight mechanics, migration, song and communication, biogeography, conservation',
        [
            ('OVERVIEW', 'Landscape and Taxonomy'),
            ('AVIAN-EVOLUTION', 'Avian Evolution: Theropods to Modern Birds'),
            ('FLIGHT-MECHANICS', 'Flight Mechanics and Wing Morphology'),
            ('SYSTEMATICS', 'Systematics and Major Groups'),
            ('MIGRATION', 'Migration: Navigation and Orientation'),
            ('SONG-COMMUNICATION', 'Bird Song and Communication'),
            ('BREEDING', 'Breeding Systems and Parental Care'),
            ('ECOLOGY-FORAGING', 'Ecology and Foraging Strategies'),
            ('BIOGEOGRAPHY', 'Biogeography and Island Biology'),
            ('CONSERVATION', 'Conservation: Decline, Threats, and Recovery'),
        ]
    ),
    'zoology': (
        'Zoology: animal body plans, comparative physiology, ethology, Tinbergens four questions, Conway Morris vs Gould on convergence',
        [
            ('OVERVIEW', 'Landscape and Taxonomy'),
            ('ANIMAL-DIVERSITY', 'Animal Diversity and Phylogeny'),
            ('BODY-PLANS', 'Body Plans: Symmetry, Segmentation, Coelom'),
            ('COMPARATIVE-PHYSIOLOGY', 'Comparative Physiology'),
            ('ETHOLOGY', "Ethology: Tinbergen's Four Questions"),
            ('BEHAVIORAL-ECOLOGY', 'Behavioral Ecology and Sociobiology'),
            ('CONVERGENT-EVOLUTION', 'Convergent Evolution: Conway Morris vs Gould'),
            ('DEVELOPMENT', 'Animal Development and Evo-Devo'),
            ('ECOLOGY-NICHES', 'Ecology, Niches, and Trophic Roles'),
            ('CONSERVATION-ZOOLOGY', 'Conservation Zoology and Defaunation'),
        ]
    ),
    # Batch 9B — Earth & Space
    'planetary-science': (
        'Planetary science: Nice model, comparative planetology, Venus as cautionary tale, exoplanet demographics from Kepler',
        [
            ('OVERVIEW', 'Landscape and Taxonomy'),
            ('SOLAR-SYSTEM-FORMATION', 'Solar System Formation: Nice Model and Grand Tack'),
            ('TERRESTRIAL-PLANETS', 'Terrestrial Planets: Comparative Planetology'),
            ('VENUS', 'Venus: Runaway Greenhouse and Cautionary Tale'),
            ('MARS', 'Mars: Geology, Climate, and Habitability'),
            ('GAS-GIANT-ICE-GIANT', 'Giant Planets and Ice Giants'),
            ('SMALL-BODIES', 'Small Bodies: Asteroids, Comets, and KBOs'),
            ('EXOPLANETS', 'Exoplanet Detection and Demographics'),
            ('HABITABILITY', 'Planetary Habitability and the HZ'),
            ('PLANETARY-INTERIORS', 'Planetary Interiors and Magnetic Fields'),
        ]
    ),
    'geochemistry': (
        'Geochemistry: U-Pb geochronology, stable isotope paleoproxies, carbon isotope excursions, element cycling',
        [
            ('OVERVIEW', 'Landscape and Taxonomy'),
            ('ELEMENT-DISTRIBUTION', 'Element Distribution and Geochemical Reservoirs'),
            ('ISOTOPE-SYSTEMS', 'Isotope Systems: Radiogenic and Stable'),
            ('GEOCHRONOLOGY', 'Geochronology: U-Pb, Ar-Ar, and Other Systems'),
            ('STABLE-ISOTOPE-PALEO', 'Stable Isotope Paleoclimatology'),
            ('CARBON-CYCLE', 'Carbon Cycle Geochemistry'),
            ('HYDROTHERMAL', 'Hydrothermal Systems and Ore Formation'),
            ('WEATHERING-SOILS', 'Weathering, Soils, and Regolith'),
            ('OCEAN-GEOCHEMISTRY', 'Ocean Geochemistry and the Marine Record'),
            ('PLANETARY-GEOCHEMISTRY', 'Planetary Geochemistry and Cosmochemistry'),
        ]
    ),
    'space-exploration': (
        'Space exploration: Tsiolkovsky equation, specific impulse, staging, launch vehicles, SpaceX reusability, mission design',
        [
            ('OVERVIEW', 'Landscape and Taxonomy'),
            ('ORBITAL-MECHANICS', 'Orbital Mechanics and the Rocket Equation'),
            ('PROPULSION', 'Propulsion Systems: Chemical to Electric'),
            ('LAUNCH-VEHICLES', 'Launch Vehicles: Evolution and Architecture'),
            ('REUSABILITY', 'Reusability Revolution: SpaceX and Beyond'),
            ('SPACECRAFT-DESIGN', 'Spacecraft Design and Subsystems'),
            ('MISSION-DESIGN', 'Mission Design: Interplanetary Trajectories'),
            ('HUMAN-SPACEFLIGHT', 'Human Spaceflight: Physiology and Life Support'),
            ('SPACE-ECONOMY', 'Space Economy: Commercial Space and New Space'),
            ('FUTURE-EXPLORATION', 'Future Exploration: Moon, Mars, and Beyond'),
        ]
    ),
    # Batch 9C — Material Culture
    'plastics-polymers': (
        'Plastics and polymers: polymer chemistry, Tg, crystallinity, major plastics families, injection molding, microplastics, bioplastics',
        [
            ('OVERVIEW', 'Landscape and Taxonomy'),
            ('POLYMER-CHEMISTRY', 'Polymer Chemistry: Chains, Mw/Mn, and Tg'),
            ('THERMOPLASTICS', 'Major Thermoplastics: PE, PP, PET, PS, PVC'),
            ('THERMOSETS', 'Thermosets: Epoxies, Polyurethanes, Phenolics'),
            ('ELASTOMERS', 'Elastomers: Natural and Synthetic Rubber'),
            ('PROCESSING', 'Processing: Injection Molding, Extrusion, Blow Molding'),
            ('ADDITIVES', 'Additives: Stabilizers, Plasticizers, Fillers'),
            ('ENVIRONMENTAL', 'Environmental Impact and Microplastics'),
            ('BIOPLASTICS', 'Bioplastics: Promises, Reality, and Limits'),
            ('ADVANCED-POLYMERS', 'Advanced Polymers: Engineering and High-Performance'),
        ]
    ),
    'papermaking': (
        'Papermaking: Cai Lun to Fourdrinier, Kraft process, paper chemistry, archival paper, digital disruption',
        [
            ('OVERVIEW', 'Landscape and Taxonomy'),
            ('HISTORY', 'History: Cai Lun Through the Fourdrinier Machine'),
            ('RAW-MATERIALS', 'Raw Materials: Wood Pulp, Cotton, and Alternatives'),
            ('KRAFT-PROCESS', 'The Kraft Process: Chemical Pulping'),
            ('PAPER-MACHINE', 'The Paper Machine: Forming, Pressing, Drying'),
            ('PAPER-CHEMISTRY', 'Paper Chemistry: Sizing, Coating, and Finishing'),
            ('ARCHIVAL-PAPER', 'Archival and Conservation Paper'),
            ('SPECIALTY-PAPERS', 'Specialty Papers: Technical and Security Papers'),
            ('DIGITAL-DISRUPTION', 'Digital Disruption and the Paper Industry'),
            ('SUSTAINABILITY', 'Sustainability: Recycling, Certification, and Alternatives'),
        ]
    ),
    'composite-materials': (
        'Composite materials: classical laminate theory, prepreg/autoclave, carbon fiber, Boeing 787 case study, end-of-life challenges',
        [
            ('OVERVIEW', 'Landscape and Taxonomy'),
            ('FUNDAMENTALS', 'Composite Fundamentals: Matrix, Fiber, Interface'),
            ('FIBER-TYPES', 'Fiber Types: Carbon, Glass, Aramid, Natural'),
            ('MATRIX-SYSTEMS', 'Matrix Systems: Thermoset and Thermoplastic'),
            ('LAMINATE-THEORY', 'Classical Laminate Theory (CLT)'),
            ('MANUFACTURING', 'Manufacturing: Prepreg, Autoclave, and Infusion'),
            ('DESIGN-ANALYSIS', 'Structural Design and Analysis'),
            ('BOEING-787', 'Case Study: Boeing 787 Dreamliner'),
            ('DAMAGE-INSPECTION', 'Damage Mechanics and NDT Inspection'),
            ('END-OF-LIFE', 'End-of-Life: Recycling and Sustainability'),
        ]
    ),
    # Batch 9D — Arts & Culture
    'graphic-design': (
        'Graphic design: Bauhaus to Swiss Style to digital, grid systems, typography in design, brand identity, UX connections',
        [
            ('OVERVIEW', 'Landscape and Taxonomy'),
            ('BAUHAUS', 'Bauhaus: Total Design and the School'),
            ('SWISS-STYLE', 'Swiss/International Style: Grid and Helvetica'),
            ('AMERICAN-MODERNISM', 'American Modernism: Rand, Bass, and Glaser'),
            ('GRID-SYSTEMS', 'Grid Systems and Layout'),
            ('TYPOGRAPHY-DESIGN', 'Typography in Graphic Design'),
            ('COLOR-IN-DESIGN', 'Color Theory and Brand'),
            ('BRAND-IDENTITY', 'Brand Identity Systems'),
            ('DIGITAL-TRANSITION', 'Digital Transition: Screen and Web Design'),
            ('CONTEMPORARY', 'Contemporary Practice and Tools'),
        ]
    ),
    'fashion': (
        'Fashion: couture system, ready-to-wear, fast fashion economics, Zara model, Rana Plaza, sustainability crisis',
        [
            ('OVERVIEW', 'Landscape and Taxonomy'),
            ('COUTURE-SYSTEM', 'The Haute Couture System'),
            ('RTW-PRÊT', "Ready-to-Wear and Prêt-à-Porter"),
            ('FASHION-HISTORY', 'Fashion History: Key Movements and Designers'),
            ('FASHION-INDUSTRY', 'The Fashion Industry: Supply Chain and Economics'),
            ('FAST-FASHION', 'Fast Fashion: Zara Model and Disruption'),
            ('RANA-PLAZA', 'Rana Plaza and the Ethics of Fashion'),
            ('SUSTAINABILITY', 'Sustainable Fashion: Materials and Circular Models'),
            ('FASHION-THEORY', 'Fashion Theory: Meaning, Identity, and Culture'),
            ('DIGITAL-FASHION', 'Digital Fashion and Virtual Dress'),
        ]
    ),
    'comics-sequential-art': (
        'Comics and sequential art: McCloud closure theory, panel transitions, Maus as turning point, manga as global phenomenon',
        [
            ('OVERVIEW', 'Landscape and Taxonomy'),
            ('HISTORY-FORM', 'History of Comics as a Form'),
            ('MCCLOUD-THEORY', "McCloud's Understanding Comics: Closure and Transitions"),
            ('PANEL-GRAMMAR', 'Panel Grammar: Gutters, Time, and Space'),
            ('SUPERHERO-TRADITION', 'The Superhero Tradition: Golden to Modern Age'),
            ('ALTERNATIVE-COMICS', 'Alternative and Underground Comics'),
            ('MAUS-LITERARY', "Maus and Comics' Literary Turn"),
            ('MANGA', 'Manga: Japanese Comics as Global Phenomenon'),
            ('GRAPHIC-NOVEL', 'The Graphic Novel as Form'),
            ('DIGITAL-WEBCOMICS', 'Digital Comics and Webcomics'),
        ]
    ),
    # Batch 10A — Computing / Life Sciences
    'machine-learning-theory': (
        'ML theory: PAC learning, VC dimension, Rademacher complexity, neural tangent kernel, double descent, generalization bounds',
        [
            ('OVERVIEW', 'Landscape and Taxonomy'),
            ('PAC-LEARNING', 'PAC Learning: Valiant Framework'),
            ('VC-DIMENSION', 'VC Dimension and Shattering'),
            ('RADEMACHER', 'Rademacher Complexity and Uniform Convergence'),
            ('BIAS-VARIANCE', 'Bias-Variance Tradeoff and Model Selection'),
            ('KERNEL-METHODS', 'Kernel Methods and Reproducing Kernel Hilbert Spaces'),
            ('NEURAL-TANGENT', 'Neural Tangent Kernel and Infinite-Width Networks'),
            ('DOUBLE-DESCENT', 'Double Descent and Modern ML Phenomenology'),
            ('INFORMATION-THEORETIC', 'Information-Theoretic Bounds'),
            ('OPEN-PROBLEMS', 'Open Problems in ML Theory'),
        ]
    ),
    'pharmacology': (
        'Pharmacology: PK/PD, ADME, CYP metabolism, receptor theory, drug development pipeline, deeper than medicine drug overview',
        [
            ('OVERVIEW', 'Landscape and Taxonomy'),
            ('RECEPTOR-THEORY', 'Receptor Theory: Agonists, Antagonists, Affinity'),
            ('PHARMACOKINETICS', 'Pharmacokinetics: ADME'),
            ('PHARMACODYNAMICS', 'Pharmacodynamics: Dose-Response and EC50'),
            ('CYP-METABOLISM', 'CYP450 Metabolism and Drug Interactions'),
            ('CNS-PHARMACOLOGY', 'CNS Pharmacology: Neurotransmitters and Targets'),
            ('CARDIOVASCULAR', 'Cardiovascular Pharmacology'),
            ('CHEMOTHERAPY', 'Cancer Pharmacology and Chemotherapy'),
            ('DRUG-DEVELOPMENT', 'Drug Development: Discovery to Approval'),
            ('PERSONALIZED', 'Pharmacogenomics and Personalized Medicine'),
        ]
    ),
    'developmental-biology': (
        'Developmental biology: Wnt/Notch/Hedgehog signaling, HOX genes, gastrulation, organogenesis, iPSCs, regeneration',
        [
            ('OVERVIEW', 'Landscape and Taxonomy'),
            ('FERTILIZATION-CLEAVAGE', 'Fertilization, Cleavage, and Blastulation'),
            ('GASTRULATION', 'Gastrulation and Germ Layer Formation'),
            ('SIGNALING-PATHWAYS', 'Signaling Pathways: Wnt, Notch, Hedgehog'),
            ('HOX-GENES', 'HOX Genes and Axial Patterning'),
            ('ORGANOGENESIS', 'Organogenesis: How Organs Form'),
            ('NEURAL-DEVELOPMENT', 'Neural Development and Brain Formation'),
            ('STEM-CELLS', 'Stem Cells: Pluripotency and Differentiation'),
            ('IPSCS', 'iPSCs: Yamanaka Factors and Reprogramming'),
            ('REGENERATION', 'Regeneration: From Planaria to Mammals'),
        ]
    ),
    # Batch 10B — History & Ideas / Language
    'political-history': (
        'Political history: revolution theory, imperialism, decolonization, Cold War historiography, democratic backsliding',
        [
            ('OVERVIEW', 'Landscape and Taxonomy'),
            ('REVOLUTION-THEORY', "Revolution Theory: Skocpol's Structural Analysis"),
            ('IMPERIALISM', 'Imperialism: Theories and Case Studies'),
            ('WORLD-WARS', 'The World Wars as Historical Rupture'),
            ('DECOLONIZATION', 'Decolonization: 1947 to 1975'),
            ('COLD-WAR', 'Cold War Historiography'),
            ('POSTWAR-ORDER', 'The Postwar Liberal Order'),
            ('DEMOCRATIC-BACKSLIDING', 'Democratic Backsliding: Causes and Patterns'),
            ('AUTHORITARIAN-RESURGENCE', 'Authoritarian Resurgence in the 21st Century'),
            ('HISTORIOGRAPHY', 'Historiography: How Political History Is Written'),
        ]
    ),
    'translation': (
        'Translation: the equivalence problem, Bible translation history, Nabokov literalism, neural MT and BLEU scores, untranslatability',
        [
            ('OVERVIEW', 'Landscape and Taxonomy'),
            ('EQUIVALENCE-PROBLEM', 'The Equivalence Problem: What Is Translation?'),
            ('HISTORY-TRANSLATION', 'History of Translation: Cicero to Jerome to Luther'),
            ('BIBLE-TRANSLATION', 'Bible Translation: Vulgate, Luther, KJV'),
            ('LITERARY-TRANSLATION', 'Literary Translation: Fidelity and Freedom'),
            ('NABOKOV', "Nabokov's Radical Literalism"),
            ('UNTRANSLATABILITY', 'Untranslatability and the Limits of Language'),
            ('INTERPRETATION', 'Simultaneous and Consecutive Interpretation'),
            ('MACHINE-TRANSLATION', 'Machine Translation: Rule-Based to Neural'),
            ('BLEU-NMT', 'Neural MT, BLEU Scores, and What They Miss'),
        ]
    ),
    'international-relations': (
        'International relations: Waltz vs Mearsheimer vs Wendt, nuclear deterrence, power transition theory, global governance',
        [
            ('OVERVIEW', 'Landscape and Taxonomy'),
            ('REALISM', 'Realism: Morgenthau, Waltz, and Mearsheimer'),
            ('LIBERALISM', 'Liberalism and Liberal Institutionalism'),
            ('CONSTRUCTIVISM', "Constructivism: Wendt's Social Theory of IR"),
            ('NUCLEAR-DETERRENCE', 'Nuclear Deterrence: MAD, Credibility, and Extended Deterrence'),
            ('POWER-TRANSITION', 'Power Transition Theory and Hegemonic Wars'),
            ('INTERNATIONAL-INSTITUTIONS', 'International Institutions: UN, WTO, IMF'),
            ('GLOBAL-GOVERNANCE', 'Global Governance and the Multilateral Order'),
            ('FOREIGN-POLICY', 'Foreign Policy Analysis'),
            ('CONTEMPORARY-IR', 'Contemporary IR: China, US, and the New Order'),
        ]
    ),
    # Batch 10C — Material / Natural / Arts
    'furniture': (
        'Furniture: joinery as applied geometry, Bauhaus tubular steel, Eames as engineering, IKEA KD model, design history',
        [
            ('OVERVIEW', 'Landscape and Taxonomy'),
            ('WOOD-JOINERY', 'Wood and Joinery: Applied Geometry'),
            ('HISTORY-STYLES', 'Furniture History: Period Styles to Modernism'),
            ('BAUHAUS-MODERNISM', 'Bauhaus and Modernist Furniture'),
            ('EAMES-ENGINEERING', 'Eames: Furniture as Engineering Problem'),
            ('SCANDINAVIAN', 'Scandinavian Design Tradition'),
            ('MATERIALS-MODERN', 'Modern Materials: Plastics, Steel, and Plywood'),
            ('IKEA-MODEL', 'IKEA and Flat-Pack as Industrial Design'),
            ('ERGONOMICS-SEATING', 'Ergonomics of Seating'),
            ('CONTEMPORARY', 'Contemporary Furniture Design and Digital Fabrication'),
        ]
    ),
    'horticulture': (
        'Horticulture: plant propagation, grafting, tissue culture, soil science, IPM, controlled environment agriculture',
        [
            ('OVERVIEW', 'Landscape and Taxonomy'),
            ('PLANT-PROPAGATION', 'Plant Propagation: Seeds, Cuttings, Division'),
            ('GRAFTING', 'Grafting and Budding Techniques'),
            ('TISSUE-CULTURE', 'Tissue Culture and Micropropagation'),
            ('SOIL-SCIENCE', 'Soil Science for Horticulture'),
            ('NUTRITION-IRRIGATION', 'Plant Nutrition and Irrigation'),
            ('IPM', 'Integrated Pest Management (IPM)'),
            ('PRUNING-TRAINING', 'Pruning, Training, and Espalier'),
            ('CONTROLLED-ENVIRONMENT', 'Controlled Environment Agriculture: Greenhouses and Vertical Farms'),
            ('LANDSCAPE-DESIGN', 'Landscape Design Principles'),
        ]
    ),
    'sports-science': (
        'Sports science: VO2max, lactate threshold, periodization, sports psychology, flow state, doping biochemistry',
        [
            ('OVERVIEW', 'Landscape and Taxonomy'),
            ('EXERCISE-PHYSIOLOGY', 'Exercise Physiology: Energy Systems'),
            ('VO2MAX', 'VO2max, Lactate Threshold, and Aerobic Capacity'),
            ('STRENGTH-POWER', 'Strength and Power: Neuromuscular Adaptations'),
            ('BIOMECHANICS', 'Biomechanics and Movement Analysis'),
            ('TRAINING-PERIODIZATION', 'Training Theory and Periodization'),
            ('NUTRITION-PERFORMANCE', 'Sports Nutrition and Ergogenic Aids'),
            ('DOPING', 'Doping Biochemistry: Mechanisms and Detection'),
            ('SPORTS-PSYCHOLOGY', 'Sports Psychology: Flow, Motivation, and Anxiety'),
            ('REHABILITATION', 'Injury, Rehabilitation, and Return-to-Play'),
        ]
    ),
    # Batch 10D — Earth & Space / History & Ideas
    'astrobiology': (
        'Astrobiology: RNA world, hydrothermal vents, extremophile envelope, Fermi paradox, biosignature detection, JWST',
        [
            ('OVERVIEW', 'Landscape and Taxonomy'),
            ('ORIGIN-OF-LIFE', 'Origin of Life: RNA World and Hydrothermal Vents'),
            ('EXTREMOPHILES', 'Extremophiles and the Limits of Life'),
            ('HABITABLE-ENVIRONMENTS', 'Habitable Environments in the Solar System'),
            ('BIOSIGNATURES', 'Biosignatures: What to Look For'),
            ('JWST-DETECTION', 'JWST and Atmospheric Characterization'),
            ('FERMI-PARADOX', 'The Fermi Paradox and SETI'),
            ('DIRECTED-PANSPERMIA', 'Panspermia and Life Distribution'),
            ('SYNTHETIC-BIOLOGY', 'Synthetic Biology and Astrobiology'),
            ('FUTURE-MISSIONS', 'Future Missions: Europa, Enceladus, and Beyond'),
        ]
    ),
    'philosophy-of-mind': (
        "Philosophy of mind: Chalmers' hard problem, Chinese Room, functionalism, qualia, free will, AI consciousness",
        [
            ('OVERVIEW', 'Landscape and Taxonomy'),
            ('MIND-BODY-PROBLEM', 'The Mind-Body Problem: Historical Overview'),
            ('FUNCTIONALISM', 'Functionalism and Multiple Realizability'),
            ('HARD-PROBLEM', "Chalmers' Hard Problem of Consciousness"),
            ('CHINESE-ROOM', "Searle's Chinese Room Argument"),
            ('QUALIA-PHENOMENOLOGY', 'Qualia and Phenomenal Consciousness'),
            ('FREE-WILL', 'Free Will, Determinism, and Moral Responsibility'),
            ('ELIMINATIVISM', 'Eliminative Materialism and Folk Psychology'),
            ('EMBODIED-COGNITION', 'Embodied and Extended Cognition'),
            ('AI-CONSCIOUSNESS', 'AI and Machine Consciousness'),
        ]
    ),
    'ethics': (
        'Ethics: consequentialism, deontology, virtue ethics, Rawls, applied AI ethics, research ethics, metaethics',
        [
            ('OVERVIEW', 'Landscape and Taxonomy'),
            ('METAETHICS', 'Metaethics: Moral Realism and Anti-Realism'),
            ('CONSEQUENTIALISM', 'Consequentialism and Utilitarianism'),
            ('DEONTOLOGY', 'Deontology: Kant and the Categorical Imperative'),
            ('VIRTUE-ETHICS', 'Virtue Ethics: Aristotle and Neo-Aristotelianism'),
            ('RAWLS', "Rawls: A Theory of Justice"),
            ('APPLIED-ETHICS', 'Applied Ethics: Bioethics and Professional Ethics'),
            ('RESEARCH-ETHICS', 'Research Ethics: Nuremberg, Helsinki, and IRBs'),
            ('AI-ETHICS', 'AI Ethics: Alignment, Fairness, and Governance'),
            ('GLOBAL-JUSTICE', 'Global Justice and Cosmopolitanism'),
        ]
    ),
}

created = 0
files_written = 0

for dirname, (description, files) in DIRS.items():
    dirpath = os.path.join(BASE, dirname)
    os.makedirs(dirpath, exist_ok=True)

    # Write STATUS.md
    rows = ''
    for suffix, title in files:
        num = '00' if suffix == 'OVERVIEW' else str(files.index((suffix, title))).zfill(2)
        fname = f'{num}-{suffix}.md'
        rows += f'| {fname:<32} | {title:<55} | 🔜 |\n'

    status_content = f"""# {dirname}/ — Status

## Files

| File                             | Topic                                                    | Status |
|----------------------------------|----------------------------------------------------------|--------|
{rows}
## Coverage Notes

{description}
"""
    with open(os.path.join(dirpath, 'STATUS.md'), 'w', encoding='utf-8') as f:
        f.write(status_content)
    files_written += 1

    # Write content stubs
    for i, (suffix, title) in enumerate(files):
        fname = f'{"00" if suffix == "OVERVIEW" else str(i).zfill(2)}-{suffix}.md'
        stub = f'# {title}\n\n> Stub -- to be written.\n'
        with open(os.path.join(dirpath, fname), 'w', encoding='utf-8') as f:
            f.write(stub)
        files_written += 1

    created += 1
    print(f'  {dirname}/ — {len(files)+1} files')

print(f'\nDone: {created} directories, {files_written} files')
