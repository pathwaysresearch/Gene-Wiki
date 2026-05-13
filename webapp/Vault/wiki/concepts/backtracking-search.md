---
type: concept
aliases: [Backtracking Search]
summary: A depth-first search algorithm for solving Constraint Satisfaction Problems by incrementally building a solution and abandoning a path (backtracking) as soon as it violates a constraint. A depth-first search algorithm commonly used for solving Constraint Satisfaction Problems (CSPs) by incrementally building candidate solutions and abandoning a path as soon as it violates any constraints.
relationships:
  - target: chronological-backtracking
    type: is-a-type-of
  - target: conflict-directed-backjumping
    type: is-an-improvement-on
  - target: least-constraining-value-heuristic
    type: uses
  - target: maintaining-arc-consistency
    type: uses
  - target: constraint-satisfaction-problems
    type: solves
  - target: minimum-remaining-values-heuristic
    type: uses
  - target: conflict-directed-backjumping
    type: is-a-specialization-of
tags: [search-algorithm, csp-solver, depth-first-search, search-algorithms, csp, ai]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Backtracking Search

## Definition
Backtracking search is a form of depth-first search used for solving Constraint Satisfaction Problems (CSPs). The algorithm incrementally assigns values to variables one at a time, and if an assignment violates a constraint, it backtracks to the previous choice point and tries a different value.

## Algorithm Overview
The algorithm recursively chooses an unassigned variable, then iterates through the values in its domain. For each value, it adds the assignment `{var = value}` and checks for consistency, often through an inference procedure. If consistent, it recursively calls itself to assign the next variable. If the recursive call fails, or if the value is found to be inconsistent, it undoes the assignment and tries the next value for the current variable. The search terminates with a solution when an assignment is complete, or with failure if all possibilities have been exhausted.

## Key Components and Heuristics
The performance of backtracking search can be significantly improved by the choice of several functions. The `SELECT-UNASSIGNED-VARIABLE` function determines which variable to assign next (e.g., using a fail-first heuristic). The `ORDER-DOMAIN-VALUES` function decides the order in which to try values for a selected variable (e.g., using the least-constraining-value heuristic). The `INFERENCE` function can be used to propagate constraints (e.g., using Maintaining Arc Consistency) after each assignment to prune the search space.

## Relationships

- **is-a-type-of**: [[chronological-backtracking|Chronological Backtracking]]
- **is-an-improvement-on**: [[conflict-directed-backjumping|Conflict Directed Backjumping]]
- **uses**: [[least-constraining-value-heuristic|Least Constraining Value Heuristic]]
- **uses**: [[maintaining-arc-consistency|Maintaining Arc Consistency]]
- **solves**: [[constraint-satisfaction-problems|Constraint Satisfaction Problems]]
- **uses**: [[minimum-remaining-values-heuristic|Minimum Remaining Values Heuristic]]
- **is-a-specialization-of**: [[conflict-directed-backjumping|Conflict Directed Backjumping]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*