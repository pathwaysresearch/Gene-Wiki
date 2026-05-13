---
type: concept
aliases: [Three-Layer Architecture]
summary: The most popular hybrid robotic software architecture, consisting of a reactive layer for low-level control, an executive layer for sequencing, and a deliberative layer for high-level planning.
relationships:
  - target: robotic-software-architecture
    type: is-a-type-of
  - target: reactive-control
    type: incorporates
tags: [robotics, software-architecture, hybrid-systems]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Three-Layer Architecture

## Overview
The three-layer architecture is the most popular type of hybrid architecture designed to combine reactive control with deliberation. It organizes a robot's software into three distinct, hierarchical layers: a reactive layer, an executive layer, and a deliberative layer.

## The Reactive Layer
The lowest level is the reactive layer, which provides low-level control to the robot. It is characterized by a very tight sensor-action loop, enabling it to respond to environmental stimuli with a decision cycle often on the order of milliseconds.

## The Executive Layer
The middle layer is the executive or sequencing layer, which serves as the glue between the reactive and deliberative layers. It receives high-level directives from the deliberative layer, such as a series of via-points from a path planner, and sequences them into commands for the reactive layer, deciding which specific reactive behavior to invoke. Its decision cycle is typically slower, around one second. This layer is also often responsible for integrating sensor information into an internal state representation, hosting functions like localization and online mapping.

## Relationships

- **is-a-type-of**: [[robotic-software-architecture|Robotic Software Architecture]]
- **incorporates**: [[reactive-control|Reactive Control]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*