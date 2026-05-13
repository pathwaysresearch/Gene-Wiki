---
type: concept
aliases: [Visual Odometry]
summary: The process of estimating the change in position and orientation of a robot or vehicle over time using only the input from a camera.
relationships:
  - target: inertial-motion-unit
    type: is_complemented_by
tags: [robotics, computer-vision, navigation, localization]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Visual Odometry

## Definition
Visual odometry is the estimation of change in position based on visual data. It is a key technique for mobile robot navigation in various indoor and outdoor environments, addressing the problem of localizing the robot.

## Application in Robotics
This technique is used to solve the problem of localizing a robot within its environment. For example, a system can use two forward-looking cameras to track feature points in 3D, reconstructing the robot's position relative to the environment from the movement of these points over time.

## Enhancing Robustness
To improve reliability, visual odometry systems can be made more robust. One strategy is to use multiple camera systems, such as one looking forward and one looking back, to ensure that features are available even if one view is temporarily featureless (e.g., facing a blank wall). For further backup, visual odometry data can be combined with data from other sensors, like an Inertial Motion Unit (IMU), using probabilistic evidence fusion techniques such as Kalman filtering.

## Relationships

- **is_complemented_by**: [[inertial-motion-unit|Inertial Motion Unit]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*