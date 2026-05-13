---
type: concept
aliases: [Constraint Satisfaction Problems (CSPs)]
summary: A class of problems represented by a set of variables, each with a possible domain of values, and a set of constraints specifying allowable combinations of values.
relationships:
  - target: backtracking-search
    type: solved-by
  - target: tree-decomposition
    type: solved-by
tags: [problem-solving, search-algorithms, ai]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Constraint Satisfaction Problems (CSPs)

## Definition
Constraint Satisfaction Problems (CSPs) are a type of problem where the goal is to find a state that satisfies a number of constraints. A CSP is defined by a set of variables, a domain of possible values for each variable, and a set of constraints that specify allowable combinations of values for subsets of variables. Many significant real-world problems can be formulated as CSPs.

## Problem Structure and Complexity
The complexity of solving a CSP is strongly related to the structure of its constraint graph. Problems whose constraint graphs have a tree structure are notable because they can be solved efficiently in linear time. For more complex, non-tree-structured problems, techniques such as cutset conditioning or tree decomposition can be used to transform or break down the problem into a more manageable form.

## Solution Methods
A common algorithm for solving CSPs is backtracking search, a form of depth-first search. This can be enhanced with various inference techniques (such as node, arc, and path consistency) that use constraints to prune the search space. Heuristics are also crucial for guiding the search. In addition to systematic search, local search methods using heuristics like min-conflicts have also been applied to CSPs with great success.

## Relationships

- **solved-by**: [[backtracking-search|Backtracking Search]]
- **solved-by**: [[tree-decomposition|Tree Decomposition]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*