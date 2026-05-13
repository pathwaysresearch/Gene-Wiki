---
type: concept
aliases: [Relaxed Problem]
summary: A simplified version of a search problem with fewer restrictions on actions, used to mechanically generate admissible heuristics.
relationships:
  - target: admissible-heuristic
    type: is_a_method_for_generating
tags: [heuristic-function, problem-solving, search]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Relaxed Problem

## Definition
A relaxed problem is derived from an original problem by removing some of the restrictions on the available actions. The state-space graph of the relaxed problem is a supergraph of the original state space because removing restrictions adds new edges or paths between states.

## Generating Admissible Heuristics
The cost of an optimal solution to a relaxed problem serves as an admissible heuristic for the original problem. This is because any optimal solution in the original problem is also a valid, but not necessarily optimal, solution in the relaxed problem. The relaxed problem may have better solutions if the added actions create shortcuts, so its optimal solution cost will never be greater than the original problem's optimal solution cost.

## Examples
For the 8-puzzle, the 'misplaced tiles' heuristic (h1) is the exact solution cost for a relaxed problem where a tile can move from any square to any other square. The 'Manhattan distance' heuristic (h2) is the exact solution cost for a relaxed problem where a tile can move one square in any direction, even onto an occupied square.

## Relationships

- **is_a_method_for_generating**: [[admissible-heuristic|Admissible Heuristic]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*