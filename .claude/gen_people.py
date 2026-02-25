"""Generate Batch 11 — People section stub directories."""
import os

BASE = 'C:/src/reference'

DIRS = {
    'mathematicians-logicians': (
        'Mathematicians and logicians from antiquity through the present: Euclid, Gauss, Riemann, Cantor, Hilbert, Gödel, Turing, Noether, Grothendieck, Tao.',
        [
            ('OVERVIEW', 'Who Shaped Mathematics and Logic — Landscape and Roster'),
            ('ANCIENT-FOUNDATIONS', 'Ancient and Classical Mathematicians: Euclid, Archimedes, Pythagoras, Diophantus'),
            ('ISLAMIC-GOLDEN-AGE', 'Islamic Golden Age: al-Khwarizmi, al-Haytham, Omar Khayyam, al-Tusi'),
            ('EARLY-MODERN', 'Renaissance and Enlightenment: Descartes, Fermat, Pascal, Leibniz, Newton'),
            ('EULER-GAUSS-ERA', 'Euler, Gauss, and the Long 18th Century: Lagrange, Laplace, Fourier'),
            ('RIEMANN-CANTOR-ERA', 'Riemann, Weierstrass, Cantor, Dedekind — Analysis and Set Theory Forged'),
            ('LOGIC-REVOLUTION', 'Logic Revolution: Boole, Frege, Peano, Russell, Hilbert, Gödel'),
            ('TURING-VON-NEUMANN', 'Church, Turing, von Neumann, Shannon — From Logic to Computing'),
            ('NOETHER-RAMANUJAN', 'Emmy Noether, Ramanujan, Hardy — Beauty in Unexpected Places'),
            ('MODERN-GIANTS', 'Nash, Grothendieck, Wiles, Perelman, Tao, Mirzakhani — Modern Era'),
        ]
    ),
    'physicists-astronomers': (
        'Physicists and astronomers who mapped the cosmos: Copernicus, Galileo, Newton, Maxwell, Planck, Einstein, Bohr, Feynman, Hawking.',
        [
            ('OVERVIEW', 'The Architects of Physical Understanding — Landscape and Roster'),
            ('ANCIENT-MEDIEVAL', 'Ancient Sky-Watchers: Aristotle, Ptolemy, Aristarchus, Alhazen'),
            ('SCIENTIFIC-REVOLUTION', 'Scientific Revolution: Copernicus, Tycho, Kepler, Galileo'),
            ('NEWTON-AND-AFTERMATH', 'Newton, Hooke, Huygens, and Classical Mechanics'),
            ('19TH-CENTURY', '19th Century: Faraday, Maxwell, Kelvin, Boltzmann, Hertz'),
            ('QUANTUM-PIONEERS', 'Quantum Pioneers: Planck, Bohr, Heisenberg, Schrödinger, Dirac, Pauli'),
            ('EINSTEIN', 'Einstein: Special Relativity, General Relativity, Cosmology'),
            ('PARTICLE-PHYSICS', 'Particle Physics: Fermi, Feynman, Gell-Mann, Weinberg, Higgs'),
            ('ASTROPHYSICS', 'Astrophysics: Chandrasekhar, Hubble, Hoyle, Penzias and Wilson, Hawking'),
            ('CONTEMPORARY', 'Contemporary Physics: CERN Generation, Gravitational Wave Pioneers (LIGO)'),
        ]
    ),
    'chemists-naturalists': (
        'Chemists and naturalists who revealed the composition of matter and catalogued life: Lavoisier, Dalton, Mendeleev, Curie, Pauling, Humboldt, Darwin, Linnaeus.',
        [
            ('OVERVIEW', 'Chemists and Naturalists — Landscape and Roster'),
            ('ALCHEMY-ROOTS', 'Alchemy and Pre-Chemistry: Jabir, Paracelsus, van Helmont, Boyle'),
            ('CHEMICAL-REVOLUTION', 'Chemical Revolution: Lavoisier, Priestley, Scheele, Cavendish'),
            ('ATOMIC-THEORY', 'Atomic Theory and the Periodic Table: Dalton, Avogadro, Mendeleev, Newlands'),
            ('ELECTROCHEMISTRY', 'Electrochemistry and Synthesis: Davy, Faraday, Kekulé, Liebig'),
            ('CURIE-ERA', 'Radioactivity and Early 20th Century: the Curies, Rutherford, Hahn, Meitner'),
            ('PAULING-ERA', 'Bonds and Structures: Pauling, Lewis, Langmuir, G.N. Lewis'),
            ('NATURALISTS', 'Great Naturalists: Aristotle, Theophrastus, Linnaeus, Buffon, Humboldt'),
            ('DARWIN-WALLACE', 'Darwin, Wallace, and the Evolutionary Framework'),
            ('MOLECULAR-BIO', '20th-Century Biology Pioneers: Watson, Crick, Franklin, McClintock, Sanger'),
        ]
    ),
    'engineers-inventors': (
        'Engineers and inventors who built the physical world: Archimedes, Watt, Brunel, Edison, Tesla, the Wright Brothers, and modern systems builders.',
        [
            ('OVERVIEW', 'Engineers and Inventors — Landscape and Roster'),
            ('ANCIENT-MEDIEVAL', 'Ancient and Medieval Engineers: Archimedes, Hero of Alexandria, Roman Builders, al-Jazari'),
            ('RENAISSANCE', 'Renaissance Engineers: Leonardo da Vinci, Gutenberg, Verantius'),
            ('INDUSTRIAL-REVOLUTION', 'Industrial Revolution: Watt, Boulton, Stephenson, Brunel, Bessemer'),
            ('ELECTRICAL-AGE', 'Electrical Age: Edison, Tesla, Westinghouse, Marconi, Heaviside'),
            ('TRANSPORTATION', 'Transportation Revolution: Wright Brothers, Benz, Ford, Sikorsky'),
            ('STRUCTURAL', 'Structural Engineers: Eiffel, Roebling, Freyssinet, Maillart, Fuller'),
            ('ELECTRONICS-ERA', 'Electronics Era: Fleming, De Forest, Kilby, Noyce, Shockley'),
            ('SYSTEMS-ENGINEERS', '20th Century Systems: Bush, Wiener, von Braun, Deming, Conway'),
            ('MODERN', 'Modern Engineer-Visionaries: Musk, Engelbart, Ritchie, Wozniak, Linus Torvalds'),
        ]
    ),
    'computing-pioneers': (
        'The people who created computing: Babbage, Lovelace, Turing, von Neumann, Hopper, Dijkstra, Ritchie, Berners-Lee, and the open source generation.',
        [
            ('OVERVIEW', 'Computing Pioneers — Landscape and Roster'),
            ('PRE-DIGITAL', 'Pre-Digital: Babbage, Lovelace, Hollerith, Zuse, Atanasoff'),
            ('FOUNDING-GENERATION', 'Founding Generation: Eckert, Mauchly, von Neumann, Wilkes, Williams'),
            ('PROGRAMMING-LANGUAGES', 'Language Designers: Hopper, McCarthy, Backus, Dijkstra, Hoare, Wirth, Knuth'),
            ('THEORY-FOUNDATION', 'Theoretical Foundations: Church, Turing, Shannon, Cook, Karp, Blum'),
            ('SYSTEMS-OS', 'Systems and OS: Ritchie, Thompson, Joy, Kernighan, Pike, Torvalds'),
            ('INTERNET-WEB', 'Internet and Web: Cerf, Kahn, Berners-Lee, Postel, Clark'),
            ('PERSONAL-COMPUTING', 'Personal Computing: Engelbart, Kay, Jobs, Wozniak, Gates, Allen'),
            ('OPEN-SOURCE', 'Open Source Movement: Stallman, Torvalds, Raymond, Wall, Guido van Rossum'),
            ('AI-PIONEERS', 'AI Pioneers: McCulloch, Minsky, McCarthy, Rumelhart, LeCun, Hinton, Bengio'),
        ]
    ),
    'explorers': (
        'Explorers and cartographers who extended the known world: Pytheas, Marco Polo, Ibn Battuta, Zheng He, Columbus, Magellan, Cook, Humboldt, Amundsen.',
        [
            ('OVERVIEW', 'Explorers — Landscape and Roster'),
            ('ANCIENT-EXPLORERS', 'Ancient Explorers: Pytheas, Hanno, Zhang Qian, Eratosthenes'),
            ('SILK-ROAD-ERA', 'Silk Road and Medieval Travel: Marco Polo, Ibn Battuta, Rabban Sauma'),
            ('CHINESE-EXPANSION', 'Chinese Expansion: Zheng He and the Treasure Fleets'),
            ('PORTUGUESE-AGE', 'Portuguese Age of Discovery: Henry the Navigator, Dias, da Gama, Cabral'),
            ('SPANISH-AGE', 'Spanish Conquest and Circumnavigation: Columbus, Magellan/Elcano, Balboa'),
            ('NORTHERN-EUROPEAN', 'Northern European Expansion: Cabot, Hudson, Baffin, Cook'),
            ('SCIENTIFIC-EXPLORERS', 'Scientific Explorers: Humboldt, Darwin, Wallace, Bates'),
            ('POLAR-EXPLORATION', 'Polar Exploration: Nansen, Amundsen, Scott, Shackleton, Peary'),
            ('OCEAN-SPACE', 'Ocean and Space Exploration: Cousteau, Piccard, Ballard, Gagarin, Armstrong'),
        ]
    ),
    'philosophers-thinkers': (
        'Philosophers and thinkers who transformed how we understand reality, knowledge, and value: Socrates, Aristotle, Kant, Hegel, Nietzsche, Wittgenstein, Rawls.',
        [
            ('OVERVIEW', 'Philosophers and Thinkers — Landscape and Roster'),
            ('ANCIENT-GREECE', 'Ancient Greece: Thales, Socrates, Plato, Aristotle, Heraclitus'),
            ('HELLENISTIC-ROMAN', 'Hellenistic and Roman: Epicurus, Zeno, Cicero, Marcus Aurelius, Plotinus'),
            ('ISLAMIC-PHILOSOPHY', 'Islamic Philosophy: al-Kindi, al-Farabi, Avicenna, al-Ghazali, Averroes'),
            ('SCHOLASTICS-RENAISSANCE', 'Scholastics and Renaissance: Aquinas, Occam, Bacon, Descartes, Spinoza'),
            ('ENLIGHTENMENT', 'Enlightenment: Locke, Hume, Voltaire, Rousseau, Kant'),
            ('GERMAN-IDEALISM', 'German Idealism to Marx: Hegel, Schopenhauer, Feuerbach, Nietzsche, Marx'),
            ('ANALYTIC-TRADITION', 'Analytic Philosophy: Frege, Russell, Moore, Wittgenstein, Quine, Carnap'),
            ('CONTINENTAL-TRADITION', 'Continental Tradition: Husserl, Heidegger, Sartre, Camus, Merleau-Ponty, Foucault'),
            ('CONTEMPORARY', 'Contemporary: Rawls, Nozick, Parfit, Singer, Chalmers, Dennett'),
        ]
    ),
    'artists-architects': (
        'Artists and architects who shaped visual culture: Leonardo, Michelangelo, Rembrandt, Goya, Monet, Picasso, Wright, Le Corbusier, Zaha Hadid.',
        [
            ('OVERVIEW', 'Artists and Architects — Landscape and Roster'),
            ('ANCIENT-MEDIEVAL', 'Ancient and Medieval Makers: Greek Sculptors, Byzantine Mosaicists, Gothic Builders'),
            ('RENAISSANCE', 'Renaissance: Brunelleschi, Ghiberti, Donatello, Leonardo, Michelangelo, Raphael'),
            ('BAROQUE-ROCOCO', 'Baroque and Rococo: Caravaggio, Bernini, Rembrandt, Vermeer, Rubens, Watteau'),
            ('NEOCLASSICAL-ROMANTIC', 'Neoclassical to Romantic: David, Goya, Turner, Friedrich, Delacroix'),
            ('IMPRESSIONISM', 'Impressionism and Post-: Monet, Renoir, Cézanne, Van Gogh, Gauguin, Seurat'),
            ('MODERNISM', 'Modernism: Picasso, Matisse, Duchamp, Mondrian, Kandinsky, Brancusi'),
            ('ARCHITECTURE-MODERN', 'Modern Architecture: Palladio, Wren, Sullivan, Wright, Le Corbusier, Mies, Kahn'),
            ('MID-20TH-CENTURY', 'Mid-20th Century: Pollock, Rothko, Warhol, Basquiat, Beuys, Bourgeois'),
            ('CONTEMPORARY', 'Contemporary: Gehry, Piano, Foster, Zaha Hadid, Ando, Ai Weiwei'),
        ]
    ),
    'writers-poets': (
        'Writers and poets who shaped language and imagination: Homer, Dante, Shakespeare, Cervantes, Goethe, Dickens, Tolstoy, Kafka, Joyce, García Márquez.',
        [
            ('OVERVIEW', 'Writers and Poets — Landscape and Roster'),
            ('ANCIENT', 'Ancient World: Homer, Sappho, Virgil, Ovid, Horace, Murasaki Shikibu'),
            ('MEDIEVAL', 'Medieval: Dante, Chaucer, Ibn Tufayl, Rumi, Christine de Pizan'),
            ('EARLY-MODERN', 'Early Modern: Cervantes, Shakespeare, Montaigne, Molière, Milton'),
            ('ENLIGHTENMENT-ROMANTIC', 'Enlightenment to Romantic: Voltaire, Goethe, Austen, Blake, Keats, Shelley, Byron'),
            ('19TH-CENTURY-NOVEL', '19th-Century Novel: Dickens, Tolstoy, Flaubert, Dostoyevsky, Eliot, Melville'),
            ('AMERICAN-VOICE', 'American Literature: Whitman, Dickinson, Twain, Henry James, Poe'),
            ('MODERNISM', 'Modernism: Joyce, Woolf, Kafka, Proust, T.S. Eliot, Borges, Faulkner'),
            ('MID-20TH', 'Mid-20th Century: Orwell, Camus, Nabokov, García Márquez, Achebe, Morrison'),
            ('POETRY-DRAMA', 'Poetry and Drama: Yeats, Neruda, Akhmatova, Brecht, Beckett, Auden'),
        ]
    ),
    'political-reformers': (
        'Political leaders and reformers who reshaped states and peoples: Washington, Lincoln, Gandhi, Mandela, Roosevelt, Atatürk, Churchill, Wangari Maathai.',
        [
            ('OVERVIEW', 'Political Leaders and Reformers — Landscape and Roster'),
            ('ANCIENT-STATESMEN', 'Ancient Statesmen: Solon, Pericles, Alexander, Caesar, Augustus, Ashoka'),
            ('EARLY-MODERN', 'Early Modern: Cromwell, Washington, Jefferson, Hamilton, Robespierre'),
            ('19TH-CENTURY', '19th Century: Napoleon, Bismarck, Lincoln, Garibaldi, Atatürk'),
            ('INDEPENDENCE-LEADERS', 'Independence and Decolonization: Gandhi, Nehru, Nkrumah, Kenyatta, Ho Chi Minh, Mandela'),
            ('DEMOCRATIC-REFORMERS', 'Democratic Reformers: Roosevelt (FDR), Churchill, Adenauer, de Gaulle'),
            ('REVOLUTIONARY-LEADERS', 'Revolutionary Figures: Lenin, Mao, Castro — Power and Consequence'),
            ('CIVIL-RIGHTS-US', 'US Civil Rights: Douglass, Du Bois, King, Parks, Thurgood Marshall, Lewis'),
            ('WOMEN-IN-POLITICS', 'Women in Politics: Pankhurst, Perón, Golda Meir, Thatcher, Merkel, Ardern'),
            ('INTERNATIONAL-ORDER', 'International Order Builders: Wilson, FDR/Churchill/Stalin, UN Founders, Gorbachev'),
        ]
    ),
    'social-reformers': (
        'Social reformers and humanitarians who fought for justice and dignity: Wilberforce, Nightingale, Montessori, King, Mandela, Carson, Malala.',
        [
            ('OVERVIEW', 'Social Reformers and Humanitarians — Landscape and Roster'),
            ('ABOLITIONISTS', 'Abolitionists: Clarkson, Wilberforce, Equiano, Douglass, Garrison, Harriet Tubman'),
            ('LABOR-MOVEMENT', 'Labor Movement: Owen, Marx, Engels, Debs, Gompers, Triangle Fire Legacy'),
            ('WOMENS-RIGHTS', "Women's Rights: Wollstonecraft, Stanton, Anthony, Pankhurst, Friedan, Steinem"),
            ('PUBLIC-HEALTH', 'Public Health Reformers: Snow, Nightingale, Semmelweis, Lister, Salk'),
            ('EDUCATION-REFORMERS', 'Education Reformers: Pestalozzi, Froebel, Dewey, Montessori, Freire'),
            ('CIVIL-RIGHTS-GLOBAL', 'Global Civil Rights: Mandela, Tutu, Havel, Wiesel, Aung San Suu Kyi'),
            ('HUMANITARIAN-ORGS', 'Founding Humanitarian Organizations: Dunant / Red Cross, UNHCR, Doctors Without Borders'),
            ('ENVIRONMENTAL', 'Environmental Advocates: Thoreau, Muir, Leopold, Carson, Wangari Maathai'),
            ('CONTEMPORARY', 'Contemporary Reformers: Malala Yousafzai, Greta Thunberg, Peter Singer, Bryan Stevenson'),
        ]
    ),
    'visionaries': (
        'Visionaries who imagined and catalyzed radically different futures: More, Bacon, Verne, Wells, Fuller, McLuhan, Engelbart, Brand, Bostrom.',
        [
            ('OVERVIEW', 'Visionaries — Landscape and Roster'),
            ('UTOPIAN-THINKERS', 'Utopian Thinkers: More, Campanella, Bacon, Owen, Fourier, Saint-Simon'),
            ('SCIENTIFIC-PROPHETS', 'Scientific Prophets: Verne, Wells, Huxley, Orwell — Fiction as Warning'),
            ('VANNEVAR-BUSH', 'Vannevar Bush and the Memex: The Blueprint for Hypertext and Research'),
            ('CYBERNETICS', 'Cybernetics Generation: Wiener, Ashby, Beer — Feedback and Control as Metaphor'),
            ('SYSTEMS-THINKERS', 'Systems Thinkers: Forrester, Meadows (Limits to Growth), Odum, Lovelock (Gaia)'),
            ('COUNTERCULTURE', 'Counterculture and Alternatives: Thoreau, Illich, Schumacher, Brand (Whole Earth)'),
            ('DIGITAL-VISIONARIES', 'Digital Visionaries: Licklider, Engelbart, Nelson, Kay, Berners-Lee'),
            ('SPACE-LONG-TERM', "Space and Long-Term Thinking: von Braun, Freeman Dyson, O'Neill, Brand, de Grey"),
            ('EFFECTIVE-ALTRUISM', 'Effective Altruism and X-Risk: Bostrom, MacAskill, Ord, Singer, Toby Ord'),
        ]
    ),
}

def write_stub(path, title):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(f'# {title}\n\n> Stub — to be written.\n')

def write_status(dirpath, dirname, description, files):
    rows = []
    rows.append(f'| 00-OVERVIEW.md | {files[0][1]} | 🔜 |')
    for i, (slug, topic) in enumerate(files[1:], 1):
        rows.append(f'| {i:02d}-{slug}.md | {topic} | 🔜 |')

    content = f"""# {dirname}/ — Status

## Files

| File | Topic | Status |
|------|-------|--------|
""" + '\n'.join(rows) + f"""

## Coverage Notes

{description}
Key connections: cross-references to relevant subject directories throughout the library.
"""
    with open(os.path.join(dirpath, 'STATUS.md'), 'w', encoding='utf-8') as f:
        f.write(content)

count_dirs = 0
count_files = 0

for dirname, (description, files) in DIRS.items():
    dirpath = os.path.join(BASE, dirname)
    os.makedirs(dirpath, exist_ok=True)
    count_dirs += 1

    write_status(dirpath, dirname, description, files)
    count_files += 1

    # 00-OVERVIEW.md
    slug0, title0 = files[0]
    write_stub(os.path.join(dirpath, '00-OVERVIEW.md'), title0)
    count_files += 1

    # numbered files
    for i, (slug, title) in enumerate(files[1:], 1):
        fname = f'{i:02d}-{slug}.md'
        write_stub(os.path.join(dirpath, fname), title)
        count_files += 1

print(f'Created {count_dirs} directories, {count_files} files.')
