---
type: concept
aliases: [Heuristic Evaluation Function]
summary: A function used in game-playing AI to estimate the utility of a non-terminal game state, typically used when a search must be cut off due to computational limits.
tags: [game-theory, adversarial-search, ai]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Heuristic Evaluation Function

## Definition
A heuristic evaluation function is a function applied to a game state to produce an estimate of its utility or value. It is used in adversarial search algorithms when the search must be cut off at a certain depth, providing an evaluation for the leaf nodes of the partial search tree.

## Role in Adversarial Search
In games with large search spaces, it is often infeasible to search all the way to a terminal state. Algorithms need to cut the search off at some point and apply a heuristic evaluation function to the resulting leaf nodes. These evaluations are then propagated up the tree to help the algorithm choose the best move from the current state. For example, in the game of Go, it is noted that writing an effective evaluation function is difficult because control of territory is often unpredictable.

## Limitations and Challenges
The text emphasizes that these evaluations are often crude estimates and can have large errors associated with them. The error in the evaluation of one node is often not independent of its neighbors, meaning if one node is evaluated incorrectly, nearby nodes in the tree are also likely to be wrong. This can lead to suboptimal move choices when used with algorithms like heuristic minimax.

## Learning Evaluation Functions
A significant advancement in game-playing AI was the development of programs that could learn their own evaluation functions. Arthur Samuel's checkers program, developed from 1952, was a pioneer in this area, learning its function by playing against itself thousands of times and improving from a novice to a strong player.

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*