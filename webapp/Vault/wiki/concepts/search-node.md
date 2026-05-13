---
type: concept
aliases: [Search Node]
summary: A data structure used in search algorithms to construct a search tree, containing the state, parent node, action taken, and path cost.
tags: [data-structure, search-algorithm, artificial-intelligence]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Search Node

## Definition
A search node is a fundamental data structure required by search algorithms to build and keep track of the search tree being constructed. Each node in the tree corresponds to a specific state in the problem's state space and contains various bookkeeping fields to facilitate the search process.

## Key Components
Each search node structure contains four primary components. `n.STATE` represents the state in the state space the node corresponds to. `n.PARENT` is a pointer to the node in the search tree that generated the current node. `n.ACTION` is the specific action that was applied to the parent's state to reach the current node's state. `n.PATH-COST`, traditionally denoted as g(n), is the total cost of the path from the initial state to the current node, as indicated by the parent pointers.

## Function in Search
The components of a parent node are used to compute the necessary components for a child node. The parent pointers are crucial as they allow for the reconstruction of the solution path once a goal node is found. By tracing back from the goal node to the root via the parent pointers, the sequence of actions that constitutes the solution can be determined.

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*