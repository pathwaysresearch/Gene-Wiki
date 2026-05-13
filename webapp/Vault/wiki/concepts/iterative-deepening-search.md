---
type: concept
aliases: [Iterative Deepening Search]
summary: A search strategy that combines the space-efficiency of depth-first search with the completeness and optimality of breadth-first search by repeatedly running depth-limited searches with increasing depth limits.
relationships:
  - target: depth-limited-search
    type: uses
  - target: breadth-first-search
    type: combines-benefits-of
  - target: depth-first-search
    type: combines-benefits-of
  - target: search-node
    type: uses
  - target: search-algorithm-complexity
    type: is-evaluated-by
tags: [uninformed-search, graph-search, algorithm]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Iterative Deepening Search

## How It Works
Iterative deepening search is a strategy that repeatedly applies depth-limited search, incrementally increasing the depth limit. It starts with a limit of 0, then 1, then 2, and so on, performing a complete depth-first search up to the current depth limit at each iteration. This process continues until a goal is found.

## Properties and Advantages
This algorithm combines the key advantages of both breadth-first and depth-first search. Like breadth-first search, it is complete (if *b* is finite) and optimal when all step costs are identical because it explores a complete layer of new nodes at each iteration. Like depth-first search, its memory requirements are modest. For these reasons, iterative deepening is often the preferred uninformed search method when the search space is large and the depth of the solution is not known.

## Complexity Analysis
Although it seems wasteful to regenerate nodes in successive iterations, the overhead is not large. The total number of nodes generated is asymptotically the same as for a single breadth-first search, with a time complexity of $O(b^d)$. The space complexity, however, is only $O(bd)$, which is a significant improvement over the $O(b^d)$ space required by breadth-first search.

## Relationships

- **uses**: [[depth-limited-search|Depth Limited Search]]
- **combines-benefits-of**: [[breadth-first-search|Breadth First Search]]
- **combines-benefits-of**: [[depth-first-search|Depth First Search]]
- **uses**: [[search-node|Search Node]]
- **is-evaluated-by**: [[search-algorithm-complexity|Search Algorithm Complexity]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*