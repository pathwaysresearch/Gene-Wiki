---
type: concept
aliases: [WalkSAT Algorithm]
summary: A local search algorithm for solving satisfiability problems, which iteratively flips variables in an unsatisfied clause based on a mix of greedy (min-conflicts) and random choices.
relationships:
  - target: dpll-algorithm
    type: alternative-to
  - target: satisfiability-threshold-conjecture
    type: performance-is-affected-by
tags: [satisfiability, local-search, stochastic-algorithm]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# WalkSAT Algorithm

## Overview

WalkSAT is described as one of the simplest and most effective local search algorithms for solving the propositional satisfiability problem (SAT). It does not perform a systematic search but instead tries to find a satisfying model by iteratively modifying a candidate assignment.

## How It Works

The algorithm begins with a random assignment of true/false values to all proposition symbols. It then iterates for a maximum number of flips. In each step, it randomly selects a clause that is currently unsatisfied by the model. It then chooses a symbol within that clause to flip its truth value.

## Flipping Strategy

The choice of which symbol to flip is probabilistic. With a given probability `p` (typically around 0.5), it performs a "random walk" by flipping a randomly selected symbol from the unsatisfied clause. With probability 1-`p`, it performs a "min-conflicts" step, greedily choosing to flip the symbol that results in the minimum number of unsatisfied clauses in the new state. If a satisfying model is found, it is returned; otherwise, the algorithm may return failure if the `max_flips` limit is reached.

## Relationships

- **alternative-to**: [[dpll-algorithm|Dpll Algorithm]]
- **performance-is-affected-by**: [[satisfiability-threshold-conjecture|Satisfiability Threshold Conjecture]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*