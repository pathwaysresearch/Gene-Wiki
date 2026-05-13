---
type: concept
aliases: [Occupancy Grid]
summary: A probabilistic representation used in robotic mapping where the environment is divided into a grid, and each cell stores the probability that it is occupied by an obstacle.
relationships:
  - target: simultaneous-localization-and-mapping-slam
    type: used-in
tags: [robotics, mapping, probabilistic-robotics]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Occupancy Grid

## Definition
An occupancy grid is a representation used for probabilistic mapping in robotics. In this model, the environment is discretized into a grid of cells, and each cell (e.g., at an (x, y) location) is assigned a probability value that represents the likelihood that the corresponding physical space is occupied by an obstacle.

## Historical Context
The occupancy grid representation was developed by Moravec and Elfes in 1985. Its creation marked one of the two primary historical threads in the evolution of robotic mapping techniques, providing a robust probabilistic framework for representing uncertain environmental data.

## Role in Mapping
This technique is a foundational method for solving the mapping problem and is a key component in some approaches to Simultaneous Localization and Mapping (SLAM). It contrasts with other mapping paradigms, such as topological mapping, which represents the environment as a graph of places and connections, or early SLAM methods that relied exclusively on Kalman filters.

## Relationships

- **used-in**: [[simultaneous-localization-and-mapping-slam|Simultaneous Localization And Mapping Slam]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*