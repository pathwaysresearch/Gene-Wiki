---
type: concept
aliases: [Joint Action]
summary: In a multi-actor setting, a joint action is a combination of individual actions taken simultaneously by all actors, represented as a tuple (a₁, ..., aₙ).
relationships:
  - target: decentralized-planning
    type: is-a-component-of
tags: [multi-agent-systems, planning, game-theory]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Joint Action

## Definition
A joint action is the fundamental concept of action in a multi-actor or multi-agent system. Instead of a single action `a`, the system's transition is determined by a joint action `(a₁, ..., aₙ)`, where `aᵢ` is the action selected by the `i`-th actor. All individual actions in the tuple are assumed to be executed simultaneously, with perfect synchronization.

## The Problem of Complexity
The introduction of joint actions dramatically increases the complexity of planning. If each of `n` actors has `b` possible individual actions, the total number of possible joint actions is `bⁿ`. This exponential growth in the branching factor of the search space makes the joint planning problem computationally challenging.

## Decoupling as a Solution
A principal focus of research in multi-actor planning is to decouple the actors as much as possible to mitigate the exponential complexity. If actors are loosely coupled or have no interaction with one another (e.g., n actors playing solitaire), the problem can be decomposed. The goal is to find methods where the complexity of the problem grows linearly with the number of actors, `n`, rather than exponentially.

## Relationships

- **is-a-component-of**: [[decentralized-planning|Decentralized Planning]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*