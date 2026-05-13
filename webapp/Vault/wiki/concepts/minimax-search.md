---
type: concept
aliases: [Minimax Search]
summary: A foundational search algorithm for two-player, zero-sum games that determines the optimal move by recursively minimizing the opponent's maximum gain.
relationships:
  - target: alpha-beta-pruning
    type: is-optimized-by
tags: [adversarial-search, game-theory, search-algorithm]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Minimax Search

## Core Concept
Minimax is a decision-making algorithm used in two-player adversarial games, such as chess or tic-tac-toe. It operates on a game tree to find the optimal move for a player, assuming that the opponent will also play optimally to maximize their own utility. The algorithm works by recursively exploring the game tree, with one player (MAX) trying to maximize the score and the other player (MIN) trying to minimize it.

## Primary Limitation
The main problem with minimax search is its computational complexity. As stated in the text, "the number of game states it has to examine is exponential in the depth of the tree." For a game with a branching factor of *b* and a search depth of *m*, the complexity is O(b^m), which makes it impractical for complex games like chess beyond a very shallow depth.

## Optimization
The primary optimization for the minimax algorithm discussed in the text is alpha-beta pruning. Alpha-beta pruning returns the exact same move as a full minimax search but achieves this by eliminating large parts of the game tree from consideration. This optimization can dramatically reduce the number of nodes that need to be evaluated.

## Relationships

- **is-optimized-by**: [[alpha-beta-pruning|Alpha Beta Pruning]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*