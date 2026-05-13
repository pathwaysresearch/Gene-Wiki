---
type: concept
aliases: [State-Space Search for Planning]
summary: A planning approach that searches through the space of possible world states, either forward from the initial state (progression) or backward from the goal (regression).
relationships:
  - target: partial-order-planning
    type: contrasted-with
tags: [planning, search-algorithms, ai]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# State-Space Search for Planning

## Overview
Planning can be framed as a search problem, where the planner is a program that searches for a solution path through a state space. This approach combines ideas from both search and logic, two major areas of AI. The states are explicit propositional or relational representations, which allows for the derivation of effective heuristics.

## Search Directions
State-space search for planning can operate in two primary directions. Forward search, or **progression**, starts from the initial state and applies actions to move forward toward the goal. Backward search, or **regression**, starts from the goal state and applies the inverse of actions to work backward toward the initial state.

## Heuristics and Historical Context
The practicality of state-space search for large planning problems was enabled by the development of effective heuristics, such as those derived from relaxing the planning problem (e.g., the ignore-delete-list heuristic). The resurgence of interest in this approach in the 1990s was pioneered by Drew McDermott's UNPOP program and further advanced by planners like Bonet and Geffner's Heuristic Search Planner (HSP).

## Relationships

- **contrasted-with**: [[partial-order-planning|Partial Order Planning]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*