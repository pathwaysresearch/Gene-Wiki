---
type: concept
aliases: [DPLL Algorithm]
summary: The Davis-Putnam-Logemann-Loveland (DPLL) algorithm is a complete, backtracking-based search algorithm for deciding the satisfiability of propositional logic formulae in conjunctive normal form.
relationships:
  - target: walksat-algorithm
    type: alternative-to
  - target: satisfiability-threshold-conjecture
    type: performance-is-affected-by
tags: [satisfiability, search-algorithm, propositional-logic]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# DPLL Algorithm

## Overview

The DPLL algorithm is a recursive, backtracking-based search algorithm designed to determine if a given sentence in propositional logic is satisfiable. It operates on the sentence's Conjunctive Normal Form (CNF) representation and works with partial models.

## Core Heuristics

The algorithm's efficiency comes from several key heuristics applied at each step of the search. The `FIND-PURE-SYMBOL` heuristic finds a symbol that appears with only one polarity (e.g., only as P, never as ¬P) throughout the clauses and assigns it the value that makes those clauses true. The `FIND-UNIT-CLAUSE` heuristic finds a clause with only one unassigned literal and assigns the corresponding symbol the value required to satisfy that clause.

## Backtracking Search

If neither the pure symbol nor the unit clause heuristic can be applied, DPLL performs a standard backtracking search. It selects an unassigned proposition symbol, assigns it `true`, and recursively calls itself. If that branch fails to find a satisfying model, it backtracks and tries assigning the symbol `false`.

## Relationships

- **alternative-to**: [[walksat-algorithm|Walksat Algorithm]]
- **performance-is-affected-by**: [[satisfiability-threshold-conjecture|Satisfiability Threshold Conjecture]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*