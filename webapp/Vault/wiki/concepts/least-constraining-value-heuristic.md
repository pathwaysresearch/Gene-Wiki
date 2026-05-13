---
type: concept
aliases: [Least-Constraining-Value Heuristic]
summary: A value-ordering heuristic for CSP solvers that prefers the value that rules out the fewest choices for neighboring variables. A heuristic for value ordering in CSP search that prefers the value that rules out the fewest choices for the neighboring variables in the constraint graph.
relationships:
  - target: backtracking-search
    type: is-used-by
  - target: backtracking-search
    type: enhances
  - target: constraint-satisfaction-problems
    type: applies-to
tags: [heuristic, csp-solver, search-strategy, search-algorithms, csp]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Least-Constraining-Value Heuristic

## Definition
The least-constraining-value heuristic is a strategy for ordering the domain values of a variable during a backtracking search. When deciding which value to try next for a selected variable, it advises choosing the value that leaves the maximum flexibility for subsequent variable assignments.

## Rationale
The heuristic prefers the value that rules out the fewest choices for the neighboring variables in the constraint graph. By leaving more options open for other variables, it increases the chances of finding a solution without having to backtrack. This is considered a "fail-last" strategy for value selection, which contrasts with "fail-first" strategies often used for variable selection. The goal is to pick a value that is likely to be part of a solution.

## Example
In a map coloring problem, suppose we are assigning a color to variable Q, which is a neighbor of SA. If choosing the color blue for Q would eliminate the last legal color available for SA, this would be a poor choice. The least-constraining-value heuristic would prefer a different color for Q, such as red, if that choice leaves SA with more available options.

## Relationships

- **is-used-by**: [[backtracking-search|Backtracking Search]]
- **enhances**: [[backtracking-search|Backtracking Search]]
- **applies-to**: [[constraint-satisfaction-problems|Constraint Satisfaction Problems]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*