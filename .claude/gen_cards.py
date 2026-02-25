#!/usr/bin/env python3
"""Generate 52 tarot-style card files — one per MAXIM volume."""

import os

OUT = os.path.join(os.path.dirname(__file__), '..', 'cards')
os.makedirs(OUT, exist_ok=True)

INNER = 47   # characters inside the box borders
TOP    = '╔' + '═' * INNER + '╗'
MID    = '╠' + '═' * INNER + '╣'
BOT    = '╚' + '═' * INNER + '╝'

SUITS = {
    'C': ('♣', 'Foundation'),
    'D': ('♦', 'Application'),
    'H': ('♥', 'Depth'),
    'S': ('♠', 'Frontier'),
}
SUIT_ORDER = ['C', 'D', 'H', 'S']

RANKS = {
    '2':  'Natural World',
    '3':  'Earth & Space',
    '4':  'Material Culture',
    '5':  'Life Sciences',
    '6':  'History & Ideas',
    '7':  'Mechanics',
    '8':  'Technology',
    '9':  'Social Sciences',
    '10': 'Language & Communication',
    'J':  'Mathematics & Physics',
    'Q':  'Arts & Culture',
    'K':  'Computing & Software',
    'A':  'People',
}
RANK_ABBR = {
    '2': 'NW', '3': 'ES', '4': 'MC', '5': 'LS',
    '6': 'HI', '7': 'M',  '8': 'T',  '9': 'SS',
    '10': 'LC', 'J': 'MP', 'Q': 'AC', 'K': 'C', 'A': 'P',
}

def row(content):
    c = content.ljust(INNER)[:INNER]
    return '║' + c + '║'

def ctr(text):
    return row(text.center(INNER))

def wrap_motto(motto):
    """Wrap motto into lines fitting INNER-2 chars (with 2-space indent)."""
    max_w = INNER - 2
    words = motto.split()
    lines, cur = [], ''
    for w in words:
        if cur:
            trial = cur + ' ' + w
        else:
            trial = w
        if len(trial) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

def render_card(rank, suit_key, dirs, art, motto):
    sym, suit_name = SUITS[suit_key]
    section = RANKS[rank]
    abbr = RANK_ABBR[rank]
    vol_roman = ['', 'I', 'II', 'III', 'IV'][SUIT_ORDER.index(suit_key) + 1]
    vol_label = f'{abbr}·{vol_roman}'

    # Header line: "rank sym" on left, vol_label on right
    left  = f'{rank}{sym}'
    right = vol_label
    gap   = INNER - len(left) - len(right)
    header = left + ' ' * gap + right

    # Suit line
    suit_line = f'{sym}  {suit_name}  {sym}'

    lines = []
    lines.append(TOP)
    lines.append(row(header))
    lines.append(ctr(''))
    lines.append(ctr(section.upper()))
    lines.append(ctr(f'── Volume {vol_roman} ──'))
    lines.append(ctr(suit_line))
    lines.append(MID)
    for a in art:
        lines.append(row('  ' + a))
    lines.append(MID)
    # directories — wrap into lines of ~43 chars
    dir_text = ' · '.join(dirs)
    max_dw = INNER - 2
    dir_words = dir_text.split(' · ')
    dlines, dcur = [], ''
    for w in dir_words:
        token = w + '/'
        trial = (dcur + ' · ' + token) if dcur else token
        if len(trial) <= max_dw:
            dcur = trial
        else:
            if dcur:
                dlines.append(dcur)
            dcur = token
    if dcur:
        dlines.append(dcur)
    for dl in dlines:
        lines.append(row('  ' + dl))
    lines.append(MID)
    for ml in wrap_motto(motto):
        lines.append(row('  ' + ml))
    lines.append(BOT)
    return '\n'.join(lines)


# ── Card data ────────────────────────────────────────────────────────────────
# Each entry: (rank, suit, [dirs], [art_lines_7], motto)
# Art lines must be <= 45 chars each (2-char indent added by render_card)

CARDS = [

# ── Natural World ────────────────────────────────────────────────────────────
('2','C',
 ['periodic-table','animal-phylogeny','spices','food-plants'],
 ['  H  He                    Li Be ...',
  ' ───────────────────────────────────',
  '  Animalia → Chordata → Mammalia',
  '  Plantae  → Angiosperms → Poaceae',
  '  ┌cinnamon┐ ┌pepper┐ ┌turmeric┐',
  '  └Cinnamomum┘ └Piper┘ └Curcuma┘',
  '  Root · Bark · Seed · Leaf · Fruit'],
 'The immediate world: named, tasted, classified.'),

('2','D',
 ['culinary-history','fermentation-spirits','mycology','marine-biology'],
 ['  ~  clay pot  ~  fire  ~  grain  ~',
  '  yeast → CO2 + ethanol (Pasteur)',
  '  Agaricus ── Amanita ── Morchella',
  '           mycelium web',
  '  ≈≈≈≈≈≈≈ ocean surface ≈≈≈≈≈≈≈≈',
  '  fish ── coral ── plankton bloom',
  '  salt · ferment · preserve · eat'],
 'Fire, yeast, and salt — the first chemistry.'),

('2','H',
 ['entomology','ornithology','zoology','horticulture'],
 ['  Insecta: ~6M spp — 75% of fauna',
  '  ╔wing venation╗ ╔compound eye╗',
  '  ♦ Passerines: 6,000 spp songbirds',
  '  Mammalia · Reptilia · Amphibia',
  '  ┌─ canopy ─┐ ┌─ shrub ─┐',
  '  └─ ground ─┘ └─ root ──┘',
  '  Graft · Prune · Propagate · Train'],
 'Six million insect species and a garden.'),

('2','S',
 ['dendrology','freshwater-biology','soil-science','coral-reefs'],
 ['  Oak 500yr ── Redwood 2000yr',
  '  Xylem ↑ water  Phloem ↓ sugar',
  '  ~~~~ river ~~~~ lake ~~~~ bog ~~~~',
  '  Caddisfly · Mayfly · Diatom',
  '  O horizon (humus) ── A (topsoil)',
  '  B (subsoil) ──────── C (bedrock)',
  '  Polyp → coral head → atoll reef'],
 'Forest, stream, soil, reef — living systems at depth.'),

# ── Earth & Space ────────────────────────────────────────────────────────────
('3','C',
 ['astronomy','geology','paleontology'],
 ['  ★ Main sequence: O B A F G K M',
  '  ◎ Sun → red giant → white dwarf',
  '  Igneous · Sedimentary · Metamorphic',
  '  ══ Crust ══ Mantle ══ Core ══',
  '  Cambrian──Ordovician──Devonian',
  '  Cretaceous──Paleogene──Pleistocene',
  '  Trilobite · Ammonite · Dinosaur'],
 'Stars above, strata below, deep time between.'),

('3','D',
 ['meteorology','climate-science','oceanography','hydrology'],
 ['  ⊂ low ⊃  cold front  ⊂ high ⊃',
  '  Cumulonimbus → tornado → squall',
  '  CO2: 280→420 ppm (1750→2024)',
  '  Thermohaline circulation: 1000yr',
  '  ≈≈≈ thermocline ≈ 200m depth ≈≈≈',
  '  Watershed → river → aquifer → sea',
  '  Evaporation · Condensation · Rain'],
 'The atmosphere moves; the ocean remembers.'),

('3','H',
 ['geography','agriculture','mineralogy','planetary-science'],
 ['  60°N ──── temperate belt ──── 30°N',
  '  Wheat 60M ha · Rice 165M ha',
  '  SiO2 quartz · KAlSi3O8 feldspar',
  '  Mohs 1 (talc) ──────── 10 (diamond)',
  '  Rocky worlds: Venus · Earth · Mars',
  '  Gas giants: Jupiter · Saturn',
  '  Ice worlds: Uranus · Neptune · KBO'],
 'Ground underfoot — from soil to planetary crust.'),

('3','S',
 ['geochemistry','space-exploration','astrobiology','remote-sensing'],
 ['  δ18O fractionation ← mantle plume',
  '  Isotope ratios date rock to ±1Myr',
  '  LEO ── GEO ── L2 ── heliocentric',
  '  O2 + CH4 ← biosignature candidates',
  '  SETI: 1420 MHz (HI line)',
  '  LiDAR pulse → DEM · SAR → InSAR',
  '  Spectroscopy sees exoplanet air'],
 'From mantle isotopes to exoplanet atmospheres.'),

# ── Material Culture ─────────────────────────────────────────────────────────
('4','C',
 ['pigments','coatings','textiles','dyeing-fiber'],
 ['  Ochre→Lead white→Ultramarine→Phthal',
  '  Oil · Acrylic · Tempera · Fresco',
  '  Primer → basecoat → topcoat → clear',
  '  Warp ─── weft ─── twill ─── satin',
  '  Loom: shed · pick · beat · advance',
  '  Madder(red) Indigo(blue) Weld(yellow)',
  '  Mordant fixes dye to protein fiber'],
 'Color made fast: pigment, coat, weave, dye.'),

('4','D',
 ['ceramics','glassmaking','jewelry','metalworking'],
 ['  Clay → bisque 900°C → glaze 1250°C',
  '  Feldspar flux melts silica network',
  '  Sand + soda ash + lime → glass melt',
  '  Blowpipe · pontil · annealing oven',
  '  Au 24k · Ag 925 · Pt 950 · alloys',
  '  Bezel · prong · pavé · channel set',
  '  Forge · anneal · quench · temper'],
 'Fire transforms earth into vessel, lens, ring.'),

('4','H',
 ['plastics-polymers','papermaking','composite-materials','furniture'],
 ['  Monomer → polymer chain → crosslink',
  '  PE · PP · PVC · PS · PET · nylon',
  '  Pulp → screen → press → dry → size',
  '  Cellulose fibers H-bond on cooling',
  '  Carbon fiber + epoxy: high E/ρ',
  '  Dovetail · mortise+tenon · dowel',
  '  Grain direction rules every joint'],
 'Polymer, sheet, laminate, joint — industrial material.'),

('4','S',
 ['woodworking','leatherworking','masonry','rope-cordage'],
 ['  Rip · crosscut · plane · chisel · saw',
  '  Green oak → seasoned → kiln-dried',
  '  Veg-tan · chrome-tan · brain-tan',
  '  Skive · stitch · burnish · finish',
  '  Ashlar · rubble · coursed · bonded',
  '  Header · stretcher · collar joint',
  '  Lay · strand · twist · braid · serve'],
 'Hand, tool, material — craft before industry.'),

# ── Life Sciences ─────────────────────────────────────────────────────────────
('5','C',
 ['natural-sciences','biology','botany','ecology'],
 ['  Atom→Molecule→Cell→Organism→Pop',
  '  Eukaryote: nucleus · ER · Golgi',
  '  6CO2 + 6H2O → C6H12O6 + 6O2',
  '  C3/C4/CAM photosynthesis pathways',
  '  Producer→Consumer→Decomposer',
  '  Trophic efficiency ~10% per level',
  '  Biome: tundra · taiga · tropical'],
 'Life: the chemistry that copies itself.'),

('5','D',
 ['human-biology','neuroscience','cognitive-science','disease'],
 ['  Cortex · Hippocampus · Amygdala',
  '  Neuron: dendrite→soma→axon→synapse',
  '  NT: DA · 5-HT · ACh · GABA · Glu',
  '  Working memory: 7±2 chunks (Miller)',
  '  Heart 100k bpm·yr · Lung 23k L/day',
  '  Pathogen → infection → immune war',
  '  Koch postulates · Bradford-Hill'],
 'Brain, body, mind — the human instrument.'),

('5','H',
 ['medicine','nutrition','genomics','immunology','microbiology'],
 ['  dx: H&P → labs → imaging → biopsy',
  '  EBM: RCT → meta-analysis → NNT',
  '  Macro: CHO · Pro · Fat · H2O',
  '  Micro: Fe · Zn · vit D · B12',
  '  Genome 3.2 Gb · ~20k genes · SNPs',
  '  B cell → plasma → IgG antibody',
  '  Bacteria · Fungi · Protozoa · Prion'],
 'Reading the body: genome, microbe, immune defense.'),

('5','S',
 ['evolutionary-biology','virology','biophysics','pharmacology','developmental-biology'],
 ['  LUCA → Bacteria · Archaea · Eukarya',
  '  Drift · Selection · Mutation · Flow',
  '  Capsid · ssRNA · dsDNA · retrovirus',
  '  R0 > 1 → epidemic; SIR model',
  '  Fick · Nernst · Hodgkin-Huxley',
  '  IC50 · LD50 · ADME · PK/PD curve',
  '  Zygote→gastrula→organogenesis'],
 'Evolution, virus, physics of life, and development.'),

# ── History & Ideas ───────────────────────────────────────────────────────────
('6','C',
 ['historical-geography','history-of-science','economic-history','military-history'],
 ['  "here be dragons" — pre-1500 maps',
  '  Longitude unsolved until ~1760',
  '  Copernicus→Galileo→Newton→Einstein',
  '  Paradigm shift (Kuhn, 1962)',
  '  Silk Road · Atlantic trade · GATT',
  '  GDP per capita 1000–2000: hockey stick',
  '  Phalanx · trebuchet · Maxim gun'],
 'Maps, revolutions, trade routes — the long record.'),

('6','D',
 ['anthropology','philosophy','mythology','religious-studies','archaeology'],
 ['  Cave art 40kya — Lascaux · Chauvet',
  '  Cuneiform 3200 BCE · Linear B 1450',
  '  Plato: Forms · Aristotle: categories',
  '  Kant: synthetic a priori · Hume: cause',
  '  Hero myth: departure→trial→return',
  '  Axial Age: Buddha·Confucius·Socrates',
  '  Stratigraphy · typology · radiocarbon'],
 'Before the tool: the story, the question, the ritual.'),

('6','H',
 ['logic','intellectual-history','social-history','historiography'],
 ['  A→B, A ∴ B  (modus ponens)',
  '  ¬(P∧¬P)    (non-contradiction)',
  '  Republic of Letters → print → web',
  '  Enlightenment → Romanticism → Modernism',
  '  Annales school: longue durée',
  '  Peasant · artisan · merchant · noble',
  "  Source criticism → archive → method"],
 'Logic, ideas in motion, and how we write the past.'),

('6','S',
 ['political-history','philosophy-of-mind','ethics','philosophy-of-science'],
 ['  Athens→Rome→Westphalia→Leviathan',
  '  Nation-state · empire · republic',
  "  Descartes' mind-body problem, 1641",
  '  Consciousness · qualia · functionalism',
  "  Hume's guillotine: is ≠ ought",
  '  Deont · Consequentialist · Virtue',
  '  Popper: falsifiability · Kuhn: paradigm'],
 'Power, mind, morality, and scientific knowledge itself.'),

# ── Mechanics ─────────────────────────────────────────────────────────────────
('7','C',
 ['mechanical','structural','aeronautics'],
 ['  ╔══lever══╗ ╔══pulley══╗ ╔screw╗',
  '  MA = F_out / F_in (mech. advantage)',
  '  ╔═══arch═══╗ span → compression',
  '  Beam: M = EI d²y/dx²  (Euler)',
  '  FoS = ultimate / working stress',
  '  Bernoulli: p + ½ρv² + ρgh = const',
  '  Cl · Cd · L/D ratio · stall angle'],
 'Lever, arch, wing — the first engineering.'),

('7','D',
 ['chemical-eng','nuclear','energy-systems'],
 ['  Distillation: VLE · McCabe-Thiele',
  '  CSTR: F_A0 X = -r_A V  (design eq)',
  '  E = mc² · fission: U-235 + n',
  '  Moderator · control rod · coolant',
  '  Carnot η = 1 - T_c/T_h (max eff.)',
  '  Rankine · Brayton · Otto cycles',
  '  Primary → secondary → grid (MW)'],
 'Reaction, fission, and thermodynamic cycles.'),

('7','H',
 ['electrical-grid','hvac','plumbing','construction-materials'],
 ['  Generator → xfmr → transmission',
  '  345kV line → substation → 120V',
  '  Psychrometric chart: T · RH · h',
  '  AHU: cooling coil · filter · fan',
  '  Bernoulli in pipes: Darcy-Weisbach',
  '  DWV: gravity · trap · vent stack',
  '  Concrete f_c · steel F_y · insul R'],
 'Grid, air, water, structure — the built environment.'),

('7','S',
 ['acoustics','optics','transportation','manufacturing'],
 ['  SPL = 20 log(p/p_ref) dB · Sabine RT',
  '  Room modes: fn = c/2L (axial)',
  "  Snell: n1 sinθ1 = n2 sinθ2",
  '  MTF · f-number · diffraction limit',
  '  Headway · capacity · LOS A→F',
  '  BRT · LRT · HSR grade separation',
  '  Lathe · mill · grind · EDM · CMM'],
 'Sound, light, motion, precision — classical tools.'),

# ── Technology ────────────────────────────────────────────────────────────────
('8','C',
 ['semiconductor-manufacturing','telecommunications','robotics'],
 ['  Si wafer → litho → etch → dope',
  '  EUV 13.5nm → FinFET → GAA 2nm',
  '  Shannon C = B log2(1 + S/N)',
  '  OFDM · MIMO · 5G NR · mmWave',
  '  DH · FK · Jacobian · trajectory',
  '  SLAM: map + localize simultaneously',
  '  Sensor → plan → actuate (loop)'],
 'Silicon, signal, and machine that moves itself.'),

('8','D',
 ['biomedical-engineering','formal-methods','systems-engineering'],
 ['  EEG · ECG · MRI · ultrasound · ct',
  '  Prosthetic: socket · pylon · foot',
  '  TLA+: state machine → model check',
  '  Hoare logic: {P} C {Q} (triple)',
  'V-model: req→design→impl→test→ops',
  '  FMEA · FTA · reliability block diag',
  '  SysML: bdd · ibd · req · seq diag'],
 'Verified systems — from implant to formal proof.'),

('8','H',
 ['urban-planning','environmental-engineering','materials-processing','geotechnical-engineering'],
 ['  FAR · setback · zoning · TOD',
  '  City: towers + parks + transit + pipe',
  '  BOD · COD → treatment → effluent',
  '  Air: PM2.5 · NOx · scrubber · ESP',
  '  Blast furnace → BOF → rolling mill',
  '  Sinter · pelletize · calcine · smelt',
  '  SPT · CPT · shear strength · Mohr-C'],
 'City, environment, material, ground — engineered place.'),

('8','S',
 ['nanotechnology','energy-storage','infrastructure-systems'],
 ['  1–100 nm: quantum confinement zone',
  '  CNT · quantum dot · graphene sheet',
  '  Li-ion: intercalation · SEI · C-rate',
  '  Energy density: Wh/kg vs power W/kg',
  '  Ragone plot: battery→supercap→flywheel',
  '  Water · power · telecom · transport',
  '  Resilience: N-1 · redundancy · MTTR'],
 'Nanoscale materials, stored energy, and resilient grids.'),

# ── Social Sciences ───────────────────────────────────────────────────────────
('9','C',
 ['economics','finance','behavioral-economics','game-theory','statistics-applied'],
 ['  Supply ↓ Demand: P* · Q* at cross',
  '  GDP · CPI · M2 · r_f · yield curve',
  '  DCF · CAPM: E[r] = rf + β(rm-rf)',
  '  Loss aversion · hyperbolic discount',
  '  PD: Defect/Coop — Nash: (D,D)',
  '  Shapley value · auction mechanism',
  '  CLT · p-value · power · effect size'],
 'Price, incentive, game, and the numbers behind policy.'),

('9','D',
 ['political-science','law','sociology','demography'],
 ['  Presidential · Parliamentary · Federal',
  '  Separation of powers · judicial review',
  '  Common law · civil law · stare decisis',
  '  Torts · contract · property · crime',
  '  Durkheim: anomie · Weber: ideal type',
  '  TFR · CDR · migration · urbanization',
  '  Age pyramid: young·stationary·aging'],
 'State, law, society, and the count of the living.'),

('9','H',
 ['criminology','psychology','organizational-behavior','public-health'],
 ['  Classical → positivist → critical theory',
  '  CPTED · hot spots · deterrence vs rehab',
  '  Maslow → Herzberg → self-determination',
  '  Big Five: O·C·E·A·N traits',
  '  Org: tall·flat·matrix·holacracy',
  '  SIR model: R0 > 1 → epidemic',
  '  Vaccination · screening · surveillance'],
 'Crime, mind, organization, and population health.'),

('9','S',
 ['media-studies','education','international-relations','development-studies'],
 ['  Agenda-setting · framing · priming',
  '  Algorithm → filter bubble → viral',
  "  Bloom's taxonomy: remember→create",
  '  Constructivism · UDL · formative ax',
  '  Realist · liberal · constructivist IR',
  '  UN · WTO · IMF · ICC — intl order',
  '  HDI: income + education + health'],
 'Media frames reality; institutions frame nations.'),

# ── Language & Communication ──────────────────────────────────────────────────
('10','C',
 ['linguistics','world-languages','codes','typography'],
 ['  Phoneme · morpheme · syntax · pragma',
  '  IPA: [p] [b] [m] — bilabial stops',
  '  Language families: IE · Sino-Tib',
  '  SOV · SVO · VSO — word order types',
  '  Morse · Braille · ASCII · Unicode',
  '  Huffman: p(a)=0.5 → 1 bit code',
  '  Serif · sans · slab · tracking · kern'],
 'Sound to glyph — the substrate of recorded thought.'),

('10','D',
 ['printing-publishing','cinema-film','radio-television','literature'],
 ['  Moveable type → offset → digital',
  '  ISBN · DOI · ISSN · edition · imprint',
  '  24fps · aspect ratio · montage cut',
  '  3-act · hero journey · mise-en-scène',
  'AM · FM · NTSC · PAL · DVB-T · OTT',
  '  Novel · Epic · Lyric · Drama · Essay',
  '  Narrator · point of view · unreliable'],
 'Print, screen, broadcast — stories at scale.'),

('10','H',
 ['rhetoric','philosophy-of-language','semiotics','translation'],
 ['  Logos · Ethos · Pathos (Aristotle)',
  '  Speaker → argument → audience',
  '  Frege: sense ≠ reference (Sinn/Bed)',
  '  Wittgenstein: meaning = use',
  '  Saussure: signifier / signified',
  '  Icon · index · symbol (Peirce)',
  '  Fidelity vs loss: Venuti foreignize'],
 'Argument, meaning, sign, and the cost of translation.'),

('10','S',
 ['journalism','oral-tradition','epigraphy','digital-media'],
 ['  News values · inverted pyramid · byline',
  '  5W1H · objectivity · source shield',
  '  Epic formula · oral-formulaic theory',
  '  Milman Parry · Homer · griots · bards',
  '  Cuneiform → Linear A → Phoenician',
  '  Rosetta Stone decoded 1822 (Champoll)',
  '  PageRank · feed · dark social · TikTok'],
 'From clay tablet to algorithmic feed — same impulse.'),

# ── Mathematics & Physics ─────────────────────────────────────────────────────
('J','C',
 ['mathematics','physics','electronics'],
 ['  ∇·E = ρ/ε0   ∇×B = μ0(J + ε0∂E/∂t)',
  '  Maxwell unified light, E, and B (1865)',
  '  V = IR · P = IV · KVL · KCL · Thevenin',
  '  RC: τ=RC · LC: ω0=1/√(LC)',
  '  BJT: I_C = β I_B  (active region)',
  '  MOSFET: I_D = k(V_GS-V_th)² /2',
  '  Logic: AND · OR · NOT · XOR · FF'],
 'Maxwell, circuit, gate — the formal physical world.'),

('J','D',
 ['materials','quantum-computing','control-theory','signal-processing','information-theory'],
 ['  Band gap: conductor·semi·insulator',
  '  |ψ⟩ = α|0⟩ + β|1⟩  |α|²+|β|²=1',
  '  CNOT + H → Bell state entanglement',
  '  Bode: gain margin · phase margin',
  '  PID: u = Kp·e + Ki∫e + Kd·de/dt',
  '  FFT: O(N log N) · DFT · windowing',
  '  H(X) = -Σ p log p  (Shannon entropy)'],
 'Qubit, feedback loop, transform, and information measure.'),

('J','H',
 ['number-theory','abstract-algebra','topology','probability-statistics','differential-geometry','numerical-methods'],
 ['  π(x) ~ x/ln x   (prime density)',
  '  Group: closure · assoc · id · inv',
  '  Ring → Field → Vector space',
  '  Möbius strip: one-sided · χ=0',
  '  Genus: sphere g=0 · torus g=1',
  '  P(A|B) = P(B|A)P(A)/P(B)  (Bayes)',
  '  Newton · bisection · RK4 · FEM'],
 'Prime, group, surface, probability, curvature, approximation.'),

('J','S',
 ['complex-analysis','fluid-dynamics','statistical-mechanics','partial-differential-equations','variational-calculus','lie-groups'],
 ['  f(z) analytic → Cauchy-Riemann eqs',
  '  Re: ρvL/μ  laminar→turbulent >4000',
  '  Z = Σ exp(-βEi)  partition function',
  '  S = k ln Ω  (Boltzmann entropy)',
  '  ∇²u = f  (Poisson · Laplace · wave)',
  '  δS/δq = 0 → Euler-Lagrange eq',
  '  Lie algebra [X,Y]=XY-YX  structure'],
 'Complex plane, flow, entropy, PDE, action, symmetry.'),

# ── Arts & Culture ────────────────────────────────────────────────────────────
('Q','C',
 ['art-history','architecture-history','architecture','music-theory'],
 ['  Paleolithic cave → fresco → oil → pixel',
  '  Patronage · academy · avant-garde · mkt',
  '  Post · Lintel · Arch · Vault · Dome',
  '  Order: Doric · Ionic · Corinthian',
  '  Staff: clef · note · rest · bar line',
  '  Harmony: triad · seventh · voicing',
  '  Form: ABA · sonata · rondo · fugue'],
 'Column, chord, canvas — the built and composed world.'),

('Q','D',
 ['photography','colors','cartography','games-history','sports-history'],
 ['  f/stop · shutter · ISO · DoF · bokeh',
  '  RAW → develop → tone curve → export',
  '  Munsell: hue · chroma · value axes',
  '  Simultaneous contrast · metamerism',
  '  Mercator · Robinson · equal-area proj',
  '  Topographic: contour · hachure · DEM',
  '  Board → card → video → esports arc'],
 'Light, color, map, game — applied seeing.'),

('Q','H',
 ['watchmaking','theater-performance','dance','industrial-design'],
 ['  Escapement: lever · cylinder · coaxial',
  '  Balance wheel · mainspring · gear train',
  '  Stage: thrust · proscenium · in-the-round',
  '  Stanislavski · Brecht · Grotowski method',
  '  Choreography: effort · space · time · flow',
  '  Ballet · modern · contact improv · hip-hop',
  '  Form follows function (Sullivan, 1896)'],
 'Mechanism, stage, movement, form — the designed artifact.'),

('Q','S',
 ['graphic-design','fashion','comics-sequential-art','sports-science'],
 ['  Grid · hierarchy · whitespace · contrast',
  '  Kerning · leading · tracking · measure',
  '  Silhouette → drape → construction line',
  '  Warp · weft · pattern → garment system',
  '  Gutter · panel · bleed · splash page',
  '  McCloud: closure between panels',
  '  VO2max · lactate threshold · power-to-wt'],
 'Grid, silhouette, panel, power — the frontier of form.'),

# ── Computing & Software ──────────────────────────────────────────────────────
('K','C',
 ['computing','ai-engineering','data-science'],
 ['  TM: tape · head · state · δ(q,s)→(q,s,d)',
  '  Church-Turing thesis · decidability',
  '  Transformer: Q·K·V attention → token',
  '  LLM: next-token P(w|context)',
  '  RAG · RLHF · fine-tune · alignment',
  '  DataFrame · vectorize · broadcast',
  '  Train/val/test · confusion matrix · AUC'],
 'Computation, intelligence, and the shape of data.'),

('K','D',
 ['languages','query-languages','scripting','os'],
 ['  Grammar: G=(N,Σ,P,S) → parse tree',
  '  Types: nominal·structural·dependent',
  '  SELECT * FROM t WHERE p GROUP BY k',
  '  Plan: seq scan · hash join · index',
  '  Pipe: prog | filter | transform | sink',
  '  Process · thread · syscall · scheduler',
  '  VM: stack · heap · static · code seg'],
 'Language, query, shell, kernel — the programming stack.'),

('K','H',
 ['cryptography','computer-architecture','machine-learning-theory','programming-language-theory'],
 ['  P→C: AES-256 key sched · 10 rounds',
  '  RSA: ed≡1(mod φ) · ECDH · ML-KEM',
  '  ALU · FPU · cache L1/L2/L3 · MMU',
  '  Pipeline: IF · ID · EX · MEM · WB',
  '  PAC learn · VC dim · margin theory',
  '  SRM: minimize R_emp + complexity',
  '  λ-calculus · type theory · PLT core'],
 'Crypto, silicon, learning theory, and formal language.'),

('K','S',
 ['distributed-systems','security-engineering','cloud-architecture'],
 ['  Raft: leader · follower · candidate',
  '  CAP: CP or AP — pick two of three',
  '  STRIDE: spoof·tamper·repud·info·DoS',
  '  Threat model → pentest → red team',
  '  VPC · subnet · IGW · NAT · SG · ACL',
  '  EC2+S3+RDS+CDN → auto-scale → IaC',
  '  Serverless · containers · service mesh'],
 'Consensus, threat model, cloud — distributed computing.'),

# ── People ────────────────────────────────────────────────────────────────────
('A','C',
 ['mathematicians-logicians','physicists-astronomers','chemists-naturalists'],
 ['  Euclid · Euler · Gauss · Riemann',
  '  Cantor · Hilbert · Gödel · Turing',
  '  Newton · Faraday · Maxwell · Curie',
  '  Einstein · Bohr · Feynman · Hawking',
  "  Lavoisier · Dalton · Mendeleev",
  '  Darwin · Humboldt · Linnaeus',
  '  e^(iπ) + 1 = 0  (Euler, 1748)'],
 'The names behind every equation in the other 51 volumes.'),

('A','D',
 ['engineers-inventors','computing-pioneers','explorers'],
 ['  Watt · Tesla · Edison · von Braun',
  '  Brunel · Eiffel · Otis · Benz · Ford',
  '  Babbage · Lovelace · Shannon · Turing',
  '  von Neumann · Hopper · Knuth · Kay',
  '  Cook · Amundsen · Earhart · Hillary',
  '  Cousteau · Ride · Armstrong · Glenn',
  '  Invention → patent → industry → world'],
 'Engineers, pioneers, explorers — applied human will.'),

('A','H',
 ['philosophers-thinkers','artists-architects','writers-poets'],
 ['  Plato · Aristotle · Kant · Hegel',
  '  Wittgenstein · Heidegger · Rawls',
  '  da Vinci · Michelangelo · Hokusai',
  '  Wright · Le Corbusier · Hadid · Piano',
  '  Homer · Dante · Shakespeare · Tolstoy',
  '  Kafka · Borges · Morrison · Achebe',
  '  Idea → form → word → endurance'],
 'Philosopher, builder, poet — the human record made permanent.'),

('A','S',
 ['political-reformers','social-reformers','visionaries'],
 ['  Locke · Jefferson · Wollstonecraft',
  '  Lincoln · Gandhi · Mandela · Havel',
  '  Wilberforce · Tubman · Anthony · Parks',
  '  Nightingale · Sanger · Carson · King',
  '  Verne · Wells · Turing · Fuller · Sagan',
  '  Visionary: sees what is not yet real',
  '  People: origin · center · culmination'],
 'Reformers and visionaries — the human at the center of the mark.'),

]


def generate():
    for rank, suit_key, dirs, art, motto in CARDS:
        content = render_card(rank, suit_key, dirs, art, motto)
        sym, suit_name = SUITS[suit_key]
        abbr = RANK_ABBR[rank]
        vol_roman = ['', 'I', 'II', 'III', 'IV'][SUIT_ORDER.index(suit_key) + 1]
        section = RANKS[rank]

        md = f'# {rank}{sym} — {section} · Volume {vol_roman}\n\n'
        md += f'*{suit_name} volume of the {section} section.*\n\n'
        md += '```\n'
        md += content
        md += '\n```\n'

        fname = f'{rank}{suit_key}.md'
        path = os.path.join(OUT, fname)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(md)
        print(f'  wrote {fname}')

    print(f'\nDone — {len(CARDS)} cards in {os.path.abspath(OUT)}')


if __name__ == '__main__':
    generate()
