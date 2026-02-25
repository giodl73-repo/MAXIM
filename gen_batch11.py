import os

dirs = {
    'mathematicians-logicians': {
        'coverage': 'Profiles and intellectual contributions of major mathematicians and logicians.',
        'files': [
            ('00-OVERVIEW.md', 'Landscape, taxonomy, and selection criteria'),
            ('01-ANCIENT-MEDIEVAL.md', 'Euclid, Archimedes, Hypatia, Al-Khwarizmi, Fibonacci'),
            ('02-EARLY-MODERN.md', 'Descartes, Pascal, Newton, Leibniz, Bernoulli family'),
            ('03-18TH-CENTURY.md', 'Euler, Lagrange, Laplace, Gauss'),
            ('04-19TH-CENTURY-ANALYSIS.md', 'Cauchy, Riemann, Weierstrass, Cantor, Dedekind'),
            ('05-19TH-CENTURY-ALGEBRA.md', 'Galois, Abel, Cayley, Lie, Noether (Emmy)'),
            ('06-LOGIC-FOUNDATIONS.md', 'Frege, Russell, Hilbert, Godel, Church'),
            ('07-20TH-CENTURY-PURE.md', 'Hardy, Ramanujan, Von Neumann, Bourbaki, Weil, Grothendieck'),
            ('08-PROBABILITY-STATISTICS.md', 'Bayes, Gauss, Pearson, Fisher, Kolmogorov, Wald'),
            ('09-MODERN-APPLIED.md', 'Turing, Shannon, Wiener (cybernetics), Nash, Mandelbrot, Tao'),
        ]
    },
    'physicists-astronomers': {
        'coverage': 'Profiles of major physicists and astronomers from Galileo through Hawking.',
        'files': [
            ('00-OVERVIEW.md', 'Landscape, taxonomy, and selection criteria'),
            ('01-ASTRONOMICAL-REVOLUTION.md', 'Copernicus, Tycho, Kepler, Galileo'),
            ('02-CLASSICAL-MECHANICS.md', 'Newton, Hooke, Huygens, Lagrange, Hamilton'),
            ('03-THERMODYNAMICS-STAT-MECH.md', 'Carnot, Clausius, Kelvin, Boltzmann, Gibbs'),
            ('04-ELECTROMAGNETISM.md', 'Faraday, Maxwell, Hertz, Lorentz, Tesla'),
            ('05-RELATIVITY.md', 'Einstein (special and general), Minkowski, Schwarzschild'),
            ('06-QUANTUM-PIONEERS.md', 'Planck, Bohr, De Broglie, Heisenberg, Schrodinger, Born, Pauli'),
            ('07-QUANTUM-FIELD-THEORY.md', 'Dirac, Feynman, Schwinger, Tomonaga, Yang, Mills'),
            ('08-NUCLEAR-PARTICLE.md', 'Rutherford, Chadwick, Fermi, Lawrence, Gell-Mann, Weinberg'),
            ('09-MODERN-COSMOLOGY.md', 'Hubble, Chandrasekhar, Curie (Marie), Hawking, Penrose, Vera Rubin'),
        ]
    },
    'chemists-naturalists': {
        'coverage': 'Profiles of major chemists and naturalists: Lavoisier, Dalton, Mendeleev, Darwin, Pasteur, Humboldt, Pauling.',
        'files': [
            ('00-OVERVIEW.md', 'Landscape, taxonomy, and selection criteria'),
            ('01-EARLY-NATURALISTS.md', 'Aristotle (natural history), Linnaeus (taxonomy), Buffon, Ray'),
            ('02-CHEMICAL-REVOLUTION.md', 'Lavoisier, Priestley, Scheele, Cavendish'),
            ('03-ATOMIC-THEORY.md', 'Dalton, Avogadro, Gay-Lussac, Berzelius'),
            ('04-ORGANIC-CHEMISTRY.md', 'Wohler, Kekule (benzene), Pasteur (stereochemistry), Liebig'),
            ('05-PERIODIC-TABLE.md', 'Mendeleev, Meyer, Moseley, Seaborg'),
            ('06-PHYSICAL-CHEMISTRY.md', 'Van Hoff, Arrhenius, Nernst, Lewis, Pauling'),
            ('07-EVOLUTION-NATURALISTS.md', 'Darwin, Wallace, Lamarck, Haeckel, Huxley (T.H.)'),
            ('08-EXPLORATION-NATURALISTS.md', 'Humboldt, Banks, Bates, Cook (scientific), Wallace'),
            ('09-20TH-CENTURY-CHEMISTRY.md', 'Haber, Bosch, Curie (Marie/Irene), Hodgkin, Crick+Watson+Franklin'),
        ]
    },
    'engineers-inventors': {
        'coverage': 'Profiles of major engineers and inventors from Archimedes through the digital revolution.',
        'files': [
            ('00-OVERVIEW.md', 'Landscape, taxonomy, and selection criteria'),
            ('01-ANCIENT-RENAISSANCE.md', 'Archimedes, Hero of Alexandria, Leonardo da Vinci, Vitruvius'),
            ('02-INDUSTRIAL-REVOLUTION.md', 'Watt, Newcomen, Stephenson, Trevithick, Brunel (Isambard)'),
            ('03-ELECTRICAL-PIONEERS.md', 'Faraday, Edison, Tesla, Westinghouse, Marconi'),
            ('04-TRANSPORTATION.md', 'Wright Brothers, Ford, Diesel, Benz, Whittle (jet engine)'),
            ('05-STRUCTURES-MATERIALS.md', 'Eiffel, Roebling (Brooklyn Bridge), Bessemer, Goodyear'),
            ('06-COMPUTING-HARDWARE.md', 'Babbage, Hollerith, Atanasoff, Von Neumann, Kilby+Noyce (IC)'),
            ('07-COMMUNICATIONS.md', 'Bell, Morse, Armstrong (FM), Shannon, Farnsworth (TV)'),
            ('08-AEROSPACE.md', 'Von Braun, Goddard, Korolev, Tsiolkovsky, Kelly Johnson'),
            ('09-MODERN-INNOVATORS.md', 'Shockley, Noyce, Jobs, Berners-Lee, Musk (rockets/EVs)'),
        ]
    },
    'computing-pioneers': {
        'coverage': 'Profiles of major computing pioneers: Babbage, Lovelace, Turing, Von Neumann, Shannon, Hopper, Knuth, Thompson, Ritchie, Kay, Berners-Lee.',
        'files': [
            ('00-OVERVIEW.md', 'Landscape, taxonomy, and selection criteria'),
            ('01-MECHANICAL-ERA.md', 'Babbage (Difference/Analytical Engine), Lovelace (first programmer), Hollerith'),
            ('02-THEORY-FOUNDATIONS.md', 'Turing (computability, Turing machine, test), Church (lambda calculus), Post'),
            ('03-EARLY-COMPUTERS.md', 'Von Neumann (architecture), Atanasoff, Eckert+Mauchly (ENIAC), Zuse'),
            ('04-INFORMATION-THEORY.md', 'Shannon (entropy, channel capacity, error correction), Nyquist, Hamming'),
            ('05-PROGRAMMING-LANGUAGES.md', 'Hopper (COBOL, first compiler), McCarthy (Lisp, AI), Backus (Fortran, BNF), Wirth'),
            ('06-ALGORITHMS-COMPLEXITY.md', 'Dijkstra, Knuth (TAOCP, TeX), Cook (NP-completeness), Karp'),
            ('07-SYSTEMS-OS.md', 'Thompson+Ritchie (Unix/C), Torvalds (Linux), Stallman (GNU), Kernighan'),
            ('08-PERSONAL-COMPUTING.md', 'Kay (Smalltalk, OOP, GUI), Engelbart (mouse, hypertext), Jobs+Wozniak'),
            ('09-INTERNET-WEB.md', 'Cerf+Kahn (TCP/IP), Berners-Lee (WWW), Andreessen (Mosaic), Page+Brin'),
        ]
    },
    'explorers': {
        'coverage': 'Profiles of major explorers: Marco Polo, Columbus, da Gama, Magellan, Cook, Amundsen, Hillary, Cousteau, Armstrong.',
        'files': [
            ('00-OVERVIEW.md', 'Landscape, taxonomy, and selection criteria'),
            ('01-SILK-ROAD-MEDIEVAL.md', 'Marco Polo, Ibn Battuta, Zheng He, Rabban Sauma'),
            ('02-AGE-OF-EXPLORATION.md', 'Columbus, da Gama (Cape route), Cabot, Amerigo Vespucci'),
            ('03-CIRCUMNAVIGATION.md', 'Magellan+Elcano (first), Drake, Anson, Bougainville'),
            ('04-PACIFIC-EXPLORATION.md', 'Cook (three voyages), Vancouver, Tasman, La Perouse'),
            ('05-ARCTIC-ANTARCTIC.md', 'Franklin (lost expedition), Amundsen, Scott, Shackleton, Nansen'),
            ('06-SCIENTIFIC-EXPEDITIONS.md', 'Humboldt (Americas), Darwin (Beagle), Wallace (Malay), Challenger expedition'),
            ('07-CONTINENTAL-INTERIORS.md', 'Livingstone+Stanley (Africa), Lewis+Clark, Burke+Wills, Younghusband'),
            ('08-VERTICAL-FRONTIERS.md', 'Hillary+Tenzing (Everest), Herzog (Annapurna), Messner (8000m), Cousteau (deep sea)'),
            ('09-MODERN-FRONTIERS.md', 'Armstrong+Aldrin (Moon), Gagarin, Glenn, Piccard (stratosphere/ocean), Ballard (Titanic)'),
        ]
    },
    'philosophers-thinkers': {
        'coverage': 'Profiles of major philosophers: Socrates, Plato, Aristotle, Descartes, Spinoza, Locke, Hume, Kant, Hegel, Nietzsche, Marx, Wittgenstein, Russell, Rawls.',
        'files': [
            ('00-OVERVIEW.md', 'Landscape, taxonomy, and selection criteria'),
            ('01-ANCIENT-GREEK.md', 'Pre-Socratics, Socrates (method), Plato (Forms, Republic), Aristotle (everything)'),
            ('02-HELLENISTIC-ROMAN.md', 'Epicurus, Stoics (Zeno, Epictetus, Marcus Aurelius), Plotinus (Neoplatonism)'),
            ('03-MEDIEVAL-ISLAMIC.md', 'Augustine, Aquinas, Avicenna (Ibn Sina), Averroes (Ibn Rushd), Maimonides'),
            ('04-RATIONALISTS.md', 'Descartes (cogito, dualism), Spinoza (substance monism), Leibniz (monads, theodicy)'),
            ('05-EMPIRICISTS-ENLIGHTENMENT.md', 'Locke, Berkeley, Hume (causation, induction problem), Rousseau'),
            ('06-KANT-GERMAN-IDEALISM.md', 'Kant (Critiques, categorical imperative), Fichte, Schelling, Hegel (dialectic)'),
            ('07-19TH-CENTURY.md', 'Schopenhauer, Marx (historical materialism), Kierkegaard, Nietzsche (will to power)'),
            ('08-ANALYTIC-TRADITION.md', 'Frege, Russell (logical atomism), Wittgenstein (TLP + PI), Quine, Davidson'),
            ('09-20TH-CENTURY-CONTINENTAL.md', 'Husserl, Heidegger, Sartre, Camus, Merleau-Ponty, Rawls (justice), Habermas'),
        ]
    },
    'artists-architects': {
        'coverage': 'Profiles of major artists and architects: Leonardo, Michelangelo, Rembrandt, Monet, Cezanne, Picasso, Le Corbusier, Wright (Frank Lloyd), Mies.',
        'files': [
            ('00-OVERVIEW.md', 'Landscape, taxonomy, and selection criteria'),
            ('01-RENAISSANCE-MASTERS.md', 'Brunelleschi (perspective), Alberti, Leonardo da Vinci, Michelangelo, Raphael'),
            ('02-BAROQUE-DUTCH.md', 'Caravaggio, Rubens, Rembrandt, Vermeer, Velazquez'),
            ('03-18TH-19TH-CENTURY.md', 'Goya, David, Turner, Constable, Delacroix, Courbet'),
            ('04-IMPRESSIONISM.md', 'Monet, Renoir, Degas, Manet, Cassatt, Pissarro'),
            ('05-POST-IMPRESSIONISM.md', 'Cezanne (proto-Cubism), Van Gogh, Gauguin, Seurat (pointillism)'),
            ('06-MODERN-ART.md', 'Picasso (Cubism), Matisse (Fauvism), Duchamp (Dada), Kandinsky, Mondrian'),
            ('07-CLASSICAL-ARCHITECTURE.md', 'Vitruvius, Palladio, Wren, Vanbrugh, Soane'),
            ('08-MODERN-ARCHITECTURE.md', 'Sullivan (form follows function), Wright (organic), Le Corbusier, Mies (less is more)'),
            ('09-CONTEMPORARY.md', 'Koolhaas, Hadid, Piano, Foster, Gehry, Ando and postwar art (Warhol, Rothko, Basquiat)'),
        ]
    },
    'writers-poets': {
        'coverage': 'Profiles of major writers and poets: Homer, Dante, Shakespeare, Cervantes, Austen, Dostoevsky, Tolstoy, Joyce, Woolf, Kafka, Borges, Morrison.',
        'files': [
            ('00-OVERVIEW.md', 'Landscape, taxonomy, and selection criteria'),
            ('01-ANCIENT-CLASSICAL.md', 'Homer (Iliad/Odyssey), Virgil (Aeneid), Sappho, Ovid, Horace'),
            ('02-MEDIEVAL.md', 'Dante (Comedy, vernacular), Chaucer (Canterbury Tales), Petrarch, Boccaccio'),
            ('03-RENAISSANCE-BAROQUE.md', 'Shakespeare (plays+sonnets), Cervantes (Don Quixote), Milton (Paradise Lost), Montaigne'),
            ('04-18TH-19TH-NOVELS.md', 'Defoe, Swift, Austen, Dickens, Flaubert, Balzac, Hardy'),
            ('05-RUSSIAN-LITERATURE.md', 'Pushkin, Gogol, Turgenev, Dostoevsky, Tolstoy, Chekhov'),
            ('06-MODERNISM.md', 'Joyce (stream of consciousness), Woolf, Proust, Kafka, Mann, Musil'),
            ('07-POETRY-TRADITIONS.md', 'Blake, Keats, Whitman, Dickinson, Yeats, Eliot (Waste Land), Rilke'),
            ('08-20TH-CENTURY-WORLD.md', 'Borges, Garcia Marquez (magical realism), Camus, Sartre (fiction), Beckett, Nabokov'),
            ('09-CONTEMPORARY.md', 'Morrison, Achebe, Rushdie, Gordimer, Coetzee, Pamuk, Munro'),
        ]
    },
    'political-reformers': {
        'coverage': 'Profiles of major political reformers: Solon, Pericles, Cromwell, Washington, Jefferson, Lincoln, Bismarck, Gandhi, Mandela, FDR.',
        'files': [
            ('00-OVERVIEW.md', 'Landscape, taxonomy, and selection criteria'),
            ('01-ANCIENT-REFORMERS.md', 'Solon (Athenian reforms), Cleisthenes (democracy), Pericles, Gracchi brothers'),
            ('02-MEDIEVAL-EARLY-MODERN.md', 'Magna Carta barons, Simon de Montfort, Luther (political consequences), Calvin'),
            ('03-REVOLUTIONARY-ERA.md', 'Cromwell, Washington, Jefferson, Hamilton, Robespierre, Napoleon'),
            ('04-19TH-CENTURY-LIBERALS.md', 'Bolivar, Garibaldi, Lincoln (abolition), Bismarck, Gladstone'),
            ('05-ANTI-COLONIAL.md', 'Gandhi (nonviolent resistance), Nehru, Ho Chi Minh, Nkrumah, Nyerere'),
            ('06-CIVIL-RIGHTS.md', 'Douglass, Du Bois, MLK, Malcolm X, Rosa Parks, Mandela'),
            ('07-DEMOCRATIC-REFORMERS.md', 'FDR (New Deal), Attlee (NHS), Adenauer, De Gaulle, Lula da Silva'),
            ('08-REVOLUTIONARY-LEADERS.md', 'Lenin, Mao, Castro, Guevara - revolutionary tactics and legacy'),
            ('09-CONTEMPORARY.md', 'Walesa, Havel, Gorbachev, Mandela (post-prison), Aung San Suu Kyi, Zelensky'),
        ]
    },
    'social-reformers': {
        'coverage': 'Profiles of major social reformers: Wilberforce, Nightingale, Stanton, Anthony, Addams, Chavez, Wollstonecraft, Tubman.',
        'files': [
            ('00-OVERVIEW.md', 'Landscape, taxonomy, and selection criteria'),
            ('01-ABOLITIONISTS.md', 'Wilberforce, Clarkson, Tubman (Underground Railroad), Douglass, Garrison'),
            ('02-WOMENS-RIGHTS.md', 'Wollstonecraft (Vindication), Stanton, Anthony, Pankhurst, Seneca Falls Declaration'),
            ('03-LABOR-MOVEMENT.md', 'Owen (utopian socialism), Debs, Gompers (AFL), Chavez (UFW), Solidarity (Walesa)'),
            ('04-PUBLIC-HEALTH-MEDICINE.md', 'Nightingale (nursing+statistics), Semmelweis, Snow (cholera map), Salk (polio vaccine)'),
            ('05-EDUCATION-REFORMERS.md', 'Pestalozzi, Froebel (kindergarten), Montessori, Dewey (progressive education), Freire'),
            ('06-CIVIL-LIBERTIES.md', 'ACLU founders, Frankfurter, Thurgood Marshall (legal strategy), Ginsburg'),
            ('07-ENVIRONMENTAL.md', 'Muir (Sierra Club), Pinchot, Carson (Silent Spring), Brundtland, Wangari Maathai'),
            ('08-POVERTY-DEVELOPMENT.md', 'Addams (Hull House), Mother Teresa, Muhammad Yunus (microfinance), Sachs vs Easterly'),
            ('09-MODERN-MOVEMENTS.md', 'Harvey Milk, Malala Yousafzai, Greta Thunberg - modern advocacy and its tactics'),
        ]
    },
    'visionaries': {
        'coverage': 'Profiles of major visionaries whose ideas shaped civilization: More, Bacon, Saint-Simon, Wells, Teilhard, Fuller, McLuhan, Sagan.',
        'files': [
            ('00-OVERVIEW.md', 'Landscape, taxonomy, and selection criteria'),
            ('01-UTOPIAN-THINKERS.md', 'Plato (Republic), More (Utopia), Campanella, Bacon (New Atlantis/inductive method)'),
            ('02-SOCIAL-VISIONARIES.md', 'Saint-Simon (technocracy), Fourier (phalansteries), Owen (New Lanark), Marx (historical vision)'),
            ('03-SCIENTIFIC-VISIONARIES.md', 'Leonardo (500yr-ahead engineering), Darwin, Faraday (field theory vision), Tesla'),
            ('04-FUTURISTS-EARLY.md', 'Wells (scientific romance as prediction), Verne, Bellamy (Looking Backward), Huxley'),
            ('05-SYSTEMS-THINKERS.md', 'Wiener (cybernetics), Von Bertalanffy (general systems), Forrester (system dynamics), Beer'),
            ('06-COMMUNICATION-VISIONARIES.md', 'McLuhan (global village), Innis, Negroponte (Being Digital), Licklider (man-computer symbiosis)'),
            ('07-ECOLOGICAL-COSMIC.md', 'Teilhard de Chardin (Omega Point), Vernadsky (noosphere), Lovelock (Gaia), Dyson'),
            ('08-TECHNOLOGICAL-VISIONARIES.md', 'Fuller (geodesic dome), Feynman (nanotechnology), Drexler, Kurzweil (singularity), Bostrom'),
            ('09-SPACE-CIVILIZATION.md', 'Tsiolkovsky (cosmic philosophy), Sagan (cosmos + contact), Hawking, Musk (multiplanetary)'),
        ]
    },
}

created = 0
for dirname, info in dirs.items():
    os.makedirs(dirname, exist_ok=True)
    lines = ['# ' + dirname + '/ -- Status\n\n## Files\n\n']
    lines.append('| File | Topic | Status |\n')
    lines.append('|------|-------|--------|\n')
    for fname, topic in info['files']:
        lines.append('| ' + fname + ' | ' + topic + ' | \U0001f51c |\n')
    lines.append('\n## Coverage Notes\n\n')
    lines.append(info['coverage'] + '\n')
    with open(dirname + '/STATUS.md', 'w', encoding='utf-8') as f:
        f.writelines(lines)
    for fname, topic in info['files']:
        stub_path = dirname + '/' + fname
        if not os.path.exists(stub_path):
            title = topic.split(' -- ')[0] if ' -- ' in topic else topic
            with open(stub_path, 'w', encoding='utf-8') as f:
                f.write('# ' + title + '\n\n> Stub -- to be written.\n')
            created += 1

print('Done: 12 directories, ' + str(created) + ' stub files created')
