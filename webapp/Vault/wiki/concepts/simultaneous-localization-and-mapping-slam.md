---
type: concept
aliases: [Simultaneous Localization and Mapping (SLAM)]
summary: A class of problems and algorithms in robotics concerned with constructing a map of an unknown environment while simultaneously keeping track of the agent's location within it.
relationships:
  - target: occupancy-grid
    type: uses
  - target: shakey-the-robot
    type: related-to
tags: [robotics, perception, mapping, localization]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Simultaneous Localization and Mapping (SLAM)

## Overview
Simultaneous Localization and Mapping, commonly known as SLAM, is a fundamental problem in robotics. It addresses the challenge of an autonomous agent operating in an unknown environment, where it must build a consistent map of its surroundings while concurrently determining its own position within that map. The text identifies both localization and mapping as hard perceptual problems for robots.

## Historical Development
Research on the SLAM problem has evolved from two distinct origins. The first thread began in 1986 with work by Smith and Cheeseman, who first applied Kalman filters to the problem. This approach was later implemented by Moutarlier and Chatila and extended by others.

## Key Techniques
The second major thread in SLAM research began with the development of the occupancy grid representation for probabilistic mapping. This approach models the environment as a grid of cells, each with a probability of being occupied. A seminal 1997 paper by Lu and Milios advanced the field by recognizing the sparse nature of the SLAM problem, which spurred the development of efficient nonlinear optimization techniques.

## Relationships

- **uses**: [[occupancy-grid|Occupancy Grid]]
- **related-to**: [[shakey-the-robot|Shakey The Robot]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*