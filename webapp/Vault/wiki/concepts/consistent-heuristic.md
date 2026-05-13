---
type: concept
aliases: [Consistent Heuristic]
summary: A heuristic function that is not only admissible but also obeys a form of the triangle inequality, ensuring that f-costs along any path are nondecreasing.
relationships:
  - target: a-star-search
    type: is_a_requirement_for
  - target: admissible-heuristic
    type: is_a_stronger_form_of
tags: [heuristic-function, search, optimality]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Consistent Heuristic

## Definition
A heuristic h(n) is consistent if, for every node n and every successor n' of n, the estimated cost of reaching the goal from n is no greater than the step cost of getting to n' plus the estimated cost from n' to the goal. This property ensures that the f-values, f(n) = g(n) + h(n), are nondecreasing along any path from the start node.

## Role in A* Search
Consistency is the key property required to prove the optimality of the graph-search version of A*. When a heuristic is consistent, whenever A* selects a node n for expansion, it has already found the optimal path to that node. This mirrors the argument for the optimality of uniform-cost search.

## Relationship to Admissibility
Consistency is a stricter condition than admissibility. While most admissible heuristics developed in practice are also consistent, it is possible to have an admissible heuristic that is not consistent. In such cases, the A* algorithm may require extra bookkeeping to ensure optimality.

## Relationships

- **is_a_requirement_for**: [[a-star-search|A Star Search]]
- **is_a_stronger_form_of**: [[admissible-heuristic|Admissible Heuristic]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*