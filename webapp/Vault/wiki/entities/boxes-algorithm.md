---
type: entity
aliases: [BOXES Algorithm]
summary: An early reinforcement learning algorithm by Michie and Chambers (1968) that solved the cart-pole problem by discretizing the continuous state space into 'boxes'.
relationships:
  - target: cart-pole-problem
    type: solves
  - target: function-approximation-in-reinforcement-learning
    type: is-an-example-of
tags: [reinforcement-learning, algorithm, control-theory, robotics]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# BOXES Algorithm

## Overview
The BOXES algorithm was developed by Michie and Chambers in 1968 to solve the cart-pole balancing problem. It was a pioneering system in reinforcement learning, notable for being implemented on a real physical cart and pole, not a simulation.

## How It Works
The algorithm's core mechanism, which gives it its name, is to first discretize the four-dimensional continuous state space of the cart-pole problem into a set of discrete regions or "boxes". It then ran trials, and when a failure occurred (the pole fell or the cart hit the end of the track), a negative reinforcement signal was associated with the final action taken in the final box. This negative signal was then propagated back through the sequence of states visited during the trial.

## Performance and Legacy
The BOXES algorithm was remarkably successful, able to balance the pole for over an hour after only about 30 trials. The text notes that the discretization of the state space could cause some problems depending on the initial position of the system. It is considered a reinforcement learning method with a function approximator.

## Relationships

- **solves**: [[cart-pole-problem|Cart Pole Problem]]
- **is-an-example-of**: [[function-approximation-in-reinforcement-learning|Function Approximation In Reinforcement Learning]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*