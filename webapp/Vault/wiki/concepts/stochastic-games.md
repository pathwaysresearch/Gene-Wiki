---
type: concept
aliases: [Stochastic Games]
summary: Games that incorporate a random element, such as dice rolls, thereby combining elements of both luck and skill.
relationships:
  - target: monte-carlo-simulation-in-games
    type: can-be-analyzed-with
tags: [game-theory, game-types, probability]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Stochastic Games

## Definition
Stochastic games are games that include a random element, mirroring the unpredictability of many real-world situations. Unlike deterministic games like chess, the game tree for a stochastic game includes chance nodes in addition to the standard MIN and MAX nodes for the players. These chance nodes represent random events, such as the throwing of dice.

## Example
The text identifies Backgammon as a typical stochastic game that combines both luck and skill. At the beginning of a player's turn, dice are rolled, and the outcome determines the set of legal moves available to that player for that turn. This introduces an element of unpredictability that players must manage alongside strategic play.

## Search in Stochastic Games
Search algorithms like minimax can be extended to handle stochastic games. The analysis for MIN and MAX nodes remains the same, but chance nodes require a different approach. The value of a chance node is the average of the values of its children, weighted by their probabilities. The text notes that it is possible to prune chance nodes by establishing bounds on the utility function, which allows for calculating bounds on the average value of a chance node without needing to evaluate all of its children.

## Relationships

- **can-be-analyzed-with**: [[monte-carlo-simulation-in-games|Monte Carlo Simulation In Games]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*