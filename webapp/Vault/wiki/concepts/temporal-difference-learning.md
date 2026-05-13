---
type: concept
aliases: [Temporal-Difference Learning]
summary: A model-free reinforcement learning method that updates value estimates based on the difference between the current estimate and a new estimate derived from the immediate reward and the value of the next state. A class of model-free reinforcement learning methods that learn by bootstrapping from the current estimate of the value function. The text covers this topic on pages 836-838, 853, and 854.
relationships:
  - target: reinforcement-learning
    type: is-a-method-in
  - target: q-learning
    type: is-used-by
  - target: sarsa
    type: is-used-by
  - target: passive-reinforcement-learning
    type: is-a-method-for
tags: [reinforcement-learning, model-free, algorithm, machine-learning, algorithms]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Temporal-Difference Learning

## Core Principle

Temporal-difference (TD) learning methods work by adjusting utility or value estimates towards a local equilibrium. Instead of waiting until the end of an episode to update values, as in direct utility estimation, TD updates occur after each step. The update for a state's utility is based on the observed reward and the estimated utility of the observed successor state, rather than requiring a model of all possible successor states.

## Convergence

The TD update rule causes the agent's utility estimates to converge to the correct values over time. While a single rare transition might cause a large, seemingly improper change, the average value of the utility estimate will converge correctly because rare transitions occur infrequently. Convergence to the true value can be guaranteed if the learning rate parameter, α, is set to decrease as the number of times a state has been visited increases.

## Applications

TD learning is a foundational technique in reinforcement learning. It is the basis for the update rule in Q-learning, where it is used to update the action-utility Q(s,a) value. The Q-learning update is given by Q(s,a) ← Q(s,a) + α(R(s) + γ max_a' Q(s',a') - Q(s,a)). The algorithm SARSA is also a close relative that uses a similar TD-based update rule.

## Relationships

- **is-a-method-in**: [[reinforcement-learning|Reinforcement Learning]]
- **is-used-by**: [[q-learning|Q Learning]]
- **is-used-by**: [[sarsa|Sarsa]]
- **is-a-method-for**: [[passive-reinforcement-learning|Passive Reinforcement Learning]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*