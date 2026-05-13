---
type: concept
aliases: [Dominant Strategy]
summary: In game theory, a strategy that yields a better outcome for a player than any other available strategy, regardless of the strategies chosen by the other players.
relationships:
  - target: dominant-strategy-equilibrium
    type: forms_basis_for
  - target: game-theory
    type: part_of
tags: [game-theory, decision-theory, strategy]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Dominant Strategy

## Definition
A dominant strategy is a core concept in game theory. A strategy is considered dominant for a player if it results in a better outcome for that player than any of their other strategies, for every possible choice of strategies by the other players. The text asserts that it is irrational for a player to play a strategy that is dominated by another, and it is also irrational not to play a dominant strategy if one exists.

## Strong vs. Weak Domination
The text distinguishes between two forms of domination. A strategy *s* **strongly dominates** another strategy *s'* if the outcome of choosing *s* is strictly better for the player than the outcome of choosing *s'*, regardless of what other players do. In contrast, a strategy *s* **weakly dominates** *s'* if *s* is better than *s'* for at least one combination of opponents' strategies and is never worse than *s'* for any other combination.

## Dominant Strategy Equilibrium
When every player in a game has a dominant strategy, the combination of these strategies is known as a **dominant strategy equilibrium**. This is a type of equilibrium where no player can benefit by unilaterally switching their strategy, given that every other player continues to play their dominant strategy. The text illustrates this with an example where both Alice and Bob have a dominant strategy to "testify," leading to an equilibrium where they both testify.

## Relationships

- **forms_basis_for**: [[dominant-strategy-equilibrium|Dominant Strategy Equilibrium]]
- **part_of**: [[game-theory|Game Theory]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*