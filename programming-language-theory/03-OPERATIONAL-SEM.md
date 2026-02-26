# Operational Semantics: Small-Step, Big-Step, Abstract Machines

## The Big Picture

Operational semantics gives programming languages precise mathematical meaning by specifying how programs execute — step by step. The abstract machine perspective goes further: it shows exactly how to implement evaluation efficiently. Every language runtime is an abstract machine.

```
+--------------------------------------------------------------------------+
|                    OPERATIONAL SEMANTICS LANDSCAPE                        |
+--------------------------------------------------------------------------+
|                                                                          |
|  BIG-STEP (Natural)          SMALL-STEP (SOS)                           |
|  e ⇓ v                       e → e'                                     |
|  "e evaluates to v"          "e steps to e' in one step"               |
|  Elegant specification       Models intermediate states                 |
|  Cannot distinguish           Distinguishes stuck from diverging        |
|  stuck from diverging         → Progress theorem is expressible         |
|                                                                          |
|  ABSTRACT MACHINES (implementations of operational semantics):          |
|                                                                          |
|  SECD (Landin 1964)   CEK (Felleisen 1987)   Krivine (1985)            |
|  Stack, Env,          Closure, Env,           CBN, environment-based    |
|  Control, Dump        Kontinuation            No closures needed        |
|                                                                          |
|  G-machine/STG (Johnsson 1984, Peyton Jones 1992)                      |
|  Spineless Tagless G-machine: GHC's lazy evaluator                     |
|  Thunks, graph reduction, sharing                                       |
|                                                                          |
|  CPS TRANSFORM: every function call is a tail call                      |
|  ANF: every sub-expression named; evaluation order explicit             |
|  → Basis of compiler intermediate representations                      |
+--------------------------------------------------------------------------+
```

---

## 1. Big-Step Semantics (Natural Semantics)

Gilles Kahn (1987) formalized big-step semantics. The judgment is `e ⇓ v`: expression e evaluates to value v.

```
BIG-STEP RULES FOR CBV λ-CALCULUS:

  Values are either λ-abstractions or base values (n, b, ...)

  ───────────         (BS-Val)
  v ⇓ v              (values evaluate to themselves)

  e₁ ⇓ λx.e    e₂ ⇓ v₂    e[v₂/x] ⇓ v
  ────────────────────────────────────     (BS-App)
  e₁ e₂ ⇓ v

  e₂ ⇓ v₂    e[v₂/x] ⇓ v
  ─────────────────────────              (BS-Let)
  let x = e₂ in e ⇓ v

READING: derivation trees are proof trees showing the evaluation
         Each rule fires when its premises hold

LIMITATION:
  Diverging programs: (Y id) doesn't have a derivation
  Stuck programs: 1 + true doesn't have a derivation
  BIG-STEP CANNOT DISTINGUISH: which of these is it?
  → You can't express "this program doesn't typecheck" vs.
    "this program loops" in big-step
  → Small-step distinguishes them: stuck has no step; diverging has infinitely many
```

---

## 2. Small-Step Semantics (SOS)

Gordon Plotkin (*A Structural Approach to Operational Semantics*, 1981):

```
SMALL-STEP RULES FOR CBV λ-CALCULUS:

  Values: v ::= λx.t | n | b | ...

  ─────────────────────────               (S-Beta)
  (λx.t) v → t[v/x]                      (fire only when argument is a value)

  t₁ → t₁'
  ─────────────                           (S-App1)
  t₁ t₂ → t₁' t₂                         (evaluate function position first)

  t₂ → t₂'
  ─────────────────                       (S-App2)
  v t₂ → v t₂'                           (function is value; evaluate argument)

PROGRESS theorem is expressible:
  A term t is "stuck" if it's not a value AND no rule applies
  Progress: if ⊢ t : τ then t is a value OR ∃t' : t → t'
  (well-typed terms never get stuck)

MULTI-STEP:
  t →* t' means t steps to t' in zero or more steps
  t is in normal form if no t' exists with t → t'

DETERMINISM: CBV small-step is deterministic
  If t → t₁ and t → t₂ then t₁ = t₂
  (evaluation order is fixed by the rules; one active redex at a time)
  Determinism is a property of the rules, not λ-calculus generally
```

---

## 3. The SECD Machine

Landin (1964) — the first formally specified interpreter. SECD = Stack, Environment, Control, Dump.

```
SECD MACHINE STATE: (S, E, C, D)
  S: Stack of values (operand stack)
  E: Environment (variable → value mapping)
  C: Control (list of terms/operations to evaluate)
  D: Dump (saved (S,E,C) triples — continuation stack for function calls)

TRANSITIONS:

  Apply (function call):
    When function + arg on stack:
    Save (S, E, C) onto D (the "return address")
    Set S = [], E = E[param → arg-value], C = [body]
    Resume with new frame

  Return:
    When C empty (function body evaluated), result is top of S
    Restore (S, E, C) from D (the saved frame)
    Push result on restored S

  Variable lookup:
    Push E(x) onto S

  Abstraction:
    Push closure (λx.t, E) onto S  ← captures current environment

SIGNIFICANCE:
  First machine to make closures explicit
  Showed how to implement higher-order functions without substitution
  "Dump" is an explicit continuation stack — precursor to call/cc

LIMITATION:
  The return address (Dump) is only for function call/return
  Cannot naturally express general first-class continuations
  → CEK machine solves this
```

---

## 4. The CEK Machine

Matthias Felleisen and Dan Friedman (1987). CEK = Closure, Environment, Kontinuation.

```
CEK MACHINE STATE: ⟨t, ρ, κ⟩
  t: term being evaluated (or value)
  ρ: environment (variable → closure)
  κ: continuation (what to do with the result)

  CLOSURE: ⟨t, ρ⟩  (term + captured environment)

CONTINUATION FORMS:
  mt         (empty continuation = program done)
  ar(t₂, ρ, κ)  (evaluating function; next: evaluate argument t₂)
  fn(⟨λx.t,ρ'⟩, κ) (have closure; next: apply to argument)

TRANSITIONS:

  Variable:
  ⟨x, ρ, κ⟩ → ⟨ρ(x), ρ', κ⟩    (look up; ρ(x) = ⟨t', ρ'⟩)

  Application:
  ⟨t₁ t₂, ρ, κ⟩ → ⟨t₁, ρ, ar(t₂, ρ, κ)⟩   (evaluate function first)

  Function ready (got a closure from evaluating t₁):
  ⟨λx.t, ρ', ar(t₂, ρ, κ)⟩ → ⟨t₂, ρ, fn(⟨λx.t,ρ'⟩, κ)⟩

  Argument ready:
  ⟨v, ρ, fn(⟨λx.t,ρ'⟩, κ)⟩ → ⟨t, ρ'[x→⟨v,ρ⟩], κ⟩

  Done:
  ⟨v, ρ, mt⟩ → DONE (v is the answer)

WHY CEK IS IMPORTANT:
  The continuation κ is first-class — it's part of the machine state
  call/cc (call-with-current-continuation) = capture κ as a value
  Continuations = reified machine state → can implement:
    - Coroutines
    - Backtracking
    - Exceptions
    - Async/await (delimited continuations)

CEK IS COMPOSITIONAL:
  Any step-by-step reduction of small-step semantics corresponds exactly
  to a sequence of CEK transitions — machine implements semantics directly
```

---

## 5. The Krivine Machine

```
KRIVINE MACHINE: implements CALL-BY-NAME (CBN)

State: (t, e, s)
  t: term
  e: environment
  s: stack of closures (arguments)

TRANSITIONS:

  Variable: (x, e, s) → (t, e', s)  where e(x) = (t, e')

  Application: (t₁ t₂, e, s) → (t₁, e, (t₂,e)::s)
               (push argument as closure onto stack; don't evaluate yet)

  Abstraction: (λx.t, e, c::s) → (t, e[x→c], s)
               (pop closure from stack; bind to parameter)

KEY INSIGHT:
  Arguments are never evaluated before passing (call-by-name)
  No "ar" continuation needed — arguments stay on stack as unevaluated closures
  This is the environment-based CBN implementation

  Call-by-need (Haskell): same but closures are SHARED and MEMOIZED
  A "thunk" in Haskell is a heap-allocated Krivine closure + result cache
```

---

## 6. GHC's Spineless Tagless G-machine (STG)

Simon Peyton Jones (1992) — the foundation of GHC's code generation:

```
STG DESIGN GOALS:
  Implement lazy (call-by-need) evaluation efficiently on real hardware
  Model closures, thunks, and sharing precisely
  Generate efficient native code

KEY CONCEPTS:

1. THUNKS (unevaluated closures):
   Every expression that isn't evaluated is a heap-allocated closure
   Closure = code pointer + captured environment
   Evaluating = calling the code pointer (ENTERS the closure)

2. SPINELESS:
   Traditional graph reduction uses a "spine" of applications
   STG avoids building the spine explicitly
   → Direct function calls (more efficient on modern hardware)

3. TAGLESS:
   Traditional lazy implementations tag each heap object with its type
   STG identifies type from the entry point code (no runtime tag needed)
   → Removes one level of indirection for type dispatch

STG LANGUAGE (GHC's intermediate language just above C--):

  Bindings: f = λ{free vars}. λx₁...xₙ → body
  Calls: f x₁ x₂  (all arguments at call site; no partial application handled here)
  Case:  case scrut of pat₁ → e₁ | ... | patₙ → eₙ
         (ONLY case forces evaluation — the single lazy-forcing construct)

HEAP OBJECTS:
  FUN closure (not yet applied)
  PAP partial application (applied to too few args)
  CON data constructor (fully applied)
  THUNK unevaluated expression (being computed or waiting)
  BLACKHOLE circular reference detection (thunk currently being evaluated)

THE EVALUATION MODEL:
  Every expression is either:
    Already in WHNF (value/constructor) → done
    A thunk → enter it (call the code pointer)
  Case is the only forcing construct
  Pattern match forces to WHNF
```

---

## 7. Continuation-Passing Style (CPS)

CPS transform converts every function call to a tail call:

```
CPS TRANSFORM (CBV):

  [[ x ]]_k         = k x
  [[ λx.t ]]_k      = k (λx. λk'. [[ t ]]_k')
  [[ t₁ t₂ ]]_k    = [[ t₁ ]]_(λf. [[ t₂ ]]_(λv. f v k))

  Every call passes an explicit continuation k (what to do with result)
  Every call site is a tail call

EXAMPLE:

  (λx. x + 1) 2
  CBV: evaluate arg, substitute, evaluate body
  CPS: (λk. (λx. λk'. k' (x+1)) 2 k) id
     = (λx. λk'. k' (x+1)) 2 id
     = (λk'. k' (2+1)) id
     = id (2+1)
     = id 3
     = 3

WHY COMPILERS USE CPS:
  Every call is a tail call → no runtime call stack needed
  All control flow is explicit (loops, exceptions, coroutines all visible)
  Easy to implement call/cc (continuation is just a value)
  Enables optimizations: inlining continuations, tail call elimination

GHC USED CPS AS IR until ~2004:
  Core → CPS IR → code generation
  Now uses Cmm (C--) instead, which is more machine-code-like
  But the STG machine is semantically CPS-based
```

**Administrative Normal Form (ANF)** — alternative to CPS:
```
ANF: every sub-expression is named; no nesting

Original:      (f (g x)) + 1
ANF:           let tmp1 = g x in
               let tmp2 = f tmp1 in
               let tmp3 = tmp2 + 1 in
               tmp3

COMPARISON:
  CPS: control flow explicit via continuations
  ANF: control flow implicit (sequential naming); simpler to read
       but semantically equivalent to CPS

  Both give: evaluation order explicit, each intermediate result named
  ANF is closer to SSA (static single assignment) in LLVM IR
  → GHC's Core is ANF-like; LLVM uses SSA; they're dual representations

CPS vs. ANF TRADEOFF:
  CPS: easy to implement call/cc; algebraically cleaner
  ANF: easier to read; closer to register-based code; better for humans
  Compiler IR: ANF/SSA preferred; denotational proofs: CPS preferred
```

---

## Decision Cheat Sheet

| Machine/Style | Evaluation | First-class continuations | Sharing | Use |
|---------------|-----------|--------------------------|---------|-----|
| SECD | CBV | No (dump is implicit) | No | Historical; pedagogical |
| CEK | CBV | Yes (κ is first-class) | No | Implementing call/cc |
| Krivine | CBN | No | No | CBN semantics |
| STG | CBNeed (lazy) | Via stack | Yes (thunks) | GHC production |
| CPS transform | CBV (transformed) | Yes | No | Compiler IR |
| ANF | CBV | No | No | LLVM/compiler IR |

---

## Common Confusion Points

**Big-step can't express progress**: In big-step semantics, the judgment e ⇓ v either has a derivation or doesn't. A stuck term (type error at runtime) and a diverging term both have no derivation — you can't tell them apart. Small-step semantics expresses both: stuck = no applicable rule (not a value); diverging = infinite rule chain.

**CPS is a transform, not a calling convention**: CPS *transforms* a direct-style program into one where every call passes an explicit continuation. It doesn't mean the compiled code actually passes continuations at runtime — good CPS compilers optimize them away (continuation-passing style compilation ≠ continuation-passing implementation).

**Thunks in GHC are black holes until evaluated**: When a thunk starts evaluating, GHC replaces it with a black hole closure. If another thread tries to evaluate the same thunk simultaneously, it blocks (and can detect cycles). This is how GHC handles sharing and lazy evaluation thread-safely.

**ANF and SSA are duals**: In ANF, every sub-expression is a named let-binding. In SSA, every variable is assigned exactly once with φ-functions at join points. They express the same structure: explicit naming of intermediate results. The difference is purely operational: ANF is functional (substitution model); SSA is imperative (assignment model).
