---
type: concept
aliases: [Problem Formulation (in AI)]
summary: The process of defining a search problem by specifying its five key components: initial state, actions, transition model, goal test, and path cost.
relationships:
  - target: search-in-ai
    type: is_prerequisite_for
  - target: state-space
    type: defines
tags: [problem-solving, modeling, ai-core-concepts]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Problem Formulation (in AI)

## Definition
Problem formulation is the essential first step in solving problems with search, and it must follow the formulation of a goal. It involves creating a well-defined, formal description of the problem that an algorithm can process. This process involves abstracting away real-world details to create a manageable model.

## Key Components
A complete problem formulation consists of five distinct parts. First is the initial state, which is where the agent begins. Second is a set of actions available to the agent in any given state. Third is a transition model, which describes the result of performing an action in a state. Fourth is a goal test function, which determines whether a given state is a goal state. Finally, a path cost function assigns a numerical cost to a sequence of actions, or path.

## Role in Search
These five components collectively define the problem's state space, which represents the environment. A search algorithm operates on this formal problem definition to find a solution, which is a path from the initial state to a goal state. The quality of the formulation can dramatically impact the size of the state space and, consequently, the difficulty of the search.

## Relationships

- **is_prerequisite_for**: [[search-in-ai|Search In Ai]]
- **defines**: [[state-space|State Space]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*