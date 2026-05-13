---
type: concept
aliases: [Satisfiability Threshold Conjecture]
summary: The observation that for random k-SAT problems, there is a critical threshold in the ratio of clauses to variables where the probability of satisfiability sharply transitions from nearly 1 to nearly 0, and where problems are computationally hardest.
tags: [satisfiability, computational-complexity, phase-transition]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Satisfiability Threshold Conjecture

## The Phase Transition

The satisfiability threshold conjecture describes a phenomenon observed in random satisfiability problems. For a given problem type, such as 3-CNF, there is a critical value for the ratio of clauses to symbols (m/n). Below this threshold, sentences are almost always satisfiable, while above it, they are almost always unsatisfiable. The transition between these two regimes is extremely sharp.

## Critical Ratio for 3-CNF

For random 3-CNF problems, this critical threshold is located at a clause/symbol ratio of approximately 4.3. A graph in the text shows the probability of a random 50-symbol 3-CNF sentence being satisfiable dropping from near 1 to near 0 right around this ratio.

## Computational Hardness

The most computationally difficult SAT problems for both complete algorithms like DPLL and local search algorithms like WalkSAT are found at this phase transition boundary. Runtimes for these algorithms are relatively low for ratios far from the threshold but exhibit a sharp peak precisely at the critical ratio of about 4.3, where the problem's satisfiability is uncertain.

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*