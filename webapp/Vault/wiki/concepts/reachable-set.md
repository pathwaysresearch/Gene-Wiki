---
type: concept
aliases: [Reachable Set]
summary: In hierarchical planning, the set of all possible outcome states that can be reached by executing any implementation of a High-Level Action (HLA) from a given initial state.
relationships:
  - target: angelic-semantics
    type: is-a-key-concept-in
  - target: optimistic-description
    type: can-be-approximated-by
  - target: pessimistic-description
    type: can-be-approximated-by
tags: [planning, state-space, ai-theory]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Reachable Set

## Definition
The reachable set for a High-Level Action (HLA) *h* from an initial state *s*, denoted REACH(s, h), is the complete set of states that can result from executing any one of the possible implementations of *h*. This concept is fundamental to defining the effects of abstract actions under angelic semantics, as it captures the full range of possible outcomes available to the agent.

## Approximations for Complex Sets
In many practical scenarios, an HLA may have infinitely many implementations or produce a complex, "wiggly" set of states that is difficult to describe exactly. To manage this complexity, the reachable set is often approximated. An optimistic description (REACH⁺) overstates the set (a superset), while a pessimistic description (REACH⁻) understates it (a subset).

## Role in Hierarchical Planning
The reachable set is used by hierarchical planners to reason about the effects of high-level plans. A plan is deemed successful if its final reachable set intersects with the goal states. Planning algorithms like `ANGELIC-SEARCH` specifically use the pessimistic description (REACH⁻) to find guaranteed solutions, as any state within this set is definitely achievable.

## Relationships

- **is-a-key-concept-in**: [[angelic-semantics|Angelic Semantics]]
- **can-be-approximated-by**: [[optimistic-description|Optimistic Description]]
- **can-be-approximated-by**: [[pessimistic-description|Pessimistic Description]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*