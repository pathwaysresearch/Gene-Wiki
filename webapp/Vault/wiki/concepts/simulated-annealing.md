---
type: concept
aliases: [Simulated Annealing]
summary: An optimization algorithm that combines hill-climbing with a random walk to escape local optima by occasionally accepting "downhill" moves with a probability that decreases over time.
relationships:
  - target: optimization-algorithm
    type: is_a
  - target: boltzmann-machine
    type: related_to
  - target: hill-climbing-search
    type: is-an-improvement-on
tags: [local-search, optimization, stochastic-algorithm]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Simulated Annealing

## Definition
Simulated annealing is a local search algorithm designed to find a global optimum by combining the efficiency of hill-climbing with the completeness of a random walk. It is inspired by the metallurgical process of annealing, where a material is heated to a high temperature and then gradually cooled to allow it to reach a low-energy crystalline state. The algorithm aims to escape local minima by sometimes accepting moves that worsen the current state's cost.

## How It Works
The algorithm operates similarly to gradient descent (minimizing cost) but with a key difference: it allows for "bad" moves to states with higher cost. The probability of accepting such a move is controlled by a "temperature" parameter. Initially, the temperature is high, making it likely that the search will bounce out of local minima, analogous to shaking a surface hard to dislodge a ball. As the search progresses, the temperature is gradually lowered, reducing the probability of accepting bad moves and allowing the state to settle into a deep, hopefully global, minimum.

## Core Idea
The central concept of simulated annealing is to balance exploration and exploitation. By starting with a high temperature (intense shaking) and gradually reducing it, the algorithm can explore the state space broadly at first and then focus on refining the solution as it cools. This process addresses the incompleteness of standard hill-climbing algorithms, which never make downhill moves and can get permanently stuck on local maxima.

## Relationships

- **is-an-improvement-on**: [[hill-climbing-search|Hill Climbing Search]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*

---
*Also referenced in: Deep+Learning+Ian+Goodfellow*