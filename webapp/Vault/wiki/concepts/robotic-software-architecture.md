---
type: concept
aliases: [Robotic Software Architecture]
summary: A methodology for structuring robotic algorithms, including languages, tools, and a philosophy for combining different control techniques like reactive and deliberative control.
relationships:
  - target: three-layer-architecture
    type: has-example
  - target: reactive-control
    type: incorporates
tags: [robotics, software-engineering, system-design]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Robotic Software Architecture

## Definition
A robotic software architecture is a methodology for structuring the algorithms that govern a robot's behavior. It encompasses the languages and tools used for programming, as well as an overarching philosophy for how different program components and control strategies are integrated.

## The Core Challenge
A central challenge for modern robotic software architectures is to effectively combine reactive control with model-based deliberative planning. These two paradigms have orthogonal strengths and weaknesses. Reactive control excels at low-level, real-time decisions driven by sensors, while deliberative planning is better for high-level, global problems that require information beyond immediate sensory input.

## The Hybrid Approach
Consequently, most contemporary robot architectures adopt a hybrid model. They use reactive techniques at the lower levels of control for immediate responses and deliberative techniques at the higher levels for strategic planning. An example of this combination is a system that uses a deliberative path planner to generate a route, which is then executed by a reactive PD controller that makes real-time adjustments.

## Relationships

- **has-example**: [[three-layer-architecture|Three Layer Architecture]]
- **incorporates**: [[reactive-control|Reactive Control]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*