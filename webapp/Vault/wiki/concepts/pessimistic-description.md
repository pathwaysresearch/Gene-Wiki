---
type: concept
aliases: [Pessimistic Description]
summary: An approximation of a High-Level Action's reachable set that may understate the set of possible outcomes, including only states that are definitely reachable.
relationships:
  - target: reachable-set
    type: is-an-approximation-of
tags: [planning, approximation, ai-theory]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Pessimistic Description

## Definition
A pessimistic description, denoted REACH⁻(s, h), is an approximation of the true reachable set of a High-Level Action (HLA) that is a subset of the actual reachable set. This means REACH⁻(s, h) is a subset of REACH(s, h). It includes only those states that are guaranteed to be reachable, regardless of which valid implementation is chosen.

## Role in Guaranteeing Solutions
The pessimistic description is critical for algorithms that need to find provably correct plans. If the pessimistic reachable set of a plan intersects with the goal set, it confirms that a solution is guaranteed to exist. The `ANGELIC-SEARCH` algorithm, for example, uses REACH⁻ to verify that a plan is guaranteed to succeed before committing to its decomposition.

## Relation to Optimistic Description
As a conservative, lower-bound estimate, the pessimistic description contrasts with the optimistic description (REACH⁺), which provides an upper bound. While a pessimistic approach might fail to identify some valid but non-guaranteed plans, any solution it finds is robust and certain to be achievable.

## Relationships

- **is-an-approximation-of**: [[reachable-set|Reachable Set]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*