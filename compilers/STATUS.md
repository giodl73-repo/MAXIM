# compilers/ — Status

**10 files | Complete ✅**

| File | Topic | Status |
|------|-------|--------|
| `00-OVERVIEW.md` | The compiler pipeline front-to-back — frontend/middle-end/backend split, the shared-middle insight (LLVM), AOT vs JIT spectrum, where each later guide fits; bridge from MIT automata/PLT theory to production compiler engineering | ✅ |
| `01-LEXING.md` | Lexical analysis — regex → NFA (Thompson) → DFA (subset construction) → minimization (Hopcroft), maximal munch, token streams, lexer generators (flex/re2c/Logos), the longest-match and keyword-vs-identifier engineering | ✅ |
| `02-PARSING.md` | Syntax analysis — recursive descent / LL(k) / Pratt vs the LR family (LR(0)/SLR/LALR(1)/LR(1)), what each class can and cannot handle, LALR conflict origins, parser generators (yacc/bison/ANTLR/tree-sitter), error recovery (panic-mode, GLR) | ✅ |
| `03-SEMANTIC-ANALYSIS.md` | Semantic analysis — AST vs parse tree, symbol tables and scope chains, name resolution, type checking vs type inference (Hindley-Milner / Algorithm W), unification, attribute grammars, the binder phase | ✅ |
| `04-INTERMEDIATE-REPRESENTATION.md` | IR design — three-address code, basic blocks, the control-flow graph, SSA form and why, φ-function placement via dominance frontiers, the SSA construction algorithm, leaving SSA | ✅ |
| `05-DATAFLOW-ANALYSIS.md` | Dataflow analysis — lattices and monotone frameworks, the meet operator and fixpoint iteration, reaching definitions / liveness / available expressions, dominators and the dominator tree, worklist algorithms | ✅ |
| `06-OPTIMIZATION.md` | Optimization passes — local/global/interprocedural, constant propagation/folding, GVN, dead code elimination, LICM and loop opts (unrolling, vectorization, strength reduction), inlining heuristics, the pass pipeline | ✅ |
| `07-REGISTER-ALLOCATION.md` | Register allocation — the interference graph, graph coloring (Chaitin-Briggs) with spilling and coalescing, linear scan and its live-interval model, SSA-based allocation, the JIT trade-off | ✅ |
| `08-CODE-GENERATION.md` | Code generation — instruction selection (maximal munch / BURS tiling / DAG), instruction scheduling (list scheduling, hazards), calling conventions and the ABI, prologue/epilogue, peephole, the assembler/linker handoff | ✅ |
| `09-RUNTIME-AND-GC.md` | The runtime — memory model and object layout, garbage collection (mark-sweep, copying/Cheney, generational, tri-color concurrent), the JIT and tiered compilation, deoptimization, stack maps and safepoints | ✅ |

## Coverage Notes

This directory is the **implementation depth** beneath two existing higher-level guides: the survey `computing/22-COMPILERS.md` (which compilers exist, who shares what, the JIT spectrum at ecosystem level) and the `programming-language-theory/` directory (lambda calculus, type theory, semantics — the *what programs mean* layer). Those are deliberately not re-derived here. This module engages the **engineering of real compilers**: the algorithms a backend team actually implements — subset construction, LALR table generation, SSA construction via dominance frontiers, dataflow lattices and fixpoint iteration, Chaitin graph-coloring allocation, instruction selection, and the runtime/GC that the generated code lives inside. The learner knows automata, formal languages, and type theory cold, so DFAs and CFGs are starting points, not lessons. Bridges run to LLVM, .NET/RyuJIT, V8, and the JVM throughout. Cross-references: `programming-language-theory/` (type inference, SSA semantics, CPS), `computing/22-COMPILERS.md` (ecosystem survey), `computer-architecture/` (pipelines, caches, ISAs that codegen targets), `os/` (loaders, virtual memory, the runtime/OS boundary), and `formal-methods/06-PROGRAM-ANALYSIS.md` (abstract interpretation, the lattice framework, translation validation).
