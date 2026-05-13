---
type: concept
aliases: [Sensor Model]
summary: A model that specifies the probability of an agent receiving a particular percept, given the current state of the world. A probabilistic model in robotics, P(z_t+1 | X_t+1), that describes the probability of receiving a particular sensor measurement given the robot's current state.
relationships:
  - target: belief-state
    type: updates
  - target: transition-model
    type: used-with
  - target: localization
    type: used-by
tags: [agent-architecture, perception, state-estimation, robotics, probabilistic-robotics, robot-perception]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Sensor Model

## Definition
A sensor model specifies how an agent's evidence variables (i.e., its percepts) get their values. It describes the probability of receiving a particular sensor reading, given the actual state of the world. This model accounts for potential uncertainty or noise in the agent's sensors.

## Role in Belief State Update
The sensor model is the mechanism by which an agent incorporates new information from its environment. When a new percept is observed, the agent uses the sensor model to update its belief state. The probabilities of world states that are consistent with the percept are increased, while the probabilities of inconsistent states are decreased.

## Connecting State and Observation
In probabilistic reasoning over time, the sensor model provides the crucial link between the unobservable state of the world and the observable data an agent receives. It allows the agent to perform inference, reasoning from observed effects (percepts) back to hidden causes (the true state of the world).

## Relationships

- **updates**: [[belief-state|Belief State]]
- **used-with**: [[transition-model|Transition Model]]
- **used-by**: [[localization|Localization]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*