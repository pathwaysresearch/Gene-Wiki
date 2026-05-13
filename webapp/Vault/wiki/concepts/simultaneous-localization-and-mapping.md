---
type: concept
aliases: [Simultaneous Localization and Mapping (SLAM)]
summary: The robotics problem of a robot building a map of an unknown environment while simultaneously keeping track of its own location within that map.
relationships:
  - target: localization
    type: solves-for
  - target: transition-model
    type: uses
  - target: sensor-model
    type: uses
tags: [robotics, robot-perception, state-estimation, mapping]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Simultaneous Localization and Mapping (SLAM)

## Definition
Simultaneous Localization and Mapping, abbreviated as SLAM, is a problem that arises when a robot must operate in an environment for which no map is available. The robot must concurrently acquire a map of its surroundings while determining its own location relative to this emerging map.

## The "Chicken-and-Egg" Problem
SLAM is characterized as a "chicken-and-egg problem" because its two constituent tasks, localization and mapping, are fundamentally codependent. To build an accurate map, the robot must know its precise location when taking sensor measurements. Conversely, to accurately determine its location, the robot needs a reliable map to reference.

## Solution Approaches
The SLAM problem is a subject of extensive study due to its importance in many robot applications. It is addressed using a variety of probabilistic techniques. One straightforward method mentioned for solving SLAM problems is the extended Kalman filter (EKF), which augments the state vector to include map features.

## Relationships

- **solves-for**: [[localization|Localization]]
- **uses**: [[transition-model|Transition Model]]
- **uses**: [[sensor-model|Sensor Model]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*