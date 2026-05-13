---
type: concept
aliases: [Pruning]
summary: A general technique in AI and search algorithms for eliminating possibilities from consideration without having to examine them, significantly improving efficiency.
relationships:
  - target: a-star-search
    type: is_a_technique_used_by
tags: [search, optimization, algorithm-technique]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Pruning

## Definition
Pruning is the concept of eliminating possibilities from consideration without having to examine them. It is an important technique for making search in large state spaces tractable by cutting off entire subtrees of the search space that are guaranteed not to contain a solution or an optimal solution.

## Application in A* Search
In the context of A* search, pruning is enabled by the use of an admissible heuristic. For example, if the algorithm is exploring a path to the node Timisoara and its f-value (cost so far + admissible heuristic) is already greater than the cost of a known path to the goal, the algorithm can safely ignore, or prune, the entire subtree rooted at Timisoara. This is possible because the admissible heuristic guarantees that the true cost through that path cannot be any better than its current f-value.

## Significance
Pruning is a fundamental concept in many areas of AI. It allows algorithms to find optimal solutions much more efficiently by intelligently ignoring large portions of the search space. The effectiveness of an algorithm like A* is directly related to how much of the search space its heuristic allows it to prune.

## Relationships

- **is_a_technique_used_by**: [[a-star-search|A Star Search]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*