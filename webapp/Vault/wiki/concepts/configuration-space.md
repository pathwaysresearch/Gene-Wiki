---
type: concept
aliases: [Configuration Space]
summary: A representation used in robot motion planning where a robot's state is described by its joint angles or other configuration parameters, rather than Cartesian coordinates. An abstract space used in robot motion planning where each point represents a unique configuration of the robot, including its location, orientation, and all its joint angles.
tags: [robotics, motion-planning, state-representation, state-space]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Configuration Space

## Definition
A configuration space is a representation where the state of a robot is defined by the configuration of its joints, such as joint angles, instead of the Cartesian coordinates of its elements. For a robot arm with two joints, the configuration space is a two-dimensional space where each point corresponds to a unique pair of joint angles.

## Structure
The space is partitioned into free space, which contains all collision-free configurations, and occupied space, which represents configurations where the robot collides with an obstacle or with itself. Planning a path for the robot is equivalent to finding a path from a start to a goal configuration that lies entirely within the free space.

## Geometric Complexity
Even when a robot's physical workspace contains simple obstacles like flat polygons, the representation of these obstacles in configuration space can be highly complex, nonlinear, and even concave. This complexity is a central challenge in motion planning, as the shape of the free space can be non-obvious and difficult to compute directly.

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*