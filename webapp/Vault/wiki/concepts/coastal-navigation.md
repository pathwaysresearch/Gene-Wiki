---
type: concept
aliases: [Coastal Navigation]
summary: A robot navigation heuristic for partially observable environments that reduces uncertainty by requiring the robot to stay near known landmarks.
tags: [robotics, navigation, planning-under-uncertainty, heuristics]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Coastal Navigation

## Definition
Coastal navigation is a heuristic used in robotics to handle uncertainty in partially observable environments.

## Core Principle
The heuristic requires the robot to stay near known landmarks. By remaining in proximity to features with known locations, the robot can more accurately update its belief about its own position, thereby decreasing its uncertainty.

## Application
This approach serves as a practical strategy for controlling a robot when solving the underlying POMDP exactly is computationally infeasible, which is common in high-dimensional, continuous robotics problems. It makes the minimization of uncertainty an explicit control objective.

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*