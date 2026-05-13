---
type: concept
aliases: [Zero-Sum Game]
summary: A type of game in which two agents act alternately, and the utility values at the end of the game for the two players are always equal and opposite, meaning one player's gain is the other's loss. A type of game in which the sum of the payoffs for all players is always zero, meaning one player's gain is exactly equal to another player's loss.
relationships:
  - target: minimax-algorithm
    type: is-solved-by
  - target: maximin
    type: analyzed-by
tags: [game-theory, adversarial-search, multiagent-systems]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Zero-Sum Game

## Definition in AI
Within the context of AI, the most common type of game studied is the deterministic, turn-taking, two-player, zero-sum game of perfect information. This means the environment is fully observable, two agents act alternately, and the outcome is deterministic.

## Core Principle
The defining characteristic of a zero-sum game is that the utility values for the players at the conclusion of the game are always equal and opposite. For instance, if one player wins a game of chess, the other player necessarily loses. This opposition between the agents' utility functions is what makes the situation adversarial.

## Application in AI
Abstract games like chess are classic examples that fit this model. They are an appealing subject for AI researchers because their states are easy to represent and the actions are defined by precise rules, unlike more complex physical games.

## Relationships

- **is-solved-by**: [[minimax-algorithm|Minimax Algorithm]]
- **analyzed-by**: [[maximin|Maximin]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*