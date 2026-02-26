# Personal Computing — Kay, Engelbart, Jobs, Wozniak

## Era Overview

```
COMPUTING FOR INDIVIDUALS: 1945–1984
======================================

  1945 ─── BUSH: "As We May Think" — Memex concept. Hyperlinked information machine.
           The intellectual ancestor of hypertext and the Web.

  1962 ─── ENGELBART: "Augmenting Human Intellect" — computing as cognitive tool.
           10-year research agenda begins at SRI.

  1963 ─── SUTHERLAND: Sketchpad — first GUI program. Direct manipulation.
           The intellectual ancestor of all graphical UIs.

  1968 ─── ENGELBART: "The Mother of All Demos"
           Mouse, windows, hypertext, collaborative editing, video conferencing
           — all demonstrated live, all non-existent elsewhere.

  1970 ─── XEROX PARC founded. Kay recruits many Engelbart alumni.

  1972 ─── KAY: Smalltalk-72. First OOP language with classes, objects, messages.

  1973 ─── XEROX ALTO — first personal computer with GUI, mouse, WYSIWYG editor.
           Never sold commercially. Used internally by Xerox.

  1975 ─── ALTAIR 8800. First personal computer kit. Gates+Allen write BASIC for it.

  1976 ─── APPLE I (Wozniak). Sold as a kit.
  1977 ─── APPLE II (Wozniak). Mass-market personal computer.
  1977 ─── TANDY TRS-80, COMMODORE PET — the 1977 trinity.

  1981 ─── IBM PC. x86 architecture. Open design. Third-party clones.

  1984 ─── MACINTOSH — mass-market GUI computer.
           Jobs saw the Alto at PARC, commercialized the concept.
```

---

## Douglas Engelbart (1925–2013)

### Bio Snapshot

American engineer and inventor. Oregon State, Berkeley. Stanford Research Institute (SRI) from 1957. Founded the Augmentation Research Center. Turing Award 1997 — given 30 years after his most important work. Spent his career watching others profit from his ideas while his research center lost funding.

### The Mother of All Demos (December 9, 1968)

Engelbart demonstrated a complete interactive computing system before 1,000 computer professionals at the Fall Joint Computer Conference in San Francisco. No one in the audience had seen anything like it.

```
WHAT THE DEMO SHOWED (1968)
============================

  THE SYSTEM: NLS (oN-Line System), running on SDS 940.

  MOUSE:
    A wooden block with two wheels on its underside.
    Moved a cursor on screen.
    First public demonstration of a pointing device.

  WINDOWS:
    Multiple windows on a single screen.
    Each window showed different content.

  HYPERTEXT:
    Documents with clickable links to other documents.
    Jump to a reference, return to origin.
    (Berners-Lee named his system after this concept, 23 years later.)

  COLLABORATIVE EDITING:
    Engelbart in San Francisco.
    Colleague Bill Paxton in Menlo Park.
    Both editing the same document simultaneously.
    (This was 1968. Google Docs appeared in 2006.)

  VIDEO CONFERENCING:
    Live video of Paxton in the presentation.
    Two-way audio.

  STRUCTURED DOCUMENTS:
    Hierarchical document structure.
    Outline view.
    Jump to any level.

  CHORD KEYBOARD:
    Five-key keyboard on left hand for modifiers.
    Still preferred by some power users for command shortcuts.
```

**Why it mattered**: Every interface element in the modern desktop — mouse, windows, hypertext links, collaborative editing — was demonstrated by Engelbart in 1968. He did not patent most of it, did not commercialize it effectively, and received comparatively little credit for decades.

**The gap between concept and product**: Engelbart's work was funded by ARPA and NASA for augmenting human intellect. It was not designed as a product. Xerox PARC (founded 1970) recruited many of Engelbart's former researchers and turned these concepts into the Alto (1973). Apple then commercialized PARC's work as the Macintosh (1984).

---

## Alan Kay (1940–present)

### Bio Snapshot

American computer scientist. Colorado (music), Utah (computer graphics). Xerox PARC 1970–1983. Atari, Apple, Disney, HP Labs, Viewpoints Research Institute. Turing Award 2003. Quotes: "The best way to predict the future is to invent it." "Object-oriented programming to me means only messaging, local retention and protection and hiding of state-process, and extreme late-binding of all things."

### The Dynabook Vision

Kay arrived at PARC with a vision he called the Dynabook: a personal computer the size of a notebook, with a display, interactive programming, and a library of knowledge accessible to anyone — including children. This was 1972.

```
THE DYNABOOK CONCEPT (1972)
============================

  What Kay imagined:
    - Portable, roughly A4 size
    - Flat screen display
    - Wireless communication
    - Personal permanent storage
    - Interactive programming environment
    - Designed for children as well as experts
    - A "metabook" — the last book

  What was available in 1972:
    - The cheapest computers: $20,000+
    - Storage: tape drives, large disk packs
    - Displays: CRTs the size of TV sets
    - Portability: not a concept

  Kay knew the Dynabook was 20–30 years away.
  He designed Smalltalk as the software for the Dynabook that
  didn't exist yet, building it on the hardware that did exist (Alto).

  The iPad (2010) is arguably the first Dynabook.
```

### Smalltalk and Object-Oriented Programming

Kay invented OOP — but his definition differs from what most programmers mean today:

```
KAY'S OOP — THE REAL DEFINITION
==================================

  The core idea: every object is a little computer.
  Objects communicate by SENDING MESSAGES.
  Objects can only affect each other through messages.
  Internal state is HIDDEN.

  "I made up the term 'object-oriented', and I can tell you I
  did not have C++ in mind." — Kay

  KAY'S THREE PRINCIPLES:
  1. Everything is an object.
  2. Objects communicate by sending and receiving messages.
  3. Objects have their own memory (state is local, hidden).

  SMALLTALK-80 — KEY FEATURES:
  ─────────────────────────────
  Classes:          Template for objects. Instance variables + methods.
  Inheritance:      Subclass extends superclass. Single inheritance.
  Message passing:  anObject someMessage: anArgument
  Everything:       Integers, booleans, classes are objects.
                    Even 'true' and 'false' are objects (True, False).
                    Even blocks (lambdas) are objects.

  SMALLTALK INNOVATIONS (first appearances):
  ───────────────────────────────────────────
  MVC (Model-View-Controller):
    Trygve Reenskaug + Smalltalk community (1979).
    Separates data (model), display (view), interaction (controller).
    Still the basis for ASP.NET MVC, Ruby on Rails, Angular, React.

  IDE as environment:
    Smalltalk's environment was the programming language.
    Browse, inspect, modify running objects.
    Hot reload while the program runs.
    Live Objects → a running system = a snapshot of all objects.
    Rails' console, Node REPL, Python ipython → Smalltalk descendants.

  Just-in-time compilation:
    Smalltalk-80 implemented a simple JIT (inline caches).
    The Deutsch-Schiffman optimization (1984) became the basis for
    V8 (JavaScript), HotSpot (Java JVM), and the .NET JIT.

  Garbage collection (independent of McCarthy):
    Smalltalk's GC was implemented independently and differently.
    It popularized generational GC for production systems.
```

**Smalltalk's legacy**: Smalltalk never dominated the market. It was too expensive to run (Xerox Alto, then specialized hardware). But its ideas are everywhere:

```
SMALLTALK'S DESCENDANTS
=========================

  Object-oriented languages:
    Objective-C (Cox, 1983) — Smalltalk message syntax + C
    Python (van Rossum, 1991) — "everything is an object"
    Ruby (Matsumoto, 1995) — explicitly Smalltalk-inspired
    Java (Gosling, 1995) — classes, inheritance, GC
    C# (Hejlsberg, 2000) — Java++ with better generics + LINQ

  IDE concepts:
    The modern IDE (browsing live objects, hot reload, REPL)
    traces to Smalltalk's image-based environment.
    Visual Studio's debugger/immediate window is a distant descendant.

  MVC pattern:
    Every web framework: Rails, Django, ASP.NET, Spring MVC.

  JIT compilation:
    V8 (Chrome/Node.js), HotSpot (JVM), CLR (.NET JIT).
    All use inline caches invented for Smalltalk.
```

---

## Steve Wozniak (1950–present) and Steve Jobs (1955–2011)

### Bio Snapshot

**Wozniak**: Silicon Valley native. HP engineer. Co-founded Apple. Designed Apple I and Apple II himself — hands-on engineering. The technical genius.

**Jobs**: Adopted, California. Calligraphy obsession at Reed College (directly influenced Mac typography). Xerox PARC visit in 1979 changed Apple's direction. Forced out of Apple 1985, returned 1997. Died of pancreatic cancer 2011.

### Apple I and Apple II (Wozniak's Designs)

```
WOZNIAK'S ENGINEERING PHILOSOPHY
===================================

  Minimize chip count.
  Elegant hardware design = fewer parts = lower cost = higher reliability.

  APPLE I (1976):
    First personal computer on a single PCB.
    Wozniak designed it to show off to the Homebrew Computer Club.
    Jobs convinced him to sell it. ~200 units sold at $666.66.
    The first Apple product.

  APPLE II (1977):
    8-bit 6502 CPU.
    Integer BASIC in ROM (written by Wozniak).
    8 expansion slots (Wozniak's fight with Jobs — Jobs wanted none).
    Color graphics output.
    Cassette tape storage (later: floppy disk drive).
    16K RAM expandable to 48K.

  DISK II (1978):
    Wozniak's floppy disk controller used 5 chips where competitors used 30.
    One of the most efficient hardware designs ever.
    Made Apple II the platform for VisiCalc (first spreadsheet, 1979).
    VisiCalc drove Apple II sales to businesses.
    The "killer app" concept — software selling hardware.
```

### Jobs and Xerox PARC (1979)

In late 1979, Jobs arranged an Apple engineering team visit to Xerox PARC in exchange for Apple stock options. Xerox PARC showed them the Alto — GUI, mouse, windows, WYSIWYG text editor.

```
WHAT JOBS SAW AT PARC (December 1979)
=======================================

  Alto computer with:
    - Mouse-driven graphical interface
    - Overlapping windows
    - Icons
    - WYSIWYG text editing (Bravo editor)

  Jobs's reaction: "You're sitting on a goldmine and you don't know it."

  What Xerox did: nothing. Xerox's business was copiers.
                  Computing was a side project.
                  The Alto was never commercially sold.

  What Jobs did: immediately redirected Apple's Lisa and Macintosh projects
                 toward a mass-market GUI computer.

  COMMON MISUNDERSTANDING:
    Jobs did not "steal" the GUI. The PARC visit was invited and agreed.
    Xerox received Apple stock as part of the deal.
    The legal dispute (Apple v. Microsoft, 1988) ended with Apple losing —
    the GUI concept itself was not protectable.
    Xerox later sued Apple (unsuccessfully).
```

### The Macintosh (1984)

```
MACINTOSH INNOVATIONS
======================

  Mass-market GUI:
    First GUI computer to succeed commercially.
    Price: $2,495. Expensive but not research-lab expensive.

  Typography:
    Jobs's calligraphy background → multiple proportional fonts.
    LaserWriter (1985) + PostScript → desktop publishing.
    Aldus PageMaker → layout software.
    Apple democratized typography.

  WYSIWYG:
    What You See Is What You Get.
    Screen display matched printed output.
    Revolutionary for people who had only seen text terminals.

  The 1984 ad (Ridley Scott):
    Aired once during the Super Bowl.
    "On January 24th, Apple Computer will introduce Macintosh.
    And you'll see why 1984 won't be like '1984'."
    IBM was the Big Brother.

  MACINTOSH'S INFLUENCE:
    Every GUI OS since: Windows 1.0 (1985) → Windows 3.1 → 95 → ...
    All descended from or react to the Mac interface conventions.
    File/Edit/View menus. Double-click to open. Drag to trash.
    These were Mac conventions, now universal.
```

---

## Comparison Table

| Figure | Key Contribution | When | Impact |
|--------|-----------------|------|--------|
| Engelbart | Mouse, windows, hypertext, collaborative editing | 1968 | Conceptual foundation of all GUIs |
| Kay | Smalltalk, OOP, Dynabook vision, MVC | 1972–1983 | OOP, IDE concept, JIT, MVC patterns |
| Wozniak | Apple I/II design, Disk II controller | 1976–1978 | Mass-market personal computer |
| Jobs | Mac GUI commercialization, product vision | 1984 | GUI as consumer product; typography; "killer app" |

---

## Who to Cite for What

| Concept | Figure |
|---------|--------|
| Mouse invention | Engelbart (1964 patent) |
| Hypertext concept | Engelbart (1968, Bush 1945) |
| Collaborative editing | Engelbart (1968 demo) |
| Object-oriented programming | Kay (Smalltalk-72) |
| MVC pattern | Reenskaug + Kay's Smalltalk group (1979) |
| JIT compilation (inline caches) | Deutsch + Schiffman (Smalltalk, 1984) |
| Dynabook / tablet concept | Kay (1972) |
| First personal computer (mass-market) | Wozniak (Apple II, 1977) |
| Desktop GUI (mass-market) | Jobs/Apple (Macintosh, 1984) |
| WYSIWYG | Engelbart/PARC (first), Jobs/Apple (mass market) |
| Desktop publishing | Jobs/Apple (LaserWriter + PageMaker, 1985) |

---

## Common Confusion Points

**"Apple invented the GUI."**
Xerox PARC built the first commercial GUI computer (Alto, 1973). Engelbart demonstrated the conceptual components (1968). Apple commercialized it at mass-market scale (1984). Microsoft copied the approach (Windows, 1985). The GUI is a case study in invention vs. commercialization.

**"OOP means classes and inheritance."**
Kay's definition: objects are computing nodes that communicate by messages. Hidden state. Late binding. C++ added classes and inheritance to C, calling it OOP — but Kay explicitly said this is not what he meant. Java and C# are closer to Kay's design, but still not Smalltalk's full dynamism. Go deliberately avoids classes and inheritance; Python and Ruby are closer to Smalltalk's spirit.

**"Wozniak designed everything at Apple."**
Apple I and Apple II: yes, entirely Wozniak. The Macintosh: Wozniak was largely absent (he had a plane crash in 1981, returned part-time). The Mac was designed by Jef Raskin (concept) and Jeff Williams + Susan Kare + the Mac team (execution) under Jobs's direction. Wozniak designed the hardware for early Apple; Jobs designed the product experience.

**"Jobs copied PARC, not invented anything."**
Jobs synthesized. PARC had the Alto in 1973 and did nothing commercial with it for a decade. Jobs saw it, correctly identified it as transformative, directed the resources to build the Mac, oversaw the design obsessiveness that made it usable, and sold it to the world. Synthesis at this level is genuinely creative. The integration of typography (his calligraphy interest), industrial design, and marketing was not at PARC.
