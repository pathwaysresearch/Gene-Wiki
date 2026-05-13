---
type: concept
aliases: [Repeated Game]
summary: A type of multiple-move game where players face the same strategic choice repeatedly, with knowledge of the history of all players' previous choices.
tags: [game-theory, sequential-games]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Repeated Game

## Definition
A repeated game is the simplest form of a multiple-move game. In this structure, players confront the same decision-making scenario multiple times. Crucially, at each step, players are aware of the entire history of choices made by all participants in previous rounds.

## Strategies and Payoffs
A strategy profile for a repeated game is more complex than in a single-move game, as it must specify a player's action for every possible history of previous choices. Similar to Markov Decision Processes (MDPs), the payoffs in a repeated game are typically additive over time, meaning the total utility is the sum of the utilities from each round.

## Key Implications
The repeated nature of the game can fundamentally alter strategic considerations. For instance, in the repeated version of the prisoner's dilemma, the knowledge that players will interact again in the future can create incentives for cooperation (e.g., both refusing to testify) that do not exist in the single-move version.

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*