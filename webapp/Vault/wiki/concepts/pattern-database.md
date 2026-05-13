---
type: concept
aliases: [Pattern Database]
summary: A technique for creating a highly accurate admissible heuristic by pre-calculating and storing the exact solution costs for every instance of a subproblem.
relationships:
  - target: admissible-heuristic
    type: is_a_method_for_generating
tags: [heuristic-function, precomputation, search]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Pattern Database

## How It Works
The core idea behind pattern databases is to create a lookup table that stores the exact solution costs for every possible instance of a subproblem. For example, in the 15-puzzle, a pattern database could store the cost of solving just the subproblem of getting tiles 1, 2, 3, and 4 to their goal positions. During a search on the full puzzle, the heuristic value for a complete state is found by looking up the configuration of its relevant subproblem in this database.

## Construction
A pattern database is constructed by searching backward from the goal state of the subproblem and recording the cost of each new pattern encountered. While this initial search to build the database can be computationally expensive, its cost is amortized over the many subsequent problem instances that will use it as a heuristic.

## Combining Databases
Multiple pattern databases can be constructed for different, non-overlapping subproblems (e.g., one for tiles 1-2-3-4 and another for 5-6-7-8). The admissible heuristics from these separate databases can be combined by taking the maximum value among them for any given state. This combined heuristic is often much more accurate than simpler ones like Manhattan distance and can reduce the number of nodes generated in a search by orders of magnitude.

## Relationships

- **is_a_method_for_generating**: [[admissible-heuristic|Admissible Heuristic]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*