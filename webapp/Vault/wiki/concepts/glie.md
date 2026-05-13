---
type: concept
aliases: [GLIE (Greedy in the Limit of Infinite Exploration)]
summary: A set of properties for exploration strategies in reinforcement learning that guarantees convergence to an optimal policy by ensuring sufficient exploration while eventually becoming greedy.
relationships:
  - target: exploration-vs-exploitation-dilemma
    type: is-a-solution-to
  - target: exploration-function
    type: is-an-implementation-of
tags: [reinforcement-learning, exploration, learning-theory]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# GLIE (Greedy in the Limit of Infinite Exploration)

## Definition

GLIE, or Greedy in the Limit of Infinite Exploration, is a technical property of a reasonable exploration scheme that will eventually lead to optimal behavior by a learning agent. It provides a formal way to balance the exploration-exploitation dilemma. A GLIE scheme must satisfy two specific conditions.

## Condition 1: Infinite Exploration

The first condition is that the scheme must try each action in each state an unbounded number of times. This ensures that the agent does not prematurely abandon an action that might be optimal simply because of an unusually bad initial series of outcomes. This guarantees that, in the limit, all actions are explored sufficiently.

## Condition 2: Eventual Greediness

The second condition is that the scheme must eventually become greedy. This means that as the agent gathers more and more experience, its policy should converge towards the one that is optimal with respect to its learned value estimates. This ensures that the agent eventually exploits the knowledge it has gained through exploration to maximize its reward.

## Relationships

- **is-a-solution-to**: [[exploration-vs-exploitation-dilemma|Exploration Vs Exploitation Dilemma]]
- **is-an-implementation-of**: [[exploration-function|Exploration Function]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*