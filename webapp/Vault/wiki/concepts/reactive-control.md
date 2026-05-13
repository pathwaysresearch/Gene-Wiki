---
type: concept
aliases: [Reactive Control]
summary: A control methodology for robots that uses a reflex agent architecture, making low-level decisions in real-time based on direct sensor input without complex environmental models.
relationships:
  - target: three-layer-architecture
    type: component-of
  - target: robotic-software-architecture
    type: is-a-type-of
tags: [robotics, control-systems, agent-architecture]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Reactive Control

## Definition
Reactive control is a control strategy, often implemented in a reflex agent architecture, that is sensor-driven and suited for making low-level decisions in real time. It contrasts with model-based approaches that require constructing a reference path or potential field from a model of the environment.

## Rationale and Use Cases
This approach is particularly appropriate in situations where accurate models of the environment are difficult or impossible to obtain, such as on the surface of Mars or for robots with limited sensors. It is also valuable when computational complexity or localization errors make model-based techniques impractical. An example is a legged robot that uses a simple rule: if its leg encounters an obstacle while moving forward, it moves the leg back and tries again at a greater height, reacting directly to sensor feedback.

## Strengths and Weaknesses
Reactive control's primary strength is its ability to make rapid, low-level decisions based on immediate sensor data. However, its main weakness is that it rarely produces a plausible solution at a global level. Global control decisions often depend on information that cannot be sensed at the moment of decision-making, for which deliberative planning is more suitable.

## Relationships

- **component-of**: [[three-layer-architecture|Three Layer Architecture]]
- **is-a-type-of**: [[robotic-software-architecture|Robotic Software Architecture]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*