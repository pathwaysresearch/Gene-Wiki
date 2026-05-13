---
type: concept
aliases: [Maximin]
summary: A technique developed by John von Neumann for finding the optimal mixed strategy in a two-player, zero-sum game by maximizing one's own minimum possible payoff.
relationships:
  - target: zero-sum-game
    type: is-a-method-for
tags: [game-theory, decision-theory, optimization]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Maximin

## Definition
The maximin technique is a method for determining the optimal mixed strategy for a player in a two-player, zero-sum game. The core principle is for a player (the maximizer) to choose a strategy that maximizes their payoff under the assumption that the other player (the minimizer) will always act to minimize that payoff.

## How It Works
The technique analyzes the game from the perspective of one player, designated E (the maximizer). E considers all possible mixed strategies, often represented by a probability `p` of choosing one action and `(1-p)` of choosing another. For each value of `p`, E calculates the expected payoff against each of O's (the minimizer's) possible pure strategies. Since O will always choose the action that results in the lowest payoff for E, E's actual expected payoff for a given `p` is the minimum of these calculated outcomes. E's optimal strategy is to choose the value of `p` that maximizes this minimum value, which typically occurs at the intersection point of the payoff lines for O's strategies.

## Application
The maximin method is applied to games that may not have a pure-strategy Nash equilibrium, such as two-finger Morra. By analyzing the expected payoffs graphically or algebraically, a player can find the precise mixed strategy (e.g., choosing "one" with probability p=7/12) that guarantees the best possible outcome against a perfectly rational opponent.

## Relationships

- **is-a-method-for**: [[zero-sum-game|Zero Sum Game]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*