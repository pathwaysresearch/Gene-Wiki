---
type: concept
aliases: [Search Tree]
summary: A data structure representing the set of possible action sequences from an initial state, where nodes are states and branches are actions, used by search algorithms.
relationships:
  - target: problem-solving-agent
    type: is-used-by
tags: [search, data-structures, algorithms]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Search Tree

## Definition
A search tree is a structure formed by the possible action sequences an agent can take, starting from an initial state. The root of the tree is the initial state of the problem. The branches from any node in the tree represent the actions that can be taken in that node's state, and the children nodes correspond to the successor states that result from those actions.

## Generation and Exploration
Search algorithms build this tree dynamically during the search process. The process begins with the root node. An algorithm then repeatedly chooses a leaf node from the current tree (the 'frontier') and 'expands' it by generating all its successor nodes and adding them to the tree. This process continues until a node containing a goal state is found.

## Role in Finding Solutions
The search tree provides the conceptual framework for search algorithms to find a solution. A solution to the problem is a path from the root node (initial state) to a goal node. The sequence of actions corresponding to the branches along this path is the action sequence the agent must execute to achieve its goal. Algorithms like TREE-SEARCH and GRAPH-SEARCH are designed to systematically explore this tree.

## Relationships

- **is-used-by**: [[problem-solving-agent|Problem Solving Agent]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*