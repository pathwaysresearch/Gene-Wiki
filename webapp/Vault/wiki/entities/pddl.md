---
type: entity
aliases: [PDDL (Planning Domain Definition Language)]
summary: A standardized language for expressing classical planning problems, defining the initial state, actions, and goals using a factored representation.
relationships:
  - target: factored-representation
    type: implements
  - target: blocks-world
    type: is_used_to_describe
  - target: classical-planning
    type: is_used_for
tags: [planning, language, knowledge-representation]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# PDDL (Planning Domain Definition Language)

## Overview
PDDL, the Planning Domain Definition Language, is a language used by planning researchers to express planning problems. It provides a factored representation that allows for the concise definition of complex domains and problems by describing a state as a collection of variables or fluents.

## Problem Definition Components
PDDL is used to describe the four key components of a search problem: the initial state (a conjunction of ground fluents), the available actions (defined by action schemas), the result of applying an action, and the goal test (a conjunction of fluents to be achieved). The text provides examples for an air cargo problem and the blocks world.

## State and Action Representation
States in PDDL are represented as a conjunction of ground, functionless atoms (fluents) under database semantics, including the closed-world and unique names assumptions. Actions are defined using schemas with a PRECOND list of fluents that must be true to execute the action, and an EFFECT list of fluents that are added or removed from the state. Time is handled implicitly, with preconditions referring to the state before the action and effects referring to the state after.

## Relationships

- **implements**: [[factored-representation|Factored Representation]]
- **is_used_to_describe**: [[blocks-world|Blocks World]]
- **is_used_for**: [[classical-planning|Classical Planning]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*