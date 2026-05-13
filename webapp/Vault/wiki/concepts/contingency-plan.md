---
type: concept
aliases: [Contingency Plan (Strategy)]
summary: A solution to a search problem in a nondeterministic or partially observable environment that specifies what action to take for different future percepts.
relationships:
  - target: and-or-graph-search
    type: is-generated-by
tags: [planning, search, nondeterminism, ai]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Contingency Plan (Strategy)

## Definition
A contingency plan, also known as a strategy, is a type of solution required when an agent operates in an environment that is nondeterministic or partially observable. Unlike a simple action sequence, a contingency plan specifies what the agent should do depending on the percepts it receives during execution. Because future percepts cannot be determined in advance, the agent's future actions must be conditional on them.

## Role in Nondeterministic Environments
In a nondeterministic environment, an agent's actions can have multiple possible outcomes. Percepts are crucial because they inform the agent about which outcome has actually occurred. The contingency plan must account for these different possibilities, providing a course of action for each potential result of an action. For example, in the erratic vacuum world, a `Suck` action might fail to clean the dirt, and the plan must specify what to do in that case.

## Contrast with Action Sequences
For problems in observable, deterministic, and fully known environments, the solution is a simple sequence of actions, such as `[Suck, Right, Suck]`. This is because the outcome of each action is predictable. However, when nondeterminism is introduced, a fixed sequence is no longer sufficient, as the agent must be prepared to react to unexpected outcomes. This necessitates the more complex, branching structure of a contingency plan, which can be found using algorithms like AND-OR search.

## Relationships

- **is-generated-by**: [[and-or-graph-search|And Or Graph Search]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*