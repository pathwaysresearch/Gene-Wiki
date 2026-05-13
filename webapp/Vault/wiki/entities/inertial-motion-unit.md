---
type: entity
aliases: [Inertial Motion Unit (IMU)]
summary: An electronic device that measures a body's acceleration, used in robotics as a backup for vision-based navigation systems.
relationships:
  - target: visual-odometry
    type: complements
tags: [robotics, sensor, navigation, localization]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Inertial Motion Unit (IMU)

## Overview
An Inertial Motion Unit (IMU) is a sensor mechanism used in robotics and other fields to sense acceleration. The text likens its function to the mechanisms for sensing acceleration that humans have in their inner ears.

## Role in Robot Navigation
In mobile robotics, an IMU serves as a crucial backup for vision-based navigation systems like visual odometry. It provides an alternative source of motion data when the visual system fails, for example, when the robot passes through a featureless area like a dark shadow or a blank wall where visual tracking is impossible.

## How It Works
The IMU tracks changes in position by integrating the sensed acceleration twice. The data from the IMU can be combined with data from vision systems through probabilistic evidence fusion techniques, such as Kalman filtering, to produce a more robust and accurate estimate of the robot's position and movement.

## Relationships

- **complements**: [[visual-odometry|Visual Odometry]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*