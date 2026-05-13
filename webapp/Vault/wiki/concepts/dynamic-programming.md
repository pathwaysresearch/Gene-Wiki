---
type: concept
aliases: [Dynamic Programming]
summary: A method for solving problems by incrementally constructing solutions to subproblems from the solutions of smaller subproblems, often applied to graph search. A mathematical optimization method, developed by Richard Bellman, that provides the modern approach to solving sequential decision problems.
relationships:
  - target: richard-bellman
    type: developed_by
  - target: policy-iteration
    type: related_to
tags: [inference-method, search-algorithm, forward-chaining, optimization, sequential-decision-making, algorithms]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Dynamic Programming

## Definition
Dynamic programming is a problem-solving method in which the solutions to subproblems are constructed incrementally from those of smaller subproblems. In the context of logical inference, forward chaining on graph search problems is a direct application of this technique.

## Application in Inference
This method is particularly effective for tasks like finding paths in a graph. When applied via forward chaining, it systematically generates facts, such as `path(X,Y)`, building up solutions from known connections. This incremental construction avoids the redundant computations that can plague other methods like depth-first backward chaining.

## Efficiency
Dynamic programming, when implemented as forward chaining for graph problems, can be significantly more efficient than recursive backward-chaining approaches. For example, in a sample pathfinding problem from A₁ to J₄, a backward-chaining Prolog implementation performed 877 inferences, many of which were redundant. In contrast, the forward-chaining approach required only 62 inferences, as the number of `path` facts that can be generated is bounded by the square of the number of nodes.

## Relationships

- **developed_by**: [[richard-bellman|Richard Bellman]]
- **related_to**: [[policy-iteration|Policy Iteration]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*