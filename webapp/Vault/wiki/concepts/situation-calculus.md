---
type: concept
aliases: [Situation Calculus]
summary: A first-order logic formalism for representing and reasoning about actions and change in AI planning, where a situation represents a sequence of actions.
relationships:
  - target: pddl
    type: alternative-to
tags: [planning, formal-logic, knowledge-representation]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Situation Calculus

## Overview
Situation calculus is an approach to planning that frames the problem as one of first-order logical deduction. A solution is a situation, which corresponds to a sequence of actions, that satisfies the goal. This formalism has been crucial for defining the formal semantics of planning and has opened up new areas of investigation in the field.

## Expressiveness
Compared to languages like PDDL, the first-order logic of situation calculus offers greater expressiveness. It can use universal quantifiers to concisely express goals that are difficult in PDDL, such as moving an arbitrary number of items. It can also be used to express global constraints on a plan.

## Practical Limitations
Despite its formal power, there have not been any practical large-scale planning programs based on logical deduction over the situation calculus. This is partly due to the difficulty of performing efficient inference in first-order logic (FOL), but the primary reason is the lack of effective, specialized heuristics for planning within the situation calculus framework.

## Relationships

- **alternative-to**: [[pddl|Pddl]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*