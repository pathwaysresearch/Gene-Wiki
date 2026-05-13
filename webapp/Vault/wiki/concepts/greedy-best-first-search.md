---
type: concept
aliases: [Greedy Best-First Search]
summary: A search algorithm that expands the node that is estimated to be closest to the goal, as determined by a heuristic function, without considering the cost of the path taken so far.
relationships:
  - target: a-star-search
    type: is_a_predecessor_to
tags: [search-algorithm, informed-search, heuristic-search]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Greedy Best-First Search

## How It Works
Greedy best-first search is an informed search algorithm that attempts to find a solution by always expanding the node that appears to be closest to the goal. It relies solely on a heuristic function, h(n), to estimate this proximity. For example, in a route-finding problem, it would expand the city with the shortest straight-line distance to the destination, regardless of the distance already traveled.

## Limitations and Incompleteness
The algorithm is not optimal and is also incomplete, even in finite state spaces. It can be misled by the heuristic and follow a path that is a dead end. As illustrated by the problem of getting from Iasi to Fagaras, the algorithm might expand Neamt because it is heuristically closest to the goal, but this is a dead end. The algorithm can then get stuck in an infinite loop by returning to a previous state (Iasi) that is still heuristically better than the correct next step (Vaslui).

## Complexity
The worst-case time and space complexity for the tree search version is O(b^m), where m is the maximum depth of the search space. However, the actual performance and the degree to which this complexity is reduced depends heavily on the quality of the heuristic function for the specific problem.

## Relationships

- **is_a_predecessor_to**: [[a-star-search|A Star Search]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*