---
type: entity
aliases: [Cart-Pole Problem]
summary: A famous benchmark problem in reinforcement learning and control theory, also known as the inverted pendulum, which involves balancing a pole on a moving cart.
relationships:
  - target: bang-bang-control
    type: uses
  - target: boxes-algorithm
    type: solved-by
tags: [reinforcement-learning, control-theory, benchmark-problem, robotics]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Cart-Pole Problem

## Overview
The cart-pole problem, also known as the inverted pendulum, is a classic control problem that has been the subject of several thousand papers in reinforcement learning and control theory. The goal is to balance a pole upright on a cart that moves along a track.

## Problem Setup
The system is described by four continuous state variables: the position of the cart ($x$), the angle of the pole ($\theta$), the cart's velocity ($\dot{x}$), and the pole's angular velocity ($\dot{\theta}$). The objective is to apply forces to the cart to keep the pole roughly upright (e.g., $\theta \approx \pi/2$) while ensuring the cart stays within the physical limits of its track.

## Control and Learning
The actions are typically discrete, such as "jerk left" or "jerk right," a regime known as bang-bang control. Early work on learning to solve this problem was done by Michie and Chambers (1968) with their BOXES algorithm, which successfully balanced a real cart and pole.

## Relationships

- **uses**: [[bang-bang-control|Bang Bang Control]]
- **solved-by**: [[boxes-algorithm|Boxes Algorithm]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*