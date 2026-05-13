---
type: concept
aliases: [Monte Carlo Simulation (in Games)]
summary: A technique for evaluating game positions, especially in stochastic games, by playing out thousands of random games to estimate the win percentage.
relationships:
  - target: stochastic-games
    type: is-a-technique-for
tags: [simulation, game-theory, ai-in-games, evaluation]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Monte Carlo Simulation (in Games)

## Definition
Monte Carlo simulation is presented as an alternative method for evaluating a game position within a search algorithm. Instead of using a static, feature-based evaluation function, this technique estimates a position's value by running a large number of randomized simulations.

## How It Works
From a given starting position, the algorithm plays thousands of games against itself to completion. For stochastic games like backgammon, these simulations incorporate random dice rolls. The value of the starting position is then approximated by the win percentage achieved across all these simulated games. This empirically derived value can then be used by a search algorithm like alpha-beta.

## Application
The text highlights the use of this technique for backgammon, stating that the resulting win percentage has been shown to be a good approximation of the true value of a position. This method is particularly effective in games where creating an accurate static evaluation function is difficult but simulating random games is computationally feasible.

## Relationships

- **is-a-technique-for**: [[stochastic-games|Stochastic Games]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*