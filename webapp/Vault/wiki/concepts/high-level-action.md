---
type: concept
aliases: [High-Level Action (HLA)]
summary: An abstract action in hierarchical planning that can be refined into a sequence of more detailed actions, embodying knowledge about how to perform a complex task.
relationships:
  - target: hierarchical-planning
    type: is-a-component-of
  - target: angelic-semantics
    type: is-described-by
tags: [planning, abstraction, ai-concepts]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# High-Level Action (HLA)

## Definition
A High-Level Action (HLA) is a non-primitive action used in hierarchical planning that can be broken down into more specific, lower-level actions. HLAs embody knowledge about how to accomplish a task. For example, the HLA *Go(Home, SFO)* implies that valid methods include driving or taking a taxi, effectively pruning irrelevant actions like buying milk from the search space.

## Implementation and Refinement
An HLA is made concrete through a process of refinement. A refinement that consists entirely of primitive, executable actions is called an implementation of the HLA. For instance, the HLA *Navigate([1, 3], [3, 2])* in the vacuum world could have implementations like [*Right, Right, Down*] or [*Down, Right, Right*]. A high-level plan, which is a sequence of HLAs, is implemented by concatenating the implementations of each of its constituent HLAs.

## Goal Achievement Semantics
A high-level plan is considered to achieve a goal from a given state if at least one of its possible implementations achieves the goal from that state. This is a crucial aspect of its definition, as it grants the agent the choice of which implementation to execute. This principle is formalized through the concept of angelic semantics.

## Relationships

- **is-a-component-of**: [[hierarchical-planning|Hierarchical Planning]]
- **is-described-by**: [[angelic-semantics|Angelic Semantics]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*