---
type: concept
aliases: [Minimax Algorithm]
summary: A recursive algorithm for choosing the optimal move in a two-player, zero-sum game by exploring the game tree to determine the move that minimizes the possible loss for a worst-case scenario.
relationships:
  - target: zero-sum-game
    type: is-used-for
tags: [adversarial-search, game-theory, decision-making]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Minimax Algorithm

## Purpose and Function
The minimax algorithm is designed to compute the optimal decision for a player from the current state in a two-player, zero-sum game. It identifies the move that maximizes the player's utility under the assumption that the opponent will play optimally to minimize it.

## How It Works
The algorithm performs a complete, depth-first exploration of the game tree. It uses a recursive computation that proceeds down to the terminal nodes (leaves) of the tree, where a utility function is applied to get a score. As the recursion unwinds, these values are "backed up" through the tree: at a player's turn (MAX node), the maximum value of the successor states is chosen; at an opponent's turn (MIN node), the minimum value is chosen.

## Complexity and Practicality
The time complexity of the minimax algorithm is O(b^m), where 'b' is the branching factor (number of legal moves) and 'm' is the maximum depth of the tree. This exponential complexity makes it impractical for real games with large game trees, such as chess. However, it serves as the fundamental basis for more practical game-playing algorithms.

## Relationships

- **is-used-for**: [[zero-sum-game|Zero Sum Game]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*