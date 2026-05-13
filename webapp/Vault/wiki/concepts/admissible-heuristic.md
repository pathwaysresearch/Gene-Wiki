---
type: concept
aliases: [Admissible Heuristic]
summary: A heuristic function that never overestimates the cost of reaching the goal from a given node. This property is crucial for guaranteeing the optimality of search algorithms like A*.
relationships:
  - target: a-star-search
    type: is_a_requirement_for
  - target: relaxed-problem
    type: can_be_generated_by
  - target: pattern-database
    type: can_be_generated_by
  - target: consistent-heuristic
    type: is_implied_by
tags: [heuristic-function, search, optimality]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Admissible Heuristic

## Definition
An admissible heuristic is a function h(n) that provides an estimated cost from a node n to the goal, with the critical property that it never overestimates the true minimum cost. For any node n, the heuristic value h(n) must be less than or equal to the true cost of the cheapest path from n to the goal.

## Role in Search Algorithms
Admissibility is a key condition for guaranteeing the optimality of the A* tree-search algorithm. When A* uses an admissible heuristic, it can safely perform pruning—eliminating possibilities from consideration without having to examine them—while still guaranteeing that the first solution it finds will be an optimal one. For example, the heuristic h_SLD (straight-line distance) is mentioned as being admissible.

## Generation from Relaxed Problems
One systematic way to create admissible heuristics is by defining a relaxed problem, which is a version of the original problem with fewer restrictions on actions. The cost of an optimal solution in the relaxed problem is guaranteed to be an admissible heuristic for the original problem. For instance, the 'misplaced tiles' and 'Manhattan distance' heuristics for the 8-puzzle are admissible because they are the exact solution costs for relaxed versions of the puzzle.

## Relationships

- **is_a_requirement_for**: [[a-star-search|A Star Search]]
- **can_be_generated_by**: [[relaxed-problem|Relaxed Problem]]
- **can_be_generated_by**: [[pattern-database|Pattern Database]]
- **is_implied_by**: [[consistent-heuristic|Consistent Heuristic]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*