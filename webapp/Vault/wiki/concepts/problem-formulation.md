---
type: concept
aliases: [Problem Formulation]
summary: The process of defining a problem for a search algorithm by specifying its initial state, actions, transition model, goal test, and path cost.
relationships:
  - target: problem-solving-agent
    type: is-used-by
  - target: abstraction-in-problem-solving
    type: relies-on
tags: [problem-solving, search, modeling]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Problem Formulation

## Definition
Problem formulation is the process of defining a problem in a way that a computational search algorithm can solve it. It involves creating a formal structure that abstracts the key elements of a real-world situation. A well-defined problem provides the necessary components for a problem-solving agent to find a solution.

## Core Components
A complete problem formulation includes several key parts. It specifies the initial state the agent starts in. It defines the set of possible actions available to the agent in a given state, `ACTIONS(s)`. It includes a transition model, specified by a function `RESULT(s, a)`, which returns the successor state that results from performing action `a` in state `s`. It also has a goal test to determine if a state is a goal state, and a path cost function that assigns a numerical cost to a sequence of actions.

## Role of Abstraction
Effective problem formulation relies heavily on abstraction, the process of removing irrelevant detail. For example, in a route-finding problem, the state is abstracted to just the current location, like `In(Arad)`, ignoring details such as the weather or scenery. Actions are also abstracted, such as `Go(Sibiu)`, rather than low-level commands like 'turn steering wheel'. This simplification is essential to make complex problems computationally tractable.

## Relationships

- **is-used-by**: [[problem-solving-agent|Problem Solving Agent]]
- **relies-on**: [[abstraction-in-problem-solving|Abstraction In Problem Solving]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*