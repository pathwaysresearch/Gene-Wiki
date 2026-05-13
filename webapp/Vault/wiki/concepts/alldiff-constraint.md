---
type: concept
aliases: [Alldiff Constraint]
summary: A global constraint specifying that all variables in its scope must take on distinct values.
relationships:
  - target: global-constraint
    type: is-a-type-of
tags: [constraint-satisfaction-problem, global-constraint]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Alldiff Constraint

## Definition
The Alldiff constraint is a global constraint which states that all the variables involved must have unique values. It is a common constraint in many real-world and puzzle problems where resources cannot be shared or items must be distinct.

## Inconsistency Detection
A simple method for detecting inconsistency with an Alldiff constraint is to compare the number of variables to the number of available values. If there are *m* variables involved in the constraint and they collectively have only *n* possible distinct values, the constraint cannot be satisfied if *m* > *n*. A more procedural algorithm involves iteratively removing any variable that has a singleton domain, deleting that value from the domains of the remaining variables, and repeating until no singletons are left. If at any point a domain becomes empty or the variable count exceeds the value count, an inconsistency is detected.

## Applications
The Alldiff constraint is fundamental to modeling problems like Sudoku, where each row, column, and 3x3 box must contain the digits 1-9 without repetition. It is also used in cryptarithmetic puzzles where different letters must map to different digits.

## Relationships

- **is-a-type-of**: [[global-constraint|Global Constraint]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*