---
type: concept
aliases: [Voronoi Graph]
summary: A graph used in robot motion planning, consisting of points in the configuration space that are equidistant from two or more obstacles, which helps find paths with maximum clearance.
relationships:
  - target: configuration-space
    type: operates-on
  - target: probabilistic-roadmap
    type: alternative-to
tags: [robotics, motion-planning, path-planning, graph-methods]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Voronoi Graph

## Definition
In the context of robot motion planning, the Voronoi graph is defined as the set of all points in the configuration space that are equidistant to two or more obstacles.

## Application in Path Planning
This method reduces the continuous path-planning problem to a discrete search on the Voronoi graph. A path found by traversing the graph has the property of maximizing the clearance between the robot and nearby obstacles, as it follows the middle of the free space corridors.

## Limitations
The text highlights several disadvantages of using Voronoi graphs. They are difficult to apply in higher-dimensional configuration spaces, and the paths they generate can include unnecessarily large detours when the configuration space is wide and open. Furthermore, the complexity of obstacle shapes in configuration space makes computing the graph itself a difficult problem.

## Relationships

- **operates-on**: [[configuration-space|Configuration Space]]
- **alternative-to**: [[probabilistic-roadmap|Probabilistic Roadmap]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*