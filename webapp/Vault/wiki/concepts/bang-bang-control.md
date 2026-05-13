---
type: concept
aliases: [Bang-Bang Control]
summary: A control strategy where the control signal switches abruptly between two extreme states, such as full force left or full force right.
relationships:
  - target: cart-pole-problem
    type: is-used-in
tags: [control-theory, robotics, reinforcement-learning]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Bang-Bang Control

## Definition
Bang-bang control is a control regime where the actions applied to a system are discrete and typically represent the extreme ends of the control range. The text describes it in the context of the cart-pole problem.

## Application
In the cart-pole balancing problem, bang-bang control is the typical action regime. The actions are discrete choices such as "jerk left" or "jerk right," representing the application of maximum force in one direction or the other to control the cart's position.

## Context
This type of control is common in problems where the state variables are continuous, but the available actions are limited to a small, discrete set of maximal inputs. It simplifies the action space for learning algorithms.

## Relationships

- **is-used-in**: [[cart-pole-problem|Cart Pole Problem]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*