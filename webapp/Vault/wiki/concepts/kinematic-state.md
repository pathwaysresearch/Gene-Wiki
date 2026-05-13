---
type: concept
aliases: [Kinematic State (Pose)]
summary: The location and angular orientation of a robot in space, defined by its available degrees of freedom.
relationships:
  - target: degree-of-freedom
    type: defined-by
  - target: dynamic-state
    type: component-of
tags: [robotics, kinematics, state-representation]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Kinematic State (Pose)

## Definition
The kinematic state of a robot, also referred to as its pose, describes its location and orientation. The term "kinematic" is derived from the Greek word for motion. It provides a snapshot of the robot's configuration without considering the forces or velocities involved.

## Relation to Degrees of Freedom
A robot's kinematic state is defined by its degrees of freedom (DOF). For a rigid mobile robot, the six degrees of freedom—three for position (x, y, z) and three for orientation (yaw, roll, pitch)—constitute its complete kinematic state.

## Distinction from Dynamic State
The kinematic state is a component of the robot's broader dynamic state. While the kinematic state describes the robot's position and orientation, the dynamic state includes this information plus the rate of change for each kinematic dimension, that is, their velocities.

## Relationships

- **defined-by**: [[degree-of-freedom|Degree Of Freedom]]
- **component-of**: [[dynamic-state|Dynamic State]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*