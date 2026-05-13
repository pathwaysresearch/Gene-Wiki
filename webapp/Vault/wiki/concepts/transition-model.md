---
type: concept
aliases: [Transition Model]
summary: A model that describes the probability distribution of the state of the world at a future time, given its state at previous times. A probabilistic model in robotics, P(X_t+1 | x_t, a_t), that describes the probability of the robot's next state given its current state and the action taken.
relationships:
  - target: belief-state
    type: updates
  - target: markov-assumption
    type: relies-on
  - target: sensor-model
    type: used-with
  - target: localization
    type: used-by
tags: [dynamic-systems, probabilistic-models, state-estimation, robotics, probabilistic-robotics, bayesian-filtering]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Transition Model

## Definition
A transition model specifies how the world evolves over time. In a probabilistic framework, it describes the probability distribution of the world's state variables at time t, given the state of the world at all previous times from 0 to t-1, denoted as P(Xₜ | X₀:ₜ₋₁).

## Role in State Estimation
For an agent maintaining a belief state, the transition model is essential for prediction. It allows the agent to project its current belief state forward in time, calculating the probability distribution over possible states in the next time step before incorporating new sensor evidence.

## Dependence on the Markov Assumption
Because the set of previous states X₀:ₜ₋₁ grows unboundedly as time increases, a full transition model is often intractable. To solve this, these models typically make a Markov assumption, which posits that the current state depends on only a finite, fixed number of previous states, rather than the entire history.

## Relationships

- **updates**: [[belief-state|Belief State]]
- **relies-on**: [[markov-assumption|Markov Assumption]]
- **used-with**: [[sensor-model|Sensor Model]]
- **used-by**: [[localization|Localization]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*