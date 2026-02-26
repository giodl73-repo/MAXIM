# Programming Language Pioneers — Hopper, Backus, McCarthy, Wirth

## Era Overview

```
FROM MACHINE CODE TO HIGH-LEVEL LANGUAGES: 1945–1980
======================================================

  1945–1950: All programming in machine code or assembly.
             Programmer = electrician + mathematician.

  1952 ─── HOPPER: A-0 compiler. First program that writes programs.
           Key insight: the computer can translate its own instructions.

  1957 ─── BACKUS et al.: Fortran I released. IBM 704.
           First widely used high-level language.
           Skeptics bet it would never outperform hand-coded assembly.
           It did — because humans code faster and make fewer errors.

  1958 ─── McCARTHY: Lisp. Symbolic computation, recursion, GC.
           First language where the language IS its own AST.

  1960 ─── BACKUS: BNF notation for ALGOL 60.
           All formal grammar description since traces to this.

  1968 ─── DIJKSTRA: "Go To Statement Considered Harmful" letter.
           Structured programming. Blocked GOTO from respectability.

  1970 ─── WIRTH: Pascal. Clean structured language for teaching.
  1972 ─── RITCHIE: C. Systems programming. (Covered in 07-SYSTEMS-OS.md)

  1975 ─── WIRTH: Modula. Separate compilation, modules.
  1984 ─── WIRTH: Oberon. Minimal language design philosophy.
```

---

## Grace Hopper (1906–1992)

### Bio Snapshot

American mathematician and US Navy Rear Admiral. Vassar BA, Yale PhD (mathematics, 1934). Joined Naval Reserve 1943, assigned to Bureau of Ordnance Computation Project at Harvard — the Mark I. Worked at Eckert-Mauchly on UNIVAC. Remained in Naval Reserve while at Remington Rand/UNIVAC; retired and called back three times. Final retirement at 79. Popularized the nanosecond demonstration (a piece of wire 11.8 inches long — the distance light travels in one nanosecond).

### The First Compiler

**Context**: In 1952, programming a UNIVAC meant writing in absolute machine code or assembly. Hopper recognized that the machine could be made to translate human-readable mathematical notation into the binary instructions it needed.

```
WHAT HOPPER BUILT — THE A-0 COMPILER (1952)
============================================

  Before A-0:
    Programmer writes each instruction as a binary code.
    Each machine model has different opcodes.
    Programs are not portable.
    Errors in manual translation are constant.

  A-0 (1952):
    A "compiler" in Hopper's sense was a library of subroutines.
    The "compiler program" assembled a running program from subroutine
    calls by selecting and copying subroutine code.
    Input: a set of subroutine calls
    Output: a complete machine-code program

  FLOW-MATIC (1955–1959):
    English-like syntax for business data processing.
    First language designed for non-mathematicians.
    Directly influenced COBOL.

  COBOL (1960):
    Committee effort (CODASYL), but Hopper's influence dominated.
    Hopper's key design principle: programs should read like English.
    Business data processing: files, records, moves, calculations.
    60 years later: still running $3 trillion/day in financial transactions.
```

**The key conceptual battle**: Hopper fought the prevailing belief that computers could only do arithmetic, not "translation," and that any "automatic programming" would be too slow to be practical. She later said the hardest part was not writing the compiler — it was convincing people it was possible.

**The first computer bug**: The famous moth found in a Harvard Mark II relay in 1947 was labeled "First actual case of bug being found" in a logbook — a play on the existing engineering term "bug." Hopper popularized the story. The moth is in the Smithsonian.

### COBOL's Longevity

```
COBOL IN 2025 — STILL RUNNING
===============================

  Why COBOL persists:
    - 95% of ATM transactions
    - 80% of in-person credit card transactions
    - Most Fortune 500 financial system cores
    - US Social Security Administration
    - Major insurance company policy systems

  Root cause:
    COBOL record-file-report model maps directly to business processes.
    Decades of audited, tested logic embedded in existing code.
    Rewrite risk > maintenance cost.

  Why it matters today:
    The Y2K crisis cost $300+ billion partly because COBOL code
    stored years as 2 digits — Hopper's original programs from the 1950s
    and 1960s were still running in 1999.
```

---

## John Backus (1924–2007)

### Bio Snapshot

Columbia dropout (twice), Columbia BA in mathematics. IBM research from 1950. Led the Fortran team. Also led the ALGOL committee. Turing Award 1977. Delivered his Turing Award lecture as a critique of the "von Neumann bottleneck" and an argument for functional programming — surprising given his Fortran history.

### Fortran

**The skeptics**: Fortran was announced in 1954. IBM's own engineers bet it would never produce code as efficient as hand-coded assembly. The standard argument: the compiler couldn't know what the programmer knew about the machine's specific behavior.

Backus bet it would — not because the compiler would be clever, but because hand-coded assembly was riddled with optimization errors that humans made from fatigue and complexity. Fortran I's compiler was correct more consistently than human assembly writers for real scientific programs.

```
FORTRAN I (1957) — TECHNICAL ACHIEVEMENTS
===========================================

  First working compiled language for scientific computation.
  IBM 704 target.

  Key innovations:
    DO loops          (mapped directly to hardware loop counter)
    IF/GOTO           (conditional branching)
    SUBROUTINES       (reusable code units)
    Format statements  (typed I/O)
    Array subscripts  (A(I,J) notation)

  Performance: within 20% of hand-optimized assembly on most programs.
  This demolished the compiler skeptics.

  The Fortran compiler itself: 25,000 lines of code,
  took 18 person-years to write.
  The most complex piece of software written to that date.
```

**Fortran's lineage**: Fortran → Fortran 77 → Fortran 90 → Fortran 2003 → Fortran 2018. Still the language of choice for HPC numerical computation (weather modeling, fluid dynamics, climate simulation) because its array semantics map well to vectorized hardware and its performance is competitive with C for numerical codes. The Fortran standard library for linear algebra (BLAS, LAPACK) underlies NumPy, MATLAB, R, and essentially all scientific computing.

### BNF Notation

Backus invented Backus-Naur Form (BNF) for the ALGOL 60 report (1960), co-developed with Peter Naur:

```
BNF — FORMAL GRAMMAR NOTATION
================================

  Rules:
    <symbol> ::= <expression>
    <expression> can include:
      literals    (terminals, written in quotes)
      <symbols>   (non-terminals, recurse)
      |           (alternatives)

  Example — simplified arithmetic expression grammar:
    <expr>   ::= <term> | <expr> "+" <term> | <expr> "-" <term>
    <term>   ::= <factor> | <term> "*" <factor> | <term> "/" <factor>
    <factor> ::= <number> | "(" <expr> ")"
    <number> ::= <digit> | <number> <digit>
    <digit>  ::= "0" | "1" | "2" | ... | "9"

  This grammar is unambiguous: parsing is deterministic.
  The recursive structure encodes operator precedence and associativity.

  Extended BNF (EBNF) adds: * (repetition), + (one or more), ? (optional)

  Every language specification since 1960 uses BNF or EBNF.
  ANTLR, yacc/bison, and every parser generator read BNF-derived notation.
  The C# language specification uses BNF notation throughout.
```

---

## John McCarthy (1927–2011)

### Bio Snapshot

Princeton PhD (mathematics). MIT professor. Stanford AI Lab founder (1962). Turing Award 1971. Coined the term "artificial intelligence" (1956 Dartmouth conference). Also invented time-sharing operating systems (while at MIT). Committed libertarian; wrote about computer rights and long-term ethics of AI.

### Lisp

McCarthy invented Lisp (List Processing) in 1958 while designing a better language for AI research at MIT. The defining characteristic: the language is defined in terms of itself. The syntax is the AST.

```
LISP — THE FOUNDATIONAL IDEAS (1960)
======================================

  S-EXPRESSIONS (symbolic expressions):
    Atoms:  x, 42, "hello", nil, t
    Lists:  (a b c)  =  (cons a (cons b (cons c nil)))

  Everything is either an atom or a list.
  Code is data: (+ 1 2) is a list whose first element is the symbol +.

  THE SEVEN PRIMITIVES (McCarthy's 1960 paper):
    (car x)          head of list
    (cdr x)          tail of list
    (cons x y)       construct a new list
    (atom x)         is x an atom?
    (eq x y)         are two atoms equal?
    (cond ...)       conditional (if-then-else)
    (lambda (x) ...) anonymous function

  Everything else can be built from these seven.

  EVAL — the universal function:
    McCarthy defined eval in terms of Lisp itself.
    An interpreter for Lisp, written in Lisp.
    This is the metacircular evaluator.
    It means: Lisp is its own metalanguage.

  (defun factorial (n)
    (cond ((= n 0) 1)
          (t (* n (factorial (- n 1))))))
```

**The key innovations McCarthy bundled into Lisp**:

```
LISP INNOVATIONS — FIRST APPEARANCES
======================================

  Recursion as primary control structure
    (instead of loops + iteration)

  Garbage collection
    McCarthy needed dynamic allocation with automatic cleanup.
    First GC: mark-and-sweep (1960).
    All modern GCs (JVM, .NET CLR, V8) trace to this design.

  First-class functions (functions as values)
    Lambda expressions. Closures.
    Functions passed as arguments, returned as values.
    C# delegates, LINQ, functional APIs — all Lisp descendants.

  Dynamic typing
    Types checked at runtime, not compile time.
    Python, Ruby, JavaScript — same design choice.

  Read-Eval-Print Loop (REPL)
    Interactive development environment.
    Still in every language's toolchain.

  Homoiconicity: code = data
    Lisp programs are Lisp lists.
    This enables macros: programs that transform programs.
    The basis for metaprogramming and DSLs.
```

**Lisp's descendants**: Common Lisp, Scheme, Racket, Clojure (Lisp on JVM), Emacs Lisp. The lambda/closure concept spread to every major language by 2000. C# 2.0 (2005) added anonymous methods; C# 3.0 (2007) added lambda expressions and LINQ — these are McCarthy's ideas from 1960.

### Artificial Intelligence

McCarthy organized the 1956 Dartmouth Summer Research Project on Artificial Intelligence — the conference that named the field. He also developed:
- **LISP** as the primary language for AI research for 40 years
- **Situation calculus**: formal logic for reasoning about actions and change
- **Circumscription**: a form of non-monotonic reasoning
- **Time-sharing**: the concept that multiple users could share one computer simultaneously (directly leading to Unix, multi-user OSes)

---

## Niklaus Wirth (1934–2024)

### Bio Snapshot

Swiss computer scientist. ETH Zurich. Designed Pascal (1970), Modula-2 (1978), Oberon (1988), and Oberon-2. Turing Award 1984. Known for "Wirth's Law": software gets slower faster than hardware gets faster. Died January 2024 at 89.

### Pascal

Pascal (1970) was designed explicitly to teach structured programming — the Dijkstra/Hoare principles that programs should be comprehensible structures, not spaghetti code.

```
PASCAL'S DESIGN PRINCIPLES
============================

  Structured control flow:
    if-then-else, while-do, for-to-do, case, with
    No unstructured goto needed for normal programming

  Strong static typing:
    Every variable declared with explicit type.
    Compiler catches type errors before execution.
    Arrays have defined bounds (range checking optional).

  Records (structs) and variant records (tagged unions):
    Direct precursor to C structs, C# structs/classes.

  Procedures and functions as first-class units:
    Parameters by value and by reference (var keyword).

  Clean syntax:
    begin/end blocks (not Algol's more complex structure).
    Semicolons between statements (not terminators).

  Pascal became:
    - THE teaching language in universities 1970s–1990s
    - Turbo Pascal (Borland, 1983) → commercial success
    - Delphi (Borland) → Object Pascal, still alive
    - Modula-2 → modules, separate compilation
    - Oberon → minimal, safety-focused systems language
```

**Wirth's influence on the field**:
- **Pascal**: taught structured programming to a generation; Turbo Pascal made fast compiled programs accessible on PCs
- **Modula-2**: first widespread language with explicit modules and separate compilation — directly influenced Ada, and conceptually influenced Java packages, .NET namespaces
- **Oberon**: influenced Go (Wirth's ETH colleague Ken Nygaard influenced Go's authors; Rob Pike studied under Thompson, and Pike was at Bell Labs — but Wirth's minimalism is cited as an inspiration for Go's design philosophy)
- **PL/0, Lola**: pedagogical compilers still used for teaching compiler construction

---

## Comparison Table

| Figure | Life | Language(s) | Year | Key Innovation |
|--------|------|-------------|------|---------------|
| Hopper | 1906–1992 | FLOW-MATIC, COBOL; A-0 compiler | 1952–1960 | First compiler; English-like business language |
| Backus | 1924–2007 | Fortran, ALGOL; BNF | 1957–1960 | First practical compiled language; formal grammar notation |
| McCarthy | 1927–2011 | Lisp | 1958–1960 | Recursion, GC, first-class functions, homoiconicity |
| Wirth | 1934–2024 | Pascal, Modula-2, Oberon | 1970–1988 | Structured programming in language design; minimalism |

---

## Who to Cite for What

| Concept | Figure |
|---------|--------|
| First compiler | Hopper (A-0, 1952) |
| English-like programming language | Hopper (FLOW-MATIC, COBOL) |
| COBOL / business data processing | Hopper |
| First practical compiled language | Backus (Fortran, 1957) |
| BNF formal grammar notation | Backus (+ Naur, 1960) |
| Recursion as programming concept | McCarthy (Lisp, 1958) |
| Garbage collection (first) | McCarthy (Lisp mark-and-sweep, 1960) |
| First-class functions / closures | McCarthy (Lisp lambda) |
| REPL (Read-Eval-Print Loop) | McCarthy (Lisp) |
| Homoiconicity / code as data | McCarthy (Lisp) |
| Structured programming in language | Wirth (Pascal) |
| Module system / separate compilation | Wirth (Modula-2) |

---

## Common Confusion Points

**"COBOL is dead."**
There are an estimated 200–240 billion lines of COBOL in production. More COBOL code is written every year than most people realize. The pandemic stimulus check distributions in the US were delayed because state unemployment systems ran on COBOL and needed emergency modifications — and there were not enough COBOL programmers.

**"Fortran was replaced by C."**
For systems programming, yes. For numerical computation, Fortran is still competitive and sometimes preferred. The BLAS and LAPACK libraries (Fortran) are the numerical core of NumPy, SciPy, MATLAB, and R. When you call `numpy.dot()`, you are likely calling Fortran code.

**"McCarthy invented functional programming."**
He invented Lisp, which is a functional language. The theoretical foundations are Church's lambda calculus (1936). The direct functional programming movement (ML, Haskell) traces to ML (Milner, 1973), which was designed independently of Lisp but converged on similar lambda-based semantics.

**"Wirth's languages failed."**
Pascal was the dominant teaching language for 20+ years. Turbo Pascal sold millions of copies. Delphi (Object Pascal) had hundreds of thousands of developers. Modula-2 influenced Ada. Oberon influenced Go. "Failed" because they did not dominate systems programming — but they shaped the thinking of everyone who did.
