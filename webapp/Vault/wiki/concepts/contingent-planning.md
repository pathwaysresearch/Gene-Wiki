---
type: concept
aliases: [Contingent Planning]
summary: A planning approach for non-deterministic or partially observable environments that creates plans with branches, allowing an agent to sense the world during execution and choose the appropriate path.
relationships:
  - target: sensorless-planning
    type: is-an-alternative-to
tags: [planning, uncertainty, robotics]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Contingent Planning

## Definition
Contingent planning is a method designed for domains that violate the assumptions of complete information and deterministic, fully observable environments. It produces plans that are not linear sequences of actions but rather contain branches to handle uncertainty.

## How It Works
A contingent plan allows the agent to sense the world during execution. Based on the information gathered through sensing, the agent decides which branch of the plan to follow. This makes the agent's behavior conditional on the actual state of the world as it is observed.

## Underlying Mechanism
The construction of contingent plans involves searching in the space of belief states. A belief state represents the set of all possible states the agent might be in, given its observations. Efficiently representing and computing these belief states is a key challenge in contingent planning.

## Relationships

- **is-an-alternative-to**: [[sensorless-planning|Sensorless Planning]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*