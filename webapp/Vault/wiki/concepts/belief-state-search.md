---
type: concept
aliases: [Belief-State Search]
summary: A search method for partially observable problems that operates in the space of belief states, where each node is a set of possible physical states.
relationships:
  - target: belief-state
    type: operates-on
  - target: partially-observable-problem
    type: solves
tags: [search-algorithm, planning, uncertainty]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Belief-State Search

## Problem Formulation
A partially observable problem can be solved by constructing a corresponding belief-state search problem. In this formulation, the states are belief states (sets of physical states). The initial state is the agent's initial belief state, which might be the set of all possible physical states if the agent starts with no information. The goal is to reach a belief state where all constituent physical states satisfy the goal test.

## Actions and Transitions
The set of actions available in a belief state `b` is typically the union of actions available in any of the physical states within `b`. The transition model is more complex than in physical state search. After an agent in belief state `b` executes an action `a`, the environment generates a percept `o`. The resulting belief state, `b_o`, is determined by predicting the outcome of the action and then updating with the percept. Because different percepts are possible, a single action can lead to multiple possible next belief states, making the search nondeterministic.

## Algorithmic Considerations
Standard search algorithms can be applied to the belief-state space by treating each belief state as an opaque, black-box node. However, this can be inefficient due to the size and complexity of belief states. A more advanced approach is to use incremental belief-state search algorithms that look inside the belief states to perform updates and transitions more efficiently, avoiding the need to represent them explicitly.

## Relationships

- **operates-on**: [[belief-state|Belief State]]
- **solves**: [[partially-observable-problem|Partially Observable Problem]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*