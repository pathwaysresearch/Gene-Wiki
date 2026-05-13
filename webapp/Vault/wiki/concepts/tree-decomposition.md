---
type: concept
aliases: [Tree Decomposition]
summary: A method for solving complex Constraint Satisfaction Problems by breaking the constraint graph into a tree of smaller, connected, and more easily solvable subproblems.
relationships:
  - target: constraint-satisfaction-problems
    type: is-a-method-for
tags: [graph-algorithms, csp, divide-and-conquer]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Tree Decomposition

## Definition
Tree decomposition is a divide-and-conquer approach for solving Constraint Satisfaction Problems. It involves transforming the problem's constraint graph into a tree structure composed of connected subproblems. The core idea is to solve each smaller subproblem independently and then combine the results.

## Key Requirements
A valid tree decomposition must satisfy three specific requirements. First, every variable in the original problem must appear in at least one subproblem. Second, any two variables connected by a constraint in the original problem must appear together in at least one subproblem. Third, if a variable appears in two separate subproblems within the tree, it must also be present in every subproblem along the path connecting them, which enforces value consistency across the decomposition.

## Application in Problem Solving
This technique is most effective when the original problem can be broken down into subproblems that are not excessively large. Once the decomposition is complete, each subproblem is solved. If any single subproblem is found to have no solution, it implies that the entire original problem is unsolvable. Otherwise, the partial solutions are combined to form a solution for the overall CSP.

## Relationships

- **is-a-method-for**: [[constraint-satisfaction-problems|Constraint Satisfaction Problems]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*