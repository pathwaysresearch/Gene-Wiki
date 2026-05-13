---
type: concept
aliases: [Depth-First Search]
summary: An uninformed search algorithm that explores as deeply as possible along each branch before backtracking.
relationships:
  - target: depth-limited-search
    type: is-generalized-by
  - target: search-node
    type: uses
  - target: search-algorithm-complexity
    type: is-evaluated-by
tags: [uninformed-search, graph-search, algorithm]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Depth-First Search

## How It Works
Depth-first search always expands the deepest unexpanded node in the current frontier of the search tree. This behavior is achieved by using a LIFO (last-in, first-out) queue, or stack, to manage the frontier. A common alternative implementation uses a recursive function that calls itself on each of its children in turn, which naturally implements the LIFO expansion order.

## Properties and Limitations
The primary advantage of depth-first search is its modest memory requirement. However, it suffers from significant drawbacks. It is not optimal, as it may find a long solution path before a shorter one that exists elsewhere in the tree. More critically, it is not complete; it can get stuck in an infinite path in state spaces with loops or infinite depth and fail to find a solution even if one exists.

## Complexity Analysis
The time complexity of depth-first search is $O(b^m)$, where *m* is the maximum depth of any path in the state space, which can be much larger than the depth *d* of the shallowest solution. Its space complexity is its main strength, at only $O(bm)$, because it only needs to store a single path from the root to a leaf node and the unexpanded siblings along that path.

## Relationships

- **is-generalized-by**: [[depth-limited-search|Depth Limited Search]]
- **uses**: [[search-node|Search Node]]
- **is-evaluated-by**: [[search-algorithm-complexity|Search Algorithm Complexity]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*