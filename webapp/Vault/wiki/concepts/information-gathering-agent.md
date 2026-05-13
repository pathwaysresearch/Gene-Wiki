---
type: concept
aliases: [Information-Gathering Agent]
summary: An agent that intelligently decides whether to act based on current knowledge or to gather more information by weighing the expected utility gain against the cost of observation.
relationships:
  - target: value-of-perfect-information-vpi
    type: uses
tags: [agent-design, decision-making, active-learning]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Information-Gathering Agent

## Design and Operation
An information-gathering agent uses a decision network to model its environment and decisions. Before committing to a final action, it evaluates the potential benefit of acquiring new information about unobserved evidence variables by calculating the Value of Perfect Information (VPI) for each.

## Decision Criterion
The agent selects the observation that appears most efficient, maximizing the ratio of utility gain to cost, `VPI(E_j) / Cost(E_j)`. If the best observation's VPI is greater than its cost, the agent executes an action to request that information. If no observation is worth its cost, the agent selects the best "real" action based on its current knowledge.

## Myopic Control
The described algorithm implements a form of myopic information gathering. It is considered "myopic" or "shortsighted" because it calculates the value of acquiring only a single evidence variable at a time, rather than considering sequences of observations. Despite this greedy simplification, the text notes that this approach often works well in practice.

## Relationships

- **uses**: [[value-of-perfect-information-vpi|Value Of Perfect Information Vpi]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*