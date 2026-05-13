---
type: concept
aliases: [Uninformed Search]
summary: A class of search algorithms that only have access to the problem definition and do not use any extra information about the state or search space.
relationships:
  - target: search-in-ai
    type: is_a_type_of
tags: [search-algorithms, graph-theory]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Uninformed Search

## Definition
Uninformed search methods, also known as blind search, are a category of search algorithms that operate using only the information available in the problem definition. This includes the initial state, the set of actions, the transition model, the goal test, and the path cost function. They do not use any domain-specific knowledge or heuristics to estimate how close a state is to the goal.

## Strategy
These algorithms systematically explore the state space according to a predetermined strategy, without any preference for nodes that might seem more promising. The order in which nodes are expanded is fixed by the algorithm's design. Because they lack guidance, they can be very inefficient in large state spaces.

## Example Algorithm
The text provides breadth-first search as a basic example of an uninformed search algorithm. Breadth-first search operates by expanding the shallowest unexpanded nodes in the search tree first. This strategy guarantees that it will find the shallowest goal, which is the optimal solution if all step costs are equal.

## Relationships

- **is_a_type_of**: [[search-in-ai|Search In Ai]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*