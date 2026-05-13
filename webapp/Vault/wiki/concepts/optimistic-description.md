---
type: concept
aliases: [Optimistic Description]
summary: An approximation of a High-Level Action's reachable set that may overstate the set of possible outcomes, including all states that are possibly reachable.
relationships:
  - target: reachable-set
    type: is-an-approximation-of
tags: [planning, approximation, ai-theory]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Optimistic Description

## Definition
An optimistic description, denoted REACH⁺(s, h), is an approximation of the true reachable set of a High-Level Action (HLA) that is a superset of the actual reachable set. This means REACH(s, h) is a subset of REACH⁺(s, h). This description includes all states that might possibly be reached, even if some are not guaranteed.

## Purpose and Use
This type of approximation is necessary when the exact reachable set is too complex or infinite to compute precisely. For example, an optimistic description of the action *Go(Home, SFO)* might state that it possibly deletes *Cash* and possibly adds *At(Car, SFOLongTermParking)*, representing the union of outcomes from different implementations without enforcing their mutual exclusivity.

## Relation to Pessimistic Description
The optimistic description provides an upper bound on the possible outcomes of an HLA, in contrast to the pessimistic description (REACH⁻), which provides a lower bound. While it cannot be used to guarantee a solution, it can be useful for pruning branches of a search tree that have no possibility of reaching a goal.

## Relationships

- **is-an-approximation-of**: [[reachable-set|Reachable Set]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*