---
type: concept
aliases: [Topological Sort]
summary: A linear ordering of the nodes of a directed acyclic graph, used in CSPs to solve tree-structured problems efficiently without backtracking.
tags: [graph-algorithm, csp-solver, tree-structured-csp]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Topological Sort

## Definition
A topological sort is an algorithm that produces a linear ordering of the variables (nodes) in a tree-structured or directed acyclic graph. The ordering ensures that for any parent-child relationship, the parent variable appears before its child in the sequence.

## Application in CSPs
For tree-structured CSPs, performing a topological sort is the first step in a highly efficient, backtrack-free solution algorithm. The process begins by picking an arbitrary variable to be the root of the tree. Then, an ordering of the variables is chosen such that each variable appears after its parent in the tree.

## Solving Tree-Structured CSPs
Once a topological sort is established, the CSP can be made directed arc-consistent in O(nd^2) time. After this preprocessing step, the variables can be assigned values by simply iterating through them in the topological order. Because the graph is directed arc-consistent, any valid value choice for a parent variable guarantees that a valid value will exist for its children. This allows the algorithm to move linearly through the variables and find a solution without any need to backtrack.

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*