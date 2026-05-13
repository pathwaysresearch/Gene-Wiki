---
type: concept
aliases: [Heuristic Minimax]
summary: A version of the minimax algorithm that uses a heuristic evaluation function at a fixed search depth, which can lead to suboptimal choices due to evaluation errors.
relationships:
  - target: heuristic-evaluation-function
    type: uses
tags: [game-theory, adversarial-search, algorithm]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Heuristic Minimax

## Definition
Heuristic minimax is an application of the minimax algorithm where the search is cut off at a predefined depth, and a heuristic evaluation function is used to estimate the value of the leaf nodes in the resulting search tree. It selects what it believes to be the optimal move based on these heuristic evaluations, provided the leaf node evaluations are correct.

## Key Weakness
The primary weakness of heuristic minimax is its assumption that the leaf node evaluations are exactly correct. In reality, these evaluations are described as crude estimates that can have large errors. The algorithm's choice of move can be highly sensitive to these errors, potentially leading to a less reliable result than using the evaluation function directly on the initial moves.

## Impact of Evaluation Errors
The text provides an example where minimax suggests a move leading to a state with a value of 99 over a move leading to a state with a value of 100. It demonstrates that if the evaluation function has a random error with a standard deviation, the supposedly worse move can actually be better a majority of the time. This is because the "better" branch might have multiple nodes close to the maximum value, and an error in any one of them could lower the overall value of the branch.

## Non-Independent Errors
The problem is compounded by the fact that errors in evaluation functions are often not independent. If one node's evaluation is wrong, it is highly probable that nearby nodes in the tree are also evaluated incorrectly. This systematic bias can further mislead the minimax algorithm into making a poor choice.

## Relationships

- **uses**: [[heuristic-evaluation-function|Heuristic Evaluation Function]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*