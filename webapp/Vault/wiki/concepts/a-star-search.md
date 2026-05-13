---
type: concept
aliases: [A* Search]
summary: An informed search algorithm that finds the least-cost path from a start to a goal node by combining the cost to reach a node, g(n), with an estimated cost to the goal, h(n). A best-first graph search algorithm that finds the least-cost path from a given initial node to a goal node using a heuristic function to guide its search. A best-first graph traversal and path-finding algorithm, noted for its completeness and optimality.
relationships:
  - target: admissible-heuristic
    type: uses
  - target: consistent-heuristic
    type: uses
  - target: greedy-best-first-search
    type: is_a_type_of
  - target: iterative-deepening-a-star
    type: has_variant
  - target: simplified-memory-bounded-a-star
    type: has_variant
  - target: search-in-ai
    type: is_a_type_of
  - target: heuristic-function
    type: uses
  - target: traveling-salesperson-problem-tsp
    type: can_solve
  - target: best-first-search
    type: is_a
tags: [search-algorithm, informed-search, pathfinding, search-algorithms, heuristics, heuristic-search]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# A* Search

## Definition
A* search is a form of best-first search that evaluates nodes by combining g(n), the cost to reach the node, and h(n), the estimated cost to get from the node to the goal. The evaluation function is defined as f(n) = g(n) + h(n). The algorithm expands the node on the frontier with the lowest f(n) value.

## Properties and Optimality
A* search is both complete and optimal. The tree-search version of A* is optimal if its heuristic function, h(n), is admissible (never overestimates the true cost). The graph-search version is optimal if h(n) is consistent. Furthermore, A* is optimally efficient for any given consistent heuristic, meaning no other optimal algorithm that extends search paths from the root is guaranteed to expand fewer nodes than A*.

## Limitations
Despite its optimality and efficiency, A* is not a universal solution for all search problems. Its primary drawback is that for most problems, the number of states it must keep in memory is still exponential in the length of the solution. This can lead to the algorithm running out of memory on large problems, which motivates the development of memory-bounded heuristic search algorithms.

## Relationships

- **uses**: [[admissible-heuristic|Admissible Heuristic]]
- **uses**: [[consistent-heuristic|Consistent Heuristic]]
- **is_a_type_of**: [[greedy-best-first-search|Greedy Best First Search]]
- **has_variant**: [[iterative-deepening-a-star|Iterative Deepening A Star]]
- **has_variant**: [[simplified-memory-bounded-a-star|Simplified Memory Bounded A Star]]
- **is_a_type_of**: [[search-in-ai|Search In Ai]]
- **uses**: [[heuristic-function|Heuristic Function]]
- **can_solve**: [[traveling-salesperson-problem-tsp|Traveling Salesperson Problem Tsp]]
- **is_a**: [[best-first-search|Best First Search]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*