---
type: concept
aliases: [Depth-Limited Search]
summary: A modification of depth-first search that imposes a predetermined depth limit to avoid issues with infinite paths.
relationships:
  - target: depth-first-search
    type: is-a-modification-of
  - target: iterative-deepening-search
    type: is-used-by
  - target: search-node
    type: uses
  - target: search-algorithm-complexity
    type: is-evaluated-by
tags: [uninformed-search, graph-search, algorithm]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Depth-Limited Search

## Definition
Depth-limited search is a search strategy that alleviates the problem of infinite paths in depth-first search by supplying a predetermined depth limit, $\ell$. In this approach, nodes at depth $\ell$ are treated as if they have no successors, effectively cutting off the search at that level.

## Properties and Trade-offs
By imposing a depth limit, this search method solves the infinite-path problem inherent in standard depth-first search. However, this introduces a new source of incompleteness: if the shallowest goal is beyond the depth limit (i.e., $\ell < d$), the algorithm will fail to find a solution. Furthermore, if $\ell > d$, the search is not optimal, as it might find a solution at a greater depth before finding the shallowest one.

## Complexity Analysis
The time complexity of depth-limited search is $O(b^\ell)$, and its space complexity is $O(b\ell)$, where *b* is the branching factor and $\ell$ is the depth limit. Standard depth-first search can be viewed as a special case of depth-limited search where the limit $\ell$ is set to infinity.

## Relationships

- **is-a-modification-of**: [[depth-first-search|Depth First Search]]
- **is-used-by**: [[iterative-deepening-search|Iterative Deepening Search]]
- **uses**: [[search-node|Search Node]]
- **is-evaluated-by**: [[search-algorithm-complexity|Search Algorithm Complexity]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*