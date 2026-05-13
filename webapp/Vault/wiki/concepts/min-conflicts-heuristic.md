---
type: concept
aliases: [Min-Conflicts Heuristic]
summary: A local search heuristic for solving CSPs that iteratively selects a conflicted variable and chooses a new value that minimizes the number of conflicts.
tags: [local-search, heuristic, csp-solver, optimization]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Min-Conflicts Heuristic

## Definition
The min-conflicts heuristic is a greedy local search algorithm used for solving Constraint Satisfaction Problems. It operates on a complete, but likely invalid, assignment and tries to repair it by iteratively minimizing the number of violated constraints.

## How It Works
The algorithm begins with a complete, often random, assignment of values to all variables. It then repeats the following steps: first, randomly select a variable that is currently involved in a conflict. Second, reassign that variable a value that minimizes the number of conflicts with other variables. This process continues until a solution is found or a preset number of iterations is reached.

## Performance and Applications
Min-conflicts is surprisingly effective for many CSPs. For the n-queens problem, its run time is roughly independent of problem size, solving even the million-queens problem in an average of 50 steps. It has also been used for hard real-world problems, such as scheduling observations for the Hubble Space Telescope, where it reduced scheduling time from weeks to minutes. The search landscape often has plateaux, so allowing sideways moves (to states with the same score) can be beneficial.

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*