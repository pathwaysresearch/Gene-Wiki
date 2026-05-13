---
type: concept
aliases: [Localization]
summary: The fundamental robotics problem of determining the position of objects, and particularly the robot itself, within its environment.
relationships:
  - target: transition-model
    type: uses
  - target: sensor-model
    type: uses
  - target: simultaneous-localization-and-mapping
    type: sub-problem-of
tags: [robotics, robot-perception, state-estimation]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Localization

## Definition
Localization is the problem of finding out where things are. This encompasses determining the location of objects in the environment as well as, crucially, the robot's own position within that environment.

## Core Importance in Robotics
Knowledge of location is described as being at the core of any successful physical interaction a robot has with its environment. For example, a robot manipulator must know the location of an object it intends to manipulate, and a navigating robot must know its own location to successfully find its way around.

## Relation to Mapping
Localization is typically performed with respect to a map. In a simplified version of the problem, a robot is provided with an exact map and must determine its pose within it. When no map is available, the problem becomes significantly harder, leading to the challenge of simultaneous localization and mapping (SLAM).

## Relationships

- **uses**: [[transition-model|Transition Model]]
- **uses**: [[sensor-model|Sensor Model]]
- **sub-problem-of**: [[simultaneous-localization-and-mapping|Simultaneous Localization And Mapping]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*