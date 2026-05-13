---
type: concept
aliases: [Belief State]
summary: A representation of an agent's knowledge about the current state in a partially observable environment, defined as the set of all possible physical states the agent might be in. A representation of an agent's knowledge about the world, corresponding to the set of all possible physical states the agent might be in. A representation of an agent's knowledge about the possible current states of a partially observable environment, often expressed as a probability distribution over those states.
relationships:
  - target: partially-observable-problem
    type: is-central-to
  - target: state-estimation
    type: is-maintained-by
  - target: sensorless-planning
    type: is-a-component-of
  - target: open-world-assumption
    type: is-based-on
  - target: transition-model
    type: updated-by
  - target: sensor-model
    type: updated-by
tags: [state-representation, uncertainty, filtering, planning, agent-architecture, state-estimation, probabilistic-reasoning]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Belief State

## Definition
A belief state is the set of all physical states an agent believes it might currently be in, given the entire sequence of its past actions and percepts. It is the key concept required for solving partially observable problems, as the agent performs search and decision-making over these sets of states rather than over single, known physical states.

## Belief-State Space
The space of all possible belief states can be extremely large. If the underlying physical problem has N states, the corresponding belief-state space can contain up to 2^N belief states, since each belief state is a subset of the set of all physical states. In practice, many of these belief states may be unreachable from the agent's initial belief state, which often represents complete ignorance (the set of all N states).

## Belief State Updates
Belief states are maintained over time through a recursive update process that incorporates new information. This process consists of two main stages. First, a prediction step (`PREDICT(b, a)`) calculates the new belief state that results from taking an action `a` from the current belief state `b`. Second, an update step (`UPDATE(predicted_b, o)`) refines this predicted belief state by incorporating a new percept `o`, filtering out any states that are inconsistent with the observation. This recursive computation is a form of state estimation.

## Relationships

- **is-central-to**: [[partially-observable-problem|Partially Observable Problem]]
- **is-maintained-by**: [[state-estimation|State Estimation]]
- **is-a-component-of**: [[sensorless-planning|Sensorless Planning]]
- **is-based-on**: [[open-world-assumption|Open World Assumption]]
- **updated-by**: [[transition-model|Transition Model]]
- **updated-by**: [[sensor-model|Sensor Model]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*