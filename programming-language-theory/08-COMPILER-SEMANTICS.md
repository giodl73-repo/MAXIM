# Compiler Semantics: Verified Compilation, SSA, CPS, GHC Pipeline

## The Big Picture

Compiler semantics is about what it means for a compiler to be *correct* — and how to prove it. A compiler is correct if it preserves the meaning (semantics) of programs: every behavior of the compiled program corresponds to a behavior of the source program. Formal tools: semantic preservation theorems, CPS transforms, SSA form, and verified compilers like CompCert.

```
+--------------------------------------------------------------------------+
|                    COMPILER SEMANTICS LANDSCAPE                           |
+--------------------------------------------------------------------------+
|                                                                          |
|  THE CORRECTNESS PROPERTY:                                               |
|  ⟦compile(p)⟧_target = ⟦p⟧_source                                      |
|  "Running the compiled program gives the same results as the source"    |
|                                                                          |
|  SEMANTIC PRESERVATION CHAIN:                                            |
|  Source language → (each optimization pass) → Target language           |
|  Each pass must have a proof: ⟦pass(p)⟧ = ⟦p⟧                         |
|                                                                          |
|  KEY INTERMEDIATE REPRESENTATIONS:                                       |
|  CPS (continuation-passing style) — all calls are tail calls            |
|  ANF (administrative normal form) — all sub-expressions named           |
|  SSA (static single assignment) — each variable defined once            |
|  → These are DUALS: ANF ≡ SSA for functional programs                   |
|                                                                          |
|  GHC PIPELINE:                                                           |
|  Surface Haskell                                                         |
|   → Desugar → Core (System Fc: typed lambda calculus with coercions)   |
|   → Optimise (inlining, strictness analysis, specialisation)            |
|   → STG (Spineless Tagless G-machine: lazy evaluation model)           |
|   → Cmm (C--: portable assembly)                                        |
|   → C / LLVM / native code                                              |
|                                                                          |
|  LLVM IR: the universal typed assembly                                   |
|  Types, SSA form, dominance tree, CFG                                   |
+--------------------------------------------------------------------------+
```

---

## 1. CompCert: The Verified C Compiler

Xavier Leroy et al. (INRIA), formalized in Coq:

**The semantic preservation theorem**:
```
COMPCERT CORRECTNESS THEOREM:

  For any C program p:
  If p compiles successfully to assembly a,
  Then every behavior of a is also a behavior of p:

    compile(p) = Some a →
    ∀ behavior b, execute(a) ↓ b → execute(p) ↓ b

  (The "down arrow" ↓ b means "terminates with behavior b")

  For terminating programs: same result.
  For diverging programs: compiled version also diverges.
  For undefined behavior: CompCert's C source semantics has UB;
    CompCert does NOT guarantee preservation of UB behaviors.

WHAT COMPCERT INCLUDES:
  Multiple optimization passes: constant propagation, CSE (common
  subexpression elimination), dead code elimination, register allocation,
  instruction scheduling
  Each pass: formal semantics in Coq + proof of semantic preservation

THE INTERMEDIATE LANGUAGES (CompCert's pipeline):
  Clight → Csharpminor → Cminor → CminorSel →
  RTL (register transfer language: SSA-ish) →
  Linearize (remove φ-functions) →
  Mach (abstract assembly: stack frames) →
  PPC/x86/ARM assembly

  ~10 languages in the pipeline, each with formal semantics,
  each with a forward simulation proof
```

**Forward vs. backward simulation**:
```
FORWARD SIMULATION:
  If source takes a step s → s', then
  compiled code takes ≥0 steps t →* t' where s' and t' correspond

  Easier to prove, but doesn't directly give semantic preservation
  (need refinement from multiple target steps per source step)

BACKWARD SIMULATION:
  If compiled code terminates, source terminates with same result
  Semantically what we want, but harder to prove

COMPCERT USES: forward simulation + determinism of target
  → Forward simulation for deterministic target → backward simulation
  → Semantic preservation for terminating/diverging programs
```

---

## 2. CPS Transformation

The CPS transform (Plotkin 1975; Fischer 1972) converts a direct-style program into one where every function call passes an explicit continuation.

**Semantic preservation of CPS**:
```
CPS TRANSFORM PRESERVES SEMANTICS:

  Direct style:   f : A → B
  CPS:            f_CPS : A → (B → R) → R

  For any direct-style program p:
    ⟦p⟧ = ⟦CPS(p) id⟧
    (run the CPS-transformed program with identity continuation)

  The transform is SEMANTICS-PRESERVING:
    Every result of the direct-style program corresponds to
    a result of the CPS-transformed program with id continuation

PROOF SKETCH:
  By structural induction on terms.
  Values are straightforward (CPS(v) = λk. k v).
  Applications: CPS(t₁ t₂) = λk. CPS(t₁)(λf. CPS(t₂)(λv. f v k))
  → Each subcomputation threads continuations through.

SIGNIFICANCE FOR COMPILERS:
  Steele + Sussman 1976 "Rabbit" compiler: first to use CPS as IR
  Representation of tail calls: every call is a tail call in CPS
  → Stack frames unnecessary → tail call optimization free
  → No stack overflow for tail-recursive programs
  Continuations in CPS are first-class → call/cc implementable
```

---

## 3. Static Single Assignment (SSA)

SSA (Cytron, Ferrante, Rosen, Wegman, Zadeck 1991) — the standard IR for optimizing compilers:

**The form**:
```
SSA DEFINITION:
  Each variable is DEFINED (assigned) exactly once in the program text.
  All definitions dominate their uses.

EXAMPLE (converting to SSA):

  Direct style:
    x = 1
    if b:
      x = x + 1    ← second assignment to x
    y = x + 2

  SSA form:
    x₁ = 1
    if b:
      x₂ = x₁ + 1
    x₃ = φ(x₁, x₂)   ← φ-function: x₃ = x₁ if !b, x₂ if b
    y = x₃ + 2

  φ-FUNCTION: at a join point (where control flow merges),
    φ selects the appropriate version of a variable based on
    which control flow path was taken.

DOMINANCE:
  Block A dominates block B if every path from entry to B passes through A
  In SSA: definitions must dominate their uses
  Dominance tree = tree structure of the CFG's dominator relationships
```

**Why SSA enables optimizations**:
```
SSA-ENABLED OPTIMIZATIONS:

1. GLOBAL VALUE NUMBERING (GVN):
   Two definitions of the same form have the same value
   x₁ = a + b  and  x₂ = a + b →  x₁ = x₂ (replace all x₂ with x₁)
   Easy in SSA: definitions are unique; find equivalent definitions

2. DEAD CODE ELIMINATION:
   If a variable has no uses after definition → definition is dead
   (easy in SSA: track use sets; if empty, eliminate)

3. CONSTANT PROPAGATION:
   If x = 5 (constant definition), replace all uses of x with 5
   In SSA: definition site is unique → simple substitution

4. LOOP-INVARIANT CODE MOTION:
   SSA makes loop-invariant values obvious (definition not in loop body)

5. REGISTER ALLOCATION:
   SSA + interference graph → coloring = register allocation
   Variables with non-overlapping live ranges can share a register
```

---

## 4. GHC's Intermediate Languages

GHC compiles Haskell through a series of intermediate languages, each with a formal semantics:

```
GHC PIPELINE:

Surface Haskell
  ↓ Parser + renamer
Surface syntax with names resolved
  ↓ Type inference (HM + extensions)
Type-annotated AST
  ↓ Desugar
CORE (System Fc) ←── OPTIMIZATIONS HAPPEN HERE
  - Inlining
  - Specialization
  - Strictness analysis (convert thunks to evaluated)
  - Constant folding
  - Rewrite rules (user-defined and built-in)
  ↓
STG (Spineless Tagless G-machine) ←── LAZY EVALUATION MODEL
  - Closure analysis
  - Thunk/value distinction explicit
  ↓
Cmm (C--: portable low-level IR) ←── NEAR-MACHINE
  - Stack layout
  - GC calls
  - Register allocation
  ↓
C / LLVM IR / Native (via NCG)
```

**GHC Core (System Fc)**:
```
GHC CORE = SYSTEM F + COERCIONS:

  System Fc = System F extended with:
    Coercions: τ ~ σ   (proof that type τ equals type σ)
    Cast: t |> co      (change type of t using coercion co)
    Coercion arrows: τ ~# σ → ... (computationally relevant coercions)

  WHY COERCIONS:
    Newtypes: newtype Age = Age Int
      → Age and Int are different types but representationally equal
      → Coercion Age ~# Int   (erased at runtime, no cost)
      → newtype coercions implement zero-cost abstractions

    Type families: type family F a where F Int = Bool; F Bool = Int
      → F Int ~ Bool is a coercion proved by type family axiom
      → Can cast terms across type family equations

  CORE AS TYPED IR:
    Every term in Core is fully type-annotated
    The type checker for Core is the final type safety check
    Optimizations must produce well-typed Core (or crash GHC)
    → Optimization correctness is partly enforced by the type checker
```

**STG machine recap** (from 03-OPERATIONAL-SEM.md):
```
STG KEY INSIGHT FOR COMPILER:

  In STG, the evaluation model is explicit:
    CASE expression = the only forcing construct
    (enters a thunk if needed; pattern matches the result)

  ALL OTHER constructs are lazy:
    Function application: builds PAP or calls closure (but not if unevaluated)
    Let/letrec: allocates closures/thunks on heap without evaluating

  CONSEQUENCE FOR CODE GENERATION:
    Case → forced evaluation → straightforward code (load from heap, branch)
    Let → heap allocation + closure creation (GC-managed)
    Function call → either direct call (known function) or via info table

  ENTRY POINTS:
    Each heap object has an "entry code" (what to do when entered/forced)
    Thunk entry: start evaluating; overwrite with result
    Constructor entry: return the constructor (already in WHNF)
    Function entry: apply to argument
```

---

## 5. LLVM IR

LLVM IR is the contemporary "typed assembly" — a universal intermediate representation used by Clang (C/C++), Rust, Swift, Julia, and many others:

```
LLVM IR KEY FEATURES:

  SSA FORM: each virtual register defined once
  TYPES: integers (i8, i32, i64), floats, pointers, structs, arrays, functions
  THREE-ADDRESS CODE: at most two inputs per instruction
  EXPLICIT CONTROL FLOW GRAPH (CFG):
    Basic blocks with labels
    Terminator instructions: br, ret, switch
    φ-functions at join points

EXAMPLE LLVM IR:

  define i32 @factorial(i32 %n) {
  entry:
    %cond = icmp eq i32 %n, 0
    br i1 %cond, label %base, label %rec
  base:
    ret i32 1
  rec:
    %n1 = sub i32 %n, 1
    %r = call i32 @factorial(i32 %n1)
    %result = mul i32 %n, %r
    ret i32 %result
  }

LLVM OPTIMIZATION PASSES:
  mem2reg: promote memory to SSA virtual registers (converts alloca to SSA)
  instcombine: algebraic simplifications (x + 0 = x, etc.)
  inline: function inlining
  loop-vectorize: SIMD vectorization of loops
  gvn: global value numbering
  sccp: sparse conditional constant propagation

RUST → LLVM:
  Rust compiles to LLVM IR via MIR (Mid-level Intermediate Representation)
  MIR = Rust-specific ANF-like form for borrow checking + optimization
  MIR → LLVM IR → native code
  The borrow checker runs on MIR (after type checking, before LLVM)
```

---

## 6. Partial Evaluation and Futamura Projections

Partial evaluation (Jones, Sestoft, Sørensen 1993): specialize a program with respect to some of its inputs:

```
PARTIAL EVALUATION:

  A program p takes two inputs (s, d) where s is "static" (known at PE time)
  and d is "dynamic" (unknown; will be provided at runtime).

  Partial evaluator: pe : Program × StaticInput → ResidualProgram
    pe(p, s) = p_s  where  p_s(d) = p(s, d)

  p_s is specialized: static computation done; only dynamic part remains.

FUTAMURA PROJECTIONS (1971, 1999):

  Let int = an interpreter (int(prog, input) = result of running prog on input)
  Let pe = partial evaluator

  First projection:
    pe(int, prog) = prog_compiled
    "Partially evaluate an interpreter w.r.t. a program = compile the program"
    → You get a compiler FROM AN INTERPRETER

  Second projection:
    pe(pe, int) = compiler
    "Partially evaluate pe itself w.r.t. an interpreter = a compiler"
    → Deriving a compiler from pe + int without hand-coding the compiler

  Third projection:
    pe(pe, pe) = compiler_compiler
    "Apply pe to itself = a tool that generates compilers"

PRACTICAL SIGNIFICANCE:
  Template Haskell (staging): first-class code generation
  Multi-stage programming (MetaML, BER MetaOCaml):
    Code brackets and escapes: ⟨ code ⟩, ~e
    Stage-1 code generates stage-0 code
  JIT compilation: specialize interpreter at runtime
  → V8's turbofan, JVM's JIT are approximations of first Futamura projection
```

---

## Decision Cheat Sheet

| Topic | Key theorem/insight | Practical use |
|-------|---------------------|---------------|
| CompCert | ⟦compile(p)⟧ = ⟦p⟧, proved in Coq | Verified C compiler for safety-critical systems |
| CPS transform | Semantics-preserving; every call is tail call | Compiler IR; call/cc implementation |
| SSA form | Each var defined once; φ at joins | LLVM, GVN, DCE, register allocation |
| GHC Core (Fc) | System F + coercions; zero-cost newtypes | All GHC optimizations |
| GHC STG | Explicit lazy evaluation model | Thunk/closure code generation |
| LLVM IR | Typed SSA for multiple source languages | Rust, Swift, Julia backend |
| Partial evaluation | pe(int, prog) = compiled program (1st Futamura) | JIT, MetaML, Template Haskell |

---

## Common Confusion Points

**CompCert doesn't verify all C programs**: CompCert compiles a large subset of C99 but not all of it (some features unsupported or conservatively handled). It guarantees preservation only for programs without undefined behavior in the source. If your C has UB (dereferencing null, signed overflow), CompCert's semantic preservation theorem doesn't cover it.

**SSA and CPS are mathematically equivalent**: Kelsey (1995) proved that SSA programs correspond exactly to CPS programs (with appropriate restrictions). φ-functions ↔ formal parameters at join points. SSA is the imperative notation; CPS is the functional notation; they represent the same structure.

**GHC Core is not an optimization target you control directly**: You interact with Core through rewrite rules (RULES pragma in Haskell). The rules fire during GHC's optimization pass on Core. Understanding Core helps understand why some Haskell code optimizes poorly (e.g., dictionary-passing overhead from typeclasses in Core).

**Partial evaluation is not just "constant folding"**: Partial evaluation can unfold loops, inline recursive functions, eliminate conditionals — anything whose branching depends on static inputs. It's more like "computation at compile time" than constant folding. The Futamura projections show its theoretical power; practical partial evaluators (like supercompilers) are harder to implement correctly.
