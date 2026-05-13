---
type: concept
aliases: [Random Walk]
summary: An exploration strategy for unknown environments where the agent selects one of the available actions from the current state at random. While complete in finite spaces, it can be extremely inefficient.
relationships:
  - target: online-search-problem
    type: is-a-method-for
tags: [exploration-strategy, online-search, stochastic-method]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Random Walk

## Definition
A random walk is an online search strategy for exploring an environment. In its simplest form, the agent selects one of the available actions from its current state at random. A variation can give preference to actions that have not yet been tried from the current state to encourage more thorough exploration.

## Completeness
A random walk is guaranteed to eventually find a goal or complete its exploration, provided that the state space is finite. This property ensures that the agent will not be stuck forever and will eventually cover the reachable parts of the environment.

## Limitations and Inefficiency
Despite being complete, a random walk can be a very slow and inefficient exploration method. The topology of a state space can create "traps" where the agent is significantly more likely to move away from a goal than towards it. In such environments, a random walk can take an exponentially long time to find the goal, making it an impractical strategy for many real-world state spaces.

## Relationships

- **is-a-method-for**: [[online-search-problem|Online Search Problem]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*