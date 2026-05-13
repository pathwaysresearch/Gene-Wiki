---
type: concept
aliases: [Online Search Problem]
summary: A type of search problem where an agent must physically execute actions to discover the environment's state space and outcomes, interleaving planning and action.
relationships:
  - target: random-walk
    type: is-solved-by-method
tags: [search-problem, robotics, exploration]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Online Search Problem

## Definition
An online search problem is one that must be solved by an agent executing actions in the world, rather than by pure computation with a known model. It involves an interleaving of planning and action. This contrasts with offline search, where an agent can compute a full solution before executing a single step. The canonical example is a robot exploring a new building to build a map.

## Agent's Limited Knowledge
In an online search problem, the agent is assumed to be in a deterministic and fully observable environment, but it does not know the transition model. The agent only knows the actions available in its current state, `ACTIONS(s)`; the cost of an action after it has been taken, `c(s, a, s')`; and how to test if a state is a goal, `GOAL-TEST(s)`. It cannot determine the result of an action, `RESULT(s, a)`, without actually performing it.

## Algorithmic Challenges
Because an online agent can only discover the successors of a state it physically occupies, it cannot jump around a search tree like an offline algorithm such as A*. This constraint means that online search algorithms should favor expanding nodes in a local order to avoid the high physical cost of traversing the environment simply to expand a distant node. Depth-first search is well-suited to this, as it expands a child of the previously expanded node.

## Relationships

- **is-solved-by-method**: [[random-walk|Random Walk]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*