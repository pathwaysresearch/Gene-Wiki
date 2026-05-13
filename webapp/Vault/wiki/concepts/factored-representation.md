---
type: concept
aliases: [Factored Representation]
summary: A method for representing a state of the world as a collection of variables or fluents, commonly used in classical planning.
relationships:
  - target: pddl
    type: is_implemented_by
  - target: classical-planning
    type: is_used_in
tags: [planning, state-representation, knowledge-representation]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Factored Representation

## Definition
In the context of AI planning, a factored representation is a method for describing a state of the world by a collection of variables. This approach, adopted by planning researchers, contrasts with atomic representations where each state is treated as an indivisible whole.

## Implementation in PDDL
The Planning Domain Definition Language (PDDL) is a language that uses a factored representation. In PDDL, a state is represented as a conjunction of ground, functionless atoms called fluents. For example, a state in a delivery problem might be `At(Truck₁, Melbourne) ∧ At(Truck₂, Sydney)`.

## Semantics
This representation typically uses database semantics. The closed-world assumption means any fluent not mentioned in the state description is considered false. The unique names assumption means that distinct names like `Truck₁` and `Truck₂` refer to distinct objects.

## Relationships

- **is_implemented_by**: [[pddl|Pddl]]
- **is_used_in**: [[classical-planning|Classical Planning]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*