---
type: concept
aliases: [Open-World Assumption]
summary: The principle that the truth value of a statement not explicitly mentioned in a knowledge base is unknown, contrasting with the closed-world assumption where it would be considered false.
relationships:
  - target: sensorless-planning
    type: is-a-principle-of
  - target: belief-state
    type: underpins
tags: [knowledge-representation, logic, planning]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Open-World Assumption

## Definition
The open-world assumption is a logical principle used in planning under uncertainty. Under this assumption, if a fluent (a condition that can change over time) does not appear in a state description, its value is considered unknown. This is a necessary shift from the approach used in classical planning.

## Contrast with Closed-World Assumption
In classical planning, the closed-world assumption is made, meaning any fluent not mentioned in a state is assumed to be false. In sensorless and partially observable planning, this is replaced by the open-world assumption. This allows the system to handle uncertainty, where states contain both positive and negative fluents, and the absence of a fluent signifies a lack of knowledge about its truth value.

## Application in Belief States
The open-world assumption is fundamental to the concept of a belief state. A belief state represents a set of possible worlds, and the lack of information about a fluent means it could be true in some of those worlds and false in others. This is essential for planning when an agent lacks sensors and cannot resolve such uncertainties about the state of the world.

## Relationships

- **is-a-principle-of**: [[sensorless-planning|Sensorless Planning]]
- **underpins**: [[belief-state|Belief State]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*