---
type: entity
aliases: [CHAFF Solver]
summary: A high-performance SAT solver developed in 2001 that could handle problems with millions of variables, marking a significant leap in the efficiency of solving propositional satisfiability problems.
relationships:
  - target: propositional-logic
    type: solves_problems_in
tags: [sat-solver, software, algorithm]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# CHAFF Solver

## Overview
CHAFF is a propositional satisfiability (SAT) solver developed by Moskewicz et al. in 2001. It represented a major breakthrough in the practical ability to solve large-scale SAT problems, particularly those arising from industrial applications like circuit verification.

## Key Innovations
The dramatic performance improvement of CHAFF was attributed to its use of several key techniques. It incorporated the watched literal indexing technique, which makes unit propagation very efficient, and clause learning techniques adapted from the Constraint Satisfaction Problem (CSP) community. These innovations allowed it to scale far beyond previous solvers.

## Impact and Legacy
CHAFF demonstrated that SAT solvers could effectively handle problems with millions of variables, a massive increase from the 10-15 variables manageable by the original DPLL algorithm in 1962. Its general approach proved highly influential, with most winning entries in the SAT competitions that began in 2002 being either descendants of CHAFF or using a similar design.

## Relationships

- **solves_problems_in**: [[propositional-logic|Propositional Logic]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*