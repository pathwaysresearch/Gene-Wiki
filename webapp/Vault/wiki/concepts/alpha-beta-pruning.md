---
type: concept
aliases: [Alpha-Beta Pruning]
summary: A search algorithm that optimizes minimax search by eliminating branches of the game tree that cannot possibly influence the final decision. A search algorithm used in two-player deterministic games that optimizes minimax search by safely eliminating branches of the game tree that cannot influence the final outcome.
relationships:
  - target: minimax-search
    type: is-an-optimization-of
  - target: evaluation-function
    type: uses
  - target: horizon-effect
    type: is-limited-by
  - target: probcut
    type: is-related-to
  - target: expectimax-tree
    type: is-related-to
tags: [adversarial-search, game-theory, search-algorithm, optimization]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Alpha-Beta Pruning

## Definition and Purpose
Alpha-beta pruning is a search algorithm that seeks to decrease the number of nodes that are evaluated by the minimax algorithm in its search tree. It is an optimization technique that computes the correct minimax decision without looking at every node in the game tree. The algorithm stops evaluating a move when it has found a move that is proven to be worse than a previously examined move, thus pruning away branches that cannot possibly influence the final decision.

## Performance Improvement
Alpha-beta pruning can significantly improve search efficiency. With an optimal ordering of successor nodes (examining the best moves first), the algorithm only needs to examine O(b^(m/2)) nodes, effectively reducing the branching factor from *b* to the square root of *b*. This means alpha-beta can solve a tree roughly twice as deep as minimax in the same amount of time. With random move ordering, the performance is roughly O(b^(3m/4)).

## Dependence on Move Ordering
The effectiveness of alpha-beta pruning is highly dependent on the order in which successor states are examined. To achieve the best-case performance, it is crucial to examine the successors that are likely to be the best first. If the worst successors are generated first, little to no pruning may occur. In practice, even simple ordering functions, such as trying captures first in chess, can bring performance close to the best-case result.

## Relationships

- **is-an-optimization-of**: [[minimax-search|Minimax Search]]
- **uses**: [[evaluation-function|Evaluation Function]]
- **is-limited-by**: [[horizon-effect|Horizon Effect]]
- **is-related-to**: [[probcut|Probcut]]
- **is-related-to**: [[expectimax-tree|Expectimax Tree]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*