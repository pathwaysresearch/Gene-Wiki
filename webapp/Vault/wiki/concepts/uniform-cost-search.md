---
type: concept
aliases: [Uniform-Cost Search]
summary: A search algorithm that expands the node with the lowest path cost (g(n)), guaranteeing it finds the cheapest solution.
relationships:
  - target: breadth-first-search
    type: is-a-generalization-of
  - target: search-node
    type: uses
  - target: search-algorithm-complexity
    type: is-evaluated-by
tags: [uninformed-search, graph-search, algorithm]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Uniform-Cost Search

## How It Works
Uniform-cost search expands nodes in order of their path cost from the root. It maintains a frontier of unexpanded nodes in a priority queue, ordered by the path cost, g(n). At each step, it selects the node with the lowest path cost from the frontier for expansion. This ensures that the first time it reaches a goal state, it has found the path with the minimum possible cost.

## Properties
Uniform-cost search is complete, provided the branching factor is finite and step costs are positive (greater than some small constant $\epsilon > 0$). It is also optimal, always finding the path with the lowest cost to a goal state. When all step costs are identical, uniform-cost search is equivalent to breadth-first search.

## Complexity Analysis
The complexity of uniform-cost search depends on the costs of the steps. If $C^*$ is the cost of the optimal solution and every action costs at least $\epsilon$, then the algorithm's worst-case time and space complexity is $O(b^{1+\lfloor C^*/\epsilon \rfloor})$. This can be significantly larger than $O(b^d)$, as the algorithm may explore large subtrees of low-cost steps before finding a more direct, higher-cost path.

## Relationships

- **is-a-generalization-of**: [[breadth-first-search|Breadth First Search]]
- **uses**: [[search-node|Search Node]]
- **is-evaluated-by**: [[search-algorithm-complexity|Search Algorithm Complexity]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*