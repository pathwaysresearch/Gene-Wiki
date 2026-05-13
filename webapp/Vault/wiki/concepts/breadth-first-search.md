---
type: concept
aliases: [Breadth-First Search]
summary: An uninformed search algorithm that explores the search tree level by level, guaranteeing it finds the shallowest goal node. A fundamental graph traversal and search algorithm that explores neighbor nodes at the present depth prior to moving on to nodes at the next depth level.
relationships:
  - target: uniform-cost-search
    type: is-a-special-case-of
  - target: search-node
    type: uses
  - target: search-algorithm-complexity
    type: is-evaluated-by
tags: [uninformed-search, graph-search, algorithm, search-algorithm, graph-traversal]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Breadth-First Search

## How It Works
Breadth-first search explores a search tree by expanding the root node first, then all successors of the root, then their successors, and so on. It systematically explores all nodes at a given depth before moving on to the nodes at the next depth level. This strategy ensures that the shallowest goal node is found first.

## Properties
Breadth-first search is complete, meaning it will find a solution if one exists, provided the branching factor *b* is finite. It is also optimal if the path cost is a nondecreasing function of the depth of the node. The most common scenario where this holds is when all actions have the same cost.

## Complexity Analysis
The primary drawback of breadth-first search is its time and space complexity. For a solution at depth *d* in a tree with branching factor *b*, the total number of nodes generated is $O(b^d)$. The space complexity is also $O(b^d)$ because every generated node remains in memory, with $O(b^{d-1})$ nodes in the *explored* set and $O(b^d)$ nodes in the *frontier*.

## Relationships

- **is-a-special-case-of**: [[uniform-cost-search|Uniform Cost Search]]
- **uses**: [[search-node|Search Node]]
- **is-evaluated-by**: [[search-algorithm-complexity|Search Algorithm Complexity]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*