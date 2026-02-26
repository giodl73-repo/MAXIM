# Computing Pioneers — Overview

## The Intellectual Lineage

Computing as a discipline has a peculiarly short history — from Babbage's gears to GPT-4 in under 200 years. What makes it remarkable is how densely the foundational ideas cluster in time: the entire theoretical basis was laid in roughly a single decade (1935–1945), before there was a single working computer to run any of it.

```
TIMELINE: COMPUTING'S INTELLECTUAL LINEAGE
==========================================

  1830s ─── BABBAGE: Mechanical computation. Programs on punched cards.
             LOVELACE: First algorithm. Understood generality of the engine.

  1890s ─── HOLLERITH: Punched-card tabulation. Census machines. IBM origin.

  1930s ─── TURING:  Computability, halting problem, universal machine (1936)
             CHURCH:  Lambda calculus. Computability via reduction (1936)
             POST:    Post correspondence problem, tag systems (1936)
             ─── All three independently defined what "computable" means ───

  1940s ─── VON NEUMANN: Stored-program architecture. EDVAC report (1945)
             ECKERT+MAUCHLY: ENIAC — first general-purpose electronic computer
             ATANASOFF+BERRY: ABC — first electronic (special-purpose)
             ZUSE: Z3 — first programmable (relay-based, Germany, 1941)
             SHANNON: Information theory. Entropy, channel capacity (1948)
             HOPPER: First compiler. COBOL. "Bug" (1952+)

  1950s ─── BACKUS: Fortran. BNF grammar (1957–1960)
             McCARTHY: Lisp. Recursion, garbage collection, AI (1958)
             HAMMING: Error-correcting codes (1950)

  1960s ─── DIJKSTRA: Shortest path, semaphores, structured programming
             KNUTH: TAOCP vol 1 (1968). TeX (1978). Algorithm analysis
             THOMPSON+RITCHIE: Unix (1969). C language (1972)

  1970s ─── KAY: Smalltalk. Object-oriented programming. GUI concept
             ENGELBART: Mouse, hypertext, collaborative computing (demo: 1968)
             WIRTH: Pascal, Modula-2. Structured languages

  1980s ─── STALLMAN: GNU project. GPL. Free software movement (1983)
             COOK+KARP: NP-completeness (1971–1972)

  1990s ─── TORVALDS: Linux kernel (1991)
             BERNERS-LEE: World Wide Web — HTTP, HTML, URL (1989–1991)
             ANDREESSEN: Mosaic browser. Web goes visual (1993)

  2000s ─── PAGE+BRIN: PageRank. Search as graph problem (1998)
```

---

## Taxonomy: What Kind of Pioneer?

Not all pioneers are the same kind. The intellectual types cut across eras:

```
  TYPE A: THEORISTS
  ─────────────────
  Proved what is and is not computable.
  Their work is mathematics — permanently true.
  Turing, Church, Post, Shannon, Cook, Karp

  TYPE B: ARCHITECTS
  ──────────────────
  Designed how machines should be built.
  Von Neumann, Babbage, Atanasoff, Zuse

  TYPE C: LANGUAGE BUILDERS
  ─────────────────────────
  Defined how humans talk to machines.
  Hopper, Backus, McCarthy, Wirth, Kay

  TYPE D: SYSTEM BUILDERS
  ───────────────────────
  Built the platforms everyone runs on.
  Thompson, Ritchie, Torvalds, Stallman,
  Berners-Lee, Cerf, Kahn

  TYPE E: PRACTITIONERS
  ─────────────────────
  Turned theory into products.
  Hollerith, Eckert+Mauchly, Engelbart,
  Jobs, Wozniak, Andreessen, Page, Brin
```

---

## Intellectual Dependency Graph

These ideas built on each other in identifiable chains:

```
  Leibniz (binary arithmetic, 1703)
      └─→ Boole (Boolean algebra, 1854)
              └─→ Shannon (circuits as Boolean logic, 1937 thesis)
                      └─→ Every digital circuit ever built

  Babbage (Analytical Engine, 1837)
      └─→ Lovelace (first algorithm, Note G)
      └─→ Hollerith (punched cards at census scale)
              └─→ IBM (Tabulating Machine Company, 1896)

  Hilbert (Entscheidungsproblem — "decision problem", 1928)
      └─→ Gödel (incompleteness theorems, 1931)
              └─→ Turing (halting problem undecidable, 1936)
              └─→ Church (lambda calculus, 1936)
                      └─→ McCarthy (Lisp, 1958)
                              └─→ Every functional language

  Turing (universal Turing machine, 1936)
      └─→ Von Neumann (stored-program architecture, 1945)
              └─→ Every von Neumann machine ever built
              └─→ Eckert+Mauchly (ENIAC, UNIVAC)

  Shannon (information theory, 1948)
      └─→ Hamming (error-correcting codes, 1950)
      └─→ Nyquist-Shannon sampling theorem
              └─→ All of digital signal processing
              └─→ All of data compression
              └─→ All of error-correcting codes (CDs, QR codes, TCP/IP)

  Hopper (first compiler A-0, 1952)
      └─→ Backus (Fortran, 1957; BNF notation, 1960)
      └─→ All compiled languages

  Thompson+Ritchie (Unix/C, 1969–1972)
      └─→ Torvalds (Linux, 1991)
      └─→ Every modern OS kernel
      └─→ C → C++ → Java → C# → Go → Rust (syntactic lineage)

  Dijkstra (shortest path, 1956)
      └─→ OSPF routing protocol
      └─→ A* pathfinding (GPS, games)

  Cook (NP-completeness, 1971)
      └─→ Karp (21 NP-complete reductions, 1972)
              └─→ Entire field of computational complexity theory
```

---

## Files in This Directory

| File | Era | Figures | Core Theme |
|------|-----|---------|------------|
| 01-MECHANICAL-ERA.md | 1820–1900 | Babbage, Lovelace, Hollerith | Mechanical computation, first programs |
| 02-THEORY-FOUNDATIONS.md | 1930s–1940s | Turing, Church, Post | What is computable? |
| 03-EARLY-COMPUTERS.md | 1940s | Von Neumann, Eckert+Mauchly, Atanasoff, Zuse | First real machines |
| 04-INFORMATION-THEORY.md | 1940s–1950s | Shannon, Nyquist, Hamming | Measure of information |
| 05-PROGRAMMING-LANGUAGES.md | 1950s–1970s | Hopper, Backus, McCarthy, Wirth | How to talk to machines |
| 06-ALGORITHMS-COMPLEXITY.md | 1950s–1970s | Dijkstra, Knuth, Cook, Karp | What can be solved efficiently? |
| 07-SYSTEMS-OS.md | 1960s–1990s | Thompson, Ritchie, Torvalds, Stallman | The platforms underneath everything |
| 08-PERSONAL-COMPUTING.md | 1960s–1980s | Kay, Engelbart, Jobs, Wozniak | Computing for individuals |
| 09-INTERNET-WEB.md | 1970s–2000s | Cerf, Kahn, Berners-Lee, Andreessen, Page, Brin | The connected world |

---

## Who to Cite for What — Master Index

| If you are talking about... | Cite |
|-----------------------------|------|
| Computability limits / halting problem | Turing (1936) |
| Lambda calculus / functional computation | Church (1936) |
| Stored-program architecture | Von Neumann (1945) |
| Information entropy | Shannon (1948) |
| Error-correcting codes | Hamming (1950) |
| First compiler | Hopper (1952) |
| First high-level language | Backus / Fortran (1957) |
| Lisp / recursion / garbage collection | McCarthy (1960) |
| Shortest-path algorithms | Dijkstra (1956) |
| Algorithm analysis / TAOCP | Knuth (1968–) |
| NP-completeness | Cook (1971) + Karp (1972) |
| Unix philosophy | Thompson + Ritchie (1969) |
| C language | Ritchie (1972) |
| Object-oriented programming | Kay / Smalltalk (1972) |
| Mouse / GUI / hypertext concept | Engelbart (1968 demo) |
| TCP/IP protocol | Cerf + Kahn (1974) |
| World Wide Web | Berners-Lee (1989) |
| Linux kernel | Torvalds (1991) |
| Free software / GPL | Stallman (1983) |
| PageRank / web search | Page + Brin (1998) |

---

## Common Confusion Points

**"Turing invented the computer."**
No. Turing proved theoretical limits of computation (1936) before any computer existed. Von Neumann's stored-program architecture (1945) is what all modern computers implement. Turing did design the ACE computer post-war, but that is not his primary contribution.

**"Von Neumann stole Eckert and Mauchly's ideas."**
The "First Draft of a Report on the EDVAC" (1945) bore only Von Neumann's name on a working draft, causing a priority dispute that lasted decades. Eckert and Mauchly held the stored-program concept prior to Von Neumann's involvement; the architecture is genuinely collaborative.

**"Ada Lovelace wrote the first program."**
Lovelace translated Menabrea's article on Babbage's Analytical Engine and added extensive notes, including Note G — an algorithm for computing Bernoulli numbers. It was never run (the Engine was never completed). Whether she conceived it independently or Babbage gave it to her is disputed, but the algorithm is mathematically real and non-trivial.

**"Shannon invented binary."**
Leibniz (1703), Boole (1854). Shannon's 1937 master's thesis proved that Boolean algebra maps directly to electrical switching circuits — the insight that made digital computing practical. He named it, not invented it.

**"Dijkstra's algorithm is just BFS."**
BFS finds shortest paths only on unweighted graphs. Dijkstra uses a priority queue and handles arbitrary non-negative edge weights. The correctness proof relies on the greedy frontier property: once a node is settled, its distance is final (proved via the triangle inequality).

**"The first computer was ENIAC."**
Priority disputes abound. Zuse's Z3 (1941, Germany) was relay-based and programmable. Atanasoff-Berry Computer (1942) was electronic but not general-purpose. Colossus (1943–44, Bletchley Park) was electronic and somewhat programmable but purpose-built. ENIAC (1945) was the first general-purpose electronic programmable computer.

**"Berners-Lee invented the internet."**
The internet (TCP/IP networking) predates the Web by 15+ years. Cerf and Kahn designed TCP/IP (1974); ARPANET goes to 1969. Berners-Lee invented the Web — HTTP protocol, HTML markup, and the URL scheme — as a document-sharing layer on top of the already-existing internet.
