---
type: concept
aliases: [Conditional Effect]
summary: A feature in an action schema where the effect of an action depends on the state in which it is executed, specified using a "when condition: effect" syntax.
tags: [action-representation, planning, pddl]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Conditional Effect

## Definition
A conditional effect is a component of an action schema that allows an action's outcome to depend on the state of the world when the action is performed. It uses the syntax "when *condition*: *effect*," where the *condition* is a logical formula evaluated against the current state to determine if the *effect* is applied.

## Motivation and Use Case
Conditional effects are necessary when an action schema does not have the same effects for all states in which its preconditions are satisfied. For example, in the vacuum world, the *Suck* action's effect depends on the robot's location. The action schema would be `Action(Suck, EFFECT: when AtL: CleanL ∧ when AtR: CleanR)`, specifying that sucking cleans the left square if the robot is at the left, and the right square if it is at the right.

## Impact on Planning
The introduction of conditional effects complicates planning, particularly with belief states. When an action's effect depends on the state, it can introduce dependencies between fluents. This can break simplifying assumptions used in some planning algorithms, such as the preservation of a 1-CNF belief-state representation, which holds only when actions have uniform effects.

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*