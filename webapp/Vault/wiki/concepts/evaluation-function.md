---
type: concept
aliases: [Evaluation Function]
summary: A function used in game-playing AI to estimate the expected utility or value of a non-terminal game position, enabling search cutoff.
relationships:
  - target: alpha-beta-pruning
    type: is-used-by
tags: [game-theory, heuristics, ai-in-games]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Evaluation Function

## Definition and Role
An evaluation function, also known as a heuristic evaluation function, returns an estimate of the expected utility of a game from a given position. In adversarial search, when the search is cut off at a certain depth before reaching a terminal state, the evaluation function is called to provide a score for the leaf nodes of the search. This allows the game-playing program to make decisions in complex games where searching to the end is infeasible.

## Design Principles
A good evaluation function must satisfy two key properties. First, it should order the terminal states in the same way as the true utility function, meaning winning states must evaluate higher than draws, which must be higher than losses. Second, the computation of the function must be fast, as it is called many times during a search.

## Feature-Based Implementation
Evaluation functions are typically designed as a weighted combination of various features of the game state. For chess, these features might include material advantage (e.g., a bishop is worth about three pawns), piece mobility, and board control. The text notes that modern programs often use nonlinear combinations of features, where the value of a piece or position can change depending on the context of the game (e.g., a bishop is worth more in the endgame). The weights for these features can be derived from centuries of human experience or estimated using machine learning techniques.

## Relationships

- **is-used-by**: [[alpha-beta-pruning|Alpha Beta Pruning]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*