---
type: concept
aliases: [PD Control]
summary: A feedback control method, also known as proportional-derivative control, used in robotics to minimize error in path following by considering both the current deviation and its rate of change.
tags: [robotics, robot-control, control-theory, feedback-control]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# PD Control

## Definition
PD (proportional-derivative) control is a feedback control mechanism used to guide a robot along a specified path. The corrective force it applies is a function of both the proportional error (current deviation from the path) and the derivative of the error (the rate at which the deviation is changing).

## Comparison with Proportional Control
Simple proportional control, which applies a counterforce proportional only to the deviation, can cause a robot to oscillate violently around the desired path. This is because the robot's natural inertia causes it to overshoot the path after a correction is applied.

## Role of the Derivative Term
The derivative component in PD control acts as a damping force. By responding to the rate of change of the error, it anticipates and counteracts the tendency to overshoot, resulting in much smoother and more stable path following. The text illustrates this with a robot arm that follows a path closely with PD control but vibrates significantly with only proportional control.

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*