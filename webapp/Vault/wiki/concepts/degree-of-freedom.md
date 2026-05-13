---
type: concept
aliases: [Degree of Freedom (DOF)]
summary: An independent direction in which a robot or one of its components can move, used to abstractly describe its motion and shape capabilities.
tags: [robotics, kinematics, robot-motion]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Degree of Freedom (DOF)

## Definition
A degree of freedom (DOF) is a concept used to count each independent direction in which a robot, or one of its effectors, can move. This abstraction is fundamental to understanding the design of effectors, which are the parts of a robot that enable it to move and change its shape.

## Examples in Robotics
A rigid mobile robot, such as an Autonomous Underwater Vehicle (AUV), is described as having six degrees of freedom: three for its translational position in (x, y, z) space and three for its angular orientation, known as yaw, roll, and pitch. These six DOFs collectively define the robot's kinematic state or pose.

## Component-Level Degrees of Freedom
Nonrigid bodies and individual components also have their own degrees of freedom. For example, a human elbow has two DOFs (flexing and rotating), while a wrist has three (up-down, side-to-side, and rotation). Robot joints are similarly designed with one, two, or three degrees of freedom. To place an object, such as a hand, at a particular point in a particular orientation requires six degrees of freedom.

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*