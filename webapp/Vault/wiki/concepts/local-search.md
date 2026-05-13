---
type: concept
aliases: [Local Search]
summary: A class of search algorithms that explore a state-space landscape by iteratively moving from the current state to a neighboring state to find a solution.
relationships:
  - target: search-in-ai
    type: is_a_type_of
  - target: state-space
    type: operates_on
  - target: heuristic-function
    type: uses
tags: [search-algorithms, optimization, heuristics]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Local Search

## Definition
Local search algorithms are a class of methods that explore the state space by maintaining a single current state and iteratively moving to a neighboring state. Unlike path-based search algorithms, they are not concerned with the path taken to the current state. Their goal is to find a state that optimizes an objective function or heuristic cost.

## The State-Space Landscape
Local search is best understood through the metaphor of a state-space landscape. In this view, each state is a location on the landscape, and the objective or heuristic function defines the elevation. If the goal is to minimize cost, the algorithm seeks the lowest valley (a global minimum). If the goal is to maximize an objective, it seeks the highest peak (a global maximum). The landscape can contain challenging features like 'flat' local maxima or shoulders.

## Algorithm Properties
The performance of local search algorithms is evaluated based on completeness and optimality. A complete algorithm is one that always finds a goal if one exists. An optimal algorithm is one that is guaranteed to find a global minimum or maximum. Many simple local search methods, like hill-climbing, are not complete or optimal as they can get stuck in local optima.

## Relationships

- **is_a_type_of**: [[search-in-ai|Search In Ai]]
- **operates_on**: [[state-space|State Space]]
- **uses**: [[heuristic-function|Heuristic Function]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*