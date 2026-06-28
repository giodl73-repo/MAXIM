# combinatorics/ — Status

## Files

| File | Topic | Status |
|------|-------|--------|
| 00-OVERVIEW.md | The combinatorics landscape: enumerative, extremal, algebraic, probabilistic; the four core questions | ✅ |
| 01-COUNTING-BASICS.md | Rules of sum/product, permutations/combinations, the twelvefold way, multisets | ✅ |
| 02-BINOMIAL-AND-IDENTITIES.md | Binomial theorem, Pascal's triangle, Vandermonde, hockey stick, multinomial coefficients | ✅ |
| 03-GENERATING-FUNCTIONS.md | Ordinary vs exponential generating functions, operations, solving recurrences, partitions | ✅ |
| 04-INCLUSION-EXCLUSION.md | The principle, derangements, surjection counts, the sieve, Bonferroni bounds | ✅ |
| 05-RECURRENCES.md | Linear recurrences, characteristic equations, Catalan recurrence, divide-and-conquer counts | ✅ |
| 06-PIGEONHOLE-AND-RAMSEY.md | Pigeonhole, Ramsey numbers R(s,t), bounds, van der Waerden, Schur | ✅ |
| 07-SPECIAL-NUMBERS.md | Catalan, Stirling 1st/2nd, Bell, Eulerian numbers, integer partitions | ✅ |
| 08-PROBABILISTIC-METHOD.md | First/second moment, Lovász local lemma, expectation and alteration arguments | ✅ |
| 09-EXTREMAL-AND-DESIGN.md | Turán, Dilworth, Sperner, Erdős–Ko–Rado, Latin squares, block designs, coding bridge | ✅ |

## Coverage Notes

Combinatorics — the mathematics of discrete counting, arrangement, and structure — is partitioned here into its four classical pillars: **enumerative** (how many?), **extremal** (how large/small can a structure be under a constraint?), **algebraic** (generating functions, symmetric functions, the algebra behind the counts), and **probabilistic** (existence proofs via random construction). This directory deliberately covers *enumerative, extremal, and algebraic* combinatorics and the probabilistic method. It does **not** re-derive graph algorithms (see `graph-algorithms/`) or probability theory and its limit laws (see `probability-statistics/`); it borrows from both. Bijective proofs, generating-function machinery, inclusion–exclusion, recurrence solving, the pigeonhole/Ramsey theory of unavoidable structure, the special counting sequences (Catalan, Stirling, Bell, Eulerian, partitions), the probabilistic method, and the extremal/design-theory results (Turán, Dilworth, Erdős–Ko–Rado, Latin squares, Steiner systems) form the spine. Bridges to CS run throughout: counting for the analysis of algorithms and complexity (#P, permanent), coding theory via designs, and hashing/derandomization via the probabilistic method. Cross-references: `number-theory/` (partitions, multiplicative structure), `abstract-algebra/` (group actions, Burnside/Pólya, finite fields behind designs), `probability-statistics/` (the underlying probability), `cryptography/` (codes, combinatorial designs).
