---
type: concept
aliases: [Fluent]
summary: A property of the world that can change over time, represented in temporal logical formalisms by a proposition indexed by a time step.
tags: [temporal-logic, knowledge-representation, state-variable]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Fluent

## Definition

A fluent, derived from the Latin word *fluens* for "flowing," is an aspect of the world that changes over time. In the context of factored state representations, "fluent" is a synonym for "state variable."

## Logical Representation

To reason about change, fluents are represented by propositions that are indexed by a time step. For example, L_{x,y}^t can represent the proposition that an agent is in square [x,y] at time t. This distinguishes them from atemporal variables, which represent permanent aspects of the world (like the location of a pit) and do not require a time superscript.

## Examples in the Wumpus World

In the wumpus world logic, fluents are used to track dynamic conditions. Examples include the agent's location (L_{x,y}^t), its orientation (FacingEast^t), whether it still has its arrow (HaveArrow^t), and whether the wumpus is alive (WumpusAlive^t).

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*