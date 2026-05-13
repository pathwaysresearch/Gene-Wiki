---
type: concept
aliases: [Abstraction (in Problem Solving)]
summary: The process of simplifying a problem by removing irrelevant details from the representation of states and actions to make it computationally tractable.
relationships:
  - target: problem-formulation
    type: is-a-key-part-of
tags: [modeling, problem-solving, representation]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Abstraction (in Problem Solving)

## Definition
In the context of AI problem solving, abstraction is the process of removing detail from a representation to simplify it. It involves creating a model of the world that includes only the information necessary to solve the problem at hand. This is a critical step in problem formulation, as it reduces the complexity of the state space and the set of actions to consider.

## Application to States and Actions
Abstraction is applied to both state descriptions and actions. For states, irrelevant details are omitted; for example, a route-finding problem's state description might only include the agent's current city, ignoring factors like the current radio program or the weather. For actions, complex procedures are simplified into high-level commands. A driving action is abstracted to its start and end locations, ignoring the continuous process of steering or the side effects like fuel consumption.

## Importance
Abstraction is crucial for solving complex, real-world problems. Without it, the state space would be intractably large, and the number of possible low-level actions would be overwhelming. By focusing the agent on only the relevant aspects of the problem, abstraction allows search algorithms to find solutions in a reasonable amount of time.

## Relationships

- **is-a-key-part-of**: [[problem-formulation|Problem Formulation]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*